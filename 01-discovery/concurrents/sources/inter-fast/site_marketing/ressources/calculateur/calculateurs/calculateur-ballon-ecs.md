---
url: https://inter-fast.fr/ressources/calculateur/calculateurs/calculateur-ballon-ecs
url_finale: https://inter-fast.fr/ressources/calculateur/calculateurs/calculateur-ballon-ecs
date_collecte: 2026-09-07
destination: site_marketing
---

# Calculateur de volume de ballon ECS

Dimensionnez le **volume de stockage d'eau chaude sanitaire** selon le type de bâtiment et les températures de stockage, d'eau froide et de puisage. Volume normalisé et puissance de réchauffage instantanés.

## 🚿 Volume ballon ECS

Dimensionnement stockage eau chaude sanitaire

Un ballon ECS trop petit, c'est la douche froide en fin de soirée et un client mécontent. Trop gros, c'est de l'argent immobilisé, de la place perdue et des pertes par stockage qui pèsent sur la facture. Le bon dimensionnement part toujours des **besoins réels en eau chaude**, puis convertit ces besoins en **volume de stockage** à la température choisie. Ce calculateur fait les deux : il estime le volume normalisé du ballon et la puissance de réchauffage associée, à partir du type de bâtiment et des températures de votre installation.

## Comment se calcule le volume d'un ballon ECS ?

La méthode se déroule en trois temps : estimer les **besoins journaliers** exprimés en litres d'eau à 40 °C, les convertir vers la **température de stockage**, puis arrondir au volume de ballon normalisé.

| Étape | Formule | Remarque | 
|---|---|---|
| Besoins/jour à 40 °C | B <sub>40</sub> = ratio × nombre d'unités | Selon le type de bâtiment | 
| Volume de stockage | V = B <sub>40</sub> × (T<sub>puisage</sub> − T<sub>EF</sub> ) ÷ (T<sub>stockage</sub> − T<sub>EF</sub> ) | Plus on stocke chaud, moins il faut de volume | 
| Puissance réchauffage (8 h) | P = B <sub>40</sub> × 4185 × (T<sub>stockage</sub> − T<sub>EF</sub> ) ÷ (8 × 3600 × 1000) | Réchauffe les besoins en 8 h, en kW | 

L'idée clé : **stocker plus chaud que la température de puisage** permet de réduire le volume, car une partie de l'eau chaude sera mitigée avec de l'eau froide au point d'usage. Les **ratios de besoins** retenus par le calculateur (litres/jour à 40 °C) sont les suivants :

| Type | Base de besoin | Unité | 
|---|---|---|
| Logement T2 | 110 L/j | par logement | 
| Logement T3 | 145 L/j | par logement | 
| Logement T4 | 180 L/j | par logement | 
| Hôtel | 125 L/j | par chambre | 
| Restaurant | 12 L/j | par repas | 
| Bureau | 7 L/j | par personne | 

Le volume calculé est ensuite arrondi au **ballon normalisé** immédiatement supérieur de la série standard (50, 75, 100, 150, 200, 250, 300, 400, 500 L…). Le calculateur vérifie aussi que la température de stockage reste **≥ 55 °C**, seuil anti-légionelle.

**L'ECS produite par une pompe à chaleur ?**

Vérifiez la performance réelle avec notre [**calculateur de COP de pompe à chaleur**](https://inter-fast.fr/ressources/calculateur/calculateurs/calculateur-cop-pac), ou estimez le besoin de chauffage du logement avec le [**calculateur de bilan thermique chauffage**](https://inter-fast.fr/ressources/calculateur/calculateurs/calculateur-bilan-thermique-chauffage).

## Exemple chiffré : un logement T3

Reprenons les valeurs par défaut : un **logement T3** (besoin 145 L/j à 40 °C), **1 unité**, stockage à **55 °C**, eau froide à **10 °C**, puisage à **40 °C**.

- **Besoins à 40 °C** : 145 × 1 =**145 L/jour**
- **Volume de stockage** : 145 × (40 − 10) ÷ (55 − 10) = 145 × 30 ÷ 45 ≈**97 L**
- **Volume normalisé** : on retient un ballon de**100 L** (premier standard ≥ 97)
- **Puissance de réchauffage (8 h)** : 145 × 4185 × 45 ÷ (8 × 3600 × 1000) ≈**0,95 kW**

Le stockage à 55 °C respecte le seuil anti-légionelle : le calculateur affiche un voyant conforme. En stockant à 60 °C, le même besoin tiendrait dans un volume encore plus réduit.

## 3 erreurs fréquentes en dimensionnement ECS

### 1. Confondre volume stocké et volume puisé

Les besoins s'expriment en eau mitigée à 40 °C, mais le ballon stocke à 55-60 °C. Oublier la conversion par les températures conduit à **surdimensionner** inutilement le ballon.

### 2. Descendre la température de stockage sous 55 °C

Stocker « tiède » pour économiser fait courir un **risque sanitaire** : sous 50 °C, la légionelle prolifère. Le calculateur alerte dès que le stockage passe sous 55 °C.

### 3. Négliger la puissance de réchauffage

Un grand volume sans puissance suffisante met trop longtemps à remonter en température après une grosse puisée. Le couple **volume / puissance** doit être cohérent avec le rythme d'utilisation réel.

## Du calcul au devis signé, sans ressaisie

Une fois le ballon dimensionné, transformez-le en chiffrage propre : [le logiciel de devis & factures InterFast](https://inter-fast.fr/fonctionnalites/logiciel-devis-factures) vous aide à éditer des devis plomberie / CVC clairs et à suivre la marge chantier. [Testez InterFast gratuitement](https://inter-fast.fr).