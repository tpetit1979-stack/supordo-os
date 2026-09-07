---
url: https://documentation.openfire.fr/knowsystem/quels-documents-fournir-a-votre-comptable-212
url_finale: https://documentation.openfire.fr/knowsystem/quels-documents-fournir-a-votre-comptable-212
date_collecte: 2026-09-06
destination: documentation_2
---

Un certains nombre de documents comptables sont nécessaires à la tenue de votre comptabilité. Ceux-ci peuvent donc vous être demandé par votre expert-comptable. 

Parmi les plus courants nous pouvons noter:

- les factures d’achat et de vente,
- le fichier des écritures comptables (FEC).

## Les factures d'achat et de vente

Les factures sont exportables au format PDF depuis la vue Liste des factures de ventes ou d'achat.

Sélectionnez simplement les factures de votre choix, puis cliquez sur Imprimer > Factures:

Les factures apparaitront alors dans un seul et même fichier PDF.

## Le fichier des écritures comptables

Le fichier des écritures comptables (FEC) est un document reprenant toutes les écritures comptables qui se sont déroulées durant un exercice donné.

Le FEC reprend l’ensemble des enregistrements informatiques qui constituent les écritures comptables de la comptabilité générale. Les pièces comptables doivent être toutes comptabilisées avant d'éditer un FEC officiel. A l'édition de ce rapport, le logiciel va extraire aussi les écritures d’à nouveau.

##### Où se trouve le FEC ?

Le fichier des écritures comptables est généré directement par OpenFire. Il est possible d'éditer ce rapport FEC au format csv ou txt en vous rendant dans **Comptabilité > Rapports > FEC**


Dans la fenêtre qui s’ouvre, il faudra alors sélectionner la plage de date concernée via les champs Start Date et End Date.

Vous avez 2 options lors de l'édition du rapport FEC :

1 - Vous transmettez à votre comptable toutes les écritures de fin d'année : le type d'export sera ainsi Officiel. Ce format permet de reprendre toutes les écritures d'une période donnée. Les écritures des à nouveaux sont reprises via le journal d'ouverture.

2 - Vous transmettez qu'un journal ou des écritures de plusieurs journaux : le type d'export sera : Non-officiel comptabilisé uniquement (bien a vérifier que vos pièces comptables soient comptabilisés en amont). Il faudra également désélectionner l’option inclure le journal d’ouverture afin de ne pas faire apparaitre les à-nouveaux et sélectionner les journaux que vous souhaitez exporter (Journal de Vente si vous ne transmettez que les écritures de factures de ventes à votre comptable)

En cliquant sur Generate, le fichier sera créé et il est téléchargeable, afin d'être consultable via le logiciel de votre choix.

## Extraire les écritures comptables

Si le format du fichier FEC ne convient pas pour import des journaux dans un autre logiciel comptable (journal de ventes par exemple), vous pouvez également extraire les écritures comptables directement de la comptabilité.

Pour cela, rendez-vous dans le menu Comptabilité > Conseiller > Ecritures comptables.

__Pour rappel__, les écritures des à nouveaux n'apparaissent pas dans les écritures comptables. Par conséquent, vous devez obligatoirement passer par le fichier FEC si vous souhaitez les à nouveaux.

Vous effectuez un filtre afin de n'avoir que la période souhaitée : le mois précédent (pour la TVA par exemple) ou une période définie.

Vous pouvez aussi ajouter le filtre Ventes afin de n'avoir que les écritures comptables du journal de vente (factures clients).

__*Important*__ : Pour exporter toutes les lignes, il est impératif de modifier le nombre de lignes en haut à droite afin que toutes les lignes soient sur la page web.

Quand toutes les lignes sont sur la même page, il faut sélectionner toutes les lignes et cliquer sur Action>Exporter :

La fenêtre Exporter les données s'ouvre. Avant de générer le fichier Excel qui sera à transmettre à votre comptable, il faut cliquer :

- format d'export : Excel
- Exports enregistrés : Export Ecritures V1 (modèle existant par défaut)
- Exporter vers le fichier