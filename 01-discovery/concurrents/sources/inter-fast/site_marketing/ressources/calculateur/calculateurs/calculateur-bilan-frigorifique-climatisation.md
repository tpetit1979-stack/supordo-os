---
url: https://inter-fast.fr/ressources/calculateur/calculateurs/calculateur-bilan-frigorifique-climatisation
url_finale: https://inter-fast.fr/ressources/calculateur/calculateurs/calculateur-bilan-frigorifique-climatisation
date_collecte: 2026-09-07
destination: site_marketing
---

# Calculateur de bilan frigorifique (climatisation)

Estimez la puissance de climatisation **pièce par pièce** en intégrant les apports solaires par orientation, les apports internes, les vitrages et la ventilation. Résultat instantané en kW froid et BTU/h.

## ❄️ Bilan thermique - Climatisation

Puissance froid avec apports solaires détaillés, usage du local, vitrages par orientation

En pleine canicule, le client veut « du froid, vite ». Choisir un split au doigt mouillé, c'est la garantie d'un appareil mal calibré : surdimensionné, il cycle court et déshumidifie mal ; sous-dimensionné, il rame à 14 h face à la baie plein sud. Le **bilan frigorifique** tranche en quelques minutes. Ce calculateur estime la **puissance de climatisation pièce par pièce** en additionnant les apports par les parois et vitrages, les **apports solaires par orientation**, le renouvellement d'air et les **apports internes** (occupants, éclairage, équipements).

## Comment se calcule un bilan frigorifique de climatisation ?

En climatisation, on ne lutte plus contre les pertes mais contre les **apports de chaleur** : tout ce qui réchauffe la pièce doit être évacué par le froid. Le calculateur somme quatre postes pour chaque pièce, avant d'appliquer une marge de 10 %.

| Poste d'apport | Formule | Ce qui l'influence | 
|---|---|---|
| **Transmission** (parois + vitrages) | U × surface × ΔT | Isolation, type de vitrage, écart de température | 
| **Apports solaires** | surface <sub>vitrage</sub> × g × I × 0,85 | Orientation du vitrage et facteur solaire g | 
| **Renouvellement d'air** | 0,34 × volume × (vol/h) × ΔT | Type de ventilation | 
| **Apports internes** | occupants × 130 + surface × W/m² <sub>écl</sub> + équipements | Usage du local (séjour, bureau, restaurant…) | 

L'**écart de température ΔT** est la différence entre la **température extérieure d'été** de la zone climatique (35 °C en zone H3 méditerranéenne, 30 °C en H2a) et la température intérieure souhaitée (26 °C par défaut). Le coefficient **0,34 Wh/(m³·K)** représente la capacité thermique volumique de l'air. Pour les apports solaires, chaque vitrage est pondéré par son **facteur solaire g** (0,42 pour un double faible émissivité, jusqu'à 0,85 en simple vitrage) et par l'**ensoleillement I** de son orientation (550 W/m² à l'ouest, 450 au sud, 200 à l'est, 100 au nord), affecté d'un coefficient de simultanéité de 0,85. Le total est enfin converti en **kW froid** et en **BTU/h** (1 kW = 3 412 BTU/h).

**Vous dimensionnez aussi le chauffage du même bâtiment ?**

Basculez sur notre [**calculateur de bilan thermique chauffage**](https://inter-fast.fr/ressources/calculateur/calculateurs/calculateur-bilan-thermique-chauffage), ou affinez la finesse de l'isolation avec le [**calcul du coefficient U d'une paroi**](https://inter-fast.fr/ressources/calculateur/calculateurs/calculateur-coefficient-u-paroi).

## Exemple chiffré : un séjour de 25 m² en zone H3

Prenons un séjour de **25 m²** sous 2,5 m (volume 62,5 m³), isolation RT2012 (U ≈ 0,36), VMC simple flux (0,5 vol/h), consigne 26 °C en zone H3 (été 35 °C, soit **ΔT = 9 K**), occupé par 4 personnes, avec 3 m² de double vitrage faible émissivité (g ≈ 0,42) plein sud (I ≈ 450 W/m²).

- **Transmission** (parois + vitrage) : 0,36 × (≈57,5 − 3) × 9 + 1,6 × 3 × 9 ≈**220 W**
- **Apports solaires** : 3 × 0,42 × 450 × 0,85 ≈**482 W**
- **Renouvellement d'air** : 0,34 × 62,5 × 0,5 × 9 ≈**96 W**
- **Apports internes** : 4 × 130 + 25 × 10 + 100 ≈**870 W**
- **Sous-total** ≈ 1 667 W,**+ 10 % de marge ≈ 1,83 kW** (≈ 6 250 BTU/h) pour ce seul séjour

On remarque que les **apports solaires et internes** pèsent ici bien plus lourd que la transmission : c'est la signature d'un calcul de climatisation. En additionnant toutes les pièces, le calculateur affiche la puissance totale, le ratio en W/m² et une recommandation de matériel (split mural, multi-split, VRV/VRF…).

## 3 erreurs fréquentes qui faussent le dimensionnement froid

### 1. Oublier les apports internes

Une cuisine professionnelle ou une salle de réunion peut dégager plus de chaleur par ses équipements et ses occupants que par ses murs. Renseigner l'usage réel du local change radicalement le résultat : ne raisonnez jamais qu'en surface.

### 2. Négliger l'orientation des vitrages

Une baie plein ouest reçoit le soleil en fin d'après-midi, au pire moment de la journée d'été. Saisir chaque vitrage avec son orientation et son type évite de sous-dimensionner une pièce très exposée.

### 3. Surdimensionner « pour être tranquille »

Une climatisation trop puissante atteint la consigne en quelques minutes, s'arrête, redémarre… Ce cyclage court use le compresseur, déshumidifie mal et dégrade le confort. La marge de 10 % suffit dans la grande majorité des cas.

## Du calcul au devis signé, sans ressaisie

Une fois la puissance froid validée, transformez-la en chiffrage propre : [le logiciel de devis & factures InterFast](https://inter-fast.fr/fonctionnalites/logiciel-devis-factures) vous aide à éditer des devis de climatisation clairs et à suivre la marge chantier. [Testez InterFast gratuitement](https://inter-fast.fr).