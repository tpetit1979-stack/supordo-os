---
source: https://help.sellsy.com/fr/articles/6154289-configuration-postman-api-v1
categorie: Intégrations et API
titre: Configuration Postman API V1
date_recuperation: 2026-09-05
---

# Configuration Postman API V1

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2159178304/e1e01a86cf03ae5798ebe5f4ae73/FAQ-Bannie%CC%80reAcademy-2+%282%29.png?expires=1788635700&signature=ebdfef4898ccbfd8feb9ff6c339df174b17f809d5e5fdd9052d03f6a1e3c1088&req=diEiH8h5lYJfXfMW1HO4zVuM%2BLW1yJRvJRfHNCpWqoHYsfUIei81KMAH1KRj%0A4ppaLY76d2hy4x2DYRA%3D%0A)

___________________________________________________________

### **Prérequis**

Avant de configurer Postman pour l'API V1 de Sellsy, assurez-vous d'avoir :

- **Postman installé** sur votre ordinateur (téléchargeable gratuitement sur **[postman.com](https://www.postman.com/)**)
- **Un accès API V1 créé** dans Sellsy avec vos tokens (Consumer Key, Consumer Secret, Access Token, Token Secret)
- **La collection API V1 Sellsy** (disponible en téléchargement à la fin de cet article)

> **Bon à savoir :** Si vous n'avez pas encore créé d'accès API, consultez l'article **[Types d'accès API](https://help.sellsy.com/fr/articles/5876615-types-d-acces-api)**.

___________________________________________________________

### Création d’un environnement API V1 

Un environnement Postman permet de stocker vos variables (tokens, URL) pour les réutiliser facilement dans vos requêtes.

**Créer un nouvel environnement**

1. Depuis Postman, cliquez sur *"Environments"* dans le menu de gauche
2. Cliquez sur le bouton *"New"* (ou le symbole **+**)
3. Sélectionnez *"Environment"* dans la fenêtre qui s'affiche

![](https://sellsy-a9cc78fb6d3a.intercom-attachments-7.com/i/o/499825131/c2456a25ceff01f6e7fa642c/e3fafa1b-781c-448b-b2a8-8687931babaa?expires=1788635700&signature=67de7ce8f2ca525d79bb712376134c29ef2e362aa8389b2d0ed1223df5cfa2ee&req=cCkuHst7nIJeFb4f3HP0gLVW9tJZ0RRZ313tK4OGF99Xe%2BwPmNXKKw2ETz3R%0AvegX2Ac2YH8Ohv9uoA%3D%3D%0A)

**Nommer l'environnement**

Nommez l'environnement **API V1** pour l'identifier facilement.

![](https://sellsy-a9cc78fb6d3a.intercom-attachments-7.com/i/o/499825136/839824fb0e0a07e4125bf55a/ff1c4952-abb4-4ebc-ba4c-48698794d8a7?expires=1788635700&signature=2fa8672aec8a0ac830111fdfe1d08a0bc9f53364e6ad706c14b86ebca037a0d4&req=cCkuHst7nIJZFb4f3HP0gBYFx5ApyR9QyiijP5qI4tvID0NyAWKNDxPxtJOy%0A7rvnsZha7YWVnTGhlA%3D%3D%0A)

**Ajouter les variables**

Ajoutez les variables suivantes dans votre environnement :

**Token consumer** : *admin_consumer_key admin_consumer_secret*

**Token utilisateur** : *admin_access_token admin_token_secret url_base*

![](https://sellsy-a9cc78fb6d3a.intercom-attachments-7.com/i/o/499825140/09b4fd572e5b7f40ded86b36/fb25007a-571e-4a20-a76a-aea007206f22?expires=1788635700&signature=b93526f12973ff6f1b2b55acde83533bffb9f0b1652194aa6e323296976c96d9&req=cCkuHst7nIVfFb4f3HP0gJeIHKA%2BCHQI4pWC2BNGd47FbFzN%2FGvOr18IY%2BuB%0A%2FheBGaPTPxrEI70hnA%3D%3D%0A)

Définissiez le type : Défaut

**Configurer les variables**

Copiez les tokens générés sur Sellsy et collez-les ensuite pour chacune des variables correspondantes (dans *"INITIAL VALUE"* et *"CURRENT VALUE"*).

Puis dans url_base mettre : [https://apifeed.sellsy.com/0/](https://apifeed.sellsy.com/0/) (dans *"INITIAL VALUE"* et *"CURRENT VALUE"*).

___________________________________________________________

### Ajouter la collection API V1

La collection Sellsy contient des exemples de requêtes prêtes à l'emploi pour tester rapidement l'API V1.

1. Depuis Postman, cliquez sur *"Collections"* dans le menu de gauche
2. Cliquez sur *"Import"*
3. Cliquez sur *"Upload files"*
4. Sélectionnez la collection API V1 Sellsy (fichier JSON) sur votre ordinateur
5. Cliquez sur *"Import"*

La collection apparaît maintenant dans votre liste de collections.

___________________________________________________________

### Configuration de l'authentification au niveau de la collection

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/1699347834/b2d7c381d763d78faf71f500d9a5/image.png?expires=1788635700&signature=2b38e464ef6ae6bc33896cc13b4f150b10eb94cd6d68187eb0c408481b745af4&req=dSYuH8p6molcXfMW1HO4zUryv8hOO%2F%2BoTE%2BWh2UgGDyC1MlOsB8PCyVMUwtL%0AJDEHxYCNPofm0GkXdWE%3D%0A)

 Cliquez sur le document ci-dessous pour consulter le fichier JSON de l'API V1 : 

Mis a jour le : 13/03/2026
