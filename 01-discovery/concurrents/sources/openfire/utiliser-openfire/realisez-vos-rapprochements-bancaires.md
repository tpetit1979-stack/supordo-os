---
source: https://support.openfire.fr/hc/fr/articles/21560286477340-R%C3%A9alisez-vos-rapprochements-bancaires
categorie: Utiliser OpenFire
titre: Réalisez vos rapprochements bancaires
date_recuperation: 2026-09-05
---

# Réalisez vos rapprochements bancaires

Le rapprochement bancaire est le processus qui consiste à associer les lignes d'un **relevé bancaire** à des **écritures comptables** (factures, paiements, etc.) déjà enregistrées dans OpenFire.

Cet article vous guide pas à pas pour effectuer un **rapprochement bancaire** en utilisant l'interface de rapprochement OpenFire. Vous apprendrez à relier les lignes de transaction de vos relevés bancaires aux écritures comptables correspondantes. Cette procédure permet de s'assurer que vos registres internes correspondent aux transactions de votre banque.

| 🧩**Prérequis** →  [Configurez vos modes de paiement manuels](https://support.openfire.fr/hc/fr/articles/19096228298012) 🧩**Prérequis** →  Configurer vos rapprochements bancaires 🧩**Prérequis** →  [Consultez vos transactions bancaires](https://support.openfire.fr/hc/fr/articles/21602920721180) 🧩**Prérequis** →  [Comment intégrer vos relevés bancaire dans OpenFire ?](https://support.openfire.fr/hc/fr/articles/21561162891932) |
| --- |

Cet article contient les sections suivantes :

- Rapprochement manuel
  - Structure de l'interface de rapprochement
  - Etapes de rapprochement
- Pour aller plus loin

| 🚨**Avertissement** : la méthode de rapprochement bancaire détaillée ci-dessous est réservée aux utilisateurs produisant leur comptabilité sous OpenFire. Elle est incompatible avec la fonction de remise en banque simplifiée. |
| --- |

# Rapprochement manuel

Suivez le chemin d'accès suivant :

`Facturation > Tableau de bord > Choisir un journal de banque > Lettrer X articles`.

![](https://support.openfire.fr/hc/article_attachments/21575644477468)

Les points du graphiques de chaque vignette de journal de banque correspondent à l'évolution du solde de votre compte bancaire.

| 💡**Note **: Vous pouvez accéder directement à l'interface de rapprochement en passant par la vue kanban de la liste des transactions du compte bancaire à rapprocher :  ![](https://support.openfire.fr/hc/article_attachments/21576498718364) |
| --- |

## Structure de l'interface de rapprochement

L'interface de rapprochement est composée de 3 zones distinctes :

![Schéma des flux comptables OF16 - Cadre 2.jpg](https://support.openfire.fr/hc/article_attachments/21586390033052)

### Zone 1 - Les transactions du relevé bancaire à rapprocher

Cette section affiche la liste des transactions qui ont été saisies manuellement (ou importées via un relevé) dans votre journal de banque. Le filtre par défaut "**Non lettré**" permet de ne conserver dans cette liste que les transactions non encore rapprochées.

Ces lignes sont les mouvements d'argent bruts de votre compte bancaire. Chaque ligne contient les informations suivantes :

| ![](https://support.openfire.fr/hc/article_attachments/21576498720156) | Description des champs :  La **date **de la transaction. **Le libellé** de l'opération, tel qu'il apparaît sur le relevé. **Le partenaire **associé si celui-ci a été renseigné au moment de l'intégration du relevé. La saisie du partenaire peut s'avérer importante car OpenFire tentera de reconnaître le partenaire (client ou fournisseur) associé à la transaction pour faire des suggestion de réconciliation. Le **montant **de la transaction. Le **balance globale** des transactions présentes. |
| --- | --- |

### Zone 2 - Les écritures comptables à rapprocher

Cette partie de l'écran affiche les écritures comptables non soldées dans votre base de données, telles que les factures clients impayées, les factures fournisseurs à régler, ou les paiements enregistrés en attente de rapprochement.

| 💡**Note **: vous pouvez utiliser la barre de recherche pour rechercher parmi toutes vos écritures celles qui correspondent à votre opération. Les critères de recherche pertinents sont notamment :   Le partenaire Le compte comptable Le montant |
| --- |

![](https://support.openfire.fr/hc/article_attachments/21586607960092)

| 💡**Note **: les écritures présentes dans cette partie répondent aux critères suivants :   Les écritures comptables dont la pièce est comptabilisée. Les écritures sur un compte configuré comme "lettrable" Les écritures dont le montant résiduel (montant non lettré) est différent de 0. |
| --- |

### Zone 3 - Synthèse et actions liées au rapprochement

On retrouve dans cette zone la transaction et la (ou les) écritures comptables à rapprocher sélectionnées. En gras la transaction à rapprocher, et en dessous les écritures comptables associées.

![](https://support.openfire.fr/hc/article_attachments/21586604621084)

Les actions disponibles sont les suivantes :

**Voir la pièce** : vous permet de consulter la pièce comptable associée à la transaction en cours de rapprochement

**A vérifier **: permet de marquer la transaction comme **à vérifier **lorsque l'utilisateur n'est pas certains de toutes les contreparties du rapprochement.

- Si la transaction n'est pas déjà associée à une écriture comptable => OpenFire marque simplement la transaction **à vérifier.**
- Dans le cas contraire, OpenFire marque la transaction comme **à vérifier** et la rapproche (lettre) de son écriture. Un filtre vous permet alors de retrouver les transactions A vérifier :

![](https://support.openfire.fr/hc/article_attachments/21586787217052)

**Réinitialiser le rapprochement : **vous permet de repartir de la situation initiale pour votre opération de rapprochement en cours.

**Valider : **permet de valider le rapprochement (lettrage).

**Délettrer **: permet de délettrer la transaction.

![](https://support.openfire.fr/hc/article_attachments/21586817277596)

## Etapes de rapprochement

Pour réaliser votre rapprochement bancaire, suivez les étapes suivantes :

### Etape 1 / Sélectionnez votre transaction à rapprocher

Pour sélectionner une transaction à rapprocher, il vous suffit de cliquer dessus. Elle apparaitra alors en encadré violet en partie gauche, et sera reprise dans la zone de rapprochement (la zone 3).

![](https://support.openfire.fr/hc/article_attachments/21586604619036)

### Etape 2 / Sélectionnez votre ou vos écritures à rapprocher

Pour sélectionner une écriture à rapprocher de la transaction bancaire, il vous suffit de cliquer dessus. Elle apparaitra alors en surbrillance violette, et sera reprise dans la zone de rapprochement (la zone 3), en dessous de la transaction en gras.

![](https://support.openfire.fr/hc/article_attachments/21587511789212)

### Etape 3 / Validez votre rapprochement

Pour valider votre rapprochement, cliquez simplement sur **Valider.**

En cas de rapprochement avec écart, vous pouvez utiliser des modèles de rapprochement afin d'automatiser les règles de contrepartie.

# Pour aller plus loin

---

| 📓**Pour aller plus loin** → Utilisez les modèles de rapprochement bancaire automatiques |
| --- |

Mis a jour le : 07/08/2025
