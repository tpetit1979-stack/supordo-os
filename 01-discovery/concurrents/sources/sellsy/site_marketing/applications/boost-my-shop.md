---
url: https://go.sellsy.com/applications/boost-my-shop
url_finale: https://go.sellsy.com/applications/boost-my-shop
date_collecte: 2026-09-07
destination: site_marketing
---

[Retour à la liste des apps](https://go.sellsy.com/marketplace)

# Boostmyshop

**Boostmyshop** propose une intégration entre sa solution, **myFulfillmen**t, et Sellsy, qui synchronise en continu vos produits, clients, commandes, stocks et factures pour un pilotage logistique et comptable fluide.

Boostmyshop myFulfillment est une plateforme SaaS tout-en-un intégrant un OMS (Order Management System), un WMS (Warehouse Management System), un TMS (Transport Management System) ainsi qu’un module de gestion des achats.

- **OMS / TMS** : import des commandes multi-canal, allocation automatique, préparation assistée par scan (pick & pack), génération d’étiquettes transporteur, gestion des retours.
- **WMS** : suivi des stocks quasi en temps réel, alertes de seuil, prévision des ruptures, picking optimisé, gestion du cross-docking. Résultat : jusqu’à 40 % de gain sur le temps de préparation et zéro erreur de picking.
- **Achats** : suggestions de réapprovisionnement basées sur les ventes et les prévisions, gestion des commandes fournisseurs, réceptions assistées.
- **Écosystème connecté** : plus de 60 connecteurs disponibles (CMS, transporteurs, etc.).

#### 
**Les bénéfices du duo myFulfillment by Boostmyshop × Sellsy :**

- Une vue unifiée de la commande à la facturation.
- Des données fiables et centralisées, sans ressaisie manuelle.
- Une réduction significative des coûts et une amélioration du service client.
- Une solution immédiatement scalable pour accompagner votre croissance.

## Principales fonctionnalités de l'intégration

L’intégration entre Boostmyshop myFulfillment et Sellsy **automatise les échanges essentiels pour synchroniser votre logistique e-commerce avec votre gestion de facturation** :

- Export automatique des produits, clients, commandes finalisées et factures dans Sellsy.
- Synchronisation quotidienne des niveaux de stock entre les dépôts myFulfillment et l’entrepôt Sellsy.
- Mappings automatisés des taux de TVA, transporteurs et modes de paiement, sans double saisie.
- Planification flexible des synchronisations de produits, commandes et stocks.


Dans le détail, cela se traduit de la façon suivante :

- **Export des produits** : création et mise à jour des articles myFulfillment dans Sellsy (SKU, libellé, éco-taxe, prix de vente, coût CUMP, codes-barres).
- **Export des clients** : à chaque commande, les informations client (société et contact) sont créées ou mises à jour dans Sellsy, l’e-mail servant de clé unique.
- **Export des commandes et factures** : dès qu’une commande est finalisée et dispose d’un numéro de suivi, une facture complète est automatiquement générée dans Sellsy, incluant les lignes produits, les frais de port, les taxes, le mode de paiement et le numéro de tracking.
- **Export des stocks** : les niveaux de stock agrégés par dépôt BMS sont transmis à l’entrepôt Sellsy sélectionné. Une synchronisation quotidienne est recommandée pour éviter les envois massifs.
- **Planification automatisée des flux** : les synchronisations PRODUCT_SYNC (toutes les 4 h), ORDER_SYNC (toutes les heures) et EXPORT_STOCK (quotidienne) s’exécutent automatiquement.
- **Mappings personnalisés** : correspondances automatisées pour les transporteurs, modes de paiement, comptes comptables et taux de TVA, garantissant une intégration sans ressaisie.
- **Feuille de route** : l’export des fournisseurs et des bons d’achat est en cours de développement pour couvrir l’ensemble du cycle d’approvisionnement.

## Tarif

L'intégration est **incluse dans les services de Boostmyshop myFulfillment avec le module Sellsy Facturation**. Si intégration concerne égalément d'autres modules, veuillez contacter l'équipe commerciale Boostmyshop pour connaître les tarifs appliqués.

## Guide d'installation

#### Étape 1 – Récupérer les identifiants API Sellsy

1. Connectez-vous à votre compte **Sellsy** .
2. Cliquez sur **Menu** >**Réglages** (en haut à droite).
3. Dans la section **Compte Sellsy** , sélectionnez le menu**Portail Développeur** .
4. Allez dans l’onglet **API V2 (bêta)** , puis cliquez sur**Créer un accès API** .
5. Choisissez le type d’accès **Personnel** , donnez un nom à votre connexion (ex :*Boostmyshop* ) et validez.
6. Copiez immédiatement les deux clés générées (**Client ID** et**Client Secret** ) — elles ne seront plus accessibles ultérieurement.

#### Étape 2 – Configurer l’intégration dans myFulfillment

1. Accédez à votre interface **myFulfillment** , puis rendez-vous dans le menu**Intégrations** .
2. Cliquez sur **Créer une nouvelle intégration** .
3. Dans la section **Général** , attribuez un nom à cette intégration (ex :*Sellsy* ).
4. Dans la section **Configuration** :
  - Renseignez les champs **Client ID** et**Client Secret** obtenus à l’étape précédente.
  - Cliquez sur **Enregistrer** .
5. Renseignez les champs 

#### Étape 3 – Paramétrages complémentaires

##### Export clients

- **Taux de taxe** : sélectionnez une catégorie**TTC** .
- **Compte comptable** : spécifiez le compte à affecter aux clients dans Sellsy.

##### Export commandes

- **Boutiques** : sélectionnez les boutiques dont les commandes seront exportées vers Sellsy.
- **Exporter depuis** : définissez une date à partir de laquelle les commandes seront transmises (les commandes antérieures seront ignorées).
- **Méthodes d’expédition** : configurez la correspondance entre les transporteurs myFulfillment et ceux de Sellsy.
- **Méthodes de paiement** : mappez les moyens de paiement utilisés entre les deux systèmes.

##### Export produits

- **Exporter les coûts** : si cette option est activée, le**CUMP** (coût unitaire moyen pondéré) calculé dans myFulfillment sera exporté comme**coût d’achat** dans Sellsy.
- **Activer la mise à jour** : si activée, cette fonction ajoutera les nouveaux produits et mettra à jour les produits existants.
 ⚠️ *À utiliser avec précaution : cela peut ralentir les performances du système.*

##### Export de stock

- **Entrepôts BMS** : sélectionnez les entrepôts à prendre en compte ; la somme de leurs stocks sera exportée.
- **Entrepôt Sellsy** : définissez l’entrepôt de destination dans Sellsy pour l’export des niveaux de stock.

#### Finalisation

Une fois l'intégration configurée et enregistrée, les synchronisations pourront démarrer automatiquement selon la planification définie dans myFulfillment

### Pas encore de compte Sellsy ?

## Vous avez besoin d'aide avec cette intégration ?

Pour tout besoin d’assistance ou autre questions relatives à ce connecteur, vous pouvez :

- Consulter la [FAQ de Boostmyshop](<http://Entrepôts BMS : sélectionnez les entrepôts à prendre en compte ; la somme de leurs stocks sera exportée.Entrepôt Sellsy : définissez l’entrepôt de destination dans Sellsy pour l’export des niveaux de stock.>)
- Contacter le **support client de Boostmyshop** :[help@boostmyshop.com](http://help@boostmyshop.com) .