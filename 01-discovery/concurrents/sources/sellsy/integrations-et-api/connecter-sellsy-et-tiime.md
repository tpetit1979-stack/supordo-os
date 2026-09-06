---
source: https://help.sellsy.com/fr/articles/15479499-connecter-sellsy-et-tiime
categorie: Intégrations et API
titre: Connecter Sellsy et Tiime
date_recuperation: 2026-09-05
---

# Connecter Sellsy et Tiime

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472460921/12e56abba1d91b7ffcb5f2c57a4a/FAQ-Bannie-CC-80reAcademy-2-2B-282-29.png?expires=1788635700&signature=b5376dda6e93364128595da8402ef181289b5780f4e79cf67d5aa36bc19f80f1&req=diQgFM14nYhdWPMW1HO4zRThFnjMYOQfDjktcO6XX4poOnigB5WctEHbP1MQ%0ASz9HWxePgYkTKgO7VsU%3D%0A)

## Introduction

Bienvenue dans le [guide d'activation de connexion Sellsy x Tiime](#h_a41153e1b5). Pour rappel, la connexion Tiime est incluse dans votre licence Sellsy Facturation, aucun coût additionnel n'est associé à son usage. Elle permet de :

- Synchroniser automatiquement les avoirs et factures de vente depuis Sellsy vers Tiime
- Synchroniser automatiquement les avoirs et factures d'achat depuis Sellsy vers Tiime
- Transmettre les pièces jointes PDF associées aux factures
- Synchroniser les clients et fournisseurs (tiers)
- Créer automatiquement les comptes de tiers dans Tiime lorsque nécessaire

> **Bon à savoir :** La synchronisation vers Tiime ne concerne que les documents [comptabilisés dans Sellsy](https://help.sellsy.com/fr/articles/5875018-comptabiliser-des-factures-d-achat-et-de-vente). Si un document n'a pas encore été comptabilisé, il ne sera pas transmis à Tiime lors des synchronisations automatiques.

### 
Données synchronisées

| Donnée | Pris en charge |
| --- | --- |
| Écritures de vente | ✅ |
| Pièces jointes de vente | ✅ |
| Écritures d'achat | ✅ |
| Pièces jointes d'achat | ✅ |
| Synchronisation / création des comptes tiers | ✅ |

> **Important :** Cette intégration fonctionne dans un seul sens. Les données sont transmises de Sellsy à Tiime. Les modifications réalisées directement dans Tiime ne sont pas automatiquement répercutées dans Sellsy.

___________________________________________________________

## Guide d'activation de connexion Sellsy x Tiime

### 
⚠️ Avant de commencer

Avant de configurer la connexion entre Sellsy et Tiime, assurez-vous de disposer des accès nécessaires et de remplir les prérequis techniques.

> **Important :** Nous recommandons que l’activation de cette intégration soit réalisée par votre expert-comptable. 
> Les licences des cabinets comptables disposent par défaut d’un accès API, ce qui n'est souvent pas le cas sur les licences d'une entreprise chez un outil comptable tel que Tiime. De plus, les étapes de paramétrage comptable seront mieux maîtrisées si elles sont effectuées par votre cabinet.
> Avant de transmettre cette page à votre expert-comptable, assurez-vous d’avoir réalisé les étapes préalables dans votre compte Sellsy, [décrites ci-dessous](#h_6cf220cff6).
> N’effectuez vous-même cette activation que si votre comptabilité est internalisée. Dans ce cas, assurez-vous que votre licence ou votre niveau de plan inclut un accès API.

Côté Sellsy

- Une licence Sellsy Facturation active ;
- Des [factures/avoirs comptabilisés](https://help.sellsy.com/fr/articles/5875018-comptabiliser-des-factures-d-achat-et-de-vente) (si un document n'a pas encore été comptabilisé, il ne sera pas transmis à Tiime lors des synchronisations automatiques) ;
- La [conformité stricte active](https://help.sellsy.com/fr/articles/6100605-activer-le-mode-conforme-pour-les-documents-de-vente) sur le compte Sellsy ;
- Les droits nécessaires pour accéder aux intégrations comptables :
- **Vous êtes client Sellsy, votre comptabilité est internalisée et gérée chez Tiime :** Vous devez disposer d'un profil administrateur ou d'un profil ayant accès aux paramètres d'intégration. Si vous ne disposez pas des droits nécessaires, contactez un administrateur de votre compte Sellsy. Pour en savoir plus sur les profils et privilèges Sellsy, consultez [cet article](https://help.sellsy.com/fr/articles/5864112-profils-de-privileges).
- **Vous êtes expert-comptable d'un client Sellsy :** Avant de poursuivre la configuration, assurez-vous que votre client vous a accordé un accès expert-comptable associé à un [profil administrateur](https://help.sellsy.com/fr/articles/5864112-profils-de-privileges). L'accès Expert-Comptable est gratuit et permet d'accéder aux données nécessaires à la synchronisation comptable. Si vous ne disposez pas encore d'un accès expert-comptable, votre client devra suivre la procédure décrite [dans cet article](https://help.sellsy.com/fr/articles/6652377-donner-un-acces-sellsy-a-mon-expert-comptable).


Côté Tiime

Si votre comptabilité est internalisée et gérée chez Tiime, une licence *Business* permettant les intégrations avec vos outils (API) est nécessaire. Autrement, aucun prérequis n'est nécessaire côté Tiime. 

Si vous avez des questions, nous vous conseillons de vous mettre en relation avec les équipes Tiime ou de [consulter les pages d'aide de Tiime](https://support.tiime.fr/fr/).


​

### 👉  Étape 1 : Connecter Tiime dans Sellsy

Depuis la [page marketplace Sellsy à propos de l’intégration Tiime](https://go.sellsy.com/applications/tiime) cliquez sur : « **Activer l’intégration** ».

Ou bien cliquez directement sur [ce lien](https://marketplaces.chift.app/fr/sellsy/apps/8021). Vous serez redirigé vers l'interface sécurisée Chift.
​

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472488002/d782a3e461361123842656555d20/Capture+d%E2%80%99e%CC%81cran+2026-06-12+a%CC%80+12_23_13.png?expires=1788635700&signature=186c8559da375dccef941b47762eb11111e3449fd9ac85a467f4b33be45526f9&req=diQgFM12lYFfW%2FMW1HO4zcLWvECNK98paYviqn0BdFiHU3viO%2BrT7lSr7z9H%0AxSuXwt%2FogedrVKzBvv4%3D%0A)

### 
👉  Étape 2 : Authentifier la connexion

Dans l’interface Chift, cliquez sur « **Activer l’intégration** ». Si c’est votre première connexion pour ce compte, cliquez sur « **En créer une nouvelle** ».

Si une connexion a déjà été créée pour ce compte, sélectionnez simplement le compte correspondant dans le menu déroulant, puis cliquez sur « **Valider** ».

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472461916/aa6001230a1726709fda56378816/Capture-2Bd-E2-80-99e-CC-81cran-2B2026-05-29-2Ba-CC-80-2B15_55_08.png?expires=1788635700&signature=ba8f256478d4666f0adaa2f9771c74ff5991bbdc39fb2e423b29f740df62efed&req=diQgFM14nIheX%2FMW1HO4zc7BtLx%2FwcFU4m%2BE5p6UtnBGpqgU7KhBP4lThJZH%0ALmT1SgKkvZOidHSiKkg%3D%0A)

Pour créer une nouvelle connexion, munissez-vous du nom et du numéro SIRET de l’entreprise utilisant Sellsy. Renseignez ces informations, puis cliquez sur « **Enregistrer** ».

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472461917/c1beacbf5d82e68de2718bf83741/Capture-2Bd-E2-80-99e-CC-81cran-2B2026-05-29-2Ba-CC-80-2B15_58_07.png?expires=1788635700&signature=a1da359676f43f585aee87d7457f246a1deec813cb9a6a3b68bccaf2320dddbe&req=diQgFM14nIheXvMW1HO4zYKsOgEu0IopjMZCqvlahj4qQ9Z2nAntsRYi0RTG%0Aw%2BBlDqkxSzgYeLFa6nc%3D%0A)

Une fois ces étapes complétées, vous allez vous retrouver sur un écran comme celui-ci :

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472488998/5c1f336eb3cdf6d160475ba9636c/Capture+d%E2%80%99e%CC%81cran+2026-06-12+a%CC%80+12_23_40.png?expires=1788635700&signature=ea0bdcfd6de5e20998c6528b534bce6630548d9fa46ae4b60cd372b2b5eb0f60&req=diQgFM12lYhWUfMW1HO4zTbfYjG70bfEA58ldIUokaao2Jf6j5N1jLU%2BJ%2BLD%0A%2Fw7a6fBQOea4UEgjFow%3D%0A)

En cliquant sur « **Connecter** », vous serez redirigé vers l’écran de connexion Sellsy.

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472461918/448ba64557ecc50dc391e6df4801/Capture-2Bd-E2-80-99e-CC-81cran-2B2026-05-29-2Ba-CC-80-2B16_00_46.png?expires=1788635700&signature=489ff2402dabe449c1b9fa4c3514888982e28b091e7e07ad3da641cf012d6fac&req=diQgFM14nIheUfMW1HO4zaPXUwIRY184U245oTz07tyXZckJHOsxI5TDcvax%0AY8wi7odwxdplODZLmIY%3D%0A)

Il vous suffit de renseigner vos identifiants Sellsy. Si plusieurs comptes sont associés à ces identifiants, sélectionnez le compte concerné dans le menu déroulant.

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472461919/7a71076cec91ec7a92678524eeaa/Capture-2Bd-E2-80-99e-CC-81cran-2B2026-05-29-2Ba-CC-80-2B16_01_26-2B-1-.png?expires=1788635700&signature=e8c9b3410d6235bb8ed6d18f5dde8b725bc1723dc200908681f011de49a44c36&req=diQgFM14nIheUPMW1HO4zb4vd2ednfX0eQAjFVy%2FDVounYBUW7uCK%2B%2FBdfhv%0APPPRCoiwvNoxFKQpKkg%3D%0A)

Puis, autoriser la connexion via Chift en cliquant sur « **Autoriser** ».

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472461925/d3354203b24dc353c8e752d8f56c/Capture-2Bd-E2-80-99e-CC-81cran-2B2026-05-29-2Ba-CC-80-2B16_01_36.png?expires=1788635700&signature=37cd9ecd830684130a7615a29fb7a63293b9b710d246c0e7ca9e387110d81441&req=diQgFM14nIhdXPMW1HO4zeAga98ZsxO2cyIersj8Vn7ERd80gC7yocBIDtOH%0A6RUz3AZNQV6qY8Cu%2FN8%3D%0A)

Vous serez ensuite redirigé vers la seconde étape d’authentification, qui vous permettra de vous connecter à votre environnement Tiime.

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472489780/dfcd605e080cbf327a6c7e106f14/Capture+d%E2%80%99e%CC%81cran+2026-06-12+a%CC%80+12_24_24.png?expires=1788635700&signature=2838281a2653f6d07429f179484c48c4c8b4b87a28f9c5a86be0a36d3652201d&req=diQgFM12lIZXWfMW1HO4zXUGrs8SOwMBcx1rR8eJUiLAVnz8FsvHviYX8fXT%0AWvgkPXMGRBzOBWWdlHI%3D%0A)

Si vous n'êtes pas encore connecté(e) à votre compte Tiime, vous allez être rédirigé(e) vers une page de connexion. Alternativement, vous pouvez effectuer cette démarche dans un onglet à part. Une fois connecté(e), il suffit de cliquer sur « **Autoriser** ».
​

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472490601/087d3711409770bc6a8f55170d1c/Capture+d%E2%80%99e%CC%81cran+2026-06-12+a%CC%80+12_24_51.png?expires=1788635700&signature=dcf9462168a17e914dfd14d75e4b7ae8c1b0db01c8545699feaee2cbd6872e3c&req=diQgFM13nYdfWPMW1HO4zVeYicqEirPNXPL%2ByP1nVwR8UAbVRL7dTgInAuvL%0AH2eQwLpsPa8SWAo9eNQ%3D%0A)


