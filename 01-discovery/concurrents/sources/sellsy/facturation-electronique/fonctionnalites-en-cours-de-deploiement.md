---
source: https://help.sellsy.com/fr/articles/16815816-fonctionnalites-en-cours-de-deploiement
categorie: Facturation électronique
titre: Fonctionnalités en cours de déploiement
date_recuperation: 2026-09-05
---

# Fonctionnalités en cours de déploiement

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2650515909/63bf5288d275b600d12dc0d12049/FAQ-Bannie%CC%80reAcademy-2+-2-.png?expires=1788674400&signature=e6e3cfbc98e388bfe8e9e5d5a402d879f70c02d516a9337ac81c472c1509393b&req=diYiFsx%2FmIhfUPMW3nq%2BgYegOs%2FuoZs8pl1NL6nVxJCqV6nMkbkAxPTChHZL%0ABRCWaIQ3Qy7gZPFT6uYrGrlblxk%3D%0A)

___________________________________________________________

### 1. Côté réception

### Automatisations et documents électroniques

À ce jour, vos automatisations — relances, suivi des retards et rapports — ne tiennent pas compte du statut de vos documents électroniques (factures et avoirs, en vente comme en achat).

Concrètement, une relance automatique paramétrée sur les factures « À régler » ne se déclenchera pas sur une facture électronique dont le statut est : *Déposée*, *Émise*, *Reçue*, *Mise à disposition*, *Prise en charge*, *Approuvée*, *Approuvée partiellement* ou *Complétée*. Le même principe s'applique au suivi des retards et aux rapports.

Une correction est prévue, déployée en deux temps :

1. Prise en compte des statuts *À régler* et *Payée*
2. Prise en compte du statut *Retard*

___________________________________________________________

### Prélèvement sur un document électronique

Pour le moment, déclencher un prélèvement sur un document électronique ne provoque aucun changement de statut dans Sellsy.

Nous vous recommandons d'éviter de déclencher un prélèvement sur les documents dont le statut est **Rejetée** ou **Refusée**, dans l'attente que cette action soit bloquée dans l'outil.

Une évolution est prévue pour que vos documents électroniques passent automatiquement au statut **Encaissée** dès qu'un règlement intervient, que ce soit par prélèvement SEPA (prélèvement bancaire automatisé) ou par carte bancaire.

___________________________________________________________

### Liaison entre factures d'achat et bons de livraison ou bons de commande fournisseur

Cette fonctionnalité est prévue dans une prochaine évolution de Sellsy. Elle vous permettra de :

- **Lier vos documents a posteriori**, à tout moment, depuis la fiche du document concerné (facture, bon de commande, bon de livraison, avoir). Cette liaison sera possible quel que soit le type et l'origine du document — standard ou électronique.
- **Conserver vos habitudes actuelles** : la liaison entre documents standards (bon de commande, bon de livraison, facture standard) fonctionnera exactement comme aujourd'hui.

___________________________________________________________

### Mise en litige d'une facture reçue

Le statut *Litige* n'est pas encore disponible dans Sellsy. Comme la plupart des plateformes de dématérialisation, Sellsy gère aujourd'hui uniquement les statuts obligatoires prévus par la réforme : *Déposée*, *Rejetée*, *Refusée*, *Approuvée* et *Encaissée*.

**En attendant :** si vous ne pouvez pas approuver une facture en l'état, refusez-la en sélectionnant le motif de refus le plus adapté à votre situation.

De nouveaux statuts sont prévus à venir :

- **Mettre en litige** : contester tout ou partie d'une facture déjà approuvée, sans avoir à la refuser entièrement.
- **Prendre en charge** : indiquer à votre fournisseur que vous avez bien pris acte de la facture, sans l'approuver officiellement.
- **Approuver partiellement** : valider une facture tout en signalant un désaccord sur une partie de son contenu.
- **Paiement transmis** : un nouveau statut et un état d'avancement pour les paiements partiels, au-delà du seul statut *Encaissée*.

___________________________________________________________

### Éviter les doublons lors de la réception de documents

En attendant la mise à disposition d'un outil dédié, voici les bonnes pratiques à adopter.

Avant de créer ou d'importer manuellement un document, posez-vous la question suivante : **est-ce que je risque de recevoir ce document par voie électronique ?**

- Jusqu’en septembre 2027, si vous êtes assujetti à la TVA française et que votre fournisseur l’est également **et est une ETI**, ne créez pas et n’importez pas ce document manuellement : vous le recevrez automatiquement par voie électronique. Le créer ou l’importer vous-même générerait un doublon.
- En cas de doute, contactez votre fournisseur pour savoir comment il va vous transmettre le document.

Une fonctionnalité de gestion automatique des doublons est prévue à venir. Elle permettra notamment :

- de détecter automatiquement les doublons certains (même type de document, même fournisseur, même numéro) ;
- d'éviter les doublons entre un document standard et son équivalent électronique ;
- de vous alerter avant la création d'un document si un doublon potentiel est détecté, que ce soit à l'import ou lors d'une saisie manuelle.

___________________________________________________________

### 2. Côté émission

### Disponibilité de l'e-reporting

L'e-reporting n'est pas encore disponible dans Sellsy. Actuellement, lorsqu'un flux relève de l'e-reporting, Sellsy génère une facture standard, sans transmission à l'administration fiscale selon le régime de TVA du client.

Cette fonctionnalité est en cours de développement, avec une disponibilité visée d’ici la fin de l’année.

> **Bon à savoir :** l'administration fiscale a annoncé une période de tolérance, sans sanction avant 2028.

___________________________________________________________

### Facturation de sociétés françaises sans SIREN ou SIRET

Dans le répertoire, lorsque le pays sélectionné est la France, une case à cocher vous permet d'indiquer que la société n'a pas de SIREN. Cela rend alors les champs associés non obligatoires.

Les cas suivants ne sont pas encore pris en charge et feront l'objet d'une évolution à venir :

- la facturation de structures françaises sans SIREN, SIRET et numéro de TVA ;
- la bascule d'une société vers un statut particulier.

Cette fonctionnalité est en cours de développement, avec une disponibilité visée d’ici la fin du mois de septembre.

___________________________________________________________

### Transmission de factures électroniques à Chorus Pro

Le fonctionnement ne change pas avec la réforme. Les factures adressées à une entité (facturation B2G, c'est-à-dire à destination du secteur public) doivent continuer de transiter par le portail Chorus Pro.

Pour faciliter ces envois, Sellsy met à votre disposition un connecteur avec la solution Flowwa.

La transmission directe de factures électroniques vers Chorus Pro depuis Sellsy est prévue dans les prochaines semaines. En attendant, deux options s'offrent à vous :

- exporter le PDF de votre facture depuis Sellsy et le déposer manuellement sur le portail Chorus Pro ;
- passer par la solution Flowwa.

___________________________________________________________

### Factures d'abonnement et facturation électronique

L'envoi automatique des factures d'abonnement en e-invoicing n'est pas encore disponible. Cette fonctionnalité est en cours de développement et sera disponible prochainement.

En attendant, seules les factures créées manuellement et les factures créées en mode *« après validation »* sont transmises en e-invoicing ou en e-reporting. Les factures d'abonnement en envoi automatique elles, continuent d'être envoyées par email dans un format classique.

Mis a jour le : 04/09/2026
