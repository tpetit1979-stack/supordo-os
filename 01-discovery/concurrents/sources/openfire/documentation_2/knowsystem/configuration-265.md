---
url: https://documentation.openfire.fr/knowsystem/configuration-265
url_finale: https://documentation.openfire.fr/knowsystem/configuration-265
date_collecte: 2026-09-06
destination: documentation_2
---

La prise de RDV en ligne est configurable afin que vous puissiez choisir sur quels appareils vous intervenez et pour quels techniciens.

Vous maitrisez les prestations disponibles à la réservation, les secteurs sur lesquels vous intervenez, et quels jours et créneaux vous ouvrez à la réservation en ligne.

Plusieurs étapes sont nécessaires pour configurer la prise de RDV en ligne : 

- Le client (contact) doit avoir un compte utilisateur avec un seul courriel.
- Le client doit avoir un parc installé : soit existant, soit l’option pour le créer est activée :
- Des créneaux doivent être disponibles ;
- Des tâches doivent être publiées ;
- Des secteurs doivent être définis sur chaque journée disponible à la réservation.

## Accès au portail

**Contacts**.

A savoir : un contact client peut avoir un sous-contact ou un contact "parent". L'accès au portail doit être créé avant la création des sous-contacts et contacts "parents".

Lorsque le contact client est créé, cliquez sur le menu déroulant

**Action > Gestion de l'accès Portail**situé en haut au centre de l’interface. Cette action va créer un compte utilisateur "portail".

Choisissez alors le profil de votre choix (B2B ou B2C) puis cliquez sur Appliquez.

Dans la fiche contact, de nouveaux champs (Couleur de texte et Couleur de fond) apparaissent et qui indiquent que le contact a un compte utilisateur :

**Configuration > Utilisateur > Profil Utilisateur.**


Si le client n'a pas reçu le mail de connexion, vous pouvez ainsi le renvoyer du compte utilisateur


## Ouverture des parcs installés

Rendez-vous dans le menu **Interventions > Configuration > Configuration**.

Puis dans la partie Prise de RDV en ligne pour déterminer si vous autorisez la création d'un parc installé extérieur, qui permet donc au client de créer en ligne son parc installé s'il n'en a pas.

L'ouverture de la création du parc installé implique de publier les marques et catégories d'articles sur lesquelles vous souhaitez intervenir. 

Il est aussi possible d'ouvrir la création d'un parc installé à des marques extérieures. Pour cela, cochez l'option Autorise la création d'un parc installé sur des marques extérieures.

Le champ "Autre marque" sera alors disponible dans le formulaire de création du parc installé.

## Configurer les marques et catégories d'articles

Lors de la création du parc installé si cette option est activée, il est nécessaire de définir quelles catégories d'articles et marques seront disponibles dans le formulaire. 

Depuis le module **Ventes >** **Configuration > Marques et Catégories d'articles**, allez dans chaque marque et catégorie que vous souhaitez activer et cliquez sur le smart button Publié.

## Configurer les tâches

Il faut également publier les tâches que vous désirez rendre disponibles.

Dans **Interventions > Configuration > Tâche**, incluez dans chaque tâche un Article lié et une Position fiscale, permettant d'indiquer le prix de l'intervention lors de la prise de rendez-vous. 

Vous pouvez maintenant cliquer sur le smart button Publié.

Attention : le créneau étant la demi-journée, les tâches dont la durée dépasse la demi-journée ne pourront pas fonctionner.

  *Plus d'information sur [la gestion des tâches](https://documentation.openfire.fr/knowsystem/gestion-des-taches-69)*

## Configurer les créneaux disponibles

Les créneaux disponibles lors de la réservation en ligne dépendent de plusieurs facteurs : d'abord, ce que vous avez défini comme mois et jours ouverts à la réservation, ensuite ce que vous avez ouvert comme horaires web chez les techniciens disponibles pour les rendez-vous web, et pour finir, des créneaux qui ne sont pas déjà occupés par des rendez-vous.

Par défaut tous les mois de l'année et les les jours ouvrés de la semaine sont ouverts.

Depuis le menu **Interventions > Configuration > Configuration > Disponibilités Web**, vous avez la possibilité d'indiquer quels sont les mois ouverts et les Jours ouverts.

Vous devez ensuite définir combien de temps en amont les jours sont visibles dans Nombre de jours ouverts à la réservation, défini par défaut à 60.

Un dernier paramètre vous permet d'utiliser la réservation en ligne uniquement pour combler les trous de votre planning en limitant la prise de rendez-vous uniquement aux journées qui ont déjà des rendez-vous de planifiés. Pour cela, décochez l'option Autorise la réservation de créneau sur des journées vierges.

Horaires employés