Depuis le menu déroulant, vous devez choisir le compte comptable à utiliser et cliquer ensuite sur « **Valider** ».
​

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472495721/ebf42d42b86a8a70c77e9492a676/Capture+d%E2%80%99e%CC%81cran+2026-06-12+a%CC%80+12_37_02.png?expires=1788635700&signature=edfe3713dc357a2dd21af1c818d10ea7431e3d0d5af1a4b7063f9b7c672e50a2&req=diQgFM13mIZdWPMW1HO4zR2evdf%2BLqY%2BXcrSU1FPFaUCmmOsXeufAmtdBO15%0A5aHv1VcmBq6T83M0nC0%3D%0A)


En dernière étape, vous devez choisir la typologie des documents à synchroniser (ventes, achats ou les deux).
​

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472498791/b6df23e19e64a703a0bb77f9f9ec/Capture+d%E2%80%99e%CC%81cran+2026-06-12+a%CC%80+12_38_34.png?expires=1788635700&signature=6fcb4f9f5c46bb9698cfa3dbb4547ffceb6143b8be582783ad7ed4164a446cac&req=diQgFM13lYZWWPMW1HO4zT9HfqJund3Cb3OoXetDYZMf7dKUxxmZFHoczroA%0ApHUrrzEyDcSLZirvQLg%3D%0A)


