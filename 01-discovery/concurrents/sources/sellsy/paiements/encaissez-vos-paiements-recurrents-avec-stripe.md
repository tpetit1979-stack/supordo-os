---
source: https://help.sellsy.com/fr/articles/5876314-encaissez-vos-paiements-recurrents-avec-stripe
categorie: Paiements
titre: Encaissez vos paiements récurrents avec Stripe
date_recuperation: 2026-09-05
---

# Encaissez vos paiements récurrents avec Stripe

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2200491624/6eb0928a9747535ea941e47c91f0/FAQ-Bannie%CC%80reAcademy-2+%282%29.png?expires=1788635700&signature=72ad839247499385f530d185d7c44dd006709c1caa0b4a19c0343279f3edecba&req=diInFs13nIddXfMW1HO4zVbD6FLj%2FSwDTS1xVG6g8MCiDVjDBiVLqdbAj2Ba%0ARCbe6PLK%2FSHdJ5psyeU%3D%0A)

### 


___________________________________________________________

### Avant de commencer

Pour connecter Stripe, vous devez :

- disposer d’un **compte Stripe actif**
- avoir un accès **administrateur** dans Sellsy

___________________________________________________________

### **Étape 1 : Connectez votre compte Stripe**

Pour connecter votre compte Stripe, suivez la procédure décrite dans l'article suivant : [Activer le paiement en ligne avec Stripe ](https://help.sellsy.com/fr/articles/5876284-activer-le-paiement-en-ligne-avec-stripe)

___________________________________________________________

### **Étape 2: Paramétrer les paiements par empreinte de CB**

Par défaut, les prélèvements Stripe ne sont pas activés, les paiements sont possibles mais sans enregistrement d’empreinte de CB.

Deux méthodes sont possibles pour activer les prélèvements :

- Au niveau du paramétrage général dans** *"Menu" > "Réglages" > "Paiement en ligne" > "Options de paiement pour vos clients"***
​
![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2171645387/bcc031996dc5ef35505e556bc9e4/Screenshot+2026-03-16+at+14_35_02.png?expires=1788635700&signature=919b2baa94af8439e42838e35c7b7217c01bcac425c7eac2946db4ed1667d23c&req=diEgF896mIJXXvMW1HO4zbxDQzH9xiL5oKecgZ%2FNwh7x4gJTHL1ohipZpqjq%0AqvmP%0A)
![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2171645027/75c498519f6fb6d65006efb6b595/image.png?expires=1788635700&signature=8a7c85ab5b75f9704f19f545f1b07b5f478ef6eebd790b59749ea996ceb6ed80&req=diEgF896mIFdXvMW1HO4zdBM%2ByZ8eCmemQ1o1QVbJpLlGtZ3NwlnYQfmnI%2Fv%0AVaeq%0A)
Si cette case est cochée, les prélèvements par carte bancaire seront automatiquement activés sur toutes les nouvelles factures.
- Au niveau **des factures** : dans les réglages d’une facture vous pouvez activer ou désactiver les prélèvements.

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2171647960/d47260c53b4a995de906d7d921f6/image.png?expires=1788635700&signature=fc4426235ebc1cf874c0503932d32883a7c873226b04cd96e8fefe9efd45d7e5&req=diEgF896mohZWfMW1HO4zWdYlHc6UuvtV8LzcyKrA1aMrwgMup1oSjelTXnj%0A80wADRdGg85hv6n4T0s%3D%0A)

___________________________________________________________

### **Étape 3 : Récupérer l’empreinte de carte bancaire du client**

Les prélèvements Stripe sont effectués **avec la carte bancaire du client**. Ses informations de carte sont stockées de manière sécurisée chez Stripe et réutilisées au moment de procéder au prélèvement.

**Option 1 :** Permettre l'enregistrement de la carte au premier paiement
Les informations de paiement du client seront enregistrées dès lors qu’il paie sa première facture avec Stripe.
​

