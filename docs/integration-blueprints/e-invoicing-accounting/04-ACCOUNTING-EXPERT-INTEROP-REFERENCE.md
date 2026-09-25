# 04 — Accounting & Expert-Comptable Interop Reference

Trois capacités analysées séparément. **Aucune supposition que les trois
doivent être construites en V1** — chacune porte sa propre classification de
version, voir `06` §15 pour la synthèse.

## A. Export (FEC / fichiers / journaux)

| Champ | Contenu |
|---|---|
| **USER JOB** | L'artisan (ou son comptable) doit pouvoir produire un fichier conforme pour un contrôle fiscal ou une clôture d'exercice. |
| **DONNÉES ENTRANTES** | Aucune — export en lecture seule des données déjà en base (Facture, Avoir, Paiement). |
| **DONNÉES SORTANTES** | Fichier FEC (format réglementaire français, `LEGAL_VERIFIED` dans son principe — obligation légale de tenue d'un FEC existe indépendamment de la facturation électronique, non détaillée dans cette recherche), ou journaux par type (ventes/achats/banque/opérations diverses). |
| **READ/WRITE** | Lecture seule. |
| **SYNC DIRECTION** | Aucune — génération à la demande, pas de synchronisation continue. |
| **MANUAL/AUTOMATIC** | Manuel (déclenché par l'utilisateur) en premier lieu ; automatisable en V3. |
| **MAPPING REQUIRED** | Oui — chaque Facture/ligne doit être projetable vers une écriture comptable (voir §12, `AccountingMapping`). |
| **SECURITY** | Lecture seule sur les données financières du tenant, export téléchargeable seulement par un rôle autorisé. |
| **MULTI-TENANT CONSEQUENCE** | Export strictement scopé à un seul tenant — aucun risque de fuite si l'isolation RLS de base est respectée (`03` §7). |
| **AUDIT** | Chaque génération d'export journalisée (qui, quand, quelle période). |
| **FAILURE MODE** | Export incomplet ou incohérent si des factures sont dans un état intermédiaire — ne jamais exporter une facture non verrouillée comme si elle était définitive. |
| **VERSION** | `LATER_ACCOUNTING` (voir `06` §15). |

**Pattern positif observé (`IMPLEMENTATION_EXAMPLE`, Evoliz)** : exposer le
FEC comme une **ressource API paginée et filtrable** (`GET /journals/fec`), pas
seulement comme un fichier à générer et télécharger — facilite grandement une
intégration programmatique côté expert-comptable. À considérer comme un
objectif de conception `ANALYSIS`, pas une obligation réglementaire (le format
FEC lui-même reste un fichier standard, l'API par-dessus est un confort
optionnel).

## B. Connecteur (logiciel comptable ou plateforme externe)

| Champ | Contenu |
|---|---|
| **USER JOB** | Synchroniser automatiquement les factures/paiements vers l'outil de production comptable de l'expert-comptable (ex. MyUnisoft, Pennylane, Cegid), sans ressaisie. |
| **DONNÉES ENTRANTES** | Éventuellement des statuts de traitement retournés par l'outil tiers (facture comptabilisée, lettrée). |
| **DONNÉES SORTANTES** | Facture/Avoir/Paiement au format attendu par le connecteur, projetés via le mapping comptable (§12). |
| **READ/WRITE** | Écriture vers le tiers ; lecture de statut en retour. |
| **SYNC DIRECTION** | SUPORDO → outil comptable, à sens unique dans un premier temps (pas de synchronisation retour vers SUPORDO au-delà d'un statut). |
| **MANUAL/AUTOMATIC** | Manuel en V1/V2 (déclenchement explicite) — automatique seulement après validation du mapping par le comptable. |
| **MAPPING REQUIRED** | Oui, obligatoire — voir §12. Sans mapping validé, aucune donnée ne doit être poussée. |
| **SECURITY** | Clé API par connecteur, jamais partagée entre tenants, jamais exposée côté client (cohérent `03` §8). |
| **MULTI-TENANT CONSEQUENCE** | Chaque tenant configure son propre connecteur — aucun mapping ni aucune clé n'est partagée entre tenants, même si le même cabinet comptable les gère tous (voir §13). |
| **AUDIT** | Chaque envoi vers le connecteur journalisé, avec statut de succès/échec par facture. |
| **FAILURE MODE** | Connecteur indisponible ou mapping invalide — jamais un échec silencieux ; cohérent avec le principe déjà posé en `03` §11. |
| **VERSION** | `LATER_ACCOUNTING`. |

**Pattern observé (`IMPLEMENTATION_EXAMPLE`, Evoliz)** : connecteur nommé par
simple clé API (`POST /companies/{id}/myunisoft/connect`) — modèle minimal à
faible friction. **Ne pas copier le nom du provider dans l'API SUPORDO** (voir
`01` §7) — l'abstraction est « connecteur comptable par clé API », le provider
est un paramètre, jamais un nom en dur dans le domaine.

## C. Accès délégué (expert-comptable)

| Champ | Contenu |
|---|---|
| **USER JOB** | Un expert-comptable consulte ou exporte les données de plusieurs dossiers clients (tenants) sans que chaque artisan doive lui recréer un compte par dossier. |
| **DONNÉES ENTRANTES** | Aucune, sauf si le comptable configure lui-même un connecteur (capacité B) pour le compte du tenant. |
| **DONNÉES SORTANTES** | Lecture des données financières du ou des tenants auxquels il est explicitement autorisé. |
| **READ/WRITE** | Lecture seule par défaut ; écriture seulement si un rôle élevé est explicitement accordé (ex. configurer un connecteur). |
| **SYNC DIRECTION** | Sans objet (accès, pas de synchronisation). |
| **MANUAL/AUTOMATIC** | Manuel — invitation explicite du tenant vers un compte expert-comptable identifié par email, jamais un accès implicite. |
| **MAPPING REQUIRED** | Non. |
| **SECURITY** | Voir §13 — un expert-comptable n'est pas un salarié du tenant, son identité et ses droits sont indépendants du modèle Personnel/Utilisateur interne. |
| **MULTI-TENANT CONSEQUENCE** | **Structurante** — un même compte expert-comptable peut être autorisé sur N tenants, avec des droits potentiellement différents par tenant (lecture seule chez l'un, configuration de connecteur chez l'autre). Voir §13. |
| **AUDIT** | Chaque accès et chaque export effectué par un compte délégué journalisé, distinctement des actions du personnel interne du tenant. |
| **FAILURE MODE** | Un tenant révoque l'accès du comptable — effet immédiat, pas de fenêtre de grâce implicite. |
| **VERSION** | `LATER_ACCOUNTING`. |

## 12. Accounting Mapping — concepts, pas des tables

```
Canonical concept
       ↓
Provider mapping
```

Concepts à préserver conceptuellement, dont l'existence future doit être
anticipée sans être construite maintenant :

- **`AccountingMapping`** — lien entre une notion métier SUPORDO (catégorie de
  prestation, taux de TVA) et un compte du plan comptable du tenant.
- **`JournalMapping`** — quel journal comptable (vente/achat/banque/opérations
  diverses) reçoit quel type de document SUPORDO.
- **`TaxMapping`** — quel taux de TVA SUPORDO correspond à quel compte de TVA
  collectée/déductible (pattern confirmé par Axonaut : deux comptes distincts
  pour un même taux nominal selon le sens vente/achat, `IMPLEMENTATION_EXAMPLE`).
- **`PaymentMethodMapping`** — quel moyen de paiement SUPORDO correspond à
  quel compte de trésorerie/journal de banque.
- **`ExternalAccountCode`** — le code de compte tel qu'il existe **dans le
  système du tenant**, jamais un code fixé par SUPORDO.

**Règle stricte, rappelée de la mission** : SUPORDO ne code **jamais** de
constantes comme `myunisoft_account_code`, `evoliz_journal_id` ou
`inqom_journal_id` dans ses objets métier. Chaque tenant définit son propre
mapping vers son propre plan comptable et son propre outil — SUPORDO ne porte
que le concept canonique et la relation vers le mapping du tenant, jamais une
valeur figée par provider.

**Pattern positif observé (`IMPLEMENTATION_EXAMPLE`, Evoliz)** : le triplet
`SaleClassification { accountid, vataccountid, vat_rate }` — une catégorie
métier (« Table et chaise ») mappée une fois vers un compte PCG, un compte de
TVA collectée et un taux — appliqué automatiquement à chaque facture ensuite.
C'est exactement la forme du concept `AccountingMapping`/`TaxMapping`
ci-dessus, sans qu'il soit nécessaire de reproduire le nom du champ.

## 13. Expert-comptable et identité — stress-test du modèle d'accès

Contraintes `STRUCTURAL_BEFORE_ACCESS_MODEL` identifiées (à représenter dès
que l'accès délégué est envisagé, **sans construire d'ACL complète
maintenant**) :

1. **Un expert-comptable n'est pas un salarié, et un compte externe n'est lié
   à un seul tenant que par accident, jamais par construction.** Il ne doit
   jamais être représenté par le même mécanisme que Personnel/Utilisateur
   interne (`08` §2 du Product Blueprint principal, distinction déjà actée
   entre personne physique dans l'entreprise et compte applicatif).
   **Correction apportée par une mission corrective ultérieure** : ce
   document ne décrète pas qu'un troisième type d'identité technique est
   nécessaire — c'est une décision de forme (modèle de données) prématurée à
   ce stade. Ce qui est requis, c'est une **capacité** : une relation de
   membership/délégation, **scopée par tenant**, entre un compte et un ou
   plusieurs tenants, portant son propre niveau de droit par relation (voir
   point 3). Que cette capacité se traduise en base par une troisième table
   d'identité, par une table de relation many-to-many sur les identités
   existantes, ou par toute autre forme, **reste une décision d'architecture
   future**, hors du périmètre de cette annexe.
2. **Un même compte peut intervenir sur plusieurs tenants**, confirmé comme
   pattern réel par les deux concurrents analysés : Axonaut (`/me { account:
   [...] }`, un utilisateur porte un tableau de comptes légaux distincts,
   `IMPLEMENTATION_EXAMPLE`) et Evoliz (séparation explicite `/companies`
   — dossiers gérés par un prescripteur — vs `/clients` — CRM interne à une
   entreprise, `IMPLEMENTATION_EXAMPLE`). Les deux éditeurs indépendants
   confirment la même architecture : ne pas modéliser l'accès expert-comptable
   comme une simple invitation d'utilisateur interne.
3. **Les droits peuvent différer par tenant** pour un même compte délégué —
   lecture seule chez l'un, configuration de connecteur chez l'autre. La
   relation compte-délégué↔tenant porte donc son propre niveau de droit,
   jamais un droit global fixé une fois pour toutes.
4. **Un accès en lecture/export seul doit être représentable sans exiger un
   accès complet** — ne pas forcer un modèle binaire (tout ou rien).

**Ce que ce stress-test ne fait pas** : il ne construit aucune ACL
universelle, aucune table de permissions fine, et **ne décrète aucune forme
de table précise**. Il établit seulement que le modèle d'identité doit
prévoir, dès sa conception (même si l'écran n'existe pas encore), la
**capacité** d'une relation de membership/délégation scopée par tenant,
distincte du mécanisme Personnel/Compte utilisateur interne déjà acté —
cohérent avec la mise en garde déjà posée par `11` P12 du Product Blueprint
principal (ne pas sur-architecturer les permissions en V1, mais ne pas
fermer la porte à une extension).

## Ce que ce document ne fait pas

Ne construit aucune des trois capacités. Ne choisit aucun format d'export ni
aucun connecteur nommé. Ne crée aucune ACL. Classement de version complet en
`06` §15.
