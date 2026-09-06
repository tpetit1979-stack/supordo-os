---
source: https://support.openfire.fr/hc/fr/articles/24649180504604-Configurer-les-pr%C3%A9l%C3%A8vements-SEPA
categorie: Configurer OpenFire
titre: Configurer les prélèvements SEPA
date_recuperation: 2026-09-05
---

# Configurer les prélèvements SEPA

Cet article vous indique comment configurer les prélèvement SEPA dans OpenFire.

Cet article vous accompagne dans la configuration du prélèvement SEPA pour réaliser des ordres de paiement pour vos fournisseurs ou des ordres de prélèvement pour vos clients . Vous apprendrez à configurer votre identifiant créancier, à créer des mandats pour vos clients et à générer vos fichiers de prélèvement pour la banque.

Cet article contient les sections suivantes :

- **Prérequis et installation**
- **Configuration de l'entreprise**
  - L'Identifiant Créancier SEPA (ICS)
  - Paramétrage des méthodes de paiement (Client et Fournisseur)
- **Gestion des mandats clients**
  - Créer un mandat bancaire (RUM)
  - Associer le mandat au contact
  - Comprendre les séquences (OOFF, FRST, RCUR, FNAL)
- **Réaliser un ordre de prélèvement**
  - Sélectionner les factures et utiliser les filtres
  - Générer et confirmer le fichier bancaire
- **Bonnes pratiques, réconciliation et erreurs courantes**

## Prérequis

  💡**Remarque** : Vous n'avez pas la main pour la mise en place de ces prérequis.
  Si vous constatez qu'il vous manque une fonctionnalité ou qu'une configuration
  citée ci-dessous est à modifier, merci de contacter notre support client.

Voici les prérequis pour bénéficier des fonctionnalités de prélèvement SEPA dans votre environnement OpenFire.

🧩**Modules **:

- **Account Banking PAIN Base Module*** (`account_banking_pain_base`) : socle technique pour les modules suivants : 
  - **Account Banking SEPA Credit Transfer*** (`account_banking_sepa_credit_transfer`) : pour les ordres de virement (prélèvements fournisseurs).
  - **Account Banking SEPA Direct Debit*** (`account_banking_sepa_direct_debit`) : pour les ordres de prélèvement (prélèvements  clients).
- **Account Banking Mandate*** (`account_banking_mandate`) : pour la gestion des mandats. En optionnel, il est possible d'ajouter : 
  - **Account Banking Mandate Contact** (`account_banking_mandate_contact`) : permet de sélectionner un mandat bancaire spécifique (et donc un compte bancaire spécifique) au niveau du contact, afin que lors d'un prélèvement automatique, ce mandat soit utilisé pour les factures émises à ce contact.
  - **Account Banking Mandate Sale** (`account_banking_mandate_sale`) : ajoute le champ « Mandat de prélèvement automatique » aux commandes de vente.
  - **Account Banking Mandate Sale Contact** (`account_banking_mandate_sale_contact`) : permet d'ajouter un mandat de contact spécifique aux ordres de vente.
  - **Contract Mandate** (A venir) (`contract_mandate`) : permet de définir un mode de mandat sur le contrat pour la création des factures avec ce mandat.

## L'Identifiant Créancier SEPA (ICS)

L'**Identifiant Créancier SEPA (ICS)** est un code unique attribué à une entreprise ou organisation qui lui permet de prélever des fonds sur les comptes bancaires de ses clients dans la zone SEPA (prélèvement automatique).

**Format** : FR + 2 chiffres de contrôle + 3 caractères nationaux + identifiant national (ex: FR12ZZZ123456)

**Usage** : Obligatoire pour émettre des mandats de prélèvement SEPA. Il identifie de manière certaine le créancier auprès des banques et des débiteurs.

**Obtention** : Délivré par votre banque sur demande, gratuit en France.

`Chemin d'accès : Paramètres > Comptabilité > SEPA/PAIN.`

1. Saisir votre code **Identifiant créancier SEPA** de votre société
2. **Enregistrer** les modifications.

| 🚨**Avertissement** : l'ICS est à configurer pour chaque société de la base. |
| --- |

## Paramétrage de la méthode de paiement

