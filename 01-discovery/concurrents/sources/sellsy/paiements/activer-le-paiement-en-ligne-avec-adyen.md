---
source: https://help.sellsy.com/fr/articles/5876306-activer-le-paiement-en-ligne-avec-adyen
categorie: Paiements
titre: Activer le paiement en ligne avec Adyen
date_recuperation: 2026-09-05
---

# Activer le paiement en ligne avec Adyen

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2200502969/83e068026202a5a03ed926121d9f/FAQ-Bannie-CC-80reAcademy-2%2B-282-29.png?expires=1788635700&signature=a40e4daf6b43e398ab7e7a8fab3cd281411ec07ac835e665096252ec8a2310e2&req=diInFsx%2Bn4hZUPMW1HO4zZWALf7n%2FpQXPARaLO6WGae08%2BPyBOzZuFXD2H5v%0AM%2F3%2FgpJ6Y%2BLj%2FeV9On0%3D%0A)

___________________________________________________________

### Avant de commencer

Pour connecter Adyen, vous devez :

- disposer d’un **compte Adyen actif**
- avoir un accès **administrateur** dans Sellsy
​

___________________________________________________________

### Étape 1 : Activer Adyen dans Sellsy

1. Ouvrez "**[Menu" > "Réglages" > Paiements en ligne](https://www.sellsy.com/settings/quickpay)"**

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2169553739/f2dac43d3805ca157418300d4ba0/Screenshot%2B2026-03-16%2Bat%2B14_35_02.png?expires=1788635700&signature=9fe3817d974252574bc2c24801976a48b68e7b18ea070ea28ddb4673194d970e&req=diEhH8x7noZcUPMW1HO4zQxtv%2Bzc%2FEx0qPQrRJHxKYlmdIfRdmLX07b0MV5l%0AhTKAJrojfIzo7BFFmzU%3D%0A)

2. Cliquez sur le bouton ***"Connecter"* dans l'encadré Adyen**

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2169556451/a0a7a014aefda667743c0dd52a31/image.png?expires=1788635700&signature=ea5b91a3e17c7913d863764034f790d249a15e28eecbf5cb176a899c05566a1e&req=diEhH8x7m4VaWPMW1HO4ze8XbrQeyupF0TV8NQ%2FuiIVRuk9UUKvG0fEW0cWL%0ALeE18%2FPdFfl748wkE5E%3D%0A)

3. Cliquez ensuite sur *"**Connecter mon compte Adyen**"* 

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2169558864/a2ab8985ee46c8fefef8a39e70f8/image.png?expires=1788635700&signature=555af67cb8d571bb2eedb7cccc331a146a23e476658baf8b2c474cbd9900c002&req=diEhH8x7lYlZXfMW1HO4zVzMtFUsVAnps2p4i2wGm88Nl1YNkALH2cWWVL4H%0AJKV%2Fn2OlKZJCfjv3RME%3D%0A)

___________________________________________________________

### Étape 2 : Configuration d'Adyen

Renseignez les informations demandées pour finaliser l'intégration d'Adyen et Sellsy.