Une fois la sélection effectuée, vous pouvez déterminer les paramètres de connexion entre Sellsy et Tiime.

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472502411/f645b16304a26887b7a6f3f0e2c5/Capture+d%E2%80%99e%CC%81cran+2026-06-12+a%CC%80+12_41_17.png?expires=1788635700&signature=6c00f5d5fc17522c48736c2a72e3e6794d166045cb6783029c7db28c79013e88&req=diQgFMx%2Bn4VeWPMW1HO4zcu56WZXpQvCJc%2FcjrwIVBDqpTbaKHHxWShLV%2B55%0Ai94HDvY6k2OP%2BQUKUOw%3D%0A)


​

### 
👉  Étape 3 : Déterminer les paramètres de connexion

Une fois l'authentification terminée, vous devez configurer les correspondances comptables entre Sellsy et Tiime.

Cette étape permet au connecteur de savoir comment traduire les données présentes dans Sellsy vers les bons éléments comptables dans Tiime.

Pour rappel, l'intégration permet de récupérer les documents de vente et/ou d'achat présents dans Sellsy et de les transmettre automatiquement à Tiime, accompagnés de leurs pièces jointes.

Vous devrez compléter les correspondances pour les éléments suivants :

- Taux / codes de TVA de vente
- Taux / codes de TVA d'achat
- Codes de TVA utilisés pour les arrondis
- Journaux comptables
- Comptes comptables
- Comptes de rabais, remises et ristournes

