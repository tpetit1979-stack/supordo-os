---
url: https://documentation.openfire.fr/knowsystem/imprimer-ma-facture-140
url_finale: https://documentation.openfire.fr/knowsystem/imprimer-ma-facture-140
date_collecte: 2026-09-06
destination: documentation_2
---

Depuis OpenFire, vous pouvez imprimer vos devis, bon de commande ou factures au format PDF. Ces PDF seront automatiquement téléchargés sur votre ordinateur.

Cela vous permet :

- de les imprimer directement après téléchargement,
- de les sauvegarder pour archive.

## Imprimer une facture

Rendez-vous sur la facture que vous souhaitez imprimer, puis cliquez sur le bouton imprimer disponible en haut à gauche, ou sur le lien Imprimer > Factures :

La facture PDF sera alors téléchargée sur votre poste.

Les factures imprimées sont également sauvegardés automatiquement dans l'application OpenFire et sont disponibles via le bouton Pièces Jointes :

Cela peut être utile dans certains cas puisqu'il permet de retrouver la dernière version imprimée d'un document. Par exemple, si vous imprimez une facture le 01/01/2022, une pièce jointe est automatiquement enregistrée et accessible via le bouton Pièces jointes.

Attention: si vous demandez la réimpression de cette facture le 01/03/2022, le document reprendra les données telles qu’elles étaient au 01/01/2022. Pour sortir un document à jour, il faut alors supprimer la pièce jointe.

Vous pouvez également imprimer un document .PDF unique contenant plusieurs factures.

Pour cela, rendez-vous sur la liste des factures disponible dans **Comptabilité > Ventes > Factures clients**.

Sélectionnez les factures a imprimer, puis cliquez sur le lien Imprimer > Factures : 

## Impression des acomptes

Il existe deux possibilités d’affichage de l’acompte sur une facture finale en pdf :

- Ligne d’acompte dans le corps de la facture : le montant total HT correspondra alors au montant HT du bon de commande moins le montant de l’acompte HT:

- Ligne d’acompte en dessous du montant TTC de la facture : le montant total HT correspond au montant du bon de commande validé et le paiement de l’acompte est considéré comme un paiement:

 Pour ce dernier affichage, les écritures comptables générées sont conformes dans le journal de ventes mais il faut bien le notifier à votre cabinet comptable si vous ne transmettez que les factures en pdf.

Pour activer cet affichage, rendez-vous dans **Comptabilité > Configuration > Impression des totaux dans les factures de vente**

Vous pouvez alors ajouter la catégorie Acompte afin qu'il apparaisse en dessous du montant TTC de la facture.

 *Plus d'information sur [l'impression des totaux dans les factures](https://documentation.openfire.fr/knowsystem/impression-des-totaux-dans-les-factures-183)*