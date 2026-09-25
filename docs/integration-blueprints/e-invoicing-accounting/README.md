STATUS: REFERENCE / FUTURE BUILD CONTRACT

NOT CURRENT V1 BUILD SCOPE

DO NOT GIVE RAW EVOLIZ/AXONAUT API DOCS TO ANTIGRAVITY

---

# E-Invoicing + Accounting Interop Blueprint — SUPORDO

## Pourquoi ces documents existent

Le [Product Blueprint principal](../../product-blueprint-antigravity/) (`docs/product-blueprint-antigravity/`) définit le V1 de SUPORDO et une séquence de tranches de construction (`12-ANTIGRAVITY-BUILD-SEQUENCE.md`). Ce V1 pose déjà une **interface abstraite** vers une future plateforme de facturation électronique (tranche T4) mais **ne branche rien de réel** — c'est un choix délibéré du blueprint principal, confirmé et non remis en cause ici.

Cette annexe prépare, en amont et indépendamment du calendrier V1, le contrat de données et d'interopérabilité que la **future** tranche `DEVIS → FACTURE → FACTURATION ÉLECTRONIQUE → COMPTABILITÉ/EXPERT-COMPTABLE` devra respecter, afin qu'au moment venu, Google Antigravity (ou tout développeur humain) puisse construire cette tranche sans inventer les règles métier, réglementaires ou d'intégration, et sans devoir lire les milliers de lignes de documentation API de deux concurrents pour les redécouvrir.

## Quand utiliser ces documents

**Dès que la tranche `T4` (Devis → Facture directe) ou `T-AVOIR` est
ouverte** dans `17-BUILD-GATES-AND-SLICE-CONTRACT.md` du Product Blueprint
principal — pas avant, et toujours pas pour enrichir le premier pilote
métier V1 (tranches `T0`-`T8` ; la verticale exacte reste `Q7`, à trancher
par le PO, non décidée ici), qui n'en a pas besoin.

**Ce dossier n'est plus dormant.** La Canonical Execution Layer
(`16`-`20` du Product Blueprint principal) existe désormais sur disque —
`16-CANONICAL-EXECUTION-INDEX.md` §9 référence explicitement cette annexe,
et `17` cite `01`/`06` directement dans ses sections `T4`/`T-AVOIR`
(mission de consolidation T4, 2026-09-25). **Nuance de statut Git** : `16`,
`17`, `19`, `README` du blueprint principal et `20` existent réellement sur
disque mais restent non committés au moment de cette mise à jour — vérifier
`git status` avant de considérer la Canonical Execution Layer comme figée.

## Lesquels sont canoniques

| Document | Rôle |
|---|---|
| `01-E-INVOICING-CANONICAL-DOMAIN.md` | **Canonique** — le contrat de données, la doctrine de projection de format, le contrat d'échange, la matrice d'idempotence, et la liste explicite « ne pas copier ». Point de référence principal. |
| `02-E-INVOICING-FRONTEND-CONTRACT.md` | **Canonique** — contrat UX par état, dérivé de `01`. |
| `03-E-INVOICING-BACKEND-CONTRACT.md` | **Canonique** — contrat de responsabilités backend, dérivé de `01`. Aucun SQL. |
| `04-ACCOUNTING-EXPERT-INTEROP-REFERENCE.md` | **Canonique** — export/connecteur/accès délégué comptable, classés par version cible. |
| `05-ACCEPTANCE-NEGATIVE-TEST-MATRIX.md` | **Canonique** — tests à préparer, jamais codés ici. |
| `06-ANTIGRAVITY-HANDOFF-PACK.md` | **Canonique, point d'entrée unique pour Antigravity** au moment venu — condense `01`-`05`, ne les recopie pas. |

Les trois fichiers sources fournis par l'utilisateur (`api axonaut.md`, `api-evolizdocs.txt` [Evoliz v1.43], `api-docs.txt` [Evoliz v1.56], situés hors du dépôt sous `C:\Users\devfi\Downloads\`) **ne sont jamais canoniques** et ne doivent jamais être transmis tels quels à Antigravity — voir la section « Ce qu'ils ne doivent jamais provoquer » ci-dessous.

