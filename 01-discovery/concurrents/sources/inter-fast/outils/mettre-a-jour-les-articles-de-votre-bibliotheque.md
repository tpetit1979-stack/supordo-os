---
source: https://help.inter-fast.co/fr/articles/11651968-mettre-a-jour-les-articles-de-votre-bibliotheque
categorie: Outils
titre: Mettre à jour les articles de votre Bibliothèque
date_recuperation: 2026-09-05
---

# Mettre à jour les articles de votre Bibliothèque

> **🛠️ Gagnez du temps sur la gestion de vos articles**
> Vous souhaitez ajuster rapidement vos tarifs, descriptions ou références produit dans InterFast ? Bonne nouvelle : vous pouvez mettre à jour votre bibliothèque d’articles en masse en important un  fichier CSV.
> Suivez le guide pour tout faire en quelques étapes simples !

## I. Quel est l'intérêt de l’import pour mettre à jour vos articles ?

Lorsque vous avez déjà une base d’articles en place dans InterFast, il peut être fastidieux de modifier vos tarifs ou descriptions un par un lorsque votre fournisseur fait évoluer des prix par exemple. 

Grâce à la fonction d’import, vous pouvez :

- Modifier vos prix de vente ou coûts d'achat en masse
- Gérer plus facilement les évolutions de catalogue fournisseurs

```
💡 L’unique condition : utiliser le fichier d’export fourni par InterFast comme base, car il contient les ID uniques de chaque article nécessaires pour identifier les éléments à mettre à jour.
```

