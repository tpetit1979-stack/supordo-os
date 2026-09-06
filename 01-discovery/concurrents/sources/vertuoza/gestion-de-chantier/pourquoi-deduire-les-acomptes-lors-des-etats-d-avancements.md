---
source: https://intercom-help.eu/vertuoza/fr/articles/161705-pourquoi-deduire-les-acomptes-lors-des-etats-d-avancements
categorie: Gestion de chantier
titre: Pourquoi déduire les acomptes lors des états d’avancements?
date_recuperation: 2026-09-05
---

# Pourquoi déduire les acomptes lors des états d’avancements?

### Qu’est-ce que la déduction des acomptes ?

Dans le cadre d’une facturation via [situations ou états d’avancement](https://intercom-help.eu/vertuoza/fr/articles/133049-avancement), si un acompte a été facturé, il faut déduire son montant au fur et à mesure des avancements, pour ne pas facturer 100% du projet + le montant de l’acompte.

### Pourquoi déduire les acomptes ?

Lorsqu’on facture via situation ou avancement, on considère qu’on facture **les travaux effectués**.

Le pourcentage d’avancement indiqué pour chaque poste du devis correspond donc à ce qui a été fait pour ce poste, **de 0% (pas commencé) à 100% (poste terminé)**. Ce pourcentage est répercuté sur le montant total du poste pour pouvoir générer **une facture d’avancement**.

C’est à dire que même si 10% du montant total du chantier à déjà été facturé via un acompte, lors du premier avancement, on considère que tous les postes sont à 0% et restent entièrement à faire/facturer.

**Exemple : Sur un projet à 1000€, on veut facturer 10% d’acompte pour acheter le matériel, puis faire 3 avancements de 30%, 30% et 40% à la livraison.**

**Si je ne déduis pas l’acompte :**

Je facture donc un acompte de 10% soit 100€ Je génère ensuite un avancement de 30% du total, soit 300€

Puis un deuxième de 30%, soit 300€

Et enfin l’avancement final de 40%, soit 400%

⇒ Sur la totalité du projet, j’ai facturé 1100€ à mon client.

**Pourquoi ne pas décompter ces 10% dans les avancements prévus par la suite et faire 30%/30%/30% ?**

Parce que cet acompte ne correspond pas à des travaux effectués. Il n’a pas d’impact sur l’avancement des postes ligne par ligne. Donc si je facture mon projet via 3 avancements de 30%, le montant total facturé sera bon, mais le dernier avancement indiquera qu’il reste encore 10% des travaux à effectuer.

### Comment déduire un acompte ?

### Déduire un acompte : le principe

Pour déduire un acompte des avancements à venir, il faut répartir le montant de cet acompte proportionnellement sur chaque facture d’avancement.

**Deux solutions :**

- Je ne sais pas exactement de quel pourcentage sera chaque avancement, mais je sais que je facture mon client via X tranches : Je divise le montant de mon acompte par X et je retire ce sous-montant de chaque facture d’avancement.

**Dans notre exemple :**

J’ai facturé 100€ d’acompte et je sais que je ferais trois avancements par la suite.

Je divise 100€ par 3 = 33,33€

Sur chaque facture d’avancement, je retire 33,33€ au total

- Je sais exactement de quels pourcentages d’avancement seront mes factures suivantes : Je retire le même % du montant de mon acompte à chaque fois.

**Dans notre exemple (30%/30%/40%) :**

Sur la première facture d’avancement je retire 30% de 100€ (soit 30€)

Sur la deuxième facture d’avancement je retire 30% de 100€ (soit 30€)

Sur la dernière facture d’avancement je retire 40% de 100€ (soit 40€)

Avec ces deux méthodes, le montant de l’acompte (100€) sera bien déduit au fur et à mesure des avancements, évitant ainsi de sur-facturer le client.

### Déduire un acompte dans Vertuoza

1. S’assurer que la facture d’acompte est bien comptabilisée et liée au chantier : elle est prise en compte dans le récapitulatif de la facturation.

![](https://downloads.intercomcdn.eu/i/o/13057146/afffe6e99efdeb6ccd07f68c/banniere.png?expires=1788620400&signature=e5decc7427a6031835e916184f9928bd88c62b244ea6216811940649fcf9a018&req=0dZvwF%2F7qDFk2hL085ZhoZja6O8s8zj1BSmpR50zsSsVPdG%2BEqmUAvR4Kkrx%0Aq1leWutZo9UmY1la%0A)

1. Créer un [avancement](https://intercom-help.eu/vertuoza/fr/articles/133049-avancement). Remplir le % d’avancement globalement ou ligne par ligne

![](https://downloads.intercomcdn.eu/i/o/13057164/152fb4fa30ae14e75903c2c3/banniere+%281%29.png?expires=1788620400&signature=b50a93357130bc8d58922b01095c367ca48e4375e3e87ba8cbde0fc3d18721a5&req=0dZvwF%2F7qjNk2hL085ZhoanqITItW0RWzEI93NucPvQByz97ySetVwGHc8iP%0AioYOLI0EFpu8kzJk%0A)

On voit bien que les 30% d’avancement se basent sur la totalité du projet, et n’excluent pas les 100€ déjà facturés. Il faut donc les déduire manuellement.

1. Descendre dans le tableau “Déduction des acomptes” et renseigner le champ % avec le même pourcentage, ici, 30%.

![](https://downloads.intercomcdn.eu/i/o/13057168/6aae856cd7165b23c4a1f17e/banniere+%282%29.png?expires=1788620400&signature=19da2c3bdd5dabc861e48c1017664a385b4f006c097715a738ef8c297c6fdddb&req=0dZvwF%2F7qj9k2hL085Zhod0JKSilS5bWWNnhQfJZT12QfOk2aycpTMiTyDwV%0AtwK6MDop6bG%2Fx7vb%0A)

1. Générer la facture à partir de l’avancement en cliquant sur les options “…” de l’avancement
2. Soumettre l’avancement, puis l’accepter suite à l’accord du client
3. Refaire la même manipulation à chaque avancement.

### Résumé : Facturation via avancement, avec ou sans déduction de l’acompte ?

![](https://downloads.intercomcdn.eu/i/o/13057181/fc51f16176c61ffa8bcfa297/banniere+%283%29.png?expires=1788620400&signature=7962ace79b049ab44784c697b6c50e7dce83b6591e5c57c7ae7400a614aaa3fd&req=0dZvwF%2F7pDZk2hL085ZhoZPW9mG50nV%2Fe%2F6O%2F55X3%2Fwod%2FqlfMhLcfTqjmhh%0AJeW9%2FZBkLiuwyuX0%0A)

Mis a jour le : 02/09/2026
