---
url: https://documentation.openfire.fr/knowsystem/mouvement-de-stocks-248
url_finale: https://documentation.openfire.fr/knowsystem/mouvement-de-stocks-248
date_collecte: 2026-09-06
destination: documentation_2
---

Dans OpenFire, les mouvements de stock représentent le transit de marchandises entre des emplacements. En effet, OpenFire utilise une méthode de suivi des stocks dite à double entrée, qui utilise donc deux entrées pour enregistrer tout mouvement de stock dans le système.

Cela signifie que pour chaque entrée dans le stock (par exemple, une réception d'achat), il y aura également une sortie correspondante (par exemple, une sortie pour une vente). Cette méthode permet d'avoir une vue précise et à jour de la quantité de stock disponible en tout temps.

Ainsi, un inventaire sur OpenFire génère des mouvements de stock entre différents emplacements.

Ces mouvements permettent donc de suivre les différents transferts qui s'opèrent sur un article dans le flux d'achat / vente au niveau du stock. 

## Illustration des mouvements de stock

Les mouvements de stock sont des opérations qui affectent la quantité de produits disponibles dans un emplacement de stock particulier.

Ils peuvent inclure des opérations telles que les entrées de stock (par exemple, lorsqu'un produit est reçu), les sorties de stock (par exemple, lorsqu'un produit est vendu), les transferts de stock (par exemple, lorsqu'un produit est transféré d'un emplacement de stock à un autre) et les ajustements de stock (par exemple, lorsqu'une correction de quantité est nécessaire).

Les mouvements de stock peuvent avoir lieu entre emplacements physiques et virtuels. Les Emplacements Virtuels sont des lieux qui n’existent pas, mais dans lesquels les produits peuvent être placés quand ils ne sont pas encore (ou plus) physiquement dans un stock.

Par exemple, si je valide la réception de 10 poêles commandés chez un fournisseur, les mouvements de stocks suivants seront créés:

Ainsi, un mouvement est créé sur l'emplacement de mon fournisseur, qui est un emplacement virtuel.

Si je vend un de ces poêles à un client, j'obtiendrais les mouvements de stocks suivants:

Mes stocks seront alors:

De la même façon, un inventaire sur OpenFire génère des mouvements de stock entre différents emplacements (éventuellement virtuels).

  Plus d'informations sur [l'](https://documentation.openfire.fr/knowsystem/consulter-mes-stocks-225)[Évolution des stocks](https://documentation.openfire.fr/knowsystem/consulter-mes-stocks-225)

## Vue des Mouvements de stock

Les mouvements de stock sont enregistrés et peuvent être suivis dans  l'application **Inventaire > Rapports > Mouvements de stocks** d'OpenFire, permettant ainsi une gestion efficace des stocks et une visibilité sur les niveaux de stock.

La vue Liste des mouvements de stock vous permettra de voir les emplacements d'origine et de destination de chaque Mouvements de stock enregistrés:

*Dans l'exemple ci-dessus, 2 Poêles 12350 (le Bon Poêle Soleil) ont été ajouté à mon stock suite à mon Inventaire du 20/10/2022.*

De la même façon, les mouvements de stocks sont également consultables depuis la fiche Article via le menu bouton Traçabilité :