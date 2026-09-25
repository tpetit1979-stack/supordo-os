# 03 — E-Invoicing Backend Contract

Contrat de responsabilités, sans SQL. Étend `08-BACKEND-AND-NONFUNCTIONAL-
CONTRACT.md` du Product Blueprint principal au domaine e-invoicing/comptabilité
— n'y contredit rien, le complète.

## 1. Responsabilités par couche (reprend `01` §1)

### Domaine Facture (`DOMAIN_CORE`)
Porte les données canoniques (`01` §2), les règles métier (immuabilité L1,
régime natif/importé L4, verrouillage), et une **référence** vers son ou ses
`ElectronicInvoiceExchange`. Ne connaît **aucun** détail de format ni de
provider.

### Service e-invoicing (`PLATFORM_CAPABILITY`)
Orchestre le cycle `01` §4 (ELIGIBILITY → ... → ACCEPT/REJECT/RETRY/RECOVER).
Ne modifie jamais directement le contenu de la Facture — seulement son état
d'échange. Responsable de l'idempotence et de la file de retry (§4-5).

### Provider adapter (`PLATFORM_CAPABILITY`, couche E)
Un adapter par Plateforme Agréée/fournisseur. Traduit le contrat d'échange
canonique (`01` §4) vers l'API propre du provider, et inversement pour les
statuts entrants. **Aucun champ du domaine ne doit exposer le vocabulaire d'un
provider donné** — voir `01` §7 DO NOT COPY.

## 2. Transaction boundaries (conceptuel)

- La transition d'état commercial de la Facture (brouillon → numérotée →
  verrouillée) est une transaction **indépendante** de la transition d'état
  d'échange électronique (`ElectronicInvoiceExchange`) — les deux ne doivent
  jamais être committées dans la même transaction technique, parce que la
  seconde dépend d'un appel réseau externe (jamais de garantie atomique
  possible avec un tiers).
- Conséquence directe : une Facture peut être valide et verrouillée
  (irréversible au sens L1) **avant** que sa transmission électronique soit
  résolue — les deux statuts progressent indépendamment, jamais fusionnés
  (cohérent avec `01` §4, `ElectronicInvoiceExchange` comme concept distinct).

## 3. Idempotency

- Toute soumission d'une Facture au service e-invoicing porte une clé
  d'idempotence générée côté SUPORDO au moment de la tentative (pas côté
  provider) — **aucun des trois documents API analysés n'implémente de vraie
  clé d'idempotence HTTP fournie par l'appelant** (`01` §7 ; confirmé absent
  chez Axonaut et Evoliz v1.43 ; et chez **Evoliz v1.56 également** — sa
  garde `already_emitted`/`retry_too_soon` est une relecture d'état serveur
  a posteriori, pas une déduplication de requête a priori, `01` §4bis) ;
  c'est un gap de marché que SUPORDO doit combler, pas hériter. **SUPORDO
  construit les deux mécanismes** : une clé d'idempotence côté appelant ET
  une garde d'état serveur — le second seul, à la Evoliz, ne suffit pas.
- Le traitement des statuts entrants (webhook ou polling) est lui-même
  idempotent : appliquer deux fois le même statut ne doit produire aucun
  effet de bord visible (cas 8 de `01` §6, principes détaillés en `01` §4ter).
- `external_document_id` est un champ du contrat d'échange
  `ElectronicInvoiceExchange` (`01` §4) — **jamais un champ de la Facture
  elle-même** (correction : une version antérieure de ce document laissait
  entendre le contraire). Il sert de clé de corrélation stable côté
  provider — distinct de `flow_id` (émis par le provider/la Plateforme
  Agréée) et de `tracking_id` (généré par SUPORDO pour son propre suivi) —
  trois identifiants à trois niveaux jamais fusionnés, pattern confirmé par
  Evoliz v1.56 qui distingue précisément ces trois rôles (`01` §4bis).
  Aucun de ces identifiants n'a vocation à vivre sur l'objet Facture du
  domaine.

## 4. Event handling et jobs asynchrones

- Réception de statut : soit par callback/webhook du provider (si
  disponible), soit par polling actif — le service e-invoicing doit
  fonctionner correctement dans les deux modes, un provider donné pouvant
  n'offrir que l'un des deux (Evoliz, par exemple, n'expose que du polling
  via `/events`, `IMPLEMENTATION_EXAMPLE`).
- Tout job asynchrone (soumission, vérification de statut, retry) est
  traçable : origine, tentative, résultat — voir §7 audit trail.

## 5. Retry

- Backoff exponentiel borné, jamais un retry immédiat en boucle.
- Un retry n'est **jamais** déclenché automatiquement dans les cas où l'état
  réel côté provider est inconnu (cas 2 et 4 de `01` §6) — d'abord vérifier,
  puis agir.
