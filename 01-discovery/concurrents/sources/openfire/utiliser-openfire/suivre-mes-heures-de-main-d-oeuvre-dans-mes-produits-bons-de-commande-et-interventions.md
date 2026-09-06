---
source: https://support.openfire.fr/hc/fr/articles/22682929135132-Suivre-mes-heures-de-main-d-oeuvre-dans-mes-produits-bons-de-commande-et-interventions
categorie: Utiliser OpenFire
titre: Suivre mes heures de main d'oeuvre dans mes produits, bons de commande et interventions
date_recuperation: 2026-09-05
---

# Suivre mes heures de main d'oeuvre dans mes produits, bons de commande et interventions

Cet article vous explique comment associer des heures de main d'oeuvre à des produits et à les suivre dans vos devis, bons de commande et interventions.

**Module**: *of_sale_project.*

Cet article contient les sections suivantes:

- [Ajouter des heures de main d'oeuvre sur un produit ou sur un kit](#h_01K6G2V4S7NV2GH4CV5TMVZAYS)
- [Consulter les heures de main d'oeuvre associées à un devis/bon de commande](#h_01K6G57JR425ZBF0398WEY9CHD)
- [Gérer la durée d'une intervention issue d'un devis/bon de commande contenant des heures de main d'oeuvre](#h_01K6JHSS80PKXB01DWQ8T91Q8V)

## Ajouter des heures de main d'oeuvre sur un produit ou sur un kit

---

Vous avez la possibilité d'associer des heures de projet (ou de main d'oeuvre) à un produit.

Pour cela, rendez-vous dans l'onglet "Vente" et dans la section "Projets". La durée est à renseigner au format (Heures : Minutes).

![](https://support.openfire.fr/hc/article_attachments/22684562151836)

*Dans cet exemple, on estime une durée de main d'oeuvre de 30min nécessaire pour installer le produit Tubage.*

Lorsque le produit est un **kit**, la durée est calculée comme la **somme des durées des composants du kit**. Elle est donc non modifiable.

*Si mon kit contient 2 unités d'un composant A de durée 0:30, et 1 unité d'un composant B de durée 1, la durée du kit sera calculée à 02:00.*

## Consulter les heures de main d'oeuvre associées à un devis/bon de commande

---

Lorsque vous créez un devis ou un bon de commande, la durée de projet des produits impliqués est bien reportée.

Vous retrouvez la durée de main d'oeuvre de vos produits dans les lignes de commande. Vous pouvez la sélectionner dans les filtres à droite si elle ne s'affiche pas par défaut.

![](https://support.openfire.fr/hc/article_attachments/22706633020828)

Vous retrouvez la durée totale de main d'oeuvre des différents produits dans l'onglet "Suivi", section "Projet" de votre devis/bon de commande.

![](https://support.openfire.fr/hc/article_attachments/22684562154012)

Cette durée étant calculée automatiquement à partir des produits ajoutés dans les lignes du devis/bon de commande, elle est non modifiable.

Vous pouvez consulter la durée de projet associée à vos bons de commande depuis la vue liste des bons de commande. Si nécessaire, vous pouvez l'afficher ou la masquer grâce aux filtres à droite de la vue liste.

![](https://support.openfire.fr/hc/article_attachments/22706633022364)

## Gérer la durée d'une intervention issue d'un devis/bon de commande contenant des heures de main d'oeuvre

---

La durée de projet (main d'oeuvre) calculée sur le devis/bon de commande est conservée lorsque vous créez une demande d'intervention ou une intervention à partir de ce bon de commande.

![](https://support.openfire.fr/hc/article_attachments/22706650622620)

| 💡**Note **: L'ajout ou la modification d'un             modèle d'intervention, ou d'une tâche sur votre DI/intervention             ne viendra pas écraser la durée calculée à partir du bon             de commande. Vous avez la main pour modifier             la durée de l'intervention si nécessaire. |
| --- |

Mis a jour le : 06/10/2025
