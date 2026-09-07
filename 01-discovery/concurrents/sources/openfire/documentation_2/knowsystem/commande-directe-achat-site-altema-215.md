---
url: https://documentation.openfire.fr/knowsystem/commande-directe-achat-site-altema-215
url_finale: https://documentation.openfire.fr/knowsystem/commande-directe-achat-site-altema-215
date_collecte: 2026-09-06
destination: documentation_2
---

Un connecteur d'achat a été développé pour faciliter la transmission des commandes d'achat du fournisseur Modinox directement depuis OpenFire vers le site Altema. Ce connecteur nécessite un compte acces-pro.altema.pro ainsi qu'un paramétrage préalable.

## Etape préliminaire

Vérifiez que le module de Connecteur Modinox soit bien installé sur votre base.

Pour cela, rendez-vous dans Configuration > Connecteurs > Configuration


Si ce menu n'apparaît pas, demandez l'installation du module Modinox au support OpenFire, par mail à l'adresse support@openfire.fr.

## Paramétrage

Les identifiants à la plateforme acces-pro.altema.pro doivent être ajoutés à la plateforme OpenFire.

Pour les renseigner, rendez-vous dans **Configuration > Connecteurs > Configuration :** 

- identifiant Modinox : information notée sur le site Altema "Mon compte>Informations>Code client"

- mot de passe : mot de passe pour accéder à votre compte sur le site Altema

- Email du client : information notée sur le site Altema "Mon compte>Informations>adresse de messagerie"

Le champ clé d'utilisation qui est généré automatiquement ne doit pas être modifié.

**Attention:** Dans la partie Fournisseurs Modinox, pensez bien à ajouter votre fournisseur :

## Commande d’achat Directe

**Accès : Ventes>Ventes>Devis** 

Lorsqu'un devis est confirmé en bon de commande client, un bon de livraison client est automatiquement généré. Ce bon de livraison reprend la liste des produits qui seront à livrer au client.

Il est accessible:

- soit depuis le bon de commande client en cliquant sur le bouton du tableau de bord Livraison,
- Soit depuis le menu Inventaire, puis livraison.

Depuis ce Bon de livraison client, il est alors possible de générer une demande de prix qui pourra être confirmée en une commande d’achat.

Pour cela, deux solutions sont possibles depuis le bon de livraison client :

- Soit ligne par ligne en cliquant sur l'icône d’engrenages disponible pour chaque ligne :

- Soit globalement via le bouton Approvisionner. Cela va alors automatiquement générer autant de demandes de prix que de fournisseurs.

Une fois les demandes de prix créées, celles-ci sont accessibles depuis l'icône Achats disponible sur le bon de livraison:

Il est alors possible, dans le cas où le fournisseur est l'un des fournisseurs renseigné sur le connecteur et est une plateforme d'Altema, de passer la commande en un clic, via le bouton Commande Modinox :

Une fenêtre récapitulative s’ouvre permettant d’ajuster les articles et les quantités.

- Les lignes noires sont les articles dont la correspondance a été retrouvée sur le site d'Altema.
- Les lignes beiges sont les articles dont la correspondance n’a pas été trouvée sur le site d'Altema. Elles seront dans tous les cas envoyées sur le site.

Cliquez sur ENVOYER pour transférer la commande sur le site d'Altema.

## Récapitulatif de la commande sur le site Altema

Sur le site d'Altema, la commande se retrouve dans Liste d'achat.

La commande provenant d'OpenFire sera considérée comme une liste d'achat et la date du transfert est notée.

Pour passer la commande sur le site, il faudra alors créer la commande à partir de cette liste d'achat.