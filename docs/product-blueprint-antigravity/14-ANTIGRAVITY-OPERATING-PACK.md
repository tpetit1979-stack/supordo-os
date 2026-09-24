# 14 — Antigravity Operating Pack

Configuration recommandée pour encadrer un agent Google Antigravity travaillant
sur le futur dépôt applicatif SUPORDO (distinct de `supordo-os`, ce dépôt
documentaire). Fondé sur la documentation **officielle actuelle**
(`antigravity.google/docs`, consultée le 23/09/2026 par lecture directe du
sitemap officiel — pas de recherche indexée tierce disponible pendant cette
mission, voir §7) et sur les règles minimales explicitement données par le PO
(mission §9).

**Avertissement de fraîcheur** : Antigravity a déjà connu au moins une refonte
majeure en moins d'un an (lancement 18/11/2025, doc actuelle référence déjà
« Antigravity 2.0 »). **Les Workflows sont dépréciés au profit des Skills à
partir du 1er novembre 2026** — dans environ 5 semaines à la date de cette
mission. Ce document construit sur les Skills, pas sur les Workflows. À
revérifier avant tout usage si cette mission est reprise après cette date.

---

## 0. Ce qu'est réellement Antigravity aujourd'hui

Une **famille de produits**, pas un outil unique : **Antigravity 2.0**
(application desktop, « command center » multi-agents), **Antigravity CLI**
(TUI léger, successeur direct de Gemini CLI avec compatibilité ascendante —
`GEMINI.md`/`AGENTS.md` toujours parsés, migration via `agy plugin import
gemini`), extensions **IDE** (VS Code, Visual Studio, JetBrains, Zed, Xcode), et
un **SDK** Python pour agents/skills custom. Le choix de surface (desktop, CLI,
IDE) est un choix d'outillage, pas une question produit — ce document reste
valable pour les trois.

---

## 1. Project / workspace

Un **Project** est « une configuration de dossiers définissant l'environnement
et le périmètre de l'agent », pouvant regrouper plusieurs dossiers/dépôts
(frontend+backend) pour du contexte cross-repo.

**Règle SUPORDO** : le Project du futur dépôt applicatif ne doit **jamais**
inclure `supordo-os` (ce dépôt documentaire) dans son périmètre déclaré. Si un
document de ce blueprint doit être consulté par l'agent, il est **copié
explicitement** dans le dépôt applicatif (ex. `docs/blueprint-reference/`), pas
référencé par un accès direct à `supordo-os`. C'est la première règle minimale
du PO (§9), directement applicable via le périmètre du Project.

## 2. Branches / worktree

