# 0006 — Limites d'Analysis C et prérequis avant agrégation H1

Cette décision consigne ce qu'Analysis C (crash-test externe de V3, 37
articles Axonaut/Costructor/OpenFire/ProGBat, 2026-09-08) a établi sur la
testabilité de H1, et ce qui reste délibérément non tranché. Elle
complète 0003 (hypothèses de continuité) et 0005 (axes de recherche),
qu'elle ne remplace pas.

## Ce qu'Analysis C a établi

**0 rupture documentée sur 39 transitions**, dans un échantillon
délibérément curaté (stress test ciblé + diversité documentaire), pas un
échantillon proportionnel ou aléatoire du corpus restant.

**Ce résultat n'est PAS une conclusion de marché.** Il est probablement
lié au genre documentaire des articles choisis (procédures de
configuration/référence) plus qu'au produit ou au secteur : le même type
de contrôle appliqué aux Pilotes A/B (genre plus narratif,
FAQ/dépannage) avait produit 21 ruptures sur 123 transitions. Aucune
comparaison de taux entre Pilotes et Analysis C ne doit être tirée : les
deux échantillons ne sont pas construits pour être comparables entre eux.

**Conséquence directe : `non_propagation` et `rupture_temporelle`**
(ajoutés en V3 pour corriger CP-7/CP-14/CP-16, voir
`analysis/SCHEMA-V2.md` §V3.5) **n'ont reçu aucun exercice sur du
matériel neuf.** Ce sont des corrections conçues et arbitrées, pas encore
validées empiriquement.

**La testabilité documentaire de H1 sur le corpus restant reste donc une
question ouverte** — ni réfutée, ni confirmée : simplement pas encore
mise à l'épreuve sur un échantillon construit pour répondre précisément à
cette question.

## Prérequis avant toute lecture agrégée de futurs résultats H1

Restent à définir, explicitement non traités par cette décision :

- **la matrice d'applicabilité par concurrent** (annoncée en 0003) ;
- **le seuil de falsification de H1**, à fixer avant lecture des
  résultats, jamais après (règle déjà posée en 0003, rappelée ici).

## Ordre de travail retenu (séquencement, pas une nouvelle méthodologie)

Avant d'investir dans les deux prérequis ci-dessus, un lot test ciblé sur
des rubriques FAQ/dépannage (Vertuoza et InterFast, ~20 articles) doit
d'abord établir si ce type de rubrique produit des ruptures documentées.

**Motif** : si les FAQ ne produisent, elles non plus, aucune
`rupture_documentee`, H1 pourrait ne pas être testable sur ce corpus
documentaire du tout — construire la matrice et fixer un seuil serait
alors un travail sans objet. Ce lot test décide si les deux prérequis
valent la peine.

Ordre retenu, à exécuter séparément, non commencé par cette décision :

1. lot test FAQ/dépannage (Vertuoza + InterFast, ~20 articles) ;
2. selon son résultat — les deux prérequis ci-dessus, ou un arbitrage
   explicite sur la testabilité de H1 sur ce corpus ;
3. industrialisation.

## Lecture flottante

Le principe de lecture flottante (relire la source sans le schéma en
tête, après extraction, pour détecter les angles morts) est retenu comme
contrôle permanent. **Le taux d'échantillonnage utilisé pendant Analysis
C (environ un quart des articles) n'est pas gravé comme ratio
permanent** : un échantillonnage substantiel reste utile en début
d'industrialisation et pourra être réduit si le rendement de découverte
— élevé lors d'Analysis C, chaque article relu ayant produit au moins une
observation nouvelle — venait à diminuer.
