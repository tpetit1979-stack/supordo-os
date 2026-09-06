---
source: https://support.openfire.fr/hc/fr/articles/29497302472604-Associer-une-adresse-d-annuaire-%C3%A0-un-journal-d-achats-pour-la-facturation-%C3%A9lectronique
categorie: Configurer OpenFire
titre: Associer une adresse d'annuaire à un journal d'achats pour la facturation électronique
date_recuperation: 2026-09-05
---

# Associer une adresse d'annuaire à un journal d'achats pour la facturation électronique

Dans le cadre de la facturation électronique, vous pouvez attribuer une adresse d'annuaire spécifique à l'un de vos journaux d'achats. Cela vous permet d'orienter automatiquement l'importation de vos factures fournisseurs vers le bon journal comptable en fonction de leur nature.

Cet article contient les sections suivantes :

- [À quoi sert l'association d'une adresse d'annuaire à un journal ?](#h_01KZPF1P82BFFF7B0T8F69FQGW)
- [Prérequis](#h_01KZPF1P8525ZZSMRGMNDRYS4J)
- [Chemin d'accès](#h_01KZPF1P86NJPE0YSHGAW7VVYZ)
- [Étapes de configuration](#h_01KZPF1P87HPKDQTKWV56KGPYC)
- [Bonnes pratiques](#h_01KZPF1P8C95NR3XCBEX4003XA)

## À quoi sert l'association d'une adresse d'annuaire à un journal ?

L'association d'une ligne d'annuaire à un journal d'achats vous permet de séparer automatiquement le traitement de vos factures dès leur réception.

🧑‍🏫Exemple : Vous pouvez associer une adresse d'annuaire dédiée pour vos frais généraux (ex : `SIREN_FRAISGENERAUX`) à votre journal de frais généraux, et une autre adresse pour vos achats de matériel (ex : `SIREN_ACHATEXPLOITATION`) à votre journal d'achats d'exploitation. 
Les factures reçues seront directement dirigées vers le journal approprié.

## Prérequis

Pour effectuer ce paramétrage, vous devez avoir préalablement créé plusieurs lignes d'annuaire distinctes pour votre entreprise.

## Chemin d'accès

Suivre le chemin d'accès suivant : Application > **Comptabilité** > **Configuration** > **Journaux**.

## Étapes de configuration

Pour lier une adresse d'annuaire à un journal d'achats spécifique :

1. Sélectionner le journal d'achats à configurer dans la liste.
2. Cliquer sur l'onglet **Paramètres avancés**.
3. Renseigner la ligne d'annuaire souhaitée dans le champ dédié.
4. Cliquer sur le bouton **Enregistrer**.

![](https://support.openfire.fr/hc/article_attachments/29507158835228)

💡Note : Plusieurs lignes d'annuaire peuvent être associées à un même journal d'achats. Si vous souhaitez attribuer d'autres adresses à d'autres journaux, répétez simplement la procédure pour chacun d'eux.

💡Note : Répétez cette procédure pour chaque journal d'achats devant être relié à une ligne d'annuaire particulière.

## Bonnes pratiques

- **Informer vos fournisseurs** : Prévenez l'ensemble de vos fournisseurs des différentes lignes d'annuaire créées pour votre entreprise ainsi que de leur usage respectif (par exemple, en leur indiquant quelle adresse utiliser selon le type de prestation ou de fourniture).
- **Vérification préalable** : Assurez-vous que l'ensemble de vos adresses d'annuaire sont enregistrées et actives avant de finaliser la configuration des journaux.
- **Sensibilisation interne** : Informez vos équipes comptables du découpage mis en place afin d'assurer un suivi cohérent des flux d'achat.

🚨Avertissement : Si aucun journal spécifique n'est relié à une ligne d'annuaire, les factures importées seront attribuées au journal d'achats défini par défaut dans votre logiciel.

Mis a jour le : 25/08/2026
