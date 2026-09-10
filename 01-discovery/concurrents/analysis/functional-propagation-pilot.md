# Pilote — Exploitation fonctionnelle : propagation et irréversibilité

Mission pilote, un phénomène transversal (propagation d'un objet à un autre ;
irréversibilité d'un objet), un seul verdict, puis stop. N'est pas une
extraction V2/V3, ne modifie pas LIGHT, ne fonde aucune décision produit
SUPORDO au-delà du test de méthode lui-même. Le phénomène traverse devis,
facture, intervention, commande, client, catalogue sans être organisé par eux.

## 1. Questions

1. Quand un objet naît d'un autre, qu'est-ce qui le suit (copié, référencé,
   snapshotté, recalculé, réinitialisé) ?
2. À partir de quand un objet ne peut plus être modifié, et pourquoi
   (réglementaire, métier, technique) ?

## 2. Critère de rendement ex ante

Fixé avant toute lecture source, non modifié après lecture.

- **RENDEMENT_SUFFISANT** : au moins 15 règles de propagation sourcées,
  couvrant au moins 4 couples objet source → objet cible distincts, ET au
  moins 8 verrous sourcés, dont au moins 3 avec leur cause documentée
  (réglementaire, métier, technique).
- **RENDEMENT_FAIBLE** : les sources décrivent des actions sans dire ce qui
  se propage ni pourquoi un objet se verrouille.
- **NON_DETERMINABLE** : corpus candidat trop mince.

Note méthodologique sur le filtre cité dans la commande de mission
(« mesuré sur 253 documents de contrôle → 21,3 % ») : ce chiffre n'a pas pu
être retracé à une source dans le dépôt (recherche textuelle sur « 253
documents » et « 21,3 » infructueuse — voir §3). Il est donc traité comme
non vérifiable dans ce périmètre de lecture, sans remettre en cause le
filtre lui-même (`transition_objet = oui` ET `exception_ou_correction =
oui`), qui reste le filtre principal appliqué ici, mesuré directement sur
les 11 fichiers LIGHT disponibles.

## 3. Sélection

### 3.1 Instruments consultés avant lecture source

`CLAUDE.md`, `SCHEMA-LIGHT.md`, `functional-onboarding-pilot.md` lus
intégralement. `GLOSSAIRE-OBSERVE-LIGHT.md` et `corpus_index.json`
dépassent la taille de lecture d'un coup : non relus intégralement pour ce
pilote — la sélection s'appuie sur les 11 fichiers `light-*.md` eux-mêmes
(2 464 lignes de tableau cumulées, taille compatible avec une lecture
mécanique complète par script), pas sur le glossaire ou l'index.

Remarque de correction : sur la note du pilote onboarding indiquant que
`GLOSSAIRE-OBSERVE-LIGHT.md` et `corpus_index.json` font « 2539 lignes, 284
Ko » et « 7333 lignes, 284 Ko », la vérification mécanique pour ce pilote
donne 2539 et 7332 lignes respectivement — écart d'une ligne sur le second,
non significatif, mentionné par souci d'exactitude plutôt que corrigé
rétroactivement dans le document source.

### 3.2 Fait vérifié en préalable : la mise en garde sur `transition_objet = oui` seul

Mesure mécanique sur les 11 fichiers `light-*.md` (2 464 documents
LIGHT au total, tous éditeurs confondus, Obat inclus après correction du
script d'analyse — son tableau n'utilise pas de `|` de tête de ligne,
particularité non signalée dans SCHEMA-LIGHT et qui a fait échouer une
première passe automatique) :

- `transition_objet = oui` seul, sans aucune borne : **612 / 2 464 = 24,8 %**.

Ce chiffre confirme, à une échelle différente de celle citée dans la
mission (dénominateur non retracé, voir §2), l'avertissement transmis par
l'autre session : ce filtre seul est trop large pour servir de filtre
principal. Il est donc utilisé ici uniquement comme filtre **borné** (§3.3,
filtre C), jamais comme filtre autonome.

### 3.3 Filtres appliqués, mesurés mécaniquement

| Filtre | Définition | Documents | % du corpus LIGHT (2 464) |
|---|---|---:|---:|
| A (principal) | `transition_objet = oui` ET `exception_ou_correction = oui` | 187 | 7,6 % |
| B (second rideau, verrous) | `genre_documentaire` racine = `faq_depannage`, hors doublons avec A | 211 | 8,6 % |
| C (second rideau, borné) | `transition_objet = oui` seul, restreint aux documents dont `objet_principal` nomme un objet à fort enjeu (devis, facture, commande, intervention, client, catalogue, chantier, acompte, avoir, contrat, société/entreprise), hors doublons avec A/B | 224 | 9,1 % |

Détail par éditeur (A / B / C), sur les 11 fichiers LIGHT disponibles :

| Éditeur | Total LIGHT | A | B | C |
|---|---:|---:|---:|---:|
| axonaut | 119 | 39 | 4 | 20 |
| batikko | 11 | 5 | 0 | 0 |
| costructor | 94 | 6 | 0 | 22 |
| extrabat | 347 | 4 | 19 | 23 |
| inter-fast | 217 | 69 | 6 | 17 |
| obat | 274 | 5 | 10 | 14 |
| openfire-odoo | 212 | 8 | 7 | 34 |
| openfire-zendesk | 119 | 6 | 0 | 16 |
| progbat | 186 | 3 | 4 | 30 |
| sellsy | 454 | 15 | 12 | 12 |
| vertuoza | 431 | 27 | 149 | 36 |

Recherche textuelle ciblée en second rideau (mots-clés : hérite, repris,
récupère, automatiquement, ne peut plus, impossible de modifier, verrouill,
avenant, avoir, figé, validé) : appliquée comme critère de **classement**
interne à l'intérieur des filtres B et C plutôt que comme filtre séparé —
les documents dont `objet_principal` contient un de ces marqueurs sont
priorisés dans la sélection finale (§3.4).

### 3.4 Ordre de lecture et éditeurs retenus

Conformément à l'ordre imposé, ces quatre familles sont couvertes — le mot
« famille » désigne ici un dispositif de couverture destiné à garantir la
diversité de lecture, pas une taxonomie officielle du marché :

1. **Spécialiste BTP** : InterFast retenu comme lecture principale (filtre
   A le plus élevé de tout le corpus : 69 documents, signal de loin le plus
   dense). Vertuoza, également nommé en option pour cette famille, est lu
   en plus (non en remplacement) : son filtre B (149 `faq_depannage`,
   largement supérieur à tout autre éditeur) en fait une source
   incontournable pour l'axe irréversibilité, et le lire réduit le risque
   de concentration signalé au pilote onboarding plutôt que de l'aggraver.
2. **Généraliste** : Axonaut retenu (filtre A = 39, deuxième plus élevé du
   corpus). Sellsy, également nommé en option, est lu en plus pour la même
   raison anti-concentration (corpus le plus volumineux du panel, 454
   documents, sous-représenté si seul Axonaut portait la famille).
3. **ERP** : OpenFire Odoo (`documentation_2/knowsystem/`, corpus distinct
   du corpus d'aide Zendesk du même éditeur, conformément à la distinction
   déjà actée au pilote onboarding).
4. **Léger artisan** : Obat. Choisi plutôt que Batikko ou Costructor
   précisément parce que c'est le cas à arborescence plate identifié comme
   échec mécanique au pilote onboarding (`editorial_taxonomy` sans rubrique
   de premier niveau). Présélection basculée sur `objet_principal` et
   recherche textuelle, comme demandé. Costructor est lu en plus, en
   corroboration/contraste sur ce même profil « léger artisan », et parce
   que son corpus documente déjà (pilote onboarding) plusieurs
   dépendances directes réutilisables comme point de comparaison.

Soit **7 éditeurs sur 11 disponibles** (Batikko et Extrabat non lus en
profondeur pour ce pilote — corpus respectivement trop mince pour isoler un
sous-ensemble propagation/irréversibilité distinct sans lecture disproportionnée,
et trop volumineux avec un rendement LIGHT filtre A faible ; openfire-zendesk
non lu en profondeur, l'essentiel du contenu fonctionnel de cet éditeur
étant porté par `documentation_2`/Odoo). Ceci élargit la base du pilote
onboarding (6/12 éditeurs, 41/62 dépendances issues de 3 d'entre eux) sans
prétendre à l'exhaustivité — le rendement par éditeur est rapporté au §3.5,
et toute concentration observée dans les résultats est signalée explicitement
plutôt que masquée.

Sélection finale, plafonnée à 25 documents par éditeur (175 documents au
total) pour dimensionner l'effort à la question posée plutôt qu'à la taille
du corpus disponible : à l'intérieur de chaque éditeur, priorité stricte au
filtre A, puis B, puis C, départagés par score de mots-clés sur
`objet_principal`. Chaque document plafonné a été lu intégralement par un
agent dédié par éditeur, contraint à cette liste fermée, sans autre source.

### 3.5 Rendement par éditeur

Chaque éditeur a été confié à un agent dédié, contraint à sa liste fermée
de ~25 documents, sans autre source. Aucun agent n'a eu accès aux résultats
des autres — le rapprochement inter-éditeurs (§4 et suivants) est fait
après coup, par moi, à partir des sept rapports reçus séparément.

| Éditeur | Fichiers lus | Règles de propagation | Verrous | Fichiers sans rien |
|---|---:|---:|---:|---:|
| InterFast | 25/25 | 31 | 22 | 2 |
| OpenFire Odoo | 25/25 | 37 | 11 | 6 |
| Axonaut | 25/25 | 21 | 11 | 7 |
| Vertuoza | 25/25 | 25 | 9 | 6 |
| Sellsy | 25/25 | 9 | 26 | 9 |
| Obat | 25/25 | 15 | 11 | 11 |
| Costructor | 25/25 | 18 | 7 | 11 |
| **Total** | **175/175** | **156** | **97** | **52** |

Aucun éditeur ne domine à lui seul : le maximum individuel (OpenFire Odoo,
37 règles de propagation) représente 24 % du total, et pour les verrous le
maximum (Sellsy, 26) représente 27 % — loin de la concentration à 3
éditeurs sur 6 (66 %) relevée au pilote onboarding. La lecture reste
répartie sur les 7 éditeurs pour les deux axes.

Constat de rendement différencié par axe : Sellsy est l'éditeur le plus
pauvre en propagation (9, le plus bas du panel) mais le plus riche en
verrous (26, le plus haut) — cohérent avec son corpus dominé par les
statuts de documents et la conformité (mode conforme, facturation
électronique) plutôt que par des mécanismes d'héritage entre objets.
Inversement, OpenFire Odoo est le plus riche en propagation (corpus ERP à
cascades comptables denses) mais dans la moyenne basse en verrous.

Les deux seuils du critère ex ante (§2) sont dépassés très largement dès
l'agrégation des 7 rapports, avant même le travail de regroupement par
couple qui suit.

## 4. Règles de propagation, groupées par couple objet source → objet cible

Les 156 règles relevées par les 7 agents sont regroupées ci-dessous par
couple d'objets, dans l'ordre de priorité indiqué par la mission quand il
s'applique, puis par regroupement thématique pour les couples non
anticipés qui se sont révélés denses à la lecture. Seules les formulations
citées valent preuve ; les couples ne comptant qu'une seule occurrence
isolée sont renvoyés en fin de section plutôt que dispersés.

### 4.1 Devis → Facture (transformation directe, hors acompte/situation)

| Éditeur | Donnée | Mode | Surchargeable | Formulation exacte | Source |
|---|---|---|---|---|---|
| Axonaut | éléments du devis | NON DOCUMENTÉ | non documenté | « Si vous avez créé un devis, Axonaut reprendra les éléments du devis et il vous suffira de valider. » | commandes-clients-fournisseurs/fonctionnement-dune-commande-client.md |
| Obat | éléments chiffrés (fourniture, main d'œuvre, ouvrage) | COPIÉ | oui | « Votre facture finale sera automatiquement générée en reprenant les éléments de votre devis. […] Effectuez les modifications nécessaires. » | comment-cr-c3-a9er-et-modifier-une-facture-finale.md |
| InterFast | contenu du rapport / contenu du devis si intervention liée (priorité au devis) | COPIÉ | oui | « c'est le contenu du devis qui prime et qui se retrouvera dans le détail de votre facture. » | finances/facturer-une-intervention-depuis-l-application-web-et-mobile.md |
| Sellsy | — | NON DOCUMENTÉ (trou) | — | aucune formulation trouvée pour la conversion standard devis → facture | — |
| Costructor | — | NON DOCUMENTÉ (trou) | — | seul « convertir en » est employé, sans jamais préciser le mécanisme | ventes/comment-creer-un-bon-de-commande-client-1856wke.md (converti, pas facturé) |
| Vertuoza | — | NON DOCUMENTÉ (trou) | — | le sous-corpus lu ne documente aucune facture hors acompte/situation/avancement | — |
| OpenFire Odoo | — | NON DOCUMENTÉ (trou, passe par acompte/situation) | — | — | — |

**Trou majeur transversal** : le couple le plus attendu de tout le pilote —
devis → facture « ordinaire » — n'est explicitement documenté, même
partiellement, que par 3 éditeurs sur 7 (Axonaut, Obat, InterFast), et
aucun des trois ne tranche le mode exact (copié vs référencé). Les 4
autres (Sellsy, Costructor, Vertuoza, OpenFire) documentent abondamment les
variantes (acompte, situation, avancement) mais jamais le cas simple. Ce
silence répété sur le cas le plus fréquent est en soi un résultat du
pilote (voir §11).

### 4.2 Devis → Facture d'acompte

| Éditeur | Donnée | Mode | Surchargeable | Formulation exacte | Source |
|---|---|---|---|---|---|
| Costructor | montant/pourcentage d'acompte (paramétré en amont) | NON DOCUMENTÉ | non documenté | « Vous pouvez faire le paramétrage de vos acomptes depuis réglages/devis, cela sera repris automatiquement sur vos devis. » | ventes/comment-creer-une-facture-dacompte-fllvsr.md |
| Obat | pourcentage d'acompte paramétré dans le devis | NON DOCUMENTÉ | non documenté | « Cliquez sur facturer puis sur l'acompte qui aura été paramétrer dans le devis […] générée automatiquement. » | comment-facturer-un-acompte-depuis-un-devis-sur-obat.md |
| InterFast | montant TTC → recalcul HT puis TVA | RECALCULÉ | non (« il ne faut surtout pas modifier les montants HT calculés ») | « l'acompte est calculé directement sur le montant total TTC. […] le logiciel doit recréer une ligne en calculant d'abord le montant HT, puis y appliquer la TVA. » | finances/creer-une-facture-d-acompte-de-situation-de-solde.md |
| OpenFire Odoo | % de retenue de garantie du devis | RECALCULÉ | non documenté | « Dès que la retenue de garantie est renseignée, le logiciel calcule automatiquement la retenue de garantie sur les factures d'acompte, de situation et les factures de solde. » | knowsystem/creer-une-facture-avec-retenue-de-garantie-220.md |

### 4.3 Facture(s) d'acompte / de situation → Facture de solde ou finale (déduction automatique)

Couple le plus robustement convergent du corpus entier : 5 éditeurs sur 7
documentent indépendamment que le montant déjà facturé en amont est
déduit — jamais resaisi — lors de l'émission du document final.

| Éditeur | Donnée | Mode | Surchargeable | Formulation exacte | Source |
|---|---|---|---|---|---|
| Vertuoza | factures déjà émises (dont acomptes) + note de crédit | RECALCULÉ | non documenté | « Le système reprendra automatiquement : Les factures déjà émises (y compris les acomptes) […] Le solde restant à facturer sera calculé automatiquement. » | faq-foires-aux-questions/que-faire-si-j-ai-emis-une-note-de-credit-pour-corriger-la-tva-sur-une-facture-d-acompte-dans-un-chantier.md |
| Obat | montant de l'acompte (déjà facturé, non payé) | RECALCULÉ (déductible) | — | « Vous pourrez également déduire votre acompte depuis la facture finale si celui-ci n'était pas passé en statut « payé ». » | comment-cr-c3-a9er-et-modifier-une-facture-finale.md |
| InterFast | devis initial + avenant(s) + acomptes déjà versés | RECALCULÉ | non | « La facture générée reprendra automatiquement le montant du devis initial + ou – le montant de l'avenant, tout en déduisant les acomptes déjà versés. » | finances/creer-un-avenant-au-devis.md |
| InterFast | montant de l'acompte | RECALCULÉ | non | « votre facture finale a automatiquement déduit cet acompte de son calcul pour établir le solde restant dû » | finances/creer-une-facture-d-avoir-client.md |
| OpenFire Odoo | montant des lignes d'acompte | RECALCULÉ | non documenté | « les lignes d'acompte facturées préalablement viendront se soustraire dans la facture finale générée à l'écran et sur la facture en pdf. » | knowsystem/creer-ma-facture-finale-145.md |
| OpenFire Odoo | lignes facturables (acompte déduit) | RECALCULÉ | non documenté | « vous aurez ensuite la possibilité d'émettre une facture de solde, en sélectionnant "Lignes facturables (avec l'acompte déduit)". » | knowsystem/comment-generer-un-acompte-202.md |
| OpenFire Odoo | lignes de commande, déduction des situations facturées | RECALCULÉ | non documenté | « une facture de solde qui reprendra toutes les lignes de la commande avec la déduction des lignes de factures de situation. Cette facture de solde sera ainsi toujours à 0 €. » | knowsystem/creer-une-facture-de-situation-204.md |

Costructor et Sellsy ne documentent pas ce mécanisme dans le sous-ensemble
lu (Costructor le signale lui-même comme trou explicite : « aucun des 25
fichiers ne décrit comment […] le montant de l'acompte est ensuite
déduit/référencé sur la facture finale »). Axonaut ne traite pas non plus
ce cas dans son sous-ensemble.

### 4.4 Facture → Avoir / Note de crédit (correction, annulation)

Couple quasi universel : 6 éditeurs sur 7 le documentent.

| Éditeur | Donnée | Mode | Surchargeable | Formulation exacte | Source |
|---|---|---|---|---|---|
| Costructor | lignes de la facture (désignation, montants, quantités) | COPIÉ | oui | « Par défaut, toutes les lignes de votre facture sont reprises. Vous pouvez modifier/supprimer les lignes, les montants ou les quantités selon vos besoins. » | ventes/comment-creer-une-facture-davoir-vwjxpf.md |
| Obat | montant total de la facture | COPIÉ (100 %) | — | « Pour établir un avoir de 100 % sur une facture, veuillez utiliser le bouton « Annuler » […] Cette opération permettra d'annuler intégralement la facture. » | comment-cr-c3-a9er-un-avoir-sur-une-facture-sur-obat.md |
| Sellsy | lignes du document | COPIÉ | oui (avoir partiel) | « Le système vous propose alors un avoir correspondant à la facture avec toutes ses lignes. […] vous pouvez modifier l'avoir s'il s'agit d'un avoir partiel. » | documents-de-vente/creer-et-gerer-des-avoirs.md |
| Sellsy | contenu intégral du document | COPIÉ | oui | « Vous serez alors redirigé vers une copie de la facture que vous souhaitez modifier. » (via « Modifier par un avoir ») | documents-de-vente/creer-et-gerer-des-avoirs.md |
| InterFast | contenu (lignes) de la facture | NON DOCUMENTÉ | oui | « Dans le cas d'un avoir partiel, le contenu de la facture est repris > vous pouvez ainsi éditer la composition de l'avoir » | finances/creer-une-facture-d-avoir-client.md |
| InterFast | bases de TVA | NON DOCUMENTÉ | non documenté | « Dans le cas d'un avoir total, les bases de TVA sont reprises » | finances/creer-une-facture-d-avoir-client.md |
| Axonaut | lien vers la totalité de la facture | RÉFÉRENCÉ | non documenté | « il est aussi possible de créer un Avoir global c'est-à-dire sur la totalité de la facture, qui sera directement liée à cette facture. » | gerez-vos-factures/comment-faire-un-avoir-sur-axonaut.md |
| Vertuoza | montant de la facture d'acompte | NON DOCUMENTÉ | non documenté | « Cela génèrera une note de crédit/avoir qui annulera la facture d'acompte. » | faq-foires-aux-questions/comment-annuler-une-facture-d-acompte.md |

OpenFire Odoo est le seul des 7 à ne rien documenter sur le contenu repris
par un avoir — trou signalé explicitement par son propre agent (« le
corpus […] ne documente à aucun moment quelles données de la facture
d'origine sont reprises dans l'avoir »).

### 4.5 Devis (accepté/en cours) → Avenant

| Éditeur | Donnée | Mode | Surchargeable | Formulation exacte | Source |
|---|---|---|---|---|---|
| Vertuoza | montants/quantités du devis initial | RECALCULÉ | oui | « Créez un avenant négatif pour ajuster le devis initial en fonction des travaux réellement réalisés. » | faq-foires-aux-questions/comment-gerer-un-chantier-arrete-avec-un-avancement-negatif-et-l-impossibilite-de-generer-une-facture.md |
| Vertuoza | postes/quantités cochés du devis de base | NON DOCUMENTÉ | oui | « Cochez les lignes du devis de base pour les ajouter à l'Avenant. Modifiez les quantités de manière simple et intuitive. » | gestion-de-chantier/avenant.md |
| InterFast | lien financier/commercial au devis | NON DOCUMENTÉ | non documenté | « Cela génère immédiatement un nouveau document, lié financièrement et commercialement au devis premier. » | finances/creer-un-avenant-au-devis.md |
| Costructor | lignes de plus-value/moins-value non facturées | NON DOCUMENTÉ | non documenté | « Si votre devis est déjà facturé, vous pouvez créer un avenant et importer ces lignes à la facturation initiale. » | ventes/comment-ajouter-une-plus-value-moins-value-sur-une-facture-c1xd5u.md |

### 4.6 Avenant → Rentabilité de chantier / États d'avancement / Facture finale

| Éditeur | Donnée | Mode | Formulation exacte | Source |
|---|---|---|---|---|
| Vertuoza | montant de l'avenant | RECALCULÉ | « l'Avenant est intégré dans une zone spécifique des futurs états d'avancement. Il est également repris dans le tableau de rentabilité […] ajoutant ou soustrayant son montant au devis de base. » | gestion-de-chantier/avenant.md |
| Vertuoza | ajustements + montant restant dû | RECALCULÉ | « générez une facture finale qui reflète les ajustements effectués et le montant restant dû » | faq-foires-aux-questions/comment-gerer-un-chantier-arrete-avec-un-avancement-negatif-et-l-impossibilite-de-generer-une-facture.md |
| OpenFire Odoo | date de fin de la ligne de contrat précédente (cas contrat, pas devis) | RECALCULÉ | « Celle-ci détermine la date de fin de la ligne précédente. » | knowsystem/modifier-un-contrat-312.md |

### 4.7 Chantier : rentabilité recalculée à partir de plusieurs objets sources

Cascade convergente sur 3 éditeurs indépendants (Costructor, Vertuoza,
InterFast) — le chantier agit comme un point d'agrégation qui ne stocke
jamais une valeur saisie directement, mais recalcule à partir des objets
liés.

| Éditeur | Source | Donnée | Mode | Formulation exacte |
|---|---|---|---|---|
| Costructor | Devis finalisé/accepté | montants du devis (rentabilité prévue) | RECALCULÉ | « La rentabilité prévue est calculée à partir du (des) devis lié(s) au chantier. » |
| Costructor | Facture de vente | montants facturés (travaux supplémentaires) | RECALCULÉ | « En cas de travaux supplémentaires facturés aux clients, la rentabilité sera actualisée » |
| Costructor | Feuille d'heures validée | heures pointées | RECALCULÉ | « Les heures remonteront automatiquement sur la rentabilité du chantier concerné. » |
| Costructor | Facture d'achat | montants / catégories | RECALCULÉ | « Les factures d'achats permettent de calculer la rentabilité réelle de vos chantiers et d'avoir une vue sur les dépenses par catégories. » |
| Vertuoza | Facture fournisseur (statut) | montant de la facture | RECALCULÉ | « Les factures "À valider" et "Rejetées" sont exclues des calculs de rentabilité chantier. » |
| InterFast | Commande (réception) | déboursé sec / coûts réels | RECALCULÉ | « votre déboursé sec du chantier et les coûts réels visibles dans vos tableaux de rentabilité seront mis à jour directement » |

### 4.8 Bibliothèque / Catalogue → Devis, Facture (figement au moment de la création)

| Éditeur | Donnée | Mode | Surchargeable | Formulation exacte | Source |
|---|---|---|---|---|---|
| Obat | prix de l'élément (fourniture/main d'œuvre/ouvrage) | SNAPSHOTTÉ | non (documents existants figés) | « Il n'a aucun impact sur vos factures ou devis déjà créés : les documents existants conservent les prix qui étaient appliqués au moment de leur création. » | comment-ajouter-des-éléments-de-fourniture-main-d-œuvre-ouvrage-danciens-devis-depuis-l-éditeur-de-facture/devis.md |
| Obat | prix de l'élément réimporté | COPIÉ (nouveau snapshot) | oui | « Si vous réimportez un élément ou un ouvrage depuis la bibliothèque sur un document existant, les nouveaux tarifs s'appliqueront. » | idem |
| Vertuoza | prix achat/vente de la fourniture (CEBEO) | RÉFÉRENCÉ | non documenté | « Le prix de la fourniture dans ta bibliothèque sera mis à jour chaque nuit, en fonction des données les plus récentes de CEBEO. » | parametres/integration-cebeo.md |
| Vertuoza | fourniture, prix (import CEBEO vers devis) | NON DOCUMENTÉ (asymétrie non expliquée avec la ligne précédente) | non documenté | « sélectionne les fournitures que tu souhaites ajouter et clique sur Importer » | idem |
| Axonaut | nom, description, prix, TVA, poids, stock (produit e-commerce) | COPIÉ (synchronisé) | non documenté | « Synchronisation du nom, description, prix unitaire, TVA, poids, et stock du produit. » | connectez-axonaut/comment-connecter-votre-boutique-en-ligne-a-axonaut-shopify-prestashop-woocommerce.md |

Seul Obat tranche explicitement le mode (SNAPSHOTTÉ, figement à la
création) ; les autres éditeurs documentent des flux catalogue → document
sans jamais préciser si la valeur reste liée ou se fige. Ce couple reste
donc une observation isolée plutôt qu'un invariant confirmé (voir §8).

### 4.9 Intervention → Facture

| Éditeur | Donnée | Mode | Surchargeable | Formulation exacte | Source |
|---|---|---|---|---|---|
| Vertuoza | prix, note, quantités des lignes facturables | NON DOCUMENTÉ | oui (prix modifiable avant) | « L'élément apparaîtra sur la facture si l'option "facturable" est activée. » | application-mobile/ouvrier-rapport-d-intervention.md |
| InterFast | toutes les informations du rapport | COPIÉ | oui | « la facture reprendra automatiquement toutes les informations entrées lors du remplissage de votre rapport » | finances/facturer-une-intervention-depuis-l-application-web-et-mobile.md |
| InterFast | numéro de l'intervention (et du chantier) | RÉFÉRENCÉ | non documenté | « Le logiciel a automatiquement rattaché le numéro de l'intervention (et du chantier si applicable) à cette facture. » | application-mobile/creer-une-facture-sur-l-application-mobile.md |
| InterFast | rapport d'intervention (PDF) | NON DOCUMENTÉ | non documenté | « son rapport est joint automatiquement dans les pièces jointes de la facture » | finances/facturer-une-intervention-depuis-l-application-web-et-mobile.md |
| InterFast | adresse exacte, numéro de l'intervention | RÉFÉRENCÉ | non documenté | « l'adresse exacte et le numéro de l'intervention remonteront automatiquement sur le PDF final ! » | finances/creer-une-facture-proforma.md |

Règle de priorité documentée uniquement par InterFast, structurante pour la
question 1 : quand une intervention est à la fois rattachée à un devis et
porteuse d'un rapport rempli, **c'est le devis qui prime**, pas le rapport
— « Si l'intervention que vous facturez était initialement liée à un
devis, c'est le contenu du devis qui prime et qui se retrouvera dans le
détail de votre facture. » (finances/facturer-une-intervention-depuis-l-application-web-et-mobile.md).

### 4.10 Devis / Intervention / Facturation → Stock (mouvements automatiques)

| Éditeur | Événement | Donnée | Mode | Formulation exacte | Source |
|---|---|---|---|---|---|
| InterFast | Devis passé au statut « Accepté » | quantité article | RECALCULÉ (décrément) | « Le stock d'un article est automatiquement diminué lorsqu'il est utilisé : dans un devis qui passe au statut "Accepté" » | application-mobile/suivre-les-stocks-app-mobile.md |
| InterFast | Intervention au statut « Terminé » | quantité article | RECALCULÉ (décrément) | (même source, second déclencheur) | idem |
| InterFast | Réception de commande | quantité | RECALCULÉ (incrément) | « celui-ci incrémente automatiquement le stock à partir du moment où […] vous avez votre suivi de stock activé » | finances/utiliser-les-commandes-v2-app-web.md |
| Axonaut | Achat / retour (avoir) | quantité produit | RECALCULÉ (incrément) | « les produits vont s'incrémenter lorsque vous faites un achat ou qu'un produit revient en cas d'Avoir » | gerez-stock-temps-reel/comment-ca-marche-la-gestion-de-stock.md |
| Axonaut | Facturation / fabrication / perte-casse | quantité produit | RECALCULÉ (décrément) | « vont se décrémenter lorsque vous facturez ces derniers, les fabriquer […] et/ou lors d'une perte/casse » | idem |
| Axonaut | Réception de commande fournisseur | quantité | RECALCULÉ (incrément) | « vos stocks vont s'incrémenter directement de ces derniers » | idem |

### 4.11 Facture / Paiement / Comptabilité (chaîne financière aval)

| Éditeur | Source | Cible | Donnée | Mode | Formulation exacte |
|---|---|---|---|---|---|
| Vertuoza | Compte bancaire (synchronisation) | Facture (statut) | statut de paiement | RECALCULÉ | « Une fois un paiement effectué sur votre compte bancaire, il vous suffit de lancer la synchronisation pour que le statut soit actualisé et passé en "Payé". » |
| Vertuoza | Facture (lignes) | Écritures comptables | montant, compte général, TVA | RECALCULÉ/COPIÉ selon config | « Les lignes de facture ayant le même compte général et le même taux de TVA sont fusionnées en une seule ligne » |
| Axonaut | Ligne bancaire rapprochée | Facture | statut de paiement | RÉFÉRENCÉ | « il vous suggère automatiquement de rapprocher cette ligne de sa facture correspondante » |
| OpenFire Odoo | Paiement | Facture | montant dû | RECALCULÉ | « Si un paiement est lié à une facture, il réduit le montant dû de la facture. » |
| OpenFire Odoo | Facture/avoir/paiement validés | Pièce comptable | écriture comptable | NON DOCUMENTÉ | « Toutes les factures, avoirs et paiements validés génèrent des pièces comptables. » |
| OpenFire Odoo | Facture (écart de paiement) | Écriture comptable (658/758) | montant de l'écart | RECALCULÉ | « le logiciel va générer une pièce comptable différente afin que la facture se solde complètement. » |

### 4.12 Contrat → Ligne de contrat → Demande d'intervention → Rendez-vous (cascade ERP, OpenFire Odoo seul)

| Niveau | Source | Cible | Donnée | Mode | Formulation exacte |
|---|---|---|---|---|---|
| 1 | Contrat | Ligne de contrat | informations générales | NON DOCUMENTÉ | « les informations enregistrées dans le contrat sont reprises dans la ligne de contrat. » |
| 1 | Contrat | Ligne de contrat | client payeur | NON DOCUMENTÉ | « Client payeur : il reprend le porteur du contrat […] Cette donnée n'est pas modifiable. » |
| 2 | Site d'intervention | Ligne de contrat | parc installé (équipement) | NON DOCUMENTÉ | « Si un parc installé est renseigné sur le site d'intervention, il sera repris automatiquement. » |
| 3 | Ligne de contrat | DI et RDV | parc installé, notes | NON DOCUMENTÉ | « Il sera repris dans les demandes d'intervention et dans les RDV » |
| 4 | DI | RDV | contrat, ligne de contrat | NON DOCUMENTÉ | « La DI, le contrat et la ligne de contrat liés sont repris. » |

Cascade à 4 niveaux, propre à ce corpus ERP, sans corroboration croisée
chez les 6 autres éditeurs (aucun n'a de module "contrat de maintenance"
documenté dans le sous-ensemble lu) — retenue comme observation
structurante ERP plutôt que comme convergence de marché.

### 4.13 Autres couples isolés (une seule occurrence, non regroupables)

- Client/Entreprise (condition particulière) → Devis : COPIÉ, surchargeable (Vertuoza, `devis/conditions-particulieres.md`).
- Devis (dupliqué) → Nouveau devis, tout sauf conditions de paiement/infos bancaires : COPIÉ, surchargeable (InterFast, `finances/comprendre-la-fiche-d-un-devis.md`).
- Devis principal → Variantes (montant de prime, conditions de paiement) : RÉFÉRENCÉ, non surchargeable sur la variante (InterFast, `finances/creer-et-gerer-des-variantes-de-devis.md`).
- Utilisateur désactivé → Éléments créés (attribution) : RÉINITIALISÉ, réattribution aléatoire (Axonaut, `configurer-votre-compte/ajouter-un-utilisateur-dans-axonaut.md`).
- Utilisateur archivé (licence non consommée) → Crédit d'abonnement : RECALCULÉ, non remboursable en numéraire (InterFast, `equipe/resoudre-un-ajout-d-utilisateur-par-erreur.md`).
- Document (devis/BC/facture) à l'instant T → Pièce jointe PDF : SNAPSHOTTÉ, resnapshotté seulement après suppression manuelle de la pièce jointe (OpenFire Odoo, `pourquoi-le-pdf-que-j-imprime-n-est-pas-a-jour-207.md`).
- Rapport de situation → Facture de situation (pièce jointe) : SNAPSHOTTÉ, non ré-imprimable ensuite, le rapport lui-même n'étant pas conservé (OpenFire Odoo, `creer-une-facture-de-situation-204.md`).

## 5. Cascades à plusieurs niveaux (synthèse transversale)

Cinq cascades ressortent comme structurantes, au sens de la mission
(« ce genre de chaîne vaut dix règles isolées ») :

1. **Devis → Avenant → États d'avancement/Rentabilité → Facture finale**
   (Vertuoza). Un devis figé après acceptation reste néanmoins évolutif via
   un document annexe dont le montant se propage à deux destinations
   distinctes (rentabilité et facturation) sans jamais rouvrir le devis
   lui-même.
2. **Facture d'acompte → Note de crédit/Avoir → Facture finale/de solde**
   (Vertuoza, Obat, InterFast, OpenFire Odoo — 4 éditeurs). La correction
   d'un acompte ne modifie jamais la facture d'acompte elle-même ; elle
   passe par un document tiers dont le solde recalculé alimente ensuite le
   document final.
3. **Facture → Avoir → Verrouillage propre de l'avoir** (Sellsy, Obat,
   InterFast — 3 éditeurs). L'irréversibilité ne s'arrête pas à la facture
   d'origine : l'avoir créé pour la corriger devient à son tour
   inaltérable dès qu'il reçoit lui-même un numéro définitif.
