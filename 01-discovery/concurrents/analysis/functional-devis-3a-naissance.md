# 3A — Naissance du devis : exploitation fonctionnelle ciblée

Mission ciblée, un seul sous-problème (comment un devis naît dans les logiciels
concurrents), un seul livrable, un seul verdict, puis stop. N'est pas une
extraction V2/V3, ne modifie pas LIGHT ni SCHEMA-LIGHT, ne prend aucune
décision produit SUPORDO définitive.

## 1. Question

Comment un devis naît-il dans les logiciels concurrents ? Reconstruire le
contrat fonctionnel VISIBLE de création du devis : ce qui doit déjà exister,
depuis où on peut créer le devis, si client/contact est requis, si
projet/affaire/chantier est requis, si site/adresse est requis, quelles
dépendances sont créables pendant la création, quelles données sont
préremplies ou héritées, si des lignes libres sont possibles, si le catalogue
est utilisable, si on peut partir d'un modèle ou d'un devis précédent, si la
duplication est possible, quel état initial reçoit le devis, et quelles
actions immédiates permettent de terminer sa création.

## 2. Périmètre et exclusions

Explicitement hors périmètre, quelle que soit la richesse documentaire
rencontrée en cours de lecture : cycle de vie complet du devis après
création, envoi, relance, acceptation/refus, signature détaillée,
révision/avenant après engagement, facturation détaillée, commandes,
permissions complètes, gestion fine des erreurs, transitions ultérieures.
Ces sujets ont été systématiquement écartés des tableaux même quand un
document sélectionné les couvrait — chaque agent d'extraction a explicitement
noté les fichiers ou passages « sans apport » pour cette raison plutôt que de
les intégrer hors-sujet.

## 3. Sélection des sources

### 3.1 Instruments consultés avant lecture

`CLAUDE.md` et `SCHEMA-LIGHT.md` lus intégralement. `functional-onboarding-pilot.md`
et `functional-propagation-pilot.md` lus intégralement comme signal E (travaux
déjà acquis). Le pilote onboarding porte le verdict **RENDEMENT_SUFFISANT** —
gate de démarrage validé, mission poursuivie.

`GLOSSAIRE-OBSERVE-LIGHT.md` (2539 lignes, 424 Ko) et `corpus_index.json`
(7332 lignes, 288 Ko) dépassent la taille de lecture complète de l'outil ;
conformément à la limite déjà documentée par les deux pilotes précédents, ils
n'ont pas été relus intégralement pour cette mission.

### 3.2 Méthode de sélection effectivement appliquée — écart assumé par rapport à la commande

La commande de mission prescrivait une sélection multi-signaux incluant un
grep mécanique du champ `moment_parcours = devis` sur les 11 fichiers
`light-*.md`. **Ce grep n'a pas été exécuté pour cette mission.** À la place,
la sélection s'est appuyée sur :

- **Signal C (rubriques/chemins)** — inspection directe de l'arborescence
  physique des corpus sources (`01-discovery/concurrents/sources/<editeur>/`)
  pour repérer les rubriques éditoriales dédiées au devis, aux ventes, aux
  clients/contacts et au catalogue (ex. `vertuoza/devis/`, `axonaut/gerez-vos-devis/`,
  `sellsy/documents-de-vente/`, `costructor/ventes/`, `openfire/documentation_2/knowsystem/`
  filtré par nom de fichier).
- **Signal D (recherche textuelle)** — recherche de motifs (`devis`, `client`,
  `chantier`, `contact`, `catalogue`) directement sur les noms de fichiers du
  corpus source, complétée par une lecture manuelle des noms de dossiers
  ambigus (cas Obat, où des dossiers au nom de slug « devis » contiennent en
  réalité un fichier `factures.md` — artefact de collecte vérifié par lecture
  avant inclusion, non un dossier vide).
- **Signal E (travaux déjà acquis)** — `functional-onboarding-pilot.md` et
  `functional-propagation-pilot.md` ont orienté le choix des éditeurs
  (rendement `filtre A` du pilote propagation par éditeur, richesse déjà
  observée sur InterFast/Vertuoza/OpenFire Odoo pour les mécanismes
  d'héritage).

**Justification de cet écart** : les rubriques éditoriales dédiées au devis
identifiées directement dans l'arborescence physique (`devis/`, `ventes/`,
`documents-de-vente/`, `gerez-vos-devis/`) constituaient un signal plus
précis et plus économe que d'extraire mécaniquement le champ `moment_parcours`
d'un fichier LIGHT de 2500+ lignes par éditeur — ces rubriques donnent
directement une liste fermée de fichiers pertinents. Ceci est documenté
comme un **écart méthodologique assumé**, pas un oubli silencieux ; il est
repris en section 19 comme limite de l'analyse. Le champ `objet_principal`
(signal A) n'a pas non plus été grepé mécaniquement pour la même raison.

### 3.3 Séparation stricte OpenFire

Conformément à la règle du dépôt, les deux corpus OpenFire ont été traités
comme deux sources indépendantes, par deux agents distincts n'ayant accès
qu'à leur propre corpus : **OpenFire (Zendesk)** (`bien-debuter/`,
`configurer-openfire/`, `utiliser-openfire/`) et **OpenFire (Odoo)**
(`documentation_2/knowsystem/`). Aucune fusion, aucune comparaison implicite
entre les deux dans les tableaux qui suivent — chaque tableau les présente
comme deux lignes distinctes.

### 3.4 Discipline d'exécution

Chaque éditeur (8 corpus au total, OpenFire compté deux fois) a été confié à
un agent dédié, contraint à une liste fermée de fichiers déterminée à
l'avance, lecture intégrale obligatoire, aucune autre source autorisée
(pas de web, pas d'autre éditeur, pas de mémoire générale du modèle sur ces
logiciels). Chaque agent a produit un rapport structuré avec citations
exactes et chemins de fichiers, exploité tel quel dans les sections
suivantes. Aucun agent n'a eu accès aux rapports des autres — le
rapprochement inter-éditeurs est fait après coup, par l'orchestrateur, à
partir des 8 rapports reçus séparément.

## 4. Couverture et diversité des éditeurs

| Famille | Éditeur(s) lus | Fichiers lus / liste fermée | Fichiers exploités |
|---|---|---:|---:|
| BTP spécialiste | Vertuoza | 19/19 | 14 |
| BTP spécialiste (corroboration) | InterFast | 19/19 | 14 |
| Généraliste | Axonaut | 14/14 | 7 |
| Généraliste (corroboration) | Sellsy | 22/22 | 15 |
| ERP / logiciel métier structuré | OpenFire (Zendesk) | 15/15 | 10 |
| ERP / logiciel métier structuré (corpus séparé) | OpenFire (Odoo) | 10/10 | 10 |
| Artisan léger | Obat | 19/19 | 12 |
| Artisan léger (corroboration) | Costructor | 15/15 | 12 |
| **Total** | **8 corpus, 7 éditeurs** | **133/133** | **94** |

Les quatre familles imposées par la mission sont couvertes, chacune avec un
éditeur principal et une corroboration indépendante — décision de suffisance
prise avant lecture (viser une richesse comparable au pilote propagation,
7 éditeurs) plutôt qu'un seul éditeur par famille, pour limiter le risque de
sur-généraliser depuis une seule source par profil de marché.

