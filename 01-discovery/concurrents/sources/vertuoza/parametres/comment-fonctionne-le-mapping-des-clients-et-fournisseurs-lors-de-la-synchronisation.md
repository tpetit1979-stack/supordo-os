---
source: https://intercom-help.eu/vertuoza/fr/articles/526829-comment-fonctionne-le-mapping-des-clients-et-fournisseurs-lors-de-la-synchronisation
categorie: Paramètres
titre: Comment fonctionne le mapping des clients et fournisseurs lors de la synchronisation ?
date_recuperation: 2026-09-05
---

# Comment fonctionne le mapping des clients et fournisseurs lors de la synchronisation ?

Le système utilise une logique en cascade : d'abord l'ID stocké, puis une recherche par nom si nécessaire, et enfin la création de l'entité si elle n'existe pas.

### Processus de mapping

**Q : Que se passe-t-il si mon contact/entreprise possède déjà un ID de synchronisation ?**

R : Le système vérifie si cet ID existe toujours dans le logiciel comptable. Si oui, il l'utilise directement pour créer la facture.

**Q : Et si l'ID n'existe pas ou n'est plus valide ?**

R : Le système recherche alors le client/fournisseur par nom (nom d'entreprise ou nom + prénom pour un contact). Si trouvé, son ID est utilisé et sauvegardé pour les prochaines fois. Sinon, un nouvel enregistrement est créé et son ID est enregistré.

**Q : Quelle différence pour une entrée manuelle ?**

R : Les entrées manuelles n'ont pas d'ID initial, donc le système passe directement à la recherche par nom. L'ID obtenu est stocké dans une table intermédiaire (non accessible aux utilisateurs) pour les futures synchronisations.

### Stockage des ID

**Q : Où sont enregistrés les ID de synchronisation ?**

R :

- Pour les contacts/entreprises de Vertuoza : dans leur fiche directement
- Pour les entrées manuelles : dans une table intermédiaire non accessible aux utilisateurs

### Bonnes pratiques

**Q : Comment optimiser la synchronisation et éviter les doublons ?**

R : Il est fortement recommandé d'indiquer les ID directement sur les fiches contacts/entreprises dans Vertuoza. Cela permet :

- Une synchronisation beaucoup plus rapide
- D'éviter la création de doublons

**Q : Pourquoi un doublon a-t-il été créé ?**

R : Cela arrive si le nom dans Vertuoza ne correspond pas exactement à celui du logiciel comptable (casse, espaces, caractères spéciaux différents) ou si l'ID stocké a été supprimé du logiciel comptable.

Mis a jour le : 14/01/2026
