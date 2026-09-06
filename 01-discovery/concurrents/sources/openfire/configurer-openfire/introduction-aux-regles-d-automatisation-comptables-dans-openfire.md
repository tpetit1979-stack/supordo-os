---
source: https://support.openfire.fr/hc/fr/articles/21515062307228-Introduction-aux-r%C3%A8gles-d-automatisation-comptables-dans-OpenFire
categorie: Configurer OpenFire
titre: Introduction aux règles d’automatisation comptables dans OpenFire
date_recuperation: 2026-09-05
---

# Introduction aux règles d’automatisation comptables dans OpenFire

Cet article présente les **règles d'automatisation comptable** dans OpenFire. Vous apprendrez comment sont articulés et utilisés les principaux éléments identifiés (**Article**, **Catégorie**, **Taxe** et **Position fiscale)** afin de simplifier la création de vos factures clients et fournisseurs.

**Cet article contient les sections suivantes :**

- Les principaux éléments utilisés dans l'automatisation
  - Les produits
  - Les catégories de produits
  - Les partenaires
  - Les taxes
  - Les positions fiscales
- Les règles d'automatisation
  - Les règles générales
  - Les produits à TVA unique
- Bonnes pratiques
- Pour aller plus loin

# Les principaux éléments utilisés dans l'automatisation

Les règles d'imputation comptable automatique des pièces (factures clients et fournisseurs) se basent sur **cinq éléments **pour déterminer les bons comptes et taxes à utiliser.

## Les produits

Les produits peuvent être configurés avec des comptes (produits et charges) et des taxes (achat et vente) par défaut ou spécifiques selon le cas de figure.

On distingue deux cas de figures :

### 1/ Les produits sans régime spécifique

Ces produits n'ont **pas de particularité comptable ou fiscale **et suivent les règles applicables à la transaction (selon la position fiscale de la transaction notamment).

Dans ce cas, le produit est configurée avec une Taxe de base pour la vente et pour l'achat. Cette taxe sera convertie par la bonne taxe au moment de la transaction.

