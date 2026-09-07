---
url: https://documentation.openfire.fr/knowsystem/mise-en-place-de-la-signature-electronique-261
url_finale: https://documentation.openfire.fr/knowsystem/mise-en-place-de-la-signature-electronique-261
date_collecte: 2026-09-06
destination: documentation_2
---

La signature électronique sur OpenFire permet aux clients de signer électroniquement des documents en utilisant leur propre signature électronique, plutôt que de devoir imprimer, signer manuellement et numériser le document pour le renvoyer.

Cette fonctionnalité est utile pour faire signer fréquemment des contrats, des devis, des bons de commande, etc.

La signature électronique sur OpenFire garantit que les documents signés sont authentiques et intègres, et permet d'économiser du temps et de l'argent en éliminant la nécessité de traiter des documents papier.

La signature électronique peut être facilement vérifiée pour garantir son authenticité.

## Mise en place de la signature électronique

La mise en place de la signature électronique nécessite un certains nombre de paramétrages et l'ajout d'un module spécifique.

*Aussi, pour toute demande d'ajout de cette fonctionnalité, vous pouvez contacter le support OpenFire par mail à l'adresse support@openfire.fr ou par téléphone au 02.30.96.02.65.*

## Faire signer électroniquement en présence du client

Plusieurs remarques :

- Les paramètres par défaut du modèle de requête peuvent être modifiés à chaud directement dans la requête en cours ;

- Il est possible d’ajouter d’autres documents via Documents à signer ;

- L’ensemble des documents à signer peuvent être téléchargés ;

- Le prénom des signataires est obligatoire ;

- Un mobile doit être défini pour l’ensemble des signataires.

Cet onglet reprend l’historique associé à la procédure de signature en cours. Il est nécessairement vide tant qu’aucune signature n’a été réalisée :

Cet onglet permet de consulter l’ensemble des documents à signer par le client :

## Faire signer électroniquement le client à distance

La procédure est la même que présentée ci-dessus, au détail prêt que la procédure n’est pas initiée depuis le devis en back-office mais depuis un bouton d’action depuis un email envoyé au client (cf. Signer en direct) :

a) Cliquer sur Accéder au devis

b) Ouvre une fenêtre dans le navigateur permettant de faire défiler les documents à signer.

c) Cliquer sur le bouton signer -> envoi un SMS avec le code de confirmation au client.

d) Il est nécessaire de faire défiler le document puis de saisir le code SMS reçu par le client pour valider la signature.

e) Il lui faut ensuite VALIDER son opération de signature. Une fois les documents signés, ils peuvent être téléchargés depuis la fenêtre de signature, depuis l’onglet infos. Les signatures sont apposées en fin de documents (pour le devis). A noter, pour les documents PDF ajoutés à la procédure de signature : une page blanche est générée à la suite du document pour recevoir la signature électronique et indiquer le nom du document ainsi que le nombre de page du document signé.

L’ensemble de ces documents sont également paraphés.

Les documents sont ensuite insérés en PJ dans la commande (si le dernier signataire a bien cliqué sur le bouton VALIDER à la fin de sa procédure).

## Gérer et suivre les signatures électroniques en cours

Vous pouvez suivre l'ensemble des différentes requêtes envoyées depuis la commande via le smart-bouton Requêtes YouSign disponible à droite :

Elles peuvent être également consultées depuis le menu de la configuration dédié pour les personnes ayant les droits associés **Ventes > Configuration > Yousign > Requête de signature.**

Depuis le menu des devis ou des commandes, des filtres de recherches sont également proposés pour retrouver l’ensemble des devis pour lesquels :

- Une procédure de signature est en cours → filtre Demande de signature envoyée
- La signature électronique est terminée → filtre Devis signés