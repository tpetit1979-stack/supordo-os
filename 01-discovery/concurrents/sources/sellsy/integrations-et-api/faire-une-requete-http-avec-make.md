---
source: https://help.sellsy.com/fr/articles/9701233-faire-une-requete-http-avec-make
categorie: Intégrations et API
titre: Faire une requête HTTP avec Make
date_recuperation: 2026-09-05
---

# Faire une requête HTTP avec Make

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2159359780/407292619f97ed8a3550660b9af7/FAQ-Bannie%CC%80reAcademy-2+%282%29.png?expires=1788635700&signature=3be811a1df2b863593a87e064310926c85b86d3c6d0a89f293a0a7954c75d509&req=diEiH8p7lIZXWfMW1HO4zahf6pIisFC0A1Vtye9Xb5RbvTdJ1Vt%2BLpPTxdEd%0AonFfhe7cWdLwZ1rZpNA%3D%0A)

Voici les étapes à suivre pour **faire une requête HTTP sur Make** : 

![](https://downloads.intercomcdn.com/i/o/1135307162/bb1d6c80e52beb4e0bfef7f9/reque%CC%82te+HTTP+Make.png?expires=1788635700&signature=4d8a3d0486c33dfc07b5c43df9dce4917de82c243258ae080faa197ad2db2864&req=dSEkE8p%2BmoBZW%2FMW1HO4zaOUG7tVhMatYD6V2XnHY35%2Fu3GhoYlnYu3awpXW%0Ai0y%2Fe9rKGPlNmUsxFX8%3D%0A)

**1. Authorize URI :** [https://login.sellsy.com/oauth2/authorization](https://login.sellsy.com/oauth2/authorization)

**2. Token URI :** [https://login.sellsy.com/oauth2/access-tokens](https://login.sellsy.com/oauth2/access-tokens)

**3. Client ID :** à générer dans Sellsy (clé privée)

**4. Client Secret :** à générer dans Sellsy (clé privée)

**URL de redirection :** 
​[https://www.integromat.com/oauth/cb/oauth2](https://www.integromat.com/oauth/cb/oauth2)

[https://www.integromat.com/oauth/cb/sellsy2](https://www.integromat.com/oauth/cb/sellsy2)

> **Bon à savoir :** Pour les étapes 3 et 4, veuillez créer des tokens V2 depuis votre compte Sellsy en suivant [ce tutoriel](https://help.sellsy.com/fr/articles/5876614-api-v2). 

Il faudra ensuite aller sur [https://developer.pingidentity.com/en/tools/pkce-code-generator.html](https://developer.pingidentity.com/en/tools/pkce-code-generator.html) et cliquer sur *"GENERATE NEW"*. 

**5. Authorize parameters :**

- Item 1 : 
- Key : code_challenge
- Value : Valeur générée par PKCE
- Item 2 : 
- Key : code_challenge_method
- Value : S256

**6. Access token parameters :** 

- Item 1 : 
- Key : code_verifier
- Value : Valeur générée par PKCE

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/1580052525/77232c8bd9388eb2e8167ec9c6d9/image.png?expires=1788635700&signature=7431d9c0bbc4561779e6a100c99dc53175ed92a5bee89c8b124f628abb9cefc1&req=dSUvFsl7n4RdXPMW1HO4zbl54Plg3Z08TyaE1817kAW0qG1CYgjwX0ahViR0%0A0c8QClMmAjwkIxjO5Ls%3D%0A)

___________________________________________________________

### Pour aller plus loin 

- Suivez notre guide pour connecter Sellsy à [Make](https://help.sellsy.com/fr/articles/7994804-make)

Mis a jour le : 13/03/2026
