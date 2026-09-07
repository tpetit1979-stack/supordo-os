---
url: https://documentation.openfire.fr/knowsystem/valoriser-les-stocks-191
url_finale: https://documentation.openfire.fr/knowsystem/valoriser-les-stocks-191
date_collecte: 2026-09-06
destination: documentation_2
---

La valorisation des stocks est un processus très important qui va permettre :

- d'évaluer le montant des stocks des différentes matières premières et marchandise,
- d'évaluer les produits les plus anciens,

Il s'agit de suivre les entrées et les sorties pour connaître en temps réel la valeur effective des stocks de produits.

## Valoriser son stock

Voici la procédure à suivre pour faire une valorisation de stock à date sans passer par un inventaire physique.

Rendez vous dans le menu **Inventaire > Rapports > Inventaire à la date**

*Attention, sur certaines bases, l'accès a ce menu peut nécessiter l'activation du mode Développeur.*

Ce rapport d’inventaire permet d’avoir une vue sur son stock actuel ou à une date précise. 

Cocher alors la case Inventaire à la date et choisissez la date d'analyse de votre choix:

Puis, cliquez sur Valoriser le stock.

Une fois le résultat affiché, un filtre par défaut nommé Article > Lieu est appliqué. Vous pouvez le retirer afin de filtrer les résultats selon vos propres critères.

 

Vous pouvez par exemple grouper vos résultats par emplacement afin d'exporter votre valorisation de stock au format Excel. Pour cela, cliquez sur Grouper par et décochez Articles.

Exporter toutes les lignes en utilisant le modèle d'export ci dessous:

Une fois exporté, vous pourrez alors appliquer un tableau croisé dynamique dans Excel pour retrouver vos valeurs, par emplacement, par catégories, par marque, par articles, etc...

Pour cela, sélectionnez vos colonnes, puis cliquez sur Insertion > Tableau croisé dynamique :

Vous pourrez alors créer un tableau croisé sur une nouvelle feuille Excel:

Une fois le tableau créé, il ne vous restera qu'a sélectionner les données qui vous intéresse:

## Partie Valorisation de l'inventaire


Deux méthodes de valorisation d'inventaire sont disponibles dans le menu **Inventaire > Configuration > Configuration**:

La valorisation d’inventaire périodique est utilisée par défaut. La valorisation perpétuelle, qui génère une écriture comptable par mouvement de stock, étant réservée aux utilisateurs avancés.

Il est également possible de définir la méthode de comptabilisation de l'inventaire dans le menu **Achat > configuration > configuration**. Le choix de la méthode de coût définira alors la valeur retenu pour l’inventaire.

**Méthode de coût:** 

- Mettez un prix coûtant pour chaque produit : Dans ce cas, la valeur retenue pour l’inventaire sera celle indiquée dans le champ « coût » de la fiche article.

- Utilisez une méthode de prix coutant : Fixe, Réel, Moyen : dans ce cas, la méthode de coût est effectué par catégorie d’article.


En effet, il est possible de gérer la façon dont sont calculés les coûts des articles directement dans les catégories d'article. 

Ces paramètres sont utilisés lors de la génération du rapport de Valorisation de l'inventaire:

- Prix standard : chaque produit sera évalué au coût que vous avez défini manuellement sur la fiche produit. Dans cette configuration, les entrées et les livraisons de marchandises n'auront aucun impact sur le coût de l'article.
- Prix moyen : chaque produit a la même valeur et cette valeur est calculée en faisant la moyenne entre les différents coûts d’achat. Avec cette méthode de calcul des coûts, le coût du produit est donc recalculé à chaque réception. Ainsi, les coûts ne sont pas simplement calculés à partir des remises appliquées sur la marque.
- Prix Réel : les produits sont évalués à leur coût d'achat. Lorsqu'un produit quitte le stock, c'est la règle FIFO (First In First Out) qui s'applique. Cela permet d’obtenir la valeur réelle de stock, sur le principe que les produits achetés en premier, sont les premiers à sortir du stock.

- Valorisation de l'inventaire: Si la valorisation perpétuelle est activée pour un produit, le système créera automatiquement des entrées comptables correspondant aux mouvements de stock, avec un prix de produit conforme à la méthode de valorisation des stocks. La variation du compte de stock établie sur la catégorie de produit représentera la valeur actuelle des stocks, le compte d'entrée et de sortie en stock présenteront la contrepartie des mouvements.

Le coût pour les ventes permet l'ajout d'un champ supplémentaire sur les articles afin que le coût utilisé pour les devis et les ventes soit bien le prix actuel de l'article et non pas son coût moyen, permettant d'avoir un marge correcte en se basant sur le coût actuel du produit.