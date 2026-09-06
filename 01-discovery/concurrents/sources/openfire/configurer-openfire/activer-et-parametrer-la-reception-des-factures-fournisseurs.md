---
source: https://support.openfire.fr/hc/fr/articles/29465754707100-Activer-et-param%C3%A9trer-la-r%C3%A9ception-des-factures-fournisseurs
categorie: Configurer OpenFire
titre: Activer et paramétrer la réception des factures fournisseurs
date_recuperation: 2026-09-05
---

# Activer et paramétrer la réception des factures fournisseurs

Dans le cadre de la facturation électronique, cet article vous explique comment activer la réception automatique de vos factures fournisseurs dans OpenFire. Vous découvrirez également comment configurer les événements automatiques transmis à la Plateforme Agréée pour simplifier votre gestion comptable au quotidien.

Cet article contient les sections suivantes :

- [Chemin d’accès de la fonctionnalité](#h_01KZGPSFDAFV46MEWNKMATM6F8)
- [Activer et paramétrer la réception des factures](#h_01KZGPSFDBDS1DDQD0TZ8V1890)

  - [Étape 1 : Activer l'importation des factures](#h_01KZGPSFDBNAP0BZ61TBXFABG5)
  - [Étape 2 : Comprendre le champ de date de suivi des flux](#h_01KZGPSFDEEC041G20X8N0VSMN)
  - [Étape 3 : Paramétrer les événements automatiques](#h_01KZGPSFDHWWKZ8S6R529F18YF)
- [Bonnes pratiques](#h_01KZGPSFDT4NGK2EGQPAG5HDRN)

## Chemin d’accès de la fonctionnalité

`Suivre le chemin d'accès suivant : Comptabilité > Configuration > Paramètres > Facturation électronique.`

## Activer et paramétrer la réception des factures

### Étape 1 : Activer l'importation des factures

1. Accéder au menu des paramètres via le chemin d'accès ci-dessus.
2. Cocher la case **IMPORT DES FACTURES FOURNISSEUR**.
3. Cliquer sur le bouton **Enregistrer**.

Ces paramètres contrôlent la réception et le traitement des factures fournisseurs entrantes via la plateforme agréée.

![](https://support.openfire.fr/hc/article_attachments/29465826709404)

### Étape 2 : Comprendre le champ de date de suivi des flux

Le champ **Dernière importation de flux depuis la Plateforme Agréée** indique la date et l'heure exactes du dernier flux entrant récupéré. Ce champ se met à jour automatiquement après chaque cycle d'importation.

| 💡**Note **: Lors de chaque importation, le système remonte automatiquement d'une heure par rapport à cette date. Cela permet de garantir qu'aucun document n'est manqué en cas de problème technique temporaire. Il est fortement recommandé de ne pas modifier manuellement cette valeur. |
| --- |

### Étape 3 : Paramétrer les événements automatiques

Afin de notifier la Plateforme Agréée de l'avancement du traitement de vos documents, vous pouvez automatiser l'envoi de plusieurs événements statutaires.

#### Champ : Envoi automatique de l'événement « Prise en charge »

Lorsqu'une facture fournisseur entre dans OpenFire à l'état de brouillon, cet événement signale à la plateforme que le document est bien reçu.

- **Activé** (par défaut) : l'événement est transmis immédiatement lors de l'importation de la facture.
- **Désactivé** : l'envoi de la confirmation de réception doit se faire manuellement.

#### Champ : Envoi automatique de l'événement « Approuvée »

Lorsque vous validez une facture fournisseur dans OpenFire, cet événement confirme l'acceptation de la facture.

- **Activé** (par défaut) : l'événement est transmis automatiquement dès la validation de la facture.
- **Désactivé** : la validation nécessite un envoi manuel de l'événement.

#### Champ : Envoi automatique de l'événement « Paiement envoyé »

Lorsqu'un ordre de paiement est téléversé, cet événement indique à la plateforme agréée que le règlement a été initié.

- **Activé** : l'événement est envoyé automatiquement lors du téléversement de l'ordre de paiement.
- **Désactivé** : aucun événement n'est transmis automatiquement.

| 💡**Note **: Ce paramètre est disponible uniquement lorsque le module des paiements en lot est installé sur votre base OpenFire. |
| --- |

## Bonnes pratiques

- **Conservez les envois automatiques activés** : Laissez les options « Prise en charge » et « Approuvée » activées par défaut pour réduire les interventions manuelles et limiter le risque d'oubli vis-à-vis de la plateforme agréée.
- **Ne modifiez pas la date de dernière importation** : L'ajustement manuel du champ de date risque d'interrompre le décalage de sécurité d'une heure géré par OpenFire et d'ignorer certaines factures transmises sur ce créneau.

Mis a jour le : 25/08/2026
