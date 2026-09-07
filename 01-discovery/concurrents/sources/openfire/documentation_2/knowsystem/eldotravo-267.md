---
url: https://documentation.openfire.fr/knowsystem/eldotravo-267
url_finale: https://documentation.openfire.fr/knowsystem/eldotravo-267
date_collecte: 2026-09-06
destination: documentation_2
---

EldoTravo est une plateforme qui permet de faciliter la recherche de professionnels du bâtiment et de simplifier le processus de réalisation de travaux pour les particuliers. 

Elle met en relation les particuliers avec des artisans qualifiés et vérifiés, et permet aux clients de laisser des avis sur les prestations fournies.

Il est possible de permettre l’envoi de certaines informations de contacts depuis OpenFire à Eldotravo pour une collecte d’avis.

 *La mise en place du connecteur EldoTravo nécessite un certain nombre de paramétrages et l'ajout d'un module spécifique. Aussi, pour toute demande d'ajout de cette fonctionnalité, vous pouvez contacter le support OpenFire par mail à l'adresse support@openfire.fr ou par téléphone au 02.30.96.02.65.*

## Configuration

Une fois que vous avez reçu la confirmation que le module EldoTravo a été installé par le support OpenFire, rendez-vous dans le menu Configuration > Connecteur > Configuration :

Dans la partie Eldotravo, deux champs spécifiques sont a renseigner:

- ID EldoTravo: il s'agit d'un identifiant fourni par Eldotravo
- URL EldoTravo: https://hooks.zapier.com/hooks/catch/3483486/owo4uwb/

 **A Savoir:** Dans le cadre de la gestion du *Règlement Général sur la Protection des Données* , Eldotravo partage un exemple de commentaire avec leurs clients à insérer dans le devis pour indiquer la possibilité de partager ces données avec le service Eldotravo:

*Je reconnais et accepte que XXXXXX transmette mes coordonnées à la société EldoTravo qui est susceptible de me contacter afin de récolter des avis et commentaires concernant la prestation ayant fait l’objet du présent devis.*

La signature du document par le client final vaut acceptation complète ou totale selon Eldotravo.

## Collecte d'avis

A la suite de vos interventions, le connecteur Eldotravo - OpenFire vous permet d’envoyer en 3 clics une demande d’avis à collecter à Eldotravo.

Les données à envoyer sont pré-configurées (ce sont les données obligatoires pour traitement d’une demande de collecte d’avis par Eldotravo).

- coordonnées du client (Prénom - Nom - email et/ou téléphone mobile)
- ville de réalisation du chantier
- date de réalisation du chantier
- Identification de la marque de l'appareil

Pour envoyer la demande d’avis, un rendez-vous doit être réalisé et avoir une adresse associée.

Plusieurs données seront ensuite envoyées à EldoTravo afin de pouvoir procéder à la collecte d'avis, parmi lesquelles: les coordonnées du client, la date des travaux, la ville, éventuellement la marque de l'appareil, etc...

Pour effectuer la collecte d'avis, passez en vue liste des rendez-vous réalisés.

Un filtre de recherche nommé Dispo envoi EldoTravo vous permet de sélectionner les rdv disponibles pour la collecte d'avis:

Ensuite, sélectionnez les rdv de votre choix, puis cliquez sur **Action > Envoi Eldotravo** :

Une fenêtre s'ouvre alors permettant de préciser certaines informations (email, marque de l'appareil posé, etc...):

 **A savoir:**  

Une demande d’avis déjà envoyée pour un client est explicitement identifiée:

- Un message en rouge indique l’envoi en doublon en cas d’envoi simple. 

- Une case “Déjà envoyé” est cochée en cas d’envois multiples.