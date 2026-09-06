---
source: https://support.openfire.fr/hc/fr/articles/19096272928796-Banques-et-comptes-bancaires
categorie: Configurer OpenFire
titre: Banques et comptes bancaires
date_recuperation: 2026-09-05
---

# Banques et comptes bancaires

Cet article vous explique comment créer et configurer les comptes bancaires de votre société et le journal comptable associé dans l'application OpenFire.

Cet article contient les sections suivantes :

- Créer une banque
- Créer un compte bancaire
- Vérifier le journal comptable associé

# Créer une banque

---

Pour associer un compte bancaire, vous devez d'abord créer la banque correspondante.

**Chemin d'accès :** `Contacts > Configuration > Comptes bancaires > Banques.`

**Procédure :**

1. Cliquer sur le bouton **Nouveau** pour ajouter une nouvelle banque, ou cliquer sur une banque existante pour la modifier.
2. Saisir les informations suivantes :
  - **Nom**
  - **Code d'identification bancaire**
  - **Adresse bancaire**
  - **Téléphone**
  - **Email**
3. Cliquer sur **Enregistrer**.

![](https://support.openfire.fr/hc/article_attachments/21536169405468)

# Créer un compte bancaire

---

Une fois la banque créée, vous pouvez ajouter le compte bancaire associé.

| 🚨**Avertissement** : pour créer un compte bancaire de votre société, RDV dans l'application de facturation / comptabilité uniquement. |
| --- |

**Chemin d'accès :** `Facturation > Configuration > Banques > Ajouter un compte bancaire`

**Procédure :**

Cliquer sur le menu "Ajouter un compte bancaire" afin d'ouvrir l'assistant de création.

![](https://support.openfire.fr/hc/article_attachments/21536169409052)

Saisir les informations suivantes :

- **Numéro de compte** : L'IBAN de votre compte bancaire.
- **Banque** : Sélectionner dans la liste déroulante la banque que vous venez de créer.
- **Code d'identification bancaire** : Code BIC associée à la banque
- **Journal **: le journal comptable associé au compte bancaire. Sélectionner un journal pour le lier à ce compte, ou laisser vide pour créer un nouveau journal lié à ce compte bancaire ; dans ce cas :
  - Le journal sera créé avec l'IBAN en nom de journal.
  - Le compte comptable du journal sera créé avec un compte 512 et un libellé reprenant l'IBAN

Cliquer sur **Enregistrer**.

![](https://support.openfire.fr/hc/article_attachments/21536448206108)

Au niveau du journal créé, vous pouvez ainsi vérifier ou modifier :

- Le nom du journal
- Le compte bancaire

| 💡**Note **: il est possible de procéder à l'ajout d'un **compte bancaire** en procédant d'abord à la création du **journal de banque**, et en ajoutant ensuite le **numéro de compte** associé. |
| --- |

| 📓**Pour aller plus loin** → [Configurer vos journaux](https://support.openfire.fr/hc/fr/articles/19096254481308) |
| --- |

Mis a jour le : 04/08/2025
