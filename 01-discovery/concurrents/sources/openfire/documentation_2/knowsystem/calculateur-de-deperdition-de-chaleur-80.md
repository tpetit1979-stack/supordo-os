---
url: https://documentation.openfire.fr/knowsystem/calculateur-de-deperdition-de-chaleur-80
url_finale: https://documentation.openfire.fr/knowsystem/calculateur-de-deperdition-de-chaleur-80
date_collecte: 2026-09-06
destination: documentation_2
---

Le calcul de déperdition de chaleur permet d'estimer la puissance en kW nécessaire pour maintenir une habitation à une température donnée.

Cette estimation permet de réaliser une première sélection parmi les générateurs de chauffage envisageables (poêle, chaudière, etc) pour votre chantier.

 *Attention : cette estimation n'a pas valeur contractuelle. Elle doit être considérée comme une aide à la décision et ne remplace pas une étude thermique réalisée par un bureau spécialisé.*


        
    

## Présentation du module

L'outil de calcul de déperdition de chaleur est accessible depuis le module **Calcul**. Si ce module n'est pas présent sur votre base, contactez le support OpenFire par mail à l'adresse support@openfire.fr ou par téléphone au 02.30.96.02.65.

**Calcul**et cliquez sur

**Créer**pour ouvrir le formulaire de saisie.

Ce formulaire vous permet de renseigner les informations relatives au calcul de déperdition de chaleur, dans différentes sections décrites ci-dessous :

#### __Contact__

- Le nom du contact : vous permet de personnaliser le rapport. Vous pouvez sélectionner un contact déjà présent dans votre base. L'adresse se pré-renseignera alors automatiquement en récupérant les informations de la fiche du contact ;

- L'adresse et le département : ils permettent de récupérer certaines informations nécessaires au calcul (cf partie Méthode de calcul ci-dessous) ;
- L'altitude de l'habitation : elle permet de déterminer la ligne de température (cf partie Méthode de calcul ci-dessous). Vous pouvez déterminer l'altitude d'un lieu donnée via plusieurs outils GPS ou via l'application Google Earth. Sur cette application, l'altitude réelle et celle de la caméra sont indiquées en bas à droite.

#### __Caractéristiques__

- La Surface à chauffer et la Hauteur de plafond permettent de déterminer le volume à chauffer ;
- Le menu déroulant Date de construction permet de calculer le coefficient G (cf partie Méthode de calcul ci-dessous) .

- La température de confort désirée permet de préciser la température que les appareils de chauffage doivent permettre de maintenir.

#### __Liens Commerciaux__

Cette partie vous permet de faire le lien entre le calcul et une opportunité, un devis ou encore un parc installé :

  Plus d'information sur [le parc installé](https://documentation.openfire.fr/knowsystem/gerer-mon-parc-installe-72)

Une fois l'ensemble des champs nécessaires renseignés, cliquez sur Calculer afin d'obtenir une estimation de la déperdition de chaleur.

OpenFire vous listera une liste d'appareils compatibles en fonction des articles présent sur votre base.


## Méthode de calcul

Les déperditions de chaleur correspondent aux besoins en chaleur pour maintenir la température désirée d'une habitation en toutes circonstances. Cette grandeur évolue en fonction de la différence de température entre l'extérieur et l'intérieur.


L'outil de calcul OpenFire permet d'estimer le niveau de déperdition maximal. Cela permet de dimensionner la puissance du système de chauffage dans les conditions où la température extérieure est la plus basse. Ce calcul nécessite donc de déterminer la température la plus froide de l'année dans la zone de l'habitation.

La déperdition de chaleur est calculée à partir de la formule :

**P = S * H * G * (T° souhaitée - T° de réf)**

La Surface **S** et la hauteur **H** permettent de calculer le volume à maintenir en température.

Le coefficient **G** est déterminé via la date de construction de la maison selon la table suivante : 

- 0.2 pour une maison passive (RT 2020)
- 0,5 pour une maison BBC (aux normes RT 2012) ;
- 0,8 pour une maison aux normes RT 2005 ;
- 0,95 pour une maison construite entre 2000 et 2005 ;
- 1,05 pour une maison construite entre 1990 et 2000 ;
- 1,15 pour une maison construite entre 1983 et 1990 ;
- 1,3 pour une maison construite entre 1974 et 1982 ;
- 1,5 pour une maison construite avant 1975 ;
- 1,8 pour une maison non isolée.

La **T° souhaitée** correspond au champ du formulaire température de confort désirée.

La **T° de réf** est calculée à partir du département et de l'altitude. Ce calcul se base sur le document de la [Norme 12831-1 Afnor](<https://www.boutique.afnor.org/fr-fr/norme/nf-en-12831/systemes-de-chauffage-dans-les-batiments-methode-de-calcul-des-deperditions/fa045762/22708?pk_source=google-adwords&pk_medium=cpc&pk_campaign=%5BDSA%5D%20Focus%20NF%20/%20ISO%20(Acquisition)&gclid=Cj0KCQjwuLShBhC_ARIsAFod4fJff47keCr03ppqnDhCSQ6bVUwrjZVgvJiw6rF9cJuj5IZxQuAPhogaAiMiEALw_wcB>) de 2004.

Pour ce calcul, on utilise l'adresse de l'habitation pour récupérer la température extérieure de base au niveau de la mer :

Pour la France métropolitaine, la température extérieure de base, notée θ e [°C], est donnée par le tableau ci-dessous (issu de la NF P 52-612/CN), ramenée au niveau de la mer (valeur θ e,D [°C]) suivant le département du site :

Ensuite, cette température extérieure de base θ e [°C] est lue dans le tableau ci-dessous en fonction de θ e,D [°C] et de l’altitude du site :

**A savoir :** en fonction de vos droits, un menu de **configuration** est également disponible.

 

Ce menu permet de consulter l'ensemble des éléments de calcul utilisé, comme la température extérieure de base par département ou encore le coefficient G en fonction des dates de construction.

## Édition et Envoi du rapport

Une fois l'estimation effectuée, un rapport peut être édité et envoyé par mail.


En cas d'envoi par mail, un fichier PDF comprenant le récapitulatif du calcul est ajouté par défaut en pièce jointe du mail.