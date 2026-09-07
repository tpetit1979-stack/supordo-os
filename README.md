# SUPORDO

SUPORDO est un projet SaaS CRM / mini-ERP destiné aux entreprises de
terrain.

Ce dépôt contient notamment un **chantier de recherche concurrentielle**,
documenté et traçable : ce qui a été collecté chez chaque concurrent,
depuis quelle adresse, par quelle méthode, et avec quelles limites
connues.

## Les quatre niveaux du corpus concurrentiel

Quatre documents jouent des rôles différents. Ne pas les confondre :

1. **`tools/collecte/sources.yaml`**
   → configuration / intention de collecte (où collecter, selon quelles
   règles, avec quelles particularités par concurrent).

2. **`01-discovery/concurrents/sources/`**
   → snapshot physique brut des sources réellement collectées.

3. **`01-discovery/concurrents/corpus_index.json`**
   → représentation canonique et machine-lisible des corpus. Ce fichier
   est **généré** par `tools/collecte/build_corpus_index.py` — il n'est
   jamais maintenu à la main. À régénérer après toute nouvelle collecte.

4. **`01-discovery/concurrents/sources/COUVERTURE.md`**
   → audit humain détaillé : ce qui a été collecté, ce qui manque, et
   pourquoi (trous connus, anomalies).

## Points importants

- **L'arborescence physique de `sources/` est principalement une
  commodité de lecture humaine.** Un script d'analyse ne doit jamais
  déduire la nature d'un corpus (aide, marketing, documentation...) à
  partir du nom d'un dossier : il doit lire `corpus_index.json`, qui
  porte cette information explicitement.
- **OpenFire a deux corpus documentaires distincts** : un centre d'aide
  historique (plateforme Zendesk) et une documentation technique
  récente (plateforme Odoo). Cette distinction **ne permet pas de
  conclure** lequel des deux est ancien, nouveau, principal, secondaire
  ou plus fiable — c'est un fait de provenance, pas une interprétation.
- **Les sources concurrentielles brutes ne doivent jamais être
  modifiées par les scripts d'analyse.** `sources/` est un snapshot de
  preuve ; toute transformation se fait en aval, jamais en le réécrivant.
