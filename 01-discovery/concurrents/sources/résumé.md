# Résumé de récupération - 4 centres d'aide concurrents

Date : 2026-09-05

## Articles récupérés par site

| # | Site | Source | Catégories | Articles récupérés | Statut |
| --- | --- | --- | --- | --- | --- |
| 1 | Openfire | https://support.openfire.fr/hc/fr | 4 | 127 | OK |
| 2 | Axonaut | https://support.axonaut.com/ | 18 | 127 | OK |
| 3 | Vertuoza | https://intercom-help.eu/vertuoza/fr/ | 22 | 433 | OK |
| 4 | Sellsy | https://help.sellsy.com/fr/ | 20 | 462 | OK |
| | **Total** | | **64** | **1149** | |

## Sites en échec

Aucun. Les 4 sites ont été récupérés intégralement.

## Incidents rencontrés en cours de route (tous résolus)

- **Openfire** : les pages HTML `/hc/fr/...` sont protégées par un challenge
  Cloudflare (403 en scraping direct). Contournement : utilisation directe de
  l'API publique Zendesk (`/api/v2/help_center/...json`), accessible avec un
  User-Agent de navigateur, qui fournit categories/articles et le contenu HTML
  complet de chaque article sans passer par le challenge.
- **Vertuoza** : 7 articles de la catégorie Stock ont échoué au premier
  passage à cause d'une coupure DNS temporaire vers `intercom-help.eu` ;
  récupérés au second passage. 1 article de la catégorie FAQ avait un nom de
  fichier trop long pour Windows (> 260 caractères de chemin) ; récupéré avec
  un nom de fichier tronqué. 3 paires d'articles de la catégorie FAQ
  partageaient exactement le même titre/slug avec des IDs différents, ce qui
  écrasait un fichier sur deux ; les 6 articles ont été re-récupérés avec un
  identifiant unique ajouté au nom de fichier pour conserver les deux
  versions. Détail dans `vertuoza/erreurs.md`.
- **Axonaut** et **Sellsy** : aucun incident.

## Détails par site

Voir `<site>/index.md` pour la liste complète des articles par catégorie, et
`<site>/erreurs.md` pour le détail des incidents propres à chaque site.
