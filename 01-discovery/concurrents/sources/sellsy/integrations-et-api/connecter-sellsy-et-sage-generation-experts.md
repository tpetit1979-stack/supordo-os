---
source: https://help.sellsy.com/fr/articles/15480890-connecter-sellsy-et-sage-generation-experts
categorie: Intégrations et API
titre: Connecter Sellsy et Sage Génération Experts
date_recuperation: 2026-09-05
---

# Connecter Sellsy et Sage Génération Experts

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472749208/02c0e3e435642b7e4e91a8a4e772/FAQ-Bannie-CC-80reAcademy-2-2B-282-29.png?expires=1788635700&signature=60300bc88f820b4e9b3b094098e451695e0402d9925cadcd2d229c984aee4fec&req=diQgFM56lINfUfMW1HO4zYd6QBrRqVnPM2a3mrDqzgVhami9gScUKYaq%2FK9N%0AJ6ZTicKw60S85LViDus%3D%0A)

## Introduction

Bienvenue dans le [guide d'activation de connexion Sellsy x Sage Génération Experts](#h_b235d1d14a). Pour rappel, la connexion Sage Génération Experts est incluse dans votre licence Sellsy Facturation, aucun coût additionnel n'est associé à son usage. Elle permet de :

- Synchroniser automatiquement les avoirs et factures de vente depuis Sellsy vers Sage Génération Experts
- Synchroniser automatiquement les avoirs et factures d'achat depuis Sellsy vers Sage Génération Experts
- Transmettre les pièces jointes PDF associées aux factures
- Synchroniser les clients et fournisseurs (tiers)
- Créer automatiquement les comptes de tiers dans Sage Génération Experts lorsque nécessaire

> **Bon à savoir :** La synchronisation vers Sage Génération Experts ne concerne que les documents [comptabilisés dans Sellsy](https://help.sellsy.com/fr/articles/5875018-comptabiliser-des-factures-d-achat-et-de-vente). Si un document n'a pas encore été comptabilisé, il ne sera pas transmis à Sage Génération Experts lors des synchronisations automatiques.

### 
Données synchronisées

| Donnée | Pris en charge |
| --- | --- |
| Écritures de vente | ✅ |
| Pièces jointes de vente | ✅ |
| Écritures d'achat | ✅ |
| Pièces jointes d'achat | ✅ |
| Synchronisation / création des comptes tiers | ✅ |

> **Important :** Cette intégration fonctionne dans un seul sens. Les données sont transmises de Sellsy à Sage Génération Experts. Les modifications réalisées directement dans Sage Génération Experts ne sont pas automatiquement répercutées dans Sellsy.

___________________________________________________________

## Guide d'activation de connexion Sellsy x Sage Génération Experts

### 
⚠️ Avant de commencer

Avant de configurer la connexion entre Sellsy et Sage Génération Experts, assurez-vous de disposer des accès nécessaires et de remplir les prérequis techniques.

> **Important :** Nous recommandons que l’activation de cette intégration soit réalisée par votre expert-comptable. 
> Les licences des cabinets comptables disposent par défaut d’un accès API, ce qui n'est souvent pas le cas sur les licences d'une entreprise chez un outil comptable tel que Sage Génération Experts. De plus, les étapes de paramétrage comptable seront mieux maîtrisées si elles sont effectuées par votre cabinet.
> Avant de transmettre cette page à votre expert-comptable, assurez-vous d’avoir réalisé les étapes préalables dans votre compte Sellsy, [décrites ci-dessous](https://help.sellsy.com/fr/articles/15479499-connecter-sellsy-et-tiime#h_6cf220cff6).
> N’effectuez vous-même cette activation que si votre comptabilité est internalisée. Dans ce cas, assurez-vous que votre licence ou votre niveau de plan inclut un accès API.


Côté Sellsy

- Une licence Sellsy Facturation active ;
- Des [factures/avoirs comptabilisés](https://help.sellsy.com/fr/articles/5875018-comptabiliser-des-factures-d-achat-et-de-vente) (si un document n'a pas encore été comptabilisé, il ne sera pas transmis à Sage Génération Experts lors des synchronisations automatiques) ;
- La [conformité stricte active](https://help.sellsy.com/fr/articles/6100605-activer-le-mode-conforme-pour-les-documents-de-vente) sur le compte Sellsy ;
- Les droits nécessaires pour accéder aux intégrations comptables :
- **Vous êtes client Sellsy, votre comptabilité est internalisée et gérée chez** **Sage Génération Experts :** Vous devez disposer d'un profil administrateur ou d'un profil ayant accès aux paramètres d'intégration. Si vous ne disposez pas des droits nécessaires, contactez un administrateur de votre compte Sellsy. Pour en savoir plus sur les profils et privilèges Sellsy, consultez [cet article](https://help.sellsy.com/fr/articles/5864112-profils-de-privileges).
- **Vous êtes expert-comptable d'un client Sellsy :** Avant de poursuivre la configuration, assurez-vous que votre client vous a accordé un accès expert-comptable associé à un [profil administrateur](https://help.sellsy.com/fr/articles/5864112-profils-de-privileges). L'accès Expert-Comptable est gratuit et permet d'accéder aux données nécessaires à la synchronisation comptable. Si vous ne disposez pas encore d'un accès expert-comptable, votre client devra suivre la procédure décrite [dans cet article](https://help.sellsy.com/fr/articles/6652377-donner-un-acces-sellsy-a-mon-expert-comptable).


Côté Sage Génération Experts

✅ **Sur Sage Génération Experts, vous devez activer l'application publique « Chift » afin que l'échange de données avec Sage Génération Experts fonctionne.** 


​Tout d'abord, ouvrez le paramétrage Marketplace :


![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472971071/ae9b2f8cb47a73622d49b9774a23/919ff0c7-25b3-4a5e-b959-9b0d2e84f201-2Ff188f3b1-be88-408e-8b3d-8eb268f56bce-Screenshot_2025-04-16_at_19_13_26.png?expires=1788635700&signature=e82f8a00f0372ec73759bf62c1532cac14e070bb27e951196adaee696128ff7a&req=diQgFMB5nIFYWPMW1HO4zYp6Bi8UWqMsOEiPJdJqd7X8LSq1fHC6kz2y76HD%0A1zfrRt7gCaQ8CzJHXfI%3D%0A)


Dans la liste des applications vous trouverez une application nommée « Chift ». Si celle-ci n'est pas encore activée, double-cliquez dessus pour l'activer.

Sur la capture d'écran ci-dessous, vous pouvez voir une ligne indiquant l'identifiant de l'entité. Copiez-le et gardez-le quelque part, vous en aurez besoin plus tard.

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472971077/c26736767c2367f29a665f4f7a03/919ff0c7-25b3-4a5e-b959-9b0d2e84f201-2Fb3ac4560-7bd6-401c-a72f-9a587ebc7f45-Screenshot_2025-04-16_at_19_14_02.png?expires=1788635700&signature=2d78edb46ecc39a481577cd48154cbd311f9edba431ed6dd23d2f41a3f6fc065&req=diQgFMB5nIFYXvMW1HO4zbyEzSWvcyW6Fhu1rxp%2B8vIQotrKDzvrXx6a3til%0AeFtp57TJALQcwyFWKFY%3D%0A)


​Ensuite, acceptez les conditions d'utilisation et activez l'application :


![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472971081/00d1234069a098b658986869ebd9/919ff0c7-25b3-4a5e-b959-9b0d2e84f201-2F4681a8ee-b743-4b6d-a6d1-7d64d9029c07-Screenshot_2025-04-16_at_19_14_21.png?expires=1788635700&signature=9da94d39df608731aa32ea031728eaa6999e08fe3b935f6cfb0aa74822144b89&req=diQgFMB5nIFXWPMW1HO4zd5u235r56N3fetf2HnZr%2BfZoDzeIV%2BpuU7Urm%2Fr%0AKswQpsd%2BDZZRYMNbPWA%3D%0A)


​Vous voyez désormais que l'application est bien activée sur l'entité :


![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472971080/3c9d0d383aa32849c737498930a0/919ff0c7-25b3-4a5e-b959-9b0d2e84f201-2Ff7d63463-e2f8-42cb-8fee-7c09763795d3-Screenshot_2025-04-16_at_19_14_02_copy.png?expires=1788635700&signature=12201cb8bbf0a956568fb5e337cb0dde16bfc9cd007e930a51c1c5e5241f0414&req=diQgFMB5nIFXWfMW1HO4zQgeMHuVbX8GzUa7jqsy7yM0nIEg3QpB0tlq45zR%0AIPM2Cwy%2B3B7%2Bd3jzRdc%3D%0A)


✅ **Une fois ces étapes complétées, vous devez activer l'application Chift sur les dossiers comptables.**

> **Bon à savoir :** Cette étape, contrairement à la première, devra être effectuée pour chaque dossier comptable que vous souhaitez synchroniser via Chift.

Tout d'abord, ouvrez le dossier comptable pour lequel vous souhaitez activer l'application Chift :


![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472971083/d6a183a4cb8cc74982347a15452f/919ff0c7-25b3-4a5e-b959-9b0d2e84f201-2F597fe391-1058-48ab-afbc-ed295142157b-Screenshot_2024-12-18_at_10_10_57.png?expires=1788635700&signature=8a10637173ad2db04e954ad35c3cc1fbe684b38afef92845d9236276f4f571d7&req=diQgFMB5nIFXWvMW1HO4zfGqbmZ8bYLEJpsNMvR6GKOFrKQZxllhPRhp7KO1%0A%2FLWGplq3kM9dvaeEwXg%3D%0A)

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472971079/c4662d6543598b58ad48d20fd54e/919ff0c7-25b3-4a5e-b959-9b0d2e84f201-2F339dd245-cbc9-4cb3-a7dc-3fb1d22a7ab0-Screenshot_2024-12-18_at_10_11_05.png?expires=1788635700&signature=0d39675dca4b50ca039bfc24dd2b6953553ee789aa44b5b2e3813b8f5e3b14bc&req=diQgFMB5nIFYUPMW1HO4zWYT1C46AW%2ByvQjkYrFFUqFylBUzfvWTvPLtKiKi%0A9FNN974U3TF52blepBs%3D%0A)


​Rendez-vous ensuite sur Marketplace (applications du dossier) :


![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472971084/deeab172505274f418ee26981643/919ff0c7-25b3-4a5e-b959-9b0d2e84f201-2F02f09e26-b628-418a-a64b-38cf0bc9a2d6-Screenshot_2024-12-18_at_10_11_19.png?expires=1788635700&signature=693f0f40f22a444c890d1040c51c1e0196f847c32340ef53bcb10be4b630f3f9&req=diQgFMB5nIFXXfMW1HO4zdpL6eJ2%2Bb6sMbsfFyaIqkUkLTIy%2B7Ximm5aynNp%0AhmFvmhCSd0HU4PfC7Ow%3D%0A)


Si l'application Chift n'est pas encore activée, double-cliquez dessus pour l'activer. 

> **Important :** 4 applications Chift existent dans Sage. Choisissez celle qui permet de connecter vos logiciels financiers.

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472971075/78baae02a3d8abc5483185394bfc/919ff0c7-25b3-4a5e-b959-9b0d2e84f201-2Fb3ac4560-7bd6-401c-a72f-9a587ebc7f45-Screenshot_2025-04-16_at_19_14_02.png?expires=1788635700&signature=34ecea7d73b1e73823313fc80091334e3a9571774167e108d9f2a32b6ebb72fb&req=diQgFMB5nIFYXPMW1HO4zSANbgoPpnZn2QgxsSta2wgL0MREfiAOVxQ5uWlC%0Afg2W3VHbT1xe8k46RmM%3D%0A)


Acceptez les conditions d'utilisation et activez l'application. 

> **Important :** Si vous voyez une mention de charge de 10 € dans les conditions, sachez que Sage GE ne vous facturera pas. Il s'agit d'une erreur de la part de Sage en cours de rectification.

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472971092/534e54f73b028f3525adf7ecbd7b/919ff0c7-25b3-4a5e-b959-9b0d2e84f201-2F7baac840-0692-4a53-be3c-1466510784e7-Screenshot_2024-12-18_at_10_12_50.png?expires=1788635700&signature=2708db3961481f624bf0968569bbacfb4d235ca62cd64f3602dc2340b4c7fe44&req=diQgFMB5nIFWW%2FMW1HO4zd8FPz3DsBBfDRutSTuornfGIZFSSxiRdabTfe3o%0AXsPeFxHwApwCkgHsuZY%3D%0A)


Vous voyez désormais que l'application est bien activée sur le dossier comptable :

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472971089/5b1f6bfaac4dc80cefd5c50618ac/919ff0c7-25b3-4a5e-b959-9b0d2e84f201-2F66369c43-7efc-416e-b70c-8c5e93efba8a-Screenshot_2024-12-18_at_10_13_43.png?expires=1788635700&signature=c889ac492d6476c73118fd9454e0f5a0507cd384e0b11a9013769e99fdc0a989&req=diQgFMB5nIFXUPMW1HO4zSLjjIn48goiapSOkeIi1iUvxF%2B6B6dNthswI3ju%0AbSbqiO6PxSpRFQjZ3hQ%3D%0A)

Maintenant vous pouvez commencer les étapes de connexion entre Sellsy et Sage GE dans Chift.


​

### 👉  Étape 1 : Connecter Sage Génération Experts dans Sellsy

Depuis la [page marketplace Sellsy à propos de l’intégration Sage Génération Experts](https://go.sellsy.com/applications/sage-generation-experts) cliquez sur : « **Activer l’intégration** ».

Ou bien cliquez directement sur [ce lien](https://marketplaces.chift.app/fr/sellsy/apps/8015). Vous serez redirigé vers l'interface sécurisée Chift.
​

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472967944/d041a0895613074f11380f6d1517/Capture+d%E2%80%99e%CC%81cran+2026-06-12+a%CC%80+16_32_58.png?expires=1788635700&signature=a7b0216342b414b2dabda25ed342e62383dd3c24a5fc368782b791938ab41b4e&req=diQgFMB4mohbXfMW1HO4zQzTS9Xzwn72QwgGS3%2F9N%2B6q1K0KF2EwbQlTJrgQ%0ATzvStyQOrcBHDJ7pNDA%3D%0A)

### 
👉  Étape 2 : Authentifier la connexion

Dans l’interface Chift, cliquez sur « **Activer l’intégration** ». Si c’est votre première connexion pour ce compte, cliquez sur « **En créer une nouvelle** ».

Si une connexion a déjà été créée pour ce compte, sélectionnez simplement le compte correspondant dans le menu déroulant, puis cliquez sur « **Valider** ».

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472754813/2a8e4999d86bc2f6854960a3acab/Capture-2Bd-E2-80-99e-CC-81cran-2B2026-05-29-2Ba-CC-80-2B15_55_08.png?expires=1788635700&signature=227867d99ccc204e1a07ff788436dd653b9e701f8503ae773a1a05f00be5118e&req=diQgFM57mYleWvMW1HO4zZofbdnQEwh8q3I6GLIComFKBQEiiVdvT9aeh%2B0w%0A4Zas5WcsHQ5B7cNj4Lw%3D%0A)

Pour créer une nouvelle connexion, munissez-vous du nom et du numéro SIRET de l’entreprise utilisant Sellsy. Renseignez ces informations, puis cliquez sur « **Enregistrer** ».

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472754816/5e6bea0befc76504f319e533903a/Capture-2Bd-E2-80-99e-CC-81cran-2B2026-05-29-2Ba-CC-80-2B15_58_07.png?expires=1788635700&signature=fc01a1abc676899749dbee1307113b696adb2cb7002f9710861e15842bfe63cc&req=diQgFM57mYleX%2FMW1HO4zediP9gcutPeIc9Gw%2FR8f3yeqMe%2B3SFYofqrPPxo%0AbUxeMlM7%2BLGp9l8zjkE%3D%0A)

