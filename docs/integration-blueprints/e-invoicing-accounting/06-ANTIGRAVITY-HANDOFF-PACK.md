# 06 — Antigravity Handoff Pack

Point d'entrée unique pour Google Antigravity **au moment où** la tranche
e-invoicing/comptabilité est ouverte dans la séquence du Product Blueprint
principal — jamais avant. Condense `01`-`05`, ne les recopie pas.

**Ce fichier reste dormant.** Le gate `15-RED-TEAM-GATE.md` du Product
Blueprint principal a établi que `14-ANTIGRAVITY-OPERATING-PACK.md` seul
n'est plus une source d'exécution suffisante (conditions GO non satisfaites).
Ce document `06` ne doit **jamais** être transmis à Antigravity avec `14`
comme unique contrat d'exécution — avant tout usage réel, il devra être
réaligné sur la future **Canonical Execution Layer** (documents `16`-`19` du
Product Blueprint principal, non créés à ce jour, hors périmètre de cette
mission). Suit, une fois cet alignement fait, le protocole `OBSERVE → PLAN →
APPROBATION HUMAINE → IMPLEMENT → VERIFY → AUDIT INDÉPENDANT → TEST HUMAIN →
MERGE`.

## CONTEXT

SUPORDO facture des artisans français. La facture électronique B2B devient
obligatoire par étapes (réception : 01/09/2026, déjà en vigueur ; émission
PME/TPE : 01/09/2027 — `01` §0). Cette tranche construit la capacité de
transmettre une facture SUPORDO via une Plateforme Agréée, sans coupler le
domaine à un fournisseur ni à une version de format donnée.

## CANONICAL DOMAIN

