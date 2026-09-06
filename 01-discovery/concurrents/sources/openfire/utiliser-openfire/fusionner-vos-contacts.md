---
source: https://support.openfire.fr/hc/fr/articles/19075584721052-Fusionner-vos-contacts
categorie: Utiliser OpenFire
titre: Fusionner vos contacts
date_recuperation: 2026-09-05
---

# Fusionner vos contacts

OpenFire dispose d’une fonctionnalité permettant une identification automatique de la plupart des doublons en fonction de différents critères comme le nom ou l’adresse mail. Cet article vous présente comment utiliser les fonctions de fusion de contact.

Cet article contient les sections suivantes :

- [Identifier des doublons](#h_01JPT7CVVD9TGYN76YZQCZBVX1)
- [Fusionner des contacts](#h_01JPT7CVVD33Y7HNJ1KV0573X3)

## **Identifier des doublons**

Un doublon est un contact qui a été créé à plusieurs reprises et qui existe plusieurs fois dans votre base de données. Un contact en double rend plus compliqué la gestion de la relation client, le suivi de l'historique, la réalisation des analyses de données, etc.

Pour accéder au contact en doublon :

Chemin d’accès :

- **Pour le plan basique :** OpenFire > Ventes > Mes clients
- **Pour les autres plans :** Contacts

Une fois sur cette liste, vous pouvez appliquer le filtre **"Doublon potentiels"**.

![](https://support.openfire.fr/hc/article_attachments/24131350544540)

**📓**Pour aller plus loin → [Les fonctions de recherche, de filtre et de regroupement de données](https://support.openfire.fr/hc/fr/articles/19075387609244)

## **Fusionner des contacts**

Si vous le souhaitez, vous pouvez fusionner des contacts identifiés comme doublons.

Pour cela : **sélectionnez les contacts à fusionner** >**Action > Fusionner**.

![](https://support.openfire.fr/hc/article_attachments/19117877013788)

Cette action ouvre une fenêtre vous permettant de choisir le contact de destination, c'est-à-dire celui qui restera dans le logiciel.

- **Fusionner les contacts :** Permet de réaliser la fusion des contacts vers le contact de destination sélectionné.
- **Ignorer ces contacts :** Permet de ne pas fusionner les contacts sélectionnés mais de poursuivre le processus de recherche des doublons.

Après avoir cliqué sur l’un de ces boutons, vous pourrez choisir d’arrêter ici en cliquant sur **“Fermer” **ou de cliquer sur le bouton **“Déduplication des autres contacts”**.

En sélectionnant cette deuxième option, l’outil ouvre une fenêtre vous permettant de  sélectionner le/ les critères de recherche des doublons de votre choix :

![](https://support.openfire.fr/hc/article_attachments/24131342627868)

**Attention : **les critères de recherche sélectionnés sont cumulatifs ; si vous recherchez des doublons sur la base de l’email et du nom, la Solution renverra tous les contacts ayant strictement le même nom et le même email.

**Exclure les contacts avec** :

- **Utilisateur associé au contact :** En cochant cette case, les contacts liés aux profils utilisateurs ne vous seront pas proposés.
- **Écritures comptables associées au contact : **Les écritures comptables peuvent bloquer des fusions de contacts selon certains critères. En cochant cette case, les contacts ayant des écritures comptables ne vous seront pas proposés.

**Limite maximum du groupe de contacts :** Permet de ne pas fusionner plus de X contacts ensemble, selon la limite que vous avez définie. Cette option est surtout utile si vous utilisez le bouton **“Fusionner automatiquement”**.

Vous pouvez ensuite :

- **Fusionner avec vérification manuelle : **Le logiciel recherche et vous propose une liste de doublon potentiel, en prenant en compte les critères sélectionnés plus tôt.
- **Fusionner automatiquement : **Le logiciel procède seul à la fusion de tous les contacts qu’il identifie comme doublon, en prenant en compte les critères sélectionnés plus tôt.

Mis a jour le : 09/12/2025
