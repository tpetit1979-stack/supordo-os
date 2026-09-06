---
source: https://help.sellsy.com/fr/articles/15480364-connecter-sellsy-et-fulll
categorie: Intégrations et API
titre: Connecter Sellsy et Fulll
date_recuperation: 2026-09-05
---

# Connecter Sellsy et Fulll

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472625885/0267995731d98ce2bbaff867466a/FAQ-Bannie-CC-80reAcademy-2-2B-282-29.png?expires=1788635700&signature=f215d70349e8317aa4da6e3b98b6ac8098c8d5ec954cda73dfa169d9a5465ab8&req=diQgFM98mIlXXPMW1HO4zbhCedPUz1GQvV%2FeA9Kn3prNYICfIW9Zk6OG2oUN%0A%2BCbVxCY4WcCA523hPms%3D%0A)

## Introduction

Bienvenue dans le [guide d'activation de connexion Sellsy x Fulll](#h_ad95ad6ac7). Pour rappel, la connexion Fulll est incluse dans votre licence Sellsy Facturation, aucun coût additionnel n'est associé à son usage. Elle permet de :

- Synchroniser automatiquement les avoirs et factures de vente depuis Sellsy vers Fulll
- Synchroniser automatiquement les avoirs et factures d'achat depuis Sellsy vers Fulll
- Transmettre les pièces jointes PDF associées aux factures
- Synchroniser les clients et fournisseurs (tiers)
- Créer automatiquement les comptes de tiers dans Fulll lorsque nécessaire

> **Bon à savoir :** La synchronisation vers Fulll ne concerne que les documents [comptabilisés dans Sellsy](https://help.sellsy.com/fr/articles/5875018-comptabiliser-des-factures-d-achat-et-de-vente). Si un document n'a pas encore été comptabilisé, il ne sera pas transmis à Fulll lors des synchronisations automatiques.

### 
Données synchronisées

| Donnée | Pris en charge |
| --- | --- |
| Écritures de vente | ✅ |
| Pièces jointes de vente | ✅ |
| Écritures d'achat | ✅ |
| Pièces jointes d'achat | ✅ |
| Synchronisation / création des comptes tiers | ✅ |

> **Important :** Cette intégration fonctionne dans un seul sens. Les données sont transmises de Sellsy à Fulll. Les modifications réalisées directement dans Fulll ne sont pas automatiquement répercutées dans Sellsy.

___________________________________________________________

## Guide d'activation de connexion Sellsy x Fulll

### 
⚠️ Avant de commencer

Avant de configurer la connexion entre Sellsy et Fulll, assurez-vous de disposer des accès nécessaires et de remplir les prérequis techniques.

> **Important :** Nous recommandons que l’activation de cette intégration soit réalisée par votre expert-comptable. 
> Les licences des cabinets comptables disposent par défaut d’un accès API, ce qui n'est souvent pas le cas sur les licences d'une entreprise chez un outil comptable tel que Fulll. De plus, les étapes de paramétrage comptable seront mieux maîtrisées si elles sont effectuées par votre cabinet.
> Avant de transmettre cette page à votre expert-comptable, assurez-vous d’avoir réalisé les étapes préalables dans votre compte Sellsy, [décrites ci-dessous](https://help.sellsy.com/fr/articles/15479499-connecter-sellsy-et-tiime#h_6cf220cff6).
> N’effectuez vous-même cette activation que si votre comptabilité est internalisée. Dans ce cas, assurez-vous que votre licence ou votre niveau de plan inclut un accès API.

### Côté Sellsy

- Une licence Sellsy Facturation active ;
- Des [factures/avoirs comptabilisés](https://help.sellsy.com/fr/articles/5875018-comptabiliser-des-factures-d-achat-et-de-vente) (si un document n'a pas encore été comptabilisé, il ne sera pas transmis à Fulll lors des synchronisations automatiques) ;
- La [conformité stricte active](https://help.sellsy.com/fr/articles/6100605-activer-le-mode-conforme-pour-les-documents-de-vente) sur le compte Sellsy ;
- Les droits nécessaires pour accéder aux intégrations comptables :
- **Vous êtes client Sellsy, votre comptabilité est internalisée et gérée chez Fulll :** Vous devez disposer d'un profil administrateur ou d'un profil ayant accès aux paramètres d'intégration. Si vous ne disposez pas des droits nécessaires, contactez un administrateur de votre compte Sellsy. Pour en savoir plus sur les profils et privilèges Sellsy, consultez [cet article](https://help.sellsy.com/fr/articles/5864112-profils-de-privileges).
- **Vous êtes expert-comptable d'un client Sellsy :** Avant de poursuivre la configuration, assurez-vous que votre client vous a accordé un accès expert-comptable associé à un [profil administrateur](https://help.sellsy.com/fr/articles/5864112-profils-de-privileges). L'accès Expert-Comptable est gratuit et permet d'accéder aux données nécessaires à la synchronisation comptable. Si vous ne disposez pas encore d'un accès expert-comptable, votre client devra suivre la procédure décrite [dans cet article](https://help.sellsy.com/fr/articles/6652377-donner-un-acces-sellsy-a-mon-expert-comptable).

### 
Côté Fulll

L’application Chift/Sellsy doit être activée sur le compte du cabinet de votre expert-comptable. Avant d’activer la connexion, veuillez vérifier que cette activation a bien été effectuée.
​

Si ce n’est pas encore le cas, ou si vous n'êtes pas certain(e), contactez le support Fulll à l’adresse [assistance@fulll.help](mailto:assistance@fulll.help) afin de demander l’activation de l’application sur le compte du cabinet de votre expert-comptable.

Il faudra vous authentifier sur votre compte Fulll pour activer l'intégration. Assurez-vous de disposer de l'identifiant et du mot de passe de votre compte Fulll.


​

### 👉  Étape 1 : Connecter Fulll dans Sellsy

Depuis la [page marketplace Sellsy à propos de l’intégration Fulll](https://go.sellsy.com/applications/fulll) cliquez sur : « **Activer l’intégration** ».

Ou bien cliquez directement sur [ce lien](https://marketplaces.chift.app/fr/sellsy/apps/8017). Vous serez redirigé vers l'interface sécurisée Chift.
​

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472638523/7f509b8e83d8db58f1ca2b70f744/Capture+d%E2%80%99e%CC%81cran+2026-06-12+a%CC%80+14_08_26.png?expires=1788635700&signature=7e60483dbe1446daa233fdc13fab97aa090f1a3a31b210373f3fd169cb1c43a2&req=diQgFM99lYRdWvMW1HO4zc995pMKpGzD8GlYzNmbhexFYesydyCtsbrWCK2W%0AQ19KLCVppamW3kuDmik%3D%0A)

### 
👉  Étape 2 : Authentifier la connexion

Dans l’interface Chift, cliquez sur « **Activer l’intégration** ». Si c’est votre première connexion pour ce compte, cliquez sur « **En créer une nouvelle** ».

Si une connexion a déjà été créée pour ce compte, sélectionnez simplement le compte correspondant dans le menu déroulant, puis cliquez sur « **Valider** ».

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472624739/a1cdceae4aca8ec1269ce166c76b/Capture-2Bd-E2-80-99e-CC-81cran-2B2026-05-29-2Ba-CC-80-2B15_55_08.png?expires=1788635700&signature=d630d57d2f903c573bae4ca101d77e6618b0ea5a4dc4f25263ab87c5be8fa5e9&req=diQgFM98mYZcUPMW1HO4zYNt%2BwAUez%2FaJ0Gmr5FRBx0WwE0ymKQ%2BKP8QFzdC%0AHJHOnlGvWu4BjOfSPgk%3D%0A)

Pour créer une nouvelle connexion, munissez-vous du nom et du numéro SIRET de l’entreprise utilisant Sellsy. Renseignez ces informations, puis cliquez sur « **Enregistrer** ».

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472624741/fbcd5e93f463fa6d0a18c7ae4478/Capture-2Bd-E2-80-99e-CC-81cran-2B2026-05-29-2Ba-CC-80-2B15_58_07.png?expires=1788635700&signature=1660d3124d68e5ce0382cbf2b4597c455e9fd0b0aa25f25252e29acc605c0530&req=diQgFM98mYZbWPMW1HO4zdPri2KQvkGj1Wyc6yilJhRNpB2w3xXTBEMORJTV%0AptHMoGvxEiSnH1xq%2BA8%3D%0A)

Une fois ces étapes complétées, vous allez vous retrouver sur un écran comme celui-ci :

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472648851/cb15fc2af3c869149be7e9aa1bf8/Capture+d%E2%80%99e%CC%81cran+2026-06-12+a%CC%80+14_14_19.png?expires=1788635700&signature=2e7b43b6083451287469ffe853d718f94a876d3d97f725d367ff8b031b151aa1&req=diQgFM96lYlaWPMW1HO4zWeReIjWTCLhmOStNOFDSb9xddw6FmQs3DplM%2FPc%0AgiJer6ae4anFobZI%2Fv0%3D%0A)

En cliquant sur « **Connecter** », vous serez redirigé vers l’écran de connexion Sellsy.

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472624744/d85cad331faf454c6162d4ec1c36/Capture-2Bd-E2-80-99e-CC-81cran-2B2026-05-29-2Ba-CC-80-2B16_00_46.png?expires=1788635700&signature=21ca5dda9617fae64d4bad3fa06056040616f642d13553af976e1baa37417354&req=diQgFM98mYZbXfMW1HO4zaULF4YKAktcqnVr%2BTM1eV%2FnqlqsT6IyP0Hn6lbD%0Abd8SvV79rstLo8HeXRU%3D%0A)

Il vous suffit de renseigner vos identifiants Sellsy. Si plusieurs comptes sont associés à ces identifiants, sélectionnez le compte concerné dans le menu déroulant.

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472624748/73a54951816774354eb619ec7b33/Capture-2Bd-E2-80-99e-CC-81cran-2B2026-05-29-2Ba-CC-80-2B16_01_26-2B-1-.png?expires=1788635700&signature=b3fa07577d9ce2e575352041d8509dfa3c34d79d1c286c49093bcdc5e225813e&req=diQgFM98mYZbUfMW1HO4zd2cHx0M3c3NiV1DlrQP2gWCj5XHFMDxN19hFGEm%0AMv87TyJX%2FfoqKgpnoys%3D%0A)

Puis, autoriser la connexion via Chift en cliquant sur « **Autoriser** ».

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472624749/2e799ebd6c1238a78a959162d46f/Capture-2Bd-E2-80-99e-CC-81cran-2B2026-05-29-2Ba-CC-80-2B16_01_36.png?expires=1788635700&signature=45dfdf8c34de89ba2b916110aabb15c47d97b7a398d88495a1a7301a63a09f2d&req=diQgFM98mYZbUPMW1HO4zQpjf8YG8BDfagpUKvohNhv%2BDi%2BVdvuuZdNOs8mj%0AOGbHG9quFepXD%2FQ9P7c%3D%0A)

Vous serez ensuite redirigé vers la seconde étape d’authentification, qui vous permettra de vous connecter à votre environnement Fulll.

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472645461/a9d650119a7693cdc87ab5a6cda6/Capture%2Bd-E2-80-99e-CC-81cran%2B2026-06-12%2Ba-CC-80%2B14_12_17.png?expires=1788635700&signature=46c4202ab067f221561f75a082f88a96426deb67eb72fa97de99a801a87ad3a7&req=diQgFM96mIVZWPMW1HO4zUi29FkfC9EkkalGVioczhNTUpXlyrUcA4wWg0HL%0AI0850LzyqI0bqhpplso%3D%0A)

