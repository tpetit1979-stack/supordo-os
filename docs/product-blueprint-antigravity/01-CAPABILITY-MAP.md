# 01 — Capability Map

Inventaire structuré des capacités fonctionnelles du domaine SUPORDO : sources,
preuves, variantes, verticalités, importance. Document de référence pour
`02-CORE-VERTICAL-BLUEPRINT.md` (frontière CORE/VERTICAL) et `07-V1-V2-V3-80-20.md`
(priorisation).

## Statuts utilisés dans ce document

| Statut | Sens |
|---|---|
| `ACQUIS DOCUMENTAIRE` | fait établi par au moins une source primaire (audit fonctionnel détaillé), preuve forte |
| `MARKET_BASELINE` | convergence observée chez plusieurs concurrents — hypothèse de départ, pas une obligation |
| `VARIANTE DE MARCHÉ` | le marché se partage entre plusieurs approches, aucune dominante |
| `SUPORDO_DECISION` | décision PO actée dans `0007-contraintes-acquises.md`, opposable |
| `RECOMMANDATION ANALYTIQUE` | recommandation de ce document — jamais une décision |
| `À TESTER TERRAIN` | le corpus documentaire ne peut pas trancher seul |
| `NON DÉTERMINÉ` | silence du corpus — silence ≠ absence |
| `MARKETING_ONLY` | affirmation marketing, non confirmée par le centre d'aide ou l'audit fonctionnel |

## 1. Méthode et hiérarchie des sources

Trois couches de preuve coexistent dans le corpus, de poids croissant :

1. **LIGHT** (`SCHEMA-LIGHT.md`, 11 productions, 2 510 documents, 12 éditeurs) — présélection/couverture. Dit *quels domaines existent chez qui et avec quelle densité documentaire*, jamais *comment ils fonctionnent*. Deux glossaires indépendants (`GLOSSAIRE-OBSERVE-LIGHT.md` et `-B.md`) confirment la même ossature sans écart de fond.
2. **Audit fonctionnel objet par objet** (`functional-*.md`, `SUPORDO-CONTRAT-FONCTIONNEL-DEVIS-V0.md`) — la seule couche qui établit des mécanismes, états, dépendances avec citation exacte. Poids le plus fort. Ne couvre à ce jour que le devis en profondeur, et les autres objets par fragments (`onboarding-pilot`, `propagation-pilot`).
3. **Marketing** (`site_marketing/`, jamais analysé avant cette mission) — sert à découvrir promesses, positionnement, verticales revendiquées. Ne prouve jamais un fonctionnement réel. Tout ce qui en provient est marqué `MARKETING_ONLY` ci-dessous.

Rappel de doctrine (0004, 0006) : un silence documentaire n'est jamais une preuve d'absence ; une fréquence documentaire n'est jamais une mesure d'importance métier.

## 2. Capacités à signal universel (10/10 ou quasi, LIGHT)

| Capacité | Concurrents (LIGHT) | Nature du signal |
|---|---|---|
| Devis | 10/10, 144 documents | universel — objet le plus documenté avec la facture |
| Facture / facturation | 10/10, 193 documents | universel |
| Client / contact | 10/10, 118 documents | universel |
| Planning | 10/10, 72 documents | universel, mais densité inégale |
| Facturation électronique / conformité fiscale | 10/10, 63 documents | universel, à dominante réglementaire (voir `06`, réforme 2026) |
| Intégrations / synchronisations (config transverse) | 10/10, 120 documents | universel comme point d'extension, pas comme capacité métier en soi |

## 3. Capacités communes mais inégales (7-9/10, LIGHT)

