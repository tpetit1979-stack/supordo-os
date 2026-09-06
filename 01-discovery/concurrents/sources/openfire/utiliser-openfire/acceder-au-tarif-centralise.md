---
source: https://support.openfire.fr/hc/fr/articles/21464464612124-Acc%C3%A9der-au-Tarif-Centralis%C3%A9
categorie: Utiliser OpenFire
titre: Accéder au Tarif Centralisé
date_recuperation: 2026-09-05
---

# Accéder au Tarif Centralisé

Le **Tarif Centralisé** désigne l'accès aux catalogues produits de toutes les marques avec lesquelles vous travaillez. Ces catalogues produits sont régulièrement actualisés en relation directe avec les fabricants.

Cette fonctionnalité vous permet d'importer et d'utiliser directement dans vos devis des produits sans avoir à créer manuellement vos produits et à saisir des informations telles que les tarifs ou les données techniques associées. Cet article se concentre sur **l'accès au Tarif Centralisé **et sur la **mise à jour des tarifs.**

**Cet article contient les sections suivantes:**

- [Demander l'accès à un catalogue de tarifs](#h_01K1EGSNK9RVA82J0DC0QMZ1JY)
- [Obtenir la dernière mise à jour des données du Tarif Centralisé](#h_01K1G6QXSHY9TJE3CKBK6DSV2G)
- [Questions particulières](#h_01KQ00VFHAKYXW8KW6C6J0HHB9)
  - [Comprendre les dates du tarif indiquées sur la marque](#h_01KQ00VFHAKYXW8KW6C6J0HHB9)
  - [Le tarif d'un produit ne correspond pas à mon catalogue](#h_01KRGMYDWH5SEC4PVMCA5A287C)
    [ ](#h_01K1G6QXSHY9TJE3CKBK6DSV2G)

# Demander l'accès à un catalogue de tarifs

---

  💡Note : Il est nécessaire d'être connecté avec un utilisateur disposant des
  droits "Gestion de contrat OpenFire" pour effectuer cette demande. Pour toute demande d'ajout des droits, contactez le support OpenFire.

Pour accéder à la liste des catalogues du Tarif Centraliser, suivre le chemin d'accès suivant:

- Vente > Configuration > Connexions TC

![catalogue tc.png](https://support.openfire.fr/hc/article_attachments/21464452183580)

L'accès aux marques identifiées comme **Partenaires **est possible gratuitement, après validation du fournisseur.
Les marques identifiées comme Non Partenaires sont accessibles sur abonnement (voir [https://openfire.fr/tarif-centralise](https://openfire.fr/tarif-centralise)).

![](https://support.openfire.fr/hc/article_attachments/21464464599196)

**Marque associée : **Ce champ est à compléter avec la marque de votre base locale dans laquelle les produits issus du catalogue viendront s'importer.

**Connexion: **Ce bouton permet d'effectuer une demande de connexion au catalogue.

  💡Note : La demande de connexion peut nécessiter une validation de nos fabricants
  partenaires. Dans ce cas, elle ne sera pas effective immédiatement.

Lorsque la connexion a été validée, la marque s'affiche comme connectée.

![](https://support.openfire.fr/hc/article_attachments/21464452190364)

Vous pouvez alors paramétrer vos conditions tarifaires liées à la marque.

  **📓**Pour aller plus loin →
  [Définir ses conditions tarifaires](https://support.openfire.fr/hc/fr/articles/17578765907484)

# Obtenir la dernière mise à jour des données du Tarif Centralisé

---

Lorsque les fabricants effectuent une mise à jour de leur catalogue, un mail est envoyé aux utilisateurs connectés.

Vous avez alors une **action manuelle** à faire pour que les tarifs des produits déjà présents sur votre base se mettent à jour.

Via cette action, le logiciel **n’importe pas de produits**, mais il mettra à jour les produits connectés présents dans votre base.

Chemin d'accès:

- Vente > Configuration > Marques

**Mettre à jour les produits: **Ce bouton vous permet d'actualiser les données des produits connectés dans votre base.

![](https://support.openfire.fr/hc/article_attachments/21464452190748)

  🚨Avertissement : La mise à jour simultanée de plus de 1500 articles peut provoquer des lenteurs sur votre base. Lorsque vous avez une opération de cette ampleur à effectuer, nous vous invitons à contacter le support OpenFire.

Vous avez la possibilité de ne pas mettre à jour certaines données parce que vous y avez apporté une modification. Pour cela, cochez les éléments que vous souhaitez conserver en l'état.

![](https://support.openfire.fr/hc/article_attachments/21464452191132)

# Questions particulières

---

## À quoi correspondent les dates du tarif indiquées sur la marque ?

![](https://support.openfire.fr/hc/article_attachments/27020171514396)

La date du tarif (1) correspond à la date du produit le plus récent parmi les articles de cette marque dans votre base. Il est possible qu'il y ait des articles dans le catalogue centralisé, que vous n'avez pas importés, qui soient à une date ultérieure.

La date de mise à jour dans la partie "Notes sur les produits centralisés" (2) correspond à la date du produit le plus récent dans le catalogue centralisé de la marque.

## Le tarif d'un produit ne correspond pas à mon catalogue

Si vous constatez des écarts de tarifs, voilà les éléments à vérifier:

1. Le produit est-il indiqué comme "Connecté" ?
  Si non, recherchez la référence dans le Tarif Centralisé pour obtenir le dernier tarif actualisé.
2. Le **prix public HT** est-il correct dans la partie "Informations Fournisseur" ?
  Si le prix public HT est correct mais que le prix de vente n'est pas correct, il faut corriger votre configuration de marque (voir l'article de documentation [suivant](https://support.openfire.fr/hc/fr/articles/17578765907484))
3. Le produit est **connecté **mais le **prix public HT** n'est pas correct dans la partie "Informations Fournisseur"
  Le prix est-il corrigé en mettant à jour le produit ? (voir la [section précédente](#h_01K1G6QXSHY9TJE3CKBK6DSV2G))
4. Le produit est connecté et le prix public HT reste incorrect après mise à jour
  Vous pouvez envoyer par mail à [support@openfire.fr](mailto:support@openfire.fr) la référence du produit qui pose problème ainsi qu'une photo de votre catalogue PDF indiquant le tarif auquel ce produit devrait être.

  **📓**Pour aller plus loin →
  [Utiliser les produits centralisés dans mes devis et dans mes kits](https://support.openfire.fr/hc/fr/articles/21466295044636)

Mis a jour le : 13/05/2026
