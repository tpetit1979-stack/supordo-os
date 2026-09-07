---
url: https://inter-fast.fr/ressources/calculateur/calculateurs/calculateur-pertes-de-charge
url_finale: https://inter-fast.fr/ressources/calculateur/calculateurs/calculateur-pertes-de-charge
date_collecte: 2026-09-07
destination: site_marketing
---

# Calculateur de pertes de charge hydrauliques

Estimez les **pertes de charge** d'un réseau d'eau à partir du débit, du diamètre, de la longueur et des singularités. Méthode Swamee-Jain, résultat instantané en kPa, mCE et m/s.

## 📐 Pertes de charge

Réseau hydraulique - méthode Swamee-Jain (Darcy-Weisbach).

Vous dimensionnez un circuit de chauffage ou un réseau d'eau et la question tombe : « quel circulateur, quel diamètre ? ». Sous-dimensionner le tube, c'est de la vitesse, du bruit et une pompe qui force ; surdimensionner, c'est du cuivre payé pour rien. La **perte de charge** est l'arbitre : elle dit combien de pression votre réseau « mange » entre le départ et le retour. Ce calculateur l'estime en quelques secondes à partir du **débit**, du **diamètre**, de la **longueur** et des **singularités**, par la méthode Swamee-Jain appliquée à la relation de Darcy-Weisbach.

## Comment se calcule une perte de charge hydraulique ?

Le calculateur enchaîne quatre étapes : vitesse du fluide, régime d'écoulement (Reynolds), coefficient de frottement, puis perte de charge. La perte de charge linéaire suit la loi de **Darcy-Weisbach**, et le coefficient de frottement *f* est estimé par la formule explicite de **Swamee-Jain** (équivalente à Colebrook, sans itération).

| Étape | Formule | Détail | 
|---|---|---|
| **Vitesse** | v = Q / A, A = π·D²/4 | Q en m³/s, D = diamètre intérieur (m) | 
| **Reynolds** | Re = ρ·v·D / μ | Régime turbulent au-delà de ≈ 4 000 | 
| **Frottement** (Swamee-Jain) | f = 0,25 / [log₁₀(ε/(3,7·D) + 5,74/Re <sup>0,9</sup> )]² | ε = rugosité ≈ 0,045 mm (tube lisse) | 
| **Perte linéaire** | ΔP/m = f·(1/D)·(ρ·v²/2) | Darcy-Weisbach, en Pa/m | 
| **Perte totale** | ΔP = (ΔP/m)·L·(1 + singularités) | singularités en fraction (30 % → 0,30) | 

Les propriétés du fluide sont prises à environ 10–20 °C : pour l'**eau**, masse volumique ρ ≈ 998 kg/m³ et viscosité dynamique μ ≈ 1,002 × 10⁻³ Pa·s ; pour un mélange **eau-glycol 30 %**, ρ ≈ 1 040 kg/m³ et μ ≈ 3 × 10⁻³ Pa·s - un fluide plus visqueux qui augmente les pertes. Le résultat final est converti en **kPa**, en **mCE** (mètres de colonne d'eau, via ΔP / (ρ·g)) et accompagné de la vitesse et du nombre de Reynolds pour vérifier le régime d'écoulement.

**Besoin de fixer d'abord le débit ou le diamètre ?**

Commencez par notre [**calculateur de débit d'eau**](https://inter-fast.fr/ressources/calculateur/calculateurs/calculateur-debit-eau) pour cadrer le débit nominal, ou enchaînez sur le [**dimensionnement de gaines aérauliques**](https://inter-fast.fr/ressources/calculateur/calculateurs/calculateur-dimensionnement-gaines) pour le côté ventilation.

## Exemple chiffré : 2 m³/h en DN25 sur 50 m

Reprenons les valeurs par défaut : un débit de **2 m³/h** dans un tube **DN25** (diamètre intérieur ≈ 26 mm), sur **50 m**, avec **30 % de singularités** et de l'eau.

- **Section** : A = π × 0,026² / 4 ≈ 5,31 × 10⁻⁴ m²
- **Vitesse** : v = (2 / 3600) / A ≈**1,05 m/s** (dans la plage recommandée)
- **Reynolds** : Re ≈ 27 100 → régime**turbulent**
- **Perte linéaire** : ΔP/m ≈**593 Pa/m**
- **Perte totale** : 593 × 50 × 1,30 ≈**38,6 kPa** , soit ≈**3,9 mCE**

Ces 3,9 mCE sont exactement le chiffre à comparer à la hauteur manométrique du circulateur. Si vous montez le débit à 3 m³/h sur le même tube, la perte de charge, qui varie avec le carré de la vitesse, bondit - d'où l'intérêt de passer en DN32 plutôt que de forcer la pompe.

## 3 erreurs fréquentes qui faussent le calcul

### 1. Confondre diamètre nominal et diamètre intérieur

Le DN n'est pas le diamètre intérieur réel. Or la perte de charge varie environ avec la puissance 5 du diamètre : quelques millimètres d'écart changent radicalement le résultat. Utilisez bien le diamètre intérieur du tube réellement posé.

### 2. Oublier les singularités

Sur un réseau riche en coudes, vannes et tés, les pertes locales peuvent représenter 30 à 50 % de la perte linéaire. Les négliger conduit à choisir un circulateur trop juste qui ne tiendra pas le débit.

### 3. Viser une vitesse trop élevée pour réduire le diamètre

Au-delà de 1,5 à 2 m/s, on gagne du cuivre mais on récolte du bruit, de l'érosion et une explosion des pertes de charge. Mieux vaut rester dans la plage 0,5–1,5 m/s.

## Du calcul au devis signé, sans ressaisie

Une fois le réseau dimensionné, transformez-le en chiffrage propre : [le logiciel de devis & factures InterFast](https://inter-fast.fr/fonctionnalites/logiciel-devis-factures) vous aide à éditer des devis CVC clairs et à suivre la marge chantier. [Testez InterFast gratuitement](https://inter-fast.fr).