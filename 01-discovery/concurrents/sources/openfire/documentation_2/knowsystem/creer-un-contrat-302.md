---
url: https://documentation.openfire.fr/knowsystem/creer-un-contrat-302
url_finale: https://documentation.openfire.fr/knowsystem/creer-un-contrat-302
date_collecte: 2026-09-06
destination: documentation_2
---

Le module Contrat vous permet de gérer une planification récurrente à laquelle est associée une facturation récurrente.**__Accès__** : **Ventes**>**Ventes**>**Contrats / Lignes de contrats** ou **Interventions**>**Contrats / Lignes de contrats**

Si vous souhaitez plus d'informations sur les contrats et la mise en place du module, contactez support@openfire.fr

Vous pourrez:

- Facturer une prestation récurrente
- Planifier une prestation récurrente
- Renouveler automatiquement le contrat

## Créer un contrat

La référence du contrat peut être définie manuellement ou de manière automatique.

Ce paramètre se trouve dans le menu **Interventions** > **Configuration** > partie **Contrats**

## Informations clients

Ici, vous pouvez renseigner le porteur du contrat en identifiant le client payeur, c’est à dire celui à qui seront adressées les factures.

La date de souscription correspond à la date de signature du contrat.

## Validité

La période du contrat détermine la période en cours du contrat.

 Elle est gérée automatiquement par le logiciel et ne peut pas être modifiée.

La date de début de période de validité détermine la date à partir de laquelle le contrat prend effet.

La date de fin détermine quand le contrat s’arrête. Celle-ci sera renseignée s'il n'y a pas renouvellement automatique. Par défaut, la case "Renouvellement automatique" est cochée, la date de fin n'est donc pas notée.

La période d'activité détermine la durée de la période du contrat. Actuellement, cette période est obligatoirement de 12 mois.

## Facturation

On retrouve les informations suivantes:

Type de facturation: détermine la fréquence et les dates de facturation des lignes de contrat.

- A la prestation: date du jour ou échu. 
Les factures prendront respectivement la date de l'intervention ou la date de fin de la période.
- Mensuelle, trimestrielle, semestrielle, annuelle: A échoir ou échu 
Le contrat sera facturé en début ou fin de période.

Journal : nom du journal de vente comptable dans lequel les factures seront enregistrées. 

Position fiscale : taux de TVA qui s’appliquera sur les articles à facturer.

Date de la prochaine facture : champ calculé qui reprend la prochaine date de facturation des lignes

En mode de saisie avancé, on a en plus accès à:

Conditions de règlement : qui permettent  le calcul de la date d'échéance de la facture.

Regrouper la facturation : détermine si les lignes de contrats sont facturées sur une seule facture ou sur des factures séparées, soit une facture par ligne de contrat.

Ce paramètre existe aussi dans les lignes de contrat.

Période de révision : c’est la révision de fin d’année pour corriger la facturation en fonction de la planification réelle de l’année. 

2 choix possibles: Aucune ou Dernier jour du contrat. En choisissant cette dernière option, cela vous permet de corriger la facturation en fonction de la planification réelle de l’année. Sinon, il n’y aura pas de révision.

## Renouvellement

Renouvellement automatique: Cocher cette option indique si le contrat doit être renouvelé automatiquement à la fin de la période du contrat. 

Si elle n’est pas cochée, une date de fin de contrat doit être renseignée 

Indexer : Cocher cette case détermine si par défaut les lignes seront indexables. L’indexation n’est pas automatique, cette case détermine seulement si les lignes de contrat seront éligibles à l’indexation.


Lorsque le contrat est sauvegardé et donc "en cours", il faut créer les lignes de contrat.

*Pour créer la ligne de contrat, voir l'article* *Créer ligne de contrat*

## Activer les lignes

Depuis le contrat, il est possible d'activer l'ensemble des lignes du contrat.

Cette opération permet de passer les **lignes de contrat** de l'état brouillon en état validé. 

## Générer les DI

Les demandes d'interventions (DI) liées à la planification des lignes de contrats sont générées par le bouton "Générer DI".

Lorsque vous cliquez sur Générer DI, le logiciel va générer des DI en fonction des informations notées dans la planification des lignes de commande et pour la période du contrat en cours de validité.

Exemple: pour une période de 01/01/2024 au 31/12/2024, la ligne de contrat a une planification de 2 fois par an et les mois de visites concernés sont Mars et Septembre, 2 DI seront générées sur la période de 03/2024 et 09/2024.