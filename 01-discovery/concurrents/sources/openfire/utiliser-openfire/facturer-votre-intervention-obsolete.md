---
source: https://support.openfire.fr/hc/fr/articles/19088213835036-Facturer-votre-intervention-obsol%C3%A8te
categorie: Utiliser OpenFire
titre: Facturer votre intervention (obsolète)
date_recuperation: 2026-09-05
---

# Facturer votre intervention (obsolète)

![All_tick_V2.png](https://support.openfire.fr/hc/article_attachments/20229346452636)

OpenFire vous permet de générer des factures, les envoyer à vos clients par mail et gérer les paiements associés.

Cet article contient les sections suivantes :

- [Facturer vos interventions](#h_01JVYHNZQ42MH02T7JRWZ0TMSZ)
  - [Exemples de flux de facturation possibles](#h_01JVYHNZQ49J0DMYWSPZGX3S42)
    - [Facturation d’un entretien récurrent sans devis préalable](#h_01JVYHNZQ4Q2C5H2CCNSPFCD28)
    - [Facturation d’un entretien ponctuel avec émission d’un devis préalable](#h_01JVYHPB82HV7574288ZC5HQXY)
    - [Facturation d’un SAV avec diagnostic, commande de pièces et intervention. ](#h_01JQ9BFT0T5Y0YJWY7JKA9GTXB)
  - [Facturer des interventions sans devis préalable ](#h_01JQ9BFT0T4FQS20YGRB4NGC08)
  - [Identifier vos interventions à facturer ](#h_01JQ9BFT0TP5MF6F1YTJ4Q0ZZN)
  - [Générer la facture ](#h_01JQ9BFT0TYR3MF6JQQRZ8Q8J4)
    - [Facturation d’une seule intervention ](#h_01JQ9BFT0TRVSZQ1716279YRJK)
    - [Facturation d’une liste d’interventions ](#h_01JQ9BFT0TV2H7VXXWH049P5QK)
  - [Facturer depuis le mobile](#h_01JQ9BFT0T7KK0SRRYNP5YDYVM)

# Facturer vos interventions

Selon votre organisation, il est possible qu’une partie de la facturation, notamment concernant vos activités de prestation chez le client, soit réalisée directement depuis les interventions. OpenFire facilite ce processus en permettant de créer facilement des devis et des factures à partir des interventions éligibles.

Plusieurs types de flux sont possibles, dont voici quelques exemples :

## Exemples de flux de facturation possibles

### Facturation d’un entretien récurrent sans devis préalable

1. Réception de la demande d’intervention de la part du client
2. Planification de l’entretien directement sur le planning par l’ADV
3. Réalisation de la prestation par le technicien
4. Génération de la facture par le technicien ou l’ADV directement après l’intervention

### Facturation d’un entretien ponctuel avec émission d’un devis préalable

1. Réception de la demande d’intervention de la part du client
2. Émission d’un devis relatif la réalisation de la prestation
3. Validation du devis par le client
4. Planification de l’entretien directement sur le planning par l’ADV
5. Réalisation de la prestation par le technicien
6. Facturation de la prestation depuis le devis par le technicien ou l’ADV directement après l’intervention

### Facturation d’un SAV avec diagnostic, commande de pièces et intervention.

1. Réception d’une demande de SAV
2. Émission d’un devis relatif à la réalisation de l’intervention de diagnostic
3. Validation du devis par le client
4. Planification de l’intervention sur le planning par l’ADV
5. Réalisation du diagnostic, et émission d’un devis complémentaire de pièce détachée et de réparation directement sur site
6. Validation du devis complémentaire par le client
7. Facturation des deux devis par le technicien (depuis son mobile) ou l’ADV (depuis le le web) directement après l’intervention

## Facturer des interventions sans devis préalable

Le présent chapitre concerne principalement la facturation des interventions de type entretien. Dans ce type de configuration, une demande d’intervention ou une intervention peuvent exister, avec des lignes de facturation prévisionnelles, alors même qu’aucun devis n’a été généré.

L’exemple type est le suivant :

Vous prenez un RDV avec votre client pour la réalisation d’un ramonage de son poêle à bois. Vous planifiez le RDV directement sur votre planning, sans signature d’un devis préalable. Un choisissant le modèle d’intervention approprié et préalablement configuré, la prestation à facturer est directement ajoutée dans l’onglet facturation de votre intervention.

![](https://support.openfire.fr/hc/article_attachments/20229346453660)

Lorsque l’intervention sera réalisée, une facture pourra être émise directement depuis l’intervention (depuis le logiciel comme depuis l’application mobile), pour facturer cette prestation.

Plus précisément, comment faire ?

A l’image de vos devis, vous retrouvez dans l’onglet facturation de votre intervention :

- **La politique de facturation** : deux politiques sont disponibles : 
  - **Quantité planifiée** : est l’équivalent de la politique de facturation “quantité commandée” du bon de commande. Les quantités prévues seront facturables dès l’intervention réalisée.
  - **Quantité livrée** : est l’équivalent de la politique de facturation “quantité livrée” du bon de commande. Seules les quantités déjà livrées seront facturables. Cette politique n’est adaptée que dans le cas où vous intégrer des pièces stockables dans vos produits à facturer. Dans ce scénario, il serait néanmoins préférable d’éditer un devis préalablement pour le client.
- La **position fiscale**
- Les **lignes à facturer**

Ces éléments peuvent être préalablement définis sur le modèle d’intervention associé à l’intervention.

**📓**Pour aller plus loin → [Modèles d'intervention](https://support.openfire.fr/hc/fr/articles/19095496210460)

### Identifier vos interventions à facturer

Pour identifier vos commandes facturables :

- Pour le **plan basique** : OpenFire > Interventions > Mon planning d’intervention
- Pour les **autres plans **: Intervention > Interventions > Planning

Choisir ensuite le mode liste, et positionner le filtre suivant :

- **Terminé **(pour ne conserver que les interventions effectivement réalisées)
- **Factures en attente** (afin de ne conserver que les interventions ayant des lignes à facturer)

![](https://support.openfire.fr/hc/article_attachments/20229346454044)

### Générer la facture

La facturation peut-être réalisée individuellement ou en sélectionnant une liste d’intervention :

#### Facturation d’une seule intervention

Depuis l’intervention > Action > Générer la facture

![](https://support.openfire.fr/hc/article_attachments/20229346455324)

#### Facturation d’une liste d’interventions

Exemple : je veux facturer d’un seul coup tous mes ramonages réalisés hier :

![](https://support.openfire.fr/hc/article_attachments/20229344123676)

Depuis la liste des interventions sélectionnées > Action > Générer la facture

Une fenêtre vous confirme la bonne génération des factures.

![](https://support.openfire.fr/hc/article_attachments/20229346457500)

💡Notes :

- - Les factures sont toujours générées en brouillon
  - Il n'est pas possible de générer des factures d'acompte depuis les rendez-vous d'intervention. Si vous souhaitez facturer un acompte, nous vous recommandons de passer préalablement par la génération d’un devis associé à la réalisation de cette intervention

## Facturer depuis le mobile

Il est possible de générer vos factures d’interventions directement depuis le mobile par le technicien en charge de la réalisation de l’intervention.

Ce processus est surtout adapté au cas de figures suivants :

- Facturation de l’entretien lorsqu’il n’y a pas de devis préalable dans le logiciel
- Facturation d’un devis complémentaire émis par le technicien depuis l’application mobile dans le cas de la vente d’une pièce détachée additionnelle

**📓**Pour aller plus loin → [Facturer depuis le mobile](https://support.openfire.fr/hc/fr/articles/19085519502876)

Mis a jour le : 06/01/2026
