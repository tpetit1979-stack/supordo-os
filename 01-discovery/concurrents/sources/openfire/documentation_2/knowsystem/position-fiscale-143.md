---
url: https://documentation.openfire.fr/knowsystem/position-fiscale-143
url_finale: https://documentation.openfire.fr/knowsystem/position-fiscale-143
date_collecte: 2026-09-06
destination: documentation_2
---

Les Positions fiscales vous permettent de créer des règles pour adapter automatiquement les taxes et les comptes utilisés sur vos devis, vos commandes ou vos factures.

Elles peuvent être appliquées automatiquement ou en fonction de certaines règles, manuellement sur un devis, ou encore être attribuées à un contact particulier.

## Configurer les positions fiscales

Attention: Les positions fiscales sont déjà préconfigurées sur votre base de données. Nous vous conseillons de contacter le support OpenFire avant toutes modifications. De plus, dans un contexte multi-société, la position fiscale doit être définie depuis chacune des sociétés.

Vous pouvez paramétrer et consulter les positions fiscales depuis le menu Comptabilité > Configuration > Taxes > Position fiscale.

Pour chaque position fiscale, vous trouverez un onglet correspondance des taxes contenant:

- Le champ Taxe par défaut permet de saisir la taxe à utiliser quand aucune taxe n'est renseignée dans le produit ni dans sa catégorie ;
- Une table de correspondance des taxes. Ce tableau permet de remplacer une taxe par une autre. Ainsi, je peux définir que la taxe TVA de base (vente) qui est celle définie par défaut sur les articles soit remplacée par la taxe TVA collectée Vente 5.5% lorsque je sélectionne la position fiscale Vente 5.5

  Plus d'information sur le paramétrage [des taxes](https://documentation.openfire.fr/knowsystem/taxes-193)

## Application automatique

Vous pouvez configurer vos positions fiscales pour qu’elles soient appliquées automatiquement, selon un ensemble de conditions.

Pour se faire, ouvrez la position fiscale que vous souhaitez modifier et cliquez sur Détecter automatiquement. Vous pouvez configurer quelques conditions :

- TVA requise : Le numéro de TVA doit être indiqué dans le formulaire de contact du client.
- Groupe de pays / Pays : cela permet d'appliquer la position fiscale dès lors que le pays en question est renseigné sur une fiche contact.

## Appliquer une position fiscale à un devis

Depuis un devis, un bon de commande, ou une facture, vous pouvez sélectionner manuellement la position fiscale à utiliser avant d’ajouter des lignes de produits:

  Plus d'information sur [les devis](https://documentation.openfire.fr/knowsystem/creer-un-devis-1)

## Assigner une position fiscale à un partenaire

Vous pouvez définir manuellement quelle position fiscale doit être utilisée par défaut pour un partenaire spécifique. Pour cela, rendez-vous sur la fiche du contact, puis dans l'onglet Comptabilité:

*Dans l'exemple ci-dessus, la position fiscale Ven-5.5 sera définie par défaut lorsqu'un devis ou un bon de commande sera fait pour ce contact.*

   Plus d'information sur [la gestion des contacts](https://documentation.openfire.fr/knowsystem/gestion-avancee-des-contacts-109)