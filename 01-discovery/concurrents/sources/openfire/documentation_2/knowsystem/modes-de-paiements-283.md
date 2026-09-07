---
url: https://documentation.openfire.fr/knowsystem/modes-de-paiements-283
url_finale: https://documentation.openfire.fr/knowsystem/modes-de-paiements-283
date_collecte: 2026-09-06
destination: documentation_2
---

Principes de fonctionnement des modes de paiements :

- Le mode de paiement identifie le moyen de paiement qui est applicable à un bon de commande client / fournisseur ou à une facture client / fournisseur ;
- A chaque enregistrement de règlement, le mode de paiement est associé un journal de type banque ou liquidité et donc un compte comptable ;
- Une bonne maîtrise comptable est nécessaire pour configurer les modes de paiement en fonction du journal.
- Le même journal peut recevoir plusieurs modes de paiements.
- Un affichage personnalisé est possible pour indiquer le mode de paiement, la date,... sur le bon de commande et la facture pdf.

## Paramétrage modes de paiements


*Accès* : **Comptabilité > Configuration > Modes de paiement** 

Un paramètre est déjà prédéfini dans votre base en fonction des éléments que vous avez apportés à OpenFire.

 Avant de modifier ou créer les modes de paiements, il faut décider de l'encaissement direct ou différé en banque pour chaque mode de paiement.

Pour créer un nouveau mode de règlement, cliquez sur Créer.

Nous prendrons l'exemple du paiement Virement Banque ZZ. Il faudra au préalable créer un journal de banque.

  Plus d'informations sur la création d'un journal __Journaux Comptables__

1 - Nom du mode de paiement qui s'affichera lors de l'enregistrement d'un règlement. il doit être explicite.

2 - Nom de la société qui sera affectée au mode de paiement.

3 - Nom du journal associé au mode de paiement.

4 - Le compte bancaire associé au journal de banque

5 - Paramètre d'affichage au niveau du bon de commande ou de la facture pdf : vous trouverez une explication plus détaillée dans le chapitre suivant.

6 - Lorsque vous avez renseigné toutes les informations, vous sauvegardez.

Le mode de paiement créé, vous pourrez l'utiliser pour effectuer le paiement à partir du bon de commande, de la facture ou directement du menu Paiements.

Plus d'informations sur la création d'un paiement :

*Enregistrer un paiement*
Plus d'informations sur la remise en banque :


*Remise en banque*
## Paramètres d'affichage et d'impression au niveau de la facture PDF

Pour chaque mode de paiement, un paramétrage du mode d'impression des paiements perçus à l'impression PDF peut être réalisé.

Ce paramétrage se base sur la saisie d'un texte type pouvant inclure des variables du type "mode de paiement" ou "référence du paiement".

Les variables sont détaillées dans le mode de paiement lui-même.

**Exemple de rendu possible à l'impression PDF de la facture :**