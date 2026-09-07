---
url: https://documentation.openfire.fr/knowsystem/ecritures-comptables-et-pieces-comptables-275
url_finale: https://documentation.openfire.fr/knowsystem/ecritures-comptables-et-pieces-comptables-275
date_collecte: 2026-09-06
destination: documentation_2
---

OpenFire offre de nombreuses fonctionnalités pour aider les entreprises à gérer leur comptabilité soit :

- au niveau de l'automatisation des pièces comptables

- en saisissant directement les pièces comptables

- en important les pièces comptables

## Automatisation des pièces comptables

**Accès :** Comptabilité > Ventes/Achats > Factures / Paiements

              **Comptabilité > Conseiller > Pièces comptables**        

Openfire permet la génération automatique des pièces comptables. Ainsi, la validation des factures, avoirs et paiements dans la gestion des factures et paiements génère automatiquement une pièce comptable dans le journal associé.

Vous pouvez retrouver la pièce comptable liée à la facture :

Et l'écriture comptable liée au paiement :

Si vous souhaitez accéder à la pièce comptable du paiement à partir de la gestion des paiement, vous avez 2 solutions :

1- Il faut cliquer sur le smart button Ecritures comptables. Les lignes des écritures comptables s'affichent avec le numéro de la pièce comptable. Vous cliquez sur une des lignes des écritures comptables et cliquez sur le numéro de la pièce comptable.

2- Lorsque le paiement est lié à la facture, vous pouvez accéder à la pièce comptable en cliquant sur le sous le total de la facture et à gauche du paiement concerné. Une fenêtre s'ouvre et il faut cliquer sur OUVRIR LES PAIEMENTS.

Pour rappel, le paiement lié à la facture permet le lettrage automatique en comptabilité.

  Plus d'informations sur [le lettrage](https://documentation.openfire.fr/knowsystem/lettrage-comptable-192)

## Saisie pièces comptables et visualisation écritures comptables

Une pièce comptable comprend des écritures comptables regroupant ainsi les opérations comptables. Il peut s'agir d'une facture d'achat qui se trouvera dans le journal d'achat ,d'une facture de vente dans le journal de vente, d'une OD de paie dans le journal d'opérations diverses,...

Chaque pièce comptable comptabilisée est numérotée et enregistrée dans le logiciel.

**Saisie pièce comptable**

**Accès :** Comptabilité > Conseiller > Pièces Comptables.

   ->Astuce: Avant de créer la pièce comptable, vous pouvez sélectionner dans les filtres le journal afin qu'il se mettent directement au moment de la saisie de la pièce. 

Cliquer sur Créer.

Remplissez les champs requis :

 **1-** Nom du journal si celui-ci n'a pas été mis automatiquement

 **2**- date de la pièce comptable

 **3**- la Référence de la pièce comptable peut être un libellé explicite car il sera repris dans les lignes des écritures comptables de la pièce, colonne Libellé.

 **4**- le compte comptable : si dans le plan comptable, le compte a un compte de contrepartie, ce dernier se mettra directement dans la ligne suivante. Si le compte comptable a une taxe par défaut, ce dernier mettra le compte de taxe associé dans la ligne suivante.

 **5**- le partenaire est le lien avec le contact dans la gestion commerciale. Si le compte comptable est un compte de tiers, il est important de lier le compte avec le partenaire afin que le montant soit visible dans la partie facturation et / ou paiement.

Ajoutez les montants à débiter ou à créditer et lorsque la pièce comptable est équilibrée, il faut cliquer sur Comptabiliser.

L'action Sauvegarder permet d'enregistrer la pièce comptable mais elle reste en brouillon. Elle n'est pas comptabilisée. Elle est donc modifiable tant qu'elle n'est pas comptabilisée.

 ->Astuce: il est possible de dupliquer une pièce comptable qui revient tous les mois.

Il faut modifier en amont la pièce dupliqué et la comptabiliser.

*Consultations écritures comptables* 

Les écritures sont consultables depuis le menu **Comptabilité > Conseiller > Écritures Comptables** :

Un certain nombre de filtres prédéfinis sont disponibles vous permettant notamment d'obtenir

- les écritures du mois en cours, ou précédent,
- les écritures non comptabilisées,
- les écritures non lettrées, ...

## Import de pièces comptables

Openfire permet la création de pièces comptables via l'import d'un fichier Excel sur votre base.

Un certain nombre de champs sont obligatoires à l'importation, dont voici les significations:

- **journal_id :** contient le code du journal comptable a utiliser. Ce code est visible dans les journaux (menu**Comptabilité > Configuration > Journaux** ) et ne doit être renseignée que sur la première ligne de la pièce comptable.

- **ref :** il s'agit de la référence de la pièce comptable. La valeur de ce champ doit être unique par fichier et ne doit être renseignée que sur la première ligne de la pièce comptable.

- **date :**  Date de la pièce comptable. La date ne doit être renseignée que sur la première ligne de la pièce comptable.

- **line_ids/name :** Nom de l'écriture comptable, libellé

- **line_ids/account :** Numéro du compte comptable utilisé pour cette écriture

- **line_ids/debit :**  Montant au débit

- **line_ids/credit :** Montant au crédit

A Savoir: Il ne faut pas mettre de colonnes à zéro. Par exemple, si j'entre un montant au *débit*, la colonne *Crédit* doit être vide et inversement.

La première ligne d'une pièce comptable doit contenir le code du journal, la référence ainsi que la date de la pièce.

Les lignes suivantes ne devront alors pas contenir de valeurs pour ces différents champs afin que le logiciel comprenne qu'il s'agit d'écritures de la même pièce.

 Attention à ne pas mettre des formules dans les colonnes mais bien des valeurs. Si besoin il suffit bien souvent de faire un copier/collage valeur du tableau. 

Une fois le fichier prêt, vous pouvez l'importer depuis le menu **Comptabilité > Conseiller > Pièces Comptables**:

Après avoir sélectionné votre fichier, cliquez sur Valider.

Le Logiciel fera alors un test d'import et vous remontera les erreurs rencontrées s'il en existent :


Si aucune erreur n'est rencontrée, le message Tout semble correct apparaîtra. Vous pourrez alors importer votre fichier en cliquant sur le bouton Importer:

Exemple d'Import:

Dans l'exemple ci dessus, le logiciel va créer une pièce comptable nommé BANK 01/01/2023 FRAIS avec une écriture au débit sur le compte 627100 et une seconde écriture au crédit sur le compte 512001.

Le résultat de l'import de ce fichier donnera:

A Savoir : A la suite de l'import, les pièces comptables importées seront toujours en statut non comptabilisées.

## Blocage des Écritures

Les écritures comptables peuvent être bloquées pour les utilisateurs n'ayant pas les droits Conseiller.

Dans ce cas, le système ne permettra alors plus la modification des écritures antérieures à cette date.

  Plus d'informations sur [la clôture comptable](https://documentation.openfire.fr/knowsystem/cloturer-un-exercice-fiscal-124#scrollTop=0)