---
source: https://support.openfire.fr/hc/fr/articles/21602603387548-Utilisez-des-mod%C3%A8les-rapprochement-bancaire-automatiques
categorie: Utiliser OpenFire
titre: Utilisez des modèles rapprochement bancaire automatiques
date_recuperation: 2026-09-05
---

# Utilisez des modèles rapprochement bancaire automatiques

Cet article vous guidera dans la création et la gestion des modèles de rapprochement bancaire pour simplifier et automatiser le lettrage de vos relevés bancaires dans OpenFire.

| 🧩**Prérequis** →  [Configurez vos rapprochements bancaires](https://support.openfire.fr/hc/fr/articles/21587458617628) 🧩**Prérequis** →  [Réalisez vos rapprochements bancaires](https://support.openfire.fr/hc/fr/articles/21560286477340) 🧩**Prérequis** →  [Comment intégrer vos relevés bancaire dans OpenFire ?](https://support.openfire.fr/hc/fr/articles/21561162891932) |
| --- |

Cet article contient les sections suivantes :

- [Qu'est-ce qu'un modèle de rapprochement ?](#h_01K222B88AYA3KJ6ESBPVKGZ2N)
- [Créer un modèle de rapprochement](#h_01K22230Z727XQ9VQSTP1FJ4PK)
- [Types de modèles de rapprochement](#h_01K2233B384EXDGRGHVNZXC4EF)
  - [Règle pour rapprocher les factures clients/fournisseurs](#h_01K22MGJDNNY5E2B6RCRM9GYJN)
  - [Bouton qui génère l'écriture de contrepartie](#h_01K22230Z4RS33ES887Q8JWFH8)
  - [Règle pour suggérer l'écriture de la contrepartie](#h_01K22230Z5BK4T8DCMEJT8750W)
- [Bonnes pratiques](#h_01K24FM8GNSERXB44Z5RK19KCN)

# Qu'est-ce qu'un modèle de rapprochement ?

---

Les modèles de rapprochement sont des règles prédéfinies qui permettent d’automatiser ou de faciliter le lettrage des lignes de vos relevés bancaires avec les écritures comptables correspondantes. Ces modèles sont particulièrement utiles pour les opérations récurrentes, comme le règlement de factures ou la gestion de frais bancaires.

Pour consulter les modèles de rapprochement par défaut, suivez le chemin d'accès suivant :

*Facturation > Configuration > Banque > Modèle de rapprochement*

# Créer un modèle de rapprochement

---

Suivez ces étapes pour créer un nouveau modèle de rapprochement :

1. Suivre le chemin d'accès suivant : `Comptabilité > Configuration > Modèles de rapprochement`.
2. Cliquer sur le bouton **Créer**.
3. Saisir le **Nom** du modèle.
4. Sélectionner le **Type** de modèle parmi les options expliquées ci-dessus.
5. Configurer les **Conditions** pour déclencher le modèle (par exemple, le montant est exact, le libellé contient un mot-clé).
6. Définir les **Actions** du modèle (par exemple, un compte de contrepartie spécifique, la validation automatique).
7. Cliquer sur le bouton **Enregistrer** pour sauvegarder votre modèle.

| 💡**Note **: les différentes options et champs du modèles sont détaillés dans la présentation des types de modèle ci-dessous |
| --- |

# Types de modèles de rapprochement

---

Il existe trois types de modèles de rapprochement :

- Règle pour rapprocher les factures clients/fournisseurs
- Bouton qui génère l'écriture de contrepartie
- Règle pour suggérer l'écriture de la contrepartie

Ces règles sont détaillées ci-dessous

| 🚨**Avertissement** : Si un enregistrement correspond à plusieurs modèles de rapprochement, le premier de la séquence de modèles est appliqué. Vous pouvez réorganiser l'ordre en faisant glisser et en déposant la poignée à côté du nom. |
| --- |

## 1/ Règle pour rapprocher les factures clients/fournisseurs

### Présentation de la règle

Ce type de modèle vous permet de lier automatiquement une ligne de relevé bancaire à une facture client ou fournisseur.

| **🧑‍🏫Exemple** : Vous créez une règle pour rapprocher automatiquement les paiements de factures d’un montant exact. Lorsqu’une ligne de relevé bancaire de 1000 € est importée, le système la lie automatiquement à la facture de 1000 € correspondante et la marque comme payée. |
| --- |

Un modèle de rapprochement de ce type est proposé par défaut dans OpenFire, intitulé : ***Factures clients/fournisseurs totalement lettrées ***

### Présentation du modèle par défaut *Factures clients/fournisseurs totalement lettrées*

*Facturation > Configuration > Banque > Modèle de rapprochement*

En partie haute, on retrouve les paramètres principaux suivants :

![](https://support.openfire.fr/hc/article_attachments/21612014841756)

**Validation automatique** : si les conditions que vous avez définies sont remplies, le système peut suggérer l'écriture comptable correspondante ou la valider automatiquement.

- **Rapprochement sans validation automatique** : Si la règle est respectée, le système vous proposera l'écriture comptable au moment du rapprochement, mais vous devrez la valider manuellement.
- **Rapprochement avec validation automatique** : Si la règle est respectée, le système effectue le lettrage et valide l'écriture comptable automatiquement dès l'importation du relevé bancaire.

**Rechercher dans la limite de X mois** : nombre de mois dans le passé dont les entrées sont à considérer pour appliquer le modèle.

**Ordre de rapprochement **: deux valeurs sont possibles et déterminent l'ordre dans lequel OpenFire va procéder au rapprochement, priorisant les transactions les plus récentes ou les plus anciennes.

#### Définition du périmètre des transactions concernées

OpenFire propose ensuite une liste de champs permettant de définir le périmètre des transactions concernées par le modèle, dans l'onglet **Conditions des transactions bancaires**.

![](https://support.openfire.fr/hc/article_attachments/21612014842652)

**Journaux disponibles : **sélection des journaux de banques ou d'espèces éligibles au modèle.

**Type de montant : **permet de définir les transactions auxquelles ce modèle s'applique, en dissociant les paiements entrants (**Montant reçu**), les paiements sortant (**Montant payé**), ou les deux (**Montant payé/reçu**)

**Etat du montant : **Le modèle de rapprochement ne sera appliqué que lorsque le montant est plus petit que, plus grand que, ou entre le(s) montant(s) spécifié(s).

**Tolérance de paiement : **définit la marge d'erreur autorisé en cas de sous-paiement. Cette tolérance peut être définie en % ou en valeur.

| 🚨**Avertissement** : pour du lettrage automatique, nous vous conseillant de rester dans un rapprochement sans tolérance. |
| --- |

OpenFire propose ensuite trois valeurs (***libellé***, ***Note ***et ***Référence) ***comme support de règles de Rapprochement entre la transaction et les **factures fournisseur / client**. Si OpenFire trouve la référence de la facture ou du paiement dans un des ces trois champs, alors le modèle de rapprochement pourra s'appliquer.

![](https://support.openfire.fr/hc/article_attachments/21612014843420)

La recherche peut également se faire si OpenFire trouve une correspondance entre d'un côté le contenu des champs **Libellé **et/ou **note** et/ou **Type de transaction** et de l'autre la facture, selon 3 règles possibles :

- ***Contient ***: doit contenir cette chaine de caractère (insensible à la casse).
- ***Ne contient pas*** : l'opposé de "Contient".
- ***Match Regex** *: définissez vos propres expressions régulières.

Un contrôle sur l'application du modèle peut-être fait également selon que le **Partenaire est défini** dans la transaction ou non.

Dans ce cas il vous faut préciser les partenaires ou les catégories de partenaires (vérification faite sur les étiquettes de contact) concerné par le modèle

![](https://support.openfire.fr/hc/article_attachments/21612014844060)

#### Automatisation de la reconnaissance partenaire

Pour rendre le rapprochement bancaire encore plus efficace, OpenFire vous permet de** configurer des règles d'automatisation pour la reconnaissance des partenaires** (clients ou fournisseurs). Plutôt que de chercher le bon contact à chaque rapprochement, vous définissez des règles qui permettent à OpenFire de faire le lien pour vous.

Par exemple, vous pouvez créer une règle simple : si le libellé d'une transaction bancaire entrante contient un mot-clé précis, comme un numéro de référence ou une abréviation spécifique, OpenFire associera automatiquement cette transaction au client correspondant.

Dès que le paiement apparaît sur votre relevé, le système est capable d'identifier le partenaire sans votre intervention.

![](https://support.openfire.fr/hc/article_attachments/21612014844444)

Pour configurer une telle règle, vous devez simplement vous rendre dans l'onglet Association du partenaire et renseigner les champs suivants :

- **Texte à trouver dans le libellé** : Le mot-clé ou la référence que OpenFire doit rechercher dans la description de la transaction.
- **Texte à trouver dans les notes** : Une condition supplémentaire, si nécessaire, pour affiner la recherche.
- **Partenaire** : Le contact (client ou fournisseur) qui doit être associé si les conditions sont remplies.

| **🧑‍🏫Exemple** : [A illustrer] |
| --- |

Une facture fournisseur :

![](https://support.openfire.fr/hc/article_attachments/21612020765596)

Une transaction :

![](https://support.openfire.fr/hc/article_attachments/21612014846236)

Au moment du rapprochement bancaire, OpenFire associe automatiquement la transaction avec la facture générée grâce au mot clé :

![](https://support.openfire.fr/hc/article_attachments/21612020766620)

## 2/ Bouton qui génère l'écriture de contrepartie

### Présentation de la règle

Ce modèle crée un bouton de validation qui génère une écriture de contrepartie. C'est idéal pour les frais récurrents qui ne sont pas liés à une facture.

- **Compte de contrepartie** : Le système génère un bouton pour vous permettre de générer l'écriture de contrepartie vers le compte que vous avez défini.
- **À vérifier** : En cochant cette option, la ligne de relevé bancaire passera au statut **À vérifier** après validation, vous laissant ainsi la possibilité de la revoir avant validation finale.

Ces règles sont très flexibles et peuvent être basées sur le libellé, le montant, la date, ou d'autres champs de la ligne de relevé bancaire.

| **🧑‍🏫Exemple** : Vous créez une règle pour toutes les lignes de relevé bancaire dont le libellé contient "Frais bancaires". Le système suggèrera automatiquement le compte comptable **627800 (Services bancaires)** pour toutes ces lignes. |
| --- |

Un modèle de rapprochement de ce type est proposé par défaut dans OpenFire, intitulé : ***Frais bancaire***

### Présentation du modèle par défaut *Frais bancaires*

*Facturation > Configuration > Banque > Modèle de rapprochement*

![](https://support.openfire.fr/hc/article_attachments/21612020768284)

Illustration :

Ce modèle de rapprochement, visuellement disponible sous forme de bouton dans la zone 3 de l'interface de rapprochement, permet d'ajouter l'écriture de contrepartie du modèle (en l'espèce le 627800 Autres frais et commissions sur prestations de services), à l'opération de lettrage en cours. Lorsque vous cliquez sur le bouton, la contrepartie proposée par défaut sera remplacée par la contrepartie du modèle.

![](https://support.openfire.fr/hc/article_attachments/21625589562524)

## 3/ Règle pour suggérer l'écriture de la contrepartie

Ce type de modèle permet de suggérer un compte de contrepartie spécifique en fonction de certaines conditions. Vous pouvez utiliser la reconnaissance par le contenu du **Libellé **de la transaction pour simplifier l'application du modèle.

Exemple ci-dessous, on veut créer à la volé la contrepartie charge et TVA sur la base d'un prélèvement orange. La transaction bancaire associée.

![](https://support.openfire.fr/hc/article_attachments/21625589564060)

Notes :

- Les montant doivent être exprimés avec un "." en séparateur de décimal.
- La dernière ligne doit être du type **Pourcentage du solde**, de préférence

| 💡**Note **: Ce format marche avec le type **Bouton **qui génère l'écriture de contrepartie aussi bien qu'avec le type **suggestion de contrepartie**. |
| --- |

Au moment du rapprochement bancaire, l'application du modèle permet de générer automatiquement la contrepartie de charge et de TVA (via le bouton dans l'exemple ci-dessous).

![](https://support.openfire.fr/hc/article_attachments/21625572774684)

Si les montants des lignes ne sont pas strictement les bons, il est possible de modifier les lignes unitairement en cliquant sur l'onglet **Opération manuelle.**

Les libellés des écritures générées sont repris de la configuration du modèle.

Il est possible de modifier à la volée la suggestion de la contrepartie, en sélectionnant la ligne et en allant dans l'onglet "Opération manuelle". Si les montants ne sont plus équilibrés, OpenFire suggérera des contreparties jusqu'à retrouver l'équilibre.

![](https://support.openfire.fr/hc/article_attachments/21625572775836)

# Bonnes pratiques

---

- **Soyez précis dans vos conditions** : Des conditions trop larges peuvent entraîner des suggestions ou des validations incorrectes. Par exemple, utilisez des mots-clés spécifiques et uniques dans le libellé de la transaction.
- **Commencez par la suggestion** : Il est recommandé de commencer par des modèles de rapprochement sans validation automatique. Une fois que vous êtes sûr que les règles fonctionnent comme prévu, vous pouvez activer l'option de validation automatique.
- **Vérifiez régulièrement** : Même avec des modèles de rapprochement, il est important de vérifier régulièrement le lettrage effectué pour s'assurer qu'il n'y a pas d'erreur.

Mis a jour le : 08/08/2025
