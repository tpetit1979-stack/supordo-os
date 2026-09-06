---
source: https://support.openfire.fr/hc/fr/articles/19084741405212-Facturer-un-acompte
categorie: Utiliser OpenFire
titre: Facturer un acompte
date_recuperation: 2026-09-05
---

# Facturer un acompte

Cet article vous présente comment générer une facture depuis un bon de commande OpenFire.

La facture d’acompte est établie en fonction de la position fiscale définie pour la commande. Elle peut être calculée soit sur la base d’un pourcentage du montant total, soit en appliquant un montant fixe. Lorsqu’un montant spécifique est facturé en tant qu’acompte, celui-ci peut, selon la configuration choisie, être considéré comme hors taxes (HT) ou toutes taxes comprises (TTC).

💡Notes : Les factures d'acompte ne peuvent être créées automatiquement que depuis un bon de commande client.

Lorsqu'un bon de commande est à facturer, le bouton **Créer une facture** en haut à gauche apparaît :

![](https://support.openfire.fr/hc/article_attachments/20226736851100)

Cliquez dessus pour débuter votre facturation et choisissez le type de facture à créer.

![](https://support.openfire.fr/hc/article_attachments/20226755669020)

Pour créer une facture d'acompte, choisissez l'une des deux options suivantes :

- **Acompte (pourcentage)** : en tenant compte de l'échéancier de votre bon de commande, OpenFire vous présélectionne le pourcentage de l’acompte. Vous pouvez modifier ce pourcentage si vous le souhaitez.
- **Acompte (montant fixe)** : en tenant compte de l'échéancier de votre bon de commande, OpenFire présélectionne le montant de l’acompte. Vous pouvez modifier ce montant si vous le souhaitez. Selon votre configuration, le montant peut être compris comme HT ou TTC.

**📓**Pour aller plus loin → [Configurer vos factures d'acompte](https://openfire.zendesk.com/knowledge/editor/01JVYN2J8DW5FHSRMG4DQDAPQA/fr?brand_id=14865518450076)

Le bouton **Créer et Afficher la facture **vous permet de générer la facture et d'être dirigé dessus directement.

Le bouton **Créer une facture** vous permet de générer la facture mais de rester sur le bon de commande.

La facture d’acompte est créée en brouillon, avec les caractéristiques suivantes :

- Elle est créée en brouillon et peut être modifiée.
- Le montant de l’acompte est porté sur une ligne de produit Acompte.
- Le numéro de la commande est repris comme origine de la facture.

![](https://support.openfire.fr/hc/article_attachments/20226755670812)

Dans la commande d’origine, une ligne de commande est ajoutée, dans une section “**Acompte**” dédiée, détaillant le montant de l’acompte facturé.

Cette ligne est directement rattachée à la facture d’acompte générée, et permettra de déduire de la facturation finale les acomptes déjà facturés. **Vous ne pouvez donc pas la modifier ou la supprimer.**

![](https://support.openfire.fr/hc/article_attachments/20226755675676)

Mis a jour le : 30/12/2025
