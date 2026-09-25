# 01 — E-Invoicing Canonical Domain

Contrat de données conceptuel du domaine Facture SUPORDO, capable d'interopérer
avec la facturation électronique française sans lui être couplé. Aucun SQL,
aucun XML généré ici.

## Statuts utilisés

`LEGAL_VERIFIED` (texte réglementaire officiel, lu directement) ·
`OFFICIAL_SPEC` (communication administrative officielle ou spécification
publique, non un texte de loi lui-même) · `IMPLEMENTATION_EXAMPLE` (Evoliz ou
Axonaut — jamais une preuve réglementaire) · `SUPORDO_DECISION` (déjà actée
dans `0007-contraintes-acquises.md`) · `ANALYSIS` (raisonnement de ce document)
· `OPEN` (non résolu par cette recherche, à vérifier avant de figer).

## 0. Ce qui est vérifié à ce jour (23/09/2026) — résumé sourcé

| Point | Statut | Source |
|---|---|---|
| Décret n° 2026-677 du 27/07/2026 remplace « PDP » et « portail public de facturation » par la notion unique de **« plateforme agréée » (PA)** | `LEGAL_VERIFIED` | Légifrance, JORFTEXT000054499487, lu directement |
| Réception électronique obligatoire pour toutes les entreprises assujetties à la TVA établies en France depuis le **01/09/2026** | `OFFICIAL_SPEC` | impots.gouv.fr, page modifiée le 26/05/2026 |
| Émission + e-reporting obligatoires pour grandes entreprises/ETI depuis le **01/09/2026** | `OFFICIAL_SPEC` | idem |
| Émission + e-reporting obligatoires pour PME/TPE/micro-entreprises à partir du **01/09/2027** | `OFFICIAL_SPEC` | idem |
| E-invoicing = B2B domestique assujetti TVA française ; e-reporting = B2C + international (données de transaction) + données de paiement pour opérations à TVA sur encaissement | `OFFICIAL_SPEC` | impots.gouv.fr |
| Formats acceptés : UBL, CII, ou format hybride (Factur-X) | `OFFICIAL_SPEC` | impots.gouv.fr |
| Factur-X, norme EN 16931, version courante **1.09.2 / ZUGFeRD 2.5.2, publiée le 04/08/2026**, 5 profils (MINIMUM, BASIC WL, BASIC, EN 16931, EXTENDED) | `OFFICIAL_SPEC` | FNFE-MPE, fetch direct |
| Une Plateforme Agréée est immatriculée par la DGFiP pour 3 ans renouvelables ; fonctions minimales : émission/transmission, extraction et transmission de données à l'administration, transmission de données de transaction/paiement, conversion de format en préservant intégrité/authenticité | `OFFICIAL_SPEC` | impots.gouv.fr |
| Le PPF (ex-Portail Public de Facturation) conserve un rôle d'**annuaire central** (lancé juin 2025) et de **concentrateur** de données vers l'administration | `OFFICIAL_SPEC` avec **flottement terminologique signalé** entre canaux officiels | AIFE + décret |
| Le **SIREN sert d'identifiant pivot** pour l'annuaire/routage | `OFFICIAL_SPEC`, certitude modérée (non recoupé deux fois) | AIFE, décret |
| Libellés exacts des statuts de cycle de vie réglementaires | **`OPEN`** — base normative identifiée (AFNOR XP Z12-012/013/014) mais liste non obtenue | — |
| Délai/format exact des données de paiement en e-reporting | **`OPEN`** | — |
| Articulation Chorus Pro (B2G) ↔ dispositif B2B | **`OPEN`**, hypothèse seulement | — |
| Mentions obligatoires actuelles sur facture (voir §5.1) | `OFFICIAL_SPEC` | service-public.gouv.fr, page du 11/08/2026, citant Code de commerce L.441-9 et CGI art. 242 nonies A |

**Aucune ligne du tableau ci-dessus n'a été dérivée d'Evoliz ou d'Axonaut** —
toutes proviennent de sources officielles.

**Correction apportée par une mission corrective ultérieure** : une version
antérieure de ce document affirmait « Evoliz n'expose aucune facturation
électronique structurée ». C'était vrai pour **Evoliz v1.43** (recherche
exhaustive, zéro occurrence) mais **faux pour Evoliz v1.56**, un second
snapshot analysé séparément — voir §4bis. Les trois documents API analysés
dans cette annexe sont donc : **Axonaut v2.0.0**, **Evoliz v1.43**, **Evoliz
v1.56**. Axonaut reste, dans sa version consultée, sans aucune fonctionnalité
de facturation électronique. Les trois restent `IMPLEMENTATION_EXAMPLE` sans
exception — jamais une source de vérité réglementaire, y compris pour Evoliz
v1.56 malgré la richesse de son cycle observé.

## 1. Les cinq couches — ne jamais les confondre

### A. SUPORDO DOMAIN
Client, Lieu, Devis, Facture, Avoir, Paiement — déjà définis dans le Product
Blueprint principal (`03-DOMAIN-DEPENDENCIES-LIFECYCLES.md`). Cette annexe ne
les redéfinit pas, elle leur ajoute une capacité de projection.

### B. CANONICAL FINANCIAL DATA
La représentation interne de la Facture SUPORDO, suffisamment riche et stable
pour être projetée vers un format externe — voir §5. Elle vit **dans** l'objet
Facture du domaine (couche A), elle n'est pas un objet séparé.

