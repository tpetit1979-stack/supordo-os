# SUPORDO

SUPORDO est un projet SaaS CRM / mini-ERP destiné aux entreprises de
terrain.

Ce dépôt contient notamment un **chantier de recherche concurrentielle**,
documenté et traçable : ce qui a été collecté chez chaque concurrent,
depuis quelle adresse, par quelle méthode, et avec quelles limites
connues.

## Par où commencer

1. `01-discovery/ARBORESCENCE.md` — le dépôt et son organisation.
2. `docs/decisions/` — les décisions actées (numérotées 0001 à 0007),
   hypothèses métier et axes de recherche.
3. `01-discovery/concurrents/sources/COUVERTURE.md` — état détaillé et
   certifié de la collecte, concurrent par concurrent.
4. `01-discovery/concurrents/analysis/SCHEMA-V2.md` — le contrat
   d'extraction (V2 gelé + extensions V3 validées).
5. `01-discovery/concurrents/analysis/REGISTRE-CP.md` — les cas
   problématiques connus du schéma, non résolus.
6. `docs/decisions/0006-limites-analysis-c.md` et
   `01-discovery/concurrents/analysis/pilote-light-corpus-inedit.md` —
   état actuel : limites connues sur H1 et dernier pilote LIGHT validé.

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
