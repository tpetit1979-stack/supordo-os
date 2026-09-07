---
url: https://inter-fast.fr/ressources/calculateur/calculateurs/calculateur-coefficient-u-paroi
url_finale: https://inter-fast.fr/ressources/calculateur/calculateurs/calculateur-coefficient-u-paroi
date_collecte: 2026-09-07
destination: site_marketing
---

# Calculateur de coefficient U d'une paroi

Estimez le **coefficient de transmission thermique U** d'une paroi multicouche en empilant les matériaux et leurs épaisseurs. Résultat instantané en W/(m²·K) avec classement RT2012 / RE2020.

## 🧱 Coefficient U paroi

Paroi multicouche - résistance thermique et coefficient U.

Avant de dimensionner un chauffage, de justifier une rénovation ou de comparer deux solutions d'isolation, il faut une donnée clé : le **coefficient U** de la paroi, sa capacité à laisser fuir la chaleur. Plus il est bas, mieux le mur isole. Ce calculateur l'obtient en empilant les couches du mur (de l'intérieur vers l'extérieur), chacune avec son épaisseur et sa conductivité thermique λ. En quelques secondes, vous obtenez la **résistance thermique R**, le **coefficient U en W/(m²·K)** et un classement par rapport aux exigences RT2012 et RE2020.

## Comment se calcule le coefficient U d'une paroi ?

Le principe est l'addition des **résistances thermiques** en série. Chaque couche oppose une résistance R égale à son épaisseur divisée par sa conductivité λ. On ajoute les **résistances superficielles** de surface (Rsi côté intérieur, Rse côté extérieur), puis on inverse la somme totale pour obtenir U.

| Grandeur | Formule | Détail | 
|---|---|---|
| **Résistance d'une couche** | R = e / λ | e = épaisseur (m), λ = conductivité W/(m·K) | 
| **Résistances superficielles** | Rsi + Rse = 0,13 + 0,04 | 0,17 m²·K/W pour un mur vertical | 
| **Résistance totale** | Rt = Rsi + Rse + Σ (e/λ) | somme de toutes les couches, en m²·K/W | 
| **Coefficient U** | U = 1 / Rt | en W/(m²·K) - plus bas = mieux isolé | 

La conductivité λ est la signature thermique du matériau : un isolant comme le **PU (λ ≈ 0,022)** ou la **laine minérale (λ ≈ 0,035)** résiste beaucoup mieux qu'une **brique (λ ≈ 0,50)** ou un **béton (λ ≈ 1,75)**. À épaisseur égale, c'est l'isolant qui fait l'essentiel de la résistance. Le calculateur classe ensuite le résultat : U ≤ 0,22 « Excellent – RE2020 », U ≤ 0,36 « Bon – RT2012 », U ≤ 0,80 « Moyen », au-delà « Insuffisant ».

**Le U en poche, place au dimensionnement ?**

Injectez cette isolation dans notre [**calculateur de bilan thermique chauffage**](https://inter-fast.fr/ressources/calculateur/calculateurs/calculateur-bilan-thermique-chauffage), ou évaluez la performance de la PAC associée avec le [**calculateur de COP de pompe à chaleur**](https://inter-fast.fr/ressources/calculateur/calculateurs/calculateur-cop-pac).

## Exemple chiffré : un mur brique + laine minérale

Reprenons la paroi par défaut, de l'intérieur vers l'extérieur : **plâtre BA13 13 mm** (λ 0,35), **brique creuse 200 mm** (λ 0,50), **laine minérale 120 mm** (λ 0,035), **enduit ciment 15 mm** (λ 1,15).

- **Plâtre** : 0,013 / 0,35 ≈**0,037** m²·K/W
- **Brique** : 0,200 / 0,50 =**0,400** m²·K/W
- **Laine minérale** : 0,120 / 0,035 ≈**3,429** m²·K/W
- **Enduit** : 0,015 / 1,15 ≈**0,013** m²·K/W
- **Superficielles** : Rsi + Rse =**0,170** m²·K/W
- **Total** : Rt ≈**4,049** m²·K/W →**U ≈ 0,247 W/(m²·K)**

Avec U ≈ 0,25, cette paroi décroche le classement **« Bon – RT2012 »** et frôle même le seuil RE2020. On voit que la laine minérale, malgré ses 120 mm seulement, apporte à elle seule plus de 80 % de la résistance totale : c'est bien l'isolant qui pilote la performance.

## 3 erreurs fréquentes qui faussent le U

### 1. Oublier les résistances superficielles

Sans le Rsi + Rse (0,17 m²·K/W pour un mur), on surestime légèrement le U et on perd la cohérence avec les valeurs réglementaires. Le calculateur les ajoute automatiquement, mais gardez en tête qu'elles changent pour une toiture ou un plancher.

### 2. Se tromper de conductivité λ

Une laine minérale peut afficher λ de 0,030 à 0,045 selon le produit. Reprendre la valeur exacte de la fiche technique (lambda déclaré) plutôt qu'une valeur moyenne évite des écarts de 10 à 20 % sur le R de la couche isolante.

### 3. Ignorer les ponts thermiques

Ce calcul donne le U « en partie courante ». Les ossatures, linteaux et planchers créent des ponts thermiques qui dégradent la performance réelle de la paroi. Pour une étude réglementaire, ils doivent être traités à part.

## Du calcul au devis signé, sans ressaisie

Une fois l'isolation arbitrée, transformez-la en chiffrage propre : [le logiciel de devis & factures InterFast](https://inter-fast.fr/fonctionnalites/logiciel-devis-factures) vous aide à éditer des devis d'isolation clairs et à suivre la marge chantier. [Testez InterFast gratuitement](https://inter-fast.fr).