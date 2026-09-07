---
url: https://inter-fast.fr/ressources/calculateur/calculateurs/calculateur-loi-ohm
url_finale: https://inter-fast.fr/ressources/calculateur/calculateurs/calculateur-loi-ohm
date_collecte: 2026-09-07
destination: site_marketing
---

# Calculateur des lois de l'électricité

Toutes les grandes formules à portée de main : **loi d'Ohm**, **puissance**, **intensité** en mono ou triphasé, **énergie & coût**, **chute de tension** et **association de résistances**. Résultat instantané, sans inscription.

## ⚡ Lois de l'électricité

Choisissez une loi, saisissez vos valeurs, obtenez le résultat

U = R × I · I = U ÷ R · R = U ÷ I

Renseignez deux valeurs, laissez la troisième vide.

P = U × I · P = R × I² · P = U² ÷ R

Renseignez deux valeurs, laissez la troisième vide.

Mono : I = P ÷ (U × cosφ) · Tri : I = P ÷ (√3 × U × cosφ)

E = P × t · Coût = E × prix du kWh

Mono : ΔU = 2 × ρ × L × I × cosφ ÷ S · Tri : ΔU = √3 × ρ × L × I × cosφ ÷ S

Série : R = R₁ + R₂ + … · Parallèle : 1 ÷ R = 1÷R₁ + 1÷R₂ + …

Sur un chantier comme en formation, les **lois de l'électricité** reviennent en permanence : dimensionner un circuit, vérifier l'intensité d'un appareil, estimer une consommation ou contrôler une chute de tension. Toutes reposent sur quelques relations simples entre la **tension** (volts), l'**intensité** (ampères), la **résistance** (ohms) et la **puissance** (watts). Ce calculateur regroupe les principales en un seul outil : **loi d'Ohm**, **loi de Joule** (puissance), **calcul d'intensité** en monophasé et triphasé, **énergie consommée** et coût, **chute de tension** et **association de résistances**. Choisissez l'onglet correspondant, saisissez vos valeurs, le résultat s'affiche instantanément.

## La loi d'Ohm : U = R × I

La **loi d'Ohm** est la relation fondamentale de l'électricité. Elle énonce que la tension aux bornes d'un récepteur est égale au produit de sa résistance par l'intensité qui le traverse. À partir d'une seule formule, on obtient les trois grandeurs en isolant l'inconnue :

| Je cherche | Formule | Unité | 
|---|---|---|
| La tension **U** | U = R × I | volt (V) | 
| L'intensité **I** | I = U ÷ R | ampère (A) | 
| La résistance **R** | R = U ÷ I | ohm (Ω) | 

Dans l'outil, l'onglet **Loi d'Ohm** applique ce principe : renseignez deux des trois valeurs, laissez la troisième vide, et le calculateur la déduit - tout en affichant au passage la puissance dissipée (P = U × I).

## La puissance électrique (loi de Joule) : P = U × I

La **puissance** est l'énergie consommée ou fournie par seconde. Pour un récepteur en courant continu ou purement résistif, elle vaut P = U × I. En combinant avec la loi d'Ohm, on obtient deux variantes très pratiques :

- **P = U × I** - la forme directe (tension × intensité) ;
- **P = R × I²** - utile quand on connaît la résistance et le courant (effet Joule) ;
- **P = U² ÷ R** - utile quand on connaît la tension et la résistance.

C'est cette relation qui explique l'**effet Joule** : un conducteur parcouru par un courant s'échauffe d'autant plus que sa résistance et l'intensité sont élevées. L'onglet **Puissance** du calculateur déduit la grandeur manquante entre P, U et I.

## Calcul de l'intensité en monophasé et triphasé

C'est sans doute le calcul le plus courant pour un électricien : connaître l'**intensité appelée** par un appareil afin de choisir le bon disjoncteur et la bonne section de câble. La formule dépend du type de réseau et du **facteur de puissance cos φ** :

| Réseau | Formule de l'intensité | Tension usuelle | 
|---|---|---|
| **Monophasé** | I = P ÷ (U × cos φ) | 230 V | 
| **Triphasé** | I = P ÷ (√3 × U × cos φ) | 400 V entre phases | 