Si vous n'êtes pas encore connecté(e) à votre compte Fulll, vous allez être rédirigé(e) vers une page de connexion. Alternativement, vous pouvez effectuer cette démarche dans un onglet à part. Une fois connecté(e), il suffit de cliquer sur « **Autoriser** ».​


![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472656672/a23c2d8a9e858fa5d76ab711b0f2/Capture+d%E2%80%99e%CC%81cran+2026-06-12+a%CC%80+14_18_32.png?expires=1788635700&signature=6fdba396806e9cc72033234713a4e9337071bfa46ce3568ad1c854553e78783c&req=diQgFM97m4dYW%2FMW1HO4zVjxnnppcVyIaIIZfuaGsU6Bhe%2BTfnC5ScOMYXkJ%0AOoqzq4VQcGBTQAF6LOk%3D%0A)


Depuis le menu déroulant, vous devez choisir le compte comptable à utiliser et cliquer ensuite sur « **Valider** ».
​
En dernière étape, vous devez choisir la typologie des documents à synchroniser (ventes, achats ou les deux).
​

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472624793/c5429d4d0728e2ff0c1fa8cfaf40/Capture%2Bd-E2-80-99e-CC-81cran%2B2026-06-12%2Ba-CC-80%2B12_38_34.png?expires=1788635700&signature=9bd381c4bc9c1f0336df0daa277e4d90ec672beee1593b15ad7fb759c5aa6598&req=diQgFM98mYZWWvMW1HO4zZI2NnL8w3EYvz%2BRXLQskvbo7W%2Bx%2FyzV3Y13JAbl%0A7zMC9ULmDrzJZKpvKGo%3D%0A)


