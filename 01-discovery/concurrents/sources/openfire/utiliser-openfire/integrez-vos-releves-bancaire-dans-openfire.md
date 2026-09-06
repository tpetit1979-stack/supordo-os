---
source: https://support.openfire.fr/hc/fr/articles/21561162891932-Int%C3%A9grez-vos-relev%C3%A9s-bancaire-dans-OpenFire
categorie: Utiliser OpenFire
titre: Intégrez vos relevés bancaire dans OpenFire
date_recuperation: 2026-09-05
---

# Intégrez vos relevés bancaire dans OpenFire

Cet article explique les **différentes méthodes pour intégrer des relevés bancaires** dans OpenFire afin de faciliter le rapprochement bancaire. Il rappelle les configurations requises au niveau des journaux et des modes de paiement et détaille les différentes procédures d'import.

Cet article contient les sections suivantes :

- Configurer vos comptes de paiement
  - Configuration des comptes par défaut
  - Surcharge par mode de paiement
- Intégrer vos relevés bancaires
  - Import via un fichier
  - Import via une connexion automatique (MyPonto)
  - Import via d'autres connexions automatiques (Paypal, Gocardless, Qonto)
  - Saisie manuelle de votre journal de banque
- Pour aller plus loin

# Intégrer vos relevés bancaires

---

Dans OpenFire Version 16, l'intégration des données bancaires peut se faire de trois manières différentes :

- La saisie manuelle de vos transactions bancaires dans le journal
- L'import d'un fichier normé de relevé bancaire, émis par votre banque
- La connexion automatique à vos comptes bancaires via notre connecteur myponto.
- La saisie manuelle de vos écritures de banque directement en comptabilité.

## Saisie manuelle de vos transactions bancaires

La saisie manuelle s'opère directement depuis le journal du tableau de bord de la comptabilité.

Pour cela, suivez le chemin d'accès : Facturation > Tableau de bord

Une fois sur le tableau de bord : Sélectionnez le journal de banque concerné > Menu « ⋮ » > Transactions

