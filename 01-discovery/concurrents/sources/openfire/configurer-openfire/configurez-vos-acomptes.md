---
source: https://support.openfire.fr/hc/fr/articles/20230718384028-Configurez-vos-acomptes
categorie: Configurer OpenFire
titre: Configurez vos acomptes
date_recuperation: 2026-09-05
---

# Configurez vos acomptes

Dans OpenFire, la facturation d'un acompte passe par l'utilisation d'un article spécifique **Acompte **dont la configuration doit être vérifiée par les Administrateur Client avant toute facturation.

Le présent article précise les options de configuration de vos Acomptes disponibles dans OpenFire.

Cet article contient les sections suivantes :

- Configurez le produit Acompte
- Configurez la catégorie de produit Acompte
- Ajustez les paramètres généraux

# Configurez le produit Acompte

---

Dans OpenFire, les acomptes sont facturés au travers d'un produit spécifique : le produit Acompte.

Le produit Acompte présente une configuration particulière, réalisée par défaut de manière standard dans votre environnement OpenFire :

- Il est de type **Service **;
- Sa catégorie de produit est **Acompte **;

![](https://support.openfire.fr/hc/article_attachments/20230708364572)

- Dans l'onglet Vente, la Taxe à la vente est **TVA de base Acompte (vente)**

![](https://support.openfire.fr/hc/article_attachments/21414226739100)

# Configurez la catégorie de produit Acompte

---

La configuration de la catégorie de produit Acompte est essentielle pour définir la manière dont vos acomptes sont enregistrés et déclarés en comptabilité.

Pour accéder à la catégorie de produit Acompte, suivre le chemin d'accès suivant :

- Pour le plan Basique : OpenFire > Configuration > Ventes > Catégories de produit
- Pour les autres plans : Facturation > Configuration > Gestion > Catégories de produit

| 💡**Note **: La loi de finances 2022 est venue aligner le régime des acomptes sur les biens sur celui des prestations de services. Dans ce cadre, à partir du 1er janvier 2023, en cas de versement d'un acompte, la TVA sur les livraisons de biens est exigible dès l'encaissement de cet acompte, par le fournisseur et non plus lors de la livraison du bien |
| --- |

Pour faciliter vos déclarations de TVA et vos opérations de clôture comptable (cut-off), nous vous recommandons de configurer des comptes de produit spécifiques pour les acomptes, déclinés par taux de TVA.

La catégorie d'acompte est ainsi préconfigurée dans votre environnement en utilisant les comptes suivant :

- un compte de revenus dédié : le compte **707900 Acompte**.
- un compte de charges standard : le compte **409100 Fournisseurs avance et acomptes versés sur commande**

![](https://support.openfire.fr/hc/article_attachments/21414226741660)

Cette approche permet à OpenFire d'utiliser automatiquement le compte d'acompte approprié en fonction de la position fiscale et des taxes associées à la transaction.

La configuration standard de votre base s'appuie sur les comptes suivants :

| **Compte racine** | **Comptes déclinés par taux de TVA** |
| --- | --- |
| 707900 Acompte | 707905 Acompte 5.5% |
| 707900 Acompte | 707910 Acompte 10.0% |
| 707900 Acompte | 707920 Acompte 20.0% |
| 707900 Acompte | 707900 Acompte |

| 📓**Pour aller plus loin** → Configurez vos **Taxes** 📓**Pour aller plus loin** → Configurez vos **Positions fiscales** |
| --- |

# Ajuster les paramètres généraux

---

Pour identifier le produit Acompte comme tel :

1. Rendez-vous dans les paramètres de ventes : Ventes > Configuration > Paramètres
2. Recherchez ensuite la configuration de l'acompte (vous pouvez vous aider de la barre de recherche en haut à droite en tapant "acompte") ;
3. Dans le champ "Produit utilisé pour les acomptes", sélectionnez le produit Acompte ;
4. Faites de même avec la catégorie des acomptes.

![](https://support.openfire.fr/hc/article_attachments/20230708365084)
🚨Avertissement : si la configuration est déjà faite, il est déconseillé de la modifier. En cas de doute, [rapprochez-vous de nos équipes OpenFire](https://support.openfire.fr/hc/fr/articles/16871194267292).

Mis a jour le : 07/08/2025
