---
source: https://support.openfire.fr/hc/fr/articles/19096254481308-Configurez-vos-journaux
categorie: Configurer OpenFire
titre: Configurez vos journaux
date_recuperation: 2026-09-05
---

# Configurez vos journaux

Cet article vous guide dans la consultation, la création et la configuration de vos journaux comptables dans OpenFire.

**Cet article contient les sections suivantes :**

- Qu'est-ce qu'un journal comptable ?
- Créer et Configurer un Journal
  - Ajouter ou éditer un journal
  - Champs spécifiques aux journaux de Ventes
  - Champs spécifiques aux journaux d'Achats
  - Champs spécifiques aux journaux d'Espèces et de Banques
- Gérer les Séquences des Journaux
  - Qu'est-ce qu'une séquence ?
  - Comment modifier la séquence d'un journal ?
- Bonnes pratiques
- Pour aller plus loin

# Qu'est-ce qu'un journal comptable ?

---

Un journal comptable est un document qui consigne de manière chronologique et continue toutes les opérations financières effectuées par votre entreprise au cours d'un exercice comptable. C'est l'épine dorsale de votre comptabilité, permettant de suivre chaque transaction avec précision.

Généralement, les entreprises utilisent plusieurs journaux afin de classifier les opérations par nature (ventes, achats, banque, etc.). et de favoriser l'analyse de leurs données financières.

| 💡**Note **: dans OpenFire, une liste de journaux est proposée par défaut, suivant votre localisation fiscale et les informations que vous avez fournies lors du lancement de votre compte.  Pour consulter la liste de ces journaux, suivre le chemin d'accès suivant : *Facturation > Configuration > Comptabilité > Journaux* |
| --- |

Types de journaux préconisés :

| Nom du journal | Description |
| --- | --- |
| Vente | Enregistre toutes les opérations liées à vos ventes |
| Achat | Enregistre toutes les opérations liées à vos achats. Au sein des journaux d'achat, on peut distinguer les deux type de journaux suivants  :    **Achats d'exploitation** : ils sont généralement alimentés automatiquement par vos achats de biens et services liés à votre activité principale.  **Achats généraux** : ils sont souvent saisis manuellement et correspondent à des achats non liés directement à l'exploitation courante (ex: fournitures de bureau). |
| Banque | Enregistre toutes les opérations liées à des mouvements bancaires. |
| Caisse | Enregistre toutes les opérations liées à des mouvements de caisse. |
| Opération Diverses | Enregistre toutes les autres opérations qui ne rentrent pas dans les catégories spécifique. Au sein des journaux divers, on peut retrouver :   Les OD de bilans Les OD de payes |

# Créer et Configurer un Journal

---

Pour créer ou modifier un journal comptable dans OpenFire, suivez le chemin d'accès suivant : Facturation > Configuration > Comptabilité > Journaux

## Ajouter ou éditer un journal

Cliquer sur le bouton **Nouveau** pour créer un nouveau journal, ou cliquer sur un journal existant pour le modifier.

### Informations générales et champs communs aux différents journaux

Au niveau de l'en-tête, les informations suivantes sont essentielles :

**Nom du journal** : Le libellé complet du journal (ex: "Vente Exploitation").

**Type** : Le type de journal (Vente, Achats, Espèces, Banque, Divers). Ce choix impacte les champs disponibles dans l'onglet "Pièces comptables".

**Société** : Sélectionnez la société à laquelle ce journal est lié (uniquement pour le multi-société)

**Séquence des pièces comptables** : La séquence utilisée pour générer les numéros des pièces comptables (voir séquence ci-dessous)

**Code** : Le nom abrégé du journal, utilisé pour l'affichage et comme préfixe par défaut pour les pièces comptables de ce journal.

| 🚨**Avertissement** : Une fois que des écritures sont saisies dans un journal, son code ne devrait plus être modifié, au moins en cours d'exercice, pour conserver l'intégrité et la cohérence des écritures au sein du journal. |
| --- |

### Règles de contrôle de saisie sur les différents journaux

Pour chaque journal, vous pouvez mettre en place des contrôles de saisie basés sur des éléments de date et de comptes comptables, depuis l'onglet "Paramètres avancés" du journal