- `retry_after` (champ du contrat d'échange) fait autorité sur le moment du
  prochain essai automatique.

## 6. Audit trail

- Chaque transition d'état de l'`ElectronicInvoiceExchange` est journalisée :
  ancien statut, nouveau statut, horodatage, source (système ou humain).
- Cohérent avec l'exigence déjà posée en `08` §7 du Product Blueprint
  principal (trace des transitions verrouillantes) — étendue ici
  explicitement au cycle e-invoicing, qui n'y était pas encore couvert.
- L'artefact exact transmis (Factur-X/UBL/CII généré) est archivé de façon
  immuable, distinct de toute régénération ultérieure (`01` §3).

## 7. Permissions et RLS

- Isolation tenant stricte sur `ElectronicInvoiceExchange` comme sur toute
  autre table (cohérent avec `08` §1 du Product Blueprint principal — et avec
  la correction B2/B3 du gate `15-RED-TEAM-GATE.md`, qui a spécifiquement
  signalé l'absence de test cross-tenant sur la Facture dans la séquence
  actuelle : cette lacune s'étend mécaniquement à l'échange électronique si
  elle n'est pas corrigée en amont).
- Accès expert-comptable (voir `04`) : lecture seule par défaut sur les
  données comptables/export, jamais d'accès en écriture sur le cycle
  d'échange électronique lui-même sauf rôle explicitement élevé.

## 8. Secret isolation

- Les identifiants d'authentification vers chaque Plateforme Agréée/provider
  sont détenus exclusivement par le provider adapter (couche E), jamais
  exposés à la couche domaine ni au frontend — cohérent avec `08` §9 et `14`
  §11 du Product Blueprint principal (politique de secrets à construire
  explicitement, aucune protection native présumée).

## 9. External IDs et version des formats

- `external_document_id`, `flow_id`, `tracking_id`, `raw_provider_reference` :
  tous opaques du point de vue du domaine, jamais interprétés comme porteurs
  de sens métier.
- `format_version` obligatoire sur chaque échange, jamais implicite — condition
  de traçabilité si la norme Factur-X évolue entre deux transmissions du même
  tenant (rythme constaté : nouvelle version tous les ~2 mois, `01` §3).

## 10. Immutable snapshots

- La Facture elle-même est verrouillée dès numérotation (`L1`, déjà acté).
- L'adresse (§2.1 de `01`) est copiée en dur au moment de l'émission, jamais
  une référence vivante.
- L'artefact de format transmis (§6 ci-dessus) est un second snapshot,
  indépendant du premier — une correction du mapper ne réécrit jamais un
  artefact déjà transmis.

## 11. Observabilité et erreurs

- Chaque appel au provider adapter est observable individuellement (succès/
  échec/latence) — cohérent avec `08` §12 du Product Blueprint principal.
- Un échec silencieux est le risque principal identifié : un statut non
  reçu ou mal interprété ne doit **jamais** aboutir à un affichage
  « Transmise » par défaut — l'état par défaut en cas d'incertitude est
  toujours « en cours de vérification », jamais un état positif présumé.

## 12. Ce qui doit être garanti à quel niveau

| Niveau | Garantie |
|---|---|
| **DB** | Isolation RLS par tenant sur toute table du domaine e-invoicing/comptabilité ; verrouillage de la Facture au niveau contrainte, pas applicatif seul (cohérent `08` §5) ; unicité de `external_document_id` par tenant, sur `ElectronicInvoiceExchange` — jamais sur la Facture |
| **Service** | Idempotence des soumissions (clé appelant + garde d'état, §3) et du traitement de statuts ; respect du graphe de transitions autorisées, événements dupliqués/obsolètes journalisés sans jamais corrompre l'état affiché (principes détaillés `01` §4ter, remplace l'ancienne formule « jamais de régression d'état ») ; séparation stricte des transactions commerciale/électronique (§2) |
| **Provider adapter** | Traduction complète domaine ↔ provider sans fuite de vocabulaire ; isolation des secrets ; observabilité individuelle par appel |
| **Frontend** | **Aucun invariant réglementaire ou financier ne dépend du frontend** — chaque règle appliquée côté UI (blocage de bouton, validation de formulaire) est redondante avec une garantie serveur équivalente, jamais la seule ligne de défense |

## Ce que ce document ne fait pas

Ne nomme aucune table, aucune fonction, aucun provider. Ne choisit aucun mode
de transport (REST/webhook/SFTP). Le choix technique précis revient à la
tranche de construction réelle, cadrée au moment où `T-EINVOICING` (voir `06`)
sera ouverte dans la séquence du Product Blueprint principal.
