# 18 — Antigravity Windows Operating Contract

Remplace `14-ANTIGRAVITY-OPERATING-PACK.md` comme **contrat opérationnel
courant** — `14` reste lisible comme recherche/historique (`16` §1), mais
n'est plus la source d'exécution. Fondé sur les findings vérifiés de
`15-RED-TEAM-GATE.md` §H (documentation officielle Antigravity, 23/09/2026).

**Règle absolue (mission §16)** : une Rule Markdown ou un Skill ne constitue
**jamais** une barrière de sécurité. `Rules`/`Skills` = `CONSULTATIVE`, toujours.
Seuls `Hooks`/permissions/sandbox comptent comme garde-fous **s'ils sont
réellement vérifiés** sur la machine réelle — pas seulement documentés.

## 0. Deux chemins, aucun choisi à la place de l'utilisateur

### A. Windows natif

L'environnement actuel du projet. Sur cette voie, plusieurs mécanismes
critiques restent `NOT_VERIFIED` ou `NOT_DOCUMENTED` — voir §1. Nécessite les
PRE-FLIGHT de §3 avant tout `IMPLEMENT`.

### B. WSL (Windows Subsystem for Linux)

Changelog Antigravity v2.16.0 (22/09/2026) : section WSL ajoutée aux
Application Settings Windows, permettant de connecter une distribution WSL
installée. Sur cette voie, le chemin de code bascule vers le comportement
Linux : le moteur de permissions unifié (Deny/Ask/Allow) et le sandbox GA
s'appliquent réellement, au lieu du système Windows non unifié. **C'est la
voie que `15` B5 recommande**, mais elle exige une installation WSL
fonctionnelle et n'a pas non plus été vérifiée empiriquement sur ce projet.

**Aucun choix fait ici entre A et B** — les deux nécessitent une vérification
PRE-FLIGHT avant le premier `IMPLEMENT` (§3).

## 1. Statut par mécanisme (vocabulaire strict)

`DOCUMENTED` · `NOT_DOCUMENTED` · `EMPIRICALLY_VERIFIED` · `NOT_VERIFIED` ·
`ENFORCED` · `CONSULTATIVE`. Un mécanisme peut porter plusieurs statuts.

| Mécanisme | Statuts | Détail |
|---|---|---|
| **Project scope** | `DOCUMENTED`, `NOT_VERIFIED` | Nom et fonction confirmés (`15` H1). Périmètre du Project seul ne suffit pas — voir ligne suivante. |
| **Outside-of-folder access** (réglage Windows dédié, absent de `14`) | `DOCUMENTED`, `NOT_VERIFIED` | *« Always Allow / Always Ask / Always Deny »* — doit être mis à **Always Deny** explicitement. Non fait par défaut. |
| **Terminal command execution** | `DOCUMENTED`, `NOT_VERIFIED` | Windows = `Ask` par défaut (`15` H4, confirmé exact) — **mais** deux presets (« Full machine », « Turbo ») le désactivent ; `14` n'interdisait que Turbo. |
| **Sandbox** | `DOCUMENTED` (contesté — trois sources en désaccord, `15` H6), `NOT_VERIFIED`, **pas `ENFORCED` par défaut** | Aucun preset Windows ne l'active (`15` H5, confirmé exact). |
| **Worktree** | `DOCUMENTED`, `NOT_VERIFIED` sur Windows spécifiquement | Mécanisme réel, mais deux correctifs récents de worktrees orphelins signalent une instabilité (`15` H2). |
| **Rules** | `DOCUMENTED`, **`CONSULTATIVE`** | Jamais bloquant, quel que soit le contenu (`15` H8, B7). `AGENTS.md` n'est pas un nom officiel — c'est `GEMINI.md`. |
| **Skills** | `DOCUMENTED`, **`CONSULTATIVE`** | Idem Rules. Remplacent les Workflows, dépréciés le 01/11/2026 (`15` H9). |
| **Hooks** | `DOCUMENTED` (mécanisme), `NOT_DOCUMENTED` (exécution Windows — pas de mention PowerShell/`.bat`/`.ps1`/interpréteur), `NOT_VERIFIED` | **Seul levier programmatique réel** (`PreToolUse` peut `deny`/`force_ask`) — mais sa sémantique Windows n'est prouvée nulle part (`15` H10). |
| **Browser** | `DOCUMENTED`, `NOT_VERIFIED` sur Windows spécifiquement | Denylist serveur fail-closed confirmée (`15` H13), plateforme non précisée dans la doc. |
| **MCP** | `DOCUMENTED` (chemins, transports), `NOT_DOCUMENTED` (spécificités Windows — `cmd /c`, `npx.cmd`, échappement) | `15` H14. |
| **Implementation Plan artifact** | `DOCUMENTED` | L'agent génère un artefact de plan avant toute modification (`15` H11). Objet distinct des deux lignes suivantes — ne jamais l'appeler « Planning Mode ». |
| **Artifact review policy** | `DOCUMENTED`, `ENFORCED` **seulement si réglée pour exiger une approbation humaine explicite avant `IMPLEMENT`** ; **`CONSULTATIVE`/inopérante si réglée sur `Always Proceed`** | Contrôle si l'Implementation Plan artifact doit être approuvé par un humain. **Nom distinct de « Request Review »** — « Request Review » est un **preset de permissions** (terminal/fichiers, macOS/Linux ; sur Windows une valeur de *Terminal Command Auto Execution*), pas le nom de cette policy (`15` H12). |
| **Mode plan du CLI** (commande `plan`, `Shift+Tab`) | `DOCUMENTED` | Mode interactif du CLI, **objet distinct** de l'artifact review policy et du preset de permissions ci-dessus. `/planning` et `/fast` ont été supprimés en version 1.1.0 (`15` H12). |
| **Artifacts** (Walkthrough, diffs, enregistrements) | `DOCUMENTED`, `NOT_DOCUMENTED` (emplacement de stockage disque) | `15` H15 — ne peut donc pas être le seul artefact de reprise, voir `19`. |
| **Secrets** | `NOT_DOCUMENTED` (secrets applicatifs), **pas `ENFORCED`** par défaut | Seule protection native = sandbox, lui-même non activé par défaut (`15` H6/H17). Politique à construire, voir §2 SECRETS. |

