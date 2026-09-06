---
source: https://support.openfire.fr/hc/fr/articles/26985634783260-Planification-des-demandes-d-intervention-depuis-la-carte
categorie: Utiliser OpenFire
titre: Planification des demandes d'intervention depuis la carte
date_recuperation: 2026-09-05
---

# Planification des demandes d'intervention depuis la carte

Cet article vous explique comment sélectionner vos demandes d'intervention (DI) directement depuis la carte, identifier les meilleures tournées disponibles et planifier vos techniciens de manière optimisée en seulement quelques clics.

Cet article contient les sections suivantes :

- [Accéder à la vue carte](#h_01KPRC2K0PQ5RK58H58HZDRQYW)
- [Sélectionner les demandes à planifier](#h_01KPRC2K0RPZMVT756KDXTQ9TT)
- [Configurer les critères de recherche](#h_01KPRC2K0XFR2HGY0TN9GENHA3)
- [Choisir la tournée idéale](#h_01KPRC2K113HCPZTFJDVT9A74C)
- [Planifier et optimiser la tournée](#h_01KPRC2K14FKCHFS1GS47CTMQ3)

### Accéder à la vue carte

`Suivre le chemin d'accès suivant : Demandes d'intervention > Vue carte.`

Les demandes d'intervention apparaissent sous forme de marqueurs colorés sur la carte. Chaque couleur correspond à un état spécifique de la demande :

- **Gris** : Brouillon
- **Orange** : À planifier
- **Bleu** : Planifié
- **Rouge** : En retard
- **Vert** : Terminé
- **Noir** : Annulé

| 💡**Note **: Vous pouvez utiliser le champ de filtre (barre de recherche en haut de l'écran) pour affiner l'affichage des DI sur la carte selon vos besoins (par type de tâche, par zone géographique ou par client). |
| --- |

En survolant un marqueur avec votre souris, une fenêtre affiche les informations essentielles comme l'adresse du client, son téléphone, la tâche concernée et la date de la dernière intervention.

### Sélectionner les demandes à planifier

Pour commencer la planification, vous avez plusieurs possibilités :

- Cliquer sur un marqueur pour sélectionner une demande individuelle.
- Cliquer sur plusieurs marqueurs pour sélectionner un groupe de demandes.
- Cliquer sur le bouton **Planifier et optimiser** qui apparaît en haut de la carte une fois votre sélection faite.

![](https://support.openfire.fr/hc/article_attachments/26985646045980)

| 💡**Note **: Il est également possible de planifier une seule demande directement depuis sa fenêtre contextuelle en cliquant sur le bouton **Planifier**. Un assistant spécifique s'ouvrira pour vous proposer les créneaux les plus proches. |
| --- |

### Configurer les critères de recherche

Une fenêtre de configuration s'ouvre pour définir vos préférences de planification :

- Sélectionner un ou plusieurs techniciens dans le champ **Techniciens** (seuls les techniciens qualifiés pour les tâches sélectionnées s'affichent).
- Choisir une période de recherche dans le champ **De** :

  - **Semaine en cours** / **Semaine prochaine**.
  - **Mois en cours** / **Mois prochain**.
  - **Date** : pour choisir une date manuelle (la recherche s'étend sur 45 jours par défaut).
- Consulter le champ **Durée à planifier** qui calcule automatiquement le temps restant à planifier des demandes d'interventions choisies.

Vous pouvez également appliquer des filtres pour affiner les résultats :

- **Tournées** :

  - **Vides** : pour voir les tournées sans aucune intervention.
  - **Optimisables** : pour voir les tournées ayant au moins une intervention déjà planifiée pour lesquelles il reste encore de la disponibilité.
- **Impact** (remplissage souhaité) :

  - **Partiel** : pour laisser de la marge dans l'emploi du temps.
  - **Complet** : pour remplir au maximum le planning.
  - **Surcharge** : pour autoriser le dépassement des horaires habituels.

![](https://support.openfire.fr/hc/article_attachments/26985646046876)

| 🚨**Avertissement** : Le filtre **Surcharge** permet de planifier au-delà des horaires de travail du technicien. Utilisez cette option avec précaution pour éviter de surcharger vos équipes. |
| --- |

### Choisir la tournée idéale

- Consulter les résultats déjà présents dans l'onglet **Tournées**. Par défaut, une recherche est lancée automatiquement sur la semaine en cours pour tous les techniciens aptes, sans filtrage spécifique.
- Si vous avez modifié plusieurs critères (techniciens, dates, liste des DI ou filtres d'impact), cliquer sur le bouton **Mettre à jour la recherche** une fois vos modifications terminées pour actualiser l'ensemble des propositions.
- Analyser les informations des tournées proposées :

  - **Jour / Date** de la tournée.
  - **Technicien** assigné.
  - **Durée disponible** : temps libre restant.
  - **Distance min. (km)** : distance la plus courte entre vos demandes et les interventions déjà prévues. Pour les tournées vides, ce champ est laissé vide.
  - **Impact** : indiqué par un badge couleur (Vert = partiel, Orange = complet, Rouge = surcharge).
- Cliquer sur la ligne de la tournée souhaitée pour la sélectionner.

| **🧑‍🏫Exemple** : Vous avez 3 demandes pour un total de 4 heures. La tournée de Jean Dupont le mardi 15 avril dispose de 6 heures libres et se trouve à 3 km de vos demandes. L'impact est affiché en **Partiel** (badge vert) : c'est une excellente candidate. |
| --- |

### Planifier et optimiser la tournée

- Vérifier la liste des demandes dans l'onglet **Demandes d'intervention**.
- Si vous retirez des DI de la liste, cliquer sur **Mettre à jour la recherche** pour recalculer les tournées disponibles.
- Cliquer sur le bouton **Planifier et optimiser**.

Le système effectue alors automatiquement les actions suivantes :

- Création et assignation des interventions au technicien.
- Placement des interventions dès le premier créneau disponible.
- Réoptimisation de l'itinéraire pour trouver le meilleur trajet.
- Passage de la tournée à l'état **Confirmée**.

| 💡**Note **: Si les adresses de départ et de retour ne sont pas définies pour la tournée, le système utilise les adresses renseignées dans la fiche du technicien. |
| --- |

### Bonnes pratiques

- Lorsque vous modifiez des critères de recherche ou retirer des demandes d'intervention, n'oubliez pas de mettre à jour la recherche pour toujours avec les meilleures propositions.
- Vérifiez que les adresses des clients sont complètes pour garantir un calcul de trajet précis.
- Utilisez le filtre **Optimisables** pour compléter des tournées existantes au lieu d'en créer de nouvelles.

Mis a jour le : 24/04/2026
