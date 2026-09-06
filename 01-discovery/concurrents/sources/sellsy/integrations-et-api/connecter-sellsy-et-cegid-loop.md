---
source: https://help.sellsy.com/fr/articles/15477351-connecter-sellsy-et-cegid-loop
categorie: Intégrations et API
titre: Connecter Sellsy et Cegid Loop
date_recuperation: 2026-09-05
---

# Connecter Sellsy et Cegid Loop

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472242969/b1a3708b3b9e63d1c636a25b9774/FAQ-Bannie-CC-80reAcademy-2-2B-282-29.png?expires=1788635700&signature=be74926cbb8025f292bd815107e18d1ee8b3b1db38dd3a1e0a5a876b5596a63a&req=diQgFMt6n4hZUPMW1HO4zSy2kiV7fCRZl%2BiH5%2BnH2IF%2Fzq6yZ4nDN1gCSA2B%0AUbmteycGHLFM06U44R8%3D%0A)

## 
​
Introduction

Bienvenue dans le [guide d'activation de connexion Sellsy x Cegid Loop](#h_691317b08a). Pour rappel, la connexion Cegid Loop est incluse dans votre licence Sellsy Facturation, aucun coût additionnel n'est associé à son usage. Elle permet de :

- Synchroniser automatiquement les avoirs et factures de vente depuis Sellsy vers Cegid Loop
- Synchroniser automatiquement les avoirs et factures d'achat depuis Sellsy vers Cegid Loop
- Transmettre les pièces jointes PDF associées aux factures
- Synchroniser les clients et fournisseurs (tiers)
- Créer automatiquement les comptes de tiers dans Cegid Loop lorsque nécessaire

> **Bon à savoir :** La synchronisation vers Cegid Loop ne concerne que les documents [comptabilisés dans Sellsy](https://help.sellsy.com/fr/articles/5875018-comptabiliser-des-factures-d-achat-et-de-vente). Si un document n'a pas encore été comptabilisé, il ne sera pas transmis à Cegid Loop lors des synchronisations automatiques.

### 
Données synchronisées

| Donnée | Pris en charge |
| --- | --- |
| Écritures de vente | ✅ |
| Pièces jointes de vente | ✅ |
| Écritures d'achat | ✅ |
| Pièces jointes d'achat | ✅ |
| Synchronisation / création des comptes tiers | ✅ |

> **Important :** Cette intégration fonctionne dans un seul sens. Les données sont transmises de Sellsy à Cegid Loop. Les modifications réalisées directement dans Cegid Loop ne sont pas automatiquement répercutées dans Sellsy.

___________________________________________________________

## Guide d'activation de connexion Sellsy x Cegid Loop

### 
⚠️ Avant de commencer

Avant de configurer la connexion entre Sellsy et Cegid Loop, assurez-vous de disposer des accès nécessaires et de remplir les prérequis techniques.

> **Important :** Nous recommandons que l’activation de cette intégration soit réalisée par votre expert-comptable. 
> Les licences des cabinets comptables disposent par défaut d’un accès API, ce qui n'est souvent pas le cas sur les licences d'une entreprise chez un outil comptable tel que Cegid Loop. De plus, les étapes de paramétrage comptable seront mieux maîtrisées si elles sont effectuées par votre cabinet.
> Avant de transmettre cette page à votre expert-comptable, assurez-vous d’avoir réalisé les étapes préalables dans votre compte Sellsy, [décrites ci-dessous](#h_5cc471b793).
> N’effectuez vous-même cette activation que si votre comptabilité est internalisée. Dans ce cas, assurez-vous que votre licence ou votre niveau de plan inclut un accès API.

Côté Sellsy

- Une licence Sellsy Facturation active ;
- Des [factures/avoirs comptabilisés](https://help.sellsy.com/fr/articles/5875018-comptabiliser-des-factures-d-achat-et-de-vente) (si un document n'a pas encore été comptabilisé, il ne sera pas transmis à Cegid Loop lors des synchronisations automatiques) ;
- La [conformité stricte active](https://help.sellsy.com/fr/articles/6100605-activer-le-mode-conforme-pour-les-documents-de-vente) sur le compte Sellsy ;
- Les droits nécessaires pour accéder aux intégrations comptables :
- **Vous êtes client Sellsy, votre comptabilité est internalisée et gérée chez Cegid Loop :** Vous devez disposer d'un profil administrateur ou d'un profil ayant accès aux paramètres d'intégration. Si vous ne disposez pas des droits nécessaires, contactez un administrateur de votre compte Sellsy. Pour en savoir plus sur les profils et privilèges Sellsy, consultez [cet article](https://help.sellsy.com/fr/articles/5864112-profils-de-privileges).
- **Vous êtes expert-comptable d'un client Sellsy :** Avant de poursuivre la configuration, assurez-vous que votre client vous a accordé un accès expert-comptable associé à un [profil administrateur](https://help.sellsy.com/fr/articles/5864112-profils-de-privileges). L'accès Expert-Comptable est gratuit et permet d'accéder aux données nécessaires à la synchronisation comptable. Si vous ne disposez pas encore d'un accès expert-comptable, votre client devra suivre la procédure décrite [dans cet article](https://help.sellsy.com/fr/articles/6652377-donner-un-acces-sellsy-a-mon-expert-comptable).

Côté Cegid Loop

Avant de procéder au paramétrage de l'intégration Cegid Loop, vous devez :
​
1. Générez une clé API depuis votre compte.

Voici comment: [https://app.arcade.software/share/VWS4eqYN11QzPXSuRdRo](https://app.arcade.software/share/VWS4eqYN11QzPXSuRdRo)

2. Connectez-vous sur Loop Hub et lié votre clé API avec le logiciel partenaire puis choisissez le dossier comptable de partage.

Voici comment: [https://app.arcade.software/share/xDBcC6VmzS1Ls7wbOeuk](https://app.arcade.software/share/xDBcC6VmzS1Ls7wbOeuk)

Choisissez un nom pour votre connexion.

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472209437/718902eb2ead7aef4e1bde26b353/919ff0c7-25b3-4a5e-b959-9b0d2e84f201-2F4cafa923-77c8-4d04-be40-0ca6103c73ab-Screenshot_2024-03-15_at_14_01_10.png?expires=1788635700&signature=59bd56109f13df4736f93b6dd9eff83bd9a8926b287ac7908d4628d233478956&req=diQgFMt%2BlIVcXvMW1HO4zfgLM8zw13YkYLY3%2Fd0VHKK6gUDefVzU6phuFhA4%0A4U4fec%2F8j0J5Znuf2xI%3D%0A)

Définissez si vous souhaitez activer le partage des données analytiques.

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472209440/7d68d746673b0f89249472481189/919ff0c7-25b3-4a5e-b959-9b0d2e84f201-2Fad1a7771-6674-4878-bb8e-fdd449c0586a-Screenshot_2024-03-19_at_08_42_17.png?expires=1788635700&signature=67de31e4872ce4c1f676271a0c8b92f163129a51d764d69deef3b4ee7ec672fd&req=diQgFMt%2BlIVbWfMW1HO4zfsKh6SbiWWWecX%2FaKJckpb6dZbJGUo6xvH2wiMY%0A9v1Hrbc168wY3XYveIg%3D%0A)

Renseignez la clé API, générez depuis votre compte.

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472209439/3f26772ad10f9cf776a50788469a/919ff0c7-25b3-4a5e-b959-9b0d2e84f201-2F7afdb127-1d02-491a-9fe6-19b1ade4a1a6-Screenshot_2024-03-15_at_14_42_10.png?expires=1788635700&signature=d0bc8d59f602a9a1c9b766b9244e6b3f52bf0e697a74da5fe6224e86adaedcce&req=diQgFMt%2BlIVcUPMW1HO4zSvriubbeMmpfK%2FnHS0dKUsqRVmd3pFESyEHNnUW%0AlbhlS2juGr648%2BUdXrk%3D%0A)

Renseignez le code secret de la clé API, généré depuis votre compte.

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472209443/316f2a2229277364e104fffac87e/919ff0c7-25b3-4a5e-b959-9b0d2e84f201-2Faa0b6304-9108-4743-b993-323547ec4499-Screenshot_2024-03-15_at_14_42_16.png?expires=1788635700&signature=009ef1ef7a259935e3804ed88d7eac7504f8451da47a75510d168d5e9012c22b&req=diQgFMt%2BlIVbWvMW1HO4zW6YVOMmSqMwsuwAciQ%2BLQiTFFUZOaLDNlyqgFEH%0A8t1zeqJWgyPRmc%2BbBYY%3D%0A)

Cliquez sur « **Connecter** » pour finaliser la connexion.

Configuration

Sélectionnez le dossier comptable à relier.

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472209444/7947c3015d4d1113102d93de1fd0/919ff0c7-25b3-4a5e-b959-9b0d2e84f201-2Fd1e73f05-50bb-40a9-9242-df975d3d1b60-Screenshot_2024-03-15_at_18_13_34.png?expires=1788635700&signature=4a8c13952c6d76181ee60e59e716dbcb4fea417a51fb06cdbeec43ff7d052a23&req=diQgFMt%2BlIVbXfMW1HO4zQjt06ZQw0eQzdMBsOE6%2F927An82Zz38P9h4aqqd%0A8%2FawPGZh8%2F%2BDnl6ecqY%3D%0A)

Cliquez sur « **Valider** » pour finaliser la configuration.


Si vous rencontrez des soucis lors de ces étapes, nous vous conseillons de vous mettre en relation avec les équipes Cegid :  [rendez-vous sur l'assistance client Cegid Loop](https://www.cegid.com/fr/assistance-clients/cegid-loop/). 


​

### 👉  Étape 1 : Connecter Cegid Loop dans Sellsy

Depuis la [page marketplace Sellsy à propos de l’intégration Cegid Loop](https://go.sellsy.com/applications/cegid-loop) cliquez sur : « **Activer l’intégration** ».

Ou bien cliquez directement sur [ce lien](https://marketplaces.chift.app/fr/sellsy/apps/8011). Vous serez redirigé vers l'interface sécurisée Chift.
​

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472195836/0d9b1aacc26d68347e4880b2d7a2/Capture+d%E2%80%99e%CC%81cran+2026-06-12+a%CC%80+09_23_27.png?expires=1788635700&signature=4e7e3de61223392d7978a9055a60b638ae9ef1ea03d865c08372c6015d96f70d&req=diQgFMh3mIlcX%2FMW1HO4zR1IyePHdWYpZpvTgplCBa8lYtzCrKU0oZK4W57N%0AXvmjaUi9L%2B7DCIb8zGs%3D%0A)

### 
👉  Étape 2 : Authentifier la connexion

Dans l’interface Chift, cliquez sur « **Activer l’intégration** ». Si c’est votre première connexion pour ce compte, cliquez sur « **En créer une nouvelle** ».

Si une connexion a déjà été créée pour ce compte, sélectionnez simplement le compte correspondant dans le menu déroulant, puis cliquez sur « **Valider** ».

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472188980/11e55b0e638e6b1219b73cb7d963/Capture%2Bd-E2-80-99e-CC-81cran%2B2026-05-29%2Ba-CC-80%2B15_55_08.png?expires=1788635700&signature=564736e7246ef27851d336a5cb03eb8d169b2f98b25ec1d9cafe0c6fb0a843bc&req=diQgFMh2lYhXWfMW1HO4zTw6mXCw%2BqXc2ZDb7E8fgytBiuxUv0Wq16XrY6cp%0AmG3oWYIK8Or%2BLZf8tKI%3D%0A)

Pour créer une nouvelle connexion, munissez-vous du nom et du numéro SIRET de l’entreprise utilisant Sellsy. Renseignez ces informations, puis cliquez sur « **Enregistrer** ».

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472188972/5689a782ffa94a58b7995574e8d1/Capture%2Bd-E2-80-99e-CC-81cran%2B2026-05-29%2Ba-CC-80%2B15_58_07.png?expires=1788635700&signature=4f3504ef9c18d1acd0504a73b1d88d94527871838192ead2efcca268cbc244d6&req=diQgFMh2lYhYW%2FMW1HO4zVB0nUxdF9xkKJQYg%2FM56r0wcthTDutEv9e92Qot%0AbtpWYTNU1CUBHSXP%2Fcs%3D%0A)

Une fois ces étapes complétées, vous allez vous retrouver sur un écran comme celui-ci :

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472197919/e5827372d93c2c3006e60344fb9b/Capture+d%E2%80%99e%CC%81cran+2026-06-12+a%CC%80+09_25_01.png?expires=1788635700&signature=6977450c73993ddc0fd53d1c7dc0adf37883af94d65c8bf0f0bf24125b739b04&req=diQgFMh3moheUPMW1HO4zSo0PGTTYQ7rWTlxAREV%2Fw8DDlVuepLOaBOIuAvf%0AgeCfBm6aqOB4KLkiRnc%3D%0A)

En cliquant sur « **Connecter** », vous serez redirigé vers l’écran de connexion Sellsy.

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472188973/3ec9bd67c5add57e2ee06e49cdc6/Capture%2Bd-E2-80-99e-CC-81cran%2B2026-05-29%2Ba-CC-80%2B16_00_46.png?expires=1788635700&signature=6be324fd9a88690167af1d2e1d59856ae2791cbb73bfbea5a35f0977ece2af24&req=diQgFMh2lYhYWvMW1HO4zZ3gms8jZ%2BC8aPBGwxIr1nCXgpgUKTG0HTwT1M5g%0AdZRTig3iyBVWHSC54mQ%3D%0A)

Il vous suffit de renseigner vos identifiants Sellsy. Si plusieurs comptes sont associés à ces identifiants, sélectionnez le compte concerné dans le menu déroulant.

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472188975/6a6b2942ef8c59e5e6d75a7451e9/Capture%2Bd-E2-80-99e-CC-81cran%2B2026-05-29%2Ba-CC-80%2B16_01_26%2B-1-.png?expires=1788635700&signature=af099189711dccf3964484b816c43793e0572387b82af8437d25c30e8d7fc582&req=diQgFMh2lYhYXPMW1HO4zZoEI4wSgmA2fo2vUa6loq2m4K8Oqm6UGgXE5%2FCJ%0AcuCkxh4yNSqcj1ZYwPo%3D%0A)

