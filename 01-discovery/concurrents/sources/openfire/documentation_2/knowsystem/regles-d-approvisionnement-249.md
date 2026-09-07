---
url: https://documentation.openfire.fr/knowsystem/regles-d-approvisionnement-249
url_finale: https://documentation.openfire.fr/knowsystem/regles-d-approvisionnement-249
date_collecte: 2026-09-06
destination: documentation_2
---

Les règles d'approvisionnement permettent de définir les conditions qui déclenchent la création d'une commande d'achat ou d'un transfert de stock. 

Par exemple, elles peuvent être utilisées pour déclencher une demande de prix lorsque le stock atteint un niveau minimum. Cela peut permettre d'anticiper les pénuries liées aux délais d'approvisionnement:

Les règles d'approvisionnement sont également liées aux routes d'approvisionnement qui permettent de déterminer les itinéraires que les articles vont suivre pour passer d'un emplacement à un autre.

  *Plus d'informations sur [les routes](https://documentation.openfire.fr/knowsystem/routes-et-regles-de-stock-226)*

## Présentation globale des règles d'approvisionnement

Voici les différents principes possibles:

- Achat : un bon de commande client (ou une autre règle) déclenche la création des ordres d'achat pour les produits à livrer ;
- Règles de flux poussés : la réception d'un produit dans un emplacement de l'entrepôt déclenche son transfert vers un autre emplacement. Le flux poussé consiste donc à produire un bien avant qu’un besoin particulier n’ait été formulé par un client. Une fois le processus de production terminé, le produit sera stocké en attendant qu’un client ne l’achète.
- Règles de flux tirés : un bon de commande client (ou une autre règle) déclenche un transfert depuis un autre emplacement. 
Dans cette organisation, c’est la demande d’un client qui sera l’élément déclencheur d’une mise en fabrication d’un produit.
- Règles de flux tirés et poussés : un bon de commande client déclenche une demande de transfert vers un autre emplacement et un deuxième transfert à leur réception, vers l'emplacement de stock.

## Modes d'application des règles d'approvisionnement

Dans OpenFire, un approvisionnement peut être déclenché par différentes opérations :

- Approvisionnement suite à une commande client : pour chaque commande client validée, un approvisionnement est créé à l’emplacement client par article commandé. Le client doit effectivement être livré ;
- Approvisionnement en fonction des règles de stock minimum : pour chaque article, des règles de stocks minimum peuvent être définies ;
- Ordre d’approvisionnement : un approvisionnement manuel peut être généré pour chaque article.

  *Plus d'informations sur [les ordres d'approvisionnement](https://documentation.openfire.fr/knowsystem/ordre-d-approvisionnement-253)*

Les règles de stock peuvent être définies pour des produits individuels ou pour des catégories de produits.

Au niveau de la fiche article, ce sont les routes qui permettent d'appeler des règles de stock, en cochant ou décochant les routes voulues selon les schémas suivants :

**__Cas 1 - Seule la route Acheter est cochée :__** Cela génère simplement le bon de livraison pour l’article.

**__Cas 2 - Les routes Acheter et Approvisionner à la commande sont cochées :__** cela génère la demande de prix automatiquement qu’importe le stock.

Cette règle d'approvisionnement à la commande (souvent nommée MTO pour Make To Order) consiste à générer, pour chaque commande client validée, une ou plusieurs demandes de prix fournisseur relatives aux articles vendus au client.

A savoir :

- Le système génère une demande de prix par fournisseur ;
- Les quantités proposées dans la demande de prix correspondent aux quantités vendues au client (pas d’interrogation des stocks disponibles).

**__Cas 3 - Seule la route Approvisionner à la commande est cochée :__** cela permet de générer la demande de prix uniquement s'il n'y a pas suffisamment de produits disponibles en stock.

Ce type de configuration est souvent appelé MTS pour Make To Stock. Dans cette configuration, la validation de la commande client génère donc le bon de livraison client.

Ce bon de livraison indique notamment l’état de disponibilité stocks des articles vendues :

- Article en attente de disponibilité : un approvisionnement est nécessaire ;
- Article disponible : les quantités en stock peuvent être réservées pour la commande.

  *Plus d'informations sur la [génération du Bon de Livraison](https://documentation.openfire.fr/knowsystem/generation-du-bon-de-livraison-59)*

Ce fonctionnement nécessite que des règles de stocks minimum soient également définies sur la fiche de l'article.

  *Plus d'informations sur les règles de stocks*

 Pour que les routes désirées puissent être appliquées aux bons de commande client existants, il faut au préalable créer une règle de réapprovisionnement pour chaque produit, avec les quantités min et max à zéro.

  *Plus d'informations sur [les ordres d'approvisionnement](https://documentation.openfire.fr/knowsystem/ordre-d-approvisionnement-253)*

**Attention:**

*une option disponible dans le menu Inventaire > Configuration > Configuration permet de réserver un article dans le bon de livraison dès lors qu'il est en stock, et ce qu'importe les règles d'approvisionnements. Dans le cas où vous livrez uniquement à la contremarque, il est nécessaire de contacter OpenFire afin de modifier les règles de votre base.*

## Quantités Minimum et Maximum

Comme nous l'avons vu, lorsque vous commandez un bien, différentes règles d'approvisionnements peuvent être utilisées. Il est par exemple possible de définir un niveau de stock minimum qui, une fois atteint, déclenche le réapprovisionnement.

Ces règles de stocks peuvent se définir à deux endroits :

- Depuis la fiche article :

- Depuis le menu **Inventaire > Contrôle d’inventaire > Règle de réapprovisionnement > créer**

Une règle de stock est définie comme suit :

Nom : nom de la règle de stock.

Article : référence de l’article concerné par la règle.

Entrepôts : définit l’entrepôt dans lequel les articles doivent être livrés.

Lieu : emplacement de destination du réapprovisionnement.

Groupe d’approvisionnement : permet d’associer la règle à un groupe d’approvisionnement existant. Les mouvements créés en passant par cette règle de réapprovisionnement seront automatiquement mis dans ce groupe d’approvisionnement. Si aucun groupe n’est défini, les mouvements générés par les règles d’approvisionnement seront regroupés en une seule préparation.

Quantité minimum : quantité minimum de stock à prévoir pour cet article. Quand le stock virtuel tombe en dessous de la valeur minimum renseignée ici, le système génère un approvisionnement pour ramener le stock à la valeur maximum définie.

Quantité multiple : Le réassort proposé sera arrondi en fonction de cette valeur multiple. Si cette valeur est à zéro, la quantité exacte sera utilisée.

Délai : au choix parmi les options suivantes:

- Jour pour acheter : correspond au nombre de jours que le fournisseur met à traiter la commande ;
- Jour pour recevoir les produits : Ce délai permet de définir le délai de déclenchement de la règle.