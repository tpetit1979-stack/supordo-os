---
url: https://documentation.openfire.fr/knowsystem/gerer-les-retours-et-les-reliquats-179
url_finale: https://documentation.openfire.fr/knowsystem/gerer-les-retours-et-les-reliquats-179
date_collecte: 2026-09-06
destination: documentation_2
---

OpenFire vous permet de gérer l’intégralité de votre cycle d’achat, de la commande auprès de votre fournisseur, jusqu’aux réceptions totales ou partielles, et aux éventuels retours de marchandises.

## Retours Fournisseur

En gestion des achats, il est parfois nécessaire de retourner certains articles aux fournisseurs. OpenFire vous permet d'effectuer ces retours, même si une partie ou même la totalité de la marchandise commandée est déjà arrivée dans votre entrepôt.

Pour effectuer un retour de marchandise, il faut vous rendre sur le bon de réception initial puis cliquer sur le bouton Retourner :

Une fenêtre s'ouvrira alors reprenant l'ensemble des articles de ce bon de réception. Vous pouvez alors retirer les lignes non concernées avant de cliquez sur le bouton Retourner

Une fois la validation effectuée, l’application annulera donc la réception de ces articles, et mettra à jour le bon de livraison afin de pouvoir réapprovisionner ces articles.

Vous avez alors la possibilité de définir s'il y a eu remboursement client ou non. Si c'est le cas, aucun nouveau bon de livraison pourra être régénéré pour cet article.

## Reliquats

La validation de la réception s’effectue donc depuis l’onglet Opérations du Bon de réception.

La réception s’effectue ligne par ligne:

- Ligne Verte : Quantité A faire (demande initiale) = Quantité Fait (réception en cours)
- Ligne Rouge : Quantité A faire < Quantité Fait (la réception est supérieure à la demande initiale)
- Ligne Bleue : Ligne en cours de modification
- Ligne Noire : Quantité A faire > Quantité Fait (non encore traitée ou la réception est inférieure à la demande initiale en l’état)

A la validation de ce bon de réception, la création d’un reliquat sera alors proposée.

Si je souhaite créer un reliquat , le premier bon de réception sera alors confirmé et un nouveau bon de réception sera généré pour le reliquat encore non reçu.