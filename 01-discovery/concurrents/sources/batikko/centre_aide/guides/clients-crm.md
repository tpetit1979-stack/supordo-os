---
url: https://batikko.com/documentation/guides/clients-crm
url_finale: https://batikko.com/documentation/guides/clients-crm
date_collecte: 2026-09-07
destination: centre_aide
---

## Vue d'ensemble

Le module Clients de Batikko est une base de données structurée pour vos contacts BTP : **particuliers** et **professionnels**. Recherche full-text, vérification SIRET officielle, scoring de fiabilité et historique complet par client (chantiers, devis, factures, paiements).

Ce n'est pas un CRM marketing complet (pas d'email marketing automatisé, pas de scoring comportemental), mais une base solide pour gérer vos relations BTP avec les fonctionnalités essentielles : vérification d'identité, traçabilité, et collaboration avec vos employés.

## Particulier vs Professionnel

### Particulier

Pour vos clients résidentiels classiques.

- Prénom + nom
- Téléphone
- Adresse complète

### Professionnel

Pour vos clients entreprises (architectes, syndics, etc.).

- Raison sociale
- SIRET (vérifié auprès de l'INSEE)
- Numéro TVA intracom
- Forme juridique
- Code APE / NAF
- Adresse + contact

Le SIRET, la TVA et l'adresse complète sont **obligatoires** pour les clients pros si vous voulez émettre des factures conformes à la réforme Factur-X de septembre 2026.

## KYC & Scoring A-E

Batikko vérifie vos clients pros et calcule un score de fiabilité automatique :

### Vérification KYC (Know Your Customer)

Quand vous saisissez un SIRET, Batikko interroge les bases publiques officielles pour vérifier : forme juridique, code activité, statut administratif (actif/cessé), date de création. Si tout est vert, le client est marqué **KYC vérifié** avec horodatage.

### Scoring A à E

Chaque client reçoit un grade (A à E) et un score numérique (0-100) basés sur des règles : ancienneté, CA généré, taux de paiement, retards, litiges.

## Comment ça marche

1. 01### Créez un clientChoisissez le type (particulier/pro). Pour un pro, saisissez le SIRET : Batikko vérifie auprès de l'INSEE et pré-remplit la raison sociale, l'adresse, la forme juridique.
2. 02### Recherche et filtresRecherche full-text sur nom, email et téléphone. Filtres par type de client et statut. Idéal pour retrouver une fiche en 2 secondes.
3. 03### Affectez aux employésEn tant que dirigeant, vous pouvez assigner certains clients à des employés spécifiques avec des permissions en lecture seule. Un commercial ne voit que ses clients.
4. 04### Liez automatiquement aux chantiersTout chantier créé pour ce client est automatiquement rattaché. La fiche client affiche l'historique complet : devis, factures, paiements, chantiers avec statuts et nombre de photos.
5. 05### Générez un portail (si syndic)Pour les clients syndics ou architectes qui doivent voir l'avancement de plusieurs chantiers, générez un portail à durée limitée (1 à 365 jours). Lien protégé par mot de passe.

## Portail syndic / architecte

Pour vos clients qui suivent plusieurs chantiers en parallèle (syndics de copropriété, architectes, donneurs d'ordre), générez un portail web dédié avec :

- URL unique protégée par mot de passe
- Durée de vie configurable (1 à 365 jours)
- Vue de tous les chantiers en cours du client
- Photos juridiques avec leur catégorie (avant/pendant/après)
- Documents (devis, factures, plans)
- Révocable à tout moment depuis votre espace

## Limites par plan

| Plan | Clients max | 
|---|---|
| Solo (gratuit) | 10 | 
| Starter / Pro / Entreprise | Illimité | 

Si vous dépassez la limite de votre plan, vous pouvez toujours **consulter** vos clients existants mais vous ne pouvez plus en créer de nouveaux jusqu'à un upgrade.

## Astuces & limitations à connaître

Saisissez le SIRET en premier pour les clients pros : tout le reste se remplit automatiquement.

Renseignez TOUJOURS le téléphone ET l'email : indispensable pour les relances multi-canal des factures.

Utilisez le scoring A-E pour identifier vos clients à risque avant de signer un nouveau devis.

Le portail syndic est révocable instantanément si vous changez d'avis.

### Limitations actuelles

## Aller plus loin

### Une question sur cette fonctionnalité ?

Notre équipe vous répond en moins de 2 heures.

[Contacter le support](https://batikko.com/contact)