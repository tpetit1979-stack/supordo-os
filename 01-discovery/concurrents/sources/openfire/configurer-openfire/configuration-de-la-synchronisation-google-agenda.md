---
source: https://support.openfire.fr/hc/fr/articles/24655908526748-Configuration-de-la-synchronisation-Google-Agenda
categorie: Configurer OpenFire
titre: Configuration de la synchronisation Google Agenda
date_recuperation: 2026-09-05
---

# Configuration de la synchronisation Google Agenda

Cet article détaille la procédure technique pour lier votre instance OpenFire à l'API Google. Cette configuration est un prérequis indispensable avant que les utilisateurs ne puissent connecter leur propre compte.

Cet article contient les sections suivantes :

- [Configuration dans la console Google Cloud](#h_01KE9Z1MVABF2K48PB7E20838W)
- [Cas spécifique : Compte Gmail personnel (Utilisateurs tests)](#h_01KE9Z1MVJ16FG2JQ2GHHXAYPG)
- [Création des identifiants (ID et Secret)](#h_01KE9Z1MVMN0J9BGJH3QS2ZYY8)
- [Configuration dans OpenFire](#h_01KE9Z1MVQ8CAEZAKJX3H1CM47)

---

## Configuration dans la console Google Cloud

### Création du projet

![](https://support.openfire.fr/hc/article_attachments/24656181847324)

- Se rendre sur la [Console Google Cloud](https://console.cloud.google.com/) et se connecter avec son compte Google administrateur.
- Cliquer sur **Sélectionner un projet** en haut à gauche, puis sur **Nouveau projet**.
- Nommer le projet "OpenFire" et cliquer sur **Créer**.

### Activation de l'API

**![](https://support.openfire.fr/hc/article_attachments/24656169994908)**

- Cliquer sur le bouton **Activer les API et les services**.
- Rechercher "Google Calendar API".
- Sélectionner l'API et cliquer sur **Activer**.

### Écran de consentement OAuth

![](https://support.openfire.fr/hc/article_attachments/24656181850268)

- Dans le menu de gauche, cliquer sur **Écran de consentement OAuth**.
- Cliquer sur **Premiers pas**.
- Renseigner les **Informations sur l’application** :

  - Nom de l’application : "OpenFire"
  - Email d’assistance : votre adresse email.
- **Sélectionner la Cible** :
  **Interne** : Si vous avez un compte Google Workspace (entreprise). L'accès sera automatique pour vos collaborateurs.
  **Externe** : Si vous utilisez un compte Gmail classique (@gmail.com).
- Renseigner votre email dans les **Coordonnées du développeur** et cliquer sur **Créer**.

---

## Cas spécifique : Compte Gmail personnel

| 🚨**Avertissement :** Si vous avez sélectionné la cible "Externe" (compte Gmail personnel), vous devez autoriser manuellement les utilisateurs. |
| --- |

- Cliquez sur le menu **Audience** à gauche.
- Dans la section **Utilisateurs tests**, cliquez sur **Add users**.
- Renseignez l'adresse email de l'utilisateur et cliquez sur **Enregistrer**.

---

## Création des identifiants (ID et Secret)

- Dans le menu de gauche, cliquez sur **Présentation** (ou Identifiants) puis sur **Créer un client OAuth**.
- Dans **Type d’application**, sélectionnez **Application web**.
- Saisissez le nom de votre entreprise dans le champ **Nom**.
- **Origines JavaScript autorisées** : Cliquez sur **Ajouter une URL** et saisissez l’URL de votre base OpenFire (ex : `https://mabase.openfire.fr`).
- **URL de redirection autorisés** : Cliquez sur **Ajouter une URL** et renseignez l’URL de votre base suivie par `/google_account/authentication` 
  (ex : `https://mabase.openfire.fr/google_account/authentication`).
- Cliquez sur **Créer**.

| 💡**Note** : Une fenêtre s'affiche avec votre **ID client** et votre **Code secret de client**. Copiez-les dans un bloc-notes. |
| --- |

---

## Configuration dans OpenFire

Une fois les codes récupérés, vous devez finaliser le paramétrage dans votre logiciel.

`Suivre le chemin d'accès suivant : Configuration > Paramètres généraux`

![](https://support.openfire.fr/hc/article_attachments/24656169996316)

- Recherchez "Google Agenda" dans la barre de recherche en haut à droite.
- Activez le module en cochant la case prévue à cet effet.
- Cliquez sur **Enregistrer** en haut à gauche.
- La page s'actualise : renseignez maintenant votre **ID client** et votre **Code secret du client**.
- Cliquez à nouveau sur **Enregistrer**.

---

## Cas d'erreurs courants

### Procédure de validation Google

![](https://support.openfire.fr/hc/article_attachments/29882457474460)

Pour permettre à vos utilisateurs de lier leur OpenFire à Google Agenda, votre identifiant d'application (*OAuth Client ID*) utilise un écran de consentement actuellement réglé sur le statut **« En cours de test »** dans la Google Cloud Console. Google restreint automatiquement l'accès aux seules adresses e-mail déclarées manuellement comme testeurs. Pour que tous vos utilisateurs puissent synchroniser leur agenda il faut passer l'application en mode **Production**.

### La solution

![](https://support.openfire.fr/hc/article_attachments/29882441336220)

Pour débloquer l'ensemble de vos clients une fois pour toutes :

1. Connectez-vous à la [Google Cloud Console](https://console.cloud.google.com/) (vérifiez que vous êtes sur le bon projet).
2. Dans le menu de gauche, allez dans **API et services**.
3. Cliquez sur **Plate-forme Google Auth** *(Google Auth Platform)*.
4. Cliquez sur l'onglet **Audience** tout en haut.
5. C'est dans cet onglet que se trouve la section **Statut de la publication** (qui indique *En cours de test* / *Testing*).
6. Cliquez sur le bouton **Publier l'application** (*Publish App*) et validez le message de confirmation.

---

La partie technique est terminée. Chaque utilisateur doit maintenant lier son compte personnel.

| 📓**Pour aller plus loin** → [Synchroniser Google Agenda avec OpenFire](https://support.openfire.fr/hc/fr/articles/19095339438620) |
| --- |

Mis a jour le : 27/08/2026
