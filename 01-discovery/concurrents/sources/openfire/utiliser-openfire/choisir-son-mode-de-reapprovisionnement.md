---
source: https://support.openfire.fr/hc/fr/articles/24779042095900-Choisir-son-mode-de-r%C3%A9approvisionnement
categorie: Utiliser OpenFire
titre: Choisir son mode de réapprovisionnement
date_recuperation: 2026-09-05
---

# Choisir son mode de réapprovisionnement

Dans OpenFire, la **gestion des achats** est intimement liée à votre **activité commerciale** et technique. L'objectif est simple : disposer du bon produit au bon moment. Pour cela, le logiciel propose **6 stratégies différentes **pour générer vos Demandes de prix (commandes fournisseurs). Cet article vous donne une vision d'ensemble de ces méthodes avant de vous permettre de plonger dans le détail de chacune d'entre elles.

## Sommaire

Cet article contient les sections suivantes :

- [Qu'est-ce qu'une demande de prix ?](#h_01KES9T8BX8V20N0M6XMS6R7F3)
- [Panorama des 5 méthodes de réapprovisionnement](#h_01KESDHH8T07N3FG9N1J6B448Q)

  - [La commande de stock (manuelle)](#h_01KESEFTZ2RZ7RFYRP91EWMX5Q)
  - [L'achat à la contremarque (flux tendu)](#h_01KESEGHK2NZ1RNWV1K7B0T7FF)
  - [Le réapprovisionnement automatisé (Règles de stock)](#h_01KES94WYG0X8GKD8JJTYKM3V0)
  - [L'approvisionnement depuis une Demande d'Intervention (Sous-traitance)](#h_01KES94WYHNS431EEHNRPXCQDH)
  - [L'approvisionnement à la commande (automatique)](#h_01KES94WYCB2D84G9YG2G596FQ)
- [Pour aller plus loin](#h_01KET89B8RZR3MAS9CBPZEXPRY)

---

## Qu'est-ce qu'une demande de prix ?

La **Demande de prix **est le **point de départ** de tout parcours d'approvisionnement. C'est l'équivalent du devis côté fournisseur. Elle peut être créée manuellement ou automatiquement par le logiciel. Elle doit être vérifiée avant toute confirmation. Une fois confirmée, elle devient un **Bon de Commande Fournisseur, **génère une réception de marchandise (**BR**) et enregistre les **valeurs de stocks futurs** des quantités achetées.

Toutes vos demandes de prix peuvent être consultées ici : Achat > Commandes > Demandes de prix

## Panorama des 5 méthodes de réapprovisionnement

Dans OpenFire, vous disposez de 5 méthodes de réapprovisionnement. Ces méthodes déterminent, selon le scénario métier rencontré, la façon dont la demande de prix peut être générée.

Une entreprise peut être amenée à utiliser plusieurs méthodes différentes d'approvisionnement.

### 1. Commande de stock (manuelle)

Ce mode est utilisé lorsque vous décidez d'acheter du matériel indépendamment de vos ventes en cours. C'est le flux idéal pour anticiper vos besoins ou saisir une opportunité chez un fournisseur.

C'est la méthode la plus directe. Vous créez vous-même la demande de prix auprès de votre fournisseur sans que le logiciel ne l'anticipe.

![Schéma AK - Approvisionnement sur stock.jpg](https://support.openfire.fr/hc/article_attachments/24785229810716)

#### Le processus étape par étape

Comme l'illustre le schéma ci-dessus, le flux se décompose en trois phases clés :

**Etape 1. La Demande de prix :**

1. Suivre le chemin d'accès suivant : Achats > Commandes > Demandes de prix.
2. Vous créez manuellement le document. À cette étape, le stock n'est pas encore impacté.
3. 👆 **Action** : Cliquer sur **Créer**, sélectionner le fournisseur et ajouter vos articles.

**Etape 2. La Confirmation fournisseur :**

1. Une fois votre commande acceptée par le fournisseur, vous devez la valider dans OpenFire.
2. 👆 **Action** : Cliquer sur le bouton **Confirmer la commande**. Le document devient alors un **Bon de Commande**.

**Etape 3. La Réception (BR) et l'Entrée en stock :**

1. La confirmation génère automatiquement un **Bon de Réception (BR)** dans votre tableau de bord **Inventaire**.
2. 🚚 **Logistique** : À l'arrivée du camion, vous vérifiez la marchandise.
3. 👆 **Action** : En **validant** le BR, les articles sont instantanément ajoutés à votre inventaire.

| **🧑‍🏫Exemple** : Vous constatez que votre stock de conduits de fumisterie est bas. Vous créez manuellement une demande de prix pour 20 longueurs afin de refaire votre réserve au dépôt. |
| --- |

| 💡**Note **: Ce mode est le plus flexible car il ne nécessite aucun paramétrage préalable sur vos fiches articles (pas besoin de règles de stock mini/maxi). |
| --- |

### 2. Achat à la contremarque (flux tendu)

L'achat à la contremarque est la méthode idéale **pour les produits que vous ne souhaitez pas stocker**, comme les appareils coûteux (poêles, pompes à chaleur). Ici, l'achat n'est déclenché que si une vente est confirmée, et **le matériel est directement réservé** pour votre client.

La demande de prix est générée depuis un Bon de Livraison (BL) suite à une commande client.

![Schéma AK - Commande fournisseur - approvisionnement à la contremarque (1).jpg](https://support.openfire.fr/hc/article_attachments/24787355519772)

#### Le processus étape par étape

Le schéma ci-dessus illustre ce flux "sur mesure" où chaque étape sécurise la réservation de votre matériel :

**Etape 1 : Le déclencheur => La commande client : **

1. Tout commence par une **Commande client confirmée**.
2. ⚡ **Automatisme** : La validation de la commande génère automatiquement un **Bon de Livraison (BL).**

**Etape 2 : Le lancement de l'achat (Appro. à la commande)** :

1. Depuis le Bon de Livraison, vous décidez de lancer l'approvisionnement.
2. 👆 **Action** : Vous cliquez sur le bouton Approvisionnement à la contremarque pour générer la **Demande de prix** associée.

**Etape 3 : la confirmation de la commande fournisseur**

1. 👆 **Action** : Une fois la **Confirmation fournisseur** effectuée, un lien indéfectible est créé.
2. ⚡ **Automatisme** : Le logiciel effectue une **Réservation automatique** : l'article qui sera reçu est déjà "fléché" pour le Bon de Livraison de votre client.

**Etape 4 : la réception et l'entrée en stock** :

1. À l'arrivée du matériel, vous traitez le **Bon de réception (BR)**.
2. 👆 **Action** : Cliquer sur **Valider la réception**. L'article entre en stock et est immédiatement marqué comme "Réservé" pour le BL initial, prêt à être livré.

| **🧑‍🏫Exemple** : Vous vendez un poêle à granulés spécifique qu'un client a choisi sur catalogue. En utilisant la contremarque, dès que le poêle arrive à votre dépôt, OpenFire sait qu'il est destiné à ce client précis et personne d'autre ne peut le prendre pour un autre chantier. |
| --- |

| 💡**Note **: Ce mode permet de **limiter au maximum** votre niveau de stock et d'**optimiser votre trésorerie**, car vous n'achetez que ce que vous avez déjà vendu. Pour que ce flux fonctionne, veillez à bien **vérifier les délais de livraison de votre fournisseur** afin de planifier l'intervention technique en cohérence avec la réception du matériel. |
| --- |

### 3. Réapprovisionnements automatisés (Règles de stock)

Cette méthode est la plus efficace pour gérer vos articles de consommation courante (conduits, granulés, petite quincaillerie) sans risque de rupture. Grâce aux **règles de stock**, c’est le logiciel qui surveille vos niveaux de stocks pour vous et prépare vos commandes au moment idéal.

Si votre stock tombe en dessous du seuil minimum, OpenFire génère automatiquement une demande de prix pour remonter au stock maximum défini.

![Schéma AK - Réapprovisionnement auto avec règles de stocks.jpg](https://support.openfire.fr/hc/article_attachments/24788001463324)

#### Le processus étape par étape

Le schéma ci-dessus illustre comment OpenFire automatise la surveillance de votre dépôt pour garantir la continuité de vos chantiers:

**Etape 1 : Le contrôle quotidien** :

1. 🤖 **Contrôle automatique** : Chaque jour, le logiciel analyse votre **stock prévisionnel** (Stock réel + Commandes fournisseurs en cours - Commandes clients à livrer).
2. Cette surveillance est totalement invisible et automatique.

**Etape 2 : L'alerte de seuil** :

1. 🚨 **Seuil atteint** : Dès que le stock prévisionnel passe en dessous d'une limite (le **Seuil Mini**), le système déclenche l'ordre de réapprovisionnement.

**Etape 3 : La génération de la demande de prix** :

1. ⚡ **Action automatique** : OpenFire calcule la quantité exacte nécessaire pour remonter jusqu'à votre **Seuil Maxi **et génère automatiquement la Demande de prix associée en brouillon dans votre menu **Achats**.

**Etape 4 : Confirmation et Réception** :

1. 👆 **Action manuelle** : Pour valider l'achat, vous devez cliquer sur **Confirmer la commande**.
2. 🚚 **Logistique** : Une fois le matériel arrivé, vous passez au **Bon de réception**.
3. 👆 **Action manuelle** : Cliquer sur **Valider la réception** pour enregistrer l'**Entrée en stock** finale.

| **🧑‍🏫Exemple** : Vous avez fixé un seuil mini de 100 sacs de granulés et un maxi de 500. Dès qu'un technicien prend des sacs pour un chantier et que votre stock descend à 90, le robot génère automatiquement une commande de 410 sacs pour retrouver votre stock complet. |
| --- |

| 💡**Note **: Ce mode permet de libérer l'esprit de vos gestionnaires de stock, car ils n'ont plus à vérifier physiquement chaque étagère pour savoir quoi commander. Pour que ce flux fonctionne, chaque article concerné doit avoir un **Fournisseur** et des règles de stocks** mini/maxi** configurés dans sa fiche. Sans ces informations, le "Robot" ne pourra pas calculer vos besoins. |
| --- |

### 4. Approvisionnement depuis une Demande d'Intervention (Sous-traitance)

Ce mode est spécifiquement conçu pour les situations de sous-traitance d'une intervention planifiée (une maintenance annuelle, ou la pose d'une installation par exemple). La demande de prix est générée directement depuis la Demande d'Intervention (DI), et ne concerne la plupart du temps que des prestations de services.

![Schéma AK - Ordre de sous-traitance depuis une DI (2).jpg](https://support.openfire.fr/hc/article_attachments/24789154860700)

#### Le processus étape par étape

Le schéma ci-dessus détaille le processus de sous-traitance d'une intervention.

**Etape 1 : Le déclencheur => La Demande d'Intervention (DI)** :

1. Tout commence par la création d'une Demande d'intervention (DI), qu'il s'agisse d'un dépannage, d'une pose ou d'une maintenance annuelle programmée.

**Etape 2 : L'achat de la prestation** :

1. 👆 **Action** : depuis la DI, vous déclenchez un **approvisionnement** en sélectionnant le mode "**sous-traitance**". Vous sélectionnez alors le prestataire extérieur comme s'il s'agissait d'un fournisseur, ainsi que les prestations sous-traitées. Cliquez sur **Générer la demande de prix.**

**Etape 3 : La commande fournisseur** :

1. OpenFire crée une demande de prix pour le service concerné. Le sous-traitant est utilisé comme fournisseur.
2. 👆 **Action** : Une fois le tarif et la disponibilité confirmés par le sous-traitant, vous cliquez sur **Confirmer la commande**.

**Etape 4 : Réalisation et Validation** :

1. Le sous-traitant réalise l'intervention.
2. Aucune gestion de stock n'est nécessaire puisque seules les prestations de services sont concernées.

| **🧑‍🏫Exemple** : Vous vendez un contrat de maintenance annuelle pour une installation de chauffage au granulés. Le site d'intervention est trop éloignée et vous décidez de sous-traiter la réalisation de cette intervention. Depuis la demande d'intervention relative à cette prestation, vous générez une demande de prix vers une société partenaire pour la réalisation de l'entretien. Tout l'historique de l'intervention reste lié au dossier de votre client. |
| --- |

| 💡**Note : **Ce mode est réservé aux **Services**. Pour tout besoin de matériel (SAV, pièces), nous conseillons de repasser par une commande client afin de garder un flux logistique standard. |
| --- |

### 5. Approvisionnement à la commande (automatique)

C'est le mode le plus rapide de génération d'un ordre d'achat à la validation d'une commande client. Dès que vous confirmez votre Commande Client (CC), OpenFire génère immédiatement la demande de prix fournisseur.

Ce mode de fonctionnement est adapté pour les produits que vous ne fabriquez pas, que vous ne stockez pas et que vous voulez commander sitôt la vente signée.

![Schéma AK - Commande fournisseur - approvisionnement à la commande.jpg](https://support.openfire.fr/hc/article_attachments/24785229811868)

#### Le processus étape par étape

Comme l'illustre le schéma ci-dessus, ce flux mise sur une automatisation maximale pour gagner en réactivité :

**Etape 1 : Le déclencheur => la confirmation de la vente**

1. Le processus démarre dès que vous validez votre **Commande client confirmée**.
2. ⚡ **Génération automatique** : À l'instant précis de la confirmation, OpenFire crée immédiatement la **Demande de prix** correspondante auprès de votre fournisseur.

**Etape 2 : La confirmation de la commande fournisseur **:

1. Bien que la demande soit créée toute seule, vous gardez la main sur sa transmission au fournisseur et sur sa confirmation.
2. 👆 **Action** : Cliquer sur le bouton **Confirmer la commande** pour transformer la demande de prix en commande ferme.

**Etape 3 : La réception logistique (BR)** :

1. La confirmation de commande génère votre **Bon de réception**.
2. 🚚 **Logistique** : À la livraison, vous contrôlez la conformité des articles reçus.
3. 👆 **Action** : Cliquer sur **Valider la réception** pour enregistrer l'**Entrée en stock** finale.

| **🧑‍🏫Exemple** : vous avez une activité de négoce B2B et vous ne stockez aucun produit. Les appareils que vous vendez sont configurés en approvisionnement à la commande. Vous recevez une commande pour 5 appareils de la part de l'un de vos revendeurs installateurs. Vous saisissez sa commande et la confirmez ; un ordre d'achat pour 5 appareils est alors automatiquement pour que vous puissiez acheter ces 5 appareils auprès du fabricant. |
| --- |

| 💡**Note :** Ce flux étant très réactif, assurez-vous que la commande client est juste et définitive avant de la confirmer, car la demande d'achat fournisseur apparaîtra immédiatement dans votre liste de tâches. |
| --- |

### Synthèse pour bien choisir

| **Méthode d'appro** | **Déclencheur** | **Automatisation** | **Idéal pour...** |
| --- | --- | --- | --- |
| Stock manuel | Manuel | Aucune | Stocks ou Besoins ponctuels |
| Contremarque | Bon de livraison | Semi-auto | Commandes clients dédiées |
| Règles de stock | Seuil de stock | Automatique | Articles de rotation courante |
| Depuis la DI | Demande d'Intervention | Aucune | Sous-traitance |
| À la commande | Validation Commande Client | Totale | Flux tendu ultra-rapide |

## Pour aller plus loin

| 📓**Pour aller plus loin** → Créer une demande de prix ou une commande fournisseur (à venir) 📓**Pour aller plus loin** → Comment réaliser un approvisionnement à la contremarque ? |
| --- |

Mis a jour le : 13/01/2026
