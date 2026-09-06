---
source: https://intercom-help.eu/vertuoza/fr/articles/145114-remplir-son-stock-pour-la-premiere-fois
categorie: Stock
titre: Remplir son stock pour la première fois
date_recuperation: 2026-09-05
---

# Remplir son stock pour la première fois

Pour pouvoir utiliser le stock Vertuoza, il faut faire un premier inventaire pour le faire correspondre à votre stock physique. Pour cela, certains éléments doivent déjà être en place dans votre Vertuoza.

### Préparer les fournitures qui seront gérées en stock dans Vertuoza

Les fournitures présentes dans le stock doivent d’abord exister dans la partie **Composants** de votre bibliothèque de prix et être configurées d’une certaine manière.

### Si les composants sont déjà présents dans la bibliothèque :

- Aller sur la page Composants dans Vertuoza
- Exporter la liste de composants via le bouton **Actions > Exporter**
- Compléter le fichier de la colonne I (Stock Y/N) à la colonne M (Quantité max)
- **Dans la colonne I** : indiquer Y sur les lignes de fournitures qui seront gérées en stock. Vous pouvez ensuite filtrer sur ces lignes ou supprimer les autres dans le fichier
- **Dans la colonne K** : Indiquer à quel emplacement du stock sera rangée la fourniture. Ces emplacements seront ensuite créés dans Vertuoza lors de l’import. Vous pouvez avoir jusqu’à trois niveaux d’emplacement, par exemple des entrepôts en niveau 1, des allées en niveau 2 et des sections en niveau 3. Pour indiquer qu’une fourniture se trouve dans l’entrepôt A, Allée 5, Section B, écrire : Entrepôt 1 | Allée 5 | Section B. Il n’est pas obligatoire d’avoir plusieurs niveaux d’emplacement, vous pouvez simplement avoir différents niveau 1, par exemple : Entrepôt, Atelier, Camionnette, Garage…
- **Dans la colonne K** (non obligatoire) : Indiquer le code barre du produit si vous l’avez, cela vous permettra de vous servir d’une douchette de scan lors des inventaires pour gagner du temps et retrouver plus vite la référence
- **Colonne L et M** : Indiquer les quantités minimum et maximum qui doivent être en stock pour cette fourniture. La quantité minimum pourra permettre de générer automatiquement un bon de commande quand on passe en dessous (si activé, voir [Préférences du stock](https://intercom-help.eu/vertuoza/fr/articles/133081-preferences-du-stock)), la quantité max est pour information
- Enregistrer le fichier au format **Excel**
- Retourner sur la page Composants dans Vertuoza
- Importer le fichier via le bouton **Actions > Importer**

**Les composants qui ont été complétés/modifiés seront mis à jour dans Vertuoza.**

Si vous commencez avec la bibliothèque de prix Vertuoza et n’avez pas encore de composants

Vous pouvez soit importer une liste de composants, soit les créer à la main (voir l’article sur [les composants](https://intercom-help.eu/vertuoza/fr/articles/132328-composants))

Si les composants sont importés, remplir les mêmes informations qu’indiqués plus haut (colonnes A à M du template d’import fourni).

Si vous créez les composants à la main :

- Aller d’abord dans Paramètres > Stock > Préférence et définissez vos **niveaux d’emplacements** (Ex : Niveau 1 : Entrepôt, Niveau 2 : Allées, Niveau 3 : Section)
- Aller dans paramètres > Stock > Emplacement et créer les **emplacements du stock** (EX : Entrepôt Bruxelles, Entrepôt Paris, Entrepôt Bruxelles > Allée 5…)

Vous pouvez désormais créer vos composants qui seront gérés en stock !

Lors de leur création, cocher “Géré en stock”, sélectionner l’emplacement où cette fourniture se range, et les quantités minimum et maximum qui doivent être en stock pour cette fourniture. La quantité minimum pourra permettre de générer automatiquement un bon de commande quand on passe en dessous (si activé, voir [Préférences du stock](https://intercom-help.eu/vertuoza/fr/articles/133081-preferences-du-stock)), la quantité max est pour information.

![](https://downloads.intercomcdn.eu/i/o/11095831/44e0cb6597fd50b55d113e85/Capture+d%E2%80%99e%CC%81cran+2024-02-28+a%CC%80+16_28_50.png?expires=1788634800&signature=9415dc20509c4fea3b418a93e82d40048197a28356c04cf375aafe29f170d9d9&req=0dRvzF3yrzZk2hL085ZhoWIrc8DnvdcFK5zwNmWTrBRIMhJZWMs5f1cbRLQI%0A8dgDwlMgfDBAFKAQ%0A)

***ASTUCE :**** Indiquez dès le début le fournisseur principal pour chaque composant, cela permettra de générer des bons de commandes et de les envoyer au fournisseur en quelques clics.*

### Faire son premier inventaire pour remplir son stock

Bravo, vous avez défini les fournitures qui peuvent être stockées chez vous et renseigné toutes les informations nécessaires. Vous allez désormais pourvoir faire un premier inventaire pour indiquer quelle quantité de chaque fourniture se trouve actuellement dans votre stock.

### Préparer le fichier pour l’import d’inventaire

Cet inventaire se fera également via un import de fichier. Pour les suivants, vous pourrez les faire directement depuis Vertuoza (voir l’article [Inventaire](https://intercom-help.eu/vertuoza/fr/articles/133090-inventaire)).

- Retourner sur la page Composants de la Bibliothèque de prix et exporter de nouveau la liste
- Filtrer la liste pour n’avoir que les composants gérés en stock
- Ajouter une colonne Quantité
- Indiquer pour chaque composant la quantité actuellement présente dans votre stock
- Supprimer toutes les colonnes sauf **IDENTIFIANT_FOURNITURE, IDENTIFIANT_EMPLACEMENT, QUANTITE.** Les trois colonnes doivent être complètes.
- Enregistrer le fichier au format **.csv**
![](https://downloads.intercomcdn.eu/i/o/11095839/49e9a03ea138613d13b26457/Capture+d%E2%80%99e%CC%81cran+2024-02-28+a%CC%80+16_30_02.png?expires=1788634800&signature=c45cadabddd5101a335d0fe834b2bac11346305275a96cd7df6ef06782285126&req=0dRvzF3yrz5k2hL085ZhoX2BnxD3h3GgUvz%2BdSzIk88ANvO9K%2FSbC0rEjEq8%0AzQ%3D%3D%0A)

### Importer son inventaire de stock dans Vertuoza

Tout est prêt, il ne reste plus qu’à importer le fichier pour remplir le stock dans Vertuoza et commencer à l’utiliser.

- Aller sur **Stock > Inventaires**
- Cliquer sur Créer un inventaire
- Choisir Type d’inventaire : **Par importation**, puis Créer

Vous êtes redirigé sur la page de détail de l’inventaire.

- Cliquer en haut sur **Importer un inventaire**
- Sélectionner le fichier **.csv**
- Vérifier et ajuster les quantités si nécessaire
- Quand tout est ok : **Clôturer l’inventaire**

Voilà, votre stock Vertuoza correspond à votre stock réel ! Vous pouvez désormais passer une [commande de stock](https://intercom-help.eu/vertuoza/fr/articles/133085-commande-de-stock), générer un [bon de sortie](https://intercom-help.eu/vertuoza/fr/articles/133086-bon-de-sortie-de-stock) ou [de retour](https://intercom-help.eu/vertuoza/fr/articles/133087-bon-de-retour) pour chantier, faire un [bon de transfert](https://intercom-help.eu/vertuoza/fr/articles/133088-bon-de-transfert) pour déplacer des fournitures d’un emplacement à un autre, [visualiser votre stock](https://intercom-help.eu/vertuoza/fr/articles/133092-etat-des-stocks) et les [mouvement en cours](https://intercom-help.eu/vertuoza/fr/articles/133093-mouvement-des-stocks), ou refaire un [inventaire](https://intercom-help.eu/vertuoza/fr/articles/133090-inventaire).

Mis a jour le : 02/09/2026
