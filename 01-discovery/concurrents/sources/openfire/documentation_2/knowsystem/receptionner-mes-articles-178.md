---
url: https://documentation.openfire.fr/knowsystem/receptionner-mes-articles-178
url_finale: https://documentation.openfire.fr/knowsystem/receptionner-mes-articles-178
date_collecte: 2026-09-06
destination: documentation_2
---

Un bon de réception sera généré automatiquement suite à la validation d'une commande fournisseur, permettant ainsi de suivre et valider sa réception. 

Ces bons peuvent également être créés sans saisie d’une commande fournisseur au préalable.

## Consultation des bons de réception

Depuis ce bon de réception, un bon de préparation et un bon de livraison sont éditables via le menu

d’impression.

Le Bon de réception est structuré de la même manière qu’un bon de livraison.

- L’onglet Demande initiale : reprend l’ensemble des lignes de la Commande fournisseur d’origine;
- L’onglet Opérations : Reprend l’ensemble des lignes à réceptionner

Une fois la réception des articles effectuée, il faut valider cette réception dans OpenFire. La confirmation de la réception valide l’entrée en stock des articles concernés.

## Réception totale

Si tous les articles ont bien été reçu, vous pouvez valider une réception simplement en cliquant sur le bouton Valider disponible en haut à gaude du bon.

## Réception partielle

La validation de la réception s’effectue donc depuis l’onglet Opérations du Bon de réception.

La réception s’effectue ligne par ligne:

- Ligne Verte : Quantité A faire (demande initiale) = Quantité Fait (réception en cours)
- Ligne Rouge : Quantité A faire < Quantité Fait (la réception est supérieure à la demande initiale)
- Ligne Bleue : Ligne en cours de modification
- Ligne Noire : Quantité A faire > Quantité Fait (non encore traitée ou la réception est inférieure à la demande initiale en l’état)

A la validation de ce bon de réception, la création d’un reliquat sera alors proposée.

  Plus d'information sur [les retours et reliquats](https://documentation.openfire.fr/knowsystem/gerer-les-retours-et-les-reliquats-179)