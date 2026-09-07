---
url: https://documentation.openfire.fr/knowsystem/plan-comptable-279
url_finale: https://documentation.openfire.fr/knowsystem/plan-comptable-279
date_collecte: 2026-09-06
destination: documentation_2
---

A l’installation, OpenFire est doté d’un plan comptable adapté au pays. Ce plan comptable peut ensuite être personnalisé en fonction des besoins de l’entreprise.

## Création du plan comptable

Le plan comptable est visible dans le menu **Comptabilité > Conseiller > Plan comptable.** Il est associé à la société. Lors de la création de votre base, deux cas de figure sont possibles:

- Soit votre plan comptable a été importé,
- Soit un plan comptable par défaut, le plan comptable français généré par le module France - Accounting de Odoo, est installé.

  Plus d'informations sur [le lettrage](https://documentation.openfire.fr/knowsystem/lettrage-comptable-192)

## Création d'un compte

Pour créer un nouveau compte comptable, la bonne méthode est de dupliquer un compte de même nature. Exception faite pour les comptes de tiers qui sont générés automatiquement à la création du partenaire.

Chaque compte comptable est défini par les éléments suivants :

- Code : numéro du compte
- Nom : libellé du compte
- Type : ce qu'il faut retenir principalement sur le type de compte : 
  - les comptes commençant par 7... seront toujours des comptes de type Revenus
  - les comptes commençant par 6... seront toujours des comptes de type Charges
  - Pour plus de précision dans la section suivante « Type de compte ».
- Taxes par défaut : taxe à utiliser par défaut en lien avec le compte concerné
- Etiquettes : étiquettes optionnelles que l’on peut ajouter pour l’édition de rapports comptables spécifiques se basant sur la classification de ces étiquettes.
- Autoriser le lettrage : compte lettrable. Dans Odoo, les comptes lettrables par défaut sont : les comptes de classe 4, les comptes de banque et de paiement (511 et 512) et les comptes de TVA.
- Obsolète : comptes à ne plus utiliser. Si coché, le compte ne sera plus proposé en saisi.
- Centralisé : si coché, le détail des écritures ne sera pas affiché dans le grand livre. Seul un regroupement par mois sera proposé


 Astuce: il est souvent plus rapide de dupliquer un compte similaire ou de même catégorie.

Il ne restera qu'à modifier son nom et son numéro. Cela permet aussi d'éviter de se tromper de type de compte.

Pour cela, rendez-vous dans le compte que vous souhaitez dupliquer, puis cliquez sur**Action > Dupliquer**

## Type de comptes

Les type de compte sont visibles depuis le menu **Comptabilité > Configuration > Comptabilité > Type de compte**

Le type de compte est utilisé :

- Comme indication pour l’utilisateur
- Pour créer des rapports comptables spécifiques
- Pour piloter les clôtures d’exercice

Pour chaque type de compte, un type interne est configuré. Il définit les caractéristiques du type de compte concerné :

Les types internes proposés sont les suivants :

- Régulier : type par défaut
- Recevable : type de compte des comptes clients
- Payable : type de compte des comptes fournisseurs
- Liquidités : type de compte des comptes de banques

Les types de comptes suivants sont proposés par défaut :

| **Type de comptes**  | **Type Interne** | 
| Actifs actuels | Régulier | 
| Actifs non-courants | Régulier | 
| Amortissement | Régulier | 
| Autre revenu | Régulier | 
| Banque et liquidités | Liquidités | 
| Bénéfices de l'année en cours | Régulier | 
| Capitaux propres | Régulier | 
| Carte de crédit | Liquidités | 
| Charges | Régulier | 

| Coût des ventes | Régulier | 
| Immobilisations | Régulier | 
| Passif à court terme | Régulier | 
| Passifs non-courants | Régulier | 
| Payable | Payable | 
| Prépaiements | Régulier | 
| Recevable | Recevable | 
| Revenus | Régulier | 

Rubriques de bilan et du compte de résultat. Les rubriques de bilan définissent de facto la maquette de présentation du bilan:

| **Rubrique**  | **Préfixe** | 
| Actif | 109 169 201 203 205 206 207 208 211 212 213 214 215 218 231 232 237 238 261 266 267 268 271 272 273 274 275 2761 27682 28 29 31 32 33 34 35 37 39 409 4091 4096 4097 4098 416 417 418 425 4287 4387 441 443 444 4452 4456 4487 451 455 456 4562 458 462 465 467 4687 471 476 478 481 486 49 501 502 503 504 505 506 507 508 51 52 58 59 | 
| Passif | 101 104 105 1061 1062 1063 1064 1068 107 108 110 119 120 129 13 14 15 161 163 164 165 166 1675 168 16881 16883 16884 17 269 279 280 281 404 405 408 4081 4084 4088 4191 4196 4197 4198 421 422 424 426 427 4282 4284 4286 43 442 4455 4457 44584 44587 446 447 4482 4486 45 457 464 4686 477 487 509 512 514 517 5186 519 | 
| Charges | 601 602 6031 6032 6037 604 605 606 607 6081 6082 6084 6087 609 61 6122 6125 62 63 641 644 645 646 647 648 649 65 655 66 666 667 671 672 675 678 6811 6812 6815 6816 6817 686 687 689 69 691 695 698 699 | 
| Produits | 701 702 703 704 705 706 707 708 709 713 72 74 75 755 760 761 762 763 764 765 766 767 768 771 772 775 777 778 781 786 787 789 791 796 797 | 
| Fournisseur | 401 402 403 | 
| Client | 411 412 413 | 

## Multisociété

Dans un mode multi-société, un plan comptable différent par société peut être généré.