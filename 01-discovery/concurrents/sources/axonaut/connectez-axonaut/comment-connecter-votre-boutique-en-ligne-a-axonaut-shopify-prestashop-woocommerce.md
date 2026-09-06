---
source: https://support.axonaut.com/connectez-axonaut/comment-connecter-votre-boutique-en-ligne-a-axonaut-shopify-prestashop-woocommerce/
categorie: 16. Connectez Axonaut à vos outils
titre: Comment connecter votre boutique en ligne à Axonaut ? (Shopify, Prestashop, Woocommerce)
date_recuperation: 2026-09-05
---

# Comment connecter votre boutique en ligne à Axonaut ? (Shopify, Prestashop, Woocommerce)

Gérer une boutique en ligne demande une organisation rigoureuse, notamment pour suivre les commandes, la facturation et la gestion des clients. Bonne nouvelle : Axonaut vous permet d’automatiser ces processus en synchronisant votre boutique Shopify, PrestaShop ou WooCommerce avec votre compte Axonaut.

Dans ce tutoriel, nous vous expliquons étape par étape comment connecter votre boutique en ligne à Axonaut afin de centraliser vos ventes et optimiser la gestion de votre activité. Suivez le guide !

## Connecter Shopify à Axonaut

### Précisions

Avant de procéder à la connexion, vérifiez bien que vous avez souscrit au minimum au forfait « Shopify ». Le forfait basic ne permet pas la connexion avec l’outil.

De plus, les prix affichés dans les lignes de factures sont en HT dans Axonaut alors que Shopify affiche du TTC dans les commandes. Pour continuer à opter pour un affichage en TTC, vous pouvez vous rendre dans la clé à molette > Configuration > Devis & Factures et cliquer sur TTC dans la colonne montant.

### Le paramétrage dans Shopify

1) Rendez-vous dans les paramètres de votre boutique Shopify, cliquez sur « Application et canaux de vente » et « Développer des applications ».

![](https://blog.axonaut.com/support/wp-content/uploads/2024/08/image-1-shpify.png)

2) Créez une application « Axonaut »

![](https://blog.axonaut.com/support/wp-content/uploads/2024/08/capture-2-shopify.png)

3) Dans l’onglet « Configuration » de votre application, cliquez sur « configurer » l’intégration de l’API de l’interface administrateur.

![](https://blog.axonaut.com/support/wp-content/uploads/2024/08/capture-3-shopify.png)

4) Sélectionnez les portes d’accès suivantes :

- Client(e)s : read_customers
- Commandes : read_orders
- Produits : read_products
- Stocks : read_inventory

Cliquez ensuite sur « sauvegarder »

5) Rendez-vous dans « Identifiants d’API » et cliquez sur « installer l’application ».

6) Cliquez sur « Révélez le jeton une fois ». C’est un jeton accès à l’API nécessaire à la connexion. **ATTENTION ! Notez-le bien car vous ne pouvez le voir qu’une seule et unique fois. **

![](https://blog.axonaut.com/support/wp-content/uploads/2024/08/capture-4-shopify.png)

### Le paramétrage dans Axonaut

1) Rendez-vous dans la clé à molette, Marketplace et recherchez l’application Shopify.

2) Cliquez sur « Activer » et « c’est parti ».

3) Entrez votre jeton d’accès ainsi que le lien de votre boutique en entier.

![](https://blog.axonaut.com/support/wp-content/uploads/2024/08/capture-5-shopify.png)

4) Une fois la connexion activée, vous pouvez importer tous vos clients, produits et commandes Shopify dans votre compte Axonaut.

- En important vos produits, la description de vos produits sera la même utilisée dans Shopify.
- En important vos commandes, cela ne créera pas une commande dans Axonaut mais vous retrouverez les factures correspondantes.

## Connecter Prestashop à Axonaut

Afin de vous permettre de gagner du temps sur la gestion de votre site, nous avons développé un plugin Prestashop. Connecté à Axonaut, il vous permettra d’automatiser toutes les tâches chronophages.

