---
url: https://documentation.openfire.fr/knowsystem/configurer-la-situation-retenue-de-garantie-et-compte-prorata-208
url_finale: https://documentation.openfire.fr/knowsystem/configurer-la-situation-retenue-de-garantie-et-compte-prorata-208
date_collecte: 2026-09-06
destination: documentation_2
---

# Etape préliminaire

Vérifier que le module de gestion de situation est bien installé dans la base. **Accès:** **Ventes > Ventes > Devis**

Sur un devis, cliquer dans l’onglet Autres informations. Les champs suivants doivent apparaître :

Si ces champs n'apparaissent pas, il faut contacter le support.

Une configuration doit être effectuée pour la création de comptes comptables, des catégories d'articles et des articles pour :

- SITUATION
- RETENUE DE GARANTIE
- PRORATA

# Configuration pour la situation



#### Création des comptes comptables SITUATION

Rendez-vous dans le menu **Comptabilité>Conseiller>Plan comptable**

Les comptes comptables en lien avec la situation sont à créer dans le plan comptable. Ces comptes ci-dessous peuvent être proposés par défaut, sinon, il faut se rapprocher du cabinet comptable pour connaître les comptes comptables associés.

ATTENTION : Pour les multi sociétés, il faut créer les comptes comptables dans chaque société ayant une comptabilité séparée.

#### Création de l’article SITUATION

Accès : Ventes>Ventes>Articles

L’article “Situation” sera utilisé pour générer les factures de situation intermédiaire, selon le même modèle que les factures d’acompte.

Informations à renseigner :

- L’article doit être de type service
- L’article est associé à une catégorie interne spécifique dédié : SITUATION

- #### Pas de configuration comptable particulière au niveau de l'article

#### 

Création de la catégorie SITUATION

**Accès : Ventes>Configuration>Catégories d'articles**

C’est la catégorie d’article qui va porter la configuration de la comptabilité.

Il faut par défaut le compte “707940 Situation HT exo”. Ce compte servira comme table de correspondance au niveau des taxes de ventes.

#### Configuration des taxes


Accès : Comptabilité>Configuration>Taxes

Une correspondance des comptes comptables “Situation” est opérée dans les différentes taxes de ventes. Pour les taxes de vente suivantes :

    TVA collectée (vente) 5,5 % ;

    TVA collectée (vente) 5,5 %TTC ;

TVA collectée (vente) 10 % ;

TVA collectée (vente) 10 % TTC ;

TVA collectée (vente) 20 % ;

    TVA collectée (vente) 20 %TTC ;

 il faut mettre la table de correspondance des comptes de situation comme l’exemple ci-dessous : le compte de produit 707940 exo doit être affecté au compte de produit en rapport avec le taux de TVA.

# Configuration pour la retenue de garantie

#### Création du compte comptable Retenue de garantie

**Accès : Comptabilité>conseiller>Plan comptable** 

- La retenue de garantie n’est pas un compte de produit ou de charge. Le type sera à mettre en “prépaiements”
- La valeur est donc imputée dans un compte 411, et la TVA est neutralisé par une taxe 0%


 

#### 

        Création de l’article RETENUE DE GARANTIE 


**Accès : Ventes>Ventes>Articles**

Informations à renseigner :

- L’article doit être de type service
- L’article est associé à une catégorie d’article spécifique dédié, ou à défaut dans une catégorie Produit Financier

- ### Dans l'onglet Facturation, noter dans le compte de revenus le compte comptable associé et cet article doit être exonéré de TVA (TVA 0% autres opérations non imposable)

# 

Configuration pour le prorata

#### Création du compte comptable PRORATA

**Accès : Comptabilité>Conseiller>Plan comptable**

Création du compte 6064300 Prorata et frais de chantier

#### Création de l’article PRORATA

**Accès : Ventes>Ventes>Articles**

Le prorata est considéré comme une charge à déduire du montant global de la vente, et non comme une diminution du CA. 

Comptablement, un compte de classe 6 (charge) est associé comme compte de revenu et comme compte de dépense pour cet article.

Le compte prorata est normalement traité à la TVA déductible de 20%.

La taxe doit donc être définie également directement dans l’article.

Eléments spécifiques :

- L’article doit être de type service
- L’article est associé à une catégorie d’article spécifique ou par défaut "PRODUIT FINANCIER"

 

- Dans l'onglet Facturation, renseigner le compte associé :

# Configuration globale ventes

**Accès : Ventes>Configuration>Configuration**

Il faut définir dans la partie Taxes et facturation / configuration d'article, les articles associés :


# Configuration des impressions pdf

**Accès : Comptabilité>Configuration>Impression des totaux dans les factures de vente**


Pour les impressions des Proratas et retenues de garanties en bas de page sur les factures en pdf, il faut créer 2 règles d'impression : 

    * une règle pour la retenue de garantie :

    * une règle pour le prorata :

A l'impression, le résultat sera le suivant :