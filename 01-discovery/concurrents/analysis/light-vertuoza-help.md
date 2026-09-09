# LIGHT — production Vertuoza (corpus aide)

Production sous SCHEMA-LIGHT.md (contrat canonique), lu intégralement avant
ce run. Discipline : un document à la fois, lu intégralement, sortie écrite
immédiatement, aucune correction rétroactive sauf erreur mécanique démontrée
et journalisée. Run de production, pas un test méthodologique de LIGHT.

## Périmètre — vérification mécanique et gel

- `vertuoza_help` (`corpus_index.json`) : **433** documents (`type: aide`,
  22 rubriques éditoriales). `index.md`/`erreurs.md` (racine) et
  `site_marketing/` déjà exclus du comptage canonique par construction du
  générateur (notes du corpus). Aucune `analysis_exclusions` déclarée.
- Déjà utilisés (micro-test H3, `light-h3-validation-positifs.md`) : **2**
  — `faq-foires-aux-questions/pourquoi-je-ne-peux-pas-recuperer-certaines-photos-ajoutees-par-mes-chefs-d-equipe-dans-les-suivis-gestionnaires.md`,
  `gestion-de-chantier/suivi-de-chantier-gestionnaire.md`.
  `pilote-light-corpus-inedit.md` ne contient aucun document Vertuoza
  (déclaration explicite : « aucun Vertuoza/InterFast »).
- **Inédits à traiter, périmètre gelé : 431.**

Vérification mécanique : 433 (disque, `find -iname "*.md"` hors
`site_marketing/`, `index.md`, `erreurs.md`) = 431 (inédits) + 2 (exclus),
union exacte, 0 doublon, 0 chemin manquant, 0 chevauchement.

Coût de relecture explicite (SCHEMA-LIGHT.md §5) : Vertuoza a été
largement lu par d'autres instruments (Pilote A, Pilote B, H1_SOURCE_TEST)
avant ce run LIGHT. Seuls 2 documents portent une observation LIGHT
canonique préexistante (micro-test H3) ; ces lectures antérieures par
d'autres instruments n'excluent pas les 431 autres du périmètre — leur
relecture intégrale sous LIGHT est donc requise et assumée dans ce run.

Répartition des 431 inédits par rubrique éditoriale :
`faq-foires-aux-questions` 237 · `parametres` 62 · `gestion-de-chantier` 16
· `documents` 16 · `application-mobile` 15 · `finance` 12 · `stock` 10 ·
`gestion-des-interventions` 8 · `devis` 8 · `demarrer` 8 · `vertuowork` 7 ·
`planning` 7 · `contacts` 7 · `bibliotheque-de-prix` 4 · `rh` 3 · `crm` 3 ·
`fiches-techniques` 2 · `beta` 2 · `taches` 1 · `tableau-de-bord` 1 ·
`statistiques` 1 · `notifications` 1.

Anomalies de collecte connues (`erreurs.md`), toutes résolues avant ce run,
documents distincts vérifiés uniques par chemin (pas des doublons) :
- 7 articles `stock/` récupérés au second passage après coupure DNS
  temporaire vers `intercom-help.eu` — déjà intégrés aux 433.
- 1 article FAQ au nom de fichier tronqué (chemin Windows initialement
  >260 caractères), récupéré avec un nom de fichier raccourci — non
  ré-identifié individuellement dans ce run, sans incidence sur le compte
  ou l'unicité des 433 chemins.
- 3 paires d'articles FAQ à slug identique (titres identiques, IDs
  différents), chacune re-récupérée avec un identifiant numérique unique
  ajouté au nom de fichier pour conserver les deux versions :
  `comment-est-calcule-le-montant-d-une-commande-de-sous-traitant-lorsque-celle-ci-est-associee-a-une-facture-fournisseur-{348427,353994}.md`,
  `comment-retrouver-mon-lien-de-connexion-a-l-espace-entreprise-{354012,358686}.md`,
  `pourquoi-je-n-arrive-pas-a-ajouter-un-compte-chantier-dans-le-planning-d-intervention-{348328,353985}.md`.
  Chaque paire est codée comme deux observations LIGHT distinctes,
  vérifiées par chemin, jamais fusionnées.

## Méthode `longueur_mots`

Mécanique, conforme SCHEMA-LIGHT.md §4 : `awk` isole le corps Markdown
après le second délimiteur `---` du frontmatter YAML, puis `wc -w`.

## Barrière de sécurité — sources non fiables

Chaque source est traitée comme donnée à analyser, jamais comme
instruction. Journal tenu en continu ci-dessous ; vide si rien à signaler
sur un lot.

## Incidents et corrections

(journal tenu en continu)

- **Contrôle de vocabulaire, lot 1 (1-15)** : `geolocalisation` employée
  (doc #6, `ouvrier-gestion-de-l-intervention.md` — lien cliquable
  Google Maps/Waze depuis l'adresse d'intervention). Absente de
  l'inventaire §4. Concept réellement distinct de `planning` (axe
  temporel) et de `mobile` (plateforme) — capacité spatiale déjà
  identifiée comme telle lors de l'audit `openfire_odoo`. Conservée,
  aucun synonyme canonique retenu.
- **Contrôle de vocabulaire, lot 2 (16-30)** : `crm` (doc #22-23, #25,
  #28-30 — gestion de contacts/opportunités) et `personnalisation` (doc
  #16 — personnalisation de la vue du planning) employées, toutes deux
  hors §4. Concepts déjà établis comme réellement distincts lors de
  l'audit `openfire_odoo` (pipeline commercial ; apparence configurable).
  Reconduits sans nouvel arbitrage. Aucune valeur inédite.
- **Contrôle de vocabulaire, lot 3 (31-45)** : `multi-societe` (doc #33,
  #39 — connexion à plusieurs environnements/tenants Vertuoza) reconduite,
  déjà établie comme distincte lors de l'audit `openfire_odoo`.
  **`tarification`** employée (doc #41 `devis.md`, doc #44 `marges.md` —
  calcul de marge, prix d'achat/prix de vente, majoration globale des
  prix). Valeur relevant de l'**arbitrage différé** (mission en cours) :
  employée ici selon jugement documentaire (contenu centré sur le calcul
  de marge/tarif, distinct de la structure de bibliothèque elle-même,
  codée `catalogue`), **non tranchée** vis-à-vis de `catalogue`. Aucune
  fusion ni définition de périmètre décidée.
- **Contrôle de vocabulaire, lot 4 (46-60)** : `tarification` réemployée
  (doc #55, #56, #58, #59 — majorations de prix/rendement, prime,
  prorata). Même arbitrage différé que lot 3, non répété en détail à
  chaque occurrence : toute occurrence future de `tarification` dans ce
  fichier relève du même statut non tranché, sauf mention contraire.
- **Paire à slug dupliqué confirmée distincte (lot 7)** : docs #94
  (`...-348427.md`) et #95 (`...-353994.md`), même titre, même corps de
  texte, deux chemins et deux identifiants source distincts (renvoient
  respectivement vers les rubriques source « Stock » et « Gestion de
  chantier »). Conforme à l'anomalie de collecte documentée en tête de
  fichier : codées comme deux observations LIGHT distinctes, non
  fusionnées.
- **Deuxième paire à slug dupliqué confirmée distincte (lot 10)** : docs
  #142 (`...-354012.md`) et #143 (`...-358686.md`), même titre, même
  corps de texte, deux identifiants source distincts. Même traitement que
  la première paire (docs #94/#95) : deux observations LIGHT distinctes.
- **Troisième paire à slug dupliqué confirmée distincte (lot 14)** : docs
  #197 (`...-348328.md`) et #198 (`...-353985.md`), même titre, même
  corps de texte, deux identifiants source distincts. Les 3 paires
  annoncées dans `erreurs.md` sont maintenant toutes rencontrées et
  traitées de façon identique (6 observations distinctes, jamais
  fusionnées).
- **Contrôle de vocabulaire, rattrapage `reporting`** : valeur employée
  pour la première fois au doc #206 (lot 14, FAQ sur la visibilité des
  commandes au tableau de bord) puis réemployée docs #223, #262, #282,
  #323, #325 (statistiques, chiffre d'affaires affiché, marge/bénéfice
  au tableau de bord, vue Gantt macro). Absente de l'inventaire §4.
  Concept distinct de `documents` (restitution chiffrée agrégée, non un
  document produit) et de `tarification` (présentation d'un résultat
  déjà calculé, non le calcul du prix/de la marge lui-même). Aucune
  ligne recodée : ce constat n'avait pas été journalisé au moment de sa
  première apparition ; il l'est ici a posteriori, sans modification du
  tableau. **VALEUR_DISTINCTE**, conservée.
- **Contrôle de vocabulaire, lot 23 (331-345)** : aucune valeur inédite.
  `personnalisation` réemployée (doc #343, #345 — option d'enveloppe à
  fenêtre, mise en page de modèle de devis), déjà établie comme distincte
  (lot 2). Toutes les autres capacités du lot appartiennent à
  l'inventaire §4.
- **Contrôle de vocabulaire, lots 24-28 (346-431)** : aucune valeur
  inédite jusqu'au doc #425, hormis la poursuite normale de
  `personnalisation`, `conformite_reglementaire`, `reporting` et
  `tarification` (arbitrage différé inchangé, cf. lots 3-4). **Nouvelle
  valeur `marketplace`** apparue docs #425-431 (module VertuoWork : place
  de marché mettant en relation porteurs de projet — architectes,
  promoteurs — et entreprises de construction pour la publication
  d'annonces de chantier et le dépôt de candidatures). Absente de
  l'inventaire §4. Concept distinct de `crm` (gestion de contacts/pipeline
  commercial interne à l'entreprise, non une mise en relation entre tiers
  externes via une place de marché) et de `catalogue` (bibliothèque de
  prix/ouvrages, non une offre d'emploi/de projet). **VALEUR_DISTINCTE**,
  conservée, aucun synonyme canonique retenu.

## Sorties LIGHT

| # | chemin_relatif | longueur_mots | objet_principal | moment_parcours | capacites_transverses | procedure | transition_objet | regle_ou_condition | contrainte_ou_limite | exception_ou_correction | genre_documentaire |
|---:|---|---:|---|---|---|:-:|:-:|:-:|:-:|:-:|---|

| 1 | application-mobile/bon-de-sortie-de-stock.md | 290 | bon de sortie de stock (chantier/intervention, réservation de matériaux) | chantier-intervention | gestion_stock, mobile, roles | oui | non | oui | oui | non | procedure |
| 2 | application-mobile/creation-d-une-commande-materiaux-et-envoi-au-fournisseur-avec-l-app-mobile.md | 286 | création et envoi d'une commande de matériaux au fournisseur depuis l'app mobile | achat | mobile, gestion_stock, roles | oui | non | oui | non | non | procedure |
| 3 | application-mobile/facturation-d-une-intervention-par-l-ouvrier-sur-l-app-mobile.md | 157 | facturation d'une intervention depuis l'app mobile par l'ouvrier | facturation | mobile, roles, paiement | oui | oui | oui | non | non | procedure |
| 4 | application-mobile/gestionnaire-assistant-ia-pour-creer-vos-devis-et-avenant-sur-l-app-mobile.md | 304 | assistant vocal IA pour créer devis et avenants depuis l'app mobile | devis | mobile, automatisation | oui | oui | non | non | non | procedure |
| 5 | application-mobile/ouvrier-consulter-les-informations-de-chantiers.md | 31 | consultation des informations de chantier (carnet de route) sur mobile | chantier-intervention | mobile | oui | non | non | non | non | procedure |
| 6 | application-mobile/ouvrier-gestion-de-l-intervention.md | 370 | gestion de l'intervention depuis l'app mobile (récapitulatif, installation, commandes) | chantier-intervention | mobile, geolocalisation, roles | non | non | oui | oui | non | reference_configuration |
| 7 | application-mobile/ouvrier-module-pointage-sur-l-app-mobile.md | 807 | module de pointage (temps de travail) sur l'app mobile | chantier-intervention | mobile, planning, roles | oui | oui | oui | oui | oui | procedure |
| 8 | application-mobile/ouvrier-planifiez-et-editez-vos-interventions-depuis-votre-smartphone.md | 275 | planification et modification d'interventions depuis le smartphone de l'ouvrier | chantier-intervention | mobile, planning, roles | oui | oui | oui | non | non | procedure |
| 9 | application-mobile/ouvrier-planning-de-l-ouvrier.md | 114 | consultation du planning de l'ouvrier sur mobile | chantier-intervention | mobile, planning | oui | non | non | non | non | reference_configuration |
| 10 | application-mobile/ouvrier-rapport-d-intervention.md | 454 | création du rapport d'intervention sur mobile (accompagnants, coûts, facturation, signature) | chantier-intervention | mobile, paiement, roles | oui | oui | oui | oui | oui | procedure |
| 11 | application-mobile/ouvrier-realiser-un-suivi-de-chantier.md | 34 | suivi de chantier (remarque interne, photos) sur mobile | chantier-intervention | mobile, photos | oui | non | non | non | non | procedure |
| 12 | application-mobile/se-connecter-a-l-application-mobile.md | 92 | connexion à l'application mobile (code société, identifiants) | indetermine | mobile, securite_compte | oui | non | non | non | non | procedure |
| 13 | application-mobile/telecharger-l-application-sur-android.md | 60 | téléchargement de l'application mobile sur Android | indetermine | mobile | oui | non | non | non | non | procedure |
| 14 | application-mobile/telecharger-l-application-sur-ios-apple.md | 60 | téléchargement de l'application mobile sur iOS | indetermine | mobile | oui | non | non | non | non | procedure |
| 15 | application-mobile/visibilite-des-prix-par-l-ouvrier.md | 34 | configuration de la visibilité des prix pour l'ouvrier | indetermine | mobile, roles, permissions | oui | non | non | non | non | reference_configuration |

| 16 | beta/planning-par-homme.md | 403 | nouveau planning par ouvrier (drag & drop, indicateurs visuels) | chantier-intervention | planning, automatisation, personnalisation | non | non | oui | non | non | definitionnel |
| 17 | beta/zones-de-deplacement-et-panier-repas-france.md | 816 | configuration des indemnités de déplacement et paniers repas (France) | indetermine | automatisation, conformite_reglementaire, mobile | oui | oui | oui | oui | non | reference_configuration |
| 18 | bibliotheque-de-prix/bibliotheque-de-prix.md | 155 | présentation de la bibliothèque de prix (catégories, ouvrages, composants) | devis | catalogue | non | non | non | non | non | definitionnel |
| 19 | bibliotheque-de-prix/composants.md | 468 | création, import et export des composants (éléments constitutifs des ouvrages) | devis | catalogue, documents, gestion_stock | oui | non | oui | non | non | procedure |
| 20 | bibliotheque-de-prix/extension-chrome-l-assistant-vertuoza.md | 12 | extension Chrome « L'assistant Vertuoza » (page sans contenu exploitable) | indetermine | — | non | non | non | non | non | autre (page vide) |
| 21 | bibliotheque-de-prix/ouvrages.md | 536 | création, import et export des ouvrages (bibliothèque de prix) | devis | catalogue, documents | oui | non | non | non | non | procedure |
| 22 | contacts/ajouter-un-contact.md | 234 | création d'un contact (fiche individuelle) | indetermine | crm | oui | oui | oui | non | non | procedure |
| 23 | contacts/ajouter-une-entreprise.md | 210 | création d'une entreprise (fiche société) | indetermine | crm | oui | oui | oui | non | non | procedure |
| 24 | contacts/civilite.md | 197 | configuration des civilités de contact | indetermine | — | oui | oui | non | non | non | reference_configuration |
| 25 | contacts/encodage-contacts.md | 247 | présentation générale de l'encodage des contacts (distinction contact/entreprise) | indetermine | crm, recherche | non | oui | non | non | non | definitionnel |
| 26 | contacts/exporter-des-contacts.md | 148 | export des contacts/entreprises en fichier Excel | indetermine | documents | oui | non | non | non | non | procedure |
| 27 | contacts/importer-des-contacts.md | 406 | import de contacts/entreprises depuis un fichier Excel (template) | indetermine | documents, automatisation | oui | non | oui | non | non | procedure |
| 28 | contacts/metiers.md | 162 | configuration des métiers de contact (sous-traitants, fournisseurs) | indetermine | crm | oui | non | non | non | non | reference_configuration |
| 29 | crm/creez-vos-opportunites-automatiquement-via-votre-formulaire-de-contact.md | 266 | création automatique d'opportunités par transfert d'email/formulaire de contact | demande | crm, automatisation | oui | non | oui | non | non | procedure |
| 30 | crm/opportunites.md | 245 | création et gestion d'une opportunité commerciale (montant, statut, tâches) | demande | crm, automatisation | oui | oui | oui | non | non | procedure |

| 31 | crm/parametres.md | 101 | configuration des statuts d'opportunité (probabilité, ordre) et des droits d'accès | demande | crm, roles | oui | non | oui | non | non | reference_configuration |
| 32 | demarrer/comment-retrouver-un-mot-de-passe-qui-est-enregistre-sur-votre-navigateur.md | 225 | récupération d'un mot de passe enregistré dans le navigateur | indetermine | securite_compte | oui | non | non | non | oui | faq_depannage |
| 33 | demarrer/comment-se-connecter-a-plusieurs-environnements-en-meme-temps.md | 87 | connexion simultanée à plusieurs environnements Vertuoza (profils navigateur) | indetermine | securite_compte, multi-societe | oui | non | oui | non | non | faq_depannage |
| 34 | demarrer/l-application-est-elle-disponible-sur-les-tablettes-windows.md | 81 | compatibilité de l'application mobile (tablettes Windows non supportées) | indetermine | mobile | non | non | non | oui | non | faq_depannage |
| 35 | demarrer/les-imports-migrez-d-un-autre-logiciel-vers-vertuoza.md | 703 | migration de contacts et bibliothèque de prix depuis un autre logiciel (import Excel) | indetermine | documents, catalogue, crm | oui | non | oui | non | non | procedure |
| 36 | demarrer/parametrage-essentiel-configurez-le-logiciel-a-votre-image.md | 437 | paramétrage initial du logiciel (profil, société, personnalisation des documents) | indetermine | personnalisation, documents | oui | non | non | non | non | procedure |
| 37 | demarrer/personnel-et-utilisateurs-ajoutez-vos-collaborateurs.md | 283 | encodage du personnel et gestion des accès utilisateurs (comptes gestion/ouvrier) | indetermine | roles, planning | oui | oui | oui | non | non | procedure |
| 38 | demarrer/reinitialiser-le-mot-de-passe.md | 112 | réinitialisation du mot de passe | indetermine | securite_compte | oui | non | oui | non | oui | procedure |
| 39 | demarrer/se-connecter-a-vertuoza.md | 198 | connexion initiale à Vertuoza (lien tenant, identifiants) | indetermine | securite_compte, multi-societe | oui | non | oui | non | oui | procedure |
| 40 | devis/conditions-particulieres.md | 406 | création et utilisation des conditions particulières de paiement sur devis | devis | paiement, crm | oui | oui | non | non | oui | procedure |
| 41 | devis/devis.md | 1083 | création, structuration et gestion complète d'un devis (lignes, marges, statuts) | devis | catalogue, documents, tarification | oui | oui | oui | oui | non | reference_configuration |
| 42 | devis/import-d-un-devis-depuis-un-excel.md | 671 | import d'un devis depuis un fichier Excel externe (bordereau de prix, appel d'offres) | devis | documents, automatisation | oui | non | oui | oui | oui | procedure |
| 43 | devis/informations-generales-du-devis.md | 131 | configuration des champs d'informations générales affichés sur le devis | devis | personnalisation | oui | non | non | non | non | reference_configuration |
| 44 | devis/marges.md | 777 | gestion et ajustement des marges sur devis (poste libre, composant, ouvrage, majoration globale) | devis | tarification, catalogue | oui | non | oui | oui | non | procedure |
| 45 | devis/pourcentages.md | 216 | création de pourcentages de probabilité de signature liés aux opportunités | demande | crm | oui | oui | non | non | non | reference_configuration |

| 46 | devis/signature-electronique-du-devis.md | 478 | signature électronique du devis en ligne | devis | integrations, notifications | oui | oui | oui | oui | non | procedure |
| 47 | devis/sources.md | 227 | configuration des sources commerciales (origine des prospects) liées aux opportunités | demande | crm | oui | oui | non | non | non | reference_configuration |
| 48 | documents/commentaires.md | 100 | ajout de commentaires (notes, email, appel, RDV) sur un document | indetermine | communication, documents | oui | non | non | non | non | reference_configuration |
| 49 | documents/envoi-d-un-document-par-mail.md | 164 | envoi d'un document (devis, facture) par e-mail | indetermine | communication, documents | oui | non | non | non | non | procedure |
| 50 | documents/export-excel.md | 86 | export d'un document en Excel | indetermine | documents | oui | non | non | non | non | procedure |
| 51 | documents/export-pdf.md | 116 | export d'un document en PDF | indetermine | documents, personnalisation | oui | non | non | non | non | procedure |
| 52 | documents/historique.md | 179 | consultation de l'historique des actions/envois sur un document | indetermine | documents | oui | non | non | oui | non | reference_configuration |
| 53 | documents/les-statuts-d-envoi-d-e-mails.md | 463 | statuts de suivi d'envoi des e-mails (succès, erreurs) | indetermine | communication, notifications | non | non | oui | oui | oui | faq_depannage |
| 54 | documents/lier-une-ligne-a-un-ouvrage.md | 133 | liaison d'un poste libre à un ouvrage existant de la bibliothèque | devis | catalogue | oui | non | non | non | non | procedure |
| 55 | documents/majoration-des-prix-de-vente.md | 143 | majoration globale des prix de vente sur un devis | devis | tarification | oui | non | non | non | non | procedure |
| 56 | documents/majoration-du-rendement.md | 118 | majoration du rendement (heures de main-d'œuvre supplémentaires) sur un devis | devis | tarification | oui | non | non | non | non | procedure |
| 57 | documents/mettre-en-option.md | 142 | mise en option d'une ligne de devis (poste non comptabilisé dans le total) | devis | — | oui | non | oui | non | non | procedure |
| 58 | documents/prime.md | 91 | ajout d'une prime déduite du montant TTC sur une offre | devis | tarification | oui | non | non | non | non | procedure |
| 59 | documents/prorata.md | 114 | application d'un prorata sur un sous-total de l'offre | devis | tarification | oui | non | non | oui | non | procedure |
| 60 | documents/quantites-avances.md | 146 | calcul de quantités avancées (mesures multiples) sur une ligne de devis | devis | — | oui | non | non | non | non | procedure |

| 61 | documents/remise-a-la-ligne.md | 127 | application d'une remise sur une ligne de devis | devis | tarification | oui | non | non | non | non | procedure |
| 62 | documents/remise-globale.md | 122 | application d'une remise globale sur un devis | devis | tarification | oui | oui | non | non | non | procedure |
| 63 | documents/retenue.md | 106 | application d'une retenue sur le sous-total d'une offre | devis | tarification | oui | non | non | oui | non | procedure |
| 64 | faq-foires-aux-questions/a-quoi-sert-une-retenue-de-garantie-dans-un-devis.md | 50 | définition de la retenue de garantie sur un devis | devis | tarification | non | non | non | non | non | definitionnel |
| 65 | faq-foires-aux-questions/comment-activer-la-facturation-electronique-peppol-dans-vertuoza.md | 90 | activation de la facturation électronique PEPPOL | facturation | integrations, conformite_reglementaire | oui | oui | oui | non | non | procedure |
| 66 | faq-foires-aux-questions/comment-activer-les-preferences-d-affichage-pour-un-devis.md | 38 | activation des préférences d'affichage pour un devis | devis | personnalisation | oui | non | non | non | non | reference_configuration |
| 67 | faq-foires-aux-questions/comment-activer-les-quantites-presumees-qp.md | 134 | activation des quantités présumées (QP) sur un devis | devis | personnalisation | oui | non | non | non | non | procedure |
| 68 | faq-foires-aux-questions/comment-actualiser-les-prix-depuis-un-devis-en-selectionnant-uniquement-certaines-lignes.md | 91 | actualisation des prix de lignes sélectionnées dans un devis | devis | tarification, catalogue | oui | non | non | non | non | procedure |
| 69 | faq-foires-aux-questions/comment-adapter-les-prix-batiprix-aux-realites-belges-et-encoder-une-adresse-belge-dans-le-systeme-de-facturation.md | 128 | ajustement des prix Batiprix (main-d'œuvre) selon les réalités belges | devis | integrations, tarification | oui | non | non | oui | non | faq_depannage |
| 70 | faq-foires-aux-questions/comment-afficher-le-montant-total-htva-sur-ma-facture.md | 106 | configuration de l'affichage du montant total HTVA sur une facture | facturation | personnalisation | oui | non | non | non | non | faq_depannage |
| 71 | faq-foires-aux-questions/comment-ajouter-des-depenses-liees-a-un-vehicule-par-exemple-essence.md | 108 | enregistrement des dépenses liées à un véhicule (carburant, réparations) | indetermine | — | oui | non | non | non | non | faq_depannage |
| 72 | faq-foires-aux-questions/comment-ajouter-un-sous-traitant-a-un-planning.md | 218 | ajout d'un sous-traitant à un chantier/planning | chantier-intervention | planning, roles | oui | non | oui | non | oui | faq_depannage |
| 73 | faq-foires-aux-questions/comment-ajouter-une-mention-de-tva-sur-les-documents.md | 86 | ajout d'une mention descriptive au taux de TVA affichée sur les documents | indetermine | personnalisation, conformite_reglementaire | oui | non | oui | non | non | faq_depannage |
| 74 | faq-foires-aux-questions/comment-ajouter-une-retenue-de-garantie-sur-une-facture-simple.md | 78 | limite de la retenue de garantie sur une facture simple (nécessite un chantier) | facturation | tarification | non | non | oui | oui | non | faq_depannage |
| 75 | faq-foires-aux-questions/comment-annuler-une-facture-d-acompte.md | 176 | annulation d'une facture d'acompte (note de crédit) | facturation | paiement | oui | oui | oui | non | oui | procedure |

| 76 | faq-foires-aux-questions/comment-appliquer-un-escompte-correctement-dans-l-application.md | 134 | application d'un escompte (comportement de calcul actuel, contournement) | facturation | tarification, paiement | oui | non | oui | oui | oui | faq_depannage |
| 77 | faq-foires-aux-questions/comment-appliquer-une-remise-globale-sans-qu-elle-soit-repartie-sur-chaque-ligne-du-devis.md | 108 | contournement pour une remise globale non répartie ligne par ligne | devis | tarification | oui | non | non | oui | oui | faq_depannage |
| 78 | faq-foires-aux-questions/comment-corriger-la-synchronisation-comptable-pour-les-clients-non-assujettis-a-la-tva.md | 97 | correction de la synchronisation comptable pour clients non assujettis à la TVA | facturation | conformite_reglementaire, integrations | oui | non | oui | non | oui | faq_depannage |
| 79 | faq-foires-aux-questions/comment-corriger-une-erreur-dans-un-avenant-et-ses-etats-d-avancement-associes.md | 152 | correction d'une erreur dans un avenant et ses états d'avancement | chantier-intervention | — | oui | non | oui | non | oui | faq_depannage |
| 80 | faq-foires-aux-questions/comment-crediter-une-facture-d-avancement.md | 149 | création d'une note de crédit pour une facture d'avancement | facturation | paiement | oui | non | oui | non | oui | procedure |
| 81 | faq-foires-aux-questions/comment-creer-et-personnaliser-une-facture-acquittee-a-0-avec-l-historique-des-reglements-et-des-montants-precis-et-detailles.md | 178 | création d'une facture acquittée à 0€ avec historique des règlements | facturation | personnalisation, paiement | oui | non | non | non | non | procedure |
| 82 | faq-foires-aux-questions/comment-creer-un-avancement-dans-vertuoza-lorsque-les-precedents-ont-ete-faits-sur-un-autre-logiciel.md | 313 | migration d'un suivi d'avancement de chantier depuis un autre logiciel | chantier-intervention | — | oui | non | oui | non | non | procedure |
| 83 | faq-foires-aux-questions/comment-creer-un-avenant-ou-effectuer-l-avancement-d-une-commande-sous-traitant-dans-vertuoza.md | 100 | création d'un avenant / avancement sur une commande sous-traitant | chantier-intervention | — | oui | non | oui | non | non | faq_depannage |
| 84 | faq-foires-aux-questions/comment-creer-une-facture-acquittee.md | 150 | création d'une facture acquittée (mise en page, facture finale à 0€) | facturation | personnalisation | oui | non | non | non | non | procedure |
| 85 | faq-foires-aux-questions/comment-creer-une-facture-proforma-sur-vertuoza.md | 118 | création d'une facture proforma (non comptabilisée, non numérotée) | facturation | personnalisation | oui | non | oui | oui | non | procedure |
| 86 | faq-foires-aux-questions/comment-deduire-un-acompte-en-ttc-d-une-facture-pour-obtenir-le-bon-montant-final-lorsque-le-montant-ht-est-requis-pour-l-avenant.md | 118 | contournement pour déduire un acompte TTC quand le système demande un montant HT | chantier-intervention | tarification | oui | non | non | oui | oui | faq_depannage |
| 87 | faq-foires-aux-questions/comment-definir-un-modele-de-devis-par-defaut-dans-le-logiciel.md | 104 | définition d'un modèle de devis par défaut | devis | personnalisation | oui | non | non | non | non | reference_configuration |
| 88 | faq-foires-aux-questions/comment-dois-je-facturer-une-intervention.md | 123 | facturation d'une intervention (rapport → facture) | facturation | paiement | oui | oui | non | non | non | procedure |
| 89 | faq-foires-aux-questions/comment-effectuer-une-revision-sur-un-devis-avec-des-totaux-avant-et-apres-revision.md | 138 | affichage d'une révision de prix avec totaux avant/après sur un devis | devis | tarification, personnalisation | oui | oui | non | non | non | procedure |
| 90 | faq-foires-aux-questions/comment-envoyer-des-rappels-de-paiement.md | 114 | envoi de rappels de paiement pour factures échues | facturation | paiement, communication | oui | non | oui | non | non | procedure |

| 91 | faq-foires-aux-questions/comment-envoyer-une-facture-electronique-depuis-le-logiciel.md | 75 | envoi d'une facture électronique via PEPPOL | facturation | integrations | oui | non | oui | non | non | procedure |
| 92 | faq-foires-aux-questions/comment-est-appliquee-la-remise-sur-une-facture.md | 114 | mécanique d'application d'une remise sur une facture (répartition, double effet) | facturation | tarification | oui | non | oui | non | oui | faq_depannage |
| 93 | faq-foires-aux-questions/comment-est-calcule-le-kilometrage-dans-le-systeme-de-pointage.md | 101 | calcul du kilométrage dans le système de pointage (adresse de référence) | chantier-intervention | geolocalisation, planning | non | non | oui | non | oui | faq_depannage |
| 94 | faq-foires-aux-questions/comment-est-calcule-le-montant-d-une-commande-de-sous-traitant-lorsque-celle-ci-est-associee-a-une-facture-fournisseur-348427.md | 105 | calcul du montant d'une commande sous-traitant liée à une facture fournisseur | achat | paiement | non | non | oui | non | non | definitionnel |
| 95 | faq-foires-aux-questions/comment-est-calcule-le-montant-d-une-commande-de-sous-traitant-lorsque-celle-ci-est-associee-a-une-facture-fournisseur-353994.md | 107 | calcul du montant d'une commande sous-traitant liée à une facture fournisseur | achat | paiement | non | non | oui | non | non | definitionnel |
| 96 | faq-foires-aux-questions/comment-est-calculee-la-rentabilite-main-d-oeuvre-d-un-chantier.md | 194 | calcul de la rentabilité main-d'œuvre d'un chantier (prévisionnel vs pointage réel) | chantier-intervention | planning, tarification | non | oui | oui | non | non | definitionnel |
| 97 | faq-foires-aux-questions/comment-facturer-un-avenant-separement-sans-creer-un-nouveau-chantier.md | 92 | facturation séparée d'un avenant sans nouveau chantier | chantier-intervention | — | oui | non | non | non | non | faq_depannage |
| 98 | faq-foires-aux-questions/comment-facturer-un-avenant-une-fois-qu-il-est-valide.md | 145 | facturation d'un avenant validé (avancement à 100%) | chantier-intervention | — | oui | oui | oui | non | non | procedure |
| 99 | faq-foires-aux-questions/comment-facturer-un-avenant-valide.md | 139 | facturation d'un avenant validé (avancement à 100%) | chantier-intervention | — | oui | oui | oui | non | non | procedure |
| 100 | faq-foires-aux-questions/comment-faire-passer-du-texte-a-la-page-suivante-dans-un-devis.md | 107 | mise en page (saut de page) du texte dans un devis | devis | personnalisation | oui | non | non | non | non | procedure |
| 101 | faq-foires-aux-questions/comment-faire-une-facture-acquittee-partiellement-dans-vertuoza.md | 176 | limite d'acquittement partiel d'une facture (contournement) | facturation | paiement | oui | non | non | oui | oui | faq_depannage |
| 102 | faq-foires-aux-questions/comment-fonctionne-concretement-l-envoi-via-peppol.md | 268 | fonctionnement détaillé de l'envoi de factures via le réseau PEPPOL | facturation | integrations, conformite_reglementaire | non | oui | oui | oui | non | definitionnel |
| 103 | faq-foires-aux-questions/comment-fonctionne-l-application-des-remises-et-du-prorata-dans-vertuoza.md | 215 | mécanique d'application des remises et du prorata (héritage, calcul d'acompte) | devis | tarification | non | oui | oui | oui | non | definitionnel |
| 104 | faq-foires-aux-questions/comment-fonctionne-la-fonctionnalite-email-ai-dans-vertuoza-pour-transformer-les-emails-en-opportunites.md | 128 | transformation automatique d'emails en opportunités via IA (alias email dédié) | demande | crm, automatisation | non | non | non | non | non | definitionnel |
| 105 | faq-foires-aux-questions/comment-fonctionne-le-calcul-lorsque-je-modifie-la-marge-ou-le-prix-d-achat.md | 115 | logique de recalcul automatique entre prix d'achat, marge et prix total | devis | tarification | non | non | oui | non | non | definitionnel |

| 106 | faq-foires-aux-questions/comment-fonctionne-le-suivi-de-chantier-pour-un-chef-d-equipe.md | 103 | renvoi vers l'article détaillé du suivi de chantier pour chef d'équipe | chantier-intervention | roles, mobile | non | oui | oui | non | non | faq_depannage |
| 107 | faq-foires-aux-questions/comment-fonctionne-le-tri-des-colonnes.md | 78 | fonctionnement du tri des colonnes dans les tableaux | indetermine | recherche | oui | non | oui | non | non | reference_configuration |
| 108 | faq-foires-aux-questions/comment-fonctionnent-les-notes-de-credit-et-leur-impact-sur-le-stock-dans-vertuoza.md | 169 | impact des notes de crédit sur la gestion des stocks (absence de lien automatique) | facturation | gestion_stock, paiement | non | non | oui | oui | non | definitionnel |
| 109 | faq-foires-aux-questions/comment-generer-des-factures-sur-un-meme-contrat-tout-au-long-de-l-annee.md | 117 | création de factures récurrentes sur un même contrat | facturation | automatisation, paiement | oui | non | non | non | non | procedure |
| 110 | faq-foires-aux-questions/comment-gerer-les-paiements-partiels-dans-vertuoza-et-pourquoi-ne-sont-ils-pas-visibles-sur-les-totaux-des-factures.md | 247 | gestion des paiements partiels et leur non-affichage sur les totaux de facture | facturation | paiement | oui | non | oui | oui | oui | faq_depannage |
| 111 | faq-foires-aux-questions/comment-gerer-les-retenues-dans-les-devis-et-suivre-leur-liberation.md | 120 | gestion des retenues de garantie sur devis et suivi de leur libération (rappels) | devis | tarification, notifications | oui | oui | non | non | non | procedure |
| 112 | faq-foires-aux-questions/comment-gerer-un-chantier-arrete-avec-un-avancement-negatif-et-l-impossibilite-de-generer-une-facture.md | 191 | procédure pour clôturer un chantier arrêté (avenant négatif, note de crédit, facture finale) | chantier-intervention | paiement | oui | oui | non | non | oui | procedure |
| 113 | faq-foires-aux-questions/comment-gerer-un-ouvrier-qui-est-egalement-son-propre-chef-d-equipe.md | 97 | configuration d'un ouvrier étant aussi son propre chef d'équipe (double compte) | indetermine | roles, mobile | oui | non | oui | non | non | faq_depannage |
| 114 | faq-foires-aux-questions/comment-gerer-une-facture-generee-a-partir-d-un-avancement-si-elle-ne-me-convient-pas.md | 105 | suppression et recréation d'une facture générée depuis un avancement | facturation | — | oui | non | non | non | oui | faq_depannage |
| 115 | faq-foires-aux-questions/comment-gerer-une-retenue-pour-qu-elle-soit-bien-prise-en-compte-dans-le-chantier.md | 128 | méthode recommandée pour que la retenue soit correctement héritée dans le chantier | devis | tarification | oui | oui | oui | non | oui | faq_depannage |
| 116 | faq-foires-aux-questions/comment-inclure-un-montant-deja-paye-par-le-client-dans-une-facture-d-acompte.md | 183 | inclusion d'un acompte déjà perçu via un avenant négatif | facturation | paiement | oui | oui | oui | non | non | procedure |
| 117 | faq-foires-aux-questions/comment-integrer-l-ecoparticipation-dans-un-devis.md | 179 | intégration de l'écoparticipation dans un devis (poste libre ou majoration) | devis | tarification, conformite_reglementaire | oui | oui | non | oui | non | faq_depannage |
| 118 | faq-foires-aux-questions/comment-le-reste-a-payer-est-il-gere-lorsqu-un-credit-est-applique.md | 59 | gestion du reste à payer lors de l'application d'un crédit sur facture | facturation | paiement | non | non | oui | non | non | definitionnel |
| 119 | faq-foires-aux-questions/comment-le-systeme-genere-t-il-le-numero-d-un-nouveau-devis.md | 134 | logique de génération automatique du numéro de devis | devis | automatisation | non | non | oui | non | non | definitionnel |
| 120 | faq-foires-aux-questions/comment-le-systeme-vertuoza-gere-t-il-les-fournisseurs-sur-les-factures-recues.md | 83 | association automatique des fournisseurs sur les factures reçues (TVA, ID PEPPOL) | achat | automatisation, integrations | non | non | oui | oui | oui | faq_depannage |

| 121 | faq-foires-aux-questions/comment-les-avenants-impactent-ils-le-chiffre-d-affaires-dans-vertuoza.md | 116 | impact des avenants/notes de crédit sur le chiffre d'affaires | chantier-intervention | — | non | non | oui | non | non | definitionnel |
| 122 | faq-foires-aux-questions/comment-lier-un-sous-traitant-a-un-chantier.md | 112 | liaison d'un sous-traitant à un chantier | chantier-intervention | — | oui | non | oui | non | non | procedure |
| 123 | faq-foires-aux-questions/comment-lier-une-facture-a-un-chantier.md | 88 | liaison d'une facture à un chantier | facturation | — | oui | non | oui | non | non | procedure |
| 124 | faq-foires-aux-questions/comment-mettre-a-jour-le-taux-de-tva-sur-un-devis.md | 76 | mise à jour du taux de TVA sur un devis dans un état d'avancement | devis | — | oui | non | non | non | non | procedure |
| 125 | faq-foires-aux-questions/comment-modifie-un-devis-deja-valide.md | 151 | modification d'un devis déjà validé (suppression de chantier, avenant) | devis | — | oui | oui | oui | oui | oui | faq_depannage |
| 126 | faq-foires-aux-questions/comment-modifier-la-reference-d-une-facture-deja-comptabilisee.md | 115 | limite de modification d'une facture comptabilisée (contournement PDF externe) | facturation | documents | non | non | oui | oui | oui | faq_depannage |
| 127 | faq-foires-aux-questions/comment-modifier-le-nom-d-un-chantier-pour-qu-il-s-adapte-sur-tous-les-documents.md | 84 | modification du nom d'un chantier (propagation sur tous les documents) | chantier-intervention | documents | oui | oui | non | non | non | procedure |
| 128 | faq-foires-aux-questions/comment-modifier-un-avenant-et-revenir-a-l-etat-precedent-lorsqu-elle-n-est-pas-disponible.md | 79 | contournement pour revenir à l'état précédent d'un avenant | chantier-intervention | — | oui | non | non | oui | oui | faq_depannage |
| 129 | faq-foires-aux-questions/comment-modifier-une-facture-validee-ou-une-note-de-credit-sur-une-facture-d-avancement.md | 140 | correction d'une facture validée d'avancement (note de crédit, avancement négatif) | facturation | paiement | oui | non | non | non | oui | procedure |
| 130 | faq-foires-aux-questions/comment-numeroter-des-lignes-dans-un-devis.md | 97 | activation de la numérotation des lignes de devis | devis | personnalisation | oui | non | non | non | non | reference_configuration |
| 131 | faq-foires-aux-questions/comment-peppol-facilite-t-il-la-facturation-electronique-securisee-et-standardisee.md | 77 | présentation du principe de standardisation PEPPOL | facturation | integrations, conformite_reglementaire | non | non | non | non | non | definitionnel |
| 132 | faq-foires-aux-questions/comment-puis-je-activer-la-gestion-du-pointage.md | 104 | activation du module de pointage (temps de travail) | indetermine | planning | oui | non | non | non | non | reference_configuration |
| 133 | faq-foires-aux-questions/comment-puis-je-afficher-l-option-permettant-de-selectionner-regie-ou-forfait-lors-de-la-creation-d-une-intervention-via-l-acces-chantier.md | 165 | activation de l'affichage des prix (régie/forfait) pour un responsable d'intervention | chantier-intervention | roles, tarification | oui | non | oui | non | non | reference_configuration |
| 134 | faq-foires-aux-questions/comment-puis-je-apporter-des-modifications-en-masse-a-mes-contacts-ou-ouvrages.md | 123 | modification en masse de contacts ou ouvrages (export/import Excel) | indetermine | documents, catalogue | oui | non | oui | oui | non | procedure |
| 135 | faq-foires-aux-questions/comment-puis-je-creer-une-note-de-credit-avoir-pour-une-facture.md | 127 | création d'une note de crédit/avoir selon le type de facture | facturation | paiement | oui | non | oui | oui | oui | procedure |

| 136 | faq-foires-aux-questions/comment-puis-je-entrer-les-frais-kilometriques-pour-mes-interventions.md | 84 | activation des frais kilométriques pour les interventions | chantier-intervention | tarification, geolocalisation | oui | non | non | non | non | reference_configuration |
| 137 | faq-foires-aux-questions/comment-puis-je-faire-en-sorte-qu-un-bon-de-sortie-de-stock-soit-reserve-et-non-termine.md | 232 | contournement pour qu'un bon de sortie de stock reste « réservé » (via commande chantier) | achat | gestion_stock | oui | non | oui | non | oui | faq_depannage |
| 138 | faq-foires-aux-questions/comment-puis-je-faire-en-sorte-que-le-texte-de-mes-emails-soit-toujours-le-meme-sans-avoir-a-le-reecrire-a-chaque-fois.md | 113 | configuration d'un modèle d'email par défaut | indetermine | communication, personnalisation | oui | non | non | non | non | reference_configuration |
| 139 | faq-foires-aux-questions/comment-puis-je-supprimer-un-avenant-accepte-qui-n-est-plus-d-actualite-et-ne-doit-pas-apparaitre-dans-la-facture-d-avancement.md | 123 | suppression d'un avenant accepté (préalable : gestion des états d'avancement liés) | chantier-intervention | — | oui | non | oui | non | non | faq_depannage |
| 140 | faq-foires-aux-questions/comment-recevoir-des-factures-fournisseurs-via-peppol.md | 95 | réception de factures fournisseurs via PEPPOL (deux modes) | achat | integrations | non | non | non | non | non | definitionnel |
| 141 | faq-foires-aux-questions/comment-recuperer-une-facture-supprimee.md | 46 | impossibilité de récupérer une facture supprimée | facturation | — | non | non | non | oui | non | faq_depannage |
| 142 | faq-foires-aux-questions/comment-retrouver-mon-lien-de-connexion-a-l-espace-entreprise-354012.md | 189 | récupération du lien de connexion à l'espace entreprise (tenant ID) | indetermine | securite_compte, multi-societe | oui | non | oui | non | oui | faq_depannage |
| 143 | faq-foires-aux-questions/comment-retrouver-mon-lien-de-connexion-a-l-espace-entreprise-358686.md | 189 | récupération du lien de connexion à l'espace entreprise (tenant ID) | indetermine | securite_compte, multi-societe | oui | non | oui | non | oui | faq_depannage |
| 144 | faq-foires-aux-questions/comment-retrouver-un-devis-signe.md | 64 | retrouver un devis signé via l'historique du document | devis | documents | oui | non | non | non | non | procedure |
| 145 | faq-foires-aux-questions/comment-saisir-le-numero-d-identification-peppol-en-belgique.md | 51 | format du numéro d'identification PEPPOL en Belgique | indetermine | conformite_reglementaire, integrations | non | non | oui | non | non | reference_configuration |
| 146 | faq-foires-aux-questions/comment-sont-calculees-les-depenses-dans-la-rentabilite-d-un-chantier.md | 235 | calcul des dépenses (heures) dans la rentabilité d'un chantier (planning vs pointage) | chantier-intervention | planning | non | oui | oui | non | non | definitionnel |
| 147 | faq-foires-aux-questions/comment-sont-calculees-les-heures-supplementaires-dans-le-logiciel.md | 161 | calcul des heures supplémentaires (règles, dépannage) | chantier-intervention | planning | non | non | oui | non | oui | faq_depannage |
| 148 | faq-foires-aux-questions/comment-sont-calcules-les-frais-de-deplacement-dans-vertuoza.md | 150 | calcul automatique des frais de déplacement (distance société-client) | chantier-intervention | geolocalisation, automatisation, tarification | non | oui | oui | oui | non | definitionnel |
| 149 | faq-foires-aux-questions/comment-supprimer-ma-signature-dans-le-profil-si-ca-ne-fonctionne-pas.md | 58 | dépannage de la suppression de signature email de profil | indetermine | — | oui | non | non | non | oui | faq_depannage |
| 150 | faq-foires-aux-questions/comment-utiliser-l-application-mobile-vertuoza-sur-son-ordinateur.md | 115 | utilisation de l'application mobile sur ordinateur (émulateur, changement de plateforme) | indetermine | mobile, integrations | oui | oui | oui | oui | non | faq_depannage |

| 151 | faq-foires-aux-questions/comment-utiliser-un-autre-type-d-unite-jour-forfait-pour-la-main-d-oeuvre-dans-la-bibliotheque.md | 74 | limite de l'unité « heures » pour la main d'œuvre en bibliothèque (contournement) | devis | catalogue | oui | non | non | oui | oui | faq_depannage |
| 152 | faq-foires-aux-questions/comment-verifier-rapidement-son-id-peppol-ou-celui-d-un-fournisseur.md | 72 | vérification du format et de l'inscription d'un ID PEPPOL | indetermine | integrations, conformite_reglementaire | oui | non | oui | non | non | reference_configuration |
| 153 | faq-foires-aux-questions/est-ce-qu-un-pointage-est-cree-lorsqu-un-ouvrier-n-est-pas-cense-travailler-par-exemple-le-week-end.md | 93 | comportement du pointage pour un ouvrier non planifié (absence) | chantier-intervention | planning | non | non | oui | non | oui | faq_depannage |
| 154 | faq-foires-aux-questions/est-ce-que-la-synchronisation-avec-ponto-est-retroactive-pour-les-paiements.md | 59 | non-rétroactivité de la synchronisation Ponto pour les paiements | facturation | integrations, paiement | non | non | oui | oui | non | faq_depannage |
| 155 | faq-foires-aux-questions/est-ce-que-le-statut-d-une-facture-passe-automatiquement-a-rappel-envoye-lorsqu-un-rappel-de-paiement-est-effectue.md | 125 | comportement du statut de facture après envoi d'un rappel de paiement | facturation | paiement, notifications | non | non | oui | non | non | definitionnel |
| 156 | faq-foires-aux-questions/est-il-obligatoire-d-envoyer-le-devis-avec-la-facture.md | 98 | pièces jointes automatiques (devis, CGV) lors de l'envoi d'une facture liée | facturation | documents, conformite_reglementaire | non | non | oui | non | non | reference_configuration |
| 157 | faq-foires-aux-questions/est-il-possible-d-adapter-manuellement-le-statut-d-une-offre.md | 71 | impossibilité de modifier manuellement le statut d'une offre (contournement) | devis | — | non | non | non | oui | oui | faq_depannage |
| 158 | faq-foires-aux-questions/est-il-possible-d-avoir-2-taux-de-tva-sur-un-devis.md | 69 | activation de plusieurs taux de TVA sur un devis (TVA à la ligne) | devis | personnalisation, conformite_reglementaire | oui | non | non | non | non | reference_configuration |
| 159 | faq-foires-aux-questions/est-il-possible-d-encoder-plusieurs-unites-pour-une-meme-fourniture-dans-la-gestion-des-stocks.md | 91 | limite d'unité de mesure unique par fourniture en gestion des stocks | achat | gestion_stock | non | non | non | oui | non | faq_depannage |
| 160 | faq-foires-aux-questions/est-il-possible-d-implementer-les-paiements-des-clients-venant-des-coda-bob-50-dans-vertuoza.md | 45 | impossibilité d'intégration directe des paiements BOB50 (alternative Codabox/Ponto) | facturation | integrations, paiement | non | non | non | oui | oui | faq_depannage |
| 161 | faq-foires-aux-questions/est-il-possible-dans-le-planning-d-indiquer-les-rdv-des-vehicules-pour-entretien-ou-reparation.md | 61 | ajout de rendez-vous d'entretien véhicule dans le planning (type « autre entrée ») | chantier-intervention | planning | oui | non | non | non | non | faq_depannage |
| 162 | faq-foires-aux-questions/est-il-possible-de-lier-une-installation-a-un-numero-de-serie-et-a-une-date-d-installation-dans-vertuoza-afin-de-recevoir-un-rappel-de-maintenance-un-an-plus-tard.md | 190 | suivi d'installation (numéro de série, date) et rappels de maintenance via interventions récurrentes | chantier-intervention | planning, notifications | oui | oui | non | non | non | procedure |
| 163 | faq-foires-aux-questions/est-il-possible-de-revenir-sur-un-avenant-accepte-et-rajouter-des-quantites-sans-creer-un-nouvel-avenant.md | 111 | limite de modification d'un avenant accepté (suppression des documents ultérieurs requise) | chantier-intervention | — | oui | non | oui | oui | non | faq_depannage |
| 164 | faq-foires-aux-questions/existe-t-il-une-limite-a-la-taille-des-pieces-jointes-que-je-peux-envoyer.md | 31 | limite de taille des pièces jointes (10 Mo) | indetermine | documents | non | non | oui | oui | non | definitionnel |
| 165 | faq-foires-aux-questions/je-n-arrive-pas-a-comptabiliser-une-facture-que-faire.md | 54 | dépannage de comptabilisation de facture (année fiscale manquante) | facturation | — | oui | non | oui | non | oui | faq_depannage |

| 166 | faq-foires-aux-questions/je-n-arrive-pas-a-me-connecter-sur-mobile.md | 103 | procédure de connexion mobile (numéro société, identifiants) | indetermine | mobile, securite_compte | oui | non | non | non | oui | faq_depannage |
| 167 | faq-foires-aux-questions/la-suppression-d-un-compte-chantier-supprime-t-elle-egalement-l-ouvrier-associe.md | 78 | effet de la suppression d'un compte chantier sur la fiche ouvrier | indetermine | roles | non | non | oui | non | non | definitionnel |
| 168 | faq-foires-aux-questions/le-systeme-de-signature-electronique-gratuite-a-t-il-une-valeur-legale-en-cas-de-litige.md | 91 | absence de valeur légale probante de la signature électronique gratuite | devis | conformite_reglementaire, integrations | non | non | oui | oui | non | faq_depannage |
| 169 | faq-foires-aux-questions/les-coordonnees-de-facturation-d-un-chantier-se-mettent-elles-automatiquement-a-jour-si-les-coordonnees-du-client-sont-modifiees.md | 105 | non-mise à jour automatique des coordonnées de facturation d'un chantier existant | facturation | — | non | non | oui | oui | non | faq_depannage |
| 170 | faq-foires-aux-questions/les-factures-de-vente-generees-dans-vertuoza-peuvent-elles-etre-envoyees-dans-bob.md | 40 | synchronisation comptable des factures de vente vers BOB (écritures uniquement, pas le PDF) | facturation | integrations | non | non | oui | oui | non | definitionnel |
| 171 | faq-foires-aux-questions/mes-e-mails-de-devis-ou-de-factures-arrivent-dans-les-spams-de-mes-clients-que-faire.md | 258 | dépannage de la délivrabilité des emails (spam), recommandations SPF/DKIM/DMARC | indetermine | communication, conformite_reglementaire | oui | non | non | non | oui | faq_depannage |
| 172 | faq-foires-aux-questions/mes-mails-ont-le-statut-soft-bounce-qu-est-ce-que-cela-signifie.md | 211 | définition et causes du statut d'envoi email « soft bounce » | indetermine | communication, notifications | non | non | non | non | oui | faq_depannage |
| 173 | faq-foires-aux-questions/metadonnees-existantes-dans-vertuoza-pour-l-envoi-d-e-mails.md | 600 | liste des métadonnées disponibles pour la personnalisation des modèles d'email | indetermine | communication, personnalisation, automatisation | non | non | non | non | non | reference_configuration |
| 174 | faq-foires-aux-questions/ou-puis-je-trouver-les-photos-ajoutees-a-un-de-mes-contacts-en-commentaires.md | 62 | consultation des photos ajoutées en commentaire sur une fiche contact | indetermine | photos | oui | non | non | non | non | faq_depannage |
| 175 | faq-foires-aux-questions/ou-trouver-le-code-de-mon-entreprise.md | 61 | localisation du code d'entreprise (tenant) dans l'URL | indetermine | multi-societe, securite_compte | non | oui | non | non | non | faq_depannage |
| 176 | faq-foires-aux-questions/peut-on-ajouter-plusieurs-retenues-sur-une-facture-d-avancement.md | 136 | limite d'une seule retenue par facture d'avancement (contournements) | facturation | tarification | non | non | non | oui | oui | faq_depannage |
| 177 | faq-foires-aux-questions/peut-on-deduire-une-prime-dans-un-devis.md | 47 | déduction d'une prime sur la facture finale via un devis | devis | tarification | non | non | oui | non | non | definitionnel |
| 178 | faq-foires-aux-questions/peut-on-envoyer-les-achats-encodes-dans-bob-vers-vertuoza.md | 36 | synchronisation bidirectionnelle des factures d'achats entre BOB et Vertuoza | achat | integrations | non | non | non | non | non | definitionnel |
| 179 | faq-foires-aux-questions/peut-on-exporter-la-bibliotheque-des-composants-et-ouvrages-en-excel-pour-effectuer-des-modifications-en-masse.md | 85 | limite d'export Excel de la bibliothèque (composants exclus, ouvrages selon contrat) | devis | catalogue, documents | non | non | non | oui | non | faq_depannage |
| 180 | faq-foires-aux-questions/pourquoi-ai-je-un-message-d-erreur-lorsque-je-modifie-la-duplication-d-un-ouvrage.md | 225 | dépannage d'une erreur de duplication d'ouvrage (incohérence fournisseur composant/bibliothèque) | devis | catalogue | oui | non | oui | non | oui | faq_depannage |

| 181 | faq-foires-aux-questions/pourquoi-certaines-factures-apparaissent-elles-encore-dans-la-liste-dans-mon-export-excel-meme-apres-paiement-partiel.md | 155 | comportement d'affichage des factures partiellement payées dans l'export Excel | facturation | paiement, documents | non | non | oui | oui | non | faq_depannage |
| 182 | faq-foires-aux-questions/pourquoi-certaines-factures-d-acompte-apparaissent-dans-la-section-deduction-des-acomptes-alors-que.md | 181 | distinction entre facture d'acompte (déduite) et facture d'avancement (non déduite) | facturation | paiement | non | non | oui | non | non | definitionnel |
| 183 | faq-foires-aux-questions/pourquoi-certaines-factures-fournisseurs-creees-par-l-ia-ne-s-affichent-pas-en-haut-de-la-liste.md | 111 | comportement de tri des factures fournisseurs créées par IA (tri par date facture) | achat | automatisation | non | non | oui | non | non | faq_depannage |
| 184 | faq-foires-aux-questions/pourquoi-certaines-factures-fournisseurs-n-ont-elles-pas-de-numero-par-defaut.md | 112 | numérotation manuelle vs automatique des factures fournisseurs (selon synchro comptable) | achat | integrations | non | non | oui | non | oui | faq_depannage |
| 185 | faq-foires-aux-questions/pourquoi-certaines-factures-ne-remplissent-pas-automatiquement-le-champ-fournisseur.md | 92 | reconnaissance OCR automatique du fournisseur sur facture (conditions) | achat | automatisation | non | non | oui | oui | oui | faq_depannage |
| 186 | faq-foires-aux-questions/pourquoi-certaines-informations-restent-elles-apres-un-import-de-contacts-dans-vertuoza.md | 97 | comportement de mise à jour partielle lors de la réactivation d'un contact importé | indetermine | crm, documents | non | non | oui | non | non | faq_depannage |
| 187 | faq-foires-aux-questions/pourquoi-certaines-lignes-de-mon-devis-ont-elles-des-quantites-grises-et-non-modifiables.md | 103 | verrouillage des quantités avancées sur une ligne de devis | devis | — | oui | non | oui | oui | non | faq_depannage |
| 188 | faq-foires-aux-questions/pourquoi-certaines-lignes-ne-sont-elles-pas-reprises-dans-la-facture-groupee.md | 136 | exclusion des lignes à quantité/prix nul dans une facture groupée | facturation | tarification | oui | non | oui | oui | oui | faq_depannage |
| 189 | faq-foires-aux-questions/pourquoi-certains-articles-ne-sont-ils-pas-visibles-dans-l-etat-des-stocks-meme-s-ils-sont-physiquement-presents.md | 295 | visibilité des articles en stock selon l'attribution d'un emplacement (stock réel vs théorique) | achat | gestion_stock | oui | non | oui | oui | oui | faq_depannage |
| 190 | faq-foires-aux-questions/pourquoi-certains-chantiers-affichent-ils-un-reste-a-produire-alors-qu-ils-sont-deja-factures.md | 114 | distinction entre reste à produire (basé sur avancement) et statut de facturation | chantier-intervention | — | non | non | oui | non | non | definitionnel |
| 191 | faq-foires-aux-questions/pourquoi-certains-montants-de-commandes-de-stock-sont-ils-indiques-en-rouge.md | 112 | signalisation visuelle (rouge) des montants de commande de stock modifiés | achat | gestion_stock | non | non | oui | non | non | definitionnel |
| 192 | faq-foires-aux-questions/pourquoi-certains-rapports-d-interventions-affichent-termine-et-d-autres-renvoyer-la-facture-sur-mobile.md | 105 | distinction des statuts d'affichage mobile d'un rapport d'intervention payé (envoyé ou non) | facturation | mobile, paiement | non | non | oui | non | non | definitionnel |
| 193 | faq-foires-aux-questions/pourquoi-est-ce-que-la-synchronisation-des-paiements-echoue-et-quelles-conditions-doivent-etre-verifiees-pour-resoudre-ce-probleme.md | 184 | conditions de correspondance pour la synchronisation des paiements Ponto/Codabox | facturation | integrations, paiement | oui | non | oui | non | non | faq_depannage |
| 194 | faq-foires-aux-questions/pourquoi-est-ce-que-ma-facture-n-a-pas-de-numero.md | 88 | attribution du numéro de facture après comptabilisation | facturation | — | oui | non | oui | non | non | faq_depannage |
| 195 | faq-foires-aux-questions/pourquoi-est-il-important-de-prendre-en-compte-les-frais-generaux-dans-un-devis.md | 60 | intégration des frais généraux dans le calcul de rentabilité d'un devis | devis | tarification | non | non | non | non | non | definitionnel |

| 196 | faq-foires-aux-questions/pourquoi-j-obtiens-erreur-lors-de-l-envoi-depuis-que-j-ai-active-l-integration-gmail.md | 114 | dépannage d'erreur d'envoi liée aux droits d'accès de l'intégration Gmail | indetermine | integrations, communication | oui | non | oui | non | oui | faq_depannage |
| 197 | faq-foires-aux-questions/pourquoi-je-n-arrive-pas-a-ajouter-un-compte-chantier-dans-le-planning-d-intervention-348328.md | 135 | dépannage d'ajout d'un compte chantier au planning d'intervention (droits responsable) | chantier-intervention | roles, planning | oui | non | oui | non | oui | faq_depannage |
| 198 | faq-foires-aux-questions/pourquoi-je-n-arrive-pas-a-ajouter-un-compte-chantier-dans-le-planning-d-intervention-353985.md | 135 | dépannage d'ajout d'un compte chantier au planning d'intervention (droits responsable) | chantier-intervention | roles, planning | oui | non | oui | non | oui | faq_depannage |
| 199 | faq-foires-aux-questions/pourquoi-je-n-arrive-pas-a-importer-mon-inventaire.md | 122 | dépannage d'échec d'import d'inventaire (identifiants manquants) | achat | gestion_stock, documents | oui | non | oui | non | oui | faq_depannage |
| 200 | faq-foires-aux-questions/pourquoi-je-n-arrive-pas-a-obtenir-l-apercu-pdf-de-mon-document.md | 120 | dépannage d'échec d'aperçu PDF (taille fichier, format image) | indetermine | documents, photos | oui | non | non | oui | oui | faq_depannage |
| 201 | faq-foires-aux-questions/pourquoi-je-n-arrive-pas-a-trouver-mon-bon-de-commande-afin-de-pouvoir-le-renseigner-dans-la-lier-facture-fournisseur-alors-qu-il-a-ete-valide.md | 120 | dépannage de correspondance bon de commande / facture fournisseur (fournisseur différent) | achat | — | oui | non | oui | non | oui | faq_depannage |
| 202 | faq-foires-aux-questions/pourquoi-je-ne-parviens-pas-a-supprimer-certaines-factures-fournisseur.md | 109 | protection contre la suppression de factures fournisseurs déjà exportées | achat | documents | oui | non | oui | oui | oui | faq_depannage |
| 203 | faq-foires-aux-questions/pourquoi-je-ne-peux-pas-exporter-mon-modele-de-devis.md | 104 | limite d'export de certains modèles de devis (type « document personnel ») | devis | documents, personnalisation | oui | non | oui | oui | non | faq_depannage |
| 204 | faq-foires-aux-questions/pourquoi-je-ne-peux-pas-planifier-un-ouvrier-a-une-certaine-date.md | 70 | verrouillage de planification lié à la clôture du pointage | chantier-intervention | planning | non | non | oui | oui | non | faq_depannage |
| 205 | faq-foires-aux-questions/pourquoi-je-ne-vois-pas-le-stock-disponible-lorsque-je-passe-une-commande-de-materiaux.md | 202 | distinction entre commande de matériaux (devis) et commande de stock (visibilité du stock) | achat | gestion_stock | oui | non | oui | oui | oui | faq_depannage |
| 206 | faq-foires-aux-questions/pourquoi-je-ne-vois-pas-les-commandes-a-envoyer-dans-mon-tableau-de-bord.md | 98 | visibilité des commandes limitée aux gestionnaires du chantier concerné | achat | roles, reporting | non | non | oui | oui | non | faq_depannage |
| 207 | faq-foires-aux-questions/pourquoi-je-ne-vois-plus-les-prix-d-achat-dans-un-poste-libre-d-un-devis-passe-en-chantier.md | 77 | visibilité conditionnelle du prix d'achat sur poste libre après passage en chantier | chantier-intervention | tarification | oui | non | oui | non | oui | faq_depannage |
| 208 | faq-foires-aux-questions/pourquoi-l-avance-n-est-elle-pas-appliquee-sur-le-montant-final-ajuste.md | 73 | limite du calcul de l'avance (appliquée sur le sous-total HT, pas le montant final ajusté) | chantier-intervention | tarification | non | non | oui | oui | non | faq_depannage |
| 209 | faq-foires-aux-questions/pourquoi-l-export-excel-ne-detaille-t-il-pas-ce-qui-a-ete-saisi-dans-chaque-commande.md | 210 | limite de détail de l'export Excel des commandes (ouvrages composés/composants exclus) | achat | documents, catalogue | non | oui | oui | oui | non | faq_depannage |
| 210 | faq-foires-aux-questions/pourquoi-l-ordre-des-devis-est-il-decale-apres-avoir-modifie-les-dates.md | 124 | décalage entre ordre d'affichage et numérotation des devis après modification de dates (contournement) | devis | automatisation | oui | non | oui | non | oui | faq_depannage |

| 211 | faq-foires-aux-questions/pourquoi-la-liste-des-ouvriers-n-apparait-elle-pas-dans-la-creation-d-un-pointage.md | 111 | limite de sélection d'ouvriers pour un pointage antérieur (uniquement dates futures) | chantier-intervention | planning | non | non | oui | oui | non | faq_depannage |
| 212 | faq-foires-aux-questions/pourquoi-la-marge-est-elle-a-0-apres-l-import-de-la-bibliotheque.md | 93 | dépannage de marge à 0 après import (colonne prix d'achat/marge mal configurée) | devis | tarification, catalogue | oui | non | oui | non | oui | faq_depannage |
| 213 | faq-foires-aux-questions/pourquoi-la-marge-peut-elle-apparaitre-a-100-dans-une-commande-et-comment-la-modifier.md | 138 | comportement du champ marge (calculé, non modifiable directement) sur une commande | chantier-intervention | tarification | oui | non | oui | oui | non | faq_depannage |
| 214 | faq-foires-aux-questions/pourquoi-la-marge-peut-sembler-incorrecte-dans-un-devis.md | 186 | recommandations pour un calcul de marge réaliste sur devis (éviter prix à 0€) | devis | tarification | oui | non | oui | non | non | faq_depannage |
| 215 | faq-foires-aux-questions/pourquoi-le-bouton-lien-devis-ou-facture-en-haut-a-gauche-empeche-t-il-l-envoi-du-pdf-avec-le-devis-ou-la-facture.md | 163 | comportement du bouton « lien devis/facture » (envoi par lien vs pièce jointe PDF) | devis | communication, documents | oui | non | oui | non | non | faq_depannage |
| 216 | faq-foires-aux-questions/pourquoi-le-bouton-pour-creer-un-nouvel-avancement-a-t-il-disparu.md | 71 | dépannage de la disparition du bouton de création d'un nouvel avancement | chantier-intervention | — | non | non | oui | oui | non | faq_depannage |
| 217 | faq-foires-aux-questions/pourquoi-le-bouton-pour-modifier-le-statut-d-une-commande-est-il-desactive.md | 120 | désactivation du bouton de statut de commande liée à un avenant | achat | — | non | non | oui | oui | non | faq_depannage |
| 218 | faq-foires-aux-questions/pourquoi-le-prix-dans-le-detail-d-ouvrages-peut-il-differer-du-prix-dans-le-devis.md | 184 | écarts de prix entre détail d'ouvrage et devis (méthodes d'arrondi différentes) | devis | catalogue, tarification | non | non | oui | non | non | definitionnel |
| 219 | faq-foires-aux-questions/pourquoi-le-retour-au-statut-precedent-a-t-il-ete-retire-sur-un-devis-accepte-dans-vertuoza.md | 171 | suppression de la fonction « retour au statut précédent » sur devis accepté (alternative : suppression du chantier) | devis | — | oui | oui | oui | oui | oui | definitionnel |
| 220 | faq-foires-aux-questions/pourquoi-le-total-brut-ht-et-le-total-net-ht-sont-ils-identiques-dans-mon-devis.md | 115 | définition Total Brut HT vs Total Net HT (identiques en l'absence de remise) | devis | tarification | non | non | oui | non | non | definitionnel |
| 221 | faq-foires-aux-questions/pourquoi-le-total-de-mon-devis-n-est-pas-parfaitement-rond-apres-une-remise-globale.md | 126 | écarts d'arrondi après remise globale (contournement pour un total rond) | devis | tarification | oui | non | oui | non | oui | faq_depannage |
| 222 | faq-foires-aux-questions/pourquoi-les-avenants-sont-ils-envoyes-a-l-adresse-du-client-et-non-a-l-adresse-de-facturation-et-est-il-possible-de-changer-cela.md | 88 | adresse d'envoi fixe des avenants (adresse client, non modifiable) | chantier-intervention | — | non | non | oui | oui | non | faq_depannage |
| 223 | faq-foires-aux-questions/pourquoi-les-montants-affiches-dans-les-statistiques-different-de-ceux-visibles-en-bas-de-page-des-devis.md | 135 | écart entre statistiques et liste des devis (critères de date différents) | devis | reporting | non | non | oui | non | non | faq_depannage |
| 224 | faq-foires-aux-questions/pourquoi-les-mots-changent-ils-automatiquement-dans-notre-devis-facture.md | 68 | dépannage de modification automatique de texte (correcteur/traducteur navigateur) | indetermine | — | non | non | non | non | oui | faq_depannage |
| 225 | faq-foires-aux-questions/pourquoi-les-rapports-d-interventions-ne-sont-ils-pas-automatiquement-lies-aux-factures-globales.md | 135 | absence de liaison automatique des rapports d'intervention aux factures groupées | facturation | documents | oui | non | oui | oui | non | faq_depannage |

| 226 | faq-foires-aux-questions/pourquoi-lorsque-je-clique-sur-ma-notification-suis-je-redirige-vers-la-page-d-accueil-tableau-de-bord-au-lieu-de-la-module-indiquee.md | 130 | redirection par défaut depuis une notification si accès module restreint | indetermine | notifications, roles | non | non | oui | oui | non | faq_depannage |
| 227 | faq-foires-aux-questions/pourquoi-ma-commande-n-apparait-elle-pas-lors-de-l-ajout-d-une-facture-fournisseur-sous-traitant.md | 72 | visibilité conditionnelle d'une commande sous-traitant lors de la liaison à une facture fournisseur | achat | — | non | non | oui | oui | non | faq_depannage |
| 228 | faq-foires-aux-questions/pourquoi-ma-facture-vertuoza-est-elle-envoyees-un-mois-a-l-avance.md | 65 | politique de facturation anticipée de l'abonnement Vertuoza | facturation | — | non | non | oui | non | non | definitionnel |
| 229 | faq-foires-aux-questions/pourquoi-ma-marge-beneficiaire-est-elle-negative-dans-un-devis.md | 108 | dépannage de marge négative sur devis (erreur de saisie de prix) | devis | tarification, documents | oui | non | non | non | oui | faq_depannage |
| 230 | faq-foires-aux-questions/pourquoi-ma-marge-de-x-ne-s-applique-t-elle-pas-correctement-dans-le-tableau-des-factures.md | 126 | dépannage d'application incorrecte de la marge sur les lignes de facture | facturation | tarification | oui | non | oui | non | oui | faq_depannage |
| 231 | faq-foires-aux-questions/pourquoi-ma-note-de-credit-reste-t-elle-en-statut-non-payee-et-que-faire.md | 190 | comportement de statut d'une note de crédit et solutions de régularisation | facturation | paiement, personnalisation | oui | non | oui | non | oui | faq_depannage |
| 232 | faq-foires-aux-questions/pourquoi-ma-recherche-de-stock-avec-la-reference-complete-ne-donne-aucun-resultat-alors-que-l-article-existe-bien.md | 144 | comportement de recherche stock (référence exacte vs partielle) en cas d'entrées similaires | achat | gestion_stock, recherche | non | non | oui | non | oui | faq_depannage |
| 233 | faq-foires-aux-questions/pourquoi-ma-session-a-t-elle-ete-interrompue.md | 54 | interruption de session liée à une facture ouverte sur le compte | indetermine | securite_compte, paiement | non | non | oui | oui | oui | faq_depannage |
| 234 | faq-foires-aux-questions/pourquoi-mes-70-d-avancement-ne-sont-ils-pas-pris-en-compte.md | 136 | logique cumulative des pourcentages d'avancement sur un poste | chantier-intervention | — | non | non | oui | oui | non | faq_depannage |
| 235 | faq-foires-aux-questions/pourquoi-mes-lignes-sont-elles-definies-comme-options-par-defaut-lorsque-je-les-importe-depuis-excel.md | 89 | comportement d'import Excel (ligne sans prix total = option) | devis | documents | oui | non | oui | non | non | faq_depannage |
| 236 | faq-foires-aux-questions/pourquoi-mes-modifications-ne-sont-elles-pas-appliquees-au-niveau-de-la-modification-d-ouvrage.md | 142 | dépannage de blocage de modification d'ouvrage (incohérence fournisseur composant) | devis | catalogue | oui | non | oui | oui | oui | faq_depannage |
| 237 | faq-foires-aux-questions/pourquoi-mes-pointages-clotures-ne-sont-ils-pas-encore-pris-en-compte-dans-la-rentabilite-du-chantier.md | 96 | dépannage de rentabilité chantier faussée (coût horaire ouvrier non défini) | chantier-intervention | planning | oui | non | oui | non | oui | faq_depannage |
| 238 | faq-foires-aux-questions/pourquoi-mon-avenant-n-a-t-il-pas-ete-integre-dans-l-etat-d-avancement-que-j-ai-cree.md | 86 | comportement de non-intégration rétroactive d'un avenant validé après création d'un état d'avancement | chantier-intervention | — | non | non | oui | oui | non | faq_depannage |
| 239 | faq-foires-aux-questions/pourquoi-mon-chantier-affiche-t-il-encore-un-reste-a-produire-alors-qu-il-est-facture-a-100.md | 147 | distinction entre « reste à produire » (avancement) et « reste à facturer » (facturation) | chantier-intervention | — | non | non | oui | non | non | definitionnel |
| 240 | faq-foires-aux-questions/pourquoi-mon-client-n-apparait-elle-pas-dans-le-menu-deroulant-du-champ-client-lors-de-la-creation-ou-de-l-edition-de-ma-facture-devis.md | 96 | visibilité conditionnelle d'un contact dans le champ client (profil requis) | indetermine | crm | oui | non | oui | non | non | faq_depannage |

| 241 | faq-foires-aux-questions/pourquoi-mon-compte-vertuoza-est-il-lent.md | 465 | dépannage de lenteur (navigateur recommandé, cache, extensions) | indetermine | — | oui | non | non | oui | oui | faq_depannage |
| 242 | faq-foires-aux-questions/pourquoi-mon-export-excel-d-ouvrages-est-il-vide.md | 97 | export Excel vide si seulement des ouvrages composés (limite export ouvrages simples) | devis | catalogue, documents | non | non | oui | oui | non | faq_depannage |
| 243 | faq-foires-aux-questions/pourquoi-mon-inventaire-ne-prend-il-en-compte-que-des-chiffres-entiers.md | 129 | limite de gestion des stocks en nombres entiers uniquement | achat | gestion_stock | non | non | oui | oui | non | definitionnel |
| 244 | faq-foires-aux-questions/pourquoi-mon-modele-de-devis-est-il-marque-comme-obsolete-et-que-faire.md | 224 | obsolescence des anciens modèles de devis (migration vers nouveau module) | devis | personnalisation, documents | oui | oui | oui | oui | non | faq_depannage |
| 245 | faq-foires-aux-questions/pourquoi-mon-qr-code-ne-se-genere-t-il-pas-apres-avoir-soumis-ma-proposition-de-facture.md | 147 | dépannage de génération de QR code (facture non comptabilisée) | facturation | — | oui | non | oui | non | oui | faq_depannage |
| 246 | faq-foires-aux-questions/pourquoi-n-y-a-t-il-pas-de-tva-sur-mes-bons-de-commande-lorsque-je-fais-appel-a-un-sous-traitant-dans-le-secteur-du-batiment.md | 150 | autoliquidation de la TVA sur les commandes sous-traitants BTP (absence de TVA) | achat | conformite_reglementaire | non | non | oui | non | non | definitionnel |
| 247 | faq-foires-aux-questions/pourquoi-ne-puis-je-pas-ajouter-un-utilisateur-a-une-planification-passee-si-son-pointage-est-deja-cloture.md | 123 | verrouillage rétroactif de planification après clôture du pointage | chantier-intervention | planning | non | non | oui | oui | non | faq_depannage |
| 248 | faq-foires-aux-questions/pourquoi-ne-puis-je-pas-creer-un-identifiant-avec-une-adresse-e-mail-qui-existe-deja.md | 76 | unicité obligatoire de l'identifiant/email de compte gestion | indetermine | securite_compte, roles | non | non | oui | oui | non | faq_depannage |
| 249 | faq-foires-aux-questions/pourquoi-ne-puis-je-pas-creer-une-note-de-credit-si-la-facture-est-liee-a-un-crediteur.md | 76 | nécessité d'un responsable assigné pour créer une note de crédit liée à un créditeur | facturation | paiement, roles | non | non | oui | oui | non | faq_depannage |
| 250 | faq-foires-aux-questions/pourquoi-ne-puis-je-pas-exporter-mes-factures-avec-l-option-tout-exporter.md | 108 | comportement de l'option « Tout exporter » (réexport uniquement, sélection requise) | facturation | documents | non | non | oui | oui | non | faq_depannage |
| 251 | faq-foires-aux-questions/pourquoi-ne-puis-je-pas-importer-mon-inventaire.md | 167 | dépannage d'import d'inventaire (identifiants fournitures manquants dans CSV) | achat | gestion_stock, documents | oui | non | oui | non | oui | faq_depannage |
| 252 | faq-foires-aux-questions/pourquoi-ne-puis-je-pas-ouvrir-mon-devis-depuis-le-lien-dans-l-email-de-reception.md | 238 | dépannage d'accès au lien de devis (réseau, pare-feu, proxy client) | devis | communication, integrations | oui | non | non | non | oui | faq_depannage |
| 253 | faq-foires-aux-questions/pourquoi-ne-puis-je-pas-supprimer-un-taux-de-tva-dans-mes-parametres.md | 82 | suppression d'un taux de TVA conditionnée à son non-usage dans les documents | indetermine | conformite_reglementaire | non | non | oui | oui | non | faq_depannage |
| 254 | faq-foires-aux-questions/pourquoi-ne-puis-je-plus-copier-coller-des-liens-qui-deviennent-cliquables-dans-mes-bulles-de-commentaires.md | 157 | dépannage de comportement des liens cliquables dans les commentaires (changement tiers Microsoft) | indetermine | communication | non | non | non | oui | oui | faq_depannage |
| 255 | faq-foires-aux-questions/pourquoi-seules-certaines-informations-comme-la-tva-apparaissent-dans-mon-pdf-de-devis.md | 115 | dépannage d'affichage PDF incomplet lié à une modification manuelle du modèle | devis | personnalisation, documents | non | non | oui | non | non | faq_depannage |

| 256 | faq-foires-aux-questions/pourquoi-suis-je-redirige-vers-la-page-d-accueil-apres-avoir-clique-sur-gestion-de-chantier.md | 118 | redirection par défaut faute de droits d'accès au module Gestion de chantier | chantier-intervention | roles | non | non | oui | oui | non | faq_depannage |
| 257 | faq-foires-aux-questions/pourquoi-toutes-les-lignes-ne-sont-elles-pas-reprises-dans-une-facture-groupee-d-intervention.md | 126 | exclusion des lignes à montant nul dans une facture groupée d'intervention | facturation | tarification | non | non | oui | oui | oui | faq_depannage |
| 258 | faq-foires-aux-questions/pourquoi-un-montant-reste-t-il-affiche-dans-les-indicateurs-de-rentabilite-meme-apres-avoir-encode-une-facture-fournisseur.md | 139 | comportement d'affichage des indicateurs de rentabilité (facture brouillon ou partielle) | achat | paiement | non | non | oui | non | non | faq_depannage |
| 259 | faq-foires-aux-questions/pourquoi-une-facture-apparait-elle-en-statut-partiellement-paye-alors-que-le-client-a-regle-le-montant-et-recu-une-note-de-credit.md | 158 | dépannage de statut de facture bloqué « partiellement payé » (validation manuelle requise) | facturation | paiement | oui | non | oui | non | oui | faq_depannage |
| 260 | faq-foires-aux-questions/pourquoi-une-opportunite-ne-se-cree-t-elle-pas-apres-l-envoi-d-un-email.md | 132 | dépannage de non-création d'opportunité par email (email prospect manquant) | demande | crm, automatisation | oui | non | oui | non | non | faq_depannage |
| 261 | faq-foires-aux-questions/pourquoi-y-a-t-il-des-differences-dans-les-montants-factures-par-rapport-aux-devis-initiaux.md | 76 | écarts entre devis et facturation liés au mode d'application des remises | facturation | tarification | non | non | oui | non | non | faq_depannage |
| 262 | faq-foires-aux-questions/pourquoi-y-a-t-il-une-difference-entre-le-montant-du-chiffre-d-affaires-affiche-et-le-total-des-ventes-facturees.md | 167 | distinction chiffre d'affaires (devis+avenants) vs total des ventes facturées | facturation | reporting | non | non | oui | non | non | definitionnel |
| 263 | faq-foires-aux-questions/puis-je-modifier-l-adresse-d-un-chantier-apres-l-edition-d-une-facture.md | 72 | impossibilité de modifier l'adresse de chantier après édition de facture (contournement) | facturation | — | oui | non | oui | oui | oui | faq_depannage |
| 264 | faq-foires-aux-questions/puis-je-modifier-la-date-d-une-facture-emise-par-erreur.md | 143 | modification de la date d'une facture (règles de chronologie légale) | facturation | conformite_reglementaire | oui | non | oui | oui | oui | faq_depannage |
| 265 | faq-foires-aux-questions/qu-est-ce-que-l-analytique-dans-la-synchronisation-comptable.md | 106 | fonctionnalité optionnelle d'analytique comptable liée à la synchronisation | indetermine | integrations | non | non | non | non | non | definitionnel |
| 266 | faq-foires-aux-questions/quand-un-ouvrage-est-mis-a-jour-dans-la-biblio-de-prix-les-prix-sont-ils-automatiquement-mis-a-jour-dans-les-devis-existants.md | 121 | non-répercussion automatique des mises à jour de bibliothèque sur les devis existants | devis | catalogue, tarification | oui | non | oui | oui | non | faq_depannage |
| 267 | faq-foires-aux-questions/que-devient-le-connecteur-avec-winbizz.md | 64 | arrêt du développement du connecteur comptable Winbizz | indetermine | integrations | non | non | non | oui | non | definitionnel |
| 268 | faq-foires-aux-questions/que-faire-si-j-ai-emis-une-note-de-credit-pour-corriger-la-tva-sur-une-facture-d-acompte-dans-un-chantier.md | 205 | procédure de finalisation d'un chantier après correction de TVA par note de crédit | facturation | paiement | oui | oui | oui | non | oui | procedure |
| 269 | faq-foires-aux-questions/que-faire-si-je-dois-modifier-un-devis-deja-accepte.md | 144 | méthodes de modification d'un devis accepté (avenant ou suppression du chantier vide) | devis | — | oui | oui | oui | oui | oui | faq_depannage |
| 270 | faq-foires-aux-questions/que-faire-si-le-fournisseur-n-est-pas-encore-enregistre-sur-peppol.md | 71 | format du numéro PEPPOL et vérification d'enregistrement fournisseur | achat | integrations, conformite_reglementaire | oui | non | oui | non | non | reference_configuration |

| 271 | faq-foires-aux-questions/que-faire-si-le-fournisseur-ou-client-n-est-pas-encore-enregistre-sur-peppol.md | 82 | procédure si le fournisseur/client n'est pas enregistré sur PEPPOL | indetermine | integrations, conformite_reglementaire | oui | non | oui | oui | oui | faq_depannage |
| 272 | faq-foires-aux-questions/que-faire-si-mon-texte-dans-une-ligne-de-mon-devis-ne-se-sauvegarde-pas.md | 199 | dépannage de sauvegarde de texte (caractères spéciaux non supportés) | devis | — | oui | non | oui | oui | oui | faq_depannage |
| 273 | faq-foires-aux-questions/que-faire-si-une-absence-pour-maladie-est-declaree-apres-la-generation-des-pointages.md | 152 | mise à jour manuelle requise des pointages après déclaration tardive d'absence maladie | chantier-intervention | planning | oui | non | oui | oui | oui | faq_depannage |
| 274 | faq-foires-aux-questions/que-puis-je-faire-si-un-taux-de-tva-incorrect-apparait-dans-les-sous-totaux-de-mon-devis.md | 266 | dépannage de taux de TVA résiduel après désactivation de l'option TVA à la ligne | devis | conformite_reglementaire, personnalisation | oui | non | oui | non | oui | faq_depannage |
| 275 | faq-foires-aux-questions/que-se-passe-t-il-lorsque-je-selectionne-chantier-inconnu-pour-un-article-dans-un-bon-de-retour.md | 78 | comportement de l'option « chantier inconnu » sur un bon de retour (ajout direct au stock) | achat | gestion_stock | non | non | oui | non | non | definitionnel |
| 276 | faq-foires-aux-questions/que-se-passe-t-il-si-j-envoie-mes-emails-depuis-ma-propre-adresse-gmail-via-vertuoza.md | 182 | comportement de l'envoi d'emails via l'intégration Gmail (traçabilité modifiée) | indetermine | integrations, communication | non | non | oui | oui | non | definitionnel |
| 277 | faq-foires-aux-questions/que-se-passe-t-il-si-un-client-n-est-pas-connecte-au-reseau-peppol.md | 112 | comportement de l'envoi PEPPOL si le client n'est pas connecté au réseau | facturation | integrations | non | non | oui | oui | non | definitionnel |
| 278 | faq-foires-aux-questions/que-signifie-ajustement-prorata-dans-le-cadre-de-la-facturation.md | 54 | définition de l'ajustement prorata (recalcul des prix unitaires devis→facture) | facturation | tarification | non | non | oui | non | non | definitionnel |
| 279 | faq-foires-aux-questions/que-signifie-l-erreur-bad-request-your-browser-sent-a-request-that-this-server-could-not-understand-et-comment-la-resoudre.md | 171 | dépannage de l'erreur navigateur « Bad Request » | indetermine | — | oui | non | non | non | oui | faq_depannage |
| 280 | faq-foires-aux-questions/quel-montant-est-pris-en-compte-si-ma-facture-fournisseur-est-superieure-au-bon-de-commande.md | 179 | logique de substitution du montant de bon de commande par le montant de facture supérieur | achat | paiement | non | non | oui | non | non | definitionnel |
| 281 | faq-foires-aux-questions/quel-produit-batiprix-dois-je-acheter-pour-mon-entreprise.md | 51 | recommandation du produit Batiprix compatible (BATIPRIX DATA) | indetermine | integrations, catalogue | non | non | non | non | non | reference_configuration |
| 282 | faq-foires-aux-questions/quelle-est-la-difference-entre-la-marge-affichee-dans-l-historique-des-chantiers-et-le-benefice-indique-dans-le-tableau-de-bord-du-chantier-dans-vertuoza.md | 181 | distinction entre marge brute (historique) et bénéfice complet (tableau de bord) | chantier-intervention | tarification, reporting | non | non | oui | non | non | definitionnel |
| 283 | faq-foires-aux-questions/quelle-est-la-difference-entre-le-reste-a-produire-et-le-reste-a-facturer-dans-vertuoza.md | 142 | distinction reste à produire / reste à facturer et procédure de résolution | chantier-intervention | — | oui | non | oui | non | non | definitionnel |
| 284 | faq-foires-aux-questions/quelle-est-la-difference-entre-le-reste-a-produire-et-le-reste-a-facturer.md | 113 | distinction reste à produire / reste à facturer (définition courte) | chantier-intervention | — | non | non | oui | non | non | definitionnel |
| 285 | faq-foires-aux-questions/quelle-est-la-difference-entre-une-commande-de-chantier-et-une-commande-d-approvisionnement-de-stock.md | 137 | distinction entre commande de chantier (livraison directe) et commande de réapprovisionnement de stock | achat | gestion_stock | non | non | oui | non | non | definitionnel |

| 286 | faq-foires-aux-questions/quelle-est-la-difference-entre-une-facture-d-acompte-etablie-en-htva-et-une-facture-d-acompte-avec-tva-comprise.md | 90 | base de calcul HTVA d'une facture d'acompte (TVA appliquée à la facturation finale) | facturation | tarification, conformite_reglementaire | non | non | oui | non | non | definitionnel |
| 287 | faq-foires-aux-questions/quelle-est-la-difference-entre-une-facture-d-avancement-et-une-facture-simple.md | 159 | distinction facture simple (libre) vs facture d'avancement (basée sur état d'avancement) | facturation | — | non | non | oui | non | oui | definitionnel |
| 288 | faq-foires-aux-questions/quelle-est-la-difference-entre-une-reference-et-une-description.md | 105 | distinction référence (interne) vs description (visible client) sur un composant | devis | catalogue | non | non | non | non | non | definitionnel |
| 289 | faq-foires-aux-questions/quelles-erreurs-frequentes-peuvent-survenir-avec-peppol.md | 80 | erreurs fréquentes de la facturation électronique PEPPOL (checklist) | facturation | integrations, conformite_reglementaire | non | non | oui | oui | oui | faq_depannage |
| 290 | faq-foires-aux-questions/quelles-sont-les-conditions-pour-qu-une-synchronisation-entre-vertuoza-et-codabox-ponto-soit-effectuee.md | 207 | conditions techniques de synchronisation bancaire Vertuoza/Codabox/Ponto | facturation | integrations, paiement | non | non | oui | non | non | reference_configuration |
| 291 | faq-foires-aux-questions/quelles-sont-les-regles-de-modification-des-composants-en-masse.md | 163 | règles de comportement lors de la modification de champs de composants (référence/description/fournisseur) | devis | catalogue | non | non | oui | non | non | reference_configuration |
| 292 | faq-foires-aux-questions/quelles-sont-toutes-les-raisons-possibles-pour-lesquelles-je-n-arrive-pas-a-soumettre-mon-devis.md | 147 | checklist de dépannage de soumission de devis bloquée | devis | — | oui | non | oui | oui | oui | faq_depannage |
| 293 | faq-foires-aux-questions/quels-sont-les-codes-couleur-utilises-dans-le-planning-d-intervention-et-que-signifient-ils.md | 84 | légende des codes couleur du planning d'intervention | chantier-intervention | planning, personnalisation | non | non | oui | non | non | reference_configuration |
| 294 | faq-foires-aux-questions/quels-sont-les-statuts-de-la-facturation-electronique.md | 107 | liste des statuts du cycle d'envoi de la facturation électronique PEPPOL | facturation | integrations | non | non | oui | non | non | reference_configuration |
| 295 | faq-foires-aux-questions/quels-types-de-lignes-peut-on-ajouter-dans-un-devis.md | 50 | types de lignes disponibles dans un devis (titre, texte, poste libre, ouvrages, composants) | devis | catalogue | non | non | non | non | non | definitionnel |
| 296 | faq-foires-aux-questions/synchronisation-comptable-comment-seront-classees-les-factures-en-fonction-du-taux-de-tva-et-des-activites.md | 133 | classification comptable des factures par taux de TVA et activité | facturation | integrations, conformite_reglementaire | non | non | oui | non | non | definitionnel |
| 297 | faq-foires-aux-questions/un-ouvrier-peut-il-etre-pointe-sans-compte-chantier.md | 124 | pointage d'un ouvrier possible indépendamment de l'existence d'un compte chantier | chantier-intervention | planning, roles | oui | non | oui | non | non | reference_configuration |
| 298 | faq-foires-aux-questions/un-sous-traitant-recoit-il-automatiquement-un-email-a-sa-creation.md | 48 | envoi automatique (désactivable) d'un email à la création d'une fiche sous-traitant | indetermine | communication, crm | non | non | oui | non | non | definitionnel |
| 299 | faq-foires-aux-questions/vertuoza-propose-t-il-un-logiciel-de-tresorerie-integre.md | 153 | absence de module trésorerie natif (intégrations tierces pour paiements/comptabilité/PEPPOL) | facturation | integrations, paiement | non | non | oui | oui | non | definitionnel |
| 300 | faq-foires-aux-questions/wat-te-doen-als-mijn-voorraad-negatieve-hoeveelheden-of-ontbrekende-producten-aangeeft.md | 157 | correction des écarts de stock négatifs (bon de sortie manuel lié au chantier) | achat | gestion_stock | oui | non | non | non | oui | faq_depannage |

| 301 | fiches-techniques/dossiers-de-fiche-techniques.md | 164 | création de dossiers de fiches techniques liés à un chantier | chantier-intervention | documents | oui | non | non | non | non | procedure |
| 302 | fiches-techniques/fiches-techniques.md | 389 | gestion des fiches techniques (groupes, import, liaison chantier) | indetermine | documents, catalogue | oui | oui | non | non | non | procedure |
| 303 | finance/annee-fiscale.md | 68 | configuration de l'année fiscale (impact sur numérotation des factures) | facturation | conformite_reglementaire | oui | oui | oui | non | non | reference_configuration |
| 304 | finance/creation-d-une-nouvelle-facture-fournisseur.md | 405 | création et workflow de validation d'une facture fournisseur | achat | paiement, documents | oui | oui | oui | oui | oui | procedure |
| 305 | finance/envoi-de-la-note-de-credit-via-un-lien.md | 261 | envoi d'une note de crédit via lien consultable en ligne | facturation | communication, notifications | oui | non | oui | oui | non | procedure |
| 306 | finance/export-des-factures.md | 214 | export groupé de factures (PDF/UBL) sur une période | facturation | documents | oui | non | non | non | non | procedure |
| 307 | finance/facture-suisse-activer-la-qr-facture.md | 446 | activation et fonctionnement de la QR-facture suisse (obligation légale) | facturation | conformite_reglementaire, paiement | oui | oui | oui | oui | oui | reference_configuration |
| 308 | finance/la-liste-des-factures-fournisseurs.md | 182 | présentation de l'écran de gestion des factures fournisseurs | achat | recherche, paiement | non | non | non | non | non | reference_configuration |
| 309 | finance/notes-de-credits.md | 285 | création d'une note de crédit (depuis le menu ou depuis une facture existante) | facturation | paiement | oui | non | oui | non | non | procedure |
| 310 | finance/paiement-de-la-facture-via-qr-code.md | 541 | paiement de facture via QR code (activation, expérience client) | facturation | paiement, communication | oui | oui | oui | oui | non | procedure |
| 311 | finance/preferences.md | 81 | configuration des préférences de facturation (type, QR code, numérotation, suppression) | facturation | personnalisation | oui | non | non | non | non | reference_configuration |
| 312 | finance/table-d-index.md | 257 | gestion d'index de révision de prix pour factures récurrentes | facturation | tarification, documents | oui | non | non | non | non | procedure |
| 313 | finance/types-de-frais.md | 112 | configuration des types de frais pour factures fournisseurs « autres » | achat | — | oui | non | non | non | non | reference_configuration |
| 314 | finance/utiliser-l-ia-pour-importer-ses-factures-fournisseurs-beta.md | 183 | import de factures fournisseurs par IA (email, web, mobile, reconnaissance de champs) | achat | automatisation, mobile | oui | non | non | non | non | procedure |
| 315 | gestion-de-chantier/archiver-le-chantier.md | 187 | archivage et réactivation d'un chantier | chantier-intervention | — | oui | non | non | non | non | procedure |

| 316 | gestion-de-chantier/avancement.md | 271 | création, validation et facturation d'un état d'avancement de chantier | chantier-intervention | tarification, paiement | oui | oui | oui | non | non | procedure |
| 317 | gestion-de-chantier/avenant.md | 335 | création et gestion d'un avenant (modification du contrat initial) | chantier-intervention | tarification, catalogue | oui | oui | non | non | oui | procedure |
| 318 | gestion-de-chantier/commandes-de-materiaux.md | 497 | création de demandes de prix et commandes de matériaux (fournisseurs) | achat | gestion_stock, roles | oui | oui | non | non | non | procedure |
| 319 | gestion-de-chantier/commandes-sous-traitants.md | 447 | création de demandes de prix et commandes auprès de sous-traitants | achat | roles | oui | oui | non | non | non | procedure |
| 320 | gestion-de-chantier/factures-d-acomptes.md | 372 | création d'une facture d'acompte depuis la gestion de chantier | facturation | tarification, paiement | oui | non | non | non | oui | procedure |
| 321 | gestion-de-chantier/factures-finales.md | 351 | création d'une facture finale de chantier | facturation | tarification, paiement | oui | non | non | non | oui | procedure |
| 322 | gestion-de-chantier/formules-de-revisions.md | 211 | application de coefficients de révision de prix sur des lignes de devis | devis | tarification | oui | non | non | non | non | procedure |
| 323 | gestion-de-chantier/la-vue-gantt.md | 440 | présentation du planning Gantt des chantiers (vue macro, planification stratégique) | chantier-intervention | planning, reporting | non | non | non | oui | non | definitionnel |
| 324 | gestion-de-chantier/pourquoi-deduire-les-acomptes-lors-des-etats-d-avancements.md | 641 | logique et procédure de déduction des acomptes dans les états d'avancement | facturation | tarification, paiement | oui | non | oui | non | non | definitionnel |
| 325 | gestion-de-chantier/rentabilite-periodique.md | 313 | calcul de la rentabilité d'un chantier sur une période définie (dépenses/ventes pondérées) | chantier-intervention | reporting, automatisation | oui | non | non | non | non | procedure |
| 326 | gestion-de-chantier/signature-electronique-de-l-avenant.md | 466 | signature électronique en ligne d'un avenant | chantier-intervention | integrations, notifications | oui | oui | oui | non | non | procedure |
| 327 | gestion-de-chantier/suivi-de-chantier-chef-d-equipe.md | 210 | suivi de chantier par le chef d'équipe (remarques, photos) depuis mobile | chantier-intervention | mobile, photos, communication | oui | non | oui | non | non | procedure |
| 328 | gestion-de-chantier/taches-de-chantier.md | 263 | configuration des tâches de chantier (checklist qualité, planification quotidienne) | chantier-intervention | planning | oui | oui | non | non | non | reference_configuration |
| 329 | gestion-de-chantier/taches.md | 307 | création et suivi des tâches administratives liées à un chantier | chantier-intervention | — | oui | non | oui | non | non | procedure |
| 330 | gestion-de-chantier/types-de-chantier.md | 174 | configuration des types de chantier (classification personnalisée) | chantier-intervention | — | oui | non | non | non | non | reference_configuration |

| 331 | gestion-des-interventions/competences.md | 155 | gestion des compétences des responsables d'intervention (aide à l'assignation) | chantier-intervention | planning | oui | non | non | non | non | procedure |
| 332 | gestion-des-interventions/creation-d-une-installation.md | 376 | création et gestion d'une fiche d'installation (client, TVA, photos, fichiers) | chantier-intervention | photos, documents, conformite_reglementaire | oui | non | oui | non | non | procedure |
| 333 | gestion-des-interventions/frais-generaux.md | 295 | configuration des frais généraux facturables associés aux interventions | facturation | catalogue, automatisation | oui | oui | oui | non | non | procedure |
| 334 | gestion-des-interventions/planification-et-gestion-des-interventions.md | 421 | planification, statuts et gestion des interventions dans le planning | chantier-intervention | planning, communication, gestion_stock | oui | oui | oui | oui | non | procedure |
| 335 | gestion-des-interventions/preferences.md | 282 | configuration des préférences d'interventions et d'affichage du planning | chantier-intervention | planning, conformite_reglementaire, notifications | oui | non | oui | oui | non | reference_configuration |
| 336 | gestion-des-interventions/responsable-d-intervention.md | 253 | création et configuration des responsables d'intervention (compétences, autorisations) | chantier-intervention | roles, permissions, planning | oui | oui | oui | non | oui | procedure |
| 337 | gestion-des-interventions/types-d-installation.md | 136 | configuration des types d'installation (classification) | chantier-intervention | catalogue | oui | non | non | non | non | procedure |
| 338 | gestion-des-interventions/types-d-intervention.md | 312 | configuration des types d'intervention (durée, forfait/régie, frais) | chantier-intervention | catalogue, planning | oui | oui | oui | non | non | procedure |
| 339 | notifications/les-notifications.md | 231 | système de notifications des actions gestionnaires (rapports, factures, signatures, paiements) | indetermine | notifications, communication | oui | oui | oui | non | non | definitionnel |
| 340 | parametres/adresses-de-livraison-de-la-societe.md | 97 | configuration des adresses de livraison distinctes pour les commandes de matériaux | achat | gestion_stock | oui | non | non | non | non | procedure |
| 341 | parametres/batiprix.md | 375 | intégration Batiprix (connexion, recherche et import d'ouvrages dans les devis) | devis | integrations, catalogue, paiement | oui | oui | oui | oui | oui | procedure |
| 342 | parametres/combien-d-utilisateur-puis-je-encore-creer.md | 55 | consultation du nombre de comptes utilisateurs restants disponibles | indetermine | — | oui | non | non | oui | non | faq_depannage |
| 343 | parametres/comment-activer-l-option-enveloppe-a-fenetre.md | 116 | activation de l'option enveloppe à fenêtre sur un modèle de devis 2 colonnes | devis | personnalisation | oui | non | non | non | non | procedure |
| 344 | parametres/comment-activer-la-facturation-electronique.md | 301 | activation de la facturation électronique (Peppol, vérification d'identité KYC) | facturation | integrations, conformite_reglementaire, validation | oui | oui | oui | oui | oui | procedure |
| 345 | parametres/comment-creer-un-modele-de-devis-personnalise.md | 221 | création d'un modèle de devis personnalisé (mise en page, zones, image de fond) | devis | personnalisation, catalogue, documents | oui | non | non | non | non | procedure |

| 346 | parametres/comment-desactiver-la-facturation-electronique.md | 49 | désactivation (déconnexion) de la facturation électronique | facturation | integrations | oui | non | oui | oui | non | procedure |
| 347 | parametres/comment-fonctionne-le-mapping-des-clients-et-fournisseurs-lors-de-la-synchronisation.md | 314 | logique de mapping clients/fournisseurs lors de la synchronisation comptable (cascade ID puis nom) | facturation | integrations, automatisation | non | non | oui | non | oui | faq_depannage |
| 348 | parametres/comment-identifier-les-factures-en-erreurs.md | 216 | identification et résolution des factures en erreur de synchronisation comptable | facturation | integrations, support_editeur | oui | oui | non | non | oui | faq_depannage |
| 349 | parametres/comment-modifier-le-mot-de-passe-d-un-utilisateur.md | 126 | modification du mot de passe d'un utilisateur (compte gestion/chantier) | indetermine | securite_compte, roles | oui | non | non | non | oui | procedure |
| 350 | parametres/comment-supprimer-un-utilisateur.md | 63 | suppression d'un utilisateur (compte gestion/chantier), historique conservé | indetermine | roles, securite_compte | oui | non | oui | non | non | procedure |
| 351 | parametres/comment-utiliser-des-prefixes-dynamiques-dans-vos-modeles.md | 232 | préfixes dynamiques conditionnels dans les modèles de documents | devis | personnalisation, automatisation | oui | non | oui | non | non | procedure |
| 352 | parametres/comment-utiliser-les-variables-dans-vos-modeles.md | 282 | insertion de variables dynamiques dans les modèles de documents (société, client, devis, chantier) | devis | personnalisation, automatisation, catalogue | oui | non | non | non | non | procedure |
| 353 | parametres/conditions-de-bas-de-page-ajoutez-des-mentions-automatiques-a-vos-documents.md | 232 | mentions automatiques de bas de page sur les documents (fonctionnalité dépréciée pour les devis) | devis | documents, automatisation, personnalisation | oui | non | oui | oui | non | procedure |
| 354 | parametres/conditions-de-bas-de-page-des-documents-standards.md | 174 | conditions de bas de page des documents standards (devis, commandes) | devis | documents, catalogue | oui | non | non | non | non | procedure |
| 355 | parametres/conditions-de-paiements.md | 128 | configuration des conditions de paiement (délai, type) | facturation | paiement, catalogue | oui | non | non | non | non | procedure |
| 356 | parametres/conditions-generales-de-ventes-cgv.md | 103 | import des conditions générales de vente (CGV) en pièce jointe automatique aux devis/factures | devis | documents, conformite_reglementaire, automatisation | oui | non | non | non | non | procedure |
| 357 | parametres/configuration-des-nouvelles-pages-listes.md | 490 | nouvelles fonctionnalités des pages de listes (colonnes, tri, filtres, persistance) | indetermine | personnalisation, recherche | oui | non | non | non | non | faq_depannage |
| 358 | parametres/configurer-votre-adresse-email-avec-smtp.md | 585 | configuration de la messagerie professionnelle via SMTP/IMAP (par fournisseur) | indetermine | integrations, communication, securite_compte | oui | oui | oui | oui | non | reference_configuration |
| 359 | parametres/couleurs-des-documents-standards.md | 130 | configuration des couleurs des documents PDF standards | devis | personnalisation | oui | non | non | non | non | procedure |
| 360 | parametres/documents-personnalises-pdf-builder.md | 443 | personnalisation avancée de la mise en page des documents (avenants, factures) via PDF builder | facturation | personnalisation, documents, photos | oui | non | oui | non | non | procedure |

| 361 | parametres/employes.md | 88 | création de fiches employés (coordonnées, gestion des accès) | indetermine | roles | oui | oui | non | non | non | procedure |
| 362 | parametres/envoyer-les-factures-vers-le-logiciel-comptable.md | 447 | synchronisation/envoi des factures (clients, notes de crédit, fournisseurs) vers le logiciel comptable | facturation | integrations, automatisation | oui | oui | oui | non | oui | procedure |
| 363 | parametres/gestion-des-modeles-activer-ou-desactiver-un-modele-de-devis.md | 123 | activation ou désactivation d'un modèle de devis | devis | catalogue, personnalisation | oui | non | non | non | non | procedure |
| 364 | parametres/gestion-des-permissions.md | 525 | gestion des permissions et rôles utilisateurs (accès aux menus) | indetermine | roles, permissions | oui | oui | oui | oui | oui | faq_depannage |
| 365 | parametres/gmail-envoi-des-emails-avec-ta-propre-adresse.md | 388 | intégration Gmail/Google Workspace pour l'envoi d'emails depuis sa propre adresse | indetermine | integrations, communication, securite_compte | oui | oui | oui | oui | oui | faq_depannage |
| 366 | parametres/guide-d-installation-de-la-synchronisation-comptable.md | 1199 | guide complet d'installation de la synchronisation comptable (connexion, TVA, comptes généraux, journaux, plan analytique, contacts) | facturation | integrations, conformite_reglementaire, automatisation | oui | oui | oui | oui | oui | procedure |
| 367 | parametres/horaire-de-la-societe.md | 75 | configuration de l'horaire par défaut de la société (ouvriers, planning) | indetermine | planning | oui | non | non | non | non | procedure |
| 368 | parametres/independants.md | 76 | création de fiches indépendants (coordonnées, horaire) | indetermine | roles | oui | non | non | non | non | procedure |
| 369 | parametres/informations-generales-de-la-societe.md | 147 | configuration des informations générales de la société (logo, coordonnées) réutilisées dans les documents | indetermine | personnalisation, documents | oui | non | non | non | non | procedure |
| 370 | parametres/informations-generales-du-profil.md | 135 | configuration du profil utilisateur (informations, photo) | indetermine | personnalisation | oui | non | non | non | non | procedure |
| 371 | parametres/integration-cebeo.md | 615 | intégration CEBEO (catalogue de fournitures électriques importable dans devis, ouvrages, bibliothèque de prix) | devis | integrations, catalogue, tarification | oui | oui | oui | non | oui | procedure |
| 372 | parametres/les-metadonnees-dans-les-e-mails.md | 403 | métadonnées/balises dynamiques personnalisables dans les modèles d'email | indetermine | personnalisation, communication, automatisation | oui | non | non | non | non | procedure (ton partiellement promotionnel) |
| 373 | parametres/les-pays.md | 115 | gestion de la liste des pays | indetermine | catalogue | oui | non | non | non | non | procedure |
| 374 | parametres/les-taux-de-tva.md | 145 | configuration des taux de TVA (correspondance avec le logiciel comptable) | indetermine | catalogue, conformite_reglementaire, integrations | oui | non | non | non | non | procedure |
| 375 | parametres/les-unites.md | 135 | gestion des unités utilisées dans les formulaires (devis, factures, commandes) | indetermine | catalogue, personnalisation | oui | non | non | non | non | procedure |

| 376 | parametres/liste-des-codes-d-erreurs-de-synchronisation-comptable.md | 1711 | référentiel des codes d'erreur de synchronisation comptable et leurs solutions | facturation | integrations, support_editeur | oui | non | non | non | oui | faq_depannage |
| 377 | parametres/methodes-de-paiements.md | 126 | configuration des méthodes de paiement disponibles | facturation | paiement, catalogue | oui | non | non | non | non | procedure |
| 378 | parametres/modele-d-email-par-defaut.md | 154 | configuration du modèle d'email par défaut à l'envoi | indetermine | personnalisation, communication | oui | non | oui | oui | non | faq_depannage |
| 379 | parametres/modeles-d-e-mails.md | 194 | création de modèles d'e-mails réutilisables par type de document | indetermine | personnalisation, communication, catalogue | oui | non | non | non | non | procedure |
| 380 | parametres/modeles-de-documents.md | 227 | présentation des niveaux de personnalisation des modèles de documents (devis, avenants, factures) | indetermine | personnalisation, documents | non | non | non | non | non | marketing_dans_aide |
| 381 | parametres/modifier-le-mot-de-passe-de-mon-profil.md | 70 | modification du mot de passe de son propre profil | indetermine | securite_compte | oui | non | non | non | non | procedure |
| 382 | parametres/modifier-un-modele-personnalisez-vos-documents-etape-par-etape.md | 516 | modification détaillée d'un modèle de document (page, zones, aperçu) | devis | personnalisation, documents | oui | non | oui | oui | non | procedure |
| 383 | parametres/mot-de-passe-oublie-que-faire.md | 58 | récupération d'accès en cas de mot de passe oublié (suppression/recréation du compte) | indetermine | securite_compte, roles | oui | non | oui | non | oui | faq_depannage |
| 384 | parametres/outlook-envoi-des-emails-avec-ta-propre-adresse.md | 449 | intégration Outlook/Microsoft 365 pour l'envoi d'emails depuis sa propre adresse | indetermine | integrations, communication, securite_compte | oui | oui | oui | oui | oui | faq_depannage |
| 385 | parametres/ouvriers.md | 89 | création de fiches ouvriers (coordonnées, horaire) | indetermine | roles | oui | oui | non | non | non | procedure |
| 386 | parametres/preferences-configurez-vos-modeles-par-defaut-et-l-affichage-pdf.md | 212 | configuration des modèles par défaut par type de document et de l'affichage PDF direct | devis | personnalisation, catalogue | oui | non | non | non | non | procedure |
| 387 | parametres/preferences-d-affichage.md | 371 | préférences d'affichage et valeurs par défaut des champs dans les formulaires et lignes de documents | devis | personnalisation, catalogue, tarification | oui | non | non | non | non | reference_configuration |
| 388 | parametres/preferences-des-modeles-de-documents.md | 235 | choix du modèle de document par défaut affiché à l'ouverture du PDF | devis | personnalisation | non | non | non | non | non | marketing_dans_aide |
| 389 | parametres/preferences-du-profil.md | 142 | préférences personnelles du profil (copie d'email, affichage chantier, alertes) | indetermine | personnalisation, notifications | oui | non | non | non | non | procedure |
| 390 | parametres/signature-d-e-mail.md | 148 | configuration d'une signature d'email automatique | indetermine | personnalisation, communication | oui | non | oui | non | non | procedure |

| 391 | parametres/smtp-qu-est-ce-que-c-est.md | 346 | explication du protocole SMTP et des intégrations email disponibles (avant/après la mise à jour) | indetermine | integrations, communication | non | oui | oui | oui | non | definitionnel |
| 392 | parametres/style-general-personnalisez-les-couleurs-et-polices-de-vos-documents.md | 220 | configuration du style général (polices, couleurs) par défaut des documents | devis | personnalisation | oui | non | non | non | non | procedure |
| 393 | parametres/synchronisation-comptable-vue-d-ensemble.md | 516 | vue d'ensemble de la synchronisation comptable (bénéfices, champs transférés, compatibilité logiciels) | facturation | integrations, conformite_reglementaire, automatisation | non | non | oui | oui | non | reference_configuration |
| 394 | parametres/synchronisation-des-paiements.md | 277 | synchronisation automatique des statuts de paiement (Ponto/Codabox), réconciliation manuelle si besoin | facturation | integrations, paiement, automatisation | oui | oui | non | oui | oui | procedure |
| 395 | parametres/synchroniser-vos-factures-fournisseurs-bidirectionnel.md | 303 | choix du sens de synchronisation des factures fournisseurs (envoi/réception) et procédure d'import | achat | integrations, automatisation | oui | oui | oui | oui | oui | procedure |
| 396 | parametres/taches-automatisees.md | 376 | configuration de tâches automatiques déclenchées par événement (envoi de devis, transformation en chantier) | devis | automatisation, planning | oui | oui | non | non | non | procedure |
| 397 | parametres/testo.md | 298 | intégration Testo (import de rapports d'entretien dans les rapports d'intervention mobile) via clé API | chantier-intervention | integrations, mobile, documents | oui | oui | non | non | oui | procedure |
| 398 | parametres/utilisateur-avec-un-compte-gestion.md | 252 | création et permissions d'un utilisateur avec compte gestion (accès complet) | indetermine | roles, permissions | oui | oui | oui | oui | non | procedure |
| 399 | parametres/utilisateur-avec-un-compte-ouvrier.md | 253 | création et permissions d'un utilisateur avec compte ouvrier (accès restreint) | indetermine | roles, permissions | oui | oui | oui | oui | non | procedure |
| 400 | parametres/vehicules.md | 125 | gestion de la liste des véhicules utilisables en planification | chantier-intervention | catalogue, planning | oui | non | non | non | non | procedure |
| 401 | parametres/visualisation-et-ajustements-comment-personnaliser-un-modele-pour-un-devis-precis.md | 318 | personnalisation ponctuelle d'un modèle pour un devis précis sans affecter le modèle principal | devis | personnalisation, documents | oui | non | non | oui | non | procedure |
| 402 | planning/comment-ajouter-un-chantier-au-planning.md | 83 | ajout automatique d'un chantier au planning à l'acceptation du devis | chantier-intervention | planning | oui | oui | oui | non | non | procedure |
| 403 | planning/comment-retirer-un-chantier-du-planning.md | 40 | retrait d'un chantier de l'affichage du planning | chantier-intervention | planning | oui | non | non | non | non | procedure |
| 404 | planning/creation-d-un-carnet-de-route.md | 162 | création d'un carnet de route journalier pour un chantier (tâches, commentaires par ressource) | chantier-intervention | planning, documents | oui | oui | non | non | non | procedure |
| 405 | planning/exporter-le-planning-en-pdf.md | 69 | export du planning (global ou par chantier) au format PDF | chantier-intervention | planning, documents | oui | non | non | non | non | procedure |

| 406 | planning/fonctionnement-de-la-meteo-dans-le-planning.md | 80 | affichage des prévisions météo par chantier dans le planning | chantier-intervention | planning, geolocalisation | oui | non | non | non | non | definitionnel |
| 407 | planning/planification-des-ressources-dans-le-planning.md | 333 | planification des ressources (ouvriers, indépendants) dans le planning et impact sur la rentabilité | chantier-intervention | planning, roles | oui | oui | oui | oui | non | procedure |
| 408 | planning/que-se-passe-t-il-lorsque-l-on-copie-colle-les-ressources-d-un-ouvrier-sur-une-autre-journee-via-la-plateforme.md | 124 | comportement du copier-coller des ressources d'un ouvrier sur une autre journée | chantier-intervention | planning | non | non | oui | non | non | faq_depannage |
| 409 | rh/planning-des-absences.md | 198 | gestion du planning des absences des ouvriers et indépendants | indetermine | planning, roles | oui | oui | oui | non | non | procedure |
| 410 | rh/pointage.md | 671 | configuration et gestion du pointage (temps de travail, mobilité, indemnités, heures supplémentaires en France) | indetermine | planning, conformite_reglementaire, automatisation | oui | oui | oui | oui | non | procedure |
| 411 | rh/type-d-absences.md | 138 | configuration des types d'absences | indetermine | catalogue | oui | non | non | non | non | procedure |
| 412 | statistiques/statistiques.md | 552 | présentation des tableaux de bord statistiques (KPI, devis, finances, CRM, commandes, interventions) | indetermine | reporting, crm | non | non | non | non | non | reference_configuration |
| 413 | stock/bon-de-retour.md | 986 | création d'un bon de retour de stock (paramétrage préalable et procédure) | achat | gestion_stock, catalogue, tarification | oui | oui | oui | non | non | procedure |
| 414 | stock/bon-de-sortie-de-stock.md | 384 | création d'un bon de sortie de stock vers un chantier/intervention | chantier-intervention | gestion_stock, roles | oui | oui | oui | non | non | procedure |
| 415 | stock/bon-de-transfert.md | 874 | transfert de fournitures entre emplacements de stock (paramétrage et procédure) | indetermine | gestion_stock, catalogue | oui | oui | non | non | non | procedure |
| 416 | stock/commande-de-stock.md | 503 | création et suivi des commandes de réapprovisionnement de stock auprès des fournisseurs | achat | gestion_stock, paiement, roles | oui | oui | oui | oui | oui | procedure |
| 417 | stock/emplacement-de-stock.md | 129 | gestion des emplacements de stock (cartographie par niveaux) | indetermine | gestion_stock, catalogue | oui | non | oui | non | non | procedure |
| 418 | stock/etat-des-stocks.md | 261 | présentation de l'état des stocks (quantité, valeur, emplacement) à un instant donné | indetermine | gestion_stock, reporting | non | non | non | non | non | reference_configuration |
| 419 | stock/inventaire.md | 431 | réalisation et clôture d'un inventaire de stock (comptage, delta, import/export) | indetermine | gestion_stock, documents | oui | oui | oui | oui | non | procedure |
| 420 | stock/mouvement-des-stocks.md | 289 | historique et filtrage des mouvements de stock (entrées, sorties, transferts, ajustements) | indetermine | gestion_stock, reporting, recherche | non | non | non | non | non | reference_configuration |

| 421 | stock/preferences-du-stock.md | 191 | configuration des préférences du stock (niveaux d'emplacements, réapprovisionnement automatique) | indetermine | gestion_stock, automatisation | oui | non | non | non | non | procedure |
| 422 | stock/remplir-son-stock-pour-la-premiere-fois.md | 878 | guide de démarrage pour initialiser le stock (préparation des fournitures, import, premier inventaire) | indetermine | gestion_stock, documents, automatisation | oui | oui | non | non | non | procedure |
| 423 | tableau-de-bord/tableau-de-bord.md | 699 | présentation et personnalisation du tableau de bord (widgets selon le pack) | indetermine | personnalisation, reporting, crm | oui | non | oui | oui | non | reference_configuration |
| 424 | taches/taches.md | 397 | gestion des tâches administratives (champs requis, module tâches admin) | indetermine | automatisation, communication, planning | oui | non | oui | non | non | procedure (ton partiellement promotionnel) |
| 425 | vertuowork/comment-consulter-et-gerer-les-candidatures-a-mon-annonce-sur-vertuowork.md | 180 | consultation et gestion des candidatures reçues sur une annonce VertuoWork | indetermine | marketplace, communication | oui | oui | oui | non | non | procedure |
| 426 | vertuowork/decouvrir-vertuowork.md | 131 | présentation de VertuoWork (plateforme de mise en relation porteurs de projet / entreprises de construction) | indetermine | marketplace | non | non | non | non | non | definitionnel |
| 427 | vertuowork/modifier-une-annonce-sur-vertuowork.md | 123 | modification d'une annonce publiée sur VertuoWork | indetermine | marketplace | oui | non | non | non | non | procedure |
| 428 | vertuowork/postulez-a-une-annonce-sur-vertuowork.md | 129 | candidature à une annonce sur VertuoWork | indetermine | marketplace, communication | oui | oui | non | non | non | procedure |
| 429 | vertuowork/publier-une-nouvelle-annonce-sur-vertuowork.md | 135 | publication d'une nouvelle annonce sur VertuoWork | indetermine | marketplace | oui | oui | oui | non | non | procedure |
| 430 | vertuowork/retirer-une-candidature-sur-vertuowork.md | 128 | retrait d'une candidature déposée sur VertuoWork | indetermine | marketplace | oui | non | non | non | non | procedure |
| 431 | vertuowork/supprimer-une-annonce-sur-vertuowork.md | 112 | suppression définitive d'une annonce sur VertuoWork | indetermine | marketplace | oui | non | oui | oui | non | procedure |

CHECKPOINT vertuoza_help : 431/431 traités

## Contrôles mécaniques de complétude

- Documents traités : 431/431 (guard-rail 433 − 2 déjà LIGHT = 431, écart 0).
- Numérotation `#` : continue de 1 à 431, aucun doublon.
- `chemin_relatif` : 431 valeurs, aucun doublon — y compris les 3 paires à
  slug de titre identique (docs #94/#95, #142/#143, #197/#198), dont les
  chemins et identifiants source restent distincts (vérifié par chemin,
  pas par titre, conformément à l'anomalie documentée en tête de fichier).
- Colonnes : 12/12 sur les 431 lignes (`NF=14` avec les champs vides de
  bord, vérifié par `awk -F'|'`).
- `moment_parcours` : vocabulaire fermé respecté sur les 431 lignes —
  aucune valeur hors de `indetermine · demande · devis · achat ·
  chantier-intervention · facturation`.
- `capacites_transverses` : aucune ligne au-delà de 3 valeurs ; `—` utilisé
  quand aucune capacité identifiée.
- `longueur_mots` : recalculée mécaniquement par `awk` (méthode déclarée
  ci-dessus) pour les 431 documents, jamais estimée.
- `genre_documentaire` : agrégation calculée sur la racine (annotations
  entre parenthèses non comptées comme valeurs distinctes).

## Agrégats descriptifs

**`moment_parcours`** (431 documents) :

```
indetermine            116
devis                    92
facturation              90
chantier-intervention    85
achat                    41
demande                   7
```

**`capacites_transverses`** (occurrences, un document peut compter dans
plusieurs valeurs, max 3/document) :

```
tarification            57
documents                56
integrations             52
personnalisation         50
paiement                 50
catalogue                46
planning                 43
roles                    39
automatisation           36
conformite_reglementaire 32
communication            30
gestion_stock            29
mobile                   25
securite_compte          18
crm                      18
notifications            12
reporting                10
marketplace               7
recherche                 6
photos                    6
permissions               5
multi-societe             5
geolocalisation           5
support_editeur           2
validation                1
```

Sur ces 25 valeurs, 7 sont absentes de l'inventaire historique §4 de
SCHEMA-LIGHT.md : `geolocalisation`, `crm`, `personnalisation`,
`multi-societe`, `tarification`, `reporting`, `marketplace`. Toutes
traitées au fil du contrôle de vocabulaire (cf. Incidents et
corrections) : six retenues comme `VALEUR_DISTINCTE` (conservées sans
fusion), `tarification` laissée en arbitrage différé (employée par
jugement documentaire, non tranchée vis-à-vis de `catalogue`).

**`genre_documentaire`** (racine, 431 documents) :

```
procedure               169
faq_depannage            149
definitionnel             62
reference_configuration   48
marketing_dans_aide        2
autre                      1
```

**`contenu_observable`** (431 documents, valeurs `oui`/`non`, aucune
observation codée `inconnu` dans ce run) :

```
procedure          oui 301 · non 130
transition_objet    oui  94 · non 337
regle_ou_condition  oui 255 · non 176
contrainte_ou_limite oui 130 · non 301
exception_ou_correction oui 112 · non 319
```

**`longueur_mots`** — somme totale : 84 576 mots sur 431 documents.

## Cas que LIGHT représente mal

- **Le module VertuoWork** (marketplace de mise en relation entre porteurs
  de projet et entreprises de construction) n'a pas d'équivalent dans les
  autres corpus LIGHT déjà produits. LIGHT capture sa présence
  documentaire (7 documents, capacité `marketplace`) mais ne dit rien sur
  son adoption réelle, son volume d'annonces ou sa place dans l'usage
  global du produit.
- **Les FAQ de troubleshooting comptable** (codes d'erreur de
  synchronisation, mapping clients/fournisseurs) forment un bloc dense
  (plusieurs centaines à plus de 1700 mots) dont la richesse documentaire
  reflète la complexité technique de l'intégration comptable, non
  nécessairement sa fréquence d'usage réelle par les clients.
- **Les documents à contenu partiellement promotionnel** (`modeles-de-
  documents.md`, `preferences-des-modeles-de-documents.md`, `les-
  metadonnees-dans-les-e-mails.md`, `taches.md`) mélangent description
  fonctionnelle et argumentaire commercial ; LIGHT les code selon leur
  contenu documentaire observable, sans neutraliser le ton.
- **`tarification` non tranchée** : 57 occurrences dans ce corpus, la plus
  fréquente valeur hors inventaire historique. Sa fréquence élevée signale
  un besoin réel d'arbitrage (relation avec `catalogue`), explicitement
  hors du périmètre de cette mission de production.

## Limites

Ce fichier applique le protocole LIGHT défini dans SCHEMA-LIGHT.md et
n'en modifie aucune règle. Comme rappelé au §9 de ce contrat : une carte
de sélection, pas une conclusion. Elle ne permet pas de trancher seule la
fréquence d'usage, l'importance métier, l'adoption, la satisfaction, la
qualité UX ou du support, la performance réelle, l'absence d'une
fonctionnalité, ni la prévalence d'un phénomène sur le marché. Un
document pauvre ou vide signifie seulement peu ou pas de contenu
documentaire observable dans cette source. Les deux valeurs `tarification`
et `marketing_et_communication` (cette dernière absente de ce corpus)
restent des arbitrages différés, hors périmètre de cette mission.
