---
source: https://help.sellsy.com/fr/articles/15457201-connecter-sellsy-et-acd
categorie: Intégrations et API
titre: Connecter Sellsy et ACD
date_recuperation: 2026-09-05
---

# Connecter Sellsy et ACD

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2469756149/0a5a14704e70016af68c9a47ce7c/FAQ-Bannie-CC-80reAcademy-2%2B-282-29.png?expires=1788635700&signature=acdf4ec56804ab8e4c1b5da0aedb4617427da632bae948bc4b0181789262efa1&req=diQhH857m4BbUPMW1HO4zeTPoA6VOHpbXlC48Na53ppZ6AISA8uqMqncujm3%0AyW8ZbzeGx7qX0B%2FX7Hs%3D%0A)

### 

## 
​Introduction

Bienvenue dans le [guide d'activation de connexion Sellsy x ACD](#h_8a6abb4e2d). Pour rappel, la connexion ACD est incluse dans votre licence Sellsy Facturation, aucun coût additionnel n'est associé à son usage. Elle permet de :

- Synchroniser automatiquement les avoirs et factures de vente depuis Sellsy vers ACD
- Synchroniser automatiquement les avoirs et factures d'achat depuis Sellsy vers ACD
- Transmettre les pièces jointes PDF associées aux factures
- Synchroniser les clients et fournisseurs (tiers)
- Créer automatiquement les comptes de tiers dans ACD lorsque nécessaire

> **Bon à savoir :** La synchronisation vers ACD ne concerne que les documents [comptabilisés dans Sellsy](https://help.sellsy.com/fr/articles/5875018-comptabiliser-des-factures-d-achat-et-de-vente). Si un document n'a pas encore été comptabilisé, il ne sera pas transmis à ACD lors des synchronisations automatiques.


Données synchronisées

| Donnée | Pris en charge |
| --- | --- |
| Écritures de vente | ✅ |
| Pièces jointes de vente | ✅ |
| Écritures d'achat | ✅ |
| Pièces jointes d'achat | ✅ |
| Synchronisation / création des comptes tiers | ✅ |

> **Important :** Cette intégration fonctionne dans un seul sens. Les données sont transmises de Sellsy à ACD. Les modifications réalisées directement dans ACD ne sont pas automatiquement répercutées dans Sellsy.

___________________________________________________________

## Guide d'activation de connexion Sellsy x ACD

### 
⚠️ Avant de commencer

Avant de configurer la connexion entre Sellsy et ACD, assurez-vous de disposer des accès nécessaires et de remplir les prérequis techniques.

> **Important :** Nous recommandons que l’activation de cette intégration soit réalisée par votre expert-comptable. 
> Les licences des cabinets comptables disposent par défaut d’un accès API, ce qui n'est souvent pas le cas sur les licences d'une entreprise chez un outil comptable tel qu'ACD. De plus, les étapes de paramétrage comptable seront mieux maîtrisées si elles sont effectuées par votre cabinet.
> Avant de transmettre cette page à votre expert-comptable, assurez-vous d’avoir réalisé les étapes préalables dans votre compte Sellsy, [décrites ci-dessous](#h_c3541fbb89).
> N’effectuez vous-même cette activation que si votre comptabilité est internalisée. Dans ce cas, assurez-vous que votre licence ou votre niveau de plan inclut un accès API.


Côté Sellsy

- Une licence Sellsy Facturation active ;
- Des [factures/avoirs comptabilisés ](https://help.sellsy.com/fr/articles/5875018-comptabiliser-des-factures-d-achat-et-de-vente)(si un document n'a pas encore été comptabilisé, il ne sera pas transmis à ACD lors des synchronisations automatiques) ;
- La [conformité stricte active](https://help.sellsy.com/fr/articles/6100605-activer-le-mode-conforme-pour-les-documents-de-vente) sur le compte Sellsy ;
- Les droits nécessaires pour accéder aux intégrations comptables :
- **Vous êtes client Sellsy, votre comptabilité est internalisée et gérée chez ACD :** Vous devez disposer d'un profil administrateur ou d'un profil ayant accès aux paramètres d'intégration. Si vous ne disposez pas des droits nécessaires, contactez un administrateur de votre compte Sellsy. Pour en savoir plus sur les profils et privilèges Sellsy, consultez [cet article](https://help.sellsy.com/fr/articles/5864112-profils-de-privileges).
- **Vous êtes expert-comptable d'un client Sellsy :** Avant de poursuivre la configuration, assurez-vous que votre client vous a accordé un accès expert-comptable associé à un [profil administrateur](https://help.sellsy.com/fr/articles/5864112-profils-de-privileges). L'accès Expert-Comptable est gratuit et permet d'accéder aux données nécessaires à la synchronisation comptable. Si vous ne disposez pas encore d'un accès expert-comptable, votre client devra suivre la procédure décrite [dans cet article](https://help.sellsy.com/fr/articles/6652377-donner-un-acces-sellsy-a-mon-expert-comptable).

Côté ACD

Avant de procéder au paramétrage de l’accès aux API ACD, les prérequis suivants doivent être respectés :

- Disposer d’**i-Suite Expert** ;
- La **Suite Expert** doit être à jour de sa dernière version ;
- Les **services webs** doivent être installés et être à jour de leur dernière version.

ACD recommande d’activer la sécurisation des comptes API afin d’isoler les accès techniques des comptes collaborateurs du cabinet et de faciliter la gestion des habilitations.


Pour consulter le détail des prérequis techniques, des modalités de configuration et des bonnes pratiques de sécurité, [rendez-vous sur le Centre d’aide ACD](https://assistance.suiteexpert.fr/hc/fr/articles/21175075290258-Utilisation-des-API-Suite-Expert). Vous y trouverez notamment les informations permettant de :

- récupérer l’URL de connexion aux API ;
- créer et sécuriser un compte API dédié ;
- partager un dossier sur i-Suite ;
- configurer les droits nécessaires à l’utilisation des API ;
- comprendre les bonnes pratiques de mise en œuvre et de sécurité.

### 👉  Étape 1 : Connecter ACD dans Sellsy

Depuis la [page marketplace Sellsy à propos de l’intégration ACD](https://go.sellsy.com/applications/acd), cliquez sur : « **Activer l’intégration** ».

Ou bien cliquez directement sur [ce lien](https://marketplaces.chift.app/fr/sellsy/apps/8003). Vous serez redirigé vers l'interface sécurisée Chift.
​

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2469692280/7ca2b0bd20a962bb408fc1cdf623/Capture+d%E2%80%99e%CC%81cran+2026-06-01+a%CC%80+09_15_33.png?expires=1788635700&signature=d5476ef8a8b95decdba3e2221c8fd05ae4234d13ef8b0036c70bffa354c4d0d6&req=diQhH893n4NXWfMW1HO4zQmXFv4C1r8tmGNztyBvV%2FHBHt0pjVGXjAs1Xbgi%0A62lvkV5IbttvXi8DTYU%3D%0A)

### 
👉  Étape 2 : Authentifier la connexion

Dans l’interface Chift, cliquez sur « **Activer l’intégration** ». Si c’est votre première connexion pour ce compte, cliquez sur « **En créer une nouvelle** ».

Si une connexion a déjà été créée pour ce compte, sélectionnez simplement le compte correspondant dans le menu déroulant, puis cliquez sur « **Valider** ».

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2469695964/d754c4e6334e232ae0887a123b20/Capture+d%E2%80%99e%CC%81cran+2026-05-29+a%CC%80+15_55_08.png?expires=1788635700&signature=ba9ea4e1cf4d3a00ca5b7585641fbea35a586ff5fc77d6bb93dc5be997ebb85f&req=diQhH893mIhZXfMW1HO4zRzRnwKRniyQyZVs7eSABLgTp5%2FNKkd9o52S6B6P%0AOLKIvA0%2Fvnxbaj0YGeU%3D%0A)

Pour créer une nouvelle connexion, munissez-vous du nom et du numéro SIRET de l’entreprise utilisant Sellsy. Renseignez ces informations, puis cliquez sur « **Enregistrer** ».

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2469700164/378cbd4ae52ea7e2e6656c542536/Capture+d%E2%80%99e%CC%81cran+2026-05-29+a%CC%80+15_58_07.png?expires=1788635700&signature=a1460b47128d988344f7901ee66b323a048bcf8a704c3dabf4642fbc5d392793&req=diQhH85%2BnYBZXfMW1HO4zWB%2FlKTmusqJ3gmEBfafw2yHYrvxqCpQgUUT9KoI%0ARr2CEftdR2dHVq3e6c8%3D%0A)

Une fois ces étapes complétées, vous allez vous retrouver sur un écran comme celui-ci :

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2469706897/8a4890b2e8708401062c94efbe2f/Capture+d%E2%80%99e%CC%81cran+2026-05-29+a%CC%80+16_00_08.png?expires=1788635700&signature=c86b941a9dbfca6baa8e270c51e4adfdadaf9c4a9212ec439a569c7780e7d7fc&req=diQhH85%2Bm4lWXvMW1HO4zQ2rDBkUZKfdSaV0e76myikSGU%2Fsyf9IkXYhqUSa%0A%2FR0aT6tSD0495jAS3PU%3D%0A)

En cliquant sur « **Connecter** », vous serez redirigé vers l’écran de connexion Sellsy.

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2469707914/e829cec057123ae974f5d10f6105/Capture+d%E2%80%99e%CC%81cran+2026-05-29+a%CC%80+16_00_46.png?expires=1788635700&signature=223a85e067410c8281e70f992b1c747910ce35948d95c13bc5ca0fcc455d7c15&req=diQhH85%2BmoheXfMW1HO4zZkJZAOvHHw7Lde9eN3bH6MBs4IZKEsEOob9G8b5%0ACkvs2bBo%2FzSOkauJTz8%3D%0A)

Il vous suffit de renseigner vos identifiants Sellsy. Si plusieurs comptes sont associés à ces identifiants, sélectionnez le compte concerné dans le menu déroulant.

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2469709135/4783941bfcdefd64a3a844d6776a/Capture+d%E2%80%99e%CC%81cran+2026-05-29+a%CC%80+16_01_26+-1-.png?expires=1788635700&signature=e2c81a56738d46aff731ba1a9d962b65ccc65fdd7e254ec6401999d4804b63db&req=diQhH85%2BlIBcXPMW1HO4zfu8TE%2FnuthJeTUODIxsqW%2FqqHdIHp1pjlz5W8NF%0AGbu8I%2B1VV%2BcEzQm%2BXSs%3D%0A)

Puis, autoriser la connexion via Chift en cliquant sur « **Autoriser** ».

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2469709945/83c5839ae882c3b33fdace7a5d9c/Capture+d%E2%80%99e%CC%81cran+2026-05-29+a%CC%80+16_01_36.png?expires=1788635700&signature=59384283d9a54a3893ec4d141c6749b942b0430f0261611549f5b204ded6598e&req=diQhH85%2BlIhbXPMW1HO4zQvYKU%2B4tGYk%2BA4dmx95aOjgydmFFnje%2BhGP4TGT%0ACdKN9dzOg58V4tbU89g%3D%0A)

Vous serez ensuite redirigé vers la seconde étape d’authentification, qui vous permettra de vous connecter à votre environnement ACD.

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2469711209/4247f39112745c6ae1378ff9d4d1/Capture+d%E2%80%99e%CC%81cran+2026-05-29+a%CC%80+16_01_54+-1-.png?expires=1788635700&signature=2a1ea8b028fd27ff66a1b4611f09470fe253af31d3a52ba16ece51a1df0f9492&req=diQhH85%2FnINfUPMW1HO4zV7W0PGz5w4W3c99AVZgkfWBdo4y01NRgBUe0EP6%0A7OBsI3R6nl4Lt9l1Kc0%3D%0A)

Ici, les premières étapes de préparation deviennent essentielles. Vous devez réenseigner :

| Champ demandé | Valeur |
| --- | --- |
| URL i-Suite Expert | URL récupérée dans ACD. Ex : [https://nomcabinet.suiteexpert.fr/cnx/iSuiteExpert](https://nomcabinet.suiteexpert.fr/cnx/iSuiteExpert) |
| Référence de connexion (CNX) | Référence récupérée dans ACD. Par défaut : CNX |
| Nom d'utilisateur | Utilisateur API créé dans ACD |
| Echeances | Choisir « **Yes **» inclura les échéances comptables dans la synchronisation des écritures. |
| Mot de passe | Mot de passe de l'utilisateur API |

Cliquez sur « **Connecter** » pour finaliser la connexion.

Une fois l'authentification validée, la connexion entre Sellsy et ACD est établie.
​

### 
👉  Étape 3 : Déterminer les paramètres de connexion

Une fois l'authentification terminée, vous devez configurer les correspondances comptables entre Sellsy et ACD.

Cette étape permet au connecteur de savoir comment traduire les données présentes dans Sellsy vers les bons éléments comptables dans ACD.

Pour rappel, l'intégration permet de récupérer les documents de vente et/ou d'achat présents dans Sellsy et de les transmettre automatiquement à ACD, accompagnés de leurs pièces jointes.

Vous devrez compléter les correspondances pour les éléments suivants :

- Taux / codes de TVA de vente
- Taux / codes de TVA d'achat
- Codes de TVA utilisés pour les arrondis
- Journaux comptables
- Comptes comptables
- Comptes de rabais, remises et ristournes

1. Taux / Codes de TVA de vente

Associez chaque taux ou code de TVA utilisé dans Sellsy au code de TVA correspondant dans ACD.

Cette correspondance permet au connecteur d'affecter correctement les montants de TVA sur les écritures de vente exportées. Exemple :

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2469717916/1dd60aa4286a314ef8e6fc8b7fed/Capture+d%E2%80%99e%CC%81cran+2026-05-29+a%CC%80+16_43_36.png?expires=1788635700&signature=d85c5df490e87076642348ccde60fcec402df40f9aed8c5bb0e00dc7535d225d&req=diQhH85%2FmoheX%2FMW1HO4zTsijKuNu%2BwwGg1vVIpA%2Fzq52xEyQcA%2B7wfc2dX%2B%0AeOIun4PSSiAgIs7dV70%3D%0A)

2. Taux / Codes de TVA d'achat

Associez chaque taux ou code de TVA utilisé sur vos factures fournisseurs Sellsy au code correspondant dans ACD.

Cette étape garantit une comptabilisation correcte de la TVA déductible lors de l'export des achats. Exemple :

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2469718730/48122f1447ac3e8dc015be1d2916/Capture%2Bd-E2-80-99e-CC-81cran%2B2026-05-29%2Ba-CC-80%2B16_43_36.png?expires=1788635700&signature=c1926c59ae64070bd984cc6dbeaf456c54ed04424566fb453c41c76f855d1f95&req=diQhH85%2FlYZcWfMW1HO4zbuwqtD%2BVMWudFqbhiLe2qjBPF13%2BrESjTqb%2BGEY%0AEyJKfaiN4akg%2Fs1H9xw%3D%0A)

