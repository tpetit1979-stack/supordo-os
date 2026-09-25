# 18 — Antigravity Windows Operating Contract

Remplace `14-ANTIGRAVITY-OPERATING-PACK.md` comme **contrat opérationnel
courant** — `14` reste lisible comme recherche/historique (`16` §1), mais
n'est plus la source d'exécution. Fondé sur les findings vérifiés de
`15-RED-TEAM-GATE.md` §H (documentation officielle Antigravity, 23/09/2026),
**complété et corrigé le 25/09/2026** par une seconde vérification directe de
la documentation officielle (liste des sources en §6). Aucune ligne du 23/09
n'a été réécrite sans citation de la source qui la corrige — voir marquage
`CORRECTION 25/09` inline ci-dessous.

**Règle absolue (mission §16)** : une Rule Markdown ou un Skill ne constitue
**jamais** une barrière de sécurité. `Rules`/`Skills` = `CONSULTATIVE`, toujours.
Seuls `Hooks`/permissions/sandbox comptent comme garde-fous **s'ils sont
réellement vérifiés** sur la machine réelle — pas seulement documentés.

## -1. Statut de ce document et hiérarchie des sources

Ce document est un **TOOL OPERATING CONTRACT** pour l'usage de Google
Antigravity dans l'écosystème SUPORDO. **Il ne définit pas le produit.** Il
doit rester utilisable quel que soit le dépôt sur lequel Antigravity
travaille — `supordo-app` (implémentation), une migration Supabase liée à
l'application, des tests, de la QA UX/navigateur, ou de la documentation
d'implémentation liée à une tranche.

```
SUPORDO-OS   = source de vérité produit / architecture / décisions (ce dépôt)
SUPORDO-APP  = dépôt d'implémentation ACTIF
               (C:\Users\devfi\supordo-app, distinct de supordo-os)
AGENTS.md    = contrat agent neutre, à la racine de supordo-app
18 (ce doc)  = adapter opérationnel spécifique à Google Antigravity
20           = contrat UX applicatif (tool-agnostic)
```

**`CORRECTION 25/09` (deuxième passe)** : la version précédente de cette
section décrivait `supordo-app` comme « futur » et `AGENTS.md` comme
« n'existe pas encore ». Faux sur les deux points — vérifié par recherche de
fichier directe le 25/09/2026, périmètre explicite :

- **`C:\Users\devfi\supordo-os`** (ce dépôt) : aucun `AGENTS.md` ni
  `GEMINI.md` trouvé à la racine ni ailleurs dans l'arbre versionné.
  Cohérent avec son statut de dépôt documentaire — `supordo-os` n'a jamais eu
  vocation à porter un contrat agent d'exécution.
- **`C:\Users\devfi\supordo-app`** : `AGENTS.md` **existe** à la racine,
  recréé le 2026-09-24 (`git log --diff-filter=A -- AGENTS.md` → `22d2969`).
  Le fichier documente lui-même qu'il a été *recréé* ce jour-là après un audit ayant
  constaté son absence (avec `CLAUDE.md`, `README.md`,
  `TECHNICAL-BASELINE.md`) alors que trois tranches étaient déjà livrées —
  un précédent direct pour la discipline PRE-FLIGHT de ce document. Son
  contenu réel confirme déjà la hiérarchie ci-dessus (`supordo-os` cité
  comme « dépôt documentaire strictement en lecture seule ») et interdit
  explicitement toute modification de `supordo-os` depuis `supordo-app`.
  Seules des copies vendor sans rapport (`node_modules/@supabase/*/AGENTS.md`)
  existent en plus — bruit de dépendances npm, pas une convention SUPORDO.

