---
url: https://openfire.fr/blog/facturation-electronique-15/facturation-electronique-quest-ce-quune-plateforme-agreee-pa-et-comment-openfire-sy-connectera-53
url_finale: https://openfire.fr/blog/facturation-electronique-15/facturation-electronique-quest-ce-quune-plateforme-agreee-pa-et-comment-openfire-sy-connectera-53
date_collecte: 2026-09-07
destination: site_marketing
---

*Dernière date de mise à jour : 30/06/2026*

La facturation électronique va transformer la manière dont les entreprises échangent leurs factures. À partir de septembre 2026, toutes les entreprises devront être en mesure de **recevoir** des factures électroniques via une Plateforme Agréée. L’obligation d’**émettre** des factures électroniques s’appliquera ensuite progressivement selon la taille des entreprises. Cette précision est importante
: dès septembre 2026, toutes les entreprises sont concernées par la réception, tandis que l’émission et l’e-reporting suivent le calendrier réglementaire prévu pour 2026-2027.

Pour comprendre le contexte réglementaire, vous pouvez consulter notre article [Facturation électronique : tout comprendre sur la nouvelle obligation pour les entreprises.](https://openfire.fr/blog/facturation-electronique-15/facturation-electronique-tout-comprendre-sur-la-nouvelle-obligation-pour-les-entreprises-49)

**Mais concrètement, qu’est-ce qu’une Plateforme Agréée ? Quel est son rôle dans la réforme ? Et comment OpenFire s’y connectera ?** 

Chez OpenFire, ce sujet est désormais concret : nous avons fait le choix de la Plateforme Agréée **Super PDP**, en cours d’intégration et un déploiement progressif à partir de 2026. Notre position est claire : OpenFire ne devient pas directement Plateforme Agréée. La PA est un métier à part entière. Le rôle de OpenFire est de rester au plus proche du terrain, là où la donnée de facturation prend naissance, puis de faire le lien avec la PA choisie.

Dans cet article, nous vous expliquons simplement :

- ce qu’est une Plateforme Agréée ;
- son rôle dans la facturation électronique ;
- comment OpenFire s’y connectera ;
- 
et ce que ce choix signifie concrètement pour vos usages quotidiens.

**Notre objectif** : vous donner une vision claire pour anticiper sereinement la transition, sans complexité inutile.

## Plateforme Agréée (PA) : de quoi parle-t-on exactement ?

Une **Plateforme Agréée**, souvent abrégée **PA**, est un acteur autorisé à faire circuler les factures électroniques dans le cadre de la réforme. Elle devient le **point de passage officiel** des factures électroniques. C’est l’intermédiaire autorisé qui permet aux factures de circuler entre entreprises, transmet les données d’e-reporting à l’administration fiscale et interroge l’annuaire national pour identifier le bon point de réception.

Elle remplace donc l’envoi direct classique : vos factures ne partent plus simplement par e-mail ou sous forme de PDF libre. Elles passent désormais par une plateforme conforme, capable de transmettre, recevoir et suivre les flux dans le cadre réglementaire.

Choisir sa Plateforme Agréée, c’est choisir par où passent officiellement vos factures, vos données de reporting et vos échanges avec l’annuaire national.
Concrètement et selon le site officiel [impots.gouv.fr](https://www.impots.gouv.fr/facturation-electronique-et-plateformes-partenaires), une PA ne remplace ni votre logiciel de gestion, ni votre expert-comptable. Elle agit comme l’infrastructure conforme qui permet au système de fonctionner.

**PDP/PA : un changement de nom, pas de fonctionnement**

Jusqu’à mi-2025, les plateformes chargées de transmettre les factures électroniques étaient appelées **PDP**, pour Plateformes de Dématérialisation Partenaires. Depuis juillet 2025, la Direction Générale des Finances Publiques a retenu une appellation plus claire : **Plateformes Agréées**, ou **PA**.

Ce changement est principalement terminologique : le rôle attendu reste le même. La plateforme doit permettre l’émission, la réception, la transmission des factures électroniques, la remontée des données attendues par l’administration et l’interopérabilité avec les autres plateformes.

Dans le langage courant, vous pourrez donc encore rencontrer l’ancien terme **PDP**, mais l’appellation à privilégier est désormais **Plateforme Agréée ou PA**.

**La liste des plateformes agréées : où en est-on aujourd'hui ?**

Pour qu’une plateforme puisse être utilisée dans le cadre de la facturation électronique obligatoire, elle doit être officiellement immatriculée ou agréée par l’administration. 
Cette reconnaissance atteste que la plateforme :

- est autorisée à émettre, transmettre et recevoir des factures électroniques ;
- sait extraire et transmettre les données fiscales attendues ;
- respecte les exigences techniques nécessaires aux échanges entre plateformes ;
- 
permet le suivi des statuts et la bonne circulation des flux.

Depuis début 2026, les travaux techniques se sont accélérés et les premiers choix d’intégration côté éditeurs sont en cours.

Chez OpenFire, nous avons retenu **SUPER PDP** comme Plateforme Agréée partenaire afin d’anticiper cette mise en conformité et de proposer une intégration fluide à nos utilisateurs. Ce choix s’inscrit dans une logique simple : proposer une connexion native entre OpenFire et SUPER PDP, tout en respectant le principe d’interopérabilité prévu par la réforme.
[>> Nous détaillons ce choix dans notre article dédié.](https://openfire.fr/blog/facturation-electronique-15/facturation-electronique-openfire-choisit-super-pdp-comme-plateforme-agreee-80) 

## Quel est le rôle exact d'une Plateforme Agréée dans la réforme ?

Avec la généralisation de la facturation électronique, la PA devient un maillon incontournable du dispositif.

Son rôle ne consiste pas à remplacer votre logiciel de gestion OpenFire, ni votre expert-comptable. Elle agit comme le point de passage officiel permettant à chaque facture d’être transmise, contrôlée, suivie et déclarée dans le cadre légal.

__Voici concrètement ce qu’une PA fera pour chaque facture__ :

**1. Contrôler la conformité du format** 

Avant toute transmission, la PA vérifie que la facture respecte l’un des formats officiels attendus : **Factur-X, UBL ou CII**.

Ces formats structurés permettent aux données d’être lues automatiquement par les logiciels, les plateformes et l’administration.

**2. Vérifier les données obligatoires** 

SIREN, SIRET, numéro de TVA intracommunautaire, montants, mentions légales, nature de l’opération, pays, adresses : les données doivent être complètes et cohérentes.

Si une information est manquante ou incohérente, la facture peut être rejetée ou bloquée.

**3. Acheminer la facture au bon destinataire** 

Même si votre client utilise une autre PA, les plateformes doivent pouvoir communiquer entre elles. C’est tout l’enjeu de l’interopérabilité : éviter les réseaux fermés et permettre aux entreprises de choisir, changer ou faire évoluer leur PA sans remettre en cause leur logiciel métier. La PA interroge l’annuaire national pour identifier le point de réception officiel associé au SIRET du destinataire.

**4. Transmettre les données fiscales à l’État**

La PA transmet les données attendues à l’administration fiscale dans le cadre de l’e-invoicing et de l’e-reporting.

Cela permet à l’État de mieux suivre les transactions, de fiabiliser le contrôle de la TVA et, à terme, de simplifier certaines obligations déclaratives.

**5. Suivre le cycle de vie de la facture** 

La réforme introduit une logique de **cycle de vie**. Cela signifie que les statuts des factures peuvent être suivis à chaque étape : reçue, rejetée, acceptée, mise à disposition, traitée, etc. Ce suivi permet de mieux tracer les échanges et de sécuriser le traitement des factures entrantes et sortantes.

**6. Garantir la traçabilité** 

Chaque étape est suivie et historisée : émission, contrôle, transmission, réception, rejet, acceptation ou traitement.

Cette traçabilité permet de réduire les litiges, de sécuriser les échanges et de mieux piloter les délais de traitement. 

__En résumé : à quoi sert une PA ?__ 

La PA est le **point de passage officiel** du système. Elle permet aux factures électroniques de circuler entre entreprises dans un cadre conforme, sécurisé et traçable. Elle ne remplace ni le logiciel de gestion, ni l’expert-comptable.

Le logiciel métier, comme OpenFire, reste l’outil dans lequel la facture est créée, suivie et exploitée au quotidien. La PA assure la transmission officielle, l’interrogation de l’annuaire national et la remontée des données attendues par l’administration.

Pour mieux comprendre comment se répartissent les rôles entre votre logiciel, votre expert-comptable et la Plateforme Agréée, vous pouvez consulter notre article : [Facturation électronique : ce que fait votre logiciel… et ce que fait votre expert-comptable.](https://openfire.fr/blog/facturation-electronique-15/facturation-electronique-ce-que-fait-votre-logiciel-et-ce-que-fait-votre-expert-comptable-52)

## PA, annuaire national et cycle de vie : les notions à comprendre

Pour bien comprendre le rôle d’une Plateforme Agréée, il faut aussi comprendre deux notions clés de la réforme : l’**annuaire national** et le **cycle de vie**. 

**L'annuaire national**

L’annuaire national peut être compris comme le registre officiel des flux de facturation électronique. Il définit l’adresse de réception officielle d’une entreprise pour l’ensemble du réseau français. Concrètement, chaque entreprise y déclare où elle souhaite recevoir ses factures fournisseurs. Cette adresse est associée à son SIRET et permet aux plateformes d’acheminer automatiquement les factures vers le bon destinataire. 

**Le cycle de vie**

Le cycle de vie correspond au suivi des statuts d’une facture. Il permet de savoir si une facture a été émise, reçue, rejetée, acceptée ou traitée.

## Comment OpenFire se connectera aux Plateformes Agréées ?

**Pourquoi les entreprises doivent-elles obligatoirement choisir une Plateforme Agréée ?**

À partir du 1er septembre 2026, toutes les entreprises assujetties à la TVA devront être en mesure de recevoir des factures électroniques via une Plateforme Agréée.
L’émission deviendra ensuite obligatoire selon le calendrier prévu par la réforme.

L’objectif est simple : garantir le bon acheminement des factures, assurer la conformité des échanges et permettre la transmission des données attendues à l’administration fiscale. Sans Plateforme Agréée, une entreprise risque de ne pas pouvoir recevoir ou transmettre correctement ses factures électroniques.

Dans la pratique, cette intégration ne repose pas nécessairement sur l’entreprise : elle peut être directement prise en charge par votre logiciel de gestion, lorsqu’il propose une solution conforme.

**L'accompagnement OpenFire**

Une question revient souvent : “*Qui va s’occuper de connecter mon logiciel à une Plateforme Agréée ?*”

**La réponse est simple : OpenFire le fait pour vous.**

OpenFire reste votre outil métier et votre opérateur de dématérialisation. Notre rôle est de préparer et structurer les données issues du terrain, puis de faire le lien avec la Plateforme Agréée choisie.

Concrètement, nos équipes assurent l’intégration avec **SUPER PDP**, notre PA partenaire, dans le cadre d’un déploiement progressif à partir de 2026. Cette connexion native OpenFire <> SUPER PDP permettra de gérer l’e-invoicing, l’e-reporting, l’annuaire national et le cycle de vie des factures directement depuis OpenFire.

**Ce que OpenFire prend en charge :** 

- l’émission des factures électroniques via SUPER PDP ;
- la réception des factures électroniques ;
- la transmission automatique des données obligatoires à l’administration ;
- la récupération des factures entrantes, y compris lorsque vos fournisseurs utilisent une autre plateforme ;
- la synchronisation des statuts : envoyée, reçue, rejetée, acceptée, traitée ;
- l’intégration dans vos workflows internes : validation, traitement, classement ;
- 
la centralisation des flux dans votre outil métier.

OpenFire préparera et structurera les données issues du terrain afin qu’elles puissent circuler correctement dans le cadre de la réforme. L’objectif est d’éviter les ressaisies, les ruptures de flux et les détours techniques inutiles entre vos équipes, vos clients, vos fournisseurs et votre expert-comptable.

__Ce qu'il faut retenir pour les clients OpenFire__ : 

**Pour les clients OpenFire, l’objectif est de rendre la réforme aussi simple que possible.** 

Vous continuez à utiliser OpenFire comme aujourd’hui pour votre facturation. La couche réglementaire est intégrée progressivement dans votre outil. La connexion à SUPER PDP est prévue nativement dans OpenFire. Cette intégration est incluse dans votre abonnement OpenFire lorsque la délégation est autorisée par vos soins.

Avec cette organisation, OpenFire devient le point de continuité entre votre activité terrain, vos factures, votre PA, vos clients, vos fournisseurs et votre expert-comptable.

## Pourquoi OpenFire a choisi la PA SUPER PDP ?

OpenFire a choisi d’intégrer SUPER PDP comme Plateforme Agréée partenaire pour proposer une solution simple, intégrée et compatible avec les exigences de la réforme.

Ce choix signifie notamment :

- une connexion native entre OpenFire et SUPER PDP ;
- la gestion de l’annuaire national directement depuis OpenFire ;
- la prise en charge de l’e-invoicing ;
- la prise en charge de l’e-reporting ;
- le suivi du cycle de vie des factures ;
- le téléchargement des factures directement dans OpenFire ;
- le suivi des statuts directement dans OpenFire : rejet, acceptation, réception, traitement.

SUPER PDP a été retenue car c'est une PA spécifiquement dédiée à la facturation électronique (elle ne fait rien d'autre), ouverte à l’interopérabilité et adaptée à une gestion centralisée depuis OpenFire.

Le choix de SUPER PDP par OpenFire ne vise pas à enfermer les clients dans un schéma unique. Il s’inscrit au contraire dans une logique d’ouverture et de liberté de choix, au coeur de la réforme de la facturation électronique.

## Comment choisir sa PA selon votre organisation ?

Le bon choix de PA est celui qui reste connecté à l’outil qui porte réellement le flux métier.

__Si vous gérez vos fournisseurs et vos achats dans OpenFire__

Il est recommandé de privilégier la réception via OpenFire. Cela permet de retrouver les factures fournisseurs directement dans votre outil, sans perte d’information ni dispersion des données. La centralisation facilite la gestion comptable, mais aussi le suivi opérationnel au quotidien.

__Si votre comptabilité fournisseur est externalisée__

Si votre expert-comptable gère déjà vos achats, vos fournisseurs ou votre comptabilité fournisseur dans son propre outil, il peut être pertinent d’utiliser la PA de son cabinet pour la réception. Dans ce cas, OpenFire reste votre outil métier pour l’émission et le pilotage opérationnel.

Grâce à l’interopérabilité entre plateformes, cette organisation peut évoluer dans le temps vers une gestion plus centralisée si besoin.

## Conclusion : comprendre les PA pour aborder 2026 sereinement

Le recours à une Plateforme Agréée sera incontournable pour toutes les entreprises, mais cela ne signifie pas que vous aurez un nouvel outil à gérer au quotidien. Une PA est avant tout le point de passage officiel qui permet aux factures électroniques de circuler, d’être contrôlées, transmises, suivies et déclarées dans les règles.

La réforme repose sur un fonctionnement complémentaire :

- votre logiciel métier produit, prépare et pilote les factures ;
- la Plateforme Agréée assure la transmission conforme ;
- l’annuaire national permet d’identifier le bon point de réception ;
- le cycle de vie permet de suivre les statuts ;
- l’expert-comptable contrôle et exploite les données.

Dans la pratique, cette couche technique sera intégrée progressivement dans OpenFire via notre connexion avec SUPER PDP. Vous continuez à utiliser OpenFire comme aujourd’hui, sans rupture dans vos habitudes.

Dès aujourd’hui, vous pouvez anticiper simplement la réforme avec deux actions concrètes :

- Préparer vos données fournisseurs (SIREN, SIRET, TVA, pays, mode de paiement) pour éviter les rejets et fluidifier les échanges.
- Clarifier avec votre expert-comptable l’organisation des flux :
  - Deux options s’offrent à vous :
    - 
**Centralisation dans OpenFire** : vous gérez toutes vos factures (émises et reçues) dans votre outil métier. Votre expert-comptable
récupère ensuite les données nécessaires à sa mission. C’est l’option la plus fluide si vous suivez déjà vos achats, vos fournisseurs et votre comptabilité fournisseur dans OpenFire.
    - 
**Partage des rôles** : vous pouvez décider d’émettre vos factures via OpenFire et de laisser votre comptable gérer la réception sur sa propre plateforme. 
Dans les deux cas, OpenFire reste votre outil métier central pour votre activité, vos clients et vos factures.
  - 

Notre engagement est simple : **assurer la conformité, automatiser les échanges et vous permettre d’aborder la réforme sereinement, sans complexité inutile.**

Vous souhaitez voir comment OpenFire intégrera la facturation électronique dans votre quotidien ? **>> Demandez une démo personnalisée de OpenFire**

#### [Camille Rouaud • Responsable Marketing](https://openfire.fr/auteur/camille-rouaud)

                                Ses articles vous permettent de rester informé des dernières nouveautés de l'ERP.