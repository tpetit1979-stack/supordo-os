# LIGHT — micro-lot expérimental de validation H3 (6 documents)

**Périmètre expérimental, pas un corpus canonique.** Ces 6 documents ne
constituent ni une production InterFast ni une production Vertuoza — ils
ont été choisis parce qu'ils portent, d'après une lecture V2/V3 antérieure
et indépendante (`mini-audit-B.md` §6), 7 contrôles positifs démontrés de
coordination conditionnelle (H3). Objet unique : tester la sensibilité du
filtre `regle_ou_condition = oui` sur des cas connus, pas produire une
carte de ces deux corpus. Rattaché à `test-sensibilite-light-h3.md`.

Schéma LIGHT canonique appliqué sans modification
(`01-discovery/concurrents/analysis/SCHEMA-LIGHT.md`). Discipline
identique aux productions réelles : un document à la fois, lu
intégralement, ligne écrite immédiatement.

## Périmètre — vérification mécanique et gel

6 chemins gelés avant codage (voir `pre-test-light-h3.md`, section
Contrôles positifs), aucune substitution :

1. `inter-fast/finances/activer-la-validation-des-commandes-fournisseurs.md`
2. `inter-fast/operations/creer-un-chantier-app-web.md`
3. `inter-fast/equipe/inviter-et-gerer-un-profil-sous-traitant.md`
4. `inter-fast/operations/consulter-et-utiliser-le-fil-d-activite-du-chantier.md`
5. `vertuoza/faq-foires-aux-questions/pourquoi-je-ne-peux-pas-recuperer-certaines-photos-ajoutees-par-mes-chefs-d-equipe-dans-les-suivis-gestionnaires.md`
6. `vertuoza/gestion-de-chantier/suivi-de-chantier-gestionnaire.md`

**Aucune exclusion** — les 6 chemins existent, sont lisibles, ont été lus
intégralement.

## Méthode `longueur_mots`

Mécanique, conforme SCHEMA-LIGHT.md §4 : `wc -w` sur le corps Markdown
après suppression du frontmatter YAML (délimité par les deux premières
lignes `---`). Les liens et syntaxe d'image (`![](url…)`) sont comptés
tels quels, non retirés — méthode brute, aucun ajustement manuel.

## Sorties LIGHT

| # | chemin_relatif | longueur_mots | objet_principal | moment_parcours | capacites_transverses | procedure | transition_objet | regle_ou_condition | contrainte_ou_limite | exception_ou_correction | genre_documentaire |
|---:|---|---:|---|---|---|:-:|:-:|:-:|:-:|:-:|---|
| 1 | inter-fast/finances/activer-la-validation-des-commandes-fournisseurs.md | 454 | validation des commandes fournisseurs (contrôle financier) | achat | paiement, roles, automatisation | oui | oui | oui | oui | oui | procedure (avec FAQ intégrée) |
| 2 | inter-fast/operations/creer-un-chantier-app-web.md | 1394 | chantier (création, méthodes multiples) | chantier-intervention | roles, permissions, automatisation | oui | oui | oui | oui | oui | procedure (avec FAQ intégrée) |
| 3 | inter-fast/equipe/inviter-et-gerer-un-profil-sous-traitant.md | 1096 | profil sous-traitant (invitation, permissions) | indetermine | roles, permissions, mobile | oui | oui | oui | oui | oui | procedure (avec FAQ intégrée) |
| 4 | inter-fast/operations/consulter-et-utiliser-le-fil-d-activite-du-chantier.md | 1291 | fil d'activité du chantier (communication temps réel) | chantier-intervention | communication, notifications, mobile | oui | oui | oui | oui | oui | procedure (avec FAQ intégrée) |
| 5 | vertuoza/faq-foires-aux-questions/pourquoi-je-ne-peux-pas-recuperer-certaines-photos-ajoutees-par-mes-chefs-d-equipe-dans-les-suivis-gestionnaires.md | 136 | photo (suivi de chantier, sélectionnabilité limitée dans le temps) | chantier-intervention | photos | oui | non | oui | oui | non | faq_depannage |
| 6 | vertuoza/gestion-de-chantier/suivi-de-chantier-gestionnaire.md | 270 | suivi de chantier (avancement / réclamation) | chantier-intervention | photos, roles, communication | oui | non | oui | oui | non | procedure |

## Contrôles mécaniques de complétude

- Documents traités : 6/6.
- Numérotation 1→6 continue, 0 doublon, 0 trou, 0 chemin manquant.
- `regle_ou_condition` : **6/6 = oui**, 0 non, 0 inconnu.
- `capacites_transverses` : aucune valeur nouvelle hors du vocabulaire
  descriptif de SCHEMA-LIGHT.md §4 (`paiement`, `roles`, `automatisation`,
  `permissions`, `mobile`, `communication`, `notifications`, `photos`).

## Journal d'incidents et corrections

Aucun. Aucune valeur ajustée après codage.

## Limites

- Échantillon non représentatif par construction (sélectionné pour porter
  des contrôles H3, pas un échantillon aléatoire ou proportionnel des
  corpus InterFast/Vertuoza).
- `objet_principal` et `genre_documentaire` restent des vocabulaires
  ouverts ; aucune conclusion de fréquence ou de prévalence ne doit être
  tirée de 6 documents.
- Ce fichier ne mesure pas si LIGHT représente séparément chaque forme de
  conditionnalité (montant, durée, état, rôle, abonnement, réglage,
  donnée) — voir `test-sensibilite-light-h3.md` pour cette distinction.