Non couverts pour cette mission (constat, pas décision de suffisance
détaillée faute de signal fort identifié en amont) : Batikko (corpus trop
mince, 14 fichiers au total selon le pilote onboarding), Extrabat (corpus
volumineux mais rendement LIGHT filtre A faible d'après le pilote
propagation), Tolteck/Leobati (corpus d'aide non collectés).

## 5. Sémantique nécessaire à cette question

Vocabulaire ouvert effectivement rencontré dans les 8 corpus, à ne pas
confondre avec un objet canonique SUPORDO :

- **Devis vs facture** : objets strictement distincts dans 7 corpus sur 8 ;
  Sellsy les traite comme deux variantes d'un même objet générique
  « document de vente », documenté explicitement (même écran, même
  protocole de création).
- **Client / société / contact / prospect** : hiérarchie à deux niveaux
  (société + contact) chez Vertuoza, Sellsy et OpenFire (les deux corpus) ;
  entité unique « client/prospect » sans distinction fonctionnelle
  documentée chez Axonaut, Obat, Costructor, InterFast (contact traité comme
  sous-objet du client, sélectionnable après coup).
- **Chantier / affaire** : objet central chez InterFast, Vertuoza, Obat,
  Costructor ; absent du vocabulaire des 15/22 fichiers Sellsy lus ; présent
  chez OpenFire (Zendesk) sous la forme voisine « contrat d'entretien » et
  chez OpenFire (Odoo) sous la forme « opportunité ».
- **Opportunité** : objet CRM distinct utilisé comme point d'entrée vers le
  devis chez Vertuoza et OpenFire (Odoo) uniquement.
- **Bibliothèque / ouvrage / catalogue / article / produit / kit** :
  vocabulaire propre à chaque éditeur pour désigner le même mécanisme
  (élément réutilisable inséré en ligne de devis) — « ouvrage »/« composant »
  (Vertuoza, Obat), « article » (OpenFire), « produit/service » (Axonaut,
  Sellsy), « élément » (Obat, Costructor), « produit centralisé »/« kit »
  (OpenFire Zendesk, spécifique au Tarif Centralisé multi-distributeurs).
- **Modèle de devis** : présent explicitement comme objet nommé chez
  InterFast, Axonaut (« thème »), Sellsy, OpenFire (les deux corpus),
  Costructor ; absent du vocabulaire Vertuoza (seul un « template » de rendu
  PDF existe, distinct du contenu) et Obat (« modèle » n'y désigne que les
  éléments de bibliothèque).
- **Variante / révision** : InterFast (« variante », document lié distinct)
  et Obat (« variante », duplication numérotée) partagent un vocabulaire et
  un mécanisme proches ; Costructor emploie « révision » pour un historique
  interne au même devis, duplicable.
- **Brouillon / Draft / en attente** : vocabulaire d'état très hétérogène,
  voir section 11.
- **Position fiscale / liste de prix / catégorie tarifaire** : vocabulaire
  propre à OpenFire (les deux corpus) et Sellsy pour des mécanismes de
  tarification conditionnelle : sans équivalent documenté chez les 6 autres
  corpus dans le périmètre lu.

## 6. Vue A — naissance du devis par concurrent

Chaque flèche est marquée DOCUMENTÉ (avec preuve) ou NON_DÉTERMINÉ. Les
citations complètes figurent dans les rapports d'agents sous-jacents ; seules
les preuves les plus structurantes sont reprises ici pour ne pas dupliquer
l'intégralité des tableaux noyau (disponibles en synthèse §7-11).

### 6.1 Vertuoza

```
AVANT LE DEVIS (DOCUMENTÉ, partiel) — un contact ou une opportunité peuvent préexister
    ↓
POINT D'ENTRÉE (DOCUMENTÉ) — menu Offre > Devis > "Nouveau" ; ou fiche opportunité ("Créer ou lier un devis")
    ↓
CRÉATION (DOCUMENTÉ) — choix création native ou import Excel
    ↓
DÉPENDANCES (NON_DÉTERMINÉ sur l'obligation) — client listé comme catégorie d'info du devis, jamais qualifié d'obligatoire
    ↓
CRÉATIONS INLINE (NON_DÉTERMINÉ contact ; DOCUMENTÉ catalogue) — un poste libre peut être "enregistré dans la bibliothèque"
    ↓
DONNÉES PRÉREMPLIES (DOCUMENTÉ) — conditions particulières du contact, TVA, civilité, champs d'une opportunité liée
    ↓
LIGNES (DOCUMENTÉ) — poste libre, ouvrages/composants de bibliothèque, import Excel
    ↓
DEVIS CRÉÉ (DOCUMENTÉ implicitement — "une fois le devis enregistré...", sans bouton nommé)
    ↓
ÉTAT INITIAL (DOCUMENTÉ) — "Draft : le devis n'a pas encore été Soumis"
    ↓
ACTIONS IMMÉDIATES (NON_DÉTERMINÉ précisément) — compléter informations générales, encoder les lignes, condition particulière, pas de liste fermée d'actions "de fin de création"
```

### 6.2 InterFast

```
AVANT LE DEVIS (DOCUMENTÉ, partiel) — client, chantier ou visite préalable (rapport de visite) peuvent préexister
    ↓
POINT D'ENTRÉE (DOCUMENTÉ, multiple) — module Devis ("+ Nouveau Devis") ; fiche client ("Nouveau un devis") ; fiche chantier ("nouveau devis") ; fiche intervention/visite ("Créer un devis")
    ↓
CRÉATION (DOCUMENTÉ) — popup titre + client (créable) + modèle (optionnel)
    ↓
DÉPENDANCES (REQUIS mobile explicite ; NON_DÉTERMINÉ web) — "le Client associé (obligatoire)" sur mobile seulement
    ↓
CRÉATIONS INLINE (DOCUMENTÉ) — client, chantier, ouvrage sur mesure, tous créables sans quitter le devis
    ↓
DONNÉES PRÉREMPLIES (DOCUMENTÉ) — pied de page, RIB, signature du rédacteur, adresse de travaux conditionnelle
    ↓
LIGNES (DOCUMENTÉ, 8 mécanismes) — libre, bibliothèque, modèle, ancien devis/facture, import PDF via IA, import fournisseur
    ↓
DEVIS CRÉÉ / ÉTAT INITIAL (DOCUMENTÉ) — "Brouillon" : "le devis n'a pas de numéro" tant qu'il y reste
    ↓
ACTIONS IMMÉDIATES (DOCUMENTÉ) — configurer client, lier chantier, dates, infos paiement, passage à "Finalisé" (attribution du numéro)
```

### 6.3 Axonaut

```
AVANT LE DEVIS (DOCUMENTÉ, faible) — rien de strictement pré-requis, client ET produit créables depuis le devis
    ↓
POINT D'ENTRÉE (DOCUMENTÉ, double) — bouton global "+" > "Devis" ; fiche client > "+" > "ajouter un devis"
    ↓
CRÉATION (DOCUMENTÉ) — formulaire modèle/thème, client, lignes, remise, conditions
    ↓
DÉPENDANCES (NON_DÉTERMINÉ sur l'obligation) — "Ensuite, sélectionnons un client/prospect", jamais qualifié
    ↓
CRÉATIONS INLINE (DOCUMENTÉ) — client et produit tous deux créables sans quitter le devis
    ↓
DONNÉES PRÉREMPLIES (DOCUMENTÉ) — coordonnées client, conditions de paiement, langue documentaire
    ↓
LIGNES (DOCUMENTÉ) — catalogue uniquement (aucune ligne libre hors catalogue documentée)
    ↓
DEVIS CRÉÉ (DOCUMENTÉ) — achèvement par bouton "Valider"
    ↓
ÉTAT INITIAL (NON_DÉTERMINÉ précisément) — seul "devis en attente" est nommé, et fusionne "créé" et "envoyé"
    ↓
ACTIONS IMMÉDIATES (DOCUMENTÉ, minimal) — "Valider" est la seule action de finalisation nommée
```

### 6.4 Sellsy

```
AVANT LE DEVIS (DOCUMENTÉ) — "veillez à ce que les informations de votre entreprise soient à jour"
    ↓
POINT D'ENTRÉE (DOCUMENTÉ, multiple) — menu Facturation > "Créer un devis" ; duplication ("Copier ce document") ; depuis modèle ; onglet Documents d'une fiche client ou prospect
    ↓
CRÉATION (DOCUMENTÉ) — société (client) puis modèle/catégorie tarifaire/apparence/langue
    ↓
DÉPENDANCES (NON_DÉTERMINÉ sur l'obligation) — société présentée en première étape, jamais qualifiée d'obligatoire
    ↓
CRÉATIONS INLINE (DOCUMENTÉ) — société créable inline ; produit/service créable depuis la fenêtre catalogue pendant la création
    ↓
DONNÉES PRÉREMPLIES (DOCUMENTÉ) — adresses (société + client), catégorie tarifaire, contenu de modèle (hors lignes)
    ↓
LIGNES (DOCUMENTÉ) — ligne manuelle, catalogue, lecteur code-barres ; import/modèle-avec-lignes NON_DÉTERMINÉ
    ↓
DEVIS CRÉÉ (DOCUMENTÉ) — "vous pouvez l'enregistrer (en brouillon) ou l'envoyer"
    ↓
ÉTAT INITIAL (PARTIELLEMENT DOCUMENTÉ) — "en brouillon" employé pour le devis, mais aucun statut système nommé et confirmé (l'article dédié aux statuts brouillon ne couvre que factures/avoirs)
    ↓
ACTIONS IMMÉDIATES (DOCUMENTÉ) — société, paramètres, lignes, préférences du document, enregistrement
```

### 6.5 OpenFire (Zendesk)

```
AVANT LE DEVIS (NON_DÉTERMINÉ pour un ordre imposé) — un contact peut préexister
    ↓
POINT D'ENTRÉE (DOCUMENTÉ, multiple) — menu Ventes > "Nouveau" ; contrat d'entretien ("GENERER LES DOCUMENTS") ; intervention/DI (génération manuelle ou automatique) ; opportunité (chemin déductible, action UI non décrite)
    ↓
CRÉATION (DOCUMENTÉ) — formulaire vierge : Bloc Client, Dates, Devis, Facturation
    ↓
DÉPENDANCES (NON_DÉTERMINÉ sur l'obligation) — champ Client existe, jamais qualifié requis/facultatif
    ↓
CRÉATIONS INLINE (DOCUMENTÉ) — contact créable via menu déroulant ; produit centralisé importé en base locale à la validation
    ↓
DONNÉES PRÉREMPLIES (DOCUMENTÉ, très riche — 13 champs distincts) — adresses, liste de prix, position fiscale, conditions de paiement, vendeur, prospecteur, équipe commerciale, société, données marketing d'opportunité
    ↓
LIGNES (DOCUMENTÉ) — catalogue local, produit centralisé, kit, modèle ; ligne libre et duplication NON_DÉTERMINÉES (silence)
    ↓
DEVIS CRÉÉ (DOCUMENTÉ implicitement)
    ↓
ÉTAT INITIAL (PARTIELLEMENT DOCUMENTÉ) — "brouillon" documenté seulement pour la génération automatique désactivée depuis une intervention ; aucun mot d'état pour la création manuelle standard
    ↓
ACTIONS IMMÉDIATES (DOCUMENTÉ) — compléter Bloc Client/Dates/Devis/Facturation, ajouter lignes/sections/notes, CGV
```

### 6.6 OpenFire (Odoo)

```
AVANT LE DEVIS (DOCUMENTÉ, partiel) — un contact ou une opportunité peuvent préexister ; chaîne CONTACT→OPPORTUNITÉ→DEVIS documentée
    ↓
POINT D'ENTRÉE (DOCUMENTÉ, double et distinct) — Ventes > Devis > "Créer" (entrée directe) ; opportunité > "Nouveau devis" (entrée distincte : préremplit le client, lie l'opportunité)
    ↓
CRÉATION (DOCUMENTÉ) — client "dans un premier temps", puis position fiscale
    ↓
DÉPENDANCES (REQUIS pour le client "dans un premier temps" ; NON_DÉTERMINÉ caractère bloquant réel) — position fiscale "nécessairement" renseignée
    ↓
CRÉATIONS INLINE (DOCUMENTÉ) — client et article tous deux créables via "Créer et modifier" sans quitter le devis
    ↓
DONNÉES PRÉREMPLIES (DOCUMENTÉ, très riche) — adresses, date du jour, données d'opportunité (client, canal, origine, parrain), position fiscale/condition de règlement de modèle
    ↓
LIGNES (DOCUMENTÉ) — catalogue article, création inline d'article, modèle (remplace les lignes déjà saisies) ; ligne libre et import NON_DÉTERMINÉS (silence)
    ↓
DEVIS CRÉÉ (DOCUMENTÉ implicitement — "une fois votre devis créé et enregistré", mécanisme de sauvegarde non décrit)
    ↓
ÉTAT INITIAL (NON_DÉTERMINÉ) — aucun libellé d'état nommé dans les 10 fichiers lus
    ↓
ACTIONS IMMÉDIATES (DOCUMENTÉ, partiel) — client, position fiscale, lignes ; impression mentionnée comme action de contrôle post-sauvegarde
```

### 6.7 Obat

```
AVANT LE DEVIS (NON_DÉTERMINÉ, partiel) — client peut préexister (import en masse)
    ↓
POINT D'ENTRÉE (PARTIELLEMENT DOCUMENTÉ) — destination nommée "Nouveau Devis", chemin d'accès exact non décrit
    ↓
CRÉATION (DOCUMENTÉ, éléments d'interface) — numéro de devis, menu "Bibliothèque", "Sélectionner un client"
    ↓
DÉPENDANCES (REQUIS à la finalisation) — "il vous sera demandé d'attribuer un client sur chaque document" ; NON_DÉTERMINÉ pour le simple enregistrement en brouillon
    ↓
CRÉATIONS INLINE (DOCUMENTÉ) — client (particulier/professionnel), élément de bibliothèque pendant la composition d'un ouvrage
    ↓
DONNÉES PRÉREMPLIES (PARTIEL) — prix de bibliothèque SNAPSHOTTÉ explicitement au moment de la création
    ↓
LIGNES (DOCUMENTÉ, plusieurs mécanismes) — ouvrage composé depuis bibliothèque personnelle, bibliothèque Obat 2024, bibliothèque Batichiffrage, poste libre HT (ajustement, pas une ligne standard), assistant vocal (mécanisme non détaillé)
    ↓
DEVIS CRÉÉ / ÉTAT INITIAL (DOCUMENTÉ, vocabulaire) — "Brouillon", "Finalisé", "Envoyé", "Signé", "Refusé" (vue Kanban) ; état de départ déduit par INTERPRÉTATION, pas affirmé littéralement
    ↓
ACTIONS IMMÉDIATES (DOCUMENTÉ) — attribuer client, construire lignes, "Finaliser et envoyer" ou "finaliser sans envoi" (numéro définitif à la finalisation)
```

### 6.8 Costructor

```
AVANT LE DEVIS (DOCUMENTÉ) — client/prospect et chantier peuvent préexister via leurs propres flux
    ↓
POINT D'ENTRÉE (DOCUMENTÉ, multiple) — menu Devis > "nouveau devis" ; devis IA ; sélection de modèle (flèche) ; import DPGF/PDF
    ↓
CRÉATION (DOCUMENTÉ) — dates, client, chantier, titre, lignes
    ↓
DÉPENDANCES (NON_DÉTERMINÉ sur l'obligation) — client et chantier présentés comme étapes numérotées, jamais qualifiés
    ↓
CRÉATIONS INLINE (DOCUMENTÉ) — client/prospect et chantier tous deux créables sans quitter le devis
    ↓
DONNÉES PRÉREMPLIES (PARTIEL) — numérotation automatique explicite ; reste largement NON_DÉTERMINÉ (modèle, IA client/chantier NON préremplis si absents du prompt)
    ↓
LIGNES (DOCUMENTÉ, 8 mécanismes) — libre, catalogue/bibliothèque, modèle, révision dupliquée, avenant (saisie manuelle, pas de copie automatique), devis IA, import DPGF/DQE, import PDF, import de lignes d'un autre document
    ↓
DEVIS CRÉÉ (DOCUMENTÉ implicitement)
    ↓
ÉTAT INITIAL (PARTIELLEMENT DOCUMENTÉ, silence notable) — "brouillon" cité seulement dans des articles périphériques (impression, marges), jamais dans l'article de création lui-même
    ↓
ACTIONS IMMÉDIATES (DOCUMENTÉ) — dates, client, chantier, titre, lignes, personnalisation, acompte, numérotation, "Enregistrer et finaliser"
```

## 7. Dépendances objet → devis (comparaison inter-éditeurs)

Statuts observés uniquement quand une preuve source existe ; NON_DETERMINE
partout ailleurs (silence documentaire, jamais traité comme facultatif).

| Relation | Vertuoza | InterFast | Axonaut | Sellsy | OpenFire (Zendesk) | OpenFire (Odoo) | Obat | Costructor |
|---|---|---|---|---|---|---|---|---|
| CLIENT/SOCIÉTÉ → DEVIS | NON_DÉT. (oblig.) ; HÉRITÉ | REQUIS (mobile) ; CRÉABLE_INLINE | NON_DÉT. (oblig.) ; CRÉABLE_INLINE ; HÉRITÉ | CRÉABLE_INLINE ; NON_DÉT. (oblig.) | NON_DÉT. (oblig.) ; CRÉABLE_INLINE ; HÉRITÉ | REQUIS ("1er temps") ; CRÉABLE_INLINE ; HÉRITÉ | REQUIS (finalisation) ; CRÉABLE_INLINE | CRÉABLE_INLINE ; NON_DÉT. (oblig.) |
| CONTACT → DEVIS (distinct du client) | HÉRITÉ ; NON_DÉT. inline | FACULTATIF/CRÉABLE_INLINE (post-création) | NON_DÉTERMINÉ (objet non distingué) | NON_DÉTERMINÉ (contact interne ≠ contact client) | CRÉABLE_INLINE ; NON_DÉT. requis | (= client, non distinct) | (= client, non distinct) | (= client/prospect, non distinct) |
| PROSPECT → DEVIS | HÉRITÉ (via opportunité) ; NON_DÉT. direct | NON_DÉTERMINÉ (silence total) | FACULTATIF | CRÉABLE, restreint (devis seul autorisé avant conversion) | NON_DÉT. (effet inverse documenté seulement) | NON_DÉTERMINÉ | NON_DÉTERMINÉ | CRÉABLE (même flux que client) |
| SITE/ADRESSE → DEVIS | NON_DÉTERMINÉ | FACULTATIF ; HÉRITÉ conditionné | HÉRITÉ ; FACULTATIF (livraison distincte) | HÉRITÉ, modifiable | HÉRITÉ (secondaires) ; question ouverte inline | HÉRITÉ (facturation/livraison) | NON_DÉTERMINÉ | NON_DÉTERMINÉ (direct) |
| PROJET/AFFAIRE/CHANTIER → DEVIS | NON_DÉT. comme précondition (sens inverse documenté) | FACULTATIF ; CRÉABLE_INLINE | NON_DÉTERMINÉ | NON_DÉTERMINÉ (notion absente) | NON_DÉT. direct (analogue "contrat") | NON_DÉT. direct (analogue "opportunité") | NON_DÉTERMINÉ | FACULTATIF ; CRÉABLE_INLINE |
| OPPORTUNITÉ → DEVIS | HÉRITÉ (si liée) ; FACULTATIF | — (non pertinent) | — | — | — | HÉRITÉ ; FACULTATIF ; point d'entrée distinct | — | — |
| MODÈLE → DEVIS | NON_DÉTERMINÉ (PDF seul) | FACULTATIF ; HÉRITÉ | FACULTATIF ; HÉRITÉ (thème) | FACULTATIF ; HÉRITÉ (hors lignes) | FACULTATIF ; HÉRITÉ | FACULTATIF ; HÉRITÉ (remplace lignes saisies) | NON_DÉTERMINÉ | FACULTATIF ; HÉRITÉ |
| DEVIS_EXISTANT → NOUVEAU_DEVIS | CRÉABLE (bouton, contenu NON_DÉT.) | CRÉABLE (duplication + variante) | CRÉABLE (duplication) | CRÉABLE (copie) | NON_DÉTERMINÉ | NON_DÉTERMINÉ | CRÉABLE (variante, contenu repris) | CRÉABLE (révision, recréation, avenant) |
| CATALOGUE/PRODUIT/OUVRAGE → DEVIS | CRÉABLE_INLINE (bidirectionnel) ; HÉRITÉ | FACULTATIF ; CRÉABLE_INLINE ; HÉRITÉ | FACULTATIF ; CRÉABLE_INLINE | FACULTATIF ; CRÉABLE_INLINE | CRÉABLE_INLINE ; HÉRITÉ | REQUIS (amont) ; CRÉABLE_INLINE ; HÉRITÉ | CRÉABLE_INLINE ; HÉRITÉ (snapshot) | FACULTATIF/RÉFÉRENCÉ ; CRÉABLE_INLINE |

**Lecture principale** : CLIENT créable en ligne pendant la création du devis
est documenté indépendamment par les 8 corpus — la relation la plus
convergente de toute la mission avec CATALOGUE créable en ligne (également
8/8). Le caractère strictement REQUIS du client n'est en revanche affirmé
explicitement que par 3 corpus sur 8 (InterFast mobile, OpenFire Odoo, Obat à
la finalisation) ; ailleurs c'est un silence documentaire, jamais une preuve
de facultativité.

## 8. Données préremplies / héritées à la création

Convergences observées (preuves complètes dans les rapports par éditeur,
sections 5) :

| Donnée héritée | Éditeurs qui la documentent | Source de la donnée |
|---|---|---|
| Adresse(s) de facturation/livraison | Vertuoza, Axonaut, Sellsy, OpenFire (Zendesk), OpenFire (Odoo) | Fiche contact/société/client |
| Conditions de paiement par défaut | Vertuoza, Axonaut, OpenFire (Zendesk), InterFast (RIB) | Contact / configuration générale |
| Position fiscale / TVA | OpenFire (Zendesk), OpenFire (Odoo) | Fiche client, sauf priorité du modèle si sélectionné après |
| Prix/description d'un élément catalogue | Vertuoza, InterFast, OpenFire (les deux), Obat, Axonaut | Fiche produit/ouvrage/article |
| Contenu d'un modèle (hors lignes) | Sellsy (explicitement SANS les lignes) | Modèle de document |
| Contenu d'un modèle (avec lignes) | InterFast, OpenFire (les deux), Costructor | Modèle de devis |
| Données d'une opportunité liée (client, canal, origine) | Vertuoza, OpenFire (Odoo) | Opportunité CRM |
| Prix figé au moment de l'ajout (snapshot explicite) | Obat seul (mode technique SNAPSHOTTÉ affirmé littéralement) | Bibliothèque |

Le **mode technique** (COPIÉ/RÉFÉRENCÉ/GÉNÉRÉ/RÉINITIALISÉ) n'est tranché
explicitement que dans de rares cas : Obat (SNAPSHOTTÉ, prix figé), Costructor
(GÉNÉRÉ, numérotation automatique) et OpenFire (Zendesk) (GÉNÉRÉ, description
technique du produit). Partout ailleurs, "NON DOCUMENTÉ" — conforme au constat
déjà fait par le pilote propagation : les documentations concurrentes
décrivent le comportement visible, rarement le mécanisme backend.

## 9. Construction des lignes du devis

| Mécanisme | Éditeurs qui le documentent | Éditeurs muets (silence, pas absence) |
|---|---|---|
| Ligne libre (texte/saisie manuelle, hors catalogue) | Vertuoza, InterFast, Sellsy, Costructor | Axonaut, OpenFire (Zendesk), OpenFire (Odoo), Obat (seul "poste libre HT" = ajustement de total, pas une ligne standard) |
| Catalogue / bibliothèque | Les 8 corpus | — |
| Modèle préremplissant les lignes | InterFast, OpenFire (Zendesk), OpenFire (Odoo), Costructor | Sellsy (documenté comme excluant les lignes), Vertuoza, Axonaut, Obat |
| Duplication / ancien devis comme source de lignes | Vertuoza (copier/coller ligne), InterFast, Axonaut, Sellsy, Obat (variantes), Costructor (révision, avenant) | OpenFire (les deux corpus) |
| Import fichier (Excel/PDF/DPGF/IA) | Vertuoza (Excel), InterFast (PDF via IA), Costructor (DPGF/DQE, PDF, IA) | Axonaut, Sellsy, OpenFire (Zendesk, OpenImport limité au catalogue), Obat (recréation logiciel tiers, contenu NON_DÉT.) |

**Variance structurante** : Axonaut et les deux corpus OpenFire ne
documentent, dans le périmètre lu, aucun mécanisme de ligne totalement libre
hors catalogue — chaque ligne semble adossée à un produit/article, créé à la
volée si besoin, mais jamais un texte chiffré sans entité produit sous-jacente.
C'est un silence répété chez 3 corpus sur 8, à traiter comme une variante
potentielle de marché plutôt qu'une conclusion (silence documentaire ≠
absence fonctionnelle).

