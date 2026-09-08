# Instructions pour Claude — dépôt SUPORDO

## Où chercher

- Carte humaine du dépôt : `01-discovery/ARBORESCENCE.md`
- Doctrine générale du corpus concurrentiel : `README.md`
- Décisions actées : `docs/decisions/` (numérotées, 0001 à 0006)
- Registre méthodologique/recherche : `01-discovery/concurrents/analysis/REGISTRE-CP.md` et `01-discovery/concurrents/analysis/SCHEMA-V2.md`

## Sessions Claude Code et continuité

Le dépôt constitue la mémoire durable du projet.
Une session Claude Code est une mémoire de travail temporaire.

### Nouvelle session

Privilégier une nouvelle session lorsqu'on :
- commence une nouvelle mission indépendante ;
- change de concurrent ou de corpus ;
- commence un nouveau lot autonome d'une production longue.

Ne pas conserver une session longue uniquement pour préserver son contexte.

Au démarrage d'une nouvelle session :
1. lire `CLAUDE.md` ;
2. exécuter `git status --short` ;
3. exécuter `git log -1 --oneline` ;
4. inspecter les fichiers directement concernés par la mission ;
5. reconstruire l'état depuis le dépôt avant toute action.

### Reprise après interruption

Une session peut s'arrêter net : perte de réseau, fermeture du terminal,
coupure. À la reprise, ne repars JAMAIS de ce que la conversation semblait
indiquer. Le fichier sur disque et Git font foi, pas le transcript de
session.

Premier réflexe, avant toute action :

```
git status --short
git log -1 --oneline
ls des dossiers concernés par la mission en cours
```

Puis dis à l'utilisateur :

- quels fichiers ont été écrits ;
- lesquels manquent par rapport à la mission annoncée ;
- si un fichier est incomplet ou incohérent ;
- si un commit est en attente.

Ne jamais recommencer une mission ou un lot avant d'avoir déterminé
mécaniquement ce qui est déjà écrit, committé et poussé. N'écris rien, ne
complète rien, ne recommence rien avant que l'utilisateur ne dise quoi
reprendre.

### Principe

Git = état durable.
`CLAUDE.md` = règles durables.
Documents du repo = connaissance durable.
Session Claude Code = contexte de travail jetable.

## Écriture incrémentale

Sur toute mission produisant plusieurs fichiers : écris-les au fur et à
mesure, jamais tous à la fin. Un travail interrompu doit laisser des
fichiers utilisables.

## Production LIGHT

Toute production LIGHT doit utiliser le protocole canonique du dépôt.
Ne jamais redéfinir ou modifier les règles LIGHT dans un prompt
spécifique à un concurrent.

Les paramètres d'exécution (lots, checkpoints, Git, reprise) peuvent
varier sans modifier le protocole d'extraction.

## Principe de suffisance décisionnelle

Une analyse n'est pas réussie parce qu'elle est maximalement exhaustive.
Elle est réussie si le niveau de preuve produit est suffisant pour la
décision qu'elle sert.

> QUESTION → PREUVE SUFFISANTE → DÉCISION → STOP

et non :

> QUESTION → LIRE TOUT CE QUI EST DISPONIBLE → PRODUIRE LE MAXIMUM → DÉCISION

Une analyse doit s'arrêter dès que la preuve nécessaire à la décision
qu'elle sert est suffisamment établie, **sauf si la mission vise
explicitement une mesure, une cartographie exhaustive ou la découverte de
variance** — ces trois cas exigent au contraire une couverture large et
ne doivent pas être coupés court.

Cette règle ne signifie pas :

- arrêter arbitrairement au premier exemple ;
- sacrifier la fidélité ;
- supprimer les contrôles adversariaux ;
- confondre un cas isolé avec une prévalence.

Elle signifie :

- dimensionner l'effort à la question posée, pas à la taille du corpus
  disponible ;
- définir le critère d'arrêt avant l'analyse lorsque c'est possible ;
- ne pas continuer à produire des observations qui ne peuvent plus
  changer la décision en cours.
