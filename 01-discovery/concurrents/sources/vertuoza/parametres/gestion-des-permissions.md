---
source: https://intercom-help.eu/vertuoza/fr/articles/212431-gestion-des-permissions
categorie: Paramètres
titre: Gestion des permissions
date_recuperation: 2026-09-05
---

# Gestion des permissions

### 1) **Qu’est-ce que la gestion des permissions ?**

La gestion des permissions permet de créer des rôles spécifiques pour les utilisateurs "gestion", leur donnant accès à certaines fonctionnalités du menu ou leur en cachant. Cela permet donc de cacher des données confidentielles et également de masquer tous les éléments dont vous n'avez pas besoin. 

Exemples :

- Le rôle "Deviseur" a accès aux sections "Contacts", "Devis", et "Bibliothèque". Si l’action "tous les devis" n’est pas activée, il ne verra que ses propres devis.
- Le rôle "Gestionnaire" a accès à "Contacts", "Bibliothèque", "Chantier", et "Facturation". Si l’action "tous les chantiers" n’est pas activée, il ne verra que les chantiers où il est gestionnaire.

[Vidéo]()

**Note** : Cette fonctionnalité est en constante amélioration. Si vous avez des retours, contactez-nous à [support@vertuoza.com]().

### 2) **Comment créer un rôle ?**

Pour créer un rôle personnalisé, suivez ces étapes :

1. Allez dans **Paramètres > Général > Utilisateurs > Rôles**.
2. Vous verrez la liste des rôles déjà créés (comme "Administrateur").
3. Cliquez sur le bouton "**Nouveau**" en haut à droite pour ajouter un rôle.
4. Dans le formulaire, donnez un nom au rôle (ex: "Gestionnaire").
5. Cochez ou décochez les éléments du menu auxquels ce rôle aura accès.
6. Cliquez sur "**Enregistrer**" pour valider.

![](https://downloads.intercomcdn.eu/i/o/19629961/015b8fdb07ae249804cf79b8/image.png?expires=1788620400&signature=2f37542c112771e976c10f2d33f8461789fb2672c12e9dea24b7b539dff8d5a2&req=0dxpx1HzqjZk2hL085ZhodRyXUz1tFLVeY%2FONymyqgu%2Fj0cMgHHm9wbEmHCP%0AvQ60gO7z%2BJJ5Q%2B00%0A)

**Exemple** : Si vous décochez "Contacts", les utilisateurs ayant ce rôle ne verront plus l’onglet dans le menu.

![](https://downloads.intercomcdn.eu/i/o/19630061/0d73fa6fa4190b8c4949101a/image.png?expires=1788620400&signature=690598fb2b9eab689f990018713a85619559620ba917f7aca1525ff291542916&req=0dxpxlj6qjZk2hL085ZhockgPZBSNKH%2ByP9H5GBn4KYbA2fRcXV4R5WRsRf6%0AlH8z5QJBRXaTlD7h%0A)

> 🚨 **Points d'attention** :
> - Si vous cachez un élément du menu, veillez à cacher également les accès àla section "Paramètres" > " dans les paramètres pour éviter que l'utilisateur puisse modifier ses propres permissions.
> - Si l’accès à une section liée au tableau de bord est restreint, il est recommandé de cacher également le tableau de bord pour éviter des accès partiels.
> - Si l’accès aux finances est restreint, l'utilisateur ne pourra plus voir/modifier les factures dans la gestion de chantier (la section "Facturation" sera limité à l'avancement). Il pourra toujours en créer depuis un état d’avancement ou le devis (sans pouvoir les voir).

### 3) **Comment assigner un rôle à un utilisateur ?**

Une fois le rôle créé, vous pouvez l’assigner à un utilisateur :

1. Allez dans **Paramètres > Général > Personnel > Employés**.
2. Cliquez sur l’icône crayon à côté de l’utilisateur à modifier.
3. Modifiez le rôle dans les paramètres de l’utilisateur.

Sur cette page, vous pouvez également restreindre l’accès aux devis et chantiers pour que l'utilisateur ne voie que ceux qui lui sont assignés.

![](https://downloads.intercomcdn.eu/i/o/19630338/dc5b0ae19ebb8f6b09c9d720/image.png?expires=1788620400&signature=48c64ba79890a434d120d68797931b7f2a5d77d30f58b5eef3cbe84fb6da8266&req=0dxpxlj5rz9k2hL085ZhocglIwj%2ByZ14S8oQ2Wu4XfmmVfIdL4VnzgTP8ftT%0AlRidPeFmvNWVWzw%2B%0A)

### 4) **Que se passe-t-il si un utilisateur tente d’accéder à une page restreinte ?**

Si un utilisateur essaie d’accéder à une page à laquelle il n’a pas accès, il sera redirigé soit vers le tableau de bord, soit vers une page d’erreur indiquant que ses permissions sont insuffisantes. Il faudra alors que l'administrateur de la société lui donne des accès supplémentaires.

![](https://downloads.intercomcdn.eu/i/o/19630525/adb5ac1fa4e177f8025c5ef2/image.png?expires=1788620400&signature=9b970f2535821183931dc21e474a3e8ab9d7d4525206159c349108a44074e159&req=0dxpxlj%2FrjJk2hL085Zhobp5cOEnLHip4ez8UHd16VSjCZIsbnOd%2BJXkUspn%0Ae%2FD8AR7FpYuwz5Ho%0A)

### 5) **Y a-t-il des limitations ?**

Oui, actuellement, vous ne pouvez cacher ou afficher que des éléments du menu principal. Les sous-sections (comme des sections spécifiques dans "Chantier") ne peuvent pas encore être gérées.

**Note** : Cette fonctionnalité est en constante amélioration. Si vous avez des retours, contactez-nous à [support@vertuoza.com]().

Mis a jour le : 13/09/2024