Une fois ces étapes complétées, vous allez vous retrouver sur un écran comme celui-ci :

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2473009336/2c48c4254c4d15533fa65c4a439d/Capture+d%E2%80%99e%CC%81cran+2026-06-12+a%CC%80+16_50_04.png?expires=1788635700&signature=368d211986cb9fa7e9e7417d76c4335826fe3371ca60c3933c70ac696b20f86c&req=diQgFcl%2BlIJcX%2FMW1HO4zflr3d07Re5HWyGtzFdyCKS%2FghmOpVe863IuSUq5%0A9YbL9Fqzin0XbbQzNs4%3D%0A)

En cliquant sur « **Connecter** », vous serez redirigé vers l’écran de connexion Sellsy.

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472754823/2f9ec0970dad2469de0c69370e6f/Capture-2Bd-E2-80-99e-CC-81cran-2B2026-05-29-2Ba-CC-80-2B16_00_46.png?expires=1788635700&signature=ac5ab1305c1278a0cc6a044da626e7f80e93a9ec770703d36edad1f8128fc7cb&req=diQgFM57mYldWvMW1HO4zZuVRnnA4lnan%2FGMsVnVCYQRUVidn79egCDRwOqP%0AfDG3YeGj8Fc9TSUj4mE%3D%0A)

