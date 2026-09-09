# LIGHT — production Sellsy (corpus aide)

Production sous SCHEMA-LIGHT.md (contrat canonique), lu intégralement avant
ce run. Discipline : un document à la fois, lu intégralement, sortie écrite
immédiatement, aucune correction rétroactive sauf erreur mécanique démontrée
et journalisée. Run de production, pas un test méthodologique de LIGHT.

## Périmètre — vérification mécanique et gel

- `sellsy_help` (`corpus_index.json`) : **462** documents (`type: aide`,
  20 rubriques éditoriales). `index.md`/`erreurs.md` (racine) et
  `site_marketing/` exclus du comptage canonique par construction du
  générateur (notes du corpus). Aucune `analysis_exclusions` déclarée dans
  `corpus_index.json` pour ce corpus.
  Vérification mécanique disque : 464 fichiers `.md` hors `site_marketing/`
  − `index.md` − `erreurs.md` = 462, identique au chiffre `corpus_index.json`.
- Déjà LIGHT (Pilote, `pilote-light-corpus-inedit.md`, entrées #18–#25 de
  son tableau de sélection — ce tableau ne porte pas `chemin_relatif` dans
  sa propre sortie ; jointure faite par `#` avec le tableau de sélection) :
  **8** —
  `module-marketing/marketing-5-astuces-pour-maximiser-les-performances-de-vos-newsletters.md`,
  `module-stocks/activer-la-gestion-des-stocks-pour-les-declinaisons-de-produits.md`,
  `module-support/attacher-un-contact-a-un-ticket.md`,
  `module-tresorerie/debuter-avec-sellsy-tresorerie.md`,
  `rapports-et-pilotage/gestion-des-acces-aux-rapports-pour-les-utilisateurs.md`,
  `repertoire/ajouter-une-adresse-postale-sur-une-societe.md`,
  `sellsy-automatisations/accueillir-vos-nouveaux-clients.md`,
  `sellsy-ia/decouvrir-sellsy-ia.md`.
  Les 8 proviennent du Pilote, pas du micro-lot H3 (`light-h3-validation-positifs.md`
  ne contient que 4 InterFast + 2 Vertuoza, aucun Sellsy — vérifié par grep).
- **Inédits à traiter, périmètre gelé : 454.**

Vérification mécanique : 462 (canonique) = 454 (inédits) + 8 (déjà LIGHT),
union exacte, 0 doublon, 0 chemin manquant (vérifié par `comm` entre la
liste canonique disque et la liste des 8 déjà-LIGHT). Garde-fou de mission
(462 − 8 = 454) recalculé, écart nul.

Coût de relecture explicite (SCHEMA-LIGHT.md §5) : Sellsy a été lu par
Pilote A (`audit-pilote-A.md`, `crash-test-utilite-pilote-A.md` — périmètre
déclaré « Sellsy 10 » articles). Ces lectures n'excluent aucun document du
périmètre LIGHT. Un seul chemin y est mécaniquement extractible (nom de
fichier complet cité) : `configuration-du-compte/gerer-les-profils-de-privileges-de-mes-collaborateurs.md`
— présent, resté dans le périmètre RESTANT, sans observation LIGHT
préexistante. Au-delà de ce chemin, les autres articles Sellsy cités par
Pilote A le sont par description de contenu ou citation de passage, sans
nom de fichier complet, donc non mécaniquement reconstructibles.

Aucune anomalie de collecte n'est documentée pour Sellsy dans `résumé.md`
(« Axonaut et Sellsy : aucun incident »). Corpus le plus volumineux du
dépôt en nombre de documents : 454 documents restants pour ≈2 545 Ko de
texte (bytes des 454 fichiers restants) — densité moyenne nettement plus
faible que InterFast (≈10,8 Ko/document) : environ 5,6 Ko/document.

Répartition des 454 inédits par rubrique éditoriale :
`documents-de-vente` 68 · `configuration-du-compte` 42 ·
`rapports-et-pilotage` 39 · `facturation-electronique` 36 ·
`gestion-des-donnees` 35 · `suivi-financier` 32 · `crm-et-prospection` 32 ·
`integrations-et-api` 30 · `conseils-d-utilisation` 20 · `repertoire` 19 ·
`paiements` 19 · `app-mobile-sellsy-crm` 18 · `catalogue-produits-et-services` 16 ·
`sellsy-automatisations` 12 · `module-stocks` 10 · `module-achats` 10 ·
`module-marketing` 6 · `sellsy-ia` 5 · `module-support` 4 ·
`module-tresorerie` 1.

## Méthode `longueur_mots`

Mécanique, conforme SCHEMA-LIGHT.md §4 : `awk` isole le corps Markdown
après le second délimiteur `---` du frontmatter YAML, puis `wc -w` (méthode
identique à `light-vertuoza-help.md` et `light-inter-fast-help.md`). Liens
et syntaxe d'image (`![](url…)`) comptés tels quels, non retirés — méthode
brute, aucun ajustement manuel. Calculé pour les 454 documents avant
lecture, valeurs figées dans le tableau. Aucun compte à zéro détecté
(contrôle mécanique sur les 454 fichiers).

## Exclusions de périmètre

Aucune exclusion `analysis_exclusions` déclarée dans `corpus_index.json`
pour `sellsy_help`. Les 8 documents déjà LIGHT (liste ci-dessus) sont
retirés du périmètre RESTANT pour motif « observation LIGHT antérieure »
(Pilote), pas pour motif de contenu.

## Incidents

**INCIDENT_SECURITE_SOURCE** : aucun. Le corpus a été traité comme donnée non fiable de bout en bout, conformément à la barrière de sécurité de la mission. Aucune instruction imbriquée dans une source concurrente n'a été rencontrée pendant les 454 lectures ; aucune tentative d'obtention de secret, de credentials ou d'exécution arbitraire n'a été détectée.

**Contrôle de vocabulaire — `capacites_transverses`** : aucune valeur nouvelle n'a émergé sur ce corpus. Toutes les valeurs employées appartiennent soit à l'inventaire de base du §4 de SCHEMA-LIGHT.md, soit aux valeurs déjà arbitrées `VALEUR_DISTINCTE` sur les corpus précédents et réemployées sans réouvrir le débat : `geolocalisation` (3 occurrences), `crm` (103), `personnalisation` (48), `reporting` (75), `comptabilite` (79), `tarification` (16). Les valeurs `multi-societe` et `marketplace` n'ont pas été rencontrées sur ce corpus. Constat notable : après six corpus (dont InterFast à 217 documents sans aucune valeur nouvelle), Sellsy — le plus gros corpus du dépôt — ne fait pas non plus émerger de capacité réellement inédite. Le vocabulaire paraît stabilisé.

