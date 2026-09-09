# Couverture de la collecte — état certifié par concurrent

Ce fichier existe pour qu'on ne conclue jamais qu'un concurrent documente
peu, ou différemment, alors qu'en réalité nous n'avons pas pu le collecter.
**Une absence ici est un TROU DE COLLECTE, jamais un fait concurrentiel.**
Silence documentaire et trou de collecte restent deux choses différentes.

Chantier : `tools/collecte/collecte.py` / `tools/collecte/sources.yaml`.
Audit de certification : 2026-09-07.

> **Note méthodologique obligatoire.** Les résumés affichés en console
> pendant certaines collectes agrégeaient plusieurs causes sous `skipped`
> et employaient `discovered` de façon ambiguë (avec ou sans les URLs
> exclues selon le contexte). Les chiffres certifiés dans ce document ont
> été reconstruits depuis `collecte.log`, les fichiers présents sur disque
> et, lorsque disponible, le sitemap source revérifié en direct — jamais
> depuis un résumé console. Le disque a servi de vérité primaire : un
> écart de 5 lignes `FETCHED` a été identifié entre le log et le disque
> (costructor -1, sellsy -2, vertuoza -2), tous confirmés comme des
> fichiers réellement présents et complets sur disque, la ligne de log
> ayant été perdue par écriture concurrente de plusieurs processus
> `collecte.py` lancés en parallèle le 07/09 sans verrou de fichier sur
> `collecte.log`. Le contenu n'a jamais été perdu, seule une ligne de
> journal l'a été. Signalé comme anomalie technique, non corrigé (voir
> section « Anomalies » ci-dessous).

---

## Historique vs nouveau — ne jamais mélanger

Six concurrents avaient un corpus **historique** (centre d'aide) déjà
présent avant ce chantier, non retouché ici :

| Concurrent | Fichiers historiques (racine, hors site_marketing/) |
|---|---:|
| axonaut | 129 (dont `erreurs.md`/`index.md` méta) |
| costructor | 114 |
| inter-fast | 223 |
| openfire | 129 (dont `erreurs.md`/`index.md` méta) — corpus Zendesk |
| sellsy | 464 |
| vertuoza | 435 |

Ces six corpus n'ont **aucune trace de log** dans ce chantier (collectés
avant l'existence de `collecte.py`/`collecte.log`, par une méthode
différente et documentée séparément dans `sources/résumé.md` pour 4
d'entre eux). Leur couverture individuelle est **NON_DETERMINABLE** depuis
cet audit — ce n'est pas un défaut, c'est hors du périmètre de ce qui
peut être vérifié ici. Aucun fichier historique n'a été déplacé, modifié
ou fusionné pendant ce chantier (contrôle git en fin de document).

---

## tolteck

| Destination | Statut | Détail certifié |
|---|---|---|
| centre_aide | **BLOQUÉ** | `help.tolteck.com` sert un certificat TLS qui ne correspond pas au nom d'hôte (`SSL: CERTIFICATE_VERIFY_FAILED`). Journalisé `TLS_CERTIFICATE_ERROR`. Aucun `verify=False`, aucun contournement. `aide_fait` reste `false`. 0 fichier. |
| site_marketing | Collecté, crawl de secours (pas de sitemap) | 204 URLs découvertes en profondeur 4 (`www.tolteck.com`, sitemap absent). 199 fichiers présents = 199 FETCHED (log et disque concordent) + 2 EXCLUDED (cgu, mentions-legales) + 1 SKIP_EXISTING + 1 HTTP_ERROR. **Reste non expliqué : 1 URL** (204 − 203). Cause NON_DETERMINABLE : le crawl en profondeur 4 ne journalise pas individuellement chaque URL découverte, et n'est de toute façon jamais qualifié d'exhaustif par construction. Écart mineur, non résolu, non estimé. |

## leobati

| Destination | Statut | Détail certifié |
|---|---|---|
| centre_aide | **BLOQUÉ** | `/bati/guide` est une application à onglets (Next.js) chargée en JavaScript sur une URL HTML unique. **Absente du sitemap** (`leobati.fr/sitemap.xml`, 70 URLs, aucune entrée `/bati/guide`) : même un crawl exhaustif par sitemap ne l'aurait pas trouvée. Bouton « Imprimer / PDF » présent mais aucune URL/endpoint PDF identifiable dans le HTML statique. `doc_collecte: spa_onglets`, `aide_fait: false`. 0 fichier. Ne jamais prétendre ce centre d'aide collecté. |
| site_marketing | **Collecté, complet** | 70 URLs sitemap = 70 fichiers présents, 0 exclusion, 0 erreur. Réconciliation exacte. |

## batikko

| Destination | Statut | Détail certifié |
|---|---|---|
| centre_aide | **Collecté, complet** | 14 fichiers, tous sous `/documentation`. |
| site_marketing | **Collecté, complet** | 46 fichiers. |
| **Réconciliation** | 63 URLs sitemap = 14 + 46 + 3 exclusions (`cgu`, `cgv`, `mentions-legales`). Exact, 0 reste. Ancienne formulation erronée « 3 déjà présentes » corrigée : c'était 3 exclusions, pas des fichiers préexistants (0 `SKIP_EXISTING` sur ce run). |
| Sur-inclusion connue | `site_marketing/privacy-policy.md` collecté — le mot-clé d'exclusion `privacy` ne matche plus `privacy-policy` depuis le passage en comparaison par segment exact (correctif anti-faux-positif suite à l'incident `/compte-cle-en-main` chez progbat). Régression mineure, signalée, non corrigée. |

## progbat