## 10. UX de création documentée

| Éditeur | Point(s) d'entrée principal(aux) | Classification dominante |
|---|---|---|
| Vertuoza | Liste devis, fiche opportunité | UX_PARTIELLEMENT_RECONSTRUCTIBLE |
| InterFast | Module Devis, fiche client, fiche chantier, fiche intervention | UX_DOCUMENTEE pour la popup et la duplication/variante/import ; PARTIELLEMENT pour les entrées secondaires |
| Axonaut | Bouton global, fiche client | UX_PARTIELLEMENT_RECONSTRUCTIBLE |
| Sellsy | Menu Facturation, duplication, modèle, fiche client/prospect | UX_DOCUMENTEE pour le protocole générique ; PARTIELLEMENT pour les entrées via fiche |
| OpenFire (Zendesk) | Menu Ventes, contrat d'entretien, intervention/DI | UX_DOCUMENTEE pour les 3 entrées détaillées ; PARTIELLEMENT pour l'entrée opportunité (action UI non décrite) |
| OpenFire (Odoo) | Menu Ventes, opportunité | UX_DOCUMENTEE pour la création inline (client/article) ; PARTIELLEMENT pour le formulaire principal et la sauvegarde |
| Obat | Destination "Nouveau Devis", sidepanel d'un devis existant | UX_DOCUMENTEE pour la variante ; PARTIELLEMENT pour le point d'entrée principal (chemin exact non décrit) |
| Costructor | Menu Devis, devis IA, import, révisions | UX_DOCUMENTEE pour la majorité des mécanismes alternatifs ; PARTIELLEMENT pour la création manuelle standard elle-même dans son détail d'interface |