Puis, autoriser la connexion via Chift en cliquant sur « **Autoriser** ».

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472188982/91868fa701af077eed859e95c855/Capture%2Bd-E2-80-99e-CC-81cran%2B2026-05-29%2Ba-CC-80%2B16_01_36.png?expires=1788635700&signature=c50c38eb102f433357fb0b6046e09c8370f8e04e453a65b1d037d35ea3cf12be&req=diQgFMh2lYhXW%2FMW1HO4zeG7D42gvwO%2FaDMZzGCmUSR%2F4otET%2FzCYwHdJJ2U%0AsYcTTp87bcvUzu8go0Q%3D%0A)

Vous serez ensuite redirigé vers la seconde étape d’authentification, qui vous permettra de vous connecter à votre environnement Cegid Loop.

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472199916/d9e713ad3b696ceabf925108c610/Capture+d%E2%80%99e%CC%81cran+2026-06-12+a%CC%80+09_26_42.png?expires=1788635700&signature=57e47bd4adf2046aa3fc76e7a7bdea06639f9350326e32a5b3c663d2899dcac9&req=diQgFMh3lIheX%2FMW1HO4zVkLt1lt%2B30spp0QPyfNcso4%2BmaLmK9ZEToJmCqc%0AYXyf7ifLUCbbFCpYKSU%3D%0A)

