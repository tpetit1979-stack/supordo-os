---
url: https://inter-fast.fr/ressources/calculateur/calculateurs/calculateur-debit-eau
url_finale: https://inter-fast.fr/ressources/calculateur/calculateurs/calculateur-debit-eau
date_collecte: 2026-09-07
destination: site_marketing
---

# Calculateur de débit d'eau (chauffage / climatisation)

Convertissez une **puissance en débit d'eau** (ou l'inverse) selon le régime de température et le fluide. Résultat instantané en m³/h, L/min et kW.

## 💧 Débit eau chauffage/clim

Conversion puissance ↔ débit

Choisir un circulateur, dimensionner une tuyauterie, équilibrer un réseau : tout commence par le **débit d'eau**. Or sur le terrain, on connaît rarement le débit directement - on connaît la **puissance** de l'émetteur (radiateur, plancher, ventilo-convecteur) et son **régime de température**. Ce calculateur fait la passerelle dans les deux sens : il convertit une puissance en débit (m³/h, L/min) ou un débit en puissance, en tenant compte du régime et du fluide caloporteur.

## Comment se calcule le débit d'eau ?

Le calcul repose sur le **bilan thermique d'un fluide caloporteur** : la puissance échangée est égale au produit du débit massique, de la capacité thermique du fluide et de l'écart de température entre départ et retour.

| Grandeur | Formule | Unités | 
|---|---|---|
| Puissance | P = qv × ρ × Cp × ΔT | qv en m³/h, ΔT en K | 
| Débit volumique | qv = P ÷ (ρ × Cp × ΔT) | Résultat en m³/h | 
| En litres/minute | qv <sub>L/min</sub> = qv × 1000 ÷ 60 | Pratique pour l'équilibrage | 

Le facteur de conversion vient des unités : avec une puissance en kW, le calculateur écrit `qv = P ÷ (ρ × Cp × ΔT ÷ 3 600 000)`. Les **propriétés du fluide** retenues sont, pour l'eau, ρ ≈ 998 kg/m³ et Cp ≈ 4 185 J/(kg·K) ; pour le glycol 30 %, ρ ≈ 1 040 kg/m³ et Cp ≈ 3 700 J/(kg·K). Le **régime** impose le ΔT :

| Régime | Départ / retour | ΔT retenu | 
|---|---|---|
| Radiateur haute température | 75 / 60 °C | 15 K | 
| Radiateur basse température | 45 / 35 °C | 10 K | 
| Plancher chauffant | 35 / 28 °C | 7 K | 
| Eau glacée (climatisation) | 7 / 12 °C | 5 K | 
| Personnalisé | - | Valeur saisie | 

**Débit connu, place à la tuyauterie.**

Enchaînez avec notre [**calculateur de pertes de charge**](https://inter-fast.fr/ressources/calculateur/calculateurs/calculateur-pertes-de-charge) pour choisir le diamètre, ou dimensionnez vos gaines de soufflage avec le [**calculateur de dimensionnement de gaines**](https://inter-fast.fr/ressources/calculateur/calculateurs/calculateur-dimensionnement-gaines).

## Exemple chiffré : 25 kW en eau glacée

Reprenons les valeurs par défaut : une **puissance de 25 kW** en mode « Puissance → Débit », régime **eau glacée 7/12 °C** (ΔT = 5 K), fluide eau (ρ = 998 kg/m³, Cp = 4 185 J/(kg·K)).

- **Dénominateur** : 998 × 4 185 × 5 ÷ 3 600 000 ≈**5,80**
- **Débit volumique** : 25 ÷ 5,80 ≈**4,31 m³/h**
- **En litres/minute** : 4,31 × 1000 ÷ 60 ≈**71,8 L/min**

À titre de comparaison, la même puissance sur un régime radiateur haute température (ΔT 15 K) ne demanderait qu'environ **1,4 m³/h** - trois fois moins, puisque le débit est inversement proportionnel au ΔT.

## 3 erreurs fréquentes sur le calcul de débit

### 1. Confondre le ΔT du régime et le ΔT réel

Le ΔT à utiliser est l'écart **départ/retour** de l'émetteur, pas l'écart avec l'ambiance. Saisir 20 K parce que « l'eau est à 35 °C et la pièce à 15 °C » fausse complètement le débit.

### 2. Garder le ΔT eau pour du glycol

L'eau glycolée a une capacité thermique plus faible : à puissance et ΔT identiques, elle demande un peu **plus de débit**. Pensez à sélectionner le bon fluide dans le calculateur.

### 3. Oublier que basse température = gros débit

Un plancher chauffant ou un régime basse température réduit le ΔT, donc augmente fortement le débit. Tuyauteries et circulateurs doivent être dimensionnés en conséquence, sous peine de bruit et de manque de débit.

## Du calcul au devis signé, sans ressaisie

Une fois le débit et le matériel validés, transformez-les en chiffrage propre : [le logiciel de devis & factures InterFast](https://inter-fast.fr/fonctionnalites/logiciel-devis-factures) vous aide à éditer des devis CVC clairs et à suivre la marge chantier. [Testez InterFast gratuitement](https://inter-fast.fr).