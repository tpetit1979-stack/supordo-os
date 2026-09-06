---
source: https://help.sellsy.com/fr/articles/10516138-connecteur-multi-entites-de-facturation
categorie: Documents de vente 
titre: Connecteur Multi-entités de Facturation
date_recuperation: 2026-09-05
---

# Connecteur Multi-entités de Facturation

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2195249292/045905f6648daf4f68da133314c9/FAQ-Bannie%CC%80reAcademy-2+%282%29.png?expires=1788635700&signature=50926909690983603a4dd1d4d013a159018a8d56ceb17565e28bd5ea627065b7&req=diEuE8t6lINWW%2FMW1HO4zU4w0aGz1e92eBbxc5BMGX7j5jZODsA9Jg1d7HcM%0A5I0Id6NWW7RCMWfniSs%3D%0A)

Le connecteur multi-entités de facturation permet de gérer un compte CRM unifié qui centralise la gestion des informations clients, prospects, contacts, devis et catalogue, tout en permettant la facturation depuis plusieurs entités. Cette solution est idéale pour les groupes d'entreprises ou de filiales, souhaitant mutualiser leur gestion commerciale et leur marketing. 

___________________________________________________________

### **Mise en place du connecteur**

Une configuration spécifique de vos différents comptes est à mettre en place par nos équipes : 

- Plan Evolution minimum sur le compte CRM maître (la nécessité d’un plan spécifique pour vos comptes facturation enfants dépendra des fonctionnalités nécessaires pour votre usage)
- Configuration initiale par l'équipe Services Sellsy (prévoir un forfait de prestation de paramétrage et d’accompagnement)

> **Attention : **La génération d’un token API est nécessaire pour l’activation du connecteur, attention à ne pas modifier/supprimer le compte ou l'adresse email utilisateur qui est utilisé pour la génération de ce token, sinon le connecteur sera désactivé.

- Paramètres de facturation homogènes entre les comptes

> **Attention :  **Les comptes maître et enfants doivent avoir les mêmes paramètres de TVA (soit encaissement, soit débit).

___________________________________________________________

### **Utilisation du connecteur** 

**Création d'un devis dans le compte maître **

Créez votre devis en sélectionnant votre modèle si vous en avez créé préalablement. Tant que le devis est en statut *“Brouillon” *vous pouvez le modifier pour correspondre à vos besoins.

Ensuite, sélectionnez la bonne entité de facturation via le champ personnalisé *"Synchroniser vers le compte enfant" *disponible en bas de votre éditeur de devis, dans l'onglet *“Modifier les préférences du document"* , *"Champs personnalisé”* :

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/1368039699/e88e26a4fe9a52890646407e424e/AD_4nXdQAdSJlBRqBdHp9pWrPl-gvh-fe0GUBur5pyDXh4S9-PFTun8zjvEy3P8CKLZUKHKsVQ7oNTxkVibGjDy0THqoO3pOxr_rbVIy_hLci1jqbVg08bFJE3XcPUoGywZ3QwNLLurf7A?expires=1788635700&signature=379d3c893d174157e01837e9c82a0600ffaf5437245b0bd26b1edc463711374c&req=dSMhHsl9lIdWUPMW1HO4zRYsAPBK5P361ZmweV0b%2Fmhru6lcK4k%2BRP1APuy2%0Aj9bkbq%2Bk6QX2WIN1CpU%3D%0A)

Enfin, validez le devis manuellement ou via signature électronique par le client.

> **Attention : **Le passage du devis en statut accepté doit être** la dernière action à effectuer**, car c’est celle-ci qui déclenche l’envoi sur le compte enfant. Toute modification du devis ultérieure au passage en statut accepté ne sera pas envoyée au compte enfant.

> **Bon à savoir : **Si une modification de contenu doit être apportée après le passage en statut accepté, il faudra dupliquer le devis maître, le modifier, choisir de nouveau le bon compte enfant et le basculer en statut *“Accepté”*.

** **

**Synchronisation automatique unidirectionnelle avec les comptes enfants **

Lors du paramétrage avec nos équipes, vous pourrez choisir le type de document de vente que vous souhaitez créer sur le(s) compte(s) enfant(s) :

- duplication du devis en statut accepté sur le compte facturation enfant choisi
- et/ou création d’un bon de commande, d’un bon de livraison ou d’une facture en statut brouillon, accepté(e) ou finalisé(e) sur le compte facturation choisi (le choix du type de document créé et de leur statut sera définitif et unique pour tous vos documents)

