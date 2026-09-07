---
url: https://documentation.openfire.fr/knowsystem/categories-d-articles-188
url_finale: https://documentation.openfire.fr/knowsystem/categories-d-articles-188
date_collecte: 2026-09-06
destination: documentation_2
---

Les catégories d'articles permettent de regrouper des produits ayant des caractéristiques similaires, afin de simplifier leurs gestions. 

Ces catégories sont obligatoires à la création d'un article, et ont à la fois vocation à classer les produits, mais également une vocation de gestion. En effet, elles peuvent être utilisées aussi bien dans les statistiques de vente que pour les imputations comptables ou que pour la valorisation de vos stocks.

## Créer une catégorie

Vous pouvez accéder aux catégories à travers différents modules, tel que le module de vente, d'achat ou d'inventaire:

A la création d'une catégorie, de nombreux champs peuvent être renseignés. Ceux-ci sont répartis en quatre sections principales.

En partie haute:

**Nom de la catégorie:** désignation de la catégorie qui sera utilisé

**Catégorie mère:** permet de créer une sous-catégorie lié à une catégorie mère.

  Une Catégorie contient des Articles mais peut également contenir d'autres Catégories.


Section: permet d'appliquer une section qui sera utilisée par défaut lors de l'ajout des articles de cette catégorie sur un devis.

Taux de marge: permet de définir un taux de marge minimum recommandé (en %) quand l'article principal d'un devis fait partie de cette catégorie.

Ainsi, le système va aller comparer le taux de marge de la catégorie de l'article principal du devis au taux de marge du devis, si celui du devis est inférieur, cela bloquera la validation du devis.

Type de catégorie: permet de choisir entre Vue et Normale. Une catégorie de type Vue est une catégorie virtuelle qui sert de mère à d'autres catégories.

Article principal: si cette option est cochée, les articles de cette catégorie seront considerés comme articles principaux sur les commandes / factures clients.

## Partie Valorisation de l'inventaire


Il est possible de gérer la façon dont sont calculés les coûts des articles directement dans les catégories.

Ces paramètres sont utilisés lors de la génération du rapport de Valorisation de l'inventaire.

**Méthode de coût:** ce champ permet de définir le calcul utilisé :

- Prix standard : chaque produit sera évalué au coût que vous avez défini manuellement sur la fiche produit. Dans cette configuration, les entrées et les livraisons de marchandises n'auront aucun impact sur le coût de l'article.
- Prix moyen : chaque produit a la même valeur et cette valeur est calculée en faisant la moyenne entre les différents coûts d’achat. Avec cette méthode de calcul des coûts, le coût du produit est donc recalculé à chaque réception. Ainsi, les coûts ne sont pas simplement calculés à partir des remises appliquées sur la marque.
- Prix Réel : les produits sont évalués à leur coût d'achat. Lorsqu'un produit quitte le stock, c'est la règle FIFO (First In First Out) qui s'applique. Cela permet d’obtenir la valeur réelle de stock, sur le principe que les produits achetés en premier, sont les premiers à sortir du stock.


**Valorisation de l'inventaire:**si la valorisation perpétuelle est activée pour un produit, le système créera automatiquement des entrées comptables correspondant aux mouvements de stock, avec un prix de produit conforme à la méthode de valorisation des stocks. La variation du compte de stock établie sur la catégorie de produit représentera la valeur actuelle des stocks, le compte d'entrée et de sortie en stock présenteront la contrepartie des mouvements.

*Plus d'information sur*

[la valorisation des stocks](https://documentation.openfire.fr/knowsystem/valoriser-les-stocks-191)
## Partie Propriétés comptables

Cette partie permet entre autre de personnaliser les comptes de revenus et de dépenses utilisés pour les articles de cette catégorie:

Cela va permettre de générer les bonnes écritures comptables lorsqu'un article de cette catégorie est facturé.

Des comptes d'entrée et de sortie en stock peuvent être définis pour la comptabilisation de la dépréciation des stocks.

  *Plus d'information sur [la valorisation des stocks](https://documentation.openfire.fr/knowsystem/valoriser-les-stocks-191)*

## Partie Logistique

La section Logistique est liée à l'application inventaire. Elle permet de définir les routes et aussi les stratégies d'enlèvement.

Par défaut, OpenFire prend d'abord les stocks les "plus âgés" (méthode FIFO), mais ce comportement peut être modifié en Last In Last Out (LIFO):

La stratégie FIFO (First In First Out) repose sur le principe que les produits achetés en premier, sont les premiers à sortir du stock. Il s’agit d’une méthode de gestion des stocks dont l’objet est de faire sortir les marchandises et matières premières par ordre d’entrée en stock.

Le stratégie LIFO (Last In First Out) part du principe que les actifs produits ou achetés en dernier, sont les premiers à sortir à nouveau du stock. Autrement dit, cette méthode considère que l’entreprise se débarrasse en premier des produits acquis le plus récemment.

  *Plus d'informations sur [les routes](https://documentation.openfire.fr/knowsystem/routes-et-regles-de-stock-226)*