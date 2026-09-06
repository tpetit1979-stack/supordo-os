---
source: https://support.openfire.fr/hc/fr/articles/23263690195612-Configurer-les-connecteurs-d-achat-pour-passer-mes-commandes-fournisseurs
categorie: Configurer OpenFire
titre: Configurer les connecteurs d'achat pour passer mes commandes fournisseurs
date_recuperation: 2026-09-05
---

# Configurer les connecteurs d'achat pour passer mes commandes fournisseurs

Cet article vous présente les connecteurs d'achat disponibles dans OpenFire et vous aide à les configurer pour simplifier vos saisies de commandes auprès de nos fournisseurs partenaires.

**Cette fonctionnalité nécessite l'installation de modules spécifiques.**

Cet article contient les sections suivantes:

- [Les connecteurs d'achat disponibles dans OpenFire](#h_01K8R5DHM2KS9N680P91VZ3C5Z)
- [Configurer mon connecteur d'achat](#h_01K8R5P05EFAT9J8F18A1G7HPA)

  **📓**Pour aller plus loin →
  [Utiliser les connecteurs d'achat](https://support.openfire.fr/hc/fr/articles/24983635969820)

## Les connecteurs d'achat disponibles dans OpenFire

---

Parmi les nombreux [partenaires](https://openfire.fr/tarif-centralise/catalogues-partenaires) OpenFire, certains ont fait le choix de mettre en place un connecteur d'achat, c'est-à-dire une fonctionnalité qui vous permet de passer vos commandes d'achat directement depuis votre logiciel OpenFire.

Grâce à ces connecteurs, vous vous épargnez une ressaisie fastidieuse, tout en vous laissant la possibilité de contrôler votre panier d'achat avant de le valider sur la plateforme du fournisseur.

À ce jour, les connecteurs d'achat disponibles dans OpenFire concernent les fournisseurs suivant:

- [Poujoulat](#h_01K8R5Y9HFER3WQDS3F26CM9PM)
- [Altema - Modinox](#h_01K8RA02SR159ESS9NMF7R2NDR)
- [Laudevco](#h_01K8R6AS3F5YZG532GR2X39K8A)
- [Lorflex](#h_01KG2MSSVXAGY80ADEBK01MECM)
- [Turbofonte](#h_01KS4YZBG40GAYBQAKNWCW8RBJ)

##

## Configurer mon connecteur d'achat

---

| 💡**Note **: L'utilisation du connecteur d'achat             nécessite l'installation d'un module spécifique. Nous vous             invitons à formuler votre demande à support@openfire.fr pour             être accompagné dans cette démarche.                                   L'accès au connecteur             d'achat est soumis à l'autorisation préalable du fournisseur             partenaire. |
| --- |

La configuration dépend de la technologie utilisée par le fournisseur. Elle diffère donc selon les connecteurs d'achat.

Chemin d'accès: *Paramètres > Paramètres des connecteurs*

- [*Configurer mon connecteur d'achat Poujoulat*](#h_01K8R5Y9HFER3WQDS3F26CM9PM)
- [*Configurer mon connecteur d'achat Modinox*](#h_01K8R6AS3F2CRS7P16TS5XDTBM)
- [*Configurer mon connecteur d'achat Laudevco*](#h_01K8R6AS3F5YZG532GR2X39K8A)
- [*Configurer mon connecteur d'achat Lorflex*](#h_01K8R6AS3F5YZG532GR2X39K8A)
- [Configurer mon connecteur d'achat Turbofonte](#h_01KS4YZBG40GAYBQAKNWCW8RBJ)

### Configurer mon connecteur d'achat Poujoulat

| 💡**Note **: Il est nécessaire d'être connecté au Tarif Centralisé Poujoulat pour utiliser ce connecteur d'achat. |
| --- |

Dans les paramètres, le connecteur est à configurer avec les éléments suivants:

![](https://support.openfire.fr/hc/article_attachments/23264037313436)

1. **Adresse du serveur: **[http://pro.poujoulat.com/CatEstimate/rest/estimateOF/envoyerDevisOpenfire/](http://pro.poujoulat.com/CatEstimate/rest/estimateOF/envoyerDevisOpenfire/)
2. **URL de redirection: **[http://pro.poujoulat.com/](http://pro.poujoulat.com/)
3. **Fournisseurs: **Pour sélectionner le fournisseur éligible dans le champ Fournisseurs, le contact associé doit être identifié comme fournisseur (*Contacts > Onglet "Ventes & Achats)*
  ![](https://support.openfire.fr/hc/article_attachments/23264037317660)
4. **Marque: **Pour sélectionner la marque concernée par le connecteur, la marque dois être associée au fournisseur précédemment sélectionné (*Vente > Configuration > Marques).*

![](https://support.openfire.fr/hc/article_attachments/23264037318172)

---

### Configurer mon connecteur d'achat Modinox

Dans les paramètres, la configuration du connecteur est pré-remplie avec l'adresse du serveur et la clé API.

![](https://support.openfire.fr/hc/article_attachments/23263716420892)

1. Votre **identifiant client**, votre **mail client** et votre **mot de passe** sont les identifiants que vous utilisez pour vous connecter à la plateforme Modinox lorsque vous passez vos commandes d'achat. Ils peuvent différer des identifiants que vous utilisez pour vous connecter sur votre espace OpenFire.
  Si vous n'avez pas ces accès, nous vous invitons à vous rapprocher de votre fournisseur.
2. **Fournisseurs:** Pour sélectionner le fournisseur éligible dans le champ Fournisseurs, le contact associé doit être identifié comme fournisseur (*Contacts > Onglet "Ventes & Achats)*

![](https://support.openfire.fr/hc/article_attachments/23264037317660)

---

### Configurer mon connecteur d'achat Laudevco

Dans les paramètres, la configuration du connecteur est pré-remplie avec l'adresse du serveur, l'URL de redirection et la clé DOLAPIKEY.

![](https://support.openfire.fr/hc/article_attachments/23264030895644)

1. **Mail client: **Le mail à renseigner est celui que vous utilisez pour vous connecter sur la plateforme Laudevco. Le mail peut différer du mail que vous utilisez pour vous connecter à votre espace OpenFire.
2. **Fournisseurs: **Pour sélectionner le fournisseur éligible dans le champ Fournisseurs, le contact associé doit être identifié comme fournisseur (*Contacts > Onglet "Ventes & Achats).*

![](https://support.openfire.fr/hc/article_attachments/23264037317660)

---

### Configurer mon connecteur d'achat Lorflex

![](https://support.openfire.fr/hc/article_attachments/26502586432412)

1. **Adresse serveur Lorflex: **Cette adresse est invariable
2. **Mail d'accès au compte Lorflex**: il s'agit du mail que vous utilisez pour vous connecter au site Lorflex lorsque vous passez vos commandes d'achat. Il peut différer du mail que vous utilisez pour vous connecter sur votre espace OpenFire.
  Si vous n'avez pas de compte sur le site Lorflex, vous pouvez en créer un directement sur le site https://lorflex.com/.
3. Votre **SIRET** doit correspondre au SIRET renseigné chez Lorflex.
4. **Fournisseurs: **Pour sélectionner le fournisseur éligible dans le champ Fournisseurs, le contact associé doit être identifié comme fournisseur (*Contacts > Onglet "Ventes & Achats).*

![](https://support.openfire.fr/hc/article_attachments/23264037317660)

---

### Configurer mon connecteur d'achat Turbofonte

![](https://support.openfire.fr/hc/article_attachments/27617490248348)

1. **Adresse serveur Turbofonte: **Cette adresse est invariable
2. **Clé API Turbofonte: **Cette clé est invariable
3. **Clé Cookies Turbofonte: **Cette clé est invariable
4. **Mail client Turbofonte**: il s'agit du mail que vous utilisez pour vous connecter à votre espace Turbofonte lorsque vous passez vos commandes d'achat. Il peut différer du mail que vous utilisez pour vous connecter sur votre espace OpenFire.
5. **Fournisseurs Turbofonte: **Pour sélectionner le fournisseur éligible dans le champ Fournisseurs, le contact associé doit être identifié comme fournisseur (*Contacts > Onglet "Ventes & Achats).*

![](https://support.openfire.fr/hc/article_attachments/23264037317660)

Mis a jour le : 21/05/2026