**Motif transversal** : dans 7 corpus sur 8, l'écran de création "normal"
(bouton principal → formulaire) est décrit par ses champs et son ordre
éditorial mais jamais par sa mécanique d'interface exacte (modal vs page
dédiée, comportement bloquant ou non). À l'inverse, les mécanismes
alternatifs et plus rares (duplication, variante, import, devis IA) sont
presque systématiquement décrits avec un luxe de détail supérieur — sans
doute parce qu'ils justifient un article dédié alors que l'écran principal
est considéré comme trivial par les rédacteurs de documentation.

## 11. État initial et actions immédiates

| Éditeur | Vocabulaire exact | Robustesse de la preuve |
|---|---|---|
| Vertuoza | « Draft » | Affirmé littéralement dans l'article de création |
| InterFast | « Brouillon » | Affirmé littéralement, fait partie d'un statut système à 7 valeurs documenté (Brouillon/Finalisé/Envoyé/Accepté/Facturé/Refusé/Annulé) |
| Axonaut | « Devis en attente » (seul terme disponible) | Fusionne "créé" et "envoyé" — pas de distinction affirmée pour un devis créé-mais-non-envoyé |
| Sellsy | « (l')enregistrer en brouillon » | Employé pour le devis mais sans confirmation d'un statut système nommé (l'article dédié aux statuts « Brouillon » ne couvre que factures/avoirs) |
| OpenFire (Zendesk) | « brouillon » | Documenté seulement pour la génération automatique désactivée depuis une intervention ; silence pour la création manuelle standard |
| OpenFire (Odoo) | Aucun terme | Silence total sur les 10 fichiers lus |
| Obat | « Brouillon » | Fait partie d'un statut système à 5-6 valeurs (vue Kanban) mais l'état de départ est déduit par interprétation, jamais affirmé littéralement pour la création |
| Costructor | « brouillon » | Cité seulement dans des articles périphériques (impression, marges), jamais dans l'article de création lui-même — silence notable signalé explicitement par l'agent |

**Constat** : contrairement à l'intuition initiale (un état "Brouillon"
universel), seuls 2 corpus sur 8 (InterFast, Obat) affirment littéralement,
dans ou à proximité immédiate de l'article de création, un statut nommé
équivalent à "brouillon" comme état de départ robuste et intégré à un système
de statuts documenté. Les 6 autres corpus emploient le terme de façon
partielle, conditionnelle, ou pas du tout. Ce motif est classé
STANDARD_PROBABLE plutôt que STANDARD_FORT (voir section 14).

Actions immédiates convergentes pour terminer la création (hors envoi/
acceptation/signature/facturation) : sélectionner ou créer le client/société ;
construire les lignes ; vérifier/ajuster les données préremplies (adresses,
conditions) ; dans plusieurs corpus, une action de passage à un statut
"validé"/"finalisé" distincte de la simple sauvegarde attribue le numéro
définitif (InterFast, Obat, et par analogie OpenFire Zendesk avec le passage
"Bon de commande").

## 12. Vue B — comparaison entre éditeurs (par phénomène)

**Phénomène 1 — Client créable à la volée pendant la création du devis**
- CONCURRENTS : les 8 corpus, indépendamment.
- VARIANTES : mécanisme intégré au menu déroulant de sélection (Vertuoza,
  OpenFire les deux, Sellsy, Costructor) vs bouton dédié dans le formulaire
  (InterFast, Axonaut, Obat).
- INCONNUS : aucun corpus ne dit explicitement ce qui se passe si l'on tente
  d'enregistrer/finaliser un devis sans aucun client sélectionné (silence
  quasi unanime, sauf Obat qui affirme le client requis "à la finalisation").