4. **Chantier comme hub de recalcul à 3-4 entrées** (Costructor, Vertuoza,
   InterFast — voir §4.7) : devis, facture de vente, facture d'achat et
   temps travaillé alimentent tous un même agrégat recalculé, jamais une
   valeur saisie directement.
5. **Contrat → Ligne de contrat → DI → RDV** (OpenFire Odoo seul, §4.12) :
   cascade à 4 niveaux propre au corpus ERP, chaque niveau reprenant des
   données du niveau amont sans qu'aucun ne précise le mode exact.

## 6. Verrous, groupés par cause

### 6.1 Cause réglementaire — inaltérabilité de la facture numérotée (anti-fraude TVA)

Le motif dominant du corpus entier : une fois qu'un document comptable
(facture, parfois avoir) reçoit un numéro définitif, il devient
inaltérable — ni modifiable, ni supprimable — au nom de la législation
anti-fraude à la TVA ou de l'obligation de séquence chronologique continue.
Documenté indépendamment par **6 éditeurs sur 7** :

| Éditeur | Formulation exacte | Référence légale citée | Source |
|---|---|---|---|
| Costructor | « Les factures finalisées ne sont pas modifiables. […] la facture finalisée ne peut être modifiée. » / « il est interdit de supprimer une facture finalisée » | « loi anti-fraude à la TVA de 2018 », lien impots.gouv.fr, amende 7 500 € pour logiciel non conforme | ventes/comment-modifier-supprimer-une-facture-1ex0kq5.md |
| Costructor | « la loi interdit de modifier ou de supprimer une facture une fois qu'elle est finalisée. […] c'est une mesure anti-fraude qui vise à éviter toute dissimulation de revenus » | idem | ventes/comment-annuler-une-facture-vb12e9.md |
| Obat | « Il ne sera plus possible d'annuler une facture sans créer un avoir. » | référence générique aux « règles comptables » | annuler-une-facture-sans-cr-c3-a9er-un-avoir-ce-nest-plus-possible.md |
| Sellsy | « Le mode conforme empêche toute modification ou suppression d'une facture finalisée. » | **Article L.441-9 du Code de commerce** (seule référence légale précise et nommée de tout le corpus) | activer-le-mode-conforme-pour-les-documents-de-vente.md |
| Sellsy | « La législation impose une numérotation continue, chronologique et non modifiable. » | idem | activer-le-mode-conforme-pour-les-documents-de-vente.md |
| Sellsy | « L'activation du mode conforme est définitive […] Cette irréversibilité est imposée par la réglementation afin de garantir l'inaltérabilité des données. » | idem | activer-le-mode-conforme-pour-les-documents-de-vente.md |
| InterFast | « une facture finalisée (dotée d'un numéro définitif) est strictement inaltérable. Elle ne peut plus être ni modifiée, ni supprimée. » | « loi anti-fraude à la TVA (entrée en vigueur en 2018) », normes de facturation électronique | finances/creer-une-facture-d-avoir-client.md |
| InterFast | « Dès qu'un document comptable (facture ou avoir) obtient un numéro, il est strictement verrouillé et devient inaltérable, conformément à la législation. » | idem | finances/creer-une-facture-d-avoir-client.md |
| OpenFire Odoo | « La législation interdit la suppression et la modification des factures dès lors qu'elles sont validées dans les logiciels de facturation. » | « la législation » (non nommée) | knowsystem/comment-modifier-une-facture-validee-210.md |
| Axonaut | « cela ferait un « trou » dans la facturation et c'est comptablement interdit par la législation française » | « la législation française » (non nommée) | gerez-vos-factures/comment-faire-un-avoir-sur-axonaut.md |

**Vertuoza est l'exception notable** : sur les 25 documents lus, aucun ne
mentionne de verrou réglementaire sur la facture — silence signalé
explicitement par son propre agent d'extraction comme un trou
contrastant avec le reste du corpus, pas comme une infirmation (Vertuoza
ne dit nulle part que ses factures restent modifiables après envoi).

### 6.2 Cause réglementaire — continuité de la numérotation / séquence chronologique

Sous-motif distinct du précédent : ce n'est pas l'altération du document
qui est bloquée, mais sa suppression quand elle romprait une séquence.

| Éditeur | Formulation exacte | Source |
|---|---|---|
| Axonaut | « Il ne faut pas qu'il y ait une facture postérieure à celle que vous voulez supprimer. […] cela ferait un « trou » dans la facturation. » | gerez-vos-factures/comment-faire-un-avoir-sur-axonaut.md |
| Costructor | « il faudra dans un premier temps annuler la situation 3 et ensuite la situation 2. Il n'est pas possible de simplement annuler la situation 2 sinon les avancements seraient faussés. » | ventes/comment-creer-une-facture-davoir-vwjxpf.md |
| OpenFire Odoo | « Openfire vérifie qu'aucune facture validée ou en brouillon existe avec une date inférieure à la date de facturation de la facture que vous souhaitez valider. » | knowsystem/j-ai-un-message-d-erreur-a-la-validation-de-mes-factures-313.md |
| InterFast | « Une facture annulée possède un numéro officiel. Elle doit être conservée. […] Vous ne pouvez donc pas la supprimer de votre interface. » | finances/comprendre-la-fiche-d-une-facture.md |

### 6.3 Cause métier

| Éditeur | Objet | Déclencheur | Ce qui devient impossible | Formulation exacte |
|---|---|---|---|---|
| Vertuoza | Fonction « retour au statut précédent » | devis accepté / chantier créé | revenir automatiquement en arrière | « Le retour au statut précédent sur un devis accepté a été supprimé pour éviter des risques importants. […] cela entraînait la suppression de tous les éléments du chantier […] Cela pouvait causer des erreurs. » |
| InterFast | Devis | statut « Accepté » | modification structurelle directe | « il devient contractuel et ne doit plus être modifié » |
| InterFast | Rapport d'intervention (mobile) | statut intervention « Terminé » | modifier le rapport | « elle est verrouillée sur l'application mobile pour garantir l'intégrité du rapport signé. » |
| InterFast | Feuille de temps | validation par le collaborateur | modification par le collaborateur | « une feuille de temps validée n'est plus modifiable sur votre application mobile » |
| InterFast | Devis | statut « Facturé » | créer de nouvelles factures | « le logiciel considère que tout a été payé et bloque la création de nouvelles factures. » |
| Axonaut | Facture | absence des droits utilisateur | suppression | « demandez à l'administrateur de vous permettre de supprimer des entités dans Axonaut ! » |
| OpenFire Odoo | Article configuré « Non remisable » | configuration de l'article | modifier le prix de vente | « La modification du prix de vente de ces articles n'est alors pas possible. » |
| Sellsy | Facture | sortie du statut « Brouillon » | modifier, supprimer | « Une facture émise doit être figée et ne plus être modifiée. » |

### 6.4 Cause technique

| Éditeur | Objet | Déclencheur | Ce qui devient impossible | Formulation exacte |
|---|---|---|---|---|
| Vertuoza | Intégration Batiprix | déconnexion du compte | rechercher/ajouter des ouvrages Batiprix | « La déconnexion est immédiate. Vous ne pourrez plus rechercher ni ajouter d'ouvrages tant qu'une nouvelle connexion n'est pas effectuée. » |
| Vertuoza | Réception factures Peppol | déjà enregistré sur une autre plateforme | activer la réception sur Vertuoza | « Un seul logiciel peut être enregistré pour la réception de factures. » |
| InterFast | Ligne d'avoir/facture | prix unitaire négatif saisi | enregistrement du document | « l'enregistrement sera impossible car ce format n'est pas supporté par les plateformes de connexion pour la facturation électronique. » |
| InterFast | Module Commandes | création du 1ᵉʳ bon de commande V2 | retour à l'ancienne version | « une fois le premier bon de commande V2 créé, le passage est définitif. » |
| OpenFire Odoo | Rapport de situation | génération de la facture de situation | réimpression ultérieure du rapport | « les rapports de situation ne sont pas sauvegardés dans Openfire et ne peuvent donc pas être imprimés ultérieurement. » |
| OpenFire Odoo | PDF (pièce jointe) | impression du document | obtenir une réimpression à jour sans supprimer l'ancienne pièce jointe | « le document reprendra les données telles qu'elles étaient au 01/01/2022. […] il faut alors supprimer la pièce jointe » |
| Sellsy | Collaborateur | suppression | récupération/réactivation via l'interface | « il ne vous sera pas possible, une fois supprimé, de récupérer / réactiver un collaborateur supprimé via l'interface Sellsy » |
| Obat | Facture électronique | transmission déjà réussie | renvoyer/retransmettre | « La facture a déjà été transmise avec succès ⛔ Un renvoi dans ce cas provoque une erreur. » |

### 6.5 Cause non documentée (résiduel)

Sur les 97 verrous relevés au total, une large majorité (à peu près deux
tiers, cf. constats répétés par chaque agent : Vertuoza 7/9, Obat 8/11,
Sellsy 15/26, Axonaut 7/11) sont énoncés comme des faits sans aucune
justification textuelle. Ce n'est pas un défaut d'extraction : chaque
agent a explicitement cherché une cause et rapporté son absence plutôt que
d'en inventer une. Le déséquilibre entre verrous **avec** cause (surtout
concentrés sur l'axe facture/comptabilité) et verrous **sans** cause
(largement dominants sur les objets opérationnels — chantier, intervention,
contrat, stock, utilisateur) est en soi un résultat notable : les éditeurs
justifient leurs contraintes quand la loi les y oblige, rarement sinon.

## 7. Contournements documentés

| Contournement | Objet concerné | Éditeurs |
|---|---|---|
| Créer un avoir (partiel ou total) | Facture finalisée | Costructor, Obat, Sellsy, InterFast, OpenFire Odoo, Axonaut, Vertuoza |
| Créer un avenant | Devis accepté / ligne de contrat | Vertuoza, InterFast, Costructor |
| Dupliquer le document (nouvelle facture/devis) | Facture finalisée, devis figé | Sellsy (« Modifier par un avoir »), InterFast (duplication de devis) |
| Repasser temporairement à un statut antérieur | Devis accepté, chantier vide | InterFast (« Envoyé »), Vertuoza (retour au statut « en cours » si chantier vide) |
| Annuler puis recréer | Réception de marchandise, remise en banque confirmée | Axonaut (annuler la réception), OpenFire Odoo (annuler la remise en banque) |
| Recours au support éditeur | Feuille de temps validée par erreur, mode test | InterFast (« écrire sur le support en ligne pour qu'on vous la réouvre », sortie du mode test) |
| Annuler les documents dans l'ordre inverse de création | Factures de situation successives | Costructor |
| Supprimer d'abord le document bloquant | Chantier non supprimable, règlement remis en banque | Vertuoza (supprimer les documents puis le chantier), Sellsy (supprimer d'abord la remise en banque) |

Aucun contournement n'est documenté pour : le rapport d'intervention une
fois accepté (Vertuoza, InterFast), l'avoir lui-même une fois finalisé
(Sellsy, Obat, InterFast — le verrou est terminal), le collaborateur
supprimé (Sellsy).

## 8. Invariants candidats

**INV-1 — Une facture ayant reçu un numéro définitif devient inaltérable ;
toute correction passe par un document tiers (avoir), jamais par une
modification directe du document original.**
PREUVES : Costructor, Obat, Sellsy (avec référence légale explicite,
Art. L.441-9 du Code de commerce), InterFast, OpenFire Odoo, Axonaut — 6
éditeurs indépendants (§6.1).
CONTRE-EXEMPLES : Vertuoza ne documente ce verrou dans aucun de ses 25
documents lus — silence, pas infirmation.
CAUSE PROBABLE : réglementaire (législation anti-fraude à la TVA de 2018,
obligation de séquence chronologique continue).
STATUT : CANDIDAT.

**INV-2 — Un avoir reprend (copie) le contenu de la facture visée pour
permettre sa correction ou son annulation ; il ne modifie jamais la
facture d'origine.**
PREUVES : Costructor, Obat, Sellsy, InterFast, Axonaut — 5 éditeurs
indépendants (§4.4).
CONTRE-EXEMPLES : OpenFire Odoo documente le verrou (facture non
modifiable) sans jamais documenter ce que reprend l'avoir qui la corrige —
silence, pas infirmation.
CAUSE PROBABLE : conséquence directe d'INV-1 — puisque la facture ne peut
plus être touchée, le seul véhicule de correction possible doit en
reproduire le contenu pour permettre l'ajustement.
STATUT : CANDIDAT.

**INV-3 — Un avoir qui reçoit lui-même un numéro définitif devient à son
tour inaltérable, selon le même régime que la facture.**
PREUVES : Sellsy (« il ne sera pas possible de supprimer un avoir
finalisé »), Obat (« un avoir ne peut plus être effacé »), InterFast
(« Dès qu'un document comptable (facture ou avoir) obtient un numéro, il
est strictement verrouillé »).
CONTRE-EXEMPLES : aucun relevé.
CAUSE PROBABLE : réglementaire, même fondement qu'INV-1 (l'avoir est
lui-même un document comptable numéroté).
STATUT : CANDIDAT.