Ici, [les premières étapes de préparation](#h_e81b200b3a) deviennent essentielles. Vous devez réenseigner la clé API et le secret de la clé API Cegid Loop.
​

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472202313/721b26d7fd93709e3228c1e3baf5/Capture+d%E2%80%99e%CC%81cran+2026-06-12+a%CC%80+09_27_25.png?expires=1788635700&signature=d9b1d3d1c71a697c421c8097f6ddfee2caf8c65dd08553eca5209b5ef1602f36&req=diQgFMt%2Bn4JeWvMW1HO4zdLhDFTgECWsesLWeK1cc5LHxzbk8hrF%2BMjeuGm2%0A3NIOVlQk0h30ORoC364%3D%0A)


Cliquez sur « **Connecter** » pour finaliser la connexion.

Une fois l'authentification validée, la connexion entre Sellsy et Cegid Loop est établie.
​

### 
👉  Étape 3 : Déterminer les paramètres de connexion

Une fois l'authentification terminée, vous devez configurer les correspondances comptables entre Sellsy et Cegid Loop.

Cette étape permet au connecteur de savoir comment traduire les données présentes dans Sellsy vers les bons éléments comptables dans Cegid Loop.

Pour rappel, l'intégration permet de récupérer les documents de vente et/ou d'achat présents dans Sellsy et de les transmettre automatiquement à Cegid Loop, accompagnés de leurs pièces jointes.

