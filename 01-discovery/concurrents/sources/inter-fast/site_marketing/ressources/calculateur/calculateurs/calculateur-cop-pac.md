---
url: https://inter-fast.fr/ressources/calculateur/calculateurs/calculateur-cop-pac
url_finale: https://inter-fast.fr/ressources/calculateur/calculateurs/calculateur-cop-pac
date_collecte: 2026-09-07
destination: site_marketing
---

# Calculateur de COP de pompe à chaleur

Estimez le **COP réel** d'une pompe à chaleur à partir de la température extérieure, de la température de départ d'eau et de la qualité du matériel. Résultat instantané avec coût annuel et économie estimée.

## ♻️ COP & Performance PAC

COP réel selon les conditions de fonctionnement.

Une pompe à chaleur ne « produit » pas de chaleur, elle la déplace : pour 1 kWh d'électricité consommé, elle restitue plusieurs kWh de chaleur. Ce rapport, c'est le **COP** (coefficient de performance). Mais le COP affiché sur la brochure (mesuré à 7 °C / 35 °C) n'a rien à voir avec celui d'un matin à −5 °C avec des radiateurs à 55 °C. Ce calculateur estime le **COP réel** à partir des vraies conditions de fonctionnement - température extérieure, température de départ d'eau et qualité du matériel - et le traduit en **coût annuel** et en **économie** face à un chauffage électrique direct.

## Comment se calcule le COP réel d'une pompe à chaleur ?

Le calculateur part de la limite physique théorique - le **COP de Carnot** - puis la corrige par un **rendement exergétique** qui traduit la qualité réelle de la machine. Toutes les températures sont converties en kelvin (K = °C + 273,15).

| Étape | Formule | Détail | 
|---|---|---|
| **COP de Carnot** | COPc = Tc / (Tc − Ts) | Tc = départ d'eau, Ts = source (en K) | 
| **COP réel** | COP = COPc × η | η exergétique : 0,35 / 0,42 / 0,50 | 
| **Dégradation grand froid** | × 0,85 si T <sub>ext</sub> < −7 °C, × 0,80 si < −15 °C | aérothermie uniquement (pas géo) | 
| **Puissance électrique** | P <sub>élec</sub> = P<sub>calo</sub> / COP | consommation absorbée | 
| **Coût annuel** | P <sub>élec</sub> × 2 000 h × 0,22 €/kWh | comparé au chauffage direct (P <sub>calo</sub> ) | 

La **source froide Ts** vaut la température extérieure pour une PAC aérothermique (air/eau, air/air), mais elle est fixée à **10 °C** pour la géothermie, car le sol reste tempéré toute l'année - c'est ce qui rend la géothermie si stable. Le **rendement exergétique η** reflète la qualité : 0,35 en entrée de gamme, 0,42 en milieu de gamme, 0,50 en premium. Enfin, le COP réel est plafonné à 1 minimum, et le calculateur le classe : ≥ 4,5 « Excellent (A+++) », ≥ 3,5 « Bon (A++) », ≥ 2,5 « Moyen (A+) », en dessous « Médiocre ».

**Quelle puissance de PAC installer derrière ce COP ?**

Dimensionnez d'abord le besoin avec notre [**calculateur de bilan thermique chauffage**](https://inter-fast.fr/ressources/calculateur/calculateurs/calculateur-bilan-thermique-chauffage), et affinez l'isolation qui conditionne la température de départ avec le [**calcul du coefficient U d'une paroi**](https://inter-fast.fr/ressources/calculateur/calculateurs/calculateur-coefficient-u-paroi).

## Exemple chiffré : une PAC air/eau à 7 °C / 35 °C

Reprenons les valeurs par défaut : PAC **air/eau**, température extérieure **7 °C**, départ d'eau **35 °C** (plancher chauffant), puissance calorifique **10 kW**, matériel **milieu de gamme** (η = 0,42).

- **Températures en kelvin** : Ts = 280,15 K, Tc = 308,15 K
- **COP de Carnot** : 308,15 / (308,15 − 280,15) = 308,15 / 28 ≈**11,0**
- **COP réel** : 11,0 × 0,42 ≈**4,62** (pas de dégradation, 7 °C > −7 °C) →**Excellent (A+++)**
- **Puissance électrique** : 10 / 4,62 ≈**2,16 kW**
- **Coût annuel** : 2,16 × 2 000 × 0,22 ≈**952 €** contre ≈ 4 400 € en chauffage direct →**≈ 3 450 € d'économie**

Refaites le calcul avec un départ à 55 °C (radiateurs) ou une extérieure à −10 °C : le COP s'effondre et l'économie fond. C'est toute la démonstration de l'intérêt d'un émetteur basse température et d'une bonne isolation en amont.

## 3 erreurs fréquentes sur le COP

### 1. Confondre le COP brochure avec le COP réel

Le COP catalogue est mesuré dans des conditions idéales (7 °C / 35 °C). Sur site, avec du froid et des radiateurs chauds, le COP réel est souvent bien plus bas. Raisonnez en conditions réelles, pas en valeur marketing.

### 2. Choisir une température de départ trop haute

Chaque degré de départ d'eau en moins fait gagner du COP. Conserver des radiateurs à 60 °C « parce que c'est ce qui existait » sabote la performance : mieux vaut surdimensionner les émetteurs pour baisser la loi d'eau.

### 3. Ignorer le climat du site

En zone froide, une PAC aérothermique perd beaucoup par grand froid et peut basculer sur sa résistance d'appoint. La géothermie, plus stable, ou un bon dimensionnement avec appoint maîtrisé évitent les mauvaises surprises sur la facture.

## Du calcul au devis signé, sans ressaisie

Une fois la PAC choisie, transformez l'étude en chiffrage propre : [le logiciel de devis & factures InterFast](https://inter-fast.fr/fonctionnalites/logiciel-devis-factures) vous aide à éditer des devis PAC clairs et à suivre la marge chantier. [Testez InterFast gratuitement](https://inter-fast.fr).