Il vous suffit de renseigner vos identifiants Sellsy. Si plusieurs comptes sont associés à ces identifiants, sélectionnez le compte concerné dans le menu déroulant.

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472754821/cf1be6706b489bbe48d9e45516c2/Capture-2Bd-E2-80-99e-CC-81cran-2B2026-05-29-2Ba-CC-80-2B16_01_26-2B-1-.png?expires=1788635700&signature=ff595109e0a57a34a93fc4a483f4782def9704a10c113404f8b7b2ad26095223&req=diQgFM57mYldWPMW1HO4zU01bq5CodONJijGsKILEjn9EyN35XegbR2Dd3Fl%0ACMDmPgixkgOOfrCYMzE%3D%0A)

Puis, autoriser la connexion via Chift en cliquant sur « **Autoriser** ».

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472754822/2cd1577bdb11cc8c92ee925071a7/Capture-2Bd-E2-80-99e-CC-81cran-2B2026-05-29-2Ba-CC-80-2B16_01_36.png?expires=1788635700&signature=b7d3d2d29c9d3b949e2062449549254cb5e215307bce510d371ee48bea6b3a8d&req=diQgFM57mYldW%2FMW1HO4zQ8fws3oB6UFvqP9t4%2BoXcyOvQO08tQa82jSUqUI%0AHRJebAbTsMcLMgEv%2Bqg%3D%0A)

