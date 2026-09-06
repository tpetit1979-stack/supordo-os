---
source: https://support.openfire.fr/hc/fr/articles/24400423661596-Cr%C3%A9er-une-demande-de-prix-ou-une-commande-fournisseur
categorie: Utiliser OpenFire
titre: Créer une demande de prix ou une commande fournisseur
date_recuperation: 2026-09-05
---

# Créer une demande de prix ou une commande fournisseur

Cet article vous explique comment créer une demande de prix dans OpenFire. Vous y trouverez le détail de chaque champ pour assurer un suivi précis de vos commandes et de vos stocks.

## Sommaire

Cet article contient les sections suivantes :

- [**Chemin d'accès**](#h_01KEVMW21KND4SYFMV9R5WHYK7)
- [**Présentation d'une commande fournisseur**](#h_01KEW551PHW7HYQTJKQ4CYWKRB)

  - [**Identification de la commande**](#h_01KEW5541A597S9YT2YJ9KEP7K)
  - [**Dates et intervenants**](#h_01KEVMW21TQ8R43CDR32VR3QFG)
  - [**Logistique et facturation**](#h_01KEVMW21XVR8HJ7DK7BBF0ZYW)
  - [**Gestion des produits et lignes de commande**](#h_01KEVMW225C1H0EXXM31CZH0N1)
- [**Formats d'impression**](#h_01KEW59YWN42KY9G56TNMA6VVW)
- [**Méthodes de transmission **](#h_01KEW6D6Q8ZSKDVEQNFCCKT2SE)
- [**Règles d'approbation**](#h_01KEW59STT16A1CHXV5DNPEAVH)
- [**Bonnes pratiques**](#h_01KEW4EQJ0FSV5YZAYMYSTMJT3)

---

## Chemin d'accès

Pour retrouver la liste des demandes de prix, vous pouvez suivre le chemin d'accès suivant : Achat > Commandes > Demande de prix.

## Présentation d'une commande fournisseur

### Identification de la commande

Lors de la création d'une nouvelle demande, plusieurs champs permettent d'identifier précisément l'origine et le contexte de l'achat :

- **Vendeur (ou fournisseur)** : Sélectionnez le fournisseur auprès de qui la commande est passée.
- **Référence fournisseur** : Saisissez la référence de la commande propre au fournisseur pour faciliter les échanges et la traçabilité.
- **Référence de la commande** : Indiquez une référence textuelle libre.

| **🧑‍🏫Exemple** : si vous générez une commande de sous-traitance depuis une Demande d'Intervention (DI), ce champ reprendra automatiquement la référence de la DI. |
| --- |

- **Document source** : Ce champ indique le document à l'origine de l'approvisionnement. Il est généralement vide lors d'une création manuelle.

Selon l'origine de la commande, des liens directs peuvent apparaître pour consulter les documents liés :

- **La commande client associée** : Utile dans le cas d'un approvisionnement à la contremarque.
- **La demande d'intervention** : Utile dans le cas d'un approvisionnement pour de la sous-traitance.

### Dates et intervenants

La gestion des délais est essentielle pour la planification de vos chantiers :

- **Date limite de la commande** : La date limite à laquelle la demande de prix doit être convertie en commande ferme.
- **Arrivée prévue** : La date de livraison promise par le fournisseur. Cette date sera reprise sur le Bon de Réception (BR) associé.
- **Acheteur** : L'utilisateur responsable de la passation de la commande.
- **Responsable technique** : Le référent technique interne pour le suivi des articles commandés.

### Logistique et facturation

Ces paramètres déterminent comment la marchandise sera reçue et payée :

- **Délivrer à ?** : Choisissez la destination de la marchandise :

  - **Réceptions** ou **Retours** : Pour une livraison dans vos entrepôts.
  - **Livraison directe client** : Pour une livraison directe sur le site du client (drop shipping).

![](https://support.openfire.fr/hc/article_attachments/24801513811484)

- **Position fiscale** : Ce champ applique automatiquement le bon régime de TVA en fonction de la configuration de la fiche fournisseur.

| 💡**Note **: pensez à vérifier l'ensemble de vos fournisseurs pour confirmer la position fiscale définie pour chacun d'eux. |
| --- |

- **Méthode de facturation** : définit la façon (et avec quel contrôle) la facture fournisseur associée à la commande sera générée. Deux options sont possibles : 

  - **Sur la base des quantités commandées** : La facture fournisseur sera basée sur les quantités saisies initialement.
  - **Sur la base des quantités reçues** : La facture sera basée uniquement sur ce qui a été réellement réceptionné.
- **Conditions de paiements fournisseurs** : Définit l'échéance de règlement (ex: 30 jours), récupérée de la fiche fournisseur.

### Gestion des produits et des lignes de commande

Pour ajouter des articles à votre document :

1. Cliquer sur **Ajouter un produit**.
2. Sélectionner l'article souhaité.
3. Vérifier la **Description** : Elle reprend par défaut le libellé de l'article et la "Description des achats" renseignée sur la fiche produit.
4. Ajuster la **Quantité** et vérifier le **prix, **l'**UdM** (Unité de Mesure) ainsi que la **TVA**.

| 🚨**Avertissement** : Si vous ajoutez un produit qui n'est pas encore référencé chez ce fournisseur, OpenFire l'ajoutera automatiquement à la fiche article avec le prix unitaire de la ligne comme nouveau tarif de référence. |
| --- |

## Formats d'impression

OpenFire propose différents types de documents PDF selon vos besoins d'échange avec le fournisseur:

![](https://support.openfire.fr/hc/article_attachments/24809837797788)

- **La demande de prix** : Utilisée pour solliciter un tarif ou une disponibilité. Les quantités et les prix ne sont pas imprimés sur ce rapport.
- **Bon de Commande** : À utiliser lorsque la commande est ferme. Le document s'intitule "Commande fournisseur" et affiche les quantités ainsi que les prix.
- **Bon de Commande sans prix** : Variante permettant de passer commande même si vos tarifs ne sont pas à jour. Les prix ne figurent pas sur le document.
- **Commande sous-traitant** : Spécifique aux prestations de service. L'adresse d'intervention est automatiquement utilisée comme adresse de livraison.

## Méthodes de transmission

Pour transmettre votre document au fournisseur, plusieurs options s'offrent à vous:

1. Cliquer sur le bouton **Envoyer le bon de commande par email**.
2. Choisir un modèle d'email adapté.
3. Personnaliser si besoin le sujet ou le corps du message.

| 💡**Note **: l'option **Demande de confirmation** permet d'envoyer un e-mail automatique au fournisseur un certain nombre de jours avant la date d'arrivée prévue pour valider le délai. Cette option est à activer directement sur la fiche du fournisseur. |
| --- |

| 🚨**Avertissement** : Pensez à ajuster le type de rapport souhaité dans vos modèles d'email pour vous assurer de transmettre le bon fichier PDF (ex: demande de prix vs bon de commande). |
| --- |

| 💡**Note **: Pour certains **fournisseurs partenaires** d'OpenFire, une **option de transmission directe de votre commande par EDI est disponible**. N'hésitez pas à consulter la liste de ces connecteurs sur notre centre d'aide. |
| --- |

## Règles d'approbation

Selon la politique de votre entreprise, une validation par un manager peut être nécessaire avant de confirmer votre achat.

Ce paramètre est valorisé au global pour l'entreprise et est repris au niveau de chaque fournisseur.

![](https://support.openfire.fr/hc/article_attachments/24809193420828)

Les valeurs possibles :

- **Jamais** : Aucune approbation n'est requise.
- **Toujours** : La commande doit être systématiquement validée par un responsable.
- **Basé sur la politique de l'entreprise** : Une approbation est requise uniquement si la commande dépasse un montant seuil.

| **🧑‍🏫Exemple** : Un montant minimum de **5 000,00 €** peut être configuré dans les paramètres généraux, et repris pour le fournisseur. Toute demande de prix générée pour un montant dépassant ce seuil nécessitera la validation d'un personne ayant le niveau de droit achat > administrateur (=manager) |
| --- |

A la validation de la demande de prix, si une approbation est requise, la commande passe au statut "**A approuver**" :

![](https://support.openfire.fr/hc/article_attachments/24809193421596)

## Bonnes pratiques

Pensez à vérifier vos **fiches fournisseurs **avant de créer vos premières demandes de prix, notamment les aspects **Position Fiscale** et **niveau d'approbation**.

Avant de cliquer sur **Confirmer la commande**, vérifiez toujours les points suivants:

- Les **quantités** commandées.
- Les **prix unitaires** selon la confirmation du fournisseur (essentiels pour la valorisation de vos stocks et l'analyse de vos marges).
- La **date prévue** pour assurer la justesse de votre planning de réception.
- La **taxe** (TVA) et la **méthode de facturation.**

Mis a jour le : 16/01/2026
