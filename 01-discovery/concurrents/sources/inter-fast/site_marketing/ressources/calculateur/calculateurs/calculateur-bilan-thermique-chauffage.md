---
url: https://inter-fast.fr/ressources/calculateur/calculateurs/calculateur-bilan-thermique-chauffage
url_finale: https://inter-fast.fr/ressources/calculateur/calculateurs/calculateur-bilan-thermique-chauffage
date_collecte: 2026-09-07
destination: site_marketing
---

# Calculateur de bilan thermique chauffage

Estimez la puissance de chauffage **pièce par pièce** à partir de la zone climatique, de l'isolation, des vitrages et de la ventilation. Résultat instantané en kW et W/m².

## 🔥 Bilan thermique - Chauffage

Puissance de chauffage pièce par pièce - vitrages, isolation, zone climatique.

Vous êtes chez le client, il vous demande « quelle puissance pour ma PAC ? ». Sortir les tables Recknagel devant lui, c'est long. Répondre au pifomètre, c'est risqué : un générateur surdimensionné cycle court, s'use et consomme ; sous-dimensionné, il ne tient pas la température par grand froid. Le **bilan thermique** tranche en deux minutes. Ce calculateur estime la **puissance de chauffage pièce par pièce** à partir de quatre leviers : la zone climatique, l'isolation, les surfaces vitrées et la ventilation.

## Comment se calcule un bilan thermique de chauffage ?

Le calculateur applique la méthode des **déperditions** : on chiffre la chaleur que la pièce perd quand il fait froid dehors, et on dimensionne le générateur pour la compenser. Pour chaque pièce, la puissance se décompose en trois postes :

| Poste de déperdition | Formule | Ce qui l'influence | 
|---|---|---|
| **Parois** (murs, toit, sol) | U × surface × ΔT | Niveau d'isolation (coefficient U) | 
| **Vitrages** | U <sub>vitrage</sub> × surface × ΔT | Type de vitrage (simple, double, triple) | 
| **Renouvellement d'air** | 0,34 × volume × (vol/h) × ΔT | Type de ventilation (naturelle, VMC, double flux) | 

L'**écart de température ΔT** est la différence entre la température de consigne (20 °C par défaut) et la **température de base extérieure** de la zone climatique : −8 °C en zone H1b, 0 °C en zone H3 méditerranéenne. Le coefficient **0,34 Wh/(m³·K)** correspond à la capacité thermique volumique de l'air. La somme des trois postes est ensuite majorée d'une **marge de relance de 10 %** pour absorber les remises en température après un ralenti de nuit.

**Besoin de la performance réelle de la PAC derrière ce besoin de puissance ?**

Enchaînez avec notre [**calculateur de COP de pompe à chaleur**](https://inter-fast.fr/ressources/calculateur/calculateurs/calculateur-cop-pac), ou affinez l'isolation avec le [**calcul du coefficient U d'une paroi**](https://inter-fast.fr/ressources/calculateur/calculateurs/calculateur-coefficient-u-paroi).

## Exemple chiffré : un séjour de 25 m² en zone H1b

Prenons un séjour de **25 m²** sous 2,5 m de hauteur (volume 62,5 m³), isolation RT2012 (U ≈ 0,36), VMC simple flux (0,5 vol/h), consigne 20 °C en zone H1b (base −8 °C, soit **ΔT = 28 K**), avec 3 m² de double vitrage faible émissivité (U ≈ 1,6).

- **Parois** : 0,36 × (≈57,5 − 3) × 28 ≈**549 W**
- **Vitrage** : 1,6 × 3 × 28 ≈**134 W**
- **Renouvellement d'air** : 0,34 × 62,5 × 0,5 × 28 ≈**298 W**
- **Sous-total** ≈ 981 W,**+ 10 % de marge ≈ 1,08 kW** pour ce seul séjour

En additionnant toutes les pièces, le calculateur affiche la puissance totale, le ratio en W/m² et une reco de matériel (PAC air/eau, cascade…). Sur un logement RT2012 bien isolé, attendez-vous à un ratio de l'ordre de **40 à 60 W/m²**.

## 3 erreurs fréquentes qui faussent le dimensionnement

### 1. Dimensionner au ratio « 100 W/m² » pour tout le monde

Ce vieux réflexe date des bâtiments non isolés. Sur du RE2020, il conduit à **doubler** la puissance réellement nécessaire - donc à un générateur qui cycle et s'use. Le calcul pièce par pièce évite ce piège.

### 2. Oublier la zone climatique

Le même logement demande bien plus de puissance à Strasbourg (H1b, −8 °C) qu'à Nice (H3, 0 °C). Renseigner la bonne zone change l'écart ΔT, donc le résultat.

### 3. Négliger les surfaces vitrées

Un séjour avec une grande baie en simple vitrage peut perdre plus par la fenêtre que par tous ses murs. Saisissez chaque vitrage avec son type pour un résultat fiable.

## Du calcul au devis signé, sans ressaisie

Une fois la puissance validée, transformez-la en chiffrage propre : [le logiciel de devis & factures InterFast](https://inter-fast.fr/fonctionnalites/logiciel-devis-factures) vous aide à éditer des devis CVC clairs, et à suivre la marge chantier. [Testez InterFast gratuitement](https://inter-fast.fr).