`Chemin d'accès : Comptabilité > Configuration > Gestion > Méthodes de paiement.`

Par défaut, il existe deux méthodes de paiement déjà configurées, une méthode de paiement pour :

- Une pour la gestion des "**Virement SEPA aux fournisseurs**"
- Une pour la gestion des "**Prélèvement SEPA clients**"

Pour chacun d'entre eux, on y retrouve :

- Le **nom** de la méthode de paiement
- Le **code** de la méthode de paiement (NE PAS MODIFIER)
- Le **type de paiement** ("sortant" pour les "virements aux fournisseurs" et "entrant" pour les "prélèvements SEPA clients"
- La version Pain utilisée, il est recommandé de laisser les valeurs par défaut : 
  - **pain.008.001.02 **pour les prélèvements SEPA Clients.
  - **pain.001.001.03** pour les virements fournisseurs.
- **Convertir en ASCII** : Permet de convertir les caractères accentué, ce qui est recommandé pour la génération du fichier PAIN.
- **Warn if not SEPA** : Permet d'avoir une alerte lorsque la méthode de paiement SEPA est utilisé avec un partenaire ou des coordonnées bancaires non conformes au SEPA : 
  - IBAN non SEPA (hors zone SEPA)
  - BIC manquant ou invalide
  - Pays du partenaire non SEPA
- **Compte bancaire requis** : Activez cette option si ce mode de paiement exige que vous connaissiez le numéro de compte bancaire de votre client ou fournisseur.
- **Mandat requis** : Pour les méthodes de paiement "Entrant" (Prélèvement SEPA Clients), activez cette option si cette méthode de paiement nécessite que votre client signe un mandat de prélèvement pour votre société.
- **Uniquement pour les ordres de paiement** : Activez cette option si vous souhaitez imposer l'utilisation d'ordres de paiement pour cette méthode de paiement.

## Paramétrage du mode de paiement spécifique

`Chemin d'accès : Comptabilité > Configuration > Gestion > Modes de paiement spécifiques.`

Contrairement aux modes de paiement classiques qui se configurent au niveau des journaux, les modes de paiement pour le SEPA se configure dans le menu des modes de paiement spécifiques.

Il est nécessaire de créer un mode de paiement par type en cliquant sur "Nouveau" en haut à gauche de l'écran :

- Prélèvement SEPA clients
- Virement SEPA aux fournisseurs

Voici la configuration à indiquer pour chacun d'entre eux :

### A. Prélèvement SEPA clients

- **Nom **: Libellé du mode de paiement : "Prélèvement SEPA clients" par exemple.
- **Société **(en multi société uniquement) : Société où le mode de paiement est utilisable
- **Méthode de paiement** : sélectionner la méthode de paiement correspondante à ce mode de paiement : "Prélèvement SEPA clients"
- **Type de paiement** : rempli automatiquement par “Entrant” ou “Sortant” en fonction de la configuration de la méthode de paiement choisie au champ ci-dessus.
- **Sélectionnable dans les ordres de paiement** : cocher la case si vous souhaitez que l’on puisse faire un ordre de paiement avec ce mode de paiement.
- **Lien vers le compte de banque** : 
  - Pour les modes de paiement qui sont toujours rattachés au même compte bancaire de votre entreprise ou si votre entreprise n'a qu'un seul compte bancaire (comme le virement des clients ou le prélèvement SEPA des fournisseurs), sélectionnez “Fixe”. 
    - Si vous avez sélectionné la valeur “Fixe”, le champ “**Journal bancaire fixe**” apparaît, vous devez alors préciser le journal à utiliser pour ce mode de paiement.
  - Pour les modes de paiement qui ne sont pas toujours rattachés au même compte bancaire (comme le prélèvement SEPA pour les clients, le virement bancaire pour les fournisseurs), sélectionnez “Variable”, ce qui signifie que vous choisirez le compte bancaire sur l'ordre de paiement.
    - Si vous avez sélectionné la valeur “Variable”, le champ “**Journaux de banque autorisés**” apparaît, ce qui vous permet de préciser quels journaux de banques sont autorisés pour ce mode de paiement. Si vide, il sera possible de sélectionner des comptes bancaires de l’ensemble de vos journaux de banque.
- **Mode de paiement pour les remboursements** : Sélectionnez le mode de paiement qui sera utilisé pour les remboursements provenant du mode de paiement actuel.
- **Transfer journal on payment/debit orders** : ??

**Section “Options pour les ordres de paiement”**

***Note **: cette section est disponible uniquement si vous avez autorisé les ordres de paiement sur ce mode de paiement)*

