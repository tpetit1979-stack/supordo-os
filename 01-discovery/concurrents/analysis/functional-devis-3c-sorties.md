# 3C — Sorties, propagation et recovery du devis : exploitation fonctionnelle ciblée

Mission ciblée, un seul sous-problème (ce que produit un devis vers l'aval), un
seul livrable, un seul verdict, puis stop. Ferme la trilogie ouverte par
`functional-devis-3a-naissance.md` (verdict `DEVIS_3A_TERMINE — EXPLOITABLE —
STOP`) et poursuivie par `functional-devis-3b-cycle.md` (verdict
`DEVIS_3B_TERMINE — EXPLOITABLE — STOP`). Ne modifie ni LIGHT, ni V2, ni V3, ni
les pilotes historiques. Ne prend aucune décision produit SUPORDO définitive.

## 1. Question et périmètre

> Une fois qu'un devis atteint l'événement approprié (finalisation,
> acceptation, signature, confirmation ou autre selon l'éditeur), quels objets
> métier peuvent naître ou être modifiés, sous quelles conditions, avec
> quelles données issues du devis, avec quels effets observables, et que se
> passe-t-il lorsque cette continuité échoue ou doit être corrigée ?

Une facture, une commande, un chantier ou une intervention ne sont étudiés ici
QUE comme objet cible issu ou affecté par le devis — jamais comme objet à part
entière. Dès qu'une question aurait exigé de suivre le cycle propre d'un objet
cible, l'analyse s'est arrêtée. Une extension du périmètre (visite terrain,
étude/dimensionnement, devis estimatif) a été demandée en complément par la
commande de mission ; elle est traitée en section 10bis, avec sa propre
discipline de preuve.

## 2. Corpus et méthode réellement utilisés

### 2.1 Instruments consultés avant lecture

`CLAUDE.md`, `functional-devis-3a-naissance.md` (intégral),
`functional-devis-3b-cycle.md` (intégral), `functional-propagation-pilot.md`
(intégral) lus avant toute sélection de source, conformément à la commande.
Les 8 corpus retenus par 3A/3B sont conservés à l'identique pour garantir la
comparabilité : Vertuoza, InterFast, Axonaut, Sellsy, OpenFire (Zendesk),
OpenFire (Odoo), Obat, Costructor. Séparation stricte OpenFire maintenue.

### 2.2 Méthode de sélection et d'exécution

Chaque éditeur a été confié à un agent d'extraction dédié, non exposé aux
rapports des autres, avec pour instruction : router en priorité sur les faits
déjà acquis en 3A/3B/pilote (cités nommément dans le brief de chaque agent
pour éviter toute redite), construire sa propre liste fermée de fichiers par
inspection directe de l'arborescence du corpus (le contenu `site_marketing/*`
étant explicitement écarté des preuves structurantes, utilisable seulement en
corroboration signalée), lire intégralement, citer exactement avec chemin, et
distinguer FAIT DOCUMENTÉ / INTERPRÉTATION / NON DÉTERMINÉ. Le rapprochement
inter-éditeurs qui suit est fait après coup, à partir des 8 rapports reçus
séparément, selon le protocole déjà utilisé par 3A, 3B et le pilote.

### 2.3 Couverture

| Éditeur | Fichiers exploités (ordre de grandeur) | Rendement |
|---|---:|---|
| Vertuoza | ~90 (dont ~55 FAQ ciblées) | Très riche — 4 lectures parallèles consolidées |
| InterFast | ~24 | Très riche |
| Axonaut | ~30 | Riche — comble un trou du pilote |
| Sellsy | ~24 | Riche — comble le trou principal du pilote |
| OpenFire (Zendesk) | 23 | Riche, avec une pièce structurante (Vital Études) |
| OpenFire (Odoo) | ~40 | Très riche, cascades comptables denses |
| Obat | ~44 | Très riche — corrige un acquis de 3A (chantier) |
| Costructor | ~38 | Très riche — corrige un acquis du pilote (devis→facture) |

Rendement global très supérieur aux seuils habituels de suffisance : les 8
corpus produisent des preuves croisées sur l'ensemble des relations
checklistées en section 3 de la commande, avec plusieurs corrections
documentaires précises apportées aux missions antérieures (voir §25).

### 2.4 Discipline de preuve

Identique à 3A/3B/pilote : FAIT DOCUMENTÉ (citation exacte + chemin) /
INTERPRÉTATION (marquée) / NON DÉTERMINÉ (silence documentaire ≠ absence
fonctionnelle). Aucune cause légale/comptable/technique n'a été inventée pour
un verrou non justifié dans la source. Le vocabulaire exact de chaque éditeur
est conservé (« commande », « bon de commande », « chantier », « intervention »
désignent des objets différents d'un éditeur à l'autre — cf. §3).

## 3. Carte des objets aval observés

| Objet aval | Éditeurs qui le documentent comme sortie du devis | Statut |
|---|---|---|
| Facture (finale/ordinaire) | InterFast, Obat, Costructor (directe) ; Sellsy (conversion manuelle) ; Axonaut, OpenFire×2 (via commande/bon de commande intermédiaire) ; Vertuoza (jamais directe — via chantier ou intervention) | STANDARD_FORT sur l'existence, VARIANTE_DE_MARCHE sur le chemin |
| Facture d'acompte | Les 8 corpus | STANDARD_FORT |
| Facture de situation/avancement | Vertuoza, InterFast, Sellsy, OpenFire (Odoo), Costructor, Obat | STANDARD_PROBABLE |
| Facture de solde | Vertuoza, InterFast, Sellsy, OpenFire (Odoo), Costructor | STANDARD_PROBABLE |
| Commande client | Axonaut (automatique), OpenFire×2 (même objet évolutif), Costructor (« convertir en ») | VARIANTE_DE_MARCHE |
| Commande/demande de prix fournisseur | Vertuoza, InterFast, OpenFire×2, Axonaut, Obat, Costructor | STANDARD_PROBABLE (mécanismes très différents) |
| Chantier/Projet/Affaire | Vertuoza, InterFast, Obat, Costructor | VARIANTE_DE_MARCHE (absent chez Axonaut/Sellsy, réattribué à l'opportunité chez OpenFire Odoo) |
| Intervention | Vertuoza, InterFast, Costructor (bidirectionnel), OpenFire×2 (sens inverse dominant) | VARIANTE_DE_MARCHE, avec inversion de sens chez plusieurs éditeurs |
| Planning/tâche | Vertuoza (chantier), InterFast (calendrier), Costructor (conversion typée) | SPÉCIFICITÉ_ÉDITEUR |
| Avoir/note de crédit | Les 8, mais toujours depuis la FACTURE, jamais directement du devis | Hors périmètre strict, mentionné pour continuité |
| Avenant | Vertuoza, InterFast, Costructor | Déjà acquis en 3B, réutilisé ici pour son effet aval (facturation, rentabilité) |
| Objet émergent : parc installé / équipement | OpenFire (Odoo) | SPÉCIFICITÉ_ÉDITEUR |
| Objet émergent : bordereau de chantier | Obat, Costructor | SPÉCIFICITÉ_ÉDITEUR |
| Objet émergent : décompte général (DGD) | InterFast, Obat, Costructor | STANDARD_PROBABLE (BTP uniquement) |
| Objet émergent : PV de réception | InterFast, Obat, Costructor | Naît du CHANTIER, pas du devis — mentionné pour mémoire |

## 4. Matrice des relations de sortie

Sélection des relations les plus structurantes ; le détail complet par
éditeur est repris section par section (§5-10).

| OBJET SOURCE | ACTION/ÉVÉNEMENT | CONDITION | OBJET CIBLE | EFFET OBSERVABLE | ÉTAT/RÉSULTAT | ÉDITEUR |
|---|---|---|---|---|---|---|
| Devis | Signature/acceptation | — | Facture directe | Création, lignes copiées | Devis → Facturé | InterFast, Obat, Costructor |
| Devis | « Convertir en facture » | — | Facture | Création manuelle, infos reprises | Devis conservé, → Facturé | Sellsy |
| Devis | Acceptation | — | Commande client (auto) | Création automatique | Devis → verrouillé indirectement (via commande) | Axonaut |
| Devis (≈bon de commande) | « Confirmer la vente »/évolution de statut | — | Bon de commande | TRANSFORMATION du même objet | Devis = bon de commande | OpenFire (Zendesk), OpenFire (Odoo) |
| Devis | « Transformer en chantier »/acceptation | — | Chantier | Création, heures/données copiées | Devis → « Chantier en cours »/lié | Vertuoza, InterFast, Obat, Costructor |
| Devis (Vertuoza) | Signature | — | Chantier OU Intervention | Bifurcation, critère de choix NON DÉTERMINÉ | Devis engagé | Vertuoza |
| Devis Accepté | « Planifier une intervention » | devis Accepté | Intervention | Création, client/adresse copiés, liaison bidirectionnelle | — | InterFast |
| Intervention (DI/rapport) | Génération | — | Devis | CRÉATION (sens inverse du flux attendu) | — | OpenFire (Zendesk via Vital Études), OpenFire (Odoo), InterFast (visite avant devis) |
| Devis finalisé | « Convertir en » | — | Bon de commande fournisseur / demande de prix | Lignes sélectionnées copiées | — | Vertuoza, InterFast, OpenFire×2, Axonaut, Obat, Costructor |

## 5. Devis → Facture

**Résultat le plus structurant de toute la mission** : contrairement à
l'hypothèse initiale d'un trou documentaire général (pilote propagation), la
lecture primaire montre que le marché se scinde en **deux familles nettes** :

**Famille A — transformation directe devis→facture documentée** :
- **InterFast** : condition = devis **Accepté** ; « Si votre devis est marqué
  comme "Facturé", le logiciel considère que tout a été payé et bloque la
  création de nouvelles factures » ; un devis ne peut être lié qu'à **une
  seule** facture en brouillon à la fois ; lignes COPIÉES, montant RECALCULÉ
  (déduction des acomptes/avenants Acceptés) ; passage automatique
  Accepté→Facturé une fois intégralement facturé, avec un forçage manuel
  récent possible sans effet comptable.
- **Obat** : condition = devis **signé** (« Pour facturer un devis, celui-ci
  doit être signé. Vous ne pourrez alors plus le modifier ni le supprimer »),
  bouton « Signer et Facturer » si non signé ; lignes COPIÉES puis
  surchargeables ; **blocage mutuel** : impossible de créer une facture finale
  si une facture de situation a déjà été émise sur ce devis (et vice-versa).
- **Costructor** : condition = devis **finalisé** (facture ordinaire/de
  situation) ou **finalisé + accepté** (acompte/situation, selon deux articles
  distincts sans justification de l'écart) ; bouton « Facturer » sur le devis
  lui-même, choix entre facture de situation et facture finale — ce point
  **infirme** le trou identifié par le pilote propagation sur ce couple.
- **Sellsy** : TRANSFORMATION/LIAISON manuelle unique via « Convertir en
  facture » depuis le devis parent : « il n'est pas possible de lier deux
  documents de vente après leur création » ; données (client, produits,
  montants, taxes) COPIÉES ; multiplicité en cascade explicitement documentée
  (« à partir d'un devis, générer plusieurs bons de livraison, puis plusieurs
  factures ») ; arbitrage manuel de statut si le total facturé diffère du
  montant du devis — ce point **comble** le trou principal identifié par le
  pilote propagation.

**Famille B — objet pivot obligatoire entre devis et facture** :
- **Axonaut** : « Cette validation génère automatiquement une commande
  correspondante dans Axonaut » ; c'est ensuite depuis la commande (jamais
  directement depuis le devis) que la facture est créée (« Émettre une
  facture » / « Faire la facture »), les informations étant COPIÉES. Seule
  exception apparente : le paiement en ligne du devis génère une facture sans
  étape « Faire la facture » visible, mécanisme exact NON DÉTERMINÉ.
- **OpenFire (Zendesk et Odoo)** : devis, estimation et bon de commande sont
  « un seul et même document dont l'état évolue » (fait déjà acquis en 3B) ;
  c'est la **commande facturable** (condition : validée + quantité en attente
  de facturation) qui produit la facture, lignes COPIÉES sans la ligne
  d'acompte.
- **Vertuoza** : **aucune transformation directe devis→facture** n'est
  documentée. La « facture simple » est définie **positivement** par son
  indépendance du devis (« établie directement depuis l'édition de facture et
  donc en partant de 0 »). Les deux seules voies de facturation liées au
  devis passent par le **chantier** (factures d'avancement/finale, RECALCULÉ)
  ou par l'**intervention** (rapport validé → « Transformer en facture »). Le
  devis signé bifurque explicitement vers « chantier **ou** intervention »
  (`devis/signature-electronique-du-devis.md`), critère de choix NON
  DÉTERMINÉ. C'est un **fait documenté de séparation de régime**, pas un
  simple silence.

**Lecture de synthèse** : la relation devis→facture existe universellement en
tant que capacité fonctionnelle (8/8), mais son architecture varie
fortement : transformation directe (3/8 nets, Sellsy en 4ᵉ), passage par un
objet pivot commande/bon de commande (3/8), passage exclusif par un chantier
ou une intervention (Vertuoza). C'est une **VARIANTE_DE_MARCHE structurante**,
pas un standard de mécanisme, même si l'existence de la capacité elle-même est
un STANDARD_FORT.

## 6. Devis → Acompte / situation / solde

Motif le plus convergent de toute la mission après le mécanisme de création
de client à la volée (3A) : les 8 corpus documentent un acompte défini au
niveau du devis (paramètre en %, montant HT ou TTC), une facture d'acompte
distincte, et une **déduction automatique (RECALCULÉ)** de cet acompte lors de
la facturation finale.

- **Paramètre d'acompte sur le devis** : InterFast, Costructor, Obat, OpenFire
  (Zendesk, produit dédié configuré) le documentent explicitement comme un
  champ du devis repris automatiquement à la facturation. Vertuoza documente
  seulement un texte libre en « conditions particulières », sans preuve que ce
  texte alimente structurellement une future facture d'acompte (NON
  DÉTERMINÉ).
- **Condition d'antériorité** : OpenFire (Zendesk) — « Les factures d'acompte
  ne peuvent être créées automatiquement que depuis un bon de commande client »
  (jamais directement depuis un devis non confirmé, ni depuis une
  intervention) ; Sellsy — « la création d'une facture d'acompte nécessite de
  créer un devis ou un bon de commande en amont ».
- **Déduction différenciée selon le statut de paiement** (Obat, précision
  nouvelle par rapport au pilote) : acompte **non payé** → déduction
  **manuelle** puis passage manuel du statut ; acompte **payé** → déduction
  **automatique**. Le déclencheur du recalcul automatique est donc le statut
  de la facture d'acompte, pas l'encaissement réel documenté indépendamment.
- **Acompte « libre »** (Obat) : permet un montant différent du % paramétré,
  sans modifier le devis lui-même.
- **Situation/avancement** : cascade RECALCULÉE documentée par Vertuoza,
  InterFast, Sellsy, OpenFire (Odoo), Costructor, Obat — le montant déjà
  facturé (acompte + situations antérieures) est systématiquement déduit,
  jamais ressaisi, du document suivant. OpenFire (Odoo) documente la version
  la plus poussée : « une facture de solde qui reprendra toutes les lignes de
  la commande avec la déduction des lignes de factures de situation. Cette
  facture de solde sera ainsi toujours à 0 € ».
- **Retenue de garantie** : propagée automatiquement sur factures
  d'acompte/situation/solde chez OpenFire (Odoo, Zendesk) et Costructor.
  Chez Vertuoza, une **anomalie structurelle** est confirmée par recoupement
  indépendant (produit + 2 FAQ) : la retenue ajoutée via le bouton natif du
  devis n'est PAS héritée dans le chantier, contournement officiel documenté
  (ligne poste libre à montant négatif) — cas rare de fonctionnalité
  affichée comme intégrée mais qui ne se propage pas comme son intitulé le
  suggère (critère CP structurel).
- **Exclusions croisées** : Sellsy interdit la combinaison acompte + factures
  partielles multiples sur un même devis ; Obat interdit la facture finale
  une fois une cascade de situations engagée (et réciproquement) ; Costructor
  interdit la facture de situation sur un devis incluant des primes
  énergétiques.

## 7. Devis → Commande

**Commande client** — trois modèles distincts, aucun ne domine :
1. **Création automatique** à l'acceptation (Axonaut) : la commande devient
   le **conteneur pivot unique** de toute sortie aval (facture classique,
   acompte, situation, proforma, bon de livraison, commande fournisseur) —
   « une commande est un dossier où vous allez pouvoir ranger les différents
   éléments d'une affaire ».
2. **Transformation de statut du même objet** (OpenFire Zendesk et Odoo) :
   devis, estimation, bon de commande ne sont pas trois objets mais trois
   états d'un seul document.
3. **Transformation manuelle optionnelle et parallèle** (Costructor,
   « convertir en » vers un bon de commande client, sans lien documenté vers
   la facturation) ; **absence de commande client** chez Vertuoza (le mot
   « commande » y désigne le devis signé lui-même) et chez Obat (seuls des
   bons de commande **fournisseur** existent depuis le devis).
4. Sellsy documente un régime à part : le bon de commande n'est pas un aval
   du devis mais un **parent alternatif équivalent** — les deux sont traités
   comme deux points d'entrée interchangeables vers les mêmes mécanismes
   aval, sauf via la fusion (N devis → 1 bon de commande).

**Commande/demande de prix fournisseur** — présente chez 7/8 éditeurs (absent
chez Sellsy, généraliste facturation), avec des architectures très
hétérogènes : liaison ligne-à-ligne optionnelle (Vertuoza, InterFast V1) ;
génération automatique avec copie des lignes/références (InterFast V2 —
fusion des doublons avec conservation du détail d'origine dans le devis) ;
chaîne à 6 étapes devis→bon de livraison→demande de prix→commande fournisseur
(OpenFire Zendesk, « contremarque »various dont un mode où la demande de prix
est immédiate à la confirmation) ; deux voies parallèles non hiérarchisées,
via le bon de livraison ou directement depuis un article de type Service
(OpenFire Odoo) ; commande fournisseur créée **dans** la commande client, sans
lien direct devis→fournisseur (Axonaut) ; sans prix, filtrée par fournisseur
(Obat) ; sélection à la carte des lignes du devis (Costructor).

## 8. Devis → Chantier / Projet / Affaire

**VARIANTE_DE_MARCHE confirmée, avec une correction significative à 3A** :
Obat, classé « NON DÉTERMINÉ » sur ce point en 3A par silence documentaire,
possède en réalité un concept de chantier riche et central : création/liaison
à la volée depuis le devis, décompte général consolidant tous les documents
liés (devis, factures d'acompte/situation/finale, avoirs), rentabilité
calculée au niveau chantier, effet automatique de fin de chantier au seuil de
100% de facturation. **3A doit être considéré comme partiellement corrigé sur
ce point** (silence documentaire d'alors ≠ absence confirmée aujourd'hui).

- **Vertuoza** : transformation directe et nommée (« Chantier en cours »),
  hub de recalcul de rentabilité (dépenses + ventes), effet automatique
  d'ajout au planning dès l'acceptation, asymétrie non expliquée entre
  données figées (coordonnées de facturation, SNAPSHOTTÉ) et données
  propagées rétroactivement (nom du chantier, RÉFÉRENCÉ).
- **InterFast** : action « Transformer en chantier » (icône dédiée), heures
  prévues COPIÉES du devis, liste d'articles optionnelle sans les prix pour
  les techniciens, multiplicité confirmée (plusieurs devis de travaux
  supplémentaires liés à un même chantier), irréversibilité du client associé
  au chantier une fois créé.
- **Costructor** : rentabilité prévue « calculée à partir du (des) devis
  lié(s) au chantier » (RECALCULÉ, pluriel explicite), chantier rattachable
  depuis l'édition d'un devis.
- **Axonaut et Sellsy** : absence confirmée activement (pas un simple
  silence) — aucun objet chantier/projet distinct dans la documentation
  support, malgré une allégation marketing isolée et non recoupée chez
  Axonaut (« bon de commande […] peut être associé à un projet »), à traiter
  comme FAIBLEMENT_DOCUMENTÉ et non comme fait acquis.
- **OpenFire (Odoo)** : le « Projet » est un système d'attributs rattaché à
  l'**opportunité**, en amont du devis — PAS une sortie du devis. Le contrat
  de maintenance n'est documenté nulle part comme naissant d'un devis
  signé — silence assumé, pas comblé par extrapolation.

## 9. Devis → Intervention / Planning

**Constat structurant non anticipé par la commande de mission** : dans
plusieurs corpus (OpenFire Zendesk et Odoo, et partiellement InterFast), le
sens **dominant documenté est intervention/demande d'intervention → devis**,
pas l'inverse attendu par l'hypothèse implicite de la mission.

- **Vertuoza** : devis signé peut bifurquer vers une intervention (alternative
  au chantier, critère NON DÉTERMINÉ) ; rapport d'intervention « sur base
  d'un devis » reprend ligne à ligne les postes du devis, activation
  manuelle « facturable » par ligne, puis transformation en facture.
- **InterFast** : action « Planifier une intervention » depuis un devis
  **Accepté** (option indisponible sinon), client/adresse COPIÉS, liaison
  bidirectionnelle (numéro/adresse affichés dans les deux sens) ; un devis
  peut être lié à **plusieurs** interventions ; restriction : lier un devis
  à une intervention déjà existante n'est possible que pour du SAV/maintenance.
- **OpenFire (Zendesk)** : le mécanisme le plus riche et le plus contraire à
  l'hypothèse initiale — « Vital Études », un outil de dimensionnement
  terrain (mobile, formulaire structuré), **génère automatiquement un devis**
  avec les produits adaptés (voir §10bis). Le seul effet aval devis→planning
  documenté est inversé : le champ « Date de pose de référence » de la
  commande est **calculé** à partir des interventions réalisées qui lui sont
  rattachées.
- **OpenFire (Odoo)** : cascade Contrat→Ligne de contrat→DI→RDV déjà connue
  (pilote), mais confirmée comme sens majoritairement descendant depuis le
  contrat, pas depuis le devis ; le seul lien devis→RDV documenté est une
  saisie manuelle de référence, jamais une création automatique.
- **Axonaut, Sellsy** : absence confirmée (le module RDV d'Axonaut est un
  outil de prospection commerciale générique, sans lien avec le devis).
- **Obat** : module Intervention existant mais en développement (« Lot 1 »),
  aucun lien devis↔intervention documenté à ce stade.
- **Costructor** : seul éditeur documentant une **boucle bidirectionnelle**
  franche — devis → bon d'intervention (« convertir en »), et intervention
  **terminée** → devis (sens inverse, « convertir en » également). Devis →
  Planning de chantier documenté séparément : conversion typée (seuls les
  éléments de main d'œuvre), calage manuel obligatoire des dates/affectations.

## 10. Autres sorties observées

- **Fusion multi-devis → document unique** (Sellsy) : sens inverse de la
  cascade attendue (N devis → 1 facture ou 1 bon de commande), avec
  conditions bloquantes propres (devise, client, catégorie tarifaire
  identiques, devis sans acompte).
- **Duplication devis/facture** (Obat) : contourne l'impossibilité de
  modifier une facture envoyée, sans lien de traçabilité documenté vers
  l'original.
- **Parc installé / équipement** (OpenFire Odoo) : créable depuis un devis ou
  une facture, avec reprise partielle automatique (client, revendeur, date de
  vente).
- **Bordereau de chantier** (Obat, Costructor) : document PDF généré depuis
  un devis ou une facture existants, TRANSFORMATION d'affichage seulement, pas
  une nouvelle entité comptable.
- **Décompte général définitif (DGD)** (InterFast, Obat, Costructor) : agrège
  devis + factures + avoirs d'un chantier, obligatoire en marché public.
- **Facture proforma** (Axonaut, OpenFire Zendesk, Costructor, Obat) : document
  sans valeur comptable généré depuis le devis/la commande, transformable
  ultérieurement.
- **Décrément automatique de stock** au passage du devis en « Accepté »
  (InterFast, confirmé), à la facturation (Axonaut), ou au bon de livraison
  généré depuis le devis confirmé (OpenFire Zendesk).
- **Connecteur multi-entités** (Sellsy) : duplication du devis accepté vers
  un compte « enfant » distinct, synchronisation unidirectionnelle, verrou de
  synchronisation si le devis est modifié après le passage en « Accepté ».

## 10bis. Cas structurant : du chiffrage initial à l'offre techniquement validée

Question complémentaire de la commande, hypothèse produit SUPORDO
(DEMANDE → PROPOSITION/DEVIS ESTIMATIF → VISITE TECHNIQUE → ÉTUDE/CALCUL →
DEVIS DÉFINITIF → DOCUMENTS TECHNIQUES → ENGAGEMENT), à ne jamais imposer au
corpus.

### A/B/C/D/E — par éditeur

- **Vertuoza** : recherche exhaustive par mots-clés sans résultat pertinent
  (hors faux positifs). Seule brique adjacente : import d'un métré/bordereau
  de prix **produit hors Vertuoza** (par un architecte) directement comme
  source de lignes de devis — pas un outil de relevé terrain interne.
  Classification : **NON_DETERMINE** (silence quasi total).
- **InterFast** : chaîne la plus complète du corpus. Objet dédié « Visite
  avant devis » (intervention typée, rapport structuré mobile — métrés,
  photos annotées, croquis), explicitement définie pour la phase de
  découverte (« vous n'êtes pas encore prêt à chiffrer »). Un bouton unique
  génère ensuite un **brouillon de devis lié** au client et à l'intervention.
  MAIS : aucun devis estimatif distinct du devis définitif ; aucun transfert
  automatique documenté des métrés vers les lignes du devis (ajout manuel via
  la bibliothèque) ; aucun objet « étude/calcul/dimensionnement » séparé ;
  documents techniques joints au devis de façon manuelle et optionnelle.
  Classification : **BRIQUES_DOCUMENTEES_MAIS_CONTINUITE_NON_ETABLIE**, la
  plus proche de CONTINUITE_DOCUMENTEE de tout le panel sur les 3 premières
  étapes (Demande, Visite, Devis), mais sans étude ni devis estimatif.
- **Axonaut** : quasi absent, confirmé plutôt que présupposé — seul un champ
  de date libre existe sur le devis (« vous souhaitez indiquer quand vous
  êtes allé chez un client »), sans statut ni document rattaché.
  Classification : **FAIBLEMENT_DOCUMENTE**.
- **Sellsy** : absent, confirmé — aucune mention fonctionnelle au-delà de
  pages marketing verticales non probantes. Classification : **NON_DETERMINE**.
- **OpenFire (Zendesk)** : preuve la plus forte du corpus. **Vital Études**
  (mobile, rattaché obligatoirement à une intervention de modèle
  « Dimensionnement Vitalome ») : formulaire structuré (principe de réseau,
  éléments) → « Votre devis est automatiquement généré avec les produits
  Vitalome adaptés » (CRÉATION automatique de lignes, pas un simple stockage
  de résultat) → sorties documentaires distinctes (dossier Vitalome pour le
  client, rapport d'intervention technique avec schéma et tableau de
  dimensionnement). Aucune dépendance bloquante documentée sur l'envoi/la
  signature. Par contraste, le **calculateur de déperdition de chaleur** du
  même corpus reste une **LIAISON manuelle** de consultation croisée,
  jamais générative de lignes, explicitement positionné comme non
  substituable à une étude réglementaire. Classification : **CONTINUITE_
  DOCUMENTEE** (partielle, verticale ventilation/ITE) coexistant avec
  **BRIQUES_DOCUMENTEES_MAIS_CONTINUITE_NON_ETABLIE** pour le calcul de
  déperdition.
- **OpenFire (Odoo)** : un second calculateur de déperdition de chaleur
  existe (formule NF EN 12831 citée), avec un champ de liaison optionnel vers
  une opportunité/un devis/un parc installé, mais le contenu exact transporté
  par cette liaison (report de données, insertion de ligne) est NON
  DÉTERMINÉ — aucune dépendance bloquante. Classification :
  **BRIQUES_DOCUMENTEES_MAIS_CONTINUITE_NON_ETABLIE**.
- **Obat** : convergence récente vers « le terrain alimente le devis », mais
  non aboutie. Champ « date de visite préalable » (métadonnée seule). Module
  **Métrés** (« bientôt disponible ») : consultable en lecture seule depuis
  le générateur de devis dès la v1.1 — alimentation prévue mais non encore
  documentée en détail. **Notes de chantier** intégrées à l'éditeur de devis,
  mais rattachées au chantier, pas au devis, et conditionnées à l'existence
  d'un chantier associé. Assistant vocal = accélérateur de saisie de la
  proposition, pas un outil de relevé terrain. Classification :
  **BRIQUES_DOCUMENTEES_MAIS_CONTINUITE_NON_ETABLIE**.
- **Costructor** : recherche ciblée sans résultat — devis IA et imports
  DPGF/DQE/PDF déjà connus (3A) sont des accélérateurs de création, pas des
  mécanismes de continuité terrain→étude→devis. Documents techniques joints
  = pièces jointes génériques non typées. Classification : **NON_DETERMINE**.

### F/G — synthèse transverse

1. **Le corpus documente-t-il une continuité PROPOSITION → TERRAIN → ÉTUDE →
   OFFRE DÉFINITIVE ?** Non comme séquence formalisée à 7 étapes chez aucun
   éditeur. Une continuité **partielle et vérifiée** existe chez InterFast
   (Demande → Visite → Devis, sans étude ni devis estimatif distinct) et chez
   OpenFire Zendesk pour un vertical précis (dimensionnement ventilation via
   Vital Études, avec génération automatique de lignes de devis).
2. **Chez quels éditeurs et sous quelles formes ?** InterFast (visite
   structurée mobile → devis lié) et OpenFire Zendesk (étude → devis généré
   automatiquement) sont les deux cas les mieux sourcés ; Obat montre une
   convergence produit récente mais non aboutie (Métrés, Notes de chantier).
   Vertuoza, Axonaut, Sellsy, Costructor et OpenFire Odoo ne documentent que
   des briques disjointes ou rien.
3. **Distinction devis simplement modifié / véritable validation technique
   intermédiaire / nouvel objet-version ?** Le corpus permet de distinguer
   ces trois cas : Vital Études (OpenFire Zendesk) illustre une **validation
   technique intermédiaire réelle** générant le devis ; les variantes (Obat,
   InterFast, déjà acquises en 3B) illustrent des **objets-versions
   parallèles**, pas une précision croissante estimative→définitive ; la
   majorité des éditeurs (InterFast compris) ne documentent qu'un **devis
   unique simplement modifié** après la visite terrain.
4. **Documents techniques réellement intégrés ?** Le rapport d'intervention
   PDF (InterFast, Vertuoza) et le rapport Vitalome avec schéma/tableau de
   dimensionnement (OpenFire Zendesk) sont les seuls documents techniques
   structurés et rattachés explicitement à l'objet devis/intervention.
   Ailleurs, il s'agit de pièces jointes génériques et manuelles.
5. **Absence de continuité documentée ≠ absence fonctionnelle** : ce
   principe a été respecté strictement — chaque classification NON_DETERMINE
   ou FAIBLEMENT_DOCUMENTE est un constat de silence, jamais une conclusion
   sur ce que fait réellement le concurrent en pratique.

## 11. Propagation des données

| SOURCE | CIBLE | DONNÉE | COMPORTEMENT OBSERVÉ | PREUVE (éditeur) |
|---|---|---|---|---|
| Devis | Facture | Client, produits, montants, taxes | COPIÉ | Sellsy, Axonaut, InterFast, Obat |
| Devis | Facture | Lignes | COPIÉ puis surchargeable | InterFast, Obat, Costructor |
| Devis | Facture d'acompte | Montant/pourcentage | RECALCULÉ (jamais les lignes) | Sellsy, InterFast, OpenFire×2, Obat |
| Facture(s) d'acompte/situation | Facture de solde | Montant déjà facturé | RECALCULÉ, déduit automatiquement | 6/8 éditeurs (voir §6) |
| Devis Accepté | Chantier | Heures prévues | COPIÉ | InterFast |
| Devis | Chantier | Coordonnées de facturation | SNAPSHOTTÉ (non rétroactif) | Vertuoza |
| Devis→Chantier | Chantier | Nom du chantier | RÉFÉRENCÉ (propagé rétroactivement à tous les documents) | Vertuoza |
| Devis Accepté | Commande fournisseur | Articles, références, quantités | COPIÉ, fusion des doublons (détail conservé dans le devis) | InterFast |
| Devis finalisé | Bon de commande fournisseur | Fournisseur + lignes sélectionnées | COPIÉ à la carte | Costructor |
| Bibliothèque/catalogue | Devis/Facture | Prix | SNAPSHOTTÉ à la création, ré-snapshotté si réimport explicite | Obat (déjà acquis pilote, reconfirmé) |
| Devis (retenue de garantie) | Factures issues | % de RG | REPORTÉ automatiquement | Costructor, OpenFire×2 |
| Devis (retenue de garantie, bouton natif) | Chantier | % de RG | NON PROPAGÉ (anomalie confirmée) | Vertuoza |
| Rapport d'intervention/DI | Devis | Données de dimensionnement, produits | COPIÉ (génération automatique de lignes) | OpenFire (Zendesk, Vital Études) |
| Intervention | Devis | Client, adresse | COPIÉ/RÉFÉRENCÉ | InterFast |

**Rappel de discipline** : le mode technique exact (copie en base vs
référence vivante) reste NON DÉTERMINÉ pour la grande majorité des
propagations — les éditeurs documentent un comportement visible
(« reprises », « automatiquement »), rarement le mécanisme backend. Seules
les exceptions listées ci-dessus (SNAPSHOTTÉ, RÉFÉRENCÉ) sont tranchées
explicitement par une source primaire.

## 12. Continuité entre objets

- **Le devis original reste-t-il visible après transformation ?** Oui,
  systématiquement quand la relation est documentée (Sellsy : « conservé et
  consultable » ; Vertuoza, InterFast, Obat, Costructor : le devis reste
  accessible depuis le chantier/la fiche facture).
- **Le nouvel objet référence-t-il le devis ?** Oui dans la quasi-totalité
  des cas documentés (champ « Chantier »/« Document d'origine »/« Devis
  d'origine » verrouillé sur la facture chez Vertuoza, OpenFire Odoo,
  InterFast).
- **Navigation bidirectionnelle ?** Documentée explicitement chez InterFast
  (devis↔intervention, numéro et adresse affichés dans les deux sens) et
  Costructor (devis↔intervention, boucle de conversion dans les deux sens).
- **Le devis change-t-il d'état après la sortie ?** Oui, quasi universellement
  quand documenté : passage vers un statut « Facturé »/« Chantier en
  cours »/verrouillage indirect (via la commande, Axonaut).
- **Plusieurs objets cibles depuis un même devis ?** Oui, très largement
  démontré (§16 Multiplicité).
- **L'objet cible peut-il exister sans le devis ?** Oui pour la facture
  (« facture simple » chez Vertuoza, facture manuelle chez OpenFire, facture
  directe chez Axonaut/Costructor) — c'est une voie parallèle documentée
  positivement, pas un silence.
- **Une modification du devis après création de la cible affecte-t-elle la
  cible ?** NON DÉTERMINÉ dans la majorité des corpus (silence quasi total) ;
  exception documentée chez Costructor : modifier un devis signé invalide sa
  signature (fait acquis 3B) mais aucun article ne dit si un bon de
  commande/une intervention déjà créés en sont affectés.

## 13. Effets secondaires

| ÉVÉNEMENT DEVIS | EFFET SECONDAIRE | AUTOMATIQUE/MANUEL | CONDITION | ÉDITEUR |
|---|---|---|---|---|
| Acceptation | Transformation en chantier ou intervention | Automatique (déclenchement), bifurcation NON DÉTERMINÉE | — | Vertuoza |
| Acceptation | Ajout automatique au planning | Automatique, réversible manuellement | — | Vertuoza |
| Acceptation | Création automatique d'une commande client | Automatique | — | Axonaut |
| Passage « Accepté » | Décrément automatique de stock | Automatique | produits associés au devis | InterFast |
| Confirmation (produits stockables) | Génération automatique d'un bon de livraison | Automatique | — | OpenFire (Zendesk) |
| Génération facture d'acompte | Ligne « Acompte »/« Retenue de garantie » non modifiable ajoutée à la commande d'origine | Automatique | — | OpenFire (Odoo), OpenFire (Zendesk) |
| Marquer l'opportunité liée « perdue » | Annulation automatique en cascade du devis | Automatique | opportunité liée | OpenFire (Odoo) |
| Facturation intégrale | Passage automatique du devis en « Facturé » | Automatique | — | InterFast |
| Signature électronique | Notification email au seul utilisateur nommé sur le devis | Automatique | — | Axonaut (déjà acquis 3B, reconfirmé) |
| Chantier atteint 100% de facturation | Modale de fin de chantier (avis client, photos, e-réputation) | Automatique | option activée | Obat |
| Devis Vitalome complété et enregistré | Génération de lignes de devis + rapport technique PDF | Automatique | modèle d'intervention dédié | OpenFire (Zendesk) |
| Validation d'une feuille d'heures | Remontée automatique sur la rentabilité du chantier + verrouillage de la feuille | Automatique | rattachement au chantier | Costructor |

## 14. Erreurs / blocages / recovery

| OPÉRATION | BLOCAGE/ERREUR | CAUSE DOCUMENTÉE | CONSÉQUENCE | RECOVERY DOCUMENTÉ | ÉDITEUR |
|---|---|---|---|---|---|
| Facturer un devis | Devis non finalisé/accepté/signé | Condition métier de statut | Facturation impossible | Finaliser/faire accepter/signer le devis | InterFast, Obat, Costructor |
| Créer une nouvelle facture | Une facture en brouillon existe déjà sur ce devis | Contrainte de multiplicité (1 seule) | Blocage | Finaliser ou supprimer le brouillon existant | InterFast |
| Facture finale après cascade de situations engagée | Incompatibilité de régime | Règle produit | Blocage définitif de ce chemin | Poursuivre uniquement par situations jusqu'à 100% | Obat |
| Facture d'avancement puis facture prévisionnelle sur la même commande | Incompatibilité croisée | Règle produit | Blocage | Aucun contournement documenté | Axonaut |
| Transformer devis→facture | Droit « édition de facture » manquant | Permission | Blocage | Contacter l'administrateur | Axonaut |
| Supprimer une commande | Documents associés existants | Règle produit (intégrité) | Blocage | Supprimer les documents d'abord, ou clôturer manuellement | Axonaut, Vertuoza (analogue commandes fournisseur) |
| Modifier le client d'un chantier existant | Champ verrouillé | Règle produit | Blocage définitif | Archiver le chantier erroné, en créer un nouveau | InterFast |
| Facture électronique déjà transmise | Renvoi refusé | Contrainte technique de la plateforme | Erreur affichée | Vérifier le statut avant tout renvoi | Obat, Vertuoza (achats reçus, non supprimables) |
| Suppression d'éléments chiffrés sur une facture de situation | Impossible | Règle produit (continuité d'avancement) | Blocage | Facturer la ligne à 100% puis émettre un avoir | Obat |
| Avoir sur facture d'acompte alors que le solde existe déjà | Impossible techniquement | Séquence de dépendance | Blocage | Annuler d'abord la facture de solde | InterFast |
| Annulation d'une facture finalisée | Modification/suppression directe interdite | Cause réglementaire (anti-fraude TVA) | Correction obligatoire par avoir | Avoir + nouvelle facture | 6/8 éditeurs (déjà acquis pilote, reconfirmé) |
| Avenant non intégré à un état d'avancement déjà créé | Pas de rattrapage rétroactif | Règle produit | Avenant absent de la facturation en cours | Aucun — nouvel avancement futur seulement | Vertuoza |
| Écart de montant devis vs total facturé | Statut ambigu à l'enregistrement | Règle produit (notion de solde) | Arbitrage manuel requis | Choix manuel du statut à appliquer | Sellsy |
| Fiche client incomplète (facturation électronique) | Blocage d'envoi | Contrainte réglementaire (Peppol/normes) | Erreur d'envoi | Corriger SIREN/SIRET/TVA/adresse | Obat |

## 15. Réversibilité

| Sortie | Statut | Éditeur(s) |
|---|---|---|
| Devis → Chantier, sans document généré | RÉVERSIBLE — suppression du chantier réouvre le devis, même objet | Vertuoza, Axonaut (via commande) |
| Devis → Chantier, avec documents générés | IRRÉVERSIBLE_DOCUMENTÉ tant que les documents existent | Vertuoza |
| Devis → Commande (Axonaut), sans documents | RÉVERSIBLE — suppression remet le devis « en attente » | Axonaut |
| Facture finalisée/numérotée | IRRÉVERSIBLE_DOCUMENTÉ — correction uniquement par avoir | Quasi tous les éditeurs (cause réglementaire) |
| Facture brouillon | RÉVERSIBLE | Tous les éditeurs qui documentent le statut |
| Annulation de signature (variante) | RÉVERSIBLE — retour au statut antérieur, pastilles réapparaissent | Obat (déjà acquis 3B) |
| Variante signée ayant déjà généré une facture | NON DÉTERMINÉ — silence total sur l'effet d'une annulation de signature sur une facture déjà émise | Obat |
| Devis modifié après signature (invalide la signature) | PARTIELLEMENT_RÉVERSIBLE — re-signature obligatoire, pas de blocage technique | Costructor (déjà acquis 3B) |
| Intervention → Devis (boucle) | RÉVERSIBLE dans le sens inverse, une fois l'intervention terminée | Costructor |
| Réservation de stock (devis/BC) | RÉVERSIBLE jusqu'à confirmation par un bon de livraison/une facture | Sellsy |
| Suppression d'un avenant déjà intégré à un document ultérieur | PARTIELLEMENT_RÉVERSIBLE — nécessite suppression cascade des documents postérieurs | Vertuoza |
| Duplication d'une facture/d'un devis (contournement) | Crée un nouvel objet sans lien de traçabilité documenté vers l'original | Obat |

## 16. Multiplicité

Comportement observé (jamais déduit d'une cardinalité backend) :

- **1 devis → plusieurs factures de situation successives**, jusqu'à 100% :
  Vertuoza, InterFast, Sellsy, OpenFire (Odoo), Obat, Costructor.
- **1 devis/bon de commande → plusieurs factures d'acompte** (jusqu'à 100%
  du montant), **puis 1 seule facture de solde** : Sellsy, OpenFire (Odoo).
- **1 commande (Axonaut) → N factures** (classique, acompte, solde, situation,
  proforma, prévisionnelle).
- **1 devis → N bons de commande, chacun avec son propre cycle
  d'avancement** : Sellsy — structure arborescente non anticipée par la
  hiérarchie linéaire habituelle.
- **N devis → 1 document fusionné** (facture ou bon de commande) : Sellsy —
  sens inverse de la cascade attendue.
- **1 chantier → plusieurs devis liés** (travaux supplémentaires) : InterFast,
  Costructor, Obat (implicite via décompte général).
- **1 devis → plusieurs commandes fournisseur/demandes de prix**, une par
  fournisseur : OpenFire (Zendesk, « Approvisionner » génère une demande par
  fournisseur), Axonaut (« passer commande auprès de vos fournisseurs […] à
  partir des éléments d'un devis », sans limite énoncée).
- **1 devis → plusieurs interventions liées** (SAV) : InterFast.
- **États d'avancement strictement séquentiels**, un seul « en cours » à la
  fois : Vertuoza.
- NON DÉTERMINÉ pour plusieurs couples (devis→commandes fournisseur multiples
  chez InterFast/Costructor ; devis→bons de commande client multiples chez
  Costructor) — silence, pas absence.

## 17. Comparaison inter-éditeurs

**Phénomène 1 — Devis→Facture : existence universelle, architecture
divergente.** STANDARD_FORT sur la capacité (8/8) ; VARIANTE_DE_MARCHE nette
sur le mécanisme : transformation directe (InterFast, Obat, Costructor,
Sellsy via conversion manuelle) vs objet pivot obligatoire commande/bon de
commande (Axonaut, OpenFire×2) vs passage exclusif par un chantier ou une
intervention (Vertuoza, cas le plus radical du panel).

**Phénomène 2 — Acompte→déduction automatique sur le solde.**
STANDARD_PROBABLE fort, désormais documenté par 6-7 éditeurs sur 8 (Vertuoza,
InterFast, Sellsy, OpenFire×2, Obat, Costructor), le RECALCULÉ étant la
formulation dominante et jamais contredite.

**Phénomène 3 — Chantier/Projet : clivage BTP spécialiste vs généraliste.**
Vertuoza, InterFast, Obat, Costructor documentent un objet chantier riche et
central ; Axonaut et Sellsy en sont dépourvus (confirmé activement) ; OpenFire
(Odoo) réattribue la notion de « Projet » à l'opportunité, en amont du devis.

**Phénomène 4 — Sens de la relation devis↔intervention, inversé chez
plusieurs éditeurs.** Contrairement à l'hypothèse implicite (devis produit
l'intervention), OpenFire (Zendesk et Odoo) documentent majoritairement le
sens inverse (intervention/étude → devis). Seul Costructor documente une
boucle bidirectionnelle symétrique et explicite.

**Phénomène 5 — Cause des verrous de sortie, jamais légale sauf pour la
facture.** Confirme et étend le motif déjà isolé par le pilote propagation :
les blocages sur les sorties du devis (commande, chantier, intervention) sont
toujours métier ou techniques ; seule la facture porte une cause
réglementaire explicite (anti-fraude TVA), reconfirmée par 3C sur ses propres
corpus (Obat, Costructor, InterFast, OpenFire×2).

**Phénomène 6 — Continuité terrain→étude→devis : deux pics isolés, pas un
standard.** InterFast (visite structurée) et OpenFire Zendesk (Vital Études,
génération automatique) sont les seuls cas de continuité documentée ; le
reste du marché observé est silencieux ou fragmentaire (§10bis).

## 18. Invariants candidats

| ID | INVARIANT CANDIDAT | PREUVES | CONTRE-EXEMPLES | STATUT |
|---|---|---|---|---|
| INV-3C-1 | Une facture d'acompte/situation déjà émise est déduite automatiquement (RECALCULÉ) du document de facturation suivant, jamais ressaisie manuellement à l'identique. | Vertuoza, InterFast, Sellsy, OpenFire (Odoo), Obat, Costructor — 6 éditeurs indépendants | Axonaut et Sellsy documentent des exclusions croisées (acompte + factures partielles incompatibles) qui nuancent sans infirmer le principe | CANDIDAT_FORT |
| INV-3C-2 | Le devis original reste consultable après transformation en objet aval, quel que soit l'objet cible. | Sellsy, Vertuoza, InterFast, Obat, Costructor, Axonaut (via commande) | Aucun contre-exemple relevé | CANDIDAT_FORT |
| INV-3C-3 | Le devis change d'état (verrouillage direct ou indirect) au moment où il produit sa première sortie structurante (facture, commande, chantier). | 7/8 éditeurs | OpenFire (Odoo) ne documente aucun verrou du devis à aucune étape (fait déjà acquis 3B, reconfirmé ici) | CANDIDAT_PROBABLE |
| INV-3C-4 | Le blocage/verrou d'une sortie du devis n'a jamais de cause légale, sauf pour la facture elle-même. | Tous les blocages non-facture recensés en §14 sont motivés métier/technique ou non motivés | Aucun contre-exemple : aucune source n'invoque de cause légale hors facture/avoir | CANDIDAT_FORT |
| INV-3C-5 | Un même devis peut produire plusieurs objets aval du même type (factures de situation, commandes fournisseur), jamais un seul et unique document figé. | 6+ éditeurs (§16) | Vertuoza impose une séquentialité stricte (un seul avancement « en cours ») — nuance la multiplicité sans l'infirmer | CANDIDAT_PROBABLE |
| INV-3C-6 | Le chemin devis→facture nécessite systématiquement un objet pivot (commande, bon de commande, chantier ou intervention) OU une transformation directe — jamais les deux à la fois chez un même éditeur. | 8/8 corpus classables sans ambiguïté dans l'une ou l'autre famille (§5) | Aucun éditeur ne documente les deux mécanismes en parallèle pour le même type de facture | CANDIDAT_PROBABLE |
| INV-3C-7 | Une étude technique intermédiaire (dimensionnement) alimentant automatiquement les lignes d'un devis existe mais reste une spécificité verticale, jamais un mécanisme générique de plateforme. | OpenFire (Zendesk, Vital Études) seul cas de génération automatique confirmée | 7/8 autres corpus silencieux ou avec liaison manuelle seulement | VARIANTE |

## 19. Contrat fonctionnel observé des sorties du devis

1. **Quels objets peuvent naître du devis** : facture (ordinaire, acompte,
   situation, solde), commande client, commande/demande de prix fournisseur,
   chantier/projet, intervention, planning/tâche, et une poignée d'objets
   émergents spécifiques (parc installé, bordereau de chantier, décompte
   général, facture proforma).
2. **Quels événements les déclenchent** : finalisation, acceptation ou
   signature du devis (selon l'éditeur, jamais uniformément), rarement le
   simple envoi. Aucun événement de préparation (enregistrement, génération
   PDF) n'a d'effet de sortie documenté nulle part.
3. **Quelles conditions sont nécessaires** : un statut minimal du devis
   (finalisé, accepté, ou signé selon l'éditeur — pas de convention unique) ;
   parfois un objet intermédiaire obligatoire (commande, bon de commande,
   chantier) ; parfois une exclusivité entre deux chemins de sortie
   concurrents (acompte vs situations, situation vs finale).
4. **Quelles informations suivent** : client, adresses, lignes/produits,
   montants et taxes sont COPIÉS presque partout où la relation est
   documentée ; les acomptes/situations déjà facturés sont RECALCULÉS et
   déduits, jamais ressaisis ; les prix catalogue peuvent être SNAPSHOTTÉS
   (Obat) ; le mode technique exact reste NON DÉTERMINÉ pour la grande
   majorité des propagations.
5. **Quelles relations sont conservées** : le devis reste presque toujours
   visible et consultable après transformation ; l'objet aval référence
   généralement le devis d'origine (champ verrouillé) ; la navigation
   bidirectionnelle est documentée dans quelques cas (InterFast, Costructor).
6. **Quels effets secondaires apparaissent** : décrément/incrément de stock,
   notifications, création automatique d'objets liés (bon de livraison, ligne
   d'acompte dans la commande d'origine), déclenchement d'automatisations
   commerciales (CRM), effets en cascade (opportunité perdue → devis annulé).
7. **Quelles opérations sont réversibles** : la plupart des sorties « objet
   conteneur vide » (chantier, commande sans documents) sont réversibles avec
   retour à l'état antérieur du devis ; la facture finalisée est
   systématiquement irréversible directement (correction par avoir
   uniquement, pour cause réglementaire) ; plusieurs zones grises subsistent
   (variante signée + facture déjà émise chez Obat, effet d'une modification
   du devis sur un objet déjà créé, largement NON DÉTERMINÉ).
8. **Comment les corrections sont gérées** : jamais par réécriture silencieuse
   de l'historique — toujours par un document correctif (avoir), un retour de
   statut documenté (Envoyé, Finalisé), ou une action de recovery nommée
   (annulation de signature chez Obat).
9. **Quelles divergences entre éditeurs sont réellement structurantes** :
   l'existence ou non d'un objet pivot obligatoire entre devis et facture
   (§5, §17 phénomène 1) ; la présence ou l'absence du concept de chantier
   (§8, §17 phénomène 3) ; le sens de la relation devis↔intervention (§9,
   §17 phénomène 4) ; l'existence, très rare et verticale, d'une génération
   automatique de devis depuis une étude technique terrain (§10bis).

## 20. Standards forts / probables

Repris des invariants (§18) : INV-3C-1 (déduction automatique des
acomptes/situations) et INV-3C-2 (devis conservé et consultable après
transformation) sont STANDARD_FORT. INV-3C-3 (verrouillage du devis à sa
première sortie), INV-3C-5 (multiplicité des objets aval) et INV-3C-6
(pivot obligatoire OU transformation directe, jamais les deux) sont
STANDARD_PROBABLE. La capacité même « le devis peut produire une facture »
est un STANDARD_FORT (8/8), indépendamment du mécanisme.

## 21. Variantes de marché

- **Architecture devis→facture** : transformation directe vs objet pivot
  obligatoire (commande/bon de commande) vs passage exclusif par un chantier
  ou une intervention (§5, §17).
- **Présence du concept chantier/projet** : central chez les spécialistes
  BTP, absent chez les généralistes, réattribué à l'opportunité chez OpenFire
  Odoo (§8).
- **Sens de la relation devis↔intervention** : devis→intervention (InterFast,
  Vertuoza) vs intervention→devis (OpenFire×2) vs boucle bidirectionnelle
  (Costructor) (§9).
- **Localisation du pivot fournisseur** : dans la commande client (Axonaut),
  via le bon de livraison (OpenFire Zendesk, chaîne à 6 étapes), directement
  depuis un article de type Service (OpenFire Odoo), ou par sélection de
  lignes à la carte depuis le devis (Costructor, Obat) (§7).
- **Continuité terrain→étude→devis** : verticale et génératrice chez OpenFire
  Zendesk (Vital Études), structurée mais manuelle chez InterFast, en
  construction chez Obat, absente ailleurs (§10bis).

## 22. Non déterminé

- Le mode technique exact (COPIÉ vs RÉFÉRENCÉ) de la quasi-totalité des
  propagations recensées en §11 — silence structurel confirmé par 3C sur
  l'ensemble des couples devis→aval, cohérent avec le constat déjà fait par
  le pilote propagation et 3A/3B.
- L'effet d'une modification du devis après création d'un objet aval sur cet
  objet aval déjà créé — silence quasi total (exception partielle : Costructor
  sur la signature invalidée).
- L'effet d'une annulation de signature de variante sur une facture déjà
  émise à partir de cette variante (Obat) — lacune de preuve isolée et
  signalée par l'agent d'extraction lui-même.
- Le critère exact de bifurcation devis→chantier vs devis→intervention chez
  Vertuoza — un seul passage documente l'existence de la bifurcation, sans
  jamais en détailler le déclencheur.
- La multiplicité exacte de certains couples (devis→bons de commande
  fournisseur multiples chez InterFast/Costructor, devis→bons de commande
  client multiples chez Costructor) — silence, pas absence.
- La fréquence réelle d'usage de chaque mécanisme documenté (objet pivot vs
  transformation directe, continuité terrain→étude) dans la pratique des
  artisans — hors périmètre documentaire de cette mission.
- Le contenu exact transporté par la liaison calcul de déperdition↔devis chez
  OpenFire (Odoo et Zendesk pour le second outil) — l'existence du lien est
  documentée, son contenu ne l'est pas.

## 23. Questions SUPORDO désormais instruisibles

**Que doit produire l'acceptation/la finalisation/la signature d'un devis ?**
- FAITS DISPONIBLES : aucune convention unique côté marché — certains
  éditeurs déclenchent une facture directement, d'autres une commande, d'autres
  un chantier. Le choix SUPORDO est donc un choix de conception assumé, pas
  une convention à copier.
- TERRAIN NÉCESSAIRE : non pour la décision de principe (le corpus documente
  suffisamment les options et leurs implications) ; oui pour calibrer
  laquelle correspond le mieux à l'usage réel des artisans SUPORDO.

**Faut-il un objet « commande » intermédiaire entre devis et facture, ou une
transformation directe ?**
- FAITS DISPONIBLES : §5, §17 phénomène 1 — les deux modèles sont également
  bien attestés (4 éditeurs nets par famille), avec un cas extrême (Vertuoza)
  où AUCUNE transformation directe n'existe.
- VARIANTES OBSERVÉES : objet pivot = conteneur organisationnel unique
  (Axonaut) vs simple évolution de statut du même document (OpenFire) vs
  absence totale, remplacée par le chantier/l'intervention (Vertuoza).
- TERRAIN NÉCESSAIRE : non pour la décision de principe ; oui pour arbitrer
  la complexité acceptable pour l'utilisateur cible SUPORDO.

**Faut-il un chantier/projet obligatoire, optionnel, ou absent ?**
- FAITS DISPONIBLES : clivage net entre spécialistes BTP (concept riche et
  central) et généralistes (absent) — cohérent avec le positionnement métier
  de SUPORDO.
- TERRAIN NÉCESSAIRE : non — le corpus suffit à motiver un chantier au moins
  optionnel, cohérent avec la cible BTP de SUPORDO.

**Comment gérer les acomptes et le solde ?**
- FAITS DISPONIBLES : mécanisme robuste et convergent (§6, INV-3C-1) —
  paramètre au niveau du devis, facture d'acompte distincte, déduction
  automatique au document suivant.
- TERRAIN NÉCESSAIRE : non pour le principe ; oui pour arbitrer les
  exclusions croisées (acompte + factures partielles simultanées, par
  exemple) selon les usages réels.

**Comment gérer la relation devis↔intervention/planning ?**
- FAITS DISPONIBLES : deux sens documentés, une boucle bidirectionnelle
  existe (Costructor) ; le sens « intervention/étude → devis » est plus
  riche chez les éditeurs qui le documentent que le sens attendu.
- VARIANTES OBSERVÉES : SUPORDO devra choisir explicitement quel sens
  privilégier ou s'il permet les deux.
- TERRAIN NÉCESSAIRE : oui — la variance est trop structurante pour trancher
  sans observer le déroulement réel d'une mission BTP (devis avant ou après
  la visite technique).

**Faut-il un mécanisme de génération automatique de devis depuis une étude
technique terrain ?**
- FAITS DISPONIBLES : un seul cas net et bien documenté (Vital Études,
  OpenFire Zendesk), sur un vertical précis (dimensionnement ventilation) ;
  le reste du marché documente au mieux des briques disjointes.
- INFORMATION MANQUANTE : le corpus ne permet pas de savoir si ce mécanisme
  est perçu comme fiable/adopté par les utilisateurs OpenFire, ni s'il est
  transposable aux verticaux visés par SUPORDO.
- TERRAIN NÉCESSAIRE : oui — c'est une des rares questions de la mission 3C
  où le corpus documentaire est structurellement insuffisant (1 seul cas net)
  pour fonder une décision de principe.

**Comment gérer la correction d'une sortie déjà produite ?**
- FAITS DISPONIBLES : le principe « jamais de réécriture silencieuse de
  l'historique, toujours un document/statut correctif » est robuste (§14,
  §19 point 8), avec une cause réglementaire uniquement pour la facture.
- TERRAIN NÉCESSAIRE : non pour le principe général ; oui pour calibrer le
  niveau de friction acceptable (avoir systématique vs retour de statut plus
  souple).

## 24. Questions terrain / produit restantes

- Les artisans qui utilisent un logiciel sans objet chantier/commande
  intermédiaire (profil Axonaut/Sellsy) perçoivent-ils cette simplicité comme
  un avantage, ou contournent-ils la limite avec des outils externes ?
- La friction du modèle Costructor/Vertuoza (devis modifié invalide une
  signature, ou bifurcation chantier/intervention peu documentée) est-elle
  vécue comme protectrice ou comme un frein commercial réel ?
- Le mécanisme « Vital Études » (génération automatique de devis depuis une
  étude) est-il perçu comme fiable par les artisans du vertical concerné, ou
  nécessite-t-il systématiquement une relecture manuelle intégrale ?
- Dans la pratique réelle, un devis est-il généralement produit avant ou
  après la visite technique, chez les artisans BTP visés par SUPORDO ?
- La possibilité de produire plusieurs commandes fournisseur / factures de
  situation depuis un même devis est-elle un besoin fréquent, ou une capacité
  technique rarement utilisée ?
- Les artisans perçoivent-ils la distinction acompte / situation / solde
  comme claire, ou source de confusion pratique (cf. les incohérences
  documentaires internes déjà relevées chez Axonaut, InterFast en 3B) ?

## 25. Limites

- **Corrections apportées aux missions antérieures, à intégrer** : le
  concept de chantier chez Obat, classé NON DÉTERMINÉ en 3A par silence
  documentaire, existe en réalité de façon riche (§8) ; le trou devis→facture
  identifié par le pilote propagation pour Sellsy, Costructor et Axonaut est
  comblé ou reclassé pour ces trois éditeurs (§5) ; Vertuoza, longtemps classé
  comme simple trou documentaire sur ce même couple, présente en fait une
  séparation de régime positivement documentée (facture simple indépendante
  du devis).
- **Bifurcation Vertuoza devis→chantier/intervention** : la preuve de son
  existence repose sur une seule phrase source ; son mécanisme de sélection
  reste NON DÉTERMINÉ — à vérifier si une décision SUPORDO en dépendait
  directement.
- **Modules en développement (Obat Interventions, Obat Métrés)** : leur
  documentation décrit une cible produit, pas nécessairement un comportement
  déployé au moment de la collecte — à traiter avec prudence dans toute
  comparaison qui suppose un état stabilisé.
- **Le cas structurant terrain/étude (§10bis) repose sur un signal fort mais
  unique** (Vital Études) pour la partie la plus proche de l'hypothèse
  SUPORDO — un seul éditeur sur 8 documente une génération automatique de
  devis depuis une étude technique ; ce n'est pas suffisant pour établir un
  standard de marché, seulement une preuve d'existence de la capacité.
- **Aucune vérification sur des éditeurs hors des 8 corpus déjà retenus par
  3A/3B** (Batikko, Extrabat, Tolteck, Leobati) — cohérent avec la décision
  de suffisance déjà actée en 3A, non rouverte ici.
- **Le détail exhaustif des tableaux par éditeur** (fourni par chaque agent
  d'extraction, avec citations complètes) n'est pas reproduit intégralement
  dans ce livrable pour éviter une duplication disproportionnée par rapport à
  la question posée — conforme au principe de suffisance décisionnelle.
- **Marketing écarté des preuves structurantes** : plusieurs signaux
  marketing intéressants (Axonaut « bon de commande associé à un projet »,
  pages verticales Sellsy évoquant chantier/intervention) ont été
  explicitement exclus des conclusions faute de corroboration par la
  documentation support — à vérifier par un test produit direct si une
  décision SUPORDO en dépendait.

## 26. Verdict

**L'analyse permet-elle maintenant de répondre suffisamment à : « Que produit
un devis vers l'aval, quelles informations suivent, quels effets sont
déclenchés, et comment les erreurs/corrections sont-elles gérées ? »**

**EXPLOITABLE.**

Justification stricte au regard du critère de la mission : 8 corpus
indépendants, couvrant les 4 familles de marché déjà imposées en 3A/3B avec
corroboration systématique, permettent de reconstruire concrètement la carte
des objets aval (§3), la matrice des relations de sortie (§4), le mécanisme
de facturation dans ses deux familles structurantes (§5), le mécanisme
d'acompte/situation/solde de façon convergente et robuste (§6, INV-3C-1), les
relations vers la commande, le chantier et l'intervention avec leurs
divergences réellement structurantes identifiées et nommées (§7-9, §17), le
cas complémentaire terrain/étude avec un signal fort mais isolé (§10bis), la
propagation des données (§11), les effets secondaires et les mécanismes de
recovery (§13-14), la réversibilité (§15) et la multiplicité (§16) — avec
suffisamment de matière convergente pour instruire directement 6 des 7
questions SUPORDO listées en §23 sans enquête terrain supplémentaire pour
leur décision de principe.

Deux points restent structurellement insuffisants pour une décision de
principe sans corroboration terrain : le sens à privilégier pour la relation
devis↔intervention (deux modèles également attestés, §9/§23) et la pertinence
d'un mécanisme de génération automatique de devis depuis une étude technique
(un seul cas net sur 8, §10bis/§23) — ces deux limites sont nommées et non
dissimulées, conformément à la discipline du dépôt.

Cette mission clôt également deux corrections utiles aux missions
antérieures (chantier Obat en 3A, régime devis→facture Vertuoza/Sellsy/
Costructor/Axonaut par rapport au pilote propagation), documentées en §25
plutôt que silencieusement absorbées.

3A + 3B + 3C fournissent désormais, ensemble, une matière suffisante pour
arrêter l'analyse concurrentielle ciblée du devis et passer à la conception
du contrat fonctionnel SUPORDO du devis — sans attendre une exhaustivité
supplémentaire sur les deux points résiduels identifiés ci-dessus, qui
relèvent du calibrage fin, pas de la structure d'ensemble.

DEVIS_3C_TERMINE — EXPLOITABLE — STOP
