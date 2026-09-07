---
url: https://documentation.openfire.fr/knowsystem/creer-et-personnaliser-un-widget-256
url_finale: https://documentation.openfire.fr/knowsystem/creer-et-personnaliser-un-widget-256
date_collecte: 2026-09-06
destination: documentation_2
---

Dans l'application Dashboard, chaque tableau peut être personnalisé pour contenir des Widgets. Les widgets sont des composants visuels qui peuvent prendre différentes formes, comme des boutons, des listes déroulantes, des cases à cocher, des graphiques, des cartes, etc...

## Les types de Widget

Depuis le tableau de votre choix, cliquez sur le bouton Ajouter et choisissez votre type d'indicateur que vous souhaitez créer.

Voici les principaux type de Widget disponibles :

- Tile: Ce bloc permet d'afficher des indicateurs importants sous forme de nombres, de pourcentages ou d'autres mesures quantitatives.

- Graphique en Barres : Permet d'afficher les valeurs sur un graphique en barres verticales

- Horizontal Bar Chart: Permet d'afficher les valeurs sur un graphique en barres honrizontales

- Courbe (Line Chart): Permet d'afficher les valeurs sur un graphique linéaire

- Zone de Graphique: Il s'agit d'un graphique linéaire (ou en courbe) où chaque valeur est représentée par une aire de couleur au lieu d'une simple ligne.

- Pie Chart: permet d'afficher les valeurs sur un graphique circulaire (ou en secteurs)

- Doughnut Chart: permet d'afficher les valeurs sur un graphique en anneau.

- Polar Area Chart: permet d'afficher un diagramme de zones polaires. Ils sont similaires aux diagrammes circulaires, mais chaque segment a le même angle - le rayon du segment diffère en fonction de la valeur.

## Saisie des Informations

La création d'un indicateur nécessite les informations suivantes :

- Name : le nom de l'indicateur et qui sera affiché dans le menu créé,
- Model : il s'agit du modèle de base de données que vous souhaitez exploiter pour faire votre analyse ( Exemple : Bon de commande pour réaliser un indicateur sur les données qui se trouvent dans les bons de commandes),
- Company : il s'agit de la société sur laquelle vous souhaitez calculer l'indicateur. Ce champ n'est pas obligatoire,
- Type : il s'agit du type de présentation graphique (linéaire, barre, fromage,...),
- Set Update Interval : il s'agit de l'intervalle de calcul de l'indicateur. Ce champ peut être vide.

Dans l'onglet Data, vous pouvez spécifier l'indicateur : type d'opération (addition, comptage,...) et le type de filtre à appliquer. Les champs seront différents en fonction du type d'indicateur sélectionné.

Dans le cas du type d'indicateur Title, les champs sont :

1 - Record Count Type : ce sera le type d'opérateur de calcul : un comptage (count), une somme (sum) ou une moyenne. Dans notre cas, le logiciel comptera le nombre de bon de commande. Au fur et à mesure que vous changer le champs, le champ Record Value est modifié car il s'agit du résultat de l'application de cet opérateur.

2 - Au fur et à mesure que vous modifiez, vous avez un aperçu écran en haut à droite,

3 - la partie Filter permet de définir le ou les filtres que vous souhaitez appliquer. Il s'agit du même principe que les filtres présents dans chaque menu du logiciel tel que les bons de commande ou les factures.

Il faut sélectionnez le champs à filtrer et vous définissez ensuite la condition.

Exemple : Date Filter Field : Date de création (du bon de commande) et Date Filter Selection : Cette année.

Le domaine est le nom technique de ce qui nous permet de définir un périmètre d'analyse. Cela permet de créer un domaine de recherche.

  *Plus d'informations sur [la notion de domaine](https://documentation.openfire.fr/knowsystem/notion-de-domaine-et-python-288)*

## Personnalisation des Widgets

Chaque Widget peut être modifié en cliquant sur l'icone suivante, disponible au survol de la souris:

Le rendu des Widgets peut ensuite être modifié et personnalisé via l'onglet Display :

Pour les Widgets de type Tile, différentes modifications et différents thèmes sont possibles.

Le menu déroulant Layout permet de sélectionner un modèle de mise en page. Chaque modèle peut ensuite être personnalisé (couleur de fond, couleur de police, etc...) :

Pour les Widget de type Graphique, il existe divers palette de couleurs disponibles qui permettent de changer les teintes présentes dans le graphique.

En complément il est possible de faire apparaitre des données complémentaires sur les graphiques, comme les valeurs et l'unité de mesure.

Voici quelques exemples de paramétrages possibles: