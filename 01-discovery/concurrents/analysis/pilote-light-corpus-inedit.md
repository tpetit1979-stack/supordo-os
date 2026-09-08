# Pilote LIGHT — premier passage réel sur corpus inédit (40 documents)

Ce document applique le schéma LIGHT (métadonnées mécaniques + `objet_principal` /
`moment_parcours` / `capacites_transverses` / `contenu_observable` / `genre_documentaire`)
à 40 documents jamais utilisés dans Pilote A, Pilote B, Analysis C, H1_SOURCE_TEST ou le
test LIGHT sur 12 documents. Objectif unique : savoir si LIGHT produit, sur du corpus
neuf, une carte factuelle exploitable à coût raisonnable — pas une validation de plus
de l'instrument.

Discipline d'exécution imposée et respectée : chaque document est ouvert seul, codé,
écrit sur disque immédiatement, puis fermé — jamais de vision globale préalable, jamais
de correction rétroactive d'une sortie déjà écrite à la lumière d'un document lu plus
tard (voir `effets_de_calibration_a_posteriori` en fin de document).

## Coût d'exécution

- Documents traités : 40/40.
- Volume lu : 14 450 mots (somme mécanique de la colonne `longueur_mots` du tableau
  ci-dessous, estimations approximatives par document) — soit ≈14 000 mots.
- Difficulté particulière : aucune, hormis le cas #9 (contenu de type menu de
  navigation plutôt qu'article, codé tel quel plutôt que substitué).
- Contexte de session : `CONTEXTE_SESSION_NON_MESURABLE`. La croissance du contexte
  n'a pas pu être mesurée de manière fiable pendant ce pilote. On ne peut donc pas
  conclure à partir de cette mission qu'une passe unique sur ~1 899 documents est
  faisable. L'industrialisation devra commencer par lots/sessions bornés, avec mesure
  réelle du contexte si l'environnement le permet.

## Sélection — méthode

Sélection **mécanique**, fondée uniquement sur `corpus_index.json` (liste des rubriques
par corpus) et un parcours systématique des dossiers : pour chaque concurrent ciblé, un
fichier par rubrique non encore utilisée dans les travaux précédents, en cyclant sur les
rubriques jusqu'au quota, dans l'ordre alphabétique des noms de fichiers au sein de
chaque rubrique. Aucun contenu n'a été lu avant la sélection. Concurrents ciblés :
OpenFire (zendesk + un article Odoo), Costructor, Sellsy, Axonaut, ProGBat, Batikko —
aucun Vertuoza/InterFast (déjà largement couverts par les travaux précédents).

## Échantillon gelé (40) — ne sera plus modifié en fonction du contenu

