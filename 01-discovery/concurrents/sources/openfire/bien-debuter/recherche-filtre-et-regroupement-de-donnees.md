---
source: https://support.openfire.fr/hc/fr/articles/19075387609244-Recherche-Filtre-et-Regroupement-de-donn%C3%A9es
categorie: Bien débuter
titre: Recherche, Filtre et Regroupement de données
date_recuperation: 2026-09-05
---

# Recherche, Filtre et Regroupement de données

Cet article vous présente les outils essentiels pour **trouver, organiser et affiner l'affichage** de vos données (clients, produits, commandes, etc.) dans votre solution OpenFire. En comprenant ces fonctions, vous pourrez obtenir des résultats précis et rapides.

Cet article contient les sections suivantes :

- [Localiser les fonctions de recherche](#h_01KC0ZWXTVKSADR92D4C1VJ6MZ)
- [La barre de recherche (recherche rapide)](#h_01KC0ZWWGCPQ7WZGCJJ4K8G8AZ)

  - [Recherche par champs](#h_01KC0ZZYZ6WWSA2FHXZ2QYZNHQ)
  - [Recherche avancée (Opérateur OU et ET)](#h_01KC0ZWSDD9A9BYNJ4N2H2N7FM)
  - [Utilisation de caractères spéciaux](#h_01KBZ1AXYZJ30EMJAT2MRPWEE1)
- [Les filtres (recherche par conditions)](#h_01KBZ1F01H5C2TAMQ9RF4W92RX)

  - [Les filtres prédéfinis](#h_01KBZ1AXZ6PQTV0CABYW9ZPZCB)
  - [Les filtres personnalisés](#h_01KBZ1AXZC1KC3YMS3XGWXEX15)
- [Grouper les résultats (Regrouper par)](#h_01KBZ1AXZH6X426DQTJKDC3X7J)
- [Les favoris](#h_01KBZ1AXZK42RDC9NNYS1YESVR)
- [Quand utiliser quoi ?](#h_01KBZ1AXZKPDX8SVTRT83ZM96Z)

# Localiser les fonctions de recherche

Les fonctions de recherche (**Recherche**, **Filtres**, **Regrouper par**, **Favoris**) sont disponibles sur l'ensemble des écrans de votre solution OpenFire et se situent toujours **en haut à droite** de la page.

![](https://support.openfire.fr/hc/article_attachments/24107173782044)

La loupe présente au bout de la barre de recherche vous permet d'afficher ou de masquer les boutons **Filtres**, **Regrouper par** et **Favoris.**

# La barre de recherche (recherche rapide)

La barre de **Recherche** vous permet de trouver rapidement des enregistrements en saisissant un ou plusieurs mots-clés.

## Recherche par champs

La barre de recherche fonctionne par proposition d'une liste de champs de recherche, adaptée à chaque menu du logiciel. Il vous suffit donc de saisir la valeur de votre recherche et d'indiquer le champ correspondant.

| Exemple : recherche des contacts ![](https://support.openfire.fr/hc/article_attachments/24107483123484)OpenFire renverra l'ensemble de vos contacts comportants **DUPONT** dans le nom | Exemple : recherche depuis les bons de commande ![](https://support.openfire.fr/hc/article_attachments/24107198979996)OpenFire renverra l'ensemble des commandes dont le client comportent **DUPONT** dans le nom. |
| --- | --- |

Vous pouvez également réaliser une recherche en appliquant **plusieurs critères sur plusieurs champs de référence**.

| **🧑‍🏫Exemple** : Pour rechercher un client dont le nom contient "VIO", habitant à "Guichen", et dont le commercial est "Bob", vous saisirez les critères dans la barre de recherche. ![](https://support.openfire.fr/hc/article_attachments/24107521557404) |
| --- |

## Recherche avancée (Opérateur OU et ET)

Vous pouvez utiliser des opérateurs pour des recherches plus précises.

- **Opérateur OU** : C'est l'opérateur par défaut, ajouté automatiquement lors d'une recherche multiple sur un même champ. Les résultats sont additionnés.

| **🧑‍🏫Exemple** : si vous rechercher, dans le champ **Produits **depuis la barre de recherche du menu des produits, les mots ***Entretien***** **et ***Ramo*** , vous obtenez tous les produits dont le nom ou la référence contiennent "Ramonage" **OU** "Entretien". ![](https://support.openfire.fr/hc/article_attachments/24107521558300)Dans la pratique, pour réaliser une telle recherche :   Positionnez vous dans la barre de recherche  Recherchez la valeur **Entretien** dans le champ *Produit*, puis faites ENTREE Recherchez la valeur **Ramo **dans le champ *Produit*, puis faites ENTREE |
| --- |

- **Opérateur ET** : Il vous permet de réaliser une recherche par entonnoir en multipliant les valeurs de recherche sur un même champ.

  - **Activer l'opérateur ET :** Maintenez les touches **MAJ + Entrée** lors de la saisie du deuxième critère de recherche.
     ![](https://support.openfire.fr/hc/article_attachments/24122081459100)

| **🧑‍🏫Exemple** : Vous recherchez tous les conduits de marque "Poujoulat" **ET** de diamètre "130". ![](https://support.openfire.fr/hc/article_attachments/24122090261660)Dans la pratique, pour réaliser une telle recherche :   Positionnez vous dans la barre de recherche  Recherchez la valeur **Pou** dans le champ *Produit*, puis faites ENTREE Recherchez la valeur **130** dans le champ *Produit* puis faites MAJ + ENTREE simultanément |
| --- |

## Utilisation de caractères spéciaux

Si vous avez un doute sur l'accentuation ou l'orthographe du terme, utilisez les caractères spéciaux suivants:

- **Caractère **`**_**`** (touche 8 du clavier)** : Permet de remplacer **un seul caractère** du mot recherché.

| **🧑‍🏫Exemple** : `J_tul` recherchera Jotul ou Jøtul. |
| --- |

- **Caractère **`**%**` : Permet de remplacer **plusieurs caractères** dans le mot.

| **🧑‍🏫Exemple** : `Lef%re` va rechercher l'ensemble des contacts dont le nom commence par "**lef"** et se termine par **"re"**, indépendamment du nombre et du type de caractères au milieu. Les résultats possibles seront donc par exemple : `Le`fèbv`re`, `Le`fev`re`, `Le`ffèv`re`... |
| --- |

| 💡**Note **: La recherche textuelle :  Ne tient pas compte des majuscules et minuscules. Prend en compte les caractères accentués. Les critères de recherche peuvent être saisis **partiellement**. |
| --- |

# Les filtres (recherche par conditions)

Les fonctions de **Filtres** sont un complément à la barre de recherche. Elles sont destinées à **restreindre dynamiquement** l'affichage de vos données selon des critères spécifiques.

#### Les filtres prédéfinis

Les filtres prédéfinis sont directement accessibles depuis le menu déroulant **Filtres**, situé sous la barre de recherche. Ils changent selon le menu sélectionné (Contacts, Produits, Devis, etc.) pour ne proposer que les plus couramment utilisés.

Comprendre les opérateurs lors de l'application de plusieurs filtres par défaut :

- **Opérateur ET (conditions supplémentaires)** : Les filtres prédéfinis de **rubriques différentes** (séparées par un trait) ajoutent une condition supplémentaire.

| **🧑‍🏫Exemple** : Ajouter les filtres "**Commandes**" (rubrique 1) et "**Entièrement facturable**" (rubrique 2) affiche uniquement les commandes qui sont en état entièrement facturable (Commandes **ET** Entièrement facturable). ![](https://support.openfire.fr/hc/article_attachments/24122564710556) |
| --- |

- **Opérateur OU (cumul de résultats)** : Les filtres prédéfinis d'une **même rubrique** (non séparées par un trait) s'utilisent de façon alternative ("OU", et cumulent donc leurs résultats.

| **🧑‍🏫Exemple** : Ajouter les filtres "**Devis**" et "**Commandes**", qui se trouvent dans une rubrique commune, additionne leurs résultats (Devis **OU** Commandes). ![](https://support.openfire.fr/hc/article_attachments/24122564712988) |
| --- |

#### Les filtres personnalisés

Pour créer un filtre avec des conditions très spécifiques, vous pouvez ajouter un filtre personnalisé.

1. Cliquer sur **Filtres** puis sur **Ajouter un filtre personnalisé**.
2. Dans la fenêtre qui s'ouvre :

  1. Choisir le **champ disponible** dans le premier menu déroulant.
  2. Choisir l'**opérateur disponible** dans le second menu déroulant.
  3. Définir la ou les **valeurs spécifiques** attendues dans le ou les champs suivants.
3. Pour appliquer le filtre comme une condition supplémentaire (**Opérateur ET**), cliquer sur **APPLIQUER** et appliquer un autre filtre.
4. Pour cumuler le résultat avec un autre filtre personnalisé (**Opérateur OU**), cliquer sur **AJOUTER UNE CONDITION**.

![](https://support.openfire.fr/hc/article_attachments/24122564713628)

# Grouper les résultats (Regrouper par)

L'outil **Regrouper par** est situé à droite des filtres. Il permet de regrouper les enregistrements selon un champ spécifique pour une meilleure visibilité des données.

- **En vue Liste** : Vous pouvez appliquer autant de groupements que vous le souhaitez. La présentation se fera sous forme de hiérarchie, du premier groupement sélectionné au dernier.

![](https://support.openfire.fr/hc/article_attachments/24122572896284)

- **En vue Kanban** : Vous ne pouvez appliquer qu'un seul niveau de regroupement.

![](https://support.openfire.fr/hc/article_attachments/24122572896924)

Si le groupement souhaité n'est pas disponible par défaut, vous pouvez cliquer sur **Ajouter un groupe personnalisé** et déterminer le champ de groupement à appliquer.

# Les favoris

L'outil **Favoris** vous permet de **sauvegarder** vos divers filtres de recherche que vous utilisez de manière récurrente.

# Quand utiliser quoi ? (Récapitulatif)

| Votre objectif | Outil à utiliser |
| --- | --- |
| Rechercher une **référence spécifique** ou un **mot-clé**. | La **barre de recherche**. |
| Filtrer selon **plusieurs conditions précises**. | Les **filtres** (prédéfinis ou personnalisés). |
| Sauvegarder des recherches récurrentes. | Les **favoris**. |

 

📓Pour aller plus loin → Les favoris

Mis a jour le : 09/12/2025
