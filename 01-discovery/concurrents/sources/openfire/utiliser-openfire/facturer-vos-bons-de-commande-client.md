---
source: https://support.openfire.fr/hc/fr/articles/20226881304604-Facturer-vos-bons-de-commande-client
categorie: Utiliser OpenFire
titre: Facturer vos bons de commande client
date_recuperation: 2026-09-05
---

# Facturer vos bons de commande client

![All_tick_V2.png](https://support.openfire.fr/hc/article_attachments/20226881290268)

OpenFire vous permet de facturer rapidement et simplement vos bon de commandes. Avec l’aide à la saisie OpenFire, générez vos factures d’acomptes et de soldes en vous basant sur le bon de commande précédemment édité.

Cet article contient les sections suivantes :

- [Facturer vos bons de commande client ](#h_01JQ9BFT0SVTR8XDAZMY2KM29S)

  - [Exemples de flux de facturation possibles ](#h_01JQ9BFT0S1V4NSSE4WVVRVH9M)

    - [Facturation d’une vente de produit avec prestation d’installation ](#h_01JQ9BFT0SBV30EZ37XDKS6V1Y)
    - [Facturation d’une vente de pièces détachées ](#h_01JQ9BFT0T3EKWPHR9WQHR4S2M)
    - [Facturation d’avance d’une prestation de service simple type entretien ](#h_01JQ9BFT0TWSW21S9PE700RQPN)
    - [Facturation à la réalisation d’une prestation de service simple type entretien ](#h_01JQ9BFT0TGBA1Z7AQXJH6F6FT)
    - [Facturation d’une vente de produit avec livraison différée (négoce B2B) ](#h_01JQ9BFT0TMMCRTX6G5Z09XGTQ)
  - [Identifier vos commandes facturables ](#h_01JQ9BFT0THSPX0XFN5W966H3D)
  - [Générer une facture d’acompte ](#h_01JQ9BFT0TVRGCXF5HWM80CFB8)
  - [Générer une facture de solde ](#h_01JQ9BFT0TPXQQ0XW10SX38VBX)
  - [Les cas particuliers ](#h_01JQ9BFT0TQ4NXWM9ASGCAQGTX)

    - [Les factures partielles ](#h_01JQ9BFT0TPZKE1S9YQQJH08JC)
    - [Les factures proforma ](#h_01JQ9BFT0TW5MQWNR3A6GT8WTN)

# Facturer vos bons de commande client

## Exemples de flux de facturation possibles

Selon la configuration de votre entreprise, la facturation peut se faire immédiatement après la validation de la commande, après l’expédition des articles ou en fonction d’un échéancier spécifique. OpenFire facilite ce processus en permettant de créer facilement des factures à partir des commandes éligibles, assurant ainsi un suivi clair des paiements et une gestion optimisée de la comptabilité.

Les factures sont souvent générées en brouillon afin d’en permettre la vérification. L’utilisateur peut facturer l’intégralité de la commande, facturer un pourcentage (acompte), facturer certaines lignes et/ou facturer un acompte fixe.

Il existe plusieurs processus de facturation en fonction du type de vente réalisée.

Voici quelques exemples :

### Facturation d’une vente de produit avec prestation d’installation

1. Le devis est transformé en commande.
2. Une facture d’acompte brouillon est générée et validée.
3. L’installation est réalisée.
4. Une facture de solde brouillon est générée (sur la base des quantités commandées, en déduisant les acomptes déjà facturés) et validée

### Facturation d’une vente de pièces détachées

1. Le devis est transformé en commande.
2. Une facture d’acompte brouillon est générée et validée.
3. Le client retire les pièces détachées.
4. Une facture de solde brouillon est générée (en fonction des quantités retirées) et validée.

### Facturation d’avance d’une prestation de service simple type entretien

1. Le devis est transformé en commande .
2. Une facture brouillon est générée et validée immédiatement après la commande.

### Facturation à la réalisation d’une prestation de service simple type entretien

1. Le devis est transformé en commande .
2. L’intervention est réalisée par le technicien.
3. Une facture brouillon est générée après l’intervention et validée .

### Facturation d’une vente de produit avec livraison différée (négoce B2B)

1. Le devis est transformé en commande .
2. Les produits commandés sont livrés au client.
3. Une facture brouillon est générée (sur la base des quantités livrées) et validée .

## Identifier vos commandes facturables

Une **commande** est considérée comme **facturable **lorsqu'elle est validée et comprend au moins une quantité en attente de facturation. Son éligibilité dépend de la **politique de facturation** en vigueur, qui définit les conditions nécessaires, telles que la confirmation de la vente, l’expédition des produits ou la réception d’un acompte.

**📓**Pour aller plus loin → [Politique de facturation](https://support.openfire.fr/hc/fr/articles/19091247558940)

Pour identifier vos commandes facturables :

- **Pour le plan basique** : OpenFire > Ventes > Mes Devis / Commandes > Filtres Commandes + Entièrement facturable

![](https://support.openfire.fr/hc/article_attachments/20226906383260)

- **Pour les autres plans** : Ventes > À facturer > Commandes à facturer

![](https://support.openfire.fr/hc/article_attachments/20226881293468)

Les lignes facturables d’une commande sont identifiées grâce à la couleur bleue de leurs quantités :

![](https://support.openfire.fr/hc/article_attachments/20226881294108)

## Générer une facture d’acompte

La facture d’acompte est établie en fonction de la position fiscale définie pour la commande. Elle peut être calculée soit sur la base d’un pourcentage du montant total, soit en appliquant un montant fixe. Lorsqu’un montant spécifique est facturé en tant qu’acompte, celui-ci peut, selon la configuration choisie, être considéré comme hors taxes (HT) ou toutes taxes comprises (TTC).

💡Note : Les factures d'acompte ne peuvent être créées automatiquement que depuis un bon de commande client.

Lorsqu'un bon de commande est à facturer, le bouton **Créer une facture** en haut à gauche apparaît :

![](https://support.openfire.fr/hc/article_attachments/20226906386204)

Cliquez dessus pour débuter votre facturation et choisissez le type de facture à créer.

![](https://support.openfire.fr/hc/article_attachments/20226906386716)

Pour créer une facture d'acompte, choisissez l'une des deux options suivantes :

- **Acompte (pourcentage)** : en tenant compte de l'échéancier de votre bon de commande, OpenFire vous présélectionne le pourcentage de l’acompte. Vous pouvez modifier ce pourcentage si vous le souhaitez.
- **Acompte (montant fixe)** : en tenant compte de l'échéancier de votre bon de commande, OpenFire présélectionne le montant de l’acompte. Vous pouvez modifier ce montant si vous le souhaitez. Selon votre configuration, le montant peut être compris comme HT ou TTC.

**📓**Pour aller plus loin → [Configurer vos factures d'acompte](https://support.openfire.fr/hc/fr/articles/19084741405212)

Le bouton **Créer et Afficher la facture **vous permet de générer la facture et d'être amené dessus directement.

Le bouton **Créer une facture** vous permet de générer la facture mais de rester sur le bon de commande.

La facture d’acompte est créée en brouillon, avec les caractéristiques suivantes :

- Elle est créée en brouillon et peut être modifiée
- Le montant de l’acompte est porté sur une ligne de produit Acompte.
- Le numéro de la commande est repris comme origine de la facture

![](https://support.openfire.fr/hc/article_attachments/20226906386972)

Dans la commande d’origine, une ligne de commande est ajoutée, dans une section “Acomptes” dédiées, détaillant le montant de l’acompte facturé.

Cette ligne est directement rattachée à la facture d’acompte générée, et permettra de déduire de la facturation finale les acomptes déjà facturés. **Vous ne pouvez donc pas la modifier ou la supprimer.**

![](https://support.openfire.fr/hc/article_attachments/20226881301276)

## Générer une facture de solde

La facture de solde correspond à la facture finale de votre commande. Elle a pour objectif de facturer l’ensemble des produits et prestations livrés, en déduisant les acomptes éventuellement déjà émis.

La **facture de solde** (ou facture finale) correspond à l’option **Facture normale** dans votre interface de facturation.

![](https://support.openfire.fr/hc/article_attachments/20226881301532)

- **Facture normale** : une facture standard est émise avec toutes les lignes de commande prêtes à être facturées, selon leur politique de facturation (basée sur la quantité commandée ou livrée) ;
- **Inclure les lignes à quantité 0** : cochez la case si vous souhaitez que la facture reprenne les produits pour lesquels la quantité commandée est à 0 dans le bon de commande.
- **Déduire les acomptes** : cochez la case si vous souhaitez que les factures d'acompte déjà créées se déduisent de la facture que vous allez créer.

## Les cas particuliers

### Les factures partielles

Une facture partielle correspond à une facture où une partie seulement des produits et des prestations de la commande d’origine sont à facturer.

- **Si la facturation est basée sur les quantités livrées**, seules les lignes correspondant aux articles expédiés et non encore facturés seront incluses dans la facture.
- **Si la facturation est basée sur les quantités commandées**, toutes les lignes non encore facturées seront prises en compte dans la facture générée.

Dans ces deux cas, il est possible que certaines lignes facturables ne nécessitent finalement pas d’être facturées immédiatement. Pour les exclure, il suffit de les supprimer de la facture brouillon. Elles redeviendront alors facturables dans la commande d’origine.

### Les factures proforma

Une **facture proforma** est un document préliminaire qui sert de facture provisoire, transmise au client avant la livraison des biens ou des prestations.

Elle n’a **aucune valeur comptable ou fiscale** et ne déclenche pas d’écritures comptables. Son but est principalement d’informer le client du montant à payer avant l’émission de la facture définitive. Elle pourra être transformée en facture ultérieurement.

La facture proforma est générée à partir d'un **bon de commande**.

![](https://support.openfire.fr/hc/article_attachments/20226906391196)

💡Note : Il n'est pas possible d'envoyer une facture proforma pour une commande si une facture d’acompte a déjà été émise. Dans ce cas, le bouton "Envoyer une facture proforma" ne s'affiche pas.

Le document pdf édité comporte bien la mention Facture pro forma et reprend le numéro de la commande d’origine :

![](https://support.openfire.fr/hc/article_attachments/20226906391964)

**📓**Pour aller plus loin → [Activer les factures pro forma](https://support.openfire.fr/hc/fr/articles/19222609331996)

Mis a jour le : 23/05/2025
