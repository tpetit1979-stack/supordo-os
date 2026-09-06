---
source: https://support.openfire.fr/hc/fr/articles/26864108607388-G%C3%A9rer-l-affichage-et-le-partage-des-Demandes-d-Intervention-DI-sur-le-portail-client
categorie: Configurer OpenFire
titre: Gérer l'affichage et le partage des Demandes d'Intervention (DI) sur le portail client
date_recuperation: 2026-09-05
---

# Gérer l'affichage et le partage des Demandes d'Intervention (DI) sur le portail client

Cet article vous explique comment configurer la visibilité de vos demandes d'intervention (DI) sur le portail client, ainsi que la gestion du partage de leurs descriptions pour une communication transparente avec vos clients.

Cet article contient les sections suivantes :

- [**Configuration de la visibilité globale (Smart Button Portail)**](#h_01KPDSKPJ479QVZ2PWYMDGWNJG)

  - [Au niveau du Modèle d'intervention](#h_01KPDSKPJ5948FKXR2B24Y2VV6)
  - [Au niveau de la Demande d'intervention (DI)](#h_01KPDSKPJAGX004Z7DBDJV2SZA)
- [**Organisation des rubriques sur le portail**](#h_01KPDSKPJEZCM2ENRRR9QKSA9N)
- [**Partage de la description des DI**](#h_01KPDSKPJJGDS1Y62YQY0AXKPR)

  - [Activation dans le modèle d'intervention](#h_01KPDSKPJJNPND1YPTQJAMK1WJ)
  - [Personnalisation sur une DI spécifique](#h_01KPDSKPJPXG497DJJ6T2D9AH5)

## Configuration de la visibilité globale

Pour que vos clients puissent retrouver leurs interventions en ligne, vous devez activer la fonctionnalité **Portail**.

### Au niveau du Modèle d'intervention

Le réglage sur le modèle définit la règle par défaut pour toutes les DI créées à partir de celui-ci.

`Suivre le chemin d'accès suivant : Configuration > Interventions > Modèles d'intervention`

- Sélectionner le modèle souhaité (ex: **RAMONAGE BOIS**).
- Activer le Smart Button **Portail** situé en haut à droite de la fiche.

  - **Activé** : Les DI utilisant ce modèle seront visibles par le client sur son espace "Mon Compte".
  - **Désactivé** : L'intervention reste confidentielle et invisible sur le web.

### Au niveau de la Demande d'intervention (DI)

Vous pouvez modifier la visibilité unitairement pour une intervention précise.

`Suivre le chemin d'accès suivant : SAV > Interventions > Demandes d'intervention`

- Ouvrir la DI concernée.
- Cliquer sur le Smart Button **Portail** pour l'activer ou le désactiver.

| 💡**Note **: Lorsqu'un modèle est sélectionné dans une DI, le champ **Portail** de la DI prend automatiquement la valeur définie dans le modèle. |
| --- |

## Organisation des rubriques sur le portail

Une fois la visibilité activée, le client retrouve ses demandes classées dans deux rubriques distinctes sur son portail:

- **SAV** : Regroupe toutes les DI dont le type est explicitement défini comme "SAV".
- **Entretien** (anciennement "Demandes d'intervention") : Regroupe les DI de type "Entretien - Maintenance".

| 🚨**Avertissement** : Les DI de type "Visite technique" ou "Installation" ne sont pas affichées dans ces rubriques spécifiques du portail afin de rester le plus clair possible pour l'utilisateur. |
| --- |

## Partage de la description des DI

Vous pouvez choisir de partager ou non le champ **Description** de vos DI avec vos clients. Cela est utile si vos descriptions contiennent des informations purement internes.

 

### Activation dans le modèle d'intervention

- Aller dans l'onglet **Portail web** du modèle d'intervention.
- Cocher ou décocher la case **Partager la description des DI sur le portail**.

  - **Cochée** : La description sera partagée par défaut pour toutes les DI de ce type.
  - **Décochée** : La description restera masquée sur le portail.

 

### Personnalisation sur une DI spécifique

Si vous avez besoin de déroger à la règle générale pour une intervention précise :

- Dans la DI, se rendre dans l'onglet **Description**.
- Modifier l'option **Partager la description dans le portail**.

| **🧑‍🏫Exemple** : Pour une DI de type SAV, si l'option est activée, le client verra le texte saisi dans le bloc "Description" directement sur son formulaire web. Si le champ est vide, le bloc ne s'affichera pas sur le portail. |
| --- |

## Bonnes pratiques

- **Vérifiez le statut** : Une DI n'est visible sur le portail que si son statut est différent de "Brouillon" ou "Annulé", et que le bouton **Portail** est bien activé.
- **Utilisez les infobulles** : En survolant les champs de configuration, des aides contextuelles vous rappellent l'impact de chaque option sur l'affichage client.

Mis a jour le : 20/04/2026
