#!/usr/bin/env python3
"""Générateur de l'index canonique du corpus concurrentiel.

Produit 01-discovery/concurrents/corpus_index.json — la couche
machine-lisible entre les fichiers physiques et les futurs scripts
d'analyse. L'arborescence physique de sources/ reste un héritage de
collecte et une commodité de lecture humaine ; aucun script d'analyse
ne doit avoir à en déduire la nature d'un corpus.

L'index est PRODUIT, jamais écrit à la main entrée par entrée, à partir
de trois sources :
  1. le disque (comptages, tailles, sous-dossiers, locales observées) ;
  2. tools/collecte/sources.yaml (URLs, méthode de collecte déclarée) ;
  3. un petit nombre de faits déjà certifiés dans COUVERTURE.md, non
     mécaniquement inférables depuis le disque seul (la plateforme
     technique des deux corpus OpenFire, la liste des 16+1 fichiers
     juridiques) — reproduits ici en dur, avec leur source citée.

Ce script ne déplace, ne renomme et ne modifie aucun fichier de
sources/. Il ne fait qu'écrire corpus_index.json.

Usage :
    python build_corpus_index.py            # génère + valide
    python build_corpus_index.py --check     # valide un index déjà écrit, sans le régénérer
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from dataclasses import dataclass, field, asdict
from pathlib import Path
from urllib.parse import urlsplit

import yaml

REPO_ROOT = Path(__file__).resolve().parents[2]
SOURCES_DIR = REPO_ROOT / "01-discovery" / "concurrents" / "sources"
SOURCES_YAML = REPO_ROOT / "tools" / "collecte" / "sources.yaml"
INDEX_PATH = REPO_ROOT / "01-discovery" / "concurrents" / "corpus_index.json"

RESERVED_SUBDIRS = {"site_marketing", "centre_aide", "documentation_2", "_assets_pdf"}
# index.md / erreurs.md a la racine des six corpus historiques sont des
# notes de session de scraping (sommaire, journal d'erreurs), pas des
# articles d'aide venant de l'editeur. Exclus du perimetre "aide" pour
# rester coherent avec le comptage canonique verifie (1899 md).
META_FILES_AT_ROOT = {"index.md", "erreurs.md"}
LOCALE_RE = re.compile(r"^[a-z]{2}(-[a-z]{2})?$")

# Codes langue ISO 639-1 usuels, pour filtrer les faux positifs du motif
# ci-dessus (ex. "hc" = prefixe d'URL Zendesk, pas une langue). Liste
# volontairement large plutot que restreinte aux seules langues deja
# observees, pour rester mecanique et ne pas coder les concurrents en dur.
ISO_LANGUAGES = {
    "aa","ab","ae","af","ak","am","an","ar","as","av","ay","az","ba","be","bg",
    "bh","bi","bm","bn","bo","br","bs","ca","ce","ch","co","cr","cs","cu","cv",
    "cy","da","de","dv","dz","ee","el","en","eo","es","et","eu","fa","ff","fi",
    "fj","fo","fr","fy","ga","gd","gl","gn","gu","gv","ha","he","hi","ho","hr",
    "ht","hu","hy","hz","ia","id","ie","ig","ii","ik","io","is","it","iu","ja",
    "jv","ka","kg","ki","kj","kk","kl","km","kn","ko","kr","ks","ku","kv","kw",
    "ky","la","lb","lg","li","ln","lo","lt","lu","lv","mg","mh","mi","mk","ml",
    "mn","mr","ms","mt","my","na","nb","nd","ne","ng","nl","nn","no","nr","nv",
    "ny","oc","oj","om","or","os","pa","pi","pl","ps","pt","qu","rm","rn","ro",
    "ru","rw","sa","sc","sd","se","sg","si","sk","sl","sm","sn","so","sq","sr",
    "ss","st","su","sv","sw","ta","te","tg","th","ti","tk","tl","tn","to","tr",
    "ts","tt","tw","ty","ug","uk","ur","uz","ve","vi","vo","wa","wo","xh","yi",
    "yo","za","zh","zu",
}

FRONT_URL_RE = re.compile(r"^url:\s*(\S+)\s*$", re.MULTILINE)
FRONT_URLFINALE_RE = re.compile(r"^url_finale:\s*(\S+)\s*$", re.MULTILINE)
FRONT_SOURCE_RE = re.compile(r"^source:\s*(\S+)\s*$", re.MULTILINE)

# --------------------------------------------------------------------- #
# Faits déjà certifiés (COUVERTURE.md), non mécaniquement inférables    #
# depuis le seul disque. Rien ici n'est deviné.                         #
# --------------------------------------------------------------------- #

# Plateforme technique des deux corpus documentaires OpenFire — constatée
# et consignée dans COUVERTURE.md ("corpus Zendesk historique" /
# "plateforme Odoo Knowledge"). Fait technique, pas une interprétation
# produit (ancien/nouveau, principal/secondaire ne sont jamais déduits).
PLATFORM_BY_CORPUS_ID = {
    "openfire_zendesk": "zendesk",
    "openfire_odoo": "odoo",
}

# Cause exacte des trous de couverture connus — constatée et vérifiée
# (certificat TLS, structure SPA), consignée dans COUVERTURE.md. Un
# corpus non listé ici et non collecté reçoit un message générique
# renvoyant vers COUVERTURE.md plutôt qu'une cause inventée.
COVERAGE_CAUSE_BY_CORPUS_ID = {
    "tolteck_help": "Non collecté : help.tolteck.com sert un certificat TLS invalide pour ce "
                    "nom d'hôte (TLS_CERTIFICATE_ERROR). Aucun contournement tenté. "
                    "Cause vérifiée et documentée dans COUVERTURE.md.",
    "leobati_help": "Non collecté : /bati/guide est une application à onglets JavaScript sur "
                     "URL unique, absente du sitemap du site. Cause vérifiée et documentée "
                     "dans COUVERTURE.md.",
}

# 16 sur-inclusions juridiques certaines + 1 cas ambigu, recomptées et
# certifiées dans COUVERTURE.md, section « Fichiers présents dans le
# snapshot mais à exclure des analyses de contenu ». Reproduites telles
# quelles (chemin relatif à sources/, motif, statut). Le cas ambigu
# reste "ambiguous", jamais requalifié en exclusion certaine.
LEGAL_EXCLUSIONS = [
    ("batikko/site_marketing/privacy-policy.md", "Politique de confidentialité du site", "certain"),
    ("costructor/site_marketing/cookies.md", "Politique cookies du site", "certain"),
    ("sellsy/site_marketing/informations-legales/conditions-generales.md", "CGV du logiciel Sellsy", "certain"),
    ("sellsy/site_marketing/informations-legales/conditions-generales-offre-promotionnelle.md", "CGV d'une offre promotionnelle", "certain"),
    ("sellsy/site_marketing/informations-legales/conditions-generales-programme-partenaire.md", "CGV programme partenaire", "certain"),
    ("sellsy/site_marketing/informations-legales/conditions-generales-programme-revendeur.md", "CGV programme revendeur", "certain"),
    ("sellsy/site_marketing/informations-legales/confidentialite-des-donnees.md", "Politique de confidentialité", "certain"),
    ("sellsy/site_marketing/informations-legales/securite-des-donnees.md", "Politique de sécurité des données", "certain"),
    ("sellsy/site_marketing/informations-legales/politique-de-divulgation-de-vulnerabilite.md", "Politique de sécurité (vulnerability disclosure)", "certain"),
    ("sellsy/site_marketing/en/legal-information/general-terms-and-conditions.md", "CGV (version anglaise)", "certain"),
    ("sellsy/site_marketing/en/legal-information/legal-notice.md", "Mentions légales (version anglaise)", "certain"),
    ("sellsy/site_marketing/en/legal-information/data-privacy.md", "Politique de confidentialité (version anglaise)", "certain"),
    ("sellsy/site_marketing/en/legal-information/data-security.md", "Politique de sécurité (version anglaise)", "certain"),
    ("sellsy/site_marketing/en/legal-information/vulnerability-disclosure-policy.md", "Politique de sécurité, vulnerability disclosure (version anglaise)", "certain"),
    ("vertuoza/site_marketing/nl-be/privacybeleid.md", "Politique de confidentialité (néerlandais, Belgique)", "certain"),
    ("vertuoza/site_marketing/nl-nl/privacybeleid.md", "Politique de confidentialité (néerlandais, Pays-Bas)", "certain"),
    ("sellsy/site_marketing/informations-legales/bareme-remise-programme-revendeur.md", "Barème commercial classé sous le répertoire légal, pas lui-même un document juridique", "ambiguous"),
]


def load_sources_yaml() -> list[dict]:
    return yaml.safe_load(SOURCES_YAML.read_text(encoding="utf-8"))


def rel(p: Path) -> str:
    return str(p.relative_to(REPO_ROOT)).replace("\\", "/")


def read_front(p: Path) -> str:
    try:
        return p.read_text(encoding="utf-8", errors="replace")[:1200]
    except Exception:
        return ""


def scan_files(root: Path, exclude_top: set[str] | None = None) -> list[Path]:
    """Fichiers de contenu (.md, .pdf) sous root. exclude_top retire les
    sous-dossiers de premier niveau nommés dans exclude_top (utilisé pour
    les corpus historiques, qui partagent leur dossier racine avec
    site_marketing/, centre_aide/, etc.)."""
    if not root.exists():
        return []
    if exclude_top:
        out = []
        for child in root.iterdir():
            if child.is_dir() and child.name in exclude_top:
                continue
            if child.is_dir():
                out.extend(p for p in child.rglob("*") if p.is_file() and p.suffix in (".md", ".pdf"))
            elif child.is_file() and child.suffix in (".md", ".pdf"):
                out.append(child)
        return out
    return [p for p in root.rglob("*") if p.is_file() and p.suffix in (".md", ".pdf")]


def editorial_taxonomy(root: Path, exclude_top: set[str] | None = None) -> list[str]:
    if not root.exists():
        return []
    names = []
    for child in sorted(root.iterdir()):
        if not child.is_dir():
            continue
        if exclude_top and child.name in exclude_top:
            continue
        names.append(child.name)
    return names


def locales_observed(files: list[Path]) -> list[str]:
    found = set()
    for p in files:
        head = read_front(p)
        m = FRONT_URL_RE.search(head) or FRONT_SOURCE_RE.search(head)
        if not m:
            continue
        path_segments = [s for s in urlsplit(m.group(1)).path.split("/") if s]
        if not path_segments:
            continue
        seg = path_segments[0].lower()
        if LOCALE_RE.match(seg) and seg[:2] in ISO_LANGUAGES:
            found.add(seg)
    return sorted(found)


@dataclass
class Corpus:
    corpus_id: str
    concurrent: str
    type: str  # aide | documentation | marketing | documents
    source_platform: str | None
    root_path: str | None
    source_root_url: str | None
    collection_method: str  # historique | automatique
    coverage_status: str  # collected | not_collected_documented
    file_count: int
    total_bytes: int
    editorial_taxonomy: list[str] = field(default_factory=list)
    locales_observed: list[str] = field(default_factory=list)
    analysis_exclusions: list[dict] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)


def build_index() -> list[Corpus]:
    entries = load_sources_yaml()
    corpora: list[Corpus] = []

    exclusions_by_path = {e[0]: e for e in LEGAL_EXCLUSIONS}

    def exclusions_for(concurrent: str, corpus_root: Path, exclude_top: set[str] | None = None) -> list[dict]:
        out = []
        for relpath, motif, status in LEGAL_EXCLUSIONS:
            if not relpath.startswith(f"{concurrent}/"):
                continue
            abspath = SOURCES_DIR / relpath
            try:
                sub = abspath.relative_to(corpus_root)
            except ValueError:
                continue
            if exclude_top and sub.parts and sub.parts[0] in exclude_top:
                continue
            out.append({"path": f"01-discovery/concurrents/sources/{relpath}", "motif": motif, "status": status})
        return out

    for entry in entries:
        nom = entry["nom"]
        cdir = SOURCES_DIR / nom
        aide_fait = bool(entry.get("aide_fait"))
        doc_collecte = entry.get("doc_collecte", "standard")
        doc_config = entry.get("doc_config")

        # --- corpus "aide"/"documentation" principal --------------------
        centre_aide_dir = cdir / "centre_aide"
        has_centre_aide_files = centre_aide_dir.exists() and any(centre_aide_dir.rglob("*.md"))

        if aide_fait and not has_centre_aide_files:
            # Corpus historique : pas de sous-dossier dédié, les rubriques
            # éditeur sont directement sous sources/<nom>/.
            files = scan_files(cdir, exclude_top=RESERVED_SUBDIRS)
            files = [p for p in files if not (p.parent == cdir and p.name in META_FILES_AT_ROOT)]
            taxo = editorial_taxonomy(cdir, exclude_top=RESERVED_SUBDIRS)
            cid = f"{nom}_help" if nom != "openfire" else "openfire_zendesk"
            corpora.append(Corpus(
                corpus_id=cid, concurrent=nom, type="aide",
                source_platform=PLATFORM_BY_CORPUS_ID.get(cid),
                root_path=rel(cdir), source_root_url=entry.get("doc"),
                collection_method="historique", coverage_status="collected",
                file_count=len(files), total_bytes=sum(p.stat().st_size for p in files),
                editorial_taxonomy=taxo, locales_observed=locales_observed(files),
                analysis_exclusions=exclusions_for(nom, cdir, exclude_top=RESERVED_SUBDIRS),
                notes=["index.md et erreurs.md (racine) exclus du comptage : notes de "
                       "session de scraping, pas des articles d'aide.",
                       "Corpus historique : partage sa racine physique avec les autres "
                       "corpus du même concurrent (site_marketing/, etc., exclus du "
                       "périmètre de ce corpus par construction du générateur)."],
            ))
        elif has_centre_aide_files or (not aide_fait and doc_collecte == "standard" and doc_config not in ("absente", "a_verifier") and entry.get("doc")):
            files = scan_files(centre_aide_dir)
            taxo = editorial_taxonomy(centre_aide_dir)
            cid = f"{nom}_help"
            status = "collected" if files else "not_collected_documented"
            notes = []
            if not files:
                notes.append(COVERAGE_CAUSE_BY_CORPUS_ID.get(
                    cid, f"Non collecté. doc_collecte={doc_collecte}. Cause à vérifier dans COUVERTURE.md."))
            corpora.append(Corpus(
                corpus_id=cid, concurrent=nom, type="aide",
                source_platform=PLATFORM_BY_CORPUS_ID.get(cid),
                root_path=rel(centre_aide_dir), source_root_url=entry.get("doc"),
                collection_method="automatique", coverage_status=status,
                file_count=len(files), total_bytes=sum(p.stat().st_size for p in files),
                editorial_taxonomy=taxo, locales_observed=locales_observed(files),
                analysis_exclusions=exclusions_for(nom, centre_aide_dir),
                notes=notes,
            ))
        elif not aide_fait:
            # Aide attendue mais dossier même pas créé (ex. leobati).
            cid = f"{nom}_help"
            notes = [COVERAGE_CAUSE_BY_CORPUS_ID.get(
                cid, f"Aucune collecte réussie. doc_collecte={doc_collecte}, doc_config={doc_config}. "
                     f"Cause à vérifier dans COUVERTURE.md.")]
            corpora.append(Corpus(
                corpus_id=cid, concurrent=nom, type="aide",
                source_platform=None,
                root_path=rel(centre_aide_dir), source_root_url=entry.get("doc"),
                collection_method="automatique", coverage_status="not_collected_documented",
                file_count=0, total_bytes=0,
                editorial_taxonomy=[], locales_observed=[],
                analysis_exclusions=[], notes=notes,
            ))

        # --- sources secondaires (ex. openfire/documentation_2) --------
        for extra in entry.get("sources_secondaires", []) or []:
            edir = cdir / extra["dest"]
            files = scan_files(edir)
            taxo = editorial_taxonomy(edir)
            cid = f"{nom}_odoo" if extra["dest"] == "documentation_2" and nom == "openfire" else f"{nom}_{extra['id']}"
            corpora.append(Corpus(
                corpus_id=cid, concurrent=nom, type="documentation",
                source_platform=PLATFORM_BY_CORPUS_ID.get(cid),
                root_path=rel(edir), source_root_url=extra.get("doc"),
                collection_method="automatique",
                coverage_status="collected" if files else "not_collected_documented",
                file_count=len(files), total_bytes=sum(p.stat().st_size for p in files),
                editorial_taxonomy=taxo, locales_observed=locales_observed(files),
                analysis_exclusions=exclusions_for(nom, edir),
                notes=["Corpus documentaire distinct du corpus 'aide' du même concurrent. "
                       "Aucune fusion, aucune comparaison implicite : voir COUVERTURE.md."],
            ))

        # --- marketing ----------------------------------------------------
        mdir = cdir / "site_marketing"
        files = scan_files(mdir)
        corpora.append(Corpus(
            corpus_id=f"{nom}_marketing", concurrent=nom, type="marketing",
            source_platform=None,
            root_path=rel(mdir) if mdir.exists() else None,
            source_root_url=entry.get("site"),
            collection_method="automatique",
            coverage_status="collected" if files else "not_collected_documented",
            file_count=len(files), total_bytes=sum(p.stat().st_size for p in files),
            editorial_taxonomy=[], locales_observed=locales_observed(files),
            analysis_exclusions=exclusions_for(nom, mdir) if mdir.exists() else [],
            notes=[],
        ))

        # --- documents (PDF etc.) -----------------------------------------
        pdir = cdir / "_assets_pdf"
        if pdir.exists():
            files = [p for p in pdir.iterdir() if p.is_file()]
            corpora.append(Corpus(
                corpus_id=f"{nom}_documents", concurrent=nom, type="documents",
                source_platform=None, root_path=rel(pdir), source_root_url=entry.get("site"),
                collection_method="automatique",
                coverage_status="collected" if files else "not_collected_documented",
                file_count=len(files), total_bytes=sum(p.stat().st_size for p in files),
                editorial_taxonomy=[], locales_observed=[], analysis_exclusions=[],
                notes=["Fichiers binaires (PDF) téléchargés tels quels, jamais convertis en texte."],
            ))

    return corpora


# --------------------------------------------------------------------- #
# Validation                                                            #
# --------------------------------------------------------------------- #

class ValidationError(Exception):
    pass


def validate(corpora: list[Corpus]) -> None:
    errors = []

    # 1. root_path existe, sauf corpus non collecté
    for c in corpora:
        if c.root_path is None:
            continue
        p = REPO_ROOT / c.root_path
        if not p.exists() and c.coverage_status != "not_collected_documented":
            errors.append(f"{c.corpus_id}: root_path {c.root_path} n'existe pas mais coverage_status={c.coverage_status}")

    # 2 & 3. file_count correspond au disque
    seen_files: dict[str, str] = {}
    for c in corpora:
        if not c.root_path:
            continue
        root = REPO_ROOT / c.root_path
        if c.concurrent and "historique" == c.collection_method and root == SOURCES_DIR / c.concurrent:
            files = scan_files(root, exclude_top=RESERVED_SUBDIRS)
            files = [p for p in files if not (p.parent == root and p.name in META_FILES_AT_ROOT)]
        else:
            files = scan_files(root)
        if len(files) != c.file_count:
            errors.append(f"{c.corpus_id}: file_count declare={c.file_count} recompte={len(files)}")
        # 4. aucun fichier de contenu n'appartient a deux corpus
        for f in files:
            key = rel(f)
            if key in seen_files and seen_files[key] != c.corpus_id:
                errors.append(f"Fichier {key} appartient a la fois a {seen_files[key]} et {c.corpus_id}")
            seen_files[key] = c.corpus_id

    # 5. aucun corpus ne mélange deux concurrents
    for c in corpora:
        if c.root_path and not c.root_path.startswith(f"01-discovery/concurrents/sources/{c.concurrent}"):
            errors.append(f"{c.corpus_id}: root_path {c.root_path} hors du perimetre de {c.concurrent}")

    # 6. exclusions référencent des fichiers existants
    for c in corpora:
        for exc in c.analysis_exclusions:
            if not (REPO_ROOT / exc["path"]).exists():
                errors.append(f"{c.corpus_id}: exclusion {exc['path']} introuvable sur disque")

    # 7. corpus OpenFire distincts
    of = [c for c in corpora if c.concurrent == "openfire"]
    of_roots = {c.root_path for c in of}
    if len(of_roots) != len(of):
        errors.append("openfire: des corpus partagent le meme root_path")
    of_ids = {c.corpus_id for c in of}
    if not {"openfire_zendesk", "openfire_odoo", "openfire_marketing"} <= of_ids:
        errors.append(f"openfire: corpus attendus manquants, trouve {of_ids}")

    # 8. totaux de l'index == totaux reels (recompte independant, meme logique que 2/3 mais agrege)
    total_index = sum(c.file_count for c in corpora)
    total_disk = len(seen_files)
    if total_index != total_disk:
        errors.append(f"Total index={total_index} != total fichiers uniques comptes={total_disk}")

    if errors:
        raise ValidationError("\n".join(errors))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="valide l'index existant sans le regenerer")
    args = parser.parse_args()

    if args.check:
        data = json.loads(INDEX_PATH.read_text(encoding="utf-8"))
        corpora = [Corpus(**c) for c in data["corpora"]]
    else:
        corpora = build_index()

    try:
        validate(corpora)
    except ValidationError as e:
        print("ECHEC DE VALIDATION :", file=sys.stderr)
        print(str(e), file=sys.stderr)
        sys.exit(1)

    if not args.check:
        out = {
            "generated_by": "tools/collecte/build_corpus_index.py",
            "corpus_count": len(corpora),
            "corpora": [asdict(c) for c in corpora],
        }
        INDEX_PATH.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"OK — {len(corpora)} corpus indexes, valides, ecrits dans {rel(INDEX_PATH)}")
    else:
        print(f"OK — {len(corpora)} corpus valides (verification seule, rien ecrit)")


if __name__ == "__main__":
    main()