1. Taux / Codes de TVA de vente

Associez chaque taux ou code de TVA utilisé dans Sellsy au code de TVA correspondant dans Tiime.

Cette correspondance permet au connecteur d'affecter correctement les montants de TVA sur les écritures de vente exportées. Exemple :

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472461926/dfbfab341d030700d45ed19f13fb/Capture-2Bd-E2-80-99e-CC-81cran-2B2026-05-29-2Ba-CC-80-2B16_43_36.png?expires=1788635700&signature=c08434f00bda7fad3042da015bca4301f779f26bc712327975659fef1c6ccc0b&req=diQgFM14nIhdX%2FMW1HO4za9dukigvvhPMeh22bwYftv6DzSFkln6DnXM0yWe%0ASX0w5t2HoNKPvRspdKo%3D%0A)

2. Taux / Codes de TVA d'achat

Associez chaque taux ou code de TVA utilisé sur vos factures fournisseurs Sellsy au code correspondant dans Tiime.

Cette étape garantit une comptabilisation correcte de la TVA déductible lors de l'export des achats. Exemple :

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472461931/262466586b31e9635d9592ac6dee/Capture-2Bd-E2-80-99e-CC-81cran-2B2026-05-29-2Ba-CC-80-2B16_43_36.png?expires=1788635700&signature=dfccc9804044ef2b9b6e56547862aeaf2657b24eb7c8d6ffcfcf013763d5e01b&req=diQgFM14nIhcWPMW1HO4zdSyKxX3LCuYjuCQ1KGlL6DDl8woVwvrBMLhwSwh%0A5vGk1KLSMFAbR%2FwVwTY%3D%0A)