> **Attention :** il faut bien avoir **activé le paiement récurrent avec Stripe** sur cette facture. Dans le cas contraire, l’empreinte de CB ne sera pas enregistrée.

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2171657853/2c7510246b6a3fea8c11e31caece/image.png?expires=1788635700&signature=7ab6a4f45ce1d395a933abc8129ae5d93a4f8da0ce2488082ca63ab52724472e&req=diEgF897molaWvMW1HO4zbi09knUTVVlsiw10MSAeJy%2F5B5e6D3byCkFn%2FJ7%0A20PGvC0mxRd3e3UQ4OM%3D%0A)

**Option 2 :** Inviter votre client à renseigner ces infos de carte
Sur le détail de votre facture, un nouvel onglet *“Prélèvements Stripe”* apparaît.

Depuis cet onglet vous pouvez inviter le client à utiliser le prélèvement automatique.

![](https://sellsy-a9cc78fb6d3a.intercom-attachments-7.com/i/o/446313402/457c8f436ec5c15f73493f28/946df82f-1068-4458-94d8-4347450badb0-6e624ac6-4838-42ad-8429-bdce78d42b59.?expires=1788635700&signature=c109f2638e4f5ba75ad703730a29a30d2b79c462df32ea74b6952903343de308&req=cCQhFch9mYFdFb4f3HP0gF0zzMWXb7wPUN9tp860xB619VtRhE8g5OKZBmXN%0AvkEPQbX5TTQRbVWOBw%3D%3D%0A)

 Il recevra un **email d’invitation** ainsi que le **lien pour payer la facture en ligne**. Une fois qu’il aura payé sa facture vous pourrez réutiliser ses informations de paiement pour les prélèvements.

___________________________________________________________

### **Étape 4 : Programmer un prélèvement par carte**

Dans l’onglet *“Prélèvement Stripe”* de votre facture, vous pouvez maintenant programmer votre prélèvement à la date souhaitée.

![](https://sellsy-a9cc78fb6d3a.intercom-attachments-7.com/i/o/446313407/a563426fccbf461d90b05a16/mpyVT3X3mbbTvAlERE4ES2erY2UhOyQZUowqsIzTalURSbw72GnM5XiK3EF-HzysxRH1ioMWFZw8MHiRlNZ9-lPx5dLM3z6zKr4E2id4X2JX_OInDmnWW8Q0a9zZz4hOBUiPAZ8_?expires=1788635700&signature=32e0e2e3e90d29dbc1a4689d3ca9587137784aaf38bd983bc2aa0e0c8b14d560&req=cCQhFch9mYFYFb4f3HP0gKf5J7hbiGO6sXs93VtOPFiiYDJyjcAVnuLA0DTF%0Am2YcyH4%2BtnYZ7%2FoL1A%3D%3D%0A)

Une fois le prélèvement programmé, celui-ci apparaît au statut *“en attente”* dans la liste des prélèvements.

Vous pouvez **annuler un prélèvement** tant qu’il est au statut *“en attente”* (clic droit sur la ligne du prélèvement > annuler).

En choisissant le délai de paiement *“plusieurs échéances”* vous pouvez programmer un prélèvement pour chaque échéance de paiement.

![](https://sellsy-a9cc78fb6d3a.intercom-attachments-7.com/i/o/446313410/0f1650ab0ec43c8ca943c6f8/d75c53e7-d201-48fb-bd5d-8826ba3dbd7d-bd3207df-3cec-4013-a9dd-ed4dd3ff4ee5.?expires=1788635700&signature=7c51f86766ac4526f90fd1fa64d5dcd82124dfbe6f5bd74fc95d7eebc7c0d62f&req=cCQhFch9mYBfFb4f3HP0gP0EyVGlhF3wRX1zxiWv7tJcqKNw6dotUChkjWZ9%0ApKOhYuwYeHFstyda1Q%3D%3D%0A)

___________________________________________________________

### **Activer le prélèvement automatique pour le règlement de vos factures d’abonnements**

> **Bon à savoir :** avant de commencer la création d'un abonnement, vous devez avoir un modèle de document avec le module de prélèvement Stripe activé

Pour commencer la création de l'abonnement, sélectionnez le modèle de document sur lequel les prélèvements Stripe sont activés, ainsi qu’un client dont l’empreinte de CB est déjà enregistrée. Le mode de génération de l’abonnement doit être en automatique.

![](https://sellsy-a9cc78fb6d3a.intercom-attachments-7.com/i/o/446313412/770dafee0dcf01f8b8bcd237/40170506-a01b-4493-bc41-e16f86fbb2e4-09f5380d-8f36-4870-abf3-70e6ec3eb4d5.?expires=1788635700&signature=52ea8a4c64ed40ec7b3ba0c7b7b84d2bc67257fd17315be5d0c18c542fce9199&req=cCQhFch9mYBdFb4f3HP0gPVlO%2BFbn00hPE%2FyDRXl0l0U5LHiN8XrqiRIC5HR%0ALqvhjIuDMStRrr8U8Q%3D%3D%0A)

Un nouveau bloc *“prélèvement automatique”* apparaît, cocher *“Activer”.* Deux options sont possibles pour la date de prélèvement de vos factures d’abonnement :

- **à l’échéance** de la facture issue du modèle. Le prélèvement sera effectué à la date limite de paiement spécifié sur le modèle.
- **à la date de génération** de la facture issue du modèle. Le prélèvement sera effectué au moment de la génération de la facture.

___________________________________________________________

### **Consulter la liste des prélèvements**

Vous pourrez retrouver la liste de tous vos prélèvements depuis le menu *"Banque" > "prélèvement Stripe"*

![](https://sellsy-a9cc78fb6d3a.intercom-attachments-7.com/i/o/446313414/81cab586ec892dab1ac29808/1ce71154-ab39-408e-8fce-ff9a8e4e9945-2354b001-bdb8-4779-aa2b-b85308306c37.?expires=1788635700&signature=3d3b45ee8c9224a83fcecda81b2e32d5dd93f1888d4118ea516ea19f297246c0&req=cCQhFch9mYBbFb4f3HP0gETMpXw%2B1qGlP%2BmI%2F8SXD5APBcKsqtbeE9B73HP%2F%0AtBWLMYoWk22QYZBVZw%3D%3D%0A)

### 

___________________________________________________________

### **Supprimer les informations de paiement d’un client**

Votre client peut supprimer ses informations de paiement depuis son espace client :

![](https://sellsy-a9cc78fb6d3a.intercom-attachments-7.com/i/o/446313420/b90a0a2be709a36fd0844a7d/8c-DRrOt6RznI-5xwiY0l2GpA1knkPP1PLk4HW96cyDOy1MpwDO86iaeLLzRqqS8JjV0vVqbFaZ1Sn_9ALANgiJuW6nkLrLvpqbmR6Wp3Oc__sGE0VjF9Ta3hOC9YL8kSnKqGEuy?expires=1788635700&signature=7fa97ffca15cd88ce8f4ec54240f7bdfd46b61a6e6a256426332fb8671f0877c&req=cCQhFch9mYNfFb4f3HP0gFprDoUhcBu%2Fct0LuYvscRChJHjSS3w2FLnc%2FrE9%0ADKlVBi3%2FlrXRokwBeQ%3D%3D%0A)

Vous pouvez aussi **supprimer ses informations** depuis la fiche détail de votre client, dans l'onglet *"Comptes et cartes bancaires" :*

![](https://downloads.intercomcdn.com/i/o/870036265/4a5fc9a8be5165007fd4e6fd/Comptes+et+cartes+bancaires.png?expires=1788635700&signature=663ffedf8c664940be5c386c628017d3493ec8611846e1b566e21c6194ed72b0&req=fCcnFsp4n4daFb4f3HP0gBo81nrfhGu1PesXuMrH8T5nFHjEIAFO9ZVaKwQm%0ACWf0QZOWUjAwuo7syg%3D%3D%0A)


​

Mis a jour le : 25/03/2026
