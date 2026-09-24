# 17 — Build Gates & Slice Contract

Corrige et supersède `12-ANTIGRAVITY-BUILD-SEQUENCE.md` comme graphe
d'exécution — `12` reste consultable pour le détail narratif et les preuves,
mais **ce document fait foi** en cas d'écart (`16` §2). Chaque tranche
ci-dessous reprend `12` et `13` par référence compacte, corrigée où `15`
l'exige.

## 0. GLOBAL_BUILD_GATE

Conditions nécessaires **avant le tout premier `IMPLEMENT` Antigravity**,
quelle que soit la tranche choisie. Un problème Facture ne bloque jamais
Auth/Tenant — voir la matrice §1, colonne `APPLIES_TO`.

| # | Condition | Statut |
|---|---|---|
| G1 | Couche canonique `16`-`19` disponible | **SATISFAIT** par cette mission (sous réserve du commit, voir G9) |
| G2 | RLS : invariant global — la règle (`16` §5.3) est canonique et imposée structurellement par le template de tranche (`19`, section RLS + `RLS-EVIDENCE.md` obligatoire) | **SATISFAIT** au niveau global — la règle existe et le template l'impose. **Distinct de la vérification SLICE** (§0ter ci-dessous) : chaque tranche doit ensuite *prouver* sa propre conformité, ce qui ne bloque pas le démarrage du build, seulement la clôture de chaque tranche |
| G3 | Permissions Antigravity vérifiées empiriquement sur la machine Windows réelle | **NON SATISFAIT** — PRE-FLIGHT `18` |
| G4 | Hook `PreToolUse` trivial exécuté avec succès sur la machine réelle | **NON SATISFAIT** — PRE-FLIGHT `18` |
| G5 | Sandbox activé et vérifié, ou secrets réels hors périmètre de lecture du Project | **NON SATISFAIT** — PRE-FLIGHT `18` |
| G6 | Distinction ENFORCÉ/CONSULTATIF appliquée à chaque mécanisme Antigravity | **SATISFAIT** par `18` |
| G7 | Format de dossier de tranche (`docs/slices/<SLICE_ID>/`) et règle de copie du blueprint définis | **SATISFAIT** par `19` |
| G8 | Position de gouvernance des données minimale : DEV = données synthétiques uniquement, aucun secret réel inutile dans le Project, aucun service-role Supabase exposé au frontend | **SATISFAIT** (règle posée ici, §0bis) — gouvernance avancée reste `OPEN` |
| G9 | Dossier `docs/product-blueprint-antigravity/` committé, `01-discovery/ARBORESCENCE.md` à jour, carte du `README` couvrant `01`-`19` | **NON SATISFAIT** — cette mission s'arrête avant tout commit (STOP explicite) |
| G10 | `supordo-app` existe comme dépôt séparé de `supordo-os` | **NON SATISFAIT** — n'existe pas encore |
| G11 | Stratégie Git : New Worktree Mode validé, ou stratégie alternative documentée | Règle posée (`14` §2, reprise `18`), vérification empirique manquante — PRE-FLIGHT `18` |

### 0bis. Règle de gouvernance des données (G8, détail)

Avant tout accès MCP à une base contenant des données réelles : aucune donnée
réelle de pilote n'est accessible à Antigravity en environnement DEV. **DEV =
données synthétiques uniquement.** Aucun secret réel inutile dans le
périmètre de lecture du Project. Aucune clé service-role Supabase exposée au
frontend. Cette règle minimale est `GLOBAL_BUILD_GATE` ; une gouvernance plus
avancée (télémétrie, Enterprise Antigravity) reste `OPEN`, non bloquante pour
démarrer.

### 0ter. RLS — GLOBAL invariant vs SLICE verification (ne pas confondre)

Deux choses distinctes, à ne jamais fusionner en un seul gate impossible à
satisfaire avant le build :

- **GLOBAL invariant (G2, GO-03)** : *toute nouvelle table tenant-private doit
  avoir RLS + policies dans la même migration, et des tests cross-tenant
  READ/WRITE.* Ce gate global est **satisfait dès que la règle est
  canonique et imposée par le template de tranche** (`19`, section RLS +
  fichier `RLS-EVIDENCE.md` obligatoire dans `docs/slices/<SLICE_ID>/`) —
  c'est le cas dès cette mission. Il **ne bloque donc pas** le démarrage du
  premier `IMPLEMENT`.