3. Codes TVA pour les arrondis

Certaines écritures peuvent engendrer des écarts d'arrondi de quelques centimes.

Vous devez indiquer le code de TVA à utiliser pour ces ajustements afin de garantir l'équilibre des écritures transmises dans ACD. Exemple :

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2469723015/a84863cd84a87d0155e3561565ef/Capture+d%E2%80%99e%CC%81cran+2026-05-29+a%CC%80+16_46_37.png?expires=1788635700&signature=6d8dec70d89a98a85ca1100f7733ca97efd67b4da6056dd516a70321856a1d65&req=diQhH858noFeXPMW1HO4zbyC47Rq8rpvOiM9AgWnryb%2BvGe0I5nYGvF4U0q1%0A1H%2F0rDq1DMjT0xYGksY%3D%0A)

4. Journaux comptables

Associez les journaux Sellsy aux journaux comptables existants dans ACD. Par exemple :

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2469724512/1ca2674a5498a807dab8310b60ce/Capture+d%E2%80%99e%CC%81cran+2026-05-29+a%CC%80+16_47_07.png?expires=1788635700&signature=fedfe176d58ba13f753ae3e208e31ad38d4364316eb27e5797433a8958eb0d9f&req=diQhH858mYReW%2FMW1HO4zRsquq7NIjUo7RfxCp9MalSboH65%2BauHqZEhpCQB%0ApgxQISUYNEEA%2Fe6p1iY%3D%0A)

