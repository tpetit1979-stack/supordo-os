---
url: https://documentation.openfire.fr/knowsystem/parametrer-une-marque-5
url_finale: https://documentation.openfire.fr/knowsystem/parametrer-une-marque-5
date_collecte: 2026-09-06
destination: documentation_2
---

L'utilisation des marques sert à piloter les conditions d’achat et de vente spécifiques par marque, celles-ci s’appliquent indifféremment aux articles importés des bases centralisées, ou à ceux créés localement.

## Créer une marque

**Accès :**  **Ventes** > **Configuration** > **Marques**. 

Sur chaque marque, on peut définir des conditions d'achat et de vente qui s'appliquent ensuite aux articles rattachés à la marque.


                        

Pour chaque création de marque, les éléments suivants sont à définir obligatoirement :

- Nom de la marque
- Code : préfixe de la marque utilisé automatiquement dans chaque référence article (généralement les 3 premières lettres de la marque en majuscules)
- Fournisseur : société qui fournit les articles de la marque, une marque n'a qu'un fournisseur mais un fournisseur peut avoir plusieurs marques.

Lorsque la marque est créée, vous pouvez demander une connexion au tarif centralisé de la marque auprès du support. Dès lors qu'elle est connectée, vous pouvez accéder au catalogue centralisé via le smart bouton Articles centralisés.

Le smart bouton Articles indique le nombre d’articles de la marque et permet un accès immédiat à ces derniers.

  Plus d'information sur [la création des articles](https://documentation.openfire.fr/knowsystem/creer-un-article-6#scrollTop=0)

## Conditions d'achat et de vente

#### Règles de gestion

Les règles de gestion sont applicables à 3 niveaux : au global fournisseur, au niveau de la catégorie d’article ou au niveau de l'article.

Pour chaque article, les règles s'appliquent de bas en haut :

- Au niveau de l'article dans **Articles ayant des règles spécifiques** : Si l’article existe dans cette table, les règles associées sont appliquées.
- **Au niveau de la catégorie dans Correspondance des catégories d’articles** : Si la catégorie de l’article existe dans cette table, les règles associées sont appliquées.
- **Au global fournisseur dans Paramètres d’import par défaut** : Dans les autres cas, les règles d’import par défaut sont appliquées.

#### Paramètres d'import par défaut

Les informations saisies dans cette section seront utilisées :

- Lors de l’import de fichier tarif de la marque concernée
- Lors de la mise à jour d’un tarif
- Lors de la connexion au tarif centralisé.

Vous devez y définir :

- La catégorie  que vont prendre les articles par défaut : si celle-ci n'est pas définie dans l'import des articles, dans le tarif centralisé, ou dans les règles spécifiques (de la catégorie ou de l'article).
- L'éventuelle remise négociée avec le fournisseur, s'applique sur le *ppht* (prix public HT)  et définit le*pa* (prix d'achat)
- Le calcul du prix de vente HT : la base de calcul est le *ppht*  qui est la valeur qui s'applique par défaut
- Le calcul du prix de revient  : la base de calcul est le*pa*  qui est la valeur qui s'applique par défaut

Une aide pour définir les règles de calcul est disponible dans l'onglet Aide.

Il faut ensuite cliquer sur APPLIQUER LES REGLES pour que les différents prix des articles soit recalculés.

  Plus d'information sur [Définir des conditions tarifaires](https://documentation.openfire.fr/knowsystem/definir-ses-conditions-tarifaires-169)


## Règles spécifiques

#### Correspondance des catégories d'articles

Cette section permet de faire le lien entre la Catégorie d'origine, transmise par le fournisseur, et la Catégorie interne définie dans la base, tout en permettant d'appliquer des règles spécifiques pour chacune de ces catégories.

Les règles sont les mêmes que pour les Paramètres d'import par défaut, elles viennent les contredire uniquement pour les lignes et pour les champs qui sont renseignés. Si un champ est laissé vide les règles des Paramètres d'import par défaut s'appliquent.

#### Articles ayant des règles spécifiques

Cette section permet de configurer des règles spécifiques propres à une sélection d’articles. Il s’agit notamment de références pour lesquelles le distributeur aura négocié des conditions commerciales dérogatoires (prix net, etc.) ou appliquera un prix de vente spécifique.

Elle fonctionne de la même manière que la table de Correspondance des catégories d'articles, dont elle vient contredire les règles lorsque celles-ci sont renseignées.

  Plus d'information sur [Définir des conditions tarifaires](https://documentation.openfire.fr/knowsystem/definir-ses-conditions-tarifaires-169)