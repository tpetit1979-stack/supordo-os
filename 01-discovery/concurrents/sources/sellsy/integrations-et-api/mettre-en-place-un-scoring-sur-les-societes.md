---
source: https://help.sellsy.com/fr/articles/5877012-mettre-en-place-un-scoring-sur-les-societes
categorie: Intégrations et API
titre: Mettre en place un scoring sur les sociétés
date_recuperation: 2026-09-05
---

# Mettre en place un scoring sur les sociétés

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2159328660/740655610b3f1ff4c2f47686ea74/FAQ-Bannie%CC%80reAcademy-2+%282%29.png?expires=1788635700&signature=c73fa1a00ad9168ac542b7a5b7a2df6c95dfefd396ccd3d2c45ef8968b01bb79&req=diEiH8p8lYdZWfMW1HO4zeCI1D67zsSC0034UQtZHKBtra7mk%2B2p4QpFB2f3%0AdczlSrWej68OUcIpWoQ%3D%0A)

Si vous avez mis en place le Widget Sellsy et activé le tracking des clients et prospects, vous pouvez mettre en place une logique de scoring à partir des événements de navigation (visite de page / soumission d’un formulaire) de vos contacts sur votre site web.

L’objectif est de pouvoir identifier rapidement les prospects à contacter, gagner du temps sur la phase de qualification et d’augmenter votre taux de conversion.

___________________________________________________________

### **Configurer un scoring **

Tout d’abord, vous devez configurer votre modèle de scoring. Pour cela vous allez choisir certaines actions de tracking et leur attribuer un pourcentage (visite d’une page ou soumission d’un formulaire).

Pour configurer votre scoring, vous devez vous rendre dans la rubrique “*Réglages*” de votre menu, puis sur “*Scoring client/prospect*”.

