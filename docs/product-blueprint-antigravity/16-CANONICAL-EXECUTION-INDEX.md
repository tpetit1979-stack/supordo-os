# 16 — Canonical Execution Index

Court et autoritaire. En cas de contradiction entre `00`→`15` et ce document
(`16`-`19`), **`16`-`19` prévalent** — mais chaque correction ci-dessous cite la
source qui l'a justifiée, jamais une réécriture sans preuve.

## 1. Rôle de ce document

`00`→`15` sont **RESEARCH / HISTORY / EVIDENCE / AUDIT** — ils restent
inchangés, ils prouvent, ils ne s'exécutent pas directement.

`16`→`19` sont la **CANONICAL EXECUTION LAYER** — la seule couche qui peut être
transformée en `SLICE PACKET` (`19`) transmis à `supordo-app`, puis à Google
Antigravity ou à tout développeur humain.

```
DOCUMENTATION CANONIQUE (16→19)
        ↓
   SLICE PACKET (19 rempli)
        ↓
   supordo-app
        ↓
   Google Antigravity / Claude Code / humain
```

**Antigravity ne reçoit jamais `00`→`15` directement.** Voir `17` pour le
détail des tranches et `18` pour le contrat opérationnel Windows.

## 2. Ordre de précédence

1. `0007-contraintes-acquises.md` — reste opposable, jamais réécrit ici.
2. `16`-`19` (ce document et ses trois suites) — priment sur toute lecture
   antérieure de `00`→`15` en cas de contradiction.
3. `15-RED-TEAM-GATE.md` — audit adverse, source de la majorité des
   corrections ci-dessous ; **une trouvaille de `15` n'est pas automatiquement
   une solution canonique** — voir §3 méthode.
4. `01`→`14` — recherche, preuve, doctrine historique. Consultés pour le détail
   et la justification, jamais transmis tels quels à un agent d'exécution.
5. `docs/integration-blueprints/e-invoicing-accounting/` — annexe spécialisée,
   **hors périmètre de `16`-`19`**, reste dormante (§9).

## 3. Méthode appliquée à chaque point de `15`

Pour chaque problème détecté par `15`, cinq statuts distincts ont été tenus
séparés — **une proposition de l'auditeur n'est jamais devenue automatiquement
une `SUPORDO_DECISION`** :

