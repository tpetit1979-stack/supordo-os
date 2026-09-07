---
url: https://documentation.openfire.fr/knowsystem/gerer-les-primes-energetiques-148
url_finale: https://documentation.openfire.fr/knowsystem/gerer-les-primes-energetiques-148
date_collecte: 2026-09-06
destination: documentation_2
---

OpenFire permet de prendre en compte les primes énergétiques et de les ajouter aux devis et aux factures.

La prime est déduite du total du devis et / ou facture et l’organisme redevable de la prime rembourse au magasin cette prime (débours).

Ces primes ne rentrent donc pas dans le calcul d’imposition de TVA, et seront donc déduites du montant TTC du document. Elles pourront alors être placées en dessous du montant du devis et / ou de la facture et non dans le corps du devis.

## Primes énergétiques

La gestion des primes énergétiques (Prime CEE et Prime Rénov) se fait via l'intégration d'articles dédiés dans le corps des devis et factures.

- Prime Rénov : prime proposée par l’administration et qui transite par des services publics tels que l’Annah.
- Prime CEE : prime proposée par des entreprises privées revendeuses de produits pétroliers. Une partie de cette prime peut être reversée au magasin poseur de produits d’énergie renouvelable.

Vous pouvez alors piloter les règles d'impression et de comptabilisation de ces articles, afin de répondre aux exigences de formalisme existantes autour de la gestion de ces primes.

L'impression de vos primes est paramétrables depuis le menu **Comptabilité > Configuration > Impression des totaux dans les factures de vente**

Vous pouvez alors créer une nouvelle ligne nommée Prime:

 *Attention:* *il ne faut jamais modifier la ligne déjà existante dans le logiciel, il faut impérativement*

*soit créer une nouvelle ligne soit dupliquer la ligne existante.*

Ajouter dans le Filtre sur catégories les catégories d'articles des primes que vous ne souhaitez pas voir apparaitre dans le corps du devis ou de la facture, mais plutôt au niveau du sous-total du devis.

Choisissez ensuite si vous voulez que le paramètre Concerne les factures et/ou Concerne les commandes clients, les primes sont alors déduites du montant TTC.

## Primes avec débours et imposables

La Prime Rénov et la Prime CEE fonctionnent toutes les deux par débours et donc ces primes sont non imposables. Le montant de la prime est déduite directement du devis et de la facture client. Pensez à bien refacturer à l’organisme redevable de la prime pour que ce dernier vous rembourse.

Dans le cas de la Prime CEE vous avez la possibilité de percevoir une partie du montant de la prime, vous déduisez alors partiellement de la facture client la prime, et la partie de la prime que vous touchez sera soumise à TVA.

Lorsque vous refacturez à l'organisme, vous n'ajoutez que l'article prime CEE non imposable (si débours). Si vous prenez une quote-part de la prime, vous ajoutez l'article Prime CEE imposable à TVA qui sera soumis à TVA à 20% par défaut.

Si les articles de prime n'existent pas, vous pouvez contacter le support technique par mail à l'adresse support@openfire.fr ou par téléphone au 02.30.96.02.65.