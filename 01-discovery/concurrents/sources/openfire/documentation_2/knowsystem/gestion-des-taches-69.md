---
url: https://documentation.openfire.fr/knowsystem/gestion-des-taches-69
url_finale: https://documentation.openfire.fr/knowsystem/gestion-des-taches-69
date_collecte: 2026-09-06
destination: documentation_2
---

Les tâches permettent de définir les interventions que les techniciens seront amenés à faire et qui seront reprises dans les interventions du planning : ramonage, pose, visite technique… Les tâches peuvent ainsi être utilisées dans les cas ou vos employés ne sont pas habilités a effectuer certaines interventions. 

Les tâches sont consultables et configurables depuis le menu **Interventions > Configurations > Tâches**

## Création d'une tâche

A la création d'une tâche, plusieurs champs non obligatoires sont proposés:

Le champ produit lié permet d'associer un article du catalogue à cette tâche. Cet article sera utilisé via les fonctions de facturation depuis le planning.

 *Attention toutefois, la facturation est également possible depuis les modèles d’intervention. Si vous utilisez les modèles d'intervention pour gérer la facturation de vos interventions, il n'est pas nécessaire de le faire depuis les tâches.*

  Plus d'information sur les [modèles d'interventions](https://documentation.openfire.fr/knowsystem/modeles-dintervention-73)

Le champ Catégorie d'employés permet d'associer cette tâche a un groupe d'employé spécifique.




Le champ Durée par défaut permet de définir une durée utilisée par défaut lors de la saisie d’une intervention sur le planning. Il reste possible de modifier cette durée lors de la prise de rendez-vous.

La case Imprimer détail permet d'imprimer le détail de la tâche sur le planning.

Il est également possible de gérer la récurrence d'une tâche via la case Tâche récurrente :

Une périodicité par défaut peut ainsi être choisie. Cette périodicité sera alors utilisée par défaut lors de l’enregistrement des contrats d’entretien.

## Catégorie de tâche

Les tâches peuvent être catégorisées depuis le menu **Interventions > Configurations > Catégories de tâches**

- de rechercher plus facilement les interventions à réaliser sur un type de prestation

- d'évaluer le nombre d’heures restant à planifier sur une période par type de tâche (ex :il me reste 20 heures de poses disponibles sur le mois de juin).

Il est possible d'associer les tâches concernées à la catégorie via le bouton Ajouter un élément.

La granularité de planification permet, lors de la saisie d’une intervention à programmer, de calculer une plage de planification par défaut, en fonction de la date de démarrage saisie.


Dans l’exemple ci-contre, une granularité de 1 mois pour les tâches de type « Entretien » permet de définir la date de fin automatiquement au 30/04.