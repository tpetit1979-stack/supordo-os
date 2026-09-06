---
source: https://help.sellsy.com/fr/articles/13376781-gerer-sa-tva-dans-le-cadre-de-la-facturation-electronique
categorie: Facturation électronique
titre: Gérer sa TVA dans le cadre de la facturation éléctronique
date_recuperation: 2026-09-05
---

# Gérer sa TVA dans le cadre de la facturation éléctronique

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/1937059665/6dc6b23890f95e867475c9525952/FAQ-Bannie-CC-80reAcademy-2-2B-282-29.png?expires=1788635700&signature=88604b01355d95e7443ea8854355d9f3d68ab4a447dfcd7898356d6bcf4b0ffd&req=dSkkEcl7lIdZXPMW1HO4zQnhIVNt%2F5VlIOi6XlcVmhNLrIgcSfm%2FPO8QJRkY%0AVoOd35XY7d%2FHVXhfqVc%3D%0A)


​

Dans le cadre de la **mise en conformité avec la réglementation française sur la TVA et la facturation électronique**, la gestion des taux de TVA évolue.

Cette page vous explique :

- pourquoi certains taux (notamment à 0 %) ne sont plus utilisables,
- comment fonctionnent les **exemptions de TVA** et les **codes VATEX**,
- ce qui change si vous êtes un **nouveau client** ou un **client existant**,
- où agir concrètement dans votre compte.

___________________________________________________________

### Pourquoi la TVA à 0 % n’est plus proposée

En France, un taux de TVA à 0 % **n’est pas un taux légal autonome**.

Lorsqu’aucune TVA n’est facturée, la loi impose désormais d’indiquer **la raison légale précise de l’exonération**.

Cette raison doit :

- être **explicitement sélectionnée**,
- être associée à un **code VATEX**, utilisé dans la facturation électronique et les échanges réglementaires.

Pour cette raison, les anciens taux à 0 % sont remplacés par un système d’**exemptions de TVA conformes**.

> **Bon à savoir** : Vous pouvez consulter cet article pour approfondir le sujet : [Remplacer les anciens taux de TVA à 0%](https://xn--remplacer%20les%20anciens%20taux%20de%20tva%20%200%25-pje/)

___________________________________________________________

### Qu’est-ce qu’une catégorie de TVA

Une **catégorie de TVA** permet de qualifier le **traitement fiscal** appliqué à une opération.

Parmi les catégories possibles, on retrouve notamment :

- **Soumise à TVA**
- **Exemptée de TVA**
- **Hors champ de TVA**

___________________________________________________________

### La catégorie « Exemptée de TVA »

Une opération **exemptée de TVA** est une opération pour laquelle :

- la TVA **pourrait en principe s’appliquer**,
- mais la loi prévoit une **exonération explicite**, sous certaines conditions.

Au sein de cette catégorie, il existe **plusieurs raisons d’exemption**, qu’il est nécessaire de préciser, par exemple :

- **Livraison intracommunautaire**
- **Export hors Union européenne**
- **Autoliquidation**
- Autres exemptions prévues par la législation

Chaque **raison d’exemption** doit être associée à un **code VATEX**, qui indique le fondement légal de l’exonération.

___________________________________________________________

### Codes VATEX : cadre réglementaire

Les **codes VATEX** sont des codes normalisés utilisés dans la facturation électronique pour identifier la raison d’exemption de TVA.

La **liste officielle et à jour des codes VATEX** est publiée par **PEPPOL** : [https://docs.peppol.eu/poacc/billing/3.0/codelist/vatex/](https://docs.peppol.eu/poacc/billing/3.0/codelist/vatex/)

___________________________________________________________

### Je suis un nouveau client Sellsy

Si vous êtes un nouveau client Sellsy, la configuration est directement **conforme à la réglementation**, sans action particulière à effectuer, sauf si vous avez une raison d’exemption non courante.

- Les **taux de TVA standards légaux** (20 %, 10 %, 5,5 %, 2,1 %, etc.) sont disponibles par défaut. Il est toutefois possible **d’ajouter un nouveau taux standard** si votre activité l’exige.
- Les **exemptions courantes** (livraison intracommunautaire, export, autoliquidation, hors champ de TVA) sont déjà configurées :

| TVA | Catégorie de TVA | Code | Code VATEX |
| --- | --- | --- | --- |
| Exempté | Exempté de TVA (La TVA pourrait s’appliquer, mais la loi prévoit explicitement une exonération) | E |  |
| Intracom | Autoliquidation cas de livraison intra communautaire | K | VATEX-EU-IC |
| Export | Exonération de TVA française pour export hors Union Européenne | G | VATEX-EU-G |
| Autoliquidé | Une opération où c'est le client qui déclare et paie la TVA au lieu du fournisseur. Utilisée principalement pour la sous-traitance dans le BTP, la vente de déchets/matériaux de récupération entre assujettis. | AE | VATEX-EU-AE |
| Hors Champs TVA | Hors du périmètre d'application de la TVA (Opération qui n’est jamais dans le champs d’application de la TVA, ex: opération émise pour raison comptable ou traçabilité financière mais qui ne constitue pas une opération économique: refacturation de frais entre 2 sociétés, refacturation de salaires etc. ) | O | VATEX-EU-O |

> **Bon à savoir** : Vous pouvez également **paramétrer des exemptions supplémentaires**, en fonction de votre situation spécifique.

___________________________________________________________

### Je suis un ancien client Sellsy

Si vous utilisiez déjà des taux de TVA à 0 % :

- Ces taux ont été **archivés **et ils seront** désactivés **d'ici Septembre 2026**.**
- Ils restent visibles dans un encart **« Anciens taux 0 % »**
- Ils ne peuvent plus être utilisés sur de nouveaux documents

Chaque ancien taux à 0 % doit être **remplacé manuellement** par :

- une **exemption de TVA valide**,
- associée au **code VATEX correspondant**.

Aucun remplacement automatique n’est effectué afin d’éviter toute erreur fiscale.

Pour vous accompagner dans cette transition, des **indicateurs visuels (flags)** sont affichés dans votre compte afin d’identifier les éléments à mettre à jour, notamment sur :

- les produits / services,
- les frais de port et emballages,
- les catégories tarifaires,
- les modèles de documents.

Vous pouvez utiliser la [plateforme d'imports](https://help.sellsy.com/fr/collections/3289354-imports) pour **mettre à jour en masse** les taux de TVA de vos produits et services. 

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/1937052668/f890ea19c1187a0b6800540a94a0/Capture+d%E2%80%99e%CC%81cran+2026-01-09+a%CC%80+16_27_50.png?expires=1788635700&signature=577e6032d370619813c90d021524096760ee9ba562d045222cabd33700e38761&req=dSkkEcl7n4dZUfMW1HO4zWzF2LOICW9k5Ha14CVuK9DfISbY6TIfcfrDSz4j%0AABuumkrPqJ9hEFoJuvM%3D%0A)

Ces indicateurs permettent de distinguer :

- les éléments **conformes**,
- ceux nécessitant une **mise à jour**.
​

> ### **Bon à savoir**
> - Un taux de TVA à 0 % doit toujours être remplacé par une **exemption légale**
> - Le choix de la raison d’exemption doit refléter **la réalité de l’opération**
> - Les **codes VATEX** garantissent la conformité réglementaire
> - Les mises à jour sont à effectuer **progressivement**, sans impact sur l’historique
> - Utilisez la plateforme d'imports pour mettre à jour en masse les taux de TVA de votre catalogue

Mis a jour le : 22/05/2026
