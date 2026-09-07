---
url: https://documentation.openfire.fr/knowsystem/menu-de-la-comptabilite-et-tableau-de-bord-174
url_finale: https://documentation.openfire.fr/knowsystem/menu-de-la-comptabilite-et-tableau-de-bord-174
date_collecte: 2026-09-06
destination: documentation_2
---

OpenFire offre de nombreuses fonctionnalités comptables. OpenFire étant un ERP ou PGI (Progiciel de gestion intégré), la comptabilité est générée automatiquement à partir des actions établies dans les autres modules d'OpenFire, telles que la gestion des facturations, la gestion des paiements et la gestion des stocks.

L'intégration avec les autres modules pour générer des écritures automatiquement se fait grâce à une configuration dans le module de la comptabilité :

- Par exemple, à la création d'un contact client ou fournisseur, le compte de tiers sera créé automatiquement dans le contact au moment de la validation d'un paiement ou d'une facture.
- De plus, le compte de revenu ou de charge est défini dans la catégorie de l'article et dans la configuration de la taxe. Les factures clients et fournisseurs validées sont ainsi directement générées sous forme de pièces comptables dans les journaux associés avec le bon compte comptable.

OpenFire permet également de gérer plusieurs sociétés dans un seul système.

## Les Menus de la comptabilité