![](https://downloads.intercomcdn.com/i/o/900252835/74f922953f149c9d7d396ca0/2.png?expires=1788635700&signature=7dcece8ad6fb809f1cce097130230448cc78cb2c6eff4ff0f5a356916d58a52e&req=fSAnFMx8lYJaFb4f3HP0gGpcPUIhJCCDIs6tFvwWCojHGe4%2B5R8jJHSCOrvH%0Ar%2FlUW0dw%2Fj0KDXGGdg%3D%3D%0A)

**Trouver la Clé API ***

Rendez-vous sur Adyen dans le menu "*Developers" > "API credentials" *ou créez en une nouvelle si besoin : 

1. Cliquez sur *“Create new credential”* et conservez le type par défaut *“Web service user”.* Ajoutez une description si souhaité puis cliquez sur *“Create credential”.*

![](https://downloads.intercomcdn.com/i/o/900258764/e7c23afcc7d99d5a6b10a0c4/3.png?expires=1788635700&signature=73db17da1b033cfe41d2fe28f9acdf04a8775a639b2c1499e86da6946d223f8f&req=fSAnFMx2modbFb4f3HP0gFCK%2BFNa8DXCan0%2BiMdEQk3GRP4YgxmplhJmUvcw%0AE7ClHsvmnCl%2FnsrXUQ%3D%3D%0A)

2. Descendez dans *"Server settings"* puis cliquez sur *“Generate API key” e*t copiez la clé.

3. N’oubliez pas de cliquer sur *“Save Changes”.*

![](https://downloads.intercomcdn.com/i/o/900260851/98cd2c94fdd580c52341af16/4.png?expires=1788635700&signature=f65c784077b918eb9ef8d996f7027f7dae3f724f2269896c11da5725b4006f21&req=fSAnFM9%2BlYReFb4f3HP0gMz5IlS5ocN6P01MbdvQE59OJSsKUE50T6eudkro%0AINYGqqKhwzE9wLnwsg%3D%3D%0A)

**Trouver la Clé HMAC ***

Rendez-vous sur Adyen dans le menu "*Developers" > "Webhooks"* ou créez en un nouveau si besoin :

1. Cliquez sur le bouton “*+ Webhook”* puis sur *“Add”* de *"Standard notification".* 

![](https://downloads.intercomcdn.com/i/o/900263691/a50c5ac3ba87e03378c2250b/5.png?expires=1788635700&signature=0ef56a5d2829e7f5b697e96961eba4af57b02199ed7c9149252305c418636b51&req=fSAnFM99m4heFb4f3HP0gHfh2xM3swRjhnX3Qwt3O2CgDI4HpKIMN%2FW9J2OU%0AcQCubS3wo7DJ6TneNw%3D%3D%0A)

2. Positionnez le bouton on/off (en haut à droite) sur *“Enabled”.* 

3. Cliquez sur le bouton *"modifier"* de *"Server configuration"* et renseignez les champs demandés : 

- URL : webhook.sellsy.com/adyen_pay_by_link
- Method (JSON) et SSL Version (TLSv1.2) puis cliquez sur “Apply”.

4. Vous pouvez inclure/exclure des comptes marchands via le bouton *"modifier"* de *"Merchant accounts"* si besoin. Par défaut, Adyen prend tous les comptes marchands présents sur le compte.

5. Si nécessaire, dans *"Security"*, ajoutez identifiant / password du serveur via le bouton *"modifier"* de *"Basic authentication".* 

6. Cliquez sur le bouton* "modifier"* de *"HMAC Key"* puis sur le bouton *“Generate”* et copiez la clé. **Attention à bien la conserver car le cas échéant, il faudra la générer de nouveau. **Cliquez sur *“Apply”.*

7. Ajoutez une description si souhaité puis cliquez sur *“Save changes”.*

![](https://downloads.intercomcdn.com/i/o/900287507/0bef64ed2249afd33d34d43a/6.png?expires=1788635700&signature=c15c06253942fb3f05f920d3065276db7ebae5ba9ab7e67a6bc3a975bcdb8ee6&req=fSAnFMF5mIFYFb4f3HP0gKepUjSZZL467LAxrXbq%2BotTsti9JdcDiuQFQ%2Flo%0AsJSB%2FfllXm2lF%2BVzTg%3D%3D%0A)

> **Bon à savoir :** Pour vérifier que votre paramétrage est correct, cliquez sur *“Test configuration”* en bas de votre page.

Sélecteur environnement *

Vous devez choisir entre *"Production"* (sélectionné par défaut) et *"Test"*. Cela correspond aux deux environnements live et test proposés par Adyen (visible dans la popup de connexion de leur interface). 

![](https://downloads.intercomcdn.com/i/o/900314371/9dc138f0086a14668df0bf09/7.png?expires=1788635700&signature=e9876cc49d072f940dfb300a1d9139bd1aa9dd3f6a31b7a769a892445d78a46c&req=fSAnFch6noZeFb4f3HP0gC0GjEOzEBjcmMm4TiHfp9ebOSBYoBfqtbFONXlL%0A6xfMXWPODQj5fhCsaw%3D%3D%0A)

Préfixe URL API *

Ce champ n’apparaît que si le sélecteur d’environnement est positionné sur *“Production”*. Il faut également le récupérer depuis l’interface Adyen, dans "*Developers" > "API URLs"*.

Il correspond au préfixe que l’on peut retrouver à la place des rectangles rouges sur l’écran ci-dessous. 

![](https://downloads.intercomcdn.com/i/o/900316489/73cbe1a71a92a8910884d843/8.png?expires=1788635700&signature=0cbb935a1232f65d46c70d54df4ee3500e851a66dac3b5f0c0c9c90d87226cb6&req=fSAnFch4mYlWFb4f3HP0gLqAvabzKB8btXkK9brimSBO6u%2BJGDAQ4cw%2BjG8d%0AchOvEqCm0fsDVl6kCg%3D%3D%0A)

Identifiant du compte marchand * 

Il contient l’identifiant du compte marchand Adyen que l’on veut associer aux liens de paiement générés. Il est visible dans "*Settings" > "Merchant account"*. 

![](https://downloads.intercomcdn.com/i/o/900318072/292bbe721618d29636e103a1/9.png?expires=1788635700&signature=1af1c62a3f0d913f25e64f6e413e2c18586bd2c033c43b3e126f300af1c83f20&req=fSAnFch2nYZdFb4f3HP0gJhxO6SNPAvV8EWen5DgffLn1aEl6UZFf5%2BQdqmk%0A1Bby1yaggg1K4S6jpA%3D%3D%0A)

Identifiant du thème

C’est un champ non obligatoire qui permet d’utiliser le thème de son choix préalablement créé dans Adyen. Sinon, c’est le thème par défaut du compte qui est utilisé. 

Pour le récupérer, rendez-vous dans "*Pay by Link" > "Themes"* puis cliquez sur le bouton à 3 points du thème voulu et faites *"Copy theme ID".*

![](https://downloads.intercomcdn.com/i/o/900319630/5cc6b80627503d3b10392831/10.png?expires=1788635700&signature=1d6699325bb6a5b8d3859640f2a1cf12b16548c77434b2eeecd12f70406bc801&req=fSAnFch3m4JfFb4f3HP0gBCd2u1NLExvwdRQc119qm4MzK4RZQNXFXoLESdi%0AeezkbMlebKvu6yCtLA%3D%3D%0A)

Pour créer un nouveau thème : 

1. Cliquez sur *“Create a new theme”,* puis choisissez un nom de thème et un display name (qui sera le nom affiché au client). 

2. Choisissez un logo, une image de fond et une couleur de fond (qui remplacera l’image si elle ne peut être chargée). 

3. Définissez-le ensuite comme thème par défaut, puis cliquez sur *"Create".* 

Moyen de paiement associé à Adyen *

**À ne pas confondre avec les moyens de paiements choisis dans Adyen**, ce sera ici le moyen de paiement que l’on voudra associer côté Sellsy à un paiement généré depuis un lien de paiement Adyen (peu importe le moyen de paiement qui aura été utilisé via Adyen). 

Les moyens de paiement disponibles ici seront ceux que l’on peut trouver dans "*Menu" > "Réglages" > "Catalogue" > "Tarifs et taxes"*, et celui sélectionné par défaut sera le premier de cette même page.

Enregistrer

Une fois que l’on a renseigné ces champs et cliqué sur *“Enregistrer”,* un appel vers Adyen (méthode [POST /paymentLinks](https://docs.adyen.com/api-explorer/Checkout/69/post/paymentLinks)) sera automatiquement généré pour créer un lien de paiement de test qui expirera aussitôt. Cela permet de vérifier si l’ensemble des champs renseignés (excepté la HMAC que l’on ne peut vérifier) sont corrects. Un message de notification confirmera alors l’enregistrement des paramètres. 

![](https://downloads.intercomcdn.com/i/o/900334705/2ad76164cac1211961922250/11.png?expires=1788635700&signature=c1488400b41cefbab90134be5a8b8fbdfc3c1b1e2e22487372b7307ba0aca061&req=fSAnFcp6moFaFb4f3HP0gOSnFVUqnTHeEZ0TqAccuFPzN3jonkVPEkj%2B7QO7%0AV%2BKP0Mh64YLPu2IClg%3D%3D%0A)

Si l’enregistrement n’a pas fonctionné, dû au fait qu’au moins un des paramètres était incorrect ou que le serveur Adyen était indisponible, cela sera indiqué via des messages d’erreur dans le module. 

![](https://downloads.intercomcdn.com/i/o/900335935/58fee0fcdab31d11e6eec49f/12.png?expires=1788635700&signature=eea51bf07fdf0e9b3c93187b7be16c639ccad507b1a08175d0c6eeff6bc66556&req=fSAnFcp7lIJaFb4f3HP0gNMDuHIGAF46DURknxq18Y5f8OV8iY7wkcBKiJX6%0AN5UigrZtYtTa9n64Mw%3D%3D%0A)

Il est également obligatoire, dès que l’on est en mode Production, de configurer ses termes et conditions depuis l’interface Adyen, sur la page "*Pay by Link" > "Settings"*. 

![](https://downloads.intercomcdn.com/i/o/900337817/6da9c929e7dd196c91a30bae/13.png?expires=1788635700&signature=cb0680e05e51dcc62080d9e0334952e4ec5a9aa450d49a417d65abff98b0f4a4&req=fSAnFcp5lYBYFb4f3HP0gDr6l140TJORLKHH4n1XEXKVDu9TFCXTV%2F%2F9OlLY%0Ax9RSBGEbAVfc6Q0BUw%3D%3D%0A)

D’autres paramétrages sont possibles depuis Adyen directement, notamment si l’on veut par exemple limiter le choix des moyens de paiement que l’on veut rendre disponible : "*Settings" > "Payment methods"*. 

___________________________________________________________

### Génération des liens de paiement

Une fois activé et configuré, Adyen Pay by Link est disponible dans les moyens de paiement que l’on peut proposer dans les préférences du document. 

![](https://downloads.intercomcdn.com/i/o/900341164/b1ddaf46a232e9f1247468fc/14.png?expires=1788635700&signature=bfceca5e6c089054ba36892f77019938b106c6cbc35e8235b74ab95ba50693a0&req=fSAnFc1%2FnIdbFb4f3HP0gPdtoUccfariRkoTVckZp6RI7minrL0o%2BOBBsPko%0AdPpMSNU0GNvfDnWJEQ%3D%3D%0A)

Lorsque vous cliquez pour la première fois sur le lien public du document de vente, un lien de paiement sera généré.

La page de paiement, accessible via le bouton *“Payer en ligne”* du lien public, sera disponible jusqu’à 70 jours après le clic sur le lien public et dans la langue de votre navigateur. Si le délai restant avant expiration est inférieur à 24h, un nouveau lien de paiement est généré et associé au document.

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2169576819/ab09b223b0a5bb7823363cbdb13c/Screenshot+2026-03-16+at+19_00_29.png?expires=1788635700&signature=f7e07b36c61a36cfad3a86abe7de94f2785fddbb92e74cba59386e4c79d5a7d3&req=diEhH8x5m4leUPMW1HO4zeOhduubAPXEcX7E0j8%2B5H3lYRA0ioKsit%2B5pJZM%0AGfuz7SYczpJ2x1%2F8B7c%3D%0A)

___________________________________________________________

### Suivi du paiement

Si le paiement a fonctionné, Adyen vous envoie une confirmation. Vous pourrez alors être redirigé vers la page de paiement.

Si le moyen de paiement utilisé n’est pas détecté comme sûr par Adyen, votre paiement sera en attente de confirmation. Vous devrez alors vous rendre sur Adyen pour accepter le paiement, dans la section "*Risk" > "Case management"*.

![](https://downloads.intercomcdn.com/i/o/904451586/384b494f1819c0fe2d370b92/18.png?expires=1788635700&signature=c43b48c06ed34f33a579f1afc8f09a2471db93f3940a49cc79a0a480ddbc01a9&req=fSAjEsx%2FmIlZFb4f3HP0gPiiivZLPzhN1pLysgx%2Bnq0128JeTA9wcW9weBP6%0AgyKmYuxaU0XOQdcMmg%3D%3D%0A)

En cliquant sur l’identifiant visible dans la colonne *"PSP reference",* vous pouvez choisir d’accepter ou refuser le paiement.

![](https://downloads.intercomcdn.com/i/o/904452105/1663497e67a15704629be594/19.png?expires=1788635700&signature=a3f8bfe31bd4069860607d4f2155169ca0f899a42b35374c3d97c2155528d621&req=fSAjEsx8nIFaFb4f3HP0gCl1ZCHHlkA2Sc8%2FDmds944bf0C9pitsEYazVJbX%0ALRVBdsYfYkSK1tgdRw%3D%3D%0A)

Mis a jour le : 25/03/2026
