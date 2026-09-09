# LIGHT — production InterFast (corpus aide)

Production sous SCHEMA-LIGHT.md (contrat canonique), lu intégralement avant
ce run. Discipline : un document à la fois, lu intégralement, sortie écrite
immédiatement, aucune correction rétroactive sauf erreur mécanique démontrée
et journalisée. Run de production, pas un test méthodologique de LIGHT.

## Périmètre — vérification mécanique et gel

- `inter-fast_help` (`corpus_index.json`) : **221** documents (`type: aide`,
  9 rubriques éditoriales). `index.md`/`erreurs.md` (racine) et
  `site_marketing/` exclus du comptage canonique par construction du
  générateur (notes du corpus). Aucune `analysis_exclusions` déclarée.
  Vérification mécanique disque : 223 fichiers `.md` hors `site_marketing/`
  − `index.md` − `erreurs.md` = 221, identique au chiffre `corpus_index.json`.
- Déjà utilisés (micro-test H3, `light-h3-validation-positifs.md`) : **4**
  — `finances/activer-la-validation-des-commandes-fournisseurs.md`,
  `operations/creer-un-chantier-app-web.md`,
  `equipe/inviter-et-gerer-un-profil-sous-traitant.md`,
  `operations/consulter-et-utiliser-le-fil-d-activite-du-chantier.md`.
  `pilote-light-corpus-inedit.md` ne contient aucun document InterFast codé
  (déclaration explicite du fichier : « aucun Vertuoza/InterFast »).
- **Inédits à traiter, périmètre gelé : 217.**

Vérification mécanique : 221 (canonique) = 217 (inédits) + 4 (déjà LIGHT),
union exacte, 0 doublon, 0 chemin manquant. Garde-fou de mission (221 − 4 =
217) recalculé, écart nul.

Coût de relecture explicite (SCHEMA-LIGHT.md §5) : InterFast a été
largement mentionné en prose par d'autres instruments avant ce run —
Pilote A (`audit-pilote-A.md`, `crash-test-utilite-pilote-A.md`),
H1_SOURCE_TEST (`h1-source-test-faq.md`) et Mini-audit B (`mini-audit-B.md`).
Seul `mini-audit-B.md` contient des chemins complets mécaniquement
extractibles (`grep -oE "inter-fast/[a-z0-9/_-]+\.md"`) : 2 —
`operations/planifier-une-intervention-a-partir-d-un-devis.md` (absent du
corpus collecté selon le fichier lui-même, non applicable au périmètre) et
`operations/guide-complet-gerer-un-chantier-dans-interfast.md` (présent,
resté dans le périmètre RESTANT, sans observation LIGHT préexistante). Ces
lectures antérieures par d'autres instruments n'excluent aucun document du
périmètre LIGHT ; au-delà de ces 2 chemins, le nombre de documents relus
par ces instruments n'est pas mécaniquement reconstructible depuis leur
prose (titres cités sans chemin).

Aucune anomalie de collecte n'est documentée pour InterFast dans
`résumé.md` (0 occurrence). Corpus le plus dense du dépôt : 217 documents
restants pour ≈2 347 Ko de texte (≈10,8 Ko/document).

Répartition des 217 inédits par rubrique éditoriale :
`finances` 47 · `outils` 36 · `mon-entreprise` 35 · `application-mobile` 28
· `operations` 25 · `debuter-avec-interfast` 20 · `equipe` 15 ·
`fluides-frigorigenes` 8 · `application-web` 3.

## Méthode `longueur_mots`

Mécanique, conforme SCHEMA-LIGHT.md §4 : `awk` isole le corps Markdown
après le second délimiteur `---` du frontmatter YAML, puis `wc -w` (méthode
identique à `light-vertuoza-help.md`). Liens et syntaxe d'image
(`![](url…)`) comptés tels quels, non retirés — méthode brute, aucun
ajustement manuel. Calculé pour les 217 documents avant lecture, valeurs
figées dans le tableau.

## Journal d'incidents

**Incidents sécurité (prompt-injection) : 0.** Les 217 documents du
corpus `inter-fast_help` ont été lus intégralement comme du contenu
concurrentiel documentaire (procédures produit, FAQ, contenu légal),
jamais comme instruction. Aucune tentative d'injection de commande, de
détournement de rôle ou d'instruction adressée à l'opérateur du run n'a
été détectée dans le texte source. Les nombreuses mentions de clés API,
webhooks, jetons d'intégration (Batiprix, Pennylane, Peppol, MCP, API
InterFast) constituent de la documentation normale destinée aux
utilisateurs InterFast configurant leurs propres comptes tiers — traitées
comme telles, non comme extraction de secret.

**Vocabulaire `capacites_transverses` : aucune valeur nouvelle.** Les 217
documents ont mobilisé exclusivement le vocabulaire de base §4 et les
valeurs étendues déjà arbitrées (`geolocalisation`, `crm`,
`personnalisation`, `multi-societe`, `reporting`, `comptabilite`,
`facturation`, `tarification`, `marketing_et_communication`). Aucun
concept nouveau n'a nécessité d'arbitrage vocabulaire pendant ce run.
2 documents (# 43, # 86) n'ont mobilisé aucune capacité transverse
identifiable (« — »).

**Occurrences `tarification` (arbitrage différé vs `catalogue`) : 17.**
Journalisées sans résolution, conformément à la mission : # 21
(`debuter-avec-interfast/etre-accompagne-pour-changer-de-logiciel.md`),
# 60 (`equipe/comprendre-les-roles-utilisateurs.md`), # 61
(`equipe/gerer-mon-equipe-et-mes-utilisateurs.md`), # 64
(`equipe/gerer-plusieurs-entreprises.md`), # 63
(`equipe/resoudre-un-ajout-d-utilisateur-par-erreur.md`), # 125
(`mon-entreprise/beneficier-du-code-promo-de-demarrage.md`), # 126
(`mon-entreprise/calculer-votre-abonnement-au-pro-rata.md`), # 131
(`mon-entreprise/connecter-batiprix-a-interfast.md`), # 148
(`mon-entreprise/parrainer-un-artisan-sur-interfast.md`), # 151
(`mon-entreprise/souscrire-a-un-abonnement.md`), # 178
(`operations/signer-un-contrat-de-maintenance.md`), # 191
(`outils/comprendre-la-fiche-d-un-produit.md`), # 193
(`outils/comprendre-le-tableau-de-la-bibliotheque.md`), # 196
(`outils/creer-et-utiliser-les-articles.md`), # 206
(`outils/importer-des-articles.md`), # 208
(`outils/mettre-a-jour-les-articles-de-votre-bibliotheque.md`), # 213
(`outils/utiliser-les-ouvrages.md`).

**Occurrences `marketing_et_communication` (arbitrage différé vs
`communication`) : 5.** Journalisées sans résolution : # 32
(`debuter-avec-interfast/boite-a-outils-telecharger-nos-modeles-et-gabarits-de-documents.md`),
# 33
(`debuter-avec-interfast/creer-votre-plaquette-de-presentation-commerciale.md`),
# 148 (`mon-entreprise/parrainer-un-artisan-sur-interfast.md`,
recouvrement avec `tarification` — programme de parrainage combinant
crédit financier et démarche commerciale), # 186
(`outils/automatiser-les-demandes-d-avis-clients.md`), # 199
(`outils/exporter-mon-fichier-clients.md`).