Le tableau de bord de la comptabilité vous permet de suivre rapidement les informations clés de votre comptabilité par journal. Vous pouvez suivre vos factures clients et fournisseurs directement par le tableau de bord ainsi que les paiements en rapprochant avec votre relevé bancaire. (*Plus d'explications dans le chapitre suivant*)

Le menu Ventes donne accès aux factures et avoirs clients, aux factures boutiques, aux paiements clients, aux remises en banque, aux prélèvements SEPA/LCR clients, à la base clients et aux articles en ventes.

Le menu Achats vous permettent d'accéder aux factures d'achats fournisseurs, aux paiements effectués à vos fournisseurs, à la base fournisseur et aux articles pouvant être achetés.

Le menu Conseiller permet de retrouver les éléments nécessaires au travail au quotidien du comptable :

- Les écritures comptables,
- Les pièces comptables
- Le plan comptable
- Les rapprochements bancaires
- Le lettrage (Correspondance des paiements manuels et des factures)
- Les comptes analytiques et écritures analytiques

Le menu Rapports permet d'éditer les documents comptables officiels et des rapports plus personnalisés : FEC, Analyse CA détaillée, Balance, Grand livre, Balance âgée des tiers, Rapport MIS (déclaration TVA ,bilan, compte de résultat,....), DEB,...

Le menu Paiements permet de générer des fichiers de paiements pour les banques.

Le menu Immobilisations permet de gérer le parc d'immobilisations (gestion des acquisitions, des amortissements, des cessions, génération des écritures comptables et rapports).

## Le Tableau de bord

En vous rendant dans le menu **Comptabilité**, vous accédez tout d'abord au tableau de bord. 

Le tableau de bord vous permet de voir l'ensemble des journaux comptables en lien avec l’exploitation : ventes, achat, banque, caisse, … et vous permet de gérer le suivi sans avoir besoin d'accéder aux écritures comptables.

La liste des journaux se trouve dans le menu Comptabilité>Configuration > Journaux

## Ventes et Achats

Pour les journaux de Ventes et Achats, vous avez accès directement :

  **1** - A toutes les factures et avoirs quelques soient leur état (Brouillon, Proforma, Annulée, Ouverte ou Payée) : c'est le raccourci de l'accès aux factures via Comptabilité>Ventes ou Achats>Factures

  **2** - Aux factures et avoirs en état Brouillon ou Proforma.

  3 - Aux factures et avoirs validés en état Ouverte et donc non réglés.

**Nouvelle**Facture ou Avoir disponible pour chaque journal lié à l'exploitation (Ventes, achat).

## Caisse

Pour le journal de Caisse, vous pouvez suivre du tableau de bord les mouvements d'espèce. Il s’agit d’un suivi de relevé de caisse. Au fur et à mesure que vous saisissez les paiements espèce dans le logiciel, vous pourrez les rapprocher (lettrer) avec les montants saisis dans le relevé.

Pour la saisie des paiements :

  Allez à l'article  __Paiements__

1 - Caisse : permet d'accéder à la liste des transactions de la caisse et de créer de nouvelles transactions. Toutes les transactions de caisse sont à saisir.

2 - Le solde en GL (Grand Livre) correspond au solde du compte comptable de la caisse associé au journal de Caisse. Si vous ne gérez pas la comptabilité dans OpenFire, il ne faut pas tenir compte de ce montant. Si vous gérez la comptabilité, le solde en GL qui est le solde du compte de caisse doit correspondre au montant du dernier relevé.

3 - Dernier relevé : solde du fond de caisse qui doit correspondre au fond de caisse réel.

4 - Lettrer éléments : permet de rapprocher les lignes saisies dans le relevé de caisse avec les paiements clients et fournisseurs enregistrés en mode de paiement espèce.

 5 - L'option Plus permet d'accéder à plus d'actions : vous pouvez créer directement un paiement client (Règlement entrant) ou un paiement fournisseur (Règlement sortant). Ces paiements apparaîtront dans le menu **Comptabilité>Ventes ou Achats>Paiements**.

 SI vous souhaitez gérer votre fond de caisse via le tableau de bord, au démarrage, il faut cliquer sur ***Nouvelles transactions*** ou **Caisse>Créer** et saisir le fond de caisse dans le Solde Initial avant de saisir les transactions :

1.   : La référence doit être explicite : nous vous conseillons de mettre la journée de la saisie de la caisse.

2.  :
il s’agit du journal comptable dans lequel il faut saisir : il faut
toujours laisser le journal concerné, soit la Caisse.

3.   il s’agit de la date de l’opération de
mouvement de la caisse.

4.  Il
s’agit du solde initial. A la 1<sup>ère</sup> saisie, le montant sera
obligatoirement de 0€. Vous pouvez donc saisir le montant de votre caisse directement dans le champs ou en cliquant sur compter.

5.   Vous pouvez saisir le détail de votre monnaie en cliquant sur compter. Une fenêtre apparaît pour indiquer le détail de la monnaie et vous cliquez sur confirmer après avoir vérifié le montant.

6.   Vous notez ensuite les opérations de mouvement d’espèce de la journée. S'il s’agit d’un paiement fournisseur par espèce et donc une sortie d’argent. Le montant sera négatif.

7.   Vous notez les opérations de mouvement d’espèce de la journée. S'il s’agit d’un paiement client par espèce et donc une entrée d’argent. Le montant sera positif.

8.   Solde calculé est un champ calculé = solde initial + ou – les transactions de la journée. Il doit correspondre au solde final.

9.   Vous notez dans ce champs le solde final. Il s’agit du montant de la caisse que vous avez en fin de journée. Il doit correspondre au montant indiqué dans le solde calculé? Il est possible de mettre le détail de la monnaie en cliquant sur Compter.


Le solde final sera ainsi noté sur le tableau de bord de caisse dans le champ Dernier relevé. L’état de l’opération sera en **Nouveau**. Vous ne pouvez
lettrer que si vous effectuez les paiements dans OpenFire. 

Une transaction est validée que si celle-ci est lettrée avec un paiement validé et donc une pièce comptable confirmée.

10. Quand la journée est saisie, vous sauvegardez et afin de valider la caisse, il faut lettrer les opérations de caisse avec les paiements. Le compte comptable doit être le même pour lettrage.
S'il n'existe pas de ligne de contrepartie, il faut créer le paiement espèce manquant.

Si tout est lettré, la transaction peut-être validée et le suivi de la caisse de la journée est terminée. Vous retrouvez les pièces comptables associées aux transactions saisies dans le smart button.

## Banque

Pour le journal de Banque, vous pouvez suivre du tableau de bord les mouvements de votre relevé bancaire. Au fur et à mesure que vous saisissez les paiements dans le logiciel, vous pourrez les rapprocher (lettrer) avec les montants saisis ou importés dans le relevé. 

 Le suivi de la banque via le tableau de bord nécessite le suivi de toute la comptabilité dans le logiciel et le fonctionnement est le même que pour le journal de caisse.

Pour plus de renseignements, contacter le support.

## Particularités d'OpenFire

__Journaux:__ Du fait de l'intégration avec les autres modules, OpenFire crée automatiquement les pièces comptables dans les journaux pour chacune de vos opérations : validation factures, enregistrement d'un paiement, etc...

Toutes les opérations comptables dans les journaux sont automatiquement équilibrées (somme des débits = somme des crédits).

__Report A Nouveaux:__

Sur de nombreux logiciels de comptabilité, lorsque l'on clôture son exercice, on a un report des A nouveaux. Le principe est que tous les comptes de 1 à 5 sont lettrés à la fin de l'exercice et le logiciel va alors générer de nouvelles écritures au 1er jour du nouvel exercice.


 A Savoir: Sur OpenFire, le report a nouveau laisse ouvert les écritures de classe 1 à 5 ainsi que les écritures non lettrées des comptes auxiliaires (401-411). Cela découle du fait qu'OpenFire intègre aussi la gestion commerciale. En effet, si le logiciel clôturait les comptes 411 et 401, le logiciel croirait que les factures sont payées.

OpenFire va cependant générer un report à nouveau lors de l'édition d'un rapport en prenant toutes les écritures non lettrées à la date de fin d'exercice, et va les regrouper ensemble à la date du début d'exercice et les lettrer entre elles.*Le journal A nouveau est consultable via le fichier FEC, ou en éditant les rapports comptables.*

A Savoir: Avant de clôturer un exercice fiscal, il faut d'abord vérifier les données de la balance et le résultat qui se trouvera dans le compte 999999.

En effet, sur OpenFire le résultat est affecté au compte 999999 Profits/pertes non distribués.

Lors de la réaffectation de compte, le cabinet comptable choisira alors s'il souhaite passer une écriture vers le compte de bénéfice (120) ou de perte (129).

  Plus d'information sur [le rapport FEC](https://documentation.openfire.fr/knowsystem/rapport-comptable-fec-213)