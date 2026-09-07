---
url: https://documentation.openfire.fr/knowsystem/modeles-dintervention-73
url_finale: https://documentation.openfire.fr/knowsystem/modeles-dintervention-73
date_collecte: 2026-09-06
destination: documentation_2
---

L'utilisation des **modèles d'interventions** permet de simplifier la création des rendez-vous et des demandes d'interventions.

Les modèles d'intervention permettent une saisie rapide des interventions en chargeant un certain nombre d’informations préalablement configurées selon le type d’intervention : VT, Entretien Granulés, etc.

Ces modèles sont configurables depuis le menu **Intervention > Configuration > Modèles d'interventions.**

*Toute modification d’un modèle de rapport, quelle qu’elle soit, ne sera répercutée que sur les interventions créées à posteriori. Aucune modification ne sera transmise aux interventions créées avant.*

## Configuration

Le champ Type d'intervention permet de sélectionner l'un des 5 types d'intervention suivants : Visite technique, Installation, Entretien - Maintenance, SAV et Divers.

Le champ Tâche permet de faire le lien entre le modèle d'intervention et la tâche voulue. La tâche identifie l’intervention effectuée par le technicien. *Ce champ n'est pas obligatoire mais il est notamment utile dans les cas où vos employés ne sont pas habilités à effectuer certaines tâches.* 

L’option Envoi des rapports permet de définir, dès que l’intervention est marquée comme terminée, si l’envoi du rapport d’intervention au client doit être fait :

- Envoi manuel : manuellement depuis la base Web OpenFire,

- Envoi automatique quand intervention en "Réalisé" : depuis l'appli mobile, dès que l'utilisateur clique sur "Terminé" dans un RDV, le RDV passe en réalisé et le rapport d'intervention part automatiquement par mail aux client,

- Envoi manuel depuis le mobile : depuis l'appli mobile, dès que l'utilisateur clique sur "Terminé" dans un RDV, il a la possibilité de cliquer sur "Envoyer le rapport" pour envoyer par mail le rapport d'intervention au client.

L'option Stockage auto du rapport vous permet de sauvegarder automatiquement le rapport d'intervention dans l'onglet Pièces Jointes du RDV:

L'option Section(s) à afficher dans l'intervention vous permet de sélectionner les sections qui seront affichées dans l'application mobile.

L'option Paiement mobile vous permet de créer le paiement depuis l'application mobile.

Une fois cochée, vous pouvez préciser les modes de paiement  autorisés.

## Facturation




L’onglet **facturation** peut être utilisé pour définir un ou plusieurs articles à facturer ainsi que la position fiscale à appliquer :

Ces éléments seront alors repris dans les rendez-vous d'intervention et les demandes d'interventions créées sur ce modèle.

La
            partie **Articles
              supplémentaires** permet de définir une liste
            d’articles proposés pour de la vente additionnelle. 

          

Ces articles pourront alors être ajoutés à la facture si besoin par l'intervenant depuis l’application mobile.

Pour qu'un article soit proposé en tant qu'article supplémentaire, il faut en amont vous rendre sur la fiche de l'article en question et cliquer sur le smart bouton dédié nommé *Mobile* :

  Vous pouvez utiliser cette fonctionnalité pour proposer en *Articles supplémentaires* l'ensemble des produits disponibles dans les camions de vos techniciens. Vos techniciens pourront ainsi ajouter ces éléments en fonction des chantiers.

Une fois ces éléments mis en place, il est possible de facturer depuis un rendez-vous ou une demande d'intervention en cliquant sur **Action > Générer les factures.**

  Plus d'information sur la __facturation des interventions__

## Questionnaire


L'onglet **Questionnaire** permet d'associer un questionnaire à ce modèle. Ainsi, il remontera sur les rendez-vous d'intervention pris depuis ce modèle.



Les questionnaires pourront alors être remplis depuis une intervention sur l'application mobile OpenFire.

Attention: actuellement, un seul questionnaire à la fois peut être ajouté au modèle d'intervention.

  Plus d'information sur [les questionnaires](https://documentation.openfire.fr/knowsystem/questionnaires-74)

## Fiche et rapport d'intervention


Les informations présentes sur les fiches et les rapports d’intervention sont également configurables depuis les modèles d’intervention. 

Si tous vos paramètres sont identiques dans vos rapports, modifiez simplement votre **Modèle par défaut** et cochez **Rapport par défaut** dans vos autres modèles.


En effet, le bouton *Rapport par défaut* permet de définir si vous souhaitez reprendre les paramètres définis dans le modèle par défaut, modèle qui s'applique lorsqu'aucun modèle d'intervention n'est sélectionné dans un rendez-vous. 

Ce modèle d'intervention par défaut est visible et paramétrable depuis le menu **Configuration > Modèle d'intervention :**

En modifiant les paramètres du modèle par défaut, tous les autres modèles en Rapport par défaut récupéreront automatiquement les paramètres modifiés.

Cependant, si vous ne souhaitez pas reprendre ces paramètres, décochez Rapport par défaut et définissez les propres paramètres d'impression de votre modèle.

Les fiches d'intervention sont davantage dédiées à l'intervenant, alors que le rapport d'intervention est à destination du client final.


  *Les rapports peuvent également être renommés (par exemple en Attestation d’entretien) et des mentions spécifiques peuvent être paramétrées pour chaque modèle via l'onglet Mentions légales.*