**Correction mécanique post-production (autocorrigée, pré-commit) :**
les 36 chemins de la rubrique `outils/` (lignes # 182–217) avaient été
écrits sans le préfixe `inter-fast/` présent partout ailleurs dans le
tableau (`outils/...` au lieu de `inter-fast/outils/...`). Détecté par le
contrôle mécanique de correspondance périmètre gelé ↔ tableau, corrigé
par substitution mécanique (`sed`) avant tout contrôle de complétude
définitif. Aucun impact sur le contenu codé (objet_principal,
moment_parcours, colonnes oui/non, genre_documentaire inchangés) : erreur
de formatage du chemin uniquement, pas de document mal identifié.

## Sorties LIGHT

| # | chemin_relatif | longueur_mots | objet_principal | moment_parcours | capacites_transverses | procedure | transition_objet | regle_ou_condition | contrainte_ou_limite | exception_ou_correction | genre_documentaire |
|---:|---|---:|---|---|---|:-:|:-:|:-:|:-:|:-:|---|
| 1 | inter-fast/application-mobile/acceder-au-support-client-app-mobile.md | 1200 | support client (accès et fonctionnement, app mobile) | indetermine | support_editeur, mobile, notifications | oui | non | oui | oui | oui | procedure (avec FAQ intégrée) |
| 2 | inter-fast/application-mobile/ajouter-une-depense-app-mobile.md | 137 | dépense (ajout via app mobile, OCR justificatifs) | indetermine | mobile, documents, automatisation | oui | oui | non | non | non | procedure |
| 3 | inter-fast/application-mobile/autoriser-le-suivi-des-deplacements-app-mobile.md | 803 | géolocalisation des salariés (suivi des déplacements, cadre légal) | chantier-intervention | geolocalisation, conformite_reglementaire, planning | oui | non | oui | oui | oui | politique_legale (avec procédure associée) |
| 4 | inter-fast/application-mobile/comprendre-la-fiche-d-intervention-app-mobile.md | 594 | fiche d'intervention (app mobile, sections et actions) | chantier-intervention | roles, documents, automatisation | oui | oui | oui | oui | oui | reference_configuration (avec FAQ intégrée) |
| 5 | inter-fast/application-mobile/consulter-mes-notifications-app-mobile.md | 1032 | notifications (app mobile, paramétrage, types, traitement) | chantier-intervention | notifications, mobile, roles | oui | oui | oui | oui | oui | procedure (avec FAQ intégrée) |
| 6 | inter-fast/application-mobile/consulter-mon-profil-app-mobile.md | 705 | profil utilisateur (app mobile, paramétrage et navigation) | indetermine | mobile, roles, multi-societe | oui | non | oui | oui | oui | procedure (avec FAQ intégrée) |
| 7 | inter-fast/application-mobile/creer-des-factures-app-mobile.md | 998 | facture (création, édition, envoi depuis app mobile) | facturation | catalogue, mobile, documents | oui | oui | oui | oui | non | procedure |
| 8 | inter-fast/application-mobile/creer-un-devis-app-mobile.md | 995 | devis (création, édition, consultation app mobile) | devis | catalogue, mobile, documents | oui | oui | non | oui | non | procedure |
| 9 | inter-fast/application-mobile/creer-une-facture-sur-l-application-mobile.md | 1064 | facture (création, envoi, facturation depuis une intervention) | facturation | mobile, roles, photos | oui | oui | oui | oui | oui | procedure (avec FAQ intégrée) |
| 10 | inter-fast/application-mobile/enregistrer-une-video-d-intervention-app-mobile.md | 804 | vidéo d'intervention (enregistrement, app mobile, abonnement Business) | chantier-intervention | photos, mobile, documents | oui | oui | oui | oui | oui | procedure (avec FAQ intégrée) |
| 11 | inter-fast/application-mobile/gerer-les-clients-app-mobile.md | 585 | clients/prospects (gestion CRM, app mobile) | indetermine | crm, mobile, geolocalisation | oui | non | non | non | non | procedure |
| 12 | inter-fast/application-mobile/gerer-les-equipements-app-mobile.md | 933 | équipements (fiches, historique, ajout, app mobile) | chantier-intervention | photos, mobile, documents | oui | non | oui | oui | oui | procedure (avec FAQ intégrée) |
| 13 | inter-fast/application-mobile/gerer-les-fournisseurs-app-mobile.md | 629 | fournisseurs (fiches, gestion CRM, app mobile) | indetermine | crm, roles, mobile | oui | non | oui | oui | non | procedure (avec FAQ intégrée) |
| 14 | inter-fast/application-mobile/gerer-vos-demandes-de-materiel-app-mobile.md | 583 | demande de matériel (création et suivi depuis une intervention, app mobile) | chantier-intervention | gestion_stock, mobile, catalogue | oui | oui | oui | oui | oui | procedure (avec FAQ intégrée) |
| 15 | inter-fast/application-mobile/planifier-un-evenement-app-mobile.md | 806 | évènement (intervention ou rendez-vous, planification app mobile) | chantier-intervention | planning, geolocalisation, mobile | oui | oui | oui | non | non | procedure |
| 16 | inter-fast/application-mobile/receptionner-une-commande-app-mobile.md | 524 | commande (réception marchandises, app mobile) | achat | gestion_stock, mobile, photos | oui | oui | non | oui | non | procedure |
| 17 | inter-fast/application-mobile/remplir-ses-feuilles-de-temps-app-mobile.md | 1350 | feuille de temps (déclaration heures et astreintes, app mobile) | chantier-intervention | validation, roles, mobile | oui | oui | oui | oui | oui | procedure (avec FAQ intégrée) |
| 18 | inter-fast/application-mobile/remplir-un-rapport-d-intervention-app-mobile.md | 1052 | rapport d'intervention (remplissage, signature, génération, app mobile) | chantier-intervention | validation, mobile, photos | oui | oui | oui | oui | oui | procedure |
| 19 | inter-fast/application-mobile/scanner-les-qr-codes-app-mobile.md | 578 | QR codes (association et scan d'actifs physiques, app mobile) | indetermine | gestion_stock, mobile, recherche | oui | oui | oui | oui | non | procedure |
| 20 | inter-fast/application-mobile/suivre-l-historique-des-interventions.md | 1092 | historique des interventions (accès selon rôle utilisateur) | chantier-intervention | roles, permissions, crm | oui | non | oui | oui | oui | reference_configuration (avec FAQ intégrée) |
| 21 | inter-fast/application-mobile/suivre-les-stocks-app-mobile.md | 982 | stocks (consultation, mouvements, app mobile) | chantier-intervention | gestion_stock, mobile, automatisation | oui | oui | oui | oui | oui | procedure (avec FAQ intégrée) |
| 22 | inter-fast/application-mobile/suivre-ses-chantiers-app-mobile.md | 1119 | chantier (fiche de synthèse, suivi, app mobile) | chantier-intervention | roles, communication, offline | oui | non | oui | oui | non | procedure (avec FAQ intégrée) |
| 23 | inter-fast/application-mobile/suivre-ses-taches-app-mobile.md | 389 | tâches (création, suivi, app mobile) | indetermine | notifications, mobile, planning | oui | non | non | non | non | procedure |
| 24 | inter-fast/application-mobile/telecharger-l-application-de-gestion.md | 360 | application de gestion (installation PWA, iOS/Android) | indetermine | mobile | oui | non | non | non | non | procedure |
| 25 | inter-fast/application-mobile/telecharger-l-application-terrain.md | 574 | application terrain (installation, connexion, mode hors-ligne) | chantier-intervention | offline, mobile, roles | oui | non | oui | oui | oui | procedure (avec FAQ intégrée) |
| 26 | inter-fast/application-mobile/utiliser-l-application-mobile-sans-reseau-mode-hors-ligne.md | 339 | mode hors ligne (rapport d'intervention sans réseau) | chantier-intervention | offline, mobile, photos | oui | non | oui | oui | non | procedure (avec FAQ intégrée) |
| 27 | inter-fast/application-mobile/utiliser-le-click-to-call-pour-appeler-depuis-le-crm.md | 329 | click-to-call (appel depuis le CRM, intégrations téléphonie VoIP) | indetermine | integrations, crm, mobile | oui | non | oui | non | non | procedure |
| 28 | inter-fast/application-mobile/utiliser-notre-application-mobile.md | 1985 | application mobile (vue d'ensemble, fonctionnalités et workflow terrain) | chantier-intervention | roles, permissions, offline | oui | oui | oui | oui | oui | procedure (avec FAQ intégrée) |
| 29 | inter-fast/application-web/collaborer-avec-les-commentaires.md | 1110 | commentaires (collaboration interne/externe, mentions) | chantier-intervention | communication, notifications, roles | oui | non | oui | oui | oui | procedure (avec FAQ intégrée) |
| 30 | inter-fast/application-web/exporter-toutes-mes-donnees.md | 1126 | export complet des données (procédure sécurisée, structure CSV) | indetermine | securite_compte, roles, documents | oui | non | oui | oui | oui | procedure (avec FAQ intégrée) |
| 31 | inter-fast/application-web/installer-l-extension-chrome.md | 1828 | extension Chrome (import d'articles depuis sites fournisseurs) | devis | integrations, catalogue, automatisation | oui | oui | oui | oui | oui | procedure (avec FAQ intégrée) |
| 32 | inter-fast/debuter-avec-interfast/boite-a-outils-telecharger-nos-modeles-et-gabarits-de-documents.md | 645 | modèles et gabarits (documents légaux, imports, présentation commerciale) | indetermine | documents, conformite_reglementaire, marketing_et_communication | oui | non | oui | oui | oui | procedure (avec FAQ intégrée) |
| 33 | inter-fast/debuter-avec-interfast/checklist-de-demarrage.md | 930 | checklist de démarrage (onboarding complet InterFast) | indetermine | integrations, automatisation, roles | oui | non | non | non | non | reference_configuration |
| 34 | inter-fast/debuter-avec-interfast/comment-enregistrer-et-retrouver-vos-pages-favorites-dans-interfast.md | 909 | pages favorites (vues personnalisées, filtres enregistrés) | indetermine | personnalisation, recherche, reporting | oui | non | non | oui | non | procedure |
| 35 | inter-fast/debuter-avec-interfast/comment-joindre-le-support-par-telephone.md | 934 | support téléphonique (canaux d'assistance, agents IA) | indetermine | support_editeur, automatisation, communication | oui | oui | oui | oui | non | procedure (avec FAQ intégrée) |
| 36 | inter-fast/debuter-avec-interfast/comment-utiliser-max-l-ia-dans-le-tchat.md | 1250 | assistant IA « Max » (support tchat, workflow, prompts) | indetermine | support_editeur, automatisation, communication | oui | oui | oui | oui | oui | procedure (avec FAQ intégrée) |
| 37 | inter-fast/debuter-avec-interfast/comprendre-la-structure-d-interfast.md | 1529 | structure des données (objets et relations InterFast) | indetermine | multi-societe, gestion_stock, automatisation | oui | non | oui | oui | oui | reference_configuration (avec FAQ intégrée) |
| 38 | inter-fast/debuter-avec-interfast/construire-le-cerveau-numerique-de-votre-entreprise.md | 4613 | « cerveau numérique » (argumentaire centralisation des données, témoignages clients) | indetermine | integrations, automatisation, crm | non | non | oui | oui | non | marketing_dans_aide (avec référence objets et FAQ) |
| 39 | inter-fast/debuter-avec-interfast/contacter-l-equipe-care.md | 790 | support client (philosophie, canaux, académie vidéo) | indetermine | support_editeur, recherche, communication | oui | non | oui | oui | non | procedure |
| 40 | inter-fast/debuter-avec-interfast/creer-votre-plaquette-de-presentation-commerciale.md | 882 | plaquette de présentation commerciale (création accompagnée, intégration aux devis) | devis | marketing_et_communication, documents, support_editeur | oui | non | oui | oui | non | procedure (avec FAQ intégrée) |
| 41 | inter-fast/debuter-avec-interfast/debuter-votre-accompagnement-30-jours.md | 1002 | accompagnement 30 jours (sessions live d'onboarding) | indetermine | support_editeur, communication, planning | oui | non | oui | oui | non | procedure (avec FAQ intégrée) |
| 42 | inter-fast/debuter-avec-interfast/decouvrir-l-application-web-et-mobile-pour-les-smartphones.md | 291 | applications (web, PWA, terrain — installation par plateforme) | indetermine | mobile, roles | oui | non | oui | non | non | procedure |
| 43 | inter-fast/debuter-avec-interfast/decouvrir-les-petites-astuces-interfast.md | 111 | astuces navigateur et outils tiers (recommandations) | indetermine | — | non | non | non | non | non | autre |
| 44 | inter-fast/debuter-avec-interfast/enregistrer-votre-ecran-avec-l-outil-loom.md | 733 | enregistrement d'écran (outil tiers Loom, pour le support) | indetermine | support_editeur, mobile | oui | non | non | non | non | procedure (avec FAQ intégrée) |
| 45 | inter-fast/debuter-avec-interfast/etre-accompagne-pour-changer-de-logiciel.md | 631 | migration de données (accompagnement gratuit/payant, changement de logiciel) | indetermine | documents, integrations, tarification | oui | non | oui | oui | non | procedure |
| 46 | inter-fast/debuter-avec-interfast/formation-complete-a-l-application-web-d-interfast.md | 585 | formation complète application web (index de tutoriels) | indetermine | integrations, gestion_stock, conformite_reglementaire | non | non | non | non | non | reference_configuration |
| 47 | inter-fast/debuter-avec-interfast/le-dictionnaire-des-fonctionnalites-d-interfast.md | 1738 | dictionnaire des fonctionnalités (glossaire, définitions métier) | indetermine | integrations, conformite_reglementaire, facturation | non | non | oui | oui | non | definitionnel (avec FAQ intégrée) |
| 48 | inter-fast/debuter-avec-interfast/maitrisez-interfast-grace-a-l-academie-video.md | 387 | académie vidéo (accès et navigation, formation) | indetermine | support_editeur, mobile, roles | oui | non | non | non | non | procedure |
| 49 | inter-fast/debuter-avec-interfast/sortir-du-mode-test.md | 657 | mode test (sortie, gestion des données de démarrage) | indetermine | conformite_reglementaire, documents, validation | oui | oui | oui | oui | oui | procedure (avec FAQ intégrée) |
| 50 | inter-fast/debuter-avec-interfast/trouver-les-reponses-a-mes-questions.md | 588 | centre d'aide (canaux : académie, aide en ligne, support, actualités) | indetermine | support_editeur, recherche, automatisation | non | non | non | oui | non | definitionnel (avec FAQ intégrée) |
| 51 | inter-fast/debuter-avec-interfast/visionner-les-replays-de-formation-hebdo.md | 688 | replays de formation hebdomadaire (archives thématiques) | indetermine | support_editeur, mobile, recherche | non | non | non | oui | non | reference_configuration (avec FAQ intégrée) |
| 52 | inter-fast/equipe/aider-un-collaborateur-a-se-connecter.md | 1120 | connexion collaborateur (activation, dépannage, réinitialisation) | indetermine | securite_compte, roles, mobile | oui | non | oui | oui | oui | faq_depannage (avec procédure) |
| 53 | inter-fast/equipe/comprendre-et-parametrer-la-fiche-utilisateur.md | 562 | fiche utilisateur (droits, coûts, documents, historique) | indetermine | roles, documents, geolocalisation | oui | oui | oui | oui | oui | procedure (avec FAQ intégrée) |
| 54 | inter-fast/equipe/comprendre-les-roles-utilisateurs.md | 718 | rôles utilisateurs (matrice de droits et tarification) | indetermine | roles, permissions, tarification | non | non | oui | oui | non | reference_configuration (avec FAQ intégrée) |
| 55 | inter-fast/equipe/configurer-et-gerer-vos-agences.md | 721 | agences (multi-établissement, comptabilité analytique) | indetermine | multi-societe, reporting, comptabilite | oui | non | oui | oui | oui | procedure (avec FAQ intégrée) |
| 56 | inter-fast/equipe/connexion-a-deux-comptes-interfast.md | 101 | connexion simultanée à deux comptes (multi-entreprise, navigation privée) | indetermine | multi-societe, securite_compte | non | non | non | oui | oui | faq_depannage |
| 57 | inter-fast/equipe/gerer-mon-equipe-et-mes-utilisateurs.md | 1206 | gestion des utilisateurs (ajout, archivage, changement de statut) | indetermine | roles, permissions, tarification | oui | oui | oui | oui | oui | procedure (avec FAQ intégrée) |
| 58 | inter-fast/equipe/gerer-plusieurs-entreprises.md | 310 | multi-entreprise (basculement, création, coûts) | indetermine | multi-societe, securite_compte, tarification | oui | non | oui | oui | non | procedure |
| 59 | inter-fast/equipe/integrer-le-calendrier-interfast-dans-une-autre-application.md | 512 | calendrier iCal (partage vers Google Calendar, Outlook, Apple) | indetermine | integrations, planning, mobile | oui | non | non | non | non | procedure |
| 60 | inter-fast/equipe/integrer-un-agenda-dans-le-calendrier-interfast.md | 952 | agenda externe (import iCal dans InterFast) | indetermine | integrations, planning, securite_compte | oui | non | oui | oui | oui | procedure (avec FAQ intégrée) |
| 61 | inter-fast/equipe/inviter-mon-comptable-sur-interfast.md | 359 | comptable (invitation, rôle lecture seule) | indetermine | roles, permissions, comptabilite | oui | non | oui | oui | non | procedure |
| 62 | inter-fast/equipe/reinitialiser-mon-mot-de-passe.md | 254 | mot de passe (réinitialisation) | indetermine | securite_compte | oui | non | non | oui | non | procedure (avec FAQ intégrée) |
| 63 | inter-fast/equipe/resoudre-un-ajout-d-utilisateur-par-erreur.md | 904 | facturation prorata (erreur d'ajout d'utilisateur, conversion en crédit) | facturation | tarification, comptabilite, roles | oui | oui | oui | oui | oui | politique_legale (avec FAQ intégrée) |
| 64 | inter-fast/equipe/suivre-les-deplacements-des-techniciens-app-web.md | 1332 | suivi des déplacements techniciens (paramétrage, cadre légal, app web) | chantier-intervention | geolocalisation, conformite_reglementaire, planning | oui | non | oui | oui | oui | politique_legale (avec procédure associée) |
| 65 | inter-fast/equipe/synchroniser-mon-adresse-email.md | 1668 | synchronisation email (SMTP, délivrabilité, dépannage) | indetermine | integrations, securite_compte, documents | oui | non | oui | oui | oui | faq_depannage (avec procédure) |
| 66 | inter-fast/equipe/utiliser-les-feuilles-de-temps-app-web.md | 1321 | feuilles de temps (activation, validation, export, mode détaillé — app web) | chantier-intervention | validation, documents, personnalisation | oui | oui | oui | oui | oui | procedure (avec FAQ intégrée) |
| 67 | inter-fast/finances/ajouter-une-depense-app-web.md | 156 | dépense (ajout, app web) | achat | documents | oui | non | non | non | non | procedure |
| 68 | inter-fast/finances/comprendre-la-fiche-d-un-devis.md | 1571 | devis (fiche récapitulative, cycle de vie, statuts) | devis | documents, validation, communication | oui | oui | oui | oui | oui | procedure (avec FAQ intégrée) |
| 69 | inter-fast/finances/comprendre-la-fiche-d-une-facture.md | 1237 | facture (fiche récapitulative, cycle de vie, statuts, paiements) | facturation | documents, validation, paiement | oui | oui | oui | oui | oui | procedure (avec FAQ intégrée) |
| 70 | inter-fast/finances/comprendre-le-tableau-des-avoirs-clients.md | 547 | avoirs clients (tableau, filtres, exports) | facturation | reporting, comptabilite, personnalisation | non | non | oui | oui | oui | reference_configuration (avec FAQ intégrée) |
| 71 | inter-fast/finances/comprendre-le-tableau-des-commandes-v2.md | 327 | commandes V2 (tableau, filtres, colonnes) | achat | gestion_stock, reporting, personnalisation | non | non | non | non | non | reference_configuration |
| 72 | inter-fast/finances/comprendre-le-tableau-des-depenses.md | 608 | dépenses (tableau, filtres, exports) | achat | reporting, comptabilite, documents | non | non | oui | oui | oui | reference_configuration (avec FAQ intégrée) |
| 73 | inter-fast/finances/comprendre-le-tableau-des-devis.md | 543 | devis (tableau, filtres, colonnes) | devis | reporting, personnalisation, documents | non | non | non | non | non | reference_configuration |
| 74 | inter-fast/finances/comprendre-le-tableau-des-factures.md | 439 | factures (tableau, filtres, colonnes) | facturation | reporting, personnalisation, documents | non | non | non | non | non | reference_configuration |
| 75 | inter-fast/finances/comprendre-le-tableau-des-paiements.md | 709 | paiements (tableau, consignation partielle, export) | facturation | paiement, reporting, comptabilite | oui | oui | oui | oui | non | procedure |
| 76 | inter-fast/finances/connecter-mon-compte-bancaire.md | 1232 | compte bancaire (connexion Powens, DSP2, migration Ponto) | indetermine | integrations, securite_compte, conformite_reglementaire | oui | non | oui | oui | oui | procedure (avec FAQ intégrée) |
| 77 | inter-fast/finances/consigner-un-paiement.md | 633 | paiement (consignation, suppression, cas particuliers) | facturation | paiement, validation, comptabilite | oui | non | oui | oui | oui | procedure (avec FAQ intégrée) |
| 78 | inter-fast/finances/creer-et-gerer-des-variantes-de-devis.md | 1006 | variantes de devis (création, envoi, acceptation) | devis | catalogue, communication, validation | oui | oui | oui | oui | oui | procedure (avec FAQ intégrée) |
| 79 | inter-fast/finances/creer-et-gerer-vos-achats-avec-le-module-commandes-v1.md | 1033 | bon de commande V1 (création, suivi, statuts) | achat | documents, catalogue, communication | oui | oui | oui | oui | non | procedure |
| 80 | inter-fast/finances/creer-un-avenant-au-devis.md | 597 | avenant au devis (plus/moins-values, facturation finale) | chantier-intervention | automatisation, validation, catalogue | oui | oui | oui | oui | oui | procedure (avec FAQ intégrée) |
| 81 | inter-fast/finances/creer-un-bon-de-commande-v1.md | 229 | bon de commande V1 (création) | achat | documents, catalogue | oui | non | non | non | non | procedure |
| 82 | inter-fast/finances/creer-un-devis-app-web.md | 1586 | devis (création, structuration, cycle de vie, app web) | devis | validation, catalogue, personnalisation | oui | oui | oui | oui | non | procedure |
| 83 | inter-fast/finances/creer-une-facture-d-acompte-de-situation-de-solde.md | 2730 | facturation par étapes (acompte, situation, solde) | facturation | validation, conformite_reglementaire, automatisation | oui | oui | oui | oui | oui | procedure (avec FAQ intégrée) |
| 84 | inter-fast/finances/creer-une-facture-d-avoir-client.md | 1203 | avoir client (création, méthodes, cas particuliers) | facturation | conformite_reglementaire, validation, documents | oui | oui | oui | oui | oui | procedure (avec FAQ intégrée) |
| 85 | inter-fast/finances/creer-une-facture-proforma.md | 582 | facture proforma (création, transformation en facture officielle) | facturation | documents, validation, catalogue | oui | oui | oui | non | oui | procedure |
| 86 | inter-fast/finances/creer-une-facture-simple.md | 92 | facture simple (création sans devis) | facturation | — | oui | non | non | non | non | procedure |
| 87 | inter-fast/finances/dissocier-mon-compte-bancaire.md | 416 | compte bancaire (dissociation, révocation) | indetermine | integrations, roles, comptabilite | oui | non | oui | oui | oui | procedure (avec FAQ intégrée) |
| 88 | inter-fast/finances/enregistrer-un-avoir-fournisseur.md | 604 | avoir fournisseur (enregistrement, suivi) | achat | comptabilite, reporting, documents | oui | non | non | oui | oui | procedure (avec FAQ intégrée) |
| 89 | inter-fast/finances/exporter-mes-factures-client.md | 587 | export comptable factures (paramétrage journal des ventes, export) | facturation | comptabilite, reporting, personnalisation | oui | non | non | oui | oui | procedure (avec FAQ intégrée) |
| 90 | inter-fast/finances/exporter-ses-factures-fournisseur.md | 382 | export comptable factures fournisseurs (paramétrage journal des achats, export) | achat | comptabilite, reporting, personnalisation | oui | non | non | non | non | procedure |
| 91 | inter-fast/finances/exporter-ses-paiements.md | 963 | export des paiements (simple, comptable / journal de banque) | facturation | comptabilite, reporting, paiement | oui | non | non | oui | non | procedure (avec FAQ intégrée) |
| 92 | inter-fast/finances/facturer-une-intervention-depuis-l-application-web-et-mobile.md | 705 | facturation d'une intervention (app web/mobile) | chantier-intervention | documents, mobile, automatisation | oui | oui | oui | oui | oui | procedure (avec FAQ intégrée) |
| 93 | inter-fast/finances/gerer-les-primes-et-les-retenues-de-garantie.md | 1253 | primes et retenues de garantie (ajout, suivi de versement) | devis | paiement, validation, comptabilite | oui | oui | oui | oui | oui | procedure (avec FAQ intégrée) |
| 94 | inter-fast/finances/import-des-devis-factures-de-mon-ancien-logiciel-avec-l-ia.md | 542 | import IA de devis/factures (ancien logiciel) | indetermine | automatisation, documents, integrations | oui | non | non | oui | non | procedure |
| 95 | inter-fast/finances/importer-et-gerer-un-dpgf.md | 1918 | DPGF (import structuré, chiffrage, export retour) | devis | automatisation, catalogue, documents | oui | oui | oui | oui | oui | procedure (avec FAQ intégrée) |
| 96 | inter-fast/finances/mentionner-la-tva-a-taux-reduits.md | 597 | TVA taux réduits (mention légale automatique) | devis | conformite_reglementaire, personnalisation, documents | oui | non | oui | oui | oui | politique_legale (avec procédure associée) |
| 97 | inter-fast/finances/modifier-le-client-sur-un-devis.md | 466 | client sur devis (modification, statuts brouillon/finalisé) | devis | crm, validation | oui | non | oui | oui | oui | procedure |
| 98 | inter-fast/finances/modifier-le-client-sur-une-facture.md | 686 | client sur facture (modification, statuts brouillon/finalisé) | facturation | crm, validation, conformite_reglementaire | oui | oui | oui | oui | oui | procedure (avec FAQ intégrée) |
| 99 | inter-fast/finances/modifier-un-devis.md | 2738 | devis (édition avancée, marges, options, synthèse rentabilité) | devis | catalogue, comptabilite, reporting | oui | non | oui | oui | oui | procedure (avec FAQ intégrée) |
| 100 | inter-fast/finances/modifier-une-depense.md | 257 | dépense (modification, allocation chantier) | achat | personnalisation, comptabilite | oui | non | non | oui | oui | procedure (avec FAQ intégrée) |
| 101 | inter-fast/finances/modifier-une-facture-client.md | 1969 | facture (édition complète, liaison chantier/intervention, structure) | facturation | catalogue, documents, validation | oui | non | oui | oui | oui | procedure (avec FAQ intégrée) |
| 102 | inter-fast/finances/personnaliser-mes-factures-fournisseurs.md | 533 | factures fournisseurs (personnalisation présentation, numérotation) | achat | personnalisation, documents, conformite_reglementaire | oui | non | non | non | non | procedure |
| 103 | inter-fast/finances/planifier-une-intervention-a-partir-d-un-devis.md | 535 | intervention planifiée depuis un devis (création, liaison) | chantier-intervention | planning, validation | oui | oui | oui | oui | oui | procedure (avec FAQ intégrée) |
| 104 | inter-fast/finances/poursuivre-la-facturation-d-un-devis-importe.md | 828 | devis importé (facturation en continu, liaison acompte) | facturation | automatisation, documents, validation | oui | oui | oui | non | oui | procedure (avec FAQ intégrée) |
| 105 | inter-fast/finances/rapprocher-des-factures-client-a-une-operation-bancaire.md | 612 | rapprochement bancaire factures client (procédure, cas multi-factures) | facturation | comptabilite, roles, paiement | oui | non | oui | oui | oui | procedure (avec FAQ intégrée) |
| 106 | inter-fast/finances/rapprocher-des-factures-fournisseur-a-une-operation-bancaire.md | 857 | rapprochement bancaire factures fournisseur (suggestions automatiques, multi-factures) | achat | comptabilite, automatisation, paiement | oui | oui | oui | oui | non | procedure |
| 107 | inter-fast/finances/resoudre-les-problemes-de-synchronisation-bancaire-ponto.md | 1765 | synchronisation bancaire Ponto (dépannage, réautorisation DSP2) | indetermine | integrations, conformite_reglementaire, securite_compte | oui | non | oui | oui | oui | faq_depannage (avec procédure) |
| 108 | inter-fast/finances/resoudre-les-problemes-de-synchronisation-bancaire-powens.md | 535 | synchronisation bancaire Powens (dépannage, réautorisation DSP2) | indetermine | integrations, conformite_reglementaire, securite_compte | oui | non | oui | oui | oui | faq_depannage (avec procédure) |
| 109 | inter-fast/finances/signer-electroniquement-un-devis.md | 830 | signature électronique de devis (procédure, documents annexes) | devis | validation, securite_compte, documents | oui | oui | oui | oui | non | procedure (avec FAQ intégrée) |
| 110 | inter-fast/finances/utiliser-le-nouvel-editeur-de-devis.md | 1695 | nouvel éditeur de devis V2 (fonctionnalités, structuration) | devis | catalogue, personnalisation, integrations | oui | non | oui | oui | oui | procedure (avec FAQ intégrée) |
| 111 | inter-fast/finances/utiliser-le-nouvel-editeur-de-facture.md | 1372 | nouvel éditeur de facture V2 (fonctionnalités, structuration) | facturation | catalogue, personnalisation, integrations | oui | non | non | non | non | procedure |
| 112 | inter-fast/finances/utiliser-les-commandes-v2-app-web.md | 2015 | commandes V2 (création, réception, validation, liaison chantier) | achat | validation, gestion_stock, automatisation | oui | oui | oui | oui | oui | procedure |
| 113 | inter-fast/finances/utiliser-les-frais-masques.md | 634 | frais masqués (application, cumul, impact marge) | devis | comptabilite, catalogue | oui | non | oui | non | non | procedure |
| 114 | inter-fast/fluides-frigorigenes/comprendre-le-tableau-des-cerfas.md | 1080 | CERFA (tableau des mouvements de fluide, bilan, export) | chantier-intervention | conformite_reglementaire, gestion_stock, reporting | oui | non | oui | oui | oui | politique_legale (avec procédure associée) |
| 115 | inter-fast/fluides-frigorigenes/enregistrer-une-bouteille-de-fluide-app-mobile.md | 322 | bouteille de fluide (enregistrement, app mobile) | chantier-intervention | gestion_stock, mobile, conformite_reglementaire | oui | non | non | oui | oui | procedure (avec FAQ intégrée) |
| 116 | inter-fast/fluides-frigorigenes/guide-complet-gerer-les-bouteilles-de-fluide.md | 2536 | bouteilles de fluide (gestion complète, BSFF, Trackdéchets) | chantier-intervention | conformite_reglementaire, gestion_stock, integrations | oui | oui | oui | oui | oui | politique_legale (avec procédure associée) |
| 117 | inter-fast/fluides-frigorigenes/recenser-un-detecteur-manuel-de-fuite.md | 447 | détecteur manuel de fuite (enregistrement, pré-remplissage documents) | chantier-intervention | conformite_reglementaire, roles, automatisation | oui | non | oui | oui | oui | procedure (avec FAQ intégrée) |
| 118 | inter-fast/fluides-frigorigenes/remplir-le-cerfa-15497.md | 1130 | CERFA 15497 (remplissage, pré-requis, modification) | chantier-intervention | conformite_reglementaire, mobile, gestion_stock | oui | non | oui | oui | oui | politique_legale (avec procédure associée) |
| 119 | inter-fast/fluides-frigorigenes/remplir-un-bsff.md | 4132 | BSFF (remplissage complet, cycle de vie, Trackdéchets) | chantier-intervention | conformite_reglementaire, integrations, gestion_stock | oui | oui | oui | oui | oui | politique_legale (avec procédure associée) |
| 120 | inter-fast/fluides-frigorigenes/renseigner-mon-numero-de-capacite.md | 146 | numéro de capacité (définition, renseignement) | indetermine | conformite_reglementaire | oui | non | oui | oui | non | definitionnel (avec procédure associée) |
| 121 | inter-fast/fluides-frigorigenes/resoudre-les-erreurs-sur-un-bsff.md | 1024 | BSFF (checklist de dépannage, erreurs courantes) | chantier-intervention | conformite_reglementaire, integrations, gestion_stock | oui | non | oui | oui | oui | faq_depannage (avec procédure) |
| 122 | inter-fast/mon-entreprise/ajouter-mes-certifications-d-entreprise.md | 298 | certifications d'entreprise (ajout, affichage sur documents) | indetermine | personnalisation, documents, conformite_reglementaire | oui | non | non | oui | oui | procedure |
| 123 | inter-fast/mon-entreprise/ajouter-mes-conditions-generales-de-vente-cgv.md | 498 | CGV (paramétrage, import, rédaction) | indetermine | conformite_reglementaire, documents, personnalisation | oui | non | non | oui | oui | procedure (avec FAQ intégrée) |
| 124 | inter-fast/mon-entreprise/arreter-mon-abonnement.md | 223 | résiliation d'abonnement (demande, conditions) | facturation | facturation, support_editeur, roles | oui | non | oui | oui | oui | procedure (avec FAQ intégrée) |
| 125 | inter-fast/mon-entreprise/beneficier-du-code-promo-de-demarrage.md | 481 | code promo de démarrage (éligibilité, activation) | achat | tarification, facturation, support_editeur | oui | oui | oui | oui | oui | procedure (avec FAQ intégrée) |
| 126 | inter-fast/mon-entreprise/calculer-votre-abonnement-au-pro-rata.md | 1039 | calcul de l'abonnement au pro-rata (ajout/archivage utilisateur, changement de plan) | facturation | tarification, facturation, roles | oui | oui | oui | oui | oui | procedure (avec contenu tarifaire et promotionnel) |
| 127 | inter-fast/mon-entreprise/comprendre-l-onglet-mon-abonnement.md | 286 | onglet Mon abonnement (factures, plan, moyen de paiement) | facturation | facturation, paiement, support_editeur | oui | non | oui | non | non | reference_configuration (avec FAQ intégrée) |
| 128 | inter-fast/mon-entreprise/comprendre-la-facturation-electronique.md | 3856 | facturation électronique (réforme 2026-2027, conformité, Peppol/Pennylane) | facturation | conformite_reglementaire, integrations, comptabilite | oui | oui | oui | oui | oui | politique_legale (avec procédure associée) |
| 129 | inter-fast/mon-entreprise/configurer-des-conditions-de-paiement.md | 944 | conditions de paiement (configuration générale et par client) | indetermine | paiement, personnalisation, crm | oui | oui | oui | oui | non | procedure |
| 130 | inter-fast/mon-entreprise/configurer-la-partie-paiements-taxes.md | 1301 | paiements et taxes (RIB, conditions de paiement, TVA, acomptes devis) | indetermine | paiement, conformite_reglementaire, personnalisation | oui | oui | oui | oui | oui | procedure (avec FAQ intégrée) |
| 131 | inter-fast/mon-entreprise/connecter-batiprix-a-interfast.md | 390 | intégration Batiprix (bibliothèque d'ouvrages dans les devis) | devis | integrations, catalogue, tarification | oui | oui | oui | oui | oui | procedure (avec FAQ intégrée) |
| 132 | inter-fast/mon-entreprise/connecter-interfast-a-pennylane.md | 2957 | intégration Pennylane (facturation électronique, comptabilité, synchronisation) | facturation | integrations, comptabilite, conformite_reglementaire | oui | oui | oui | oui | oui | procedure (avec FAQ intégrée) |
| 133 | inter-fast/mon-entreprise/connecter-interfast-a-peppol.md | 1644 | intégration Peppol (envoi/réception factures électroniques, Belgique) | facturation | integrations, conformite_reglementaire, crm | oui | oui | oui | oui | oui | procedure (avec FAQ intégrée) |
| 134 | inter-fast/mon-entreprise/connecter-interfast-a-une-ia-via-mcp.md | 2022 | intégration MCP (connexion IA externe, clé API, création de devis assistée) | indetermine | integrations, automatisation, securite_compte | oui | oui | oui | oui | oui | procedure (avec contenu définitionnel et FAQ) |
| 135 | inter-fast/mon-entreprise/connecter-trackdechets-a-interfast.md | 62 | intégration Trackdéchets (traçabilité déchets dangereux) | indetermine | integrations, conformite_reglementaire | oui | non | non | non | non | procedure |
| 136 | inter-fast/mon-entreprise/construire-les-modeles-de-rapports.md | 1252 | modèles de rapports d'intervention (constructeur, personnalisation) | chantier-intervention | personnalisation, mobile, documents | oui | oui | oui | oui | oui | procedure |
| 137 | inter-fast/mon-entreprise/construire-ses-modeles-de-devis.md | 947 | modèles de devis (création, personnalisation, utilisation) | devis | personnalisation, documents, catalogue | oui | oui | oui | oui | oui | procedure (avec FAQ intégrée) |
| 138 | inter-fast/mon-entreprise/creer-un-modele-d-e-mail.md | 506 | modèles d'email (création, variables, envoi) | indetermine | communication, personnalisation, mobile | oui | oui | oui | non | non | procedure |
| 139 | inter-fast/mon-entreprise/exporter-son-journal-d-achats.md | 276 | journal d'achats (export comptable, justificatifs) | facturation | comptabilite, documents | oui | non | non | oui | non | procedure |
| 140 | inter-fast/mon-entreprise/exporter-son-journal-de-ventes.md | 291 | journal de ventes (export comptable, justificatifs) | facturation | comptabilite, documents | oui | non | oui | oui | non | procedure |
| 141 | inter-fast/mon-entreprise/mettre-a-jour-la-carte-bancaire-de-paiement.md | 478 | carte bancaire de paiement (mise à jour, échec de paiement) | facturation | paiement, roles, securite_compte | oui | non | oui | oui | oui | procedure (avec FAQ intégrée) |
| 142 | inter-fast/mon-entreprise/modifier-la-numerotation-des-depenses.md | 384 | numérotation des dépenses (format, prochain numéro) | facturation | comptabilite, conformite_reglementaire, personnalisation | oui | non | oui | oui | oui | procedure (avec FAQ intégrée) |
| 143 | inter-fast/mon-entreprise/modifier-la-numerotation-des-devis-factures.md | 233 | numérotation des devis/factures (format, prochain numéro) | facturation | conformite_reglementaire, personnalisation, comptabilite | oui | non | oui | oui | non | procedure |
| 144 | inter-fast/mon-entreprise/modifier-le-logo-et-les-informations-de-l-entreprise.md | 756 | logo et informations de l'entreprise (onboarding, coordonnées, métiers) | indetermine | personnalisation, conformite_reglementaire, documents | oui | non | oui | oui | oui | procedure (avec FAQ intégrée) |
| 145 | inter-fast/mon-entreprise/modifier-le-pays-d-etablissement-de-mon-entreprise.md | 98 | pays d'établissement (modification, adaptation des formats d'adresse) | indetermine | personnalisation, crm | oui | non | oui | non | non | procedure |
| 146 | inter-fast/mon-entreprise/parametrer-l-export-comptable.md | 3025 | paramétrage de l'export comptable (TVA, journal ventes/achats, agences) | facturation | comptabilite, conformite_reglementaire, roles | oui | oui | oui | oui | oui | procedure (avec FAQ intégrée) |
| 147 | inter-fast/mon-entreprise/parametrer-mes-chantiers.md | 1362 | paramétrage du module Chantiers (renommage, accès documents, traitement des déchets) | chantier-intervention | personnalisation, permissions, conformite_reglementaire | oui | oui | oui | oui | oui | procedure (avec FAQ intégrée) |
| 148 | inter-fast/mon-entreprise/parrainer-un-artisan-sur-interfast.md | 534 | programme de parrainage (lien, avantages, crédits) | achat | tarification, facturation, marketing_et_communication | oui | oui | oui | oui | oui | procedure (avec FAQ intégrée et contenu promotionnel) |
| 149 | inter-fast/mon-entreprise/personnaliser-mes-devis-factures-clients.md | 509 | personnalisation de la présentation des devis/factures (en-tête, polices, filigrane, CGV, pied de page) | indetermine | personnalisation, documents, conformite_reglementaire | oui | non | oui | oui | non | reference_configuration (avec procédure) |
| 150 | inter-fast/mon-entreprise/personnaliser-mes-rapports-d-intervention.md | 807 | personnalisation des rapports d'intervention (style, filigrane, géolocalisation) | chantier-intervention | personnalisation, geolocalisation, photos | oui | non | oui | oui | oui | reference_configuration (avec FAQ intégrée) |
| 151 | inter-fast/mon-entreprise/souscrire-a-un-abonnement.md | 386 | souscription à un abonnement (choix du plan, paiement) | achat | tarification, paiement, facturation | oui | oui | oui | non | non | procedure |
| 152 | inter-fast/mon-entreprise/supprimer-un-import-de-fichier.md | 349 | suppression d'un import de fichier (annulation, nettoyage base) | indetermine | crm, conformite_reglementaire, documents | oui | non | oui | oui | oui | procedure (avec FAQ intégrée) |
| 153 | inter-fast/mon-entreprise/telecharger-ma-facture-d-abonnement.md | 102 | facture d'abonnement (téléchargement) | facturation | facturation, documents | oui | non | non | oui | non | procedure |
| 154 | inter-fast/mon-entreprise/utiliser-l-api-d-interfast.md | 1005 | API REST InterFast (documentation, authentification, différences MCP) | indetermine | integrations, automatisation, securite_compte | oui | non | oui | oui | non | definitionnel (avec FAQ intégrée) |
| 155 | inter-fast/mon-entreprise/utiliser-les-blocs-de-texte.md | 73 | blocs de texte (mentions légales, notes, insertion dans documents) | indetermine | documents, personnalisation | oui | non | non | non | non | procedure |
| 156 | inter-fast/mon-entreprise/utiliser-les-proprietes-personnalisees.md | 1743 | propriétés personnalisées (création, objets compatibles, export) | indetermine | personnalisation, catalogue, reporting | oui | oui | oui | oui | oui | procedure (avec FAQ intégrée) |
| 157 | inter-fast/operations/archiver-desarchiver-un-chantier.md | 657 | archivage/désarchivage d'un chantier (conservation de l'historique) | chantier-intervention | documents, mobile, communication | oui | non | oui | oui | non | procedure (avec FAQ intégrée) |
| 158 | inter-fast/operations/comprendre-la-fiche-d-intervention-app-web.md | 870 | fiche d'intervention app web (actions, onglets, rapport, suppression) | chantier-intervention | communication, photos, documents | oui | oui | oui | oui | oui | procedure (avec FAQ intégrée) |
| 159 | inter-fast/operations/comprendre-la-fiche-d-un-chantier.md | 1368 | fiche d'un chantier (informations générales, onglets vente/dépenses/interventions) | chantier-intervention | planning, gestion_stock, communication | oui | oui | oui | oui | non | reference_configuration (avec procédure) |
| 160 | inter-fast/operations/comprendre-la-fiche-d-une-maintenance.md | 964 | fiche de maintenance (visites, interventions, équipements, devis/factures) | chantier-intervention | planning, automatisation, documents | oui | oui | oui | oui | oui | reference_configuration (avec FAQ intégrée) |
| 161 | inter-fast/operations/comprendre-le-module-calendrier.md | 1525 | module Calendrier (vues, filtres, synchronisation iCal) | chantier-intervention | planning, roles, integrations | oui | non | oui | oui | oui | reference_configuration (avec FAQ intégrée) |
| 162 | inter-fast/operations/comprendre-le-tableau-des-chantiers.md | 727 | tableau des chantiers (vues tableau/planning/synthèse) | chantier-intervention | planning, reporting, personnalisation | oui | non | oui | non | non | reference_configuration |
| 163 | inter-fast/operations/comprendre-le-tableau-des-maintenances.md | 2676 | tableau des maintenances (facturation automatique, planification des visites, visites prévisionnelles) | chantier-intervention | automatisation, planning, facturation | oui | oui | oui | oui | oui | procedure (avec FAQ intégrée) |
| 164 | inter-fast/operations/comprendre-les-contrats-de-maintenance.md | 709 | contrats de maintenance (échéancier de facturation indépendant des visites) | chantier-intervention | automatisation, facturation, crm | oui | oui | oui | oui | non | procedure (avec FAQ intégrée) |
| 165 | inter-fast/operations/configurer-le-module-calendrier.md | 1060 | configuration du module Calendrier (affichage, absences, feuilles d'heures, statuts) | chantier-intervention | personnalisation, planning, roles | oui | non | oui | non | oui | reference_configuration (avec FAQ intégrée) |
| 166 | inter-fast/operations/creer-un-decompte-general-definitif-dgd.md | 782 | décompte général définitif DGD (bilan financier de fin de chantier) | facturation | conformite_reglementaire, facturation, validation | oui | oui | oui | oui | non | politique_legale (avec procédure associée) |
| 167 | inter-fast/operations/declarer-une-absence.md | 135 | déclaration d'absence (activation, saisie) | indetermine | planning, roles | oui | non | non | non | non | procedure |
| 168 | inter-fast/operations/documenter-les-visites-avant-devis.md | 1118 | visite avant devis (chiffrage terrain, photos, rapport) | devis | mobile, photos, documents | oui | oui | oui | oui | non | procedure (avec FAQ intégrée) |
| 169 | inter-fast/operations/exporter-mes-interventions.md | 746 | export des interventions (CSV, PDF) | chantier-intervention | documents, reporting, photos | oui | non | oui | oui | oui | procedure (avec FAQ intégrée) |
| 170 | inter-fast/operations/gerer-les-taches-app-web.md | 1124 | gestion des tâches (listes, assignation, usage mobile) | indetermine | mobile, notifications, roles | oui | non | oui | oui | oui | procedure (avec FAQ intégrée) |
| 171 | inter-fast/operations/guide-complet-gerer-un-chantier-dans-interfast.md | 11982 | cycle complet de gestion d'un chantier (demande → devis → chantier → exécution → facturation → rentabilité) | indetermine | automatisation, planning, facturation | oui | oui | oui | oui | oui | procedure (avec contenu marketing important et FAQ) |
| 172 | inter-fast/operations/organiser-le-planning-chantier.md | 848 | planning chantier (visualisation, planification, personnalisation affichage) | chantier-intervention | planning, personnalisation, reporting | oui | non | oui | oui | non | procedure |
| 173 | inter-fast/operations/planifier-les-interventions-sur-une-carte.md | 719 | planification cartographique des interventions (géolocalisation, tournées) | chantier-intervention | geolocalisation, planning, crm | oui | non | oui | oui | oui | procedure (avec FAQ intégrée) |
| 174 | inter-fast/operations/planifier-les-maintenances-sur-une-carte.md | 231 | planification cartographique des maintenances | chantier-intervention | geolocalisation, planning | oui | non | non | non | non | procedure |
| 175 | inter-fast/operations/planifier-un-evenement-app-web.md | 870 | planification d'un événement (intervention, rendez-vous, absence) | chantier-intervention | planning, crm, documents | oui | oui | oui | non | oui | procedure (avec FAQ intégrée) |
| 176 | inter-fast/operations/remplir-modifier-un-rapport-d-intervention-app-web.md | 797 | rapport d'intervention app web (remplissage, modification, traçabilité) | chantier-intervention | photos, validation, documents | oui | non | oui | oui | oui | procedure |
| 177 | inter-fast/operations/remplir-un-pv-de-reception-de-chantier.md | 356 | PV de réception de chantier (rédaction, signature) | chantier-intervention | conformite_reglementaire, validation, mobile | oui | non | oui | oui | oui | politique_legale (avec procédure associée) |
| 178 | inter-fast/operations/signer-un-contrat-de-maintenance.md | 783 | signature électronique d'un contrat de maintenance (via devis, pièce jointe) | devis | validation, tarification, documents | oui | oui | oui | oui | oui | procedure |
| 179 | inter-fast/operations/suivre-les-heures-et-la-rentabilite-d-un-chantier.md | 1999 | suivi des heures et rentabilité d'un chantier (déboursé, marges) | chantier-intervention | reporting, gestion_stock, roles | oui | oui | oui | oui | oui | procedure (avec FAQ intégrée) |
| 180 | inter-fast/operations/suivre-les-heures-et-la-rentabilite-d-une-maintenance.md | 895 | suivi des heures et rentabilité d'une maintenance | chantier-intervention | reporting, mobile, personnalisation | oui | non | non | non | non | procedure |
| 181 | inter-fast/operations/utiliser-les-formulaires-de-demande.md | 790 | formulaires de demande (public, personnalisés, intégration) | demande | personnalisation, crm, mobile | oui | oui | oui | oui | non | procedure (avec FAQ intégrée) |
| 182 | inter-fast/outils/activer-et-utiliser-la-page-publique-de-vos-equipements-via-qr-code.md | 394 | page publique des équipements via QR code (accès sans authentification, signalement) | chantier-intervention | securite_compte, documents, mobile | oui | oui | oui | oui | oui | procedure (avec FAQ intégrée) |
| 183 | inter-fast/outils/ajouter-des-clients-prospects-fournisseurs.md | 825 | ajout clients/prospects/fournisseurs/contacts (CRM) | indetermine | crm, communication, notifications | oui | non | oui | oui | oui | procedure (avec FAQ intégrée) |
| 184 | inter-fast/outils/ajouter-et-consigner-des-equipements-niveau-1.md | 918 | équipements niveau 1 (saisie, import CSV, association intervention) | indetermine | documents, crm, mobile | oui | oui | oui | oui | oui | procedure (avec FAQ intégrée) |
| 185 | inter-fast/outils/archiver-un-client.md | 71 | archivage d'un client (CRM) | indetermine | crm | oui | non | oui | oui | non | procedure |
| 186 | inter-fast/outils/automatiser-les-demandes-d-avis-clients.md | 1066 | automatisation des demandes d'avis clients (Eldo, Bilik, Google My Business) | facturation | automatisation, integrations, marketing_et_communication | oui | oui | oui | non | non | procedure |
| 187 | inter-fast/outils/automatiser-mes-actions-et-taches.md | 1119 | automatisations (actions et tâches, modèles, scénarios) | indetermine | automatisation, communication, conformite_reglementaire | oui | oui | oui | oui | oui | procedure (avec FAQ intégrée) |
| 188 | inter-fast/outils/changer-le-statut-d-un-client.md | 42 | statut d'un client (client/prospect/fournisseur) | indetermine | crm | oui | oui | non | non | non | procedure |
| 189 | inter-fast/outils/comprendre-la-fiche-d-un-client.md | 1654 | fiche client (sections, documents, interventions, devis/factures, équipements) | indetermine | crm, documents, communication | oui | oui | oui | oui | oui | reference_configuration (avec FAQ intégrée) |
| 190 | inter-fast/outils/comprendre-la-fiche-d-un-fournisseur.md | 785 | fiche fournisseur (informations, dépenses, commandes) | indetermine | crm, gestion_stock, documents | oui | non | non | non | non | reference_configuration (avec FAQ intégrée) |
| 191 | inter-fast/outils/comprendre-la-fiche-d-un-produit.md | 1252 | fiche produit (stock, mouvements, alarmes, bibliothèque) | indetermine | gestion_stock, catalogue, tarification | oui | oui | oui | oui | oui | reference_configuration (avec FAQ intégrée) |
| 192 | inter-fast/outils/comprendre-la-fiche-d-un-prospect.md | 1058 | fiche prospect (informations, conversion en client, équipements) | demande | crm, documents, communication | oui | oui | oui | non | non | reference_configuration (avec FAQ intégrée) |
| 193 | inter-fast/outils/comprendre-le-tableau-de-la-bibliotheque.md | 937 | bibliothèque d'articles (catalogue, ouvrages, import/export, stock) | devis | catalogue, tarification, gestion_stock | oui | oui | oui | non | non | procedure |
| 194 | inter-fast/outils/comprendre-les-tableaux-du-crm.md | 1526 | tableaux du CRM (vues clients/prospects/fournisseurs/contacts/équipements, carte) | indetermine | crm, roles, geolocalisation | oui | non | oui | oui | oui | reference_configuration (avec FAQ intégrée) |
| 195 | inter-fast/outils/configurer-une-automatisation.md | 1177 | configuration d'une automatisation (déclencheur, scénario, arrêt, modèle devis→chantier) | devis | automatisation, roles, facturation | oui | oui | oui | oui | oui | procedure (avec FAQ intégrée) |
| 196 | inter-fast/outils/creer-et-utiliser-les-articles.md | 307 | création/modification/export/suppression d'articles (bibliothèque) | devis | catalogue, tarification, integrations | oui | non | non | non | non | procedure |
| 197 | inter-fast/outils/creer-un-catalogue-d-articles.md | 180 | création de catalogue et sous-catalogue d'articles | indetermine | catalogue, personnalisation | oui | non | oui | non | non | procedure |
| 198 | inter-fast/outils/envoyer-et-suivre-l-envoi-et-le-statut-de-vos-emails-historique-et-actions.md | 1821 | envoi et suivi des emails (statuts, pixel invisible, expéditeur) | indetermine | communication, documents, crm | oui | oui | oui | oui | oui | procedure (avec FAQ intégrée et contenu définitionnel) |
| 199 | inter-fast/outils/exporter-mon-fichier-clients.md | 649 | export du fichier clients (CSV, campagnes email externes) | indetermine | crm, documents, marketing_et_communication | oui | non | oui | oui | oui | procedure (avec FAQ intégrée) |
| 200 | inter-fast/outils/exporter-ses-stocks-au-format-csv-avec-qr-codes-associes.md | 978 | export des stocks CSV avec QR codes (inventaire, import masse) | indetermine | gestion_stock, documents, catalogue | oui | oui | oui | oui | oui | procedure (avec FAQ intégrée) |
| 201 | inter-fast/outils/gerer-les-equipements-niveau-2.md | 1453 | équipements niveau 2 (types, propriétés personnalisées, IA plaque signalétique, pré-remplissage) | chantier-intervention | personnalisation, automatisation, photos | oui | oui | oui | oui | oui | procedure (avec FAQ intégrée) |
| 202 | inter-fast/outils/gerer-les-stocks-app-web.md | 1520 | gestion des stocks (emplacements, produits, décrémentation, export) | indetermine | gestion_stock, catalogue, documents | oui | oui | oui | non | non | procedure |
| 203 | inter-fast/outils/gerer-vos-demandes-de-materiel-app-web.md | 1475 | demandes de matériel (préparation, récupération, liaison chantier) | chantier-intervention | gestion_stock, roles, mobile | oui | oui | oui | oui | oui | procedure (avec FAQ intégrée) |
| 204 | inter-fast/outils/guide-complet-la-gestion-des-stocks-dans-interfast.md | 1066 | guide de la gestion des stocks (mouvements, liaison bibliothèque, cas d'usage) | indetermine | gestion_stock, catalogue, roles | oui | oui | oui | oui | oui | procedure (avec contenu définitionnel et FAQ) |
| 205 | inter-fast/outils/guide-complet-travailler-avec-des-proprietaires-syndics-agences-immobilieres-et-autres-donneurs-d-ordre.md | 2084 | travailler avec syndics/agences/donneurs d'ordre (relations, sites et emplacements GMAO) | indetermine | crm, facturation, planning | oui | oui | oui | oui | oui | definitionnel (avec procédure et FAQ) |
| 206 | inter-fast/outils/importer-des-articles.md | 1286 | import d'articles (préparation fichier, matching, correction erreurs) | indetermine | catalogue, tarification, gestion_stock | oui | non | oui | oui | oui | procedure (avec FAQ intégrée) |
| 207 | inter-fast/outils/importer-des-clients.md | 1689 | import de clients (préparation fichier, mapping, annulation) | indetermine | crm, conformite_reglementaire, comptabilite | oui | non | oui | oui | oui | procedure (avec FAQ intégrée) |
| 208 | inter-fast/outils/mettre-a-jour-les-articles-de-votre-bibliotheque.md | 733 | mise à jour en masse des articles de la bibliothèque (import CSV, prix) | indetermine | catalogue, tarification, documents | oui | non | oui | oui | non | procedure |
| 209 | inter-fast/outils/modifier-un-catalogue-d-articles.md | 39 | renommage d'un catalogue d'articles | indetermine | catalogue, personnalisation | oui | non | non | non | non | procedure |
| 210 | inter-fast/outils/partager-sa-bibliotheque-d-articles-et-d-ouvrages.md | 789 | partage de bibliothèque d'articles entre entreprises (multi-société) | indetermine | catalogue, multi-societe, permissions | oui | non | oui | oui | oui | procedure (avec FAQ intégrée) |
| 211 | inter-fast/outils/suivre-les-executions-des-automatisations.md | 1204 | suivi des exécutions des automatisations (journal, statuts, relance) | indetermine | automatisation, communication, validation | oui | non | oui | oui | oui | procedure (avec FAQ intégrée) |
| 212 | inter-fast/outils/utiliser-le-portail-client.md | 1332 | portail client (accès, visibilité, signature électronique, demandes en ligne) | indetermine | presence_en_ligne, validation, securite_compte | oui | oui | oui | oui | oui | procedure (avec FAQ intégrée) |
| 213 | inter-fast/outils/utiliser-les-ouvrages.md | 1094 | ouvrages (création, imbrication, masquage prix/composition, mobile) | devis | catalogue, tarification, mobile | oui | oui | oui | oui | oui | procedure (avec FAQ intégrée) |
| 214 | inter-fast/outils/utiliser-les-qr-codes-app-web.md | 1171 | QR codes (création, association, utilisation mobile) | chantier-intervention | mobile, gestion_stock, personnalisation | oui | oui | oui | oui | non | procedure |
| 215 | inter-fast/outils/utiliser-les-relations-clients.md | 1400 | relations clients (liens propriétaire/locataire, payeur automatique maintenance) | facturation | crm, facturation, automatisation | oui | oui | oui | oui | oui | procedure (avec FAQ intégrée) |
| 216 | inter-fast/outils/utiliser-les-tableaux-de-bord.md | 561 | tableaux de bord (activité, financier) | indetermine | reporting, comptabilite, multi-societe | oui | non | non | non | non | reference_configuration |
| 217 | inter-fast/outils/visualiser-les-clients-sur-une-carte.md | 609 | visualisation des clients sur une carte (CRM, géolocalisation) | indetermine | geolocalisation, crm, planning | oui | oui | non | non | oui | procedure |

## Contrôles mécaniques de complétude

- Documents traités : **217/217** (périmètre gelé intégral).
- Numérotation `#` : 1→217 continue, vérifiée mécaniquement — 0 doublon,
  0 trou.
- `chemin_relatif` : 217 valeurs uniques, correspondance exacte 1:1 (même
  ensemble, même ordre) avec la liste `restant` gelée en début de run.
  Une incohérence de préfixe sur 36 lignes (`outils/` sans `inter-fast/`)
  a été détectée et corrigée avant validation (voir Journal d'incidents).
- `longueur_mots` : les 217 valeurs du tableau correspondent exactement,
  ligne à ligne, aux valeurs precalculées mécaniquement dans
  `interfast_wordcounts.tsv` (méthode `awk`+`wc -w` déclarée en tête de
  fichier) — 0 écart.
- 12 colonnes par ligne : vérifié mécaniquement sur les 217 lignes
  (14 champs séparés par `|`, bordures comprises).
- `moment_parcours` : 217/217 valeurs dans le vocabulaire fermé
  (`indetermine · demande · devis · achat · chantier-intervention ·
  facturation`) — 0 violation.
- Colonnes `oui/non` (procedure, transition_objet, regle_ou_condition,
  contrainte_ou_limite, exception_ou_correction) : 217/217 valeurs
  strictement `oui` ou `non` — 0 valeur `inconnu`, 0 valeur hors
  vocabulaire.
- `capacites_transverses` : maximum 3 par document respecté sur les
  217 lignes (191 lignes à 3, 18 à 2, 6 à 1, 2 à 0) ; aucune valeur hors
  vocabulaire de base/étendu/arbitrage différé détectée.

## Agrégats descriptifs

Agrégats mécaniques sur les 217 documents traités. Purement descriptifs
— aucune conclusion de prévalence ou de couverture fonctionnelle
InterFast n'en est tirée (principe SCHEMA-LIGHT.md).

**Volume**

- Total : 214 821 mots cumulés sur 217 documents.
- Moyenne : ≈990 mots/document. Minimum : 39 mots (# 209, renommage
  d'un catalogue). Maximum : 11 982 mots (# 171, guide complet de
  gestion d'un chantier — plus de 10× la moyenne du corpus).
- 13 documents sous 150 mots (procédures atomiques à une action) ; à
  l'autre extrême, 6 documents dépassent 3000 mots (# 38, # 119, # 128,
  # 146, # 171, # 205 — guides et pages réglementaires denses).

**`moment_parcours` (vocabulaire fermé, 217/217)**

`indetermine` 89 · `chantier-intervention` 53 · `facturation` 35 ·
`devis` 23 · `achat` 15 · `demande` 2.

La proportion élevée d'`indetermine` (41 %) reflète la nature du corpus
`outils`/`mon-entreprise` : fiches de configuration, fiches d'entité CRM
(client/prospect/fournisseur) et documentation d'objets transverses
(bibliothèque, automatisations, tableaux de bord) qui ne s'ancrent pas à
un moment unique du parcours commercial.

**`capacites_transverses` — 10 valeurs les plus fréquentes (sur 217
documents, max 3/document)**

`documents` 62 · `mobile` 45 · `conformite_reglementaire` 40 ·
`personnalisation` 39 · `roles` 37 · `catalogue` 31 · `automatisation`
31 · `integrations` 30 · `crm` 29 · `validation` 27.

**`genre_documentaire` (racine, vocabulaire ouvert)**

`procedure` 167 · `reference_configuration` 26 · `politique_legale` 11 ·
`faq_depannage` 6 · `definitionnel` 5 · `marketing_dans_aide` 1 ·
`autre` 1.

**Colonnes `contenu_observable` (oui / 217)**

`procedure` 204 · `regle_ou_condition` 170 · `contrainte_ou_limite` 169
· `exception_ou_correction` 128 · `transition_objet` 95.

La colonne `transition_objet` est la moins souvent `oui` (95/217, 44 %) :
cohérent avec un corpus où une majorité de documents (fiches CRM,
paramétrages, exports) décrivent un seul objet stable plutôt qu'un
enchaînement d'objets métier.

## Cas mal représentés

- **# 171 (`operations/guide-complet-gerer-un-chantier-dans-interfast.md`,
  11 982 mots) et # 205
  (`outils/guide-complet-travailler-avec-des-proprietaires-syndics-...md`,
  2 084 mots)** : guides « bout-en-bout » couvrant délibérément
  plusieurs moments du parcours (demande → devis → chantier → exécution
  → facturation pour # 171 ; planification → facturation pour # 205).
  Codés `moment_parcours = indetermine` faute de mapping unique dans le
  vocabulaire fermé — ce codage est mécaniquement correct mais aplatit
  la nature transversale réelle du document. Le schéma LIGHT ne prévoit
  pas de valeur multiple pour `moment_parcours` ; ces deux documents sont
  sous-représentés par une colonne à valeur unique.
- **# 204 (`outils/guide-complet-la-gestion-des-stocks-dans-interfast.md`)**
  : même profil, guide transversal (vente/achat/intervention/stock)
  également codé `indetermine`.
- **# 38 (`debuter-avec-interfast/construire-le-cerveau-numerique-de-votre-entreprise.md`)**
  : seul document du corpus dont la racine `genre_documentaire` est
  `marketing_dans_aide` — contenu à dominante promotionnelle/témoignages
  clients logé dans la documentation d'aide. Cas limite entre
  documentation produit et argumentaire commercial ; SCHEMA-LIGHT.md ne
  fournit pas de sous-critère pour distinguer un degré de promotion
  dans un article par ailleurs structurellement informatif.
- **13 documents sous 150 mots** (# 2, # 43, # 56, # 86, # 120, # 135,
  # 145, # 153, # 155, # 167, # 185, # 188, # 209) : procédures à une
  seule action ou pages de renvoi minimales. Les 12 colonnes LIGHT
  restent applicables mais portent peu d'information distinctive —
  plusieurs partagent un profil quasi identique (`procedure`, colonnes
  `non` presque partout, `genre_documentaire = procedure`) sans que le
  schéma prévoie de marqueur de « densité informationnelle ».

## Limites

- `objet_principal` et `genre_documentaire` restent des vocabulaires
  ouverts non normalisés entre productions LIGHT successives ; aucune
  comparaison de fréquence avec `light-vertuoza-help.md` ou les autres
  corpus déjà traités n'a été tentée dans ce fichier.
- `tarification` (vs `catalogue`) et `marketing_et_communication` (vs
  `communication`) restent sous arbitrage différé : les 17 et 5
  occurrences respectives sont journalisées mais non résolues, comme
  prescrit par la mission. Toute analyse en aval qui traiterait ces
  valeurs comme définitivement distinctes de `catalogue`/`communication`
  irait au-delà de ce que ce fichier établit.
- Le codage des colonnes `contenu_observable` (procedure,
  transition_objet, regle_ou_condition, contrainte_ou_limite,
  exception_ou_correction) reste un jugement de lecture par document,
  non un calcul mécanique : deux lecteurs pourraient trancher
  différemment sur des cas limites (ex. une simple remarque
  « ⚠️ » constitue-t-elle une `contrainte_ou_limite` ou une
  `exception_ou_correction` ?). Aucun second passage de vérification
  croisée n'a été effectué sur ce run.
- Ce fichier ne mesure et ne conclut rien sur la présence ou l'absence
  fonctionnelle d'une capacité chez InterFast au-delà de ce que le
  contenu documentaire observable décrit explicitement — conformément
  au principe SCHEMA-LIGHT.md de non-inférence depuis le silence
  documentaire.
- Aucune conclusion comparative SUPORDO vs InterFast n'est produite ni
  suggérée par ce fichier.
