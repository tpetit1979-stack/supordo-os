---
source: https://support.openfire.fr/hc/fr/articles/26708133196828-G%C3%A9rer-le-parc-de-bouteilles-de-fluides
categorie: Configurer OpenFire
titre: Gérer le parc de bouteilles de fluides
date_recuperation: 2026-09-05
---

# Gérer le parc de bouteilles de fluides

La gestion rigoureuse de vos bouteilles est le cœur de votre traçabilité. Cet article vous explique comment créer vos contenants, suivre les volumes de gaz et assurer la passation entre vos techniciens et le stock central.

Cet article contient les sections suivantes :

- [Création d'une bouteille (Back Office)](#h_01KNW0ESFQ7NBFBD4QRJ26YHR8)
- [Suivi et mouvements de fluides](#h_01KNW0ESFX3MKQDR3YCCDF8XCV)
- [Gestion des bouteilles sur l'application mobile](#h_01KNW0ESFZP9TCYX54FWRFEDJS)
- [Cas particulier : L'import initial de vos stocks](#h_01KNW0ESG1R5TRMFJ86CHX0VTR)

## Création d'une bouteille sur l'application bureau

Chaque bouteille présente dans votre entreprise doit posséder sa fiche propre pour permettre un suivi précis du volume et du type de fluide.

`Suivre le chemin d'accès suivant : Intervention > Configuration > Bouteilles`

- Cliquer sur **Créer**.
- Renseigner les informations obligatoires :

  - **Nom** : Indiquez l'identifiant unique marqué sur la bouteille.
  - **Fluide** : Sélectionnez la nature du gaz (ex: R32, R410A).
  - **Capacité totale** : La contenance maximale de la bouteille en litres.
  - **Type de fluide** : Précisez s'il s'agit de fluide **Neuf** ou **Usagé** (récupéré).
- **Assigner la bouteille (Optionnel)** : Dans le champ **Employé**, vous pouvez sélectionner le technicien qui transporte la bouteille.

| 💡**Note **: L'assignation est un outil de confort. ** Si la bouteille est assignée** : Elle n'apparaîtra **que** pour ce technicien sur son application mobile. ** Si la bouteille n'est pas assignée** : Elle reste disponible pour **n'importe quel technicien** de l'entreprise. |
| --- |

## Suivi et mouvements de fluides

OpenFire calcule automatiquement le niveau de vos bouteilles au fil des interventions :

- **Capacité totale** : Il s'agit du volume maximal (en litres) que peut contenir la bouteille.
- **Quantité contenue** : C'est la quantité de fluide présente dans la bouteille à un instant T. Ce chiffre diminue lors d'une charge et augmente lors d'une récupération.

| 🚨**Avertissement** : Si vous constatez une erreur dans la **Quantité contenue**, deux solutions s'offrent à vous pour la corriger : ** Modifier le rapport d'intervention** : Si l'erreur provient d'une saisie erronée lors d'un dépannage ou d'une maintenance. ** Créer une transaction de "Correction"** : Directement sur la fiche de la bouteille. Une **Description de la correction** vous sera alors obligatoirement demandée pour justifier cet ajustement dans votre traçabilité. |
| --- |

## Gestion des bouteilles sur l'application mobile

Le technicien peut consulter ses bouteilles et en ajouter de nouvelles en cas d'achat direct chez un fournisseur.

- Ouvrir le menu **Bouteilles** sur l'application mobile.
- Pour ajouter une bouteille : Cliquer sur **+** ou **Ajouter**.
- Renseigner le nom, le type de fluide et la quantité initiale.

| 💡**Note **: Les bouteilles créées sur mobile sont automatiquement assignées au technicien connecté. |
| --- |

## Cas particulier : L'import initial de vos stocks

Lors de votre démarrage sur OpenFire, vous devez déclarer vos stocks existants sans fausser votre bilan annuel.

`Suivre le chemin d'accès suivant : Intervention > Configuration > Bouteilles`

- Utilisez le type de transaction **Import bouteille**.
- Cette fonction permet de définir la **Quantité contenue** dans la bouteille au moment du lancement sans que ce volume ne soit comptabilisé comme un "achat" de l'année en cours.

| ** 🧑‍🏫Exemple** : Si vous commencez à utiliser OpenFire en juin avec une bouteille déjà entamée contenant 3 litres, l'import permet d'initialiser ce stock sans impacter vos statistiques d'acquisition de fluides de l'année. |
| --- |

## Bonnes pratiques

- **Archivage** : Lorsqu'une bouteille est vide et rendue au fournisseur, archivez sa fiche pour ne plus l'afficher dans les listes actives.
- **Contrôle** : Comparez régulièrement la **Quantité contenue** théorique dans OpenFire avec le niveau réel de vos bouteilles pour identifier d'éventuels oublis de saisie.

| 📓**Pour aller plus loin** → [Configurer la gestion des fluides](https://support.openfire.fr/hc/fr/articles/21549285255452) |
| --- |

| 📓**Pour aller plus loin** → [Remplir un Cerfa 15497 depuis l'application mobile](https://support.openfire.fr/hc/fr/articles/26774989574300) |
| --- |

Mis a jour le : 14/04/2026