| Capacité | Concurrents | Concentration notable |
|---|---|---|
| Catalogue / tarification | 9/10, 82 documents | — |
| Stock / réception | 9/10, 71 documents | — |
| Sécurité / authentification | 9/10, 58 documents | technique, pas métier |
| Site / adresse / lieu | 9/10, 24 documents | peu structuré comme objet autonome — voir `03` |
| Paiement / règlement | 9/10, 70 documents | — |
| Affaire / projet / chantier | 8/10, 84 documents | absent chez Axonaut, Sellsy (confirmé, pas un silence — voir `03`) |
| Documents | 8/10, 70 documents | — |
| Comptabilité / rapprochement bancaire | 8/10, 66 documents | — |
| Signature électronique | 8/10, 33 documents | — |
| Utilisateurs / comptes | 8/10, 34 documents | — |
| Application mobile | 8/10, 23 documents | — |
| Avoir / remboursement | 8/10, 20 documents | — |
| Rapports / pilotage | 8/10, 86 documents | **72 % chez Sellsy seul** — signal concentré, pas une baseline |
| SAV / support | 7/10, 54 documents | **54 % chez Vertuoza** — idem |
| Intervention | 6/10, 65 documents | densité correcte en LIGHT, mais faible en audit fonctionnel détaillé (voir `03`) |
| Tâches / notifications | 7/10, 19 documents | — |
| Acompte | 7/10, 22 documents | — |
| Onboarding / configuration | 7/10, 15 documents | — |

## 4. Capacités à diffusion restreinte — candidates verticales

| Capacité | Concurrents | Lecture |
|---|---|---|
| **Fluides frigorigènes / conformité froid-clim** | 2/10 (InterFast, OpenFire) | signal étroit mais **profondeur exceptionnelle** (11 documents dédiés chez InterFast seul : Cerfa 15497, BSFF, Trackdéchets, numéro de capacité) — candidat `VERTICAL_REGULATORY` + `VERTICAL_DATA` fort, voir `02` |
| **Équipement / actif / parc installé** | 2/10 (InterFast, OpenFire) | corrélé au point précédent — candidat `VERTICAL_DATA` |
| **Maintenance** (contrats, planification récurrente) | 3/10 | corrélé à la présence d'un parc installé — candidat `VERTICAL_WORKFLOW` |
| **CRM / opportunités (pipeline commercial)** | 3/10 (Sellsy, OpenFire, Vertuoza) | signal restreint mais transversal (pas lié à un métier BTP précis) — candidat frontière `CORE_EXTENSIBLE`, pas `VERTICAL_*` |
| **IA générative appliquée** (résumé, rédaction) | 1/10 réel (Sellsy) | **signal éditeur-spécifique** — 5/10 en comptage brut mais 1 seul corpus porte une vraie fonctionnalité IA générative (Sellsy IA / Mistral), les autres occurrences sont des règles conditionnelles sans rapport avec l'IA générative. Ne pas lire comme une baseline. |
| **Visite / relevé terrain structuré** | 2/10 en LIGHT (silence quasi total) | signal faible en LIGHT, mais l'audit fonctionnel détaillé (3C) trouve 2 cas forts (InterFast, OpenFire Zendesk) — voir `03`/`04` |
| **Bibliothèques de prix par corps de métier** | 1/10 (ProGBat, add-on payant "BatiChiffrage") | **seul précédent marché direct du modèle CORE + PACKS MÉTIERS** demandé par le PO |

## 5. Positionnement métier observé par concurrent