![](https://support.openfire.fr/hc/article_attachments/21505085997724)

**Comptes autorisés** : Permet de contrôler les écritures en sélectionnant les comptes autorisés pour ce journal.

**Date de verrouillage** : Ce champ permet de définir une date de verrouillage pour l'ensemble des utilisateurs. Aucune écriture comptable ne pourra être créée ou modifiée pour une date **antérieure ou égale** à la date de verrouillage. Ce verrouillage est souvent utilisé pour clore définitivement un exercice comptable ou une période fiscale, assurant ainsi l'intégrité des données.

**Date de verrouillage (hors profil conseillé) **: Ce champ définit une date de verrouillage des écritures pour tous les utilisateurs, à l'exception de ceux ayant le rôle **Conseiller**. Il permet de figer les données pour une période donnée (par exemple, la clôture mensuelle), tout en offrant aux auditeurs ou aux gestionnaires (les Conseillers) la flexibilité de faire des ajustements si nécessaire, sans perturber le travail des autres utilisateurs.

**Verrouiller les entrées postées avec Hash** (uniquement pour les journaux de type "Vente", "Achats" et "Divers") : Cette option empêche un utilisateur de remettre en brouillon une écriture publiée. Une fois publiée, l'écriture ne peut plus être modifiée.

## Champs spécifiques aux journaux de Ventes

**Compte des revenus par défaut** : Le compte par défaut pour les écritures comptables de type vente saisie dans ce journal.

**Séquence dédiée aux avoirs** : Cochez cette case si vous souhaitez une séquence différente pour les avoirs, différentes de celles des factures de ce journal

**Séquence pour les avoirs** : La séquence utilisée pour les numéros des avoirs.

**Vérifier la chronologie** : Cette option empêche la validation des factures liées au journal si :

- Il existe des brouillons de factures avec une date antérieure.
- Il y a des factures validées avec une date postérieure.

Paramètres avancés des journaux de type "Ventes"

![](https://support.openfire.fr/hc/article_attachments/21505038543772)

**Facturation électronique** : Gérez les paramètres liés à la facturation électronique.

| 📓**Pour aller plus loin** → Facturation électronique (à venir) |
| --- |

**Planifier une activité **: vous pouvez définir ici une activité à saisir automatiquement à la date d'échéance de la facture, afin de faciliter le recouvrement.

**Utilisateur réalisant l'activité** : permet de définir l'utilisateur en charge de la relance des factures de ce journal. Si vide, OpenFire attribuera la relance au vendeur de la facture.

| **🧑‍🏫Exemple** d'activité pour un flux de facturation en n étape ![](https://support.openfire.fr/hc/article_attachments/21505176201884) |
| --- |

| 📓**Pour aller plus loin** →  Méthode de relance de vos factures (à venir) |
| --- |

**Type de référence : **vous pouvez définir la référence par défaut qui apparaîtra sur les factures du client, une fois celle-ci validée, pour aider le client à se référer à cette facture en particulier lors du paiement.

**Standard de référence : **Vous pouvez choisir différents modèles par type de référence. Le modèle par défaut est la référence Odoo**.**

## Champs spécifiques aux journaux d'Achats

**Compte de Charges par défaut (pour les journaux d'achat)** : Le compte par défaut pour les écritures comptables de type achat saisie dans ce journal

## Champs spécifiques aux journaux d'Espèces et de Banques

**Compte d'espèces** (pour les journaux de caisse): Le compte par défaut pour les écritures comptables de type espèces.

**Compte bancaire** (pour les journaux de banque): Le compte par défaut pour les écritures comptables de banque.

**Compte d'attente : **compte d'attente utilisé par OpenFire à l'import des relevés bancaires. Ce compte sera utilisé en contrepartie du compte bancaire pour générer les mouvements journal à l'intégration des relevés, en attente du rapprochement définitif.

![](https://support.openfire.fr/hc/article_attachments/21573085474076)

**Compte de profit : **compte utilisé pour enregistré un profit lorsque le solde final est différent de ce qui a été calculé par le système

**Compte des pertes : **compte utilisé pour enregistré une perte lorsque le solde final de la caisse est différent de ce qui a été calculé par le système

**Séquence des paiements dédiés** : Cochez cette case si vous ne souhaitez pas partager la même séquence pour les paiements et les opérations bancaires publiés sur ce journal.

**Numéro de compte bancaire** : Le numéro de compte bancaire associé à ce journal.

**Provenance des relevés bancaires** : Indique si les relevés bancaires sont importés ou non dans OpenFire. L'importation des relevés bancaires nécessite l'installation d'un module dédié.

**Modes de paiements entrant** : permet de définir les modes de règlements clients disponibles pour ce journal

**Modes de paiements sortant **: permet de définir les modes de règlements fournisseurs disponibles pour ce journal

| 📓**Pour aller plus loin** →  Modes de paiement manuels |
| --- |

# Gérer les Séquences des Journaux

---

Les séquences sont essentielles pour la numérotation automatique et continue de vos pièces comptables.

## Qu'est-ce qu'une séquence ?

Une séquence définit une **méthode de numérotation des pièces à l'intérieur d'un journal**. Dans OpenFire, l'intégralité des pièces générées sont séquencées, afin d'assurer la traçabilité et l'intégrité des écritures comptables générées.

A chaque création de journal, une **séquence est automatiquement générée**, utilisant par défaut le code du journal comme préfixe. La séquence est générée par défaut sur le format suivant : `CODE/ANNEE/NUMEROTATION`, où :

- CODE correspond au code définit pour le journal
- Année correspond à l'année de la date de saisie de la pièce
- NUMEROATION correspond à une numérotation continue (sans intervalles entre chaque pièces générées) sur 5 caractères  .

Suggestions de séquences à utiliser pour vos différents journaux :

| Code | Type de séquence | Type | Mise en oeuvre | Préfixe | Taille de la séquence |
| --- | --- | --- | --- | --- | --- |
| VTE | Factures clients | Vente | Sans espace | VTE/%(range_year)s/ | 5 |
| ACH | Factures fournisseurs | Achat | Sans espace | ACH/%(range_year)s/ | 5 |
| AVC | Avoir clients | Vente | Sans espace | AVC/%(range_year)s/ | 5 |
| AVF | Avoir fournisseurs | Achat | Sans espace | AVF/%(range_year)s/ | 5 |
| ACG | Achats Généraux | Achat | Sans espace | ACG/%(range_year)s/ | 5 |
| OD | Opérations Diverses | Divers | Sans espace | OD/%(range_year)s/ | 5 |
| BQE | Banque | Banque | Sans espace | BQE/%(range_year)s/ | 5 |
| PAY | Paiements en attente | Caisse | Sans espace | PAY/%(range_year)s/ | 5 |
| ESP | Espèce | Banque | Sans espace | ESP/%(range_year)s/ | 5 |
| SAL | Salaires | Salaire | Sans espace | SAL/%(range_year)s/ | 5 |
| TVA | TVA sur encaissement | Divers | Sans espace | TVA/%(range_year)s/ | 5 |

## Comment modifier la séquence d'un journal ?

Vous pouvez consulter les séquences d'un journal depuis le formulaire de ce journal.

Vous pouvez également retrouver la liste de l'ensemble des séquences** en mode développeur** depuis le menu suivant : `Configuration > Techniques > Séquences et identifiants`.

![](https://support.openfire.fr/hc/article_attachments/21535189331740)

### Créer et Éditer une Séquence

| 🚨**Avertissement** : vérifier la bonne installation du module account_move_name_sequence afin d'accéder à la configuration des séquences de chaque journal depuis le journal. ![](https://support.openfire.fr/hc/article_attachments/21535217781404) |
| --- |

Cliquer sur le bouton **Nouveau** pour ajouter une nouvelle séquence, ou cliquer sur une séquence existante pour la modifier.

#### Au niveau de l'en-tête

**Nom** : Le libellé de la séquence. Il est conseillé de reprendre le nom du journal associé.

**Mise en œuvre** :

- **Standard** : Numérotation standard, sans vérification de la continuité.
- **Sans espace** : Numérotation continue, n'autorisant pas les écarts.

**Codes de séquencement** : Ce code permet d'attribuer la séquence à un objet spécifique (ex: `sale.order` pour les bons de commande).

**Active** : Si cette case est cochée, la séquence est utilisable.

**Société** : La société dans laquelle la séquence sera disponible.

#### Au niveau de l'onglet "Séquence"

**Préfixe** : Chaîne de caractères précédant la numérotation. Vous pouvez inclure des éléments de date (année, mois, jour). Référez-vous à la légende disponible dans la plateforme pour savoir comment compléter ce champ.

**Suffixe** : Chaîne de caractères suivant la numérotation. Vous pouvez également inclure des éléments de date. Référez-vous à la légende disponible dans la plateforme pour savoir comment compléter ce champ.

**Taille de la séquence** : Le nombre de chiffres composant la numérotation.

**Étape** : Le nombre par lequel le prochain numéro de séquence sera incrémenté.

**Utiliser des sous-séquences par intervalle de date** : Cette option permet d'ajuster la séquence en tenant compte de critères de temps. Si elle est cochée, une nouvelle table apparaît, vous permettant de sélectionner les intervalles et le prochain numéro par intervalle.

| 💡**Note **: La date prise en compte pour le choix de la plage de date est la date de la facture, et non la date du jour de la saisie. |
| --- |

## Bonnes pratiques

---

- **Nommage clair** : Donnez des noms explicites à vos journaux et séquences pour faciliter l'identification.
- **Cohérence des codes** : Assurez-vous que les codes de journal sont uniques et ne sont pas modifiés une fois que des écritures y sont saisies.
- **Séparation des achats** : Distinguez les journaux d'achats d'exploitation et d'achats généraux pour une gestion plus fine.
- **Mode développeur** : Activez le mode développeur uniquement lorsque vous avez besoin de configurer des aspects techniques comme les séquences.
- **Vérification de la chronologie** : Si la conformité de la chronologie des factures est essentielle pour votre entreprise, assurez-vous que le module nécessaire est installé et que l'option est activée sur les journaux concernés.

## Pour aller plus loin

---

| 📓**Pour aller plus loin** →  Modes de paiement manuels 📓**Pour aller plus loin **→ Facturation électronique (à venir) |
| --- |

Mis a jour le : 07/08/2025
