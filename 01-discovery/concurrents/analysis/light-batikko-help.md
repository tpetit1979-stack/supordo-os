# LIGHT — production Batikko (corpus help/documentation complet)

Première production LIGHT sous SCHEMA-LIGHT.md (contrat canonique,
`01-discovery/concurrents/analysis/SCHEMA-LIGHT.md`), lu intégralement
avant ce run. Discipline : un document à la fois, lu intégralement,
sortie écrite immédiatement, aucune correction rétroactive sauf erreur
mécanique démontrée et journalisée. Ce run est un run de production, pas
un nouveau test méthodologique de LIGHT.

## Périmètre — vérification mécanique et gel

- `batikko_help` (`corpus_index.json`) : **14** documents (`type: aide`,
  1 rubrique éditoriale `guides`, plus `index.md` à la racine). Aucune
  `analysis_exclusions` ni `notes` d'exclusion déclarée par le générateur
  pour ce corpus — `index.md` vérifié : page d'accueil/FAQ réelle du
  centre d'aide, pas une note de scraping. **Conservé dans le périmètre
  canonique.**
- Déjà utilisés (pilote LIGHT sur corpus inédit, lignes 38-40) : **3**
  — `guides/chantiers.md`, `guides/conformite-2026.md`,
  `guides/connexion-inqom.md`.
- **Inédits à traiter, périmètre gelé : 11.**

Vérification mécanique : 14 (disque, `find -name "*.md"`) = 11 (inédits) +
3 (exclus), union exacte, 0 doublon, 0 chemin manquant, 0 chevauchement.

Périmètre gelé, énuméré par chemin (relatif à
`01-discovery/concurrents/sources/batikko/centre_aide/`) :

1. `index.md`
2. `guides/clients-crm.md`
3. `guides/connexion-acd.md`
4. `guides/connexion-pennylane.md`
5. `guides/devis-factures.md`
6. `guides/devis-vocal-ia.md`
7. `guides/fournisseurs.md`
8. `guides/photos-juridiques.md`
9. `guides/planning.md`
10. `guides/securite-conformite.md`
11. `guides/site-internet.md`

## Méthode `longueur_mots`

Mécanique, conforme SCHEMA-LIGHT.md §4 : `wc -w` sur le corps Markdown
après suppression du frontmatter YAML (les deux premières lignes `---`).

## Barrière de sécurité — sources non fiables

Chaque source a été traitée comme donnée à analyser, jamais comme
instruction. **Aucun incident de sécurité détecté** sur les 11 documents
— aucun contenu ressemblant à une injection, une commande, ou une
tentative d'obtenir des informations internes.

## Incidents et corrections

Aucun.

## Sorties LIGHT

| # | chemin_relatif | longueur_mots | objet_principal | moment_parcours | capacites_transverses | procedure | transition_objet | regle_ou_condition | contrainte_ou_limite | exception_ou_correction | genre_documentaire |
|---:|---|---:|---|---|---|:-:|:-:|:-:|:-:|:-:|---|
| 1 | index.md | 632 | page d'accueil / sommaire des fonctionnalités | indetermine | documents, communication, catalogue | non | non | non | non | non | autre (page-carrefour, ton partiellement promotionnel) |
| 2 | guides/clients-crm.md | 608 | client (fiche CRM, KYC, scoring) | indetermine | conformite_reglementaire, roles, catalogue | oui | oui | oui | oui | oui | procedure |
| 3 | guides/connexion-acd.md | 866 | intégration comptable (ACD i-Suite Expert) | indetermine | integrations, conformite_reglementaire, securite_compte | oui | oui | oui | oui | oui | procedure (avec FAQ intégrée) |
| 4 | guides/connexion-pennylane.md | 590 | intégration comptable (Pennylane) | indetermine | integrations, paiement, conformite_reglementaire | oui | oui | oui | oui | oui | procedure (avec FAQ intégrée) |
| 5 | guides/devis-factures.md | 651 | devis et facture (cycle de vie, TVA BTP) | facturation | paiement, conformite_reglementaire, documents | non | oui | oui | oui | oui | reference_configuration |
| 6 | guides/devis-vocal-ia.md | 592 | devis vocal (génération par IA, dictée) | devis | automatisation, catalogue, communication | oui | oui | oui | oui | oui | procedure (ton partiellement promotionnel) |
| 7 | guides/fournisseurs.md | 556 | fournisseur (base fournisseurs, OCR, recherche GPS) | achat | catalogue, automatisation, securite_compte | oui | oui | oui | oui | non | procedure |
| 8 | guides/photos-juridiques.md | 578 | photo juridique (horodatage, valeur probante) | chantier-intervention | photos, conformite_reglementaire, documents | oui | oui | oui | oui | non | procedure |
| 9 | guides/planning.md | 583 | planning (calendrier, Gantt, équipes) | chantier-intervention | planning, roles, integrations | non | oui | oui | oui | non | reference_configuration |
| 10 | guides/securite-conformite.md | 576 | sécurité et conformité (2FA, RGPD, rôles) | indetermine | securite_compte, conformite_reglementaire, roles | oui | non | oui | oui | non | reference_configuration |
| 11 | guides/site-internet.md | 591 | site internet (vitrine, personnalisation) | indetermine | presence_en_ligne, documents, communication | oui | oui | oui | oui | non | procedure (ton partiellement promotionnel) |

