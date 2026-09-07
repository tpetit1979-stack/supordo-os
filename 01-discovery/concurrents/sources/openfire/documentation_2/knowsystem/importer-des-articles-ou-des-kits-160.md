---
url: https://documentation.openfire.fr/knowsystem/importer-des-articles-ou-des-kits-160
url_finale: https://documentation.openfire.fr/knowsystem/importer-des-articles-ou-des-kits-160
date_collecte: 2026-09-06
destination: documentation_2
---

Openfire permet la création et la mise à jour d'articles, ou même de kits, via l'import d'un fichier Excel sur votre base. Il est possible d'y associer l'ensemble des données techniques afin de permettre l'accès automatique à ces informations depuis votre base.

            
        
    

## Importer et mettre à jour un tarif

1. Champs obligatoires:

Une fois en possession du fichier de tarif du fournisseur, il faut préparer le contenu du fichier. En effet, un certain nombre de champs sont obligatoires à l'importation, dont voici les significations : 

  Attention à ne pas mettre des formules dans les colonnes mais bien des valeurs. Si besoin, il suffit bien souvent de faire un copier/collage valeur du tableau. 

- brand_id : correspond à la marque de l'article. Attention, ce champ est sensible à la casse. Il doit être strictement identique au nom de la marque dans votre base.

- date_tarif : correspond à la date du tarif. Ce champ doit être renseigné de la forme JJ/MM/AAAA (exemple: 01/05/2022).

- categ_id : correspond à la catégorie de l'article (exemple POELE A BOIS). Attention, ce champ est sensible à la casse : s'il n'est pas strictement identique à un nom de catégorie déjà existante, une nouvelle catégorie sera créée.

- type : permet de préciser s'il s'agit d'un article de Type Service, consommable ou produit stockable. Dans la majorité des cas, il doit être renseigné avec la valeur product qui correspond aux produits stockables

- default_code : correspond à la référence de l'article. Attention à ne pas modifier les références articles entre deux imports, sinon il y aura des doublons.

- name : correspond au nom commercial de l'article.

- list_price : correspond au prix de vente de l'article (à arrondir 2 chiffres après la virgule). Dans la majorité des cas l'import de ce prix suffira. Il sera en effet possible d'appliquer vos règles de prix et vos remises fournisseurs depuis la marque. Lors de l'import d'articles, il y'a en effet deux possibilités :

**Méthode 1:**  Vous importez simplement la variable list_price (à arrondir 2 chiffres après la virgule), dans ce cas, la valeur de list_price alimentera le champ Prix Public HT de la fiche article.

Les autres champs de la fiche article seront alors calculés en fonction des règles configurées sur la marque.

Par exemple, si vous renseignez les valeurs suivantes dans votre marque :

  - Remise = 50
  - Prix de vente HT = ppht*1.2
  - Prix de revient = pa+100

__Exemple:__ vous importez le fichier ci-dessous :

Vous obtenez :

**Méthode 2 :** Vous déclarez toutes les valeurs de prix dans le fichiers d'import. Dans ce cas, les valeurs à utiliser sont les suivantes:

  - of_seller_pp_ht: Prix public hors taxe HT Fournisseur
  - of_seller_price: Prix d’achat Fournisseur
  - standard_price: Coût (=Prix de revient) Distributeur
  - list_price: Prix de vente Distributeur

Il faut alors configurer la marque spécifiquement en positionnant dans les champs de calcul les valeurs suivantes :

  - Remise = VIDE
  - Prix de vente HT = pv
  - Prix de revient = pr

	__Exemple :__ vous importez le fichier ci-dessous:

Les différents prix de votre article sont alors renseignés comme tels :

  Plus d'information sur [Définir ses conditions tarifaires](https://documentation.openfire.fr/knowsystem/definir-ses-conditions-tarifaires-169) 

2. Champs optionnels :

Les données techniques des appareils peuvent également être importées via le fichier Excel. Ces champs sont optionnels mais peuvent être repris sur les devis :

Voici la liste des champs disponibles pour l'onglet technique:

- Écotaxe : ecotax_amount

- Éco-label : of_eco_label

- Équivalence flamme verte : of_equivalence_flamme_verte

