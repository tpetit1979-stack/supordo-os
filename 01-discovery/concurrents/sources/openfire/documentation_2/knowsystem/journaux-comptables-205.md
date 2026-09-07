---
url: https://documentation.openfire.fr/knowsystem/journaux-comptables-205
url_finale: https://documentation.openfire.fr/knowsystem/journaux-comptables-205
date_collecte: 2026-09-06
destination: documentation_2
---

Les journaux comptables jouent un rôle essentiel dans la gestion financière d'une entreprise, en enregistrant de façon chronologique et continue, toutes les opérations financières effectuées par une entreprise au cours d’un exercice comptable.

Généralement, les entreprises ont plusieurs journaux afin de classifier les opérations par nature.

## Configuration des journaux bancaires

Avant de commencer à utiliser les journaux bancaires dans OpenFire, il est important de les créer et configurer correctement.

Pour créer un journal comptable, rendez-vous dans le menu Comptabilité > Configuration > Journaux :

A la création, différents champs sont à renseigner:

- Nom : Il est important de choisir un nom de journal clair et qui décrit clairement son objectif. Par exemple, "Journal principal", "Journal des ventes", "Journal des dépenses", etc...

- Type : Sélectionnez le type de compte approprié pour votre journal en fonction de son objectif. OpenFire prend en charge différents types de comptes tels que les comptes bancaires, les comptes clients, les comptes fournisseurs, etc...

Assurez-vous de choisir le type de compte correspondant à votre journal afin d'aligner correctement les transactions financières. Les journaux suivants sont préconisés : 

| **Nom du Journal** | **Type** | 
| Vente | Vente | 
| Achats d'exploitation | Achats | 
| Achats Généraux | Achats | 
| Opérations Diverses | Divers | 
| Banque | Banque | 
| Paiement client | Banque | 
| Stock | Divers | 
| Caisse | Liquidités | 

A Savoir : Il est judicieux de séparer les Achats Exploitation et les Achats Généraux :

  - Les Achats Exploitation sont alimentés automatiquement par les achats.
  - Les Achats Généraux sont saisis manuellement.

- Code : Le code doit être un unique. Pour un journal de banque nous les définissons généralement de la forme *BNK* suivi d'un chiffre.
Attention : Une fois que des écritures sont saisies dans un journal, le code du journal ne peut plus être modifié !
- Séquence d’écriture : séquence de numérotations des écritures de ce journal

- Séquence dédiée aux avoir : si cochée, une séquence propre aux avoirs de ce journal sera créée. Pour ce journal donc, deux séquences de numérotations différentes seront donc utilisées : Une séquence pour les avoir et une séquence pour les factures.

- Définissez les comptes de débit et de crédit à utiliser par défaut sur ce journal et enregistrez. Déterminez les comptes de contrepartie appropriés pour les transactions dans le journal. Choisissez les comptes appropriés en fonction du type d'opération et assurez-vous qu'ils correspondent à la logique comptable de votre entreprise.
- Onglet Paramètres avancés :

Détail des champs :

- Types de compte autorisés : moyen de contrôle des écritures par sélection des types de compte autorisés pour ce journal ;
- Comptes autorisés : moyen de contrôle des écritures par sélection des comptes autorisés pour ce journal ;
- Grouper les lignes de facture : fonction autorisant le groupement des écritures comptables générées à l’intérieur d’une même pièce comptable ; le regroupement peut se faire par compte comptable ou par article.
- Montrer le journal dans le tableau de bord : affichage du journal dans le tableau de bord comptabilité.

Pour les journaux de type « Banque », l’onglet « compte bancaire » est ajouté. Voir la section « Compte Bancaire ».

 **Attention:** Avant de finaliser la configuration du journal, assurez-vous de valider et de vérifier les paramètres. Vérifiez que toutes les informations sont correctement saisies et que les paramètres sont cohérents avec les pratiques comptables de votre entreprise.

## Séquence des journaux


            Les séquences permettent de définir une méthode de numérotation des pièces à l’intérieur d’un journal. Dans OpenFire, l’intégralité des pièces générées sont séquencées.

 *Plus d'informations sur [les séquences de journaux](https://documentation.openfire.fr/knowsystem/sequences-des-journaux-278)*

## Rapports et analyses

OpenFire offre des fonctionnalités de reporting et d'analyse avancées pour les journaux bancaires.

Depuis le menu Comptabilité > Rapports, vous pouvez éditer un rapport au format PDF comprenant les écritures des journaux de vente et/ou d'achats

Ce rapport peut être trié par date ou par numéro d'écritures:

Il est également possible d'extraire le journal des ventes depuis le menu Comptabilité > Rapports > FEC :

Dans la fenêtre suivante, remplissez alors les champs comme tels :

- Start Date : date de début de période
- End Date : date de fin de période
- Export Type : Non-officiel
- Extension du fichier : csv ou txt (dépendant du besoin de votre comptable)
- Vous pouvez désélectionner l’option inclure le journal d’ouverture afin de ne pas faire apparaitre les à-nouveaux
- Journaux : sélectionner le journal de votre choix, et supprimer les autres

En cliquant sur Generate, le fichier sera créé et il est téléchargeable, afin d'être consultable via le logiciel de votre choix.