Vous devrez compléter les correspondances pour les éléments suivants :

- Taux / codes de TVA de vente
- Taux / codes de TVA d'achat
- Codes de TVA utilisés pour les arrondis
- Journaux comptables
- Comptes comptables
- Comptes de rabais, remises et ristournes

1. Taux / Codes de TVA de vente

Associez chaque taux ou code de TVA utilisé dans Sellsy au code de TVA correspondant dans Cegid Loop.

Cette correspondance permet au connecteur d'affecter correctement les montants de TVA sur les écritures de vente exportées. Exemple :

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472188983/07542f2ddb6613ca9661941c96f1/Capture%2Bd-E2-80-99e-CC-81cran%2B2026-05-29%2Ba-CC-80%2B16_43_36.png?expires=1788635700&signature=fd4bee6d44004e0e21744d16ab0f67be91740d2b7d4178a3f3e8ee877068c1b0&req=diQgFMh2lYhXWvMW1HO4zXF%2F2WbfQyw7MIZoKds3UfBBEM5AJ0UYNTmToUeM%0Ali6L9FttW%2BVSYY2SsKE%3D%0A)

2. Taux / Codes de TVA d'achat

Associez chaque taux ou code de TVA utilisé sur vos factures fournisseurs Sellsy au code correspondant dans Cegid Loop.

