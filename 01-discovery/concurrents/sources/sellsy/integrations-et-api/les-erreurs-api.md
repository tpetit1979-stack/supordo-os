---
source: https://help.sellsy.com/fr/articles/9448806-les-erreurs-api
categorie: Intégrations et API
titre: Les erreurs API
date_recuperation: 2026-09-05
---

# Les erreurs API

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2159286932/1bf0f405f0e66cc656260be80928/FAQ-Bannie%CC%80reAcademy-2+%282%29.png?expires=1788635700&signature=8da5b80a70d0d05ce23fe9c5b85e4e96b3752412442982493920ef8f9076725c&req=diEiH8t2m4hcW%2FMW1HO4zctfM%2B%2FKDFJyahEGux15P28xtgoF28VFHFaPwTDG%0A1fz4zJMueZWhwld0x%2Fw%3D%0A)

Lorsque vous exécutez vos requêtes, il se peut que vous ayez une erreur en résultat. 

![](https://downloads.intercomcdn.com/i/o/1077095958/e60a9227bb6d35280e70e754/erreurs.png?expires=1788635700&signature=1c83af11c43c24423d58ceee70d42582c3aaeb64b9908a58f977fdfe4d79b04f&req=dSAgEcl3mIhaUfMW1HO4zZsx%2F0LcjKJPT7EbMe3sDp8kxa2uUc%2F7D8%2F7CJf2%0AjmZqnfDksUtjw0HQz%2B4%3D%0A)

___________________________________________________________

### Les différents codes erreurs 

Voici les différentes erreurs que vous pourriez rencontrer : 

- 400 Bad Request : Cette erreur est renvoyée quand il y a des erreurs dans la requête. En général, l’erreur est indiquée à la suite.
- 400 Payment required : Cette erreur est renvoyée quand la personne qui a créé les tokens ne dispose pas de la licence nécessaire pour exécuter la requête (Exemple : une création d’opportunité sans avoir de licence de vente).
- 401 Unauthorized : Cette erreur est renvoyée lorsque l'authentification est non valide. Cela se présentera quand il y a un problème d’identification avec les tokens sur l’environnement. Cette erreur peut aussi être constatée lorsque les tokens sont demandés par deux scripts distincts (Jeton révoqué par un autre) ou lorsque le créateur des tokens API n'a plus d'accès à Sellsy.
- 403 Forbidden : Cette erreur est renvoyée lorsque l'authentification fournie ne possède pas les autorisations nécessaires pour accéder à l'URL spécifique. Par exemple, un jeton OAuth qui dispose uniquement d'un accès à la facturation recevra une réponse 403 lors d’une requête d’opportunités (qui nécessite une licence vente).
- 400 Payment required : Cette erreur est renvoyée quand la personne qui a créé les tokens ne dispose pas de la licence nécessaire pour exécuter la requête (Exemple : une création d’opportunité sans avoir de licence de vente).
- 429 Too many requests : Cette erreur est renvoyée quand votre compte ou application dépasse ses limites quant aux API. Nous recommandons de mettre un délai de 200 MS entre chaque appel pour un bon traitement des données. Généralement, une optimisation du code permet de résoudre le problème (Utilisation méthode de batch).
- 500 Internal server error : Ce code d'erreur indique que le serveur est temporairement indisponible ou en maintenance. Ce message vous indique donc que votre site est en ligne et qu'il fonctionne, mais qu'il est actuellement et temporairement inaccessible.
- 502 Bad Gateway : Cette erreur se produit lors de la mise à jour du serveur API pendant un laps de temps très court. Pour s’en prémunir, il suffit de mettre en place une approche de retry.

___________________________________________________________

### Les erreurs de process 

Les erreurs de process sont renvoyées par l'API dans l'objet réponse. Chaque erreur possède un identifiant, ce qui vous permet de personnaliser les messages. Voici les différentes erreurs de process que vous pourriez rencontrer :

- **E_USER_NOT_LOGGED** : L'utilisateur n'est pas connecté.
- **E_IO_MODE_DONT_EXIST** : Le mode d'input/output n'existe pas.
- **E_IO_MODE_DO_IN_MISSING** : L’attribut DO_IN de l’API V1 est manquant.
- **E_DO_IN_WRONG_FORMAT** : Le format d'entrée est mauvais.
- **E_METHOD_DONT_EXIT** : La méthode spécifiée n'existe pas.
- **E_DO_IN_PARAM_MISSING** : Le paramètre DO_IN est manquant.
- **E_PRIV_NOT_ALLOWED** : L'utilisateur ne dispose pas des privilèges pour accéder à cette ressource.
- **E_SUBSCRIBE_HAVETO** : L'utilisateur a besoin de souscrire à un abonnement pour accéder à cette ressource.
- **E_PARAM_MISSING** : Le paramètre est manquant.
- **E_PARAM_INVALID** : Le paramètre est invalide.
- **E_PARAM_REQUIRED** : Le paramètre est manquant ou incorrect et il est obligatoire.
- **E_OBJ_NOT_LOADABLE** : La valeur passée ne fait pas référence à un objet utilisable pour cet appel.
- **E_OBJ_NOT_EDITABLE** : Un objet n’est plus modifiable (Facture finalisée).
- **E_OBJ_NOT_LOADED** : L'objet n'est pas chargé.
- **E_LIST_DONT_EXIST** : La liste n'existe pas.
- **E_LIST_VALUE_DONT_EXIST** : La valeur demandée n'existe pas dans la liste.
- **E_PAGINATION_MAX** : Le paramètre pagination est incorrect.
- **E_UNKNOW** : Erreur inconnue.
- **E_CUSTOM** : Erreur manuelle.
- **E_CORPORATION_BLOCKED** : Account blocked. Contact us.
- **E_PLUGIN_NOT_LOADED** : Plugin is not loaded.
- **E_QUOTA_NOT_SUFFICIENT** : Quota for plugin is insufficient.
- **E_FEATURE_DISABLED** : Feature is disabled, you need to upgrade your account.
- **E_LICENCE_BLOCKED** : Current licence is blocked.
- **E_LICENCE_NO** : No licence available.
- **E_LIMIT_REQUEST_REACHED** : You reached the limit of requests. Please contact us for further informations.
- **E_SERVICE_UNVAILABLE** : We can not perform your request. Please re-try later.

Mis a jour le : 13/03/2026
