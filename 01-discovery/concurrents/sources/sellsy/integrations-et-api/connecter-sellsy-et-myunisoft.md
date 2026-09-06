---
source: https://help.sellsy.com/fr/articles/15478608-connecter-sellsy-et-myunisoft
categorie: Intégrations et API
titre: Connecter Sellsy et MyUnisoft
date_recuperation: 2026-09-05
---

# Connecter Sellsy et MyUnisoft

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472331496/ad165f36e05026291418f0566e2b/FAQ-Bannie-CC-80reAcademy-2-2B-282-29.png?expires=1788635700&signature=16f0d2c95077163e9ebfa778ec2c1bb74d22ac480ac5d82ac0297ce77c80d5a2&req=diQgFMp9nIVWX%2FMW1HO4zdIphPxzWbCWZNmL0wxEFcZDpAsBL1Hdz7UMMVBB%0A8svnuLnU3RlV4lrNpH0%3D%0A)

##  

Introduction

Bienvenue dans le [guide d'activation de connexion Sellsy x MyUnisoft](#h_1b81ec1224). Pour rappel, la connexion MyUnisoft est incluse dans votre licence Sellsy Facturation, aucun coût additionnel n'est associé à son usage. Elle permet de :

- Synchroniser automatiquement les avoirs et factures de vente depuis Sellsy vers MyUnisoft
- Synchroniser automatiquement les avoirs et factures d'achat depuis Sellsy vers MyUnisoft
- Transmettre les pièces jointes PDF associées aux factures
- Synchroniser les clients et fournisseurs (tiers)
- Créer automatiquement les comptes de tiers dans MyUnisoft lorsque nécessaire

> **Bon à savoir :** La synchronisation vers MyUnisoft ne concerne que les documents [comptabilisés dans Sellsy](https://help.sellsy.com/fr/articles/5875018-comptabiliser-des-factures-d-achat-et-de-vente). Si un document n'a pas encore été comptabilisé, il ne sera pas transmis à MyUnisoft lors des synchronisations automatiques.

### 
Données synchronisées

| Donnée | Pris en charge |
| --- | --- |
| Écritures de vente | ✅ |
| Pièces jointes de vente | ✅ |
| Écritures d'achat | ✅ |
| Pièces jointes d'achat | ✅ |
| Synchronisation / création des comptes tiers | ✅ |

> **Important :** Cette intégration fonctionne dans un seul sens. Les données sont transmises de Sellsy à MyUnisoft. Les modifications réalisées directement dans MyUnisoft ne sont pas automatiquement répercutées dans Sellsy.

___________________________________________________________

## Guide d'activation de connexion Sellsy x MyUnisoft

### 
⚠️ Avant de commencer

Avant de configurer la connexion entre Sellsy et MyUnisoft, assurez-vous de disposer des accès nécessaires et de remplir les prérequis techniques.

> **Important :** Nous recommandons que l’activation de cette intégration soit réalisée par votre expert-comptable. 
> Les licences des cabinets comptables disposent par défaut d’un accès API, ce qui n'est souvent pas le cas sur les licences d'une entreprise chez un outil comptable tel que MyUnisoft. De plus, les étapes de paramétrage comptable seront mieux maîtrisées si elles sont effectuées par votre cabinet.
> Avant de transmettre cette page à votre expert-comptable, assurez-vous d’avoir réalisé les étapes préalables dans votre compte Sellsy, [décrites ci-dessous](#h_25f8583be6).
> N’effectuez vous-même cette activation que si votre comptabilité est internalisée. Dans ce cas, assurez-vous que votre licence ou votre niveau de plan inclut un accès API.


Côté Sellsy

- Une licence Sellsy Facturation active ;
- Des [factures/avoirs comptabilisés](https://help.sellsy.com/fr/articles/5875018-comptabiliser-des-factures-d-achat-et-de-vente) (si un document n'a pas encore été comptabilisé, il ne sera pas transmis à MyUnisoft lors des synchronisations automatiques) ;
- La [conformité stricte active](https://help.sellsy.com/fr/articles/6100605-activer-le-mode-conforme-pour-les-documents-de-vente) sur le compte Sellsy ;
- Les droits nécessaires pour accéder aux intégrations comptables :
- **Vous êtes client Sellsy, votre comptabilité est internalisée et gérée via MyUnisoft :** Vous devez disposer d'un profil administrateur ou d'un profil ayant accès aux paramètres d'intégration. Si vous ne disposez pas des droits nécessaires, contactez un administrateur de votre compte Sellsy. Pour en savoir plus sur les profils et privilèges Sellsy, consultez [cet article](https://help.sellsy.com/fr/articles/5864112-profils-de-privileges).
- **Vous êtes expert-comptable d'un client Sellsy :** Avant de poursuivre la configuration, assurez-vous que votre client vous a accordé un accès expert-comptable associé à un [profil administrateur](https://help.sellsy.com/fr/articles/5864112-profils-de-privileges). L'accès Expert-Comptable est gratuit et permet d'accéder aux données nécessaires à la synchronisation comptable. Si vous ne disposez pas encore d'un accès expert-comptable, votre client devra suivre la procédure décrite [dans cet article](https://help.sellsy.com/fr/articles/6652377-donner-un-acces-sellsy-a-mon-expert-comptable).


Côté MyUnisoft

Pour débuter l'intégration entre Sellsy et MyUnisoft, vous devez :
​
​**1. Générez un token API pour votre connexion avec MyUnisoft.**

Rendez-vous sur votre compte, paramètres puis Connecteurs.

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472343424/d7c206158087acf419b8a817560c/919ff0c7-25b3-4a5e-b959-9b0d2e84f201-2Fe902616e-0d36-41c4-a980-0d83fc389ac0-Screenshot_2024-03-20_at_14_32_22.png?expires=1788635700&signature=3a54a66f1ca12d711d6cbfc59186998dc848d50dc4a98fb69cf3f8dd5607fa70&req=diQgFMp6noVdXfMW1HO4zehPSM5D5d95eoTPeBTw0txm9ScweVJnHnGULU5%2B%0AE9qrxoGbkIA4tYeO8AA%3D%0A)

Vous trouverez dans la liste des connecteurs, le logiciel que vous souhaitez connecter avec My Unisoft.

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472343430/42bb72b11e90d75a58185d129901/919ff0c7-25b3-4a5e-b959-9b0d2e84f201-2F46a172a1-3115-4cc9-8693-15b6a7ed2d39-Screenshot_2024-03-20_at_14_32_43.png?expires=1788635700&signature=446ebd1ddb98476bd6f8ad0c29437903080c64e4f9a13b5bc68db0cbb00b17ad&req=diQgFMp6noVcWfMW1HO4zdyk%2BumsMXYZ53Zl0MZnxwjn5uA2i38lWivNbNcM%0AjUq1OeivdRueYnLympk%3D%0A)

Sélectionnez Sellsy et générez une clé API à renseigner dans la page de connexion.

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472343425/6356490e1ac6c7fade8d151bf6c7/919ff0c7-25b3-4a5e-b959-9b0d2e84f201-2Fe8b353db-24e4-48f2-8b70-e14059d604ba-Screenshot_2024-03-20_at_14_32_49.png?expires=1788635700&signature=1077b979b1abcf983bdf8ca6200566fae0593d4dae3dc00091040a2c83198f60&req=diQgFMp6noVdXPMW1HO4zV7H4bhersZtpWJWdLZmRNDDOfvUiSml%2FlPXNriL%0AHzNwhwbVarPfW0BaMAU%3D%0A)

**2. Créez la connexion API.**

Choisissez un nom pour votre connexion.

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472343409/5436ef61464e38a02c770e20aaa2/919ff0c7-25b3-4a5e-b959-9b0d2e84f201-2F03215dd2-5bcb-44b4-b264-4c44464f763f-Screenshot_2024-03-18_at_10_47_37.png?expires=1788635700&signature=27ee30f37e6b60fd0679efaa0243faed50dcb80e9922398f198fff4badbf1300&req=diQgFMp6noVfUPMW1HO4zewUV7g0bnuhSplhT1QuziN5Z%2FHQC8Wftw1GZBE%2B%0AAAonp95u84hpYNjyoFU%3D%0A)

Souhaitez-vous récupérer les données analytiques ?

Si oui, alors sélectionnez le champ « **actif** », sinon comptabilité analytique = « **inactif** ».

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472343411/02dac5196dbf7c7abaaf3073719d/919ff0c7-25b3-4a5e-b959-9b0d2e84f201-2Fdd9fa027-adf7-4f3a-9419-6af34054e64f-Screenshot_2024-03-18_at_10_47_43.png?expires=1788635700&signature=ef9706218f32d54f26795d156cdc14a7905adf76a6f6ff4f5f3b4b8a5306b568&req=diQgFMp6noVeWPMW1HO4zWP4fPjzKWSFfR6FyRco%2FZ7dBbu%2Bg9yDFNWJT4nr%0AqFDTALrN7l0klZRhoFU%3D%0A)

Renseignez l'API token que vous avez généré depuis votre compte MyUnisoft.

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472343413/029e044a1f8827c7a42156f6e308/919ff0c7-25b3-4a5e-b959-9b0d2e84f201-2F79f7675f-d364-491c-912e-65c6285fbfea-Screenshot_2024-03-18_at_10_47_47.png?expires=1788635700&signature=ce8d9fa6a9a23a1744b781ca804369ca34f69adca2e90fa0aee98293d6d34968&req=diQgFMp6noVeWvMW1HO4zdDY21WEx4CRVmj2HQnSNcbM0h%2BG68Sv9V0w4McH%0AL725FKULCstJguMPu%2BA%3D%0A)