Vous devez renseigner les Techniciens disponibles, puis depuis **Interventions > Configuration** **> Employés**, rendez-vous dans l'onglet Horaires de votre employé pour paramétrer des horaires web.

  *Plus d'information sur [la gestion des employés](https://documentation.openfire.fr/knowsystem/employes-65)*


## Configurer les secteurs disponibles

 

            

Après avoir défini les créneaux, il faut configurer la zone d'intervention dans laquelle le client pourra prendre rendez-vous.**Création**

Les Secteurs sont accessibles depuis le menu Intervention > Configuration > Secteurs

L'utilisation des secteurs permet également de simplifier la planification des tournées d'interventions. La recherche des interventions peut ainsi être optimisée et OpenFire analyse pour vous les secteurs pour vous proposer la meilleure option de planification.

  *Plus d'information sur [les Secteurs](https://documentation.openfire.fr/knowsystem/secteurs-70#scrollTop=0)*

Affectation depuis le planning

Une fois les secteurs créés, rendez-vous dans le menu **Interventions > Interventions > Planning**

Vous devez ensuite, pour chaque jour et intervenant, affecter les secteurs.

Une journée sans secteur ne sera pas proposée à la prise de RDV en ligne.

A savoir : si la journée n’a pas de secteur affecté, le premier rendez-vous planifié dans la journée définira le secteur de cette journée. Si vous planifiez un rendez-vous avec un secteur différent de celui affecté à cette journée, la journée prend alors le secteur du rendez-vous planifié.

Affectation depuis les tournées

Une journée peut avoir **plusieurs secteurs ouverts** à la réservation en ligne. En vous rendant dans le menu Interventions > Interventions > Tournées, vous pouvez ajouter ou supprimer des secteurs par tournée. 

Si vous avez déjà des rendez-vous d'intervention qui sont dans des secteurs différents sur une même journée, les clients de ces secteurs pourront prendre rendez-vous en ligne ce jour-là.

  Attention : si vous créez des rendez-vous d'intervention sur un secteur donné et que vous supprimez ensuite ces rendez-vous, le secteur restera dans la tournée de l'intervenant et les clients de ce secteur pourront toujours prendre rendez-vous en ligne ce jour-là.

## Configurer la granularité


Plusieurs leviers existent pour affiner la granularité de réservation possible :

- Définir les créneaux possibles dans une journée directement dans les employés ; 
 *Plus d'information sur [la configuration des employés](https://documentation.openfire.fr/knowsystem/employes-65)*
- Ouverture de réservation : limiter le nombre de jours ouverts à la réservation ; 
 *Plus d'information sur [la](https://documentation.openfire.fr/knowsystem/configurations-generales-20) [configuration des interventions](https://documentation.openfire.fr/knowsystem/configurations-generales-20)*
- Appliquer la configuration manuelle ou à la demi-journée ;
- Granularité manuelle : au niveau de la tâche déterminée, les créneaux ouverts pour la prise de rendez-vous en ligne ;
- Appliquer des configurations différentes par magasin ;
- Choisir les utilisateurs qui peuvent accéder à la prise de rendez-vous en ligne.

Granularité de réservation manuelle - configuration dans la tâche

Rendez-vous dans **Interventions > Configuration > Configuration**, dans la section Prise de RDV en ligne, un paramètre existe afin d'affiner la granularité de réservation à la demi-journée ou manuelle :


Le paramètre est positionné par défaut à "Demi-journée".

Quand la granularité de réservation est "Manuelle" alors, lors de la prise de rendez-vous en ligne, le calcul du créneau dépend des horaires définis dans la tâche sélectionnée.

## 

Configuration spécifique par société


Dans **Interventions > Configuration > Configuration**, le paramètre ci-dessous permet de définir une configuration par société.

Quand la case est décochée, la configuration s'applique à toutes les sociétés. 

Quand la case est cochée, la configuration globale laisse place à celle de la société courante uniquement.

Les conditions générales de ventes ne sont pas concernées par ce paramètre. Elles sont toujours dépendantes de la compagnie.

## 

Configurer l'état du rendez-vous d'intervention



Dans **Interventions > Configuration > Configuration,** il est possible de choisir quel sera l'état du rendez-vous d'intervention dans le back office (version web) une fois pris par le client via le portail. Le rendez-vous d'intervention peut être créé directement en "Confirmé" ou bien en "Brouillon", laissant alors la main aux magasins pour le valider.


## Prix de la prestation


Dans Interventions > Configuration > Configuration, un paramètre contrôle l'affichage ou non du prix de la prestation lors de la prise de rendez-vous en ligne par le client.


Côté portail, lors de la prise de rendez-vous en ligne, à l'étape "Prestation", le prix est affiché. Il est repris de la tâche.