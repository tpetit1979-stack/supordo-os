---
source: https://support.openfire.fr/hc/fr/articles/19075536692508-G%C3%A9olocalisez-vos-prospects-et-clients
categorie: Utiliser OpenFire
titre: Géolocalisez vos prospects et clients
date_recuperation: 2026-09-05
---

# Géolocalisez vos prospects et clients

![All_tick_V2.png](https://support.openfire.fr/hc/article_attachments/19562982709276)

La géolocalisation des contacts dans OpenFire vous permet d’accéder à de nombreuses fonctions d’affichage, de planification de RDV et d’optimisation de vos tournées notamment.

Cet article contient les sections suivantes :

- [Géolocalisation manuelle ou automatique ?](#h_01JPQSHJ6F9FX2J0Q7KBHKBASW)
- [Géolocalisation manuelle depuis la fiche contact](#h_01JPQSHJ6FD78EV3B4CRNXN6ED)
- [Géolocaliser une liste de contacts](#h_01JPQSHJ6FPVN8Q4PXWAJ79H0X)
- [Géolocaliser un contact depuis l’application mobile](#h_01JPQSHJ6F0E9ATF5YE8TE3FB3)
- [Géolocaliser l’adresse du contact](#h_01JPQSHJ6G7JSAB68YV6J9P2TB)
- [Géolocaliser la position du téléphone](#h_01JPQSHJ6GTGPRE6QAVHX037YN)

## Géolocalisation manuelle ou automatique ?

La fonction de géolocalisation permet d'associer les coordonnées GPS à la fiche du contact.

La géolocalisation peut-être :

- **Manuelle **→ l’utilisateur devra manuellement déclencher et vérifier la géolocalisation de son contact
- **Automatique ** → dès l’enregistrement de l’adresse de votre contact, OpenFire tentera de la géolocaliser automatiquement

**📓**Pour aller plus loin → [Paramètres de géolocalisation](https://support.openfire.fr/hc/fr/articles/24124483323676)

## Géolocalisation manuelle depuis la fiche contact

Pour ce faire, rendez vous dans l’onglet **"Localisation"**.

Une fois l’adresse du contact renseignée, vous pouvez cliquer sur le bouton **"Calculer sur base de l'adresse"** :

![](https://support.openfire.fr/hc/article_attachments/19098144568220)

Les coordonnées GPS seront recherchées et mémorisées :

![](https://support.openfire.fr/hc/article_attachments/19098144568604)

Vous pouvez à tout moment, mettre les informations de l’adresse à jour en cliquant sur le bouton "**Actualiser**".

Vous pouvez également forcer manuellement les coordonnées GPS dans les champs Lat et Long pour plus de précision.

Vous pouvez également consulter l’origine et la qualité de la géolocalisation :

![](https://support.openfire.fr/hc/article_attachments/19098161113116)

Voici les valeurs disponibles pour l’état de géolocalisation :

- **Non géolocalisé **: la géolocalisation n’a pas été tentée
- **Succès **: la géolocalisation a réussi
- **Échoué **: la géolocalisation n’a pas fonctionné (l’adresse comporte peut-être des imprécisions ou des anomalies)
- **Manuel **: les coordonnées ont été définies manuellement, où la géolocalisation a été réalisée depuis le mobile, en bornant la position du téléphone
- **Sans adresse** : le contact ne dispose pas d’adresse

Voici les niveaux de précisions disponibles :

- **Manuel **: les coordonnées ont été saisies manuellement
- **Excellent **: la précision est normalement vérifiée au niveau du numéro de la rue
- **Haut **: la précision est normalement vérifiée au niveau de la rue
- **Moyen **: la précision est normalement vérifiée au niveau du code postal
- **Bas **: la précision est faible, seule la commune semble avoir été identifiée
- **Indéterminé **: aucune géolocalisation n’est réalisée
🚨Avertissement : Lorsque la géolocalisation du contact a été effectuée depuis l’application mobile, par bornage du téléphone, l’état de géolocalisation et le niveau de précision sont définis comme “manuel”. 
## Géolocaliser une liste de contacts

Vous pouvez géolocaliser une liste de plusieurs contacts simultanément.

Pour cela, depuis la liste de vos contacts, vous pouvez utiliser les Filtres prédéfinis des contacts pour ne conserver à l’écran que les contacts non géolocalisés :

![](https://support.openfire.fr/hc/article_attachments/19098161113372)

Une fois vos contacts sélectionnés, vous pouvez utiliser l’action de géolocalisation :

![](https://support.openfire.fr/hc/article_attachments/19098144571164)

Vous accédez alors à une fenêtre de géolocalisation en masse.

Dans cette fenêtre, vous pouvez choisir le mode de traitement des contacts de votre choix :

- **Mettre à jour tous les contacts sélectionnés **: Cette option met à jour les coordonnées GPS de tous les contacts sélectionnés, même ceux qui sont déjà géolocalisés.
- **Mettre à jour tous les contacts sélectionnés sauf les contacts géolocalisés **: Cette option met à jour les coordonnées GPS de tous les contacts sélectionnés qui n’ont pas déjà été géolocalisés.

Une fois votre choix fait, vous pouvez cliquer sur** “Géolocaliser” **en haut à gauche.

![](https://support.openfire.fr/hc/article_attachments/19098144572316)

💡Note : La mention “Adresse non géolocalisée” est présentée chaque fois que cette information est pertinente pour l’utilisateur, comme par exemple sur le formulaire de vos interventions :
![](https://support.openfire.fr/hc/article_attachments/19098144573212)

## Géolocaliser un contact depuis l’application mobile

Depuis l’application mobile, vous pouvez créer des contacts ou retrouver l’ensemble de vos contacts déjà existants.

**📓**Pour aller plus loin → [Les équipes commerciales](https://support.openfire.fr/hc/fr/articles/19088301569180)

Deux méthode de géolocalisation sont disponibles depuis le mobile :

### **Géolocaliser l’adresse du contact**

Depuis une fiche contact, vous retrouvez un bouton **“Géolocaliser l’adresse”**.

| ![](https://support.openfire.fr/hc/article_attachments/19098161116188) | ![](https://support.openfire.fr/hc/article_attachments/19098161118108) |
| --- | --- |

En cliquant dessus, la recherche est effectuée à l'aide du service de géolocalisation définit par défaut dans votre environnement (Open Street Map, Bano ou Google Place Map), et un point de localisation vous est proposé. Si ce point vous convient, vous pouvez** “Valider”** la recherche.
🧑‍🏫Exemple : Ce mode de géolocalisation est particulièrement utile lorsque vous ajoutez un contact sans être sur place.
### **Géolocaliser la position du téléphone**

Une autre méthode de géolocalisation vous est proposée depuis le mobile :

Cliquer sur **“Géolocaliser ma position”** permet de borner votre mobile et d'enregistrer votre localisation actuelle comme l’adresse du client.
🧑‍🏫Exemple : Ce mode de géolocalisation est utile pour enregistrer l’adresse d’un contact lorsque vous êtes chez lui.🚨Avertissement : Pour utiliser cette fonctionnalité, il est nécessaire d’autoriser la localisation dans les paramètres de l’application.
Vous pouvez observer l’état de géolocalisation d’un contact depuis sa fiche.

Au niveau de l’adresse du client, deux statuts peuvent apparaître :

- Adresse non géolocalisée
- Adresse géolocalisée

![](https://support.openfire.fr/hc/article_attachments/19098144575516)

Mis a jour le : 09/12/2025