Les journaux sélectionnés doivent avoir été préalablement autorisés lors du partage du dossier dans i-Suite Expert.

5. Comptes comptables

Associez les comptes comptables utilisés dans Sellsy aux comptes correspondants dans ACD.

Ces correspondances permettent d'affecter correctement les écritures comptables lors de leur création.

Nous vous recommandons de vérifier la cohérence entre votre plan comptable Sellsy et votre plan comptable ACD avant de valider le paramétrage.

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2469725749/23efc019e83ec54782291f7040fd/Capture+d%E2%80%99e%CC%81cran+2026-05-29+a%CC%80+16_50_04.png?expires=1788635700&signature=206383922b4286aeb881e414f91c8e9ecf71b3cde7048b9a39a4d5449185ec3d&req=diQhH858mIZbUPMW1HO4zfRUAsrcgdXbyQv730BxpGSKvfAUp73RkMxA3oKO%0AYiMhQsQTNibeoecOu6Y%3D%0A)

6. Rabais, remises et ristournes

Si vous utilisez des rabais, remises ou ristournes dans Sellsy, vous devez également définir les comptes comptables qui recevront ces montants dans ACD en cliquant sur « **Oui** », puis sur « **Enregistrer** ».

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2469729234/319914d20adea9a71499b3817da1/Capture+d%E2%80%99e%CC%81cran+2026-05-29+a%CC%80+16_51_33.png?expires=1788635700&signature=abc039858c9ee3a88e11cce5793fe835fbe7b55c87f0a54b947ea59602db35c2&req=diQhH858lINcXfMW1HO4zZzjD7WGMlBlKFSx1sxnkw69MFLYuE6DteefetQW%0AMWoCvzbkWZnA2eNbMnA%3D%0A)

