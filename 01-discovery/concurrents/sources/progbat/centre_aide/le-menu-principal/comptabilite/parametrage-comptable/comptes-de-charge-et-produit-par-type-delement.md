---
url: https://docv5.progbat.com/le-menu-principal/comptabilite/parametrage-comptable/comptes-de-charge-et-produit-par-type-delement
url_finale: https://docv5.progbat.com/le-menu-principal/comptabilite/parametrage-comptable/comptes-de-charge-et-produit-par-type-delement
date_collecte: 2026-09-06
destination: centre_aide
---

# Comptes de charge et Produit par type d'élément

Précisez ici le compte de charge ou de produit associé à chaque type d'achat et de vente.

## Un système en cascade

Le paramétrage peut paraître simpliste, mais il permet en réalité d'aller très loin, en permettant :

- de saisir des codes comptables pour des ouvrages ou des éléments spécifiques
- de ventiler les achats et les ventes par taux de TVA.

▶️ Au moment de l'export comptable :

- Le logiciel cherche pour chaque ligne de la facture si l'élément ou l'ouvrage est enregistré en bibliothèque, et si un compte comptable a été saisi pour cet élément ou cet ouvrage en particulier. 
  - Si oui, il applique le code comptable spécifique, et saute les étapes suivantes.
- Si non, le logiciel recherche si cet élément ou cet ouvrage est lié à une famille métier, et si et si un compte comptable a été saisi pour cette famille métier. 
  - Si oui, il applique le code comptable spécifique de la famille, et saute l'étape suivante.
- Si aucune des 2 conditions précédentes n'est remplie, alors le logiciel applique le compte "générique" défini ici.
- Enfin, le logiciel analyse le taux de TVA appliqué à la ligne, et ajoute en fonction du taux une extension au compte de charge ou de produit, pour réaliser une ventilation par taux de TVA. 
  - Si le compte utilisé est le 7040, et que l'extension choisie pour le taux à 20% est 20, le compte appliqué à l'écriture sera le 704020.

## Compte de charge par fournisseur

Afin de simplifier la saisie, notamment des frais généraux, il est possible d'affecter un compte de charge au niveau de la fiche fournisseur, comme par exemple 606110 pour le fournisseur EDF, ou 606120 pour le fournisseur "Carburant".

Ainsi, en saisissant ou en océrisant un ticket carburant, le compte de charge sera immédiatement appliqué.

Mis à jour