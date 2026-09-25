# 19 — Slice Handoff Template

Modèle exact pour fabriquer chaque `SLICE PACKET`. Utilisable **sans
dépendance à une fonctionnalité propriétaire Antigravity** — par Google
Antigravity, par Claude Code, ou par un développeur humain qui reprend le
projet à froid.

## 0. Où vit un packet de tranche

```
docs/slices/<SLICE_ID>/
  README.md              ← ce template rempli, la vue d'ensemble
  CONTEXT.md              ← section CONTEXT + USER JOB + PRODUCT VALUE
  DECISIONS.md             ← SUPORDO DECISIONS + ARCHITECTURE DECISIONS + OPEN QUESTIONS
  ARCHITECTURE.md           ← FRONTEND/BACKEND/SUPABASE/RLS/STORAGE/INTEGRATIONS/AI/STATES
  ACCEPTANCE.md              ← ACCEPTANCE TESTS
  NEGATIVE-TESTS.md           ← NEGATIVE TESTS
  TEST-RESULTS.md               ← résultats d'exécution réels, pas les fichiers de test seuls
  RLS-EVIDENCE.md                ← dump des policies effectives, pas l'intention déclarée
  CAPABILITY-STATUS.md            ← REAL / PROTOTYPE / MOCK / NOT_IMPLEMENTED par capacité
  KNOWN-LIMITATIONS.md             ← dette acceptée, datée
  NEXT-SLICE.md                     ← prochaine tranche prévue et ses prérequis
  SOURCE.md                          ← métadonnées de traçabilité (§2)
```

Les migrations restent dans le dossier migrations normal du projet
applicatif, **référencées** depuis `ARCHITECTURE.md`, jamais dupliquées ici.
Aucun Walkthrough propriétaire Antigravity ne peut être l'unique preuve
(`15` I) — tout ce qui est requis ci-dessous doit exister dans ce dossier,
en Markdown versionné.

## 1. Règle d'ouverture

`# OPEN QUESTIONS` doit être **vide** pour toute question qui bloque
**cette** tranche précise avant `IMPLEMENT`. Une question `OPEN` non bloquante
pour cette tranche (ex. Q18 pour une tranche qui ne touche pas Chantier/
Intervention) peut rester listée pour mémoire, explicitement marquée
`NON-BLOQUANTE POUR CETTE TRANCHE`.

## 2. `SOURCE.md` — contenu minimal obligatoire

```
SLICE_ID: <identifiant unique, ex. T0, T-AVOIR, T-PACK-CLIM>
SOURCE_BLUEPRINT_COMMIT: <hash du commit de docs/product-blueprint-antigravity/ ayant cadré cette tranche>
CANONICAL_INDEX_VERSION: <version ou hash de 16-CANONICAL-EXECUTION-INDEX.md>
CREATED_AT: <date de création du packet>
START_COMMIT: <hash du commit supordo-app au démarrage de la tranche>
END_COMMIT: <hash du commit supordo-app à la fin — rempli après réalisation>
```

Sans ce fichier, personne ne peut savoir **sur quelle version** du blueprint
une tranche a été construite — c'est l'aggravant n°1 identifié par `15` I
(le blueprint vit dans un autre dépôt que le code).

## 3. Le template

