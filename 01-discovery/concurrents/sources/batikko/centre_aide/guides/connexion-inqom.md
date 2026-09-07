---
url: https://batikko.com/documentation/guides/connexion-inqom
url_finale: https://batikko.com/documentation/guides/connexion-inqom
date_collecte: 2026-09-07
destination: centre_aide
---

## Vue d'ensemble

Le connecteur **Batikko × Inqom** relie votre gestion quotidienne à la comptabilité de votre cabinet. À chaque facture validée dans Batikko, l'écriture comptable correspondante est créée dans votre dossier Inqom, avec la facture PDF rattachée en pièce justificative.

Vous travaillez sur le terrain, votre expert-comptable retrouve un dossier alimenté au fil de l'eau : plus d'export, plus de ressaisie, plus de pochette de justificatifs à préparer en fin de mois.

- Connexion sécurisée en quelques clics (OAuth)
- Écritures de vente créées à la validation des factures
- Écritures d'achat depuis vos dépenses
- Pièce justificative rattachée à chaque écriture
- Ventilation sur le plan comptable de votre cabinet
- TVA multi-taux BTP : 20 %, 10 %, 5,5 %

## Prérequis

Le connecteur Inqom est inclus, sans surcoût.

Votre cabinet comptable utilise Inqom et vous a invité sur votre dossier avec un rôle permettant l'envoi d'écritures (rôle DAF, demandez à votre cabinet si vous n'avez pas encore d'accès).

## Connecter Inqom en 4 étapes

1. 01### Ouvrez les réglages de votre entrepriseDans le menu latéral de Batikko : Mon entreprise → Entreprise, puis ouvrez l'onglet « Comptabilité ».
2. 02### Cliquez sur « Connecter » sur la carte InqomVous êtes redirigé vers la page de connexion sécurisée d'Inqom.
3. 03### Autorisez Batikko sur votre dossierConnectez-vous avec vos identifiants Inqom et validez l'autorisation. Batikko ne voit jamais votre mot de passe.
4. 04### C'est terminéBatikko identifie votre dossier comptable et affiche la connexion comme active. Vos prochaines factures validées créeront automatiquement leurs écritures dans Inqom.

Un bouton de **synchronisation manuelle** est disponible dans le même onglet pour transmettre les factures et dépenses des 30 derniers jours.

## Ce qui est synchronisé

Chaque facture validée devient une écriture dans le journal de ventes : client au débit, produits et TVA au crédit.

Vos dépenses partent dans le journal d'achats, avec le justificatif scanné ou un récapitulatif généré.

La facture PDF ou le justificatif est rattaché directement à son écriture, votre cabinet ne vous relance plus.

Les écritures sont ventilées sur les comptes réels de votre dossier (411, 706, TVA par taux), tels que votre cabinet les a définis.

La synchronisation va **de Batikko vers Inqom**. Les devis ne sont pas transmis (un devis n'a pas de traduction comptable), et une écriture déjà transmise ne part jamais en double.

## Questions fréquentes

La connexion me dit qu'aucun dossier comptable n'est accessible.

Votre compte Inqom n'a pas d'accès direct à votre dossier (c'est le cas si le dossier a été créé par votre cabinet). Demandez à votre cabinet de vous inviter sur votre dossier avec le rôle DAF, puis reconnectez-vous.

Mes anciennes factures sont-elles transmises ?

La synchronisation automatique concerne les factures validées après la connexion. Le bouton de synchronisation manuelle transmet celles des 30 derniers jours.

Une facture peut-elle créer deux écritures ?

Non. Batikko garde la trace de chaque document transmis : une facture déjà envoyée est définitivement acquise et ne repart jamais, même en relançant une synchronisation manuelle.

Comment déconnecter Inqom ?

Dans Mon entreprise → Entreprise → onglet Comptabilité, cliquez sur « Déconnecter ». Les écritures déjà créées restent dans votre dossier ; les suivantes ne partiront plus.

Un problème de connexion ou une question sur la synchronisation ? Écrivez-nous à [\[email protected\]](https://batikko.com/cdn-cgi/l/email-protection#9cefe9ececf3eee8dcfefde8f5f7f7f3b2faee), nous répondons rapidement.

## Aller plus loin

### Une question sur cette fonctionnalité ?

Notre équipe vous répond en moins de 2 heures.

[Contacter le support](https://batikko.com/contact)