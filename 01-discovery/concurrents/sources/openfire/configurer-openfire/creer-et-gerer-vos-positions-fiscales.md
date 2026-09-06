---
source: https://support.openfire.fr/hc/fr/articles/21514064474268-Cr%C3%A9er-et-g%C3%A9rer-vos-positions-fiscales
categorie: Configurer OpenFire
titre: Créer et gérer vos positions fiscales
date_recuperation: 2026-09-05
---

# Créer et gérer vos positions fiscales

Cet article vous guidera dans la création et la configuration des **positions fiscales** d'OpenFire. Ces règles comptables avancées vous permettent d'automatiser l'application des taxes et des comptes, en fonction de la situation de vos clients et fournisseurs, pour vos transactions.

| 🧩**Prérequis** → avoir lu l'article [**Introduction aux règles d’automatisation comptables dans OpenFire**](https://support.openfire.fr/hc/fr/articles/21515062307228) |
| --- |

**Cet article contient les sections suivantes :**

- Qu'est-ce qu'une position fiscale ?
- Créer ou modifier une position fiscale
  - Informations principales
  - Correspondance des taxes et des comptes
  - Détection automatique des positions fiscales
  - Affectation manuelle des positions fiscales
- Bonnes pratiques
- Pour aller plus loin

# Qu'est-ce qu'une position fiscale ?

---

Les positions fiscales sont des règles qui permettent d'ajuster automatiquement les taxes et les comptes d'une transaction de ventes ou d'achat. Elles sont utiles lorsque vous devez appliquer des règles de taxation différentes de celles par défaut, par exemple, en fonction du type de transaction, de la localisation géographique ou de l'activité de votre client.

Pour consulter la liste des positions fiscales disponibles, suivez le chemin d'accès suivant : `Facturation > Configuration > Comptabilité > Position fiscale`

| 💡**Note **: OpenFire propose une liste de positions fiscales par défaut, basée sur votre localisation et les informations fournies lors de la création de votre compte. |
| --- |

Voici les principales ***positions fiscales ***proposées par défaut :

| **Position fiscale ** | **Commentaires** | Type |
| --- | --- | --- |
| VEN-EXO | Ventes exonérées | Standard OpenFire |
| VEN-5.5 | Ventes 5,5% | Standard OpenFire |
| VEN-10.0 | Ventes 10,0% | Standard OpenFire |
| VEN-20.0 | Ventes 20,0% | Standard OpenFire |
| VEN-20.0 E | Ventes 20,0% à l'emporter | Optionnelle OpenFire |
| VEN-AL | Ventes autoliquidation | Standard OpenFire |
| ACH-5.5 | Achats 5,5% | Standard OpenFire |
| ACH-10.0 | Achats 10,0% | Standard OpenFire |
| ACH-20.0 | Achats 20,0% | Standard OpenFire |
| ACH-IMMO-5.5 | Achats immobilisations 5,5% | Optionnelle OpenFire |
| ACH-IMMO-10.0 | Achats immobilisations 10,0% | Optionnelle OpenFire |
| ACH-IMMO-20.0 | Achats immobilisations 20,0% | Standard OpenFire |
| ACH-UE | Achats intracommunautaires 20,0% | Standard OpenFire |
| ACH-AL | Achats autoliquidation | Standard OpenFire |

# Créer ou modifier une position fiscale

---

Depuis la liste des positions fiscales, ajoutez en une nouvelle en cliquant sur “Nouveau” ou éditez en une existante en cliquant dessus.

## Informations principales

**Position fiscale** : c'est le nom de la position fiscale. Il est recommandé de lui donner un nom explicite qui correspond à la taxe appliquée.

## Correspondance des taxes et des comptes

Pour chaque position fiscale, il vous faut définir les règles d'application des taxes.

- **Taxe par défaut** : si aucune règle de correspondance n'est trouvée, cette taxe sera appliquée.
- **Correspondance des taxes** : cette section permet de faire le lien entre la taxe par défaut du produit et la nouvelle taxe qui sera appliquée dans le contexte de cette position fiscale.

![](https://support.openfire.fr/hc/article_attachments/21526888284700)

| 🧑‍🏫Exemple : dans un devis, si vous sélectionnez la position fiscale **TVA 5,5%**, tous les articles ayant la **TVA de base (vente)** comme taxe par défaut se verront appliquer la **TVA 5,5% (vente)**. |
| --- |

**Correspondance des comptes** : cette table doit généralement rester vide, car l'affectation des comptes est gérée directement au niveau de la taxe elle-même.

## Détection automatique des positions fiscales

Il est possible de définir des règles d'affectation automatique d'une position fiscale à un partenaire ou à une transaction.

![](https://support.openfire.fr/hc/article_attachments/21528060903452)

- **Détecter automatiquement** : cochez cette case si vous souhaitez qu'OpenFire applique automatiquement cette position fiscale lors d'une commande ou d'une facture lorsque les conditions définies (pays, groupe de pays) sont remplies par le partenaire.
- **TVA requise** : cette option s'applique uniquement si votre partenaire dispose d'un numéro de TVA intracommunautaire, qui devra être renseigné sur sa fiche.
- **Numéro d'identification fiscal étranger** : ce champ est facultatif si votre activité est limitée à la France. Il est utilisé si vous opérez dans d'autres zones géographiques.
- **Groupe de pays / Pays** : ces champs sont utilisés pour définir à quel partenaire (selon son adresse de livraison) cette position fiscale s'applique. Si vous sélectionnez un pays, vous pouvez affiner votre choix en sélectionnant une ou plusieurs régions, où bien en affinant par intervalles de code postaux.

![](https://support.openfire.fr/hc/article_attachments/21526885242268)

## Affectation manuelle des positions fiscales

Il est possible de définir manuellement une position fiscale.

### **Au niveau du partenaire**

il est possible de forcer l'utilisation d'une position fiscale pour un type de partenaire. C'est notamment recommandé pour vos fournisseurs pour qui le régime fiscale ne varie jamais (Exemple : achat 20% ou Achat Intra communautaire).

Cette position fiscale est définie au niveau de la rubrique Information Fiscale de l'onglet Ventes & Achats de la fiche partenaire :

![](https://support.openfire.fr/hc/article_attachments/21528073265820)

### **Dans une commande ou une facture**

Sélectionnez manuellement la position fiscale avant d’ajouter vos lignes de produits.

### **Dans un modèle de devis**

Définissez une position fiscale par défaut à utiliser dans le contexte du modèle. Si défini, la position fiscale est reprise dans chaque commande ou facture utilisant le modèle.

| 🚨**Avertissement** : dans une commande ou une facture client, **la position fiscale du modèle prévaudra la plupart du temps sur la position fiscale du partenaire **car la sélection du modèle d'intervention intervient généralement après la sélection du partenaire. Pour contourner cette situation, nous vous recommandons de décliner vos modèles de devis par typologie de client. |
| --- |

# Bonnes pratiques

---

- Donnez des noms clairs et explicites à vos positions fiscales pour les identifier facilement (ex : **VEN-AL**, pour **Ventes autoliquidation**).
- Testez toujours vos positions fiscales sur une transaction (devis, commande, facture) avant de les utiliser en production.

# Pour aller plus loin

---

| 📓Pour aller plus loin → Configurer vos taxes 📓Pour aller plus loin → Configurer vos positions fiscales 📓Pour aller plus loin → Configurer vos prix en HT (B2B) ou en TTC (B2C) 📓Pour aller plus loin → Configurez vos acomptes |
| --- |

Mis a jour le : 04/08/2025
