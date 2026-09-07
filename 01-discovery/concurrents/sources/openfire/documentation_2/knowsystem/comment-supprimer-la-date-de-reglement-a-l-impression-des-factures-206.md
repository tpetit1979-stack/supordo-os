---
url: https://documentation.openfire.fr/knowsystem/comment-supprimer-la-date-de-reglement-a-l-impression-des-factures-206
url_finale: https://documentation.openfire.fr/knowsystem/comment-supprimer-la-date-de-reglement-a-l-impression-des-factures-206
date_collecte: 2026-09-06
destination: documentation_2
---

Dans **Comptabilité > Configuration > Mode de paiement**, vous accédez au paiement concerné (par exemple "Chèque").

Dans le paramètre d'affichage, le libellé inscrit sur la facture est noté dans le champ Configuration : *payé par...*

Si vous souhaitez enlever la date du paiement, il faut alors supprimer la partie la mention {format_date(object.payment_date)} :

Tous les champs proposés et que vous souhaitez ajouter sur une facture se trouvent en dessous dans la partie "exemple de variables".