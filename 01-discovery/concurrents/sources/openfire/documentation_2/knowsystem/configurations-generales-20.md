---
url: https://documentation.openfire.fr/knowsystem/configurations-generales-20
url_finale: https://documentation.openfire.fr/knowsystem/configurations-generales-20
date_collecte: 2026-09-06
destination: documentation_2
---

De nombreux éléments du planning et de l'application mobile peuvent être modifiés et personnalisés.

Ces options de personnalisation sont disponibles depuis le menu **Interventions > Configuration > Configuration**.

Ces options sont regroupées en différentes sections :

## Intervention

- Gérer les prélèvements SEPA depuis les Demandes d'Intervention : 
Si cette option est cochée, il sera possible de générer les paiements "prélèvements SEPA" et générer le fichier de prélèvement pour la banque. Il faut au préalable que la configuration pour le prélèvement SEPA soit faite.
- Afficher les dates réelles d'intervention dans le planning intervention par employé :

Si cette option est cochée, les dates, heures et durées planifiées seront alors remplacées par les dates, heures et durées constatées par l’application mobile.

*La configuration par défaut utilise les dates planifiées et non les dates réelles.*

- (OF) Catégorie des VT : Si vous mettez la catégorie "Visite technique", la date de visite technique 
 qui se trouve dans le devis se renseignera automatiquement en fonction de la date du RDV
de la visite technique. Le numéro de lu devis / bon commande doit être noté dans le RDV pour le lien.


- Flexibilité des RDV :activer la flexibilité des rendez-vous. 
Ceci influence la planification de rendez-vous d'intervention.

- (OF) RDVs réguliers : activer la gestion des rendez-vous réguliers dans le planning. 
 *Plus d'information sur* *[les rendez-vous réguliers](https://documentation.openfire.fr/knowsystem/gerer-les-rdv-reguliers-194).*

## Secteurs


- Affecte automatiquement un secteur à la création d'un contact : lorsque l'option est activée, 
 permet d'affecter automatiquement un contact au secteur correspond à son code postal
(sous réserve que le secteur soit créé au préalable).

  Plus d'information sur [les secteurs](https://documentation.openfire.fr/knowsystem).

## Bons de livraisons

- BL d'intervention : permet de choisir d'utiliser ou non les bons de livraisons depuis les rendez-vous d'intervention. Si cette option est activée, il est alors possible de générer un bon de livraison depuis un rendez-vous.

  Plus d'information sur [les bons de livraison](https://documentation.openfire.fr/knowsystem/generation-du-bon-de-livraison-59).


- Article des BL :
permet de définir un article qui sera utilisé pour le retour de pose effectué depuis l'application mobile.Toute nouvelle ligne sera créée dans l'onglet "Opérations" du bon de livraison avec cet article, la description d'article définie par l'utilisateur mobile, ainsi que la quantité utilisée.

## Fiche d'intervention

- Cacher montant restant : permet de cacher le montant restant sur les fiches d'intervention (ancien modèle).
- Ajout en PJ : permet de rendre disponible la fiche d'intervention depuis l'application mobile.

## Créneaux non travaillés


Ainsi les créneaux disponibles et indisponibles peuvent être matérialisés par une couleur spécifique, de même que les jours fériés.


## Vue Calendrier

Le paramètre **Vue Calendrier** permet de définir l’amplitude d’affichage des horaires sur la vue calendrier standard.

La vue calendrier est disponible via l'icone

L’objectif est d’ajuster l’affichage afin de n’avoir à l’écran que les amplitudes de travail de l’entreprise.

Exemple avec les paramètres *heure min 8h	 / heure max 20h*	 :

## Recherche de créneaux horaires

Les champs suivants permettent de paramétrer les critères par défaut lorsque vous planifiez une intervention depuis une demande d'intervention (Interventions>Interventions>Demande d'intervention).

## Vue planning

- Le paramètre  **Exclusion d'intervenants** permet d’exclure certains techniciens de l’affichage planning.
- Le paramètre Affichage permet de personnaliser la vue planning afin de disposer les évènements de la même manière que ceux de la vue calendrier:

*Rechercher une demande d'intervention (icone Loupe):*

Cet état par défaut peut être choisi entre Brouillon et Confirmé:

## Mobile

L'option Affichage planning regroupe les configurations liées à l'application mobile.

Les paramètres Avant la date du jour et Après la date du jour permettent de définir une plage de date pour la synchronisation des RDV. Les RDV qui ne sont pas compris dans ces dates ne seront pas synchronisés.

Les options limite de récupération de l'historique et limite de récupération des photos permettent de définir un délai maximum de stockage de ces données en mois.

Il est possible de définir un nombre de pièces jointes maximum à ajouter sur les RDV d'intervention.

De même, les options taille MAX d'une PJ et Résolution permettent de définir un poids et une résolution maximum pour la pièce jointe (respectivement définie en Mo et en Pixels).


La modification de l'intervention permet de définir une plage de dates à partir de laquelle l'intervention va être modifiable depuis le planning de l'application mobile

Ainsi :

- le délai de modification avant la date du jour vous permet de modifier des interventions passées, tant qu'elles sont en statut Confirmé ou Réalisé.

- le délai de modification après la date du jour vous permet de modifier les interventions futures en statut Confirmé.

La saisie des temps permet de sélectionner la méthode de suivi de la durée des interventions.

- La saisie manuelle permet au technicien de saisir manuellement son temps d’intervention depuis l’application mobile.
- La saisie automatique permet l’utilisation d’un compteur de temps depuis l’application mobile.
- Une option permet également de rendre la saisie des temps obligatoire pour pouvoir clôturer l'intervention depuis l'application mobile.

Il est également possible de bloquer l'envoi des informations de montant sur l'application mobile:

  Plus d'information sur [l'application mobile](https://documentation.openfire.fr/knowsystem/telechargement-et-connexion-93).