Deux modes réels : **Local Mode** (l'agent opère directement dans le dossier
actif — donc potentiellement la branche courante) et **New Worktree Mode**
(git worktree isolé, dédié à ne pas toucher l'état de travail principal).

**Règle SUPORDO** : **New Worktree Mode obligatoire par défaut** pour toute
tranche de `12-ANTIGRAVITY-BUILD-SEQUENCE.md`. Le Local Mode n'est autorisé que
pour des tâches d'inspection pure (`OBSERVE`), jamais pour `IMPLEMENT`. Rien
dans le produit n'empêche techniquement un commit direct sur `main` — c'est une
discipline de configuration, pas un acquis du produit.

## 3. Permissions

Mécanisme officiel : **moteur de permission fin unifié**, trois listes
**Deny / Ask / Allow**, priorité stricte `Deny > Ask > Allow`. Couvre
`read_file`, `write_file`, `command`, `read_url`, `execute_url`, `mcp`. Config
dans `~/.gemini/antigravity-cli/settings.json` (global) ou équivalent
workspace.

Trois presets globaux : **Default**, **Request Review** (approbation
systématique, accès fichiers restreint au workspace — recommandé), **Turbo**
(aucune restriction — **interdit** dans ce projet).

**⚠️ Spécificité Windows (l'environnement de ce projet)** : sous Windows,
**toutes les commandes sont « Ask » par défaut** et **le sandbox terminal est
désactivé par défaut**, nécessitant une activation manuelle — comportement
distinct de macOS/Linux où certaines commandes s'exécutent sans prompt à
l'intérieur d'un sandbox isolé. **Ne jamais supposer un comportement macOS/
Linux documenté ailleurs comme valant pour ce projet** — activer et vérifier
explicitement le sandbox Windows avant tout usage réel.

**Configuration recommandée (`settings.json` du projet applicatif)** :
```json
{
  "permissions": {
    "deny": [
      "command(sudo)", "command(rm -rf)", "command(choco)", "command(winget)",
      "read_file(../supordo-os/**)", "write_file(../**)"
    ],
    "allow": [
      "command(git status)", "command(git diff)", "command(npm run test)"
    ],
    "ask": ["command(*)", "read_url(*)", "execute_url(*)", "mcp(*)"]
  }
}
```
Liste indicative, à affiner avec Antigravity lui-même lors du cadrage de
`T0` — mais le principe `deny` sur tout chemin hors du dépôt applicatif et
`ask` par défaut sur toute commande/réseau doit être posé avant la première
tranche, pas découvert en cours de route.

## 4. Rules persistantes

Mécanisme officiel : **Rules**, fichiers Markdown, 12 000 caractères max.
Emplacements : global `~/.gemini/GEMINI.md`, **projet : `.agents/rules/` à la
racine du dépôt applicatif** (rétro-compatible `.agent/rules`). Activation :
manuelle (`@mention`), always-on, décision du modèle, ou glob pattern.

**Rules SUPORDO recommandées (always-on)** :
- `.agents/rules/supordo-doctrine.md` — rappel de la discipline de preuve `0007`, des statuts (`SUPORDO_DECISION` vs `RECOMMANDATION` vs `OPEN`), et de l'interdiction de trancher silencieusement une question `OPEN` du registre `09`/`12`.
- `.agents/rules/supordo-invariants.md` — invariants non négociables (immuabilité facture L1, isolation RLS, jamais de champ éditable pour une valeur dérivée) — référence directe à `08`.
- `.agents/rules/supordo-honesty.md` — discipline `REAL`/`PROTOTYPE`/`MOCK`/`NOT_IMPLEMENTED`, interdiction de présenter un mécanisme simulé comme réel.
- Rule à activation `glob` sur `**/*.sql` et fichiers de migration — rappel RLS avant toute modification de schéma.

## 5. Skills persistantes

Mécanisme officiel : **Agent Skills** (standard ouvert), dossier
`.agents/skills/<nom>/SKILL.md` + `scripts/`/`examples/`/`resources/`
optionnels, modèle de « progressive disclosure » (découverte → activation →
exécution). **Construire sur les Skills, pas sur les Workflows (dépréciés au
1er novembre 2026).**

**Skills SUPORDO candidates** :
- `slice-observe` — protocole d'observation d'une tranche (template §9, doc `09`/`12`).
- `slice-verify` — exécution systématique de la matrice de tests `13` pertinente à la tranche en cours.
- `check-tenant-isolation` — script de vérification RLS réutilisable à chaque tranche touchant une nouvelle table.

## 6. Hooks

Mécanisme **réel, non déprécié**, distinct des Workflows. Cinq événements :
`PreToolUse`, `PostToolUse`, `PreInvocation`, `PostInvocation`, `Stop`. Config
`.agents/hooks.json` (workspace) ou global. `PreToolUse` peut renvoyer
`allow`/`deny`/`ask`/`force_ask`/`deny_unless_prior_grant` — **point de levier
programmatique réel**, au-delà des règles textuelles.

**Hooks SUPORDO recommandés** :
- `PreToolUse` sur toute écriture touchant un fichier de politique RLS ou de test → `force_ask`, jamais d'auto-approbation, quel que soit le preset de permission actif.
- `PreToolUse` sur toute commande `npm install`/`pip install` d'un paquet non déjà présent dans le lockfile → `ask`.
- `PreToolUse` sur toute écriture hors du dossier `.agents/` et du code applicatif déclaré du Project → `deny`.

## 7. Planning / Implementation Plan

Mécanisme officiel : **Implementation Plan**, artefact généré par l'agent avant
modification, revu par l'humain. **Planning Mode** : **Request Review**
(recommandé — l'agent s'arrête toujours et demande une approbation explicite
avant de continuer) vs **Always Proceed** (**interdit** dans ce projet).

Commandes associées : `/goal` (exécution jusqu'à complétion **sans pause pour
input intermédiaire** — l'inverse d'un mode supervisé) et `/grill-me` (l'agent
pose des questions de clarification avant d'implémenter, recommandé en
`OBSERVE`/`PLAN`).

**Règle SUPORDO** : **`Planning Mode = Request Review` imposé, jamais Always
Proceed.** `/goal` n'est utilisé qu'après approbation explicite du plan, jamais
pour enchaîner plusieurs tranches sans repasser par `VERIFY`/`AUDIT` entre
chacune — un `/goal` couvre au maximum une seule tranche de `12`, jamais
plusieurs.

## 8. Vérification visuelle / navigateur

Mécanisme **réel** : **Browser Subagent** dédié, Chrome dans un profil séparé
de l'utilisateur, captures d'écran à l'initiative de l'agent ou sur demande,
**enregistrements vidéo** des actions (Recording Artifact View, IDE
uniquement). Sécurité à deux couches : denylist serveur Google (fail-closed) +
allowlist locale éditable (initialisée à `localhost` seul, prioritaire dans le
sens où la denylist prime toujours).

**Règle SUPORDO** : toute tranche avec impact interface (`12`, presque toutes)
exige une capture ou un enregistrement du Browser Subagent en étape `VERIFY` —
conforme à l'exigence `13` (aucune preuve de "page visible" seule, mais une
preuve de comportement réellement observé).

## 9. Git

Panneau VCS natif (Antigravity 2.0) : vues **Agent Edits**, **Uncommitted
changes**, **Branch changes**, diff, suggestions de message de commit, terminal
intégré. **Aucune création automatique de Pull Request ni revue de code
formalisée par un tiers trouvée dans la documentation** — la revue reste celle
de l'utilisateur via le panneau diff.

**Règle SUPORDO** : le merge du worktree vers `main` reste **toujours un geste
humain explicite**, jamais une action autonome de l'agent, même après un
`VERIFY`/`AUDIT` réussi — cohérent avec la règle minimale du PO (« Antigravity
ne doit jamais écrire directement sur main »).

## 10. Supabase DEV

Connexion via **MCP** uniquement (« Antigravity peut inspecter le schéma en
direct de Neon, Supabase ou AlloyDB pour suggérer les bons noms de tables/
colonnes ») — pas de connecteur Supabase propriétaire hors MCP trouvé. Config
`mcpServers` dans `.agents/mcp_config.json` (workspace) ou global.

**Règle SUPORDO, directement liée à la règle minimale du PO** (« Antigravity ne
doit jamais modifier une base de production ni appliquer une migration de
production ») : le serveur MCP Supabase configuré pour ce projet **ne pointe
que vers le projet Supabase DEV** (`08` §10 — environnements séparés). Les
identifiants du projet Supabase de production ne sont **jamais** présents dans
la configuration MCP accessible à l'agent, sous aucune forme.

## 11. Secrets

**Zone d'ombre documentaire confirmée par la recherche** : la gestion des
secrets n'est documentée officiellement que dans le contexte **MCP** (headers
custom, OAuth, Google Application Default Credentials, tokens stockés dans
`~/.gemini/antigravity-cli/mcp_oauth_tokens.json`). **Aucune page officielle
dédiée aux secrets applicatifs** (`.env` d'un projet, clé de service Supabase)
n'a été trouvée — seule protection connue : le sandbox bloque par défaut la
lecture de `.env` et `~/.ssh`.

**Règle SUPORDO** : ne **jamais** présumer une protection native au-delà du
sandbox documenté. Politique explicite à construire nous-mêmes : les secrets
applicatifs (clé service-role Supabase, clés API des intégrations `06`) ne sont
**jamais** placés dans un fichier lisible par l'agent en clair — injectés par
variable d'environnement au niveau du déploiement, hors du périmètre de lecture
du Project Antigravity. Un Hook `PreToolUse` scannant les diffs pour des motifs
de clé/secret avant tout `write_file`/commit est recommandé en complément
(mécanisme à construire, pas garanti nativement par Antigravity).

## 12. Dépendances

Pas de mécanisme dédié nommé — géré par la permission générique `command`.
Sous Windows (cet environnement), toute commande est déjà `Ask` par défaut, ce
qui inclut `npm install`/`pip install` — comportement conservateur par défaut,
**mais à figer explicitement dans la configuration du projet plutôt que de
compter sur un défaut qui pourrait changer**.

## 13. Appels réseau

Couverts par `read_url`/`execute_url`, en `Ask` par défaut sur toutes les
plateformes. Aucune règle supplémentaire nécessaire au-delà de la configuration
de permission posée en §3 — s'assurer que les appels réseau vers les
intégrations `06` (LLM, transcription, PDP) passent explicitement par les
interfaces `PLATFORM_CAPABILITY` définies en `12` §0.2, pas par un appel direct
non abstrait depuis le code métier.

## 14. Preuves de fin de tâche

Mécanisme **Artifacts** (Implementation Plans, diffs visuels, diagrammes,
images, enregistrements navigateur) + **Walkthrough** — artefact de fin de
tâche spécifiquement conçu pour un humain n'ayant pas suivi le travail en temps
réel.

**Règle SUPORDO** : le Walkthrough de chaque tranche doit inclure explicitement
la déclaration `REAL`/`PROTOTYPE`/`MOCK`/`NOT_IMPLEMENTED` par capacité livrée
(exigée par `13`), pas seulement une liste de fichiers modifiés.

## 15. Audit indépendant

Deux mécanismes réels trouvés :
- **Subagents** — agents concurrents nommés, peuvent lire les transcripts les uns des autres pour auditer un flux multi-étapes ; permet de définir un « subagent auditeur » dédié.
- **Teamwork** (`/teamwork-preview`) — architecture hiérarchique avec rôles nommés **Critic** (revue de correction/complétude), **Challenger** (tests adversariaux), **Auditor** (« vérifie les preuves de test contre le résultat réel des commandes »), **Success Auditor** (vérification finale bout-en-bout).

**⚠️ Teamwork porte le suffixe `-preview`** dans sa commande — statut encore
expérimental à la date de cette recherche, à ne pas présenter comme un
mécanisme mature et stable.

**Règle SUPORDO** : l'étape `AUDIT INDÉPENDANT` de la séquence (§16) utilise un
**subagent auditeur dédié sans accès au contexte de planification/
implémentation** de la tranche (équivalent à un agent frais, pas un fork qui
hérite du contexte de l'implémenteur) — Teamwork/Critic peut être essayé en
complément si disponible, mais jamais comme unique garantie tant qu'il reste en
`-preview`.

---

## 16. Séquence obligatoire, mécanisme par mécanisme

`OBSERVE → PLAN → APPROBATION HUMAINE → IMPLEMENT → VERIFY → AUDIT INDÉPENDANT
→ TEST HUMAIN → MERGE`

| Étape | Mécanisme Antigravity mobilisé |
|---|---|
| OBSERVE | Local Mode ou lecture seule dans le Project scoping (§1), `/grill-me` encouragé |
| PLAN | Implementation Plan, Planning Mode = `Request Review` (§7) |
| APPROBATION HUMAINE | Revue du plan via le panneau de revue (commentaires inline, bouton Proceed) — jamais `Always Proceed` |
| IMPLEMENT | New Worktree Mode (§2), permissions Default/Request Review (jamais Turbo, §3), Hooks actifs (§6) |
| VERIFY | Exécution de `13`, Browser Subagent pour toute tranche UI (§8), déclaration REAL/PROTOTYPE/MOCK/NOT_IMPLEMENTED |
| AUDIT INDÉPENDANT | Subagent auditeur sans contexte partagé (§15), vérifie la déclaration VERIFY contre les preuves réelles |
| TEST HUMAIN | Champ dédié de chaque tranche (`12`) — un humain utilise réellement la capacité |
| MERGE | Geste humain explicite (§9), jamais automatique |

## 17. Règles minimales du PO — mécanisme d'application

| Règle (mission §9) | Mécanisme d'application concret |
|---|---|
| Ne jamais accéder à `supordo-os` sauf fichier explicitement copié | Périmètre du Project (§1) |
| Ne jamais modifier un chemin hors du repository autorisé | Permissions `deny` (§3) + Hook `PreToolUse` (§6) |
| Ne jamais écrire directement sur `main` | New Worktree Mode obligatoire (§2) + merge humain (§9) |
| Ne jamais modifier une base de production / appliquer une migration de production | MCP Supabase scopé DEV uniquement, jamais de credentials prod accessibles (§10) |
| Ne jamais installer un logiciel système sans approbation explicite | `command` en `Ask`/`deny` pour les installeurs système (§3, §12) |
| Ne jamais exposer une clé ou un secret | Politique explicite hors sandbox natif, Hook de scan (§11) |
| Ne jamais contourner une RLS ou un test pour obtenir un résultat vert | Hook `force_ask` sur les fichiers RLS/tests (§6) + AUDIT indépendant (§15) |
| Ne jamais inventer le comportement d'une question `OPEN` | Rule always-on `supordo-doctrine.md` (§4) référençant `09`/`12` |
| Ne jamais transformer silencieusement REAL en PROTOTYPE/MOCK, ni présenter un MOCK comme REAL | Rule `supordo-honesty.md` (§4) + déclaration obligatoire en VERIFY (§14) + AUDIT (§15) |
| Ne jamais présenter un mécanisme IA/réglementaire/signature/conformité comme réel sans intégration réelle et tests | Même discipline, appliquée spécifiquement aux `PLATFORM_CAPABILITY` de `12` §0.2 |
| Ne jamais considérer l'Implementation Plan comme preuve de réalisation | VERIFY/AUDIT fondés sur exécution réelle (tests, Browser Subagent), jamais sur le Plan seul |

---

## 18. Retour d'expérience "sharp-kepler"

**Non trouvé publiquement**, malgré une recherche dédiée (recherche web
indisponible pendant cette mission précise — budget épuisé — collecte faite
uniquement via lecture directe de la documentation officielle, qui ne
référence aucun retour d'expérience nommé). Ne pas combler ce manque par une
supposition : si cette référence existe, elle n'a pas pu être vérifiée dans le
cadre de cette mission et ne doit pas être citée comme source dans les
documents produits.

## 19. Ce que ce document ne fait pas

Ne configure aucun projet Antigravity réel, ne crée aucun fichier `.agents/`
dans un dépôt applicatif (qui n'existe pas encore), ne touche à aucun projet
Supabase. C'est un cahier des charges pour la configuration à poser au moment
du premier build réel — à valider contre la documentation Antigravity du jour,
qui peut avoir évolué d'ici là (voir avertissement de fraîcheur en tête de
document).
