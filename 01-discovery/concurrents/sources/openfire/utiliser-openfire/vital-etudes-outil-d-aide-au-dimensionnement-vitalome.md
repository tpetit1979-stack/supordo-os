---
source: https://support.openfire.fr/hc/fr/articles/25322865422748-VITAL-ETUDES-Outil-d-aide-au-dimensionnement-Vitalome
categorie: Utiliser OpenFire
titre: VITAL-ETUDES : Outil d'aide au dimensionnement Vitalome
date_recuperation: 2026-09-05
---

# VITAL-ETUDES : Outil d'aide au dimensionnement Vitalome

Cet article vous explique comment utiliser l'outil d'aide au dimensionnement Vitalome VITAL-ETUDES.

L'outil VITAL-ETUDES vous donne accès à un formulaire d'aide au dimensionnement sur l'application mobile OpenFire. Ce formulaire complété permet la génération semi-automatique d'un devis ainsi que d'un rapport de calepinage et dimensionnement.

📱Cet outil est disponible uniquement sur la version mobile d'OpenFIre.

| 🧩**Prérequis** →             [Se connecter à l'application mobile ](https://support.openfire.fr/hc/fr/articles/19088383198876) |
| --- |

- [Créer une intervention de type dimensionnement Vitalome](#h_01KGQ8XX1QV3JVGY3DK7HEJTY4)
  - [Créer une intervention depuis l'ordinateur](#h_01KGQ8ZCF0V4YHXQAFA9K1RTEJ)
  - [Créer une intervention depuis l'application mobile](#h_01KGQ8ZCF0V4YHXQAFA9K1RTEJ)
- [Compléter le formulaire de dimensionnement](#h_01KGQ9KAC2H43PE9RSXDJ8XXH5)
- [Générer le devis associé](#h_01KGQAP71S914XJ4EZFDTZP5DZ)
  - [Avertissements à la génération du devis](#h_01KGQEQN491QZ1Z4DCZTN2BPSY)
  - [Modifier le devis généré](#h_01KGQETYAFV8NJJZT0AE507KTX)
  - [Imprimer le devis](#h_01KGQG0SDWXNZZ4SMBZJWJS7T2)
- [Générer le rapport d'intervention (calepinage et dimensionnement)](#h_01KGQFW7Z4Z5PYD218KGP26745)

## Créer une intervention de type dimensionnement Vitalome

Pour commencer à remplir un formulaire de dimensionnement, vous devez créer une intervention.

Vous pouvez créer votre intervention depuis votre base OpenFire, ou bien directement depuis le mobile.

- [Créer une intervention depuis l'ordinateur](#h_01KGQ8ZCF0V4YHXQAFA9K1RTEJ)
- [Créer une intervention depuis l'application mobile](#h_01KGQ8ZCF0V4YHXQAFA9K1RTEJ)

### Créer une intervention depuis l'ordinateur

Chemin d'accès: *Interventions > Interventions > Nouveau*

Les informations principales à compléter sont

- le modèle d'intervention: Dimensionnement Vitalome
- le client
- le technicien qui utilisera l'application mobile pour effectuer le dimensionnement
- la tâche "Dimensionnement Vitalome"

![](https://support.openfire.fr/hc/article_attachments/25343833941276)

Lorsque l'intervention est créée, cliquer sur le bouton "**Confirmer**" pour que le technicien puisse effectuer l'intervention depuis son application mobile OpenFire.

### Créer une intervention depuis l'application mobile

📹[Visionner le tutoriel vidéo](https://drive.google.com/file/d/1ht_YsDP6QbmskL40rulVHMeXyRbCntaS/view?usp=sharing)

Il est nécessaire que votre intervention ait pour modèle d'intervention "Dimensionnement Vitalome" et pour tâche "Dimensionnement Vitalome" pour que vous ayiez accès au formulaire de dimensionnement sur le mobile.

![](https://support.openfire.fr/hc/article_attachments/25322898764956)

###

## Compléter le formulaire de dimensionnement

Sur le mobile, depuis l'intervention, toucher "Accéder à l'intervention" puis "Dimensionner un réseau".

Renseignez les différentes rubriques.

📹[Visionner le tutoriel vidéo](https://drive.google.com/file/d/1mkcrpL1BFwENlKn3brlgioaJXtL6wnJQ/view?usp=drive_link)

- **Principe de réseau**

![](https://support.openfire.fr/hc/article_attachments/25324506858652)

Un principe de réseau est un plan type qui représente:

- le moteur (carré M)
- les éventuels éléments directionnels, T ou Y (rond "ED")
- les pièces humides (carrés P)

qui constituent votre réseau de ventilation.

Sélectionnez le principe de réseau qui se rapproche le plus de votre configuration terrain. Si vous avez moins de pièces humides que représentées sur le principe de réseau, vous pourrez déclarer que la pièce représentée n'existe pas.

Une fois votre principe de réseau sélectionné, vous pourrez compléter les éléments en touchant l'icone "modifier" en haut à gauche. Puis, touchez chaque élément (M, ED, P) pour venir renseigner les informations correspondantes.

![](https://support.openfire.fr/hc/article_attachments/25324506859036)

![](https://support.openfire.fr/hc/article_attachments/25324490495516)

## Générer le devis associé

Lorsque le formulaire est complété, touchez "Valider" jusqu'à revenir sur l'écran de l'intervention, puis touchez "Enregistrer".

Votre devis est automatiquement généré avec les produits Vitalome adaptés selon les informations renseignées dans le formulaire. Il est accessible dans la section "Devis/Commandes".

![](https://support.openfire.fr/hc/article_attachments/25324490495900)

Vous pouvez également accéder à votre devis depuis l'ordinateur.

Chemin d'accès: *Interventions > Interventions.*

Depuis votre intervention, cliquez sur le *smart button* "Commande".

![](https://support.openfire.fr/hc/article_attachments/25324490496924)

### Avertissements à la génération du devis

Lors de la génération automatique du devis, des avertissements peuvent s'afficher dans les cas suivants:

- **le système n'a pas trouvé de produit correspondant à votre saisie formulaire.**
  Dans cette situation, nous vous invitons à vérifier que vous avez bien mis à jour vos produits dans votre base OpenFire. Si le problème persiste, vous pouvez vous rapprocher de l'assistance technique Vitalome.
- **le système a trouvé plusieurs produits éligibles à votre saisie formulaire**
  Si vous aviez défini dans votre base un produit à utiliser par défaut (*par exemple une réglette d'entrée d'air auto*), le système ajoute automatiquement au devis le produit par défaut.
  Sinon, le système ajoutera le premier produit correspondant trouvé.
  Les produits à utiliser "par défaut" se renseignent dans la section "Données techniques" de la fiche produit
  *![](https://support.openfire.fr/hc/article_attachments/25324490497308)*
  *Dans cette situation, s'il y a plusieurs produits de type "Réglette d'entrée d'air" en fonctionnement "auto", le produit "Autoréglable EMMA" sera ajouté par défaut au devis.*

Les avertissements sont visibles:

- **Depuis l'ordinateur: **sur la barre d'information latérales du devis

  ![](https://support.openfire.fr/hc/article_attachments/25324490497820)
- **Depuis le mobile: **sur la page de l'intervention, touchez l'icone d'information "i".

  ![](https://support.openfire.fr/hc/article_attachments/25324490498332)

### Modifier le devis généré

Si vous souhaitez supprimer ou ajouter un produit au devis généré automatiquement, vous pouvez le faire depuis l'ordinateur ou directement depuis le mobile. Vous pouvez également déplacer les produits de section en section.

[📹Visionner le tutoriel vidéo](https://drive.google.com/file/d/16zUbkqL_HnDoyIPvRu32XncXHYBMsvdt/view?usp=sharing)

Tant que le devis n'est pas signé, vous pouvez à tout moment revenir sur votre formulaire de dimensionnement pour le modifier et générer un nouveau devis en touchant "Enregistrer" à la fin de la saisie.

### Imprimer le devis

Depuis l'ordinateur, rendez vous sur votre devis et sélectionnez "Imprimer > Dossier Vitalome".

Ce dossier contient la page de garde, le devis et les conditions générales de vente.

![](https://support.openfire.fr/hc/article_attachments/25324833335068)

## Générer le rapport d'intervention (calepinage et dimensionnement)

**Depuis l'ordinateur**, rendez vous sur votre intervention et sélectionnez "Imprimer > Rapport d'intervention".

Ce rapport au format pdf contient les résultats des réponses au formulaire, le schéma du principe de réseau complété ainsi que le tableau des dimensionnements calculés.

![](https://support.openfire.fr/hc/article_attachments/25324833335324)

Mis a jour le : 06/02/2026
