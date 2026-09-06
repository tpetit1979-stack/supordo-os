---
source: https://support.openfire.fr/hc/fr/articles/24375599455004-Configuration-des-articles-pour-les-achats-et-stocks
categorie: Configurer OpenFire
titre: Configuration des articles pour les achats et stocks
date_recuperation: 2026-09-05
---

# Configuration des articles pour les achats et stocks

La **fiche produit** est le point de départ d'une gestion des achats et des stocks réussie. Cet article vous guide dans la configuration de vos produits pour garantir un flux d'approvisionnement adapté à vos process et la bonne génération de vos commandes fournisseurs.

Cet article contient les sections suivantes :

- [Introduction](#h_01KD4BH1ER1F8K1YJ2EMED7ZFK)
- [Paramètres produits](#h_01KD5ZXZPM5ZZHRYMQB4KYMRZQ)
  - [Produit pouvant être acheté](#h_01KD4BH1ER1F8K1YJ2EMED7ZFK)
  - [Type de produit](#h_01KD4BH1ER1F8K1YJ2EMED7ZFK)
  - [Marque & fournisseurs](#h_01KD5YW8A97EBCG4WSJ89PPNXY)
  - [Prix d'achat](#h_01KD56ANK1V541E8AJM85DN6KJ)
  - [Coût (d'inventaire) et Coût théorique](#h_01KD5ZC8MABV8CT34BCDR7BV6N)
    - [Le coût d'inventaire](#h_01KD5ZC8MAZHPDYM3DDB1076PT)
    - [Le coût théorique](#h_01KD5ZC8MAZA0PRM2CP2GX2WJ4)
  - [Taxes fournisseurs et politique de contrôle des factures fournisseurs](#h_01KD4BRNGKHAEK1D092NK9DVHS)
  - [Description des achats](#h_01KD4BXENA360EAR18Q1R7S89B)
  - [Configuration des routes ](#h_01KD5ZGZ4GG287R50Z5FNJ5Y63)
- [Bonnes pratiques](#h_01KD5YZKYQ21FPCRQMHTJ3GBDM)

---

## Introduction

Chemin d'accès : `Inventaire > Produit`

Vous retrouvez ci-dessous les différents paramètres de vos fiches produits utiles à la bonne mise en œuvre de vos achats et stocks.

## Paramètres produits

### Produit pouvant être acheté

Suivre le chemin d'accès suivant : **Produit** > Onglet **Informations Générales **> section **Divers**** **

Cocher impérativement la case **Peut être acheté** dans la section **Divers** pour permettre l'approvisionnement.

![](https://support.openfire.fr/hc/article_attachments/24416682176412)

### Type de produit

Suivre le chemin d'accès suivant : **Produit** > Onglet **Informations Générales**

Le comportement de l'article dans votre inventaire dépend de son type.

Choisir le **Type de produit** :

Dans OpenFire, chaque fiche article doit être qualifiée pour définir comment le logiciel doit gérer cet élément, notamment en termes de stocks et de facturation.

Le Produit stockable

C'est un article physique pour lequel vous souhaitez suivre précisément les quantités disponibles en temps réel.

- **Usage **: La gestion de stock est activée. Chaque entrée (achat) ou sortie (vente/pose) impacte votre inventaire.
- **Traçabilité **: Permet un suivi rigoureux des mouvements et de la valeur de votre stock.

| **🧑‍🏫Exemple** : Un poêle à bois, une unité de climatisation, ou des pièces détachées onéreuses. |
| --- |

Le Consommable

Il s'agit d'un produit physique que vous utilisez pour vos chantiers ou interventions, mais dont vous ne souhaitez pas suivre le stock de manière unitaire ou rigoureuse

- **Usage **: Le logiciel considère que vous en avez toujours assez en stock. Il n'y a pas de blocage si le stock théorique est à zéro.
- **Logistique **: Simplifie la saisie pour le petit matériel souvent utilisé en volume.

| **🧑‍🏫Exemple** : sac de plâtre, vis, chevilles, ruban adhésif technique, ou produits de nettoyage. |
| --- |

Le Service

Le service correspond à une prestation immatérielle, une compétence ou du temps passé par vos techniciens.

- **Usage **: Par nature, il n'y a pas de gestion de stock physique.
- **Planification **: Ce type d'article est souvent lié à la gestion des interventions et à la main-d'œuvre

| **🧑‍🏫Exemple** : Forfait de ramonage, mise en service d'une pompe à chaleur, ou frais de déplacement. |
| --- |

Le cas des kits :

Le kit est un ensemble de produit ou de service. Il n'a pas d'existence en tant que tel. A ce titre, les kits sont créés comme des ***service. **S*es composants en revanche peuvent être de tous les types.

| **🧑‍🏫Exemple** : Kits de raccordement, Kit de création de conduit. |
| --- |

### Marque & fournisseurs

Depuis l'onglet **Informations générales vous pouvez **valoriser la marque de l’article.

Depuis l'onglet **Achat **:

- Le fournisseur associé à la marque est identifié comme premier fournisseur dans la liste.
- Le prix d’achat de référence défini au niveau de l’article correspond au prix d’achat chez ce fournisseur.
- Vous pouvez ajouter d'autres **Fournisseurs** qui proposent ce produit ainsi que leur **Prix** respectif.

![](https://support.openfire.fr/hc/article_attachments/24416677169308)

### Prix d'achat

Suivre le chemin d'accès suivant : **Produit** > Onglet **Informations Générales **> section **Informations Fournisseur**.** **

Correspond au prix d’achat du fournisseur principal du produit (= fournisseur associé à la marque du produit).

Ce prix sera repris par défaut pour les achats associés à ce produit.

![](https://support.openfire.fr/hc/article_attachments/24416686341532)

### Coût (d'inventaire) et Coût théorique

Dans l'onglet **Informations générales** :

![](https://support.openfire.fr/hc/article_attachments/24416814071964)

| 💡**Note **: Le coût théorique n'est visible que lorsque la méthode de coût de la catégorie de produit associée est FIFO ou Coût Moyen ; dans le contexte d'une méthode de coût standard, le coût et le coût théorique ont vocation à être identiques. |
| --- |

#### Le Coût (d'inventaire)

Le champ **Coût **(parfois appelé *coût d'inventaire* ou *coût réel*) représente la réalité comptable de vos stocks à un instant T.

Voici comment se définit cette notion dans OpenFire :

- **Valeur d'inventaire** : Ce coût est utilisé pour valoriser votre stock et calculer la valeur financière de votre entreprise dans vos rapports de bilan.
- **Reflet des flux réels** : Contrairement au coût théorique qui est une base de négociation, le **Coût** est le résultat direct de vos entrées et sorties de marchandises.
- **Dépendance à la méthode de calcul** : Sa valeur est calculée par OpenFire en fonction de la méthode de valorisation sélectionnée dans la catégorie de l'article :

  - **Coût Standard** : Le coût est fixé manuellement et ne bouge pas, même si le prix d'achat varie.
  - **Coût Moyen (AVCO)** : Le coût est recalculé à chaque réception pour lisser les prix d'achat.
  - **FIFO** : Le coût affiché correspond à la valeur du prochain lot qui sortira de l'entrepôt.

| 🚨**Avertissement** : Toute modification manuelle du champ **Coût** sur une fiche produit déclenche automatiquement une écriture comptable d'ajustement. Cela signifie que vous modifiez artificiellement la valeur de votre stock, ce qui impacte directement vos rapports financiers. |
| --- |

Les méthodes de coût sont définies ci-après.

#### Le coût théorique

Le **Coût théorique** est un indicateur commercial calculé automatiquement, soit via l'import de vos tarifs fournisseurs, soit par l'application de règles spécifiques configurées directement sur la **Marque** du produit. Contrairement au coût d'inventaire, il reflète les conditions commerciales que vous avez officiellement validées avec vos partenaires.

**Pourquoi utiliser le coût théorique ?**

OpenFire vous permet de choisir ce champ en substitution du **Coût** standard pour le calcul de vos marges dans les devis clients. Cette option est avantageuse car elle vous permet de :

- **Stabiliser vos calculs de rentabilité** : votre marge est calculée sur la base de vos tarifs négociés actuels.
- **Éviter les fluctuations** : vous ne dépendez pas des variations ponctuelles de vos prix d'achat réels ou de la méthode de valorisation des stocks (AVCO, FIFO) qui peuvent impacter la valeur comptable du produit.
- L'utilisation du coût théorique garantit que **vos commerciaux travaillent toujours sur la base d'une marge théorique actualisée**, indépendamment des mouvements de stock en cours.

Le choix de la valeur de coût de référence pour le calcul des marges dans le devis est défini au niveau des catégories de produit, et est défini ci-après.

### Taxes fournisseurs et politique de contrôle des factures fournisseurs

Suivre le chemin d'accès suivant : `Produit > Onglet Achats > section Factures Fournisseurs`

1. Renseigner les **Taxes fournisseur** par défaut pour les commandes d'achat. La valeur par défaut est normalement **TVA de base (achat). **Cette configuration de base permet d'appliquer la position fiscale du fournisseur. Si une taxe spécifique est systématiquement utilisée pour le produit, elle peut être ajoutée ici.
2. Sélectionner votre **Politique de contrôle** pour la facturation :
  - **Sur base des quantités commandées** : la facture fournisseur peut être créée dès que le bon de commande est confirmé.
  - **Sur base des quantités reçues** : la facture ne peut être générée qu'après la réception physique (partielle ou totale) des produits.

![](https://support.openfire.fr/hc/article_attachments/24416677169692)

### Description des achats

Suivre le chemin d'accès suivant : `Produit > Onglet Achats > section Description des achats`.

Vous pouvez déterminer une description spécifique pour ce produit qui sera utilisée par défaut comme libellé de ce produit dans les commandes fournisseur :

![](https://support.openfire.fr/hc/article_attachments/24416785597852)

### Configuration des routes

Suivre le chemin d'accès suivant : `Produit > Onglet Inventaire > section Opérations`.

![](https://support.openfire.fr/hc/article_attachments/24416839327132)

Les **Routes** définissent le chemin logistique que suit un produit pour son approvisionnement. Elles permettent de déterminer comment et quand un article doit être acheté ou déplacé.

Les différentes autres routes disponibles :

- **Acheter **: il s'agit de la route standard de OpenFire. Elle est utilisée pour les produits approvisionnés à la contremarque, pour l'approvisionnement standard ou selon des règles de stocks prédéfinies.
- **Réapprovisionnement sur commande** : cette route déclenche un achat dès qu'une commande client est confirmée.
- **Approvisionnement en drop-shipping** : cette option permet de faire livrer le produit directement par le fournisseur au client final, sans passer par votre stock.

D'autres routes peuvent être configurées à la demande.

## Bonnes pratiques

- **Prix d'achat **: Pensez à bien vérifier les prix d'achat de vos bons de commande fournisseurs avant de les valider pour éviter de propager de mauvaises données de valorisation.
- **Vérifiez vos unités : **Assurez-vous que l'unité de mesure (unité, mètre, carton) est la même sur votre fiche produit et sur votre commande fournisseur pour éviter des erreurs de calcul massives.
- **Contrôle régulier** : Consultez votre rapport d'évaluation des stocks pour détecter d'éventuelles erreurs de saisie sur les prix.

##

Mis a jour le : 12/01/2026
