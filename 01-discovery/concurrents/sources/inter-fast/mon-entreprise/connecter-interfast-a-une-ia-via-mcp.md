---
source: https://help.inter-fast.co/fr/articles/13769485-connecter-interfast-a-une-ia-via-mcp
categorie: Mon Entreprise
titre: Connecter InterFast à une IA via MCP
date_recuperation: 2026-09-05
---

# Connecter InterFast à une IA via MCP

> **🔔 Pilotez InterFast à la voix ou au clavier !** Grâce au connecteur MCP, transformez votre IA en assistant personnel. Ne perdez plus de temps en saisie : demandez-lui simplement de créer un devis ou de consulter votre planning et laissez la magie opérer.
> ​
> ✅ *Les capacités du MCP sont pour l'instant limitées aux actions suivantes :*
> 1. Rechercher un client
> 2. Créer un client (particulier, professionnel ou syndic)
> 3. Rechercher un devis
> 4. Consulter le détail d'un devis
> 5. Créer un devis (vierge ou depuis un modèle)
> 6. Modifier un devis
> 7. Lister les modèles de devis
> 8. Rechercher un article ou un ouvrage de la bibliothèque
> 9. Rechercher des chantiers
> 10. Consulter le planning
> 11. Planifier une intervention
> 12. Replanifier une intervention
> 13. Consulter les statistiques de facturation
> 14. Tester la connexion

