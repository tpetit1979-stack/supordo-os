---
url: https://documentation.openfire.fr/knowsystem/consulter-mes-stocks-225
url_finale: https://documentation.openfire.fr/knowsystem/consulter-mes-stocks-225
date_collecte: 2026-09-06
destination: documentation_2
---

Pour suivre votre stock sur OpenFire, il existe différentes possiblités:

- Vous pouvez visualiser les détails de votre stock, tels que le nom du produit, la quantité en stock, la quantité minimale, la quantité maximale, etc,
- Vous pouvez également utiliser les rapports de stock tels que l'inventaire à la date,
- Vous pouvez également visualiser les mouvements de stock pour chaque produit en cliquant sur le bouton "Mouvements" dans la fiche produit.

*Notez que pour pouvoir suivre votre stock de manière efficace, il est important de configurer correctement les paramètres d'inventaire dans OpenFire et d'effectuer régulièrement des mouvements de stock, tels que des transferts internes ou des ajustements de stock.*

## Vue du stock depuis l'article


            __Dans la vue liste des articles, différentes valeurs sont disponibles:__

- Quantités réelles : correspond au stock que j’ai physiquement dans mon stock
- Quantités sortantes : correspond aux quantités d'articles présents sur un bon de livraison (et qui vont donc sortir du stock)
- Quantités Entrantes : correspond aux quantités d'articles en attente de réception (et qui vont donc sortir du stock)
- Quantités Prévues : correspond à mes quantités réelles auxquels je soustrais mes quantités sortantes et j'additionne mes quantités entrantes (= stock total - ce que j’ai vendu mais pas encore livré + ce que j’ai commandé mais pas encore reçu).

__Depuis les bons de commandes:__

Les informations de stock sont également visibles dans les lignes de commandes :

- Stock total = correspond au stock que j’ai physiquement dans mon entrepôt
- Stock dispo = correspond à mon stock total moins mon stock réservé
- Stock théorique = stock total - ce que j’ai vendu mais pas encore livré + ce que j’ai commandé mais pas encore reçu.

__Depuis la fiche Article:__

Les quantités de stock et les quantités prévisionnelles sont disponibles depuis les boutons en haut à droite:

## Évolution des stocks

Pour illustrer l'évolution des stocks dans OpenFire, prenons comme exemple l'évolution des quantités de stock sur les poêles Lune. Je dispose initialement de 4 poêles en stock.

Étape1: Je valide la vente d'une unité de cet article et un bon de livraison est créé.

Les prévisions affichent alors 3 Articles:

- 4 en stock
- 1 à sortir
- 0 à réceptionner

Étape 2 : Je souhaite garder mes 4 poêles en stock. J'approvisionne donc mon bon de livraison et je créer un bon de réception.

Les prévisions affichent alors 4 Articles:

- 4 en stock
- 1 à sortir
- 1 à réceptionner

Étape 3 : Je valide mon bon de réception.

Les prévisions affichent alors 4 Articles, répartis comme tel:

- 5 en stock
- 1 à sortir
- 0 à réceptionner

Étape 4 : Je pose le poêle chez mon client. Je valide donc mon bon de livraison.

## Inventaire à la date

Le rapport Inventaire à la date vous permet d’avoir une vue sur son stock actuel ou à une date précise. 

Pour y accéder, rendez vous dans le menu Inventaire > Rapports > Inventaire à la date

*Attention, sur certaines bases, l'accès a ce menu peut nécessiter l'activation du mode Développeur.*

*Pour cela,  rendez-vous dans l’onglet Configuration puis cliquez sur l’option Activer le mode développeur à droite :*


*De nouveaux menus apparaitront alors.* 

Cocher alors la case Inventaire à la date et choisissez la date d'analyse de votre choix:

Puis, cliquez sur Valoriser le stock.

Une fois le résultat affiché, un filtre par défaut nommé Article > Lieu est appliqué. Vous pouvez le retirer afin de filtrer les résultats selon vos propres critères.

 

Vous pouvez par exemple grouper vos résultats par emplacement afin d'exporter votre valorisation de stock au format Excel.

Exporter toutes les lignes en utilisant le modèle d'export ci dessous:

Une fois exporté, vous pourrez alors appliquer un tableau croisé dynamique dans Excel pour retrouver vos valeurs, par emplacement, par catégories, par marque, par articles, etc...

Pour cela, sélectionnez vos colonnes, puis cliquez sur **Insertion > Tableau croisé dynamique** :

Vous pourrez alors créer un tableau croisé sur une nouvelle feuille Excel:

Une fois le tableau créé, il ne vous restera qu'a sélectionner les données qui vous intéresse:

## Mouvement de stock

Les mouvements de stock dans OpenFire sont des opérations qui affectent la quantité de produits disponibles dans un emplacement de stock particulier.

Ils peuvent inclure des opérations telles que les entrées de stock (par exemple, lorsqu'un produit est reçu), les sorties de stock (par exemple, lorsqu'un produit est vendu), les transferts de stock (par exemple, lorsqu'un produit est transféré d'un emplacement de stock à un autre) et les ajustements de stock (par exemple, lorsqu'une correction de quantité est nécessaire).

  Plus d'informations sur [les mouvements de Stock](https://documentation.openfire.fr/knowsystem/mouvement-de-stocks-248)