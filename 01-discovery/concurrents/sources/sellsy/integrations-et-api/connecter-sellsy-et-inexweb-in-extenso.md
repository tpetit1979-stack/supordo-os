---
source: https://help.sellsy.com/fr/articles/15480642-connecter-sellsy-et-inexweb-in-extenso
categorie: Intégrations et API
titre: Connecter Sellsy et InexWeb (In Extenso)
date_recuperation: 2026-09-05
---

# Connecter Sellsy et InexWeb (In Extenso)

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472687095/c2068948375f4d8c74b3a4e7528b/FAQ-Bannie-CC-80reAcademy-2-2B-282-29.png?expires=1788635700&signature=ba710fae4180ff6949045a7bc9c90e102ff1022041abd4cc8ba7cc3f3e4a97ed&req=diQgFM92moFWXPMW1HO4zdt%2Fv5JK83aOxRIXJz208iZRbjtQ8qyBshUGJIJ1%0AuzEUCW4O8cC26oFvpLo%3D%0A)

## Introduction

Bienvenue dans le [guide d'activation de connexion Sellsy x InexWeb](#h_365639ff8f). Pour rappel, la connexion InexWeb est incluse dans votre licence Sellsy Facturation, aucun coût additionnel n'est associé à son usage. Elle permet de :

- Synchroniser automatiquement les avoirs et factures de vente depuis Sellsy vers InexWeb
- Synchroniser automatiquement les avoirs et factures d'achat depuis Sellsy vers InexWeb
- Transmettre les pièces jointes PDF associées aux factures
- Synchroniser les clients et fournisseurs (tiers)
- Créer automatiquement les comptes de tiers dans InexWeb lorsque nécessaire

> **Bon à savoir :** La synchronisation vers InexWeb - In Extenso ne concerne que les documents [comptabilisés dans Sellsy](https://help.sellsy.com/fr/articles/5875018-comptabiliser-des-factures-d-achat-et-de-vente). Si un document n'a pas encore été comptabilisé, il ne sera pas transmis à InexWeb lors des synchronisations automatiques.

### 
Données synchronisées

| Donnée | Pris en charge |
| --- | --- |
| Écritures de vente | ✅ |
| Pièces jointes de vente | ✅ |
| Écritures d'achat | ✅ |
| Pièces jointes d'achat | ✅ |
| Synchronisation / création des comptes tiers | ✅ |

> **Important :** Cette intégration fonctionne dans un seul sens. Les données sont transmises de Sellsy à InexWeb. Les modifications réalisées directement dans InexWeb - In Extenso ne sont pas automatiquement répercutées dans Sellsy.

___________________________________________________________

## Guide d'activation de connexion Sellsy x InexWeb

### 
⚠️ Avant de commencer

Avant de configurer la connexion entre Sellsy et InexWeb - In Extenso, assurez-vous de disposer des accès nécessaires et de remplir les prérequis techniques.

> **Important :** Nous recommandons que l’activation de cette intégration soit réalisée par votre expert-comptable. 
> Les licences des cabinets comptables disposent par défaut d’un accès API, ce qui n'est souvent pas le cas sur les licences d'une entreprise chez un outil comptable tel qu’InexWeb. De plus, les étapes de paramétrage comptable seront mieux maîtrisées si elles sont effectuées par votre cabinet.
> Avant de transmettre cette page à votre expert-comptable, assurez-vous d’avoir réalisé les étapes préalables dans votre compte Sellsy, [décrites ci-dessous](https://help.sellsy.com/fr/articles/15479499-connecter-sellsy-et-tiime#h_6cf220cff6).
> N’effectuez vous-même cette activation que si votre comptabilité est internalisée. Dans ce cas, assurez-vous que votre licence ou votre niveau de plan inclut un accès API.

Côté Sellsy

- Une licence Sellsy Facturation active ;
- Des [factures/avoirs comptabilisés](https://help.sellsy.com/fr/articles/5875018-comptabiliser-des-factures-d-achat-et-de-vente) (si un document n'a pas encore été comptabilisé, il ne sera pas transmis à InexWeb - InExtenso lors des synchronisations automatiques) ;
- La [conformité stricte active](https://help.sellsy.com/fr/articles/6100605-activer-le-mode-conforme-pour-les-documents-de-vente) sur le compte Sellsy ;
- Les droits nécessaires pour accéder aux intégrations comptables :
- **Vous êtes client Sellsy, votre comptabilité est internalisée et gérée chez** **InexWeb - InExtenso :** Vous devez disposer d'un profil administrateur ou d'un profil ayant accès aux paramètres d'intégration. Si vous ne disposez pas des droits nécessaires, contactez un administrateur de votre compte Sellsy. Pour en savoir plus sur les profils et privilèges Sellsy, consultez [cet article](https://help.sellsy.com/fr/articles/5864112-profils-de-privileges).
- **Vous êtes expert-comptable d'un client Sellsy :** Avant de poursuivre la configuration, assurez-vous que votre client vous a accordé un accès expert-comptable associé à un [profil administrateur](https://help.sellsy.com/fr/articles/5864112-profils-de-privileges). L'accès Expert-Comptable est gratuit et permet d'accéder aux données nécessaires à la synchronisation comptable. Si vous ne disposez pas encore d'un accès expert-comptable, votre client devra suivre la procédure décrite [dans cet article](https://help.sellsy.com/fr/articles/6652377-donner-un-acces-sellsy-a-mon-expert-comptable).

### 
Côté InexWeb - In Extenso

L’application Chift/Sellsy doit être activée sur le compte du cabinet de votre expert-comptable. Avant d’activer la connexion, veuillez vérifier que cette activation a bien été effectuée.
​

Si ce n’est pas encore le cas, ou si vous n'êtes pas certain(e), contactez le support InexWeb - In Extenso à l’adresse [assistance@fulll.help](mailto:assistance@fulll.help) afin de demander l’activation de l’application sur le compte du cabinet de votre expert-comptable.

Il faudra vous authentifier sur votre compte InexWeb pour activer l'intégration. Assurez-vous de disposer de l'identifiant et du mot de passe de votre compte InexWeb.


​

### 👉  Étape 1 : Connecter InexWeb dans Sellsy

Depuis la [page marketplace Sellsy à propos de l’intégration InexWeb](https://go.sellsy.com/applications/in-extenso) cliquez sur : « **Activer l’intégration** ».

Ou bien cliquez directement sur [ce lien](https://marketplaces.chift.app/fr/sellsy/apps/8022). Vous serez redirigé vers l'interface sécurisée Chift.
​

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472717236/5b35e8eeefcd7b5e6e4ec0b14162/Capture+d%E2%80%99e%CC%81cran+2026-06-12+a%CC%80+14_51_34.png?expires=1788635700&signature=3faa13e0755c770fb215b521125d70997ea7c1534566cc0c7788b9b39d417936&req=diQgFM5%2FmoNcX%2FMW1HO4zYB8W0HtFPw9HYeFEgY6v7HAi6W62f3%2B9Odf9ksX%0A3MbWhXFxY%2FT1KDAtTF0%3D%0A)

### 
👉  Étape 2 : Authentifier la connexion

Dans l’interface Chift, cliquez sur « **Activer l’intégration** ». Si c’est votre première connexion pour ce compte, cliquez sur « **En créer une nouvelle** ».

Si une connexion a déjà été créée pour ce compte, sélectionnez simplement le compte correspondant dans le menu déroulant, puis cliquez sur « **Valider** ».

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472687792/e2426b66932729e2671e4d95efa2/Capture-2Bd-E2-80-99e-CC-81cran-2B2026-05-29-2Ba-CC-80-2B15_55_08.png?expires=1788635700&signature=122188302fede6c061b3afbb1021f8d04727ce21e7ea531766de72793f89dd17&req=diQgFM92moZWW%2FMW1HO4zbb8UTe5IEAk4nD47sAcTJkG%2FKxMicSsJGSGTstV%0A9BEXlRgs2yb8YoWeTuU%3D%0A)

Pour créer une nouvelle connexion, munissez-vous du nom et du numéro SIRET de l’entreprise utilisant Sellsy. Renseignez ces informations, puis cliquez sur « **Enregistrer** ».

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472687793/743c2cbefb8f3c6c925aed732b8e/Capture-2Bd-E2-80-99e-CC-81cran-2B2026-05-29-2Ba-CC-80-2B15_58_07.png?expires=1788635700&signature=a513b9028233d34cb22888064faadbd215e2bf885a26f764266af2d6cc6b2c28&req=diQgFM92moZWWvMW1HO4zZSys8ujLQJ5nY3XbuMmFSukDDDlmISYi2d%2BrnDg%0AIYCYYz6%2BeJXw3tFWUQo%3D%0A)

Une fois ces étapes complétées, vous allez vous retrouver sur un écran comme celui-ci :

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472719904/1481364e3a7535b96fa217204741/Capture+d%E2%80%99e%CC%81cran+2026-06-12+a%CC%80+14_52_34.png?expires=1788635700&signature=285376b8ac2796b01c9f6d221d6515926c57b4bfe2b333c076762e1e29b20ada&req=diQgFM5%2FlIhfXfMW1HO4zXsKe2VKqGkRk2HoD2vaFPeQqNG0C%2FYkw8pOd7pv%0AL5QmKhmL%2B8BLRCfg2y4%3D%0A)

En cliquant sur « **Connecter** », vous serez redirigé vers l’écran de connexion Sellsy.

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472687798/ebd7d0b996309ebb0ed14e860298/Capture-2Bd-E2-80-99e-CC-81cran-2B2026-05-29-2Ba-CC-80-2B16_00_46.png?expires=1788635700&signature=d4cd8f270246bf852e8dbde1717e86b45eddd9971515878d789542b10095fd50&req=diQgFM92moZWUfMW1HO4zcHtSXZcKy74kS9G3w70ESU9cB8H3BnMa12KjNa8%0ANG%2FvowlZeI1Hz4oSBqo%3D%0A)

Il vous suffit de renseigner vos identifiants Sellsy. Si plusieurs comptes sont associés à ces identifiants, sélectionnez le compte concerné dans le menu déroulant.

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472687810/04d220998ca6d3c90b953d5e1e15/Capture-2Bd-E2-80-99e-CC-81cran-2B2026-05-29-2Ba-CC-80-2B16_01_26-2B-1-.png?expires=1788635700&signature=efd39da98c0eb7bafff4a56229628abaf28373dfe27bc66ed32fed436e730d3e&req=diQgFM92moleWfMW1HO4zVx7OrRT2AnpUKvivnZMf%2FsdS%2BEX61nzzZrbTjfS%0AExahqeU5aus0OaCyXTo%3D%0A)

Puis, autoriser la connexion via Chift en cliquant sur « **Autoriser** ».

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472687811/2f0f512cc48cee88120e9f03ae54/Capture-2Bd-E2-80-99e-CC-81cran-2B2026-05-29-2Ba-CC-80-2B16_01_36.png?expires=1788635700&signature=12f12e7dd72174a7e972eb722829b80ce8f966a25e66f082acdadfc09f17bd21&req=diQgFM92moleWPMW1HO4zTPiW%2FpyWIKAQqc6dlJm3VIW1vjwLSYS0NObx2nE%0ADZTM1TPNBgY4b5DOmxE%3D%0A)

Vous serez ensuite redirigé vers la seconde étape d’authentification, qui vous permettra de vous connecter à votre environnement InexWeb.

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472722386/741b6ef38186432f5b32fccc4e62/Capture+d%E2%80%99e%CC%81cran+2026-06-12+a%CC%80+14_53_57.png?expires=1788635700&signature=26349540ed4a192d26abcbf430d2e839aae2cb772fe4191fc238ab9a832aef03&req=diQgFM58n4JXX%2FMW1HO4zcMeA26AEYmZJodtQIAolyc6hoKV1FXoocZLXxIp%0AreSkCJzUrq2t2lg52KQ%3D%0A)