> 💡 Disponible avec votre abonnement ? Le MCP fait partie de l'abonnement Business.
> ​
> Starter — non inclus
> Pro — non inclus
> Business — ✅ inclus — en 🧪 bêta, activation sur demande (faites votre demande via le support en ligne).
> ​
> 👉 Pour vérifier votre plan : rendez-vous dans [Mon Abonnement](https://app.inter-fast.fr/dashboard/company?c=billing).

## I. Définition

### A. Qu'est-ce que le MCP (Model Context Protocol) ?

Le **MCP** est une technologie qui sert de pont intelligent entre deux mondes : d'un côté, votre logiciel InterFast (qui contient vos données métiers), et de l'autre, une Intelligence Artificielle (comme ChatGPT ou Claude).

### B. Comment ça marche ?

D'ordinaire, une IA est limitée aux informations qu'elle a apprises durant son entraînement. En activant le MCP, vous lui donnez une **"fenêtre de lecture"** sur votre propre compte InterFast.

Voici le cycle de fonctionnement :

1. **La Demande :** Vous demandez à l'IA : *"Quelles sont mes interventions demain ?"*.
2. **La Connexion :** Grâce au lien MCP, l'IA interroge instantanément votre base de données InterFast de manière sécurisée.
3. **L'Action :** L'IA analyse vos données et vous répond directement, ou effectue l'action demandée (ex: créer un devis ou planifier un rendez-vous).

### C. Ce que cela change pour vous :

- **Plus de saisie manuelle :** L'IA connaît vos clients et vos tarifs.
- **Assistance en temps réel :** Vous pouvez discuter avec vos données (ex: *"Fais-moi un résumé du chiffre d'affaires du mois dernier"*).
- **Automatisation métier :** Vous décrivez un chantier complexe, et l'IA le transforme en devis structuré dans votre interface InterFast.

## II. Connecter InterFast à ChatGPT

### A. Vidéo tutoriel d'Hedi

[Vidéo]()

### B. Étapes détaillées

### Pré-requis

> ⚠️ Pour utiliser les serveurs MCP et les fonctionnalités avancées de connexion avec des outils externes, vous devez disposer d'un abonnement **[ChatGPT Business](https://chatgpt.com/pricing/)**. Vous pouvez aussi tester gratuitement [Claude](https://claude.com/pricing) et basculer sur le plan Pro selon votre volume d'utilisation. 
> ​
>  Les comptes gratuits ne permettent pas encore d'ajouter des serveurs MCP personnalisés pour interagir avec des logiciels tiers comme InterFast.

### Étape 1 : Générer votre clé API dans InterFast

Tout commence par la création d'un pont sécurisé entre InterFast et votre IA.

1. Rendez-vous sur votre **Profil** (en bas de votre menu InterFast).
2. Allez dans l'onglet **Sécurité**.
3. Dans la section **Clés API**, cliquez sur **Ajouter une clé**.
4. Nommez-la (ex: "Connexion IA ChatGPT") et enregistrez.
5. **Important :** Copiez le lien du serveur MCP qui s'affiche sous votre clé.

![](https://downloads.intercomcdn.com/i/o/tarury57/2081841419/6e17486c1b273fdbbcbaca28e346/CleanShot+2026-02-19+at+10_57_36%402x.png?expires=1788619500&signature=f45aaf7dfe92137d97ad8f65d96101639d6993cfc0c499b90ab41bf45e1bfb50&req=diAvF8F6nIVeUPMW1HO4zZUWJstrqk9Ie7ooNeAXrBPA%2Bh1T%2Bvc84WI8V1uP%0An33J4tM%2FqhzfLN2Loqk%3D%0A)

![](https://downloads.intercomcdn.com/i/o/tarury57/2081879088/fb3ee1a01d35ce5405fc181e5630/CleanShot+2026-02-19+at+11_14_17%402x.png?expires=1788619500&signature=8c646ecf4a15fbdda25a041100bc17e271662379c45c12a6d6a4ba1e23b41e81&req=diAvF8F5lIFXUfMW1HO4zZDr5QTRoFaOk6VA4s6c%2F6hRmxd1UkIdPN0cKE2r%0A%2BPQ%2B23XnuhSbjKR5USc%3D%0A)

### Étape 2 : Configurer l'outil d'IA

Une fois l'URL copiée, vous devez l'indiquer à votre interface d'intelligence artificielle (les étapes peuvent varier légèrement selon l'outil, ici l'exemple pour ChatGPT) :

1. Allez dans les **Paramètres** de votre application d'IA.
2. Recherchez les options **Applications** (Apps) puis **Paramètres Avancés** (Advanced settings).
​
![](https://downloads.intercomcdn.com/i/o/tarury57/2081851459/a61355b0b48ac68cae08d974149a/CleanShot-2B2026-02-19-2Bat-2B11_00_25-402x.png?expires=1788619500&signature=1d3991a6306066ead2a0ceced2734db05ba0e5389731282eeaf6e3298bfd1c0b&req=diAvF8F7nIVaUPMW1HO4zUj701uNCCRAlZFONt%2FH8ST2t4TnGdA%2FpHogd6Cg%0AXc7b%0A)

​
![](https://downloads.intercomcdn.com/i/o/tarury57/2081852776/0eb77580a1c829f1613fcc95d736/CleanShot+2026-02-19+at+11_03_11%402x.png?expires=1788619500&signature=4bace51aa704357f9042e3a4f0a94b0ebe749db5fc6b0b9c4e8f36393fc60062&req=diAvF8F7n4ZYX%2FMW1HO4zVGbArJKw53s%2FiAMxVhsBGi252fhFmJoSgxXsEXe%0AI2is%0A)

​*⚠️ Vous devez activer le mode développeur pour pouvoir créer une appli.* 
​
![](https://downloads.intercomcdn.com/i/o/tarury57/2081861761/07fd9d464fe41c9b7b87b7998452/CleanShot+2026-02-19+at+11_05_42%402x.png?expires=1788619500&signature=6c9ed3091d6f88355913cbd133652314ecb21d3576b6fd45e97354e651c00f2e&req=diAvF8F4nIZZWPMW1HO4zdQS0TTHPUa0nzNXoD6qacuQe4YIcXUeMUIneKFb%0AyFQI%0A)

​
3. Ajoutez une nouvelle connexion serveur en cliquant sur **"créer une appli"** :
- **Nom :** InterFast.
- **URL du serveur :** Collez le lien MCP récupéré à l'étape I.
- **Authentification :** Sélectionnez "Pas d'authentification" (le lien contient déjà votre clé sécurisée).
​
![](https://downloads.intercomcdn.com/i/o/tarury57/2081882632/27a98c6e1af7f9307c92144d6480/CleanShot+2026-02-19+at+11_15_56%402x.png?expires=1788619500&signature=e85de6a23bd88cfed03ced21fc802141e5e9ad0efce8ae050a8ad36c6a84430a&req=diAvF8F2n4dcW%2FMW1HO4zUanLAxN%2Bdeku58N5lkQS3mfMXbUEHQzZiSjEKeT%0A0jz8%0A)
4. Validez. La connexion est établie !
​
![](https://downloads.intercomcdn.com/i/o/tarury57/2081980298/229058eb4ab4150bf4f9dd1d7e7f/CleanShot+2026-02-19+at+11_52_16%402x.png?expires=1788619500&signature=797ef41037291f2d6aeb027155673997c7c634b9553321b44f98cac2ad7923a0&req=diAvF8B2nYNWUfMW1HO4ze2LWh65L01oDs1QgH0I5ceE9Z4tTTRaNN9c7NO5%0A8yed%0A)

### Étape 3 : Piloter InterFast par la discussion

Maintenant que le lien est fait, vous pouvez solliciter InterFast directement dans votre conversation :

1. Activez l'outil **InterFast** dans votre interface de chat.
2. Posez une question pour tester la connexion, par exemple : *"Que peux-tu faire avec InterFast ?"*.
3. L'IA vous confirmera ses capacités : rechercher des clients, consulter le planning, créer des devis, etc.

![](https://downloads.intercomcdn.com/i/o/tarury57/2081989517/b23ffc1322d0dc1f02bd62d83397/CleanShot+2026-02-19+at+11_57_24%402x.png?expires=1788619500&signature=e620a2b24983c6a653daa86958cdfd829427c9ac89ee9e4c02a7e859b9d91410&req=diAvF8B2lIReXvMW1HO4zeXshKyDW%2B%2FGXlh%2FZJ5IKPcseBUzw8mA%2B0St5A4%2B%0AAOnvgEkoOoh3Y1aa7ss%3D%0A)

> ⚠️ Les capacités du MCP sont pour l'instant limitées aux actions suivantes :
> 1. Rechercher un client
> 2. Créer un client (particulier, professionnel ou syndic)
> 3. Rechercher un devis
> 4. Consulter le détail d'un devis
> 5. Créer un devis (vierge ou depuis un modèle)
> 6. Modifier un devis
> 7. Lister les modèles de devis
> 8. Rechercher un article ou un ouvrage de la bibliothèque
> 9. Rechercher des chantiers
> 10. Consulter le planning
> 11. Planifier une intervention
> 12. Replanifier une intervention
> 13. Consulter les statistiques de facturation
> 14. Tester la connexion

### C. Cas pratique : Créer un devis complexe

Exemple 1 : Créer un devis à partir d'une description simple

L'IA est capable de transformer une description simple en un devis structuré dans votre logiciel :

- **Votre demande :** *"Crée un devis de climatisation multisplit pour le client [Nom]. Il y a 5 pièces à équiper. Propose une solution complète avec installation."*
​
- **L'action de l'IA :** Elle va rechercher le client dans votre base, structurer les sections (Fourniture, Pose, Mise en service) et vous demander validation.
​
- **Le résultat :** Une fois validé, le devis apparaît instantanément dans votre module **Ventes** sur InterFast.

![](https://downloads.intercomcdn.com/i/o/tarury57/2082000633/0e1dd361a993b0b16469916476ed/CleanShot+2026-02-19+at+12_03_22%402x.png?expires=1788619500&signature=6610cb4e556c9f3b33fa0af19e58bd5255b6ac05e875145807a24c98293ba6b4&req=diAvFMl%2BnYdcWvMW1HO4zTZnflSCq7n5KdHmMCrp0X8ZodYbyG3pq5%2B6rt%2Fe%0AnERgi0WV9L0AkoT7o%2Fc%3D%0A)

![](https://downloads.intercomcdn.com/i/o/tarury57/2082008299/3c67c7fbada85718d865411e574a/CleanShot+2026-02-19+at+12_06_03%402x.png?expires=1788619500&signature=17527033a207788ba69c66381abb0ac1403a73af2b348733f3820efe6443e88f&req=diAvFMl%2BlYNWUPMW1HO4zU01aWmevaN1LNmtOs9a04ylGzzttZGYPVgRGpYI%0AULouRkTv6Zg9M2KCLAM%3D%0A)


​

Exemple 2 : Créer un devis précis en interrogeant votre Bibliothèque

L'IA peut aller encore plus loin en chiffrant le devis avec vos propres références et tarifs :

- **Votre demande :** "*Crée un devis de climatisation multisplit pour le client [Nom]. Recherche les unités intérieures et extérieures dans ma bibliothèque et ajoute un forfait de pose.*"
- **L'action de l'IA :** Grâce à son outil de recherche paginée, elle va interroger et parcourir vos catalogues pour trouver vos références exactes. Elle structure ensuite les sections (Fourniture, Pose) avec vos vrais prix.
- **Le résultat :** Le devis apparaît instantanément dans votre module Ventes, chiffré précisément avec vos propres éléments de bibliothèque.

Exemple 3 : Créer un devis à partir d'un modèle pré-enregistré

Pour gagner un temps précieux, vous pouvez demander à l'IA de démarrer un chiffrage en se basant sur une trame que vous utilisez souvent :

- **Votre demande :** "Crée un devis pour le client [Nom du client] en utilisant mon modèle de devis nommé 'Contrat d'entretien PAC'."
- **L'action de l'IA :** L'IA va rechercher votre client ainsi que le modèle exact dans vos paramètres InterFast. Elle générera un nouveau devis au statut Brouillon reprenant toute la structure, les articles et les textes de votre modèle.

Exemple 4 : Modifier les lignes et sections d'un devis existant

Vous avez besoin de faire une correction rapide sans ouvrir l'éditeur de devis ? L'IA peut le faire pour vous :

- **Votre demande :** "Ouvre le devis D26-0123. Supprime la section 'Mise en service' et modifie la quantité de l'article 'Unité intérieure' pour en mettre 3."
- **L'action de l'IA :** Grâce à la connexion MCP, l'IA retrouve votre document et applique précisément vos modifications de quantités et suppressions de lignes en un instant.

## III. Différences entre API et MCP

InterFast propose également [une documentation API](https://developers.inter-fast.fr/). Bien que les deux technologies permettent de connecter InterFast à l'extérieur, elles ne répondent pas aux mêmes besoins. Voici comment choisir.

### A. L'API (Application Programming Interface)

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

## IV. Gagnez du temps au Bureau

Le connecteur IA transforme votre manière de travailler. Plus besoin de chercher chaque article un par un : décrivez votre projet, et laissez l'intelligence artificielle structurer vos documents techniques.

**Prêt à tester ?** Créez votre première clé API et demandez à votre assistant de vous lister vos interventions de demain !

## V. Questions fréquentes (FAQ)

L'IA prépare une structure de devis. Le document est créé au statut "Brouillon" : vous gardez toujours la main pour ajuster les tarifs et les articles avant l'envoi définitif.


Oui. La connexion utilise une clé API cryptée et privée. L'IA n'accède qu'aux informations nécessaires pour répondre à vos commandes spécifiques.

​
Oui, le protocole MCP est un standard. Vous pouvez utiliser le même lien serveur pour connecter InterFast à ChatGPT, Claude ou tout autre outil compatible.


Non, ils sont complémentaires.
- L'**API** est les "mains" du système : elle déplace des données d'un point A à un point B.
​
- Le **MCP** est le "cerveau" (ou plutôt les lunettes de l'IA) : il permet à une Intelligence Artificielle de comprendre ce qu'il y a dans votre dossier InterFast pour vous répondre.


C'est plus simple que l'API classique, mais cela demande une configuration initiale de votre Assistant IA (ChatGPT, Claude Desktop ou une autre interface compatible). Une fois connecté, vous parlez en langage naturel, sans code.


Non, absolument pas ! L'intelligence artificielle est directement connectée à votre Bibliothèque InterFast. Lorsque vous lui demandez de chiffrer un projet, elle utilise un outil de recherche avancée (recherche paginée) pour parcourir vos propres catalogues. Elle va ainsi puiser vos véritables articles et ouvrages, reprenant vos descriptions exactes et vos prix de vente configurés, pour construire le brouillon du devis.
​
​



Non. L'IA respecte strictement les règles de conformité d'InterFast et la loi anti-fraude à la TVA. Elle ne peut modifier (ajouter, supprimer ou changer des lignes) que sur des devis qui sont au statut "Brouillon". Si votre devis est déjà finalisé, envoyé ou accepté par votre client, l'action sera bloquée par sécurité.



Il vous suffit de lui indiquer le nom exact de votre modèle lors de votre demande (par exemple : *"Utilise mon modèle nommé 'Contrat Entretien PAC'"*). L'IA est connectée à vos paramètres d'entreprise via le MCP : elle ira chercher la bonne trame, avec vos textes et vos articles pré-enregistrés, pour générer votre nouveau brouillon.

Mis à jour le : 05/08/2026