Cliquez sur « **Connecter** » pour finaliser la connexion.


Si vous rencontrez des soucis lors de ces étapes, nous vous conseillons de vous mettre en relation avec les équipes MyUnisoft ou de [consulter leur base de connaissances](https://support.myunisoft.fr/).


​

### 👉  Étape 1 : Connecter MyUnisoft dans Sellsy

Depuis la [page marketplace Sellsy à propos de l’intégration MyUnisoft](https://go.sellsy.com/applications/myunisoft) cliquez sur : « **Activer l’intégration** ».

Ou bien cliquez directement sur [ce lien](https://marketplaces.chift.app/fr/sellsy/apps/8006). Vous serez redirigé vers l'interface sécurisée Chift.
​

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472355645/e9b1804494a2a3bd17cd639acd59/Capture+d%E2%80%99e%CC%81cran+2026-06-12+a%CC%80+11_06_08.png?expires=1788635700&signature=a7d5f2cd99d33e1c7e07bef81aca9672c798c3c81b752d2802191cf3e5306794&req=diQgFMp7mIdbXPMW1HO4zXMkZqpgM3z90D6KrdGArgjvnIkYTMiXwUaMl%2B1C%0Aqu6vmJN%2F9iUqgvRNXWk%3D%0A)

### 
👉  Étape 2 : Authentifier la connexion

Dans l’interface Chift, cliquez sur « **Activer l’intégration** ». Si c’est votre première connexion pour ce compte, cliquez sur « **En créer une nouvelle** ».

Si une connexion a déjà été créée pour ce compte, sélectionnez simplement le compte correspondant dans le menu déroulant, puis cliquez sur « **Valider** ».

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472333301/18046d102f0bc227409ae8330c74/Capture-2Bd-E2-80-99e-CC-81cran-2B2026-05-29-2Ba-CC-80-2B15_55_08.png?expires=1788635700&signature=3da46a90ab7674f704609b9af2032b7a3761c589a34fb9cfec1b24e75807e23d&req=diQgFMp9noJfWPMW1HO4zQHa3ibFaK0Sq3GhdVUcBwJg1r3Pr0TkTqPswUep%0And3mUDvxNK72xKZJ4QU%3D%0A)

Pour créer une nouvelle connexion, munissez-vous du nom et du numéro SIRET de l’entreprise utilisant Sellsy. Renseignez ces informations, puis cliquez sur « **Enregistrer** ».

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472333303/430671b5bd2b346425d184e8db6d/Capture-2Bd-E2-80-99e-CC-81cran-2B2026-05-29-2Ba-CC-80-2B15_58_07.png?expires=1788635700&signature=584df51d6e52833ff2fe9c2cd06bcd96a0f0752b9db6617cc2d8919f91b2253c&req=diQgFMp9noJfWvMW1HO4zWxiwffkQq%2FZyldILfP99MWMi2i6D4b1gPLe2x%2F3%0ACWxXhAGK3ZSX5eDRXtI%3D%0A)

