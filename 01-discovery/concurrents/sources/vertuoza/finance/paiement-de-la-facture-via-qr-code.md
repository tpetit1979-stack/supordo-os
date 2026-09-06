---
source: https://intercom-help.eu/vertuoza/fr/articles/254753-paiement-de-la-facture-via-qr-code
categorie: Finance
titre: Paiement de la facture via QR code
date_recuperation: 2026-09-05
---

# Paiement de la facture via QR code

## **Qu’est-ce que le paiement de factures via QR Code ?**

Le paiement par QR Code est une fonctionnalité qui vous permet d’envoyer vos factures au format digital. Vos clients peuvent ainsi les consulter en ligne et les payer simplement en scannant le QR Code affiché avec leur application bancaire.

Lorsque le client scanne le QR Code **avec son application bancaire**, les champs du virement sont automatiquement préremplis :

- Montant
- IBAN
- Communication structurée si vous avec activé l'option "**code VCS" **dans **Paramètres > Factures > Préférences **OU la référence de la facture si l'option "code VCS" est désactivée.

Cela facilite et accélère le processus de paiement.

## Comment utiliser le paiement par QR Code ?

1. Activer le paiement de la facture via QR Code

Pour activer cette fonctionnalité lors de l’envoi de votre facture via Vertuoza :

- Cochez l’option « Paiement via QR Code » en haut de la page.
- Insérez la balise **[LINK_FACTURE]** dans l’e-mail. Cette balise génère un lien permettant au client de consulter la facture et de payer en ligne.

> Le modèle de document utilisé est celui défini par défaut dans les paramètres > Documents > Préférences. Il n'est plus possible de définir un modèle lors de l'envoi par email car le lien de ce document sera toujours le même pour cette facture, il n'est pas différent d'un envoi à un autre.

2. L’expérience de paiement pour votre client

Voici les étapes à suivre pour régler une facture via QR Code :

1. **Consulter la facture** : En cliquant sur le lien dans l'e-mail, le client accède à la facture en ligne.
2. **Cliquer sur "Payer facture"** : Le client clique sur ce bouton en haut à droite de l’écran.
3. **Scanner le QR Code** : En scannant le QR Code avec son application bancaire, les informations nécessaires (montant, IBAN, communication) sont automatiquement remplies.
4. **Finaliser le paiement** : Le client vérifie les informations et valide le virement dans son application bancaire.
5. **Télécharger la facture** : Si le client souhaite conserver une copie, il peut la télécharger en cliquant sur "Télécharger facture".

3. Notification

Vous recevrez une notification lorsque le client ouvrira votre facture via le lien. Toutefois, vous ne recevrez pas de notification si il a utilisé le QR code car nous n'avons pas de moyen de le savoir. 

Une fois le paiement effectué, l’argent sera ajouté sur votre compte comme pour un virement classique.  **Il vous sera toujours nécessaire d'indiquer la facture comme payé via l'action manuelle ou via la synchronisation des paiements avec votre compte bancaire ([plus d'info ici](https://intercom-help.eu/vertuoza/fr/articles/132174-synchronisation-des-paiements)).**


Le modèle d'email par défaut contient déjà la balise **[LINK_FACTURE]**. Si vous avez créé un modèle personnalisé, assurez-vous d'y inclure cette balise pour permettre à vos clients de consulter et payer la facture en ligne.
[Plus d'info ici](https://intercom-help.eu/vertuoza/fr/articles/132097-modeles-d-e-mails)

> Exemple d’email :
> **Objet** : Votre facture [N°FACTURE] est disponible
> Cher(e) [CIVILITE_CLIENT] [NOM_CLIENT],
> Veuillez trouver ci-joint la facture demandée.
> Si vous avez des questions, n’hésitez pas à contacter votre gestionnaire [NOM_GESTIONNAIRE] à l’adresse suivante : [MAIL_GESTIONNAIRE].
> Vous pouvez consulter et payer cette facture en cliquant sur ce lien : [LINK_FACTURE]
> Merci et bonne journée,
> Bien à vous,



### 

Mis a jour le : 19/02/2025
