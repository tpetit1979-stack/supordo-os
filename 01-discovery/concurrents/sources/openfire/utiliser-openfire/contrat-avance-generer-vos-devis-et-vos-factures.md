---
source: https://support.openfire.fr/hc/fr/articles/23885779064988-Contrat-avanc%C3%A9-G%C3%A9n%C3%A9rer-vos-devis-et-vos-factures
categorie: Utiliser OpenFire
titre: Contrat avancé : Générer vos devis et vos factures
date_recuperation: 2026-09-05
---

# Contrat avancé : Générer vos devis et vos factures

Cet article vous présente comment générer les commandes et facturer vos contrats d'entretien, qu'ils soit récurrents ou à la prestation.

Cet article contient les sections suivantes :

- [Principe de fonctionnement](#h_01KB3V9N5WAS4VV0N9T12GXCE3)
- [Facturer vos contrats récurrents](#h_01KB3VA6ZPX1KCJF3GY7SW8A96)
  - [Générer les commandes de vos contrats récurrents](#h_01KB3W7HJ14XP3PTQN508P808H)
  - [Facturer les commandes de vos contrats récurrents](#h_01KB3WCPGAJWTBM1M5RYFWHXCY)
- [Facturer vos contrats à la prestation](#h_01KB3VC13KHGMH367P7QENA7HW)
  - [Générer les commandes de vos contrats à la prestation](#h_01KB3YNM86KWX48EVZJB9E4XP6)
  - [Facturer les commandes de vos contrats à la prestation](#h_01KB3W67C1W8XQP8GFX85JBGVJ)

# Principe de fonctionnement

Pour rappel, vous pouvez générer, pour chacun de vos contrats d'entretien et pour chaque période de facturation, soit des commandes, soit des factures.  Bien que rajoutant une étape, nous vous recommandons de choisir la génération de ***ventes** *plutôt que celle de ***factures ***pour les raisons suivantes :

- **Facilite l'analyse du prévisionnel de facturation** sur la période puisque l'ensemble des ventes à date de facturation cible auront été générées dès le début de la période.
- **Uniformise vos processus** : toute la facturation de l'entreprise s'appuie sur un seul et même flux : la facturation des bons de commande.
- **Simplifie la gestion des exceptions** en cours de contrat (avoirs, reports, etc.).

Quelle que soit l'option retenue, la méthode de génération reste la même.

Le présent article détaille l'action de génération des commandes, et leur facturation.

| 💡**Note **: Pour générer vos commandes ou vos factures, il est essentiel que votre contrat soit correctement configuré avec les informations de facturation. |
| --- |

| 📓**Pour aller plus loin** → Créer un contrat d'entretien |
| --- |

La méthode de génération diffère selon qu'il s'agit d'un contrat en facturation récurrente ou en facturation à la prestation.

# Facturer vos contrats récurrents

## Générer les commandes de vos contrats récurrents

La génération des Commande est à faire de préférence au début de chaque période annuelle du contrat, pour en simplifier le suivi.

1. Accéder à la liste de vos contrats.
2. Sélectionner le contrat concerné.
3. Cliquer sur le bouton d’action **GENERER LES DOCUMENTS**.

![](https://support.openfire.fr/hc/article_attachments/23886143229852)

Une fenêtre s’ouvre. Vous avez le choix entre deux options :

- **Seulement la prochaine récurrence :** prochaine date de facturation uniquement => Crée un seul document (devis ou facture) pour la prochaine échéance.
- **Récurrence dans la période choisie :** tous les documents de la période sélectionnée => Crée l’ensemble des documents (devis ou facture) jusqu'à la date sélectionnée. Vous pouvez ensuite choisir de regrouper ces documents (commande ou facture) en un seul ou d'en créer un pour chaque échéance de facturation prévue.

![](https://support.openfire.fr/hc/article_attachments/23886143232796)

OpenFire créera les commandes ou les factures correspondantes et les liera à votre contrat et à ses lignes.

| 💡**Note **: il est recommandé de générer simultanément tous les documents de vente (devis ou facture) de la période du contrat en cours pour en simplifier le suivi. |
| --- |

Exemple pour une facturation en 12 échéances mensuelles :

- OpenFire créé une ligne par échéance
- Chaque ligne à une date de facturation prévisionnelle correspondant à l'échéance à facturer

![](https://support.openfire.fr/hc/article_attachments/23886143233564)

## Facturer les commandes de vos contrats récurrents

Pour les commandes générées en lien avec un contrat en facturation récurrente, une politique de facturation dédiée est utilisée : **Date contractuelle.**

![](https://support.openfire.fr/hc/article_attachments/23886124177436)

Cette politique de facturation permet d'anticiper la facturation des lignes de commande d'un contrat en se basant sur la sélection d'une date future.

| **🧑‍🏫Exemple** : je suis le 25 septembre et je veux facturer en avance toutes les échéances de contrat facturables au 1er octobre. |
| --- |

Cette option est disponible dans la fenêtre de facturation classique de votre bon de commande.

Pour l'utiliser :

- Cocher la case : **Forcer la facturation des échéances du contrat**.
- Définissez la date cible de facturation.
- Créer la facture.

OpenFire facturera alors **toutes les échéances** dont les lignes **ayant des quantités à facturer** et dont la date de facturation prévisionnelle est **antérieure ou égale à la date définie**.

![](https://support.openfire.fr/hc/article_attachments/23886245377692)

# Facturer vos contrats à la prestation

## Générer les commandes de vos contrats à la prestation

Pour vos contrats à la prestation, la génération des bons de commande relatives aux prestations du contrat est réalisées au travers de l'action de génération des Demandes d'Interventions.

Les principes de cette méthode :

- Pour les contrats à la prestation, l'action **GENERER LES DOCUMENTS** n'est pas disponible.
- La génération des commandes passe exclusivement par l'action de création des DI.
- Chaque Demande d'Intervention générée est liée à sa commande (1 Demande d'Intervention = 1 commande).

Pour générer les Demandes d'Intervention et leurs commandes depuis votre contrat :

- Cliquez sur l'action **GENERER LES DI.**
- Définissez la période pour laquelle vous souhaitez créer les DI et leurs commandes.
- Cliquez sur **GENERER.**

![](https://support.openfire.fr/hc/article_attachments/23886424150044)

OpenFire créé alors toutes les DI de la période et les commandes associées.

Les commandes générées ont les caractéristiques suivantes :

- Le champ **Demande d'Intervention d'origine** est valorisée avec la DI d'origine.
- La **date de facturation prévisionnelle** de la ligne est définie avec la date de **début de la période de la planification** de la DI associée.
- Si vous **annulez** ou **supprimez **la **Demande d'Intervention**, la commande associée est annulée automatiquement.
- Une** politique de facturation** dédiée est attribuée : **À chaque prestation.**

![](https://support.openfire.fr/hc/article_attachments/23886455464860)

Vous retrouvez depuis la Demande d'Intervention les informations de la commande associée :

![](https://support.openfire.fr/hc/article_attachments/23886455464988)

## Facturer les commandes de vos contrats à la prestation

La politique de facturation **A chaque prestation** permet de lié à la facturation de la commande à la réalisation de l'intervention associée. La commande ne passera "À facturer" que lorsque l'intervention aura été planifiée et réalisée.

![](https://support.openfire.fr/hc/article_attachments/23886455465116)

Une fois l'intervention réalisée, la commande passe automatiquement ***facturable :***

- La commande ressort dans la liste des commandes à facturer.
- Elle peut être facturée de façon classique, comme n'importe quel autre bon de commande.

Mis a jour le : 29/12/2025
