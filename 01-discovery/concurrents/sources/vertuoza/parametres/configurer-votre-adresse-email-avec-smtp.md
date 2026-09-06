---
source: https://intercom-help.eu/vertuoza/fr/articles/413323-configurer-votre-adresse-email-avec-smtp
categorie: Paramètres
titre: Configurer votre adresse email avec SMTP
date_recuperation: 2026-09-05
---

# Configurer votre adresse email avec SMTP

## Introduction

Ce guide vous accompagne pas à pas pour configurer vos paramètres email (SMTP et IMAP) dans l'application Vertuoza afin d'intégrer votre messagerie professionnelle.

## Accès à la Configuration

1. Dans l'application Vertuoza, cliquez sur les trois petits points situés en bas du menu principal

2. Accédez à votre **profil**

3. Dirigez-vous vers le dernier onglet "Intégration email"

4. Cliquez sur SMTP/IMAP

## Configuration des Paramètres

Paramètres SMTP (Serveur Sortant - Envoi des emails)

Les paramètres SMTP permettent d'envoyer des emails depuis l'application Vertuoza.

**Champs à renseigner :**

*Serveur SMTP :*

- Saisissez l'adresse de votre serveur SMTP

- Format : smtp.votre-fournisseur.com

*Port SMTP :*

- Port 587 (recommandé - TLS)

- Port 465 (SSL)

- Port 25 (non sécurisé - déconseillé)

*Sécurité SMTP :*

- TLS (pour port 587)

- SSL (pour port 465)

*Nom d'utilisateur SMTP :*

- Votre adresse email complète

*Mot de passe SMTP :*

- Le mot de passe de votre compte email

- Si vous avez activé l'authentification à deux facteurs, utilisez un "mot de passe d'application"

Paramètres IMAP (Serveur Entrant - Réception des emails)

Pour accéder aux paramètres IMAP, vous devez d'abord **activer le switch IMAP **dans la modale de paramètres.

Les paramètres IMAP permettent de recevoir et synchroniser vos emails depuis votre serveur de messagerie.

**Champs à renseigner :**

*Serveur IMAP :*

- Saisissez l'adresse de votre serveur IMAP

- Format : imap.votre-fournisseur.com

*Port IMAP :*

- Port 993 (recommandé - avec SSL)

- Port 143 (non sécurisé - déconseillé)

*Sécurité IMAP :*

- Sélectionnez SSL pour une connexion sécurisée

- Évitez "Aucune" pour des raisons de sécurité

*Nom d'utilisateur :*

- Votre adresse email complète (ex: [votremail@entreprise.com](mailto:votremail@entreprise.com))

*Mot de passe :*

- Le mot de passe de votre compte email

- Si vous avez activé l'authentification à deux facteurs, utilisez un "mot de passe d'application"

Configurations par Fournisseur (exemple)

 OVH

SMTP :

- Serveur : ssl0.ovh.net. (attention, parfois c'est pro1.mail.ovh.net etc)

- Port : 587 (ou 465 pour SSL)

- Sécurité : TLS (SSL is port 465)

IMAP :

- Serveur : ssl0.ovh.net (attention, parfois c'est pro1.mail.ovh.net etc)

- Port : 993

- Sécurité : SSL

iCloud

  SMTP:

- Serveur: [smtp.mail.me.com](http://smtp.mail.me.com/)
- Port: 587
- Chiffrement: TLS (= STARTTLS)
- Nom d'utilisateur: [lejoly.construction@icloud.com](mailto:lejoly.construction@icloud.com)
- Mot de passe: ⚠️ Mot de passe d'application (pas le mot de passe iCloud - voir ci-dessous)

  IMAP:

- Serveur: [imap.mail.me.com](http://imap.mail.me.com/)
- Port: 993
- Chiffrement: SSL
- Nom d'utilisateur: [lejoly.construction@icloud.com](mailto:lejoly.construction@icloud.com)
- Mot de passe: ⚠️ Même mot de passe d'application (pas le mot de passe iCloud - voir ci-dessous)

Créer un Mot de Passe d'Application (OBLIGATOIRE)

1. Aller sur [Apple Account](https://appleid.apple.com/)
2. Se connecter avec son identifiant Apple
3. Dans la section Sécurité, aller dans Mots de passe spécifiques
4. Cliquer sur Générer un mot de passe d'application
5. Donner un nom (ex: "Vertuoza Email")
6. Copier le mot de passe généré (format: xxxx-xxxx-xxxx-xxxx)

  ⚠️ Sans cette étape, aucune connexion SMTP/IMAP ne fonctionnera avec iCloud.

Yahoo Mail

SMTP :

- Serveur : smtp.mail.yahoo.com

- Port : 587 ou 465

- Sécurité : SSL/TLS

IMAP :

- Serveur : imap.mail.yahoo.com

- Port : 993

- Sécurité : SSL/TLS

La Poste (laposte.net)

SMTP :

- Serveur : smtp.laposte.net

- Port : 587

- Sécurité : SSL/TLS

IMAP :

- Serveur : imap.laposte.net

- Port : 993

- Sécurité : SSL/TLS

Orange

SMTP :

- Serveur : smtp.orange.fr

- Port : 587

- Sécurité : STARTTLS

IMAP :

- Serveur : imap.orange.fr

- Port : 993

- Sécurité : SSL/TLS

Mis a jour le : 06/02/2026
