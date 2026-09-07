---
url: https://documentation.openfire.fr/knowsystem/terminer-une-intervention-95
url_finale: https://documentation.openfire.fr/knowsystem/terminer-une-intervention-95
date_collecte: 2026-09-06
destination: documentation_2
---

## Saisie des temps

Pour clôturer une intervention, cliquez sur le bouton Terminer disponible en bas de la fenêtre de détails de l'intervention.

Une fenêtre vous demandera confirmation. Vous pourrez ensuite, selon la configuration de votre base, saisir vos temps d'intervention.

En effet, vous pouvez choisir si vous souhaitez utiliser ou non le timer intégré à l'application pour le suivi des temps d'intervention.

Depuis la Configuration des Interventions sur le web, trois modes de saisie des temps sont disponibles :

- Pas de suivi : vous pouvez rentrer simplement la Durée réelle manuellement dans l'onglet Compte rendu de l'intervention ;
- Saisie manuelle : le technicien peut rentrer manuellement la durée depuis l'application mobile :
- Saisie automatique : permet d'activer le suivi via le timer

  *Plus d'information sur la [configuration des interventions](https://documentation.openfire.fr/knowsystem/configurations-generales-20)*

Une notion de Temps de trajet a également été intégrée dans l'intervention. Vous pouvez le remplir manuellement en back-office ou depuis le mobile avec le mode Saisie manuelle.

En cliquant sur la zone de texte, un compteur vous permet de sélectionner la durée de votre choix:

Vous pouvez décider de rendre ou non obligatoire la saisie des temps en activant le paramètre Suivi des temps obligatoire depuis la Configuration des Interventions qui bloquera la modification des données de l'intervention tant que le bouton Démarrer n'est pas cliqué.

## Le compte-rendu d’intervention

L'ensemble des informations (réponses aux questionnaires, photos, signatures, etc...) saisie lors de l'intervention est envoyée à la base OpenFire et peut être ajoutée aux fiches ou aux rapports d'intervention.

Les informations présentes sur ces fiches et rapports sont configurables depuis les modèles d’intervention.

Sur chaque modèle d'intervention, une option nommée Envoi des rapports permet alors de définir si l’envoi du rapport d’intervention au client doit être fait :

- manuellement depuis la base Web OpenFire,
- manuellement depuis l’application mobile dès que l’intervention est marquée comme terminée,
- ou automatiquement dès que l’intervention est marquée comme terminée. __Attention__ : cela nécessite que votre configuration pour envoyer des mails soit opérationnelle.

## Statut des interventions

Lorsque l'intervention est terminée, son statut change et l'intervention passe en Réalisé sur l'application mobile et en back office.

Les applications réalisées apparaissent alors avec un code couleur vert dans la vue jour et la vue planning.

Sur la base OpenFire, un bouton Clôturer sur votre intervention vous permet de bloquer sa modification depuis le mobile, quel que soit son statut.

Cliquez alors sur Ré-ouvrir pour la rendre de nouveau modifiable.

## Modification des interventions

Il est possible de modifier le RDV tant que celui-ci n'est pas réalisé ou clôturé et si les droits sont mis au niveau de la configuration>Intervention.

Si le RDV est en statut réalisé sur l'application mobile, il est quand même possible de le modifier en fonction des droits de l'utilisateur. Ce dernier doit :

- Aller sur le RDV concerné

- Cliquer sur les 3 petits points en haut à droite

- Cliquer Modifier un RDV ou Editer un RDV.

Le technicien pourra alors repasser le RDV en statut Confirmé et retourner sur le RDV pour le modifier.