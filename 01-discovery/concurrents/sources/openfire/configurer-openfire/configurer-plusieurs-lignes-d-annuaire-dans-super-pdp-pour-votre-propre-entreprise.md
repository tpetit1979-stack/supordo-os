---
source: https://support.openfire.fr/hc/fr/articles/28949959830044-Configurer-plusieurs-lignes-d-annuaire-dans-SUPER-PDP-pour-votre-propre-entreprise
categorie: Configurer OpenFire
titre: Configurer plusieurs lignes d'annuaire dans SUPER PDP pour votre propre entreprise
date_recuperation: 2026-09-05
---

# Configurer plusieurs lignes d'annuaire dans SUPER PDP pour votre propre entreprise

Cet article vous explique comment créer et gérer plusieurs lignes d'annuaire au sein de votre compte partenaire SUPER PDP. Cette configuration est idéale si vous possédez différents services d'achats ou si vous souhaitez router automatiquement vos factures vers des journaux comptables spécifiques.

Cet article contient les sections suivantes :

- [Section 1 : Comprendre l'utilité des lignes d'annuaire multiples](#h_01KXNDWF4Z9ERN43YY70353QJJ)
- [Section 2 : Consulter vos lignes d'annuaire existantes](#h_01KXNDXX76JBM2Y3Q7XEAP62DW)
- [Section 3 : Ajouter une nouvelle ligne d'annuaire](#h_01KXNDZ9508VDJPSNPYX6EXYC3)
- [Bonnes pratiques](#h_01KXNE3G1AYJ415V62THWWY622)

Suivre le chemin d'accès suivant : Navigateur web > Se connecter à votre espace client sur https://www.superpdp.tech

| 💡**Note **: Si vous avez opté pour la délégation à OpenFire lors de l'enregistrement de votre compte SUPER PDP, vous n'avez peut-être pas encore défini de mot de passe.  Effectuez simplement une **demande de réinitialisation** via le lien "Mot de passe oublié" sur `https://www.superpdp.tech/app/users/reset_password` en utilisant l'adresse e-mail déclarée lors de votre inscription. |
| --- |

## Section 1 : Comprendre l'utilité des lignes d'annuaire multiples

La réforme de la facturation électronique vous permet de définir plusieurs lignes d'annuaire pour une même entité. Celles-ci servent à identifier formellement vos différents points de réception de factures aux yeux de vos fournisseurs et partenaires.

Plusieurs cas de figure justifient la création de lignes multiples :

- **Utilisation de logiciels multiples** : router les factures vers différents logiciels de gestion que vous utiliseriez en parallèle.
- **Organisation par services** : séparer les flux documentaires si vous disposez de différents départements ou services d'achats indépendants dans votre entreprise.
- **Routage comptable** : diriger automatiquement les bonnes factures directement vers les journaux d'achats correspondants dans votre comptabilité.

##

##

## Section 2 : Consulter vos lignes d'annuaire existantes

Avant d'ajouter de nouveaux points de réception, il est conseillé de visualiser vos adresses déjà actives.

1. Se connecter à l'interface en ligne de SUPER PDP.
2. Consulter la liste affichée dans la section **Lignes d'annuaire** au centre de votre écran.
3. Vérifier que le statut de chaque ligne indique bien la mention **OK**.

![](https://support.openfire.fr/hc/article_attachments/28949959820316)

## Section 3 : Ajouter une nouvelle ligne d'annuaire

Pour créer une nouvelle adresse de facturation, suivez ces quelques étapes :

- Cliquer sur le bouton **Nouvelle ligne d'annuaire**.
- Renseigner l'adresse de routage souhaitée dans le champ **Adresse**.
- Cliquer sur le bouton **Créer** pour valider et enregistrer votre nouvelle ligne.

![](https://support.openfire.fr/hc/article_attachments/28949959820828)

| **🧑‍🏫Exemple** :  Une adresse PPF (Portail Public de Facturation) valide sur l'annuaire respecte des formats bien précis basés sur vos identifiants d'entreprise. Elle peut prendre la forme simple de votre SIREN ou de votre SIRET. Pour des besoins de routage interne, vous pouvez utiliser un suffixe explicite collé à votre numéro, tel que : `853322915_EXPLOITATION` |
| --- |

## Bonnes pratiques

- **Vérification du statut** : Assurez-vous toujours que le statut de votre nouvelle ligne d'annuaire passe bien à **OK** immédiatement après sa création pour garantir son bon fonctionnement.
- **Nomenclature claire** : Si vous utilisez des suffixes (comme dans l'exemple ci-dessus), veillez à utiliser des noms courts, clairs et sans caractères spéciaux complexes afin d'éviter toute erreur de routage.

| 🚨**Avertissement** : Ne communiquez vos lignes d'annuaire spécifiques (vos adresses avec suffixes) à vos fournisseurs qu'une fois leur statut validé et activé sur la plateforme SUPER PDP.  Dans le cas contraire, vos partenaires ne pourront pas vous adresser leurs factures. |
| --- |

Mis a jour le : 16/07/2026