- SOURCES : voir tableau §7.

**Phénomène 2 — Catalogue alimentable depuis le devis lui-même (aller-retour)**
- CONCURRENTS : les 8 corpus documentent la création inline d'un élément
  catalogue pendant la création du devis ; Vertuoza et Costructor documentent
  en plus le sens inverse explicite (enregistrer une ligne du devis comme
  nouvel élément de bibliothèque).
- VARIANTES : OpenFire (Odoo) est seul à documenter une contrainte amont
  (catégorie obligatoire à la création de l'article) qui bloque ensuite la
  validation du devis si la marge est insuffisante.
- SOURCES : voir tableau §7 et §9.

**Phénomène 3 — Duplication/variante/révision d'un devis existant comme mode de création**
- CONCURRENTS : Vertuoza (bouton, contenu non détaillé), InterFast
  (duplication + variante distincte), Axonaut (duplication), Sellsy (copie),
  Obat (variante, contenu intégralement repris), Costructor (révision +
  recréation + avenant).
- VARIANTES : InterFast exclut explicitement les conditions de paiement/RIB
  de la duplication ; Obat au contraire reprend "l'intégralité du contenu,
  pas de ressaisie" pour ses variantes.
- INCONNUS : les deux corpus OpenFire sont muets sur ce mécanisme dans le
  périmètre lu.
- SOURCES : voir tableau §7.

**Phénomène 4 — Modèle de devis préremplissant tout ou partie du contenu**
- CONCURRENTS : InterFast, OpenFire (les deux, avec la particularité Odoo
  que sélectionner un modèle après avoir saisi des lignes manuellement les
  efface et les remplace), Costructor.
- VARIANTES : Sellsy documente explicitement que son "modèle de document"
  NE contient PAS de lignes (seulement mise en page/tarif/mentions/TVA) —
  contre-exemple documenté, pas un silence.
- INCONNUS : Vertuoza et Obat ne disposent pas, dans le vocabulaire du corpus
  lu, d'un objet "modèle de contenu de devis" distinct du rendu PDF/de la
  bibliothèque.
- SOURCES : voir tableau §7 et §9.

**Phénomène 5 — Absence documentée de ligne libre hors catalogue**
- CONCURRENTS concernés par le silence : Axonaut, OpenFire (les deux corpus).
- CONTRASTE : Vertuoza, InterFast, Sellsy, Costructor documentent
  explicitement une ligne de texte libre sans entité catalogue.
- INCONNUS : silence documentaire chez 3 corpus sur 8, à ne pas interpréter
  comme absence fonctionnelle certaine.
- SOURCES : voir tableau §9.

**Phénomène 6 — Génération assistée du contenu (IA, vocal)**
- CONCURRENTS : Costructor (devis IA à partir de prompt/pièce jointe/dictée,
  très documenté), InterFast (import de PDF/anciens devis via IA), Obat
  (assistant devis vocal, mécanisme interne non documenté dans le corpus
  fermé).
- VARIANTES : Costructor documente explicitement que le client/chantier ne
  sont PAS préremplis automatiquement par l'IA s'ils sont absents du prompt
  — contrainte négative documentée, pas un silence.
- SOURCES : ventes/comment-creer-un-devis-ia-9jz7n7.md (Costructor) ;
  finances/import-des-devis-factures-de-mon-ancien-logiciel-avec-l-ia.md
  (InterFast).

**Phénomène 7 — Opportunité CRM comme point d'entrée distinct**
- CONCURRENTS : Vertuoza et OpenFire (Odoo) uniquement, tous deux avec CRM
  intégré.
- VARIANTES : OpenFire (Odoo) documente ce point d'entrée comme
  fonctionnellement distinct de l'entrée directe (préremplit le client,
  lie l'opportunité, reprend les données marketing) ; Vertuoza documente un
  préremplissage similaire mais moins détaillé.
- SOURCES : crm/opportunites.md (Vertuoza) ;
  documentation_2/knowsystem/creer-un-devis-depuis-une-opportunite-128.md
  (OpenFire Odoo).

## 13. Contrat fonctionnel observé de création du devis

| Capacité observée | Éditeurs qui la documentent | Variantes | Conditions/dépendances | Niveau de confiance factuelle |
|---|---|---|---|---|
| Créer un client pendant la création du devis | 8/8 | Menu déroulant vs bouton dédié | Aucune précondition documentée | Élevé (8 sources indépendantes) |
| Ajouter un élément catalogue à la volée (créer un produit/ouvrage sans quitter le devis) | 8/8 | Fenêtre dédiée vs pop-up inline | OpenFire (Odoo) : catégorie obligatoire en amont | Élevé |
| Préremplir automatiquement les données du client (adresse a minima) | 5/8 (Vertuoza, Axonaut, Sellsy, OpenFire×2) | Champ modifiable partout où documenté | Sélection préalable du client | Élevé sur le principe, mode technique non documenté |
| Créer un devis depuis une fiche client | 5/8 (InterFast, Sellsy, OpenFire Zendesk implicite, Axonaut, Costructor indirect) | Formulaire résultant rarement redétaillé | Fiche client existante | Moyen (existence du bouton documentée, contenu du formulaire résultant rarement redécrit) |
| Créer un devis depuis un chantier/projet/affaire | 3/8 (InterFast, Costructor, OpenFire Zendesk via contrat d'entretien) | Chantier créable inline chez InterFast et Costructor | Chantier existant ou créé à la volée | Moyen |
| Dupliquer un devis existant / créer une variante | 6/8 | Contenu intégralement repris (Obat) vs partiellement (InterFast exclut conditions de paiement) | Devis source existant | Moyen-élevé |
| Partir d'un modèle de devis préremplissant les lignes | 4/8 (InterFast, OpenFire×2, Costructor) | Sellsy documente l'exclusion explicite des lignes | Modèle créé au préalable | Moyen |
| Ligne libre sans catalogue | 4/8 (Vertuoza, InterFast, Sellsy, Costructor) | — | Aucune | Moyen (silence chez 3 corpus à ne pas lire comme absence) |
| État initial nommé "brouillon"-équivalent, affirmé dans/près de l'article de création | 2/8 clairement (InterFast, Obat) ; 4/8 partiellement | Vocabulaire non normalisé : Draft, Brouillon, "en attente" | — | Faible-moyen |
| Génération assistée du contenu par IA ou reconnaissance de document | 2/8 (Costructor, InterFast) | Prompt/pièce jointe/dictée (Costructor) vs import PDF reconnu (InterFast) | — | Moyen (2 sources, mécanisme bien détaillé chez les deux) |
| Devis créé depuis une opportunité CRM, distinct de l'entrée directe | 2/8 (Vertuoza, OpenFire Odoo) | — | Opportunité existante | Moyen |

## 14. Standards probables / variantes / inconnus (classification des motifs)

- **STANDARD_FORT** : création d'un client à la volée pendant la création du
  devis (8/8, aucun contre-exemple, formulations indépendantes et directes) ;
  ajout d'un élément catalogue à la volée pendant la création du devis (8/8,
  même constat).
- **STANDARD_PROBABLE** : préremplissage de l'adresse client (5/8, aucun
  contre-exemple mais 3 silences) ; existence d'un mécanisme de
  duplication/variante d'un devis existant (6/8, 2 silences chez le même
  éditeur — OpenFire, les deux corpus) ; existence d'un état "brouillon"
  ou équivalent avant finalisation (documenté à des degrés très inégaux, mais
  jamais contredit explicitement).
