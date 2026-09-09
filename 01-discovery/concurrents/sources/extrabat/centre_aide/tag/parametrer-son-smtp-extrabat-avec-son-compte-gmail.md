---
url: https://servicescompris.extrabat.com/tag/parametrer-son-smtp-extrabat-avec-son-compte-gmail
url_finale: https://servicescompris.extrabat.com:443/tag/parametrer-son-smtp-extrabat-avec-son-compte-gmail/
date_collecte: 2026-09-09
destination: centre_aide
---

Configurer un serveur SMTP Gmail dans Extrabat vous permet de continuer à envoyer vos emails transactionnels via l’interface du logiciel, tout en utilisant les serveurs de votre fournisseur Google. Cela inclut des communications essentielles comme l’envoi de devis, les confirmations de commande ou encore les relances de paiement.

En utilisant Gmail, vous pouvez personnaliser vos envois en affichant votre propre adresse Gmail comme expéditeur, garantissant une meilleure délivrabilité et une communication professionnelle.

Ce tutoriel vous guide étape par étape pour configurer le serveur SMTP de Gmail dans Extrabat.

## Étape 1 : Accéder à la configuration SMTP

1. Cliquez sur le bouton « + », accédez aux **Paramètres** , puis sélectionnez**Mode d’envoi des emails** .
2. Choisissez la **deuxième option** parmi les choix proposés.
3. Cliquez sur le lien situé sous cette option : *« Si vous choisissez cette option, vous devez paramétrer vos comptes SMTP en suivant ce lien »* .

## Étape 2 : Ajouter une configuration SMTP

1. Une fois dans le configurateur SMTP, cliquez sur Ajouter.
2. Dans la section *« Vous pouvez choisir une configuration pré-saisie (optionnel) »* , sélectionnez Gmail comme fournisseur. Les champs Adresse du serveur SMTP et Numéro de port seront automatiquement remplis.

## Étape 3 : Renseigner vos informations de connexion

1. Dans la section « Vos Informations » où le mot « magasin » apparaît par défaut, sélectionnez le nom du compte utilisateur pour lequel vous souhaitez configurer le serveur SMTP
2. Dans le champ **Identifiant SMTP** , entrez l’adresse email Gmail du compte utilisateur.
3. Dans le champ **Mot de passe SMTP** , vous devrez renseigner un**mot de passe d’application** généré depuis votre compte Google.

## Étape 4 : Générer un mot de passe d’application Gmail

						
						Précédent
					

					
						
						Suivant
					

									
1. Connectez-vous à votre compte Google.
2. Accédez à l’onglet **Sécurité** dans les paramètres du compte (activez la validation en deux étapes si elle n’est pas encore configurée).
3. Dans la barre de recherche *« Rechercher dans le compte Google »* , tapez et sélectionnez**« Mots de passe des applications »** . Vous devrez peut-être vous reconnecter.

			
⚠️ Si l’option ne s’affiche pas, voici quelques raisons possibles :


- La validation en deux étapes n’est pas configurée pour votre compte.
- La validation en deux étapes est configurée uniquement pour les clés de sécurité.
- Votre compte a été créé via une organisation (entreprise, école, etc.).

1. Dans la section **Nom de l’appli** , saisissez**Extrabat** , puis cliquez sur**Créer** .
2. Copiez le mot de passe généré.

## Étape 6 : Finaliser et tester la configuration

1. Revenez sur la page du configurateur SMTP dans myextrabat.com.
2. Collez le mot de passe dans le champ Mot de passe SMTP.
3. Vérifiez le mot de passe en cliquant sur l’icône « œil » pour supprimer les éventuels espaces superflus.
4. Cliquez sur Valider pour enregistrer la configuration.
5. Laissez l’encodage SMTP sur UTF-8 par défaut
6. Cliquez sur Valider une fois toutes les informations saisies
7. Après validation, sélectionnez le profil que vous venez de créer et cliquez sur Tester
8. Si les informations sont correctes, un message de succès s’affichera et vous recevrez un email confirmant la bonne configuration