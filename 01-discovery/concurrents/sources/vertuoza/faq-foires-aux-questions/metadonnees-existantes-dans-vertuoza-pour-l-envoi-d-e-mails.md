---
source: https://intercom-help.eu/vertuoza/fr/articles/281074-metadonnees-existantes-dans-vertuoza-pour-l-envoi-d-e-mails
categorie: FAQ (Foires Aux Questions)
titre: Métadonnées existantes dans Vertuoza pour l'envoi d'e-mails
date_recuperation: 2026-09-05
---

# Métadonnées existantes dans Vertuoza pour l'envoi d'e-mails

### **Qu'est-ce que les métadonnées ?**

Les **métadonnées** sont des éléments de texte placés dans un modèle d'email, que vous pouvez personnaliser. Lors de l'envoi de l'email, ces balises sont remplacées par des informations spécifiques, telles que le nom du client ou la référence du devis. Par exemple, la balise **[NOM_CLIENT]** sera remplacée par le nom complet du client dans l'email.

### **Comment les utiliser ?**

Lorsque vous sélectionnez un type de mail à envoyer (par exemple, un devis ou une facture), vous choisissez les métadonnées correspondant à ce type. Vous pouvez ensuite insérer ces balises dans le corps de l'email où vous souhaitez que les informations soient affichées.

Voici une liste des types de mails courants et des métadonnées que vous pouvez utiliser pour personnaliser vos envois :

___________________________________________________________

### **1. Devis**

Les métadonnées à utiliser dans un mail de devis sont :

- **[NOM_CLIENT]** : Nom complet du client
- **[NOM_ARCHI]** : Nom complet de l'architecte
- **[NOM_GESTIONNAIRE]** : Nom complet du gestionnaire
- **[MAIL_GESTIONNAIRE]** : Mail du gestionnaire de chantier
- **[MAIL_COMMERCIAL]** : Mail du commercial
- **[REFERENCE]** : Référence du devis
- **[LIEN]** : Lien externe à la plate-forme (Dropbox, drive, etc.)
- **[DATE_JOUR]** : Date actuelle
- **[LINK_DEVIS]** : Lien du devis
- **[CIVILITE_ARCHI]** : Civilité de l'architecte
- **[NUMBER_QUOTE]** : Numéro du devis

### **2. Demande / Proposition de prix**

- **[NOM_CLIENT]** : Nom complet du client
- **[NOM_ARCHI]** : Nom complet de l'architecte
- **[NOM_GESTIONNAIRE]** : Nom complet du gestionnaire
- **[MAIL_GESTIONNAIRE]** : Mail du gestionnaire de chantier
- **[NOM_CHANTIER]** : Nom du chantier
- **[REFERENCE]** : Référence
- **[LIEN]** : Lien externe à la plate-forme
- **[DATE_JOUR]** : Date actuelle
- **[CIVILITE_ARCHI]** : Civilité de l'architecte

___________________________________________________________

### **3. Commande Matériaux**

- **[NOM_CLIENT]** : Nom complet du client
- **[NOM_ARCHI]** : Nom complet de l'architecte
- **[NOM_GESTIONNAIRE]** : Nom complet du gestionnaire
- **[MAIL_GESTIONNAIRE]** : Mail du gestionnaire de chantier
- **[NOM_CHANTIER]** : Nom du chantier
- **[REFERENCE]** : Référence
- **[LIEN]** : Lien externe à la plate-forme
- **[DATE_JOUR]** : Date actuelle
- **[CIVILITE_ARCHI]** : Civilité de l'architecte

___________________________________________________________

### **4. Facturation**

- **[NOM_CLIENT]** : Nom complet du client
- **[NOM_ARCHI]** : Nom complet de l'architecte
- **[NOM_GESTIONNAIRE]** : Nom complet du gestionnaire
- **[MAIL_GESTIONNAIRE]** : Mail du gestionnaire de chantier
- **[NOM_CHANTIER]** : Nom du chantier
- **[REFERENCE]** : Référence
- **[LIEN]** : Lien externe à la plate-forme
- **[DATE_JOUR]** : Date actuelle
- **[DATE_FACTURE]** : Date de la facture
- **[NO_FACTURE]** : Numéro de la facture
- **[CIVILITE_ARCHI]** : Civilité de l'architecte

___________________________________________________________

### **5. Suivi de chantier - Avancement(s)**

- **[NOM_CLIENT]** : Nom complet du client
- **[NOM_ARCHI]** : Nom complet de l'architecte
- **[NOM_GESTIONNAIRE]** : Nom complet du gestionnaire
- **[MAIL_GESTIONNAIRE]** : Mail du gestionnaire de chantier
- **[NOM_CHANTIER]** : Nom du chantier
- **[REFERENCE]** : Référence
- **[LIEN]** : Lien externe à la plate-forme
- **[DATE_JOUR]** : Date actuelle

___________________________________________________________

### **6. Intervention**

- **[NOM_RESPONSABLE]** : Nom complet du responsable
- **[DATE_INTER]** : Date d'intervention
- **[HORAIRE_INTER]** : Horaire de l'intervention
- **[ADRESSE]** : Adresse de l'intervention
- **[NOM_INSTALLATION]** : Nom de l'installation

___________________________________________________________

### **Exemple d'utilisation des métadonnées dans un email :**

Supposons que vous envoyez un **devis** à un client, voici comment cela pourrait être rédigé avec les métadonnées :

Bonjour [CIVILITE_ARCHI] [NOM_ARCHI],

Veuillez trouver ci-joint le devis n° **[NUMBER_QUOTE]** pour le chantier **[NOM_CHANTIER]**.

Le devis a été préparé pour le client **[NOM_CLIENT]** et la référence est **[REFERENCE]**.

Pour plus d'informations, vous pouvez consulter le devis en ligne ici : **[LINK_DEVIS]**.

Date de l'envoi : **[DATE_JOUR]**.

Cordialement,

**[NOM_GESTIONNAIRE]**

**[MAIL_GESTIONNAIRE]**

Mis a jour le : 12/03/2025