> **ℹ️ Vous souhaitez plutôt partager votre catalogue avec une autre entreprise ?**
> InterFast permet également de **partager une bibliothèque d’articles** avec une autre entreprise.
> 
> ​[Découvrez comment fonctionne le partage de bibliothèque](https://help.inter-fast.co/fr/articles/16780447-partager-sa-bibliotheque-d-articles-et-d-ouvrages).

## II. Étapes détaillées

###  A. Exporter la base actuelle

Avant toute mise à jour, commencez par exporter votre bibliothèque existante :

- Rendez-vous dans l’onglet **Bibliothèque** depuis le menu InterFast.
- Cliquez sur le lien **Exporter** tout en bas de la page de listing des articles.
- Un fichier CSV contenant tous vos articles sera mis à disposition pour téléchargement.

![](https://downloads.intercomcdn.com/i/o/tarury57/1587824751/764545671eb0631531a864598231/CleanShot+2025-06-25+at+16_03_28%402x.png?expires=1788674400&signature=6ca7f4cdc6ed09babc44207e31b73b8271adf01d2e7315744626c9e51ac3110e&req=dSUvEcF8mYZaWPMW3nq%2BgYJJJq2vFBk1Bnpt%2BqpAsCYTbIsIaHIwNCdGV4O2%0A15o1b4tsAukGMVal9ml6E9LdTdU%3D%0A)

![](https://downloads.intercomcdn.com/i/o/tarury57/1587852665/f25e886d32b12a19402f0f98d847/CleanShot+2025-06-25+at+13_09_55%402x.png?expires=1788674400&signature=e84792fa7b16608a27872e12929627dcb5f48a60dc84651acdad384f08c69d93&req=dSUvEcF7n4dZXPMW3nq%2BgdX0Wbjcmw3aKoL3a2yGHDr%2FyXw6CgUMWTEnDYHS%0A2CiLLXpz4wd9bxLBF1GnRc6cuzA%3D%0A)

Ce fichier contient toutes les colonnes essentielles, dont la référence** unique** de chaque article (indispensable pour que l’import fonctionne comme une mise à jour et non comme une création).

### B. Modifier les données dans le fichier CSV

Ouvrez le fichier CSV dans Excel, Google Sheets ou un tableur compatible.
Vous pouvez modifier librement les colonnes suivantes :

- Prix d'achat
- Prix de vente
- Taux de TVA

⚠️ **Peuvent être considéré comme identifiant unique** : 

- La référence InterFast (*ART0105 par exemple*)
- Le code fournisseur
- Le code fabricant
- L'indentifiant interne InterFast (Uniquement pour l'utilisation de l'API)

Donc ne supprimez pas ces colonnes, car elles permettent (selon votre choix) à InterFast d’identifier les articles existants à mettre à jour.

Une fois vos modifications effectuées, enregistrez le fichier au **format .CSV.**

![](https://downloads.intercomcdn.com/i/o/tarury57/1591566123/f4b8ece5feb23c5a0d11efd8cdad/CleanShot+2025-06-27+at+15_25_09%402x.png?expires=1788674400&signature=bcd20f923d16533544dee48d6a8e24731c25f68124485d036d799d6c7dd6be32&req=dSUuF8x4m4BdWvMW3nq%2BgdeS95I88vOZ%2B4h4vcSn95UPrig32lC70GWxJO%2F%2B%0AeaeCz0bwu3X%2BdmzSh0tSkCVEP5k%3D%0A)

** **

### C. Importer le fichier mis à jour dans InterFast

De retour sur InterFast :

- Cliquez sur le bouton **Importer** dans la bibliothèque, en haut à droite, puis sur "**Une mise à jour de prix**" :

![](https://downloads.intercomcdn.com/i/o/tarury57/1587855081/b50f45e526a8c12e9c1e9bf403cb/CleanShot+2025-06-25+at+11_48_12%402x.png?expires=1788674400&signature=54d9f54c5b9b43cddf81253eb48dcb4d3a5654607b054547dd298a93d258f529&req=dSUvEcF7mIFXWPMW3nq%2Bgarzb2JV0%2B1pUbTcgcuByyYa%2BRkaY8TmCY%2FLCNZ9%0AcUu8XNxKqvBjp9UkpoEuUBkWVyY%3D%0A)

![](https://downloads.intercomcdn.com/i/o/tarury57/1587857589/e41a3fe0193144acc1d6cad55c1e/CleanShot%2B2025-06-25%2Bat%2B16_19_23-402x.png?expires=1788674400&signature=5f87645fc58bb52262c812667ee8d50e1a71f49650ebb0757b85b996503a9693&req=dSUvEcF7moRXUPMW3nq%2BgRNLdbWAcRMuVh3GvWNzHdhsE5%2FRopW1LPV47Hf4%0A4ivt84OJGTbTkh8WTMJDFgd19cU%3D%0A)

- Glissez-déposez votre fichier CSV modifié ou cliquez pour le sélectionner et ensuite, cliquez sur "**Suivant**" :

![](https://downloads.intercomcdn.com/i/o/tarury57/1587862338/9ea423e8b1b9cdfb095267aca0ad/CleanShot+2025-06-25+at+13_13_40%402x.png?expires=1788674400&signature=56149dd245cad060d6c50a556092abaf6097300d71f42f5f55365277c7c57759&req=dSUvEcF4n4JcUfMW3nq%2BgWjgaSvr15yss1QU13BPQvFInlnFZ0qM8Of3Ssoa%0AaHHvMIFaLy5fZtz9d4LwnWqO3Gk%3D%0A)

- *Identification des articles* :  l’identifiant unique qui permettra à InterFast de retrouver chaque article dans votre bibliothèque. Sélectionnez celui que vous utilisez dans votre fichier, ensuite faites-le correspondre au champ prévu côté InterFast et cliquez sur "**Suivant**" :

![](https://downloads.intercomcdn.com/i/o/tarury57/1591544257/cae5f1f2ca97fc0758b44a71fe89/CleanShot+2025-06-27+at+15_29_03%402x.png?expires=1788674400&signature=43c39d9be012f9fc4e1472d00bc352d75a23f46ad5365b5560416cedf74ccf49&req=dSUuF8x6mYNaXvMW3nq%2BgdbO1szfvGnY5yTN8C2Ix9e4wcwWZ6%2Bmh5lFpKSw%0A3v3g6Wn1OW3kZN%2FMrqT0neEI98o%3D%0A)

- *Vérifiez les correspondances de colonnes : *

![](https://downloads.intercomcdn.com/i/o/tarury57/1591547895/c66840c88c74932aefcbd59d8439/Session+2025-06-27+15_31_40.png?expires=1788674400&signature=36310c4b32179aa96f5909498a13ca150f81a608e4aace211eb81f7592a50df5&req=dSUuF8x6molWXPMW3nq%2BgZJXeOzlaA3s0Qw2wHBBjjlilbDU9Ds2y60e0Zy0%0A8GWrmd9fdVZLpvMiBt4Lm8fyRgM%3D%0A)

- Vérifier les colonnes à mettre à jour avant de lancer l’import :

![](https://downloads.intercomcdn.com/i/o/tarury57/1591556582/d39ac9abdcf55512d6e351d50d65/CleanShot+2025-06-27+at+15_37_05%402x.png?expires=1788674400&signature=21f556ce49c3f1672563aab8bdfc0002269c914616ad85d64e0480ac8710184c&req=dSUuF8x7m4RXW%2FMW3nq%2BgSPchY8WDcoy9SPBTcbiCcOvROmAEsDy4wx%2FtGhL%0AcdlfM148tVJBMBwZoKgOW7iZtG4%3D%0A)

Une fois l’import terminé, vous pouvez le retrouver dans votre bibliothèque d’articles, en bas à droite de l’écran, ainsi que dans la rubrique "**Imports**" accessible depuis vos paramètres.

*Bibliothèque :*

![](https://downloads.intercomcdn.com/i/o/tarury57/1591560039/414366551fc60c37a3df1d3de3b3/CleanShot+2025-06-27+at+15_38_43%402x.png?expires=1788674400&signature=a9098a55170556f7bd4a835c5354c7a9484be2bc9711e918b43c5fdf02121a67&req=dSUuF8x4nYFcUPMW3nq%2BgX63My4u6lw39hSiIhcqyNvpsRMJyixmmlUbKjK0%0A10cQaxhOqixpZGrOEU1dMKl98tc%3D%0A)

*Paramètres > Imports : *

![](https://downloads.intercomcdn.com/i/o/tarury57/1591562676/3fa115c055ff247cb0947a208237/CleanShot+2025-06-27+at+15_40_11%402x.png?expires=1788674400&signature=663d1d17d3010a4bfe3b31d09ee35f2cfa126d9967e557e70a3c205cae17e906&req=dSUuF8x4n4dYX%2FMW3nq%2BgYg2npKP6v7WaCjsofasfXcy30g0Cp8kgzOnX6Yj%0AiBFIYvJicIPYpnquG5ZNBqbmTKE%3D%0A)

⏳ Vos articles existants seront mis à jour selon les nouvelles informations.

*Changement de tous les prix de vente dans la bibliothèque : *

![](https://downloads.intercomcdn.com/i/o/tarury57/1591569124/d5a8fde65e089eeaa7085318e993/CleanShot+2025-06-27+at+15_45_04%402x.png?expires=1788674400&signature=88e0d3d1d427c0ea1c7e85e3d89f4dd6443a03c12b26570bddafe1d9cc91a3cc&req=dSUuF8x4lIBdXfMW3nq%2BgdtPiQIQIqWhgjcF8WH5D7UtU1nirpdQGBb%2FrZnm%0AtwFh9EknRvcc2ugBkSdwmfndi%2BQ%3D%0A)

### D. Que se passe-t-il en cas d’erreur ? 

⚠️ **L’import est irréversible** : une fois votre fichier envoyé, les données de votre bibliothèque d’articles seront définitivement mises à jour. Il ne sera pas possible de revenir en arrière.

C’est pourquoi il est essentiel de préparer votre fichier CSV avec soin et de vérifier toutes les informations avant de procéder à l’import.

✅ Nos conseils pour limiter les risques :

- Conservez une copie de votre fichier d’export initial, pour pouvoir restaurer vos données si besoin.
- Si vous avez de nombreuses lignes à modifier, commencez par tester l’import avec un fichier de 2 ou 3 articles, afin de valider le bon format et la correspondance des colonnes.

Prenez le temps de bien vérifier votre fichier – mieux vaut prévenir que corriger.

___________________________________________________________

## Conclusion

Grâce à l’import CSV, la mise à jour de votre bibliothèque de prix devient un jeu d’enfant. Plus besoin de tout modifier manuellement : un export, quelques ajustements dans un tableur, un import et le tour est joué. 🚀

Mis à jour le : 04/09/2026
