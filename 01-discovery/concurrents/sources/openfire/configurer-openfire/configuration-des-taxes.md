---
source: https://support.openfire.fr/hc/fr/articles/21429167750940-Configuration-des-Taxes
categorie: Configurer OpenFire
titre: Configuration des Taxes
date_recuperation: 2026-09-05
---

# Configuration des Taxes

Cet article vous guidera à travers la configuration des taxes dans OpenFire, vous permettant d'assurer une imputation comptable correcte et une gestion efficace de la TVA.

Vous apprendrez à créer de nouvelles taxes et à définir leurs comportements.

**Cet article contient les sections suivantes :**

- Présentation des Taxes
- Création et Configuration des Taxes
- Le cas particulier des Taxes de type "Groupe de Taxes"
- Configuration des Taxes par défaut
- Usage et Bonnes Pratiques
- Pour Aller plus loin

# Présentation des Taxes

---

Les taxes dans OpenFire sont essentielles pour configurer les paramètres et les règles d'imputation comptable dans le cadre d'un régime de TVA, notamment :

- L'imputation des comptes comptables de taxes par taux de TVA.
- L'imputation des comptes comptables de produit et de charge par taux de TVA.

**Dans OpenFire, les taxes sont définies par défaut.**

| 💡**Note **: Il est essentiel de bien vérifier cette imputation au préalable pour assurer l'exactitude de votre comptabilité. |
| --- |

Pour consulter la liste de vos taxes, suivre le chemin d'accès suivant :

- Facturation > Configuration > Comptabilité > Taxes.

Taxes de ventes par défaut :

