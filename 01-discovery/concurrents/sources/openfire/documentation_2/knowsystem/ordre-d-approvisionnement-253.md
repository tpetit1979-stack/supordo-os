---
url: https://documentation.openfire.fr/knowsystem/ordre-d-approvisionnement-253
url_finale: https://documentation.openfire.fr/knowsystem/ordre-d-approvisionnement-253
date_collecte: 2026-09-06
destination: documentation_2
---

Les Ordres d’Approvisionnement permettent d'indiquer qu'il faut approvisionner certains produits pour un emplacement. 

Les ordres d’approvisionnement peuvent être générés de deux façons différentes :

- Automatiquement : C’est le cas notamment lorsque une commande génère automatiquement une demande de prix,
- Manuellement : un ordre peut être passé manuellement pour un article spécifique depuis la fiche article.

## Scénarios d'Approvisionnements

L’approvisionnement depuis la fiche article distingue deux scénarios différents :

## Lancer les règles de réapprovisionnement

Le planificateur Lancer les règles de réapprovisionnement est un moteur de calcul qui planifie et priorise la production et les achats automatiquement en fonction des règles définies sur les articles.

**Inventaire > Opérations > Lancer les règles de réapprovisionnement**une fois que vous êtes en mode Développeur :


Par défaut, le planificateur est configuré pour s'exécuter une fois par jour (OpenFire a créé automatiquement une Action Planifiée pour cela).

La planification s’applique sur les ordres de réapprovisionnement confirmés et qui n'ont pas encore été lancés.

## Approvisionnement depuis le menu Inventaire

Rendez-vous dans le menu

**Inventaire > Opérations > Tous les transferts**et cliquer sur

**Créer.**Plusieurs champs seront alors disponibles :

__Partie Haute:__

Partenaire : permet de renseigner le nom du fournisseur.

 A Savoir : Il est important de noter que les produits qui sont commandés dans un approvisionnement doivent être associés à un fournisseur dans OpenFire. Si un produit n'a pas de fournisseur associé, il ne sera pas disponible pour être ajouté à un ordre d'approvisionnement.

Emplacement d'origine : Ce champ est automatiquement renseigné. Il reprend généralement l'emplacement virtuel du fournisseur.  Plus d'informations sur [les emplacements](https://documentation.openfire.fr/knowsystem/entrepots-et-emplacements-227)

Date prévue : la date prévue est la date à laquelle l’approvisionnement pourra être validé. Par défaut elle correspond à la date de la saisie,

Semaine prévue : Numéro de la semaine correspondant à la date prévue.

Date réelle : Date à laquelle l'approvisionnement a été validé.

Document d’origine : document source de l’ordre d’approvisionnement.

Transporteur : permet de renseigner le transporteur utilisé pour cet approvisionnement

Responsable Technique: permet de renseigner le nom d'un responsable pour cet emplacement de stock

__Onglet Informations Complémentaires :__

Type de Livraison: Au choix parmi un menu déroulant comprenant

Type de préparation: Au choix parmi un menu déroulant comprenant **Référence commande client :** permet de faire le lien vers le bon de commande client. 

**Groupe d’approvisionnement :** groupe d’approvisionnement dans lequel est intégré l’approvisionnement. Le champ Groupe d'approvisionnement comprend par défaut le lien vers la commande d'achat d'où est issu cet approvisionnement. 

**Priorité :** un niveau de priorité peut être défini pour chaque ordre via un menu déroulant (Non urgent, normale, urgent, très urgent). La priorité définit l’ordre de traitement des approvisionnements lorsqu’ils sont lancés:

## Approvisionnement depuis la fiche article


            **Demande d'Approvisionnement :**


ou sur le Bouton Approvisionnement :

Ensuite, cliquez sur le bouton

**Créer,**Plusieurs champs seront alors disponibles:

__Partie Haute:__

Entrepôt :

Routes préférées : route que l’ordre d’approvisionnement doit suivre de préférence. Généralement, cette route est reprise du document source de l’ordre d’approvisionnement (exemple bon de commande client). Elle pourrait néanmoins être saisie manuellement, 

__Onglet Informations Complémentaires :__

Document d’origine : document source de l’ordre d’approvisionnement.

**Commande Fournisseur :** permet de faire le lien vers le bon de commande d'achat associée. 

Groupe d’approvisionnement : groupe d’approvisionnement dans lequel est intégré l’approvisionnement.

**Règle :** permet de préciser la règle choisie pour le réapprovisionnement. Elle peut-être définie automatiquement (par le système lorsque l’ordre provient d’un document spécifique) ou manuellement (forcée par le responsable des approvisionnements)..   *Plus d'informations sur [les règles d'approvisionnements.](https://documentation.openfire.fr/knowsystem/regles-d-approvisionnement-249)*

**Adresse client :** il s’agit de l’adresse de livraison exacte de l’article chez le client dans le cadre d’une opération de drop-shipping (livraison directe chez le client)

**Notes :** lorsque l’ordre d’approvisionnement provient d’un document source (exemple bon de commande client), les notes reprennent la description de l’article à approvisionner.

Lorsque l’ordre est créé manuellement, les notes servent à décrire le produit à approvisionner.