| # | corpus_id | rubrique | chemin_relatif | raison mécanique |
|---:|---|---|---|---|
| 1 | openfire_zendesk | bien-debuter | bien-debuter/caracteristiques-techniques-et-configurations-requises.md | diversification rubrique |
| 2 | openfire_zendesk | guides-videos | guides-videos/acceder-au-tarif-centralise.md | diversification rubrique |
| 3 | openfire_zendesk | configurer-openfire | configurer-openfire/achats-intracommunautaires-et-autoliquidation-comptabilite-francaise.md | diversification rubrique |
| 4 | openfire_zendesk | utiliser-openfire | utiliser-openfire/choisir-son-mode-de-reapprovisionnement.md | diversification rubrique |
| 5 | openfire_zendesk | bien-debuter | bien-debuter/comment-indiquer-le-niveau-de-priorite-de-mon-probleme-quand-je-contacte-openfire.md | échantillonnage neutre dans rubrique (2e fichier) |
| 6 | openfire_zendesk | guides-videos | guides-videos/consulter-l-historique-des-interventions-d-un-client-sur-mobile.md | échantillonnage neutre dans rubrique |
| 7 | openfire_zendesk | configurer-openfire | configurer-openfire/activer-la-facturation-electronique-dans-openfire-et-connecter-super-pdp.md | échantillonnage neutre dans rubrique |
| 8 | openfire_zendesk | utiliser-openfire | utiliser-openfire/comprendre-la-composition-d-une-facture.md | échantillonnage neutre dans rubrique |
| 9 | openfire_odoo | knowsystem | knowsystem/102.md | diversification genre (2e corpus documentaire OpenFire, plateforme distincte) |
| 10 | costructor_help | abonnement | abonnement/comment-ajouter-un-utilisateur-additionnel-j9e14d.md | diversification éditeur + rubrique |
| 11 | costructor_help | equipe-collaborateurs | equipe-collaborateurs/comment-creer-des-modeles-de-feuilles-dheures-2hqkci.md | diversification rubrique |
| 12 | costructor_help | gestion-dentreprise | gestion-dentreprise/comment-fonctionne-le-livre-des-recettes-1bj062h.md | diversification rubrique |
| 13 | costructor_help | imports-exports | imports-exports/comment-exporter-mes-factures-dachats-1ewcnjr.md | diversification rubrique |
| 14 | costructor_help | securite | securite/comment-activer-lauthentification-a-deux-facteurs-17ypgjk.md | diversification rubrique |
| 15 | costructor_help | site-internet | site-internet/comment-creer-son-site-internet-f61wvw.md | diversification rubrique |
| 16 | costructor_help | debuter-sur-costructor | debuter-sur-costructor/comment-activer-la-facturation-electronique-et-comment-fonctionne-t-elle-f1ogg.md | diversification rubrique |
| 17 | costructor_help | achats | achats/comment-creer-un-fournisseur-sous-traitant-1cubnry.md | diversification rubrique |
| 18 | sellsy_help | module-marketing | module-marketing/marketing-5-astuces-pour-maximiser-les-performances-de-vos-newsletters.md | diversification éditeur + rubrique jamais touchée |
| 19 | sellsy_help | module-stocks | module-stocks/activer-la-gestion-des-stocks-pour-les-declinaisons-de-produits.md | diversification rubrique |
| 20 | sellsy_help | module-support | module-support/attacher-un-contact-a-un-ticket.md | diversification rubrique |
| 21 | sellsy_help | module-tresorerie | module-tresorerie/debuter-avec-sellsy-tresorerie.md | diversification rubrique |
| 22 | sellsy_help | rapports-et-pilotage | rapports-et-pilotage/gestion-des-acces-aux-rapports-pour-les-utilisateurs.md | diversification rubrique |
| 23 | sellsy_help | repertoire | repertoire/ajouter-une-adresse-postale-sur-une-societe.md | diversification rubrique |
| 24 | sellsy_help | sellsy-automatisations | sellsy-automatisations/accueillir-vos-nouveaux-clients.md | diversification rubrique |
| 25 | sellsy_help | sellsy-ia | sellsy-ia/decouvrir-sellsy-ia.md | diversification rubrique |
| 26 | axonaut_help | axonaut-et-votre-secteur-activite | axonaut-et-votre-secteur-activite/evenementiel-pourquoi-axonaut-est-adapte-a-votre-activite.md | diversification éditeur + rubrique |
| 27 | axonaut_help | centralisez-gestion-emails-courriers | centralisez-gestion-emails-courriers/ajout-rapide-par-email.md | diversification rubrique |
| 28 | axonaut_help | compte-pro-cartes | compte-pro-cartes/beneficiaire-effectif-quels-documents-sont-acceptes.md | diversification rubrique |
| 29 | axonaut_help | connectez-axonaut | connectez-axonaut/axonaut-zapier-connectez-vos-meilleurs-logiciels.md | diversification rubrique |
| 30 | axonaut_help | creez-campagnes-marketing | creez-campagnes-marketing/boostez-vos-ventes-grace-au-module-segmentation-axonaut.md | diversification rubrique |
| 31 | axonaut_help | creez-depenses-facilement | creez-depenses-facilement/ajouter-un-paiement-sur-une-depense.md | diversification rubrique |
| 32 | axonaut_help | etat-tresorerie-temps-reel | etat-tresorerie-temps-reel/comment-ca-marche-le-menu-pilotage-tresorerie.md | diversification rubrique |
| 33 | axonaut_help | gerez-ressources-humaines | gerez-ressources-humaines/comment-ca-marche-ressources-humaines.md | diversification rubrique |
| 34 | progbat_help | le-menu-principal | le-menu-principal/accueil.md | diversification éditeur + rubrique |
| 35 | progbat_help | pour-bien-demarrer | pour-bien-demarrer/demarrer-avec-progbat.md | diversification rubrique |
| 36 | progbat_help | presentation-generale | presentation-generale/gestion-de-stocks.md | diversification rubrique |
| 37 | progbat_help | assistance | assistance/la-documentation.md | diversification rubrique |
| 38 | batikko_help | guides | guides/chantiers.md | diversification éditeur (seule rubrique disponible) |
| 39 | batikko_help | guides | guides/conformite-2026.md | échantillonnage neutre dans rubrique |
| 40 | batikko_help | guides | guides/connexion-inqom.md | échantillonnage neutre dans rubrique |

**Aucune substitution.** Tous les 40 chemins existent et sont lisibles (vérifié avant lecture de contenu).

