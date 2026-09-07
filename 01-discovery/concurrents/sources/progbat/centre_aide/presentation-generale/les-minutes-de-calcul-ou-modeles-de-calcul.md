---
url: https://docv5.progbat.com/presentation-generale/les-minutes-de-calcul-ou-modeles-de-calcul
url_finale: https://docv5.progbat.com/presentation-generale/les-minutes-de-calcul-ou-modeles-de-calcul
date_collecte: 2026-09-06
destination: centre_aide
---

# Les minutes de calcul ou modèles de calcul

Pas toujours simple de calculer une surface ou un volume lorsque l’on souhaite chiffrer ses travaux…

Sur ProGBat, vous allez pouvoir :

👉 Calculer très facilement la quantité (surface, volume, etc) nécessaire pour réaliser vos travaux

👉 Retrouver à tout moment quel calcul vous a permis de saisir une quantité dans un devis

👉 Créer vos propres modèles de calcul, et les enregistrer. Vous pourrez ensuite les utiliser à l'infini, et les rendre "automatiques"

**Pour des chiffrages facilités, et un gain de temps considérable !**

## Qu'est ce qu'une minute ou modèle de calcul

Il s'agit d'un tableau, dans lequel chaque ligne contient une variable, un chiffre ou une opération, et qui permet de réaliser des calculs, un peu comme sur un tableau Excel.

Un exemple vaut mieux qu'un long discours :

**Voici un exemple simple de modèle pour calculer une surface :** 

### Le principe

- La première variable s'appelle LONG, mais vous pouvez la nommer comme vous voulez. Nous avons choisi LONG pour "longueur". 
  - Dans l'opération, nous avons simplement mis un chiffre. Au niveau de l'ouvrage, l'idéal est de saisir 0 ou 1, la véritable longueur sera mise à jour dans le devis.
  - Le commentaire est libre, il permet parfois de préciser l'opération réalisée, ou la valeur attendue par la variable.
- La deuxième variable s'appelle LARG, pour "largeur", mais là aussi, on aurait pu la nommer autrement. 
  - Dans l'opération, comme pour la ligne précédente, nous avons simplement mis un chiffre. 💡Si ce modèle est surtout destiné à calculer des surfaces de murs, on pourrait appeler la variable "hauteur", et mettre 2.5 dans l'opération, ce sera une donnée de moins à modifier dans le devis (mais qui restera modifiable bien sûr).
  - Dans le commentaire, on précise que LARG peut correspondre à une largeur ou à une hauteur.
- La troisième variable s'appelle SURF, sans surprise pour "surface", mais on aurait pu écrire S, ou SURFACE, ou Surface, ou TOTAL... 
  - Dans l'opération, nous faisons un calcul, en demandant de multiplier la longueur par la largeur, ce qui dans notre exemple donnera le résultat 15

### Ajouter une ligne de calcul

Cliquez simplement sur le bouton "Ajouter une ligne de calcul".

Sur notre exemple, imaginons que nous souhaitions déduire les surfaces d'ouverture, nous pourrions ajouter une ligne :

- Variable = DEDUCTION
- Opération = nombre de m² à déduire

puis une autre ligne :

- Variable = SURF_NETTE
- Opération = SURF - DEDUCTION

### Supprimer une ligne de calcul

Cliquez simplement sur la corbeille en bout de ligne.

⚡ Attention, supprimer une ligne peut modifier totalement le résultat, voire créer des erreurs si la variable supprimée est utilisée plus bas dans le calcul.

### Repoussez les limites

Allez encore plus loin, en utilisant les formules mathématiques javascript, pour des modèles très poussés, comme celui-ci, pour calculer la surface d'un double rampant :

## Intégrer un modèle de calcul 

### Dans une fiche ouvrage

Il est très utile d'appliquer un modèle de calcul à un ouvrage, car il sera automatiquement récupéré lorsque vous ajouterez cet ouvrage dans un devis.

### Dans une fiche élément

Le principe est rigoureusement identique à la fiche ouvrage, vous pouvez vous y reporter [en cliquant ici.](https://docv5.progbat.com/presentation-generale/les-minutes-de-calcul-ou-modeles-de-calcul#integrer-un-modele-de-calcul-dans-une-fiche-ouvrage)

#### Cas d'usage 

pourrait être, pour de la vente de carrelage :

ajouter une ligne :

- Variable = SURFACE (sous entendu "à carreler")
- Opération = nombre de m² à carreler

puis une autre ligne :

- Variable = PERTE
- Opération = SURFACE * 0.05 (pour 5% de perte)

et une dernière ligne

- Variable = NET
- Opération = SURFACE + PERTE

### Dans une ligne de devis

⚡ **C'est là que la minute ou modèle de calcul prend tout son intérêt.**

Le fait d'avoir appliqué un modèle à un ouvrage ou à un élément permet simplement que le modèle soit automatiquement appliqué à la ligne du devis contenant l'ouvrage ou l'élément, ce qui est déjà un gain de temps considérable.

#### Le menu de ligne

Lorsque vous sélectionnez une ligne dans votre devis, le menu de ligne apparaît :

Cliquez sur le bouton (Calculer la quantité) du menu de ligne pour ouvrir, créer ou modifier un modèle de calcul

Mis à jour