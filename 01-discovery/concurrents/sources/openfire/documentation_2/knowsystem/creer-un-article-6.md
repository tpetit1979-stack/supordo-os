---
url: https://documentation.openfire.fr/knowsystem/creer-un-article-6
url_finale: https://documentation.openfire.fr/knowsystem/creer-un-article-6
date_collecte: 2026-09-06
destination: documentation_2
---

La liste des Articles regroupe l’ensemble des articles et des prestations existantes. Ainsi, vous y retrouverez vos articles, composants et prestations, mais aussi celles de vos fournisseurs. 

Les articles sont disponibles via les menu Ventes > Ventes > Articles et Achats > Achats > Articles

## Créer un article

 

Les articles peuvent être créés depuis le menu des articles via le bouton Créer ou depuis un devis via le bouton Créer et modifier :

Les éléments suivants peuvent alors être définis :

Nom de l’article: désignation commerciale qui apparaîtra sur les devis.

Type d’article: au choix parmi:

- Produit stockable : article physique pour lesquels la gestion de stock est activée.
- Service : article de type Prestation de service / main d'œuvre.
- Consommable : article physique pour lequel on ne suit pas l'inventaire. Il existe quand même des mouvements de stock pour les articles de type "consommable" mais ils ne seront pas comptabilisés pour l'inventaire.

Marque: pour toutes vos prestations, la marque sera votre société.

  Plus d'information sur [les marques](https://documentation.openfire.fr/knowsystem/parametrer-une-marque-5)

Référence interne: code article / référence du fournisseur. Celle-ci doit être unique pour l’ensemble de vos articles.

Catégorie Interne: Famille à laquelle se rattache l’article. 

C'est un champ important pour les éléments suivants :

- Statistiques
- Imputations comptables
- Calcul des conditions tarifaires
- Imputation des normes

Coût : prix d’achat transmis au client si vous transmettez des tarifs au prix d’achat HT.

Prix de vente : prix de vente HT transmis au client distributeur.

Remise interdite : si cochée, aucune remise ne sera acceptée pour cet article dans le contexte du devis.

Date du tarif : date de mise à jour du tarif, fortement conseillée afin de connaître la date de dernière mise à jour. Cela présente également une facilité pour filtrer les données articles.

Prix public HT : prix public HT récupéré dans la base du fabricant.

Prix d’achat : prix d’achat calculé à partir des conditions de remises notées dans la marque.

## Onglet Inventaire

L'onglet Inventaire vous permet de paramétrer diverses informations concernant la gestion de stock de l'article.

Vous pouvez y définir les routes que l'article empruntera, de son achat à sa livraison, son suivi, son poids, son volume, etc.

Plus d'information sur les __Routes__

## Onglet Ventes


        C'est dans cet onglet que vous pouvez renseigner les garanties éventuelles des articles, son délai de livraison au client, ainsi que la structure de son prix.

## Onglet Facturation

Vous pouvez définir vos politiques de taxe et de facturation :

  Plus d'information sur [les Politiques de facturation](https://documentation.openfire.fr/knowsystem/politique-de-facturation-141) 

## Onglet Articles liés


        Si vous faites de la vente en ligne via votre site web, cet onglet vous servira à définir des articles qui s'achètent avec l'article original.

 Plus d'information sur Rendre un article disponible sur le site

## Onglet Technique



Vous retrouverez ici les champs qui correspondent à la qualification technique des produits de la cheminée.

Ces valeurs seront alors reprises dans la description de l’article au niveau du devis.

## Onglet Notes

La description pour les devis vous permet de définir des descriptions additionnelles qui seront reprises par défaut dans vos devis. Elle sera modifiable lors de la création du devis.

De même, le champ Description du Fabricant peut également être complété et apparaitre sur les devis. Généralement ce champ est plutôt utilisé par les fabricants pour ajouter des notes sur les articles centralisés.

Par défaut les champs Description pour les fournisseurs et pour le ramassage n'apparaitront par contre pas sur les devis.

Avertissements: Cet encart offre la possibilité d'appliquer un message d'avertissement ou bloquant sur un article.

- Avertissement : transmet le message à l’utilisateur lors de la saisie de l’article dans la ligne du devis.

- Message Bloquant : transmet le message à l’utilisateur lors de la saisie de l’article dans la ligne du devis et bloque la possibilité d’utiliser l’article.

## Onglet Images


        Vous pouvez ajouter des images de votre article dans cet onglet. Elles apparaîtront à l'impression du devis.