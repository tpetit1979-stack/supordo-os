---
source: https://intercom-help.eu/vertuoza/fr/articles/279070-pourquoi-ai-je-un-message-d-erreur-lorsque-je-modifie-la-duplication-d-un-ouvrage
categorie: FAQ (Foires Aux Questions)
titre: Pourquoi ai-je un message d’erreur lorsque je modifie la duplication d’un ouvrage ?
date_recuperation: 2026-09-05
---

# Pourquoi ai-je un message d’erreur lorsque je modifie la duplication d’un ouvrage ?

Le problème survient lorsqu’une ligne est ajoutée à un composant dans l’ouvrage, mais que le fournisseur de ce composant dans la bibliothèque a été modifié sans que ce changement soit appliqué à la ligne du composant de l’ouvrage. Cela crée une incohérence entre le fournisseur enregistré dans l’ouvrage et celui présent dans la bibliothèque. 

Par exemple, si l’ouvrage A mentionne un fournisseur pour un composant, mais que le fournisseur de ce composant dans la bibliothèque a été modifié sans que ce changement soit reflété dans l’ouvrage A, la tentative de duplication de l’ouvrage A échoue en raison de cette divergence. 

De même, si l’ouvrage B contient également un composant qui utilise le même fournisseur, la modification de celui-ci dans la bibliothèque sans ajustement de la ligne du composant dans l’ouvrage B peut également entraîner un message d’erreur lors de la duplication.
​

**Solutions :** 

Pour éviter ce problème, deux solutions sont possibles :

- Supprimer la ligne du composant dans l’ouvrage initial et la recréer avec le bon fournisseur
​
- Modifier le fournisseur dans la bibliothèque afin qu’il corresponde à celui souhaité pour la ligne du composant de l’ouvrage.

[Envie d'en savoir plus sur la rubrique Bibliothèques de Prix ? Explorez notre collection complète d'articles dédiés en cliquant ici.](https://intercom-help.eu/vertuoza/fr/collections/211965-bibliotheque-de-prix)

Mis a jour le : 21/11/2025
