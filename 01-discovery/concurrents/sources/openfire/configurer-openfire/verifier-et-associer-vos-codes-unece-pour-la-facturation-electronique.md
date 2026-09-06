---
source: https://support.openfire.fr/hc/fr/articles/28951137996316-V%C3%A9rifier-et-associer-vos-codes-UNECE-pour-la-facturation-%C3%A9lectronique
categorie: Configurer OpenFire
titre: Vérifier et associer vos codes UNECE pour la facturation électronique
date_recuperation: 2026-09-05
---

# Vérifier et associer vos codes UNECE pour la facturation électronique

Cet article vous guide pas à pas dans la configuration et la vérification des codes UNECE au sein de votre logiciel OpenFire. Ces codes standardisés sont indispensables pour garantir que vos factures électroniques sortantes respectent strictement les normes de la réforme française et ne soient pas rejetées par les plateformes de vos acheteurs.

Cet article contient les sections suivantes :

- [Section 1 : Qu'est-ce qu'un code UNECE et pourquoi est-il essentiel ?](#h_01KXNEXG1C0WWZSZKNE32E1EMV)
- [Section 2 : Consulter la liste globale des codes UNECE](#h_01KXNEXG1GEM2BK2PR133CG5JB)
- [Section 3 : Vérifier les codes UNECE de vos taxes](#h_01KXNEXG1MGAGDF3A8NZ9TN6Y5)
- [Section 4 : Vérifier les codes UNECE de vos unités de mesure](#h_01KXNEXG2GF6JF4ZA66ZF6QTJ6)
- [Section 5 : Vérifier les codes UNECE de vos méthodes de paiement](#h_01KXNEXG30VH2EHYWGTVS23ESP)
- [Bonnes pratiques](#h_01KXNEXG3QJDEFTMPE855YHY3D)

## Section 1 : Qu'est-ce qu'un code UNECE et pourquoi est-il essentiel ?

Les codes UNECE (ou codes CEE-ONU) sont des identifiants standards internationaux établis par la Commission économique pour l'Europe des Nations Unies (*United Nations Economic Commission for Europe*).

Dans le cadre de la facturation électronique, ces codes servent à traduire de manière universelle les unités de mesure, les pays, les catégories de taxes ou encore les conditions de paiement. Ils permettent aux logiciels de gestion et aux futures Plateformes Agréées (PA) de se comprendre automatiquement, sans ambiguïté linguistique ou textuelle.

| 🚨**Avertissement** : Si l'un de ces codes est manquant ou incorrect sur vos factures sortantes (notamment aux formats Factur-X ou UBL), la plateforme de votre acheteur rejettera automatiquement votre facture pour cause de syntaxe invalide. |
| --- |

| 💡**Note **:  Dans OpenFire, nous avons déjà réalisé une pré-association par défaut pour la majorité de vos configurations. Il vous revient toutefois de les vérifier précisément en suivant ce guide. |
| --- |

## Section 2 : Consulter la liste globale des codes UNECE

Avant de commencer vos vérifications, vous pouvez visualiser l'ensemble des codes disponibles dans votre base de données.

Suivre le chemin d'accès suivant : Paramètres > Techniques > Liste des codes UNECE

Cette liste regroupe trois grandes familles de dictionnaires indispensables pour la facturation électronique :

- **Moyens de paiement**
- **Catégories de taxes**
- **Types de taxes**

## Section 3 : Vérifier les codes UNECE de vos taxes

Chaque taxe de votre grille comptable doit être associée à sa codification internationale standardisée.

Suivre le chemin d'accès suivant : Comptabilité > Configuration > Taxes

- Cliquer sur la taxe que vous souhaitez configurer.
- Repérer les champs **Type de taxe de l'UNECE** et **Catégorie de taxe de l'UNECE**.

![](https://support.openfire.fr/hc/article_attachments/28951266006044)

- Sélectionner les codes correspondants en vous aidant du tableau de correspondance ci-dessous :

| **Type de TVA** | **Type (UNECE)** | **Catégorie (UNECE)** | **Commentaire / Mention obligatoire** | Motif d'exemption de TVA |
| --- | --- | --- | --- | --- |
| **TVA Standard (20%)** | `VAT` | `S` (Standard rate) | Taux par défaut pour la majorité des prestations de vente de matériel ou de main d'œuvre standard. |  |
| **TVA Réduite (10% ou 5.5%)** | `VAT` | `S` (Standard rate) | Même catégorie `S` que le taux normal, seule la valeur numérique de la taxe change (rénovation énergétique, pose de PAC ou solaire). |  |
| **Autoliquidation - Sous-traitance** | `VAT` | `AE` (Vat Reverse Charge) | Obligatoire pour les artisans sous-traitants d'un donneur d'ordre. Déclenche automatiquement la mention légale "Autoliquidation" sur le PDF. |  |
| **Ventes UE 0%** | `VAT` | `K` (VAT exempt for EEA intra-community supply of goods and services) | Indique que l'article est exonéré de TVA en raison d'une livraison intracommunautaire au sein de l'Espace économique européen. | VATEX-EU-K |
| **TVA 0% export hors UE (vente)** | `VAT` | `G` Free export item, tax not charged | Code indiquant que l'article est libre d'exportation et exonéré de taxes | VATEX-EU-G |

| **🧑‍🏫Exemple** :  Pour une taxe standard à 20 %, le champ **Type de taxe de l'UNECE** doit afficher `[VAT] Value added tax` et le champ **Catégorie de taxe de l'UNECE** doit afficher `[S] Standard rate`. |
| --- |

## Section 4 : Vérifier les codes UNECE de vos unités de mesure

Vos unités de vente doivent également être configurées afin que le format de votre facture (comme le format Factur-X) comprenne la nature des quantités facturées.

Suivre le chemin d'accès suivant : Ventes > Configuration > Unité de mesure

- Cliquer sur l'unité de mesure à vérifier.
- Repérer le champ **Code UNECE**.

![](https://support.openfire.fr/hc/article_attachments/28951421876508)

Exemple des principales valeurs de référence :

- **Métiers du Temps Passé & Main d'œuvre (Tous secteurs)** :

  - `HUR` (Hour) : L'heure. Indispensable pour la main d'œuvre au temps passé.
  - `EA` (Each) : L'élément / L'unité. Très utilisé pour facturer un forfait unique (forfait déplacement, forfait mise en service).
  - `DAY` (Day) : Le jour. Pour les chantiers de rénovation chiffrés à la journée.
- **Génie Climatique, Chauffage, Froid & Solaire (Installation)** :

  - `C62` (One / Unit) : La pièce / L'unité. Le code idéal pour tout le matériel individualisable (pompe à chaleur, chaudière, onduleur, etc.).
  - `SET` (Set) : Le kit / L'ensemble. Pour les configurations vendues comme un ensemble indissociable (kit de raccordement).
  - `LBR` (Pound) ou `KGM` (Kilogram) : Pour la recharge ou la récupération des fluides frigorigènes lors des entretiens.
- **Câblage, Réseaux, Tuyauterie & Consommables** :

  - `MTR` (Metre) : Le mètre. Pour le linéaire (liaison frigorifique en cuivre, câble électrique).
  - `MTK` (Square metre) : Le mètre carré. Pour les isolants ou l'intégration des panneaux solaires en toiture.
  - `LTR` (Litre) : Le litre. Pour le remplissage des circuits (liquide caloporteur, glycol, désembouant).
- **Acteurs de la Maintenance Récurrente (Contrats, Dépannage)** :

  - `ANN` (Year) : L'année. Pour la facturation des contrats de maintenance annuels.
  - `MON` (Month) : Le mois. Pour les abonnements de maintenance facturés mensuellement.

## Section 5 : Vérifier les codes UNECE de vos méthodes de paiement

Le mode de règlement prévu sur la facture doit lui aussi correspondre à la table internationale officielle validée par l'AFNOR.

Suivre le chemin d'accès suivant : Comptabilité > Configuration > Méthode de paiement

- Cliquer sur la méthode de paiement à configurer.
- Saisir la valeur correspondante dans le champ **Code UNECE.**

![](https://support.openfire.fr/hc/article_attachments/28951391731740)

Exemple des principales valeurs de référence :

| **Mode de règlement dans OpenFire** | **Code UNECE** | **Nom officiel (AFNOR)** | **Usage terrain pour vos équipes** |
| --- | --- | --- | --- |
| **Manuel / non spécifié** | `1` | `Instrument not defined` | Code de secours : si le mode de règlement n'est pas encore connu à l'émission de la facture, il évite les rejets automatiques par la PA. |
| **Espèces** | `10` | `Cash` | Dépannages rapides. Attention à l'obligation de traçabilité inaltérable NF525 dans votre module de caisse. |
| **Chèque** | `20` | `Cheque` | Très utilisé en fin de chantier dans le bâtiment. |
| **Virement standard** | `30` | `Credit transfer` | Pour les virements hors zone euro ou flux spécifiques. |
| **Carte Bancaire** | `42` | `Payment to bank account` | Encaissé par le technicien sur son TPE portable en fin d'intervention. |
| **Prélèvement standard** | `49` | `Direct debit` | Pour les prélèvements hors cadre standard SEPA. |
| **Virement SEPA** | `58` | `SEPA credit transfer` | Le code principal pour le paiement des acomptes et soldes de chantiers (installations de PAC, panneaux solaires). |
| **Prélèvement SEPA** | `59` | `SEPA direct debit` | Idéal pour vos clients qui gèrent des abonnements ou des contrats de maintenance récurrents (chauffage, poêles). |

## Bonnes pratiques

**Le code de secours **`**1**` : Si vous ne savez pas encore comment votre client va régler sa facture au moment de l'émission, utilisez le code **1** (`Instrument not defined`). Cela permet de valider la facture sans bloquer le flux d'envoi vers la Plateforme Agréée.

Mis a jour le : 06/08/2026
