---
source: https://help.inter-fast.co/fr/articles/11571129-automatiser-les-demandes-d-avis-clients
categorie: Outils
titre: Automatiser les demandes d’avis clients
date_recuperation: 2026-09-05
---

# Automatiser les demandes d’avis clients

> 📣 Gagnez du temps et récoltez plus d’avis clients sans lever le petit doigt.
> Grâce à l’intégration entre InterFast et vos outils d’avis, vos demandes partent automatiquement après chaque facture payée. On vous montre comment activer ça en quelques clics.

> 💡 Disponible avec votre abonnement ? L'automatisation des demandes d'avis fait partie des abonnements Pro et Business (elle s'appuie sur le module Automatisations).
> 
> Starter — non inclus
> Pro — ✅ inclus
> Business — ✅ inclus
> 
> 🧪 Le module Automatisations est actuellement en bêta : encore en évolution, quelques ajustements sont possibles.
> 👉 Pour vérifier ou changer votre plan : rendez-vous dans [Mon Abonnement](https://app.inter-fast.fr/dashboard/company?c=billing).

## I. Demande d’avis Eldo

## A. Vidéo tutoriel d’Hedi

[Vidéo]()

## B. Étapes détaillées

### 1. Créer une nouvelle automatisation avec le modèle “Demande d’avis Eldo”

Nous allons voir ensemble comment mettre en place l’intégration entre nos deux solutions, qui permet de transmettre automatiquement à Eldo l’information indiquant qu’une facture a été réglée. Une fois le paiement confirmé, Eldo pourra à son tour déclencher l’envoi de demandes d’avis au client final.

Pour commencer, direction le module des [Automatisations](https://app.inter-fast.fr/dashboard/automations/definitions).

Vous allez pouvoir **créer une nouvelle automatisation** en utilisant le modèle prêt à l’emploi “Demande d’avis Eldo”.

![](https://downloads.intercomcdn.com/i/o/tarury57/1573087317/5f2c3ee4f3a4f427acac840638af/Google+Chrome+2025-06-16+14_00_03.png?expires=1788619500&signature=a953fab1afe3523a945b0f0e0c4f35a8dd740cf40c272fadbcb170f27b0f7451&req=dSUgFcl2moJeXvMW1HO4zYuqCgEp4cu1mvcn8DvqoY5nheIxWPea9z%2F%2B6E6v%0APdLwxC7d4%2FFuAZOyJ%2Bw%3D%0A)

![](https://downloads.intercomcdn.com/i/o/tarury57/1573087733/2a862b3814e7458c3f44020ab1ee/CleanShot+2025-06-16+at+13_58_45%402x.png?expires=1788619500&signature=5f7e131d0a1a39138906be3f2a73100acc5f90401d0a5dd47ac71791b8536f9a&req=dSUgFcl2moZcWvMW1HO4zUpiCjUPeWPd78iMp9Iwy8HTlGBDVp2ZMdM5AUVE%0Ax0tBcBTE%2BqtZTSG079Y%3D%0A)

✅ Ce modèle est déjà pré-paramétré et il vous suffit de le personnaliser avec vos informations.

![](https://downloads.intercomcdn.com/i/o/tarury57/1573089309/98247368858a459abdbcf2826075/CleanShot+2025-06-16+at+13_59_08%402x.png?expires=1788619500&signature=4ac0d1bcfafc66702c1f74b6c3eaf587a05f79161f17281dcc80f147a40bc614&req=dSUgFcl2lIJfUPMW1HO4zekhb6ou0Fj%2FNSB%2B6vuspLJysu6i3q6YxFqQIurc%0AhHGxpxxe5ZLV90PIz2Q%3D%0A)

### 2. Ajouter la clé API fournie par Eldo

Une fois l’automatisation créée, vous devez **renseigner la clé API** que vous a transmise Eldo.

Cette clé permet à InterFast de communiquer automatiquement les données pertinentes avec la plateforme Eldo.

![](https://downloads.intercomcdn.com/i/o/tarury57/1573090078/18062b91efb7290de43c3e54cd2f/CleanShot+2025-06-16+at+13_59_18.png?expires=1788619500&signature=395678b934a2557e3950c10de1d3e0d6c51de2294113d1f85cf14ed7157901b5&req=dSUgFcl3nYFYUfMW1HO4zYHQLEy4%2FIyPck4Fkalj6EE55urGV987GekI7WFr%0A8oo8%2Bhpy9ZoiH8rx6vw%3D%0A)

⚠️ Pensez à bien copier-coller la clé API sans espace ni caractère supplémentaire.

### 3. Facturer un particulier

Ensuite, continuez votre process habituel :

- Créez une facture à destination d’un client particulier.
- Validez la facture et passez-la au statut "*Payée*".

```
💡 C’est bien passage au statut "Payée" qui déclenchera l’automatisation.
```

![](https://downloads.intercomcdn.com/i/o/tarury57/1573107641/a228d086e65af09f09f1858fb17a/CleanShot+2025-06-16+at+14_13_39%402x.png?expires=1788619500&signature=8e76675f966058a5f7437fe5b5e47e97b9b0a35a3fccdab2c0f700efe0800071&req=dSUgFch%2BmodbWPMW1HO4zZrfaWrklPy5Jj%2FwA68jfUqPvaRZ47WmjWBGFLmB%0AiE2A39%2BLTf1PJ9uh%2BKI%3D%0A)

### 4. Vérifier dans Eldo que le contact a bien été transmis

Vous pouvez ensuite vous rendre sur votre [compte utilisateur Eldo](https://www.eldo.com/compte-pro/reviews-management?status=ALL&offset=10&search=contact&sortOrder=DESC).

Tapez le nom du client associé à la facture payée dans la barre de recherche. 

Vous devrez retrouver les informations suivantes :

- son nom et prénom
- son email
- son numéro de téléphone
- la date des travaux, qui correspond à la date d’émission de la facture

L’objectif est de s’assurer que tout est bien transmis pour que la demande d’avis parte automatiquement.
​

## II. Demande d’avis Bilik

Comme pour notre partenaire Eldo, vous pouvez également récolter vos avis avec notre partenaire Bilik.

### A. Étapes détaillées

### 1. Créer une nouvelle automatisation avec le modèle “Demande d’avis Bilik”

Nous allons voir ensemble comment activer l’intégration entre InterFast et Bilik. L'automatisation informera Bilik qu’une facture a été payée. Une fois cette notification reçue, Bilik se chargera d’envoyer une demande d’avis au client final.

Pour commencer, ouvrez le module **Automatisations** depuis votre interface InterFast.

Créez une nouvelle automatisation en sélectionnant le modèle prêt à l’emploi **“Demande d’avis Bilik”**.

![](https://downloads.intercomcdn.com/i/o/tarury57/1573209645/e596e910a544145c026b153ccec0/Google%2BChrome%2B2025-06-16%2B14_00_03.png?expires=1788619500&signature=2b527514a307fadecf778c452008a99c3abaef5473902364d01e3598c389d03d&req=dSUgFct%2BlIdbXPMW1HO4zU3I26gcwJnISYFZ%2FnTae1a%2FP8lKQQp1IzXdVD3g%0AFYsujarunOsjHwXMuqg%3D%0A)

![](https://downloads.intercomcdn.com/i/o/tarury57/1573211006/41870aed056224fe5c93f612368e/CleanShot+2025-06-16+at+13_58_45%402x.png?expires=1788619500&signature=1072f04ae204a60d38c4c1b7432616641d985d711638113aadcb4857c27039de&req=dSUgFct%2FnIFfX%2FMW1HO4zUEReHfzQ0cQ3gYbyiNZQU7cu8nNfC4lZbcy2DV1%0Aorvgx1aIGT7nRLshjE4%3D%0A)

 
✅ Ce modèle est déjà configuré avec les bons déclencheurs (paiement de facture) et l’action correspondante (envoi d’une notification à Bilik).

![](https://downloads.intercomcdn.com/i/o/tarury57/1573213903/7675dc05ef86fba9ae141f926fd9/CleanShot+2025-06-16+at+15_17_57%402x.png?expires=1788619500&signature=7ee7ffe8720495aa0967d2edc9b751d9a0346bc0c93bc9257fd7a6f98736b618&req=dSUgFct%2FnohfWvMW1HO4zadSHyYcctNibelEFN5MKmrwo%2FJgU0hFht1E9aNM%0AxEqA2pwVf0OzQnyZszE%3D%0A)

### 2. Ajouter l’URL fournie par Bilik

Voyons ensemble comment paramétrer l'envoi de la demande d'avis : 
​

![](https://downloads.intercomcdn.com/i/o/tarury57/1573254952/09ae66ebe19b4a9541f7560f492c/CleanShot-2B2025-06-16-2Bat-2B15_19_01-402x.png?expires=1788619500&signature=4016691824dfe98ffd4f077d369735abac8cc9578ee0aa0020735e795be4c3b9&req=dSUgFct7mYhaW%2FMW1HO4zfgYk4Fs3kAeaqM8kLOMqzVv8QW4JVvUxgWJxfIK%0AMGcUu%2FKORk%2FISoPwbdc%3D%0A)

Dans le champ **URL**, vous devez coller l’adresse fournie par Bilik.
Cette URL permet à InterFast d’envoyer automatiquement les informations de contact du client à votre compte Bilik.

![](https://downloads.intercomcdn.com/i/o/tarury57/1573220755/93e6a6a483c61ac865109432418b/CleanShot+2025-06-16+at+15_20_15%402x.png?expires=1788619500&signature=25da6389dac3a6e14fd2dbd38bf326646b318792d8103e775b9baa7e0aa66e2b&req=dSUgFct8nYZaXPMW1HO4zYnzbOs835JnvWh7IsfyMecFGjebSRa913PuF%2BRf%0A8KC0PFkbX9ri%2Bt5drhA%3D%0A)


⚠️ Pensez à bien copier-coller l'URL sans espace ni caractère supplémentaire.

### 3. Vérifier les données envoyées automatiquement

Bonne nouvelle : les données à envoyer sont déjà pré-remplies ! 

![](https://downloads.intercomcdn.com/i/o/tarury57/1573218128/2f9fd7c1444c670c83def62531cc/CleanShot+2025-06-16+at+15_20_23%402x.png?expires=1788619500&signature=9d160c59a8bd0770b85af3c08ff6b0f6c9b8c9a21357fa2b05d41e18d80825ee&req=dSUgFct%2FlYBdUfMW1HO4zTn6ysRLLAF8ktM7h9zDOAa4HzGbh7PvnIA%2B86ix%0AWWvabL2%2FfURTZdt4FdU%3D%0A)

Les champs **firstName**, **lastName** et **email** sont automatiquement liés aux informations du contact principal de la facture.


⚠️ Il est important de ne pas modifier ces champs, car la configuration a été réalisée en amont par notre équipe technique.

### 4. Ajouter des en-têtes HTTP (optionnel)

En complément, vous pouvez ajouter des en-têtes HTTP, notamment si Bilik vous a transmis des UTM spécifiques (ex. : pour identifier une source, une campagne, etc.).

Ces en-têtes peuvent contenir :

- du texte statique (ex. : campagne = juin2025)
- ou des variables dynamiques, issues de la fiche client ou de la facture

Ces UTM serviront à : 

- suivre les performances des demandes d’avis par canal
- segmenter les retours clients dans un outil externe

Ils sont optionnels, mais très utiles si vous souhaitez avoir une analyse fine du parcours client !

![](https://downloads.intercomcdn.com/i/o/tarury57/1573224010/21debdb92c44d7bad930ea229472/CleanShot+2025-06-16+at+15_22_51%402x.png?expires=1788619500&signature=a5b93e70780153156b8ae5f966feb877dd2e79b6c0143e2b773fd9e3ce74bba4&req=dSUgFct8mYFeWfMW1HO4zcMjcldzPbYJtp%2Bcvl8HzyWmt1%2BUstP1VOrXKH5U%0AdRKzZoTypNZUiZjWtg0%3D%0A)

### 5. Envoyer une facture payée pour tester l’automatisation

Comme pour toute automatisation liée à la facturation :

- Créez une facture à destination d’un client particulier
- Une fois payée, passez-la au statut **“Payée”**

```
💡 C’est bien passage au statut "Payée" qui déclenchera l’automatisation.
```

## III. Demande d'avis Google

InterFast permet également d'envoyer une demande d'avis Google par email / sms au travers de ses automatisations.

Voici les étapes à suivre.

### A. **Création d'un lien d'avis Google My Business**

1. Depuis votre ordinateur, connectez-vous à [Google My Business](https://business.google.com/fr/business-profile/)
2. Rendez-vous sur la fiche de votre établissement
3. Cliquez sur “Accueil” dans le menu présent à gauche.
4. Cliquez sur “Recevoir d’autres avis”.
5. Copiez l’URL courte.

> 💡 L'URL courte doit ressembler à ceci :
> ﻿​[https://g.page/r/CZyZx1IEBVLlEAE/review](https://g.page/r/CZyZx1IEBVLlEAE/review)

### ** B. Partage du lien Google My Business**

1) Accédez au [module Automatisations](https://app.inter-fast.fr/dashboard/automations/definitions)

2) Créez une nouvelle automatisation (sans modèle)

![](https://downloads.intercomcdn.com/i/o/tarury57/1935996416/0c5a7826229509e54871b6eac293/CleanShot+2026-01-13+at+08_24_52%402x.png?expires=1788619500&signature=2718e3a16bd7099330d1abce7a7a4773ebeaa30b50ae8e97b4af2a5cc78f4016&req=dSkkE8B3m4VeX%2FMW1HO4zQaRhVJUqgz%2BDOB7gYUnkpP9hQI7MIEPT%2BDcEB0N%0AaI76iWwdr13BYD728ck%3D%0A)

3) Choisissez "Facture" comme type d'automatisation

![](https://downloads.intercomcdn.com/i/o/tarury57/1935999755/fbf233c764e8de04d3eff3d4eb8b/CleanShot+2026-01-13+at+08_26_49%402x.png?expires=1788619500&signature=752ef57dc2f215bb0456120ec8045c6f5a8e29043fc4da31758517b812e0cdba&req=dSkkE8B3lIZaXPMW1HO4zVPOOWxqiNcrh78vBNOlZQPk5k5OHm6ihgDojSCT%0AOq3j7HgRnAwcE51PMqA%3D%0A)

4) Nommez votre automatisation pour y retrouver plus facilement

![](https://downloads.intercomcdn.com/i/o/tarury57/1936001730/b86054d1b5bf187cfd338c80c303/CleanShot+2026-01-13+at+08_27_22%402x.png?expires=1788619500&signature=91abd3b47756052500be6949b2726d584f698b96ee3748b7749aaf4fc26d15aa&req=dSkkEMl%2BnIZcWfMW1HO4zQQ1OJE4BxT6YiHbp3OjcQxlUtHr3uiFkpgDberk%0AD7ZedhNJHyNWqY%2FjObc%3D%0A)

5) Choisissez la valeur "La facture est payée" comme déclencheur automatique


![](https://downloads.intercomcdn.com/i/o/tarury57/1936003976/afdeac5c69e987767d4433a4004c/CleanShot+2026-01-13+at+08_28_25%402x.png?expires=1788619500&signature=bedffca7dd38eb2dcaf1180095e619c72f0bee5954788ebcfbfbe1f5be71532c&req=dSkkEMl%2BnohYX%2FMW1HO4zbRPzRGmi8FWO4Sfi2QxHl26rQLMA1y%2BMSv06L41%0AmG2hEcZRD%2BLCxuEwuV4%3D%0A)

6) Créez une étape d'envoi d'email / sms

![](https://downloads.intercomcdn.com/i/o/tarury57/1936006044/e9761a99f8b14575f793ad13d635/CleanShot+2026-01-13+at+08_29_36%402x.png?expires=1788619500&signature=d16d83c2a57e4dbe5707eb87895e33e6d18613b3116d70571d31f195d86c7293&req=dSkkEMl%2Bm4FbXfMW1HO4zdOsnO4Fujyeam7RAGbT%2BB%2BeL6k%2FVHVGq6DZnN8L%0AUh8iUgopMKC8Rcspux4%3D%0A)

7) Intégrez votre lien Google My Business

![](https://downloads.intercomcdn.com/i/o/tarury57/1936013956/c95c905c6c10f042b239bab2c415/CleanShot+2026-01-13+at+08_31_27%402x.png?expires=1788619500&signature=4293288b9ed7574ced1af61addb3cd78da1c9030260d004df788eb0597ca62ac&req=dSkkEMl%2FnohaX%2FMW1HO4zSMC5awh%2BmDEK8tnRI1lp4fcKzBmkMiMLxF%2Ft7cF%0AG4f43RlcKyzYOeTk5pc%3D%0A)

8) Choisissez "La facture payée" comme condition d'arrêt

![](https://downloads.intercomcdn.com/i/o/tarury57/1936235258/754cb85f405fa048d9eb20bbc639/CleanShot%2B2026-01-13%2Bat%2B09_59_36-402x.png?expires=1788619500&signature=76e9f385d0457633922d19fa65c452a76a07c10b4770fb0de043930bcae3885b&req=dSkkEMt9mINaUfMW1HO4zeuob1ZO2Hk8%2B%2BC27Q%2B%2FuxFOQOB0XJ5AxLgKvCQM%0AIFAfGATT25GhNDSrHdo%3D%0A)

> 💡 L'automatisation ne s’exécute qu’une seule fois. Concrètement, dès que la facture passe au statut **Payée**, l’e-mail est envoyé automatiquement au client, puis l’automatisation s’arrête. Elle ne renverra pas l’e-mail une seconde fois.

9) Activez l'automatisation

![](https://downloads.intercomcdn.com/i/o/tarury57/1936020018/e46bd299d3b567b909f1fb4e4a3a/CleanShot+2026-01-13+at+08_36_08%402x.png?expires=1788619500&signature=9c0f20b003be74a0c2633fb23055edd68b20a09e3e93984e214281dfea6f46f2&req=dSkkEMl8nYFeUfMW1HO4zd6B%2BG%2FMCSJoZfcth8infKALSfZZQgy%2Fll3Pu2z8%0AxrzV667IZDgWLTSyv7Q%3D%0A)

Et le tour est joué ! Votre automatisation est prête.
​

![](https://downloads.intercomcdn.com/i/o/tarury57/1936020853/3a977c5c69c83a61ecb7e615cf47/CleanShot+2026-01-13+at+08_36_32%402x.png?expires=1788619500&signature=b1a954aba058c16b934bc2e9543dac6120a5bd8e5a9aa94c27173d488cfcbd7c&req=dSkkEMl8nYlaWvMW1HO4zS79TyG92juaaNB6upnCcKzWtdvBTtK2GC1a%2F33%2F%0AH0bSIcEfwaMLoLlHaiI%3D%0A)

> 💡 L’automatisation ne s’exécutera qu’une seule fois.
> 
> Concrètement, dès que la facture passe au statut **Payée**, l’e-mail est envoyé automatiquement au client, puis l’automatisation s’arrête.
> Elle ne renverra pas l’e-mail une seconde fois.

___________________________________________________________

Avec ces  automatisations pour les plateformes Eldo, Bilik et Google My Business, vous gagnez un temps précieux tout en boostant efficacement vos avis clients.

Chaque demande d'avis part au bon moment, sans oubli, et de manière personnalisée. Vous maximisez ainsi vos chances de récolter un avis 5⭐ et d'améliorer votre visibilité auprès de clients potentiels !

Mis à jour le : 05/08/2026
