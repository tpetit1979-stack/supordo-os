---
url: https://documentation.openfire.fr/knowsystem/gerer-les-kits-4
url_finale: https://documentation.openfire.fr/knowsystem/gerer-les-kits-4
date_collecte: 2026-09-06
destination: documentation_2
---

Vous avez la possibilité de vendre des articles de manière groupée, par l'utilisation des kits. Dans OpenFire, un kit est un ensemble de composants regroupés dans le but de :

- Simplifier la lecture du devis et de la facture par le client,
- Permettre un traitement forfaitaire de fournitures techniques,
- Éviter les ambiguïtés sur les éléments consommés en plus ou en moins.

## Créer un kit

Vous pouvez créer les kits depuis le menu **Ventes > Ventes > Articles** ou via Ventes > Ventes > **Kits.**

Un kit est vu dans OpenFire comme un produit à part entière. A ce titre, la plupart des champs a renseigner sont donc identiques à ceux de la création d'article standard.

  Plus d'information sur [la création d'article](https://documentation.openfire.fr/knowsystem/creer-un-article-6)

Quelques étapes propres aux kits sont a suivre:

1. Création de l’article « Kit »: une case à Cocher permet de définir si l'article est un kit

  Si vous créez le kit depuis Articles, vous devez cocher la case est un kit. Néanmoins, si vous créez le kit depuis Ventes > Kits, l'article est automatiquement créé comme un kit.

2. Affectation des composants du kit dans l’article lui-même;

Les quantités utilisées sont définies pour chaque ligne de composant.

Une fois les composants ajoutés, le prix de l'ensemble des composants du kit est alors visible dans information générale, via le champ Prix compos/kit.



3. Ajustement du tarif du kit.

La section Kits de l'onglet Information Générale va vous permettre de gérer la tarification du kit.

Cette section vous permet de définir le mode de gestion du prix du kit:

- en tarification calculée : la somme des composants est le prix du kit,

- en tarification fixée : le prix sera celui que vous définissez dans Prix de vente. 

Il est plutôt conseillé d’utiliser le mode de tarification calculé sur vos kits. Cela permet que le prix des kits soit automatiquement mis à jour lorsque le prix de ses composants change.

## Utiliser les kits dans les devis

Le kit s'ajoute dans un devis de la même manière qu'un autre article.

Le mode de tarification  (calculée ou fixée) et les composants (via le bouton Voir Composants) sont également  disponibles depuis la fenêtre d'ajout des articles. Il est alors possible de modifier la composition du kit et de changer le prix (qu'il soit calculé ou fixé).

#### Un produit utilisant une nomenclature de kit apparaîtra sous la forme d'un élément de ligne unique sur un devis et une commande client, mais générera un bon de livraison avec un élément de ligne pour chacun des composants du kit.




Il est également possible de faire apparaitre tous les composants du kit au devis avec leurs prix unitaires. Cela permet d'afficher le prix de chaque élément dans le devis comme s'ils avaient été ajoutés manuellement.

Pour cela, cliquez sur Ajout composants Kit :

Dans la fenêtre suivante, il suffira de sélectionner le kit a importer. Si besoin il est alors possible de désélectionner des composants:

## Mode d'impression

 Dans l'onglet **Impression** du devis, vous avez la possibilité de changer le mode d'impression du kit. 

L'option Mode d'impression permet de faire apparaitre ou non les descriptions des kits sur les devis et bon de commande.

- Le mode d'impression par défaut est Étendu. Ce mode signifie que vous voyez le détail du kit dans le devis imprimé.

- Le mode Restreint permet d'afficher une ligne par kit avec information minimale ;

- Vous avez la possibilité de cacher les descriptions en sélectionnant Aucun dans le menu déroulant suivant.


 

Plus d'information sur__[l'impression du devis](https://documentation.openfire.fr/knowsystem/parametrer-l-impression-du-devis-129)__