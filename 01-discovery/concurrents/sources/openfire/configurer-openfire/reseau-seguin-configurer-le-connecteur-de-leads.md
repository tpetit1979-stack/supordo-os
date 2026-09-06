---
source: https://support.openfire.fr/hc/fr/articles/25649042113692-R%C3%A9seau-Seguin-Configurer-le-connecteur-de-leads
categorie: Configurer OpenFire
titre: Réseau Seguin: Configurer le connecteur de leads
date_recuperation: 2026-09-05
---

# Réseau Seguin: Configurer le connecteur de leads

Cet article vous présente la fonctionnalité "**Connecteur de leads**".

Elle est accessible aux professionnels du réseau Seguin.

Cette fontionnalité vous permet de recevoir des opportunités envoyées par le groupe Seguin directement dans votre CRM OpenFire et d'actualiser le statut de votre opportunité dans OpenFire automatiquement sur le Cloud Seguin.

| 🧩**Prérequis** →             [Créer une opportunité](https://support.openfire.fr/hc/fr/articles/19075730913948-Cr%C3%A9er-une-opportunit%C3%A9) |
| --- |

Cet article contient les sections suivantes:

- [Configurer le connecteur de leads Seguin](#h_01KHXH8RHV5Z4SYN28CSS0J5BV)
- [Identifier les leads reçus du Cloud Seguin](#h_01KHXH8RHV40GPMD10STK3CJM6)
- [Mettre à jour les étapes de son pipeline](#h_01KHXH8RHVDWY6STA9WFTJ6A8A)
   

  ## Configurer le connecteur de leads Seguin

| 💡**Note **: L'utilisation du connecteur de             leads Seguin             nécessite l'installation d'un module spécifique. Nous vous             invitons à formuler votre demande à support@openfire.fr pour             être accompagné dans cette démarche.                                   L'accès au connecteur             de leads est soumis à l'autorisation préalable du groupe Seguin. |
| --- |

Chemin d'accès: *Paramètres > Paramètres des connecteurs > Configurer les connecteurs Seguin*

![](https://support.openfire.fr/hc/article_attachments/25649027224604)

- **URL de l'API Seguin: **Cette URL est communiquée par Seguin.

![](https://support.openfire.fr/hc/article_attachments/25649042110748)

| 💡**Note **: Si vous êtes en multi-sociétés,             vous pouvez choisir de configurer un connecteur différent             par société. Sinon, laissez le champ "Société associée au connecteur" à vide. |
| --- |

![](https://support.openfire.fr/hc/article_attachments/25649042110876)

- **Utilisateur Seguin: **Cet utilisateur dans votre base de donnée a été créé spécifiquement lors du processus d'installation du connecteur. Cet utilisateur ne doit pas être supprimé ni archivé.
- **Société associée au connecteur: **Il s'agit de la société pour laquelle les paramètres du connecteur de lead s'appliquent. Si ce champ est laissé vide, toutes les sociétés auront la même configuration.
- **Token: **Mot de passe crypté, fourni par Seguin lors de la configuration du connecteur
- **Actions automatisées API: **Il s'agit des actions dans votre base qui viendront déclencher la mise à jour de l'opportunité dans le Cloud Seguin. Par défaut, 3 actions déclenchent la mise à jour du statut de l'opportunité dans le Cloud Seguin: 

  - la mise à jour du statut de l'opportunité  (Visite Technique, Gagné, Perdu, ...)
  - La création d'un bon de commande pour cette opportunité
  - La création d'un rendez-vous d'intervention pour cette opportunité

  🕐 La synchronisation entre le statut de votre opportunité dans OpenFire et le statut de l'opportunité dans le Cloud Seguin est effectuée deux fois par jour: le matin à 11h30 et le soir à 20h30.

Chemin d'accès: *CRM > Configuration > Sources*

![](https://support.openfire.fr/hc/article_attachments/25649042111260)

La source Cloud Seguin a été créée lors de la configuration du connecteur. Cette source viendra s'ajouter sur les opportunités qui ont été envoyées automatiquement dans votre CRM OpenFire par Seguin.

---

## Identifier les opportunités reçues du Cloud Seguin

*Chemin d'accès : CRM  > Ventes > Mon pipeline*

![](https://support.openfire.fr/hc/article_attachments/25649042111900)

Les opportunités reçues automatiquement grâce au connecteur de leads s'identifient:

- Par le **vendeur: **Il s'agit de l'utilisateur qui a été créé lors de la configuration du connecteur.
- Par la **source: **Il s'agit de la source qui a été créée lors de la configuration du connecteur
- Par la présence de l'**identifiant Seguin: **Il s'agit de la référence de l'opportunité sur le Cloud Seguin

![](https://support.openfire.fr/hc/article_attachments/25649027226012)

## Mettre à jour les étapes de son pipeline

Chemin d'accès: *CRM > Configuration > Etapes*

Cette configuration s'effectue accompagné de votre chef de projet ou de l'équipe support.

![](https://support.openfire.fr/hc/article_attachments/25649445947292)

À chaque étape de votre pipeline doit être associée un des 9 statuts disponibles dans le Cloud Seguin, à savoi:

- Gagné
- Perdu
- Faux: il s'agit d'une opportunité factice / d'un test
- Devis
- Rendez-vous
- Qualification en cours / lead contacté
- Répondeur
- À recontacter
- Faux numéro

| 🚨**Avertissement** : Si vous ajoutez une nouvelle étape à votre pipeline, pensez à actualiser la correspondance avec le statut Seguin. |
| --- |

Mis a jour le : 20/03/2026
