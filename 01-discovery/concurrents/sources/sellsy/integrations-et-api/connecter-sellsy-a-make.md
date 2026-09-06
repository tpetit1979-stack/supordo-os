---
source: https://help.sellsy.com/fr/articles/7994804-connecter-sellsy-a-make
categorie: Intégrations et API
titre: Connecter Sellsy à Make
date_recuperation: 2026-09-05
---

# Connecter Sellsy à Make

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2159356529/ff0e7b52bae9aced66a1e55a69d6/FAQ-Bannie%CC%80reAcademy-2+%282%29.png?expires=1788635700&signature=3483029f7389ce3f66ff10b0c0d50ada0fa664514b51a0738bbf2e23d67cdbc5&req=diEiH8p7m4RdUPMW1HO4zXzEBRpiqckbKSSpHtd7KnGMYe83TO3sXicdigv6%0AppcP8Mz%2FEspKI1qsM5E%3D%0A)

> **Attention** : Make ne propose plus de connexion avec les tokens personnels, seul l’accès privé est disponible (flux: Flow authorization code). 

Pour connecter Sellsy à Make, vous devez, au préalable, avoir généré des tokens API v2. Pour ce faire, veuillez suivre [ce tutoriel](https://help.sellsy.com/fr/articles/5876615-types-d-acces-api). 
​
Lors de la création d'un token public ou privé en API v2, une URL de redirection vous sera demandée, veuillez renseigner l'URL suivante :  [https://www.integromat.com/oauth/cb/sellsy2](https://www.integromat.com/oauth/cb/sellsy2)

> **Bon à savoir** : Nous recommandons d'accepter toutes les autorisations. 

![](https://downloads.intercomcdn.com/i/o/761556868/e88a6648c2ef1e867c440f90/token.png?expires=1788635700&signature=91dbb1786547fee4823dc1808cf12ea4194cdd163a52a7ced793ccdbc7dd099e&req=cyYmE8x4lYdXFb4f3HP0gIZOa0o8TZcFz2ky%2BRzLdf9OZ%2BLnT9bW%2FvBgisN6%0AQOD6fAuMAOkuvnMndg%3D%3D%0A)

Sélectionnez ensuite le type de tokens que vous avez généré précédemment.

![](https://downloads.intercomcdn.com/i/o/760077756/c543c6203b857a2a3f8989ff/create_connection.png?expires=1788635700&signature=31e8a7717f84b9d45d66fefad84fc2508c371ab89d62abc4fd8a9de66dea5ff6&req=cyYnFs55moRZFb4f3HP0gOoZos7lnXpaAVrfjSrm6gjDt3I2YsOMArEb0CSt%0AnkIXVlb5xbcPvziDYQ%3D%3D%0A)

Puis renseignez le Client ID et le Client Secret. 
​
Enfin, ouvrez les paramètres avancés en cliquant sur *"Show advanced settings"* et cochez tous les scopes d'autorisation sauf *objectives.read* et *objectives.write*
​

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/1340069351/27402da27740e9e1a02d585e79d3/advanced+settings.png?expires=1788635700&signature=e23d59e5f4436d67edd5070cd7f3a373f73e6887e53d54602e5c4de7f6e68fb5&req=dSMjFsl4lIJaWPMW1HO4zfw6tHtWcVG6tPhvlWpa2J5AvWaMg%2FDfiY2GTDnE%0Amd6r64ijCQviRNvKalg%3D%0A)

> **Bon à savoir :** Nous recommandons la création d'un accès API privé dédié à l'utilisation de Make. En effet, cela pourra vous éviter le changement d’identifiants sur d’autres logiciels par révocation de tokens. 

___________________________________________________________

### Pour aller plus loin 

- [Faire une requête HTTP avec Make](https://help.sellsy.com/fr/articles/9701233-faire-une-requete-http-avec-make)

Mis a jour le : 12/06/2026
