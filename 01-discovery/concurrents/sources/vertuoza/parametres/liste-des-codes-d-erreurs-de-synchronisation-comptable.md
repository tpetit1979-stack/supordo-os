---
source: https://intercom-help.eu/vertuoza/fr/articles/148196-liste-des-codes-d-erreurs-de-synchronisation-comptable
categorie: Paramètres
titre: Liste des codes d'erreurs de synchronisation comptable
date_recuperation: 2026-09-05
---

# Liste des codes d'erreurs de synchronisation comptable

Si vous n'avez pas encore fait le paramètrage, [rendez-vous ici](https://intercom-help.eu/vertuoza/fr/articles/522539-guide-de-configuration-de-la-synchronisation-comptable)

**Copiez le code d'erreur affichez dans l'historique de votre facture et recherchez-le (CTRL + F ou cmd + F) dans la liste ci-dessous.** Si la solution n'est pas clair, contactez notre support.

| Code d'erreur | Description | Solution |
| --- | --- | --- |
| INTERNAL_SERVER_ERROR | Erreur technique interne du serveur | Si vous avez un agent local, vérifiez qu'il est en ligne. Vérifiez que le setup a été totalement réalisé. Réessayez dans une heure et si ça ne fonctionne toujours pas, contactez notre support |
| MISSING_VAT_CODE | Un code TVA n'est pas configuré ou incorrect | Les codes TVA ajoutés dans le paramétrage ne sont pas bons ou incomplets. Ouvrez votre facture en erreur, regardez le taux de TVA utilisé. Vérifiez le mapping des codes TVA dans votre [paramétrage](https://intercom-help.eu/vertuoza/fr/articles/522539-guide-de-configuration-de-la-synchronisation-comptable#h_dff76839d0) |
| ERROR_INVOICE_NUMBER_ALREADY_USED | Ce numéro de facture existe déjà | Une facture avec ce même numéro existe déjà dans votre logiciel comptable, vérifiez dans celui-ci. Si la facture a déjà été synchronisée, marquez-la comme synchronisée ([plus d'info](https://intercom-help.eu/vertuoza/fr/articles/522564-envoyer-les-factures-vers-le-logiciel-comptable#)) |
| MISSING_WORKSITE_EXTERNAL_ID | L'identifiant comptable du chantier est manquant | Vous avez activé les analytiques mais vous n'avez pas mis de code chantier pour tous les chantiers. Ajoutez un identifiant comptable dans la fiche chantier : Ouvrez le chantier et cliquez sur Éditer dans l'onglet "Tableau de bord". Là vous avez un champ "Identifiant comptable". Celui-ci est vide ou ne correspond pas à l'analytique de votre logiciel comptable ([plus d'info](https://intercom-help.eu/vertuoza/fr/articles/522539-guide-de-configuration-de-la-synchronisation-comptable#)) |
| UNKNOWN_ERROR | Erreur inconnue | Si vous avez un agent local, vérifiez qu'il est en ligne. Vérifiez que le setup a été totalement réalisé. Réessayez dans une heure et si ça ne fonctionne toujours pas, contactez notre support |
| ERROR_CONFIGURATION_LOCALAGENT | Impossible de se connecter à l'agent local | Vérifiez ou réinstallez l'agent local lié à votre logiciel comptable |
| DUPLICATE_INVOICE | Cette facture existe déjà | Notre système détecte si une facture existe déjà dans votre logiciel comptable. Veuillez vérifier dans votre logiciel comptable et si c'est le cas, marquez celle-ci comme synchronisée |
| ERROR_PARTNER_NOT_FOUND | Le client/fournisseur n'existe pas | 2 CAS :   - Les coordonnées du client de facturation sont des coordonnées manuelles (du texte). Il faut alors vérifier que le nom de ce client dans la facture est identique à celui dans votre logiciel comptable.  - Le client de facturation est un contact ou une entreprise. Il faut alors vérifier que l'identifiant comptable est bien indiqué sur la fiche contact/entreprise et que celui-ci existe bien dans votre logiciel comptable.   Vous pouvez obtenir la liste de tous les nom/identifiants de votre logiciel comptable auprès de notre support. |
| ERROR_INVALID_FIELD_FORMAT_JOURNAL_ID | Le format de l'ID journal n'est pas valide | Erreur de paramétrage. Vous pouvez obtenir la liste des codes des journaux auprès de notre support. Consultez notre article sur le [paramétrage](https://intercom-help.eu/vertuoza/fr/articles/522539-guide-de-configuration-de-la-synchronisation-comptable#) |
| ERROR_TAX_CODE_NOT_FOUND | Le code TVA n'existe pas | Les codes TVA ajoutés dans le paramétrage ne sont pas bons ou incomplets. Ouvrez votre facture en erreur, regardez le taux de TVA utilisé. Vérifiez le mapping des codes TVA dans votre [paramétrage](https://intercom-help.eu/vertuoza/fr/articles/522539-guide-de-configuration-de-la-synchronisation-comptable#h_dff76839d0) |
| ERROR_JOURNAL_NOT_FOUND | Le journal n'existe pas | Erreur de paramétrage. Vous pouvez obtenir la liste des codes des journaux auprès de notre support. Consultez notre article sur le [paramétrage](https://intercom-help.eu/vertuoza/fr/articles/522539-guide-de-configuration-de-la-synchronisation-comptable#) |
| ERROR_INVALID_BODY | Un champ dans votre requête est invalide | Veuillez contacter notre support, vous ne pouvez rien faire pour cette erreur |
| ERROR_COMPANY_NOT_FOUND | La société n'existe pas dans le logiciel comptable | Problème de paramétrage, veuillez contacter notre support |
| ERROR_JOURNAL_ALREADY_OPEN | Le journal est déjà ouvert | Fermez d'abord le journal avant de créer l'écriture. Contactez votre comptable pour fermer le journal |
| VALIDATION_ERROR | Erreur de validation des données | Veuillez contacter notre support, vous ne pouvez rien faire pour cette erreur |
| ERROR_LINE_AMOUNTS_DO_NOT_MATCH | Les montants d'une ligne sont incohérents | Veuillez contacter notre support, vous ne pouvez rien faire pour cette erreur |
| ERROR_CONNECTOR_AUTHENTICATION | Le mot de passe ou identifiant du logiciel comptable est incorrect | Reconnectez-vous au logiciel comptable avec les bons identifiants. Consultez notre article sur le [paramétrage](https://intercom-help.eu/vertuoza/fr/articles/522539-guide-de-configuration-de-la-synchronisation-comptable#) |
| ERROR_ACCOUNT_NUMBER_NOT_FOUND | Le compte général n'existe pas | Erreur de paramétrage. Vous pouvez obtenir la liste des comptes auprès de notre support. Consultez notre article sur le [paramétrage](https://intercom-help.eu/vertuoza/fr/articles/522539-guide-de-configuration-de-la-synchronisation-comptable#) |
| ERROR_INVALID_VAT_FORMAT | Le numéro de TVA n'est pas au bon format | Utilisez le format sans espaces ni points (ex: BE0784930037) |
| ERROR_PARTNER_ALREADY_EXISTS | Ce client/fournisseur existe déjà | 2 CAS :   - Les coordonnées du client de facturation sont des coordonnées manuelles (du texte). Il faut alors vérifier que le nom de ce client dans la facture est identique à celui dans votre logiciel comptable.  - Le client de facturation est un contact ou une entreprise. Il faut alors vérifier que l'identifiant comptable est bien indiqué sur la fiche contact/entreprise et que celui-ci existe bien dans votre logiciel comptable.   Vous pouvez obtenir la liste de tous les nom/identifiants de votre logiciel comptable auprès de notre support. |
| ERROR_API_RESOURCE_NOT_FOUND | L'action n'est pas supportée par votre logiciel | L'intégration ne permet pas de réaliser l'action pour votre logiciel comptable. Certains logiciels comptables ne permettent pas l'envoi ou la réception des factures ([plus d'info](https://intercom-help.eu/vertuoza/fr/articles/522531-synchronisation-comptable-vue-d-ensemble#)) ou bien la gestion des analytiques ([plus d'info](https://intercom-help.eu/vertuoza/fr/articles/522539-guide-de-configuration-de-la-synchronisation-comptable#)). |
| ERROR_UNEXPECTED | Erreur inattendue liée aux données | Si vous avez un agent local, vérifiez qu'il est en ligne. Vérifiez que le setup a été totalement réalisé. Réessayez dans une heure et si ça ne fonctionne toujours pas, contactez notre support |
| ERROR_INVALID_FIELD_FORMAT_INVOICE_NUMBER | Le numéro de facture est trop long ou invalide | Certains logiciels ont des limitations dans le nombre de chiffres du numéro. Ouvrez la facture et diminuez le nombre de caractères de votre numéro de facture |
| ERROR_PARTNER_ALREAY_EXIST | Ce client/fournisseur existe déjà | 2 CAS :   - Les coordonnées du client de facturation sont des coordonnées manuelles (du texte). Il faut alors vérifier que le nom de ce client dans la facture est identique à celui dans votre logiciel comptable.  - Le client de facturation est un contact ou une entreprise. Il faut alors vérifier que l'identifiant comptable est bien indiqué sur la fiche contact/entreprise et que celui-ci existe bien dans votre logiciel comptable.   Vous pouvez obtenir la liste de tous les nom/identifiants de votre logiciel comptable auprès de notre support. |
| UNEXEPECTED_SAGE100FR_ERROR | Erreur inattendue Sage 100 FR | Contactez le support pour identifier le problème |
| UNEXPECTED_PENNYLANEV2_ERROR | Erreur inattendue Pennylane | Contactez le support pour identifier le problème |
| ERROR_INTERNAL_ERROR | Erreur technique interne | Si vous avez un agent local, vérifiez qu'il est en ligne. Vérifiez que le setup a été totalement réalisé. Réessayez dans une heure et si ça ne fonctionne toujours pas, contactez notre support |
| ERROR_TAX_CODE_NOT_GOOD_SCOPE | Ce code TVA ne peut pas être utilisé ici | Utilisez un code TVA vente pour les ventes, achat pour les achats ([plus d'info](https://intercom-help.eu/vertuoza/fr/articles/522539-guide-de-configuration-de-la-synchronisation-comptable#h_dff76839d0)). |
| ERROR_NO_ACTIVE_CONNECTION | Aucune connexion active n'existe | Activez et configurez correctement la synchronisation |
| UNEXEPECTED_BOB_ERROR | Erreur inattendue Bob 50 | Contactez le support pour identifier le problème |
| ERROR_PARTNER_ALREAY_EXISTS | Ce client/fournisseur existe déjà | 2 CAS :   - Les coordonnées du client de facturation sont des coordonnées manuelles (du texte). Il faut alors vérifier que le nom de ce client dans la facture est identique à celui dans votre logiciel comptable.  - Le client de facturation est un contact ou une entreprise. Il faut alors vérifier que l'identifiant comptable est bien indiqué sur la fiche contact/entreprise et que celui-ci existe bien dans votre logiciel comptable.   Vous pouvez obtenir la liste de tous les nom/identifiants de votre logiciel comptable auprès de notre support. |
| UNEXEPECTED_WINBOOKS_ERROR | Erreur inattendue Winbooks | Contactez le support pour identifier le problème |
| ERROR_BACKEND_FORBIDDEN | Erreur technique | Veuillez réessayer et contactez le support si le problème persiste |
| ERROR_CONFIGURATION_CONNECTION | Problème dans la configuration de la connexion | Vérifiez ou recommencez la connexion à votre logiciel comptable |
| UNEXPECTED_EXACTONLINEBE_ERROR | Erreur inattendue Exact Online BE | Contactez le support pour identifier le problème |
| ERROR_PERIOD_CLOSED | La période comptable est clôturée | Rouvrez la période ou utilisez une autre date |
| ERROR_MISSING_INVOICE_NUMBER | Le numéro de facture est manquant | Ajoutez un numéro de facture |
| UNEXPECTED_EXACTONLINENL_ERROR | Erreur inattendue Exact Online NL | Contactez le support pour identifier le problème |
| ERROR_NEGATIVE_INVOICE | Une facture ne peut pas être négative | Utilisez une note de crédit au lieu d'une facture négative |
| MISSING_DATA | Des données obligatoires sont manquantes | Vérifiez que tous les champs obligatoires de la facture sont remplis |
| ERROR_BOOKYEAR_NOT_FOUND | Aucun exercice comptable pour cette date | Créez l'exercice comptable incluant cette date |
| ERROR_ANALYTIC_ACCOUNTING_NOT_ACTIVE | La comptabilité analytique n'est pas activée | Activez la comptabilité analytique dans le logiciel |
| ERROR_INVALID_PATH_PARAMETER | Erreur technique | Veuillez réessayer et contactez le support si le problème persiste |
| ERROR_ZERO_INVOICE | Le montant de la facture ne peut pas être zéro | Créez une facture avec un montant supérieur à zéro |
| ERROR_GATEWAY_TIMEOUT | Le logiciel ne répond pas | Veuillez réessayer et contactez le support si le problème persiste |
| UNEXPECTED_ODOO_ERROR | Erreur inattendue Odoo | Contactez le support pour identifier le problème |
| ERROR_MISSING_LAST_NAME | Le nom est obligatoire pour une personne physique | Ajoutez le nom du client/fournisseur |
| ERROR_TAX_RATE_NOT_CORRESPONDING | Le taux de TVA ne correspond pas au code TVA | Utilisez un code TVA avec le bon taux ou modifiez le mapping |
| ERROR_JOURNAL_NOT_GOOD_SCOPE | Le journal ne peut pas être utilisé pour ce type | Utilisez un journal vente pour les ventes, achat pour les achats |
| ERROR_UNKNOWN | Erreur inconnue | Veuillez réessayer et contactez le support si le problème persiste |
| ERR0R_INVOICE_CREATION | Erreur lors de la création de la facture | Contactez le support pour identifier le problème |
| UNEXPECTED_YUKI_ERROR | Erreur inattendue Yuki | Contactez le support pour identifier le problème |

### 

Mis a jour le : 02/09/2026