Une fois ces étapes complétées, vous allez vous retrouver sur un écran comme celui-ci :

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472358698/c1df93a3494904cd5a91ed017584/Capture+d%E2%80%99e%CC%81cran+2026-06-12+a%CC%80+11_07_44.png?expires=1788635700&signature=9f51574e20eaa55110b0007937cb8ea51dd21c63ee13a3984cdba67fbdbd1fe4&req=diQgFMp7lYdWUfMW1HO4zeMMp0FPfzbuZl6D89dgxjAlruKXDJ%2B7QbCWCX%2Bu%0AX1f%2BMOwKmWGgMbQJSos%3D%0A)

En cliquant sur « **Connecter** », vous serez redirigé vers l’écran de connexion Sellsy.

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472333313/dd5feea39413420a9975daac09b7/Capture-2Bd-E2-80-99e-CC-81cran-2B2026-05-29-2Ba-CC-80-2B16_00_46.png?expires=1788635700&signature=df36f9cf033ec25723e3c63042eb56702f7371fd634cc10bc2b9e374f7cfe9cc&req=diQgFMp9noJeWvMW1HO4zSgPSBZ3OXdjBEE7SjOyQHl%2F1aampwFBXw6eEntR%0AVmK5A3%2B2r%2Frp8Q2USwQ%3D%0A)

