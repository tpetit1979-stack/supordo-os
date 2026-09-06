---
source: https://intercom-help.eu/vertuoza/fr/articles/262171-comment-utiliser-des-prefixes-dynamiques-dans-vos-modeles
categorie: Paramètres
titre: Comment utiliser des préfixes dynamiques dans vos modèles ?
date_recuperation: 2026-09-05
---

# Comment utiliser des préfixes dynamiques dans vos modèles ?

Les préfixes vous permettent d’ajouter un complément de texte à une variable, tout en s'adaptant dynamiquement aux données. Si aucune donnée n’est disponible pour la variable, le préfixe n’apparaît pas, assurant une présentation propre et logique.

### **Comment ajouter un préfixe ?**

### **1. Sélectionnez une variable :**

- Accédez à l'éditeur du modèle et cliquez sur une variable existante, comme [clientContact.noms].

### **2. Activez l'option de préfixe :**

![](https://downloads.intercomcdn.eu/i/o/yr18hzl2/34463717/1b42930e023a385626bdfab3cbd4/image.png?expires=1788620400&signature=bcfe2cedc3ee0230ac73e40d78cfcd9dd1047cc552838e765cb413df1f27317b&req=09Frw1v9rTBk2hL085ZhoZA1bFDLCdIUJj%2BnMQnnG%2B2%2BCcdeUFMdkGFn8gnx%0AkDR7n2OHNiG5Vxap%0A)

- Un menu contextuel s’affiche avec une option pour ajouter un préfixe.

### **3. Saisissez le texte du préfixe :**

![](https://downloads.intercomcdn.eu/i/o/yr18hzl2/34464066/7c93384fbdb51f07f72f72a59b3e/image.png?expires=1788620400&signature=39a9314ebdf2a50490ef6c71a4e85bc6236673d10d27e6f2d065aa4372c50faa&req=09Frw1z6qjFk2hL085ZhoQUwtnYSe27uKpJf7gUVl2FHGpmUS9BimwGeA3yc%0A2xJ0dMfcX14su3Mv%0A)

- Par exemple : "À l'attention de".
- Cliquez sur **Appliquer** pour valider votre choix.

### **4. Vérifiez le rendu :**

- Si la donnée associée à la variable est vide, le préfixe ne s’affichera pas.
- Si la donnée est présente, le texte complet s’affichera, par exemple : "À l'attention de Jean Dupont".

### **Exemples d’utilisation :**

1. **Adresse client :**
- Variable : [clientContact.noms]
- Préfixe : "À l'attention de"
- Résultat (si les données sont disponibles) : "À l'attention de Marie Durand"
2. **Numéro de TVA :**
- Variable : [client.tva]
- Préfixe : "TVA N°"
- Résultat : "TVA N° FR123456789"
3. **Coordonnées bancaires :**
- Variable : [societe.iban]
- Préfixe : "IBAN :"
- Résultat : "IBAN : FR76 1234 5678 9012 3456"

Mis a jour le : 22/01/2025
