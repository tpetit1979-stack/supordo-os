---
source: https://support.openfire.fr/hc/fr/articles/24374815547420-Comment-r%C3%A9aliser-un-approvisionnement-%C3%A0-la-contremarque
categorie: Utiliser OpenFire
titre: Comment réaliser un approvisionnement à la contremarque ?
date_recuperation: 2026-09-05
---

# Comment réaliser un approvisionnement à la contremarque ?

Cet article vous guide à travers les 6 étapes du flux "contremarque", de la signature du devis jusqu'à la facturation client, en passant par les étapes d'approvisionnement et de réception des marchandises.

Cet article contient les sections suivantes :

[**Section 1 : Qu'est-ce qu'un approvisionnement à la contremarque ?**](#h_01KCY68X5SZTASZ3369347DHCN)

- [Présentation](#h_01KCY45EY5DF0MBE2YBZY031JE)
- [Schéma opérationnel](#h_01KCY4A3PA99Z2D97Y24FQ2DWK)

[**Section 2 : Configuration et prérequis**](#h_01KCY68FYW02T73T0Q9JBK58K3)

[**Section 3 : Le flux opérationnel en 6 étapes**](#h_01KCY683YYV01EM0STN0RXCC2M)

- [Étape 1 : Confirmation du devis](#h_01KCY3CG3BWJMCQREVV58VRENR)
- [Étape 2 : Lancement de l'approvisionnement depuis le BL](#h_01KCY3CG3FK0TAD6GR4QXWDVCK)
- [Étape 3 : Validation de la commande d'achat](#h_01KCY3CG3RB732138XE3K7ZS64)
- [Étape 4 : Réception des produits](#h_01KCY3CG3V408GCR54A2FC5ZBA)
- [Étape 5 : Validation de la livraison client](#h_01KCY3CG4F47AGXJC561T8PV98)
- [Étape 6 : Facturation](#h_01KCY3CG4JA2661B3B23QN3DGH)

[**Bonnes pratiques**](#h_01KD41CXWT966TDNSYFHZ6M4GR)

[**Pour aller plus loin**](#h_01KD41R42VFWTYTE1BF2XSQF02)

---

# Section 1 : Qu'est-ce qu'un approvisionnement à la contremarque ?

## Présentation

L'approvisionnement à la contremarque est une **méthode de gestion "juste-à-temps"** qui consiste à n'acheter un produit qu'une fois celui-ci vendu à votre client .

Contrairement à l'approvisionnement **Standard** (gestion sur stock), où l'entreprise achète des volumes pour servir ses clients rapidement , **la contremarque lie automatiquement chaque commande d'achat à un client spécifique**.

Cette méthode repose sur plusieurs principes clés :

- **Flux tendu** : vous n'achetez que ce que vous vendez, ce qui permet d'optimiser votre trésorerie.
- **Stock éphémère** : le produit ne reste pas en stock car il est réservé à une livraison client dès sa réception.
- **Délai de traitement** : comme le produit n'est pas disponible immédiatement en rayon, le délai de livraison final dépend du temps de réponse de votre fournisseur.

## Schéma opérationnel

![Schéma AK - Processus d'approvisionnement à la contremarque.jpg](https://support.openfire.fr/hc/article_attachments/24375461554972)

Ce schéma illustre le parcours de gestion pour réaliser un approvisionnement à la contremarque dans OpenFire : la confirmation du **Devis** (1) génère un **Bon de livraison** depuis lequel sont déclenchés les **Achats contremarques** fournisseur (2, 3). Une fois les produits reçus (4) , la livraison client peut-être validée (5), permettant enfin à la **Comptabilité** d'éditer les factures client et fournisseur (6).

# Section 2 : Configuration et prérequis

| 🧩**Prérequis** → Configurer vos articles pour l'achat et le stock (en cours) 🧩**Prérequis** → Créer un bon de livraison, de réception ou un transfert interne (en cours) |
| --- |

# Section 3 : Le flux opérationnel en 6 étapes

## Étape 1 : Confirmation du devis client

Tout commence par la validation de votre proposition commerciale.

Suivre le chemin d'accès suivant : `Ventes > Devis`.

1/ Sélectionner votre devis contenant des produits stockables ou consommables.

2/ Cliquer sur le bouton **Confirmer**.

3/ Le système génère automatiquement un **Bon de Livraison (BL)** en haut à droite de l'écran.

## Étape 2 : Lancement de l'approvisionnement depuis le BL

Une fois le BL créé, vous devez commander les produits manquants.

1/ Pour retrouver votre **Bon de livraison (BL), **vous pouvez soit :

- Cliquer sur le Smart Bouton **Livraison** qui est apparu sur votre commande.

![](https://support.openfire.fr/hc/article_attachments/24376263462812)

- Retrouver la liste de tous vos **Bons de Livraison (BL)** en suivant le chemin d'accès suivant : `Inventaire > Vue d'ensemble > Livraisons`.

![](https://support.openfire.fr/hc/article_attachments/24376263463196)

2/ Depuis votre BL, Cliquer sur le bouton **APPROVISIONNEMENT**.

![](https://support.openfire.fr/hc/article_attachments/24414343366428)

3/ Dans la fenêtre qui s'ouvre, sélectionner les produits concernés

![](https://support.openfire.fr/hc/article_attachments/24377105218460)

Détails de la fenêtre d'approvisionnement :

1. **Choisir à la ligne** **les produits que vous souhaitez approvisionner.** Par défaut, seules les lignes qui ont besoin d’être approvisionnées sont cochées (= les produits stockables avec le statut “Attente de disponibilité” ou “Partiellement disponible”).
2. Utiliser les boutons **SELECTIONNER TOUT **ou **DESELECTIONNER TOUT** au besoin pour ajuster rapidement votre sélection.
3. Lancer l'**APPROVISIONNEMENT DE CONTREMARQUE **(par opposition à l'APPROVISIONNEMENT STANDARD qui lui créera un approvisionnement sans le lier au BL et à la commande client en cours).

4/ Cliquer sur **APPROVISIONNEMENT DE CONTREMARQUE**.

À la suite de l'approvisionnement :

- OpenFire créera **une commande pour chaque fournisseur** des lignes approvisionnées. Exemple : vous commandez à la contremarque le poêle chez Seguin et les éléments de conduit chez Poujoulat ; OpenFire créera une demande de prix pour Seguin, et une autre pour Poujoulat.
- Les commandes sont créées à l'état **Demande de prix** : elles devront être validées (suite à la réception de la confirmation de la commande par le fournisseur notamment).
- Chaque **approvisionnement **généré est **lié à la livraison** (= une fois les quantités reçues, ces dernières seront directement réservées pour ce BL d'origine).
- Une fois l'approvisionnement à la contremarque réalisé, le bon de livraison et les lignes approvisionnées passent à l'état **En attente d'une autre opération **(= la réception des marchandises).
- Le **Mode d'approvisionnement** est valorisé pour chaque ligne, ainsi que le **Bon de commande fournisseur associé.**

| 📓**Pour aller plus loin** → Créer un bon de livraison, de réception ou un transfert interne 📓**Pour aller plus loin** → Réaliser un approvisionnement depuis un Bon de livraison 📓**Pour aller plus loin** → Consulter vos stocks depuis un produit, une ligne de commande, ou une ligne de facture |
| --- |

## Étape 3 : Validation de la commande d'achat fournisseur

Votre commande d'achat est maintenant créée en tant que "Demande de prix".

1/ Pour retrouver votre commande, vous pouvez soit :

- Cliquer sur le Smart Bouton **Achat** qui est apparu sur votre BL.

![](https://support.openfire.fr/hc/article_attachments/24400057470876)

- Retrouver la **liste de toutes vos commandes** en suivant le chemin d'accès suivant : `Achats > Commandes > Demandes de prix`. Vous pouvez rechercher : 

  - Par le Document source (= la commande client d'origine).
  - Le client de la contremarque.
  - le fournisseur.

![](https://support.openfire.fr/hc/article_attachments/24414982230428)

2/ Vérifier les informations clés de votre commande :

- Le vendeur du produit (=Fournisseur).
- Les quantités et le prix des produits commandés.
- Le lieu et la date de livraison demandés.
- La commande d'origine et le client associé.

![](https://support.openfire.fr/hc/article_attachments/24467020866716)

3/ **ENVOYER PAR EMAIL** la demande de prix à votre fournisseur.

La commande passe à l'état ENVOYÉ dès l'envoi par email réalisé.

4/ Cliquer sur **CONFIRMER LA COMMANDE** pour valider l'achat auprès du fournisseur, une fois la confirmation reçue.

À la confirmation de la commande :

- La commande passe à l'état BON DE COMMANDE.
- OpenFire prépare le Bon de Réception, en attente de la réception des marchandises.
- La date prévue de la réception est calculée suivant la date de livraison demandée.

| 📓**Pour aller plus loin** → Créer une demande de prix ou une commande fournisseur 📓**Pour aller plus loin** → Envoyer la demande de prix à votre fournisseur |
| --- |

## Étape 4 : Réception des produits

Dès que le fournisseur vous livre, vous devez entrer les produits en stock.

1. Pour accéder au bon de réception : 

  1. Depuis la commande fournisseur : 

    1. Cliquer sur le bouton Smart Bouton **Réception **qui est apparu sur votre commande fournisseur.
    2. Ou cliquer sur **RECEVOIR LES PRODUITS** pour arriver directement dans le bon de réception (BR)
  2. Retrouver la liste de tous vos bons de réceptions (BR) en suivant le chemin d'accès suivant :  `Inventaire > Vue d'ensemble > Réception`, puis utilisez les fonctions de recherche.
2. Utiliser le bouton **COPIER LES QUANTITÉS** pour remplir la colonne **Fait**.
3. Cliquer sur **VALIDER**.

| 📓**Pour aller plus loin** → Créer un bon de livraison, de réception ou un transfert interne 📓**Pour aller plus loin** → Retrouver et piloter vos opérations en cours (BL, BR, Transfert) (en cours) |
| --- |

## Étape 5 : Validation de la livraison client

Les produits étant désormais en stock, vous pouvez finaliser la livraison chez votre client.

1. Retourner sur le **Bon de Livraison (BL)** initial.
2. Le statut de disponibilité est passé à **Disponible** (en vert).
3. Cliquer sur **VALIDER** pour confirmer que les produits sont posés ou livrés.

## Étape 6 : Facturation finale

Une fois les produits livrés, vous pouvez déclencher la facture.

1. Retourner sur le bon de commande client (Vente).
2. Cliquer sur **CRÉER UNE FACTURE**.

# Bonnes pratiques

- Vérifier toujours que l'option **Peut être acheté** est activée sur la fiche de vos articles, sinon ils n'apparaîtront pas dans les propositions d'achat.
- Vérifier la **configuration **de vos **marques **et de vos **articles **afin de vous assurer que les commandes générées seront conformes à vos **conditions commerciales. **
- Vérifier la **position fiscale** de vos **fournisseurs **au préalable, afin d'être sur que les commandes générées auront le bon régime de TVA.

# Pour aller plus loin

| 📓**Pour aller plus loin** → Configurer vos articles pour les achats et stocks |
| --- |

Mis a jour le : 08/01/2026