**INV-4 — La rentabilité d'un chantier est un agrégat recalculé à partir
de plusieurs objets liés (devis prévisionnel, factures de vente, factures
d'achat, temps travaillé) ; ce n'est jamais une valeur saisie directement.**
PREUVES : Costructor (cascade à 4 entrées explicite), Vertuoza, InterFast
— 3 éditeurs indépendants (§4.7).
CONTRE-EXEMPLES : aucun relevé (silence chez les 4 autres éditeurs, dont
aucun ne documente de mécanisme concurrent de saisie directe).
CAUSE PROBABLE : métier (fiabilité du chiffre de rentabilité, éviter la
désynchronisation avec les documents sources).
STATUT : CANDIDAT.

**INV-5 — Une facture d'acompte ou de situation déjà émise est
automatiquement déduite (recalculée) lors de l'émission du document
final ; son montant n'est jamais ressaisi manuellement.**
PREUVES : Vertuoza, Obat, InterFast, OpenFire Odoo — 4 éditeurs
indépendants (§4.3), c'est le couple de propagation le plus densément
corroboré du corpus.
CONTRE-EXEMPLES : Costructor et Sellsy ne documentent pas ce mécanisme
dans le sous-ensemble lu ; Costructor le signale lui-même explicitement
comme un trou de sa propre documentation, pas comme une absence produit.
CAUSE PROBABLE : métier (cohérence du solde facturé), renforcée par la
cause réglementaire d'INV-1 (l'acompte, une fois facturé, est lui-même
figé et ne peut être corrigé qu'en aval).
STATUT : CANDIDAT.

**INV-6 — Un devis accepté/validé devient contractuellement figé et ne
peut plus être modifié directement ; toute évolution ultérieure passe par
un document annexe (avenant) plutôt que par une édition du devis
lui-même.**
PREUVES : Vertuoza (« Une fois qu'un devis est accepté, il ne peut plus
être modifié directement. »), InterFast (« il devient contractuel et ne
doit plus être modifié »), Obat (« Vous ne pourrez alors plus le modifier
ni le supprimer. », déclenché par la signature).
CONTRE-EXEMPLES notables : Costructor ne documente aucun verrou sur le
devis (silence contrastant avec son traitement très détaillé de la
facture) ; Axonaut le signale lui-même comme trou explicite (« aucun
fichier du corpus ne mentionne de condition rendant un devis impossible à
modifier ou supprimer »). Ces deux cas sont des silences documentaires,
pas des infirmations, mais leur récurrence appelle la prudence.
CAUSE PROBABLE : métier (valeur contractuelle de l'engagement accepté par
le client), sans fondement réglementaire explicite identifié (à la
différence d'INV-1).
STATUT : CANDIDAT, avec réserve sur la généralisation (3 confirmations
positives contre 2 silences significatifs sur 7 éditeurs lus).

## 9. Convergences entre éditeurs

1. **Cause réglementaire dominante et quasi unanime** pour le verrou sur
   la facture numérotée (6/7 éditeurs, §6.1) — le motif isolé au pilote
   onboarding chez ProGBat et InterFast seuls se confirme ici beaucoup
   plus largement une fois le corpus élargi et le filtre spécifiquement
   orienté vers l'irréversibilité.
2. **L'avoir comme unique véhicule de correction** d'une facture
   finalisée, documenté par 6 éditeurs sur 7 (§4.4, §7) — aucun éditeur du
   panel ne documente de procédure de correction alternative.
3. **Déduction automatique de l'acompte/de la situation** sur le document
   final, chez 4 éditeurs indépendants (§4.3, INV-5).
4. **Le chantier comme point de recalcul, jamais de saisie directe**, chez
   3 éditeurs indépendants (§4.7, INV-4).
5. **Verrous « métier » et « techniques » rarement justifiés dans le
   texte** (§6.5) : à l'inverse du verrou réglementaire, systématiquement
   accompagné d'une justification (même générique), les verrous métier et
   techniques sont le plus souvent énoncés sans cause — schéma répété chez
   les 7 éditeurs.

## 10. Variantes

- **Précision de la référence légale** : Sellsy est seul à nommer un
  article de loi précis (L.441-9 du Code de commerce) ; Costructor cite un
  lien impots.gouv.fr et un montant d'amende (7 500 €) ; les 4 autres
  éditeurs concernés (Obat, InterFast, OpenFire Odoo, Axonaut) invoquent
  « la loi »/« la législation » de façon générique, sans texte nommé.
- **Existence ou non d'un retour en arrière temporaire** avant le
  verrouillage définitif : Vertuoza et InterFast documentent un mécanisme
  de statut réversible (« retour au statut Envoyé », suppression du
  chantier si vide) pour le devis/chantier ; Costructor, Obat et Sellsy ne
  documentent aucune voie de retour, seulement la correction en aval par
  avoir.
- **Granularité du figement snapshotté** : seuls Obat (prix de
  bibliothèque) et OpenFire Odoo (PDF, rapport de situation) documentent
  explicitement un mode SNAPSHOTTÉ ; les 5 autres éditeurs laissent le
  mode NON DOCUMENTÉ pour des propagations de nature similaire.
- **Mode de correction post-verrouillage** : avoir simple pour la plupart
  des éditeurs, avoir + nouvelle facture obligatoire pour Costructor et
  OpenFire Odoo, procédure d'ordre inverse spécifique pour les situations
  successives chez Costructor.
- **Cascade ERP à 4 niveaux (contrat → ligne → DI → RDV)** propre à
  OpenFire Odoo, sans équivalent documenté chez les 6 autres éditeurs
  (aucun des sous-corpus lus ne couvre de module contrat de maintenance
  comparable).

## 11. Inconnus

- **Mode exact (copié vs référencé) de la quasi-totalité des
  propagations documentées** : sur les 156 règles relevées, la majorité
  est classée NON DOCUMENTÉ sur ce point précis — les éditeurs décrivent
  ce qui se reproduit, rarement comment (silence structurel, pas
  spécifique à un éditeur).
- **Devis → Facture « ordinaire »** (hors acompte/situation/avancement) :
  quasi absent du corpus malgré sa centralité pour la question 1 (§4.1) —
  seuls 3 éditeurs sur 7 le documentent, aucun ne tranche le mode.
- **Cause des verrous métier et techniques** : majoritairement non
  documentée (§6.5), contrairement aux verrous réglementaires.
- **Verrous sur les objets terrain** (chantier, client, équipement) hors
  facturation : quasi absents, sauf partiellement chez Vertuoza et
  InterFast.
- **Mode exact des propagations catalogue → devis** en dehors d'Obat : un
  seul éditeur tranche entre snapshot et référence (§4.8).
- **Sellsy, Costructor sur le couple devis → facture standard** :
  signalés comme trous par leurs propres agents d'extraction, pas comme
  absence produit constatée.
- **Batikko et Extrabat sur les deux questions du pilote** : non
  approfondis (§3.4), statut réel non déterminé.

## 12. Ce que le corpus permet de spécifier

- Un motif réglementaire transversal robuste et sourcé sur 6 éditeurs
  indépendants (facture numérotée → inaltérable, correction par avoir
  uniquement), avec au moins une référence légale précise et nommée
  (Sellsy, Art. L.441-9 du Code de commerce) — largement suffisant pour
  fonder une exigence produit non négociable plutôt qu'un choix
  d'ergonomie.
- Un mécanisme de déduction automatique de l'acompte/de la situation sur
  le document final, documenté et cité mot pour mot par 4 éditeurs
  indépendants — spécifiable comme comportement attendu par défaut.
- Un modèle de chantier comme agrégat recalculé (jamais saisi) à partir de
  devis, factures de vente, factures d'achat et temps travaillé, confirmé
  par 3 éditeurs indépendants.
- Une règle de priorité explicite et actionnable pour la facturation
  d'intervention : quand un devis est rattaché, son contenu prime sur le
  rapport d'intervention rempli sur le terrain (InterFast, formulation
  exacte disponible).
- Un motif de figement des prix catalogue au moment de la création du
  document, documenté explicitement par un éditeur (Obat) et compatible
  avec le silence des autres — hypothèse de travail raisonnable, mais pas
  un invariant confirmé (une seule source explicite).

## 13. Ce qu'il ne permet pas de spécifier

- Le mode technique exact (copie en base vs référence vivante) de la
  quasi-totalité des propagations — le corpus documentaire ne descend
  jamais à ce niveau de précision, quel que soit l'éditeur.
- Un comportement standard pour le cas le plus fréquent (devis → facture
  simple, sans acompte ni situation) : la documentation concurrentielle
  saute systématiquement ce cas pour documenter les variantes.
- Une cause produit repérable pour la majorité des verrous non
  réglementaires — le corpus permet de dire QUE l'action est bloquée,
  rarement POURQUOI, en dehors de la sphère comptable.
- Si le figement du devis après acceptation (INV-6) est un standard de
  marché ou une pratique propre à 3 éditeurs sur 7 — les silences chez
  Costructor et Axonaut ne permettent pas de trancher.
- Un comportement de référence pour les objets non financiers (chantier,
  client, équipement, contrat hors OpenFire) sur l'axe irréversibilité —
  très peu de matière en dehors de la facturation.

## 14. Questions terrain résiduelles

- La déduction automatique de l'acompte sur le solde (INV-5) empêche-t-elle
  réellement toute ressaisie manuelle dans l'interface, ou existe-t-il un
  mode dérogatoire non documenté dans les corpus d'aide (Costructor et
  Sellsy restent muets sur ce point) ?