Il vous suffit de renseigner vos identifiants Sellsy. Si plusieurs comptes sont associés à ces identifiants, sélectionnez le compte concerné dans le menu déroulant.

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472333311/1db391ef60aa3d080f4dc37b0a46/Capture-2Bd-E2-80-99e-CC-81cran-2B2026-05-29-2Ba-CC-80-2B16_01_26-2B-1-.png?expires=1788635700&signature=a204f50b36d2515584533bcd7117d1de88c3d52f6e0db55e78be6731c140661e&req=diQgFMp9noJeWPMW1HO4zTqYVJfks4smliRp%2F41e7E6Q7rcVVl4qMFqltAYl%0A3LDy7gsznP6IuAEwv%2Bs%3D%0A)

Puis, autoriser la connexion via Chift en cliquant sur « **Autoriser** ».

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472333312/6ff21a4147832b8b9d8c27e960dd/Capture-2Bd-E2-80-99e-CC-81cran-2B2026-05-29-2Ba-CC-80-2B16_01_36.png?expires=1788635700&signature=23fcd9919619a4b52b70442b1e53ef046efecf73a8791f275eacaed5e7d2f679&req=diQgFMp9noJeW%2FMW1HO4zcj21Cfb0yzf%2FsRyvD4LgSALdtCiBfLVM4r4CLuJ%0AlV1kHjgJ7Bu%2Fltq1wFQ%3D%0A)

Vous serez ensuite redirigé vers la seconde étape d’authentification, qui vous permettra de vous connecter à votre environnement MyUnisoft.

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472360795/223b922d0c4ef1af20d7e36185be/Capture+d%E2%80%99e%CC%81cran+2026-06-12+a%CC%80+11_09_13.png?expires=1788635700&signature=a838c91c354b4605cf9fe49af7511845ccb24843638f35a6f8bfbee65e734387&req=diQgFMp4nYZWXPMW1HO4zVCfBxH9WZE1SM4iAqjOFlmYx8jdPR6x6mI7PYRv%0ArJ3bAm10z30ZqGtkcco%3D%0A)

Ici, [les premières étapes de préparation](#h_b43cbcb321) deviennent essentielles. Vous devez réenseigner la clé API MyUnisoft.
​

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472379355/4a66490f43cbe6093a786dfede98/Capture+d%E2%80%99e%CC%81cran+2026-06-12+a%CC%80+11_20_54.png?expires=1788635700&signature=fb1a199fc1faf7bd37e3a5c1e8eda284f361d33280b2fe6c13e69bef3c43ad74&req=diQgFMp5lIJaXPMW1HO4zXIkc7B%2FkuYiVXQdDpDWDO01YW2LyWF4W8KG%2F3f3%0A2oF3VV86p0sWKt8jj1w%3D%0A)


