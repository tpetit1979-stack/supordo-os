---
url: https://servicescompris.extrabat.com/les-bonnes-pratiques
url_finale: https://servicescompris.extrabat.com:443/les-bonnes-pratiques/
date_collecte: 2026-09-09
destination: centre_aide
---

# Catégorie :Les bonnes pratiques

## [Comment créer un tiers payant.](https://servicescompris.extrabat.com/comment-creer-un-tiers-payant/)

	
-Il vous faut demander en premier lieu à activer le module « Tiers payant » (via l’assistance d’Extrabat, cela est gratuit).

-Une fois ce parametrage effectué, il vous faut créer vos « tiers payant » ex « Prime CEE » depuis le   [puis la bulle](https://servicescompris.extrabat.com/content/uploads/sites/5/2013/07/plus.jpg)   [=> Fournisseurs.](https://servicescompris.extrabat.com/content/uploads/sites/5/2013/07/parametre.jpg)

Sur la fiche de ce fournisseur, vous aurez la possibilité de saisir les mentions légales et/ou le montant pris en charge par ce tiers-payant (afficher à l’impression).

Sur vos pièces commerciales, vous pouvez maintenant »‘ajouter un tiers payant ».


Vous avez 2 possibilités, sortir l’impression destinée à votre client et également le document destiné à votre tiers payant.




## [Je veux envoyer des mails à partir d’Extrabat mais avec ma boîte mail](https://servicescompris.extrabat.com/je-veux-envoyer-des-mails-a-partir-dextrabat-mais-avec-ma-boite-mail/)

	
Si vous ne désirez plus envoyer vos mails à partir du serveur d’Extrabat mais à partir de votre adresse mail professionnelle **(sauf les mails en @orange.fr ou @orange.com voir plus bas)**


vous retrouvez dans vos paramètres (Outils et Paramètres) [un menu Configurateur SMTP](https://www.myextrabat.com/parametres/configuration_smtp/ajouter) :

- Choisir un utilisateur (le votre par exemple)
- Choisir un des choix du menu déroulant.
- Remplir les champs demandés et effectuer un test de délivrabilité
- [https://www.myextrabat.com/parametres/coordonnees/mode_email](https://www.myextrabat.com/parametres/coordonnees/mode_email) (et activer la dernière option)

PS : Bien effectuer le test de délivrabilité

Si toutefois vous avez une adresse en @nomDeVotreEntreprise.com alors il faudra faire la demande de ces informations à votre technicien informatique.

Vous trouverez ci dessous le mail type que vous pouvez leur envoyer :

*Bonjour,* 

*Je souhaite configurer l’envoi de mail via le SMTP de mon nom de domaine.*

*Il me faudrait les informations suivante :*
*– Adresse du serveur SMTP (ssl ou tls)*
*– Numéro du port du serveur SMTP*


**Pour les mails en orange :** Nous vous conseillons vivement de prendre contact avec un prestataire informatique pour qu »il vous fasse une boite mail professionnelle afin d’envoyer les mails à partir d’extrabat. Cela n’aura aucun impact sur votre mail actuel puisque tout sera redirigé dessus.

**Pour les mails sur  Google (Gmail)** cliquez sur le lien 

[ici](https://servicescompris.extrabat.com/parametrer-son-smtp-extrabat-avec-son-compte-gmail/)

**Pour les mails sur  Yahoo** Si vous l’avez fait sous Yahoo par exemple, cliquez sur le lien 

[ici](https://serversmtp.com/fr/serveur-smtp-yahoo/)

## [Comment paramétrer un nouveau logiciel de comptabilité dans Extrabat](https://servicescompris.extrabat.com/comment-parametrer-un-nouveau-logiciel-de-comptabilite-dans-extrabat/)

	
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


## [A lire et à méditer par la suite](https://servicescompris.extrabat.com/lire-mediter-par-la-suite/)

	
Ci-joint un dossier Stratégie du magazine Actu-piscine à dévorer à tête reposé.

Bonne réflexion.

## [Le temps c’est de l’argent](https://servicescompris.extrabat.com/le-temps-cest-de-largent/)

	
Article intéressant qui donne à réfléchir et qui vous permet de repenser  votre organisation [***Pisciniers, et si vous abandonniez le fax***](http://www.actu-piscine.fr/dossiers.php?Action=Article&Id=457#xtor=EPR-1-[Magazine-201403]-20140327) – Source Actu-piscine du 04/04/2014

## [Préparez votre offre Chauffage](https://servicescompris.extrabat.com/preparez-votre-offre-chauffage/)

	
A découvrir les chiffres du chauffage de piscine en France en 2013 en cliquant [ici](http://www.actu-piscine.fr/dossiers.php?Action=Article&Id=453#xtor=EPR-1-[Magazine-201402]-20140220http://) (source Actu piscine).

Au delà des chiffres qui couronnent la pompe à chaleur, vous vous devez d’être prêt pour la saison à savoir

1. des mailings prêts à partir dès que le beau temps sortira le bout de son nez,
2. Envoyez-les la veille d’un week-end, vos clients seront détendus et pourront se projeter dans une eau chaude à 30° en famille,
3. Une offre complète (hydraulique, électricité, socle) sans concurrence possible d’internet,
4. Un délai le plus court possible,
5. Une offre de crédit ou une facilité de paiement.

Bref, un travail de professionnel.

## [La gestion du changement](https://servicescompris.extrabat.com/la-gestion-du-changement/)

	
Comment l’anticiper, comment la prévoir et comment la mettre en place ?

Je vous entends déjà ! Pourquoi changer ? Tout va bien chez moi ! La crise ? Même pas peur…

Des évidences :

- Le métier a changé,
- Les produits ont changé,
- Les clients ont changé,
- Les mentalités ont changé,
- En bref, un monde en mouvement.


Votre objectif :

- Des objectifs simples, compréhensibles et faciles à mettre en œuvre,
- Écrivez ce que vous voulez faire,
- N’éludez pas les problèmes,
- Un principe Gagnant-Gagnant,
- Ne vous laissez pas attendrir par « Mais on l’a déjà fait avant et cela n’a pas marché »
- Prenez le temps de la réflexion et innovez,
- Prenez le parti d’avoir une évolution permanente et continue.

Quelques liens à consulter :

## [Rassurez vos clients en cours de construction](https://servicescompris.extrabat.com/rassurez-vos-clients-en-cours-de-construction/)

	
Il est primordial de rassurer vos clients en ces temps de misère météorologique.

Il vous faut anticiper le stress de vos clients en les rassurant sur votre capacité à gérer son chantier, son inquiétude par rapport à la solidité de son ouvrage, son souci de bonne finition et son délai.

Profitez en à travers une visite chantier, un envoi d’un message que vous comprenez son inquiétude et que vous êtes bien l’homme de la situation qu’il a choisi lors de l’acte commercial.

Profitez en aussi pour faire un nouveau point sur les délais de mise à disposition afin qu’il comprenne que le temps perdu n’est pas rattrapable et que vous ferez le maximum.

Finalement, peu importe le moyen mais COMMUNIQUEZ!!



## [L’organisation c’est maintenant.](https://servicescompris.extrabat.com/lorganisation-cest-maintenant/)

	
L’ORGANISATION C’EST MAINTENANT.

Gagnez en organisation, en fluidité, en satisfaction client.

Pourquoi avoir à ce jour plusieurs outils d’organisation ( excel, Google agenda, logiciel de gestion commerciale, planning, etc..) alors que tous ses éléments peuvent être réunis dans :

– un seul logiciel

– tout le monde travaille avec le même outil,

– plus de perte d’informations,

– des dossiers clients mis à jour en temps réel,

– une efficacité retrouvée,

– un accès nomade via les tablettes et smartphones,

– un fichier mis à jour prêt à être rentabiliser grâce à un logiciel d’emailing intégré,

– une valorisation certaine de votre entreprise.

Pourquoi ne pas programmer et préparer toutes les campagnes de promotions, d’emailing que vous allez envoyer à vos clients en Mars, Avril, Mai, etc..

Pourquoi ne pas pré planifier toutes les remises en route ( souvent lié à vos mises en hivernage), ce qui vous permettra d’anticiper un trop plein de travail et d’y trouver une solution en Février plutôt qu’en urgence au dernier moment et à quel prix,

Pourquoi ne pas mettre son planning de chantier dans l’ordre et d’analyser si vos équipes vont supporter la charge de travail au printemps et au besoin prévoir du personnel supplémentaire,

Pourquoi ne pas prévoir une demi-journée par semaine pour les urgences.

Pourquoi ne pas faire une réunion sur le thème : Que peut-on améliorer pour 2014 ?

Les professionnels de la piscine sont des professionnels complets et souvent autodidacte mais l’organisation d’une entreprise a des règles que l’on peut ignorer et qu’il ne vaut mieux pas ignorer au risque de se retrouver avec des structures fragilisées économiquement.

Alors, le changement c’est maintenant.

## [Mieux gérer ses emails professionnels](https://servicescompris.extrabat.com/mieux-gerer-ses-emails-professionnels/)

	
L’envoi de mail est devenu l’outil de communication principal dans le milieu professionnel. Il permet d’échanger, envoyer des fichiers, organiser des réunions, fixer des rendez-vous… Mais tout comme un bureau désordonné, une messagerie mal gérée peut vite devenir un casse tête et une source de stress. D’après une étude publiée en 2012 par l’éditeur de solutions logicielles Mindjet, 68 % des collaborateurs reçoivent jusqu’à 100 e-mails par jour, la sollicitation est incessante d’où l’intérêt de savoir gérer ses priorités. Voici donc quelques conseils pour optimiser votre temps face au caractère chronophage des messageries, pour ne pas perdre votre énergie en recherchant un ancien message ou dans la rédaction d’un mail.

 **Trier ses mails**

> Le matin est en général le moment propice pour traiter vos mails puisqu’il demande une bonne concentration. Vous pouvez vous fixer un temps à ne pas dépasser dans le traitement de votre courriel ; 45 minutes par jour par exemple.

> Classez vos mails dès leur arrivée pour ne pas encombrer votre messagerie. Pour cela, créez des dossiers en fonction des projets, de votre destinataire : clients, fournisseurs, prospects… à personnaliser selon votre activité. Dans les paramètres de votre messagerie électronique (sur Outlook dans « outils » > « règles de message »), vous pouvez également choisir de classer automatiquement un mail dès son arrivée en fonction de l’expéditeur ou de l’objet. Le mail se rangera directement dans le dossier qui lui est attitré.

 **Gérer l’urgence**

Hiérarchisez le degré d’urgence de vos mails à l’aide des drapeaux ou étoiles (suivant le type de messagerie électronique) prévus à cet effet. Vous pouvez aussi créer des dossiers « Urgents », « A traiter » et placez les mails concernés à l’intérieur.

 **Gérer ses contacts**

Votre messagerie est un vivier de contacts constituant une réelle base de données. Prenez le temps de mettre à jour votre répertoire en remplissant et enregistrant correctement chaque fiche de vos interlocuteurs (nom, prénom, fonction, numéro de téléphone…). Pour plus de praticité, vous pouvez même synchroniser par la suite votre carnet d’adresse avec votre smartphone.

 **Rédiger ses mails**

La rédaction de mails professionnels requiert un réel savoir-faire !

> Tout d’abord, employez un style direct dans vos réponses pour gagner du temps.

> Utilisez le correcteur d’orthographe de la messagerie. Il n’est pas fiable à 100% néanmoins il vous évitera d’envoyer un mail avec des fautes de frappes.

> Créez votre signature automatique pour éviter de la réécrire dans chaque mail, ce qui constituerait une grosse perte de temps.

> Écrivez un titre clair et concis dans l’objet de vos mails, en relation directe avec leur contenu. Cela vous permettra de retrouver vos messages plus facilement, quand vous lancerez une recherche par exemple.

 **Désactiver la notification automatique des messages qui arrivent** (la fameuse fenêtre pop up qui s’ouvre à chaque nouvel e-mail) et les alertes sonores afin de ne plus être perturbé car la perte de concentration est réelle : presque 64 secondes pour reprendre le fil de sa pensée après avoir été dérangé par le pop up.

 **Dernier conseil**… Préférez le face à face lorsque l’occasion s’y prête afin de privilégier les échanges physiques et entretenir votre réseau, impératif pour votre activité de consultant/formateur autonome.

## [Votre fichier client, source de votre business](https://servicescompris.extrabat.com/votre-fichier-client-source-de-votre-business/)

	
Tout le monde est d’accord afin de décréter que la fidélisation de votre fichier client est la clé de succès de votre entreprise.Elle vous génère des revenus réguliers, pérennise votre entreprise et vous permet de réfléchir à votre stratégie sereinement.

Tout le monde est d’accord aussi pour dire que 2/3 des devis accessoires (pompe à chaleur, couverture été, traitement de l’eau, volet roulant, robot automatique, domotique, etc..) se réalisent entre Mars/Avril jusqu’à Juin/Juillet.

On est aussi d’accord pour dire que pendant cette période, il faudrait le double de personnel afin de concrétiser rapidement et efficacement ses devis en commandes.

Nous avons fait un test l’été dernier sur une cinquantaine de magasins afin de connaître le montant des devis qui n’étaient pas relancés et les montants totaux oscillaient entre 120 K€ et 290 K€.

Face à ce constat :

1) nous avons mis en place un envoi d’offre promotionnelles rattachés à vos devis avec un système de relance automatique avec numéros du client afin que vous puissiez suivre et gérer vos devis,

2) nous avons intégré dans votre base articles une notion de fin de vie (par exemple, une couverture été a une durée de vie de 48 mois, le changement d’une charge filtrante de 60 mois, etc..) et lorsque celle-ci arrive à terme, un tableau de bord vous le rappelle avec la proposition d’un envoi d’une offre personnalisé,

3) nous avons intégré un logiciel d’emailing qui vous permet aussi bien d’envoyer des invitations à vos prospects que des offres commerciales à vos clients équipés d’accessoires avec un historique des clients qui ont cliqué sur le mail.

Ces outils sont à votre disposition et doivent être préparés pour la saison à venir afin que vous puissiez travailler par anticipation plutôt que par réaction.

Avec toute notre considération.

L’équipe Extrabat Piscines.