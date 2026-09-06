---
source: https://support.openfire.fr/hc/fr/articles/19096331565468-Exercices-et-p%C3%A9riodes-comptables
categorie: Configurer OpenFire
titre: Exercices et périodes comptables
date_recuperation: 2026-09-05
---

# Exercices et périodes comptables

Cet article a pour objectif de vous guider dans la gestion des exercices et des périodes comptables au sein de votre logiciel OpenFire. Vous y découvrirez comment paramétrer ces éléments essentiels pour une comptabilité claire et structurée.

Cet article contient les sections suivantes:

- [Créer un exercice comptable](https://support.openfire.fr/hc/fr/articles/19096331565468/live_preview/01K19KXNDYS3VX0ZQDNP4VQ9HV#:~:text=des%20p%C3%A9riodes%20comptables-,Cr%C3%A9er%20un%20exercice%20comptable,-Dans%20OpenFire%2C%20la)
- [Gérer les périodes comptables](https://support.openfire.fr/hc/fr/articles/19096331565468/live_preview/01K19KXNDYS3VX0ZQDNP4VQ9HV#:~:text=de%20vos%20soci%C3%A9t%C3%A9s.-,G%C3%A9rer%20les%20p%C3%A9riodes%20comptables,-Les%20p%C3%A9riodes%20comptables)
  - [Types de périodes comptables](https://support.openfire.fr/hc/fr/articles/19096331565468/live_preview/01K19KXNDYS3VX0ZQDNP4VQ9HV#:~:text=propos%C3%A9%20par%20d%C3%A9faut.-,Types%20de%20p%C3%A9riodes%20comptables,-Les%20types%20de)
  - [Génération automatique des périodes comptables](https://support.openfire.fr/hc/fr/articles/19096331565468/live_preview/01K19KXNDYS3VX0ZQDNP4VQ9HV#:~:text=la%20section%20suivante.-,G%C3%A9n%C3%A9ration%20automatique%20des%20p%C3%A9riodes%20comptables,-Cette%20fonctionnalit%C3%A9%20vous)

# Créer un exercice comptable

Dans OpenFire, la notion d'exercice comptable est une notion propre, distincte des périodes comptables de référence. La clôture des périodes mensuelles ou annuelles s'effectue progressivement, en verrouillant les journaux ou les périodes concernées. Les à-nouveaux, quant à eux, sont générés en temps réel dans les différents rapports de gestion (comme le Compte de Résultat ou le FEC), sans apparaître directement dans votre comptabilité.

Pour créer un exercice comptable, suivez ces étapes :

1. Suivre le chemin d'accès suivant : **Facturation > Configuration > Comptabilité > Exercices**.
2. Cliquer sur le bouton **Nouveau**.
3. Définir les valeurs suivantes :
  - **Nom** : Saisissez le nom de votre exercice comptable (par exemple : "Ex. 2024")
  - **Date de début** : Sélectionnez la date de début de l’exercice comptable.
  - **Date de fin** : Sélectionnez la date de fin de l’exercice comptable.
  - **Société** : Sélectionnez la société concernée par les dates de cet exercice.

Vous avez la possibilité de créer autant d’exercices que nécessaire. Chaque écriture comptable sera ainsi automatiquement liée à l’exercice correspondant.

| 🚨**Avertissement** : en cas d'environnement multi société, vous devez créer un exercice comptable pour chacune de vos sociétés. |
| --- |

# Gérer les périodes comptables

Les périodes comptables dans OpenFire sont des périodes de référence essentielles pour le filtrage, les rapports et les statistiques. Elles facilitent grandement vos recherches. Vous pouvez les créer de manière individuelle ou opter pour une génération automatique. Le type de période "Mois fiscal" est proposé par défaut.

## Types de périodes comptables

Les types de périodes comptables sont utilisés pour générer les périodes liées à vos exercices fiscaux. Vous pouvez aussi créer une période de référence personnalisée en définissant sa périodicité ainsi que ses dates de début et de fin.

Pour ajouter ou modifier un type de période comptable :

1. Suivre le chemin d'accès suivant : **Facturation > Configuration > Plages de date > Types de plages de dates**.
2. Pour un nouveau type, cliquer sur le bouton **Nouveau ; **pour modifier un type existant, cliquer directement sur le type à modifier.
3. Dans l'onglet **Configuration**, saisissez les informations suivantes :
  - **Nom** : Indiquez le libellé du type de plages de dates.
  - **Autoriser le chevauchement** : Si cette case est cochée, deux périodes de types différents ne pourront pas se superposer. **Exemple** : Il ne sera pas possible de créer une période "1er semestre 2020" de type "Semestre" et une période "2020 - 06" si elles se chevauchent.
  - **Est un mois fiscal ?** : Ce champ indique si la période est mensuelle de l'exercice et n'est pas modifiable par l'utilisateur.
  - **Société** : Sélectionnez la société concernée par la période. Si la période concerne plusieurs sociétés de la base de données, laissez ce champ vide.
4. L'onglet **Génération** vous permet de paramétrer des valeurs par défaut qui seront reprises au travers des fonctions de création en masse de périodes comptables. Ces valeurs sont reprises et détaillées dans la section suivante.

## Génération automatique des périodes comptables

Cette fonctionnalité vous permet de générer plusieurs périodes en fonction de critères communs.

Pour générer automatiquement vos périodes comptables :

1. Naviguez via le chemin d'accès : **Facturation > Configuration > Plages de date > Générer les plages de dates**.
2. Saisissez les informations suivantes :
  - **Type** : Choisissez le type de période comptable souhaité (vous pouvez en créer de nouveaux dans la section précédente).
  - **Société** : Sélectionnez la société concernée par la génération des périodes comptables. Si la période est destinée à plusieurs sociétés de la base, ne spécifiez aucune société en particulier.
  - **Durée** : Définissez la durée de la périodicité à générer (en années, mois, semaines ou jours).
  - **Date de début** : Indiquez la date à partir de laquelle la génération des périodes comptables doit commencer.
  - **Jusqu’à** : Vous pouvez spécifier une date limite pour la génération des périodes comptables. Alternativement, indiquez le **nombre de périodes comptables à générer**, ce qui correspond au nombre de fois que vous souhaitez répéter la "durée" ou la "périodicité".
  - **Préfixe du nom des plages** : Choisissez le préfixe à utiliser pour nommer les périodes générées (par exemple, "2024 - " pour obtenir "2024 - 01").
  - **Expression du nom des plages** : Il est également possible d'utiliser une expression pour personnaliser la génération du nom des plages. Référez-vous aux explications fournies dans l’interface du logiciel pour son utilisation.
3. Cliquez sur le bouton **SOUMETTRE**.

| **🧑‍🏫Exemple** : Si vous configurez la génération pour 12 périodes mensuelles à partir du 1er janvier 2025 avec le préfixe "2025 - ", le logiciel créera les périodes de "2025 - 01" à "2025 - 12". |
| --- |

![Génération en lot de période comptable.png](https://support.openfire.fr/hc/article_attachments/21406590534812)

Vous obtenez alors le résultat suivant :

![Liste de périodes fiscales générées.png](https://support.openfire.fr/hc/article_attachments/21406575870620)

A ce stade, vous êtes parvenus à créer un exercice comptable et différentes périodes de référence pour affiner vos analyses et vos rapports financier.

| 📓**Pour aller plus loin** → Configurer vos plans comptables général et auxiliaire 📓**Pour aller plus loin** → Configurer vos taxes 📓**Pour aller plus loin** → Configurer vos positions fiscales 📓**Pour aller plus loin** → Configurer vos journaux |
| --- |

Mis a jour le : 07/08/2025
