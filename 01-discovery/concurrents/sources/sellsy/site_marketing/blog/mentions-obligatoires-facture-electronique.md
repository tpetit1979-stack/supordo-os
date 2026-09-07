---
url: https://go.sellsy.com/blog/mentions-obligatoires-facture-electronique
url_finale: https://go.sellsy.com/blog/mentions-obligatoires-facture-electronique
date_collecte: 2026-09-07
destination: site_marketing
---

Facturation Electronique

30/9/2025

- mis à jour le

# Les mentions obligatoires sur une facture électronique

### Sommaire

{{video-banner-blog}}

À partir de 2026, **toutes les entreprises devront émettre et recevoir leurs factures dans un format électronique structuré**, conforme aux exigences de l’administration fiscale. Cela implique non seulement un changement d’outil, mais aussi une adaptation aux nouvelles mentions obligatoires. Numéro unique, TVA intracommunautaire, conditions de règlement… certaines informations restent les mêmes, tandis que d’autres deviennent désormais incontournables avec la réforme.

Comprendre ces obligations dès aujourd’hui, c’est anticiper les contrôles, éviter les rejets de facture et surtout gagner du temps dans vos processus de gestion.

## Ce qui change dans la loi avec la facture électronique

Sur le plan juridique, la facture électronique ne crée pas un nouveau type de facture : elle s’inscrit dans la continuité du Code de commerce et du Code général des impôts, qui fixent déjà les mentions obligatoires (identité des parties, numérotation, TVA, conditions de règlement…). Mais la réforme introduit une nouveauté majeure : **la façon dont ces mentions doivent être transmises et complétées**.

En pratique, la loi demande désormais que certaines informations, jusque-là facultatives ou implicites sur une facture papier, **deviennent obligatoires dans le cadre électronique**. C’est le cas notamment des données de paiement (IBAN, mode de règlement, échéances) ou encore du suivi de cycle de vie de la facture (émise, reçue, acceptée, rejetée, payée).

L’autre évolution tient au format structuré. Une facture papier pouvait se présenter sous n’importe quelle forme tant qu’elle comportait les mentions légales. Désormais, la loi impose que ces données soient intégrées dans un format électronique normé (Factur-X, UBL, CII) afin d’être lisibles par les systèmes de gestion et par l’administration fiscale. Cela transforme la facture en un document à la fois légal et technique, au service du contrôle comme de l’automatisation.

Autrement dit, la réforme ne change pas le fond des obligations, mais elle en modifie la portée : les mentions deviennent plus nombreuses, plus détaillées et surtout interopérables, parce qu’elles ne sont plus seulement écrites pour un lecteur humain mais aussi pour un système d’information.

## Les nouvelles mentions obligatoires

Tout d’abord, il faut rappeler qu’une facture — qu’elle soit papier ou électronique — n’est pas un simple document commercial : c’est un document légal et fiscal.

