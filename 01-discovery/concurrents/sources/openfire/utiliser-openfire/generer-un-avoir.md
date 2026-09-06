---
source: https://support.openfire.fr/hc/fr/articles/19084802918940-G%C3%A9n%C3%A9rer-un-avoir
categorie: Utiliser OpenFire
titre: Générer un avoir
date_recuperation: 2026-09-05
---

# Générer un avoir

Cet article vous présente les différentes méthodes disponibles de génération d'avoir.

Cet article contient les sections suivantes :

- [Les différentes façons de créer un avoir](#h_01JQ9FMJWCM3D9C4ZTM3A6P41C)
- [Créer un avoir depuis une facture](#h_01JQ9FMJWCAMX79CPJG0WKG0HC)
  - [Créer un avoir partiel](#h_01JQ9FMJWCWFPRAXCFFAGGTVT5)
  - [Créer un avoir intégral](#h_01JQ9FMJWCGDETZA2WPC6FFPW2)
  - [Créer un avoir de modification de la facture](#h_01JQ9FMJWC89NYJ9Y54JXPTFV1)
  - [Compléter et valider votre avoir](#h_01JQ9FMJWCEA7A3SX2X1R7NF2P)
- [Créer un avoir sans passer par une facture](#h_01JQ9FMJWCF77DKSEN0DRW9W89)

# Les différentes façons de créer un avoir

Plusieurs méthodes de création d’avoir existent en fonction des besoins :

- **Créer un avoir depuis une facture** : la facture existe et vous souhaitez créer un avoir en lien avec celle-ci.
- **Créer un avoir sans passer par une facture** : la facture n'est pas existante et il faut créer un avoir directement.
🧑‍🏫Exemple : **Cas d’usage pour un avoir client.** La facture d’origine n’existe pas encore dans OpenFire, ce qui peut notamment arriver dans le cadre d’un démarrage en cours d’activité dans OpenFire.🧑‍🏫Exemple : **Cas d’usage pour un avoir fournisseur.** Vous avez une note de crédit en attente d'affectation.
# Créer un avoir depuis une facture
💡Note : Il est recommandé de dé-lettrer les paiements des factures avant de générer un avoir, sauf cas d’un avoir partiel simple qui donnera lieu, le cas échéant, à un remboursement.
![](https://support.openfire.fr/hc/article_attachments/19224029677596)

Pour créer un avoir depuis une facture, rendez-vous sur celle-ci et cliquez sur le bouton **Avoir** en haut.

![](https://support.openfire.fr/hc/article_attachments/19224074886428)
🚨Avertissement : Lors de l'utilisation du bouton de création d'avoir, OpenFire considère automatiquement qu'il s'agit d'un avoir. Par conséquent, il ne faut jamais enregistrer un avoir avec un montant négatif.
Une fenêtre apparaît pour vous permettre de déterminer les paramètres de l’avoir à générer.

![](https://support.openfire.fr/hc/article_attachments/19224029679900)

Trois types d’avoir existent dans votre solution. Il vous faut donc choisir entre :

- L’avoir partiel ;
- L’avoir intégral ;
- L’avoir de modification d’une facture existante.

## Créer un avoir partiel

Ce type d’avoir est utilisé lorsque vous souhaitez rembourser ou annuler une partie seulement de la prestation facturée.

C’est notamment le cas lorsqu’un client retourne une partie des produits facturés, ou que vous accordez une réduction sur une partie de la prestation.

Il est souvent basé sur des lignes spécifiques de la facture d'origine, mais peut aussi porter sur un produit “geste commercial” dédié, que l’utilisateur peut ajouter manuellement une fois l’avoir créé, et après avoir supprimé l’ensemble des autres lignes.

L’avoir partiel créé un avoir en brouillon que vous pourrez modifier
🚨Avertissement : Cette méthode ne permet pas de facturer à nouveau le bon de commande.🚨Avertissement : Lorsque l’on utilise le bouton de création d’avoir, la base OpenFire comprend nativement qu’il s’agit d’un avoir. Il ne faut donc jamais saisir d’avoirs d’un montant négatif.
🧑‍🏫Exemple : Pour un geste commercial. 

Vous avez une facture avec un poêle, un kit fumisterie et un forfait de pose. Le poêle est légèrement rayé et vous faites une réduction de 50€ sur le prix de celui-ci.

- Créez un avoir partiel ;
- Supprimez les lignes de produit;
- Ajoutez un produit “Geste commercial” du montant HT de la remise ;
- Validez l’avoir.

Vous devrez ensuite le lettrer à votre facture d’origine.
![](https://support.openfire.fr/hc/article_attachments/19224029682716)

🧑‍🏫Exemple : Pour l’annulation définitive de tout ou une partie des prestations facturées.

Vous avez une facture avec des pièces que vous n’avez finalement pas posées et vous devez faire un avoir sur ces produits.

- Créez un avoir partiel ;

- Supprimez les lignes de produits à l’exception de celles qui n’ont pas été posées ;
- Validez l’avoir.

Vous devrez ensuite le lettrer à votre facture d’origine (voir capture d’écran ci-dessus).

## Créer un avoir intégral

Ce type d’avoir est utilisé lorsque vous souhaitez annuler complètement une facture déjà émise.

C’est notamment le cas lorsqu’une erreur a été commise sur la facture initiale ou lorsque la commande initiale a été annulée.

L’avoir intégral créé un avoir du même montant que la commande d’origine. Cet avoir sera automatiquement validé et associé (= lettré) à la facture d’origine.
💡Note : Cette méthode vous permet de refacturer votre bon de commande en lien avec la facture.

🧑‍🏫Exemple : Vous avez facturé le bon de commande trop tôt :

- - Après avoir délettré vos paiements de la facture, cliquez sur le bouton Avoir en haut de la facture.
  - Créez un avoir intégral.
  - L'avoir ainsi généré est automatiquement confirmé et lettré avec la facture.
  - La commande d’origine redevient facturable.

-

## Créer un avoir de modification de la facture

Ce type d'avoir est utilisé pour rectifier une facture en générant un avoir sur la totalité de celle-ci, puis en émettant une nouvelle facture correcte.

C’est notamment le cas lorsqu’une erreur a été faite sur le montant total ou sur la TVA ; une nouvelle facture corrigée doit alors être émise après l'annulation de la précédente.
🚨Avertissement : Cette méthode ne permet pas de facturer à nouveau le bon de commande.
## Compléter et valider votre avoir

Une fois le type d’avoir sélectionné, il vous reste à valider les informations suivantes :

**Motif** : indiquez ici le motif de l'avoir. Celui-ci apparaîtra sur l'impression PDF de l'avoir mais pourra être modifié ultérieurement ;

**Choix de la date** : deux choix sont proposés :

- **Spécifique **: choisissez une date comptable spécifique ;
- **Date de la pièce comptable** : cette option reprend la date de facturation de la facture d’origine.

**Date d'avoir** : date de l'avoir. Apparaît uniquement si vous avez coché "date spécifique" au champ précédent ;
🚨Avertissement : Vous ne pourrez pas valider un avoir avec une date antérieure à la dernière facture ou avoir validé.
**Utiliser un journal spécifique** : vous pouvez choisir le journal sur lequel l'avoir sera enregistré. Par défaut, le journal de la facture d’origine est repris.
💡Note : Les séquences de documents (factures, avoirs, bons de commande…) font l’objet d’un échange avec votre chef de projet et sont configurées par celui-ci lors de votre lancement.
# Créer un avoir sans passer par une facture

Vous pouvez créer un avoir sans passer par une facture. Pour cela :

- **Pour le plan Basique** : 
  - Tableau de bord Mes avoirs
  - `Ventes > Mes avoirs` ;
- **Pour les autres plans** : 
  - `Facturation > Clients (ou Fournisseurs pour un avoir fournisseur) > Avoir (ou Remboursement dans le cas d'un avoir fournisseur` ;
  - ou `Facturation > Tableau de bord > Créer un nouvel avoir`.

![](https://support.openfire.fr/hc/article_attachments/19224074891548)

Cliquer sur le bouton **Nouveau** en haut à gauche.

- À l'image d'une facture, remplir les différents champs tels que le client / fournisseur concerné par l'avoir, le ou les produits portant l'avoir et son / leur montant, etc.
- Confirmer ensuite l'avoir.
🚨Avertissement : Le montant d’un avoir doit toujours être positif.

Mis a jour le : 30/12/2025
