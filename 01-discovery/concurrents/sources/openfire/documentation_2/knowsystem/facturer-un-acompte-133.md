---
url: https://documentation.openfire.fr/knowsystem/facturer-un-acompte-133
url_finale: https://documentation.openfire.fr/knowsystem/facturer-un-acompte-133
date_collecte: 2026-09-06
destination: documentation_2
---

Le règlement d'un acompte passe par l'émission d'une facture d'acompte.

Pour cela, une catégorie d’article spécifique Acompte est préconfigurée dans votre base OpenFire et un compte de revenus par défaut y est associé. 

A savoir: La loi de finances 2022 est venue aligner le régime des acomptes sur les biens sur celui des prestations de services. Dans ce cadre, à partir du 1er janvier 2023, en cas de versement d'un acompte, la TVA sur les livraisons de biens sera exigible dès l'encaissement de cet acompte, par le fournisseur et non plus lors de la livraison du bien

## Saisir une facture d’acompte



Les factures d’acompte se génèrent depuis une commande client d’origine. Ainsi, pour facturer un acompte, rendez-vous sur le bon de commande a facturer, puis cliquez sur créer une facture*

**Cette fonction n’est proposée que pour les commandes validées.*

Dans la fenêtre qui s'ouvre, vous aurez alors la possibilité de saisir le montant de votre facture d'acompte en pourcentage ou de saisir directement le montant de l'acompte.

*Les factures d’acompte sont généralement générées sur la base de la saisie d’un montant TTC, mais selon votre configuration le montant peut être a saisir en HT.*

Si plusieurs articles *Acompte* sont configurés, le choix de l’article d'acompte à utiliser est proposé.

En cliquant sur Créer et afficher les factures, le logiciel vous créera une facture d'acompte en brouillon que vous pourrez alors valider si tout est correct.

La facture d’acompte ainsi générée ne reprend que la ligne Acompte

Dans l’onglet « Autres informations », la facture d’acompte reprend les informations suivantes :

- Position fiscale de la facture (si défini) ;
- Document d’origine : commande à l’origine de la facture ;
- Numéro de la pièce comptable (uniquement lorsque la facture est validée) ;
- Compte comptable d’imputation ;
- Description de la TVA : nom de la taxe, compte comptable associé et montant.

Quand la facture d’acompte est validée, il faut créer le paiement à partir de cette facture d’acompte.

Le paiement doit être identique au montant de la facture d’acompte.

Il sera alors automatiquement lettrer à la facture d'acompte.

  Plus d'information sur [Enregistrer un paiement](https://documentation.openfire.fr/knowsystem/enregistrer-un-paiement-161)  et [Associer Paiement et factures](https://documentation.openfire.fr/knowsystem/associer-paiements-et-factures-162#scrollTop=0)

 Lorsqu’une facture d’acompte est générée, une ligne de commande acompte est ajoutée au bon de commande. Cette ligne a les particularités suivantes :

- Quantité commandée et livrée à 0,

- Prix unitaire correspondant au montant de l’acompte facturé

## Saisir la facture finale

Pour générer la facture finale, il faut également se rendre sur le bon de commande. En cliquant sur créer une facture, vous aurez ensuite la possibilité d'émettre une facture de solde, en sélectionnant Lignes facturables (acomptes déduits).

  Plus d'information sur __[Créer une facture finale](https://documentation.openfire.fr/knowsystem/creer-ma-facture-finale-145)__