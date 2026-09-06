---
source: https://help.inter-fast.co/fr/articles/11756324-utiliser-l-api-d-interfast
categorie: Mon Entreprise
titre: Utiliser l'API d'InterFast
date_recuperation: 2026-09-05
---

# Utiliser l'API d'InterFast

> ⚙️ **Cet article s'adresse à un profil technique.** L'API REST d'InterFast permet de connecter votre compte à vos propres outils et automatisations. Son utilisation suppose des compétences en développement (requêtes HTTP, gestion d'une clé d'authentification) et un abonnement Business.

> 💡 Disponible avec votre abonnement ? L'accès à l'API REST et au connecteur MCP est réservé au plan Business.
> Starter — ❌ non disponible
> Pro — ❌ non disponible
> Business — ✅ inclus
> 👉 Pour vérifier ou changer votre plan : rendez-vous dans [Mon Abonnement](https://app.inter-fast.fr/dashboard/company?c=billing).


InterFast propose une API REST permettant de gérer un compte entreprise.

## I. Documentation

Vous pouvez consulter la documentation API d'InterFast sur cette page :

[https://developers.inter-fast.fr/](https://developers.inter-fast.fr/)

Notre équipe technique documente de nouvelles requêtes.


À date, l'API couvre les modules suivants :

- [Calendrier](https://developers.inter-fast.fr/#tag/%C3%A9v%C3%A9nements)
- [CRM](https://developers.inter-fast.fr/#tag/clients)
- [Devis](https://developers.inter-fast.fr/#tag/devis)
- [Bibliothèque](https://developers.inter-fast.fr/#tag/biblioth%C3%A8que)

## II. Demande d'accès

L'API est réservée aux utilisateurs de l'abonnement Business (cf. notre [page Tarifs](https://inter-fast.fr/ressources/page-pricing)).

**Adressez-vous à l'équipe Care**, sur le support en ligne, pour tout renseignement.

> ⚠️ InterFast offre un niveau de support limité sur l'API
> ﻿Il est donc nécessaire que vous fassiez appel aux services d'un développeur qualifié qui sera en capacité de lire et appliquer la documentation.

## III. Authentification

L'API utilise des clés d'API pour authentifier les requêtes.

La clé d'API se compose d'une chaîne de 32 caractères qui est générée par l'utilisateur à partir de la [section Sécurité](https://app.inter-fast.fr/dashboard/profile/2828?settings=security) de son Profil utilisateur :

![](https://downloads.intercomcdn.com/i/o/tarury57/1614774411/9ac17dbc80bdeaae986bb017aba3/CleanShot+2025-07-11+at+11_56_43.png?expires=1788619500&signature=07c8cf5d2f69340f1823eed4f85c28ec027358cec6f9fc981dc9320356dd0c7d&req=dSYmEs55mYVeWPMW1HO4zch4x47u0f%2BkPobdQUKcEYNqfChlDsYqJiufX5%2Fk%0A3LeoZDxdxUKJKybKrIk%3D%0A)

Cette clé d'API doit être fournie dans l'entête X-API-KEY de chaque requête.

## IV. Différences entre API et MCP

InterFast propose également [un connecteur MCP](https://help.inter-fast.co/fr/articles/13769485-connecter-interfast-a-une-ia-via-mcp) pour vos assistants IA (ex: Claude, ChatGPT). Bien que les deux technologies permettent de connecter InterFast à l'extérieur, elles ne répondent pas aux mêmes besoins. Voici comment choisir.

### A. L'API (Application Programming Interface)

###  

- **C'est quoi ?** C'est un connecteur "rigide" conçu pour que deux logiciels communiquent entre eux selon des règles strictes.
​
- **Fonctionnement :** Elle exécute des ordres précis et répétitifs.
​
- **C'est pour qui ?** Les développeurs ou les outils d'automatisation (Zapier, Make, N8N, etc.).
​
- **Usage principal :** Pour créer des **automatisations fixes ***(des tâches répétitives et structurées)* entre vos applications de gestion sans intervention humaine.
​
- *Exemples :* "À chaque fois qu'un formulaire est rempli sur mon site web, créer automatiquement le prospect dans InterFast."
​
​*"À chaque fois qu'un devis est signé, crée un dossier dans Google Drive".*

### B. Le MCP (Model Context Protocol)

###  

- **C'est quoi ?** C'est un connecteur "intelligent" conçu spécifiquement pour donner du contexte à une Intelligence Artificielle.
​
- **Fonctionnement :** Il donne à l'IA le "contexte" de votre entreprise. L'IA peut lire, comprendre et agir sur vos données en fonction d'une discussion naturelle.
​
- **C'est pour qui ?** Les utilisateurs qui dialoguent avec des assistants IA (comme Claude ou ChatGPT).
​
- **Usage principal :** Donner à l'IA la capacité de "lire" vos données InterFast et d'agir dessus en temps réel avec des tâches variées / créatives par simple discussion en langage nature.
​
- *Exemple :* Vous dites à l'IA : *"Analyse les derniers devis de M. Dupont et propose-moi une relance par mail."* *(L'IA utilise le MCP pour lire les devis elle-même et formuler un modèle d'email)*


Tableau Mémo

| **Caractéristique** | **API (ex: N8N / Make)** | **MCP (ex: ChatGPT / Claude)** |
| --- | --- | --- |
| **Langage** | Code informatique | Langage naturel (Français) |
| **Usage** | Automatisation de tâches répétitives | Assistance, rédaction et analyse |
| **Flexibilité** | Faible (scénario figé) | Très élevée (s'adapte à vos questions) |
| **But** | Relier deux logiciels | Faire de l'IA votre assistant métier |

> 💡 Choisissez donc l'**API** pour vos processus automatiques qui ne changent jamais. Choisissez le **MCP** dès que vous avez besoin de réfléchir, de rédiger ou de gagner du temps sur la création de documents complexes par la discussion.

## En résumé


L'API REST d'InterFast permet d'automatiser la gestion d'un compte entreprise, sur quatre modules : Calendrier, CRM, Devis et Bibliothèque. Elle est **réservée au plan Business** : l'accès se demande à l'équipe Care, puis s'utilise avec une **clé de 32 caractères** passée dans l'en-tête **X-API-KEY** de chaque requête.


Pour une assistance en langage naturel plutôt que du code, InterFast propose aussi un **connecteur MCP** destiné aux agents IA.


Il n'existe **pas de connecteur natif Make, Zapier ou n8n** : l'interconnexion passe soit par l'API REST (l'outil no-code appelle InterFast), soit par les **webhooks des automatisations natives** (InterFast envoie la donnée vers l'outil).


Le support InterFast sur l'API reste **limité** — pour un vrai projet d'intégration, faites-vous accompagner par un développeur.

## V. Questions fréquentes (FAQ)

- L’accès à l'API est exclusivement réservé aux utilisateurs disposant de l'**[abonnement Business](https://inter-fast.fr/ressources/page-pricing)**.
- L'API permet d'accéder à des données / actions supplémentaires et d'interconnecter InterFast à des logiciels externes.

- La **documentation complète** est disponible à l'adresse suivante : https://developers.inter-fast.fr/
- Votre clé API est unique à votre profil utilisateur et à votre environnement.
Elle peut être créée dans l'**onglet Sécurité** de votre profil.

- Navré, notre équipe de Conseillers ne peut fournir qu'un **niveau de support limité** sur l'API.
- Il est impératif de faire appel aux services d'un **développeur qualifié** pour le développement de vos requêtes et scénarios d'automatisation.

- Oui, l'API REST permet d'interconnecter InterFast à des outils no-code comme Make / N8N / Zapier.
- Vous pouvez également déclencher des webhooks dans les [automatisations natives](https://help.inter-fast.co/fr/articles/11035957-automatiser-mes-actions-et-taches?q=webhook) d'InterFast pour envoyer de la donnée vers vos applications externes.


Notre équipe technique a commencé le développement d'un connecteur MCP.
Plus d'informations seront communiquées dans les Actualités du support en ligne, lorsque le développement sera terminé.


À date l'API d'InterFast permet d'interagir avec les modules suivants :
- **Opérations** (Événements / Interventions / Modèles de rapports)
- **CRM** (Clients / Contacts / Adresses / Activités)
- **Ventes** (Devis / Factures)
- **Compte** (Utilisateurs / Agences)
- **Outils** (Bibliothèque / Propriétés personnalisées)

- Pour toute demande d'assistance technique sur l'API, vous devez impérativement communiquer :
​
1. Le type de requête.
2. Le code associé.
3. Le résultat attendu.
4. Le résultat observé.
- Ces éléments seront ensuite transmis à l'équipe technique pour analyse.



Mis à jour le : 03/09/2026