Vous serez ensuite redirigé vers la seconde étape d’authentification, qui vous permettra de vous connecter à votre environnement Sage GE.

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2473012683/26650baaa5356eaadfc9f758afd5/Capture+d%E2%80%99e%CC%81cran+2026-06-12+a%CC%80+16_51_32.png?expires=1788635700&signature=c9687b6e3d7b032e2d777ae0121ccbc3bd8cb03f1e09de79a672aeec7b68f4c6&req=diQgFcl%2Fn4dXWvMW1HO4zV%2BG%2B7KTDrNXBlIPPn0yRIFQHlxyfYnaI%2BixX%2BdA%0A61X1BiHVxzYqzyy46ys%3D%0A)

Sur cet nouvel écran, vous allez avoir besoin de l'identifiant de votre entité, récupéré plus tôt lors des étapes à réaliser dans Sage GE. Une fois les identifiants saisis, il suffit de cliquer sur « **Connecter** ».
​

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2473018516/ab87178938c5294daaf887e339a5/Capture+d%E2%80%99e%CC%81cran+2026-06-12+a%CC%80+16_52_36.png?expires=1788635700&signature=b5ec20bc8c2358b9e8c7ed5f606da8253612b34b4742839a4d81420537fc5f08&req=diQgFcl%2FlYReX%2FMW1HO4zb0mi9PBTc1OR4E2jka9%2BcWCsnOwdkBS2jEOZ%2FQQ%0ANuUYQQoWsE585987rdQ%3D%0A)


