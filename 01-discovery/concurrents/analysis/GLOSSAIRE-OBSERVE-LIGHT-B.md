# GLOSSAIRE OBSERVÉ LIGHT — VERSION B

Exécution indépendante. `GLOSSAIRE-OBSERVE-LIGHT.md` (première expérience) n'a été ni
lu, ni consulté, ni utilisé comme référence pour construire ce document. Aucune
comparaison entre les deux versions n'est faite ici.

## 1. Périmètre

### Productions LIGHT canoniques identifiées

Recherche mécanique dans `01-discovery/concurrents/analysis/` de tous les fichiers
`light-*.md` et du pilote historique. 12 productions retenues comme canoniques :

| Fichier | Corpus / concurrent | Lignes LIGHT exploitables | Particularité de structure |
|---|---|---:|---|
| `pilote-light-corpus-inedit.md` | multi-concurrents (7 corpus, voir détail ci-dessous) | 40 | `chemin_relatif` absent du tableau de sortie propre (dette documentée SCHEMA-LIGHT.md §11) ; reconstitué ici par jointure mécanique sur `#` avec le tableau « Échantillon gelé » du même fichier. `longueur_mots` en estimation visuelle, non `wc -w`. |
| `light-costructor-help.md` | `costructor_help` | 94 | Format standard. |
| `light-axonaut-help.md` | `axonaut_help` | 119 | Format standard. |
| `light-progbat-help.md` | `progbat_help` | 186 | Format standard. |
| `light-batikko-help.md` | `batikko_help` | 11 | Format standard, plus petit corpus. |
| `light-openfire-zendesk.md` | `openfire_zendesk` | 119 | Tableau interrompu par des lignes vides internes (séparation visuelle par rubrique) ; une seule table logique, reconstituée mécaniquement. |
| `light-openfire-odoo.md` | `openfire_odoo` | 212 | Même particularité de lignes vides internes que `openfire_zendesk`. |
| `light-vertuoza-help.md` | `vertuoza_help` | 431 | Même particularité de lignes vides internes (plus fréquente, ~27 coupures). |
| `light-inter-fast-help.md` | `inter_fast_help` | 217 | Format standard. |
| `light-sellsy-help.md` | `sellsy_help` | 454 | Format standard, plus gros corpus dédié. |
| `light-extrabat-help.md` | `extrabat_help` | 347 | Convention propre à cette production : `objet_principal` codé littéralement `— (commentaire)` pour les pages sans contenu substantiel (37 lignes concernées). Effet sur le calcul de racine mécanique, voir §3. |
| `light-obat-help.md` | `obat_help` | 274 | Tableau sans barre verticale de bordure gauche ; noms de colonnes et `chemin_relatif` entourés de backticks. Mêmes 12 colonnes, même ordre. |

**Nombre de productions : 12.**
**Nombre total de lignes LIGHT exploitées : 2504.**

Détail du pilote par corpus (jointure Échantillon gelé ↔ Sorties LIGHT, sur `#`) :
`openfire_zendesk` 8, `costructor_help` 8, `sellsy_help` 8, `axonaut_help` 8,
`progbat_help` 4, `batikko_help` 3, `openfire_odoo` 1 — total 40.

Total de lignes par corpus, pilote + production dédiée cumulés :

| corpus_id | pilote | production dédiée | total |
|---|---:|---:|---:|
| costructor_help | 8 | 94 | 102 |
| axonaut_help | 8 | 119 | 127 |
| progbat_help | 4 | 186 | 190 |
| batikko_help | 3 | 11 | 14 |
| openfire_zendesk | 8 | 119 | 127 |
| openfire_odoo | 1 | 212 | 213 |
| vertuoza_help | 0 | 431 | 431 |
| inter_fast_help | 0 | 217 | 217 |
| sellsy_help | 8 | 454 | 462 |
| extrabat_help | 0 | 347 | 347 |
| obat_help | 0 | 274 | 274 |
| **Total** | **40** | **2464** | **2504** |

11 corpus distincts au total (le pilote ne porte sur aucun corpus qui lui soit propre :
ses 7 corpus recoupent des productions dédiées existantes).

### Production explicitement exclue de ce périmètre

`light-h3-validation-positifs.md` (6 lignes, InterFast/Vertuoza) n'est **pas** retenue
comme production canonique. Le fichier s'auto-qualifie explicitement dès sa première
ligne : *« Périmètre expérimental, pas un corpus canonique »*, et précise que son objet
unique est de tester la sensibilité du filtre `regle_ou_condition = oui` sur des cas
connus, pas de cartographier InterFast ou Vertuoza. Cette exclusion n'est pas une
interprétation de cette mission : elle est écrite dans le fichier source lui-même.
Écartée en conséquence, sans lecture de son tableau au-delà de cette vérification de
statut.

### Lignes LIGHT vs documents sources uniques

Chaque production dédiée documente explicitement l'exclusion des documents déjà
observés par le pilote (ou, pour Sellsy et InterFast, par des instruments antérieurs à
LIGHT — Pilote A, Analysis C — exclusion relevant du choix de chaque production, pas
d'une règle SCHEMA-LIGHT rétroactive). Sur cette base déclarée par chaque fichier
source (non re-vérifiée ici par relecture des corpus, hors périmètre de cette
mission) : **2504 lignes LIGHT correspondent à 2504 documents distincts**, sans
recoupement connu entre productions. Cette mission n'a pas cherché à re-vérifier
mécaniquement cette absence de recoupement au niveau des chemins de fichiers
eux-mêmes (voir §9 Limites).

## 2. Méthode

- **Valeur exacte (Niveau A)** : `objet_principal` extrait tel quel, sans aucune
  correction, simplification, singularisation, lemmatisation ni fusion.
- **Racine mécanique (Niveau B)** : calculée à partir de la valeur exacte par
  l'algorithme suivant, appliqué sans exception :
  1. repérer les positions de la première parenthèse ouvrante `(`, du premier `/`
     et du premier tiret cadratin `—` (Unicode U+2014, distinct du trait d'union
     simple `-`) ;
  2. couper au séparateur dont la position est la plus faible ;
  3. si aucun séparateur n'est trouvé, garder la chaîne entière ;
  4. supprimer les espaces de début/fin ;
  5. passer en minuscules ;
  6. réduire les suites d'espaces à un seul espace ;
  7. retirer la ponctuation terminale résiduelle (`. , ; : ! ? -`).
- **Distinction mécanique / sémantique** : la racine est une clé de regroupement
  purement textuelle. Elle ne présuppose et ne produit aucune identité fonctionnelle.
  Deux racines identiques peuvent recouvrir deux objets différents ; deux racines
  différentes peuvent recouvrir le même objet sous deux formulations. Cette
  distinction structure les §5 à §7.

## 3. Contrôles mécaniques

- Lignes identifiées au §1 : 2504.
- Lignes effectivement extraites (script Python, parsing des tableaux Markdown des
  12 productions) : 2504. **Aucun écart.**
- Valeurs exactes distinctes : **2411**.
- Racines mécaniques distinctes : **1861**.
- Cohérence : 2504 valeurs exactes se réduisent à 2411 valeurs distinctes (93 valeurs
  répétées à l'identique), qui se réduisent à leur tour à 1861 racines (davantage de
  regroupement, l'algorithme de coupe absorbant les qualificatifs entre parenthèses et
  après `/`).

### Anomalie journalisée : racine vide

37 lignes (toutes dans `light-extrabat-help.md`) ont `objet_principal` littéralement
codé `— (commentaire explicatif)` — c'est-à-dire que le tiret cadratin est le
**premier caractère** de la valeur. L'algorithme de coupe (§2) trouve alors le
séparateur `—` en position 0 et produit une racine vide (`""`). Ce n'est pas un bug du
script d'extraction : c'est le résultat mécanique honnête de l'algorithme appliqué à
une convention d'écriture propre à cette production (utiliser `—` comme valeur
`objet_principal` pour signaler « pas de contenu substantiel »). Ces 37 lignes sont
comptabilisées dans l'inventaire sous une racine notée `∅` (vide), distincte des autres
racines, décrite au §4. Aucune valeur exacte n'a été modifiée pour éviter cette
anomalie.

Aucune autre anomalie de parsing détectée (0 ligne orpheline, 0 colonne décalée après
vérification manuelle des 12 en-têtes contre le schéma canonique à 12 colonnes,
`chemin_relatif` du pilote reconstitué sans écart — les 40 identifiants `#` des deux
tableaux du pilote coïncident exactement).

## 4. Inventaire brut des racines

### 4.A — Racines par fréquence décroissante (occurrences ≥ 3)

104 racines sur 1861 apparaissent au moins 3 fois. Elles concentrent une part
minoritaire mais significative du corpus (voir aussi §4.C pour l'autre extrême — les
racines mono-corpus, très majoritaires en nombre).