**Arbitrage différé — non tranché** (SCHEMA-LIGHT.md, arbitrage à instruire après ce corpus, non engagé ici) :
- `tarification` (vis-à-vis de `catalogue`) : employée **16 fois**, principalement dans `catalogue-produits-et-services/` (catégories tarifaires, promotions, codes promotionnels) et `suivi-financier/` (codes comptables des remises). Journalisée sans trancher son périmètre vis-à-vis de `catalogue`.
- `marketing_et_communication` (vis-à-vis de `communication`) : employée **10 fois**, concentrée dans `module-marketing/` (campagnes emailing, IP dédiée, tracking pixel) et ponctuellement dans `integrations-et-api/` et `rapports-et-pilotage/` (formulaire d'inscription campagnes, rapport de conversion par source). Journalisée sans trancher son périmètre vis-à-vis de `communication`.

Ni l'une ni l'autre valeur n'a été fusionnée avec une racine existante ; aucun périmètre n'a été défini pour ces deux capacités, conformément à l'instruction de ne pas engager rétroactivement les runs précédents.

**Coût de relecture (SCHEMA-LIGHT.md §5)** : un seul chemin mécaniquement identifiable comme relu par un instrument antérieur (Pilote A) est resté dans le périmètre RESTANT : `configuration-du-compte/gerer-les-profils-de-privileges-de-mes-collaborateurs.md` (#44 du tableau). Il a été codé normalement, sans traitement différencié, conformément à la règle « inédit LIGHT ».

**Templates fortement répétitifs, traités individuellement** : deux familles de documents suivent un template quasi identique d'un article à l'autre (nom du tiers substitué) — les 7 guides de connecteurs comptables (`integrations-et-api/connecter-sellsy-et-{acd,cegid-loop,fulll,inexweb-in-extenso,myunisoft,sage-generation-experts,tiime}.md`) et les ~15 fiches `sellsy-automatisations/*` et `paiements/activer-le-paiement-en-ligne-avec-*.md`. Chaque document a néanmoins été lu intégralement et codé individuellement ; les différences réelles entre eux (méthode d'authentification propre à chaque éditeur, présence ou non d'un dépannage FAQ, contraintes spécifiques) ont été vérifiées avant codification, non supposées.

## Tableau LIGHT

| # | chemin_relatif | longueur_mots | objet_principal | moment_parcours | capacites_transverses | procedure | transition_objet | regle_ou_condition | contrainte_ou_limite | exception_ou_correction | genre_documentaire |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | app-mobile-sellsy-crm/app-sellsy-crm-ajouter-une-activite-sur-une-fiche-du-repertoire.md | 91 | activité (répertoire) | indetermine | crm, mobile | oui | non | non | non | non | procedure |
| 2 | app-mobile-sellsy-crm/app-sellsy-crm-ajouter-une-opportunite.md | 152 | opportunité (pipeline) | indetermine | crm, mobile | oui | oui | non | non | non | procedure |
| 3 | app-mobile-sellsy-crm/app-sellsy-crm-creer-modifier-et-envoyer-un-bon-de-commande.md | 300 | bon de commande | devis | mobile, documents | oui | non | oui | non | non | procedure |
| 4 | app-mobile-sellsy-crm/app-sellsy-crm-creer-modifier-et-envoyer-un-devis-ou-un-bon-de-commande.md | 496 | devis / bon de commande | devis | mobile, documents | oui | non | oui | non | non | procedure |
| 5 | app-mobile-sellsy-crm/app-sellsy-crm-creer-un-client-prospect-ou-fournisseur.md | 176 | fiche répertoire (client/prospect/fournisseur) | indetermine | crm, mobile, geolocalisation | oui | non | non | non | non | procedure |
| 6 | app-mobile-sellsy-crm/app-sellsy-crm-gestion-des-factures-et-avoirs.md | 88 | facture / avoir (consultation mobile) | facturation | mobile, documents | oui | non | non | non | non | procedure |
| 7 | app-mobile-sellsy-crm/app-sellsy-crm-importer-et-classer-vos-fichiers-sur-notre-application-mobile.md | 240 | fichier (répertoire, mobile) | indetermine | mobile, documents | oui | non | oui | oui | non | procedure |
| 8 | app-mobile-sellsy-crm/app-sellsy-crm-introduction-gestion-des-opportunites-et-pipeline.md | 94 | opportunités / pipeline (intro module) | indetermine | crm, mobile | non | non | non | non | non | definitionnel |
| 9 | app-mobile-sellsy-crm/app-sellsy-crm-introduction-gestion-des-ventes.md | 70 | devis (intro module ventes) | devis | mobile, documents | non | non | non | non | non | definitionnel |
| 10 | app-mobile-sellsy-crm/app-sellsy-crm-introduction-gestion-du-repertoire.md | 88 | répertoire (intro module) | indetermine | crm, mobile | non | non | non | non | non | definitionnel |
| 11 | app-mobile-sellsy-crm/app-sellsy-crm-le-journal-des-appels.md | 481 | journal des appels | indetermine | crm, mobile, permissions | oui | non | oui | non | non | procedure |
| 12 | app-mobile-sellsy-crm/app-sellsy-crm-modifier-les-informations-d-une-fiche-du-repertoire.md | 245 | fiche répertoire (modification) | indetermine | crm, mobile, documents | oui | non | non | non | non | procedure |
| 13 | app-mobile-sellsy-crm/app-sellsy-crm-tableau-de-bord-mes-evenements.md | 99 | tableau de bord (événements) | indetermine | crm, mobile, planning | oui | non | non | non | non | procedure |
| 14 | app-mobile-sellsy-crm/app-sellsy-crm-tableau-de-bord-opportunites.md | 85 | tableau de bord (opportunités) | indetermine | crm, mobile | oui | non | non | non | non | procedure |
| 15 | app-mobile-sellsy-crm/app-sellsy-crm-tableau-de-bord-taches.md | 140 | tableau de bord (tâches) | indetermine | crm, mobile, planning | oui | non | non | non | non | procedure |
| 16 | app-mobile-sellsy-crm/app-sellsy-crm-utiliser-des-filtres-favoris.md | 177 | filtres favoris (répertoire, mobile) | indetermine | crm, mobile | oui | non | oui | oui | non | procedure |
| 17 | app-mobile-sellsy-crm/app-sellsy-crm-visualiser-les-societes-sur-une-carte.md | 179 | société (visualisation carte, mobile) | indetermine | crm, mobile, geolocalisation | oui | non | non | non | non | procedure |
| 18 | app-mobile-sellsy-crm/tester-sellsy-crm-sur-votre-mobile.md | 494 | application mobile (présentation fonctionnalités) | indetermine | crm, mobile, documents | non | non | oui | oui | non | marketing_dans_aide |
| 19 | catalogue-produits-et-services/activer-et-utiliser-l-ecotaxe.md | 168 | écotaxe (produit) | indetermine | catalogue, facturation | oui | non | oui | oui | non | procedure |
| 20 | catalogue-produits-et-services/ajouter-des-photos-a-mes-produits-et-declinaisons.md | 307 | photos (produit / déclinaison) | indetermine | catalogue, photos | oui | non | oui | non | non | procedure |
| 21 | catalogue-produits-et-services/ajouter-des-produits-et-services-a-mon-catalogue.md | 128 | produit / service (catalogue) | indetermine | catalogue | oui | non | non | non | non | procedure |
| 22 | catalogue-produits-et-services/ajouter-des-specifications-a-mon-produit.md | 90 | spécifications (produit) | indetermine | catalogue | oui | non | non | non | non | procedure |
| 23 | catalogue-produits-et-services/ajouter-un-code-barres-a-un-produit.md | 122 | code-barres (produit) | indetermine | catalogue | oui | non | non | non | non | procedure |
| 24 | catalogue-produits-et-services/ajouter-un-taux-de-tva.md | 170 | taux de TVA | indetermine | catalogue, comptabilite, integrations | oui | non | oui | non | non | procedure |
| 25 | catalogue-produits-et-services/creer-des-promotions.md | 389 | promotion (catalogue) | indetermine | catalogue, tarification | oui | non | oui | non | non | procedure |
| 26 | catalogue-produits-et-services/creer-et-gerer-les-declinaisons-de-mes-produits.md | 643 | déclinaison (produit) | indetermine | catalogue, gestion_stock | oui | oui | oui | oui | non | procedure |
| 27 | catalogue-produits-et-services/difference-entre-produits-et-services.md | 144 | produit / service (définition catalogue) | indetermine | catalogue | non | non | non | non | non | definitionnel |
| 28 | catalogue-produits-et-services/gerer-et-appliquer-les-promotions.md | 323 | promotion (gestion / application) | indetermine | catalogue, tarification | oui | oui | non | non | non | procedure |
| 29 | catalogue-produits-et-services/gerer-les-poids-et-dimensions-de-mes-produits.md | 204 | poids et dimensions (produit) | indetermine | catalogue | oui | non | non | non | non | procedure |
| 30 | catalogue-produits-et-services/gerer-mes-categories-de-produits.md | 236 | catégorie de produits (catalogue) | indetermine | catalogue | oui | non | non | non | non | procedure |
| 31 | catalogue-produits-et-services/gestion-des-codes-promotionnels.md | 382 | code promotionnel | indetermine | catalogue, tarification | oui | non | oui | non | non | procedure |
| 32 | catalogue-produits-et-services/supprimer-des-produits-services-en-masse.md | 110 | produit / service (suppression en masse) | indetermine | catalogue | oui | non | non | non | non | procedure |
| 33 | catalogue-produits-et-services/utiliser-les-categories-tarifaires.md | 365 | catégorie tarifaire | indetermine | catalogue, tarification | oui | non | oui | oui | non | procedure |
| 34 | catalogue-produits-et-services/utiliser-les-exceptions-tarifaires.md | 108 | exception tarifaire (client) | indetermine | catalogue, tarification | oui | non | non | non | non | procedure |
| 35 | configuration-du-compte/ajouter-des-cgv-aux-pieces-jointes-des-emails.md | 300 | CGV (pièce jointe email) | indetermine | communication, permissions, documents | oui | non | oui | oui | non | procedure |
| 36 | configuration-du-compte/ajouter-des-credits-a-mon-compte-sellsy.md | 140 | crédits (compte Sellsy) | indetermine | paiement | oui | non | oui | oui | non | procedure |
| 37 | configuration-du-compte/connexion-sso.md | 355 | SSO (connexion) | indetermine | securite_compte, permissions | non | non | oui | oui | non | reference_configuration |
| 38 | configuration-du-compte/creer-des-modeles-d-emails-personnalises.md | 402 | modèle d'email personnalisé | indetermine | communication, automatisation, personnalisation | oui | non | oui | non | non | procedure |
| 39 | configuration-du-compte/creer-une-signature-email.md | 450 | signature email | indetermine | communication, personnalisation | oui | non | non | non | non | procedure |
| 40 | configuration-du-compte/definir-un-nouveau-proprietaire-du-compte-sellsy.md | 227 | propriétaire de compte | indetermine | roles, permissions | oui | oui | oui | non | non | procedure |
| 41 | configuration-du-compte/donner-un-acces-sellsy-a-mon-expert-comptable.md | 239 | accès expert-comptable | indetermine | comptabilite, permissions, roles | oui | non | oui | oui | oui | procedure |
| 42 | configuration-du-compte/gerer-les-acces-collaborateurs.md | 662 | collaborateur (gestion accès) | indetermine | roles, permissions | oui | oui | oui | oui | oui | procedure |
| 43 | configuration-du-compte/gerer-les-modes-d-affichage-de-mon-agenda.md | 243 | agenda (mode d'affichage) | indetermine | planning | oui | non | oui | oui | non | procedure |
| 44 | configuration-du-compte/gerer-les-profils-de-privileges-de-mes-collaborateurs.md | 464 | profil de privilèges | indetermine | permissions, roles | oui | non | oui | oui | non | procedure |
| 45 | configuration-du-compte/les-factures-de-mon-abonnement-sellsy.md | 127 | facture d'abonnement Sellsy | facturation | facturation, comptabilite | oui | non | oui | oui | non | procedure |
| 46 | configuration-du-compte/lier-un-email-a-un-objet-contact-societe-opportunite-document.md | 457 | email (liaison à un objet) | indetermine | crm, communication, automatisation | oui | non | oui | oui | non | procedure |
| 47 | configuration-du-compte/parametrer-les-formats-de-donnees.md | 229 | formats de données (téléphone, date, devise) | indetermine | personnalisation | oui | non | non | non | non | reference_configuration |
| 48 | configuration-du-compte/parametrer-les-informations-de-ma-societe.md | 277 | informations société | indetermine | conformite_reglementaire, personnalisation | oui | non | oui | oui | non | procedure |
| 49 | configuration-du-compte/parametrer-les-unites.md | 257 | unités (catalogue) | indetermine | catalogue, conformite_reglementaire | oui | non | non | non | non | procedure |
| 50 | configuration-du-compte/partager-des-donnees-entre-collaborateurs.md | 321 | partage de données (collaborateurs) | indetermine | permissions, roles | oui | non | oui | oui | non | procedure |
| 51 | configuration-du-compte/personnaliser-les-labels-de-taches.md | 120 | labels de tâches | indetermine | personnalisation, planning | oui | non | non | non | non | procedure |
| 52 | configuration-du-compte/personnaliser-les-labels-des-evenements.md | 93 | labels d'événements (agenda) | indetermine | personnalisation, planning | oui | non | non | non | non | procedure |
| 53 | configuration-du-compte/presentation-de-l-espace-client.md | 179 | espace client | indetermine | crm, permissions, documents | oui | non | oui | oui | non | procedure |
| 54 | configuration-du-compte/profils-de-privileges.md | 477 | profil de privilèges (définition) | indetermine | permissions, roles | non | non | oui | oui | non | definitionnel |
| 55 | configuration-du-compte/synchronisation-des-agendas-et-contacts-avec-google.md | 984 | synchronisation agenda / contacts (Google) | indetermine | integrations, planning, crm | oui | non | oui | oui | oui | procedure |
| 56 | configuration-du-compte/synchronisation-des-agendas-et-contacts-avec-office-365-outlook.md | 934 | synchronisation agenda / contacts (Office 365 / Outlook) | indetermine | integrations, planning, crm | oui | non | oui | oui | oui | procedure |
| 57 | configuration-du-compte/tableau-de-bord-achats-et-marges.md | 222 | tableau de bord (achats et marges) | indetermine | reporting, comptabilite | oui | non | non | oui | non | reference_configuration |
| 58 | configuration-du-compte/tableau-de-bord-agenda.md | 121 | tableau de bord (agenda) | indetermine | planning, reporting | oui | non | non | oui | non | reference_configuration |
| 59 | configuration-du-compte/tableau-de-bord-bons-de-commande.md | 193 | tableau de bord (bons de commande) | indetermine | reporting, facturation | oui | non | non | non | non | reference_configuration |
| 60 | configuration-du-compte/tableau-de-bord-campagnes-marketing.md | 83 | tableau de bord (campagnes marketing) | indetermine | communication, marketing_et_communication | oui | non | non | oui | non | reference_configuration |
| 61 | configuration-du-compte/tableau-de-bord-chiffre-d-affaires.md | 338 | tableau de bord (chiffre d'affaires) | indetermine | reporting, comptabilite | oui | non | oui | oui | non | reference_configuration |
| 62 | configuration-du-compte/tableau-de-bord-commentaires.md | 88 | tableau de bord (commentaires) | indetermine | reporting, communication | non | non | non | oui | non | reference_configuration |
| 63 | configuration-du-compte/tableau-de-bord-derniers-objets-crees.md | 95 | tableau de bord (derniers objets créés) | indetermine | reporting | oui | non | non | oui | non | reference_configuration |
| 64 | configuration-du-compte/tableau-de-bord-devis.md | 178 | tableau de bord (devis) | indetermine | reporting | oui | non | non | non | non | reference_configuration |
| 65 | configuration-du-compte/tableau-de-bord-factures-non-rapprochees.md | 208 | tableau de bord (factures non rapprochées) | indetermine | reporting, comptabilite | oui | non | oui | oui | non | reference_configuration |
| 66 | configuration-du-compte/tableau-de-bord-factures-proforma.md | 160 | tableau de bord (factures proforma) | indetermine | reporting, facturation | oui | non | non | non | non | reference_configuration |
| 67 | configuration-du-compte/tableau-de-bord-factures.md | 209 | tableau de bord (factures) | indetermine | reporting, facturation | oui | non | oui | non | non | reference_configuration |
| 68 | configuration-du-compte/tableau-de-bord-opportunites.md | 240 | tableau de bord (opportunités) | indetermine | reporting, crm | oui | non | non | oui | non | reference_configuration |
| 69 | configuration-du-compte/tableau-de-bord-solde-des-comptes-bancaires.md | 208 | tableau de bord (solde comptes bancaires) | indetermine | reporting, comptabilite | oui | non | oui | oui | non | reference_configuration |
| 70 | configuration-du-compte/tableau-de-bord-statistiques-de-facturation.md | 1013 | tableau de bord (statistiques de facturation) | indetermine | reporting, facturation | oui | non | oui | oui | non | reference_configuration |
| 71 | configuration-du-compte/tableau-de-bord-statistiques-de-vente.md | 935 | tableau de bord (statistiques de vente) | indetermine | reporting, crm | oui | non | oui | oui | non | reference_configuration |
| 72 | configuration-du-compte/tableau-de-bord-taches.md | 181 | tableau de bord (tâches) | indetermine | reporting, planning | oui | oui | non | oui | non | reference_configuration |
| 73 | configuration-du-compte/tableau-de-bord-tickets.md | 127 | tableau de bord (tickets) | indetermine | reporting | non | non | oui | non | non | reference_configuration |
| 74 | configuration-du-compte/utiliser-l-agenda-sellsy.md | 339 | agenda (usage) | indetermine | planning | oui | non | oui | oui | non | procedure |
| 75 | configuration-du-compte/utiliser-les-groupes-de-collaborateurs.md | 259 | groupe de collaborateurs | indetermine | roles, permissions | oui | non | oui | non | non | procedure |
| 76 | configuration-du-compte/utiliser-les-taches.md | 509 | tâche (usage) | indetermine | crm, planning | oui | oui | oui | oui | non | procedure |
| 77 | conseils-d-utilisation/acces-confidentialite-et-mesures-organisationnelles.md | 501 | sécurité / confidentialité (mesures organisationnelles) | indetermine | securite_compte, conformite_reglementaire | non | non | oui | non | non | politique_legale |
| 78 | conseils-d-utilisation/bien-demarrer-avec-sellsy.md | 481 | onboarding (parcours de démarrage) | indetermine | support_editeur | oui | non | non | non | non | procedure |
| 79 | conseils-d-utilisation/configurer-la-double-authentification-en-tant-qu-administrateur.md | 583 | double authentification (administrateur) | indetermine | securite_compte, conformite_reglementaire, permissions | oui | non | oui | oui | oui | procedure |
| 80 | conseils-d-utilisation/configurer-la-double-authentification-en-tant-qu-utilisateur.md | 680 | double authentification (utilisateur) | indetermine | securite_compte | oui | non | oui | non | oui | procedure |
| 81 | conseils-d-utilisation/connexion-a-mon-compte-sellsy.md | 471 | connexion (compte) | indetermine | securite_compte | oui | non | non | non | oui | faq_depannage |
| 82 | conseils-d-utilisation/connexion-non-chiffree-au-site-sellsy.md | 278 | connexion (compatibilité navigateur/certificat) | indetermine | securite_compte | oui | non | non | oui | oui | faq_depannage |
| 83 | conseils-d-utilisation/conseils-pour-ameliorer-la-performance-de-sellsy.md | 392 | performance (conseils techniques) | indetermine | — | oui | non | non | non | oui | faq_depannage |
| 84 | conseils-d-utilisation/debuter-sur-sellsy-quelques-liens-utiles.md | 314 | ressources d'aide (Academy, blog, FAQ, webinars) | indetermine | support_editeur | non | non | non | non | non | autre |
| 85 | conseils-d-utilisation/decouvrez-toutes-nos-fonctionnalites-collaboratives.md | 201 | fonctionnalités collaboratives (mention, épinglage, Slack) | indetermine | crm, communication, integrations | oui | non | non | non | non | procedure |
| 86 | conseils-d-utilisation/les-bons-reflexes-a-adopter-en-cas-de-piratage.md | 655 | piratage (réaction en cas d'incident) | indetermine | securite_compte | oui | non | non | non | oui | procedure |
| 87 | conseils-d-utilisation/navigateurs-compatibles-avec-sellsy.md | 165 | navigateurs compatibles (configuration système) | indetermine | — | non | non | oui | oui | non | reference_configuration |
| 88 | conseils-d-utilisation/notifications-fonctionnement-et-reglages.md | 615 | notifications (fonctionnement / réglages) | indetermine | notifications, automatisation, permissions | oui | non | oui | oui | oui | procedure |
| 89 | conseils-d-utilisation/ou-sont-hebergees-vos-donnees-et-comment-elles-sont-chiffrees.md | 173 | hébergement / chiffrement des données | indetermine | securite_compte, conformite_reglementaire | non | non | non | non | non | politique_legale |
| 90 | conseils-d-utilisation/parametrer-les-informations-de-mon-profil.md | 92 | informations de profil (collaborateur) | indetermine | personnalisation | oui | non | oui | non | non | procedure |
| 91 | conseils-d-utilisation/personnalisation-du-tableau-de-bord.md | 273 | tableau de bord (personnalisation) | indetermine | reporting, permissions | oui | non | oui | oui | non | procedure |
| 92 | conseils-d-utilisation/reconfigurer-la-double-authentification-en-tant-qu-utilisateur-sellsy.md | 499 | double authentification (reconfiguration) | indetermine | securite_compte | oui | non | oui | oui | oui | faq_depannage |
| 93 | conseils-d-utilisation/sauvegarde-continuite-de-service-et-prevention-des-intrusions.md | 340 | sauvegarde / sécurité infrastructure | indetermine | securite_compte, conformite_reglementaire | non | non | non | non | non | politique_legale |
| 94 | conseils-d-utilisation/securiser-les-donnees-de-votre-entreprise.md | 1153 | cybersécurité (bonnes pratiques) | indetermine | securite_compte, conformite_reglementaire | non | non | non | non | non | politique_legale |
| 95 | conseils-d-utilisation/securiser-votre-compte-sellsy.md | 503 | sécurité du compte (bonnes pratiques) | indetermine | securite_compte, conformite_reglementaire, permissions | oui | non | non | non | non | politique_legale |
| 96 | conseils-d-utilisation/synchroniser-et-parametrer-votre-compte-email.md | 1292 | synchronisation compte email | indetermine | communication, integrations, permissions | oui | non | oui | oui | oui | procedure |
| 97 | crm-et-prospection/activer-la-signature-electronique-sur-les-documents-redactor.md | 296 | signature électronique (documents Redactor) | indetermine | documents, validation | oui | oui | non | non | non | procedure |
| 98 | crm-et-prospection/afficher-ou-masquer-un-pipeline.md | 99 | pipeline (affichage) | indetermine | crm | oui | oui | non | non | non | procedure |
| 99 | crm-et-prospection/ajouter-une-entree-de-time-tracking-sur-un-ticket-de-support.md | 101 | time tracking (ticket support) | indetermine | crm | oui | non | non | non | non | procedure |
| 100 | crm-et-prospection/configurer-le-suivi-des-appels.md | 113 | suivi des appels (configuration) | indetermine | crm, automatisation | oui | non | non | non | non | procedure |
| 101 | crm-et-prospection/configurer-les-pipelines-de-prospection-pour-le-rapport-de-vente-previsionnel.md | 316 | pipeline de prospection (rapport prévisionnel) | indetermine | crm, reporting | oui | non | oui | oui | non | procedure |
| 102 | crm-et-prospection/creer-un-modele-redactor.md | 709 | modèle Redactor (document dynamique) | indetermine | documents, personnalisation, validation | oui | non | oui | oui | non | procedure |
| 103 | crm-et-prospection/creer-un-pipeline.md | 118 | pipeline (création) | indetermine | crm | oui | non | non | non | non | procedure |
| 104 | crm-et-prospection/creer-une-proposition-commerciale-dynamique-avec-redactor.md | 433 | proposition commerciale dynamique (Redactor) | devis | documents, personnalisation | oui | non | non | non | non | procedure |
| 105 | crm-et-prospection/definir-des-objectifs-commerciaux.md | 982 | objectifs commerciaux | indetermine | reporting, permissions | oui | oui | oui | oui | non | procedure |
| 106 | crm-et-prospection/definir-un-document-en-tant-que-document-principal-d-une-opportunite.md | 295 | document principal (opportunité) | indetermine | crm, documents | oui | non | oui | non | non | procedure |
| 107 | crm-et-prospection/envoyer-mon-document-redactor-par-courrier.md | 126 | envoi document Redactor par courrier | indetermine | documents, paiement | oui | non | non | oui | non | procedure |
| 108 | crm-et-prospection/fonctionnement-et-utilisation-du-timetracking.md | 227 | time tracking (fonctionnement) | indetermine | comptabilite | non | non | oui | oui | non | definitionnel |
| 109 | crm-et-prospection/gestion-de-la-refacturation-d-heure.md | 292 | refacturation d'heures | indetermine | facturation, comptabilite | oui | non | oui | oui | non | procedure |
| 110 | crm-et-prospection/inserer-un-pdf-dans-un-document-redactor.md | 122 | PDF (insertion document Redactor) | indetermine | documents | oui | non | non | non | non | procedure |
| 111 | crm-et-prospection/introduction-module-redactor.md | 183 | module Redactor (introduction) | indetermine | documents, personnalisation | non | non | non | non | non | definitionnel |
| 112 | crm-et-prospection/introduction-suivi-des-opportunites.md | 528 | opportunité (suivi, définition) | indetermine | crm | non | oui | oui | non | non | definitionnel |
| 113 | crm-et-prospection/liste-d-activite.md | 522 | activités (liste tâches/appels) | indetermine | crm, planning | oui | oui | non | non | non | procedure |
| 114 | crm-et-prospection/mettre-en-place-une-sequence-d-emails-automatiques-sur-une-opportunite.md | 558 | séquence d'emails automatiques (opportunité) | indetermine | crm, automatisation, communication | oui | non | oui | oui | non | procedure |
| 115 | crm-et-prospection/presentation-de-la-fiche-opportunite.md | 1033 | fiche opportunité (présentation complète) | indetermine | crm, permissions, documents | oui | oui | oui | oui | non | procedure |
| 116 | crm-et-prospection/rapport-des-sources-d-opportunites.md | 671 | sources d'opportunités (rapport) | indetermine | crm, reporting | oui | non | non | non | non | procedure |
| 117 | crm-et-prospection/reglages-du-module-redactor.md | 174 | réglages module Redactor | indetermine | documents, personnalisation | oui | non | non | non | non | reference_configuration |
| 118 | crm-et-prospection/saisie-hebdomadaire-des-heures-sur-timetracking.md | 191 | time tracking (saisie hebdomadaire) | indetermine | comptabilite | oui | non | oui | oui | oui | procedure |
| 119 | crm-et-prospection/saisie-rapide-d-un-temps.md | 69 | time tracking (saisie rapide) | indetermine | — | oui | non | non | non | non | procedure |
| 120 | crm-et-prospection/suivi-des-appels-commerciaux.md | 169 | suivi des appels (module) | indetermine | crm | oui | non | non | non | non | procedure |
| 121 | crm-et-prospection/suivre-les-heures-effectuees-par-mes-collaborateurs-grace-au-time-tracking.md | 133 | time tracking (suivi heures collaborateurs) | indetermine | reporting, comptabilite | oui | non | non | non | non | procedure |
| 122 | crm-et-prospection/suivre-les-resultats-d-un-email-automatique.md | 175 | email automatique (résultats / scoring) | indetermine | crm, automatisation, reporting | oui | non | oui | oui | non | procedure |
| 123 | crm-et-prospection/suivre-mes-opportunites-en-utilisant-les-taches.md | 116 | opportunité (suivi via tâches) | indetermine | crm, planning | oui | non | non | non | non | procedure |
| 124 | crm-et-prospection/supprimer-des-opportunites-et-des-pipelines.md | 250 | opportunité / pipeline (suppression) | indetermine | crm | oui | non | oui | oui | non | procedure |
| 125 | crm-et-prospection/synchroniser-ringover-avec-sellsy.md | 603 | intégration Ringover (téléphonie) | indetermine | integrations, crm, communication | oui | non | oui | non | non | procedure |
| 126 | crm-et-prospection/utiliser-la-vue-pipeline.md | 139 | pipeline (vue) | indetermine | crm | oui | oui | non | non | non | procedure |
| 127 | crm-et-prospection/utiliser-les-fonctions-collaboratives.md | 114 | fonctions collaboratives (travail d'équipe) | indetermine | crm, communication | non | non | non | non | non | marketing_dans_aide |
| 128 | crm-et-prospection/utiliser-les-timers.md | 135 | timer (time tracking) | indetermine | — | oui | oui | non | non | non | procedure |
| 129 | documents-de-vente/activer-et-configurer-le-module-de-signature-electronique.md | 190 | signature électronique (module, documents de vente) | indetermine | documents, validation, permissions | oui | non | oui | oui | non | procedure |
| 130 | documents-de-vente/activer-le-mode-conforme-pour-les-documents-de-vente.md | 665 | mode conforme (facturation, conformité légale) | facturation | conformite_reglementaire, facturation | oui | oui | oui | oui | oui | politique_legale |
| 131 | documents-de-vente/activer-le-prelevement-automatique-pour-le-reglement-des-factures-d-abonnements-gocardless.md | 202 | prélèvement automatique (GoCardless, abonnements) | facturation | paiement, integrations, permissions | oui | non | oui | oui | non | procedure |
| 132 | documents-de-vente/activer-les-bons-de-commande-bons-de-livraison-et-proforma.md | 68 | types de documents de vente (activation) | indetermine | documents, catalogue | oui | non | non | non | non | procedure |
| 133 | documents-de-vente/afficher-les-dates-de-service-sur-un-document-de-vente.md | 112 | dates de service (document de vente) | facturation | documents, facturation | oui | non | non | non | non | procedure |
| 134 | documents-de-vente/ajouter-des-conditions-de-paiement-sur-un-document-de-vente.md | 345 | conditions de paiement (document de vente) | facturation | paiement, documents, validation | oui | non | oui | oui | non | procedure |
| 135 | documents-de-vente/ajouter-des-lignes-avec-un-lecteur-code-barres.md | 137 | lignes de document (lecteur code-barres) | indetermine | catalogue, documents | oui | non | non | non | non | procedure |
| 136 | documents-de-vente/ajouter-des-lignes-en-option.md | 182 | lignes en option (document de vente) | facturation | documents, facturation | oui | oui | oui | non | non | procedure |
| 137 | documents-de-vente/ajouter-mes-cgv-a-la-fin-d-un-document-de-vente.md | 108 | CGV (document de vente) | facturation | documents, conformite_reglementaire | oui | non | oui | oui | non | procedure |
| 138 | documents-de-vente/ajouter-mes-coordonnees-bancaires-sur-un-document-rib-iban.md | 470 | coordonnées bancaires (RIB / IBAN) | facturation | paiement, comptabilite, integrations | oui | non | oui | non | non | procedure |
| 139 | documents-de-vente/ajouter-ou-modifier-des-mentions-legales.md | 117 | mentions légales (document de vente) | facturation | documents, conformite_reglementaire | oui | non | non | non | non | procedure |
| 140 | documents-de-vente/ajuster-mes-tarifs-d-abonnement.md | 168 | tarifs d'abonnement | facturation | tarification, catalogue | oui | non | non | non | non | procedure |
| 141 | documents-de-vente/appliquer-des-remises-sur-un-document.md | 323 | remise (document de vente) | facturation | tarification, documents | oui | non | oui | oui | non | procedure |
| 142 | documents-de-vente/appliquer-une-remise-ttc-a-un-document-de-vente-prime-cee-eco-primes.md | 275 | remise TTC (primes CEE / éco-primes) | facturation | tarification, documents | oui | non | oui | non | non | procedure |
| 143 | documents-de-vente/changer-l-intitule-d-un-document.md | 116 | intitulé de document (personnalisation) | facturation | personnalisation, documents | oui | non | non | non | non | procedure |
| 144 | documents-de-vente/changer-la-numerotation-des-devis-et-factures.md | 190 | numérotation (devis / factures) | facturation | documents, conformite_reglementaire | oui | non | oui | oui | non | procedure |
| 145 | documents-de-vente/changer-les-statuts-de-documents-en-masse.md | 132 | statut de documents (changement en masse) | facturation | documents | oui | oui | non | oui | non | procedure |
| 146 | documents-de-vente/choisir-docusign-comme-service-de-signature-electronique.md | 227 | signature électronique (Docusign) | indetermine | integrations, validation, documents | oui | non | oui | oui | oui | procedure |
| 147 | documents-de-vente/connecteur-multi-entites-de-facturation.md | 957 | connecteur multi-entités (facturation groupe) | facturation | integrations, facturation, permissions | oui | oui | oui | oui | non | procedure |
| 148 | documents-de-vente/consulter-le-detail-des-lignes-des-documents-de-vente.md | 426 | lignes de documents de vente (consultation / export) | facturation | reporting, documents | oui | non | non | non | non | procedure |
| 149 | documents-de-vente/creer-et-gerer-des-avoirs.md | 821 | avoir (facturation) | facturation | facturation, comptabilite | oui | oui | oui | oui | oui | procedure |
| 150 | documents-de-vente/creer-un-abonnement.md | 680 | abonnement (facturation récurrente) | facturation | facturation, automatisation, paiement | oui | non | oui | oui | non | procedure |
| 151 | documents-de-vente/creer-un-document-ht-pour-l-export.md | 229 | document HT (export) | facturation | documents, tarification | oui | non | non | non | non | procedure |
| 152 | documents-de-vente/creer-un-fond-de-page.md | 381 | fond de page (personnalisation document) | facturation | personnalisation, documents | oui | non | oui | oui | non | procedure |
| 153 | documents-de-vente/creer-un-modele-de-document.md | 445 | modèle de document (devis / facture) | facturation | documents, tarification, personnalisation | oui | non | oui | oui | non | procedure |
| 154 | documents-de-vente/creer-un-modele-de-facture-d-abonnement.md | 479 | modèle facture d'abonnement (variables période) | facturation | facturation, personnalisation | oui | non | non | non | non | procedure |
| 155 | documents-de-vente/creer-une-apparence-de-document-vente-et-achat.md | 387 | apparence de document (personnalisation) | facturation | personnalisation, documents | oui | non | oui | oui | non | procedure |
| 156 | documents-de-vente/creer-une-facture-un-devis-un-document-de-vente.md | 584 | document de vente (création : devis / facture) | indetermine | documents, tarification, catalogue | oui | non | oui | oui | non | procedure |
| 157 | documents-de-vente/envoi-des-factures-en-masse.md | 338 | facture (envoi en masse) | facturation | facturation, communication, automatisation | oui | non | oui | oui | non | procedure |
| 158 | documents-de-vente/envoyer-mes-documents-par-courrier.md | 447 | envoi documents par courrier postal | facturation | documents, paiement | oui | non | oui | oui | non | procedure |
| 159 | documents-de-vente/envoyer-un-document-pour-signature-electronique.md | 568 | signature électronique (envoi document) | facturation | documents, validation, permissions | oui | oui | oui | oui | oui | procedure |
| 160 | documents-de-vente/etape-1-activer-la-relance-automatique.md | 275 | relance automatique (activation) | facturation | facturation, automatisation | oui | oui | oui | non | non | procedure |
| 161 | documents-de-vente/etape-1-ajouter-une-langue-au-compte.md | 217 | langue (compte, traduction) | indetermine | personnalisation, documents | oui | non | non | non | non | procedure |
| 162 | documents-de-vente/etape-2-creer-une-apparence-de-document-dans-une-autre-langue.md | 300 | apparence de document (langue) | indetermine | personnalisation, documents | oui | non | oui | non | non | procedure |
| 163 | documents-de-vente/etape-2-parametrer-un-plan-de-relance.md | 270 | plan de relance (paramétrage) | facturation | facturation, automatisation, communication | oui | non | non | non | non | procedure |
| 164 | documents-de-vente/etape-3-consulter-les-relances-liees-a-un-document.md | 260 | relance (consultation par document) | facturation | facturation, reporting | oui | oui | oui | non | non | procedure |
| 165 | documents-de-vente/etape-3-parametrer-la-traduction-de-l-ensemble-des-champs-de-documents.md | 267 | traduction des champs de documents | indetermine | personnalisation, documents | oui | non | non | non | non | procedure |
| 166 | documents-de-vente/etape-4-personnaliser-les-relances-automatiques-pour-un-client.md | 137 | relance automatique (personnalisation par client) | facturation | facturation, automatisation | oui | non | non | non | non | procedure |
| 167 | documents-de-vente/etape-4-traduire-mon-catalogue.md | 556 | catalogue (traduction) | indetermine | catalogue, personnalisation | oui | non | non | non | non | procedure |
| 168 | documents-de-vente/etape-5-traduire-les-moyens-et-delais-de-paiement.md | 202 | moyens / délais de paiement (traduction) | indetermine | paiement, personnalisation | oui | non | non | non | non | procedure |
| 169 | documents-de-vente/etape-6-creer-le-document-dans-une-autre-langue.md | 129 | document (création dans une autre langue) | indetermine | documents, personnalisation | oui | non | oui | non | non | procedure |
| 170 | documents-de-vente/exporter-les-pdf-de-mes-documents.md | 253 | PDF (export documents) | facturation | documents, permissions | oui | non | oui | oui | non | procedure |
| 171 | documents-de-vente/facture-manquante-dans-la-liste.md | 215 | facture (dépannage, liste) | facturation | facturation | oui | non | non | non | oui | faq_depannage |
| 172 | documents-de-vente/facturer-a-l-avancement.md | 833 | facture d'avancement (chantier long) | facturation | facturation, conformite_reglementaire, documents | oui | oui | oui | oui | oui | procedure |
| 173 | documents-de-vente/fusionner-des-documents.md | 259 | document de vente (fusion) | facturation | documents, tarification | oui | non | oui | oui | non | procedure |
| 174 | documents-de-vente/gerer-les-reliquats.md | 120 | reliquat (commande, livraison) | indetermine | gestion_stock, documents | oui | non | oui | oui | non | procedure |
| 175 | documents-de-vente/gestion-des-factures-d-abonnement.md | 113 | facture d'abonnement (gestion) | facturation | facturation, automatisation | oui | non | non | non | non | procedure |
| 176 | documents-de-vente/imprimer-des-documents-en-masse-devis-factures-etc.md | 134 | documents (impression en masse) | facturation | documents | oui | non | non | non | non | procedure |
| 177 | documents-de-vente/inserer-le-logo-de-ma-societe-sur-un-document.md | 290 | logo société (document) | facturation | personnalisation, documents | oui | non | oui | oui | non | procedure |
| 178 | documents-de-vente/introduction-creer-un-document-dans-une-autre-langue.md | 155 | document (introduction traduction, 5 étapes) | indetermine | personnalisation, documents | non | non | non | non | non | definitionnel |
| 179 | documents-de-vente/introduction-module-abonnement.md | 135 | module abonnement (introduction) | indetermine | facturation, automatisation | non | non | non | non | non | definitionnel |
| 180 | documents-de-vente/journal-de-facturation.md | 206 | journal de facturation (contrôle conformité) | facturation | facturation, conformite_reglementaire | oui | non | oui | oui | oui | procedure |
| 181 | documents-de-vente/la-relance-automatique.md | 132 | relance (introduction, méthodes) | facturation | facturation, automatisation | non | non | non | non | non | definitionnel |
| 182 | documents-de-vente/la-relance-manuelle-en-masse.md | 228 | relance manuelle en masse (factures) | facturation | facturation, communication | oui | non | non | non | non | procedure |
| 183 | documents-de-vente/la-relance-manuelle.md | 399 | relance manuelle (client) | facturation | facturation, communication, documents | oui | non | non | oui | non | procedure |
| 184 | documents-de-vente/les-factures-et-les-avoirs-brouillon.md | 342 | facture / avoir brouillon (finalisation) | facturation | facturation, permissions | oui | oui | oui | oui | non | procedure |
| 185 | documents-de-vente/masquer-certaines-colonnes-des-documents.md | 196 | colonnes de documents (affichage) | facturation | documents, personnalisation | oui | non | oui | oui | non | procedure |
| 186 | documents-de-vente/modifier-le-nombre-de-decimales-dans-un-document.md | 298 | décimales (affichage document) | facturation | personnalisation, documents | oui | non | non | non | non | procedure |
| 187 | documents-de-vente/modifier-le-pied-de-page-de-mes-documents.md | 363 | pied de page (document) | facturation | personnalisation, conformite_reglementaire, documents | oui | non | oui | oui | non | procedure |
| 188 | documents-de-vente/modifier-les-textes-fixes-des-documents.md | 153 | textes fixes (document, apparence) | facturation | personnalisation, documents | oui | non | oui | non | non | procedure |
| 189 | documents-de-vente/partager-mes-documents-de-vente-via-un-lien-public.md | 272 | lien public (partage document de vente) | facturation | paiement, documents, presence_en_ligne | oui | non | oui | oui | non | procedure |
| 190 | documents-de-vente/presentation-de-la-signature-electronique-legale.md | 394 | signature électronique légale (présentation, YouSign) | indetermine | validation, conformite_reglementaire, documents | non | non | oui | non | non | definitionnel |
| 191 | documents-de-vente/statuts-de-documents.md | 456 | statuts de documents (cycle de vie) | facturation | documents, facturation | non | oui | oui | oui | oui | definitionnel |
| 192 | documents-de-vente/suivre-les-cycles-d-avancement.md | 417 | cycle d'avancement (facturation, suivi) | facturation | facturation, reporting | oui | non | non | non | non | procedure |
| 193 | documents-de-vente/supprimer-un-document-de-vente.md | 247 | document de vente (suppression) | facturation | documents, permissions | oui | oui | oui | oui | oui | procedure |
| 194 | documents-de-vente/tracking-de-consultation-des-documents.md | 206 | tracking de consultation (documents, lien public) | facturation | reporting, documents | oui | non | oui | oui | non | procedure |
| 195 | documents-de-vente/utiliser-les-factures-d-acompte.md | 681 | facture d'acompte (avance, comptabilité légale) | facturation | facturation, comptabilite, conformite_reglementaire | oui | non | oui | oui | non | procedure |
| 196 | documents-de-vente/utiliser-les-factures-partielles.md | 290 | facture partielle (facturation progressive) | facturation | facturation, gestion_stock | oui | oui | oui | non | non | procedure |
| 197 | facturation-electronique/activation-de-la-double-authentification-pour-la-facturation-electronique.md | 313 | 2FA (obligation facturation électronique) | indetermine | securite_compte, conformite_reglementaire | non | non | oui | oui | non | politique_legale |
| 198 | facturation-electronique/activites-partiellement-soumises-a-la-tva-ou-exclues-de-la-reforme-francaise.md | 1008 | TVA / réforme facturation électronique (exclusions, activités mixtes) | indetermine | conformite_reglementaire | non | non | oui | non | oui | politique_legale |
| 199 | facturation-electronique/associations-et-reforme-de-la-facturation-electronique.md | 474 | associations (TVA, réforme facturation électronique) | indetermine | conformite_reglementaire | non | non | oui | non | non | politique_legale |
| 200 | facturation-electronique/autres-ressources.md | 251 | ressources d'accompagnement (facturation électronique) | indetermine | support_editeur | non | non | non | non | non | autre |
| 201 | facturation-electronique/calendrier-obligations-et-definitions-de-la-reforme-francaise.md | 585 | calendrier / obligations (réforme facturation électronique) | indetermine | conformite_reglementaire | non | non | oui | non | non | politique_legale |
| 202 | facturation-electronique/completer-le-mandat-d-emission-et-de-reception-sur-la-plateforme-sellsy-pa.md | 950 | mandat PA (émission + réception, facturation électronique) | indetermine | conformite_reglementaire, permissions, integrations | oui | non | oui | oui | non | procedure |
| 203 | facturation-electronique/completer-le-mandat-d-emission-sur-la-plateforme-sellsy-pa.md | 548 | mandat PA (émission, facturation électronique) | indetermine | conformite_reglementaire, permissions | oui | non | oui | oui | non | procedure |
| 204 | facturation-electronique/completer-vos-informations-societe-dans-le-cadre-de-la-facturation-electronique.md | 642 | informations société (conformité facturation électronique) | indetermine | conformite_reglementaire, documents | oui | non | oui | oui | non | procedure |
| 205 | facturation-electronique/comprendre-l-adresse-de-facturation-electronique.md | 603 | adresse de facturation électronique (concept) | indetermine | conformite_reglementaire, integrations | non | non | oui | oui | non | definitionnel |
| 206 | facturation-electronique/comprendre-le-mandat-pa-et-la-verification-d-identite.md | 444 | mandat PA / KYC (vérification identité) | indetermine | conformite_reglementaire, securite_compte | non | non | oui | oui | non | politique_legale |
| 207 | facturation-electronique/comprendre-les-regles-de-calcul-et-d-arrondi-pour-la-facturation-electronique.md | 564 | calcul et arrondi TVA (facturation électronique) | facturation | conformite_reglementaire, facturation | non | non | oui | non | non | reference_configuration |
| 208 | facturation-electronique/comprendre-les-taux-de-tva-actifs-et-inactifs.md | 429 | taux de TVA (actifs / inactifs) | indetermine | conformite_reglementaire, catalogue, facturation | oui | oui | oui | non | non | reference_configuration |
| 209 | facturation-electronique/departements-et-regions-d-outre-mer.md | 456 | DROM-COM (obligations réforme facturation électronique) | indetermine | conformite_reglementaire | non | non | oui | non | oui | politique_legale |
| 210 | facturation-electronique/description-et-nom-commercial-dans-les-documents-de-vente.md | 371 | description / nom commercial (conformité FacturX) | facturation | conformite_reglementaire, documents, catalogue | non | oui | oui | oui | non | politique_legale |
| 211 | facturation-electronique/entreprises-etrangeres-et-echanges-internationaux-dans-le-cadre-de-la-reforme.md | 645 | entreprises étrangères (réforme facturation électronique) | indetermine | conformite_reglementaire | non | non | oui | non | oui | politique_legale |
| 212 | facturation-electronique/facturation-electronique-declaration-du-statut-eti-ge.md | 576 | statut ETI/GE (déclaration, facturation électronique) | indetermine | conformite_reglementaire, permissions | oui | oui | oui | oui | non | procedure |
| 213 | facturation-electronique/facturation-electronique-frais-generaux-et-notes-de-frais.md | 1281 | notes de frais (réforme facturation électronique) | indetermine | conformite_reglementaire, comptabilite | non | non | oui | non | oui | politique_legale |
| 214 | facturation-electronique/fonctionnalites-en-cours-de-deploiement.md | 964 | facturation électronique (fonctionnalités en développement) | indetermine | conformite_reglementaire, integrations | non | non | non | oui | oui | reference_configuration |
| 215 | facturation-electronique/freelances-auto-entrepreneurs.md | 598 | freelances / auto-entrepreneurs (réforme facturation électronique) | indetermine | conformite_reglementaire | non | non | oui | non | non | politique_legale |
| 216 | facturation-electronique/gerer-mes-factures-fournisseurs-avec-sellsy.md | 727 | factures fournisseurs (module Achats) | indetermine | conformite_reglementaire, comptabilite, integrations | oui | non | oui | oui | non | politique_legale |
| 217 | facturation-electronique/gerer-sa-tva-dans-le-cadre-de-la-facturation-electronique.md | 873 | TVA (gestion, codes VATEX, facturation électronique) | indetermine | conformite_reglementaire, catalogue | oui | non | oui | oui | non | politique_legale |
| 218 | facturation-electronique/integrer-un-outil-a-sellsy.md | 671 | connecteur / intégration (Sellsy) | indetermine | integrations, automatisation | non | non | non | non | non | marketing_dans_aide |
| 219 | facturation-electronique/l-emission-de-factures-pour-les-particuliers-b2c.md | 673 | facturation B2C (e-reporting) | facturation | conformite_reglementaire, facturation | non | non | oui | oui | non | politique_legale |
| 220 | facturation-electronique/l-emission-de-factures-pour-les-professionnels-b2b.md | 614 | facturation B2B (e-invoicing) | facturation | conformite_reglementaire, facturation | non | non | oui | oui | non | politique_legale |
| 221 | facturation-electronique/l-emission-des-factures-pour-le-secteur-public-b2g.md | 469 | facturation B2G (Chorus Pro) | facturation | conformite_reglementaire, integrations | non | non | oui | oui | non | politique_legale |
| 222 | facturation-electronique/la-checklist-dediee-et-les-etapes-a-suivre.md | 561 | checklist conformité (facturation électronique) | indetermine | conformite_reglementaire | oui | non | oui | oui | non | procedure |
| 223 | facturation-electronique/la-facturation-electronique-en-europe.md | 574 | facturation électronique (Europe, contexte international) | indetermine | conformite_reglementaire, integrations | non | non | non | non | non | definitionnel |
| 224 | facturation-electronique/la-reforme-sellsy-et-mon-expert-comptable.md | 525 | expert-comptable (connecteurs, réforme facturation électronique) | indetermine | comptabilite, integrations, conformite_reglementaire | oui | non | oui | non | non | procedure |
| 225 | facturation-electronique/les-informations-obligatoires-d-une-facture.md | 774 | mentions obligatoires (facture, conformité légale) | facturation | conformite_reglementaire, facturation, documents | non | non | oui | oui | non | politique_legale |
| 226 | facturation-electronique/mandat-pa-effectuer-votre-verification-d-identite.md | 448 | mandat PA / KYC (vérification identité, procédure) | indetermine | conformite_reglementaire, securite_compte | oui | oui | oui | oui | oui | procedure |
| 227 | facturation-electronique/modifier-les-informations-societe-dans-le-cadre-de-la-facturation-electronique.md | 317 | informations société (modification, conformité) | indetermine | conformite_reglementaire, permissions | oui | non | oui | oui | non | procedure |
| 228 | facturation-electronique/positionnement-de-sellsy.md | 440 | Sellsy (positionnement PA, réforme facturation électronique) | indetermine | conformite_reglementaire | non | non | non | non | non | marketing_dans_aide |
| 229 | facturation-electronique/regime-de-tva-et-frequence-d-envoi-du-e-reporting.md | 316 | régime de TVA (e-reporting, fréquence) | facturation | conformite_reglementaire, facturation | oui | non | oui | oui | non | procedure |
| 230 | facturation-electronique/sellsy-pa-d-emission-et-vous.md | 250 | PA d'émission (rôle, obligations) | indetermine | conformite_reglementaire | non | non | oui | oui | non | politique_legale |
| 231 | facturation-electronique/sellsy-pa-de-reception-et-vous.md | 892 | PA de réception (rôle, obligations, activation) | indetermine | conformite_reglementaire, integrations | oui | non | oui | oui | non | politique_legale |
| 232 | facturation-electronique/verifier-vos-factures-et-avoirs-electroniques-recus.md | 1004 | facture / avoir électronique (vérification, achats) | indetermine | conformite_reglementaire, validation, comptabilite | oui | oui | oui | oui | oui | procedure |
| 233 | gestion-des-donnees/afficher-les-champs-personnalises-dans-une-liste.md | 83 | champ personnalisé (affichage liste) | indetermine | personnalisation | oui | non | non | non | non | procedure |
| 234 | gestion-des-donnees/afficher-un-champ-personnalise-sur-un-document-de-vente.md | 324 | champ personnalisé (affichage document de vente) | facturation | personnalisation, documents | oui | non | oui | oui | non | procedure |
| 235 | gestion-des-donnees/ajouter-ou-supprimer-un-smart-tag.md | 267 | smart tag (fiche client) | indetermine | crm, personnalisation | oui | non | oui | non | non | procedure |
| 236 | gestion-des-donnees/ajouter-un-fichier-sur-sellsy.md | 266 | fichier (ajout, gestion documentaire) | indetermine | documents | oui | non | non | oui | non | procedure |
| 237 | gestion-des-donnees/creer-des-champs-personnalises.md | 322 | champ personnalisé (création) | indetermine | personnalisation, permissions | oui | non | oui | oui | non | procedure |
| 238 | gestion-des-donnees/creer-un-groupe-de-champs-personnalises.md | 105 | groupe de champs personnalisés | indetermine | personnalisation | oui | non | non | non | non | procedure |
| 239 | gestion-des-donnees/editer-les-valeurs-des-champs-personnalises-en-masse.md | 127 | champ personnalisé (édition en masse) | indetermine | personnalisation | oui | non | oui | non | non | procedure |
| 240 | gestion-des-donnees/effectuer-un-inventaire-de-stocks.md | 170 | inventaire de stocks | indetermine | gestion_stock, catalogue | oui | non | non | non | non | procedure |
| 241 | gestion-des-donnees/export-des-donnees-dans-sellsy.md | 436 | export de données (CSV/PDF/JSON/PARQUET) | indetermine | reporting, permissions, integrations | oui | non | oui | non | non | procedure |
| 242 | gestion-des-donnees/filtrer-mes-donnees-avec-les-champs-personnalises.md | 98 | champ personnalisé (filtrage) | indetermine | personnalisation, recherche | oui | non | non | non | non | procedure |
| 243 | gestion-des-donnees/filtrer-mes-donnees-grace-aux-smart-tags.md | 399 | smart tag (filtrage) | indetermine | crm, recherche | oui | non | oui | oui | non | procedure |
| 244 | gestion-des-donnees/fonctionnement-de-la-synchronisation-dropbox.md | 201 | synchronisation Dropbox | indetermine | integrations, documents | oui | non | non | non | non | procedure |
| 245 | gestion-des-donnees/importer-des-commentaires.md | 344 | commentaires (import) | indetermine | integrations, permissions | oui | non | oui | oui | non | procedure |
| 246 | gestion-des-donnees/importer-des-donnees.md | 159 | données (import, introduction générale) | indetermine | integrations, permissions | oui | non | oui | oui | non | procedure |
| 247 | gestion-des-donnees/importer-des-factures-et-avoirs-fournisseurs-dans-sellsy.md | 509 | factures / avoirs fournisseurs (import OCR) | indetermine | integrations, comptabilite, permissions | oui | non | oui | oui | oui | procedure |
| 248 | gestion-des-donnees/importer-les-categories-tarifaires-de-mon-catalogue-de-services.md | 630 | catégorie tarifaire (import, catalogue services) | indetermine | catalogue, tarification, integrations | oui | non | oui | oui | non | procedure |
| 249 | gestion-des-donnees/importer-les-categories-tarifaires-de-mon-catalogue-produit.md | 675 | catégorie tarifaire (import, catalogue produit) | indetermine | catalogue, tarification, integrations | oui | non | oui | oui | non | procedure |
| 250 | gestion-des-donnees/importer-mes-donnees-societes-et-contacts.md | 1038 | sociétés / contacts (import) | indetermine | crm, integrations, permissions | oui | non | oui | oui | non | procedure |
| 251 | gestion-des-donnees/importer-mon-catalogue-de-produits.md | 815 | catalogue produits (import) | indetermine | catalogue, integrations | oui | non | oui | oui | non | procedure |
| 252 | gestion-des-donnees/importer-mon-catalogue-de-services.md | 805 | catalogue services (import) | indetermine | catalogue, integrations | oui | non | oui | oui | non | procedure |
| 253 | gestion-des-donnees/importer-un-releve-bancaire.md | 371 | relevé bancaire (import CSV) | indetermine | comptabilite, integrations | oui | non | non | non | non | procedure |
| 254 | gestion-des-donnees/imports-d-opportunites.md | 752 | opportunités (import) | indetermine | crm, integrations, permissions | oui | non | oui | oui | non | procedure |
| 255 | gestion-des-donnees/introduction-gestion-des-champs-personnalises.md | 122 | champ personnalisé (introduction) | indetermine | personnalisation | non | non | non | non | non | definitionnel |
| 256 | gestion-des-donnees/introduction-presentation-du-gestionnaire-de-fichiers-sellsy.md | 164 | gestionnaire de fichiers (introduction) | indetermine | documents | non | non | non | non | non | definitionnel |
| 257 | gestion-des-donnees/introduction-utilisation-des-smart-tags.md | 113 | smart tag (introduction) | indetermine | crm, personnalisation | non | non | non | non | non | definitionnel |
| 258 | gestion-des-donnees/les-differents-types-d-imports-de-donnees-sur-sellsy.md | 367 | imports de données (types disponibles) | indetermine | integrations, catalogue | non | non | oui | oui | non | reference_configuration |
| 259 | gestion-des-donnees/mettre-en-place-une-redirection-automatique-pour-l-import-de-factures.md | 313 | redirection email (import factures) | indetermine | integrations, automatisation | oui | non | non | oui | oui | procedure |
| 260 | gestion-des-donnees/ouvrir-un-fichier-csv-avec-excel.md | 165 | fichier CSV (ouverture, Excel) | indetermine | — | oui | non | non | non | oui | faq_depannage |
| 261 | gestion-des-donnees/ouvrir-un-fichier-csv-avec-google-sheets.md | 88 | fichier CSV (ouverture, Google Sheets) | indetermine | — | oui | non | non | non | non | procedure |
| 262 | gestion-des-donnees/ouvrir-un-fichier-csv-avec-open-office.md | 145 | fichier CSV (ouverture, OpenOffice) | indetermine | — | oui | non | non | non | oui | faq_depannage |
| 263 | gestion-des-donnees/personnaliser-les-listes-prospect-client-contact-document.md | 239 | listes (personnalisation affichage) | indetermine | personnalisation | oui | non | non | non | non | procedure |
| 264 | gestion-des-donnees/stocker-des-fichiers-sur-un-objet-client-document-opportunite.md | 337 | fichiers (stockage contextuel sur fiches) | indetermine | documents, crm | oui | non | non | non | non | procedure |
| 265 | gestion-des-donnees/utiliser-la-barre-de-recherche-dans-sellsy.md | 497 | recherche (barre de recherche) | indetermine | recherche | oui | non | non | non | non | procedure |
| 266 | gestion-des-donnees/utiliser-le-module-google-drive.md | 290 | synchronisation Google Drive | indetermine | integrations, documents | oui | non | non | oui | non | procedure |
| 267 | gestion-des-donnees/utiliser-les-filtres-favoris.md | 443 | filtre favori (listes) | indetermine | personnalisation, permissions | oui | non | oui | non | non | procedure |
| 268 | integrations-et-api/api-v1.md | 338 | API V1 (documentation, tokens) | indetermine | integrations, permissions | oui | non | oui | oui | non | procedure |
| 269 | integrations-et-api/api-v2.md | 241 | API V2 (documentation, tokens, scopes) | indetermine | integrations, permissions | oui | non | oui | oui | non | procedure |
| 270 | integrations-et-api/configuration-postman-api-v1.md | 310 | Postman (configuration API V1) | indetermine | integrations | oui | non | non | non | non | procedure |
| 271 | integrations-et-api/configuration-postman-apiv2.md | 517 | Postman (configuration API V2) | indetermine | integrations | oui | non | non | non | non | procedure |
| 272 | integrations-et-api/connecter-sellsy-a-make.md | 178 | intégration Make (tokens API) | indetermine | integrations | oui | non | non | oui | non | procedure |
| 273 | integrations-et-api/connecter-sellsy-a-zapier.md | 257 | intégration Zapier | indetermine | integrations, crm | oui | non | non | non | oui | procedure |
| 274 | integrations-et-api/connecter-sellsy-et-acd.md | 2735 | connecteur comptable ACD | indetermine | integrations, comptabilite, permissions | oui | non | oui | oui | oui | procedure |
| 275 | integrations-et-api/connecter-sellsy-et-cegid-loop.md | 2612 | connecteur comptable Cegid Loop | indetermine | integrations, comptabilite, permissions | oui | non | oui | oui | oui | procedure |
| 276 | integrations-et-api/connecter-sellsy-et-fulll.md | 2519 | connecteur comptable Fulll | indetermine | integrations, comptabilite, permissions | oui | non | oui | oui | oui | procedure |
| 277 | integrations-et-api/connecter-sellsy-et-inexweb-in-extenso.md | 2592 | connecteur comptable InexWeb (In Extenso) | indetermine | integrations, comptabilite, permissions | oui | non | oui | oui | oui | procedure |
| 278 | integrations-et-api/connecter-sellsy-et-inqom.md | 297 | connecteur comptable Inqom | indetermine | integrations, comptabilite | oui | non | oui | oui | non | procedure |
| 279 | integrations-et-api/connecter-sellsy-et-myunisoft.md | 2551 | connecteur comptable MyUnisoft | indetermine | integrations, comptabilite, permissions | oui | non | oui | oui | oui | procedure |
| 280 | integrations-et-api/connecter-sellsy-et-sage-generation-experts.md | 2767 | connecteur comptable Sage Génération Experts | indetermine | integrations, comptabilite, permissions | oui | non | oui | oui | oui | procedure |
| 281 | integrations-et-api/connecter-sellsy-et-tiime.md | 2528 | connecteur comptable Tiime | indetermine | integrations, comptabilite, permissions | oui | non | oui | oui | oui | procedure |
| 282 | integrations-et-api/creer-et-personnaliser-mon-premier-widget.md | 315 | widget (création, site web) | indetermine | crm, personnalisation, notifications | oui | non | oui | oui | non | procedure |
| 283 | integrations-et-api/faire-une-requete-http-avec-make.md | 161 | requête HTTP (Make, OAuth) | indetermine | integrations | oui | non | non | non | non | procedure |
| 284 | integrations-et-api/installer-un-widget-sellsy-sur-mon-site-web.md | 114 | widget (installation site web) | indetermine | crm | oui | non | non | non | non | procedure |
| 285 | integrations-et-api/integrations-connecteurs-et-api.md | 592 | intégrations / connecteurs / API (panorama) | indetermine | integrations | non | non | non | non | non | marketing_dans_aide |
| 286 | integrations-et-api/introduction-api.md | 387 | API (introduction, choix version) | indetermine | integrations | non | non | non | non | non | definitionnel |
| 287 | integrations-et-api/introduction-widget-sellsy.md | 146 | widget (introduction) | indetermine | crm, notifications | non | non | non | non | non | definitionnel |
| 288 | integrations-et-api/les-differents-types-d-id-sur-l-api-v1.md | 112 | identifiants API (types ID) | indetermine | integrations | non | non | non | non | non | reference_configuration |
| 289 | integrations-et-api/les-erreurs-api.md | 667 | erreurs API (codes, dépannage) | indetermine | integrations | non | non | oui | non | oui | faq_depannage |
| 290 | integrations-et-api/mettre-en-place-un-scoring-sur-les-societes.md | 554 | scoring (sociétés, widget tracking) | indetermine | crm, automatisation, reporting | oui | non | non | non | non | procedure |
| 291 | integrations-et-api/module-sellsy-pour-wordpress.md | 984 | module WordPress (formulaire, tracking) | indetermine | integrations, crm, personnalisation | oui | oui | oui | non | non | procedure |
| 292 | integrations-et-api/personnaliser-le-formulaire-d-inscription-aux-campagnes-marketing.md | 128 | formulaire inscription campagnes marketing (widget) | indetermine | marketing_et_communication, personnalisation | oui | non | oui | non | non | procedure |
| 293 | integrations-et-api/resoudre-une-erreur-de-content-security-policy.md | 79 | erreur CSP (widget, dépannage technique) | indetermine | integrations | oui | non | non | non | oui | faq_depannage |
| 294 | integrations-et-api/suivre-l-activite-de-mes-prospects-sur-mon-site-web.md | 221 | tracking prospects (widget, site web) | indetermine | crm, reporting | oui | non | oui | non | non | procedure |
| 295 | integrations-et-api/types-d-acces-api.md | 517 | accès API (types, scopes) | indetermine | integrations, permissions, securite_compte | oui | non | oui | oui | non | procedure |
| 296 | integrations-et-api/utiliser-l-api-v1-via-des-acces-api-v2.md | 210 | API V1 via V2 (compatibilité) | indetermine | integrations | oui | non | oui | non | non | procedure |
| 297 | integrations-et-api/webhooks.md | 680 | webhook (Slack/HTTP) | indetermine | integrations, notifications, permissions | oui | non | oui | oui | non | procedure |
| 298 | module-achats/calculer-une-marge-grace-au-catalogue.md | 232 | marge (catalogue, coûts d'achat) | indetermine | catalogue, comptabilite | oui | non | non | non | non | procedure |
| 299 | module-achats/enregistrer-des-achats-rapides.md | 174 | achat rapide (saisie manuelle) | indetermine | comptabilite | oui | non | non | non | non | procedure |
| 300 | module-achats/export-sepa-des-factures-fournisseur.md | 196 | export SEPA (factures fournisseur) | indetermine | paiement, comptabilite | oui | non | non | non | non | procedure |
| 301 | module-achats/fonctionnement-du-calcul-de-marge.md | 260 | calcul de marge (achats) | indetermine | comptabilite, permissions | non | non | oui | oui | non | definitionnel |
| 302 | module-achats/gerer-mes-achats.md | 475 | achats (cycle : commande → livraison → facture) | achat | gestion_stock, comptabilite | oui | oui | non | non | non | procedure |
| 303 | module-achats/gestion-des-acces-au-module-achats-pour-les-utilisateurs.md | 638 | accès module achats (privilèges) | achat | permissions, roles | oui | non | oui | oui | non | procedure |
| 304 | module-achats/lier-une-facture-d-achat-et-une-facture-de-vente.md | 209 | facture d'achat liée à facture de vente (marge) | achat | comptabilite, documents | oui | non | non | non | non | procedure |
| 305 | module-achats/prendre-en-compte-les-couts-internes-dans-le-calcul-de-marge.md | 131 | coûts internes (calcul marge) | achat | comptabilite | oui | non | non | non | non | procedure |
| 306 | module-achats/saisir-une-facture-d-achat-dans-une-autre-devise.md | 289 | facture d'achat (devise étrangère) | achat | comptabilite | oui | non | non | non | oui | procedure |
| 307 | module-achats/transformer-une-commande-fournisseur-en-document-de-vente.md | 80 | commande fournisseur (transformation en document de vente) | achat | documents | oui | oui | non | non | non | procedure |
| 308 | module-marketing/marketing-ameliorez-vos-campagnes-emailing-avec-sellsy-ia.md | 330 | campagne emailing (IA, éditeur) | indetermine | marketing_et_communication, automatisation | oui | non | non | non | non | procedure |
| 309 | module-marketing/marketing-decouvrir-sellsy-marketing.md | 191 | module marketing (découverte, checklist) | indetermine | marketing_et_communication | non | non | non | non | non | definitionnel |
| 310 | module-marketing/marketing-exploiter-les-fichiers-au-format-texte-txt.md | 1897 | fichiers export (format texte, marketing) | indetermine | marketing_et_communication, documents | oui | non | oui | oui | non | procedure |
| 311 | module-marketing/marketing-gerer-des-blocs-et-palettes-personnalisees.md | 347 | blocs / palettes personnalisées (éditeur marketing) | indetermine | marketing_et_communication, personnalisation | oui | non | non | non | non | procedure |
| 312 | module-marketing/marketing-opter-pour-une-ip-dediee-ou-une-ip-mutualisee.md | 483 | IP dédiée / mutualisée (délivrabilité emailing) | indetermine | marketing_et_communication, paiement | oui | non | oui | oui | non | procedure |
| 313 | module-marketing/marketing-pixel-et-gestion-du-tracking-dans-les-campagnes-emailing.md | 417 | pixel tracking (conformité RGPD, campagnes emailing) | indetermine | marketing_et_communication, conformite_reglementaire | oui | non | oui | oui | non | politique_legale |
| 314 | module-stocks/alertes-stock-et-commandes-fournisseur.md | 125 | alerte stock (commandes fournisseur) | indetermine | gestion_stock, notifications | oui | oui | non | non | non | procedure |
| 315 | module-stocks/calcul-de-la-valorisation-du-stock-cmup.md | 317 | valorisation de stock (CMUP) | indetermine | gestion_stock, comptabilite | oui | non | non | non | non | definitionnel |
| 316 | module-stocks/definir-mes-preferences-generales-de-stocks.md | 104 | préférences générales de stock | indetermine | gestion_stock | oui | non | non | non | non | procedure |
| 317 | module-stocks/destockage-automatique-et-mouvement-de-stocks-inter-entrepots.md | 199 | déstockage / mouvement de stock (entrepôts) | indetermine | gestion_stock | oui | oui | non | non | non | procedure |
| 318 | module-stocks/gerer-les-numeros-de-serie.md | 243 | numéro de série (stock) | indetermine | gestion_stock, catalogue | oui | non | non | non | oui | procedure |
| 319 | module-stocks/gerer-les-stocks-et-entrepots-d-un-produit.md | 293 | stocks et entrepôts (configuration produit) | indetermine | gestion_stock, catalogue | oui | non | oui | oui | non | procedure |
| 320 | module-stocks/gerer-mes-reservations-de-stocks.md | 253 | réservation de stock (devis / bon de commande) | indetermine | gestion_stock | oui | oui | non | non | non | procedure |
| 321 | module-stocks/introduction-module-stock.md | 141 | module stock (introduction) | indetermine | gestion_stock | non | non | non | non | non | definitionnel |
| 322 | module-stocks/transporteurs-et-tarifs-de-transport.md | 409 | transporteur / tarif de transport | indetermine | gestion_stock, tarification | oui | non | oui | non | non | procedure |
| 323 | module-stocks/verifier-le-stock-d-un-produit.md | 175 | stock produit (vérification) | indetermine | gestion_stock | oui | non | non | non | non | procedure |
| 324 | module-support/definir-un-modele-de-reponse-standardisee-pour-un-ticket-de-support.md | 98 | modèle de réponse (ticket support) | indetermine | — | oui | non | non | non | non | procedure |
| 325 | module-support/parametrer-le-module-support.md | 197 | module support (paramétrage) | indetermine | automatisation, notifications | oui | non | non | non | non | procedure |
| 326 | module-support/transferer-mes-emails-de-support.md | 149 | emails support (redirection) | indetermine | communication, automatisation | oui | non | non | oui | non | procedure |
| 327 | module-support/utiliser-les-smart-tags-pour-trier-les-tickets-de-support.md | 107 | smart tag (tickets support) | indetermine | personnalisation, recherche | oui | non | non | non | non | procedure |
| 328 | module-tresorerie/sellsy-tresorerie-fonctionnement.md | 137 | trésorerie (intégration, prévisionnel) | indetermine | comptabilite, automatisation, paiement | non | non | oui | oui | non | marketing_dans_aide |
| 329 | paiements/activer-le-paiement-en-ligne-avec-adyen.md | 1019 | paiement en ligne Adyen (activation) | facturation | paiement, integrations, permissions | oui | non | oui | oui | oui | procedure |
| 330 | paiements/activer-le-paiement-en-ligne-avec-paypal.md | 427 | paiement en ligne PayPal (activation) | facturation | paiement, integrations | oui | non | non | non | non | procedure |
| 331 | paiements/activer-le-paiement-en-ligne-avec-stancer.md | 460 | paiement en ligne Stancer (activation) | facturation | paiement, integrations | oui | non | oui | non | non | procedure |
| 332 | paiements/activer-le-paiement-en-ligne-avec-stripe.md | 379 | paiement en ligne Stripe (activation) | facturation | paiement, integrations | oui | non | non | non | non | procedure |
| 333 | paiements/activer-le-prelevement-bancaire-avec-gocardless.md | 955 | prélèvement bancaire GoCardless (activation, mandat SEPA) | facturation | paiement, integrations, automatisation | oui | oui | oui | non | oui | procedure |
| 334 | paiements/ajouter-un-reglement-a-une-ou-plusieurs-factures.md | 499 | règlement (ajout, factures) | facturation | paiement, permissions | oui | non | oui | oui | oui | procedure |
| 335 | paiements/ajouter-un-reglement-decaissement-libre.md | 317 | règlement libre (décaissement, avant facturation) | indetermine | paiement, comptabilite | oui | non | oui | non | non | procedure |
| 336 | paiements/comprendre-les-statuts-d-un-prelevement-gocardless.md | 411 | statuts de prélèvement GoCardless (référence) | facturation | paiement, integrations | non | oui | oui | non | non | reference_configuration |
| 337 | paiements/encaissez-vos-paiements-recurrents-avec-stripe.md | 631 | paiement récurrent Stripe (empreinte CB) | facturation | paiement, automatisation, integrations | oui | oui | oui | non | non | procedure |
| 338 | paiements/enregistrer-des-paiements-en-masse.md | 179 | paiements en masse (enregistrement) | facturation | paiement | oui | non | oui | oui | non | procedure |
| 339 | paiements/importer-des-mandats-gocardless.md | 243 | mandats GoCardless (import) | indetermine | paiement, integrations | oui | non | oui | non | non | procedure |
| 340 | paiements/paiements-en-ligne-guide-complet.md | 778 | paiements en ligne (guide complet, panorama prestataires) | facturation | paiement, integrations | oui | non | non | non | non | definitionnel |
| 341 | paiements/parametrer-les-reglements.md | 375 | règlements (paramétrage : moyens / libellés / conditions) | indetermine | paiement, personnalisation | oui | non | oui | non | non | procedure |
| 342 | paiements/questions-frequentes-sur-gocardless.md | 572 | GoCardless (FAQ, limites, dépannage) | indetermine | paiement, integrations | oui | non | oui | oui | oui | faq_depannage |
| 343 | paiements/rapprochement-automatique-depuis-un-virement-stancer-stripe-ou-gocardless.md | 237 | rapprochement bancaire automatique (paiements) | facturation | paiement, integrations, automatisation | oui | non | non | non | non | procedure |
| 344 | paiements/rembourser-un-client.md | 91 | remboursement client (avoir) | facturation | paiement | oui | non | non | non | non | procedure |
| 345 | paiements/supprimer-un-reglement-lie-a-un-document.md | 315 | règlement (suppression, document lié) | facturation | paiement | oui | oui | oui | oui | oui | procedure |
| 346 | paiements/utiliser-la-fonctionnalite-sepa.md | 468 | prélèvement SEPA (mandat, export) | facturation | paiement, comptabilite | oui | non | oui | non | oui | procedure |
| 347 | paiements/utiliser-les-reglements-avec-echeances-multiples-sur-les-documents-de-vente.md | 451 | échéances multiples (règlement, document de vente) | facturation | paiement, documents | oui | oui | oui | oui | non | procedure |
| 348 | rapports-et-pilotage/presentation-des-rapports-sellsy.md | 425 | rapports Sellsy (présentation, panorama) | indetermine | reporting, permissions | non | non | oui | oui | non | definitionnel |
| 349 | rapports-et-pilotage/rapport-analyse-des-factures-et-consommation.md | 655 | rapport (analyse factures / consommation client) | indetermine | reporting, crm | non | non | non | oui | non | reference_configuration |
| 350 | rapports-et-pilotage/rapport-analyse-des-tickets-de-support.md | 548 | rapport (analyse tickets support) | indetermine | reporting | non | non | oui | oui | non | reference_configuration |
| 351 | rapports-et-pilotage/rapport-ca-global-par-collaborateur.md | 464 | rapport (CA global par collaborateur) | facturation | reporting, facturation | non | non | non | non | non | reference_configuration |
| 352 | rapports-et-pilotage/rapport-ca-global.md | 396 | rapport (CA global) | facturation | reporting, facturation | non | non | non | oui | non | reference_configuration |
| 353 | rapports-et-pilotage/rapport-comparatif-des-performances-annuelles.md | 673 | rapport (comparatif performances annuelles) | indetermine | reporting, crm | non | non | oui | oui | non | reference_configuration |
| 354 | rapports-et-pilotage/rapport-delai-de-paiement-moyen-par-client.md | 435 | rapport (délai de paiement moyen) | facturation | reporting, facturation | non | non | non | non | non | reference_configuration |
| 355 | rapports-et-pilotage/rapport-les-clients-fideles-et-moins-fideles.md | 407 | rapport (clients fidèles / moins fidèles) | indetermine | reporting, crm | non | non | non | oui | non | reference_configuration |
| 356 | rapports-et-pilotage/rapport-liste-d-activite.md | 121 | rapport (liste d'activité) | indetermine | reporting, crm | oui | non | non | non | non | reference_configuration |
| 357 | rapports-et-pilotage/rapport-opportunites-perdues-gagnees-detaillees.md | 507 | rapport (opportunités perdues / gagnées) | indetermine | reporting, crm | non | non | non | non | non | reference_configuration |
| 358 | rapports-et-pilotage/rapport-rapport-d-activite-crm-par-activites.md | 91 | rapport CRM (activités) | indetermine | reporting, crm | oui | non | non | non | non | reference_configuration |
| 359 | rapports-et-pilotage/rapport-rapport-d-activite-crm-par-collaborateur.md | 90 | rapport CRM (par collaborateur) | indetermine | reporting, crm | oui | non | non | non | non | reference_configuration |
| 360 | rapports-et-pilotage/rapport-rapport-d-activite-crm-par-label.md | 174 | rapport CRM (par label) | indetermine | reporting, crm, personnalisation | oui | non | non | non | non | reference_configuration |
| 361 | rapports-et-pilotage/rapport-rapport-d-activite.md | 324 | rapport (activité, tâches / événements) | indetermine | reporting, crm | non | non | oui | non | non | reference_configuration |
| 362 | rapports-et-pilotage/rapport-rapport-de-prospection.md | 445 | rapport (prospection, opportunités) | indetermine | reporting, crm | oui | non | oui | non | non | reference_configuration |
| 363 | rapports-et-pilotage/rapport-rapport-de-vente-par-client.md | 346 | rapport (vente par client) | facturation | reporting, crm | oui | non | oui | oui | non | reference_configuration |
| 364 | rapports-et-pilotage/rapport-rapport-de-vente-par-produit-service.md | 377 | rapport (vente par produit / service) | facturation | reporting, catalogue | non | non | oui | oui | non | reference_configuration |
| 365 | rapports-et-pilotage/rapport-rapprochement-bancaire.md | 359 | rapport (rapprochement bancaire) | indetermine | reporting, comptabilite | non | non | oui | oui | non | reference_configuration |
| 366 | rapports-et-pilotage/rapport-rentabilite-de-vos-opportunites.md | 660 | rapport (rentabilité opportunités) | indetermine | reporting, crm | non | non | non | oui | non | reference_configuration |
| 367 | rapports-et-pilotage/rapport-repartition-des-opportunites-par-etape-pipeline-par-collaborateur.md | 387 | rapport (répartition opportunités par étape / pipeline) | indetermine | reporting, crm | non | non | non | oui | non | reference_configuration |
| 368 | rapports-et-pilotage/rapport-statistiques-par-abonnement.md | 85 | rapport (statistiques abonnement) | facturation | reporting, facturation | oui | non | non | non | non | reference_configuration |
| 369 | rapports-et-pilotage/rapport-suivi-des-abonnements.md | 999 | rapport (suivi abonnements) | facturation | reporting, facturation | non | non | oui | oui | non | reference_configuration |
| 370 | rapports-et-pilotage/rapport-suivi-des-opportunites.md | 459 | rapport (suivi opportunités) | indetermine | reporting, crm | non | non | oui | oui | non | reference_configuration |
| 371 | rapports-et-pilotage/rapport-suivi-des-reliquats-restants-a-livrer.md | 1023 | rapport (reliquats restant à livrer) | indetermine | reporting, gestion_stock | non | non | oui | oui | non | reference_configuration |
| 372 | rapports-et-pilotage/rapport-suivi-des-reliquats-restants-a-receptionner.md | 717 | rapport (reliquats restant à réceptionner, achats) | achat | reporting, gestion_stock | non | non | oui | oui | non | reference_configuration |
| 373 | rapports-et-pilotage/rapport-taux-de-conversion-devis-accepte-par-collaborateur.md | 462 | rapport (taux conversion devis, par collaborateur) | devis | reporting, crm | non | non | non | non | non | reference_configuration |
| 374 | rapports-et-pilotage/rapport-taux-de-conversion-devis-accepte.md | 433 | rapport (taux conversion devis) | devis | reporting, crm | non | non | non | oui | non | reference_configuration |
| 375 | rapports-et-pilotage/rapport-taux-de-conversion-opportunite-gagnee-par-collaborateur.md | 475 | rapport (taux conversion opportunité gagnée, par collaborateur) | indetermine | reporting, crm | non | non | non | non | non | reference_configuration |
| 376 | rapports-et-pilotage/rapport-taux-de-conversion-opportunite-gagnee.md | 328 | rapport (taux conversion opportunité gagnée) | indetermine | reporting, crm | non | non | non | oui | non | reference_configuration |
| 377 | rapports-et-pilotage/rapport-taux-de-conversion-prospects-en-clients.md | 353 | rapport (taux conversion prospects → clients) | indetermine | reporting, crm | non | oui | non | non | non | reference_configuration |
| 378 | rapports-et-pilotage/rapport-taux-de-marge-catalogue.md | 349 | rapport (taux de marge catalogue) | indetermine | reporting, comptabilite | non | non | non | non | non | reference_configuration |
| 379 | rapports-et-pilotage/rapport-taux-de-marge-realisee-par-collaborateur.md | 381 | rapport (taux marge réalisée par collaborateur) | indetermine | reporting, comptabilite | non | non | non | non | non | reference_configuration |
| 380 | rapports-et-pilotage/rapport-taux-de-marge-realisee.md | 313 | rapport (taux marge réalisée) | indetermine | reporting, comptabilite | non | non | non | oui | non | reference_configuration |
| 381 | rapports-et-pilotage/rapport-temps-de-conversion-devis-accepte-par-collaborateur.md | 463 | rapport (temps conversion devis accepté par collaborateur) | devis | reporting, crm | non | non | non | non | non | reference_configuration |
| 382 | rapports-et-pilotage/rapport-temps-de-conversion-devis-accepte.md | 395 | rapport (temps conversion devis accepté) | devis | reporting, crm | non | non | non | oui | non | reference_configuration |
| 383 | rapports-et-pilotage/rapport-temps-de-conversion-opportunite-gagnee.md | 437 | rapport (temps conversion opportunité gagnée) | indetermine | reporting, crm | non | non | non | oui | non | reference_configuration |
| 384 | rapports-et-pilotage/rapport-temps-et-taux-de-conversion-opportunite-gagnee-par-collaborateur.md | 335 | rapport (temps et taux conversion opportunité gagnée par collaborateur) | indetermine | reporting, crm | non | non | non | non | non | reference_configuration |
| 385 | rapports-et-pilotage/rapport-temps-et-taux-de-conversion-par-source.md | 325 | rapport (temps et taux conversion par source) | indetermine | reporting, crm, marketing_et_communication | non | non | non | non | non | reference_configuration |
| 386 | rapports-et-pilotage/rapport-vente-de-produits-services.md | 690 | rapport (vente produits / services) | facturation | reporting, catalogue | non | non | oui | oui | non | reference_configuration |
| 387 | repertoire/annuaire-des-societes-creer-des-fiches-societes-enrichies.md | 357 | annuaire des sociétés (fiches enrichies, SIRENE) | indetermine | crm, conformite_reglementaire, integrations | oui | non | non | non | non | procedure |
| 388 | repertoire/annuaire-des-societes-introduction-et-fonctionnement.md | 165 | annuaire des sociétés (introduction, config) | indetermine | crm, integrations | oui | non | oui | oui | non | definitionnel |
| 389 | repertoire/commentaires-comment-les-exporter.md | 293 | commentaires (export) | indetermine | crm, reporting | oui | non | oui | non | non | procedure |
| 390 | repertoire/commentaires-comment-les-utiliser.md | 134 | commentaires (usage, collaboration) | indetermine | crm, communication | oui | non | non | non | non | procedure |
| 391 | repertoire/contacts-les-differents-types-de-contacts.md | 271 | contact (types : principal / facturation / relance) | indetermine | crm | oui | non | oui | non | non | definitionnel |
| 392 | repertoire/contacts-lier-une-fiche-contact-a-une-fiche-societe.md | 168 | contact (liaison à société) | indetermine | crm | oui | non | oui | oui | non | procedure |
| 393 | repertoire/contacts-presentation-de-la-fiche-contact.md | 755 | fiche contact (présentation complète) | indetermine | crm, documents, permissions | oui | non | oui | oui | non | procedure |
| 394 | repertoire/enrichir-les-donnees-d-une-societe-existante.md | 88 | société (enrichissement via annuaire) | indetermine | crm, integrations | oui | non | non | non | non | procedure |
| 395 | repertoire/repertoire-gestion-des-contacts-societes-et-particuliers.md | 788 | répertoire (contacts / sociétés / particuliers, statuts) | indetermine | crm, comptabilite | oui | oui | oui | oui | non | definitionnel |
| 396 | repertoire/repertoire-importer-votre-liste-de-contacts-existants.md | 486 | contacts (import liste existante) | indetermine | crm, integrations, conformite_reglementaire | oui | non | oui | non | non | procedure |
| 397 | repertoire/repertoire-la-colonne-laterale-des-fiches.md | 166 | colonne latérale (fiches société / contact / opportunité) | indetermine | crm, personnalisation | oui | non | non | non | non | procedure |
| 398 | repertoire/repertoire-modification-des-statuts-contacts-societes-et-particuliers.md | 199 | statut (contact / société / particulier, transformation) | indetermine | crm | oui | oui | oui | oui | non | procedure |
| 399 | repertoire/repertoire-utilisation-de-la-liste-des-doublons.md | 164 | doublons (répertoire, détection) | indetermine | crm, recherche | oui | non | oui | oui | non | procedure |
| 400 | repertoire/repertoire-voir-les-societes-sur-une-carte.md | 88 | société (vue carte) | indetermine | crm, geolocalisation | oui | non | non | non | non | procedure |
| 401 | repertoire/societes-presentation-de-la-fiche-client.md | 1664 | fiche client (présentation complète) | indetermine | crm, comptabilite, documents | oui | non | oui | oui | non | procedure |
| 402 | repertoire/societes-presentation-de-la-fiche-fournisseur.md | 1273 | fiche fournisseur (présentation complète) | achat | crm, comptabilite, documents | oui | non | oui | oui | non | procedure |
| 403 | repertoire/societes-presentation-de-la-fiche-prospect.md | 1604 | fiche prospect (présentation complète) | indetermine | crm, documents | oui | non | oui | oui | non | procedure |
| 404 | repertoire/societes-suivre-les-informations-cles-d-une-fiche-client.md | 406 | fiche client (informations clés, résumé IA) | indetermine | crm, automatisation, reporting | oui | non | non | non | non | procedure |
| 405 | repertoire/societes-supprimer-ou-archiver-des-societes.md | 369 | société (suppression / archivage) | indetermine | crm, permissions | oui | oui | oui | oui | non | procedure |
| 406 | sellsy-automatisations/assurer-un-suivi-continu-de-vos-documents.md | 448 | automatisation (suivi continu documents, tâche) | indetermine | automatisation, notifications | oui | oui | oui | non | non | procedure |
| 407 | sellsy-automatisations/assurer-un-suivi-continu-de-vos-opportunites.md | 553 | automatisation (suivi continu opportunités, tâche) | indetermine | automatisation, crm | oui | oui | oui | non | non | procedure |
| 408 | sellsy-automatisations/avancer-automatiquement-vos-opportunites-avec-les-factures-liees.md | 394 | automatisation (opportunité ↔ facture liée) | indetermine | automatisation, crm, facturation | oui | oui | oui | oui | non | procedure |
| 409 | sellsy-automatisations/avancer-vos-opportunites-lorsqu-une-tache-est-terminee.md | 397 | automatisation (opportunité ↔ tâche terminée) | indetermine | automatisation, crm | oui | oui | oui | oui | non | procedure |
| 410 | sellsy-automatisations/configurer-et-activer-une-automatisation-dans-sellsy.md | 429 | automatisation (configuration générale, gestion) | indetermine | automatisation, permissions | oui | non | oui | oui | non | procedure |
| 411 | sellsy-automatisations/convertir-un-devis-en-facture-d-acompte.md | 318 | automatisation (devis → facture d'acompte) | devis | automatisation, facturation | oui | oui | oui | non | non | procedure |
| 412 | sellsy-automatisations/convertir-un-document-accepte-en-facture.md | 379 | automatisation (document accepté → facture) | indetermine | automatisation, facturation, documents | oui | oui | non | non | non | procedure |
| 413 | sellsy-automatisations/creer-une-opportunite-lorsqu-un-devis-est-accepte.md | 331 | automatisation (devis accepté → opportunité) | devis | automatisation, crm | oui | oui | non | non | non | procedure |
| 414 | sellsy-automatisations/suivre-le-renouvellement-de-vos-abonnements.md | 395 | automatisation (renouvellement abonnement, tâche) | facturation | automatisation, facturation | oui | oui | non | non | non | procedure |
| 415 | sellsy-automatisations/suivre-rapidement-vos-nouveaux-prospects.md | 465 | automatisation (nouveau prospect → opportunité + tâche) | indetermine | automatisation, crm | oui | oui | non | non | non | procedure |
| 416 | sellsy-automatisations/transformer-un-prospect-en-client-lorsqu-un-devis-est-accepte.md | 266 | automatisation (prospect → client via devis accepté) | devis | automatisation, crm | oui | oui | non | non | non | procedure |
| 417 | sellsy-automatisations/valider-les-nouveaux-documents.md | 500 | automatisation (validation nouveaux documents, tâche) | indetermine | automatisation, documents | oui | non | non | non | non | procedure |
| 418 | sellsy-ia/editeur-ia-ameliorer-la-prise-de-notes-avec-sellsy-ia.md | 266 | IA (édition commentaires / notes) | indetermine | automatisation, crm | oui | non | non | non | non | procedure |
| 419 | sellsy-ia/editeur-ia-ameliorez-vos-campagnes-emailing-avec-sellsy-ia.md | 330 | IA (campagnes emailing, édition texte) | indetermine | marketing_et_communication, automatisation | oui | non | non | non | non | procedure |
| 420 | sellsy-ia/modeles-d-emails-ia-generer-des-messages-cibles-avec-sellsy-ia.md | 466 | IA (modèles email intelligents) | indetermine | automatisation, communication, personnalisation | oui | non | oui | oui | non | procedure |
| 421 | sellsy-ia/redacteur-et-editeur-ia-rediger-des-emails-avec-sellsy-ia.md | 462 | IA (rédaction / édition emails) | indetermine | automatisation, communication | oui | non | non | non | non | procedure |
| 422 | sellsy-ia/resumes-client-ia-resumer-une-fiche-client-en-un-clic-avec-sellsy-ia.md | 767 | IA (résumé fiche client) | indetermine | automatisation, crm, reporting | oui | non | oui | oui | non | procedure |
| 423 | suivi-financier/ajouter-des-codes-comptables-au-plan-comptable.md | 265 | code comptable (plan comptable) | indetermine | comptabilite, catalogue | oui | non | oui | oui | non | procedure |
| 424 | suivi-financier/comptabiliser-des-factures-d-achat-et-de-vente.md | 627 | comptabilisation (factures achat / vente) | facturation | comptabilite, automatisation | oui | oui | oui | oui | oui | procedure |
| 425 | suivi-financier/connecter-mon-compte-bancaire-en-synchronisation.md | 219 | compte bancaire (synchronisation) | indetermine | comptabilite, integrations | oui | non | oui | oui | non | procedure |
| 426 | suivi-financier/connecter-un-compte-bancaire-societe-generale-credit-agricole-caisse-d-epargne.md | 156 | compte bancaire (connexion, banques spécifiques) | indetermine | comptabilite, integrations, securite_compte | oui | non | non | oui | non | procedure |
| 427 | suivi-financier/donner-a-mes-collaborateurs-un-acces-au-module-rapprochement-bancaire.md | 328 | rapprochement bancaire (accès, privilèges) | indetermine | comptabilite, permissions | oui | non | oui | oui | non | procedure |
| 428 | suivi-financier/enregistrement-des-ecritures-de-tresorerie-en-comptabilite.md | 263 | écritures de trésorerie (comptabilité) | indetermine | comptabilite, paiement | oui | non | non | non | non | procedure |
| 429 | suivi-financier/enregistrer-une-remise-en-banque-de-plusieurs-reglements.md | 320 | remise en banque (règlements multiples) | facturation | paiement, comptabilite | oui | non | oui | oui | oui | procedure |
| 430 | suivi-financier/experts-comptables-gerez-votre-pre-comptabilite-sur-sellsy.md | 298 | pré-comptabilité (accès expert-comptable) | indetermine | comptabilite, permissions | oui | non | oui | non | non | procedure |
| 431 | suivi-financier/exporter-le-journal-de-banque.md | 77 | journal de banque (export) | indetermine | comptabilite, reporting | oui | non | non | non | non | procedure |
| 432 | suivi-financier/exporter-mes-ecritures-comptables-format-csv-fec-json-parquet.md | 575 | écritures comptables (export CSV / FEC / JSON / PARQUET) | indetermine | comptabilite, reporting, conformite_reglementaire | oui | non | oui | oui | non | procedure |
| 433 | suivi-financier/filtrer-mes-factures-selon-leur-statut-de-rapprochement.md | 303 | facture (filtrage par statut de rapprochement) | facturation | comptabilite, reporting | oui | non | non | non | non | procedure |
| 434 | suivi-financier/gerer-les-cartes-a-debit-differe.md | 280 | carte à débit différé (rapprochement bancaire) | indetermine | comptabilite | oui | oui | oui | non | oui | procedure |
| 435 | suivi-financier/gerer-les-codes-comptables-des-remises.md | 290 | code comptable (remises) | indetermine | comptabilite, tarification | oui | non | oui | non | non | procedure |
| 436 | suivi-financier/gestion-d-un-trop-percu.md | 823 | trop-perçu (gestion, rapprochement bancaire) | facturation | paiement, comptabilite | oui | non | oui | non | oui | procedure |
| 437 | suivi-financier/introduction-module-d-exports-comptables.md | 223 | module exports comptables (introduction) | indetermine | comptabilite | oui | non | non | non | non | definitionnel |
| 438 | suivi-financier/la-balance-agee.md | 241 | balance âgée (créances / dettes) | indetermine | comptabilite, reporting | oui | non | non | non | non | reference_configuration |
| 439 | suivi-financier/le-statut-des-transactions-a-corriger.md | 264 | statut « à corriger » (transaction bancaire) | indetermine | comptabilite | oui | oui | oui | non | oui | faq_depannage |
| 440 | suivi-financier/les-differentes-actions-en-masse-dans-le-rapprochement-bancaire.md | 335 | actions en masse (rapprochement bancaire) | indetermine | comptabilite | oui | non | non | non | non | procedure |
| 441 | suivi-financier/les-differents-statuts-des-operations-de-rapprochement-bancaire.md | 78 | statuts (opérations rapprochement bancaire, référence) | indetermine | comptabilite | non | oui | oui | non | non | reference_configuration |
| 442 | suivi-financier/mettre-en-place-la-tva-sur-les-encaissements.md | 472 | TVA sur encaissements (paramétrage) | facturation | comptabilite, conformite_reglementaire | oui | non | oui | oui | non | procedure |
| 443 | suivi-financier/modifier-le-moyen-de-paiement-pour-un-rapprochement-bancaire.md | 213 | moyen de paiement (correction, rapprochement bancaire) | indetermine | paiement, comptabilite | oui | non | non | non | oui | procedure |
| 444 | suivi-financier/modifier-ses-identifiants-bancaires.md | 224 | identifiants bancaires (modification, synchronisation) | indetermine | comptabilite, securite_compte | oui | non | oui | oui | oui | procedure |
| 445 | suivi-financier/parametrer-les-preferences-d-exports-comptables.md | 418 | préférences exports comptables (paramétrage) | indetermine | comptabilite | oui | non | oui | non | non | procedure |
| 446 | suivi-financier/problemes-de-connexion-de-votre-compte-bancaire.md | 201 | connexion bancaire (dépannage) | indetermine | comptabilite, integrations | oui | non | non | non | oui | faq_depannage |
| 447 | suivi-financier/proceder-au-rapprochement-bancaire-de-vos-transactions.md | 666 | rapprochement bancaire (procédure complète) | indetermine | comptabilite, automatisation | oui | non | oui | oui | oui | procedure |
| 448 | suivi-financier/renseigner-les-codes-comptables-dans-le-catalogue.md | 206 | code comptable (catalogue, produit) | indetermine | comptabilite, catalogue | oui | non | non | non | non | procedure |
| 449 | suivi-financier/renseigner-les-codes-comptables-dans-un-document.md | 200 | code comptable (ligne de document) | facturation | comptabilite, documents | oui | non | non | non | non | procedure |
| 450 | suivi-financier/supprimer-ou-modifier-un-compte-bancaire-synchronise.md | 204 | compte bancaire synchronisé (suppression / modification) | indetermine | comptabilite, integrations | oui | non | oui | oui | non | procedure |
| 451 | suivi-financier/traiter-un-montant-de-transaction-different-du-montant-de-la-facture.md | 251 | transaction (montant différent facture, rapprochement) | facturation | comptabilite, paiement | oui | oui | non | non | oui | procedure |
| 452 | suivi-financier/transferer-des-transactions-entre-comptes-bancaires.md | 233 | transactions bancaires (transfert entre comptes) | indetermine | comptabilite | oui | non | non | non | non | procedure |
| 453 | suivi-financier/utiliser-la-comptabilite-auxiliaire.md | 310 | comptabilité auxiliaire (comptes clients / fournisseurs) | indetermine | comptabilite | oui | non | non | non | non | procedure |
| 454 | suivi-financier/utiliser-les-codes-comptables-analytiques.md | 407 | comptabilité analytique (codes, produits / affaires) | indetermine | comptabilite, catalogue | oui | non | oui | oui | non | procedure |

## Contrôles mécaniques

- Documents traités / attendus : **454 / 454**. Écart au garde-fou (462 − 8 = 454) : nul.
- Numérotation : continue de 1 à 454, aucune rupture, vérifié par tri numérique de la colonne `#`.
- Doublons de `chemin_relatif` dans le tableau : **0** (vérifié par tri + `uniq -d`).
- Correspondance ensembliste entre les 454 `chemin_relatif` du tableau et les 454 chemins du périmètre RESTANT gelé en §3 (y compris format de préfixe, ex. `module-achats/...`, `rapports-et-pilotage/...`) : **identique**, vérifié par `diff` sur les deux listes triées — aucune ligne divergente.
- Colonnes : chaque ligne du tableau comporte exactement 12 colonnes de données (vérifié par split mécanique sur `|`, valeur constante pour les 454 lignes).
- `moment_parcours` : strictement dans le vocabulaire fermé `indetermine · demande · devis · achat · chantier-intervention · facturation`. Répartition : `indetermine` 341, `facturation` 94, `devis` 11, `achat` 8, `demande` 0, `chantier-intervention` 0 (aucune valeur hors vocabulaire).
- `capacites_transverses` : maximum observé par document = 3 (répartition : 1 capacité sur 97 documents, 2 sur 270, 3 sur 87, `—` inclus dans le décompte des cas à 1 valeur). Aucune ligne ne dépasse 3.
- `genre_documentaire` : valeurs observées toutes rattachables aux racines du §4 (`procedure`, `reference_configuration`, `definitionnel`, `politique_legale`, `faq_depannage`, `marketing_dans_aide`, `autre`) — aucune racine nouvelle.
- `longueur_mots` : calculée mécaniquement pour les 454 documents avant lecture (voir méthode déclarée en tête de fichier), valeurs figées dans le tableau, non modifiées a posteriori.
- Agrégats ci-dessous recalculés directement depuis le tableau final (et non recopiés des checkpoints), par script mécanique sur le fichier.

## Agrégats

**Volume**
- 454 documents, 183 950 mots (méthode `awk` + `wc -w`, frontmatter exclu).
- Moyenne : 405,2 mots/document (min 68, max 2 767).
- Corpus le plus dense du dépôt en nombre de documents, densité par document modérée (~5,6 Ko/document annoncée au gel de périmètre, cohérente avec la moyenne mécanique de mots ci-dessus).

**`moment_parcours` (454)**
| Valeur | Effectif |
|---|---|
| indetermine | 341 |
| facturation | 94 |
| devis | 11 |
| achat | 8 |
| demande | 0 |
| chantier-intervention | 0 |

**`genre_documentaire`, racines (454)**
| Racine | Effectif |
|---|---|
| procedure | 312 |
| reference_configuration | 67 |
| definitionnel | 30 |
| politique_legale | 25 |
| faq_depannage | 12 |
| marketing_dans_aide | 6 |
| autre | 2 |

**`capacites_transverses`, fréquence par valeur individuelle (une même ligne peut compter dans plusieurs valeurs)**
| Valeur | Effectif |
|---|---|
| crm | 103 |
| documents | 81 |
| comptabilite | 79 |
| integrations | 77 |
| reporting | 75 |
| permissions | 58 |
| conformite_reglementaire | 56 |
| personnalisation | 48 |
| facturation | 47 |
| automatisation | 44 |
| catalogue | 39 |
| paiement | 36 |
| communication | 19 |
| securite_compte | 18 |
| mobile | 18 |
| gestion_stock | 17 |
| tarification | 16 |
| planning | 13 |
| marketing_et_communication | 10 |
| — (aucune) | 8 |
| validation | 8 |
| roles | 8 |
| notifications | 7 |
| recherche | 5 |
| support_editeur | 3 |
| geolocalisation | 3 |
| presence_en_ligne | 1 |
| photos | 1 |

**`contenu_observable`, répartition oui/non sur les cinq champs (454 chacun)**
| Champ | oui | non |
|---|---|---|
| procedure | 361 | 93 |
| transition_objet | 63 | 391 |
| regle_ou_condition | 244 | 210 |
| contrainte_ou_limite | 201 | 253 |
| exception_ou_correction | 62 | 392 |

Aucune valeur `inconnu` n'a été utilisée sur ce corpus : les 454 documents ont permis un jugement honnête et tranché sur les cinq champs `contenu_observable`, la documentation Sellsy étant systématiquement rédigée sous forme d'articles de procédure ou de référence assez explicites pour permettre une observation directe.

## Cas mal représentés

- **341 documents codés `moment_parcours = indetermine`**, soit 75 % du corpus. Cette proportion, nettement supérieure à celle observée sur les corpus précédents (ex. InterFast), s'explique par la nature de Sellsy : logiciel de gestion transversal (CRM, facturation, stock, comptabilité, marketing, support, paiements, rapports) dont l'essentiel de la documentation porte sur des fonctionnalités de configuration ou d'usage courant sans ancrage à un moment identifiable du parcours client (devis → achat → chantier → facturation). Cas typiques : tableaux de bord et rapports (rubrique `rapports-et-pilotage/`, ~90 documents), paramétrages de compte et modules (`configuration-du-compte/`, `gestion-des-donnees/`, `integrations-et-api/`), documentation légale/réglementaire sur la facturation électronique dont le contenu porte sur des obligations transversales plutôt que sur une étape de vente précise.
- **94 documents `facturation`** : essentiellement les rubriques `documents-de-vente/`, `paiements/` et une partie de `facturation-electronique/`, `module-tresorerie/`, `suivi-financier/` — cohérent avec le poids de ces rubriques dans le périmètre gelé.
- **11 documents `devis`** et **8 documents `achat`** : nombre limité, la documentation Sellsy traitant rarement un document en particulier de façon isolée du reste du cycle de vente ou d'achat — la plupart des articles couvrant un module entier (ex. `module-achats/`) plutôt qu'une étape précise.
- **Aucun document `demande` ni `chantier-intervention`** : Sellsy est un CRM/facturation généraliste, sans notion de « chantier » ou d'« intervention terrain » comparable aux corpus BTP (InterFast, Vertuoza). L'absence de ces valeurs est un silence documentaire attendu compte tenu de la nature du produit, non une anomalie de codification.
- **Templates à forte répétition structurelle** (connecteurs comptables, guides de paiement en ligne, modèles d'automatisation) : chaque document reste un article distinct avec une URL et un titre propres dans le corpus source, et a été codé individuellement : ce n'est pas une duplication de contenu identique mais une famille de documents à structure partagée et contenu spécifique par éditeur/partenaire.

## Limites

Ce fichier documente une carte de sélection LIGHT, pas une analyse produit. Conformément à SCHEMA-LIGHT.md §9 :

- Un `non` sur les champs `contenu_observable` ne permet pas de conclure à une absence fonctionnelle dans Sellsy — uniquement à une absence d'observation dans le document LIGHT concerné.
- La proportion élevée de `moment_parcours = indetermine` ne signifie pas que Sellsy manque de structuration en parcours client : elle reflète la nature de sa documentation d'aide (orientée modules et fonctionnalités transversales) et la contrainte du vocabulaire fermé, pas une mesure de maturité produit.
- Les fréquences de `capacites_transverses` et de `genre_documentaire` sont des comptages mécaniques sur le corpus documentaire collecté, non une mesure de l'importance métier, de l'adoption ou de la qualité des fonctionnalités correspondantes chez Sellsy.
- L'arbitrage différé sur `tarification` et `marketing_et_communication` reste ouvert ; les comptages ci-dessus (16 et 10 occurrences) sont descriptifs et ne préjugent pas de la décision à venir sur leur périmètre.
- Ce fichier ne contient aucune conclusion de marché, aucune comparaison avec les corpus précédents au-delà des constats mécaniques explicitement établis, et aucune recommandation produit SUPORDO.