Depuis le menu déroulant, vous devez choisir le compte comptable à utiliser et cliquer ensuite sur « **Valider** ».
​
En dernière étape, vous devez choisir la typologie des documents à synchroniser (ventes, achats ou les deux).
​

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472754828/ddebf15a9ab486a6b21443563d46/Capture-2Bd-E2-80-99e-CC-81cran-2B2026-06-12-2Ba-CC-80-2B12_38_34.png?expires=1788635700&signature=f8a1ff64bfc2a748e3706a75d3b91de8f954f53957b179379b83f8bd13f17cb9&req=diQgFM57mYldUfMW1HO4zewq7iNIw52HhJHHUaWcsCD7gW9CXcIXPU2Qi2pd%0Aeu25m9GjXUDM%2FahCrRg%3D%0A)


Une fois la sélection effectuée, vous pouvez déterminer les paramètres de connexion entre Sellsy et Sage Génération Experts.


​

### 
👉  Étape 3 : Déterminer les paramètres de connexion

Une fois l'authentification terminée, vous devez configurer les correspondances comptables entre Sellsy et Sage GE.

Cette étape permet au connecteur de savoir comment traduire les données présentes dans Sellsy vers les bons éléments comptables dans Sage GE.

Pour rappel, l'intégration permet de récupérer les documents de vente et/ou d'achat présents dans Sellsy et de les transmettre automatiquement à Sage GE, accompagnés de leurs pièces jointes.

