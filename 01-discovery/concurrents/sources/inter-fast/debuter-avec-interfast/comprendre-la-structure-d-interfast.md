---
source: https://help.inter-fast.co/fr/articles/12919047-comprendre-la-structure-d-interfast
categorie: Débuter avec InterFast
titre: Comprendre la structure d'InterFast
date_recuperation: 2026-09-05
---

# Comprendre la structure d'InterFast

## I. Introduction

[Vidéo YouTube](https://www.youtube.com/watch?v=fiM4HIrlJyA)

L'application InterFast est constituée de nombreux objets interconnectés qui nourrissent l'intelligence de l'entreprise et permettent des connexions fluides entre les différents environnements. 

L'importance de chaque objet réside dans sa contribution à la vision globale et à la traçabilité des activités.

## II. Tableau des objets

Voici une définition rapide des principaux objets et la liste de ceux auxquels ils sont directement liés. Ces interconnexions offrent une structure unifiée et homogène de vos données pour en faciliter l'exploitation :

| **OBJET** | **DÉFINITION** | **CONNEXIONS PRINCIPALES** |
| --- | --- | --- |
| **I. Opérations** |  |  |
| **[Interventions](https://help.inter-fast.co/fr/articles/10253860-planifier-un-evenement-app-web#h_effa544bfd)** | Événements du Calendrier nécessitant un rapport d'intervention. | - Utilisateurs (Planificateur / Intervenant) - Clients / Prospects (dont les Contacts et Adresses client) - Agences - Équipements (conditionnés par l'Adresse client) - Chantiers - Maintenances - Devis clients - Factures clients - Commandes fournisseurs - Factures fournisseurs - Automatisations - Documents (Galerie d'images / Vidéos / fichiers PDF) - Commentaires - Actions commerciales (Emails) |
| **[Rendez-vous](https://help.inter-fast.co/fr/articles/10253860-planifier-un-evenement-app-web#h_4d92ecf649)** | Événements du Calendrier pour lesquels aucun rapport d'intervention n'est attendu. | - Utilisateurs (Planificateur / Intervenant) - Clients / Prospects (dont les Adresses client) - Agences - Chantiers |
| **[Tâches](https://help.inter-fast.co/fr/articles/11161651-gerer-les-taches-app-web)** | Actions à réaliser. | - Utilisateurs (Assigné) *NB. À terme, les tâches seront reliées à d'autres objets* |
| **[Chantiers](https://help.inter-fast.co/fr/articles/10253930-comprendre-la-fiche-d-un-chantier)** | Dossiers numériques regroupant les informations d'un projet. | - Utilisateurs (Créateur / Intervenant) - Clients / Prospects (dont les Adresses client) - Agences - Interventions - Devis clients - Factures clients - Avoirs clients - Commandes fournisseurs - Factures fournisseurs - Stock de produits (associé au Chantier) - Commentaires |
| **[Maintenances](https://help.inter-fast.co/fr/articles/10253850-comprendre-la-fiche-d-une-maintenance)** | Dossiers numériques regroupant les informations d'un contrat de maintenance. | - Utilisateurs (Créateur / Intervenant) - Clients / Prospects (dont les Adresses client) - Interventions - Équipements (conditionnés par l'Adresse) - Devis clients - Factures clients - Avoirs clients - Commandes fournisseurs - Factures fournisseurs - Commentaires |
| **II. Ventes** |  |  |
| **[Devis client](https://intercom.help/interfast/fr/articles/10245590-creer-un-devis)** | Document commercial proposant un prix pour une prestation de services ou une vente de marchandises, avant réalisation de celle-ci. | - Utilisateurs (Éditeur) - Clients / Prospects (dont les Contacts et Adresses clients) - Agences - Interventions (liées au Client OU à ses relations) - Chantiers - Maintenances - Factures (liées au Client OU à ses relations) - Commandes fournisseurs (par conversion du devis en BDC) - Articles / Ouvrages de la Bibliothèque - Automatisations (liées aux Devis) - Documents (Pièces jointes) - Commentaires - Actions commerciales (Emails simples ou avec signature électronique) Sous-objets périphériques : *Modèles de devis* |
| **[Factures client](https://help.inter-fast.co/fr/articles/10253768-creer-une-facture-simple)** | Document comptable établi par un vendeur à son client à la suite de la réalisation d'une prestation de services ou de la vente d'une marchandise. | - Utilisateurs (Éditeur) - Clients / Prospects (dont les Contacts et Adresses clients) - Agences - Interventions (liées au Client OU à ses relations) - Chantiers - Maintenances - Devis (liés au Client OU à ses relations) - Avoirs - Paiements clients - Articles / Ouvrages de la Bibliothèque - Automatisations (liées aux Factures) - Documents (Pièces jointes) - Commentaires - Actions commerciales (Emails) |
| **[Avoirs clients](https://help.inter-fast.co/fr/articles/10253824-creer-une-facture-d-avoir-client)** | Document comptable établi pour corriger ou annuler tout ou partie d'une facture initiale. | - Utilisateurs (Éditeur) - Clients / Prospects (dont les Contacts et Adresses clients) - Agences - Interventions (liées au Client OU à ses relations) - Chantiers - Maintenances - Facture client - Articles / Ouvrages de la Bibliothèque - Documents (Pièces jointes) - Commentaires - Actions commerciales (Emails) |
| **[Paiements clients](https://help.inter-fast.co/fr/articles/10512915-consigner-un-paiement)** | Enregistrement des sommes d'argent payées par le client en échange de la réalisation d'une prestation de services ou de la vente d'une marchandise. | - Utilisateurs (Consignateur) - Clients / Prospect - Facture client |
| **[Commandes fournisseurs](https://help.inter-fast.co/fr/articles/11560415-utiliser-les-commandes-v2-app-web)** | Document commercial formalisant une intention d'achat d'une prestation de services ou de marchandises. | - Utilisateurs (Éditeur) - Fournisseurs - Interventions - Chantiers - Maintenances - Facture fournisseur - Articles / Ouvrages de la Bibliothèque - Documents (Pièces jointes) - Commentaires - Actions commerciales (Emails) |
| **[Factures](https://help.inter-fast.co/fr/articles/10253916-ajouter-une-depense-app-web) / [Avoirs fournisseurs](https://help.inter-fast.co/fr/articles/10253998-enregistrer-un-avoir-fournisseur)** | Document comptable que l'entreprise reçoit et qui détaille les biens ou services acquis, établissant une dette ou un crédit auprès du fournisseur. | - Utilisateurs (Éditeur) - Fournisseurs - Agences - Interventions - Chantiers - Maintenances - Commandes fournisseurs - Paiements fournisseurs - Articles / Ouvrages de la Bibliothèque - Documents (Pièces jointes) - Commentaires - Actions commerciales (Emails) |
| **III. Outils** |  |  |
| **[Clients](https://help.inter-fast.co/fr/articles/10253952-comprendre-la-fiche-d-un-client) / [Prospects](https://help.inter-fast.co/fr/articles/10253899-ajouter-des-clients-prospects-fournisseurs#h_a86e9237c9)** | Personnes physiques (Particuliers) ou morales (Professionnels, Syndics) qui achètent actuellement (clients) ou qui ont le potentiel d'acheter (prospects) les prestations de services ou les marchandises de l'entreprise. | - Utilisateurs (Commercial Affecté) - Clients / Prospects (Relations) - Équipements (en lien avec les Adresses du client) - Interventions - Chantiers - Maintenances - Devis - Factures - Avoirs - Documents - Commentaires - Actions commerciales (Emails / Appels / SMS / Notes) *Sous-objets périphériques :* - *Contacts* - *Relations* - *Adresses (incluant les Sites et les Emplacements)* |
| **[Fournisseurs](https://help.inter-fast.co/fr/articles/10253899-ajouter-des-clients-prospects-fournisseurs#h_5dab1f8ab4)** | Les Fournisseurs sont les entités ou individus qui vendent des biens, des matières premières ou des services nécessaires à l'activité et au fonctionnement de l'entreprise. | - Clients / Prospects (Relations) - Interventions - Commandes fournisseur - Factures fournisseur - Documents - Commentaires - Actions commerciales (Emails / Appels / SMS / Notes) *Sous-objets périphériques :* - *Contacts* - *Relations* - *Adresses* |
| **[Équipements](https://help.inter-fast.co/fr/articles/10253843-ajouter-et-consigner-des-equipements-niveau-1)** | Matériel ou machines installées chez les Clients / Prospects. | - Clients / Prospects - Adresse client - Interventions liées - Documents (Galerie d'images + fichiers PDF) - QR code |
| **[Articles](https://help.inter-fast.co/fr/articles/11172963-utiliser-les-articles)** | Prestation de service ou Matériel pré-enregistré pour composer des documents *(devis, factures, commandes)*. ​ ​ | - Catalogue de la Bibliothèque - Catégorie comptable - Ouvrage (Combinaison d'articles) - Devis client - Facture client - Avoir client - Commande fournisseur |
| **[Ouvrages](https://help.inter-fast.co/fr/articles/10253871-utiliser-les-ouvrages)** | Compositions de plusieurs articles pour composer des documents devis ou des factures. | - Articles (Composants) - Catalogue de la Bibliothèque - Devis client - Facture client - Avoir client - Commande fournisseur |
| **[Produits en stock](https://help.inter-fast.co/fr/articles/10254009-gerer-les-stocks-app-web#h_379643b8c2)** | Actif physique de l'entreprise *(Consommables, Outillages, Bouteilles de fluide)*. | - Articles de la Bibliothèque - Emplacement - Intervention > *notamment CERFA et BSFF pour les bouteilles de fluide* - Chantier - Client / Prospect - QR Code |
| **[Utilisateurs](https://help.inter-fast.co/fr/articles/10253862-comprendre-la-fiche-utilisateur)** | Personnels autorisés à utiliser l'application InterFast selon un rôle et des permissions prédéfinis. | - Compte entreprise - Agence(s) - Interventions - Rendez-vous - Tâches - Chantiers - Maintenances - Devis client - Factures client - Avoirs client - Paiements client - Commandes fournisseurs - Factures fournisseurs - Client / Prospect - Emplacement - Automatisations (Assigné / Émetteur) - Feuilles de temps |
| **[Automatisations](https://help.inter-fast.co/fr/articles/11035957-automatiser-mes-actions-et-taches)** | Scénario d'actions qui se déclenche selon des règles prédéfinies. | - Interventions - Demandes client - Devis client - Factures client - Maintenances |
| **[Feuilles de temps](https://help.inter-fast.co/fr/articles/10253906-utiliser-les-feuilles-de-temps-app-web)** | Déclaration du temps de travail effectif par un collaborateur salarié | - Utilisateur - Interventions |
| **[Agences](https://help.inter-fast.co/fr/articles/12599199-gerer-ses-agences)** | Succursales ou équipes internes de l'entreprise. | - Compte entreprise - Utilisateurs (membres) - Interventions / Rendez-vous - Chantiers - Devis client - Factures client - Avoirs client - Factures fournisseur - Tableaux de bord |
| **[Types d'activité](https://help.inter-fast.co/fr/articles/10253856-utiliser-les-tableaux-de-bord#h_998b0c7f14)** | Label permettant de distinguer des domaines précis du modèle d'affaires d'une entreprise du CVC ​ ​*Trois types d'activité : SAV / Chantier / Maintenance* | - Interventions - Chantiers - Maintenances - Devis clients - Factures clients - Avoirs clients - Factures fournisseurs |
| **[Emplacements de stock](https://help.inter-fast.co/fr/articles/10254009-gerer-les-stocks-app-web#h_75f94ce30d)** | Entrepôts, magasins ou véhicules où sont stockés les produits de l'entreprise | - Produits en stock - Utilisateurs (Affectation) |
| **[QR Codes](https://help.inter-fast.co/fr/articles/12645780-utiliser-les-qr-codes-app-web)** | Codes numériques qui facilitent le suivi et l'association aux équipements et aux produits en stock. | - Équipement - Produit en stock *(Consommable / Outillage / Bouteille de fluide)* |

## III. Questions Fréquentes


Ne rassemblez pas toutes les informations sur une seule fiche Client. Utilisez la fonctionnalité des **[Relations](https://help.inter-fast.co/fr/articles/11651322-decouvrir-les-relations-clients)**.
    ◦ Créez une fiche pour le gestionnaire/payeur *(ex: le Syndic)*.
    ◦ Créez des fiches distinctes pour chaque site ou locataire *(pour l'historique technique)*.
    ◦ Liez-les via l'onglet "Relations". Cela permet de planifier l'intervention chez le locataire tout en adressant la facture au propriétaire/syndic.



Cela dépend de l'objet, pour préserver l'intégrité de la structure :
    ◦ **Interdit :** Les factures finalisées (portant un numéro) ne peuvent être supprimées conformément à la loi anti-fraude TVA. Elles peuvent seulement être annulées par un avoir.
    ◦ **Possible :** Les devis / factures au statut brouillon, les clients sans éléménts associés, les interventions quelque soit leur statut, etc.
    ◦ **Recommandé :** Utilisez l'**Archivage**. Cela masque l'objet *(Client, Chantier, Utilisateur)* des listes actives tout en conservant les liens historiques pour vos statistiques et les informations associées.



Oui, vous êtes propriétaire de vos données. L'administrateur du compte peut demander un **[Export complet](https://help.inter-fast.co/fr/articles/12916629-exporter-toutes-mes-donnees)** (archive ZIP contenant les fichiers CSV de chaque objet : Clients, Interventions, Factures, etc.) pour récupérer la totalité des informations stockées sur InterFast par votre entreprise.


Voilà, vous êtes désormais incollable sur la structure des données d'InterFast ! 🥳

Mis à jour le : 29/12/2025
