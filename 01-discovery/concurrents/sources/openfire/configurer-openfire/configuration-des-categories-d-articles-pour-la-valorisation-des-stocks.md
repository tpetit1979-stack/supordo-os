---
source: https://support.openfire.fr/hc/fr/articles/24421364127772-Configuration-des-cat%C3%A9gories-d-articles-pour-la-valorisation-des-stocks
categorie: Configurer OpenFire
titre: Configuration des catégories d'articles pour la valorisation des stocks
date_recuperation: 2026-09-05
---

# Configuration des catégories d'articles pour la valorisation des stocks

Simplifiez le suivi de votre inventaire en configurant correctement vos catégories de produits. Cet article vous accompagne dans le choix de la **méthode d'inventaire** (manuelle ou automatisée) et de votre **méthode de valorisation** (Standard, FIFO ou AVCO). Ce sont deux paramètres essentiels pour automatiser la valorisation de vos articles en stock.

Cet article contient les sections suivantes :

[Introduction](#h_01KD4GBXP0D74BKSXW9MRQJM1R)

[Section 1 : Méthode de valorisation manuelle ou automatisée des stocks](#h_01KD4GRK05C7ZEHAYX50JZ9RRJ)

- [Valorisation manuelle](#h_01KD57WSJDGJ5BR9MHPTJMXVXG)
- [Valorisation automatisée](#h_01KD5AAHFQ2F57T6TX5EG6JQ1N)

[Section 2 : Méthode de coût](#h_01KD4GRJ78F2XE0W0Y48CG200D)

- [La méthode du coût standard](#h_01KD4EG3FD2RQQ20H0HFRZEEVQ)
- [La méthode du coût moyen (AVCO) ](#h_01KD4FFVGYTG6A96YQRVJXJEK0)
- [La méthode du FIFO (First in First Out)](#h_01KD4B48MYKX5ZQ58RM8V6ZN0Q)
- [Règles spéciales de mise à jour du coût de vos articles](#h_01KD5X81F2WB6GJ4JXYZDGRC2P)

[Bonne pratiques](#h_01KD4FYKWX686NPF5AP1HDVKQ8)

---

## Introduction

Chemin d'accès : `Inventaire > Configuration > Produits > Catégories de produits`.

Deux réglages spécifiques doivent être configurés au niveau de chaque **Catégorie de produit** pour assurer la façon dont les stocks sont valorisés :

- Le champ **Valorisation des stocks** : définit si le calcul est périodique ou en temps réel (défini par défaut sur **Manuelle**).
- Le champ **Méthode de coût** : définit la règle de calcul du prix (défini par défaut sur **Prix standard**).

![](https://support.openfire.fr/hc/article_attachments/24422047276188)

## Méthode de valorisation manuelle ou automatisée des stocks

Ce paramètre vous permet de définir le rythme suivant lequel vous allez valoriser votre stock. Deux valeurs sont disponibles : **Manuelle **ou **Automatisée**.

![](https://support.openfire.fr/hc/article_attachments/24431500399004)

### Valorisation manuelle

Il s'agit de la **valeur par défaut **dans OpenFire**. **Cette **méthode **est aussi **la plus simple à mettre en œuvre**

Dans ce mode de fonctionnement :

- La **valorisation **est réalisée manuellement et **périodiquement (**mensuellement ou lors des opérations de clôture par exemple) et non pas recalculée automatiquement en temps réel par le logiciel lors de chaque mouvement.
- **Aucune écriture comptable** n'est **générée automatiquement **lors des mouvements de stock.

Cette méthode repose sur une collaboration entre vos équipes :

- Les collaborateurs en entrepôt réalisent un **inventaire physique** régulier pour compter les produits réellement présents.
- L'équipe comptable **valorise **ensuite le stock et **enregistre les pièces comptables** manuellement en s'appuyant sur ces relevés de terrain.

### Valorisation automatisée

Il s'agit d'une méthode de gestion plus avancée.

Dans ce mode de fonctionnement :

- **Chaque entrée ou sortie de stock** **génère une écriture comptable** automatiquement et directement dans un journal de stock dédié.
- La **valorisation de l'inventaire peut ainsi se faire en instantanée** directement depuis la comptabilité.

Si vous utilisez la valorisation automatisée, vous devez renseigner les champs suivants dans la catégorie:

1. **Compte de valorisation de stock** : contient la valeur actuelle de vos produits en stock.
2. **Compte d'entrée en stock** : compte de contrepartie pour les réceptions de marchandises.
3. **Compte de sortie de stock** : compte de contrepartie pour les livraisons clients.

| 💡**Note **: la valorisation automatisée des stocks est une méthode exigeante de suivi des stocks qui nécessite un contrôle et une attention particulière lors de la réalisation des opérations de stocks. Elle n'est pas recommandée pour les petites équipes ne disposant pas d'opérateur dédié à la saisie de ces opérations. |
| --- |

## Méthode de coût

Dans OpenFire, la manière dont vous valorisez vos stocks influence directement votre rentabilité et votre comptabilité. Cette section détaille les trois méthodes de calcul des coûts disponibles pour vos catégories d'articles afin de vous aider à choisir celle qui correspond le mieux à votre activité.

![](https://support.openfire.fr/hc/article_attachments/24422584969372)

### La méthode du coût standard

#### Logique de calcul du coût et de la valeur

Il s'agit de la **méthode **de calcul des coûts **par défaut** dans OpenFire.

Le **coût **du produit est **défini manuellement** dans sa fiche produit et sert à calculer la valorisation. Même si le prix d'achat indiqué sur un bon de commande diffère, la valorisation correspond au coût défini dans la fiche produit.

Chaque évolution du coût de la fiche article étant enregistrée dans une table d’historique.

#### Exemple

| **Etape** | **Opération** | **Coût unitaire** | **Qté dispo.** | **Valeur d’entrée ou de sortie** | **Valeur totale** |
| --- | --- | --- | --- | --- | --- |
| Start | Coût standard de l’article | 10 € |  |  |  |
| Etape 1 | Réception de 8 qté pour 10€ / unité | 10 € | 8 | + 80 € (8 * 10 €) | 80 € |
| Etape 2 | Réception de 4 qté pour 16€ / unité | 10 € | 12 | + 40 € (4 * 10 €) | 120 € |
| Etape 3 | Livraison de 10 unités | 10 € | 2 | -100 € (-10 * 10 €) | 20 € |
| Etape 4 | Réception de 2 qté pour 9€ / unité | 10 € | 4 | + 20 € (2 * 10 €) | 40 € |

#### Décryptage de l'exemple

**Etape ****1 : Réception conforme** **au coût**

Vous recevez 8 unités achetées à 10 €. Comme votre coût standard est de 10 €, la valeur d'entrée correspond au prix d'achat réel. Votre stock vaut 80 €.

**Etape ****2 : Réception de marchandise avec écart de prix d'achat**** versus le coût standard du projet**

Vous achetez 4 unités plus cher (16 €). **Attention** : OpenFire ignore ce prix de 16 € pour votre stock et utilise votre coût standard de 10 €. La valeur ajoutée est donc de 40 €, portant le total à 120 €.

**Etape 3 : Sortie de stock**

Vous livrez 10 unités. Le logiciel déduit ces articles au coût standard de 10 €. La valeur de votre inventaire baisse de 100 €. Il vous reste 2 unités pour une valeur de 20 €.

**Etape 4 : Réception finale : **nouvel achat à prix bas

Vous recevez 2 unités achetées à 9 €. Là encore, le logiciel applique votre coût standard de 10 € pour valoriser l'entrée. La valeur augmente de 20 €, pour un inventaire final de 40 €.

#### Pourquoi choisir cette méthode ?

Elle offre une grande stabilité comptable puisque la valeur de votre stock ne fluctue pas selon les aléas des prix du marché. Elle est pertinente si vos prix d'achat sont très stables ou si vous souhaitez travailler avec des marges théoriques fixes.

| 🚨**Avertissement** : Cette **méthode est peu précise et ne devrait pas être retenue si vous souhaitez utiliser OpenFire pour valoriser vos stocks** dans un contexte de forte variation de vos prix d'achat. Si vous utilisez cette méthode, n'oubliez pas de mettre à jour manuellement votre coût standard si vos tarifs fournisseurs changent durablement, afin que votre valorisation reste proche de la réalité économique. |
| --- |

###

### La méthode du coût moyen (AVCO)

La méthode **AVCO** est idéale pour les professionnels de la maintenance et de l'énergie. Contrairement au FIFO, elle permet de lisser les variations de prix d'achat en calculant une moyenne constante de la valeur de votre stock.

Dans OpenFire, la méthode AVCO recalcule le **Coût unitaire** à chaque nouvelle réception de marchandise.

- **Mélange des coûts** : Le prix des anciens articles en stock est fusionné avec le prix des nouveaux arrivants.
- **Stabilité lors des sorties** : Contrairement au FIFO, le coût utilisé pour une livraison ne change pas en fonction de l'ancienneté du lot, mais utilise la moyenne actuelle.

#### Logique de calcul du coût et de la valeur

OpenFire met à jour le **coût **automatiquement ; voici comment :

- **Analyse du stock disponible** : combien d'articles il vous reste en réserve et à quel prix ils ont été achetés.
- **Intégration des nouveaux achats** : ajout du prix et des quantités reçues.
- **Moyenne pondérée** : division de la valeur totale cumulée par le nombre total d'articles.

#### Exemple

| **Etape** | **Opération** | **Coût unitaire** | **Qté dispo.** | **Valeur d’entrée ou de sortie** | **Valeur totale** |
| --- | --- | --- | --- | --- | --- |
| Etape 1 | Réception de 8 qté pour 10€ / unité | 10 € | 8 | + 80 € (8 * 10 €) | 80 € |
| Etape 2 | Réception de 4 qté pour 16€ / unité | 12 € | 12 | + 64 € (4 * 16 €) | 144 € |
| Etape 3 | Livraison de 10 unités | 12 € | 2 | - 120 € (-10 * 12 €) | 24 € |
| Etape 4 | Réception de 2 qté pour 6€ / unité | 9 € | 4 | + 12 € (2 * 6 €) | 36 € |

#### Décryptage de l'exemple

Voici comment OpenFire traite les chiffres lors de ces mouvements successifs en AVCO :

**Etape 1 : **vous recevez 8 unités à 10 €. La valeur de l’inventaire est de 80 €. Le **Coût unitaire** est logiquement de 10 €.

**Etape 2 : Lissage du coût (La moyenne) : **Vous achetez 4 unités plus cher (16 €). La valeur du stock est calculée en additionnant la valeur du stock précédent et la valeur du stock entrant : 80 € + (4 * 16 €) = 144 €. Le coût unitaire est calculé en divisant la valeur du stock par la quantité en stock : 144 € / 12 = 12 €.

**Etape 3 : livraison & sortie de stock : **vous livrez 10 unités. Le coût unitaire moyen est utilisé pour calculer la valeur du stock, indépendamment du prix d’achat du produit. Par conséquent, la valeur du stock est de : 144 € - (10 * 12 €) = 24 €.

**Etape 4 : réception finale : **vous recevez 2 unités à un prix très bas (6 €). Valeur du stock : 24 € + (2 * 6 €) = 36 €. Coût unitaire : 36 € / 4  = 9 €.

#### Pourquoi choisir cette méthode ?

Méthode particulièrement utile pour les professionnels qui achètent des composants à des prix qui peuvent varier d'une commande à l'autre

- **Simplicité** : La valeur de votre stock est plus stable et moins sensible aux pics de prix temporaires.
- **Gestion des petites pièces** : Très efficace pour les fournitures de maintenance (visserie, joints, petits composants) où le suivi par lot individuel serait trop complexe.

| **🧑‍🏫Exemple** : Si vous achetez des sacs de granulés à différents prix durant l'hiver, l'AVCO vous permet de connaître le prix de revient moyen pour l'ensemble de vos contrats d'entretien |
| --- |

| 🚨**Avertissement** : Si vous modifiez manuellement le champ **Coût** dans la fiche produit, cela générera une écriture d'ajustement automatique pour recalculer la valeur totale de votre stock. La modification de la valeur numérique dans le champ Coût des produits de la catégorie concernée crée **un nouvel enregistrement dans le rapport d'évaluation des stocks afin d'ajuster la valeur du produit**.   **Création d'un enregistrement** : OpenFire crée une ligne dans votre "Rapport d'évaluation des stocks". **Ajustement de la valeur** : Cette ligne sert de preuve comptable pour justifier que la valeur totale de ce que vous avez en magasin a changé. **Mise à jour automatique** : Une fois cette modification faite, le logiciel reprend la main pour recalculer le coût lors de vos prochains achats. |
| --- |

### La méthode du FIFO (First in First Out)

Le **FIFO** (Premier Entré, Premier Sorti) est la méthode la plus précise. Elle suit le prix d'achat exact de chaque lot. Les articles les plus anciens sont considérés comme les premiers vendus.

- **Prix d'achat réel** : Contrairement au Coût Moyen Pondéré, le logiciel utilise le prix d'achat exact de chaque lot.
- **Rotation du stock** : Le prix de l'achat le plus ancien est utilisé comme coût pour la prochaine vente, jusqu'à ce que ce lot complet soit épuisé.
- **Mise à jour automatique** : Dès qu'un lot est terminé, le logiciel passe automatiquement au prix du lot suivant dans la file d'attente.

#### Logique de calcul du coût et de la valeur

Dans OpenFire, la valeur de votre inventaire et le coût unitaire sont recalculés à chaque étape :

- **Lors d'une réception (Entrée)** :
  1. **Valeur de l'inventaire** : On ajoute la valeur de la marchandise entrante à la valeur précédente.
  2. **Coût unitaire** : Il est calculé en divisant la valeur totale de l'inventaire par la quantité totale d'articles en main.
- **Lors d'une livraison (Sortie)** :
  1. **Valeur sortante** : On multiplie la quantité sortie par son prix d'achat d'origine.
  2. **Valeur de l'inventaire** : On soustrait la valeur sortante de la valeur précédente.
  3. **Coût unitaire** : On divise la nouvelle valeur de l'inventaire par la quantité restante.

#### Exemple

| **Etape** | **Opération** | **Coût unitaire** | **Qté dispo.** | **Valeur d’entrée ou de sortie** | **Valeur totale** |
| --- | --- | --- | --- | --- | --- |
| Etape 1 | Réception de 8 qté pour 10€ / unité | 10 € | 8 | + 80 € (8 * 10 €) | 80 € |
| Etape 2 | Réception de 4 qté pour 16€ / unité | 12 € | 12 | + 64 € (4 * 16 €) | 144 € |
| Etape 3 | Livraison de 10 unités | 16 € | 2 | -112€ (8*10€ + 2*16€) | 32 € |
| Etape 4 | Réception de 2 qté pour 6€ / unité | 11 € | 4 | +12 € (2 * 6€) | 44 € |

#### Décryptage de l'exemple

Voici comment OpenFire traite les chiffres lors de ces mouvements successifs en FIFO :

**Etape 1** : Vous recevez 8 unités achetées à 10 €. Votre stock vaut 80 € et le coût affiché est de 10 €.

**Etape 2** : Vous recevez 4 unités supplémentaires, mais le prix fournisseur a augmenté à 16 €. La valeur totale grimpe à **144 €** (80 € anciens + 64 € nouveaux). Le **Coût unitaire** moyen affiché par le logiciel devient **12 €** ($144 € / 12$ unités).

**Etape 3 : la livraison (La logique "Premier Entré, Premier Sorti") :** OpenFire puise d'abord dans le lot le plus ancien. Il prend les 8 unités du premier lot (à 10 € = 80 €). Il prend les 2 unités manquantes dans le deuxième lot (à 16 € = 32 €). Résultat : La valeur totale sortie est de 112 €. Il vous reste 2 unités en stock, qui proviennent du lot à 16 €. Coût unitaire : Le coût affiché passe à 16 €, car c'est la valeur réelle des articles restants.

**Réception finale : v**ous recevez 2 unités à un prix très bas (6 €). La valeur totale devient **44 €** (32 € restants + 12 € nouveaux). Le coût moyen pondéré affiché pour vos 4 unités disponibles est maintenant de **11 €** ($44 € / 4$).

#### Pourquoi choisir cette méthode ?

- **Précision des données** : Cette méthode est la plus fidèle à la réalité économique, mais elle est très sensible aux erreurs de saisie humaine. Vérifiez toujours vos prix d'achat avant de valider une réception
- **Traçabilité** : Utilisez la méthode FIFO si vous travaillez avec des composants dont les prix fluctuent rapidement, comme dans le secteur du **Photovoltaïque** ou du **CVC**.

| 🚨**Avertissement** : Une erreur de prix sur une réception faussera toute votre file d'attente de coûts jusqu'à épuisement complet de ce lot. |
| --- |

### Règles spéciales de mise à jour du coût de vos articles

Si vous sélectionnez la méthode de coût **FIFO** ou **AVCO** pour une catégorie, trois paramètres additionnels s'affichent pour affiner la gestion de vos valeurs :

![](https://support.openfire.fr/hc/article_attachments/24431295268508)

**Mettre à jour le coût des articles suite aux mouvements de stocks : **cette option assure que le champ **Coût** de la fiche article est actualisé après chaque mouvement (entrée ou sortie), conformément à la méthode de calcul choisie. Par défaut, ce paramètre est activé (**Vrai**).

| 💡**Note **: nous recommandons de ne pas désactiver ce paramètre afin de garantir la précision de la valorisation de votre inventaire. |
| --- |

**Mettre à jour le coût des articles suite aux imports : **ce réglage permet de protéger le champ **Coût **lors d'un import de données. Il évite que le **coût **du produit soit écrasé par l'application automatique des conditions commerciales liées à la marque du produit. Par défaut, ce paramètre est désactivé (**Faux**).

| 🚨**Avertissement** : ce paramètre n'empêche pas une mise à jour manuelle via un import standard si vous forcez le champ Coût dans votre fichier. Il sert principalement à bloquer la mise à jour automatique par les tarifs théoriques de la marque. |
| --- |

**Coût pour les ventes : **ce champ vous permet de choisir la référence utilisée pour calculer vos marges dans les devis.

- **Coût** : base la marge sur le prix de revient réel en stock.
- **Coût théorique** : base la marge sur le prix d'achat théorique renseigné sur la fiche article.

## Bonnes pratiques

- **Uniformité** : utilisez la même méthode de valorisation pour tous les produits d'une même catégorie afin de ne pas fausser vos analyses de marge.
- **Anticipation **: déterminez au préalable, pour chaque catégorie ou groupe de catégories, les règles de valorisation à appliquer, les changements de configuration en cours d'activité ayant des conséquences significatives sur la valeur de votre stock.
- **Méthode **: lorsque vous ajoutez une nouvelle catégorie de produit, dupliquez une catégorie de même nature afin d'en dupliquer les paramétrages sensibles

Mis a jour le : 29/12/2025