Vous devrez compléter les correspondances pour les éléments suivants :

- Taux / codes de TVA de vente
- Taux / codes de TVA d'achat
- Codes de TVA utilisés pour les arrondis
- Journaux comptables
- Comptes comptables
- Comptes de rabais, remises et ristournes

1. Taux / Codes de TVA de vente

Associez chaque taux ou code de TVA utilisé dans Sellsy au code de TVA correspondant dans Sage GE.

Cette correspondance permet au connecteur d'affecter correctement les montants de TVA sur les écritures de vente exportées. Exemple :

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472754831/5ddf2f3ddd22bd1d41a8f05905c1/Capture-2Bd-E2-80-99e-CC-81cran-2B2026-05-29-2Ba-CC-80-2B16_43_36.png?expires=1788635700&signature=48e64383c1749d6eeecd6995c9dc5ba0c7e899d798ca7442ee5c9fc4aeb29320&req=diQgFM57mYlcWPMW1HO4zd7f%2F4Sq7xIwtrxqieLu8C4n%2B2XZ6mEzZ665cDk2%0AVoD6JdiWWykVkMPLCro%3D%0A)

2. Taux / Codes de TVA d'achat

Associez chaque taux ou code de TVA utilisé sur vos factures fournisseurs Sellsy au code correspondant dans Sage GE.

Cette étape garantit une comptabilisation correcte de la TVA déductible lors de l'export des achats. Exemple :

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472754833/8f0a36a07d846056f5b3be549ad7/Capture-2Bd-E2-80-99e-CC-81cran-2B2026-05-29-2Ba-CC-80-2B16_43_36.png?expires=1788635700&signature=d6ad4f9bd707545b4eeea11acc689ad78218566f34aaab9a037e3284b0bc3f73&req=diQgFM57mYlcWvMW1HO4zSJdZ6g2RHUJalzgcKxKZUlsi549kRBGpZGxtO1L%0AtJBlYdSugqtxoFDoOGM%3D%0A)

3. Codes TVA pour les arrondis

Certaines écritures peuvent engendrer des écarts d'arrondi de quelques centimes.

Vous devez indiquer le code de TVA à utiliser pour ces ajustements afin de garantir l'équilibre des écritures transmises dans Sage GE. Exemple :

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472754835/ecd631603c8dbe499951a150ebfd/Capture-2Bd-E2-80-99e-CC-81cran-2B2026-05-29-2Ba-CC-80-2B16_46_37.png?expires=1788635700&signature=c1f7a03033af02ffdb0a5d576ab50550be23009bed37f725e685cfb0e8ddb51c&req=diQgFM57mYlcXPMW1HO4zVZfID5gaq4EmNUU8FBWlNxNTFFbYoNA7cItoUcT%0AFxfPOeoF5YsTQBXW6PA%3D%0A)

4. Journaux comptables

Associez les journaux Sellsy aux journaux comptables existants dans Sage GE. Par exemple :

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472754837/8d66820127c37d20529cfc7cafab/Capture-2Bd-E2-80-99e-CC-81cran-2B2026-05-29-2Ba-CC-80-2B16_47_07.png?expires=1788635700&signature=cfb3981f91698d7c1bac50079add88bb440c00c93ec479847cb27cf25704ac37&req=diQgFM57mYlcXvMW1HO4zRI%2BlIjAlcKJaVxMPXZ%2FY2uHpfTASpjcTRWjzqHC%0AwY1CTs5SrxyDghtbpjQ%3D%0A)

Les journaux sélectionnés doivent avoir été préalablement autorisés lors du partage du dossier dans Sage GE.

5. Comptes comptables

Associez les comptes comptables utilisés dans Sellsy aux comptes correspondants dans Sage GE.

