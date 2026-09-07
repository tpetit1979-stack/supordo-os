---
url: https://documentation.openfire.fr/knowsystem/enregistrer-un-paiement-161
url_finale: https://documentation.openfire.fr/knowsystem/enregistrer-un-paiement-161
date_collecte: 2026-09-06
destination: documentation_2
---

Sur OpenFire, un paiement peut être directement lié à une facture ou être enregistré pour une utilisation ultérieure.

- Si un paiement est lié à une facture, il réduit le montant dû de la facture. Vous pouvez avoir plusieurs paiements liés à la même facture.
- Si un paiement n'est pas lié à une facture, vous pouvez utiliser ce crédit/débit en attente pour payer des factures enregistrées ou des factures à venir.

Il est possible d'enregistrer un paiement depuis une facture, un bon de commande, une fiche contact ou encore depuis le menu comptabilité.

## Paiement d'une facture

Une fois une facture établie, il est possible de gérer les paiements associés.

Dans la facture créé cliquer sur le bouton enregistrer un paiement. Une fenêtre sera affiché pour saisir le montant payé.

  *Si vous enregistrez un paiement sur une facture client ou une facture fournisseur, cela reprends toutes les infos de la facture (montant, mémo) et le paiement est automatiquement rapproché avec la facture en réduisant le montant dû.*

Mode de paiement: permet de définir le mode de paiement utilisé pour ce règlement (chèque, virement, etc...)

  Plus d'information sur __les modes de paiements__

Montant du règlement: Il est possible dans OpenFire de gérer les paiements partiels et donc de saisir uniquement le montant payé au lieu du montant total de la facture.

Une fois le paiement restant sera effectué, la facture sera affichée comme payée.

Date de règlement: pré-rempli à la date du jour par défaut.

Mémo: ce champ permet de notez la référence d'un document dans les cas ou le paiement se réfère à un document (une commande client, une commande fournisseur ou une facture).

Catégorie: il est possible via ce champ de préciser s'il s'agit d'un premier acompte ou encore d'un paiement de solde.

Une fois catégorisé, en vous rendant dans **Comptabilité > Ventes > Paiements**, vous aurez alors la possibilité de filtrer les paiements enregistrés par date, par lettrage et par donc par catégorie.

Une fois la création du paiement confirmée, une pièce comptable sera créée reflétant la transaction qui vient d'être faite dans l'application de Comptabilité.



## Paiements non liés à une facture

Dans l'application Comptabilité, vous pouvez créer un nouveau paiement à partir du menu Ventes (pour enregistrer un règlement client) ou du menu Achats (pour payer un fournisseur).

Si vous utilisez ces menus, le paiement n'est pas lié à une facture, mais peut facilement être rapproché ultérieurement avec une facture.

  Plus d'information sur l'article: [Associer Paiements et Factures](https://documentation.openfire.fr/knowsystem/associer-paiements-et-factures-162)

        
    

## Différence de paiement

Lorsque vous enregistrez un paiement supérieur au montant de la facture, OpenFire vous proposera de gérer la différence de paiement.

Exemple: Nous enregistrons un paiement de 150€ pour une facture de 145€. Le logiciel nous propose alors un choix "différence de paiement" pour gérer les 5€ en plus. 

Nous pouvons choisir de "marquer la facture comme payée complètement" et de comptabiliser la différence dans le compte de notre choix:

*Généralement les comptes utilisés sont les comptes 658, lorsque le paiement est en notre défaveur, et 758 lorsque le paiement est en notre faveur.*

Si le paiement a déjà été enregistré, il est possible de solder la facture via une OD.

Vous avez la possibilité de solder ces factures en créant une écriture d'OD dans OpenFire.

Le plus simple pour le faire est de vous rendre sur la facture à solder, puis, dans l'onglet *Autres Informations*, cliquez sur la pièce comptable. 

Ensuite, cliquez sur le bouton Écritures lettrées disponible en haut à droite:

Enfin, cochez les écritures à l'écran et cliquez sur le bouton Action > Lettrer les écritures:

Cliquez sur le bouton Lettrer avec écart. Dans la fenêtre suivante il vous suffira de renseigner les deux champs suivants :

Si le restant dû est à votre défaveur, renseigner le compte de charge 658:

- Journal des pertes: Opérations diverses

- Compte de radiation: 658 000 (si c'est en votre défaveur)

Sinon, vous pourrez renseigner le compte 758 000 (si c'est en votre faveur)

## Annuler, modifier ou rembourser un paiement

Lorsqu'un paiement est enregistré sur OpenFire, plusieurs actions sont possibles. Vous pouvez l'annuler, le modifier ou le rembourser.

  Plus d'information sur l'article dédié: [Annuler, rembourser ou modifier un paiement](https://documentation.openfire.fr/knowsystem/annuler-rembourser-ou-modifier-un-paiement-163)