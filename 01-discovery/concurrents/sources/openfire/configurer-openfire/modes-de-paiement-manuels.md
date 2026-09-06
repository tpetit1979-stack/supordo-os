---
source: https://support.openfire.fr/hc/fr/articles/19096228298012-Modes-de-paiement-manuels
categorie: Configurer OpenFire
titre: Modes de paiement manuels
date_recuperation: 2026-09-05
---

# Modes de paiement manuels

OpenFire propose plusieurs options pour **gérer les paiements clients et fournisseurs**. Cet article se concentre sur la **configuration des modes de paiement **utilisés pour l'enregistrement manuels des règlements clients et fournisseurs. Une bonne **compréhension des principes comptables** liés aux modes de paiement est essentielle pour une configuration efficace.

**Cet article contient les sections suivantes:**

- Présentation des modes de paiement
- Configuration des modes de paiement
  - Informations principales
  - Méthode de comptabilisation directe ou différée des paiements
- Configuration des comptes de paiement par défaut

# Présentation des modes de paiement

---

Les modes de paiement sont intrinsèquement liés à votre comptabilité : chaque enregistrement de paiement génère des écritures comptables. Avant de configurer un mode de paiement, il est essentiel de déterminer si l'encaissement (ou décaissement) sera comptabilisé dans la banque de façon **directe ou différée**.

Voici comment OpenFire gère les principaux modes de paiements :

- **Espèces** : L'encaissement est réalisé **directement **via le journal de caisse, sur le compte 530 du journal
- **Chèque** : L'encaissement est souvent **différé**. Le paiement est d'abord enregistré sur un compte d’attente (type 511). Ce n'est qu'après la remise en banque ou le rapprochement bancaire que le montant est transféré vers votre compte de banque 512.
- **Carte Bancaire (CB), Virement** : Ces paiements peuvent être traités de deux manières :
  - **Encaissement direct** : Le paiement est directement imputé à votre compte de banque 512 via le journal de banque.
  - **Encaissement différé** : Le paiement passe par un compte d'attente, similaire au processus des chèques, avant d'être transféré vers le compte de banque 512 lors du rapprochement ou de la remise.

| 💡**Note **: Des modes de paiement sont déjà préexistants dans OpenFire, basés sur nos configurations standards et sur les informations que vous avez fournies lors du lancement de votre compte. La liste de ces paiements est consultable de deux manières :   **Soit depuis le journal de banque associé** : suivre le chemin d'accès suivant : *Facturation > Configuration > Comptabilité > Journaux.*   **Soit depuis la liste des modes de paiements** :  Suivre le chemin d'accès suivant :  *Facturation > Configuration > Paiements > Mode de paiement.* |
| --- |