Autrement, cliquez sur « **Non** », puis sur « **Passer** ».

En cas de doute, rapprochez-vous de votre cabinet comptable ou de votre administrateur ACD.
​

### 
👉  Étape 4 : Derniers ajustements techniques

Votre connexion est maintenant configurée.

Avant d'activer l'intégration, quelques paramètres complémentaires vous permettent d'adapter le fonctionnement de la synchronisation à votre organisation comptable.

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2469749914/90ec1f4c67b28bb725b63d190c59/Capture+d%E2%80%99e%CC%81cran+2026-05-29+a%CC%80+16_54_13.png?expires=1788635700&signature=449053719b3e7bdb34154563ea9f364beb4b1db4f44bc0c08e99ca256f7d34ab&req=diQhH856lIheXfMW1HO4zZ6UG1Z%2Bdtc64w6JbaBhYNwmlv028tNk2RAtxaIx%0AHCKnzE5cGmuvMV1L%2BtI%3D%0A)

1. Date de début de synchronisation

Sélectionnez la date à partir de laquelle les factures/avoirs Sellsy devront être transmis à ACD.

Chaque nuit, le connecteur synchronisera automatiquement les factures et avoirs :

- ayant une date égale ou postérieure à la date sélectionnée ;
- marqués comme devant être envoyées en comptabilité.

