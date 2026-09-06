---
source: https://support.openfire.fr/hc/fr/articles/22807168780828-Contrat-avanc%C3%A9-Cr%C3%A9er-vos-contrats-de-maintenance-et-d-entretien
categorie: Utiliser OpenFire
titre: Contrat avancé : Créer vos contrats de maintenance et d'entretien
date_recuperation: 2026-09-05
---

# Contrat avancé : Créer vos contrats de maintenance et d'entretien

Cet article a pour objectif de vous accompagner dans la création de vos **contrats de maintenance** sur OpenFire. Vous y découvrirez comment configurer les informations essentielles de votre contrat, de la facturation à la planification des interventions, et comment automatiser ces processus pour gagner en efficacité.

Cet article contient les sections suivantes :

- [Prérequis](#h_01KB3REDYK7HE9XY85ZB17WKY3)
- [Principe d'utilisation](#h_01KB3REDYK7HE9XY85ZB17WKY3)
- [Créer votre contrat](#h_01K6ZN9A8P37VBQ7CZAJMBY7WD)
  - [Identifier votre client](#h_01K6ZYNZ6J70R56TN19NNXRRP3)
  - [Qualifier votre contrat](#h_01K6ZVDFDBSK1VZD8HD4NWA3VN)
  - [Gérer les dates de votre contrat](#h_01K7044MHSA62EH1DGYJN7MZ0K)
  - [Configurer les règles de facturation et de regroupement](#h_01K70DNXCXNRJK6A6HPNTKZYHN)
  - [Configurer les règles d'impression de votre contrat](#h_01KB3ZT1FXJ44CYE6NDPR8HB14)
- [Créer vos lignes de contrat](#h_01K70AZXDGRVSA34D6586H36D8)
  - [Définir le site d'intervention](#h_01K70BD7G2EHWHKBTSHRNM2B7B)
  - [Vérifier les dates de facturation](#h_01K70C109A6RHV9483WAJXQQGN)
  - [Sélectionner le produit ou la prestation à facturer](#h_01K70CJN527X691QTMGBZ7PKVG)
  - [Prévoir les interventions du contrat](#h_01K70HWHSH96S3432Y1EDRCD68)
- [Bonnes pratiques](#h_01K6ZN9A9GK65NV0DCK3WYF8CM)
- [Pour aller plus loin](#h_01K6ZN9A9JN32C9NQ20NJFQZY3)

---

## Prérequis

| 🧩**Prérequis** →   Quelle méthode choisir pour gérer mes contrats d'entretien ? (en cours) |
| --- |

## Principe d'utilisation

Le contrat de maintenance permet de centraliser l'ensemble des informations de facturation et de planification de l'ensemble des prestations récurrentes que vous effectuez pour votre client dans le cadre de votre contrat.

Depuis le contrat, vous pourrez :

- Générer l'ensemble des demandes d'interventions relatives aux prestations à effectuer pour l'année de contrat en cours.
- Générer toutes les commandes clients (ou toutes les factures directement) relatives aux prestation à facturer pour l'année de contrat en cours.

## Créer votre contrat

Suivez le chemin d'accès suivant : le contrat peut être accessible à deux endroits distincts :

`Ventes > Commandes > Contrat `

`Interventions > Interventions > Contrat`

Un contrat regroupe l'ensemble des informations de facturation et de planification de l'ensemble des prestations récurrentes que vous effectuez chez votre client. Pour un même client, vous pouvez :

- **Option 1** : Créer un seul contrat global pour votre client, en utilisant une ligne de contrat distincte pour chaque site d'intervention.
- **Option 2** : Créer un contrat différent pour chaque équipement, site d'intervention ou type de prestation.

| 💡**Note **: Pour plus de simplicité, nous vous recommandons de créer un contrat par client, en regroupant toutes les prestations qui partagent les mêmes modalités de facturation (même fréquence, même type de facturation). Ainsi, un client peut avoir plusieurs contrats si ses besoins de facturation sont différents. |
| --- |

Créer votre contrat en cliquant sur le bouton **Créer** en haut à gauche de votre écran.

| 💡**Note **: Pour simplifier la création de contrat, vous pouvez dupliquer vos contrats et vos lignes de contrat. Pensez à bien vérifier chaque contrat ou ligne de contrat dupliqué(e) pour ne pas propager des erreurs de saisies. |
| --- |

### Identifier votre client

Un contrat est toujours lié à un client principal, renseigné dans le champ **Partenaire**. Il peut concerner plusieurs sites d'intervention, que vous définirez dans les différentes lignes de contrat.

Le champ **Contact de facturation** vous permet de désigner un contact spécifique pour la facturation, si ce dernier est différent du client principal. Ce contact sera automatiquement repris dans les commandes et factures générées par le contrat.

![](https://support.openfire.fr/hc/article_attachments/22810231945884)

Pour le suivi analytique, vous pouvez également lui attribuer Un **Groupe **(ou compte analytique), qui permettra de regrouper tous les produits et toutes les charges du contrat pour en suivre la rentabilité au fur et à mesure de sa réalisation.

| 💡**Note **: Nous vous recommandons de générer un compte analytique par contrat et par période annuelle afin de simplifier l'analyse de la rentabilité de ce dernier. |
| --- |

Pour la création d'un compte analytique, nous vous recommandons de suivre ces bonnes pratiques :

- **Nom du compte analytique** : Reprenez le nom commercial du contrat et ajoutez-y sa période d'application.
- **Client** : Indiquez le nom du client signataire du contrat.
- **Référence** : Utilisez la référence du contrat ou du bon de commande initial.
- **Plan analytique** : Sauf si vous avez une configuration spécifique, utilisez le plan par défaut.

![](https://support.openfire.fr/hc/article_attachments/22810016706716)

| 📓**Pour aller plus loin** → Créer un compte analytique (à venir) |
| --- |

### Qualifier votre contrat

Afin d'identifier et de qualifier vos contrats, vous pouvez utiliser les champs suivants :

**Identification du contrat : **

- **Nom du contrat** : La désignation commerciale du contrat que vous partagez avec votre client (ex. : "Contrat Sérénité", "Contrat Performance").
- **Référence client** : Le numéro du contrat ou du bon de commande initial que vous partagez avec votre client.
- **Référence interne** : Un identifiant unique pour votre entreprise, jamais partagé avec le client.
- **Type de contrat** : Indiquez s'il s'agit d'une première souscription ou d'un renouvellement.

**Classification et analyse : **

- **Type analytique** : Catégorisez vos contrats pour mieux différencier vos activités et analyser la rentabilité.

| **🧑‍🏫Exemple** : Vous pouvez créer des types analytiques par type d'appareil (Entretien poêle à bois, Maintenance climatisation) ou pour distinguer l'activité de maintenance des autres services de votre entreprise. |
| --- |

- **Étiquettes** : Attribuez des étiquettes personnalisées pour qualifier et filtrer vos contrats selon vos besoins.

![](https://support.openfire.fr/hc/article_attachments/22810151637660)`n*Exemple de qualification d'un contrat*`n

### Gérer les dates de votre contrat

Pour un pilotage efficace de vos contrats, il est essentiel de bien en maîtriser les dates.

Voici les différentes dates que l'on retrouve :

- **Date de souscription **: Date à laquelle le contrat a été signé ou accepté
- **Date de début** : Date à laquelle le contrat et la facturation associée débute.

| 💡**Note **: Nous vous recommandons, pour simplifier le suivi de votre contrat et autant que possible, de travailler sur des périodes contractuelles pleines d'un an, et de démarrer votre contrat le premier jour du mois de référence. Exemple : date de début : 01/07/2025 |
| --- |

- **Date de fin **: Correspond à la date de fin du contrat, et donc la fin de la période de facturation. Ce champ peut rester vide si cette date n'est pas connue d'avance.
- **Date de la prochaine facture** : Cette date est calculée automatiquement par OpenFire, en tenant compte de la date de début du contrat, la récurrence du contrat et le type de facturation.
- **Dernière date facturée** : cette date correspond à la date de la dernière facture générée en lien avec le contrat. À la création du contrat ce champ est donc vide.

![](https://support.openfire.fr/hc/article_attachments/22811502416284)

### Configurer les règles de facturation et de regroupement

Afin de configurer correctement les règles de facturation de vos contrats, il est essentiel de bien comprendre les deux notions suivantes :

#### Type de document générés par le contrat : commande ou facture ?

Ce paramètre détermine le type de document créé par le contrat pour supporter la facturation :

- **Factures** : Le contrat génère directement des factures.
- **Ventes** : Le contrat génère des commandes clients pour la période en cours. Ces commandes devront ensuite être facturées. Si vous choisissez de générer des **Ventes**, vous pouvez également choisir de les confirmer automatiquement en cochant la case **Confirmation automatique des commandes.**

| 💡**Note **: Nous vous recommandons de choisir la génération de ***ventes** *plutôt que celle de ***factures ***pour les raisons suivantes :  **Facilite l'analyse du prévisionnel de facturation** sur la période puisque l'ensemble des ventes à date de facturation cible auront été générées dès le début de la période. **Uniformise vos processus** : toute la facturation de l'entreprise s'appuie sur un seul et même flux : la facturation des bons de commande. **Simplifie la gestion des exceptions** en cours de contrat (avoirs, reports, etc.). |
| --- |

#### Mode de facturation : récurrent ou à la prestation ?

Le mode de facturation définit la manière dont les commandes (ou les factures) associées à la période du contrat sont générées. Deux options sont disponibles :

##### **Option 1 : Facturation récurrente**

La commande (ou la facture) est établie suivant une périodicité régulière (mensuelle, trimestrielle, annuelle). Chaque commande (ou facture) est associée à une récurrence du contrat.

Pour configurer la récurrence, vous devez définir :

- La **fréquence **de la répétition (tous les "n" jours / mois / trimestres / semestres / années)
- Le t**ype de facturation : **
  - À échoir : la commande (ou la facture) est générée au début de la période
  - Échu : la commande (ou la facture) est générée à la fin de la période

![](https://support.openfire.fr/hc/article_attachments/23885703646236)

| **🧑‍🏫Exemple** :   Si facturation annuelle en début d'année : **Facturer toutes les** 1 année - pré-payé Si facturation trimestrielle en fin de trimestre : **Facturer tous les** 1 trimestre - post-payé Si facturation tous les 2 mois en début de période : **Facturer tous les** 2 mois - pré-payé Si facturation mensuelle en fin de mois : **Facturer tous les** 1 mois - post-payé |
| --- |

##### **Option 2 : Facturation à la prestation**

La commande est établie en début de période du contrat. Chaque commande est associée à une intervention précise à réaliser dans le cadre du contrat. La commande deviendra facturable à la réalisation de la prestation.

| 💡**Note **: Dans le cadre d'un contrat **À la prestation**, le type de document à générer ***Ventes*** est imposé, afin de permettre au système de faire précisément le lien entre l'intervention prévue et la commande utilisée pour sa facturation ; la date de facturation prévisionnelle de la commande sera alors la date planifiée de l'intervention. |
| --- |

#### Critères de regroupement

**Regrouper la facturation** : Ce champ vous permet de choisir comment regrouper les lignes de contrat dans un même document de vente :

- **Ne pas regrouper** : Chaque ligne de contrat génère son propre devis ou facture.
- **Par contact de facturation** : Les lignes de contrat ayant le même contact de facturation sont regroupées.
- **Par contact de facturation et adresse d’intervention** : Les lignes de contrat avec le même contact de facturation et la même adresse d’intervention sont regroupées.

| 💡**Note **: Si votre contrat comprend plusieurs lignes, vous pouvez définir des règles de facturation spécifiques pour chacune d'elles. Toutefois, pour simplifier la gestion, il est recommandé de regrouper dans un même contrat uniquement les prestations qui partagent les mêmes modalités de facturation. |
| --- |

### Configurer les règles d'impression de votre contrat

L'onglet **Impression** vous permet de personnaliser l'apparence des documents générés.

- **Période du contrat** : Cochez cette option si vous souhaitez que la période de facturation affichée sur la commande ou la facture soit la période totale du contrat, et non pas la période de l'échéance en cours. Exemple : pour un contrat avec la période 01/01/2025 - 31/12/2025 et avec une récurrence mensuelle : 
  - Facturer en Mars devrais afficher la période 01/03/2025 - 31/03/2025.
  - Avec cette option, la période 01/01/2025 - 31/12/2025 sera affichée à la place.
- **Documents personnalisés** : Ajoutez des documents (CGV, brochures, etc.) à votre devis ou facture.

L'onglet **Commentaire **vous permet d'ajouter des notes personnalisées qui apparaîtront en haut ou en bas des documents générés, à l'image de ce qui existe déjà pour les commandes ou les factures clients.

## Créer vos lignes de contrat

Les lignes de contrat vous permettent de définir les services ou les produits à inclure dans votre contrat. Vous pouvez ajouter plusieurs lignes à un même contrat.

Chaque ligne de contrat peut avoir sa propre configuration, notamment pour le mode de facturation : vous pouvez surcharger la configuration du contrat et choisir un mode de facturation spécifique pour cette ligne (**Récurrent** ou **À la prestation**).

### Définir le site d'intervention

Pour chaque ligne de votre contrat, vous pouvez définir une adresse d'intervention différente.

Dans le cadre d'un contrat multisites : Une ligne = Un site d'intervention.

![](https://support.openfire.fr/hc/article_attachments/22812608124444)

| 💡**Note **: dans le cadre de contrat de maintenance multisites, vous pouvez définir un code magasin directement dans la fiche de chaque site d'intervention. Ce code permet de simplifier l'identification du magasin auprès de ses partenaires (clients & sous-traitants) et sera repris sur les différents documents associés au contrat (commandes, factures, demandes d'intervention...) |
| --- |

### Vérifier les dates de facturation

Pour chaque ligne de contrat, vous pouvez vérifier les dates de référence utilisées pour la génération des documents de vente (commande ou facture).

- Les **dates **de **début **et de **fin **sont reprises du contrat.
- Les **dates de prochaine période** (début et fin) définissent la prochaine période de facturation de la ligne de contrat.

| **🧑‍🏫Exemple** : imaginez un contrat débutant le 01/01/2025, avec une facturation trimestrielle à échoir. La prochaine période de facturation sera la première du contrat, soit du 01/01/2025 au 31/03/2025. À ce stade, aucune facture ou commande n'a encore été générée. ![](https://support.openfire.fr/hc/article_attachments/22812762983068) |
| --- |

- La date de **Dernière facture** correspond à la date de la dernière facturée générée en lien avec le contrat et la ligne de contrat.
- La date de **Dernière commande **est calculée par OpenFire, et reprend la date de la dernière commande générée en lien avec le contrat.
- Le **décalage de facturation** correspond au nombre de jours de décalage entre la facture et la fin de la période (en mode post-payé) ou début de la période (en mode pré-payé) de facturation. => A vérifier

### Sélectionner le produit ou la prestation à facturer

Pour chaque ligne, vous pouvez sélectionner **le produit **à facturer.

![](https://support.openfire.fr/hc/article_attachments/22812746802588)

Un système de balise peut-être utilisé pour enrichir la **description **de la prestation, en permettant d'y ajouter certaines informations clés du contrat. Vous pouvez retrouver la liste de ces balises directement dans l'onglet **"Autres informations"** du contrat.

![](https://support.openfire.fr/hc/article_attachments/25162748129948)

| **🧑‍🏫Exemple** d'une description permettant de reprendre, dans la commande générée par le contrat, la période de facturation, le nom et le code du site d'intervention :  Période facturée : du #DATE DEBUT# au #DATE FIN#  Site facturé : #ADRESSE# (code magasin : #CODE ADRESSE#) |
| --- |

Vous devez ensuite définir les éléments de prix de la prestation :

Le** Prix Unitaire **(calculé directement par application de la liste de prix du contrat au produit sélectionné), le **Coût **et l'**Unité de mesure **du produit ainsi que la **Remise **éventuelle.

| 🚨**Avertissement** : Les quantités et les prix que vous définissez sur chaque ligne de contrat doivent correspondre à vos échéances de facturation (ou de génération de commande). **🧑‍🏫Exemple** Si votre contrat a une valeur annuelle de 600 € et qu'il est facturé au trimestre, les valeurs à renseigner seront : **Quantité** : 1 et **Prix unitaire** : 150 € |
| --- |

### Prévoir les interventions du contrat

L'onglet **Planification** vous permet de définir les modalités de création des **Demandes d'Intervention (DI)** liées à votre contrat.

- **Modèle d’intervention** : Le type d'intervention à réaliser (ex. : "Maintenance annuelle").
- **Fréquence** et **Type de fréquence** : La fréquence et le type de planification de vos interventions (ex. :"2" "fois par an").
- **Mois de visite** : Les mois spécifiques de l'année durant lesquels les interventions doivent avoir lieu.
- **Équipements** : Les équipements sur lesquels les interventions seront effectuées.

![](https://support.openfire.fr/hc/article_attachments/22813294873628)

## Bonnes pratiques

- **Renseignez les champs obligatoires** : Assurez-vous que les champs obligatoires, comme l'**Adresse d’intervention** sur les lignes de contrat, sont bien remplis avant de générer des documents.
- **Utilisez les variables d'impression** : 💡Note : vous pouvez insérer des variables dans la description de vos produits pour qu'elles se complètent automatiquement dans les documents générés.
  - `#SITE INTERVENTION#` : l'adresse de l'intervention
  - `#DATE DEBUT#` : la date de début du contrat

## Pour aller plus loin

📓Pour aller plus loin → Comprendre les statuts d'une Demande d'Intervention

Mis a jour le : 29/01/2026