![](https://support.openfire.fr/hc/article_attachments/21451606743324)

# Configuration des modes de paiement

---

La création des modes de paiement se fait directement depuis les journaux de banques associés.

Pour accéder aux journaux comptables, suivre le chemin d'accès suivant :

Facturation > Configuration > Comptabilité > Journaux.

## Informations principales

Pour créer un nouveau mode de paiement :

1. Sélectionner le **journal de banque** associé au mode de paiement.
2. Repérer les deux onglets disponibles dans les journaux existants pour créer un mode de paiement :
  - L'onglet **Mode de paiement entrant** pour les règlements clients.
  - L'onglet **Mode de paiement sortant** pour les règlements fournisseurs.
3. Cliquer sur **Ajouter une ligne**.

![](https://support.openfire.fr/hc/article_attachments/21452021691932)

Vous devrez ensuite renseigner les champs suivants :

- **Méthode de paiement** (obligatoire) : La méthode de paiement doit toujours être **manuel**, sauf pour des cas de paiements spécifiques (prélèvement SEPA, intermédiaire de paiement (à venir)).
- **Nom du mode de paiement** (obligatoire) : Le nom que vous souhaitez donner au mode de paiement (par exemple, "Chèque Client", "Virement Fournisseur").
- **Compte de paiement en attente** : Il s'agit du compte comptable d’attente sur lequel l’écriture de paiement sera générée, en attente du rapprochement. La valeur à renseigner dans ce champ dépend de la *méthode d’enregistrement des paiements* (voir la section ci-après).

**![](https://support.openfire.fr/hc/article_attachments/21452006450204)**

- **Séquence** : Détermine l’ordre d’apparition du mode de paiement dans les listes de sélection.
- **Journal** (non modifiable) : Le journal auquel appartient le mode de paiement.
- **Type de paiement** (non modifiable) : Indique si le paiement est entrant ou sortant. Cette valeur est automatiquement définie selon l'onglet (entrant ou sortant) que vous avez choisi pour créer le mode de paiement.
- **Société** (non modifiable) : Ce champ affiche le nom de la société sur laquelle vous vous trouvez au moment de la création du mode de paiement.

La partie **Impression sur documents** vous permet de spécifier les informations relatives aux paiements que vous souhaitez voir apparaître sur vos factures.

Les exemples de variables fournis vous permettent de personnaliser les informations de paiements que vous souhaitez imprimez à l'impression d'une commande ou d'une facture.

| **🧑‍🏫Exemple** : L'utilisation de `**{payment_amount} payé par {payment_mode} le {date}**` donnera le rendu suivant : "88,00 € payé par Carte Bancaire le 26/02/2025". |
| --- |

![](https://support.openfire.fr/hc/article_attachments/21452021693084)

## Méthode de comptabilisation directe ou différée des paiements

Lorsque vous enregistrez un paiement dans OpenFire, vous avez le choix entre deux approches principales, chacune ayant un impact différent sur votre comptabilité et la gestion de votre trésorerie :

### **Méthode 1 - Enregistrement avec un compte d’attente (méthode différée) :**

Cette méthode consiste à enregistrer le paiement sur un **compte comptable d’attente** dans un premier temps. Ce compte sert de "zone tampon" pour les fonds qui ne sont pas encore sur votre compte bancaire réel (par exemple, un chèque que vous avez reçu mais pas encore déposé). Le véritable mouvement vers votre compte bancaire ne s'opère qu'ultérieurement, lors du **rapprochement bancaire**. Cette approche est idéale pour un suivi précis des flux financiers. Elle implique que les opérations de remise en banque et / ou de rapprochement bancaire soit réalisées dans OpenFire.

Pour configurer cette méthode, deux options sont possibles :

- Si le champ **Compte de paiement entrants en suspens **du mode de paiement est défini, c’est ce compte qui sera utilisé en contrepartie du compte client.

  ![](https://support.openfire.fr/hc/article_attachments/21452006450716)
- Sinon, c’est le compte de paiement en attente identifié dans les paramètres généraux qui sera utilisé par défaut. Pour vérifier ou modifier les comptes de paiement définis par défaut dans les paramètres généraux, Suivre le chemin d'accès suivant : `Facturation > Paramètres généraux > Comptes par défaut.`
  ![](https://support.openfire.fr/hc/article_attachments/21452006451100)

| **🧑‍🏫Exemple** de pièce comptable de paiement générée :  ![](https://support.openfire.fr/hc/article_attachments/21452021693980) |
| --- |

### **Méthode 2 - Enregistrement direct dans le compte de banque (méthode directe) :**

Avec cette méthode, le paiement est enregistré **directement dans votre compte comptable de banque** dès sa saisie. Cela signifie que le montant est immédiatement considéré comme disponible sur votre compte bancaire. Cette approche est plus simple mais implique généralement que le **rapprochement bancaire ne sera pas effectué dans OpenFire**, mais plutôt dans un autre logiciel dédié à votre comptabilité ou à votre banque. Elle est adaptée si vous ne souhaitez pas gérer les étapes de rapprochement intermédiaire dans OpenFire.

Pour configurer cette méthode, il suffit de définir, pour chaque mode de paiement concerné, le **compte de banque 512** comme **Compte de paiement entrants en suspens.**

![](https://support.openfire.fr/hc/article_attachments/21452006451868)

| **🧑‍🏫Exemple** de pièce comptable de paiement générée :  ![](https://support.openfire.fr/hc/article_attachments/21452006452124) |
| --- |

# Configuration des comptes de paiement par défaut

---

Pour vérifier ou modifier les comptes de paiement définis par défaut dans les paramètres généraux, Suivre le chemin d'accès suivant :  `Facturation > Paramètres généraux > Comptes par défaut.`

Vous y trouverez les champs suivants à configurer :

- **Compte d’attente de la banque** : Les transactions du relevé bancaire sont enregistrées sur ce compte d’attente jusqu’au rapprochement définitif, qui permet de les lier au compte correct.
- **Compte de paiements entrants en suspens** : Ce compte enregistre les paiements jusqu’à ce qu’ils soient associés à un dépôt sur votre relevé bancaire.
- **Compte de paiements sortants en suspens** : Ce compte enregistre les paiements jusqu’à ce qu’ils soient associés à un retrait sur votre relevé bancaire.

# Bonnes pratiques

---

- **Anticipez votre gestion comptable** : Avant de configurer un mode de paiement, il est essentiel de bien comprendre si l'encaissement (ou le décaissement) sera immédiat ou différé et quelles écritures comptables cela impliquera.
- **Nommez clairement vos modes de paiement** : Utilisez des noms explicites qui vous aideront à identifier rapidement le moyen de paiement
- **Vérifiez les paramètres par défaut** : Assurez-vous que les comptes d'attente définis dans les paramètres généraux correspondent à votre flux comptable par défaut si vous utilisez l'option d'enregistrement via un compte d'attente.
- **Testez vos configurations** : Après avoir configuré un nouveau mode de paiement, effectuez quelques tests avec des paiements fictifs pour vous assurer que les écritures comptables sont générées comme attendu.

# Pour aller plus loin

---

| 📓Pour aller plus loin → Gérer les rapprochements bancaires dans OpenFire (à venir) 📓Pour aller plus loin → Importer des relevés bancaires dans OpenFire (à venir) 📓Pour aller plus loin → Configurer les journaux comptables dans OpenFire (à venir) |
| --- |

Mis a jour le : 31/07/2025