Cliquez sur « **Connecter** » pour finaliser la connexion.

Une fois l'authentification validée, la connexion entre Sellsy et MyUnisoft est établie.
​

### 
👉  Étape 3 : Déterminer les paramètres de connexion

Une fois l'authentification terminée, vous devez configurer les correspondances comptables entre Sellsy et MyUnisoft.

Cette étape permet au connecteur de savoir comment traduire les données présentes dans Sellsy vers les bons éléments comptables dans MyUnisoft.

Pour rappel, l'intégration permet de récupérer les documents de vente et/ou d'achat présents dans Sellsy et de les transmettre automatiquement à MyUnisoft, accompagnés de leurs pièces jointes.

Vous devrez compléter les correspondances pour les éléments suivants :

- Taux / codes de TVA de vente
- Taux / codes de TVA d'achat
- Codes de TVA utilisés pour les arrondis
- Journaux comptables
- Comptes comptables
- Comptes de rabais, remises et ristournes

1. Taux / Codes de TVA de vente

Associez chaque taux ou code de TVA utilisé dans Sellsy au code de TVA correspondant dans MyUnisoft.

Cette correspondance permet au connecteur d'affecter correctement les montants de TVA sur les écritures de vente exportées. Exemple :

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472333317/047a7d4d4f2f51cd7ddcfdfb66be/Capture-2Bd-E2-80-99e-CC-81cran-2B2026-05-29-2Ba-CC-80-2B16_43_36.png?expires=1788635700&signature=f089cad4fe0e47a0b3c9f36de7571ab6fd85e2b1a7202db4432196300cb3cdf2&req=diQgFMp9noJeXvMW1HO4zXVJx%2F5%2BBIqQ6J5vVGS3ta6F%2BDAOrUFLB%2BxGqPsn%0AnrRR4S6bhEyK6NxJfXM%3D%0A)

2. Taux / Codes de TVA d'achat

Associez chaque taux ou code de TVA utilisé sur vos factures fournisseurs Sellsy au code correspondant dans MyUnisoft.

Cette étape garantit une comptabilisation correcte de la TVA déductible lors de l'export des achats. Exemple :

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472333318/6c12272f4f036484867bc40af9c6/Capture-2Bd-E2-80-99e-CC-81cran-2B2026-05-29-2Ba-CC-80-2B16_43_36.png?expires=1788635700&signature=1e0d6337d54ec3366ea58c260fdbe7586d989c927be2a3181cec5cc1e2e77813&req=diQgFMp9noJeUfMW1HO4zTnIPiEFX3RpKjRx5uCjiUYu5%2FOSwBcsFEqbO479%0A2GuU6mDN3mcJsH8YHO4%3D%0A)

3. Codes TVA pour les arrondis

Certaines écritures peuvent engendrer des écarts d'arrondi de quelques centimes.

Vous devez indiquer le code de TVA à utiliser pour ces ajustements afin de garantir l'équilibre des écritures transmises dans MyUnisoft. Exemple :

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472333319/e8c2fb59723d024bcaddcc8592d3/Capture-2Bd-E2-80-99e-CC-81cran-2B2026-05-29-2Ba-CC-80-2B16_46_37.png?expires=1788635700&signature=b3d50fe9791e28400ec9052631a06d7c9f893a401bd17bf23f702f4ace46b388&req=diQgFMp9noJeUPMW1HO4zTfyuRbo36mcLyfrD7pGC5ISdq4bVmMCDOi82ZBF%0AgBSofvIWdpl%2B4D0NxAI%3D%0A)

4. Journaux comptables

Associez les journaux Sellsy aux journaux comptables existants dans MyUnisoft. Par exemple :

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472333322/426cba55ce3e3fe9164ca7258f7b/Capture-2Bd-E2-80-99e-CC-81cran-2B2026-05-29-2Ba-CC-80-2B16_47_07.png?expires=1788635700&signature=39431e21d1f20e969f78879aab387e2436969c6c698df1647358dee24ce0ab73&req=diQgFMp9noJdW%2FMW1HO4zUH5%2Fl9FSK0IQ5U3I1iZhHQhmRY8T3KLXX%2BBz3Db%0AUW2xawn%2B15RVQUwP5Qo%3D%0A)

