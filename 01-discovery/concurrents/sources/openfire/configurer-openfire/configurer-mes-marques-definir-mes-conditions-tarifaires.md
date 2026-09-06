---
source: https://support.openfire.fr/hc/fr/articles/17578765907484-Configurer-mes-marques-d%C3%A9finir-mes-conditions-tarifaires
categorie: Configurer OpenFire
titre: Configurer mes marques: définir mes conditions tarifaires
date_recuperation: 2026-09-05
---

# Configurer mes marques: définir mes conditions tarifaires

Vos fiches produits contiennent une section "Informations Fournisseur" et une section "Informations Distributeur". Selon vos politiques commerciales, vous pouvez être amenés à configurer une remise, un coût et/ou un prix de vente spécifique pour chaque produit ou chaque catégorie de produits.

Cet article vous explique comment renseigner la partie Configuration de votre marque.

Cet article contient les sections suivantes:

- [Prérequis: Comprendre les prix indiqués sur une fiche produit](#h_01JN1AC64JWG4M4Z726XFETFY4)
- [Configurer les paramètres par défaut de la marque](#h_01M11A8YRP98XH38YHA2K6YY42)
- [Configurer votre remise](#h_01M11A8YRP98XH38YHA2K6YY42)
  - [Remise - Le fabricant communique un prix unique (public ou d'achat) et vous paramétrez votre remise](#h_01JN1AEPTCKDKA5RDCD7JS9Y7J)
  - [Remise - Le fabricant communique un prix public conseillé HT et un prix d'achat](#h_01JN1AE4BNGVY9AEFXCAZFST5R)
- [Comprendre la différence entre coût et coût théorique](#h_01JN1ACDH871HT7CE18JKHQRSY)
- [Utiliser les structures de prix](#01JNP53XSWWPVVA6HD879ZHN5D)
- [Votre politique tarifaire dépend des familles de produits](#h_01JN1ACGWRE9WYJZFRK33A7AY9)
- [Votre politique tarifaire est spécifique à certains articles](#h_01JN1ACNBK8EQTBPZYNZYT0KNG)
- [Définir des catégories internes personnalisées pour les produits centralisés](#01K6G497XMJFCK698NF6PXTD60)

## Prérequis: Comprendre les prix indiqués sur une fiche produit

---

Chemin d'accès: `Ventes > Produits > [Produit]`

![](https://support.openfire.fr/hc/article_attachments/29876884663452)

- **Rubrique Informations Fournisseur:**
  Cette rubrique renseigne:
  - **le Prix d'achat:** auquel vous achetez le produit à votre fournisseur.
  - **le Prix public HT** conseillé par le fournisseur.
  - **la Remise** est la remise revendeur qui vous est accordée par votre fournisseur. Votre **prix d'achat** est calculé par l'application de la **remise** sur le **prix public HT conseillé**
- **Rubrique Informations Distributeur**
  - **le Prix de vente** est le prix auquel vous allez vendre votre produit dans vos devis. Il peut être égal au prix public HT conseillé par votre fournisseur, ou différent selon votre politique de vente.
  - le **Coût **correspond à ce que vous coûte ce produit. Il peut être égal au prix d'achat de la rubrique **Informations Fournisseur** ou différent si vous y appliquez des surcoûts comme des frais logisitiques.

## Configurer les paramètres par défaut de la marque

---

**Chemin d'accès: **`Ventes > Configuration > Marques > [MARQUE]`

Les **paramètres d'import par défaut** sont appliqués à tous les articles de la marque.

Vous pourrez alors modifier les champs suivants :

![configuration_marque.png](https://support.openfire.fr/hc/article_attachments/18707352423836)

- **Catégorie**  : catégorie affectée par défaut aux articles de cette marque
- **Remise** : taux de remise appliqué sur l’ensemble des produits de la marque à partir du Prix Public HT fabricant (ppht).
- **Prix de vente HT** : c’est le prix HT auquel vous souhaitez revendre et qui sera calculé à partir du ppht.
- **Coût**  : c’est le coût d’achat qui sera calculé à partir du prix d’achat fabricant (pa) et qui englobe souvent les frais de transport.

💡L'onglet Aide vous donne des exemples de formules pour configurer vos conditions tarifaires.

Note : Dès que vous modifiez les paramètres de la marque, vous devez cliquer sur Appliquer les règles après les modifications afin que les conditions de vente et d’achat soit appliquées sur les articles enregistrés dans votre base client.

## Configurer votre remise

---

### Le fabricant communique un prix unique (public ou d'achat) et vous paramétrez votre remise

Le champ **Remise** permet de calculer le prix complémentaire au prix communiqué par le fabricant.

- Si le fabricant ne fournit qu'**un prix public conseillé HT**, je renseigne une remise** **qui me permettra de calculer mon prix d'achat.
- Si le fabricant ne fournit qu'un **prix net d'achat**, alors mon produit aura la casé "Basé sur prix net" cochée, et je renseigne une remise pour me permettre de calculer un prix public HT indicatif.

💡L'onglet Aide vous donne des exemples de formules pour configurer vos remises

*Exemple 1 : Vous avez une remise globale de 30.5% sur tous vos articles. Dans Remise, renseignez "30.5" (Attention, les décimales sont séparées par des points).*

*Exemple 2 : Vous avez deux remises, une de 30.5% et une autre de 5%. Dans Remise, renseignez "cumul(30.5,5)" pour prendre en compte les deux remises dans votre prix d'achat*

### Le fabricant communique un prix public conseillé HT et un prix d'achat: pas de remise

Les prix public conseillé et les prix d'achat sont directement renseignés par le fabricant. Le champ Remise de cette marque doit être **laissé vide**.

Note: Si vous mettez une Remise à 0 à la place d'un champ vide, on va venir appliquer une remise de 0% et le prix d'achat sera égal au prix public conseillé.

### Comprendre la différence entre Coût et Coût théorique

---

Le prix de revient sera renseigné dans le champ **Coût** du produit si vous êtes en méthode de coût "coût standard", dans le champ **Coût théorique** si vous êtes en "coût moyen" ou "FIFO".

Chemin d'accès: `Ventes > Configuration > Catégories de produits`.

![configuration_methode_cout.png](https://support.openfire.fr/hc/article_attachments/18707352426012)

  **📓**Pour aller plus loin →
  [Configuration des catégories d'articles pour la valorisation des stocks](https://support.openfire.fr/hc/fr/articles/24421364127772)

### Utiliser les structures de prix

---

Vous pouvez stocker dans les produits des éléments de prix (onglet Vente de la fiche produit)

- **Transport sur achat**
- **Transport sur vente**
- **Coefficient de vente**
- **Autres frais logistiques**
- **Taxes divers**
- **Frais divers**

Les codes associés à chaque élément de la structure de prix sont rappelés dans la rubrique Aide des paramètres de marque.

![structure_pricx.png](https://support.openfire.fr/hc/article_attachments/18858097479452)

Vous pouvez utiliser ces éléments de prix dans vos formules de calcul des conditions tarifaires:

![](https://support.openfire.fr/hc/article_attachments/18858097480732)

*Dans cet exemple, pour définir un **prix de vente** on multiplie le **prix public hors taxe** par le **coefficient de vente** (cf structure de prix) auquel on ajoute le **transport sur vente **(cf structure de prix).*

## Votre politique tarifaire dépend des familles de produits

---

Les  catégories d’origine correspondent aux catégories définies par le fabricant. Pour chaque catégorie d’origine transmise par le fabricant, vous pouvez :

- Y faire correspondre votre propre **catégorie interne**. Si rien n'est renseigné, le logiciel va venir appliquer la catégorie dans la rubrique "Paramètres d'import par défaut".
- Spécifier vos conditions de **remise, prix de vente HT ou coût** qui vont alors être prioritaires sur les paramètres d’import par défaut définis au niveau de la marque.  Si rien n'est renseigné, le logiciel va venir appliquer les conditions de la rubrique "Paramètres d'import par défaut".

💡Si l’actualisation du tarif ne concerne qu’une catégorie ou une sélection d’articles, vous pouvez utiliser les fonctions de Mise à jour par ligne via les boutons ci dessous, à la place du bouton Appliquer les règles plus haut.

![config_marque_par_categ.png](https://support.openfire.fr/hc/article_attachments/18707320737692)

*Dans cet exemple, une remise spécifique de 40% vient s'appliquer aux produits de la catégorie "ACCESSOIRES" (tandis que la remise générique de 30% définie plus haut s'applique à tous les autres produits).*

*Dans cet exemple, le prix de vente des produits de la catégorie "AMENAGEMENT" sont redirigés vers la catégorie interne "Produits Techniques". Leur prix de vente est défini comme le prix public hors taxe communiqué par le fabricant * 2 (tandis que le prix de vente générique défini plus haut, =ppht, s'applique à tous les autres produits). *

## Votre politique tarifaire est spécifique à certains produits

---

Vous pouvez également spécifier vos conditions tarifaires sur un article particulier. Ces conditions vont alors être prioritaires sur les paramètres d’import par défaut et sur les conditions par catégories d’articles.

![config_marque_par_produit.png](https://support.openfire.fr/hc/article_attachments/18707352431132)

*Dans cet exemple, le coût du poêle AMSTERDAM ESTAILLADE FF est défini comme le prix d'achat (pa) augmenté de 10%. Pour tous les autres articles, ce sont les conditions génériques définies plus haut qui s'appliquent, à savoir coût = prix d'achat, ou bien les conditions spécifiques à certaines catégories d'articles si vous en avez définies.*

## Définir des catégories internes personnalisées pour les produits centralisés

Par défaut, tous les produits de votre marque sont associés à la catégorie interne définie dans les paramètres d'import par défaut.

![](https://support.openfire.fr/hc/article_attachments/22683981550108)

Le fabricant peut lui-même définir des catégories de produits. Pour réutiliser les catégories de produits du fabricant, vous pouvez définir une correspondance de produits dans la section "Correspondance des catégories d'articles". Pensez à cliquer sur le bouton "Appliquer les règles" pour que votre correspondance soit prise en compte.

![](https://support.openfire.fr/hc/article_attachments/22683981553564)

*Dans cet exemple, les produits de la catégorie AMENAGEMENT dans la base centralisée auront la catégorie AMENAGEMENT dans votre base.*
*Les produits de la catégorie ACCESSOIRES dans la base centralisée auront la catégorie ACCESSOIRE dans votre base.*
*Les produits de la catégorie DIVERS dans la base centralisée n'ont pas de catégorie associée. Ils prennent donc la catégorie par défaut "Tous".*

Mis a jour le : 27/08/2026