Si vous n'êtes pas encore connecté(e) à votre compte InexWeb, vous allez être rédirigé(e) vers une page de connexion. Alternativement, vous pouvez effectuer cette démarche dans un onglet à part. Une fois connecté(e), il suffit de cliquer sur « **Autoriser** ».
​

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472724058/e07266a9cf56716f7270d6ec580d/Capture+d%E2%80%99e%CC%81cran+2026-06-12+a%CC%80+14_54_42.png?expires=1788635700&signature=0c449ea1ab8737f925b242ee750b657dc8e270bc1805d4317f92765fee5479e7&req=diQgFM58mYFaUfMW1HO4zd5xb1pQg8XvNOvQTcT2mvjUXoCBL4UxQW5gsI9D%0AdnYNrhyJ1n45qITBjuY%3D%0A)


Depuis le menu déroulant, vous devez choisir le compte comptable à utiliser et cliquer ensuite sur « **Valider** ».
​
En dernière étape, vous devez choisir la typologie des documents à synchroniser (ventes, achats ou les deux).
​

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472687816/38ffa70efeaf92ee3ee000c6da5d/Capture-2Bd-E2-80-99e-CC-81cran-2B2026-06-12-2Ba-CC-80-2B12_38_34.png?expires=1788635700&signature=22e5bbe1588833b8a6622324069ef4e0944adf15ed63f81c6314cc5fb7289732&req=diQgFM92moleX%2FMW1HO4zUghyzezFPAQpGLDXmIVUoeWgNB8Ckot7TIK2T9I%0ACkXv6kk%2B%2Bdp981jYbnw%3D%0A)