| racine | occurrences | # corpus | corpus concernés | valeurs exactes représentatives (jusqu'à 5, avec compte) | chemins représentatifs (jusqu'à 5) | moments observés |
|---|---:|---:|---|---|---|---|
| ∅ (vide — placeholder « — ») | 37 | 1 | extrabat_help | — (page sans contenu substantif, résidu de gabarit de navigation) (17); — (page sans contenu substantif, question sans réponse) (6); — (billet éditorial/motivationnel, sans contenu instructif) (1); — (page d'accueil du centre d'aide, flux d'articles hétérogène) (1); — (billet éditorial sur la conduite du changement, sans contenu produit) (1) | astuce-le-raccourci-de-recherche.md; cloturer-la-caisse.md; comment-bien-parametrer-son-navigateur-internet-firefox.md; comment-creer-sa-signature-le-logiciel-extrabat.md; comment-donner-les-droits-utilisateur-consulter-etou-modifier.md | indetermine=35; chantier-intervention=1; devis=1 |
| rapport | 36 | 1 | sellsy_help | rapport (analyse factures / consommation client) (1); rapport (analyse tickets support) (1); rapport (CA global par collaborateur) (1); rapport (CA global) (1); rapport (comparatif performances annuelles) (1) | rapports-et-pilotage/rapport-analyse-des-factures-et-consommation.md; rapports-et-pilotage/rapport-analyse-des-tickets-de-support.md; rapports-et-pilotage/rapport-ca-global-par-collaborateur.md; rapports-et-pilotage/rapport-ca-global.md; rapports-et-pilotage/rapport-comparatif-des-performances-annuelles.md | indetermine=23; facturation=8; devis=4; achat=1 |
| indetermine | 33 | 3 | axonaut_help, openfire_odoo, progbat_help | indetermine (page sans contenu exploitable, navigation seule) (14); indetermine (page en construction, aucun contenu exploitable) (9); indetermine (page d'accueil, fragment HTML incomplet) (2); indetermine (plateforme eLearning, aucun cours publié) (2); indetermine (page-carrefour, chantiers/personnel) (1) | le-menu-principal/bibliotheque/elements.md; le-menu-principal/bibliotheque/elements/fournitures.md; le-menu-principal/bibliotheque/elements/location.md; le-menu-principal/bibliotheque/elements/main-doeuvre.md; le-menu-principal/bibliotheque/elements/outillage.md | indetermine=33 |
| facture | 24 | 8 | axonaut_help, costructor_help, extrabat_help, inter_fast_help, openfire_odoo, openfire_zendesk, progbat_help, sellsy_help | facture (avec ou sans devis) (1); facture (création, langues, adresses communes, CGV, images — hub multi-sujets) (1); facture (liste, recherche, filtres) (1); facture (annulation/modification via avoir) (1); facture (création : acompte, travaux, avancement/situation, directe, avoir, copie) (1) | ventes/comment-creer-une-facture-ndrp7y.md; gerez-vos-factures/creer-une-facture-avec-axonaut-2.md; le-menu-principal/devis-factures/factures.md; le-menu-principal/devis-factures/factures/annuler-ou-modifier-une-facture.md; le-menu-principal/devis-factures/factures/creer-une-facture.md | facturation=23; indetermine=1 |
| tableau de bord | 24 | 3 | extrabat_help, progbat_help, sellsy_help | tableau de bord (opportunités) (2); tableau de bord (tâches) (2); tableau de bord (personnalisation : vignettes, lignes) (1); tableau de bord (événements) (1); tableau de bord (achats et marges) (1) | pour-bien-demarrer/demarrer-avec-progbat/personnaliser-le-tableau-de-bord.md; app-mobile-sellsy-crm/app-sellsy-crm-tableau-de-bord-mes-evenements.md; app-mobile-sellsy-crm/app-sellsy-crm-tableau-de-bord-opportunites.md; app-mobile-sellsy-crm/app-sellsy-crm-tableau-de-bord-taches.md; configuration-du-compte/tableau-de-bord-achats-et-marges.md | indetermine=24 |
| devis | 20 | 7 | axonaut_help, extrabat_help, inter_fast_help, obat_help, openfire_zendesk, progbat_help, sellsy_help | devis (création, IA, duplication, téléchargement PDF) (1); devis/factures (présentation générale, fonctionnalités : chiffrage, signature, facturation, avenants) (1); devis (copie, révision, avenant — actions selon statut) (1); devis (liste, statuts : brouillon/finalisé/envoyé/accepté/refusé) (1); devis (création, 4 méthodes) (1) | gerez-vos-devis/creer-un-devis-avec-axonaut.md; le-menu-principal/devis-factures.md; le-menu-principal/devis-factures/copie-revision-avenant.md; le-menu-principal/devis-factures/devis.md; le-menu-principal/devis-factures/devis/creer-un-devis.md | devis=19; indetermine=1 |
| facturation électronique | 13 | 7 | batikko_help, costructor_help, inter_fast_help, obat_help, openfire_zendesk, progbat_help, sellsy_help | facturation électronique / plateforme agréée (3); facturation électronique / transfert comptable (1); facturation électronique / plateforme agréée (réception, PDP fournisseurs) (1); facturation électronique (émission factures clients) (1); facturation électronique (réception factures fournisseurs) (1) | debuter-sur-costructor/comment-transferer-les-factures-electroniques-vers-une-adresse-mail-comptable-wizy4e.md; conformite/la-facture-electronique.md; le-menu-principal/depenses/factures-dachat/facture-electronique-recue-par-pdp.md; configurer-openfire/activer-et-parametrer-l-emission-de-vos-factures-clients.md; configurer-openfire/activer-et-parametrer-la-reception-des-factures-fournisseurs.md | facturation=10; indetermine=2; achat=1 |
| automatisation | 13 | 1 | sellsy_help | automatisation (suivi continu documents, tâche) (1); automatisation (suivi continu opportunités, tâche) (1); automatisation (opportunité ↔ facture liée) (1); automatisation (opportunité ↔ tâche terminée) (1); automatisation (configuration générale, gestion) (1) | sellsy-automatisations/assurer-un-suivi-continu-de-vos-documents.md; sellsy-automatisations/assurer-un-suivi-continu-de-vos-opportunites.md; sellsy-automatisations/avancer-automatiquement-vos-opportunites-avec-les-factures-liees.md; sellsy-automatisations/avancer-vos-opportunites-lorsqu-une-tache-est-terminee.md; sellsy-automatisations/configurer-et-activer-une-automatisation-dans-sellsy.md | indetermine=9; devis=3; facturation=1 |
| signature électronique | 12 | 6 | axonaut_help, extrabat_help, obat_help, openfire_odoo, progbat_help, sellsy_help | signature électronique (Oodrive Sign) (2); signature électronique (jesignexpert, lettre de mission) (1); signature électronique (Yousign, eIDAS, crédit par signature) (1); signature électronique (1); signature électronique (devis, envoi, vérification SMS) (1) | gerez-vos-devis/comment-connecter-jesignexpert-a-axonaut.md; gerez-vos-devis/signature-electronique-des-devis-documents-yousign.md; conformite/la-signature-electronique.md; les-options/pourquoi-des-options/signature-electronique.md; knowsystem/configuration-262.md | indetermine=6; devis=5; facturation=1 |
| fiche client | 10 | 5 | axonaut_help, extrabat_help, inter_fast_help, progbat_help, sellsy_help | fiche client (échanges, prospect→client, fusion de doublons) (1); fiche client (informations, adresses, contacts, conditions de règlement, activité, ProGBox) (1); fiche client (sections, documents, interventions, devis/factures, équipements) (1); fiche client (présentation complète) (1); fiche client (informations clés, résumé IA) (1) | optimisez-gestion-commerciale/la-fiche-client-axonaut.md; le-menu-principal/contacts/clients/la-fiche-client.md; inter-fast/outils/comprendre-la-fiche-d-un-client.md; repertoire/societes-presentation-de-la-fiche-client.md; repertoire/societes-suivre-les-informations-cles-d-une-fiche-client.md | indetermine=9; demande=1 |
| rendez-vous | 8 | 2 | extrabat_help, openfire_zendesk | rendez-vous (présentation des éléments) (1); rendez-vous (planification, mobile) (1); rendez-vous (depuis fiche contact) (1); rendez-vous (depuis planning) (1); rendez-vous (réalisation, équipement/rapport/facturation) (1) | guides-videos/decouvrir-la-presentation-d-un-rendez-vous.md; guides-videos/planifier-un-rendez-vous-sur-le-mobile.md; guides-videos/prendre-rendez-vous-depuis-le-contact.md; guides-videos/prendre-rendez-vous-depuis-le-planning.md; guides-videos/realiser-un-rendez-vous-sur-le-mobile.md | chantier-intervention=7; indetermine=1 |
| facture d'acompte | 7 | 5 | costructor_help, extrabat_help, obat_help, openfire_zendesk, sellsy_help | facture d'acompte (commande divisée) (3); facture d'acompte (transition depuis devis) (1); facture d'acompte (génération depuis commande) (1); facture d'acompte (avance, comptabilité légale) (1); facture d'acompte (1) | ventes/comment-creer-une-facture-dacompte-fllvsr.md; utiliser-openfire/facturer-un-acompte.md; documents-de-vente/utiliser-les-factures-d-acompte.md; creer-une-facture-dacompte.md; gestion-commerciale/page/7.md | facturation=7 |
| client | 7 | 4 | batikko_help, costructor_help, extrabat_help, progbat_help | client / prospect (fiche contact) (1); client (fichier clients/prospects, relation, rentabilité) (1); client (création, depuis devis ou liste) (1); client (fiche CRM, KYC, scoring) (1); client/prospect (création via agenda) (1) | ventes/comment-creer-un-client-prospect-ue8wib.md; le-menu-principal/contacts/clients.md; le-menu-principal/contacts/clients/creer-un-client.md; guides/clients-crm.md; creer-un-client-via-lagenda.md | indetermine=5; devis=1; demande=1 |
| commande fournisseur | 7 | 4 | axonaut_help, extrabat_help, openfire_zendesk, sellsy_help | commande fournisseur (bon de commande PDF) (1); commande fournisseur (demande de prix) (1); commande fournisseur (transformation en document de vente) (1); commande fournisseur (reliquat) (1); commande fournisseur (protocole EDI) (1) | commandes-clients-fournisseurs/creer-une-commande-fournisseur.md; utiliser-openfire/creer-une-demande-de-prix-ou-une-commande-fournisseur.md; module-achats/transformer-une-commande-fournisseur-en-document-de-vente.md; annuler-un-reliquat-de-commande-fournisseur.md; comment-envoyer-sa-commande-fournisseur-via-le-protocole-edi.md | achat=7 |
| règlement | 7 | 4 | costructor_help, extrabat_help, openfire_zendesk, sellsy_help | règlement (paiement sur facture) (1); règlement (suppression sur facture) (1); règlement (paiement, lettrage) (1); règlement (ajout, factures) (1); règlement (suppression, document lié) (1) | ventes/comment-enregistrer-un-reglement-sur-une-facture-j8zd6o.md; ventes/comment-supprimer-un-reglement-sur-une-facture-1jal4w6.md; utiliser-openfire/enregistrer-un-reglement-client-ou-fournisseur.md; paiements/ajouter-un-reglement-a-une-ou-plusieurs-factures.md; paiements/supprimer-un-reglement-lie-a-un-document.md | facturation=7 |
| modification | 7 | 3 | axonaut_help, costructor_help, obat_help | modification/suppression de facture (encadrement légal anti-fraude TVA) (1); modification/suppression de dépense (cas bloquants : payée, réceptionnée, droits) (1); modification/suppression de devis (statuts, cas bloquants) (1); modification/suppression de facture (paiement, avoir, droits — contenu recoupant #80/#84) (1); modification/suppression de produit (désactivation, archives, droits) (1) | ventes/comment-modifier-supprimer-une-facture-1ex0kq5.md; creez-depenses-facilement/modifier-supprimer-une-depense.md; gerez-vos-devis/modifier-un-devis.md; gerez-vos-factures/comment-modifier-une-facture.md; gerez-vos-produits/modifier-un-produit.md | indetermine=3; facturation=2; achat=1; devis=1 |
| produit | 7 | 3 | axonaut_help, openfire_zendesk, sellsy_help | produit/service (ajout, IA, vente en ligne, code-barres, traduction — hub multi-sujets) (1); produit (fiche produit, complet) (1); produit (import en masse, tarifs) (1); produit / service (catalogue) (1); produit / service (définition catalogue) (1) | gerez-vos-produits/comment-ajouter-des-produits-services-dans-axonaut.md; utiliser-openfire/creer-un-produit.md; utiliser-openfire/importer-mes-produits-avec-open-import.md; catalogue-produits-et-services/ajouter-des-produits-et-services-a-mon-catalogue.md; catalogue-produits-et-services/difference-entre-produits-et-services.md | indetermine=6; achat=1 |
| synchronisation email | 7 | 3 | axonaut_help, inter_fast_help, obat_help | synchronisation email (Google Workspace, routage) (1); synchronisation email (OVH, règle de redirection) (1); synchronisation email (Gandi, redirection) (1); synchronisation email (Microsoft 365, règle de flux) (1); synchronisation email (définition + multi-fournisseurs) (1) | centralisez-gestion-emails-courriers/comment-synchroniser-ses-emails-google-workspace-avec-axonaut.md; centralisez-gestion-emails-courriers/emails-synchroniser-ovh-avec-axonaut.md; centralisez-gestion-emails-courriers/synchronisation-des-mails-avec-gandi.md; centralisez-gestion-emails-courriers/synchronisation-des-mails-avec-microsoft365-office-365.md; centralisez-gestion-emails-courriers/synchroniser-ses-emails-ca-veut-dire-quoi-2.md | indetermine=7 |
| champ personnalisé | 7 | 2 | axonaut_help, sellsy_help | champ personnalisé (types, zones d'affichage, vs catégories) (1); champ personnalisé (affichage liste) (1); champ personnalisé (affichage document de vente) (1); champ personnalisé (création) (1); champ personnalisé (édition en masse) (1) | optimisez-gestion-commerciale/les-champs-personnalises-dans-axonaut-cest-quoi.md; gestion-des-donnees/afficher-les-champs-personnalises-dans-une-liste.md; gestion-des-donnees/afficher-un-champ-personnalise-sur-un-document-de-vente.md; gestion-des-donnees/creer-des-champs-personnalises.md; gestion-des-donnees/editer-les-valeurs-des-champs-personnalises-en-masse.md | indetermine=6; facturation=1 |
| contact | 7 | 2 | openfire_zendesk, sellsy_help | contact (création, mobile) (1); contact (mise à jour, mobile) (1); contact (fiche client/fournisseur, complet) (1); contact (fusion de doublons) (1); contact (import en masse via Excel/OpenImport) (1) | guides-videos/creer-un-contact-sur-mobile.md; guides-videos/mettre-a-jour-un-contact-sur-mobile.md; utiliser-openfire/creer-un-contact.md; utiliser-openfire/fusionner-vos-contacts.md; utiliser-openfire/importer-des-contacts-a-partir-d-un-fichier-excel.md | indetermine=7 |
| mot de passe | 7 | 2 | extrabat_help, inter_fast_help | mot de passe (oubli, réinitialisation) (3); mot de passe (réinitialisation) (1); mot de passe (changement/réinitialisation) (1); mot de passe (nouvelle mesure de sécurité, critères) (1); mot de passe (sécurisation, conseils) (1) | inter-fast/equipe/reinitialiser-mon-mot-de-passe.md; comment-changer-votre-mot-de-passe.md; mot-de-passe-oublie.md; mots-de-passe-nouvelle-mesure-de-securite.md; securisez-vos-mots-de-passe.md | indetermine=7 |
| synchronisation agenda | 7 | 2 | extrabat_help, sellsy_help | synchronisation agenda (CalDAV/mobile) (2); synchronisation agenda (CalDAV, smartphone Apple) (2); synchronisation agenda / contacts (Google) (1); synchronisation agenda / contacts (Office 365 / Outlook) (1); synchronisation agenda (forcer) (1) | configuration-du-compte/synchronisation-des-agendas-et-contacts-avec-google.md; configuration-du-compte/synchronisation-des-agendas-et-contacts-avec-office-365-outlook.md; agenda-2.md; forcer-la-synchronisation-de-mes-rendez-vous-a-venir.md; parametrage.md | indetermine=7 |
| article | 7 | 1 | extrabat_help | article (duplication) (1); article (mise à jour depuis pièce commerciale) (1); article (mise à jour via paramètres) (1); article (fraîcheur de mise à jour, code couleur) (1); article (création) (1) | comment-dupliquer-article.md; comment-mettre-a-jour-un-article-a-partir-dune-piece-commerciale.md; comment-mettre-a-jour-un-article-par-les-parametres.md; comment-savoir-si-article-jour-periode-de-moins-dun.md; creer-un-nouvel-article.md | indetermine=6; devis=1 |
| application mobile | 6 | 6 | costructor_help, inter_fast_help, obat_help, openfire_zendesk, progbat_help, sellsy_help | application mobile (PWA) (1); application mobile (accès utilisateur / accès compagnon) (1); application mobile (téléchargement, connexion) (1); application mobile (vue d'ensemble, fonctionnalités et workflow terrain) (1); application mobile (présentation fonctionnalités) (1) | debuter-sur-costructor/telecharger-lapplication-costructor-sur-mobile-s25hdg.md; application-mobile.md; guides-videos/telecharger-l-application-openfire-et-se-connecter.md; inter-fast/application-mobile/utiliser-notre-application-mobile.md; app-mobile-sellsy-crm/tester-sellsy-crm-sur-votre-mobile.md | indetermine=5; chantier-intervention=1 |
| taux de tva | 6 | 5 | axonaut_help, costructor_help, extrabat_help, openfire_zendesk, sellsy_help | taux de TVA (modification sur document) (1); taux de TVA (ajout, TVA intracommunautaire) (1); taux de TVA (prestation, mobile) (1); taux de TVA (1); taux de TVA (actifs / inactifs) (1) | ventes/comment-modifier-le-taux-de-tva-dun-document-y36yd8.md; gerez-vos-factures/ajouter-des-taux-de-tva.md; guides-videos/modifier-le-taux-de-tva-d-une-prestation-sur-mobile.md; catalogue-produits-et-services/ajouter-un-taux-de-tva.md; facturation-electronique/comprendre-les-taux-de-tva-actifs-et-inactifs.md | indetermine=4; facturation=2 |
| abonnement | 6 | 4 | axonaut_help, costructor_help, obat_help, sellsy_help | abonnement (souscription initiale) (1); abonnement (formules, renouvellement, factures, frais tiers) (1); abonnement (facturation récurrente) (1); abonnement / choix de pack (1); abonnement / choix de pack (micro-entreprise) (1) | abonnement/comment-sabonner-a-costructor-vxkaie.md; configurer-votre-compte/abonnement-axonaut-on-vous-explique-tout.md; documents-de-vente/creer-un-abonnement.md; entreprise-eurl/sarl/sas-comment-s-abonner-c3-a0-obat-et-choisir-son-pack.md; micro-entreprise/auto-entrepreneur-comment-s-abonner-c3-a0-obat-et-choisir-son-pack.md | indetermine=5; facturation=1 |
| rapprochement bancaire | 6 | 4 | axonaut_help, costructor_help, openfire_zendesk, sellsy_help | rapprochement bancaire / transaction (1); rapprochement bancaire (connexion, réconciliation, DSP2, instabilité) (1); rapprochement bancaire (comptes d'attente, lettrage) (1); rapprochement bancaire (lettrage manuel) (1); rapprochement bancaire (accès, privilèges) (1) | gestion-dentreprise/comment-justifier-une-transaction-bancaire-7y52fe.md; etat-tresorerie-temps-reel/rapprochement-bancaire-comment-ca-marche.md; configurer-openfire/configurez-vos-regles-de-rapprochement-bancaire.md; utiliser-openfire/realisez-vos-rapprochements-bancaires.md; suivi-financier/donner-a-mes-collaborateurs-un-acces-au-module-rapprochement-bancaire.md | indetermine=4; facturation=2 |
| opportunité | 6 | 3 | openfire_odoo, openfire_zendesk, sellsy_help | opportunité (CRM, pipeline) (1); opportunité (analyse pipeline, tunnels de conversion) (1); opportunité (pipeline) (1); opportunité (suivi, définition) (1); opportunité (suivi via tâches) (1) | utiliser-openfire/creer-une-opportunite.md; knowsystem/analyser-ses-opportunites-120.md; app-mobile-sellsy-crm/app-sellsy-crm-ajouter-une-opportunite.md; crm-et-prospection/introduction-suivi-des-opportunites.md; crm-et-prospection/suivre-mes-opportunites-en-utilisant-les-taches.md | indetermine=4; demande=2 |
| facture proforma | 5 | 5 | axonaut_help, costructor_help, extrabat_help, inter_fast_help, obat_help | facture proforma (2); facture proforma / devis en brouillon (filigrane) (1); facture proforma (devis/douane/financement, création depuis commande) (1); facture proforma (création, transformation en facture officielle) (1) | ventes/comment-imprimerenvoyer-une-facture-proforma-ou-un-devis-en-brouillon-yme5bk.md; gerez-vos-factures/facture-proforma.md; inter-fast/finances/creer-une-facture-proforma.md; comment-creer-une-facture-proforma.md; comment-faire-une-facture-proforma-avec-obat.md | devis=2; facturation=2; indetermine=1 |
| fiche fournisseur | 5 | 5 | axonaut_help, inter_fast_help, openfire_zendesk, progbat_help, sellsy_help | fiche fournisseur (échanges, commandes, fusion de doublons) (1); fiche fournisseur (informations, adresses, contacts, conditions de règlement, activité, ProGBox) (1); fiche fournisseur (règles d'import automatique de factures) (1); fiche fournisseur (informations, dépenses, commandes) (1); fiche fournisseur (présentation complète) (1) | optimisez-gestion-commerciale/la-fiche-fournisseur.md; le-menu-principal/contacts/fournisseurs/la-fiche-fournisseur.md; configurer-openfire/configurer-les-regles-d-import-de-facture-sur-la-fiche-fournisseur.md; inter-fast/outils/comprendre-la-fiche-d-un-fournisseur.md; repertoire/societes-presentation-de-la-fiche-fournisseur.md | achat=4; indetermine=1 |
| planning | 5 | 5 | batikko_help, obat_help, openfire_odoo, openfire_zendesk, progbat_help | planning (chantiers, phases, personnel) (1); planning (calendrier, Gantt, équipes) (1); planning (vues disponibles) (1); planning (vues : planning/calendrier/liste/carte, filtres) (1); planning (page de catégorie) (1) | le-menu-principal/chantiers-personnel/planning.md; guides/planning.md; guides-videos/decouvrir-les-differentes-vues-du-planning.md; knowsystem/affichage-du-planning-79.md; planning.md | chantier-intervention=5 |
| chantier | 5 | 4 | batikko_help, inter_fast_help, obat_help, progbat_help | chantier (concept, distinction chantier/marché de travaux, statuts) (1); chantier (création, 3 méthodes) (1); chantier (fiche de synthèse, suivi, app mobile) (1); chantier (page de catégorie) (1); chantier (dossier digital) (1) | le-menu-principal/chantiers-personnel/chantiers.md; le-menu-principal/chantiers-personnel/chantiers/creer-un-chantier.md; inter-fast/application-mobile/suivre-ses-chantiers-app-mobile.md; chantier.md; guides/chantiers.md | chantier-intervention=5 |
| fournisseur | 5 | 4 | batikko_help, costructor_help, extrabat_help, progbat_help | fournisseur (fichier fournisseurs, achats, livraisons, factures d'achat) (1); fournisseur (création, depuis commande/facture ou liste) (1); fournisseur (base fournisseurs, OCR, recherche GPS) (1); fournisseur (ajout à un article) (1); fournisseur / sous-traitant (1) | le-menu-principal/contacts/fournisseurs.md; le-menu-principal/contacts/fournisseurs/creer-un-fournisseur.md; guides/fournisseurs.md; rajouter-un-fournisseur-a-un-article.md; achats/comment-creer-un-fournisseur-sous-traitant-1cubnry.md | achat=4; indetermine=1 |
| compte bancaire | 5 | 3 | costructor_help, inter_fast_help, sellsy_help | compte bancaire (rapprochement) (1); compte bancaire (connexion Powens, DSP2, migration Ponto) (1); compte bancaire (dissociation, révocation) (1); compte bancaire (synchronisation) (1); compte bancaire (connexion, banques spécifiques) (1) | debuter-sur-costructor/comment-connecter-son-compte-bancaire-xupyjb.md; inter-fast/finances/connecter-mon-compte-bancaire.md; inter-fast/finances/dissocier-mon-compte-bancaire.md; suivi-financier/connecter-mon-compte-bancaire-en-synchronisation.md; suivi-financier/connecter-un-compte-bancaire-societe-generale-credit-agricole-caisse-d-epargne.md | indetermine=5 |
| ouvrage | 5 | 3 | extrabat_help, obat_help, progbat_help | ouvrage (bibliothèque, prestation vendue au client) (1); ouvrage (création, mise à jour, gestion depuis devis et bibliothèque) (1); ouvrage (suppression) (1); ouvrage (renommage) (1); ouvrage (fourniture/main d'œuvre) sur devis/factures (1) | le-menu-principal/bibliotheque/ouvrages.md; le-menu-principal/bibliotheque/ouvrages/gestion-des-ouvrages.md; comment-supprimer-un-ouvrage.md; renommer-un-ouvrage.md; comment-ajouter-un-ouvrage-sur-vos-devis/factures.md | devis=3; indetermine=2 |
| dépense | 5 | 2 | axonaut_help, inter_fast_help | dépense (OCR, devise, récurrence) (1); dépense (ajout via app mobile, OCR justificatifs) (1); dépense (ajout, app web) (1); dépense (modification, allocation chantier) (1); dépense / paiement (1) | creez-depenses-facilement/ajouter-une-depense.md; inter-fast/application-mobile/ajouter-une-depense-app-mobile.md; inter-fast/finances/ajouter-une-depense-app-web.md; inter-fast/finances/modifier-une-depense.md; creez-depenses-facilement/ajouter-un-paiement-sur-une-depense.md | achat=4; indetermine=1 |
| société | 5 | 2 | axonaut_help, sellsy_help | société/contact (fiche, catégorisation auto, unicité particulier) (1); société (visualisation carte, mobile) (1); société (enrichissement via annuaire) (1); société (vue carte) (1); société (suppression / archivage) (1) | optimisez-gestion-commerciale/comment-creer-une-societe-dans-axonaut.md; app-mobile-sellsy-crm/app-sellsy-crm-visualiser-les-societes-sur-une-carte.md; repertoire/enrichir-les-donnees-d-une-societe-existante.md; repertoire/repertoire-voir-les-societes-sur-une-carte.md; repertoire/societes-supprimer-ou-archiver-des-societes.md | indetermine=5 |
| configuration smtp | 5 | 1 | extrabat_help | configuration SMTP (Yahoo) (1); configuration SMTP (personnalisé) (1); configuration SMTP (Brevo) (1); configuration SMTP (boîte mail personnalisée) (1); configuration SMTP (Gmail) (1) | configuration-smtp-extrabat-avec-yahoo.md; configuration-smtp-extrabat.md; e-mailing.md; je-veux-envoyer-des-mails-a-partir-dextrabat-mais-avec-ma-boite-mail.md; parametrer-son-smtp-extrabat-avec-son-compte-gmail.md | indetermine=5 |
| ia | 5 | 1 | sellsy_help | IA (édition commentaires / notes) (1); IA (campagnes emailing, édition texte) (1); IA (modèles email intelligents) (1); IA (rédaction / édition emails) (1); IA (résumé fiche client) (1) | sellsy-ia/editeur-ia-ameliorer-la-prise-de-notes-avec-sellsy-ia.md; sellsy-ia/editeur-ia-ameliorez-vos-campagnes-emailing-avec-sellsy-ia.md; sellsy-ia/modeles-d-emails-ia-generer-des-messages-cibles-avec-sellsy-ia.md; sellsy-ia/redacteur-et-editeur-ia-rediger-des-emails-avec-sellsy-ia.md; sellsy-ia/resumes-client-ia-resumer-une-fiche-client-en-un-clic-avec-sellsy-ia.md | indetermine=5 |
| time tracking | 5 | 1 | sellsy_help | time tracking (ticket support) (1); time tracking (fonctionnement) (1); time tracking (saisie hebdomadaire) (1); time tracking (saisie rapide) (1); time tracking (suivi heures collaborateurs) (1) | crm-et-prospection/ajouter-une-entree-de-time-tracking-sur-un-ticket-de-support.md; crm-et-prospection/fonctionnement-et-utilisation-du-timetracking.md; crm-et-prospection/saisie-hebdomadaire-des-heures-sur-timetracking.md; crm-et-prospection/saisie-rapide-d-un-temps.md; crm-et-prospection/suivre-les-heures-effectuees-par-mes-collaborateurs-grace-au-time-tracking.md | indetermine=5 |
| avoir | 4 | 4 | axonaut_help, extrabat_help, openfire_zendesk, sellsy_help | avoir (global/partiel/fournisseur, suppression encadrée de facture) (1); avoir (partiel / intégral / modification) (1); avoir (facturation) (1); avoir (création, transformation facture) (1) | gerez-vos-factures/comment-faire-un-avoir-sur-axonaut.md; utiliser-openfire/generer-un-avoir.md; documents-de-vente/creer-et-gerer-des-avoirs.md; je-veux-faire-un-avoir.md | facturation=4 |
| gestion de stock | 4 | 4 | axonaut_help, costructor_help, openfire_odoo, progbat_help | gestion de stock / produit (1); gestion de stock (fabrication, bons de livraison, réception, location) (1); gestion de stock (configuration générale, routes, stratégies) (1); gestion de stock (absence assumée) (1) | debuter-sur-costructor/comment-gerer-ses-stocks-cb6503.md; gerez-stock-temps-reel/comment-ca-marche-la-gestion-de-stock.md; knowsystem/configurations-250.md; presentation-generale/gestion-de-stocks.md | indetermine=4 |
| agenda | 4 | 3 | costructor_help, extrabat_help, sellsy_help | agenda (synchronisation Google Agenda) (1); agenda (mode d'affichage) (1); agenda (usage) (1); agenda (modification RDV, sélection utilisateur) (1) | debuter-sur-costructor/comment-synchroniser-lagenda-costructor-avec-google-agenda-7f0syd.md; configuration-du-compte/gerer-les-modes-d-affichage-de-mon-agenda.md; configuration-du-compte/utiliser-l-agenda-sellsy.md; je-ne-peux-pas-modifier-mon-agenda.md | indetermine=3; chantier-intervention=1 |
| cgv | 4 | 3 | costructor_help, inter_fast_help, sellsy_help | CGV (conditions générales de vente) (1); CGV (paramétrage, import, rédaction) (1); CGV (pièce jointe email) (1); CGV (document de vente) (1) | debuter-sur-costructor/inserer-mes-cgv-conditions-generales-de-ventes-vk2gwi.md; inter-fast/mon-entreprise/ajouter-mes-conditions-generales-de-vente-cgv.md; configuration-du-compte/ajouter-des-cgv-aux-pieces-jointes-des-emails.md; documents-de-vente/ajouter-mes-cgv-a-la-fin-d-un-document-de-vente.md | indetermine=3; facturation=1 |
| paiement | 4 | 3 | extrabat_help, inter_fast_help, openfire_odoo | paiement (annulation, remboursement, modification) (1); paiement (rapprochement avec facture) (1); paiement (consignation, suppression, cas particuliers) (1); paiement (lettrage) (1) | knowsystem/annuler-rembourser-ou-modifier-un-paiement-163.md; knowsystem/associer-paiements-et-factures-162.md; inter-fast/finances/consigner-un-paiement.md; comment-effectuer-un-paiement-en-passant-par-le-lettrage.md | facturation=4 |
| commentaires | 4 | 2 | inter_fast_help, sellsy_help | commentaires (collaboration interne/externe, mentions) (1); commentaires (import) (1); commentaires (export) (1); commentaires (usage, collaboration) (1) | inter-fast/application-web/collaborer-avec-les-commentaires.md; gestion-des-donnees/importer-des-commentaires.md; repertoire/commentaires-comment-les-exporter.md; repertoire/commentaires-comment-les-utiliser.md | indetermine=3; chantier-intervention=1 |
| connexion | 4 | 2 | openfire_zendesk, sellsy_help | connexion (application mobile) (1); connexion (application web, base test/production) (1); connexion (compte) (1); connexion (compatibilité navigateur/certificat) (1) | bien-debuter/se-connecter-a-l-application-mobile.md; bien-debuter/se-connecter-a-l-application-web.md; conseils-d-utilisation/connexion-a-mon-compte-sellsy.md; conseils-d-utilisation/connexion-non-chiffree-au-site-sellsy.md | indetermine=4 |
| intégration comptable | 4 | 2 | batikko_help, costructor_help | intégration comptable (Pennylane via Chift) (1); intégration comptable (ACD i-Suite Expert) (1); intégration comptable (Pennylane) (1); intégration comptable / synchronisation (facture → écriture) (1) | debuter-sur-costructor/comment-connecter-costructor-a-pennylane-14mfqxx.md; guides/connexion-acd.md; guides/connexion-pennylane.md; guides/connexion-inqom.md | facturation=2; indetermine=2 |
| remise en banque | 4 | 2 | extrabat_help, sellsy_help | remise en banque (règlements multiples) (1); remise en banque (annulation) (1); remise en banque (simplifiée) (1); remise en banque (espèces) (1) | suivi-financier/enregistrer-une-remise-en-banque-de-plusieurs-reglements.md; annuler-une-remise-en-banque.md; comment-effectuer-une-remise-en-banque-simplifiee.md; faire-remise-banque-despeces.md | facturation=4 |
| code comptable | 4 | 1 | sellsy_help | code comptable (plan comptable) (1); code comptable (remises) (1); code comptable (catalogue, produit) (1); code comptable (ligne de document) (1) | suivi-financier/ajouter-des-codes-comptables-au-plan-comptable.md; suivi-financier/gerer-les-codes-comptables-des-remises.md; suivi-financier/renseigner-les-codes-comptables-dans-le-catalogue.md; suivi-financier/renseigner-les-codes-comptables-dans-un-document.md | indetermine=3; facturation=1 |
| mandat pa | 4 | 1 | sellsy_help | mandat PA (émission + réception, facturation électronique) (1); mandat PA (émission, facturation électronique) (1); mandat PA / KYC (vérification identité) (1); mandat PA / KYC (vérification identité, procédure) (1) | facturation-electronique/completer-le-mandat-d-emission-et-de-reception-sur-la-plateforme-sellsy-pa.md; facturation-electronique/completer-le-mandat-d-emission-sur-la-plateforme-sellsy-pa.md; facturation-electronique/comprendre-le-mandat-pa-et-la-verification-d-identite.md; facturation-electronique/mandat-pa-effectuer-votre-verification-d-identite.md | indetermine=4 |
| modèle de courrier | 4 | 1 | extrabat_help | modèle de courrier (création) (3); modèle de courrier (import Word/OpenOffice, marqueurs) (1) | creer-modele-de-courrier.md; nouvelle-fonctionnalite-modele-courrier.md; tag/courrier.md; tag/creer-un-modele-de-courrier.md | indetermine=4 |
| moteur de recherche | 4 | 1 | extrabat_help | moteur de recherche (optimisation, critères) (1); moteur de recherche (personnalisation nom/prénom) (1); moteur de recherche (champs disponibles) (1); moteur de recherche (recherche précise, filtre articles) (1) | moteur-de-recherche-plus-rapide.md; personnalisez-votre-recherche-dans-le-moteur-de-recherche.md; rechercher-dans-le-logiciel.md; rechercher-plus-precis.md | indetermine=4 |
| photo | 4 | 1 | extrabat_help | photo (prise depuis rendez-vous, porte-documents) (3); photo (annotation, géolocalisation, Extrabat Today) (1) | espace-client.md; je-veux-geolocaliser-ma-photo-et-annoter-ma-photo.md; je-veux-prendre-une-photo-avec-extrabat-today.md; tablette-smartphone.md | chantier-intervention=4 |
| pièce commerciale | 4 | 1 | extrabat_help | pièce commerciale (jointe à un SAV) (1); pièce commerciale (duplication) (1); pièce commerciale (envoi par mail) (1); pièce commerciale (réaffectation à un autre client) (1) | comment-joindre-une-piece-commerciale-a-un-sav.md; dupliquer-devis-commande-facture.md; envoyer-une-piece-commerciale-exemple-facture-devis-relance-etc-par-mail-au-client.md; veux-affecter-devis-facture-a-client.md | indetermine=2; chantier-intervention=1; facturation=1 |
| smart tag | 4 | 1 | sellsy_help | smart tag (fiche client) (1); smart tag (filtrage) (1); smart tag (introduction) (1); smart tag (tickets support) (1) | gestion-des-donnees/ajouter-ou-supprimer-un-smart-tag.md; gestion-des-donnees/filtrer-mes-donnees-grace-aux-smart-tags.md; gestion-des-donnees/introduction-utilisation-des-smart-tags.md; module-support/utiliser-les-smart-tags-pour-trier-les-tickets-de-support.md | indetermine=4 |
| achats | 3 | 3 | axonaut_help, obat_help, sellsy_help | achats (fournisseurs, dépenses, commandes, notes de frais, indemnités km) (1); achats (cycle : commande → livraison → facture) (1); achats/bons de commande/rentabilité (page de catégorie) (1) | creez-depenses-facilement/comment-ca-marche-achats.md; module-achats/gerer-mes-achats.md; la-gestion-des-achats-bons-de-commande-et-de-la-rentabilit-c3-a9-sur-obat.md | achat=3 |
| bibliothèque | 3 | 3 | extrabat_help, obat_help, progbat_help | bibliothèque (ouvrages vs éléments — structure du catalogue) (1); bibliothèque (signature utilisateur, recherche transversale — agrégat) (1); bibliothèque (page de catégorie) (1) | le-menu-principal/bibliotheque.md; tag/bibliotheque.md; biblioth-c3-a8que.md | indetermine=3 |
| calcul de marge | 3 | 3 | costructor_help, obat_help, sellsy_help | calcul de marge (option devis brouillon) (1); calcul de marge (achats) (1); calcul de marge (devis) (1) | ventes/comment-activer-le-calcul-des-marges-vv5czm.md; module-achats/fonctionnement-du-calcul-de-marge.md; comment-utiliser-le-calcul-de-marge-sur-obat.md | devis=2; indetermine=1 |
| contacts | 3 | 3 | obat_help, progbat_help, sellsy_help | contacts (catégories : clients, prospects, fournisseurs, sous-traitants) (1); contacts (import liste existante) (1); contacts (page de catégorie) (1) | le-menu-principal/contacts.md; repertoire/repertoire-importer-votre-liste-de-contacts-existants.md; contacts.md | indetermine=3 |
| facture d'abonnement | 3 | 3 | costructor_help, inter_fast_help, sellsy_help | facture d'abonnement (1); facture d'abonnement (téléchargement) (1); facture d'abonnement (gestion) (1) | abonnement/telecharger-les-factures-dabonnement-costructor-1cmafv1.md; inter-fast/mon-entreprise/telecharger-ma-facture-d-abonnement.md; documents-de-vente/gestion-des-factures-d-abonnement.md | facturation=2; indetermine=1 |
| facture d'achat | 3 | 3 | costructor_help, progbat_help, sellsy_help | facture d'achat (moyens d'intégration : saisie, photo, PDP) (1); facture d'achat (devise étrangère) (1); facture d'achat / export (1) | le-menu-principal/depenses/factures-dachat.md; module-achats/saisir-une-facture-d-achat-dans-une-autre-devise.md; imports-exports/comment-exporter-mes-factures-dachats-1ewcnjr.md | achat=3 |
| factures | 3 | 3 | inter_fast_help, obat_help, sellsy_help | factures (tableau, filtres, colonnes) (1); factures / avoirs fournisseurs (import OCR) (1); factures (page de catégorie) (1) | inter-fast/finances/comprendre-le-tableau-des-factures.md; gestion-des-donnees/importer-des-factures-et-avoirs-fournisseurs-dans-sellsy.md; factures.md | facturation=2; indetermine=1 |
| marge | 3 | 3 | costructor_help, progbat_help, sellsy_help | marge / prix (ajustement en masse sur devis) (1); marge (concept de marge brute, calcul, mise à jour de la bibliothèque) (1); marge (catalogue, coûts d'achat) (1) | ventes/comment-ajuster-la-marge-ou-les-prix-dun-devis-1pvn0w4.md; pour-bien-demarrer/parametrage/parametres-de-lentreprise/marges.md; module-achats/calculer-une-marge-grace-au-catalogue.md | indetermine=2; devis=1 |
| modèle de document | 3 | 3 | extrabat_help, progbat_help, sellsy_help | modèle de document (personnalisation : sections, tags, conditions, mise en forme) (1); modèle de document (devis / facture) (1); modèle de document (duplication) (1) | presentation-generale/les-modeles-de-documents.md; documents-de-vente/creer-un-modele-de-document.md; comment-dupliquer-un-modele-de-document.md | indetermine=2; facturation=1 |
| moyen de paiement | 3 | 3 | costructor_help, obat_help, sellsy_help | moyen de paiement (abonnement) (2); moyen de paiement (correction, rapprochement bancaire) (1) | abonnement/comment-mettre-a-jour-son-moyen-de-paiement-6rwou1.md; suivi-financier/modifier-le-moyen-de-paiement-pour-un-rapprochement-bancaire.md; ajouter-ou-modifier-un-moyen-de-paiement-sur-obat.md | indetermine=3 |
| plan comptable | 3 | 3 | axonaut_help, costructor_help, openfire_zendesk | plan comptable / comptes auxiliaires (1); plan comptable (saisie manuelle ou import massif) (1); plan comptable (comptes généraux, tiers) (1) | debuter-sur-costructor/comment-parametrer-le-plan-comptable-et-les-comptes-auxiliaires-8bld86.md; gerez-votre-comptabilite/saisir-ou-importer-mon-plan-comptable-dans-axonaut.md; configurer-openfire/plan-comptable-general-et-auxiliaire.md | indetermine=3 |
| utilisateur | 3 | 3 | axonaut_help, extrabat_help, progbat_help | utilisateur (ajout/suppression/réactivation, message d'erreur email) (1); utilisateur (création, droits par défaut : administrateur/utilisateur/expert-comptable) (1); utilisateur (ajout) (1) | configurer-votre-compte/ajouter-un-utilisateur-dans-axonaut.md; pour-bien-demarrer/parametrage/utilisateurs/creer-modifier-supprimer-un-utilisateur.md; ajouter-un-utilisateur.md | indetermine=3 |
| campagne emailing | 3 | 2 | axonaut_help, sellsy_help | campagne emailing (ciblage, coût, opt-out, verrouillage post-envoi) (1); campagne emailing (template externe, opt-out, verrouillage post-envoi) (1); campagne emailing (IA, éditeur) (1) | creez-campagnes-marketing/creer-une-campagne-emailing-a-partir-dun-template-axonaut.md; creez-campagnes-marketing/creer-une-campagne-emailing-a-partir-dun-template-hors-axonaut.md; module-marketing/marketing-ameliorez-vos-campagnes-emailing-avec-sellsy-ia.md | indetermine=3 |
| gestion des stocks | 3 | 2 | inter_fast_help, obat_help | gestion des stocks (emplacements, produits, décrémentation, export) (1); gestion des stocks (page de catégorie) (1); gestion des stocks (bibliothèque) (1) | inter-fast/outils/gerer-les-stocks-app-web.md; gestion-des-stocks-simplifi-c3-a9s.md; la-gestion-des-stocks-sur-obat.md | indetermine=3 |
| géolocalisation | 3 | 2 | extrabat_help, openfire_zendesk | géolocalisation (carte fiche client) (2); géolocalisation (contacts) (1) | utiliser-openfire/geolocalisez-vos-prospects-et-clients.md; faire-apparaitre-la-carte-sur-la-page-daccueil-du-client.md; geolocalisation.md | indetermine=3 |
| import de devis | 3 | 2 | costructor_help, progbat_help | import de devis (DPGF/DQE, Excel/PDF) (1); import de devis/factures (migration depuis ancien système) (1); import de devis (fichier Excel/CSV, structuration automatique) (1) | imports-exports/comment-importer-un-devis-dpgf-dqe-excelpdf-1btrzbp.md; pour-bien-demarrer/demarrer-avec-progbat/importer-mes-devis-et-factures.md; pour-bien-demarrer/demarrer-avec-progbat/importer-mes-devis-et-factures/importer-mes-devis.md | devis=3 |
| planning chantier | 3 | 2 | extrabat_help, inter_fast_help | planning chantier (création/gestion, bonnes règles) (2); planning chantier (visualisation, planification, personnalisation affichage) (1) | inter-fast/operations/organiser-le-planning-chantier.md; les-bonnes-regles-afin-de-creer-gerer-son-planning-chantier.md; planning-chantier.md | chantier-intervention=3 |
| rapport d'intervention | 3 | 2 | extrabat_help, inter_fast_help | rapport d'intervention (remplissage, signature, génération, app mobile) (1); rapport d'intervention (Extrabat Today) (1); rapport d'intervention (technicien, mobile) (1) | inter-fast/application-mobile/remplir-un-rapport-d-intervention-app-mobile.md; je-veux-rentrer-un-rapport-dintervention-sur-extrabat-today.md; procedure-dun-rapport-dintervention-dun-technicien.md | chantier-intervention=3 |
| sav | 3 | 2 | extrabat_help, openfire_zendesk | SAV (dossier complet, cycle commercial/logistique/technique) (1); SAV (enregistrement) (1); SAV (enregistrement + planification RDV) (1) | utiliser-openfire/gerer-et-planifier-un-sav.md; comment-enregistrer-sav.md; enregistrer-un-nouveau-sav-et-caler-le-rendez-vous.md | chantier-intervention=3 |
| tarif centralisé | 3 | 2 | openfire_odoo, openfire_zendesk | tarif centralisé (accès catalogues fournisseurs) (1); tarif centralisé (accès, recherche d'articles) (1); tarif centralisé / catalogue (1) | utiliser-openfire/acceder-au-tarif-centralise.md; knowsystem/acceder-aux-tarifs-centralises-152.md; guides-videos/acceder-au-tarif-centralise.md | indetermine=2; devis=1 |
| trésorerie | 3 | 2 | axonaut_help, sellsy_help | trésorerie (intégration, prévisionnel) (1); trésorerie (pilotage financier) (1); trésorerie / pilotage financier (1) | module-tresorerie/sellsy-tresorerie-fonctionnement.md; module-tresorerie/debuter-avec-sellsy-tresorerie.md; etat-tresorerie-temps-reel/comment-ca-marche-le-menu-pilotage-tresorerie.md | indetermine=3 |
| tva | 3 | 2 | progbat_help, sellsy_help | TVA (taux, mentions légales) (1); TVA / réforme facturation électronique (exclusions, activités mixtes) (1); TVA (gestion, codes VATEX, facturation électronique) (1) | pour-bien-demarrer/parametrage/parametres-de-lentreprise/tva.md; facturation-electronique/activites-partiellement-soumises-a-la-tva-ou-exclues-de-la-reforme-francaise.md; facturation-electronique/gerer-sa-tva-dans-le-cadre-de-la-facturation-electronique.md | indetermine=3 |
| variantes de devis | 3 | 2 | inter_fast_help, obat_help | variantes de devis (création, envoi, acceptation) (1); variantes de devis (1); variantes de devis (stabilité des références) (1) | inter-fast/finances/creer-et-gerer-des-variantes-de-devis.md; les-variantes-de-devis-dans-obat.md; variantes-de-devis-vos-references-restent-stables-de-la-creation-a-la-facture.md | devis=3 |
| éditeur de style | 3 | 2 | extrabat_help, obat_help | éditeur de style (devis/commande/facture) (1); éditeur de style (masquage) (1); éditeur de style (mise en forme lignes) (1) | inserer-ligne-dans-devis-commande-facture.md; comment-cacher-l-c3-a9diteur-de-style-sur-le-devis.md; comment-utiliser-l-c3-a9diteur-de-style.md | indetermine=2; devis=1 |
| affaire | 3 | 1 | extrabat_help | affaire (bonnes pratiques, gestion) (1); affaire (création, association pièces commerciales) (1); affaire (synthèse rentabilité) (1) | bonnes-regles-afin-de-creer-affaire-de-gerer.md; creer-affaire-y-associer-pieces-commerciales-commande-bl-de-reception-facture-avoirs.md; synthese-rentabilite-dune-affaire.md | indetermine=3 |
| assistant devis vocal | 3 | 1 | obat_help | assistant devis vocal (option abonnement) (1); assistant devis vocal (page de catégorie) (1); assistant devis vocal (utilisation et tarification) (1) | activation-de-lassistant-devis-vocal.md; assistante-devis-vocal.md; dictez-vos-devis-depuis-obat-grace-a-notre-assistant-vocal.md | devis=3 |
| ca restant à facturer | 3 | 1 | extrabat_help | CA restant à facturer (rapport) (3) | ca-restant-a-facturer.md; comptabilite.md; statistiques.md | facturation=3 |
| catégorie tarifaire | 3 | 1 | sellsy_help | catégorie tarifaire (1); catégorie tarifaire (import, catalogue services) (1); catégorie tarifaire (import, catalogue produit) (1) | catalogue-produits-et-services/utiliser-les-categories-tarifaires.md; gestion-des-donnees/importer-les-categories-tarifaires-de-mon-catalogue-de-services.md; gestion-des-donnees/importer-les-categories-tarifaires-de-mon-catalogue-produit.md | indetermine=3 |
| demande d'intervention | 3 | 1 | openfire_zendesk | demande d'intervention (visibilité portail client) (1); demande d'intervention (SAV/entretien, portail client) (1); demande d'intervention (planification cartographique) (1) | configurer-openfire/gerer-l-affichage-et-le-partage-des-demandes-d-intervention-di-sur-le-portail-client.md; utiliser-openfire/consulter-et-suivre-ses-sav-et-entretien-sur-le-portail-client.md; utiliser-openfire/planification-des-demandes-d-intervention-depuis-la-carte.md | chantier-intervention=3 |
| document de vente | 3 | 1 | sellsy_help | document de vente (création : devis / facture) (1); document de vente (fusion) (1); document de vente (suppression) (1) | documents-de-vente/creer-une-facture-un-devis-un-document-de-vente.md; documents-de-vente/fusionner-des-documents.md; documents-de-vente/supprimer-un-document-de-vente.md | facturation=2; indetermine=1 |
| double authentification | 3 | 1 | sellsy_help | double authentification (administrateur) (1); double authentification (utilisateur) (1); double authentification (reconfiguration) (1) | conseils-d-utilisation/configurer-la-double-authentification-en-tant-qu-administrateur.md; conseils-d-utilisation/configurer-la-double-authentification-en-tant-qu-utilisateur.md; conseils-d-utilisation/reconfigurer-la-double-authentification-en-tant-qu-utilisateur-sellsy.md | indetermine=3 |
| fichier csv | 3 | 1 | sellsy_help | fichier CSV (ouverture, Excel) (1); fichier CSV (ouverture, Google Sheets) (1); fichier CSV (ouverture, OpenOffice) (1) | gestion-des-donnees/ouvrir-un-fichier-csv-avec-excel.md; gestion-des-donnees/ouvrir-un-fichier-csv-avec-google-sheets.md; gestion-des-donnees/ouvrir-un-fichier-csv-avec-open-office.md | indetermine=3 |
| import de template email | 3 | 1 | axonaut_help | import de template email (Mailchimp, conversion HTML) (1); import de template email (Sendinblue, code HTML) (1); import de template email (Mailjet, conversion HTML) (1) | creez-campagnes-marketing/campagne-emailing-importer-mon-template-mailchimp.md; creez-campagnes-marketing/campagne-emailing-importer-mon-template-sendinblue.md; creez-campagnes-marketing/utiliser-un-template-mailjet-pour-vos-campagnes-marketing-axonaut.md | indetermine=3 |
| impression | 3 | 1 | extrabat_help | impression (bug plugin Firefox, contournement) (2); impression (extension JS Print, autoriser accès) (1) | gestion-commerciale/impression.md; je-n-arrive-pas-a-imprimer-sous-firefox.md; si-vous-narrivez-pas-imprimer.md | indetermine=3 |
| informations société | 3 | 1 | sellsy_help | informations société (1); informations société (conformité facturation électronique) (1); informations société (modification, conformité) (1) | configuration-du-compte/parametrer-les-informations-de-ma-societe.md; facturation-electronique/completer-vos-informations-societe-dans-le-cadre-de-la-facturation-electronique.md; facturation-electronique/modifier-les-informations-societe-dans-le-cadre-de-la-facturation-electronique.md | indetermine=3 |
| interface de caisse | 3 | 1 | extrabat_help | interface de caisse (sélections produits) (2); interface de caisse (paramétrage, Extrabat Piscine) (1) | afficher-des-produits-sur-linterface-de-caisse.md; comment-parametrer-linterface-de-caisse.md; interface-de-caisse.md | indetermine=3 |
| intégration install bois | 3 | 1 | extrabat_help | intégration Install Bois (Extrabat Chauffage) (3) | assistance.md; connexion-install-bois.md; dossier-client.md | chantier-intervention=3 |
| inventaire | 3 | 1 | extrabat_help | inventaire (stock) (3) | faire-un-inventaire.md; tag/inventaire.md; tag/stock.md | indetermine=3 |
| ligne de devis | 3 | 1 | progbat_help | ligne de devis (création : titre, sous-titre, prestation, commentaire, saut de page) (1); ligne de devis (fonctionnalités avancées : dupliquer, déplacer, afficher composition) (1); ligne de devis (contenu détaillé : numérotation, désignation, quantité, unité, prix, TVA, types de vente) (1) | le-menu-principal/devis-factures/devis/les-lignes-du-devis/creer-une-ligne-de-devis.md; le-menu-principal/devis-factures/devis/les-lignes-du-devis/fonctionnalites-avancees.md; le-menu-principal/devis-factures/devis/les-lignes-du-devis/saisir-une-ligne-de-devis.md | devis=3 |
| modèle de message | 3 | 1 | extrabat_help | modèle de message (email personnalisé) (2); modèle de message (création/utilisation) (1) | comment-creer-un-modele-de-message.md; comment-utiliser-la-fonctionnalite-modele-de-message.md; video.md | indetermine=3 |
| paramétrage navigateur | 3 | 1 | extrabat_help | paramétrage navigateur (Firefox) (1); paramétrage navigateur (Firefox, onglets favoris) (1); paramétrage navigateur (Firefox, téléchargements) (1) | bien-parametrer-firefox.md; comment-lancer-toutes-mes-adresses-web-preferees-en-ouvrant-firefox.md; parametrer-firefox-pour-lenregistrement-des-fichiers.md | indetermine=3 |
| pipeline | 3 | 1 | sellsy_help | pipeline (affichage) (1); pipeline (création) (1); pipeline (vue) (1) | crm-et-prospection/afficher-ou-masquer-un-pipeline.md; crm-et-prospection/creer-un-pipeline.md; crm-et-prospection/utiliser-la-vue-pipeline.md | indetermine=3 |
| produit centralisé | 3 | 1 | openfire_zendesk | produit centralisé (import dans devis) (1); produit centralisé (import dans kit) (1); produit centralisé (utilisation dans devis/kits) (1) | guides-videos/importer-un-produit-centralise-dans-un-devis.md; guides-videos/importer-un-produit-centralise-dans-un-kit.md; utiliser-openfire/utiliser-les-produits-centralises-dans-mes-devis-et-dans-mes-kits.md | devis=2; indetermine=1 |
| raccourci écran d'accueil | 3 | 1 | extrabat_help | raccourci écran d'accueil (Android) (2); raccourci écran d'accueil (Apple) (1) | comment-creer-raccourci-sur-ma-tablette-android.md; mettre-raccourci-sur-sa-tablette-ou-smartphone-android.md; mettre-raccourci-sur-son-ecran-daccueil-sur-smartphone-ou-tablette-apple.md | indetermine=3 |
| rapport crm | 3 | 1 | sellsy_help | rapport CRM (activités) (1); rapport CRM (par collaborateur) (1); rapport CRM (par label) (1) | rapports-et-pilotage/rapport-rapport-d-activite-crm-par-activites.md; rapports-et-pilotage/rapport-rapport-d-activite-crm-par-collaborateur.md; rapports-et-pilotage/rapport-rapport-d-activite-crm-par-label.md | indetermine=3 |
| rapports d'intervention et signatures | 3 | 1 | extrabat_help | rapports d'intervention et signatures (Extrabat Today) (3) | les-rapports-dintervention-et-les-signatures-sur-extrabat-today.md; sav.md; services-contrats-dentretien.md | chantier-intervention=3 |
| tournée | 3 | 1 | openfire_zendesk | tournée (optimisation) (1); tournée (remplissage automatique) (1); tournée (optimisation, statuts) (1) | guides-videos/optimiser-et-re-organiser-les-tournees.md; utiliser-openfire/optimiser-et-remplir-automatiquement-une-tournee-depuis-le-planning.md; utiliser-openfire/optimiser-vos-tournees-d-intervention-en-cours.md | chantier-intervention=3 |
| widget | 3 | 1 | sellsy_help | widget (création, site web) (1); widget (installation site web) (1); widget (introduction) (1) | integrations-et-api/creer-et-personnaliser-mon-premier-widget.md; integrations-et-api/installer-un-widget-sellsy-sur-mon-site-web.md; integrations-et-api/introduction-widget-sellsy.md | indetermine=3 |

104 racines dans cette table (occurrences ≥ 3).

### 4.B — Racines par nombre de corpus/concurrents concernés (≥ 3 corpus)

43 racines apparaissent dans au moins 3 corpus distincts.

| racine | # corpus | occurrences | corpus concernés |
|---|---:|---:|---|
| facture | 8 | 24 | axonaut_help, costructor_help, extrabat_help, inter_fast_help, openfire_odoo, openfire_zendesk, progbat_help, sellsy_help |
| devis | 7 | 20 | axonaut_help, extrabat_help, inter_fast_help, obat_help, openfire_zendesk, progbat_help, sellsy_help |
| facturation électronique | 7 | 13 | batikko_help, costructor_help, inter_fast_help, obat_help, openfire_zendesk, progbat_help, sellsy_help |
| signature électronique | 6 | 12 | axonaut_help, extrabat_help, obat_help, openfire_odoo, progbat_help, sellsy_help |
| application mobile | 6 | 6 | costructor_help, inter_fast_help, obat_help, openfire_zendesk, progbat_help, sellsy_help |
| fiche client | 5 | 10 | axonaut_help, extrabat_help, inter_fast_help, progbat_help, sellsy_help |
| facture d'acompte | 5 | 7 | costructor_help, extrabat_help, obat_help, openfire_zendesk, sellsy_help |
| taux de tva | 5 | 6 | axonaut_help, costructor_help, extrabat_help, openfire_zendesk, sellsy_help |
| facture proforma | 5 | 5 | axonaut_help, costructor_help, extrabat_help, inter_fast_help, obat_help |
| fiche fournisseur | 5 | 5 | axonaut_help, inter_fast_help, openfire_zendesk, progbat_help, sellsy_help |
| planning | 5 | 5 | batikko_help, obat_help, openfire_odoo, openfire_zendesk, progbat_help |
| client | 4 | 7 | batikko_help, costructor_help, extrabat_help, progbat_help |
| commande fournisseur | 4 | 7 | axonaut_help, extrabat_help, openfire_zendesk, sellsy_help |
| règlement | 4 | 7 | costructor_help, extrabat_help, openfire_zendesk, sellsy_help |
| abonnement | 4 | 6 | axonaut_help, costructor_help, obat_help, sellsy_help |
| rapprochement bancaire | 4 | 6 | axonaut_help, costructor_help, openfire_zendesk, sellsy_help |
| chantier | 4 | 5 | batikko_help, inter_fast_help, obat_help, progbat_help |
| fournisseur | 4 | 5 | batikko_help, costructor_help, extrabat_help, progbat_help |
| avoir | 4 | 4 | axonaut_help, extrabat_help, openfire_zendesk, sellsy_help |
| gestion de stock | 4 | 4 | axonaut_help, costructor_help, openfire_odoo, progbat_help |
| indetermine | 3 | 33 | axonaut_help, openfire_odoo, progbat_help |
| tableau de bord | 3 | 24 | extrabat_help, progbat_help, sellsy_help |
| modification | 3 | 7 | axonaut_help, costructor_help, obat_help |
| produit | 3 | 7 | axonaut_help, openfire_zendesk, sellsy_help |
| synchronisation email | 3 | 7 | axonaut_help, inter_fast_help, obat_help |
| opportunité | 3 | 6 | openfire_odoo, openfire_zendesk, sellsy_help |
| compte bancaire | 3 | 5 | costructor_help, inter_fast_help, sellsy_help |
| ouvrage | 3 | 5 | extrabat_help, obat_help, progbat_help |
| agenda | 3 | 4 | costructor_help, extrabat_help, sellsy_help |
| cgv | 3 | 4 | costructor_help, inter_fast_help, sellsy_help |
| paiement | 3 | 4 | extrabat_help, inter_fast_help, openfire_odoo |
| achats | 3 | 3 | axonaut_help, obat_help, sellsy_help |
| bibliothèque | 3 | 3 | extrabat_help, obat_help, progbat_help |
| calcul de marge | 3 | 3 | costructor_help, obat_help, sellsy_help |
| contacts | 3 | 3 | obat_help, progbat_help, sellsy_help |
| facture d'abonnement | 3 | 3 | costructor_help, inter_fast_help, sellsy_help |
| facture d'achat | 3 | 3 | costructor_help, progbat_help, sellsy_help |
| factures | 3 | 3 | inter_fast_help, obat_help, sellsy_help |
| marge | 3 | 3 | costructor_help, progbat_help, sellsy_help |
| modèle de document | 3 | 3 | extrabat_help, progbat_help, sellsy_help |
| moyen de paiement | 3 | 3 | costructor_help, obat_help, sellsy_help |
| plan comptable | 3 | 3 | axonaut_help, costructor_help, openfire_zendesk |
| utilisateur | 3 | 3 | axonaut_help, extrabat_help, progbat_help |

### 4.C — Racines observées chez un seul corpus/concurrent

**1729 racines sur 1861 (93 %) n'apparaissent que dans un seul corpus.** Ce chiffre ne
doit pas être lu comme « 1729 spécificités éditeur » : LIGHT seul ne permet pas de
distinguer une racine mono-corpus qui reflète un vocabulaire produit réel d'une racine
mono-corpus qui reflète seulement le fait que ce corpus a été rédigé avec plus de
granularité, ou que ce sujet n'a simplement pas été documenté ailleurs. La liste
exhaustive des 1729 racines n'est pas reproduite ici (elle romprait la lisibilité du
document) ; la table ci-dessous en donne la répartition par corpus et un échantillon
représentatif de dix racines par corpus (triées par fréquence décroissante à
l'intérieur du corpus).

| corpus | # racines mono-corpus | exemples (jusqu'à 10, avec occurrences) |
|---|---:|---|
| vertuoza_help | 422 | calcul du montant d'une commande sous-traitant liée à une facture fournisseur (2), création d'une note de crédit (2), distinction reste à produire (2), dépannage d'ajout d'un compte chantier au planning d'intervention (2), facturation d'un avenant validé (2), récupération du lien de connexion à l'espace entreprise (2), absence de liaison automatique des rapports d'intervention aux factures groupées (1), absence de module trésorerie natif (1), absence de valeur légale probante de la signature électronique gratuite (1), activation de l'affichage des prix (1) |
| sellsy_help | 244 | rapport (36), automatisation (13), ia (5), time tracking (5), code comptable (4), mandat pa (4), smart tag (4), catégorie tarifaire (3), document de vente (3), double authentification (3) |
| obat_help | 220 | assistant devis vocal (3), conditions générales de vente (2), facturation électronique obligatoire (2), gestion des achats (2), marketplace (2), page partenaires (2), plus (2), postes libres ht (2), recherche devis (2), synchronisation calendrier (2) |
| openfire_odoo | 192 | connecteur d'achat (2), activation et configuration des listes de prix (1), activation et utilisation des pistes commerciales avant conversion en opportunités (1), affichage sans fil (1), amortissement (1), analyse des tunnels de conversion commerciale (1), analyse des ventes et devis via tableau croisé dynamique (1), analyse du chiffre d'affaires facturé (1), approvisionnement en exception (1), approvisionnement intersociété (1) |
| extrabat_help | 176 | ∅ (37), article (7), configuration smtp (5), modèle de courrier (4), moteur de recherche (4), photo (4), pièce commerciale (4), affaire (3), ca restant à facturer (3), impression (3) |
| inter_fast_help | 163 | bon de commande v1 (2), bsff (2), commandes v2 (2), qr codes (2), support client (2), académie vidéo (1), accompagnement 30 jours (1), agences (1), agenda externe (1), ajout clients (1) |
| progbat_help | 109 | ligne de devis (3), attestation de conformité (2), bibliothèque de prix tierce (2), compte de charge (2), accès rapides (1), adresses de l'entreprise (1), affectation de personnel (1), archives (1), assistance (1), assurances et cgv (1) |
| axonaut_help | 81 | import de template email (3), serveur smtp (2), acceptation (1), acompte et solde (1), automatisation commerciale (1), avance de trésorerie (1), avance immédiate (1), bénéficiaire effectif (1), carte de paiement (1), carte de paiement mobile (1) |
| costructor_help | 63 | feuille d'heures (2), acompte au prorata (1), agent ia conversationnel (1), ajustement ht (1), annulation de facture (1), application desktop (1), assurance décennale (1), authentification (1), bibliothèque collaborative d'ouvrages (1), bibliothèque de prix (1) |
| openfire_zendesk | 55 | demande d'intervention (3), produit centralisé (3), tournée (3), connecteur wizville (2), connecteurs d'achat (2), contrat (2), intervention (2), newsletter produit (2), taxe (2), équipement (2) |
| batikko_help | 4 | devis et facture (1), devis vocal (1), photo juridique (1), sécurité et conformité (1) |

Racines à occurrence unique (hapax), toutes corpus confondues : **1622**.

Constat mécanique notable : les corpus les plus volumineux (vertuoza_help 431 lignes,
sellsy_help 462 lignes cumulées) produisent aussi le plus de racines mono-corpus en
valeur absolue. Ce lien entre volume documentaire et nombre de racines uniques est une
observation mécanique, pas une conclusion sur la richesse fonctionnelle réelle de ces
produits — silence documentaire ≠ absence fonctionnelle, et volume documentaire ≠
richesse produit (cf. §9).

## 5. Regroupements sémantiques candidats

Ces regroupements sont des propositions, pas des décisions. Le rapprochement
lexical entre deux racines n'implique aucune identité fonctionnelle démontrée.

**FAMILLE_CANDIDATE : facture (documents)**
RACINES CONCERNÉES : `facture`, `factures`, `facture d'acompte`, `facture d'achat`,
`facture d'abonnement`, `facture proforma`.
VALEURS EXACTES ILLUSTRATIVES : « facture (liste, recherche, filtres) », « factures
(tableau, filtres, colonnes) », « facture d'acompte (commande divisée) », « facture
proforma (devis/douane/financement, création depuis commande) ».
CONCURRENTS/CORPUS CONCERNÉS : 8 corpus pour `facture` seul ; recouvrement large sur
l'ensemble de la famille.
JUSTIFICATION LINGUISTIQUE MINIMALE : toutes les racines partagent le lexème
« facture » comme tête nominale, avec un déterminant de sous-type (`d'acompte`,
`d'achat`, `d'abonnement`, `proforma`) ou une variation de nombre (`facture` /
`factures`).
STATUT : `CONCEPT_PROCHE_MAIS_DISTINCT` — `facture` et `factures` peuvent recouvrir un
même objet vu au singulier (document) ou au pluriel (vue liste) ; les sous-types
(`acompte`, `achat`, `abonnement`, `proforma`) sont documentés comme des variantes de
statut/usage distinctes plutôt que comme des synonymes du terme générique.

**FAMILLE_CANDIDATE : devis (documents et composants)**
RACINES CONCERNÉES : `devis`, `ligne de devis`, `variantes de devis`, `import de
devis`, `devis type / BPU` (valeur exacte observée, racine « devis type »).
VALEURS EXACTES ILLUSTRATIVES : « devis (liste, statuts : brouillon/finalisé/…) »,
« ligne de devis (contenu détaillé : numérotation, désignation, quantité…) »,
« variantes de devis (création, envoi, acceptation) ».
CONCURRENTS/CORPUS CONCERNÉS : 7 corpus pour `devis` ; `ligne de devis` concentrée sur
progbat_help ; `variantes de devis` sur inter_fast_help et obat_help.
JUSTIFICATION LINGUISTIQUE MINIMALE : lexème commun « devis », avec `ligne de devis`
marquant un niveau de granularité inférieur (composant du document) et `variantes de
devis` un état/déclinaison du document.
STATUT : `CONCEPT_PROCHE_MAIS_DISTINCT` — `ligne de devis` est un objet contenu (objet
et conteneur), pas un synonyme de `devis`.

**FAMILLE_CANDIDATE : facturation électronique / facture (généraliste)**
RACINES CONCERNÉES : `facturation électronique`, `mandat pa`, `facture` (sous-ensemble
des valeurs exactes liées à la conformité PDP/Chorus Pro).
VALEURS EXACTES ILLUSTRATIVES : « facturation électronique / plateforme agréée »,
« mandat PA (émission + réception, facturation électronique) ».
CONCURRENTS/CORPUS CONCERNÉS : 7 corpus pour `facturation électronique`.
JUSTIFICATION LINGUISTIQUE MINIMALE : `facturation électronique` partage le radical
« facture » avec la famille du même nom, mais désigne un processus réglementaire de
transmission (PDP, PPF, mandat), pas le document lui-même.
STATUT : `CONCEPT_PROCHE_MAIS_DISTINCT`.

**FAMILLE_CANDIDATE : client / tiers (fiche et entité)**
RACINES CONCERNÉES : `client`, `fiche client`, `société`, `contact`, `contacts`.
VALEURS EXACTES ILLUSTRATIVES : « client / prospect (fiche contact) », « fiche client
(informations, adresses, contacts…) », « société/contact (fiche, catégorisation
auto…) », « contact (fiche client/fournisseur, complet) ».
CONCURRENTS/CORPUS CONCERNÉS : `client` (4 corpus), `fiche client` (5 corpus),
`société` (2), `contact` (2), `contacts` (3).
JUSTIFICATION LINGUISTIQUE MINIMALE : les cinq racines désignent, à des degrés divers,
l'entité tierce (personne ou société) avec laquelle l'utilisateur du logiciel est en
relation commerciale ; plusieurs valeurs exactes elles-mêmes emploient un double libellé
(« client / prospect », « société/contact ») signalant une hésitation lexicale
source, pas seulement une hésitation d'extraction.
STATUT : `AMBIGU` — LIGHT ne permet pas de trancher si `client`/`fiche client` sont
strictement synonymes (objet et sa vue détaillée) ou si `contact`/`société` désignent
une entité distincte (personne physique vs personne morale) au sein du même tiers. Voir
§7.

**FAMILLE_CANDIDATE : fournisseur (fiche et entité)**
RACINES CONCERNÉES : `fournisseur`, `fiche fournisseur`, `commande fournisseur`.
VALEURS EXACTES ILLUSTRATIVES : « fournisseur (fichier fournisseurs, achats,
livraisons…) », « fiche fournisseur (informations, adresses, contacts…) »,
« commande fournisseur (bon de commande PDF) ».
CONCURRENTS/CORPUS CONCERNÉS : `fournisseur` (4 corpus), `fiche fournisseur` (5),
`commande fournisseur` (4).
JUSTIFICATION LINGUISTIQUE MINIMALE : structure identique à la famille client/tiers
(`fournisseur` / `fiche fournisseur`) ; `commande fournisseur` ajoute un objet
transactionnel distinct (bon de commande), pas une fiche.
STATUT : `SYNONYME_PROBABLE` pour `fournisseur` / `fiche fournisseur` (même logique
objet/vue détaillée que `client`/`fiche client`, par symétrie) ; `CONCEPT_PROCHE_MAIS_DISTINCT`
pour `commande fournisseur` (objet transactionnel séparé de la fiche).

**FAMILLE_CANDIDATE : paiement (règlement, encaissement)**
RACINES CONCERNÉES : `paiement`, `règlement`, `moyen de paiement`, `remise en banque`.
VALEURS EXACTES ILLUSTRATIVES : « paiement (rapprochement avec facture) »,
« règlement (paiement sur facture) », « moyen de paiement (abonnement) », « remise en
banque (règlements multiples) ».
CONCURRENTS/CORPUS CONCERNÉS : `paiement` (3 corpus), `règlement` (4), `moyen de
paiement` (3), `remise en banque` (2).
JUSTIFICATION LINGUISTIQUE MINIMALE : `règlement` apparaît systématiquement dans un
contexte d'encaissement sur facture existante ; `paiement` est employé plus largement
(y compris pour des dépenses, hors du strict encaissement client).
STATUT : `CONCEPT_PROCHE_MAIS_DISTINCT` — `règlement` semble un terme plus étroit
(l'acte d'encaissement sur une facture) que `paiement` (terme générique pouvant couvrir
aussi bien l'encaissement client que le règlement d'une dépense/achat) ; LIGHT seul ne
permet pas de confirmer cette hypothèse pour tous les corpus.

**FAMILLE_CANDIDATE : compte bancaire / rapprochement**
RACINES CONCERNÉES : `compte bancaire`, `rapprochement bancaire`, `trésorerie`.
VALEURS EXACTES ILLUSTRATIVES : « compte bancaire (connexion Powens, DSP2…) »,
« rapprochement bancaire (connexion, réconciliation, DSP2, instabilité) »,
« trésorerie (pilotage financier) ».
CONCURRENTS/CORPUS CONCERNÉS : `compte bancaire` (3 corpus), `rapprochement bancaire`
(4), `trésorerie` (2).
JUSTIFICATION LINGUISTIQUE MINIMALE : les trois racines partagent le champ lexical
bancaire/financier, sans lexème commun direct.
STATUT : `CONCEPT_PROCHE_MAIS_DISTINCT` — `compte bancaire` est l'objet (le compte
lui-même, sa connexion), `rapprochement bancaire` une action/processus appliqué à cet
objet (objet et une action, cf. consigne §5 de la mission), `trésorerie` un niveau de
pilotage agrégé distinct des deux premiers.

**FAMILLE_CANDIDATE : abonnement (souscription logicielle)**
RACINES CONCERNÉES : `abonnement`, `facture d'abonnement`, `moyen de paiement`.
VALEURS EXACTES ILLUSTRATIVES : « abonnement (souscription initiale) », « facture
d'abonnement (téléchargement) », « moyen de paiement (abonnement) ».
CONCURRENTS/CORPUS CONCERNÉS : `abonnement` (4 corpus), `facture d'abonnement` (3).
JUSTIFICATION LINGUISTIQUE MINIMALE : les trois racines partagent le même domaine
(souscription au logiciel lui-même, distinct des ventes du client final) et
apparaissent souvent dans les mêmes rubriques documentaires (« abonnement/... »).
STATUT : `CONCEPT_PROCHE_MAIS_DISTINCT` — objet (`abonnement`) et ses artefacts
associés (`facture d'abonnement`, `moyen de paiement`).

**FAMILLE_CANDIDATE : gestion de stock**
RACINES CONCERNÉES : `gestion de stock`, `gestion des stocks`, `inventaire`.
VALEURS EXACTES ILLUSTRATIVES : « gestion de stock (fabrication, bons de livraison,
réception, location) », « gestion des stocks (emplacements, produits,
décrémentation, export) », « inventaire (stock) ».
CONCURRENTS/CORPUS CONCERNÉS : `gestion de stock` (4 corpus), `gestion des stocks`
(2), `inventaire` (1, extrabat_help).
JUSTIFICATION LINGUISTIQUE MINIMALE : `gestion de stock` / `gestion des stocks` ne
diffèrent que par le nombre (singulier/pluriel) — variation orthographique de
rédacteur, pas de distinction de sens apparente sur les valeurs exactes lues.
`inventaire` désigne plus spécifiquement l'opération de comptage.
STATUT : `SYNONYME_PROBABLE` pour `gestion de stock` / `gestion des stocks` ;
`CONCEPT_PROCHE_MAIS_DISTINCT` pour `inventaire` (action spécifique) vis-à-vis des deux
premières (fonction générale).

**FAMILLE_CANDIDATE : chantier / affaire**
RACINES CONCERNÉES : `chantier`, `affaire`, `planning chantier`.
VALEURS EXACTES ILLUSTRATIVES : « chantier (concept, distinction chantier/marché de
travaux, statuts) », « affaire (création, association pièces commerciales) »,
« planning chantier (création/gestion, bonnes règles) ».
CONCURRENTS/CORPUS CONCERNÉS : `chantier` (4 corpus), `affaire` (1, extrabat_help
uniquement), `planning chantier` (2).
JUSTIFICATION LINGUISTIQUE MINIMALE : aucun lexème commun entre `chantier` et
`affaire` ; le rapprochement est purement fonctionnel (unité de suivi d'un projet
client), suggéré par une valeur exacte elle-même explicite : « chantier (concept,
**distinction chantier/marché de travaux**, statuts) » chez batikko_help.
STATUT : `AMBIGU` — la distinction chantier/affaire est nommée dans le mémorandum de
la mission (§7) comme une question ouverte ; `affaire` n'apparaît que chez un seul
corpus (extrabat_help), ce qui peut refléter une spécificité produit réelle ou
simplement le vocabulaire propre à cet éditeur. Voir §7.

**FAMILLE_CANDIDATE : intervention / rendez-vous / SAV**
RACINES CONCERNÉES : `rendez-vous`, `rapport d'intervention`, `demande
d'intervention`, `sav`.
VALEURS EXACTES ILLUSTRATIVES : « rendez-vous (réalisation, équipement/rapport/
facturation) », « rapport d'intervention (remplissage, signature, génération, app
mobile) », « demande d'intervention (SAV/entretien, portail client) », « SAV
(dossier complet, cycle commercial/logistique/technique) ».
CONCURRENTS/CORPUS CONCERNÉS : `rendez-vous` (2 corpus), `rapport d'intervention` (2),
`demande d'intervention` (1), `sav` (2).
JUSTIFICATION LINGUISTIQUE MINIMALE : les quatre racines partagent le champ lexical de
l'intervention terrain ; une valeur exacte lie explicitement `demande d'intervention`
et `SAV` (« demande d'intervention (SAV/entretien, portail client) »).
STATUT : `AMBIGU` — LIGHT ne permet pas de déterminer si `SAV` désigne un objet propre
(un dossier), un processus, ou un type particulier d'intervention parmi d'autres ; la
mission liste explicitement cette question au §7.

**FAMILLE_CANDIDATE : catalogue (produit / ouvrage / article)**
RACINES CONCERNÉES : `produit`, `article`, `ouvrage`, `bibliothèque`, `catégorie
tarifaire`, `produit centralisé`.
VALEURS EXACTES ILLUSTRATIVES : « produit (fiche produit, complet) », « article
(mise à jour depuis pièce commerciale) », « ouvrage (bibliothèque, prestation vendue
au client) », « bibliothèque (ouvrages vs éléments — structure du catalogue) ».
CONCURRENTS/CORPUS CONCERNÉS : `produit` (3 corpus), `article` (1, extrabat_help),
`ouvrage` (3), `bibliothèque` (3), `catégorie tarifaire` (1), `produit centralisé` (1).
JUSTIFICATION LINGUISTIQUE MINIMALE : aucun lexème commun entre `produit`, `article` et
`ouvrage` ; le rapprochement repose sur le fait que les trois désignent l'élément
vendable de base du catalogue, dans trois éditeurs différents (sellsy/openfire pour
`produit`, extrabat pour `article`, progbat/obat pour `ouvrage`).
STATUT : `AMBIGU` — pourrait être trois éditeurs employant trois termes pour le même
concept (synonymie inter-éditeurs), ou trois concepts légèrement différents (produit
générique vs article de caisse vs ouvrage de bâtiment incluant main d'œuvre). Le
contenu LIGHT ne tranche pas.

**FAMILLE_CANDIDATE : rapport / tableau de bord (restitution)**
RACINES CONCERNÉES : `rapport`, `rapport crm`, `rapport d'intervention`, `tableau de
bord`.
VALEURS EXACTES ILLUSTRATIVES : « rapport (analyse factures / consommation client) »,
« rapport CRM (par collaborateur) », « tableau de bord (opportunités) ».
CONCURRENTS/CORPUS CONCERNÉS : `rapport` (1, sellsy_help), `tableau de bord` (3),
`rapport d'intervention` (2).
JUSTIFICATION LINGUISTIQUE MINIMALE : lexème commun « rapport » pour deux des trois
racines ; `tableau de bord` est une forme de restitution différente (vue synthétique
persistante vs document généré à la demande).
STATUT : `CONCEPT_PROCHE_MAIS_DISTINCT` pour `rapport` vs `tableau de bord` (deux
formes de restitution distinctes) ; `rapport d'intervention` est à part — c'est un
document du domaine chantier/intervention, pas un document de pilotage commercial, donc
`AMBIGU` s'il doit être rattaché à cette famille ou à la famille intervention ci-dessus.

## 6. Domaines fonctionnels candidats

Construits à partir des racines et regroupements ci-dessus. La checklist fournie par la
mission sert de repère, pas de grille à remplir de force ; seuls les domaines
réellement observés sont listés, et des domaines hors checklist sont ajoutés quand les
racines les justifient.

| DOMAINE_CANDIDAT | RACINES ASSOCIÉES | OBSERVATIONS LIGHT | CORPUS CONCERNÉS | EXEMPLES DE VALEURS EXACTES | COMMENTAIRE D'AMBIGUÏTÉ |
|---|---|---:|---|---|---|
| Devis | `devis`, `ligne de devis`, `variantes de devis`, `import de devis`, `devis type` | ~30 (racines ≥3 de la famille) | 7 corpus | « devis (création, 4 méthodes) », « ligne de devis (contenu détaillé…) » | Granularité document/ligne non tranchée comme identité ou distinction (§7). |
| Facturation | `facture`, `factures`, `facture d'acompte`, `facture d'achat`, `facture d'abonnement`, `facture proforma`, `facturation électronique`, `avoir`, `règlement` | ~90 | 8+ corpus | « facture (annulation/modification via avoir) », « facturation électronique / plateforme agréée » | Regroupe plusieurs sous-familles distinctes (§5) ; ne pas traiter comme un seul objet. |
| Client / tiers | `client`, `fiche client`, `société`, `contact`, `contacts` | ~29 | 5 corpus | « fiche client (informations clés, résumé IA) » | Distinction client/contact non tranchée par LIGHT (§7). |
| Fournisseur / achats | `fournisseur`, `fiche fournisseur`, `commande fournisseur`, `achats`, `facture d'achat` | ~27 | 6 corpus | « commande fournisseur (transformation en document de vente) » | — |
| Paiement / trésorerie | `paiement`, `règlement`, `moyen de paiement`, `remise en banque`, `compte bancaire`, `rapprochement bancaire`, `trésorerie` | ~27 | 6 corpus | « rapprochement bancaire (connexion, réconciliation, DSP2, instabilité) » | Frontière `paiement`/`règlement` non tranchée (§7). |
| Chantier / affaire / intervention | `chantier`, `affaire`, `planning chantier`, `rendez-vous`, `sav`, `demande d'intervention`, `rapport d'intervention`, `planning` | ~34 | 7 corpus | « chantier (dossier digital) », « demande d'intervention (SAV/entretien…) » | Domaine le plus chargé en ambiguïtés listées §7 (chantier/affaire, visite/intervention, SAV). |
| Catalogue | `produit`, `article`, `ouvrage`, `bibliothèque`, `catégorie tarifaire`, `produit centralisé`, `gestion de stock`, `gestion des stocks`, `inventaire` | ~32 | 6 corpus | « bibliothèque (ouvrages vs éléments — structure du catalogue) » | Vocabulaire le plus dispersé entre éditeurs (produit/article/ouvrage), synonymie non confirmée (§7). |
| Signature électronique | `signature électronique` | 12 | 6 corpus | « signature électronique (Yousign, eIDAS, crédit par signature) » | Statut souvent codé `procedure` avec capacité `conformite_reglementaire` ; racine isolée, pas rattachée mécaniquement à `devis` malgré la proximité de sens dans plusieurs valeurs exactes. |
| Conformité / fiscalité | `taux de tva`, `tva`, `cgv`, `plan comptable`, `code comptable` | ~20 | 6 corpus | « taux de TVA (ajout, TVA intracommunautaire) », « plan comptable (comptes généraux, tiers) » | — |
| Comptabilité / marge | `marge`, `calcul de marge`, `intégration comptable` | ~11 | 4 corpus | « intégration comptable (Pennylane via Chift) » | — |
| Reporting / pilotage | `rapport`, `rapport crm`, `tableau de bord` | ~63 | 4 corpus | « rapport (analyse tickets support) », « tableau de bord (achats et marges) » | Très concentré sur sellsy_help pour `rapport`/`automatisation` — silence sur les autres éditeurs n'implique pas absence de reporting chez eux (§9). |
| CRM / prospection | `opportunité`, `pipeline`, `campagne emailing` | ~13 | 5 corpus | « opportunité (analyse pipeline, tunnels de conversion) » | Recoupe partiellement le domaine « client/tiers » (le prospect est un état du tiers, pas un objet séparé identifié mécaniquement). |
| Automatisation / IA | `automatisation`, `ia` | 18 | 1 corpus (sellsy_help) | « automatisation (opportunité ↔ facture liée) », « IA (résumé fiche client) » | Concentration mono-corpus forte : peut refléter une spécificité produit réelle (Sellsy IA) ou un simple effet de nommage — LIGHT ne tranche pas. |
| Application mobile / accès | `application mobile`, `mot de passe`, `connexion`, `double authentification` | ~18 | 8 corpus | « application mobile (vue d'ensemble, fonctionnalités et workflow terrain) » | Transverse par nature (capacité `mobile`, `securite_compte`), pas un domaine métier au sens strict — retenu car récurrent dans `objet_principal`. |
| Personnalisation / configuration compte | `champ personnalisé`, `modèle de document`, `modèle de courrier`, `utilisateur`, `agenda`, `synchronisation email`, `synchronisation agenda` | ~40 | 8 corpus | « champ personnalisé (types, zones d'affichage, vs catégories) » | Domaine hétérogène rassemblant plusieurs sous-fonctions de paramétrage transverses. |

Domaines de la checklist mission **non retrouvés comme racines distinctes** dans ce
niveau d'agrégation (ce qui ne signifie pas qu'ils sont absents des corpus — voir §9) :
« demande / prospect / lead » n'apparaît pas comme racine autonome (le prospect
apparaît uniquement en qualificatif de `client`, ex. « client / prospect ») ; « photos »,
« documents », « rôles / permissions », « tâches / notifications » n'émergent pas comme
racines `objet_principal` à fréquence ≥ 3 — ces notions apparaissent surtout dans le
champ `capacites_transverses`, hors périmètre d'extraction de cette mission (§1 de la
mission : seul `objet_principal` est exploité comme champ principal).

## 7. Ambiguïtés à résoudre plus tard

**Client vs Contact vs Société ?**
TERMES/RACINES OBSERVÉS : `client`, `fiche client`, `contact`, `société`.
CONCURRENTS CONCERNÉS : axonaut_help, batikko_help, costructor_help, extrabat_help,
openfire_zendesk, progbat_help, sellsy_help.
CE QUE LIGHT ÉTABLIT : les quatre termes coexistent dans le corpus documentaire, parfois
dans une même valeur exacte (« client / prospect (fiche contact) »,
« société/contact (fiche, catégorisation auto, unicité particulier) »).
CE QUE LIGHT N'ÉTABLIT PAS : si `contact` désigne une personne physique rattachée à une
`société`/un `client`, ou un synonyme générique de tiers ; si `fiche client` est
uniquement la vue détaillée de `client` ou porte des informations que `client` seul ne
porte pas.
TYPES DE SOURCES À RELIRE PLUS TARD : documents `fiche client`/`contact` en V3, en
particulier chez axonaut_help (« société/contact ») et sellsy_help.

**Chantier vs Affaire vs Projet ?**
TERMES/RACINES OBSERVÉS : `chantier`, `affaire`.
CONCURRENTS CONCERNÉS : batikko_help, extrabat_help (`affaire`), inter_fast_help,
obat_help, progbat_help.
CE QUE LIGHT ÉTABLIT : `chantier` est largement partagé (4 corpus) ; `affaire`
n'apparaît que chez extrabat_help ; une valeur exacte batikko_help signale elle-même
une « distinction chantier/marché de travaux ».
CE QUE LIGHT N'ÉTABLIT PAS : si `affaire` chez Extrabat est un synonyme de `chantier`
sous un autre nom, ou un objet de niveau supérieur regroupant plusieurs chantiers.
TYPES DE SOURCES À RELIRE PLUS TARD : le corpus extrabat_help complet sur `affaire`
(3 occurrences identifiées, §4.A) comparé aux définitions `chantier` des autres
éditeurs.

**Visite / Rendez-vous vs Intervention ?**
TERMES/RACINES OBSERVÉS : `rendez-vous`, `rapport d'intervention`, `demande
d'intervention`, `planning chantier`.
CONCURRENTS CONCERNÉS : extrabat_help, inter_fast_help, openfire_zendesk.
CE QUE LIGHT ÉTABLIT : `rendez-vous` est employé pour la prise de créneau
(planification), `rapport d'intervention` pour la restitution après passage terrain ;
les deux termes coexistent chez extrabat_help.
CE QUE LIGHT N'ÉTABLIT PAS : si « rendez-vous » et « intervention » désignent deux
étapes d'un même objet (prévu vs réalisé) ou deux objets distincts.
TYPES DE SOURCES À RELIRE PLUS TARD : séquence documentaire complète chez
openfire_zendesk (guides-videos/prendre-rendez-vous-*, realiser-un-rendez-vous-*).

**SAV comme objet, processus ou type d'intervention ?**
TERMES/RACINES OBSERVÉS : `sav`, `demande d'intervention`.
CONCURRENTS CONCERNÉS : extrabat_help, openfire_zendesk.
CE QUE LIGHT ÉTABLIT : une valeur exacte openfire_zendesk relie explicitement les deux
(« demande d'intervention (SAV/entretien, portail client) ») ; `sav` est parfois codé
comme « dossier complet » (extrabat_help : « SAV (dossier complet, cycle
commercial/logistique/technique) »).
CE QUE LIGHT N'ÉTABLIT PAS : si SAV est un statut d'intervention, un type de dossier
séparé, ou un processus transverse au cycle chantier.
TYPES DE SOURCES À RELIRE PLUS TARD : rubrique SAV complète chez extrabat_help et
openfire_zendesk (utiliser-openfire/gerer-et-planifier-un-sav.md et voisins).

**Produit vs Article vs Ouvrage ?**
TERMES/RACINES OBSERVÉS : `produit`, `article`, `ouvrage`, `bibliothèque`.
CONCURRENTS CONCERNÉS : axonaut_help, extrabat_help, obat_help, openfire_zendesk,
progbat_help, sellsy_help.
CE QUE LIGHT ÉTABLIT : trois lexèmes distincts sans recoupement lexical direct,
concentrés chacun sur un sous-ensemble d'éditeurs différent (`produit` chez
axonaut/openfire/sellsy, `article` uniquement chez extrabat, `ouvrage` chez
extrabat/obat/progbat).
CE QUE LIGHT N'ÉTABLIT PAS : si ces trois termes recouvrent le même objet catalogue
sous un vocabulaire différent par éditeur, ou trois objets réellement distincts
(élément vendable générique vs article de caisse vs prestation de bâtiment incluant
main d'œuvre).
TYPES DE SOURCES À RELIRE PLUS TARD : définitions catalogue produit chez extrabat_help
et progbat_help/obat_help en particulier.

**Devis vs Ligne de devis vs Variante de devis ?**
TERMES/RACINES OBSERVÉS : `devis`, `ligne de devis`, `variantes de devis`.
CONCURRENTS CONCERNÉS : inter_fast_help, obat_help, progbat_help.
CE QUE LIGHT ÉTABLIT : `ligne de devis` est documentée comme composant interne du
devis (progbat_help, 3 articles dédiés à la création/gestion des lignes) ; `variantes
de devis` comme un mécanisme de déclinaison du même devis (obat_help : « vos
références restent stables de la création à la facture »).
CE QUE LIGHT N'ÉTABLIT PAS : le modèle de données exact (une variante est-elle un
nouveau devis, un état du même devis, ou un objet séparé lié) — LIGHT n'observe que du
contenu documentaire, pas un schéma de données.
TYPES DE SOURCES À RELIRE PLUS TARD : articles `variantes de devis` obat_help et
inter_fast_help en V3.

**Paiement vs Règlement ?**
TERMES/RACINES OBSERVÉS : `paiement`, `règlement`, `moyen de paiement`.
CONCURRENTS CONCERNÉS : costructor_help, extrabat_help, inter_fast_help,
openfire_odoo, openfire_zendesk, sellsy_help.
CE QUE LIGHT ÉTABLIT : `règlement` apparaît systématiquement associé à une facture
(« règlement (paiement sur facture) », « enregistrer un règlement sur une facture »),
`paiement` est employé plus largement (dépenses, remboursements, consignations).
CE QUE LIGHT N'ÉTABLIT PAS : si les deux termes sont de purs synonymes chez un même
éditeur (choix rédactionnel) ou s'ils recouvrent des concepts de portée différente.
TYPES DE SOURCES À RELIRE PLUS TARD : glossaire ou FAQ interne des éditeurs qui
emploient les deux termes dans des corpus distincts (costructor_help vs extrabat_help).

**Facture vs Facturation électronique ?**
TERMES/RACINES OBSERVÉS : `facture`, `facturation électronique`, `mandat pa`.
CONCURRENTS CONCERNÉS : 7 corpus pour `facturation électronique`.
CE QUE LIGHT ÉTABLIT : `facturation électronique` est systématiquement associée à un
vocabulaire de conformité réglementaire (PDP, Chorus Pro, mandat PA, eIDAS) plutôt qu'à
la création du document lui-même.
CE QUE LIGHT N'ÉTABLIT PAS : si c'est un canal de transmission de la même `facture`,
ou un objet/processus séparé (avec son propre cycle de vie, statuts, obligations).
TYPES DE SOURCES À RELIRE PLUS TARD : rubrique `facturation-electronique/` complète
chez sellsy_help (mandat PA, KYC) et obat_help/progbat_help/costructor_help.

**Document vs pièce commerciale vs pièce jointe ?**
TERMES/RACINES OBSERVÉS : `pièce commerciale`, `document de vente`, `modèle de
document`.
CONCURRENTS CONCERNÉS : extrabat_help, sellsy_help, progbat_help.
CE QUE LIGHT ÉTABLIT : `pièce commerciale` (extrabat_help) et `document de vente`
(sellsy_help) semblent désigner la même famille d'objets (devis/commande/facture) sous
deux vocabulaires d'éditeur différents.
CE QUE LIGHT N'ÉTABLIT PAS : l'équivalence exacte, ni si l'un des deux termes couvre un
périmètre plus large (ex. incluant les pièces jointes email) que l'autre.
TYPES DE SOURCES À RELIRE PLUS TARD : articles `document de vente` (sellsy_help) et
`pièce commerciale` (extrabat_help) en lecture croisée.

## 8. Limites

- **Périmètre strictement instrumental.** Cette mission n'a lu aucun document source,
  n'a utilisé aucune connaissance externe, et n'a exploité que le champ
  `objet_principal` des 12 productions LIGHT canoniques (plus `moment_parcours`,
  `chemin_relatif` et `genre_documentaire` comme contexte mécanique).
- **Fréquence documentaire ≠ importance produit.** Un root fréquent (ex. `rapport`,
  36 occurrences, toutes chez sellsy_help) reflète la densité de la documentation
  Sellsy sur ce sujet, pas une place supérieure du reporting dans le produit Sellsy par
  rapport à ses concurrents.
- **Fréquence documentaire ≠ fréquence d'usage.** Aucune donnée d'usage réel n'est
  mobilisée ici.
- **Silence documentaire ≠ absence fonctionnelle.** Un domaine candidat absent de la
  table §6 pour un éditeur donné ne signifie pas que le produit ne le couvre pas —
  seulement que LIGHT n'a pas observé ce vocabulaire dans le corpus d'aide couvert par
  la production correspondante.
- **Racine mécanique ≠ objet métier.** L'algorithme de coupe (§2) regroupe des chaînes
  de caractères, pas des concepts. Deux racines identiques peuvent recouvrir deux
  usages différents (voir en particulier `client`/`fiche client`, `rapport`).
- **Regroupement lexical (§5) ≠ identité fonctionnelle.** Chaque `STATUT` proposé est
  une hypothèse de travail à vérifier en V3, jamais une conclusion.
- **Vocabulaire concurrent ≠ vocabulaire SUPORDO.** Aucun terme de ce document ne doit
  être repris tel quel comme nom d'objet dans une future modélisation SUPORDO sans
  passage par une analyse fonctionnelle dédiée.
- **Couverture inégale des corpus.** Les corpus vont de 11 lignes (batikko_help,
  cumulé pilote+dédié : 14) à 462 lignes (sellsy_help). Les comparaisons de fréquence
  brute entre corpus sont donc structurellement biaisées par ce déséquilibre de volume
  documentaire, pas seulement par un éventuel déséquilibre fonctionnel réel.
- **Non-recoupement entre productions non re-vérifié indépendamment.** L'absence de
  chevauchement de documents entre le pilote et les productions dédiées (§1) repose sur
  les déclarations d'exclusion de chaque fichier source, non sur une comparaison
  mécanique des 2504 chemins relatifs entre eux menée par cette mission.
- **`light-h3-validation-positifs.md` exclu.** 6 observations LIGHT supplémentaires
  existent sur InterFast/Vertuoza dans ce fichier auto-déclaré non canonique ; elles ne
  sont pas comptées dans les 2504 lignes de ce document (§1).
- **Aucune décision SUPORDO.** Ce document ne contient ni ontologie, ni modèle de
  données, ni spécification, ni backlog.
