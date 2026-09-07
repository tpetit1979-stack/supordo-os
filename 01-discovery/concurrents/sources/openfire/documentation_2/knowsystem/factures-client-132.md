---
url: https://documentation.openfire.fr/knowsystem/factures-client-132
url_finale: https://documentation.openfire.fr/knowsystem/factures-client-132
date_collecte: 2026-09-06
destination: documentation_2
---

OpenFire vous permet de générer des factures, les envoyer à vos clients par mail et gérer les paiements associés.

Lorsqu'un devis est validé en bon de commande, il est alors possible de créer la facture du client depuis la même fenêtre.

## Politique de facturation


OpenFire prend en charge plusieurs méthodes de facturation:

- Facturer selon la quantité commandée,
- Facturation selon la quantité expédiée.

Cette configuration peut se faire de façon générale ou pour chaque article.

  Plus d'information sur le paramétrage de la __[Politique de facturation](https://documentation.openfire.fr/knowsystem/politique-de-facturation-141)__ 


## Présentation de la facture

1. Numéro de la pièce de facture après validation.
2. Entête de la facture : Nom et adresse de facture du client + Adresse de livraison + Condition de règlement + Date de facturation + Position fiscale + Nom du vendeur + Equipe commerciale
3. Dans l'onglet Lignes de factures, vous ajoutez les éléments qui comprennent au minimum la référence article, la description, le compte comptable associé, la quantité, l'unité de mesure, le prix unitaire de vente, la taxe appliquée et le montant. 
Il est possible d'avoir des informations supplémentaires comme la section, le coût d'achat, la remise en % que vous souhaitez appliquer au client, l'immobilisation associée, le compte analytique...
4. Si vous validez une facture à partir d'un bon de commande ou si vous validez une facture boutique, le smart button Livraison apparaît en haut à droite pour accéder au bon de livraison client.
5. Visualisation de vos marges.
6. Possibilité de noter des informations complémentaires en dessous de la facture.
7. Boutons d'actions
8. Etats de la facture.

Une facture peut avoir les états suivants :

- Brouillon: après création depuis la commande sans numéro ni date,
- Ouverte: après la validation de la facture brouillon,
- Payé : après lettrage des paiements à la facture.


Le système génère des factures qui sont initialement à l’état Brouillon. Ainsi, tant que ces factures ne sont pas validées, elles n'ont pas d’impact comptable au sein du système.

Une fois validée, la facture finale passe au statut « ouverte ».

  **Attention:** Une facture ouverte est numérotée et datée. Pour cette raison, elle ne peut donc pas être supprimée.

En effet, la loi exige le séquençage continu des factures. Ainsi, pour être conforme, une facture doit obligatoirement comporter un numéro unique basé sur une séquence chronologique continue, ce qui implique obligatoirement :

- Un numéro unique pour chaque facture ;
- Une chronologie basée sur la date de création de la facture ;
- Une numérotation chiffrée et continue, et sans rupture inexpliquée. Par exemple, si la numérotation d’une facture est 22/0031, la suivante devra porter le numéro 22/0032.

Dans l'onglet Autres informations, vous retrouvez

- le nom du journal Vente associé à la facture
- le compte comptable du partenaire
- Date d'échéance de la facture
- Niveau de relance : cette option vous permet de gérer vos relances factures.

  Plus d'information sur __Relancer mes factures__

- Date de visite technique : à remplir si vous souhaitez que la date s'affiche sur la facture.
- Etiquette client : reprend les étiquettes notées dans la fiche client
- Pièce comptable de la facture au moment de la validation.
- Compte analytique
- Document d'origine : le document peut provenir d'un bon de commande, d'une intervention ou d'une facture s'il s'agit d'un avoir.
- Type de devis : ce champs peut être utilisé pour effectuer des recherches par type.
- Contient un kit et mode d'impression : le logiciel indique si la facture contient un kit et dans quel format les composants du kits seront imprimés dans la facture.
- Suivi interne : champs libre que vous pouvez utilisez pour suivre vos factures avec des filtres. Ce champ ne sera pas imprimé sur la facture.
- Documents joints : liste des fichiers PDF joints à la facture.

Vous avez aussi le récapitulatif du montant de la TVA et par taux de TVA.

En bas de l'écran, vous avez le RSE pour connaître l'historique des actions effectuées sur la facture.

Dans l'onglet Commentaires, il est possible à tout moment d'insérer des informations complémentaires en haut ou en bas de la facture.

## Créer une facture Pro-forma

L'édition d'une facture Pro-forma est possible en cochant l'option dans le menu Comptabilité > Configuration > Configuration puis dans la partie Facturation et Paiement.

 

Le bouton « Pro-forma » sera alors disponible sur une facture brouillon et génèrera une facture de ce type.

## Créer une facture à partir d'une commande

