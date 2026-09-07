---
url: https://documentation.openfire.fr/knowsystem/balance-agee-274
url_finale: https://documentation.openfire.fr/knowsystem/balance-agee-274
date_collecte: 2026-09-06
destination: documentation_2
---

La Balance âgée des tiers est un rapport détaillé de vos en-cours par période, en fonction de leurs échéances.

La balance âgée présente les soldes dus et leur ancienneté à la date de son édition. Le suivi de la balance âgée des tiers permet d'y voir plus clair dans les paiements réalisés et en attente.

Deux rapports sont disponibles dans OpenFire via les sous-menus:

- Rapports PDF,
- Rapports comptables.

Afin de mettre en place une balance âgée, il est nécessaire de régler quelques points importants :

- Avoir achevé la saisie comptable (factures d’achats, de ventes, relevés bancaires, etc.) pour être le plus précis possible.
- Avoir révisé les comptes et lettré les comptes de tiers.
- Avoir complété la date d’échéance de la facture lors de la saisie de la pièce comptable.

## Rapport PDF

Ce rapport est disponible dans el menu **Rapports > Balance âgée des tiers** (partie Rapports PDF).

Ce rapport permet d'obtenir un fichier PDF comprenant les dettes et les créances en fonction des dates d'échéance des factures à payer ou à recevoir.

On peut ainsi voir les échéances à venir et celles qui sont passées depuis plus de 15 jours, 30 jours, 60 jours, etc..:

Date de début : date de référence du rapport. Le solde des comptes sera calculé par rapport à cette date.

Durée de la période : Défini la durée de l’échéance de référence par antériorité à la date de début ; Ainsi, si vous demandez une période de 30 jours alors Odoo génère une analyse des créanciers pour le mois passé, les deux derniers mois, etc.

Du partenaire : type de compte à exporter : clients, fournisseurs ou ensemble des comptes de tiers.

Mouvements cibles : toutes les écritures ou uniquement celles comptabilisées.

OpenFire calculera alors un tableau de solde créditeur par date de début. Ainsi, si vous demandez une période de 30 jours, alors OpenFire génère une analyse des créanciers pour le mois passé, les deux derniers mois, et ainsi de suite:

## Rapport Comptable

Un autre rapport est disponible dans le menu Rapports > Balance âgée des tiers (partie Rapports Comptables)

Ce rapport précise, pour chaque compte de tiers (les clients ou les fournisseurs) :

- Le numéro de compte ou la dénomination du tiers
- Le montant de la dette d’une entreprise (balance âgée fournisseurs) ou le montant de ses créances à encaisser (balance âgée clients)
- La ventilation des sommes en fonction de l’échéance : sommes échues, sommes dont l’échéance intervient à moins de 30 jours, à plus de 30 jours, à plus de 60 jours, etc.

Il existe deux types de balances âgées : celle pour les clients (suivi des créances) et celle pour les fournisseurs (suivi des dettes). La balance âgée fournisseurs fonctionne sur le même principe que celle des clients, à ceci près qu'elle détaille les montants des factures qui restent à payer.

L'option Afficher le détail des écritures permet de masquer les comptes dont le solde est à zéro dans le fichier.

L'option Affiche le détail des écritures permet de choisir l'affichage au choix entre:

- Rendus du Rapport sans détail des écritures :

- Rapports avec détail des écritures :