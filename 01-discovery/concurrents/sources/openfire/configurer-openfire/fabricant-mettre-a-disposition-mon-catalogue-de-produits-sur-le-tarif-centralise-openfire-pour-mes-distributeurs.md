---
source: https://support.openfire.fr/hc/fr/articles/17228367601180-Fabricant-Mettre-%C3%A0-disposition-mon-catalogue-de-produits-sur-le-Tarif-Centralis%C3%A9-OpenFire-pour-mes-distributeurs
categorie: Configurer OpenFire
titre: Fabricant: Mettre à disposition mon catalogue de produits sur le Tarif Centralisé OpenFire pour mes distributeurs
date_recuperation: 2026-09-05
---

# Fabricant: Mettre à disposition mon catalogue de produits sur le Tarif Centralisé OpenFire pour mes distributeurs

Vous souhaitez mettre à disposition votre catalogue de produits sur le Tarif Centralisé OpenFire et souhaitez connaître les conséquences de vos mises à jour pour vos distributeurs connectés. Cet article vous indique les modalités de mise à jour disponibles et les procédures associées.

Cet article contient les sections suivantes:

- [Quelles informations sont à transmettre dans le Tarif Centralisé ?](#h_01JE63Y2HXXZPZH3BBC6DBB1TP)
- [Le paramétrage de mes marques](#01JE65HWPTNTGHRM15YY1JZQGF)
- [Modalité 1: Je transmets mes données au format Excel à OpenFire](#01JE63YR76VJE36KJ44EDG1DC9)
- [Modalité 2 : J'importe moi-même mes tarifs sur le logiciel](#01JE65HWPTNTGHRM15YY1JZQGF)
  - [Différents types d'avertissements à l'import](#h_01JE6AWN03VDXQ4WBHCA9RKYPG)
  - [Synthèse de l'import](#01JE6BAFT7FWWQHJGFCZBYAXZ7)
- [Produits retirés du catalogue](#01JE6BK1NGEXTM0S83BX5BXEPE)
- [Création, scission, fusion et archivage de marques](#01JE6D2H3MY6JN159PZPDHAJWQ)

# Les données éligibles à l'intégration

Le Tarif Centralisé permet de regrouper en une unique base de données toutes les informations tarifaires et techniques associées aux produits de votre catalogue.

Les données suivantes sont indispensables à l'enregistrement d'un produit dans votre base centralisé.

- **La référence interne du produit***: il s'agit du code produit **unique**.
- **La date de mise à jour du tarif***
- **La marque du produit***
- **Le modèle du produit***
- **La catégorie (ou famille) du produit:* **cette catégorie permet à vos distributeurs de configurer leurs conditions de remises par catégories de produits et d'afficher les produits dans des sections dédiées dans leurs devis.
- **Le nom de l'article***
- **Le prix public hors taxe conseillé*: **en euros.
- **Le prix d'achat: **en euros. *(Optionnel si vous êtes en Prix Simplifiés)*

D'autres informations sont intégrées pour enrichir les articles dans le Tarif Centralisé telles que:

- **Le secteur métier du produit: **Cheministe, Photovoltaïque, Isolation,...
- **Les données techniques des produits: **ces données techniques sont dépendantes du secteur métier. Pour les produits du secteur cheministe nous intégrons la puissance nominale, le rendement, les émissions de CO, COV, COG, poussière (en % et mg/Nm³), l'indice de performance i, la puissance énergétique saisonnière,...
- **La description du fabricant: **ce champ texte peut-être utilisé pour apporter des précisions sur le produit, qui n'ont pas leur place dans le nom.
- **La normes des produits**
- **L'éco-taxe et éco-contribution**
- **Les visuels des produits: **une URL renvoyant vers une image à télécharger
- **Les fichiers techniques, manuels d'installation, guides d'entretien et d'utilisation** associés: au format PDF.

# Le paramétrage de mes marques

Avant d'importer vos tarifs, vous devez déterminer si votre marque sera:

- **En prix simplifiés**: Vous ne fournissez qu'un prix public conseillé Hors Taxe (ppht) ou qu'un prix d'achat et vos utilisateurs connectés définissent des conditions de remises. Vous devez alors fournir une remise indicative dans votre configuration de marque pour l'import:
  - Si vous communiquez uniquement un ppht, le logiciel applique la remise pour calculer le prix d'achat
  - Si vous communiquez un prix d'achat uniquement, le logiciel applique la remise pour calculer le ppht. Dans ce cas, il faut cocher la case **"basé sur prix net"**
- **En prix public / prix d'achat fixé**: Vous fournissez pour chaque article un prix public hors taxe conseillé et un prix d'achat fixe. Dans ce second cas, vous ne devez pas configurer de remise dans votre marque car son application viendrait écraser le prix d'achat que vous fournissez.
- **En prix simplifié pour certaines catégories, en prix public / prix d'achat fixé pour d'autres: **Dans cette situation mixte, ne configurez pas de remise de marque mais configurez une remise pour les catégories de produits qui sont en prix simplifié uniquement.

Voir l'article [Définir mes conditions tarifaires sur les produits du Tarif Centralisé](https://support.openfire.fr/hc/fr/articles/17578765907484)

# Modalité 1: Je transmets mes données au format Excel à OpenFire

Le format de fichier de standard pour la communication des données produits entre le fabricant et les distributeurs est le format **FAB-DIS**. Si votre logiciel usine vous permet d'exporter du FAB-DIS, vous pouvez nous le transmettre tel quel et nous le convertiront dans notre format d'import.

Si vous ne disposez pas d'un fichier FAB-DIS, n'hésitez pas à nous transmettre un **fichier Excel ou csv** avec les informations décrites précédemment (une ligne par produit).

**Cas particulier des media: **Les media tels que les photos des produits sont à nous transmettre

- soit dans un dossier avec la référence interne du produit comme nom du fichier .jpeg ou .png
- soit dans le tableur du fichier tarif avec l'url du media correspondant à la référence interne du produit

💡Pour vous aider, nous vous mettons à disposition un [fichier d'import de tarifs.](https://docs.google.com/spreadsheets/d/1SuhTPlsxkJroFyOhiTrQ-nYVSozGT_l9/export?format=xlsx)

# Modalité 2 : J'importe moi-même mes tarifs sur le logiciel

Si vous choisissez d'importer vous-mêmes vos tarifs, connectez-vous à votre base fabricant: f10-xxx.openfire.fr.

Vous trouverez le guide pour définir votre construire votre fichier d'import sur [cet article](https://support.openfire.fr/hc/fr/articles/18848702816924).

Les tarifs s'importent *via* le module OpenImport: Configuration > OpenImport > Créer

| **Champ** | **Valeur à compléter** |
| --- | --- |
| **Type d'import** | Articles |
| **Date** | Conserver la date du jour |
| **Fichier** | Chargez votre fichier Excel ou csv |
| **Nom** | Tarif [Marque] [Date] |
| **Préfixe de référence** |  |
| **Séparateur de champs** |  |

Cliquer sur **Simuler l'import** pour vérifier si le fichier est conforme. Si vous n'avez aucun avertissement, vous pouvez cliquer sur **Importer** puis **Sauvegarder** votre import.

⚠️ Avertissement: Les produits déjà présents dans votre base Tarif Centralisé qui ne sont pas dans votre fichier d'import **demeurent inchangés**: ils ne sont ni archivés, ni modifiés. La date du tarif associée à ces articles est inchangée.

## Différents types d'avertissements à l'import

### Ajout d'une nouvelle catégorie interne

Avertissement: "*Ajout de la configuration pour la catégorie xxx"*

Ce message signifie que la catégorie du produit de l'article n'est pas configurée dans votre marque. Rendez-vous dans Vente > Configuration > Marque > Correspondance des catégories d'articles pour associer à la nouvelle catégorie d'origine créée à une catégorie interne.

Note: Lorsque vous créez ou modifiez des catégories de produits, nous vous invitons à prévenir vos distributeurs connectés. Ces catégories ont des conséquences sur leurs sections de devis et leur configuration de prix.

### Une référence produit est en doublon

Avertissement: *"xxx réf. xxx existe en N exemplaires dans le fichier d'import. Seule la première ligne est importée"*

La référence interne d'un produit doit être unique. Si vous rencontrez ce message, nous vous invitons à supprimer le doublon dans votre fichier d'import pour vous assurer que la ligne importée contienne les informations correctes.

## Synthèse de l'import

Ce tableau de synthèse visible dans l'OpenImport vous permet de vérifier la cohérence entre le nombre d'articles créés et le nombre d'articles mis à jour et votre fichier d'import.

![](https://support.openfire.fr/hc/article_attachments/17232094193436)

Si vous constatez un nombre anormalement élevé d'articles ajoutés alors que vous avez peu de nouvelles références dans votre catalogue, cela peut indiquer que vos références importées ne correspondent pas aux précédentes références présentes dans le Tarif Centralisé. Nous vous invitons à vérifier les références internes de vos produits importés.

⚠️ Avertissement: L'ajout d'un **nouveau produit **ou d'une **nouvelle référence** ne l'importe pas automatiquement dans la base de vos distributeurs connectés.
Lorsque vous ajoutez de nouveaux articles, nous vous invitons à prévenir vos distributeurs connectés.

# Produits retirés du catalogue

**1. Classer l'article comme "obsolète"**

Vous pouvez cocher manuellement la case "Article obsolète" dans la fiche article, ou importer vos produits dans OpenImport avec la colonne "of_obsolete: TRUE" dans votre fichier tarifs.

Un article obsolète s'affiche avec un marqueur s'il est utilisé dans un devis:

![](https://support.openfire.fr/hc/article_attachments/29519198761500)

**2. Archiver les articles**

Il ne faut jamais supprimer un article. En revanche, on peut archiver un article retiré du catalogue:

- Manuellement et individuellement en cliquant sur le smart bouton Actif/Archivé dans l'article en question
- Manuellement et par groupe en sélectionnant tous vos articles à archiver puis en allant sur **Actions > Archiver**
- Via l'OpenImport, en ajoutant la colonne "Active: FALSE" dans votre fichier tarifs

⚠️ Avertissement: L'archivage d'un produit dans votre base fabricant ne l'archive pas systématiquement dans la base de vos distributeurs connectés si ceux-ci ont encore des produits en stock. La notion d'**article obsolète** est importante car elle redescend aux distributeurs connectés, même s'il leur reste du stock.

# Création, scission, fusion et archivage de marques

Ces opérations ont des **conséquences importantes** pour vos distributeurs connectés. Pour toute création de marque, scission, fusion ou archivage de marques nous vous invitons à nous contacter pour que nous puissions mettre en place la procédure qui répond à votre situation.

Mis a jour le : 11/08/2026
