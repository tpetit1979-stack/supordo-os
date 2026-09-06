---
source: https://help.inter-fast.co/fr/articles/12928587-importer-et-gerer-un-dpgf
categorie: Finances
titre: Importer et gérer un DPGF
date_recuperation: 2026-09-05
---

# Importer et gérer un DPGF

> 💡 Disponible avec votre abonnement ? L'import et la gestion des DPGF font partie de l'abonnement Business.
> 
> Starter — non inclus
> Pro — non inclus
> Business — ✅ inclus
> 
> 👉 Pour vérifier ou changer votre plan : rendez-vous dans [Mon Abonnement](https://app.inter-fast.fr/dashboard/company?c=billing).

### Qu'est-ce qu'un DPGF?

Le **DPGF** (Décomposition du Prix Global et Forfaitaire) est un document financier incontournable dans le secteur du BTP, souvent utilisé pour répondre aux appels d'offres (publics ou privés).

Contrairement à un simple devis, le DPGF sert à "découper" le prix global de votre chantier. Il permet à votre client de comprendre exactement comment est construit votre tarif, en isolant le coût de chaque poste (ex: Terrassement, Plomberie) et les quantités associées.

- **Pour vous :** C'est la référence qui servira tout au long du chantier, notamment pour facturer vos situations de travaux (au pourcentage d'avancement).
​
- **La règle d'or :** Dans un marché au forfait, les quantités données par le client sont souvent *indicatives*. C'est à vous de les vérifier avant de chiffrer !
​
- **Différence avec le BPU :** Le DPGF fixe un prix total pour un projet connu à l'avance. Le BPU (Bordereau des Prix Unitaires) fixe un prix à l'unité pour des quantités inconnues à l'avance.

Ressaisir manuellement des centaines de lignes depuis un fichier Excel ou PDF vers votre logiciel de gestion est une tâche chronophage et source d'erreurs.

C'est pourquoi InterFast a développé un import intelligent pour transformer instantanément le tableau de votre client en un devis prêt à l'emploi !

Pour l'entreprise de travaux, le DPGF est essentiel car il servira de référence tout au long du chantier, notamment pour établir les **factures de** **situation des travaux** sur la base d'un pourcentage de réalisation de chaque ligne.

## **I. Préparation et Importation du DPGF**

Avant d'importer votre DPGF dans InterFast, il est indispensable de mettre en forme votre fichier Excel ou Google Sheets pour garantir que les données soient lues correctement.

### **1. Structuration du fichier**

Ouvrez le fichier fourni par votre client *(généralement au format .xlsx)*.

Assurez-vous qu'il contient les colonnes essentielles :

- Numérotation
- Désignation des articles / ouvrages
- Unité
- Quantité
- Prix unitaire de vente
​

Assurez-vous également que la hiérarchie des ouvrages soit claire.

