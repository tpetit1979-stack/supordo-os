---
url: https://documentation.openfire.fr/knowsystem/conditions-de-reglement-156
url_finale: https://documentation.openfire.fr/knowsystem/conditions-de-reglement-156
date_collecte: 2026-09-06
destination: documentation_2
---

Les conditions de règlement permettent de définir un échéancier prévisionnel de facturation et d’encaissement dans le cadre du projet, principalement pour garantir que les clients paient leurs factures correctement et à temps.

Ces conditions peuvent être appliquées aux commandes clients, aux factures clients, aux factures fournisseurs et aux contacts.

## Paramétrer vos conditions de règlement


Rendez-vous dans **Comptabilité > Configuration > Conditions de règlement** et cliquez sur Créer .

Une condition de règlement est définie par les éléments suivants :

- Conditions de règlement : nom de la condition
- Actif : vrai/faux. Permet d'activer ou non cette condition de règlement
- Description sur les factures: le texte saisi dans ce champ sera repris automatiquement sur les factures .
- Délais : cette partie sert à définir les différentes échéances.

Dans la section Délais, vous pouvez ajouter un ensemble de règles, appelées conditions, pour définir ce qui doit être payé et à quelle date d’échéance.

Pour ajouter un terme, cliquez sur Ajouter une ligne et définissez son Type, Valeur et Calcul de la date d’échéance.

**Définir une échéance :** 

__Type d’échéance :__ 

- Pourcentage,
- Balance (solde dû),
- Montant fixe,
- Valeur de l’échéance en % (ou en €)

Lorsque vous cliquez sur le type d'échéance, une fenêtre s'affiche.

Vous pouvez y définir l'arrondi du montant:

__Calcul de la date d'échéance:__ 

- Nombre de jours après la date de la commande ou de facturation,
- Nombre de jours après la dernière échéance,
- Nombre de jours après expiration du mois de facturation,
- Dernier jour du mois suivant,
- Dernier jour du mois en cours.

Dans l'exemple suivant, 30 % sont dus le jour de l'émission de la facture et le solde est dû à la fin du mois suivant.

Attention: Les conditions de paiement ne doivent pas être confondues avec les factures d'acompte. Si, pour une commande spécifique, vous émettez plusieurs factures à votre client, il ne s'agit ni d'un délai de paiement ni d'un échéancier, mais d'une politique de facturation.

  Plus d'information sur le paramétrage de la __[Politique de facturation](https://documentation.openfire.fr/knowsystem/politique-de-facturation-141)__ 


### Configuration complémentaire

Il est possible de faire apparaitre les conditions de règlements sur la facture. Pour cela, rendez-vous dans le menu Ventes > Configuration > Configuration, dans la partie Taxe et facturation :

## Utiliser les conditions de règlements

Les conditions de règlement peuvent être définies dans vos Devis et vos factures via la liste déroulante dédiée:

Le choix d'une condition de règlement sur un devis fera alors apparaitre un échéancier prévisionnel en bas de la page.

Cet échéancier est modifiable par simple clic:

Par exemple ici, le montant de la première échéance est calculé à 1671€, mais je peux le modifier à 1700€.

Il faudra alors cliquer sur le bouton Mise à jour pour que l'échéancier se recalcule selon le montant que vous aurez modifié:

Les conditions de règlements peuvent également être appliquées directement à un contact dans l'onglet Comptabilité :