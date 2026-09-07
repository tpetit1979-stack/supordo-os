---
url: https://go.sellsy.com/blog/tout-ce-que-vous-avez-toujours-voulu-savoir-sur-le-format-csv
url_finale: https://go.sellsy.com/blog/tout-ce-que-vous-avez-toujours-voulu-savoir-sur-le-format-csv
date_collecte: 2026-09-07
destination: site_marketing
---

Facturation

12/5/2021

- mis à jour le

# Tout ce que vous avez toujours voulu savoir sur le format CSV

### Sommaire

S’il y a bien un sujet qui amène souvent à la crise de nerfs, c’est l’exploitation des fichiers CSV 😭

Les fichiers CSV sont des fichiers texte qui permettent de manipuler des données en colonnes, comme peut le faire un fichier de tableur type Excel.

C’est souvent le format de choix quand on souhaite **exporter** ou **importer** des données dans un logiciel, et c’est également souvent un casse-tête.

Voici un petit guide pour vous apprendre à utiliser le format CSV et à en déceler les pièges.


## C’est quoi un fichier CSV ?


Un fichier CSV est à l’origine un fichier dont les colonnes sont représentées par des virgules.


CSV signifie ***Comma Separated Values***, ce qui se traduit par ***Valeurs séparées par des virgules***.


Les sauts de ligne correspondent, elles, aux lignes du tableau.


Prenons par exemple un fichier texte contenant :

Nom,Type,Variété

Pomme,Fruit,Golden

Tomate,Légume,Roma

Salade,Légume,Iceberg


Si vous ouvrez ce fichier dans Excel (ou autre tableur), vous devriez obtenir un tableau de ce type :



Notez que la première ligne (titres de colonnes) peut exister ou non. La plupart des logiciels vous demanderont s’il y a lieu d’en tenir compte lors d’un import.


## Le grand problème de la virgule.


Le principal problème rencontré avec les fichiers CSV est cette notion de séparateur.


Comme nous l’avons vu précédemment, le séparateur par défaut est la virgule.


Ce choix est idéal aux Etats-Unis, car la virgule n’est pas utilisée dans les nombres, le séparateur de décimales étant un point.


Par exemple, ce type de ligne ne pose pas de problème aux USA :

Tomato,Vegetable,$12.80


Cependant, bien évidemment, en Europe et en France, nous utilisons la virgule comme séparateur de décimales, donc la même ligne ne fonctionnerait pas :


Tomate,Légume,12,80€



Dans ce cas, nous aurions une colonne avec 12 et une autre avec 80€.


Pour résoudre ce problème, il est d’usage en Europe d’utiliser un autre séparateur comme la **tabulation** ou le **point-virgule.**


Notre ligne compatible en Europe serait donc (avec des points-virgules) :


Tomate;Légume;12,80€


## Mon fichier est délimité par des virgules, comment l’exploiter ?

Si vous utilisez des outils américains, il est probable que si vous exportez des données, elles soient séparées par des virgules.

Le plus souvent, les tableurs européens ne sont pas prévus pour gérer des fichiers séparés par des virgules, ce qui peut vous amener à ce type de rendu si vous vous contentez de cliquer dessus :

Nous parlerons des problèmes de caractères plus loin, mais on voit tout de suite que les colonnes n’ont pas été prises en compte. 🤔


Pour contourner ce problème, il convient d’indiquer au tableur le type de séparateur que nous souhaitons utiliser.


Dans le cas d’Excel pour Mac, il va falloir créer un fichier Excel vide et ensuite cliquer sur “Importer” dans le menu Fichier.


Une fenêtre (qui est similaire sur tous les tableurs) va permettre d’indiquer que le séparateur est bien la virgule :

Tout de suite, on y voit plus clair et les valeurs sont bien importées dans des colonnes :


Note : il y a autant de spécificités qu’il y a de tableurs et de plateformes. PC, Mac, Excel, Open Office, Gooogle Sheets. A vous de vérifier le procédé dans votre tableur préféré.

À noter que le tableur d’Open Office est une bonne option gratuite pour manipuler des CSV.


## OK j’ai mes colonnes mais les caractères sont bizarres ?


C’est le deuxième problème ultra-classique rencontré avec les fichiers CSV : l’encodage.


Sans trop rentrer dans des détails techniques, pour qu’un fichier texte informatique puisse être lu, il doit être encodé avec un jeu de caractères.


Il en existe des dizaines, voire des centaines, souvent lié à l’usage de langues avec des alphabets complexes comme le coréen ou le chinois par exemple.


Dans les faits, la norme quasi exclusive sur le web pour les langues européennes est le format UTF8.


Quand vous téléchargez un fichier depuis un logiciel en ligne dans 90% des cas il sera formaté en UTF-8.


Mais là encore, nos logiciels gardent leurs vieilles habitudes et peuvent attendre un autre type d’encodage. Par exemple, Excel pour Mac va attendre un encodage de type Macintosh qui n’est plus utilisé depuis des années…


Là encore, les fonctions d’import vont pouvoir nous aider :



Notez que si vous recevez un fichier “exotique” vous pouvez tester plusieurs types d’encodage et voir lequel est correct dans l’aperçu.

Enfin, nos données sont bien formatées 💪🏻


## Et si mon séparateur existe dans les valeurs de mon fichier ?

Dernière subtilité du format CSV, il peut arriver que votre séparateur soit présent dans vos cellules.

Par exemple :

Tomate,Légume,Très goûteuse, la tomate est pleine de vitamines.


Vous l’aurez compris, la dernière virgule fait partie du texte, je ne veux pas deux colonnes.


Pour ce cas particulier, vous avez la possibilité d’entourer vos cellules d’un identificateur qui va permettre de ne pas tenir compte de la virgule dans ce contexte. Ce sont souvent les guillemets, simples ou doubles, qui sont utilisés.


Notre ligne deviendrait donc :

"Tomate","Légume","Très goûteuse, la tomate est pleine de vitamines."

Tenir compte de cette subtilité est important : si par exemple votre séparateur n’apparaît qu’en milieu de fichier, vous pourriez avoir l’impression que votre fichier est correct alors que toute la fin est décalée.

Bien entendu, il ne faut pas que l’identificateur lui-même soit présent dans les cellules, c’est pourquoi on utilise généralement les guillemets droits, peu utilisés dans la rédaction de textes en général.

## Quelques conseils pour bien gérer vos fichiers CSV


Pour remplacer un sélecteur sans passer par un tableur, vous pouvez utiliser un éditeur de texte et la fonction “Rechercher-Remplacer”. Si vous avez besoin de remplacer un sélecteur par le caractère “Tabulation” (qui est invisible), sélectionnez une tabulation et collez-la dans le champ désiré.


Vérifiez toujours les dernières lignes de votre fichier avant de l’exploiter, s’il y a une erreur en milieu de fichier, vous le verrez sur les dernières lignes.


Vous pouvez créer de toutes pièces un fichier CSV avec un éditeur de texte. L’extension de fichier importe peu, vous pouvez utiliser aussi bien CSV que TXT.


Google Sheet permet de très facilement importer des CSV et détecte tout seul les séparateurs et l’encodage dans l’immense majorité des cas.


Voilà, vous savez tout sur le CSV, à vous de jouer 😎