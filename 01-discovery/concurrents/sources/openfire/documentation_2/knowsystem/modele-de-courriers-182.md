---
url: https://documentation.openfire.fr/knowsystem/modele-de-courriers-182
url_finale: https://documentation.openfire.fr/knowsystem/modele-de-courriers-182
date_collecte: 2026-09-06
destination: documentation_2
---

Les modèles de courrier permettent d'intégrer des formulaires PDF à votre base, afin de pouvoir les imprimer ou les joindre à vos mails, à vos devis, etc... Ces documents peuvent aussi être renseignés automatiquement et ajoutés à certains objets comme vos devis, ou vos factures.

## Créer ou modifier un modèle

Vous pouvez créer ou modifier ces modèles en vous rendant dans **Vente > Configuration > Modèles de courriers** :

La liste des modèles de courriers apparaitra alors avec le nom du document PDF associé:

Pour créer un modèle de courrier, il vous suffit de cliquer sur Créer :

Vous pourrez alors charger votre fichier au format PDF.

L'option Impression rapide permet de rendre accessible ce document depuis le menu Imprimer de l'objet choisi (bon de commande, facture, etc...) :

Les objets (Accès) en question sont les suivants :

  - **Factures** : Comptabilité>Ventes>Factures Clients

  - **Bon de commande** : Ventes>Ventes>Devis ou Bons de commandes

  - **Piste/opportunité** : Ventes>CRM>Mon Pipeline

  - **Planning d'intervention OpenFire** : Interventions>Planning

  - **Intervention à programmer** : Interventions>Interventions>Demandes d'intervention ou Entretien Maintenance ou SAV

  - **Modèle d'article** : Ventes>Ventes>Articles

  - **Partenaire** : Ventes>Ventes>Clients

  - **Incident** : Projet>Rechercher>Incidents

  - **Transfert** : Inventaire>Opérations>Tous les transferts

Une fois sauvegardé, le document est alors accessible depuis l'objet en question:

Il est également possible laisser le document éditable. Ainsi, s'il s'agit d'un PDF, il sera possible de le remplir via le navigateur Web:

Attention: Cela nécessite d'importer un fichier PDF éditable (type formulaire).

## Remplissage automatique des documents

Il est possible de remplir automatiquement certains champs d'un formulaire PDF. Ainsi, à l'impression, les documents seront préremplis.

Pour cela, un tableau permet de de faire correspondre la valeur à récupérer avec le champ PDF à remplir. Comme précédemment, cela nécessite d'importer un fichier PDF éditable (type formulaire).

Par exemple, la valeur *%(c_name)s* permet ici d'afficher le nom du client dans le champ a1.

Attention: Le paramétrage de ces valeurs nécessite de vous rapprocher du support OpenFire. Pour toutes demandes, merci de vous rapprocher du support, par mail à l'adresse support@openfire.fr, ou par téléphone au 02.30.96.02.65.