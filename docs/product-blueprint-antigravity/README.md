# SUPORDO — Product Blueprint (Antigravity handoff)

Synthèse exécutive. Ce dossier transforme le corpus concurrentiel et la doctrine
produit du dépôt SUPORDO en matière exploitable pour construire un vrai MVP avec
Google Antigravity + Supabase. **Aucun fichier source du dépôt n'a été modifié.
Aucun code applicatif n'a été créé. Aucune table Supabase n'existe encore.**

## Deux couches, à ne jamais confondre

**`00`→`15` = RESEARCH / HISTORY / EVIDENCE / AUDIT.** Recherche
concurrentielle, doctrine produit, séquence de build historique, audit
indépendant adverse (`15-RED-TEAM-GATE.md`, verdict `NOT_READY`). Ces
documents prouvent et expliquent — **ils ne constituent plus directement le
contrat donné à Antigravity.**

**`16`→`19` = CANONICAL EXECUTION LAYER.** Courte, autoritaire, corrigée après
audit. `16-CANONICAL-EXECUTION-INDEX.md` est le point d'entrée : ordre de
précédence, supersession map, registre unique des décisions ouvertes.
`17-BUILD-GATES-AND-SLICE-CONTRACT.md` porte les tranches et les gates.
`18-ANTIGRAVITY-WINDOWS-OPERATING-CONTRACT.md` remplace `14` comme contrat
opérationnel réel. `19-SLICE-HANDOFF-TEMPLATE.md` est le moule de chaque
packet de tranche.

**DO NOT GIVE `00`→`15` DIRECTLY TO ANTIGRAVITY.** Antigravity reçoit un
`SLICE PACKET` dérivé de `16`→`19` (via `docs/slices/<SLICE_ID>/`, format
`19`), jamais le dossier `00`→`15` en bloc.

```
DOCUMENTATION CANONIQUE (16→19)
        ↓
   SLICE PACKET (19 rempli)
        ↓
   supordo-app
        ↓
   Google Antigravity / Claude Code / humain
```

## Le produit

SUPORDO est un CRM/mini-ERP pour artisans et petites entreprises de terrain. La
direction produit, donnée par le PO (pas une conclusion du corpus) : **CORE
commun + PACKS MÉTIERS**, pour éviter à la fois le CRM BTP généraliste peu
différencié et le logiciel monométier impossible à étendre.

Le CORE porte les capacités communes : clients, lieux, devis, planning,
intervention, chantier, facturation, paiement, documents, photos, historique.
Les packs métiers apportent catalogues, caractéristiques techniques, formulaires
de relevé, règles de calcul, conformité réglementaire et vocabulaire propres à
un corps de métier.

## Ce que le corpus a réellement permis d'établir

Le corpus (2 510 documents de centre d'aide LIGHT, 12 éditeurs français, + un
premier balayage de ~4 200 pages marketing jamais analysées avant cette mission)
a permis de construire un **contrat fonctionnel solide sur l'objet Devis** (8
corpus, 3 missions d'audit détaillées) et des fragments exploitables sur les
autres objets (Client, Catalogue, Facture, Avoir, Chantier/Intervention,
Personnel). Il a en revanche confirmé, sur plusieurs axes indépendants (objets,
parcours, capacités), que **les zones où SUPORDO doit se différencier —
intervention, parc installé, capture terrain, usage solo — sont précisément
celles que le corpus documente le moins.** Ce n'est pas une lacune de méthode :
c'est un fait de marché (un centre d'aide documente ce qui coince, pas la
routine terrain) à assumer, pas à combler par des suppositions.

**Découverte structurante du balayage marketing** : sur le volet
climatisation/PAC/chauffage, OpenFire et InterFast documentent tous deux, dans
leur centre d'aide (`ACQUIS DOCUMENTAIRE`), un module réglementaire réel et
profond (fluides frigorigènes, Cerfa 15497). Sur le volet fumisterie/poêles-
cheminées en revanche, la seule preuve disponible est une page produit et un
catalogue fabricants chez OpenFire, **jamais confirmés en centre d'aide**
(`MARKETING_ONLY` — aucun des 12 corpus d'aide étudiés ne documente cette
verticale). C'est la meilleure preuve disponible que le modèle CORE + PACKS
MÉTIERS est viable, mais elle est asymétrique entre les deux verticales de
stress-test du PO — ce qui oriente directement la recommandation de verticale
de lancement ci-dessous.

## Frontière CORE / VERTICAL — le stress-test tient

Testée sur fumisterie vs climatisation/PAC/chauffage (`02`), l'abstraction
CORE + PACKS tient : aucune des deux verticales n'oblige à dupliquer le moteur
devis, facture, planning ou l'objet Lieu. Ce qui varie systématiquement — et
doit donc vivre dans un pack — c'est le catalogue, le schéma de relevé terrain,
les règles de calcul, la référence réglementaire précise et la liste de photos
attendues. Risques de mauvaise abstraction identifiés et leurs mitigations :
`02` §4.

## V1 recommandé

**CORE minimum** (Client, Lieu, Devis avec un modèle de verrouillage unique,
Catalogue à schéma technique typé dès le départ, Facture + Avoir avec
immuabilité légale, acompte/solde recalculés automatiquement, planning simple,
utilisateurs simples, interface abstraite vers un PDP de facturation
électronique) **+ un pack métier profond**.