Les journaux sélectionnés doivent avoir été préalablement autorisés lors du partage du dossier dans MyUnisoft.

5. Comptes comptables

Associez les comptes comptables utilisés dans Sellsy aux comptes correspondants dans MyUnisoft.

Ces correspondances permettent d'affecter correctement les écritures comptables lors de leur création.

Nous vous recommandons de vérifier la cohérence entre votre plan comptable Sellsy et votre plan comptable MyUnisoft avant de valider le paramétrage.

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472333320/bf3326708a28c6cd7c19324791c6/Capture-2Bd-E2-80-99e-CC-81cran-2B2026-05-29-2Ba-CC-80-2B16_50_04.png?expires=1788635700&signature=d2282361d1f58a41d31ade3706f29cae3d5e365c06ba1b0a4dc929a04b6ef9f6&req=diQgFMp9noJdWfMW1HO4zV6S8BWtAmrKwk6VYqlTslPZPTPiOJ1AyPK2br41%0At43SRuy5qbXNNghsYi8%3D%0A)

6. Rabais, remises et ristournes

Si vous utilisez des rabais, remises ou ristournes dans Sellsy, vous devez également définir les comptes comptables qui recevront ces montants dans MyUnisoft en cliquant sur « **Oui** », puis sur « **Enregistrer** ».

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472333321/73b01383522b41c27109f4b33e58/Capture-2Bd-E2-80-99e-CC-81cran-2B2026-05-29-2Ba-CC-80-2B16_51_33.png?expires=1788635700&signature=e480712eec4cf8ffb45d44b99e39dd40543f7b4103cf817936b7e9cff4dd1438&req=diQgFMp9noJdWPMW1HO4zZ9qvKF3Injgaarmkzfxnoz5ab63f2%2Bbe5RXDrjW%0AjeSfx6klhwK5cHf6IJ4%3D%0A)

Autrement, cliquez sur « **Non** », puis sur « **Passer** ».

En cas de doute, rapprochez-vous de votre cabinet comptable ou de votre administrateur MyUnisoft.
​

### 
👉  Étape 4 : Derniers ajustements techniques

Votre connexion est maintenant configurée.

Avant d'activer l'intégration, quelques paramètres complémentaires vous permettent d'adapter le fonctionnement de la synchronisation à votre organisation comptable.

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472333326/75908b9956fc804acb23fc4fd24c/Capture-2Bd-E2-80-99e-CC-81cran-2B2026-05-29-2Ba-CC-80-2B16_54_13.png?expires=1788635700&signature=ba1b9010fc7b515550a503d8cef1773ad4f6363de7691011ed24e6878f7a044b&req=diQgFMp9noJdX%2FMW1HO4zeJFniubfb%2F%2BmdcCgBYansPUMPQr%2BVAL7uKo0FWP%0AGphyHs%2FY1x%2FZPj8kT7Y%3D%0A)

1. Date de début de synchronisation

Sélectionnez la date à partir de laquelle les factures/avoirs Sellsy devront être transmis à MyUnisoft.

Chaque nuit, le connecteur synchronisera automatiquement les factures et avoirs :

- ayant une date égale ou postérieure à la date sélectionnée ;
- marqués comme devant être envoyées en comptabilité.

> **Bon à savoir :**  Si vous mettez en place l'intégration pour la première fois, choisissez une date cohérente avec votre période comptable afin d'éviter l'export de documents déjà traités dans MyUnisoft.

2. Création des écritures en brouillon / attente

La création des écritures en brouillon via API est prise en charge par MyUnisoft : vous devez faire un choix concernant la synchronisation des écritures selon vos habitudes ou celles de votre expert-comptable.

> **Bon à savoir :** L'absence de création d'écritures en brouillon/attente ne signifie pas qu'une écriture ne peut pas être modifiée post-import. Elle peut être modifiée à tout moment en comptabilité. L'écriture arrivera, par défaut, en « **traitée **», mais le statut peut être modifié en « **à traiter** » post-import automatique.

3. Synchroniser les documents sans justificatif

Choisissez si les factures ou avoirs ne disposant pas de pièce jointe doivent être transmis à MyUnisoft.

