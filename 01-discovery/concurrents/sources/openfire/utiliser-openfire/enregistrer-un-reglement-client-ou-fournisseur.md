---
source: https://support.openfire.fr/hc/fr/articles/19088047512220-Enregistrer-un-r%C3%A8glement-client-ou-fournisseur
categorie: Utiliser OpenFire
titre: Enregistrer un règlement client ou fournisseur
date_recuperation: 2026-09-05
---

# Enregistrer un règlement client ou fournisseur

OpenFire vous permet de gérer et de suivre tous les paiements et remboursements clients et fournisseurs. Vous pouvez enregistrer un paiement de différentes manières : un paiement libre non lié à une facture, un paiement depuis une commande client qui sera appliqué à la prochaine facture, un paiement directement associé à une facture spécifique ou des règlement / prélèvement SEPA en lot.

Cet article vous guide dans l'enregistrement de ces différents types de paiements.

Cet article contient les sections suivantes :

- [Comprendre la composition d'un paiement](#h_01JS21347FD4655TT4D7P8A75D)
- [Enregistrer un paiement depuis une facture](#h_01JS21347FZ2M0CP1FYBS1BXPT)
  - [Saisir un règlement partiel ou total](#h_01JS21347FQWPJS3DRTKY3VFC5)
  - [Visualiser les règlements de la facture](#h_01JS21347FFCTN7TPCRNNME65N)
  - [Associer (lettrer) ou dissocier (dé-letter) un paiement de sa facture](#h_01JS21347F4P0TYGP6RQ3DQVZG)
- [Enregistrer un paiement depuis un devis ou bon de commande client](#h_01JS21347FTWD2RJC4T8EQPEPG)

# Comprendre la composition d’un paiement

Chemin d’accès à mes paiements :

- **Pour le plan basique :** `Ventes > Mes paiements ` OU `OpenFire > Mes paiements `
- **Pour les autres plans :** `Facturation > Clients > Paiements `

Un paiement se compose de plusieurs champs :

![](https://support.openfire.fr/hc/article_attachments/19627404313116)

- **Mode de paiement** : il s'agit du moyen de paiement utilisé pour régler la facture (chèque, carte bancaire, espèces...). Ce champ est obligatoire.

**📓 **Pour aller plus loin → Mode de paiement

- **Journal** : il s'agit du journal comptable sur lequel sera enregistré le paiement. En sélectionnant le mode de paiement, celui-ci récupère le journal associé automatiquement. Ce champ est obligatoire.
- **Montant **: il s’agit du montant du paiement enregistré.
- **Date du paiement** : il s’agit de la date à laquelle vous avez reçu le paiement.
- **Mémo** : il s'agit de l'objet auquel se rattache le paiement (numéro de facture, de bon de commande, etc.).
- **Référence** : il s'agit de la référence du paiement (numéro de chèque, de transaction, etc.).
- **Étiquettes du paiement** : vous pouvez ajouter une ou plusieurs étiquettes au paiement (acompte 1, acompte 2, solde...), si vous souhaitez classer vos paiements par type.

Un paiement doit ensuite être lettré à une facture.

# Enregistrer un paiement depuis une facture

## Saisir un règlement partiel ou total

Lorsque vous êtes sur une facture, cliquez sur le bouton "Enregistrer un paiement".

![](https://support.openfire.fr/hc/article_attachments/19627406094492)

Si vous entrez un montant différent du montant dû de la facture, OpenFire vous proposera deux options :

- **Laisser ouvert** :

![](https://support.openfire.fr/hc/article_attachments/19627406095644)

- **Si le montant réglé est inférieur au montant dû de la facture** : le paiement enregistré sera lettré à la facture et celle-ci restera ouverte pour le nouveau montant restant dû ;
- **Si le montant réglé est supérieur au montant dû de la facture** : la facture sera alors soldée mais l’écart de règlement ne sera pas lettré en comptabilité. L’utilisateur devra alors procéder manuellement à ce lettrage.

- **Marquer comme entièrement payée** :

![](https://support.openfire.fr/hc/article_attachments/19627404318748)

- OpenFire vous demandera alors de préciser :
  - Le compte comptable à utiliser pour comptabiliser la différence ;
  - Le libellé de l’écriture de contrepartie qui enregistrera la différence.

Pièce comptable générée :

![](https://support.openfire.fr/hc/article_attachments/19627404320028)

Libellé de l’écriture de règlement :

![](https://support.openfire.fr/hc/article_attachments/19627406101276)

**💡**Note : Généralement, les comptes utilisés pour enregistrer les écarts de règlement sont les suivants :

- Pour un écart de règlement en votre faveur : 758000 Produits divers de gestion courante
- Pour un écart de règlement en votre défaveur : 658000 Charges diverses de gestion courante

Les paiements enregistrés directement depuis la facture sont automatiquement lettrés à cette dernière.

## Visualiser les règlements de la facture

Au niveau des totaux de la facture, vous pouvez consulter la liste des paiements associés à la facture, entre le **total** et le **Montant dû**.

- Le ![](https://support.openfire.fr/hc/article_attachments/19627406101404)vous donne accès aux informations comptables du paiement.
- La ![](https://support.openfire.fr/hc/article_attachments/19627406103324)vous permet d’accéder directement au formulaire du paiement.

![](https://support.openfire.fr/hc/article_attachments/19627406103964)

## Associer (lettrer) ou dissocier (dé-letter) un paiement de sa facture

La fonction **ANNULER LE LETTRAGE** permet de dissocier le paiement de la facture, sans pour autant annuler le paiement.

![](https://support.openfire.fr/hc/article_attachments/19627404323356)

Le paiement ainsi délettré est visible en dessous du montant dû, dans la rubrique **Crédit en circulation**. Dans cette rubrique, vous pouvez également retrouver :

- Les éventuels autres **paiements **non lettrés (= en attente) du client!;
- Les éventuels **avoirs **du client également en attente de lettrage.

En utilisant la fonction AJOUTER, vous pouvez, en un clic, associer le règlement ou l’avoir en attente à la facture en cours.

# Enregistrer un paiement depuis un devis ou bon de commande client

Lorsque vous êtes sur un devis ou un bon de commande, cliquez sur le bouton "**Enregistrer un paiement d'avance**" pour Enregistrer un paiement.

**💡**Note : L'intitulé de ce bouton est le même que vous ayez déjà ou non édité une facture ou enregistré un précédent paiement.

**💡**Note : Depuis un devis ou bon de commande client, vous ne pouvez pas Enregistrer un paiement dont le montant est supérieur au montant dû.

Cliquez ensuite sur le bouton "**Enregistrer un paiement d'avance**" pour Enregistrer le paiement

Mis a jour le : 29/12/2025
