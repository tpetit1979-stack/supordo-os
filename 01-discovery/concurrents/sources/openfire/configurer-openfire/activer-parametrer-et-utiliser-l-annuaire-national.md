---
source: https://support.openfire.fr/hc/fr/articles/28949845181980-Activer-param%C3%A9trer-et-utiliser-l-annuaire-national
categorie: Configurer OpenFire
titre: Activer, paramétrer et utiliser l'annuaire national
date_recuperation: 2026-09-05
---

# Activer, paramétrer et utiliser l'annuaire national

Cet article vous explique comment activer et exploiter l'annuaire national au sein de votre logiciel OpenFire. Cet outil essentiel permet de maintenir à jour les informations légales de vos partenaires commerciaux (clients et fournisseurs) afin d'assurer la bonne transmission de vos factures électroniques.

Cet article contient les sections suivantes :

- [Section 1 : Activation et paramétrage de l'annuaire](#h_01KXNBD4ABMD62968Z49NN63A6)
- [Section 2 : Consultation globale des lignes de l'annuaire](#h_01KXNCHCA23GRQHCBXPF17931J)
- [Section 3 : Gestion de l'annuaire depuis une fiche contact](#h_01KXNDB0XDQWKG7XB47XYT2PZE)
- [Bonnes pratiques](#h_01KXNDDVFT573NQ2Y9HNYR5X28)

##

##

## Section 1 : Activation et paramétrage de l'Annuaire

L'annuaire permet à OpenFire de synchroniser et de récupérer automatiquement les informations légales de vos partenaires (clients professionnels et fournisseurs) depuis l'annuaire public de l'État.

Suivre le chemin d'accès suivant : Comptabilité > Configuration > Paramètres

Repérer et cocher la case **Annuaire** sous l'onglet de facturation électronique (ce paramètre est commun à toutes les sociétés de votre base OpenFire).

![](https://support.openfire.fr/hc/article_attachments/29403962785436)

Configurer vos règles de synchronisation automatique :

- **Synchronisation de l'annuaire du partenaire si la dernière synchronisation remonte à plus de** : indiquez le nombre de jours souhaité (conseillé : **30 jours**).
- **Synchronisation de l'annuaire d'un partenaire privé inactif si la dernière synchronisation remonte à plus de** : indiquez le nombre de jours souhaité (conseillé : **5 jours**, afin de détecter rapidement l'activation future de leur adresse de facturation).

Cliquer sur le bouton **Enregistrer** pour valider vos options.

| 💡**Note **: Vous pouvez à tout moment lancer manuellement la synchronisation des données de l'annuaire d'un client ou d'un fournisseur directement depuis sa fiche contact individuelle. |
| --- |

##

## Section 2 : Consultation de l'annuaire

Suivre le chemin d'accès suivant : Comptabilité > Configuration > Facturation électronique en France > Lignes de l'annuaire.

Cette vue vous permet de visualiser, sous forme de liste, l'ensemble des lignes d'annuaire rattachées aux partenaires présents dans votre carnet d'adresses.

![](https://support.openfire.fr/hc/article_attachments/28949845173404)

| 💡**Note **: Cette liste est uniquement consultative. Elle vous offre une vue d'ensemble rapide de l'état de synchronisation de tous vos contacts. |
| --- |

## Section 3 : Gestion de l'annuaire depuis une fiche contact

Vous pouvez consulter et forcer la mise à jour des données d'annuaire de vos clients ou fournisseurs directement depuis leur fiche individuelle.

Suivre le chemin d'accès suivant : Contacts > Sélectionner un partenaire > Onglet Ventes & Achats

![](https://support.openfire.fr/hc/article_attachments/28949845174812)

Dans cet onglet, plusieurs informations issues de l'annuaire sont affichées :

- Le statut de l'annuaire (tel que défini par la norme AFNOR).
- Le nom de l'entité juridique dans l'annuaire et son numéro SIREN.
- La date de la dernière synchronisation réussie pour ce compte.

Pour actualiser manuellement les données ou gérer des adresses multiples, vous pouvez réaliser les actions suivantes :

- Cliquer sur le bouton **SYNCHRONISATION DE L'ANNUAIRE** pour forcer la mise à jour immédiate des informations (très utile lors de la création d'un nouveau contact).
- Sélectionner la ligne adéquate dans le champ **Ligne d'annuaire par défaut** si votre contact dispose de plusieurs adresses de facturation.
- Cliquer sur le bouton intelligent (smart button) **Lignes actives de l'annuaire** situé en haut de la fiche pour consulter le détail des lignes du partenaire.

| 🚨**Avertissement** : Si vous ne forcez pas la synchronisation lors de la création d'une fiche contact, la mise à jour se fera tout de même automatiquement, mais de façon différée selon les règles (par exemple 5 ou 30 jours) définies dans vos paramètres globaux. |
| --- |

## Bonnes pratiques

**Cartographier les contacts multi-adresses :** Si un client ou un fournisseur dispose de plusieurs lignes d'annuaire (plusieurs adresses de facturation possibles), nous vous recommandons de créer autant de sous-contacts rattachés à la fiche principale que de lignes d'annuaire existantes. Cela vous permet d'associer la bonne adresse de routage pour chaque situation d'achat ou de vente.

| **🧑‍🏫Exemple** : Votre client possède un siège social et une antenne régionale qui gèrent leur facturation séparément. Créez un sous-contact "Siège" et un sous-contact "Antenne", puis attribuez à chacun sa ligne d'annuaire spécifique dans l'onglet Ventes & Achats. |
| --- |

Mis a jour le : 05/08/2026
