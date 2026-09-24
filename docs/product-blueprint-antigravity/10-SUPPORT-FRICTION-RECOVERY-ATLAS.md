# 10 — Support Friction & Recovery Atlas

Mining transversal des centres d'aide (hors `site_marketing/`, sauf mention
contraire) de 10 concurrents (extrabat, obat, batikko, sellsy, costructor,
vertuoza, axonaut, inter-fast, openfire×2, progbat). Objectif : où les logiciels
concurrents font-ils trébucher leurs utilisateurs, quelles erreurs deviennent
coûteuses ou irréversibles, quelles actions demandent aujourd'hui de lire une
page d'aide.

**Discipline de preuve (rappel strict)** : un centre d'aide documente une
**surface de complexité documentée**, jamais une mesure statistique d'usage ou
de douleur. Le nombre d'articles sur un sujet n'est ni une fréquence d'incident
ni une importance réelle pour l'utilisateur. Chaque friction ci-dessous porte son
niveau de preuve exact (nombre de sources indépendantes) — jamais gonflé.

**Méthode** : 4 lots de mining en parallèle (~150 fichiers lus intégralement sur
plusieurs milliers repérés par grep), taxonomie de frictions élaborée
progressivement (pas plaquée a priori), puis confrontation et déduplication par
le thread principal.

---

## 0. Corrections au blueprint existant (`01-09`), découvertes pendant le mining

**Ces fichiers ne sont pas modifiés.** Les corrections suivantes sont à traiter
comme des mises à jour de fait pour tout travail futur s'appuyant sur `01-09`.

### 0.1 La fumisterie a une preuve fonctionnelle documentaire réelle — pas seulement marketing

`01-CAPABILITY-MAP.md` §5 et `02-CORE-VERTICAL-BLUEPRINT.md` affirmaient qu'aucun
concurrent ne documente la fumisterie/poêles-cheminées dans son centre d'aide
(signal marketing seul chez OpenFire). **C'est inexact** : le centre d'aide
**OpenFire Odoo** (`documentation_2/`) documente une intégration catalogue
fabricant réelle — catégorie d'article native `POELE A BOIS`, et des
**connecteurs d'achat nommés** vers des fabricants réels de poêles/conduits
(Poujoulat, Modinox, Laudevco, Lorflex, Turbofonte), avec le même mécanisme que
pour le froid (demande de prix → commande fournisseur → confirmation manuelle).
Source : `importer-des-articles-ou-des-kits-160.md`,
`utiliser-les-connecteurs-d-achat-sur-openfire.md`.

**Conséquence pour `07` §0** : la recommandation de verticale de lancement
(climatisation/PAC/chauffage) reste défendable — climatisation/PAC/chauffage a
**deux** témoins indépendants (InterFast + OpenFire) contre **un seul**
(OpenFire) pour la fumisterie — mais l'écart de preuve entre les deux
verticales est **moins large** que ce que `01`/`02`/`07` affirmaient. Le tableau
de `09` Q7 doit être lu avec cette nuance.

### 0.2 Le système de rôles/permissions Obat contredit Q11 (`09`)

`09-DECISIONS-RISKS-ANTIGRAVITY-HANDOFF.md` Q11 jugeait la preuve sur les
rôles/permissions « faible (5/10), jamais détaillée ». **Obat documente en
réalité 7 rôles avec permissions individuelles activables/désactivables par
utilisateur** (pas seulement par rôle fixe) — `multi-user-les-differents-
roles-et-acces.md`. C'est le système de permissions le plus détaillé de tout le
corpus connu à ce jour. La `RECOMMANDATION ANALYTIQUE` de Q11 (« rôles minimaux »)
reste défendable pour un V1 pilote, mais ne doit plus être justifiée par
« absence de preuve de marché » — la preuve existe, elle est simplement portée
par un seul témoin.

### 0.3 Le devis vocal a maintenant une preuve `ACQUIS DOCUMENTAIRE`, pas seulement `MARKETING_ONLY`

`05-AI-AND-AUTOMATION-BLUEPRINT.md` ne disposait que de revendications marketing
(Vertuoza, Batikko) pour la thèse voix→devis. **Le centre d'aide Obat** (pas son
site marketing) documente un pipeline réel : voix/texte/document → pré-devis
généré (bibliothèque interne ou chiffrage IA) → **validation humaine obligatoire
avant enregistrement** (`dictez-vos-devis-depuis-obat-grace-a-notre-assistant-
vocal.md`). C'est une troisième preuve fonctionnelle réelle du modèle « l'IA
fait le brouillon, l'humain valide », aux côtés d'InterFast et OpenFire Zendesk
déjà connus de `04`/`05` — mais celle-ci porte spécifiquement sur la **voix**,
pas seulement sur le relevé structuré. Renforce directement la thèse centrale de
`05` §9.