- Oui : Les documents seront synchronisés même si aucun justificatif n'est associé.
- Non : Seuls les documents accompagnés d'un justificatif seront transmis.

> **Important :** Nous recommandons de désactiver cette option si votre cabinet comptable exige systématiquement la présence d'un justificatif pour chaque écriture.

4. Libellé des écritures

Définissez la manière dont les libellés des écritures comptables seront générés dans MyUnisoft.

Ce paramètre détermine les informations qui apparaîtront dans les écritures créées par l'intégration et facilitera leur lecture par votre cabinet comptable.

Les options disponibles sont les suivantes :

- Ligne client/fournisseur avec le nom du client/fournisseur et description Sellsy sur les autres lignes
- La ligne de tiers (client ou fournisseur) affiche uniquement le nom du tiers.
- Les autres lignes comptables reprennent la description renseignée dans Sellsy.
Cette option permet de conserver le maximum de détails issus du document d'origine.
- Nom du client/fournisseur dans toutes les lignes
- Toutes les lignes comptables contiendront uniquement le nom du client ou du fournisseur.
Cette option offre une lecture homogène des écritures dans l'outil comptable.
- Nom du client/fournisseur et description Sellsy dans toutes les lignes
- Chaque ligne comptable affichera à la fois le nom du tiers et la description issue de Sellsy.
Cette option est généralement la plus détaillée et facilite l'identification du contenu de chaque ligne d'écriture.
- Numéro de facture et nom du client/fournisseur
- Les écritures sont libellées à partir du numéro de facture ainsi que du nom du client ou du fournisseur.
Exemple :
```
FAC-2025-00123 - Société Dupont
```
Cette option facilite les recherches à partir d'un numéro de facture dans le logiciel comptable.

En cas de doute, rapprochez-vous de votre cabinet comptable afin de choisir le format de libellé le plus adapté à ses habitudes de traitement et de contrôle.

5. Activer l'intégration

Une fois ces paramètres renseignés, cliquez sur **Activer l'intégration**.

La synchronisation automatique sera alors activée.

Par défaut, l'intégration s'exécute automatiquement chaque jour à **05h00**.

Les nouvelles factures et avoirs répondant aux critères définis seront transmis à MyUnisoft avec leurs écritures comptables, leurs tiers et leurs pièces jointes associées.

> **Important : **Nous recommandons de vérifier attentivement les premiers documents transmis dans MyUnisoft. Plus une anomalie est détectée tôt, plus elle est simple à corriger. Une fois les premiers contrôles validés et les éventuels ajustements effectués, l’intégration fonctionnera de manière autonome.

___________________________________________________________

## **Questions fréquentes**

