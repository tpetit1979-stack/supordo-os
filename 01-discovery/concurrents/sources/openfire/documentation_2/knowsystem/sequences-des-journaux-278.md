---
url: https://documentation.openfire.fr/knowsystem/sequences-des-journaux-278
url_finale: https://documentation.openfire.fr/knowsystem/sequences-des-journaux-278
date_collecte: 2026-09-06
destination: documentation_2
---

Dans OpenFire, une séquence est utilisée pour numéroter les pièces à l'intérieur d'un journal. Les pièces générées, telles que les factures ou les bons de commande, sont toutes soumises à une séquence numérique.

Voici la méthodologie pour gérer les séquences dans OpenFire :

- Lors de la création d'un journal, une séquence est automatiquement générée. Par défaut, le code du journal est utilisé comme préfixe pour les numéros des pièces de ce journal.
- Vous avez la possibilité de modifier la séquence directement à partir du journal. Cela signifie que vous pouvez personnaliser la numérotation des pièces en ajustant les paramètres de la séquence associée au journal.
- La liste complète de toutes les séquences est accessible dans le mode développeur d'OpenFire. Pour y accéder, rendez-vous dans le menu "Configuration", puis sélectionnez "Techniques" et enfin "Séquences et identifiants".
- Il est recommandé de définir un nom de séquence identique au nom du journal correspondant. Cela permet d'associer clairement une séquence à un journal spécifique et facilite la gestion et la compréhension des numéros de pièces.

1. Créez un journal. Une séquence sera générée automatiquement et définira par défaut le code du journal comme préfixe des pièces de ce journal.

2. Modifiez la séquence directement depuis le journal si nécessaire.

3. Accédez à la liste de l'ensemble des séquences en mode développeur : Configuration > Techniques > Séquences et identifiants.

4. Définissez un nom de séquence identique au nom du journal.

5. Dans le tableau de préparation du plan de configuration, définissez pour chaque journal le nom, le type, le code journal, les séquences d'écritures, les comptes de débits et crédit par défaut.

Il est conseillé de reprendre le nom du journal associé pour le nom de la séquence. La séquence peut être modifiée directement depuis le journal.

En suivant cette méthodologie, vous pouvez gérer les séquences de numérotation des pièces dans OpenFire et personnaliser les numéros en fonction de vos besoins spécifiques.

## Tableau de préparation du plan de configuration

A définir pour chaque journal :

- Nom des journaux
- Type du journal
- Code journal
- Séquences d’écritures
- Comptes de débits et crédit par défaut

Détail des champs :

- Nom : Nom de la séquence. Il est conseillé de reprendre le nom du journal associé
- Mode d’implémentation : deux règles sont proposées :
- Standard : numérotation standard, sans vérification de la continuité de la chaîne et des bris de séquence éventuels ;
- Sans écart : numérotation continue n’autorisant pas les écarts de numérotations et les bris de séquence.
- Préfixe de la séquence : Chaine de caractère précédent la numérotation. Cette chaîne peut permettre d’incrémenter des éléments de date (année, mois et jour). Voir balise.
- Suffixe de la séquence : Chaine de caractères suivant la numérotation. Cette chaîne peut permettre d’incrémenter des éléments de date (année, mois et jour). Voir balise.
- Taille de la séquence Nombre de chiffre composant la numérotation
- Etape : le prochain numéro de séquence sera incrémenté par ce nombre
- Utiliser des sous-séquences par intervalle de date : permet d’ajuster la séquence en tenant compte de critères de temps. Si cocher, une nouvelle table apparait permettant de sélectionner les intervalles et le prochain numéro par intervalle

La date faisant référence pour le choix de la plage de date est la date de la facture et non la date du jour de la saisie.