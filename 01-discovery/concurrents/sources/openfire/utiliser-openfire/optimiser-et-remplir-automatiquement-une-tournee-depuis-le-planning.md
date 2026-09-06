---
source: https://support.openfire.fr/hc/fr/articles/26960539283228-Optimiser-et-remplir-automatiquement-une-tourn%C3%A9e-depuis-le-planning
categorie: Utiliser OpenFire
titre: Optimiser et remplir automatiquement une tournée depuis le planning
date_recuperation: 2026-09-05
---

# Optimiser et remplir automatiquement une tournée depuis le planning

Cet article vous explique comment combler automatiquement les temps morts d'une tournée en planifiant les demandes d'intervention les plus proches géographiquement. Cette fonctionnalité vous permet d'optimiser le planning de vos techniciens tout en réduisant les déplacements inutiles.

Cet article contient les sections suivantes :

- [Chemin d'accès](#h_01KPT6RQA941E7SVRXVT9F9W5S)
- [Configurer les critères de recherche](#h_01KPT6RQAB857NX7TDSZW0S4WK)
- [Sélectionner le point de départ de la tournée](#h_01KPT6RQAQEX59Z22FFKS5VZE6)
- [Lancer le remplissage automatique](#h_01KPT6RQAS0GGMJBEY5QKTNE8J)

### Chemin d'accès

`Suivre le chemin d'accès suivant : Intervention > Planning > Planning vue semaine.`

Pour ouvrir l'assistant, cliquez sur l'icône **loupe** située en bas de la colonne de la journée du technicien concerné.

![](https://support.openfire.fr/hc/article_attachments/26960568591132)

| 💡**Note **: Cette fonctionnalité est exclusivement disponible en vue semaine ; la vue jour ne permet pas d'utiliser cet outil. |
| --- |

### Configurer les critères de recherche

Les critères disponibles dans l'assistant vous permettent de filtrer les demandes d'intervention (DI) qui seront proposées sur la carte :

- **États des demandes** : restreignez la recherche aux demandes ayant un statut spécifique. Par défaut, le système sélectionne les états **En retard de planification**, **À planifier rapidement** et **À planifier**.
- **Étiquettes** : filtrez les demandes sur celles ayant l'étiquette sélectionnée.
- **Secteurs** : filtrez les demandes d'intervention sur des secteurs spécifiques.
- **Modèle d'intervention** : ciblez un modèle d'intervention précis si nécessaire.
- **Rayon (km)** : définissez la distance maximale de recherche (sous forme de cercle) autour de la demande que vous choisirez comme point de départ. Cela permet de limiter les propositions à une zone géographique restreinte pour éviter des déplacements trop lointains.
- **Ignorer la durée** : cochez cette option si vous souhaitez inclure des interventions dont la durée dépasse celle des créneaux disponibles.

![](https://support.openfire.fr/hc/article_attachments/26960539279644)

| 💡**Note **: À chaque modification de critère, il est important de cliquer sur le bouton **Mettre à jour la recherche** pour actualiser les résultats affichés sur la carte. |
| --- |

#### Lancer la recherche

- Cliquer sur le bouton **Rechercher** pour afficher les demandes d'intervention éligibles.
- Consulter les résultats directement sur la carte interactive.

Les demandes sont représentées sur la carte par des couleurs selon leur état :

- **Gris -** **Brouillon** : demande à l'état initial.
- **Bleue -** **Planifié** : intervention déjà planifiée.
- **Orange -** **À planifier** : demande en attente de planification.
- **Rouge -** **En retard** : demande dont la date de planification est dépassée.

![](https://support.openfire.fr/hc/article_attachments/26960568592796)

### Sélectionner le point de départ de la tournée

Pour initier le remplissage, vous devez définir quelle demande servira de base au calcul de l'itinéraire :

- Cliquer sur une demande d'intervention sur la carte pour la choisir comme point de départ.
- Consulter le volet à droite de la carte qui affiche alors le détail de la demande sélectionnée.
- Vérifier que la demande sélectionnée correspond bien à votre priorité.

Le système planifiera cette première demande, puis cherchera automatiquement la demande la plus proche pour compléter la suite de la journée.

### Lancer le remplissage automatique

- Cliquer sur le bouton **Remplir la tournée**.
- Patienter pendant que le système traite les données. Vous êtes ensuite automatiquement renvoyé vers le planning.
- Constater que la journée du technicien a été complétée à partir du point de départ choisi.

Le système fonctionne par itérations : il planifie une demande, puis repart de la position de celle-ci pour trouver la suivante la plus proche, crée l'intervention, et ainsi de suite.

Le processus s'arrête automatiquement dans les trois cas suivants :

- Il n'y a plus de créneau disponible sur la tournée du jour.
- Aucune demande d'intervention (DI) ne peut être insérée dans la durée de disponibilité restante.
- Les demandes restantes ne respectent pas la zone limite (rayon) définie dans vos critères.

Mis a jour le : 22/04/2026