![](https://sellsy-a9cc78fb6d3a.intercom-attachments-7.com/i/o/446446268/6b3807a52f3f84a1020b05b7/0L4716GTEuRc9oYkcIwFFKq_axFgOx4pJH3h8BcvWWPC0r8XxKoaI54LadUn973jNefUDEcb2uMHYC9QlccRJt-Lfn3wA84XmJVX0xzsPbpoaaO3MDXIP2OoYDd7prmQo-ItKmMJ?expires=1788635700&signature=66339e190788812f1a67c19a2c819f86ee6f369f979ff7e119cf2881a3a93b95&req=cCQhEs14n4dXFb4f3HP0gM1uOFtlLcUWmP61jUL15u2x9UVr0v8q5vzdB4yz%0AlUFy7ejT293OLwGPDA%3D%3D%0A)

La liste principale présente l’ensemble des évènements de scoring déjà définis. Vous pouvez cliquer sur “*Nouvel événement*” en haut à droite de la page pour ajouter une nouvelle règle de scoring.

![](https://sellsy-a9cc78fb6d3a.intercom-attachments-7.com/i/o/446446287/7ea6ac4922eb1613d95dee35/RXTJmXKtkfKY0T1CuVKaJGhCVHvMWrXXo9hWhWjvuo5Tk-JvIySf-cI8DHsuHIJef6FmmausybVcvIoVKlNzEZVy97uCySaxIzA2VP_FkfwuXmtismOtrP6YDKYIceWEufBEKuko?expires=1788635700&signature=15e908172c1ce6a34af74aeaba316e243f3115d53005beecaa32eb183f6e7452&req=cCQhEs14n4lYFb4f3HP0gD%2B2Hnk3emgeodHlGjh2PYmIuw99o7IMAJ53tNNT%0Aao3aWYkRoyGzirAuFQ%3D%3D%0A)

Un événement de scoring peut correspondre à deux types d’action :

- Visite d’une page,
- Soumission d’un formulaire.

___________________________________________________________

### **Configurer un événement de scoring pour une visite d’une page**

Vous devez indiquer le nom de l’évènement et choisir le type d’action “*visite d’une page*”. Vous pouvez choisir le pourcentage que vous souhaitez attribuer (entre 1 et 100).

Ensuite vous devez spécifier l’url ou les urls correspondantes.

![](https://downloads.intercomcdn.com/i/o/525289274/3705c962c4591659be4bad08/Capture+d%E2%80%99e%CC%81cran+2022-06-06+a%CC%80+17.46.34.png?expires=1788635700&signature=607c516eaa51f7029a4c692a9787b57bd98af165f861a7cbadfbe44b6dcb7b2f&req=cSIiFMF3n4ZbFb4f3HP0gO7Y318LOb8XcH9Jlq681DFMTcRFyk07Rjyar0EM%0A8OTZfXtej6f8kv7CIA%3D%3D%0A)

###  

___________________________________________________________

### **Configurer un évènement pour la soumission d’un formulaire**

Vous devez indiquer le nom de l’évènement et choisir le type d’action “*soumission d’un formulaire*”.

**L’identifiant HTML** correspond à l’ID HTML du formulaire. Vous pourrez retrouver cette information dans le code source de votre page. Sur les navigateurs récents, vous pouvez utiliser la fonctionnalité “*Inspecter l'élément*” (en faisant un clic droit sur le formulaire) pour parcourir le code source. Pour finir, vous devez spécifier l’url sur laquelle se trouve le formulaire qui a été soumis.

![](https://sellsy-a9cc78fb6d3a.intercom-attachments-7.com/i/o/446446297/4ea86a58f0cf9440def65075/dSHyS_mqPFPdb7BDbGRY0jPYqNbkby_41_ZbuqfI-VPEeX-UohnLOVTCxUsXLcgs51OHwyNK7s9Eq3SAN3B9kqPL85D7hJo9YCHKBL4H4NA8f4DGtMHLM5Lov6QGd149KbHVDqum?expires=1788635700&signature=4f1bf7b66afdb889cd6439d66a265b0ca33fdae0e1e43c65eeac76fc6bd17132&req=cCQhEs14n4hYFb4f3HP0gJSMsGq4XH7%2FTZsPGhYxYlNgK6vOYxyQG1G47oWk%0A%2BBfvIuyBlYZvZ44GSA%3D%3D%0A)

Vous pouvez également choisir si l'événement peut se cumuler ou non, dans le cas où l'événement est cumulable alors le score sera ajouté autant de fois que l'événement se produira.

___________________________________________________________

### **Tracking et widget Sellsy**

Lorsque vous mettez en place un Widget Sellsy (un formulaire de contact par exemple) sur les pages de votre site web, dès lors qu’un de vos visiteurs soumet le formulaire, le tracking est automatiquement mis en place pour cette personne. Ainsi, le widget va récupérer l’ensemble des données de navigation pour les enregistrer et récupérer le parcours de votre visiteur.

![](https://sellsy-a9cc78fb6d3a.intercom-attachments-7.com/i/o/446446302/c4608f5181154c67ed2c997b/SjlF9yvBHay07-XkfAeMl9XiPfb0M0NrNNbcjX727GBpYX5xT5FChZrSPcdIA5iyREp7dRH9zi8K_g_iw-5NK_5wCT_Zaes-sQDFR-9twCmynlZ0TCJn9lpyQVyeST_yF8ocefg_?expires=1788635700&signature=6957bf77626890346846e7f96d78dc163a68ed8b56458b044e60bc23eea651ba&req=cCQhEs14noFdFb4f3HP0gJyK66WlfWye5KXkkuzYC2JKJKZc2QfAp97CtwgS%0ArqZj7YnoG7wQdpEM5g%3D%3D%0A)

___________________________________________________________

### **Trouver l’information de scoring pour mon prospect **

Une fois que vous avez configuré votre modèle de scoring, vous pouvez aller vérifier les informations de scoring sur les différentes entités de prospections.

Vous trouverez l’information Score sur les éléments suivants :

- Listing des opportunités
- Vue pipeline des opportunités
- Listing des prospect / client
- Fiche prospect / client

![](https://sellsy-a9cc78fb6d3a.intercom-attachments-7.com/i/o/446446317/7dfb0b85f06a737e40a6c11d/mv1_zdlQh4HpvqQI7sa0LL0pPH1W8jajkvHyLdUD3ek3YFJXpDeLeONAshMB1b0nxAX4CjVt39BopJygwLwC2cgHqx1z0JaINLXVMQGSNVV_w3BpmGWkyCVSpdf_VOcTj0luAA3x?expires=1788635700&signature=53f7d6afd7cad4ebdf9d9aed8a7b0a95c8a90482f71e40a8bbf2cde2bd91a62f&req=cCQhEs14noBYFb4f3HP0gLieYMUlyW0pITwkM4lugYS8l4ZBORwG5ReWekw5%0AV%2FiPiJsj5MC%2BNNDmAw%3D%3D%0A)

Si la colonne score n’est pas affichée sur vos listes, cliquez sur la roue crantée à droite de votre écran puis sur “*Gestion des colonnes*”. Cochez “*Score*” puis validez. 

___________________________________________________________

### **Filtrer ses données par score**

Sur les différents éléments (prospects, opportunités, clients) vous avez en effet la possibilité de filtrer vos données par score. Indiquez un score, puis choisissez une règle (inférieur, supérieur, égal, dans l’intervalle, etc…).

![](https://sellsy-a9cc78fb6d3a.intercom-attachments-7.com/i/o/446446329/babb701a741308fda9d44706/DlnE7cjXINwTFg852AUbxQ3zF3CbUa-ea9Am02a_yESJIVj0OeI4vWiWZag1O3bKEmsUOurneA7KohTtk3PCFLySAluAE6bLJOYgVeksK5L2wmKnqu1Uo04iuDyIQiPLVWYhiaWi?expires=1788635700&signature=83a2c2d4a8e2f7928df223753383a0efe16e8c41b7519f7a2a35ae431fd43b5b&req=cCQhEs14noNWFb4f3HP0gG5jpa7zywV8Us%2Fp56gW2%2ByZFYheRd%2B12ByYZMf7%0A9fDe4YEYu6RQPGSNHQ%3D%3D%0A)

Mis a jour le : 13/03/2026
