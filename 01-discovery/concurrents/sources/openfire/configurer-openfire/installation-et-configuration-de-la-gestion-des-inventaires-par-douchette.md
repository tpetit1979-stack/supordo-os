---
source: https://support.openfire.fr/hc/fr/articles/29102059033372-Installation-et-configuration-de-la-gestion-des-inventaires-par-douchette
categorie: Configurer OpenFire
titre: Installation et configuration de la gestion des inventaires par douchette
date_recuperation: 2026-09-05
---

# Installation et configuration de la gestion des inventaires par douchette

Ce guide vous explique comment paramétrer les groupes d'options de code-barres dans OpenFire afin d'adapter l'utilisation de votre douchette à vos processus de stock. Grâce à ces réglages, vous optimiserez la saisie des réceptions, des expéditions et des inventaires tout en réduisant les erreurs de manipulation.

Cet article contient les sections suivantes :

- [Chemin d'accès de la fonctionnalité](#h_01KY6Z83Y2756Q98Z352GG35GF)
- [1. Identification du groupe d'options](#h_01KY6Z83Y30SWBBS4TY3N7SA7P)
- [2. Mode de fonctionnement et saisie](#h_01KY6ZEMBV57PCG0CS12SQ8FYF)
- [3. Gestion des mouvements de stock](#h_01KY6Z83Y84V8EA7QXJ84WF2EJ)
- [4. Saisie et validation des quantités](#h_01KY6Z83YBHEW1V9XH80593DCY)
- [5. Traitement des lots et numéros de série](#h_01KY6Z83YE2MZ7171TS08E2WKH)
- [6. Emplacements, rangement et colisage](#h_01KY6Z83YGG11BM1FRYXD18YVH)
- [7. Interface et notifications](#h_01KY6Z83YJM3Y8YC7C0A1TPAJ6)
- [8. Regroupement des mouvements à traiter](#h_01KY6Z83YKDK06B773M2F63221)
- [9. Configuration des lignes d'options par champ](#h_01KY6Z83YMCTKQ7RM3RR7BJZ57)
- [Créer et enregistrer un groupe d'options](#h_01KY6Z83YPH40C70SWV0JR135R)
- [Exemple pour une configuration simple de l'inventaire](#h_01KY6ZFJ3V9YGMFW50XNXCJ2SD)
- [Bonnes pratiques](#h_01KY6ZGNZYKSSWFE8QWJP98QEP)

### Chemin d'accès de la fonctionnalité

Suivre le chemin d'accès suivant : **Inventaire** > **Configuration** > **Options de code-barres**.

### 1. Identification du groupe d'options

La section d'identification permet de nommer et de catégoriser votre profil de configuration.

- **Nom** : nom clair décrivant le groupe de réglages (exemple : *Réception Magasin*, *Sortie Chantier*).
- **Code** : identifiant court en majuscules permettant de reconnaître rapidement le type d'opération associé dans le système. 🧑‍🏫Exemple : Utilisez les codes **IN** pour les réceptions, **OUT** pour les expéditions, **REL** pour les réapprovisionnements ou **INT** pour les transferts internes.

### 2. Mode de fonctionnement et saisie

Ces paramètres définissent la manière dont l'opérateur interagit avec l'écran lors du scan.

- **Mode** : sélectionnez le mode **Guidé** pour que l'interface indique étape par étape à l'utilisateur quel produit, emplacement ou lot scanner. Le système contrôle la cohérence de chaque scan en direct.
- **Entrée manuelle** : cochez cette case pour activer la saisie au clavier dès l'ouverture de la page. L'opérateur peut modifier des informations à la main tout en gardant le lecteur actif.
- **Champ focus en saisie manuelle** : indiquez quel champ reçoit le curseur en priorité lors de l'ouverture de la saisie manuelle (par défaut : le champ **Emplacement**).

### 3. Gestion des mouvements de stock

Déterminez quelles opérations et informations s'affichent sur l'écran de la douchette.

- **Mouvements confirmés** : permet de traiter des mouvements de stock sans réservation préalable de marchandises en magasin.
- **Afficher les mouvements en attente** : affiche la liste des articles qu'il reste à scanner pour finaliser la commande ou le transfert.
- **Source des mouvements en attente** : choisissez l'origine des données affichées à l'écran entre les **Opérations détaillées** (détail par lot et emplacement) ou les **Opérations** (vue globale).
- **Opérations détaillées** : affiche directement les lignes de détail du transfert sur l'écran du lecteur.
- **Conserver les valeurs à l'écran** : maintient les informations saisies (comme un numéro d'emplacement ou de lot) d'un scan à l'autre jusqu'à la fin du traitement du mouvement.

💡Note : Conserver les valeurs à l'écran est idéal lorsque vous scannez plusieurs produits issus d'un même emplacement ou appartenant à un même lot.

### 4. Saisie et validation des quantités

Ajustez la manière dont les quantités d'articles sont comptabilisées lors de la lecture.

- **Quantité manuelle** : affiche systématiquement le champ quantité en mode édition pour forcer l'opérateur à valider ou saisir la quantité à la main.
- **Confirmation manuelle** : exige l'appui sur un bouton pour valider l'opération. Aucun scan ne valide automatiquement le mouvement.
- **Accumuler les quantités lues** : additionne chaque nouveau scan à la quantité déjà lue au lieu de remplacer la valeur existante.
- **Autoriser quantité négative** : permet d'effectuer un mouvement même si la quantité scannée est supérieure au stock disponible.

🚨Avertissement : L'activation de l'option **Autoriser quantité négative** peut générer des erreurs d'inventaire sur votre base OpenFire. Réservez cette option à des cas exceptionnels ou à des flux d'urgence.

### 5. Traitement des lots et numéros de série

Facilitez la traçabilité de vos équipements et matériaux lors des opérations de scan.

- **Obtenir les lots automatiquement** : sélectionne le lot automatiquement en appliquant vos règles de sortie de stock (exemple : FIFO - Premier entré, premier sorti).
- **Créer les lots manquants** : crée automatiquement un nouveau numéro de lot dans OpenFire si le code-barres scanné est inconnu.
- **Renseigner les champs à partir du lot** : complète automatiquement le produit, l'emplacement et le colis dès que le code-barres du lot est lu.
- **Ignorer quantité en stock** : ne prend pas en compte la disponibilité en stock lors de la lecture d'un lot ou d'un colis.

### 6. Emplacements, rangement et colisage

Organisez le déplacement de vos marchandises au sein de votre dépôt ou de vos véhicules.

- **Empl. dest. - Rangement** : calcule et propose automatiquement l'emplacement de destination idéal en fonction de vos règles de rangement configurées.
- **Tri par emplacement** : classe les mouvements à réaliser sur l'écran selon les coordonnées logistiques des emplacements (origine ou destination).
- **Mise en colis auto.** : regroupe automatiquement les articles scannés dans un colis avant la validation finale du transfert.

### 7. Interface et notifications

Personnalisez le confort visuel de vos collaborateurs pendant la saisie.

- **Ignorer champs renseignés** : empêche la douchette de réécrire sur une donnée déjà validée si un champ obligatoire est déjà rempli.
- **Afficher les notifications Odoo** : affiche des messages d'alerte contextuels (pop-ups) sur l'écran web en cas d'erreur ou d'événement important.
- **Lire les articles (mode inventaire)** : affiche au fur et à mesure la liste des articles scannés pendant vos opérations d'inventaire.

### 8. Regroupement des mouvements à traiter

Organisez la liste de travail de l'opérateur pour lui éviter des déplacements inutiles dans le dépôt.

- **Clé de regroupement** : définit sous forme de règle technique comment rassembler les lignes de stock dans la liste « À faire » de la douchette.

🧑‍🏫Exemple : La valeur `object.location_id,object.product_id,object.lot_id` permet de regrouper les articles à traiter par emplacement, puis par produit, et enfin par lot.

### 9. Configuration des lignes d'options par champ

Au bas du groupe d'options, vous trouvez la liste des champs individuels (emplacements, produits, lots, etc.). Chaque ligne permet de définir précisément le comportement champ par champ :

- **Nom** : libellé lisible du champ dans l'application (ex : **Emplacement**, **Produit**, **Lot**).
- **Nom de champ** : nom technique du champ utilisé par le système OpenFire.
- **Étape** : numéro d'étape dans le parcours de scan. Détermine l'ordre dans lequel les champs doivent être scannés.
- **Séquence** : ordre d'affichage du champ au sein d'une même étape.
- **À scanner** : autorise la saisie de ce champ au moyen d'un scan de code-barres.
- **Obligatoire** : rend la saisie de ce champ obligatoire avant de pouvoir valider l'opération.

### Créer et enregistrer un groupe d'options

Pour configurer un nouveau groupe d'options de code-barres dans votre base :

1. Accéder au menu des options de code-barres.
2. Cliquer sur le bouton **Créer**.
3. Saisir le **Nom** et le **Code** de votre groupe d'options.
4. Cocher ou décocher les options souhaitées dans les différentes sections selon votre besoin métier.
5. Ajouter ou ajuster les lignes dans le tableau inférieur pour définir les règles par champ.
6. Cliquer sur le bouton **Enregistrer**.

### Exemple pour une configuration simple de l'inventaire

Paramètre de base :

- Saisie manuelle de l'emplacement
- Comptage par accumulation

![](https://support.openfire.fr/hc/article_attachments/29102359611036)

![](https://support.openfire.fr/hc/article_attachments/29102359613084)

![](https://support.openfire.fr/hc/article_attachments/29102382731420)

### Bonnes pratiques

- **Testez vos réglages en conditions réelles** : effectuez une simulation de réception ou d'expedition avec une douchette de test après toute modification importante de configuration.
- **Simplifiez le parcours terrain** : si vos techniciens ou magasiniers travaillent rapidement, privilégiez l'option **Obtenir les lots automatiquement** et limitez le nombre de confirmations manuelles.
- **Distinguez les profils** : créez un groupe d'options distinct pour les entrées de stock et pour les sorties afin de ne pas alourdir l'interface utilisateur.

###

Mis a jour le : 23/07/2026
