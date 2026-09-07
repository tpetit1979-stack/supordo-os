---
url: https://documentation.openfire.fr/knowsystem/immobilisations-223
url_finale: https://documentation.openfire.fr/knowsystem/immobilisations-223
date_collecte: 2026-09-06
destination: documentation_2
---

Une immobilisation est un bien inscrit à l’actif de l’entreprise et qui va servir l’activité de l’entreprise sur une durée supérieure à un exercice comptable.

Les immobilisations sont déduites des charges chaque année en répartissant leurs coûts sur une certaine durée. On parle d’amortissements.

## Créer une immobilisation

Il est possible de créer des Immobilisations depuis le menu **Comptabilité > Immobilisations >** **Immobilisations** :

En cliquant sur le bouton Créer, cela vous ouvrira le formulaire de création d'immobilisation, où vous pouvez entrer les détails de l'immobilisation.

Dans ce formulaire, vous pouvez entrer les informations sur l'actif immobilisé, telles que sa valeur, sa date d'acquisition, sa durée de vie estimée, etc...:

Différents champs sont a renseigner parmi lesquels:

- Immobilisation parente: permet de définir la catégorie de l'immobilisation. Cela permet de regrouper les immobilisations qui répondent aux mêmes critères (durée, etc.),

- Purchase Value: correspond à la valeur totale du bien,

- Asset Profile: correspond à des modèles d'immobilisation. Sur ces modèles il est possible de définir un compte d'immobilisation (218200 dans notre exemple), ainsi que la TVA à utiliser,

- Date d'amortissement: permet de préciser la date d'acquisition du bien, ainsi que la durée de l'amortissement,

- Méthode d'amortissement: permet de préciser la méthode de calcul des amortissements et de choisir d'utiliser ou non le prorata temporis (permet de prendre en compte le nombre de jour écoulé de l’année comptable et non l'année complète pour les premiers amortissements). L’amortissement est souvent linéaire (taux d’amortissement constant) mais la méthode de calcul peut être modifiée: La méthode de calcul d'amortissement en valeur résiduelle permet de soustraire la valeur résiduelle du coût initial de l'actif pour obtenir la base amortissable. Vous calculez ensuite la dépréciation annuelle de l'actif en utilisant un taux d'amortissement dégressif qui est appliqué à la base amortissable. Le taux d'amortissement dégressif est généralement plus élevé au début de la durée de vie utile de l'actif, et diminue progressivement au fil du temps. Cela signifie que l'amortissement est plus important pendant les premières années d'utilisation de l'actif, puis diminue progressivement au fil du temps. Cette méthode peut donc être utile pour les actifs dont la valeur diminue rapidement au cours des premières années, mais qui ont une valeur résiduelle importante à la fin de leur durée de vie utile.

Une fois que vous avez entré toutes les informations nécessaires, cliquez sur Sauvegarder pour enregistrer l'immobilisation. Cela générera l'immobilisation en statut Brouillon et l'ajoutera à votre liste d'immobilisations. Vous pouvez ensuite la confirmer.

  Plus d'information sur [le calcul des amortissements](https://documentation.openfire.fr/knowsystem/ammortissements-224)

## Hierarchie des amortissements

La hiérarchie des immobilisations est une fonctionnalité qui permet d'organiser les actifs de votre entreprise en une structure hiérarchique.

Elle permet de regrouper les actifs selon leur niveau d'appartenance à des catégories spécifiques, ce qui facilite la gestion des actifs et leur suivi.

Par exemple, vous pouvez organiser vos actifs en groupes tels que Véhicule, Machines, Informatique, etc...

Vous pouvez ensuite définir des sous-groupes pour chaque catégorie, comme Voitures de fonction, Véhicules de livraison, Matériel de bureau, Ordinateurs, etc...