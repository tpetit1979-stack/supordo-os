---
source: https://support.axonaut.com/gerez-vos-factures/gestion-des-factures/comment-utiliser-la-tva-sur-marge-dans-axonaut/
categorie: 03. Gérez vos factures
titre: Comment utiliser la TVA sur marge dans Axonaut ?
date_recuperation: 2026-09-05
---

# Comment utiliser la TVA sur marge dans Axonaut ?

Vous vendez des biens concernés par le régime de la **TVA sur marge** et vous souhaitez savoir comment le gérer dans Axonaut ?

Dans ce tutoriel, nous allons voir comment paramétrer un produit, choisir entre TVA classique et TVA sur marge au moment de la facturation, puis comprendre comment Axonaut calcule et affiche la TVA sur la facture.

## Qu’est-ce que la TVA sur marge ?

Avec une TVA classique, la TVA est calculée sur le prix de vente selon le taux appliqué.

Avec la TVA sur marge, elle est calculé uniquement sur la différence entre le prix de vente TTC et le prix d’achat TTC. En clair, seule la marge réalisée est soumise à la TVA.

## Comment paramétrer la TVA sur marge ?

![](https://support.axonaut.com/wp-content/uploads/2026/08/image-49.png)

👉 Rendez-vous dans Devis & Factures > Produits et Services

En modifiant une fiche produit, vous pouvez préciser que le produit est susceptible d’être soumis à la TVA sur marge.

Cela permet ensuite à Axonaut de vous proposer ce mode de calcul lorsque vous utilisez le produit dans un devis ou une facture.

⚠️Cette configuration n’impose toutefois pas définitivement la TVA sur marge au produit.

## La TVA classique et la TVA sur marge dans une facture

![](https://support.axonaut.com/wp-content/uploads/2026/08/unnamed.png)

Lorsque vous ajoutez le produit dans un devis ou une facture, Axonaut vous permet de choisir le mode de TVA à appliquer : TVA classique ou TVA sur marge.

Une même facture peut donc tout à fait comporter des produits soumis à la TVA classique et des produits soumis à la TVA sur marge. Axonaut applique le bon mode de calcul ligne par ligne.

Le choix n’est pas non plus figé pour un produit. Par exemple, un même produit peut être ajouté avec une TVA sur marge sur une première facture puis avec une TVA classique sur une autre facture.

## Renseigner les informations nécessaires à la TVA sur marge

![](https://support.axonaut.com/wp-content/uploads/2026/08/unnamed-1.png)

Lorsque vous choisissez **TVA sur marge** pour une ligne, Axonaut vous demande de renseigner :

- Le prix d’achat TTC.
- Le prix de vente TTC.
- La quantité.
- Le taux de TVA sur marge applicable.

Axonaut calcule ensuite la TVA uniquement sur la différence entre le prix de vente TTC et le prix d’achat TTC.

## Pourquoi la colonne TVA reste-t-elle vide sur la facture ?

![](https://support.axonaut.com/wp-content/uploads/2026/08/unnamed-1-1.png)

L’affichage de la TVA sur marge répond à une particularité importante. Sur le PDF de la facture, les informations permettant au client de reconstituer la marge ne doivent pas être détaillées.

C’est pourquoi, pour une ligne soumise à la TVA sur marge :

- La colonne TVA n’indique pas le montant ou le taux de TVA.
- Le détail HT et TVA de la ligne n’est pas affiché de la même manière qu’avec une TVA classique.

## Comment les totaux apparaissent-ils en bas de la facture ?

![](https://support.axonaut.com/wp-content/uploads/2026/08/unnamed-2-1.png)

Axonaut distingue les lignes avec TVA classique des lignes avec TVA sur marge dans le récapitulatif de la facture.

Les lignes avec TVA classique contribuent aux totaux HT, TVA et TTC. Pour les lignes avec TVA sur marge, c’est différent. Le détail permettant de reconstituer la marge n’est pas affiché.

Cependant, leur montant est bien pris en compte dans le total de la facture. Il est repris dans une ligne dédiée : « Total régime particulier (TTC) ».

L’ensemble des lignes, qu’elles soient avec TVA classique ou TVA sur marge, contribue bien au **total TTC global** de la facture.

## Quelle mention est ajoutée sur la facture ?

![](https://support.axonaut.com/wp-content/uploads/2026/08/unnamed-3.png)

Lorsqu’une facture comporte des produits avec TVA sur marge, une mention spécifique est également ajoutée :

« Régime particulier – Agences de voyages ou Biens d’occasions – Art. 242 nonies A, annexe II CGI »

Cette mention permet d’identifier l’utilisation du régime particulier directement sur la facture.

Si vous avez des questions, n’hésitez pas à les poser via la bulle bleue en bas de votre écran !

Mis a jour le : 19 août 2026
