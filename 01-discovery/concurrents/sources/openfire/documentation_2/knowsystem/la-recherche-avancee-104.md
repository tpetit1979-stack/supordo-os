---
url: https://documentation.openfire.fr/knowsystem/la-recherche-avancee-104
url_finale: https://documentation.openfire.fr/knowsystem/la-recherche-avancee-104
date_collecte: 2026-09-06
destination: documentation_2
---

OpenFire permet l'utilisation de différents opérateurs afin d'ajuster au mieux vos recherches.

## Opérateurs Ou/Et

**Opérateur OU** : Il s'agit de l'opérateur par défaut. 

Ainsi, deux mots saisis sont recherchés avec l'opérateur OU. Par exemple, la recherche *Thomas ou Jean* donne alors deux résultats:

**Opérateur ET** : pour activer l'opérateur ET, il faut maintenir les touches **MAJ + Entrée** à la recherche du second mot. 

Dans ce cas, le client (ou autre élément) est trouvé si les 2 mots existent dans le champ de recherche. La recherche *Thomas et Jean* donne alors un seul résultat:

## Recherche avancée

La recherche ne tient pas compte des majuscules et des minuscules, mais la recherche tient compte des caractères accentués. 

Dès lors, si vous souhaitez effectuer une recherche en ne connaissant pas l'accentuation du nom, vous pouvez utiliser le caractère spécial  **_**   (disponible sur la touche du 8).

Ce caractère permet de remplacer tout caractère à la position exacte de la chaîne recherchée.

Par exemple :

- « J_tul » pour Jotul ou Jøtul
- « St_v » pour Stuv ou Stûv
- « po_le » pour poêle ou poele
- « Fr_d_ric » pour Frédéric ou Frederic
- « 69___ » pour les codes postaux du département 69

De la même manière, si vous souhaitez effectuer une recherche en ne connaissant que certains des caractères, vous pouvez utiliser le caractère %

  *P*ar exemple, la recherche *%utou* va rechercher tous les contacts dont le nom contient au moins une lettre suivi de *utou*