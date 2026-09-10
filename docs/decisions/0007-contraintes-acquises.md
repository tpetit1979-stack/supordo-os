# 0007 — Contraintes acquises

Ce fichier dit ce qui est **opposable** au moment de coder ou de décider.
Il ne raconte rien, il n'explique rien : il contraint, oriente, ou arrête.

Il est court par construction. S'il dépasse deux pages écran, il faut en
retirer, pas en ajouter. Ce qui n'y tient pas va dans le contrat fonctionnel
ou dans les analyses sources.

---

## Comment l'utiliser — humain et agent

Quatre statuts, quatre comportements. **Aucun autre.**

| Statut | Ce que ça veut dire | Comportement attendu |
|---|---|---|
| `LEGAL_CITÉ` | contrainte externe citée par une source concurrente, **non encore vérifiée à la source officielle** | respecter, et vérifier avant mise en production |
| `SUPORDO_DECISION` | décision prise par le PO | respecter, ne pas « améliorer », ne pas rouvrir |
| `MARKET_BASELINE` | convergence observée chez les concurrents | adopter comme hypothèse de départ **seulement si aucune décision contraire n'existe** |
| `OPEN` | question non tranchée | **s'arrêter et demander.** Ne pas choisir par défaut |

**Une convergence concurrentielle n'est jamais une obligation.** Le fait que
huit éditeurs fassent la même chose ne prouve pas qu'ils ont raison — la
décision 0001 en est la démonstration : nous les croyions aveugles aux rôles,
ils ne l'étaient pas, et le corpus n'a jamais dit qu'ils avaient raison.

**Règles de tenue :** une entrée ne s'ajoute qu'avec une source nommée ; ne se
modifie qu'avec une source nouvelle, jamais avec un raisonnement ; passe de
`MARKET_BASELINE` ou `OPEN` à `SUPORDO_DECISION` uniquement sur arbitrage
explicite du PO.

**Sources primaires :** `functional-onboarding-pilot.md`,
`functional-propagation-pilot.md`, `functional-devis-3a-naissance.md`,
`functional-devis-3b-cycle.md`, `functional-devis-3c-sorties.md`.
Corpus : 2 510 documents, 12 éditeurs français.

---

## L — Contraintes externes

Toutes citées par des sources concurrentes. **Aucune n'a encore été vérifiée
sur Légifrance ou une source officielle.** À faire avant mise en production.

### L1 · Une facture numérotée est immuable
`LEGAL_CITÉ`
Correction par un document tiers — un avoir — jamais par modification du
document d'origine.
**Pourquoi :** anti-fraude TVA ; Art. L.441-9 du Code de commerce cité par
Sellsy.
**Source :** 6 éditeurs (Costructor, Obat, Sellsy, InterFast, OpenFire Odoo,
Axonaut) — `propagation` §6.1.
**Conséquence :** l'état `émise` est terminal. Aucune route d'écriture ne
l'accepte. À poser dès la première migration.

### L2 · Un avoir numéroté relève du même régime
`LEGAL_CITÉ`
**Source :** Sellsy, Obat, InterFast — `propagation` §6.1.

### L3 · Numérotation séquentielle continue
`LEGAL_CITÉ`
Pas de trou, pas de réattribution, pas de renumérotation.
**Source :** `propagation` §6.2.

### L4 · Une facture importée n'est pas une facture émise
`SUPORDO_DECISION`
Ne jamais faire passer une facture historique reprise d'un autre logiciel
pour une facture native émise par SUPORDO.
**Ce que cela n'interdit pas :** importer numéro, date, montant, PDF, client,
rattachement, état de paiement, avec `provenance = système précédent`.
**Pourquoi :** ProGBat interdit l'import de factures, mais rien n'établit une
interdiction générale — et la migration d'historique reste un levier
commercial. La distinction porte sur le régime du document, pas sur la
reprise de données.
**Source :** ProGBat — `onboarding` §6 ; reformulation PO.

---

## S — Décisions SUPORDO

### S1 · Le lieu est distinct du client
`SUPORDO_DECISION`
Le lieu survit au changement de propriétaire, de locataire ou de payeur.
L'historique d'intervention est rattaché au lieu, pas seulement au tiers.
**Conséquence :** très coûteux à changer — casse la mémoire longue et le SAV.