3. Codes TVA pour les arrondis

Certaines écritures peuvent engendrer des écarts d'arrondi de quelques centimes.

Vous devez indiquer le code de TVA à utiliser pour ces ajustements afin de garantir l'équilibre des écritures transmises dans Tiime. Exemple :

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472461933/fa2f0b0bbb594c4af7bc7041aaf2/Capture-2Bd-E2-80-99e-CC-81cran-2B2026-05-29-2Ba-CC-80-2B16_46_37.png?expires=1788635700&signature=f121dc66cb46d7420d990173a90efabf3f954a8f224f523089766bae0fd8e508&req=diQgFM14nIhcWvMW1HO4za2Vx3819Aog1obrY4WfC0fX%2F6gR1r1dJ8qkvbmE%0AZOibYOpDlpI3da8FgGE%3D%0A)

4. Journaux comptables

Associez les journaux Sellsy aux journaux comptables existants dans Tiime. Par exemple :

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472461934/658df2f7637c9fd308065111da0c/Capture-2Bd-E2-80-99e-CC-81cran-2B2026-05-29-2Ba-CC-80-2B16_47_07.png?expires=1788635700&signature=c4ee27940a961218d0ed91990cc4410d33a2d85cdb5a5bf153804c50ee9d459e&req=diQgFM14nIhcXfMW1HO4zQATtRgCfTIxe%2BzBZY%2BDSC%2BV36DXomuOp0ECemdg%0AHXw0f5YdogsuMEEpWQw%3D%0A)

Les journaux sélectionnés doivent avoir été préalablement autorisés lors du partage du dossier dans Tiime.

5. Comptes comptables

Associez les comptes comptables utilisés dans Sellsy aux comptes correspondants dans Tiime.

Ces correspondances permettent d'affecter correctement les écritures comptables lors de leur création.

Nous vous recommandons de vérifier la cohérence entre votre plan comptable Sellsy et votre plan comptable Tiime avant de valider le paramétrage.

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472461937/faf23124757aca69d838737bd278/Capture-2Bd-E2-80-99e-CC-81cran-2B2026-05-29-2Ba-CC-80-2B16_50_04.png?expires=1788635700&signature=d3a82442515cfc1fb079c58aef9c6fc8bcab2eca8c08ee1d17c0eb11d2bdfbe7&req=diQgFM14nIhcXvMW1HO4zaEule1ABlvfgHI0vqhLvexd8uvxWMCIhGjWK%2BR8%0A8KUnQOYUnErMheizCdA%3D%0A)

6. Rabais, remises et ristournes

Si vous utilisez des rabais, remises ou ristournes dans Sellsy, vous devez également définir les comptes comptables qui recevront ces montants dans Tiime en cliquant sur « **Oui** », puis sur « **Enregistrer** ».

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472461938/e60041269698bea7c9e214725eb3/Capture-2Bd-E2-80-99e-CC-81cran-2B2026-05-29-2Ba-CC-80-2B16_51_33.png?expires=1788635700&signature=dc70048c968b089e30cacbf1a02c0406781cdbf3bd7c9996195fb3f003625b57&req=diQgFM14nIhcUfMW1HO4zVNwLEFCW9O5cWyFZW7%2BuKy2c1Nf2nupwbKkl4Sp%0AIZA4MIuy%2F7J3qoLkUqM%3D%0A)

Autrement, cliquez sur « **Non** », puis sur « **Passer** ».

En cas de doute, rapprochez-vous de votre cabinet comptable ou de votre administrateur Tiime.
​

### 
👉  Étape 4 : Derniers ajustements techniques

Votre connexion est maintenant configurée.