```markdown
# META

SLICE_ID:
SOURCE_BLUEPRINT_COMMIT:
CANONICAL_INDEX_VERSION:

# CONTEXT

<Une ou deux phrases : où cette tranche se situe dans 17-BUILD-GATES-AND-
SLICE-CONTRACT.md, quel(s) objet(s) du domaine elle touche.>

# USER JOB

<Ce que l'utilisateur peut faire à la fin de cette tranche, qu'il ne pouvait
pas faire avant.>

# PRODUCT VALUE

<Pourquoi cette capacité compte, en une phrase — pas un pitch.>

# IN SCOPE

<Liste fermée. Rien d'implicite.>

# OUT OF SCOPE

<Liste fermée. Explique où va chaque élément écarté (autre tranche, V2,
DO_NOT_BUILD_YET) — jamais un simple silence.>

# CANONICAL OBJECTS

<Objets du domaine touchés, avec leur classification DOMAIN_CORE /
PLATFORM_CAPABILITY / CORE_EXTENSIBLE / VERTICAL_* (12 §0.2, 16 §8).>

# SUPORDO DECISIONS

<Uniquement celles listées 16 §8 comme SUPORDO_DECISION, citées par leur
identifiant (S1-S5, L4). Ne jamais en inventer une nouvelle ici.>

# ARCHITECTURE DECISIONS

<Uniquement celles listées 16 §8 comme ARCHITECTURE_DECISION, ou une nouvelle
si elle est strictement dérivée d'un invariant déjà acté — jamais une
préférence d'implémentation non justifiée.>

# OPEN QUESTIONS

<Doit être VIDE pour toute question BLOQUANTE pour cette tranche (règle §1).
Source unique : 16 §6 (registre Q1-Q19). Ne jamais trancher ici une question
encore OPEN dans 16 — remonter au PO à la place.>

# FRONTEND CONTRACT

<Si cette tranche comporte une composante UI : conformité obligatoire à
`20-APPLICATION-UX-ARCHITECTURE-CONTRACT.md`. Pour chaque écran métier
nouveau ou modifié par cette tranche, renseigner au minimum (20 §7) :

```
USER_GOAL / ENTRY_CONTEXT / PRIMARY_INFORMATION / PRIMARY_ACTION /
SECONDARY_ACTIONS / CONTEXT_TO_PRESERVE / NEXT_SUPPORTED_ACTION /
EMPTY_STATE / LOADING_STATE / ERROR_STATE / SUCCESS_FEEDBACK
```

Ne pas recopier `20` ici — uniquement les valeurs propres à cette tranche.
Si aucune composante UI : écrire "Aucune UI dans cette tranche.">

# BACKEND CONTRACT

# SUPABASE / DATA

<Conceptuel — pas de SQL. Renvoie à 08-BACKEND-AND-NONFUNCTIONAL-CONTRACT.md
et 17 pour les contraintes applicables.>

# RLS

<Rappel obligatoire (16 §5.3, GO-03) : toute nouvelle table tenant-private
active RLS + policies dans la même migration, avec au moins un test cross-
tenant READ et un test cross-tenant WRITE listés ci-dessous en ACCEPTANCE/
NEGATIVE TESTS.>

# STORAGE

<Si des fichiers tenant-private sont créés : test d'isolation Storage séparé
obligatoire (16 §5.3).>

# INTEGRATIONS

<Aucune intégration e-invoicing ici — voir règle §5 ci-dessous.>

# AI

<Si applicable : préciser la couche exacte selon la décomposition de 17 §2
T8 (AUDIO CAPTURE / TRANSCRIPTION / VOICE NOTE / STRUCTURED EXTRACTION /
TRADE CLASSIFICATION / CATALOG MATCHING / QUOTE-LINE GENERATION / OCR /
VISION / AUTOMATIC DECISION) — ne jamais traiter "IA" comme un bloc unique.
AUTOMATIC DECISION reste interdite structurellement (0007 S4).>

# STATES / TRANSITIONS

<Graphe explicite des transitions autorisées pour tout objet à cycle de vie
touché par cette tranche — jamais un simple "ne régresse jamais".>

# ERROR / RECOVERY

# ACCEPTANCE TESTS

# NEGATIVE TESTS

<Catégories pertinentes parmi celles de 13-ACCEPTANCE-NEGATIVE-TEST-MATRIX.md
— HAPPY PATH ne suffit jamais seul.>

# MIGRATIONS

<Liste des migrations créées, avec leur emplacement réel dans le dépôt
applicatif — jamais dupliquées ici, seulement référencées.>

# EVIDENCE REQUIRED

<Ce qui doit être produit et conservé — résultats de tests exécutés, dump RLS
effectif, captures — jamais une déclaration d'intention seule.>

# BROWSER / HUMAN TEST

<Capture/enregistrement Browser Subagent pour tout impact UI (18 §2 BROWSER).
Test humain réel décrit — qui, quoi, quel résultat attendu.>

# REAL / PROTOTYPE / MOCK / NOT_IMPLEMENTED

<Une ligne par capacité livrée. Jamais REAL sans test exécuté et vérifié
(règle du PO, mission précédente §16). À recopier dans CAPABILITY-STATUS.md.>

# RECOVERABILITY ARTIFACTS

<Confirmation que TEST-RESULTS.md, RLS-EVIDENCE.md, CAPABILITY-STATUS.md et
SOURCE.md (END_COMMIT rempli) existent dans le dossier de cette tranche avant
de la considérer close.>

# STOP CONDITIONS

<Dans quelles circonstances cette tranche doit s'arrêter et attendre une
décision humaine — au minimum : toute question OPEN bloquante découverte en
cours de route, tout PRE-FLIGHT 18 en FAIL, tout doute sur REAL vs PROTOTYPE.>

# NEXT SLICE

<Tranche suivante prévue selon 17, et ses prérequis exacts — permet une
reprise à froid sans relire toute la séquence.>
```

## 4. Règle transversale — e-invoicing

Aucune tranche issue de ce template ne construit de facturation électronique
réelle. Si une tranche touche Facture et qu'une question e-invoicing se pose,
la section `# INTEGRATIONS` porte uniquement :

> **E-INVOICING SPECIALIZED CONTRACT REQUIRED BEFORE INVOICE/E-INVOICING
> IMPLEMENTATION**

— voir `16` §9. `docs/integration-blueprints/e-invoicing-accounting/` n'est
jamais copié dans un packet de tranche.

## 5. Ce que ce template ne fait pas

Ne remplit aucune tranche réelle — c'est un moule, pas un exemple. Ne
présuppose aucune fonctionnalité Antigravity propriétaire dans sa
compréhension : un développeur humain sans accès à Antigravity peut le lire
et le remplir intégralement.