Une fois la sélection effectuée, vous pouvez déterminer les paramètres de connexion entre Sellsy et Fulll.


​

### 
👉  Étape 3 : Déterminer les paramètres de connexion

Une fois l'authentification terminée, vous devez configurer les correspondances comptables entre Sellsy et Fulll.

Cette étape permet au connecteur de savoir comment traduire les données présentes dans Sellsy vers les bons éléments comptables dans Fulll.

Pour rappel, l'intégration permet de récupérer les documents de vente et/ou d'achat présents dans Sellsy et de les transmettre automatiquement à Fulll, accompagnés de leurs pièces jointes.

Vous devrez compléter les correspondances pour les éléments suivants :

- Taux / codes de TVA de vente
- Taux / codes de TVA d'achat
- Codes de TVA utilisés pour les arrondis
- Journaux comptables
- Comptes comptables
- Comptes de rabais, remises et ristournes

1. Taux / Codes de TVA de vente

Associez chaque taux ou code de TVA utilisé dans Sellsy au code de TVA correspondant dans Fulll.

Cette correspondance permet au connecteur d'affecter correctement les montants de TVA sur les écritures de vente exportées. Exemple :

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472624787/5231376c05d4757da8aa486a4822/Capture-2Bd-E2-80-99e-CC-81cran-2B2026-05-29-2Ba-CC-80-2B16_43_36.png?expires=1788635700&signature=aaea64603bf64550ef57db4f2adac1b0d526fc4a8e486b94b7234967212583fc&req=diQgFM98mYZXXvMW1HO4ze%2FZtBJ90M5nGhxWAg0rexXtNSePL0OddrIcoiLY%0AJhjrUYr6jEpQcaDCSYM%3D%0A)

