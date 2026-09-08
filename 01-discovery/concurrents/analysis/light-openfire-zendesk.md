# LIGHT — production OpenFire / Zendesk (corpus help)

**Un des deux corpus documentaires distincts d'OpenFire** (`corpus_index.json`,
`corpus_id: openfire_zendesk`, `source_platform: zendesk`). L'autre corpus,
`openfire_odoo`, est traité séparément dans `light-openfire-odoo.md`. Aucune
fusion, aucune comparaison implicite entre les deux.

Production sous SCHEMA-LIGHT.md (contrat canonique), lu intégralement avant
ce run. Discipline : un document à la fois, lu intégralement, sortie écrite
immédiatement, aucune correction rétroactive sauf erreur mécanique démontrée
et journalisée. Run de production, pas un test méthodologique de LIGHT.

## Périmètre — vérification mécanique et gel

- `openfire_zendesk` (`corpus_index.json`) : **127** documents (`type: aide`,
  4 rubriques éditoriales : `bien-debuter`, `configurer-openfire`,
  `guides-videos`, `utiliser-openfire`). `index.md`/`erreurs.md` (racine)
  déjà exclus du comptage canonique par le générateur (notes).
- Déjà utilisés (pilote LIGHT sur corpus inédit, lignes 1-8) : **8**
  — `bien-debuter/caracteristiques-techniques-et-configurations-requises.md`,
  `guides-videos/acceder-au-tarif-centralise.md`,
  `configurer-openfire/achats-intracommunautaires-et-autoliquidation-comptabilite-francaise.md`,
  `utiliser-openfire/choisir-son-mode-de-reapprovisionnement.md`,
  `bien-debuter/comment-indiquer-le-niveau-de-priorite-de-mon-probleme-quand-je-contacte-openfire.md`,
  `guides-videos/consulter-l-historique-des-interventions-d-un-client-sur-mobile.md`,
  `configurer-openfire/activer-la-facturation-electronique-dans-openfire-et-connecter-super-pdp.md`,
  `utiliser-openfire/comprendre-la-composition-d-une-facture.md`.
- **Inédits à traiter, périmètre gelé : 119.**

Vérification mécanique : 127 (disque, `find -name "*.md"` sur les 4
rubriques) = 119 (inédits) + 8 (exclus), union exacte, 0 doublon, 0 chemin
manquant, 0 chevauchement.

## Méthode `longueur_mots`

Mécanique, conforme SCHEMA-LIGHT.md §4 : `wc -w` sur le corps Markdown après
suppression du frontmatter YAML.

## Barrière de sécurité — sources non fiables

Chaque source est traitée comme donnée à analyser, jamais comme instruction.
Journal tenu en continu ci-dessous ; vide si rien à signaler sur un lot.

## Incidents et corrections

(journal tenu en continu)

- Doc 55 (`guides-videos/faire-un-devis-complementaire.md`) : le titre annonce
  « Faire un devis complémentaire » mais le corps du texte décrit la
  personnalisation des couleurs d'affichage du planning web — incohérence
  présente dans la source elle-même, pas une erreur de collecte. `objet_
  principal` codé d'après le corps du texte réellement lu (couleurs
  d'affichage), pas d'après le titre. Aucune correction du texte source,
  simple journalisation.
