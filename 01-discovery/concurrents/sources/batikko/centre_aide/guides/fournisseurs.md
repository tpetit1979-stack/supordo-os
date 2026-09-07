---
url: https://batikko.com/documentation/guides/fournisseurs
url_finale: https://batikko.com/documentation/guides/fournisseurs
date_collecte: 2026-09-07
destination: centre_aide
---

## Vue d'ensemble

Le module Fournisseurs centralise vos achats et factures fournisseurs avec deux super-pouvoirs : **l'OCR automatique** pour scanner vos factures papier ou PDF, et la **recherche GPS de proximité** pour trouver le fournisseur le plus proche depuis le terrain.

Le module est inclus dans les plans Pro et Entreprise (sur abonnement séparé pour les autres). C'est l'un des outils les plus rentables du temps : fini les piles de factures papier qui s'accumulent.

## Base fournisseurs

Chaque fournisseur a sa fiche complète avec :

Nom, SIRET, numéro de TVA, statut actif/inactif.

Matériaux, sous-traitants, services, autre. Filtrable.

Email, téléphone, contact commercial.

Rue, code postal, ville. Coordonnées GPS auto-calculées.

Comptant, 15j, 30j, 45j, 60j.

IBAN/BIC chiffrés et stockés de manière sécurisée.

Action utile : un bouton « géocoder en lot » convertit en GPS toutes les fiches qui n'ont pas encore de coordonnées (utile si vous importez une vieille base).

## OCR avancé pour vos factures

Batikko utilise un moteur d'OCR avancé pour scanner automatiquement vos factures fournisseurs (PDF ou photo). Précision moyenne d'environ 95% sur les champs clés.

### Données extraites automatiquement

- Numéro de facture
- Date d'émission
- Date d'échéance
- Montant HT
- Taux TVA
- Montant TVA
- Montant TTC
- SIRET fournisseur
- Nom fournisseur
- Lignes de détail

Un **score de confiance** est calculé pour chaque extraction. Vous pouvez valider directement ou corriger avant de valider. Les PDF sont automatiquement convertis pour analyse.

## Recherche GPS de proximité

Sur le chantier, il vous manque un sac de ciment ? Au lieu d'appeler 5 fournisseurs, utilisez la recherche GPS de proximité :

1. 01### Activez la géolocalisationSoit Batikko utilise la géolocalisation du navigateur, soit vous saisissez manuellement vos coordonnées GPS.
2. 02### Définissez le rayonDe 1 à 500 km. Pour un dépannage urgent, 5-10 km est en général suffisant en zone urbaine.
3. 03### Filtrez par catégorieMatériaux, sous-traitants, location d'outillage. Affichez seulement ce qui vous intéresse.
4. 04### Résultats triés par distanceListe triée du plus proche au plus loin avec distance calculée en kilomètres. Cliquez pour avoir l'itinéraire.

## Cycle de la facture fournisseur

Une facture fournisseur peut être créée de deux façons :

### Saisie manuelle

Tous les champs renseignés à la main. Rapide pour une facture simple ou si vous n'avez pas de PDF.

### OCR + validation

Uploadez le PDF ou la photo. Google Cloud Vision extrait, vous validez ou corrigez. Idéal pour les factures volumineuses.

Statuts gérés automatiquement :

- « À payer » : facture créée, date échéance future
- « En retard » : passée la date d'échéance sans paiement (auto-flag)
- « Payée » : paiement enregistré (date_paiement)
- « Annulée » : annulation manuelle

## Astuces & limitations

Scannez vos factures dès que vous les recevez : ne laissez pas s'accumuler les piles.

Renseignez le RIB de vos fournisseurs habituels pour générer rapidement les virements.

Utilisez la recherche GPS sur chantier : ça change la vie pour les achats urgents.

L'OCR est très précis (~95%) mais relisez toujours les montants avant validation.

Les IBAN/BIC sont chiffrés et stockés de manière sécurisée : aucune fuite possible.

### Limitations actuelles

Les factures fournisseurs ne sont pas encore liées aux chantiers (pas de cost tracking par projet pour l'instant). Pas de catalogue marketplace fournisseur intégré.

## Aller plus loin

### Une question sur cette fonctionnalité ?

Notre équipe vous répond en moins de 2 heures.

[Contacter le support](https://batikko.com/contact)