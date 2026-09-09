---
url: https://servicescompris.extrabat.com/tag/comment-parametrer-un-nouveau-logiciel-de-comptabilite-dans-extrabat
url_finale: https://servicescompris.extrabat.com:443/tag/comment-parametrer-un-nouveau-logiciel-de-comptabilite-dans-extrabat/
date_collecte: 2026-09-09
destination: centre_aide
---

Par définition, Extrabat peut s’interfacer avec n’importe quel logiciel de comptabilité car ces échanges sont normés et chaque éditeur les respecte à ce jour.

A ce jour, Extrabat est interfacé avec ***68 logiciels de comptabilité*** et cette liste s’allonge d’année en année.

Afin d’inscrire un nouveau logiciel de comptabilité compatible avec Extrabat, nous allons vous présenter un cas d’école avec :

- Marine la cliente Extrabat qui veut intégrer son logiciel de comptabilité Néo Comptabilité
- Anthony le commercial Extrabat
- Nicolas le développeur Extrabat
- Eric le développeur de chez Néo

Tous les échanges peuvent être réalisés par mail et si besoin des échanges téléphoniques sont préconisés par les parties prenantes :


- ***Demande de la part de Marine à Eric de son cahier des charges d’intégration des écritures comptables afin qu’Extrabat s’adapte à leurs méthodes et réponse d’Eric:***

Exemple de mail :

Bonjour,

A la demande de Marine, veuillez trouver ci-joint un document expliquant le format d’échange de données lié à une intégration comptable de la gestion vers notre comptabilité.

N’hésitez pas à revenir vers moi si besoin.

Cordialement,)

- ***Réponse reçue d’Eric** **sur le format préconisé*** **:**

1. INTEGRATION COMPTABLE v4.2

1.1 Objet

L’intégration comptable consiste à importer dans la comptabilité :

–  les écritures liées aux différentes pièces de ventes ou d’achats générées dans la gestion commerciale ;

–  les renseignements caractérisant les tiers clients et fournisseurs saisis en gestion commerciale. 
1.2 Format général 
Le fichier d’intégration doit être un fichier texte ASCII ANSI WINDOWS d’extension « .txt ». 
Les enregistrements sont délimités par un classique CR (retour chariot – code ASCII = 13) + LF (saut de ligne – code ASCII = 10). 
Les champ d’un enregistrement sont délimité par des tabulations (code ASCII = 9, nommé [TAB] dans l’exemple). C’est un fichier unique dont les lignes peuvent correspondre à différentes catégories d’enregistrements :

• « A » : Enregistrement d’initialisation

• «T»:Tiers

• « C » : Contact d’un tiers

• « R » : Compte bancaire (RIB) d’un tiers

• «E»:Ecriture

• « X » : Ventilation analytique d’une écriture

• « Z » : Enregistrement récapitulatif 
Les premières lignes du fichier décrivent les champs présents (parmi les champs disponibles) pour chacun des types d’enregistrements sous la forme : T[TAB]REFERENCE [TAB]DESIGNATION… 
Les lignes suivantes correspondent aux données des enregistrements selon leurs types. 
1.3 Nom du fichier 
Le nom du fichier n’est pas imposé mais le fichier doit se situer dans le répertoire d’intégration de la comptabilité tel que défini dans son paramétrage. 
1.4 Types des données 
Ci-dessous la définition ainsi que le format des types de données présentes dans les fichiers transférés :

Format

Descriptif

A

Texte alphanumérique comportant un nombre de caractères maximum limité (nombre placé à côté)

Ax

Texte multi-lignes (mémo)
Utilisez ‘||’ (Alt Gr+6) pour les retours à la ligne du texte

N

Valeur numérique décimale (virgule ou point comme séparateur décimal)

$

Valeur monétaire (virgule ou point comme séparateur décimal) avec ou sans symbole monétaire

D

Date sous la forme JJ/MM/AA ou JJ/MM/AAAA

E

Nombre entier non décimal

L

Indicateur logique :

–  ‘X’ = activé

–  ‘-‘ = désactivé

Remarques :

• La colonne « O» défini une colonne dont la présence est obligatoire pour le traitement de la ligne. Par ailleurs, en cas d’absence de donnée sur un champ facultatif, la valeur sera renseignée par la valeur telle que définie dans l’enregistrement par défaut, s’il existe.

• Les noms des colonnes peuvent être fournis indistinctement en majuscules ou en minuscules, avec ou sans accents, et avec ou sans les espaces entre les mots

- ***Réponse de Nicolas le développeur d’Extrabat avec un exemple de fichier :***

Bonjour,

J’ai adapté le format dans Extrabat.

Ci-joint un exemple d’export de 2 factures avec des données fictives, pour validation du format de fichier,

Cordialement,

- ***Réponse d’Eric de chez Néo avec de la méthode et du conseil :***

Bonjour,

Après vérification, quelques erreurs dans le fichier transmis (mais c’est normal sur un premier jet).

Attention : Impératif

- Une ligne du fichier débute toujours par une balise identifiant le type de l’enregistrement ;
- Toujours déclarer les tiers avant les écritures pour éviter le problème de l’intégration d’une écriture sur un tiers inconnu en compta et dont c’est la première intégration. A la limite, vous pouvez suivre l’ordre défini dans le format d’échanges à savoir : A, T, C, R, E, X.

Conseil

- Sur les écritures de ventes, privilégier le n° de facture client dans le champ PIECE plutôt que REFERENCE qui contient plutôt une référence de commande du client.

Restant à votre disposition,

Cordialement,

- ***Suite à un nouveau fichier de test de Nicolas, une nouvelle remarque constructive d’Eric :***

Bonjour,

- La balise des écritures est bien E et non A;
- Toujours déclarer les tiers avant les écritures pour éviter le problème de l’intégration d’une écriture sur un tiers inconnu en compta et dont c’est la première intégration.

Il semblerait que le fichier généré ne possède que les champs obligatoires à l’intégration. Il serait quand même plus cohérent d’envoyer aussi des infos permettant de créer les enregistrements en compta avec un maximum de précision, par exemple : échéance de la facture, mode de règlement de la facture, mode de règlement par défaut du tiers, représentant par défaut du tiers, compte collectif du tiers, …

Cordialement,

- ***Nouvel envoi de fichier de test de Nicolas et réponse d’Eric :***

Bonjour,

Le fichier transmis est valide.

Quand je parlais de collectif, c’était sur l’enregistrement de type tiers et non sur l’écriture.

Mais comme vous l’expliquez, il s’agit là d’information non obligatoire mais faisant partie de l’enrichissement intéressant des données.

Nous pourrons effectivement en rediscuter par la suite.

Cordialement,

*Au final, avec huit échanges par mail, nous avons paramétré un nouveau logiciel de comptabilité dans Extrabat et cela a été réalisé avant la formation Extrabat, ce qui est fortement conseillé 🙂*