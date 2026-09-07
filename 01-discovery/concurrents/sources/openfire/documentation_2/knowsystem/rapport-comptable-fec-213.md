---
url: https://documentation.openfire.fr/knowsystem/rapport-comptable-fec-213
url_finale: https://documentation.openfire.fr/knowsystem/rapport-comptable-fec-213
date_collecte: 2026-09-06
destination: documentation_2
---

Le fichier des écritures comptables (FEC) est un document reprenant toutes les écritures comptables qui se sont déroulées durant un exercice donné.

Le FEC reprend l’ensemble des enregistrements informatiques qui constituent les écritures comptables de la comptabilité générale. Vous devez être en mesure de présenter un FEC pour chaque exercice comptable clos, avec toutes les écritures comptables enregistrées, y compris les écritures d’à nouveau.

## Extraire le FEC

Le fichier des écritures comptables est généré directement par OpenFire. Il est possible d'éditer ce rapport FEC au format .csv ou .txt en vous rendant dans Comptabilité > Rapports > FEC


Dans la fenêtre qui s’ouvre, il faudra alors sélectionner la plage de date concernée via les champs Start Date et End Date.

Vous avez 2 options lors de l'édition du rapport FEC :

1 - Vous transmettez à votre comptable toutes les écritures de fin d'année : le type d'export sera ainsi Officiel. Ce format permet de reprendre toutes les écritures d'une période donnée et les écritures des à nouveaux est repris via le journal d'ouverture.

2 - Vous transmettez qu'un journal ou des écritures de plusieurs journaux : le type d'export sera : Non-officiel comptabilisé uniquement (bien vérifier que vos pièces comptables soient comptabilisés en amont). Il faudra également désélectionner l’option inclure le journal d’ouverture afin de ne pas faire apparaitre les à-nouveaux et sélectionner les journaux que vous souhaitez exporter (Journal de Vente si vous ne transmettez que les écritures de factures de ventes à votre comptable)

En cliquant sur Generate, le fichier sera créé et il est téléchargeable, afin d'être consultable via le logiciel de votre choix.

   **__Attention__** : **dès que vous exportez les écritures comptables sur une période donnée pour les importer dans un autre logiciel comptable, vous devez impérativement bloquer l'accès à modification des écritures sur la période définie. __Exemple__ : vous exportez les écritures du mois de juin 2023, vous verrouillez les écritures jusqu'au 30 juin 2023. Ce verrouillage n'est pas définitif, vous pourrez toujours débloquer l'accès**

Pour verrouiller temporairement des écritures comptables, vous allez dans le menu Comptabilité > Configuration > Mettre à jour la date de verrouillage des comptes.

Une fenêtre s'affiche et vous notez la date à laquelle vous souhaitez bloquer l'accès temporairement dans les champs :

 - **Date de verrouillage pour les non-conseillers** : vous verrouillez les accès aux utilisateurs qui n'ont accès qu'à la facturation et paiement.

 - **Date de verrouillage pour les conseillers** : vous verrouillez les accès aux utilisateurs qui ont accès à toute l'application Comptabilité.

Vous pouvez revenir à tout moment pour modifier ces dates.

## Extraire les écritures comptables

Si le format du fichier FEC ne convient pas pour import des journaux dans un autre logiciel comptable (journal de ventes par exemple), vous pouvez également extraire les écritures comptables directement de la comptabilité. 

Pour cela, rendez-vous dans le menu Comptabilité > Conseiller > Ecritures comptables.

__**Pour rappel**__, les écritures des à nouveaux n'apparaissent pas dans les écritures comptables. Par conséquent, vous devez obligatoirement passer par le fichier FEC si vous souhaitez les à nouveaux.

__A savoir:__ Sur de nombreux logiciels de comptabilité, lorsque l'on clôture son exercice, on a un report des A nouveaux. Le principe est que tous les comptes de 1 à 5 sont lettrés à la fin de l'exercice et le logiciel va alors générer de nouvelles écritures au 1er jour du nouvel exercice.

Vous effectuez un filtre afin de n'avoir que la période souhaitée : le mois précédent (pour la TVA par exemple) ou une période définie.

Vous pouvez aussi ajouter le filtre Ventes afin de n'avoir que les écritures comptables du journal de vente (factures clients).

**__*Important*__** : Pour exporter toutes les lignes, il est impératif de modifier le nombre de lignes en haut à droite afin que toutes les lignes soient sur la page web.

Quand toutes les lignes sont sur la même page, il faut sélectionner toutes les lignes et cliquer sur Action>Exporter :

La fenêtre Exporter les données s'ouvre. Avant de générer le fichier Excel qui sera à transmettre à votre comptable, il faut cliquer :

- format d'export : Excel
- Exports enregistrés : Export Ecritures V1 (modèle existant par défaut)
- Exporter vers le fichier