Avant d'activer l'intégration, quelques paramètres complémentaires vous permettent d'adapter le fonctionnement de la synchronisation à votre organisation comptable.

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472461942/080212c41fe22ebdc888b3a8e9af/Capture-2Bd-E2-80-99e-CC-81cran-2B2026-05-29-2Ba-CC-80-2B16_54_13.png?expires=1788635700&signature=cd29f31afa64c47fffaba6c901454b14bd07d98292a4fde2b1bd6a30dc2e6682&req=diQgFM14nIhbW%2FMW1HO4zQ4xNm97aSGwayFju%2BOl3Q%2BeCn%2F9wv56AVZIQDiT%0AOAyMXsGZHfS07grutwI%3D%0A)

1. Date de début de synchronisation

Sélectionnez la date à partir de laquelle les factures/avoirs Sellsy devront être transmis à Tiime.

Chaque nuit, le connecteur synchronisera automatiquement les factures et avoirs :

- ayant une date égale ou postérieure à la date sélectionnée ;
- marqués comme devant être envoyées en comptabilité.

> **Bon à savoir :**  Si vous mettez en place l'intégration pour la première fois, choisissez une date cohérente avec votre période comptable afin d'éviter l'export de documents déjà traités dans Tiime.

2. Création des écritures en brouillon / attente

La création des écritures en brouillon via API n'est pas prise en charge par Tiime : le choix effectué sur cette étape n'aura aucun impact sur la synchronisation.

> **Bon à savoir :** L'absence de création d'écritures en brouillon/attente ne signifie pas qu'une écriture ne peut pas être modifiée post-import. Elle peut être modifiée à tout moment en comptabilité. L'écriture arrivera, par défaut, en « **traitée **», mais le statut peut être modifié en « **à traiter** » post-import automatique.

3. Synchroniser les documents sans justificatif

Choisissez si les factures ou avoirs ne disposant pas de pièce jointe doivent être transmis à Tiime.

- Oui : Les documents seront synchronisés même si aucun justificatif n'est associé.
- Non : Seuls les documents accompagnés d'un justificatif seront transmis.

> **Important :** Nous recommandons de désactiver cette option si votre cabinet comptable exige systématiquement la présence d'un justificatif pour chaque écriture.

4. Libellé des écritures

Définissez la manière dont les libellés des écritures comptables seront générés dans Tiime.

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

Les nouvelles factures et avoirs répondant aux critères définis seront transmis à Tiime avec leurs écritures comptables, leurs tiers et leurs pièces jointes associées.

> **Important : **Nous recommandons de vérifier attentivement les premiers documents transmis dans Tiime. Plus une anomalie est détectée tôt, plus elle est simple à corriger. Une fois les premiers contrôles validés et les éventuels ajustements effectués, l’intégration fonctionnera de manière autonome.

___________________________________________________________

## **Questions fréquentes**

