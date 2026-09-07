# Arborescence du dépôt — ce qui a été collecté, depuis où, à quoi ça sert

Document de lecture, écrit pour quelqu'un qui reprend ce projet sans être
développeur. Il ne recommande rien, ne juge pas la qualité des données :
il décrit ce qui existe réellement sur le disque, vérifié fichier par
fichier au moment de la rédaction (2026-09-07).

Deux mots reviennent tout du long :
- **« Historique »** : collecté à la main avant le 06/09/2026, avant que
  l'outil automatique n'existe.
- **« Nouveau »** : collecté automatiquement les 06 et 07/09/2026 par un
  programme (`tools/collecte/collecte.py`).

---

## 1. Tableau des sources par concurrent

Une ligne par concurrent et par type de contenu collecté. Chaque ligne a
été vérifiée : l'adresse (URL) lue dans l'en-tête des fichiers markdown
correspond à un seul domaine internet (aucun dossier ne mélange deux
sites), sauf mention contraire.

| Concurrent | Contenu (dossier) | URL racine exacte | Type de source | Méthode | Fichiers .md | Autres fichiers | Poids | Date de collecte |
|---|---|---|---|---|---:|---|---:|---|
| axonaut | rubriques historiques (18 dossiers) | `support.axonaut.com` | Centre d'aide | Scraping manuel initial | 127 | 0 | 0,89 Mo | 2026-09-05 |
| axonaut | `site_marketing/` | `axonaut.com` | Site commercial | Collecte automatisée | 50 | 0 | 0,33 Mo | 2026-09-07 |
| axonaut | `_assets_pdf/` | `axonaut.com` | Documents PDF téléchargés depuis le site commercial | Collecte automatisée | 0 | 4 PDF | 7,57 Mo | 2026-09-07 |
| costructor | rubriques historiques (10 dossiers) | `support.costructor.co` | Centre d'aide | Scraping manuel initial | 112 | 0 | 0,22 Mo | 2026-09-05 |
| costructor | `site_marketing/` | `costructor.co` | Site commercial | Collecte automatisée | 181 | 0 | 1,53 Mo | 2026-09-07 |
| inter-fast | rubriques historiques (9 dossiers) | `help.inter-fast.co` | Centre d'aide | Scraping manuel initial | 221 | 0 | 2,45 Mo | 2026-09-05 |
| inter-fast | `site_marketing/` | `inter-fast.fr` | Site commercial | Collecte automatisée | 799 | 0 | 6,87 Mo | 2026-09-07 |
| openfire | rubriques historiques (4 dossiers) | `support.openfire.fr` | Centre d'aide (plateforme Zendesk) | Scraping manuel initial | 127 | 0 | 0,79 Mo | 2026-09-05 |
| openfire | `site_marketing/` | `openfire.fr` | Site commercial | Collecte automatisée | 166 | 0 | 1,16 Mo | 2026-09-07 |
| openfire | `documentation_2/` | `documentation.openfire.fr` | Documentation technique (plateforme Odoo, **distincte** du centre d'aide ci-dessus) | Collecte automatisée | 213 | 0 | 0,66 Mo | 2026-09-06 |
| sellsy | rubriques historiques (20 dossiers) | `help.sellsy.com` | Centre d'aide | Scraping manuel initial | 462 | 0 | 2,38 Mo | 2026-09-05 |
| sellsy | `site_marketing/` | `go.sellsy.com` | Site commercial | Collecte automatisée | 882 | 0 | 5,66 Mo | 2026-09-07 |
| vertuoza | rubriques historiques (22 dossiers) | `intercom-help.eu` (plateforme tierce, pas le domaine de vertuoza.com) | Centre d'aide | Scraping manuel initial | 433 | 0 | 0,75 Mo | 2026-09-05 |
| vertuoza | `site_marketing/` | `www.vertuoza.com` | Site commercial | Collecte automatisée | 1213 | 0 | 10,52 Mo | 2026-09-07 |
| batikko | `centre_aide/` | `batikko.com/documentation` | Centre d'aide | Collecte automatisée | 14 | 0 | 0,07 Mo | 2026-09-07 |
| batikko | `site_marketing/` | `batikko.com` | Site commercial | Collecte automatisée | 46 | 0 | 0,33 Mo | 2026-09-07 |
| progbat | `centre_aide/` | `docv5.progbat.com` | Centre d'aide | Collecte automatisée | 190 | 0 | 0,46 Mo | 2026-09-06 |
| progbat | `site_marketing/` | `www.progbat.com` | Site commercial | Collecte automatisée | 50 | 0 | 0,37 Mo | 2026-09-06 |
| tolteck | `centre_aide/` | `help.tolteck.com` (jamais atteint) | Centre d'aide | **Bloqué**, voir §7 | 0 | 0 | 0 | — |
| tolteck | `site_marketing/` | `www.tolteck.com` | Site commercial | Collecte automatisée | 199 | 0 | 2,00 Mo | 2026-09-07 |
| leobati | `site_marketing/` | `www.leobati.fr` | Site commercial | Collecte automatisée | 70 | 0 | 0,26 Mo | 2026-09-07 |

Leobati n'a pas de ligne « centre_aide » : ce dossier n'existe pas — voir §7.

**Cohérence des adresses.** Pour les 4 077 fichiers « nouveaux », l'adresse
lue dans le champ `url:` de l'en-tête et celle lue dans le champ
`url_finale:` (l'adresse réelle après redirection éventuelle) ont été
comparées une par une : **aucun écart de domaine trouvé**. Pour les
1 494 fichiers « historiques », il n'existe qu'un seul champ d'adresse
(`source:`) — il n'y a rien à comparer, mais il est présent et lisible
sur les 1 494.

---

## 2. Détail par concurrent

### axonaut
- `axonaut-et-votre-secteur-activite/` (2) — `evenementiel-pourquoi-axonaut-est-adapte-a-votre-activite.md`, `franchises-comment-gerer-votre-reseau-avec-axonaut.md`
- `centralisez-gestion-emails-courriers/` (11) — `ajout-rapide-par-email.md`, `comment-ajouter-un-contact-depuis-gmail-ou-outlook.md`, `comment-synchroniser-ses-emails-google-workspace-avec-axonaut.md`
- `centralisez-gestion-sav/` (2), `commandes-clients-fournisseurs/` (2), `compte-pro-cartes/` (9), `configurer-votre-compte/` (12), `connectez-axonaut/` (5), `creez-campagnes-marketing/` (8), `creez-depenses-facilement/` (7), `etat-tresorerie-temps-reel/` (5), `gerez-rentabilite-projets/` (2), `gerez-ressources-humaines/` (1), `gerez-stock-temps-reel/` (5), `gerez-vos-devis/` (13), `gerez-vos-factures/` (20), `gerez-vos-produits/` (2), `gerez-votre-comptabilite/` (6), `optimisez-gestion-commerciale/` (15)
- `site_marketing/` (50) — `administrative-assistant.md`, `affiliation.md`, `a-propos.md`
- `_assets_pdf/` (4) — `guide-demarrage.pdf`, `optimiser-la-performance-de-sa-tpe-pme.pdf`, `plaquette.pdf`
- URL au hasard : `https://support.axonaut.com/centralisez-gestion-emails-courriers/ajout-rapide-par-email/`
- Ce qui manque : rien de bloqué. Les 4 PDF sont stockés tels quels (jamais convertis en texte) — voir §3.

### costructor
- `abonnement/` (9), `achats/` (3), `chantiers/` (6), `debuter-sur-costructor/` (31), `equipe-collaborateurs/` (4), `gestion-dentreprise/` (4), `imports-exports/` (7), `securite/` (2), `site-internet/` (1), `ventes/` (45)
  - exemples `abonnement/` : `comment-ajouter-un-utilisateur-additionnel-j9e14d.md`, `comment-ajouter-une-seconde-entreprise-c2jr6v.md`, `comment-beneficier-de-loffre-jeune-entreprise-1vs4eiy.md`
- `site_marketing/` (181) — `adequation.md`, `alpha-sud.md`, `alteridea.md`
- URL au hasard : `https://support.costructor.co/fr/article/comment-creer-un-chantier-ub213u/`
- Ce qui manque : rien de bloqué.

### inter-fast
- `application-mobile/` (28), `application-web/` (3), `debuter-avec-interfast/` (20), `equipe/` (16), `finances/` (48), `fluides-frigorigenes/` (8), `mon-entreprise/` (35), `operations/` (27), `outils/` (36)
  - exemples `finances/` : `activer-la-validation-des-commandes-fournisseurs.md`, `ajouter-une-depense-app-web.md`, `comprendre-la-fiche-d-un-devis.md`
- `site_marketing/` (799) — `calculator.md`, `batigest-vs-codial.md`, `batigest-vs-costructor.md`
- URL au hasard : `https://inter-fast.fr/ressources/guides/fiches-de-poste/charge-de-relation-client`
- Ce qui manque : rien de bloqué. Site commercial très volumineux (799 pages) — beaucoup de pages comparatives contre d'autres logiciels (« X-vs-Y ») et de fiches métiers.

### openfire
- `bien-debuter/` (10), `configurer-openfire/` (39), `guides-videos/` (26), `utiliser-openfire/` (52) — ensemble = centre d'aide historique
  - exemples `configurer-openfire/` : `achats-intracommunautaires-et-autoliquidation-comptabilite-francaise.md`, `activer-et-parametrer-l-emission-de-vos-factures-clients.md`, `activer-et-parametrer-la-reception-des-factures-fournisseurs.md`
- `documentation_2/` (213) — `dm-openfire-fr.md`, `faq.md`, `index.md` — **second corpus documentaire, distinct**, voir §7
- `site_marketing/` (166) — `logiciel-cheminee.md`, `logiciel-gestion-des-fluides.md`, `logiciel-gestion-intervention-technique.md`
- URL au hasard (centre d'aide historique) : `https://support.openfire.fr/hc/fr/articles/18985859599644-Caract%C3%A9ristiques-techniques-et-configurations-requises`
- URL au hasard (documentation_2) : `https://documentation.openfire.fr/knowsystem/les-modeles-de-devis-2`
- Ce qui manque : rien de bloqué, mais deux documentations différentes coexistent sans avoir été comparées — voir §7.

### sellsy
- 20 rubriques historiques : `app-mobile-sellsy-crm/` (18), `catalogue-produits-et-services/` (16), `configuration-du-compte/` (42), `conseils-d-utilisation/` (20), `crm-et-prospection/` (32), `documents-de-vente/` (68), `facturation-electronique/` (36), `gestion-des-donnees/` (35), `integrations-et-api/` (30), `module-achats/` (10), `module-marketing/` (7), `module-stocks/` (11), `module-support/` (5), `module-tresorerie/` (2), `paiements/` (19), `rapports-et-pilotage/` (40), `repertoire/` (20), `sellsy-automatisations/` (13), `sellsy-ia/` (6), `suivi-financier/` (32)
  - exemples `documents-de-vente/` : `activer-et-configurer-le-module-de-signature-electronique.md`, `activer-le-mode-conforme-pour-les-documents-de-vente.md`, `activer-le-prelevement-automatique-pour-le-reglement-des-factures-d-abonnements-gocardless.md`
- `site_marketing/` (882) — `activer-le-module-tresorerie.md`, `alimenter-son-previsionnel-de-tresorerie.md`, `analyser-et-comprendre-son-suivi-de-tresorerie.md`
- URL au hasard : `https://go.sellsy.com/blog/crm-manager-fiche-metier-missions-et-formation`
- Ce qui manque : rien de bloqué. Contient 12 pages juridiques propres à Sellsy (CGV, confidentialité, sécurité) à écarter de toute analyse de contenu — voir §7.

### vertuoza
- 22 rubriques historiques dont `faq-foires-aux-questions/` (238, la plus grosse), `parametres/` (62), `gestion-de-chantier/` (17), `application-mobile/` (15), `documents/` (16), `finance/` (12), `stock/` (10) ; les autres font moins de 10 fichiers chacune (`beta`, `bibliotheque-de-prix`, `contacts`, `crm`, `demarrer`, `devis`, `fiches-techniques`, `gestion-des-interventions`, `notifications`, `planning`, `rh`, `statistiques`, `tableau-de-bord`, `taches`, `vertuowork`)
  - exemples `faq-foires-aux-questions/` : `a-quoi-sert-une-retenue-de-garantie-dans-un-devis.md`, `comment-activer-la-facturation-electronique-peppol-dans-vertuoza.md`, `comment-activer-les-preferences-d-affichage-pour-un-devis.md`
- `site_marketing/` (1213, le plus gros dossier du dépôt) — `a-propos.md`, `4-astuces-pour-trouver-des-chantiers.md`, `5-astuces-pour-bien-gerer-son-parc-materiel.md`
- URL au hasard : `https://www.vertuoza.com/fr-ch/blog/reception-des-travaux`
- Ce qui manque : rien de bloqué. Site commercial disponible en plusieurs langues/pays (France, Belgique, Suisse, Pays-Bas) — toutes les variantes sont mélangées dans le même dossier `site_marketing/`.

### batikko
- `centre_aide/` (14) — `chantiers.md`, `clients-crm.md`, `conformite-2026.md`
- `site_marketing/` (46) — `canicule-et-batiment-gerer-la-securite-chantier-et-l-administratif-avec-batikko.md`, `digitalisation-suivi-chantier-fini-le-papier.md`, `etude-cas-electricien-double-chiffre-affaires.md`
- URL au hasard : `https://batikko.com/documentation/guides/planning`
- Ce qui manque : rien de bloqué. `site_marketing/privacy-policy.md` est la politique de confidentialité du site — à écarter de toute analyse de contenu, voir §7.

### progbat
- `centre_aide/` (190, la plus grosse documentation technique du dépôt) — `application-mobile.md`, `la-documentation.md`, `le-support-technique.md`
- `site_marketing/` (50) — `achats.md`, `avenant-btp-devis-supplementaire-levier-rentabilite-securite-juridique-chantiers.md`, `bibliotheques-prix.md`
- URL au hasard : `https://docv5.progbat.com/les-options/pourquoi-des-options/signature-electronique`
- Ce qui manque : rien de bloqué.

### tolteck
- `centre_aide/` — **dossier vide**, jamais rempli, voir §7
- `site_marketing/` (199) — `4-etapes-cles-a-appliquer-pour-etre-bien-reference.md`, `7-raisons-de-creer-un-site-internet-dartisan.md`, `accompagnement-cee-maprimerenov-gratuit.md`
- URL au hasard : `https://www.tolteck.com/fr-fr/presence-en-ligne`
- Ce qui manque : le centre d'aide entier (`help.tolteck.com`) — voir §7. Aucune rubrique historique pour tolteck (il n'était pas parmi les six concurrents collectés avant le 06/09).

### leobati
- `site_marketing/` (70) — `alternative-obat-tolteck-batappli.md`, `equipe.md`, `facturation-2026.md`
- URL au hasard : `https://www.leobati.fr/guides/facture-de-situation-chantier`
- Ce qui manque : le centre d'aide entier (`/bati/guide`) — voir §7. Comme tolteck, aucune rubrique historique.

---

## 3. Inventaire par extension (tout le dépôt)

| Extension | Nombre | Poids total | Où | Produits par | À quoi ça sert |
|---|---:|---:|---|---|---|
| `.md` | 5 581 | 38,19 Mo | `01-discovery/` en entier | Scraping manuel (1 494) + `collecte.py` (4 077) + rédaction humaine/assistée (documents de méthode, mini-audits, décisions, ce document) | Le contenu lisible : articles de centre d'aide, pages de site commercial, et toute la documentation du projet lui-même |
| `.bin` | 4 086 | 693,66 Mo | `tools/collecte/cache/<concurrent>/raw/` | `collecte.py`, automatiquement, à chaque page récupérée avec succès | **Cache technique.** Ouvert un exemplaire : c'est la page HTML brute telle que reçue du site (commence par `<!DOCTYPE html>...`), nommée par une empreinte (hash) de son adresse. Sert uniquement à éviter de retélécharger une page déjà récupérée si le programme est relancé. **Confirmé : pur cache, aucune information qui ne soit pas déjà dans les `.md`.** |
| `.pdf` | 4 | 7,57 Mo | `01-discovery/concurrents/sources/axonaut/_assets_pdf/` | Téléchargés tels quels par `collecte.py` depuis le site d'axonaut | Documents commerciaux (plaquette, guide de démarrage...) conservés en l'état, jamais convertis en texte dans ce chantier |
| `.log` | 1 | 2,36 Mo | `tools/collecte/collecte.log` | `collecte.py`, une ligne à chaque action | Le journal complet de la collecte : quelle page a été récupérée, ignorée, exclue, en erreur, et quand. Sert de preuve d'audit. |
| `.json` | 10 | 1,74 Mo | `tools/collecte/cache/<concurrent>/index.json`, un par concurrent | `collecte.py` | Ouvert un exemplaire : une liste d'adresses, chacune avec son statut, l'adresse finale après redirection, le type de contenu, le chemin du fichier `.bin` correspondant et la date. **C'est l'index du cache** — il dit où retrouver quelle page brute, mais ne contient aucun texte lui-même. **Confirmé : cache technique.** |
| `.yaml` | 41 | 0,29 Mo | 1 dans `tools/collecte/` (config de collecte), 40 dans `01-discovery/concurrents/extracted/` (résultat d'analyse) | 1 écrit à la main (config), 40 produits par un travail d'extraction manuelle/assistée à partir des `.md` historiques | Voir §4 |
| `.py` | 2 | 0,04 Mo | `tools/collecte/` | Écrits pour ce chantier | Le programme de collecte (`collecte.py`) et ses tests automatiques (`test_collecte.py`) |
| `.pyc` | 2 | 0,05 Mo | `tools/collecte/__pycache__/` | Généré automatiquement par Python quand `.py` est exécuté | Fichier technique de démarrage plus rapide de Python. Sans utilité en soi, se régénère tout seul, jamais versionné dans git. |
| *(sans extension)* | 1 | ~0 | racine du dépôt | Écrit à la main | `.gitignore` — la liste des fichiers que git ne doit jamais suivre |

---

## 4. Ce qui a été produit par l'analyse

Cette section ne concerne que trois concurrents sur les dix : **Vertuoza,
InterFast et Sellsy**. Les rubriques historiques d'axonaut, costructor et
openfire ont été collectées mais **jamais analysées** dans ce chantier —
voir §7. Aucun des quatre nouveaux concurrents (tolteck, progbat, batikko,
leobati) ni aucun contenu `site_marketing/`/`documentation_2/` n'est
concerné par cette section.

- **`01-discovery/concurrents/extracted/{inter-fast,sellsy,vertuoza}/*.yaml`
  (40 fichiers)** — le résultat concret du travail d'analyse : pour
  chaque article de centre d'aide choisi, une description structurée de
  qui fait quoi, avec quelle preuve (citation exacte de la source), les
  ruptures d'information observées, etc. Toujours d'actualité : c'est la
  matière brute sur laquelle les documents suivants raisonnent. Vérifié :
  chacun des 40 fichiers correspond bien à un article encore présent dans
  les rubriques historiques (aucun fichier orphelin).
- **`SCHEMA-V2.md`** — la règle du jeu de cette extraction : quels
  champs remplir, sept règles à respecter (par exemple : ne jamais
  affirmer une rupture sans preuve écrite dans la source), et les huit
  types d'action reconnus (visibilité, affectation, permission,
  transmission, validation, notification, édition partagée,
  automatisation). Toujours d'actualité — c'est la version en vigueur.
- **`audit-pilote-A.md`** — le constat qui a fait abandonner la
  **version précédente** du schéma (« V1 ») : six erreurs où un score
  numérique gonflait artificiellement l'importance d'un fait mal établi.
  Dépassé en tant que méthode (V1 n'est plus utilisée) mais gardé comme
  preuve de pourquoi V2 existe.
- **`mini-audit-V2.md`** — la vérification que le nouveau schéma (V2)
  corrige bien les six erreurs, sur 30 articles. Toujours d'actualité :
  c'est le document qui a validé V2 pour la suite, et qui a fait
  remonter onze premiers cas problématiques (CP-1 à CP-11 ; deux autres,
  CP-12 et CP-13, viennent du document suivant).
- **`crash-test-utilite-pilote-A.md`** — un test différent : est-ce que
  les données extraites permettent réellement de répondre à des
  questions concrètes (comparer deux concurrents sur un même sujet,
  retracer un dossier d'un bout à l'autre) ? Toujours d'actualité :
  c'est de là que viennent CP-12 (les noms d'objets ne sont pas
  normalisés — gros problème pour comparer) et CP-13.
- **`mini-audit-B.md`** — la même vérification sur un deuxième lot de
  10 articles, choisis cette fois pour forcer des cas de coordination
  entre plusieurs personnes. Toujours d'actualité : il ajoute cinq
  nouveaux cas (CP-14 à CP-18) et confirme que sept des onze premiers
  cas ne sont pas des accidents isolés.
- **`REGISTRE-CP.md`** — l'index unique des 18 cas problématiques,
  avec pour chacun : à quel axe de recherche il se rattache, son statut
  (isolé, récurrent, structurel...) et l'ordre dans lequel les traiter.
  Toujours d'actualité, et c'est le document le plus récent de la
  série — **aucun des 18 cas n'a été corrigé**, ce registre les liste,
  il ne les résout pas.

---

## 5. La doctrine

`docs/decisions/` (numérotées, dans l'ordre où elles ont été écrites) et
le schéma d'extraction :

- **`0001-hypothese-initiale.md`** — tranche : l'idée de départ (« les
  concurrents gèrent mal le travail à plusieurs ») est-elle vraie ? Réponse : fausse pour Vertuoza et InterFast, à reformuler.
- **`0002-carte-metier-initiale.md`** — tranche : quel schéma de
  référence utiliser pour situer un article dans le parcours d'une
  affaire (devis → chantier → facture...) ? Explicitement une hypothèse
  de travail, pas une vérité imposée aux concurrents.
- **`0003-hypotheses-continuite.md`** — tranche : que veut-on dire
  précisément par « continuité » ? Définit deux notions séparées (entre
  étapes d'un même dossier ; entre personnes différentes) à ne jamais
  confondre.
- **`0004-architecture-assessment.md`** — tranche : comment séparer
  ce que documente un centre d'aide, ce qu'affirme un site commercial,
  et le croisement des deux. Prévoit un futur schéma d'extraction pour
  le contenu marketing — **non construit à ce jour**, voir §7.
- **`0005-axes-de-recherche.md`** — tranche : quels axes de recherche
  garder après les deux premiers essais, et dans quel ordre traiter les
  18 cas problématiques.
- **`SCHEMA-V2.md`** (dans `analysis/`, pas `docs/decisions/`, mais
  c'est bien une pièce de doctrine) — tranche : la structure technique
  exacte de l'extraction (voir §4).

**Recoupements et contradictions.** Aucune contradiction trouvée entre
ces documents : chacun s'appuie explicitement sur les précédents et dit
ce qu'il ne remplace pas. Un recoupement à noter, pas une contradiction :
`0002` et `0003` parlent tous les deux de continuité, mais `0002` pose le
schéma général du parcours d'une affaire tandis que `0003` en tire deux
définitions précises et testables — le second affine le premier, il ne
le double pas. Le seul écart réel est un **engagement non tenu** :
`0004` décide qu'un second schéma d'extraction, plus léger, doit être
conçu pour le contenu marketing — ce schéma n'existe pas, voir §7.

---

## 6. L'outillage

`tools/collecte/` contient tout ce qui a servi à la collecte automatisée :

- **`collecte.py`** (870 lignes) — le programme lui-même : il lit
  `sources.yaml`, respecte les règles `robots.txt` de chaque site,
  cherche un plan du site (sitemap), télécharge les pages, les
  transforme en texte lisible (markdown) et les range au bon endroit.
- **`sources.yaml`** — la liste des dix concurrents avec, pour chacun,
  son adresse de centre d'aide, son adresse de site commercial, et des
  notes sur les cas particuliers rencontrés.
- **`test_collecte.py`** — 24 vérifications automatiques du programme
  (par exemple : une adresse comme `/compte-cle-en-main` ne doit pas
  être confondue avec `/compte`). Reproductible : se relance en une
  commande, sans rien télécharger.
- **`collecte.log`** — le journal, décrit en §3.

**Reproductible sans perte :** `collecte.py`, `sources.yaml`,
`test_collecte.py`. Les relancer reproduit la méthode à l'identique.

**Reproductible avec nuance :** relancer `collecte.py` aujourd'hui ne
redonnera pas exactement les mêmes fichiers, puisque les sites des
concurrents changent avec le temps. C'est attendu, pas un défaut.

**Peut disparaître sans perte :** `tools/collecte/cache/` (693,66 Mo,
uniquement des copies techniques déjà transformées dans `sources/`) et
`tools/collecte/__pycache__/` (fichiers Python générés automatiquement).
Supprimer l'un ou l'autre n'efface aucune information : ils se
reconstruisent en relançant le programme.

---

## 7. Les trous

**Ce qui manque et devrait exister :**
- Le centre d'aide **tolteck** (`help.tolteck.com`) — jamais récupéré,
  le site présente un certificat de sécurité invalide pour ce nom
  d'adresse. Aucun contournement n'a été tenté.
- Le centre d'aide **leobati** (`/bati/guide`) — c'est une page unique
  qui affiche son contenu par onglets chargés après coup par le
  navigateur ; le programme de collecte ne voit que l'onglet affiché
  par défaut, et cette page n'apparaît même pas dans le plan du site.
- Un schéma d'extraction pour le contenu **site_marketing** — prévu par
  la décision `0004`, jamais construit. Résultat : sur les 4 077
  fichiers « nouveaux » (38 Mo, la quasi-totalité du contenu récent),
  **aucun n'a été analysé** au sens du §4 — ce sont des pages brutes,
  pas encore travaillées.
- L'analyse des rubriques historiques **axonaut, costructor et
  openfire** — collectées le 05/09 comme les trois autres, mais jamais
  passées par le travail d'extraction décrit en §4, qui n'a porté que
  sur Vertuoza, InterFast et Sellsy.
- Une comparaison entre les deux documentations openfire
  (`utiliser-openfire/` etc. et `documentation_2/`) — les deux existent,
  aucune des deux notes n'a été confrontée à l'autre.

**Ce qui existe et pourrait surprendre :**
- `01-discovery/concurrents/sources/tolteck/centre_aide/` — un dossier
  **vide**, créé avant que le blocage de sécurité ne soit découvert,
  jamais rempli depuis, jamais suivi par git (git ne garde pas les
  dossiers vides). Il ne représente aucune donnée.
- 16 fichiers dans plusieurs `site_marketing/` (Batikko 1, Costructor 1,
  Sellsy 12, Vertuoza 2) sont les pages légales des concurrents
  eux-mêmes (conditions générales, politique de confidentialité,
  sécurité des données) — conservées pour la trace complète de la
  collecte, mais à écarter de toute analyse de contenu produit. La
  liste exacte, fichier par fichier, est dans
  `01-discovery/concurrents/sources/COUVERTURE.md`.
- Les 18 cas problématiques du `REGISTRE-CP.md` (§4) sont tous encore
  ouverts — aucun n'a été résolu, c'est documenté comme tel.

**Doublons :** aucun trouvé. Une vérification systématique (toutes les
adresses de tous les fichiers « nouveaux », comparées entre elles) n'a
révélé aucune adresse présente deux fois, ni dans le même dossier ni
dans deux dossiers différents.

**Origine ou usage non déterminable :** aucun fichier de contenu
(`.md`, `.pdf`) n'est dans ce cas — chacun a une adresse d'origine
lisible et un dossier de destination cohérent avec elle. Les seuls
éléments « techniques » sans grand intérêt à tracer individuellement
sont les fichiers de cache (`.bin`, `.json`), déjà expliqués en §3.

---

## Pour reprendre ce projet dans six mois

**Les cinq fichiers à lire en premier, dans l'ordre :**

1. `01-discovery/ARBORESCENCE.md` — ce document : la carte.
2. `01-discovery/concurrents/sources/COUVERTURE.md` — l'état détaillé et
   certifié de la collecte, concurrent par concurrent.
3. `docs/decisions/0005-axes-de-recherche.md` — où en est la réflexion,
   et ce qui reste à trancher.
4. `01-discovery/concurrents/analysis/REGISTRE-CP.md` — les 18 problèmes
   connus du schéma d'extraction, non résolus.
5. `tools/collecte/sources.yaml` — la liste exacte des dix concurrents
   et de leurs adresses, avec les particularités de chacun.

**Ce qui n'a pas de raison d'être claire dans cette arborescence :**
- Pourquoi seuls trois concurrents sur dix ont un dossier
  `extracted/` alors que dix ont un dossier `sources/` — la réponse
  est en §4 et §7, mais rien dans les noms de dossiers ne le signale.
- Pourquoi `openfire` a deux documentations séparées
  (`utiliser-openfire/` et `documentation_2/`) alors qu'aucun autre
  concurrent n'a cette structure — la réponse est en §2 et §7, mais un
  lecteur pressé pourrait croire à une erreur de rangement.
- Pourquoi un dossier `tolteck/centre_aide/` existe alors qu'il n'y a
  jamais eu de collecte tolteck avant le 06/09 — c'est un dossier vide
  sans contenu, expliqué en §7, mais sa seule présence peut laisser
  penser qu'une collecte a eu lieu puis disparu.
