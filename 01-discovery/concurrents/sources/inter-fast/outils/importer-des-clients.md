---
source: https://help.inter-fast.co/fr/articles/10254004-importer-des-clients
categorie: Outils
titre: Importer des Clients
date_recuperation: 2026-09-05
---

# Importer des Clients

### 

> 💡 **Le service d'import par InterFast :** Vous avez un fichier client volumineux, complexe ou vous avez peur de faire une erreur ? Pas de panique ! Notre équipe Care peut s'en charger gratuitement pour vous. 
> Envoyez-nous simplement votre fichier (Excel ou CSV) directement via la bulle de tchat en bas à gauche de votre écran, et nous l'intégrerons proprement dans votre compte.

> 💡 **Disponible avec votre abonnement ?** L'import de clients est inclus dans tous les abonnements.
> - **Starter** — ✅ inclus
> - **Pro** — ✅ inclus
> - **Business** — ✅ inclus
> 👉 Pour vérifier ou changer votre plan : rendez-vous dans [Mon Abonnement.](https://app.inter-fast.fr/dashboard/company?c=billing)

## 
I. Vidéo tutoriel d'Hedi 

[Vidéo YouTube](https://www.youtube.com/watch?v=ipakYSW6w7E)

## II. Préparer vos données

La clé d'un import réussi, c'est la qualité de votre fichier de départ. Nous vous recommandons d'utiliser **Google Sheets et notre fichier template pour réaliser votre import **👉 **[[Cliquez ici pour télécharger l'exemple de fichier clients]](https://docs.google.com/spreadsheets/d/1qb7nzhG8uvI3TjlIedi1tyYYnoYdi3FSbv42UxGb604/edit?usp=sharing)**

### A. Les colonnes à renseigner

La qualité de l'import dépend du respect des colonnes. Voici les informations que vous pouvez importer dans Interfast. Assurez-vous que votre fichier contient des colonnes distinctes pour ces éléments :

- **A. Nom de l’Entreprise** (Uniquement pour les clients Pros)
- **B. Nom du Client**
- **C. Prénom du Client**
- **D. Adresse** (Numéro et nom de voie)
- **E. Code postal**
- **F. Ville**
- **G. Numéro de téléphone**
- **H. Numéro de téléphone secondaire** (facultatif)
- **I. E-mail**
- **J. Mémo Client** (Notes internes, facultatif)
- **K. Siret**
- **L. N° TVA**
- **M. Compte Comptable**

![](https://downloads.intercomcdn.com/i/o/tarury57/1842129783/3cc148365c980e945fbf036d93fd/2024-08-2111h5548-1_cl164p.png?expires=1788619500&signature=c0579a503cc045e9016e47c110005245aae7622449620d33ca95e947d91b72fd&req=dSgjFMh8lIZXWvMW1HO4zdAXnEdjvCu6VLFkNsTt19WtXqgRySm72i%2FUBN3d%0AxL0Id4Yj3hbKrdxCzH4%3D%0A)

### B. Préparer le transfert de vos données - Méthode par colonne

Cette méthode a un double objectif : Empêche de modifier accidentellement les en-têtes (titres) du modèle et vous permet de vérifier que chaque donnée atterrit bien dans la colonne prévue.

1. Ouvrez votre fichier **source** et le fichier **Modèle Interfast** dans deux onglets distincts.
2. Dans votre fichier source, cliquez sur la lettre de la colonne à copier (tout en haut) pour la sélectionner entièrement, puis faites **Copier**.
3. Dans le **Modèle Interfast**, cliquez sur la lettre de la colonne correspondante (cible) et faites **Coller**.
4. Répétez l'opération pour chaque information.

![](https://downloads.intercomcdn.com/i/o/tarury57/1842132160/b231586c09222e1c1da3e8d8bf60/2025-11-19_14h31_14.gif?expires=1788619500&signature=4e31a86eef27e2318715bc613d243004e0fae92592cb9d31fad9288739b745d3&req=dSgjFMh9n4BZWfMW1HO4zb%2BZKPNRu8a5WP1UrDevEIilXItegDUjlV%2BM3Qx%2F%0AznGS50UBx69qDzqmwaQ%3D%0A)

**Important :** Ne modifiez jamais la première ligne (l'entête) du modèle Interfast. Le logiciel a besoin de ces titres exacts pour mapper les colonnes et éviter les erreurs.

### C. Distinguer les "Pros" des "Particuliers"

Interfast fait la différence automatiquement grâce à la colonne **Entreprise**.

- **Client Professionnel :** La colonne "Entreprise" doit être **remplie** (ex: ENTREPRISE MICHEL).

![](https://downloads.intercomcdn.com/i/o/tarury57/1842138565/f9b5834e3ebbe30f9b271132c8bb/capture-decran-2024-04-02-a-18_129cnxy.png?expires=1788619500&signature=9a506703332ddde8ed3e8891204364ae1aeca48af3f0eacf0e9121eed70b6c38&req=dSgjFMh9lYRZXPMW1HO4zdfUKrxnKgLXNGtZqJaOZVu67hPCJ52wRSyTp3tb%0AW34W%2FEDWPZinkz9aduM%3D%0A)

- **Client Particulier :** La colonne "Entreprise" doit rester strictement **vide**.

![](https://downloads.intercomcdn.com/i/o/tarury57/1842138729/9bd13fd22b088ec368dca0ca5582/capture-decran-2024-04-02-a-18_17xvttf.png?expires=1788619500&signature=dbe46a6e34794d7c99202ac3da82d277fe601dbf67f7c1dcb4bc9bd1906b84e0&req=dSgjFMh9lYZdUPMW1HO4zcAmx17OyYaixSfVgxpJWZ7xPAIq3eWEqul50emL%0APCWSX4eYQnMiFgNDzBo%3D%0A)

### D. Importer plusieurs contacts pour une même entreprise

Dans le bâtiment, pour un même client professionnel (ex: une agence immobilière ou un syndic), vous avez souvent plusieurs interlocuteurs : le gérant, la comptable, le gestionnaire technique, etc. Pour qu'Interfast comprenne que **Jean Dupont** et **Marie Martin** travaillent tous les deux pour l'entreprise **"Immo Plus"**, la méthode est simple : **La colonne "Nom de l'Entreprise" doit être strictement identique.**

1) Comment faire dans votre fichier Excel / Sheets ?

1. **Remplissez la première ligne** avec le nom de l'entreprise (et éventuellement son adresse de facturation).
2. **Créez une nouvelle ligne en dessous** pour votre premier contact (ex: le chef de chantier).
3. **Collez exactement le même nom d'entreprise** dans la colonne A ("Nom de l'Entreprise").
4. Remplissez les colonnes **Nom**, **Prénom**, **Téléphone** et **Email** avec les infos de ce contact.
5. Répétez l'opération pour chaque interlocuteur supplémentaire.

**Exemple :**

| **A. Nom de l’Entreprise** | **B. Nom** | **C. Prénom** | **I. Email** | **Rôle (Explication)** |
| --- | --- | --- | --- | --- |
| **Bati Rénov 13** |  |  | [contact@bati-renov.fr](mailto:contact@bati-renov.fr) | *Fiche principale de la société* |
| **Bati Rénov 13** | Dupont | Jean | [jean@bati-renov.fr](mailto:jean@bati-renov.fr) | *1er contact (Gérant)* |
| **Bati Rénov 13** | Martin | Julie | [compta@bati-renov.fr](mailto:compta@bati-renov.fr) | *2ème contact (Comptable)* |

 
2) Et pour plusieurs adresses d'une même entreprise ?

Le principe est identique aux contacts : créez **une ligne par adresse**, en gardant le **nom de l'entreprise strictement identique** sur chaque ligne. InterFast rattachera toutes ces adresses au même client.

**Exemple :**

| **A. Nom de l'entreprise** | **Adresse** | **Ville** | **Rôle (Explication)** |
| --- | --- | --- | --- |
| **Bati Rénov 13** | 12 rue des Oliviers | Marseille | Adresse de facturation |
| **Bati Rénov 13** | 8 avenue du Chantier | Aix-en-Provence | 2ᵉ adresse (site) |
| **Bati Rénov 13** | 45 chemin des Pins | Aubagne | 3ᵉ adresse (site) |

Vous pouvez combiner les deux : plusieurs contacts **et** plusieurs adresses pour la même entreprise, toujours en répétant le nom d'entreprise à l'identique sur chaque ligne.

> ⚠️ **Attention à l'orthographe !**
> Que vous regroupiez **plusieurs contacts** ou **plusieurs adresses**, InterFast se base sur **le nom de l'entreprise** (client professionnel) ou sur **le nom du client** (particulier) pour rattacher les lignes à un même client pendant l'import. Ce nom doit être écrit **exactement de la même façon** sur chaque ligne à regrouper.
> 
> Par exemple, si vous écrivez **« Bati Rénov 13 »** sur la première ligne et **« Bati Renov 13 »** (sans accent) sur la deuxième, InterFast créera **deux clients différents**.

## III. Importer le fichier dans Interfast

Votre fichier est propre ? C'est le moment de l'envoyer sur votre espace.

1. Rendez-vous dans le module **CRM** (menu latéral).
2. Cliquez sur le bouton d'import (icône de nuage ou flèche) en haut à droite :
3. Sélectionnez votre fichier **CSV** 
![](https://downloads.intercomcdn.com/i/o/tarury57/1842140624/1dcfe8f43a5c667b89735babcb2a/fichier-1_3wvysp.png?expires=1788619500&signature=46fe32a3f78278b9ca2715646f3fe7a48c59e033fbf26a4ee508731c0217c7a4&req=dSgjFMh6nYddXfMW1HO4zQlvrQ4z%2F9BkGaGvT4RDxSYdVFu2FvdXLtI%2FKb2V%0AcMO1%0A)

### A. L'étape du Mapping (Association)

Le logiciel va vous demander de faire correspondre vos colonnes avec celles d'Interfast.

![](https://downloads.intercomcdn.com/i/o/tarury57/1842140776/d793bdb52c34ffe92b950c2050da/maping-1_d79qnd.png?expires=1788619500&signature=350a01e6346e9f3b059be877d5064bc27572e7206a821d3c8712b3873f052966&req=dSgjFMh6nYZYX%2FMW1HO4zVaRgyA2oG6bOlXbZ8AnwbazL6gZ3JzALi%2BHk8K6%0AHW%2FwJMw4I5%2F%2Ft2S%2FtnI%3D%0A)

### B. Validation

Une prévisualisation s'affiche. Vérifiez que les colonnes ne sont pas décalées (ex: le téléphone à la place de la ville). Si tout est vert, validez ! Vos clients sont maintenant créés.

![](https://downloads.intercomcdn.com/i/o/tarury57/1842141259/e618419ecb348be52f23273786f7/verifi-1_4b8k3o.png?expires=1788619500&signature=900e51d8730f6e24e3590dad52ef12e3b5566118660aeea11dccfd18f17dfa95&req=dSgjFMh6nINaUPMW1HO4zRIBvcfmJiwmF4NstLqc7TCU%2BoJI2lIIb41dC%2Bbg%0A0ZmyDjTRASe%2FkVhhscY%3D%0A)

> **Attention :** Si une donnée ne s'affiche pas, vérifiez qu'elle n'a pas été sélectionnée deux fois pour deux champs différents.

## IV. Annuler un import de clients erroné

Si vous vous apercevez après coup que votre fichier comportait des erreurs (colonnes inversées, doublons, fautes de frappe), InterFast vous permet de faire machine arrière très facilement.

1. Rendez-vous dans vos **Paramètres** > **Imports de données**.
2. Retrouvez l'import concerné dans l'historique de vos actions.
3. Cliquez sur le bouton **Supprimer** **l'import** .
4. Confirmez votre action. Tous les clients créés lors de cette session d'import spécifique seront instantanément retirés de votre base de données.

![](https://downloads.intercomcdn.com/i/o/tarury57/2450043321/652e1b8f787d316869af113c6535/FE0E374E-C6E1-417C-8E5F-0A32DC1165F3.jpeg?expires=1788619500&signature=4b79376fbdbcf73d9388ea4b19d049b4e6d645c2d3a1db5387f6afc49c14f3e1&req=diQiFsl6noJdWPMW1HO4zZBKXRFomkwcqsDquM6WZ5r1yo%2BQFumXV2mHBD8R%0AN%2BIYzWcpUA1udj8zNJ8%3D%0A)

![](https://downloads.intercomcdn.com/i/o/tarury57/2450042759/385d6f5e81cf97633c74be7c153d/image.png?expires=1788619500&signature=15ace5fc0317ee40d9013fa91383d45642b1f331d80364851b2b356fa9c36f17&req=diQiFsl6n4ZaUPMW1HO4zS9m3WiAzi2r3j5%2FhRwndVaXfbiUY9OeFOCbsLGU%0AvG7PUohDiosZdT%2B12Ng%3D%0A)

## 
En résumé 


L'import de clients vous permet de reprendre toute votre base existante dans InterFast en une seule opération, plutôt que de ressaisir chaque fiche à la main.


La clé d'un import réussi tient à la préparation du fichier : des colonnes bien identifiées, la distinction entre professionnels et particuliers, et un **nom d'entreprise (ou de client) écrit exactement de la même façon** sur chaque ligne à regrouper. InterFast se charge ensuite d'associer les contacts et les adresses au bon client.


Si votre fichier est volumineux ou complexe, l'équipe Care peut réaliser l'import **gratuitement** pour vous — il suffit de le demander depuis le tchat.
​

## 
V. Questions fréquentes (FAQ)

1. Créez d'abord le champ dans le logiciel (voir l'article : [[Créer une propriété personnalisée]](https://help.inter-fast.co/fr/articles/10253812-utiliser-les-proprietes-personnalisees)).
2. Ajoutez une nouvelle colonne dans votre fichier Excel avec le nom exact de cette propriété en en-tête.

Si vos numéros s'affichent 612345678 au lieu de 0612345678 :
1. Sélectionnez la colonne des téléphones.
2. Allez dans le menu **Format > Nombre > Format numérique personnalisé**.
3. Dans le champ, tapez 00 00 00 00 00.
4. Cliquez sur **Appliquer**.

![](https://downloads.intercomcdn.com/i/o/tarury57/1848160006/e2fbb3ac3c1a32eec75a444a8b54/capture-decran-2024-05-03-a-19_1jv68tv.png?expires=1788619500&signature=97f071b6b764759f36e773f3db7b7bb47c9cf9da2caedcc694a67ef1b286dcd4&req=dSgjHsh4nYFfX%2FMW1HO4zWTknwM%2BzO2FuMOFzx7PGiZ5WjnTxqeA7gJ2OEa7%0ApBWrYPQAPD%2F%2BxTzqB6M%3D%0A)


![](https://downloads.intercomcdn.com/i/o/tarury57/1848160005/928c24cb10316dc47ab09e2ff2ef/capture-decran-2024-05-03-a-19_1pbc59i.png?expires=1788619500&signature=253ab2be807299e9fa6bd43faba32a042187d58f0acb7ef9c8ac83654d260110&req=dSgjHsh4nYFfXPMW1HO4zRpVveV7oqiZg1w1k9Atq7VZv7CnvDnoS2N89Fxy%0ANsYlTeiAfZmQ1WvXRY8%3D%0A)






*Exemple : Votre ancien logiciel a mis le "N° de rue" dans la colonne A et le "Nom de rue" dans la colonne B, mais vous voulez tout dans une seule colonne "Adresse".*
1. Créez une nouvelle colonne vide.
2. Utilisez la formule suivante : =CONCATENER(A2;" ";B2)
3. Étirez la formule sur toutes vos lignes.

![](https://downloads.intercomcdn.com/i/o/tarury57/1848159310/e90eef6739307f4b5774a6ad0f8e/Capture-2025-01-06-2Bat-2B10_09_41.gif?expires=1788619500&signature=cb1eb8d4fe10b7488b30d102ad095c5657528e8f996fa0dd68a133dbb27a3a79&req=dSgjHsh7lIJeWfMW1HO4zf94%2Bgz%2FmIXhm%2FZYjCdbZB48GRpmnBPFSMZgR7GU%0A89sqGjWxKNYRMhQdfJk%3D%0A)




Si vous avez une colonne "Jean Dupont" et que vous devez séparer les Nom & Prénoms deux options s'offrent à vous :
- **Option rapide :** Utilisez une IA comme ChatGPT avec la consigne : *"Voici une liste de noms complets, sépare-les en deux colonnes : Prénom et Nom format CSV"*.
- **Option Google Sheets :** Utilisez la fonction **Données > Diviser le texte en colonnes** en choisissant l'espace comme séparateur.
**Vérification indispensable avant import** 
Les traitements automatiques (IA ou Google Sheets) ne sont pas infaillibles, notamment sur les **noms composés** (ex: Jean-Pierre) ou les **particules** (ex: De La Croix). **Prenez le temps de relire votre fichier** pour corriger manuellement les éventuelles erreurs de découpage avant de l'envoyer dans Interfast.




Pour éviter que "Hélène" devienne "HÃ©lÃ¨ne", il est impératif d'exporter votre fichier final au bon format. 👉 **Fichier > Télécharger > Valeurs séparées par des virgules (.csv)**. 

*Note : Google Sheets gère par défaut le format UTF-8 qui protège vos accents.*


Si des doublons apparaissent après l'import, utilisez l'outil de fusion d'Interfast pour regrouper vos fiches clients.

Cliquez sur le bouton "Actions" pour :
*> transformer un Particulier en Pro (et vice versa)*
*> fusionner / supprimer le Client*

![](https://downloads.intercomcdn.com/i/o/tarury57/1848157873/5b6e501be70cf5045fd4e8d3a204/Ih2PUGmup4mwZdyUZ1ByloPgJzuch7p2YC58Be37.jpeg?expires=1788619500&signature=72b4f999f720273796311e6a06daf2e1d0082bf8d6503bdd5b171dc9ff5a81b1&req=dSgjHsh7molYWvMW1HO4zWe3B4k6YOBYFH5q%2B%2Fcj6hpJgx0xM3Qh2smoypHK%0AKifjDE7CO3DNRqK3HBg%3D%0A)

﻿2) Cliquez sur l'icône Stylo pour éditer les informations du Client :
![](https://downloads.intercomcdn.com/i/o/tarury57/1848157874/ec6ed811153ded971e9fa1e0cd06/CleanShot-2B2025-06-24-2Bat-2B13_29_04.png?expires=1788619500&signature=767083aef862254cb055b53f9211792c560a5727127ec6de60c58c979ba55a5e&req=dSgjHsh7molYXfMW1HO4za2xnUq%2B5NpSiR5Im9ZDgGdr%2FLtphoxz24uMhL%2BU%0AA8P9H92%2FgmlxuF6OVpk%3D%0A)

​
Si ce message s'affiche pendant le chargement, cela signifie généralement que votre fichier est volumineux et que le traitement demande plus de temps que prévu par le navigateur.

**Pas de panique, l'import n'a pas échoué.** Le processus continue de fonctionner normalement en "arrière-plan" sur nos serveurs, même si votre écran affiche une erreur.

**⚠️ Action importante :** **Ne relancez surtout pas l'import** et allez vérifier si l'import est en cours depuis votre espace "Mon entreprise" > "Paramétre" > "Import"
![](https://downloads.intercomcdn.com/i/o/tarury57/1848210000/be3b925fc152db68888ee41ea49a/image.png?expires=1788619500&signature=ed6d292b1ede7174a8315fd755aade1f7e0439955dac834f4ace6133e500393f&req=dSgjHst%2FnYFfWfMW1HO4ze3o%2BfXr9CF1menx%2Fg9Eg8wtENnksJv9LqDoED%2Fd%0AEvniDno4Rmikzqy6mNk%3D%0A)
**Si votre import est en cours il y aura un statut "En cours"**


C'est une sécurité légale. L'import efface bien les fiches, à une exception près : si l'un de ces clients importés a été rattaché entre-temps à un Devis ou une Facture **finalisé(e)** (possédant un numéro officiel). Pour respecter la loi anti-fraude à la TVA, le logiciel verrouille ce client, car il est désormais lié à une pièce comptable inaltérable.

Mis à jour le : 03/09/2026
