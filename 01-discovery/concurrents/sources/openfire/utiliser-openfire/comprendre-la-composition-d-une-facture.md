---
source: https://support.openfire.fr/hc/fr/articles/20229766831260-Comprendre-la-composition-d-une-facture
categorie: Utiliser OpenFire
titre: Comprendre la composition d'une facture
date_recuperation: 2026-09-05
---

# Comprendre la composition d'une facture

Cet article détaille les éléments constitutifs d'une facture dans OpenFire et vous donne les clés pour les créer et en vérifier les informations essentielles avant de les valider.

Cet article contient les sections suivantes :

- [Comprendre la composition d’une facture ](#h_01JQ9BFT0T3P6V08128SM0HCHE)
  - [Vérifier les informations principales de votre facture ](#h_01JQ9BFT0TQHWTQD5QQ6R9WCAE)
  - [Vérifier les lignes de votre facture ](#h_01JQ9BFT0TCEMT9Z50K5VVJA8R)
  - [Vérifier les écritures comptables de votre facture ](#h_01JQ9BFT0TPAQ0KK7R7N2JSWXV)
  - [Vérifier les informations additionnelles de votre facture ](#h_01JQ9BFT0T6EK50S8K5YBYQMP8)
    - [Rubrique Facture ](#h_01JQ9BFT0T87TSMKXEZFTYSX72)
    - [Rubrique Comptabilité ](#h_01JQ9BFT0TT83DZVVFF441KMQN)
    - [Rubrique Paramètres d’impressions, Marketing & Commentaires ](#h_01JQ9BFT0TN6M39H6X6NN2MNSY)
  - [Boutons d’actions et barre d’état](#h_01JQ9BFT0VPEP3MHAZ15Z6RG1N)

# Comprendre la composition d’une facture

Plusieurs parties et plusieurs onglets constituent une facture :

## Vérifier les informations principales de votre facture

![](https://support.openfire.fr/hc/article_attachments/20229735454108)

**Client** : il s'agit du client à laquelle la facture est adressée. Si la facture est générée depuis une commande client, c’est l’adresse de facturation de la commande qui est reprise comme Client de la facture.

**Adresse de livraison** : Si la facture est générée depuis une commande client, c’est l’adresse de livraison de la commande qui est reprise.

**Référence de la commande **: Il s’agit d’une référence libre permettant d’identifier la facture. Si la facture est générée depuis une commande client, c’est le champ “**Référence commande**” de cette commande qui est repris.

**Date de facturation** : il s'agit de la date de la facture. Si ce champ reste vide, la date du jour sera appliquée à la confirmation de la facture.

🚨Avertissement : Il est impossible de dater une facture à une date antérieure à celle de la dernière facture validée. 

Si ce cas se présente, le message "Erreur de chronologie" s'affichera. Cette erreur peut également survenir si une facture en brouillon possède une date de facturation antérieure à celle de la facture que vous tentez de valider.

Le message "Erreur de chronologie" illustre cette situation. Il peut également survenir si vous avez une facture en brouillon avec une date de facturation antérieure à la date de facturation de la facture que vous essayez de valider.

**Exemple **: vous essayez de valider une facture en date du 1er janvier 2025 mais vous avez une autre facture en brouillon dont la date de facturation est le 31 décembre 2024.

Validez cette facture ou brouillon ou videz le champ **Date de facturation** pour ne plus avoir l'erreur.

**Position fiscale** : il s'agit de la position fiscale de la facture.

**Référence du paiement** : il s'agit de la référence à reprendre sur les paiements à réaliser en lien avec cette facture. Si ce champ reste vide, le numéro de la facture sera repris à la confirmation de la facture.

**Conditions de paiement** : il s'agit des conditions applicables pour le paiement de cette facture. Selon le type de facture générée, l’application de différentes conditions de paiements peut être automatisée.

  🧑‍🏫Exemple :

Vous validez avec votre client une commande pour l’installation d’une chaudière
    à granulés. La condition de paiement de la commande est la suivante : Acompte
    30% - Solde à la pose.

Chacune des deux factures associées à cette condition de paiement aura
    cependant des conditions de paiement différentes.

*Pour la facture d’acompte *: vous proposerez probablement un paiement à réception de la facture.
💡Note : Vous pouvez déterminer la condition de paiement applicable systématiquement via le paramètre général suivant :
![](https://support.openfire.fr/hc/article_attachments/20229766819356)

*Pour la facture de solde ***: **vous pourrez proposer un paiement comptant ou à terme en une seule échéance.
💡Note : Pour chaque condition de paiement appliqué dans une commande client, vous pouvez définir la condition de paiement à appliquer à la facture finale.
![](https://support.openfire.fr/hc/article_attachments/20229735454876)

**Date d'échéance** : il s'agit de la date d'échéance de la facture. Celle-ci est calculée par la condition de paiement sélectionnée.

**Type de vente** : reprend le **type** du bon de commande dont est issue la facture.

**Journal** : il s'agit du journal sur lequel la facture est comptabilisée.

## Vérifier les lignes de votre facture

À l’image de vos commandes client, vous pouvez compléter le corps de votre facture en ajoutant les produits et prestations à facturer.

Lorsque votre facture est générée depuis une commande client, les lignes sont déjà complétées. Tant que la facture n’est pas validée, vous pouvez les modifier ou les supprimer, ou en ajouter des nouvelles.

![](https://support.openfire.fr/hc/article_attachments/20229735455516)

En bas de vos lignes de facture, vous retrouvez le bloc relatif aux totaux de votre facture :

- **Montant HT** : total des montants HT des lignes de votre facture ;
- **TVA **: détaille le montant de TVA par taux identifié dans la facture ;
- **Total** : total TTC de la facture ;
- **Montant dû** : solde restant à payer par votre client.

Si des règlements ont été enregistrés pour ce client sans être associés à une facture, ils apparaîtront sous l’appellation **"Crédit en circulation"**. Vous pouvez les appliquer à la facture en cliquant sur le bouton **"AJOUTER"**.

| ![](https://support.openfire.fr/hc/article_attachments/20229766821660) | ![](https://support.openfire.fr/hc/article_attachments/20229766824348) |
| --- | --- |

## **Vérifier les écritures comptables de votre facture**

Dans OpenFire :

- Une facture est une pièce comptable ;
- Chaque ligne de facture correspond à une écriture comptable de la pièce.

![](https://support.openfire.fr/hc/article_attachments/20229766824732)

L’affectation des différents comptes est automatisée et dépend de votre configuration. Ils peuvent être modifiés directement dans votre facture tant que cette dernière est en brouillon.

Si une anomalie de compte est constatée, n’hésitez pas à vérifier la configuration générale !

## **Vérifier les informations additionnelles de votre facture**

Cet onglet reprend les informations diverses qui constituent la facture :

![](https://support.openfire.fr/hc/article_attachments/20229766825500)

### Rubrique Facture

**Référence client** : désigne le code client défini dans sa fiche client.

**Suivi interne **: ce champ vous permet de noter des informations internes relatives au suivi de la facturation. Ce champ peut-être affiché dans la liste des factures afin de diffuser une information rapide à toutes les personnes consultant cette facture. Il est possible de modifier ce champ même si la facture est comptabilisée.

![](https://support.openfire.fr/hc/article_attachments/20229766826140)

**Date de visite technique **: si la facture est issue d'un bon de commande et que celui-ci a son champ Date de visite technique renseigné, la date sera reprise ici automatiquement. Il est possible de modifier ce champ même si la facture est comptabilisée.

**Etiquettes clients **: si le client a des étiquettes sur sa fiche contact, elles seront reprises ici.

**Prospecteur **: il s'agit du prospecteur de cette facture.

**Vendeur **: il s'agit du vendeur de cette facture.

**Équipe commerciale **: il s'agit de l'équipe commerciale de cette facture.

**Compte bancaire destinataire **: il s'agit du numéro bancaire sur lequel la facture sera payée. C'est un compte bancaire de la société s'il s'agit d'une facture client ou d'un avoir fournisseur, sinon, c'est un numéro de compte bancaire du tiers.

### Rubrique Comptabilité

**Société **: il s'agit de la société à laquelle appartient cette facture.

**Publication automatique **: désigne les modalités selon lesquelles la facture peut-être validée et comptabilisée automatiquement à une date de référence. Plusieurs valeurs sont disponibles :

- **Non **: la facture n’est jamais comptabilisée automatiquement
- **À la date** : la facture sera comptabilisée automatiquement le jour de la date de facturation saisie
- **Mensuel **: comptabilisée le dernier jour du mois de la date de facturation
- **Trimestriel **: comptabilisée le dernier jour du trimestre de la date de facturation
- **Annuel **: comptabilisée le dernier jour de l’année de la date de facturation

**À vérifier** : si cette case est cochée, cela signifie que l'utilisateur n'était pas sûr de toutes les informations relatives au moment de la création de la pièce comptable et qu'elle doit être vérifiée de nouveau. La pièce peut être vérifiée depuis `Facturation > Conseiller > Ecritures comptables`(ou Pièces comptables) ; un filtre **À vérifier** est disponible pour lister tous les éléments à vérifier.

### Rubrique Paramètres d’impressions, Marketing & Commentaires

Ces rubriques sont identiques à celles définies dans les devis.

**📓**Pour aller plus loin → [Créer, personnaliser et envoyer vos devis](https://support.openfire.fr/hc/fr/articles/19076240168988)

## Boutons d’actions et barre d’état

Les différents boutons d’action vous permettent d'agir sur la facture :

![](https://support.openfire.fr/hc/article_attachments/20229766826652)

- **Envoyer & Imprimer **: vous permet d’envoyer la facture à votre client, en utilisant l’éditeur de mail standard Odoo.
- **Enregistrer un paiement **: cette action vous permet de saisir un règlement directement rattaché à votre facture.

**📓**Pour aller plus loin → [Enregistrer un paiement depuis une commande ou une facture](https://support.openfire.fr/hc/fr/articles/19085215074844)

- **Aperçu **: permet de prévisualiser la facture au format HTML.
- **Avoir : **vous permet de saisir un avoir en lien avec votre facture.

**📓**Pour aller plus loin → [Créer un avoir](https://support.openfire.fr/hc/fr/articles/19084802918940)

- **Etat de la facture : **Une barre de d’état de la facture est également disponible. Les états disponibles pour votre facture sont les suivants : 
  - **Brouillon **: les factures brouillon peuvent être modifiées ou supprimées.
  - **Comptabilisée **: la facture est validée et ne peut plus être modifiée.
  - **Annulée **: il s’agit d’une facture brouillon qui a été annulée a posteriori (une facture comptabilisée ne peut pas être annulée).
- **Etat de règlement** : une indication sur l’état de règlement est également disponible sous l’état de la facture. Les états proposés sont Partiel ou Payé.

![](https://support.openfire.fr/hc/article_attachments/20229766828700)

Mis a jour le : 30/12/2025
