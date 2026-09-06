---
source: https://support.openfire.fr/hc/fr/articles/22805129291036-Configuration-g%C3%A9n%C3%A9rale
categorie: Configurer OpenFire
titre: Configuration générale
date_recuperation: 2026-09-05
---

# Configuration générale

Cet article a pour objectif de vous guider dans le paramétrage de la prise de rendez-vous en ligne. Les options de paramétrage vous permettront d'être en adéquation avec votre activité et votre façon de travailler.

Cet article contient les sections suivantes :

- [Paramétrages généraux](#h_01K6ZGZ9NGK1KYCZHK8GHNBSK1)
- [Temps de trajet de la première intervention](#h_01K6ZKFGPSV38THNPYYYWP9WT1)

# Paramétrages généraux

Pour répondre au mieux à votre façon de travailler et à ce que vous souhaitez proposer à vos clients, un certain nombre de paramétrages sont disponibles.

Chemin d’accès :

- **Pour les clients basiques** : OpenFire > Configuration > Paramètres > Intervention > Section Prise de rendez-vous en ligne
- **Pour les autres plans** : Interventions > Configuration > Paramètres > Section Prise de rendez-vous en ligne

Paramétrer les informations suivantes :

- **Autorise les nouveaux clients**

Ce paramètre vous permet de définir si vous proposez la prise de rendez-vous en ligne à tous les visiteurs de votre site internet ou uniquement à vos clients. Si vous proposez la réservation en ligne à vos clients uniquement, il faut qu’ils disposent d’un compte portail.

  **📓**Pour aller plus loin → Gérer les accès portail pour vos clients (à venir).

- **Techniciens disponibles**

Vous pouvez définir les techniciens disponibles pour réaliser les rendez-vous pris en ligne.

- **Jours ouverts**

Vous pouvez définir les jours de la semaine ouverts à la prise de rendez-vous en ligne.

- **Nombre de jours ouverts**

Vous pouvez définir la période (en jours) pour laquelle vous ouvrez la prise de rendez-vous en ligne. Le nombre de jours maximum est de 180 jours, donc 6 mois.

- **Mode de recherche**

Le mode de recherche permet de définir comment sont calculés les créneaux disponibles. Vous pouvez choisir le mode de recherche qui correspond le mieux à votre activité / votre région.

Il existe plusieurs modes de recherche :

- Aller
- Retour
- Aller / Retour
- Aller ou Retour
- Aller si matin / Retour si après-midi

  **📓**Pour aller plus loin → Paramètres de la recherche (à venir).

- **Type de recherche**

Le type de recherche vous permet d’indiquer le critère de recherche à prendre en compte pour la proposition des créneaux disponibles. Il peut être paramétré :

- en distance (km)
- en durée (minute)

  💡Note : Le type de recherche en distance est calculé sur la distance réelle (nombre de kilomètres
  par la route).

  💡Note : Le mode de recherche fonctionne de concert avec le type de recherche.
  Par exemple, si votre paramétrage du mode de recherche est Aller et le type de
  recherche est défini à 10 km, les propositions seront filtrées sur les créneaux dont la distance Aller par rapport au rendez-vous précédent ne dépasse pas 10 km.

- **Journée vierge**

Vous pouvez autoriser, ou non, la réservation par vos clients sur une journée où il n’y a pas encore de rendez-vous. Si vous autorisez la réservation sur des journées vierges, le champ **"Type de recherche pour les journées vierges"** vous permet d’indiquer la durée maximale ou la distance maximale que vous souhaitez parcourir. Ceci correspond à votre zone d’intervention.

![](https://support.openfire.fr/hc/article_attachments/22805129282716)

Ce paramètre de distance ou durée n'est valable que pour le premier rendez-vous. Pour les rendez-vous suivants, les propositions seront calculés par rapport au paramétrage du **Type de recherche**.

- **Afficher le prix de la prestation**

Si ce paramètre est coché, les prix des prestations sont indiquées lors de la prise de rendez-vous.

![](https://support.openfire.fr/hc/article_attachments/22805088564508)

  💡Note : L'affichage du prix de la prestation est lié aux produits présents dans le modèle d'intervention.

  **📓**Pour aller plus loin → Modèle d'intervention (à venir) et Rapport d'équipement (à venir)

- **Etat des RDV**

Ce paramètre permet de définir l’état (Brouillon ou Confirmé) dans lequel sont créés les rendez-vous.

- **Fichier PDF des Conditions Générales de Vente**

Vous pouvez charger un document PDF que le client pourra consulter et accepter en fin de processus de prise de rendez-vous en ligne.

![](https://support.openfire.fr/hc/article_attachments/22805853129500)

- **Libellé horaires**

Lorsqu’ils prennent rendez-vous en ligne, les clients se positionnent sur un créneau du matin ou un créneau de l’après-midi. Vous pouvez spécifier les horaires correspondant à ces créneaux.

![](https://support.openfire.fr/hc/article_attachments/22805088566556)

- **Notes de confirmation de RDV**

Ceci est un champ qui permet de spécifier des informations génériques additionnelles pour le client. Ces notes apparaissent à la fin du processus de prise de rendez-vous en ligne, juste avant la validation du créneau.

Ce message est au format HTML, ce qui signifie qu'il peut contenir du texte, des liens, et d'autres éléments de mise en forme.

*Exemple : "Nous revenons vers vous pour vous préciser notre créneau de passage."*

- **Bouton de redirection**

A la fin du processus de prise de rendez-vous en ligne, il y a un bouton de redirection. Si vous avez votre propre site internet, vous pouvez renseigner l’URL du bouton de redirection ainsi que le libellé du bouton.

**![](https://support.openfire.fr/hc/article_attachments/22805088567068)**

#

# **Temps de trajet de la première intervention**

Une option est disponible pour choisir d’inclure, ou non, le temps de trajet de la première intervention.

Chemin d’accès :

- **Pour les plans basiques** : OpenFire > Configuration > Paramètres > Intervention > Section Planification d’intervention
- **Pour les autres plans** : Interventions > Configuration > Paramètres > Section Planification d’intervention

Si l’option est activée, le temps de trajet est ajouté à l’heure de début de la première intervention. Par exemple, si un technicien commence à 8h et que le premier rendez-vous est à 15 minutes, il sera positionné à 8h15 sur le planning.

Si l’option n’est pas activée, le rendez-vous se positionne au début de la journée de travail du technicien, en considérant qu’il commence à 8h quel que soit le temps de route qu’il a pour aller chez son premier client.

Ce paramétrage peut être défini différemment pour le matin et pour l’après-midi.

![](https://support.openfire.fr/hc/article_attachments/22806378503708)

Mis a jour le : 03/12/2025
