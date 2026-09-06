---
source: https://intercom-help.eu/vertuoza/fr/articles/455278-zones-de-deplacement-et-panier-repas-france
categorie: BETA
titre: Zones de déplacement et panier repas (France)
date_recuperation: 2026-09-05
---

# Zones de déplacement et panier repas (France)

En France, le secteur du bâtiment est encadré par des conventions collectives qui prévoient des indemnités spécifiques liées aux conditions de travail :

- **Indemnités de déplacement** : calculées selon les zones géographiques définies (petit déplacement) ou le nombre d’heures de trajet (grand déplacement).
- **Indemnités de panier repas** : versées lorsque l’ouvrier ne peut pas rentrer chez lui pour déjeuner.

Cette fonctionnalité permet **l’encodage automatisé** de ces indemnités, afin de **faciliter et fiabiliser le calcul des fiches de paie**.

⚠️ **Note :**
Il n’y a pas d’impact sur la rentabilité des chantiers pour l’instant, car les indemnités sont calculées à la journée et ne peuvent pas encore être réparties sur plusieurs chantiers.

___________________________________________________________

### ⚙️ Paramétrage des zones et paniers repas

Le paramétrage se fait depuis **Paramètres > Pointage > Préférences**.
Plusieurs sections permettent d’adapter la configuration selon les besoins de votre entreprise.


### 1️⃣ Gestion des pointages

Permet d’activer le **module de pointage** pour l’encodage et la validation des heures de travail dans les comptes chantiers et gestion.


### 2️⃣ Paramétrage des trajets

Cette section permet d’activer ou de masquer certains champs relatifs aux trajets dans l’application Ouvrier et dans la Web App.

Les options disponibles sont :

- **Points de départ et d’arrivée** → permet de sélectionner le lieu de départ (domicile, entreprise, hôtel).
- **Type de véhicule** → utile si vous distinguez les véhicules personnels et ceux de société.
- **Durée de trajet** → active la saisie du temps de transport (utile pour les grands déplacements).
- **Distance parcourue** → permet d’encoder les kilomètres parcourus (non utilisée pour la France).
- **Rôles de transport** → indique si la personne est chauffeur, passager, etc.

💡 Exemple :
Si vos ouvriers effectuent uniquement des petits déplacements avec des véhicules d’entreprise, vous pouvez masquer les champs “Lieu de départ” ou “Type de véhicule” pour simplifier la saisie.


### 3️⃣ Gestion des paniers repas, restaurant et hôtel (France)

Permet d’activer le calcul automatique des paniers repas et des indemnités d’hébergement.

- Seuil d’attribution automatique : 5 heures travaillées par défaut
→ Si un ouvrier travaille plus de 5 heures, un panier repas est attribué automatiquement.

Les informations apparaissent ensuite dans l’export comptable pour que le comptable ou le secrétariat social réalise le calcul final.


🟢 **Bon à savoir :**
Les paniers doivent être notés dans la remarque du pointage, et non dans la remarque du chantier.



### 4️⃣ Zones de déplacements (France)

Activez cette option pour permettre le calcul automatique des **zones de petits déplacements** selon la localisation du chantier.

- **Calcul des déplacements depuis** : choisissez la base de calcul (Entreprise ou Domicile).
- Cliquez sur ⚙️ **Configuration des zones** pour définir vos zones (1A, 1B, 2, 3, 4, 5).

📍 **Important :**

- Les zones sont calculées à partir du **siège social**.
- Chaque chantier doit avoir une **adresse** renseignée pour être pris en compte.
- Les montants ne sont pas saisis dans Vertuoza : ils seront calculés par le comptable à partir de l’export.

### 5️⃣ Heures supplémentaires (France)

Permet d’activer le calcul automatique des **heures supplémentaires** hebdomadaires selon la législation française :

- **Première majoration** : 25 % entre 35 et 43 heures
- **Deuxième majoration** : 50 % à partir de 43 heures

### 6️⃣ Heures de nuit

Permet d’intégrer le calcul automatique des heures de nuit dans les exports de pointage.

- **Période de nuit** : de 20h00 à 06h00 (modifiable selon vos besoins).

### 🚧 Détails pratiques sur les déplacements

### Petit déplacement

L’ouvrier se rend sur chantier et rentre chez lui le soir.

Indemnités concernées :

- **Trajet** : le temps de déplacement n’est pas compté comme temps de travail chantier.
- **Transport** : remboursement du coût (train, essence, etc.).
- **Panier repas** : versé si l’ouvrier ne peut pas déjeuner sur place.

La **zone** dépend de la distance entre le **siège social** et le **chantier** (Zone 1 → 5).

___________________________________________________________

### Grand déplacement

L’ouvrier se rend sur un chantier éloigné et reste sur place (hôtel).

Indemnités concernées :

- Temps de trajet rémunéré
- Hébergement et repas (nombre de nuits et de repas)
Aucune notion de zone ici.

Les informations (lieu, nuitées, repas) peuvent être notées directement dans la **remarque du pointage**.

___________________________________________________________

### 📱 Comment ça fonctionne dans Vertuoza

De nouveaux champs sont disponibles :

- **Temps de trajet aller / retour**
- **Lieu de départ et d’arrivée**
- **Type de véhicule**
- **Zone de déplacement**
- **Panier repas**

Ces champs apparaissent :

- Dans l’**application mobile** (pointage ouvrier)
- Dans la **Web App** (édition d’un pointage)

___________________________________________________________

### Exemple – Mobile :

![](https://downloads.intercomcdn.eu/i/o/yr18hzl2/70996307/210d5f776e5da14681ade7fcf1a4/image.png?expires=1788634800&signature=b1d2a2ccf349776851f4886aa2a7536fe54b1debd7f264281b5cfb1af8525289&req=19VmzF75rDBk2hL085ZhoRGNhDGofKNMEIB3kPxReCOapeeE%2Bfm6wBrJc%2FoR%0AJZMHWN%2FPWntRXfnc%0A)

### 

Exemple – Web :

![](https://downloads.intercomcdn.eu/i/o/yr18hzl2/70996433/4f87605210860acb4df837739c08/image.png?expires=1788634800&signature=7124c3fcf466697f6476417a86dc5d778c02654cbc95c0e6c529255686e1b023&req=19VmzF7%2BrzRk2hL085ZhoZUZzdo2f7Eay8rUJ8tpxRGdy0PNZBg5aYxj2wGA%0ACaWiIba4gx6Vwe4Q%0A)

___________________________________________________________

### 📊 Export Excel

Un nouvel **export Excel – modèle France** est disponible pour visualiser :

- Les zones de déplacement
- Le nombre de paniers repas
- Les heures supplémentaires et heures de nuit
- Les trajets et types de véhicules

Ces données peuvent ensuite être transmises directement au comptable ou au secrétariat social.

![](https://downloads.intercomcdn.eu/i/o/yr18hzl2/70924812/409f28a2dbca3740dbc045002082/image.png?expires=1788634800&signature=4df08a54c87c0aa032ff7f1c2e6f418e6968541832bd676cc0a6d2bde8f80c03&req=19Vmx1zyrTVk2hL085ZhoawVuIf1YAvnY03YMQknF7F0J8OpVNQnlX9Zbrjn%0AidkoFdYzEuOKtRoJ%0A)

Mis a jour le : 24/10/2025
