---
source: https://support.openfire.fr/hc/fr/articles/19085649027484-Saisir-une-intervention-sur-le-planning
categorie: Utiliser OpenFire
titre: Saisir une intervention sur le planning
date_recuperation: 2026-09-05
---

# Saisir une intervention sur le planning

Cet article vous décrit les principaux champ du RDV d'intervention afin de vous aider dans la saisie de votre planning.

Cet article contient les sections suivantes :

- [Accéder au planning](#h_01KCRWMWRBY9N7CQ8216J0MK5X)
- [Saisir l'en-tête d'une intervention](#h_01KCRWF7CG4791CWB54C7AXY7B)
- [Détailler la planification ](#h_01KCRWF7CRS8PDMABJQP5EVA61)

  - [Où (Localisation)](#h_01KCRY49K72MQWWWA3YPB7ADVW)
  - [Qui (Intervenants)](#h_01KCRY4CPE74JYF6RYXDASSFY0)
  - [Quoi (contenu)](#h_01KCRY4FQWAZD2VKTWQJMX185N)
  - [Quand (Planification temporelle)](#h_01KCRY4K19M9R7SYJG156A7FVC)
  - [Le cas des RDV figés ou flexibles](#h_01KCS0F9WZVNSX1BPRTHHSF3YF)
  - [Le cas des RDV récurrents](#h_01KCS18AS0BHN669XG2RPBPRJ9)
- [Les onglets de l'intervention](#h_01KCRWF7DFQ7SER74365KPVKA2)

  - [L'onglet Infos Générales](#h_01KCS50F4W7G5Q8G9F20WJK7XR)
  - [L'onglet Ventes](#h_01KCS8Y87ERECHMT9RQJP0GVB3)
  - [L'onglet Paiement](#h_01KCS8Y87EZ5SEEYVWMNZA1EEP)
  - [L'onglet Photos](#h_01KCS8Y87EJ256WCEDE6R995ZM)
  - [L'onglet Compte-rendu](#h_01KCS8Y87EP40WB3Q6JJ7FGH94)
  - [L'onglet Questionnaire](#h_01KCS8Y87EA9TDZCC3V0RH853X)
- [Les statuts de l'intervention](#h_01JVY2DFN5EP9H1MAW8RQHWF3K)
- [Pour aller plus loin](#h_01KCS7HE33EEEEE07H0PD9TABC)

# Accéder au planning

*Chemin d’accès au planning d’intervention* :
**Plan Basique** : `Interventions > Mon planning d'intervention`
**Autres plans** : `Interventions > Iinterventions > Planning`

*Pour créer une nouvelle intervention, vous pouvez : *

- Cliquez sur le bouton **Nouveau**
- Cliquer sur le bouton **+** directement dans le créneau concerné

# Saisir l'en-tête d'une intervention

Cette section définit les informations principales visibles sur votre planning.

![](https://support.openfire.fr/hc/article_attachments/24335496807068)

- **Titre de l'intervention** : libellé visible sur le planning. Il se génère automatiquement à la sauvegarde selon le schéma **NOM - MODÈLE D'INTERVENTION**, mais reste modifiable.
- **Type d'évènement** : vous permet de choisir entre créer un évènement ou une intervention selon votre besoin.

| 📓**Pour aller plus loin** → [Evènement ou Intervention ?](https://support.openfire.fr/hc/fr/articles/24330699101724) |
| --- |

| 💡**Note **: le présent article traite de la création des RDV de type intervention |
| --- |

- **Modèle d'intervention** : le modèle d'intervention est un champ obligatoire et essentiel dans le processus de saisie d'une intervention. Il permet de définir notamment : 

  - La tâche et la durée par défaut de l'intervention.
  - Le questionnaire d'intervention ou de satisfaction.
  - Les règles de gestion et d'impression du rapport d'intervention.
  - Les règles de générations des devis et factures associées à ces interventions.

| 📓**Pour aller plus loin** → Configurer vos modèles d'intervention |
| --- |

- **Organisateur** : créateur du rendez-vous ou responsable du planning.

| 🚨**Avertissement** : L'organisateur n'est pas l'intervenant ! |
| --- |

- **Demande d'intervention** : à renseigner si le rendez-vous est lié à une demande existante.
- **Étiquettes** : permettent de transmettre des informations à l'intervenant. Elles sont visibles sur l'application mobile.

| **🧑‍🏫Exemple** : Le technicien peut ajouter des étiquettes depuis le terrain pour informer le planificateur (ex: POÊLE CHAUD). |
| --- |

# Détailler la planification

## Où (Localisation)

![](https://support.openfire.fr/hc/article_attachments/24338393611804)

- **Client** : contact concerné par le rendez-vous. Les étiquettes du client sont automatiquement reprises et affichées dans chaque intervention.
- **Adresse** : lieu de l'intervention. Elle peut différer de l'adresse du client (ex. : locataire).
- **Secteur** : renseigné selon le client et son code postal de l'adresse.

| 📓**Pour aller plus loin** → Configurer vos secteurs d'intervention |
| --- |

## Qui (Intervenants)

![](https://support.openfire.fr/hc/article_attachments/24338393613212)

- **Équipe** : sélection d'un groupe d'intervenants.
- **Techniciens** : liste des intervenants. S'ils sont correctement configurés, ils accèdent au rendez-vous sur leur mobile.
- **Technicien principal** : celui sur lequel le rendez-vous apparaît graphiquement au planning.

| 📓**Pour aller plus loin** → Configurer vos employés 📓**Pour aller plus loin** → Configurer vos équipes d'intervention |
| --- |

## Quoi (Contenu)

![](https://support.openfire.fr/hc/article_attachments/24338407237148)

- **Équipements** : cocher la case pour choisir un ou plusieurs équipements déjà enregistrés pour l'adresse d'intervention indiquée.

| 📓**Pour aller plus loin** → Créer un équipement 📓**Pour aller plus loin** → Saisir une intervention multi-équipement |
| --- |

- **Type** : définit la nature de la mission (**Entretien-Maintenance**, **Installation**, **SAV**, **Visite technique**). Le type est utile pour l'affichage, la recherche ou les statistiques.
- **Tâche** : action précise à réaliser au travers de l'intervention. La tâche est généralement définie directement dans le modèle d'intervention. Si la tâche est toujours identique au modèle d'intervention, l'option de gestion des tâches simplifiées permet de masquer ce champ.

| 📓**Pour aller plus loin** → Configurer vos tâches |
| --- |

- **Durée** : se remplit automatiquement selon la tâche mais reste modifiable manuellement.

## Quand (Planification temporelle)

![](https://support.openfire.fr/hc/article_attachments/24338407239452)

Renseigner le **Début le** (date et heure).

La date **Se terminant à** se calcule seule selon la durée mais peut être ajustée.

**Toute la journée** : utilise les horaires du technicien principal pour calculer l'heure de début et l'heure de fin de l'intervention.

**Forcer les dates** : permet de planifier en dehors des horaires de travail, ou en forçant le créneau pourtant en conflit de date avec une autre intervention.

Lorsqu'un conflit de RDV est détecté, un avertissement est affiché pour l'utilisateur.

![](https://support.openfire.fr/hc/article_attachments/24338407245212)

## Le cas des RDV figés ou flexibles

Vous pouvez définir si l'horaire de votre intervention est flexible ou s'il a fait l'objet d'un accord exprès avec votre client. On parle alors de RDV figé. Un RDV flexible favorisera les opérations d'optimisation de tournée, à l'inverse des RDV figés.

Dans le champ **Figer la date et l'heure**, plusieurs options sont disponibles** :**

| **Choix** | **Description** | **Impacts techniques** | Impact sur les règles d'optimisation |
| --- | --- | --- | --- |
| **Ne pas figer** | L'intervention est libre. | Elle peut être déplacée ou réorganisée automatiquement. |  |
| **Première intervention de la journée** | Bloque l'intervention au tout début du planning du technicien. | L'heure de début s'aligne sur l'heure de démarrage du technicien. Les champs de date deviennent non modifiables | Si une intervention est figée en **Première** ou **Dernière** position de la journée, l'optimisation de tournée utilisera l'adresse de ce client comme point de départ (ou d'arrivée) réel de la tournée du technicien |
| **Dernière intervention de la journée** | Bloque l'intervention en fin de journée. | L'heure de fin correspond à l'heure de fin de service du technicien. L'heure de début est déduite selon la durée. |
| **Dernière**** intervention de la matinée** | Bloque l'intervention en fin de matinée | L'heure de fin de l'intervention correspond à l'heure de fin de travail du matin du technicien | Si une intervention est figée en fin de matinée et/ou en début d'après-midi, le mode d'optimisation "Journée entière" ne sera pas disponible. Seuls les modes "À la demi-journée", "Matin" ou "Après-midi" seront applicables |
| **Première intervention de l'après-midi** | Bloque l'intervention en début d'après-midi | L'heure de début d'intervention correspond à l'heure de démarrage de l'après-midi du technicien |
| **Figer à une heure précise** | Verrouille le rendez-vous à l'horaire exact saisi. | L'optimisation ne touchera pas à ce créneau. Utile pour les rendez-vous avec un impératif horaire fort. | Si une intervention est figée **à une heure précise en milieu de demi-journée**, alors :  seule l’autre demi-journée reste optimisable, si deux demi-journées sont figées, l’optimisation n’est plus disponible. |

| 💡**Note **: Sur l'application mobile, le technicien retrouve également le champ **Figer la date et l'heure** dans la section **Date**. Seules les options encore disponibles s'affichent (ex. : si une "Première de la journée" existe déjà, l'option disparaît). |
| --- |

Dans le planning, les interventions figées :

- Apparaissent avec une icône cadenas.![](https://support.openfire.fr/hc/article_attachments/24338393618716)
- Ne peuvent pas être "drag & drop" ni de technicien, ni de date.
- Ne peuvent pas être étendues ou rétrécies.

## Le cas des RDV récurrents

Cocher la case **Récurrent ?** permet de définir une répétition (jour, semaine, mois, année) pour une intervention.

Trois critères sont configurables :

- **la répétition** : chaque jour, chaque semaine, chaque mois, chaque année ;
- **les jours **(si la répétition est semaine) : les jours sur lesquels votre client est disponible ;
- **la date de fin de la répétition** : en nombre de répétitions, avec une date fin ou sans date de fin.

![](https://support.openfire.fr/hc/article_attachments/24338407250716)

# Les onglets de l'intervention

L'intervention est composée de six onglets pour gérer les aspects gravitant autour du rendez-vous.

## L'onglet Infos Générales

Cet onglet regroupe :

![](https://support.openfire.fr/hc/article_attachments/24338969657244)

**1/** Les différentes origines possibles de l'intervention :  **opportunités**, les **Commandes**, les **Bons de livraison **ou encore les** contrats. **

**2**/ Les **Description interne** (pour le technicien) et **Description externe** (pour le client).

![](https://support.openfire.fr/hc/article_attachments/24338969658524)

**3**/ les différents **documents personnalisés** à joindre à l'impression des rapports d'intervention selon les paramètres d'impression.

![](https://support.openfire.fr/hc/article_attachments/24338938464028)

![](https://support.openfire.fr/hc/article_attachments/24338938464284)4/ le **Type analytique** de l'intervention, à utiliser pour vos statistiques. Le type analytique est souvent utilisé pour différencier vos différentes activités (Exemple : Solaire / Bois-Energie / ...)

5/ Les **sections à afficher dans l'intervention** sur le mobile. Ces sections sont définies dans le modèles d'intervention.

## L'onglet Ventes

On retrouve ici les principales informations requises pour la générations des ventes additionnelles générées depuis cette intervention, notamment :

- Le compte analytique ;
- Le détail des devis / commandes générés depuis l'intervention ;
- Le statut de facturation de l'intervention, basée sur le statut de facturation des commandes associées.

![](https://support.openfire.fr/hc/article_attachments/24338938465436)

| 📓**Pour aller plus loin** → Gérer et planifier un SAV 📓**Pour aller plus loin** → Contrat simplifié : l'utilisation des DI récurrente |
| --- |

## L'onglet Paiement

Vous retrouvez ici le **montant de la commande** à l'origine de l'intervention, son montant restant dû et la valeur totale des bons de livraison associés.

![](https://support.openfire.fr/hc/article_attachments/24338973052316)

## L'onglet Photo

Vous retrouvez ici l'ensemble des photos prises au cours de l'intervention.

Nous distinguons :

- Les photos de **L'INTERVENTION **: ces photos sont prises depuis l'application mobile, au niveau de l'intervention. Une photo peut-être ajoutée manuellement à cet endroit.
- Les photos du **QUESTIONNAIRE **: ces photos sont prises depuis l'application mobile, depuis une question du questionnaire de l'intervention.
- **Photos** : centralise les images prises sur mobile ou ajoutées manuellement.

![](https://support.openfire.fr/hc/article_attachments/24339321032988)

## L'onglet Compte-rendu

Les informations de cet onglet sont complétées automatiquement à la fin de l'intervention sur mobile. Il contient le compte-rendu du technicien, les **Dates et durées réelles** (début, fin, pause) et les **Signatures** (technicien et client).

![](https://support.openfire.fr/hc/article_attachments/24339302105884)

## L'onglet Questionnaire

Vous retrouvez ici le questionnaire associé à l'intervention, à laquelle le technicien en intervention devra répondre depuis son application mobile.

Le questionnaire est normalement défini directement au niveau du modèle d'intervention.

Les réponses apportées par le techniciens seront visibles sur chacune des lignes. Les photos associées aux questionnaires sont, elles, visibles depuis l'onglet **Photo **de l'intervention.

![](https://support.openfire.fr/hc/article_attachments/24339321033756)

La complétion du questionnaire peut également se faire directement depuis le web, en cliquant sur le bouton **REPONDRE **présent en haut à gauche du questionnaire.

![](https://support.openfire.fr/hc/article_attachments/24339302106268)

Une interface Web dédiée est alors disponible pour vous permettre de répondre.

![](https://support.openfire.fr/hc/article_attachments/24339321034780)

# Les statuts de l'intervention

Le statut reflète l’avancement opérationnel de l’intervention.

Les principaux statuts de l'intervention sont les suivants :

| **Nom** | **Type** | **Contexte métier** |
| --- | --- | --- |
| **Brouillon ** | Auto | Il s'agit du premier statut de l'intervention. Les dates et les modalités de l'intervention en sont pas encore confirmées, que ce soit en interne ou vis à vis du client. |
| **Confirmé** | Manuel | L'intervention est validée, auprès du client notamment.  Certains paramètres peuvent automatiser la confirmation d'un RDV, notamment dans le contexte de la recherche de créneau ou de la prise de RDV en ligne. |
| **En cours ** | Auto | L'intervention est en cours de réalisation sur le mobile |
| **Non terminé ** | Auto |  |
| **Terminé** | Manuel / Auto | L'intervention a été réalisée |
| **Reporté** | Manuel | L’intervention n'a pas eu lieu et est à reprogrammer |
| **Annulé ** | Manuel | L’intervention a été annulée |
| **En cours d'optimisation** | Auto |  |
| **Clôturé** | Manuel | Le traitement et le suivi de l'intervention sont terminés, plus aucune action n'est requise sur cette dernière. |

Le statut de l'intervention est présenté dans le formulaire de l'intervention ainsi que sur l'ensemble des vues des interventions (liste, kanban, planning, etc.).

![](https://support.openfire.fr/hc/article_attachments/24339720651036)

# **Pour aller plus loin**

| 📓Pour aller plus loin → Configurer vos modèles d'intervention 📓Pour aller plus loin → Configurer vos employés |
| --- |

Mis a jour le : 04/02/2026