![](https://support.openfire.fr/hc/article_attachments/21575607729948)

Vous accédez alors à **l'historique des transactions** de ce compte bancaire et vous pouvez saisir manuellement de nouvelles transactions en cliquant sur **Nouveau**.

![](https://support.openfire.fr/hc/article_attachments/21575749854108)

La **séquence **est auto-générée par le système.

La **date de paiement** doit correspondre à la date de la transaction telle que figurant sur votre relevé bancaire.

Le **libellé **est celui renseigné sur le relevé bancaire.

Le **partenaire** peut-être ajouté manuellement. Il correspond au client, au fournisseur ou au collaborateur concernés par la transaction.

Le **montant **correspond au montant de la transaction. Il est négatif pour un paiement sortant (paiements fournisseurs, salaire collaborateurs, frais bancaires...). Il est positif pour un règlement entrant (règlements clients, remboursement fournisseurs...).

| 🚨**Avertissement** :   Il est recommandé de saisir de manière régulière et en respectant scrupuleusement les données de votre compte bancaire afin de ne pas générer d'écart entre les données fournies par votre banque et les données intégrées dans OpenFire.  Il est recommandé également de ne pas multiplier les méthodes d'intégration de vos données bancaires (saisie manuelle VS import de relevé) afin d'éviter les doublons de données. |
| --- |

## Import via un fichier

### Vérification de votre configuration de base

Cette méthode nécessite d'installer des modules complémentaires (OCA) en fonction du format de votre fichier bancaire.

#### Installer les modules nécessaires pour l'import des fichiers de relevés bancaires structurés

Les banques proposent des **formats **de **fichier de relevé bancaire** structurés. Selon votre banque et les formats de fichier récupérés, il vous faut installer un (ou plusieurs) des modules suivants :

- Pour un fichier de type **camt**, installez `account_statement_import_camt`.
- Pour un fichier de type **camt54**, installez `account_statement_import_camt54`.
- Pour un fichier de type **CFONB**, installez `account_statement_import_fr_cfonb`.
- Pour un fichier de type **ofx**, installez `account_statement_import_ofx`.

#### Configurer la structure d'import pour vos fichiers non standardisés

Si vous ne récupérer pas un fichier dans l’un des formats standardisés, vous pouvez passer par l'import d'un fichier personnalisés en installant le module  `account_statement_import_file`.

Il vous faudra alors configurer un modèle d'import adapté à la structure de votre fichier.

Pour cela, suivez le chemin d'accès : Facturation > Configuration > Comptabilité > Statement Sheet Mappings.

1/ Créer un **nouveau modèle d'import** et renseignez **les paramètres** du fichier dans l'en-tête du formulaire.

Détail des principaux champs :

- **Thousands Separator** (séparateur de millier)
- **Decimals Separator **(séparateur de décimales)
- **Timestamp Format** (format de date)

| Exemple de format | Rendu |
| --- | --- |
| %d/%m/%Y | 01/01/2025 |

- **Header lines skip count** (numéro des lignes d'entête de document)
- **Footer lines skip count** (numéro des lignes de pied de page)
- **Encoding** (format d'encodage)

2/ Faites correspondre l**es colonnes de votre fichier** avec les **valeurs attendues** par l'import

| 💡**Note **: Si le fichier n'a pas d'en-tête, ajoutez les noms ou les numéros de colonnes. Vous pouvez concaténer plusieurs colonnes du fichier dans le même champ, en indiquant les noms ou les numéros de colonnes séparés par une virgule. |
| --- |

Détail des principaux champs :

**Timestamp column** (date de la transaction) : champ obligatoire, qui reprend obligatoirement le format défini en entête du modèle au niveau du champ **Timestamp Format**

**Amount type : **définit le type de valeur transcrite dans le fichier. Trois valeurs sont possibles :

- Valeur simple : utiliser le montant indiqué dans la colonne Montant de votre fichier
- Valeur absolue : utiliser la même colonne pour le débit et le crédit (valeur absolue + signe)
- Colonne distincte Crédit/Débit : utiliser une colonne distincte pour le débit et le crédit

| 🚨**Avertissement** : Si vous utiliser la fonction “Amount type = Distinct Credit/debit Column”, faire un test pour s’assurer que les montants correspondent bien au debit / credit de la banque. |
| --- |

Voici un exemple de configuration :

| **🧑‍🏫Exemple** : Import d'un relevé bancaire non standardisé suivant :  ![](https://support.openfire.fr/hc/article_attachments/21573858864028)Entête du modèle d'import :  ![](https://support.openfire.fr/hc/article_attachments/21573872999964)Association des colonnes :  ![](https://support.openfire.fr/hc/article_attachments/21574005599516) |
| --- |

| 🚨**Avertissement** : Si vous utiliser la fonction “Amount type” = Distinct Credit/debit Column”, faire un test pour s’assurer que les montants correspondent bien au debit / credit de la banque. |
| --- |

#### Vérification de la configuration de votre journal de banque

La **provenance des relevés bancaires **du journal de banque concerné doit être à **Importer**

![](https://support.openfire.fr/hc/article_attachments/21573365820828)

Il est possible de définir par défaut dans le journal de la banque le modèle d'import :

![](https://support.openfire.fr/hc/article_attachments/21573308946076)

### Import du fichier

Suivez le chemin d'accès suivant : `Facturation > Tableau de bord`.

Sélectionnez le **journal de banque** correspond à votre relevé, et cliquez sur le bouton **Import de relevé (OCA)**.

![](https://support.openfire.fr/hc/article_attachments/21573301247644)

Vous pouvez ensuite **Charger votre fichier**.

![](https://support.openfire.fr/hc/article_attachments/21573301248796)

| 💡**Note **: pour un fichier non standard, choisissez le modèle d'import configuré précédemment. |
| --- |

Cliquez ensuite sur :

**Importer et visualiser**

![](https://support.openfire.fr/hc/article_attachments/21573365823004)

ou **Importer et commencer le rapprochement**.

![](https://support.openfire.fr/hc/article_attachments/21573301250716)

| 📓**Pour aller plus loin** → Comment effectuer un rapprochement bancaire ? |
| --- |

## Import via une connexion automatique (MyPonto)

MyPonto est un agrégateur de banque qui permet de gérer l'ensemble de vos comptes bancaires professionnels depuis une seule plateforme. Cette méthode nécessite l'ouverture d'un compte payant MyPonto.

### Créer une intégration sur MyPonto :

- Accédez au tableau de bord MyPonto.
- Créez une intégration pour obtenir votre **Client ID** et **Client Secret**.

![](https://support.openfire.fr/hc/article_attachments/21573365824540)

| 💡**Note **: Pour la configuration sur votre espace MyPonto, rapprochez vous de votre chef de projet OpenFire |
| --- |

### Vérifier votre configuration OpenFire

**Installer le module OCA :**

- Installez le module  `Online Bank Statements: MyPonto.com (account_statement_import_online_ponto)`

**Configurer la connexion sur OpenFire :** Suivez le chemin d'accès suivant : `Facturation > Configuration > Banques > Online Bank Statement Providers`.

- Créez une nouvelle entrée.
- **Journal :** Sélectionnez le journal de banque concerné.
- **Service :** Choisissez `MyPonto.com`.
- **Schedule update interval :** Définissez la fréquence d'importation automatique.
- **Login :** Renseignez le **Client ID** de MyPonto.
- **Secret Key :** Renseignez le **Client Secret** de MyPonto.
- Cliquez sur le bouton **PULL ONLINE BANK STATEMENT** pour lancer un import manuel.
- **Ponto Date Field** : Date à laquelle sera enregistré la date de la ligne du relevé bancaire

![](https://support.openfire.fr/hc/article_attachments/21573301253020)

### Importer vos données bancaires

[documentation à venir]

Les relevés bancaires vont alors s'intégrer automatiquement en fonction de la configuration ci-dessus.

Au niveau du  tableau de bord de la comptabilité, on constate que la connexion est faite. Vous avez la possibilité d’aller lettrer votre relevé bancaire avec vos écritures comptables

![](https://support.openfire.fr/hc/article_attachments/21573301256092)

L'interface de rapprochement se présente comme suivant :

![](https://support.openfire.fr/hc/article_attachments/21573365830684)

## Import via d'autres connexions automatiques

Sur le même principe que MyPonto, d'autres fournisseurs peuvent être intégrés pour une connexion automatique.

Voici les fournisseurs disponibles :

| Fournisseurs | Module à installer |
| --- | --- |
| GoCardless | account_statement_import_online_gocardless |
| Paypal | account_statement_import_online_paypal |
| Qonto | account_statement_import_online_qonto |

N'hésitez pas à vous rapprocher de votre chef de projet OpenFire pour ajouter ces fournisseurs.

## Saisie manuelle de votre journal de banque

La saisie manuelle de votre journal de banque se fait via la saisie d'une pièce comptable directement depuis votre journal de banque.

Chemin d'accès : Facturation > Comptabilité > Journaux > Pièces comptables

- Créez une nouvelle pièce
- Saisissez la référence de votre pièce (par exemple : Relevé bancaire du JJMMAAA)
- Ajustez la date comptable de la pièce (par défaut la date de création de la pièce)
- Sélectionnez le journal de banque concerné
- Saisissez vos écritures comptables

![](https://support.openfire.fr/hc/article_attachments/21573365832220)

| 🚨**Avertissement** : il n'existe pas à date de méthode de rapprochement bancaire si vous saisissez directement votre relevé bancaire dans le journal de banque. Une option pourrait être d'utiliser les fonctions de lettrages classiques dans une pareille situation. N'hésitez pas à vous rapprocher de votre chef de projet OpenFire. |
| --- |

# Pour aller plus loin

---

| 📓**Pour aller plus loin** → Comment effectuer un rapprochement bancaire ? 📓**Pour aller plus loin** → [Configurez vos modes de paiement manuels](https://support.openfire.fr/hc/fr/articles/19096228298012) |
| --- |

Mis a jour le : 07/08/2025
