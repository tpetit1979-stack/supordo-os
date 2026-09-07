---
url: https://documentation.openfire.fr/knowsystem/envoyer-un-sms-sur-openfire-238
url_finale: https://documentation.openfire.fr/knowsystem/envoyer-un-sms-sur-openfire-238
date_collecte: 2026-09-06
destination: documentation_2
---

OpenFire vous permet d'envoyer différents type de SMS en fonction de vos besoins:

- SMS Marketting
- Rappel de RDV
- SMS à la demande

## Marketing par SMS

La communication commerciale par SMS est une aide à la vente efficace. Attention toutefois à bien respecter la réglementation sur l’envoi de SMS commerciaux.

Depuis les opportunités de vente de votre pipeline (portefeuille), ou encore depuis votre liste de contact, vous pouvez sélectionner les prospects à l’aide de filtres et envoyer un SMS à tous les prospects sélectionnés.

Lorsque votre modèle de SMS commercial est défini, il vous suffit de sélectionner vos prospects pour envoyer votre SMS:

Sélectionnez ensuite le modèle de votre choix. Ces modèles sont configurables depuis le menu **Configuration > SMS > Modèles**:

Une fenêtre vous permettra alors de créer un modèle de SMS pouvant être appliqué à différents modules OpenFire (Contacts, Piste CRM, etc...):

## Rappel automatique de rendez-vous

Vous pouvez optimiser votre temps et votre planning en réduisant votre taux d’absentéisme grâce aux SMS automatiques de rappel de rendez-vous ou d’intervention.

Objectif premier de l’intégration, le rappel automatique de rendez-vous scrute le planning du lendemain et envoie un SMS à tous les clients pour rappeler l’heure et le motif du rendez-vous. Ce processus est entièrement automatique.

Il suffit de paramétrer la planification des alertes pour que ce service soit actif.

Pour cela,  rendez-vous dans l’onglet Configuration puis cliquez sur l’option Activer le mode développeur à droite :

De nouveaux menus apparaitront alors. Puis rendez-vous dans le menu Configuration > Technique > Automatisation > Actions planifiées

Dans la liste des actions planifiées, sélectionnez alors SMS rappel intervention.

Pour suspendre l’action planifiée, décochez la case Actif. Pour définir l’heure d’envoi du SMS, modifiez l’heure dans la date de prochaine exécution. L’unité d’intervalle est le Jour. Les données techniques ne peuvent être modifiées que par le support OpenFire.

Le modèle de SMS Rappel automatique RDV est configuré lors de l’installation.

Ces modèles sont configurables depuis le menu Configuration > SMS > Modèles:

1. Nom du modèle
2. Objet associé au modèle : Planning, Client, …
3. Utilisateur API chez OVH
4. Expéditeur chez OVH : apparait en début de SMS
5. Destinataire : vide dans le modèle, rempli automatiquement à l’envoi du SMS
6. Texte du SMS avec les balises de publipostage

## SMS à la demande

Dans OpenFire, il est possible de répondre immédiatement à un client par SMS pour lui communiquer une référence, des coordonnées GPS, …

Cette fonction SMS à la demande est accessible depuis les fiches suivantes :

- Contact
- Opportunité
- Intervention
- Commande
- Facture

L'envoi des sms se fait alors via le bouton Action:

Une fenêtre vous permet alors de personnaliser le SMS: