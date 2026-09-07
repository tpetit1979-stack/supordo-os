---
url: https://documentation.openfire.fr/knowsystem/facturer-un-contrat-309
url_finale: https://documentation.openfire.fr/knowsystem/facturer-un-contrat-309
date_collecte: 2026-09-06
destination: documentation_2
---

La création des factures se fait depuis le contrat.

Les lignes de contrat facturables apparaissent en bleu sur le contrat.

Une ligne de contrat est facturable y compris si elle n'a qu'une exception de facturation.

En cliquant sur “Créer les factures”, cela ouvre l'assistant de facturation.

Période de facturation: le logiciel prendra toutes les lignes dont la date de facturation prévisionnelle des lignes de contrat est inférieure ou égale à la date précisée dans ce champ.




Date de facturation: vous permet d’indiquer quelle date sera mise sur les factures générées



**Date du jour**: toutes les factures brouillon auront pour date de facturation la date du jour.

**Manuelle**: toutes les factures brouillon auront pour date de facturation la date spécifiée.

**Calculée**: le système génère des factures à la date de prochaine facturation théorique calculée par le contrat.

Exemple un contrat en facturation annuelle à échoir : la prochaine facture est au 01/01 de l'année suivante. La facture sera donc générée à cette date.

Si la date de facturation sélectionnée est

**date du jour**ou

**manuelle**, le système pourra regrouper les articles sur une même facture en fonction de l'option "

**Regrouper la facturation**" présente sur les lignes du contrat.

En date de facturation "

**Calculée**", le système générera autant de factures que de dates de facturation prévisionnelles.

#### Lignes à facturer

En fonction des inforations précédentes, il faut cliquer sur “

Calculer” pour obtenir les lignes qui seront facturées.
Il est possible d’exclure des lignes en les décochant “A facturer” ou en cliquant sur la poubelle.

#### Exceptions

Sur le même principe, il faut calculer les lignes d’exceptions à facturer.

**Remarque**: si la facture générée en brouillon est supprimée, le système à date ne sait pas réactiver les exceptions de facturation.

Il faudra donc aller mettre à 0 la quantité facturée de la ligne d'exception pour que le système la rende facturable dans la prochaine facture.




Vous pouvez enfin Générer les factures

## Depuis la liste des contrats

En sélectionnant plusieurs contrats, vous avez la possibilité de les facturer via le menu Action > Facturation multiple

L’assistant de facturation est dans ce cas limité à la période de facturation et la date de facturation.

Toutes les lignes de contrat et exceptions considérées comme facturables seront prises en compte dans les factures brouillon générées.