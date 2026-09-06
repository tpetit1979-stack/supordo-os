---
source: https://support.openfire.fr/hc/fr/articles/29466353991580-G%C3%A9rer-vos-%C3%A9v%C3%A9nements-de-facturation-%C3%A9lectronique
categorie: Utiliser OpenFire
titre: Gérer vos événements de facturation électronique
date_recuperation: 2026-09-05
---

# Gérer vos événements de facturation électronique

Cet article vous explique le fonctionnement des **événements** dans le cadre de la facturation électronique française au sein de OpenFire. Vous découvrirez ce qu'est un événement, comment le consulter, le configurer et comment émettre ou traiter les notifications liées au cycle de vie de vos factures.

Cet article contient les sections suivantes :

- [Qu'est-ce qu'un événement de facturation électronique ?](#h_01KZGT3CSEH83B8XHD5428DHXC)
- [Les principaux statuts d'événements](#h_01KZGT3CSJM3216Z47A1HXR4YT)
- [Comment consulter les événements d'une facture ?](#h_01KZGT3CT3J6005QEX0MXRZSHY)
- [Comment recevoir et traiter un événement entrant ?](#h_01KZGT3CT96FM0ZRC29ZAHNC47)
- [Comment envoyer un événement manuellement ?](#h_01KZGT3CTKPK3BBKVK1TR2MW3M)
- [Les motifs et actions associés les plus courants](#h_01M0H199QF5SGCQR5B6PWH2VNF)
- [Pour aller plus loin](#h_01KZGT3CTYFDN8ZMJJ8YZ88J15)
- [Bonnes pratiques](#h_01KZGVNZP8Y1BJC29GA0Q668EA)

## Qu'est-ce qu'un événement de facturation électronique ?

Dans le cadre de la réforme de la facturation électronique, chaque facture client ou fournisseur échangée via la Plateforme Agréée génère des **événements**. Un événement est une notification automatisée ou manuelle qui renseigne le **statut** de votre facture tout au long de son cycle de vie : dépôt, réception, approbation, mise en paiement, litige ou refus.

Les événements circulent dans deux sens :

- **Événements sortants** : générés par votre entreprise (automatiquement ou manuellement) pour informer la Plateforme Agréée et le destinataire de l'état de la facture.
- **Événements entrants** : reçus de la Plateforme Agréée pour vous notifier d'un changement d'état effectué par votre interlocuteur (facture approuvée, mise en litige, paiement effectué, etc.).

| 💡**Note **: Les événements de facturation électronique ne doivent pas être confondus avec les interventions planifiées dans votre agenda technique. Ils concernent exclusivement le suivi administratif des **factures** et des **avoirs**. |
| --- |

## Les principaux statuts d'événements

Chaque événement modifie le statut d'avancement de votre facture, qu'elle soit client ou fournisseur.

Voici les principaux statuts rencontrés en fonction du type d'opération (client ou fournisseur) :

Pour vos factures clients

| **Statut** | **Signification** | **Génération** | **Quand l'utiliser (événements manuels)** |
| --- | --- | --- | --- |
| **Déposée** | La facture a quitté votre logiciel vers la Plateforme Agréée. | Auto | — |
| **Rejetée** | Erreur technique lors du transfert (format invalide, etc.). | Auto | — |
| **Reçue par la plateforme** | La PA a bien réceptionné le fichier et validé sa conformité technique. | Auto | — |
| **Transmise** | La facture a été transmise à la PA de votre destinataire. | Auto | — |
| **Prise en charge** | Le destinataire a intégré la facture dans son circuit de validation. | Auto / Manuel | Le destinataire confirme avoir reçu et traité la facture. |
| **Suspendue** | Le processus est interrompu en attente d'informations complémentaires. | Manuel | Le destinataire a besoin de documents supplémentaires ou d'une correction. |
| **En litige** | La facture fait l'objet d'une contestation (montant, prestations). | Manuel | Le destinataire conteste tout ou partie de la facture. |
| **Approuvée partiellement** | Seule une partie de la facture est acceptée. | Manuel | Accord partiel sur le montant. Une facture rectificative sera nécessaire. |
| **Refusée** | La facture est refusée par le destinataire ou rejetée définitivement. | Manuel | Le destinataire refuse la facture (erreur, doublon). Une nouvelle facture devra être émise. |
| **Approuvée ** | Le document est accepté sans réserve par le destinataire. | Manuel | Le destinataire valide la facture sans réserve pour paiement. |
| **Annulée** | Un avoir a été émis pour annuler la facture initiale. | Manuel | La facture est annulée comptablement. Clôture du cycle pour une facture de vente. |

Pour vos factures fournisseurs 

| **Statut** | **Signification** | **Génération** | **Quand l'utiliser (événements manuels)** |
| --- | --- | --- | --- |
| **Prise en charge** | Vous avez intégré la facture fournisseur dans votre circuit de validation. | Auto | — |
| **Suspendue** | La validation est interrompue en attente d'informations du fournisseur. | Manuel | Vous attendez un justificatif manquant ou une correction du fournisseur. |
| **En litige** | Vous contestez tout ou partie de la facture fournisseur. | Manuel | Vous contestez le montant ou les prestations. Un échange est nécessaire. |
| **Approuvée partiellement** | Vous n'acceptez qu'une partie de la facture. | Manuel | Vous validez certaines lignes mais en refusez d'autres. |
| **Refusée** | Vous refusez la facture fournisseur. | Manuel | La facture est incorrecte ou ne correspond pas à la commande. |
| **Approuvée** | La facture est validée sans réserve pour paiement. | Manuel | La facture est prête à être payée. |
| **Paiement envoyé** | L'ordre de paiement a été exécuté. | Manuel | Le règlement (virement, chèque) a été effectué. Clôture du cycle. |

**Trois phases sont identifiables : **

1. **Phase d'envoi** : `Déposée` → `Reçue par la plateforme` (ou `Rejetée` en cas d'erreur technique).
2. **Phase de traitement** : `Prise en charge` → `Suspendue` / `En litige` / `Approuvée partiellement` / `Refusée` / `Approuvée`.
3. **Phase de clôture** : `Paiement envoyé` (pour les achats) ou `Annulée` (pour les ventes).

**Cycle de vie typique d'une facture client**

![](https://support.openfire.fr/hc/article_attachments/29678482609436)

**Cycle de vie typique d'une facture fournisseur**

![](https://support.openfire.fr/hc/article_attachments/29678488563100)

## Comment consulter les événements de vos factures ?

Depuis votre facture

Suivre le chemin d'accès suivant : **Comptabilité** > **Factures client** (ou **Factures fournisseur**) > Ouvrir une facture > Onglet **Facturation électronique**.

1. Ouvrir la facture concernée depuis la liste.
2. Cliquer sur l'onglet **Facturation électronique** situé dans la partie inférieure du formulaire.
3. Consulter le journal chronologique des événements :

  - Le **statut**
  - La **date et l'heure** d'enregistrement.
  - Les **informations détaillées** (motifs, commentaires ou pièces jointes associés).
4. Cliquer sur la ligne d'un événement pour en afficher le détail complet.

Exemple :

![](https://support.openfire.fr/hc/article_attachments/29739681632284)

Ces statuts peuvent être affichés depuis la liste de vos factures ou utiliser comme filtre avancé, pour en simplifier le pilotage :

![](https://support.openfire.fr/hc/article_attachments/29739689424540)

| 💡**Note **: N'hésitez pas à créer des filtres favoris pour mieux traiter vos factures en fonction du type d'événements reçu, notamment ***Dernier événement contient "Litige"** *ou encore ***Dernier événement contient "refus".*** |
| --- |

Depuis la liste des événements

Suivre le chemin d'accès suivant : **Comptabilité > Configuration > Facturation électronique en France > Evénements de factures**

Vous retrouvez ici la liste de l'ensemble des événements enregistrés pour l'ensemble de vos factures, clients ou fournisseurs.

| 💡**Note **: vous pouvez remonter à la facture d'origine depuis n'importe quel événement en cliquant simplement sur le champ "Facture" de l'événement, afin d'en faciliter le traitement. |
| --- |

## Comment recevoir et traiter un événement entrant ?

Lorsqu'une mise à jour de statut provient de la Plateforme Agréée (par exemple, un signalement de litige par un client), OpenFire génère automatiquement une **activité**.

### Qui reçoit l'alerte ?

Selon la configuration appliquée à votre base, l'activité est attribuée :

- Aux utilisateurs désignés dans les paramètres de facturation électronique.
- Au créateur de la facture.
- Au vendeur ou commercial assigné au document.

![](https://support.openfire.fr/hc/article_attachments/29466883146268)

| **🧑‍🏫Exemple** :  Si votre client signale un événement **En litige** avec le motif **« Quantité facturée incorrecte »**, OpenFire crée automatiquement une activité pour que vous puissiez corriger l'anomalie. |
| --- |

### Traiter un événement entrant

Cliquer sur le tableau de bord des activités (icône **Horloge** en haut à droite).

Sélectionner l'activité correspondant à l'événement de facturation électronique.

Cliquer sur le lien pour ouvrir la facture concernée.

Consulter l'onglet **Facturation électronique** pour prendre connaissance des éléments :

- **Motif** : cause du litige, du refus ou de l'acceptation partielle.
- **Commentaire** : précisions apportées par l'émetteur.
- **Pièces jointes** : justificatifs éventuels.

Réaliser les démarches nécessaires :

- **En cas de litige** : prendre contact avec le client, corriger le document ou établir un avoir.
- **En cas d'approbation partielle** : contrôler les lignes contestées et adapter le montant de la régularisation.
- **En cas de paiement envoyé** : contrôler votre compte bancaire puis effectuer le lettrage de la facture.

## Comment envoyer un événement manuellement ?

Dans le cadre du suivi de vos flux d'achats et de ventes, vous pouvez être amené à notifier manuellement la Plateforme Agréée d'un changement de statut.

### Étapes pour envoyer un événement

- Ouvrir la facture client ou fournisseur concernée.
- Accéder à l'onglet **Facturation électronique**.
- Cliquer sur le bouton **Envoyer un événement**.

![](https://support.openfire.fr/hc/article_attachments/29466641990044)

Puis :

Sélectionner la valeur adéquate dans le champ **Statut**.

Si le statut sélectionné est un statut à justification (litige, refus, approbation partielle) :

- Choisir la raison dans le champ **Motif**.
- Renseigner le champ **Commentaire** pour apporter des explications explicites.
- Téléverser des éléments dans le champ **Pièces jointes** si nécessaire.

Cliquer sur le bouton **Valider** pour transmettre l'événement.

![](https://support.openfire.fr/hc/article_attachments/29466641990428)

| 💡**Note **: OpenFire automatise la majorité des envois, par exemple lors de l'émission d'un ordre de paiement bancaire ou de la validation comptable d'une facture fournisseur si vos paramètres le prévoient. |
| --- |

### Cas particulier pour les évènements de type **Refus**

Vous devez confirmer manuellement le refus. Une telle action est définitive et obligera votre fournisseur à émettre une nouvelle facture le cas échéant.

![](https://support.openfire.fr/hc/article_attachments/29466883147164)

## Les motifs et actions associés les plus courants

Lors de la saisie d'un événement, vous pouvez préciser un **Motif** accompagné d'un **Commentaire** et d'une **Action** recommandée.

### Motifs courants

- **Article facturé incorrect** : les prestations facturées ne correspondent pas à celles réalisées
- **Montant incorrect** : le montant de la facture ne correspond pas au bon de commande ou au devis
- **Informations manquantes** : des éléments nécessaires au traitement de la facture sont absents
- **Doublon** : la facture a déjà été reçue et traitée
- **Autre** : motif libre à préciser dans le commentaire

### Actions possibles

- **Créer une Facture Rectificative** : un avoir ou facture rectificative doit être émise
- **Envoyer un justificatif** : un document complémentaire doit être transmis
- **Corriger la facture** : la facture doit être modifiée et renvoyée
- **Aucune action** : le statut est informatif et ne nécessite pas d'action

| **🧑‍🏫Exemple** : Si un client refuse une facture car le montant ne correspond pas au devis, vous pouvez saisir un événement avec le statut **Refusé**, le motif **Montant incorrect**, le commentaire **Le montant facturé diffère du devis n°DEV-2024-0042**, et l'action **Créer une Facture Rectificative**. |
| --- |

## Pour aller plus loin

La gestion des alertes et des envois automatiques se configure au niveau des paramètres généraux de l'application.

| 📓**Pour aller plus loin** → [Activer et paramétrer la réception des factures fournisseurs](https://support.openfire.fr/hc/fr/articles/29465754707100) 📓**Pour aller plus loin** → [Activer et paramétrer l'émission de vos factures clients](https://support.openfire.fr/hc/fr/articles/29465837149212) |
| --- |

## Bonnes pratiques

- **Traiter les activités quotidiennes** : consultez régulièrement votre tableau de bord des activités afin de régler les litiges déclarés par vos clients dans les meilleurs délais.
- **Renseigner systématiquement des commentaires précis** : lors de l'émission d'un litige ou d'un refus sur une facture fournisseur, donnez des explications claires dans le champ **Commentaire** afin d'éviter tout blocage administratif.
- **Ne pas tenter de supprimer un document transmis** : un document envoyé vers la Plateforme Agréée ne peut plus être supprimé de la base. Utilisez la procédure de refus puis d'émission d'avoir.
- **Définir des responsables d'alertes identifiés** : assurez-vous dans la configuration qu'au moins un utilisateur clé ou comptable est configuré dans le champ **Utilisateurs à alerter**.

Mis a jour le : 25/08/2026
