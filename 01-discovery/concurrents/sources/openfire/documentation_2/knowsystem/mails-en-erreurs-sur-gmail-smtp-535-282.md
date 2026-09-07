---
url: https://documentation.openfire.fr/knowsystem/mails-en-erreurs-sur-gmail-smtp-535-282
url_finale: https://documentation.openfire.fr/knowsystem/mails-en-erreurs-sur-gmail-smtp-535-282
date_collecte: 2026-09-06
destination: documentation_2
---

Le problème vient généralement du fait que Gmail a durci sa politique de sécurité. Dorénavant, il ne faut plus saisir votre "vrai" mot de passe gmail dans OpenFire mais un mot de passe généré par google spécifiquement pour OpenFire.

Voici comment procéder:

Etape 1: Activation de la double validation

Connectez-vous à votre compte Gmail et cliquez sur votre profil en haut à droite. Cliquez ensuite sur “Gérer votre compte Google”.

Rendez-vous ensuite dans l’onglet “Sécurité” et activez la validation en deux étapes (dans la partie “Connexion à Google”).

Cliquez sur commencer et suivez les instructions. 

Renseignez bien votre numéro de téléphone portable lorsque cela vous le sera demandé, car des codes de vérification Google vous seront par sms.

Etape 2: Activation des mots de passe des applications

Lorsque cela est terminé, retournez dans l’onglet “Sécurité” de votre compte Google et cliquez de nouveau sur “Validation en 2 étapes”.

Tout en bas de la page, il faut cliquer sur “Mots de passe des applications”.

Ensuite, il faut créer un mot de passe pour l’application OpenFire.

Pour cela, créez une application en sélectionnant “autre”, nommez “Openfire” et cliquez sur le bouton “Générer”. Cela générera un mot de passe à 16 caractères qu’il faudra noter.

Cela génèrera un mot de passe à 16 caractères qu’il faudra noter.

Connectez-vous enfin à votre base Openfire (assurez-vous d’être sur un profil disposant des droits de configuration) et cliquez sur "activer le mode développeur" tout en bas à droite. Une fois la page rechargée, rendez-vous de nouveau dans l'onglet Configuration > Technique > serveurs de courriel sortant

Cliquez sur le serveur correspondant à votre adresse Gmail pour laquelle vous venez de configurer votre compte.

Modifiez ensuite le mot de passe pour y entrer les 16 caractères préalablement transmis par Google et cliquez sur “test de connexion” pour vérifier que tout fonctionne correctement.