Une fois la sélection effectuée, vous pouvez déterminer les paramètres de connexion entre Sellsy et InexWeb - InExtenso.


​

### 
👉  Étape 3 : Déterminer les paramètres de connexion

Une fois l'authentification terminée, vous devez configurer les correspondances comptables entre Sellsy et InexWeb - InExtenso.

Cette étape permet au connecteur de savoir comment traduire les données présentes dans Sellsy vers les bons éléments comptables dans InexWeb - InExtenso.

Pour rappel, l'intégration permet de récupérer les documents de vente et/ou d'achat présents dans Sellsy et de les transmettre automatiquement à InexWeb, accompagnés de leurs pièces jointes.

Vous devrez compléter les correspondances pour les éléments suivants :

- Taux / codes de TVA de vente
- Taux / codes de TVA d'achat
- Codes de TVA utilisés pour les arrondis
- Journaux comptables
- Comptes comptables
- Comptes de rabais, remises et ristournes

1. Taux / Codes de TVA de vente

Associez chaque taux ou code de TVA utilisé dans Sellsy au code de TVA correspondant dans InexWeb - InExtenso.

Cette correspondance permet au connecteur d'affecter correctement les montants de TVA sur les écritures de vente exportées. Exemple :

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472687815/dfac1287d1501f0a07761179d760/Capture-2Bd-E2-80-99e-CC-81cran-2B2026-05-29-2Ba-CC-80-2B16_43_36.png?expires=1788635700&signature=1e107474c8cbb2f866481b0c74a6a9b4d2641bacd08d746155b77aa3fed7e967&req=diQgFM92moleXPMW1HO4zbvROt1y0Ecbn4U4x5bwSs%2FD8rMu%2FyP9wBVoMyxz%0AzR8%2FvXKhKcqaYhAyDu8%3D%0A)

