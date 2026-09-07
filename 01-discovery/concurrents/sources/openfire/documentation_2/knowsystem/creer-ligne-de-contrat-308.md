---
url: https://documentation.openfire.fr/knowsystem/creer-ligne-de-contrat-308
url_finale: https://documentation.openfire.fr/knowsystem/creer-ligne-de-contrat-308
date_collecte: 2026-09-06
destination: documentation_2
---

***__Accès pour la création__*** : **Interventions>Interventions>Contrats**

La création d’une ligne de contrat peut uniquement se faire depuis un contrat.

A partir du contrat, il faut cliquer sur Ajouter un élément :

Par défaut, la ligne de contrat est en état Brouillon et les informations enregistrées dans le contrat sont reprises dans la ligne de contrat.

Certains paramètres peuvent être modifiés dans la  ligne de contrat.

Dans le pavé informations client, vous trouverez les champs suivants en contrat simple :

- Client payeur: il reprend le porteur du contrat auquel la ligne est rattachée. Cette donnée n'est pas modifiable.

- Code magasin : (champ supplémentaire dans le cas d'un contrat avancé) il est repris depuis la fiche contact du site d’intervention

Vous trouverez ces champs supplémentaires en contrat Avancé :

- Prestataire : ce champ n’est pas obligatoire. Il ne vaut que dans le cas d’une sous-traitance du contrat

## Onglet facturation

Cet onglet est uniquement disponible sur un type de contrat avancé.

Il permet de définir les prestations à facturer. 

Pour les types de facturation autres que "à la prestation", le montant total sera divisé selon la fréquence de facturation.

exemple :

pour une facturation mensuelle, mettre 12 prestations

pour une facturation annuelle : mettre 1 article type forfait quel que soit le nombre de visites.


On retrouve également les éléments saisis sur le contrat. Ils sont modifiables.

Détails facturation: cocher cette case permet de visualiser les éléments suivants:

- Fréquence de facturation
- Type de facturation
- Position fiscale
- Période de révision

Dans ce cas, il faut que toutes les lignes concernées soient cochées "Regrouper la facturation"

Les prestations sur lesquelles reposent la facturation seront saisies à ce niveau.

Exceptions de facturation

Le principe des exceptions de facturation est de pouvoir intégrer automatiquement une facturation exceptionnelle à venir, en plus ou en moins:

  - C’est un complément de facturation lié à une prestation spécifique réalisée en plus

ou

  - une remise exceptionnelle liée par exemple à l'annulation d'une visite relativement à ce qui était prévu.

Les exceptions vous permettent ainsi, de ne pas modifier les lignes de références, mais simplement de traiter l'exception à côté.

## Onglet Planification

Il est possible de sélectionner un Modèle d’intervention. [Plus d'informations](https://documentation.openfire.fr/knowsystem/modeles-dintervention-73)

Tâche : une seule tâche peut être associée à ligne de contrat.

Si vous effectuez plusieurs prestations en même temps (entretien chaud et froid), il faut créer la tâche mixte correspondante

Fréquence : nombre d’interventions et période de récurrence.

Mois de visite : Mois pour lesquels un rendez vous devra être réalisé.

Nombre de visites : il est calculé automatiquement selon la fréquence et les mois de visites saisis.

Il détermine le nombre de demandes d’intervention qui seront créés.

Notes : descriptif qui sera repris sur les DI et les RDV

## Onglet équipement

Si un parc installé est renseigné sur le site d’intervention, il sera repris automatiquement.

Un seul parc installé peut être défini par ligne de contrat

Il sera repris dans les demandes d’intervention et dans les RDV

## Onglet Suivi

Les demandes d'intervention générées sont visibles ici, avec leur état de planification et le cas échéant, les rendez vous liés et les rapports d'intervention.

## Activer les lignes

Cette opération permet de valider la ligne en brouillon. 

Depuis le contrat, il est ensuite possible de générer les DI puis les factures.

 

## Modifier une ligne

##### Ligne en brouillon

Une ligne de contrat est totalement modifiable si elle est en brouillon. 

Cela concerne notamment l'adresse d'intervention, le type et la fréquence de facturation


Il est possible de repasser une ligne dans l’état “brouillon” si:

- aucune facture ne lui est rattachée

et si

- aucun RDV d’intervention est rattaché à une demande d’intervention de la ligne

##### Ligne activée

##### **Onglet facturation** 

Vous pouvez modifier les éléments de facturation (articles, exceptions, position fiscale…)

Au niveau des articles, les quantités, coût et prix de vente sont modifiables.

##### Onglet Planification

La fréquence et les mois de visite sont modifiables

## Générer les DI

La génération des DI se fait depuis le contrat.

 Plus d'information sur la [Génération des DI](https://documentation.openfire.fr/knowsystem/contrats-302#table_of_content_heading_1707749377267_2197)

## Planification

Les DI liées à une ligne peuvent être visualisées depuis le smartbouton "Planification"

Sur la vue liste, vous avez notamment le numéro et la date de la facture associée à la DI qui sont indiqués.

Ces informations sont également accessibles depuis la Di elle même, ainsi que le numéro de contrat et la ligne de contrat associés.

**Remarque**: Pour les contrats à la prestation, la date du RDV d'intervention doit se situer dans l'intervalle de dates de la DI, pour que la ligne de contrat associée soit facturable.

## RDV

Les rendez vous doivent être générés depuis la DI.

La DI, le contrat et la ligne de contrat liés sont repris.

## Dupliquer une ligne

Afin de permettre de créer plus rapidement des contrats multi-lignes, vous avez la possibilité de dupliquer une ligne de contrat.

A date, cette duplication est uniquement possible au sein d’un même contrat.

Cette action est possible directement depuis la  ligne de contrat via le menu **Action > Dupliquer**

La ligne dupliquée peut ensuite être modifiée dans les mêmes conditions qu'une nouvelle ligne.