---
source: https://help.sellsy.com/fr/articles/5876615-types-d-acces-api
categorie: Intégrations et API
titre: Types d'accès API
date_recuperation: 2026-09-05
---

# Types d'accès API

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2159158740/731572517b863b0984d6d797d634/FAQ-Bannie%CC%80reAcademy-2+%282%29.png?expires=1788635700&signature=24f56909f9adf1b73ad55ac46f8231a55d9cb31848871cabd7a2c42fe8228f29&req=diEiH8h7lYZbWfMW1HO4zTm%2B4qd%2BG1OdtHcXKf2pDdTm15g4am1kCldUViJQ%0AVUXCbGx8w3Obijoiqzk%3D%0A)

___________________________________________________________

### Créer un accès API

Pour créer un accès API pour votre application, rendez-vous sur *“Réglages”* puis sur *“Portail Développeur”*.

![](https://sellsy-a9cc78fb6d3a.intercom-attachments-7.com/i/o/454005283/accf4ea3ec86950631305fb5/BWxNBGwCTcCCMfD7RPIb6-DQ6S7oRChS6cjZ0qztuYvk5kJozNdULpLovFL3aVL5Y0YhEeVoAHiyb-Ke1o82G2a9NKvi1BhQIe4rJnekhbSCAKwgLMNkP2xBRH6dCrvN9wV7j9Mp?expires=1788635700&signature=617f15fa28b046202fb3525195083c16ac75e77446c6a265c692b72f216e3449&req=cCUjFsl7n4lcFb4f3HP0gLoW5cv0MC5XgRpoxHSeR7RR3gqMwLnKAGFFF7%2Bd%0Am4YcsNNFWEVxQXQ54w%3D%3D%0A)

 
En débutant la création de votre accès API, vous pourrez choisir le type d’accès : 

- **Public : **pour des raisons de sécurité, ce type d’accès est réservé aux partenaires Sellsy.
- **Personnel :** pour une connexion **serveur à serveur**.

> **Bon à savoir :** Les droits du collaborateur associé et sa licence seront appliqués à l'accès API.

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/1394354195/71796fcc1d5babb09522ba0e3e90/personnel.png?expires=1788635700&signature=7a57fda285104780e6daa1026597708973f9c825da9ed4da24664c03122651d6&req=dSMuEsp7mYBWXPMW1HO4zS10msaSBq09KD6Ir9vCyKFlOs%2FdQsHn8Hbrcv6Y%0A2YHTc5j3QEHEfGM4JiE%3D%0A)

- **Privé :** pour une connexion **client à serveur**.

> **Bon à savoir :** Les droits du collaborateur se connectant et sa licence seront appliqués à l'accès API.

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/1394355239/2b94f536f15f393c7f921f8e59d4/prive%CC%81.png?expires=1788635700&signature=9c0401d740481d82af2d73141279adb81c416696744b70c4e76653bc7d2cc25c&req=dSMuEsp7mINcUPMW1HO4zcXbTEOxct%2BMrXselq7MBi4peSaTk5wAzdDlAHZ1%0AnOMj476F8YkRIVJ6N7o%3D%0A)

___________________________________________________________

### **Autorisations (Scopes)**

Les autorisations, autrement appelées **scopes**, permettent de limiter, si nécessaire, les droits de l'accès API.

**Fonctionnement :**

- Si vous ne voulez aucune restriction, cochez toutes les autorisations
- Si vous souhaitez limiter les actions possibles, sélectionnez uniquement les scopes nécessaires

> **Bon à savoir** : Parmi les scopes, vous avez la possibilité d'utiliser l'API V1 via votre accès API V2. Vous trouverez plus d'informations à ce sujet dans l'article **[Utiliser l'API V1 via des accès API V2](https://help.sellsy.com/fr/articles/8544417-utiliser-l-api-v1-via-des-acces-api-v2)**.

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/1394356654/a2c86f4a9c5a7e44db82eb63ac18/6sRHnWOF7Z2u5olxBsuuzuOb8I6AgL6GYe_7DrJGgzeRSuhYhmbnUtSwYqA4WQArn-QaXLht-PIzFlKqvnGYTBXnhhKSwRgeWcmCYt0J5-Qx1zu4v_KlKn8BcyJ7fRpoQRUt45vo?expires=1788635700&signature=68436346e5230a1707d620e9c6a5b56aa94acea12d049d6244caee180e52f2ac&req=dSMuEsp7m4daXfMW1HO4zYqnDEt1FVe%2BrBfvVWRFIXQJrj2HBek8nE0f28jz%0AnvHri21Nci2Tdf9YyMY%3D%0A)

- **Tokens de type personnels,** ce type d’accès vous permet de connecter une application externe à Sellsy et d’échanger des informations en utilisant votre accès collaborateur.
- **Tokens de type privés,** ce type d'accès vous permet de créer une application externe à Sellsy, les collaborateurs de votre compte Sellsy pourront se connecter à l’application avec leurs identifiants Sellsy.