2. Taux / Codes de TVA d'achat

Associez chaque taux ou code de TVA utilisé sur vos factures fournisseurs Sellsy au code correspondant dans InexWeb - InExtenso.

Cette étape garantit une comptabilisation correcte de la TVA déductible lors de l'export des achats. Exemple :

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472687820/430224a6b9b724d4474dc7b36a08/Capture-2Bd-E2-80-99e-CC-81cran-2B2026-05-29-2Ba-CC-80-2B16_43_36.png?expires=1788635700&signature=e085c2966e7b55c8422a3915ea6b3c2c9a4a44aca94e8862256e178ba82367ec&req=diQgFM92moldWfMW1HO4zex3ObOwmgJTSE4SEp4thFlhotf3mANM6H2RbNAF%0AGjTs%2F%2F8FvBhcyJvI3%2BQ%3D%0A)

3. Codes TVA pour les arrondis

Certaines écritures peuvent engendrer des écarts d'arrondi de quelques centimes.

Vous devez indiquer le code de TVA à utiliser pour ces ajustements afin de garantir l'équilibre des écritures transmises dans InexWeb - InExtenso. Exemple :

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472687821/f4b37899df9af1a71194361050fd/Capture-2Bd-E2-80-99e-CC-81cran-2B2026-05-29-2Ba-CC-80-2B16_46_37.png?expires=1788635700&signature=fad9dcc8525e8a50399b87c816d576efe1fd10ad6ab2f49492f0951e8d2ad902&req=diQgFM92moldWPMW1HO4zXO3mG1rz3gBM9dLp8dp4zDuEj8x3fnldV1iFxBA%0Abg3xk%2BppwWMDHn7gm0s%3D%0A)

