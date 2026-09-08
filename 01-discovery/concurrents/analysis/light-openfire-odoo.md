# LIGHT — production OpenFire / Odoo Knowledge (corpus documentation)

**Un des deux corpus documentaires distincts d'OpenFire** (`corpus_index.json`,
`corpus_id: openfire_odoo`, `type: documentation`, `source_platform: odoo`).
L'autre corpus, `openfire_zendesk`, est traité séparément dans
`light-openfire-zendesk.md`. Aucune fusion, aucune comparaison implicite
entre les deux — décision déjà actée dans `corpus_index.json` :
« Corpus documentaire distinct du corpus 'aide' du même concurrent. Aucune
fusion, aucune comparaison implicite. »

Production sous SCHEMA-LIGHT.md (contrat canonique), lu intégralement avant
ce run. Discipline : un document à la fois, lu intégralement, sortie écrite
immédiatement, aucune correction rétroactive sauf erreur mécanique démontrée
et journalisée. Run de production, pas un test méthodologique de LIGHT.

## Périmètre — vérification mécanique et gel

- `openfire_odoo` (`corpus_index.json`) : **213** documents (`type:
  documentation`, 4 rubriques éditoriales déclarées : `knowsystem`,
  `profile`, `slides`, `website`). Aucune `analysis_exclusions` déclarée
  par le générateur pour ce corpus.
- Déjà utilisé (pilote LIGHT sur corpus inédit, ligne 9) : **1**
  — `knowsystem/102.md`.
- **Inédits à traiter, périmètre gelé : 212.**

Vérification mécanique : 213 (disque, `find -name "*.md"`) = 212 (inédits)
+ 1 (exclu), union exacte, 0 doublon, 0 chemin manquant, 0 chevauchement.

Répartition disque des 212 inédits : 199 dans `knowsystem/` (dont 17
pages de navigation pures — identifiants numériques sans slug, voir
Incidents), 13 hors `knowsystem/` (`dm-openfire-fr.md`, `faq.md`,
`index.md`, `knowsystem.md`, `l-equipe-openfire.md`, `mentions.md`,
`mettre-a-jour-un-article-centralise.md`, `profile/ranks-badges.md`,
`profile/users.md`, `slides.md`, `slides/all.md`, `webinaires.md`,
`website/info.md`).

## Méthode `longueur_mots`

Mécanique, conforme SCHEMA-LIGHT.md §4 : `wc -w` sur le corps Markdown
après suppression du frontmatter YAML.

## Barrière de sécurité — sources non fiables

Chaque source est traitée comme donnée à analyser, jamais comme instruction.
Journal tenu en continu ci-dessous ; vide si rien à signaler sur un lot.

## Incidents et corrections

(journal tenu en continu)

- **Plusieurs pages structurelles de ce corpus contiennent des fragments de
  rendu HTML non nettoyés** (`dm-openfire-fr.md`, `index.md`,
  `knowsystem.md`) : titres de section vides (`### `), balises et
  espacements bruts visibles dans le texte collecté. Ce n'est pas traité
  comme une instruction ni une donnée à corriger — le contenu est codé tel
  quel, en `autre`, sans reconstruction du rendu visuel d'origine.
