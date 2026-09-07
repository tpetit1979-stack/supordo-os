---
url: https://documentation.openfire.fr/knowsystem/realiser-une-intervention-300
url_finale: https://documentation.openfire.fr/knowsystem/realiser-une-intervention-300
date_collecte: 2026-09-06
destination: documentation_2
---

L'application mobile OpenFire est utilisable hors connexion (mode off-line). Le changement de mode se fait automatiquement selon la disponibilité du réseau.

# Réaliser l'intervention


A la création du rendez-vous d'intervention, vous avez la possibilité d'intégrer des questionnaires et photos de préparation dédiés. Cette phase permet notamment d'avoir un suivi de l'avant/après l'intervention grâce aux photos.

Le questionnaire quant à lui permet de récolter les informations pour savoir dans quel contexte s'effectue l'intervention.

Les sections affichées (Photos, Questionnaire, Facturation,...) sont configurables dans les modèles d'intervention.

  Plus d'informations sur [les modèles d'interventions](https://documentation.openfire.fr/knowsystem/modeles-dintervention-73)

Pour démarrer l'intervention, cliquez sur le bouton dédié :

## 1. Parc Installé


Il est possible de créer le parc installé depuis l'application mobile via l'icône Equipement:

En cliquant dans le champ produit, la fenêtre de recherche s'ouvre pour vous permettre de sélectionner l'article.

Vous pouvez utiliser des filtres de recherche par marque et/ou par catégorie.

Seules les marques et catégories paramétrées "Mobile" seront affichées.

Vous pouvez ensuite sélectionner l'article puis indiquer son état.

En cliquant sur le bouton Créer, le parc installé sera alors visible sur la fiche du contact.

  Plus d'informations sur [le parc installé](https://documentation.openfire.fr/knowsystem/gerer-mon-parc-installe-72)

A savoir : pour qu'une marque soit disponible à la création du parc installé sur l'application OpenFire, il faut que l'option Mobile soit cochée sur la configuration de la marque.

## 2. Photos


Pour permettre d'avoir des informations visuelles sur ce qui a été fait lors de l'intervention, vous pouvez 

prendre des photos depuis l'application ou charger des photos de la galerie de votre téléphone.

Vous pouvez annoter ces photos ou les supprimer si besoin.  

Un outil de Dessin est également disponible vous permettant de réaliser des croquis d'installation:

Vous pouvez également dessiner sur les photos en cliquant sur l'icone Dessin. 

Une fois les photos et les dessins sauvegardés, ils sont visibles dans l'intervention et sont envoyés à votre base web OpenFire.

Il est alors possible de les faire apparaitre dans les rapports d'interventions :

## 3. Questionnaire


Pour accompagner la réalisation de l'intervention, il est possible de charger un questionnaire en amont de l'intervention dans le rendez-vous d'intervention. 

Les réponses du questionnaire seront alors envoyées à votre base Openfire et pourront être ajoutées au rapport ou à la fiche d'intervention.

  Plus d'informations sur [les questionnaires](https://documentation.openfire.fr/knowsystem/questionnaires-74).

## 4. Facturation


Depuis l'application, vous avez accès aux données de facturation chargées dans le rendez-vous correspondant dans le backoffice. Un onglet Facturation vous permet d'ajouter les articles qui seront facturés à la suite de l'intervention.

Il est possible depuis l'application de supprimer ces articles et d'en ajouter de nouveau.

Les articles supplémentaires proposés, par défaut, sont ceux qui ont été définis dans l'onglet du même nom dans le modèle d'intervention attaché au rendez-vous.

Il est possible de rechercher sur toute la base article (par désignation ou référence interne) via la zone de recherche et de filtrer par marque et/ou catégorie.

  Plus d'informations sur [les modèles d'intervention](https://documentation.openfire.fr/knowsystem/modeles-dintervention-73).

## 5. Paiement


Depuis l'application, vous avez la possibilité de créer les paiements. Ce paiement sera enregistré directement dans la gestion des paiements et en comptabilité.


Cliquez sur Payer l'intervention.

Le montant affiché n'est pas modifiable.

Choisissez le mode de paiement et cliquez sur PAYER.

Tant que le RDV n'est pas sauvegardé ou terminé, vous pouvez annuler le paiement à tout moment.


A savoir: L'intervenant doit avoir les droits de générer un paiement. (Application Comptabilité et finance au minimum Facturation)

Le modèle d'intervention doit avoir l'option paiement mobile activée et être publié sur Mobile.


  Plus d'informations sur [les modèles d'intervention](https://documentation.openfire.fr/knowsystem/modeles-dintervention-73).

## 6. Livraison

Il est possible d'éditer le bon de livraison via l'application Mobile. Cela permet de renseigner si des éléments ont été utilisés ou non, ou si des pièces sont à commander en plus de la commande initiale.

Pour activer cette fonctionnalité, rendez vous dans le menu **Interventions > Configuration > Configuration**.

Il faudra alors sélectionner un article *Divers* que l'utilisateur mobile pourra ajouter au bon de livraison avec une description.

Après validation et sauvegarde, l'article ajouté sera alors visible sur la base web OpenFire.

La description et la référence saisies par l'utilisateur mobile seront alors visibles en cliquant sur l'article en question, dans le bon de livraison.

Il faut alors charger le bon article en s'aidant des descriptions qui ont été donné par l'utilisateur mobile.

## 7. Signature

Depuis l'application, l'intervenant et le client peuvent signer pour valider les éléments de l'intervention.

Au même titre que les photos et les questionnaires, les signatures pourront alors apparaitre sur le rapport d'intervention.

En cliquant sur le bouton signature, deux options seront proposées:

- Signature avec Prévisualisation, qui vous permet de prévisualiser le rapport d'intervention,

- Signature sans Prévisualisation.

  Plus d'informations sur [les modèles d'intervention](https://documentation.openfire.fr/knowsystem/modeles-dintervention-73).

# Clôturer l'intervention

Pour clôturer une intervention, cliquez sur le bouton Terminer disponible en bas de la fenêtre de détails de l'intervention.

Une pop up vous demandera alors confirmation. Vous pourrez ensuite, selon la configuration de votre base, saisir vos temps d'intervention.

Les informations (réponses aux questionnaires, photos, signatures, ...) saisies lors de l'intervention sont envoyées à la base OpenFire et peuvent être ajoutées aux fiches ou aux rapports d'intervention.

  Plus d'informations sur [Terminer une intervention](https://documentation.openfire.fr/knowsystem/terminer-une-intervention-95)