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
| Plateforme documentaire | Note | La documentation `centre_aide` est servie via GitBook (`docv5.progbat.com`). GitBook y expose `llms.txt` et `llms-full.txt` — constatés lors d'un diagnostic le 2026-09-08, potentiellement utiles pour une future collecte. Non exploités par la collecte actuelle. |
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
