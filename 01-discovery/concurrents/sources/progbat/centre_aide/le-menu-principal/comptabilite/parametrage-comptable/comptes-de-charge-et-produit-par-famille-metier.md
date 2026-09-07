---
url: https://docv5.progbat.com/le-menu-principal/comptabilite/parametrage-comptable/comptes-de-charge-et-produit-par-famille-metier
url_finale: https://docv5.progbat.com/le-menu-principal/comptabilite/parametrage-comptable/comptes-de-charge-et-produit-par-famille-metier
date_collecte: 2026-09-06
destination: centre_aide
---

# Comptes de charge et produit par famille métier

## Un système en cascade

Le paramétrage permet :

- de saisir des codes comptables pour des familles métiers
- de saisir des codes comptables pour des ouvrages ou des éléments spécifiques
- de ventiler les achats et les ventes par taux de TVA.

▶️ Au moment de l'export comptable :

- Le logiciel cherche pour chaque ligne de la facture si l'élément ou l'ouvrage est enregistré en bibliothèque, et si un compte comptable a été saisi pour cet élément ou cet ouvrage en particulier. 
  - Si oui, il applique le code comptable spécifique, et saute les étapes suivantes.
- Sinon, le logiciel recherche si cet élément ou cet ouvrage est lié à une famille métier, et si et si un compte comptable a été saisi pour cette famille métier. 
  - Si oui, il applique le code comptable spécifique de la famille, et saute l'étape suivante.
- Si aucune des 2 conditions précédentes n'est remplie, alors le logiciel applique le compte "générique" défini ici.
- Enfin, le logiciel analyse le taux de TVA appliqué à la ligne, et ajoute en fonction du taux une extension au compte de charge ou de produit, pour réaliser une ventilation par taux de TVA. 
  - Si le compte utilisé est le 7041, et que l'extension choisie pour le taux à 20% est 20, le compte appliqué à l'écriture sera le 704120.

Mis à jour