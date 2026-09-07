---
url: https://documentation.openfire.fr/knowsystem/gerer-les-periodes-comptables-170
url_finale: https://documentation.openfire.fr/knowsystem/gerer-les-periodes-comptables-170
date_collecte: 2026-09-06
destination: documentation_2
---

Les périodes comptables dans OpenFire correspondent à des périodes de référence sur lesquelles les filtres, rapports et statistiques seront basés. Elles vous aideront à effectuer des recherches plus facilement au niveau des filtres.

Les périodes comptables peuvent être créées soit ligne par ligne, soit en effectuant une génération automatique.

## Périodes comptables

*Accès : Comptabilité>Configuration>Périodes Comptables*

Les périodes comptables sont à créer ligne par ligne. Il faut définir toutes les périodicités possibles en commençant par l'exercice annuel qui est le plus souvent l'exercice fiscal. Il existe par défaut 3 types de période comptable : Année, Mois ou Quinzaine.

## Génération automatique des périodes comptables

*Accès : Comptabilité>Configuration>Generate Date Ranges ou Générer les périodes comptables*

Il permet de générer plusieurs périodes en fonction de critères communs :

 - **Préfixe du nom de la période** : sélectionnez le préfixe du nom de la période. Exemple : "2023 - " : permet de définir le préfixe à utiliser pour le nommage des périodes générées.

 - **Durée** : durée de la périodicité en année, mois, semaine ou jour qui sera générée.

 - **Nombre de périodes comptables à générer** : le nombre de fois que vous souhaitez générer la "durée" ou la "périodicité".

 - **Type** : type de période comptable : par défaut : année fiscale, mois fiscale ou quinzaine civile

 - **Date de début** : date du début de la génération des périodes comptables

 - **Parent** : en option, si vous souhaitez affecter une année fiscale sur un mois fiscal.

 

Dès que les renseignements sont remplis, il faut cliquer sur SOUMETTRE.

Dans notre exemple ci-dessus, le logiciel génèrera 12 mois fiscaux : "2023 - 01" à "2023 - 12"


## Types de période comptable

*Accès : Comptabilité>Configuration>Types de Période Comptable*

Les types de période comptable servent à la génération des périodes relatives à vos exercices fiscaux. Vous pouvez également créer une période de référence de votre choix, en sélectionnant une périodicité et des dates de début et de fin.

Deux types de périodes sont proposées par défaut :

- L’année fiscale : elle correspond à l’exercice fiscal
- Le mois fiscal : il correspond aux périodes mensuelles composant l’exercice fiscal

Description des champs :

− Chevauchement autorisé : si coché, deux périodes de différents types ne peuvent pas se superposer. Exemple si coché : il ne sera pas possible de créer une période 1er semestre 2020 de type Semestre et une période "2020 - 06" car elle se superpose.

− Est un mois fiscal : période mensuelle de l’exercice. Non éditable par l’utilisateur.

− Est une année fiscale : période annuelle de l’exercice. Non éditable par l’utilisateur

− Société : société concernée par la période. Si la période est attribuée à plusieurs sociétés de la base, ne pas spécifier de société en particulier dans ce champ.