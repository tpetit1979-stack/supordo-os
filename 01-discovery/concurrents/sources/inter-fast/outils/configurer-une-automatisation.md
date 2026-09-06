---
source: https://help.inter-fast.co/fr/articles/12599455-configurer-une-automatisation
categorie: Outils
titre: Configurer une automatisation
date_recuperation: 2026-09-05
---

# Configurer une automatisation

> 💡 L'objectif est simple : faire en sorte que le logiciel travaille pour vous. Que ce soit pour relancer un devis en attente, envoyer un SMS de confirmation de passage ou créer un chantier dès qu'un devis est signé, l'automatisation garantit qu'aucune étape de votre relation client n'est oubliée.

## I. Étapes détaillées

### A. Étape 1 : Choisir son déclencheur (Le "Quand")

1. Rendez-vous dans le menu Automatisations puis cliquez sur le bouton de lecture ▶️ pour accéder à la configuration.
2. Dans la zone A (Déclencheur), choisissez l'événement qui lancent l'action (ex: "Quand un devis est envoyé").
3. Utilisez les Filtres (B) pour affiner (ex: uniquement pour certains types de clients ou de montants).

![](https://downloads.intercomcdn.com/i/o/tarury57/1945200355/c6798a1c8e5e2a4203fb332c8ac8/Capture-2Bd-E2-80-99e-CC-81cran-2B2025-04-07-2Ba-CC-80-2B11_46_19.png?expires=1788674400&signature=70bdb025ac83e3044b3b5e7e7cd4870fa03cbc8d2e2bea0b3128c0406113dd4b&req=dSkjE8t%2BnYJaXPMW3nq%2BgTlHtvHrwmL9F77%2FthONBsaBBDnuvpGj3%2FnfAvqP%0AZJ%2FnqI49M17HjI0y%2FS0R1TxZky4%3D%0A)

### B. Étape 2 : Définir les étapes du scénario (Le "Quoi")

Au centre de votre écran, vous allez construire votre parcours :

1. Cliquez sur + Ajouter une étape.
2. Choisissez l'action à réaliser (Envoyer un email, un SMS, ou créer une tâche interne).
3. Astuce métier : Pour les relances de devis, vous pouvez définir un Délai (ex: envoyer le mail 7 jours après l'envoi initial).

![](https://downloads.intercomcdn.com/i/o/tarury57/1945204633/c29bbb789dd5abdea27b03edbaf7/CleanShot+2026-01-15+at+16_31_52%402x.png?expires=1788674400&signature=91092da71715c734b47a789f044f0d878ded371e357ed5982161211644522426&req=dSkjE8t%2BmYdcWvMW3nq%2BgWYrh4ku5EpXTX3JRTXDgxzosV8IWVw243%2FhC5%2FA%0AjrnnWF8r3PqTWHBzCIyn1GWJcvA%3D%0A)

### C. Étape 3 : Sécuriser l'arrêt de l'automatisation

C'est une étape clé pour ne pas paraître insistant auprès de vos clients :

1. Dans la zone C (Stopper automatiquement lorsque), indiquez la condition de fin.
2. *Exemple type :* "Si le devis est signé", l'automatisation s'arrête immédiatement pour ne pas envoyer de relances inutiles.

![](https://downloads.intercomcdn.com/i/o/tarury57/1945208278/87cd2b4fc5551c8936d71645fb38/CleanShot+2026-01-15+at+16_39_39%402x.png?expires=1788674400&signature=d96b3a7e1c706e7155ef50265404936154fbfdfbf8167296efb5907930e43818&req=dSkjE8t%2BlYNYUfMW3nq%2BgZPbPIJqghN4grtBBxNwt4T4Rt1rBprh7kv9HsnM%0AUCt8cIKlRSl8cCl2rJjkjfmw%2F%2Bo%3D%0A)

### D. Étape 4 : Activation et Sauvegarde

1. Vérifiez que la case Activer l'automatisation (D) est cochée si vous voulez qu'elle soit opérationnelle tout de suite.
2. Si vous avez plusieurs automatisations sur un même objet (devis, facture, intervention, etc.), pensez à cocher la case "Autoriser plusieurs automatisations en parallèle".
3. Cliquez sur Sauvegarder en haut à droite pour valider votre scénario.

![](https://downloads.intercomcdn.com/i/o/tarury57/1945219610/0eaaf39a86f9b3ea087776caa475/CleanShot+2026-01-15+at+17_50_27%402x.png?expires=1788674400&signature=280e5c692435e0c805ab1f2a57df050cbe38e940527993fe30cce538ea205579&req=dSkjE8t%2FlIdeWfMW3nq%2BgRclQHa0OQj9r0lBJTjrKqJ%2FtW6HDxFj1WTCOg0R%0AryiDFMk9Cd%2FDpHM9BHrii7UfwlE%3D%0A)

### 💡 Quelques conseils pratiques

- **Le test avant tout :** Utilisez le Mode Test du logiciel pour tester vos automatisations avec de faux clients avant de les lancer réellement. *(Vous pouvez demander l'activation du mode test cette à l'équipe Care directement depuis le tchat).*
- **Relances intelligentes :** Personnalisez vos emails en insérant des variables (Nom du client, numéro de devis) pour garder une image professionnelle et humaine.
- **Attention aux maintenances :** Pour l'instant, privilégiez les rappels de maintenance en interne plutôt que vers les clients pour garder un contrôle total sur votre planning.

## II. Exemple de modèle prêt à l'emploi : Devis accepté ➔ Chantier + Facture d'acompte

Passons à la pratique avec un modèle déjà préconfiguré dans vos automatisations. Dès qu'un devis est accepté par votre client, il enchaîne la création du chantier puis la génération de la facture d'acompte.

![](https://downloads.intercomcdn.com/i/o/tarury57/2648920223/d05292ee6ad18ea27734f1a6583b/CleanShot+2026-09-03+at+16_14_58%402x.png?expires=1788674400&signature=2996f3cce2c3382ed89dd4fc42a4c33b8d7e13ec3db73171030e6a197f1cb397&req=diYjHsB8nYNdWvMW3nq%2BgVJZc4WIyCrmDMVvx2NgcfiLLvB2B%2B07GjWYWbxK%0Ar6hr9Sufh70jQuplOFTDi0zQ4cE%3D%0A)

A. Pré-requis

Avant d'activer ce modèle, assurez-vous d'avoir :

- Un rôle **Administrateur** ou **Propriétaire** (seuls ces deux rôles peuvent configurer les automatisations).
- Un devis à faire accepter par votre client, **comportant des conditions de paiement avec un acompte** — c'est ce qui permet la génération de la facture d'acompte.

B. Créer l'automatisation à partir du modèle

1. Ouvrez le menu **Automatisations → Automatisations**, puis créez une nouvelle automatisation.
2. Dans la fenêtre « Nouvelle automatisation », sous « Choisissez votre modèle », sélectionnez **« Devis accepté ➔ Chantier + Facture d'acompte »**, puis cliquez sur **C'est parti !**.
​
![](https://downloads.intercomcdn.com/i/o/tarury57/2650826989/54fbb78d8234d10e0fca23659958/CleanShot+2026-09-04+at+12_30_23.png?expires=1788674400&signature=a2c63ae4a45fbe21032b067b001b3e8838504ce05e2217ca7385509c448dbe20&req=diYiFsF8m4hXUPMW3nq%2BgeAdRi0agveOmcG5ACRXvm7V7zG8ANYDcBi%2BNuYT%0ASgOK%2Bs7VROFZ%2BBoWQZWugowf%2BTw%3D%0A)

L'automatisation s'ouvre préremplie, en deux parties :
​

![](https://downloads.intercomcdn.com/i/o/tarury57/2650808090/ece3f6be87c91fbe510a0b71374d/CleanShot%2B2026-09-03%2Bat%2B16_25_23-402x.png?expires=1788674400&signature=72346cdea6a2e80e6aea4add8ef5ff5dc9c008e91066f45212a242210f155737&req=diYiFsF%2BlYFWWfMW3nq%2BgVBCSrz8%2BwYqIQq%2FexkrwqR4ezTekW0z0a8LSrPO%0ATXEuQEderWwmuQHSbz0kugKI83s%3D%0A)


​**a) Les étapes du scénario** (au centre), déjà en place :

- **Créer le chantier** — crée un nouveau chantier et l'associe au devis accepté.
- **Créer la facture d'acompte** — génère la facture d'acompte du devis et la rattache au chantier.

Cliquez sur une étape pour la paramétrer. Chaque étape propose une option **« Délai »** (désactivée par défaut) : activez-la si vous voulez que l'action s'exécute un certain temps **avant ou après** le déclenchement. Vous pouvez aussi ajouter d'autres étapes avec **« + Ajouter une étape »**.
​

**b) Les réglages de l'automatisation** (panneau de droite) :

- Nom et Description (préremplis).
- Déclencher automatiquement lorsque : « Le devis est accepté ». *(Champ laissé vide = déclenchement manuel uniquement.)*
- Filtres *(facultatif)* : restreindre selon le Client, le Type de client, l'Activité, le Reste à facturer… (bouton « Tous les filtres »).
- Stopper automatiquement lorsque : les événements qui arrêtent l'automatisation, ex. « Le devis est annulé », « Le devis est refusé ».
- Autoriser plusieurs automatisations en parallèle : à cocher seulement si vous voulez que plusieurs automatisations tournent en même temps sur un même objet (devis, facture...).

C. Activer et enregistrer

- Indiquez un délai de déclenchement pour la création du chantier suite à l'acceptation du devis

![](https://downloads.intercomcdn.com/i/o/tarury57/2648953673/ff7db3cbcfabf4e6928468ea60f7/CleanShot+2026-09-03+at+16_30_36%402x.png?expires=1788674400&signature=a8e709a14c2d26dcbb924f8fd5934577e430d4bc1cc535b374eb375275882f0a&req=diYjHsB7nodYWvMW3nq%2BgWyqTToau1lJWK%2FI4tfbKfe78%2B97RmOkK8kE4xoQ%0AOrqheTtwZeFTSRFI3ni2nCmNr5o%3D%0A)
- Indiquez un délai de déclenchement pour la génération automatique de votre facture d'acompte, qui sera liée au chantier créé lui-même automatiquement à l'étape précédente 

![](https://downloads.intercomcdn.com/i/o/tarury57/2648958201/88104c90d1cce9b8dd0ac63b85ce/CleanShot+2026-09-03+at+16_32_04%402x.png?expires=1788674400&signature=b34382951fb44c2b84208ee67ecf907e3c86f1ddbbf4724ac8e228b7e97c892a&req=diYjHsB7lYNfWPMW3nq%2BgejE9q4FBo0plbqZYaDR8MJhA8o7wzwGsePMWQj2%0Ad9nV6XvHvdQNzFtL3LCTtdGJtDg%3D%0A)
- Enregistrez ✅

D. Résultat

Lors de l'acceptation de votre devis, le chantier se crée bien et tout est interconnecté comme toujours.
​
Le chantier apparaît bien dans les opérations liées au devis.

![](https://downloads.intercomcdn.com/i/o/tarury57/2648982421/786db702e423c0232a170c2ceed8/CleanShot+2026-09-03+at+16_39_43%402x.png?expires=1788674400&signature=d51d3c9f13de2156c0a8ca349ea816ad57a05f50c5ae88c43dd53251d658d286&req=diYjHsB2n4VdWPMW3nq%2BgVBZHlIBm0vi0mUiXfAvqqxEeU5ju2%2FYoV7StNy8%0Aj66tBy81gD6ND6SFqbL%2BNBGN0PI%3D%0A)

Et le devis apparaît bien dans l'onglet **Ventes › Devis du chantier** créé automatiquement.

![](https://downloads.intercomcdn.com/i/o/tarury57/2648983657/0acf178c7271f090382e1c7a7007/CleanShot+2026-09-03+at+16_40_11%402x.png?expires=1788674400&signature=711216bda3d43de198116bc83c7739f8c39b00204204e474f5e65cf05695bd40&req=diYjHsB2nodaXvMW3nq%2BgQoqR1KC5Ddpzpf2Dkurv5SdrgJHz5ABNO12L2Ud%0ADQdqr9zpAVhbMA0Te2PcoXDRNiI%3D%0A)

Suite à la création du chantier également, la facture d'acompte est générée automatiquement et on peut la retrouver dans l'onglet **Ventes › Factures du chantier** également.

![](https://downloads.intercomcdn.com/i/o/tarury57/2648986179/a89e5b60348bdafacbb4001f05da/CleanShot+2026-09-03+at+16_42_22%402x.png?expires=1788674400&signature=4d01a56eda67cc6b2e040dc1f4cfa52128ac2afcf342d7d661e6a084b57b6aab&req=diYjHsB2m4BYUPMW3nq%2BgbpEa16gfYVdZ4QGvYsHw4zjk6DU4ZAWUIZioS0j%0AaWW8KgGVqGV4%2BzwaQ9PsGYVaU5g%3D%0A)

Notez qu'elle se créé en reprenant les conditiions paramétrées initialement dans le devis.

> 💡 Pensez à actualiser votre page régulièrement pour voir la génération du chantier puis de la facture d'acompte, selon les délais que vous avez configuré dans l'automatisation.

E. Vérification et contrôle des informations

- **Où retrouver les éléments créés ?**
​
- Le chantier se trouve dans le module **Chantiers**.
​
![](https://downloads.intercomcdn.com/i/o/tarury57/2648994094/e6cfefd4dbce8f7b3222aa937245/CleanShot+2026-09-03+at+16_45_19%402x.png?expires=1788674400&signature=3841062789b6d71d1e2e8196db538559bb0d7cc9989dc959db8a27c66bec77b4&req=diYjHsB3mYFWXfMW3nq%2BgYx0ga%2BHv2RY2ZafEtJjFvY%2BC10YWsWW2ZTbJyIX%0A2ccoplUimhenjEzpFTiKoFaoNI0%3D%0A)
- La facture d'acompte se trouve dans vos **Factures clients**.
​
![](https://downloads.intercomcdn.com/i/o/tarury57/2648995061/089416fa43aed99907a87ca5a469/CleanShot+2026-09-03+at+16_45_08%402x.png?expires=1788674400&signature=6d2a63260da7cfd00433de442666c7b214ea55b819bf6ef58a2cc8bb57d38b23&req=diYjHsB3mIFZWPMW3nq%2BgZH%2Bvqts49vAht5XOFW8m%2BmX1Zpkd499k9wAbtvF%0AGcel7M0rPRezdR0GZ7wLsdoLLLQ%3D%0A)
- **En cas d'erreur de manipulation :** Vous pouvez toujours modifier / supprimer la facture générée en **brouillon**, modifier les paramètres du chantier manuellement ou désactiver temporairement l'automatisation.

## Conclusion : Prenez les commandes de votre croissance

L’automatisation n’est pas là pour remplacer votre expertise, mais pour libérer votre esprit des tâches administratives répétitives. En configurant correctement vos scénarios de relances et de suivis, vous garantissez à vos clients une réactivité irréprochable tout en vous concentrant sur ce que vous faites de mieux : votre métier sur le terrain.

Rappelez-vous qu'une bonne automatisation se surveille : jetez régulièrement un œil à votre onglet Exécutions pour garder le contrôle total sur vos dossiers en cours.

Prêt à passer à la vitesse supérieure ? Commencez par un scénario simple, comme une relance de facture à J+7, et observez le temps que vous gagnez chaque semaine.
​

## III. Questions fréquents (FAQ)


Les modifications ne sont pas rétroactives. Les processus déjà lancés continuent avec l'ancienne configuration. Vous devez arrêter manuellement les anciennes exécutions dans l'onglet Exécutions.

![](https://downloads.intercomcdn.com/i/o/tarury57/1945262481/29caa4ead0d5fc6974659e5d9941/CleanShot+2026-01-15+at+16_47_52%402x.png?expires=1788674400&signature=c85d004780b13d1029289eaca7e6d0493f9793c572bf2c37a7890f0039741f0d&req=dSkjE8t4n4VXWPMW3nq%2BgSHWw3q20x%2FCfmNBN4fFQB0oYjfrJV0RUOUQ2G0o%0AGrfTpDbn3mPW%2Fj6FKFm5BzX25Jw%3D%0A)

![](https://downloads.intercomcdn.com/i/o/tarury57/1945262912/2141e7ced5f2a7071d83e042549e/CleanShot+2026-01-15+at+16_47_18%402x.png?expires=1788674400&signature=1875a2693801966667f6cc994002032d892dbd08804fd41b6cc1537f11e8758c&req=dSkjE8t4n4heW%2FMW3nq%2BgSZlLW8wGhuQRSg9niS3CA%2BPgM7dZwXykh%2BkJx%2Fw%0A7hYwYyCPg0SDCDolivNOgnfDGjU%3D%0A)



Par défaut, ils sont envoyés au contact principal défini dans votre fiche client (CRM). Vérifiez bien que ce contact est le bon avant d'activer vos relances.

![](https://downloads.intercomcdn.com/i/o/tarury57/1945265119/3d29efaf913b105eaa5d4c288b8b/CleanShot+2026-01-15+at+16_48_58%402x.png?expires=1788674400&signature=824c28671b112223181258a8740fec419ac2cd13ba7cadaa587334d1800e9586&req=dSkjE8t4mIBeUPMW3nq%2BgWpplgC7Pym%2BykggJuzn4U6KP9qHY7ybuU%2F8YNnK%0AKP4YuItqI1RdMWhdABXYcZQg3QY%3D%0A)



Oui ! Si vous ne mettez pas de déclencheur automatique, vous pouvez lancer votre scénario manuellement sur une facture ou un devis spécifique via le bouton dédié.
​
Il faut prendre le soin au préalable de supprimer la condition de déclenchement de l'automatisation : 

![](https://downloads.intercomcdn.com/i/o/tarury57/1945280537/21e3c15c9e1c1602c4313d9cd886/CleanShot+2026-01-15+at+18_02_33.gif?expires=1788674400&signature=ef413a0e2ca80fda7a53687cf6babba8bf27c54c9f0cc0c471ec18c091b8406e&req=dSkjE8t2nYRcXvMW3nq%2BgYsK5pqqU56gIWc53xymV5Ofhee34YZStK70Ftvs%0A9wSXf70LDu1f%2B4Yv1bAOFfZmXRs%3D%0A)

*Déclenchement manuel sur une facture par exemple : *

![](https://downloads.intercomcdn.com/i/o/tarury57/1945267697/fe72ba471a5697c847a844d99ce2/Capture-2Bd-E2-80-99e-CC-81cran-2B2025-04-07-2Ba-CC-80-2B12_15_56.png?expires=1788674400&signature=8053b3cc7d11305f797915a94395ae2aa9870d2c6682df6d45518e56c7e76e9a&req=dSkjE8t4modWXvMW3nq%2BgbO2BIYjBaaExrQnl%2Ft3kYuiH5f%2BA5xP9QgKjEdP%0AglXo%2FHlwWkrdEBnSwA0zCXXmWaM%3D%0A)

Mis à jour le : 04/09/2026
