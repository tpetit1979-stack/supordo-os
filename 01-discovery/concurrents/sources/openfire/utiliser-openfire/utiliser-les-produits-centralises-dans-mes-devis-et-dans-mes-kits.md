---
source: https://support.openfire.fr/hc/fr/articles/21466295044636-Utiliser-les-produits-centralis%C3%A9s-dans-mes-devis-et-dans-mes-kits
categorie: Utiliser OpenFire
titre: Utiliser les produits centralisés dans mes devis et dans mes kits
date_recuperation: 2026-09-05
---

# Utiliser les produits centralisés dans mes devis et dans mes kits

Lorsque vous êtes connectés au **Tarif Centralisé** d'une marque, vous pouvez ajouter les produits de son catalogue directement dans vos devis et vos kits.

Cet article se concentre sur **l'ajout des produits centralisés dans un devis/kit** et **l'import de produits** depuis la base centralisée.

**Prérequis: **Il est nécessaire d'être **connecté** aux marques centralisées et d'avoir au préalable **configuré** **vos conditions tarifaires **dans les marques concernées.

| 🧩**Prérequis** →   [Accéder aux Tarifs Centralisés](https://support.openfire.fr/hc/fr/articles/21464464612124) 🧩**Prérequis** →   [Définir mes conditions tarifaires sur les produits du Tarif Centralisé](https://support.openfire.fr/hc/fr/articles/17578765907484) |
| --- |

**Cet article contient les sections suivantes:**

- [Importer les produits centralisés depuis un devis/kit](#h_01K1G7HW7KDRMTM248X7YQQVZT)
  - [Utiliser un produit centralisé dans un devis](#h_01K1G87ZQQ4RTSSNWQ5217YJ5N)
  - [Utiliser un produit centralisé dans un kit](#h_01K1G7M0XKQD42TTWJNF94HSVZ)
- [Utiliser un filtre pour rechercher un produit centralisé](#h_01K1G866H93YGSKTNCEXR62STJ)
- [Importer un produit centralisé depuis la marque](#h_01K1G8RXP7DZGJG4WW83SJ6ZMZ)
- [Gérer les alertes sur les prochaines dates de tarifs](#h_01KS7XXK9KTSX9D4X44TZ0R19S)

# Importer les produits centralisés depuis un devis/kit

---

## Utiliser un produit centralisé dans un devis

Chemin d'accès:

- Vente > Commandes > Devis

Créez un nouveau devis comme à l'accoutumée. Dans les lignes de devis, saisissez le **raccourci** "**m:"** suivi des trois premières lettres de la marque pour rechercher sur la base centralisée.

Les produits affichés en rouge désignent les produits centralisés qui n'ont pas encore été importés dans votre base locale. Les produits affichés en noir désignent les produits déjà présents dans votre base locale.

Pour plus d'efficacité dans la recherche, saisissez directement la référence de l'article à la suite du raccourci m:.

![](https://support.openfire.fr/hc/article_attachments/21466295034524)

| **🧑‍🏫Exemple** : m:jot vous permet de chercher parmi les articles centralisés Jotul. |
| --- |

À la validation du devis, le produit centralisé **s'importe dans votre base locale**. Il est donc visible dans votre liste de produits, porte la coche **"Connecté"** et apparaîtra en noir lors de la prochaine recherche.
![](https://support.openfire.fr/hc/article_attachments/21466295036700)

## Utiliser un produit centralisé dans un kit

Chemin d'accès:

- Vente > Produits > Produits

Créez un nouveau produit de type kit **dans votre marque entreprise.**
Dans l'onglet "Kit", ajoutez une ligne par composant.
Utilisez le **raccourci "m:" **suivi des trois premières lettres du fabricant pour rechercher votre composant parmi les produit de la base centralisée.

Pour plus d'efficacité dans la recherche, saisissez directement la référence de l'article à la suite du raccourci m:.

![](https://support.openfire.fr/hc/article_attachments/21466295037340)

À la validation du kit, le produit centralisé **s'importe dans votre base locale**. Il est donc visible dans votre liste de produits, porte la coche "Connecté" et apparaîtra en noir lors de la prochaine recherche.
![](https://support.openfire.fr/hc/article_attachments/21466295036700)

# Utiliser un filtre pour rechercher un produit centralisé

---

Si le raccourci **m: **ne vous a pas permis de trouver le produit d'intérêt depuis une ligne de devis ou de kit, cliquez sur "**Recherche avancée" **dans le menu déroulant de la ligne de devis/kit** **et appliquez les filtres suivants:

- **Marque: **la marque centralisée d'intérêt
- **Rechercher sur la base centralisée**
- Taper votre **référence **dans la barre de recherche

De la même façon, les produits s'affichent en rouge s'ils n'ont pas encore été importés dans votre base locale, en noir s'ils sont déjà présents.

![](https://support.openfire.fr/hc/article_attachments/21466284065564)

Ce filtre est également utilisable depuis votre vue Produits.

Chemin d'accès:

- Vente > Produits > Produits

![](https://support.openfire.fr/hc/article_attachments/21466284066076)

# Importer un produit centralisé depuis la marque

---

  💡Note : L'import de produits en lots depuis la marque peut provoquer des ralentissements
  lors de la mise à jour si le volume de produits importé est conséquent. Nous déconseillons
  cet usage
  et nous vous conseillons plutôt d'importer vos articles directement dans vos
  devis et dans vos kits au fur et à mesure de vos besoins.

Chemin d'accès:

- Vente > Configuration > Marques

![](https://support.openfire.fr/hc/article_attachments/21466284066460)

**Produits centralisés: **Ce *smart button *en haut à droite de la marque vous permet d'aller consulter la liste des produits centralisés.

Ces produits apparaissent en rouge lorsqu'ils ne sont pas encore présents dans votre base locale.

![](https://support.openfire.fr/hc/article_attachments/21466284066844)

Vous pouvez sélectionner ceux qui vous intéressent et cliquer sur **Action > Importer.**

## Gérer les alertes sur les prochaines dates de tarifs

---

  💡Note : Cette fonctionnalité nécessite l'installation d'un module spécifique, et n'est éligible que pour certaines marques partenaires.

Si le fabricant a renseigné dans sa base centralisée la prochaine date de mise à jour de ses tarifs, vous pouvez choisir de recevoir un avertissement sur vos devis si le tarif des produits va être amené à évoluer prochainement.

Dans le cas où le fabricant a choisi d'utiliser cette fonctionnalité, les champs suivants seront renseignés dans la partie Informations Fournisseur de la fiche produit.

Chemin d'accès:

- Ventes > Produits > Produits

![](https://support.openfire.fr/hc/article_attachments/27644239534236)

- **Date du prochain tarif: **la date a laquelle le fabricant a prévu de faire évoluer le tarif de ce produit
- **Prochain prix public HT: **la valeur que devrait prendre le Prix public HT du produit lorsque le fabricant aura réalisé la prochaine mise à jour.
- **Prochain prix d'achat:  **la valeur que devrait prendre le Prix d'achat du produit lorsque le fabricant aura réalisé la prochaine mise à jour.

Si les valeurs sont vides, cela signifie que le fabricant n'a pas renseigné cette information.

| 🚨**Avertissement** : La mise à jour des prix n'est           pas automatique.           Il vous faudra cliquer sur "Mettre à jour mes produits" à réception           du mail indiquant que le fabricant a mis à jour ses tarifs.                       Voir l'article dédié           [Obtenir la dernière mise à jour des données du Tarif Centralisé](https://support.openfire.fr/hc/fr/articles/21464464612124-Acc%C3%A9der-au-Tarif-Centralis%C3%A9#h_01K1G6QXSHY9TJE3CKBK6DSV2G) |
| --- |

Vous pouvez renseigner dans vos paramètres le nombre de jours à partir duquel vous souhaitez recevoir un avertissement sur les devis avec des produits concernés.

Chemin d'accès:

- Paramètres > Ventes > Tarif

![](https://support.openfire.fr/hc/article_attachments/27644129407132)

Par défaut, un paramètre à 0 indique que vous ne serez pas notifié sur les devis si le tarif des produits va évoluer.

Chemin d'accès:

- Ventes > Commandes

À l'ajout du produit dans un devis, une bannière d'avertissement s'affiche si le prix est susceptible de changer dans le délai que vous avez configuré.

![](https://support.openfire.fr/hc/article_attachments/27644089656604)

Mis a jour le : 22/05/2026
