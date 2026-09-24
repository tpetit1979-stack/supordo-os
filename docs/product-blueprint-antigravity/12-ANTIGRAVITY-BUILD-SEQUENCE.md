# 12 — Antigravity Build Sequence

Transforme le V1 du blueprint (`07-V1-V2-V3-80-20.md`) en tranches de construction
réellement exécutables et vérifiables par Google Antigravity. **Ne modifie aucun
fichier `00-09`** — les corrections identifiées ci-dessous sont documentées ici,
pas rétro-appliquées.

Les « cas limites » de chaque tranche s'appuient, quand pertinent, sur
`10-SUPPORT-FRICTION-RECOVERY-ATLAS.md` (frictions réellement observées chez les
concurrents) et `11-SIMPLIFICATION-PRINCIPLES.md` (principes PREVENT/DETECT/
EXPLAIN/RECOVER qui en découlent) — référencés explicitement par leur code (Mx,
Px) plutôt que reformulés.

## 0. Réconciliation du blueprint (préalable obligatoire à la séquence)

Contrôle explicite demandé par la mission avant toute construction de tranches.
Chaque point est traité séparément — aucune correction silencieuse.

### 0.1 CORE+PACKS reste une direction PO, pas une conclusion du corpus

`02-CORE-VERTICAL-BLUEPRINT.md` le dit dès son ouverture : « le corpus n'a jamais
été construit pour tester une architecture CORE+PACKS — c'est une direction
produit du PO ». **Précision nécessaire** : le « stress-test » de `02` §3 vérifie
une **cohérence structurelle interne** (l'abstraction ne casse pas quand on
l'applique à deux verticales) — ce n'est ni une validation empirique, ni une
preuve d'adoption. Toute phrase future du type « l'abstraction tient » doit être
lue comme « n'a pas été invalidée par un raisonnement structurel », jamais comme
« validée par le marché ». Aucune tranche ci-dessous ne doit présenter le
découpage CORE/PACKS comme un acquis prouvé auprès de l'utilisateur final.

### 0.2 DOMAIN_CORE / PLATFORM_CAPABILITY / CORE_EXTENSIBLE / VERTICAL_* — correction de `02` §2

`02` §2 classe « Sécurité / auth / multi-tenant / rôles » et « Transcription
vocale » en `CORE`, au même rang que Client, Devis, Facture — **c'est une
confusion entre objet métier et service technique transversal**, explicitement
signalée comme risque par la présente mission. Correction, sans modifier `02` :

| Catégorie | Définition | Exemples reclassés depuis `02` |
|---|---|---|
| `DOMAIN_CORE` | objet métier au comportement identique partout | Client, Lieu, Devis, Facture, Avoir, Paiement (le concept), Planning/RDV, Personnel (le concept RH) |
| `PLATFORM_CAPABILITY` | service technique transversal, n'appartient à aucun objet métier | Auth, isolation RLS/multi-tenant, Storage, moteur LLM, moteur de transcription vocale, moteur OCR, moteur vision, connecteur PDP, connecteur signature électronique, connecteur paiement |
| `CORE_EXTENSIBLE` | objet/moteur métier commun dont le **contenu** varie par pack | Catalogue/Article, Stock, Rapports/pilotage, CRM/pipeline, mécanisme d'attachement Document/Photo, moteur Visite/Relevé |
| `VERTICAL_*` | inchangé, voir `02` | catalogues fabricants, formulaires conditionnels, règles de calcul, conformité réglementaire métier |

Conséquence directe : une règle métier comme « un devis peut nécessiter une
signature pour être considéré accepté » reste `DOMAIN_CORE` (elle vit dans
l'objet Devis) ; le **connecteur** vers un fournisseur de signature électronique
est `PLATFORM_CAPABILITY` (il peut être changé sans toucher au modèle Devis). Même
logique pour la facturation électronique : l'obligation légale de transmission
est une règle `DOMAIN_CORE` attachée à Facture ; le connecteur PDP est
`PLATFORM_CAPABILITY`.

### 0.3 Chantier ≠ Intervention — correction de `02` §2 et `03` §1

`02` et `03` fusionnent Chantier et Intervention dans une seule ligne/fiche. **Ce
n'est pas neutre** : `0007` O4 et `SUPORDO-CONTRAT-FONCTIONNEL-DEVIS-V0.md` §21
documentent que **Vertuoza n'a aucune transformation directe devis→facture — seules
les voies chantier et intervention y mènent**, ce qui n'a de sens que si ce sont
deux objets distincts avec des rôles différents. Par ailleurs, `03` §4 point 4
traite déjà « le sens devis ↔ intervention » comme une question `OPEN` séparée du
lien devis→chantier (`STRUCTURAL` chez les spécialistes BTP) — la fusion en une
seule fiche a masqué que ce sont deux relations distinctes à trancher
séparément, pas une seule.

**Nuance supplémentaire** : le corpus lui-même emploie ces deux mots de façon
inconsistante selon l'éditeur (« chantier » chez les spécialistes BTP orientés
exécution longue, « intervention » chez les éditeurs orientés service ponctuel) —
la fusion dans `03` n'est donc pas seulement une erreur de synthèse, elle a
recopié une ambiguïté réelle du marché sans la signaler comme telle.

**Nouvelle question ouverte, à ajouter au registre `09` sans le modifier (portée
ici)** :

> **Q18** — Chantier et Intervention sont-ils deux objets distincts dans SUPORDO,
> et si oui, quelle est leur relation (une Intervention appartient-elle à un
> Chantier ? existent-ils indépendamment ? un Chantier peut-il contenir plusieurs
> Interventions ?) — Source : absence de traitement direct dans `03`, contraste
> Vertuoza (exclusif via ces deux voies) vs InterFast (Intervention avec son
> propre cycle et son propre lien conditionnel au devis, `03` fiche Chantier/
> Intervention). Aucune réponse de marché majoritaire. **Urgence :
> `STRUCTURAL_BEFORE_SCHEMA`** pour toute tranche touchant l'un des deux objets
> au-delà du lien direct avec le devis.

**Conséquence pour la séquence de construction** : la tranche T6 ci-dessous
(`Devis → Chantier`) est scopée **strictement à Chantier**, exactement comme
`SUPORDO-CONTRAT-FONCTIONNEL-DEVIS-V0.md` §21 la définit déjà — elle ne
présuppose aucune fusion avec Intervention. Une tranche « Intervention » n'est
**pas** conçue dans ce document : elle reste bloquée par Q18 et par Q8 (`09`,
sens devis↔intervention) et par Q14 (généralisation de la cascade maintenance/
parc installé) — voir §3 « Ce qui reste hors séquence ».

### 0.4 Relevé métier : quatre niveaux distincts, à ne pas confondre

`05-AI-AND-AUTOMATION-BLUEPRINT.md` et `07` §1 (pack métier V1) restent ambigus
sur ce qu'est exactement le « relevé terrain » en V1. Clarification à appliquer
dans toute tranche :

1. **Relevé structuré minimal** — formulaire fixe, champs statiques par pack,
   saisie manuelle, aucune IA. C'est le périmètre exact de T8 tel que défini par
   `SUPORDO-CONTRAT-FONCTIONNEL-DEVIS-V0.md` §21 (« pas de génération automatique
   de lignes en V0 », « validation humaine systématique »).
2. **Formulaire conditionnel avancé** — logique de branchement selon les réponses
   (`VERTICAL_WORKFLOW`) — hors V1, complexité `MOYENNE-FORTE` non justifiée avant
   un premier retour terrain sur le niveau 1.
3. **OCR** (lecture de plaque signalétique/document) — `05` opportunité #2,
   `PLATFORM_CAPABILITY` (moteur) + `VERTICAL_DATA` (champs attendus) — V2.
4. **Extraction IA avancée / structuration voix→lignes de devis** — `05`
   opportunité #1, le précédent OpenFire Zendesk (« Vital Études ») relève de ce
   niveau, **pas** du niveau 1. Sa présence dans `04`/`05` ne doit pas laisser
   croire que T8 la construit dès V1 — c'est une tranche V2 distincte
   (`T8-VOIX`, voir §4).

### 0.5 Q3 — ne pas confondre changement d'état et verrou de mutabilité (correction de `09` Q3)

`09-DECISIONS-RISKS-ANTIGRAVITY-HANDOFF.md` Q3 recommandait de « verrouiller à la
première sortie structurante (M10) » — **c'est une erreur de raisonnement,
corrigée ici sans modifier `09`**. M10 (0007) documente **quand l'état du devis
change** (7/8, l'invariant le mieux prouvé du cycle) ; O3 documente **quand le
contenu devient non modifiable** (5 modèles, aucun dominant, `OPEN`). Le corpus
lui-même prouve que ce sont deux événements distincts : M5 (0007) établit que
« l'envoi ne verrouille rien » chez 3 éditeurs explicites, alors que l'envoi est
très probablement la première « sortie structurante » qui ferait changer l'état
d'un devis brouillon. **Un devis peut donc changer d'état sans devenir
verrouillé.** `SUPORDO-CONTRAT-FONCTIONNEL-DEVIS-V0.md` le modélise correctement
(§21, T2 : « passage BROUILLON → FINALISÉ ... sans verrouillage de contenu à ce
stade » ; T3 : « verrouillage métier du contenu » seulement à l'engagement) — la
séquence T1-T8 ci-dessous suit **cette** version, pas la reformulation erronée de
`09`. Q3 (verrou de mutabilité) reste `OPEN` et distincte de M10 (changement
d'état, `ACQUIS DOCUMENTAIRE`).

### 0.6 Q4 — correction du fondement de la recommandation « transformation directe »

`09` Q4 justifiait la recommandation « transformation directe » par « l'absence
de preuve d'un pivot » — **c'est factuellement inexact**, vérifié en retournant à
`SUPORDO-CONTRAT-FONCTIONNEL-DEVIS-V0.md` §17 : la relation devis→facture connaît
**trois architectures documentées**, pas une majorité écrasante et une absence :
**transformation directe (4/8 : InterFast, Obat, Costructor, Sellsy)**, **objet
pivot obligatoire (3/8 : Axonaut, OpenFire×2)**, **passage exclusif par un objet
tiers (1/8 : Vertuoza, ni direct ni pivot — uniquement via chantier/
intervention)**. L'objet pivot **est documenté**, pas absent — c'est une
`VARIANTE DE MARCHÉ` réelle à 3/8, pas un silence. La recommandation
« transformation directe » reste défendable, mais **pour une autre raison**,
celle que `SUPORDO-CONTRAT-FONCTIONNEL-DEVIS-V0.md` §17 donne réellement :
plurality relative (4/8, pas une majorité absolue), modèle le plus direct pour un
utilisateur solo, n'impose pas un objet « commande » non universel. Toute tranche
ci-dessous qui s'appuie sur ce choix (T4) doit citer cette justification exacte,
pas celle de `09`.

### 0.7 CRM démarre-t-il au Client/Devis, ou faut-il un objet Demande/Lead ?

`04-JOURNEYS-UX-BLUEPRINT.md` parcours C constate un « trou total sur la capture
de la demande elle-même ». Ce blueprint ne tranche pas cette question par
invention. **Nouvelle question ouverte, portée ici, à intégrer au registre `09`
sans le modifier** :

> **Q19** — SUPORDO a-t-il besoin d'un objet léger Demande/Lead/Qualification en
> amont du Client et du Devis, ou le cycle démarre-t-il toujours directement au
> Client ? Aucune preuve corpus dans un sens ou dans l'autre (angle mort complet,
> `04` §1 parcours C). **Urgence : `CAN_WAIT_V2`** — aucune tranche V1 ci-dessous
> n'en dépend (T1 démarre directement au Client, cohérent avec M1 8/8), mais la
> décision doit être prise avant de construire un module CRM/pipeline (`07` V2).

### 0.8 Catalogue : donnée privée au tenant vs référentiel partagé

`08-BACKEND-AND-NONFUNCTIONAL-CONTRACT.md` ne distingue pas, pour l'objet
Catalogue/Article, ce qui est **privé à un tenant** (son propre prix, ses propres
marges, ses lignes personnalisées) de ce qui pourrait être un **référentiel
partagé entre tenants** (marques/fabricants, caractéristiques techniques
publiques d'un produit standard). Le corpus ne permet pas de trancher ce point
(`06` §3 confirme qu'aucun marché de catalogue fabricant mature n'existe pour en
déduire une architecture). **Contrainte de conception à ajouter, sans modifier
`08`** : le modèle de données du Catalogue ne doit pas imposer un `tenant_id`
systématique sur chaque ligne dès la conception — un référentiel de marques/
caractéristiques techniques partagé entre tenants (même s'il n'est peuplé que
pour un seul tenant en V1 pilote) doit rester représentable sans dupliquer les
données par tenant. Ce point s'applique directement à `T-PACK-CLIM` ci-dessous.

### 0.9 Autres contradictions repérées en cours de réconciliation

- `07-V1-V2-V3-80-20.md` §1 core minimum liste « Devis (naissance + un modèle de
  verrouillage) » comme une seule ligne — après 0.5 ci-dessus, il faut lire cela
  comme deux tranches distinctes (changement d'état = T1/T2, verrou = T3), pas
  une seule décision ni une seule tranche.
- `01-CAPABILITY-MAP.md` §7 (analyse 80/20) qualifie la « Complexité » de
  l'objet Visite/relevé terrain de `FORTE` en bloc — après 0.4 ci-dessus, cette
  complexité ne s'applique qu'aux niveaux 2-4 (formulaire conditionnel, OCR, IA) ;
  le niveau 1 (relevé structuré minimal, T8) est de complexité `FAIBLE-MOYENNE`,
  cohérent avec sa position en V1.

---

## 1. Principe de tranche

Une tranche produit une **capacité utilisateur de bout en bout** (frontend +
backend + sécurité + données réelles), pas un module technique isolé. Chaque
tranche doit rester assez petite pour être comprise, planifiée, construite,
testée et auditée séparément — suit le protocole `OBSERVE → PLAN → APPROBATION
HUMAINE → IMPLEMENT → VERIFY → AUDIT INDÉPENDANT → TEST HUMAIN → MERGE` défini
en `14-ANTIGRAVITY-OPERATING-PACK.md`.

## 2. Séquence V1 — fondations + boucle devis/facture + premier pack métier

Ordre de dépendance : `T0 → T1 → T-PACK-CLIM → T2 → T3 → T4 → T5 → T6` et `T8`
(peut démarrer après T1, mais son contenu réel dépend de `T-PACK-CLIM`).

### T0 — Fondations plateforme (multi-tenant, auth, RLS)

- **JOB UTILISATEUR** : aucun (prérequis invisible) — sans cette tranche, aucune donnée n'est en sécurité.
- **VALEUR PRODUITE** : un tenant peut être créé, un utilisateur peut s'authentifier, et aucune donnée d'un tenant n'est visible par un autre. C'est la seule tranche de cette séquence qui n'est pas une "capacité utilisateur" au sens strict — elle est la condition d'existence de toutes les autres (mission §7 tolère cette exception, gate obligatoire).
- **SCOPE** : création de tenant, authentification basique (incluant un flux de réinitialisation de mot de passe self-service standard — `11` P13, contre-exemple Vertuoza à ne jamais reproduire), un rôle unique (propriétaire), RLS activée sur un schéma de test minimal (une table factice suffit à prouver l'isolation).
- **OUT OF SCOPE** : rôles multiples, invitation d'utilisateurs, personnel vs compte utilisateur (`09` Q10, `CAN_WAIT_V2`).
- **OBJETS** : Tenant (`PLATFORM_CAPABILITY`), Utilisateur (`DOMAIN_CORE`, modèle simple V1 selon `07`).
- **DÉPENDANCES** : aucune.
- **DÉCISIONS PO NÉCESSAIRES** : aucune bloquante — modèle de rôle minimal déjà couvert par `RECOMMANDATION ANALYTIQUE` `07`/`08`.
- **BACKEND** : Auth (`PLATFORM_CAPABILITY`), politiques RLS par tenant (`08` §1).
- **FRONTEND** : écran de création de compte/tenant, écran de connexion.
- **RLS / PERMISSIONS** : isolation stricte tenant — c'est l'objet même de la tranche.
- **STORAGE** : aucun.
- **INTÉGRATIONS** : aucune.
- **IA** : aucune.
- **PROVENANCE** : sans objet.
- **ÉTATS/TRANSITIONS** : Tenant créé → actif. Utilisateur créé → authentifié.
- **CAS LIMITES** : tentative de lecture croisée entre deux tenants ; tentative de création de tenant en double ; session expirée.
- **RISQUES** : R9 (`09`) — RLS non posée correctement dès cette tranche compromet tout le reste.
- **DEFINITION OF DONE** : un deuxième tenant créé en test ne peut lire aucune donnée du premier, vérifié par un test automatisé, pas par lecture de code.
- **CRITÈRES D'ACCEPTATION** : voir `13-ACCEPTANCE-NEGATIVE-TEST-MATRIX.md` §T0.
- **TESTS NÉGATIFS** : tenant A lit tenant B → refus systématique, y compris via une requête directe contournant l'UI.
- **PREUVES QUE L'AGENT DEVRA FOURNIR** : test automatisé d'isolation cross-tenant exécuté et son résultat ; capture de la politique RLS effective (pas seulement son intention déclarée dans le code).
- **TEST HUMAIN** : un humain crée deux comptes, vérifie manuellement qu'aucune donnée ne fuit entre eux.
- **CONDITION POUR OUVRIR LA TRANCHE SUIVANTE** : DoD atteint et audit indépendant (`14`) confirmant l'isolation.

### T1 — Création rapide d'un devis (`SUPORDO-CONTRAT-FONCTIONNEL-DEVIS-V0.md` §21)

- **JOB UTILISATEUR** : chiffrer une demande client sans préparation préalable.
- **VALEUR PRODUITE** : premier devis brouillon réel, persisté, éditable.
- **SCOPE** : création autonome d'un devis ; client sélectionnable ou créable à la volée (M1, 8/8) ; lignes depuis un catalogue minimal ou en texte libre (`OPEN` Q1 — décision PO nécessaire, voir ci-dessous) ; sauvegarde en `BROUILLON` sans effet d'état fort.
- **OUT OF SCOPE** : finalisation, numérotation, envoi (T2), tout mécanisme IA (T8-VOIX).
- **OBJETS** : Devis (`DOMAIN_CORE`, état `BROUILLON`), Client (`DOMAIN_CORE`), Catalogue (`CORE_EXTENSIBLE`, contenu minimal ou stub à ce stade).
- **DÉPENDANCES** : T0.
- **DÉCISIONS PO NÉCESSAIRES** : **Q1 (`09`, `BLOCKS_V1`)** — ligne libre hors catalogue autorisée ou non dès cette tranche.
- **BACKEND** : création Devis/Client, pas de contrainte de verrouillage à ce stade.
- **FRONTEND** : écran de création de devis, sélection/création client inline, ajout de ligne.
- **RLS/PERMISSIONS** : héritées de T0, aucune règle additionnelle.
- **STORAGE** : aucun (pas encore de document PDF).
- **INTÉGRATIONS** : aucune.
- **IA** : aucune.
- **PROVENANCE** : sans objet (aucune donnée IA/importée à ce stade).
- **ÉTATS/TRANSITIONS** : (création) → `BROUILLON`.
- **CAS LIMITES** : devis sans aucune ligne ; client supprimé pendant l'édition du devis ; deux lignes catalogue identiques.
- **RISQUES** : sur-construire le catalogue avant le pack métier (R8, `09`) — le catalogue de T1 doit rester un moteur nu, le contenu vertical arrive en `T-PACK-CLIM`.
- **DEFINITION OF DONE** : un devis brouillon complet est créé, persisté, réaffiché après rechargement, avec client et au moins une ligne.
- **CRITÈRES D'ACCEPTATION / TESTS NÉGATIFS** : voir `13` §T1.
- **PREUVES QUE L'AGENT DEVRA FOURNIR** : capture d'écran du devis créé et rechargé ; test automatisé de persistance.
- **TEST HUMAIN** : un humain crée un devis de bout en bout sans documentation, chronomètre le temps, note toute confusion.
- **CONDITION POUR OUVRIR LA TRANCHE SUIVANTE** : DoD atteint, Q1 tranchée par le PO.

### T-PACK-CLIM — Contenu du premier pack métier (climatisation/PAC/chauffage)

- **JOB UTILISATEUR** : disposer d'un catalogue et d'un relevé pertinents pour le métier réel de l'artisan, pas un CRM générique.
- **VALEUR PRODUITE** : première preuve concrète, dans le produit, que l'abstraction CORE+PACKS fonctionne (`02`, sous réserve de 0.1 ci-dessus — preuve technique, pas preuve de marché).
- **SCOPE** : schéma de caractéristiques techniques typé (marque, puissance, SCOP/SEER, type de fluide) ; catalogue saisi/importé manuellement, **pas synchronisé temps réel** (`06` §3) ; schéma de relevé structuré minimal (bilan thermique sommaire, emplacement unité extérieure, alimentation électrique disponible — champs fixes, pas de logique conditionnelle, cf. 0.4 niveau 1).
- **OUT OF SCOPE** : formulaire conditionnel avancé, OCR, deuxième pack métier (fumisterie, V2).
- **OBJETS** : Catalogue/Article (`CORE_EXTENSIBLE`, contenu vertical), schéma de Relevé (`CORE_EXTENSIBLE`, contenu vertical `VERTICAL_CAPTURE`).
- **DÉPENDANCES** : T1 (moteur catalogue nu doit exister).
- **DÉCISIONS PO NÉCESSAIRES** : **Q7 (`09`, `BLOCKS_V1`)** — confirmation de la verticale de lancement (`RECOMMANDATION ANALYTIQUE` : climatisation/PAC/chauffage, le PO cite pourtant la fumisterie en premier exemple, voir `07` §0 — **nuance apportée par `10` §0.1** : OpenFire Odoo documente en réalité un catalogue fumisterie réel avec connecteurs fabricants nommés, l'écart de preuve entre les deux verticales est donc moins large qu'affirmé initialement, sans renverser la recommandation) ; **Q9 (`09`, `BLOCKS_A_SLICE`)** — jusqu'où déclarer la conformité réglementaire (déclaratif seulement en V1).
- **BACKEND** : schéma de caractéristiques technique extensible (0.8 ci-dessus — pas de `tenant_id` systématique sur un futur référentiel de marques partagé).
- **FRONTEND** : écran de gestion de catalogue avec champs techniques typés ; formulaire de relevé à champs fixes.
- **RLS/PERMISSIONS** : catalogue privé au tenant par défaut ; concevoir le modèle pour ne pas empêcher un référentiel partagé plus tard (0.8).
- **STORAGE** : aucun à ce stade (pas encore de photo, voir T8).
- **INTÉGRATIONS** : aucune (§0.8, `06` §3 — pas d'API catalogue fabricant en V1).
- **IA** : aucune.
- **PROVENANCE** : sans objet.
- **ÉTATS/TRANSITIONS** : sans objet (données de configuration, pas un objet à cycle de vie).
- **CAS LIMITES** : caractéristique technique manquante sur un article ; unité de mesure incohérente (kW vs BTU) — aucune preuve corpus sur la validation attendue, à concevoir prudemment.
- **RISQUES** : R1 (`09`) — sur-généraliser le schéma de pack depuis la seule verticale documentée ; concevoir le schéma assez nu pour rester réutilisable par un second pack (fumisterie, V2) sans réécriture.
- **DEFINITION OF DONE** : un catalogue climatisation/PAC réel est saisi et utilisable dans un devis (T1) ; un relevé de visite climatisation/PAC peut être rempli et rattaché à un client/lieu.
- **CRITÈRES D'ACCEPTATION / TESTS NÉGATIFS** : voir `13` §T-PACK-CLIM.
- **PREUVES QUE L'AGENT DEVRA FOURNIR** : capture du catalogue rempli avec au moins 5 articles réalistes ; capture du formulaire de relevé rempli.
- **TEST HUMAIN** : si possible, faire remplir le relevé par une personne non-développeuse pour juger la clarté des champs (À TESTER TERRAIN, `04`).
- **CONDITION POUR OUVRIR LA TRANCHE SUIVANTE** : DoD atteint, Q7 et Q9 tranchées.

### T2 — Finalisation et envoi

- **JOB UTILISATEUR** : transmettre un devis chiffré au client.
- **VALEUR PRODUITE** : un devis numéroté et envoyé, encore modifiable (0.5 ci-dessus).
- **SCOPE** : passage `BROUILLON → FINALISÉ` (numérotation, client devient requis) puis `→ ENVOYÉ` (envoi par email — `06` §1). **Aucun verrouillage de contenu à cette étape** (0.5, M5 : 3 éditeurs confirment que l'envoi ne verrouille rien).
- **OUT OF SCOPE** : verrou de mutabilité (T3), signature (T3).
- **OBJETS** : Devis (`DOMAIN_CORE`).
- **DÉPENDANCES** : T1.
- **DÉCISIONS PO NÉCESSAIRES** : **Q6 (`09`, `BLOCKS_A_SLICE`)** — minimum de contenu pour finaliser (`RECOMMANDATION ANALYTIQUE` : bloquer à 0 € uniquement, seul signal du corpus, Vertuoza).
- **BACKEND** : génération de numéro (séquentiel, cohérent avec le futur régime facture L3 même si le devis lui-même n'a pas de contrainte légale — 0007 §V le rappelle) ; envoi email transactionnel.
- **FRONTEND** : bouton "Finaliser", bouton "Envoyer", statut visible.
- **RLS/PERMISSIONS** : inchangé.
- **STORAGE** : génération d'un PDF du devis (Supabase Storage).
- **INTÉGRATIONS** : email transactionnel (`06` §1, `PLATFORM_CAPABILITY`).
- **IA** : aucune.
- **PROVENANCE** : sans objet.
- **ÉTATS/TRANSITIONS** : `BROUILLON → FINALISÉ → ENVOYÉ`.
- **CAS LIMITES** : devis vide finalisé (Q6) ; échec d'envoi email ; client sans email renseigné.
- **RISQUES** : présenter le PDF généré comme "envoyé avec succès" sans confirmation réelle du fournisseur email (R5/R10, discipline REAL/PROTOTYPE, `14`).
- **DEFINITION OF DONE** : un devis finalisé est numéroté de façon séquentielle et reste éditable ; un email contenant le PDF est effectivement reçu en test.
- **CRITÈRES D'ACCEPTATION / TESTS NÉGATIFS** : voir `13` §T2.
- **PREUVES QUE L'AGENT DEVRA FOURNIR** : email de test reçu (capture) ; test automatisé prouvant qu'un devis `ENVOYÉ` reste éditable (contre-preuve explicite de non-verrouillage).
- **TEST HUMAIN** : un humain finalise et envoie un devis à sa propre adresse, vérifie la réception et le contenu du PDF.
- **CONDITION POUR OUVRIR LA TRANCHE SUIVANTE** : DoD atteint, Q6 tranchée.

### T3 — Engagement du client

- **JOB UTILISATEUR** : faire accepter ou signer le devis par le client.
- **VALEUR PRODUITE** : un devis engagé, verrouillé, avec un chemin de retour documenté.
- **SCOPE** : passage `ENVOYÉ → ACCEPTÉ/SIGNÉ` ; **verrouillage métier du contenu à cette étape précisément** (0.5 — c'est ici, pas à T2, que le verrou de mutabilité s'applique) ; recovery nommé disponible en cas d'erreur.
- **OUT OF SCOPE** : signature électronique tierce réelle en V1 minimal (peut rester une case à cocher manuelle — voir décision Q2 ci-dessous) ; transformation en facture (T4).
- **OBJETS** : Devis (`DOMAIN_CORE`).
- **DÉPENDANCES** : T2.
- **DÉCISIONS PO NÉCESSAIRES** : **Q2 (`09`, `BLOCKS_V1`)** — signature = acceptation ou deux événements ; **Q3 (`09`, `BLOCKS_V1`, corrigée en 0.5)** — où exactement place-t-on le verrou de mutabilité, **indépendamment** de la question du changement d'état déjà réglée par M10/T2.
- **BACKEND** : contrainte d'immutabilité du contenu posée au niveau backend (`08` §6 — jamais seulement côté frontend), pas seulement un statut affiché.
- **FRONTEND** : action "Accepter"/"Signer" côté client (portail client minimal ou action manuelle côté artisan si pas de portail en V1) ; affichage clair de l'état verrouillé ; action de recovery visible (ex. dupliquer pour corriger, jamais réécrire).
- **RLS/PERMISSIONS** : si un portail client existe, accès en lecture seule scoping strict au devis concerné.
- **STORAGE** : PDF signé/accepté conservé (snapshot, cohérent avec `03` mode "snapshotté" documenté pour les pièces jointes).
- **INTÉGRATIONS** : signature électronique réelle **si** Q2 l'exige — sinon `PLATFORM_CAPABILITY` non activée en V1, à ne jamais présenter comme active si elle ne l'est pas (`14`).
- **IA** : aucune.
- **PROVENANCE** : sans objet pour cette tranche (pas de donnée IA en jeu).
- **ÉTATS/TRANSITIONS** : `ENVOYÉ → ACCEPTÉ/SIGNÉ` (verrou de contenu activé à cette transition).
- **CAS LIMITES** : tentative de modification après verrouillage (doit échouer côté backend, pas seulement être masquée côté UI) ; double acceptation ; recovery demandé sur un devis déjà transformé en facture (dépend de T4, à anticiper — le mécanisme d'annulation d'engagement de `P2` doit explicitement refuser ce cas). Suivre le modèle Obat « variantes de devis » (`10` §2 M2, `11` P2 — annulation de signature sans renommage ni casse des références) plutôt que l'ancien mécanisme Vertuoza (retiré du produit car il supprimait tout le chantier lié).
- **RISQUES** : R3 (`09`) — si le verrou n'est pas réellement posé au niveau backend, toute la chaîne d'irréversibilité en aval (facture, L1) est compromise.
- **DEFINITION OF DONE** : un devis accepté est réellement non modifiable (testé par une tentative directe, pas seulement par l'absence de bouton) ; un chemin de recovery existe et a été testé.
- **CRITÈRES D'ACCEPTATION / TESTS NÉGATIFS** : voir `13` §T3.
- **PREUVES QUE L'AGENT DEVRA FOURNIR** : test automatisé de tentative de modification post-verrouillage échouant explicitement (pas silencieusement) ; capture du chemin de recovery.
- **TEST HUMAIN** : un humain tente de modifier un devis verrouillé et vérifie que le refus est clair, pas une erreur technique brute.
- **CONDITION POUR OUVRIR LA TRANCHE SUIVANTE** : DoD atteint, Q2 et Q3 tranchées séparément.

### T4 — Devis → Facture directe

- **JOB UTILISATEUR** : facturer un devis accepté.
- **VALEUR PRODUITE** : première facture réelle du système, traçable jusqu'au devis d'origine.
- **SCOPE** : transformation directe (0.6 ci-dessus — justification correcte : plurality 4/8, pas absence de pivot) ; lignes/client/montants copiés ; devis original conservé et référencé, reste consultable (INV-3C-2).
- **OUT OF SCOPE** : objet pivot ou passage exclusif par un tiers (options écartées pour V1, voir 0.6) ; acompte/solde (T5).
- **OBJETS** : Devis (`DOMAIN_CORE`), Facture (`DOMAIN_CORE`).
- **DÉPENDANCES** : T3 (devis Accepté/Signé requis).
- **DÉCISIONS PO NÉCESSAIRES** : **Q4 (`09`, `STRUCTURAL_BEFORE_SCHEMA`, justification corrigée en 0.6)** — confirmer transformation directe.
- **BACKEND** : contrainte d'immutabilité de la facture posée **au niveau base de données** dès sa numérotation (`08` §5, L1/0007) — aucune route d'écriture ne doit l'accepter après.
- **FRONTEND** : bouton "Facturer" sur un devis accepté ; affichage du lien devis↔facture dans les deux sens.
- **RLS/PERMISSIONS** : inchangé.
- **STORAGE** : PDF facture généré, snapshotté.
- **INTÉGRATIONS** : interface abstraite vers un PDP de facturation électronique posée dès cette tranche (`06` §2, `08` §14) — **branchement réel non requis en V1**, mais l'abstraction doit exister pour éviter le risque R4.
- **IA** : aucune.
- **PROVENANCE** : sans objet.
- **ÉTATS/TRANSITIONS** : Devis `ACCEPTÉ/SIGNÉ` → Facture `BROUILLON` → Facture `NUMÉROTÉE` (irréversible dès cet instant).
- **CAS LIMITES** : tentative de facturer un devis non accepté (doit être refusée) ; tentative de re-facturer un devis déjà facturé (cohérent avec M7 : 1→N documenté, mais jamais 1→1 implicite — clarifier si une seconde facture est un nouveau document distinct ou une erreur) ; tentative de modifier une facture déjà numérotée par un chemin détourné — le contre-exemple à ne jamais reproduire est Vertuoza (`10` §2 M1, `11` P9) où le support recommandait d'éditer le PDF via un outil externe faute de mécanisme de correction adapté : SUPORDO doit refuser cette issue au niveau produit, pas la documenter comme solution.
- **RISQUES** : R3 (`09`) — le trou documentaire le plus important du corpus (mode exact copié/référencé) rend cette tranche la plus sensible de toute la séquence V1.
- **DEFINITION OF DONE** : une facture numérotée est générée depuis un devis accepté, immuable dès sa création (testé), et reste liée au devis d'origine consultable.
- **CRITÈRES D'ACCEPTATION / TESTS NÉGATIFS** : voir `13` §T4.
- **PREUVES QUE L'AGENT DEVRA FOURNIR** : test automatisé de tentative de modification d'une facture numérotée échouant systématiquement, y compris par un chemin d'accès direct à la base ; capture du lien bidirectionnel devis↔facture.
- **TEST HUMAIN** : un humain tente, via l'interface ET via un outil d'administration de la base si possible, de modifier une facture numérotée.
- **CONDITION POUR OUVRIR LA TRANCHE SUIVANTE** : DoD atteint, Q4 tranchée, invariant L1 testé et audité indépendamment (`14`).

### T5 — Acompte puis solde

- **JOB UTILISATEUR** : demander un acompte avant travaux, puis facturer le solde.
- **VALEUR PRODUITE** : facture de solde correcte sans ressaisie manuelle du montant déjà encaissé — le mécanisme le mieux corroboré de tout le corpus (INV-3C-1/INV-5, 4-6/8 éditeurs indépendants).
- **SCOPE** : paramètre d'acompte défini sur le devis ; facture d'acompte distincte générée ; déduction **recalculée**, jamais ressaisie, à la facturation du solde.
- **OUT OF SCOPE** : cascade de situations multiples (BTP avancé, V2) — un seul régime actif en V1 (acompte simple XOR situations, jamais les deux).
- **OBJETS** : Devis, Facture d'acompte, Facture de solde (tous `DOMAIN_CORE`).
- **DÉPENDANCES** : T4.
- **DÉCISIONS PO NÉCESSAIRES** : aucune bloquante — mécanisme le mieux prouvé du corpus, `RECOMMANDATION ANALYTIQUE` directement actionnable.
- **BACKEND** : le montant déjà facturé doit être un calcul dérivé (`08` §6), jamais un champ librement éditable.
- **FRONTEND** : paramétrage du taux/montant d'acompte sur le devis ; génération de la facture de solde avec déduction visible et non modifiable manuellement.
- **RLS/PERMISSIONS** : inchangé.
- **STORAGE** : PDF des deux factures.
- **INTÉGRATIONS** : aucune nouvelle (paiement en ligne différé V2, `07`).
- **IA** : aucune.
- **PROVENANCE** : sans objet.
- **ÉTATS/TRANSITIONS** : Facture d'acompte `NUMÉROTÉE` → Facture de solde calculée en tenant compte de l'acompte.
- **CAS LIMITES** : acompte supérieur au montant total ; tentative de modifier manuellement le montant déduit sur la facture de solde (doit échouer) ; annulation d'un acompte déjà facturé (renvoie vers Avoir, hors scope V1 minimal si non couvert).
- **RISQUES** : confondre "recalculé" et "éditable avec valeur par défaut" — le corpus est explicite : jamais ressaisi, donc jamais éditable non plus.
- **DEFINITION OF DONE** : une facture de solde générée déduit automatiquement l'acompte déjà facturé, valeur non modifiable manuellement, testé.
- **CRITÈRES D'ACCEPTATION / TESTS NÉGATIFS** : voir `13` §T5.
- **PREUVES QUE L'AGENT DEVRA FOURNIR** : test automatisé du calcul de déduction sur plusieurs scénarios (acompte partiel, acompte égal au total).
- **TEST HUMAIN** : un humain configure un acompte, facture, puis facture le solde et vérifie le montant sans calcul manuel.
- **CONDITION POUR OUVRIR LA TRANCHE SUIVANTE** : DoD atteint.

### T6 — Devis → Chantier (scope strictement Chantier, pas Intervention — voir 0.3)

- **JOB UTILISATEUR** : suivre l'exécution d'un devis accepté sans ressaisie.
- **VALEUR PRODUITE** : un chantier créé et lié à son devis d'origine, hub de recalcul de rentabilité (`03`, INV-4).
- **SCOPE** : création ou liaison du chantier **depuis** un devis engagé ; chantier jamais un préalable au devis (S2) ; référence explicite conservée dans les deux sens.
- **OUT OF SCOPE** : objet Intervention (bloqué par Q18/Q8/Q14, voir 0.3 et §3 ci-dessous) ; agrégation de dépenses/temps détaillée (peut suivre en V1 ou V2 selon capacité, non structurant pour cette tranche elle-même).
- **OBJETS** : Devis (`DOMAIN_CORE`), Chantier (`CORE_EXTENSIBLE` selon `02`, à confirmer après Q18).
- **DÉPENDANCES** : T3.
- **DÉCISIONS PO NÉCESSAIRES** : aucune bloquante pour ce scope restreint — le lien Devis→Chantier est `STRUCTURAL` documenté (Vertuoza, InterFast, Obat, Costructor) indépendamment de Q18.
- **BACKEND** : rentabilité chantier comme calcul dérivé (`08` §6, INV-4) dès la création, même si peu de données l'alimentent encore.
- **FRONTEND** : bouton "Créer le chantier" depuis un devis accepté ; vue chantier avec lien vers le devis d'origine.
- **RLS/PERMISSIONS** : inchangé.
- **STORAGE** : aucun nouveau.
- **INTÉGRATIONS** : aucune.
- **IA** : aucune.
- **PROVENANCE** : sans objet.
- **ÉTATS/TRANSITIONS** : Devis `ACCEPTÉ/SIGNÉ` → Chantier créé (état "en cours" minimal en V1).
- **CAS LIMITES** : tentative de créer un chantier sans devis (doit rester possible, cohérent avec S2 — le lien n'est établi que si l'utilisateur part du devis) ; deux chantiers pour un même devis (0007 M7 documente 1→N pour le devis en général — vérifier si applicable ici ou si c'est une erreur à bloquer, `NON DÉTERMINÉ`, à traiter avec prudence plutôt qu'à trancher).
- **RISQUES** : R1/R2 (`09`) — c'est l'objet le moins bien outillé du corpus ; ne pas sur-construire au-delà du scope strict ci-dessus.
- **DEFINITION OF DONE** : un chantier est créé depuis un devis accepté, consultable dans les deux sens, avec un calcul de rentabilité dérivé fonctionnel même à vide.
- **CRITÈRES D'ACCEPTATION / TESTS NÉGATIFS** : voir `13` §T6.
- **PREUVES QUE L'AGENT DEVRA FOURNIR** : capture du lien bidirectionnel devis↔chantier.
- **TEST HUMAIN** : un humain crée un chantier depuis un devis et vérifie qu'il retrouve facilement le devis d'origine depuis le chantier.
- **CONDITION POUR OUVRIR LA TRANCHE SUIVANTE** : DoD atteint.

### T8 — Visite/relevé alimentant un devis (niveau 1 uniquement — voir 0.4)

- **JOB UTILISATEUR** : chiffrer un devis à partir d'observations terrain tracées, sans tout ressaisir de mémoire au bureau.
- **VALEUR PRODUITE** : la capacité la plus directement liée à la thèse produit du PO (`05`), construite ici dans sa forme la plus sobre et la mieux prouvée (InterFast, OpenFire Zendesk).
- **SCOPE** : création d'un rapport de visite structuré (champs fixes du pack `T-PACK-CLIM`, photos, notes) ; lien au devis ; **alimentation manuelle** des lignes de devis depuis ce rapport — **aucune génération automatique de lignes en V1** (0.4 niveau 1, conforme à `SUPORDO-CONTRAT-FONCTIONNEL-DEVIS-V0.md` §21).
- **OUT OF SCOPE** : structuration IA, transcription vocale, génération automatique de lignes (`T8-VOIX`, V2, voir §4).
- **OBJETS** : Devis (`DOMAIN_CORE`), Rapport de visite (`CORE_EXTENSIBLE`, contenu vertical via `T-PACK-CLIM`).
- **DÉPENDANCES** : T1, T-PACK-CLIM.
- **DÉCISIONS PO NÉCESSAIRES** : aucune bloquante — scope déjà cadré par V0 elle-même.
- **BACKEND** : persistance du rapport de visite, capture conservée localement en cas de perte de connexion terrain (`08` §13, contrainte mobile) puis synchronisée.
- **FRONTEND** : formulaire de relevé mobile (champs fixes du pack), prise de photo, note libre ; validation humaine systématique avant toute ligne ajoutée au devis.
- **RLS/PERMISSIONS** : inchangé.
- **STORAGE** : photos terrain — régime de consentement média à appliquer si publiables (S5, `08` §4), sinon régime standard.
- **INTÉGRATIONS** : aucune en V1 (pas d'OCR, pas de LLM à ce stade).
- **IA** : aucune en V1 — c'est la tranche la plus tentante à "enrichir" prématurément, à ne pas faire (0.4).
- **PROVENANCE** : sans objet en V1 (aucune donnée IA à tracer) — deviendra pertinent en `T8-VOIX` (S4).
- **ÉTATS/TRANSITIONS** : Rapport de visite créé → consultable, rattaché au devis.
- **CAS LIMITES** : capture interrompue par perte de connexion (le brouillon de relevé ne doit jamais être perdu, `08` §13) ; photo non consentie par erreur marquée publiable.
- **RISQUES** : R6 (`09`) — même sans IA, ne jamais présenter une photo terrain comme une preuve de conformité réglementaire si ce n'est pas son rôle.
- **DEFINITION OF DONE** : un rapport de visite climatisation/PAC est créé sur mobile, survit à une interruption de connexion simulée, et ses données peuvent être copiées manuellement dans un devis.
- **CRITÈRES D'ACCEPTATION / TESTS NÉGATIFS** : voir `13` §T8.
- **PREUVES QUE L'AGENT DEVRA FOURNIR** : test de coupure de connexion pendant la capture, preuve que rien n'est perdu ; capture du relevé rempli et lié au devis.
- **TEST HUMAIN** : test terrain réel recommandé — `04` §1 signale cette zone comme faiblement documentée par le corpus, la preuve de valeur doit venir de l'usage, pas de la documentation.
- **CONDITION POUR OUVRIR LA TRANCHE SUIVANTE** : DoD atteint ; retour terrain récolté avant de construire `T8-VOIX`.

## 3. Ce qui reste explicitement hors séquence V1

- **Objet Intervention** (distinct de Chantier, 0.3) — bloqué par Q18 (nouvelle) et Q8/Q14 (`09`) ; aucune tranche ne le construit avant validation terrain.
- **T7 — Avenant** — `CAN_WAIT_V2` (`07`), scope déjà défini par `SUPORDO-CONTRAT-FONCTIONNEL-DEVIS-V0.md` §21, prêt à être détaillé en V2.
- **Formulaire conditionnel avancé, OCR** (niveaux 2-3 de 0.4) — V2.
- **Deuxième pack métier (fumisterie)** — V2, nécessaire pour valider ou invalider l'abstraction `T-PACK-CLIM` sur un second cas (`02` §4, R1).
- **Paiement en ligne, rapprochement bancaire, branchement réel du PDP** — V2 (`07`), l'abstraction PDP est posée dès T4 mais son branchement réel suit un calendrier légal propre (`06` §2).

## 4. Candidats pour la première tranche réelle Antigravity

**Ne choisit pas à la place du PO.** Trois candidats, avec leurs compromis.

### Candidat 1 — T0 + T1 (fondations + création de devis)

- **Pertinence** : le chemin le plus court vers une preuve technique de bout en bout (auth, RLS, persistance, UI) sans toucher aux questions produit les plus disputées (Q2, Q3, Q4).
- **Teste techniquement** : la chaîne complète frontend/backend/sécurité de base sur Supabase, la discipline REAL/PROTOTYPE d'Antigravity sur un cas simple.
- **Teste produit** : très peu — un devis brouillon seul ne prouve aucune différenciation.
- **Ne teste pas** : l'irréversibilité légale (T4), la thèse voix/terrain (T8), l'abstraction pack métier.
- **Risques** : donne une fausse impression de rapidité si les tranches suivantes (T3, T4) s'avèrent bien plus coûteuses.
- **Décisions bloquantes restantes** : Q1 (ligne libre).

### Candidat 2 — T0 + T-PACK-CLIM + T8 (fondations + pack métier + visite/relevé minimal)

- **Pertinence** : teste en premier ce qui différencie réellement SUPORDO, avant d'investir dans la mécanique commerciale standard.
- **Teste techniquement** : le modèle de données CORE_EXTENSIBLE (catalogue + relevé) et la résilience terrain (capture hors-ligne).
- **Teste produit** : directement la thèse du PO — mais **sans** la partie la plus visible (génération automatique de devis, différée en `T8-VOIX`), donc un test partiel de la thèse, pas complet.
- **Ne teste pas** : le cycle commercial (devis→facture), l'irréversibilité légale.
- **Risques** : périmètre plus large que le candidat 1 (deux tranches de contenu métier en une seule mise en route) ; nécessite Q7 et Q9 tranchées avant de commencer, alors que le candidat 1 n'a besoin que de Q1.
- **Décisions bloquantes restantes** : Q7 (verticale), Q9 (conformité déclarative).

### Candidat 3 — T0 + T1 + T-PACK-CLIM (fondations + devis générique + contenu du premier pack, sans le relevé terrain)

- **Pertinence** : point milieu — prouve que l'abstraction CORE+PACKS fonctionne réellement en code (un pack métier réel branché sur un devis réel), sans encore s'attaquer à la zone la moins documentée du corpus (capture terrain, T8).
- **Teste techniquement** : le mécanisme d'extension du catalogue par pack (0.8), utilisable en conditions réelles dès T1.
- **Teste produit** : partiellement — un devis avec du contenu métier réel, mais sans la démonstration terrain qui est au cœur de la différenciation.
- **Ne teste pas** : la capture terrain, le cycle commercial complet.
- **Risques** : le plus équilibré des trois, mais retarde la preuve de la thèse voix/terrain qui est la plus incertaine et la plus importante à valider tôt.
- **Décisions bloquantes restantes** : Q1, Q7, Q9.
