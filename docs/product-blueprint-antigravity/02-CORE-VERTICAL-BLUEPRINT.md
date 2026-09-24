# 02 — Core / Vertical Blueprint

Frontière CORE / CORE_EXTENSIBLE / VERTICAL, stress-testée sur les deux verticales
désignées par le PO : fumisterie/poêles/cheminées et climatisation/PAC/chauffage.

**Direction PO (rappel, pas un constat du corpus)** : SUPORDO = CORE commun + PACKS
MÉTIERS. Objectif de ce document : trouver la ligne, pas la deviner.

## Statuts de classement (mission §7)

`CORE` · `CORE_EXTENSIBLE` · `VERTICAL_DATA` · `VERTICAL_WORKFLOW` · `VERTICAL_RULE` ·
`VERTICAL_CAPTURE` · `VERTICAL_REGULATORY` · `UNKNOWN`

## 1. Ce que le corpus donne à voir sur ce sujet précis, et ses limites

Le corpus concurrentiel **n'a jamais été construit pour tester une architecture
CORE+PACKS** — c'est une direction produit du PO (§2 de la mission), pas une
conclusion du corpus. Deux faits du corpus sont cependant directement utilisables :

1. **ProGBat vend des bibliothèques de prix par corps de métier en add-on payant**
   (BatiChiffrage) sur un cœur BTP généraliste — `ACQUIS DOCUMENTAIRE`, c'est le seul
   précédent marché direct d'un modèle proche de CORE+PACKS.
2. **OpenFire est le seul concurrent avec une spécialisation produit réelle et
   documentée sur les deux verticales de stress-test du PO** — fumisterie/poêles-
   cheminées ET climatisation/froid — avec un module réglementaire nommé (`ACQUIS
   DOCUMENTAIRE` côté centre d'aide pour le froid ; `MARKETING_ONLY` pour l'étendue
   exacte du module fumisterie, dont l'existence marketing est confirmée mais la
   profondeur fonctionnelle non auditée). InterFast documente la même spécialisation
   froid/climatisation, avec la même profondeur réglementaire.

Tout le reste de ce document est une **analyse structurelle**, pas un rapport de
lecture — c'est le travail que le corpus, à lui seul, ne peut pas faire.

## 2. Classement des grandes capacités

