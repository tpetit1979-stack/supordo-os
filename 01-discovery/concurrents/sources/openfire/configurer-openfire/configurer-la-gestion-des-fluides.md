---
source: https://support.openfire.fr/hc/fr/articles/21549285255452-Configurer-la-gestion-des-fluides
categorie: Configurer OpenFire
titre: Configurer la gestion des fluides
date_recuperation: 2026-09-05
---

# Configurer la gestion des fluides

Cet article vous guide dans le paramétrage initial d'OpenFire pour activer la gestion des fluides frigorigènes. Cette étape est indispensable pour générer vos Cerfa 15497 et assurer votre conformité réglementaire.

Cet article contient les sections suivantes :

- [Vérification des prérequis](#h_01KNVZ61R7SPDCZK7W3CYAE8DA)
- [Paramétrage de la société (Attestation de capacité)](#h_01KNVY55EE4E6YFJX4CSYEAFS6)
- [Connexion à Trackdéchets](#h_01KNVY55EK2JXMZA6S4DQATBCM)
- [Configuration du matériel de détection de fuite](#h_01KNVY55EQ6Y18FF5GBBMWERBS)

## Vérification des prérequis

Avant de commencer, vous devez vous assurer que les fonctionnalités "Fluides" sont bien activées sur votre base de données.

- Connectez-vous à votre instance OpenFire.
- Vérifiez la présence du menu **Bouteilles** ou **Bilan des fluides** dans le module **Intervention**.

| 💡**Note **: Si vous ne voyez pas ces menus, cela signifie que les modules spécifiques ne sont pas encore installés sur votre base. |
| --- |

| 🚨**Avertissement** : L'activation de ces fonctionnalités nécessite l'intervention de nos équipes techniques. Si les menus ne sont pas visibles, **rapprochez-vous de notre support client** pour demander l'installation du module de gestion des fluides. |
| --- |

## Paramétrage de la société

Avant de réaliser vos premières interventions, vos informations d'attestation doivent être renseignées pour apparaître sur les documents officiels.

`Suivre le chemin d'accès suivant : Configuration > Utilisateurs & Société > Société`

- Sélectionner votre société.
- Dans l'onglet **Attestations**, remplir les champs suivants :

  - **Cerfa 15497 - N° d'attestation de capacité** : Votre numéro officiel.
  - **Organisme de délivrance** : Le nom de l'organisme qui vous a certifié.
- Vérifier que votre **SIRET**, **E-mail** et **Téléphone** sont bien renseignés dans l'onglet **Informations générales**.

| 🚨**Avertissement** : Ces coordonnées sont obligatoires pour la liaison avec Trackdéchets. Une erreur ici bloquera la création de vos bordereaux. |
| --- |

## Connexion à Trackdéchets

OpenFire permet de dématérialiser vos bordereaux de suivi de fluides (BSFF). Pour cela, vous devez lier votre compte Trackdéchet.

- Posséder un compte actif sur la plateforme [Trackdéchets](https://www.google.com/search?q=https://trackdechet.beta.gouv.fr/).
- `Suivre le chemin d'accès suivant : Configuration > Paramètres généraux`
- Faire défiler jusqu'à la section **Intégrations**.
- Cliquer sur le bouton **AUTHENTIFICATION** dans le bloc **Authentification Trackdéchets**.

| 💡**Note **: Si vous ne parvenez pas à vous authentifier, contactez le support OpenFire pour vérifier que l'URL de votre base est bien autorisée dans l'application tierce Trackdéchets. |
| --- |

## Configuration du catalogue Produits

Pour gagner du temps et éviter les erreurs de saisie, vous pouvez configurer les données techniques directement sur vos fiches produits.

`Suivre le chemin d'accès suivant : Ventes > Produits > Produits`

- Sur la fiche du produit, définissez le **Secteur technique** sur **Climaticien **dans l'onglet **Données techniques**.
- Une fois activé, complétez les champs techniques qui s'affichent :

  - **Système permanent de détection de fuite** : Cocher si l'appareil en est équipé de série.
  - **Nature de fluide** : Sélectionner le gaz utilisé.
  - **Charge de l'équipement (kg)** : Indiquer la charge nominale d'usine.
  - **Tonnage équivalent CO2** : Le logiciel le calcule automatiquement.

| 💡**Note **: Lorsqu'un équipement client est créé à partir de ce produit, il récupère **automatiquement** l'ensemble de ces informations. |
| --- |

## Configuration des données techniques de l'équipement

La fiche de l'équipement centralise les données réelles de l'installation pour le calcul du Cerfa.

`Suivre le chemin d'accès suivant : Intervention > Parc de matériel > Équipements`

- Dans l'onglet **Données techniques**, vérifiez les informations héritées du produit et complétez les champs si nécessaire :

  - **Système permanent de détection de fuite**.
  - **Nature de fluide**
  - **Charge de l'équipement (kg)** :
  - **Charge complémentaire (kg)** : Indiquer la charge additionnelle ajoutée lors de l'installation (liaisons frigorifiques par exemple).
  - **Tonnage équivalent CO2** : Recalculé automatiquement sur la base de la **Charge totale **et de la** nature du fluide sélctionné**.

| 💡**Note **: Le champ **Charge totale** est la somme de la **charge de l'équipement** et de la **charge complémentaire**. Ce champ est non modifiable pour garantir la fiabilité des données. |
| --- |

### Autonomie du technicien sur le terrain

Si l'équipement n'a pas été configuré au préalable par le bureau, le technicien conserve une totale autonomie :

- **Saisie mobile** : L'ensemble de ces champs techniques peuvent être complétés par le technicien directement depuis son application mobile au moment de l'intervention.
- **Activation immédiate** : Dès que la **Nature de fluide** et la **Charge de l'équipement** sont renseignées et enregistrées sur le mobile, le rapport **CERFA 15497** peut être complété.

## Configuration du matériel de détection de fuite

La réglementation impose de préciser quel appareil a été utilisé pour le contrôle d'étanchéité.

`Suivre le chemin d'accès suivant : Intervention > Configuration > Matériel`

- Cliquer sur **Créer**.
- Renseigner le **Nom** de l'appareil (ex: Détecteur TESTO 316-3).
- Sélectionner le type **Détecteur de fuite**.
- **Important** : Dans le champ **Employé**, sélectionner le technicien qui utilisera cet appareil.

| **🧑‍🏫Exemple** : Si vous avez 5 techniciens équipés, vous devez créer 5 fiches matériel et assigner chaque appareil à son utilisateur respectif. Cela permettra au technicien de retrouver son matériel automatiquement sur son application mobile. |
| --- |

## Bonnes pratiques

- **Vérifiez les dates** : Assurez-vous que les dates de validité de vos attestations de capacité sont à jour dans la fiche Société.
- **Secteur d'activité** : Vérifiez que vos équipements clients sont bien liés au secteur d'activité **Climaticien** pour que les onglets de gestion des fluides s'affichent.

| 📓**Pour aller plus loin** → [Gérer le parc de bouteilles de fluides](https://support.openfire.fr/hc/fr/articles/26708133196828) |
| --- |

| 📓**Pour aller plus loin** → [Remplir un Cerfa 15497 depuis l'application mobile](https://support.openfire.fr/hc/fr/articles/26774989574300) |
| --- |

Mis a jour le : 14/04/2026