> **Bon à savoir :  **Un seul document de chaque type sera créé automatiquement via le connecteur. Mais si vous réalisez plusieurs factures pour un devis (facturation partielle, facturation d'avancement, etc..), un paramétrage vous permettra de remonter dans le compte maître les liens publics de ces factures additionnelles créées par vos soins sur les comptes *enfants* (qui devront être reliées au devis dupliqué).

Ainsi, suite au passage du devis maître en statut *“Accepté”,* il faudra compter un délai incompressible d’environ **5 minutes** pour la synchronisation.

Une fois ce délai passé, sont ensuite créés dans le compte enfant choisi :

- les coordonnées clients/prospects/contacts + les produits/services (si non existantes)
- le(s) document(s) de vente choisi(s) lors du paramétrage du connecteur avec :
- Le nom du propriétaire du devis maître sous la forme d’un smart tag
- Un commentaire dans l’onglet *“Commentaires”* avec un lien public permettant la visualisation du devis maître

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/1368051867/6547c1b16bfa17f445e74d818ffe/AD_4nXeNDfdv9d7KeeR6UeAA4rsPIUPZR7UQSl2RQwbb1trzBZsXpnPPkh-uNJMa0gjSr8jVlNlr6NSJdSr4iGVqgf9WaMRZX4OXZZr6PyuHrto2q19qxhwHFZJtNRZyNKJSDAhMaYI3hQ?expires=1788635700&signature=42b1035255caac6d723d048173e9409e6a878001450718f86c9709b7ada0e672&req=dSMhHsl7nIlZXvMW1HO4zR11GVvx%2B0cfPTGPX3QRfk%2BFa0QA8gWeuJ0LsGAA%0AXPHN%2BGzxniA5LHPS2j0%3D%0A)

> **Bon à savoir : ** La synchronisation des données est unidirectionnelle, soit uniquement du compte CRM *"maître"* vers les comptes Facturation* "enfants",* garantissant la cohérence des données.

> **Attention : **Si vous choisissez de faire également de la facturation sur votre compte maître, il n’y aura pas de synchronisation des documents devant être facturés sur le compte maître. La synchronisation automatique n’est opérée que dans le cas du choix d’un transfert vers un compte facturation *"enfant".*

**Remontée d’informations sur le compte maître**

Une notification apparaît sur le fil d’activité de la fiche société et un commentaire s’ajoute sur le devis du compte maître dans l'onglet *“Commentaires” *pour : 

- confirmer la synchronisation réussie ou l’éventuelle erreur de synchronisation en précisant la raison
- mettre à disposition le lien public permettant de visualiser le ou les documents créés via le connecteur sur le compte enfant et leur statut

> **Attention : ** Tant que ces nouveaux documents seront en statut *“brouillon”* sur le compte enfant, le lien public sera présent sur le compte maître, mais le document ne sera pas encore accessible

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/1368057227/c54c3fcb668e7da66dc85b0a16a8/AD_4nXcoWcrNux0B3XX0MggDpfi1HbkIyy8umzmOW_u0gr0CxTEGjM_otUcRAmVbgWk_ynnSJ1LsvMTGCByX2kQ3d3Ih3Ey7UlJeMB3NR35R0SA6N9oXXKPvba5zgS4DY3-DfNAIX0Xe?expires=1788635700&signature=e6b721d932f268385c88f5198d6f7e4420140475da85625822c689418ffef49a&req=dSMhHsl7moNdXvMW1HO4zTio0VvmkIrutPXxlqTmK%2F5xA%2BpqoDx3edT1l0q7%0Amo3%2BYfz5%2BvgkEQX4yK8%3D%0A)

___________________________________________________________

### **Limitations du connecteur **

Limitations fonctionnelles de la version actuelle du connecteur :

- Les exceptions tarifaires ne sont pas synchronisées sur le catalogue des comptes enfants.
- La synchronisation et gestion des stocks ne sont pas disponibles.
- Seuls les champs personnalisés liés aux documents seront synchronisés, et ils doivent avoir les mêmes codes et valeurs entre les comptes maître et enfants.
- Les nouveaux produits/services créés dans le compte maître ne seront pas synchronisés automatiquement sur vos comptes enfants mais uniquement si un devis qui le comporte est transféré. Il sera donc créé dans le compte enfant choisi uniquement (si non existant) et ne sera pas catégorisé automatiquement.

___________________________________________________________

### Pour aller plus loin 

- Vous êtes client chez Sellsy et souhaitez mettre en place ce connecteur ?
Prenez contact avec notre équipe professional Services : [https://go.sellsy.com/demande-info-sellsy-services](https://go.sellsy.com/demande-info-sellsy-services)

- Vous utilisez actuellement le connecteur et vous avez des questions techniques ? Vous pouvez contacter le support Sellsy via le chat directement qui pourra répondre à vos questions.

Mis a jour le : 24/03/2026
