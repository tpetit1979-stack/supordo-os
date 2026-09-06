---
source: https://support.openfire.fr/hc/fr/articles/19076110273436-Cr%C3%A9er-un-produit
categorie: Utiliser OpenFire
titre: Créer un produit
date_recuperation: 2026-09-05
---

# Créer un produit

La liste des produits regroupe l’ensemble de vos produits (au sens produit stockable) et de vos services.

Cette page vous guide sur la création et la gestion de vos produits dans OpenFire.

Cet article contient les sections suivantes :

- [Comprendre les champs du formulaire](#h_01JPQPCNZE5FC8SDRY020PENRD)
  - [Entête du formulaire](#h_01JPQPCNZEGNNGE6WTA90K14A2)
  - [Onglet “Informations générales”](#h_01JPQPCNZEP980GGVSQ9K7EKJ8)
  - [Onglet "Vente"](#h_01JPQPCNZENNTG4KWGE9QKV66H)
  - [Onglet "Achat"](#h_01JPQPCNZE03QM86AH6DEC6G0S)
  - [Onglet “Inventaire”](#h_01JPQPCNZF9GT7RG5M5BHARFKJ)
  - [Onglet “Comptabilité”](#h_01JPQPCNZFPRZM2AMH3YVN6E79)
- [Actions et navigations associées](#h_01JPQPCNZF2N3MA2BJKN337TQN)
  - [Actions disponibles](#h_01JPQPCNZFD9D5K2J5ZGFJ25MQ)
  - [Smart Boutons](#h_01JPQPCNZFAGP1E2FFD41CNM9G)
- [Pour aller plus loin](#h_01JPQPCNZFK7ZK0EHMNE7DJRRH)

# Comprendre les champs du formulaire

Chemin d’accès :

- Pour le plan basique : OpenFire > Ventes > Mes produits
- Pour les autres plans : Ventes > Produits > Produits.

Le formulaire de création d’un article est composé de différents onglets repris ci-dessous.

## Entête du formulaire

Au niveau de l’entête du formulaire, vous retrouvez les différents champs suivants :

**Nom du produit** : désignation commerciale qui apparaîtra sur les devis.

**Image :** Cet espace permet d'insérer la photo de votre choix, en cliquant sur le stylo “modifier” de l’appareil photo :

![](https://support.openfire.fr/hc/article_attachments/19097641608476)

💡Note : Plusieurs médias (photos, notices, etc.) peuvent être associés à votre produit, et pourront être utilisés par défaut dans vos devis.
**Article obsolète** : Un article est marqué comme obsolète lorsque son ou ses fournisseurs ne le vendent plus. Il ne peut donc plus être acheté. S’il vous en reste en stock, ce produit peut en revanche encore être vendu.

**Est un kit** : permet d’identifier les produits de type “kit”, c’est à dire les produits eux-mêmes constitués d’une liste de composants

**📓**Pour aller plus loin → [Créer un kit](https://support.openfire.fr/hc/fr/articles/19076134763548)

**Étiquettes **: Vous pouvez créer et appliquer les étiquettes de votre choix dans ce champ.

**Connecté **: permet d’identifier les produits issus du tarif centralisé. Le tarif centralisé est un service OpenFire qui vous permet d’accéder aux tarifs d’un ensemble de fournisseurs référencés.

**📓**Pour aller plus loin → [Accéder aux tarifs centralisés](https://support.openfire.fr/hc/fr/articles/17228367601180)

## Onglet “Informations générales”

### Informations distributeur

Cette rubrique propose des champs de qualification du produit et des éléments de prix.

#### Qualification de l’article

**Type de produit** : 3 types sont disponibles, permettant de dissocier notamment vos produit de vos prestations :

- **Produit stockable **: produit pour lequel les quantités en stock sont gérées (exemple : un poêle à granulés)
- **Service **: produit de type prestation de service / main d'œuvre (exemple : un forfait de maintenance)
- **Consommable **: produit pour lequel on ne suit pas le stock (exemple : de la visserie)

**Catégorie **: Famille à laquelle se rattache le produit. La catégorie est un élément essentiel du produit, utilisée notamment pour :

- Les statistiques
- Les imputations comptables
- Le calcul des conditions tarifaires
- Le choix des données techniques à compléter
- L'imputation des normes

**Marque : **

- **Pour un produit négoce** : la marque est celle communiquée par le fabricant.
- **Pour une prestation de service** : la marque sera la plupart du temps celle de votre propre entreprise.
💡Note : La marque est la valeur de référence pour la gestion du tarif centralisé. Les imports et les mises à jour de ces tarifs sont gérées depuis le menu de marques. 
**📓**Pour aller plus loin → [Marques et fournisseurs](https://support.openfire.fr/hc/fr/articles/19097519042332)

**Modèle : **correspond au modèle identifié dans le tarif du fournisseur. Dans le cadre du tarif centralisé, ce modèle peut  être transmis directement par le fournisseur. Plusieurs produits peuvent correspondre à un même modèle ; cela permet notamment de gérer de façon simplifiée les différentes déclinaisons d’un même appareil.

**Référence interne **: il s’agit de votre propre référence pour identifier le produit dans votre liste. La référence interne doit être unique par marque.
💡Note : Les produits importés depuis le tarif centralisé ont par défaut comme référence interne la référence transmise par le fabricant. Il ne faut alors pas modifier cette référence pour garder le lien avec le tarif du fabricant. 
#### Eléments de prix

**Coût **: correspond au prix de revient de l’article.

Par défaut, ce coût est défini manuellement par l’utilisateur.

Il peut également être valorisé par application des conditions commerciales définies dans la marque du produit.

Il est notamment utilisé pour le calcul de la marge dans les devis.
💡Note : Ce coût peut également servir à valoriser les stocks du produit en question. Dans ce cas, une méthode de coût adaptée doit être définie au niveau de chaque famille de produit. Une autre valeur de coût, appelé le “coût théorique”, peut alors être utilisée. 
**📓**Pour aller plus loin : [Coût d'inventaire, Coût théorique et méthode de coût Coût d'inventaire, Coût théorique et méthode de coût](https://support.openfire.fr/hc/fr/articles/19095774098844)

**Prix de vente** : correspond au prix de vente HT de référence du produit. C’est ce prix qui sera repris par défaut dans vos devis.

Par défaut, ce prix est défini manuellement par l’utilisateur.

Il peut également être valorisé par application des conditions commerciales définies dans la marque du produit.
💡Note : Le prix de vente peut être défini comme un prix TTC, si la taxe associée est configurée comme “incluse dans le prix”.
**📓**Pour aller plus loin → [Configuration des taxes](https://support.openfire.fr/hc/fr/articles/19084567800348)

**Marge **: calculée automatiquement selon le coût et le prix de vente.

**Taxe à la vente :** cette taxe correspond à la taxe qui sera utilisée par défaut pour le produit dans vos devis et vos factures client.

Deux cas de figure sont possibles :

1/ Si la taxe du produit est toujours la même, elle peut être forcée au niveau de l’article ;
🧑‍🏫Exemple : C’est le cas notamment des articles de combustible bois ou granulés vendus en TVA 10% : 
![](https://support.openfire.fr/hc/article_attachments/19097641609116)

2/ Si la taxe du produit dépend du régime fiscal applicable pour le client, une TVA dite de base peut-être appliquée. C’est le régime de TVA du client, du devis ou de la facture qui sera ainsi appliquée.

🧑‍🏫Exemple : C’est le cas notamment des appareils de chauffage au bois : 

Si vendus et installé dans une maison de plus de 2 ans : une TVA à 5,5% s’applique

Si vendus et installé dans une maison neuve : une TVA à 20% s’applique

Dans l’article on positionne ainsi une TVA de base, neutre :

**![](https://support.openfire.fr/hc/article_attachments/19097641621148)**

**Remise interdite** : si cochée, aucune remise ne sera acceptée pour cet article dans le contexte du devis.

### Informations fournisseur

Cette rubrique propose des champs relatifs aux informations provenant du fournisseur du produit. Ces champs sont notamment pertinents dans le contexte d’une activité de négoce.

**Date du tarif **: correspond à la date de dernière mise à jour du tarif par le fabricant. Une date trop lointaine peut indiquer un retard dans la mise à jour de vos tarifs.

Dans le contexte d’un produit importé du tarif centralisé, cette date est mise à jour automatiquement.

**Prix d’achat **: correspond au prix d’achat du produit chez votre fournisseur principal.

Par défaut, ce prix est défini manuellement par l’utilisateur. Il peut également être valorisé par application des conditions commerciales définies dans la marque du produit.

**Prix public HT** : correspond au prix public HT préconisé par le fournisseur du produit. Par défaut, ce prix est défini manuellement par l’utilisateur. Il peut également être valorisé directement par le fabricant dans le contexte d’un produit importé depuis le tarif centralisé.

**Remise **: calculée automatiquement selon le Prix public HT et le prix d’achat. Cette remise correspond donc à votre remise commerciale pour ce produit.

### Informations avancées

**Unité de mesure de vente**: permet de définir l'unité utilisée pour la vente d'un produit.

**Unité de mesure d'achat** : permet de définir l'unité utilisée pour l'achat d'un produit auprès d'un fournisseur.

L’unité de mesure utilisée par défaut est l’unité.

💡Note : La possibilité de distinguer ces deux unités est particulièrement
    utile
    si vous achetez un produit dans une unité différente de celle dans laquelle
    vous
    le vendez. Par exemple, vous pouvez acheter un produit en bobine de 30 mètres
    linéaires (30ML) et le vendre
    au mètre (m).

Pour les produits issus du tarif centralisé, les unités sont proposées
    directement par le fabricant.

Les deux unités (vente et achat) doivent appartenir à la même catégorie.
    Vous
    ne pouvez pas acheter un produit en lots de 12 (catégorie 'Unité') et le
    revendre
    au mètre (catégorie 'Longueur/Distance').

  🚨Avertissement :

Il est important de noter que le choix des unités de mesure peut avoir un impact sur la gestion des stocks et la comptabilité. Il est donc important de choisir les unités appropriées pour chaque produit.

Une fois qu'un produit a été utilisé dans un devis ou une commande, vous ne pouvez plus en modifier l'unité de mesure. La seule solution est donc de créer un nouveau produit avec la nouvelle unité à utiliser, et d'archiver le précédent produit dont l'unité ne correspond plus si nécessaire.

### Divers

**Peut être vendu **: si cochée, le produit sera proposé à la saisie dans les devis et factures client

**Peut être acheté **: si cochée, le produit sera proposé à la saisie dans les commandes et les factures fournisseur

**Basé sur le prix net **: si cochée, les prix de cet article sont basés sur un prix d’achat fixe fourni par le fournisseur du produit. Ce champ est un champ calculé lors des imports via le tarif centralisé

**Notes internes : **correspond aux informations diverses de ce produit, à usage interne uniquement. Ces informations ne seront pas visibles par le client.

## Onglet "Vente"

### Politique de facturation

**Politique de facturation : **correspond aux règles qui seront appliquées lorsque ce produit sera facturé depuis un bon de commande client.

Deux politiques de facturation distinctes existent :

- ***Quantités commandées*** : à la facturation de la commande client, la quantité facturée pour le produit correspondra à la quantité vendue au client. Le logiciel vérifiera d’abord si une ou plusieurs quantité(s) du produit n’ont pas déjà été facturée(s), afin d’éviter les doublons de facturation. Dans ce scénario, la facturation avant la livraison des produits est donc possible.
- ***Quantités livrées** :* à la facturation de la commande client, la quantité facturée pour le produit correspondra à la quantité déjà livrée au client. Le logiciel vérifiera d’abord si une ou plusieurs quantité(s) du produit n’ont pas déjà été facturée(s) , afin d’éviter les doublons de facturation.

🧑‍🏫Exemple : J’ai vendu à mon client 10 sacs de granulés, je lui en ai déjà livrés 5, et facturé 2. 

- Si mon produit est en politique de facturation sur “quantités commandées”, alors ma prochaine facture sera de 8 sacs (10 sacs commandés - 2 sacs déjà facturés)
- Si mon produit est en politique de facturation sur “quantités livrées”, alors ma prochaine facture sera de 3 sacs (5 sacs livrés - 2 sacs déjà facturés)

**📓**Pour aller plus loin → [Politique de facturation](https://support.openfire.fr/hc/fr/articles/19091247558940)

#### Structure de prix

Les différents champs listés dans cette rubrique permettent de définir certains attributs de prix qui pourront être utilisés pour la construction du coût théorique ou du prix de vente du produit. Ces attributs pourront notamment être utilisés dans la configuration des conditions commerciales au niveau de la marque du produit.

![](https://support.openfire.fr/hc/article_attachments/19097641623324)
🧑‍🏫Exemple : Le prix de vente de mon produit peut être calculé, au niveau de la marque, en additionnant au prix d’achat du produit un coût de transport sur achat et d’autres frais logistiques.
**Description vente : **Cette note sera visible par défaut sur vos documents de ventes (devis, bon de commande, facture), vous pourrez toujours la modifier sur votre devis.

**Norme **: permet d’associer une norme à votre produit. Cette norme pourra être reprise dans vos documents de vente afin d’informer votre client ou à des fins réglementaires. C’est notamment le cas lorsque la mention de la norme est obligatoire sur votre facture afin de permettre à votre client de bénéficier d’une subvention.

**Description de la norme **: A chaque norme, un texte descriptif peut être associé. Il sera repris ici pour info, et le sera également sur vos devis.

**📓**Pour aller plus loin → [Normes de produit](https://support.openfire.fr/hc/fr/articles/19091185034140)

**Description du fabricant : **Généralement, ce champ est plutôt utilisé par les fabricants pour ajouter des informations diverses relatives à leurs produits. Une option vous permet d’afficher cette description sur vos devis.

**URL : **ce champ vous permet de saisir le lien vers une page web de description du produit. Il peut s’agit par exemple de la page du site web de votre fournisseur

## Onglet "Achat"

Pour chacun de vos produits, un ou plusieurs fournisseurs peuvent être définis.

Par défaut, le fournisseur associé à la marque sélectionnée pour le produit est présélectionné dans la liste proposée.

![](https://support.openfire.fr/hc/article_attachments/19097641624860)

**Taxes fournisseurs**

Cette taxe correspond à la taxe qui sera utilisée par défaut pour le produit dans vos commandes et vos factures fournisseurs.

**Politique de contrôle : **ce paramètre définit la règle qui est appliquée pour le produit lorsque l’utilisateur génère la facture du fournisseur depuis la commande fournisseur d’origine.

Deux politiques de facturation distinctes existent :

- ***Sur base des quantités commandées*** : la quantité facturée pour le produit correspondra à la quantité achetée au fournisseur. Le logiciel vérifiera d’abord si une ou plusieurs quantité(s) du produit n’ont pas déjà été facturée(s), afin d’éviter les doublons de facturation.
- ***Sur base des quantités reçues *****: **la quantité facturée pour le produit correspondra à la quantité déjà reçue. Le logiciel vérifiera d’abord si une ou plusieurs quantité(s) du produit n’ont pas déjà été facturée(s) , afin d’éviter les doublons de facturation.

**Description des achats : **Cette note sera visible par défaut sur vos documents d’achat (demande de prix, bon de commande, facture) ; vous pourrez toujours la modifier sur chaque document

## Onglet “Inventaire”

[à venir]

## Onglet “Comptabilité”

[à venir]

## Articles liés

**Produits optionnels **: Permet de faire une proposition de produit ou de service optionnel, chaque fois que le produit en question est saisi dans un devis.

# Actions et navigations associées

## Actions disponibles

Depuis le formulaire du produit, les actions suivantes sont disponibles :

![](https://support.openfire.fr/hc/article_attachments/19097641625756)

**Imprimer les étiquettes : **cette action permet d’éditer une étiquette produit. Un certain nombre de format par défaut vous sont proposés :

![](https://support.openfire.fr/hc/article_attachments/19097656065564)

**Réapprovisionner : **cette action vous permet de réaliser une demande de réassort pour le produit :

![](https://support.openfire.fr/hc/article_attachments/19097641628316)

**Appliquer les règles : **cette action permet de recalculer les éléments de prix de votre produit par application des conditions commerciales définies dans la marque du produit.

## Smart boutons

En haut à droite de votre fiche produit, les smart boutons suivants sont disponibles :

| ![](https://support.openfire.fr/hc/article_attachments/19097656067228) | Si ce bouton est vert, le produit peut être utilisé depuis l’application mobile. Dans le cas contraire, ce bouton est rouge. Pour passer de l’un à l’autre, il suffit de cliquer sur ce bouton. |
| --- | --- |
| ![](https://support.openfire.fr/hc/article_attachments/19097641629596) | Indique les quantités déjà vendues pour ce produit. En cliquant dessus, vous accédez aux ventes correspondantes. |
| ![](https://support.openfire.fr/hc/article_attachments/19097641630108) | Indique les quantités déjà achetées pour ce produit. En cliquant dessus, vous accédez aux achats correspondants. |
| ![](https://support.openfire.fr/hc/article_attachments/19097656068764) | Indique les mouvements de stocks d’entrées et de sorties pour ce produit. En cliquant dessus, vous accédez aux mouvements correspondants. |

# Pour aller plus loin

**📓**Pour aller plus loin → [Importer mes produits avec Open Import](https://support.openfire.fr/hc/fr/articles/18848702816924)

Mis a jour le : 22/07/2026
