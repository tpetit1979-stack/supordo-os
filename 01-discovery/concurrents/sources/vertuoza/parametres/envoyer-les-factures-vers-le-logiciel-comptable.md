---
source: https://intercom-help.eu/vertuoza/fr/articles/522564-envoyer-les-factures-vers-le-logiciel-comptable
categorie: Paramètres
titre: Envoyer les factures vers le logiciel comptable
date_recuperation: 2026-09-05
---

# Envoyer les factures vers le logiciel comptable

## 

Si vous n'avez pas encore fait le paramètrage, [rendez-vous ici](https://intercom-help.eu/vertuoza/fr/articles/522539-guide-de-configuration-de-la-synchronisation-comptable)


La synchronisation fonctionne de manière identique pour les factures clients, les notes de crédit (avoirs) et les factures fournisseurs.

**Conditions** :
- Les factures clients et notes de crédit doivent être **comptabilisées**
- Les factures fournisseurs doivent être **acceptées**


Un nouveau statut "Statut compta" apparaît dans vos listes de factures avec quatre états possibles :

- **À envoyer** : La facture doit être envoyée vers la comptabilité
- **Envoi en cours** : La facture est en cours d'envoi (attendez quelques secondes)
- **Envoyé** : La facture a été envoyée avec succès dans votre logiciel comptable
- **Erreur** : La facture n'a pas pu être synchronisée (voir section résolution d'erreurs)


[Vidéo]()


Étape 1 : Accéder à la liste des factures
Allez dans la liste correspondant au type de document à synchroniser : Factures clients, Notes de crédit ou Factures fournisseurs.

Étape 2 : Filtrer les factures à envoyer
Utilisez le filtre "Statut compta" pour afficher uniquement les factures "**À envoyer**". Cela vous permet de voir rapidement ce qui reste à synchroniser.

Étape 3 : Sélectionner et envoyer
1. Sélectionnez les factures que vous souhaitez synchroniser
2. Utilisez l'action groupée "Envoyer à la comptabilité"
3. Le statut passe à "**Envoi en cours**" puis "**Envoyé**" après quelques secondes


Si une facture affiche le statut "**Erreur**", pas de panique. Une information détaillée est disponible dans l'historique de la facture.

**Pour consulter l'erreur** : Cliquez sur le bouton "**Détails**" sous le statut compta de la facture en erreur. Vous verrez le message d'erreur et pourrez identifier le problème.

➡️ Consultez notre article [Comprendre et résoudre les erreurs de synchronisation](https://intercom-help.eu/vertuoza/fr/articles/148196-resoudre-les-erreurs-de-synchronisation) pour plus de détails sur les erreurs courantes et leurs solutions.


L'action "**Marquer comme synchronisé**" vous permet de marquer manuellement des factures comme déjà présentes dans votre comptabilité, sans les envoyer.

**Utilisez cette fonction dans deux cas :**
1. **Lors du démarrage** : Si vous venez de configurer la synchronisation et que votre comptable a déjà encodé les factures passées, marquez-les comme synchronisées pour éviter les doublons.
2. **Encodage manuel** : Si vous avez une erreur et préférez encoder la facture manuellement dans votre logiciel comptable, marquez-la comme synchronisée pour qu'elle n'apparaisse plus dans les factures "À envoyer".
De cette manière, le statut compta reflète toujours précisément les factures qu'il reste à envoyer vers le logiciel comptable.


Le fonctionnement est strictement identique pour les notes de crédit et les factures fournisseurs. Suivez les mêmes étapes depuis leurs listes respectives.

💡 Pour les factures fournisseurs, vous avez également la possibilité de les **recevoir** depuis votre logiciel comptable. Consultez l'article [Synchroniser vos factures fournisseurs](https://intercom-help.eu/vertuoza/fr/articles/522567-synchroniser-vos-factures-fournisseurs-bidirectionnel) pour en savoir plus.


### 

Mis a jour le : 08/01/2026
