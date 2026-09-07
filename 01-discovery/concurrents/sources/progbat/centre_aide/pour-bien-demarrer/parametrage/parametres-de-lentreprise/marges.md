---
url: https://docv5.progbat.com/pour-bien-demarrer/parametrage/parametres-de-lentreprise/marges
url_finale: https://docv5.progbat.com/pour-bien-demarrer/parametrage/parametres-de-lentreprise/marges
date_collecte: 2026-09-06
destination: centre_aide
---

# Marges

**Cliquez sur le bouton "Paramètres" en haut à droite de l'écran** , **puis sur la vignette "Entreprise".
Ouvrez la section "Marges"**

## Le concept de marge

ProGBat utilise le concept de la "marge brute", c'est à dire calculée sur le prix d'achat.

Exemple :

- Un article est affiché 100 € en prix public,
- Votre fournisseur vous accorde 30% de remise, vous l'achetez donc 70 €.
- Si vous vendez cet article 100 €, 
  - **votre marge brute sera de (100 - 70) / 70, soit 42,86 %**
  - votre marge nette sera de (100 - 70) / 100, soit 30%.

### Pourquoi ne pas utiliser la marge nette, qui correspond à la remise accordée par mon fournisseur sur le prix public ?

Simplement parce que vous êtes libre de vos prix de vente, et rien de vous oblige à vendre 100 € un produit acheté 70 €, sous prétexte qu'il s'agit du prix public du catalogue fournisseur.

La marge brute permet de mieux contrôler ses marges, et donc sa rentabilité.

## Que représente la marge sur ProGBat ?

Par souci de simplification, la marge définie sur ProGBat regroupe 2 taux :

- Le pourcentage de frais généraux, appliqué sur le prix d'achat. On obtient le "prix de revient".
- Le pourcentage de bénéfice souhaité, appliqué sur le prix de revient, pour obtenir le prix de vente.

Autrement dit, si vous souhaitez appliquer 10% de frais généraux, et 20% de bénéfices, vous devrez fixer votre marge à 32% :

10% de frais généraux 20% de bénéfices

100 + (100 * 10%) = 110 110 + (110 * 20%) = 132

(132 - 100) / 100 = **32%**

5% de frais généraux 30% de marge

100 + (100 * 5%) = 105 105 + (105 * 30%) = 136,50

(136,50 - 100) / 100 = **36,5%**

### La méthode simple de calcul

*Méthode simple de calcul pour* **10***% de frais généraux, et* **20***% de bénéfices :* 

1,**10** * 1,**20** = 1,**32 soit 32%**

*Méthode simple de calcul pour* **5***% de frais généraux et* **30***% de bénéfices :*

1,**05** * 1,**30** = 1,**365 soit 36,5%**

## Saisir / modifier vos marges

Vous avez défini vos taux de marge avec la méthode précédente, vous pouvez maintenant les appliquer pour chaque type d'élément

- Les fournitures,
- La main d'œuvre,
- La location d'outillage ou matériel de chantier,
- La sous-traitance,
- l'outillage, plus particulièrement l'amortissement de votre propre matériel, notamment engins de chantier.

### Mise à jour de la bibliothèque

A chaque fois que vous allez modifier un taux de marge, le logiciel vous demandera si vous souhaitez appliquer la nouvelle marge à toute la bibliothèque.

#### La bibliothèque d'éléments

- L'application du nouveau taux de marge modifiera le prix de vente de l'élément, et ne modifiera pas son prix d'achat.
- Le nouveau taux sera appliqué à un élément uniquement si sa marge est égale à l'ancien taux.
- Autrement dit, si vous aviez "forcé" la marge d'un élément en particulier, il ne sera pas modifié pour éviter d'écraser vos marges spécifiques.

#### La bibliothèque d'ouvrages

- Si vous travaillez avec des ouvrages composés, le taux de marge des ouvrages ne sera jamais celui qui est défini ici, car la marge de l'ouvrage dépendra de la marge de chaque élément le composant.
- Lorsque le prix d'un élément est mis à jour, tous les ouvrages dont la composition contient cet élément sont automatiquement mis à jour, ainsi que la marge calculée de chaque ouvrage.

Mis à jour