Ces correspondances permettent d'affecter correctement les écritures comptables lors de leur création.

Nous vous recommandons de vérifier la cohérence entre votre plan comptable Sellsy et votre plan comptable Sage GE avant de valider le paramétrage.

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472754839/dda924236cf422a7fda56f4058bc/Capture-2Bd-E2-80-99e-CC-81cran-2B2026-05-29-2Ba-CC-80-2B16_50_04.png?expires=1788635700&signature=23efa751844c7cf0621b0c79ba3dc5922623c2b207bc99704a63e0bc1e754539&req=diQgFM57mYlcUPMW1HO4zRrPfm5uoRhdpd5jOX%2FJtRvwPn0vy3Yl3sAmZ%2Fqy%0A3GRuuF3exs5VhSopOdE%3D%0A)

6. Rabais, remises et ristournes

Si vous utilisez des rabais, remises ou ristournes dans Sellsy, vous devez également définir les comptes comptables qui recevront ces montants dans Sage GE en cliquant sur « **Oui** », puis sur « **Enregistrer** ».

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472754871/f74fadc0e7730a911fc55b9d2d2d/Capture-2Bd-E2-80-99e-CC-81cran-2B2026-05-29-2Ba-CC-80-2B16_51_33.png?expires=1788635700&signature=c7c4da734e740e832460c59c787ba849499cffeb35789ad4eb462d2d5e44ce59&req=diQgFM57mYlYWPMW1HO4zS0LvSN8ifntRaOreFY%2F3PJ7t4XnDOwLDrONvFYj%0Aap%2FgVE%2BXU9%2FMxFUOkuE%3D%0A)

Autrement, cliquez sur « **Non** », puis sur « **Passer** ».

En cas de doute, rapprochez-vous de votre cabinet comptable ou de votre administrateur Sage GE.
​

### 
👉  Étape 4 : Derniers ajustements techniques

Votre connexion est maintenant configurée.

Avant d'activer l'intégration, quelques paramètres complémentaires vous permettent d'adapter le fonctionnement de la synchronisation à votre organisation comptable.

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472754854/4839d48b2f1d37da09c8098dec73/Capture-2Bd-E2-80-99e-CC-81cran-2B2026-05-29-2Ba-CC-80-2B16_54_13.png?expires=1788635700&signature=0a485ce17d861dfc76baff844224257e1d45ae8fd9f3f955e9a50e486e0d57d0&req=diQgFM57mYlaXfMW1HO4zbz79yYvLXsU9sX94YffRaCeVSzmhypexy6B3p6i%0AtMQxNyl%2FEFD9sFGVctk%3D%0A)

1. Date de début de synchronisation

Sélectionnez la date à partir de laquelle les factures/avoirs Sellsy devront être transmis à Sage GE.

Chaque nuit, le connecteur synchronisera automatiquement les factures et avoirs :

- ayant une date égale ou postérieure à la date sélectionnée ;
- marqués comme devant être envoyées en comptabilité.

> **Bon à savoir :**  Si vous mettez en place l'intégration pour la première fois, choisissez une date cohérente avec votre période comptable afin d'éviter l'export de documents déjà traités dans Sage GE.

2. Création des écritures en brouillon / attente

La création des écritures en brouillon via API n'est pas prise en charge par Sage GE : le choix effectué sur cette étape n'aura aucun impact sur la synchronisation.

> **Bon à savoir :** L'absence de création d'écritures en brouillon/attente ne signifie pas qu'une écriture ne peut pas être modifiée post-import. Elle peut être modifiée à tout moment en comptabilité. L'écriture arrivera, par défaut, en « **traitée **», mais le statut peut être modifié en « **à traiter** » post-import automatique.

3. Synchroniser les documents sans justificatif

Choisissez si les factures ou avoirs ne disposant pas de pièce jointe doivent être transmis à Sage GE.

- Oui : Les documents seront synchronisés même si aucun justificatif n'est associé.
- Non : Seuls les documents accompagnés d'un justificatif seront transmis.

> **Important :** Nous recommandons de désactiver cette option si votre cabinet comptable exige systématiquement la présence d'un justificatif pour chaque écriture.

4. Libellé des écritures

Définissez la manière dont les libellés des écritures comptables seront générés dans Sage GE.

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

