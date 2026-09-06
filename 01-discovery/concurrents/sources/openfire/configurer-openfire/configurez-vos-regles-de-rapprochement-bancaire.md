---
source: https://support.openfire.fr/hc/fr/articles/21587458617628-Configurez-vos-r%C3%A8gles-de-rapprochement-bancaire
categorie: Configurer OpenFire
titre: Configurez vos règles de rapprochement bancaire
date_recuperation: 2026-09-05
---

# Configurez vos règles de rapprochement bancaire

Cet article vous guide dans la **configuration **des fonctionnalités de **rapprochement bancaire**. Il détaille la **configuration des comptes de paiement** en attente, l'ajustement des paramètres **des journaux bancaires** (méthodes de regroupement et modes de lettrage), et illustre ces concepts avec des exemples concrets de réconciliation, que la facture client soit déjà soldée ou non.

Cet article contient les sections suivantes :

- Configurer vos comptes de paiement
  - Configuration des comptes par défaut
  - Surcharge par mode de paiement
- Configurer vos journaux de banque
  - Définir la méthode de regroupement des lignes de transaction bancaire
  - Définir la méthode de regroupement des lignes de transaction bancaire
- Illustration des différents mode de lettrage / réconciliation
  - Cas 1 - Facture client non soldé + 1 transaction bancaire
  - Cas 2 - Facture client soldé + 1 transaction bancaire
- Pour aller plus loin

# Configurer vos comptes de paiement

---

Pour que le rapprochement bancaire fonctionne correctement, vous devez configurer les **comptes de paiement en attente**. Ce compte va servir **d'intermédiaire **pour l'enregistrement des paiements entrant, **en attendant le rapprochement** avec le relevé bancaire.

## Configuration des comptes par défaut

Le paramétrage d'un compte de paiement en attente est obligatoire.

Pour vérifier ou modifier les comptes de paiement définis par défaut dans les paramètres généraux, Suivre le chemin d'accès suivant :  `Facturation > Paramètres généraux > Comptes par défaut.`

Vous y trouverez les champs suivants à configurer :

- **Compte d’attente de la banque** : Les transactions du relevé bancaire sont enregistrées sur ce compte d’attente jusqu’au rapprochement définitif, qui permet de les lier au compte correct.
- **Compte de paiements entrants en suspens** : Ce compte enregistre les paiements jusqu’à ce qu’ils soient associés à un dépôt sur votre relevé bancaire.
- **Compte de paiements sortants en suspens** : Ce compte enregistre les paiements jusqu’à ce qu’ils soient associés à un retrait sur votre relevé bancaire.

Dans le champ **Compte de paiements entrants en suspens**, renseignez le compte générique `512002 Paiements entrants en suspens`.

| 🚨**Avertissement** : Il est **impossible **d'enregistrer un** compte de type banque** comme **Compte de paiements entrants en suspens**. Si vous ne souhaitez pas faire de rapprochement bancaire, vous devrez configurer chaque mode de paiement individuellement. |
| --- |

Voici les configurations standard que nous vous préconisons :

| **Comptes par défaut** | **Compte comptable préconisé** | Lettrable | Type |
| --- | --- | --- | --- |
| Compte d'attente de la banque | 512001 Compte d'attente de la banque | Oui | Actifs circulants |
| Compte de paiements entrants en suspens | 512002 Paiements entrants en suspens | Oui | Actifs circulants |
| Compte de paiements sortants en suspens | 512003 Paiements sortants en suspens | Oui | Passif circulants |
| Compte de virement interne | 580001 Transfert de liquidités | Oui | Actifs circulants |
| Compte des gains d'escompte | 765000 Escomptes obtenus | Non | Produits |
| Compte des pertes d'escompte | 665000 Escomptes accordés | Non | Charges |

## Surcharge par mode de paiement

Vous pouvez définir un compte de paiement en attente spécifique pour un mode de paiement donné.

Suivez le chemin d'accès suivant : `Facturation > Configuration > Paiements > Journaux > Onglet Mode de paiement entrant`.

Sélectionnez un mode de paiement, puis cliquez sur le champ **Compte de paiement en suspens**.

Pour les **modes de paiement entrant**, le compte sélectionné doit être de type **Actifs circulants.**

Pour les **modes de paiement sortant**, le compte sélectionné doit être de type **Passifs circulants.**