- **SLICE verification** : chaque tranche doit ensuite **prouver**,
  concrètement, que les tables qu'elle crée respectent effectivement la
  règle — c'est une condition de *clôture* de cette tranche précise
  (`RLS-EVIDENCE.md` rempli avec le dump des policies effectives, pas
  l'intention déclarée), pas une condition de démarrage du build dans son
  ensemble.

Un `GLOBAL_BUILD_GATE` ne peut jamais consister en « chaque tranche future
doit déjà être prouvée » — ce serait impossible à satisfaire avant même
d'avoir commencé. Le gate global porte sur l'existence et l'imposition de la
règle ; la preuve elle-même est un critère `SLICE_GATE`, tranche par tranche.

## 1. Matrice GO reclassifiée (`15` K, GO-01→GO-17)

Classification : `GLOBAL_BUILD_GATE` (bloque tout premier IMPLEMENT) ·
`SLICE_GATE` (bloque certaines tranches seulement) · `STRUCTURAL_OBJECT_GATE`
(bloque la première migration créant l'objet concerné) · `FIELD_GATE` (ne se
ferme qu'après test terrain) · `NON_BLOCKING_IMPROVEMENT`.

| GO_ID | Classification | Applies to | Why | Source | Binary condition | Current status |
|---|---|---|---|---|---|---|
| GO-01 | `GLOBAL_BUILD_GATE` | Toute tranche | Sans index canonique, un agent lit `00`-`15` dans le désordre et applique des conclusions périmées | `15` J, K | Index existe et fusionne Q1-Q19 / n'existe pas | **SATISFAIT** — `16` (sous réserve G9) |
| GO-02 | `STRUCTURAL_OBJECT_GATE` (Lieu) | Première migration créant Client | S1 opposable, effet domino n°1, coût de report déjà croissant | `15` B1, `03` §4, `0007` S1 | Posé et testé / non | Corrigé dans `17` §2 T1 (ci-dessous) ; test à exécuter à l'implémentation |
| GO-03 | `GLOBAL_BUILD_GATE` (règle) + `SLICE_GATE` (preuve par tranche, voir §0ter) | Toute table tenant-private, toute tranche | RLS "héritée" est techniquement faux ; la règle s'applique à chaque migration, mais sa *preuve* est un critère de clôture par tranche, pas de démarrage global | `15` B2 | Règle explicite existe et est imposée par le template / non | **SATISFAIT au niveau global** (règle posée `16` §5.3, imposée par `19`) — la preuve par tranche reste à produire à chaque clôture, voir §0ter |
| GO-04 | `STRUCTURAL_OBJECT_GATE` (Catalogue) | Première migration Catalogue (`T-PACK`) | Frontière privé/partagé non tranchée, risque de fuite commerciale tenant | `15` B3 | Tranchée / non | `ARCHITECTURE_CANDIDATE` posée `16` §5.2, non arbitrée — bloque `T-PACK`, pas `T0`/`T1` |
| GO-05 | `SLICE_GATE` (T3) | `T3` uniquement | Portail client = route d'accès non/faiblement authentifiée, surface de fuite la plus probable | `15` B4 | Exclu ou défini+testé / ni l'un ni l'autre | Toujours **NON SATISFAIT** — voir `17` §2 T3 |
| GO-06 | `STRUCTURAL_OBJECT_GATE` (Catalogue/Devis) | `T1`/`T4` | S3 non testé = perte de données irréversible invisible à la livraison | `15` B8 | Test existe / non | **NON SATISFAIT** — ajouté aux critères d'acceptation `T1`/`T4` ci-dessous |
| GO-07 | `STRUCTURAL_OBJECT_GATE` (Facture) | `T4` | Contrainte légale la mieux identifiée après L1, non testée sur son objet réel | `15` B9 | Fait / non | **NON SATISFAIT** — ajouté aux critères `T4` |
| GO-08 | `GLOBAL_BUILD_GATE` | Toute tranche | Sécurité critique du projet repose sur un mécanisme non confirmé sur la plateforme réelle | `15` H3 | Vérifié sur la machine / non | **NON SATISFAIT** — PRE-FLIGHT `18` |
| GO-09 | `GLOBAL_BUILD_GATE` | Toute tranche | Seul levier programmatique réel non vérifié en sémantique Windows | `15` H10 | Exécuté et constaté / non | **NON SATISFAIT** — PRE-FLIGHT `18` |
| GO-10 | `GLOBAL_BUILD_GATE` | Toute tranche | Protection secrets invoquée par `14` repose sur un sandbox éteint par défaut | `15` H6 | Fait / non | **NON SATISFAIT** — PRE-FLIGHT `18` |
| GO-11 | `GLOBAL_BUILD_GATE` | Toute tranche | Rules/Skills présentées à tort comme des barrières | `15` B7 | Distinction faite / non | **SATISFAIT** — `18` |
| GO-12 | `SLICE_GATE` | La tranche retenue en premier | Aucune tranche ne s'ouvre avec une question `BLOCKS_*` non tranchée | `16` §6 | Tranchées / non | **NON SATISFAIT** — dépend du PO, minimum Q1 |
| GO-13 | `NON_BLOCKING_IMPROVEMENT` | Documentation | Trois capacités disparues sans trace | `15` C1/C2 | Explicite pour les trois / non | **SATISFAIT** — `16` §7 (Avoir=V1, Planning=V1, transcription libre=`OPEN` explicite) |
| GO-14 | `SLICE_GATE` | Choix de première tranche | Un candidat ne peut omettre un prérequis qu'il déclare lui-même | `15` C3, G | Cohérent / non | **SATISFAIT** — candidats corrigés §3 ci-dessous |
| GO-15 | `GLOBAL_BUILD_GATE` | Toute tranche | Condition de reprise sans Antigravity | `15` I | Défini / non | **SATISFAIT** — `19` |
| GO-16 | `GLOBAL_BUILD_GATE` | Tout accès MCP à une base réelle | Conditions officielles autorisent la revue humaine du contenu transmis à Google | `15` C11 | Prise / non | **SATISFAIT au niveau minimal** — `17` §0bis |
| GO-17 | `GLOBAL_BUILD_GATE` | Tout | Corpus non committé = état durable inexistant | `15` C13 | Fait / non | **NON SATISFAIT** — commit en attente de validation humaine (hors périmètre de cette mission) |

**Aucun GO Facture (GO-04, 05, 06, 07) ne bloque `T0`/`T1`/`T-PLANNING`** —
conformément à l'objectif de la mission.

## 2. Tranches

Ordre de dépendance corrigé : `T0 → T-PLANNING, T1 → T-PACK → T2 → T3 → T4 →
T-AVOIR → T5 → T6` et `T8` (peut démarrer après `T1`, contenu réel dépend de
`T-PACK`). `T-PLANNING` et `T-AVOIR` sont **nouvelles** (`16` §7, GO-13).

### T0 — Fondations plateforme (Auth/Tenant/Membership/migrations/RLS/app shell)

Reprend `12` T0, **corrigé pour retirer Lieu** — T0 ne crée pas Client, donc
Lieu n'y a pas sa place (voir doctrine `16` §5.1, corrigée : Lieu devient
first-class dans la **première tranche qui crée Client**, pas dans T0 lui-même
— dans la séquence actuelle, c'est `T1` ci-dessous).

- **PURPOSE** : fondation technique pure — authentification, tenant,
  appartenance (membership) de base, discipline de migration, RLS, coquille
  applicative. Aucun objet métier.
- **DOMAIN OBJECTS** : Tenant (`PLATFORM_CAPABILITY`), Utilisateur
  (`DOMAIN_CORE`, modèle simple). **Lieu n'est pas créé dans cette tranche.**
- **STRUCTURAL GATES** : GO-03 (RLS), GO-08/09/10 (PRE-FLIGHT `18`). **GO-02
  (Lieu) ne s'applique pas à T0** — il s'applique à `T1`, voir ci-dessous.
- **RLS** : voir GLOBAL_BUILD_GATE G2/GO-03 — la table factice de `12` T0 ne
  suffit plus seule comme preuve ; au moins une table du domaine réel de
  cette tranche (Tenant ou Utilisateur) doit être testée en isolation
  cross-tenant avant DoD.
- **EVIDENCE** : test automatisé d'isolation cross-tenant exécuté directement
  contre l'API/la base (pas l'UI) ; dump de la politique RLS effective.
- **RECOVERABILITY** : premier dossier `docs/slices/T0/` créé selon `19`.
- Le reste (BACKEND, FRONTEND, ACCEPTANCE, tests négatifs) inchangé — voir
  `12` T0 et `13` §T0.

### T-PLANNING — Planning/RDV simple (nouvelle, `16` §7)

- **PURPOSE** : agenda minimal, universel (10/10 LIGHT), débloque les
  parcours A et D (`04`).
- **USER JOB** : voir un RDV/intervention du jour, en planifier un nouveau.
- **DEPENDENCIES** : `T0`.
- **BLOCKING DECISIONS** : aucune.
- **STRUCTURAL GATES** : GO-03 (RLS sur la nouvelle table RDV).
- **IN SCOPE** : création/consultation d'un RDV simple, lié à Client et
  éventuellement Lieu.
- **OUT OF SCOPE** : synchronisation calendrier externe (`06` de l'annexe
  intégrations — hors périmètre ici), planification multi-intervenants.
- **DOMAIN OBJECTS** : RDV (`DOMAIN_CORE`, nouveau).
- **RLS** : isolation tenant standard, test cross-tenant R/W (GO-03).
- **ACCEPTANCE/NEGATIVE TESTS** : à construire sur le modèle `13` — aucune
  matrice existante à ce jour, gap signalé, non bloquant pour ouvrir la
  tranche.
- **OPEN NEXT** : synchronisation calendrier externe (V2/V3).

### T1 — Création rapide d'un devis

Reprend `12` T1, avec deux corrections :

- **DOMAIN OBJECTS** : Devis, Client, Catalogue (stub), **et Lieu — première
  tranche qui crée Client, donc première tranche où Lieu devient first-class**
  (`16` §5.1, GO-02, corrigé). Lieu possède sa propre identité, distincte du
  Client ; l'historique opérationnel peut s'y rattacher ; le rattachement
  Devis↔Lieu est optionnel à la création (cohérent S2) mais le champ et
  l'objet Lieu lui-même doivent exister dès cette tranche. **La cardinalité
  exacte Client↔Lieu reste `OPEN`** (`STRUCTURAL_BEFORE_SCHEMA`, non arbitrée
  ici) — ne pas l'inventer au moment de coder : représenter Lieu comme objet
  séparé suffit à satisfaire GO-02, la cardinalité elle-même attend le PO.
- **STRUCTURAL GATES** : **GO-02** (Lieu first-class, corrigé — s'applique
  ici, pas à T0) et **GO-06** (test S3, voir ACCEPTANCE ci-dessous) — tous
  deux nouveaux par rapport à `12`.
- **ACCEPTANCE (ajout)** : test S3 — créer une ligne à prix P, modifier le
  prix catalogue à P', recharger le devis, la ligne vaut toujours P (`15` B8,
  correction minimale exacte du gate).
