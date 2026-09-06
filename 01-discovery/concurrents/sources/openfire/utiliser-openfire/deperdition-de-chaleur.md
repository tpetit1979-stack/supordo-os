---
source: https://support.openfire.fr/hc/fr/articles/26207308414108-D%C3%A9perdition-de-chaleur
categorie: Utiliser OpenFire
titre: Déperdition de chaleur
date_recuperation: 2026-09-05
---

# Déperdition de chaleur

Cet article vous accompagne dans l'utilisation de l'outil de calcul de déperdition de chaleur intégré à OpenFire. Grâce à cette fonctionnalité, vous pourrez estimer la puissance nécessaire (en kW) pour chauffer une habitation et proposer l'appareil le mieux adapté à votre client.

Cet article contient les sections suivantes :

- [Prérequis et accès](#h_01KM0J1NDB866E2N4KZMFY0VNM)
- [Créer un nouveau calcul](#h_01KM0J1NDCSN2KC4YVCHHHJNRE)

  - [Renseigner les informations du contact](#h_01KM0J1NDCN69T4YR1MCF5987B)
  - [Définir les caractéristiques du bâtiment](#h_01KM0J1NDEDBWRAYTVS7M7K6WD)
- [Obtenir et analyser les résultats](#h_01KM0J1NDHTE0Z8WQR80QNKH7W)

  - [Calculer la déperdition et la consommation](#h_01KM0J1NDHSVHENXMJS05ZGA9M)
  - [Comparer les consommations par combustible](#h_01KM0J1NDJK1CXGQS9X59PD0X9)
  - [Consulter les appareils compatibles](#h_01KM0J1NDM2V9K2P6F8PET9R5A)
- [Éditer et envoyer le rapport PDF](#h_01KM0J1NDN4YHKCDMNPZKT6QKN)

# Prérequis et accès

L'outil de calcul est disponible pour les professionnels via le module **Calculs**.

`Suivre le chemin d'accès suivant : Application > Calculs > Calcul de déperdition de chaleur et de consommation.`

| 💡**Note **: Si ce module n'apparaît pas sur votre base, contactez le support OpenFire par mail à support@openfire.fr ou par téléphone au 02.30.96.02.65. |
| --- |

# Créer un nouveau calcul

## Renseigner les informations du contact

Pour commencer une nouvelle simulation, cliquez sur le bouton **Nouveau**.

![](https://support.openfire.fr/hc/article_attachments/26207345252508)

- Sélectionnez un client existant dans le champ **Contact** ou saisissez un nom manuellement dans le champ **Nom**.
- Renseignez l'**Adresse**, le **Code postal** et la **Ville**.
- Indiquez l'**Altitude** de l'habitation : elle est essentielle pour déterminer la température extérieure de base.

## Définir les caractéristiques du bâtiment

Cette section permet de modéliser le volume et l'isolation du logement.

![](https://support.openfire.fr/hc/article_attachments/26207308408860)

- Saisissez la **Surface à chauffer (en m²)** et la **Hauteur sous plafond**.
- Indiquez la **Température de confort désirée** (généralement 19°C ou 20°C).
- Sélectionnez la **Date de construction**.

  - Pour les bâtiments récents (après 2005), le coefficient d'isolation est déduit de la norme (ex: RT 2012).
  - Pour les bâtiments anciens, précisez le type de **Murs**, de **Toiture** et de **Plancher bas** pour affiner le calcul.

# Obtenir et analyser les résultats

## Calculer la déperdition et la consommation

Une fois la saisie terminée, cliquez sur le bouton **Calculer**. Le système affiche instantanément :

- **Déperdition de chaleur** : la puissance nominale requise pour l'appareil (en kW).
- **Consommation annuelle** : l'énergie totale estimée nécessaire pour une année (en kWh/an).

## Comparer les consommations par combustible

L'onglet **Consommation par combustible** est un outil de vente puissant. Il permet de traduire la consommation annuelle en quantités concrètes selon l'énergie choisie.

![](https://support.openfire.fr/hc/article_attachments/26207308408988)

| **🧑‍🏫Exemple** : Pour un besoin de 5 800 kWh/an, vous pourrez montrer à votre client qu'il consommera environ 1,4 tonnes de bûche, contre 600 litres de fioul avec un coût estimé de 430€ pour l'un et 625€ pour l'autre. |
| --- |

## Consulter les appareils compatibles

![](https://support.openfire.fr/hc/article_attachments/26207345254684)

Dans l'onglet **Appareils compatibles**, OpenFire liste les produits de votre catalogue dont la puissance correspond au calcul.

- Cochez la case **Impression** en bout de ligne pour que l'appareil soit intégré au rapport final.

# Lier le calcul à une opportunité ou une commande

Pour assurer le suivi commercial, il est fortement conseillé de rattacher votre calcul à un dossier de vente.

![](https://support.openfire.fr/hc/article_attachments/26209011391644)

- Allez dans l'onglet **Opportunité / Commande**.
- Dans le champ **Opportunité**, sélectionnez l'affaire en cours pour ce client.
- Si la vente est déjà plus avancée, vous pouvez également lier le calcul à un **Bon de commande**.

| 💡**Note **: Cette liaison permet de retrouver le calcul de déperdition directement depuis la fiche de l'opportunité ou du devis de votre client, centralisant ainsi toutes les informations techniques et commerciales. |
| --- |

# Éditer et envoyer le rapport PDF

![](https://support.openfire.fr/hc/article_attachments/26207308412828)

- Cliquez sur le bouton **Imprimer** puis sélectionnez **Rapport de déperdition de chaleur**.
- Pour transmettre le document, cliquez sur **Envoyer par email**.

| 🚨**Avertissement** : Cette estimation est un outil d'aide à la vente. Elle ne remplace en aucun cas une étude thermique réglementaire réalisée par un bureau d'études. |
| --- |

# Méthodologie

Pour plus de précision sur le calcul effectué, n'hésitez pas à consulter notre méthodologie sur site [deperditiondechaleur.fr](https://deperditiondechaleur.fr/methodologie)

# Bonnes pratiques

- **Géolocalisation :** Assurez-vous que l'adresse est complète pour que le logiciel récupère automatiquement le bon département et le DJU (Degré Jour Unifié) associé.
- **Sélection d'appareils :** Si aucune case n'est cochée dans le tableau des appareils compatibles, le tableau n'apparaîtra pas sur le rapport final.
- **Précision :** Pour les bâtiments anciens, prenez le temps de renseigner le type d'isolation des parois pour éviter de surdimensionner le poêle.

Mis a jour le : 18/03/2026
