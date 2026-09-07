---
url: https://documentation.openfire.fr/knowsystem/lettrage-comptable-192
url_finale: https://documentation.openfire.fr/knowsystem/lettrage-comptable-192
date_collecte: 2026-09-06
destination: documentation_2
---

Le lettrage comptable (ou réconciliation comptable) est une opération consistant à relier des écritures comptables entre elles, via une référence de lettrage. Cela permet, par exemple de faire le lien entre des factures et des paiements ou des avoirs.

Le lettrage permet ainsi d’effectuer le suivi de l’encaissement des factures et d’identifier, plus aisément, celles qui sont en attente de règlement.

Il existe plusieurs méthodes de lettrage sur OpenFire :

- Lettrage à la facturation,
- Lettrage piloté en comptabilité,
- Lettrage à partir des écritures comptables.

## Lettrage à la facturation



**Accès** : **Comptabilité>Ventes ou Achats>Factures Clients ou Factures Fournisseurs**

Sur OpenFire, une facture peut être liée à un paiement soit en passant par :

 - **enregistrer un règlement** : la saisie d’un paiement depuis la facture engendre un lettrage automatique avec la facture.

 - **Ajouter** qui se trouve en dessous du Montant dû de la facture : dès qu'une facture est validée, OpenFire vous avertira si un paiement est en circulation et donc non rapproché pour ce client ou ce fournisseur. Ce message est visible via un message en haut de fenêtre:

Dans ce cas, vous pouvez rapprocher ce paiement à la facture près des totaux au bas, sous la rubrique « en cours de crédits ».

Le paiement sera alors lettré à la facture. Plusieurs paiements peuvent être liés à la même facture. 

Une fois que les paiements seront totalement effectués et que le montant dû sera à zéro,  le lettrage est total, et la facture est en état payée.*Ecart de paiements :*

Si le montant du paiement est différent au solde dû de la facture et qu'aucun avoir ne sera effectué car le montant de l'écart est trop faible (inférieur à 1 euro), il est possible de lettrer entièrement la facture et la passer en état payé. Pour cela, lorsque vous saisissez le paiement et que le logiciel constate un écart entre le paiement et la facture, le champ Différence de paiement s'affiche.

Vous avez 2 options :

- Laisser ouvert : le paiement s'affectera à la facture et l'écart du paiement restera en attente de circulation.

- Marquer la facture comme payée complètement : le logiciel va générer une pièce comptable différente afin que la facture se solde complètement.

         * Si le montant de l'écart est en votre défaveur, dans le champ Comptabiliser la différence dans, il faut mettre **impérativement** le compte : **658000** ou un compte commençant par **658...**

         * Si le montant de l'écart est en votre faveur, dans le champ Comptabiliser la différence dans, il faut mettre impérativement le compte : **7**58000 ou un compte commençant par **758...**

**A savoir :** Toutes les factures, avoirs et paiements validés génèrent des pièces comptables. Le lettrage effectué au niveau de la facturation est aussi visible directement dans la comptabilité OpenFire. A l'inverse, les factures et paiements enregistrés dans la comptabilité ne remontent pas dans la gestion de la facturation et des paiements. En revanche, le lettrage effectué directement en comptabilité sera répercuté dans la gestion de la facturation. Il est donc possible de piloter le lettrage directement en comptabilité.

## Lettrage piloté en comptabilité

**Accès :** *Comptabilité > Conseiller > Correspondance des factures et des paiements*

Dès lors que les factures et paiements ne sont générés que dans la partie *Comptabilité>Ventes ou Achats,* il est possible de contrôler les lettrages / rapprochements entre les paiements, avoirs et les factures via la Correspondance des factures et des paiements. 

Cette page vous permettra d'afficher la liste des factures, des avoirs et des paiements non rapprochés n'émanant que de la gestion des factures et paiements. 

  Plus d'information sur [la](https://documentation.openfire.fr/knowsystem/correspondance-des-paiements-et-des-factures-167) [Correspondance des paiements et des factures](https://documentation.openfire.fr/knowsystem/correspondance-des-paiements-et-des-factures-167)

*Ecart de paiements :*

Si le montant du paiement est différent de celui de la facture et qu'aucun avoir ne sera effectué car le montant de l'écart est trop faible (inférieur à 1 euro), il est possible de lettrer entièrement en cliquant sur Créer l'ajustement après avoir sélectionner les lignes à lettrer.

Pour créer l'ajustement :

- sélectionner le compte 658... si l'écart est en votre défaveur

- sélectionner le compte758... si l'écart est en votre faveur.

- Journal : choisir un journal de type "Opérations diverses"

- Libellé : vous notez la raison de l'ajustement : "Ecart règlement"

- Montant : le montant proposé est le montant de l'écart suite à la sélection des lignes au-dessus

- cliquer sur LETTRER

   Il est possible de l*ettrer d’un seul coup toutes les entrées équilibrées présentées en utilisant les touches :* *Ctrl+Entrée*

## Lettrage à partir des écritures comptables


**Accès :** *Comptabilité > conseiller > écritures comptables*

Vous retrouvez toutes les écritures émanant de la gestion de la facturation et des paiements mais aussi les écritures émanant des pièces comptables saisies directement en passant par **Comptabilité>Conseiller>Pièces comptables**.

Utilisez les filtres et les regroupements afin d’afficher uniquement les écritures à lettrer.

Exemple :

- Filtre « payable » : n’affiche que les écritures de comptes fournisseurs ;
- Filtre « recevable » : n’affiche que les écritures de comptes clients ;
- Filtre « non lettré » : permet de n’afficher que les écritures non lettrées ;

Grouper par compte : permet de grouper les écritures en fonction du compte de tiers à lettrer ;

Filtre sur le numéro de compte : permet de ne conserver à l’écran que les écritures d’un même compte afin de faciliter le lettrage.

Sélectionner ensuite les écritures à lettrer, puis cliquez sur Action > Lettrer les écritures

## Consultation des lettrages

Pour retrouver un ensemble d’écritures lettrées, vous pouvez :

- Filtrer sur les références de lettrage
- Regrouper les écritures comptables par référence de lettrage

Depuis une écriture comptable lettrée, vous pouvez également retrouver les écritures du même lettrage en cliquant sur la référence de lettrage présentée dans l’écriture.

## Rapport des écritures non lettrées

Vous pouvez accéder à un rapport des écritures non lettrées depuis le menu **Rapports > Écritures non lettrées.**

Ce rapport correspond au grand livre des comptes auxiliaires (clients / fournisseurs) non lettrés à date.

Différents filtres sont alors possibles, comme la possibilité de n'exporter que les comptes clients ou fournisseurs:

Ce rapport peut être ouvert dans le navigateur ou exporter au format .XLSX ou .PDF.