Voir `01` intégralement. Résumé : Facture canonique = identité vendeur/
acheteur (lien + snapshot immuable à l'émission) + quatre concepts d'adresse
distincts (légale, lieu de prestation = Lieu SUPORDO en lien + snapshot,
livraison, routage) + lignes à un seul taux de TVA chacune (EN 16931 BT-151/
BT-152 — plusieurs taux possibles entre lignes, jamais sur une seule) +
ventilation TVA agrégée (BT-118/BT-119) + totaux + références croisées
directes (devis, facture précédente, avoir) + discriminant de régime (natif/
importé). `ElectronicInvoiceExchange` est un concept séparé
(`PLATFORM_CAPABILITY`), jamais fusionné au domaine Facture — tout
identifiant externe (`external_document_id`, `flow_id`, `tracking_id`) lui
appartient, jamais à la Facture.

## FRONTEND CONTRACT

Voir `02` intégralement. 12 états, chacun avec contexte/action/erreur
traduite/recovery. Aucun code technique brut jamais affiché à l'artisan.

## BACKEND CONTRACT

Voir `03` intégralement. Séparation stricte Domaine/Service e-invoicing/
Provider adapter. Aucun invariant réglementaire ou financier ne dépend
uniquement du frontend.

## INVARIANTS

- L1/L2/L3 (`0007`, déjà actés) s'appliquent sans exception à toute facture,
  qu'elle soit ou non transmise électroniquement.
- Une facture transmise et refusée/rejetée ne se corrige que par avoir **si
  les préconditions réelles le permettent** (`01` §4ter, §6 cas 6) — jamais
  par réécriture, et jamais une règle « refus ⇒ avoir » codée en automatisme
  aveugle.
- Le service respecte un graphe explicite de transitions autorisées ;
  événements dupliqués ignorés sans effet, événements obsolètes journalisés
  jamais appliqués, état jamais corrompu par l'ordre d'arrivée réseau (`01`
  §4ter — remplace l'ancienne formule trop simple « ne régresse jamais »).
- Aucun nom de provider n'apparaît dans une entité du domaine (`01` §1, §7).
- Aucune version de format n'est codée comme invariant métier (`01` §3).

## EXTERNAL BOUNDARIES

Provider adapter = frontière stricte. Tout ce qui touche une Plateforme
Agréée, un connecteur comptable ou un annuaire passe par cette couche — jamais
d'appel direct depuis le domaine ou le frontend (`03` §1).

## ERROR MODEL

Deux catégories distinctes, jamais fusionnées : erreurs de **validation**
(détectées avant soumission, corrigibles par l'utilisateur) et erreurs
**d'échange** (survenant après soumission, gérées par la matrice `01` §6).
Chaque erreur porte un code technique interne ET une traduction en langage
métier (`02`) — jamais l'un sans l'autre.

## IDEMPOTENCY

Voir `01` §6 (matrice complète, 10 cas) et `03` §3. Clé d'idempotence générée
côté SUPORDO, jamais confiée au provider. Aucun des deux concurrents analysés
n'a résolu ce point — SUPORDO le construit sans référence externe.

## SECURITY / RLS

Isolation tenant stricte sur `ElectronicInvoiceExchange`, mapping comptable
et accès délégué expert-comptable (`03` §7, `04` §13). Secrets provider
jamais exposés au frontend (`03` §8). Voir aussi la correction B2/B3 du gate
`15-RED-TEAM-GATE.md` du Product Blueprint principal — la même rigueur RLS
s'applique ici, sans exception pour cette tranche.

## ACCEPTANCE TESTS / NEGATIVE TESTS

Voir `05` intégralement — 7 catégories (Canonical Data, Immutability,
Idempotency, Provider Failure, Security, Recovery, Format).

## OUT OF SCOPE (cette annexe entière)

- Le V1 du Product Blueprint principal — cette tranche n'y est **pas**
  ajoutée, quelle que soit la facilité apparente de le faire.
- Tout code, SQL, migration, projet Supabase.
- Tout choix de Plateforme Agréée nommée.
- Les extensions BTP (§15 ci-dessous).

## OPEN QUESTIONS (reprises de `01` §5, liste fermée)

1. Libellés français exacts des statuts de cycle de vie réglementaires (base
   normative identifiée : AFNOR XP Z12-012/013/014, non consultée en détail
   — piste non vérifiée : codes CDV 202/210/212 cités par Evoliz v1.56 comme
   « définis par la spécification DGFiP », `IMPLEMENTATION_EXAMPLE` seulement,
   `01` §4bis).
2. Délai et format exact des données de paiement en e-reporting.
3. Articulation précise Chorus Pro (B2G) ↔ dispositif B2B.
4. Mécanisme fin d'adressage au-delà du principe SIREN-pivot.
5. Montant actuel de l'indemnité forfaitaire de recouvrement et du taux
   d'escompte (traditionnellement 40 €, non revérifié dans cette recherche).

**Ne jamais combler ces `OPEN` avec une valeur tirée d'Evoliz ou d'Axonaut.**

## REAL / PROTOTYPE / MOCK policy

Reprend telle quelle la discipline de `14-ANTIGRAVITY-OPERATING-PACK.md` §16-17
du Product Blueprint principal. Application spécifique à cette tranche : tant
que l'intégration avec une vraie Plateforme Agréée n'est pas construite et
testée, **aucune interface ne doit afficher un badge « facture électronique
conforme »** — l'interface abstraite posée en T4 du blueprint principal (`06`
§2 de `docs/product-blueprint-antigravity`) reste `NOT_IMPLEMENTED` jusqu'à
preuve du contraire.

## 15. Minimum Now / Later

Classement pour éviter la sur-architecture — **le premier pilote métier V1
(verticale encore à décider par le PO, Q7 du Product Blueprint principal)
n'est alourdi par aucun de ces éléments.**

### STRUCTURAL_NOW
*(doit être représentable dans le schéma Facture dès sa conception en T4 du
blueprint principal, même sans e-invoicing réelle — coût de report élevé)*

1. Discriminant de régime natif/importé sur la Facture (`L4`).
2. Verrouillage générique (capable de servir à la fois l'immuabilité légale
   L1 et un futur verrou de transmission).
3. Quatre concepts d'adresse distincts, non fusionnés (`01` §2.1).
4. **Corrigé** : un seul taux de TVA par ligne (EN 16931 BT-151/BT-152,
   `01` §2.4) — la multiplicité se joue entre lignes, jamais au sein d'une
   ligne.
5. Références croisées directes (devis, facture précédente, avoir) en FK,
   jamais en lookup indirect.
6. Devise + montant comme paire typée.
7. Séquence de numérotation garantie au niveau base (déjà signalé B9 du gate
   `15` du blueprint principal).
8. Deux axes de statut orthogonaux : commercial (déjà existant) et futur
   statut de transmission — jamais fusionnés, même avant que le second existe.
9. **Retiré** (correction) : aucun champ de corrélation externe n'est justifié
   sur la Facture elle-même — `external_document_id`, `flow_id`, `tracking_id`
   appartiennent tous à `ElectronicInvoiceExchange` par défaut (`01` §4,
   §4bis). Un champ de corrélation strictement interne à SUPORDO, sans lien
   avec l'e-invoicing, resterait envisageable mais n'a aucune justification
   trouvée dans cette recherche — à ne poser que si un besoin réel émerge
   ailleurs, hors périmètre de cette annexe.
10. Confirmation que S4 (provenance ciblée, déjà acté) couvre bien le cas
    d'une donnée transmise à un tiers/l'administration — aucun nouveau
    mécanisme, juste une application confirmée.
11. Lien métier + snapshot immuable coexistants pour Lieu et pour l'identité
    Seller/Buyer (`01` §2.1, corrigé — ni l'un ni l'autre seul ne suffit).

### T4 = BUILD_WITH_INVOICE_SLICE (T4 du blueprint principal)
Population réelle des champs canoniques (identité, mentions obligatoires),
facture directe simple (un devis → une facture) —
`ElectronicInvoiceExchange` reste vide/non utilisé à ce stade. Correspond
strictement aux points `STRUCTURAL_NOW` ci-dessus, appliqués une première
fois.

### T5 = acomptes / factures de situation
Le triptyque acompte/situation/solde (`deposit_type` 1/2/3 observé chez
Axonaut, `advance_deduction_mode` chez Evoliz, §2.8 de `01`) est déjà
`ACQUIS DOCUMENTAIRE` dans le Product Blueprint principal (`12`). **Ce que
`T5` ajoute au-delà de `T4`** : plusieurs factures liées au même devis
(chaîne acompte→solde, référence croisée `01` §2.7), déduction automatique
des acomptes déjà facturés du solde restant dû (`01` §2.5). **Ce qui reste
`DO_NOT_BUILD_YET`** : la facturation de situation/avancement au sens BTP
complet (courbe d'avancement, retenue de garantie) — voir ci-dessous, ce
n'est pas la même chose qu'un simple acompte/solde.

### T-AVOIR = correction d'une facture émise
Lien bidirectionnel direct Facture↔Avoir (`01` §2.7, jamais un lookup
indirect comme Evoliz), régime d'immuabilité hérité dès numérotation (L2),
et surtout la matrice de recovery `01` §4ter/§6 cas 6 : un avoir n'est
**jamais** proposé automatiquement sur un simple statut « refusé » — les
préconditions réelles doivent être vérifiées (cas documenté chez Evoliz
v1.56 où l'avoir lui-même peut être bloqué). Avoir total au minimum ; avoir
partiel reste `DO_NOT_BUILD_YET`.

### BUILD_WITH_EINVOICING_SLICE (FUTURE_EINVOICING)
`ElectronicInvoiceExchange` réel, format mapper, provider adapter, résolution
d'annuaire, machinerie de retry/idempotence, les 12 états frontend de `02`.
Peut être **préparé architecturalement dès T4** (les points `STRUCTURAL_NOW`
ci-dessus) sans être construit avant que la tranche e-invoicing soit
explicitement ouverte.

### LATER_ACCOUNTING
Export FEC, mapping comptable (§12 de `04`), connecteur, accès délégué
expert-comptable.

### DO_NOT_BUILD_YET
Facturation de situation/avancement complète (courbe d'avancement),
retenue de garantie, primes post-TVA (CEE/MaPrimeRénov'), réception de
factures fournisseurs entrantes (pattern « bintray »), multi-devises,
intégration Chorus Pro B2G, avoir partiel — besoins réels (`ANALYSIS`,
confirmés par Evoliz) mais non justifiés pour le premier pilote.

### Note de re-vérification (mission de consolidation T4)
Les deux fichiers sources `api-evolizdocs.txt` (confirmé **Evoliz v1.43**,
zéro occurrence e-invoicing — cohérent avec §0) et `api axonaut.md`
(Axonaut v2.0.0) ont été re-fournis et re-vérifiés à cette occasion :
aucun fait nouveau, les deux fichiers sont identiques à ceux déjà analysés
en profondeur dans `01`. Un objet **`Contract`** (nommé « Order » dans sa
propre description) a été identifié chez Axonaut — pivot optionnel entre
Devis et Facture(s), porteur de `generate_and_send_recurring_invoices`,
`invoice_frequency_in_months`, `first_invoice_planned_date` — pertinent
comme `REFERENCE` pour l'arbitrage encore `OPEN` **O4/Q4** du Product
Blueprint principal (objet pivot vs transformation directe), **jamais une
preuve qu'un tel objet doit exister dans SUPORDO**. Détail complet et
analyse du pipeline commercial Axonaut (Opportunities/Pipes) :
`FUTURE_PRODUCT_INPUT`, hors périmètre de cette annexe (invoicing/
accounting), à ne pas construire ni même arbitrer ici.

## Ce que ce document ne fait pas

Ne remplace pas `01`-`05` — en cas de doute sur un point condensé ici,
retourner au document source cité. Ne démarre aucune implémentation.