L'intégration fonctionne uniquement de Sellsy vers MyUnisoft.
Les factures et avoirs créés **[et comptabilisés](https://help.sellsy.com/fr/articles/5875018-comptabiliser-des-factures-d-achat-et-de-vente)** dans Sellsy, ainsi que les écritures comptables, les tiers et les pièces jointes associées, sont automatiquement transmis vers MyUnisoft.
Les modifications réalisées directement dans MyUnisoft ne sont pas automatiquement répercutées dans Sellsy.
Une fois activée, la synchronisation s'exécute automatiquement chaque nuit.
​

Les paramètres de l'intégration peuvent être modifiés à tout moment après sa mise en service.
Vous pouvez notamment mettre à jour :
- Les taux TVA
- Les journaux comptables
- Les comptes comptables
- Les comptes de rabais, remises et ristournes
Les modifications seront prises en compte pour les futures synchronisations.
[Si de nouveaux taux de TVA sont créés dans Sellsy,](https://help.sellsy.com/fr/articles/5871870-ajouter-un-taux-de-tva) pensez à compléter leur correspondance dans le connecteur avant leur première utilisation.
​

Lorsqu'une écriture a déjà été créée dans MyUnisoft, la correction doit généralement être réalisée directement dans MyUnisoft.
Si l'erreur est liée au paramétrage du connecteur (code TVA, compte comptable, journal, etc.), nous recommandons également de corriger la configuration de l'intégration afin d'éviter que l'erreur ne se reproduise lors des synchronisations suivantes.
Dans la majorité des cas, les corrections d'écritures déjà intégrées sont réalisées dans MyUnisoft.
​

Nous recommandons de vérifier attentivement les premières factures et avoirs transmis dans MyUnisoft afin de confirmer que :
- Les comptes comptables sont corrects
- Les codes TVA sont correctement affectés
- Les journaux utilisés sont les bons
- Les tiers sont correctement créés ou rapprochés
- Les pièces jointes sont bien présentes
Plus une anomalie est détectée tôt, plus elle est simple à corriger.
Une fois les premiers contrôles validés et les éventuels ajustements effectués, l'intégration fonctionnera de manière autonome et vous n'aurez généralement plus à intervenir sur son paramétrage.
​

Lors de la synchronisation, le connecteur recherche automatiquement une correspondance existante dans MyUnisoft à partir de plusieurs critères :
- Compte auxiliaire
- Numéro de TVA
- SIRET ou numéro d'entreprise
- Nom du tiers
Si aucune correspondance n'est trouvée, un nouveau client ou fournisseur est créé automatiquement dans MyUnisoft.
​

Pour faciliter le suivi des écritures importées depuis Sellsy, nous recommandons de définir avec votre cabinet comptable :
- Des journaux dédiés aux flux Sellsy
- Une convention de libellés spécifique
- Une procédure de contrôle des imports
Cette organisation permet généralement d'identifier facilement les écritures provenant de l'intégration.

Les pièces jointes associées aux documents de vente et d'achat peuvent être transmises vers MyUnisoft avec les écritures comptables.
​[Lors du paramétrage de l'intégration](#h_831b429eed), vous pouvez choisir de synchroniser tous les documents ou uniquement ceux disposant d'un justificatif.
​

Nous préconisons de faire intervenir votre expert-comptable pour la configuration de l'intégration. Assurez-vous qu'il dispose d'un [accès gratuit expert-comptable](https://help.sellsy.com/fr/articles/6652377-donner-un-acces-sellsy-a-mon-expert-comptable) avec un [profil d'administrateur](https://help.sellsy.com/fr/articles/5864112-profils-de-privileges).
​

La comptabilité analytique n'est pas prise en charge par cette intégration.


En cas d'erreur lors de la connexion, vérifiez :
- La clé API
- Le code secret API
Si le problème persiste, rapprochez-vous de votre administrateur afin de vérifier la configuration de l'environnement MyUnisoft.
​

Assurez-vous d'avoir bien respecté [ces étapes.](#h_b0d180ae09) Si le problème persiste, rapprochez-vous de votre administrateur afin de vérifier la configuration de l'environnement MyUnisoft.
​

Assurez-vous de bien avoir respecté [ces étapes](#h_b0d180ae09). Si le problème persiste, rapprochez-vous de votre administrateur afin de vérifier la configuration de l'environnement MyUnisoft.
​

 Veuillez vérifier que :
- La facture a bien été comptabilisée dans Sellsy. Les documents de vente et d'achat non comptabilisés ne sont pas synchronisés vers MyUnisoft.
- L'exercice comptable concerné n'est pas clôturé dans MyUnisoft.
- La devise de la facture est autorisée dans MyUnisoft.
- Le pays du client ou du fournisseur est autorisé dans MyUnisoft.
- Les différents paramètres de synchronisation (journal, TVA, dossier comptable, etc.) sont correctement configurés.
Si après ces vérifications le problème persiste, contactez le support Sellsy via le chat en précisant la facture et/ou la période concernée.

___________________________________________________________

Autres articles associés

- [Gérer les profils de privilèges](https://help.sellsy.com/fr/articles/5864116-gerer-les-profils-de-privileges-de-mes-collaborateurs#h_108be3a993)
- [Activer la conformité](https://help.sellsy.com/fr/articles/6100605-activer-le-mode-conforme)
- [Comptabilisation des documents](https://help.sellsy.com/fr/articles/5875018-comptabiliser-une-facture-d-achat-de-vente)
- [Donner un accès Sellsy à mon expert-comptable](https://help.sellsy.com/fr/articles/6652377-donner-un-acces-sellsy-a-mon-expert-comptable)
- [Ajouter un taux de TVA](https://help.sellsy.com/fr/articles/5871870-ajouter-un-taux-de-tva)

Mis a jour le : 12/06/2026