L'intégration fonctionne uniquement de Sellsy vers Tiime.
Les factures et avoirs créés **[et comptabilisés](https://help.sellsy.com/fr/articles/5875018-comptabiliser-des-factures-d-achat-et-de-vente)** dans Sellsy, ainsi que les écritures comptables, les tiers et les pièces jointes associées, sont automatiquement transmis vers Tiime.
Les modifications réalisées directement dans Tiime ne sont pas automatiquement répercutées dans Sellsy.
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

Lorsqu'une écriture a déjà été créée dans Tiime, la correction doit généralement être réalisée directement dans Tiime.
Si l'erreur est liée au paramétrage du connecteur (code TVA, compte comptable, journal, etc.), nous recommandons également de corriger la configuration de l'intégration afin d'éviter que l'erreur ne se reproduise lors des synchronisations suivantes.
Dans la majorité des cas, les corrections d'écritures déjà intégrées sont réalisées dans Tiime.
​

Nous recommandons de vérifier attentivement les premières factures et avoirs transmis dans Tiime afin de confirmer que :
- Les comptes comptables sont corrects
- Les codes TVA sont correctement affectés
- Les journaux utilisés sont les bons
- Les tiers sont correctement créés ou rapprochés
- Les pièces jointes sont bien présentes
Plus une anomalie est détectée tôt, plus elle est simple à corriger.
Une fois les premiers contrôles validés et les éventuels ajustements effectués, l'intégration fonctionnera de manière autonome et vous n'aurez généralement plus à intervenir sur son paramétrage.
​

Lors de la synchronisation, le connecteur recherche automatiquement une correspondance existante dans Tiime à partir de plusieurs critères :
- Compte auxiliaire
- Numéro de TVA
- SIRET ou numéro d'entreprise
- Nom du tiers
Si aucune correspondance n'est trouvée, un nouveau client ou fournisseur est créé automatiquement dans Tiime.
​

Pour faciliter le suivi des écritures importées depuis Sellsy, nous recommandons de définir avec votre cabinet comptable :
- Des journaux dédiés aux flux Sellsy
- Une convention de libellés spécifique
- Une procédure de contrôle des imports
Cette organisation permet généralement d'identifier facilement les écritures provenant de l'intégration.
​

Les pièces jointes associées aux documents de vente et d'achat peuvent être transmises vers Tiime avec les écritures comptables.
​[Lors du paramétrage de l'intégration](#h_cf8b0d6b93), vous pouvez choisir de synchroniser tous les documents ou uniquement ceux disposant d'un justificatif.
​

Nous préconisons de faire intervenir votre expert-comptable pour la configuration de l'intégration. Assurez-vous qu'il dispose d'un [accès gratuit expert-comptable](https://help.sellsy.com/fr/articles/6652377-donner-un-acces-sellsy-a-mon-expert-comptable) avec un [profil d'administrateur](https://help.sellsy.com/fr/articles/5864112-profils-de-privileges).


La comptabilité analytique n'est pas prise en charge par cette intégration.


Nous vous conseillons de vous rapprocher de votre administrateur afin de vérifier la configuration de l'environnement Tiime.
​

Nous vous conseillons de vous rapprocher de votre administrateur afin de vérifier la configuration de l'environnement Tiime.
​

Nous vous conseillons de vous rapprocher de votre administrateur afin de vérifier la configuration de l'environnement Tiime.
​

 Veuillez vérifier que :
- La facture a bien été comptabilisée dans Sellsy. Les documents de vente et d'achat non comptabilisés ne sont pas synchronisés vers Tiime.
- L'exercice comptable concerné n'est pas clôturé dans Tiime.
- La devise de la facture est autorisée dans Tiime.
- Le pays du client ou du fournisseur est autorisé dans Tiime.
- Les différents paramètres de synchronisation (journal, TVA, dossier comptable, etc.) sont correctement configurés.
> **Bon à savoir :** Vous pouvez retrouver vos imports dans la section « Paramètres » puis « Intégration », sur la tuile Chift. 
> ​
> ![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472528022/f4a862f60b8e0108a669c8fb86b7/Capture+d%E2%80%99e%CC%81cran+2026-06-12+a%CC%80+12_56_24.png?expires=1788635700&signature=9bd7b9543f6ca2203587cbd26c2495ad924c877564704b3276cca5a9574d9e4a&req=diQgFMx8lYFdW%2FMW1HO4zaEB3NJ2F1vOdEqnElMjWxfqN2a7b6v5fMKEInc8%0AIC7n1cHcSiIkr2ZXIIM%3D%0A)
> Un point d’exclamation sur la tuile signifie que des données sont en attente de votre approbation.
Si après ces vérifications le problème persiste, contactez le support Sellsy via le chat en précisant la facture et/ou la période concernée.

___________________________________________________________

Autres articles associés

- [Gérer les profils de privilèges](https://help.sellsy.com/fr/articles/5864116-gerer-les-profils-de-privileges-de-mes-collaborateurs#h_108be3a993)
- [Activer la conformité](https://help.sellsy.com/fr/articles/6100605-activer-le-mode-conforme)
- [Comptabilisation des documents](https://help.sellsy.com/fr/articles/5875018-comptabiliser-une-facture-d-achat-de-vente)
- [Donner un accès Sellsy à mon expert-comptable](https://help.sellsy.com/fr/articles/6652377-donner-un-acces-sellsy-a-mon-expert-comptable)
- [Ajouter un taux de TVA](https://help.sellsy.com/fr/articles/5871870-ajouter-un-taux-de-tva)

Mis a jour le : 12/06/2026