| Capacité | Classement | Justification |
|---|---|---|
| Client / contact | `CORE` | même concept et comportement partout, aucun signal de variation métier |
| **Lieu** | `CORE` | S1 (`SUPORDO_DECISION`) : le lieu est un concept générique, distinct du client. Structurellement identique quel que soit le métier — c'est ce qu'il *porte* qui varie |
| Devis (naissance, cycle, dérivation) | `CORE` | comportement quasi identique 8/8 corpus quel que soit le secteur BTP couvert (généraliste ou spécialisé) — voir `03` |
| Facture / Avoir | `CORE` | contrainte légale universelle (L1-L3/0007), aucune variation métier documentée |
| Paiement | `CORE` | aucun signal de variation métier |
| Planning / RDV | `CORE` | universel 10/10 en LIGHT |
| Personnel / compte utilisateur | `CORE` | même modèle quel que soit le métier |
| Facturation électronique / conformité fiscale | `CORE` | réforme française universelle, ne dépend pas du métier — voir `06` |
| Sécurité / auth / multi-tenant / rôles | `CORE` | infrastructure, indépendante du métier |
| **Catalogue / Article** | `CORE_EXTENSIBLE` | le moteur (ligne, prix figé à la création — S3, snapshot) est universel ; le **contenu** (quels articles, quelles caractéristiques techniques, quelles marques) varie entièrement par métier. C'est la définition même de CORE_EXTENSIBLE. |
| **Chantier / Intervention** | `CORE_EXTENSIBLE` | le concept (objet d'exécution, agrégation de rentabilité) est commun, mais les **étapes concrètes** diffèrent par métier (une intervention fumisterie n'a pas les mêmes jalons qu'une intervention clim/PAC) |
| Stock | `CORE_EXTENSIBLE` | moteur commun, référentiel produit variable |
| Rapports / pilotage | `CORE_EXTENSIBLE` | moteur d'agrégation commun, mais forte concentration Sellsy (72 %) — signal éditeur, pas un standard à répliquer tel quel |
| CRM / pipeline commercial | `CORE_EXTENSIBLE` | transversal, non lié à un métier BTP particulier — signal restreint (3/10) mais pas vertical |
| Document / Photo (mécanisme d'attachement) | `CORE_EXTENSIBLE` | le moteur (stocker, rattacher, consentement S5) est générique ; **quoi photographier et pourquoi** est vertical (voir `VERTICAL_CAPTURE` ci-dessous) |
| Signature électronique | `CORE_EXTENSIBLE` | moteur générique, mais le **provider** doit rester interchangeable — voir `06` |
| IA générative (résumé, rédaction, suggestion) | `CORE_EXTENSIBLE` | moteur transversal (le même LLM sert tous les métiers) ; **le contexte injecté** (vocabulaire, catalogue, règles) est vertical — voir `05` |
| Transcription vocale (speech-to-text) | `CORE` | l'acte technique de transcrire de la voix en texte ne dépend d'aucun métier — c'est la **structuration** en aval qui est vertical |
| Vision / analyse de photo | `CORE_EXTENSIBLE` | moteur générique de description d'image ; **ce qu'on cherche à détecter** (anomalie sur un conduit de cheminée vs état d'un tableau électrique pour une PAC) est vertical |
| **Visite / relevé technique** | `CORE_EXTENSIBLE` | le moteur (créer une session de capture structurée, rattachée à un lieu/client, pouvant générer des lignes de devis) doit être générique — InterFast et OpenFire Zendesk le prouvent chacun à leur façon. Le **schéma exact des champs relevés** est vertical, voir ci-dessous |
| Formulaires / questions conditionnelles de relevé | `VERTICAL_CAPTURE` | dépend entièrement du métier — ce qu'on demande pour dimensionner un poêle n'a rien à voir avec ce qu'on demande pour une PAC |
| Catalogues fabricants / marques | `VERTICAL_DATA` | référentiel produit propre à chaque filière (fumisterie ≠ CVC) |
| Caractéristiques techniques produit | `VERTICAL_DATA` | schéma de caractéristiques différent par famille de produit |
| Règles de calcul / dimensionnement métier | `VERTICAL_RULE` | ex. calcul de tirage pour une cheminée, bilan thermique pour une PAC — logiques métier disjointes |
| **Équipement / actif / parc installé** | `VERTICAL_DATA` | 2/10 seulement (InterFast, OpenFire), corrélé aux métiers à obligation de suivi (froid, chauffage) — voir `03` pour le niveau de preuve exact |
| Maintenance récurrente / contrats | `VERTICAL_WORKFLOW` | 3/10, corrélé au parc installé — la logique de relance diffère par métier (ramonage annuel obligatoire vs entretien PAC périodique selon puissance) |
| Conformité réglementaire métier (Cerfa 15497, BSFF, Trackdéchets, numéro de capacité, DTU fumisterie) | `VERTICAL_REGULATORY` | c'est la capacité la mieux prouvée du corpus dans sa catégorie, mais strictement propre au froid/climatisation — aucune preuve équivalente pour fumisterie dans le corpus |
| Vocabulaire métier (glossaire technique) | `VERTICAL_DATA` | alimente le contexte IA (voir `05`) — un terme n'a pas le même sens d'un métier à l'autre |

## 3. Stress-test — fumisterie/poêles/cheminées vs climatisation/PAC/chauffage

Objectif : vérifier si l'abstraction CORE_EXTENSIBLE tient sur deux métiers réels et
distincts, pas seulement en théorie.

| Dimension | Fumisterie / poêles / cheminées | Climatisation / PAC / chauffage | L'abstraction CORE tient-elle ? |
|---|---|---|---|
| Catalogue | modèles de poêles/inserts par marque, diamètres de conduit, matériaux (inox, terre cuite), rendements | unités intérieures/extérieures par marque, puissance, SCOP/SEER, type de fluide frigorigène et charge | **Oui** — même moteur `CORE_EXTENSIBLE` (article + caractéristiques techniques typées), schémas de caractéristiques différents injectés par pack |
| Relevé terrain | hauteur/diamètre de conduit existant, matériau, tirage, distance aux matériaux combustibles, accès toiture | bilan thermique sommaire, emplacement unité extérieure, alimentation électrique disponible, isolation | **Oui** — même moteur de capture structurée (`CORE_EXTENSIBLE`), formulaire différent par pack (`VERTICAL_CAPTURE`) |
| Obligation réglementaire | ramonage obligatoire (périodicité réglementaire/assurantielle, DTU 24.1), attestation de ramonage à fournir | obligation d'entretien périodique selon puissance et charge de fluide frigorigène, Cerfa 15497, numéro de capacité de l'installateur, déclaration Trackdéchets | **Non identique, mais motif structurel commun** : les deux sont des obligations de **maintenance périodique avec preuve documentaire** — un moteur `CORE_EXTENSIBLE` "obligation récurrente + relance + document de preuve" peut servir les deux, avec la règle de fréquence et la référence légale injectées par pack (`VERTICAL_REGULATORY`) |
| Parc installé | conduit/souche de cheminée comme actif suivi dans le temps | unité de PAC/clim comme actif suivi, avec numéro de série et charge de fluide | **Oui structurellement** — même objet `VERTICAL_DATA` rattaché au `Lieu` (CORE), schéma de champs différent |
| Photo attendue | état du conduit, souche en toiture, plaque signalétique de l'appareil | plaque signalétique de l'unité, état du tableau électrique, emplacement de l'unité extérieure | **Oui** — même mécanisme d'attachement (`CORE_EXTENSIBLE`), liste de photos attendues différente (`VERTICAL_CAPTURE`) |
| Preuve documentaire disponible dans le corpus | **quasi nulle** — aucun concurrent du centre d'aide ne documente cette verticale ; signal marketing uniquement chez OpenFire | **forte** — InterFast et OpenFire documentent tous deux le module réglementaire en détail | Confirme un **déséquilibre de preuve entre les deux verticales de stress-test**, pas une différence de structure — voir §4 |

**Verdict du stress-test : l'abstraction CORE + PACKS MÉTIERS tient sur les deux
verticales testées.** Aucune des deux n'oblige à dupliquer le moteur devis, facture,
planning ou l'objet Lieu. Ce qui varie systématiquement est : le contenu du
catalogue, le schéma du relevé terrain, la règle de calcul, la référence
réglementaire précise et la liste de photos attendues — exactement les six familles
que le PO désigne comme contenu de pack (§2 de la mission).

## 4. Risques de mauvaise abstraction identifiés

| Risque | Description | Recommandation (`RECOMMANDATION ANALYTIQUE`) |
|---|---|---|
| **Sur-généraliser depuis la seule verticale bien documentée** | Le froid/climatisation est la seule verticale avec une preuve documentaire dense (InterFast + OpenFire). Le risque est de modéliser le CORE (et notamment le pack métier lui-même) en calquant implicitement la structure "fluide frigorigène + Cerfa" comme gabarit universel — ce gabarit ne survivrait pas à la fumisterie, à la plomberie ou à l'électricité. | Concevoir le schéma de pack métier de façon **assez nue** pour que "aucune obligation réglementaire" et "pas de parc installé" soient des états valides d'un pack, pas des exceptions |
| **Sous-outiller le CORE sur l'objet Chantier/Intervention** | C'est l'objet le moins bien documenté du corpus (`03`) alors que c'est un point de passage obligé de toutes les verticales testées. Le risque est de le laisser trop pauvre en V1 faute de preuve, alors qu'il porte la différenciation produit. | Ne pas attendre une preuve documentaire supplémentaire sur cet objet — accepter `À TESTER TERRAIN` et concevoir son modèle de données par les stress-tests de ce document plutôt que par lecture corpus |
| **Sur-architecturer le pack métier avant le deuxième cas d'usage** | Construire un système de pack générique et paramétrable avant d'avoir vu deux verticales réelles en fonctionnement (fumisterie ET clim) risque de produire une abstraction fausse, jamais éprouvée. | Construire le pack froid/climatisation en premier (meilleure preuve), le pack fumisterie en second **avec obligation explicite de faire évoluer le moteur de pack si la fumisterie ne rentre pas dans le moule** — ne pas figer le mécanisme de pack avant ce deuxième test |
| **Dupliquer le moteur devis/facture par métier** | Un risque classique en modélisation multi-verticale est de créer, sous la pression du besoin métier, des variantes de l'objet Devis par pack. Le corpus est clair : 8/8 concurrents traitent le devis comme un objet unique, quel que soit leur degré de spécialisation métier (y compris OpenFire et InterFast, les deux plus spécialisés). | Le devis, la facture, le paiement, le planning restent **strictement CORE** — un pack ne peut qu'ajouter du contenu (lignes, champs de relevé, catalogue, règles de calcul), jamais dupliquer l'objet |
| **Absorber le parc installé/maintenance dans le CORE parce qu'il "semble" transversal** | Le concept de "suivi d'un actif dans le temps" pourrait sembler suffisamment général pour rejoindre le CORE. Mais la preuve documentaire (`03`) montre une cascade entièrement spécifique à un seul éditeur (OpenFire Odoo, module ERP), non généralisable — l'intégrer au CORE créerait un moteur bâti sur un seul témoin. | Garder `VERTICAL_DATA`/`VERTICAL_WORKFLOW` tant qu'une deuxième verticale (au minimum) n'a pas confirmé le même besoin de suivi d'actif |
| **Construire le catalogue V1 comme une liste plate d'articles** | Si le moteur catalogue (`CORE_EXTENSIBLE`) est conçu trop simplement (nom + prix), il ne survivra pas à la complexité réelle des catalogues fumisterie/clim (marque, modèle, variantes, caractéristiques techniques typées, compatibilité). | Concevoir dès V1 un schéma de caractéristiques technique **extensible par pack**, même si le premier pack seul l'utilise pleinement |

## 5. Ce que ce document ne tranche pas

- La **liste exacte des packs à construire au-delà des deux verticales de stress-test**
  n'est pas un sujet de ce document — voir `07-V1-V2-V3-80-20.md`.
- Le **modèle de données du pack métier lui-même** (comment un pack déclare un
  catalogue, un formulaire de relevé, une règle réglementaire) n'est pas conçu ici —
  c'est un sujet d'architecture pour Antigravity, cadré par `08` et `09`, pas par ce
  document conceptuel.
- Ce classement est un **jugement d'architecture**, pas une décision SUPORDO au sens
  de `0007` — il n'engage rien tant qu'il n'a pas été validé par le PO.