![](https://sellsy-a9cc78fb6d3a.intercom-attachments-7.com/i/o/454005302/2a20dc6ef655390c21db4e83/kN2odizz-8UWkOfZjb3Y2MliZ2-wWIlggHl6lZ8AhMXOAPLNKpFAs_7mSk5xU6vERAzPXGHjDkm9j-kYjGWlyuyxVl_xbi7lXWvx1UXD7CRnJ7ZMDpDaX12atZkI0UGZZl9nOah-?expires=1788635700&signature=dd663fbfbbfc654c2212a78f16f9c3472e71689361896c0bb14a67a757e1fdf4&req=cCUjFsl7noFdFb4f3HP0gJcI7ajCcRFXA%2BL3QFOi1N3HE7KsycjaCZtcmP97%0AJo8yVz3cfs96N9%2BosQ%3D%3D%0A)

Une fois votre connexion effectuée, il ne vous reste plus qu'à autoriser votre application à accéder à votre compte Sellsy.

![](https://sellsy-a9cc78fb6d3a.intercom-attachments-7.com/i/o/454005311/e725d0d9c3f35b4e3b2f965e/80SEAMxTGci8eUxCqm0ui03b3JuMLC0rqKy3N4jgDMwXKsmvPPVibhNr9sL9QdyeZxLSTHr8a7SJc8VlIlCU3PO9PNFoKWF7vL9FK-sOgZoeHHS1SHy5rlP0ui2kJfW5aYAZzWQs?expires=1788635700&signature=ad4e56ef6e764a4190fd49b3181583059a849043e4f1f6f9ff53e3384b2867a7&req=cCUjFsl7noBeFb4f3HP0gBuMFal7z7kHP0QYTPClevvxLNNcnwkVKIZrfRZM%0A6AT2ZrkCpgxBo2SEOA%3D%3D%0A)

**Tokens de type publics : **ce type d'accès vous permet de créer une application externe à Sellsy, l’ensemble des utilisateurs Sellsy pourront tout simplement se connecter à votre application avec leurs identifiants Sellsy.

> **Bon à savoir :** Les accès de type Privés et Publics nécessitent une Url de redirection commençant par http ou https.

> **Attention :** Pour des raisons de sécurité, un accès de type public doit être validé par nos équipes pour justifier son utilisation. Pour cela, merci de nous envoyer un mail à [contact@sellsy.com](mailto:contact@sellsy.com)

___________________________________________________________

### **Client ID et Client Secret**

Pour chaque type d'accès, un **Client ID** et un **Client Secret** seront générés automatiquement.

**Important :** N'oubliez pas de les copier immédiatement après la création de l'accès afin de pouvoir authentifier et connecter votre application.
​

> **Attention :** Le Client Secret ne sera affiché qu'une seule fois. Si vous le perdez, vous devrez créer un nouvel accès API.

![](https://sellsy-a9cc78fb6d3a.intercom-attachments-7.com/i/o/454005320/3a9859a2cfaf5e67d2b5667a/OaPr3-agr9OEWTfadZB1ZGOXOixGQoArL_hWUhjakmoMKozZ3JsSnkmknJdKWBs9kWdMOOfQ3kUX79g06OGApSZ49DlmMq42uRDapMlZtQ7xjM4dp0JOZN6bMhy0q2pVHAJMTXps?expires=1788635700&signature=3b2461678c75bf494b01140f54e490be42f9fd1845c0fd085ef9f10ecf8945cc&req=cCUjFsl7noNfFb4f3HP0gBx3s9Mghym%2F7p%2F8NXa2VXe%2Bkp5Uvhfnkdskkh6n%0A%2B%2BBM3xTAh7gd0oO3tQ%3D%3D%0A)

___________________________________________________________

### **Liste des accès API **

La liste des accès API est disponible dans la rubrique *"Réglages"*, *"Portail Développeur"*, *"API v2"*.

![](https://sellsy-a9cc78fb6d3a.intercom-attachments-7.com/i/o/454005331/06bda57ad92cfb8dd486b17a/dUehlGcEvMe89xLXVP3mTVX556htJRngG4058W_EJ8NN07pxwwpo8cUbrduijAmRTY5XuAnZUEzp1slK2eSrb665koqyioVfeMYH7zoshlLvFe40Fj8IOCR1qigJKI9KsjFHsyhn?expires=1788635700&signature=742156784de97bbdd0ecda8af6ff4adc68942c8abebef9d0068435883681d90b&req=cCUjFsl7noJeFb4f3HP0gIX9jPYmXp4CbaEOH7BHl%2B4h5ub39i51cVeTYFhB%0A5cH78AfP%2FCJCddbiQw%3D%3D%0A)

___________________________________________________________

### **Tester vos accès API avec Postman**

Pour tester vos accès API, nous vous recommandons d'utiliser Postman, un outil gratuit de test d'API.

**Configuration selon la version d'API :**

- **[Configuration Postman API V1](https://help.sellsy.com/fr/articles/6154289-configuration-postman-api-v1)** : Guide de configuration pour tester l'API V1
- **[Configuration Postman API V2](https://help.sellsy.com/fr/articles/6154292-configuration-postman-apiv2)** : Guide de configuration pour tester l'API V2

Ces guides vous accompagnent pas à pas dans la configuration de Postman pour effectuer vos premiers appels API. 

Mis a jour le : 13/03/2026
