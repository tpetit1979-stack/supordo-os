---
source: https://support.openfire.fr/hc/fr/articles/29506298259228-Configurer-les-r%C3%A8gles-d-import-de-facture-sur-la-fiche-fournisseur
categorie: Configurer OpenFire
titre: Configurer les règles d'import de facture sur la fiche fournisseur
date_recuperation: 2026-09-05
---

# Configurer les règles d'import de facture sur la fiche fournisseur

Cet article explique comment paramétrer la fiche d'un fournisseur dans OpenFire afin d'automatiser et de simplifier l'importation de ses factures électroniques. Vous découvrirez les étapes de configuration ainsi que le fonctionnement des règles de correspondance d'articles et de taxes.

Cet article contient les sections suivantes :

- [Chemin d'accès à la fiche fournisseur](#h_01KZPC4X1RHTAE90G1QQZQVTHB)
- [Règles de reconnaissance des articles à l'import](#h_01KZPC4X1T885RCT7QEPGHN6YB)
- [Étapes pour configurer les paramètres d'import par défaut](#h_01KZPC4X1ZKG6056JZK169YF68)
- [Description des champs de configuration](#h_01KZPC4X23WWC2Y7GJZ1DZFJW3)
- [Règles d'application automatique des taxes](#h_01KZPC4X2BRK7W5SDXVSN3ERGP)
- [Bonnes pratiques](#h_01KZPC4X2ER75320YZFSRMHWR6)

## Chemin d'accès à la fiche fournisseur

Suivre le chemin d'accès suivant : `Contacts > Contacts > sélectionner un fournisseur > onglet Facturation`.

## Règles de reconnaissance des articles à l'import

Lorsqu'une facture électronique est reçue, OpenFire analyse le fichier structuré (XML) pour associer automatiquement chaque ligne à un article de votre base de données selon la logique prioritaire suivante :

1. **Recherche par code article ou code-barres :** OpenFire recherche un article existant dont la référence interne correspond au code présent dans la facture.
2. **Recherche dans les références fournisseur :** Si l'article n'est pas trouvé, le système vérifie si ce code fournisseur est associé à un article dans vos tables de prix d'achat et sélectionne le premier correspondant.
3. **Application du produit par défaut :** À défaut, le système applique le produit par défaut configuré sur la fiche du fournisseur.
4. **Création d'une ligne sans article :** Si aucune règle ne correspond, la ligne est créée sans article en reprenant le compte de charge et la taxe par défaut définis sur le fournisseur.

## Étapes pour configurer les paramètres d'import par défaut

1. Suivre le chemin d'accès suivant : `Contacts > Contacts`.
2. Cliquer sur le fournisseur concerné pour ouvrir sa fiche.
3. Cliquer sur l'onglet **Facturation**.
4. Descendre jusqu'à la section **Import des factures fournisseur**.
5. Renseigner les champs de configuration selon vos besoins.
6. Cliquer sur le bouton **Enregistrer**.

## Description des champs de configuration

Les champs de la fiche fournisseur sont les suivants :

![](https://support.openfire.fr/hc/article_attachments/29506298255900)

- **Produit par défaut** : produit automatiquement sélectionné sur les lignes de facture importées.  Si ce champ est renseigné, les champs **Compte de charge par défaut** et **Taxes par défaut** sont masqués car ils ne sont plus nécessaires.
- **Compte de charge par défaut** : compte comptable utilisé si aucun produit par défaut n'est défini.
- **Taxes par défaut** : taxes appliquées automatiquement aux lignes de facture à défaut d'article.
- **Forcer la description de la ligne de facture** : texte personnalisé appliqué à l'ensemble des lignes de la facture importée.
- **Forcer une seule ligne de facture** : option à cocher pour regrouper le montant total de la facture sur une seule ligne au lieu d'importer le détail ligne par ligne.
- **Forcer le journal d'achat** : journal comptable spécifique utilisé pour ce fournisseur. Si ce champ reste vide, le premier journal d'achat disponible est appliqué.

| 🚨**Avertissement** : Si vous avez rattaché une ligne d'annuaire spécifiquement à l'un de vos journaux comptables, ce journal sera utilisé en priorité, quelle que soit la configuration réalisée sur la fiche fournisseur. |
| --- |

- **Email pour les relances de factures** : adresse email dédiée aux échanges concernant le suivi et les relances de factures.

| 💡**Note **: Si vous gérez plusieurs sociétés dans OpenFire, ces paramètres sont configurables indépendamment pour chaque société. |
| --- |

## Règles d'application automatique des taxes

Les taxes appliquées sur la facture importée sont déterminées dans l'ordre suivant :

- **Si un article est identifié** : le système applique les taxes définies sur l'article pour la société concernée.
- **Si aucun article n'est identifié** : le système utilise les taxes par défaut paramétrées sur la fiche fournisseur.
- **Si aucune taxe par défaut n'est configurée** : OpenFire recherche une taxe correspondant aux données du fichier (montant TTC/HT, taxe fixe ou pourcentage, données UNECE).

## Bonnes pratiques

- **Configurer le fournisseur au préalable :** renseignez toujours les paramètres d'import de la fiche fournisseur avant d'importer ses premières factures afin d'éviter tout traitement manuel ultérieur.
- **Vérifier les premières factures :** contrôlez systématiquement les premières factures générées pour valider la bonne affectation des comptes et des taxes.
- **Utiliser la ligne unique avec parcimonie :** l'option **Forcer une seule ligne de facture** regroupe toutes les informations. À n'utiliser que si le détail de la facture ne présente pas d'intérêt comptable.

Mis a jour le : 02/09/2026