| Destination | Statut | Détail certifié |
|---|---|---|
| centre_aide | **Collecté, complet** | 190 URLs sitemap = 190 fichiers. Exact. |
| site_marketing | **Collecté, complet** | 51 URLs sitemap = 50 fichiers + 1 exclusion (`mentions-legales`). Exact. Le faux positif initial sur `/compte-cle-en-main` (exclu à tort par un ancien regex matchant `compte` en préfixe) a été corrigé et la page récupérée ; 0 sur-inclusion résiduelle détectée. |
| Plateforme documentaire | Note | La documentation `centre_aide` est servie via GitBook (`docv5.progbat.com`). GitBook y expose `llms-full.txt` — constaté lors d'un diagnostic le 2026-09-08, potentiellement utile pour une future collecte. Non exploité par la collecte actuelle. |
| Pages sans corps documentaire | Constat | 5 pages `centre_aide/le-menu-principal/bibliotheque/elements/*` (`fournitures`, `location`, `main-doeuvre`, `outillage`, `sous-traitance`) vérifiées le 2026-09-08 : pas de corps documentaire substantiel dans la source elle-même (confirmé par l'export GitBook natif et `llms-full.txt`, pas un défaut de rendu JS côté collecte). Ce constat ne démontre ni un défaut de collecte, ni une absence fonctionnelle dans ProGBat. |

## axonaut *(centre_aide historique non touché)*

| Destination | Statut | Détail certifié |
|---|---|---|
| site_marketing | **Collecté, complet** | 65 URLs sitemap = 50 fichiers MD + 4 PDF (`_assets_pdf/`) + 11 HTTP 404 (liens morts dans leur propre sitemap, pages de secteurs métiers supprimées côté axonaut.com). Exact. 0 exclusion, 0 violation de classement, 0 sur-inclusion juridique. |

## costructor *(centre_aide historique non touché)*

| Destination | Statut | Détail certifié |
|---|---|---|
| site_marketing | **Collecté, complet** | 184 URLs sitemap (index WordPress, 5 sous-sitemaps revérifiés en direct) = 180 FETCHED (log) + 1 fichier confirmé sur disque mais dont la ligne `FETCHED` a été perdue par écriture concurrente (`rentabilite-chantier.md`, présent, daté 07/09) + 2 exclusions (`cgu`, `mentions-legales`) + 1 SKIP_EXISTING = 184, exact une fois le disque utilisé comme vérité (181 fichiers réels). |
| Sur-inclusion réelle | `site_marketing/cookies.md` (`costructor.co/cookies`) — page de politique cookies du site lui-même, jamais couverte par la liste d'exclusion (`cookies` n'y figure pas). Gap préexistant du vocabulaire d'exclusion, pas une régression de ce chantier. |
| Faux positifs du scan juridique (non des sur-inclusions) | Deux articles de blog dont le titre contient « mentions légales » (`blog/mentions-legales-devis-travaux`, `blog/comment-faire-facture-macon`) sont des contenus éditoriaux sur les mentions légales obligatoires d'un devis BTP — pas les CGU/CGV de costructor lui-même. Correctement collectés. |

## inter-fast *(centre_aide historique non touché)*

| Destination | Statut | Détail certifié |
|---|---|---|
| site_marketing | **Collecté, complet** | 802 URLs sitemap = 799 fichiers + 3 exclusions (2× `cgv`, 1× `politique-de-confidentialite`). Exact. 0 erreur, 0 violation de classement, 0 sur-inclusion juridique détectée. |

## openfire *(deux corpus documentaires distincts, jamais fusionnés)*

| Corpus | Emplacement | Statut | Détail certifié |
|---|---|---|---|
| Centre d'aide historique (Zendesk) | racine `openfire/` (hors site_marketing/documentation_2) | **non touché** | 129 fichiers (dont 2 méta), collecté avant ce chantier. |
| Second corpus documentaire (Odoo Knowledge) | `openfire/documentation_2/` | **Collecté, complet** | 214 URLs sitemap = 213 fichiers + 1 HTTP 404 (`/contactus`, lien mort dans leur propre sitemap). Exact. Plateforme distincte (`documentation.openfire.fr`), pas de rendu JS bloquant vérifié avant collecte. |
| site_marketing | `openfire/site_marketing/` | **Collecté, complet** | 172 URLs sitemap = 166 fichiers + 1 exclusion (`mentions-legales`) + 5 `SKIPPED_NON_HTML` (contenu non-HTML servi, légitimement non converti). Exact. |

**Ces deux corpus documentaires ne sont ni fusionnés ni comparés terme à
terme.** Recouvrement thématique réel observé (facturation, achats,
comptabilité couverts dans les deux) mais registres différents : le
corpus Odoo est technique/générique, le corpus Zendesk est éditorialisé
pour le métier (chauffage, ramonage). Aucune conclusion sur lequel est le
plus à jour ou le plus poussé par l'éditeur — non déductible de la
collecte seule.

## sellsy *(centre_aide historique non touché)*

| Destination | Statut | Détail certifié |
|---|---|---|
| site_marketing | **Collecté, complet** | Domaine redéclaré `go.sellsy.com` (redirection 301 depuis `www.sellsy.com`, vérifiée avant collecte : robots.txt standard, sitemap déclaré, 145 liens internes réels). 885 URLs sitemap = 880 FETCHED (log) + 2 fichiers confirmés sur disque avec ligne de log perdue (écriture concurrente) + 1 exclusion (`mentions-legales`) + 2 `PARSE_ERROR` = 885, exact une fois le disque utilisé (882 fichiers réels). |
| Sur-inclusion réelle | **12 pages juridiques/conformité propres à sellsy non exclues**, réparties sur deux répertoires dédiés entiers : `site_marketing/informations-legales/` (7 fichiers : `conditions-generales`, `conditions-generales-offre-promotionnelle`, `conditions-generales-programme-partenaire`, `conditions-generales-programme-revendeur`, `confidentialite-des-donnees`, `securite-des-donnees`, `politique-de-divulgation-de-vulnerabilite`) et `site_marketing/en/legal-information/` (5 fichiers : `general-terms-and-conditions`, `legal-notice`, `data-privacy`, `data-security`, `vulnerability-disclosure-policy`). Un 8e fichier du répertoire français, `informations-legales/bareme-remise-programme-revendeur.md`, est un barème commercial (remises partenaires) classé par sellsy sous le même répertoire légal mais n'est pas lui-même un document juridique — traité comme **ambigu**, pas compté dans les 12. Le mot `mentions-legales` (même préfixe de chemin) a, lui, correctement été exclu — la liste d'exclusion ne couvre pas `conditions-generales`, `informations-legales`, `legal-notice`, `confidentialite`/`data-privacy`, `securite-des-donnees`/`data-security` ni `vulnerability-disclosure-policy`. Gap préexistant du vocabulaire d'exclusion, pas une régression de ce chantier. Le premier passage d'audit n'avait détecté que 5 de ces 12 fichiers (recherche par mot-clé isolé, pas par répertoire) — corrigé ici après relecture exhaustive des deux répertoires. La plus large sur-inclusion juridique détectée dans ce corpus. |

