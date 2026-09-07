---
url: https://documentation.openfire.fr/knowsystem/creer-une-facture-de-situation-204
url_finale: https://documentation.openfire.fr/knowsystem/creer-une-facture-de-situation-204
date_collecte: 2026-09-06
destination: documentation_2
---

## Etapes préliminaires

Vérifiez tout d'abord que le module de gestion de situation soit bien installé dans la base.

Pour cela, rendez-vous dans **Ventes > Ventes > Devis,** cliquez sur un devis et cliquez ensuite sur l’onglet Autres informations . 

Il faut voir dans la partie Facturation les champs suivants :

Si ces champs n'apparaissent pas, contactez le support.

Avant l'utilisation, vérifiez la configuration si elle n'a pas été faite.

  Voir article  [Configurer la situation, retenue de garantie et compte prorata](https://documentation.openfire.fr/knowsystem/configurer-la-situation-retenue-de-garantie-et-compte-prorata-208)

## Facture de situation simple



Dans le champ “Nb. situations”, notez le nombre de situations que vous allez devoir faire au long du chantier. Si, au moment du devis, vous ne connaissez pas le nombre exact de situations, il faut dans tous les cas noter un chiffre afin que le bouton d’action “SITUATION” apparaisse. Ce nombre peut être modifié à tout moment (tant en diminuant qu'en augmentant ce nombre) tant que la facture finale n'est pas validée.

Dès lors que le champ Nb situations est rempli et que le devis est confirmé en bon de commande, un bouton d’action “SITUATION N°1” apparaît :


En cliquant sur “Situation n°1”, les lignes de commandes apparaissent sous forme de lignes de situation :

         **1.** "Pré-remplir" : permet de définir sur l'ensemble des lignes de commande : 

            * l'état d'avancement sur la **situation en cours** en % : 

            * l'état d'**avancement cumulé en cours** en % : 


Si l'état d'avancement n'est pas au global, il est possible de mettre le % d'avancement ligne par ligne dans la colonne "Sit. n (%)"

       **2.** "Total n-1 (%)" : information du % d'avancement avant la nouvelle situation.

       **3.** "Sit. n(%)" : information du % d'avancement de la situation actuelle.

       **4.** "Total n (%) : information du % d'avancement cumulé des situations.

       **5.** "Situation en cours" : Numéro de la situation en cours.

       **6.** "Date rapport situation" : date à laquelle la situation a été réalisée et qui sera notée sur le rapport de situation.

       **7.** "Situation en cours HT" : suivi du bon de commande avec le montant HT des situations déjà facturées ; montant de la situation et le montant total cumulé.

       **8.** "Situation en cours TTC" : suivi du bon de commande avec le montant TTC des situations déjà facturées ; montant de la situation et le montant total cumulé.

      **9.** "GENERER LA FACTURE DE SITUATION" : bouton d'action pour générer la facture de situation en brouillon.

     **10.** "RAPPORT DE SITUATION" : bouton d'action pour imprimer le rapport de situation. Ce rapport sera en pièce jointe automatiquement dès validation de la facture liée à la situation.

Quand les informations sont renseignées et après vérification des montants de la situation en cours, générez la facture de situation. La facture sera en brouillon et vous pourrez la valider après relecture.

Par défaut, le rapport de situation se trouvera en pièce jointe de la facture.

  Attention: les rapports de situation ne sont pas sauvegardés dans Openfire et ne peuvent donc pas être imprimés ultérieurement.

Le bon de commande passera ensuite en situation n°2, le bouton d'action se nommera et ainsi de suite, en fonction du nombre de situations noté dans le bon de commande.

Une ligne "situation n°1" apparaîtra sur le bon de commande et ainsi de suite jusqu'à la facture finale.

En fin de travaux, quand toutes les situations seront terminées, à partir du bon de commande, le bouton d'action se nommera .

L'action "Générer la facture finale" va créer 2 factures en brouillon :

- une facture de situation avec le rapport de situation et indiquant le solde à payer

- une facture de solde qui reprendra toutes les lignes de la commande avec la déduction des lignes de factures de situation. Cette facture de solde sera ainsi toujours à 0 €.

Ces 2 factures sont à valider après relecture des informations.

  Plus d'informations sur __[Créer une facture finale](https://documentation.openfire.fr/knowsystem/creer-ma-facture-finale-145)__