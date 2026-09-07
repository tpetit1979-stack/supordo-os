---
url: https://documentation.openfire.fr/knowsystem/generation-du-bon-de-livraison-59
url_finale: https://documentation.openfire.fr/knowsystem/generation-du-bon-de-livraison-59
date_collecte: 2026-09-06
destination: documentation_2
---

Lorsque vous validez une commande client, un bon de livraison client est automatiquement généré.

Le bon de livraison reprend la liste des produits qui seront à livrer au client.

Ce bon de livraison est accessible:

- soit depuis le bon de commande client en cliquant sur le bouton Livraison:

- soit depuis le menu **Inventaire** , puis livraison:

## Structure du Bon de Livraison

Le bon de livraison est structuré comme suit :

- Numéro du BL : exemple: COMPAGNY/OUT/00094 → le OUT signifie que ce document concerne une livraison de marchandise = les marchandises vont sortir de vos stocks / entrepôts.
- Partenaire : Identification du client destinataire de la livraison.
- Date prévue : date à laquelle la livraison du client est attendue ; si le BL est relié à une intervention planning, cette date sera synchronisée avec la date de cette intervention.

L’onglet Demande initiale reprend l’ensemble des lignes de la commande client d’origine. Les approvisionnements peuvent donc être réalisés depuis cet onglet.

L’onglet Opérations reprend quant à lui l’ensemble des lignes prêtes à être livrées au client final. La validation du BL (ou Retour de pose), sera réalisée depuis cet onglet.

## Approvisionnements depuis le Bon de Livraison

Depuis ce Bon de livraison client, il est alors possible de générer une demande de prix.

La demande de prix correspond à une demande de devis au fournisseur.

Cette étape, n'est pas obligatoire mais elle importante dans le processus achat . La demande de prix consiste à préparer la liste des produits dont on a besoin d'acheter, dans le but d'approvisionnement de stock. Cette liste sera envoyée par email à notre fournisseur pour qu'il nous envoie la demande avec les prix à jour. 

Une demande de prix peut-être confirmée ou refusée. Lorsqu’elle est confirmée, elle devient une commande d’achat.

*Plus d'informations sur [la génération d'une commande d'achat](https://documentation.openfire.fr/knowsystem/generer-une-commande-d-achat-157)*