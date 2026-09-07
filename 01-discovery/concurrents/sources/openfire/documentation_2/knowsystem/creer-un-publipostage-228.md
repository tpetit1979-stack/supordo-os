---
url: https://documentation.openfire.fr/knowsystem/creer-un-publipostage-228
url_finale: https://documentation.openfire.fr/knowsystem/creer-un-publipostage-228
date_collecte: 2026-09-06
destination: documentation_2
---

Le module Publipostage vous permet de créer et d'envoyer des mails en masse à une liste de contact.

Cette application permet également de suivre les éléments envoyés en affichant différents paramètres, tel que le taux d’ouverture, le taux d’envoi, etc...

L'application Publipostage est accessible via l'icone

__Attention__ : **L'envoi de mail en masse via cette application nécessite que votre serveur de mails (orange, gmail, outlook,...) soit en capacité d'envoyer un nombre important de mails en une fois**. Vous devez donc vérifier vos conditions d'envoi de mails en masse via la configuration de votre compte de messagerie. 

Un serveur mail doit être aussi paramétré sur votre base et vos adresses mails ne doivent pas être en format majuscule. P*lus d'informations sur la [configuration des serveurs mails](https://documentation.openfire.fr/knowsystem/parametrer-un-serveur-mail-151)*

## Tableau de bord

  Seuls les utilisateurs ayant le droit Publipostage : utilisateur (Configuration>Utilisateurs>Utilisateurs) peuvent accéder au module de publipostage.


En vous rendant dans le menu Publipostage, vous accéderez tout d'abord au tableau de bord sous forme de vue kanban.

Cette vue illustre l’état des publipostages ainsi que les statistiques sur les emails envoyés.

Chaque ligne en bleu est cliquable et vous permet d'accéder à davantage de statistiques sur les mails:

 Plus d'information sur [le rapport et suivi d'envoi](https://documentation.openfire.fr/knowsystem/rapports-232)

        

## Création du mail

La fenêtre s’affiche pour saisir les informations relatives à votre publipostage :

- Sujet (obligatoire) : permet de saisir l'objet du mail qui sera envoyé à vos destinataires.

- Destinataires : dans cette section, vous pouvez précisez le/les destinataires de votre message :

Clients : sélectionne les emails de la liste de vos contacts qui seront des destinataires ;

Pistes/Opportunité : sélectionne les contacts créés à partir des pistes ou des opportunités ;

Liste de diffusion : pour vous faciliter la tâche, OpenFire propose d'utiliser des listes de diffusion.

*Plus d'informations sur [les listes de diffusion](https://documentation.openfire.fr/knowsystem/liste-de-diffusion-229)*

Remarque : à l’exception de l’option "Liste de diffusion", il est possible de modifier et de filtrer la sélection des destinataire en cliquant sur Modifier la sélection :

- Corps du courriel : Dans cet onglet, vous pouvez peut choisir le modèle d’email à utiliser, ou créer le votre en cliquant sur le +

Il est possible de personnaliser le modèle à l'aide de blocs prédéfinis sur la gauche pour faciliter la conception:

Choisissez simplement vos blocs et déposez-les (en glissant/déposant) exactement à l'endroit où vous voulez qu'ils apparaissent dans votre email :

Vous pouvez également personnaliser votre mise en page via la barre d'outils disponible en haut :

L'icone de baguette magique vous permet de sélectionner un style de mise en forme.

Les boutons suivants permettent de mettre en gras, en italique ou encore de souligner le texte.

La gomme permet de supprimer la mise en forme.

Le bloc suivant vous permet de saisir la couleur et la taille de la police, ainsi que l'alignement du texte:

Le dernier bloc d'outil permet d'insérer des liens ou des images.

Attention: il est important de toujours importer les images via le bouton dédié et de ne pas seulement copier-coller l'image dans le corps du publipostage. En effet, si l'image est copiée-collée, elle ne sera pas transférée de la même façon aux différents fournisseurs de messagerie et risquerait de mal, ou de ne pas, apparaitre.

- Onglet Configuration de l’email : dans cet onglet, vous pouvez préciser le nom qui va être affiché aux destinataires, et inclure une pièce jointe en cas de besoin :

Lorsque vous terminez la configuration de votre publipostage, enregistrez vos modifications.

En enregistrant votre publipostage, il sera mis automatiquement en état brouillon, et vous pouvez le visualiser dans la vue Kanban.

Avant de planifier l’envoi de votre publipostage, vous avez la possibilité de le tester en cliquant sur le courriel test.

Dans le pop-up qui s’affiche, vous pourrez alors préciser une adresse email sur lequel sera envoyé l’email de test :

Après la première étape, vous pouvez envoyer directement l’email en cliquant sur le bouton Envoyer

Vous pouvez également planifier l’envoi de ce publipostage en cliquant sur le bouton Planifier pour plus tard disponible dans l'onglet Option :

Après la planification, votre publipostage, passe en étape en attente, et plusieurs Smart Buttons s’affichent pour vous donner un aperçu et des détails sur le publipostage en cours.

Une fois les emails envoyés, le publipostage passe en dernière étape, qui vous indique le résultat de l’envoi des emails avec des statistiques tels que le pourcentage des emails envoyés, celui des emails ouverts, les clics et d’autres statistiques que vous pouvez consulter en ouvrant le publipostage que vous souhaitez examiner depuis la colonne Kanban.

 Plus d'information sur [le rapport et suivi d'envoi](https://documentation.openfire.fr/knowsystem/rapports-232)