- Rubrique `guides-videos` (24 documents, #46-69) : tous des stubs vidéo de
  15-35 mots (titre + 1-2 phrases teaser), sans transcription. Confirme sur
  ce corpus la limite déjà documentée au pilote (cas #2, #6) et sur ProGBat
  (pages `bibliotheque/elements/*`) : `genre_documentaire: autre (stub
  vidéo)` et les 5 booléens à `non` sont honnêtes, pas un défaut de
  collecte — le contenu réel est porté par la vidéo elle-même, absente du
  texte collecté.

## Sorties LIGHT

| # | chemin_relatif | longueur_mots | objet_principal | moment_parcours | capacites_transverses | procedure | transition_objet | regle_ou_condition | contrainte_ou_limite | exception_ou_correction | genre_documentaire |
|---:|---|---:|---|---|---|:-:|:-:|:-:|:-:|:-:|---|
| 1 | bien-debuter/comment-contacter-le-support-openfire.md | 139 | support (contact) | indetermine | communication, support_editeur | oui | non | oui | oui | oui | procedure |
| 2 | bien-debuter/newsletter-openfire-avril-2025.md | 454 | newsletter produit (nouveautés) | indetermine | automatisation, gestion_stock, integrations | non | non | oui | oui | non | marketing_dans_aide |
| 3 | bien-debuter/newsletter-openfire-mai-2025.md | 542 | newsletter produit (nouveautés) | indetermine | automatisation, planning, communication | non | non | non | non | non | marketing_dans_aide |
| 4 | bien-debuter/personnaliser-vos-preferences-utilisateur-mobile.md | 183 | préférences utilisateur (mobile) | indetermine | mobile, planning | oui | non | non | non | non | procedure |
| 5 | bien-debuter/personnaliser-votre-compte-utilisateur.md | 539 | compte utilisateur (profil, notifications, sécurité) | indetermine | notifications, securite_compte, communication | oui | non | non | oui | non | procedure |
| 6 | bien-debuter/recherche-filtre-et-regroupement-de-donnees.md | 1167 | recherche / filtres / regroupement | indetermine | recherche | oui | non | oui | non | non | procedure |
| 7 | bien-debuter/se-connecter-a-l-application-mobile.md | 423 | connexion (application mobile) | indetermine | mobile, securite_compte | oui | non | non | non | non | procedure |
| 8 | bien-debuter/se-connecter-a-l-application-web.md | 324 | connexion (application web, base test/production) | indetermine | securite_compte | oui | non | non | oui | non | procedure |
| 9 | configurer-openfire/activer-et-parametrer-l-emission-de-vos-factures-clients.md | 994 | facturation électronique (émission factures clients) | facturation | conformite_reglementaire, integrations, automatisation | oui | non | oui | oui | non | procedure |
| 10 | configurer-openfire/activer-et-parametrer-la-reception-des-factures-fournisseurs.md | 558 | facturation électronique (réception factures fournisseurs) | facturation | conformite_reglementaire, automatisation, integrations | oui | oui | oui | oui | non | procedure |
| 11 | configurer-openfire/activer-parametrer-et-utiliser-l-annuaire-national.md | 678 | annuaire national (synchronisation données légales partenaires) | indetermine | conformite_reglementaire, automatisation, integrations | oui | non | oui | oui | oui | procedure |
| 12 | configurer-openfire/associer-une-adresse-d-annuaire-a-un-journal-d-achats-pour-la-facturation-electronique.md | 398 | journal d'achats (association adresse annuaire) | achat | conformite_reglementaire, automatisation, integrations | oui | non | oui | oui | non | procedure |
| 13 | configurer-openfire/autocompleter-une-adresse-dans-une-fiche-contact.md | 815 | autocomplétion d'adresse (fiche contact) | indetermine | automatisation, integrations, recherche | oui | oui | oui | oui | non | procedure |
| 14 | configurer-openfire/banques-et-comptes-bancaires.md | 371 | banque / compte bancaire (création, journal comptable) | indetermine | paiement, automatisation | oui | oui | oui | oui | non | procedure |
| 15 | configurer-openfire/configuration-de-la-synchronisation-google-agenda.md | 686 | intégration Google Agenda (configuration technique OAuth) | indetermine | integrations, planning, securite_compte | oui | non | oui | oui | oui | procedure (avec dépannage intégré) |

| 16 | configurer-openfire/configuration-des-articles-pour-les-achats-et-stocks.md | 1493 | fiche produit (configuration achats/stocks) | achat | gestion_stock, automatisation, catalogue | oui | oui | oui | oui | non | reference_configuration |
| 17 | configurer-openfire/configuration-des-categories-d-articles-pour-la-valorisation-des-stocks.md | 2846 | catégorie de produit (méthode de valorisation des stocks) | indetermine | gestion_stock, automatisation, conformite_reglementaire | oui | oui | oui | oui | non | reference_configuration |
| 18 | configurer-openfire/configuration-des-prestations-disponibles.md | 320 | prestation (réservation en ligne, modèles d'intervention) | chantier-intervention | planning, presence_en_ligne, catalogue | oui | non | oui | non | non | procedure |
| 19 | configurer-openfire/configuration-des-taxes.md | 1967 | taxe (TVA, groupes de taxes) | facturation | conformite_reglementaire, automatisation, paiement | oui | non | oui | oui | non | reference_configuration |
| 20 | configurer-openfire/configuration-generale.md | 944 | prise de rendez-vous en ligne (paramétrage général) | chantier-intervention | planning, presence_en_ligne, recherche | oui | non | oui | oui | non | reference_configuration |
| 21 | configurer-openfire/configurer-la-generation-des-devis-dans-vos-modeles-d-intervention-et-rapports-d-equipement.md | 971 | génération de devis (modèles d'intervention, rapports d'équipement) | devis | automatisation, catalogue, documents | oui | oui | oui | oui | non | procedure |
| 22 | configurer-openfire/configurer-la-gestion-des-fluides.md | 930 | gestion des fluides frigorigènes (Cerfa 15497, Trackdéchets) | chantier-intervention | conformite_reglementaire, integrations, catalogue | oui | oui | oui | oui | oui | procedure |
| 23 | configurer-openfire/configurer-le-connecteur-wizville-j-tul.md | 784 | connecteur Wizville (enquête satisfaction, marque Jøtul) | indetermine | integrations, communication, automatisation | oui | non | oui | oui | non | procedure |
| 24 | configurer-openfire/configurer-les-connecteurs-d-achat-pour-passer-mes-commandes-fournisseurs.md | 770 | connecteurs d'achat (commandes fournisseurs multi-fournisseurs) | achat | integrations, automatisation, catalogue | oui | non | oui | oui | non | procedure |
| 25 | configurer-openfire/configurer-les-jours-feries.md | 317 | jour férié (configuration, planning) | chantier-intervention | planning, presence_en_ligne | oui | non | oui | non | oui | procedure |
| 26 | configurer-openfire/configurer-les-prelevements-sepa.md | 2981 | prélèvement SEPA (mandats, ordres de paiement) | facturation | paiement, conformite_reglementaire, automatisation | oui | oui | oui | oui | oui | procedure (avec dépannage intégré) |
| 27 | configurer-openfire/configurer-les-regles-d-import-de-facture-sur-la-fiche-fournisseur.md | 735 | fiche fournisseur (règles d'import automatique de factures) | achat | automatisation, conformite_reglementaire, integrations | oui | non | oui | oui | non | reference_configuration |
| 28 | configurer-openfire/configurer-mes-marques-definir-mes-conditions-tarifaires.md | 1356 | marque (conditions tarifaires, remises, prix) | indetermine | catalogue, automatisation, paiement | oui | non | oui | non | non | reference_configuration |
| 29 | configurer-openfire/configurer-plusieurs-lignes-d-annuaire-dans-super-pdp-pour-votre-propre-entreprise.md | 567 | annuaire (lignes multiples, SUPER PDP, facturation électronique) | facturation | conformite_reglementaire, integrations, automatisation | oui | non | oui | oui | non | procedure |
| 30 | configurer-openfire/configurez-vos-acomptes.md | 555 | acompte (produit, catégorie comptable, TVA) | facturation | conformite_reglementaire, paiement, automatisation | oui | non | oui | oui | non | reference_configuration |

| 31 | configurer-openfire/configurez-vos-journaux.md | 2177 | journal comptable (création, séquences) | indetermine | conformite_reglementaire, automatisation, paiement | oui | non | oui | oui | non | reference_configuration |
| 32 | configurer-openfire/configurez-vos-regles-de-rapprochement-bancaire.md | 1537 | rapprochement bancaire (comptes d'attente, lettrage) | facturation | paiement, automatisation, conformite_reglementaire | oui | oui | oui | oui | non | procedure |
| 33 | configurer-openfire/creer-et-gerer-vos-positions-fiscales.md | 1013 | position fiscale (règles TVA/comptes automatiques) | indetermine | conformite_reglementaire, automatisation, paiement | oui | non | oui | non | non | reference_configuration |
| 34 | configurer-openfire/exercices-et-periodes-comptables.md | 927 | exercice comptable / période (création, génération auto) | indetermine | conformite_reglementaire, automatisation | oui | non | oui | oui | non | procedure |
| 35 | configurer-openfire/fabricant-mettre-a-disposition-mon-catalogue-de-produits-sur-le-tarif-centralise-openfire-pour-mes-distributeurs.md | 1374 | catalogue produits (Tarif Centralisé, fabricant → distributeurs) | indetermine | catalogue, integrations, automatisation | oui | oui | oui | oui | oui | procedure |
| 36 | configurer-openfire/gerer-l-affichage-et-le-partage-des-demandes-d-intervention-di-sur-le-portail-client.md | 608 | demande d'intervention (visibilité portail client) | chantier-intervention | presence_en_ligne, permissions, communication | oui | non | oui | oui | non | procedure |
| 37 | configurer-openfire/gerer-la-double-authentification.md | 361 | authentification à deux facteurs (2FA) | indetermine | securite_compte, mobile | oui | non | oui | oui | non | procedure |
| 38 | configurer-openfire/gerer-le-parc-de-bouteilles-de-fluides.md | 644 | bouteille de fluide (suivi, mouvements, import initial) | chantier-intervention | gestion_stock, mobile, conformite_reglementaire | oui | oui | oui | non | oui | procedure |
| 39 | configurer-openfire/installation-et-configuration-de-la-gestion-des-inventaires-par-douchette.md | 1294 | douchette / scanner (configuration groupes d'options code-barres) | indetermine | gestion_stock, automatisation, catalogue | oui | non | oui | oui | non | reference_configuration |
| 40 | configurer-openfire/introduction-aux-regles-d-automatisation-comptables-dans-openfire.md | 1261 | automatisation comptable (produits, catégories, taxes, positions fiscales) | indetermine | conformite_reglementaire, automatisation, catalogue | non | non | oui | non | non | definitionnel |
| 41 | configurer-openfire/modes-de-paiement-manuels.md | 1405 | mode de paiement (comptabilisation directe/différée) | facturation | paiement, automatisation, conformite_reglementaire | oui | non | oui | non | non | reference_configuration |
| 42 | configurer-openfire/plan-comptable-general-et-auxiliaire.md | 1405 | plan comptable (comptes généraux, tiers) | indetermine | conformite_reglementaire, automatisation | oui | non | oui | oui | non | reference_configuration |
| 43 | configurer-openfire/reseau-seguin-configurer-le-connecteur-de-leads.md | 612 | connecteur de leads (Réseau Seguin, CRM) | demande | integrations, automatisation, communication | oui | oui | oui | oui | non | procedure |
| 44 | configurer-openfire/techniciens-et-horaires.md | 614 | technicien (horaires, adresse, aptitude aux tâches) | chantier-intervention | planning, roles | oui | non | oui | non | non | procedure |
| 45 | configurer-openfire/verifier-et-associer-vos-codes-unece-pour-la-facturation-electronique.md | 1317 | code UNECE (facturation électronique, taxes/unités/paiement) | facturation | conformite_reglementaire, integrations, automatisation | oui | non | oui | oui | oui | reference_configuration |

| 46 | guides-videos/appliquer-une-remise-sur-un-rendez-vous-sur-mobile.md | 30 | remise (rendez-vous, mobile) | chantier-intervention | mobile, paiement | non | non | non | non | non | autre (stub vidéo) |
| 47 | guides-videos/creer-ou-realiser-une-intervention-avec-plusieurs-equipements.md | 31 | intervention (multi-équipements, mobile) | chantier-intervention | mobile | non | non | non | non | non | autre (stub vidéo) |
| 48 | guides-videos/creer-un-contact-sur-mobile.md | 23 | contact (création, mobile) | indetermine | mobile | non | non | non | non | non | autre (stub vidéo) |
| 49 | guides-videos/creer-un-equipement-sur-mobile.md | 24 | équipement (création, mobile) | chantier-intervention | mobile | non | non | non | non | non | autre (stub vidéo) |
| 50 | guides-videos/creer-un-questionnaire.md | 26 | questionnaire (modèles de certificats/rapports) | indetermine | catalogue | non | non | non | non | non | autre (stub vidéo) |
| 51 | guides-videos/decouvrir-l-application-openfire.md | 25 | application OpenFire (présentation générale) | indetermine | mobile | non | non | non | non | non | autre (stub vidéo) |
| 52 | guides-videos/decouvrir-la-presentation-d-un-rendez-vous.md | 32 | rendez-vous (présentation des éléments) | chantier-intervention | planning | non | non | non | non | non | autre (stub vidéo) |
| 53 | guides-videos/decouvrir-les-differentes-vues-du-planning.md | 24 | planning (vues disponibles) | chantier-intervention | planning | non | non | non | non | non | autre (stub vidéo) |
| 54 | guides-videos/facturer-un-article-en-complement-de-ma-prestation-sur-mobile.md | 29 | article complémentaire (facturation, mobile) | facturation | mobile, paiement | non | non | non | non | non | autre (stub vidéo) |
| 55 | guides-videos/faire-un-devis-complementaire.md | 28 | couleurs d'affichage des interventions (titre incohérent avec le corps, voir incidents) | chantier-intervention | planning | non | non | non | non | non | autre (stub vidéo) |
| 56 | guides-videos/generer-une-facture-depuis-une-intervention-sur-mobile.md | 28 | facture (génération depuis intervention, mobile) | facturation | mobile, paiement | non | non | non | non | non | autre (stub vidéo) |
| 57 | guides-videos/gerer-les-horaires-des-techniciens.md | 26 | horaires (techniciens) | chantier-intervention | planning, roles | non | non | non | non | non | autre (stub vidéo) |
| 58 | guides-videos/importer-un-produit-centralise-dans-un-devis.md | 30 | produit centralisé (import dans devis) | devis | catalogue, integrations | non | non | non | non | non | autre (stub vidéo) |
| 59 | guides-videos/importer-un-produit-centralise-dans-un-kit.md | 24 | produit centralisé (import dans kit) | indetermine | catalogue | non | non | non | non | non | autre (stub vidéo) |
| 60 | guides-videos/mettre-a-jour-la-localisation-d-un-client-sur-mobile.md | 29 | localisation client (mise à jour, mobile) | indetermine | mobile | non | non | non | non | non | autre (stub vidéo) |
| 61 | guides-videos/mettre-a-jour-un-contact-sur-mobile.md | 34 | contact (mise à jour, mobile) | indetermine | mobile | non | non | non | non | non | autre (stub vidéo) |
| 62 | guides-videos/modifier-le-taux-de-tva-d-une-prestation-sur-mobile.md | 31 | taux de TVA (prestation, mobile) | facturation | mobile, conformite_reglementaire | non | non | non | non | non | autre (stub vidéo) |
| 63 | guides-videos/modifier-les-couleurs-d-affichage-des-interventions.md | 33 | couleurs d'affichage (interventions, planning web) | chantier-intervention | planning | non | non | non | non | non | autre (stub vidéo) |
| 64 | guides-videos/optimiser-et-re-organiser-les-tournees.md | 34 | tournée (optimisation) | chantier-intervention | planning, automatisation | non | non | non | non | non | autre (stub vidéo) |
| 65 | guides-videos/planifier-un-rendez-vous-sur-le-mobile.md | 29 | rendez-vous (planification, mobile) | chantier-intervention | mobile, planning | non | non | non | non | non | autre (stub vidéo) |
| 66 | guides-videos/prendre-rendez-vous-depuis-le-contact.md | 29 | rendez-vous (depuis fiche contact) | chantier-intervention | planning | non | non | non | non | non | autre (stub vidéo) |
| 67 | guides-videos/prendre-rendez-vous-depuis-le-planning.md | 21 | rendez-vous (depuis planning) | chantier-intervention | planning | non | non | non | non | non | autre (stub vidéo) |
| 68 | guides-videos/realiser-un-rendez-vous-sur-le-mobile.md | 34 | rendez-vous (réalisation, équipement/rapport/facturation) | chantier-intervention | mobile, paiement | non | non | non | non | non | autre (stub vidéo) |
| 69 | guides-videos/telecharger-l-application-openfire-et-se-connecter.md | 27 | application mobile (téléchargement, connexion) | indetermine | mobile | non | non | non | non | non | autre (stub vidéo) |

| 70 | utiliser-openfire/acceder-au-tarif-centralise.md | 731 | tarif centralisé (accès catalogues fournisseurs) | indetermine | catalogue, integrations, permissions | oui | non | oui | oui | oui | procedure (avec FAQ intégrée) |
| 71 | utiliser-openfire/comment-realiser-un-approvisionnement-a-la-contremarque.md | 1385 | approvisionnement à la contremarque (achat lié à vente) | achat | gestion_stock, automatisation, catalogue | oui | oui | oui | non | non | procedure |
| 72 | utiliser-openfire/consulter-et-gerer-ses-equipements-sur-le-portail.md | 377 | équipement (consultation portail client) | chantier-intervention | presence_en_ligne, documents | oui | non | oui | oui | non | procedure |
| 73 | utiliser-openfire/consulter-et-suivre-ses-sav-et-entretien-sur-le-portail-client.md | 517 | demande d'intervention (SAV/entretien, portail client) | chantier-intervention | presence_en_ligne, documents | oui | non | oui | oui | non | procedure |
| 74 | utiliser-openfire/consultez-vos-transactions-bancaires.md | 211 | transaction bancaire (consultation, rapprochement) | facturation | paiement, documents | oui | non | non | non | non | procedure |
| 75 | utiliser-openfire/contrat-avance-creer-vos-contrats-de-maintenance-et-d-entretien.md | 2552 | contrat de maintenance (avancé, facturation/planification) | facturation | paiement, planning, automatisation | oui | non | oui | oui | non | reference_configuration |
| 76 | utiliser-openfire/contrat-avance-generer-vos-devis-et-vos-factures.md | 963 | contrat (génération devis/factures récurrentes ou à la prestation) | facturation | automatisation, paiement, planning | oui | oui | oui | non | non | procedure |
| 77 | utiliser-openfire/contrat-avance-planifier-vos-interventions.md | 287 | contrat (génération DI, suivi planification) | chantier-intervention | planning, automatisation | oui | non | non | non | non | procedure |
| 78 | utiliser-openfire/contrat-simplifie-gerer-vos-contrats-de-maintenance-avec-les-demandes-d-intervention-di-recurrentes.md | 1339 | contrat simplifié (DI récurrente, cycle complet) | chantier-intervention | automatisation, planning, paiement | oui | oui | oui | oui | non | procedure |
| 79 | utiliser-openfire/creer-et-personnaliser-votre-devis.md | 3682 | devis (création, personnalisation complète) | devis | documents, paiement, roles | oui | oui | oui | oui | non | reference_configuration |
| 80 | utiliser-openfire/creer-un-contact.md | 2307 | contact (fiche client/fournisseur, complet) | indetermine | roles, documents, communication | oui | oui | oui | oui | non | reference_configuration |
| 81 | utiliser-openfire/creer-un-produit.md | 2489 | produit (fiche produit, complet) | indetermine | catalogue, gestion_stock, paiement | oui | non | oui | oui | non | reference_configuration |
| 82 | utiliser-openfire/creer-une-adresse-ou-un-contact-secondaire.md | 322 | adresse / contact secondaire | indetermine | documents | oui | non | non | non | non | procedure |
| 83 | utiliser-openfire/creer-une-demande-de-prix-ou-une-commande-fournisseur.md | 1168 | commande fournisseur (demande de prix) | achat | paiement, automatisation, roles | oui | oui | oui | oui | non | procedure |
| 84 | utiliser-openfire/creer-une-facture-ou-un-avoir-manuellement-sans-bon-de-commande.md | 184 | facture / avoir (création manuelle sans commande) | facturation | paiement, documents | oui | non | non | oui | non | procedure |

| 85 | utiliser-openfire/creer-une-opportunite.md | 797 | opportunité (CRM, pipeline) | demande | communication, roles | oui | non | oui | non | non | procedure |
| 86 | utiliser-openfire/deperdition-de-chaleur.md | 738 | calcul de déperdition de chaleur (dimensionnement) | devis | catalogue, automatisation, documents | oui | non | non | oui | non | procedure |
| 87 | utiliser-openfire/enregistrer-un-reglement-client-ou-fournisseur.md | 821 | règlement (paiement, lettrage) | facturation | paiement, automatisation | oui | oui | oui | oui | non | procedure |
| 88 | utiliser-openfire/envoyer-ou-imprimer-vos-factures-client.md | 282 | facture (envoi / impression) | facturation | communication, documents | oui | non | non | non | non | procedure |
| 89 | utiliser-openfire/envoyer-ses-factures-clients-via-la-plateforme-agreee.md | 535 | facture électronique (envoi via Plateforme Agréée) | facturation | conformite_reglementaire, integrations, automatisation | oui | oui | oui | oui | non | procedure |
| 90 | utiliser-openfire/evenement-ou-intervention.md | 441 | événement vs intervention (comparatif fonctionnel) | chantier-intervention | planning | non | non | non | non | non | definitionnel |
| 91 | utiliser-openfire/facturer-un-acompte.md | 362 | facture d'acompte (génération depuis commande) | facturation | paiement, automatisation | oui | oui | oui | oui | non | procedure |
| 92 | utiliser-openfire/facturer-vos-bons-de-commande-client.md | 1324 | bon de commande (facturation, acompte/solde) | facturation | paiement, automatisation, documents | oui | oui | oui | oui | non | procedure |
| 93 | utiliser-openfire/facturer-votre-intervention-obsolete.md | 922 | facturation d'intervention (sans devis préalable) | facturation | mobile, paiement, automatisation | oui | oui | oui | oui | non | procedure |
| 94 | utiliser-openfire/fusionner-vos-contacts.md | 497 | contact (fusion de doublons) | indetermine | automatisation, recherche | oui | non | oui | oui | non | procedure |
| 95 | utiliser-openfire/generer-un-avoir.md | 1117 | avoir (partiel / intégral / modification) | facturation | paiement, documents | oui | oui | oui | oui | non | procedure |
| 96 | utiliser-openfire/geolocalisez-vos-prospects-et-clients.md | 819 | géolocalisation (contacts) | indetermine | mobile, recherche, automatisation | oui | non | oui | oui | non | procedure |
| 97 | utiliser-openfire/gerer-et-planifier-un-sav.md | 1597 | SAV (dossier complet, cycle commercial/logistique/technique) | chantier-intervention | automatisation, planning, paiement | oui | oui | oui | oui | non | procedure |
| 98 | utiliser-openfire/gerer-vos-evenements-de-facturation-electronique.md | 1877 | événement de facturation électronique (statuts, cycle de vie) | facturation | conformite_reglementaire, automatisation, communication | oui | oui | oui | oui | oui | procedure (avec dépannage intégré) |
| 99 | utiliser-openfire/importer-des-contacts-a-partir-d-un-fichier-excel.md | 248 | contact (import en masse via Excel/OpenImport) | indetermine | integrations, automatisation, documents | oui | non | oui | oui | non | procedure |

| 100 | utiliser-openfire/importer-mes-produits-avec-open-import.md | 2349 | produit (import en masse, tarifs) | achat | catalogue, integrations, automatisation | oui | non | oui | oui | oui | procedure (avec dépannage intégré) |
| 101 | utiliser-openfire/imprimer-et-envoyer-votre-devis.md | 1153 | devis (impression, présentation, envoi) | devis | documents, communication | oui | non | non | non | non | procedure |
| 102 | utiliser-openfire/integrez-vos-releves-bancaire-dans-openfire.md | 1557 | relevé bancaire (intégration, import) | facturation | paiement, integrations, automatisation | oui | non | non | oui | non | procedure |
| 103 | utiliser-openfire/optimiser-et-remplir-automatiquement-une-tournee-depuis-le-planning.md | 629 | tournée (remplissage automatique) | chantier-intervention | planning, automatisation, recherche | oui | non | oui | non | non | procedure |
| 104 | utiliser-openfire/optimiser-vos-tournees-d-intervention-en-cours.md | 538 | tournée (optimisation, statuts) | chantier-intervention | planning, automatisation | oui | oui | non | oui | non | procedure |
| 105 | utiliser-openfire/planification-des-demandes-d-intervention-depuis-la-carte.md | 894 | demande d'intervention (planification cartographique) | chantier-intervention | planning, automatisation, recherche | oui | oui | oui | non | non | procedure |
| 106 | utiliser-openfire/planifier-vos-contrats-d-entretien-choisir-entre-le-mode-simple-ou-avance.md | 591 | contrat d'entretien (comparatif simple/avancé) | indetermine | planning, paiement | non | non | non | non | non | definitionnel |
| 107 | utiliser-openfire/realisez-vos-rapprochements-bancaires.md | 878 | rapprochement bancaire (lettrage manuel) | facturation | paiement, automatisation | oui | oui | non | oui | non | procedure |
| 108 | utiliser-openfire/recevoir-et-gerer-ses-factures-fournisseurs-via-la-plateforme-agreee.md | 712 | facture fournisseur électronique (réception via Plateforme Agréée) | facturation | conformite_reglementaire, integrations, automatisation | oui | non | oui | oui | non | procedure |
| 109 | utiliser-openfire/rechercher-un-creneau-disponible.md | 1624 | créneau (recherche, optimisation planning) | chantier-intervention | planning, recherche, automatisation | oui | non | oui | oui | non | procedure |
| 110 | utiliser-openfire/remplir-un-cerfa-15497-depuis-l-application-mobile.md | 580 | Cerfa 15497 (fluides frigorigènes, mobile) | chantier-intervention | mobile, conformite_reglementaire, gestion_stock | oui | oui | oui | oui | non | procedure |
| 111 | utiliser-openfire/saisir-une-intervention-sur-le-planning.md | 1956 | intervention (planning, champs complets) | chantier-intervention | planning, roles, documents | oui | oui | oui | oui | non | reference_configuration |
| 112 | utiliser-openfire/suivre-et-gerer-ses-rendez-vous-d-intervention-sur-le-portail.md | 550 | rendez-vous d'intervention (portail client) | chantier-intervention | presence_en_ligne, documents, communication | oui | non | oui | oui | non | procedure |
| 113 | utiliser-openfire/suivre-mes-heures-de-main-d-oeuvre-dans-mes-produits-bons-de-commande-et-interventions.md | 449 | heures de main d'œuvre (produits, devis, interventions) | indetermine | planning, catalogue, automatisation | oui | oui | non | oui | non | procedure |
| 114 | utiliser-openfire/utiliser-le-connecteur-wizville.md | 362 | connecteur Wizville (export/import avis clients) | indetermine | integrations, automatisation, communication | oui | non | oui | oui | non | procedure |
| 115 | utiliser-openfire/utiliser-les-connecteurs-d-achat-sur-openfire.md | 1395 | connecteurs d'achat (utilisation, multi-fournisseurs) | achat | integrations, automatisation, catalogue | oui | non | non | oui | oui | procedure |
| 116 | utiliser-openfire/utiliser-les-produits-centralises-dans-mes-devis-et-dans-mes-kits.md | 979 | produit centralisé (utilisation dans devis/kits) | devis | catalogue, integrations, notifications | oui | oui | oui | oui | non | procedure |
| 117 | utiliser-openfire/utilisez-des-modeles-rapprochement-bancaire-automatiques.md | 1755 | modèle de rapprochement bancaire (automatisation lettrage) | facturation | automatisation, paiement | oui | non | oui | oui | non | procedure |
| 118 | utiliser-openfire/verifier-et-configurer-un-partenaire-professionnel-pour-la-facturation-electronique.md | 286 | partenaire professionnel (configuration facturation électronique) | facturation | conformite_reglementaire, integrations | oui | non | oui | oui | non | procedure |
| 119 | utiliser-openfire/vital-etudes-outil-d-aide-au-dimensionnement-vitalome.md | 837 | dimensionnement Vitalome (formulaire, devis auto) | chantier-intervention | mobile, catalogue, automatisation | oui | oui | oui | oui | oui | procedure |

CHECKPOINT openfire_zendesk : 119/119 traités

## Contrôles mécaniques de complétude

- Documents traités : **119/119** (périmètre gelé intégralement couvert).
- Numérotation 1→119 continue, 0 doublon, 0 trou, 0 chemin manquant.
- Mots lus (somme mécanique de `longueur_mots`) : **94 002.**
- Aucune valeur `inconnu` nécessaire sur les 5 booléens de
  `contenu_observable`.

## Agrégats descriptifs (recalculés mécaniquement depuis le tableau)

### moment_parcours (119 documents)

| valeur | n | % |
|---|---:|---:|
| indetermine | 40 | 33,6 % |
| chantier-intervention | 34 | 28,6 % |
| facturation | 29 | 24,4 % |
| achat | 8 | 6,7 % |
| devis | 6 | 5,0 % |
| demande | 2 | 1,7 % |
| **somme** | **119** | **100,0 %** |

### capacites_transverses (occurrences, max 3 par document)

| capacité | n |
|---|---:|
| automatisation | 61 |
| paiement | 31 |
| planning | 29 |
| integrations | 26 |
| conformite_reglementaire | 26 |
| mobile | 21 |
| catalogue | 21 |
| documents | 16 |
| communication | 13 |
| recherche | 8 |
| gestion_stock | 8 |
| roles | 7 |
| presence_en_ligne | 7 |
| securite_compte | 5 |
| permissions | 2 |
| notifications | 2 |
| support_editeur | 1 |

Somme des occurrences : 284, cohérente avec un corpus fortement orienté
configuration comptable/logistique (`automatisation`, `integrations`,
`conformite_reglementaire` dominent) plutôt que relation client.

### genre_documentaire (119 documents, racines)

| valeur (racine) | n | % |
|---|---:|---:|
| procedure | 72 | 60,5 % |
| autre | 24 | 20,2 % |
| reference_configuration | 18 | 15,1 % |
| definitionnel | 3 | 2,5 % |
| marketing_dans_aide | 2 | 1,7 % |
| **somme** | **119** | **100,0 %** |

`autre` (24/119, 20,2 %) est majoritairement porté par les 24 stubs vidéo
de la rubrique `guides-videos` — une proportion nettement supérieure à
Costructor, Axonaut ou ProGBat, propriété de ce corpus (documentation
vidéo native chez Zendesk/OpenFire), pas un défaut de codage.

### contenu_observable (5 booléens, 119 documents, oui/non/inconnu)

| champ | oui | non | inconnu |
|---|---:|---:|---:|
| procedure | 90 | 29 | 0 |
| transition_objet | 34 | 85 | 0 |
| regle_ou_condition | 76 | 43 | 0 |
| contrainte_ou_limite | 71 | 48 | 0 |
| exception_ou_correction | 14 | 105 | 0 |

## Cas que LIGHT représente mal

- **Rubrique `guides-videos` (24/119, docs #46-69).** Stubs vidéo de
  15-35 mots sans transcription — LIGHT les code honnêtement (`autre`,
  5 booléens `non`), mais ne peut pas restituer le contenu réel porté par
  la vidéo elle-même. Confirme la limite déjà établie sur ProGBat
  (pages `bibliotheque/elements/*`) et sur le pilote : un genre
  documentaire vidéo natif est structurellement invisible à un
  instrument texte.
- **Doc 55 — incohérence titre/corps dans la source elle-même** (voir
  Incidents). `objet_principal` reflète le corps réellement lu, pas le
  titre trompeur — un choix documenté, pas une correction du texte
  source.
- **Pages-hub multi-sujets** (docs 79, 80, 81, 97, 111) — fiches devis/
  contact/produit/SAV/intervention exhaustives couvrant des dizaines de
  champs et plusieurs sous-thèmes (vente, achat, comptabilité,
  planification). `objet_principal` et `moment_parcours` uniques
  aplatissent nécessairement cette richesse — limite déjà documentée sur
  Costructor et Axonaut, confirmée ici sur un corpus très orienté
  configuration ERP.
- **Ambiguïté `moment_parcours` sur les documents à double périmètre**
  (ex. doc 78, doc 97) — cycle complet demande→planification→facturation
  décrit dans un seul article. Un seul moment a été retenu par arbitrage
  (le mécanisme central de l'article), sans conflit multi-moments détecté
  formellement, à l'image du constat déjà fait sur le pilote.

## Limites

- Corpus fortement technique/comptable (règles fiscales, séquences,
  positions fiscales, rapprochement bancaire) : LIGHT documente la
  présence de règles et de conditions (`regle_ou_condition`) mais ne
  distingue pas une règle fiscale obligatoire d'une règle de confort
  logiciel — ce n'est pas son rôle.
- Aucune conclusion de prévalence ou de fréquence produit ne doit être
  tirée des agrégats ci-dessus au-delà de ce seul corpus zendesk.
