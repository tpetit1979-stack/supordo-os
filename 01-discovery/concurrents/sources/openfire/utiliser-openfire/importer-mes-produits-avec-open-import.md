---
source: https://support.openfire.fr/hc/fr/articles/18848702816924-Importer-mes-produits-avec-Open-Import
categorie: Utiliser OpenFire
titre: Importer mes produits avec Open Import
date_recuperation: 2026-09-05
---

# Importer mes produits avec Open Import

Bien que la majorité des catalogues produits soit disponible via le Tarif Centralisé OpenFire, vous avez la possibilité d'importer vous-mêmes vos produits et kits. Cet article vous présente les modalités d'import et les bonnes pratiques.

Cet article contient les sections suivantes:

- [Importer un tarif](#h_01JNNEYDET6XYM2R2X6CHWFG8Y)
  - [Configurer les conditions tarifaires de sa marque](#h_01JNNFE6V2XX55Z9HK59KCF89F)
    - [Option 1 : Votre marque est en Prix Simplifiés, vous ne fournissez qu'un prix (le prix public ou le prix d'achat)](#h_01JNNF1GGT4CJ89WE7K9BZX0P5)
    - [Option 2 : Votre marque communique un prix public conseillé en euros Hors Taxes et un prix d'achat fixé](#01JNNF2MEGSWRVAKNK23XJS4SF)
  - [Créer le fichier d'import de tarifs](#h_01JNNFFK3N5ZWCZMRASYC1824J)
    - [Les données obligatoires](#h_01JNNHGX5TV5HHZ8SJM43P140T)
    - [Les données complémentaires facultatives](#h_01JNNHH57MTNA03X4M7RAW2ZPD)
    - [Les données techniques](#h_01JNNHHFM1BQ5QFZJRFRYJ88AH)
  - [Importer avec OpenImport](#h_01JNNJSRV7KFMFKSN4C25F9J80)
    - [Différents types d'avertissements à l'import](#h_01JE6AWN03VDXQ4WBHCA9RKYPG)
    - [Synthèse de l'import](#01JE6BAFT7FWWQHJGFCZBYAXZ7)
- [Mettre à jour un tarif existant](#h_01JNNEYPZWJZ8QZKWBBHXNF4EF)
- [Importer des kits](#h_01JNNEYWJ14N7051S279S9H1GD)

# Importer un tarif

Bien qu'il soit tout à fait possible de créer des produits à la main, nous vous offrons la possibilité d'importer un catalogue complet à partir d'un fichier Excel ou CSV grâce à la fonctionnalité **Open Import**. Une fois installé, vous pouvez retrouver ce module dans les paramètres de votre base.

![](https://support.openfire.fr/hc/article_attachments/24288240854300)

##

## 1️⃣ Configurer les conditions tarifaires de sa marque

Le premier élément à déterminer dans l'import d'un catalogue est le mode de gestion des prix de votre marque. Deux options s'offrent à vous:

1. **Option 1 "Prix simplifié". **Cette option s'applique si:
  - Vous avez un coefficient de remise entre votre prix d'achat et votre prix public HT (ex: 30% de remise)
  - ou bien bien vous ne fournissez qu'un prix public HT (PPHT)
  - ou bien vous n'utilisez que des prix net d'achat
2. **Option 2 "Prix d'achat et prix de vente fixés": **Votre marque communique un prix public conseillé en euros hors taxe et un prix d'achat qui dépend des produits et qui n'est pas calculable par application d'une remise sur le PPHT

### Option 1 : Votre marque est en Prix Simplifiés, vous ne fournissez qu'un prix (le prix public HT ou le prix d'achat)

Dans cette situation, voilà le paramétrage à appliquer:

- **Paramétrage de la marque **(Vente > Configuration > Marque > [Votre Marque])
  Renseignez votre remise.
- **OpenImport (voir ci-dessous):**
  - Renseignez la colonne **list_price**. Le logiciel appliquera la remise pour calculer le prix d'achat
  - Si vous êtes en prix net d'achat, renseignez les colonnes **list_price **(= votre prix d'achat) et **of_is_net_price** (= basé sur prix net)

### Option 2 : Votre marque communique un prix public conseillé en euros Hors Taxes et un prix d'achat fixé

Dans cette situation, voilà le paramétrage à appliquer:

- **Paramétrage de la marque **(Vente > Configuration > Marque > [Votre Marque])
  Le champ **remise **doit être laissé vide.
- **OpenImport (voir ci-dessous):**
  - Renseignez les colonnes **list_price **(= prix de vente)**, of_seller_pp_untaxed **(= PPHT)
  - Renseignez les colonnes **of_seller_price **(= prix d'achat distributeur) et **standard_price **(= coût)

Avertissement: Si vous renseignez une remise dans la marque, le prix d'achat importé sera effacé et recalculé selon la remise configurée.

## 2️⃣ Créer le fichier d'import de tarifs

Nous mettons à votre disposition cette [matrice d'import de tarifs](https://docs.google.com/spreadsheets/d/1SuhTPlsxkJroFyOhiTrQ-nYVSozGT_l9/export?format=xlsx) que vous pouvez importer sous Excel ou CSV.

### Les données obligatoires

Les champs **obligatoires** sont renseignés en gras:

- **brand_id:**  {Sélection} correspond à la marque du produit. Attention, ce champ est sensible à la casse. Il doit être strictement identique au nom de la marque dans votre base.
- **of_cost_date** : {Date} correspond à la date du tarif. Ce champ doit être renseigné sous la forme JJ/MM/AAAA (exemple: 01/01/2025) ou AAAA-MM-JJ (exemple: 2025-01-01)
- **categ_id** : {Sélection} correspond à la catégorie du produit (exemple POELE A BOIS). Attention, ce champ est sensible à la casse : s'il n'est pas strictement identique à un nom de catégorie déjà existante, une nouvelle catégorie sera créée.
- **detailed_type** : {Sélection} [product, consu, service] permet de préciser s'il s'agit d'un produit de Type service (service), consommable (consu) ou produit stockable (product). Dans la majorité des cas, il doit être renseigné avec la valeur product qui correspond aux produits stockables
- **default_code** : {Texte} correspond à la référence du produit. Attention à ne pas modifier les références produits entre deux imports, sinon il y aura des doublons.
- **name** : {Texte} correspond à la désignation commerciale du produit.
- **OPTION 1: Prix simplifiés**
  - **list_price : **{Chiffre à 2 décimales maximum} correspond au prix de vente du produit. Dans la majorité des cas l'import de ce prix suffira. Il sera en effet possible d'appliquer vos règles de prix et vos remises fournisseurs depuis la marque.
    **OU**
  - **of_seller_price: **{Chiffre à 2 décimales maximum} correspond au prix d'achat auprès du fabricant. Si vous êtes en prix simplifié et ne renseigné qu'un prix d'achat, il faudra ajouter la colonne **of_is_net_price: **True.
- **OPTION 2: Prix d'achat fixé**
  - **of_seller_pp_untaxed**: {Chiffre à 2 décimales maximum} correspond au prix de vente conseillé en euros hors taxe communiqué par le fabricant. Souvent égal au list_price, vous pourrez venir modifier votre prix de vente dans les paramètres de votre marque.
  - **of_seller_price: **{Chiffre à 2 décimales maximum} correspond au prix d'achat auprès du fabricant
  - **list_price**: {Chiffre à 2 décimales maximum} ce champ est obligatoire, souvent égal au prix de vente conseillé en euros hors taxe (ppht), vous pourrez venir le modifier ultérieurement dans les paramètres de votre marque s'il diffère du ppht fabricant.

Vous retrouvez ensuite ces informations dans la fiche produit:

![fiche_article_tarifs.png](https://support.openfire.fr/hc/article_attachments/18850093736604)

### Les données complémentaires facultatives

Vous pouvez communiquer des informations spécifiques sur certains produits:

- **description_sale:** {Texte} Une information supplémentaire liée au produit qui viendra s'afficher sur la ligne du devis.
- **of_manufacturer_description: **{Texte} Une information supplémentaire liée au produit communiquée par le fabricant à l'intention du revendeur uniquement.
- **description_purchase: **{Texte} Un message supplémentaire qui viendra s'ajouter sur la ligne de commande.

Vous pouvez spécifier des unités de mesure particulières à sélectionner parmi les unités disponibles.

- **uom_po_id: **{Sélection} L'unité d'achat du produit.
- **uom_id: **{Sélection} L'unité de vente du produit.

La nomenclature des unités est la suivante:

| **Catégorie d'unité** | **Quantité** | **Nom de l'unité** |
| --- | --- | --- |
| Unité | 1 (référence) | Unité(s) |
| Unité | 3 | LOT3 |
| Longueur | 1 (référence) | m |
| Longueur | 35 | 35ML |
| Poids | 1 (référence) | kg |
| Poids | 59 | 59KG |

*Si vous devez importer un produit qui se vend en palette de 50, vous saisirez "uom_id = LOT50".*

  ⚠️ Avertissement:  Les unités d'achat et de vente d'un produit doivent appartenir à la même catégorie d'unité de mesure (exemple: on ne peut pas acheter une bobine de 30 m  (catégorie Longueur) et revendre le produit à l'unité (catégorie Unité) ou au kilo (catégorie Poids) . Le produit pourra être revendu au mètre (catégorie Longueur).

Vous pouvez afficher des **avertissements **qui s'afficheront sous forme de fenêtre d'avertissement lorsque le produit est ajouté dans un devis. Pour utiliser ce champ il est nécessaire d'avoir activé dans votre configuration les options "Avertissements de vente" et "Avertissements" d'achat.

- **sale_line_warn: **{Sélection} [no-message, warning, block]. Le type de message d'alerte.
- **sale_line_warn_msg: **{Texte} Le texte à afficher.

### Les données techniques

Nous vous invitons à compléter la description de vos produits avec les champs correspondant aux **données techniques**. De cette façon, celles-ci viendront s'ajouter automatiquement sur vos devis selon les paramètres d'impression que vous aurez défini.

Voici la liste des champs disponibles:

- **of_industry_id: **{Sélection} [Cheministe, ...] Le secteur d'activité de votre produit. Les données techniques s'affichent selon le secteur d'activité sélectionné.
- **of_power_rating: **{Chiffre à 2 décimales maximum} La puissance nominale. Ne pas ajouter l'unité.
- **of_yield: **{Chiffre à 2 décimales maximum} Le rendement. Ne pas ajouter l'unité.
- **of_i_index: **{Chiffre à 2 décimales maximum} L'indice i.
- **of_eco_label: **{Texte} Le label éco-énergie du produit [A+, A, ...].
- **of_flamme_verte: **{Nombre entier} Le nombre d'étoiles flamme verte.
- **of_flamme_verte_equivalence: **{Texte} L'équivalence flamme verte.
- **of_co_emission: **{Pourcentage à 2 décimales maximum} L'émission de monoxyde de carbone (CO) en pourcentage. Ne pas ajouter le %.
- **of_co_mg_emission: **{Chiffre à 2 décimales maximum} L'émission CO en mg/Nm³ d'air. Ne pas ajouter l'unité.
- **of_goc_emission: **{Chiffre à 2 décimales maximum} L'émission de Composés Organiques Gazeux (COG) en mgC/Nm³ d'air. Ne pas ajouter l'unité.
- **of_voc_emission: **{Chiffre à 2 décimales maximum} L'émission en Composés Organiques Volatils (COV) en mg/Nm³ d'air. Ne pas ajouter l'unité.
- **of_nox_emission: **{Chiffre à 2 décimales maximum} L'émission d'Oxyde d'Azote (NOx) en mg/Nm³ d'air. Ne pas ajouter l'unité.
- **of_dust_emission: **{Chiffre à 2 décimales maximum} L'émission de poussière en mg/Nm³ d'air. Ne pas ajouter l'unité.
- **of_season_efficiency: **{Pourcentage à 2 décimales maximum} L'efficacité énergétique saisonnière. Ne pas ajouter le %.
- **of_fonds_air_bois: **{VRAI/FAUX}. Indique si le produit est éligible au fonds air bois.

## 3️⃣ Importer avec OpenImport

Les tarifs s'importent *via* le module OpenImport: Paramètres > OpenImport > Nouveau

![](https://support.openfire.fr/hc/article_attachments/24288240855708)

| **Champ** | **Valeur à compléter** |
| --- | --- |
| **Type d'import** | Produits |
| **Date** | Conserver la date du jour |
| **Fichier** | Chargez votre fichier Excel ou csv |
| **Nom** | Tarif [Marque] [Date] |
| **Préfixe de référence** |  |
| **Séparateur de champs** |  |

Cliquer sur **Simuler l'import** pour vérifier si le fichier est conforme. Si vous n'avez aucun avertissement, vous pouvez cliquer sur **Import** puis **Sauvegarder** votre import.

| 🚨**Avertissement** : L'OpenImport peut traiter au maximum 20.000 lignes par fichier. |
| --- |

### Différents types d'avertissements à l'import

- **Ajout d'une nouvelle catégorie interne**

Avertissement: "*champ Catégorie de produit (categ_id) valeur XXX n'a pas de correspondance. Produit non importé"*

Ce message signifie que la catégorie du produit importée n'est pas configurée dans votre marque. Rendez-vous dans Vente > Configuration > Marque > Correspondance des catégories de produits pour associer à la nouvelle catégorie d'origine créée une catégorie interne.

- **La marque n'est pas présente ou mal orthographiée**

Avertissement: "*champ Marque (brand_id) valeur XXX n'a pas de correspondance. Produit non importé"*
*"champ Marque (brand_id) requis mais non présent dans le fichier d'import. Produit non importé".*

La marque présente dans le fichier d'import n'est pas présente dans vos marques. Rendez-vous dans Vente > Configuration > Marque pour vérifier la présence et l'orthographe de votre marque.

- **Une référence produit est en doublon**

Avertissement: *"xxx réf. xxx existe en N exemplaires dans le fichier d'import. Seule la première ligne est importée"*

La référence interne d'un produit doit être unique. Si vous rencontrez ce message, nous vous invitons à supprimer le doublon dans votre fichier d'import pour vous assurer que la ligne importée contienne les informations correctes.

- **Vous ajoutez de nouvelles catégories de produits**

Avertissement: *"Marque XXX : Ajout de la configuration pour la catégorie "XXX"*

Votre fichier d'import contient des catégories de produit qui n'existaient pas auparavant dans votre base. Ces catégories sont automatiquement ajoutées dans la configuration de votre marque dans la colonne "catégorie d'origine" pour que vous puissiez y associer une catégorie interne et d'éventuelles conditions tarifaires spécifiques.

### Synthèse de l'import

Ce tableau de synthèse visible dans Open Import vous permet de vérifier la cohérence entre le nombre de produits créés et le nombre de produits mis à jour et votre fichier d'import.

![](https://support.openfire.fr/hc/article_attachments/18854230974364)

Si vous constatez un nombre anormalement élevé de produits ajoutés alors que vous avez peu de nouvelles références dans votre catalogue, cela peut indiquer que vos références importées ne correspondent pas aux précédentes références présentes dans vos produits. Nous vous invitons à vérifier les références internes de vos produits importés.

# Mettre à jour un tarif existant

Pour mettre à jour un tarif existant, il vous suffit d'importer les colonnes suivantes en reprenant les **default_code** des produits que vous souhaitez modifier et les informations suivantes obligatoires.

- **of_cost_date**
- **brand_id**
- **type**
- **default_code**
- **name**
- **categ_id**
- **OPTION 1: **Vous êtes en prix simplifié sur la marque
  - **list_price**
    ou bien
  - **of_seller_price **et **of_is_net_price**
- **OPTION 2:** Vous êtes en prix d'achat fixé sur la marque
  - **list_price**
  - **of_seller_pp_untaxed**
  - **of_seller_price**

Vous pouvez également ajouter toutes les autres colonnes décrites précédemment si vous souhaitez les mettre à jour.

⚠️ Avertissement: Même si votre mise à jour ne concerne pas le prix, vous devez remettre vos colonnes liées au tarif dans l'import, sinon elles seront effacées et recalculées.

# Importer des kits

Il est possible d'importer des kits directement dans OpenFire.

Nous mettons à votre disposition la [matrice d'import des kits](https://docs.google.com/spreadsheets/d/1Nrz1osTChg_eW4hUHsdGHqHwdXOLabSL/export?format=xlsx) à téléverser dans OpenImport.

Le principe est le suivant :

1. Import des composants pour qu'ils soient présents dans la base.
  La première étape est de s'assurer que les produits qui vont composer le kit sont bien présents sur la base. Si ce n'est pas le cas, il faut les importer à partir du tarif centralisé, ou bien en suivant la première partie de cette documentation.
2. Import des produits de type "Kit".

  Les valeurs à définir dans le fichier Excel/CSV sont les suivantes:

  - **of_cost_date**
  - **brand_id: **Votre marque. Le kit vous appartient, il n'est pas proposé par le fabricant en tant que tel.
  - **default_code**
  - **name**
  - **categ_id**
  - **detailed_type:** service. Le kit n'est pas stocké en tant que tel, ce sont les composants qui sont des produits stockés.
  - **pack_component_price:** {Sélection} [totalized, ignored]. Mettre à 'totalized' pour calculer automatiquement le prix du kit selon le prix des composants
  - **pack_ok:** {VRAI/FAUX} Mettre à "VRAI".

  Ce fichier est à importer en type d'import "Produits" sur Open Import.
3. Import d'un fichier permettant de faire le lien entre les produits de type Kit et les composants du kit.

  Préparez le fichier d'import permettant de relier les produits de type kit et leurs composants avec les valeurs suivantes:

- **product_id/default_code:** la référence interne du produit à intégrer dans ce kit en tant que composant **avec son préfixe de marque**, que vous avez précédemment importé dans l'étape 1 (exemple: MON_928520)
- **parent_product_id/default_code**: la référence interne du produit Kit **avec son préfixe de marque** que vous avez précédemment importé dans l'étape 2. (exemple: SEG_KIT001)
- **quantity**: La quantité de ce composant dans le kit

| **parent_product_id/default_code** | **product_id/default_code** | **quantity** |
| --- | --- | --- |
| MON_KIT001 | SEG_928520 | 1 |
| MON_KIT001 | DIX_241145.24 | 2 |

*Dans cet exemple, le kit de Mon Entreprise MON_KIT001 contient 1 composant SEG_928520 et 2 composants DIX_241145.24*

Ce fichier est à importer en type d'import "Composant de kits" sur Open Import.

Mis a jour le : 21/07/2026