## Quelles sources ont servi

- **Réglementaire/officiel** (source de vérité) : décret n° 2026-677 du 27/07/2026 (Légifrance, lu directement) ; impots.gouv.fr (calendrier, formats, plateformes agréées, mentions obligatoires — pages datées, lues directement) ; AIFE (annuaire, spécifications techniques) ; FNFE-MPE (norme Factur-X, lue directement) ; service-public.gouv.fr (mentions obligatoires facture, page du 11/08/2026) ; norme EN 16931 (Commission européenne, citée par FNFE-MPE) ; recoupement avec `docs/product-blueprint-antigravity/06-ANNEXE-recherche-api-candidats.md` §9 (recherche indépendante antérieure du même jour, convergente).
- **Implémentation/comparaison** (jamais source de vérité) : documentation API Axonaut v2.0.0 (export Swagger, ~8 780 lignes) ; documentation API Evoliz v1.43 (export OpenAPI 3.0, ~20 400 lignes, aucune couche e-invoicing) ; documentation API Evoliz **v1.56** (export OpenAPI 3.0, ~22 850 lignes, second snapshot analysé lors d'une mission corrective — porte un cycle de facturation électronique réel, voir `01` §4bis).

Chaque affirmation de `01`-`06` porte un statut explicite : `LEGAL_VERIFIED`, `OFFICIAL_SPEC`, `IMPLEMENTATION_EXAMPLE`, `SUPORDO_DECISION`, `ANALYSIS`, ou `OPEN`. Une affirmation `IMPLEMENTATION_EXAMPLE` (Evoliz/Axonaut) n'est **jamais** une preuve réglementaire, même quand ces éditeurs affirment eux-mêmes citer une loi — voir `01` §7 (règles affirmées par Evoliz, à vérifier séparément).

## Points de correction signalés

`docs/product-blueprint-antigravity/06-ANNEXE-recherche-api-candidats.md` §9.4 cite Factur-X en version « 1.08, décembre 2025, non confirmée par fetch direct ». La recherche menée pour cette annexe a obtenu, par fetch direct de fnfe-mpe.org, la version **1.09.2 / ZUGFeRD 2.5.2, publiée le 4 août 2026**. Ce fichier-ci ne modifie pas l'annexe existante (hors périmètre de cette mission) — voir `01` §3 pour le détail sourcé.

**Corrections internes à cette annexe, apportées par une mission corrective ultérieure** (tracées dans les fichiers eux-mêmes) : l'affirmation initiale « Evoliz n'expose aucune facturation électronique structurée » était vraie pour la version 1.43 seule, fausse pour la version 1.56 ultérieurement fournie (`01` §4bis) ; le modèle « plusieurs taux de TVA par ligne » était dérivé à tort d'Axonaut et contredit la norme EN 16931 elle-même, une ligne ne porte qu'un seul taux (`01` §2.4) ; la doctrine Lieu/adresse est passée de « référence ou snapshot » à « référence et snapshot, les deux coexistent » (`01` §2.1) ; le champ de corrélation externe a été retiré de la Facture et recentré sur `ElectronicInvoiceExchange` (`01` §4, `03` §3, `06` §15).

## Ce que ces documents ne doivent jamais provoquer

- Ne jamais transmettre les fichiers sources Axonaut/Evoliz à Antigravity — seul `06-ANTIGRAVITY-HANDOFF-PACK.md` doit lui être donné.
- Ne jamais présenter une structure, un statut ou un champ Evoliz/Axonaut comme une obligation légale SUPORDO.
- Ne jamais coder une version de format (Factur-X 1.09.2, UBL 2.1...) comme un invariant métier — le format est une projection versionnée, pas le domaine.
- Ne jamais faire dépendre SUPORDO d'un fournisseur de plateforme agréée nommé.
- Ne jamais avancer le calendrier de la facturation électronique dans le V1 du Product Blueprint principal — cette annexe prépare, elle n'exécute pas.