2. Taux / Codes de TVA d'achat

Associez chaque taux ou code de TVA utilisé sur vos factures fournisseurs Sellsy au code correspondant dans Fulll.

Cette étape garantit une comptabilisation correcte de la TVA déductible lors de l'export des achats. Exemple :

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472624790/c82dfe9ad2d267deb03ba7b7f036/Capture-2Bd-E2-80-99e-CC-81cran-2B2026-05-29-2Ba-CC-80-2B16_43_36.png?expires=1788635700&signature=c3bb99d553a4087032323428ff339698ac05afa9b6c51e8b336e4300acf6aed8&req=diQgFM98mYZWWfMW1HO4zba%2Bj2cKSTbQ%2BH6hZWQyZxL21kAM46j8JVjwOwiT%0AP5g9emV35GBmbOfAaXE%3D%0A)

3. Codes TVA pour les arrondis

Certaines écritures peuvent engendrer des écarts d'arrondi de quelques centimes.

Vous devez indiquer le code de TVA à utiliser pour ces ajustements afin de garantir l'équilibre des écritures transmises dans Fulll. Exemple :

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472624786/9d092bac6dbc759aee81fdbf0491/Capture-2Bd-E2-80-99e-CC-81cran-2B2026-05-29-2Ba-CC-80-2B16_46_37.png?expires=1788635700&signature=60b06ee18b95ee033069a5820cafbb24f3151f0a6a38d28df99840e8625718f4&req=diQgFM98mYZXX%2FMW1HO4zVUlzBSF40xTsJ6rw9yxwbbpZgj2scDd9MRPOhN%2B%0AKSikQRDqCiYsAqHQjw0%3D%0A)

4. Journaux comptables

Associez les journaux Sellsy aux journaux comptables existants dans Fulll. Par exemple :

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472624784/a55d128ecc80a4228b5ac3d5c15f/Capture-2Bd-E2-80-99e-CC-81cran-2B2026-05-29-2Ba-CC-80-2B16_47_07.png?expires=1788635700&signature=37f0f7d256b23232511880221f6ca7c7d778d62f7ae3782538b4cbc289773d7a&req=diQgFM98mYZXXfMW1HO4zZuUpBtfFZ%2BqLFgiEqXNJo0llFp9ERGHEW0b6EOl%0AFSyHN1CbLdkEtwCGabk%3D%0A)

