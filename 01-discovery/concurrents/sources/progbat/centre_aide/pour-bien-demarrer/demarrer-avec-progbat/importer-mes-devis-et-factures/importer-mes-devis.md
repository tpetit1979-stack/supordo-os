---
url: https://docv5.progbat.com/pour-bien-demarrer/demarrer-avec-progbat/importer-mes-devis-et-factures/importer-mes-devis
url_finale: https://docv5.progbat.com/pour-bien-demarrer/demarrer-avec-progbat/importer-mes-devis-et-factures/importer-mes-devis
date_collecte: 2026-09-06
destination: centre_aide
---

# Importer mes devis

▶️ Le concept est simple :

- Vous créez un devis sur ProGBat.
- Vous importez le contenu depuis un fichier Excel ou csv.

## Préparez votre fichier

Pour pouvoir importer un devis dans ProGBat, vous devez

- Soit l'exporter depuis votre ancien logiciel au format Excel ou csv. Rapprochez-vous de l'éditeur du logiciel pour savoir comment exporter le contenu d'un devis.
- Soit utiliser un devis, un DPGF, ou autre chiffrage réalisé sur Excel,
- Soit essayer de transformer un fichier Word en Excel, si vous utilisiez Word pour réaliser vos devis.

▶️ **Dans tous les cas, vous devez obtenir un fichier Excel ou csv, pour le mettre en forme et le préparer à être importé dans ProGBat.**

- Ouvrez votre fichier dans Excel (ou votre tableur habituel).
- Ne conservez que les lignes du contenu :  supprimez les entêtes (nom du chantier, références diverses, etc...), les lignes de totaux et sous-totaux, les lignes vides, etc
- Votre fichier doit contenir au minimum les 5 colonnes suivantes : 
  - N° de ligne (facultatif) 
    - Sans numérotation des titres, sous-titres et lignes, le logiciel ne pourra pas réaliser une [structure automatique](https://docv5.progbat.com/pour-bien-demarrer/demarrer-avec-progbat/importer-mes-devis-et-factures/importer-mes-devis#structure-automatique) )
  - Libellé (ou désignation)
  - Quantité
  - Unité
  - Prix unitaire H.T

## Importez le fichier

- Sélectionnez votre fichier Excel
- Précisez si la première ligne du fichier contient les titres de colonnes,
- Cliquez sur "Suivant".
- Faites correspondre les colonnes ProGBat à celles de votre fichier

## Structure du fichier

### Structure automatique

▶️ **Pour une structure optimale et automatique, il est très important que le numéro de ligne soit renseigné.**

## 💡 Comment ProGBat structure-t-il le devis ?

- Une ligne avec un numéro de ligne, sans quantité et sans unité sera considérée comme un titre (une tranche), ou comme un sous-titre (sous-tranche)
- Une ligne sans numéro de ligne, sans quantité et sans unité sera considérée comme un commentaire
- Les autres lignes seront considérées comme des lignes d'ouvrage

En fonction de la numérotation des lignes, et des critères ci-dessus, une structure vous est proposée avant l'import.

Si votre fichier ne contient aucun numéro de ligne, la structure ne sera certainement pas correcte.

La structure manuelle décrite ci-après vous permettra de vérifier, corriger, ou créer la structure de votre devis.

### Structure manuelle

Vérifiez, modifiez, ou créez (dans le cas où le fichier ne contient pas de numéros de lignes) la structure de votre devis :

- Vérifiez pour chaque ligne s'il s'agit d'une ligne de titre, d'ouvrage ou de commentaire, et modifiez si nécessaire
- Vérifiez si le niveau est correct, et modifiez si nécessaire. 
  - Dans l'exemple le titre est de niveau 1, et les ouvrages de niveau 2.
  - Un sous-titre aurait un niveau 2, et les ouvrages contenus dans le sous-titre un niveau 3.

Après vérifications, vous pouvez importer le fichier dans votre devis.

## ⚠️ IMPORTANT

**Si votre devis contient déjà des lignes, elles seront "écrasées" et remplacées par le fichier importé.**

## Astuce après import du contenu de votre devis

Lorsque vous importez un fichier Excel, vous importez du texte, qui n'est pas lié à votre bibliothèque d'ouvrages.

Vous pouvez rattacher chaque ligne de votre devis à un ouvrage de votre bibliothèque, sans modifier le libellé de l'ouvrage importé (essentiel pour un DPGF), simplement en cliquant sur l'icone du lien dans le menu de ligne.

Ainsi chaque ligne sera automatiquement chiffrée, et liée à un ouvrage de votre bibliothèque.

[PrécédentImporter mes devis et factures](https://docv5.progbat.com/pour-bien-demarrer/demarrer-avec-progbat/importer-mes-devis-et-factures)

[SuivantPoursuivre la facturation faite sur mon ancien logiciel](https://docv5.progbat.com/pour-bien-demarrer/demarrer-avec-progbat/importer-mes-devis-et-factures/poursuivre-la-facturation-faite-sur-mon-ancien-logiciel)

Mis à jour