En installant le plugin sur votre site e-commerce, vous retrouverez dans Axonaut l’intégralité de vos ventes, de vos clients, de vos stocks en temps réel. Les factures seront générées par notre logiciel agréé.

Pour télécharger le plugin, rendez-vous dans la clé à molette > Marketplace et recherchez Prestashop dans la liste disponible.

### Les fonctionnalités du plugin Prestashop – Axonaut

[![](https://support.axonaut.com/wp-content/uploads/2023/10/File1578414690175expires1619193600ampsignaturefbda6580b10f84d6c085d3293912bec33fd3723acead4db2f47dabaaa3a72c78-75.jpg)](https://support.axonaut.com/wp-content/uploads/2023/10/File1578414690175expires1619193600ampsignaturefbda6580b10f84d6c085d3293912bec33fd3723acead4db2f47dabaaa3a72c78-75.jpg)

#### Produits :

1. Synchronisation des produits directement via le bouton de synchronisation dans le module.

2. Synchronisation du nom, description, prix unitaire, TVA, poids, et stock du produit.

3. Création d’un produit dans Axonaut dès sa création dans PrestaShop.

4. Mise à jour du nom, description, prix unitaire, TVA et stock à chaque vente du produit.

#### Clients :

1. Synchronisation des clients directement via le bouton de synchronisation dans le module

2. Synchronisation du nom du client, email, adresse postale, numéros de téléphone fixe et portable.

3. Mise à jour du nom du client, adresse postale, numéros de téléphone fixe et portable lors d’une vente.

4. Création d’un prospect dans Axonaut lors d’une inscription à la boutique PrestaShop.

#### Factures :

1. Une facture est générée dans Axonaut lors que la commande dans PrestaShop est émise.

2. Prise en compte des TVA.

3. Prise en compte des frais de port.

4. Prise en compte des emballages cadeaux.

*Attention :*

- *Ce plugin est en BETA, il peut souffrir d’instabilité, n’hésitez pas à nous remonter d’éventuels bugs auxquels vous seriez confrontés.*
- *Module développé sous la version 1.7.5.2 de Prestashop. Si votre version est inférieure, le module peut ne pas être fonctionnel pour celle-ci. *
- *Le mode multiboutique n’est actuellement pas compatible Axonaut.*

## Connecter Woocommerce à Axonaut

En installant le plugin sur votre site e-commerce, vous retrouverez dans Axonaut l’intégralité de vos ventes, de vos clients, de vos stocks en temps réel. Les factures seront générées par notre logiciel agréé.

### Les fonctionnalités du plugin WooCommerce – Axonaut

#### Produits :

1. Synchronisation des produits directement via le bouton de synchronisation dans le module.

2. Synchronisation du nom, description, prix unitaire, TVA, poids, et stock du produit.

3. Création d’un produit dans Axonaut dès sa première vente dans WooCommerce.

4. Mise à jour du nom, description, prix unitaire, TVA et stock à chaque vente du produit.

#### Clients :

1. Synchronisation des clients directement via le bouton de synchronisation dans le module

2. Synchronisation du nom du client, email, adresse postale, numéro de téléphone fixe.

3. Mise à jour du nom du client, adresse postale, numéro de téléphone fixe lors d’une vente.

4. Création d’un prospect dans Axonaut lors d’une inscription à la boutique WooCommerce.

#### Factures :

1. Une facture est générée dans Axonaut dès la commande passée dans WooCommerce.

2. Prise en compte des TVA.

3. Prise en compte des frais de port.
4. Prise en compte des codes de réduction.

*Attention :*

- *Les produits variables ne sont pour l’instant pas compatibles avec notre plugin.*

💡La connexion entre Woocommerce et Axonaut est bidirectionnelle. Le stock actualisé dans Axonaut remontera donc également dans Woocommerce.

Pour toutes questions supplémentaires, n’hésitez pas à revenir vers nous via le live-chat en bas à droite 😉

Mis a jour le : 17 mars 2025
