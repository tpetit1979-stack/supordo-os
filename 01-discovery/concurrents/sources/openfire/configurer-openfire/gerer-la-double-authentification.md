---
source: https://support.openfire.fr/hc/fr/articles/18965476941084-G%C3%A9rer-la-double-authentification
categorie: Configurer OpenFire
titre: Gérer la double authentification
date_recuperation: 2026-09-05
---

# Gérer la double authentification

![All_tick_V2.png](https://support.openfire.fr/hc/article_attachments/19563197391644)

La validation en deux étapes, également appelée "authentification à deux facteurs", vous permet d'ajouter un niveau de sécurité afin de protéger votre compte en cas de vol de votre mot de passe.

Cet article contient les sections suivantes :

- Activer la double authentification
- Désactiver la double authentification

🚨Avertissement : La double authentification n’est pour l’instant pas disponible sur l’application mobile OpenFire. Si vous l’activez, vous ne pourrez pas vous connecter sur mobile. Activez-la seulement si vous utilisez uniquement l’application web.

# Activer la double authentification

L’utilisation de la double authentification nécessite l’utilisation d’une application sur votre mobile.
Nous ne recommandons aucune application en particulier, notez cependant que les plus connues sont Google Authenticator, ou encore Microsoft Authenticator.

🍎 iOS :
[Google Authenticator](https://apps.apple.com/fr/app/google-authenticator/id388497605)

[Microsoft Authenticator](https://apps.apple.com/fr/app/microsoft-authenticator/id983156458)

🤖 Android :

[Google Authenticator](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2&hl=fr)

[Microsoft Authenticator](https://play.google.com/store/apps/details?id=com.azure.authenticator&hl=fr)

Activer l’authentification à deux facteurs :

1. Accéder à votre profil. Pour cela, cliquer sur votre nom en haut à droite, puis “Mon profil”.
2. Dans votre profil, accéder à l’onglet “Sécurité du compte”.
3. Dans l’onglet “Sécurité du compte”, activer la coche “Authentification à deux facteurs”.
4. Suivre les instructions à l'écran.
  ![](https://support.openfire.fr/hc/article_attachments/18965447650844)

Une fois la double authentification sélectionnée, il vous faut configurer l’application d’authentification.

![](https://support.openfire.fr/hc/article_attachments/18965476936988)

Une fois la manipulation terminée le message “Votre compte est protégé” s’affichera.

Lors de vos prochaines connexions un code supplémentaire délivré par l’application d’authentification vous sera demandé.

![](https://support.openfire.fr/hc/article_attachments/18965476938140)

Cochez “**Ne plus demander sur cet appareil**” uniquement si vous êtes sur votre ordinateur personnel et n’en partagez pas son accès.

# Désactiver la double authentification

Dans un premier temps, notez que nous ne vous recommandons pas de désactiver cette étape supplémentaire. En effet ce code ajoute un niveau de sécurité non négligeable à la protection de votre compte.

Si cependant vous devez désactiver temporairement cette protection, vous pouvez suivre ces étapes.

Activer l’authentification à deux facteurs :

1. Accéder à votre profil. Pour cela, cliquer sur votre nom en haut à droite, puis “Mon profil”.
2. Dans votre profil, accéder à l’onglet “Sécurité du compte”.
3. Dans l’onglet “Sécurité du compte”, désactiver la coche “Authentification à deux facteurs”.

A noter qu’en aucun cas le support OpenFire ne peut contourner la double authentification ou la désactiver.

Mis a jour le : 08/12/2025