- **VARIANTE_DE_MARCHE** : présence ou non d'une ligne libre hors catalogue
  (4 oui francs, 3 silences chez Axonaut et OpenFire, situation qui pourrait
  refléter un vrai choix produit plutôt qu'un simple angle mort
  documentaire, vu la cohérence interne de ces 3 corpus sur ce point précis) ;
  modèle de devis incluant ou excluant les lignes (Sellsy exclut
  explicitement, 4 autres incluent).
- **SPECIFICITE_EDITEUR** : opportunité CRM comme point d'entrée (2/8,
  seulement chez les éditeurs à CRM intégré) ; génération IA du contenu
  (2/8, Costructor et InterFast) ; assistant vocal (Obat seul, mécanisme non
  détaillé) ; cascade contrat d'entretien → devis (OpenFire Zendesk seul dans
  ce périmètre).
- **NON_DETERMINE** : mode technique (copié/référencé/généré) de la quasi-
  totalité des données héritées, sauf 3 exceptions ponctuelles (Obat, OpenFire
  Zendesk, Costructor) ; caractère strictement bloquant ou non de l'absence
  de client à l'enregistrement (silence quasi général, 3 exceptions
  affirmatives) ; existence d'un minimum de lignes requis pour finaliser un
  devis (silence total sur les 8 corpus).

