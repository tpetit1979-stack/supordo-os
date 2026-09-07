---
url: https://go.sellsy.com/blog/innovation-resilience-sellsy-nouvel-hebergeur
url_finale: https://go.sellsy.com/blog/innovation-resilience-sellsy-nouvel-hebergeur
date_collecte: 2026-09-07
destination: site_marketing
---

Nos dernières actus

15/5/2025

- mis à jour le

# Innovation et résilience : Sellsy passe à la vitesse supérieure avec un nouvel hébergeur

### Sommaire

*Après le déménagement des bureaux bordelais en 2023, c’est notre infrastructure d’hébergement qui a, elle aussi, changé d’adresse en 2024… tout en restant en France ! Un nouveau chapitre technologique pour Sellsy, toujours plus sécurisé, performant, et souverain.*


## Un hébergement souverain, performant et sécurisé


Depuis sa levée de fonds en janvier 2022, Sellsy connait une forte croissance. Il a donc fallu anticiper les limites de l’infrastructure on-premise jusque-là utilisée, pour améliorer nos capacités de scalabilité et de résilience.

Un élément stratégique était de ne pas dépendre d’un fournisseur de cloud américain, afin de garantir la **souveraineté** et la **conformité des données :** un réel critère de choix pour nos clients.

C’est **l’hébergeur français** [**Scaleway**](https://www.scaleway.com/fr?utm_source=partner&utm_medium=organic&utm_campaign=202503-nur-ww-all-generic_gated_content&utm_content=enix_sellsy_) qui a été choisi, en raison des nombreux avantages offerts par ses solutions cloud et serveurs Bare Metal. Sur le plan logiciel, notre équipe technique a opté pour le déploiement de sa nouvelle plateforme à l’aide d’un ensemble d’outils reposant sur Kubernetes.

Pour accompagner cette transition et assurer l’exploitation de la plateforme en continu (24/7), Sellsy collabore désormais avec l’infogéreur [Enix.io](http://enix.io/) spécialiste du Cloud Native et du DevOps.

## La préparation de la migration vers Scaleway


Pendant six mois, les équipes ont travaillé à une **transformation majeure du code de Sellsy** pour assurer une transition fluide vers notre nouvelle architecture.

L’un des chantiers les plus conséquents a été la **refonte complète de la gestion des bases de données**. Au lieu d’une instance centrale mutualisée entre tous les clients, chaque client dispose désormais de sa propre base de donnée, nécessitant des adaptations en profondeur ainsi que la création de scripts de migration robustes pour garantir la continuité des services.

En parallèle, l’équipe infra de Sellsy a adapté les applications à Kubernetes. Bien qu’elles aient déjà été conteneurisées, certaines nécessitaient encore une isolation complète pour s’aligner avec nos nouveaux standards d’architecture.

*Selon Quentin Loupot, “c*e projet de longue haleine pour migrer nos infrastructures dans le Cloud est avant tout un succès collectif : nos équipe en interne qui ont su relever le défi d’une transformation complète de nos systèmes d’hébergement.”

Cette séparation claire a permis d’améliorer la **fiabilité et la maîtrise de nos mises en production**.


## Le grand déménagement : une nouvelle infrastructure pour Sellsy


Pendant 3 mois l**es équipes de Sellsy et d’Enix ont été en lien direct** (merci Slack connect!) pour piloter les différentes phases de la migration.

L‘interconnexion du réseau entre les 2 infrastructures réalisée en amont a grandement facilité cette étape, car elle a permis de continuer l’exploitation des services le temps qu’ils soient basculés d’une infra à une autre, tout en limitant les coupures.

Ainsi, durant ces 3 mois, les **données des clients de Sellsy ont été déplacées progressivement** de la base centrale dans MariaDB vers leurs bases de données dédiées dans les différentes instances Postgresql.


## Sécurité et fiabilité : vos données méritent le meilleur


Chez Sellsy, nous considérons vos données comme un actif stratégique. C’est pourquoi notre nouvelle infrastructure Cloud, toujours hébergée en France, renforce nos engagements de **sécurité, de continuité et de conformité**.

Nos applications sont désormais déployées simultanément sur **trois datacenters Scaleway en région parisienne**, via un **cluster Kubernetes multi-zone**, garantissant ainsi une **haute disponibilité native**.

Côté bases de données, nous avons mis en place une sauvegarde en continu grâce au **Point In Time Recovery (PITR)** de PostgreSQL, pour une restauration rapide et granulaire en cas d’incident.

Et parce qu’il ne peut y avoir d’innovation sans confiance, nous allons encore plus loin :

- **Chiffrement des données** en transit et au repos
- **Surveillance proactive** 24/7 contre les intrusions
- **Traçabilité et contrôle strict** des accès internes
- **Sauvegardes automatiques quotidiennes**

*“Notre nouvelle infrastructure tient toutes ses promesses : +30 % de performance, une sécurité renforcée, et des processus d’exploitation largement automatisés. C’est un changement structurel au service de la fiabilité et de l’expérience utilisateur.” – Quentin Loupot, Head of Infra chez Sellsy*


## Une base solide pour préparer l’avenir


Avec ce nouveau socle technologique, Sellsy est prêt à **accompagner sereinement sa croissance**, tout en continuant à offrir à ses clients un service robuste, sécurisé et respectueux des réglementations.

Cette migration marque **une étape clé** dans notre transformation technique — mais certainement pas la dernière. Elle ouvre la voie à **de nouvelles innovations** à venir sur notre plateforme, toujours plus orientées performance, automatisation et simplicité d’usage.

Et ce, toujours avec une exigence forte : proposer à nos clients un CRM **fiable, souverain et performant**, conçu en France, pour les entreprises françaises.