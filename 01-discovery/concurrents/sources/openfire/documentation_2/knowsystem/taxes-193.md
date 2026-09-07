---
url: https://documentation.openfire.fr/knowsystem/taxes-193
url_finale: https://documentation.openfire.fr/knowsystem/taxes-193
date_collecte: 2026-09-06
destination: documentation_2
---

Les taxes dans OpenFire permettent de configurer les paramètres et les règles d’imputation comptable à utiliser dans le contexte d’un régime de TVA.

Les taxes permettent notamment les points suivants : 

- Imputation des comptes comptables de taxes par taux de TVA ;
- Imputation des comptes comptables de produit et charge par taux de TVA.

Il convient donc de bien vérifier cette imputation au préalable.

## Configurer les taxes

Attention: Les taxes sont déjà préconfigurées sur votre base de données. Nous vous conseillons de contacter le support OpenFire avant toutes modifications. 

Vous pouvez créer, paramétrer et consulter les taxes depuis le menu Comptabilité > Configuration > Comptabilité > Taxes.**Onglet « Définition » :**

Détail des champs :

- **« Portée »** : définie s’il s’agit d’une taxe de vente ou une taxe d’achat
- **« Calcul de la taxe »** : défini la règle de calcul de la taxe. Choix possibles :
  - *Groupe de taxe* (non utilisé) ;
  - *Fixé* : montant fixe en € ;
  - *Pourcentage du prix* : Le taux saisi sera appliqué sur le prix correspondant. Ledit prix est donc considéré comme HT (exemple : à la vente d'un appareil 2500 € en TVA 20%, la TVA sera de 500 € (20% x 2500). Le TTC sera donc de 3000 €) ;
  - *Pourcentage du prix taxe incluse* : Le taux saisi est considéré comme inclus dans le prix correspondant. Ledit prix est donc considéré comme TTC (exemple : à la vente d'un appareil à 2500 €, la TVA est alors de 417 € (2500 / (1+20%)). Le HT sera alors de 2083 €).
- **« Montant »** : montant de la taxe, en % ou en €
- **« Compte de taxe »** : compte comptable d’imputation correspondant.

**Onglet « Options avancées » :**


Détail des champs :

- « Etiquette sur les factures » : nom de la taxe tel qu’apparaissant dans la colonne « Taxe » de la commande et de la facture ;
- « Etiquettes » : Etiquettes optionnelles qui pourraient être utilisées pour des rapports personnalisés ;
- « **Inclus dans le prix**  » : si coché, signifie que lorsque cette taxe est utilisé, le prix indiqué sera TTC et non HT. C’est notamment le cas pour les taxes 5.5-TTC, 10.0-TTC et 20.0-TTC.

## Affectation des comptes

L’affectation des comptes permet de piloter l’imputation comptable de la vente ou de l’achat d’un article en fonction d’un régime de TVA en substituant le compte de l’article (achat ou vente) par un compte correspondant défini dans la taxe.

Dans Openfire, **le compte de l'article est fourni par la catégorie d'articles** à laquelle appartient cet article afin de simplifier le paramétrage de la base. Il est en effet plus simple de paramétrer une catégorie d'articles que les centaines ou milliers d'articles qui sont dans cette catégorie !

*Le compte de vente (compte de revenu) associé à la catégorie d'articles est le compte de vente HT.*

*Il suffit alors de configurer la correspondance avec le compte de vente associé au taux de TVA : 704000 Travaux HT 🡪 704050 Travaux 5,5%.*


## Achats intracommunautaires

Les achats intra-communautaires correspondent aux achats effectués auprès d’une entreprise non immatriculées en France mais résidente de l’Union Européenne.

La TVA intracommunautaire a les particularités suivantes :

- Elle est à la fois collectée et déduite ;
- Elle a des lignes spécifiques à son traitement sur la déclaration CA3.

| Code | Libellé du compte | Type | 
| 44521000 | TVA due intracommunautaire | Passif à court termes | 
| 44566200 | TVA déductible intracommunautaire | Actif actuel | 

**TVA due intracommunautaire :**


TVA déductible intracommunautaire :


Une position fiscale spécifiques est créée pour ces achats intracommunautaire ; voir les [positions fiscales](https://documentation.openfire.fr/knowsystem/position-fiscale-143).

## Sous-traitance et TVA en autoliquidation

Depuis le 1er janvier 2014, un nouveau dispositif d'autoliquidation de TVA est instauré pour les contrats de sous-traitance dans le secteur du bâtiment afin de limiter la fraude fiscale.

**Pour le sous-traitant :**

- Facturation HT avec position fiscale exonérée
- Mention en bas de facture : « TVA - autoliquidation, art. 283 nonies 2 pour les marchandises et/ou 283-2 pour les services »
- Déclaration de TVA CA3 mensuelle : indiquer votre chiffre d’affaire sous-traitant sur la ligne 5 « autres opérations non imposables ».

Pour la facturation du client, il est nécessaire d’utiliser un régime fiscal exonéré. L’imputation est faite dans un compte de vente exonéré via la catégorie de produits. Il est important de configurer cette imputation pour toutes les catégories concernées.

**Pour le donneur d’ordre :**

- Paiement de la facture HT
- Déclaration de TVA CA3 mensuelle : 
  - Indiquer le montant HT de la sous-traitance sur la ligne 2 «
  - autres opérations imposables » ;
  - Déclarer la TVA acquittée et également déductible donc une opération blanche pour le donneur d’ordres ;
  - Déclarer les sommes sur la CA3… sous peine de lourde amende !

**Création des comptes de TVA due et déductible :**

| Code | Libellé du compte | Type | 
| 44522000 | TVA due autoliquidation | Passif à court terme | 
| 44566300 | TVA déductible autoliquidation | Actif actuel | 

**Taxe Sous-Traitant due autoliquidation :**

**Taxe Sous-Traitant déductible autoliquidation :**


[positions fiscales](https://documentation.openfire.fr/knowsystem/position-fiscale-143).