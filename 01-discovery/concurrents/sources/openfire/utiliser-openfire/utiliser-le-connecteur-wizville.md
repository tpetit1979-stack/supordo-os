---
source: https://support.openfire.fr/hc/fr/articles/26309314521756-Utiliser-le-connecteur-Wizville
categorie: Utiliser OpenFire
titre: Utiliser le connecteur Wizville
date_recuperation: 2026-09-05
---

# Utiliser le connecteur Wizville

Wizville est une solution d’enquête de satisfaction en continu pour les réseaux de points de vente permettant aux clients de partager leur avis en répondant à un court questionnaire de satisfaction.

Dans le cadre de son partenariat avec OpenFire, Jøtul a souhaité développer un connecteur Wizville pour vous permettre de solliciter des avis clients, directement depuis votre base OpenFire, suite à la pose d'un appareil Jøtul, et de réceptionner les avis clients émis.

**Cette fonctionnalité est dédiée aux concessionnaires Jøtul. Elle nécessite l'installation d'un module dédié. Pour cela, vous rapprocher de support@openfire.fr**

| 🧩**Prérequis** →             [Configurer le connecteur Wizville Jøtul ](https://support.openfire.fr/hc/fr/articles/26297092194332) |
| --- |

Cet article contient les sections suivantes:

- [Export: Sélection des clients à solliciter via Wizville](#h_01KMDKNP01NTG98HP6RQQ4SDPG)
- [Import: intégration des réponses des clients collectées par Wizville](#h_01KMDKNP01NTG98HP6RQQ4SDPG)

---

### Export: Sélection des clients à solliciter via Wizville

OpenFire se base sur vos factures clients pour identifier les clients à solliciter.

Les clients à solliciter sont les suivants:

- Client pour lequel on a émis une facture concernée par le filtre défini dans votre configuration Wizville (voir l'article Configurer le connecteur Wizville Jøtul).
- Client pour lequel une adresse mail a été renseignée
- Client n'ayant pas la case "Contact Wizville refusé" cochée

![](https://support.openfire.fr/hc/article_attachments/26309621050780)

Lorsqu'une facture a été sélectionnée pour une sollicitation Wizville, elle est marquée comme "Envoyée à Wizville":

![](https://support.openfire.fr/hc/article_attachments/26309610977820)

Cette information est également notifiée dans les notes de la facture.

![](https://support.openfire.fr/hc/article_attachments/26309621053212)

Tous les jours à 3h du matin, le logiciel recherche les clients éligibles et génère un fichier d'export.

Les fichiers d'export générés sont visibles via le menu *Paramètres > Wizville > Historique*

Le fichier généré est déposé sur le serveur Wizville et permet de contacter les clients concernés.

Lorsqu'un fichier d'export a été déposé sur le serveur Wizville, il est indiqué comme "Traité".

![](https://support.openfire.fr/hc/article_attachments/26309621055516)

### Import: intégration des réponses des clients collectées par Wizville

Tous les jours à 4h du matin, le logiciel recherche si des réponses ont été obtenues par Wizville sur des sollicitations clients. Si tel est le cas, le logiciel crée une nouvelle entrée de type "Import" dans l'historique des imports/exports Wizville.

Les réponses sont renseignées dans la fiche Client, onglet "Informations Wizville"

![](https://support.openfire.fr/hc/article_attachments/26309610985884)

Mis a jour le : 18/06/2026