![](https://support.openfire.fr/hc/article_attachments/21524871349660)

![](https://support.openfire.fr/hc/article_attachments/21524875257756)

| 💡**Note **: dans ce cas, il n'est pas nécessaire de définir de compte de produit et de charge par défaut pour le produit. Ces valeurs seront pilotées par les catégories de produit. |
| --- |

### 2/ Les produits avec un régime spécifique

Ces **produits ont des règles spécifiques** et sont configurés afin de prendre le pas sur les autres paramètres (exemple : les sacs de granulés sont toujours vendus en TVA 10%).

Dans ce cas, le produit est directement configuré avec les comptes et les taxes à appliquer.

| 🧑‍🏫Exemple : les sacs de granulés sont toujours vendus à la TVA 10%. On retrouve donc toujours au niveau de ces produits les comptes de revenus et de charges systématiquement associés à ce produit :  ![](https://support.openfire.fr/hc/article_attachments/21524871352476)Ainsi que la taxe associé à ce produit :  ![](https://support.openfire.fr/hc/article_attachments/21524871352988) |
| --- |

## Les catégories de produits

Il est possible de définir au niveau des catégories de produit les **comptes de revenus et de charges par défaut** à utiliser pour l'ensemble des produits de la catégorie. Il est effectivement plus simple de gérer ce point de paramétrage au niveau de quelques dizaines de catégories plutôt qu'au niveau de millier de produits.

Ainsi, sauf configuration contraire dans le produit, ce sont les comptes de la catégorie qui seront utilisés pour la transaction.

Il est d'usage de définir dans les catégories de produit le **compte comptable de produit ou de charge à utiliser pour les transactions hors taxes. **

C'est au niveau de chacune des taxes que la ventilation se fera du compte par défaut vers le compte associé à la TVA en question.

| 🧑‍🏫Exemple : la catégorie de produit Foyer Bois sera configuré ainsi, avec les comptes de produit et de charge par défaut suivant. ![](https://support.openfire.fr/hc/article_attachments/21523785098780)Dans la taxe **TVA collectée 5,5%, **ce compte est remplacé par le compte correspondant adapté à la TVA de la transaction :  ![](https://support.openfire.fr/hc/article_attachments/21523771918364) |
| --- |

## Les partenaires

Un régime de TVA ou d'imputation spécifique peut être imposé pour un client ou pour une typologie de client particulier.

Dans ce cas, nous définissons au niveau du partenaire (client ou fournisseur), la position fiscale par défaut.

| 🧑‍🏫Exemple : pour des ventes en B2B, la TVA applicable en France est de 20%. Nous pouvons ainsi configurer la position fiscale de tous nos clients professionnels ainsi :  ![](https://support.openfire.fr/hc/article_attachments/21524875261340) |
| --- |

La position fiscale de référence associée à la transaction. Cette position fiscale sera reprise par défaut dans toutes les transactions du partenaire (et pourrait éventuellement être modifiée manuellement dans la commande ou la facture).

## Les taxes

Les **taxes** vous permettent de configurer les règles d'imputation comptable pour la TVA. Vous pouvez définir :

- L'imputation des comptes comptables de taxes par taux de TVA.
- L'imputation des comptes comptables de produits et de charges par taux de TVA.

![](https://support.openfire.fr/hc/article_attachments/21515062306844)

| 📓Pour aller plus loin → Configurer vos taxes |
| --- |

## Les positions fiscales

Les **positions fiscales** vous permettent de créer des règles pour adapter automatiquement les taxes et les comptes utilisés pour une transaction. L'adaptation se fait selon différents critères, comme par exemple :

**La localisation géographique : **un professionnel de l'installation ou de la maintenance qui exerce sur une zone frontalière appliquera des régimes fiscaux différents de part et d'autre de la frontière.

**La règlementation applicable : **la vente d'un même produit ou service peut se voir appliquer un régime différent selon le contexte.

| 🧑‍🏫Exemple : la TVA applicable à une transaction de fourniture et d'installation d'un appareil de chauffage au bois peut varier selon l'âge de la maison :   Maison de moins de deux ans => TVA 20% Maison de plus de deux ans => TVA 5,5% |
| --- |

**Le type de client : **La TVA peut également varier selon le type de client (professionnel / particulier)

| 🧑‍🏫Exemple : la TVA applicable à une transaction de fourniture et d'installation d'un appareil de chauffage au bois peut varier selon qu'il s'agisse d'une client personne morale ou personne physique :   Client personne morale => TVA 20% Client personne physique => TVA 5,5% |
| --- |

**Le contexte de la vente :** la TVA et les comptes d'imputation peuvent également varier selon qu'il s'agisse d'une vente à l'emporter ou d'une vente de type "fourniture et pose".

| 🧑‍🏫Exemple : Vente d'un poêle à l'emporter VS avec prestation d'installation :   Vente l'emporter :   TVA 20% Compte de produit 707120 Vente de marchandise à l'emporter TVA 20%   Vente fourniture et pose :  TVA 5,5%  Compte de produit 707055 - Vente de marchandise TVA 5,5% |
| --- |

| 📓Pour aller plus loin → Configurer vos positions fiscales |
| --- |

# Règles d'automatisation des données comptables

---

## Règles générales

L'automatisation fonctionne selon une hiérarchie :

1. Les **produits** et les **catégories de produits** définissent des taxes et des comptes par défaut.
2. Les **taxes** définissent le compte de TVA ainsi que les comptes de produits et de charges adaptés.
3. La **position fiscale** définit la taxe à appliquer et les comptes à utiliser selon le contexte de la transaction.

Voici le schéma de synthèse :

![](https://support.openfire.fr/hc/article_attachments/21525055034524)

## Les produits à TVA unique

Si un produit ou une prestation est toujours vendu avec la même TVA, vous pouvez forcer la taxe et les comptes de produits ou de charges en les définissant directement au niveau du **produit**.

| 💡**Note **: Dans ce cas, les règles de la position fiscale ne s'appliqueront pas pour ce produit, sauf configuration spécifique de ces dernières |
| --- |

# Bonnes pratiques

---

- **Commencer par le général** : Configurez d'abord les règles générales (catégories, taxes) avant de créer des règles spécifiques (produits, positions fiscales).
- **Vérifier vos configurations** : Créez une facture de test après chaque modification pour vous assurer que les bonnes règles s'appliquent.
- **Utiliser les positions fiscales avec soin** : Les positions fiscales sont très puissantes. Utilisez-les pour des contextes transactionnels clairs et spécifiques pour éviter les erreurs.

# Pour aller plus loin

---

| 📓Pour aller plus loin → Configurer vos taxes 📓Pour aller plus loin → Configurer vos positions fiscales 📓Pour aller plus loin → Configurer vos prix en HT (B2B) ou en TTC (B2C) 📓Pour aller plus loin → Configurez vos acomptes |
| --- |

Mis a jour le : 04/08/2025
