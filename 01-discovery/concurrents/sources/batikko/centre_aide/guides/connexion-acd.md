---
url: https://batikko.com/documentation/guides/connexion-acd
url_finale: https://batikko.com/documentation/guides/connexion-acd
date_collecte: 2026-09-07
destination: centre_aide
---

## Vue d'ensemble

Le connecteur **Batikko × ACD i-Suite Expert** relie votre gestion quotidienne à la comptabilité de votre cabinet. À chaque facture validée dans Batikko, la pièce est déposée dans la GED de votre dossier, puis l'écriture comptable correspondante est créée et rattachée à ce justificatif.

Vous travaillez sur le terrain, votre expert-comptable retrouve un dossier alimenté au fil de l'eau : plus d'export, plus de ressaisie, plus de pochette de justificatifs à préparer en fin de mois.

- Connexion directe au serveur i-Suite de votre cabinet
- Écritures de vente créées à la validation des factures
- Écritures d'achat depuis vos dépenses et factures fournisseurs
- Justificatif déposé en GED et rattaché à son écriture
- Ventilation sur le plan comptable de votre cabinet
- TVA multi-taux BTP : 20 %, 10 %, 5,5 %

## Prérequis

Le connecteur ACD est inclus, sans surcoût.

Votre cabinet comptable utilise ACD i-Suite Expert et vous a ouvert un accès à votre dossier. Si vous n'en avez pas encore, demandez-le-lui : c'est lui qui le crée.

C'est le cabinet qui publie le dossier. Sans publication, aucune API n'y donne accès et la connexion sera refusée.

Côté cabinet également. C'est ce lien qui permet de rattacher automatiquement chaque justificatif à son écriture.

Les deux derniers points relèvent de votre **cabinet comptable**, pas de vous. Un seul message suffit : « Pouvez-vous publier mon dossier sur i-Suite et relier la GED à la comptabilité ? J'aimerais y connecter mon logiciel de gestion. »

## Les informations à récupérer

Contrairement à Pennylane ou Inqom, ACD n'a pas de serveur central : chaque cabinet a le sien. Batikko a donc besoin de quatre informations, que vous trouvez dans votre accès i-Suite ou que votre cabinet vous communique.

Propre à votre cabinet, du type https://isuite.acd-groupe.fr. C'est l'adresse que vous utilisez pour vous connecter à votre espace.

Visible dans l'adresse de votre page d'accueil ACD, sous la forme cnx1225.

Le code de votre dossier pour une connexion de type client, ou votre adresse e-mail pour un accès cabinet.

Celui de votre accès i-Suite. Il est chiffré dans Batikko et n'est jamais affiché après l'enregistrement.

À renseigner uniquement si vos identifiants donnent accès à plusieurs dossiers, pour indiquer lequel alimenter.

## Connecter ACD en 4 étapes

1. 01### Ouvrez les réglages de votre entrepriseDans le menu latéral de Batikko : Mon entreprise → Entreprise, puis ouvrez l'onglet « Comptabilité ».
2. 02### Cliquez sur « Connecter » sur la carte ACDUn formulaire s'ouvre et vous demande les informations réunies à l'étape précédente.
3. 03### Saisissez vos identifiants i-SuiteBatikko teste immédiatement la connexion à votre serveur. Si une information est erronée, le message vous dit lequel des quatre champs revoir, et rien n'est enregistré.
4. 04### C'est terminéLa connexion s'affiche comme active. Vos prochaines factures validées déposeront automatiquement leur justificatif en GED et créeront leur écriture.

Un bouton de **synchronisation manuelle** est disponible dans le même onglet pour transmettre les factures et dépenses des 30 derniers jours.

## Ce qui est synchronisé

Chaque facture validée devient une écriture dans le journal de ventes : client au débit, produits et TVA au crédit.

Vos dépenses et vos factures fournisseurs partent dans le journal d'achats, avec leur justificatif.

Le document est déposé dans la GED de votre dossier i-Suite, puis rattaché à son écriture : votre cabinet ne vous relance plus.

Les écritures sont ventilées sur les comptes réels de votre dossier (411, 706, TVA par taux), tels que votre cabinet les a définis.

La synchronisation va **de Batikko vers ACD**. Les devis ne sont pas transmis (un devis n'a pas de traduction comptable), et une écriture déjà transmise ne part jamais en double.

## Questions fréquentes

La connexion à i-Suite est refusée.

Vérifiez les quatre champs dans l'ordre : l'adresse du serveur telle qu'elle apparaît dans votre navigateur, la référence CNX, votre identifiant, puis le mot de passe. Si tout est exact, le dossier n'est probablement pas encore publié sur i-Suite : c'est votre cabinet qui le fait.

Où trouver ma référence CNX ?

Dans l'adresse de votre page d'accueil ACD, juste après le nom du serveur. Elle ressemble à cnx1225. En cas de doute, votre cabinet vous la donne en une minute.

Mes justificatifs arrivent mais pas les écritures.

C'est le signe que la GED n'est pas reliée à la comptabilité dans votre dossier. Demandez à votre cabinet d'établir ce lien, puis relancez une synchronisation manuelle.

Mes anciennes factures sont-elles transmises ?

La synchronisation automatique concerne les factures validées après la connexion. Le bouton de synchronisation manuelle transmet celles des 30 derniers jours.

Une facture peut-elle créer deux écritures ?

Non. Batikko garde la trace de chaque document transmis : une facture déjà envoyée est définitivement acquise et ne repart jamais, même en relançant une synchronisation manuelle.

Mon mot de passe i-Suite est-il en sécurité ?

Il est chiffré en base et n'est jamais réaffiché après l'enregistrement. Vous pouvez le remplacer à tout moment en reconnectant le service.

Comment déconnecter ACD ?

Dans Mon entreprise → Entreprise → onglet Comptabilité, cliquez sur « Déconnecter ». Les écritures déjà créées restent dans votre dossier ; les suivantes ne partiront plus.

Un problème de connexion ou une question sur la synchronisation ? Écrivez-nous à [\[email protected\]](https://batikko.com/cdn-cgi/l/email-protection#acdfd9dcdcc3ded8eccecdd8c5c7c7c382cade), nous répondons rapidement.

## Aller plus loin

### Une question sur cette fonctionnalité ?

Notre équipe vous répond en moins de 2 heures.

[Contacter le support](https://batikko.com/contact)