Ne jamais généraliser au-delà de ces deux dépôts sans re-vérifier — « ni
ailleurs » n'est plus une affirmation de ce document. `AGENTS.md` est
retenu **parce qu'il est déjà la convention neutre effectivement en usage
dans `supordo-app`, et qu'Antigravity la supporte officiellement au même
titre que `GEMINI.md`** (§1, ligne `Rules`), **pas parce que Google
l'impose**. Ce document (`18`) ne peut jamais servir à inventer ou
remplacer une décision produit absente du corpus `16`-`20` — il documente
uniquement *comment* exécuter ces décisions avec l'outil, jamais *ce qu'*
elles sont.

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
| **Terminal command execution** | `DOCUMENTED`, `NOT_VERIFIED` | Windows = `Ask` par défaut (`15` H4, confirmé exact) — **mais** deux presets (« Full machine », « Turbo ») le désactivent ; `14` n'interdisait que Turbo. **Précision 25/09** (`antigravity.google/docs/permissions/`, `/docs/cli/reference/`) : clé `toolPermission` du `settings.json` — valeurs `request-review` (défaut), `proceed-in-sandbox`, `always-proceed`, `strict`. `always-proceed` = équivalent config du preset Turbo, **interdit** pour SUPORDO. Le flag CLI `--dangerously-skip-permissions` existe et contourne `/permissions` (« Tool permission rules... continue to govern shell commands across all execution modes » — sauf ce flag) : la doc établit qu'il auto-approuve les tool calls / court-circuite la couche de permissions elle-même. **`HOOK_BYPASS_WITH_DANGEROUS_FLAG = NOT_VERIFIED`** — la documentation ne démontre pas que ce flag désactive ou contourne spécifiquement les Hooks `PreToolUse` (mécanisme distinct des permissions, §1 ligne `Hooks`) ; ne pas l'affirmer. **L'interdiction SUPORDO du flag reste entière** (il bypasse au minimum les permissions, ce qui suffit à l'interdire), mais **ne pas la justifier par un effet sur les Hooks non prouvé**. |
| **Sandbox** | `DOCUMENTED` (**contesté — quatre sources en désaccord désormais**, `15` H6 + nouvelle contradiction ci-dessous), `NOT_VERIFIED`, **pas `ENFORCED` par défaut** | Aucun preset Windows ne l'active (`15` H5, confirmé exact). **`CORRECTION 25/09` (deuxième passe) — ne pas trancher silencieusement** : `DOCUMENTED_CURRENT_CONFLICT` — source `antigravity.google/docs/sandbox/` (25/09/2026) : *« Antigravity's updated permission system is currently available on macOS and Linux, where the sandbox is enabled by default »* ; source `antigravity.google/docs/settings` (25/09/2026) : *« Sandboxing is currently disabled by default, but this may change in future releases. It is supported on macOS and Linux »*. Les deux pages sont datées identiquement, aucune ne se présente comme périmée. Hypothèse non confirmée : `/sandbox/` pourrait décrire le « permission system » (Desktop 2.0) et `/settings` un toggle IDE distinct — **non vérifié, ne pas supposer**. `OPERATIONAL_RULE` : l'état réellement observé/configuré sur la machine prévaut sur les deux pages — c'est tout l'objet de `PRE-FLIGHT-05`, qui reste `NOT_VERIFIED` et **plus critique qu'avant** cette découverte. Windows = « previous behavior », désactivé par défaut, seul point non contesté entre les sources. Bascule via `settings.json` (`enableTerminalSandbox: true`, `toolPermission: "proceed-in-sandbox"`) ou flag CLI `--sandbox`. |
| **Worktree** | `DOCUMENTED`, `NOT_VERIFIED` sur Windows spécifiquement | Mécanisme réel, mais deux correctifs récents de worktrees orphelins signalent une instabilité (`15` H2). |
| **Rules** | `DOCUMENTED`, **`CONSULTATIVE`** | Jamais bloquant, quel que soit le contenu (`15` H8, B7). **`CORRECTION 25/09`** : `15` H8 affirmait que `AGENTS.md` n'était pas un nom officiel. Faux — `antigravity.google/docs/cli/best-practices/` (vérifié 25/09/2026) : *« Create a `GEMINI.md` or `AGENTS.md` file at your workspace root »* — les deux noms sont documentés comme équivalents, aucune précédence indiquée entre eux. `AGENTS.md` est donc officiellement supporté ; SUPORDO le retient comme contrat neutre pour cette raison, pas par défaut faute d'alternative (voir §-1). N'implémente aucune barrière — reste `CONSULTATIVE` comme toute Rule. |
| **Skills** | `DOCUMENTED`, **`CONSULTATIVE`** | Idem Rules. Remplacent les Workflows, dépréciés le 01/11/2026 (`15` H9) — non contredit par la recherche du 25/09. |
| **Execution modes (CLI)** | `DOCUMENTED`, `NOT_VERIFIED` | **`CORRECTION 25/09`** : aucun mode nommé « Fast Mode » n'existe dans la documentation actuelle (`antigravity.google/docs/cli/modes/`). Trois modes réels, cycle via `Shift+Tab` : **Default** (pause sur chaque écriture, diff + `y`/`n`), **Accept-Edits** (auto-approuve toute écriture fichier, hérité par les subagents), **Plan** (préfixe `/plan`, outils lecture seule, plan présenté avant écriture). L'équivalent fonctionnel le plus proche de ce que la mission appelle « Fast Mode » est **Accept-Edits**, pas un mode dédié. Les permissions `command` (§ ci-dessous) restent gouvernées séparément dans tous les modes. |
| **Hooks** | `DOCUMENTED` (mécanisme), `NOT_DOCUMENTED` (exécution Windows — pas de mention PowerShell/`.bat`/`.ps1`/interpréteur), `NOT_VERIFIED` | **Seul levier programmatique réel** (`PreToolUse` peut `deny`/`force_ask`) — mais sa sémantique Windows n'est prouvée nulle part (`15` H10). **Confirmé 25/09** (`antigravity.google/docs/hooks`), inchangé : 5 événements (`PreToolUse`/`PostToolUse`/`PreInvocation`/`PostInvocation`/`Stop`), `PreToolUse` renvoie `allow`/`deny`/`ask`/`force_ask`/`deny_unless_prior_grant` + `reason` optionnel. Chemins confirmés : `.agents/hooks.json` (workspace), `~/.gemini/config/hooks.json` (global) — l'exécution Windows du script de commande reste `NOT_DOCUMENTED`, statut inchangé. |
| **Browser** | `DOCUMENTED`, `NOT_VERIFIED` sur Windows spécifiquement | Denylist serveur fail-closed confirmée (`15` H13), plateforme non précisée dans la doc. **Confirmé 25/09** (`antigravity.google/docs/ide/browser/`), inchangé : modèle deux couches (denylist serveur + allowlist locale), profil Chrome séparé de l'utilisateur, captures + enregistrements vidéo. Toggle de désactivation complète disponible (User Settings → Browser Tools) si le Browser Subagent doit être neutralisé en attendant vérification Windows. Statut Windows toujours non détaillé dans la doc — `NOT_VERIFIED` inchangé. |
| **MCP** | `DOCUMENTED` (chemins, transports), `NOT_DOCUMENTED` (spécificités Windows — `cmd /c`, `npx.cmd`, échappement) | `15` H14, non contredit par la recherche du 25/09. |
| **Implementation Plan artifact** | `DOCUMENTED` | L'agent génère un artefact de plan avant toute modification (`15` H11). Objet distinct des deux lignes suivantes — ne jamais l'appeler « Planning Mode ». **Précision 25/09** : produit par le mode d'exécution **Plan** (`/plan`, voir ligne `Execution modes` ci-dessus) ou par la commande `/plan` explicite ; `/goal` (exécution autonome jusqu'à complétion) et `/grill-me` (questions de clarification avant d'implémenter) restent tous deux `DOCUMENTED` et actifs (`antigravity.google/docs/slash-commands/`, 25/09/2026) — `/planning` et `/fast` restent absents de toute doc actuelle, cohérent avec `15` H12 (suppression 1.1.0, non contredite). |
| **Subagents (built-in)** | `DOCUMENTED`, `NOT_VERIFIED` | **Ajout 25/09** (`antigravity.google/docs/subagents/`) : trois subagents intégrés nommés — **Research** (exploration codebase), **Browser** (voir ligne Browser), **Self** (clone exact de l'agent appelant, mêmes outils). Subagents custom = fichier Markdown + frontmatter YAML, `.agents/agents/<nom>.md` (workspace) ou `~/.gemini/config/agents/<nom>.md` (global), champ `tools` limitant l'accès. **Point de vigilance pour `12` §15/mission §7** : un subagent custom **hérite par défaut des permissions du parent** (accès terminal, lecture/écriture) — un « subagent auditeur read-only » n'est **pas** read-only par défaut ; le lecture-seule doit être déclaré explicitement dans le champ `tools` du frontmatter (exclure `write_file`/`command`), jamais supposé du seul nom ou de la description du subagent. |
| **Plugins** | `DOCUMENTED`, `NOT_VERIFIED` | **Ajout 25/09** (`antigravity.google/docs/plugins/`) : empaquette Skills + Subagents + Rules + config MCP + Hooks en un seul artefact installable. Chemins : `.agents/plugins/` (workspace), `~/.gemini/config/plugins/` (global), `~/.gemini/antigravity-cli/plugins/` (CLI). Doc officielle elle-même déconseille pour du one-off — cohérent avec mission §9 : pas d'industrialisation avant qu'un workflow réutilisable stable existe réellement. |
| **Artifact review policy** | `DOCUMENTED`, `ENFORCED` **seulement si réglée pour exiger une approbation humaine explicite avant `IMPLEMENT`** ; **`CONSULTATIVE`/inopérante si réglée sur `Always Proceed`** | Contrôle si l'Implementation Plan artifact doit être approuvé par un humain. **Nom distinct de « Request Review »** — « Request Review » est un **preset de permissions** (terminal/fichiers, macOS/Linux ; sur Windows une valeur de *Terminal Command Auto Execution*), pas le nom de cette policy (`15` H12). **Précision 25/09** (`antigravity.google/docs/cli/reference/`, `/docs/settings`) : clé `artifactReviewPolicy` du `settings.json`, défaut `"asks-for-review"`, **trois valeurs possibles** — `asks-for-review` (=Request Review), `agent-decides` (**nouvelle option intermédiaire, non couverte par `15` H12** — l'agent choisit seul quand demander une revue, traiter comme équivalent à `always-proceed` pour SUPORDO : interdite), `always-proceed` (interdite, inchangé). |
| **Mode plan du CLI** (commande `/plan`, `Shift+Tab`) | `DOCUMENTED` | Mode interactif du CLI, **objet distinct** de l'artifact review policy et du preset de permissions ci-dessus. `/planning` et `/fast` ont été supprimés en version 1.1.0 (`15` H12) — **confirmé toujours absent** de `/docs/slash-commands/` et `/docs/cli/modes/` au 25/09/2026. `/plan` (raccourci du mode Plan) reste `DOCUMENTED` et actif, ajouté en v2.17.0 selon le changelog officiel (`antigravity.google/changelog/`, 25/09/2026) — cohérent, pas une réintroduction de `/planning`. |
| **Artifacts** (Walkthrough, diffs, enregistrements) | `DOCUMENTED`, `NOT_DOCUMENTED` (emplacement de stockage disque) | `15` H15 — ne peut donc pas être le seul artefact de reprise, voir `19`. **Confirmé 25/09** (`antigravity.google/docs/artifacts`) : la doc officielle elle-même ne tranche pas si les Artifacts remplacent la documentation versionnée d'un dépôt — **position SUPORDO explicite, non déléguée à la doc Google** : un Artifact Antigravity (Implementation Plan, Walkthrough, diff) est une preuve de session, jamais un substitut à `19-SLICE-HANDOFF-TEMPLATE.md` versionné dans le dépôt. Toute tranche doit laisser une preuve dans le dépôt même si l'Artifact disparaît. CLI : révision via `Ctrl+R` (Artifact Picker), actions groupées `Shift+A`/`Shift+R` — détail pratique, sans incidence sur ce principe. |
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
- **HOW TO VERIFY** : preset `Default` ou `Request Review` actif (jamais `Turbo` ni `Full machine`), confirmé à l'écran avant toute session. Sur CLI : `toolPermission` du `settings.json` réglé sur `request-review` ou `proceed-in-sandbox` (jamais `always-proceed`/`strict` mal compris comme permissif), **et confirmer que `--dangerously-skip-permissions` n'est jamais utilisé** dans un script ou alias de lancement (§1, ligne `Terminal command execution`, ajout 25/09).
- **FAILURE CONSEQUENCE** : accès disque complet silencieux (`Full machine` a le même effet que Turbo sur l'accès hors dossier, `15` H7) ; `--dangerously-skip-permissions` contourne au minimum la couche de permissions elle-même (`HOOK_BYPASS_WITH_DANGEROUS_FLAG = NOT_VERIFIED` — ne pas présumer un effet sur les Hooks `PreToolUse`, non démontré par la doc, §1 ligne `Terminal command execution`).
- **FALLBACK** : refuser de lancer `IMPLEMENT` tant que le preset n'est pas confirmé manuellement.

### SANDBOX
- **STATUS** : `NOT_VERIFIED`, pas `ENFORCED` par défaut, **`DOCUMENTED_CURRENT_CONFLICT`** entre deux pages officielles sur l'état par défaut macOS/Linux (§1, ligne `Sandbox` — non applicable à Windows, seule plateforme de ce projet, où les deux sources s'accordent sur « désactivé par défaut »).
- **HOW TO VERIFY** : activer manuellement (preset « Custom »), tenter une lecture de `.env` depuis l'agent, confirmer le blocage. **`OBSERVED_RUNTIME_WINDOWS` reste à renseigner** — aucun test réel effectué sur cette machine à ce jour ; c'est ce test, pas la lecture d'une page de doc, qui doit trancher `PRE-FLIGHT-05`.
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

### SUBAGENTS
- **STATUS** : `DOCUMENTED` (mécanisme et 3 subagents intégrés — §1), `NOT_VERIFIED` (comportement réel de l'héritage de permissions).
- **HOW TO VERIFY** : avant de déclarer un subagent custom « read-only » (ex. auditeur RLS, revue UX), inspecter son frontmatter et confirmer que le champ `tools` **exclut explicitement** `write_file`/`command` — ne jamais se fier au nom ou à la description du subagent (§1, ligne `Subagents`, ajout 25/09). `WHEN_TO_USE` : recherche indépendante multi-fichiers, audit RLS, revue UX, exécution parallèle de tests. `WHEN_NOT_TO_USE` : tâche courte qu'un humain peut vérifier directement, ou tâche nécessitant le contexte de planification de l'implémenteur (voir AUDIT ci-dessous — un subagent d'audit doit être **frais**, jamais un fork). `EXPECTED_OUTPUT` : rapport structuré, jamais une modification directe si `WRITE_ACCESS` n'a pas été explicitement accordé.
- **FAILURE CONSEQUENCE** : un « subagent auditeur » qui hérite silencieusement des droits d'écriture du parent peut modifier ce qu'il est censé auditer.
- **FALLBACK** : restreindre via un Hook `PreToolUse` dédié au subagent si le champ `tools` s'avère insuffisant en pratique.

### BROWSER
- **STATUS** : `DOCUMENTED`, `NOT_VERIFIED` sur Windows.
- **HOW TO VERIFY** : capture d'écran réelle obtenue pour une tranche à impact UI, profil Chrome séparé confirmé.
- **FAILURE CONSEQUENCE** : preuve de "page visible" confondue avec preuve de comportement (interdit par `13`).
- **FALLBACK** : capture manuelle par un humain si le Browser Subagent échoue.
- **Relation à `20`** : le Browser Subagent est l'outil d'exécution de la QA UX (screenshots, enregistrements, responsive) ; les *critères* de ce qui doit être vérifié (continuité de contexte, anti-CRUD, anatomie d'écran, responsive, navigation) restent définis par `20-APPLICATION-UX-ARCHITECTURE-CONTRACT.md`, jamais par ce document. `18` ne définit aucun critère UX, seulement le mécanisme pour les vérifier.

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
- **STATUS** : `ENFORCED` seulement si l'**artifact review policy** (distincte du preset de permissions « Request Review » et du mode `plan` du CLI, voir §1) est explicitement réglée sur `asks-for-review`, jamais `agent-decides` ni `always-proceed`.
- **HOW TO VERIFY** : réglage `artifactReviewPolicy: "asks-for-review"` confirmé à l'écran (pas supposé par défaut, ajout 25/09 : le défaut officiel l'est effectivement, mais à re-vérifier car un défaut documenté peut changer entre versions) — vérifier séparément (1) l'Implementation Plan artifact est bien généré, (2) l'artifact review policy exige une approbation, (3) le preset de permissions terminal/fichiers est correctement réglé (§ PERMISSIONS ci-dessus). Trois vérifications distinctes, jamais fusionnées (`15` H12).
- **FAILURE CONSEQUENCE** : un plan approuvé sans revue réelle équivaut à `always-proceed`, interdit — `agent-decides` produit le même risque de façon moins visible (l'agent peut simplement ne jamais choisir de demander une revue).
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
| PRE-FLIGHT-12 | Fichier de configuration effectivement lu par cette installation identifié empiriquement — la doc officielle cite `~/.gemini/antigravity-cli/settings.json` (permissions/sandbox) **et** un `/.gemini/config.json` par dépôt introduit en v2.17.0 qui remplace `.agents/settings.json` ; ne pas supposer qu'un chemin cité par `14` reste lu sans le vérifier | Oui | à faire |
| PRE-FLIGHT-13 | `--dangerously-skip-permissions` confirmé absent de tout script/alias de lancement Antigravity utilisé pour ce projet | Oui | à faire |
| PRE-FLIGHT-14 | Pour tout subagent custom déclaré « read-only » (ex. auditeur), frontmatter `tools` inspecté et confirmé sans `write_file`/`command` | Oui (si un tel subagent est utilisé) | à faire |

Chaque `PRE-FLIGHT` bloquant en `FAIL` interdit `IMPLEMENT` sur **toute**
tranche — c'est un `GLOBAL_BUILD_GATE` (`17` §0), pas un `SLICE_GATE`.

## 4. Ce que ce document ne fait pas

Ne configure aucun projet Antigravity réel. Ne teste rien lui-même — les
PRE-FLIGHT ci-dessus sont à exécuter par un humain avant le premier usage. Ne
choisit pas entre le chemin A (Windows natif) et B (WSL). Reste à revalider
si Antigravity évolue après la date de cette mission (voir avertissement de
fraîcheur déjà posé par `14`, toujours valable). Ne crée, à l'occasion de sa
mise à jour du 25/09/2026, **aucun** subagent permanent, hook, plugin, skill,
`GEMINI.md`, ni configuration de permissions réelle — uniquement de la
documentation et des usages potentiels identifiés (§1, §2).

## 5. Périmètre garanti par `20`, jamais par ce document

`20-APPLICATION-UX-ARCHITECTURE-CONTRACT.md` est le contrat UX applicatif —
tool-agnostic. `18` ne redéfinit aucun critère UX ; il documente uniquement
le mécanisme Antigravity (Browser Subagent, Artifacts, Walkthrough) qui sert
à vérifier que `20` est respecté. En cas de conflit apparent entre une
capacité Antigravity et une exigence de `20`, `20` prévaut — `18` s'adapte à
`20`, jamais l'inverse.

## 6. Sources consultées pour la mise à jour du 25/09/2026

Toutes vérifiées par lecture directe le 25/09/2026 (`LAST_VERIFIED_DATE`).
`RUNTIME_BEHAVIOR_TAKES_PRECEDENCE_WHEN_DOCS_CONFLICT = YES` — une
observation réelle sur cette machine prévaut toujours sur ce qui suit.

| Source | Apport principal à cette mise à jour |
|---|---|
| `antigravity.google/docs/cli/best-practices/` | `AGENTS.md`/`GEMINI.md` officiellement équivalents — corrige `15` H8 |
| `antigravity.google/docs/permissions/` | Presets Default/Request Review/Turbo, six actions couvertes, spécificité Windows `unsandboxed` ; `--dangerously-skip-permissions` documenté comme bypass des permissions, **pas** des Hooks (`HOOK_BYPASS_WITH_DANGEROUS_FLAG = NOT_VERIFIED`) |
| `antigravity.google/docs/sandbox/` | Quote exacte : *« sandbox is enabled by default »* sur macOS/Linux — **contredit par `/docs/settings` ci-dessous, `DOCUMENTED_CURRENT_CONFLICT`, non tranché** ; Windows non `ENFORCED` par défaut, seul point d'accord entre les deux pages |
| `antigravity.google/docs/hooks` | Cinq événements, valeurs de retour `PreToolUse`, chemins `.agents/hooks.json` |
| `antigravity.google/docs/subagents/` | Trois subagents intégrés nommés, format custom, héritage de permissions |
| `antigravity.google/docs/cli/reference/` | Clés `settings.json` (`toolPermission`, `artifactReviewPolicy`), 40+ commandes slash |
| `antigravity.google/docs/settings` | Confirme les mêmes clés côté Desktop/IDE, `allowNonWorkspaceAccess` ; quote exacte : *« Sandboxing is currently disabled by default... supported on macOS and Linux »* — **contredit `/docs/sandbox/` ci-dessus**, voir §1 ligne `Sandbox` |
| Recherche fichier locale (`C:\Users\devfi\supordo-os`, `C:\Users\devfi\supordo-app`) | `AGENTS.md` absent de `supordo-os` ; **présent** à la racine de `supordo-app` (committé 24/09/2026) — voir §-1, corrige la version précédente de cette section |
| `antigravity.google/docs/artifacts` | Rôle des Artifacts, silence officiel sur leur statut face à la doc versionnée (comblé par une position SUPORDO explicite) |
| `antigravity.google/docs/artifact-review/` | Distinction confirmée entre artifact review policy, preset permissions, mode plan CLI |
| `www.antigravity.google/docs/walkthrough` | Contenu et audience du Walkthrough ; persistance disque toujours non documentée |
| `antigravity.google/docs/cli/artifacts/` | UX pratique CLI (`Ctrl+R`, Artifact Picker, `Shift+A`/`Shift+R`) |
| `antigravity.google/docs/home` | Confirmation des 4 surfaces (Desktop/CLI/IDE/SDK), lien changelog |
| `antigravity.google/changelog/` | Version observée **2.17.0** (~22-23/09/2026) ; WSL ajouté en 2.16.0 ; `/plan` ajouté en 2.17.0 ; `.agents/settings.json` déprécié au profit de `/.gemini/config.json` |
| `antigravity.google/docs/slash-commands/` | `/plan`, `/goal`, `/grill-me` actifs ; `/planning`/`/fast` absents (cohérent `15` H12) |
| `antigravity.google/docs/cli/modes/` | Aucun « Fast Mode » nommé — modes réels : Default / Accept-Edits / Plan |
| `antigravity.google/docs/ide/browser/` | Modèle deux couches denylist/allowlist confirmé, toggle de désactivation complète |
| `antigravity.google/docs/plugins/` | Chemins d'installation, position officielle contre l'industrialisation prématurée |
| `developers.googleblog.com` (transition Gemini CLI) | Échéance 18/06/2026 déjà passée à la date de cette mise à jour ; Hooks/Subagents/Skills préservés dans la transition |

**Non trouvé / redirection sans contenu** : `/docs/cli/sandbox/`,
`/docs/cli/subagents/`, `/docs/cli/settings/`, `/docs/browser-subagent`
redirigent vers des pages à onglets (`?tab=cli`) dont le contenu spécifique
CLI n'a pas pu être extrait séparément lors de cette mission — traité comme
`NOT_VERIFIED` plutôt que comme une absence de mécanisme. Sources
secondaires de la mission (Getting Started, IDE Overview, codelab, blog de
présentation) non consultées lors de cette mise à jour — rien dans les
sources prioritaires consultées ne signale qu'elles contrediraient ce
document ; à consulter seulement si un point précis reste flou en usage
réel.
