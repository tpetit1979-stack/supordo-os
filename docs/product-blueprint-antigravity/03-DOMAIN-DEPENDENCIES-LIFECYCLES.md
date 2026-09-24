# 03 — Domain Objects, Dependencies & Lifecycles

Objets métier fondamentaux, états, transitions, dépendances, propagations,
invariants, effet domino. **Aucun schéma SQL, aucune table, aucune migration** —
uniquement le niveau conceptuel qui alimente `08-BACKEND-AND-NONFUNCTIONAL-CONTRACT.md`.

Sources primaires : `0007-contraintes-acquises.md` (intégral), `functional-devis-
3a/3b/3c` + `SUPORDO-CONTRAT-FONCTIONNEL-DEVIS-V0.md` (devis), `functional-
onboarding-pilot.md` et `functional-propagation-pilot.md` (156 règles de
propagation, 97 verrous, 6 invariants candidats — autres objets).

## Taxonomie de dépendance (mission §8)

`HARD` (sans A, B ne fonctionne pas) · `STRUCTURAL` (B peut exister sans A mais
l'ajouter tard coûte cher ou casse la cohérence) · `LEGAL_GATE` (contrainte
réglementaire) · `SOFT` (confort/UX) · `OPTIONAL` (pas de dépendance réelle) ·
`OPEN` (la relation elle-même dépend d'une décision non prise).

## Taxonomie de propagation

copiée · snapshottée · référence vivante · recalculée · héritée · `INDETERMINE`
(le corpus ne permet pas de savoir — ne jamais deviner).

---

## 1. Fiches objets

### Devis
- **Responsabilité** : document commercial pivot entre client et exécution/facturation. Objet le mieux documenté du corpus (8 corpus dédiés, missions 3A/3B/3C).
- **Naissance** : sans parent nécessaire (`SUPORDO_DECISION` S2). Client créable à la volée (`MARKET_BASELINE` 8/8, aucun contre-exemple). Élément de catalogue "créable à la volée" annoncé 8/8 mais sémantique non tranchée — sélectionner ≠ créer ≠ ligne libre ≠ convertir (`OPEN`, question O1/O2 de 0007). État initial "brouillon" robuste chez 2/8 corpus seulement.
- **États** : cinq modèles de verrouillage distincts coexistent au moment de l'acceptation/signature (`VARIANTE DE MARCHÉ`, `OPEN` — O3). Machine candidate observée chez InterFast : Brouillon → Finalisé → Envoyé → Accepté/Signé → Facturé/Chantier. Génération PDF/impression sans effet d'état (5 éditeurs, aucun contre-exemple). L'envoi seul ne verrouille rien (3 éditeurs explicites).
- **Parents** : Client [`SOFT`/`STRUCTURAL` — obligatoire chez OpenFire seul (blocage documenté), facultatif ailleurs] ; Catalogue [`OPEN`, dépend de l'arbitrage O1 sur la ligne libre].
- **Enfants** : Facture (transformation ordinaire) [`STRUCTURAL`, **trou documentaire majeur** — seulement 3/7 éditeurs documentent le mode, aucun ne tranche copié vs référencé] ; Facture d'acompte [`STRUCTURAL`, 4 éditeurs] ; Chantier [`STRUCTURAL` chez les BTP spécialistes (Vertuoza, InterFast, Obat, Costructor), `OPTIONAL`/absent chez les généralistes (Axonaut, Sellsy — absence confirmée, pas un silence)] ; Intervention [`OPEN` — le sens même de la relation varie par éditeur ; OpenFire (Zendesk et Odoo) documente le sens **inverse** (intervention/étude → devis)] ; Avenant [`STRUCTURAL`, additif jamais remplacement, 3/3 de ceux qui le documentent].
- **Propagation** : catalogue → devis, prix **snapshotté** (Obat, source unique, cohérent avec S3) ; devis → chantier, coordonnées de facturation **snapshottées non rétroactives**, nom du chantier **référencé rétroactivement** (Vertuoza — deux modes différents sur le même flux) ; devis → facture, client/produits/montants/taxes **copiés** (4 éditeurs) ; retenue de garantie **reportée** (Costructor, OpenFire) mais **non propagée chez Vertuoza — anomalie confirmée, pas une hypothèse**.
- **Invariants** : un devis produit 1→N objets aval du même type, jamais 1→1 (6+ éditeurs) ; le devis change d'état à sa **première** sortie structurante, pas à l'envoi, pas à la signature seule (7/8) ; le devis reste consultable après transformation (6/8, aucun contre-exemple).
- **Événements structurants** : signature = acceptation ou deux événements distincts (`OPEN` O2, 2 éditeurs séparent / 4 fusionnent, **aucune contrainte légale**) ; verrou de mutabilité (`OPEN` O3, 5 modèles, **aucune cause réglementaire sur le devis, dans aucun des 8 corpus** — contraste net avec la facture).
- **Preuve globale** : la plus forte du corpus sur un objet unique.

### Client
- **Responsabilité** : `NON DÉTERMINÉ` en détail — le corpus documente ses effets, jamais son modèle propre.
- **Naissance** : sans parent, y compris à la volée pendant la création d'un devis (Axonaut, OpenFire). Cohérent avec S2.
- **États** : `NON DÉTERMINÉ`.
- **Parents** : aucun — objet racine.
- **Enfants** : Devis [`HARD` chez OpenFire (blocage documenté), `SOFT`/`OPTIONAL` ailleurs] ; compte de tiers comptable [`STRUCTURAL`, généré "dès qu'un événement comptable intervient", OpenFire] ; condition particulière [`OPTIONAL`, copiée vers le devis, surchargeable, Vertuoza].
- **Propagation** : position fiscale du contact → devis, **héritée** ("appliquée par défaut", OpenFire).
- **Invariants** : aucun formalisé.
- **Preuve globale** : faible-moyenne (2/6 éditeurs sur la naissance à la volée).

### Lieu
- **Responsabilité** : `SUPORDO_DECISION` (S1) — distinct du client, survit au changement de propriétaire/locataire/payeur. L'historique d'intervention s'y rattache. **Ce n'est pas une observation des pilotes fonctionnels lus** : ils ne traitent quasiment jamais le lieu comme objet autonome.
- **Naissance / États / Parents / Enfants / Propagation / Invariants** : `NON DÉTERMINÉ` dans les sources fonctionnelles disponibles. Point le plus proche observé : OpenFire Odoo documente un "site d'intervention" porteur d'un parc installé repris automatiquement en ligne de contrat — structure propre à ce seul éditeur, non généralisable.
- **Preuve globale** : quasi nulle en dehors de 0007 lui-même — la décision S1 doit rester la référence, pas une lecture corpus supplémentaire.

### Catalogue / Article
- **Responsabilité** : porteur de prix et de caractéristiques réutilisables sur les documents commerciaux.
- **Naissance** : asymétrie documentée — OpenFire permet la création à la volée du contact mais **pas** du produit (recherche uniquement). Sémantique non tranchée (`OPEN`, M2/0007).
- **Parents** : plan comptable [`STRUCTURAL` chez Costructor] ; réglage stock global [`STRUCTURAL` avant activation du stock par produit] ; taux de marge défini [`SOFT`].
- **Enfants** : ligne de devis/facture [prix **snapshotté**, S3] ; stock [`HARD`, décrémenté/incrémenté automatiquement, InterFast + Axonaut].
- **Propagation** : **snapshottée** à la création du document (Obat, cohérent avec S3) ; **référence vivante** pour un article synchronisé quotidiennement depuis un fournisseur externe (Vertuoza, CEBEO) — **coexistence de deux modes selon la source du catalogue, jamais réconciliée par le corpus**.
- **Événements structurants** : marge par défaut modifiée → n'affecte les prix existants que si la marge de l'élément égalait l'ancien taux (ProGBat, non-rétroactivité conditionnelle).
- **Preuve globale** : moyenne sur la naissance, faible sur le mode de propagation exact (1 source explicite pour snapshot).

### Chantier / Intervention
- **Responsabilité** : point d'agrégation et de recalcul (rentabilité), jamais un objet à saisie directe de valeurs financières.
- **Naissance** : sans parent requis (S2 couvre l'intervention explicitement).
- **États** : partiellement documentés — statut "Terminé" déclenche décrément de stock (InterFast) et verrouille le rapport d'intervention (cause métier : "garantir l'intégrité du rapport signé").
- **Parents** : Devis [`SOFT`/`OPTIONAL` en général ; chez InterFast, si intervention liée à un devis, **le devis prime** sur le rapport pour la facturation — `HARD` dans ce cas précis, 1 source].
- **Enfants** : Facture [voir propagation] ; rentabilité chantier [`STRUCTURAL`, recalculée jamais saisie, **3 éditeurs indépendants, aucun contre-exemple** — c'est l'invariant candidat le mieux corroboré après ceux du devis].
- **Propagation vers Facture** : InterFast — **copiée** (surchargeable) ; numéro d'intervention/chantier **référencé** (non surchargeable). Vertuoza — mode exact `NON DÉTERMINÉ`.
- **Propagation vers Rentabilité** : devis (montants prévus), factures de vente, factures d'achat, temps travaillé — tous **recalculés** en cascade, jamais saisis (Costructor, Vertuoza, InterFast).
- **Preuve globale** : moyenne sur le mécanisme de rentabilité (3/7 convergents) ; **faible-nulle sur l'objet lui-même** (naissance, états génériques) — confirme l'avertissement déjà connu du `PROTOCOLE-AUDIT-FONCTIONNEL.md` §8 : « le corpus n'aidera pas » sur cet objet.

### Facture
- **Responsabilité** : document comptable définitif, régime le plus contraint légalement de tout le domaine.
- **Naissance** : depuis un devis (mode `NON DÉTERMINÉ`, voir ci-dessus) ; depuis une intervention (InterFast, copiée) ; de façon autonome (`NON DÉTERMINÉ`).
- **États** : Brouillon → numérotée/validée (irréversible, cause métier + légale combinées, Sellsy).
- **Parents** : Devis [`STRUCTURAL`, trou documentaire majeur] ; Intervention [`STRUCTURAL` chez InterFast] ; Contrat/ligne de contrat [`LEGAL_GATE` partielle, OpenFire Odoo seul].
- **Enfants** : Avoir [`HARD`, seul véhicule de correction documenté, 6/7 éditeurs, aucune alternative] ; écriture comptable [`STRUCTURAL`, recalculée] ; statut de paiement [`SOFT`, mis à jour par rapprochement].
- **Propagation** : depuis facture d'acompte/situation vers facture finale — **recalculée**, jamais ressaisie (4 éditeurs indépendants — **le couple le plus densément corroboré du corpus entier**, cohérent avec M8/INV-3C-1 côté devis).
- **Invariants** : une facture numérotée est **inaltérable**, correction uniquement par avoir (6/7 éditeurs, `LEGAL_CITÉ` L1/0007, Art. L.441-9 cité par Sellsy, **jamais vérifié à la source officielle**) ; acompte/situation déduit automatiquement, jamais ressaisi (4/7).
- **Événements structurants** : numérotation = verrou terminal (L1, L3/0007). **Exception documentaire notable** : aucun des 25 documents Vertuoza lus ne mentionne de verrou réglementaire sur la facture — silence signalé comme résultat en soi, pas une infirmation.
- **Preuve globale** : très forte sur l'irréversibilité ; forte sur la déduction acompte→solde ; **faible-nulle sur le mode exact de la transformation devis→facture ordinaire — le cas le plus fréquent est aussi le moins documenté**.
- **Cas particulier — facture importée** (`SUPORDO_DECISION` L4/0007, à vérifier directement dans 0007, pas par un résumé antérieur) : une facture historique reprise d'un autre logiciel lors de l'onboarding **n'est jamais assimilée à une facture émise par SUPORDO**. Ce que cela n'interdit pas : importer numéro, date, montant, PDF, client, rattachement, état de paiement, avec `provenance = système précédent`. ProGBat interdit l'import de factures dans son centre d'aide, mais rien n'établit une interdiction générale — 0007 le lit comme un choix éditeur, pas une contrainte de marché, et rappelle explicitement que la migration d'historique reste un levier commercial.

### Avoir
- **Responsabilité** : unique véhicule de correction d'une facture finalisée.
- **Naissance** : depuis une facture, jamais de façon autonome.
- **États** : partiel (éditable) → total/finalisé (verrou terminal, même régime que la facture).
- **Parents** : Facture [`HARD`, 6/7 éditeurs].
- **Enfants** : aucun — objet terminal (« l'irréversibilité ne s'arrête pas à la facture d'origine : l'avoir devient à son tour inaltérable dès qu'il reçoit lui-même un numéro »).
- **Propagation** : **copiée** depuis la facture, surchargeable avant finalisation (Costructor, Sellsy, InterFast, Obat) ; **référence vivante** chez Axonaut (lien plutôt que copie) — **OpenFire Odoo est seul à ne rien documenter** sur ce point.
- **Invariants** : copie le contenu de la facture visée (5/7) ; devient lui-même inaltérable une fois numéroté (3 formulations explicites, aucun contre-exemple) — `LEGAL_CITÉ` L2/0007.
- **Preuve globale** : forte (5-6/7 convergents), un seul angle mort (OpenFire Odoo).

### Paiement
- **Responsabilité** : `NON DÉTERMINÉ` en détail — traité uniquement comme déclencheur d'un changement de statut de facture.
- **Parents** : compte bancaire (synchronisation) [`STRUCTURAL` chez Vertuoza] ; facture.
- **Enfants** : statut de facture [`HARD`, "payé" recalculé après rapprochement, Vertuoza + OpenFire Odoo] ; écriture comptable [`STRUCTURAL`, OpenFire Odoo].
- **Propagation** : montant dû → **recalculé** à chaque paiement lié (OpenFire Odoo).
- **Preuve globale** : faible — jamais modélisé en tant qu'objet autonome (naissance, méthodes, états).

### Document / Photo
- **Responsabilité** : `NON DÉTERMINÉ` comme objet autonome dans les pilotes lus. Le consentement média (S5, `SUPORDO_DECISION`) n'est pas une observation de ces pilotes — c'est une décision PO indépendante, portant uniquement sur les médias publiables.
- **Propagation observée** : document (devis/BC/facture) → PDF joint, **snapshotté** à l'instant T (OpenFire Odoo) ; rapport de situation → facture de situation, **snapshotté**, non ré-imprimable ensuite car le rapport source lui-même n'est pas conservé (**trou technique documenté**, 1 source).
- **Preuve globale** : quasi nulle — un seul éditeur, aucune corroboration croisée. La photo terrain proprement dite est absente des deux pilotes fonctionnels transversaux ; elle réapparaît uniquement dans `functional-devis-3c-sorties.md` (parcours 2, voir `04`).

### Personnel / Utilisateur
- **Responsabilité** : deux objets distincts chez au moins deux éditeurs — fiche RH (personnel) vs accès applicatif (compte utilisateur). Correspond à M14/0007.
- **Naissance** : Vertuoza impose un ordre strict et explicite (personnel → compte utilisateur). Axonaut distingue les deux sans dépendance d'ordre aussi stricte.
- **Parents** : paramétrage essentiel [`HARD` chez Vertuoza].
- **Enfants** : rôle/droits [`HARD`, un utilisateur doit exister avant qu'un rôle lui soit attribué] ; rentabilité de chantier [`SOFT`, le taux horaire influence le calcul].
- **Propagation** : utilisateur désactivé → éléments créés **réinitialisés** avec réattribution aléatoire (Axonaut, 1 source, cas isolé) ; utilisateur archivé avec licence non consommée → **recalculé** en crédit d'abonnement, non remboursable (InterFast, 1 source).
- **Preuve globale** : moyenne sur la distinction personnel/utilisateur (2/6 éditeurs — 0007 signale déjà cette preuve comme faible).

---

## 2. Graphe de dépendances

```mermaid
graph LR
  Client -->|SOFT/STRUCTURAL| Devis
  Client -->|STRUCTURAL| CompteTiers["Compte de tiers comptable"]
  Catalogue -->|"HARD, snapshot (S3)"| Devis
  Devis -->|"STRUCTURAL, trou documentaire majeur"| Facture
  Devis -->|STRUCTURAL| FactureAcompte["Facture d'acompte"]
  FactureAcompte -->|"HARD, recalcul"| FactureSolde["Facture de solde/finale"]
  Facture -->|"HARD, LEGAL_GATE L1/L2"| Avoir
  Devis -->|"STRUCTURAL (specialistes BTP), OPTIONAL (generalistes)"| Chantier
  Devis -.->|"OPEN — sens contesté"| Intervention
  Intervention -.->|"OPEN — OpenFire documente l'inverse"| Devis
  Devis -->|STRUCTURAL| Avenant
  Chantier -->|"HARD, recalcul (3 editeurs)"| Rentabilite["Rentabilité chantier"]
  Facture -->|HARD| Rentabilite
  Intervention -->|"HARD si lié (InterFast, 1 source)"| Facture
  Personnel -->|"HARD chez Vertuoza, OPEN ailleurs"| CompteUtilisateur["Compte utilisateur"]
  CompteUtilisateur -->|HARD| Role["Rôle / droits"]
  CompteBancaire["Compte bancaire"] -->|"SOFT, devient HARD au rapprochement"| StatutFacture["Statut de facture"]
  Lieu -.->|"S1 — structure non observée dans le corpus"| ParcInstalle["Parc installé (vertical, 02")]
```

Arêtes en pointillé (`-.->`) = relation dont l'existence ou le sens dépend d'une
décision non prise (`OPEN`) ou d'un objet quasi non documenté. Aucune arête ci-dessus
n'a été déduite d'un ordre de menu ou d'un ordre éditorial de documentation — les
cas repérés comme tels (ordre Entreprise/Équipe/Intégrations chez InterFast,
Paramétrage/Import chez ProGBat) ont été explicitement exclus.

## 3. Modes de propagation observés (synthèse transversale)

| Flux | Mode | Preuve |
|---|---|---|
| Catalogue → ligne de devis/facture | **snapshotté** | S3 (`SUPORDO_DECISION`), corroboré Obat |
| Catalogue externe synchronisé → ligne | **référence vivante** | Vertuoza (CEBEO), 1 source — coexiste avec le mode ci-dessus, jamais réconcilié |
| Devis → facture (acompte, situation) | **recalculé** | 4 éditeurs indépendants, aucun contre-exemple — le mécanisme le mieux corroboré du corpus |
| Devis → facture (ordinaire) | `INDETERMINE` (mode exact) | 3/7 éditeurs seulement documentent la transformation, aucun ne tranche |
| Devis → chantier (coordonnées facturation) | **snapshotté, non rétroactif** | Vertuoza |
| Devis → chantier (nom du chantier) | **référencé, rétroactif** | Vertuoza — deux modes différents sur le même flux |
| Facture → avoir (contenu) | **copié** (majorité) / **référence vivante** (Axonaut) | 5/7, un angle mort (OpenFire Odoo) |
| Retenue de garantie | **reportée** (Costructor, OpenFire) / **non propagée** (Vertuoza) | anomalie confirmée, pas une hypothèse |
| Client → devis (position fiscale) | **héritée** | OpenFire, 1 source |
| Intervention → facture | **copié** | InterFast, 1 source |
| Paiement → montant dû facture | **recalculé** | OpenFire Odoo |

**Règle de lecture** : `0007 §N` interdit explicitement de chercher le mode
technique exact (copie vs référence) au-delà de ce que les sources documentent — le
corpus décrit un comportement visible, jamais le stockage. Les cases `INDETERMINE`
ci-dessus le resteront après toute relecture supplémentaire du même corpus.

## 4. Effets domino les plus importants

Capacités dont une décision erronée ou tardive coûte cher à l'ensemble du produit
(mission §5) :

1. **S1 — Lieu distinct du client.** Si posé tard, casse la mémoire longue et le SAV
   sur tout objet déjà créé. `SUPORDO_DECISION`, déjà actée — aucune raison de la
   rouvrir, mais son implémentation doit être posée **dès la première migration**.
2. **S3 — Prix catalogue figé à la création.** Touche toute ligne de tout document
   commercial. Poser un mode "référence vivante" par défaut casserait l'historique
   dès le premier changement de prix catalogue.
3. **Le mode exact de la transformation devis → facture ordinaire.** C'est l'arête la
   plus fréquemment empruntée du graphe et la moins documentée. Une erreur ici
   (référence au lieu de copie, ou l'inverse) affecte directement l'irréversibilité
   légale de la facture (L1) — c'est une décision à prendre **avant le schéma**, pas
   après.
4. **Le sens de la relation devis ↔ intervention (`OPEN`).** Détermine l'architecture
   UX entière du parcours terrain (voir `04`) : partir du devis pour planifier, ou
   partir d'une visite/étude pour générer le devis. Le corpus documente les deux
   sens chez des éditeurs différents — ce n'est pas un détail d'implémentation, c'est
   une question de direction produit.
5. **S4 — Provenance ciblée.** Si l'architecture ne prévoit pas, dès le départ, un
   emplacement pour tracer la provenance d'un champ (IA, import, capture terrain)
   *lorsque cette provenance sert la validation, la sécurité ou la traçabilité*,
   l'ajouter après coup sur des données déjà en base est un chantier de migration
   lourd — et un système de data lineage universel serait, à l'inverse, une
   sur-ingénierie que S4 interdit explicitement.

## 5. Limites de ce document

- Les objets Lieu, Document/Photo et Paiement restent quasi non documentés comme
  objets autonomes — leur modèle conceptuel devra s'appuyer sur `02` (stress-test
  vertical) et une validation terrain, pas sur une relecture supplémentaire du
  corpus actuel.
- La cascade Contrat → Ligne de contrat → Demande d'intervention → RDV (parc
  installé, OpenFire Odoo) est une preuve à un seul témoin — utilisable comme
  référence structurelle pour concevoir le pack métier clim/chauffage, mais jamais
  comme standard de marché.
