---
source: https://intercom-help.eu/vertuoza/fr/articles/367831-smtp-qu-est-ce-que-c-est
categorie: Paramètres
titre: SMTP : qu'est-ce que c'est ?
date_recuperation: 2026-09-05
---

# SMTP : qu'est-ce que c'est ?

Le **SMTP (Simple Mail Transfer Protocol)** est le protocole technique utilisé pour envoyer des emails. C’est une sorte de « tuyau de sortie » qui permet à Vertuoza (ou à n’importe quelle autre application) d’envoyer un email depuis votre propre adresse email, via votre fournisseur de messagerie (Gmail, Outlook, etc.).

### Avant : envoi via Vertuoza

Jusqu’à présent, tous les emails envoyés depuis Vertuoza (devis, factures, rapports, commandes…) utilisaient une adresse générique du type **[noreply_nom@vertuoza.com]()**.
Cela pouvait poser certains problèmes :

- 📤 Vos clients ne voyaient pas votre vraie adresse email comme expéditeur
- ⚠️ Certains emails pouvaient arriver en spam
- 🧩 Manque de fluidité si vous préfériez gérer vos échanges via votre messagerie habituelle

### Maintenant : envoi avec votre propre adresse

Grâce à la nouvelle intégration email, vous pouvez désormais envoyer vos emails Vertuoza **avec votre propre adresse professionnelle** (ex. : Gmail ou Google Workspace).

✅ Avantages :

- Vos emails apparaissent comme venant de **votre adresse**
- 📩 Une copie est automatiquement visible dans votre boîte d’envoi habituelle (Gmail par exemple)
- 🚀 Meilleure délivrabilité (moins de spams)
- 🔒 Toujours un historique des emails envoyés dans Vertuoza

⚠️ **Important à savoir** :
Depuis cette mise à jour, **les statuts de réception et d’ouverture des emails (vu / non vu, délivré, etc.) n’apparaissent plus dans l’historique Vertuoza.**
👉 C’est désormais **votre serveur de messagerie (Google, Outlook, ou autre via SMTP)** qui gère ces informations.

### Quelles intégrations sont disponibles ?

- 🔗 **Google (Gmail & Google Workspace)**
- 🔗 **SMTP personnalisé**
- 🔗 **Microsoft Outlook / 365**

👉 Guide pour configurer SMTP : [Configurer votre adresse email avec SMTP](https://intercom-help.eu/vertuoza/fr/articles/413323-configurer-votre-adresse-email-avec-smtp)

### Historique Vertuoza : qu’est-ce qui reste ?

Dans l’historique de vos documents (devis, factures, etc.), vous continuez de voir :

- ✅ La trace que l’email a bien été **envoyé**
- ✅ Le contenu de l’email et ses pièces jointes
- ✅ Le(s) destinataire(s)

Mais vous ne verrez plus :

- ❌ Le statut « reçu » ou « ouvert » (puisque c’est le serveur de messagerie de l’utilisateur qui gère ça maintenant).

👉 **[Pour plus d’informations sur le processus d’envoi d’e-mails avec votre propre adresse ](https://intercom-help.eu/vertuoza/fr/articles/411728-envoi-des-emails-avec-ta-propre-adresse)**

Mis a jour le : 21/11/2025