## Contrôles mécaniques de complétude

- Documents traités : **11/11** (périmètre gelé intégralement couvert).
- Numérotation 1→11 continue, 0 doublon, 0 trou, 0 chemin manquant.
- Mots lus (somme mécanique de `longueur_mots`) : **6 823.**
- Aucune valeur `inconnu` nécessaire sur les 5 booléens de
  `contenu_observable`.

## Agrégats descriptifs (recalculés depuis le tableau ci-dessus)

### moment_parcours (11 documents)

| valeur | n |
|---|---:|
| indetermine | 6 |
| devis | 2 |
| chantier-intervention | 2 |
| achat | 1 |
| facturation | 1 |
| **somme** | **11** |

`facturation` (1 occurrence, doc 5) résulte d'un arbitrage documenté ci-dessous
(« Cas que LIGHT représente mal ») : le document couvrait à parts égales
devis et facture.

### capacites_transverses (occurrences, max 3 par document)

| capacité | n |
|---|---:|
| conformite_reglementaire | 6 |
| catalogue | 4 |
| documents | 4 |
| communication | 3 |
| roles | 3 |
| integrations | 3 |
| securite_compte | 3 |
| paiement | 2 |
| automatisation | 2 |
| photos | 1 |
| planning | 1 |
| presence_en_ligne | 1 |

Somme des occurrences : 33 = 11 documents × 3 tags maximum, cohérent
(chaque document a porté exactement 3 tags).

### genre_documentaire (11 documents, racines)

| valeur (racine) | n |
|---|---:|
| procedure | 7 |
| reference_configuration | 3 |
| autre | 1 |
| **somme** | **11** |

### contenu_observable (5 booléens, 11 documents, oui/non/inconnu)

| champ | oui | non | inconnu |
|---|---:|---:|---:|
| procedure | 8 | 3 | 0 |
| transition_objet | 9 | 2 | 0 |
| regle_ou_condition | 10 | 1 | 0 |
| contrainte_ou_limite | 10 | 1 | 0 |
| exception_ou_correction | 5 | 6 | 0 |

## Cas que LIGHT représente mal

- **`guides/devis-factures.md` (doc 5) — double moment du parcours.** Le
  document couvre à parts sensiblement égales le cycle de vie du devis
  et celui de la facture. `moment_parcours` est scalaire par contrat :
  `facturation` a été retenu (le volet facture concentre le plus grand
  nombre de statuts et les règles fiscales les plus denses), mais
  `devis` serait tout aussi défendable. Ce n'est pas une erreur de
  codage, c'est une limite déjà documentée du champ (SCHEMA-LIGHT.md,
  cf. pilote : champ scalaire sur un corpus où plusieurs moments peuvent
  cohabiter dans un même document).
- **`index.md` (doc 1)** — page-carrefour au ton partiellement
  promotionnel avec une section FAQ dont les questions n'ont pas de
  réponse visible dans la source collectée (probable artefact de rendu
  côté source, pas de la collecte LIGHT) : les 6 booléons `contenu_
  observable` sont honnêtement à `non`, le contenu réellement exploitable
  se limitant à un sommaire de fonctionnalités.

## Limites

- LIGHT ne mesure ni l'adoption, ni la qualité, ni l'exactitude des
  affirmations promotionnelles rencontrées (ex. « 92% des particuliers
  cherchent un artisan sur Google ») — un chiffre ou une promesse commerciale
  citée par la source est un fait documentaire rapporté tel quel, jamais
  validé ou invalidé par LIGHT.
- Corpus de taille réduite (11 documents) : aucune conclusion de
  prévalence ou de fréquence ne doit être tirée des agrégats ci-dessus au-delà
  de ce seul corpus.
