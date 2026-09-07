---
url: https://docv5.progbat.com/presentation-generale/les-modeles-de-documents
url_finale: https://docv5.progbat.com/presentation-generale/les-modeles-de-documents
date_collecte: 2026-09-06
destination: centre_aide
---

# Les modèles de documents

- Ouvrez le menu "Paramétrage" (la roue crantée en haut à droite de l'écran)
- Choisissez la vignette "Modèles de documents"

## Courriers de relance, un modèle particulier

## Choisissez le type de modèle

Cliquez sur la flèche à côté de "Modèles de devis", et choisissez le type de modèle que vous souhaitez créer, ou modifier.

## Créer un modèle de document personnalisé

### Depuis un modèle existant

Il est recommandé de partir d'un modèle existant pour créer et personnaliser votre propre modèle.

- Nous vous proposons plusieurs modèles, que vous pouvez prévisualiser, et dupliquer pour les personnaliser. 
  - Les modèles "non éditable" définis par ProGBat ne sont pas modifiables directement, vous devez d'abord les dupliquer.

### Depuis une page blanche

Cliquez sur le bouton "Nouveau modèle de devis".

Cette méthode n'est pas recommandée, sauf de parfaitement maîtriser l'outil de personnalisation.

Il est préférable de [partir d'un modèle existant](https://docv5.progbat.com/presentation-generale/les-modeles-de-documents#depuis-un-modele-existant).

## Personnaliser un modèle de document

### Sections personnalisables

Un modèle se découpe en plusieurs sections.

- Entête et Pied de page se répèteront sur chaque page. 
  - Le pied de page va contenir notamment des informations qui doivent obligatoirement apparaître sur toutes les pages d'un devis ou d'une facture : 
    - le numéro de devis/facture
    - le numéro de la page, et le nombre de pages total du document
    - les informations juridiques de votre entreprise
- Certaines sections vont pouvoir être "propagées", c'est à dire dupliquées sur d'autre modèles, pour vous éviter de tout refaire à chaque fois que vous créez un nouveau modèle. 
  - Entête de page,
  - Entête générique,
  - Corps du document,
  - Pied de page.

## Personnaliser une section

La section "Corps du document" est un peu particulière, sa personnalisation est [détaillée plus loin](https://docv5.progbat.com/presentation-generale/les-modeles-de-documents#personnaliser-le-corps-du-document).
Pour toutes les autres sections, le concept est le même.

### Insérer du texte

Placez votre curseur à l'endroit où vous souhaitez insérer ou modifier du texte, et saisissez-le.

Grâce aux outils de l'éditeur, vous pourrez très simplement modifier la taille ou la couleur du texte, le mettre en gras ou en italique, l'aligner, créer des listes, exactement comme vous le feriez avec un traitement de texte comme Word.

### Insérer un tableau

Pour une mise en forme optimale, il est souvent très utile d'utiliser des tableaux.

Par exemple un tableau de 1 ligne et 2 colonnes permettent de parfaitement afficher le logo dans la première cellule, et les coordonnées de l'entreprise dans la 2ème, et le numéro et date du devis dans la troisième, aligné à droite. Dans l'exemple ci-dessous, vous voyez distinctement l'organisation en tableaux.

### Insérer une image

Généralement, le logo de l'entreprise est affiché sur vos devis et factures.

Mais vous souhaitez peut-être ajouter les logos de vos qualifications RGE, ou Qualibat.

Cliquez simplement sur l'icone "image" du menu de l'éditeur, et ajoutez une image déjà enregistrée, ou depuis votre ordinateur.

L'image est immédiatement dimensionnable à la souris pour s'intégrer parfaitement à votre modèle.

### Insérer des données

#### Les tags.

Le concept d'un modèle est de pouvoir afficher des informations différentes selon le devis ou la facture que l'on affiche : les informations du client, du chantier, du document en lui-même, etc...

Sur le logiciel, ces données sont identifiées par des "tags", qui sont toujours sous la forme @tag

Dans l'image au dessus, vous trouvez par exemple le tag @nomComTiers, qui affichera le nom du client.

Pour afficher le bon tag, vous trouverez à droite de la page, classé par thème, tous les tags disponibles.

Il vous suffit de mettre le curseur à l'endroit souhaité dans la section, et de cliquer sur le tag à droite de la page pour qu'il s'insère dans votre texte.

Vous pourrez appliquer au tag exactement les mêmes propriétés qu'un texte classique, c'est à dire le mettre en gras, en souligné, modifier sa taille, sa couleur...

#### Les méta-tags

Certains tags affichent beaucoup plus qu'une simple valeur, et reprennent toutes les informations nécessaires, pour vous garantir de ne rien oublier :

- **Numérotation automatique du document :** @numerotationDocument
  - Affiche le type et la date du document, y compris les numéros de révision ou de situation, ainsi que le devis d'origine pour une facture
- **Récapitulatif des lots** : @recaptulatifLots affiche un tableau récapitulatif de tous les titres de 1er niveau de votre devis ou facture :

### Utiliser des conditions

Il est intéressant de pouvoir afficher certaines données ou certains textes, uniquement si une condition est remplie.

Par exemple, comme sur l'image au dessus, on affichera "A l'attention de M. DUPONT" uniquement si un contact a été défini pour ce devis.

**Les conditions s'utilisent de la manière suivante :** 

**[si @tag]**`texte à afficher` **[sinon]*** `afficher autre chose`**[/si]**
**[sinon] est facultatif*

👉 Par exemple :

**[si @contactClient]**`À l'attention de @contactClient`**[/si]**

👉 signifie :

*"[Si un contact client est renseigné dans la fiche client], alors affiche le texte 'À l'attention de' et va chercher le nom du contact client dans la fiche client, [/Fin de la condition]"*

👉 Le résultat sera :

`A l'attention de Marcel DUPONT`

**Voici d'autres exemples :** 

**[si** 
***@estSituation***
**]**
`Situation n°` *@numSituation*
**[/si]**

*Traduction : Si le document est une situation de travaux, alors affiche le texte 'Situation n°' et va chercher le numéro de situation dans la facture.*

**[si @tauxRetenueGarantie > 0]**
 `Retenue de garantie :` *@tauxRetenueGarantie*
 `%` **[/si]**

*Traduction : Si le taux de la retenue de garantie est supérieur à 0, alors affiche le texte 'Retenue de garantie :' et va chercher le taux de la retenue de garantie, en ajoutant à la fin le texte '%'.*

**[si @tauxRetenueGarantie = 0]**
 `Aucune retenue de garantie n'est appliquée` **[/si]**

*Traduction : Si le taux de retenue de garantie est égal à 0, alors affiche le texte 'Aucune retenue de garantie n'est appliquée'.*

**[si @numRevision]**
 *@dateRevision*
 **[sinon]**
 *@dateCreation*
 **[/si]**

*Traduction : Si le devis contient un numéro de révision, alors affiche la date de révision du devis ; si le devis ne contient pas de numéro de révision, alors affiche la date de création du devis.*

###  Insérer un saut de page

Vous souhaitez par exemple avoir une page de garde, et que le corps de votre devis ou facture démarre toujours en page 2 ?

A la fin de la section "Entête", ajoutez un "saut de page" en cliquant sur l'icone dans le menu de l'éditeur

###  Insérer une ligne séparatrice

Cliquez sur l'icone dans le menu de l'éditeur

###  Insérer une division

Kézako ? Une division, c'est un bloc, comme une cellule de tableau, qui va accueillir du contenu, et que l'on va pouvoir mettre en forme facilement.

Cliquez sur l'icone dans le menu de l'éditeur et choisissez un style prédéfini.

Pour les "pros" du CSS, tentez l'onglet "Avancé" pour aller plus loin.

###  Accéder au code source.

Réservé aux connaisseurs du html et du css, entrez directement dans le code source de votre modèle.

## Personnaliser le corps du document

### Mise en forme de chaque type de ligne

- Sélectionnez un type de ligne, et appliquez le style que vous souhaitez (taille, couleur, alignement...)

### Afficher / masquer les prix

Il peut être utile de masquer les prix des lignes d'ouvrage par exemple, et de n'afficher que les totaux des titres, pour produire une estimation tout en évitant que vos prix unitaires fassent le tour de la concurrence. Si votre client semble d'accord sur votre estimation, vous pourrez lui fournir un devis détaillé et conforme à la réglementation pour la signature du marché.

**Important : un devis ou une facture doivent obligatoirement comporter le prix unitaire et la quantité de chaque ligne.**

- Sélectionnez le type de ligne souhaité, et cliquez sur le signe **€** dans la ligne de l'éditeur pour afficher/masquer les prix de cette ligne.

### Choisir les colonnes et le nom des colonnes affichés

Dans la partie droite de la page :

- Déplacez à la souris les colonnes pour les afficher ou non, et organisez-les dans l'ordre souhaité.
- Passez la souris sur le nom d'une colonne, et cliquez sur le petit crayon qui apparaît pour changer le nom de la colonne.

Les modifications sont immédiatement appliquées dans la section.

### Choisir les lignes à afficher

Par défaut, le logiciel affiche tous les types de ligne disponibles, mais vous pouvez choisir celles que vous souhaitez afficher.

#### Afficher les sous-totaux

Par défaut, le logiciel affiche les sous-totaux au niveau des titres, mais vous pouvez choisir de les afficher en fin de section.

Pour cela, activez "Lignes de sous-totaux" (voir image ci-dessus), et choisissez si vous souhaitez ajouter une ligne au dessus et/ou au dessous du sous-total.

### Les possibilités sont infinies

Nous ne pouvons pas détailler précisément tout ce que vous pouvez faire, n'hésitez pas à consulter votre support technique, ou à lui confier la réalisation de vos modèles de document.

[PrécédentLes minutes de calcul ou modèles de calcul](https://docv5.progbat.com/presentation-generale/les-minutes-de-calcul-ou-modeles-de-calcul)

[SuivantCourriers de relance, un modèle particulier](https://docv5.progbat.com/presentation-generale/les-modeles-de-documents/courriers-de-relance-un-modele-particulier)

Mis à jour