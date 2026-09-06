---
source: https://intercom-help.eu/vertuoza/fr/articles/132285-devis
categorie: Devis
titre: Devis
date_recuperation: 2026-09-05
---

# Devis

Les devis sont la première étape de la gestion de chantier depuis Vertuoza. Ils peuvent être créés ligne par ligne à partir de poste libre, en récupérant des ouvrages ou composants dans votre bibliothèque de prix, ou en important un fichier excel.

### **Navigation dans l'écran devis:**

Le fonctionnement général et la navigation sont similaires aux autres écrans de Vertuoza:

1. Une zone de recherche.
2. Des filtres qui peuvent être appliqués.
3. Le tableau reprenant les informations.
4. Les boutons d'actions à l'extrême droite du tableau (placez votre curseur sur chaque bouton pour en connaître la signification).
5. Le bouton "Nouveau" pour créer un nouvel élément.

### **Créer un devis**

Pour créer un nouveau devis, rendez-vous dans le **menu de gauche > Offre > Devis**

A partir du bouton **Nouveau** à droite, vous pouvez choisir de créer un nouveau devis dans Vertuoza ou d’importer depuis un fichier Excel (Si l’option est activée dans les **Paramètres > Propriétés > Devis et avenant > Import Excel**). L’import Excel concerne uniquement les lignes des postes du devis, les informations générales et mentions légales doivent être saisies dans Vertuoza.

Voir *Comment importer un devis à partir d’un fichier Excel (link)*

### **Structure d’un devis**

Les devis dans Vertuoza sont structurés en trois/quatre parties :

- **Informations du devis** : client, coordonnées, conditions et méthodes de paiements… Les champs disponibles dépendent de ce qui a été configuré dans **Paramètres > Général > Préférences d’affichage**

Voir *Informations générales du devis (link)*

- **4 onglets** : Informations, Encodage, Totaux, Visualisation
- **Encodage du devis** : les lignes du devis. Elles peuvent être de 5 types (pour les PRO et PRO+), ou de 9 types à partir du pack Expert : Titre, sous-titre, texte, poste libre, ouvrages (issus de la bibliothèque), fourniture (issus de la bibliothèque), équipement (issus de la bibliothèque), main d’oeuvre (issus de la bibliothèque), sous-traitant (issus de la bibliothèque). Pour plus d’informations, voir plus bas *Comment encoder les lignes d’un devis ? (link ancre)*
- **Tableau de résumé des marges** (à partir du pack Expert) : Calcul de la marge prévisionnelle que vous ferez sur ce chantier en fonction des composants utilisés depuis votre bibliothèque de prix. *Par exemple, vous vendez pour 500€ de main d’oeuvre dont le prix d’achat vous revient à 250€ : vous devriez faire 100% de marge.* Attention, vous devez indiquer un prix d’achat dans tous vos composants pour que le résultat soit cohérent.
- **Informations supplémentaires :** Gestion des déchets (si coché dans **Paramètres > Général > Préférences d’affichage)**, remarque, fichiers complémentaires…

### **Encoder les lignes d’un devis**

Pour vous guider dans la création de vos offres, celles-ci sont structurées en plusieurs colonnes, dont certaines doivent être activées dans **Paramètres > Général > Préférences d’affichage**

- La **case à cocher** en début de ligne permet de sélectionner plusieurs lignes pour les supprimer en lot, les copier (dans ce devis ou un autre), ou les mettre en option (le tarif défini n’apparaitra alors pas dans le total)
- **Type** sert à sélectionner le type de ligne souhaitées :
- Titre : Sur fond de couleur, reprend le total des lignes en dessous, permet de structurer le devis
- Sous-titre : Idem que titre mais dans le cas où des sous-parties sont également nécessaires
- Texte : Permet d’ajouter une ligne de texte libre sans que ce soit lié à un prix
- Poste libre : Permet de créer un poste dans le devis, de gérer les quantités, l’unité, le prix…
- Ouvrages (à partir d’Expert) : Aller récupérer un ouvrage depuis votre *bibliothèque de prix (link)*
- Fourniture, équipement, main d’oeuvre, sous-traitants (à partir d’Expert) : Aller récupérer un composant depuis votre *bibliothèque de prix*
- **Article** (si activée) sert à numéroter les lignes du devis
- **Catégorie** permet de filtrer les ouvrages ou composants dans la bibliothèque pour les ajouter au devis
- **Description** du poste
- **Quantité** vendue
- **Unité** du poste
- **Prix unitaire (PU)**
- **Prix total**
- **TVA à la ligne** (si activée)

### **Options des lignes du devis**

En bout de ligne, le plus permet d’ajouter une nouvelle ligne au devis et la corbeille de la supprimer.

Les “**Trois petits points”** permettent d’accéder à des actions sur chaque ligne de devis :

- Editer le détail du poste libre : aller ajuster le prix en jouant sur le prix d’achat et marge ou en le calculant à partir de composant de la bibliothèque (à partir d’Expert)
- Enregistrer dans la bibliothèque : enregistrer le poste en tant qu’ouvrage simple dans la bibliothèque pour pouvoir le réutiliser sur des prochains devis
- Remarque : ajouter un commentaire sur le poste. Il pourra être visible ou non sur le document final en fonction du *template de devis* (link) choisi
- Remise : Ajouter une remise sur le poste. La remise sera visible sur le document final.
- Quantité avancée : Permet de calculer plus précisément la quantité du poste en fonction des mesures. Par exemple : 10mc de gouttière pour la façade avant + 5mc pour la façade est + 3mc de sécurité = 18mc de gouttière vendue. Ces quantité avancée pourront être visible ou non sur le document final en fonction du *template de devis* (link) choisi
- Mettre ou retirer une option sur le poste
- Lier une photo au poste
- Lier à un ouvrage : dans le cas d’un import Excel, lier un poste libre à un ouvrage de la bibliothèque pour récupérer vos tarifs déjà connus
- Copier ou coller la ligne

### **Envoyer et gérer un devis**

Une fois le devis enregistré, plusieurs options sont disponibles. Retournez sur la vue liste du menu **Offres.** Vos devis peuvent avoir différents statuts :

- Draft : le devis n’a pas encore été Soumis
- A envoyer : le devis a été enregistré, mais pas encore été envoyé au client depuis Vertuoza
- Envoyé : le devis a été envoyé mais pas encore accepté par le client

Durant ces trois statuts, le devis est encore complètement éditable.

- Chantier en cours : le devis a été accepté par le client et transformé en chantier
- Refusé : le devis a été refusé par le client, il disparait de la liste qui est filtré par défaut sur les devis en cours et accepté, mais existe toujours dans Vertuoza

Comme dans chaque vue liste, vous pourrez ensuite gérer le devis via les boutons d’action en bout de ligne : Envoyer, Refuser, Accepter, Exporter, Dupliquer…

Voir aussi :

*Structure de l’application*

*Envoyer un mail depuis Vertuoza*

Mis a jour le : 02/09/2026