Les journaux sélectionnés doivent avoir été préalablement autorisés lors du partage du dossier dans Fulll.

5. Comptes comptables

Associez les comptes comptables utilisés dans Sellsy aux comptes correspondants dans Fulll.

Ces correspondances permettent d'affecter correctement les écritures comptables lors de leur création.

Nous vous recommandons de vérifier la cohérence entre votre plan comptable Sellsy et votre plan comptable Fulll avant de valider le paramétrage.

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472624785/513d4668735a5442d09bc6c9a71e/Capture-2Bd-E2-80-99e-CC-81cran-2B2026-05-29-2Ba-CC-80-2B16_50_04.png?expires=1788635700&signature=13138501a7f6a4d58fd308fcc01e7972a7eace8d6d64e9da43e0ae998e87122a&req=diQgFM98mYZXXPMW1HO4zeZzlfeHFy9gqY2zR555WOgtmiamJHuKK7EquYTN%0AVoWaM5NcTXqu%2B4jhOYE%3D%0A)

6. Rabais, remises et ristournes

Si vous utilisez des rabais, remises ou ristournes dans Sellsy, vous devez également définir les comptes comptables qui recevront ces montants dans Fulll en cliquant sur « **Oui** », puis sur « **Enregistrer** ».

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472461938/e60041269698bea7c9e214725eb3/Capture-2Bd-E2-80-99e-CC-81cran-2B2026-05-29-2Ba-CC-80-2B16_51_33.png?expires=1788635700&signature=dc70048c968b089e30cacbf1a02c0406781cdbf3bd7c9996195fb3f003625b57&req=diQgFM14nIhcUfMW1HO4zVNwLEFCW9O5cWyFZW7%2BuKy2c1Nf2nupwbKkl4Sp%0AIZA4MIuy%2F7J3qoLkUqM%3D%0A)

Autrement, cliquez sur « **Non** », puis sur « **Passer** ».

En cas de doute, rapprochez-vous de votre cabinet comptable ou de votre administrateur Fulll.
​

### 
👉  Étape 4 : Derniers ajustements techniques

Votre connexion est maintenant configurée.

Avant d'activer l'intégration, quelques paramètres complémentaires vous permettent d'adapter le fonctionnement de la synchronisation à votre organisation comptable.

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472624798/54980d277ca19caeba1a359d5769/Capture-2Bd-E2-80-99e-CC-81cran-2B2026-05-29-2Ba-CC-80-2B16_54_13.png?expires=1788635700&signature=04aade5dd638c5d960520631e039625af49f9ea685543104570330bafd9ac32e&req=diQgFM98mYZWUfMW1HO4zUMNshV5uoXE5nvLL0v0e80yXH%2B%2BMv78piTTXflO%0A2%2FwiG2dinbcyC9b7Kp8%3D%0A)

1. Date de début de synchronisation

Sélectionnez la date à partir de laquelle les factures/avoirs Sellsy devront être transmis à Fulll.

Chaque nuit, le connecteur synchronisera automatiquement les factures et avoirs :

- ayant une date égale ou postérieure à la date sélectionnée ;
- marqués comme devant être envoyées en comptabilité.

> **Bon à savoir :**  Si vous mettez en place l'intégration pour la première fois, choisissez une date cohérente avec votre période comptable afin d'éviter l'export de documents déjà traités dans Fulll.

2. Création des écritures en brouillon / attente

La création des écritures en brouillon via API n'est pas prise en charge par Fulll : le choix effectué sur cette étape n'aura aucun impact sur la synchronisation.

> **Bon à savoir :** L'absence de création d'écritures en brouillon/attente ne signifie pas qu'une écriture ne peut pas être modifiée post-import. Elle peut être modifiée à tout moment en comptabilité. L'écriture arrivera, par défaut, en « **traitée **», mais le statut peut être modifié en « **à traiter** » post-import automatique.

3. Synchroniser les documents sans justificatif

Choisissez si les factures ou avoirs ne disposant pas de pièce jointe doivent être transmis à Fulll.

- Oui : Les documents seront synchronisés même si aucun justificatif n'est associé.
- Non : Seuls les documents accompagnés d'un justificatif seront transmis.

> **Important :** Nous recommandons de désactiver cette option si votre cabinet comptable exige systématiquement la présence d'un justificatif pour chaque écriture.