**Verticale recommandée pour ce premier pack : climatisation / PAC / chauffage**
— `RECOMMANDATION ANALYTIQUE`, pas une décision. C'est la seule verticale du
corpus avec deux preuves fonctionnelles indépendantes et le meilleur précédent
pour la thèse IA du PO (OpenFire Zendesk : visite → devis généré
automatiquement). **Le PO cite pourtant la fumisterie en premier exemple** —
c'est un écart à trancher explicitement, pas à décider silencieusement (`07`
§0, `09` Q7).

Détail complet, y compris IA embarquée en V1 (transcription vocale, premier
pilote devis vocal) et intégrations V1 (email, stockage, signature
électronique, identité entreprise) : `07-V1-V2-V3-80-20.md`.

## Risques majeurs

Le trou documentaire le plus coûteux du corpus (transformation devis→facture,
la plus fréquente et la moins documentée), la bascule réglementaire de
facturation électronique au 01/09/2027, et les risques d'exécution propres à
Antigravity (simulation présentée comme réelle, promesses non tenues) sont les
trois risques qui structurent le plus la conception. Liste complète et
mitigations : `09` Partie B.

## Décisions majeures encore ouvertes

Registre unique **Q1→Q19**, source faisant foi : `16-CANONICAL-EXECUTION-
INDEX.md` §6 — chaque question porte un statut d'urgence (`BLOCKS_V1`,
`STRUCTURAL_BEFORE_SCHEMA`, `FIELD_TEST_REQUIRED`, `LEGAL_VERIFICATION_
REQUIRED`, etc.). Les plus urgentes concernent directement le devis
(verrouillage, minimum de contenu, ligne libre — héritées telles quelles de
`0007` O1-O6, jamais rouvertes ni recopiées avec perte) et le choix de
verticale de lancement.

## Carte des documents

| Document | Contenu |
|---|---|
| `01-CAPABILITY-MAP.md` | Inventaire des capacités, sources, verticalités, analyse 80/20 qualitative |
| `02-CORE-VERTICAL-BLUEPRINT.md` | Frontière CORE/VERTICAL, stress-test fumisterie vs clim/PAC, risques d'abstraction |
| `03-DOMAIN-DEPENDENCIES-LIFECYCLES.md` | Objets métier, états, graphe de dépendances (Mermaid), propagations, effets domino |
| `04-JOURNEYS-UX-BLUEPRINT.md` | 9 parcours bout-en-bout classés par niveau de preuve, architecture de l'information par zone |
| `05-AI-AND-AUTOMATION-BLUEPRINT.md` | Carte des opportunités IA, thèse voix+vertical+catalogue+relevé |
| `06-INTEGRATIONS-API-HORIZON.md` + annexe | Besoins d'intégration, candidats API sourcés (20 catégories), réforme facturation électronique |
| `07-V1-V2-V3-80-20.md` | Backlog V1/V2/V3/Parking Lot, verticale de lancement recommandée |
| `08-BACKEND-AND-NONFUNCTIONAL-CONTRACT.md` | Contraintes de conception pour le futur backend Supabase — aucun SQL |
| `09-DECISIONS-RISKS-ANTIGRAVITY-HANDOFF.md` | Registre de décisions, risques, protocole et templates de prompts pour Antigravity — **partiellement corrigé, voir `16`** |
| `10-SUPPORT-FRICTION-RECOVERY-ATLAS.md` | Frictions concurrentielles minées dans les centres d'aide, motifs transversaux, corrections apportées à `01`-`09` (§0) |
| `11-SIMPLIFICATION-PRINCIPLES.md` | Principes PREVENT/DETECT/EXPLAIN/RECOVER dérivés de `10` |
| `12-ANTIGRAVITY-BUILD-SEQUENCE.md` | Séquence de tranches V1 historique — **supersédée par `17` sur plusieurs points, voir `16` §4** |
| `13-ACCEPTANCE-NEGATIVE-TEST-MATRIX.md` | Matrice de tests par tranche historique — référencée par `17`, corrigée par les GO de `17` §1 |
| `14-ANTIGRAVITY-OPERATING-PACK.md` | Contrat opérationnel Antigravity historique — **remplacé par `18`, ne plus utiliser seul (`15` verdict)** |
| `15-RED-TEAM-GATE.md` | Audit indépendant adverse, verdict `NOT_READY`, source de la majorité des corrections de `16`-`19` |
| `16-CANONICAL-EXECUTION-INDEX.md` | **Point d'entrée de la couche d'exécution** — ordre de précédence, supersession map, registre Q1-Q19 |
| `17-BUILD-GATES-AND-SLICE-CONTRACT.md` | Tranches corrigées (Lieu réintégré, Avoir/Planning réintégrés, candidats corrigés), matrice GO reclassifiée |
| `18-ANTIGRAVITY-WINDOWS-OPERATING-CONTRACT.md` | Contrat opérationnel réel, PRE-FLIGHT Windows, statut ENFORCED/CONSULTATIF par mécanisme |
| `19-SLICE-HANDOFF-TEMPLATE.md` | Modèle exact de packet de tranche, format `docs/slices/<SLICE_ID>/` |

## Discipline de preuve appliquée

Statuts utilisés sans exception dans l'ensemble du dossier : `ACQUIS DOCUMENTAIRE` ·
`MARKET_BASELINE` · `VARIANTE DE MARCHÉ` · `SUPORDO_DECISION` (opposable,
`0007`) · `RECOMMANDATION ANALYTIQUE` (jamais une décision) · `OPEN` /
`À TESTER TERRAIN` · `NON DÉTERMINÉ` · `MARKETING_ONLY`. Une convergence
concurrentielle n'est jamais lue comme une obligation ; un silence documentaire
n'est jamais lu comme une absence fonctionnelle ; aucune affirmation marketing
n'est présentée comme une preuve de fonctionnement.
