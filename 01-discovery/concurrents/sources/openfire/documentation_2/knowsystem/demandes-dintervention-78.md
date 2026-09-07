---
url: https://documentation.openfire.fr/knowsystem/demandes-dintervention-78
url_finale: https://documentation.openfire.fr/knowsystem/demandes-dintervention-78
date_collecte: 2026-09-06
destination: documentation_2
---

Les demandes d'interventions permettent de saisir les interventions à effectuer sans avoir besoin de connaitre la date exacte de l'intervention afin de les attribuer plus tard en fonction des disponibilités des ressources. 

Le rendez-vous d’intervention n’existe pas encore. Ainsi la date, l’heure, l’adresse et l’intervenant restent à valider. La demande d'intervention est donc un objet particulier, précédent le rendez-vous d’intervention, au sein duquel les modalités de planification de l’intervention peuvent être définies.

Les demandes d'interventions peuvent être créées et consultées depuis le menu **Intervention > Interventions > Demandes d'intervention**

## Créer une demande d'intervention

A la création d'une demande d'intervention, seuls quatre champs sont obligatoires : le type d'intervention, le client (Partenaire), la tâche à effectuer et la plage de date sur laquelle la ou les interventions seront à effectuer.

#### Titre et priorité


A gauche du titre de la demande, il est possible de définir une notion d'importance ou de priorité via l'utilisation des étoiles :

#### Type d'intervention

Une demande d'intervention peut-être ponctuelle ou récurrente (pour un contrat d’entretien par exemple). Cette récurrence est possible en fonction du type d'intervention sélectionné.

Intervention ponctuelle : il s’agit d’une prestation unique, dont l’exécution se fait en une ou plusieurs fois, sans répétition dans le temps. Les deux sources les plus fréquentes d’interventions ponctuelles sont les chantiers d’installation, les interventions de dépannage ou de SAV.

Intervention récurrente : il s’agit de prestations dont la planification se répète dans le temps suivant une fréquence à définir (annuellement, trimestriellement, etc) en fonction du type d’opération. Les sources les plus fréquentes d’interventions récurrentes sont les contrats d’entretien et de maintenance exécutés sur un équipement installé.


Les interventions à programmer ne sont plus découpées entre récurrentes et ponctuelles mais entre 4 types d'intervention :

- Installation : le type Installation qualifie toutes les interventions ponctuelles, généralement liées à une commande client et impliquant d'intervenir pour installer un appareil chez un client.

- Visite technique : la visite technique est l'intervention avant installation. Ses fonctionnalités sont équivalentes à celle du type Installation.

- SAV : les demandes d'intervention de type SAV sont également des demandes d'interventions ponctuelles et qui peuvent être liées à un contrat.

- Entretien - Maintenance : les demandes d'intervention de type Entretien - Maintenance permettent la gestion de la récurrence. Celle-ci vous permet d'avoir des rappels automatiques sur vos demandes d'intervention en fonction d'une période choisie et pendant une durée précise.

Le type Entretien - Maintenance est aussi celui qui est utilisé pour les contrats - qui permettent de gérer une planification et une facturation récurrentes.

 Ces 4 types d'intervention sont aussi repris dans les rendez-vous d'intervention.

#### Modèle d'intervention

L'utilisation des modèles d'interventions permet de simplifier la création des rendez-vous et des demandes d'interventions. Ainsi, les modèles d'intervention permettent une saisie rapide des interventions, en chargeant un certain nombre d’informations comme le type d’intervention.

  Plus d'informations sur les [modèles d'interventions](https://documentation.openfire.fr/knowsystem/modeles-dintervention-73)

Le champ Commande client permet de faire le lien entre la demande d'intervention et un bon de commande client.

  *Des* *étiquettes* *peuvent être appliquées aux demandes d'interventions, par exemple pour qualifier rapidement le type de SAV.*

## Parties Qui et Où

Dans la partie Qui, il est possible dès la demande d'intervention de définir les intervenants ou le prestataire à reprendre lors de la planification du rendez-vous.



Les coordonnées du client sont à définir dans la partie Où.

Par défaut, l'adresse d'intervention reprend la valeur de la fiche du partenaire sélectionné.

Néanmoins, il est possible de modifier l'adresse d'intervention via le menu déroulant dédié.

## Parties Quoi et Quand

La partie Quoi permet de définir la tâche de l'intervention ainsi que sa durée prévisionnelle.

  Plus d'informations sur les [Tâches](https://documentation.openfire.fr/knowsystem/gestion-des-taches-69)

La partie Quand regroupe les éléments nécessaires à la réservation d'un créneau de rendez-vous.

Il est possible d'y définir une plage de date pour l'intervention, mais également les jours de disponibilité du client.

*Dans cet exemple, l'intervention est à effectuer entre le 1er et le 14 mai, et le client n'est disponible que les lundis, mercredis et samedis.*

Si la demande d'intervention est de type Entretien - Maintenance, et si l'option **Est récurrente** est cochée, alors c'est également dans cette partie que l'on va pouvoir définir la récurrence de l'intervention.

*Dans cet exemple, l'intervention est à répéter tous les 6 mois, si possible au mois de mars et septembre.*

## Description, produit installé, Historique et facturation

En bas de la demande d'intervention, l'onglet Description permet de saisir un commentaire qui sera alors repris dans la partie Description Interne du rendez-vous d'intervention.

La partie produit installé vous permet de faire le lien entre votre demande et votre parc installé.

  Plus d'informations sur le [parc installé](https://documentation.openfire.fr/knowsystem/gerer-mon-parc-installe-72)

L'onglet historique permet d'afficher l'historique des interventions programmées ou effectuées pour ce partenaire, ainsi que les informations de contrat s'il y a lieu.

L'onglet Facturation permet de gérer la facturation en amont du RDV et de générer des commandes clients ou fournisseurs.

Pour cela, ajoutez les lignes d'article dans l'onglet Facturation, puis cliquez sur Action > Générer devis client ou Générer commande fournisseur, et retrouvez-les ensuite dans les Smart boutons correspondants.

Toutes vos lignes de facturation, qu'elles aient ou non donné lieu à une commande, sont automatiquement reprises dans le RDV créé depuis la Demande d'Intervention, avec l'information de la commande liée. Pour les lignes de facturation qui n'ont pas encore été prises en compte, vous pouvez directement facturer en cliquant sur **Action > Générer les factures**