Les nouvelles factures et avoirs répondant aux critères définis seront transmis à Sage GE avec leurs écritures comptables, leurs tiers et leurs pièces jointes associées.

> **Important : **Nous recommandons de vérifier attentivement les premiers documents transmis dans Sage GE. Plus une anomalie est détectée tôt, plus elle est simple à corriger. Une fois les premiers contrôles validés et les éventuels ajustements effectués, l’intégration fonctionnera de manière autonome.

___________________________________________________________

## **Questions fréquentes**

L'intégration fonctionne uniquement de Sellsy vers Sage GE.
Les factures et avoirs créés **[et comptabilisés](https://help.sellsy.com/fr/articles/5875018-comptabiliser-des-factures-d-achat-et-de-vente)** dans Sellsy, ainsi que les écritures comptables, les tiers et les pièces jointes associées, sont automatiquement transmis vers Sage GE.
Les modifications réalisées directement dans Sage GE ne sont pas automatiquement répercutées dans Sellsy.
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

Lorsqu'une écriture a déjà été créée dans Sage GE, la correction doit généralement être réalisée directement dans Sage GE.
Si l'erreur est liée au paramétrage du connecteur (code TVA, compte comptable, journal, etc.), nous recommandons également de corriger la configuration de l'intégration afin d'éviter que l'erreur ne se reproduise lors des synchronisations suivantes.
Dans la majorité des cas, les corrections d'écritures déjà intégrées sont réalisées dans Sage GE.
​

Nous recommandons de vérifier attentivement les premières factures et avoirs transmis dans Sage GE afin de confirmer que :
- Les comptes comptables sont corrects
- Les codes TVA sont correctement affectés
- Les journaux utilisés sont les bons
- Les tiers sont correctement créés ou rapprochés
- Les pièces jointes sont bien présentes
Plus une anomalie est détectée tôt, plus elle est simple à corriger.
Une fois les premiers contrôles validés et les éventuels ajustements effectués, l'intégration fonctionnera de manière autonome et vous n'aurez généralement plus à intervenir sur son paramétrage.
​

Lors de la synchronisation, le connecteur recherche automatiquement une correspondance existante dans Sage GE à partir de plusieurs critères :
- Compte auxiliaire
- Numéro de TVA
- SIRET ou numéro d'entreprise
- Nom du tiers
Si aucune correspondance n'est trouvée, un nouveau client ou fournisseur est créé automatiquement dans Sage GE.
​

Pour faciliter le suivi des écritures importées depuis Sellsy, nous recommandons de définir avec votre cabinet comptable :
- Des journaux dédiés aux flux Sellsy
- Une convention de libellés spécifique
- Une procédure de contrôle des imports
Cette organisation permet généralement d'identifier facilement les écritures provenant de l'intégration.
​

Les pièces jointes associées aux documents de vente et d'achat peuvent être transmises vers Sage GE avec les écritures comptables.
​[Lors du paramétrage de l'intégration](#h_e05988a243), vous pouvez choisir de synchroniser tous les documents ou uniquement ceux disposant d'un justificatif.
​

Nous préconisons de faire intervenir votre expert-comptable pour la configuration de l'intégration. Assurez-vous qu'il dispose d'un [accès gratuit expert-comptable](https://help.sellsy.com/fr/articles/6652377-donner-un-acces-sellsy-a-mon-expert-comptable) avec un [profil d'administrateur](https://help.sellsy.com/fr/articles/5864112-profils-de-privileges).


La comptabilité analytique n'est pas prise en charge par cette intégration.


Nous vous conseillons de vous rapprocher de votre administrateur afin de vérifier la configuration de l'environnement Sage GE.
​

Nous vous conseillons de vous rapprocher de votre administrateur afin de vérifier la configuration de l'environnement Sage GE.
​

Nous vous conseillons de vous rapprocher de votre administrateur afin de vérifier la configuration de l'environnement Sage GE.
​

 Veuillez vérifier que :
- La facture a bien été comptabilisée dans Sellsy. Les documents de vente et d'achat non comptabilisés ne sont pas synchronisés vers Sage GE.
- L'exercice comptable concerné n'est pas clôturé dans Sage GE.
- La devise de la facture est autorisée dans Sage GE.
- Le pays du client ou du fournisseur est autorisé dans Sage GE.
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