Cette étape garantit une comptabilisation correcte de la TVA déductible lors de l'export des achats. Exemple :

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472188990/274fe116b8b4a721ac966cf2b808/Capture-2Bd-E2-80-99e-CC-81cran-2B2026-05-29-2Ba-CC-80-2B16_43_36.png?expires=1788635700&signature=793c9ba063290f9bf97f740e2165e183af9653592a59107b29594341af1a1a6e&req=diQgFMh2lYhWWfMW1HO4zQRHTLDyBVCRbB6TdE6eBNq2u4SopCxnB755I97Q%0AYgOsVXCAec3KMSnGexU%3D%0A)

3. Codes TVA pour les arrondis

Certaines écritures peuvent engendrer des écarts d'arrondi de quelques centimes.

Vous devez indiquer le code de TVA à utiliser pour ces ajustements afin de garantir l'équilibre des écritures transmises dans Cegid Loop. Exemple :

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472188988/0659837671b96cf331d58d643081/Capture%2Bd-E2-80-99e-CC-81cran%2B2026-05-29%2Ba-CC-80%2B16_46_37.png?expires=1788635700&signature=9fe0a7b0ec9555d9bd168fa71e5d6203ba8dc0aa9ec9be699ec4f7b8451be8bf&req=diQgFMh2lYhXUfMW1HO4zRYtrtf8hvMBcV2xDllu%2FUiBAy9xfr4AtQsGTABj%0AlXntqPEiFAMS5MOBzk0%3D%0A)

4. Journaux comptables

Associez les journaux Sellsy aux journaux comptables existants dans Cegid Loop. Par exemple :

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472188989/1677e318013b6e62d3f3d803cc0f/Capture%2Bd-E2-80-99e-CC-81cran%2B2026-05-29%2Ba-CC-80%2B16_47_07.png?expires=1788635700&signature=50260ab3903dacc622f014839a6d90338b55be382b9cbaa3fc24a77c4a585dce&req=diQgFMh2lYhXUPMW1HO4zT3oURsweKkbC9ZH2fuYZCaL6YGOaMstZ4AC5vjR%0A9beGuBKi8OfIZxeEum0%3D%0A)

Les journaux sélectionnés doivent avoir été préalablement autorisés lors du partage du dossier dans Cegid Loop.

5. Comptes comptables

Associez les comptes comptables utilisés dans Sellsy aux comptes correspondants dans Cegid Loop.

Ces correspondances permettent d'affecter correctement les écritures comptables lors de leur création.

Nous vous recommandons de vérifier la cohérence entre votre plan comptable Sellsy et votre plan comptable Cegid Loop avant de valider le paramétrage.

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472188991/9192aebac8f37d29b610adf42e35/Capture%2Bd-E2-80-99e-CC-81cran%2B2026-05-29%2Ba-CC-80%2B16_50_04.png?expires=1788635700&signature=958dffe255298eb92b779addc6b29613cb21494456ca60647ead964b8ed7f1a0&req=diQgFMh2lYhWWPMW1HO4zWvQHNP%2Bp1D6qQhSFNFITURYiXucNdJfTieDXeeD%0ARf748aWcjbonz0ez7FY%3D%0A)