### C. E-INVOICING PLATFORM CAPABILITY
Routage, projection de format, transmission, statuts, retry, accusés,
provider — voir §7. C'est un service technique transversal, `PLATFORM_CAPABILITY`
au sens de `12-ANTIGRAVITY-BUILD-SEQUENCE.md` §0.2 du blueprint principal — il
ne porte aucune règle métier propre, il exécute des règles définies ailleurs.

### D. ACCOUNTING INTEROP
FEC, journaux, mapping comptable, export, expert-comptable — voir `04`.
Également `PLATFORM_CAPABILITY`/`CORE_EXTENSIBLE` selon le sous-élément, jamais
`DOMAIN_CORE`.

### E. PROVIDER ADAPTER
Evoliz, MyUnisoft, Inqom, Plateforme Agréée A, Plateforme Agréée B, etc. —
implémentations interchangeables de C et D. **Un nom de provider ne doit
jamais apparaître dans une entité de la couche A ou B.** C'est la règle la
plus souvent violée en pratique (voir §7 pour comment l'éviter concrètement).

## 2. Canonical Invoice Contract

Le plus petit modèle métier durable, avant tout schéma SQL. Chaque champ porte
son statut.

### 2.1 Identité et adresses — quatre concepts distincts, jamais fusionnés

| Concept | Définition | Statut | Remarque |
|---|---|---|---|
| **Adresse légale/facturation** (Seller/Buyer) | Adresse fiscale du vendeur et de l'acheteur, portée sur la facture | `OFFICIAL_SPEC` (mention obligatoire) | Toujours présente. |
| **Lieu de prestation** | Où le service a été réellement exécuté (chantier, domicile client) — c'est le **Lieu** SUPORDO (`S1`, `SUPORDO_DECISION`, distinct du Client) | `SUPORDO_DECISION` (S1) + `ANALYSIS` (application au domaine facture) | **Absent du modèle Axonaut** (qui ne distingue que facturation/livraison/devis, `IMPLEMENTATION_EXAMPLE` négatif) — confirme que S1 comble un vrai trou du marché, pas une sur-ingénierie. |
| **Adresse de livraison** | Où un bien matériel a été livré, si distinct | `OFFICIAL_SPEC` (mention obligatoire nouvelle pour grandes entreprises depuis 01/09/2026 si différente de l'adresse de facturation) | Pertinent surtout si SUPORDO vend du matériel en plus de la prestation. |
| **Adresse électronique de routage** | Identifiant technique (SIREN-pivot) permettant à l'annuaire de la Plateforme Agréée d'acheminer l'échange — **ce n'est pas une adresse postale** | `OFFICIAL_SPEC`, certitude modérée | Appartient à la couche C (E-invoicing Platform Capability), pas au domaine Facture lui-même — voir §7. |

**Règle de conception corrigée (`ANALYSIS`)** : ni la référence vivante seule,
ni le snapshot seul ne suffisent — une version antérieure de ce document
tranchait implicitement en faveur de la seule référence, ce qui est
insuffisant. La Facture porte **les deux, à des fins différentes** :

- un **lien métier** vers le Lieu SUPORDO (S1) quand la prestation y a été
  exécutée — permet la navigation, le regroupement, l'historique par lieu ;
- un **snapshot immuable** des données de lieu/adresse telles qu'elles
  étaient au moment de l'émission — seule preuve historique opposable,
  indépendante de toute modification ultérieure du Lieu ou du Client.

Le même raisonnement s'applique aux données Seller/Buyer nécessaires à une
facture émise (§2.2) : un lien vers le Client ne suffit jamais seul, un
snapshot immuable de son identité légale au moment de l'émission est
également nécessaire. **Confirmé par Evoliz v1.56** (`IMPLEMENTATION_EXAMPLE`,
voir §4bis) : le SIREN de l'acheteur interrogé pour résoudre l'adressage
électronique est explicitement **celui historisé à la création du document,
jamais le SIREN courant de la fiche client** — cohérent avec ce que le
Factur-X lui-même embarque une fois généré. Cohérent aussi avec le pattern
positif déjà observé chez Axonaut : `billing_address`/`delivery_address`
copiées en dur dans la facture au moment de l'émission (S3/0007 appliqué par
analogie à l'adresse et à l'identité, pas seulement au prix).

### 2.2 Identifiants d'entreprise

Seller : nom légal, forme juridique + capital si société, **SIREN**, adresse
légale, **numéro de TVA intracommunautaire**. Buyer : nom, **SIREN** (mention
obligatoire nouvelle pour le client des grandes entreprises depuis 01/09/2026),
numéro de TVA intracommunautaire (sauf factures ≤ 150 € HT). `OFFICIAL_SPEC`,
service-public.gouv.fr.

### 2.3 Numérotation, dates, devise

Numéro de facture séquentiel (déjà `LEGAL_CITÉ` L3/0007, appliqué à la Facture
— voir la correction B9 du gate `15-RED-TEAM-GATE.md` du blueprint principal :
ne jamais l'imposer au Devis par analogie). Date d'émission, date de
l'opération (livraison/exécution de la prestation), date d'échéance —
`OFFICIAL_SPEC`. Devise : code ISO 4217, avec montant typé (jamais un nombre
brut sans devise associée) — `ANALYSIS`, cohérent avec le pattern
multi-devises observé chez Axonaut et Evoliz (`IMPLEMENTATION_EXAMPLE`).

### 2.4 Lignes — corrigé après vérification directe d'EN 16931

Description, quantité, unité, prix unitaire HT, remises (ligne et globales,
montant ou pourcentage).

**Correction apportée par une mission corrective ultérieure.** Une version
antérieure de ce document affirmait « un ensemble de taux de TVA par ligne »,
dérivée par analogie du pattern `tax_rates[]` d'Axonaut — exactement l'erreur
de méthode que la discipline de preuve de cette annexe interdit (dériver le
domaine canonique d'une implémentation concurrente plutôt que de la norme).
Vérification directe effectuée (Peppol BIS Billing 3.0, implémentation de
référence d'EN 16931 — `OFFICIAL_SPEC` quasi-primaire ; le texte CEN
lui-même, payant, n'a pas été consulté) :

- **BT-151** (catégorie de TVA) et **BT-152** (taux de TVA) sont portés par
  `ClassifiedTaxCategory` au niveau de la **ligne**, en cardinalité **1..1 /
  0..1** — **une ligne porte exactement un taux de TVA, jamais un
  ensemble.**
- La multiplicité de taux n'existe qu'au niveau **agrégé de la facture**
  (BT-118/BT-119, `TaxSubtotal`, cardinalité 0..n) — c'est une ventilation
  résultant des lignes, pas un attribut d'une ligne individuelle.

**Modèle canonique corrigé** : un traitement TVA (une catégorie + un taux)
applicable par ligne ; plusieurs taux/catégories possibles **entre** les
lignes d'une même facture ; ventilation agrégée au niveau facture (§2.5).

**Conséquence directe pour le cas BTP réel** (prestation mixte main d'œuvre à
10 % + fourniture à 20 %) : ce cas se représente par **au moins deux lignes
distinctes**, chacune avec son propre taux — jamais par une ligne à taux
multiples. C'est une déduction structurelle directe des cardinalités
officielles ci-dessus (`ANALYSIS` de haute confiance ; aucune citation
littérale du cas BTP français précis n'a été trouvée, seulement la règle
générale qui l'implique).

### 2.5 Ventilation de TVA et totaux

Ventilation agrégée par taux (exigée par la norme EN 16931 elle-même,
`OFFICIAL_SPEC`) : net total (HT), total de taxe, total brut (TTC), reste dû
(après déduction des acomptes déjà facturés — mécanisme déjà `ACQUIS
DOCUMENTAIRE` le mieux corroboré du Product Blueprint principal, `03` §1,
invariant acompte/solde). Motifs d'exonération de TVA : à vérifier au BOFiP
avant toute liste figée — Evoliz affirme une table de codes citant des
articles du CGI **avec une anomalie apparente** (code 7 et code 8 citent tous
deux « art. 293 B du CGI », probablement un doublon de documentation) —
`IMPLEMENTATION_EXAMPLE`, **`OPEN`**, ne jamais copier cette table sans
vérification indépendante.

### 2.6 Conditions et moyens de paiement

Conditions de paiement (échéance, mentions de pénalité de retard). L'indemnité
forfaitaire de recouvrement (traditionnellement 40 €) et le taux d'escompte
sont des mentions traditionnellement obligatoires en droit français mais
**non revérifiées par cette recherche** — `OPEN`, à confirmer contre le Code
de commerce (art. L.441-10 et suivants) avant toute implémentation, ne
jamais se fonder sur la présence de ces champs chez Evoliz (`term.nopenalty`,
`term.recovery_indemnity`, `IMPLEMENTATION_EXAMPLE`) comme preuve de la règle
elle-même.

### 2.7 Références croisées

Devis d'origine, commande (numéro de bon de commande si préétabli — mention
obligatoire, `OFFICIAL_SPEC`), contrat, facture précédente (chaîne
acompte→solde ou situation→situation), avoir (lien **bidirectionnel direct**,
`ANALYSIS` — **à ne pas reproduire comme chez Evoliz**, où le schéma `Credit`
ne porte aucune FK explicite vers la facture d'origine et exige un appel
séparé `/links` pour la retrouver, `IMPLEMENTATION_EXAMPLE` négatif).

### 2.8 Rôle du document (déjà largement couvert par la doctrine devis existante)

Un document peut être une facture ordinaire, une facture d'acompte, une
facture de solde — mécanisme déjà `ACQUIS DOCUMENTAIRE` dans le Product
Blueprint principal (T5, `12`). Cette annexe n'y ajoute rien de nouveau,
seulement une confirmation croisée : le triptyque `deposit_type` d'Axonaut
(1=premier acompte, 2=acompte intermédiaire, 3=solde, `IMPLEMENTATION_EXAMPLE`)
et le mode `advance_deduction_mode` d'Evoliz confirment que ce n'est pas une
spécificité SUPORDO mais un besoin de marché reconnu.

### 2.9 Extensions BTP identifiées mais non retenues au niveau canonique minimal

Retenue de garantie, primes post-TVA nommées et plafonnées (type CEE,
MaPrimeRénov'), facturation de situation/avancement — concepts réels et
directement pertinents pour la cible artisan de SUPORDO (`ANALYSIS`, observés
chez Evoliz comme `IMPLEMENTATION_EXAMPLE`), mais **classés `DO_NOT_BUILD_YET`**
— voir `06` §15. Ne pas les intégrer au contrat canonique minimal maintenant :
ce sont des extensions du modèle Facture, pas des prérequis structurels.

### 2.10 Provenance et régime

La Facture porte un discriminant de régime (native SUPORDO vs importée,
`SUPORDO_DECISION` L4/0007) — déjà signalé comme lacune structurelle par le
gate `15-RED-TEAM-GATE.md` du blueprint principal (C9), confirmé ici comme
également nécessaire pour la facturation électronique : une facture importée
ne doit **jamais** être soumise à la Plateforme Agréée comme si elle avait été
émise nativement.

## 3. Doctrine de projection Factur-X / UBL / CII

**La doctrine proposée par la mission est correcte, confirmée par cette
recherche (`ANALYSIS`)** :

```
SUPORDO canonical invoice
        ↓
   FORMAT MAPPER
        ├── Factur-X (norme EN 16931, profil à choisir : MINIMUM à EXTENDED)
        ├── UBL
        └── CII (syntaxe UN/CEFACT, base de Factur-X)
```

| Élément | Appartient à |
|---|---|
| Identité vendeur/acheteur, lignes, totaux, ventilation TVA, références, dates | **Domaine** (Facture SUPORDO) |
| Choix du profil Factur-X (MINIMUM/BASIC/EN16931/EXTENDED), structure XML exacte, mapping élément-à-élément vers la syntaxe CII/UBL | **Mapper** |
| Transport, enveloppe technique, authentification, statuts propriétaires du fournisseur | **Provider** (couche E) |

**Pourquoi c'est structurant, pas cosmétique** : Factur-X évolue à un rythme
rapide et documenté — version 1.09.2 publiée le 04/08/2026, version antérieure
notée au 10/06/2026, soit une mise à jour en moins de deux mois constatée dans
cette seule recherche. **Coder une version de format comme un invariant du
domaine serait une erreur immédiatement coûteuse** — c'est précisément ce que
le contrôle final (§7 de la mission, red team) interdit.

**Ce qui doit être versionné** : le mapper lui-même porte un `format_version`
explicite (champ déjà prévu dans le contrat d'échange, §4). **Ce qui doit être
archivé** : l'artefact exact transmis (le XML/PDF Factur-X réellement envoyé),
conservé immuable à côté de la Facture — une régénération ultérieure avec un
mapper mis à jour ne doit jamais remplacer la preuve de ce qui a été
effectivement transmis (`ANALYSIS`, cohérent avec l'exigence légale
d'authenticité/intégrité du document transmis).

## 4. E-Invoicing Exchange Contract

Concepts à préserver, **pas des tables** :

`ElectronicInvoiceExchange { provider, provider_account, routing_address,
routing_scheme, external_document_id, flow_id, tracking_id, format,
format_version, submitted_at, acknowledged_at, last_status_at,
technical_status, business_status, attempt_count, last_error_code,
last_error_message, retry_after, raw_provider_reference }`

Cet objet vit dans la couche C (`PLATFORM_CAPABILITY`), jamais dans la couche A
— la Facture porte une référence vers son (ou ses) `ElectronicInvoiceExchange`,
jamais l'inverse conceptuellement dominant.

### Cycle

```
ELIGIBILITY → ADDRESSING → VALIDATION → FORMAT GENERATION → SUBMISSION
→ TECHNICAL ACK → BUSINESS STATUS → ACCEPT / REJECT / RETRY / RECOVER
```

- **ELIGIBILITY** — la facture relève-t-elle de l'e-invoicing (B2B domestique
  assujetti) ou seulement de l'e-reporting (B2C, international) ? `OFFICIAL_SPEC`.
- **ADDRESSING** — résolution de la Plateforme Agréée du destinataire via
  l'annuaire, probablement par SIREN pivot. `OFFICIAL_SPEC`, certitude modérée.
- **VALIDATION** — conformité au profil de format choisi avant soumission.
- **FORMAT GENERATION** — projection canonique → Factur-X/UBL/CII (§3).
- **SUBMISSION** — envoi à la Plateforme Agréée de l'émetteur (pas directement
  au destinataire — c'est la PA qui relaie).
- **TECHNICAL ACK** — accusé de réception technique du flux.
- **BUSINESS STATUS** — statut métier du cycle de vie. **Les libellés
  officiels exacts restent `OPEN`** (base normative identifiée : AFNOR
  XP Z12-012/013/014, non consultée en détail dans cette recherche) — ne
  jamais inventer de libellés français avant vérification de ces normes.
- **ACCEPT / REJECT / RETRY / RECOVER** — voir §6.

Axonaut et Evoliz v1.43 n'exposent **aucun** de ces concepts. **Evoliz v1.56
en expose une implémentation réelle** (voir §4bis) — cette section a
néanmoins été construite à partir de la structure réglementaire elle-même,
pas par analogie avec un concurrent, et reste inchangée dans son contenu
normatif : §4bis compare, elle ne remplace pas.

## 4bis. Evoliz v1.56 — comparaison OFFICIAL SPEC vs IMPLEMENTATION

Second snapshot Evoliz analysé, version confirmée `1.56` (`grep "version:"` →
ligne 238 du fichier source). Le premier analysé, v1.43, ne portait aucune
couche e-invoicing (§0). Tout ce qui suit reste `IMPLEMENTATION_EXAMPLE` sans
exception — un choix d'architecture d'un éditeur, jamais une preuve
réglementaire, même quand Evoliz cite lui-même du contenu à consonance légale
(voir « affirmations non vérifiées » en fin de section).

### Convergences avec le cycle OFFICIAL_SPEC de §4

| Étape OFFICIAL_SPEC | Ce qu'Evoliz 1.56 fait concrètement | Convergence |
|---|---|---|
| ADDRESSING | `GET .../electronic-addresses` (résout les adresses candidates via un annuaire qu'Evoliz nomme « Chaintrust/AFNOR » — `IMPLEMENTATION_EXAMPLE`, à ne pas confondre avec l'annuaire officiel PPF/AIFE de §0) puis `PATCH .../routing-address` (fixe le choix ; **la valeur envoyée par l'appelant n'est jamais fiable, tout est re-dérivé et revalidé côté serveur** contre le référentiel) | Forte — confirme qu'ADDRESSING est une étape distincte et « server-authoritative », cohérent avec la doctrine déjà posée |
| SUBMISSION | `POST .../transmit`, strictement séparé de la résolution d'adresse — « fixer » et « envoyer » sont deux appels distincts | Forte |
| TECHNICAL ACK | `tech_status` (chaîne libre non normalisée, ex. `"Pending"`/`"Ok"`), `pa_response` (opaque), `ack` (objet libre) dans la réponse de `transmit` | Partielle — Evoliz répercute les valeurs brutes du provider sans les normaliser (voir DO NOT COPY) |
| BUSINESS STATUS | **Absent côté sortant** (facture/avoir/acompte) — aucun champ persistant lisible par `GET` ; l'état ne se déduit qu'indirectement des codes d'erreur renvoyés par un appel ultérieur (`already_emitted`, `invoice_rejected`...). **Présent côté entrant** (achat) : `e_invoicing.status` (enum `received`/`refused`/`cashed`) + `status_code` (enum `'202'`/`'210'`/`'212'`), qu'Evoliz attribue à « la spécification DGFiP » sans la citer précisément | **Asymétrie notable — voir DO NOT COPY, ne pas la reproduire** |
| RETRY | `retry_too_soon` (409), délai non chiffré dans la documentation consultée | Confirme la nécessité d'un `retry_after` côté SUPORDO, sans en donner de valeur de référence |

### Cas limites et protections observés

- **Historisation du SIREN acheteur au moment de la création du document**,
  jamais le SIREN courant de la fiche client — directement transposé en §2.1
  (doctrine Lieu + snapshot).
- **`skip: true` (acheteur hors périmètre e-invoicing — particulier, étranger,
  pas de SIREN) vs `422 invalid_client_siren` (SIREN présent mais malformé)**
  — deux cas distincts, jamais confondus : « hors périmètre » n'est pas une
  erreur, « donnée invalide » en est une.
- **Garde anti-double-émission `already_emitted`/`retry_too_soon` (409),
  qu'Evoliz qualifie lui-même d'« idempotent-guarded »** — ce n'est **pas**
  une clé d'idempotence HTTP fournie par l'appelant, c'est une relecture de
  l'état serveur à chaque nouvel appel (confirmé par recherche exhaustive du
  fichier : aucune clé d'idempotence, aucun header dédié). **Ne pas copier ce
  vocabulaire comme preuve que le sujet est résolu** — SUPORDO doit
  construire les deux mécanismes (clé d'idempotence appelant + garde d'état
  serveur), voir `03` §3.
- **Avoirs** : cycle strictement symétrique aux factures, avec quatre codes
  409 additionnels propres à la dépendance causale d'un avoir envers l'état
  PA de son document source (`avoir_source_not_emitted`,
  `avoir_source_not_deposited`, `avoir_total_refused_invoice`,
  `avoir_total_rejected_invoice`). **Tension non résolue par Evoliz
  lui-même** : sa seule voie de recovery documentée après un refus PA sur une
  facture est « créez un avoir total » — mais transmettre cet avoir à la PA
  est *lui-même bloqué* si la facture source a justement été refusée/rejetée.
  Evoliz ne propose aucune issue dans ce cas précis. **Ne pas résoudre cette
  tension en silence dans la doctrine SUPORDO** — voir §4ter et la matrice
  §6, cas 6.
- **Acomptes** : même cycle, mêmes garde-fous, pas de dépendance causale
  supplémentaire (pas de document source amont).
- **Notification de paiement** (`POST .../payments/{id}/notify-payment`) :
  distincte du rapprochement bancaire interne — notifie explicitement la PA
  qu'un paiement a été reçu sur une facture déjà transmise, avec ses propres
  préconditions (`invoice_not_emitted`, `invoice_rejected`) et sa propre
  garde anti-doublon (`already_notified`).
- **Trois identifiants de corrélation à trois niveaux, jamais fusionnés** :
  `flow_id` (émis par la PA elle-même, nullable), `tracking_id` (généré par
  Evoliz, toujours présent), `external_document_number` (fourni par
  l'appelant, connu depuis la v1.43, usage général non spécifique à
  l'e-invoicing). **Confirme directement** que ces identifiants appartiennent
  conceptuellement à `ElectronicInvoiceExchange` (§4), jamais à la Facture
  elle-même — voir la correction apportée en `03` et `06`.
- **Bascule `e_invoicing` (feature flag) en cascade** : son activation durcit
  rétroactivement la validation de ressources déjà existantes (SIRET/SIREN
  devient obligatoire sur un client professionnel français, un
  `business_process` devient obligatoire sur le document) sans changer leur
  schéma de base — pattern d'architecture à noter, voir DO NOT COPY.

### Affirmations à caractère réglementaire faites par Evoliz v1.56, non vérifiées (`OPEN`)

- Référence « BR-FR-CPRO-15 » citée pour justifier la limite de 50 caractères
  du numéro d'engagement légal (BT-13) — non retrouvée ni vérifiée
  indépendamment dans cette recherche.
- « Lifecycle code ... as defined by the DGFiP specification » pour les codes
  CDV 202/210/212 — Evoliz attribue ces codes à une spécification DGFiP
  externe sans la citer précisément. **Piste concrète mais non vérifiée**
  pour l'item `OPEN` §5.1 (libellés officiels de cycle de vie) — à confronter
  directement à AFNOR XP Z12-012/013/014 ou à la spécification DGFiP avant
  toute reprise, ne pas adopter ces codes comme `OFFICIAL_SPEC` sur la seule
  foi de cette citation.
- Formulations « mandatory »/« obligation » sur les champs SIRET/SIREN/TVA
  conditionnés par le flag `e_invoicing` — présentées comme des conséquences
  de la loi sans citation de texte précise.

## 4ter. Machine d'état — principes, pas un graphe réglementaire figé

Les libellés officiels exacts du cycle de vie réglementaire restent `OPEN`
(§5.1) — ce document ne crée donc **aucun graphe de statuts réglementaires
définitif**. Ce qui suit encadre le *comportement* du service e-invoicing
indépendamment des libellés exacts, et **remplace l'invariant trop simple
« le statut ne régresse jamais »** d'une version antérieure de ce document :

- **Graphe explicite de transitions autorisées** — même avant de connaître
  les libellés exacts, l'ordre partiel est déjà connu : ELIGIBILITY →
  ADDRESSING → VALIDATION → FORMAT GENERATION → SUBMISSION → TECHNICAL ACK →
  BUSINESS STATUS (terminal : ACCEPT ou REJECT, RETRY possible avant toute
  transition terminale). Toute transition hors de cet ordre partiel est
  **rejetée** par le service, pas seulement ignorée.
- **Événements externes idempotents** — recevoir deux fois le même événement
  de statut ne produit qu'un seul effet (cas 8, §6).
- **Événements dupliqués ignorés sans effet** — un événement strictement
  identique (même identifiant, même contenu) reçu plusieurs fois n'est
  traité qu'une fois, silencieusement.
- **Événements obsolètes ou incompatibles journalisés, jamais appliqués** —
  un événement qui contredirait une transition déjà terminale (ex. un accusé
  technique reçu après un statut métier déjà définitif) est conservé dans
  l'historique d'audit (`03` §6) mais n'altère jamais l'état affiché.
- **État courant jamais corrompu par l'ordre d'arrivée réseau** — l'état
  affiché est déterminé par la position dans le graphe de transitions
  autorisées, jamais par le dernier événement arrivé chronologiquement côté
  réseau (qui peut être désordonné).

Ces cinq principes s'appliquent **quels que soient les libellés exacts** une
fois connus — ils portent sur la discipline de traitement, pas sur la
nomenclature réglementaire.

### Séparation des statuts (corrige une confusion potentielle de `02`)

Trois notions de statut, **jamais fusionnées** :

| Notion | Porteur | Exemple |
|---|---|---|
| `SUPORDO UX STATE` | Frontend (`02`) | « Transmise », « Action requise » — vocabulaire orienté utilisateur, stable dans le temps |
| `EXTERNAL TECHNICAL STATUS` | `ElectronicInvoiceExchange.technical_status` | Accusé technique brut du provider (ex. `tech_status` Evoliz) |
| `EXTERNAL BUSINESS STATUS` | `ElectronicInvoiceExchange.business_status` | Statut métier réglementaire — **libellés exacts `OPEN`**, code CDV le cas échéant |

Le mapping `EXTERNAL BUSINESS STATUS → SUPORDO UX STATE` est **versionné**
(un même statut externe peut être présenté différemment si la compréhension
du cycle de vie officiel évolue) — jamais codé en dur comme une équivalence
figée dans l'interface.

**Interdiction explicite** : aucune règle universelle du type « statut
externe = REFUSED ⇒ créer un avoir » n'est codée sans vérifier, au moment de
l'implémentation réelle, (a) que le document est juridiquement émis/déposé
(cf. distinction CDV 200/210 observée chez Evoliz — un document refusé avant
dépôt confirmé n'est pas dans le même état qu'un document refusé après), et
(b) qu'un avoir est réellement le recovery approprié à *ce* statut précis, pas
seulement le recovery qu'un concurrent a choisi de proposer. Le cas Evoliz
lui-même (§4bis) montre qu'une règle de recovery apparemment simple peut
avoir des impasses documentées (avoir bloqué sur facture déjà refusée) — la
doctrine SUPORDO ne doit ni copier une règle simpliste, ni en inventer une
qui résout artificiellement une tension que même la source d'implémentation
n'a pas résolue.

## 5. Ce que la recherche officielle n'a pas permis de résoudre (`OPEN`, liste fermée)

1. Libellés français exacts des statuts de cycle de vie réglementaires — voir
   §4bis pour une piste non vérifiée (codes CDV 202/210/212 cités par Evoliz
   v1.56 comme définis par la spécification DGFiP, `IMPLEMENTATION_EXAMPLE`
   seulement).
2. Délai et format exact des données de paiement transmises en e-reporting.
3. Articulation précise entre Chorus Pro (B2G) et le dispositif B2B — la page
   AIFE suggère une extension B2B (« Chorus Pro Factures inter-entreprises »)
   mais cette affirmation n'a pas été recoupée par une seconde source.
4. Mécanisme fin d'adressage (SIREN seul, ou SIREN+SIRET, ou code de routage
   propre à l'annuaire) au-delà du principe du SIREN comme pivot.
5. Montant exact de l'indemnité forfaitaire de recouvrement et du taux
   d'escompte actuellement en vigueur (traditionnellement 40 €, non
   revérifié).

**Ne pas combler ces `OPEN` par une valeur plausible tirée d'Evoliz ou
d'Axonaut.** Revérifier directement les sources citées en §0 avant de figer
une implémentation qui en dépend.

## 6. Matrice idempotence et reprise

Voir `05-ACCEPTANCE-NEGATIVE-TEST-MATRIX.md` pour la version testable ; la
matrice de comportement attendu est posée ici.

| # | Situation | Action SUPORDO | Donnée conservée | Message frontend | Retry ? | Action humaine ? | Risque de doublon |
|---|---|---|---|---|---|---|---|
| 1 | Double clic utilisateur | Déduplication par clé côté flow, deuxième requête sans effet | Facture + `flow_id` unique | « Transmission en cours », bouton désactivé | Non | Non | Nul si clé d'idempotence réelle (§7 backend) |
| 2 | Réseau coupe après envoi, avant réponse | Ne jamais re-soumettre à l'aveugle — vérifier le statut auprès du provider avant tout retry | Tentative horodatée, `attempt_count+1` | « Transmission en cours de vérification » | Différé, après vérification | Oui si la vérification échoue après délai | Modéré, mitigé par la vérification préalable |
| 3 | Timeout provider | Retry borné avec backoff, si l'opération de soumission est elle-même idempotente côté provider | `last_error_code=timeout`, `retry_after` | « Nouvelle tentative en cours » | Oui, automatique borné | Après épuisement des tentatives | Faible si idempotence côté provider confirmée (`OPEN` par provider réel) |
| 4 | Provider reçoit mais SUPORDO ne reçoit pas l'ACK | Ne jamais re-soumettre sans vérification active du statut | `technical_status = unknown_pending_verification` | « Statut en cours de vérification » | Non automatique, vérification active | Alerte si non résolu après délai | **Élevé si mal géré — cas le plus structurant** |
| 5 | Adresse de routage invalide | Rejet à l'étape ADDRESSING si détectable en amont | `last_error_code = routing_invalid` | « Nous n'arrivons pas à identifier la plateforme de ce client — vérifiez son SIREN » | Oui après correction | Oui, obligatoire | Nul (rien transmis) |
| 6 | Facture déjà transmise, retransmission tentée | Refus systématique côté SUPORDO ; **si le statut externe est REFUSED/REJECTED, ne proposer un avoir qu'après vérification des préconditions réelles** (document juridiquement émis/déposé, cf. §4ter — un simple statut « refusé avant dépôt confirmé » n'a pas la même conséquence qu'un « refusé après dépôt ») | Historique de transmission intact | « Déjà transmise. » puis, seulement si les préconditions sont réunies : « Pour corriger, émettez un avoir. » | Non | Décision de créer un avoir, jamais automatique | Nul si refus backend-enforced ; **risque résiduel documenté** : Evoliz v1.56 montre qu'un avoir peut lui-même être bloqué si le document source est refusé/rejeté (`avoir_total_refused_invoice`/`avoir_total_rejected_invoice`, §4bis) — SUPORDO doit prévoir explicitement ce cas plutôt que de le découvrir en production |
| 7 | Retry trop tôt (avant `retry_after`) | Mise en attente jusqu'à `retry_after` | `retry_after` inchangé | « Nouvelle tentative programmée dans X min » | Différé automatique | Non, sauf forçage explicite averti | Faible |
| 8 | Statut externe dupliqué | Traitement idempotent par identifiant/horodatage d'événement | Dernier statut appliqué avec sa source | Aucun changement visible au doublon | Sans objet | Non | Nul si le traitement de statut est idempotent |
| 9 | Statut arrivé dans un ordre inattendu | Monotonie du cycle de vie — ne jamais régresser un statut déjà avancé | Historique complet de tous les statuts reçus | Aucun changement si l'état affiché reste cohérent | Sans objet | Alerte support si incohérence réelle | Nul (risque réel = régression d'état visible) |
| 10 | Provider indisponible | File d'attente explicite, jamais un échec silencieux | Statut « en attente du service » | « Transmission différée, sera automatique au rétablissement » | Automatique différé, backoff long | Si panne prolongée au-delà d'un seuil | Faible si la file est elle-même idempotente |

## 7. DO NOT COPY

| Observed pattern | Why interesting | What not to copy | SUPORDO abstraction if any |
|---|---|---|---|
| Axonaut : B2C = Company avec nom écrasé par concaténation employé | Contournement d'un modèle à une seule entité | Le mécanisme d'écrasement de nom | Modéliser Client comme entité polymorphe (personne physique/morale) dès la conception |
| Axonaut : `is_for_invoice`/`is_for_delivery`/`is_for_quotation` booléens cumulables sans défaut | Système de tags simple | Absence de rôle par défaut, absence de « lieu de prestation » | Rôles d'adresse typés + Lieu SUPORDO comme concept séparé (déjà acté) |
| Axonaut : Quotation à 3 statuts plats (`accepted/refused/pending`) | Sous-spécification volontaire | Ce modèle pauvre | SUPORDO garde sa propre discipline de statuts, déjà posée dans le Product Blueprint principal |
| Axonaut : Invoice sans champ `status` explicite (dérivé de `paid_date`) | État implicite fragile | L'absence de machine à états déclarée | Statut explicite et versionné sur la Facture |
| Axonaut : incohérence de format de date (Unix ts string vs RFC3339) entre Devis et Facture du même produit | Signe d'API sans contrat unifié | Toute incohérence de ce type | Un seul format (ISO 8601) partout, sans exception |
| Axonaut : `accounting_code` tantôt string brute, tantôt objet `{code,name}` selon l'endpoint | Incohérence structurelle | La forme variable | Type unique et cohérent pour tout code comptable, quel que soit le point d'usage |
| Axonaut : `roles` en string à séparateur `;` | Anti-pattern de modélisation | Le parsing par convention de séparateur | Rôles en tableau typé |
| Axonaut : création silencieuse d'un Product si `id`/`internal_id` absents (upsert implicite) | Pratique dangereuse pour l'intégrité référentielle | Le comportement silencieux | Rejet explicite ou résolution contrôlée par code produit |
| Evoliz : codes numériques de statut en puissances de deux (`1,2,4,8,16,22`) | Encodage bitmask propriétaire | La numérotation elle-même | Statuts nommés, pas des entiers magiques |
| Evoliz : `Credit` sans FK directe vers la facture d'origine (nécessite `/links`) | Lacune de traçabilité directe | L'absence de référence directe | FK bidirectionnelle explicite Facture ↔ Avoir |
| Evoliz : plafond arbitraire de 3 `bonuses` par facture | Décision produit Evoliz, pas une règle métier universelle | Le chiffre 3 comme règle | Si retenu un jour (`DO_NOT_BUILD_YET`), ne pas hériter d'un plafond non justifié |
| Evoliz : table de codes d'exonération de TVA citant le CGI, avec doublon apparent (codes 7 et 8) | Exemple concret du risque de copier une table réglementaire d'un tiers sans vérification | La table telle quelle | Vérifier chaque motif d'exonération au BOFiP avant toute liste figée |
| Evoliz : « taux de TVA maximum accepté 30% » présenté comme règle système | Ressemble à une règle légale mais n'en cite aucune | Toute déduction d'un plafond légal depuis ce champ | Ne jamais dériver une règle fiscale d'une contrainte de validation d'un concurrent |
| Evoliz : connecteur nommé `myunisoft/connect` | Couplage nominatif à un outil précis | Le nom du provider dans l'endpoint | Adapter générique « connecteur comptable par clé API », provider en paramètre |
| Evoliz : `term.nopenalty`/`term.recovery_indemnity` présentés comme mentions légales sans citation de texte | Suggère une obligation sans la prouver | Prendre ces champs comme preuve de la règle | Vérifier indépendamment au Code de commerce avant d'implémenter la mention |
| Axonaut : `tax_rates[]`, plusieurs taux de TVA par ligne, généralisé à tort dans une version antérieure de ce document | Illustre précisément le risque que la discipline de preuve de cette annexe vise à prévenir — une structure d'implémentation transformée en règle métier sans vérification normative | Le nombre de taux par ligne ; ne jamais dériver le modèle canonique de ce champ | Une ligne = un taux (EN 16931 BT-151/BT-152, §2.4) ; le besoin BTP multi-taux se résout par plusieurs lignes, pas par un champ multi-valué |
| Evoliz v1.56 : « idempotent-guarded » appliqué à une garde d'état serveur (`already_emitted`/`retry_too_soon`), pas une clé d'idempotence HTTP | Vocabulaire trompeur si repris tel quel — donne l'impression qu'une vraie idempotence existe | Le terme « idempotent » pour ce seul mécanisme | SUPORDO construit une vraie clé d'idempotence côté appelant, en complément d'une garde d'état serveur — les deux, jamais l'un à la place de l'autre (`03` §3) |
| Evoliz v1.56 : statut électronique persistant côté achats (`e_invoicing.status`), seulement inférable par erreur côté ventes | Asymétrie d'architecture réelle, probablement non délibérée comme bonne pratique | L'asymétrie elle-même | Exposer un `business_status` persistant et lisible symétriquement dans les deux sens de flux |
| Evoliz v1.56 : `tracking_id` formaté `evoliz-{type}-{id}-{année}-{seq}` | Convention de corrélation propre à l'éditeur | Le format et le préfixe `evoliz-` | Un identifiant de corrélation généré par SUPORDO existe dans `ElectronicInvoiceExchange` uniquement, sous un format propre |
| Evoliz v1.56 : seule voie de recovery après refus PA = avoir total, sans alternative, y compris quand cette voie est elle-même bloquée | Montre les limites d'une règle de recovery rigide plutôt qu'un modèle à imiter | La règle « REFUSED ⇒ avoir total » comme automatisme universel | Voir §4ter — vérifier les préconditions réelles avant de proposer un avoir, ne jamais l'imposer par défaut |

## 8. Ce que ce document ne fait pas

Ne conçoit aucune table, aucune migration. Ne choisit aucune Plateforme
Agréée. Ne fixe aucune version de format comme définitive. Ne construit aucune
des extensions BTP identifiées en §2.9 — voir `06` §15 pour leur classement
exact.
