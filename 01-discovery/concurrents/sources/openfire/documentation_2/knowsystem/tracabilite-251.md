---
url: https://documentation.openfire.fr/knowsystem/tracabilite-251
url_finale: https://documentation.openfire.fr/knowsystem/tracabilite-251
date_collecte: 2026-09-06
destination: documentation_2
---

La traçabilité d'un article est la capacité à retracer l'historique de sa production, de son stockage, de sa distribution et de son utilisation.

Dans OpenFire, la traçabilité des articles est assurée par l'utilisation de numéros de série ou de lots, qui permettent de suivre chaque article de manière individuelle.

Ces numéros de série ou de lots sont enregistrés à chaque étape de la chaîne d'approvisionnement, ce qui permet de retracer l'historique de chaque article en cas de besoin.

Attention: L'utilisation des numéros de série peut entrainer des blocages dans certains cas. Aussi, avant de modifier les paramétrages de votre base, rapprochez-vous du support OpenFire, par mail à l'adresse support@openfire.fr afin de valider le fonctionnement attendu.

## Activation du Suivi des lots / Numéro de série

Dans OpenFire, vous pouvez gérer les numéros de série à l'aide du module de suivi de stock. Pour activer le suivi de stock, rendez-vous dans le menu Stock > Configuration > Configuration :

L'option Suivi des lots ou des numéros de série permet d'activer la gestion de ces paramètres.

Vous pouvez ensuite spécifier les sociétés pour lesquelles vous souhaitez que la gestion de la traçabilité interne et la génération automatique des numéros de série est activée.

Ensuite, vous pourrez activez la gestion des numéros de série pour les articles de votre choix, en vous rendant dans l'onglet Inventaire du produit :

## Génération du numéro de série

Le numéro de série des articles est généralement déclaré au niveau des bons de reception, lorsque l'on réceptionne la marchandise. Or, à ce stade, le produit étant emballé, il n'est pas toujours possible de connaitre le numéro de série de l'appareil.

Il est alors possible de renseigner un numéro de série temporaire. Le numéro de série exact sera connu au moment de l'installation puis renseigné à ce moment là.

Ce numéro de série temporaire peut-être renseigné lors de la commande fournisseur du poêle (commande fournisseur) dans OpenFire.

La génération de ce numéro de série est possible dès la demande de prix, via l’action Générer les n° de série : 

Ce numéro de série est composé du numéro de la commande fournisseur suivi d'un numéro unique.

Ce numéro de série généré n’est pas le numéro de série de l'appareil fourni par le fournisseur. Il pourra être modifié ensuite par le numéro de série du fabricant lors de la réception.

Les numéros de série sont ensuite accessibles depuis le smart bouton de la commande d'achat :

Lorsque vous recevez des produits avec des numéros de série, une icone apparait dans la partie Opérations. Vous pouvez enregistrer le numéro de série final via ce bouton pour chaque produit reçu :