### S2 · Un objet peut naître sans son parent
`SUPORDO_DECISION`
Un devis n'exige aucune affaire préexistante. Un client peut naître depuis
l'écran de devis. Une intervention peut exister sans devis.
**Test de validité :** si l'un de ces trois cas exige un écran amont, le
modèle est faux.

### S3 · Prix catalogue figés à la création
`SUPORDO_DECISION`
Un prix repris du catalogue est copié dans la ligne, pas référencé. Une
modification ultérieure du catalogue n'altère pas les documents existants.
**Appui :** Obat le documente (SNAPSHOTTÉ) — source unique, compatible avec
le silence des autres.

### S4 · Provenance là où elle sert
`SUPORDO_DECISION`
Une information issue d'une interprétation IA, d'un import ou d'une capture
terrain doit pouvoir conserver sa provenance **lorsque celle-ci est
nécessaire à la validation, à la sécurité métier ou à la traçabilité**.
**Ne pas en déduire** une architecture de provenance universelle au niveau de
chaque champ. Pas de lineage sur `customer.first_name`.
**Pourquoi :** une mémoire alimentée par IA sans provenance est une mémoire
capable de mentir — mais tracer chaque champ construirait un système de data
lineage avant le MVP.

### S5 · Consentement sur les médias publiables
`SUPORDO_DECISION`
Les médias susceptibles d'une diffusion externe portent finalité, date,
auteur du consentement et droit de retrait. **Pas tous les fichiers** : une
facture PDF, un bon fournisseur ou une notice fabricant n'entrent pas dans ce
régime.
**Pourquoi :** droit à l'image et propriété d'autrui sur les photos de
chantier. Le consentement relève du droit, pas du marketing.

---

## M — Baselines de marché

Hypothèses de départ. **Le niveau de preuve est indiqué** : il conditionne le
poids à leur donner.

| # | Règle | Preuve | Source |
|---|---|---|---|
| M1 | Client créable à la volée pendant la création d'un devis | **8/8**, aucun contre-exemple | 3A §13 |
| M2 | Élément de catalogue créable à la volée pendant la création d'un devis — **sémantique à vérifier** : sélectionner un article ≠ créer un article ≠ ligne libre ≠ convertir une ligne en article | **8/8** annoncé, distinction non tranchée | 3A §13 |
| M3 | Aucun projet, chantier ou affaire requis avant un devis | **8/8** facultatif ou non déterminé | 3A §7 |
| M4 | Génération PDF et impression : aucun effet d'état | 5 éditeurs, aucun contre-exemple | 3B §7 |
| M5 | L'envoi ne verrouille rien ; le devis reste modifiable au moins jusque-là | 3 éditeurs explicites, jamais contredit | 3B §14 |
| M6 | Le devis reste consultable après transformation | 6 éditeurs, aucun contre-exemple | 3C INV-3C-2 |
| M7 | Un devis peut produire plusieurs objets aval du même type — relation 1→N, jamais 1→1 | 6+ éditeurs | 3C INV-3C-5 |
| M8 | Acompte et situation déduits automatiquement du solde, jamais ressaisis | 6 éditeurs | 3C INV-3C-1 |
| M9 | L'avenant est additif, jamais un remplacement | 3/3 de ceux qui le documentent | 3B §8.4 |
| M10 | Le devis change d'état à sa **première** sortie structurante — pas à l'envoi, pas à la signature seule | 7/8 | 3C INV-3C-3 |
| M11 | L'identité entreprise se propage sur les documents générés | 4/6 | onboarding §7 |
| M12 | La rentabilité d'un chantier est un agrégat recalculé, jamais saisie | 3 éditeurs | propagation §4.7 |
| M13 | La numérotation verrouille la suppression, pas l'édition | **2 éditeurs seulement** | 3B §6.3 |
| M14 | Personnel ≠ compte utilisateur | **2 éditeurs** | onboarding §8 |
| M15 | Cascade des conditions de règlement : chantier → client → défaut → devis → facture, surchargeable à chaque niveau | **1 éditeur (ProGBat)** — bonne idée fonctionnelle, pas un standard | onboarding §6 |
| M16 | Le devis prime sur le rapport d'intervention au moment de facturer | **1 éditeur (InterFast)** | propagation §4.9 |

