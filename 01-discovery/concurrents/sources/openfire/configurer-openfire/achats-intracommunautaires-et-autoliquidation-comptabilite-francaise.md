---
source: https://support.openfire.fr/hc/fr/articles/21430467360028-Achats-Intracommunautaires-et-Autoliquidation-Comptabilit%C3%A9-fran%C3%A7aise
categorie: Configurer OpenFire
titre: Achats Intracommunautaires et Autoliquidation (Comptabilité française)
date_recuperation: 2026-09-05
---

# Achats Intracommunautaires et Autoliquidation (Comptabilité française)

Cet article vous guide dans la configuration des taxes **Achats intracommunautaires** et A**utoliquidation** pour la sous-traitance, afin d'assurer leur correcte imputation comptable dans OpenFire.

Cet article contient les sections suivantes :

- Achats Intracommunautaires
- Sous-traitance et TVA en Autoliquidation

# Achats Intracommunautaires

---

Les achats intracommunautaires désignent les acquisitions de biens ou de services auprès d'entreprises non immatriculées en France mais résidentes de l'Union Européenne.

Les particularités de la TVA intracommunautaire sont les suivantes :

- Elle est à la fois collectée et déduite pour l'entreprise qui réalise l'achat.
- Elle dispose de lignes spécifiques pour son traitement sur la déclaration CA3.

## Les composants de la TVA Intracommunautaire

**Dans OpenFire, les Taxes relatives à la gestion des achats intra-communautaires sont définies par défaut.**

Pour les consulter, suivez le chemin d'accès suivant :

- Facturation > Configuration > Comptabilité > Taxes.

Pour gérer la TVA intracommunautaire de manière optimale dans OpenFire, nous vous recommandons d'utiliser une taxe de type **Groupe de taxes**.

### Les comptes d'imputation des différentes taxes du groupe

![](https://support.openfire.fr/hc/article_attachments/21431736897052)

### Les taxes du groupe

![](https://support.openfire.fr/hc/article_attachments/21431736897692)

#### TVA due s/ acq. Intracom 20% :

- Taux de -20% (taux applicable en France),
- **Type de taxe** réglé sur **Achats**,
- Compte d'imputation de la taxe : **44521000 TVA due sur prestations intracommunautaires**.

#### TVA déd. s/ acq. Intracom 20%:

- Taux de 20% (taux applicable en France),
- **Type de taxe** réglé sur **Achats**,
- Compte d'imputation de la taxe : **44566200 TVA déductible intracommunautaire.**

### La taxe de type groupe "TVA Intracommunautaire" :

![](https://support.openfire.fr/hc/article_attachments/21431736898076)

### La position fiscale "Achats UE"

Une position fiscale spécifique est généralement associée à ces achats intracommunautaires pour automatiser l'application de ce groupe de taxes.

![](https://support.openfire.fr/hc/article_attachments/21431658316188)

## Exemple d'utilisation

🧑‍🏫Exemple : Lors de la saisie d'une facture d'achat intracommunautaire, vous appliquerez le groupe de taxes "**TVA Intracommunautaire**" à votre ligne de produit. OpenFire calculera simultanément la TVA due (collectée) et la TVA déductible. Le montant net de TVA sur la facture sera de zéro, mais les écritures comptables et les lignes de déclaration de TVA (CA3) seront correctement générées pour les deux aspects de la TVA.

### Détail des écritures de la facture :

![](https://support.openfire.fr/hc/article_attachments/21431736898588)

### Impression de la facture :

![](https://support.openfire.fr/hc/article_attachments/21431736900892)

# Sous-traitance et TVA en Autoliquidation

---

Depuis le 1er janvier 2014, un nouveau dispositif d'autoliquidation de TVA a été mis en place pour les contrats de sous-traitance dans le secteur du bâtiment, afin de lutter contre la fraude fiscale.

Les particularités de l'Autoliquidation sont les suivantes :

- Elle est à la fois collectée et déduite pour l'entreprise qui réalise l'achat.
- Elle dispose de lignes spécifiques pour son traitement sur la déclaration CA3.

## Principes de fonctionnement

**Pour le sous-traitant :**

- Facturation Hors Taxes (HT) avec une position fiscale exonérée.
- Mention obligatoire en bas de facture :
  - "TVA - autoliquidation, art. 283 nonies 2 pour les marchandises et/ou 283-2 pour les services"
- Déclaration de TVA CA3 mensuelle : Indication du chiffre d'affaires sous-traitant sur la ligne 5 "autres opérations non imposables".

Pour la facturation du client, il est nécessaire d'utiliser un régime fiscal exonéré. L'imputation est réalisée dans un compte de vente exonéré via la catégorie de produits.

💡Note : Il est important de configurer cette imputation pour toutes les catégories de produits concernées.

**Pour le donneur d'ordre :**

- Paiement de la facture HT.
- Déclaration de TVA CA3 mensuelle :
  - Indication du montant HT de la sous-traitance sur la ligne 2 "autres opérations imposables".
  - Déclaration de la double TVA acquittée / déductible (=opération blanche pour le donneur d'ordre)

| 🚨**Avertissement** : Déclarer les sommes sur la CA3 est obligatoire, y compris dans le contexte de l'autoliquidation avec des TVA s'annulant. |
| --- |

## Les composants de la TVA en Autoliquidation

**Dans OpenFire, les Taxes relatives à la gestion des achats en autoliquidation sont définies par défaut.**

Pour les consulter, suivez le chemin d'accès suivant :

- Facturation > Configuration > Comptabilité > Taxes.

Pour gérer la TVA en autoliquidation de manière optimale dans OpenFire, nous vous recommandons d'utiliser une taxe de type **Groupe de taxes, **comme pour la TVA intra communautaire détaillée ci-dessus.

### Les comptes d'imputation des différentes taxes du groupe

![](https://support.openfire.fr/hc/article_attachments/21431799497116)

### Les taxes du groupe

![](https://support.openfire.fr/hc/article_attachments/21431844684700)

#### TVA due autoliquidation

- Taux de -20% (taux applicable en France),
- **Type de taxe** réglé sur **Achats**,
- Compte d'imputation de la taxe : **44522000 TVA due autoliquidation**

#### TVA déd. autoliquidation

- Taux de 20% (taux applicable en France),
- **Type de taxe** réglé sur **Achats**,
- Compte d'imputation de la taxe : **44566300 TVA déductible autoliquidation**

### La taxe de type groupe "TVA Autoliquidation" :

![](https://support.openfire.fr/hc/article_attachments/21431799498012)

### La position fiscale "ACH-AL"

Une position fiscale spécifique est généralement associée à ces achats en autoliquidation pour automatiser l'application de ce groupe de taxes.

![](https://support.openfire.fr/hc/article_attachments/21431844685340)

# Usage et Bonnes Pratiques

**Bonnes pratiques :**

- Privilégié l'utilisation d'une taxe de type Groupe de Taxe pour configurer l'autoliquidation et les achats intracommunautaires.

# Pour aller plus loin

| 📓**Pour aller plus loin** → Configurer vos positions fiscales 📓**Pour aller plus loin** → Configurer vos taxes 📓**Pour aller plus loin** → Taxes spécifiques : Achats Intracommunautaires et Autoliquidation 📓**Pour aller plus loin** → Configurer la TVA sur Encaissement |
| --- |

Mis a jour le : 30/07/2025
