---
url: https://docv5.progbat.com/pour-bien-demarrer/parametrage/parametres-de-lentreprise/numero-des-documents
url_finale: https://docv5.progbat.com/pour-bien-demarrer/parametrage/parametres-de-lentreprise/numero-des-documents
date_collecte: 2026-09-06
destination: centre_aide
---

# Numéro des documents

⚡ Les factures doivent être numérotées à l'aide d'un numéro unique basé sur une séquence chronologique continue, sans rupture. Cela implique que 2 factures ne peuvent pas avoir le même numéro.

**Cliquez sur le bouton "Paramètres" en haut à droite de l'écran** , **puis sur la vignette "Entreprise".
Ouvrez la section "Numéro des documents"**

## Paramétrer la numérotation des documents

Sélectionnez le type de document souhaité.

Nous prendrons pour exemple la numérotation des factures.

Dans cet exemple :

- Le numéro commence par l'année sur 4 chiffres. 
  - Bien entendu, le numéro se mettra à jour à chaque changement d'année de manière automatique.
- Nous avons ajouté le numéro du mois. 
  - Le mois est disponible uniquement si l'année a été ajoutée avant dans le modèle.
- Puis nous avons ajouté du texte 
  - Ici, uniquement un tiret, mais nous aurions pu par exemple commencer notre modèle de numérotation par une zone texte, pour écrire "F-" par exemple.
- Et enfin, nous avons prévu que le compteur comporte 4 chiffres. 
  - Ceci est important, car si vous laissez le compteur avec 1 chiffre par exemple, la facture 10 aura bien le numéro 10, mais si vous triez vos factures par numéro, la facture 10 se retrouvera juste après la facture 1, et pas après la facture 9, car il s'agit de tris alphanumériques.
  - En tri alphanumérique, 202411-10 est plus petit que 202411-9, car le caractère "1" est plus petit que le caractère "9"

## Poursuivre la numérotation de mon ancien logiciel

Vous utilisiez Excel, ou un logiciel de facturation, et vous avez déjà une numérotation en cours que vous devez conserver, ne serait-ce que pour poursuivre la chronologie obligatoire.

- Configurez votre numérotation pour qu'elle soit au plus proche de celle que vous utilisiez auparavant.
- Si votre dernière facture avait le numéro 250 par exemple, saisissez 251 dans le champ "Commencer le compteur à la valeur :"
- Ainsi, la première facture que vous validerez sur ProGBat démarrera au numéro 251.

## Autoriser le préfixage des numéros de facture

Vous pouvez être amené à avoir plusieurs séries de numérotations distinctes, par exemple si vous avez plusieurs site de facturation, ou si vous souhaitez différencier 2 types de facturation comme "travaux" et "vente showroom" par exemple.

- Activez dans ce cas l'option "Autoriser le préfixage des numéros de facture"
- Au moment de la validation d'une facture, vous pourrez saisir le préfixe correspondant. 
  - le compteur est propre à chaque série.

## Optez pour une numérotation simple

Contrairement à l'époque "papier", l'informatique permet aujourd'hui de retrouver et d'afficher très simplement et rapidement toutes les informations d'une facture, sans que son numéro ne comporte l'année, le code client, et encore moins le mois.

Au plus votre numérotation sera simple, au mieux se sera.

Une simple configuration du type F00001 est largement suffisante, et sera appréciée de votre expert comptable de l'administration fiscale en cas de contrôle.

## Factures : numéro provisoire

Lorsque vous créez une facture sur ProGBat, elle porte un numéro provisoire, au format $000001 Ceci permet de supprimer une facture provisoire, sans créer de trou dans votre numérotation.

Votre modèle de numérotation, et le numéro réel de la facture s'appliqueront au moment de la validation de la facture.

Mis à jour