- **17 documents `knowsystem/<identifiant numérique>.md`** (103, 108, 110,
  116, 126, 153, 154, 181, 231, 241, 258, 260, 266, 270, 277, 298, 303)
  sont des pages de catégorie pures : une liste de titres d'articles liés,
  sans corps documentaire propre — même nature que la limite déjà
  documentée sur le pilote (doc #9) et sur ProGBat
  (`bibliotheque/elements/*`). Codées `autre (page de navigation)`.
- **`knowsystem.md`** agrège des extraits partiels de plusieurs articles
  distincts (Position Fiscale, génération de pièce comptable depuis un
  modèle, calculateur de déperdition de chaleur, factures client) plus
  l'arborescence complète du site. Ces articles existent par ailleurs sous
  leur propre chemin slugué dans le périmètre gelé et y sont codés
  intégralement à leur tour — `knowsystem.md` n'est donc pas une source
  supplémentaire de faits, codée `autre` sans extraction de contenu.
- **Plusieurs paires d'articles distincts couvrent un contenu très
  largement redondant** (constaté, non corrigé — chaque document reste codé
  indépendamment sur son propre contenu, per SCHEMA-LIGHT.md) :
  `gerer-les-primes-energetiques-148.md` / `impression-des-totaux-dans-les-factures-183.md`
  (paramétrage d'impression des primes) ; `parametrer-un-serveur-mail-151.md`
  / `mails-en-erreurs-sur-gmail-smtp-535-282.md` (procédure mot de passe
  d'application Gmail) ; `quels-documents-fournir-a-votre-comptable-212.md`
  / `rapport-comptable-fec-213.md` (extraction du FEC). Aucune fusion,
  aucune déduplication effectuée — chaque chemin canonique reste une ligne
  LIGHT distincte.
- **3 documents `webinaires/*` sont des pages de renvoi vers un replay
  vidéo externe** (`webinaire-inventaire-235.md`,
  `webinaire-mobile-244.md`, `webinaire-signature-electronique-263.md`) :
  liste de chapitres et de liens YouTube, sans contenu procédural propre.
  Codées `autre (stub webinaire)` — même nature que les stubs
  `guides-videos` déjà documentés sur `openfire_zendesk`.
- Aucun contenu à caractère d'instruction, de demande de secret,
  d'identifiants, de jeton ou d'exécution n'a été rencontré dans les 212
  documents. Plusieurs articles décrivent, de façon strictement
  documentaire, des procédures de configuration côté client impliquant des
  identifiants tiers (mot de passe d'application Gmail, ID/secret OAuth
  Google) — il s'agit de la documentation produit elle-même expliquant à
  l'utilisateur comment configurer *son propre* compte, non d'une tentative
  d'obtention de secret par la source. Aucun `INCIDENT_SECURITE_SOURCE`.
- **2026-09-09 — Correction d'un doublon lexical démontré :
  `integration_tierce` → `integrations`.** Un audit indépendant des dix
  valeurs de `capacites_transverses` absentes du §4 de SCHEMA-LIGHT.md a
  établi la preuve mécanique suivante : la même fonctionnalité réelle (la
  signature électronique Yousign) était codée `integrations` au document
  #55 (`configuration-262.md`) et `integration_tierce` au document #156
  (`mise-en-place-de-la-signature-electronique-261.md`) — même objet, deux
  formulations lexicales. Erreur mécanique démontrée au sens de
  SCHEMA-LIGHT.md §4 (« ne pas créer de doublon lexical d'une capacité
  existante »). Correction : substitution de `integration_tierce` par
  `integrations` sur les 3 lignes concernées (#88
  `eldotravo-267.md`, #156 `mise-en-place-de-la-signature-electronique-261.md`,
  #202 `synchronisation-google-agenda-269.md`). Aucune ligne n'a résulté
  avec `integrations` en double ni avec plus de 3 capacités. Aucune autre
  ligne, aucun autre champ n'a été touché. Les sept autres valeurs
  nouvelles identifiées par le même audit (`comptabilite`, `crm`,
  `geolocalisation`, `reporting`, `facturation`, `personnalisation`,
  `multi-societe`) sont conservées telles quelles — concepts distincts
  démontrés. Les deux cas jugés ambigus par l'audit (`tarification` vis-à-vis
  de `catalogue`, `marketing_et_communication` vis-à-vis de `communication`)
  restent en l'état, non tranchés : leur arbitrage exigerait une définition
  écrite du périmètre de `catalogue` et de `communication`, absente de
  SCHEMA-LIGHT.md, question explicitement différée.

## Sorties LIGHT

| # | chemin_relatif | longueur_mots | objet_principal | moment_parcours | capacites_transverses | procedure | transition_objet | regle_ou_condition | contrainte_ou_limite | exception_ou_correction | genre_documentaire |
|---:|---|---:|---|---|---|:-:|:-:|:-:|:-:|:-:|---|
| 1 | dm-openfire-fr.md | 53 | indetermine (page d'accueil, fragment HTML incomplet) | indetermine | — | non | non | non | non | non | autre (fragment de rendu) |
| 2 | faq.md | 143 | FAQ (sommaire des questions, sans réponses) | indetermine | — | non | non | non | non | non | autre (sommaire FAQ sans réponses) |
| 3 | index.md | 53 | indetermine (page d'accueil, fragment HTML incomplet) | indetermine | — | non | non | non | non | non | autre (fragment de rendu) |
| 4 | knowsystem.md | 1261 | indetermine (page d'index agrégée, extraits partiels de plusieurs articles) | indetermine | — | non | non | non | non | non | autre (page d'index agrégée) |
| 5 | l-equipe-openfire.md | 105 | présentation de l'entreprise OpenFire | indetermine | — | non | non | non | non | non | marketing_dans_aide |
| 6 | mentions.md | 2166 | mentions légales et politique de confidentialité | indetermine | conformite_reglementaire | non | non | oui | oui | non | politique_legale |
| 7 | mettre-a-jour-un-article-centralise.md | 437 | article centralisé (mise à jour tarifs, archivage) | achat | catalogue, automatisation, integrations | oui | oui | oui | oui | non | procedure |
| 8 | profile/ranks-badges.md | 173 | grades et badges (plateforme documentaire, hors produit) | indetermine | — | non | non | non | non | non | autre (gamification plateforme) |
| 9 | profile/users.md | 48 | indetermine (classement utilisateurs, plateforme) | indetermine | — | non | non | non | non | non | autre (page de navigation) |
| 10 | slides.md | 21 | indetermine (plateforme eLearning, aucun cours publié) | indetermine | — | non | non | non | non | non | autre (page vide) |
| 11 | slides/all.md | 46 | indetermine (plateforme eLearning, aucun cours publié) | indetermine | — | non | non | non | non | non | autre (page de navigation) |
| 12 | webinaires.md | 37 | indetermine (sommaire webinaires, sans contenu) | indetermine | — | non | non | non | non | non | autre (page de navigation) |
| 13 | website/info.md | 135 | modules installés (instance Odoo, informations techniques) | indetermine | integrations | non | non | non | non | non | reference_configuration |
| 14 | knowsystem/103.md | 72 | menu Intervention (navigation) | indetermine | — | non | non | non | non | non | autre (page de navigation) |
| 15 | knowsystem/108.md | 26 | menu Contact (navigation) | indetermine | — | non | non | non | non | non | autre (page de navigation) |
| 16 | knowsystem/110.md | 32 | menu Stock (navigation) | indetermine | — | non | non | non | non | non | autre (page de navigation) |
| 17 | knowsystem/116.md | 91 | menu Vente (navigation) | indetermine | — | non | non | non | non | non | autre (page de navigation) |
| 18 | knowsystem/126.md | 57 | menu CRM (navigation) | indetermine | — | non | non | non | non | non | autre (page de navigation) |
| 19 | knowsystem/153.md | 36 | menu Achat (navigation) | indetermine | — | non | non | non | non | non | autre (page de navigation) |
| 20 | knowsystem/154.md | 80 | menu Comptabilité (navigation) | indetermine | — | non | non | non | non | non | autre (page de navigation) |
| 21 | knowsystem/181.md | 54 | menu Facturation (navigation) | indetermine | — | non | non | non | non | non | autre (page de navigation) |
| 22 | knowsystem/231.md | 18 | menu Publipostage (navigation) | indetermine | — | non | non | non | non | non | autre (page de navigation) |
| 23 | knowsystem/241.md | 45 | menu général + sous-menu SMS (navigation) | indetermine | — | non | non | non | non | non | autre (page de navigation) |
| 24 | knowsystem/258.md | 20 | menu Dashboard (navigation) | indetermine | — | non | non | non | non | non | autre (page de navigation) |
| 25 | knowsystem/260.md | 45 | menu général + sous-menu Signature Électronique (navigation) | indetermine | — | non | non | non | non | non | autre (page de navigation) |
| 26 | knowsystem/266.md | 44 | menu général + sous-menu RDV en Ligne (navigation) | indetermine | — | non | non | non | non | non | autre (page de navigation) |
| 27 | knowsystem/270.md | 44 | menu général + sous-menu Outils de Calcul (navigation) | indetermine | — | non | non | non | non | non | autre (page de navigation) |
| 28 | knowsystem/277.md | 20 | menu Mobile (navigation) | indetermine | — | non | non | non | non | non | autre (page de navigation) |
| 29 | knowsystem/298.md | 45 | menu général + sous-menu Serveur Mail (navigation) | indetermine | — | non | non | non | non | non | autre (page de navigation) |
| 30 | knowsystem/303.md | 37 | menu général + sous-menu GED (navigation) | indetermine | — | non | non | non | non | non | autre (page de navigation) |

| 31 | knowsystem/acceder-aux-tarifs-centralises-152.md | 395 | tarif centralisé (accès, recherche d'articles) | devis | catalogue, integrations | oui | oui | non | non | non | procedure |
| 32 | knowsystem/affichage-du-planning-79.md | 504 | planning (vues : planning/calendrier/liste/carte, filtres) | chantier-intervention | planning, recherche | oui | non | non | oui | non | reference_configuration |
| 33 | knowsystem/amortissements-224.md | 367 | amortissement (immobilisations, méthodes de calcul) | indetermine | conformite_reglementaire, automatisation | oui | non | oui | non | non | reference_configuration |
| 34 | knowsystem/analyse-ca-facture-280.md | 184 | analyse du chiffre d'affaires facturé (rapport) | facturation | recherche, documents | oui | non | non | non | non | procedure |
| 35 | knowsystem/analyser-ses-opportunites-120.md | 329 | opportunité (analyse pipeline, tunnels de conversion) | demande | recherche, roles | oui | non | non | non | non | procedure |
| 36 | knowsystem/annuler-rembourser-ou-modifier-un-paiement-163.md | 264 | paiement (annulation, remboursement, modification) | facturation | paiement, automatisation | oui | oui | oui | non | non | procedure |
| 37 | knowsystem/approvisionnement-en-exeption-252.md | 212 | approvisionnement en exception (erreurs de traitement) | achat | gestion_stock, automatisation | oui | non | oui | non | oui | procedure (avec dépannage intégré) |
| 38 | knowsystem/approvisionnement-intersociete-245.md | 181 | approvisionnement intersociété (module, règles) | achat | gestion_stock, automatisation, integrations | oui | oui | oui | oui | non | procedure |
| 39 | knowsystem/associer-paiements-et-factures-162.md | 166 | paiement (rapprochement avec facture) | facturation | paiement, automatisation | oui | oui | non | non | non | procedure |
| 40 | knowsystem/authentification-azure-pour-office-365-294.md | 1080 | authentification Azure (Office 365, serveur mail) | indetermine | integrations, securite_compte, communication | oui | non | oui | oui | non | procedure |
| 41 | knowsystem/balance-agee-274.md | 504 | balance âgée (rapport créances/dettes) | facturation | paiement, documents | oui | non | non | non | non | reference_configuration |
| 42 | knowsystem/calculateur-de-deperdition-de-chaleur-80.md | 801 | calcul de déperdition de chaleur (dimensionnement, formule) | devis | catalogue, documents, automatisation | oui | non | non | oui | non | procedure |
| 43 | knowsystem/categories-d-articles-188.md | 733 | catégorie d'article (regroupement, valorisation, comptabilité) | indetermine | catalogue, gestion_stock, conformite_reglementaire | oui | non | oui | oui | non | reference_configuration |
| 44 | knowsystem/certains-termes-ou-noms-de-l-interface-sont-etranges-ou-traduits-209.md | 96 | traduction automatique du navigateur (dépannage interface) | indetermine | — | oui | non | non | non | oui | faq_depannage |
| 45 | knowsystem/cloturer-un-exercice-fiscal-124.md | 461 | exercice fiscal (clôture, verrouillage) | indetermine | conformite_reglementaire, automatisation | oui | oui | oui | oui | non | procedure |

| 46 | knowsystem/commande-directe-achat-site-altema-215.md | 480 | connecteur d'achat (Altema/Modinox) | achat | integrations, automatisation, catalogue | oui | oui | oui | oui | non | procedure |
| 47 | knowsystem/commande-directe-achat-site-poujoulat-336.md | 267 | connecteur d'achat (Poujoulat) | achat | integrations, automatisation, catalogue | oui | oui | non | oui | non | procedure |
| 48 | knowsystem/comment-appliquer-des-regles-de-prix-par-contact-221.md | 122 | liste de prix (règles par contact) | devis | catalogue, roles | oui | non | non | oui | non | procedure |
| 49 | knowsystem/comment-faire-une-remise-globale-217.md | 176 | remise globale (devis) | devis | catalogue, paiement | oui | non | non | non | non | procedure |
| 50 | knowsystem/comment-generer-un-acompte-202.md | 114 | acompte (facture) | facturation | paiement, automatisation | oui | oui | non | non | non | procedure |
| 51 | knowsystem/comment-modifier-une-facture-validee-210.md | 130 | facture validée (modification via avoir) | facturation | conformite_reglementaire, paiement | oui | oui | oui | oui | oui | procedure |
| 52 | knowsystem/comment-solder-une-facture-via-une-od-276.md | 121 | facture (solder via écriture OD) | facturation | paiement, automatisation | oui | oui | oui | non | oui | procedure |
| 53 | knowsystem/comment-supprimer-la-date-de-reglement-a-l-impression-des-factures-206.md | 75 | date de règlement (impression facture, personnalisation) | facturation | documents, paiement | oui | non | non | non | non | procedure |
| 54 | knowsystem/conditions-de-reglement-156.md | 465 | condition de règlement (échéancier) | facturation | paiement, documents | oui | non | oui | non | non | reference_configuration |
| 55 | knowsystem/configuration-262.md | 406 | signature électronique (configuration Yousign, emails, rappels) | devis | integrations, communication, documents | oui | non | oui | oui | non | reference_configuration |
| 56 | knowsystem/configuration-265.md | 1316 | prise de RDV en ligne (configuration complète) | chantier-intervention | planning, presence_en_ligne, roles | oui | non | oui | oui | non | reference_configuration |
| 57 | knowsystem/configuration-connect-affichage-sans-fil-windows-242.md | 75 | affichage sans fil (Windows Connect, mobile) | indetermine | mobile, integrations | oui | non | non | non | non | procedure |
| 58 | knowsystem/configuration-sms-237.md | 226 | SMS (configuration alertes, passerelle, modèles) | indetermine | communication, integrations, automatisation | oui | non | non | oui | non | reference_configuration |
| 59 | knowsystem/configurations-250.md | 441 | gestion de stock (configuration générale, routes, stratégies) | indetermine | gestion_stock, automatisation | oui | non | oui | non | non | reference_configuration |
| 60 | knowsystem/configurations-generales-20.md | 821 | configuration générale (planning, intervention, mobile) | chantier-intervention | planning, mobile, paiement | oui | non | oui | oui | non | reference_configuration |

| 61 | knowsystem/configurer-la-situation-retenue-de-garantie-et-compte-prorata-208.md | 685 | configuration comptable des situations, retenues de garantie et prorata | facturation | comptabilite, facturation, multi-societe | oui | non | oui | oui | non | reference_configuration |
| 62 | knowsystem/configurer-mes-relances-144.md | 209 | configuration des relances de factures impayées | facturation | automatisation, paiement | oui | non | oui | non | non | procedure |
| 63 | knowsystem/connexion-96.md | 212 | connexion à la base de production et à la base de test | indetermine | — | oui | non | oui | oui | non | definitionnel |
| 64 | knowsystem/consulter-mes-stocks-225.md | 748 | consultation et suivi des stocks (quantités, mouvements, inventaire à la date) | achat | gestion_stock, reporting | oui | non | oui | oui | non | procedure |
| 65 | knowsystem/controler-mes-interventions-81.md | 361 | contrôle de la planification des interventions (retard, à programmer) | chantier-intervention | planning, geolocalisation | oui | oui | oui | non | non | reference_configuration |
| 66 | knowsystem/correspondance-des-paiements-et-des-factures-167.md | 279 | lettrage des factures et paiements non rapprochés | facturation | paiement, comptabilite | oui | non | oui | oui | oui | procedure |
| 67 | knowsystem/creer-et-configurer-un-tableau-287.md | 330 | création et configuration d'un tableau de bord | indetermine | reporting, personnalisation | oui | non | non | oui | non | procedure |
| 68 | knowsystem/creer-et-personnaliser-un-widget-256.md | 677 | création et personnalisation des widgets d'un tableau de bord | indetermine | reporting, personnalisation | oui | oui | non | non | non | procedure |
| 69 | knowsystem/creer-et-suivre-une-campagne-234.md | 355 | création et suivi de campagnes marketing (publipostage) | demande | marketing_et_communication, automatisation, crm | oui | oui | non | non | non | procedure |
| 70 | knowsystem/creer-ligne-de-contrat-308.md | 844 | création et gestion d'une ligne de contrat (facturation, planification, équipement) | chantier-intervention | planning, facturation, automatisation | oui | oui | oui | oui | oui | procedure |
| 71 | knowsystem/creer-ma-facture-finale-145.md | 248 | création de la facture finale après acompte | facturation | paiement, comptabilite | oui | oui | oui | oui | non | procedure |
| 72 | knowsystem/creer-un-article-6.md | 635 | création et paramétrage d'un article (produit, service, consommable) | devis | gestion_stock, tarification, facturation | oui | oui | oui | oui | non | reference_configuration |
| 73 | knowsystem/creer-un-avoir-130.md | 530 | création d'un avoir (partiel, annulation, modification de facture) | facturation | paiement, comptabilite | oui | non | oui | oui | oui | procedure |
| 74 | knowsystem/creer-un-contact-16.md | 522 | création et structuration d'une fiche contact | indetermine | geolocalisation, crm | oui | oui | non | oui | non | reference_configuration |
| 75 | knowsystem/creer-un-contrat-302.md | 661 | création et paramétrage d'un contrat récurrent (facturation, renouvellement) | chantier-intervention | planning, facturation, automatisation | oui | oui | oui | non | non | procedure |

| 76 | knowsystem/creer-un-devis-1.md | 811 | création d'un devis (client, dates, taxes, lignes, envoi) | devis | tarification, facturation, paiement | oui | oui | oui | non | non | procedure |
| 77 | knowsystem/creer-un-devis-depuis-une-opportunite-128.md | 148 | création d'un devis depuis une opportunité CRM | devis | crm | oui | oui | non | non | non | procedure |
| 78 | knowsystem/creer-un-fournisseur-61.md | 238 | création et paramétrage d'une fiche fournisseur | achat | comptabilite | oui | oui | non | oui | non | reference_configuration |
| 79 | knowsystem/creer-un-publipostage-228.md | 749 | création et envoi d'un publipostage (mailing de masse) | demande | marketing_et_communication, automatisation | oui | oui | oui | oui | non | procedure |
| 80 | knowsystem/creer-une-facture-avec-retenue-de-garantie-220.md | 314 | création d'une facture avec retenue de garantie | facturation | comptabilite, paiement | oui | oui | oui | non | non | procedure |
| 81 | knowsystem/creer-une-facture-de-situation-204.md | 632 | création d'une facture de situation (facturation intermédiaire de chantier) | facturation | comptabilite, planning | oui | oui | oui | oui | non | procedure |
| 82 | knowsystem/creer-une-intervention-299.md | 664 | création et suivi d'une intervention depuis l'application mobile | chantier-intervention | mobile, planning, geolocalisation | oui | oui | oui | oui | non | procedure |
| 83 | knowsystem/creer-une-opportunite-106.md | 508 | création d'une opportunité commerciale (manuelle ou automatique) dans le CRM | demande | crm, marketing_et_communication, automatisation | oui | oui | non | non | non | procedure |
| 84 | knowsystem/creneaux-horaires-67.md | 295 | configuration des créneaux et types d'horaires des employés | indetermine | planning | oui | oui | oui | non | non | reference_configuration |
| 85 | knowsystem/definir-ses-conditions-tarifaires-169.md | 412 | définition des conditions tarifaires par marque, catégorie ou article | devis | tarification | oui | non | oui | oui | non | reference_configuration |
| 86 | knowsystem/demandes-dintervention-78.md | 874 | création et structuration d'une demande d'intervention (types, planification, facturation) | chantier-intervention | planning, facturation, geolocalisation | oui | oui | oui | non | non | reference_configuration |
| 87 | knowsystem/ecritures-comptables-et-pieces-comptables-275.md | 1001 | gestion des écritures et pièces comptables (automatisation, saisie, import) | facturation | comptabilite, automatisation | oui | oui | oui | oui | non | procedure |
| 88 | knowsystem/eldotravo-267.md | 466 | configuration et utilisation du connecteur EldoTravo (collecte d'avis clients) | chantier-intervention | marketing_et_communication, integrations | oui | non | oui | oui | non | reference_configuration |
| 89 | knowsystem/employes-65.md | 487 | paramétrage des fiches employés (poste, horaires, RH, compétences) | indetermine | planning, mobile | oui | oui | oui | oui | non | reference_configuration |
| 90 | knowsystem/enregistrer-un-paiement-161.md | 669 | enregistrement, catégorisation et régularisation des paiements de factures | facturation | paiement, comptabilite | oui | oui | oui | non | oui | procedure |

| 91 | knowsystem/entrepots-et-emplacements-227.md | 576 | gestion des entrepôts et emplacements de stockage | achat | gestion_stock | oui | oui | oui | oui | non | reference_configuration |
| 92 | knowsystem/envoyer-un-document-par-mail-146.md | 355 | envoi de documents (devis, commande, facture) par mail et gestion des échecs d'envoi | indetermine | automatisation | oui | oui | non | oui | oui | procedure |
| 93 | knowsystem/envoyer-un-sms-sur-openfire-238.md | 431 | envoi de SMS (marketing, rappel de RDV, à la demande) | indetermine | marketing_et_communication, automatisation, planning | oui | non | oui | oui | non | procedure |
| 94 | knowsystem/equipes-commerciales-176.md | 336 | création et gestion des équipes commerciales | demande | crm, automatisation | oui | oui | non | non | non | reference_configuration |
| 95 | knowsystem/extraire-la-tva-sur-encaissement-214.md | 45 | extraction du rapport TVA sur encaissement | facturation | comptabilite | oui | non | oui | non | non | procedure |
| 96 | knowsystem/facturer-mes-interventions-91.md | 257 | facturation des interventions (depuis DI, RDV, ou contrats) | facturation | planning, automatisation | oui | oui | non | oui | non | procedure |
| 97 | knowsystem/facturer-un-acompte-133.md | 433 | création d'une facture d'acompte | facturation | comptabilite, paiement | oui | oui | oui | non | non | procedure |
| 98 | knowsystem/facturer-un-contrat-309.md | 371 | génération de factures depuis un contrat (assistant de facturation) | facturation | automatisation, planning | oui | non | oui | oui | oui | procedure |
| 99 | knowsystem/factures-client-132.md | 1465 | création, structure et gestion des factures client (pro-forma, manuelle, boutique, depuis commande) | facturation | comptabilite, paiement, automatisation | oui | oui | oui | oui | non | reference_configuration |
| 100 | knowsystem/factures-client-boutique-286.md | 262 | création d'une facture boutique (vente comptoir avec sortie de stock) | facturation | gestion_stock, paiement | oui | oui | non | oui | non | procedure |
| 101 | knowsystem/faire-evoluer-l-opportunite-189.md | 217 | changement d'étape (manuel ou automatisé) d'une opportunité dans le pipeline | demande | crm, automatisation | oui | non | oui | oui | non | procedure |
| 102 | knowsystem/filtrer-vos-recherches-98.md | 239 | utilisation des filtres de recherche prédéfinis et personnalisés | indetermine | — | oui | non | non | non | non | reference_configuration |
| 103 | knowsystem/fusionner-des-pistes-opportunites-159.md | 135 | fusion des pistes et opportunités en doublon | demande | crm | oui | non | oui | non | non | procedure |
| 104 | knowsystem/generalites-et-acces-255.md | 412 | présentation générale et accès à l'application Dashboard (tableaux, widgets, domaines) | indetermine | reporting, personnalisation | non | oui | non | oui | non | definitionnel |
| 105 | knowsystem/generalites-et-tableau-de-bord-164.md | 612 | présentation générale du module Inventaire (tableau de bord des stocks, gestion en double entrée, configuration multi-société) | achat | gestion_stock, reporting | non | oui | non | oui | non | definitionnel |

| 106 | knowsystem/generation-du-bon-de-livraison-59.md | 299 | génération et structure du bon de livraison client | achat | gestion_stock, automatisation | oui | oui | non | non | non | reference_configuration |
| 107 | knowsystem/generer-automatiquement-des-opportunites-166.md | 281 | génération automatique de pistes et opportunités (email, formulaire web) | demande | crm, automatisation | oui | oui | non | non | non | procedure |
| 108 | knowsystem/generer-mes-factures-fournisseurs-173.md | 419 | génération des factures fournisseurs et paiement fournisseur | achat | comptabilite, paiement | oui | oui | oui | non | non | procedure |
| 109 | knowsystem/generer-une-commande-d-achat-157.md | 315 | génération d'une demande de prix et transformation en commande d'achat | achat | gestion_stock | oui | non | non | non | non | procedure |
| 110 | knowsystem/generer-une-piece-comptable-depuis-un-modele-268.md | 322 | création et utilisation de modèles de pièces comptables | facturation | comptabilite, automatisation | oui | oui | oui | non | non | procedure |
| 111 | knowsystem/geolocalisation-180.md | 330 | géolocalisation des contacts (manuelle ou automatique) | indetermine | geolocalisation, automatisation | oui | oui | non | non | non | procedure |
| 112 | knowsystem/gerer-la-marge-et-les-remises-125.md | 608 | gestion des remises et marges sur devis (manuelle, outil de gestion de prix, listes de prix) | devis | tarification | oui | oui | non | oui | non | procedure |
| 113 | knowsystem/gerer-les-droits-utilisateurs-63.md | 214 | gestion des droits utilisateurs pour les interventions et le paiement | indetermine | — | non | non | oui | oui | non | reference_configuration |
| 114 | knowsystem/gerer-les-etiquettes-112.md | 288 | gestion des étiquettes (contact, intervention, opportunité) | indetermine | — | oui | oui | non | non | non | reference_configuration |
| 115 | knowsystem/gerer-les-kits-4.md | 560 | création et utilisation des kits d'articles dans les devis | devis | gestion_stock, tarification | oui | oui | oui | non | non | procedure |
| 116 | knowsystem/gerer-les-listes-de-prix-150.md | 296 | activation et configuration des listes de prix | devis | tarification | oui | non | oui | oui | non | reference_configuration |
| 117 | knowsystem/gerer-les-opportunites-perdues-121.md | 200 | gestion des motifs et du suivi des opportunités perdues | demande | crm | oui | oui | non | oui | non | procedure |
| 118 | knowsystem/gerer-les-periodes-comptables-170.md | 445 | création et génération des périodes comptables | facturation | comptabilite | oui | non | oui | non | non | reference_configuration |
| 119 | knowsystem/gerer-les-primes-energetiques-148.md | 450 | gestion des primes énergétiques (CEE, Rénov) dans les devis et factures | devis | comptabilite, tarification | oui | non | oui | oui | non | reference_configuration |
| 120 | knowsystem/gerer-les-rdv-reguliers-194.md | 254 | planification et annulation de rendez-vous réguliers/récurrents | chantier-intervention | planning, automatisation | oui | non | oui | oui | oui | procedure |

| 121 | knowsystem/gerer-les-retours-et-les-reliquats-179.md | 303 | gestion des retours fournisseurs et reliquats de réception | achat | gestion_stock | oui | non | oui | oui | non | procedure |
| 122 | knowsystem/gerer-mon-parc-installe-72.md | 479 | création et gestion du parc installé (équipements chez le client) | chantier-intervention | geolocalisation, planning | oui | oui | oui | non | non | reference_configuration |
| 123 | knowsystem/gestion-avancee-des-contacts-109.md | 590 | gestion avancée des fiches contact (adresses, notes, comptabilité, marketing, géolocalisation) | indetermine | geolocalisation, comptabilite, marketing_et_communication | non | oui | oui | non | non | reference_configuration |
| 124 | knowsystem/gestion-des-doublons-8.md | 230 | détection et fusion des doublons de contacts | indetermine | — | oui | non | non | non | non | procedure |
| 125 | knowsystem/gestion-des-parrainages-254.md | 271 | configuration et gestion des parrainages clients (récompenses) | demande | crm, marketing_et_communication | oui | oui | non | oui | non | reference_configuration |
| 126 | knowsystem/gestion-des-taches-69.md | 359 | création et catégorisation des tâches d'intervention | chantier-intervention | planning, facturation | oui | oui | non | non | non | reference_configuration |
| 127 | knowsystem/gestion-electronique-des-documents-ged-301.md | 351 | organisation et gestion documentaire (GED) des documents clients | indetermine | — | oui | non | non | oui | non | reference_configuration |
| 128 | knowsystem/grouper-les-resultats-et-creer-des-favoris-105.md | 187 | regroupement des résultats de recherche et création de favoris | indetermine | — | oui | non | non | non | non | reference_configuration |
| 129 | knowsystem/immobilisations-223.md | 489 | création et hiérarchisation des immobilisations comptables | indetermine | comptabilite | oui | oui | oui | non | non | reference_configuration |
| 130 | knowsystem/importer-des-articles-ou-des-kits-160.md | 1224 | import et mise à jour en masse d'articles et de kits via fichier Excel | devis | tarification, automatisation, gestion_stock | oui | oui | oui | oui | non | procedure |
| 131 | knowsystem/impression-des-totaux-dans-les-factures-183.md | 165 | configuration de l'impression des primes dans le sous-total des factures | facturation | comptabilite, tarification | oui | non | oui | non | non | reference_configuration |
| 132 | knowsystem/impression-du-planning-82.md | 131 | impression du planning d'intervention au format PDF | chantier-intervention | planning | oui | non | non | oui | non | procedure |
| 133 | knowsystem/imprimer-ma-facture-140.md | 364 | impression de factures/devis/commandes en PDF et gestion des acomptes à l'impression | facturation | comptabilite | oui | oui | oui | oui | non | procedure |
| 134 | knowsystem/introduction-au-crm-118.md | 598 | présentation générale du module CRM (tableau de bord, pipeline, étapes) | demande | crm, marketing_et_communication | non | oui | oui | oui | non | definitionnel |
| 135 | knowsystem/introduction-aux-achats-sur-openfire-58.md | 141 | présentation générale du processus d'achat (du bon de livraison à la commande fournisseur) | achat | gestion_stock | non | oui | non | non | non | definitionnel |

| 136 | knowsystem/introduction-aux-sms-236.md | 558 | présentation du service SMS OVH et de son fonctionnement technique | indetermine | marketing_et_communication, automatisation | non | non | oui | oui | non | definitionnel |
| 137 | knowsystem/j-ai-perdu-mes-identifiants-de-connexion-199.md | 140 | récupération des identifiants de connexion perdus | indetermine | — | oui | non | non | non | oui | faq_depannage |
| 138 | knowsystem/j-ai-un-message-d-erreur-a-la-validation-de-mes-factures-313.md | 151 | résolution de l'erreur de séquençage chronologique à la validation d'une facture | facturation | comptabilite | oui | non | oui | non | oui | faq_depannage |
| 139 | knowsystem/je-n-arrive-pas-a-me-connecter-200.md | 82 | dépannage de connexion (URL, identifiants incorrects) | indetermine | — | oui | oui | non | non | oui | faq_depannage |
| 140 | knowsystem/je-n-arrive-pas-a-me-connecter-a-l-application-mobile-314.md | 117 | dépannage de connexion à l'application mobile | indetermine | mobile | oui | non | non | non | oui | faq_depannage |
| 141 | knowsystem/journaux-comptables-205.md | 762 | création et configuration des journaux comptables | facturation | comptabilite | oui | oui | oui | non | non | reference_configuration |
| 142 | knowsystem/l-application-discussion-158.md | 486 | utilisation de la messagerie interne (canaux, messages directs, favoris, notifications) | indetermine | automatisation | oui | non | non | non | non | reference_configuration |
| 143 | knowsystem/la-navigation-83.md | 185 | présentation de la navigation générale (applications, menus, fil d'Ariane) | indetermine | — | non | non | non | non | non | definitionnel |
| 144 | knowsystem/la-recherche-avancee-104.md | 226 | utilisation des opérateurs de recherche avancée (ET/OU, caractères spéciaux) | indetermine | — | oui | non | non | non | non | reference_configuration |
| 145 | knowsystem/la-recherche-simple-18.md | 160 | utilisation de la recherche simple | indetermine | — | oui | non | non | non | non | reference_configuration |
| 146 | knowsystem/le-tunnel-de-conversion-149.md | 341 | analyse des tunnels de conversion commerciale (Quali, Quanti, objectifs) | demande | crm, reporting | non | non | oui | oui | non | reference_configuration |
| 147 | knowsystem/les-modeles-de-devis-2.md | 328 | création et utilisation des modèles de devis | devis | tarification | oui | non | oui | non | non | procedure |
| 148 | knowsystem/les-vues-84.md | 393 | présentation des différents modes d'affichage (liste, kanban, carte, pivot) | indetermine | reporting, geolocalisation | non | oui | non | non | non | definitionnel |
| 149 | knowsystem/lettrage-comptable-192.md | 981 | lettrage comptable des factures et paiements (à la facturation, en comptabilité, depuis les écritures) | facturation | comptabilite, paiement | oui | oui | oui | non | oui | procedure |
| 150 | knowsystem/liste-de-diffusion-229.md | 431 | création et alimentation des listes de diffusion (manuelle, import, formulaire web) | demande | marketing_et_communication, automatisation | oui | non | oui | non | non | procedure |

| 151 | knowsystem/livrer-et-facturer-a-plusieurs-adresses-219.md | 112 | gestion de plusieurs adresses de livraison/facturation par contact | indetermine | — | oui | non | non | non | non | reference_configuration |
| 152 | knowsystem/mails-en-erreurs-sur-gmail-smtp-535-282.md | 296 | résolution de l'erreur SMTP 535 Gmail (mot de passe d'application) | indetermine | automatisation | oui | non | oui | non | oui | faq_depannage |
| 153 | knowsystem/menu-de-la-comptabilite-et-tableau-de-bord-174.md | 1518 | présentation des menus comptables et du tableau de bord (ventes, achats, caisse, banque, à-nouveaux) | facturation | comptabilite, paiement | oui | oui | oui | non | non | reference_configuration |
| 154 | knowsystem/mettre-a-jour-un-article-centralise-168.md | 430 | mise à jour et archivage des articles depuis une base tarifaire centralisée fournisseur | devis | tarification | oui | non | oui | oui | non | procedure |
| 155 | knowsystem/migration-des-sav-291.md | 258 | migration des anciens SAV vers les demandes d'intervention | chantier-intervention | — | oui | non | non | non | non | procedure |
| 156 | knowsystem/mise-en-place-de-la-signature-electronique-261.md | 563 | mise en place et utilisation de la signature électronique (Yousign) sur les devis | devis | integrations, automatisation | oui | non | oui | oui | non | procedure |
| 157 | knowsystem/modele-de-courriers-182.md | 331 | création et paramétrage de modèles de courriers PDF (impression, remplissage automatique) | indetermine | automatisation | oui | non | non | oui | non | reference_configuration |
| 158 | knowsystem/modeles-de-commentaire-186.md | 228 | création et mise en forme des modèles de commentaires de devis | devis | — | oui | non | non | non | non | reference_configuration |
| 159 | knowsystem/modeles-dintervention-73.md | 690 | configuration des modèles d'intervention (facturation, questionnaire, rapport) | chantier-intervention | planning, facturation, mobile | oui | oui | oui | non | non | reference_configuration |
| 160 | knowsystem/modes-de-paiements-283.md | 407 | paramétrage des modes de paiement (journal, compte bancaire, affichage) | facturation | comptabilite, paiement | oui | oui | non | non | non | reference_configuration |
| 161 | knowsystem/modifier-un-contrat-312.md | 346 | modification d'un contrat et gestion des avenants | chantier-intervention | facturation, planning | oui | oui | oui | non | non | procedure |
| 162 | knowsystem/mouvement-de-stocks-248.md | 431 | fonctionnement et suivi des mouvements de stock (double entrée) | achat | gestion_stock | non | oui | non | non | non | definitionnel |
| 163 | knowsystem/navigation-et-notifications-222.md | 577 | navigation dans l'application mobile (vues jour/planning/contacts) et notifications | chantier-intervention | mobile, geolocalisation, planning | oui | oui | oui | oui | non | reference_configuration |
| 164 | knowsystem/notion-de-modele-domaine-et-operateur-288.md | 1272 | utilisation avancée des modèles, domaines et opérateurs Python pour personnaliser les Widgets | indetermine | reporting, personnalisation | oui | non | oui | oui | non | reference_configuration |
| 165 | knowsystem/optimisation-des-rdv-89.md | 313 | optimisation de la planification des rendez-vous (recherche de créneau) | chantier-intervention | planning, geolocalisation | oui | oui | non | non | non | procedure |

| 166 | knowsystem/optimisation-des-tournees-285.md | 529 | création et optimisation des tournées d'intervention | chantier-intervention | planning, geolocalisation, automatisation | oui | non | oui | non | non | procedure |
| 167 | knowsystem/ordre-d-approvisionnement-253.md | 607 | création et gestion des ordres d'approvisionnement (automatique, manuel) | achat | gestion_stock, automatisation | oui | oui | oui | non | non | reference_configuration |
| 168 | knowsystem/parametrage-des-civilites-113.md | 181 | gestion des civilités et de leur affichage sur devis/factures | indetermine | — | oui | oui | non | oui | non | reference_configuration |
| 169 | knowsystem/parametrer-l-impression-du-devis-129.md | 587 | paramétrage de l'impression du devis (structure, images, titres, modèles) | devis | personnalisation | oui | non | non | non | non | reference_configuration |
| 170 | knowsystem/parametrer-les-campagnes-les-canaux-et-les-origines-197.md | 215 | configuration des campagnes, canaux et origines marketing | demande | marketing_et_communication, crm | oui | non | non | non | non | reference_configuration |
| 171 | knowsystem/parametrer-les-etapes-119.md | 342 | création et gestion des étapes du pipeline commercial | demande | crm, automatisation | oui | non | oui | oui | non | reference_configuration |
| 172 | knowsystem/parametrer-les-projets-195.md | 238 | configuration des modèles de projets et attributs pour les opportunités | demande | crm | oui | oui | oui | non | non | reference_configuration |
| 173 | knowsystem/parametrer-les-sections-175.md | 312 | configuration des sections de devis (classiques et avancées) | devis | personnalisation | oui | oui | non | non | non | reference_configuration |
| 174 | knowsystem/parametrer-un-serveur-mail-151.md | 587 | configuration d'un serveur mail sortant et dépannage des erreurs SMTP | indetermine | automatisation | oui | non | oui | oui | oui | reference_configuration |
| 175 | knowsystem/parametrer-une-marque-5.md | 626 | création et configuration d'une marque (conditions d'achat/vente, règles de gestion) | devis | tarification | oui | oui | oui | non | non | reference_configuration |
| 176 | knowsystem/parametrer-une-norme-165.md | 197 | création et affichage des normes techniques sur les documents | devis | tarification | oui | non | non | oui | non | reference_configuration |
| 177 | knowsystem/personnalisation-du-planning-117.md | 182 | personnalisation de l'affichage du planning (filtres, couleurs, créneaux) | chantier-intervention | planning, personnalisation | oui | oui | non | non | non | reference_configuration |
| 178 | knowsystem/personnaliser-votre-compte-utilisateur-97.md | 307 | personnalisation du compte utilisateur (mot de passe, fuseau horaire, notifications, page d'accueil) | indetermine | — | oui | non | oui | oui | non | reference_configuration |
| 179 | knowsystem/plan-comptable-279.md | 902 | création et structuration du plan comptable (comptes, types, multisociété) | facturation | comptabilite | oui | oui | oui | non | non | reference_configuration |
| 180 | knowsystem/planification-directe-86.md | 577 | planification directe d'un rendez-vous d'intervention depuis le planning | chantier-intervention | planning, facturation | oui | oui | oui | non | non | procedure |

| 181 | knowsystem/planifier-et-suivre-une-activite-190.md | 426 | planification et suivi des activités de relance liées aux opportunités | demande | crm, planning | oui | oui | non | non | non | procedure |
| 182 | knowsystem/politique-de-facturation-141.md | 434 | configuration de la politique de facturation (quantités commandées vs livrées) | facturation | comptabilite | oui | non | oui | non | non | reference_configuration |
| 183 | knowsystem/position-fiscale-143.md | 390 | configuration des positions fiscales (taxes automatiques par contact/pays) | devis | tarification, comptabilite | oui | oui | oui | oui | non | reference_configuration |
| 184 | knowsystem/pourquoi-le-pdf-que-j-imprime-n-est-pas-a-jour-207.md | 110 | dépannage de l'impression PDF obsolète (pièce jointe figée) | indetermine | — | oui | non | non | non | oui | faq_depannage |
| 185 | knowsystem/prise-de-rdv-en-ligne-264.md | 309 | prise de rendez-vous en ligne par le client (équipement, créneau, contrat) | chantier-intervention | planning, geolocalisation | non | non | oui | non | non | reference_configuration |
| 186 | knowsystem/quels-documents-fournir-a-votre-comptable-212.md | 569 | export des documents comptables pour le comptable (factures, FEC, écritures) | facturation | comptabilite | oui | non | oui | non | non | procedure |
| 187 | knowsystem/questionnaires-74.md | 457 | création et configuration des questionnaires et questions d'intervention | chantier-intervention | mobile, planning | oui | oui | oui | non | non | reference_configuration |
| 188 | knowsystem/rapport-comptable-fec-213.md | 677 | extraction du fichier des écritures comptables (FEC) et verrouillage des périodes | facturation | comptabilite | oui | non | oui | non | non | procedure |
| 189 | knowsystem/rapport-des-ventes-142.md | 271 | analyse des ventes et devis via tableau croisé dynamique | demande | reporting | oui | non | non | oui | non | reference_configuration |
| 190 | knowsystem/rapport-et-suivi-d-envoi-232.md | 241 | suivi et reporting des campagnes de publipostage | demande | marketing_et_communication, reporting | non | non | non | non | non | reference_configuration |
| 191 | knowsystem/rapports-de-gestion-tva-sur-encaissement-56.md | 354 | génération des rapports de gestion (encours, échéancier fournisseurs, TVA sur encaissement) | facturation | comptabilite, reporting | oui | non | non | oui | non | reference_configuration |
| 192 | knowsystem/realiser-une-intervention-300.md | 824 | réalisation d'une intervention depuis l'application mobile (parc installé, photos, questionnaire, facturation, paiement, livraison, signature) | chantier-intervention | mobile, paiement, facturation | oui | oui | oui | oui | non | procedure |
| 193 | knowsystem/receptionner-mes-articles-178.md | 259 | réception des articles (bon de réception total ou partiel) | achat | gestion_stock | oui | oui | oui | non | non | procedure |
| 194 | knowsystem/regles-d-approvisionnement-249.md | 971 | configuration des règles d'approvisionnement (achat, flux poussés/tirés, quantités min/max) | achat | gestion_stock, automatisation | oui | oui | oui | oui | non | reference_configuration |
| 195 | knowsystem/relancer-mes-factures-139.md | 253 | relance des factures impayées (individuelle ou groupée) | facturation | automatisation, paiement | oui | oui | oui | oui | non | procedure |

| 196 | knowsystem/relations-273.md | 385 | configuration et gestion des relations entre contacts | indetermine | — | oui | oui | oui | oui | non | reference_configuration |
| 197 | knowsystem/remise-en-banque-304.md | 384 | création et gestion des remises en banque (regroupement de paiements) | facturation | comptabilite, paiement | oui | oui | non | non | oui | procedure |
| 198 | knowsystem/routes-226.md | 509 | configuration des routes logistiques (itinéraires des articles, règles de flux) | achat | gestion_stock, automatisation | oui | oui | non | oui | non | reference_configuration |
| 199 | knowsystem/saisir-un-inventaire-57.md | 912 | saisie et validation d'un inventaire physique (ajustement de stock) | achat | gestion_stock | oui | oui | oui | oui | non | procedure |
| 200 | knowsystem/secteurs-70.md | 386 | configuration des secteurs géographiques pour la planification des tournées | chantier-intervention | planning, geolocalisation | oui | oui | oui | non | non | reference_configuration |
| 201 | knowsystem/sequences-des-journaux-278.md | 562 | configuration des séquences de numérotation des journaux comptables | facturation | comptabilite | oui | non | oui | non | non | reference_configuration |
| 202 | knowsystem/synchronisation-google-agenda-269.md | 595 | configuration de la synchronisation Google Agenda (API Google, identifiants OAuth) | chantier-intervention | planning, integrations | oui | non | non | oui | non | procedure |
| 203 | knowsystem/taxes-193.md | 840 | configuration des taxes (TVA, intracommunautaire, autoliquidation sous-traitance BTP) | facturation | comptabilite | oui | oui | oui | oui | non | reference_configuration |
| 204 | knowsystem/telechargement-et-connexion-93.md | 225 | installation, connexion et mise à jour de l'application mobile | indetermine | mobile | oui | non | oui | non | non | procedure |
| 205 | knowsystem/terminer-une-intervention-95.md | 502 | clôture d'une intervention (saisie des temps, compte-rendu, statut) | chantier-intervention | mobile, planning | oui | oui | oui | non | non | procedure |
| 206 | knowsystem/tracabilite-251.md | 433 | gestion de la traçabilité des articles (numéros de série, lots) | achat | gestion_stock | oui | non | non | oui | non | reference_configuration |
| 207 | knowsystem/transferts-internes-246.md | 162 | réalisation et suivi des transferts internes de stock entre entrepôts | achat | gestion_stock | oui | oui | non | non | non | procedure |
| 208 | knowsystem/utiliser-les-pistes-127.md | 320 | activation et utilisation des pistes commerciales avant conversion en opportunités | demande | crm | oui | oui | non | non | non | procedure |
| 209 | knowsystem/valoriser-les-stocks-191.md | 691 | valorisation des stocks (méthodes de coût, inventaire à la date) | achat | gestion_stock, comptabilite | oui | non | oui | oui | non | reference_configuration |
| 210 | knowsystem/webinaire-inventaire-235.md | 181 | page de renvoi vers un webinaire enregistré sur la gestion d'inventaire | indetermine | — | non | non | non | non | non | autre (stub webinaire) |
| 211 | knowsystem/webinaire-mobile-244.md | 73 | page de renvoi vers un webinaire enregistré sur l'application mobile et les RDV | indetermine | — | non | non | non | non | non | autre (stub webinaire) |
| 212 | knowsystem/webinaire-signature-electronique-263.md | 58 | page de renvoi vers un webinaire enregistré sur la signature électronique | indetermine | — | non | non | non | non | non | autre (stub webinaire) |

CHECKPOINT openfire_odoo : 212/212 traités

## Contrôles mécaniques de complétude

- Périmètre gelé : 212. Lignes produites : 212. Numérotation continue de 1
  à 212, sans trou ni doublon (`awk` sur le champ `#`).
- 0 doublon de `chemin_relatif` (`awk` sur le champ 3, `sort | uniq -d`).
- 12 colonnes par ligne : vérifié par `awk -F'|'` (`NF=14` pour chaque
  ligne de données, incluant les deux champs vides de bordure) — 0 écart.
- `longueur_mots` : calculé pour les 212 documents par la méthode
  mécanique déclarée ci-dessus, sans exception. Somme totale : **83 094**
  mots (recalculée par `awk` sur le champ 4 de la table, pas recopiée).
- Vocabulaire fermé `moment_parcours` : les 212 valeurs appartiennent
  strictement à `{indetermine, demande, devis, achat,
  chantier-intervention, facturation}` — vérifié par inspection des
  valeurs distinctes produites par `awk`.
- Vocabulaire des 5 champs `contenu_observable` (`procedure,
  transition_objet, regle_ou_condition, contrainte_ou_limite,
  exception_ou_correction`) : strictement `{oui, non}` sur les 212 lignes,
  chaque paire (oui, non) sommant à 212.

## Agrégats descriptifs (recalculés depuis la table, non recopiés)

**`moment_parcours`** (212) : indetermine 77 · facturation 42 ·
chantier-intervention 27 · devis 23 · achat 23 · demande 20.

**`genre_documentaire`** (racine, 212) : procedure 85 ·
reference_configuration 80 · autre 29 · definitionnel 9 · faq_depannage 7 ·
politique_legale 1 · marketing_dans_aide 1.

**`contenu_observable`** (oui / non, sur 212) :
- `procedure` : oui 167 · non 45
- `transition_objet` : oui 94 · non 118
- `regle_ou_condition` : oui 106 · non 106
- `contrainte_ou_limite` : oui 82 · non 130
- `exception_ou_correction` : oui 20 · non 192

**`capacites_transverses`** (tally des valeurs non vides, ordre
décroissant, top 10 sur les 212 lignes — vocabulaire ouvert, max 3 par
document ; recalculé après correction du 2026-09-09, cf. Incidents) :
automatisation 47 · comptabilite 35 · planning 31 · paiement 27 ·
gestion_stock 24 · crm 17 · tarification 14 · integrations 13 ·
geolocalisation 13 · marketing_et_communication 12 (+ reporting 11, mobile
11, facturation 11, catalogue 8, personnalisation 7, documents 6,
conformite_reglementaire 5, roles 3, recherche 3, communication 3,
securite_compte 1, presence_en_ligne 1, multi-societe 1).

## Cas que LIGHT représente mal

- Les pages de navigation pures (17 identifiants numériques) et les stubs
  vidéo/webinaire (3 pages) sont mécaniquement comptées comme des
  observations LIGHT au même titre que les articles procéduraux longs
  (jusqu'à 1518 mots pour `menu-de-la-comptabilite-et-tableau-de-bord-174.md`).
  Le schéma ne pondère pas par densité informationnelle — un dénombrement
  brut de lignes surestime la richesse réelle du corpus si utilisé sans
  regarder `longueur_mots` et `genre_documentaire` en parallèle.
- La duplication de contenu entre paires d'articles (primes énergétiques,
  dépannage SMTP Gmail, FEC) n'est pas un signal LIGHT en soi : rien dans
  le schéma ne détecte ou ne signale la redondance inter-documents ; elle
  n'a été repérée qu'à la lecture manuelle et journalisée ci-dessus par
  prudence, sans action corrective.
- `knowsystem.md` (page d'index agrégée) contient, en apparence, des
  extraits de plusieurs procédures réelles ; coder cette page en `autre`
  sans extraction est correct au sens du contrat (la même information est
  déjà codée intégralement à son propre chemin), mais un lecteur qui ne
  lirait que cette seule ligne LIGHT sous-estimerait le contenu réel de la
  page source.

## Limites

- Cette production ne compare pas `openfire_odoo` à `openfire_zendesk` :
  les deux corpus restent des observations LIGHT strictement séparées,
  conformément à la note de `corpus_index.json`.
- Les agrégats ci-dessus décrivent la distribution des 212 lignes
  produites dans cette session ; ils ne doivent pas être comparés aux
  agrégats historiques (pilote, Costructor, Axonaut, ProGBat) sans
  recalcul commun — cf. SCHEMA-LIGHT.md §11, Compatibilité historique.
- Aucune inférence d'absence produit n'est faite à partir du silence
  documentaire de ce corpus (SCHEMA-LIGHT.md, principe explicite).
- Ce fichier ne contient aucune synthèse SUPORDO ni recommandation
  produit : c'est une production LIGHT brute, à charge pour une analyse
  ultérieure (hors du périmètre de cette mission) d'en tirer des
  conclusions.