4. Journaux comptables

Associez les journaux Sellsy aux journaux comptables existants dans InexWeb - InExtenso. Par exemple :

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472687828/40ca24048b2cf824e3dad8926d9b/Capture-2Bd-E2-80-99e-CC-81cran-2B2026-05-29-2Ba-CC-80-2B16_47_07.png?expires=1788635700&signature=4413a065bbd631da2d01bad1be5fe4c8a4c5df95c5dd7be062ff56339f09ecbb&req=diQgFM92moldUfMW1HO4zcfJXhCyHX%2Bol2Hm0gDyC75EjSalRgbC%2BkQXa5Nl%0AjnTJ3FwUWyVxeIrkhug%3D%0A)

Les journaux sélectionnés doivent avoir été préalablement autorisés lors du partage du dossier dans InexWeb - InExtenso.

5. Comptes comptables

Associez les comptes comptables utilisés dans Sellsy aux comptes correspondants dans InexWeb - InExtenso.

Ces correspondances permettent d'affecter correctement les écritures comptables lors de leur création.

Nous vous recommandons de vérifier la cohérence entre votre plan comptable Sellsy et votre plan comptable InexWeb avant de valider le paramétrage.

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472687827/5391420ba1f31e8e7ec241a678a7/Capture-2Bd-E2-80-99e-CC-81cran-2B2026-05-29-2Ba-CC-80-2B16_50_04.png?expires=1788635700&signature=0c298255de4ad675facf53687c34093b21b724d109e1657e32b8a7028145292d&req=diQgFM92moldXvMW1HO4zREbTxAr7a1kqOHUxyALy%2FhQZhGQq8%2B7DwSxF8uH%0AW8BcSV%2BLj5pjMZ4P4B8%3D%0A)

6. Rabais, remises et ristournes

