---
url: https://openfire.fr/blog/facturation-electronique-15/glossaire-de-la-facturation-electronique-les-termes-cles-a-connaitre-102
url_finale: https://openfire.fr/blog/facturation-electronique-15/glossaire-de-la-facturation-electronique-les-termes-cles-a-connaitre-102
date_collecte: 2026-09-07
destination: site_marketing
---

Facturation électronique, e-invoicing, e-reporting, Plateforme Agréée, Factur-X, annuaire national… La réforme s’accompagne de nombreux termes techniques qui ne sont pas toujours simples à distinguer.

Ce glossaire vous aide à comprendre rapidement le vocabulaire essentiel de la facturation électronique, le rôle des différents acteurs et le fonctionnement prévu dans OpenFire.

Pour retrouver le calendrier, les entreprises concernées et les principales obligations, consultez notre article pour [tout comprendre sur la nouvelle obligation de facturation électronique](https://openfire.fr/blog/facturation-electronique-15/facturation-electronique-tout-comprendre-sur-la-nouvelle-obligation-pour-les-entreprises-49).

## Les notions essentielles de la réforme

- #### Facturation électronique

Une facture électronique n’est pas un simple PDF envoyé par email. Il s’agit d’une facture créée, transmise et reçue dans un format conforme, contenant des données structurées qui peuvent être automatiquement lues et traitées par les logiciels.

Pour les opérations concernées par la réforme, la facture devra circuler par l’intermédiaire d’une Plateforme Agréée. Les formats prévus comprennent notamment UBL, CII et les formats mixtes associant des données structurées à une représentation lisible, comme Factur-X.

- #### E-invoicing

L’e-invoicing désigne l’émission, la transmission et la réception de factures électroniques entre entreprises établies en France et assujetties à la TVA française. La facture est transmise dans un format structuré par une Plateforme Agréée. Elle ne circule donc plus uniquement sous la forme d’un PDF libre envoyé par email.

- #### E-Reporting

L’e-reporting correspond à la transmission à l’administration fiscale de données relatives aux opérations qui ne relèvent pas directement de l’e-invoicing. Il concerne notamment certaines ventes réalisées auprès de particuliers, les opérations avec des entreprises établies à l’étranger et, selon les cas, les données de paiement ou d’encaissement.

Pour comprendre les opérations concernées et les données à transmettre, découvrez [ce que les professionnels de l’énergie doivent savoir sur l’e-reporting](https://openfire.fr/blog/facturation-electronique-15/e-reporting-et-facturation-electronique-ce-que-les-professionnels-de-lenergie-doivent-vraiment-savoir-59).

- #### Cycle de vie d'une facture électronique

Le cycle de vie désigne le suivi des différents statuts d’une facture pendant son traitement. Il permet notamment de savoir si la facture a été déposée, reçue, rejetée, acceptée ou mise en paiement. Les statuts sont échangés entre les outils et les Plateformes Agréées afin d’améliorer la traçabilité des factures et de faciliter leur suivi.

- #### Données structurées

Les données structurées sont les informations de la facture enregistrées dans des champs normalisés et compréhensibles par un logiciel : numéro de facture, date, SIREN, montants hors taxes, taux de TVA, total à payer ou encore références du client. Contrairement aux informations simplement affichées dans une image ou un PDF classique, elles peuvent être contrôlées, importées et traitées automatiquement.

## Les acteurs et l'infrastructure de la réforme de la facturation électronique

- #### Plateforme Agréée (PA)

Une Plateforme Agréée est une entreprise privée immatriculée par l’administration fiscale. Elle assure la circulation officielle des factures électroniques entre les entreprises et transmet à l’administration les données réglementaires attendues.

Elle peut notamment :

- émettre, transmettre et recevoir les factures électroniques ;
- consulter l’annuaire national pour identifier le destinataire ;
- transmettre les données d’e-reporting ;
- faire circuler les statuts du cycle de vie.

Le terme Plateforme Agréée remplace l’ancienne appellation Plateforme de Dématérialisation Partenaire, ou PDP.

Pour aller plus loin, découvrez [le rôle d’une Plateforme Agréée et la manière dont OpenFire s’y connectera](https://openfire.fr/blog/facturation-electronique-15/facturation-electronique-quest-ce-quune-plateforme-agreee-pa-et-comment-openfire-sy-connectera-53).

- #### PA d'émission et PA de réception

La PA d’émission, parfois abrégée PAe, est la plateforme utilisée pour transmettre les factures clients.

La PA de réception, ou PAr, est celle déclarée pour recevoir les factures fournisseurs. Une entreprise peut organiser différemment ses flux d’émission et de réception, notamment lorsque la comptabilité fournisseur est principalement gérée dans un autre outil ou chez l’expert-comptable.

- #### Annuaire national de la facturation électronique

L’annuaire national est le registre central utilisé pour acheminer les factures vers le bon destinataire.

Pour chaque entreprise ou établissement, il indique notamment la Plateforme Agréée chargée de la réception et l’adresse électronique de facturation associée. Les plateformes peuvent ainsi déterminer automatiquement où transmettre une facture à partir des informations d’identification du client.

L’annuaire ne fonctionne donc pas comme une boîte email classique.

- #### Concentrateur de données

Le concentrateur de données est la composante publique chargée de recevoir des Plateformes Agréées les données de facturation, de transaction et de paiement destinées à l’administration fiscale.

Depuis le recentrage du Portail Public de Facturation, celui-ci assure principalement deux fonctions : l’annuaire national et la concentration des données transmises à l’administration. Il n’a plus vocation à constituer une plateforme gratuite d’émission et de réception pour toutes les entreprises.

- #### Opérateur de dématérialisation

Un opérateur de dématérialisation est un logiciel ou un prestataire qui prépare les factures et leurs données, mais qui n’est pas lui-même une Plateforme Agréée.

Au sens fonctionnel, OpenFire joue ce rôle : les données naissent dans l’outil métier, puis OpenFire les prépare, les structure et les transmet à la PA choisie. OpenFire reste ainsi au plus proche des interventions, des devis et des opérations qui sont à l’origine de la facture.

La réforme ne modifie pas seulement les outils : elle implique aussi de bien répartir les responsabilités. Retrouvez [ce que prend en charge votre logiciel et ce qui reste du ressort de votre expert-comptable](https://openfire.fr/blog/facturation-electronique-15/facturation-electronique-ce-que-fait-votre-logiciel-et-ce-que-fait-votre-expert-comptable-52).

- #### Solution compatible

Une solution compatible est un logiciel métier, un ERP ou un logiciel de facturation capable de communiquer avec une ou plusieurs Plateformes Agréées. Elle crée ou exploite les données nécessaires, assure leur conformité et les transmet à la PA par une connexion adaptée. OpenFire sera une solution compatible connectée nativement à SUPER PDP.

## Les formats de facture électronique

- #### Factur-X

Factur-X est un format mixte, également appelé format hybride. Il associe :

- un document PDF lisible par une personne ;
- un fichier XML contenant les données structurées lisibles par les logiciels.

Il permet donc de conserver une représentation visuelle proche d’une facture traditionnelle tout en automatisant son traitement. Factur-X fait partie des trois formats du socle minimal de réception de la réforme française.  [(source : impots.gouv)](https://www.impots.gouv.fr/professionnel/je-decouvre-la-facturation-electronique)

- #### UBL

UBL signifie Universal Business Language.

Il s’agit d’un format XML entièrement structuré permettant de représenter une facture et ses données de manière normalisée. Il est particulièrement adapté aux échanges automatisés entre logiciels et plateformes.

- #### CII

CII signifie Cross Industry Invoice.

Comme UBL, il s’agit d’un format XML structuré permettant aux systèmes informatiques de lire et de traiter automatiquement les informations d’une facture. UBL, CII et les formats mixtes comme Factur-X font partie des formats prévus par le dispositif français. [(source : impots.gouv)](https://www.impots.gouv.fr/professionnel/je-decouvre-la-facturation-electronique)

- #### Normes AFNOR de la facturation électronique

Les normes AFNOR précisent les règles communes permettant aux logiciels et aux Plateformes Agréées d’échanger des factures de manière fiable.

Le dispositif s’appuie notamment sur :

- XP Z12-012, consacrée aux formats, profils de facture et statuts du cycle de vie ;
- XP Z12-013, consacrée aux API entre les systèmes d’information et les Plateformes Agréées ;
- XP Z12-014, consacrée aux principaux cas d’usage B2B.

Ces normes constituent un socle commun pour les entreprises, les solutions compatibles et les Plateformes Agréées.

- #### Peppol

Peppol est un réseau international et un ensemble de spécifications permettant l’échange sécurisé de documents électroniques, dont des factures, entre des organisations utilisant des systèmes différents.

Il repose sur des points d’accès interconnectés et sur des règles communes de transport et de validation. Peppol contribue ainsi à faciliter les échanges électroniques et l’interopérabilité entre acteurs.

## Comprendre les flux de facturation électronique

- #### Flux d'émission des factures électroniques

Le flux d’émission correspond au trajet suivi par une facture client.

Dans OpenFire, la facture est créée à partir des données métier : client, intervention, commande, devis, prestations, produits et TVA. OpenFire prépare ensuite les données dans le format attendu et les transmet à la Plateforme Agréée. La PA identifie le point de réception du client dans l’annuaire national, transmet la facture à sa plateforme et fait remonter les statuts associés.

La réception sera la première échéance concrète pour de nombreuses PME et TPE. Découvrez [comment préparer dès maintenant la réception de vos factures fournisseurs](https://openfire.fr/blog/facturation-electronique-15/facturation-electronique-2026-comment-preparer-la-reception-de-vos-factures-fournisseurs-100).

- #### Flux de réception des factures électroniques

Le flux de réception correspond au circuit des factures envoyées par vos fournisseurs.

Le fournisseur transmet sa facture à sa propre Plateforme Agréée. Celle-ci consulte l’annuaire national, identifie votre PA de réception et lui adresse la facture. La facture peut ensuite être mise à disposition dans votre logiciel de gestion. Avec SUPER PDP comme PA de réception, l’objectif est de permettre le téléchargement et le traitement des factures directement dans OpenFire.

## Interopérabilité et liberté de choix

- #### Principe d'interopérabilité

L’interopérabilité est la capacité de plusieurs logiciels et Plateformes Agréées à communiquer entre eux, même lorsqu’ils sont exploités par des acteurs différents. Une entreprise ne doit donc pas avoir à utiliser la même plateforme que tous ses clients ou fournisseurs. Elle peut également faire évoluer son choix de PA sans remettre en cause son logiciel métier.

Pour OpenFire, ce principe est essentiel : la réforme doit ouvrir les flux, et non enfermer les entreprises dans un réseau ou un outil unique.

- #### La haute transférabilité

La haute transférabilité n’est pas une appellation réglementaire officielle. Chez OpenFire, elle désigne la capacité à récupérer, faire circuler et transférer les données de facturation sans dépendre d’un environnement fermé.

Elle suppose notamment qu’un client puisse changer de Plateforme Agréée ou faire évoluer l’organisation de ses flux sans perdre ses données ni devoir remplacer son logiciel métier.

## OpenFire et SUPER PDP

- #### SUPER PDP

SUPER PDP est la Plateforme Agréée choisie par OpenFire pour son parcours standard de facturation électronique.

La connexion native OpenFire–SUPER PDP est conçue pour couvrir les principaux besoins de la réforme : émission et réception des factures, e-reporting, consultation de l’annuaire national et suivi du cycle de vie. Ce choix vise à éviter l’ajout d’une couche technique déconnectée du terrain : la facture continue à être préparée et pilotée depuis l’outil métier.

Pour connaître les critères qui ont guidé cette décision, découvrez pourquoi OpenFire a choisi SUPER PDP comme Plateforme Agréée.

- #### SUPER PDP en délégation pour OpenFire

La délégation consiste à autoriser OpenFire à gérer la connexion technique entre votre environnement OpenFire et votre compte SUPER PDP. Avec cette délégation, les flux et les statuts peuvent être centralisés dans OpenFire. L’intégration et l’usage de SUPER PDP dans ce parcours sont inclus dans l’abonnement OpenFire, sous réserve de l’autorisation donnée par le client.

La délégation ne remet pas en cause la liberté de choisir une autre Plateforme Agréée.

- #### Parcours d'enregistrement SUPER PDP & OpenFire

Le parcours d’enregistrement sera accessible depuis OpenFire. Il doit permettre de réaliser les principales étapes nécessaires à l’activation :

1. création ou activation du compte SUPER PDP ;
2. validation de la délégation donnée à OpenFire ;
3. vérification de l’identité du représentant légal ;
4. déclaration de la plateforme et de l’adresse de facturation dans l’annuaire national.

L’objectif est de guider les clients dans un parcours intégré, sans inscription technique séparée ni rupture avec leur environnement OpenFire.

Vous souhaitez passer des définitions à l’action ? Retrouvez [les cinq étapes concrètes pour préparer votre entreprise à la facturation électronique](https://openfire.fr/blog/facturation-electronique-15/facturation-electronique-comment-preparer-votre-entreprise-en-5-etapes-concretes-60).

**Une question sur la facturation électronique ?** 

Vous souhaitez approfondir un cas particulier, comprendre le rôle de votre expert-comptable ou organiser vos flux d’émission et de réception ? Consultez [nos réponses aux questions les plus fréquentes sur la facturation électronique](https://openfire.fr/blog/facturation-electronique-15/facturation-electronique-nos-reponses-a-vos-questions-97). 

__Vous ne connaissez pas OpenFire ?__ 

Découvrez comment OpenFire centralise vos interventions, vos devis, vos clients et votre facturation dans une solution métier adaptée aux professionnels de l’installation, de la maintenance et du SAV.

→ [Demander une démonstration de OpenFire](https://openfire.fr/demo-gratuite) 

__Vous êtes déjà client OpenFire ?__ 

Nos équipes vous accompagnent pour comprendre la réforme, préparer vos données et organiser votre transition vers la facturation électronique.

→ [Contacter l’équipe OpenFire](https://openfire.fr/contact)

#### [Camille Rouaud • Responsable Marketing](https://openfire.fr/auteur/camille-rouaud)

                                Ses articles vous permettent de rester informé des dernières nouveautés de l'ERP.