Le **cos φ** (facteur de puissance) vaut environ 1 pour une charge résistive (convecteur, ballon d'eau chaude, éclairage incandescent), et plutôt 0,8 à 0,9 pour un moteur ou un appareil avec électronique de puissance. Plus le cos φ est faible, plus l'intensité appelée est élevée pour une même puissance utile. L'onglet **Intensité** calcule directement le courant et affiche la **puissance apparente** (en VA) correspondante.

**Vous préparez un tableau électrique complet ?**

Une fois les intensités connues, passez au [**configurateur de tableau électrique**](https://inter-fast.fr/ressources/calculateur/calculateurs/calculateur-tableau-electrique) pour répartir les circuits, les différentiels A/AC et obtenir la liste de matériel selon la NF C 15-100.

## Énergie consommée et coût : E = P × t

L'**énergie** est la puissance intégrée dans le temps. Une puissance de 1 000 W (1 kW) utilisée pendant 1 heure consomme 1 **kilowattheure** (kWh). Le coût s'obtient simplement en multipliant par le prix du kWh :

- **Énergie (kWh)** = P (kW) × durée (h)
- **Coût (€)** = énergie (kWh) × prix du kWh (€)

L'onglet **Énergie & coût** part d'une puissance en watts et d'une durée d'utilisation quotidienne, puis extrapole la consommation et la facture sur le mois et l'année - idéal pour estimer le poids d'un équipement (chauffe-eau, climatiseur, motorisation) ou argumenter un remplacement auprès d'un client.

## La chute de tension d'un câble

Tout câble a une résistance : sur une longue distance, la tension « se perd » en route, c'est la **chute de tension**. Trop élevée, elle fait sous-alimenter les appareils et chauffer les conducteurs. La formule simplifiée retenue par la NF C 15-100 est :

| Réseau | Chute de tension ΔU | 
|---|---|
| **Monophasé** | ΔU = 2 × ρ × L × I × cos φ ÷ S | 
| **Triphasé** | ΔU = √3 × ρ × L × I × cos φ ÷ S | 

Avec **ρ** la résistivité du conducteur (0,0225 Ω·mm²/m pour le **cuivre**, 0,036 pour l'**aluminium**), **L** la longueur en mètres, **I** l'intensité en ampères et **S** la section en mm². La norme fixe une chute de tension maximale de **3 % pour l'éclairage** et de **5 % pour les autres usages**. Au-delà, il faut augmenter la section du câble. L'onglet **Chute de tension** calcule ΔU en volts et en pourcentage, et indique si la valeur reste conforme.

## Association de résistances : série et parallèle

Plusieurs résistances peuvent se combiner pour former une **résistance équivalente**. Le calcul dépend du montage :

- **En série** (résistances bout à bout) : elles s'additionnent, R = R₁ + R₂ + R₃ + … La résistance équivalente est toujours plus grande que la plus grande des résistances.
- **En parallèle** (résistances côte à côte) : 1 ÷ R = 1÷R₁ + 1÷R₂ + … La résistance équivalente est toujours plus petite que la plus petite des résistances.

L'onglet **Résistances** accepte une liste de valeurs séparées par des virgules et renvoie directement la résistance équivalente, en série comme en parallèle.

## Toutes les formules en un coup d'œil

| Loi | Formule principale | Pour trouver… | 
|---|---|---|
| Loi d'Ohm | U = R × I | I = U ÷ R · R = U ÷ I | 
| Puissance (loi de Joule) | P = U × I | P = R × I² · P = U² ÷ R | 
| Intensité monophasée | I = P ÷ (U × cos φ) | P = U × I × cos φ | 
| Intensité triphasée | I = P ÷ (√3 × U × cos φ) | P = √3 × U × I × cos φ | 
| Énergie | E = P × t | Coût = E × prix kWh | 
| Chute de tension (mono) | ΔU = 2 × ρ × L × I × cos φ ÷ S | ΔU % = ΔU ÷ U × 100 | 
| Résistances série | R = R₁ + R₂ + … | - | 
| Résistances parallèle | 1 ÷ R = 1÷R₁ + 1÷R₂ + … | - | 

## 3 erreurs fréquentes

### 1. Oublier le cos φ dans le calcul d'intensité

Pour un moteur ou un appareil avec électronique de puissance, négliger le facteur de puissance (le prendre égal à 1) sous-estime l'intensité réellement appelée - et donc le calibre du disjoncteur et la section de câble.

### 2. Confondre puissance, énergie et intensité

La puissance (W) est instantanée, l'énergie (Wh ou kWh) tient compte de la durée, et l'intensité (A) est le courant. Un appareil « de 2 000 W » ne consomme 2 kWh que s'il fonctionne une heure pleine à pleine puissance.

### 3. Sous-dimensionner sur une grande longueur de câble

Sur une ligne longue, la chute de tension grimpe vite. Vérifiez toujours qu'elle reste sous 3 % (éclairage) ou 5 % (autres usages) : au besoin, augmentez la section plutôt que de rester au calibre minimal.

## Du calcul au devis d'électricité signé

Une fois vos circuits et votre matériel dimensionnés, transformez-les en chiffrage pro : [le logiciel de devis & factures InterFast](https://inter-fast.fr/fonctionnalites/logiciel-devis-factures) aide les électriciens à éditer des devis clairs, gérer la TVA et suivre la marge chantier. [Testez InterFast gratuitement](https://inter-fast.fr).

## FAQ

Pilotez toute votre activité d'électricien au même endroit

Du relevé sur le terrain au devis signé : planning, interventions de dépannage et d'installation, devis, factures et suivi de chantier dans un seul logiciel pensé pour les électriciens.

[Logiciel pour électricien](https://inter-fast.fr/metiers/logiciel-electricien)