6. Rabais, remises et ristournes

Si vous utilisez des rabais, remises ou ristournes dans Sellsy, vous devez également définir les comptes comptables qui recevront ces montants dans Cegid Loop en cliquant sur « **Oui** », puis sur « **Enregistrer** ».

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472188993/2998a4e57ee10523a15f8051477c/Capture%2Bd-E2-80-99e-CC-81cran%2B2026-05-29%2Ba-CC-80%2B16_51_33.png?expires=1788635700&signature=f7ca9a0930f638ecbcbfb34ebb89ac4d1c003baf04814b17b1bdc9dcb3830364&req=diQgFMh2lYhWWvMW1HO4zdP94QL0tlMEDXS8%2F%2FJ%2BA6g3s2%2FajIRwIlaLdqSi%0Ay6h4rvaljEkitmjqHec%3D%0A)

Autrement, cliquez sur « **Non** », puis sur « **Passer** ».

En cas de doute, rapprochez-vous de votre cabinet comptable ou de votre administrateur Cegid Loop.
​

### 
👉  Étape 4 : Derniers ajustements techniques

Votre connexion est maintenant configurée.

Avant d'activer l'intégration, quelques paramètres complémentaires vous permettent d'adapter le fonctionnement de la synchronisation à votre organisation comptable.

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2472188994/30c8c20400df8e175e673ec11eae/Capture%2Bd-E2-80-99e-CC-81cran%2B2026-05-29%2Ba-CC-80%2B16_54_13.png?expires=1788635700&signature=53e16c6d144c99b7b201542bff0e4930ee6b33b5b2a1d01e67239ab2eec73d0a&req=diQgFMh2lYhWXfMW1HO4zaLQxAQomdcJMsP2IeECUuZHWEry9hlJsplosFsd%0ANDaQPM%2FGFeXebQ0n3WA%3D%0A)

1. Date de début de synchronisation

Sélectionnez la date à partir de laquelle les factures/avoirs Sellsy devront être transmis à Cegid Loop.

Chaque nuit, le connecteur synchronisera automatiquement les factures et avoirs :

- ayant une date égale ou postérieure à la date sélectionnée ;
- marqués comme devant être envoyées en comptabilité.

> **Bon à savoir :**  Si vous mettez en place l'intégration pour la première fois, choisissez une date cohérente avec votre période comptable afin d'éviter l'export de documents déjà traités dans Cegid Loop.

2. Création des écritures en brouillon / attente

La création d'écritures en brouillon via API n’est pas prise en charge par Cegid Loop. Les écritures arrivent directement en comptabilité. Le choix effectué sur cette étape n’aura donc aucun impact sur la synchronisation.

> **Bon à savoir :** L'absence de création d'écritures en brouillon/attente ne signifie pas qu'une écriture ne peut pas être modifiée post-import. Elle peut être modifiée à tout moment en comptabilité. L'écriture arrivera, par défaut, en « **traitée **», mais le statut peut être modifié en « **à traiter** » post-import automatique.

3. Synchroniser les documents sans justificatif

Choisissez si les factures ou avoirs ne disposant pas de pièce jointe doivent être transmis à Cegid Loop.

- Oui : Les documents seront synchronisés même si aucun justificatif n'est associé.
- Non : Seuls les documents accompagnés d'un justificatif seront transmis.

> **Important :** Nous recommandons de désactiver cette option si votre cabinet comptable exige systématiquement la présence d'un justificatif pour chaque écriture.

4. Libellé des écritures

Définissez la manière dont les libellés des écritures comptables seront générés dans Cegid Loop.

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

Les nouvelles factures et avoirs répondant aux critères définis seront transmis à Cegid Loop avec leurs écritures comptables, leurs tiers et leurs pièces jointes associées.

> **Important : **Nous recommandons de vérifier attentivement les premiers documents transmis dans Cegid Loop. Plus une anomalie est détectée tôt, plus elle est simple à corriger. Une fois les premiers contrôles validés et les éventuels ajustements effectués, l’intégration fonctionnera de manière autonome.

