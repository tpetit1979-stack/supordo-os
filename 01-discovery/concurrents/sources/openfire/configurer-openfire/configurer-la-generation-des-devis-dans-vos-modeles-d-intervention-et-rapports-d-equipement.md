---
source: https://support.openfire.fr/hc/fr/articles/23705389072412-Configurer-la-g%C3%A9n%C3%A9ration-des-devis-dans-vos-Mod%C3%A8les-d-Intervention-et-Rapports-d-%C3%89quipement
categorie: Configurer OpenFire
titre: Configurer la génération des devis dans vos Modèles d'Intervention et Rapports d'Équipement
date_recuperation: 2026-09-05
---

# Configurer la génération des devis dans vos Modèles d'Intervention et Rapports d'Équipement

Cet article a pour objectif de vous guider pas à pas dans la configuration des options de génération de devis au sein de vos **Modèles d'Intervention** et **Rapports d'Équipement** sur OpenFire. Ces paramètres vous permettent d'automatiser et de standardiser la manière dont les devis sont créés à partir des interventions, facilitant ainsi le travail de vos équipes terrain et administratives.

# Sommaire

Cet article contient les sections suivantes :

- [**Configuration dans les Modèles d'Intervention**](#h_01KAECD0KFY7FJZHY106WXDVWN)
- [**Configuration dans les Rapports d'Équipement**](#h_01KAECD0M1D150N7H2KX5N88NW)
- [**Bonnes Pratiques**](#h_01KAECD0M64BRPAY1435018K9X)
- [**Pour aller plus loin**](#h_01KAECD0M6VYTFV63V5JM10SQA)

---

# Configuration dans les Modèles d'Intervention

La configuration des Modèles d'Intervention est cruciale pour la gestion des devis et de la facturation liés à vos interventions de terrain.

## Accéder à l'onglet Ventes

Suivre le chemin d'accès suivant : `Interventions > Configuration > Interventions > Modèles d'intervention`

1. Sélectionner le Modèle d'Intervention à modifier.
2. Cliquer sur l'onglet **Ventes**.

![](https://support.openfire.fr/hc/article_attachments/24471071269404)

## Définir le Modèle de devis

Ce champ définit le modèle de devis (mise en page, conditions, etc.) qui sera utilisé par défaut pour générer un devis depuis une Intervention (ou Demande d'Intervention).

- **Action :** Sélectionner le modèle de devis qui correspond le mieux à ce type d'intervention (ex. : SAV, maintenance, diagnostic, etc.).

| 🚨**Avertissement** : Si ce champ n'est pas renseigné, aucun modèle ne sera prérempli lors de la création manuelle d'un devis. |
| --- |

| 💡**Conseil** : Définissez toujours un modèle de devis pour permettre la génération rapide de devis depuis vos interventions. |
| --- |

## Choisir la Méthode de génération

La méthode de génération détermine si la création du devis sera manuelle (déclenchée par l'utilisateur) ou automatique (déclenchée par la confirmation de l'intervention).

| **Méthode** | **Comportement** | **Utilisation recommandée** |
| --- | --- | --- |
| **Manuelle** | L'utilisateur doit cliquer sur un bouton pour déclencher la création du devis. | Interventions nécessitant une validation (ex. : SAV) avant de chiffrer. |
| **À la validation** | **Pour les DI non récurrentes** : le devis est généré automatiquement dès que la demande d'intervention est confirmée.   **Pour les DI récurrentes** : le devis est généré automatiquement dès que l'intervention est confirmée. | Interventions standardisées avec un devis systématique et prédéfini. |

| 🧑‍🏫**Exemple** :  **Manuelle :** Diagnostic sur place, l'utilisateur crée le devis après l'état des lieux. **À la validation :** Contrat de maintenance avec un forfait prédéfini. |
| --- |

## Confirmer automatiquement le devis généré

Ce champ n'apparaît que si vous avez choisi la méthode **À la validation**. Il permet d'accélérer le processus en confirmant automatiquement le devis.

- **Activé :** Le devis est généré **ET** confirmé automatiquement en bon de commande. C'est un gain de temps pour les processus très standardisés.
- **Désactivé :** Le devis est généré en brouillon. Cela permet une validation manuelle ou un ajustement avant d'être confirmé.

| 💡**Note** : Un devis confirmé n'est plus éditable depuis l'application terrain. |
| --- |

| 🧑‍🏫**Exemple** :  **Activé :** Intervention SAV sous garantie avec un devis à 0 €. **Désactivé :** Devis de pièces détachées nécessitant une validation finale du technicien. |
| --- |

## Choisir la politique de facturation

(à venir)

## Limiter les articles dans les devis

Cette option contrôle quels articles de votre base de données peuvent être ajoutés manuellement aux devis générés depuis ce modèle.

- **Ne pas limiter les articles :**

  - **Fonctionnement :** Tous les articles de votre base peuvent être ajoutés par l'utilisateur.
  - **Cas d'usage :** Dépannage avec pièces imprévisibles, interventions de diagnostic, offrant une flexibilité maximale.
- **Limiter aux articles supplémentaires :**

  - **Fonctionnement :** Seuls les articles définis dans la liste (ci-dessous) peuvent être ajoutés. Si la liste est vide, aucun article supplémentaire ne peut être ajouté.
  - **Avantages :** Standardisation des devis, réduction des erreurs de saisie et guidage des techniciens sur le terrain (sur mobile, ces articles sont proposés par défaut lors de la recherche).
  - **Cas d'usage :** Maintenance préventive ou contrats avec un catalogue d'articles très défini.

| 🧑‍🏫**Exemple** : Pour un Modèle d'Intervention Maintenance chaudière, vous pourriez limiter aux articles suivants :  **Filtre standard** **Joint de culasse** **Détartrant** **Main d'œuvre maintenance** |
| --- |

---

# Configuration dans les Rapports d'Équipement

La configuration au niveau du Rapport d'Équipement permet de proposer des lignes de commandes spécifiques basées sur le type d'équipement.

## Accéder à la configuration

Suivre le chemin d'accès suivant : `Intervention > Configuration > Équipement > Rapports d'équipement`

## Sélectionner le Modèle de devis

Dans l'onglet **Ventes**, le champ **Modèle de devis** ne sert ici qu'à définir les lignes de commandes associées à l'équipement.

- **Action :** Sélectionner un modèle de devis qui contient uniquement les lignes de commandes (articles) standards pour ce type d'équipement.

| 💡**Note **: Le modèle sélectionné ici **n'applique PAS** ses paramètres généraux (position fiscale, conditions de règlement, etc.) au devis final. Ces informations doivent être définies dans le Modèle d'Intervention ou ajustées manuellement. |
| --- |

Les **Lignes de commandes** affichées sont en lecture seule et ne peuvent être modifiées qu'en éditant le modèle de devis source. Ces lignes seront **proposées** automatiquement à l'utilisateur lors de la génération du devis, qui pourra choisir de les inclure ou non.

---

# Bonnes Pratiques

- **Standardisation :** Utilisez la fonctionnalité **Limiter aux articles supplémentaires** pour les interventions récurrentes. Cela garantit l'exactitude des devis et guide vos techniciens.
- **Simplicité :** Si une intervention nécessite toujours la même facturation, utilisez la **Méthode de génération "À la validation"** et l'option **Confirmer automatiquement** pour un maximum d'automatisation.

---

# Pour aller plus loin

| 📓**Pour aller plus loin** → [Créer et gérer vos Modèles de devis] |
| --- |

| 📓**Pour aller plus loin** → [Gérer les devis et les commandes sur l'Application Mobile OpenFire](https://support.openfire.fr/hc/fr/articles/23706295298844) |
| --- |

Mis a jour le : 01/09/2026