> **Bon à savoir :**  Si vous mettez en place l'intégration pour la première fois, choisissez une date cohérente avec votre période comptable afin d'éviter l'export de documents déjà traités dans ACD.

2. Création des écritures en brouillon / attente

La création d'écritures en brouillon via API n’est pas prise en charge par ACD. Les écritures arrivent directement en comptabilité. Le choix effectué sur cette étape n’aura donc aucun impact sur la synchronisation.

> **Bon à savoir :** L'absence de création d'écritures en brouillon/attente ne signifie pas qu'une écriture ne peut pas être modifiée post-import. Elle peut être modifiée à tout moment en comptabilité. L'écriture arrivera, par défaut, en « **traitée **», mais le statut peut être modifié en « **à traiter** » post-import automatique.

### 

3. Synchroniser les documents sans justificatif

Choisissez si les factures ou avoirs ne disposant pas de pièce jointe doivent être transmis à ACD.

- Oui : Les documents seront synchronisés même si aucun justificatif n'est associé.
- Non : Seuls les documents accompagnés d'un justificatif seront transmis.

> **Important :** Nous recommandons de désactiver cette option si votre cabinet comptable exige systématiquement la présence d'un justificatif pour chaque écriture.

4. Libellé des écritures

Définissez la manière dont les libellés des écritures comptables seront générés dans ACD.

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

Les nouvelles factures et avoirs répondant aux critères définis seront transmis à ACD avec leurs écritures comptables, leurs tiers et leurs pièces jointes associées.

> **Important : **Nous recommandons de vérifier attentivement les premiers documents transmis dans ACD. Plus une anomalie est détectée tôt, plus elle est simple à corriger. Une fois les premiers contrôles validés et les éventuels ajustements effectués, l’intégration fonctionnera de manière autonome.

___________________________________________________________

## Questions fréquentes

