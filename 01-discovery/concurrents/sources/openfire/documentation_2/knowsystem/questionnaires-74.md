---
url: https://documentation.openfire.fr/knowsystem/questionnaires-74
url_finale: https://documentation.openfire.fr/knowsystem/questionnaires-74
date_collecte: 2026-09-06
destination: documentation_2
---

OpenFire permet de créer des questionnaires sur mesure en fonction des différents types d'interventions. 

## Questionnaires


Les questionnaires peuvent être associés aux rendez-vous d'intervention et apparaitre sur les rapports d'intervention.

Ces modèles sont configurables depuis le menu Intervention > Configuration > Questionnaires

Les questionnaires peuvent être de deux types :

- questionnaire d'intervention : concerne les rendez-vous d'intervention
- questionnaire d'équipement : concerne uniquement la gestion du parc installé

   Plus d'informations sur le [parc installé](https://documentation.openfire.fr/knowsystem/gerer-mon-parc-installe-72)

A la création d'un questionnaire, il est possible d'y associer des questions via le bouton Ajouter un élément.


## Questions

Les questions sont configurables depuis le menu Intervention > Configuration > Questions

Plusieurs champs sont à renseigner à la création d'une question :

**Séquence :** permet d'indiquer l'ordre d'affichage de la question. 

**Type de question** : l'option Type de question permet, comme pour les questionnaires, de définir si les questions sont du type intervention ou équipement.

**Question obligatoire** : une réponse devra obligatoirement être saisie pour cette question. Dans le cas contraire, le rendez vous ne pourra pas être passé en réalisé.

**Catégorie** : les catégories de questions permettent de différencier les objectifs de ces questions :

- Appareil : liste des caractéristiques techniques de l’appareil, fabricant, modèle, puissance, …
- Ramonage et Entretien : liste des opérations à effectuer lors d’une intervention, nombre d’heures d’utilisation, état des joints, état des réfractaires, …

**Impression**

**: Cette option permet de définir si la question doit apparaitre sur le rapport d'intervention : soit toujours, jamais, ou uniquement si une réponse a été apportée.**

**Type de réponse :** ce menu déroulant permet de choisir le format de la réponse attendue :

*Oui / Non.*

Formulaire: permet d'importer un formulaire PDF éditable. Vous pourrez ensuite répondre directement depuis le mobile aux différents champs intégrés : sélection, texte, etc...

*Exemple d'application possible pour un questionnaire de VT*

Ensuite, si le questionnaire est utilisé pour un RDV d'intervention, vous avez la possibilité de remplir le questionnaire depuis l'application mobile :

Les réponses du questionnaire seront alors envoyées à votre base Openfire et pourront être ajoutées au rapport ou à la fiche d'intervention.

  Plus d'informations sur [l'application Mobile](https://documentation.openfire.fr/knowsystem/telechargement-et-connexion-93) 

**Réponses possibles :** permet de sélectionner et créer les réponses possibles. Celles-ci peuvent être modifiées, supprimées et archivées depuis le menu Intervention > Configuration > Réponses

Joindre une photo : permet d'ajouter une photo pour cette question. Il est possible de rendre l'ajout de la photo obligatoire.

**Conditions** : cette option permet de proposer une question en fonction des réponses précédentes.

__Exemple:__


Dans l'exemple ci dessous, le code identifiant *QUEST14* a été associé à la question "Quel type d'isolation avez-vous ?": 

Il est alors possible, via la condition *QUEST14 = "Combles"* de ne poser la question "Nature de l'isolant", si et seulement si la réponse à la question "Quel type d'isolation avez-vous?" est "Combles"

Ainsi, sur l'application mobile, la question Nature de l'isolant apparaitra si la réponse précédente est *Combles* :