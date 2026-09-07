---
url: https://documentation.openfire.fr/knowsystem/gerer-la-marge-et-les-remises-125
url_finale: https://documentation.openfire.fr/knowsystem/gerer-la-marge-et-les-remises-125
date_collecte: 2026-09-06
destination: documentation_2
---

OpenFire permet de gérer vos remises commerciales de différentes façons.

Sur chaque devis, il est possible de modifier le prix d'un article manuellement ou encore d'y appliquer une remise. Néanmoins, deux outils vous permettent de simplifier la gestion des remises:

- l'outil de gestion des prix
- l'utilisation des listes de prix

## Ajout manuel d'une remise

Il est possible d'ajouter "manuellement" une remise de deux façons :

- En changeant le prix de la ligne du devis et en ajoutant un commentaire dans la description de cette ligne, par exemple :

Ce qui donne le résultat suivant :

- Il est également possible d'utiliser le champ dédié Remise disponible pour chaque ligne de commande :

Ce qui donne le résultat suivant :

En complément, il existe un outil dédié de Gestion de prix qui permet davantage d'options et qui est présenté ci-dessous.

## Outil de gestion des prix

L'outil de gestion des prix vous permet de gérer vos remises ou vos marges depuis un menu unique. Vous avez la possibilité de mettre à jour le prix des lignes d'un devis en une seule étape et de simuler les marges obtenues en appliquant telle ou telle remise.

Ce menu est disponible depuis les devis ou les bons de commandes via le bouton dédié Gestion Prix :

Dans la fenêtre qui s'ouvre, vous avez alors la possibilité de gérer vos remises via différents champs et modes de calcul :

Le champ Mode de remise vous permet de choisir si vous souhaitez que la remise apparaisse sur les montants totaux du devis ou non:

- Le choix Appliquer la gestion de prix dans les lignes permettra d'appliquer les remises directement dans les lignes d'articles du devis. Une note pourra alors être ajoutée pour indiquer le montant de la remise en cochant l'option Afficher dans les notes (voir un peu plus bas) ;

- Le choix Appliquer la gestion de prix dans les totaux permettra d'afficher dans le devis une ligne Article de Remise qui portera toutes les remises. Les autres lignes de la commande resteront alors inchangées :

Le champ Base de calcul vous permet de décider si vous souhaitez calculer vos remises et marges par article ou par section de devis (disponible seulement si vous disposez des sections avancées sur votre base et qu'elles sont activées. Rapprochez-vous du support Openfire si nécessaire).

Le champ Mode de calcul vous permet de sélectionner la façon dont la réduction sera calculée.

  Vous pouvez utiliser cet outil afin de mettre à jour le prix des articles du devis et les remettre au prix actuel des articles sur votre base. Utile en cas de mise à jour des prix d'un fournisseur. Pour cela, sélectionnez Base de calcul: Articles et Mode de calcul: remettre au prix magasin

Une fois votre remise sélectionnée, vous pouvez sauvegarder, puis cliquer sur Simuler afin de vérifier le résultat de ce changement.

Le résultat de la simulation apparait alors:

Si tout est bon pour vous, vous pouvez alors cliquer sur Appliquer au Devis/Bon de commande.


Vous avez également la possibilité d'exclure des articles lors du calcul:

L'option afficher dans les notes permet d'ajouter automatiquement une note sur la remise appliquée dans le devis :

La marge présente en bas du devis est une marge calculée sur le montant HT. Elle fait la moyenne des marges de l'ensemble des lignes du devis/bon de commande.


La marge des lignes d'articles est calculée soustrayant le cout HT d'un article à son prix de vente HT.

## Liste de prix

Les listes de prix vous permettent de gérer des tarifications différentes par groupe de contacts mais aussi par devis.

Vous pouvez y accéder depuis le menu **Ventes > Configuration > Liste de prix**

 *Plus d'information sur [les Listes de prix](https://documentation.openfire.fr/knowsystem/gerer-les-listes-de-prix-150)*