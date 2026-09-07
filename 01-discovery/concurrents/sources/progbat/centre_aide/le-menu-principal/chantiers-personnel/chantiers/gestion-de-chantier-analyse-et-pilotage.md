---
url: https://docv5.progbat.com/le-menu-principal/chantiers-personnel/chantiers/gestion-de-chantier-analyse-et-pilotage
url_finale: https://docv5.progbat.com/le-menu-principal/chantiers-personnel/chantiers/gestion-de-chantier-analyse-et-pilotage
date_collecte: 2026-09-06
destination: centre_aide
---

# Gestion de chantier, analyse et pilotage

## La fiche Chantier

A l'ouverture, la fiche chantier affiche plusieurs blocs d'informations :

### Le bloc "Chantier"

- **Le statut du chantier** :
  - *A l'étude* : Vous êtes dans la phase d'étude, les devis sont en cours de chiffrage, les travaux n'ont pas débuté.
  - *En cours* : Lorsqu'un devis rattaché à un chantier est passé au statut "Accepté", le statut du chantier passe automatiquement "En cours".
  - *Achevé* : Passez le statut en "Achevé" lorsque les travaux et les paiements sont terminés.
    - *Vous ne pourrez plus saisir d'heures de travail, ni ajouter des phases au planning, mais vous pourrez encore saisir des dépenses telles que des factures d'achat.*
  - *Perdu* *:* Malheureusement, vous n'avez pas obtenu ce chantier.
    - 💡Nous recommandons de créer la fiche chantier uniquement à partir du moment où le devis est accepté, pour éviter de créer des chantiers "pour rien". [1 - Depuis un devis](https://docv5.progbat.com/le-menu-principal/chantiers-personnel/chantiers/creer-un-chantier#au-moment-de-la-creation-dun-devis)
  - *Litige* : Ca arrive parfois....
- **L'identifiant** : quelques mots pour retrouver facilement le chantier. Par défaut, il est composé du premier mot du nom du chantier, et de la ville.
- **Nom du chantier** .
- **Le chargé d'affaire** : Il s'agit du chargé d'affaire ou conducteur de travaux en charge de ce chantier.
- **La date d'ouverture du chantier** : il s'agit de la date officielle déclarée par le maître d'oeuvre par procès verbal. A partir de cette date, ce sont les entreprises qui sont juridiquement responsables du chantier. 
Le client (maître d'ouvrage) retrouvera la pleine propriété et responsabilité du chantier le jour de la réception officielle (PV de réception).
- **L'adresse postale** du chantier.

### Le bloc Client

- Une simple vignette contenant les informations du client attaché à ce chantier. 
  - Cliquez sur la vignette pour affecter un autre client si besoin.
  - Cliquez sur l'oeil en haut à droite pour ouvrir la fiche client.

#### Modifier le client attaché au chantier

- Cliquez sur le bloc Client,
- Choisissez un autre client dans le premier champ du formulaire.
- Validez.

### Le bloc Informations

- Un champ pour saisir librement des informations internes.

### Les conditions de règlement

- Par défaut, le chantier hérite des conditions de règlement par défaut de l'entreprise, [définies ici](https://docv5.progbat.com/pour-bien-demarrer/parametrage/parametres-de-lentreprise/autres-parametres#conditions-de-reglement) .
- Si des conditions spécifiques pour le client ont été saisies dans la fiche client, le chantier héritera des conditions spécifiques de la fiche client.
- Et vous pouvez, si besoin, définir des conditions spécifiques pour le chantier, qui seront différentes des conditions de règlement de l'entreprise et de celles du client.

### Le bloc Contacts

Si vous réalisez plutôt de "gros" chantiers, vous allez régulièrement rencontrer les mêmes architectes, maîtres d'œuvre, coordinateurs de sécurité, OPC, etc...

Enregistrez tous ces contacts dans une fiche "Tiers", dans une catégorie que vous aurez créée.

Vous pourrez alors simplement ajouter les contacts pour chaque chantier, pour faciliter votre communication avec ces divers intervenants.

Exemple : [Créez une catégorie de Tiers](https://docv5.progbat.com/le-menu-principal/contacts#gerez-vos-propres-categories-de-contacts) "MO", pour y saisir les architectes et maîtres d'oeuvre. Ajouter l'architecte ou le maître d'oeuvre à ce chantier en cliquant sur "Nouveau contact".

## Section Marchés de travaux

### La liste des marchés de travaux

Si le chantier comporte plusieurs marchés, il seront affichés ici :

- Sélectionnez "Analyse globale" pour obtenir les statistiques de tous les marchés du chantier.
- ou sélectionnez le marché que vous souhaitez analyser.

### La synthèse

Ce premier onglet affiche quelques chiffres clés sur le chantier ou le marché sélectionné.

#### Simulation en temps réel

Ce petit outil graphique, extrêmement simple à utiliser, permet de s'assurer, à tout moment, que le chantier ne "dérape" pas, c'est à dire que les achats déjà réalisés et le temps passés correspondent à l'avancement du chantier, et soient cohérents par rapport aux prévisions de dépenses.

Déplacez simplement le curseur "Avancement des travaux" selon votre estimation, pour vérifier si les curseurs matériaux, main d'oeuvre et sous-traitance restent bien au vert, ou s'ils passent à l'orange ou au rouge. Simple et efficace !

👉 **Les achats de matériaux sont pratiquement à 100%, alors que le chantier n'est qu'à 70% d'avancement :**

- Si tous les matériaux pour ce chantier ont déjà été achetés, tout est normal puisque je n'aurai plus d'achat à faire jusqu'à la fin
- Sinon, il faut s'inquiéter et tenter de résoudre ce problème.

👉 **84% de la main d'œuvre prévue a déjà été utilisée :**

- Si le chantier nécessitait plus de monde au début qu'à la fin, cet écart peut être normal.
- Sinon, il faut là aussi s'inquiéter, le chantier est en train de déraper.

### Les ventes

Consultez les listes et accédez rapidement aux devis et aux factures du chantier, ou du marché sélectionné.

### Les dépenses

Consultez les listes et accédez rapidement aux bons de commandes, bons de livraisons, matériaux utilisés et factures d'achat du chantier, ou du marché sélectionné.

- Astuce : dans la liste "Matériaux", cliquez sur "Afficher les détails" pour voir la liste des bons de livraisons, transferts de marchandises, factures d'achats

### La main d'oeuvre

Consultez la liste des heures saisies pour ce chantier ou le marché sélectionné.

### La sous-traitance

Consultez les listes et accédez rapidement aux bons de commandes, travaux sous-traités, et factures de vos sous-traitant du chantier, ou du marché sélectionné.

## Section ProGBox

Accédez en un clic à l'espace de stockage de documents [ProGBox](https://docv5.progbat.com/presentation-generale/progbox-archivage-de-documents) du chantier.

Sur l'exemple ci-dessus, nous voulons estimer la rentabilité du chantier avec un avancement à 70%, simplement en déplaçant le premier curseur.

Mis à jour