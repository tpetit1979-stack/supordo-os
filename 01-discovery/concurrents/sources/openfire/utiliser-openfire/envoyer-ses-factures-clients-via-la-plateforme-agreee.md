---
source: https://support.openfire.fr/hc/fr/articles/29506789788572-Envoyer-ses-factures-clients-via-la-Plateforme-Agr%C3%A9%C3%A9e
categorie: Utiliser OpenFire
titre: Envoyer ses factures clients via la Plateforme Agréée
date_recuperation: 2026-09-05
---

# Envoyer ses factures clients via la Plateforme Agréée

Cet article vous explique comment préparer et envoyer vos factures clients au format électronique à vos clients professionnels via OpenFire et votre Plateforme Agréée (PA).

Cet article contient les sections suivantes :

- [Préparation : sélection de la ligne d'annuaire](#h_01KZPDTYWK2Z8N8RTT5BAAVDK9)

  - [Sur le devis ou bon de commande](#h_01KZPDTYWMBVAGDPFNH96XF3HT)
  - [Sur la facture client](#h_01KZPDTYWQQP9D82506VWZPCV0)
- [Méthodes d'envoi des factures clients](#h_01KZPDTYWTBTHAMKPGSB5T2VES)
- [Suivi de l'état d'envoi](#h_01KZPDTYX0W35EZVC0H6V879GM)
- [Bonnes pratiques](#h_01KZPDTYX3YGXZQ49MRYMZ59HX)

## Préparation : sélection de la ligne d'annuaire

Pour pouvoir transmettre une facture électronique à un client professionnel (B2B), vous devez associer la bonne ligne d'annuaire à son compte.

### Sur le devis ou bon de commande

1. Lors de la saisie d'un devis ou bon de commande, sélectionnez le client professionnel.
2. Dans la section **Détails client**, vérifiez le champ **Ligne d'annuaire**.
3. Si nécessaire, sélectionnez la ligne d'annuaire appropriée. 
  (La ligne par défaut définie sur la fiche du client sera appliquée automatiquement).

![](https://support.openfire.fr/hc/article_attachments/29506986920220)

### Sur la facture client

Lors de la confirmation de la commande et de la génération de la facture, la ligne d'annuaire renseignée est automatiquement transmise sur le document comptable.

![](https://support.openfire.fr/hc/article_attachments/29506928550172)

## Méthodes d'envoi des factures clients

OpenFire vous propose deux modalités pour transmettre vos factures électroniques à la Plateforme Agréée :

- **Envoi automatique (par défaut) :** OpenFire réalise un envoi regroupé de toutes vos factures validées en attente une fois par jour, durant la nuit.
- **Envoi immédiat :** Si vous souhaitez transmettre immédiatement une facture à votre client sans attendre le traitement nocturne :

  1. Ouvrir la facture validée.
  2. Repérer le bandeau d'information bleu en haut du document.
  3. Cliquer sur le lien bleu **Cliquez ici pour l'envoyer immédiatement**.

![](https://support.openfire.fr/hc/article_attachments/29506928550300)

💡Note : Dès que vous cliquez sur l'action d'envoi immédiat, la facture est transmise et le bandeau d'information bleu disparaît de l'écran.

## Suivi de l'état d'envoi

Pour vérifier la prise en charge et la livraison de votre facture chez le client :

1. Ouvrir la facture concernée dans `Comptabilité > Clients > Factures clients`.
2. Cliquer sur l'onglet **Facturation électronique**.
3. Consultez la section **ÉVÉNEMENTS** pour observer les étapes de traitement (ex : `Prise en charge`, `Envoyé`).

🚨Avertissement : Si votre client professionnel n'a pas de ligne d'annuaire valide sur la facture, l'envoi électronique échouera. Assurez-vous de la conformité de sa fiche contact.

Avant envoi :

- Le flux de facturation électronique a été créé mais n'a pas encore été transmis à la PA ; il est "à envoyer"
- Aucun événement n'est référencé

![](https://support.openfire.fr/hc/article_attachments/29676160165916)

Après envoi :

- Le flux passe à "envoyé"
- Les événements d'émission et de réception par la plateforme sont listés (après avoir synchroniser votre PA depuis le tableau de bord)

![](https://support.openfire.fr/hc/article_attachments/29676378217116)

Une fois reçue et validée par votre client :

- Le flux reste à "envoyé"
- Les différents évènements sont répertoriés, reflétant le cycle de vie de votre facture

![](https://support.openfire.fr/hc/article_attachments/29676422709276)

## Bonnes pratiques

- **Vérifier l'annuaire dès le devis :** prenez l'habitude de valider la ligne d'annuaire dès la création du devis pour éviter des blocages au moment de la facturation.
- **Privilégier l'envoi automatique :** laissez le traitement de nuit gérer vos envois quotidiens, et n'utilisez l'envoi immédiat que pour les demandes urgentes.

Mis a jour le : 25/08/2026
