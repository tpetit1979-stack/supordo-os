---
url: https://batikko.com/documentation/guides/connexion-pennylane
url_finale: https://batikko.com/documentation/guides/connexion-pennylane
date_collecte: 2026-09-07
destination: centre_aide
---

## Vue d'ensemble

Le connecteur **Batikko × Pennylane** est certifié par Pennylane. Une fois activé, chaque facture de vente finalisée dans Batikko est transmise automatiquement dans votre dossier Pennylane, avec ses lignes détaillées et sa TVA correctement ventilée.

Vous facturez depuis le chantier, votre comptable retrouve tout dans Pennylane : plus d'export manuel, plus de PDF envoyés par email, plus de ressaisie.

- Connexion sécurisée en quelques clics (OAuth)
- Synchronisation automatique des factures de vente
- TVA multi-taux : 20 %, 10 %, 5,5 %
- Clients créés et rattachés automatiquement
- Aucune facture envoyée en double
- Journal de synchronisation consultable

## Prérequis

Le connecteur Pennylane est inclus dans tous les plans, sans surcoût.

Vous devez pouvoir vous connecter à Pennylane avec votre propre identifiant. Si c'est votre cabinet comptable qui a ouvert le dossier, demandez-lui de vous y inviter (voir les questions fréquentes).

## Connecter Pennylane en 4 étapes

1. 01### Ouvrez les réglages de votre entrepriseDans le menu latéral de Batikko : Mon entreprise → Entreprise, puis ouvrez l'onglet « Comptabilité ».
2. 02### Cliquez sur « Connecter » sur la carte PennylaneVous êtes redirigé vers la page de connexion sécurisée de Pennylane.
3. 03### Autorisez Batikko sur votre dossierConnectez-vous avec vos identifiants Pennylane et validez l'autorisation d'accès. Batikko ne voit jamais votre mot de passe.
4. 04### C'est terminéDe retour dans Batikko, la connexion apparaît comme active. Vos prochaines factures finalisées partiront automatiquement vers Pennylane.

Un bouton de **synchronisation manuelle** est aussi disponible dans le même onglet, pour rattraper les factures émises avant la connexion.

## Ce qui est synchronisé

Chaque facture finalisée est transmise avec son numéro, ses dates et ses montants.

Le détail de chaque ligne (désignation, quantité, montant) arrive dans Pennylane, pas un simple total.

Chaque ligne porte son taux de TVA : 20 %, taux intermédiaire 10 %, taux réduit 5,5 %. Les totaux sont exactement équilibrés.

Le client de la facture est retrouvé ou créé dans Pennylane, sans doublons.

La synchronisation va **de Batikko vers Pennylane** et concerne les factures de vente. Les achats et les écritures saisies directement dans Pennylane ne sont pas rapatriés dans Batikko.

## E-facturation : qui fait quoi

La facturation électronique et la comptabilité sont deux circuits distincts, et le connecteur respecte cette séparation :

### Batikko émet vos e-factures

L'émission au format électronique réglementaire passe par la plateforme agréée partenaire de Batikko. Rien à configurer de plus.

### Pennylane reçoit votre comptabilité

Le connecteur alimente votre dossier comptable. Il ne déclenche aucune émission : votre facture n'entre jamais deux fois dans le circuit e-facturation.

## Questions fréquentes

Mon dossier Pennylane a été ouvert par mon cabinet comptable, la connexion échoue.

C'est le cas le plus fréquent : demandez à votre cabinet de vous inviter sur votre dossier Pennylane avec votre propre adresse email. Une fois l'invitation acceptée, vous pourrez autoriser la connexion depuis Batikko.

Mes anciennes factures sont-elles envoyées ?

La synchronisation automatique concerne les factures finalisées après la connexion. Utilisez la synchronisation manuelle pour transmettre l'historique.

Une facture peut-elle partir deux fois ?

Non. Batikko garde la trace de chaque facture transmise et ne renvoie jamais un doublon, même si vous relancez une synchronisation manuelle.

Comment déconnecter Pennylane ?

Dans Mon entreprise → Entreprise → onglet Comptabilité, cliquez sur « Déconnecter ». Les factures déjà transmises restent dans Pennylane ; les suivantes ne partiront plus.

Un problème de connexion ou une question sur la synchronisation ? Écrivez-nous à [\[email protected\]](https://batikko.com/cdn-cgi/l/email-protection#93e0e6e3e3fce1e7d3f1f2e7faf8f8fcbdf5e1), nous répondons rapidement.

## Aller plus loin

### Une question sur cette fonctionnalité ?

Notre équipe vous répond en moins de 2 heures.

[Contacter le support](https://batikko.com/contact)