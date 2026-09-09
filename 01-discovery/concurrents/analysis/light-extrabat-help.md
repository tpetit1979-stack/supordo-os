# LIGHT — production Extrabat (corpus aide)

Production sous SCHEMA-LIGHT.md (contrat canonique), lu intégralement avant
ce run. Discipline : un document à la fois, lu intégralement, sortie écrite
immédiatement, aucune correction rétroactive sauf erreur mécanique démontrée
et journalisée. Run de production, pas un test méthodologique de LIGHT.

## Périmètre — vérification mécanique et gel

Le périmètre LIGHT est le périmètre d'**ANALYSE**, pas le périmètre de
collecte. `corpus_index.json` (`extrabat_help`) distingue les deux :

- Collecte : **1670** fichiers `.md` sur disque sous
  `01-discovery/concurrents/sources/extrabat/centre_aide/`, inchangés.
- Exclusions d'analyse déclarées dans `corpus_index.json`, champ
  `analysis_exclusions` (chemin + motif, par document) : **1323**, en trois
  motifs — `LANGUE_NON_FRANCAISE` 223 (sous-arbres `/de`, `/es`, `/en`),
  `ARCHIVE_TAXONOMIE` 1060 (pages `/tag/`, doublons exacts d'articles),
  `PAGINATION` 40 (pages `/page/N/`, index chronologiques). Liste exhaustive
  et mécaniquement reconstructible : voir `corpus_index.json` →
  `corpora[corpus_id="extrabat_help"].analysis_exclusions` (renvoi, non
  retype ici — 1323 lignes).
- **Périmètre LIGHT (analyse) : 347.** Recalculé mécaniquement (liste des
  fichiers `.md` sur disque sous `centre_aide/` moins l'ensemble des
  chemins `analysis_exclusions`), pas recopié depuis `corpus_index.json`.
  Garde-fou de mission 1670 − 1323 = 347 : **écart nul**. Les 1323 chemins
  d'exclusion ont tous été retrouvés sur disque (0 chemin manquant).

Extrabat est le seul corpus du dépôt à porter des exclusions d'analyse.
Aucun document extrabat n'a jamais reçu d'observation LIGHT antérieure —
périmètre entièrement inédit au sens SCHEMA-LIGHT.md §5.

**Dix fichiers préservés** (`ANALYTICAL_EXCLUSION_PRESERVE` dans
`build_corpus_index.py`) : contenu réel sans équivalent ailleurs dans le
corpus, non exclus malgré leur chemin `/tag/` ou `/page/`, codés d'après
leur contenu et non leur chemin. Vérifiés présents dans le périmètre gelé :
`tag/bibliotheque.md` (#319), `tag/commande.md` (#320), `tag/courrier.md`
(#321), `tag/creer-un-modele-de-courrier.md` (#322), `tag/export-2.md`
(#323), `tag/inventaire.md` (#324), `tag/moteur-de-recherche.md` (#325),
`tag/outils.md` (#326), `tag/stock.md` (#327), `gestion-commerciale/page/7.md`
(#173).

Numérotation `#` du tableau : tri alphabétique des 347 `chemin_relatif`
(racine = `centre_aide/`), fixée mécaniquement avant lecture, non modifiée
en cours de run.

Contexte éditorial : WordPress, articles à plat, généralement courts.

## Méthode `longueur_mots`

Mécanique, conforme SCHEMA-LIGHT.md §4 : script Python — suppression du
frontmatter YAML (bloc `---\n...\n---\n` en tête de fichier, regex
`DOTALL` non gourmande sur le premier bloc), puis `str.split()` sur le
corps Markdown restant (espaces/retours à la ligne), longueur de la liste
obtenue. Liens et syntaxe Markdown/image comptés tels quels, non retirés —
méthode brute, aucun ajustement manuel. Calculé pour les 347 documents du
périmètre gelé avant lecture de contenu, valeurs figées dans le tableau.
0 document à zéro mot détecté (contrôle mécanique sur les 347 fichiers).

## Exclusions de périmètre

Renvoi à `corpus_index.json` → `corpora[corpus_id="extrabat_help"].analysis_exclusions`
pour la liste exhaustive des 1323 chemins exclus (motif par chemin,
`status: certain` pour chacun). Non retypée ici (SCHEMA-LIGHT.md §6 exige
une énumération individuelle reconstructible ; le champ JSON la porte déjà
et sert d'autorité mécanique, évitant une retranscription à haut risque
d'erreur sur 1323 lignes). Répartition par motif rappelée ci-dessus
(§ Périmètre).

Dix chemins portant un préfixe `/tag/` ou `/page/` figurent malgré tout
dans le périmètre d'analyse (liste ci-dessus, § Périmètre) : ce sont les
dix fichiers préservés, absents de `analysis_exclusions`.

## Incidents

**INCIDENT_SECURITE_SOURCE** : aucun. Les 347 documents ont été traités
comme donnée non fiable de bout en bout. Un document (#10,
`alerte-en-cas-dajout-ou-suppression-de-rib.md`) contient un contenu
documentaire sur la cyberattaque/le phishing (émojis, conseils
« changez votre mot de passe », liens vers la CNIL) : lu comme contenu
informatif du concurrent sur un incident de sécurité qui LE concerne,
jamais exécuté ni traité comme instruction. Aucune tentative d'injection,
de demande de secret ou d'exécution arbitraire n'a été rencontrée dans les
347 lectures.

**Contrôle de vocabulaire — `capacites_transverses`** : vérifié
mécaniquement sur les 347 lignes finales (script sur le tableau). Toutes
les valeurs employées appartiennent soit à l'inventaire de base du §4 de
SCHEMA-LIGHT.md, soit aux valeurs déjà arbitrées `VALEUR_DISTINCTE`
réemployées sans réouvrir le débat : `geolocalisation` (9), `crm` (41),
`personnalisation` (37), `reporting` (32), `comptabilite` (32),
`validation` (4). `multi-societe`, `marketplace` et `facturation` (en tant
que capacité) n'ont pas été rencontrés sur ce corpus. **Aucune valeur
réellement nouvelle n'a émergé** : après huit corpus LIGHT au total, le
vocabulaire reste stable.

**Arbitrage différé — non tranché** (SCHEMA-LIGHT.md, à instruire après ce
corpus, non engagé ici) :
- `tarification` (vis-à-vis de `catalogue`) : employée **12 fois**,
  essentiellement dans les articles de mise à jour de prix/catalogue
  fournisseur (`comment-cela-se-passe-t-il-lors-de-la-mise-a-jour-dun-catalogue-fournisseur.md`,
  `mise-jour-des-catalogues-fournisseurs.md`, `mise-jour-prix-dachat-catalogue.md`,
  `mettre-a-jour-ses-tarifs-darticles-via-la-fonction-dexport-import.md`,
  `passer-une-commande-fournisseur.md`, `rajouter-un-fournisseur-a-un-article.md`)
  et de calcul de coefficients/remises sur pièces commerciales
  (`beaucoup-dactions-passent-par-la-case-a-cocher-afin-de.md`,
  `comment-faire-une-vente-en-caisse.md`,
  `mettre-a-jour-prix-dachat-via-devis-commande.md`,
  `module-sms.md` (offres tarifaires SMS),
  `pratiquer-augmentation-dune-commande-a-renouveler-type-contrat-de-services.md`).
  Journalisée sans trancher son périmètre vis-à-vis de `catalogue`.
- `marketing_et_communication` (vis-à-vis de `communication`) : employée
  **2 fois** (`realiser-un-emailing.md`, campagne emailing ciblée ;
  `rentabilite-des-canaux-de-publicites.md`, statistiques de canaux
  publicitaires). Journalisée sans trancher son périmètre vis-à-vis de
  `communication`.

Ni l'une ni l'autre valeur n'a été fusionnée avec une racine existante ;
aucun périmètre n'a été défini pour ces deux capacités, conformément à
l'instruction de ne pas engager rétroactivement les runs précédents.

## Tableau LIGHT

| # | chemin_relatif | longueur_mots | objet_principal | moment_parcours | capacites_transverses | procedure | transition_objet | regle_ou_condition | contrainte_ou_limite | exception_ou_correction | genre_documentaire |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | accuse-de-reception-sur-les-e-mails-envoyes-par-extrabat.md | 122 | accusé de réception (email) | indetermine | notifications | oui | non | non | oui | non | procedure |
| 2 | activer-les-relances-par-sms-a-vos-clients-de-vos-contrats-dentretien.md | 119 | relance SMS (contrat d'entretien) | chantier-intervention | notifications, planning | oui | non | non | non | non | procedure |
| 3 | affecter-de-reception-a-plusieurs-affaires.md | 58 | bon de réception (affectation multi-affaires) | achat | gestion_stock | oui | non | oui | non | non | procedure |
| 4 | afficher-des-produits-sur-linterface-de-caisse.md | 83 | interface de caisse (sélections produits) | indetermine | catalogue | oui | non | non | oui | non | procedure |
| 5 | afficher-question-complementaire-page-daccueil.md | 64 | question complémentaire (page d'accueil) | indetermine | personnalisation | oui | non | non | non | non | procedure |
| 6 | agenda-2.md | 360 | synchronisation agenda (CalDAV/mobile) | indetermine | integrations, mobile | oui | non | non | non | oui | procedure |
| 7 | ajouter-suivi-prospect.md | 215 | suivi prospect | demande | crm | oui | non | non | oui | non | procedure |
| 8 | ajouter-un-utilisateur.md | 149 | utilisateur (ajout) | indetermine | securite_compte, permissions | oui | non | non | oui | non | procedure |
| 9 | alarmes-pour-les-rdv.md | 61 | alarmes RDV/intervention | chantier-intervention | notifications, planning | oui | non | non | non | non | procedure |
| 10 | alerte-en-cas-dajout-ou-suppression-de-rib.md | 339 | alerte sécurité RIB | indetermine | securite_compte, notifications | oui | non | oui | oui | oui | faq_depannage |
| 11 | amelioration-affichage-sav-sur-page-daccueil.md | 72 | affichage SAV (page d'accueil) | chantier-intervention | personnalisation | oui | non | non | non | non | procedure |
| 12 | annuler-des-relances-clients.md | 95 | relance client (annulation) | facturation | communication | oui | non | non | non | non | procedure |
| 13 | annuler-un-reliquat-de-commande-fournisseur.md | 50 | commande fournisseur (reliquat) | achat | gestion_stock | oui | oui | non | non | non | procedure |
| 14 | annuler-une-remise-en-banque.md | 58 | remise en banque (annulation) | facturation | paiement | oui | non | non | non | non | procedure |
| 15 | application-extrabat-today.md | 220 | application mobile Extrabat Today | chantier-intervention | mobile, offline, photos | non | non | non | non | non | definitionnel |
| 16 | application-extradoc.md | 103 | application ExtraDoc (GED mobile) | indetermine | mobile, documents, permissions | non | non | non | non | non | definitionnel |
| 17 | application.md | 1131 | application Extrabat Today v3.5 (nouveautés) | chantier-intervention | mobile, photos, offline | non | non | non | oui | non | marketing_dans_aide |
| 18 | assistance.md | 532 | intégration Install Bois (Extrabat Chauffage) | chantier-intervention | integrations, documents, conformite_reglementaire | oui | non | non | non | non | marketing_dans_aide |
| 19 | associer-la-domotique-klereo-a-extrabat.md | 51 | intégration domotique Kléreo (piscine) | indetermine | integrations | oui | non | non | non | non | procedure |
| 20 | associer-rendez-vous-plusieurs-utilisateurs-sur-plusieurs-jours.md | 45 | rendez-vous (multi-utilisateurs, multi-jours) | chantier-intervention | planning | oui | non | non | non | non | procedure |
| 21 | astuce-le-raccourci-de-recherche.md | 45 | — (page sans contenu substantif, résidu de gabarit de navigation) | indetermine | — | non | non | non | non | non | autre |
| 22 | astuces.md | 309 | signatures électroniques (accès Oodrive) | indetermine | documents, conformite_reglementaire | oui | non | non | oui | oui | procedure |
| 23 | attacher-une-documentation-a-un-article.md | 75 | documentation (liaison à un article) | indetermine | documents, catalogue | oui | non | non | non | non | procedure |
| 24 | attribuer-action-a-collaborateur.md | 65 | action (fiche client, attribution) | indetermine | crm, notifications | oui | non | non | non | non | procedure |
| 25 | avoir-acces-ses-rendez-vous-sans-avoir-acces-extrabat.md | 53 | synchronisation rendez-vous (accès externe) | indetermine | mobile, notifications, integrations | oui | non | non | non | non | procedure |
| 26 | avoir-en-temps-reel-sur-un-article-toutes-ses-affectations-reassort-reserve-a-commander.md | 69 | affectation stock (article) | indetermine | gestion_stock, recherche | oui | non | non | non | non | procedure |
| 27 | beaucoup-dactions-passent-par-la-case-a-cocher-afin-de.md | 273 | actions en masse (pièces commerciales) | indetermine | tarification, documents, paiement | oui | oui | non | non | non | reference_configuration |
| 28 | biblitoheque.md | 248 | tag (bibliothèque, porte-documents) | indetermine | documents, recherche, photos | oui | non | non | non | non | procedure |
| 29 | bien-parametrer-firefox.md | 62 | paramétrage navigateur (Firefox) | indetermine | — | oui | non | non | non | non | reference_configuration |
| 30 | bien-preparer-ses-commandes-pre-saison.md | 56 | statistiques ventes (préparation commandes pré-saison) | achat | reporting, gestion_stock | oui | non | non | non | non | procedure |
| 31 | bloquer-gestion-commerciale-client-independant-de-lencours.md | 70 | blocage gestion commerciale (client) | indetermine | permissions, validation | oui | non | oui | oui | non | procedure |
| 32 | bon-de-travaux.md | 149 | bon de travaux (intervenant) | chantier-intervention | gestion_stock, planning | oui | oui | oui | non | non | procedure |
| 33 | bonnes-regles-afin-de-creer-affaire-de-gerer.md | 56 | affaire (bonnes pratiques, gestion) | indetermine | permissions, reporting | non | non | oui | non | non | reference_configuration |
| 34 | brouillon-2.md | 45 | délettrage (droits d'accès) | indetermine | permissions | oui | non | non | non | non | procedure |
| 35 | ca-restant-a-facturer.md | 714 | CA restant à facturer (rapport) | facturation | reporting, documents, notifications | oui | non | oui | oui | oui | reference_configuration |
| 36 | calculez-le-cout-de-son-sav-sous-garantie.md | 60 | coût SAV (sous garantie) | chantier-intervention | comptabilite, reporting | oui | non | non | non | non | procedure |
| 37 | changement-de-taux-de-tva-au-1er-janvier-2014.md | 182 | taux de TVA (changement réglementaire) | facturation | conformite_reglementaire, comptabilite | oui | non | oui | non | non | politique_legale |
| 38 | changer-le-statut-dun-clientprospecten-cours-de-chantier.md | 111 | statut client/prospect (chantier) | chantier-intervention | crm, planning | oui | oui | non | non | non | procedure |
| 39 | checklist-de-fin-dannee-extrabat.md | 541 | checklist fin d'année (clôture comptable) | facturation | comptabilite, documents, communication | oui | non | oui | oui | non | procedure |
| 40 | choisir-de-mettre-non-interlocuteur-devis-commande.md | 61 | interlocuteur par défaut (devis/commande) | devis | personnalisation | oui | non | non | non | non | procedure |
| 41 | classer-les-taches-planning.md | 40 | tâches planning (classement/ordre) | indetermine | planning | oui | non | non | non | non | procedure |
| 42 | cloturer-la-caisse.md | 44 | — (page sans contenu substantif, résidu de gabarit de navigation) | indetermine | — | non | non | non | non | non | autre |
| 43 | comment-activer-javascript-sous-android.md | 37 | activation JavaScript (Android) | indetermine | — | oui | non | non | non | non | reference_configuration |
| 44 | comment-associer-un-commercial-a-une-commande-client-pour-le-calcul-de-sa-commission.md | 120 | commission commerciale (commande client) | achat | crm, reporting, comptabilite | oui | non | oui | non | non | procedure |
| 45 | comment-attribuer-une-adresse-par-defaut-pour-les-pieces-type-fournisseur.md | 180 | adresse par défaut (pièces fournisseur) | achat | personnalisation, documents | oui | non | non | non | non | procedure |
| 46 | comment-bien-parametrer-son-navigateur-internet-firefox.md | 46 | — (page sans contenu substantif, résidu de gabarit de navigation) | indetermine | — | non | non | non | non | non | autre |
| 47 | comment-bloquer-les-sorties-de-stock-depuis-le-module-diviser-en-sous-commandes.md | 59 | sortie de stock (sous-commandes) | chantier-intervention | gestion_stock | oui | non | non | non | non | procedure |
| 48 | comment-cela-se-passe-t-il-lors-de-la-mise-a-jour-dun-catalogue-fournisseur.md | 156 | mise à jour catalogue fournisseur (tarifs) | achat | catalogue, tarification, gestion_stock | oui | non | oui | non | non | procedure |
| 49 | comment-changer-votre-mot-de-passe.md | 267 | mot de passe (changement/réinitialisation) | indetermine | securite_compte, permissions | oui | non | oui | oui | oui | procedure |
| 50 | comment-creer-raccourci-sur-ma-tablette-android.md | 61 | raccourci écran d'accueil (Android) | indetermine | mobile | oui | non | non | non | non | procedure |
| 51 | comment-creer-sa-signature-le-logiciel-extrabat.md | 47 | — (page sans contenu substantif, résidu de gabarit de navigation) | indetermine | — | non | non | non | non | non | autre |
| 52 | comment-creer-un-modele-de-message.md | 398 | modèle de message (email personnalisé) | indetermine | communication, personnalisation, documents | oui | non | non | non | non | procedure |
| 53 | comment-creer-un-nouvel-exercice-comptable.md | 206 | exercice comptable (création) | facturation | comptabilite | oui | non | non | non | non | procedure |
| 54 | comment-creer-un-tiers-payant.md | 105 | tiers payant (création) | facturation | paiement, documents | oui | non | non | oui | non | procedure |
| 55 | comment-creer-une-facture-proforma.md | 158 | facture proforma | devis | documents, personnalisation | oui | non | oui | non | non | definitionnel |
| 56 | comment-donner-les-droits-utilisateur-consulter-etou-modifier.md | 15 | — (page sans contenu substantif, question sans réponse) | indetermine | — | non | non | non | non | non | autre |
| 57 | comment-dupliquer-article.md | 57 | article (duplication) | indetermine | catalogue | oui | non | oui | oui | non | procedure |
| 58 | comment-dupliquer-un-modele-de-document.md | 45 | modèle de document (duplication) | indetermine | documents, personnalisation | oui | non | non | non | non | procedure |
| 59 | comment-effectuer-un-paiement-en-passant-par-le-lettrage.md | 243 | paiement (lettrage) | facturation | paiement, comptabilite | oui | oui | non | non | non | procedure |
| 60 | comment-effectuer-un-paiement-multiple-par-la-fiche-client.md | 226 | paiement multiple (fiche client) | facturation | paiement, comptabilite | oui | non | non | non | non | procedure |
| 61 | comment-effectuer-une-remise-en-banque-simplifiee.md | 218 | remise en banque (simplifiée) | facturation | paiement, documents | oui | non | non | non | non | procedure |
| 62 | comment-enregistrer-sav.md | 34 | SAV (enregistrement) | chantier-intervention | — | oui | non | oui | non | non | procedure |
| 63 | comment-envoyer-lidentifiant-de-lespace-client-sur-sa-boite-mail.md | 198 | identifiants espace client (envoi email) | indetermine | securite_compte, communication, presence_en_ligne | oui | non | oui | non | non | procedure |
| 64 | comment-envoyer-sa-commande-fournisseur-via-le-protocole-edi.md | 178 | commande fournisseur (protocole EDI) | achat | integrations, gestion_stock | oui | non | oui | non | non | procedure |
| 65 | comment-faire-apparaitre-la-liste-des-factures-soldees-ou-non.md | 109 | liste factures (soldées/non soldées) | facturation | reporting, comptabilite | oui | non | non | non | non | procedure |
| 66 | comment-faire-retour-article-creer-avoir.md | 51 | — (page sans contenu substantif, résidu de gabarit de navigation) | indetermine | — | non | non | non | non | non | autre |
| 67 | comment-faire-une-vente-en-caisse.md | 242 | vente en caisse (Extrabat Piscine) | achat | catalogue, paiement, tarification | oui | non | non | non | non | procedure |
| 68 | comment-fonctionne-lespace-client.md | 43 | — (page sans contenu substantif, résidu de gabarit de navigation) | indetermine | — | non | non | non | non | non | autre |
| 69 | comment-fonctionnent-les-tags-et-a-quoi-servent-ils.md | 248 | tag (bibliothèque, porte-documents) | indetermine | documents, recherche, photos | oui | non | non | non | non | procedure |
| 70 | comment-formater-une-image-en-708-x-142-pixels.md | 104 | redimensionnement image (Paint.NET) | indetermine | photos | oui | non | non | non | non | procedure |
| 71 | comment-geolocaliser-un-client-avec-myextrabat.md | 45 | — (page sans contenu substantif, résidu de gabarit de navigation) | indetermine | — | non | non | non | non | non | autre |
| 72 | comment-gerer-un-stock-alerte.md | 96 | stock alerte (article) | achat | gestion_stock, notifications | oui | non | non | non | non | procedure |
| 73 | comment-importer-des-articles-dun-catalogue-fournisseur.md | 185 | import articles (catalogue fournisseur) | achat | catalogue, gestion_stock, tarification | oui | non | non | oui | non | procedure |
| 74 | comment-joindre-une-piece-commerciale-a-un-sav.md | 189 | pièce commerciale (jointe à un SAV) | chantier-intervention | documents, crm | oui | non | non | non | non | procedure |
| 75 | comment-lancer-toutes-mes-adresses-web-preferees-en-ouvrant-firefox.md | 80 | paramétrage navigateur (Firefox, onglets favoris) | indetermine | — | oui | non | non | non | non | reference_configuration |
| 76 | comment-le-code-client-ou-code-comptable-se-cree.md | 68 | code client/comptable (création automatique) | facturation | comptabilite, crm | oui | oui | oui | non | non | definitionnel |
| 77 | comment-mettre-a-jour-un-article-a-partir-dune-piece-commerciale.md | 220 | article (mise à jour depuis pièce commerciale) | indetermine | catalogue, gestion_stock | oui | non | non | non | non | procedure |
| 78 | comment-mettre-a-jour-un-article-par-les-parametres.md | 245 | article (mise à jour via paramètres) | indetermine | catalogue, gestion_stock | oui | non | oui | non | non | procedure |
| 79 | comment-mettre-en-forme-devis-gras-italique-souligne-total-etc.md | 80 | mise en forme devis (texte, raccourcis) | devis | personnalisation, documents | oui | non | non | non | non | reference_configuration |
| 80 | comment-mettre-jour-les-articles-par-famille-famille-ou-par-fournisseur.md | 15 | — (page sans contenu substantif, question sans réponse) | indetermine | — | non | non | non | non | non | autre |
| 81 | comment-parametrer-cle-api-mailjet.md | 479 | intégration Mailjet (clé API, emailing) | indetermine | integrations, communication, securite_compte | oui | non | non | oui | oui | procedure |
| 82 | comment-parametrer-la-synchronisation-de-son-smartphone-apple-avec-lagenda-extrabat.md | 13 | — (page sans contenu substantif, question sans réponse) | indetermine | — | non | non | non | non | non | autre |
| 83 | comment-parametrer-le-smtp-brevo-dans-extrabat.md | 402 | intégration Brevo (SMTP, emailing) | indetermine | integrations, communication, securite_compte | oui | non | non | non | oui | procedure |
| 84 | comment-parametrer-linterface-de-caisse.md | 175 | interface de caisse (paramétrage, Extrabat Piscine) | indetermine | catalogue, paiement | oui | non | non | non | non | procedure |
| 85 | comment-parametrer-un-nouveau-logiciel-de-comptabilite-dans-extrabat.md | 982 | intégration logiciel de comptabilité (protocole d'export) | indetermine | integrations, comptabilite, documents | oui | non | oui | oui | oui | reference_configuration |
| 86 | comment-passer-une-commande-fournisseur-de-la-solution-extrabat-vers-pool-360.md | 239 | commande fournisseur (intégration Pool 360) | achat | integrations, gestion_stock, catalogue | oui | non | non | non | oui | procedure |
| 87 | comment-realiser-une-facture-en-autoliqudation.md | 96 | facture (autoliquidation TVA) | facturation | conformite_reglementaire, documents | oui | non | non | non | non | politique_legale |
| 88 | comment-relier-notice-technique-article.md | 47 | — (page sans contenu substantif, résidu de gabarit de navigation) | indetermine | — | non | non | non | non | non | autre |
| 89 | comment-rentrer-un-reglement-rapidement-sur-une-facture.md | 48 | — (page sans contenu substantif, résidu de gabarit de navigation) | indetermine | — | non | non | non | non | non | autre |
| 90 | comment-reparer-son-navigateur-internet-firefox.md | 45 | — (page sans contenu substantif, résidu de gabarit de navigation) | indetermine | — | non | non | non | non | non | autre |
| 91 | comment-savoir-si-article-jour-periode-de-moins-dun.md | 157 | article (fraîcheur de mise à jour, code couleur) | indetermine | catalogue, recherche | oui | non | oui | non | non | reference_configuration |
| 92 | comment-se-creer-une-base-article-a-partir-des-catalogues-fournisseurs.md | 194 | base articles (import depuis catalogues fournisseurs) | devis | catalogue, gestion_stock | oui | non | non | non | non | procedure |
| 93 | comment-sont-geres-les-paiements-differes-par-cheques.md | 115 | paiement différé (chèques) | facturation | paiement | oui | non | non | non | non | definitionnel |
| 94 | comment-souvre-le-tiroir-caisse.md | 44 | tiroir-caisse (mécanisme d'ouverture) | indetermine | — | non | non | non | non | non | definitionnel |
| 95 | comment-supprimer-un-ouvrage.md | 46 | ouvrage (suppression) | indetermine | — | oui | non | oui | oui | non | procedure |
| 96 | comment-supprimer-un-service.md | 73 | service (suppression) | indetermine | permissions | oui | non | oui | oui | non | procedure |
| 97 | comment-utiliser-la-fonctionnalite-modele-de-message.md | 288 | modèle de message (création/utilisation) | indetermine | communication, personnalisation | oui | non | non | non | non | procedure |
| 98 | commnet-figer-len-tete-des-taches-planning.md | 38 | en-tête planning (figer) | indetermine | planning | oui | non | non | non | non | procedure |
| 99 | comptabilite.md | 714 | CA restant à facturer (rapport) | facturation | reporting, documents, notifications | oui | non | oui | oui | oui | reference_configuration |
| 100 | compter-caisse-fin-de-journee.md | 59 | fond de caisse (comptage fin de journée) | indetermine | comptabilite, paiement | oui | non | non | non | oui | procedure |
| 101 | configuration-smtp-extrabat-avec-yahoo.md | 521 | configuration SMTP (Yahoo) | indetermine | integrations, communication, securite_compte | oui | non | non | non | non | procedure |
| 102 | configuration-smtp-extrabat.md | 419 | configuration SMTP (personnalisé) | indetermine | integrations, communication, securite_compte | oui | non | non | non | non | procedure |
| 103 | connaitre-les-statistiques-des-rendez-vous.md | 62 | statistiques rendez-vous | indetermine | reporting, planning | oui | non | non | non | non | procedure |
| 104 | connexion-install-bois.md | 532 | intégration Install Bois (Extrabat Chauffage) | chantier-intervention | integrations, documents, conformite_reglementaire | oui | non | non | non | non | marketing_dans_aide |
| 105 | consulter-vos-signatures-electroniques-avec-oodrive-sign.md | 309 | signatures électroniques (accès Oodrive) | indetermine | documents, conformite_reglementaire | oui | non | non | oui | oui | procedure |
| 106 | creer-affaire-y-associer-pieces-commerciales-commande-bl-de-reception-facture-avoirs.md | 49 | affaire (création, association pièces commerciales) | indetermine | documents | oui | non | non | non | non | procedure |
| 107 | creer-client-via-linterface-de-caisse.md | 46 | — (page sans contenu substantif, résidu de gabarit de navigation) | indetermine | — | non | non | non | non | non | autre |
| 108 | creer-modele-de-courrier.md | 168 | modèle de courrier (création) | indetermine | documents, personnalisation, communication | oui | non | non | non | non | procedure |
| 109 | creer-nouveau-mode-de-reglement.md | 103 | mode de règlement (création) | facturation | paiement, permissions | oui | non | oui | non | non | procedure |
| 110 | creer-nouvelle-saison.md | 32 | saison (couleur, planning) | indetermine | personnalisation, planning | oui | non | non | non | non | procedure |
| 111 | creer-ou-modifier-un-compte-comptable.md | 37 | compte comptable (création/modification) | facturation | comptabilite | oui | non | non | non | non | procedure |
| 112 | creer-recurrence.md | 124 | récurrence de facturation (commande divisée) | facturation | automatisation, notifications, planning | oui | non | non | non | non | procedure |
| 113 | creer-type-darticle.md | 65 | type d'article (création) | indetermine | catalogue | oui | non | non | non | non | procedure |
| 114 | creer-un-article-texte-sans-prix-ni-quantite.md | 70 | article texte (sans prix/quantité) | devis | catalogue, documents | oui | non | non | non | non | procedure |
| 115 | creer-un-bon-de-livraison-sans-prix.md | 66 | pièce commerciale sans prix (BL) | indetermine | documents, personnalisation | oui | non | non | non | non | procedure |
| 116 | creer-un-client-via-lagenda.md | 110 | client/prospect (création via agenda) | demande | crm, planning | oui | non | non | non | non | procedure |
| 117 | creer-un-modele-de-document-sur-mesure-devis-facture-etc.md | 232 | modèle de document sur mesure (devis/facture) | indetermine | documents, personnalisation, conformite_reglementaire | non | non | non | oui | non | reference_configuration |
| 118 | creer-un-nouvel-article.md | 45 | article (création) | indetermine | catalogue | oui | non | non | non | non | procedure |
| 119 | creer-une-facture-dacompte.md | 212 | facture d'acompte (commande divisée) | facturation | paiement, documents | oui | oui | non | non | non | procedure |
| 120 | creer-une-fiche-client-ou-prospect.md | 60 | fiche client/prospect (création) | demande | crm, recherche | oui | non | non | non | non | procedure |
| 121 | ctrl-f-et-ctrl-p.md | 132 | raccourcis clavier (recherche/impression) | indetermine | recherche | oui | non | non | non | non | reference_configuration |
| 122 | de-la-facturation-de-la-commande-jusqua-la-gestion-de-la-preparation-du-kit-sortie-du-stock.md | 158 | procédure interservices (facturation/dépôt, sortie de stock) | chantier-intervention | gestion_stock, planning | oui | oui | oui | non | oui | procedure |
| 123 | deplacer-plusieurs-articles-voire-familles-darticles.md | 51 | — (page sans contenu substantif, résidu de gabarit de navigation) | indetermine | — | non | non | non | non | non | autre |
| 124 | deplacer-plusieurs-lignes-dans-la-gestion-commerciale.md | 55 | lignes/nomenclature dynamique (déplacement, pièce commerciale) | indetermine | documents | oui | non | non | non | non | procedure |
| 125 | desactiver-ou-rendre-inactif-article.md | 140 | article (désactivation) | indetermine | catalogue, recherche | oui | oui | oui | oui | non | procedure |
| 126 | detail-du-stock-reserve.md | 48 | stock réservé (détail par article) | indetermine | gestion_stock, reporting | oui | non | non | non | non | procedure |
| 127 | dossier-client.md | 532 | intégration Install Bois (Extrabat Chauffage) | chantier-intervention | integrations, documents, conformite_reglementaire | oui | non | non | non | non | marketing_dans_aide |
| 128 | droits-de-lagenda.md | 53 | droits agenda (partage) | indetermine | permissions, planning | oui | non | non | non | non | procedure |
| 129 | dupliquer-devis-commande-facture.md | 45 | pièce commerciale (duplication) | indetermine | documents | oui | non | non | non | non | procedure |
| 130 | e-mailing.md | 402 | configuration SMTP (Brevo) | indetermine | integrations, communication, securite_compte | oui | non | non | non | oui | procedure |
| 131 | editer-la-liste-des-articles.md | 35 | liste articles (export) | indetermine | catalogue, reporting | oui | non | non | non | non | procedure |
| 132 | effectuer-relance-facture-client.md | 311 | relance facture client | facturation | paiement, communication, documents | oui | non | non | non | non | procedure |
| 133 | enregistrer-paiement-multiple.md | 14 | — (page sans contenu substantif, question sans réponse) | indetermine | — | non | non | non | non | non | autre |
| 134 | enregistrer-reglement.md | 140 | règlement facture (enregistrement) | facturation | paiement, comptabilite | oui | oui | non | non | non | procedure |
| 135 | enregistrer-un-nouveau-sav-et-caler-le-rendez-vous.md | 110 | SAV (enregistrement + planification RDV) | chantier-intervention | planning, crm | oui | non | oui | non | non | procedure |
| 136 | enregistrer-un-nouveau-service-et-caler-un-rendez-vous.md | 113 | service (enregistrement + planification RDV) | chantier-intervention | planning, crm | oui | non | oui | non | non | procedure |
| 137 | enregistrer-une-reception-de-stock.md | 186 | réception de stock (commande fournisseur) | achat | gestion_stock | oui | oui | non | non | non | procedure |
| 138 | entrer-fond-de-caisse.md | 72 | fond de caisse (paramétrage + saisie) | indetermine | comptabilite, paiement | oui | non | non | non | non | procedure |
| 139 | envoyer-les-codes-dacces-de-lespace-client-votre-client.md | 49 | — (page sans contenu substantif, résidu de gabarit de navigation) | indetermine | — | non | non | non | non | non | autre |
| 140 | envoyer-piece-commerciale-client-avec-piece-jointe.md | 48 | — (page sans contenu substantif, résidu de gabarit de navigation) | indetermine | — | non | non | non | non | non | autre |
| 141 | envoyer-une-piece-commerciale-exemple-facture-devis-relance-etc-par-mail-au-client.md | 58 | pièce commerciale (envoi par mail) | indetermine | communication, documents | oui | non | non | non | non | procedure |
| 142 | espace-client.md | 108 | photo (prise depuis rendez-vous, porte-documents) | chantier-intervention | photos, mobile | oui | non | non | non | non | procedure |
| 143 | evolutions-plage-de-dates-au-niveau-des-pieces-commerciales.md | 194 | filtre de dates (pièces commerciales, évolution infra) | indetermine | reporting, documents | non | non | non | oui | oui | faq_depannage |
| 144 | export.md | 231 | exports (catégorie, index) | indetermine | reporting, documents | oui | non | non | non | non | reference_configuration |
| 145 | exporter-affaires-utilisateur.md | 44 | export affaires (par utilisateur) | indetermine | reporting | oui | non | non | non | non | procedure |
| 146 | exporter-chiffre-daffaires-origine-de-contact.md | 53 | export CA (origine de contact) | indetermine | reporting, crm | oui | non | non | non | non | procedure |
| 147 | exporter-ecritures-de-gestion-commerciale-logiciel-de-comptabilite.md | 218 | export écritures comptables | facturation | comptabilite, integrations | oui | non | non | non | oui | procedure |
| 148 | exporter-les-commandes.md | 44 | export commandes | achat | reporting, comptabilite | oui | non | non | non | non | procedure |
| 149 | exports-des-services.md | 81 | export services (contrats) | chantier-intervention | reporting, geolocalisation, planning | oui | non | non | non | non | procedure |
| 150 | extrabat-today-telechargeable-sur-lapple-store.md | 156 | application Extrabat Today (téléchargement, géolocalisation RDV) | chantier-intervention | mobile, geolocalisation, communication | non | non | non | non | non | marketing_dans_aide |
| 151 | extrabat-today-version-3-5-nouvelles-fonctionnalites.md | 1131 | application Extrabat Today v3.5 (nouveautés) | chantier-intervention | mobile, photos, offline | non | non | non | oui | non | marketing_dans_aide |
| 152 | extradoc-lapplication-de-stockage-des-documents.md | 103 | application ExtraDoc (GED mobile) | indetermine | mobile, documents, permissions | non | non | non | non | non | definitionnel |
| 153 | faire-apparaitre-la-carte-sur-la-page-daccueil-du-client.md | 132 | géolocalisation (carte fiche client) | indetermine | geolocalisation, crm | oui | non | non | non | non | procedure |
| 154 | faire-emailing.md | 44 | — (page sans contenu substantif, résidu de gabarit de navigation) | indetermine | — | non | non | non | non | non | autre |
| 155 | faire-etiquettes-articles.md | 100 | étiquettes articles (export/impression) | indetermine | catalogue, documents | oui | non | non | non | oui | procedure |
| 156 | faire-remise-banque-despeces.md | 68 | remise en banque (espèces) | facturation | paiement, comptabilite | oui | non | non | non | non | procedure |
| 157 | faire-retour-article-linterface-de-caisse.md | 49 | retour article (interface de caisse, avoir) | achat | gestion_stock, paiement | oui | oui | non | non | non | procedure |
| 158 | faire-retour-materiel-garantie.md | 105 | retour matériel (garantie, SAV) | chantier-intervention | gestion_stock, documents | oui | non | oui | non | non | procedure |
| 159 | faire-un-devis.md | 138 | devis (création) | devis | catalogue, documents | oui | non | non | non | non | procedure |
| 160 | faire-un-inventaire.md | 195 | inventaire (stock) | indetermine | gestion_stock, recherche | oui | non | non | non | non | procedure |
| 161 | faites-le-test-avez-vous-les-bons-reflexes-extrabat.md | 266 | bonnes pratiques (auto-diagnostic d'utilisation) | indetermine | crm, catalogue, mobile | non | non | non | non | non | marketing_dans_aide |
| 162 | fichier-e-mail-jour.md | 73 | adresse e-mail client (contrôle qualité fichier) | indetermine | crm, validation | oui | non | oui | non | non | definitionnel |
| 163 | filtrer-sav-contrats-de-services-code-postal.md | 53 | filtre SAV/contrats (code postal) | chantier-intervention | recherche, geolocalisation | oui | non | non | non | non | procedure |
| 164 | fixer-taches-haut-planning.md | 53 | en-tête planning (figer) | indetermine | planning | oui | non | non | non | non | procedure |
| 165 | forcer-la-synchronisation-de-mes-rendez-vous-a-venir.md | 91 | synchronisation agenda (forcer) | indetermine | mobile, integrations | oui | non | non | non | oui | faq_depannage |
| 166 | fusionner-des-fournisseurs.md | 68 | fournisseurs (fusion doublons) | achat | catalogue, validation | oui | non | non | non | non | procedure |
| 167 | fusionner-deux-fiches-clients.md | 139 | fiche client (fusion/doublons) | indetermine | crm, documents | oui | non | non | non | non | procedure |
| 168 | geolocalisation.md | 132 | géolocalisation (carte fiche client) | indetermine | geolocalisation, crm | oui | non | non | non | non | procedure |
| 169 | gerer-les-doublons-dans-les-bases-clients-prospects.md | 105 | doublons clients/prospects (gestion) | indetermine | crm, recherche | oui | non | non | non | non | procedure |
| 170 | gerer-ses-parametres-utilisateurs-dans-lapplication-extrabat-today.md | 178 | paramètres utilisateur (application Extrabat Today) | indetermine | mobile, personnalisation, photos | oui | non | non | non | non | procedure |
| 171 | gestion-commerciale.md | 754 | signature électronique (Oodrive Sign) | indetermine | documents, securite_compte, notifications | oui | non | oui | non | non | procedure |
| 172 | gestion-commerciale/impression.md | 190 | impression (bug plugin Firefox, contournement) | indetermine | documents | oui | non | non | oui | oui | faq_depannage |
| 173 | gestion-commerciale/page/7.md | 212 | facture d'acompte (commande divisée) | facturation | paiement, documents | oui | oui | non | non | non | procedure |
| 174 | gestion-consentement.md | 583 | gestion du consentement RGPD (campagnes emailing) | indetermine | conformite_reglementaire, communication, crm | oui | oui | oui | oui | non | politique_legale |
| 175 | historique-ventes-gestion-commerciale.md | 93 | historique des ventes (client) | indetermine | reporting, crm | oui | non | non | non | non | procedure |
| 176 | il-est-temps.md | 152 | — (billet éditorial/motivationnel, sans contenu instructif) | indetermine | — | non | non | non | non | non | marketing_dans_aide |
| 177 | imprimer-des-etiquettes-articles-suite-a-un-bon-de-reception.md | 114 | étiquettes articles (impression via Excel/Word, bon de réception) | achat | catalogue, documents | oui | non | non | non | non | procedure |
| 178 | imprimer-plusieurs-factures-seule.md | 66 | liste de factures (impression en masse) | facturation | documents, reporting | oui | non | non | non | non | procedure |
| 179 | index.md | 535 | — (page d'accueil du centre d'aide, flux d'articles hétérogène) | indetermine | documents, communication | non | non | non | non | non | autre |
| 180 | infos.md | 292 | financement client (partenariat Franfinance) | devis | paiement, documents, conformite_reglementaire | oui | non | non | oui | non | marketing_dans_aide |
| 181 | inserer-la-date-du-jour-dans-un-modele-de-courrier-cree-sous-word.md | 45 | date du jour (modèle courrier Word) | indetermine | documents, personnalisation | oui | non | non | non | non | reference_configuration |
| 182 | inserer-ligne-dans-devis-commande-facture.md | 73 | éditeur de style (devis/commande/facture) | indetermine | personnalisation, documents | oui | non | non | non | non | reference_configuration |
| 183 | interface-de-caisse.md | 83 | interface de caisse (sélections produits) | indetermine | catalogue | oui | non | non | oui | non | procedure |
| 184 | interface-extrabat-beltys.md | 57 | intégration Beltys (Drive, publication article) | indetermine | integrations, catalogue | oui | non | non | oui | non | procedure |
| 185 | jai-plusieurs-agences-plusieurs-modes-de-reglements-carte-bleue-especes.md | 65 | modes de règlement (multi-agences, interface caisse) | facturation | paiement, personnalisation | oui | non | non | non | non | procedure |
| 186 | je-n-arrive-pas-a-imprimer-sous-firefox.md | 190 | impression (bug plugin Firefox, contournement) | indetermine | documents | oui | non | non | oui | oui | faq_depannage |
| 187 | je-narrive-pas-a-noter-un-code-client-dans-la-fiche-contact.md | 55 | code client (conflit, doublon) | indetermine | crm, validation | oui | non | oui | non | oui | faq_depannage |
| 188 | je-ne-peux-pas-modifier-mon-agenda.md | 61 | agenda (modification RDV, sélection utilisateur) | indetermine | planning, permissions | non | non | oui | non | oui | faq_depannage |
| 189 | je-saisis-mon-code-postal-ou-ma-ville.md | 37 | code postal/ville (autocomplétion, fiche contact) | indetermine | — | non | non | non | non | non | definitionnel |
| 190 | je-veux-changer-le-statut-de-mon-intervention-sav-ou-services-dans-extrabat-today.md | 80 | statut intervention (SAV/Services, application Today) | chantier-intervention | mobile, planning | oui | oui | non | non | non | procedure |
| 191 | je-veux-creer-une-alerte-planning.md | 143 | alerte planning (widget, texte d'alerte) | chantier-intervention | notifications, planning | oui | non | non | non | non | procedure |
| 192 | je-veux-envoyer-des-mails-a-partir-dextrabat-mais-avec-ma-boite-mail.md | 232 | configuration SMTP (boîte mail personnalisée) | indetermine | integrations, communication | oui | non | oui | oui | non | procedure |
| 193 | je-veux-exporter-sous-excell-mes-factures-et-reglements.md | 40 | export factures/règlements (Excel) | facturation | reporting, comptabilite | oui | non | non | non | non | procedure |
| 194 | je-veux-faire-la-liaison-dextrabat-piscines-avec-mon-logiciel-danalyse-de-leau-ocediciel-actisoft-testo.md | 206 | intégration logiciel d'analyse de l'eau (Ocediciel/Actisoft/Test'o) | chantier-intervention | integrations, documents | oui | non | non | oui | oui | procedure |
| 195 | je-veux-faire-un-avoir.md | 75 | avoir (création, transformation facture) | facturation | documents, paiement | oui | oui | non | non | non | procedure |
| 196 | je-veux-geolocaliser-ma-photo-et-annoter-ma-photo.md | 93 | photo (annotation, géolocalisation, Extrabat Today) | chantier-intervention | photos, geolocalisation, mobile | oui | non | non | non | non | procedure |
| 197 | je-veux-imprimer-une-liste-des-factures.md | 32 | liste factures (impression) | facturation | documents, reporting | oui | non | non | non | non | procedure |
| 198 | je-veux-mettre-a-jour-mes-coordonnees-gps-dans-la-fiche-extrabat-a-partir-dextrabat-today.md | 146 | coordonnées GPS (mise à jour depuis Extrabat Today) | chantier-intervention | geolocalisation, mobile | oui | non | non | non | non | procedure |
| 199 | je-veux-personnaliser-mes-preferences-utilisateurs.md | 192 | préférences utilisateur (personnalisation globale) | indetermine | personnalisation, permissions, notifications | oui | non | non | non | non | reference_configuration |
| 200 | je-veux-prendre-un-rendez-vous.md | 179 | rendez-vous (prise, plusieurs méthodes) | indetermine | planning, mobile, communication | oui | non | non | non | non | procedure |
| 201 | je-veux-prendre-une-photo-avec-extrabat-today.md | 108 | photo (prise depuis rendez-vous, porte-documents) | chantier-intervention | photos, mobile | oui | non | non | non | non | procedure |
| 202 | je-veux-prevenir-de-mon-retard-via-lapplication-extrabat-today.md | 125 | retard (notification client, Extrabat Today) | chantier-intervention | mobile, notifications, geolocalisation | oui | non | oui | oui | non | procedure |
| 203 | je-veux-rembourser-un-client-en-especes-par-linterface-de-caisse.md | 150 | remboursement client (espèces, interface caisse) | achat | paiement, gestion_stock | oui | non | oui | oui | non | procedure |
| 204 | je-veux-rentrer-un-rapport-dintervention-sur-extrabat-today.md | 194 | rapport d'intervention (Extrabat Today) | chantier-intervention | mobile, offline, documents | oui | non | non | non | oui | procedure |
| 205 | je-veux-retrouver-un-client-par-son-numero-de-telephone.md | 48 | recherche client (par téléphone) | indetermine | recherche, crm | oui | non | non | non | non | procedure |
| 206 | je-veux-voir-mon-debourse-a-partir-dun-devis.md | 136 | déboursé (devis, répartition par type d'article) | devis | catalogue, reporting | oui | non | non | non | non | procedure |
| 207 | la-gestion-du-changement.md | 136 | — (billet éditorial sur la conduite du changement, sans contenu produit) | indetermine | — | non | non | non | non | non | marketing_dans_aide |
| 208 | la-saisie-des-temps-sur-extrabat-today.md | 113 | saisie des temps (Extrabat Today) | chantier-intervention | mobile, planning | oui | non | non | non | non | procedure |
| 209 | la-signature-electronique.md | 754 | signature électronique (Oodrive Sign) | indetermine | documents, securite_compte, notifications | oui | non | oui | non | non | procedure |
| 210 | le-nom-du-client-napparait-pas-dans-lagenda.md | 106 | nom client (affichage agenda, champ objet/notes) | indetermine | crm, planning | oui | non | oui | non | non | faq_depannage |
| 211 | le-rgpd-tout-savoir-sur-le-reglement-general-sur-la-protection-des-donnees.md | 189 | RGPD (droits utilisateurs, gestion données personnelles) | indetermine | conformite_reglementaire, crm, securite_compte | oui | non | oui | oui | non | politique_legale |
| 212 | le-temps-cest-de-largent.md | 32 | — (billet éditorial, renvoi vers article externe) | indetermine | — | non | non | non | non | non | marketing_dans_aide |
| 213 | le-widjet-meteo-refait-son-apparition-pour-noel.md | 72 | widget météo (page d'accueil) | indetermine | personnalisation | oui | non | non | non | non | procedure |
| 214 | les-astuces-extrabat-gagner-du-temps.md | 150 | astuces (gain de temps, liste transversale) | indetermine | recherche, mobile, personnalisation | non | non | non | non | non | reference_configuration |
| 215 | les-bonnes-pratiques-a-adopter.md | 330 | bonnes pratiques (saisie, sécurité, plugins) | indetermine | securite_compte, personnalisation, catalogue | non | non | oui | oui | non | reference_configuration |
| 216 | les-bonnes-pratiques-avant-de-faire-son-inventaire-de-fin-dexercice.md | 235 | inventaire fin d'exercice (bonnes pratiques préparatoires) | indetermine | gestion_stock, comptabilite | oui | non | non | non | non | procedure |
| 217 | les-bonnes-pratiques.md | 2916 | — (page catégorie « bonnes pratiques », agrégat de plusieurs articles dupliqués) | indetermine | documents, communication | oui | non | oui | non | non | autre |
| 218 | les-bonnes-regles-afin-de-creer-gerer-son-planning-chantier.md | 193 | planning chantier (création/gestion, bonnes règles) | chantier-intervention | planning, documents | oui | oui | oui | non | non | procedure |
| 219 | les-differentes-facons-denvoyer-un-devis-dans-extrabat.md | 172 | devis (envoi, méthodes multiples) | devis | communication, documents | oui | non | oui | non | non | procedure |
| 220 | les-formations-gratuites-dextrabat-inscrivez-vous.md | 163 | — (formations gratuites, promotion ateliers découverte) | indetermine | — | non | non | non | non | non | marketing_dans_aide |
| 221 | les-raccourcis-du-moteur-de-recherche.md | 224 | raccourcis (moteur de recherche) | indetermine | recherche, catalogue | oui | non | non | non | non | reference_configuration |
| 222 | les-rapports-dintervention-et-les-signatures-sur-extrabat-today.md | 210 | rapports d'intervention et signatures (Extrabat Today) | chantier-intervention | mobile, offline, notifications | non | non | non | non | non | definitionnel |
| 223 | lettrer-payer-facture.md | 84 | lettrage (facture/avoir) | facturation | paiement, comptabilite | oui | oui | non | non | non | procedure |
| 224 | lire-mediter-par-la-suite.md | 28 | — (billet éditorial, renvoi vers dossier stratégie externe) | indetermine | — | non | non | non | non | non | marketing_dans_aide |
| 225 | logiciel-extrabat-comptabilite-comptatible-fec.md | 124 | FEC (Fichier des Écritures Comptables, conformité) | facturation | conformite_reglementaire, comptabilite | oui | oui | non | oui | non | politique_legale |
| 226 | lorganisation-cest-maintenant.md | 274 | — (billet éditorial/motivationnel sur l'organisation, sans procédure produit) | indetermine | — | non | non | non | non | non | marketing_dans_aide |
| 227 | ma-piece-commerciale-est-illisible-a-limpression-sous-firefox.md | 159 | impression illisible (bug polices Firefox) | indetermine | documents | oui | non | non | non | oui | faq_depannage |
| 228 | me-suis-trompe-de-type-de-reglement-especes-carte-bleue-cheques.md | 120 | règlement (correction erreur de type, contrepasser) | facturation | paiement, comptabilite, conformite_reglementaire | oui | oui | non | oui | oui | faq_depannage |
| 229 | messagerie-pro-buzzee-mail.md | 293 | intégration Buzzee Mail (messagerie professionnelle) | indetermine | integrations, communication, crm | oui | non | non | non | non | marketing_dans_aide |
| 230 | mettre-a-jour-base-articles.md | 62 | articles (mise à jour en masse) | indetermine | catalogue | oui | non | non | non | non | procedure |
| 231 | mettre-a-jour-la-duree-de-garantie-dun-article.md | 60 | durée de garantie (article) | indetermine | catalogue | oui | non | oui | non | non | procedure |
| 232 | mettre-a-jour-mon-stock-sans-faire-dinventaire.md | 45 | stock (mise à jour via bon de réception) | achat | gestion_stock | oui | non | non | non | non | procedure |
| 233 | mettre-a-jour-prix-dachat-via-devis-commande.md | 60 | prix d'achat (mise à jour via devis/commande) | devis | catalogue, tarification | oui | non | non | non | non | procedure |
| 234 | mettre-a-jour-ses-tarifs-darticles-via-la-fonction-dexport-import.md | 163 | tarifs articles (mise à jour export/import CSV) | indetermine | catalogue, tarification, documents | oui | non | oui | oui | oui | procedure |
| 235 | mettre-photo-dans-le-porte-doc-dun-dossier-client-la-mettre-en-page-daccueil.md | 17 | — (page sans contenu substantif, question sans réponse) | indetermine | — | non | non | non | non | non | autre |
| 236 | mettre-raccourci-sur-sa-tablette-ou-smartphone-android.md | 98 | raccourci écran d'accueil (Android) | indetermine | mobile | oui | non | non | non | non | procedure |
| 237 | mettre-raccourci-sur-son-ecran-daccueil-sur-smartphone-ou-tablette-apple.md | 46 | raccourci écran d'accueil (Apple) | indetermine | mobile | oui | non | non | non | non | procedure |
| 238 | mettre-un-article-en-option.md | 134 | article en option (devis/commande/facture) | devis | catalogue, documents | oui | oui | oui | non | non | procedure |
| 239 | mettre-une-image-dans-sa-signature-utilisateur.md | 47 | signature utilisateur (image) | indetermine | personnalisation, documents | oui | non | non | non | non | procedure |
| 240 | mieux-gerer-ses-emails-professionnels.md | 532 | — (conseils génériques de gestion des e-mails professionnels, sans lien produit) | indetermine | — | non | non | non | non | non | marketing_dans_aide |
| 241 | migration-du-support-vers-zendesk.md | 503 | support/assistance (migration vers Zendesk) | indetermine | support_editeur, securite_compte, communication | oui | non | oui | oui | non | reference_configuration |
| 242 | mise-a-jour-des-nomenclatures.md | 50 | nomenclatures (mise à jour) | indetermine | catalogue | oui | non | non | non | non | procedure |
| 243 | mise-a-jour-nouvelle-interface-pour-la-creation-de-la-fiche-client.md | 1731 | fiche client (interface de création, champs particulier/professionnel) | indetermine | crm, personnalisation, conformite_reglementaire | non | non | oui | non | non | reference_configuration |
| 244 | mise-jour-des-catalogues-fournisseurs.md | 129 | catalogues fournisseurs (mise à jour tarifs, widget) | achat | catalogue, tarification, notifications | oui | non | non | non | non | procedure |
| 245 | mise-jour-prix-dachat-catalogue.md | 132 | prix d'achat catalogue (mise à jour via widget) | achat | catalogue, tarification | oui | non | non | oui | non | procedure |
| 246 | modifier-coordonnees-de-iban-devis-commandes-factures.md | 126 | IBAN (coordonnées bancaires, pièces commerciales) | indetermine | paiement, documents | oui | non | non | oui | non | procedure |
| 247 | module-sms.md | 252 | module SMS (confirmation RDV) | indetermine | notifications, communication, tarification | oui | non | non | oui | non | procedure |
| 248 | mon-client-ne-peut-pas-aller-sur-son-espace-client.md | 97 | espace client (accès, mot de passe) | indetermine | securite_compte, crm | oui | non | non | non | oui | faq_depannage |
| 249 | mon-client-regle-sa-facture-avec-plusieurs-modes-de-reglement-differents.md | 127 | règlement facture (espace client, multi-modes) | facturation | paiement, comptabilite | oui | oui | non | non | non | procedure |
| 250 | mon-email-revient-delivery-alors-que-ladresse-mail-bonne-fonctionne-autre-mesasagerie.md | 76 | email rejeté (SPF, domaine) | indetermine | integrations, securite_compte | oui | non | non | oui | oui | faq_depannage |
| 251 | mot-de-passe-oublie.md | 320 | mot de passe (oubli, réinitialisation) | indetermine | securite_compte, permissions | oui | non | oui | non | oui | faq_depannage |
| 252 | moteur-de-recherche-plus-rapide.md | 57 | moteur de recherche (optimisation, critères) | indetermine | recherche | oui | non | non | non | non | reference_configuration |
| 253 | mots-de-passe-nouvelle-mesure-de-securite.md | 221 | mot de passe (nouvelle mesure de sécurité, critères) | indetermine | securite_compte | oui | non | oui | non | oui | politique_legale |
| 254 | ne-peux-modifier-mode-de-reglement.md | 194 | règlement (impossibilité de modifier, contrepasser, loi anti-fraude 2018) | facturation | paiement, conformite_reglementaire, comptabilite | oui | oui | oui | oui | oui | politique_legale |
| 255 | ne-veux-voir-mode-de-reglement-exemple-traite-liste-de-relances-clients.md | 62 | mode de règlement (exclusion de la liste des relances) | facturation | paiement, personnalisation | oui | non | non | non | non | procedure |
| 256 | nomenclature-dynamique.md | 120 | nomenclature dynamique (création, devis) | devis | catalogue, personnalisation, recherche | oui | non | non | non | non | procedure |
| 257 | non-classe.md | 541 | checklist fin d'année (clôture comptable) | facturation | comptabilite, documents, communication | oui | non | oui | oui | non | procedure |
| 258 | nouveau-service-extrabat.md | 253 | — (actualité produit, annonce de nouveautés à venir) | indetermine | documents | non | non | non | non | non | marketing_dans_aide |
| 259 | nouvelle-fonctionnalite-les-produits-precurseurs-dexplosifs.md | 136 | produits précurseurs d'explosifs (signalement réglementaire) | indetermine | conformite_reglementaire, catalogue | oui | non | oui | non | non | politique_legale |
| 260 | nouvelle-fonctionnalite-modele-courrier.md | 106 | modèle de courrier (import Word/OpenOffice, marqueurs) | indetermine | documents, personnalisation | oui | non | oui | non | non | procedure |
| 261 | nouvelle-fonctionnalites-sur-les-fiches-sav.md | 173 | fiche SAV (retour fournisseur) | chantier-intervention | gestion_stock, documents, communication | oui | non | non | non | non | procedure |
| 262 | nouvelle-obligation-de-lurssaf-renseignement-du-numero-sap-de-lintervenant.md | 191 | numéro SAP (obligation URSSAF) | indetermine | conformite_reglementaire | oui | non | oui | non | non | politique_legale |
| 263 | optimiser-ses-rendez-vous-par-zone-geographique.md | 108 | rendez-vous (optimisation tournée, proximité géographique) | chantier-intervention | geolocalisation, planning | non | non | non | non | non | definitionnel |
| 264 | parametrage.md | 222 | synchronisation agenda (CalDAV, smartphone Apple) | indetermine | mobile, integrations | oui | non | non | non | oui | procedure |
| 265 | parametrer-action.md | 67 | action (paramétrage, réponses) | indetermine | crm, personnalisation | oui | non | non | non | non | procedure |
| 266 | parametrer-firefox-pour-lenregistrement-des-fichiers.md | 45 | paramétrage navigateur (Firefox, téléchargements) | indetermine | — | oui | non | non | non | non | reference_configuration |
| 267 | parametrer-journal-de-caisse-rentrer-fond-de-caisse.md | 72 | journal de caisse (paramétrage, fond de caisse) | indetermine | comptabilite, paiement | oui | non | non | non | non | procedure |
| 268 | parametrer-son-livre-de-caisse-electronique.md | 94 | livre de caisse électronique (paramétrage, plan comptable) | indetermine | comptabilite, paiement | oui | non | non | non | non | procedure |
| 269 | parametrer-son-smtp-extrabat-avec-son-compte-gmail.md | 528 | configuration SMTP (Gmail) | indetermine | integrations, communication, securite_compte | oui | non | non | oui | non | procedure |
| 270 | passage-oblige.md | 172 | fiche client (bonnes pratiques de saisie, suivi statistique) | indetermine | crm, reporting, planning | oui | non | non | non | non | reference_configuration |
| 271 | passer-une-commande-fournisseur.md | 372 | commande fournisseur (création) | achat | gestion_stock, documents, tarification | oui | non | non | non | non | procedure |
| 272 | personnalisez-votre-recherche-dans-le-moteur-de-recherche.md | 52 | moteur de recherche (personnalisation nom/prénom) | indetermine | recherche, personnalisation | oui | non | non | non | non | reference_configuration |
| 273 | plannification-plus-rapide.md | 62 | planification chantier (planning, RDV rapide) | chantier-intervention | planning | oui | non | non | non | non | procedure |
| 274 | planning-chantier.md | 193 | planning chantier (création/gestion, bonnes règles) | chantier-intervention | planning, documents | oui | oui | oui | non | non | procedure |
| 275 | pourquoi-mes-mails-arrivent-dans-les-spams.md | 211 | emails en spam (diagnostic, préconisations) | indetermine | communication, integrations, securite_compte | oui | non | non | oui | oui | faq_depannage |
| 276 | pratiquer-augmentation-dune-commande-a-renouveler-type-contrat-de-services.md | 46 | commande à renouveler (augmentation tarifaire, contrat services) | facturation | tarification, automatisation | oui | non | non | non | non | procedure |
| 277 | prendre-rendez-vous-commercial.md | 48 | — (page sans contenu substantif, résidu de gabarit de navigation) | indetermine | — | non | non | non | non | non | autre |
| 278 | preparez-votre-offre-chauffage.md | 110 | — (conseils commerciaux saisonniers, chauffage piscine) | indetermine | — | non | non | non | non | non | marketing_dans_aide |
| 279 | procedure-dun-rapport-dintervention-dun-technicien.md | 211 | rapport d'intervention (technicien, mobile) | chantier-intervention | mobile, photos, planning | oui | oui | non | non | non | procedure |
| 280 | rajouter-un-fournisseur-a-un-article.md | 56 | fournisseur (ajout à un article) | indetermine | catalogue, tarification | oui | non | non | non | non | procedure |
| 281 | rassurez-vos-clients-en-cours-de-construction.md | 120 | — (conseil relationnel/communication client, sans procédure produit) | chantier-intervention | — | non | non | non | non | non | marketing_dans_aide |
| 282 | realiser-un-emailing.md | 244 | emailing (campagne, éditeur, ciblage) | indetermine | marketing_et_communication, crm, personnalisation | oui | non | non | non | non | procedure |
| 283 | recevoir-tableau-de-bord-mail.md | 54 | tableau de bord (envoi par email, périodicité) | indetermine | reporting, notifications | oui | non | non | non | non | procedure |
| 284 | rechercher-article-inactif-ou-desactive.md | 75 | article inactif (recherche) | indetermine | catalogue, recherche | oui | non | non | non | non | procedure |
| 285 | rechercher-dans-le-logiciel.md | 49 | moteur de recherche (champs disponibles) | indetermine | recherche | non | non | non | non | non | reference_configuration |
| 286 | rechercher-plus-precis.md | 108 | moteur de recherche (recherche précise, filtre articles) | indetermine | recherche, catalogue | oui | non | non | non | non | reference_configuration |
| 287 | rechercher-un-article.md | 71 | recherche article (filtre « commence par ») | indetermine | recherche, catalogue | oui | non | non | non | non | procedure |
| 288 | recuperer-client-mis-erreur-statut-corbeille.md | 54 | client (récupération depuis corbeille, erreur) | indetermine | crm, recherche | oui | oui | non | non | oui | faq_depannage |
| 289 | relance-des-devis-par-sms.md | 221 | relance devis (SMS, réponse client) | devis | notifications, communication, crm | oui | oui | non | non | non | procedure |
| 290 | relier-une-notice-etou-un-eclate-a-un-article-dans-un-dossier-client.md | 77 | notice technique/éclaté (liaison à un article) | indetermine | documents, catalogue | oui | non | non | non | non | procedure |
| 291 | renommer-un-ouvrage.md | 88 | ouvrage (renommage) | indetermine | personnalisation, crm | oui | non | non | non | non | procedure |
| 292 | rentabilite-des-canaux-de-publicites.md | 85 | rentabilité canaux de publicité (statistiques) | indetermine | reporting, marketing_et_communication | oui | non | non | non | non | procedure |
| 293 | rentrer-son-objectif-mensuel-de-chiffre-daffaire.md | 82 | objectif CA mensuel (paramétrage, widget) | indetermine | reporting, comptabilite | oui | non | non | non | non | procedure |
| 294 | rgpd.md | 189 | RGPD (droits utilisateurs, gestion données personnelles) | indetermine | conformite_reglementaire, crm, securite_compte | oui | non | oui | oui | non | politique_legale |
| 295 | sachez-vous-servir-des-etoiles.md | 125 | raccourcis moteur de recherche (astérisques) | indetermine | recherche, catalogue | oui | non | non | non | non | reference_configuration |
| 296 | saisir-titre-a-facture-via-linterface-de-caisse.md | 26 | titre facture (interface de caisse) | facturation | personnalisation | oui | non | non | non | non | procedure |
| 297 | salon-de-lyon-2014-du-18-au-21-novembre-2014-six-conseils-afin-de-reussir-sa-visite-source-actu-piscine.md | 36 | — (annonce événementielle, salon professionnel) | indetermine | — | non | non | non | non | non | marketing_dans_aide |
| 298 | sav.md | 210 | rapports d'intervention et signatures (Extrabat Today) | chantier-intervention | mobile, offline, notifications | non | non | non | non | non | definitionnel |
| 299 | savoir-se-servir-des-raccourcis-clavier-ctrl-f-ctrl-p.md | 44 | — (page sans contenu substantif, résidu de gabarit de navigation) | indetermine | — | non | non | non | non | non | autre |
| 300 | securisez-vos-mots-de-passe.md | 75 | mot de passe (sécurisation, conseils) | indetermine | securite_compte | oui | non | non | non | non | reference_configuration |
| 301 | securite-fr.md | 320 | mot de passe (oubli, réinitialisation) | indetermine | securite_compte, permissions | oui | non | oui | non | oui | faq_depannage |
| 302 | securite.md | 320 | mot de passe (oubli, réinitialisation) | indetermine | securite_compte, permissions | oui | non | oui | non | oui | faq_depannage |
| 303 | selectionner-plusieurs-articles-dans-une-piece-commerciale.md | 23 | sélection multiple d'articles (pièce commerciale) | indetermine | documents | oui | non | non | non | non | procedure |
| 304 | services-contrats-dentretien.md | 210 | rapports d'intervention et signatures (Extrabat Today) | chantier-intervention | mobile, offline, notifications | non | non | non | non | non | definitionnel |
| 305 | si-vous-narrivez-pas-imprimer.md | 44 | impression (extension JS Print, autoriser accès) | indetermine | documents | oui | non | non | non | oui | faq_depannage |
| 306 | sms.md | 221 | relance devis (SMS, réponse client) | devis | notifications, communication, crm | oui | oui | non | non | non | procedure |
| 307 | statistiques-origines-par-annee.md | 81 | statistiques origines de contact (par année) | indetermine | reporting, crm | oui | non | non | non | non | procedure |
| 308 | statistiques.md | 714 | CA restant à facturer (rapport) | facturation | reporting, documents, notifications | oui | non | oui | oui | oui | reference_configuration |
| 309 | supprimer-ecritures-comptabilite.md | 27 | écritures comptables (suppression, sauvegarde préalable) | facturation | comptabilite | oui | non | oui | non | non | procedure |
| 310 | supprimer-prospect-client.md | 86 | client/prospect (suppression impossible, corbeille) | indetermine | crm | oui | oui | non | oui | non | procedure |
| 311 | supprimer-un-compte-utilisateur.md | 49 | compte utilisateur (suppression d'accès) | indetermine | permissions, securite_compte | oui | non | non | non | non | procedure |
| 312 | supprimer-un-devis-ou-une-facture.md | 43 | devis/commande (suppression) | devis | documents | oui | non | non | oui | non | procedure |
| 313 | supprimer-une-fiche-ou-un-dossier-client.md | 75 | fiche client (suppression, corbeille) | indetermine | crm | oui | oui | non | oui | non | procedure |
| 314 | synchronisation-avec-outlook.md | 33 | synchronisation Outlook (non supportée officiellement) | indetermine | integrations | non | non | non | oui | oui | faq_depannage |
| 315 | synchroniser-mon-agenda-avec-mon-telephone-sous-android.md | 360 | synchronisation agenda (CalDAV/mobile) | indetermine | integrations, mobile | oui | non | non | non | oui | procedure |
| 316 | synchroniser-mon-agenda-sur-iphone-ou-ipad.md | 222 | synchronisation agenda (CalDAV, smartphone Apple) | indetermine | mobile, integrations | oui | non | non | non | oui | procedure |
| 317 | synthese-rentabilite-dune-affaire.md | 85 | affaire (synthèse rentabilité) | indetermine | reporting, documents | oui | non | non | non | non | procedure |
| 318 | tablette-smartphone.md | 108 | photo (prise depuis rendez-vous, porte-documents) | chantier-intervention | photos, mobile | oui | non | non | non | non | procedure |
| 319 | tag/bibliotheque.md | 83 | bibliothèque (signature utilisateur, recherche transversale — agrégat) | indetermine | documents, recherche, personnalisation | oui | non | non | non | non | procedure |
| 320 | tag/commande.md | 212 | facture d'acompte (commande divisée) | facturation | paiement, documents | oui | oui | non | non | non | procedure |
| 321 | tag/courrier.md | 173 | modèle de courrier (création) | indetermine | documents, personnalisation, communication | oui | non | non | non | non | procedure |
| 322 | tag/creer-un-modele-de-courrier.md | 173 | modèle de courrier (création) | indetermine | documents, personnalisation, communication | oui | non | non | non | non | procedure |
| 323 | tag/export-2.md | 69 | export (articles, factures/règlements — agrégat) | indetermine | catalogue, reporting, comptabilite | oui | non | non | non | non | procedure |
| 324 | tag/inventaire.md | 188 | inventaire (stock) | indetermine | gestion_stock, recherche | oui | non | non | non | non | procedure |
| 325 | tag/moteur-de-recherche.md | 224 | raccourcis (moteur de recherche) | indetermine | recherche, catalogue | oui | non | non | non | non | reference_configuration |
| 326 | tag/outils.md | 167 | outils transversaux (création article, statistiques — agrégat) | indetermine | catalogue, reporting, crm | oui | non | non | non | non | procedure |
| 327 | tag/stock.md | 188 | inventaire (stock) | indetermine | gestion_stock, recherche | oui | non | non | non | non | procedure |
| 328 | totaux-dans-les-pieces-commerciales.md | 75 | sous-totaux (pièces commerciales) | indetermine | documents, personnalisation | oui | non | non | non | non | procedure |
| 329 | transferer-factures-de-vente-logiciel-de-comptabilite-extrabat.md | 13 | — (page sans contenu substantif, question sans réponse) | indetermine | — | non | non | non | non | non | autre |
| 330 | transfert-dun-article-dun-depot-a-un-autre.md | 90 | transfert de stock (entre dépôts) | indetermine | gestion_stock, permissions | oui | non | oui | oui | non | procedure |
| 331 | transformer-plusieurs-bl-en-seule-facture.md | 205 | pièces commerciales (regroupement BL en facture) | facturation | documents, gestion_stock | oui | oui | non | non | non | procedure |
| 332 | trouver-article-vendu-a-client.md | 92 | article vendu (recherche historique client) | indetermine | recherche, reporting | oui | non | non | non | non | procedure |
| 333 | tutorial-plage-de-date.md | 27 | plage de dates (recherche pièces commerciales, tutoriel vidéo) | indetermine | recherche | non | non | non | non | non | autre |
| 334 | un-nouveau-raccourci-dans-le-moteur-de-recherche-le-nom-du-client.md | 76 | raccourci recherche (tâches planning par client) | chantier-intervention | recherche, planning | oui | non | non | non | non | procedure |
| 335 | un-nouveau-widget-notifications.md | 76 | widget notifications (Extrabat Today) | chantier-intervention | notifications, mobile | oui | non | non | non | non | procedure |
| 336 | un-raccourci-f3-afin-de-consulter-rapidement-la-fiche-article.md | 213 | raccourci F3 (fiche article) | indetermine | catalogue, recherche | oui | non | non | non | non | reference_configuration |
| 337 | une-aide-a-la-vente-avec-la-simulation-de-financement-franfinance.md | 292 | financement client (partenariat Franfinance) | devis | paiement, documents, conformite_reglementaire | oui | non | non | oui | non | marketing_dans_aide |
| 338 | utiliser-le-copier-coller.md | 73 | copier-coller (articles, pièces commerciales) | indetermine | documents, catalogue | oui | non | non | non | non | procedure |
| 339 | veux-affecter-devis-facture-a-client.md | 122 | pièce commerciale (réaffectation à un autre client) | facturation | documents, crm | oui | non | oui | oui | non | procedure |
| 340 | veux-creer-article-directement-a-partir-dun-devis.md | 152 | article (création directe depuis devis) | devis | catalogue, comptabilite | oui | non | non | non | non | procedure |
| 341 | veux-creer-questions-complementaires.md | 126 | questions complémentaires (création) | indetermine | personnalisation, crm | oui | non | non | non | non | procedure |
| 342 | veux-regrouper-plusieurs-commandes-bons-de-livraison-seule-facture.md | 67 | commandes/BL (regroupement en facture) | facturation | documents, gestion_stock | oui | oui | non | non | non | procedure |
| 343 | veux-supprimer-facture.md | 57 | facture (suppression impossible, loi 2018) | facturation | conformite_reglementaire, comptabilite | oui | non | oui | oui | non | politique_legale |
| 344 | video.md | 398 | modèle de message (email personnalisé) | indetermine | communication, personnalisation, documents | oui | non | non | non | non | procedure |
| 345 | voir-valorisation-de-stock-a-date.md | 50 | valorisation de stock (export à date) | indetermine | gestion_stock, reporting | oui | non | non | non | non | procedure |
| 346 | votre-fichier-client-source-de-votre-business.md | 299 | — (argumentaire marketing sur la relance de devis et le fichier client) | devis | crm, communication, automatisation | non | non | non | non | non | marketing_dans_aide |
| 347 | widget-2.md | 76 | widget notifications (Extrabat Today) | chantier-intervention | notifications, mobile | oui | non | non | non | non | procedure |

## Contrôles mécaniques

- Documents traités / attendus : **347 / 347**. Écart au garde-fou (1670 − 1323 = 347) : nul.
- Numérotation : continue de 1 à 347, aucune rupture (vérifié par tri numérique de la colonne `#`, script Python).
- Doublons de `chemin_relatif` dans le tableau : **0** (vérifié mécaniquement, ensemble des 347 valeurs de chemin toutes distinctes).
- Correspondance ensembliste entre les 347 `chemin_relatif` du tableau et les 347 chemins du périmètre gelé (liste construite en §3, disque moins `analysis_exclusions`), y compris format de préfixe (`tag/...`, `gestion-commerciale/...`) : **identique**, vérifié par comparaison d'ensembles Python — 0 chemin manquant, 0 chemin en trop.
- Aucun chemin du tableau ne figure dans `analysis_exclusions` (`corpus_index.json`) : vérifié par intersection d'ensembles, **0 correspondance**.
- Les 10 fichiers préservés (`ANALYTICAL_EXCLUSION_PRESERVE`) sont tous présents et codés : `tag/bibliotheque.md` (#319), `tag/commande.md` (#320), `tag/courrier.md` (#321), `tag/creer-un-modele-de-courrier.md` (#322), `tag/export-2.md` (#323), `tag/inventaire.md` (#324), `tag/moteur-de-recherche.md` (#325), `tag/outils.md` (#326), `tag/stock.md` (#327), `gestion-commerciale/page/7.md` (#173).
- Colonnes : chaque ligne du tableau comporte exactement 12 colonnes de données (vérifié par split mécanique sur `|`, script Python sur les 347 lignes).
- `moment_parcours` : strictement dans le vocabulaire fermé `indetermine · demande · devis · achat · chantier-intervention · facturation`. Répartition : `indetermine` 213, `chantier-intervention` 47, `facturation` 45, `achat` 21, `devis` 18, `demande` 3 (aucune valeur hors vocabulaire).
- `capacites_transverses` : maximum observé par document = **3** (vérifié mécaniquement, aucune ligne ne dépasse), `—` (aucune capacité) sur 41 documents.
- `genre_documentaire` : les 347 valeurs se rattachent toutes aux racines du §4 (`procedure`, `definitionnel`, `reference_configuration`, `autre`, `politique_legale`, `faq_depannage`, `marketing_dans_aide`) — aucune racine nouvelle.
- `longueur_mots` : calculée mécaniquement pour les 347 documents avant lecture de contenu (script Python, méthode déclarée en tête de fichier) ; vérification a posteriori que les 347 valeurs du tableau correspondent exactement aux valeurs précalculées : **0 écart**.
- Agrégats ci-dessous recalculés directement depuis le tableau final par script mécanique, non recopiés des checkpoints.

## Agrégats

**Volume**
- 347 documents, 58 502 mots (méthode : suppression frontmatter YAML + `split()`, décrite en tête de fichier).
- Moyenne : 168,6 mots/document (min 13, max 2 916).
- Corpus le plus court en moyenne du dépôt (nettement en dessous d'InterFast, Sellsy, ProGBat) — cohérent avec son contexte éditorial WordPress/articles à plat annoncé par la mission.

**`moment_parcours` (347)**
| Valeur | Effectif |
|---|---|
| indetermine | 213 |
| chantier-intervention | 47 |
| facturation | 45 |
| achat | 21 |
| devis | 18 |
| demande | 3 |

**`genre_documentaire`, racines (347)**
| Racine | Effectif |
|---|---|
| procedure | 224 |
| reference_configuration | 32 |
| autre | 26 |
| marketing_dans_aide | 22 |
| faq_depannage | 19 |
| definitionnel | 13 |
| politique_legale | 11 |

**`capacites_transverses`, fréquence par valeur individuelle (une même ligne peut compter dans plusieurs valeurs)**
| Valeur | Effectif |
|---|---|
| documents | 86 |
| catalogue | 49 |
| crm | 41 |
| — (aucune) | 41 |
| personnalisation | 37 |
| mobile | 34 |
| communication | 33 |
| paiement | 32 |
| reporting | 32 |
| comptabilite | 32 |
| gestion_stock | 31 |
| planning | 30 |
| recherche | 30 |
| integrations | 27 |
| notifications | 26 |
| securite_compte | 25 |
| conformite_reglementaire | 20 |
| permissions | 17 |
| photos | 12 |
| tarification | 12 |
| geolocalisation | 9 |
| offline | 7 |
| validation | 4 |
| automatisation | 3 |
| marketing_et_communication | 2 |
| presence_en_ligne | 1 |
| support_editeur | 1 |

**`contenu_observable`, répartition oui/non sur les cinq champs (347 chacun, aucun `inconnu` employé)**
| Champ | oui | non |
|---|---|---|
| procedure | 288 | 59 |
| transition_objet | 33 | 314 |
| regle_ou_condition | 65 | 282 |
| contrainte_ou_limite | 58 | 289 |
| exception_ou_correction | 42 | 305 |

Aucune valeur `inconnu` n'a été utilisée : les 347 documents, même les plus courts ou les plus dégradés, ont permis un jugement honnête et tranché sur les cinq champs `contenu_observable` — soit le phénomène est observable, soit son absence est elle-même observable (silence documentaire net, pas ambiguïté de lecture).

## Cas mal représentés

- **25 documents sans contenu substantif** (7 % du corpus) : 23 résidus de gabarit WordPress (menu de navigation du blog, réseaux sociaux, pagination, suivis d'une chaîne hexadécimale répétée — probablement un artefact de cache ou de test — sans aucun contenu de réponse) ou questions sans réponse rédigée, codés `objet_principal = —`, tous les champs `contenu_observable = non`, `genre_documentaire = autre` : `astuce-le-raccourci-de-recherche.md` (#21), `cloturer-la-caisse.md` (#42), `comment-bien-parametrer-son-navigateur-internet-firefox.md` (#46), `comment-creer-sa-signature-le-logiciel-extrabat.md` (#51), `comment-donner-les-droits-utilisateur-consulter-etou-modifier.md` (#56), `comment-faire-retour-article-creer-avoir.md` (#66), `comment-fonctionne-lespace-client.md` (#68), `comment-geolocaliser-un-client-avec-myextrabat.md` (#71), `comment-mettre-jour-les-articles-par-famille-famille-ou-par-fournisseur.md` (#80), `comment-parametrer-la-synchronisation-de-son-smartphone-apple-avec-lagenda-extrabat.md` (#82), `comment-relier-notice-technique-article.md` (#88), `comment-rentrer-un-reglement-rapidement-sur-une-facture.md` (#89), `comment-reparer-son-navigateur-internet-firefox.md` (#90), `creer-client-via-linterface-de-caisse.md` (#107), `deplacer-plusieurs-articles-voire-familles-darticles.md` (#123), `enregistrer-paiement-multiple.md` (#133), `envoyer-les-codes-dacces-de-lespace-client-votre-client.md` (#139), `envoyer-piece-commerciale-client-avec-piece-jointe.md` (#140), `faire-emailing.md` (#154), `mettre-photo-dans-le-porte-doc-dun-dossier-client-la-mettre-en-page-daccueil.md` (#235), `prendre-rendez-vous-commercial.md` (#277), `savoir-se-servir-des-raccourcis-clavier-ctrl-f-ctrl-p.md` (#299), `transferer-factures-de-vente-logiciel-de-comptabilite-extrabat.md` (#329). Silence documentaire de la source, pas absence fonctionnelle : le titre de chacune de ces pages indique un sujet réel (mot de passe, synchronisation, retour article…) déjà couvert ailleurs dans le corpus par un article complet.
- **2 pages catégorie/index agrégeant du contenu dupliqué** : `index.md` (#179, page d'accueil du centre d'aide, digest hétérogène de plusieurs articles) et `les-bonnes-pratiques.md` (#217, 2916 mots, la plus longue du corpus) reproduisent en quasi-totalité le texte d'au moins dix autres documents déjà présents individuellement dans le périmètre (ex. `comment-creer-un-tiers-payant.md`, `je-veux-envoyer-des-mails-a-partir-dextrabat-mais-avec-ma-boite-mail.md`, `comment-parametrer-un-nouveau-logiciel-de-comptabilite-dans-extrabat.md`, `le-temps-cest-de-largent.md`, `lire-mediter-par-la-suite.md`, `la-gestion-du-changement.md`, `preparez-votre-offre-chauffage.md`, `rassurez-vos-clients-en-cours-de-construction.md`, `lorganisation-cest-maintenant.md`, `mieux-gerer-ses-emails-professionnels.md`, `votre-fichier-client-source-de-votre-business.md`). Codées d'après leur contenu réel (agrégat hétérogène), signalées ici pour que leur poids dans les agrégats de mots (2916 + 535 mots) ne soit pas interprété comme deux observations indépendantes supplémentaires.
- **26 groupes de doublons verbatim sous URL distincte, 60 documents concernés (17 % du corpus)** — chaque document reste une entrée distincte du corpus source (URL et titre propres) et a été lu et codé individuellement conformément à SCHEMA-LIGHT.md §7, mais le contenu est identique mot pour mot à un ou plusieurs autres documents du périmètre. Liste complète des groupes (numéro de ligne du tableau) :
  `#28≡#69` · `#18≡#104≡#127` · `#35≡#99≡#308` · `#22≡#105` · `#83≡#130` · `#4≡#183` · `#172≡#186` · `#142≡#201≡#318` · `#171≡#209` · `#17≡#151` · `#16≡#152` · `#39≡#257` · `#211≡#294` · `#251≡#301≡#302` · `#222≡#298≡#304` · `#289≡#306` · `#6≡#315` · `#264≡#316` · `#218≡#274` · `#52≡#344` · `#180≡#337` · `#335≡#347` · `#119≡#173≡#320` · `#160≡#324≡#327` · `#221≡#325` · `#108≡#321≡#322`.
  Cette redondance structurelle (articles republiés sous plusieurs URLs, pages catégorie WordPress dupliquant un article, migrations de contenu) gonfle mécaniquement les agrégats de mots et de valeurs `capacites_transverses`/`genre_documentaire` par rapport à un corpus sans répétition — à interpréter comme un artefact éditorial de la source, non comme une insistance produit.
- **Anomalie sur les fichiers préservés** : contrairement à la description de la mission selon laquelle les dix fichiers `ANALYTICAL_EXCLUSION_PRESERVE` porteraient un contenu introuvable ailleurs dans le corpus, **4 des 9 pages `/tag/`** (`tag/commande.md` #320, `tag/inventaire.md` #324, `tag/moteur-de-recherche.md` #325, `tag/stock.md` #327) se sont révélées être des doublons verbatim d'articles autonomes déjà présents dans le périmètre (respectivement `creer-une-facture-dacompte.md`/`gestion-commerciale/page/7.md`, `faire-un-inventaire.md` ×2, `les-raccourcis-du-moteur-de-recherche.md`). Trois autres pages `/tag/` (`tag/bibliotheque.md` #319, `tag/export-2.md` #323, `tag/outils.md` #326) sont des agrégats de deux à trois extraits d'articles existants plutôt qu'un contenu inédit. Seules `tag/courrier.md` (#321) et `tag/creer-un-modele-de-courrier.md` (#322) reproduisent un contenu qui n'existe qu'à une nuance textuelle près ailleurs (`creer-modele-de-courrier.md`, #108). Constat factuel, non un défaut de méthode LIGHT : la vérification d'unicité alléguée par la mission portait vraisemblablement sur l'absence de ces contenus dans les autres pages `/tag/` exclues (motif `ARCHIVE_TAXONOMIE`), pas sur l'ensemble du périmètre d'analyse.
- **213 documents (61 %) codés `moment_parcours = indetermine`** : cohérent avec un logiciel de gestion transversal (facturation, stock, CRM, planning, SAV, intégrations tierces) dont la majorité des articles portent sur une fonctionnalité ou un paramétrage sans ancrage à une étape précise du cycle devis → achat → chantier-intervention → facturation. Cas typiques : paramétrages techniques (SMTP, navigateur, raccourcis clavier), fonctionnalités transverses (recherche, permissions, RGPD), et les pages dégradées/agrégats ci-dessus, codées `indetermine` par défaut faute de valeur applicable.
- **3 documents seulement `demande`** : très peu de documents ancrent le contenu au stade de la prospection initiale — cohérent avec un corpus dominé par la gestion commerciale post-devis plutôt que par l'acquisition commerciale.
- **22 documents `marketing_dans_aide`** : proportion notable (6,3 %) par rapport aux corpus précédents (Sellsy 6/454, soit 1,3 %). S'explique par la présence, dans ce corpus WordPress historique, d'anciens billets de blog éditoriaux/motivationnels sans contenu produit (`il-est-temps.md`, `la-gestion-du-changement.md`, `mieux-gerer-ses-emails-professionnels.md`, `les-formations-gratuites-dextrabat-inscrivez-vous.md`, etc.) et de pages produit à forte tonalité commerciale (intégrations partenaires avec code de réduction, simulation de financement Franfinance).

## Limites

Ce fichier documente une carte de sélection LIGHT, pas une analyse produit. Conformément à SCHEMA-LIGHT.md §9 :

- Un `non` sur les champs `contenu_observable` ne permet pas de conclure à une absence fonctionnelle dans Extrabat — uniquement à une absence d'observation dans le document LIGHT concerné.
- La proportion élevée de `moment_parcours = indetermine` (61 %) ne signifie pas qu'Extrabat manque de structuration en parcours client : elle reflète la nature très fragmentée et technique de sa documentation d'aide historique (articles courts, souvent un paramétrage isolé), pas une mesure de maturité produit.
- Les fréquences de `capacites_transverses` et de `genre_documentaire` sont des comptages mécaniques sur le corpus documentaire collecté, non une mesure de l'importance métier, de l'adoption ou de la qualité des fonctionnalités correspondantes chez Extrabat. Ces comptages sont en outre mécaniquement gonflés par les 60 documents dupliqués et les 2 pages agrégats recensés en « Cas mal représentés » : un total brut ne doit jamais être lu comme 347 observations indépendantes.
- L'arbitrage différé sur `tarification` (12 occurrences) et `marketing_et_communication` (2 occurrences) reste ouvert ; les comptages ci-dessus sont descriptifs et ne préjugent pas de la décision à venir sur leur périmètre.
- Les 25 documents sans contenu substantif et les doublons signalés reflètent des artefacts de collecte/republication du site WordPress source, pas une évaluation de la qualité de la documentation Extrabat par SUPORDO.
- Ce fichier ne contient aucune conclusion de marché, aucune comparaison chiffrée avec les corpus précédents au-delà des constats mécaniques explicitement établis, et aucune recommandation produit SUPORDO.