- Le reste inchangé — voir `12` T1, `13` §T1.

### T-PACK — Contenu du pack métier (verticale à décider, Q7)

Reprend `12` T-PACK-CLIM, renommé génériquement `T-PACK` ici tant que Q7 n'est
pas tranchée (`16` §6 — ne pas présumer climatisation/PAC comme acquis, voir
`09`/`07` §0 pour la recommandation analytique, non une décision).

- **STRUCTURAL GATES (ajout)** : **GO-04 — la frontière `referentiel_produit`/
  `article_catalogue` (`ARCHITECTURE_CANDIDATE`, `16` §5.2) doit être arbitrée
  avant cette migration**, sans quoi le risque de fuite commerciale tenant
  identifié par `15` B3 reste ouvert.
- **BLOCKING DECISIONS** : Q7 (verticale), Q9 (conformité déclarative), **et
  désormais l'arbitrage GO-04**.
- Le reste inchangé — voir `12` T-PACK-CLIM, `13` §T-PACK-CLIM.

### T2 — Finalisation et envoi

Inchangé — voir `12` T2, `13` §T2. `RLS/PERMISSIONS` : appliquer GO-03
explicitement (`12` disait « inchangé » — lire cette mention comme « aucune
nouvelle table, donc aucune nouvelle policy à écrire », jamais comme « RLS
héritée sans vérification »).

