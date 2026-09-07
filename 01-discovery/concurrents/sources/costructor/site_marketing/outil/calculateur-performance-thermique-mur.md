---
url: https://costructor.co/outil/calculateur-performance-thermique-mur
url_finale: https://costructor.co/outil/calculateur-performance-thermique-mur/
date_collecte: 2026-09-07
destination: site_marketing
---

# Calculatrice de performance thermique d’un mur

**Calculez la performance thermique d’un bâtiment**, couche par couche, avec notre calculateur. Cet outil gratuit s’adresse aux maçons, façadiers, constructeurs et particuliers qui envisagent une rénovation énergétique. Pour chaque couche, indiquez le matériau et son épaisseur, et obtenez instantanément l’indice de performance thermique. 

Couches du mur

De l’extérieur vers l’intérieur · jusqu’à 5 couches

Veuillez compléter au moins une couche (matériau + épaisseur).

Détail par couche

      R = R<sub>si</sub>(0,13) + Σ(e/λ) + R<sub>se</sub>(0,04)  ·  Formule EN ISO 6946 — paroi verticale
    

## Comment utiliser le calculateur de résistance thermique ?

Saisissez les épaisseurs pour chaque couches de votre mur, de l’extérieur vers l’intérieur. Chaque couche correspond à un matériau : brique, isolant, matériaux bois…

- **Matériau** : sélectionnez dans la liste déroulante, organisée par famille (structures porteuses, isolants, matériaux bois, finitions).
- **Épaisseur** : indiquez l’épaisseur de chaque couche en centimètres.

Une fois toutes les couches renseignées, cliquez sur **Calculer la performance** pour obtenir :

- la résistance thermique totale **R** (en m²·K/W) ;
- le **coefficient U** (en W/m²·K) ;
- l’**indice A à G** , comparable à une étiquette énergie ;
- l’**épaisseur totale** du mur ;
- le **détail par couche** avec la contribution de chaque matériau.

## Comment calculer la résistance thermique d’un mur ?

La résistance thermique d’un mur se calcule en additionnant les résistances de chaque couche de matériau, plus les résistances de surface. Pour chaque couche, la formule est simple :

**R = e / λ**

Où **e** est l’épaisseur en mètres et **λ** (lambda) la conductivité thermique du matériau en W/m·K. Plus λ est faible, meilleur est l’isolant — la laine de verre affiche λ = 0,035 W/m·K, quand le béton banché monte à 1,75 W/m·K.

