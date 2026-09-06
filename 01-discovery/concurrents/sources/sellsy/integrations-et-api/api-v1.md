---
source: https://help.sellsy.com/fr/articles/5876609-api-v1
categorie: Intégrations et API
titre: API V1
date_recuperation: 2026-09-05
---

# API V1

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2159248340/cc04133371a405e28fe4ac2743bc/FAQ-Bannie%CC%80reAcademy-2+%282%29.png?expires=1788635700&signature=e307455316891f277d63d40861e6bf6a1410afa6cead90f3324f689d6cf637a6&req=diEiH8t6lYJbWfMW1HO4zeaXL8%2FkTfvSghdmjWl9bXxrywYXudVBe0%2Fy3PAG%0AmOOSld9nmxfVucm1%2FEk%3D%0A)

Nous travaillons actuellement sur une [nouvelle version de notre API](https://help.sellsy.com/hc/api/api-v2). L’API V1 est toujours maintenue, mais elle ne fait plus l’objet de nouvelles évolutions.

L’API V2 ne propose pas encore l’ensemble des fonctionnalités disponibles dans l’API V1. Cette dernière reste donc, pour le moment, nécessaire pour certains usages.

___________________________________________________________

### Documentation 

La documentation de l'API V1 est disponible depuis [https://api.sellsy.fr/](https://api.sellsy.fr/)

Sur le site de l'API, vous trouverez toutes les informations nécessaires pour :

- Établir une connexion selon votre type d'authentification
- Comprendre la structure des requêtes et des réponses
- Gérer les erreurs et codes de retour

La documentation de toutes les commandes disponibles est accessible depuis l'onglet *"Documentation"* > *"Méthodes"*.

![](https://downloads.intercomcdn.com/i/o/778039697/5d3b22651a74473127016302/Methode.png?expires=1788635700&signature=343c6ae8f41139bfd0318f7b169781f81d7af08e54d59980255b4860c3ea0f18&req=cycvFsp3m4hYFb4f3HP0gJebBTEnrFCspJ59ewZrNPfEHDNaiOzlCH6j%2BdCL%0A4wd93vp%2Fzz3IiUdP7w%3D%3D%0A)

___________________________________________________________

### Création d’un token 

Pour utiliser l'API V1, vous devez d'abord créer un accès API et générer vos tokens d'authentification.

**Accéder au Portail Développeur**

1. Depuis votre compte Sellsy, ouvrez le menu principal
2. Accédez à *"Réglages"*
3. Cliquez sur *"Portail Développeur"*

![](https://downloads.intercomcdn.com/i/o/1077055604/1881dff1cb530585c790bc89/portail+de%CC%81veloppeur.png?expires=1788635700&signature=d528a91698561bb3398a8ec9c985cab756f3de3d6a3646e5f67d2378d7173e33&req=dSAgEcl7mIdfXfMW1HO4zf9FY1H8uLI5%2F%2B%2Bd3pRPi%2BDZMQFxusDi79VamZAV%0AQJxCzvOemHp2%2B310eYQ%3D%0A)

**Créer une nouvelle application**

1. Depuis la page Portail Développeur, cliquez sur l'onglet *"API V1"*
2. Cliquez sur *"Ajouter une application"*
3. Une fenêtre s'affiche

![](https://downloads.intercomcdn.com/i/o/1077060876/db88be0d9b950e0d5c79ffdf/APIV1.png?expires=1788635700&signature=f879424d86cdffe0cbd8847bbb2771d07bc95658fd3fbf886d588bc3740cdb34&req=dSAgEcl4nYlYX%2FMW1HO4zbegbZPDmM7lEEJ2lGdFpiF3HyP8iNDDLZLFbTGX%0AgZwu40f73OQmxhI5PSM%3D%0A)

Renseignez les informations suivantes, puis cliquez sur *"Valider"* pour créer l'application.

![](https://downloads.intercomcdn.com/i/o/1077068138/649425f291a8f0f68bb5f34f/Ajout+d-une+appli.png?expires=1788635700&signature=783dbf5eb67ba1d76c58b778a42bf43a32bf8add8be117ebb258f819f36d82cf&req=dSAgEcl4lYBcUfMW1HO4zSNRSgRc45m0aoShILoZ1%2Boi3x06Ay43IMCD26%2F8%0Azl3BZs4T3Za45aPiQfI%3D%0A)

> **Attention :** Le niveau de privilège de vos tokens reprend [le profil de privilège du collaborateur](https://help.sellsy.com/fr/articles/5864112-profil-de-privileges) propriétaire des tokens. Il est donc recommandé que ce soit un administrateur qui crée l’accès. 
> Si le compte du collaborateur venait à être désactivé ou supprimé, les tokens associés deviendraient automatiquement inutilisables. Le créateur des accès API doit donc toujours avoir un accès à Sellsy. 
> ![](https://downloads.intercomcdn.com/i/o/p6qpddj1/1567948853/01a42f257b8b17dc26f134d2ca03/Cursor_et_Capture_d%E2%80%99e%CC%81cran_2025-06-12_a%CC%80_16_34_33.png?expires=1788635700&signature=c3bd62c1a1d02b0109fb828299e41beb0f22a400610ed24949a438dee1e418e9&req=dSUhEcB6lYlaWvMW1HO4zd75fnXhOVWg68K%2FJxADkBdova7o0O86O3IuVCkB%0AUJTKec6sRIPSUPczuDw%3D%0A)

> **Bon à savoir :** L’URL API pour une authentification en V1 est : [https://apifeed.sellsy.com/0/](https://apifeed.sellsy.com/0/) 

Vous aurez ensuite accès aux tokens à renseigner sur l’interface développeur que vous utilisez. 

![](https://downloads.intercomcdn.com/i/o/1077071750/e08fb5aaa096ff7d24e464fd/tokens.png?expires=1788635700&signature=a44a31b5d004a2d5fb2ad366a462c0fb8c77b8b004ce0cf199a4cf972bc08ca4&req=dSAgEcl5nIZaWfMW1HO4zbyb2C0ImEOoIVmaMRiTFU8onS9dm3gRLKGn22lf%0A2FrfyrgSVTXpuKBUySM%3D%0A)

N’oubliez pas de cliquer sur *“Générer un token utilisateur”* pour obtenir également les tokens à ce niveau.

> **Bon à savoir : **Vous pouvez retrouver plus d'informations sur l’authentification dans la rubrique : [https://api.sellsy.fr/documentation/intro](https://api.sellsy.fr/documentation/intro)

___________________________________________________________

### Pour aller plus loin

- [Configuration Postman API V1](https://help.sellsy.com/fr/articles/6154289-configuration-postman-api-v1)

Mis a jour le : 13/03/2026