### T3 — Engagement du client

Inchangé — voir `12` T3, `13` §T3, à l'exception de :

- **STRUCTURAL GATES (ajout)** : **GO-05 — portail client**. Si un portail
  client existe même minimal dans cette tranche, il doit être **explicitement
  exclu du V1** (acceptation manuelle côté artisan), **ou** construit comme
  sous-tranche nommée avec ses propres tests (jeton opaque à forte entropie,
  expiration, révocation, scope à un seul devis, deux tests négatifs : jeton
  d'un autre devis, jeton d'un autre tenant). `12` T3 laissait cette capacité
  en option implicite (« portail client minimal ou action manuelle ») — **ce
  flou est refermé ici** : le choix doit être fait avant `IMPLEMENT`, pas
  découvert pendant.

### T4 — Devis → Facture directe

Reprend `12` T4, avec un ajout :

- **STRUCTURAL GATES (ajout)** : **GO-07** — test de numérotation Facture
  sous concurrence (émission simultanée, absence de trou et de doublon),
  garanti au niveau séquence base (pas un `MAX()+1` applicatif). **Le statut
  séquentiel du numéro de Devis, s'il existe, doit être documenté comme un
  choix produit assumé, jamais comme une conséquence de L3** (L3 concerne la
  Facture uniquement — `15` B9, mission §12).