Rappel de discipline : ces labels qualifient la convergence documentaire, pas
une recommandation produit. Fréquence documentaire ≠ importance fonctionnelle ;
silence documentaire ≠ absence fonctionnelle.

## 15. Questions SUPORDO devenues instruisibles

**Faut-il exiger un client avant de pouvoir créer/enregistrer un devis ?**
- FAITS DISPONIBLES : 8/8 corpus documentent la création de client à la
  volée ; seuls 3/8 (InterFast mobile, OpenFire Odoo, Obat à la finalisation)
  affirment explicitement un caractère requis, et seulement à un stade
  précis (mobile, "premier temps", finalisation).
- VARIANTES OBSERVÉES : "requis à la finalisation mais pas à l'enregistrement
  en brouillon" (Obat) vs "requis dès le formulaire mobile" (InterFast) vs
  silence total sur le caractère bloquant (5/8).
- INFORMATION MANQUANTE : aucun corpus ne documente le message d'erreur ou le
  comportement exact d'un devis sans client à l'enregistrement.
- TERRAIN NÉCESSAIRE : non — un test direct sur les logiciels concurrents ou
  une décision produit assumée peuvent trancher sans enquête terrain
  supplémentaire.

**Faut-il permettre la création de client inline pendant la création du devis ?**
- FAITS DISPONIBLES : capacité STANDARD_FORT, 8/8 corpus, mécanisme mature et
  documenté avec précision partout.
- VARIANTES OBSERVÉES : menu déroulant intégré vs bouton dédié — détail
  d'implémentation, pas de divergence fonctionnelle.
- INFORMATION MANQUANTE : aucune — le corpus est unanime et suffisant.
- TERRAIN NÉCESSAIRE : non.