Si vous utilisez des rabais, remises ou ristournes dans Sellsy, vous devez également définir les comptes comptables qui recevront ces montants dans InexWeb en cliquant sur « **Oui** », puis sur « **Enregistrer** ».

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472687826/e1fd367d02572c8a0cf0f9fbd2ed/Capture-2Bd-E2-80-99e-CC-81cran-2B2026-05-29-2Ba-CC-80-2B16_51_33.png?expires=1788635700&signature=de2621522015cb8152e117a7d022e68ebc6f00b087aea760a3de5db0a9607791&req=diQgFM92moldX%2FMW1HO4zXyxGXXm4MoP63nUnU%2BCoh0J14zQSGGsQiUpCO%2FQ%0A9aTqLJ8CrcCJseYh7h8%3D%0A)

Autrement, cliquez sur « **Non** », puis sur « **Passer** ».

En cas de doute, rapprochez-vous de votre cabinet comptable ou de votre administrateur InexWeb - InExtenso.
​

### 
👉  Étape 4 : Derniers ajustements techniques

Votre connexion est maintenant configurée.

Avant d'activer l'intégration, quelques paramètres complémentaires vous permettent d'adapter le fonctionnement de la synchronisation à votre organisation comptable.

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472687824/c7bb35ac57aeffcb5b3224bef0a2/Capture-2Bd-E2-80-99e-CC-81cran-2B2026-05-29-2Ba-CC-80-2B16_54_13.png?expires=1788635700&signature=c48f1a7ce214a5c08585a16c675dbbecd16b1976536c5f9c4e5d9bc9f64decc2&req=diQgFM92moldXfMW1HO4zUn2kQX8bKOna5ikltBBlgvzQXKYBsIFCYWP6Rfq%0A9TfzmQQb09cRaM01BF8%3D%0A)

1. Date de début de synchronisation

Sélectionnez la date à partir de laquelle les factures/avoirs Sellsy devront être transmis à InexWeb - InExtenso.

Chaque nuit, le connecteur synchronisera automatiquement les factures et avoirs :

- ayant une date égale ou postérieure à la date sélectionnée ;
- marqués comme devant être envoyées en comptabilité.

> **Bon à savoir :**  Si vous mettez en place l'intégration pour la première fois, choisissez une date cohérente avec votre période comptable afin d'éviter l'export de documents déjà traités dans InexWeb - InExtenso.

2. Création des écritures en brouillon / attente

La création des écritures en brouillon via API n'est pas prise en charge par InexWeb : le choix effectué sur cette étape n'aura aucun impact sur la synchronisation.

> **Bon à savoir :** L'absence de création d'écritures en brouillon/attente ne signifie pas qu'une écriture ne peut pas être modifiée post-import. Elle peut être modifiée à tout moment en comptabilité. L'écriture arrivera, par défaut, en « **traitée **», mais le statut peut être modifié en « **à traiter** » post-import automatique.

3. Synchroniser les documents sans justificatif

Choisissez si les factures ou avoirs ne disposant pas de pièce jointe doivent être transmis à InexWeb - InExtenso.

- Oui : Les documents seront synchronisés même si aucun justificatif n'est associé.
- Non : Seuls les documents accompagnés d'un justificatif seront transmis.

> **Important :** Nous recommandons de désactiver cette option si votre cabinet comptable exige systématiquement la présence d'un justificatif pour chaque écriture.

4. Libellé des écritures

Définissez la manière dont les libellés des écritures comptables seront générés dans InexWeb - InExtenso.

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

Les nouvelles factures et avoirs répondant aux critères définis seront transmis à InexWeb avec leurs écritures comptables, leurs tiers et leurs pièces jointes associées.

> **Important : **Nous recommandons de vérifier attentivement les premiers documents transmis dans InexWeb - InExtenso. Plus une anomalie est détectée tôt, plus elle est simple à corriger. Une fois les premiers contrôles validés et les éventuels ajustements effectués, l’intégration fonctionnera de manière autonome.

___________________________________________________________

## **Questions fréquentes**