___________________________________________________________

## **Questions fréquentes**

L'intégration fonctionne uniquement de Sellsy vers Cegid Loop.
Les factures et avoirs créés **[et comptabilisés](https://help.sellsy.com/fr/articles/5875018-comptabiliser-des-factures-d-achat-et-de-vente)** dans Sellsy, ainsi que les écritures comptables, les tiers et les pièces jointes associées, sont automatiquement transmis vers Cegid Loop.
Les modifications réalisées directement dans Cegid Loop ne sont pas automatiquement répercutées dans Sellsy.
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

Lorsqu'une écriture a déjà été créée dans Cegid Loop, la correction doit généralement être réalisée directement dans Cegid Loop.
Si l'erreur est liée au paramétrage du connecteur (code TVA, compte comptable, journal, etc.), nous recommandons également de corriger la configuration de l'intégration afin d'éviter que l'erreur ne se reproduise lors des synchronisations suivantes.
Dans la majorité des cas, les corrections d'écritures déjà intégrées sont réalisées dans Cegid Loop.
​

Nous recommandons de vérifier attentivement les premières factures et avoirs transmis dans Cegid Loop afin de confirmer que :
- Les comptes comptables sont corrects
- Les codes TVA sont correctement affectés
- Les journaux utilisés sont les bons
- Les tiers sont correctement créés ou rapprochés
- Les pièces jointes sont bien présentes
Plus une anomalie est détectée tôt, plus elle est simple à corriger.
Une fois les premiers contrôles validés et les éventuels ajustements effectués, l'intégration fonctionnera de manière autonome et vous n'aurez généralement plus à intervenir sur son paramétrage.
​

Lors de la synchronisation, le connecteur recherche automatiquement une correspondance existante dans Cegid Loop à partir de plusieurs critères :
- Compte auxiliaire
- Numéro de TVA
- SIRET ou numéro d'entreprise
- Nom du tiers
Si aucune correspondance n'est trouvée, un nouveau client ou fournisseur est créé automatiquement dans Cegid Loop.
​

Pour faciliter le suivi des écritures importées depuis Sellsy, nous recommandons de définir avec votre cabinet comptable :
- Des journaux dédiés aux flux Sellsy
- Une convention de libellés spécifique
- Une procédure de contrôle des imports
Cette organisation permet généralement d'identifier facilement les écritures provenant de l'intégration.
​

Les pièces jointes associées aux documents de vente et d'achat peuvent être transmises vers Cegid Loop avec les écritures comptables.
​[Lors du paramétrage de l'intégration](#h_4d0b2c848e), vous pouvez choisir de synchroniser tous les documents ou uniquement ceux disposant d'un justificatif.
​

Nous préconisons de faire intervenir votre expert-comptable pour la configuration de l'intégration. Assurez-vous qu'il dispose d'un [accès gratuit expert-comptable](https://help.sellsy.com/fr/articles/6652377-donner-un-acces-sellsy-a-mon-expert-comptable) avec un [profil d'administrateur](https://help.sellsy.com/fr/articles/5864112-profils-de-privileges).
​

La comptabilité analytique n'est pas prise en charge par cette intégration.


En cas d'erreur lors de la connexion, vérifiez :
- La clé API
- Le code secret API
Si le problème persiste, rapprochez-vous de votre administrateur afin de vérifier la configuration de l'environnement Cegid Loop.
​

Assurez-vous d'avoir bien respecté [ces étapes.](#h_b7ffaa64c0) Si le problème persiste, rapprochez-vous de votre administrateur afin de vérifier la configuration de l'environnement Cegid Loop.
​

Assurez-vous de bien avoir respecté [ces étapes](#h_e81b200b3a). Si le problème persiste, rapprochez-vous de votre administrateur afin de vérifier la configuration de l'environnement Cegid Loop.
​

 Veuillez vérifier que :
- La facture a bien été comptabilisée dans Sellsy. Les documents de vente et d'achat non comptabilisés ne sont pas synchronisés vers Cegid Loop.
- L'exercice comptable concerné n'est pas clôturé dans Cegid Loop.
- La devise de la facture est autorisée dans Cegid Loop.
- Le pays du client ou du fournisseur est autorisé dans Cegid Loop.
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
