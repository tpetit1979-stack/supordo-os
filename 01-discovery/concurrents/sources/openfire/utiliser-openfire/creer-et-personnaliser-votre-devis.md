---
source: https://support.openfire.fr/hc/fr/articles/19076240168988-Cr%C3%A9er-et-personnaliser-votre-devis
categorie: Utiliser OpenFire
titre: Créer et personnaliser votre devis
date_recuperation: 2026-09-05
---

# Créer et personnaliser votre devis

Cet article vous indique comment réaliser un devis dans OpenFire.

Créer un devis d'installation précis et professionnel est essentiel pour conclure des affaires et établir une relation de confiance avec vos clients. Cet article vous guide à travers les étapes clés pour élaborer un devis clair, détaillé et conforme aux attentes de vos prospects.

Cet article contient les sections suivantes :

- [Créer votre devis](#h_01JPSBWS33DT42Z8E6P5KS81X9)
- [Compléter les informations principales](#h_01JPSBWS33G1552SV6TF0BRKFT)
- [Ajouter et structurer vos "Lignes de commandes"](#h_01JPSBWS34S6FP0AE6PYQVNCJD)
- [Ajouter vos conditions générales](#h_01JPSBWS34NZ4TCEJSFYXJSJ9G)
- [Compléter les informations additionnelles de votre devis](#h_01JPSBWS34GEDBTWDMQ50XMRM2)

## **Créer votre devis**

Chemin d’accès :

- **Pour le plan basique :** `OpenFire > Ventes > Mes devis`
- **Pour les autres plans :** `Ventes > Commandes > Devis`

Pour commencer un devis, vous pouvez cliquer sur **"Nouveau**", en haut à gauche.

## **Compléter les informations principales**

### **Bloc Client**

Le bloc CLIENT vous permet d’identifier les coordonnées de votre devis ainsi que les références de la commande.

**Client :** Permet de rechercher un client.

**Adresse de facturation : ** Permet de définir un contact différent de celui à qui est adressé le devis. Ce contact sera repris pour éditer la facture, en lieu et place du client du devis. C’est utile notamment lorsque votre client dispose d’un service comptabilité propre à qui la facture doit être transmise.  ** **

**Adresse de livraison :** Permet de définir un lieu de livraison de la prestation différent de l’adresse du client à qui est adressé le client. Cette adresse sera reprise comme adresse de livraison dans les bons de livraisons et les interventions associées.
💡Note : Vous avez la possibilité d'utiliser, pour l'adresse de livraison ou de facturation, soit une adresse secondaire du client, soit une adresse totalement différente.🚨Avertissement : Par défaut, les adresses de livraison et de facturation enregistrées sur un contact seront automatiquement renseignées dans les champs correspondants.
**📓**Pour aller plus loin → [Gérer les adresses secondaires](https://support.openfire.fr/hc/fr/articles/19075703945500)

**Référence commande :** vous permet d’affecter une référence spécifique pour la commande en cours. Cette référence peut-être utilisée dans différents cas de figure :

- Distinguer des versions de devis pour un même client (exemple “Version 1 avec poêle canalisable”).
- Proposer une référence commerciale qui sera utilisée avec le client comme référence de suivi, en plus éventuellement du numéro de commande.

### **Bloc Dates**

Le bloc **DATES** centralise les principales dates du devis :

**Devis :** désigne la date de création du devis, par défaut ce champ sera complété par la date du jour, mais il reste modifiable jusqu’à la validation de ce dernier.

**Expiration :** Correspond à la date de validité de votre de devis. Par défaut, le devis expire un mois après sa date de création, mais ce champ reste modifiable.
💡Note : Vous pouvez personnaliser cette date d’échéance par défaut dans les paramètres de configuration.
**Visite technique **: cette date correspond à la date de réalisation de votre visite technique. Dans le cadre d’un projet d’installation, il est obligatoire de faire figurer cette date sur vos devis.

**Livraison : **désigne la date de livraison de la prestation promise au client. Si cette date est définie, le Bon de Livraison se basera sur cette date plutôt que celle calculée en fonction des délais indiqués sur chaque produit du devis. Ce délai est d’ailleurs calculé et présenté dans le champ **Prévu **accolé à la date de livraison.

**📓**Pour aller plus loin → [Imprimer un devis](https://support.openfire.fr/hc/fr/articles/19076269547164)

### **Bloc Devis**

**Modèle de devis :** Permet de sélectionner un modèle sur la base duquel votre devis sera généré. Cela permet notamment de prédéfinir le régime fiscal, les produits à insérer et les règles d’impression à votre devis. Ces éléments seront ensuite personnalisables.

**📓**Pour aller plus loin → [Modèle de devis](https://support.openfire.fr/hc/fr/articles/19091379170588)

**Type :** Permet de différencier vos ventes selon des critères de votre choix comme par exemple le secteur d’activité (Installation PV / Installation Poêle / Installation Chaudière) ou le type de prestation (Installation / SAV / Contrat d’entretien). Le type est utilisé notamment pour l’analyse de votre activité, avec une répartition possible par type de vos différents indicateurs : CA par type / Marge par type / etc.

**Devis envoyé :** Cette case est automatiquement cochée si vous procédez à l'envoi du devis par email depuis OpenFire. Elle peut aussi être complétée manuellement si vous avez envoyé votre devis sans passer par le logiciel.

### **Bloc Facturation**

**Liste de prix :** La liste de prix représente la version du tarif appliquée à un client, soit en raison d'une négociation spécifique avec ce dernier, soit en fonction de son appartenance à un groupe (par exemple, une liste de prix professionnelle pour les artisans). Par défaut, c’est la liste de prix public de l’entreprise qui est appliquée dans le devis, sauf si une liste spécifique a été renseignée directement dans la fiche du client.
🚨Avertissement : Seules les lignes d'articles ajoutées après le renseignement de ce champ prendront en compte la liste de prix.
**📓**Pour aller plus loin → [Liste de prix](https://support.openfire.fr/hc/fr/articles/19091357200796)

**Position fiscale :** détermine le régime fiscal appliqué au devis et à ses lignes.

- Si un client possède une position fiscale définie sans fiche, celle-ci sera appliquée par défaut.
- Si un modèle de devis est saisi après avoir sélectionné le client, la position fiscale du modèle prévaudra.

Dans les autres cas, ce champ devra être renseigné manuellement dans le devis.
🚨Avertissement : Certains articles peuvent avoir une configuration fiscale spécifique, qui prendra le pas sur la position fiscale du devis.
**📓**Pour aller plus loin → [Comment les taxes sont calculées sur les lignes de devis et les factures](https://support.openfire.fr/hc/fr/articles/19084567800348)

**Conditions de paiement :** Définit les échéances prévisionnelles de paiement du devis par le client. Des conditions de paiement par défaut sont suggérées. Une fois sélectionnées, elles peuvent être consultées et modifiées. Ces échéances restent ajustables via l'échéancier prévisionnel situé en bas du devis.

Exemple : ![](https://support.openfire.fr/hc/article_attachments/19107352622876)

Votre échéancier :

![](https://support.openfire.fr/hc/article_attachments/19107352626716)

**📓**Pour aller plus loin → [Les conditions de paiement](https://support.openfire.fr/hc/fr/articles/19097987879068)

Une fois toutes les informations déclarées en partie haute, il est temps de venir saisir les produits et prestations qui composent votre devis, et d’en structurer la présentation.

Dans le corps de votre devis, vous pouvez ainsi insérer trois types d’éléments différents :

- Des produits ;
- Des sections ;
- Des notes.

![](https://support.openfire.fr/hc/article_attachments/19107390021916)

Ces trois éléments sont détaillés ci-dessous

## **Ajouter et structurer vos “Lignes de commande”**

### **Ajouter vos prestations**

**Ajouter un produit : **Ce bouton vous permet de sélectionner les produits ou kit à ajouter à votre devis, en saisissant directement dans le menu déroulant la référence ou la désignation du produit recherché. Il lance la recherche de référence produit. En sélectionnant **"recherche avancée" **une fenêtre de recherche s'ouvre et vous permet d'appliquer des filtres de recherches pour trouver votre produit.

![](https://support.openfire.fr/hc/article_attachments/19107390024220)
💡Note : La saisie se fait désormais en mode liste, pour favoriser une saisie plus rapide.
Une fois votre ligne ajoutée, la modification des autres informations (quantité, prix, description, taxe) reste modifiable sur la ligne directement.

Vous pouvez également accéder aux informations détaillées de la ligne en cliquant sur le petit ![](https://support.openfire.fr/hc/article_attachments/19107390031644) :

![](https://support.openfire.fr/hc/article_attachments/19107352636572)

- **Produit **: désigne le produit sélectionné ;
- **Quantité **: désigne la quantité de produit vendu, à l’unité de mesure sélectionnée ;
- **Prix unitaire** : désigne le prix de vente unitaire du produit. Ce prix peut-être un prix de vente HT ou un prix de vente TTC, selon la taxe associée au produit. 
  - Si la taxe associée au produit est une taxe TTC, alors le prix unitaire affiché est un prix TTC également. Sinon le prix unitaire est considéré comme hors taxe.

**📓**Pour aller plus loin → [Comment les taxes sont calculées sur les lignes de devis et les factures](https://support.openfire.fr/hc/fr/articles/19084567800348)

- **Coût : **correspond au prix de revient de l’article sur la base de laquelle la marge sera calculée.
- **Prix d’achat **: correspond au prix d’achat du produit auprès de son fournisseur.

**📓**Pour aller plus loin → [Prix d’achat, Coût d'inventaire, Coût théorique et méthode de coût](https://support.openfire.fr/hc/fr/articles/19095774098844)

- **Taxes **: correspond à la taxe appliquée sur le produit.

**📓**Pour aller plus loin → [Comment les taxes sont calculées sur les lignes de devis et les factures](https://support.openfire.fr/hc/fr/articles/19084567800348)

- **Remise (%)** : vous permet de saisir une remise en % pour chacune de vos lignes. Il existe d’autres méthodes de remise.

**📓**Pour aller plus loin → [Suivez vos marges et proposez des remises commerciales](https://support.openfire.fr/hc/fr/articles/19076258578332)

- **Délai **: correspond au nombre de jours entre la confirmation de la commande et la livraison des prestations pour le client. Ce délai est calculé selon le délai de livraison déclaré au niveau du produit

![](https://support.openfire.fr/hc/article_attachments/19107390035996)

- **Article principal : **désigne, dans le cadre d’un devis d’installation, le produit correspondant à l’appareil ou à l’équipement principal installé. Par exemple, et selon votre activité, il pourra s’agir de la référence liée au poêle, à la chaudière ou aux panneaux photovoltaïques. Ce paramètre est géré au niveau de la catégorie de produit.

![](https://support.openfire.fr/hc/article_attachments/19107390038044)

Ainsi, tous les produits de la catégorie POÊLE BOIS seront considérés comme articles principaux dans le contexte du devis.

**📓**Pour aller plus loin → [Marques et fournisseurs](https://support.openfire.fr/hc/fr/articles/19097519042332)

- **Politique de facturation** : correspond aux règles de facturation applicables à la ligne de commande.
- **Date de facturation prévisionnelle** : désigne la date à laquelle la prestation sera facturée, calculée selon la politique de facturation applicable.

**📓**Pour aller plus loin → [Politique de facturation](https://support.openfire.fr/hc/fr/articles/19091247558940)

- **Description **: correspond à la désignation du produit pour le client, dans le contexte du devis. Cette description est générée automatiquement selon un certain nombre de paramètres et de données (comme par exemple les données techniques existantes au niveau du produit). Cette description est modifiable dans le devis.

Exemple d’une description générée pour un produit de type poêle disposant de données technique.

![](https://support.openfire.fr/hc/article_attachments/19107352647324)
💡Note : Vous pouvez personnaliser les descriptions de vos lignes de commandes au niveau de la marque.
### **Structurer votre devis avec des sections et des notes additionnelles**

**Ajouter une section :** Les sections permettent de structurer votre devis en y ajoutant des chapitres, afin d’en faciliter la lecture. Vous pouvez créer autant de sections que nécessaire, et les positionner à l’endroit de votre choix par simple glisser-déposer (drag and drop).

Vous pouvez choisir d'imprimer le total HT et / ou TTC de chaque section de devis.
Pour cela, dans le devis / bon de commande, cliquez sur l'onglet **Impression** et choisissez de cocher ou décocher les options suivantes :

- **Tableau récapitulatif** : affiche un tableau récapitulatif des sections sous les lignes de commande sur l'impression du rapport PDF.
🧑‍🏫Exemple : ![](https://support.openfire.fr/hc/article_attachments/20286685033628)

- **Afficher le sous-total** : affiche le montant par section sur l'impression du rapport PDF.
🧑‍🏫Exemple : ![](https://support.openfire.fr/hc/article_attachments/20286685036444)

- **Type de montant** : définit le type de montant affiché dans les sous-totaux par section et dans le tableau récapitulatif sur l'impression du rapport PDF. Vous pouvez ainsi choisir d'afficher les sous-totaux en montant HT, en montant TTC ou les deux (comme dans les exemples ci-dessus).

Par défaut, les sections offrent un seul niveau de hiérarchisation. Si vous souhaitez structurer vos devis de manière plus avancée avec des sections et sous-sections, vous avez la possibilité d’activer les sections avancées.

**📓**Pour aller plus loin → [Structurer vos devis avec les sections avancées](https://support.openfire.fr/hc/fr/articles/19084531360028)

- **Ajouter une note :** permet de renseigner une note directement dans le corps de votre devis. Cette note est visible à l’écran et reprise à l’impression pour votre client.

  💡Notes : 

- L'ensemble des lignes d’un devis peut être déplacé à votre convenance,
        pas simple glisser-déposer, en utilisant le picto
        ![](https://support.openfire.fr/hc/article_attachments/19107390040220)
        présent au début de chaque ligne.
- Pour supprimer une ligne, vous pouvez cliquer sur
        ![](https://support.openfire.fr/hc/article_attachments/19107390041500)
        à la fin de chaque ligne.

Voici un exemple de rendu incluant des sections et une note au niveau de l’article Poêle :

![](https://support.openfire.fr/hc/article_attachments/19107352651676)

### **Consulter les totaux du devis**

En bas de vos lignes de commande, vous retrouvez le bloc relatif aux totaux de votre devis :

![](https://support.openfire.fr/hc/article_attachments/19107352662172)

- **Montant HT** : total des montants HT des lignes du devis ;
- **TVA **: détaille le montant de TVA par taux identifié dans le devis ;
- **Total** : total TTC du devis ou de la commande ;
- **Reste à facturer HT** : correspond au montant non encore facturé de votre commande, hors taxe, déduction faite des acomptes éventuellement déjà facturés ;
- **Reste à facturer HT (hors acompte)** : correspond au montant non encore facturé de votre commande, hors taxe, sans tenir compte des éventuelles factures d’acompte déjà émises pour votre client.

  🧑‍🏫Exemple : mon devis est de 3 000 € HT. J’ai uniquement facturé un acompte
  de 500 € HT. 

- Le reste à facturer HT de mon devis est de : 2 500 € HT
- Le reste à facturer HT (hors acompte) est de : 3 000 € HT

## **Ajouter vos Conditions Générales**

### **Vous retrouvez dans le bas de votre devis un champ dédié à vos Conditions Générales de Ventes  **

### **![](https://support.openfire.fr/hc/article_attachments/19107390052508)**

### **Les conditions générales peuvent être gérées de différentes manières. **

**📓**Pour aller plus loin → [Les CGV](https://support.openfire.fr/hc/fr/articles/19091350823324)

## **Compléter les informations additionnelles de votre devis**

### **Onglet "Suivi"**

#### Section SUIVI

**Document d'origine :** Reprend la référence du document depuis lequel le devis a été généré.

**Opportunité :** Reprend la référence de l’opportunité depuis lequel le devis a été généré. Cela permet de modifier le vendeur et le prospecteur du devis pour y mettre ceux de l’opportunité.

**Étapes de suivi : **Les étapes de suivi vous permettent de définir votre propre flux de travail à appliquer à vos devis et commandes en cours. Il existe de nombreux usages possibles autour de ces étapes de suivi, comme par exemple permettre à vos équipes ADV de suivre la préparation du chantier (planification / approvisionnement / …) ou le suivi des étapes administratives et ou règlementaires (retour consuel / retour organisme de financement / etc.).

**Étiquettes de suivi : **À l’image de vos étapes de suivi, les étiquettes de suivi sont un puissant outil visuel pour suivre l’avancement de vos commandes en cours.

![](https://support.openfire.fr/hc/article_attachments/19107352671900)

Les étapes de suivi et les étiquettes peuvent être utilisées dans la vue Kanban :

![](https://support.openfire.fr/hc/article_attachments/19107390058908)

**Info : V**ous permet de saisir n’importe quelle information utile au bon suivi du dossier.

**Notes de suivi **: À l’image du champ info, les notes de suivi vous permettent de partager les informations clés relatives au suivi de la production de la commande, à partager avec les différentes parties prenantes internes.

**Notes d’intervention :** À l’image du champ **Notes de suivi**, les notes d’intervention vous permettent de partager les informations clés relatives à la planification de l’intervention associée à la commande, à partager avec les différentes parties prenantes internes. Ces notes seront reprises au niveau de chaque intervention liée.

Pour en savoir plus sur le suivi de vos commandes en cours
💡Note : Ces informations ne seront pas présentes à l’impression de votre devis.
**📓**Pour aller plus loin → [Suivre vos commandes en cours](https://support.openfire.fr/hc/fr/articles/19084558912540)

#### Section MARKETING

Dans cette rubrique, nous retrouvons les champs relatifs à la qualification des modes d’acquisition du prospect.

![](https://support.openfire.fr/hc/article_attachments/19107390061212)

Apporté par : désigne le contact par qui le prospect est arrivé.
**📓**Pour aller plus loin → [Campagnes, canaux et origines](https://support.openfire.fr/hc/fr/articles/19098016415900)
Lorsque le devis est généré depuis une opportunité, ces informations sont héritées de cette dernière.

#### Section DATES DE PROJET

Dans cette rubrique, vous retrouvez certaines informations de date relatives à la planification de la commande.

**Date de pose de référence **: correspond à la date de pose, calculée par le logiciel, dès lors qu’une intervention de type “Installation” est rattachée à la commande. Si plusieurs interventions de type "Installation" sont planifiées en lien avec la commande, le logiciel retiendra la date de la première intervention non encore réalisée ou annulée, en suivant l’ordre chronologique.

  🧑‍🏫Exemple :

La commande CC2500038 est associée aux deux interventions suivantes :

![](https://support.openfire.fr/hc/article_attachments/19109184587548)

Les deux interventions étant confirmées, la date de pose de référence retenue
    pour la commande sera le 31/03/2025

![](https://support.openfire.fr/hc/article_attachments/19109184588572)

Une fois la première intervention réalisée, la date de pose de référence
    basculera automatiquement à la date suivante, à savoir le 28/04.

À travers ce champ vous pouvez donc consulter la prochaine intervention directement depuis la commande. L’un des usages possibles est notamment de pouvoir afficher vos commandes par dates de prochaines interventions directement dans la vue Kanban des commandes :

![](https://support.openfire.fr/hc/article_attachments/19107352680220)

**Date de pose forcée **: vous permet de forcer le cas échéant la date de pose de référence de la commande. Une fois la case cochée, un nouveau champ apparaît, intitulé **Date de pose manuelle**, vous permettant de forcer cette date.

**Semaine de pose** : Correspond à la traduction de la date de pose retenue en numéro de semaine.

### **Onglet "Autres informations"**

#### Section VENTES

**Vendeur :** Désigne le commercial chargé de la vente. Par défaut, il s'agit de l'utilisateur déclaré comment vendeur dans l’opportunité associée au devis, ou à défaut celui ayant créé le contact.

**Prospecteur : **Désigne le prospecteur (ou assistant commercial) chargé de la vente. Par défaut, il s'agit de l'utilisateur déclaré comme prospecteur dans l’opportunité associée au devis, ou à défaut déclaré comme tel dans la fiche du client directement.

**Equipe commerciale :** Attribue une équipe commerciale en tant que responsable de la vente. Ce champ est rempli par défaut si une équipe commerciale est renseignée sur la fiche contact du client.

**Société :** Ce champ s'applique aux environnements multi sociétés. Il permet de désigner la société à laquelle la vente est rattachée. Par défaut, ce sera la société sur laquelle se trouve l'utilisateur qui crée le devis.

**Confirmation en ligne :** Permet d’activer la fonction de validation en ligne par signature électronique de la commande.

Si la case “**Signature**” est cochée, lors de la génération de l’aperçu client ou via le mail transmis au client, le client pourra procéder à la signature directement via la fonction “**Accepter et Signer**”.

![](https://support.openfire.fr/hc/article_attachments/19107352682140)

![](https://support.openfire.fr/hc/article_attachments/19107352684188)

**📓**Pour aller plus loin → [Faites signer votre devis par signature électronique](https://support.openfire.fr/hc/fr/articles/19084528821788)

#### Section FACTURATION ET PAIEMENTS

Dans cette section, vous retrouvez des champs dédiés au pilotage des règles de facturation et à leur anticipation.

**Politique de facturation : **Correspond aux règles qui seront appliquées à la commande lors de la facturation. Deux politiques de facturation distinctes existent :

- **Quantités commandées : **À la facturation de la commande client, la quantité facturée pour le produit correspondra à la quantité vendue au client. Le logiciel vérifiera d’abord si une ou plusieurs quantité(s) du produit n’ont pas déjà été facturée(s), afin d’éviter les doublons de facturation. Dans ce scénario, la facturation avant la livraison des produits est donc possible.
- **Quantités livrées : **À la facturation de la commande client, la quantité facturée pour le produit correspondra à la quantité déjà livrée au client. Le logiciel vérifiera d’abord si une ou plusieurs quantité(s) du produit n’ont pas déjà été facturée(s), afin d’éviter les doublons de facturation.

**Statut de la facture :** ce champ apparaît à la transformation de votre devis en bon de commande. Ce champ est calculé automatiquement et désigne l’état de facturation de votre commande, en tenant compte de la politique de facturation et des factures éventuellement déjà émises.

Trois valeurs sont disponibles pour ce champ :

- **Rien à facturer** : aucune des lignes de la commande n’est facturable ;
- **À facturer** : au moins une quantité de l’une des lignes de la commande est facturable ;
- **Entièrement facturé** : l’ensemble des lignes de la commande a été facturé.

**Forcer le statut de facturation** : ce champ permet à l’utilisateur de définir manuellement un statut de facturation différent de celui calculé par le logiciel.
🧑‍🏫Exemple : Vous avez vendu 6 mètres de tubage mais n’en avez facturé que 5 mètres. Théoriquement, la ligne de commande reste à facturer pour 1 mètre de tubage. Pour clôturer le dossier, vous pouvez venir forcer l’état de facturation de la commande.
**Date de facturation prévisionnelle** : Désigne, lorsqu’elle peut être calculée, la date de prochaine facturation de la commande concernée.

- *Si facturation basée sur les quantités livrées* : cette date correspond à la date prévue du prochain bon de livraison à valider, en lien avec la commande.
- *Si facturation basée sur les quantités commandées* : cette date n’est pas valorisée. Dans les rapports, la date reprise sera la date du jour.

**📓**Pour aller plus loin → [Politique de facturation](https://support.openfire.fr/hc/fr/articles/19091247558940)

#### Section LIVRAISON

**Politique d’expédition** : permet de déterminer comment la date prévisionnelle de la livraison est calculée. Deux choix sont possibles :

- **Aussi vite que possible** : la livraison pouvant se faire en plusieurs fois, la prochaine date de livraison du BL sera calculée sur la base du produit ayant le délai de livraison le plus court.
- **Quand tous les produits sont prêts **: la livraison étant prévue pour se faire d’un bloc, la prochaine date de livraison du BL sera calculée sur la base du produit ayant le délai de livraison le plus grand.

**Statut de livraison** : correspond à un statut de livraison dépendant des livraisons associées. 4 statuts sont disponibles :

- Non livré
- À commencé
- Partiellement livré
- Entièrement livré

### **Onglet "Impression"**

**📓**Pour aller plus loin → [Imprimer et envoyer un devis](https://support.openfire.fr/hc/fr/articles/19076269547164)

### **Onglet "Commentaires"**

Les commentaires vous servent à enrichir votre devis d’informations additionnelles, à disposer au-dessus (commentaires du haut) ou au-dessous (commentaires du bas) de vos lignes de commande à l’impression du devis.

Vous pouvez les compléter manuellement, ou les générer depuis une liste de modèles prédéfinis.

![](https://support.openfire.fr/hc/article_attachments/19107390077084)

**📓**Pour aller plus loin → [Les modèles de commentaires](https://support.openfire.fr/hc/fr/articles/19109593908124)

**Visualiser, envoyer et confirmer le devis**

Pour visualiser votre devis, plusieurs solutions sont disponibles :

![](https://support.openfire.fr/hc/article_attachments/19107352690076)

1/ **Imprimer **votre devis : Une fois votre devis créé, vous pouvez le visualiser en cliquant sur **"Imprimer**" en haut à droite du devis. Cela vous donnera la version imprimable PDF du devis.

2/ Générer un **Aperçu client** : L’aperçu client est un rendu HTML de votre devis. Ce rendu peut être transmis à votre client pour consultation & validation ligne.

![](https://support.openfire.fr/hc/article_attachments/19107352694044)

**📓**Pour aller plus loin → [Imprimer et envoyer un devis](https://support.openfire.fr/hc/fr/articles/19076269547164)

**Envoyer **

**Pour envoyer le devis, **vous pouvez cliquer sur **"Envoyer par E-mail"**. Cela permet d’ouvrir une fenêtre de mail où vous pourrez rédiger votre message ou sélectionner un modèle de mail, votre devis y sera automatiquement joint en format PDF.

**📓**Pour aller plus loin → [Les modèles de mails](https://support.openfire.fr/hc/fr/articles/19096352238620)

**Confirmer la vente **

Une fois le devis signé par votre client, vous pouvez cliquer sur **"Confirmer la vente"** en haut à gauche. Votre devis passera alors au statut bon de commande.

Cette confirmation peut aussi se faire automatiquement selon les options sélectionnées dans le champ **“Confirmation en ligne”** dans l’onglet **“Autres informations”** du devis.

Mis a jour le : 30/12/2025
