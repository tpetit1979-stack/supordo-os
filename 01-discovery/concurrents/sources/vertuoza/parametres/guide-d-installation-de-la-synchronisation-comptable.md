---
source: https://intercom-help.eu/vertuoza/fr/articles/522539-guide-d-installation-de-la-synchronisation-comptable
categorie: Paramètres
titre: Guide d'installation de la synchronisation comptable
date_recuperation: 2026-09-05
---

# Guide d'installation de la synchronisation comptable

> ℹ️ Ce guide vous accompagne de A à Z. Vous n'aurez à le faire **qu'une seule fois**. Pensez à contacter votre **comptable** avant de démarrer. Et si vous bloquez à une étape, le support Vertuoza est là : [support@vertuoza.com](mailto:support@vertuoza.com)


Avant de démarrer, demandez à votre comptable :
- Les **codes TVA** pour chaque taux utilisé (0 %, 6 %, 21 %…)
- Les **numéros de comptes généraux** pour vos achats et ventes
- Les **codes des journaux comptables** (ventes, achats, notes de crédit)
> 💡 Votre Customer Success ou le support peuvent vous fournir la liste complète des codes disponibles dans votre logiciel. Votre comptable vous dira ensuite lesquels utiliser.

**ETAPES DE CONFIGURATION** 


Dans Vertuoza : Paramètres → Intégrations → Synchro comptable. Sélectionnez votre logiciel et cliquez sur Connecter.
[Vidéo]()

**Deux types de connexion :**
**Pour les logiciels accessible depuis un navigateur** (Exact, Odoo, Pennylane, Horus, etc).
La connexion est directe et immédiate :
1. Une fenêtre s'ouvre pour saisir vos identifiants ou ceux de votre comptable
2. Remplissez les champs demandés
3. Validez la connexion
> ✨ **Astuce** : Cliquez sur "**Comment se connecter**" pour obtenir de l'aide spécifique à votre logiciel.
> [Vidéo]()

**Pour les logiciels installés localement** (uniquement Bob 50, Sage 100, Winbooks Classic)
Un programme doit être installé sur le serveur ou l'ordinateur où se trouve votre logiciel comptable. Nous vous conseillons de prendre contact avec le support, afin qu'une personne de chez Vertuoza vous accompagne.

⚠️ **Important** :
- L'installation nécessite un accès administrateur au serveur
- Rapprochez-vous de votre comptable et/ou de votre informaticien
- L'opération prend environ 15 minutes
[Vidéo]()
> 📞 **Besoin d'assistance ?** N'hésitez surtout pas à contacter votre Customer Success ou le support Vertuoza. Ils vous guideront étape par étape pour une configuration sécurisée.


Une fois que la connexion est marquée comme **Active**, retournez dans Vertuoza :
1. Allez dans **Paramètres > Intégrations > Synchro comptable**
2. Cliquez sur **Modifier**
3. Suivez les différentes étapes ci-dessous
[Vidéo]()

Pour synchroniser les taux de TVA, vous devez **obligatoirement lier chaque taux de TVA utilisé dans Vertuoza** avec le code correspondant dans votre logiciel comptable.

**Comment procéder :**
1. Cliquez sur **Codes TVA**
2. Pour chaque taux de TVA que vous utilisez dans vos factures, cliquez sur **Éditer**
3. Renseignez le code TVA de votre logiciel comptable
4. Indiquer s'il s'agit d'une TVA de vente ou d'achat (ou les deux)
> ✨ **Astuce** : Les codes TVA sont disponibles dans votre logiciel comptable ou via la liste fournie par votre Customer Success / support.
> ⚠️ **Attention** : Si vous oubliez de lier un code TVA ou si vous indiquez le mauvais code, vous aurez une erreur lors des synchronisations.


[Vidéo]()



Définissez des comptes généraux par défaut dans vos paramètres. Votre comptable doit vous indiquer les comptes généraux à utiliser. Nos équipes peuvent également vous envoyer la liste de tous les comptes généraux.

**Comment procéder :**
1. Cliquez sur **Comptes généraux**
2. Ajoutez les comptes généraux que vous utilisez régulièrement dans vos factures
3. Liez ensuite ces comptes dans les paramètres de la configuration de la synchronisation

**Flexibilité de modification**
Vous conservez la possibilité de modifier le compte général facture par facture si nécessaire, directement depuis Vertuoza avant la synchronisation vers votre logiciel comptable.
> ✨ **Astuce : le compte "fourre-tout"**
> Si vous n'êtes pas sûr du compte à utiliser, demandez à votre comptable d'utiliser un **compte d'attente**. Toutes vos factures y seront centralisées, et il les réaffectera ensuite.

> ⚠️ **Attention** : Un compte qui n'existe pas dans votre logiciel comptable générera une erreur.



Indiquez le nom ou le code (dans le cas du logiciel Horus) du journal comptable tel qu'il apparaît dans votre logiciel comptable. Vous devez configurer les journaux pour les factures de vente, les factures d'achat et les notes de crédit.