| Concurrent | Positionnement (centre d'aide + marketing) |
|---|---|
| **OpenFire** | **Seul concurrent du corpus avec une double spécialisation produit réelle** : fumisterie/poêles-cheminées (page produit dédiée, catalogue fabricants centralisé 900 000+ produits/250+ marques) ET climatisation/froid (module réglementaire complet, Cerfa 15497 mobile, Trackdéchets). Pas un positionnement SEO — un module fonctionnel nommé. `MARKETING_ONLY` pour l'étendue exacte des fonctions ; `ACQUIS DOCUMENTAIRE` pour l'existence du corpus dédié fluides frigorigènes (centre d'aide). |
| **InterFast** | BTP + spécialisation froid/climatisation documentée en centre d'aide (rubrique `fluides-frigorigenes/`, 8 documents) et en marketing (5 landing pages métier : chauffagiste, électricien, froid-climatisation, PAC, plombier). |
| **ProGBat** | BTP généraliste avec extension par corps de métier en add-on payant (BatiChiffrage) — precedent du modèle CORE+PACKS, pas une spécialisation produit propre. |
| Axonaut, Costructor, Extrabat, Obat, Batikko, Vertuoza, Tolteck, Leobati | BTP généraliste, ciblage SEO multi-métier en marketing (landing pages par corps de métier chez plusieurs), aucune spécialisation produit détectée dans l'échantillon lu. `MARKETING_ONLY`. |
| Sellsy, Axonaut | CRM/facturation généraliste multi-secteur, non spécifiquement BTP. |

**Aucun concurrent ne cible la fumisterie/poêles/cheminées dans son centre d'aide** (silence total en LIGHT). Le signal existe uniquement côté marketing chez OpenFire (`MARKETING_ONLY` pour l'étendue, mais le module réglementaire froid est lui `ACQUIS DOCUMENTAIRE`). C'est un point de vigilance direct pour le stress-test §2 du PO — voir `02`.

## 6. Capacités revendiquées en marketing, non confirmées fonctionnellement (`MARKETING_ONLY`)

Balayage ciblé (~15 fichiers sur ~4 200 pages marketing collectées — un premier sondage, pas une couverture exhaustive).

| Capacité | Concurrent | Citation / élément |
|---|---|---|
| **Devis vocal → devis structuré** | Vertuoza | "devis en 45 secondes", multilingue 50+ langues, avenants par commande vocale mobile |
| **Devis vocal BTP avec structuration** | Batikko | dictée → transcription → lignes structurées → devis conforme (TVA multi-taux) → conversion Factur-X via PDP. Le document le plus explicite du corpus sur "l'IA fait le brouillon, l'humain valide" |
| **IA générative CRM** | Sellsy | résumé fiche client, rédaction d'emails, champs intelligents — via Mistral (partenaire français, hébergement UE revendiqué) |
| **Photos de chantier horodatées** | Batikko | — |
| **Application mobile terrain + remplissage CERFA mobile + itinéraires optimisés** | OpenFire | — |
| **"Assistant administratif IA"** | Axonaut | **Attention — ce n'est pas de l'IA** : service humain (assistantes certifiées). Ne jamais citer comme précédent IA. |
| Écosystème d'intégrations comptables/bancaires françaises (Qonto, Pennylane, 9 connecteurs compta, Payplug/SumUp) | ProGBat | le plus riche du corpus marketing sur ce point |
| Trackdéchets, catalogue fabricants centralisé | OpenFire | cohérent avec le module froid/fumisterie du centre d'aide |

**Lecture pour le blueprint** : Vertuoza et Batikko revendiquent déjà un parcours proche de la vision voix→devis structuré du PO (§2 de la mission). C'est un signal de faisabilité marché (quelqu'un l'a construit), pas une preuve que SUPORDO doit le répliquer à l'identique, et pas une preuve de qualité réelle du mécanisme (non vérifiable depuis la documentation marketing).

## 7. Analyse 80/20 qualitative — capacités structurantes

Pas de score numérique (interdit par la mission). Échelle qualitative FAIBLE/MOYENNE/FORTE sur la complexité ; jugement narratif sur les 8 autres axes.

| Capacité | Centralité | Workflow closure | Pilot necessity | Coût du report | Convergence marché | Différenciation | Valeur verticale | Levier IA | Complexité |
|---|---|---|---|---|---|---|---|---|---|
| Client (création + rattachement) | très forte — racine du graphe | oui | oui | très élevé (touche tout) | 8/8 | faible | faible | faible | FAIBLE |
| Devis (naissance + cycle) | très forte | oui | oui | très élevé | 8/8 | moyenne (verrouillage, dérivation) | moyenne | forte (visite→devis) | MOYENNE |
| Catalogue / prix figé | forte | non seul | oui | élevé (S3 SUPORDO_DECISION) | 8/8 | faible | forte en verticale (catalogues métier) | moyenne | FAIBLE-MOYENNE |
| Facture (émission + immuabilité) | très forte | oui | oui — sans elle pas de produit vendable | très élevé (contrainte légale L1) | 6/8 + citation légale | faible (contrainte, pas différenciateur) | faible | faible | MOYENNE (légal) |
| Acompte/situation/solde (recalcul automatique) | forte | oui | oui pour BTP | élevé | 6/8, le mécanisme le mieux corroboré du corpus | moyenne | forte (situations de travaux) | faible | MOYENNE |
| Chantier/Intervention (objet + agrégation rentabilité) | forte mais mal outillée par le corpus | oui | oui | élevé — coûteux à ajouter tard (S1, graphe objets) | 3-8/8 selon le sous-mécanisme | **forte — axe de différenciation SUPORDO** | forte | forte (rapport terrain) | FORTE (corpus pauvre) |
| Visite/relevé terrain → devis pré-rempli | faible en preuve, forte en ambition PO | ferme un parcours entier si réussi | non indispensable au tout premier pilote, mais central à la thèse produit | élevé si ajouté après coup (ré-architecture UX+data) | 2/8 (InterFast, OpenFire Zendesk) | **très forte — c'est la proposition de valeur du PO** | très forte | **très forte — le vrai terrain d'application voix+photo** | FORTE |
| Parc installé / équipement | faible en preuve (2/8, isolé OpenFire Odoo pour la cascade complète) | ferme le parcours maintenance | non pour V1 générique, oui pour verticale clim/chauffage | élevé si différé | 2/8 | forte | très forte (spécifique clim/chauffage/fumisterie) | moyenne | MOYENNE-FORTE |
| Lieu (distinct du client) | forte structurellement (S1) | non seul | pas visible pour l'utilisateur mais structurant | **très élevé** — 0007 le dit explicitement ("casse la mémoire longue et le SAV" si changé tard) | faible preuve directe (1 décision PO, pas une convergence documentée) | faible visible, forte en mémoire longue | moyenne | faible | FAIBLE si posé tôt, FORTE si posé tard |
| Personnel ≠ compte utilisateur | moyenne | non | non pour solo | moyen | 2/8 (M14, preuve faible) | faible | faible | faible | FAIBLE |
| CRM / pipeline commercial | faible-moyenne | ferme un parcours commercial amont | non pour V1 terrain | moyen | 3/8 | faible (généraliste) | faible (pas lié à une verticale) | moyenne | MOYENNE |
| Provenance IA ciblée (S4) | forte transversalement dès qu'IA impliquée | non seul | oui dès qu'une capture IA existe | élevé si ajouté après coup sur des données déjà en base | 1 décision PO, pas de convergence marché | forte (différenciateur de confiance) | égale partout | — (méta-capacité) | MOYENNE |

## 8. Limites explicites de ce document

- Le balayage marketing (§6) porte sur ~15 fichiers sur ~4 200 : suffisant pour orienter le blueprint, insuffisant pour clore le sujet. Toute décision produit ferme sur l'IA/intégrations doit repasser par une lecture plus large avant d'être actée.
- L'absence de "poêle/cheminée/fumisterie" dans les 2 510 documents LIGHT (§5) ne prouve pas l'absence de la verticale sur le marché élargi — seulement qu'aucun des 12 concurrents étudiés n'en documente une dans son centre d'aide, à l'exception du signal marketing OpenFire.
- Les domaines à faible volume documentaire (visite : 2 documents LIGHT, équipement/parc : 9, maintenance : 9) sont des pistes, pas des preuves suffisantes pour figer un modèle de données — voir `03-DOMAIN-DEPENDENCIES-LIFECYCLES.md` pour le niveau de preuve détaillé objet par objet.