- **Interdire le prélèvement avant la date d’échéance** *(disponible uniquement si vous avez choisi une méthode de paiement “Entrant”* : Si vous activez cette option, un message d’erreur s'affiche lorsque vous confirmez un ordre de prélèvement comportant une ligne de paiement dont la date de paiement est antérieure à la date d’échéance.
- **Date d’exécution du paiement par défaut** : sélectionnez la date d'exécution du paiement par défaut entre 
  - Vide :
  - Immédiatement :
  - Date d’échéance :
  - Date fixe :
- **Grouper les opérations des ordres de paiement** : Si coché, les lignes de transaction de l’ordre de paiement seront groupées lors de la confirmation de l’ordre de paiement. Le regroupement ne sera effectué que si 
  - les champs suivants ont les mêmes valeurs : “Partenaire”, “Devise”, “Compte bancaire de destination”, “Date de paiement”
  - le “Type de communication” est “Libre” (d’autres modules peuvent définir des champs supplémentaires pour restreindre le regroupement).

**Section “Sélectionner les lignes d’écritures à payer - valeur par défaut”**

***Note **: cette section est disponible uniquement si vous avez autorisé les ordres de paiement sur ce mode de paiement)*

Cette section permet de sélectionner les valeurs par défaut lorsque l’on veut “Créer les lignes de paiement à partir de la pièce comptable” depuis un ordre de prélèvement

