# Instructions pour Claude — dépôt SUPORDO

## Reprise après interruption

Une session peut s'arrêter net : perte de réseau, fermeture du terminal,
coupure. À la reprise, ne repars JAMAIS de ce que la conversation semblait
indiquer.

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

N'écris rien, ne complète rien, ne recommence rien avant que l'utilisateur
ne dise quoi reprendre.

## Écriture incrémentale

Sur toute mission produisant plusieurs fichiers : écris-les au fur et à
mesure, jamais tous à la fin. Un travail interrompu doit laisser des
fichiers utilisables.

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
