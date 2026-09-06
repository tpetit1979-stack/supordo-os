---
source: https://help.sellsy.com/fr/articles/5870726-statuts-de-documents
categorie: Documents de vente 
titre: Statuts de documents
date_recuperation: 2026-09-05
---

# Statuts de documents

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2195129018/b9142c1ebf58bb54f41d94cbaea8/FAQ-Bannie%CC%80reAcademy-2+%282%29.png?expires=1788635700&signature=75600b854c2a0ae9314c0e7b63dbf119b097ca12bde9d43b7e5828b3cff1d236&req=diEuE8h8lIFeUfMW1HO4zW7LJAmJDMpi7pr3OJ%2Fs3H1w2RDiJvzX7nx5C%2BkF%0An1EA3nwYu08n8%2B9yaO8%3D%0A)

Les documents de vente Sellsy possèdent tous une gamme de statuts correspondant à leur état d'avancement dans le processus de vente.

Ces statuts diffèrent d'un type de document à l'autre. Voici par exemple les statuts disponibles pour un document de type facture :

- À régler
- Paiement partiel
- Payée
- Retard
- Annulée

L'avantage de ces statuts est de vous permettre d'accéder rapidement et facilement à l'information, l'exemple type étant de filtrer les factures en retard pour relancer les clients.

___________________________________________________________

### **Changements de statut automatiques**

La plupart des changements de statut sont automatiques.

Par exemple :

- L'enregistrement d'un paiement total sur une facture va changer le statut en "*Payée*"
- L'envoi par email d'un devis va changer le statut en "*Envoyé*"

**Statuts entre documents liés**

De la même manière, les changements de statuts entre documents liés sont aussi effectués automatiquement.

Un exemple simple est la transformation d'un devis en facture, qui va changer le statut du devis à "*Facturé*" (si besoin, vous pouvez toutefois modifier manuellement le statut d'un devis sur "*Facturé*" sans créer de facture).

**Consulter l'historique**

À tout moment, vous pouvez vérifier l'enchaînement des documents et des statuts en cliquant sur l'onglet "*Historique du document*".

![](https://sellsy-a9cc78fb6d3a.intercom-attachments-7.com/i/o/445622278/bc06d77fa030eb5911dcd607/HI-y1tMUjDD1MRongc8bNnMHyTtHgKEyFu0A_cGmZpaNhJSlROqRX2jkA8tGgSB5OrPHz4iRaNPC_MZJ_KLiwDWMTY15YMYNT0EaPBtzqLgHnHT48EbVm4ebXO8H9SPB6_2BxK_A?expires=1788635700&signature=d89403215ef70001772099db4a719ba86d42cc06d4edbdfe989dc54a459fefc6&req=cCQiEMt8n4ZXFb4f3HP0gF%2B%2Bo2CYwe49ScSYDm%2Fw1FLddvMUyxCpyeBlkxnj%0AQ55ZNNFrTqBTxK9HEA%3D%3D%0A)

___________________________________________________________

### **Fonctionnement des statuts de factures **

Une facture émise doit être figée et ne plus être modifiée. **Vous ne pouvez donc pas modifier ni supprimer** une facture à compter du moment où elle sort du statut "*Brouillon*".

**Annulation d'une facture**

Afin de respecter les bonnes pratiques de facturation, vous ne pouvez plus annuler une facture dans un autre statut que brouillon. **Vous devez créer ou lier un avoir et ensuite effectuer une nouvelle facture**.

**Identifier les factures avec avoir**

Afin de pouvoir identifier les factures qui possèdent au moins un avoir, vous avez la possibilité de filtrer la liste des factures à l'aide du filtre "*Avoir lié*".

![](https://sellsy-a9cc78fb6d3a.intercom-attachments-7.com/i/o/445622282/a56d888fe4dba718528a6080/i7GPoRtBO6beVkWGZFA4TKG_NVCBVTX9BfXYXZt-9bFPe70yeT9LtPnBplA0D5zP_8dE_hfbz6fdiwByJlwDSoDDLqqDom-WOIEEgasq5En3YgIbrjM4Hw_ObCpC8uuZxbBBBrTe?expires=1788635700&signature=2509efc4a8fa057dbf841ca2f65315068a61ca418f2a0c05019966e1338fdcbb&req=cCQiEMt8n4ldFb4f3HP0gEOD0FFeqWj5RlOTYIoMxijbfoH9NPbDetip4bIX%0ANWZYPCv3sTHmreynOA%3D%3D%0A)

___________________________________________________________

### **Cas particuliers **

Dans certains cas, le système ne peut pas déterminer lui-même les statuts des documents parents, car la gestion des statuts se base sur la notion de solde.

Par exemple, si un devis a donné lieu à des factures légèrement différentes (ajout d'une remise par exemple), le total des factures diffère du montant du devis.

Dans ce cas de figure, le système vous demandera à l'enregistrement quel statut vous souhaitez appliquer aux documents en amont.

![](https://sellsy-a9cc78fb6d3a.intercom-attachments-7.com/i/o/445622283/030aff8d2dda0c9c80581972/03Y5A1U6N3mkw-G3yp1F_oNa_0RFo07cYuiCXr1MXckww1omJQzjuf_7XFXLM6MJ2dyiwZ3USN2vp-VL836TE0W7hymgKAEzMpXWQCZQY4Iz5aLFOLZ36MlZ05Nnw9PoOVIYPBnY?expires=1788635700&signature=cbbce8bf58fab636f5a34908bf862f4537226c2f1c17da0695be8e6ec112f95f&req=cCQiEMt8n4lcFb4f3HP0gFGMYW3tqtPmCb8E9cQ1QVasFzaqcTiz32OjKWxE%0AFCvYEGXg0zjdCbSHbw%3D%3D%0A)

> **Bon à savoir : **cette alerte sera affichée si le montant total est inférieur ou dépasse le montant du document parent (le devis dans cet exemple).

Ces règles s'appliquent sur toute la chaîne de documents. Vous pouvez par exemple, à partir d'un devis, générer plusieurs bons de livraison, puis plusieurs factures.

Le système gère automatiquement les liens entre ces documents et leurs statuts respectifs.

Mis a jour le : 24/03/2026
