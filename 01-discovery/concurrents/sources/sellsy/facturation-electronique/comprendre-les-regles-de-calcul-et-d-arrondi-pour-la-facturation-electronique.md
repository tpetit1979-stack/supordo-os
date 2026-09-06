---
source: https://help.sellsy.com/fr/articles/13481776-comprendre-les-regles-de-calcul-et-d-arrondi-pour-la-facturation-electronique
categorie: Facturation électronique
titre: Comprendre les règles de calcul et d'arrondi pour la facturation électronique
date_recuperation: 2026-09-05
---

# Comprendre les règles de calcul et d'arrondi pour la facturation électronique

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/1978070728/77a3901d35dd95e1413980282340/FAQ-Bannie-CC-80reAcademy-2-2B-282-29.png?expires=1788635700&signature=0fc0353283f34e21aa544dafdb03b4abd879ace4161c76e4607c173a845b3cfb&req=dSkgHsl5nYZdUfMW1HO4zSTebKcBGjjmcsEztsulEnplukfl6a00TIFu71Tu%0A4GYGXp8OIzJJIqG5t44%3D%0A)

### **Les méthodes d’arrondi de la TVA**

La loi autorise **deux méthodes de calcul** pour la TVA :

Somme des montants de TVA par ligne

Avec cette méthode, la TVA est calculée et arrondie pour chaque ligne du document. Les montants arrondis sont ensuite additionnés pour obtenir le montant total de TVA du document.

> **Exemple :**
> Deux produits soumis à une TVA de 20 % :
> 15,63 € HT et 23,69 € HT
> TVA : 3,13 € + 4,74 € = 7,87 €
> Total TTC : **47,19 €**

Calcul de la TVA sur le total du document

Avec cette méthode, les montants hors taxes sont d’abord additionnés. La TVA est ensuite calculée et arrondie une seule fois sur le total HT du document.

> **Exemple :**
> Deux produits soumis à une TVA de 20 % :
> 15,63 € HT et 23,69 € HT
> Total HT : 39,32 €
> TVA : 7,86 €
> Total TTC : **47,18 €**

**Sellsy applique cette seconde méthode, le calcul de la TVA sur le montant total du document depuis plusieurs années**, conformément aux règles de la norme EN 16931.

___________________________________________________________

### Règles d'arrondi dans les calculs de Factur-X

La [norme Factur-X (paragraphe 7.1.8 de la norme)](https://fnfe-mpe.org/factur-x/) définit les règles d’arrondi suivantes dans les calculs dès qu’il y a multiplication ou division.

La méthode d’arrondi est celle de la valeur la plus proche, avec la règle pour la détermination de la fraction résiduelle à 0,5 suivante :

- **Pour les nombres positifs :** arrondi à la valeur supérieure. *Par exemple, 13,455 arrondi à 2 chiffres donne 13,46.*
- **Pour les nombres négatifs :** arrondi à la valeur inférieure (de façon à ce qu’un arrondi de 2 nombres strictement opposés donne des nombres arrondis strictement opposés). *Par exemple, -13,455 donne -13,46.*

Concrètement, cela signifie que tout résultat issu d’un calcul intermédiaire (prix unitaire × quantité, base HT × taux de TVA, etc.) doit être arrondi à deux décimales en appliquant strictement cette règle.

___________________________________________________________

### Ce qui change concrètement dans Sellsy

Depuis la mise en conformité à la facturation électronique, vous avez peut-être remarqué de légers changements dans l’affichage de certains montants sur vos documents de vente, notamment au niveau des arrondis. Ces évolutions sont normales et résultent de l’application des règles officielles prévues par la norme Factur-X et la norme européenne EN 16931.

La méthode de calcul de TVA ne change pas. Cependant, nous devons désormais nous assurer que vos documents de vente respectent l’arrondi à deux décimales sur le calcul à la ligne. Cela veut dire que :

- **Sur vos documents de vente,** tous les montants sont arrondis à deux décimales, *par exemple 0,12 €.*
- Selon votre configuration, **vous pouvez continuer à afficher quatre décimales sur les lignes**, *par exemple 0,1200 €.*

Depuis l’application de ces règles, il peut donc exister de légers écarts entre certaines factures anciennes et les nouvelles factures émises. 
Ces différences, généralement minimes, sont uniquement liées à la normalisation des règles d’arrondi imposées par la facturation électronique. Elles n’affectent ni la conformité, ni la validité, ni la fiabilité de vos documents.
​

> À retenir
> - Tous les montants sont arrondis à deux décimales.
> - Depuis toujours, Sellsy applique un arrondi unique de la TVA sur le total HT du document.
> - Les écarts éventuellement observés lors de comparaisons correspondent à des méthodes de calcul différentes, et non à des erreurs.

Mis a jour le : 20/02/2026