## Sorties LIGHT (une ligne ajoutée immédiatement après codage de chaque document)

| # | longueur_mots (approx.) | objet_principal | moment_parcours | capacites_transverses | procedure | transition_objet | regle_ou_condition | contrainte_ou_limite | exception_ou_correction | genre_documentaire |
|---:|---:|---|---|---|:-:|:-:|:-:|:-:|:-:|---|
| 1 | 200 | configuration technique (navigateur/OS) | indetermine | mobile | non | non | oui | oui | non | reference_configuration |
| 2 | 30 | tarif centralisé / catalogue | indetermine | catalogue | non | non | non | non | non | autre (stub vidéo, texte insuffisant pour trancher) |
| 3 | 550 | taxe / TVA (fiscalité) | indetermine | paiement, conformite_reglementaire | oui | non | oui | oui | non | reference_configuration |
| 4 | 1100 | demande de prix / réapprovisionnement | achat | automatisation, gestion_stock, catalogue | oui | oui | oui | oui | non | procedure |
| 5 | 550 | ticket de support / priorité d'incident | indetermine | communication, support_editeur | oui | non | oui | non | oui | procedure |
| 6 | 25 | historique d'interventions client | chantier-intervention | mobile | oui | non | non | non | non | autre (stub vidéo) |
| 7 | 1000 | facturation électronique / plateforme agréée | facturation | integrations, conformite_reglementaire, paiement | oui | oui | oui | oui | oui | procedure |
| 8 | 1250 | facture | facturation | paiement, automatisation | oui | oui | oui | oui | oui | reference_configuration |
| 9 | 15 | indetermine (menu de navigation, pas un article) | indetermine | recherche | non | non | non | non | non | autre |
| 10 | 150 | utilisateur additionnel / abonnement | indetermine | permissions, paiement | oui | non | oui | oui | non | procedure |
| 11 | 140 | feuille d'heures / modèle | chantier-intervention | planning | oui | non | non | non | non | procedure |
| 12 | 220 | livre des recettes (comptabilité) | facturation | catalogue, paiement | oui | oui | oui | non | non | procedure |
| 13 | 120 | facture d'achat / export | achat | documents, paiement | oui | non | oui | oui | non | procedure |
| 14 | 150 | authentification / sécurité du compte | indetermine | securite_compte | oui | non | oui | non | non | procedure |
| 15 | 160 | site internet (vitrine) | indetermine | documents, photos, presence_en_ligne (nouveau) | oui | non | oui | oui | non | procedure |
| 16 | 550 | facturation électronique / plateforme agréée | facturation | integrations, conformite_reglementaire, notifications | oui | oui | oui | oui | oui | procedure |
| 17 | 60 | fournisseur / sous-traitant | achat | — | oui | non | non | non | non | procedure |
| 18 | 350 | newsletter (conseils marketing) | indetermine | communication | non | non | non | non | non | marketing_dans_aide |
| 19 | 250 | produit / déclinaison / stock | indetermine | catalogue, gestion_stock | oui | non | oui | oui | non | procedure |
| 20 | 100 | ticket de support / contact | indetermine | communication | oui | oui | non | non | oui | procedure |
| 21 | 500 | trésorerie (pilotage financier) | indetermine | paiement, automatisation, integrations | oui | non | non | non | non | procedure (ton partiellement promotionnel, cas limite) |
| 22 | 380 | rapport / privilège d'accès | indetermine | permissions, roles | oui | non | oui | non | non | procedure |
| 23 | 200 | adresse (fiche société) | indetermine | recherche, documents | oui | non | oui | non | non | procedure |
| 24 | 400 | automatisation / tâche (accueil client) | indetermine | automatisation, notifications, planning | oui | oui | oui | non | non | procedure |
| 25 | 300 | assistant IA / crédits IA | indetermine | automatisation, integrations, conformite_reglementaire | non | non | oui | oui | non | definitionnel |
| 26 | 320 | indetermine (présentation sectorielle multi-fonctionnalités) | indetermine | documents, communication, planning | non | non | non | non | non | marketing_dans_aide |
| 27 | 300 | prospect / dépense (ajout par email) | demande | communication, notifications, automatisation | oui | oui | oui | non | non | procedure |
| 28 | 280 | bénéficiaire effectif / compte pro bancaire | indetermine | conformite_reglementaire, documents, paiement | non | non | oui | oui | non | definitionnel |
| 29 | 480 | intégration / API (Zapier) | indetermine | integrations, automatisation, recherche | oui | non | non | non | non | procedure (ton partiellement promotionnel) |
| 30 | 550 | segmentation client (CRM) | indetermine | automatisation, communication | oui | oui | oui | non | non | procedure (ton partiellement promotionnel) |
| 31 | 350 | dépense / paiement | achat | paiement, integrations | oui | oui | oui | oui | oui | procedure |
| 32 | 650 | trésorerie / pilotage financier | indetermine | paiement, documents, integrations | non | non | non | non | non | definitionnel |
| 33 | 600 | ressources humaines / congés / bulletin de salaire | indetermine | validation, roles, documents | oui | oui | oui | oui | oui | procedure |
| 34 | 60 | tableau de bord | indetermine | roles | non | non | non | non | non | autre (page d'index, renvoie vers un autre article) |
| 35 | 90 | onboarding / import de données | indetermine | documents, catalogue | non | non | non | oui | non | autre (page d'index) |
| 36 | 200 | gestion de stock (absence assumée) | indetermine | gestion_stock, integrations | non | non | non | oui | non | definitionnel |
| 37 | 120 | documentation / recherche (méta) | indetermine | recherche, automatisation | oui | non | non | non | oui | procedure |
| 38 | 650 | chantier (dossier digital) | chantier-intervention | photos, permissions, notifications | oui | oui | oui | oui | oui | procedure |
| 39 | 550 | facturation électronique / plateforme agréée (PDP) | facturation | conformite_reglementaire, integrations, documents | oui | oui | oui | oui | oui | procedure |
| 40 | 500 | intégration comptable / synchronisation (facture → écriture) | facturation | integrations, permissions, paiement | oui | oui | oui | oui | oui | procedure |

## Répartition `genre_documentaire` (recompte mécanique sur les 40 lignes)

| Genre | Nombre | Part |
|---|---:|---:|
| procedure (dont 3 au ton partiellement promotionnel) | 26 | 65 % |
| autre (stubs vidéo / pages d'index sans contenu exploitable) | 5 | 12,5 % |
| definitionnel | 4 | 10 % |
| reference_configuration | 3 | 7,5 % |
| marketing_dans_aide | 2 | 5 % |
| **Total** | **40** | **100 %** |

## Contrôle qualité

### A — Documents peu structurés (ordre aveugle : source relue → constat indépendant → LIGHT révélé → comparaison)

| # | Constat indépendant (avant de revoir LIGHT) | Comparaison |
|---:|---|---|
| 2 | Intro + lien vidéo, aucune structure factuelle exploitable | Identique à la sortie LIGHT — aucune perte |
| 9 | Liste de titres de menu, pas de phrase, aucune structure | Identique — aucune perte |
| 17 | 3 étapes d'action minimales, aucune règle/contrainte énoncée | Identique — aucune perte |

**Aucune perte structurelle détectée sur les 3 documents peu structurés contrôlés.**

### B — Documents fortement structurés (risque de sur-inclusion)

| # | Vérification | Verdict |
|---:|---|---|
| 33 | Les 5 `oui` correspondent à 5 faits distincts et cités (validation congés, transition bulletin→dépense, limite d'édition des fiches de paie, correction d'erreur) | Pas de sur-inclusion |
| 38 | Cycle de statuts complet, limites par plan chiffrées, restauration après archivage — chaque `oui` adossé à une phrase distincte | Pas de sur-inclusion |
| 40 | `exception_ou_correction: oui` justifié par une FAQ de dépannage réelle en fin d'article, pas une extrapolation | Pas de sur-inclusion |

**Aucune sur-interprétation détectée sur les 3 documents fortement structurés contrôlés.**

## Effets de calibration a posteriori (journalisés, non corrigés rétroactivement)

- Après avoir codé **#16** (Costructor, facturation électronique/Pennylane) et **#39** (Batikko, PDP), je note que **#7** (OpenFire, SUPER PDP) aurait pu recevoir le même `objet_principal` exact (« facturation électronique / plateforme agréée ») dès sa rédaction — c'est le cas, la cohérence a été maintenue sans besoin de correction rétroactive, mais je le signale car ce n'était pas garanti a priori.
- Après **#21** (Sellsy Trésorerie) et **#32** (Axonaut Trésorerie), je remarque que les deux auraient mérité un tag `capacites_transverses` commun plus précis que ceux choisis indépendamment (« paiement, automatisation, integrations » vs « paiement, documents, integrations ») — les deux décisions restent défendables prises isolément, mais un vocabulaire de capacité dédié (« pilotage_financier » ou « tresorerie ») aurait probablement émergé si ces deux documents avaient été codés dans l'ordre inverse ou revus ensemble. Non corrigé, conformément à la consigne.
- Le motif « plateforme agréée / facturation électronique » est apparu de façon indépendante chez **4 éditeurs distincts** (InterFast — Analysis C —, OpenFire #7, Costructor #16, Batikko #39) : je ne l'avais pas anticipé en construisant l'échantillon (sélection neutre, aucun mot-clé lié à la facturation électronique n'a guidé le choix des rubriques), c'est donc une confirmation de fond, pas un artefact de sélection.

## Contrôle de neutralité / découverte

**`objet_principal` — candidats nouveaux conservés** (aucun écarté pour n'apparaître que chez un seul éditeur) : BSFF, CERFA, compte pro bancaire / bénéficiaire effectif, site internet (vitrine gratuite intégrée), trésorerie / pilotage financier (2 éditeurs), segmentation client (IA), assistant IA / crédits IA, ticket de support / priorité d'incident, chantier en tant que dossier digital complet, intégration comptable (Inqom), demande de prix (3e confirmation cross-éditeur après Analysis C).

**`capacites_transverses` — candidats nouveaux conservés** : `gestion_stock`, `conformite_reglementaire` (fiscal + environnemental + facturation électronique — un seul tag pour plusieurs déclinaisons, à trancher plus tard), `securite_compte`, `presence_en_ligne`, `support_editeur`.

**Genres difficiles à classer** : 5 documents sur 40 (#2, #6, #9, #34, #35) sont des pages-stub (vidéo sans transcription, ou page d'index renvoyant vers un autre article) — codées `autre`, sans contenu factuel exploitable. 3 documents (#21, #29, #30) mélangent procédure réelle et ton commercial (« boostez vos ventes », avantages mis en avant) — codés `procedure` avec la réserve notée dans le tableau, plutôt que forcés en `marketing_dans_aide`, car des étapes d'action réelles y figurent.

**Moment du parcours — constat le plus important de ce pilote** : **26 documents sur 40 (65 %)** sont codés `moment_parcours: indetermine`. Aucun cas de conflit multi-moments n'a été rencontré (`cas_multi_moments` : liste vide) — le problème n'est donc pas le caractère scalaire du champ, mais sa **couverture** : l'énumération (demande → devis → chantier → facturation → SAV) décrit bien le cycle commercial client, mais une majorité du contenu réellement rencontré sur un corpus diversifié est **transverse** — paramétrage de compte, sécurité, RH/paie, conformité réglementaire, marketing, IA, intégrations comptables, pilotage de trésorerie — et ne s'y rattache légitimement à aucun moment précis. `indetermine` a été utilisé honnêtement, jamais forcé.

**Limite à retenir.** La vue parcours métier ne couvre qu'environ un tiers du corpus
documentaire de ce pilote. Deux tiers des documents sont transverses — sécurité, RH,
conformité, intégrations, configuration, etc. — et ne se rattachent légitimement à
aucun moment du cycle client. La sélection V3 par moment métier reposera donc sur une
base plus étroite que prévu. Ce n'est pas un défaut du champ, c'est une propriété du
corpus observé.

**Limite connue (§12 de la mission) — recherchée nulle part, observée nulle part sous sa forme silencieuse.** Plusieurs faits de passage vers l'extérieur ou vers un tiers ont été rencontrés (Inqom #40, Chorus Pro #39, Pennylane #16, rapprochement bancaire #31) : dans tous les cas, le texte source signalait explicitement la limite (« reste manuel », « ne sont pas transmis », formulation d'état actuel) — aucun n'était présenté sur un ton neutre indiscernable d'une fonctionnalité normale, contrairement au cas trouvé lors du test sur 12 documents. **La limite connue n'est pas réapparue sous sa forme problématique dans ce pilote.**

## Verdict

`LIGHT_PRET_AVEC_LIMITE_DOCUMENTEE`

La carte reste fidèle et exploitable : aucune perte structurelle détectée en contrôle aveugle, aucune sur-interprétation détectée, la neutralité a fonctionné (13 candidats nouveaux conservés, aucun écarté), et la limite déjà connue ne s'est pas manifestée sous sa forme silencieuse. La limite réelle et nouvellement établie par ce pilote — la faible couverture de `moment_parcours` sur du contenu transverse (65 % `indetermine`) — ne compromet pas la fonction de cartographie : `objet_principal`, `capacites_transverses`, `genre_documentaire` et `contenu_observable` restent renseignés et informatifs même quand `moment_parcours` ne l'est pas. Cette limite est documentée ici pour arbitrage humain, pas corrigée.
