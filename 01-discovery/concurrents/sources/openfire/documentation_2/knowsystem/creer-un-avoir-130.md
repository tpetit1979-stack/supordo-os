---
url: https://documentation.openfire.fr/knowsystem/creer-un-avoir-130
url_finale: https://documentation.openfire.fr/knowsystem/creer-un-avoir-130
date_collecte: 2026-09-06
destination: documentation_2
---

Dès qu'une facture est validée, il est possible d'établir un Avoir à partir de la facture. Les factures d’avoir suivent les mêmes règles de numérotation que les factures. 

Plusieurs méthodes de création d’avoir existent en fonction des besoins :

- Créer un avoir sans passer par une facture : la facture n'est pas existante et il faut créer un avoir directement ;
- Créer un avoir en brouillon : à utiliser lorsqu'il y a litige sur la facture et la facture ne sera pas payée entièrement ou demande un remboursement partiel ; on parle alors d'un avoir partiel ; **Attention** : cette méthode**ne permet pas** de refacturer le bon de commande.
- Annuler une facture : si vous souhaitez annuler définitivement la facture dans sa totalité ;
- Modification d'une facture : peut être utilisé lorsque votre facture est erronée et que vous souhaitez la régénérer.

**Attention :** Il faut tout d'abord délettrer les paiements des factures avant de pouvoir générer un avoir.

## Créer un avoir en brouillon / partiel

Vous pouvez créer un avoir partiel dans le cas où le client ne payera pas la totalité de la facture. Pour cela, suivez les étapes ci-dessous :

    

    2/ Depuis la facture, délettrez tous les paiements qui lui sont associés.

    2/ Allez à la facture que vous souhaitez modifier puis cliquez sur **Avoir > Créer un avoir en brouillon**.

3/ Modifiez ou supprimez des lignes de l'avoir en brouillon généré pour que l'avoir porte sur le(s) article(s) concernés et soit d'un montant TTC égal à celui que vous voulez retrancher de la facture d'origine.

  Lorsque l’on utilise le bouton Avoir disponible sur une facture, la base OpenFire comprend nativement qu’il s’agit d’un avoir. Il ne faut donc jamais saisir d’avoirs d’un montant négatif.


   3/ Validez puis associez l'avoir à la facture comme s'il s'agissait d'un paiement.

## Annuler une facture

Vous pouvez annuler la facture dans le cas où le projet est par exemple annulé. Pour cela, suivez les étapes ci-dessous :

        1/ Depuis la facture, délettrez tous les paiements qui lui sont associés.

    2/ Générez un avoir et choisissez un avoir de type annuler pour que la facture soit annulée par un avoir.

    3/ Depuis le bon de commande client, vous pouvez désormais générer une nouvelle facture dans **Ventes > Bon de commande**.

   Inutile de créer de nouveaux paiements client, ils vous seront proposés lorsque vous validerez la nouvelle facture.

## Modifier une facture

Si une facture validée est erronée et qu'il faut la corriger, voici les étapes à suivre si vous souhaitez corriger une facture erronée.

    1/ Depuis la facture, délettrez tous les paiements qui lui sont associés.

    2/ Générez un avoir et choisissez un avoir de type **modifier** pour que la facture d'origine soit annulée par un avoir et qu'une nouvelle facture brouillon soit éditée. 

3/ Vous êtes ensuite immédiatement positionné sur une nouvelle facture brouillon que vous pouvez modifier.

Inutile de créer de nouveaux paiements client, ils vous seront proposés lorsque vous validerez la nouvelle facture.

## Créer un avoir sans passer par une facture

Accès : Comptabilité>Tableau de bord

Pour créer un avoir, dans le tableau de bord, rendez-vous sur le journal de "Ventes" concerné et cliquez sur "Plus" et, dans la colonne "Nouvelle", cliquez sur "Avoir". Un avoir en brouillon se crée.