![](https://support.openfire.fr/hc/article_attachments/24671422580124)

- **Filtre sur les journaux** : sélectionner sur quel(s) journal(aux) il faut prendre les lignes d’écritures à payer.
- **Mode de paiement sur la facture** : sélectionner quel mode de paiement à utiliser pour la facture entre : 
  - Vide :
  - Identique :
  - Identique ou vide :
  - Tout :
- **Mouvements cibles** : Choisissez si vous souhaitez sélectionner : 
  - Toutes les écritures passées
  - Toutes les écritures
- **Lié à une facture ou à un avoir**
- **Type du filtre sur la date** : choisissez si vous souhaitez que le filtre sur la date se fasse sur : 
  - date d’échéance
  - date d’écriture

**Section “Options des écritures comptables groupées”**

- **Générer des écritures comptables groupées lors du téléversement d’un fichier** : cochez la case si vous souhaitez générer des écritures comptables groupées lors du téléversement d’un fichier
- **Comptabiliser les écritures** : cochez la case si vous souhaitez comptabiliser les écritures de l’ordre de prélèvement.

**Section “Afficher le compte bancaire dans la facture”**

- **Afficher le compte bancaire** : Permet de définir si et comment vous souhaitez imprimer le compte bancaire du client sur la facture, avec comme option : 
  - "Complet" : affiche l'ensemble du numéro du compte bancaire
  - "les n premiers caractères" : affiche les premiers numéros du compte bancaire
    - indiquer le nombre dans le champ **# de caractères**
  - "les n derniers caractères" : affiche les derniers numéros du compte bancaire
    - indiquer le nombre dans le champ **# de caractères**
  - "Non" ou "vide" : N'imprime pas le compte bancaire du client sur la facture.
- **Compte bancaire des journaux** : Permet de de définir si vous souhaitez imprimer le compte bancaire de votre journal sur la facture.

**Section “Note”**

Permet de renseigner une note sur ce mode de paiement.

### B. Virement SEPA aux fournisseurs

## Configuration des comptes bancaires de l'entreprise

Pour chaque compte bancaire de l'entreprise, un journal de banque doit être créé.

Pour chaque compte bancaire concerné par les opérations SEPA (prélèvement ou règlement), il faut venir saisir l'IBAN dans le journal associé :

![](https://support.openfire.fr/hc/article_attachments/24959700324892)

## Gestion des mandats clients

`Chemin d'accès : Comptabilité > Client > Mandats bancaires`

Il faut un groupe de droit particulier pour accéder aux mandats bancaires.

Le mandat est l'autorisation officielle que votre client vous donne pour prélever sur son compte.

  🚨Note : Avant de créer le mandat, assurez-vous d'avoir bien renseigné le compte
  bancaire (IBAN/BIC) sur la fiche du **Contact** au niveau de l'onglet
  **Facturation**.

  **📓**Pour aller plus loin →
  [Créer un compte bancaire](https://support.openfire.fr/hc/fr/articles/19096272928796)

Pour ajouter un mandat bancaire, cliquer sur Nouveau en haut à gauche puis compléter les informations suivantes :

- **Libellé **: Laisser le champ vide car il sera généré automatiquement avec une référence unique (ex: BM0001). Cette référence correspond à la **RUM** (Référence Unique de Mandat).
- **Format** : sélectionner "Mandat SEPA".
- **Type **: indique le type de prélèvement que vous souhaitez faire : 
  - "Mandat générique" : Ne permet pas de faire des prélèvement SEPA, ne pas utiliser.
  - "Récurrent" : pour faire des prélèvement récurrent, va de paire avec la valeur "RCUR" dans le type de séquence.
  - "One-off" : pour faire un prélèvement unique, va de paire avec la valeur "OOFF" dans le type de séquence.
- **Compte bancaire** : Sélectionner le compte bancaire de votre client
- **Partenaire **: Champ qui est renseigné automatiquement avec le contact lié au compte bancaire sélectionné
- Choisir la **Structure** :
  - **Basique (Core)** : pour un client particulier (B2C). C'est le modèle le plus courant.
    - **Pour qui ?** Utilisable pour tous vos clients (particuliers, professions libérales, ou entreprises).
    - **Droit au remboursement :** Votre client a le droit de contester un prélèvement et d'être remboursé **sans justification** pendant **8 semaines** après le débit (et jusqu'à 13 mois en cas d'absence de mandat valide).
    - **Mise en place :** Très simple. Le client signe le mandat et vous le renvoie. Il n'a aucune démarche à faire auprès de sa banque.
  - **Entreprise (B2B)** : Ce format est exclusivement réservé aux transactions entre deux entités professionnelles.
    - **Pour qui ?** Uniquement si votre client est une entreprise ou une administration (pas de particuliers).
    - **Droit au remboursement :** C'est son grand avantage. Une fois le prélèvement effectué, **votre client ne peut plus le contester** (sauf en cas de fraude avérée). Cela sécurise totalement votre encaissement.
    - **Mise en place :** Plus contraignante. Votre client doit signer le mandat, vous le renvoyer, **MAIS il doit aussi impérativement l'enregistrer auprès de sa propre banque**. Si sa banque n'a pas enregistré le mandat, elle rejettera systématiquement votre prélèvement.

Tableau comparatif rapide

| **Caractéristique** | **SEPA CORE** | **SEPA B2B** |
| --- | --- | --- |
| **Cible** | Tout public (B2C & B2B) | Professionnels uniquement |
| **Sécurité créancier** | Risque de rejet sous 8 semaines | Encaissement définitif |
| **Action du client** | Signature simple | Signature + enregistrement à sa banque |
| **Délai de traitement** | Standard | Souvent plus rapide (J-1) |

| 💡Le conseil de l'expert OpenFire  **Utilisez le mandat CORE** si vous voulez de la simplicité. C'est l'option la moins "bloquante" pour vos clients, car ils n'ont rien à demander à leur banquier. C'est idéal pour les petits contrats de maintenance. **Utilisez le mandat B2B** pour des montants importants ou si vous avez besoin d'une certitude totale de paiement. Assurez-vous simplement que votre client a bien fait la démarche auprès de sa banque, sinon votre flux de prélèvement sera rejeté au premier essai. |
| --- |

- Type de séquence pour le prochain prélèvement : définit comment le prélèvement est présenté à la banque avec comme valeurs possibles : 
  - **"OOFF (One-Off)"** : prélèvement ponctuel unique.
  - **"FRST (First)"** : premier prélèvement d'une série récurrente.
  - **"RCUR (Recurrent)"** : prélèvements suivants de la série.
  - **"FNAL (Final)"** : dernier prélèvement d'une série.

Note : certaines banques acceptent la valeur **RCUR** même pour un premier paiement. Nous recommandons néanmoins pour votre premier virement d'utiliser la valeur "First" et d'utiliser ensuite la valeur "Reccurent" pour les suivantes, et Final pour le dernier

En cas de reprise de données et que le prélèvement est déjà en cours pour ce client, il faut utiliser "Reccurent".

- **Date de signature** du mandat (et uploader le document dans le champ **Image du mandat**.

### Associer le mandat au contact

L'automatisation n'est pas totale : après avoir créé le mandat, vous devez confirmer son utilisation par défaut pour les factures.

1. Sur la fiche du **Contact**, onglet **Ventes & Achats**.
2. Dans le champ **Mode de paiement client**, choisir "Prélèvement SEPA".
3. Dans le champ **Contact Mandate**, sélectionner le mandat créé précédemment.

Méthodologie de validation d'un mandat SEPA :

1. Depuis la fiche client : créer un mandat SEPA
2. L'envoyer au client via email (une action dédiée existe depuis le mandat lui-même)
3. A réception du mandat signé de la part du client : 
  1. Retournez sur le mandat du client
  2. Mettre le mandat signé en PJ du mandat (facultatif)
  3. Validez le mandat

## 4. Réaliser un ordre de prélèvement

Une fois vos factures validées, vous pouvez préparer le fichier à envoyer à votre banque.

`Suivre le chemin d'accès suivant : Facturation > Clients > Ordre de prélèvement.`

### Sélectionner les factures

1. Cliquer sur **Créer**, puis sur le bouton **Créer les lignes de paiement à partir de la pièce comptable**.
2. Utilisez les filtres pour affiner la recherche :
  - **État** : sélectionnez "Toutes les écritures passées" pour ne prendre que les factures validées (posted).
  - **Autoriser les lignes en litige** : si décoché, le système ignore les factures marquées avec le champ "Aucun suivi" (en litige).
  - **Mode de paiement** : laissez sur "Identique" pour ne récupérer que les factures dont le mode de paiement correspond à celui de votre ordre.

### Générer et confirmer le fichier

1. Une fois les lignes ajoutées, cliquer sur **Confirmer le paiement**. Cela crée un paiement en brouillon.
2. Cliquer sur **Générer un fichier de paiement** pour télécharger le fichier `.xml`.
3. **Important** : Une fois le fichier déposé à la banque, cliquez sur le bouton **Fichier téléchargé**. Cette action comptabilise le paiement et passe automatiquement les factures liées à l'état **Payé **ou** En paiement **en fonction de la configuration de votre journal de banque pour le rapprochement bancaire

  **📓**Pour aller plus loin →
  [Configurez vos règles de rapprochement bancaire](hc/fr/articles/21587458617628)

## 5. Bonnes pratiques, réconciliation et erreurs courantes

- **Rapprochement bancaire** : Le processus OCA est totalement compatible avec la comptabilité standard. Lors de l'import de votre relevé bancaire, le système fera le lettrage entre le montant reçu et le "Paiement SEPA" généré. Comptablement, le résultat est identique à une déclaration de paiement manuelle sur facture.
- **Erreurs de format (Ex: Crédit Agricole)** : 🚨Avertissement : Certaines banques sont très strictes sur le formatage des données (ex: attente de 0/1 plutôt que Vrai/Faux). Si votre fichier est rejeté, contactez le support OpenFire pour vérifier la compatibilité du module avec votre établissement.
- **Automatisation des contrats** : Si vous gérez des contrats de maintenance via des Demandes d'Intervention (DI), assurez-vous que les factures générées héritent bien du mode de paiement "Prélèvement SEPA" défini sur le contact.
- **Signature électronique** : 💡Note : Il n'existe pas encore de module natif pour envoyer le mandat en signature automatique. Vous devez utiliser un outil tiers (type Yousign), puis importer le document signé dans OpenFire pour archivage.

📓Pour aller plus loin → [Importer et rapprocher ses relevés bancaires].

Mis a jour le : 14/08/2026
