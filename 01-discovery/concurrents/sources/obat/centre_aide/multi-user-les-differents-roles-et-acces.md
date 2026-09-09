---
url: https://aide.obat.fr/multi-user-les-differents-roles-et-acces
url_finale: https://aide.obat.fr/multi-user-les-differents-roles-et-acces
date_collecte: 2026-09-09
destination: centre_aide
---

# Multi user : les différents rôles et accès

## Dans un environnement où plusieurs utilisateurs interagissent, les niveaux d'accès sont déterminés par les rôles assignés à chacun. Nous allons donc vous expliquer les droits et les permissions associés à chaque rôle.



### 👥 Les 7 rôles Obat

| Rôle | Description courte | 
|---|---|
| 👑 [**Propriétaire**](https://aide.obat.fr#proprietaire) | Créateur de l'entreprise. Accès complet, aucune restriction. | 
| 🔧 **Administrateur** | Quasi identique au Propriétaire, sans les actions impactant la facturation Obat. | 
| 💼 [**Commercial**](https://aide.obat.fr#commercial) | Focalisé sur la relation client : devis, factures (si autorisé), chantiers de son périmètre. | 
| 📊 **Expert comptable** | Accès large en lecture/écriture sur la comptabilité et les achats, mais ne peut pas créer/modifier de factures ni de devis. Siège gratuit. | 
| 🏗️ **Chef de chantier** | Focalisé sur l'exécution terrain : planning, calendrier, suivi du temps, chantiers. Accès aux clients, fournisseurs, devis, factures et à tous les chantiers **uniquement si les permissions supplémentaires sont activées** . | 
| 👷 [**Ouvrier**](https://aide.obat.fr#Ouvrier) | Accès minimal : pointage de ses heures, vue de ses chantiers et de son calendrier. | 

### 📖 Résumé par rôle


#### 👑 Propriétaire

### 🟢 Ce qu'il peut faire

- 
**Tout.** Aucune restriction sur aucun module.
- 
Seul rôle pouvant accéder à l' **Espace Partenaire**
- 
Seul rôle pouvant **changer d'offre** , souscrire de nouvelles options, régler les factures d'abonnement
- 
Seul rôle pouvant **créer de nouvelles licences/sièges** utilisateur
- 
Seul rôle pouvant accéder aux **Modules**
- 
Accès complet au **Chat** (conversations liées aux chantiers)

### 🔴 Ce qu'il ne peut pas faire

- 
Rien. Il a accès à l'intégralité de l'application.

### ⚙️ Personnalisations possibles

- 
Aucune (accès total)


#### 🔧 Administrateur

### 🟢 Ce qu'il peut faire

- 
Accéder à **toutes les fonctionnalités métier** (devis, factures, chantiers, planning, calendrier, suivi du temps, achats, bibliothèque, pilotage, clients, fournisseurs, banques, etc.)
- 
**Gérer les utilisateurs** (inviter, activer, désactiver) — uniquement sur des sièges déjà disponibles
- 
Accéder aux **paramètres** (entreprise, informations, calendrier, banques, comptabilité, documents, envoi de mails, préférences, utilisateurs, compte, abonnement en lecture)
- 
Gérer le **parrainage** avec toutes les permissions (comme le propriétaire)
- 
Utiliser le **Chat** avec toutes les permissions (comme le propriétaire)

### 🔴 Ce qu'il ne peut pas faire

- 
❌ Changer d'offre tarifaire ou la stopper
- 
❌ Souscrire de nouvelles options / sièges
- 
❌ Régler une facture d'abonnement Obat
- 
❌ Changer le moyen de paiement
- 
❌ Accéder à l'Espace Partenaire
- 
❌ Accéder aux Modules
- 
❌ Accéder à Recall et Compte pro
- 
❌ S'abonner à Batichiffrage (depuis la Bibliothèque)

### ⚙️ Personnalisations possibles

- 
**Peut accéder aux informations bancaires** (activée par défaut à l'invitation) : si décoché → pas d'accès aux Banques (menu, paramètres, widget dashboard, option virement sur factures)


#### 💼 Commercial


### 🟢 Ce qu'il peut faire

- 
✅ Gérer les **clients** (créer, modifier, visualiser) — limité à son périmètre si personnalisation activée
- 
✅ Gérer les **chantiers** (créer, modifier, visualiser) — limité aux chantiers de ses clients si personnalisation activée
- 
✅ Gérer les **devis** (créer, modifier, envoyer, dupliquer, supprimer, changer de statut)
- 
✅ Gérer les **factures** (si personnalisation "Peut gérer les factures" activée)
- 
✅ Visualiser les **fournisseurs** et la**Bibliothèque** (avec restrictions sur suppression)
- 
✅ Visualiser le **calendrier** (uniquement ses événements, peut modifier ses événements et types d'événements)
- 
✅ Visualiser le **planning** de ses clients/chantiers (lecture seule — pas de mode édition, lots/tâches, bibliothèque, plan de charge)
- 
✅ Accéder aux **paramètres** : Mes informations, Envoi de mails, Compte, Affiliation
- 
✅ Utiliser la **barre de recherche** (sauf recherche Achats)
- 
✅ Voir le **Dashboard** : widgets reste à encaisser, CA, chantiers, tableau des documents (adaptés à son périmètre si restreint)

### 🔴 Ce qu'il ne peut pas faire

- 
❌ Accéder au **Suivi du temps** (icône cachée)
- 
❌ Accéder aux **Achats** (menu caché)
- 
❌ Accéder aux **Banques** (menu caché)
- 
❌ Accéder au **PV de réception** (bouton caché — peut voir le PV dans les documents liés)
- 
❌ Accéder aux **Configurations** (entreprise, ressources) du module OPC
- 
❌ Modifier le champ "commercial" sur les fiches clients
- 
❌ Modifier le champ "Intervenant" et "Chef de chantier" sur les chantiers
- 
❌ Voir le graphique "TVA collectée" sur le Pilotage
- 
❌ Accéder aux paramètres : Mon entreprise, Mon calendrier, Banques, Comptabilité, Mes documents, Préférences, Utilisateurs, Abonnement, Modules, Partenaires
- 
❌ Accéder à : Kit marketing, Renalto, Recall, Compte pro
- 
❌ Voir le popover Onboarding Croissance (Planning, Calendrier, Suivi du temps)
- 
❌ Voir le bouton "Changer d'offre" / "S'abonner à Batichiffrage"
- 
❌ Créer des achats depuis le bouton "Créer"
- 
❌ **Chat** : ne peut pas créer de conversations liées à un chantier depuis le chat ou les panneaux d'informations

### ⚙️ Personnalisations possibles (3 permissions, toutes ON par défaut à l'invitation)

- 
**Peut gérer les factures** (activée par défaut) : si décoché → perd l'accès à la création/modification/suppression/envoi/statut des factures, avoirs, retenues de garantie et primes énergétiques
- 
**Peut gérer l'ensemble des clients/chantiers** (activée par défaut) : si décoché → ne voit que son périmètre (ses clients et les chantiers de ses clients), le dashboard et le pilotage s'adaptent
- 
**Peut accéder au pilotage** (activée par défaut) : si décoché (combiné avec "Peut gérer l'ensemble des clients/chantiers" décoché) → seul le widget "Performance commerciale" est visible


#### 📊 Expert comptable


### 🟢 Ce qu'il peut faire

- 
✅ Accéder aux **factures** en lecture seule (visualiser, télécharger, imprimer)
- 
✅ **Créer et modifier des contacts** (clients)
- 
✅ Accéder aux **chantiers** (tous) avec toutes les données financières —**Créer et modifier des chantiers**
- 
✅ Accéder au **Suivi du temps** en lecture (visualiser + export CSV/XLSX, sans pouvoir saisir de données)
- 
✅ Accéder aux **Achats** avec toutes les permissions
- 
✅ Accéder aux **Banques** avec toutes les permissions
- 
✅ Accéder à la **Bibliothèque** (avec restriction sur Batichiffrage)
- 
✅ Accéder au **Pilotage** avec toutes les permissions
- 
✅ Gérer les **fournisseurs** avec toutes les permissions
- 
✅ Accéder à la **Rentabilité** chantier avec toutes les permissions
- 
✅ Accéder aux paramètres : Mon entreprise, Mes informations, Banques, Comptabilité, Mes documents, Envoi de mails, Préférences, Compte, Abonnement (lecture seule), Affiliation
- 
✅ Valider les pointages (notification suivi du temps)

### 🔴 Ce qu'il ne peut pas faire

- 
❌ **Créer ou modifier des factures** (pas de bouton "Nouvelle facture", pas de modification, pas de changement de statut, pas d'envoi)
- 
❌ **Créer ou modifier des devis** (pas de bouton "Nouveau devis", pas de modification)
- 
❌ **Créer ou modifier des avoirs, retenues de garantie, primes énergétiques**
- 
❌ **Accéder aux options de paiement** (ex : paiement par virement)
- 
❌ Ne voit pas le **champ "commercial"** lors de l'ajout ou la modification d'un client
- 
❌ Accéder au **Planning** (menu caché)
- 
❌ Accéder au **Calendrier** (menu caché)
- 
❌ Accéder au **PV de réception** (peut voir les PV dans les documents liés)
- 
❌ Modifier le Suivi du temps (saisie de données)
- 
❌ Accéder aux paramètres : Utilisateurs, Modules, Partenaires
- 
❌ Accéder à : Kit marketing, Marketplace, Recall, Renalto, Compte pro
- 
❌ Stopper l'abonnement ou souscrire de nouvelles options
- 
❌ Régler une facture d'abonnement
- 
❌ Voir le popover Onboarding Croissance
- 
❌ Voir le bouton "Changer d'offre" / "S'abonner à Batichiffrage"
- 
❌ **Chat** : ne peut pas créer de conversation liée à un chantier depuis le chat ou le panneau latéral

### ⚙️ Personnalisations possibles

- 
Aucune personnalisation possible


#### 🏗️ Chef de chantier

⚠️ **Toutes les permissions supplémentaires ci-dessous sont activées par défaut.** Un administrateur ou propriétaire doit les activer dans les paramètres de l'utilisateur pour débloquer les accès correspondants.



### 🟢 Ce qu'il peut faire (par défaut, sans permission supplémentaire)

- 
✅ Accéder au **Planning** avec toutes les permissions (mode édition, lots/tâches, bibliothèque, plan de charge)
- 
✅ Accéder au **Calendrier** avec toutes les permissions (sauf modification d'événements non créés par lui)
- 
✅ Accéder au **Suivi du temps** avec toutes les permissions (validation admin + interface ouvriers)
- 
✅ Visualiser les **chantiers qui lui sont attribués** — sans données financières (colonnes Devisé, Facturé, Encaissé, Avancement masquées)
- 
✅ **Créer et modifier des chantiers** , attribuer des intervenants sur des chantiers (ne peut pas supprimer)
- 
✅ **Créer et modifier des clients** et des**fournisseurs**
- 
✅ Accéder aux **Achats** avec toutes les permissions
- 
✅ Accéder à la **Rentabilité** chantier (peut voir "Nouvel achat" et "Nouvelle saisie de temps")
- 
✅ Accéder au **PV de réception** avec toutes les permissions
- 
✅ Accéder à la **Marketplace**
- 
✅ Voir le **Dashboard** : widget Chantiers (sans données financières, sans barre marge) + notification suivi du temps
- 
✅ Utiliser la **barre de recherche** (sauf Devis, Factures, Clients par défaut)
- 
✅ Accéder aux paramètres : Mes informations, Mon calendrier, Compte, Affiliation

### 🟢 Ce qu'il peut faire en plus (si permissions supplémentaires activées — toutes ON par défaut)

- 
⚙️ **Peut voir les éléments de facturation** → peut consulter les devis et les factures de ses chantiers (lecture seule)
- 
⚙️ **Peut gérer les factures** → peut créer, modifier et supprimer des factures
- 
⚙️ **Peut gérer les devis** → peut voir, créer, modifier et supprimer des devis
- 
⚙️ **Peut gérer les ressources** → peut créer et modifier les ressources du planning et accéder à l'ensemble des paramètres de configuration des ressources
- 
⚙️ **Peut voir tous les chantiers** → peut voir tous les chantiers de l'entreprise (et pas uniquement ceux qui lui sont attribués)

### 🔴 Ce qu'il ne peut pas faire

- 
❌ **Supprimer** un chantier
- 
❌ Voir les **données financières** des chantiers
- 
❌ Voir la **barre d'avancement de marge** de chantier
- 
❌ Accéder aux **Banques** (menu caché)
- 
❌ Accéder à la **Bibliothèque** (menu caché)
- 
❌ Accéder au **Pilotage** (icône cachée) — pas d'accès aux statistiques de l'entreprise
- 
❌ Voir les widgets Dashboard : reste à encaisser, CA, tableau des documents, banques
- 
❌ Accéder aux **Retenues de garantie** et**Primes énergétiques**
- 
❌ Accéder aux paramètres : Mon entreprise, Banques, Comptabilité, Mes documents, Envoi de mails, Préférences, Abonnement, Utilisateurs, Modules, Partenaires
- 
❌ Accéder à : Kit marketing, Renalto, Recall, Compte pro
- 
❌ Voir le popover Onboarding Croissance
- 
❌ Voir le bouton "Changer d'offre"
- 
❌ Ne peut pas **changer d'abonnement**

### ⚙️ Personnalisations possibles (5 permissions, toutes ON par défaut à l'invitation)

| Permission | Impact si activée | 
|---|---|
| **Peut voir les éléments de facturation** | Peut consulter les devis et les factures liés à ses chantiers (lecture seule) | 
| **Peut gérer les factures** | Peut créer, modifier et supprimer des factures | 
| **Peut gérer les devis** | Peut voir, créer, modifier et supprimer des devis | 
| **Peut gérer les ressources** | Peut créer et modifier les ressources du planning et accéder aux paramètres de configuration des ressources | 
| **Peut voir tous les chantiers** | Peut voir l'ensemble des chantiers de l'entreprise (par défaut : uniquement ses chantiers attribués) | 

Si le chef de chantier ne dispose pas de la permission **« Peut gérer les ressources »**, certaines informations et fonctionnalités ne seront pas accessibles :

- 
Les **coûts** ne sont pas visibles dans le panneau**Ressources**
- 
Les **coûts** ne sont pas affichés dans le**suivi du temps**
- 
L’ **export du suivi du temps** n’est pas disponible
- 
L’onglet **Rentabilité** n’est pas accessible


#### 👷 Ouvrier


### 🟢 Ce qu'il peut faire

- 
✅ Voir le **Planning** de ses chantiers (lecture seule — pas de mode édition, pas de lots/tâches, pas de bibliothèque, pas de plan de charge)
- 
✅ Voir le **Calendrier** de ses événements (lecture seule — ne peut pas créer ni modifier d'événement, pas de backlog, pas de types)
- 
✅ **Pointer ses heures** via le Suivi du temps (interface mobile uniquement, pas d'accès à l'interface admin)
- 
✅ **Gérer ses absences**
- 
✅ Voir la liste de **ses chantiers** (sans données financières)
- 
✅ Accéder au **Chat** (ne peut pas créer de conversations liées à un chantier)
- 
✅ Voir le **Dashboard** : widget Calendrier + widget Suivi du temps (interface ouvriers)
- 
✅ Accéder aux paramètres : Mes informations, Compte, Affiliation

### 🔴 Ce qu'il ne peut pas faire

- 
❌ Accéder aux **Devis** (menu caché)
- 
❌ Accéder aux **Factures** (menu caché) — ni avoirs, RG, primes énergétiques
- 
❌ Accéder aux **Clients** (menu caché)
- 
❌ Accéder aux **Fournisseurs** (menu caché)
- 
❌ Accéder aux **Banques** (menu caché)
- 
❌ Accéder aux **Achats** (menu caché)
- 
❌ Accéder à la **Bibliothèque** (menu caché)
- 
❌ Accéder au **Pilotage** (icône cachée)
- 
❌ Accéder à la **Rentabilité** chantier
- 
❌ Accéder au **PV de réception**
- 
❌ Accéder aux **Configurations** OPC (entreprise, ressources)
- 
❌ **Créer/modifier/supprimer** un chantier
- 
❌ Voir les **données financières** des chantiers
- 
❌ Voir les boutons "Nouvelle facture", "Nouveau devis", "Modifier", "Supprimer" sur les chantiers
- 
❌ Voir l'encart **"Documents liés"** sur le side panel chantier
- 
❌ Voir la **barre d'avancement de marge** de chantier
- 
❌ Voir la **barre de recherche** (icône cachée)
- 
❌ Voir le bouton **"Créer"**
- 
❌ Voir les widgets Dashboard : reste à encaisser, CA, tableau des documents, banques, chantiers (sur mobile smartphone : uniquement widget Calendrier)
- 
❌ **Valider** des pointages
- 
❌ Voir les **notifications** (icône cloche cachée)
- 
❌ **Chat** : ne peut pas créer de conversations liées à un chantier
- 
❌ Accéder aux paramètres : Mon entreprise, Mon calendrier, Banques, Comptabilité, Mes documents, Envoi de mails, Préférences, Abonnement, Utilisateurs, Modules, Partenaires
- 
❌ Accéder à : Kit marketing, Marketplace, Contacts, Renalto, Recall, Compte pro
- 
❌ Voir le popover Onboarding Croissance
- 
❌ Voir le bouton "Changer d'offre"

### ⚙️ Personnalisations possibles

- 
Aucune personnalisation possible


### ⚙️ Personnalisations possibles (4 permissions, toutes ON par défaut à l'invitation)

| Permission | Impact si activée | 
|---|---|
| **Peut modifier la facture de l'intervention** | Peut modifier les lignes de facturation dans le rapport d'intervention (sinon encart Facturation en lecture seule) | 
| **Peut envoyer rapport et facture au client** | Voit le bouton "Finaliser et envoyer" à la fin de l'intervention (sinon uniquement "Finaliser") | 
| **Peut voir tous les chantiers/clients** | Peut voir l'ensemble des chantiers et clients de l'entreprise (par défaut : uniquement ses chantiers assignés et leurs clients) | 
| **Peut créer des interventions** | Peut créer de nouvelles interventions depuis le calendrier (sinon consultation et modification uniquement) | 

### 📊 Tableaux détaillés par module

#### 🗂️ Navigation et menus

| Module / Menu | 👑 Propriétaire | 🔧 Admin | 💼 Commercial | 📊 Expert comptable | 👷 Ouvrier | 
|---|---|---|---|---|---|
| Dashboard (accueil) | ✅ | ✅ | ✅ | ✅ | ✅ | 
| Devis | ✅ | ✅ | ✅ | ❌ | ❌ | 
| Factures | ✅ | ✅ | ⚙️ | ❌ | ❌ | 
| Avoirs | ✅ | ✅ | ⚙️ | ❌ | ❌ | 
| Retenues de garantie | ✅ | ✅ | ⚙️ | ✅ | ❌ | 
| Primes énergétiques | ✅ | ✅ | ⚙️ | ✅ | ❌ | 
| Interventions | ✅ | ✅ | ❌ | ❌ | ❌ | 
| Chantiers | ✅ | ✅ | ✅ | ✅ | 🔸 Ses chantiers | 
| Clients | ✅ | ✅ | ✅ | ✅ | ❌ | 
| Fournisseurs | ✅ | ✅ | ✅ | ✅ | ❌ | 
| Achats | ✅ | ✅ | ❌ | ✅ | ❌ | 
| Banques | ✅ | ⚙️ | ❌ | ✅ | ❌ | 
| Planning | ✅ | ✅ | 🔸 Lecture seule | ❌ | 🔸 Ses chantiers | 
| Calendrier | ✅ | ✅ | 🔸 Ses événements | ❌ | 🔸 Lecture seule | 
| Suivi du temps | ✅ | ✅ | ❌ | 🔸 Lecture + export | 🔸 Mobile | 
| Bibliothèque | ✅ | ✅ | 🔸 Sans suppression | ✅ | ❌ | 
| Pilotage | ✅ | ✅ | ⚙️ | ✅ | ❌ | 
| Barre de recherche | ✅ | ✅ | 🔸 Sans achats | ✅ | ❌ | 
| Bouton "Créer" | ✅ | ✅ | 🔸 Sans achats | 🔸 Sans facture/devis | ❌ | 
| Chat | ✅ | ✅ | 🔸 Pas de conversations chantier | 🔸 Pas de conversations chantier | 🔸 Pas de conversations chantier | 
| Kit marketing | ✅ | ✅ | ❌ | ❌ | ❌ | 
| Marketplace | ✅ | ✅ | ✅ | ❌ | ❌ | 
| Renalto | ✅ | ✅ | ❌ | ❌ | ❌ | 
| Recall | ✅ | ❌ | ❌ | ❌ | ❌ | 
| Compte pro | ✅ | ❌ | ❌ | ❌ | ❌ | 
| PV de réception | ✅ | ✅ | ❌ | ❌ | ❌ | 
| Parrainage | ✅ | ✅ | ❌ | ❌ | ❌ | 
| Notifications (cloche) | ✅ | ✅ | ✅ | ✅ | ❌ | 

#### 🏠 Dashboard — Widgets

| Widget | 👑 Propriétaire | 🔧 Admin | 💼 Commercial | 📊 Expert comptable | 🏗️ Chef chantier | 👷 Ouvrier | 
|---|---|---|---|---|---|---|
| Reste à encaisser | ✅ | ✅ | 🔸 Périmètre | ✅ | ❌ | ❌ | 
| Chiffre d'affaires | ✅ | ✅ | 🔸 Périmètre | ✅ | ❌ | ❌ | 
| Chantiers | ✅ | ✅ | 🔸 Périmètre | ✅ | 🔸 Sans données financières | 🔸 Ses chantiers | 
| Tableau des documents | ✅ | ✅ | 🔸 Périmètre | ✅ | ❌ | ❌ | 
| Banques | ✅ | ⚙️ | ❌ | ✅ | ❌ | ❌ | 
| Calendrier | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | 
| Suivi du temps | ❌ | ❌ | ❌ | ❌ | 🔸 Interface Admin | 🔸 Interface Ouvriers | 
| Notification pointage | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ | 

#### ⚙️ Paramètres

| Onglet | 👑 Propriétaire | 🔧 Admin | 💼 Commercial | 📊 Expert comptable | 🏗️ Chef chantier | 👷 Ouvrier | 
|---|---|---|---|---|---|---|
| Mon entreprise | ✅ | ✅ | ❌ | ✅ | ❌ | ❌ | 
| Mes informations | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 
| Mon calendrier | ✅ | ✅ | ❌ | ❌ | ✅ | ❌ | 
| Banques | ✅ | ⚙️ | ❌ | ✅ | ❌ | ❌ | 
| Comptabilité | ✅ | ✅ | ❌ | ✅ | ❌ | ❌ | 
| Mes documents | ✅ | ✅ | ❌ | ✅ | ❌ | ❌ | 
| Envoi de mails | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ | 
| Préférences | ✅ | ✅ | ❌ | ✅ | ❌ | ❌ | 
| Abonnement | ✅ | 🔸 Lecture seule | ❌ | 🔸 Lecture seule | ❌ | ❌ | 
| Compte | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 
| Utilisateurs | ✅ | 🔸 Sans créer de licence | ❌ | ❌ | ❌ | ❌ | 
| Modules | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | 
| Partenaires | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | 
| Affiliation | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 

#### 🎛️ Personnalisations par rôle

| Rôle | Personnalisation | État par défaut | Impact si activée / désactivée | 
|---|---|---|---|

| Rôle | Personnalisation | État par défaut | Impact si activée / désactivée | 
|---|---|---|---|
| 🔧 **Administrateur** | Peut accéder aux informations bancaires | ✅ ON par défaut | ❌ Si décoché → pas d'accès aux Banques (menu, paramètres, widget dashboard, option virement sur factures) | 
| 💼 **Commercial** | Peut gérer les factures | ✅ ON par défaut | ❌ Si décoché → perd l'accès à la création/modification/suppression/envoi/statut des factures, avoirs, retenues de garantie et primes énergétiques | 
| 💼 **Commercial** | Peut gérer l'ensemble des clients/chantiers | ✅ ON par défaut | ❌ Si décoché → ne voit que les clients qui lui sont affectés et les chantiers de ces clients. Le dashboard et le pilotage s'adaptent à son périmètre | 
| 💼 **Commercial** | Peut accéder au pilotage | ✅ ON par défaut | ❌ Si décoché (combiné avec "Peut gérer l'ensemble des clients/chantiers" décoché) → seul le widget "Performance commerciale" est visible | 
| 🏗️ **Chef de chantier** | Peut voir les éléments de facturation | ✅ ON par défaut | ❌ Si décoché → perd l'accès en lecture aux devis et factures liés à ses chantiers | 
| 🏗️ **Chef de chantier** | Peut gérer les factures | ✅ ON par défaut | ❌ Si décoché → ne peut plus créer, modifier ni supprimer des factures | 
| 🏗️ **Chef de chantier** | Peut gérer les devis | ✅ ON par défaut | ❌ Si décoché → ne peut plus voir, créer, modifier ni supprimer des devis | 
| 🏗️ **Chef de chantier** | Peut gérer les ressources | ✅ ON par défaut | ❌ Si décoché → ne peut plus créer/modifier les ressources du planning ni accéder aux paramètres de configuration des ressources | 
| 🏗️ **Chef de chantier** | Peut voir tous les chantiers | ✅ ON par défaut | ❌ Si décoché → ne voit que ses chantiers attribués | 
| 🔨 **Technicien** | Peut modifier la facture de l'intervention | ✅ ON par défaut | ❌ Si décoché → encart Facturation en lecture seule dans le rapport d'intervention | 
| 🔨 **Technicien** | Peut envoyer rapport et facture au client | ✅ ON par défaut | ❌ Si décoché → voit uniquement "Finaliser" au lieu de "Finaliser et envoyer" | 
| 🔨 **Technicien** | Peut voir tous les chantiers/clients | ✅ ON par défaut | ❌ Si décoché → ne voit que ses chantiers assignés et leurs clients | 
| 🔨 **Technicien** | Peut créer des interventions | ✅ ON par défaut | ❌ Si décoché → consultation et modification uniquement, pas de création | 

💡 **Note :** Les permissions additionnelles sont **activées par défaut à l'invitation d'un nouvel utilisateur**. Un Propriétaire ou Administrateur peut les désactiver manuellement dans les paramètres de l'utilisateur pour restreindre les accès.


**📌 Légende des tableaux :**

✅ Accès complet — ❌ Pas d'accès — 🔸 Accès partiel (voir détail dans la section du rôle) — ⚙️ Dépend d'une personnalisation activable dans les paramètres utilisateur



**Consultez également 👇**[Comment inviter un utilisateur ?](https://aide.obat.fr/comment-inviter-un-utilisateur?hsLang=fr)


 **💡Si vous avez encore des questions, n’hésitez pas à nous contacter et nous serons là pour vous aider par email : support@obat.fr , à travers notre fenêtre de chat, ou par téléphone au ☎️ 02 52 33 19 31 .**