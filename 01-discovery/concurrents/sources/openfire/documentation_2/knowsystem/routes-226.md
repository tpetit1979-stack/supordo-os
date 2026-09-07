---
url: https://documentation.openfire.fr/knowsystem/routes-226
url_finale: https://documentation.openfire.fr/knowsystem/routes-226
date_collecte: 2026-09-06
destination: documentation_2
---

Les routes correspondent à l'itinéraire que vont prendre vos articles dans votre entreprise. Elles sont importantes pour le bon processus de la gestion des stocks puisqu'elles permettent de guider vos articles vers le bon emplacement, et permettent de définir des emplacements par défaut.

Attention: avant de modifier les paramétrages de votre base, rapprochez-vous du support OpenFire, par mail à l'adresse support@openfire.fr, ou par téléphone au 02.30.96.02.65, afin de valider le fonctionnement attendu.

## Généralités

Les routes sont des itinéraires prédéfinis que les articles vont emprunter pour passer d'un emplacement à un autre. Elles peuvent être utilisées pour contrôler la façon dont les produits sont traités lors de leur déplacement entre les différents emplacements.

Les routes peuvent être définies en fonction de la nature des produits, de leur emplacement ou des opérations qui doivent être effectuées sur les produits avant qu'ils n'atteignent leur destination.

Par exemple, depuis un entrepôt, vous pouvez accéder aux routes proposées:

Par défaut ,un certain nombre de Routes existent: notamment la route d'Achat et de réception.

Ces routes font appel à des règles d'approvisionnement. Ces règles déterminent les actions à entreprendre lorsqu'un produit est en rupture de stock ou en surstock dans un emplacement donné.

   Plus d'informations sur [les règles d'approvisionnement](https://documentation.openfire.fr/knowsystem/regles-de-stock-249)

Par exemple, la route Achat appelle une règle d'approvisionnement nommée *Nom_de_votre_entrepôt : Buy*. 

Par défaut, cette règle génère une demande de prix quand des bons de commande client passent à l'état confirmé:

La partie Règles de flux poussés permet de définir que la réception d'un produit dans un emplacement de l'entrepôt déclenche son transfert vers un autre emplacement. Les règles de flux poussés se déclenchent donc lorsque les articles entrent dans un emplacement spécifique.

 

## Activation du routage par article

Pour utiliser les routes, activez l'option Routage avancé des articles défini par des règles dans la configuration de l'inventaire:

Cette option permet notamment d'ajouter le choix des routes dans l'onglet inventaire des fiches articles:

Cela vous permet donc de sélectionner par article, ou par catégorie d'articles, les règles d'approvisionnements à appliquer.

La création des ordres d'achat, selon la route définie, sera déclenchée par le planificateur. Celui-ci tourne automatiquement une fois par jour, et peut être lancé manuellement dans l'onglet "Opérations" du module inventaire :


## Routes spécifiques par ligne de commande

Dans le menu **Ventes > Configuration**, il est possible d'activer l’option Choisir des routes spécifiques à chaque ligne de commande :

Cette option permet de définir une étape supplémentaire qui aboutit à la création d'un bon de commande selon les lignes de commandes (exemple: une route pour fumisterie et une route pour les poêles).

Cette option ajoute le champ Route en haut des devis, et si deux articles ont des routes différentes, alors deux bons de livraison seront générés.

Cela peut être utile si vous vendez des produits fabriqués en interne. La ligne de vente peut être définie dans les paramètres de la route de production pour un produit particulier et peut inclure des informations telles que le client cible, le prix de vente, etc...

Cela permet de centraliser les informations liées à la vente du produit dans le processus de production, ce qui peut faciliter la planification et la gestion des stocks.