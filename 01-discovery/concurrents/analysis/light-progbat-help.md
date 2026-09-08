# LIGHT — production ProGBat (corpus help/documentation complet)

Troisième production LIGHT réelle, après clôture de Costructor LIGHT et
Axonaut LIGHT. Schéma LIGHT appliqué strictement sans modification —
protocole établi par `pilote-light-corpus-inedit.md`, confirmé identique
entre Costructor et Axonaut (voir échange de session précédent), repris ici
sans nouvelle définition. Discipline : un document à la fois, lu
intégralement, sortie écrite immédiatement, aucune correction rétroactive
sauf erreur mécanique démontrée et journalisée.

## Périmètre — vérification mécanique et gel

- `progbat_help` (`corpus_index.json`) : **190** documents (6 rubriques
  éditoriales : `assistance`, `conformite`, `le-menu-principal`,
  `les-options`, `pour-bien-demarrer`, `presentation-generale`, plus 2
  fichiers à la racine).
- **Nuance par rapport à Costructor/Axonaut** : pour ces deux corpus,
  `corpus_index.json` documentait explicitement l'exclusion de
  `index.md`/`erreurs.md` (« notes de session de scraping, pas des
  articles d'aide »). Pour `progbat_help`, le champ `analysis_exclusions`
  et `notes` sont **vides** — aucune exclusion déclarée par le générateur.
  Vérification de contenu : `index.md` (racine) est une page de bienvenue
  et FAQ réelle (licence, tarifs, conformité), pas une note de scraping —
  **conservée dans le périmètre canonique**, conformément à ce que le
  générateur a lui-même déterminé pour ce corpus. Aucun `erreurs.md`
  trouvé sur disque.
- Déjà utilisés (pilote LIGHT sur corpus inédit, lignes 34-37) : **4**
  — `le-menu-principal/accueil.md`, `pour-bien-demarrer/demarrer-avec-progbat.md`,
  `presentation-generale/gestion-de-stocks.md`, `assistance/la-documentation.md`.
- **Inédits à traiter, périmètre gelé : 186.**

Vérification mécanique : 190 (disque, `find -name "*.md"`) = 186 (inédits)
+ 4 (exclus), union exacte, 0 doublon interne, 0 chemin manquant, 0
chevauchement.

Volume mécanique (`wc -w`, frontmatter YAML inclus, avant lecture de
contenu) sur les 186 inédits : **57 978 mots.**

## Incidents et corrections

(journal tenu en continu)

- Correction de méthode, journalisée avant tout calcul d'agrégat : ce
  paragraphe annonçait initialement que la colonne `longueur_mots` du
  tableau resterait une estimation approximative par document, comme
  dans les deux productions précédentes. En pratique, chaque valeur de
  `longueur_mots` a été remplie par comptage mécanique (`wc -w` du
  fichier brut) plutôt que par estimation visuelle — d'où l'égalité
  exacte, non fortuite, entre la somme de la colonne et le volume de
  calibrage ci-dessus (voir Résultat mécanique final). Aucune ligne du
  tableau n'a été modifiée ; seule cette annonce préalable est corrigée
  pour rester honnête sur la méthode réellement suivie.
- **2026-09-08 — correction narrative sur les 5 pages `bibliotheque/
  elements/*` classées `autre`.** Interprétation initiale (section « Cas
  que LIGHT représente mal ») : défaut de collecte probable / rendu
  JavaScript non capturé par le collecteur. Vérification ultérieure :
  interprétation réfutée par diagnostic ciblé (export `.md` natif
  GitBook, export agrégé `llms-full.txt`, comparaison à notre collecte)
  — les pages n'ont pas de corps documentaire dans la source elle-même.
  Diagnostic retenu : `ISSUE_A_PAGE_SANS_CONTENU_DOCUMENTAIRE`. Impact :
  correction narrative uniquement — aucune ligne du tableau LIGHT et
  aucun agrégat n'ont été modifiés.

## Sorties LIGHT

| # | chemin_relatif | longueur_mots | objet_principal | moment_parcours | capacites_transverses | procedure | transition_objet | regle_ou_condition | contrainte_ou_limite | exception_ou_correction | genre_documentaire |
|---:|---|---:|---|---|---|:-:|:-:|:-:|:-:|:-:|---|
| 1 | application-mobile.md | 312 | application mobile (accès utilisateur / accès compagnon) | indetermine | mobile, planning, automatisation | oui | non | oui | oui | non | definitionnel (avec procédure associée) |
| 2 | assistance/le-support-technique.md | 464 | ticket de support technique | indetermine | communication, notifications, support_editeur | oui | non | non | oui | oui | faq_depannage |
| 3 | assistance/les-tutos-video.md | 194 | tutos vidéo (support) | indetermine | communication, support_editeur | oui | non | non | non | non | procedure |
| 4 | assistance/que-deviennent-mes-demandes-damelioration-du-logiciel-apres-en-avoir-fait-part-a-lequipe-support.md | 367 | traitement des demandes d'amélioration produit | indetermine | communication, automatisation, support_editeur | non | non | non | oui | non | definitionnel (ton partiellement promotionnel) |
| 5 | conformite/attestation-de-conformite.md | 134 | attestation de conformité (anti-fraude TVA) | indetermine | conformite_reglementaire, documents | oui | non | oui | non | non | politique_legale (avec procédure associée) |
| 6 | conformite/la-facture-electronique.md | 666 | facturation électronique / plateforme agréée | facturation | conformite_reglementaire, integrations, documents | non | oui | oui | oui | non | definitionnel (avec glossaire et calendrier réglementaire) |
| 7 | conformite/la-signature-electronique.md | 166 | signature électronique | devis | conformite_reglementaire, documents, mobile | non | non | oui | oui | non | definitionnel (ton partiellement promotionnel) |
| 8 | index.md | 839 | présentation générale / FAQ (licence, tarifs, conformité, hébergement, sécurité, migration) | indetermine | paiement, conformite_reglementaire, securite_compte | non | non | oui | oui | non | autre (page multi-sujets, FAQ d'accueil — cf. limites) |
| 9 | le-menu-principal/assistance.md | 84 | assistance (accès aux 3 services : documentation, tutos, support) | indetermine | communication, support_editeur | non | non | non | non | non | autre (page-carrefour renvoyant vers 3 sous-articles) |
| 10 | le-menu-principal/bibliotheque.md | 280 | bibliothèque (ouvrages vs éléments — structure du catalogue) | indetermine | catalogue | non | non | non | non | non | definitionnel |
| 11 | le-menu-principal/bibliotheque/batichiffrage-c.md | 639 | bibliothèque de prix tierce (BatiChiffrage©, intégration) | devis | catalogue, integrations, paiement | non | oui | non | non | non | definitionnel (avec liens procéduraux) |
| 12 | le-menu-principal/bibliotheque/batichiffrage-c/utiliser-batichiffrage-c.md | 163 | bibliothèque de prix tierce (BatiChiffrage©, paramétrage des prix) | devis | catalogue, integrations | oui | non | non | non | non | procedure (article inachevé — cf. limites) |
| 13 | le-menu-principal/bibliotheque/elements.md | 48 | indetermine (page en construction, aucun contenu exploitable) | indetermine | catalogue | non | non | non | non | non | autre (page en cours d'élaboration) |
| 14 | le-menu-principal/bibliotheque/elements/fournitures.md | 43 | indetermine (page sans contenu exploitable, navigation seule) | indetermine | catalogue | non | non | non | non | non | autre (stub de navigation) |
| 15 | le-menu-principal/bibliotheque/elements/location.md | 43 | indetermine (page sans contenu exploitable, navigation seule) | indetermine | catalogue | non | non | non | non | non | autre (stub de navigation) |
| 16 | le-menu-principal/bibliotheque/elements/main-doeuvre.md | 43 | indetermine (page sans contenu exploitable, navigation seule) | indetermine | — | non | non | non | non | non | autre (stub de navigation) |
| 17 | le-menu-principal/bibliotheque/elements/outillage.md | 42 | indetermine (page sans contenu exploitable, navigation seule) | indetermine | — | non | non | non | non | non | autre (stub de navigation) |
| 18 | le-menu-principal/bibliotheque/elements/sous-traitance.md | 42 | indetermine (page sans contenu exploitable, navigation seule) | indetermine | — | non | non | non | non | non | autre (stub de navigation) |
| 19 | le-menu-principal/bibliotheque/familles.md | 546 | famille (organisation de la bibliothèque : famille métier / famille ouvrage-élément) | indetermine | catalogue, recherche | oui | non | non | non | non | procedure |
| 20 | le-menu-principal/bibliotheque/ouvrages.md | 192 | ouvrage (bibliothèque, prestation vendue au client) | devis | catalogue, paiement | non | non | non | non | non | definitionnel (avec liens procéduraux) |
| 21 | le-menu-principal/bibliotheque/ouvrages/gestion-des-ouvrages.md | 786 | ouvrage (création, mise à jour, gestion depuis devis et bibliothèque) | devis | catalogue, documents, paiement | oui | oui | oui | oui | non | procedure |
| 22 | le-menu-principal/bibliotheque/ouvrages/les-ouvrages-composes.md | 798 | ouvrage composé (décomposition en éléments : matériaux, main d'œuvre, location, sous-traitance, outillage) | devis | catalogue, paiement, integrations | oui | oui | oui | non | non | definitionnel (avec exemple chiffré et procédure associée) |
| 23 | le-menu-principal/bibliotheque/textes.md | 248 | texte enregistré (bibliothèque de textes réutilisables) | indetermine | documents, communication, automatisation | oui | non | oui | non | non | procedure |
| 24 | le-menu-principal/chantiers-personnel.md | 59 | indetermine (page-carrefour, chantiers/personnel) | indetermine | planning | non | non | non | non | non | autre (page-carrefour renvoyant vers 5 sous-articles) |
| 25 | le-menu-principal/chantiers-personnel/bons-dintervention.md | 49 | indetermine (page en construction, aucun contenu exploitable) | indetermine | — | non | non | non | non | non | autre (page en cours d'élaboration) |
| 26 | le-menu-principal/chantiers-personnel/chantiers.md | 781 | chantier (concept, distinction chantier/marché de travaux, statuts) | chantier-intervention | planning, paiement | non | oui | oui | oui | non | definitionnel (avec statuts et règles associées) |
| 27 | le-menu-principal/chantiers-personnel/chantiers/creer-un-chantier.md | 278 | chantier (création, 3 méthodes) | chantier-intervention | planning | oui | oui | oui | non | non | procedure |
| 28 | le-menu-principal/chantiers-personnel/chantiers/gestion-de-chantier-analyse-et-pilotage.md | 917 | fiche chantier (analyse, pilotage, simulation d'avancement) | chantier-intervention | planning, paiement, documents | oui | oui | oui | oui | non | reference_configuration |
| 29 | le-menu-principal/chantiers-personnel/personnel.md | 172 | personnel (fiche salarié/intérimaire, gestion RH) | indetermine | roles, conformite_reglementaire, planning | non | non | non | oui | non | definitionnel (avec réserve réglementaire) |
| 30 | le-menu-principal/chantiers-personnel/personnel/horaires-specifiques.md | 132 | horaires spécifiques (personnel) | indetermine | planning, roles | oui | non | non | non | non | procedure |
| 31 | le-menu-principal/chantiers-personnel/personnel/la-fiche-personnel-salarie.md | 962 | fiche personnel/salarié (état civil, contrat, rémunération, accès mobile compagnons) | indetermine | roles, conformite_reglementaire, paiement | oui | non | oui | oui | oui | reference_configuration |
| 32 | le-menu-principal/chantiers-personnel/personnel/la-liste-du-personnel.md | 137 | liste du personnel (filtres, statuts) | indetermine | roles, recherche | oui | non | oui | non | non | reference_configuration |
| 33 | le-menu-principal/chantiers-personnel/personnel/synchroniser-le-planning-chantier-avec-lagenda-des-compagnons.md | 361 | synchronisation planning/agenda (Google/Outlook/iCal, compagnons) | indetermine | integrations, planning, mobile | oui | non | oui | oui | non | procedure |
| 34 | le-menu-principal/chantiers-personnel/planning.md | 134 | planning (chantiers, phases, personnel) | chantier-intervention | planning, mobile | non | non | non | non | non | definitionnel (ton partiellement promotionnel) |
| 35 | le-menu-principal/chantiers-personnel/planning/affecter-du-personnel.md | 661 | affectation de personnel (phases de chantier, planning) | chantier-intervention | planning, roles, automatisation | oui | oui | oui | non | non | procedure |
| 36 | le-menu-principal/chantiers-personnel/planning/planning-chantier.md | 650 | planning de chantier (phases, dépendances type Gantt) | chantier-intervention | planning, automatisation | oui | oui | oui | non | non | procedure |
| 37 | le-menu-principal/chantiers-personnel/saisie-des-heures.md | 154 | saisie des heures (objectifs : coût salarial, rentabilité chantier) | chantier-intervention | planning, paiement | non | non | non | non | non | definitionnel (avec liens procéduraux) |
| 38 | le-menu-principal/chantiers-personnel/saisie-des-heures/consulter-et-exporter-les-heures.md | 333 | heures saisies (consultation, export, filtres) | chantier-intervention | planning, documents, recherche | oui | non | oui | non | non | reference_configuration |
| 39 | le-menu-principal/chantiers-personnel/saisie-des-heures/saisie-des-heures-au-bureau.md | 198 | saisie des heures « au bureau » (transfert depuis planning, saisie manuelle) | chantier-intervention | planning, automatisation | oui | oui | non | non | oui | procedure |
| 40 | le-menu-principal/chantiers-personnel/saisie-des-heures/saisie-des-heures-par-les-salaries-et-chefs-dequipes.md | 116 | saisie des heures par les salariés/chefs d'équipe (application mobile compagnons) | chantier-intervention | mobile, planning, roles | non | non | non | oui | non | definitionnel (ton partiellement promotionnel) |
| 41 | le-menu-principal/comptabilite.md | 122 | comptabilité (export, connexion expert-comptable) | indetermine | conformite_reglementaire, integrations, roles | non | non | non | non | non | definitionnel (ton partiellement promotionnel, page-carrefour) |
| 42 | le-menu-principal/comptabilite/archives.md | 277 | archives (factures, archive fiscale NF-525) | facturation | conformite_reglementaire, documents | oui | non | oui | oui | non | politique_legale (avec procédure associée) |
| 43 | le-menu-principal/comptabilite/chiffres-cles.md | 49 | indetermine (page en construction, aucun contenu exploitable) | indetermine | — | non | non | non | non | non | autre (page en cours d'élaboration) |
| 44 | le-menu-principal/comptabilite/exports-comptables.md | 345 | export comptable (journal des ventes/achats/règlements) | facturation | conformite_reglementaire, integrations, documents | oui | oui | oui | non | non | procedure |
| 45 | le-menu-principal/comptabilite/parametrage-comptable.md | 115 | paramétrage comptable (comptes, TVA, familles, tiers) | indetermine | conformite_reglementaire, roles | non | non | non | non | non | autre (page-carrefour renvoyant vers 8 sous-articles) |
| 46 | le-menu-principal/comptabilite/parametrage-comptable/comptes-complementaires.md | 78 | comptes complémentaires (majorations/déductions factures, compte prorata) | indetermine | conformite_reglementaire | oui | non | oui | non | non | reference_configuration |
| 47 | le-menu-principal/comptabilite/parametrage-comptable/comptes-de-charge-et-produit-par-famille-metier.md | 243 | compte de charge/produit par famille métier (résolution en cascade) | indetermine | conformite_reglementaire, automatisation | non | non | oui | non | non | reference_configuration (avec logique de résolution en cascade) |
| 48 | le-menu-principal/comptabilite/parametrage-comptable/comptes-de-charge-et-produit-par-type-delement.md | 321 | compte de charge/produit par type d'élément (résolution en cascade, compte par fournisseur) | indetermine | conformite_reglementaire, automatisation | non | non | oui | non | non | reference_configuration (avec logique de résolution en cascade) |
| 49 | le-menu-principal/comptabilite/parametrage-comptable/comptes-de-tiers.md | 316 | comptes de tiers / comptes auxiliaires (clients, fournisseurs, sous-traitants) | indetermine | conformite_reglementaire, roles | oui | non | oui | non | non | reference_configuration |
| 50 | le-menu-principal/comptabilite/parametrage-comptable/comptes-de-tva.md | 151 | comptes de TVA (facture d'acompte, extensions par taux) | facturation | conformite_reglementaire | oui | non | oui | non | oui | reference_configuration |
| 51 | le-menu-principal/comptabilite/parametrage-comptable/comptes-financiers.md | 78 | comptes financiers (comptes bancaires/caisse, extension par mode de paiement) | indetermine | conformite_reglementaire, paiement | oui | non | non | non | non | reference_configuration |
| 52 | le-menu-principal/comptabilite/parametrage-comptable/exercice-comptable.md | 51 | indetermine (page sans contenu exploitable, navigation seule) | indetermine | — | non | non | non | non | non | autre (stub de navigation) |
| 53 | le-menu-principal/comptabilite/parametrage-comptable/journaux.md | 38 | journaux comptables (codes achats/ventes/banques/caisse) | indetermine | conformite_reglementaire | oui | non | non | non | non | reference_configuration |
| 54 | le-menu-principal/comptabilite/parametrage-comptable/moyens-de-paiement.md | 105 | moyens de paiement (extension de compte comptable par mode de règlement) | indetermine | conformite_reglementaire, paiement, automatisation | oui | non | non | non | non | reference_configuration |
| 55 | le-menu-principal/comptabilite/tva-sur-encaissement.md | 189 | TVA sur encaissement (déclaration, tableau de suivi) | facturation | conformite_reglementaire, paiement | non | non | oui | oui | non | definitionnel (avec exemple chiffré) |
| 56 | le-menu-principal/contacts.md | 164 | contacts (catégories : clients, prospects, fournisseurs, sous-traitants) | indetermine | roles, recherche | oui | non | non | non | non | procedure |
| 57 | le-menu-principal/contacts/clients.md | 216 | client (fichier clients/prospects, relation, rentabilité) | indetermine | roles, recherche | non | non | non | non | non | definitionnel (avec liens procéduraux) |
| 58 | le-menu-principal/contacts/clients/creer-un-client.md | 247 | client (création, depuis devis ou liste) | devis | roles, documents | oui | oui | non | non | non | procedure |
| 59 | le-menu-principal/contacts/clients/la-fiche-client.md | 604 | fiche client (informations, adresses, contacts, conditions de règlement, activité, ProGBox) | indetermine | documents, conformite_reglementaire, paiement | oui | non | oui | oui | non | reference_configuration |
| 60 | le-menu-principal/contacts/fournisseurs.md | 136 | fournisseur (fichier fournisseurs, achats, livraisons, factures d'achat) | achat | catalogue, documents, conformite_reglementaire | non | non | non | non | non | definitionnel (avec liens procéduraux) |
| 61 | le-menu-principal/contacts/fournisseurs/creer-un-fournisseur.md | 201 | fournisseur (création, depuis commande/facture ou liste) | achat | roles, documents | oui | oui | non | non | non | procedure |
| 62 | le-menu-principal/contacts/fournisseurs/la-fiche-fournisseur.md | 339 | fiche fournisseur (informations, adresses, contacts, conditions de règlement, activité, ProGBox) | achat | documents, conformite_reglementaire, paiement | oui | non | oui | oui | non | reference_configuration |
| 63 | le-menu-principal/contacts/prospects.md | 83 | prospect (distinction client/prospect) | indetermine | roles | non | non | non | non | non | definitionnel (renvoi vers l'article Clients) |
| 64 | le-menu-principal/contacts/sous-traitants.md | 45 | sous-traitant (gestion identique à fournisseur) | indetermine | roles | non | non | non | non | non | definitionnel (renvoi vers l'article Fournisseurs) |
| 65 | le-menu-principal/depenses.md | 46 | dépenses (achats, commandes, livraisons, factures d'achat) | achat | paiement, documents | non | non | non | non | non | autre (page-carrefour, plusieurs sous-articles inachevés — cf. limites) |
| 66 | le-menu-principal/depenses/commande-fournisseur.md | 39 | indetermine (page en construction, aucun contenu exploitable) | indetermine | — | non | non | non | non | non | autre (page en cours d'élaboration) |
| 67 | le-menu-principal/depenses/commande-sous-traitant.md | 39 | indetermine (page en construction, aucun contenu exploitable) | indetermine | — | non | non | non | non | non | autre (page en cours d'élaboration) |
| 68 | le-menu-principal/depenses/factures-dachat.md | 89 | facture d'achat (moyens d'intégration : saisie, photo, PDP) | achat | paiement, documents, automatisation | non | non | non | non | non | definitionnel (avec liens procéduraux) |
| 69 | le-menu-principal/depenses/factures-dachat/facture-electronique-recue-par-pdp.md | 192 | facturation électronique / plateforme agréée (réception, PDP fournisseurs) | achat | conformite_reglementaire, integrations, automatisation | non | non | oui | oui | non | definitionnel (avec calendrier réglementaire) |
| 70 | le-menu-principal/depenses/factures-dachat/photographier-les-tickets-de-caisse.md | 32 | indetermine (page en construction, aucun contenu exploitable) | indetermine | — | non | non | non | non | non | autre (page en cours d'élaboration) |
| 71 | le-menu-principal/depenses/factures-dachat/saisie-des-factures-fournisseurs.md | 254 | facture fournisseur (saisie : PDF/image, OCR/océrisation, papier) | achat | automatisation, documents, mobile | oui | oui | oui | non | non | procedure |
| 72 | le-menu-principal/depenses/livraisons.md | 39 | indetermine (page en construction, aucun contenu exploitable) | indetermine | — | non | non | non | non | non | autre (page en cours d'élaboration) |
| 73 | le-menu-principal/depenses/transferts-materiaux.md | 39 | indetermine (page en construction, aucun contenu exploitable) | indetermine | — | non | non | non | non | non | autre (page en cours d'élaboration) |
| 74 | le-menu-principal/devis-factures.md | 229 | devis/factures (présentation générale, fonctionnalités : chiffrage, signature, facturation, avenants) | indetermine | conformite_reglementaire, documents, automatisation | non | non | non | non | oui | definitionnel (ton partiellement promotionnel) |
| 75 | le-menu-principal/devis-factures/attestations-de-tva.md | 253 | attestation de TVA (remplacement réglementaire, texte automatique dans le devis) | devis | conformite_reglementaire, documents, automatisation | non | non | oui | oui | oui | politique_legale |
| 76 | le-menu-principal/devis-factures/avenant.md | 435 | avenant (devis complémentaire en cours de chantier) | devis | documents, paiement | oui | oui | oui | oui | non | procedure |
| 77 | le-menu-principal/devis-factures/copie-revision-avenant.md | 351 | devis (copie, révision, avenant — actions selon statut) | devis | documents, paiement | oui | oui | oui | non | non | procedure |
| 78 | le-menu-principal/devis-factures/devis-type-et-bpu.md | 862 | devis type / BPU (bibliothèque de contenus de devis réutilisables) | devis | catalogue, paiement, conformite_reglementaire | oui | oui | oui | oui | non | procedure |
| 79 | le-menu-principal/devis-factures/devis.md | 465 | devis (liste, statuts : brouillon/finalisé/envoyé/accepté/refusé) | devis | recherche, documents | oui | oui | oui | oui | non | reference_configuration (avec liens procéduraux) |
| 80 | le-menu-principal/devis-factures/devis/chiffrer-un-devis.md | 556 | chiffrage de devis (3 méthodes : simple, avancée, expert/ouvrages composés) | devis | catalogue, paiement | oui | oui | non | oui | non | procedure |
| 81 | le-menu-principal/devis-factures/devis/creer-un-devis.md | 235 | devis (création, 4 méthodes) | devis | roles, documents | oui | non | non | non | non | procedure |
| 82 | le-menu-principal/devis-factures/devis/facturer-un-devis.md | 53 | indetermine (page sans contenu exploitable, navigation seule) | indetermine | — | non | non | non | non | non | autre (stub de navigation) |
| 83 | le-menu-principal/devis-factures/devis/finaliser-et-envoyer-un-devis.md | 604 | devis (finalisation, envoi : mail, signature électronique, remise en main propre) | devis | documents, communication, securite_compte | oui | oui | oui | oui | non | procedure |
| 84 | le-menu-principal/devis-factures/devis/la-synthese-du-devis.md | 54 | indetermine (page sans contenu exploitable, navigation seule) | indetermine | — | non | non | non | non | non | autre (stub de navigation) |
| 85 | le-menu-principal/devis-factures/devis/le-pied-du-devis.md | 916 | pied de devis (conditions de règlement, texte d'acceptation, gestion des déchets, totaux, mentions TVA) | devis | conformite_reglementaire, paiement, documents | oui | non | oui | oui | non | politique_legale (avec procédures associées — cf. limites, contenu réglementaire dense) |
| 86 | le-menu-principal/devis-factures/devis/lentete-du-devis.md | 487 | entête de devis (informations, objet, client, chantier) | devis | roles, documents | oui | non | oui | oui | non | procedure |
| 87 | le-menu-principal/devis-factures/devis/les-lignes-du-devis.md | 84 | lignes de devis (chiffrage, cœur de métier) | devis | catalogue, paiement | non | non | non | non | non | definitionnel (avec liens procéduraux, ton partiellement promotionnel) |
| 88 | le-menu-principal/devis-factures/devis/les-lignes-du-devis/creer-une-ligne-de-devis.md | 451 | ligne de devis (création : titre, sous-titre, prestation, commentaire, saut de page) | devis | catalogue, documents | oui | non | non | non | non | procedure |
| 89 | le-menu-principal/devis-factures/devis/les-lignes-du-devis/fonctionnalites-avancees.md | 474 | ligne de devis (fonctionnalités avancées : dupliquer, déplacer, afficher composition) | devis | catalogue, recherche | oui | non | non | non | non | procedure (article partiellement incomplet — plusieurs sections sans contenu, cf. limites) |
| 90 | le-menu-principal/devis-factures/devis/les-lignes-du-devis/saisir-une-ligne-de-devis.md | 1064 | ligne de devis (contenu détaillé : numérotation, désignation, quantité, unité, prix, TVA, types de vente) | devis | catalogue, conformite_reglementaire, automatisation | oui | non | oui | oui | non | reference_configuration |
| 91 | le-menu-principal/devis-factures/devis/mentions-obligatoires-du-devis.md | 779 | mentions obligatoires du devis (cadre légal) | devis | conformite_reglementaire, documents | non | non | oui | oui | non | politique_legale |
| 92 | le-menu-principal/devis-factures/devis/onglets-parametres-et-actions.md | 355 | devis (onglets, actions : enregistrer, finaliser, facturer) | devis | documents, automatisation | oui | oui | oui | oui | non | procedure (article partiellement incomplet — sections « Les onglets »/« Actions »/« Options » vides, cf. limites) |
| 93 | le-menu-principal/devis-factures/devis/variantes-et-options.md | 239 | option/variante de devis (lignes non comptées dans le total) | devis | catalogue, documents | oui | oui | non | non | non | procedure |
| 94 | le-menu-principal/devis-factures/echeances-clients.md | 269 | échéances clients (factures impayées, relances niveau 1-3) | facturation | paiement, communication, documents | oui | non | non | non | non | procedure (avec conseils pratiques) |
| 95 | le-menu-principal/devis-factures/factures.md | 188 | facture (liste, recherche, filtres) | facturation | recherche, documents | oui | non | non | non | non | procedure |
| 96 | le-menu-principal/devis-factures/factures/annuler-ou-modifier-une-facture.md | 612 | facture (annulation/modification via avoir) | facturation | conformite_reglementaire, documents | oui | oui | oui | oui | oui | politique_legale (avec procédures associées) |
| 97 | le-menu-principal/devis-factures/factures/creer-une-facture.md | 492 | facture (création : acompte, travaux, avancement/situation, directe, avoir, copie) | facturation | paiement, documents, automatisation | oui | oui | oui | non | non | procedure |
| 98 | le-menu-principal/devis-factures/factures/finaliser-et-envoyer-une-facture.md | 702 | facture (finalisation, envoi, mode test, mentions légales) | facturation | conformite_reglementaire, integrations, documents | oui | oui | oui | oui | non | politique_legale (avec procédures associées) |
| 99 | le-menu-principal/devis-factures/factures/le-pied-de-la-facture.md | 511 | pied de facture (conditions de règlement, totaux, remises, déductions, avancement) | facturation | paiement, documents | oui | non | oui | non | non | reference_configuration |
| 100 | le-menu-principal/devis-factures/factures/lentete-de-la-facture.md | 651 | entête de facture (informations, objet, client, chantier) | facturation | roles, documents | oui | non | oui | oui | non | procedure |
| 101 | le-menu-principal/devis-factures/factures/les-differents-types-de-factures.md | 484 | types de facture (acompte, travaux, avancement/situation, directe, avoir) | facturation | conformite_reglementaire, paiement | non | non | oui | oui | non | politique_legale (avec définitions) |
| 102 | le-menu-principal/devis-factures/factures/les-lignes-de-la-facture.md | 896 | ligne de facture (saisie d'avancement, suppression, annulation, modification) | facturation | documents, catalogue | oui | non | oui | oui | non | procedure |
| 103 | le-menu-principal/devis-factures/factures/onglets-parametres-et-actions.md | 721 | facture (onglets, actions : règlements, avenant, nouvelle situation) | facturation | paiement, documents, automatisation | oui | oui | non | oui | non | procedure |
| 104 | le-menu-principal/reglements.md | 86 | règlements (encaissement clients, paiement fournisseurs, retenue de garantie) | facturation | paiement, communication | non | non | non | non | non | definitionnel (avec liens procéduraux) |
| 105 | le-menu-principal/reglements/encaissement-dune-facture-client.md | 383 | encaissement de facture client (saisie manuelle du règlement) | facturation | paiement, documents | oui | oui | non | non | non | procedure (section rapprochement bancaire inachevée — cf. limites) |
| 106 | le-menu-principal/reglements/paiement-dune-facture-fournisseur.md | 53 | indetermine (page sans contenu exploitable, navigation seule) | indetermine | — | non | non | non | non | non | autre (stub de navigation) |
| 107 | le-menu-principal/reglements/reclamer-et-encaisser-une-retenue-de-garantie.md | 50 | indetermine (page sans contenu exploitable, navigation seule) | indetermine | — | non | non | non | non | non | autre (stub de navigation) |
| 108 | le-menu-principal/service-juridique.md | 411 | service juridique (Caarl : chatbot IA, modèles de documents, avocats, recouvrement) | indetermine | conformite_reglementaire, communication, automatisation | non | non | non | non | non | marketing_dans_aide |
| 109 | le-menu-principal/service-juridique/base-de-modeles-de-documents.md | 192 | modèle de document juridique (Caarl, téléchargement) | indetermine | conformite_reglementaire, documents, recherche | oui | non | non | non | non | procedure (ton partiellement promotionnel) |
| 110 | le-menu-principal/service-juridique/chatbot-ia-et-hotline-juridique.md | 218 | chatbot IA / hotline juridique (Caarl) | indetermine | conformite_reglementaire, communication, automatisation | oui | non | oui | oui | non | procedure (ton partiellement promotionnel) |
| 111 | le-menu-principal/service-juridique/consultations-avocats-en-visioconference.md | 439 | consultation avocat en visioconférence (Caarl) | indetermine | communication, conformite_reglementaire, automatisation | oui | non | oui | oui | non | reference_configuration (avec procédure et règles d'annulation) |
| 112 | le-menu-principal/service-juridique/recouvrement-de-factures-impayees.md | 342 | recouvrement de factures impayées (Caarl, amiable + judiciaire) | facturation | paiement, conformite_reglementaire, communication | non | oui | oui | non | non | definitionnel (avec liens procéduraux, ton partiellement promotionnel) |
| 113 | le-menu-principal/service-juridique/recouvrement-de-factures-impayees/conditions-dacces-au-service-de-recouvrement-amiable.md | 351 | conditions d'accès au recouvrement amiable (créance certaine/liquide/exigible, délais de prescription) | facturation | conformite_reglementaire, paiement | non | non | oui | oui | non | politique_legale (sous forme de FAQ) |
| 114 | le-menu-principal/service-juridique/recouvrement-de-factures-impayees/depot-de-ma-facture-et-suivi.md | 684 | dépôt de facture impayée et suivi (recouvrement, Caarl) | facturation | paiement, documents, conformite_reglementaire | oui | oui | oui | oui | oui | faq_depannage |
| 115 | le-menu-principal/service-juridique/recouvrement-de-factures-impayees/paiement-de-la-commission.md | 459 | commission de recouvrement (honoraires, barème, reversement) | facturation | paiement, conformite_reglementaire | non | non | oui | oui | oui | faq_depannage |
| 116 | le-menu-principal/tableaux-de-suivi.md | 448 | tableau de suivi (board personnalisable, type CRM simplifié) | indetermine | planning, recherche | oui | oui | non | oui | non | definitionnel (fonctionnalité en version bêta — cf. limites) |
| 117 | les-options/pourquoi-des-options.md | 327 | options (modèle économique : Essential/Premium/All Inclusive, liste des options) | indetermine | paiement | non | non | non | non | non | marketing_dans_aide |
| 118 | les-options/pourquoi-des-options/acces-compagnons.md | 157 | option « accès compagnons » (application mobile salariés) | indetermine | mobile, planning, paiement | oui | non | oui | oui | non | procedure (ton partiellement promotionnel) |
| 119 | les-options/pourquoi-des-options/assistance-juridique-et-recouvrement.md | 59 | option « assistance juridique et recouvrement » | indetermine | conformite_reglementaire, communication | non | non | non | non | non | marketing_dans_aide |
| 120 | les-options/pourquoi-des-options/bibliotheques-batichiffrage-c.md | 107 | option « bibliothèques BatiChiffrage© » (achat de licence par corps de métier) | devis | catalogue, paiement | oui | non | non | non | non | procedure (ton partiellement promotionnel) |
| 121 | les-options/pourquoi-des-options/connexion-comptes-bancaires.md | 84 | option « connexion comptes bancaires » (Powens, rapprochement) | indetermine | integrations, paiement, securite_compte | oui | non | non | non | non | procedure (ton partiellement promotionnel) |
| 122 | les-options/pourquoi-des-options/connexions-comptables.md | 67 | indetermine (page sans contenu exploitable, navigation seule) | indetermine | — | non | non | non | non | non | autre (stub de navigation) |
| 123 | les-options/pourquoi-des-options/connexions-comptables/mes-outils-comptables-en-option.md | 327 | connexion PDP / OD (outils comptables en option, réforme facturation électronique) | facturation | conformite_reglementaire, integrations, paiement | non | non | oui | non | non | marketing_dans_aide (avec cadre réglementaire) |
| 124 | les-options/pourquoi-des-options/connexions-comptables/mes-outils-comptables-en-option/acd.md | 61 | connexion comptable ACD (synchronisation factures avec expert-comptable) | facturation | integrations, conformite_reglementaire | oui | non | non | non | non | procedure |
| 125 | les-options/pourquoi-des-options/connexions-comptables/mes-outils-comptables-en-option/cegid-loop.md | 65 | connexion comptable Cegid Loop (synchronisation factures avec expert-comptable) | facturation | integrations, conformite_reglementaire | oui | non | non | non | non | procedure |
| 126 | les-options/pourquoi-des-options/connexions-comptables/mes-outils-comptables-en-option/inqom.md | 61 | connexion comptable Inqom (synchronisation factures avec expert-comptable) | facturation | integrations, conformite_reglementaire | oui | non | non | non | non | procedure |
| 127 | les-options/pourquoi-des-options/connexions-comptables/mes-outils-comptables-en-option/myunisoft.md | 63 | connexion comptable MyUnisoft (synchronisation factures avec expert-comptable) | facturation | integrations, conformite_reglementaire | oui | non | non | non | non | procedure |
| 128 | les-options/pourquoi-des-options/connexions-comptables/mes-outils-comptables-en-option/sage-100-fr.md | 67 | connexion comptable Sage 100 FR (synchronisation factures avec expert-comptable) | facturation | integrations, conformite_reglementaire | oui | non | non | non | non | procedure |
| 129 | les-options/pourquoi-des-options/connexions-comptables/mes-outils-comptables-en-option/sage-bob-50.md | 71 | connexion comptable Sage BOB 50 (synchronisation factures avec expert-comptable) | facturation | integrations, conformite_reglementaire | oui | non | non | non | non | procedure |
| 130 | les-options/pourquoi-des-options/connexions-comptables/mes-outils-comptables-en-option/sage-generation-experts.md | 70 | connexion comptable Sage Génération Experts (synchronisation factures avec expert-comptable) | facturation | integrations, conformite_reglementaire | oui | non | non | non | non | procedure |
| 131 | les-options/pourquoi-des-options/connexions-comptables/mes-outils-de-gestion-externe.md | 52 | outils de gestion externe (transfert de données de facturation/comptables) | facturation | integrations, documents | non | non | non | non | non | definitionnel (avec liens procéduraux) |
| 132 | les-options/pourquoi-des-options/connexions-comptables/mes-outils-de-gestion-externe/meg-mon-expert-en-gestion.md | 87 | connexion comptable MEG (mon expert en gestion) | facturation | integrations, conformite_reglementaire | oui | non | oui | oui | non | procedure |
| 133 | les-options/pourquoi-des-options/connexions-comptables/mes-outils-de-gestion-externe/pennylane.md | 475 | connexion comptable Pennylane (synchronisation factures, mode d'envoi) | facturation | integrations, conformite_reglementaire, automatisation | oui | oui | oui | non | non | procedure (ton partiellement promotionnel) |
| 134 | les-options/pourquoi-des-options/connexions-supplementaires.md | 250 | option « connexions supplémentaires » (utilisateurs simultanés) | indetermine | roles, paiement | oui | non | oui | oui | non | reference_configuration (avec procédure d'achat) |
| 135 | les-options/pourquoi-des-options/gestion-des-droits.md | 85 | option « gestion des droits » (permissions utilisateurs) | indetermine | roles, permissions, paiement | oui | non | non | non | non | procedure (ton partiellement promotionnel) |
| 136 | les-options/pourquoi-des-options/maintenance-et-interventions.md | 81 | option « maintenance et interventions » (module) | chantier-intervention | planning, paiement | oui | non | non | non | non | procedure (ton partiellement promotionnel, page-carrefour) |
| 137 | les-options/pourquoi-des-options/maintenance-et-interventions/contrat-de-maintenance.md | 286 | contrat de maintenance (création, reconduction, consultation) | chantier-intervention | planning, paiement, notifications | oui | oui | non | non | non | procedure |
| 138 | les-options/pourquoi-des-options/maintenance-et-interventions/interventions.md | 481 | bon d'intervention (création, planification, signature, facturation, suivi) | chantier-intervention | planning, mobile, documents | oui | oui | non | non | non | procedure |
| 139 | les-options/pourquoi-des-options/maintenance-et-interventions/materiels-installes.md | 370 | matériel installé (enregistrement, traçabilité, tâches de maintenance) | chantier-intervention | gestion_stock, planning, documents | oui | non | oui | oui | non | reference_configuration |
| 140 | les-options/pourquoi-des-options/ocerisation.md | 113 | option « océrisation » (crédits OCR pour factures/tickets) | achat | automatisation, paiement | oui | non | oui | oui | non | procedure (ton partiellement promotionnel) |
| 141 | les-options/pourquoi-des-options/signature-electronique.md | 466 | signature électronique (devis, envoi, vérification SMS) | devis | securite_compte, paiement, notifications | oui | oui | oui | non | non | procedure (ton partiellement promotionnel) |
| 142 | les-options/pourquoi-des-options/souscrire-une-option.md | 77 | souscription d'option (boutique, paiement, renouvellement) | indetermine | paiement, automatisation | oui | non | oui | non | non | procedure |
| 143 | les-options/pourquoi-des-options/stockage-progbox.md | 47 | indetermine (page sans contenu exploitable, navigation seule) | indetermine | — | non | non | non | non | non | autre (stub de navigation) |
| 144 | pour-bien-demarrer/demarrer-avec-progbat/importer-mes-contacts.md | 335 | import de contacts (fichier Excel/CSV) | indetermine | documents, integrations | oui | non | oui | non | non | procedure |
| 145 | pour-bien-demarrer/demarrer-avec-progbat/importer-mes-devis-et-factures.md | 128 | import de devis/factures (migration depuis ancien système) | devis | documents, integrations | non | non | non | non | non | definitionnel (avec liens procéduraux) |
| 146 | pour-bien-demarrer/demarrer-avec-progbat/importer-mes-devis-et-factures/importer-mes-devis.md | 591 | import de devis (fichier Excel/CSV, structuration automatique) | devis | documents, integrations, catalogue | oui | oui | oui | oui | non | procedure |
| 147 | pour-bien-demarrer/demarrer-avec-progbat/importer-mes-devis-et-factures/poursuivre-la-facturation-faite-sur-mon-ancien-logiciel.md | 924 | migration de facturation (poursuite depuis un ancien logiciel, cas multiples : devis, acompte, situations) | facturation | conformite_reglementaire, documents, paiement | oui | oui | oui | oui | non | politique_legale (avec procédures multiples associées) |
| 148 | pour-bien-demarrer/demarrer-avec-progbat/importer-une-bibliotheque.md | 61 | import de bibliothèque (fournitures, ouvrages, tarif fournisseur) | indetermine | catalogue, documents | oui | non | non | non | non | procedure (page-carrefour) |
| 149 | pour-bien-demarrer/demarrer-avec-progbat/importer-une-bibliotheque/importer-mes-fournitures.md | 394 | import de fournitures (fichier ou tarif fournisseur) | indetermine | catalogue, documents, integrations | oui | non | oui | oui | non | procedure |
| 150 | pour-bien-demarrer/demarrer-avec-progbat/importer-une-bibliotheque/importer-mes-ouvrages.md | 64 | import d'ouvrages (fichier Excel/CSV) | indetermine | catalogue, documents | oui | non | non | non | non | procedure |
| 151 | pour-bien-demarrer/demarrer-avec-progbat/importer-une-bibliotheque/importer-un-tarif-fournisseur.md | 395 | import de tarif fournisseur (fichier fourniture ou tarif fournisseur — contenu quasi identique à #149, cf. limites) | indetermine | catalogue, documents, integrations | oui | non | oui | oui | non | procedure |
| 152 | pour-bien-demarrer/demarrer-avec-progbat/personnaliser-le-tableau-de-bord.md | 436 | tableau de bord (personnalisation : vignettes, lignes) | indetermine | recherche | oui | non | non | non | non | procedure |
| 153 | pour-bien-demarrer/parametrage.md | 82 | paramétrage (accès, droits administrateur) | indetermine | roles, permissions | non | non | oui | oui | non | definitionnel |
| 154 | pour-bien-demarrer/parametrage/mon-offre-progbat.md | 200 | offre ProGBat (licence, abonnement, factures, multi-comptes) | indetermine | paiement, roles | oui | non | oui | non | non | reference_configuration |
| 155 | pour-bien-demarrer/parametrage/mon-profil.md | 53 | indetermine (page sans contenu exploitable, navigation seule) | indetermine | — | non | non | non | non | non | autre (stub de navigation) |
| 156 | pour-bien-demarrer/parametrage/mon-profil/authentification-multifacteur.md | 322 | authentification multifacteur (sécurité de connexion) | indetermine | securite_compte | oui | non | oui | oui | non | procedure |
| 157 | pour-bien-demarrer/parametrage/mon-profil/envoi-demails.md | 502 | envoi d'emails (expéditeur, signature, méthode d'envoi : serveur ProGBat vs boîte mail propre) | indetermine | communication, integrations | oui | non | non | oui | non | reference_configuration (avec comparaison de méthodes) |
| 158 | pour-bien-demarrer/parametrage/mon-profil/envoi-demails/parametrer-ma-propre-messagerie.md | 382 | messagerie personnelle (connexion Gmail/Outlook/FAI/domaine à ProGBat) | indetermine | integrations, communication, securite_compte | oui | non | non | non | non | procedure |
| 159 | pour-bien-demarrer/parametrage/mon-profil/mon-profil.md | 162 | profil utilisateur (identifiant de connexion, mot de passe) | indetermine | securite_compte, roles | oui | non | oui | non | non | procedure |
| 160 | pour-bien-demarrer/parametrage/mon-profil/parametres-dutilisation.md | 302 | paramètres d'utilisation (enregistrement auto, visibilité privée, export CSV/Excel) | indetermine | automatisation, permissions, documents | oui | non | oui | oui | non | reference_configuration |
| 161 | pour-bien-demarrer/parametrage/parametres-de-lentreprise.md | 95 | indetermine (page sans contenu exploitable, navigation seule) | indetermine | — | non | non | non | non | non | autre (stub de navigation) |
| 162 | pour-bien-demarrer/parametrage/parametres-de-lentreprise/adresses.md | 193 | adresses de l'entreprise (siège social, établissements/dépôts) | indetermine | documents, conformite_reglementaire | oui | non | oui | non | non | procedure |
| 163 | pour-bien-demarrer/parametrage/parametres-de-lentreprise/assurances-et-conditions-generales.md | 250 | assurances et CGV (conditions générales de vente, mentions obligatoires) | indetermine | conformite_reglementaire, documents | oui | non | oui | oui | non | politique_legale (avec procédure associée) |
| 164 | pour-bien-demarrer/parametrage/parametres-de-lentreprise/attestation-de-conformite.md | 106 | attestation de conformité (paramétrage entreprise, génération) | indetermine | conformite_reglementaire, documents | oui | non | oui | non | non | politique_legale (avec procédure associée) |
| 165 | pour-bien-demarrer/parametrage/parametres-de-lentreprise/autres-parametres.md | 1174 | autres paramètres entreprise (signature, validité devis, conditions de règlement, acomptes, pénalités) | devis | conformite_reglementaire, paiement, documents | oui | non | oui | oui | non | reference_configuration (avec texte légal de pénalités) |
| 166 | pour-bien-demarrer/parametrage/parametres-de-lentreprise/comptes-bancaires.md | 308 | comptes bancaires (paramétrage, connexion Powens) | indetermine | integrations, paiement, securite_compte | oui | non | non | non | non | procedure |
| 167 | pour-bien-demarrer/parametrage/parametres-de-lentreprise/horaires.md | 80 | horaires (entreprise, prime repas) | indetermine | planning, paiement | oui | non | non | non | non | reference_configuration |
| 168 | pour-bien-demarrer/parametrage/parametres-de-lentreprise/informations-generales.md | 533 | informations générales entreprise (mentions légales, informations commerciales) | indetermine | conformite_reglementaire, documents | oui | non | oui | non | non | reference_configuration |
| 169 | pour-bien-demarrer/parametrage/parametres-de-lentreprise/marges.md | 584 | marge (concept de marge brute, calcul, mise à jour de la bibliothèque) | indetermine | catalogue, paiement | oui | oui | oui | non | non | definitionnel (avec formules de calcul et procédure associée) |
| 170 | pour-bien-demarrer/parametrage/parametres-de-lentreprise/numero-des-documents.md | 547 | numérotation des documents (factures, devis — séquence chronologique) | facturation | conformite_reglementaire, documents | oui | oui | oui | non | non | politique_legale (avec procédure associée) |
| 171 | pour-bien-demarrer/parametrage/parametres-de-lentreprise/tva.md | 100 | TVA (taux, mentions légales) | indetermine | conformite_reglementaire | non | non | oui | non | non | reference_configuration |
| 172 | pour-bien-demarrer/parametrage/utilisateurs.md | 82 | utilisateurs (accès, licence vs connexions simultanées) | indetermine | roles, paiement | non | non | oui | oui | non | definitionnel (avec liens procéduraux) |
| 173 | pour-bien-demarrer/parametrage/utilisateurs/creer-modifier-supprimer-un-utilisateur.md | 395 | utilisateur (création, droits par défaut : administrateur/utilisateur/expert-comptable) | indetermine | roles, permissions, securite_compte | oui | non | non | oui | non | reference_configuration |
| 174 | pour-bien-demarrer/parametrage/utilisateurs/gestion-des-droits-dacces.md | 704 | gestion des droits d'accès (rôles personnalisés, permissions détaillées, documents privés) | indetermine | roles, permissions, documents | oui | non | non | non | non | reference_configuration |
| 175 | pour-bien-demarrer/tester-progbat.md | 397 | essai gratuit ProGBat (inscription, compte de test réel, factures de test) | indetermine | paiement, conformite_reglementaire | oui | non | oui | oui | non | politique_legale (avec procédure associée) |
| 176 | presentation-generale/la-page-daccueil.md | 152 | page d'accueil (tableau de bord, onglets, accès rapides, menu général) | indetermine | recherche, documents | non | non | non | non | non | definitionnel (avec liens procéduraux) |
| 177 | presentation-generale/la-panicroom.md | 646 | FAQ dépannage (faux bugs courants : filtres actifs, multi-utilisateur, numérotation provisoire, chiffre d'affaires apparent) | indetermine | roles, recherche | non | non | non | non | oui | faq_depannage |
| 178 | presentation-generale/les-acces-rapides.md | 248 | accès rapides (recherche, raccourcis de consultation/création, multi-comptes) | indetermine | recherche, planning, roles | oui | non | non | non | non | reference_configuration |
| 179 | presentation-generale/les-documents-prives.md | 231 | document privé (devis/facture, statut public/privé, héritage) | indetermine | permissions, roles, documents | oui | non | oui | non | non | reference_configuration |
| 180 | presentation-generale/les-formulaires-et-zones-de-saisie.md | 391 | formulaires et zones de saisie (textes enregistrés, champs date, champs calculés, texte enrichi) | indetermine | documents, automatisation | oui | non | non | non | non | reference_configuration |
| 181 | presentation-generale/les-listes.md | 836 | liste (recherche, filtre, tri, export, modification en masse) | indetermine | recherche, documents | oui | oui | non | non | non | reference_configuration |
| 182 | presentation-generale/les-minutes-de-calcul-ou-modeles-de-calcul.md | 702 | minute de calcul / modèle de calcul (surface, volume, application automatique aux lignes de devis) | devis | catalogue, automatisation | oui | oui | non | oui | non | procedure (avec exemples de formules) |
| 183 | presentation-generale/les-modeles-de-documents.md | 1470 | modèle de document (personnalisation : sections, tags, conditions, mise en forme) | indetermine | documents, automatisation | oui | non | oui | oui | non | reference_configuration |
| 184 | presentation-generale/les-modeles-de-documents/courriers-de-relance-un-modele-particulier.md | 32 | indetermine (page en construction, aucun contenu exploitable) | indetermine | — | non | non | non | non | non | autre (page en cours d'élaboration) |
| 185 | presentation-generale/les-onglets.md | 192 | onglets (multitâche, navigation) | indetermine | — | oui | non | non | oui | non | procedure |
| 186 | presentation-generale/progbox-archivage-de-documents.md | 638 | ProGBox (archivage de documents, stockage cloud intégré) | indetermine | documents, paiement, automatisation | oui | non | non | oui | non | definitionnel (avec procédure associée, ton partiellement promotionnel) |

## Résultat mécanique final

Tous les totaux ci-dessous sont calculés par script (parsing des 186 lignes
du tableau, aucun comptage manuel).

- **Documents traités : 186/186** (périmètre gelé intégralement couvert,
  numérotation 1→186 continue, 0 doublon, 0 trou). Vérification
  supplémentaire : l'ensemble des 186 chemins réellement codés est
  strictement identique, comparaison mécanique par ensembles, à l'ensemble
  des 186 chemins du périmètre gelé annoncé avant lecture de contenu — 0
  écart, 0 substitution.
- **Mots (somme mécanique de `longueur_mots`) : 57 978.** Identique au
  volume de calibrage mécanique annoncé avant lecture (voir Incidents et
  corrections pour l'explication de cette égalité).
- **Durée : CONTEXTE_SESSION_NON_MESURABLE** (aucune estimation produite),
  comme pour les deux productions précédentes.
- **Incidents : aucun.** 0 correction mécanique de vocabulaire fermé
  nécessaire (contre 1 pour Costructor, 0 pour Axonaut) — seule la
  correction de méthode documentée plus haut a été journalisée.

### moment_parcours (186 documents)

| valeur | n | % |
|---|---:|---:|
| indetermine | 100 | 53,8 % |
| facturation | 34 | 18,3 % |
| devis | 30 | 16,1 % |
| chantier-intervention | 14 | 7,5 % |
| achat | 8 | 4,3 % |
| **somme** | **186** | **100,0 %** |

**Taux `indetermine` : 53,8 % (100/186).** Se situe entre Costructor
(51,1 %) et Axonaut (66,4 %) — cohérent avec un outil très centré métier
BTP (comme Costructor : chantiers, devis, factures de situation) mais
comportant, comme Axonaut, un volume important de paramétrage transverse
(comptabilité, utilisateurs, modèles de documents, options). Aucune valeur
`demande` (vue au pilote, ligne 27) n'est réapparue sur ce corpus non plus
— absence cohérente avec les deux productions précédentes, pas une
dérive.

### capacites_transverses (occurrences, un document peut en porter jusqu'à 3)

| capacité | n |
|---|---:|
| documents | 67 |
| conformite_reglementaire | 60 |
| paiement | 54 |
| automatisation | 29 |
| integrations | 29 |
| roles | 29 |
| catalogue | 27 |
| planning | 23 |
| communication | 15 |
| recherche | 15 |
| securite_compte | 9 |
| mobile | 8 |
| permissions | 6 |
| support_editeur | 4 |
| notifications | 3 |
| gestion_stock | 1 |

`conformite_reglementaire` domine nettement plus que sur Costructor et
Axonaut : ProGBat documente une quantité inhabituelle d'obligations
légales françaises spécifiques au BTP (mentions obligatoires du devis,
gestion des déchets, retenue de garantie, TVA sur marge/encaissement,
numérotation chronologique, attestation anti-fraude TVA, CGV, assurance
décennale) — cohérent avec son positionnement éditorial très orienté
conformité. Aucune capacité nouvelle hors du vocabulaire déjà observé aux
pilotes/Costructor/Axonaut n'a été introduite.

### genre_documentaire (186 documents, racines regroupées)

| valeur | n | % |
|---|---:|---:|
| procedure | 69 | 37,1 % |
| reference_configuration | 34 | 18,3 % |
| definitionnel | 33 | 17,7 % |
| autre | 28 | 15,1 % |
| politique_legale | 14 | 7,5 % |
| faq_depannage | 4 | 2,2 % |
| marketing_dans_aide | 4 | 2,2 % |
| **somme** | **186** | **100,0 %** |

`politique_legale` (14, 7,5 %) est nettement plus fréquent que sur
Costructor (2/94, 2,1 %) ou Axonaut (2/119, 1,7 %) — confirme, sur un
troisième corpus, le constat de densité réglementaire déjà noté ci-dessus.

**`autre` est très supérieur aux deux corpus précédents** (28/186, 15,1 %,
contre 1/94 pour Costructor et 3/119 pour Axonaut) — décomposition
mécanique de ces 28 documents :
- **14** sont des stubs de navigation purs (fil d'Ariane/menu applicatif
  sans corps d'article), concentrés dans
  `le-menu-principal/bibliotheque/elements/*`, une sous-arborescence
  entière — absence de contenu confirmée dans la source elle-même, pas un
  défaut de collecte (voir « Cas que LIGHT représente mal » ci-dessous).
- **9** portent explicitement la mention « Cette documentation est en
  cours d'élaboration... » ou « Cet article est en cours de rédaction... »
  — un défaut de complétude assumé par l'éditeur, pas un problème de
  collecte.
- **5** sont des pages-carrefour multi-sujets (hub renvoyant vers
  plusieurs sous-articles), comme observé sur les deux corpus précédents.

### contenu_observable (5 booléens, 186 documents, oui/non/inconnu)

| champ | oui | non | inconnu |
|---|---:|---:|---:|
| procedure | 117 | 69 | 0 |
| transition_objet | 40 | 146 | 0 |
| regle_ou_condition | 84 | 102 | 0 |
| contrainte_ou_limite | 63 | 123 | 0 |
| exception_ou_correction | 10 | 176 | 0 |

Aucune valeur `inconnu` n'a été nécessaire sur ce lot : les 186 documents
étaient chacun suffisamment explicites pour trancher les 5 booléens de
manière factuelle — y compris les 23 documents à contenu quasi nul
(stubs et pages en construction), pour lesquels les 5 valeurs sont
honnêtement `non` (absence démontrée par le contenu réel, pas incertitude).

`exception_ou_correction` (10/186, 5,4 %) se situe entre Costructor
(8/94, 8,5 %) et Axonaut (47/119, 39,5 %) — cohérent avec un éditorial
ProGBat qui documente peu de scénarios de dépannage explicites hors de
quelques pages dédiées (`la-panicroom.md`, service de recouvrement).

### Cas que LIGHT représente mal

**Limitations déjà connues (confirmées sur ce troisième corpus) :**

- **Pages-hub multi-sujets et contenu très dense.** Comme sur Costructor
  et Axonaut, plusieurs pages agrègent des sujets hétérogènes ou une
  densité réglementaire très élevée sous un seul `objet_principal` forcé
  à l'unique — notamment `pour-bien-demarrer/parametrage/parametres-de-
  lentreprise/autres-parametres.md` (1174 mots : signature, validité de
  devis, décimales, conditions de règlement en cascade, acomptes, texte
  légal de pénalités de retard) et `presentation-generale/les-modeles-de-
  documents.md` (1470 mots : sections, tags, méta-tags, logique
  conditionnelle complète). `objet_principal` capture le sujet dominant
  mais aplatit la richesse structurelle interne.
- **Contenu réglementaire non spécifique au logiciel.** Comme chez
  Costructor et Axonaut, plusieurs documents sont davantage des fiches de
  conformité juridique françaises (mentions obligatoires du devis, loi
  anti-fraude TVA, décret gestion des déchets, obligations d'assurance)
  qu'une documentation produit au sens strict — codés `politique_legale`
  sans que le schéma ne distingue « obligation légale externe » de
  « fonctionnalité propriétaire ».

**Nouveaux cas observés sur ce corpus (non rencontrés, ou rencontrés
autrement, sur Costructor et Axonaut) :**

- **Sous-arborescence sans contenu documentaire (`bibliotheque/
  elements/`).** 5 des 6 pages de cette rubrique (fournitures, location,
  main d'œuvre, outillage, sous-traitance) ne contiennent aucun corps
  d'article, seulement un titre et une coquille de navigation ; la
  6e (`elements.md`) porte l'encart « documentation en cours
  d'élaboration ». Vérification menée le 2026-09-08 : plusieurs modes
  d'observation concordent — l'export `.md` natif de la plateforme
  GitBook, l'export agrégé `llms-full.txt` de GitBook, et notre collecte
  locale du 06/09 — pour montrer que ces pages n'ont pas de corps
  documentaire substantiel dans la source elle-même. Ce n'est donc pas un
  défaut de collecte démontré. Ce n'est pas non plus la preuve d'une
  absence fonctionnelle dans ProGBat : des articles voisins
  (`gestion-des-ouvrages.md`, `les-ouvrages-composes.md`) mentionnent les
  fournitures, la main d'œuvre, la location, la sous-traitance et
  l'outillage comme des composants réels du chiffrage. LIGHT documente
  correctement ces pages (`autre`, 5 booléens `non`) mais ne peut pas, par
  construction, distinguer une absence de rédaction d'une absence de
  fonctionnalité — la limite reste réelle, seule son interprétation était
  erronée.
- **Documentation en reconstruction assumée.** 9 documents affichent
  littéralement « en cours de rédaction/d'élaboration » — signal explicite
  que ProGBat retravaille sa documentation (probablement suite à une
  refonte de version, cf. mentions « pour l'adapter à votre nouvelle
  version de ProGBat » sur plusieurs stubs `depenses/*`). Aucun des deux
  corpus précédents ne présentait ce marqueur de transition éditoriale à
  cette échelle.
- **Contenu dupliqué entre deux articles.** `pour-bien-demarrer/demarrer-
  avec-progbat/importer-une-bibliotheque/importer-mes-fournitures.md`
  (ligne 149) et `.../importer-un-tarif-fournisseur.md` (ligne 151)
  partagent un texte quasi identique malgré des titres différents — même
  phénomène de redondance éditoriale que les 3 articles factures dupliqués
  chez Axonaut, ici confirmé sur un troisième éditeur indépendant.
- **`genre_documentaire: faq_depannage` appliqué à du contenu para-
  juridique tiers.** Les deux occurrences de recouvrement de créances
  (lignes 114, 115) mêlent conditions contractuelles d'un service tiers
  (Caarl) et FAQ de dépannage — un cas limite entre `politique_legale` et
  `faq_depannage` qu'aucune règle du protocole ne tranche explicitement ;
  codé `faq_depannage` car la forme dominante (questions/réponses) l'a
  emporté sur le fond (obligations contractuelles).
- **Motif « facturation électronique / plateforme agréée » confirmé une
  6e fois.** Après InterFast, OpenFire, Costructor et Batikko (pilote),
  ProGBat documente lui aussi ce motif à trois reprises indépendantes
  (`conformite/la-facture-electronique.md`,
  `depenses/factures-dachat/facture-electronique-recue-par-pdp.md`,
  `les-options/.../mes-outils-comptables-en-option.md`) — confirmation
  supplémentaire, non anticipée par la sélection, que ce sujet traverse
  la quasi-totalité de l'industrie du logiciel de gestion BTP française.

