---
url: https://documentation.openfire.fr/knowsystem/parametrer-un-serveur-mail-151
url_finale: https://documentation.openfire.fr/knowsystem/parametrer-un-serveur-mail-151
date_collecte: 2026-09-06
destination: documentation_2
---

Il est possible de connecter OpenFire à votre compte de messagerie de telle sorte qu’OpenFire puisse émettre des mails depuis votre serveur de messagerie.

**Dans un premier temps notez que l'utilisation d'un hébergeur mail destiné aux particuliers n'est ni recommandé, ni supporté par Openfire.**

**En effet cet usage est souvent limité ou bloqué par les fournisseurs tels que Gmail, Microsoft, Yahoo, etc.**

**Les manipulations énoncées sur cet articles peuvent fonctionner au moment de la configuration avec un service destiné aux particuliers, mais nous ne pouvons vous apporter aucune garantie sur la pérennité de cette solution.**

## Activation du mode Debug

La configuration des envois d’email se fait depuis le menu configuration et nécessite l'activation du mode Développeur.

Pour cela,  rendez-vous dans l’onglet Configuration puis cliquez sur l’option Activer le mode développeur à droite :

Après le chargement de la page, retournez dans le menu Configuration. Cliquez ensuite sur **Technique > Serveurs de courriel sortant**

*Ces différents menus vous permettent de piloter votre envoi de mail.*

## Configuration des serveurs Mails

Cliquez sur Créer , puis renseignez les différents paramètres demandés.

*ssl0.ovh.net*et le port à utiliser est le 587.

*smtp.office365.com*et le port à utiliser est le 587.

Après avoir saisis les différents paramètres de votre compte, vous pouvez vérifier que tout fonctionne en cliquant sur le bouton "Test de connexion".

Si tout est correct, vous obtenez le message suivant:

## Erreurs Possibles

Erreur SMTP 40X:

Les codes erreurs SMTP 40X correspondent à des erreurs temporaires, exemple 421 Try again later. Ces erreurs sont remontées par le serveur expéditeur. Cela peut être un problème d'indisponibilité temporaire, ou encore un problème de quota de mail.

Erreur SMTP 534 et/ou SMTP 535:

Le problème vient généralement du fait que Gmail a durci sa politique de sécurité. Dorénavant, il ne faut plus saisir le mot de passe de votre adresse gmail dans OpenFire mais un mot de passe généré par google spécifiquement pour OpenFire.

Voici comment procéder:**Etape 1: Activation de la double validation**

Connectez-vous à votre compte Gmail et cliquez sur votre profil en haut à droite. Cliquez ensuite sur “Gérer votre compte Google”.

Rendez-vous ensuite dans l’onglet “Sécurité” et activez la validation en deux étapes (dans la partie “Connexion à Google”).

Cliquez sur commencer et suivez les instructions. 

Renseignez bien votre numéro de téléphone portable lorsque cela vous le sera demandé, car des codes de vérification Google vous seront transmis par sms.

Etape 2: **Activation des mots de passe des applications**

Lorsque cela est terminé, retournez dans l’onglet “Sécurité” de votre compte Google et cliquez de nouveau sur “Validation en 2 étapes”.

Vérifiez que la validation en 2 étapes est bien activée :

Tout en bas de la page, il faut cliquer sur “Mots de passe des applications”.

**__IMPORTANT :__** Si vous ne retrouvez pas l'emplacement "Mot de passe des applications" alors vous pouvez également faire une recherche "application" dans la barre de recherche située au dessus et sélectionner "Mot de passe des applications".


Ensuite, il faut créer un mot de passe pour l’application.

Pour cela, créez une application en sélectionnant “autre”, notez le nom de votre base client et cliquez sur le bouton “Générer”.

Vous allez obtenir un mot de passe à 16 caractères qu’il va falloir reporter dans Openfire.

Connectez-vous à votre base Openfire depuis un profil ayant accès à l'application Configuration,  et cliquez sur [activer le mode développeur](https://documentation.openfire.fr/knowsystem/parametrer-un-serveur-mail-151#Activation-du-mode-Debug) puis accédez au menu [serveurs de courriel sortant](https://documentation.openfire.fr/knowsystem/parametrer-un-serveur-mail-151#Activation-du-mode-Debug).

Cliquez sur le serveur correspondant à votre adresse Gmail pour laquelle vous venez de configurer votre compte.

Modifiez ensuite le mot de passe pour y entrer les 16 caractères préalablement transmis par Google et cliquez sur “test de connexion” pour vérifier que tout fonctionne correctement.