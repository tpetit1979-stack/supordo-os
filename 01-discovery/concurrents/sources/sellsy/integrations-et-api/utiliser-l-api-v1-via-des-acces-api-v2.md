---
source: https://help.sellsy.com/fr/articles/8544417-utiliser-l-api-v1-via-des-acces-api-v2
categorie: Intégrations et API
titre: Utiliser l’API V1 via des accès API V2
date_recuperation: 2026-09-05
---

# Utiliser l’API V1 via des accès API V2

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2159274648/80aa679a01aa362add9b53b95dc6/FAQ-Bannie%CC%80reAcademy-2+%282%29.png?expires=1788635700&signature=62310a63ad879f342826f0c665e416ae12d8ff3fb484ac0e9be8a121c0a8b905&req=diEiH8t5mYdbUfMW1HO4zb7eikc%2BnsZRP8wE12Io7ncVQBzFrjTqrp3WNbuk%0AR7GQTmw4b4i4w0%2BybkY%3D%0A)

Pour le moment, toutes les requêtes V1 ne sont pas encore disponibles sur l'API V2. Cependant, il est tout à fait possible de passer des requêtes API V1 en utilisant des accès V2.

___________________________________________________________

### **Activer le scope API V1**

Pour pouvoir utiliser l'API V1 via un accès V2, vous devez d'abord activer le scope approprié.

**Accéder aux paramètres de votre accès**

1. Depuis le menu Sellsy, accédez à *"Réglages"*
2. Cliquez sur *"Portail Développeur"*
3. Sélectionnez l'onglet *"API V2" et *assurez-vous que le scope API V1 est bien activé
4. Ouvrez votre accès API V2

![](https://downloads.intercomcdn.com/i/o/873596629/ee0c28954bf098ad62435c44/Scope_V1.png?expires=1788635700&signature=b01bd978631b31032e397c690eb2c5f7b8ac4e209152c6a895b01462013758ab&req=fCckE8B4m4NWFb4f3HP0gL8VhcNoZnRYVr8pZzw4r7Zglro%2B0YDgazyvTiwU%0Azq2rq3uDpwTFSuSv%2Fw%3D%3D%0A)

**Utiliser l'authentification OAuth 2.0**

Pour appeler l'API V1 via un accès V2, utilisez **OAuth 2.0** comme méthode d'authentification. 

URL des appels V1 : [https://apifeed.sellsy.com/0/](https://apifeed.sellsy.com/0/) 

Dans le header : 

- “Authorization” : Bearer <votre_access_token>”
- "content-type" : multipart/form-data

> **Attention :** Tous les appels sont en **Post** (même les récupérations de listes). 

Exemple depuis Postman : 

![](https://downloads.intercomcdn.com/i/o/873602342/b22ba30080d0a579899c2833/Exemple+Postman+1.png?expires=1788635700&signature=2afc25e63a2253df77d3f2ab2a9ef94bfadc89b5590e6b1287b74cff7777c396&req=fCckEMl8noVdFb4f3HP0gL0Ldi70sPTAz7c5NcPIH92bm4twXfeqvOlFfj8S%0A6l1uU3xYxg6ztCpCCw%3D%3D%0A)

![](https://downloads.intercomcdn.com/i/o/873602491/4281de5cde56f5bf23f8637f/Exemple+Postman+2.png?expires=1788635700&signature=407f166adb722e9f09e18901c9750823f5d88d7048ff4e67cf56ce0728426b39&req=fCckEMl8mYheFb4f3HP0gJCA9VwXNI98o8nv6mtRMKU3ykVWR5nzW3GpobnG%0AbcWxc2Y9ovHqYm%2F5Gw%3D%3D%0A)

Si vous utilisez Make, voici un exemple de configuration :

![](https://downloads.intercomcdn.com/i/o/873602920/289b15108276529169b6e64d/Exemple+Make.png?expires=1788635700&signature=844535945a4f24c3dd29e785e6b2b1de2530d5404bf5ea2dca97b46ddde34ced&req=fCckEMl8lINfFb4f3HP0gDUdzjfb4wC%2BTI36pkCpNWzESERoBTqO6uNdthfO%0AnrUwTV0Me1tro%2B8z6g%3D%3D%0A)

Si vous utilisez un outil ne permettant pas les appels multipart/form-data, voici une autre approche possible : 

Dans le header : 

- “Authorization” : Bearer <votre_access_token>”
- "content-type" : application/x-www-form-urlencoded

​ 

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/1316913119/7eedbbbbcb7bdde9762bbc1764d8/approche%2BJSON%2B1.png?expires=1788635700&signature=88116351ab259ef7d495a569f1e9de96404320d80880faed97434d6e4bd7b5ae&req=dSMmEMB%2FnoBeUPMW1HO4zVKV%2F4Q%2BM%2FlEQ4uMzIKtxTuLWVHW5fRo4zm4c8KX%0A65LmBiiM%2Fv72B5NRNCc%3D%0A)

Mis a jour le : 13/03/2026