![](https://support.openfire.fr/hc/article_attachments/21430942559644)

Taxes d'achat par défaut :

![](https://support.openfire.fr/hc/article_attachments/21430970598428)

# Création et Configuration des Taxes

---

Pour ajouter une nouvelle taxe, cliquez sur **Nouveau**. Pour éditer une taxe existante, cliquez sur celle-ci.

## Informations Générales de la taxe

Vous devrez saisir les informations suivantes :

**Nom de la taxe** : C'est le libellé de la taxe, pour une utilisation interne uniquement.

**Type de taxe** : Détermine l'usage de la taxe, à savoir : Achat (facture fournisseur), Vente (facture client) ou Aucun

| 💡**Note **: **Aucun** signifie que la taxe ne peut pas être utilisée seule, mais elle peut être incluse dans un groupe de taxes |
| --- |

**Calcul de la taxe** : Plusieurs choix sont possibles :

- **Groupe de taxe** La taxe est un ensemble de plusieurs taxes.

| 📓**Pour aller plus loin** → Voir la section "Les groupes de taxes" ci-après dans cet article |
| --- |

- **Fixe** : Un montant fixe en euros.
- **Pourcentage du prix** : Le taux saisi sera appliqué sur le prix hors taxes (HT).
- **Pourcentage du prix taxe incluse** : Le taux saisi est considéré comme inclus dans le prix toutes taxes comprises (TTC).

| 🧑‍🏫Exemple :  **Pourcentage du prix **: Si vous vendez un appareil à 2500 € avec une TVA de 20%, la TVA sera de 500 € (20% x 2500) et le prix TTC sera de 3000 € (2500 + 500). **Pourcentage du prix taxe incluse** : Si vous vendez le même appareil à 2500 € (TTC), la TVA sera de 417 € (2500 / (1+20%)) et le prix HT sera de 2083 € (2500 - 417). |
| --- |

**Portée de la taxe** : Permet de restreindre l'utilisation des taxes aux produits ou aux services. Laissez ce champ vide pour ne pas appliquer de restrictions.

**Active** : Si cette case est décochée, la taxe ne sera plus utilisable.

**Montant** : Montant de la taxe, exprimé en pourcentage ou en euros, selon la méthode de calcul de la taxe retenue

Exemple d'une configuration type pour une TVA collectée 5,5% :

![](https://support.openfire.fr/hc/article_attachments/21430139527836)

## Informations de l'onglet "Définition" de la Taxe

Cet onglet est divisé en deux blocs :

- Un premier bloc concernant le **calcul des taxes** relatives aux **factures**
- Un second bloc pour le **calcul des taxes** relatives aux **avoirs**.

La configuration de ces deux blocs permet d'**automatiser la création de la pièce comptable** dans le journal de vente ou d'achat concerné.

- **La première ligne** de chaque bloc **permet de définir la** ***Base***** **(= l'assiette) de la taxe, correspondant au montant hors taxe de la ligne de facture.
- La ou **les lignes suivantes** permettent d'**éclater le montant de la taxe en différents comptes** de taxes associés.

Pour chacune de ces lignes, vous pouvez renseigner la ou les grilles de taxe correspondant à votre rapport des taxes.

Exemple d'une configuration type pour une TVA collectée 5,5% :

![](https://support.openfire.fr/hc/article_attachments/21430123329436)

## Informations de l'onglet "Options Avancées" de la Taxe

**Étiquettes sur les factures** : C'est le nom de la taxe tel qu'il apparaît dans la colonne **TVA **des commandes et des factures imprimées.

**Groupe de taxe** : Permet de rattacher la taxe à un groupe de taxes existant. L'utilisation d'un groupe de taxe est utile pour homogénéiser l'impression des informations de taxes sur la factures lorsque plusieurs taxes d'un même montant sont présents dans la facture. C'est notamment le cas lorsque des taxes dissociées pour les biens et les services sont présentes dans le devis. Il est repris en dessous du Montant HT de la facture sur les factures imprimées.

![](https://support.openfire.fr/hc/article_attachments/21431114212380)

**Inclure dans le coût analytique** : Si activé, le montant calculé par cette taxe sera assigné au même compte analytique que la ligne de facture (si présent).

**Société** : Société à laquelle la taxe est associée.

**Pays** : Pays auquel la taxe est associée.

**Inclus dans le prix** : Cochez cette case si le prix que vous utilisez pour l'article et les factures inclut cette taxe.

**Impacte la base des taxes ultérieures** : Si activé, le total TTC devient la base de calcul des taxes appliquées au même produit et ayant une séquence supérieure, à condition qu'elles l'acceptent (l'option "Assiette affectée par les impôts antérieurs" doit être cochée sur ces taxes.)

**Exigibilité fiscale** : Vous avez deux options :

- **Basé sur la facture** : La taxe est due dès la validation de la facture.
- **Basé sur le paiement** : La taxe est due dès la réception du paiement de la facture. Pour une configuration détaillée, consultez l'article "Configurer la TVA sur encaissement".

Exemple d'une configuration type pour une TVA collectée 5,5% :

![](https://support.openfire.fr/hc/article_attachments/21430139528220)

## Informations de l'onglet "Affectation des Comptes" de la Taxe

Cet onglet permet de ventiler les comptes de référence définis au niveau des produits ou des catégories de produit (souvent le compte comptable de produit ou de charge hors taxes) vers les différents comptes comptables associés à la Taxe en question.

Exemple d'une configuration type pour une TVA collectée 5,5% :

![](https://support.openfire.fr/hc/article_attachments/21430139528732)

| 🧑‍🏫Exemple : Dans cet exemple, le ***compte de l'article*** correspond au ***compte de revenus*** défini dans la fiche du produit vendu, ou à défaut dans sa catégorie. Si je vends une chaudière à granulés dont le ***compte de revenus*** de référence est le ***707000 Marchandises HT***, alors OpenFire remplacera ce compte par le*** compte de revenus ***(à utiliser à la place) ***707050 Marchandises 5,5%*** chaque fois que ce produit sera vendu à la TVA collectée 5,5%. |
| --- |

## Le cas particulier des Taxes de type "Groupe de Taxes"

Dans OpenFire, une taxe de type "Groupe de taxes" est une Taxe qui en regroupe plusieurs pour former un ensemble cohérent.

### Avantages des Groupes de Taxes

Utiliser les groupes de taxes présente plusieurs avantages significatifs :

- **Simplification** : Appliquez un ensemble complexe de taxes en une seule sélection, plutôt que de choisir chaque taxe individuellement.
- **Cohérence** : Assurez-vous que toutes les taxes requises pour une situation donnée sont toujours appliquées ensemble, réduisant les erreurs.
- **Visibilité** : Le calcul détaillé de chaque taxe composante reste visible sur les documents (factures, devis), offrant une transparence totale.
- **Adaptabilité** : Idéal pour les cas où plusieurs types de taxes s'appliquent simultanément (ex. : TVA et éco participation, ou TVA due et TVA déductible pour les opérations spécifiques).

### Créer un Groupe de Taxes

Pour créer ou modifier un groupe de taxes :

1. Suivre le chemin d'accès suivant : Facturation > Configuration > Comptabilité > Taxes.
2. Cliquez sur **Nouveau** pour créer une nouvelle taxe, ou éditez une taxe existante qui n'est pas déjà un groupe.
3. Dans le champ **Calcul de la taxe**, sélectionnez **Groupe de taxe**.
4. Dans l'onglet **Définition**, vous pourrez ajouter les différentes taxes qui composeront ce groupe.
  - Pour chaque ligne, sélectionnez une **Taxe** existante que vous avez configurée individuellement au préalable.
  - La colonne **Montant** dans cet onglet ne sera pas modifiable, car le montant total du groupe de taxes sera la somme des montants calculés de toutes les taxes qui le composent.
  - Les **Grilles de taxe** doivent être correctement configurées pour chaque taxe composante afin que les montants apparaissent précisément dans vos rapports fiscaux (ex: déclaration de TVA).

### Exemple de Groupe de Taxes

#### TVA + Eco-participation

Vous pouvez créer un groupe de taxes nommé "**TVA 20% + Éco-Participation**".

Ce groupe inclut :

- Une taxe "TVA 20%" configurée avec un calcul en pourcentage.
- Une taxe "Éco-Participation" configurée avec un calcul fixe (par exemple, 0,50 €).

Lorsque vous appliquez ce groupe à une ligne de produit dans une facture, OpenFire calcule automatiquement pour la ligne la TVA collectée à 20% ainsi que le montant de l'éco-participation, les additionnant au prix pour obtenir le total TTC.

#### TVA Intra-communautaire

Pour la **TVA intracommunautaire**, vous pouvez créer un groupe de taxes "TVA Intracommunautaire" incluant une taxe "TVA Due Intracom." et une taxe "TVA Déductible Intracom.". Ce groupe permet de gérer les deux aspects de la TVA intracommunautaire en une seule sélection.

| 📓**Pour aller plus loin** → TVA autoliquidée et TVA intra-communautaire (localisation fiscale française) |
| --- |

# Configuration des Taxes par défaut

---

OpenFire permet de définir des Taxes à appliquer par défaut à la création d'un nouveau produit.

Ces taxes sont identifiées dans les paramètres généraux de la facturation :

- Facturation > Configuration > Taxes > Taxes par défaut

![](https://support.openfire.fr/hc/article_attachments/21430139529372)

## Les TVA de base (vente) et TVA de base (achat)

Ces deux taxes sont **utilisées **dans la configuration** par défaut** de votre base **OpenFire**, afin de simplifier la gestion de l'affectation des taxes par produit, lorsque ces produits peuvent être achetés ou vendus à différents taux de TVA.

| 🧑‍🏫Exemple : un poêle à bois ou à granulés peut être vendu à 5,5% ou à 20% de TVA, selon le contexte de l'installation (client professionnel ou particulier, maison neuve ou rénovation) |
| --- |

Ces taxes** **sont utilisées par défaut pour chaque nouveau produit créé dans votre base, permettant ainsi de neutraliser la gestion de la taxe pour chaque article.

**Le régime de TVA à appliquer à une vente ou à un achat** est ainsi piloté par la **position fiscale** uniquement.

| 💡**Note **: pour votre activité, si une même taxe est systématiquement appliquée à l'ensemble de vos produits et services, vous pouvez définir cette taxe comme taxe par défaut, en lieu et place des TVA de base présentées ci-dessus. C'est notamment le cas si toutes vos prestations sont vendues en TVA collectée 20%. |
| --- |

## La TVA de base Acompte (vente)

La **TVA de base Acompte (vente) **est utilisée dans la configuration** par défaut** de votre base **OpenFire. **

Elle est associée au produit Acompte, et permet de décliner le calcul de la taxe associée au produit Acompte selon le régime de TVA de votre facture.

| 🚨**Avertissement** : il est déconseillé de modifier la configuration de votre article Acompte. En cas de doute, n'hésitez pas à vous rapprocher de votre équipe support OpenFire. |
| --- |

## Configurer un Produit avec taux de TVA fixe

Si un produit (ou un service) est toujours acheté ou vendu au même taux de TVA, vous pouvez forcer la taxe concernée directement dans l'onglet **Vente** de la fiche du produit.

![](https://support.openfire.fr/hc/article_attachments/21431252017436)

# Usage et Bonnes Pratiques

---

Lors de la création et validation d'une facture, les taxes s'appliquent automatiquement selon votre configuration.

**Bonnes pratiques :**

- Vérifiez systématiquement l'imputation des comptes comptables de taxes et de produit/charge pour chaque taux de TVA configuré, surtout dans les phases de démarrage de votre activité sous OpenFire.

# Pour aller plus loin

---

| 📓**Pour aller plus loin** → Configurer vos positions fiscales 📓**Pour aller plus loin** → Taxes spécifiques : Achats Intracommunautaires et Autoliquidation 📓**Pour aller plus loin** → Configurer la TVA sur Encaissement |
| --- |

Mis a jour le : 30/07/2025
