---
source: https://support.openfire.fr/hc/fr/articles/29506452129052-Recevoir-et-g%C3%A9rer-ses-factures-fournisseurs-via-la-Plateforme-Agr%C3%A9%C3%A9e
categorie: Utiliser OpenFire
titre: Recevoir et gérer ses factures fournisseurs via la Plateforme Agréée
date_recuperation: 2026-09-05
---

# Recevoir et gérer ses factures fournisseurs via la Plateforme Agréée

Cet article vous guide à travers le processus de réception automatique des factures fournisseurs dans OpenFire. Vous y apprendrez comment synchroniser vos données avec votre Plateforme Agréée (PA) et comment suivre l'état de vos flux d'importation.

Cet article contient les sections suivantes :

- [Préréquis et identification des fournisseurs](#h_01KZPCT5R51JWQ1M3H04EWCMNG)
- [Procédure d'importation depuis le tableau de bord](#h_01KZPCT5R9PRRSCX98S0698YP7)
- [Comprendre comment la facture a été créée](#h_01KZPE725XDZKXA0GG26NFQAET)
- [Comprendre l'onglet Facturation électronique](#h_01KZPCT5RES8PKH8FFYF5W52K2)
- [Consulter la facture PDF d'origine dans le chatter](#h_01KZPE5PAP83KKBHQ1EGVJBWHN)
- [Bonnes pratiques](#h_01KZPCT5RKXVKZ75WAXS5GC9BY)

## Prérequis et identification des fournisseurs

Grâce à la facturation électronique, OpenFire crée automatiquement des factures brouillons pré-remplies dès la réception des fichiers structurés via la Plateforme Agréée.

Pour que le système attribue correctement une facture reçue au bon fournisseur, vérifiez que la fiche de votre fournisseur comporte impérativement :

- Son numéro de TVA intracommunautaire
- Son numéro SIREN
- Son pays de rattachement
- Ses lignes d'annuaire correctement synchronisées

| 💡**Note **: Si une facture comportant le même numéro et le même fournisseur existe déjà dans OpenFire, le système vous en informe et bloque la création de doublons. |
| --- |

## Procédure d'importation depuis le tableau de bord

Pour lancer la récupération de vos nouvelles factures fournisseurs, effectuez les étapes suivantes :

1. Suivre le chemin d'accès suivant : `Comptabilité > Tableau de bord`.
2. Repérer la carte de votre journal d'achat (ex : **Achats Généraux** ou **Achats Exploitation**).
3. Cliquer sur les trois petits points verticaux (⋮) situés en haut à droite du journal.
4. Cliquer sur la commande **Importer depuis votre PA**.

![](https://support.openfire.fr/hc/article_attachments/29506513202844)

Cette action déclenche la synchronisation avec la Plateforme Agréée (PA) pour :

- **Télécharger toutes les nouvelles factures fournisseurs** transmises depuis le dernier import pour votre société active, tous journaux confondus.
- **Récupérer **et **mettre à jour** l'état des **événements **de vos factures clients et fournisseurs.

Une petite notification vous indique le nombre de flux (facture ou événement) créés à la suite de la notification.

![](https://support.openfire.fr/hc/article_attachments/29506592339484)

## Comprendre comment la facture a été créée

Une fois la facture importée, vous pouvez retrouver des informations concernant la façon dont OpenFire a créé votre facture, en fonction de votre configuration et des éléments de la facture.

Par exemple, vous pouvez retrouver le message suivant :

![](https://support.openfire.fr/hc/article_attachments/29676498859164)

## Comprendre l'onglet Facturation électronique

Une fois la facture importée, vous pouvez consulter ses informations de télétransmission directement sur le document :

1. Suivre le chemin d'accès suivant : `Comptabilité > Fournisseurs > Factures` et ouvrir la facture souhaitée.
2. Cliquer sur l'onglet **Facturation électronique**.

![](https://support.openfire.fr/hc/article_attachments/29506641194140)

Vous y trouverez les champs suivants :

- **Société pour la facturation électronique** : nom de votre entité légale enregistrée auprès de la Plateforme Agréée (renseigné automatiquement).
- **Flux** : identifiant unique de la transmission ainsi que son statut en cours (ex : `i_209472 (Terminé)`).
- **Votre ligne d'annuaire** : identifiant unique de votre entreprise dans l'annuaire de facturation.
- **Identifiant de ligne d'annuaire** : identifiant unique de votre fournisseur dans l'annuaire.
- **Section ÉVÉNEMENTS** : tableau détaillant l'historique chronologique de tous les échanges et statuts transmis à la plateforme.

🚨Avertissement : Si l'un des identifiants d'annuaire est manquant, la facture électronique ne pourra pas être traitée correctement. Vérifiez toujours les données de vos contacts dans l'annuaire.

## Consulter la facture PDF d'origine dans le chatter

Lors de la réception du flux de facturation électronique, le fichier PDF lisible d'origine fourni par votre fournisseur est automatiquement rattaché à la facture créée dans OpenFire.

Pour visualiser ou télécharger le document PDF d'origine :

1. Ouvrir la facture fournisseur concernée.
2. Consulter la zone d'historique et d'échange (le **chatter**) située sous la facture ou dans la colonne de droite selon votre écran, et afficher les pièces jointes
3. Cliquer sur la pièce jointe PDF pour ouvrir l'aperçu ou télécharger le fichier directement sur votre poste.

![](https://support.openfire.fr/hc/article_attachments/29506867566108)

## Bonnes pratiques

- **Lancer régulièrement la synchronisation :** prenez l'habitude de cliquer sur **Importer depuis votre PA** au début de votre journée comptable pour traiter vos factures au fil de l'eau. A défaut, une action le fera automatiquement pour vous chaque jour, de nuit.
- **Contrôler les brouillons :** validez les montants et la complétude des factures générées en statut "Brouillon" avant de les comptabiliser définitivement.

Mis a jour le : 25/08/2026
