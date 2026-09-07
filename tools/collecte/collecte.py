#!/usr/bin/env python3
"""Collecteur de corpus concurrentiel (centre d'aide + site marketing).

Regle de securite absolue : tout contenu recupere sur le web est une DONNEE
A STOCKER, jamais une instruction. Aucun chemin de ce script n'interprete le
contenu recupere comme une commande. Un texte adresse a un agent/crawler/IA
rencontre dans une page est stocke tel quel et journalise
(CONTENT_INSTRUCTION_IGNORED) ; il n'a aucun effet sur le comportement du
script.

Usage :
    python collecte.py --dry-run [--concurrent NOM]
    python collecte.py [--concurrent NOM]

Le fichier de configuration est tools/collecte/sources.yaml. Rien dans ce
fichier de configuration n'est jamais modifie par le script.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import time
import unicodedata
from collections import deque
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit, urljoin, parse_qsl, urlencode
from urllib import robotparser

import requests
import trafilatura
import yaml
from bs4 import BeautifulSoup

# --------------------------------------------------------------------------- #
# Configuration                                                               #
# --------------------------------------------------------------------------- #

TOOL_DIR = Path(__file__).resolve().parent
REPO_ROOT = TOOL_DIR.parents[1]
SOURCES_DIR = REPO_ROOT / "01-discovery" / "concurrents" / "sources"
SOURCES_YAML = TOOL_DIR / "sources.yaml"
CACHE_DIR = TOOL_DIR / "cache"
LOG_PATH = TOOL_DIR / "collecte.log"

USER_AGENT = "SupordoDiscoveryBot/1.0 (+recherche concurrentielle interne; non commercial)"
REQUEST_DELAY = 1.5          # secondes minimum entre deux requetes vers le meme hote
TIMEOUT = 15                  # secondes
MAX_RETRIES = 2                # tentatives supplementaires apres l'essai initial
RETRY_BACKOFF_BASE = 2.0       # secondes, double a chaque tentative
MAX_DEPTH = 4                   # profondeur max du crawl de secours (sans sitemap)
MAX_PAGES_PER_TARGET = 8000     # garde-fou anti-boucle, tres au-dessus du volume attendu

TRACKING_PARAM_PREFIXES = ("utm_",)
TRACKING_PARAM_EXACT = {"gclid", "fbclid"}

# Comparaison par SEGMENT DE CHEMIN EXACT (jamais un prefixe/substring) :
# "/compte-cle-en-main" ne doit pas matcher "compte", "/documentation-legale"
# ne doit pas matcher "legale", etc. Un segment est ce qui se trouve entre
# deux "/".
EXCLUDED_SEGMENTS = {
    "login", "sign-in", "signin", "register", "sign-up", "signup",
    "cart", "panier", "checkout", "account", "compte",
    "privacy", "politique-de-confidentialite",
    "mentions-legales", "cgu", "cgv", "terms",
}

# Detection heuristique, a but de journalisation UNIQUEMENT. Ne bloque ni
# n'altere jamais le stockage du contenu ; ne declenche aucune action.
INJECTION_RE = re.compile(
    r"\bclaudebot\b|\bclaude-user\b|\bclaude\b|\bchatgpt\b|\bgptbot\b|"
    r"\banthropic\b|\bopenai\b|"
    r"ignore\s+.{0,25}instructions?|"
    r"ignore[sz]?\s+.{0,25}instructions?\s+(pr[ée]c[ée]dentes|ci-dessus)|"
    r"you\s+are\s+(now\s+)?(an?\s+)?(ai|assistant|bot|crawler|agent)\b|"
    r"en\s+tant\s+qu'?(ia|assistant|robot|crawler|agent)\b|"
    r"system\s*prompt|nouvelle\s+instruction|new\s+instructions?\s*:|"
    r"disregard\s+(all|previous|your)|"
    r"instructions?\s+(pour|à|destin[ée]es?\s+à)\s+(l'|un\s+)?(ia|assistant|crawler|robot|agent)",
    re.IGNORECASE,
)

BINARY_SKIP_EXT = {
    ".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp", ".ico", ".bmp",
    ".css", ".js", ".mjs", ".woff", ".woff2", ".ttf", ".eot", ".otf",
    ".zip", ".rar", ".7z", ".gz", ".tar",
    ".mp4", ".mp3", ".avi", ".mov", ".wav", ".webm",
    ".xml", ".json", ".txt",
    ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx",
}


# --------------------------------------------------------------------------- #
# Utilitaires generaux                                                        #
# --------------------------------------------------------------------------- #

def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def today() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def sha1(text: str) -> str:
    return hashlib.sha1(text.encode("utf-8")).hexdigest()


def slugify(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = text.strip("-")
    return text or "index"


def hosts_for(url: str) -> set[str]:
    """Hote declare + variante avec/sans www, pour la portee de crawl."""
    host = urlsplit(url).netloc.lower()
    bare = host[4:] if host.startswith("www.") else host
    return {bare, "www." + bare}


def canonicalize(url: str) -> str:
    """Supprime fragment + parametres de tracking, normalise le slash final."""
    parts = urlsplit(url)
    query_pairs = [
        (k, v)
        for k, v in parse_qsl(parts.query, keep_blank_values=True)
        if not k.lower().startswith(TRACKING_PARAM_PREFIXES)
        and k.lower() not in TRACKING_PARAM_EXACT
    ]
    query = urlencode(query_pairs)
    path = parts.path or "/"
    if len(path) > 1 and path.endswith("/"):
        path = path.rstrip("/")
    return urlunsplit((parts.scheme, parts.netloc.lower(), path, query, ""))


def is_excluded_path(url: str) -> bool:
    segments = [s.lower() for s in urlsplit(url).path.split("/") if s]
    return any(seg in EXCLUDED_SEGMENTS for seg in segments)


def has_binary_ext(url: str) -> bool:
    path = urlsplit(url).path.lower()
    return any(path.endswith(ext) for ext in BINARY_SKIP_EXT)


def is_pdf_url(url: str) -> bool:
    return urlsplit(url).path.lower().endswith(".pdf")


# --------------------------------------------------------------------------- #
# Journal                                                                     #
# --------------------------------------------------------------------------- #

class Journal:
    def __init__(self, path: Path):
        self.path = path
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self._fh = open(self.path, "a", encoding="utf-8")

    def log(self, concurrent: str, destination: str, event: str, url: str = "", extra: str = ""):
        line = f"{now_iso()}\t{concurrent}\t{destination}\t{event}\t{url}\t{extra}"
        self._fh.write(line + "\n")
        self._fh.flush()

    def close(self):
        self._fh.close()


# --------------------------------------------------------------------------- #
# Politesse : delai minimum par hote                                          #
# --------------------------------------------------------------------------- #

class RateLimiter:
    def __init__(self, delay: float):
        self.delay = delay
        self._last: dict[str, float] = {}

    def wait(self, host: str):
        now = time.monotonic()
        prev = self._last.get(host)
        if prev is not None:
            elapsed = now - prev
            if elapsed < self.delay:
                time.sleep(self.delay - elapsed)
        self._last[host] = time.monotonic()


# --------------------------------------------------------------------------- #
# robots.txt + sitemaps                                                       #
# --------------------------------------------------------------------------- #

@dataclass
class RobotsInfo:
    parser: robotparser.RobotFileParser
    sitemaps: list[str]
    fetch_ok: bool  # False = erreur reseau/serveur -> on refuse tout par prudence
    error_code: str = ""  # code de log quand fetch_ok est False


def fetch_robots(base_url: str, session: requests.Session, limiter: RateLimiter) -> RobotsInfo:
    parts = urlsplit(base_url)
    robots_url = f"{parts.scheme}://{parts.netloc}/robots.txt"
    limiter.wait(parts.netloc)
    rp = robotparser.RobotFileParser()
    try:
        resp = session.get(robots_url, timeout=TIMEOUT, headers={"User-Agent": USER_AGENT})
    except requests.exceptions.SSLError:
        # Certificat TLS invalide/incorrect pour ce nom d'hote : jamais de
        # contournement (pas de verify=False). On refuse tout, domaine ignore
        # dans cette passe, a diagnostiquer separement.
        rp.disallow_all = True
        return RobotsInfo(parser=rp, sitemaps=[], fetch_ok=False, error_code="TLS_CERTIFICATE_ERROR")
    except requests.RequestException:
        # Panne reseau : on ne peut pas etablir les regles -> on refuse tout, par prudence.
        rp.disallow_all = True
        return RobotsInfo(parser=rp, sitemaps=[], fetch_ok=False, error_code="ROBOTS_FETCH_ERROR")

    if resp.status_code == 404:
        # Pas de robots.txt publie : autorisation par defaut (pratique standard).
        rp.parse([])
        return RobotsInfo(parser=rp, sitemaps=[], fetch_ok=True)

    if resp.status_code != 200:
        # Statut anormal (5xx, etc.) : on refuse tout par prudence plutot que de deviner.
        rp.disallow_all = True
        return RobotsInfo(parser=rp, sitemaps=[], fetch_ok=False, error_code="ROBOTS_FETCH_ERROR")

    text = resp.text
    rp.parse(text.splitlines())
    sitemaps = re.findall(r"(?im)^\s*sitemap:\s*(\S+)", text)
    return RobotsInfo(parser=rp, sitemaps=sitemaps, fetch_ok=True)


def fetch_sitemap_urls(
    sitemap_url: str,
    session: requests.Session,
    limiter: RateLimiter,
    allowed_hosts: set[str],
    seen_sitemaps: set[str],
    depth: int = 0,
) -> list[str]:
    if sitemap_url in seen_sitemaps or depth > 5:
        return []
    seen_sitemaps.add(sitemap_url)
    host = urlsplit(sitemap_url).netloc
    limiter.wait(host)
    try:
        resp = session.get(sitemap_url, timeout=TIMEOUT, headers={"User-Agent": USER_AGENT})
        resp.raise_for_status()
    except requests.RequestException:
        return []

    try:
        soup = BeautifulSoup(resp.content, "xml")
    except Exception:
        return []

    urls: list[str] = []
    sitemap_tags = soup.find_all("sitemap")
    if sitemap_tags:
        for tag in sitemap_tags:
            loc = tag.find("loc")
            if loc and loc.text:
                urls.extend(
                    fetch_sitemap_urls(
                        loc.text.strip(), session, limiter, allowed_hosts, seen_sitemaps, depth + 1
                    )
                )
        return urls

    for tag in soup.find_all("url"):
        loc = tag.find("loc")
        if loc and loc.text:
            u = loc.text.strip()
            if urlsplit(u).netloc.lower() in allowed_hosts:
                urls.append(u)
    return urls


# --------------------------------------------------------------------------- #
# Crawl de secours par profondeur (sans sitemap)                              #
# --------------------------------------------------------------------------- #

def extract_links(html: str, base_url: str, allowed_hosts: set[str]) -> list[str]:
    try:
        soup = BeautifulSoup(html, "lxml")
    except Exception:
        return []
    links = []
    for a in soup.find_all("a", href=True):
        href = a["href"].strip()
        if not href or href.startswith(("mailto:", "tel:", "javascript:", "#")):
            continue
        absolute = urljoin(base_url, href)
        parts = urlsplit(absolute)
        if parts.scheme not in ("http", "https"):
            continue
        if parts.netloc.lower() not in allowed_hosts:
            continue
        links.append(canonicalize(absolute))
    return links


# --------------------------------------------------------------------------- #
# Recuperation de page + cache                                                #
# --------------------------------------------------------------------------- #

@dataclass
class FetchResult:
    ok: bool
    status_code: int | None = None
    final_url: str | None = None
    content: bytes | None = None
    content_type: str = ""
    error: str = ""
    error_code: str = "HTTP_ERROR"


def fetch_url(url: str, session: requests.Session, limiter: RateLimiter) -> FetchResult:
    host = urlsplit(url).netloc
    delay = RETRY_BACKOFF_BASE
    last_error = ""
    for attempt in range(MAX_RETRIES + 1):
        limiter.wait(host)
        try:
            resp = session.get(
                url, timeout=TIMEOUT, allow_redirects=True, headers={"User-Agent": USER_AGENT}
            )
        except requests.exceptions.SSLError as exc:
            # Certificat TLS invalide : jamais de contournement, jamais de
            # retry (un probleme de certificat n'est pas transitoire).
            return FetchResult(ok=False, error=str(exc), error_code="TLS_CERTIFICATE_ERROR")
        except requests.RequestException as exc:
            last_error = str(exc)
            if attempt < MAX_RETRIES:
                time.sleep(delay)
                delay *= 2
                continue
            return FetchResult(ok=False, error=last_error)

        if resp.status_code >= 500 and attempt < MAX_RETRIES:
            time.sleep(delay)
            delay *= 2
            continue

        return FetchResult(
            ok=resp.status_code == 200,
            status_code=resp.status_code,
            final_url=resp.url,
            content=resp.content,
            content_type=resp.headers.get("Content-Type", ""),
            error="" if resp.status_code == 200 else f"HTTP {resp.status_code}",
        )
    return FetchResult(ok=False, error=last_error or "echec inconnu")


class CacheIndex:
    """Cache par URL canonique. Ne touche jamais aux fichiers de sources/."""

    def __init__(self, concurrent: str):
        self.dir = CACHE_DIR / concurrent
        self.raw_dir = self.dir / "raw"
        self.raw_dir.mkdir(parents=True, exist_ok=True)
        self.index_path = self.dir / "index.json"
        if self.index_path.exists():
            self.data = json.loads(self.index_path.read_text(encoding="utf-8"))
        else:
            self.data = {}

    def get(self, canon_url: str) -> dict | None:
        return self.data.get(canon_url)

    def put_success(self, canon_url: str, final_url: str, content: bytes, content_type: str):
        key = sha1(canon_url)
        raw_path = self.raw_dir / f"{key}.bin"
        raw_path.write_bytes(content)
        self.data[canon_url] = {
            "status": "success",
            "final_url": final_url,
            "content_type": content_type,
            "cache_file": str(raw_path),
            "fetched_at": now_iso(),
        }
        self._save()

    def put_error(self, canon_url: str, error: str):
        self.data[canon_url] = {"status": "error", "error": error, "fetched_at": now_iso()}
        self._save()

    def _save(self):
        self.index_path.write_text(json.dumps(self.data, ensure_ascii=False, indent=1), encoding="utf-8")


# --------------------------------------------------------------------------- #
# Classement / chemins de sortie                                              #
# --------------------------------------------------------------------------- #

def classify_integre(url: str, doc_prefixe: str) -> str:
    path = urlsplit(url).path
    prefix = doc_prefixe.rstrip("/")
    if path == prefix or path.rstrip("/") == prefix or path.startswith(prefix + "/"):
        return "centre_aide"
    return "site_marketing"


def compute_output_path(nom: str, destination: str, url: str, doc_prefixe: str | None) -> Path:
    path = urlsplit(url).path
    if destination == "centre_aide" and doc_prefixe:
        prefix = doc_prefixe.rstrip("/")
        if path.startswith(prefix):
            path = path[len(prefix):]
    segments = [slugify(s) for s in path.split("/") if s]
    if not segments:
        segments = ["index"]
    base_dir = SOURCES_DIR / nom / destination
    if len(segments) == 1:
        return base_dir / f"{segments[0]}.md"
    return base_dir.joinpath(*segments[:-1]) / f"{segments[-1]}.md"


def compute_pdf_path(nom: str, url: str) -> Path:
    path = urlsplit(url).path
    name = slugify(path.rsplit("/", 1)[-1].removesuffix(".pdf")) + ".pdf"
    return SOURCES_DIR / nom / "_assets_pdf" / name


# --------------------------------------------------------------------------- #
# Conversion HTML -> markdown                                                 #
# --------------------------------------------------------------------------- #

def html_to_markdown(html_bytes: bytes, url: str) -> str | None:
    try:
        text = trafilatura.extract(
            html_bytes,
            url=url,
            output_format="markdown",
            include_tables=True,
            include_links=True,
            include_images=False,
            favor_recall=True,
        )
    except Exception:
        return None
    return text


def write_markdown(out_path: Path, requested_url: str, final_url: str, destination: str, body: str):
    out_path.parent.mkdir(parents=True, exist_ok=True)
    front_matter = (
        "---\n"
        f"url: {requested_url}\n"
        f"url_finale: {final_url}\n"
        f"date_collecte: {today()}\n"
        f"destination: {destination}\n"
        "---\n\n"
    )
    out_path.write_text(front_matter + body, encoding="utf-8")


# --------------------------------------------------------------------------- #
# Plan de crawl par concurrent                                                #
# --------------------------------------------------------------------------- #

@dataclass
class CrawlTarget:
    kind: str            # "fixed" (centre_aide OU site_marketing entier) | "integre"
    base_url: str
    hosts: set[str]
    dest_fixed: str | None
    doc_prefixe: str | None
    label: str


def build_targets(entry: dict) -> list[CrawlTarget]:
    targets: list[CrawlTarget] = []
    doc_config = entry.get("doc_config")
    doc_collecte = entry.get("doc_collecte", "standard")
    nom = entry["nom"]

    if doc_config == "integre":
        if not entry.get("marketing_fait") or (not entry.get("aide_fait") and doc_collecte == "standard"):
            targets.append(
                CrawlTarget(
                    kind="integre",
                    base_url=entry["site"],
                    hosts=hosts_for(entry["site"]),
                    dest_fixed=None,
                    doc_prefixe=entry.get("doc_prefixe"),
                    label=f"{nom}:site(integre)",
                )
            )
    else:
        if (
            not entry.get("aide_fait")
            and doc_collecte == "standard"
            and doc_config in ("sous_domaine", "domaine_separe")
            and entry.get("doc")
        ):
            targets.append(
                CrawlTarget(
                    kind="fixed",
                    base_url=entry["doc"],
                    hosts=hosts_for(entry["doc"]),
                    dest_fixed="centre_aide",
                    doc_prefixe=None,
                    label=f"{nom}:centre_aide",
                )
            )
        if not entry.get("marketing_fait") and entry.get("site"):
            targets.append(
                CrawlTarget(
                    kind="fixed",
                    base_url=entry["site"],
                    hosts=hosts_for(entry["site"]),
                    dest_fixed="site_marketing",
                    doc_prefixe=None,
                    label=f"{nom}:site_marketing",
                )
            )

    # Sources documentaires secondaires declarees explicitement (ex : un
    # second sous-domaine de doc distinct du corpus deja collecte). Chacune
    # ecrit dans son propre dossier sources/<nom>/<dest>/, jamais dans
    # centre_aide/ ou site_marketing/. Jamais suivi automatiquement : doit
    # etre declare ici, avec doc_collecte: standard, pour etre crawle.
    for extra in entry.get("sources_secondaires", []) or []:
        if extra.get("doc_collecte") != "standard" or not extra.get("doc"):
            continue
        targets.append(
            CrawlTarget(
                kind="fixed",
                base_url=extra["doc"],
                hosts=hosts_for(extra["doc"]),
                dest_fixed=extra["dest"],
                doc_prefixe=None,
                label=f"{nom}:{extra['dest']}",
            )
        )
    return targets


# --------------------------------------------------------------------------- #
# Traitement d'une cible de crawl                                             #
# --------------------------------------------------------------------------- #

def process_target(
    entry: dict,
    target: CrawlTarget,
    session: requests.Session,
    limiter: RateLimiter,
    journal: Journal,
    cache: CacheIndex,
    dry_run: bool,
    stats: dict,
):
    nom = entry["nom"]
    label = target.label

    robots = fetch_robots(target.base_url, session, limiter)
    if not robots.fetch_ok:
        journal.log(nom, label, robots.error_code, target.base_url, "cible ignoree par prudence ; aucun contournement TLS")
        stats["robots_fetch_error"] = stats.get("robots_fetch_error", 0) + 1
        if robots.error_code == "TLS_CERTIFICATE_ERROR":
            stats["tls_certificate_error"] = stats.get("tls_certificate_error", 0) + 1
        return

    seen_sitemaps: set[str] = set()
    candidate_urls: list[str] = []
    for sm in robots.sitemaps:
        candidate_urls.extend(
            fetch_sitemap_urls(sm, session, limiter, target.hosts, seen_sitemaps)
        )
    candidate_urls = sorted(set(canonicalize(u) for u in candidate_urls))

    if candidate_urls:
        discovery_mode = "sitemap"
    else:
        discovery_mode = "depth4"
        journal.log(
            nom, label, "COUVERTURE",
            target.base_url,
            "crawl profondeur 4 — exhaustivite non garantie",
        )
        candidate_urls = depth_crawl(
            target.base_url, target.hosts, robots.parser, session, limiter, journal, nom, label
        )

    journal.log(nom, label, "DISCOVERY_MODE", target.base_url, f"{discovery_mode} ({len(candidate_urls)} urls)")

    for url in candidate_urls[:MAX_PAGES_PER_TARGET]:
        handle_candidate(entry, target, url, robots.parser, session, limiter, journal, cache, dry_run, stats)


def depth_crawl(
    base_url: str,
    allowed_hosts: set[str],
    robots_rp: robotparser.RobotFileParser,
    session: requests.Session,
    limiter: RateLimiter,
    journal: Journal,
    nom: str,
    label: str,
) -> list[str]:
    start = canonicalize(base_url)
    seen = {start}
    queue = deque([(start, 0)])
    discovered = []

    while queue and len(discovered) < MAX_PAGES_PER_TARGET:
        url, depth = queue.popleft()
        discovered.append(url)
        if depth >= MAX_DEPTH:
            continue
        if is_excluded_path(url) or has_binary_ext(url):
            continue
        if not robots_rp.can_fetch(USER_AGENT, url):
            journal.log(nom, label, "ROBOTS_DENIED", url, "decouverte")
            continue
        result = fetch_url(url, session, limiter)
        if not result.ok or not result.content:
            continue
        if "html" not in (result.content_type or "").lower():
            continue
        try:
            html_text = result.content.decode("utf-8", errors="replace")
        except Exception:
            continue
        for link in extract_links(html_text, result.final_url or url, allowed_hosts):
            if link not in seen:
                seen.add(link)
                queue.append((link, depth + 1))
    return discovered


def handle_candidate(
    entry: dict,
    target: CrawlTarget,
    url: str,
    robots_rp: robotparser.RobotFileParser,
    session: requests.Session,
    limiter: RateLimiter,
    journal: Journal,
    cache: CacheIndex,
    dry_run: bool,
    stats: dict,
):
    nom = entry["nom"]
    label = target.label
    canon = canonicalize(url)

    if has_binary_ext(canon) and not is_pdf_url(canon):
        return  # actifs binaires non-PDF : jamais collectes

    if is_excluded_path(canon):
        journal.log(nom, label, "EXCLUDED", canon)
        stats["excluded"] = stats.get("excluded", 0) + 1
        return

    # Classement provisoire (avant redirection) pour un filtrage rapide.
    if target.kind == "integre":
        dest = classify_integre(canon, target.doc_prefixe or "")
        if dest == "centre_aide" and entry.get("doc_collecte") == "spa_onglets":
            journal.log(nom, "centre_aide", "SPA_UNSUPPORTED", canon,
                        "doc_collecte=spa_onglets ; non recupere dans ce chantier")
            stats["spa_unsupported"] = stats.get("spa_unsupported", 0) + 1
            return
        if dest == "centre_aide" and entry.get("aide_fait"):
            stats["skip_already_done"] = stats.get("skip_already_done", 0) + 1
            return
        if dest == "site_marketing" and entry.get("marketing_fait"):
            stats["skip_already_done"] = stats.get("skip_already_done", 0) + 1
            return
    else:
        dest = target.dest_fixed

    if not robots_rp.can_fetch(USER_AGENT, canon):
        journal.log(nom, dest, "ROBOTS_DENIED", canon)
        stats["robots_denied"] = stats.get("robots_denied", 0) + 1
        return

    provisional_out = (
        compute_pdf_path(nom, canon)
        if is_pdf_url(canon)
        else compute_output_path(nom, dest, canon, target.doc_prefixe)
    )
    if provisional_out.exists():
        journal.log(nom, dest, "SKIP_EXISTING", canon, str(provisional_out))
        stats["skip_existing"] = stats.get("skip_existing", 0) + 1
        return

    stats["discovered"] = stats.get("discovered", 0) + 1

    if dry_run:
        journal.log(nom, dest, "DRY_RUN_PLANNED", canon, f"-> {provisional_out}")
        stats["would_fetch"] = stats.get("would_fetch", 0) + 1
        return

    cached = cache.get(canon)
    if cached and cached.get("status") == "success":
        raw_path = Path(cached["cache_file"])
        if raw_path.exists():
            content = raw_path.read_bytes()
            final_url = cached.get("final_url", canon)
            content_type = cached.get("content_type", "")
            journal.log(nom, dest, "CACHED", canon)
            stats["from_cache"] = stats.get("from_cache", 0) + 1
        else:
            content, final_url, content_type = _fetch_and_cache(canon, session, limiter, cache, journal, nom, dest, stats)
            if content is None:
                return
    else:
        content, final_url, content_type = _fetch_and_cache(canon, session, limiter, cache, journal, nom, dest, stats)
        if content is None:
            return

    if final_url and canonicalize(final_url) != canon:
        journal.log(nom, dest, "REDIRECT", canon, f"-> {final_url}")

    final_canon = canonicalize(final_url) if final_url else canon

    # Reclassement definitif sur l'URL finale (regle : le classement depend
    # de l'URL finale apres redirection).
    if target.kind == "integre":
        final_dest = classify_integre(final_canon, target.doc_prefixe or "")
        if final_dest == "centre_aide" and (
            entry.get("doc_collecte") == "spa_onglets" or entry.get("aide_fait")
        ):
            journal.log(nom, "centre_aide", "SKIP_APRES_REDIRECTION", canon, f"-> {final_url}")
            return
        if final_dest == "site_marketing" and entry.get("marketing_fait"):
            journal.log(nom, "site_marketing", "SKIP_APRES_REDIRECTION", canon, f"-> {final_url}")
            return
        dest = final_dest

    if is_excluded_path(final_canon):
        journal.log(nom, dest, "EXCLUDED_APRES_REDIRECTION", canon, f"-> {final_url}")
        return

    if is_pdf_url(final_canon) or "application/pdf" in (content_type or "").lower():
        out_path = compute_pdf_path(nom, final_canon)
        if out_path.exists():
            journal.log(nom, dest, "SKIP_EXISTING", canon, str(out_path))
            return
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_bytes(content)
        journal.log(nom, dest, "PDF_DETECTED", canon, str(out_path))
        stats["pdf"] = stats.get("pdf", 0) + 1
        return

    if "html" not in (content_type or "").lower():
        journal.log(nom, dest, "SKIPPED_NON_HTML", canon, content_type)
        return

    out_path = compute_output_path(nom, dest, final_canon, target.doc_prefixe)
    if out_path.exists():
        journal.log(nom, dest, "SKIP_EXISTING", canon, str(out_path))
        stats["skip_existing"] = stats.get("skip_existing", 0) + 1
        return

    body = html_to_markdown(content, final_url or canon)
    if not body or not body.strip():
        journal.log(nom, dest, "PARSE_ERROR", canon, "extraction vide")
        stats["parse_error"] = stats.get("parse_error", 0) + 1
        return

    if INJECTION_RE.search(body):
        journal.log(nom, dest, "CONTENT_INSTRUCTION_IGNORED", canon,
                     "texte adresse a un agent/IA detecte ; stocke tel quel, non execute")

    write_markdown(out_path, canon, final_url or canon, dest, body)
    journal.log(nom, dest, "FETCHED", canon, str(out_path))
    stats["fetched"] = stats.get("fetched", 0) + 1


def _fetch_and_cache(canon, session, limiter, cache, journal, nom, dest, stats):
    result = fetch_url(canon, session, limiter)
    if not result.ok:
        cache.put_error(canon, result.error)
        journal.log(nom, dest, result.error_code, canon, result.error or f"HTTP {result.status_code}")
        stats["errors"] = stats.get("errors", 0) + 1
        if result.error_code == "TLS_CERTIFICATE_ERROR":
            stats["tls_certificate_error"] = stats.get("tls_certificate_error", 0) + 1
        return None, None, None
    cache.put_success(canon, result.final_url or canon, result.content, result.content_type)
    return result.content, result.final_url or canon, result.content_type


# --------------------------------------------------------------------------- #
# Point d'entree                                                              #
# --------------------------------------------------------------------------- #

def load_entries(only: str | None) -> list[dict]:
    entries = yaml.safe_load(SOURCES_YAML.read_text(encoding="utf-8"))
    if only:
        entries = [e for e in entries if e["nom"] == only]
    return entries


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="ne fetch pas le corps des pages sitemap, n'ecrit rien")
    parser.add_argument("--concurrent", default=None, help="limiter a un concurrent (nom)")
    parser.add_argument(
        "--dest", default=None,
        help="limiter aux cibles dont la destination correspond exactement "
             "(ex: documentation_2, centre_aide, site_marketing)",
    )
    args = parser.parse_args()

    entries = load_entries(args.concurrent)
    journal = Journal(LOG_PATH)
    session = requests.Session()
    limiter = RateLimiter(REQUEST_DELAY)

    global_stats: dict[str, dict] = {}

    for entry in entries:
        nom = entry["nom"]
        targets = build_targets(entry)
        if args.dest:
            targets = [t for t in targets if (t.dest_fixed or "integre") == args.dest]
        if not targets:
            journal.log(nom, "-", "AUCUNE_CIBLE", "", "rien a faire pour ce concurrent dans cette passe")
            continue
        cache = CacheIndex(nom)
        stats_by_dest: dict[str, dict] = {}
        for target in targets:
            dest_key = target.dest_fixed or "integre"
            stats = stats_by_dest.setdefault(dest_key, {})
            process_target(entry, target, session, limiter, journal, cache, args.dry_run, stats)
        global_stats[nom] = stats_by_dest

    journal.log("-", "-", "RUN_TERMINE", "", "dry_run" if args.dry_run else "reel")
    journal.close()

    print_summary(global_stats, args.dry_run)


def print_summary(global_stats: dict, dry_run: bool):
    print()
    print(f"=== Bilan {'(DRY RUN)' if dry_run else ''} ===")
    for nom, by_dest in global_stats.items():
        print(f"\n{nom}:")
        for dest, stats in by_dest.items():
            discovered = stats.get("discovered", 0)
            fetched = stats.get("fetched", 0) + stats.get("would_fetch", 0)
            skipped = (
                stats.get("skip_existing", 0)
                + stats.get("skip_already_done", 0)
                + stats.get("excluded", 0)
                + stats.get("robots_denied", 0)
                + stats.get("spa_unsupported", 0)
            )
            errors = stats.get("errors", 0) + stats.get("parse_error", 0) + stats.get("robots_fetch_error", 0)
            print(
                f"  {dest:15s} discovered={discovered:5d} fetched={fetched:5d} "
                f"skipped={skipped:5d} errors={errors:5d} "
                f"(cache={stats.get('from_cache',0)} pdf={stats.get('pdf',0)})"
            )


if __name__ == "__main__":
    main()
