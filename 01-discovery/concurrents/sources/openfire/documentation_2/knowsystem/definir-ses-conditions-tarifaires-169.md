---
url: https://documentation.openfire.fr/knowsystem/definir-ses-conditions-tarifaires-169
url_finale: https://documentation.openfire.fr/knowsystem/definir-ses-conditions-tarifaires-169
date_collecte: 2026-09-06
destination: documentation_2
---

Il est possible d'appliquer des conditions tarifaires différentes pour chaque catégorie ou article d'une marque.

Les paramètres sur les prix de vente et d’achat d'une marque peuvent donc être précisés :

- Sur la marque ;
- Sur les catégories d’articles ;
- Sur les articles.

## Gestion des prix par marque

Rendez-vous dans le menu **Ventes > Configuration > Marques**, puis recherchez la marque voulue.

Vous pourrez alors modifier les champs suivants :

- Catégorie : catégorie affectée par défaut aux articles si aucune catégorie n’est renseignée dans la base centralisée ou si aucune correspondance de catégorie n’est effectuée.
- Remise : taux de remise appliqué sur l’ensemble des produits de la marque à partir du Prix public HT fabricant (ppht).
- Prix de vente HT : c’est le prix de revente HT auquel vous souhaitez revendre et qui sera calculé à partir du ppht.
- Prix de revient : c’est le prix de revient (ou coût d’achat) qui sera calculé à partir du prix d’achat fabricant (pa) et qui englobe souvent les frais de transport.

 *Vous pouvez vous aider de l’onglet Aide afin de retrouver les définitions de chaque libellé et de comprendre les modalités de calcul possible.*

Cas particulier : certaines marques disposent d'un tarif centralisée sur lequel les prix public HT et les prix d'achat sont déjà renseignés. Dans ce cas, il est possible de ne pas paramétrer de remise afin d'utiliser les prix d'achat de la base centralisée. Il faut alors configurer la marque spécifiquement en positionnant dans les champs de calcul les valeurs suivantes :

  - Remise = VIDE
  - Prix de vente HT = pv
  - Prix de revient = pr

 Attention : dès lors que vous modifiez les paramètres de la marque, vous devez cliquer sur Appliquer les règles après les modifications afin que les conditions de vente et d’achat soit appliquées sur les articles enregistrés dans votre base client.

## Gestion des prix par catégories


Les catégories d’origine correspondent aux catégories définis par le fabricant. Pour chaque catégorie d’origine transmise par le fabricant, vous pouvez :

- Y faire correspondre votre propre catégorie interne ;
- Spécifier vos conditions de remise, prix de vente HT ou prix de revient qui vont alors prendre le pas sur les paramètres d’import par défaut définis au niveau de la marque.

*Si l’actualisation du tarif ne concerne qu’une catégorie ou une sélection d’articles, vous pouvez utiliser les fonctions d’actualisation par ligne via les boutons ci dessous, au lieu du bouton* *Appliquer les règles.*