L'intégration fonctionne uniquement de Sellsy vers InexWeb - InExtenso.
Les factures et avoirs créés **[et comptabilisés](https://help.sellsy.com/fr/articles/5875018-comptabiliser-des-factures-d-achat-et-de-vente)** dans Sellsy, ainsi que les écritures comptables, les tiers et les pièces jointes associées, sont automatiquement transmis vers InexWeb - InExtenso.
Les modifications réalisées directement dans InexWeb ne sont pas automatiquement répercutées dans Sellsy.
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

Lorsqu'une écriture a déjà été créée dans InexWeb, la correction doit généralement être réalisée directement dans InexWeb - InExtenso.
Si l'erreur est liée au paramétrage du connecteur (code TVA, compte comptable, journal, etc.), nous recommandons également de corriger la configuration de l'intégration afin d'éviter que l'erreur ne se reproduise lors des synchronisations suivantes.
Dans la majorité des cas, les corrections d'écritures déjà intégrées sont réalisées dans InexWeb - InExtenso.
​

Nous recommandons de vérifier attentivement les premières factures et avoirs transmis dans InexWeb afin de confirmer que :
- Les comptes comptables sont corrects
- Les codes TVA sont correctement affectés
- Les journaux utilisés sont les bons
- Les tiers sont correctement créés ou rapprochés
- Les pièces jointes sont bien présentes
Plus une anomalie est détectée tôt, plus elle est simple à corriger.
Une fois les premiers contrôles validés et les éventuels ajustements effectués, l'intégration fonctionnera de manière autonome et vous n'aurez généralement plus à intervenir sur son paramétrage.
​

Lors de la synchronisation, le connecteur recherche automatiquement une correspondance existante dans InexWeb à partir de plusieurs critères :
- Compte auxiliaire
- Numéro de TVA
- SIRET ou numéro d'entreprise
- Nom du tiers
Si aucune correspondance n'est trouvée, un nouveau client ou fournisseur est créé automatiquement dans InexWeb - InExtenso.
​

Pour faciliter le suivi des écritures importées depuis Sellsy, nous recommandons de définir avec votre cabinet comptable :
- Des journaux dédiés aux flux Sellsy
- Une convention de libellés spécifique
- Une procédure de contrôle des imports
Cette organisation permet généralement d'identifier facilement les écritures provenant de l'intégration.
​

Les pièces jointes associées aux documents de vente et d'achat peuvent être transmises vers InexWeb avec les écritures comptables.
​[Lors du paramétrage de l'intégration](#h_095cd57771), vous pouvez choisir de synchroniser tous les documents ou uniquement ceux disposant d'un justificatif.
​

Nous préconisons de faire intervenir votre expert-comptable pour la configuration de l'intégration. Assurez-vous qu'il dispose d'un [accès gratuit expert-comptable](https://help.sellsy.com/fr/articles/6652377-donner-un-acces-sellsy-a-mon-expert-comptable) avec un [profil d'administrateur](https://help.sellsy.com/fr/articles/5864112-profils-de-privileges).


La comptabilité analytique n'est pas prise en charge par cette intégration.


Nous vous conseillons de vous rapprocher de votre administrateur afin de vérifier la configuration de l'environnement InexWeb - InExtenso.
​

Nous vous conseillons de vous rapprocher de votre administrateur afin de vérifier la configuration de l'environnement InexWeb - InExtenso.
​

Nous vous conseillons de vous rapprocher de votre administrateur afin de vérifier la configuration de l'environnement InexWeb - InExtenso.
​

 Veuillez vérifier que :
- La facture a bien été comptabilisée dans Sellsy. Les documents de vente et d'achat non comptabilisés ne sont pas synchronisés vers InexWeb - InExtenso.
- L'exercice comptable concerné n'est pas clôturé dans InexWeb - InExtenso.
- La devise de la facture est autorisée dans InexWeb - InExtenso.
- Le pays du client ou du fournisseur est autorisé dans InexWeb - InExtenso.
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