> ✨ **Astuce** : Les codes des journaux comptables sont disponibles dans votre logiciel comptable ou via la liste fournie par votre Customer Success / support.

> ⚠️ **Attention** : Un mauvais journal générera une erreur lors de vos synchronisations.


Le plan analytique permet de suivre la rentabilité par chantier. Cochez simplement la case si vous utilisez un plan analytique dans votre comptabilité.

> ℹ️ **Disponibilité** : Le plan analytique n'est pas disponible sur tous les logiciels comptables. Il n'est notamment pas supporté sur : ACD, Eboekhouden, FreeAgent, Fulll, Netsuite, Pennylane, Sage Génération Experts, Tiime, Visma eAccounting, AFAS Software, Moneybird.

> Pour les logiciels **Horus** et **Exact**, vous devez renseigner un **ID associé à votre code analytique**. 
> ⚠️ Cet ID **n’est disponible que via nos équipes**.
> Il a ce format : 5e9b5f80-be8a-4014-828b-0bea4bbb4785.

> ⚠️ **Attention** : Si vous avez déjà des codes analytiques créés dans votre logiciel comptable pour des chantiers existants dans Vertuoza, vous devez obligatoirement indiquer l'identifiant de ce code analytique dans le champ "Identifiant comptable" de votre chantier (accessible depuis la gestion de chantier, dans l'édition du chantier sur l'onglet "Tableau de bord").




Si vos contacts existent déjà dans votre logiciel comptable, liez-les pour éviter les doublons.

Ouvrez la fiche d'un contact et renseignez le champ **identifiant comptable** (dans le 2e onglet). Vous pouvez aussi le faire en masse via un import de contacts. Nos équipes peuvent vous aider dans cette démarche !

**Si vous ne renseignez pas l'identifiant comptable :** Lors de la synchronisation, Vertuoza recherchera le client/fournisseur avec son nom. Si rien n'est trouvé, il sera créé automatiquement. Par la suite, ce même client/fournisseur sera réutilisé pour les prochaines factures.

> ✨ **Astuce** : Les identifiants sont disponibles dans votre logiciel comptable ou via la liste fournie par votre Customer Success / support.



Mode de regroupement des lignes de facture
Lors de la synchronisation de vos factures vers votre logiciel comptable, vous pouvez choisir le niveau de détail souhaité pour les lignes de facture :

- **Option "Regroupées" (recommandée)**
Les lignes de facture ayant le même compte général et le même taux de TVA sont fusionnées en une seule ligne dans le logiciel comptable.
*Exemple : Une facture de 5 lignes avec un seul compte général et une seule TVA sera transmise en 1 ligne unique. Si cette même facture comporte 2 taux de TVA différents, elle sera transmise en 2 lignes (une par taux de TVA).*
- **Option "Par ligne"**
Toutes les lignes de la facture sont transmises individuellement, conservant ainsi le détail complet de chaque article ou prestation.
*Exemple : Une facture de 5 lignes sera toujours transmise avec ses 5 lignes, quel que soit le compte général ou la TVA.*
> ✨ **Astuce :** Si vous hésitez, optez pour le mode **"Regroupées"**. Cette option simplifie la lecture des écritures comptables tout en conservant les informations essentielles (montant HT, TVA, compte général). Le détail complet reste consultable dans le PDF de la facture joint.

Statut des factures dans le logiciel comptable
Vous pouvez définir le statut par défaut des factures une fois synchronisées dans votre logiciel comptable :
- **Statut "Brouillon"**
Les factures arrivent en mode non-validées dans le logiciel, permettant  à votre comptable de les vérifier et de les modifier si nécessaire avant comptabilisation. Cette option nécessite cependant une action manuelle pour valider et comptabiliser chaque facture.
- **Statut "Comptabilisée"**
Les factures sont directement enregistrées et comptabilisées, sans intervention supplémentaire.

![](https://downloads.intercomcdn.eu/i/o/yr18hzl2/100253151/1452dc9e272cb823bd58c7a9c550/image.png?expires=1788620400&signature=ec431f1c9087338d8077f889550f16a6d58b7bbb3d4510dc7c890b1b9bfb82a4&req=0dVvx135rTIplxv889osp%2FXbmjUreYZ%2BSNdNcrja0HMz3D23mMmVHjVJWxwr%0AmcHjRUJ%2FS%2BRsHaXpJA%3D%3D%0A)


Prochaines étapes : 

➡️ [Synchroniser vos factures clients](https://intercom-help.eu/vertuoza/fr/articles/522564-envoyer-les-factures-vers-le-logiciel-comptable)

➡️ [Synchroniser vos factures fournisseurs](https://intercom-help.eu/vertuoza/fr/articles/522567-synchroniser-vos-factures-fournisseurs-bidirectionnel)

Mis a jour le : 04/06/2026