La résistance thermique totale de la paroi (conforme à la norme [NF EN ISO 6946](https://www.iso.org/standard/65708.html)) est :

**R_total = Rse + R₁ + R₂ + … + Rn + Rsi**

Les **résistances de surface** (Rsi = 0,13 m²K/W côté intérieur, Rse = 0,04 m²K/W côté extérieur) modélisent les échanges convectifs à la surface de la paroi pour une paroi verticale. Le calculateur les intègre systématiquement sans que vous ayez à les saisir.

Le **coefficient U** est l’inverse de R_total :

**U = 1 / R_total**

Un U faible indique un mur peu conducteur. La RE2020 fixe un seuil de U ≤ 0,30 W/m²·K pour les murs extérieurs neufs, ce qui correspond à R_total ≥ 3,3 m²K/W environ. Pour la RT 2012, le seuil était identique, mais la RE2020 encourage en pratique des valeurs bien meilleures pour atteindre les objectifs carbone.

## Quels seuils de résistance thermique pour les murs en RE2020 ?

La RE2020 fixe un U ≤ 0,30 W/m²K pour les murs extérieurs des constructions neuves. L’indice A–G affiché par le calculateur traduit ce coefficient en une échelle lisible, du niveau passif (A) au mur non isolé (G).

| Indice | U (W/m²K) | R total (m²K/W) | Interprétation | 
|---|---|---|---|
| A | ≤ 0,15 | ≥ 6,7 | Niveau passif — dépasse largement la RE2020 | 
| B | 0,15 – 0,22 | 4,5 – 6,7 | Très bonne isolation — niveau BBC-E ou label E+C- | 
| C | 0,22 – 0,30 | 3,3 – 4,5 | Conforme RE2020 pour construction neuve | 
| D | 0,30 – 0,45 | 2,2 – 3,3 | Insuffisant en neuf — acceptable en rénovation légère | 
| E | 0,45 – 0,60 | 1,7 – 2,2 | Isolation insuffisante — amélioration recommandée | 
| F | 0,60 – 0,80 | 1,25 – 1,7 | Mauvaise isolation — murs anciens non ou peu isolés | 
| G | > 0,80 | < 1,25 | Très mauvaise isolation — pierre ou béton brut sans isolant | 

En rénovation, les exigences sont assouplies selon la zone climatique (H1, H2, H3) et le type d’intervention, mais atteindre au minimum la classe D reste l’objectif minimal pour tout travail d’isolation subventionné (MaPrimeRénov’).

## Résistance thermique de compositions de murs courants

Pour calibrer votre projet, voici les performances calculées pour des compositions de murs fréquemment rencontrées sur les chantiers. Les valeurs intègrent les résistances de surface (Rsi + Rse = 0,17 m²K/W) mais pas les enduits, pour isoler la contribution structurelle et isolante.

| Composition du mur | Épaisseur totale | R total | U | Indice | 
|---|---|---|---|---|
| Parpaing 20 cm seul (sans isolation) | 20 cm | 0,38 m²K/W | 2,60 W/m²K | G | 
| Parpaing 20 cm + ITE laine de roche 10 cm | 30 cm | 3,0 m²K/W | 0,33 W/m²K | D | 
| Parpaing 20 cm + ITE laine de roche 14 cm | 34 cm | 3,9 m²K/W | 0,26 W/m²K | C | 
| Béton cellulaire 30 cm (monomur) | 30 cm | 3,2 m²K/W | 0,31 W/m²K | D | 
| Béton banché 20 cm + ITE PUR/PIR 12 cm | 32 cm | 5,1 m²K/W | 0,20 W/m²K | B | 
| Ossature bois : BA13 + laine de bois 15 cm + OSB 8 mm | 18 cm | 4,0 m²K/W | 0,25 W/m²K | C | 
| Mur en pierre calcaire 60 cm (maçonnerie ancienne) | 60 cm | 0,6 m²K/W | 1,67 W/m²K | G | 

Le constat est net : un mur en parpaing nu (sans isolation) est en classe G, alors que l’ajout de 14 cm de laine de roche en ITE le fait passer en classe C, conforme RE2020. Le polyuréthane, plus performant par centimètre (λ = 0,025 W/m·K), permet d’atteindre la classe B avec seulement 12 cm. L’ossature bois offre de bons résultats pour des épaisseurs réduites.

## FAQ – Calculateur thermique mur

### Quelle est la formule pour calculer la résistance thermique d’un mur ?

La résistance thermique d’un mur multicouche est la somme des résistances de chaque couche, plus les résistances de surface. Pour chaque couche : R = épaisseur (m) / conductivité thermique λ (W/m·K). Le R_total inclut Rsi = 0,13 m²K/W (face intérieure) et Rse = 0,04 m²K/W (face extérieure), conformément à la norme NF EN ISO 6946 pour les parois verticales.

### Quelle différence entre R et U pour un mur ?

R est la résistance thermique (m²K/W) : plus elle est élevée, mieux le mur isole. U est le coefficient de transmission thermique (W/m²K), égal à l’inverse de R_total (U = 1/R_total). La RE2020 exprime ses exigences en U, mais les deux grandeurs sont interchangeables : améliorer R, c’est diminuer U.

### Quelle résistance thermique pour un mur conforme RE2020 ?

La RE2020 impose U ≤ 0,30 W/m²K pour les murs extérieurs en construction neuve, soit R_total ≥ 3,3 m²K/W. Pour un mur en parpaing de 20 cm (R ≈ 0,21 m²K/W hors surfaces), il faut ajouter au minimum 12 à 14 cm de laine de roche ou 8 à 10 cm de polyuréthane pour atteindre ce seuil.

### Cet outil est-il conforme aux normes en vigueur ?

Le calculateur applique la méthode de la norme NF EN ISO 6946 avec les résistances de surface standard (Rsi = 0,13, Rse = 0,04 m²K/W). Les valeurs λ utilisées correspondent aux valeurs déclarées des matériaux courants. Pour un projet soumis à dépôt de permis de construire, les valeurs certifiées fabricant et l’intervention d’un thermicien restent indispensables.

### Peut-on utiliser cet outil pour un projet de rénovation ?

Oui. Saisissez d’abord le mur existant pour obtenir sa performance de départ, puis ajoutez une couche d’isolant (ITE ou ITI) pour simuler le gain de R et l’évolution de l’indice. C’est un bon moyen de comparer rapidement différents scénarios — 10 cm vs 14 cm, laine de roche vs fibre de bois — avant de demander des devis.

### L’indice A à G correspond-il au DPE du logement ?

Non. L’indice affiché concerne uniquement la performance thermique du mur calculé. Le DPE (Diagnostic de Performance Énergétique) intègre l’ensemble des parois, les équipements de chauffage, la ventilation et les apports solaires selon la méthode réglementaire 3CL-DPE. Un mur en classe C ne garantit pas un DPE C pour le logement.

### Qui peut utiliser ce calculateur ?

Maçons, façadiers, constructeurs, thermiciens et particuliers. L’outil ne nécessite aucune connaissance en thermique avancée : il suffit de connaître les matériaux et les épaisseurs de sa paroi. Pour les professionnels, il constitue un outil de vérification rapide en phase conception ou en réponse client, complémentaire des logiciels de calcul réglementaire.