---
url: https://documentation.openfire.fr/knowsystem/liste-de-diffusion-229
url_finale: https://documentation.openfire.fr/knowsystem/liste-de-diffusion-229
date_collecte: 2026-09-06
destination: documentation_2
---

## Création manuelle

**Publipostages > Listes de diffusion**. Cliquez ensuite sur le bouton Créer :

Vous pouvez créer manuellement des nouveaux contacts, en cliquant sur le bouton Créer.

En cliquant sur l'icone Destinataire, vous accédez aux destinataires de cette liste:

Il est alors possible d'en créer ou d'en importer via les boutons dédiés présents en haut à gauche de la fenêtre:

En cliquant sur créer, vous pouvez introduire les informations nécessaires, comme le nom, la liste de diffusion, les étiquettes, la société, …

*Lorsqu'un contact appartient à une liste de diffusion, celles-ci sont accessible via un bouton d'accès rapide depuis la fiche du contact:*

## Import des contacts dans les listes de diffusion

Vous pouvez importer plusieurs contacts à votre liste en passant par un import Excel.

Pour cela, créez dans un premier temps toutes vos listes de diffusion (newsletter, rappel de ramonage... par exemple). Dans un fichier Excel, créez trois colonnes : email, name et list_id

Rendez-vous ensuite dans Publipostages>Publipostages>Liste de diffusion et cliquez sur une liste de diffusion déjà existantes. Cliquez ensuite sur "Importer" et choisissez votre fichier Excel. Cliquez sur "Valider" pour vérifier qu'Openfire ne vous retourne aucune erreur et importez.*Même si vous importez les contacts depuis une liste de diffusion qui n'est pas celle à laquelle ils appartiennent, la colonne "list_id" permet de redistribuer chaque contact dans la bonne liste de diffusion. Dans l'exemple précédent, même en important le fichier depuis la liste de diffusion "Newsletter", le contact Jean Dujardin ira ainsi bien dans la liste de diffusion "Rappel ramonage annuel" et non dans "Newsletter".*

## Création automatique

Si vous utilisez OpenFire pour gérer votre site Web, vous pouvez ajouter des widgets de newsletter dans la partie que vous souhaitez de votre site web afin de créer automatiquement les contacts. En effet, ces widgets permettent aux visiteurs de s’inscrire dans une liste de diffusion préconfigurée.

Pour se faire cliquez sur l’application **Site Web** disponible via l'icone 

Le site s’ouvre, sur la partie backend, allez donc dans la partie où vous souhaitez insérer le widget d’inscription automatique à une liste de diffusion.

Cliquez ensuite, sur le bouton Editer en haut à droite:

La boite de widgets s’ouvre, pour sélectionner les widgets à insérer sur La page en cours.

Pour notre cas, nous avons le choix entre le widget Newsletter:

Le widget Newsletter permet d’insérer un bloc sur la page et qui porte un champ email à insérer par l’utilisateur et un bouton s’inscrire, à ce niveau on peut préconfigurer la liste sur laquelle va s’inscrire le visiteur du site:

De cette façon, l’inscription se fait par les utilisateurs automatiquement à travers le widget newsletter.

 Plus d'information sur le site Web