---
source: https://support.openfire.fr/hc/fr/articles/24473567048348-G%C3%A9rer-et-planifier-un-SAV
categorie: Utiliser OpenFire
titre: Gérer et planifier un SAV
date_recuperation: 2026-09-05
---

# Gérer et planifier un SAV

Cet article vous guide dans la gestion complète d'un Service Après-Vente (DI de type SAV). Vous y découvrirez comment coordonner les étapes commerciales, logistiques et techniques pour assurer un suivi efficace de vos dépannages.

## Sommaire

**Cet article contient les sections suivantes :**

- [**Comprendre le fonctionnement des SAV**](#h_01KEA4AH5WHW8XXT3XBR9NV9GX)

  - [1. La gestion commerciale et administrative](#h_01KEBSRRA69YX2W20Y02G7P44M)
  - [2. L'approvisionnement des pièces et le suivi des stocks](#h_01KEBSRY6N4W2YTSX68SNT5M7E)
  - [3. La planification et la réalisation de l'intervention](#h_01KEBSS1F6640V4GYB8Z6SYFXT)
- [**Réaliser le p****arcours type d'un dossier SAV**](#h_01KEA4MFVS1HFN5PJMP2F3TG23)

  - [1. Créer une DI de type SAV](#h_01KEA504GGMP3TGE3QTFY2GYYW)
  - [2. Émettre et confirmer votre devis SAV](#h_01KEA42BFXD2MPD0GXP2XK0J8X)
  - [3. Commander ou réserver les pièces détachées](#h_01KEANKY6NGPHRC7PMH94G0V2E)
  - [4. Planifier et réaliser l'intervention](#h_01KEAN08M812N52BHY2P5M5HQR)
  - [5. Facturer votre SAV](#h_01KEA42BG8A0AYQMHJWRMYY902)
- [**Piloter vos SAV au quotidien**](#h_01KEARVSHQ5584ERK42SKEGTRR)

  - [Suivre les étapes via la vue Kanban](#h_01KEAWM717G3X9ZEGDHRK7B55X)
  - [Utiliser les statuts automatiques (Planification, Réalisation, Facturation)](#h_01KEAWK0YRRWRBS0GSE8THYAC6)
  - [Optimiser le suivi via les tableaux de bord](#h_01KEAVBHB7GSVH9YCZPY81A4WT)

---

## Comprendre le fonctionnement des SAV

La gestion d'un SAV chez OpenFire repose sur trois flux majeurs :

### 1. La gestion commerciale et administrative du SAV

Dès la création de la demande, une étape de **Chiffrage client** est nécessaire pour établir un **Devis client** (incluant les pièces et la main-d'œuvre). L'intervention ne se poursuit qu'après la **Confirmation client** qui génère un **Bon de commande validé**. Le logiciel permet d'éditer une **Facture d'acompte client** dès la validation de la commande, avant de procéder à la **Facturation** finale une fois l'ensemble de la prestation terminée.

### 2. L'approvisionnement des pièces et le suivi des stocks

Une fois la commande confirmée, si l'intervention nécessite des pièces détachées, un **Bon de livraison (BL)** est généré. Il passe par une phase de réservation de stock (ou approvisionnement) jusqu'à la **Validation BL** qui confirme la sortie physique des pièces du stock.

### 3. La planification et la réalisation de l'intervention

En parallèle de la logistique, la **Planification** permet de fixer un **RDV d'intervention**. La **Réalisation de l'intervention** par le technicien clôture le cycle technique en passant le rendez-vous au statut **RDV réalisé**.

Voici un schéma de fonctionnement :

![](https://support.openfire.fr/hc/article_attachments/24670411284508)

## Réaliser le parcours type d'un dossier SAV

### 1. Créer une DI de type SAV

`Suivre le chemin d'accès suivant : Interventions > Interventions > SAV`

Créer une DI de type SAV depuis la liste des DI ou directement depuis la fiche client en utilisant l'action **DEMANDE D'INTERVENTION.**

**![](https://support.openfire.fr/hc/article_attachments/24658281609756)**

Pour créer votre SAV  :

Utiliser le **Titre de la demande d'intervention** pour saisir une description brève du SAV (ex : Ne démarre plus). Pour souligner le caractère d'urgence, vous pouvez soit utiliser les étoiles, soit utiliser une étiquette dédiée.

Renseigner la **Date de la demande** pour améliorer le suivi de votre SAV.

Choisir un **Modèle d’intervention** de type SAV préalablement constitué.

Valoriser le **client **et le **site d'intervention.**

![](https://support.openfire.fr/hc/article_attachments/24658344938268)

Sélectionner **l'équipement** concerné par le SAV. Si le client n'a qu'un équipement, celui ci est proposé par défaut lorsque vous cochez la case ***Equipement***. Sinon, à vous de sélectionner l'équipement concerné.

![](https://support.openfire.fr/hc/article_attachments/24661405329564)

Utiliser le champ **Description** pour noter tous les détails du dépannage et regrouper les informations nécessaires à son suivi.

Vous pouvez également **enregistrer une note interne** dans le chatter pour dater une information, ou planifier une action à réaliser en utilisant les **activités**.

![](https://support.openfire.fr/hc/article_attachments/24661405329948)

**Valider **enfin** **le SAV.

| 📓**Pour aller plus loin** → Créer et suivre vos demandes d'intervention (à venir) 📓**Pour aller plus loin** → Configurer vos modèles d'intervention (à venir) |
| --- |

### 2. Emettre et confirmer votre devis SAV

#### Le cas des SAV hors garantie

Cliquer sur l'action **Générer devis** depuis votre DI SAV.![](https://support.openfire.fr/hc/article_attachments/24662194097052)

Vérifier les informations préremplies (adresses, liste de prix, position fiscale).

![](https://support.openfire.fr/hc/article_attachments/24661712835356)

| 💡**Note **: Si votre devis concerne **plusieurs équipements**, vous pouvez ajouter un modèle de devis pour chaque équipement. Les lignes de ces modèles seront ajoutées à la commande, en lien avec chaque équipement. Vous pouvez ensuite **Générer le devis**. |
| --- |

Dans le devis généré vous pouvez ajouter les produits nécessaires : **Pièces détachées** (produits stockables) et/ou **Main-d'œuvre** (service).

![](https://support.openfire.fr/hc/article_attachments/24661684193308)

| 💡**Note **: Vous pouvez générer plusieurs devis pour une même DI, par exemple un premier devis de diagnostic puis un second pour la réparation. |
| --- |

Choisir la bonne politique de facturation :

Pour les devis de type SAV, nous vous recommandons d'utiliser la ***politique de facturation***** **"*A chaque prestation *(elle peut être **définie par défaut dans vos modèles de devis SAV). **Ainsi, la commande est liée à l'intervention et ne devient **facturable **qu'**une fois l'intervention réalisée**.

Une fois le devis confirmé, vous pouvez générer votre facture d'acompte afin de déclencher la commande des pièces détachées éventuelles.

| 💡**Note **: lorsque un premier diagnostic sur site est nécessaire, noter qu'il sera possible pour le technicien de générer **directement depuis son mobile **un **devis complémentaire** pour les pièces détachées requises (une bougie par exemple), de le faire valider par le client via signature électronique, et, s'il possède la pièce détachée dans son camion, de pouvoir intervenir directement. |
| --- |

#### Le cas particulier des SAV sous garantie

Pour les SAV sous garantie, nous conseillons de **générer une commande client à 0€** pour les pièces détachées (en utilisant par exemple une **liste de prix** "*SAV sous garantie*" configurée avec une remise de 100%). **Cette commande vaut prise en charge** pour le client, permet de déclencher normalement le **Bon de livraison** et de sortir les pièces du stock tout en validant la **prise en charge**, sans facturer le client final (les commandes à zéro ne sont jamais facturables).

### 3. Commander ou réserver les pièces détachées

La validation de la commande client permet de générer le BL depuis lequel est piloté la réservation ou l'approvisionnement des pièces détachées, de manière classique.

| [📓**Pour aller plus loin** → Comment réaliser un approvisionnement à la contremarque ?](https://support.openfire.fr/hc/fr/articles/24374815547420) 📓**Pour aller plus loin** → Consulter et réserver du stock depuis un produit, une commande ou un BL (à venir) |
| --- |

### 4. Planifier et réaliser l'intervention

La planification de l'intervention sur site intervient généralement une fois le devis SAV validé par le client et, le cas échéant, une fois les pièces détachées disponibles.

- **Planification** : La planification est réalisée de manière classique depuis la DI SAV, directement depuis le planning ou en utilisant la recherche de créneau depuis la DI. Pour les urgences SAV, l'optimisation par **Date** est recommandée pour intervenir au plus vite.
- **Réalisation (Mobile)** : Le technicien consulte l'intervention sur son mobile, saisit son compte-rendu, prend des photos du dépannage, fait signer le client, génère les factures manquantes (solde) et encaisse le règlement restant.

| 💡**Note **: Si une commande de pièces détachées à été effectuée, pensez à valider le BL pour enregistrer la sortie de stock. |
| --- |

| 📓**Pour aller plus loin** → [Rechercher un créneau disponible](https://support.openfire.fr/hc/fr/articles/19085638198684) |
| --- |

### 4. Facturer votre SAV

La facturation du SAV correspond à la facturation des commandes client associés au SAV.

Pour retrouver vos SAV à facturer :

1. Afficher la liste de vos SAV : Interventions > Interventions > SAV
2. Filtrer vos SAV comme suivant : *Statut de facturation* = ***A facturer*** (et éventuellement : *Suivi de la réalisation* = ***Entièrement réalisé***, pour vous assurer que tout à bien été fait pour ce dossier)![](https://support.openfire.fr/hc/article_attachments/24662718790940)

Pour facturer votre SAV, accéder au(x) devis associé(s), et les facturer de manière classique.

| 💡**Note **: Si ses **droits **l'y autorisent, le technicien génère le plus souvent la **facture finale directement depuis son mobile** à la fin de l'intervention. Cela lui permet d'encaisser immédiatement le règlement du client. |
| --- |

## Piloter vos SAV

### Suivre les étapes via la vue Kanban

L'étape Kanban vous permet de définir vos propres étapes de gestion pour suivre l'avancée de vos SAV.

L'étape Kanban est disponible dans **l'onglet Description > Rubrique Informations** de chaque SAV :

![](https://support.openfire.fr/hc/article_attachments/24663150849948)

Cette étape est généralement utilisée pour l'affichage de la vue Kanban de vos SAV :

![](https://support.openfire.fr/hc/article_attachments/24663150850204)

Exemple d'étapes de suivi pour vos SAV :

Nouveau > Diagnostic en cours > Devis à réaliser > SAV à planifier > SAV à facturer > Terminé

| 💡**Note **: Des **règles d’automatisation** peuvent être configurées via les actions automatisées pour permettre le passage de votre SAV d'une étape à l'autre. N'hésitez pas à vous rapprocher de votre chef de projet OpenFire ! |
| --- |

| 📓**Pour aller plus loin** → Configurer les étapes de vos demandes d'intervention (à venir) |
| --- |

### Utiliser les statuts automatiques (Planification, Réalisation, Facturation)

Trois statuts automatiques sont disponibles :

1. Le **statut de planification **: il vous permet de suivre si la prestation en lien avec le SAV a bien été planifiée. ![](https://support.openfire.fr/hc/article_attachments/24663150851484)
2. Le **suivi de la réalisation** : il vous permet de suivre si l'intervention associée au SAV a bien été réalisée. Il est disponible dans **l'onglet Description > Rubrique Informations** de chaque SAV :![](https://support.openfire.fr/hc/article_attachments/24663150851612)
3. Le **statut de facturation** : il vous permet de suivre si vos SAV sont à facturer ou non, selon l'état des commandes client associées. Il est disponible dans **l'onglet Ventes > Rubrique Ventes **de chaque SAV :![](https://support.openfire.fr/hc/article_attachments/24663150852764)

L'ensemble de ces statuts sont disponibles dans les filtres de recherches de vos SAV :

![](https://support.openfire.fr/hc/article_attachments/24663150853020)

### Optimiser le suivi via les tableaux de bord

Pour bien suivre vos SAV, nous vous **recommandons d'utiliser un tableau de bord** dédié, avec notamment l'utilisation des indicateurs dédiés suivants, pour ne rien oublier :

![](https://support.openfire.fr/hc/article_attachments/24663312312988)

| 💡**Note **: Des **tableaux de bords** peuvent vous être proposés par défaut. N'hésitez pas à vous rapprocher de votre chef de projet OpenFire si vous souhaitez y accéder ou pour les personnaliser ! |
| --- |

Mis a jour le : 07/01/2026
