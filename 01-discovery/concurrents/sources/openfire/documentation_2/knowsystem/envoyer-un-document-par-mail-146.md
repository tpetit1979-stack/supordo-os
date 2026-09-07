---
url: https://documentation.openfire.fr/knowsystem/envoyer-un-document-par-mail-146
url_finale: https://documentation.openfire.fr/knowsystem/envoyer-un-document-par-mail-146
date_collecte: 2026-09-06
destination: documentation_2
---

Une fois un devis, une commande ou une facture sauvegardé, vous avez la possibilité de l'envoyer par mail.

Attention: Cela nécessite un paramétrage spécifique permettant à votre base OpenFire d'utiliser votre serveur de messagerie.   Plus d'information sur le __paramétrage d'un serveur mail__ 

## Envoyer un document

Le bouton Envoyer par email permet d'envoyer automatiquement un courriel à votre client avec le devis, le bon de commande, ou la facture en pièce jointe.

Le modèle de mail s’affiche alors: 

Depuis cette vue, vous pouvez notamment : 

- Ajouter des destinataires,
- Modifier le corps du mail à envoyer,
- Ajouter d’autres pièces jointes.


Vous pouvez régler le corps du message avant de l'envoyer et même l'enregistrer comme modèle si vous souhaitez le réutiliser.

Le choix du modèle peut être affiné dans le menu Utiliser un modèle .

Gestion des Destinataires:

Par défaut, les destinataires de l’email sont les abonnées aux documents, et le client est automatiquement ajouté comme abonné du document.

Pour ne pas envoyer un mail à un abonné, il faut le supprimer préalablement à l’envoi du mail

## Accès aux courriels et renvoi mails en erreur

Vous avez la possiblité de consulter les mails envoyés, et de renvoyer les mails en erreur depuis OpenFire.

Pour cela, il faut passer en mode développeur, comme pour le paramétrage du mot de passe de l'adresse mail, puis vous rendre dans le menu **Configuration > Technique > Courriels** :

Pour chaque courriel, un état est attribué en fonction du résultat de l’envoi :

- Envoyé par email
- Echec de l’envoi (en rouge dans la liste)

Vous pouvez donc utiliser le filtre de recherche *Echec* afin de n'avoir à l'écran que les mails en erreur.

En cas d’anomalie, pour chaque email, les raisons de l’échec sont détaillées dans l’onglet « raison de l’échec ».:

Une fois l’anomalie corrigée, et pour chaque mails en erreur, vous avez alors la possibilité de relancer l'envoi en cliquant sur le symbole de la flèche verte :

Puis en cliquant sur l'icone Envoyer (icone en forme d'avion en papier):

A Savoir: Les courriels envoyés ne sont listés dans ce menu que si la fonction de suppression automatique n'est pas cochée au niveau du modèle d’email :