### 0.4 Tension non résolue sur L4/0007 (facture importée) — nécessite vérification légale

`0007` L4 lit l'interdiction ProGBat d'importer des factures historiques comme
« un choix éditeur, rien n'établit une interdiction générale ». **ProGBat
lui-même revendique une base légale précise** (« loi de finance 2016 ») dans son
propre centre d'aide (`poursuivre-la-facturation-faite-sur-mon-ancien-
logiciel.md`). Ni `0007` ni ce mining ne permettent de vérifier cette citation
à une source officielle. **Ne pas trancher** — ajouté au registre `09` Q12/Q13
(`LEGAL_VERIFICATION_REQUIRED`) comme point de vérification supplémentaire,
sans modifier le statut déjà acté de L4 (`SUPORDO_DECISION`, qui porte sur ce
que SUPORDO fait, pas sur ce que ProGBat est légalement obligé de faire).

### 0.5 Un troisième niveau d'irréversibilité, non couvert par `08`/`09` : la bascule de conformité au niveau du compte entier

`08` et `09` traitent l'irréversibilité au niveau du **document** (facture
numérotée, avoir finalisé). Le mining révèle un niveau supplémentaire, non
couvert : une **bascule de configuration au niveau du compte entier**,
irréversible, activée pour raison réglementaire. Exemples : Sellsy
« Mode conforme » (« ni l'utilisateur ni Sellsy ne peuvent la désactiver
ensuite ») ; migration de plateforme de facturation électronique chez Obat/
ProGBat. **Nouveau constat à ajouter à `08` §7 (audit) sans le modifier ici** :
toute bascule de ce type doit être présentée à l'utilisateur comme un moment de
décision solennel (confirmation explicite, pas un simple article d'aide après
coup), pas comme un réglage ordinaire — voir `11` principe P-CONFORMITE.

---

## 1. Taxonomie transversale unifiée (19 motifs)

Construite par fusion des 4 taxonomies provisoires indépendantes des forks —
aucun motif forcé, plusieurs sont apparus dans un seul lot et restent isolés
tels quels.

| # | Motif | Corroboration (concurrents indépendants) | Nature |
|---|---|---|---|
| M1 | Correction obligatoire par objet secondaire (avoir/avenant/contrepassation), jamais par édition directe | **9/10** — quasi universel | Négatif (contrainte structurante) |
| M2 | Verrou irréversible mal signalé en amont (violation du principe EXPLAIN) | 6/10 | Négatif |
| M3 | Dépendance cachée entre objets liés, non affichée au moment de l'échec | 7/10 | Négatif |
| M4 | Suppression jamais réelle — soft-delete généralisé, toujours un statut réversible | **5/10 indépendants** (extrabat, obat, batikko, vertuoza, sellsy en partie) | **Positif** — motif le mieux corroboré du corpus entier |
| M5 | Synchronisation externe fragile ou asymétrique (comptabilité/banque/déchets/Peppol/multi-entités) | 5/10 | Négatif |
| M6 | Ressaisie forcée malgré import/migration, parfois contredisant la promesse marketing du même article | 4/10 | Négatif |
| M7 | Propagation non automatique entre objets pourtant liés | 3/10 | Négatif |
| M8 | Configuration préalable lourde et distribuée avant une première action | 2/10 (mais preuve dense) | Négatif |
| M9 | Permission grossière (menu entier, pas sous-section) | 2/10, **contrasté par un contre-exemple riche (Obat)** | Négatif/mixte |
| M10 | Récupération de compte = destruction (pas de vrai reset) | 1/10, isolé mais frappant | Négatif |
| M11 | Mobile ≠ desktop (capacités/droits différents) | 3/10 | Négatif |
| M12 | IA = brouillon, jamais finalisé sans validation humaine explicite | **3/10 `ACQUIS DOCUMENTAIRE`** (InterFast, OpenFire Zendesk, Obat) + 2 `MARKETING_ONLY` | **Positif** |
| M13 | Bascule de conformité irréversible au niveau du **compte**, pas du document | 2/10 (Sellsy, Obat/ProGBat) | Négatif, motif nouveau |
| M14 | Contournement recommandé par l'éditeur qui peut lui-même introduire un nouveau bug | 2/10 | Négatif |
| M15 | Scellement/preuve juridique tiers qualifié pour la photo terrain | 2/10 indépendants (Obat/Certificall, Batikko/Certigna) | **Positif** |
| M16 | Réglementation qui rend le produit progressivement plus strict, jamais plus permissif | 1/10, isolé | Neutre (signal d'anticipation) |
| M17 | Capture terrain conçue offline-tolerant, synchronisation différée | 3/10 indépendants | **Positif** |
| M18 | État dérivé incohérent avec l'état réel affiché à l'utilisateur | 1/10, isolé | Négatif |
| M19 | Incohérence interne produit (traitement différent d'objets similaires) | 1/10, isolé | Signal de dette, pas un modèle |

---

## 2. Détail des motifs les plus significatifs

### M1 — Correction par objet secondaire (9/10 concurrents)

Le motif le plus universel et le mieux corroboré du corpus après M4. Confirme
directement L1/L2 (`0007`) mais l'étend à des objets non couverts par `0007` :
avenant (Costructor : pas d'objet dédié, création manuelle + import de lignes),
feuille d'heures (Costructor : verrouillée après validation, correction par
refus motivé + re-soumission), rapport d'intervention signé (Vertuoza :
verrouillage total, **aucun contournement documenté**).

**Exemple le plus grave du corpus** — Vertuoza, `modifier-la-reference-d-une-
facture-deja-comptabilisee` : une fois une facture comptabilisée, la
modification est **impossible dans l'outil**, et **la solution officielle du
support est d'éditer le PDF via un outil externe (ChatGPT ou un lecteur PDF)**.
C'est l'exemple le plus net du corpus d'un produit qui, faute d'un mécanisme de
correction adapté, pousse l'utilisateur vers une pratique dangereuse pour
l'intégrité d'une pièce comptable. Preuve : 1 source, mais le motif général
(M1) est corroboré 9/10.

### M2 — Verrou irréversible mal signalé (6/10)

- **ProGBat**, `annuler-ou-modifier-une-facture.md` : impossible de dater un
  avoir avant la date de la dernière facture émise — **contrainte de séquence
  temporelle globale**, pas seulement un verrou sur le document visé. Plus
  stricte que le principe L1/L2 déjà connu.
- **Costructor**, `comment-masquer-le-numero-de-revision` : modifier un devis
  déjà signé oblige à le refaire signer, sans cause affichée dans le flux.
- **Sellsy**, `creer-et-gerer-des-declinaisons-de-mes-produits` : activer les
  déclinaisons produit est **irréversible** — impossible d'ajouter une nouvelle
  dimension après coup, le produit parent devient inutilisable.

### M3 — Dépendance cachée entre objets liés (7/10)

- **InterFast**, BSFF/facture de solde : impossible de créer un avoir sur une
  facture d'acompte si la facture de solde associée n'est pas d'abord annulée.
- **OpenFire Odoo**, paiement : modifier un paiement déjà remis en banque ou
  lettré exige de défaire la remise / dé-lettrer **dans le bon ordre**, deux
  préconditions distinctes non affichées ensemble.
- **Obat**, avoir : un avoir détaillé est **impossible si un acompte a déjà été
  facturé** — dépendance jamais expliquée en amont, seulement découverte à
  l'échec.
- **Extrabat**, IBAN : certains modèles de documents personnalisés ont l'IBAN
  **codé en dur dans le template**, invisible depuis l'interface standard —
  correction possible uniquement via ticket support. Risque financier direct
  (paiement vers un ancien compte).

### M4 — Soft-delete généralisé (5/10 indépendants, motif positif le mieux prouvé)

Aucun des concurrents mining n'a documenté de suppression dure sur un objet
métier central (client, chantier, facture brouillon) — toujours un statut
réversible (Corbeille, archivage, désactivation) :
- Extrabat : client "Corbeille" réversible en un clic.
- Obat : statut Corbeille équivalent.
- Batikko : chantier archivé, **« restaurable même 10 ans après »**.
- Vertuoza : suppression d'utilisateur préserve l'historique au niveau
  "personnel" (corrobore M14/0007 au passage).
- Sellsy : 3 régimes de suppression client (léger/complet/archive), la
  suppression complète reste **bloquée sur les factures émises, conservées
  pour raison légale malgré la demande explicite de tout supprimer** — bon
  exemple de contrainte légale primant sur une action utilisateur.

**Exception documentée et significative** : Vertuoza, `comment-recuperer-une-
facture-supprimee` — la suppression d'une facture (à l'état où elle est
supprimable) est **strictement irréversible, sans corbeille ni délai de
grâce**. C'est la seule exception nette au motif M4 trouvée dans le corpus — à
traiter comme un contre-modèle, pas comme un standard.

### M5 — Synchronisation externe fragile (5/10)

- **Vertuoza**, comptabilité : **~40 codes d'erreur de synchronisation**
  distincts listés officiellement, plusieurs renvoyant directement au support
  sans action utilisateur possible.
- **InterFast**, Trackdéchets (BSFF) : synchronisation **mono-directionnelle**
  — une modification faite côté Trackdéchets n'est jamais remontée dans
  InterFast, état divergent silencieux possible (avertissement ⚠️ explicite de
  l'éditeur).
- **Sellsy**, connecteur multi-entités : synchronisation asynchrone à délai non
  garanti (~5 min), sens unique, et **toute modification du devis maître après
  passage en "Accepté" n'est jamais propagée** — seule solution : dupliquer
  entièrement le devis maître.
- **InterFast**, Peppol : modification d'une fiche client **non rétroactive**
  sur les factures déjà finalisées → erreur persistante, correction possible
  uniquement via le support.

### M6 — Ressaisie forcée malgré import (4/10)

- **Costructor** : import PDF de devis — les ouvrages détaillés deviennent de
  simples lignes de fourniture (dégradation silencieuse de structure).
- **Costructor** : import d'ancienne facture (PDF/image/Factur-X) — **aucune
  extraction automatique**, toutes les métadonnées ressaisies manuellement,
  contredisant la promesse d'« éviter les ressaisies fastidieuses » du même
  article.
- **OpenFire Odoo** : import de catalogue — un champ non inclus dans un import
  "partiel" **écrase silencieusement** une donnée existante (le prix repasse à
  0 si `list_price` est omis).

### M9 — Permission grossière, contrastée (2/10 + 1 contre-exemple riche)

- **Vertuoza** documente **lui-même** un risque de fuite d'accès résiduel
  (« cacher Finances laisse un accès résiduel à la facturation via
  l'avancement ») — aveu explicite de l'éditeur, rare dans le corpus.
- **Axonaut** : absence de permission cause une absence silencieuse d'option
  (bouton disparu), pas un message d'erreur explicite.
- **Contre-exemple riche** : Obat (voir §0.2) — 7 rôles + permissions
  individuelles. À utiliser comme référence positive pour SUPORDO, pas comme
  preuve qu'une granularité fine est indispensable en V1.

### M12 — IA = brouillon jamais finalisé sans validation humaine (motif positif, preuve renforcée)

Voir §0.3. Trois témoins `ACQUIS DOCUMENTAIRE` indépendants (InterFast, OpenFire
Zendesk, Obat) convergent sur le même principe : une capture IA (voix, relevé)
produit toujours un **brouillon**, jamais un document finalisé automatiquement.
Vertuoza ajoute un détail `MARKETING_ONLY` cohérent : « si vous faites une
erreur en dictant, vous pourrez corriger le texte plus tard depuis votre
ordinateur » — correction **différée**, pas en direct sur mobile.

### M13 — Bascule de conformité au niveau du compte (motif nouveau)

- **Sellsy**, « Mode conforme » : activation définitive, présentée sobrement en
  article d'aide plutôt que comme un moment de décision solennel dans le
  produit.
- **Obat**, migration de plateforme de facturation électronique (changement de
  PDP) : mandat signé, migration automatisée, **zéro action manuelle côté
  utilisateur** au-delà de la signature — exemple positif de dépendance externe
  complexe rendue invisible pour l'utilisateur, à opposer au cas Sellsy.

### M15 — Scellement photo tiers qualifié (motif positif émergent)

- **Obat** : partenariat Certificall — photo scellée juridiquement
  (géolocalisation, horodatage, hash SHA-256), payant à l'unité (0,40 €/photo),
  **mobile uniquement**.
- **Batikko** (`MARKETING_ONLY`, mais convergent avec un fait de centre d'aide
  Obat donc plus qu'un simple signal isolé) : partenariat Certigna équivalent,
  offert en illimité selon plan, QR code de vérification publique.

Deux éditeurs indépendants convergent sur le même mécanisme pour la preuve
juridique chantier — signal de marché réel pour la conception de la capture
terrain SUPORDO (S4/provenance appliqué à la photo), au-delà d'un simple
attachement de fichier.

### M17 — Capture terrain offline-tolerant (3/10 indépendants)

- **Extrabat** : signature de rapport d'intervention fonctionne offline sur
  mobile, synchronisation temps réel à la reconnexion.
- **Obat** : pointage mobile avec validation réversible (bouton "Annuler").
- **Batikko** (`MARKETING_ONLY`) : PWA, cohérent avec le même principe.

Corrobore directement la contrainte déjà posée en `08` §13 (capture terrain
jamais dépendante d'une connexion continue) — ce n'est donc plus seulement une
exigence déduite de la contrainte métier, c'est un motif de marché observé.

---

## 3. Tableau consolidé de toutes les frictions extraites

Format condensé (concurrent · source · objet · motif dominant · réversible ·
risque principal · preuve). Le détail complet de chaque friction (déclencheur,
symptôme, cause, comportement produit, message fourni, solution officielle,
contournement) reste disponible dans les rapports de mining sources — ce
tableau sert de carte de navigation, pas de duplication intégrale.

| Concurrent | Source (fichier) | Objet | Motif | Réversible ? | Risque principal | Preuve |
|---|---|---|---|---|---|---|
| InterFast | creer-une-facture-d-avoir-client.md | Facture/Avoir | M1 | Non (avoir devient inaltérable) | Financier+juridique | 1 source, cohérent L1/L2 |
| InterFast | creer-une-facture-d-avoir-client.md | Avoir/Acompte | M3 | — | Financier | 1 source |
| InterFast | resoudre-un-ajout-d-utilisateur-par-erreur.md | Personnel/Utilisateur | M13-adjacent | Partiel (crédit) | Financier | 1 source |
| InterFast | remplir-un-bsff.md | BSFF/Fluides frigo | M8 | Oui pour la config | Réglementaire fort | 1 source |
| InterFast | remplir-un-bsff.md | BSFF/Trackdéchets | M5 | Non | Réglementaire+UX | 1 source, ⚠️ éditeur |
| InterFast | remplir-un-bsff.md | BSFF | M14 | Oui côté Trackdéchets seul | Opérationnel+réglementaire | 1 source |
| InterFast | resoudre-les-erreurs-sur-un-bsff.md | BSFF/CERFA | M14 | Partiel, manuel | Financier+réglementaire | 1 source |
| InterFast | creer-une-facture-d-acompte-de-situation-de-solde.md | Devis/Facture | M2 | Oui non intuitif | UX+opérationnel | 1 source |
| InterFast | creer-une-facture-d-acompte-de-situation-de-solde.md | Facture de situation | M2 | Non | UX | 1 source |
| InterFast | connecter-interfast-a-peppol.md | Facturation électronique | M5 | Non en libre-service | Opérationnel | 1 source |
| InterFast | modifier-une-facture-client.md | Facture | M1 | Non | Financier+juridique | corrobore F1 |
| InterFast | importer-des-clients.md | Client/Import | M6 | Oui (fusion) | Opérationnel | 1 source |
| InterFast | importer-des-clients.md | Client/Import | M3 | Non (protection voulue) | Intégrité | 1 source, positif |
| OpenFire Zendesk | gerer-vos-evenements-de-facturation-electronique.md | Facturation électronique | M13 | Non | Financier+réglementaire | 1 source |
| OpenFire Odoo | annuler-rembourser-ou-modifier-un-paiement.md | Paiement | M3 | Oui si ordre respecté | Comptable | 1 source |
| ProGBat | annuler-ou-modifier-une-facture.md | Facture | M2 | Non | Financier+juridique | 1 source, plus strict que L1/L2 |
| ProGBat | poursuivre-la-facturation-faite-sur-mon-ancien-logiciel.md | Import/Migration (L4) | M6 | Non applicable | Financier+comptable | voir §0.4 |
| OpenFire Odoo | importer-des-articles-ou-des-kits.md | Catalogue | M6 | Oui si averti | Financier | 1 source, voir §0.1 |
| Vertuoza | retour-au-statut-precedent-devis-accepte.md | Devis/Chantier | M2 | Non (fonctionnalité retirée) | Perte de données | 1 source |
| Vertuoza | coordonnees-de-facturation-chantier-client-modifiees.md | Chantier/Client | M7 | — | Financier | 1 source |
| Vertuoza | comment-recuperer-une-facture-supprimee.md | Facture | exception à M4 | **Non — irréversible** | Perte totale, légal | 1 source |
| Vertuoza | modifier-la-reference-d-une-facture-deja-comptabilisee.md | Facture | M1 (cas extrême) | Non | Légal/UX majeur | 1 source |
| Vertuoza | liste-des-codes-d-erreurs-de-synchronisation-comptable.md | Facture/Compta | M5 | Variable | UX+financier | preuve dense |
| Vertuoza | gestion-des-permissions.md | Utilisateur/Rôle | M9 | — | Sécurité | 1 source, aveu éditeur |
| Vertuoza | mot-de-passe-oublie-que-faire.md | Auth | M10 | Oui mais destructif | UX majeur | 1 source |
| Vertuoza | assistant-ia-devis-avenant-mobile.md | Devis/IA vocale | M12 | — | UX | `MARKETING_ONLY`, corrobore M12 |
| Vertuoza | ouvrier-rapport-d-intervention.md | Intervention | M1 (extrême) | **Non** | UX/financier | 1 source |
| Axonaut | modifier-un-devis.md | Devis | M1 | Conditionnel | Financier/UX | corrobore Vertuoza #1/22 |
| Axonaut | comment-modifier-une-facture.md | Facture | M1 | Oui mais fragile | Financier | 1 source |
| Axonaut | comment-modifier-une-facture.md (suppression) | Facture | M2 | Non | Légal, cite la loi | corrobore L3/0007 |
| Axonaut | droits-responsabilites-utilisateurs.md | Personnel/Utilisateur | motif tarifaire | — | Financier (incitatif) | corrobore M14/0007 |
| Axonaut | gestion-dlc-dluo-dlm-et-garanties.md | Stock/Catalogue | attente≠réalité | — | Risque métier si mécompris | 1 source, aveu produit |
| Costructor | comment-modifier-supprimer-une-facture.md | Facture | M1 | Non | Financier+juridique | corrobore Sellsy, L1/0007 |
| Costructor | comment-creer-une-facture-davoir.md | Facture/Avoir | M1 | Non dans l'ordre inverse | UX métier BTP | 1 source |
| Costructor | recreer-un-ancien-devis.md | Devis | M6/L4-adjacent | — | Risque séquence | 1 source |
| Costructor | comment-importer-un-devis-dpgf-dqe-excelpdf.md | Devis/Catalogue | M6 | — | Structurel (dégradation silencieuse) | 1 source |
| Costructor | comment-migrer-mes-donnees-dun-autre-logiciel.md | Facture | M6 | — | tension avec L3/0007 | 1 source |
| Costructor | comment-importer-une-ancienne-facture.md | Facture | M6 | — | promesse≠réalité | 1 source |
| Costructor | comment-gerer-les-membres-de-son-equipe.md | Personnel/Utilisateur | M9 (contre-exemple) | — | Complexité de choix | 1 source, 9 rôles sans matrice |
| Costructor | comment-utiliser-les-feuilles-dheures.md | Personnel/Chantier | M1 | Non direct | — | corrobore motif transversal |
| Costructor | comment-creer-un-avenant-a-un-devis.md | Devis/Facture | M7 | — | pertinent O5/0007 | 1 source |
| Costructor | comment-importer-des-produits-dans-ma-bibliotheque.md | Catalogue | limite technique | — | pertinent T-PACK-CLIM | 1 source, 5000 lignes max |
| Costructor | comment-activer-la-facturation-electronique.md | Facture/Intégration | — | — | pertinent `06`/`09` | 1 source |
| Sellsy | creer-et-gerer-des-avoirs.md | Avoir/Facture | M1 | Variable selon chemin | Financier | 1 source |
| Sellsy | questions-frequentes-sur-gocardless.md | Facture/Paiement | M7 | Non automatique | **Financier direct** | 1 source |
| Sellsy | connecteur-multi-entites-de-facturation.md | Devis/Intégration | M5+M7+M6 | Non (dupliquer requis) | pertinent Q3/09 | 1 source, cas riche |
| Sellsy | envoyer-un-document-pour-signature-electronique.md | Devis/Signature | nouvel état "expiré" | Oui, procédure | UX | 1 source, voir §4 |
| Sellsy | creer-et-gerer-les-declinaisons-de-mes-produits.md | Catalogue | M2 | **Non** | pertinent T-PACK-CLIM | 1 source |
| Sellsy | societes-presentation-de-la-fiche-prospect.md | Client/Prospect | pertinent Q19/12 | — | — | 1 source, voir §4 |
| Sellsy | gerer-les-acces-collaborateurs.md | Personnel/Utilisateur | exception à M4 | **Non, définitif** | Turnover mal protégé | 1 source |
| Sellsy | societes-supprimer-ou-archiver-des-societes.md | Client | M4 (positif) | Oui, 3 régimes | légal prime sur demande utilisateur | 1 source |
| Sellsy | supprimer-ou-modifier-un-compte-bancaire-synchronise.md | Paiement/Intégration | M2 (bien expliqué) | — | contre-exemple positif EXPLAIN | 1 source |
| Sellsy | comprendre-le-mandat-pa-et-verification-identite.md | Facture/Réglementaire | — | — | pertinent Q13/09, KYC facial | 1 source, cite Art. 242 nonies F CGI |
| Sellsy | importer-mes-donnees-societes-et-contacts.md | Client/Import | M6 | — | doublons silencieux | 1 source |
| Sellsy | connexion-sso.md | Auth/Sécurité | trou de continuité | — | pas d'accès de secours documenté | 1 source |
| Sellsy | facturer-a-l-avancement.md | Devis/Facture | M8+M2 | Non une fois finalisée | — | 1 source |
| Sellsy | activer-le-mode-conforme-pour-les-documents-de-vente.md | Facture/Compte | M13 | **Non, définitif** | — | 1 source, voir §2 M13 |
| Extrabat | ne-peux-modifier-mode-de-reglement.md | Règlement | M1 | Oui via contrepasse | Financier | cite Art. 88 CGI |
| Extrabat | mon-client-ne-peut-pas-aller-sur-son-espace-client.md | Client/Accès | M3 | Oui | UX | 1 source |
| Extrabat | recuperer-client-mis-erreur-statut-corbeille.md | Client | M4 (positif) | Oui | Faible | corrobore M4 fortement |
| Extrabat | mon-email-revient / spams.md | Email | M3 | Oui après correction DNS | Commercial (devis non reçu) | 1 source |
| Extrabat | gerer-les-doublons-dans-les-bases-clients-prospects.md | Client | M19 | Oui (masquage) | — | asymétrie clients/fournisseurs |
| Extrabat | bloquer-gestion-commerciale-client-independant-de-lencours.md | Client/Facturation | PREVENT positif | Oui | Protection | 1 source |
| Extrabat | transfert-dun-article-dun-depot-a-un-autre.md | Stock/Dépôt | M3 | — | UX | 1 source |
| Extrabat | desactiver-ou-rendre-inactif-article.md | Catalogue | M4 (positif) | Oui | Faible | corrobore M4 |
| Extrabat | veux-affecter-devis-facture-a-client.md | Facture/Client | M3 | Partiel | Financier+oubli | fenêtre de correction qui se referme |
| Extrabat | modifier-coordonnees-de-iban-devis-commandes-factures.md | IBAN/Documents | M3 (critique) | Non en libre-service | **Financier direct** | voir §2 M3 |
| Extrabat | forcer-la-synchronisation-de-mes-rendez-vous-a-venir.md | Agenda/Sync | M5 | Oui, manuel | UX (RDV manqué) | 1 source |
| Extrabat | synchronisation-avec-outlook.md | Agenda/Sync | limite native admise | — | UX | honnêteté rare du corpus |
| Extrabat | rapports-dintervention-signatures-today.md | Intervention | M17 (positif) | — | — | corrobore offline-tolerant |
| Extrabat | checklist-de-fin-dannee.md | Comptabilité | M8/LEGAL_GATE implicite | Non (clôture=verrou) | Financier | limite dure 3 exercices, jamais documentée ailleurs |
| Extrabat | gestion-consentement.md | RGPD/Email | irréversible côté admin | Non côté admin | Juridique | corrobore S5/0007 |
| Obat | achats-facturation-electronique-suppression-impossible.md | Achat/FE | M2 (exemplaire) | Non | Juridique/fiscal préventif | voir §2, PREVENT+EXPLAIN modèle |
| Obat | dans-quelles-conditions-supprimer-annuler-facture.md | Facture | M1 | Brouillon oui, sinon non | Financier | détaille L1/0007 |
| Obat | annuler-facture-sans-avoir-plus-possible.md | Facture/Avoir | M16 | Non | Financier/légal | produit devient plus strict dans le temps |
| Obat | peut-on-supprimer-elements-facture-situation.md | Facture de situation | M1 | Non en édition directe | Financier | ajout≠suppression |
| Obat | comment-creer-avoir-obat.md | Avoir | M3 | — | Financier | dépendance acompte→avoir détaillé |
| Obat | variantes-devis-references-stables.md | Devis/Variantes | M2 (RECOVER exemplaire) | **Oui, explicitement** | — | voir §4, transposable Q3/09 |
| Obat | recreer-devis-autre-logiciel.md | Migration/Devis | M6, corrobore L4 | — | Financier/légal | applique L4 au devis, pas que facture |
| Obat | deja-inscrit-autre-plateforme-cle-migration.md | Facturation électronique | M13 (positif) | — | Faible | dépendance externe rendue invisible |
| Obat | resoudre-erreurs-envoi-facture-electronique.md | Facturation électronique | M5 (EXPLAIN exemplaire) | Oui après correction | Financier | table diagnostic cause→action |
| Obat | facturation-electronique-obligatoire-septembre-2026.md | FE (réception) | M2 | **Non, explicite** | Financier+réglementaire | confirme L1-L3 côté réception |
| Obat | multi-user-differents-roles-acces.md | Personnel/Rôles | voir §0.2 | — | — | contredit Q11/09 |
| Obat | multi-user-interface-pointage-mobile.md | Personnel/Pointage | M4 (positif) | **Oui, explicite** | Faible | motif RECOVER |
| Obat | protegez-donnees-bancaires-obat.md | Sécurité/Banque | PREVENT exemplaire | — | Protection | contraste avec Extrabat IBAN |
| Obat | reconnaissance-optique-ocr.md | Achats/OCR | AI WRONG OUTPUT | — | Financier si non relu | pas d'indicateur de confiance visible |
| Obat | dictez-devis-assistant-vocal.md | Devis vocal IA | M12 (`ACQUIS DOCUMENTAIRE`) | — | — | voir §0.3 |
| Obat | photos-certifiees-obat.md | Photo/Preuve | M15 (positif) | — | Juridique(preuve)+financier | voir §2 |
| Batikko | devis-factures.md | Devis | 3e variante verrou | — | — | `MARKETING_ONLY` |
| Batikko | chantiers.md | Chantier | M4 (positif) | **Oui, 10 ans** | Faible | `MARKETING_ONLY` mais convergent |
| Batikko | photos-juridiques.md | Photo/Preuve | M15 | — | — | `MARKETING_ONLY`, convergent avec Obat |
| Batikko | fournisseurs.md | Fournisseur/OCR | AI confidence (positif) | — | — | `MARKETING_ONLY`, contraste avec Obat |

---

## 4. Frictions les plus significatives pour SUPORDO (top 15, cross-lots)

1. **Vertuoza — édition de PDF hors produit pour corriger une facture comptabilisée** (M1 extrême). Le signal le plus clair de ce qui arrive quand aucun mécanisme de correction adapté n'existe.
2. **Vertuoza — suppression de facture strictement irréversible**, seule exception nette au motif M4 (soft-delete) du corpus — contre-modèle explicite à ne pas suivre.
3. **Extrabat — IBAN codé en dur dans un template personnalisé**, invisible depuis l'interface, corrigible uniquement par ticket support — risque financier direct (paiement vers un ancien compte).
4. **Obat — suppression bloquée à tous les niveaux et pour tous les rôles dès réception d'une facture électronique**, avec message contextuel systématique — modèle PREVENT+EXPLAIN le plus abouti du corpus, directement transposable à l'irréversibilité L1 de SUPORDO.
5. **Obat — variantes de devis : annulation de signature sans casser les références** — modèle RECOVER directement transposable à Q3 (`09`), le meilleur précédent du corpus sur "comment corriger une erreur humaine de signature sans détruire l'historique".
6. **Sellsy — connecteur multi-entités** : verrou de mutabilité + propagation figée + ressaisie forcée dans le même mécanisme — cas d'école pour cadrer Q3/Q4 avant l'architecture multi-tenant.
7. **Sellsy — prospect ne peut créer que des devis** avant transformation en client — premier élément factuel (1 témoin) pour la nouvelle question Q19 (`12`, objet Demande/Lead).
8. **Sellsy — GoCardless non annulé automatiquement** à l'annulation d'une facture liée — motif de propagation absente à risque financier direct, pertinent pour `08` §6.
9. **InterFast/OpenFire — cluster BSFF/Trackdéchets** : configuration en 5 sous-systèmes, synchronisation mono-directionnelle, règle métier non appliquée par défaut sur mobile — le terrain le plus riche pour appliquer PREVENT/DETECT/RECOVER sur le pack métier climatisation/PAC.
10. **OpenFire — cycle d'événements de facturation électronique** (10 statuts client, 7 fournisseur) — la meilleure preuve concrète de ce que "gérer" la facturation électronique implique en exploitation, pas seulement à l'émission.
11. **Obat + Batikko — scellement photo tiers qualifié**, deux éditeurs indépendants — signal de marché fort pour S4/provenance appliqué à la photo terrain.
12. **Vertuoza — mot de passe oublié = suppression + recréation de compte**, aucun flux de reset standard.
13. **Vertuoza — ~40 codes d'erreur de synchronisation comptable** exposés bruts à l'utilisateur — signal qu'une intégration mal abstraite devient un fardeau support permanent.
14. **Axonaut/Costructor — suppression de facture en masse "pratiquement impossible sans consultation du support"** (Axonaut) — contrainte légale qui se traduit par une charge opérationnelle lourde, non outillée.
15. **Extrabat — limite dure de 3 exercices comptables simultanés**, jamais mentionnée ailleurs dans le corpus — signal qu'il existe des limites structurelles non documentées par les autres éditeurs, à anticiper dans le modèle de données SUPORDO.

---

## 5. Ce que ce mining ne permet pas de conclure

- **Aucune fréquence d'incident réelle** — un article FAQ dédié à un problème
  (ex. F10 InterFast « de nombreux utilisateurs sont bloqués ») est un signal
  éditorial de correction produit passée, pas une mesure d'usage actuel.
- **Aucune priorité d'implémentation** — ce document alimente `11` et `13`, il
  ne remplace pas l'analyse 80/20 déjà faite en `01`/`07`.
- **Le corpus batikko** relève d'un genre documentaire plus proche du marketing
  produit que du support réel (articles à la troisième personne, tableaux de
  statut roadmap) — toute friction batikko de ce document reste `MARKETING_ONLY`
  sauf convergence explicite avec un fait de centre d'aide d'un autre concurrent
  (comme M15, M4, M17 ci-dessus).
