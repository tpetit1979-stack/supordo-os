---
source: https://help.sellsy.com/fr/articles/6154292-configuration-postman-apiv2
categorie: Intégrations et API
titre: Configuration Postman APIV2
date_recuperation: 2026-09-05
---

# Configuration Postman APIV2

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2159222834/70d9fdb5dcc7ba358523e5f259d4/FAQ-Bannie%CC%80reAcademy-2+%282%29.png?expires=1788635700&signature=70d334396511d9f64a428e59a584cf6234e07114826cad5c22ed18d31df99f11&req=diEiH8t8n4lcXfMW1HO4zYJTJIcDPc5Nz5foXDajz1UcPdasKRG5NzG%2BM5X%2B%0Ai5%2BEFXazGaxZ0Fjongw%3D%0A)

___________________________________________________________

### **Prérequis**

Avant de configurer Postman pour l'API V2 de Sellsy, assurez-vous d'avoir :

- **Postman installé** sur votre ordinateur (téléchargeable gratuitement sur **[postman.com](https://www.postman.com/)**)
- **Un accès API V2 créé** dans Sellsy (type personnel ou privé)
- **Vos identifiants API** (Client ID et Client Secret)

> **Bon à savoir :** Si vous n'avez pas encore créé d'accès API, consultez l'article **[Types d'accès API](https://help.sellsy.com/fr/articles/5876615-types-d-acces-api)**.

**Documentation complète :** **[API V2 Sellsy](https://api.sellsy.com/doc/v2/)**

___________________________________________________________

### **Paramétrage de Postman**

Un environnement Postman permet de stocker vos variables (identifiants, URL) pour les réutiliser facilement dans vos requêtes.

**Créer un nouvel environnement**

1. Depuis Postman, cliquez sur *"Environments"* dans le menu de droite
2. Cliquez sur le bouton *"New"* (ou le symbole **+**)
3. Sélectionnez *"Environment"* dans la fenêtre qui s'affiche

![](https://sellsy-a9cc78fb6d3a.intercom-attachments-7.com/i/o/499825854/178d42c3ebb272692b52a209/2408c284-12dc-4043-b605-8c20926575d6?expires=1788635700&signature=3a38933afa097fafbd58fe97e4180358379f4bda37fbc2c825950d4d9044269c&req=cCkuHst7lYRbFb4f3HP0gNCd1Dka%2F%2FCnF4wyMzt5%2BfSAhrepccqzoCwbtHT8%0AbQyf%2Bh4zYjoCwkIH7g%3D%3D%0A)

**Nommer l'environnement**

Nommez l'environnement **API V2** pour l'identifier facilement.

![](https://sellsy-a9cc78fb6d3a.intercom-attachments-7.com/i/o/499825861/e7a9be9940ce8e465ad3dcb1/cc4dea87-ed77-4c64-82da-4d71c8f89307?expires=1788635700&signature=06880e0e526d71f1acf0c0ad42cb2f03ac3af75fd5071cec3937bee68daf4660&req=cCkuHst7lYdeFb4f3HP0gPOVz6b4VXZdXaKzAcI6rUEqzCaU3%2BDXzwXy15wE%0AiyzFNNZxjl13D686Cg%3D%3D%0A)

**Ajouter les variables**

Ajoutez les variables suivantes dans votre environnement :

- url_base
- sellsyApiHost
- sellsyAuthorizationHost
- apiv2_client_id
- apiv2_client_secret

**​Définissez le type :** Défaut

​

**Configurer les variables**

Copiez les tokens générés sur Sellsy et les coller ensuite pour chacune des variables correspondantes (dans *"INITIAL VALUE"* et *"CURRENT VALUE"*)

- Dans url_base, mettre : [https://api.sellsy.com](https://api.sellsy.com/) (dans *"INITIAL VALUE"* et *"CURRENT VALUE"*)

- Dans sellsyApiHost, mettre : [https://api.sellsy.com](https://api.sellsy.com/) (dans *"INITIAL VALUE"* et *"CURRENT VALUE"*)

- Dans sellsyAuthorizationHost, mettre : [https://login.sellsy.com](https://login.sellsy.com/) (dans *"INITIAL VALUE"* et *"CURRENT VALUE"*)

 **Récupérer vos identifiants API**

1. Rendez-vous dans Sellsy sur *"Réglages"* > *"Portail Développeur"* > *"API V2"*
2. Copiez votre **Client ID** et **Client Secret**

**Documentation :** Pour plus de détails sur la génération des tokens V2, consultez la **[documentation API V2](https://api.sellsy.com/doc/v2/)**.

![](https://downloads.intercomcdn.com/i/o/822437743/820ba97eca445d32e114f4dd/variables.png?expires=1788635700&signature=f98eb6910ec201bcc479d9d9957d136d3964ca8de3ac02eaaa5d53a270bb2e79&req=fCIlEsp5moVcFb4f3HP0gCx0yxForYF8mQ4t43YFK8PCcPOQpWF40xzAnNbP%0ACaUderhr17OEJIkwnQ%3D%3D%0A)

___________________________________________________________

### **Configuration pour accès privé (optionnel)**

Si vous utilisez un **accès de type privé** (au lieu d'un accès personnel), vous devez configurer une URL de redirection spécifique.

**Modifier l'URL de redirection dans Sellsy :**

1. Depuis Sellsy, accédez à votre accès API V2 de type privé
2. Dans le champ *"URL de redirection"*, renseignez :
https://oauth.pstmn.io/v1/browser-callback
3. Enregistrez les modifications

![](https://downloads.intercomcdn.com/i/o/796743912/b9f3707b98de39a99b39b842/Acce%CC%80s_prive%CC%81.png?expires=1788635700&signature=c45ca32fc6d357579e6f0c17c2b3fb66e0747b0448956b76525435b22e4e297a&req=cykhEc19lIBdFb4f3HP0gHBH%2B0O1GW8ymYeq%2B40377xKiTnPjiiqtcJcYBjU%0ADeKhUkzXejECQ6TNHg%3D%3D%0A)

**Connexion avec un accès de type privé (Côté Postman) :**

Création accès v2 type privé :

Auth url : [https://login.sellsy.com/oauth2/authorization](https://login.sellsy.com/oauth2/authorization)

Access tokens url : [https://login.sellsy.com/oauth2/access-tokens](https://login.sellsy.com/oauth2/access-tokens)

Callback URL : [https://oauth.pstmn.io/v1/browser-callback](https://oauth.pstmn.io/v1/browser-callback)

![](https://downloads.intercomcdn.com/i/o/796773277/6630a368a04a259b29ad3099/New_token.png?expires=1788635700&signature=863ac041b993203760c310827084c041af896a3147d968df48e2fea7cd698c62&req=cykhEc59n4ZYFb4f3HP0gHAnBOTiQBJJ44snjqOw32d1LMUQlncpcftfLz%2FK%0AdAm2irHsI2g9dMKJ%2Bg%3D%3D%0A)

Ajouter la collection API V2

1. Depuis Postman, cliquez sur *"Collections"* dans le menu de gauche
2. Cliquez sur *"Import"*
3. Cliquez sur *"Upload files"*
4. Sélectionnez le fichier de la collection API V2 Sellsy (fichier JSON) sur votre ordinateur
5. Cliquez sur *"Import"*

Vous pourrez télécharger la collection depuis la page d'accueil de la [documentation de l'API V2](https://api.sellsy.com/doc/v2/) :

![](https://downloads.intercomcdn.com/i/o/1135263066/a47da4eae00a043107341a0c/collection.png?expires=1788635700&signature=3afe843d292f4b10e851469fb331093b90ae78613bafea4673b58a573530df4a&req=dSEkE8t4noFZX%2FMW1HO4zS6p%2F%2Bw1Mxb6ihYgpMTPe2O0e6mRJ%2B9kidj5XURl%0AvP8FIL5I8EZPzo%2F7yio%3D%0A)

Vérification des paramétrages des autorisations 

1. ans Postman, cliquez sur la collection *"API V2"* dans le menu de gauche
2. Accédez à l'onglet *"Authorization"*

**Pour accès personnel : **

![](https://sellsy-a9cc78fb6d3a.intercom-attachments-7.com/i/o/499825882/e99de1255b1fc08a068ff838/38eb4419-3c8c-4e82-8fea-7d6ba38fd00d?expires=1788635700&signature=9b58b6358e11c4a75b3665cacfb5454a641fd99b5b784f80290ea46b5c6bcc55&req=cCkuHst7lYldFb4f3HP0gKmU2utQObn8Q58fSJYZtj9Tu5NAmpHl2cBHSzSX%0ACYPaMmyVp07Ev882kA%3D%3D%0A)

**Pour accès privé : **

![](https://downloads.intercomcdn.com/i/o/970844067/3cdff66599437cae33a9d3e0/Untitled.png?expires=1788635700&signature=f95cb35d3685e6faabfe86d3435ae06e70818c80b5c24e7430779ae8c813428f&req=fScnHs16nYdYFb4f3HP0gO6eM8qo%2BxN9sImH5EU24M4wqkRquMIQvIhL7IFV%0AjzjlaOoQIJHD1cL8Gw%3D%3D%0A)

En déroulant la collection API V2, vous aurez ensuite l’intégralité de toutes les requêtes présentes dans la documentation sur l’API V2.

![](https://downloads.intercomcdn.com/i/o/822405827/d3d532471dd2a0afdaead991/reque%CC%82tes_API_V2.png?expires=1788635700&signature=4556f579ab38bbbc57ab4605b85128ad4d7c8b7317fe89a647b06094c08cd92c&req=fCIlEsl7lYNYFb4f3HP0gFuFsVFpMF%2BzRFwD7yekXAhf5y2jU6IxTG82WveO%0AIEG8IsnZpYmGHatOuQ%3D%3D%0A)

___________________________________________________________

### Récupérer des données Postman sous un autre langage 

Si pour des besoins spécifiques, vous avez besoin de traduire le code que vous renvoie Postman dans un autre langage, voici comment procéder. 

![](https://downloads.intercomcdn.com/i/o/796767658/6e48cacb8e404784b9be76ea/Autre_language.png?expires=1788635700&signature=af230167d0d2fa635bb58106d49344c4da7a7505548e1b0233e054be4ff1b6aa&req=cykhEc95m4RXFb4f3HP0gLQjTuZDOHsIA9kAqgLX7U0%2FtmsBv46049SeM23W%0Ah1zESkuxQ5d0h8dQKg%3D%3D%0A)

Mis a jour le : 13/03/2026
