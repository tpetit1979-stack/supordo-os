# Erreurs de recuperation

Date : 2026-09-05
Source : https://intercom-help.eu/vertuoza/fr/

Incidents rencontres et corriges pendant la recuperation :
- 7 articles de la categorie Stock ont echoue au premier passage (coupure DNS
  temporaire vers intercom-help.eu). Recuperes avec succes au second passage.
- 1 article de la categorie FAQ avait un nom de fichier trop long pour Windows.
  Recupere avec un nom de fichier tronque.
- 3 paires d'articles de la categorie FAQ partageaient le meme slug (titres
  identiques, IDs differents), ce qui a d'abord ecrase un fichier sur deux.
  Les 6 articles ont ete re-recuperes avec un identifiant unique ajoute au nom
  de fichier pour conserver les deux versions.

Aucune erreur restante. 22 categories et 433 articles recuperes au total.
