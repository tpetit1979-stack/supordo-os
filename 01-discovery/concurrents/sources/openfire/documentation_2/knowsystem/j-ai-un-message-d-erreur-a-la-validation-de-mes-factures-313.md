---
url: https://documentation.openfire.fr/knowsystem/j-ai-un-message-d-erreur-a-la-validation-de-mes-factures-313
url_finale: https://documentation.openfire.fr/knowsystem/j-ai-un-message-d-erreur-a-la-validation-de-mes-factures-313
date_collecte: 2026-09-06
destination: documentation_2
---

Les factures émises par une entreprise doivent être rangées chronologiquement dans un livre comptable. 

Les dates d'émissions et la numérotation des factures doivent se suivre et être cohérentes.

Les factures doivent être numérotées à l'aide d'un numéro unique basé sur une séquence chronologique continue, sans rupture. Cela implique que 2 factures ne peuvent pas avoir le même numéro.

Pour assurer cette chronologie, lors de la validation d'une facture, Openfire vérifie qu'aucune facture validée ou en brouillon existe avec une date inférieure à la date de facturation de la facture que vous souhaitez valider.

Si une facture avec une date antérieure est trouvée, vous obtenez ce message d'erreur

Il faut alors :

- Soit modifier la date de facturation de votre facture actuelle si des factures validées ont une date postérieure
- Soit modifier les dates de facturations de vos factures brouillon.

Il faut alors vider la zone date de facturation de la facture.