L'intégration fonctionne uniquement de Sellsy vers ACD.
Les factures et avoirs créés **[et comptabilisés](https://help.sellsy.com/fr/articles/5875018-comptabiliser-des-factures-d-achat-et-de-vente)** dans Sellsy, ainsi que les écritures comptables, les tiers et les pièces jointes associées, sont automatiquement transmis vers ACD.
Les modifications réalisées directement dans ACD ne sont pas automatiquement répercutées dans Sellsy.
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

Lorsqu'une écriture a déjà été créée dans ACD, la correction doit généralement être réalisée directement dans ACD.
Si l'erreur est liée au paramétrage du connecteur (code TVA, compte comptable, journal, etc.), nous recommandons également de corriger la configuration de l'intégration afin d'éviter que l'erreur ne se reproduise lors des synchronisations suivantes.
Dans la majorité des cas, les corrections d'écritures déjà intégrées sont réalisées dans ACD.
​

Nous recommandons de vérifier attentivement les premières factures et avoirs transmis dans ACD afin de confirmer que :
- Les comptes comptables sont corrects
- Les codes TVA sont correctement affectés
- Les journaux utilisés sont les bons
- Les tiers sont correctement créés ou rapprochés
- Les pièces jointes sont bien présentes
Plus une anomalie est détectée tôt, plus elle est simple à corriger.
Une fois les premiers contrôles validés et les éventuels ajustements effectués, l'intégration fonctionnera de manière autonome et vous n'aurez généralement plus à intervenir sur son paramétrage.
​

Lors de la synchronisation, le connecteur recherche automatiquement une correspondance existante dans ACD à partir de plusieurs critères :
- Compte auxiliaire
- Numéro de TVA
- SIRET ou numéro d'entreprise
- Nom du tiers
Si aucune correspondance n'est trouvée, un nouveau client ou fournisseur est créé automatiquement dans ACD.
​

Pour faciliter le suivi des écritures importées depuis Sellsy, nous recommandons de définir avec votre cabinet comptable :
- Des journaux dédiés aux flux Sellsy
- Une convention de libellés spécifique
- Une procédure de contrôle des imports
Cette organisation permet généralement d'identifier facilement les écritures provenant de l'intégration.
​

Les pièces jointes associées aux documents de vente et d'achat peuvent être transmises vers ACD avec les écritures comptables.
[Lors du paramétrage de l'intégration](#h_855db9fb9b), vous pouvez choisir de synchroniser tous les documents ou uniquement ceux disposant d'un justificatif.
​

Nous préconisons de faire intervenir votre expert-comptable pour la configuration de l'intégration. Assurez-vous qu'il dispose :
- D'un [accès gratuit expert-comptable](https://help.sellsy.com/fr/articles/6652377-donner-un-acces-sellsy-a-mon-expert-comptable) au compte Sellsy concerné avec un [profil administrateur associé](https://help.sellsy.com/fr/articles/5864112-profils-de-privileges)
- Des droits nécessaires dans ACD
- Des informations de connexion i-Suite Expert
​

La comptabilité analytique **n'est pas prise en charge** par l'intégration entre Sellsy et ACD.
​

En cas d'erreur lors de la connexion, vérifiez :
- L'URL i-Suite Expert
- La référence de connexion (CNX)
- Le nom d'utilisateur API
- Le mot de passe de l'utilisateur API
Si le problème persiste, rapprochez-vous de votre administrateur afin de vérifier la configuration de l'environnement i-Suite Expert.
​

Vérifiez :
- Que le dossier est partagé dans i-Suite Expert
- Que l'utilisateur API dispose des droits d'accès sur ce dossier
- Que le partage du dossier est actif
Si le problème persiste, rapprochez-vous de votre administrateur afin de vérifier la configuration de l'environnement i-Suite Expert.



Vérifiez :
- Que les accès API sont activés
- Que l'utilisateur API est actif
- Que votre version d'ACD est compatible
- Que le module i-Suite Expert est bien installé et opérationnel
- Que les informations de connexion renseignées sont correctes
Si le problème persiste, rapprochez-vous de votre administrateur afin de vérifier la configuration de l'environnement i-Suite Expert.
​


Veuillez vérifier que :
- La facture a bien été comptabilisée dans Sellsy. Les documents de vente et d'achat non comptabilisés ne sont pas synchronisés vers ACD.
- L'exercice comptable concerné n'est pas clôturé dans ACD.
- La devise de la facture est autorisée dans ACD.
- Le pays du client ou du fournisseur est autorisé dans ACD.
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