![](https://downloads.intercomcdn.com/i/o/tarury57/1848741821/203fc6b2739759437a7dc6d887cc/Capture+d-e%CC%81cran+000323+-25-11-2025.png?expires=1788618600&signature=6804178f48c9f881a6aeb80333b92409657d4f8313bab7728f3aa032b2793fae&req=dSgjHs56nIldWPMW1HO4zZZ283zkMSC298JO4mYj7Ej1fzNz50fMvhmXaACu%0A8MmQG8mUS2p0g6%2BHN98%3D%0A)

*Exemple d'un DPGF*

- **Remplissage des données :** vous pouvez compléter les colonnes **Quantité** et **Prix Unitaire - Vente** pour établir votre estimation financière globale.

![](https://downloads.intercomcdn.com/i/o/tarury57/1848746572/1949be539ba452529a48b546fa52/image.png?expires=1788618600&signature=0ed516e9b0998760d3e6a75c9d7b1c9f50a136dc39559b3b964dbd1794b11491&req=dSgjHs56m4RYW%2FMW1HO4zbwJatcgh703Pt%2BsfKiUYguTbV9qAJoP1ATY6ss%2B%0A5oFN%0A)
*Remplissage de la Quantité et du Prix unitaire de vente*
- **Numérotation Hiérarchique :** assurez-vous que chaque ligne possède une numérotation logique qui reflète la structure du document.
​
- *Exemple :* Si vous avez un ouvrage numéroté **4.1**, les articles qu'il contient doivent être numérotés **4.1.1**, **4.1.2**, **4.1.3**, etc.
​
Cela permettra à InterFast de reconstruire la hiérarchie de votre document.
​
![](https://downloads.intercomcdn.com/i/o/tarury57/1848749757/e47399870342ee2824df68a6f83e/image.png?expires=1788618600&signature=b2ebb9a2c418274a6f34bdc114f9333f4e2beee1456d81ab75f42f0d4c11490d&req=dSgjHs56lIZaXvMW1HO4zaVcSaM19wmqhmSpt4ZbAmmG3iO3dJhNkYOKVhG5%0AN7KQ%0A)
- **Nettoyage des en-têtes :** votre première ligne doit contenir des titres clairs pour vos en-têtes de colonne : **Numéro**, **Désignation des Ouvrages**, **U** (Unité), **Quantité**, **Prix Unitaire de vente**.

![](https://downloads.intercomcdn.com/i/o/tarury57/1848752967/7386152d977e86ccb6a90b37a523/image.png?expires=1788618600&signature=9ac3d2cde456bc787a4ea494d7e65f606412a939c52dcd2a01f2e48d9ab656de&req=dSgjHs57n4hZXvMW1HO4zY2RzsPE9tWzUH%2BY67Pm7Lh%2FYDv5l5GxXYG8iJAp%0AV2v4%0A)

### **2. Exportation au format CSV**

Une fois votre tableau prêt et vérifié :

- Allez dans le menu **Fichier** > **Télécharger** (ou Enregistrer sous).
- Sélectionnez le format **Valeurs séparées par des virgules (.csv)**.
C'est ce format spécifique qui pourra être importé sur InterFast.

![](https://downloads.intercomcdn.com/i/o/tarury57/1848754680/40100ca82d3ddefc886cb120408b/image.png?expires=1788618600&signature=3bba20a16f97959c16d74595ae8444cf8c13b60f844c09f6e996de8c8884e4e7&req=dSgjHs57mYdXWfMW1HO4zWOVeny88BakIt8P4IykNjI8xlCbIYDlpvjlb1Pc%0ABMR2%0A)

### **3. Lancement de l'import dans InterFast**

Rendez-vous maintenant sur votre application web InterFast :

- Allez dans le module **Ventes** > **[Devis](https://app.inter-fast.fr/dashboard/billing/quotations?quotation=%7B%22pageIndex%22%3A0%7D)**.
- Cliquez sur le bouton **Actions** en haut à droite, puis sélectionnez **Import depuis un CSV** (Importer un devis / DPGF).
​
![](https://downloads.intercomcdn.com/i/o/tarury57/1848758395/6e361c0517434e491c244d0e9789/image.png?expires=1788618600&signature=be58263dfcea614f9ddcefbc58d7223afb183919090018c2d527a3ed36a4d8ce&req=dSgjHs57lYJWXPMW1HO4zRietXVVbUPyrdrBBQIGumE2Oth5KiiNzFoEoPLS%0Avrus%0A)
- Une fenêtre d'importation s'ouvre. Glissez-déposez votre fichier .csv ou cliquez pour le sélectionner depuis votre ordinateur.

![](https://downloads.intercomcdn.com/i/o/tarury57/2464883049/a98b5ab241be2a39610c93df8bfa/image.png?expires=1788618600&signature=c45a3f19ff85a927752d0482cdfe80655d546a038b8f9888cfadaf4fc7915b05&req=diQhEsF2noFbUPMW1HO4zZaJrSLKfhnqgCL9tDTlNMXGqDB5AKWXE5DNzFw1%0AhmEy%0A)
- Cliquez ensuite sur **Suivant** pour passer à l'étape de configuration.

## II. Paramétrage et Validation de l'import

Une fois votre fichier CSV chargé, vous devez organiser l'association des colonnes pour qu'InterFast comprenne le contenu de votre fichier. Suivez les étapes décrites ci-après.

### 1. Numérotation et Structure

InterFast a besoin de savoir quelle colonne sert de référence pour structurer le devis *(créer les sections et sous-sections)*.

- **Sélection de la colonne :** Dans le menu déroulant, choisissez la colonne de votre fichier qui contient **les numéros de ligne** *(ex: Numéro)*.

![](https://downloads.intercomcdn.com/i/o/tarury57/1849584332/1d0f69d1291b6078406d9e8b1e31/image.png?expires=1788618600&signature=a7f9e4e869d51d7d163aca51f0d3fefab5f3085e1d1d2c2399655d33e37a8346&req=dSgjH8x2mYJcW%2FMW1HO4zRk8bQVV%2FW5%2BxyiZryesIBAS9iiIFEm%2BPPZk0SWC%0AlFQ8Xnyk%2FwXQdzOs%2BWA%3D%0A)

### 2. Gestion des lignes de description

Vos DPGF contiennent souvent des phrases de contexte (ex: *"Tous les équipements sont prévus avec..."*) qui ne sont ni des titres, ni des ouvrages chiffrés. Vous devez décider comment les traiter :

- **Le choix du comportement :** à l'étape **"Lignes de désignation uniquement"**, un menu vous propose plusieurs options :

![](https://downloads.intercomcdn.com/i/o/tarury57/1849585877/f8365d01fdc4b833635c9e2a017d/image.png?expires=1788618600&signature=86f4f64772f8fcbcb4c6889c0f2198adfb85f7ea2643b36f26185765fafbbf0d&req=dSgjH8x2mIlYXvMW1HO4zRW0qS%2F3LyYbFqxA3Hr08YfwnY89WKh1Unq6ysS4%0Af4Yz%0A)

- **Rattacher à la ligne précédente (Recommandé) :** la description viendra s'ajouter en tant que description sous l'article ou le titre précédent.

![](https://downloads.intercomcdn.com/i/o/tarury57/1849587136/cb107081b07289f4453891c29048/image.png?expires=1788618600&signature=ef65fcc411e86c7481418c008ce406f1da73c2ab3fb6d367efca36fe74dcc8ce&req=dSgjH8x2moBcX%2FMW1HO4zYmnPJAS1rNi%2BNQj%2FkDn5zQ%2Fx6wBgNXN06FxqKUO%0AVNln%0A)
- **Créer une ligne "texte libre" :** La ligne aura sa propre numérotation et apparaîtra comme un élément distinct.

![](https://downloads.intercomcdn.com/i/o/tarury57/1849588141/4c553f4a395d7f10cdf1186ad117/image.png?expires=1788618600&signature=e23fc6dda3c77f2e285faa020ec6e90c12467705c9120bf942a0a64c2f092eb2&req=dSgjH8x2lYBbWPMW1HO4zUsJ01CTlkhcyQ3tKrwsKWDZt0hGluKthIlHs2rP%0A4DhN%0A)
- **Ignorer :** La ligne ne sera pas importée.

### 3. Mapping des colonnes (Association)

C'est une étape clé où vous reliez les colonnes de votre fichier CSV aux champs d'InterFast afin que les informations soient correctement reconnues.

- **Désignation :** associez votre colonne "Désignation des articles / ouvrages" au champ **"Désignation"**.
- **Quantité :** Associez votre colonne "Quantité" au champ **"Quantité"**.
- **Prix Unitaire :** Associez votre colonne "Prix Unitaire - Vente" au champ **"Prix unitaire"**.
- **Unités :** Associez votre colonne "U" au champ **"Unité"**.

![](https://downloads.intercomcdn.com/i/o/tarury57/1849589133/95e2139a75c2e9591042f2602ac2/image.png?expires=1788618600&signature=66db13f81f1bfe46d465f2603f6f4763ecf7240eee61b3f6a5f9abcdd138c68a&req=dSgjH8x2lIBcWvMW1HO4zQkZQgHqpwNmMthBrSOBaBaJlz0TonRP0TQx%2FpQK%0A0rvQ%0A)

> ⚠️ Ne réalisez aucune association pour la colonne désignée à l'étape précédente pour la numérotation des lignes. En effet, toute association entraînerait une erreur lors de l'import du DPGF.

### 4. Vérification et Finalisation

Avant de valider, un tableau récapitulatif vous permet de contrôler visuellement que les données sont bien placées dans les colonnes adaptées.

![](https://downloads.intercomcdn.com/i/o/tarury57/1849591573/005725b13431206f2bca0ed205e8/image.png?expires=1788618600&signature=c426a71134e782956622d3d77f52cdabf09dc3975d193d6a3b448db833d05d66&req=dSgjH8x3nIRYWvMW1HO4zfuZM4Jm%2FsKODP0iftZblYgqbU0%2FI0d4DFfBCIx0%0AYvEkVcPIXm9TNgqGPaw%3D%0A)

- Si tout est correct, cliquez sur **Terminer** pour procéder à l'import du DPGF.

### 5. Résultat

InterFast génère immédiatement un nouveau devis au statut **Brouillon**.

![](https://downloads.intercomcdn.com/i/o/tarury57/1849592739/359a2e72d1aabb3453588b8bba4a/image.png?expires=1788618600&signature=4cbf19e4fe47e6b0961a05410ff1cd374350ec260022988cebc66cbe2d4a2c9f&req=dSgjH8x3n4ZcUPMW1HO4zWUXt%2Be8bPVhgMze37lU5i%2BEfGezhVZ4Q6quADTt%0AdNln74BkcXIcu6emHDg%3D%0A)

En l'ouvrant, vous constaterez que la structure hiérarchique *(sections, sous-sections)* a été respectée, vous offrant un devis propre et prêt à être édité.

![](https://downloads.intercomcdn.com/i/o/tarury57/1849593914/d407c6117dc9922061a5079efc7d/image.png?expires=1788618600&signature=cc50013423171b20a19ad21989e36b763d1a71571a7ab5017920f493ec61a5bb&req=dSgjH8x3noheXfMW1HO4zbtn2BK3MDOIduDijHIIFlpkpzWt7nOYMpkYEOq8%0A58IfSrrf71fq77dsH4Q%3D%0A)

> ⚠️ Le devis redémarre sa numérotation à 1 et ne reprend pas, *stricto sensu*, la numérotation du DPGF afin d'assurer la propre cohérence du document. 

## III. Édition et Enrichissement du Devis

Votre DPGF est importé, mais il est encore "brut". L'éditeur d'InterFast vous permet de le transformer en un devis commercial complet et rentable.

![](https://downloads.intercomcdn.com/i/o/tarury57/2464885864/44c32f5ef29e5812d407c80d6dca/image.png?expires=1788618600&signature=3ad87b659e00f6c534be74eac63702ff32d130b6db10b9f1bc7dcf81a27015fe&req=diQhEsF2mIlZXfMW1HO4zbtbZxvbjgGeUG%2FSHpMZf5YfQaWF47%2FPanK1GGee%0AxIylDrqopJpwg27pPyY%3D%0A)

### 1. Ajustement des Prix et Marges

L'import a récupéré vos prix de vente, mais vous pouvez affiner votre rentabilité ligne par ligne.

- **Saisie des Prix d'Achat :** pour chaque article, renseignez le **Prix d'achat** (fournitures). Le logiciel calculera automatiquement votre coefficient de marge en fonction du Prix unitaire de Vente - que vous pouvez également modifier.

![](https://downloads.intercomcdn.com/i/o/tarury57/1849609646/0058d1745845ed943168864a25e2/image.png?expires=1788618600&signature=f06676be29463920036fe484262ebc15766b44413297332539e03012d88d2ae5&req=dSgjH89%2BlIdbX%2FMW1HO4zTx9y9VxVWkphYTq%2BQXPMI%2FpC%2FfBzQRQhYZn2YIP%0ADDAI%0A)
- **Application d'une marge globale :** une fois les prix d'achat renseignés, vous pouvez également uniformiser votre coefficient de marge. Cliquez sur le bouton "**Modifier..."** en bas de page, puis choisissez **Coefficient de marge**.

![](https://downloads.intercomcdn.com/i/o/tarury57/1849612159/eb41788db05a30df01b092448323/image.png?expires=1788618600&signature=647b56d5c8feab42c24ca62dfa2b8593c12a9842e2ea3f3ec6ec68692d9df6dd&req=dSgjH89%2Fn4BaUPMW1HO4zQ%2BUeQsPIzO73hzbTUEING9uAx%2Bq0m1xQlPETnOd%0AOurD%0A)

Vous pourrez appliquer un coefficient unique *(ex: 2.0)* à l'ensemble des lignes dont le prix d'achat est renseigné.

![](https://downloads.intercomcdn.com/i/o/tarury57/1849612934/ef9323b8b5981d160d5f27b40412/image.png?expires=1788618600&signature=129f9bfbd03a065885613e7cb6ad38b6cd8fd3760e710bf688b57c561e347957&req=dSgjH89%2Fn4hcXfMW1HO4zelp%2FY7rZAywHWImKuRRCYwxdnxlvIG5RWfNIaub%0A3dPO%0A)
- **Application d'un taux de TVA global :** à partir du même bouton "**Modifier...**" en bas de page, choisissez l'option **Taux de TVA** pour uniformiser le taux *(ex: 10% pour de la rénovation)* sur l'ensemble du document.
​
![](https://downloads.intercomcdn.com/i/o/tarury57/1849615725/7b4b152cedbff168d9a0d7a9d952/image.png?expires=1788618600&signature=cebf6e1909193104888bac132494d0f7e0404168fa367a31507702127835ceb4&req=dSgjH89%2FmIZdXPMW1HO4zX40P5eRxqoTKWaGnV%2BfEPlPbe%2BDoBSfOHQjuPdj%0Alycf%0A)

### 2. Enrichissement depuis la Bibliothèque

Vous pouvez remplacer les lignes importées du DPGF par des articles précis de votre Bibliothèque.

- Cliquez sur le bouton "**Bibliothèque"** au niveau d'une ligne ou d'une section.

![](https://downloads.intercomcdn.com/i/o/tarury57/1849620727/069309f1bf9d5266f77077d2e0c6/image.png?expires=1788618600&signature=5fc2fcf73dce78f259d707f24d552fdf5e7364982d28205806c710d5237e31d2&req=dSgjH898nYZdXvMW1HO4zclf9cUibVbF0QhXyk0osnhzJC1tvCO5oxffm1oZ%0ADhEX%0A)
- Recherchez votre article *(ex: "Prise murale standard")* et ajoutez-le. Il s'ajoutera dans votre devis pour l'enrichir de données fiables.

![](https://downloads.intercomcdn.com/i/o/tarury57/2464892296/4822e232aeeac7ff8c1d6a48963c/image.png?expires=1788618600&signature=98611065ffb62f453746942b681398cdd9bb6a7ee264ffbcdb50d4db80ec62d3&req=diQhEsF3n4NWX%2FMW1HO4zWwLn2BdMqHdcLN5x23r3KTLrkir9ZCHJVN01xQV%0AGKjxC0AovoRRLsaeB68%3D%0A)

- Vous pouvez convertir les sections importées en **ouvrages**, en cliquant sur l'icône "..." à droite de la ligne. Pour rappel, un [ouvrage](https://help.inter-fast.co/fr/?q=ouvrage) est un ensemble d'articles dont la composition ou les prix peuvent être masqués.

![](https://downloads.intercomcdn.com/i/o/tarury57/2464895358/e1d61e5a9c78100d401ec83ae8d3/image.png?expires=1788618600&signature=f3a8693f56b4f52018bff96ae3f985a0b7b3dead6aa1714c32a4267573463505&req=diQhEsF3mIJaUfMW1HO4zVL2EhzqueJimviVT3rn7TfKPbh7zc5T03i5mHM0%0Atxz19F%2B7aplEr6l1tWw%3D%0A)

### 3. Finalisation Administrative


- **Identification du Client :** En haut du devis, utilisez la barre de recherche pour associer ce document au client concerné. Ses coordonnées s'afficheront automatiquement dans l'encart dédié.

![](https://downloads.intercomcdn.com/i/o/tarury57/1849627752/d0dae96287a316478ae684df0f5f/image.png?expires=1788618600&signature=a19cc5450f7bf251a87074103b43a4df69bfda0c9d16ee0c4c94e966067e3ac6&req=dSgjH898moZaW%2FMW1HO4zWmSaCnKSuGDWInV8%2F8KyQBkBvLdEsPVfnALZD8f%0AwHZ%2B%0A)

### 4. Validation Finale

Une fois le chiffrage terminé, changez le statut du document de Brouillon à **Finalisé**.

InterFast attribuera alors un **numéro de devis** officiel *(ex: D-INT-2511-410)*, ce qui figera le document.

![](https://downloads.intercomcdn.com/i/o/tarury57/1849630941/c125708970b792a0563b7fcf4954/image.png?expires=1788618600&signature=fead89888e85bec351375e275bc7ce185446b96f771177c104ef626ab8c9ff20&req=dSgjH899nYhbWPMW1HO4zeR2hiQQ2qYwxpg5Xp4zFuV1sqoa3Dxy40Fa7GTX%0AkP2omB%2BstMaCrJNpfV8%3D%0A)

## IV. Export et mise à jour du DPGF

Une fois votre travail de chiffrage terminé sur InterFast, il est fréquent que le client exige une réponse à son appel d'offres en complétant son fichier Excel (DPGF).

Voici comment transférer vos modifications (prix, quantités ajustées) vers le document source, sans tout ressaisir manuellement.

### 1. Export des données modifiées

Depuis la fiche de synthèse de votre devis sur InterFast :

- Cliquez sur le bouton **Actions** en haut à droite.
- Sélectionnez l'option **Exporter en CSV**.

![](https://downloads.intercomcdn.com/i/o/tarury57/2464879574/f5a64bb6a7187c82d748c1d821f4/image.png?expires=1788618600&signature=4fb6983b928ee844195ce83f045ec44c337ec89529029a316d698d0f5a125502&req=diQhEsF5lIRYXfMW1HO4zePzdRfpff4GSy5xyNvp4aRi7CvKfv0bKbICdCYJ%0ACVLI%0A)
- Vous récupérez ainsi un fichier brut contenant toutes vos lignes à jour, vos nouveaux prix unitaires et vos quantités validées.

### 2. Réintégration dans le tableur (Excel / Sheets)

La méthode la plus sûre pour ne pas "casser" le fichier de votre client est de procéder par comparaison :

- Ouvrez le fichier CSV que vous venez d'exporter dans votre tableur (Excel ou Google Sheets).
- Ouvrez en parallèle le **DPGF original** de votre client.
- Copiez les colonnes clés de votre export *(Quantité, Prix Unitaire de Vente)* et collez-les **à droite** des colonnes correspondantes dans le fichier original.

![](https://downloads.intercomcdn.com/i/o/tarury57/1849651023/aba61412197d94f87ccfbfaf5b9a/image.png?expires=1788618600&signature=666a18261db82691461410d6b96f35c69e144acdea1ed2df95cf6d936e9aa7b4&req=dSgjH897nIFdWvMW1HO4zUJvqM3FDZsKQJAwe3eDOA6VvCLvPrYuAjPF%2F3u0%0AVKgIHPEOinKmIX70qGQ%3D%0A)

- Reportez ensuite les valeurs finales dans les cases prévues à cet effet. Cela vous permettra de vérifier visuellement qu'aucun décalage de ligne ne s'est produit.

![](https://downloads.intercomcdn.com/i/o/tarury57/1849672564/34f39dd852df9d35aa53b1e5183a/image.png?expires=1788618600&signature=de7efdb242a8ad10f8b3930221480a21136e4802edd7f47bef895bbb2fe5d9d0&req=dSgjH895n4RZXfMW1HO4zaD%2F%2BBzAAMQInJvBu6SBq%2FCni7h2vwd1KmXOKhMe%0Ar4Ggxr%2BjIKudnYbP7zI%3D%0A)

 
​

### 3. Vérification des formats

Avant d'enregistrer, une vérification technique est indispensable pour que le fichier reste fonctionnel chez votre client :

- Assurez-vous que les cellules des colonnes **"Quantité"** et **"Prix Unitaires"** sont bien formatées en tant que **Nombres** *(ou Monétaire)* et non en tant que *Texte*. Utilisez le menu **Format** de votre tableur pour appliquer ce changement.

![](https://downloads.intercomcdn.com/i/o/tarury57/1849654848/1e94ebc3e17ac9351b4f69715992/image.png?expires=1788618600&signature=b82119e89af17b7d9f6844af63d77494583f534a468ab51657e855bdd1159892&req=dSgjH897mYlbUfMW1HO4zSCHAR5TP08XCMJHcfqkTkE0TxwRfE33CueN9ckL%0ARL9x%0A)
- Si ces données sont considérées comme du texte, les formules de calcul automatique *(totaux, sous-totaux)* du fichier Excel de votre client ne fonctionneront plus.
​

### 4. Finalisation

Une fois les données reportées et vérifiées :

- Enregistrez ou téléchargez votre fichier au format attendu par le client (généralement **.xlsx** ou **.csv**).

![](https://downloads.intercomcdn.com/i/o/tarury57/1849655917/6be729cce9734b74e198ff5ccd68/image.png?expires=1788618600&signature=39a6c37503d17cf156d4314c57aaf139993ee0a2e06f0858ec8b9422c1b42365&req=dSgjH897mIheXvMW1HO4zVGlBmqHA61Q2LBg0NwOr9olIIwvBpSkVsyd%2BgsV%0ALVZO%0A)
- Votre DPGF est maintenant chiffré, conforme à la demande initiale, et prêt à être envoyé.

##  V. Questions fréquentes (FAQ)


Ce blocage arrive généralement pour deux raisons :
- L'ancien éditeur a du mal à supporter la taille du document. *Solution :* Basculez sur le Nouvel Éditeur (V2).
- Lors de l'import, vous avez "mappé" (associé) la colonne de numérotation à l'[étape 3](#h_9d8c188333). 
*Solution :* Supprimez ce brouillon et recommencez l'import en laissant la ligne "Numérotation" sur *Ignorer* à l'étape de l'association des colonnes

​


Non, les imports et exports de DPGF complexes sont exclusivement réservés aux entreprises ayant souscrit à l'abonnement **Business**
​


Oui. La structure (les sections imbriquées) est parfaitement respectée, mais InterFast redémarre sa propre numérotation (1., 1.1, 1.2) pour garantir la cohérence technique du document dans le logiciel.

## Conclusion

L'import de DPGF est une fonctionnalité puissante qui transforme une corvée administrative en un avantage concurrentiel.

1. **Gain de temps massif :** fini la ressaisie ligne par ligne de marchés de plusieurs pages.
2. **Fiabilité :** vous éliminez les erreurs de copie (prix, quantités) et les oublis.
​
3. **Professionnalisme :** vous produisez instantanément des documents structurés et conformes aux attentes de votre client. En cas d'acceptation, votre devis pourra être converti en facture en 2 clics.
​

L'import de DPGF transforme une tâche administrative longue et fastidieuse en un véritable avantage concurrentiel. Vous éliminez les risques d'erreurs de copie, vous chiffrez plus rapidement vos appels d'offres, et une fois le devis accepté, vos situations de travaux mensuelles se généreront en quelques clics ! 🚀

Mis à jour le : 05/08/2026
