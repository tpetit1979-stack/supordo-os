---
source: https://support.openfire.fr/hc/fr/articles/24467930558748-Contrat-simplifi%C3%A9-g%C3%A9rer-vos-contrats-de-maintenance-avec-les-Demandes-d-Intervention-DI-R%C3%A9currentes
categorie: Utiliser OpenFire
titre: Contrat simplifié : gérer vos contrats de maintenance avec les Demandes d’Intervention (DI) Récurrentes
date_recuperation: 2026-09-05
---

# Contrat simplifié : gérer vos contrats de maintenance avec les Demandes d’Intervention (DI) Récurrentes

Cet article vous explique comment gérer de manière simplifiée vos** contrats de maintenance annuelle**, grâce aux **Demandes d’Intervention Récurrentes (DIR)**, en détaillant les mécanismes de planification et de facturation disponibles depuis les demandes d'intervention.

Cet article contient les sections suivantes :

- [Prérequis](#h_01KDD5638Y2297HSK2S62NZVW6)
- [Comprendre le fonctionnement du contrat simplifié](#h_01KDD5TPAEDT0JHQQECWFQM089)
- [Créer et configurer une Demande d'Intervention Récurrente](#h_01KDD7J8V956VY22BDFWXKGTPE)
- [Planifier les interventions du contrat](#h_01KDDJQWFTCVQNWHT43AS5NGSA)
- [Automatiser la création des commandes du contrat](#h_01KDDR5GDAFRT4X77W3MEEB771)
- [Réaliser et facturer vos contrats d'interventions](#h_01KDDR9DVH9ADV6VGMZXSG0MXX)
- [Renouveler ou terminer votre contrat](#h_01KDDW0BV161VHKA44F03CTGRK)
- [Bonnes pratiques](#h_01KDDPRYB9G87YS7RDTGZC8R3Z)

---

## Prérequis

| 🧩**Prérequis** →   [Planifier vos contrats d’entretien : choisir entre le mode simple ou avancé](https://support.openfire.fr/hc/fr/articles/24467159028380) |
| --- |

## Comprendre le fonctionnement du contrat simplifié

La gestion des contrats simplifiés dans OpenFire repose sur les quatre piliers suivants :

- **Demande d’intervention (DI) Récurrente :** C'est le réservoir de vos interventions à venir. Elle définit la période cible, le modèle d'intervention et la fréquence (récurrence).
- **RDV d’intervention :** Il correspond au créneau dans votre planning où la prestation est planifiée puis réalisée.
- **Bon de commande :** Il valide le prix de la prestation et sert de support à la facturation.
- **Facture client :** L'étape finale de votre cycle de vente.

| 💡**Note **: Dans ce mode de gestion, la **Demande d'intervention récurrente** est le point de départ de tout votre flux de travail. |
| --- |

Principes de fonctionnement : 
- Votre **contrat **(ou prestation) **est enregistré** en tant que demande d’intervention récurrente, et sert de base à la planification de vos interventions année après année.
- À **chaque planification**, OpenFire **génère **automatiquement** le bon de commande** associé.
- Le bon de commande peut être validé automatiquement ou non suivant la configuration retenue.
- A la **réalisation **de **l’intervention**, la **facture est générée** (sur la base de la commande client associée). Cette facturation est réalisée depuis le mobile ou depuis le web.

Schéma de fonctionnement :

![](https://support.openfire.fr/hc/article_attachments/24470770973980)

## Créer et configurer une DI récurrente

`Suivre le chemin d'accès suivant : Interventions > Demandes d'intervention > Créer`

Pour mettre en place votre contrat, vous devez créer correctement votre DI :

- Saisir le **Titre de la demande d'intervention** (ex. : Contrat d'entretien annuel poêle à granulés)
- Choisir le **Modèle d’intervention** correspondant (ex. : Contrat d’entretien Granulés)

![](https://support.openfire.fr/hc/article_attachments/24471185998492)

- Cocher la case **Récurrence** dans l'onglet **QUAND**
- Définir la fréquence dans le champ **Répéter chaque** (ex: 1 An)
- Préciser le **Mois** cible de l'intervention (ex. : Décembre), et les plages de dates associées (ex. : **Entre le **01/12/2025 **et le **31/12/2025)

![](https://support.openfire.fr/hc/article_attachments/24471178292124)

Pensez à bien valider votre DI une fois configurée.

![](https://support.openfire.fr/hc/article_attachments/24471227662876)

| 💡**Note **: Assurez-vous que le **Modèle d'intervention** choisi est correctement configuré pour générer automatiquement les commandes client afin de gagner du temps lors de la planification. Voir ci-dessous. |
| --- |

| 📓**Pour aller plus loin** → Créer et suivre vos demandes d'intervention (à venir) |
| --- |

## Planifier les interventions du contrat

`Suivre le chemin d'accès suivant : Interventions > Demandes d'intervention`

Chaque année (ou à chaque récurrence du contrat) vous devez planifier l'intervention associée. Pour planifier votre contrat, vous pouvez :

1. Soit** PLANIFIER L'INTERVENTION** depuis la DI, en utilisant la fonctionnalité de recherche de créneau
2. Soit saisir directement l'intervention dans le planning, en prenant le soin de bien associer l'intervention à sa DI récurrente d'origine

![](https://support.openfire.fr/hc/article_attachments/24473113549724)

Vous pouvez retrouver l'historique des interventions dans les smart boutons de la DI récurrente.

| 📓**Pour aller plus loin** → Les différentes méthodes de planification d'une intervention (en cours) 📓**Pour aller plus loin** → [Rechercher un créneau disponible ](https://support.openfire.fr/hc/fr/articles/19085638198684) |
| --- |

## Automatiser la création des commandes du contrat

Chaque année (ou à chaque récurrence du contrat), nous recommandons la création d'un bon de commande client distinct. Ce bon de commande permet notamment :

- De servir de support à la facturation.
- De prévoir le chiffre d'affaire à facturer.

Les règles de création de la **commande à chaque planification **sont déterminées au niveau du **modèle d'intervention** retenue. Vous pouvez notamment :

- Définir le **modèle de devis** à utiliser et les conditions tarifaires à appliquer.
- **Automatiser la création** du devis à chaque planification (**🧑‍🏫Exemple :** Vous programmez un ramonage chaque année en octobre. Dès que vous fixez le rendez-vous dans le planning pour l'année N+1, OpenFire crée tout seul le bon de commande de 180 € prêt à être facturé après votre passage.)
- **Automatiser **la **confirmation **du devis à sa création (dans le cadre d'un contrat, la confirmation du devis n'est pas obligatoire puisque le client a déjà signé son contrat).

![](https://support.openfire.fr/hc/article_attachments/24471554873500)

Au niveau du*** modèle de devis*** associé, vous pouvez également choisir la **politique de facturation*** "**à chaque prestation**"*, pour permettre de conditionner la facturation de la commande à la réalisation effective de l'intervention.

![](https://support.openfire.fr/hc/article_attachments/24471554874268)

**Lors de la confirmation d'un rendez-vous d'intervention en lien avec votre DI**, OpenFire génèrera donc automatiquement le bon de commande associé, que vous pouvez retrouver :

- Dans le smart bouton ***Commande ***de l'intervention et de la demande d'intervention.

![](https://support.openfire.fr/hc/article_attachments/24473168382876)

- Dans l'onglet ***Ventes ***de l'intervention et de la demande d'intervention.

![](https://support.openfire.fr/hc/article_attachments/24472537543452)

| 💡**Note **: au niveau de la **demande d'intervention**, vous retrouvez, année après année, l'historique de l'ensemble des commandes réalisées en lien avec ce contrat. |
| --- |

| 📓**Pour aller plus loin** → [Configurer la génération des devis dans vos Modèles d'Intervention et Rapports d'Équipement](https://support.openfire.fr/hc/fr/articles/23705389072412) |
| --- |

## Réaliser et facturer vos contrats d'interventions

La **facturation **de vos contrats simplifiés (ou DI récurrentes) se fait **via les bons de commande** puisque une commande est générée pour chaque intervention.

Si vous avez choisi la politique de facturation "***À la prestation***" pour votre devis, ce dernier ne sera facturable qu'une fois l'intervention réalisée.

Le statut de facturation est disponible directement depuis la commande, la DI récurrente ou l'intervention associée.

![](https://support.openfire.fr/hc/article_attachments/24473236999324)

Pour facturer votre intervention :

1. Accéder à la DI ou à l'intervention à facturer.
2. Remonter à la commande associée.
3. Facturer la commande, de manière classique.![](https://support.openfire.fr/hc/article_attachments/24473277431580)

💡**Astuces **: vous pouvez retrouver, depuis la liste des DI ou des interventions, toutes celles ***à facturer*** en utilisant le filtre dédié :

| 📓**Pour aller plus loin** → Facturer vos interventions (à venir) |
| --- |

## Renouveler ou terminer votre contrat

Une fois votre DI récurrente configurée, OpenFire prend le relais pour le **renouvellement des années suivantes** (vous n'avez pas d’action particulière à faire).

Concrètement, à chaque planification, OpenFire va **recalculer la date de prochaine planification** de la DI récurrente au premier jour du prochain mois de prestation, selon les règles de récurrence que vous avez définies.

**🧑‍🏫Exemple** : votre contrat prévoit l'entretien de la chaudière de votre client chaque mois de décembre, une fois l'entretien planifié pour le mois de décembre de l'année en cours (2025 dans notre exemple), OpenFire recalculera la date de prochaine intervention au 01/12/2026.

![](https://support.openfire.fr/hc/article_attachments/24473364130844)

**Si votre contrat se termine**, vous pouvez simplement décocher la case Récurrence de votre DI récurrente. Le statut de planification de la DI passera alors à terminer, et ce dernier sortira de la liste de vos contrats à planifier.

## Bonnes pratiques

Pour exploiter au mieux la gestion simplifiée de vos contrats, nous vous recommandons d'appliquer les conseils suivants :

- **Standardiser vos titres de DI :** Utilisez une nomenclature claire comme `[Type de contrat] - [Nom du client] - [Équipement]` (ex. : "Entretien Annuel - BEGOOD - Poêle Granulés") pour faciliter vos recherches dans la liste des interventions.
- **Vérifier la date de prochaine planification :** Après avoir planifié un rendez-vous, retournez brièvement sur la DI récurrente pour vérifier que la section **QUAND** a bien été mise à jour pour l'année suivante. C'est la garantie que votre contrat ne sera pas oublié.
- **Utiliser les étiquettes :** Marquez vos clients avec des étiquettes comme **Sous contrat** ou **PAG** (Poêle à Granulés). Cela vous permet de filtrer rapidement votre base de données pour des opérations de communication ou de relance.

💡Note : Si vous avez un grand volume de contrats (plus de 500), envisagez de passer au **Mode Avancé** pour bénéficier d'outils de génération de masse plus puissants.

Mis a jour le : 29/12/2025