## 2. Séquence opérationnelle

Pour chaque étape : `STATUS` (des mécanismes mobilisés), `HOW TO VERIFY`,
`FAILURE CONSEQUENCE`, `FALLBACK`.

### PRE-FLIGHT
- **STATUS** : voir checklist §3, bloquant.
- **HOW TO VERIFY** : chaque `PRE-FLIGHT-0X` passé en `PASS` avant toute autre étape.
- **FAILURE CONSEQUENCE** : sécurité du projet reposant sur des mécanismes non vérifiés — c'est l'erreur critique B5/B6 de `15`.
- **FALLBACK** : basculer sur le chemin B (WSL) si le chemin A échoue de façon répétée.

### PROJECT SCOPE
- **STATUS** : `DOCUMENTED`, `NOT_VERIFIED`.
- **HOW TO VERIFY** : le Project du dépôt applicatif ne référence jamais `supordo-os` ; `Outside-of-folder access = Always Deny` réglé et vérifié à l'écran.
- **FAILURE CONSEQUENCE** : violation directe de la première règle minimale du PO.
- **FALLBACK** : aucun — bloquant.

### GIT/WORKTREE
- **STATUS** : `DOCUMENTED`, `NOT_VERIFIED`.
- **HOW TO VERIFY** : `New Worktree Mode` sélectionné par défaut, testé sur un commit factice, vérifier l'absence de dossiers orphelins `.system_generated/worktrees` après merge/suppression.
- **FAILURE CONSEQUENCE** : écriture directe sur `main`, ou pollution du dépôt par des worktrees orphelins.
- **FALLBACK** : stratégie de branche manuelle (créer/merger la branche soi-même en dehors d'Antigravity) si le Worktree Mode échoue.

### PERMISSIONS
- **STATUS** : `DOCUMENTED`, `NOT_VERIFIED`.
- **HOW TO VERIFY** : preset `Default` ou `Request Review` actif (jamais `Turbo` ni `Full machine`), confirmé à l'écran avant toute session.
- **FAILURE CONSEQUENCE** : accès disque complet silencieux (`Full machine` a le même effet que Turbo sur l'accès hors dossier, `15` H7).
- **FALLBACK** : refuser de lancer `IMPLEMENT` tant que le preset n'est pas confirmé manuellement.

### SANDBOX
- **STATUS** : `NOT_VERIFIED`, pas `ENFORCED` par défaut.
- **HOW TO VERIFY** : activer manuellement (preset « Custom »), tenter une lecture de `.env` depuis l'agent, confirmer le blocage.
- **FAILURE CONSEQUENCE** : aucune protection réelle de `.env`/`~/.ssh` malgré la croyance inverse.
- **FALLBACK** : si le blocage n'est pas constaté, ne placer **aucun** secret réel dans le périmètre de lecture du Project (voir SECRETS).

### HOOKS
- **STATUS** : `NOT_DOCUMENTED` (Windows), `NOT_VERIFIED`.
- **HOW TO VERIFY** : PRE-FLIGHT dédié — écrire un hook `PreToolUse` trivial qui `deny` une commande anodine, l'exécuter, constater le refus réel.
- **FAILURE CONSEQUENCE** : si les hooks ne s'exécutent pas sous Windows, **le dispositif de sécurité entier doit être repensé** (`15` C10) — basculer sur WSL.
- **FALLBACK** : chemin B (WSL).

### RULES/SKILLS
- **STATUS** : `CONSULTATIVE`, toujours.
- **HOW TO VERIFY** : sans objet — aucune vérification ne les rendra bloquantes.
- **FAILURE CONSEQUENCE** : traiter une Rule comme une garantie de sécurité est l'erreur `15` B7 exacte.
- **FALLBACK** : déplacer toute garantie critique vers un Hook (enforcé) ou une étape humaine (`AUDIT`, `MERGE`).

### MCP
- **STATUS** : `NOT_DOCUMENTED` (Windows), `NOT_VERIFIED`.
- **HOW TO VERIFY** : connexion au serveur MCP Supabase **DEV uniquement**, confirmer qu'aucun credential de production n'est présent dans `mcp_config.json`.
- **FAILURE CONSEQUENCE** : échec de connexion silencieux (mode d'échec MCP classique sous Windows) ou, pire, accès accidentel à un projet Supabase non prévu.
- **FALLBACK** : accès Supabase manuel (CLI/dashboard) par un humain si MCP échoue.

### BROWSER
- **STATUS** : `DOCUMENTED`, `NOT_VERIFIED` sur Windows.
- **HOW TO VERIFY** : capture d'écran réelle obtenue pour une tranche à impact UI, profil Chrome séparé confirmé.
- **FAILURE CONSEQUENCE** : preuve de "page visible" confondue avec preuve de comportement (interdit par `13`).
- **FALLBACK** : capture manuelle par un humain si le Browser Subagent échoue.

### SECRETS
- **STATUS** : `NOT_DOCUMENTED`, pas `ENFORCED`.
- **HOW TO VERIFY** : scan manuel du diff avant tout commit/write pour motifs de clé/secret ; clé service-role Supabase jamais présente dans un fichier lisible par l'agent.
- **FAILURE CONSEQUENCE** : exposition d'un secret réel — le vecteur qui compromettrait toutes les données de tous les tenants simultanément (`15` B6).
- **FALLBACK** : injection par variable d'environnement au niveau du déploiement, hors du périmètre de lecture du Project, systématiquement — ne jamais dépendre du sandbox seul.

### DATA GOVERNANCE
- **STATUS** : `DOCUMENTED` ici (§0bis de `17`), minimal.
- **HOW TO VERIFY** : toute donnée en environnement DEV est synthétique ; confirmer qu'aucune donnée de tenant pilote réel n'y transite.
- **FAILURE CONSEQUENCE** : les Interactions Antigravity peuvent être vues/utilisées par des employés/contractants Google (`15` H18/C11) — une donnée réelle de pilote y serait exposée.
- **FALLBACK** : gouvernance avancée (télémétrie off, offre Enterprise) — `OPEN`, non bloquante pour démarrer, mais à statuer avant tout usage avec de vraies données.

### PLAN REVIEW
- **STATUS** : `ENFORCED` seulement si l'**artifact review policy** (distincte du preset de permissions « Request Review » et du mode `plan` du CLI, voir §1) est explicitement réglée pour exiger une approbation humaine, jamais `Always Proceed`.
- **HOW TO VERIFY** : réglage de l'artifact review policy confirmé à l'écran (pas supposé par défaut) — vérifier séparément (1) l'Implementation Plan artifact est bien généré, (2) l'artifact review policy exige une approbation, (3) le preset de permissions terminal/fichiers est correctement réglé (§ PERMISSIONS ci-dessus). Trois vérifications distinctes, jamais fusionnées (`15` H12).
- **FAILURE CONSEQUENCE** : un plan approuvé sans revue réelle équivaut à `Always Proceed`, interdit.
- **FALLBACK** : aucun — bloquant, pas de fallback accepté sur ce point.

### IMPLEMENT
- **STATUS** : dépend de toutes les étapes précédentes en `PASS`.
- **HOW TO VERIFY** : `New Worktree Mode` actif, permissions confirmées, hooks vérifiés.
- **FAILURE CONSEQUENCE** : toute dérive de `12`/`17` (simulation présentée comme réelle, écriture hors périmètre).
- **FALLBACK** : arrêt immédiat de la tranche, retour à `PLAN`.

### VERIFY
- **STATUS** : reprend `13` intégralement (jamais build/page/200 comme preuve).
- **HOW TO VERIFY** : tests automatisés exécutés, capture Browser Subagent pour tout impact UI.
- **FAILURE CONSEQUENCE** : déclaration `REAL` non vérifiée (interdiction explicite du PO).
- **FALLBACK** : déclarer `PROTOTYPE`/`NOT_IMPLEMENTED` plutôt que de simuler.

### AUDIT
- **STATUS** : `NOT_VERIFIED` (Teamwork), sinon `DOCUMENTED`.
- **HOW TO VERIFY** : subagent auditeur **sans contexte partagé** avec l'implémenteur (agent frais, pas un fork). Teamwork/`Critic` (`-preview`) utilisable en complément seulement, jamais comme unique garantie — introuvable dans la documentation actuelle en dehors de son propre nom (`15` H16 : `/docs/subagents` ne documente que trois subagents intégrés — Research, Browser, Self).
- **FAILURE CONSEQUENCE** : audit biaisé par le contexte de l'implémenteur.
- **FALLBACK** : audit humain si aucun agent frais indépendant n'est disponible.

### MERGE
- **STATUS** : `ENFORCED` par discipline humaine uniquement — aucune automatisation trouvée (`15` H15 : pas de PR automatique documentée).
- **HOW TO VERIFY** : geste humain explicite, jamais un merge déclenché par l'agent lui-même.
- **FAILURE CONSEQUENCE** : écriture directe sur `main`.
- **FALLBACK** : aucun — c'est la dernière ligne de défense, non négociable.

## 3. Checklist PRE-FLIGHT

**Le premier `IMPLEMENT` est interdit tant que les PRE-FLIGHT bloquants ne
sont pas `PASS`.**

| # | Test | Bloquant ? | PASS/FAIL |
|---|---|---|---|
| PRE-FLIGHT-01 | `Outside-of-folder access` réglé sur `Always Deny`, vérifié à l'écran | Oui | à faire |
| PRE-FLIGHT-02 | Preset permissions confirmé `Default`/`Request Review`, jamais `Turbo`/`Full machine` | Oui | à faire |
| PRE-FLIGHT-03 | `New Worktree Mode` testé sur un commit factice, aucun dossier orphelin après | Oui | à faire |
| PRE-FLIGHT-04 | Hook `PreToolUse` trivial exécuté, refus constaté réellement | Oui | à faire |
| PRE-FLIGHT-05 | Sandbox testé (tentative de lecture `.env`), résultat constaté quel qu'il soit | Oui | à faire |
| PRE-FLIGHT-06 | Artifact review policy réglée pour exiger une approbation humaine (jamais `Always Proceed`), vérifiée séparément du preset de permissions « Request Review » et du mode `plan` du CLI | Oui | à faire |
| PRE-FLIGHT-07 | Serveur MCP Supabase pointant uniquement vers DEV, aucun credential prod présent | Oui | à faire |
| PRE-FLIGHT-08 | Aucun secret réel dans le périmètre de lecture du Project | Oui | à faire |
| PRE-FLIGHT-09 | Données DEV confirmées synthétiques, aucune donnée de tenant pilote réel | Oui | à faire |
| PRE-FLIGHT-10 | Browser Subagent testé, capture obtenue avec succès | Non (fallback humain existe) | à faire |
| PRE-FLIGHT-11 | Emplacement de stockage des Artifacts/Walkthrough identifié manuellement (non documenté officiellement) | Non | à faire |

Chaque `PRE-FLIGHT` bloquant en `FAIL` interdit `IMPLEMENT` sur **toute**
tranche — c'est un `GLOBAL_BUILD_GATE` (`17` §0), pas un `SLICE_GATE`.

## 4. Ce que ce document ne fait pas

Ne configure aucun projet Antigravity réel. Ne teste rien lui-même — les
PRE-FLIGHT ci-dessus sont à exécuter par un humain avant le premier usage. Ne
choisit pas entre le chemin A (Windows natif) et B (WSL). Reste à revalider
si Antigravity évolue après la date de cette mission (voir avertissement de
fraîcheur déjà posé par `14`, toujours valable).