- **BLOCKING DECISIONS (ajout)** : **T4 ne peut pas être considérée
  "complète" pour un usage réel tant que `T-AVOIR` (ci-dessous) n'existe pas**
  — une facture émise sans mécanisme de correction est le risque le plus
  sévère identifié par `15` (C1).
- Le reste inchangé — voir `12` T4, `13` §T4.

### T-AVOIR — Correction d'une facture (nouvelle, `16` §7)

- **PURPOSE** : seul mécanisme de correction d'une facture numérotée (L1/L2,
  `0007`), sans lequel `T4` livre un système sans recours.
- **USER JOB** : corriger une facture erronée sans jamais la réécrire.
- **DEPENDENCIES** : `T4`.
- **BLOCKING DECISIONS** : aucune nouvelle — L1/L2 déjà `LEGAL_CITÉ`.
- **STRUCTURAL GATES** : Avoir hérite du régime d'immuabilité de la Facture
  dès sa propre numérotation (L2) — même exigence de test que GO-07,
  appliquée à l'Avoir.
- **IN SCOPE** : avoir total (inverse tous les montants) au minimum ; lien
  bidirectionnel direct Facture↔Avoir (FK, pas un lookup indirect — `03` note
  qu'un angle mort existe chez un concurrent sur ce point précis, à ne pas
  reproduire).
- **OUT OF SCOPE** : avoir partiel (V2, si non justifié dès V1).
- **DOMAIN OBJECTS** : Avoir (`DOMAIN_CORE`).
- **BACKEND** : immuabilité posée au niveau base dès numérotation, comme la
  Facture.
- **RLS** : GO-03 standard.
- **ACCEPTANCE** : une facture numérotée peut être corrigée par un avoir qui
  copie son contenu ; l'avoir devient lui-même inaltérable dès sa propre
  numérotation.
- **NEGATIVE TESTS** : tentative de modifier directement la facture source
  après création de l'avoir → refus ; tentative de modifier l'avoir après sa
  numérotation → refus.
- **EVIDENCE** : test automatisé des deux refus ci-dessus, exécuté par un
  chemin d'accès direct à la base, pas seulement l'API applicative.
- **OPEN NEXT** : avoir partiel, si un besoin réel émerge en V2.

### T5 — Acompte puis solde

Inchangé — voir `12` T5, `13` §T5.

### T6 — Devis → Chantier

