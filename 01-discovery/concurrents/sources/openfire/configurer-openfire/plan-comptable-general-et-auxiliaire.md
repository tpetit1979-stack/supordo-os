---
source: https://support.openfire.fr/hc/fr/articles/19096261914524-Plan-comptable-g%C3%A9n%C3%A9ral-et-auxiliaire
categorie: Configurer OpenFire
titre: Plan comptable général et auxiliaire
date_recuperation: 2026-09-05
---

# Plan comptable général et auxiliaire

**Le plan comptable** (PC) est l'ensemble structuré des **comptes utilisés pour enregistrer toutes les transactions financières** de votre entreprise. Il est essentiel pour une gestion comptable précise et pour la production de vos rapports financiers.

Cet article vous guide pas à pas pour **comprendre, consulter et gérer les plans comptables général et auxiliaire de vos sociétés comptables** au sein de votre environnement OpenFire.

Cet article contient les sections suivantes :

- Consulter votre plan comptable
- Créer un compte comptable général
  - Dupliquer un compte existant
  - Configurer un compte
  - Comprendre les types de comptes
  - Utiliser les groupes de comptes
- Gérer les comptes clients et fournisseurs
- Gérer le plan comptable en multi sociétés

# Consulter votre plan comptable

---

**Votre environnement OpenFire** est livré avec un plan comptable **préconfiguré** et adapté à votre activité et à votre localisation fiscale. Vous avez ensuite la possibilité de le personnaliser pour qu'il corresponde exactement aux spécificités de votre entreprise.

*Pour accéder à votre plan comptable et le consulter :*

- ***Pour le plan Basique** : **OpenFire > Configuration > Comptabilité > Plan comptable*
- ***Pour les autres plans** :  **Facturation > Configuration > Comptabilité > Plan comptable.*

Chaque plan comptable est associé à une société spécifique. Pour rechercher un compte en particulier, vous pouvez utiliser la **barre de recherche** ou naviguer dans les différents groupes de comptes via le **volet latéral** de l'interface.

