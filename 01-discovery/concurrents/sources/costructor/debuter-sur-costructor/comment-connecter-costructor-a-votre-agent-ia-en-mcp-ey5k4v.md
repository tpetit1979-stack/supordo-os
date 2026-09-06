---
source: https://support.costructor.co/fr/article/comment-connecter-costructor-a-votre-agent-ia-en-mcp-ey5k4v/
categorie: Débuter sur Costructor
titre: Comment connecter Costructor à votre agent IA en MCP ?
date_recuperation: 2026-09-05
---

# Comment connecter Costructor à votre agent IA en MCP ?

> Le serveur MCP Costructor est en bêta, gratuit et ouvert à tous jusqu'au 31 août 2026.

Le **serveur MCP Costructor** permet à votre assistant IA de lire et d'agir sur vos données Costructor via un ensemble d'outils dédiés. Vous pilotez ainsi Costructor en conversant avec le LLM de votre choix.

Il implémente le [Model Context Protocol](https://modelcontextprotocol.io/), un standard ouvert créé par Anthropic et maintenu par la communauté, qui permet aux grands modèles de langage de découvrir et d'appeler les outils exposés par un serveur. Du point de vue de l'utilisateur final, une fois le serveur installé, votre assistant gagne un nouvel ensemble de capacités.

> Connecter le serveur MCP Costructor partage les données de votre compte Costructor avec un outil IA tiers. **Lisez attentivement les Conditions et informations avant de vous connecter.** En autorisant la connexion, vous acceptez ces conditions, y compris le partage de vos données de compte avec l'outil IA choisi.

## Point de terminaison (endpoint)

|

Champ
 |

Valeur
 |  |
|

URL du serveur
 |

[`https://api.costructor.co/mcp`](https://api.costructor.co/mcp)
 |  |
|

Authentification
 |

OAuth (voir la section Authentification)
 |  |

Le serveur réutilise le même fournisseur d'identité que l'API Costructor. Les scopes OAuth documentés dans la référence de l'API régissent ce que chaque outil peut faire en votre nom.

## Ce que vous pouvez faire

Une fois connecté, votre assistant peut réaliser des **actions et écritures** sur votre compte :

1. **Créer** de nouveaux éléments dans votre compte Costructor
2. **Modifier** et mettre à jour des éléments existants

## L'installer

Choisissez le client qui correspond à votre assistant. Certains clients (Cursor, VS Code) proposent une installation en un clic ; d'autres (Claude, ChatGPT, Le Chat) demandent de coller l'URL dans leurs paramètres de connecteurs.

Pour la configuration manuelle, utilisez simplement l'URL du serveur et l'authentification OAuth :

```
{
  "mcpServers": {
    "costructor": {
      "url": "https://api.costructor.co/mcp"
    }
  }
}
```

Au premier appel, votre client ouvre le flux OAuth Costructor dans le navigateur pour autoriser la connexion.

## Authentification (OAuth)

1. Ajoutez le serveur MCP dans votre client avec l'URL ci-dessus.
2. Au premier appel d'outil, le client déclenche le flux OAuth et ouvre une page de connexion Costructor.
3. Connectez-vous et **autorisez** l'accès. Les scopes accordés déterminent les actions autorisées.
4. Le client stocke le jeton d'accès et rafraîchit automatiquement la session.

Vous pouvez **révoquer l'accès à tout moment** depuis la section *applications connectées* de votre compte Costructor.

## Lien avec l'API Costructor

Le serveur MCP est construit **au-dessus de l'API Costructor** et utilise ses endpoints en aval pour agir en votre nom. Les outils MCP sont pensés autour de ce dont un assistant a besoin pour accomplir une tâche, plutôt que de refléter l'API à l'identique : un seul outil peut combiner plusieurs endpoints, ajouter de la validation, ou adapter les entrées/sorties à un usage conversationnel. Il n'y a donc pas de correspondance un-à-un entre un outil et un endpoint de l'API.

Utilisez l'**API directement** si vous construisez une intégration backend sur mesure, un connecteur ERP, ou un produit embarqué. Utilisez le **serveur MCP** si vous souhaitez une interface conversationnelle et ad hoc vers votre compte Costructor via un assistant que vous utilisez déjà.

> Le serveur MCP n'expose qu'un sous-ensemble sélectionné de l'API : les endpoints de lecture et un jeu vérifié d'opérations d'écriture. Pour les autres cas d'usage, utilisez l'API directement.

#### Utiliser l'API directement

L'API Costructor utilise des **clés API** pour authentifier les requêtes. Vous pouvez consulter et gérer vos clés API via Réglages > API.

|

Champ
 |

Valeur
 |  |
|

URL de base
 |

[https://api.costructor.co/external/v1](https://api.costructor.co/external/v1)
 |  |
|

Authentification
 |

Clé API via jeton `Bearer`
 |  |

Toutes les requêtes API nécessitent un Bearer Token. Passez votre clé API dans l'en-tête `Authorization` au format `Bearer YOUR_API_TOKEN` :

```
curl -H "Authorization: Bearer YOUR_API_TOKEN" \
  [https://api.costructor.co/external/v1/contacts](https://api.costructor.co/external/v1/contacts)
```

Consultez la référence de l'API pour la liste complète des endpoints.

## Modèle de sécurité

1. Chaque appel d'outil est **authentifié en votre nom** : le serveur détient un jeton d'accès OAuth émis pour votre utilisateur Costructor. Il ne peut pas agir au-delà de ce que votre rôle et votre organisation autorisent.
2. Le serveur MCP Costructor lui-même **ne stocke pas** le contenu des conversations, ni les transcriptions, ni vos données métier ; il ne fait que relayer les appels d'outils vers l'API.
3. Le **client MCP** (Claude, ChatGPT, Cursor, etc.) détient la conversation, y compris les données renvoyées par les outils. Vérifiez la politique de traitement des données de votre client avant de vous connecter.
4. Vous pouvez révoquer l'accès à tout moment depuis la section *applications connectées* de votre compte Costructor.

> Besoin de signaler un bug, de demander une fonctionnalité, ou vous n'avez pas trouvé votre réponse ? Contactez le support Costructor.

Mis à jour le : 06/08/2026