- Éligible Fonds Air Bois : of_fonds_air_bois

- Émission de CO en %: of_emission_co

- Émission de CO en mg: of_emission_co_mg

- Émission de poussière : of_emission_poussiere

- Émission de NOx : of_emission_nox

- Émission de COV : of_cov_emission

- Émission de COG : of_cog_emission

- Flamme verte : of_flamme_verte

- Norme : norme_id

- Indice I : of_indice_i

- Puissance nominale : of_puissance_nom

- Rendement : of_rendement

- % Efficacité énergétique saisonnière : of_efficacite_saison

L'import de ces données techniques peut se faire pour certaines lignes de votre fichier Excel et pas pour d'autres, ce qui donne ce genre de rendu :

- Description : description

- Description du fabricant : description_fabricant

**Attention:**Ne pas importer uniquement les données techniques: Il est important de toujours importer le prix de vente, même lorsque vous souhaitez seulement mettre à jour les données techniques, sans quoi le prix de vente repassera à 0.

3. Import du fichier

Une fois fait, vous pourrez alors l’importer sur votre base OpenFire.

Pour cela rendez-vous dans le menu **Configuration > OpenImport** 

L’avantage de passer par ce module est que le logiciel contrôle plusieurs éléments tels que les articles en doublons et il indique la raison du problème d’import.

En cliquant sur le bouton Créer, et non pas importer, vous allez pouvoir préparer votre import en remplissant les champs comme ci-dessous:

● Type d’import : sélectionner “Articles”

● Nom : préciser le nom de l’import effectué (exemple: Tarif Poêle du 01/01/2023).

● Date : date du jour par défaut

Ensuite, chargez votre fichier, puis cliquez sur SIMULER IMPORT

 Il est important de toujours simuler l'import avant d'importer définitivement le fichier. Cela va en effet permettre de vérifier la présence des champs obligatoires, le formatage des données et même la présence d'éventuels doublons.

Si aucune erreur ne remonte, il est alors possible d'importer le fichier en cliquant sur le bouton Importer.

4. Archiver les références inutilisées

Vous avez la possibilité d'archiver dans votre base client les références articles qui ne sont pas présentes dans votre fichier d'import et/ou qui ne sont plus commercialisées.

Dans **Ventes > Configuration > Marques**, vous accédez aux articles via le tableau de bord en haut à droite.

Ensuite, vous pouvez grouper les résultats par date de tarif:

Vous avez alors la possibilité de sélectionner les articles n'ayant pas la date de mise à jour la plus récente afin de les archiver. Les références archivées ne pourront alors plus être utilisées dans un Devis.

*Ces articles ne seront pas supprimés et pourront être désarchivés si besoin.*

## Import et mise à jour des kits

Il est possible d'importer des kits directement dans OpenFire. Le principe est le suivant :

**Étape 1 :** import des articles pour qu'ils soient présents dans la base.

La première étape est donc de s'assurer que les articles qui vont composer le kit sont bien présents sur la base. Si ce n'est pas le cas, il va falloir les importer en suivant la première partie de cette fiche.

**Étape 2 :** import des kits afin de créer les spécificités du kit.

Le fichier ressemble au fichier d'import classique à la différence que :

- la colonne type sera valorisée en service,
- la colonne of_is_kit = true permet a l'outil de savoir qu'il faut créer un kit,
- la colonne of_pricing permet de définir la méthode de calcul du prix du kit. Il vaut mieux laisser la valeur computed . Ainsi le prix du kit sera automatiquement calculé à partir des composants du kits,
- la colonne list_price peut rester à 1 car le prix sera actualisé par la suite en fonction des composants du kit.

**Étape 3:** import d'un fichier permettant de faire le lien entre les articles et le kit afin que celui-ci ai des composants.

Ce fichier sera a importer en type d'OpenImport "Composants de Kits":

- la colonne kit_id/default_code doit contenir le nom du kit,
- la colonne product_id/default_code doit contenir la référence de l'article,
- la colonne product_qty contiendra le nombre d'article,
- la colonne product_uom_id contient l'unité de mesure de l'article. Vous pouvez laisser cette valeur en Unité.