**Faut-il exiger un projet/chantier avant de créer un devis, ou autoriser un devis hors chantier ?**
- FAITS DISPONIBLES : seulement 3/8 corpus documentent une relation directe
  chantier→devis (InterFast, Costructor : facultatif + créable inline ;
  OpenFire Zendesk : via contrat d'entretien) ; Vertuoza documente la
  direction inverse (le devis précède et engendre le chantier).
- VARIANTES OBSERVÉES : chantier facultatif et créable à la volée (InterFast,
  Costructor) vs chantier comme résultat du devis accepté (Vertuoza) vs
  silence (Axonaut, Sellsy, Obat, OpenFire Odoo).
- INFORMATION MANQUANTE : le corpus ne permet pas de savoir si un devis
  "orphelin" (sans chantier) est un cas normal ou marginal dans l'usage réel.
- TERRAIN NÉCESSAIRE : oui — la variance documentaire est trop large et trop
  silencieuse pour trancher sans observer l'usage réel des artisans.

**Faut-il permettre des lignes libres hors catalogue ?**
- FAITS DISPONIBLES : 4/8 corpus documentent une ligne libre explicite ;
  3/8 (Axonaut, OpenFire×2) n'en documentent aucune dans le périmètre lu.
- VARIANTES OBSERVÉES : silence cohérent et répété chez 3 corpus (potentiel
  choix produit assumé plutôt qu'angle mort documentaire).
- INFORMATION MANQUANTE : le corpus ne permet pas de distinguer un choix
  produit délibéré (toujours passer par un article, même créé à la volée)
  d'un simple manque de documentation.
- TERRAIN NÉCESSAIRE : oui pour confirmer l'intention produit chez Axonaut/
  OpenFire ; non pour la décision SUPORDO elle-même si le corpus déjà
  disponible (4/8 le permettent) est jugé suffisant pour trancher.

**Quel état initial utiliser ?**
- FAITS DISPONIBLES : vocabulaire non normalisé et preuve inégale (2/8
  robuste, 4/8 partielle, 2/8 quasi silencieuse).
- VARIANTES OBSERVÉES : Draft (Vertuoza), Brouillon (InterFast, Obat,
  Costructor en périphérie), fusion créé+envoyé (Axonaut), silence (OpenFire
  Odoo).
- INFORMATION MANQUANTE : le corpus ne permet pas de savoir si l'absence de
  mention chez OpenFire (Odoo) et la fusion chez Axonaut reflètent une
  absence réelle d'état intermédiaire ou un simple silence éditorial.
- TERRAIN NÉCESSAIRE : non — le motif majoritaire (un état non finalisé avant
  numérotation définitive) est assez robuste pour instruire une décision
  SUPORDO sans enquête terrain supplémentaire.

**Faut-il permettre la duplication/création de variantes d'un devis existant ?**
- FAITS DISPONIBLES : 6/8 corpus documentent un mécanisme, avec des
  granularités de reprise différentes.
- VARIANTES OBSERVÉES : reprise totale (Obat) vs reprise partielle excluant
  les conditions de paiement (InterFast).
- INFORMATION MANQUANTE : aucune donnée sur la fréquence d'usage réelle de ce
  mécanisme.
- TERRAIN NÉCESSAIRE : non pour la décision de principe (le corpus suffit à
  motiver l'existence de la capacité) ; oui seulement pour calibrer finement
  ce qui doit être exclu de la reprise.

## 16. Questions terrain résiduelles

- Dans une vraie entreprise, un devis sans client rattaché a-t-il un usage
  réel (brouillon de travail, chiffrage exploratoire), ou le corpus documente-
  t-il une possibilité technique jamais utilisée en pratique ?
- Les artisans qui utilisent des logiciels sans ligne libre documentée
  (profil Axonaut/OpenFire) contournent-ils systématiquement en créant un
  article catalogue "au vol", ou est-ce vécu comme une friction ?
- Le chantier est-il, dans l'usage réel InterFast/Costructor, très souvent
  créé après le devis (comme documenté chez Vertuoza) malgré la possibilité
  technique de le créer avant/pendant ?
- Le mécanisme de devis généré par IA (Costructor, et import via IA chez
  InterFast) est-il perçu comme fiable par les artisans, ou nécessite-t-il
  systématiquement une relecture manuelle intégrale avant envoi ?
- Un devis est-il très souvent créé par duplication d'un ancien devis plutôt
  que "from scratch", chez les éditeurs qui documentent ce mécanisme
  richement (InterFast, Obat, Costructor) ?
- Le double niveau contact/société (Vertuoza, Sellsy, OpenFire) apporte-t-il
  une vraie valeur perçue par l'utilisateur final, ou l'entité unique
  "client" (Axonaut, Obat, Costructor) est-elle vécue comme suffisante et
  plus simple ?

## 17. Rendement par concurrent

| Corpus | Fichiers examinés | Nouveaux éléments structurants | Confirmations d'éléments déjà observés (pilotes précédents) | Apport nul constaté |
|---|---:|---|---|---|
| Vertuoza | 19 (14 exploités) | Dissociation contact/société avec héritage documenté ; ligne "poste libre" copiable entre devis | Recoupe le pilote onboarding (silence sur premier devis Vertuoza, désormais comblé) | 5 fichiers hors périmètre (cycle de vie, permissions) |
| InterFast | 19 (14 exploités) | Multiplicité des points d'entrée (client, chantier, intervention) ; mécanisme de variante distinct de la duplication ; import IA de documents PDF | Confirme le motif mode-test/numérotation-définitive du pilote onboarding | 5 fichiers hors périmètre (avenant, personnalisation PDF, import client global) |
| Axonaut | 14 (7 exploités) | Aucun mécanisme de ligne libre documenté (silence structurant) | Confirme la dépendance client↔devis "créable à la volée" déjà notée au pilote onboarding | 7 fichiers hors périmètre (modification, catégorisation, transformation en facture) |
| Sellsy | 22 (15 exploités) | Confirmation explicite du mécanisme "document de vente" générique (devis=facture même écran) ; restriction documentée prospect→devis seul | Premier apport direct sur ce corpus pour la question devis | 7 fichiers hors périmètre (statuts factures, mode conforme, CGV) |
| OpenFire (Zendesk) | 15 (10 exploités) | Cascade contrat d'entretien → devis ; génération automatique/manuelle depuis intervention ; 13 données préremplies distinctes recensées | Confirme et enrichit fortement le pilote onboarding (seul créateur de devis identifié chez OpenFire jusqu'ici) | 5 fichiers hors périmètre (fusion contacts, import Excel, config RDV) |
| OpenFire (Odoo) | 10 (10 exploités) | Point d'entrée opportunité→devis distinct et détaillé ; comportement de remplacement des lignes par un modèle sélectionné après coup | Premier corpus Odoo exploité sur ce sujet précis (absent des deux pilotes précédents) | Aucun fichier sans apport |
| Obat | 19 (12 exploités) | Mécanisme de variante avec reprise intégrale sans ressaisie ; prix de bibliothèque explicitement snapshotté | Confirme le mode SNAPSHOTTÉ déjà identifié au pilote propagation (§4.8) | 7 fichiers hors périmètre (planning chantier, portail client, assistant vocal non détaillé) |
| Costructor | 15 (12 exploités) | Devis généré par IA (prompt/pièce jointe/dictée) ; import DPGF/DQE/PDF ; système de révisions distinct de la duplication | Confirme l'absence de séquence onboarding déjà notée (collection de fiches indépendantes) | 3 fichiers hors périmètre (signature, portail chantier, affichage cosmétique) |

Aucun corpus n'a d'apport nul sur l'ensemble de sa liste ; chaque éditeur
contribue au moins un élément structurant propre. Rendement descriptif,
aucun score.

## 18. Ce que l'analyse permet réellement de savoir

- Reconstruire, pour 8 corpus indépendants couvrant les 4 familles de marché
  demandées, une séquence de naissance du devis au moins partiellement
  documentée de bout en bout, avec citations exactes et sources vérifiables.
- Établir avec un niveau de preuve élevé (8/8, formulations indépendantes)
  que la création de client à la volée et l'ajout de catalogue à la volée
  pendant la création du devis sont deux capacités quasi universelles du
  marché observé.
- Documenter, avec preuve directe, plusieurs mécanismes alternatifs de
  création (duplication, variante, révision, modèle, import de fichier,
  génération par IA) et leur répartition inégale entre éditeurs.
- Identifier un contraste net et reproductible entre les éditeurs qui
  documentent un état "brouillon" robuste et intégré à un système de statuts
  (InterFast, Obat) et ceux qui n'en documentent aucun ou de façon fragmentaire
  (OpenFire Odoo, Costructor à l'article de création lui-même).
- Isoler un silence cohérent et potentiellement significatif sur la ligne
  libre hors catalogue chez 3 corpus (Axonaut, OpenFire×2), à traiter comme
  hypothèse de variante de marché plutôt que fait établi.
- Séparer clairement contact/client/prospect/société selon les éditeurs,
  révélant une divergence structurelle de modèle de données observable
  (hiérarchie à deux niveaux vs entité unique) qui a une incidence directe
  sur la façon dont un devis peut être rattaché à un tiers.

## 19. Ce qu'elle ne permet PAS encore de savoir

- Le mode technique exact (copié/référencé/généré) de la quasi-totalité des
  données héritées — silence structurel du corpus documentaire, déjà
  identifié par le pilote propagation, confirmé ici sur le sous-domaine
  spécifique de la création du devis.
- Si l'absence de ligne libre chez Axonaut et OpenFire (les deux corpus)
  reflète un choix produit assumé ou un simple silence de documentation.
- Le comportement exact (blocage, avertissement, autorisation silencieuse)
  d'une tentative d'enregistrement ou de finalisation d'un devis sans client
  sélectionné, sur aucun des 8 corpus.
- L'existence ou non d'un minimum de contenu (au moins une ligne, un montant
  non nul) requis pour finaliser un devis — silence total sur les 8 corpus.
- La fréquence réelle d'usage de chaque mécanisme documenté (duplication,
  modèle, ligne libre, IA) dans la pratique des artisans — la mission ne
  documente que l'existence de la capacité, jamais son taux d'adoption.
- Si le champ `moment_parcours = devis` du schéma LIGHT, non grepé
  mécaniquement pour cette mission (écart assumé, §3.2), aurait révélé des
  candidats supplémentaires significatifs — limite méthodologique à
  documenter pour un futur run canonique sur ce sujet.
- Le comportement précis de l'écran de création principal (modal, page
  dédiée, comportement de validation) pour 7 corpus sur 8 — seule la liste
  des champs et leur ordre éditorial est disponible, jamais la mécanique
  d'interface elle-même.

## 20. Verdict

**Cette analyse permet-elle réellement de répondre à : « qu'est-ce qui doit
exister avant quoi, depuis où et avec quelles données, pour créer un
devis ? »**

**EXPLOITABLE.**

Justification stricte au regard du critère qualitatif de la commande : 8
corpus indépendants, couvrant les 4 familles de marché imposées avec
corroboration systématique (2 éditeurs par famille), permettent de
reconstruire concrètement les préconditions (client créable à la volée dans
100 % des corpus, catalogue créable à la volée dans 100 % des corpus), les
points d'entrée (au moins deux points d'entrée documentés pour 5 corpus sur
8), et les mécanismes de création (ligne libre, catalogue, modèle,
duplication, import, génération IA), avec suffisamment de matière convergente
pour instruire directement 4 des 6 questions SUPORDO listées en section 15
sans enquête terrain supplémentaire.

Deux questions structurantes (dépendance chantier→devis, présence d'une
ligne libre hors catalogue chez 3 éditeurs) restent partiellement
non tranchées par le corpus documentaire seul et nécessitent une
corroboration terrain — c'est la raison pour laquelle le verdict n'est pas
qualifié de exhaustif, mais reste EXPLOITABLE au sens du critère de la
mission : les briques principales sont robustes, les questions encore
ouvertes sont identifiées et nommées, pas dissimulées.

Même ce verdict acquis, 3B n'est pas lancée.

DEVIS_3A_TERMINE — EXPLOITABLE — STOP