## vertuoza *(centre_aide historique non touché)*

| Destination | Statut | Détail certifié |
|---|---|---|
| site_marketing | **Collecté, complet** | 1289 URLs sitemap = 1211 FETCHED (log) + 2 fichiers confirmés sur disque avec ligne de log perdue (écriture concurrente) + 3 exclusions (`politique-de-confidentialite` ×3 locales fr) + 73 HTTP 404 (liens morts dans leur propre sitemap, articles de blog listés pour des locales fr-be/fr-ch où ils n'existent pas) = 1289, exact une fois le disque utilisé (1213 fichiers réels). |
| Sur-inclusion réelle | **2 pages** : `nl-be/privacybeleid.md` et `nl-nl/privacybeleid.md` — la politique de confidentialité de vertuoza en néerlandais (« Privacybeleid »), non exclue car la liste d'exclusion ne couvre que le français (`politique-de-confidentialite`) et l'anglais implicite (`privacy`), pas le néerlandais. Les 3 variantes françaises (`fr-fr`, `fr-be`, `fr-ch`) ont, elles, correctement été exclues. Gap de couverture linguistique du vocabulaire d'exclusion, pas une régression de ce chantier. Le premier passage d'audit avait conclu à tort « 0 sur-inclusion » sur ce concurrent (3 candidats identifiés étaient bien des faux positifs — articles de blog éditoriaux sur les mentions légales obligatoires, pas les CGU/CGV de vertuoza — mais la recherche n'avait pas couvert les locales néerlandaises). |

## extrabat

Collecte réelle du 09/09/2026, via `collecte.py --concurrent extrabat` (aucun paramètre non prévu). Vérifications préalables (domaine canonique, robots.txt, SPA, liens HTML) faites manuellement avant le lancement — non automatisées dans le code.

| Destination | Statut | Détail certifié |
|---|---|---|
| centre_aide | **Collecté, quasi complet** | Découverte : crawl de secours profondeur 4 (aucune ligne `Sitemap:` déclarée dans `robots.txt` de `servicescompris.extrabat.com`, malgré l'existence réelle d'un `sitemap_index.xml` sur le serveur — même mécanisme que tolteck). 2077 candidats découverts par le crawl = **1670 fichiers FETCHED** + 3 EXCLUDED (segments `login`, `compte`, `cgv` — coïncidence avec des slugs de tag, pas de vraies pages de connexion/compte/CGV) + 1 HTTP_ERROR (404) + 21 SKIP_EXISTING (doublons de schéma http/https vers un fichier déjà écrit dans ce même run, `canonicalize()` ne normalisant pas le schéma) + 382 actifs binaires non-PDF jamais journalisés par construction (images `/content/uploads/...`, cf. `collecte.py` l. 658-659). Réconciliation manuelle contre le sitemap réel non déclaré (§ ci-dessous) : exacte à 1 URL près. |
| site_marketing | **Collecté, complet** | Découverte : sitemap déclaré dans `robots.txt` de `www.extrabat.com` (`sitemaps.xml`). 37 URLs sitemap = 35 FETCHED + 1 EXCLUDED (`mentions-legales`) + 1 SKIP_EXISTING (`/rendez-vous` redirige vers `/demo`, déjà collecté). Exact, 0 reste. |

### Réconciliation manuelle par source

**centre_aide** (`servicescompris.extrabat.com`, sitemap réel non déclaré dans robots.txt, récupéré manuellement le 09/09/2026 : `sitemap_index.xml` → 4 sous-sitemaps `post-sitemap.xml` (1023), `page-sitemap.xml` (2), `e-landing-page-sitemap.xml` (0), `category-sitemap.xml` (63) = 1088 URLs brutes, 996 après déduplication par canonicalisation) :

- 996 URLs sitemap pertinentes
- 553 sont des pièces jointes média (`/content/uploads/...`, images) — jamais collectées par construction (`has_binary_ext`), non une lacune
- 1670 fichiers effectivement collectés (chiffre du crawl profondeur 4, périmètre différent du sitemap — le crawl découvre aussi des pages hors sitemap, notamment les 1069 archives `/tag/` et 15 `/page/N/`, absentes du sitemap Yoast)
- Recoupement sitemap ↔ corpus/journal : sur les 996 URLs sitemap, **1 seule reste inexpliquée après exclusion des médias** : `https://servicescompris.extrabat.com/test` — page WordPress orpheline (répond HTTP 200, existe réellement) jamais atteinte par le crawl profondeur 4, non liée depuis aucune page explorée en profondeur ≤4 depuis l'accueil. Cause déterminée : **page orpheline non atteinte par le crawl**, matérialité nulle (1 page de test, pas un article).
- Les 63 URLs `category-sitemap.xml` n'utilisent pas de préfixe `/category/` distinct (base de catégorie WordPress supprimée) : elles se confondent avec des chemins de premier niveau ordinaires et ont été normalement découvertes et collectées par le crawl, sans traitement spécial nécessaire.

**site_marketing** (`www.extrabat.com`, sitemap déclaré dans robots.txt) : réconciliation déjà exacte via le mécanisme du script lui-même (37 = 35 + 1 + 1, voir tableau ci-dessus) — pas de sitemap parallèle à vérifier manuellement, un sitemap étant déjà déclaré.

**Total Extrabat** : 1670 (centre_aide) + 35 (site_marketing) = **1705 fichiers**.

### Dette signalée — pages `/tag/` et `/page/N/` (décision actée, non exclues à ce stade)

**1069 fichiers sous `centre_aide/tag/`** et **15 fichiers sous `centre_aide/page/`** (1084 fichiers, 65 % du corpus centre_aide) sont des pages d'archive/pagination WordPress, pas des articles documentaires. Diagnostic read-only du 09/09/2026 (échantillon de 10 `/tag/` + 5 `/page/`, 3 comparaisons directes tag↔article) : conclusion **INDEX_NAVIGATION_SEULEMENT** — les pages `/tag/` à article unique sont des doublons intégraux, caractère pour caractère, de l'article qu'elles référencent (25/25, 6/6, 2/2 blocs de 200 caractères identiques sur les 3 comparaisons) ; les pages `/tag/` multi-articles et `/page/N/` sont des index à extraits courts, aucun contenu propre. Décision actée : **collectées telles quelles** (comportement non modifié du script), **non supprimées, non exclues à ce stade**. Un audit séparé de canonicalité/déduplication est prévu avant toute décision d'exclusion analytique ou tout run LIGHT sur ce corpus. `EXCLUDED_SEGMENTS` ne couvre ni `tag` ni `page` — dette à ajouter à la liste de dette du collecteur (§ Dette du collecteur, ci-dessous) si une exclusion structurelle est un jour actée.

### Page juridique entrée au titre de la dette d'exclusion connue

**1 fichier** : `site_marketing/politique-rgpd.md` (`www.extrabat.com/politique-rgpd`) — politique de protection des données personnelles d'Extrabat France SAS elle-même (texte juridique complet, coordonnées `contact@extrabat.com`), non couverte par `EXCLUDED_SEGMENTS` (qui ne contient ni `rgpd` ni `politique-rgpd`). Gap de vocabulaire du même type que ceux déjà recensés pour sellsy/costructor/vertuoza, pas une régression propre à cette collecte. Non supprimé.

**Vérifiés et écartés (faux positifs, contenu éditorial légitime)** : `centre_aide/rgpd.md` et `centre_aide/le-rgpd-tout-savoir-sur-le-reglement-general-sur-la-protection-des-donnees.md` — articles d'aide expliquant aux clients d'Extrabat comment utiliser les fonctionnalités RGPD du logiciel (liens vers la CNIL, description du widget RGPD), pas la politique de confidentialité d'Extrabat elle-même. Correctement collectés. `centre_aide/tag/rgpd.md` déjà comptée dans la dette `/tag/` ci-dessus.

### Anomalies constatées, non corrigées

1. **Faux positifs `EXCLUDED_SEGMENTS` sur des slugs de tag homonymes.** `/tag/login`, `/tag/compte`, `/tag/cgv` ont été exclus non pas parce que ce sont des pages de connexion/compte/CGV, mais parce que leur slug de tag correspond littéralement à un segment de la liste d'exclusion. Sans conséquence documentaire (ce sont de toute façon des pages d'archive `/tag/`, déjà hors périmètre utile), mais signale que `EXCLUDED_SEGMENTS` ne distingue pas le rôle d'un segment de chemin de sa simple valeur textuelle.
2. **`canonicalize()` ne normalise pas le schéma http/https**, produisant des candidats dupliqués (ex. `http://.../de` et `https://.../de`) dans la liste de découverte. Sans conséquence sur le corpus final (`SKIP_EXISTING` absorbe le doublon au sein du même run), mais gonfle artificiellement les compteurs `discovered`/candidats.
3. **Couplage structurel confirmé** entre traversée (discovery) et conservation (écriture) dans `is_excluded_path()` : aucun mécanisme actuel ne permet d'exclure `/tag/`ou`/page/` de la sortie sans aussi les exclure de la traversée du crawl de secours — cf. diagnostic du 09/09/2026, aucune modification apportée à `collecte.py` en conséquence (hors périmètre de cette mission).
4. **`url_finale` porte un port `:443` explicite** (ex. `https://servicescompris.extrabat.com:443/...`) pour la totalité des fichiers `centre_aide`, jamais normalisé par `canonicalize()` (qui ne touche ni au schéma ni au port). Sans conséquence sur le nommage des fichiers (`compute_output_path` ne dépend que du chemin, pas de l'hôte), mais une future comparaison d'URL brute entre `url` et `url_finale` doit en tenir compte.

### Exclusions d'analyse (périmètre d'analyse ≠ périmètre de collecte, 09/09/2026)

Suite à la décision actée de conserver `/tag/` et `/page/N/` sur disque (ci-dessus), un audit de canonicalité/déduplication a été conduit avant tout run LIGHT sur ce corpus. **Aucun fichier de `sources/` n'a été supprimé, déplacé ou modifié** — `sources/` reste le snapshot de preuve intégral. Seul `corpus_index.json` distingue désormais, via `analysis_exclusions`, le périmètre de collecte (1670 fichiers `centre_aide`) du périmètre d'analyse.

**Méthode (par empreinte, sans lecture fichier par fichier)** : hash du corps de texte (frontmatter retiré, espaces normalisés) de chacun des 1670 fichiers `centre_aide`, regroupement par hash identique. Un groupe contenant au moins un fichier hors `/tag/` et hors `/page/` confirme un doublon exact, exclusion sans perte. Pour les groupes composés uniquement de fichiers `/tag/`ou`/page/` (contenu potentiellement unique), vérification par confinement (le corps est-il une sous-chaîne d'un article existant, y compris après retrait d'un éventuel en-tête `## [titre](lien)` propre au gabarit d'archive) — seuls ces cas ont fait l'objet d'une lecture réelle.

**Preuve de non-perte (étape bloquante)** :
- Sur 1169 fichiers `/tag/` (dont 100 sous `/de`, `/es`, `/en` — archives de tag localisées, absentes d'un simple comptage par dossier `centre_aide/tag/`) : 1112 doublons confirmés (998 par hash exact, 109 par confinement direct, 5 par confinement après retrait d'en-tête), 48 pages dont l'extraction a capturé le menu de navigation du site à la place du contenu réel (gabarit cassé pour ces tags précis — texte non documentaire, sans perte d'information puisqu'aucune réponse n'y est de toute façon présente), et **9 fichiers dont le contenu ne se retrouve nulle part ailleurs dans le corpus** : `tag/bibliotheque.md`, `tag/commande.md`, `tag/courrier.md`, `tag/creer-un-modele-de-courrier.md`, `tag/export-2.md`, `tag/inventaire.md`, `tag/stock.md`, `tag/moteur-de-recherche.md`, `tag/outils.md`. Contenu réel et substantiel (procédures complètes), lu individuellement. Cause de l'absence d'un article canonique séparé : **NON DÉTERMINABLE** — aucune ligne `HTTP_ERROR`, `ROBOTS_DENIED` ou `EXCLUDED` ne correspond à une URL candidate pour ce contenu dans `collecte.log`, et le crawl profondeur 4 (2077 candidats) n'a découvert aucune page séparée le portant. Hypothèse la plus probable, non vérifiable sans nouvelle collecte : contenu jamais publié sous son propre permalien, ou page supprimée côté site avec persistance de la relation de tag. **Ces 9 fichiers ne sont PAS exclus du périmètre d'analyse.**
- Sur 46 fichiers `/page/N/` (hors `/tag/`, hors sous-arbres de langue) : 26 résolus (17 par hash, 9 par confinement — pages d'archive chronologiques multi-articles, contenu déjà présent ailleurs par fragments), et **1 fichier dont le contenu ne se retrouve nulle part ailleurs** : `gestion-commerciale/page/7.md`, identique caractère pour caractère à `tag/commande.md` — même cause NON DÉTERMINABLE que ci-dessus, **non exclu**.
- 20 des 21 fichiers `/page/N/` restants après ces résolutions sont des pages d'index chronologiques multi-articles (contenu agrégé déjà présent ailleurs par fragments, cf. diagnostic INDEX_NAVIGATION_SEULEMENT du tour précédent) — safe à exclure.

**403 et collecte incomplète (étape 2)** : recherche stricte `HTTP 403` (avec espace, pour éviter les faux positifs de microsecondes d'horodatage ou de segments d'URL contenant la sous-chaîne « 403 ») dans `collecte.log` : **0 occurrence**, tous concurrents confondus. Le seul `HTTP_ERROR` du run extrabat reste le 404 déjà documenté. La réconciliation déjà écrite plus haut n'est pas affectée.

**Exclusions ajoutées** (mécanisme `analysis_exclusions` de `build_corpus_index.py`, motif distinct de `LEGAL_EXCLUSIONS` — inférées mécaniquement depuis `url_finale`, appliquées au seul concurrent `extrabat`, aucun autre corpus touché) :

| Motif | Définition | Fichiers exclus |
|---|---:|---:|
| `LANGUE_NON_FRANCAISE` | premier segment de chemin `de`/`es`/`en` (sous-arbre entier, tag/page inclus) | 223 |
| `ARCHIVE_TAXONOMIE` | segment `tag`, hors langue, hors les 9 exceptions ci-dessus | 1060 |
| `PAGINATION` | segment `page`+numéro, hors langue, hors tag, hors l'exception ci-dessus | 40 |
| **Total exclusions d'analyse** | | **1323** |

**`extrabat_help` : `file_count` (périmètre de collecte) = 1670 avant comme après — inchangé, aucun fichier supprimé.** Périmètre d'analyse (collecte − exclusions) = 1670 − 1323 = **347** (337 articles français réels + 9 pages `/tag/` + 1 page `/page/` préservées comme uniques copies de leur contenu).

`build_corpus_index.py` régénéré (24 corpus, 8 règles validées) ; `test_build_corpus_index.py` : **19/19 passent, aucune modification de test nécessaire** (le nouveau mécanisme utilise une constante séparée de `LEGAL_EXCLUSIONS`, sans effet sur `test_16_certain_1_ambiguous`).

## obat

Collecte réelle du 09/09/2026, via `collecte.py --concurrent obat`. Une première tentative (aide.obat.fr + www.obat.fr) a été tuée par le système (mémoire insuffisante) alors que le crawl profondeur 4 démarrait sur `www.obat.fr` ; `centre_aide` était déjà intégralement traité à ce moment (390/390 candidats). La reprise (`SKIP_EXISTING`) a sauté `centre_aide` sans le retraiter et complété `site_marketing` seul. Vérifications préalables (domaine canonique, robots.txt, plateforme, liens HTML) faites manuellement avant le lancement — non automatisées dans le code.

| Destination | Statut | Détail certifié |
|---|---|---|
| centre_aide | **Collecté, quasi complet** | 274 fichiers. Découverte : crawl de secours profondeur 4 (aucune ligne `Sitemap:` déclarée dans le robots.txt de `aide.obat.fr`, bien qu'un `sitemap.xml` existe réellement sur le serveur, 200/XML, urlset direct). 391 candidats découverts par le crawl = 274 FETCHED + 101 SKIP_EXISTING (doublons `?hsLang=fr`, `canonicalize()` ne filtre pas ce paramètre) + 14 HTTP 404 + 1 PDF. Réconciliation manuelle contre le sitemap réel non déclaré (§ ci-dessous) : 248/249 URLs retrouvées, 1 orpheline expliquée. |
| site_marketing | **Collecté — exhaustivité NON VÉRIFIABLE** | 695 fichiers + 9 PDF. Découverte : crawl de secours profondeur 4, mais pour une raison différente de aide.obat.fr — `www.obat.fr` ne publie **aucun sitemap à aucun emplacement usuel** (`/sitemap.xml`, `/sitemap_index.xml`, `/wp-sitemap.xml` tous testés en 404 le 09/09/2026, plateforme confirmée WordPress + PHP + MySQL, absence de plugin SEO ou sitemap natif désactivé — cause probable, non vérifiable de l'extérieur). **Cas identique à tolteck : aucune réconciliation externe possible.** Comptes bruts uniquement : 934 candidats découverts = 695 FETCHED + 186 SKIP_EXISTING (doublons `?sort=oldest/most-read/a-z/z-a` sur une vingtaine de pages catégorie/topic du blog, `canonicalize()` ne filtre pas `sort`) + 6 HTTP 404 + 9 PDF + 2 EXCLUDED (`login`, `cgv`) + 3 EXCLUDED_APRES_REDIRECTION (`/app`→`/login`, `/connect/google`→accounts.google.com/…/signin, `/app?target_ui=tools`→`/login`) + 1 ROBOTS_DENIED (`/app/referral`, `Disallow: /app/`) = 902 candidats expliqués sur 934 ; écart de 32 non journalisé par construction — actifs binaires non-PDF (`has_binary_ext`), jamais loggés dans ce cas de figure (même comportement que documenté pour extrabat), matérialité nulle. **Aucun chiffre ci-dessus n'est présenté comme preuve de complétude.** |

### Les deux hosts basculent en crawl profondeur 4, pour des raisons différentes — ne pas confondre

- `aide.obat.fr` : sitemap **existant mais non déclaré** dans robots.txt → réconciliation externe possible et faite (voir ci-dessous).
- `www.obat.fr` : sitemap **réellement absent**, à tout emplacement testé → aucune réconciliation externe possible, exhaustivité non vérifiable, même situation que tolteck (site_marketing).

### Réconciliation manuelle — centre_aide uniquement

`aide.obat.fr/sitemap.xml` récupéré manuellement le 09/09/2026 : urlset direct (pas un index), 249 URLs uniques.

- 248 des 249 URLs sitemap retrouvées parmi les 274 fichiers collectés (comparaison par chemin d'URL, indépendante du nom de fichier sur disque).
- **1 URL sitemap inexpliquée** : `https://aide.obat.fr/kb-search-results` — répond HTTP 200 (non vérifié en direct, seule son absence du crawl est établie), jamais atteinte par le crawl profondeur 4 depuis l'accueil (page de résultats de recherche HubSpot, probablement générée dynamiquement et non liée statiquement). Cause déterminée : **page orpheline non atteinte par le crawl**, matérialité nulle (page utilitaire, pas un article).
- **26 fichiers collectés absents du sitemap** : 24 pages de navigation/catégorie du centre d'aide HubSpot (ex. `devis.md`, `factures.md`, `planning.md`, `chantier.md`, `astuces.md`, `comptabilite.md`, `contacts.md`, `multi-user.md`, `pilotage.md`, `mon-abonnement.md`, etc. — pages courtes, 269 à 3641 octets, texte d'introduction propre à chacune, pas des doublons entre elles), 1 page utilitaire sans contenu documentaire (`hcms/mem/logout.md`, page de déconnexion HubSpot, cf. anomalies), et quelques articles réels non repris dans le sitemap pour une raison non déterminable (`lassistant-ia-dobat.md`, `la-consultation-bancaire-sur-obat.md`, `assistante-devis-vocal.md`, etc.). Ces 26 fichiers sont un **surplus** du crawl par rapport au sitemap, pas une perte : le corpus `centre_aide` est plus complet que le seul sitemap ne le suggérerait.
- 22 fichiers correspondent à des slugs HubSpot contenant un caractère `/` littéral dans le titre de l'article (ex. « Comment ajouter un client à votre devis/factures »), écrits par `collecte.py` dans une sous-arborescence (`comment-ajouter-un-client-c3-a0-votre-devis/factures.md`) plutôt qu'à plat. Vérifié un par un via le `url_finale` du frontmatter : aucune perte, simple effet de la segmentation de chemin par `compute_output_path()`.

**Collisions `?hsLang=fr` et `?sort=` : absorbées sans perte.** La réconciliation sitemap ci-dessus (248/249, le seul manquant étant une page orpheline non liée à un doublon de paramètre) démontre que les doublons de requête n'ont fait disparaître aucun contenu distinct sur `centre_aide`. Sur `site_marketing`, sans sitemap pour vérifier de la même façon, le raisonnement est structurel : `SKIP_EXISTING` ne saute que l'écriture d'un fichier déjà présent, jamais sa première tentative de récupération — une page listant plusieurs tris (`?sort=…`) est donc toujours récupérée au moins une fois avant qu'une variante ultérieure soit sautée.

### 403 stricts, PARSE_ERROR, contenus vides

Recherche stricte `HTTP 403` (avec espace) sur l'ensemble du log obat : **0 occurrence**. `PARSE_ERROR` : **0 occurrence**. Quelques fichiers très courts mais non vides repérés (`hcms/mem/logout.md` 236 octets, `site_marketing/resetting.md` 249 octets, `centre_aide/astuces.md` 269 octets) — ce sont des pages utilitaires (déconnexion, réinitialisation de mot de passe) ou des pages catégorie courtes, pas des échecs d'extraction.

### Pages juridiques entrées au titre de la dette d'exclusion connue

**2 fichiers** : `site_marketing/confidentialite.md` (politique de confidentialité d'Obat SAS) et `site_marketing/legal.md` (mentions légales d'Obat SAS : raison sociale, capital, RCS, TVA) — non couverts par `EXCLUDED_SEGMENTS` (qui ne contient ni `confidentialite` ni `legal`, seulement `privacy` et `mentions-legales`). Gap de vocabulaire du même type que ceux déjà recensés pour costructor/sellsy/vertuoza/extrabat, pas une régression propre à cette collecte. Non supprimés.

**Vérifiés et écartés (faux positifs, contenu éditorial légitime)** : `blog/cgv-batiment.md` (article expliquant ce que doivent contenir des CGV dans le bâtiment en général, pas les CGV d'Obat) et `blog/mentions-obligatoires-devis.md` (article sur les mentions obligatoires d'un devis BTP). Un PDF `cgv-batiment-obat.pdf` existe également parmi les ressources téléchargeables du blog (`wp-content/uploads/2020/06/CGV_Batiment_Obat.pdf`) ; sa nature (CGV propre à Obat vs modèle téléchargeable pour artisans, aux côtés d'autres modèles de devis dans le même dossier) n'a pas été tranchée — laissé **ambigu**, non compté dans les 2 ci-dessus, comparable au cas du barème sellsy.

### /blog/author/* et PDF

**6 pages `/blog/author/*`** (`laurie`, `mathilde`, `franck`, `flo`, `editorial-team`, `marianick-tobat-fr`) — archives auteur, correctement classées sous `site_marketing/blog/author/`, 0,7 % du corpus marketing, repérées dès le dry run. **9 PDF** sous `_assets_pdf/` proviennent de `blog/wp-content/uploads/` (modèles de devis, mandat de débours, CGV bâtiment) ; 1 PDF supplémentaire (`mandat-de-debours`) collecté côté `centre_aide` lors du premier passage (avant l'interruption) — 10 PDF au total, tous binaires, jamais convertis en texte.

### Sous-domaines identifiés, non collectés

Trois sous-domaines identifies le 09/09/2026 et NON COLLECTES : travaux.obat.fr, education.obat.fr, partenariats.obat.fr. Hors perimetre declare (site + doc uniquement), jamais atteints par le crawl puisque hosts_for() limite la portee au host declare. Nature du contenu non verifiee. Cas comparable a openfire : un editeur peut porter plusieurs proprietes documentaires ou editoriales distinctes. Vérification du 09/09/2026 : les trois répondent HTTP 200 (existence confirmée, contenu non exploré).

### Contenu ressemblant à une instruction adressée à une IA

**3 détections** (`INJECTION_RE`), toutes vérifiées individuellement, **toutes des faux positifs, aucune exécutée** : deux occurrences du paramètre de tracking `?utm_source=chatgpt.com` dans des liens sortants (`blog/nouveautes-btp-2026.md`, `blog/gestion-rh-btp.md`), et une occurrence de l'expression administrative française « donnant lieu à une nouvelle instruction » (`blog/qualification-opqibi.md`, sens bureaucratique du mot « instruction », sans rapport avec une IA). Contenu stocké tel quel dans les trois cas, comme prévu par le script.

### Exclusions d'analyse

**Aucune exclusion créée.** Le dry run puis la collecte réelle n'ont fait apparaître aucun motif d'archive, de taxonomie, de pagination ou de langue dépassant 1 % du corpus (à comparer aux 78 % du cas extrabat). Les pages de catégorie/navigation trouvées (`devis.md`, `factures.md`, etc. côté centre_aide ; une vingtaine de pages topic côté blog) contiennent chacune un texte d'introduction propre et distinct, pas un contenu dupliqué d'un article existant — la méthode par empreinte n'a pas été nécessaire. `obat` n'est pas ajouté à `ANALYTICAL_EXCLUSION_PRESERVE`.

### Anomalies constatées, non corrigées

1. **`canonicalize()` ne filtre ni `?hsLang=` (HubSpot) ni `?sort=`/`?campaign=`** (paramètres propres à obat), produisant les collisions décrites ci-dessus. Absorbées sans perte par `SKIP_EXISTING`, mais gonflent artificiellement les compteurs de candidats — même famille d'anomalie que le défaut de normalisation de schéma http/https déjà documenté pour extrabat.
2. **Vocabulaire d'exclusion incomplet pour les pages juridiques**, cette fois `confidentialite` et `legal` (voir ci-dessus) — même famille de gap que costructor/sellsy/vertuoza/extrabat.
3. **1 page utilitaire HubSpot sans contenu documentaire collectée** : `centre_aide/hcms/mem/logout.md` (page de déconnexion, 236 octets). `EXCLUDED_SEGMENTS` couvre les variantes de « login » mais pas « logout ». Cas isolé (1 fichier), pas une famille — aucune exclusion créée pour autant.
4. **1 page utilitaire similaire côté site_marketing** : `site_marketing/resetting.md` (réinitialisation de mot de passe, 249 octets). Même gap de vocabulaire (« reset »/« resetting » absent de `EXCLUDED_SEGMENTS`).
5. **32 candidats du crawl `site_marketing` non expliqués individuellement dans le log** — actifs binaires non-PDF (`has_binary_ext`), jamais journalisés par construction (`collecte.py` l. 658-659). Sans conséquence documentaire, même comportement que documenté pour extrabat.
6. **Log EXCLUDED pré-redirection étiqueté sous le label de cible (`obat:site_marketing`) plutôt que sous la destination résolue (`site_marketing`)**, contrairement à `ROBOTS_DENIED` et aux événements post-classement. Cosmétique, sans impact sur le corpus, repéré lors de la réconciliation.
7. **Interruption mémoire du 09/09/2026** : le premier lancement de `collecte.py --concurrent obat` a été tué par le système d'exploitation (mémoire insuffisante) au moment où il entamait le crawl profondeur 4 sur `www.obat.fr`, après avoir intégralement traité `centre_aide`. Reprise sans perte via `SKIP_EXISTING` : aucun fichier `centre_aide` retraité, `site_marketing` complété en une seconde exécution. Cause du pic mémoire non déterminée avec certitude (corrélée au volume du crawl profondeur 4, 934 URLs, mémoire consommée par le graphe de découverte en mémoire vive — hypothèse non vérifiée).

---

## Fichiers présents dans le snapshot mais à exclure des analyses de contenu

**16 fichiers certains, recomptés et vérifiés individuellement le
07/09/2026** (chemin, URL et titre lus un par un — jamais sur un mot du
corps du texte). Ces fichiers restent dans le snapshot brut afin de
préserver la traçabilité exacte de la collecte, mais ils sont **hors
périmètre des comptages et analyses de contenu concurrentiel** : ce sont
les pages légales/conformité du concurrent lui-même, pas des pages
produit ou marketing.

| # | Concurrent | Fichier | URL source | Motif |
|---:|---|---|---|---|
| 1 | batikko | `site_marketing/privacy-policy.md` | `batikko.com/privacy-policy` | Politique de confidentialité du site |
| 2 | costructor | `site_marketing/cookies.md` | `costructor.co/cookies` | Politique cookies du site |
| 3 | sellsy | `site_marketing/informations-legales/conditions-generales.md` | `go.sellsy.com/informations-legales/conditions-generales` | CGV du logiciel Sellsy |
| 4 | sellsy | `site_marketing/informations-legales/conditions-generales-offre-promotionnelle.md` | `.../conditions-generales-offre-promotionnelle` | CGV d'une offre promotionnelle |
| 5 | sellsy | `site_marketing/informations-legales/conditions-generales-programme-partenaire.md` | `.../conditions-generales-programme-partenaire` | CGV programme partenaire |
| 6 | sellsy | `site_marketing/informations-legales/conditions-generales-programme-revendeur.md` | `.../conditions-generales-programme-revendeur` | CGV programme revendeur |
| 7 | sellsy | `site_marketing/informations-legales/confidentialite-des-donnees.md` | `.../confidentialite-des-donnees` | Politique de confidentialité |
| 8 | sellsy | `site_marketing/informations-legales/securite-des-donnees.md` | `.../securite-des-donnees` | Politique de sécurité des données |
| 9 | sellsy | `site_marketing/informations-legales/politique-de-divulgation-de-vulnerabilite.md` | `.../politique-de-divulgation-de-vulnerabilite` | Politique de sécurité (vulnerability disclosure) |
| 10 | sellsy | `site_marketing/en/legal-information/general-terms-and-conditions.md` | `go.sellsy.com/en/legal-information/general-terms-and-conditions` | CGV (version anglaise) |
| 11 | sellsy | `site_marketing/en/legal-information/legal-notice.md` | `.../legal-notice` | Mentions légales (version anglaise) |
| 12 | sellsy | `site_marketing/en/legal-information/data-privacy.md` | `.../data-privacy` | Politique de confidentialité (version anglaise) |
| 13 | sellsy | `site_marketing/en/legal-information/data-security.md` | `.../data-security` | Politique de sécurité (version anglaise) |
| 14 | sellsy | `site_marketing/en/legal-information/vulnerability-disclosure-policy.md` | `.../vulnerability-disclosure-policy` | Politique de sécurité, vulnerability disclosure (version anglaise) |
| 15 | vertuoza | `site_marketing/nl-be/privacybeleid.md` | `vertuoza.com/nl-be/privacybeleid` | Politique de confidentialité (néerlandais, Belgique) |
| 16 | vertuoza | `site_marketing/nl-nl/privacybeleid.md` | `vertuoza.com/nl-nl/privacybeleid` | Politique de confidentialité (néerlandais, Pays-Bas) |

**1 cas ambigu, non compté dans les 16** : `sellsy/site_marketing/informations-legales/bareme-remise-programme-revendeur.md` (`go.sellsy.com/informations-legales/bareme-remise-programme-revendeur`) — un barème commercial de remises, classé par sellsy sous son répertoire légal mais n'étant pas lui-même un document juridique (CGU/CGV/confidentialité/sécurité). Laissé dans le snapshot sans statut tranché.

**Fichiers vérifiés et écartés de cette liste après lecture** (faux
positifs d'un scan par mot-clé, contenu éditorial légitime, correctement
collecté) : 2 articles de blog costructor, 1 article centre_aide progbat,
2 articles inter-fast, 5 articles de blog vertuoza (3 locales ×
« mentions légales devis » + 2 « sécurité chantier »), 1 guide leobati.
Le détail de cette vérification est dans les sections par concurrent
ci-dessus.

> Doctrine : ces 16 fichiers restent dans le snapshot brut afin de
> préserver la traçabilité exacte de la collecte, mais ils sont hors
> périmètre des comptages et analyses de contenu concurrentiel. Ne pas
> les déplacer, ne pas les supprimer, ne pas les altérer.

### Dette du collecteur — vocabulaire à envisager pour un FUTUR run

Liste de segments de chemin à évaluer pour une future révision de
`EXCLUDED_SEGMENTS` dans `collecte.py`. **Non appliqué maintenant** :

```
cookies
cookie-policy
privacy-policy
privacy-notice
privacybeleid            (NL — trouvé en usage reel, vertuoza)
conditions-generales
informations-legales
legal-notice
legal-information
terms-of-service
terms-and-conditions
general-terms-and-conditions
data-privacy
data-security
securite-des-donnees
confidentialite-des-donnees
vulnerability-disclosure-policy
politique-de-divulgation-de-vulnerabilite
```

Constat structurel à arbitrer en même temps : sellsy et vertuoza
organisent leurs pages légales dans un **répertoire dédié entier**
(`/informations-legales/`, `/en/legal-information/`) plutôt que des
pages isolées. Une règle par répertoire (« tout ce qui est sous
`/informations-legales/` ») serait plus robuste qu'une liste de mots
isolés, mais changerait la nature de la règle d'exclusion (actuellement
par segment de chemin, pas par arborescence) — décision de conception,
pas une correction mécanique.

---

## Audit de classement A–E (tous concurrents, tous fichiers non-historiques)

**0 violation détectée** sur les 3 312 fichiers audités (`centre_aide` +
`site_marketing` + `documentation_2` de tous les concurrents) :
- A (mauvaise destination) : 0
- B (hors périmètre autorisé) : 0
- C (même URL dans plusieurs destinations) : 0
- D (plusieurs fichiers pour une même URL) : 0
- E (URL source illisible/absente) : 0

---

## Anomalies techniques signalées, non corrigées

1. **Écriture concurrente non protégée sur `collecte.log`.** Plusieurs
   processus `collecte.py` lancés en parallèle le 07/09 ont occasionnellement
   perdu une ligne `FETCHED` (5 cas sur ~5000, tous confirmés présents et
   complets sur disque). Cause : `Journal` ouvre le fichier en mode append
   sans verrou OS. À arbitrer : verrou fichier, ou log par processus fusionné
   après coup.
2. **Sémantique ambiguë du bilan console.** `discovered` dans `print_summary`
   exclut les URLs exclues/déjà présentes alors que `DISCOVERY_MODE` dans le
   log compte le total brut ; `skipped` agrège cinq causes distinctes. Non
   corrigé dans ce chantier (modification de la seule couche d'affichage
   possible mais non effectuée — à arbitrer).
3. **Vocabulaire d'exclusion incomplet pour les pages juridiques.** Ne
   couvre pas `cookies`, `conditions-generales`, `informations-legales`,
   `legal-notice` (voir sellsy, costructor). Le passage en comparaison par
   segment exact (correctif du 06/09) a aussi fait perdre `privacy-policy`
   chez batikko (couvert auparavant par un matching plus large mais plus
   permissif). Aucune correction appliquée — inventaire seulement.
4. **Crawl de secours (profondeur 4) chez tolteck** : écart non expliqué de
   1 URL entre le total découvert (204) et le total tracé (203). Cause
   NON_DETERMINABLE, matérialité faible.

**Règle opérationnelle future :** ne pas exécuter plusieurs instances de
`collecte.py` partageant le même `collecte.log` tant qu'aucun mécanisme
de verrouillage de fichier ou de journal séparé par processus n'existe.

---

## Gel et versionnement (2026-09-07)

Le snapshot a été figé et commité : `git log -1` = `8b9d03b` — « collecte:
gel du corpus concurrentiel certifie ». 4083 fichiers versionnés (~38 Mo :
`site_marketing/`, `centre_aide/`, `documentation_2/`, `_assets_pdf/`
pour les 10 concurrents, ce `COUVERTURE.md`, `tools/collecte/*.py`,
`sources.yaml`, `collecte.log`). `git status --short` propre après
commit. Aucun fichier historique déplacé/modifié, aucune fusion openfire,
aucun `--force`.

`.gitignore` corrigé : `site_marketing/`/`centre_aide/` étaient exclus
par une règle d'origine, alors que `documentation_2/` et `_assets_pdf/`
ne l'étaient pas — incohérence corrigée, les quatre familles sont
désormais traitées à l'identique (versionnables). `tools/collecte/cache/`
(~663 Mo) reste exclu sans exception. `tools/collecte/collecte.log` a
reçu une exception explicite après audit (aucun secret/token/cookie,
seul le nom d'utilisateur Windows local apparaît dans les chemins
absolus des lignes de log — signalé, jugé non sensible).

Dépôt sans remote configuré au moment du gel (`git remote -v` vide) :
le commit existe uniquement en local. Voir le rapport de session pour le
détail.