![](https://support.openfire.fr/hc/article_attachments/21408395106076)

Voici les principaux filtres de recherche que vous pouvez utiliser :

- **Créances** : Affiche les comptes clients (généralement les comptes commençant par 411).
- **Dettes fournisseurs** : Affiche les comptes fournisseurs (généralement les comptes commençant par 401).
- **Produits** : Affiche les comptes de la classe 7 (comptes de revenus).
- **Charges** : Affiche les comptes de la classe 6 (comptes de dépenses).

# Créer un compte comptable général

---

La plupart des comptes généraux sont créés automatiquement au début de votre utilisation d'OpenFire, soit lors de la génération de votre base de données, soit lors de l'importation de votre plan comptable existant. Cependant, vous pourriez avoir besoin de créer de nouveaux comptes comptables généraux en cours d'activité.

## Dupliquer un compte existant

Pour créer un nouveau compte comptable, la **méthode la plus simple et la plus fiable** est de **dupliquer un compte de même nature**. Cela vous permet de récupérer sa configuration existante et de l'adapter.

Pour ce faire :

1. Sélectionnez le compte à dupliquer dans la liste des comptes
2. Cliquez sur le bouton **Configuration** en bout de ligne de l'enregistrement sélectionné

  ![Liste de comptes comptables lettrables](https://support.openfire.fr/hc/article_attachments/21408566787996)
3. Cliquez sur **Action** puis sur **Dupliquer**.

## Configurer un compte

Après avoir dupliqué un compte ou si vous créez un compte de zéro, vous devrez compléter les informations suivantes :

**Code** : Numéro du compte. Ce numéro doit être **unique** par société.

**Nom du compte** : Libellé clair du compte.

![](https://support.openfire.fr/hc/article_attachments/21408552371228)

Depuis l'onglet **Comptabilité**

**Type** : Définit la nature et le comportement du compte (voir la section "Comprendre les types de comptes" ci-dessous pour plus de détails).

**Taxes par défaut** : Permet de définir la taxe à utiliser par défaut lorsque ce compte est associé à un produit ou une charge.

**Étiquettes** : Vous permet d'attribuer des étiquettes optionnelles pour l'édition de rapports comptables spécifiques.

**Journaux autorisés** : Définit la liste des journaux dans lesquels ce compte peut être utilisé. Si ce champ est vide, le compte peut être utilisé dans tous les journaux.

**Obsolète** : Cochez cette case si le compte ne doit plus être utilisé. Le compte ne sera alors plus proposé lors des saisies.

**Centralisé** : Si cette case est cochée, seuls les montants centralisés par période seront affichés dans les rapports du Grand Livre, sans les détails.

**Éditable** : Un compte non éditable ne peut être modifié que par l'administrateur OpenFire.

**Groupe** : Permet d'attribuer un compte parent à la création d'un nouveau compte (voir la section "Utiliser les groupes de comptes" ci-dessous).

**Société** : Société à laquelle le compte est associé.

Depuis la vue liste des comptes comptables

**Autoriser le lettrage** : Cette option est disponible directement depuis la vue liste des comptes comptables via un bouton d'activation. Les comptes lettrables par défaut sont généralement les comptes de classe 4 (comptes de tiers), les comptes de banque et de paiement (511 et 512), et les comptes de TVA.

| **🧑‍🏫Exemple** : Dans l'exemple ci-dessous, les comptes de TVA commençant par 445 autorisent le lettrage. ![](https://support.openfire.fr/hc/article_attachments/21408566787996) |
| --- |

## Comprendre les types de comptes

Le type de compte joue un rôle crucial en définissant les fonctions suivantes :

- **Objectif et comportement** du compte dans la production comptable : compte lettrable, etc.
- Génération de **rapports juridiques et financiers** spécifiques à chaque pays.
- Définition des règles de **clôture d'un exercice et **de génération des **écritures d'ouverture **par type de compte

| 🚨**Avertissement** : A la création d'un compte, OpenFire attribue le type de compte automatiquement en fonction de la racine du code de compte saisie. Si, en cours de création, vous modifiez la racine du code, pensez à actualiser manuellement le type de compte associé. |
| --- |

Les types de comptes définissent la structure du bilan de la façon suivante :

![](https://support.openfire.fr/hc/article_attachments/21408566788252)

## Utiliser les groupes de comptes

Les groupes de comptes permettent de classifier plusieurs comptes comme des sous-comptes d'un compte principal. Cette fonctionnalité simplifie grandement la **consolidation de vos rapports financiers**, comme la balance générale.

Chaque compte est automatiquement associé à son groupe par défaut, en fonction des deux premiers caractères de son code. Le volet latéral vous permet d'utiliser cette notion de groupe de compte pour faciliter la recherche et la navigation dans votre plan comptable.

Voici les principaux groupes de comptes :

- **Groupes 1 à 5** : Correspondent aux comptes de bilan.
- **Groupes 6 et 7** : Correspondent aux comptes de résultat.
- **Groupe 9** : Il s'agit d'un groupe spécifique à OpenFire (ou Odoo, la base d'OpenFire), temporairement utilisé pour le compte 99999 qui valorise le résultat de l'exercice de la société.

![](https://support.openfire.fr/hc/article_attachments/21408566788380)

# Gérer les comptes clients et fournisseurs

---

Contrairement aux comptes généraux, la création des comptes de tiers (clients ou fournisseurs) est généralement **automatisée** dans OpenFire, sauf lors d'une éventuelle reprise de données initiale.

La génération d'un compte de tiers se produit dès qu'un événement comptable intervient pour le client ou le fournisseur concerné, par exemple lors de :

- L'enregistrement d'une facture.
- L'enregistrement d'un règlement.
- La saisie d'une pièce comptable.

La création des comptes de tiers se base sur un modèle qui standardise la génération du code et du libellé du compte.

*Pour configurer ce modèle :*

- ***Depuis le plan Basique** : OpenFire > Configuration > Paramètres généraux*
- ***Depuis les autres plans** :  Facturation > Configuration > Paramètres généraux.*

![](https://support.openfire.fr/hc/article_attachments/21408566788764)

Voici des exemples de configuration types :

| Syntaxe | Rendu |
| --- | --- |
| `('411%05i' % partner.id, partner.name)` | **Pour le client Jean-Paul Belmondo**  ID de l'enregistrement : 12300  **Code** : 41112300  **Libellé** : Jean-Paul Belmondo |
| `([s+(i>1 and '%02d' % i or '') for s in ['411%s' % partner.name.replace(' ', '').replace('-','').replace('.','')[:3].upper()] for i in [int((partner.env['account.account'].search([('code','=like',s+'%'),('company_id', '=', company.id)]).filtered(lambda a:len(a.code)==len(s)or a.code[len(s):].isdigit()).sorted(key=lambda a: (len(a.code),a.code))[-1:].code or '0'*(len(s)+1))[len(s):] or '1')+1]][0], partner.name)` | **Pour le client Jean-Paul Belmondo**  ID de l'enregistrement : 12300  **Code** : 411BEL01  **Libellé** : Jean-Paul Belmondo |
| `('401%05i' % partner.id, partner.name)` | **Pour le fournisseur Cheminées Poujoulat**  ID de l'enregistrement : 7200  **Code** : 41172000  **Libellé** : Cheminées Poujoulat |
| `([s+(i>1 and '%02d' % i or '') for s in ['401%s' % partner.name.replace(' ', '').replace('-','').replace('.','')[:3].upper()] for i in [int((partner.env['account.account'].search([('code','=like',s+'%'),('company_id', '=', company.id)]).filtered(lambda a:len(a.code)==len(s)or a.code[len(s):].isdigit()).sorted(key=lambda a: (len(a.code),a.code))[-1:].code or '0'*(len(s)+1))[len(s):] or '1')+1]][0], partner.name)` | **Pour le fournisseur Altema**  ID de l'enregistrement : 4321  **Code** : 401ALT01  **Libellé** : Altéma |

# Gérer le plan comptable en multi-sociétés

---

Si vous travaillez avec plusieurs sociétés dans votre environnement OpenFire, sachez qu'un nouveau plan comptable France est automatiquement chargé à chaque ajout d'une nouvelle société comptable.

# Bonnes pratiques

---

- **Pensez à dupliquer** : Lorsque vous créez un nouveau compte général, la duplication d'un compte existant de même nature est la méthode la plus simple pour garantir une configuration cohérente.
- **Vérifiez le type de compte** : Assurez-vous que le **Type** de compte est correctement défini, car cela impacte directement les rapports financiers et le comportement du compte.
- **Utilisez les groupes de comptes** : Tirez parti des groupes de comptes pour une meilleure organisation et une consolidation simplifiée de vos rapports financiers.

Mis a jour le : 30/07/2025
