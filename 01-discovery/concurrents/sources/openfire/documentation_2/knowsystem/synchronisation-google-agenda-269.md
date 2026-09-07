---
url: https://documentation.openfire.fr/knowsystem/synchronisation-google-agenda-269
url_finale: https://documentation.openfire.fr/knowsystem/synchronisation-google-agenda-269
date_collecte: 2026-09-06
destination: documentation_2
---

OpenFire peut être intégré au Calendrier Google Agenda. Ainsi, vous pouvez gérer vos rendez-vous depuis les deux plateformes (les mises à jour s’effectuant dans les deux sens).

Si la fonction vous intéresse, rapprochez-vous du support Openfire qui procèdera à la configuration préalable de votre base. 

         
    
        ## Configuration Google Agenda




Pour commencer la configuration, rendez-vous sur ce lien : [https://console.developers.google.com/](https://console.developers.google.com/)

Vérifiez que vous serez connecté avec le compte de l'agenda Google que vous allez relier à Openfire.

En haut à droite de votre écran, cliquez sur "CRÉER UN PROJET" et entrez un nom de projet. Vous pouvez changer votre id de projet si vous le souhaitez.



Dans le menu du côté gauche, sélectionnez le sous-menu "API et services activés" et cliquez sur "+ ACTIVER LES API ET LES SERVICES"



Tapez dans la barre de recherche le mot clé "calendar" et sélectionnez l'API "Google Calendar API"

Activez l'API Calendar en cliquant sur le bouton bleu "ACTIVER"

Lorsque c'est fait, les détails de l'API Calendar seront disponibles. Sur la page des API, cliquez sur le bouton bleu "CRÉER DES IDENTIFIANTS".

Vérifiez que l'API sélectionnée est bien "Google Calendar API", ensuite sélectionnez "Données utilisateurs" et cliquez sur le bouton "SUIVANT"

Spécifiez ensuite un nom d'application (par exemple "OpenFire"), ainsi qu'une adresse courriel dans les champs "Adresse e-mail d'assistance utilisateur" et "Adresses e-mail" de la partie "Coordonnées du développeur"

Enfin, cliquez sur le bouton "ENREGISTRER ET CONTINUER"

Passez directement à l'étape suivante en cliquant sur le bouton "ENREGISTRER ET CONTINUER"

Vérifiez que le type d'application est mis sur "Application Web", ensuite renseignez un nom (par exemple "OpenFire")

Cliquez sur le bouton "+ AJOUTER UN URI" de la partie "Origines JavaScript autorisées", et renseignez l'URL de votre environnement OpenFire:



Vous devez maintenant configurer les pages autorisées sur lesquelles vous serez redirigé.



Pour cela, cliquez sur le bouton "+ AJOUTER UN URI" de la partie "URI de redirection autorisés", et renseignez l'URL de votre environnement OpenFire suivie par *'/google_account/authentication'*



Réitérez l'opération 2 fois en cliquant de nouveau sur le bouton "+ AJOUTER UN URI" et en renseignant l'URL de votre environnement OpenFire suivie par *'/google_calendar/sync_data' et par '/google_calendar/remove_references'*



Vous devez ainsi vous retrouver avec une liste de 3 URI comme ci-dessous


Enfin, cliquez sur le bouton "CRÉER" juste en dessous, puis sur le bouton "OK" en bas de page:





Dès que c'est fait, retournez sur la page de l'ID clients OAuth 2.0 en cliquant sur le menu "Identifiants" du côté gauche, puis sur le nom de votre authentification.

Vous aurez enfin les deux informations (ID client et Code secret du client) que vous devez ajouter dans Openfire.

## Configuration Openfire


Une fois la configuration Google effectuée et en possession de votre ID client et code secret du client, ouvrez un nouvel onglet dans votre navigateur et connectez-vous à votre base Openfire.

Rendez-vous dans le module de Configuration>Paramètres généraux et descendez jusqu'à la partie "Intégration Google" pour entrez les identifiants dans les champs correspondants.

Ensuite, rendez-vous dans "Intervention>Configuration>Configuration" et vous cochez RDVs réguliers pour afficher Google Agenda et vous cochez Google Agenda.





   Assurez-vous d'être connecté avec un profil utilisateur qui a les droits de configuration.



Rendez-vous ensuite dans le module Interventions et passez le planning en vue calendrier. Cliquez sur le bouton "Sync. avec Google".



Une pop-up vous informe que vous allez être redirigé sur Google pour autoriser l'accès au calendrier. Cliquez sur le bouton "ok". Vous serez redirigé sur un nouvel onglet sur la fenêtre suivante :




Cliquez sur le bouton "Autoriser" et retournez sur Openfire pour cliquez de nouveau sur le bouton "Sync. avec Google".

En cas d'erreurs qui surviendraient lors de la configuration, rapprochez-vous du support Openfire.