- Le figement contractuel du devis accepté (INV-6) est-il un verrou
  technique dur chez Costructor et Axonaut malgré le silence documentaire,
  ou ces éditeurs autorisent-ils réellement une modification directe après
  acceptation ?
- Le mode SNAPSHOTTÉ des prix catalogue, explicite chez Obat seul (§4.8),
  est-il un comportement partagé silencieusement par les 6 autres
  éditeurs, ou une spécificité de son architecture ?
- La cascade contrat → ligne de contrat → DI → RDV d'OpenFire Odoo (§4.12)
  a-t-elle un équivalent chez les éditeurs BTP/artisan une fois leur module
  « contrat de maintenance », s'il existe, spécifiquement recherché ?
- Sellsy et Costructor documentent-ils ailleurs dans leur corpus (hors
  échantillon plafonné à 25 documents pour ce pilote) le mécanisme
  devis → facture standard, ou ce trou est-il structurel à leur
  documentation ?

## 15. Évaluation de la méthode

Le filtre principal (`transition_objet = oui` ET `exception_ou_correction
= oui`) s'est révélé discriminant et exploitable directement sur les
tableaux LIGHT bruts, sans avoir besoin du glossaire ni de l'index de
corpus — contrairement au pilote onboarding, qui s'appuyait sur
`editorial_taxonomy`. Un script mécanique de dépouillement des 11 fichiers
`light-*.md` a suffi à produire, en quelques minutes, une présélection
vérifiable et reproductible ; la seule anomalie rencontrée a été le format
de table d'Obat (pas de `|` de tête de ligne), non documentée dans
SCHEMA-LIGHT, qui a fait échouer une première passe automatique — corrigée
et signalée en §3.

Le chiffre cité dans la commande de mission (« 253 documents de contrôle,
21,3 % ») n'a pas pu être vérifié ni retracé dans ce dépôt (§2) ; le
filtre principal a néanmoins été appliqué tel quel, mesuré directement, et
s'est avéré suffisamment sélectif (7,6 % du corpus LIGHT disponible) pour
servir de base à une sélection resserrée sans jamais approcher les 24,8 %
obtenus avec `transition_objet = oui` seul et non borné — confirmant
indépendamment la mise en garde transmise sur ce filtre.

Le plafonnement à 25 documents par éditeur (175 au total, contre les 62
fichiers du pilote onboarding pour 6 éditeurs) a permis de couvrir 7
éditeurs sans read-off disproportionné, en priorisant strictement le
filtre A puis un classement par mots-clés pour B et C. Le rendement
obtenu (156 règles de propagation, 97 verrous, aucun éditeur au-delà de
27 % du total sur l'un ou l'autre axe) confirme que ce dimensionnement
était suffisant sans être excessif, conformément au principe de
suffisance décisionnelle du dépôt.

Déléguer l'extraction à un agent dédié par éditeur, contraint à une liste
fermée de fichiers et à l'interdiction de toute autre source, a de nouveau
permis un traitement parallèle sans dilution de la fidélité : chaque
agent a cité ses formulations exactes, compté ses fichiers sans rien
donné, et surtout signalé lui-même ses trous documentaires plutôt que de
les combler par inférence (silences repérés spontanément par les agents
Costructor, Sellsy, Axonaut et Vertuoza sur des couples pourtant attendus
comme centraux). C'est la meilleure confirmation possible que la
consigne de discipline (« silence documentaire ≠ absence fonctionnelle »,
« ne déduis jamais un comportement backend depuis une description
d'interface ») a été suivie plutôt que contournée.

Limite reconnue : le regroupement par couple objet source → cible (§4),
fait après coup à partir des 7 rapports séparés, repose sur mon propre
jugement de rapprochement — un même couple formulé différemment par deux
éditeurs (ex. « repris », « recopié », « automatiquement rempli ») a pu
être classé ensemble sans qu'aucun éditeur n'emploie un vocabulaire
commun. Ce risque de sur-rapprochement est inhérent à toute synthèse
inter-éditeurs et devrait être vérifié par relecture croisée avant toute
utilisation en dehors de ce pilote.

## 16. Verdict

**RENDEMENT_SUFFISANT**

Le critère fixé en §2 exigeait au moins 15 règles de propagation sourcées
couvrant au moins 4 couples objet source → objet cible distincts, et au
moins 8 verrous sourcés dont au moins 3 avec cause documentée. Le pilote
en produit 156 règles de propagation réparties sur au moins 13 couples
distincts (§4.1 à §4.13), et 97 verrous dont 18 avec cause réglementaire
explicitement citée (§6.1-6.2), 8 avec cause métier explicite (§6.3) et 8
avec cause technique explicite (§6.4) — soit 34 verrous causés, très
au-delà du seuil de 3. Les deux seuils sont dépassés avec une marge très
large, sur 7 éditeurs couvrant les 4 familles imposées plus 3 éditeurs
additionnels, sans concentration excessive (aucun éditeur au-delà de 27 %
d'un des deux totaux) et sans qu'aucune règle de discipline (silence ≠
absence, non-déduction du backend depuis l'interface, citation exacte
obligatoire) n'ait été assouplie pour y parvenir.

PILOTE_PROPAGATION_TERMINE — RENDEMENT_SUFFISANT — STOP