`A. PROBLÈME CONFIRMÉ` · `B. INVARIANT CONFIRMÉ` · `C. SOLUTION PROPOSÉE PAR
LA RED TEAM` · `D. DÉCISION CANONIQUE RÉELLEMENT AUTORISÉE` · `E. OPEN` (si le
choix précis n'est pas encore acté).

Exemple appliqué (Lieu, détail complet en §5 et `17`) : `15` B1 = A+B confirmés
(Lieu absent de la séquence, S1 reste opposable) ; `15` propose « Client 1→N
Lieu » = **C, une proposition, pas D**. La décision canonique réellement
autorisée (D) est plus étroite : Lieu doit être first-class, avec identité
propre, dès la tranche qui crée Client — **la cardinalité exacte reste E,
`OPEN`/`STRUCTURAL_BEFORE_SCHEMA`**.

## 4. Supersession Map — 15 corrections enregistrées

| # | Sujet | Ancienne source | Ancienne conclusion | Source corrective | Conclusion à utiliser | Impact si la mauvaise version est lue |
|---|---|---|---|---|---|---|
| 1 | Fumisterie : niveau de preuve | `README`, `01` §5, `02`, `07` §0 | Aucune preuve en centre d'aide ; `MARKETING_ONLY` seul | `10` §0.1 | Preuve fonctionnelle réelle à 1 témoin (OpenFire Odoo) ; écart 2 vs 1, pas 2 vs 0 | Q7 arbitrée sur une asymétrie surévaluée |
| 2 | Verrou de mutabilité du devis | `09` Q3 | « Verrouiller à la première sortie structurante (M10) » | `12` §0.5 | M10 = changement d'**état** ; O3 = verrou de **contenu**, deux événements distincts. Verrou à l'engagement (T3), pas à l'envoi (T2) | Devis verrouillé dès l'envoi, contredit M5 |
| 3 | Justification « transformation directe » | `09` Q4 | « Cohérente avec l'absence de preuve d'un pivot » | `12` §0.6 (source exacte : V0 §11, pas §17, corrigé par `15` C6) | Le pivot **est** documenté (3/8). Justification réelle : pluralité 4/8 + modèle le plus direct pour un solo + pas d'objet commande imposé | Décision `STRUCTURAL_BEFORE_SCHEMA` prise sur un fait faux |
| 4 | Classement CORE des services techniques | `02` §2 | Auth, RLS, multi-tenant, transcription vocale = `CORE`, au rang de Client/Devis | `12` §0.2 | `PLATFORM_CAPABILITY` — service technique transversal, distinct de l'objet métier | Connecteur fournisseur modélisé comme objet métier |
| 5 | Chantier et Intervention | `02` §2, `03` §1 | Une seule fiche/ligne fusionnée | `12` §0.3 | Deux objets distincts ; **Q18** ouverte, `STRUCTURAL_BEFORE_SCHEMA` | Fusion de deux objets encore `OPEN` en une table |
| 6 | Rôles/permissions : niveau de preuve | `09` Q11 | « Preuve faible (5/10), jamais détaillée » | `10` §0.2 | Obat documente 7 rôles + permissions individuelles. Rôles minimaux restent défendables en V1, mais plus par absence de preuve | Sous-dimensionnement du **modèle**, pas seulement de l'UI |
| 7 | Devis vocal : niveau de preuve | `05` (préambule) | 2 précédents fonctionnels + 2 `MARKETING_ONLY` | `10` §0.3 | 3 témoins `ACQUIS DOCUMENTAIRE` (InterFast, OpenFire Zendesk, Obat) | Thèse centrale du PO sous-évaluée |
| 8 | Périmètre IA du V1 | `05` §10, `07` §1 | Transcription vocale libre (#4) + pilote devis vocal **en V1** | `12` §0.4/T8, `13` §T8 | Aucune IA en V1, tout en `T8-VOIX` (V2) | Contradiction non résolue — voir §7 ci-dessous, statut rendu explicite ici |
| 9 | Irréversibilité : niveaux couverts | `08` §7, `09` | Niveau **document** (facture, avoir) | `10` §0.5, `11` P7 | Troisième niveau : bascule irréversible au niveau **compte entier** | Bascule irréversible présentée comme un réglage ordinaire |
| 10 | Complexité du relevé terrain | `01` §7 | `FORTE` en bloc | `12` §0.9 | `FAIBLE-MOYENNE` niveau 1 (T8) ; `FORTE` niveaux 2-4 | T8 différé à tort ou sur-construit d'emblée |
| 11 | Devis : une tranche ou deux ? | `07` §1 | Une ligne (« naissance + un modèle de verrouillage ») | `12` §0.9 | Deux tranches distinctes : changement d'état (T1/T2), verrou (T3) | Une tranche mélangeant deux décisions dont une reste `OPEN` |
| 12 | L4 / facture importée | `0007` L4 | Interdiction ProGBat = « choix éditeur » | `10` §0.4 | Tension non résolue : ProGBat invoque une base légale non vérifiable. **Statut `SUPORDO_DECISION` de L4 inchangé** (il porte sur ce que fait SUPORDO, pas sur ProGBat) | Import construit sur une lecture légale non vérifiée |
| 13 | Registre des questions ouvertes | `09` Partie A | 17 questions (Q1-Q17) | `12` §0.3 et §0.7 | 19 questions — Q18 (`STRUCTURAL_BEFORE_SCHEMA`), Q19 (`CAN_WAIT_V2`) | Voir §6 — registre unique ci-dessous, ce trou est refermé par ce document |
| 14 | Carte des documents | `README` (blueprint) | 9 documents (`01`-`09`) | Existence de `10`-`15` | 15 documents avant cette mission, 19 désormais | Porte d'entrée périmée — corrigé au `README` par cette mission |
| 15 | Terminologie facturation électronique | `06` §2, `07`, `08` §14, `09` Q13, `12` T4 | « PDP » (Plateforme de Dématérialisation Partenaire) | `docs/integration-blueprints/.../06-ANNEXE-recherche-api-candidats.md` §9.2 | Décret n° 2026-677 : notion unique de « plateforme agréée » (PA) | Interface nommée d'après un statut juridique supprimé — **hors périmètre de `16`-`19`, voir §9** |

**Aucune de ces 15 lignes n'a été rouverte par cette mission** — elles sont
reprises telles que `15` les a établies, avec vérification que chaque
« conclusion à utiliser » est bien sourcée dans `10`/`12`/l'annexe, pas une
réinterprétation nouvelle.

## 5. Trois corrections structurelles supplémentaires, cadrées par cette mission

Ces points ont été **confirmés comme problèmes** par `15` (A/B), mais leur
**solution proposée** (C) a été distinguée de la **décision canonique
réellement autorisée** (D) — voir méthode §3.

### 5.1 Lieu (`15` B1)

- **A/B confirmés** : S1 (`SUPORDO_DECISION`, `0007`) est opposable ; aucune
  tranche de `12` ne construit Lieu ; le gate `15` le désigne comme effet
  domino n°1.
- **C, proposition de `15`** : cardinalité « Client 1→N Lieu ».
- **D, décision canonique réellement autorisée** : Lieu est un objet
  first-class dès la première tranche métier qui crée Client (`17` T1) ; Lieu
  possède sa propre identité ; l'historique opérationnel peut s'y rattacher ;
  le modèle permet un changement futur de propriétaire/locataire/payeur sans
  recréer le Lieu ; Client et Lieu ne sont jamais fusionnés.
- **E, `OPEN`** : la cardinalité exacte Client↔Lieu n'est **pas** actée ici —
  `STRUCTURAL_BEFORE_SCHEMA`, voir `17` GO-02.

### 5.2 Catalogue partagé vs privé au tenant (`15` B3)

- **A/B confirmés** : des données techniques potentiellement partagées et des
  données commerciales privées au tenant (prix d'achat, remise, marge,
  personnalisation) ne peuvent pas vivre sans frontière de sécurité explicite.
- **C, proposition de `15`** : `referentiel_produit` + `article_catalogue`.
- **D, décision canonique réellement autorisée** : c'est une
  **`ARCHITECTURE_CANDIDATE` forte** (voir §8) — pas une `SUPORDO_DECISION`
  issue du corpus. Les invariants suivants sont en revanche canoniques dès
  maintenant : prix d'achat/remise/marge/personnalisation tenant = **toujours
  privés** ; toute donnée privée porte l'isolation tenant appropriée ; une
  donnée globale/partagée n'expose **jamais** de donnée commerciale tenant ;
  aucun tenant ne peut écrire arbitrairement dans un référentiel global.
- **E, `OPEN`** : la forme exacte (deux tables, un schéma, autre mécanisme)
  reste à arbitrer avant la première migration catalogue — `17` GO-04.

### 5.3 RLS « héritée » (`15` B2)

- **A/B confirmés** : « RLS héritée de T0 »/« inchangée » est **techniquement
  faux** en PostgreSQL — RLS s'active et se définit par table, sans mécanisme
  d'héritage.
- **C, proposition de `15`** : obligation explicite par migration + tests
  cross-tenant read/write à partir de T2 + test Storage à T8.
- **D, décision canonique réellement autorisée** — reprise **telle quelle**,
  aucune raison de l'affaiblir : **toute nouvelle table tenant-private créée
  par une tranche (1) active RLS dans la même migration, (2) possède ses
  policies dans la même migration, (3) possède au moins un test cross-tenant
  READ et un test cross-tenant WRITE, (4) ne passe pas la Definition of Done
  sans ces tests.** Storage Supabase possède ses propres règles/policies —
  toute tranche créant des fichiers tenant-private teste séparément
  l'isolation Storage. Détail complet en `17` GLOBAL_BUILD_GATE.

## 6. Registre unique Q1→Q19

Reconcilié depuis `09` Partie A (Q1-Q17) et `12` §0.3/§0.7 (Q18-Q19), sans
suppression. Urgences inchangées ; `Q3` et `Q4` portent leur justification
corrigée (supersession §4 lignes 2-3).

| # | Question | Urgence | Qui décide |
|---|---|---|---|
| Q1 | Ligne libre hors catalogue, oui/non ? | `BLOCKS_V1` | PO |
| Q2 | Signature = acceptation, ou deux événements ? | `BLOCKS_V1` | PO |
| Q3 | Verrou de mutabilité du devis — **distinct de M10 (changement d'état)** | `BLOCKS_V1` | PO |
| Q4 | Objet pivot devis→facture, ou transformation directe ? | `STRUCTURAL_BEFORE_SCHEMA` | PO |
| Q5 | Mécanismes de dérivation à retenir | `CAN_WAIT_V2` | PO |
| Q6 | Minimum de contenu pour finaliser un devis ? | `BLOCKS_A_SLICE` | PO |
| Q7 | Verticale de lancement (fumisterie ou climatisation/PAC) — **preuve corrigée, voir supersession §4.1** | `BLOCKS_V1` | PO |
| Q8 | Sens de la relation devis ↔ intervention | `FIELD_TEST_REQUIRED` puis `STRUCTURAL_BEFORE_SCHEMA` | Terrain puis PO |
| Q9 | Jusqu'où automatiser Cerfa/Trackdéchets en V1 ? | `BLOCKS_A_SLICE` | PO |
| Q10 | Séparer Personnel et Compte utilisateur dès quand ? | `CAN_WAIT_V2` | PO |
| Q11 | Granularité des rôles/permissions — **preuve corrigée, voir supersession §4.6** | `CAN_WAIT_V2`/`V3` | PO |
| Q12 | Vérification officielle de L1/L2/L3 | `LEGAL_VERIFICATION_REQUIRED` | PO/juridique |
| Q13 | Facturation électronique : détails PA/Factur-X — **hors périmètre `16`-`19`, voir §9** | `LEGAL_VERIFICATION_REQUIRED` | PO/juridique |
| Q14 | Généralisation cascade maintenance/parc installé | `FIELD_TEST_REQUIRED` | Terrain |
| Q15 | Usage réel capture voix/photo terrain | `FIELD_TEST_REQUIRED` | Terrain |
| Q16 | Besoin réel de mode hors-ligne au-delà de la capture terrain | `FIELD_TEST_REQUIRED` | PO/terrain |
| Q17 | Critère de bifurcation devis→chantier vs devis→intervention | `STRUCTURAL_BEFORE_SCHEMA` | PO |
| Q18 | Chantier et Intervention : deux objets, quelle relation ? | `STRUCTURAL_BEFORE_SCHEMA` | PO |
| Q19 | Objet Demande/Lead nécessaire avant Client ? | `CAN_WAIT_V2` | PO |

**Source unique** : ce tableau. `09` Partie A et `12` §0.3/§0.7 restent
consultables pour le détail (options documentées, impact backend/UX,
recommandation analytique) mais ne sont plus la référence d'urgence — en cas
d'écart, `16` prévaut.

## 7. Fonctions disparues — reclassification (`15` C1, C2 ; mission §10)

Aucune décision à la place du PO ici — seulement un statut explicite, avec
source et raison, pour qu'aucune de ces trois capacités ne reste « oubliée ».

| Capacité | Statut | Source | Raison |
|---|---|---|---|
| **Avoir** | `V1` | `07` §1 (« Facture + Avoir (L1 immuabilité) » en core minimum) ; `03` (seul véhicule de correction documenté, `HARD`, 6/7 éditeurs) ; `10` M1 (motif quasi universel, 9/10) | `15` C1 (erreur majeure) : sans Avoir, une facture erronée émise en pilote n'a aucun recours produit — le contournement documenté (éditer le PDF hors produit, `10` §2) est précisément ce que `12` T4 refuse. Tranche `T-AVOIR` créée en `17`, gate avant toute émission réelle de facture. |
| **Planning/RDV** | `V1` | `07` §1 (« universel 10/10, nécessaire à toute intervention », débloque parcours A et D) | `15` C2 (erreur majeure) : `07` le place en V1 core, `12` l'omettait silencieusement. Tranche `T-PLANNING` créée en `17`. |
| **Transcription vocale libre (`05` opportunité #4)** | **`OPEN`** — contradiction non tranchée, voir supersession §4.8 | `05` §10 et `07` §1 la placent en V1 ; `12` §0.4/T8 et `13` §T8 l'excluent entièrement de V1 (tout en `T8-VOIX`, V2) | Ni `05`/`07` ni `12`/`13` n'ont été rouverts par cette mission — le désaccord est réel, pas résolu. **Gate explicite en `17`** : le PO tranche si la transcription pure (sans structuration, sans rattachement catalogue) est un composant V1 séparable de `T8-VOIX`, conformément à la décomposition en couches imposée par la mission §9 (voir `17`). |

## 8. `SUPORDO_DECISION` actives vs `ARCHITECTURE_DECISION` vs `ARCHITECTURE_CANDIDATE`

Trois catégories, à ne jamais confondre :

- **`SUPORDO_DECISION`** — arbitrage produit du PO, sourcé dans `0007`. Liste
  complète : **S1** (Lieu distinct du Client), **S2** (objet sans parent),
  **S3** (prix catalogue figé à la création), **S4** (provenance ciblée), **S5**
  (consentement médias publiables), **L4** (facture importée ≠ émise).
- **`ARCHITECTURE_DECISION`** — règle technique non négociable, dérivée
  directement d'un invariant déjà acté, sans arbitrage produit nécessaire.
  Actée ici : **RLS + policies dans la même migration que toute nouvelle
  table tenant-private** (§5.3) ; **numérotation de facture garantie au
  niveau base/DB, testée sous concurrence** (`0007` L3, `15` B9) ; **Lieu
  first-class dès la tranche créant Client** (§5.1, hors cardinalité).
- **`ARCHITECTURE_CANDIDATE`** — proposition d'architecture forte, pas encore
  arbitrée. Actée ici : `referentiel_produit`/`article_catalogue` (§5.2) —
  à trancher avant `17` GO-04.

## 9. `LEGAL_*`

**`LEGAL_CITÉ`** (cité par des sources concurrentes, jamais vérifié à la
source officielle) : **L1** (facture numérotée immuable), **L2** (avoir même
régime), **L3** (numérotation séquentielle continue) — tous trois
`LEGAL_VERIFICATION_REQUIRED` avant mise en production réelle (Q12).

**Facturation électronique (Factur-X/plateforme agréée)** : `EXPLICITEMENT
HORS PÉRIMÈTRE` de `16`-`19`. L'annexe `docs/integration-blueprints/e-invoicing-
accounting/` existe séparément et devra être corrigée à part (notamment après
analyse complète Evoliz 1.56, déjà faite dans l'annexe elle-même). Pour toute
tranche Facture/e-invoicing dans `17`, la seule mention autorisée est :

> **E-INVOICING SPECIALIZED CONTRACT REQUIRED BEFORE INVOICE/E-INVOICING
> IMPLEMENTATION**

## 10. `MARKET_BASELINE`

Seize convergences de marché (M1-M16, `0007`), de preuve variable (8/8 pour
M1/M3 à 1 témoin pour M15/M16) — **jamais une obligation SUPORDO**, adoptées
comme hypothèse de départ seulement en l'absence de décision contraire. Détail
intégral : `0007` §M. Les plus structurantes pour `17` : **M1** (client
créable à la volée, 8/8), **M5** (l'envoi ne verrouille rien, 3 éditeurs), **M8**
(acompte/situation recalculés jamais ressaisis, 6 éditeurs), **M10** (le devis
change d'état à sa première sortie structurante, 7/8).

## 11. `OPEN` — synthèse

Toutes les lignes `OPEN`/`STRUCTURAL_BEFORE_SCHEMA`/`FIELD_TEST_REQUIRED` du
registre §6, plus : la cardinalité Client↔Lieu (§5.1), la forme exacte du
catalogue partagé (§5.2), l'inclusion V1 de la transcription vocale libre
(§7), et les neuf ambiguïtés `D1`-`D9` de `15` (O1-O6/Q1-Q6 intacts à 0
décision actée — le contrat V0 les liste toutes comme réservées au PO ou
`NON DÉTERMINÉ`, jamais arbitrées malgré le gate « prêt pour décision
produit » ; la relation Chantier/Intervention ; le critère de bifurcation
Vertuoza ; le minimum de contenu du devis, signal à 1 témoin non repris par
V0 ; le mode référence-vivante d'un catalogue synchronisé externe ;
la terminologie PDP/PA, hors périmètre). **Ne pas combler par une décision
silencieuse — c'est la règle la plus souvent violée quand une couche
d'exécution est produite sous pression.**

## 12. Références vers les gates de `17`

Le détail opérationnel (GLOBAL_BUILD_GATE, matrice GO reclassifiée, tranches
T0→T8, candidats de première tranche corrigés) est dans
`17-BUILD-GATES-AND-SLICE-CONTRACT.md`. Ce document (`16`) ne contient aucune
tranche — seulement le registre qui les gouverne.