| **🧑‍🏫Exemple** : Vous pouvez définir le compte `511200 Chèques à encaisser` pour votre journal de chèques. Si ce champ est laissé vide, OpenFire utilisera le compte par défaut. ![](https://support.openfire.fr/hc/article_attachments/21587458606492) |
| --- |

| 💡**Note **: Si vous ne souhaitez pas passer par un compte d'attente pour l'un de vos modes de paiements, vous devez configurer directement pour chaque mode de paiement, au niveau de son journal, un **Compte de paiement entrant en suspens** de type banque (le compte de banque du journal). Ainsi, lorsque vous enregistrerez un paiement dans OpenFire, il sera automatiquement comptabilisé dans le compte de banque. |
| --- |

| 📓**Pour aller plus loin** → [Configurez vos modes de paiement manuels](https://support.openfire.fr/hc/fr/articles/19096228298012) |
| --- |

# Configurer vos journaux de banque

---

Deux paramètres associés aux journaux de banque doivent être préalablement vérifiés.

### Définir la méthode de regroupement des lignes de transaction bancaire

Correspond au champ **Reconcile Aggregation** présent sur les journaux de banque.

Ce champ **Reconcile Aggregation** permet de définir la granularité de l'agrégation (=niveau de regroupement) des lignes de relevé lors du rapprochement.

La méthode **Statement (Relevé) **regroupe les transactions par *relevé bancaire d'origine*, puis par *date décroissante*.

Dans la fenêtre de rapprochement, le rapprochement est visible comme suivant :

![](https://support.openfire.fr/hc/article_attachments/21587458607644)

Les méthodes **Day **(jour), **Week** (semaine) et **Month **(mois) **regroupe **les transactions **par critère de date** de transaction, respectivement selon le jour, la semaine ou le mois de la transaction.

Par exemple, le rapprochement par jour est visible comme suivant :

![](https://support.openfire.fr/hc/article_attachments/21587462178204)

## Définir le Mode de lettrage / réconciliation

Le **mode de lettrage** se configure au niveau du journal bancaire. Il permet de définir la façon dont OpenFire doit traiter les écritures existantes au moment de la réconciliation bancaire.

![](https://support.openfire.fr/hc/article_attachments/21587462179484)

Deux options sont possibles :

- **Conserver les comptes d’attente** : Les écritures comptables sur les comptes d'attente sont conservées. Un nouveau mouvement de compte est créé pour lettrer l'ensemble. C'est le mode par défaut recommandé.
- **Modifier la pièce** : Les écritures comptables existantes sont modifiées pour supprimer les comptes d'attente et lettrer directement avec les écritures de contrepartie.

| 🚨**Avertissement** : La méthode "Modifier la pièce" doit être utilisée avec prudence en ce qu'elle supprime certaines données comptables générées sur des comptes d'attente durant l'action de rapprochement bancaire. |
| --- |

| 💡**Note **: Lors de l’installation du module, toutes les lignes de relevé bancaire déjà réconciliées sont par défaut en mode “modifier la pièce" |
| --- |

# Illustration des différents mode de lettrage / réconciliation

### Cas 1 - Facture client non soldé + 1 transaction bancaire

Ce cas correspond à une gestion ou les règlements ne sont pas enregistrés dans la gestion commerciale mais directement pilotés par les relevés bancaires.

Nous avons donc :

- 1 facture client pour un montant de 180 € TTC
- 1 transaction bancaire pour un montant de 180 € TTC

Avant lettrage, les écritures comptables sont comme suivantes :

![](https://support.openfire.fr/hc/article_attachments/21587462180636)

Voici comment évoluent ces écritures suivant le mode de réconciliation retenue :

#### Cas 1A - Réconciliation “Conserver les comptes d’attente”

Dans ce cas, lors du rapprochement bancaire, OpenFire va :

- **Créer une nouvelle pièce de banque** pour solder le compte client et le compte d'attente (la pièce GAM/2025/0004 dans notre exemple crédite le compte client du montant du règlement et débite le compte d'attente 512001 utilisé lors de l'enregistrement de la transaction bancaire.
- **Lettrer les comptes clients et les comptes d'attentes** entre eux.

![](https://support.openfire.fr/hc/article_attachments/21587462181148)

#### Cas 1B - Réconciliation “Modifier la pièce”

Dans ce cas, lors du rapprochement bancaire, OpenFire va :

- **Remplacer**, dans la pièce de banque,** le compte d'attente par le compte client**
- **Lettrer **les écritures de **compte client **entre elles

![](https://support.openfire.fr/hc/article_attachments/21587458612380)

| 🚨**Avertissement** : Bien que plus légère en production d'écritures comptables, cette méthode modifie au fil de l'eau des écritures comptables de banque et doit donc être utilisé avec précaution. |
| --- |

### Cas 2 - Facture client soldé + 1 transaction bancaire

Ce cas correspond à une gestion ou les règlements sont enregistrés dans la gestion commerciale et rapprochés des transactions du relevé bancaire par les équipes comptables lors des opérations de rapprochement bancaire.

Nous avons donc :

- 1 facture client pour un montant de 180 € TTC
- 1 règlement client pour un montant de 180 € TTC
- 1 transaction bancaire pour un montant de 180 € TTC

Avant lettrage, les écritures comptables sont comme suivantes :

![](https://support.openfire.fr/hc/article_attachments/21587458613020)

Voici comment évoluent ces écritures suivant le mode de réconciliation retenue :

#### Cas 2A - Réconciliation “Conserver les comptes d’attente”

Dans ce cas, lors du rapprochement bancaire, OpenFire va :

- **Créer une nouvelle pièce de banque** pour :
  - **Solder le compte d'attente de la banque** généré à l'enregistrement de la transaction via le relevé bancaire (écriture au débit).
  - **Solder le compte de paiement en suspens** généré à l'enregistrement du paiement depuis la gestion commerciale (écriture au débit).
- **Lettrer les comptes de paiement en suspens et les comptes d'attentes** entre eux.

![](https://support.openfire.fr/hc/article_attachments/21587462184732)

#### Cas 2B - Réconciliation “Modifier la pièce”

Dans ce cas, lors du rapprochement bancaire, OpenFire va :

- **Remplacer**, dans la pièce de banque,** le compte d'attente de la banque** (généré par l'import du relevé bancaire)** **par le compte de **paiement en suspens**
- **Lettrer **les écritures du **compte de paiement en suspens** entre elles afin de solder ce compte.

![](https://support.openfire.fr/hc/article_attachments/21587462186780)

# Pour aller plus loin

---

| 📓**Pour aller plus loin** → [Réalisez vos rapprochements bancaires](https://support.openfire.fr/hc/fr/articles/21560286477340) 📓**Pour aller plus loin** → [Intégrez vos relevés bancaire dans OpenFire](https://support.openfire.fr/hc/fr/articles/21561162891932) 📓**Pour aller plus loin** → Utilisez les modèles de rapprochement bancaire automatiques (à venir) |
| --- |

Mis a jour le : 07/08/2025
