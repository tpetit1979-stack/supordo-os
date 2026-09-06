---
source: https://support.openfire.fr/hc/fr/articles/28201675219356-Autocompl%C3%A9ter-une-adresse-dans-une-fiche-Contact
categorie: Configurer OpenFire
titre: Autocompléter une adresse dans une fiche Contact
date_recuperation: 2026-09-05
---

# Autocompléter une adresse dans une fiche Contact

L'autocomplétion d'adresse vous permet de remplir automatiquement les champs **Rue**, **Code postal**, **Ville** et **Pays** lors de la création ou de la modification d'un contact. Cette fonctionnalité accélit la saisie et réduit les erreurs d'adressage.

Cet article contient les sections suivantes :

- [Prérequis](#h_01KV7JPXPKDFBWJYX06502FV96)
- [Activer l'autocomplétion d'adresse](#h_01KV59QSAXZKHW28VM3B95YK50)
- [Configurer le fournisseur](#h_01KV59QSAYYFR78PG1YP12HZGR)
- [Ajuster les paramètres de recherche](#h_01KV59QSB30JYARDQHVXGGQKB8)
- [Compléter les coordonnées GPS](#h_01KV59TMY7EH8D2BNF93F0ZYJR)
- [Utiliser l'autocomplétion dans une fiche contact](#h_01KV59TMY97PD5NW575DGC0H10)
- [Comprendre l'état de géolocalisation](#h_01KV59TMYDH88ZMCQECYZNMZH5)
- [Suivi des modifications dans le chatter](#h_01KV59VBNWP438MAN6BPVTTDE1)

Suivre le chemin d'accès suivant : **Contacts** > **Configuration** > **Paramètres de géolocalisation** > **Autocomplétion d'adresse**.

## Prérequis

Pour bénéficier de l'autocomplétion d'adresse, le module **of_address_autocomplete** doit être installé sur votre base de données. Pour vérifier si le module est installé :

1. Ouvrir l'application **Contacts**
2. Suivre le chemin d'accès suivant : **Contacts** > **Configuration** > **Paramètres de géolocalisation**
3. Si la section **Autocomplétion d'adresse** n'apparaît pas dans les paramètres, le module n'est pas installé

| 💡**Note **: Si le module n'est pas installé, le champ **Rue** se comporte comme un champ texte standard et aucune suggestion d'adresse ne sera proposée. Veuillez contacter l'équipe support OpenFire pour en demander l'installation. |
| --- |

## Activer l'autocomplétion d'adresse

1. Ouvrir les paramètres de géolocalisation
2. Cocher la case **Activer l'autocomplétion d'adresse**
3. Une fois activée, les options de configuration supplémentaires apparaissent

### Configurer le fournisseur d'autocomplétion

Le fournisseur est le service qui propose les suggestions d'adresses. Plusieurs fournisseurs sont disponibles :

- **BAN / Géoplateforme** : service gratuit, couvre uniquement la France
- **MapBox** : service mondial, nécessite une clé API dédiée
- **Photon (Komoot / OSM)** : service gratuit, couverture mondiale

| 💡**Note **: Le fournisseur d'autocomplétion peut être différent de celui utilisé pour le géocodage standard. Pour MapBox, saisir votre clé API dans le champ **Clé API MapBox** qui apparaît lorsque ce fournisseur est sélectionné. |
| --- |

### Ajuster les paramètres de recherche

Deux paramètres permettent de contrôler le comportement de l'autocomplétion :

- **Nombre minimum de caractères** : nombre de caractères à saisir avant que les suggestions n'apparaissent (minimum : 3, défaut : 3)
- **Nombre maximum de résultats** : nombre de suggestions affichées dans la liste déroulante (défaut : 10)

| 💡**Note **: Un nombre minimum de caractères trop faible peut saturer le fournisseur avec des requêtes trop courtes. La valeur minimale autorisée est de 3. |
| --- |

### Compléter les coordonnées GPS

| 🚨**Avertissement** : Cette option nécessite que le fournisseur choisi retourne des coordonnées précises. Pour MapBox, un appel supplémentaire est effectué à la sélection de l'adresse. |
| --- |

1. Cocher la case **Remplir les coordonnées de géolocalisation**
2. Lors de la sélection d'une suggestion, les champs **Latitude**, **Longitude**, **État de géolocalisation** et **Précision** sont automatiquement renseignés

## Utiliser l'autocomplétion dans une fiche contact

Suivre le chemin d'accès suivant : **Contacts** > **Contacts** > **Nouveau** (ou ouvrir un contact existant).

1. Saisir l'adresse dans le champ **Rue**
2. Après avoir atteint le nombre minimum de caractères configuré, une liste de suggestions apparaît
3. Sélectionner l'adresse correspondante dans la liste
4. Les champs **Rue**, **Code postal**, **Ville** et **Pays** sont automatiquement remplis

| **🧑‍🏫Exemple** : En saisissant "15 rue de la Pa", la suggestion "15 Rue de la Paix, 75002 Paris, France" apparaît. En la sélectionnant, tous les champs d'adresse sont complétés instantanément. Si vous modifiez manuellement la rue après avoir sélectionné une suggestion, le système conserve l'état **Autocomplétion** et ne déclenche pas de géocodage automatique. |
| --- |

## Comprendre l'état de géolocalisation

Le champ **État de géolocalisation** sur la fiche contact indique comment les coordonnées GPS ont été obtenues :

- **Autocomplétion** : l'adresse a été posée via le widget d'autocomplétion
- **Manuel** : les coordonnées ont été saisies ou modifiées manuellement
- **Géocodé** : les coordonnées ont été calculées automatiquement par le service de géolocalisation

Lorsqu'une adresse est posée par autocomplétion, les modifications ultérieures sur le contact ne basculent pas l'état vers **Manuel** et ne déclenchent pas de géocodage automatique.

## Suivi des modifications dans le chatter

Le chatter (fil de discussion en bas de la fiche contact) trace automatiquement les actions d'autocomplétion :

- **Adresse autocomplétée** : un message simple indique le fournisseur utilisé et l'adresse retenue
- **Adresse corrigée manuellement** : si vous modifiez la rue après avoir sélectionné une suggestion, un message affiche la valeur d'origine et la valeur corrigée

## Bonnes pratiques

- **Avant un import massif de contacts** : désactiver l'option de géocodage automatique dans les paramètres pour éviter de saturer le fournisseur
- **Pour la France** : privilégier le fournisseur BAN/Géoplateforme, gratuit et optimisé pour les adresses françaises
- **Pour une couverture internationale** : utiliser MapBox ou Photon selon vos besoins
- **Vérifier les suggestions** : toujours contrôler l'adresse proposée avant de la valider, surtout pour les adresses atypiques

Mis a jour le : 16/06/2026
