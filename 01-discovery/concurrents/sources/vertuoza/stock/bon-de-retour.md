---
source: https://intercom-help.eu/vertuoza/fr/articles/133087-bon-de-retour
categorie: Stock
titre: Bon de retour
date_recuperation: 2026-09-05
---

# Bon de retour

Avec Vertuoza, vous avez la possibilité de créer des bons de retour. 

Il est généralement émis lorsqu'il est nécessaire de renvoyer des marchandises ou des produits à un fournisseur ou de les réintégrer dans le stock de l'entreprise après une sortie. 

Ils seront valorisés dans la rentabilité du chantier au niveau des commandes matériaux.

Par exemple : 

imaginons que j’ai fait un bon de sortie de 10 plaques d’OSB et que finalement les ouvriers n'en ont utilisé que 6, je fais un bon de retour de 4 plaques OSB afin de remettre la fourniture dans mon stock Vertuoza.

### **Paramétrage du bon de retour :**

Avant de commencer, il y a 3 étapes importantes à suivre au niveau du paramétrage.

**Stock**

1. **Préférences** *(Paramètres > Stock > **Préférences**)*

- Choisir le nombre de niveaux pour pouvoir cartographier la localisation des emplacements de stock.
- Choisir l’intitulé de ces niveaux, par exemple : Entrepôt - Allée - Box.
- **Réapprovisionnement automatique** - **Oui** : afin qu’un brouillon de bon de commande soit créé par défaut quand la quantité min. de cette fourniture est atteinte.
- “**Enregistrer**”.

1. **Emplacements** *(Paramètres > Stock > **Emplacements)***

- Une zone de recherche.
- Des filtres peuvent être appliqués.
- Activer / Désactiver l’affichage des sous-niveaux.
- Le tableau reprenant les informations.
- Les boutons d’actions à l’extrême droite du tableau (placez votre curseur sur chaque bouton pour en connaître la signification).

**Créer un emplacement**

- Cliquer sur “**+ Nouveau**”.
- Cliquer sur l’intitulé 1 que vous avez créé, par exemple : Entrepôt.
- Insérer un ou plusieurs entrepôts.
- “**Soumettre**”.
- Le ou les entrepôts sont ajoutés.
- Cliquer sur **“+ Nouveau”** (pour ajouter un deuxième niveau).
- Cliquer sur l’intitulé 2 que vous avez créé, par exemple : Allée.
- Sélectionner l’intitulé 1 (Entrepôt).
- Insérer une ou plusieurs Allées.
- “**Soumettre**”.
- Le ou les allées liées à votre entrepôt sont affichées dans le tableau.
- Cliquer sur “**+ Nouveau**” (pour ajouter un troisième niveau).
- Cliquer sur l’intitulé 3 que vous avez créé, par exemple : Box.
- Sélectionner l’intitulé 1 (Entrepôt).
- Sélectionner l’intitulé 2 (Allée).
- Insérer un ou plusieurs Box.
- “**Soumettre**”.
- Le ou les boxs liés à votre entrepôt et votre allée sont affichés dans le tableau.

**Fourniture** *(Bibliothèque > Composants)*

- Des filtres peuvent être appliqués.
- Une zone de recherche.
- Bouton Action : import ou export des composants.
- Le tableau reprenant les informations.
- Les boutons d’actions à l’extrême droite du tableau (placez votre curseur sur chaque bouton pour en connaître la signification).

**Paramétrage à effectuer :**

- Filtrer sur **“Type”.**
- Sélectionner **“Fourniture”**.

Ou créer un nouveau composant de type fourniture (Article : Composants).

- Cliquer à droite sur le bouton d’action : Editer (crayon).
- Sous **“Géré en stock”**, cliquer sur le bouton grisé **“non”** afin qu’il soit activé.
- Sélectionner l’emplacement par défaut afin que la fourniture soit liée à cet emplacement.
- Ajouter le code EAN si vous en avez un, qui est le code-barres de votre fourniture.
- Ajouter la quantité minimum et maximum de marchandise (si vous avez activé le **Réapprovisionnement automatique** dans vos préférences de stock, comme expliqué ci-dessus, par défaut un brouillon de bon de commande sera créé quand le min. est atteint).
- **“Soumettre”**.
- La fourniture pourra dès à présent être gérée dans votre stock.

**Fournisseurs** *(Contacts > Entreprises)*

- Des filtres peuvent être appliqués.
- Une zone de recherche.
- Bouton Action : import ou export des composants.
- Le tableau reprenant les informations.
- Les boutons d’actions à l’extrême droite du tableau (placez votre curseur sur chaque bouton pour en connaître la signification).
- Le bouton Action(s) pour faire des imports / exports de vos Entreprises. (Article : Entreprises)
- Le bouton **“+ Nouveau”** pour créer une nouvelle entreprise.

**Paramétrage à effectuer :**

- Remplir le champ Franco / Frais.
- Franco : le montant min. à payer pour ne pas devoir payer les frais de transport.
- Frais : le montant de frais de transport à payer si le prix n’atteint pas le franco.
- **“Soumettre”**.

### **Navigation dans l'écran du Bon de retour :**

Le fonctionnement général et la navigation sont similaires aux autres écrans de Vertuoza :

- Des filtres peuvent être appliqués.
- Une zone de recherche.
- Le tableau reprenant les informations.
- Les statuts du bon de retour :
- Brouillon
- Terminé : la valeur de votre bon de sortie sera comptabilisée dans la rentabilité de votre chantier seulement après avoir confirmé sa création.
- Les boutons d’actions à l’extrême droite du tableau (placez votre curseur sur chaque bouton pour en connaître la signification).
- Le bouton "**Nouveau**" pour créer un nouvel élément.

### **Créer un bon de retour :**

Sur la base de vos commandes faites au préalable ainsi que de vos bons de sortie, vous pouvez aller créer un bon de retour pour la marchandise qu’ils y a à remettre en stock. Vous pouvez ajouter de la fourniture provenant de plusieurs fournisseurs différents.

1. Cliquer sur “**Nouveau**”.
2. Brouillon : mon stock n’est pas encore impacté.
3. Remplir le champ **“Référence”.**
4. Remplir le champ **“Intervention”** OU **“Chantier”** lié à cette fourniture.
5. Encoder la fourniture (provenant de votre bibliothèque).
6. Quantité à faire revenir dans chaque emplacement.

- Stock actuel - Réel : la quantité à l’instant T.
- Stock actuel - Théorique : la quantité à l’instant T + commandes qui n’ont pas encore été livrées.
- Stock Actuel - Minimum : la quantité min. de la marchandise (définie dans les composants de type fourniture, voir ci-dessus).
- Stock Actuel - Maximum : la quantité max. de la marchandise (définie dans les composants de type fourniture, voir ci-dessus).
- Prix unitaire.
- Total.
- Cliquer sur la corbeille à droite de la ligne pour supprimer une fourniture.
- Cliquer sur le + à droite de la ligne pour ajouter une fourniture.
- Insérer une remarque interne.
- **“Soumettre”.**

Mis a jour le : 02/09/2026