Pour générer une facture à partir d'un bon de commande, allez dans le menu Ventes>Ventes>Bons de commandes et allez sur la commande concernée. Vérifiez que toutes les lignes de commandes soient facturables (lignes bleues). Si les lignes de commandes sont non facturables (lignes noires), celles-ci n'apparaîtront pas sur la facture en brouillon. Vous devez donc vérifier la politique de facturation sur votre commande et appliquer les actions nécessaires.

Cliquez sur Créer une facture :

OpenFire vous propose plusieurs options :

- Lignes facturables : reprend l'ensemble des lignes facturables (lignes bleues) de la commande sans prendre en compte la ligne d'acompte.

- Lignes facturables (acomptes déduits): reprend l'ensemble des lignes facturables moins les acomptes déjà facturés. Il vous faudra sélectionner cette option si vous souhaitez générer une facture finale à la suite d'une facture d'acompte. Plus d'information sur__[Créer une facture finale](https://documentation.openfire.fr/knowsystem/creer-ma-facture-finale-145)__ 

- Acomptes (pourcentage) et Montant de l’acompte: génération d’une facture d’acompte brouillon sur la base d’un pourcentage ou d’un montant fixe. 
 Plus d'information sur__[Fa](https://documentation.openfire.fr/knowsystem/facturer-un-acompte-133)____[cturer un acompte](https://documentation.openfire.fr/knowsystem/facturer-un-acompte-133)__ 

Le logiciel propose par défaut l'option la plus adaptée : lignes facturables (acomptes déduits). Avec cette option, si aucune facture d'acompte n'a été établie à partir du bon de commande, le logiciel ne reprendra que les lignes facturables.

Quand l'option est choisie, vous cliquez soit sur :

- CREER ET AFFICHER DES FACTURES pour accéder directement à la facture en état Brouillon. Cet état est visible en haut à droite de la fenêtre. Après vérification éventuelle des comptes de revenus et de la TVA, vous pouvez valider la facture. La facture passe ainsi de l’état Brouillon à l’état Ouverte. Un numéro de facture sera alors attribué et une pièce comptable sera générée. Si un paiement a été enregistré avant la validation de la facture, celui-ci n'apparaîtra qu'après la validation de la facture.

- CREER LES FACTURES pour générer la facture brouillon mais vous restez sur le bon de commande. Pour accéder à la facture brouillon et effectuer la validation, il faut donc cliquer sur factures dans le tableau de bord en haut à droite. Vous pourrez ainsi valider la facture brouillon.

   Lorsque la facture a repris toutes les lignes du bon de commande et qu'elle est validée, l'état de la facture noté sur le bon de commande passe en "entièrement facturée".

## Créer une facture à partir du planning intervention

  Plus d'information sur __Facturer mes interventions__

## Créer une facture manuelle

Il est possible de générer des factures directement sans passer par les contrats, les commandes clients ou les interventions. Cela est utile dans le cas où vous ne gérez pas le processus de vente (devis/commande) ou les stocks (bons de livraison/bon de réception). En effet, une facture manuelle ne génère pas de bon de livraison et donc pas de mouvements de stocks. Si vous gérez les stocks et que vous souhaitez créer des factures directement, vous devez créer une facture boutique.

  Plus d'information sur __Factures client Boutique__

Pour générer directement une facture, vous allez dans **Comptabilité > Ventes > Factures Clients**, puis cliquez sur Créer

La facture est à l'état brouillon. Elle est donc modifiable tant que la facture n'est pas validée. Vous notez ensuite les éléments suivants :

- Dans l'entête : nom client ; date de facture qui sera la date du jour par défaut ; position fiscale ; condition de règlement ; ...

 - Dans le corps de la facture : ajoutez les articles en cliquant sur **Ajouter un élément**. Vous avez 2 possibilités : 

* vous recherchez un article et le logiciel reprendra automatiquement le compte comptable et la taxe associée à l'article.

   * si l'article n'existe, vous pouvez noter directement dans **Description** l'intitulé de la ligne à facturer et vous devez renseigner le compte comptable qui sera à affecter ainsi que la taxe :

Si le compte comptable n'existe pas, vous pouvez le créer en suivant la procédure dans l'article [Plan Comptable](https://documentation.openfire.fr/knowsystem/plan-comptable-279).

Lorsque toutes les informations sont notées dans la facture, vous cliquez sur sauvegarder pour vérifier le montant total de votre facture et vous cliquez sur **valider** la facture. Lorsque la facture est validée, vous ne pouvez plus annuler la facture et cette dernière passe à l'état ouverte.

## Imprimer une facture


Lorsque vous imprimez une facture, celle-ci s'enregistre automatiquement dans les pièces-jointes sous un nom commençant par INV. A la prochaine impression, c'est cette facture qui s'imprimera encore.

Ainsi, si vous lettrez ou délettrez des paiements, ou si vous ajoutez/modifiez des commentaires sur la facture par exemple, il faudra au préalable supprimer la facture en pièce-jointe (reconnaissable par son nom commençant par INV) avant de réimprimer la facture pour voir les changements.