**La facture électronique doit donc contenir** [**les mêmes informations essentielles qu’une facture papier**](https://go.sellsy.com/blog/creer-une-facture-les-mentions-obligatoires-a-faire-apparaitre-sur-une-facture) : l’identité du vendeur, celle de l’acheteur, ainsi que la description précise de la transaction.  Mais, comme nous avons vu auparavant, la différence majeure réside dans le format. 

C’est précisément ce changement qui entraîne l’apparition de nouvelles exigences. Là où une facture papier pouvait se limiter à un ensemble d’informations “visibles”, la facture électronique doit inclure des données supplémentaires, normalisées, qui permettent un suivi automatisé du cycle de vie : émission, transmission, réception, voire statut de paiement. Concrètement, trois types d’informations gagnent en importance.

D’abord, **les données logistiques et opérationnelles**. Par exemple, l’adresse de livraison ou le mode de transport, qui n’étaient pas toujours indiqués sur une facture papier, deviennent utiles pour suivre la chaîne de facturation de bout en bout.

Ensuite, **les informations liées au paiement**. Le mode de règlement, l’IBAN ou encore la date effective de paiement sont intégrés dans la facture électronique afin de tracer plus précisément le règlement et d’éviter les doublons ou retards non justifiés.

Enfin, **les informations de statut**. Une facture électronique n’est pas figée : son cycle de vie est suivi en temps réel. Le système doit donc savoir si la facture a été émise, reçue, acceptée, refusée ou payée. Ce suivi, inexistant sur le papier, devient obligatoire dans le nouveau dispositif.

Il faut savoir que la facture électronique ne se limite plus à constater une opération commerciale, elle devient un outil de pilotage et de contrôle partagé entre l’entreprise et l’administration.

### Données logistiques et opérationnelles

Sur papier, on se contentait souvent de l’adresse de facturation. Avec la facture électronique c’est la chaîne complète qui doit pouvoir être reconstituée : qui vend quoi, à qui, où et quand c’est livré. Concrètement, la facture intègre des champs normalisés liés à la livraison et au contexte de l’opération :

- **Lieu et adresse de livraison** (utile si différent du siège client)
- **Dates clés** (date réelle de livraison/prestation, parfois distincte de la date de facture)
- **Références opérationnelles** (commande, contrat, numéro de livraison)
- **Type d’opération** (vente de biens, prestation de services, cas particuliers)

Pointe technique : dans les formats structurés (Factur-X, UBL, CII), ces infos vivent dans des blocs dédiés (ex. un bloc “Delivery” avec un lieu et une date). L’objectif c’est de permettre aux systèmes (ERP, PPF/plateformes) d’aligner automatiquement la facture avec la commande et le bon de livraison, et de déclencher les contrôles (cohérence des dates, adresse, référence de commande, etc.).

Le bénéfice ? moins de litiges “on n’a jamais reçu”, moins d’allers-retours, et une réconciliation plus rapide côté compta/achats.

### Données de paiement

La réforme pousse à préciser comment et quand on paie avec plus de détail. On demande désormais d’intégrer :

- **Mode de règlement** (virement, prélèvement, carte, etc.)
- **Coordonnées de paiement** (p. ex. IBAN du bénéficiaire)
- **Échéances précises** (une ou plusieurs dates)
- **Référence de virement** (pour l’appariement automatique)
- **Conditions de retard** (pénalités, indemnité forfaitaire)

Il faut savoir que dans un fichier structuré, on trouve un bloc “PaymentMeans” (qui décrit le mode de règlement) et un bloc “FinancialAccount” (qui précise l’IBAN et le BIC du bénéficiaire). La référence de paiement y circule sous forme codée, et non plus simplement en texte libre. Cette normalisation permet aux systèmes bancaires et comptables d’associer automatiquement un règlement à la facture correspondante, avec un niveau de fiabilité beaucoup plus élevé que dans le cadre d’un simple PDF.

### Données de statut

L’un des fondements de la facture électronique c’est précisément sa capacité à transformer la facture en un processus vivant et traçable, plutôt qu’en un document figé. La facture électronique enregistre et partage en continu les différentes étapes de son cycle de vie. Cette dynamique permet de suivre l’avancement d’une transaction de bout en bout et d’apporter une visibilité qui n’existait pas avec le papier. C’est pour cela que les données de statut deviennent obligatoires sur la facture électronique.

Concrètement, trois moments clés sont désormais standardisés :

- **Réception et accusés :** à la réception d’une facture électronique, le client ou sa plateforme envoie automatiquement une confirmation. Cette notification constitue la preuve tangible que le document a bien été reçu.
- **Acceptation/Rejet :** la réponse du destinataire est formalisée. En cas de rejet, un motif codifié est renvoyé (ex. IBAN invalide, référence manquante), ce qui permet d’identifier rapidement l’anomalie.
- **Paiement :** la facture peut être enrichie d’informations sur la date effective de règlement, offrant une traçabilité complète jusqu’à la clôture de la transaction.

Ces statuts sont transportés via des messages de cycle de vie (acknowledgements, notifications) que les plateformes échangent. Ils permettent aux systèmes de suivre automatiquement l’évolution de la facture et de signaler tout blocage.

{{rt-banner-1}}

## Les mentions particulières dans la facture électronique

Lorsqu’on parle de mentions obligatoires, il ne faut pas oublier qu’au-delà du socle commun (identité des parties, numérotation, TVA, conditions de règlement…), certaines situations imposent d’ajouter des mentions particulières. C’est le cas par exemple lorsqu’une opération est exonérée de TVA, soumise à autoliquidation, ou réalisée par une micro-entreprise en franchise de TVA.

Ces obligations ne sont pas nouvelles : elles existaient déjà pour les factures papier ou PDF. La grande différence avec la facture électronique réside dans le format. Sur une facture papier, il suffisait d’inscrire la mention en toutes lettres. Dans le cadre électronique, ces informations doivent toujours apparaître en clair, mais aussi être **codées dans des champs normés** (Factur-X, UBL, CII). 

Ce qu’il faut savoir, c’est que ces mentions particulières couvrent essentiellement trois familles de cas :

- Les situations fiscales spécifiques (exonération, autoliquidation, TVA sur marge, franchise de TVA…).
- Les statuts particuliers de l’entreprise (micro-entreprise, liquidation judiciaire, etc.).
- Les conditions commerciales précises (acompte, pénalités de retard, références contractuelles).

L’enjeu c’est de s’assurer qu’elles soient correctement intégrées au format électronique. C’est cette codification qui leur donne toute leur portée dans le nouveau système : elles ne sont plus de simples annotations, mais des **données normées** que le Portail Public de Facturation (PPF) et les Plateformes Agrées (PA) peuvent traiter et contrôler automatiquement.

## Se préparer aux mentions obligatoires dans la facture électronique

Vous l’avez compris, la généralisation de la facture électronique pour 2026–2027 impose un travail sur les mentions obligatoires, et il est important, donc, de travailler dès maintenant sur trois axes.

### Vérifier vos pratiques actuelles

Commencez par analyser vos factures papier ou PDF : toutes les mentions obligatoires y figurent-elles ? Les mentions particulières liées à votre activité (TVA exonérée, autoliquidation, micro-entreprise…) sont-elles systématiquement indiquées ? Cette mise au point permet de corriger d’éventuelles lacunes avant de passer au format électronique.

### Anticiper la codification des données

Dans le format électronique, les mentions doivent être présentes en clair, mais aussi codées dans des champs normalisés (Factur-X, UBL, CII). Il est donc essentiel de vérifier que vos outils de facturation (ERP, logiciels comptables, solutions de gestion) sont capables de gérer cette double exigence.

### Choisir un partenaire de dématérialisation

Dès 2026, toutes les factures devront transiter soit par le [Portail Public de Facturation (PPF)](https://go.sellsy.com/blog/portail-public-de-facturation), par une [Plateforme Agré](https://go.sellsy.com/blog/plateformes-agreees)e (PA, ex-PDP). Certaines solutions, comme [Sellsy](https://go.sellsy.com/), sont déjà agréées PA et permettront de garantir que vos factures, avec toutes leurs mentions obligatoires, soient transmises et reconnues par l’administration en toute conformité.

En résumé, la préparation passe autant par une mise en conformité juridique (mentions légales toujours présentes) que par une mise en conformité technique (capacité à les coder dans le format électronique). Anticiper dès maintenant, c’est éviter les rejets de factures demain et sécuriser la transition vers un système 100 % électronique.