4. Libellé des écritures

Définissez la manière dont les libellés des écritures comptables seront générés dans Fulll.

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

Les nouvelles factures et avoirs répondant aux critères définis seront transmis à Fulll avec leurs écritures comptables, leurs tiers et leurs pièces jointes associées.

> **Important : **Nous recommandons de vérifier attentivement les premiers documents transmis dans Fulll. Plus une anomalie est détectée tôt, plus elle est simple à corriger. Une fois les premiers contrôles validés et les éventuels ajustements effectués, l’intégration fonctionnera de manière autonome.

___________________________________________________________

## **Questions fréquentes**

L'intégration fonctionne uniquement de Sellsy vers Fulll.
Les factures et avoirs créés **[et comptabilisés](https://help.sellsy.com/fr/articles/5875018-comptabiliser-des-factures-d-achat-et-de-vente)** dans Sellsy, ainsi que les écritures comptables, les tiers et les pièces jointes associées, sont automatiquement transmis vers Fulll.
Les modifications réalisées directement dans Fulll ne sont pas automatiquement répercutées dans Sellsy.
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

Lorsqu'une écriture a déjà été créée dans Fulll, la correction doit généralement être réalisée directement dans Fulll.
Si l'erreur est liée au paramétrage du connecteur (code TVA, compte comptable, journal, etc.), nous recommandons également de corriger la configuration de l'intégration afin d'éviter que l'erreur ne se reproduise lors des synchronisations suivantes.
Dans la majorité des cas, les corrections d'écritures déjà intégrées sont réalisées dans Fulll.
​

Nous recommandons de vérifier attentivement les premières factures et avoirs transmis dans Fulll afin de confirmer que :
- Les comptes comptables sont corrects
- Les codes TVA sont correctement affectés
- Les journaux utilisés sont les bons
- Les tiers sont correctement créés ou rapprochés
- Les pièces jointes sont bien présentes
Plus une anomalie est détectée tôt, plus elle est simple à corriger.
Une fois les premiers contrôles validés et les éventuels ajustements effectués, l'intégration fonctionnera de manière autonome et vous n'aurez généralement plus à intervenir sur son paramétrage.
​

Lors de la synchronisation, le connecteur recherche automatiquement une correspondance existante dans Fulll à partir de plusieurs critères :
- Compte auxiliaire
- Numéro de TVA
- SIRET ou numéro d'entreprise
- Nom du tiers
Si aucune correspondance n'est trouvée, un nouveau client ou fournisseur est créé automatiquement dans Fulll.
​

Pour faciliter le suivi des écritures importées depuis Sellsy, nous recommandons de définir avec votre cabinet comptable :
- Des journaux dédiés aux flux Sellsy
- Une convention de libellés spécifique
- Une procédure de contrôle des imports
Cette organisation permet généralement d'identifier facilement les écritures provenant de l'intégration.
​

Les pièces jointes associées aux documents de vente et d'achat peuvent être transmises vers Fulll avec les écritures comptables.
​[Lors du paramétrage de l'intégration](#h_4e398d3408), vous pouvez choisir de synchroniser tous les documents ou uniquement ceux disposant d'un justificatif.
​

Nous préconisons de faire intervenir votre expert-comptable pour la configuration de l'intégration. Assurez-vous qu'il dispose d'un [accès gratuit expert-comptable](https://help.sellsy.com/fr/articles/6652377-donner-un-acces-sellsy-a-mon-expert-comptable) avec un [profil d'administrateur](https://help.sellsy.com/fr/articles/5864112-profils-de-privileges).


La comptabilité analytique n'est pas prise en charge par cette intégration.


Nous vous conseillons de vous rapprocher de votre administrateur afin de vérifier la configuration de l'environnement Fulll.
​

Nous vous conseillons de vous rapprocher de votre administrateur afin de vérifier la configuration de l'environnement Fulll.
​

Nous vous conseillons de vous rapprocher de votre administrateur afin de vérifier la configuration de l'environnement Fulll.
​

 Veuillez vérifier que :
- La facture a bien été comptabilisée dans Sellsy. Les documents de vente et d'achat non comptabilisés ne sont pas synchronisés vers Fulll.
- L'exercice comptable concerné n'est pas clôturé dans Fulll.
- La devise de la facture est autorisée dans Fulll.
- Le pays du client ou du fournisseur est autorisé dans Fulll.
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
