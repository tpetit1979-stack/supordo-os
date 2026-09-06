---
source: https://intercom-help.eu/vertuoza/fr/articles/132286-import-d-un-devis-depuis-un-excel
categorie: Devis
titre: Import d’un devis depuis un Excel
date_recuperation: 2026-09-05
---

# Import d’un devis depuis un Excel

Lorsque vous travaillez avec des architectes ou en réponse à des appels des offres, vous avez parfois besoin d’importer directement un document extérieur (métré, bordereau de prix…) pour générer un devis dans Vertuoza. C’est tout à fait possible à deux conditions :

- que le format du fichier source soit en Excel
- que le fichier soit nettoyé avant import pour correspondre au format attendu par Vertuoza

### **Dans quel cas importer un devis depuis Excel ?**

Le moment de l’offre ou vous importerez le fichier dans Vertuoza peut varier en fonction des situations.

Dans le cas d’un appel d’offre où le template du bordereau de prix est imposé, il est souvent plus intéressant de gérer les remises de prix et les allers-retours directement sur le bordereau d’origine, et de procéder au nettoyage du fichier et à l’import une fois l’appel d’offre remporté.

Dans le cas où vous avez plus de liberté sur le format (si c’est vous qui fournissez le fichier d’origine à un architecte par exemple), vous pouvez préparer un devis type qui reprend le format Vertuoza afin de l’importer et de le modifier directement dans Vertuoza.

### **Comment importer un devis dans Vertuoza ?**

### **Préparer le fichier**

Le fichier source en Excel doit être nettoyé pour être correctement importé dans Vertuoza.

- Supprimez les informations autres que les lignes de prix (logo, nom, adresse…)
- Renommer les colonnes pour correspondre au format Vertuoza :
- **Référence** pour le numéro d’article (Ex : 1, 1.1, 1.2…)
- **Dénomination*** pour le nom du poste (Ex: **Doublage thermique intérieur en panneaux composites)**
- **Unité** (Ex: m2)
- **Quantité*** (Ex : 54)
- **TM** : Type de marché (Ex : QF = Quantité Forfaitaire, QP = Quantité Présumée)
- **Prix unitaire*** (Ex : 35€)
- **Prix total*** (Ex : 1890€)
- **Commentaire** - Apparaitront sous le poste en plus clair et légèrement décalé (Ex : Matériaux conformes aux normes UE)
**colonne obligatoire*
**Attention :**
Si le prix total n’est pas renseigné, la ligne se met en option
Si les quantités ne sont pas renseignées, la ligne se met en titre
**Astuce :**
Avant d’importer le fichier, ajoutez une colonne Format en première colonne. Cette colonne permet d’indiquer le type de ligne? C’est particulièrement utile dans le cas où votre devis est structuré avec des titres, des sous titres, des lignes de texte ect.
Pour préciser le type de ligne, ajoutez le code correspondant :
- **T** : **ligne de titre**
- **S** : **sous-titre**
- **P** :** Poste libre**
Il n’est pas nécessaire de laisser le total, il se calculera automatiquement. Voici un exemple de fichier :
​
![](https://downloads.intercomcdn.eu/i/o/18794632/9e7a278a9fc55cf5a19258aa/image.png?expires=1788620400&signature=4817299a36d2bbeb34de56e46254256fb9b3ff8919e1b7ba8e93f4ed8734c0ae&req=0d1ozFz8rzVk2hL085Zhocl6k%2BvRXtu4Czjo9JZ1%2FETLgQA7YY5qH9eONGqC%0A1g%3D%3D%0A)

Template import devis => Disponible dans le bas de l'article

### **Importer le devis Excel dans Vertuoza**

!! Assurez-vous d’avoir bien coché **Import de devis excel** dans **Paramètres > Propriétés > Devis et avenant > Import Excel** !!

- Aller dans le menu de gauche, **Offres > Devis**
- Cliquer sur **Nouveau**
- Choisir **A partir d’un Excel**
- Choisir votre **fichier Excel nettoyé**
- Indiquer **le numéro de la feuille du classeur** où est le devis (dans l’idéal, 1)
- Cliquer sur **Importer**

A ce stade, Vertuoza doit détecter automatiquement quelle colonne de votre fichier correspond à quelle info. Vous pouvez **vérifier et ajuster** en entrant la lettre de la colonne de votre fichier en face du Titre. Si vous n’avez pas utilisé un type de colonne non-requise (Ex : Type de marché), vous pouvez la laisser vide.

- Confirmer cette étape
- Vérifiez le récapitulatif. Vous pouvez supprimer les lignes inutiles s’il y en a en les décochant.
- Cliquer sur Confirmer & valider l’importation

Vous arrivez ensuite sur le devis éditable dans Vertuoza. Bravo ! Vous pouvez désormais *remplir les informations générales (link)*, ajuster les types de lignes, en ajouter, modifier les prix, *les marges (link)*…

Le devis se gère ensuite de la même manière que tous les documents.

**Aller plus loin :**

*>> Envoyer un mail depuis Vertuoza*

*>> Structure de l’application*

Mis a jour le : 02/09/2026
