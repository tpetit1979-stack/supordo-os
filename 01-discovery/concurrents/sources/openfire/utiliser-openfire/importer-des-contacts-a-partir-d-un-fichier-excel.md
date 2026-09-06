---
source: https://support.openfire.fr/hc/fr/articles/29873444685724-Importer-des-contacts-%C3%A0-partir-d-un-fichier-Excel
categorie: Utiliser OpenFire
titre: Importer des contacts à partir d'un fichier Excel
date_recuperation: 2026-09-05
---

# Importer des contacts à partir d'un fichier Excel

Dans cet article, nous vous expliquons comment importer un fichier Excel de contacts dans OpenFire.

| 🧩**Prérequis** →   [Créer un contact](https://support.openfire.fr/hc/fr/articles/19072931003420) |
| --- |

  🚨Avertissement : Les imports à partir d'un fichier Excel doivent être faits avec OpenImport, qui permet de conserver l'historique du fichier Excel utilisé et d'apporter des correctifs éventuels.

Vous pouvez importer des contacts en lot à partir d'un fichier Excel grâce à la fonctionnalité "**OpenImport**". Pour cela, il est nécessaire d'avoir un compte permettant d'accéder aux Paramètres de votre base OpenFire.

**Chemin d’accès : **

*Paramètres > OpenImport > Nouveau*

Le fichier Excel utilisé doit respecter la [matrice d'import suivante](https://docs.google.com/spreadsheets/d/1-GwNW-Z82bhsVQsR9Cr1w12doqubPujK/export?format=xlsx).

Choisissez le type d'import **Partenaire**

![](https://support.openfire.fr/hc/article_attachments/29873444678300)

D'autres champs non présents dans la matrice sont disponibles. Vous pouvez accéder à la totalité des champs éligibles à l'import pour les contacts en bas de votre page OpenImport:

![](https://support.openfire.fr/hc/article_attachments/29873444679708)

**Points de vigilance:**

- la colonne **name **doit toujours être remplie
- la colonne **ref** de votre fichier Excel doit être de type texte (et non pas nombre)

**Pour importer un contact de type société, les colonnes spécifiques à renseigner sont:**

- **type: **contact
- **name (colonne obligatoire): **le nom de la société
- **of_company_name: **le nom de la société
- **company_type: **"company"
- **is_customer: **0
- **is_company: **1

Commencez toujours par **"Simuler l'import". **Les éventuelles erreurs ou alertes s'affichent. Une fois que tout est corrigé, cliquez sur **"Import"**

**![](https://support.openfire.fr/hc/article_attachments/29873444681884)**

L'historique de vos imports est accessible depuis la vue liste.

![](https://support.openfire.fr/hc/article_attachments/29873444682780)

Mis a jour le : 27/08/2026