M13 à M16 reposent sur une ou deux sources. Les traiter comme **options de
conception à étudier**, pas comme des défauts.

**Modes de propagation tranchés par une source primaire** — les seuls du
corpus, tout le reste est indéterminé :
`catalogue → devis` prix **snapshotté** (Obat) · `devis → chantier`
coordonnées de facturation **snapshottées non rétroactives** et nom du
chantier **référencé rétroactivement** (Vertuoza) · `devis → facture` client,
produits, montants, taxes **copiés** (4 éditeurs) · retenue de garantie
**reportée** (Costructor, OpenFire) mais **non propagée chez Vertuoza —
anomalie confirmée**.

---

## O — Questions ouvertes

**S'arrêter et demander.** Ne pas choisir par défaut. Ces six questions sont
l'objet du contrat fonctionnel devis.

| # | Question | État du marché |
|---|---|---|
| O1 | Ligne libre hors catalogue, oui ou non ? | 4 éditeurs oui, 3 silences cohérents. Détermine le mur d'entrée à l'onboarding |
| O2 | Signature = acceptation, ou deux événements ? | Bascule binaire : 2 éditeurs séparent, 4 fusionnent. **Aucune contrainte légale** |
| O3 | Où placer le verrou de mutabilité du devis ? | 5 modèles, aucun dominant. **Aucune cause réglementaire sur le devis, dans aucun des 8 corpus** |
| O4 | Objet pivot entre devis et facture, ou transformation directe ? | 8/8 se classent dans l'une ou l'autre famille, **aucun ne fait les deux** |
| O5 | Quels mécanismes de dérivation retenir : duplication, variante, révision, avenant ? | 4 mécanismes distincts, aucun éditeur ne les a tous |
| O6 | Minimum de contenu pour finaliser un devis ? | **Silence total 8/8.** Seule exception : Vertuoza bloque à 0 € |

---

## N — Ne pas chercher

Le corpus ne peut pas répondre. **N'y consacrer aucune analyse.**

- **Copie ou référence** — le mode technique de la quasi-totalité des
  propagations. Les éditeurs décrivent un comportement visible, jamais le
  stockage.
- **Le cas normal** — la documentation d'aide saute systématiquement le cas
  standard pour décrire les variantes. *Un centre d'aide documente ce qui
  coince, pas ce qui marche.*
- **La cause des verrous non réglementaires** — le corpus dit que l'action
  est bloquée, rarement pourquoi.
- **Ordre imposé ou ordre éditorial** — jamais distinguable.
- **Effet d'une modification du devis sur un objet déjà créé** — non
  déterminé presque partout.
- **Toute donnée d'usage** — adoption, fréquence, satisfaction, volonté de
  payer, contournements. Décision 0004 : la documentation est une source
  éditoriale.

---

## V — Vocabulaire à ne pas employer

- **« Révision »** — deux sens incompatibles selon l'éditeur : version
  automatique chez Costructor, formule de prix chez Vertuoza.
- **« Modèle »** — deux objets différents : 4 éditeurs pré-remplissent les
  lignes, Sellsy les exclut explicitement.
- **États du devis** — aucun vocabulaire de marché. « Draft », « Brouillon »,
  « en attente » ; l'état initial n'est clairement documenté que chez 2
  corpus sur 8.

---

## Suite

Ce fichier ne produit pas de décisions. Il enregistre celles qui sont prises.

Les six questions de la section O s'arbitrent dans
`SUPORDO-CONTRAT-FONCTIONNEL-DEVIS-V0.md`, selon la chaîne
**ACQUIS → OPTIONS → RECOMMANDATION → DÉCISION PO → À TESTER TERRAIN**.
Chaque décision prise y remonte ici en `SUPORDO_DECISION`.

Et rappel des décisions 0004 et 0006 : la documentation concurrentielle ne
démontre ni l'usage réel, ni l'exhaustivité fonctionnelle, ni l'absence d'une
fonctionnalité. H1_REAL_WORLD reste entièrement non tranchée. Les questions
de terrain sont hors de ce fichier.
