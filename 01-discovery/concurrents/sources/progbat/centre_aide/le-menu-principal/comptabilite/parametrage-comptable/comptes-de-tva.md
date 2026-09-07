---
url: https://docv5.progbat.com/le-menu-principal/comptabilite/parametrage-comptable/comptes-de-tva
url_finale: https://docv5.progbat.com/le-menu-principal/comptabilite/parametrage-comptable/comptes-de-tva
date_collecte: 2026-09-06
destination: centre_aide
---

# Comptes de TVA

Saisissez ici les comptes de TVA associés à chaque taux.

## Compte d'attente

Ce compte est actuellement utilisé pour comptabiliser les factures d'acompte :

compte

Débit

Crédit

411 - client

1000

419 - clients créditeurs

1000

4457 - TVA encaissée

200

4458 - TVA en attente

200

Lors d'une prochaine évolution, le 419 sera crédité pour le montant hors taxes, permettant de ne plus utiliser le compte 4458.

## Les extensions

▶️ Au moment de l'export comptable :

- Le logiciel analyse le taux de TVA appliqué à la ligne, et ajoute en fonction du taux une extension au compte de charge ou de produit, pour réaliser une ventilation par taux de TVA. 
  - Si le compte utilisé est le 7041, et que l'extension choisie pour le taux à 20% est 20, le compte appliqué à l'écriture sera le 704120.

Mis à jour