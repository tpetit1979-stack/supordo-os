---
url: https://batikko.com/documentation/guides/devis-factures
url_finale: https://batikko.com/documentation/guides/devis-factures
date_collecte: 2026-09-07
destination: centre_aide
---

## Vue d'ensemble

La facturation est le nerf de la guerre dans le BTP. Batikko gère le cycle complet de l'offre commerciale jusqu'à l'encaissement, avec toutes les spécificités du bâtiment français : **contribution REP** (éco-fee), **ajustements CEE**, **franchise TVA** pour les micro-entreprises, **autoliquidation** pour la sous-traitance, et **Factur-X** prêt pour septembre 2026.

Tous les documents sont générés automatiquement en PDF avec votre branding, envoyés par email avec suivi d'ouverture, et signables électroniquement par votre client.

## Cycle de vie du devis

Un devis Batikko passe par plusieurs statuts qui gèrent les actions disponibles :

Devis en cours de construction. C'est le SEUL statut où vous pouvez modifier les lignes.

Envoyé au client par email. Suivi d'ouverture activé. Plus modifiable.

Le client a signé électroniquement. Peut être converti en facture.

Le client a refusé. Vous pouvez le dupliquer pour faire une variante.

Annulé manuellement. N'apparaît plus dans les listes actives.

Sorti de la liste active mais conservé pour l'historique.

## Cycle de vie de la facture

Une facture créée (manuellement ou par conversion d'un devis accepté) suit ce parcours :

Modifiable. État initial à la création.

Validée mais pas encore envoyée. Encore modifiable.

Email envoyé au client avec suivi d'ouverture. Verrouillée.

Encaissement intégral. Suivi date_paiement.

Acompte reçu. Solde restant à recouvrer.

Délai de paiement dépassé sans encaissement. Déclenche les relances.

Statut intermédiaire avant l'IMPAYÉE selon votre configuration.

Annulée. Peut générer un avoir si déjà envoyée.

Sortie des listes actives.

Batikko gère également les **factures d'acompte**, les **factures de solde** et les **avoirs** liés à une facture originale.

## Structure des lignes

Chaque ligne d'un devis ou d'une facture supporte tous les besoins du BTP français :

Texte libre du poste (ex: « Fourniture et pose carrelage 60×60 »).

Quantité numérique et unité libre (m², m³, ml, h, forfait, etc.).

Prix de vente HT par unité.

Prix d'achat multiplié par votre coefficient de marge donne le prix unitaire. Permet de tracer votre rentabilité.

Chaque ligne a sa propre TVA (5,5% / 10% / 20%). Indispensable BTP.

Éco-contribution BTP par ligne, pour les déchets de chantier.

Pourcentage ou montant fixe sur le total HT.

Ajustements personnalisés et nommés (ex: prime CEE en négatif).

En cas de TVA mixte sur le document (plusieurs taux dans les lignes), Batikko génère automatiquement la ventilation par taux, obligatoire selon l'article 242 nonies A du CGI.

## Cas particuliers TVA

### Franchise en base de TVA

Si vous êtes micro-entrepreneur ou en franchise (CA inférieur aux seuils), activez l'option dans vos paramètres. Batikko force automatiquement toutes les TVA à 0% sur tous les documents et ajoute la mention légale obligatoire « TVA non applicable, art. 293 B du CGI ».

### Autoliquidation TVA (sous-traitance BTP)

Pour les prestations en sous-traitance BTP entre assujettis (article 283-2 nonies CGI), cochez « Autoliquidation » sur la facture. La TVA est forcée à 0% et la mention « Autoliquidation - art. 283-2 nonies CGI » est ajoutée. C'est le donneur d'ordre qui collectera la TVA.

## Relances automatiques

Batikko envoie automatiquement 3 niveaux de relance, chaque jour, sur les factures impayées :

Chaque relance envoyée est historisée et incluse dans l'email avec un suivi d'ouverture pour savoir si votre client a vu le rappel.

## Astuces & bonnes pratiques

Activez la signature électronique : c'est ce qui bloque légalement les contestations client.

Construisez votre bibliothèque d'ouvrages BTP dès le premier mois : vous gagnerez des heures sur tous vos prochains devis.

Renseignez TOUJOURS le SIRET et la TVA de vos clients pros : c'est obligatoire pour la facturation électronique 2026.

Le coefficient de marge vous permet de tracer votre rentabilité par poste.

Activez le format Factur-X dans vos paramètres dès maintenant : vous serez prêt automatiquement en septembre 2026.

Pour un acompte, créez d'abord la facture d'acompte avec le pourcentage souhaité, puis la facture de solde au moment de la livraison.

## Aller plus loin

### Une question sur cette fonctionnalité ?

Notre équipe vous répond en moins de 2 heures.

[Contacter le support](https://batikko.com/contact)