Inchangé — **scope strictement Chantier, jamais Intervention** (`16` §4 ligne
5, Q18 toujours `OPEN`) — voir `12` T6, `13` §T6. Aucune tranche « Intervention »
n'est conçue ici ; elle reste bloquée par Q18, Q8, Q14.

### T8 — Visite/relevé, décomposé en couches (mission §9)

`12` T8 et `13` §T8 restent valables pour le **niveau 1** (relevé structuré
minimal), mais la mission corrective exige de séparer explicitement ce qui
était amalgamé sous « IA » :

| Couche | Contenu | Version | Gate |
|---|---|---|---|
| **AUDIO CAPTURE** | Enregistrement audio brut sur mobile | `T8` niveau 1 possible dès V1 si retenu | Indépendant des couches suivantes |
| **TRANSCRIPTION** | Audio → texte, sans structuration | `OPEN` — voir `16` §7 (transcription vocale libre) | Testable indépendamment de tout le reste |
| **VOICE NOTE** | Note vocale attachée à un objet, jamais interprétée | Compatible V1 si `TRANSCRIPTION` retenue | — |
| **STRUCTURED EXTRACTION** | Texte → champs typés du relevé | `T8-VOIX`, V2 | `12` §0.4 niveau 4 |
| **TRADE CLASSIFICATION** | Rattachement à une catégorie métier du pack | `T8-VOIX`, V2 | Dépend de `T-PACK` stable |
| **CATALOG MATCHING** | Rattachement à un article du catalogue | `T8-VOIX`, V2 | Dépend de `T-PACK` stable |
| **QUOTE-LINE GENERATION** | Génération de lignes de devis | `T8-VOIX`, V2, validation humaine systématique | `13` §T8-VOIX |
| **OCR** | Lecture de plaque signalétique/document | V2 | `12` §0.4 niveau 3 |
| **VISION** | Analyse d'image (anomalie, état visuel) | `EXPERIMENTAL`, jamais sans cadrage juridique/assurantiel (`05` #3) | Aucune décision automatique |
| **AUTOMATIC DECISION** | Toute décision prise sans validation humaine | **Interdite structurellement** sur l'ensemble des couches ci-dessus | `0007` S4, `13` HUMAN VALIDATION |

**Ce document ne tranche pas** l'inclusion de `TRANSCRIPTION`/`AUDIO CAPTURE`
seules en V1 — c'est l'objet du gate `16` §7. Si le PO les inclut, elles
forment une sous-tranche `T8-VOICE-SIMPLE`, dépendances `T1`, indépendante de
`T-PACK` et de `T8-VOIX`. `T8-VOIX` (structuration complète) reste V2,
inchangée par rapport à `12`.

## 3. Candidats pour la première tranche réelle — corrigés (GO-14)

**Ne choisit toujours pas à la place du PO.** Le candidat 2 de `12` §4 était
invalide (`15` C3 : omettait `T1`, prérequis déclaré des deux tranches
incluses). Corrigé ici :

### Candidat 1 — `T0 + T1`
Inchangé, voir `12` §4. Décision bloquante : Q1.

### Candidat 2 — `T0 + T1 + T-PACK + T8` (corrigé — inclut désormais T1)
Fusion de l'ancien candidat 2 invalide et du chemin qui le complète
réellement. Décisions bloquantes réelles : **Q1, Q7, Q9** (pas seulement Q7/
Q9 comme l'affirmait `12`) — l'erreur de `15` C3 est corrigée ici, pas
répétée.

### Candidat 3 — `T0 + T1 + T-PACK`
Inchangé, voir `12` §4. Décisions bloquantes : Q1, Q7, Q9.

**Observation transversale reprise de `15` G** : aucun des trois candidats ne
ferme un cycle testable par un artisan en conditions réelles (un devis qu'on
ne peut ni envoyer ni facturer). La première tranche réellement testable
terrain est `T2`. C'est un fait de séquence, pas un argument pour l'un des
candidats.

## 4. Ce que ce document ne fait pas

Ne choisit aucune verticale (Q7). Ne construit aucune tranche Intervention
(Q18 ouverte). N'arbitre pas la frontière catalogue (GO-04). Ne construit
aucune migration, aucun code. `docs/integration-blueprints/e-invoicing-
accounting/` reste hors périmètre — voir `16` §9.
