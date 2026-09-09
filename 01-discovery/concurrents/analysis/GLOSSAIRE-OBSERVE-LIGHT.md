# Glossaire observé — inventaire sémantique du corpus LIGHT

Document produit par exploitation mécanique des productions LIGHT existantes. Ne
relit aucune source, ne modifie aucune production LIGHT, ne décide d'aucun objet
canonique SUPORDO. Répond à une seule question : quels objets/concepts métier ont
été observés dans LIGHT, avec quels termes, chez quels éditeurs.

## 1. Périmètre

### Productions LIGHT identifiées (mécaniquement, depuis `01-discovery/concurrents/analysis/`)

13 fichiers `light-*.md` / assimilés recensés, dont 1 pilote historique, 11
productions par corpus, et 1 micro-lot de validation méthodologique H3 :

| Production | Fichier | Lignes | Nature |
|---|---|---:|---|
| Pilote | `pilote-light-corpus-inedit.md` | 40 | historique, antérieur à SCHEMA-LIGHT.md (§11) ; `chemin_relatif` absent du tableau de sortie, reconstitué ici par jointure `#` avec le tableau de sélection séparé |
| Axonaut | `light-axonaut-help.md` | 119 | production par corpus |
| Batikko | `light-batikko-help.md` | 11 | production par corpus |
| Costructor | `light-costructor-help.md` | 94 | production par corpus, historique (§11) |
| Extrabat | `light-extrabat-help.md` | 347 | production par corpus |
| InterFast | `light-inter-fast-help.md` | 217 | production par corpus (exclut mécaniquement les 4 documents déjà couverts par le micro-lot H3, cf. §2) |
| Obat | `light-obat-help.md` | 274 | production par corpus |
| OpenFire (Odoo) | `light-openfire-odoo.md` | 212 | production par corpus |
| OpenFire (Zendesk) | `light-openfire-zendesk.md` | 119 | production par corpus |
| ProGBat | `light-progbat-help.md` | 186 | production par corpus, historique (§11) |
| Sellsy | `light-sellsy-help.md` | 454 | production par corpus |
| Vertuoza | `light-vertuoza-help.md` | 431 | production par corpus (exclut mécaniquement les 2 documents déjà couverts par le micro-lot H3, cf. §2) |
| Micro-lot H3 | `light-h3-validation-positifs.md` | 6 | échantillon expérimental non représentatif (test de sensibilité du filtre `regle_ou_condition`), 4 documents InterFast + 2 Vertuoza |
| **Total** | | **2510** | |

`pre-test-light-h3.md` et `test-sensibilite-light-h3.md` ne sont **pas** des
productions LIGHT : ce sont des documents méthodologiques qui analysent les
mêmes 6 lignes que `light-h3-validation-positifs.md`, sans tableau LIGHT propre.
Ils n'ont pas été comptés une seconde fois.

**10 concurrents distincts** sont représentés dans ce total (unité « éditeur »,
conforme à `corpus_index.json` — OpenFire regroupe ses deux sous-corpus
Zendesk et Odoo sous un seul `concurrent`) : axonaut, batikko, costructor,
extrabat, inter-fast, obat, openfire, progbat, sellsy, vertuoza.

### Source de données

Uniquement les 13 fichiers ci-dessus, champ `objet_principal`. Le champ
`moment_parcours` est repris en contexte mécanique, sans interprétation. Aucune
relecture des articles sources, aucun usage du Web, aucun usage de V2/V3,
aucune modification de LIGHT.

## 2. Méthode

### Règle valeur exacte / racine

Pour chaque ligne LIGHT :

1. **Valeur exacte** — le contenu de `objet_principal`, tel quel, sans
   modification.
2. **Racine mécanique** — le segment situé avant la première parenthèse `(`,
   la première barre oblique `/`, ou le premier tiret cadratin `—` ; le
   segment obtenu est mis en minuscules, les espaces sont réduits, la
   ponctuation terminale est retirée. Aucune autre normalisation.

La racine sert uniquement au regroupement de comptage. Elle n'écrase jamais la
valeur exacte, conservée intégralement en colonne « valeurs exactes » partout
dans ce document.

**Cas particulier observé** : Extrabat code 37 documents avec la valeur exacte
`— (motif)` (ex. `— (page d'accueil du centre d'aide, flux d'articles
hétérogène)`) pour signaler l'absence d'objet métier substantiel dans un
document. Le tiret cadratin étant en position 0, la racine mécanique de ces
37 lignes est la chaîne vide. Ce n'est pas une erreur d'extraction : c'est le
résultat mécanique correct de la règle appliquée à une convention propre à
cette production. Ces 37 lignes forment leur propre regroupement dans
l'inventaire (§3.1, racine `(vide)`) et ne doivent pas être lues comme un
concept métier.

### Jointure du pilote

Dans `pilote-light-corpus-inedit.md`, le tableau de sortie LIGHT (lignes
89-128) ne porte pas `chemin_relatif` — colonne présente uniquement dans le
tableau de sélection séparé (lignes 42-81). Les deux tableaux partagent la
même numérotation `#` 1→40, sans trou ni doublon. La jointure mécanique par
`#` a été vérifiée : 40/40 lignes appariées, aucune ambiguïté rencontrée. Cette
reconstitution est faite dans ce document uniquement pour produire
`chemin_relatif` en contexte ; elle ne modifie pas le pilote lui-même.

### Vérification de non-chevauchement

Contrôle mécanique effectué (comparaison des `chemin_relatif`, par concurrent) :

- **Pilote vs les 11 productions par corpus** : 0 chemin en commun. Le pilote
  a été explicitement construit sur des rubriques « non encore utilisées dans
  les travaux précédents » (auto-déclaration du fichier) ; le contrôle
  mécanique confirme qu'aucun des 40 chemins ne réapparaît dans une production
  ultérieure.
- **Micro-lot H3 vs InterFast/Vertuoza** : 0 chemin en commun, et ce par
  construction déclarée — `light-inter-fast-help.md` énumère explicitement
  les 4 chemins « déjà utilisés (micro-test H3) » et les exclut de son propre
  périmètre gelé (221 documents canoniques = 217 traités ici + 4 déjà en H3) ;
  `light-vertuoza-help.md` fait de même pour ses 2 documents (433 = 431 + 2).
  Le micro-lot H3 n'est donc pas un doublon des productions complètes : c'est
  le complément qui ferme la couverture totale de ces deux corpus.

Conséquence : les 2510 lignes exploitées dans ce document représentent
2510 documents distincts, sans double comptage détecté mécaniquement.


## 3. Inventaire par racine

**2510 lignes LIGHT exploitées → 2417 valeurs exactes distinctes
(93 doublons exacts, essentiellement des reformulations
identiques répétées sur des familles d'articles très proches — cf. §8) →
1864 racines distinctes.**

La réduction de 2417 valeurs exactes à 1864 racines confirme
l'avertissement de la mission : `objet_principal` est un champ libre, un
comptage de valeurs exactes serait resté proche du nombre de lignes. La racine
réduit l'espace d'un facteur ≈1,35 (2417 → 1864), pas d'un facteur massif —
cohérent avec un vocabulaire réellement ouvert et peu répété d'un document à
l'autre plutôt qu'avec quelques catégories récurrentes.

Répartition par fréquence de racine :

| Tranche | Nombre de racines | Part |
|---|---:|---:|
| ≥ 5 occurrences | 41 | 2.2% |
| 2 à 4 occurrences | 199 | 10.7% |
| 1 occurrence (racine unique) | 1624 | 87.1% |

Les trois sous-sections ci-dessous couvrent l'intégralité des 1864
racines — aucune n'est omise, conformément au caractère de cartographie
exhaustive de cette mission. Le niveau de détail décroît avec la fréquence :
les racines fréquentes portent le plus d'information pour le choix de
domaines (§6), les racines uniques sont listées de façon compacte (une seule
occurrence, donc un seul concurrent, une seule valeur exacte, un seul
chemin — les colonnes "échantillon" n'ont pas lieu d'être répétées).

### 3.1 Racines fréquentes (≥ 5 occurrences — 41 racines)

| Racine | Occurrences | Concurrents | Valeurs exactes représentatives | Chemins représentatifs | moment_parcours observés |
|---|---:|---|---|---|---|
|  | 37 | extrabat:37 | — (page sans contenu substantif, résidu de gabarit de navigation)<br>— (page sans contenu substantif, question sans réponse)<br>— (billet éditorial/motivationnel, sans contenu instructif)<br>— (page d'accueil du centre d'aide, flux d'articles hétérogène)<br>— (billet éditorial sur la conduite du changement, sans contenu produit) | extrabat:astuce-le-raccourci-de-recherche.md<br>extrabat:cloturer-la-caisse.md<br>extrabat:comment-bien-parametrer-son-navigateur-internet-firefox.md<br>extrabat:comment-creer-sa-signature-le-logiciel-extrabat.md<br>extrabat:comment-donner-les-droits-utilisateur-consulter-etou-modifier.md | indetermine:35, chantier-intervention:1, devis:1 |
| rapport | 36 | sellsy:36 | rapport (analyse factures / consommation client)<br>rapport (analyse tickets support)<br>rapport (CA global par collaborateur)<br>rapport (CA global)<br>rapport (comparatif performances annuelles) | sellsy:rapports-et-pilotage/rapport-analyse-des-factures-et-consommation.md<br>sellsy:rapports-et-pilotage/rapport-analyse-des-tickets-de-support.md<br>sellsy:rapports-et-pilotage/rapport-ca-global-par-collaborateur.md<br>sellsy:rapports-et-pilotage/rapport-ca-global.md<br>sellsy:rapports-et-pilotage/rapport-comparatif-des-performances-annuelles.md | indetermine:23, facturation:8, achat:1, devis:4 |
| indetermine | 33 | progbat:24, openfire:8, axonaut:1 | indetermine (page d'accueil, fragment HTML incomplet)<br>indetermine (page d'index agrégée, extraits partiels de plusieurs articles)<br>indetermine (classement utilisateurs, plateforme)<br>indetermine (plateforme eLearning, aucun cours publié)<br>indetermine (sommaire webinaires, sans contenu) | openfire:dm-openfire-fr.md<br>openfire:index.md<br>openfire:knowsystem.md<br>openfire:profile/users.md<br>openfire:slides.md | indetermine:33 |
| facture | 24 | sellsy:6, openfire:5, progbat:5, inter-fast:4, extrabat:2, axonaut:1, costructor:1 | facture (création, langues, adresses communes, CGV, images — hub multi-sujets)<br>facture (avec ou sans devis)<br>facture (autoliquidation TVA)<br>facture (suppression impossible, loi 2018)<br>facture (création, édition, envoi depuis app mobile) | axonaut:gerez-vos-factures/creer-une-facture-avec-axonaut-2.md<br>costructor:ventes/comment-creer-une-facture-ndrp7y.md<br>extrabat:comment-realiser-une-facture-en-autoliqudation.md<br>extrabat:veux-supprimer-facture.md<br>inter-fast:inter-fast/application-mobile/creer-des-factures-app-mobile.md | facturation:23, indetermine:1 |
| tableau de bord | 24 | sellsy:21, progbat:2, extrabat:1 | tableau de bord (envoi par email, périodicité)<br>tableau de bord (personnalisation : vignettes, lignes)<br>tableau de bord (événements)<br>tableau de bord (opportunités)<br>tableau de bord (tâches) | extrabat:recevoir-tableau-de-bord-mail.md<br>progbat:pour-bien-demarrer/demarrer-avec-progbat/personnaliser-le-tableau-de-bord.md<br>sellsy:app-mobile-sellsy-crm/app-sellsy-crm-tableau-de-bord-mes-evenements.md<br>sellsy:app-mobile-sellsy-crm/app-sellsy-crm-tableau-de-bord-opportunites.md<br>sellsy:app-mobile-sellsy-crm/app-sellsy-crm-tableau-de-bord-taches.md | indetermine:24 |
| devis | 20 | progbat:6, inter-fast:5, extrabat:3, openfire:2, sellsy:2, axonaut:1, obat:1 | devis (création, IA, duplication, téléchargement PDF)<br>devis (création)<br>devis (envoi, méthodes multiples)<br>devis/commande (suppression)<br>devis (création, édition, consultation app mobile) | axonaut:gerez-vos-devis/creer-un-devis-avec-axonaut.md<br>extrabat:faire-un-devis.md<br>extrabat:les-differentes-facons-denvoyer-un-devis-dans-extrabat.md<br>extrabat:supprimer-un-devis-ou-une-facture.md<br>inter-fast:inter-fast/application-mobile/creer-un-devis-app-mobile.md | devis:19, indetermine:1 |
| automatisation | 13 | sellsy:13 | automatisation (suivi continu documents, tâche)<br>automatisation (suivi continu opportunités, tâche)<br>automatisation (opportunité ↔ facture liée)<br>automatisation (opportunité ↔ tâche terminée)<br>automatisation (configuration générale, gestion) | sellsy:sellsy-automatisations/assurer-un-suivi-continu-de-vos-documents.md<br>sellsy:sellsy-automatisations/assurer-un-suivi-continu-de-vos-opportunites.md<br>sellsy:sellsy-automatisations/avancer-automatiquement-vos-opportunites-avec-les-factures-liees.md<br>sellsy:sellsy-automatisations/avancer-vos-opportunites-lorsqu-une-tache-est-terminee.md<br>sellsy:sellsy-automatisations/configurer-et-activer-une-automatisation-dans-sellsy.md | indetermine:9, devis:3, facturation:1 |
| facturation électronique | 13 | openfire:3, costructor:2, obat:2, progbat:2, sellsy:2, inter-fast:1, batikko:1 | facturation électronique / transfert comptable<br>facturation électronique (réforme 2026-2027, conformité, Peppol/Pennylane)<br>facturation électronique (page de catégorie)<br>facturation électronique (calendrier légal, formats, obligations)<br>facturation électronique (émission factures clients) | costructor:debuter-sur-costructor/comment-transferer-les-factures-electroniques-vers-une-adresse-mail-comptable-wizy4e.md<br>inter-fast:inter-fast/mon-entreprise/comprendre-la-facturation-electronique.md<br>obat:`facturation-c3-a9lectronique.md`<br>obat:`facturation-electronique-dans-le-btp-dates-cles-formats-et-obligations.md`<br>openfire:configurer-openfire/activer-et-parametrer-l-emission-de-vos-factures-clients.md | facturation:10, achat:1, indetermine:2 |
| signature électronique | 12 | sellsy:4, axonaut:2, extrabat:2, progbat:2, obat:1, openfire:1 | signature électronique (jesignexpert, lettre de mission)<br>signature électronique (Yousign, eIDAS, crédit par signature)<br>signature électronique (Oodrive Sign)<br>signature électronique (Universign)<br>signature électronique (configuration Yousign, emails, rappels) | axonaut:gerez-vos-devis/comment-connecter-jesignexpert-a-axonaut.md<br>axonaut:gerez-vos-devis/signature-electronique-des-devis-documents-yousign.md<br>extrabat:gestion-commerciale.md<br>extrabat:la-signature-electronique.md<br>obat:`comment-activer-la-signature-c3-a9lectronique-sur-obat.md` | indetermine:6, devis:5, facturation:1 |
| fiche client | 10 | extrabat:5, sellsy:2, axonaut:1, inter-fast:1, progbat:1 | fiche client (échanges, prospect→client, fusion de doublons)<br>fiche client/prospect (création)<br>fiche client (fusion/doublons)<br>fiche client (interface de création, champs particulier/professionnel)<br>fiche client (bonnes pratiques de saisie, suivi statistique) | axonaut:optimisez-gestion-commerciale/la-fiche-client-axonaut.md<br>extrabat:creer-une-fiche-client-ou-prospect.md<br>extrabat:fusionner-deux-fiches-clients.md<br>extrabat:mise-a-jour-nouvelle-interface-pour-la-creation-de-la-fiche-client.md<br>extrabat:passage-oblige.md | indetermine:9, demande:1 |
| rendez-vous | 8 | openfire:5, extrabat:3 | rendez-vous (multi-utilisateurs, multi-jours)<br>rendez-vous (prise, plusieurs méthodes)<br>rendez-vous (optimisation tournée, proximité géographique)<br>rendez-vous (présentation des éléments)<br>rendez-vous (planification, mobile) | extrabat:associer-rendez-vous-plusieurs-utilisateurs-sur-plusieurs-jours.md<br>extrabat:je-veux-prendre-un-rendez-vous.md<br>extrabat:optimiser-ses-rendez-vous-par-zone-geographique.md<br>openfire:guides-videos/decouvrir-la-presentation-d-un-rendez-vous.md<br>openfire:guides-videos/planifier-un-rendez-vous-sur-le-mobile.md | chantier-intervention:7, indetermine:1 |
| article | 7 | extrabat:7 | article (duplication)<br>article (mise à jour depuis pièce commerciale)<br>article (mise à jour via paramètres)<br>article (fraîcheur de mise à jour, code couleur)<br>article (création) | extrabat:comment-dupliquer-article.md<br>extrabat:comment-mettre-a-jour-un-article-a-partir-dune-piece-commerciale.md<br>extrabat:comment-mettre-a-jour-un-article-par-les-parametres.md<br>extrabat:comment-savoir-si-article-jour-periode-de-moins-dun.md<br>extrabat:creer-un-nouvel-article.md | indetermine:6, devis:1 |
| champ personnalisé | 7 | sellsy:6, axonaut:1 | champ personnalisé (types, zones d'affichage, vs catégories)<br>champ personnalisé (affichage liste)<br>champ personnalisé (affichage document de vente)<br>champ personnalisé (création)<br>champ personnalisé (édition en masse) | axonaut:optimisez-gestion-commerciale/les-champs-personnalises-dans-axonaut-cest-quoi.md<br>sellsy:gestion-des-donnees/afficher-les-champs-personnalises-dans-une-liste.md<br>sellsy:gestion-des-donnees/afficher-un-champ-personnalise-sur-un-document-de-vente.md<br>sellsy:gestion-des-donnees/creer-des-champs-personnalises.md<br>sellsy:gestion-des-donnees/editer-les-valeurs-des-champs-personnalises-en-masse.md | indetermine:6, facturation:1 |
| client | 7 | extrabat:3, progbat:2, batikko:1, costructor:1 | client (fiche CRM, KYC, scoring)<br>client / prospect (fiche contact)<br>client/prospect (création via agenda)<br>client (récupération depuis corbeille, erreur)<br>client/prospect (suppression impossible, corbeille) | batikko:guides/clients-crm.md<br>costructor:ventes/comment-creer-un-client-prospect-ue8wib.md<br>extrabat:creer-un-client-via-lagenda.md<br>extrabat:recuperer-client-mis-erreur-statut-corbeille.md<br>extrabat:supprimer-prospect-client.md | indetermine:5, demande:1, devis:1 |
| commande fournisseur | 7 | extrabat:4, axonaut:1, openfire:1, sellsy:1 | commande fournisseur (bon de commande PDF)<br>commande fournisseur (reliquat)<br>commande fournisseur (protocole EDI)<br>commande fournisseur (intégration Pool 360)<br>commande fournisseur (création) | axonaut:commandes-clients-fournisseurs/creer-une-commande-fournisseur.md<br>extrabat:annuler-un-reliquat-de-commande-fournisseur.md<br>extrabat:comment-envoyer-sa-commande-fournisseur-via-le-protocole-edi.md<br>extrabat:comment-passer-une-commande-fournisseur-de-la-solution-extrabat-vers-pool-360.md<br>extrabat:passer-une-commande-fournisseur.md | achat:7 |
| contact | 7 | openfire:5, sellsy:2 | contact (création, mobile)<br>contact (mise à jour, mobile)<br>contact (fiche client/fournisseur, complet)<br>contact (fusion de doublons)<br>contact (import en masse via Excel/OpenImport) | openfire:guides-videos/creer-un-contact-sur-mobile.md<br>openfire:guides-videos/mettre-a-jour-un-contact-sur-mobile.md<br>openfire:utiliser-openfire/creer-un-contact.md<br>openfire:utiliser-openfire/fusionner-vos-contacts.md<br>openfire:utiliser-openfire/importer-des-contacts-a-partir-d-un-fichier-excel.md | indetermine:7 |
| facture d'acompte | 7 | extrabat:3, costructor:1, obat:1, openfire:1, sellsy:1 | facture d'acompte (transition depuis devis)<br>facture d'acompte (commande divisée)<br>facture d'acompte<br>facture d'acompte (génération depuis commande)<br>facture d'acompte (avance, comptabilité légale) | costructor:ventes/comment-creer-une-facture-dacompte-fllvsr.md<br>extrabat:creer-une-facture-dacompte.md<br>extrabat:gestion-commerciale/page/7.md<br>extrabat:tag/commande.md<br>obat:`comment-facturer-un-acompte-depuis-un-devis-sur-obat.md` | facturation:7 |
| modification | 7 | axonaut:5, costructor:1, obat:1 | modification/suppression de dépense (cas bloquants : payée, réceptionnée, droits)<br>modification/suppression de devis (statuts, cas bloquants)<br>modification/suppression de facture (paiement, avoir, droits — contenu recoupant #80/#84)<br>modification/suppression de produit (désactivation, archives, droits)<br>modification/suppression de contact (archives, droits, réaffectation) | axonaut:creez-depenses-facilement/modifier-supprimer-une-depense.md<br>axonaut:gerez-vos-devis/modifier-un-devis.md<br>axonaut:gerez-vos-factures/comment-modifier-une-facture.md<br>axonaut:gerez-vos-produits/modifier-un-produit.md<br>axonaut:optimisez-gestion-commerciale/modifier-un-contact.md | achat:1, devis:1, facturation:2, indetermine:3 |
| mot de passe | 7 | extrabat:6, inter-fast:1 | mot de passe (changement/réinitialisation)<br>mot de passe (oubli, réinitialisation)<br>mot de passe (nouvelle mesure de sécurité, critères)<br>mot de passe (sécurisation, conseils)<br>mot de passe (réinitialisation) | extrabat:comment-changer-votre-mot-de-passe.md<br>extrabat:mot-de-passe-oublie.md<br>extrabat:mots-de-passe-nouvelle-mesure-de-securite.md<br>extrabat:securisez-vos-mots-de-passe.md<br>extrabat:securite-fr.md | indetermine:7 |
| produit | 7 | sellsy:4, openfire:2, axonaut:1 | produit/service (ajout, IA, vente en ligne, code-barres, traduction — hub multi-sujets)<br>produit (fiche produit, complet)<br>produit (import en masse, tarifs)<br>produit / service (catalogue)<br>produit / service (définition catalogue) | axonaut:gerez-vos-produits/comment-ajouter-des-produits-services-dans-axonaut.md<br>openfire:utiliser-openfire/creer-un-produit.md<br>openfire:utiliser-openfire/importer-mes-produits-avec-open-import.md<br>sellsy:catalogue-produits-et-services/ajouter-des-produits-et-services-a-mon-catalogue.md<br>sellsy:catalogue-produits-et-services/difference-entre-produits-et-services.md | indetermine:6, achat:1 |
| règlement | 7 | costructor:2, extrabat:2, sellsy:2, openfire:1 | règlement (paiement sur facture)<br>règlement (suppression sur facture)<br>règlement (correction erreur de type, contrepasser)<br>règlement (impossibilité de modifier, contrepasser, loi anti-fraude 2018)<br>règlement (paiement, lettrage) | costructor:ventes/comment-enregistrer-un-reglement-sur-une-facture-j8zd6o.md<br>costructor:ventes/comment-supprimer-un-reglement-sur-une-facture-1jal4w6.md<br>extrabat:me-suis-trompe-de-type-de-reglement-especes-carte-bleue-cheques.md<br>extrabat:ne-peux-modifier-mode-de-reglement.md<br>openfire:utiliser-openfire/enregistrer-un-reglement-client-ou-fournisseur.md | facturation:7 |
| synchronisation agenda | 7 | extrabat:5, sellsy:2 | synchronisation agenda (CalDAV/mobile)<br>synchronisation agenda (forcer)<br>synchronisation agenda (CalDAV, smartphone Apple)<br>synchronisation agenda / contacts (Google)<br>synchronisation agenda / contacts (Office 365 / Outlook) | extrabat:agenda-2.md<br>extrabat:forcer-la-synchronisation-de-mes-rendez-vous-a-venir.md<br>extrabat:parametrage.md<br>extrabat:synchroniser-mon-agenda-avec-mon-telephone-sous-android.md<br>extrabat:synchroniser-mon-agenda-sur-iphone-ou-ipad.md | indetermine:7 |
| synchronisation email | 7 | axonaut:5, inter-fast:1, obat:1 | synchronisation email (Google Workspace, routage)<br>synchronisation email (OVH, règle de redirection)<br>synchronisation email (Gandi, redirection)<br>synchronisation email (Microsoft 365, règle de flux)<br>synchronisation email (définition + multi-fournisseurs) | axonaut:centralisez-gestion-emails-courriers/comment-synchroniser-ses-emails-google-workspace-avec-axonaut.md<br>axonaut:centralisez-gestion-emails-courriers/emails-synchroniser-ovh-avec-axonaut.md<br>axonaut:centralisez-gestion-emails-courriers/synchronisation-des-mails-avec-gandi.md<br>axonaut:centralisez-gestion-emails-courriers/synchronisation-des-mails-avec-microsoft365-office-365.md<br>axonaut:centralisez-gestion-emails-courriers/synchroniser-ses-emails-ca-veut-dire-quoi-2.md | indetermine:7 |
| abonnement | 6 | obat:3, axonaut:1, costructor:1, sellsy:1 | abonnement (formules, renouvellement, factures, frais tiers)<br>abonnement (souscription initiale)<br>abonnement / choix de pack<br>abonnement / choix de pack (micro-entreprise)<br>abonnement (page de catégorie) | axonaut:configurer-votre-compte/abonnement-axonaut-on-vous-explique-tout.md<br>costructor:abonnement/comment-sabonner-a-costructor-vxkaie.md<br>obat:`entreprise-eurl/sarl/sas-comment-s-abonner-c3-a0-obat-et-choisir-son-pack.md`<br>obat:`micro-entreprise/auto-entrepreneur-comment-s-abonner-c3-a0-obat-et-choisir-son-pack.md`<br>obat:`mon-abonnement.md` | indetermine:5, facturation:1 |
| application mobile | 6 | costructor:1, inter-fast:1, obat:1, openfire:1, progbat:1, sellsy:1 | application mobile (PWA)<br>application mobile (vue d'ensemble, fonctionnalités et workflow terrain)<br>application mobile<br>application mobile (téléchargement, connexion)<br>application mobile (accès utilisateur / accès compagnon) | costructor:debuter-sur-costructor/telecharger-lapplication-costructor-sur-mobile-s25hdg.md<br>inter-fast:inter-fast/application-mobile/utiliser-notre-application-mobile.md<br>obat:`application-mobile.md`<br>openfire:guides-videos/telecharger-l-application-openfire-et-se-connecter.md<br>progbat:application-mobile.md | indetermine:5, chantier-intervention:1 |
| chantier | 6 | inter-fast:2, progbat:2, obat:1, batikko:1 | chantier (fiche de synthèse, suivi, app mobile)<br>chantier (page de catégorie)<br>chantier (concept, distinction chantier/marché de travaux, statuts)<br>chantier (création, 3 méthodes)<br>chantier (dossier digital) | inter-fast:inter-fast/application-mobile/suivre-ses-chantiers-app-mobile.md<br>obat:`chantier.md`<br>progbat:le-menu-principal/chantiers-personnel/chantiers.md<br>progbat:le-menu-principal/chantiers-personnel/chantiers/creer-un-chantier.md<br>batikko:guides/chantiers.md | chantier-intervention:6 |
| opportunité | 6 | sellsy:4, openfire:2 | opportunité (analyse pipeline, tunnels de conversion)<br>opportunité (CRM, pipeline)<br>opportunité (pipeline)<br>opportunité (suivi, définition)<br>opportunité (suivi via tâches) | openfire:knowsystem/analyser-ses-opportunites-120.md<br>openfire:utiliser-openfire/creer-une-opportunite.md<br>sellsy:app-mobile-sellsy-crm/app-sellsy-crm-ajouter-une-opportunite.md<br>sellsy:crm-et-prospection/introduction-suivi-des-opportunites.md<br>sellsy:crm-et-prospection/suivre-mes-opportunites-en-utilisant-les-taches.md | demande:2, indetermine:4 |
| rapprochement bancaire | 6 | openfire:2, sellsy:2, axonaut:1, costructor:1 | rapprochement bancaire (connexion, réconciliation, DSP2, instabilité)<br>rapprochement bancaire / transaction<br>rapprochement bancaire (comptes d'attente, lettrage)<br>rapprochement bancaire (lettrage manuel)<br>rapprochement bancaire (accès, privilèges) | axonaut:etat-tresorerie-temps-reel/rapprochement-bancaire-comment-ca-marche.md<br>costructor:gestion-dentreprise/comment-justifier-une-transaction-bancaire-7y52fe.md<br>openfire:configurer-openfire/configurez-vos-regles-de-rapprochement-bancaire.md<br>openfire:utiliser-openfire/realisez-vos-rapprochements-bancaires.md<br>sellsy:suivi-financier/donner-a-mes-collaborateurs-un-acces-au-module-rapprochement-bancaire.md | indetermine:4, facturation:2 |
| taux de tva | 6 | sellsy:2, axonaut:1, costructor:1, extrabat:1, openfire:1 | taux de TVA (ajout, TVA intracommunautaire)<br>taux de TVA (modification sur document)<br>taux de TVA (changement réglementaire)<br>taux de TVA (prestation, mobile)<br>taux de TVA | axonaut:gerez-vos-factures/ajouter-des-taux-de-tva.md<br>costructor:ventes/comment-modifier-le-taux-de-tva-dun-document-y36yd8.md<br>extrabat:changement-de-taux-de-tva-au-1er-janvier-2014.md<br>openfire:guides-videos/modifier-le-taux-de-tva-d-une-prestation-sur-mobile.md<br>sellsy:catalogue-produits-et-services/ajouter-un-taux-de-tva.md | indetermine:4, facturation:2 |
| compte bancaire | 5 | inter-fast:2, sellsy:2, costructor:1 | compte bancaire (rapprochement)<br>compte bancaire (connexion Powens, DSP2, migration Ponto)<br>compte bancaire (dissociation, révocation)<br>compte bancaire (synchronisation)<br>compte bancaire (connexion, banques spécifiques) | costructor:debuter-sur-costructor/comment-connecter-son-compte-bancaire-xupyjb.md<br>inter-fast:inter-fast/finances/connecter-mon-compte-bancaire.md<br>inter-fast:inter-fast/finances/dissocier-mon-compte-bancaire.md<br>sellsy:suivi-financier/connecter-mon-compte-bancaire-en-synchronisation.md<br>sellsy:suivi-financier/connecter-un-compte-bancaire-societe-generale-credit-agricole-caisse-d-epargne.md | indetermine:5 |
| configuration smtp | 5 | extrabat:5 | configuration SMTP (Yahoo)<br>configuration SMTP (personnalisé)<br>configuration SMTP (Brevo)<br>configuration SMTP (boîte mail personnalisée)<br>configuration SMTP (Gmail) | extrabat:configuration-smtp-extrabat-avec-yahoo.md<br>extrabat:configuration-smtp-extrabat.md<br>extrabat:e-mailing.md<br>extrabat:je-veux-envoyer-des-mails-a-partir-dextrabat-mais-avec-ma-boite-mail.md<br>extrabat:parametrer-son-smtp-extrabat-avec-son-compte-gmail.md | indetermine:5 |
| dépense | 5 | inter-fast:3, axonaut:2 | dépense (OCR, devise, récurrence)<br>dépense (ajout via app mobile, OCR justificatifs)<br>dépense (ajout, app web)<br>dépense (modification, allocation chantier)<br>dépense / paiement | axonaut:creez-depenses-facilement/ajouter-une-depense.md<br>inter-fast:inter-fast/application-mobile/ajouter-une-depense-app-mobile.md<br>inter-fast:inter-fast/finances/ajouter-une-depense-app-web.md<br>inter-fast:inter-fast/finances/modifier-une-depense.md<br>axonaut:creez-depenses-facilement/ajouter-un-paiement-sur-une-depense.md | achat:4, indetermine:1 |
| facture proforma | 5 | axonaut:1, costructor:1, extrabat:1, inter-fast:1, obat:1 | facture proforma (devis/douane/financement, création depuis commande)<br>facture proforma / devis en brouillon (filigrane)<br>facture proforma<br>facture proforma (création, transformation en facture officielle) | axonaut:gerez-vos-factures/facture-proforma.md<br>costructor:ventes/comment-imprimerenvoyer-une-facture-proforma-ou-un-devis-en-brouillon-yme5bk.md<br>extrabat:comment-creer-une-facture-proforma.md<br>inter-fast:inter-fast/finances/creer-une-facture-proforma.md<br>obat:`comment-faire-une-facture-proforma-avec-obat.md` | devis:2, indetermine:1, facturation:2 |
| fiche fournisseur | 5 | axonaut:1, inter-fast:1, openfire:1, progbat:1, sellsy:1 | fiche fournisseur (échanges, commandes, fusion de doublons)<br>fiche fournisseur (informations, dépenses, commandes)<br>fiche fournisseur (règles d'import automatique de factures)<br>fiche fournisseur (informations, adresses, contacts, conditions de règlement, activité, ProGBox)<br>fiche fournisseur (présentation complète) | axonaut:optimisez-gestion-commerciale/la-fiche-fournisseur.md<br>inter-fast:inter-fast/outils/comprendre-la-fiche-d-un-fournisseur.md<br>openfire:configurer-openfire/configurer-les-regles-d-import-de-facture-sur-la-fiche-fournisseur.md<br>progbat:le-menu-principal/contacts/fournisseurs/la-fiche-fournisseur.md<br>sellsy:repertoire/societes-presentation-de-la-fiche-fournisseur.md | achat:4, indetermine:1 |
| fournisseur | 5 | progbat:2, batikko:1, extrabat:1, costructor:1 | fournisseur (base fournisseurs, OCR, recherche GPS)<br>fournisseur (ajout à un article)<br>fournisseur (fichier fournisseurs, achats, livraisons, factures d'achat)<br>fournisseur (création, depuis commande/facture ou liste)<br>fournisseur / sous-traitant | batikko:guides/fournisseurs.md<br>extrabat:rajouter-un-fournisseur-a-un-article.md<br>progbat:le-menu-principal/contacts/fournisseurs.md<br>progbat:le-menu-principal/contacts/fournisseurs/creer-un-fournisseur.md<br>costructor:achats/comment-creer-un-fournisseur-sous-traitant-1cubnry.md | achat:4, indetermine:1 |
| ia | 5 | sellsy:5 | IA (édition commentaires / notes)<br>IA (campagnes emailing, édition texte)<br>IA (modèles email intelligents)<br>IA (rédaction / édition emails)<br>IA (résumé fiche client) | sellsy:sellsy-ia/editeur-ia-ameliorer-la-prise-de-notes-avec-sellsy-ia.md<br>sellsy:sellsy-ia/editeur-ia-ameliorez-vos-campagnes-emailing-avec-sellsy-ia.md<br>sellsy:sellsy-ia/modeles-d-emails-ia-generer-des-messages-cibles-avec-sellsy-ia.md<br>sellsy:sellsy-ia/redacteur-et-editeur-ia-rediger-des-emails-avec-sellsy-ia.md<br>sellsy:sellsy-ia/resumes-client-ia-resumer-une-fiche-client-en-un-clic-avec-sellsy-ia.md | indetermine:5 |
| ouvrage | 5 | extrabat:2, progbat:2, obat:1 | ouvrage (suppression)<br>ouvrage (renommage)<br>ouvrage (fourniture/main d'œuvre) sur devis/factures<br>ouvrage (bibliothèque, prestation vendue au client)<br>ouvrage (création, mise à jour, gestion depuis devis et bibliothèque) | extrabat:comment-supprimer-un-ouvrage.md<br>extrabat:renommer-un-ouvrage.md<br>obat:`comment-ajouter-un-ouvrage-sur-vos-devis/factures.md`<br>progbat:le-menu-principal/bibliotheque/ouvrages.md<br>progbat:le-menu-principal/bibliotheque/ouvrages/gestion-des-ouvrages.md | indetermine:2, devis:3 |
| photo | 5 | extrabat:4, vertuoza:1 | photo (prise depuis rendez-vous, porte-documents)<br>photo (annotation, géolocalisation, Extrabat Today)<br>photo (suivi de chantier, sélectionnabilité limitée dans le temps) | extrabat:espace-client.md<br>extrabat:je-veux-geolocaliser-ma-photo-et-annoter-ma-photo.md<br>extrabat:je-veux-prendre-une-photo-avec-extrabat-today.md<br>extrabat:tablette-smartphone.md<br>vertuoza:vertuoza/faq-foires-aux-questions/pourquoi-je-ne-peux-pas-recuperer-certaines-photos-ajoutees-par-mes-chefs-d-equipe-dans-les-suivis-gestionnaires.md | chantier-intervention:5 |
| planning | 5 | openfire:2, batikko:1, obat:1, progbat:1 | planning (calendrier, Gantt, équipes)<br>planning (page de catégorie)<br>planning (vues : planning/calendrier/liste/carte, filtres)<br>planning (vues disponibles)<br>planning (chantiers, phases, personnel) | batikko:guides/planning.md<br>obat:`planning.md`<br>openfire:knowsystem/affichage-du-planning-79.md<br>openfire:guides-videos/decouvrir-les-differentes-vues-du-planning.md<br>progbat:le-menu-principal/chantiers-personnel/planning.md | chantier-intervention:5 |
| société | 5 | sellsy:4, axonaut:1 | société/contact (fiche, catégorisation auto, unicité particulier)<br>société (visualisation carte, mobile)<br>société (enrichissement via annuaire)<br>société (vue carte)<br>société (suppression / archivage) | axonaut:optimisez-gestion-commerciale/comment-creer-une-societe-dans-axonaut.md<br>sellsy:app-mobile-sellsy-crm/app-sellsy-crm-visualiser-les-societes-sur-une-carte.md<br>sellsy:repertoire/enrichir-les-donnees-d-une-societe-existante.md<br>sellsy:repertoire/repertoire-voir-les-societes-sur-une-carte.md<br>sellsy:repertoire/societes-supprimer-ou-archiver-des-societes.md | indetermine:5 |
| time tracking | 5 | sellsy:5 | time tracking (ticket support)<br>time tracking (fonctionnement)<br>time tracking (saisie hebdomadaire)<br>time tracking (saisie rapide)<br>time tracking (suivi heures collaborateurs) | sellsy:crm-et-prospection/ajouter-une-entree-de-time-tracking-sur-un-ticket-de-support.md<br>sellsy:crm-et-prospection/fonctionnement-et-utilisation-du-timetracking.md<br>sellsy:crm-et-prospection/saisie-hebdomadaire-des-heures-sur-timetracking.md<br>sellsy:crm-et-prospection/saisie-rapide-d-un-temps.md<br>sellsy:crm-et-prospection/suivre-les-heures-effectuees-par-mes-collaborateurs-grace-au-time-tracking.md | indetermine:5 |

### 3.2 Racines à fréquence moyenne (2 à 4 occurrences — 199 racines)

| Racine | Occ. | Concurrents | Exemple(s) représentatif(s) | Chemin représentatif |
|---|---:|---|---|---|
| agenda | 4 | sellsy:2, costructor:1, extrabat:1 | agenda (synchronisation Google Agenda); agenda (modification RDV, sélection utilisateur) | costructor:debuter-sur-costructor/comment-synchroniser-lagenda-costructor-avec-google-agenda-7f0syd.md |
| avoir | 4 | axonaut:1, extrabat:1, openfire:1, sellsy:1 | avoir (global/partiel/fournisseur, suppression encadrée de facture); avoir (création, transformation facture) | axonaut:gerez-vos-factures/comment-faire-un-avoir-sur-axonaut.md |
| cgv | 4 | sellsy:2, costructor:1, inter-fast:1 | CGV (conditions générales de vente); CGV (paramétrage, import, rédaction) | costructor:debuter-sur-costructor/inserer-mes-cgv-conditions-generales-de-ventes-vk2gwi.md |
| code comptable | 4 | sellsy:4 | code comptable (plan comptable); code comptable (remises) | sellsy:suivi-financier/ajouter-des-codes-comptables-au-plan-comptable.md |
| commentaires | 4 | sellsy:3, inter-fast:1 | commentaires (collaboration interne/externe, mentions); commentaires (import) | inter-fast:inter-fast/application-web/collaborer-avec-les-commentaires.md |
| connexion | 4 | openfire:2, sellsy:2 | connexion (application mobile); connexion (application web, base test/production) | openfire:bien-debuter/se-connecter-a-l-application-mobile.md |
| gestion de stock | 4 | axonaut:1, costructor:1, openfire:1, progbat:1 | gestion de stock (fabrication, bons de livraison, réception, location); gestion de stock / produit | axonaut:gerez-stock-temps-reel/comment-ca-marche-la-gestion-de-stock.md |
| intégration comptable | 4 | batikko:3, costructor:1 | intégration comptable (ACD i-Suite Expert); intégration comptable (Pennylane) | batikko:guides/connexion-acd.md |
| mandat pa | 4 | sellsy:4 | mandat PA (émission + réception, facturation électronique); mandat PA (émission, facturation électronique) | sellsy:facturation-electronique/completer-le-mandat-d-emission-et-de-reception-sur-la-plateforme-sellsy-pa.md |
| modèle de courrier | 4 | extrabat:4 | modèle de courrier (création); modèle de courrier (import Word/OpenOffice, marqueurs) | extrabat:creer-modele-de-courrier.md |
| moteur de recherche | 4 | extrabat:4 | moteur de recherche (optimisation, critères); moteur de recherche (personnalisation nom/prénom) | extrabat:moteur-de-recherche-plus-rapide.md |
| paiement | 4 | openfire:2, extrabat:1, inter-fast:1 | paiement (lettrage); paiement (consignation, suppression, cas particuliers) | extrabat:comment-effectuer-un-paiement-en-passant-par-le-lettrage.md |
| pièce commerciale | 4 | extrabat:4 | pièce commerciale (jointe à un SAV); pièce commerciale (duplication) | extrabat:comment-joindre-une-piece-commerciale-a-un-sav.md |
| remise en banque | 4 | extrabat:3, sellsy:1 | remise en banque (annulation); remise en banque (simplifiée) | extrabat:annuler-une-remise-en-banque.md |
| smart tag | 4 | sellsy:4 | smart tag (fiche client); smart tag (filtrage) | sellsy:gestion-des-donnees/ajouter-ou-supprimer-un-smart-tag.md |
| achats | 3 | axonaut:1, obat:1, sellsy:1 | achats (fournisseurs, dépenses, commandes, notes de frais, indemnités km); achats/bons de commande/rentabilité (page de catégorie) | axonaut:creez-depenses-facilement/comment-ca-marche-achats.md |
| affaire | 3 | extrabat:3 | affaire (bonnes pratiques, gestion); affaire (création, association pièces commerciales) | extrabat:bonnes-regles-afin-de-creer-affaire-de-gerer.md |
| assistant devis vocal | 3 | obat:3 | assistant devis vocal (option abonnement); assistant devis vocal (page de catégorie) | obat:`activation-de-lassistant-devis-vocal.md` |
| bibliothèque | 3 | extrabat:1, obat:1, progbat:1 | bibliothèque (signature utilisateur, recherche transversale — agrégat); bibliothèque (page de catégorie) | extrabat:tag/bibliotheque.md |
| ca restant à facturer | 3 | extrabat:3 | CA restant à facturer (rapport) | extrabat:ca-restant-a-facturer.md |
| calcul de marge | 3 | costructor:1, obat:1, sellsy:1 | calcul de marge (option devis brouillon); calcul de marge (devis) | costructor:ventes/comment-activer-le-calcul-des-marges-vv5czm.md |
| campagne emailing | 3 | axonaut:2, sellsy:1 | campagne emailing (ciblage, coût, opt-out, verrouillage post-envoi); campagne emailing (template externe, opt-out, verrouillage post-envoi) | axonaut:creez-campagnes-marketing/creer-une-campagne-emailing-a-partir-dun-template-axonaut.md |
| catégorie tarifaire | 3 | sellsy:3 | catégorie tarifaire; catégorie tarifaire (import, catalogue services) | sellsy:catalogue-produits-et-services/utiliser-les-categories-tarifaires.md |
| contacts | 3 | obat:1, progbat:1, sellsy:1 | contacts (page de catégorie); contacts (catégories : clients, prospects, fournisseurs, sous-traitants) | obat:`contacts.md` |
| demande d'intervention | 3 | openfire:3 | demande d'intervention (visibilité portail client); demande d'intervention (SAV/entretien, portail client) | openfire:configurer-openfire/gerer-l-affichage-et-le-partage-des-demandes-d-intervention-di-sur-le-portail-client.md |
| document de vente | 3 | sellsy:3 | document de vente (création : devis / facture); document de vente (fusion) | sellsy:documents-de-vente/creer-une-facture-un-devis-un-document-de-vente.md |
| double authentification | 3 | sellsy:3 | double authentification (administrateur); double authentification (utilisateur) | sellsy:conseils-d-utilisation/configurer-la-double-authentification-en-tant-qu-administrateur.md |
| facture d'abonnement | 3 | costructor:1, inter-fast:1, sellsy:1 | facture d'abonnement; facture d'abonnement (téléchargement) | costructor:abonnement/telecharger-les-factures-dabonnement-costructor-1cmafv1.md |
| facture d'achat | 3 | progbat:1, sellsy:1, costructor:1 | facture d'achat (moyens d'intégration : saisie, photo, PDP); facture d'achat (devise étrangère) | progbat:le-menu-principal/depenses/factures-dachat.md |
| factures | 3 | inter-fast:1, obat:1, sellsy:1 | factures (tableau, filtres, colonnes); factures (page de catégorie) | inter-fast:inter-fast/finances/comprendre-le-tableau-des-factures.md |
| fichier csv | 3 | sellsy:3 | fichier CSV (ouverture, Excel); fichier CSV (ouverture, Google Sheets) | sellsy:gestion-des-donnees/ouvrir-un-fichier-csv-avec-excel.md |
| gestion des stocks | 3 | obat:2, inter-fast:1 | gestion des stocks (emplacements, produits, décrémentation, export); gestion des stocks (page de catégorie) | inter-fast:inter-fast/outils/gerer-les-stocks-app-web.md |
| géolocalisation | 3 | extrabat:2, openfire:1 | géolocalisation (carte fiche client); géolocalisation (contacts) | extrabat:faire-apparaitre-la-carte-sur-la-page-daccueil-du-client.md |
| import de devis | 3 | progbat:2, costructor:1 | import de devis (DPGF/DQE, Excel/PDF); import de devis/factures (migration depuis ancien système) | costructor:imports-exports/comment-importer-un-devis-dpgf-dqe-excelpdf-1btrzbp.md |
| import de template email | 3 | axonaut:3 | import de template email (Mailchimp, conversion HTML); import de template email (Sendinblue, code HTML) | axonaut:creez-campagnes-marketing/campagne-emailing-importer-mon-template-mailchimp.md |
| impression | 3 | extrabat:3 | impression (bug plugin Firefox, contournement); impression (extension JS Print, autoriser accès) | extrabat:gestion-commerciale/impression.md |
| informations société | 3 | sellsy:3 | informations société; informations société (conformité facturation électronique) | sellsy:configuration-du-compte/parametrer-les-informations-de-ma-societe.md |
| interface de caisse | 3 | extrabat:3 | interface de caisse (sélections produits); interface de caisse (paramétrage, Extrabat Piscine) | extrabat:afficher-des-produits-sur-linterface-de-caisse.md |
| intégration install bois | 3 | extrabat:3 | intégration Install Bois (Extrabat Chauffage) | extrabat:assistance.md |
| inventaire | 3 | extrabat:3 | inventaire (stock) | extrabat:faire-un-inventaire.md |
| ligne de devis | 3 | progbat:3 | ligne de devis (création : titre, sous-titre, prestation, commentaire, saut de page); ligne de devis (fonctionnalités avancées : dupliquer, déplacer, afficher composition) | progbat:le-menu-principal/devis-factures/devis/les-lignes-du-devis/creer-une-ligne-de-devis.md |
| marge | 3 | costructor:1, progbat:1, sellsy:1 | marge / prix (ajustement en masse sur devis); marge (concept de marge brute, calcul, mise à jour de la bibliothèque) | costructor:ventes/comment-ajuster-la-marge-ou-les-prix-dun-devis-1pvn0w4.md |
| modèle de document | 3 | extrabat:1, progbat:1, sellsy:1 | modèle de document (duplication); modèle de document (personnalisation : sections, tags, conditions, mise en forme) | extrabat:comment-dupliquer-un-modele-de-document.md |
| modèle de message | 3 | extrabat:3 | modèle de message (email personnalisé); modèle de message (création/utilisation) | extrabat:comment-creer-un-modele-de-message.md |
| moyen de paiement | 3 | costructor:1, obat:1, sellsy:1 | moyen de paiement (abonnement); moyen de paiement (correction, rapprochement bancaire) | costructor:abonnement/comment-mettre-a-jour-son-moyen-de-paiement-6rwou1.md |
| paramétrage navigateur | 3 | extrabat:3 | paramétrage navigateur (Firefox); paramétrage navigateur (Firefox, onglets favoris) | extrabat:bien-parametrer-firefox.md |
| pipeline | 3 | sellsy:3 | pipeline (affichage); pipeline (création) | sellsy:crm-et-prospection/afficher-ou-masquer-un-pipeline.md |
| plan comptable | 3 | axonaut:1, costructor:1, openfire:1 | plan comptable (saisie manuelle ou import massif); plan comptable / comptes auxiliaires | axonaut:gerez-votre-comptabilite/saisir-ou-importer-mon-plan-comptable-dans-axonaut.md |
| planning chantier | 3 | extrabat:2, inter-fast:1 | planning chantier (création/gestion, bonnes règles); planning chantier (visualisation, planification, personnalisation affichage) | extrabat:les-bonnes-regles-afin-de-creer-gerer-son-planning-chantier.md |
| produit centralisé | 3 | openfire:3 | produit centralisé (import dans devis); produit centralisé (import dans kit) | openfire:guides-videos/importer-un-produit-centralise-dans-un-devis.md |
| raccourci écran d'accueil | 3 | extrabat:3 | raccourci écran d'accueil (Android); raccourci écran d'accueil (Apple) | extrabat:comment-creer-raccourci-sur-ma-tablette-android.md |
| rapport crm | 3 | sellsy:3 | rapport CRM (activités); rapport CRM (par collaborateur) | sellsy:rapports-et-pilotage/rapport-rapport-d-activite-crm-par-activites.md |
| rapport d'intervention | 3 | extrabat:2, inter-fast:1 | rapport d'intervention (Extrabat Today); rapport d'intervention (technicien, mobile) | extrabat:je-veux-rentrer-un-rapport-dintervention-sur-extrabat-today.md |
| rapports d'intervention et signatures | 3 | extrabat:3 | rapports d'intervention et signatures (Extrabat Today) | extrabat:les-rapports-dintervention-et-les-signatures-sur-extrabat-today.md |
| sav | 3 | extrabat:2, openfire:1 | SAV (enregistrement); SAV (enregistrement + planification RDV) | extrabat:comment-enregistrer-sav.md |
| tarif centralisé | 3 | openfire:3 | tarif centralisé (accès, recherche d'articles); tarif centralisé (accès catalogues fournisseurs) | openfire:knowsystem/acceder-aux-tarifs-centralises-152.md |
| tournée | 3 | openfire:3 | tournée (optimisation); tournée (remplissage automatique) | openfire:guides-videos/optimiser-et-re-organiser-les-tournees.md |
| trésorerie | 3 | sellsy:2, axonaut:1 | trésorerie (intégration, prévisionnel); trésorerie (pilotage financier) | sellsy:module-tresorerie/sellsy-tresorerie-fonctionnement.md |
| tva | 3 | sellsy:2, progbat:1 | TVA (taux, mentions légales); TVA / réforme facturation électronique (exclusions, activités mixtes) | progbat:pour-bien-demarrer/parametrage/parametres-de-lentreprise/tva.md |
| utilisateur | 3 | axonaut:1, extrabat:1, progbat:1 | utilisateur (ajout/suppression/réactivation, message d'erreur email); utilisateur (ajout) | axonaut:configurer-votre-compte/ajouter-un-utilisateur-dans-axonaut.md |
| variantes de devis | 3 | obat:2, inter-fast:1 | variantes de devis (création, envoi, acceptation); variantes de devis | inter-fast:inter-fast/finances/creer-et-gerer-des-variantes-de-devis.md |
| widget | 3 | sellsy:3 | widget (création, site web); widget (installation site web) | sellsy:integrations-et-api/creer-et-personnaliser-mon-premier-widget.md |
| éditeur de style | 3 | obat:2, extrabat:1 | éditeur de style (devis/commande/facture); éditeur de style (masquage) | extrabat:inserer-ligne-dans-devis-commande-facture.md |
| acompte | 2 | openfire:2 | acompte (facture); acompte (produit, catégorie comptable, TVA) | openfire:knowsystem/comment-generer-un-acompte-202.md |
| action | 2 | extrabat:2 | action (fiche client, attribution); action (paramétrage, réponses) | extrabat:attribuer-action-a-collaborateur.md |
| actions en masse | 2 | extrabat:1, sellsy:1 | actions en masse (pièces commerciales); actions en masse (rapprochement bancaire) | extrabat:beaucoup-dactions-passent-par-la-case-a-cocher-afin-de.md |
| adresse | 2 | openfire:1, sellsy:1 | adresse / contact secondaire; adresse (fiche société) | openfire:utiliser-openfire/creer-une-adresse-ou-un-contact-secondaire.md |
| annuaire des sociétés | 2 | sellsy:2 | annuaire des sociétés (fiches enrichies, SIRENE); annuaire des sociétés (introduction, config) | sellsy:repertoire/annuaire-des-societes-creer-des-fiches-societes-enrichies.md |
| apparence de document | 2 | sellsy:2 | apparence de document (personnalisation); apparence de document (langue) | sellsy:documents-de-vente/creer-une-apparence-de-document-vente-et-achat.md |
| application extrabat today v3.5 | 2 | extrabat:2 | application Extrabat Today v3.5 (nouveautés) | extrabat:application.md |
| application extradoc | 2 | extrabat:2 | application ExtraDoc (GED mobile) | extrabat:application-extradoc.md |
| attestation de conformité | 2 | progbat:2 | attestation de conformité (anti-fraude TVA); attestation de conformité (paramétrage entreprise, génération) | progbat:conformite/attestation-de-conformite.md |
| balance âgée | 2 | openfire:1, sellsy:1 | balance âgée (rapport créances/dettes); balance âgée (créances / dettes) | openfire:knowsystem/balance-agee-274.md |
| bibliothèque de prix tierce | 2 | progbat:2 | bibliothèque de prix tierce (BatiChiffrage©, intégration); bibliothèque de prix tierce (BatiChiffrage©, paramétrage des prix) | progbat:le-menu-principal/bibliotheque/batichiffrage-c.md |
| bon de commande | 2 | openfire:1, sellsy:1 | bon de commande (facturation, acompte/solde); bon de commande | openfire:utiliser-openfire/facturer-vos-bons-de-commande-client.md |
| bon de commande v1 | 2 | inter-fast:2 | bon de commande V1 (création, suivi, statuts); bon de commande V1 (création) | inter-fast:inter-fast/finances/creer-et-gerer-vos-achats-avec-le-module-commandes-v1.md |
| bonnes pratiques | 2 | extrabat:2 | bonnes pratiques (auto-diagnostic d'utilisation); bonnes pratiques (saisie, sécurité, plugins) | extrabat:faites-le-test-avez-vous-les-bons-reflexes-extrabat.md |
| bordereau de chantier | 2 | costructor:1, obat:1 | bordereau de chantier | costructor:chantiers/comment-creer-un-bordereau-de-chantier-1492z8v.md |
| bouteille de fluide | 2 | inter-fast:1, openfire:1 | bouteille de fluide (enregistrement, app mobile); bouteille de fluide (suivi, mouvements, import initial) | inter-fast:inter-fast/fluides-frigorigenes/enregistrer-une-bouteille-de-fluide-app-mobile.md |
| bsff | 2 | inter-fast:2 | BSFF (remplissage complet, cycle de vie, Trackdéchets); BSFF (checklist de dépannage, erreurs courantes) | inter-fast:inter-fast/fluides-frigorigenes/remplir-un-bsff.md |
| calcul de déperdition de chaleur | 2 | openfire:2 | calcul de déperdition de chaleur (dimensionnement, formule); calcul de déperdition de chaleur (dimensionnement) | openfire:knowsystem/calculateur-de-deperdition-de-chaleur-80.md |
| calcul du montant d'une commande sous-traitant liée à une facture fournisseur | 2 | vertuoza:2 | calcul du montant d'une commande sous-traitant liée à une facture fournisseur | vertuoza:faq-foires-aux-questions/comment-est-calcule-le-montant-d-une-commande-de-sous-traitant-lorsque-celle-ci-est-associee-a-une-facture-fournisseur-348427.md |
| catalogue produits | 2 | openfire:1, sellsy:1 | catalogue produits (Tarif Centralisé, fabricant → distributeurs); catalogue produits (import) | openfire:configurer-openfire/fabricant-mettre-a-disposition-mon-catalogue-de-produits-sur-le-tarif-centralise-openfire-pour-mes-distributeurs.md |
| cerfa 15497 | 2 | inter-fast:1, openfire:1 | CERFA 15497 (remplissage, pré-requis, modification); Cerfa 15497 (fluides frigorigènes, mobile) | inter-fast:inter-fast/fluides-frigorigenes/remplir-le-cerfa-15497.md |
| checklist fin d'année | 2 | extrabat:2 | checklist fin d'année (clôture comptable) | extrabat:checklist-de-fin-dannee-extrabat.md |
| code client | 2 | extrabat:2 | code client/comptable (création automatique); code client (conflit, doublon) | extrabat:comment-le-code-client-ou-code-comptable-se-cree.md |
| commandes v2 | 2 | inter-fast:2 | commandes V2 (tableau, filtres, colonnes); commandes V2 (création, réception, validation, liaison chantier) | inter-fast:inter-fast/finances/comprendre-le-tableau-des-commandes-v2.md |
| comptabilité | 2 | obat:1, progbat:1 | comptabilité (page de catégorie); comptabilité (export, connexion expert-comptable) | obat:`comptabilit-c3-a9.md` |
| compte de charge | 2 | progbat:2 | compte de charge/produit par famille métier (résolution en cascade); compte de charge/produit par type d'élément (résolution en cascade, compte par fournisseur) | progbat:le-menu-principal/comptabilite/parametrage-comptable/comptes-de-charge-et-produit-par-famille-metier.md |
| compte utilisateur | 2 | extrabat:1, openfire:1 | compte utilisateur (suppression d'accès); compte utilisateur (profil, notifications, sécurité) | extrabat:supprimer-un-compte-utilisateur.md |
| conditions de paiement | 2 | inter-fast:1, sellsy:1 | conditions de paiement (configuration générale et par client); conditions de paiement (document de vente) | inter-fast:inter-fast/mon-entreprise/configurer-des-conditions-de-paiement.md |
| conditions générales de vente | 2 | obat:2 | conditions générales de vente (CGV); conditions générales de vente (CGV) BTP | obat:`comment-acc-c3-a9der-et-param-c3-a9trer-vos-conditions-g-c3-a9n-c3-a9rales-de-vente-sur-obat.md` |
| connecteur d'achat | 2 | openfire:2 | connecteur d'achat (Altema/Modinox); connecteur d'achat (Poujoulat) | openfire:knowsystem/commande-directe-achat-site-altema-215.md |
| connecteur wizville | 2 | openfire:2 | connecteur Wizville (enquête satisfaction, marque Jøtul); connecteur Wizville (export/import avis clients) | openfire:configurer-openfire/configurer-le-connecteur-wizville-j-tul.md |
| connecteurs d'achat | 2 | openfire:2 | connecteurs d'achat (commandes fournisseurs multi-fournisseurs); connecteurs d'achat (utilisation, multi-fournisseurs) | openfire:configurer-openfire/configurer-les-connecteurs-d-achat-pour-passer-mes-commandes-fournisseurs.md |
| connexion bancaire | 2 | obat:1, sellsy:1 | connexion bancaire (Bridge API); connexion bancaire (dépannage) | obat:`comment-connecter-votre-banque-sur-obat.md` |
| contrat | 2 | openfire:2 | contrat (génération devis/factures récurrentes ou à la prestation); contrat (génération DI, suivi planification) | openfire:utiliser-openfire/contrat-avance-generer-vos-devis-et-vos-factures.md |
| contrat de maintenance | 2 | openfire:1, progbat:1 | contrat de maintenance (avancé, facturation/planification); contrat de maintenance (création, reconduction, consultation) | openfire:utiliser-openfire/contrat-avance-creer-vos-contrats-de-maintenance-et-d-entretien.md |
| création d'une note de crédit | 2 | vertuoza:2 | création d'une note de crédit/avoir selon le type de facture; création d'une note de crédit (depuis le menu ou depuis une facture existante) | vertuoza:faq-foires-aux-questions/comment-puis-je-creer-une-note-de-credit-avoir-pour-une-facture.md |
| distinction reste à produire | 2 | vertuoza:2 | distinction reste à produire / reste à facturer et procédure de résolution; distinction reste à produire / reste à facturer (définition courte) | vertuoza:faq-foires-aux-questions/quelle-est-la-difference-entre-le-reste-a-produire-et-le-reste-a-facturer-dans-vertuoza.md |
| document | 2 | sellsy:2 | document (création dans une autre langue); document (introduction traduction, 5 étapes) | sellsy:documents-de-vente/etape-6-creer-le-document-dans-une-autre-langue.md |
| documentation | 2 | extrabat:1, progbat:1 | documentation (liaison à un article); documentation / recherche (méta) | extrabat:attacher-une-documentation-a-un-article.md |
| débours | 2 | axonaut:1, costructor:1 | débours / note de débit (produit hors CA); débours (ajustement net à payer) | axonaut:gerez-vos-factures/creer-un-debours-ou-note-de-debit-dans-axonaut.md |
| décompte général | 2 | costructor:1, obat:1 | décompte général (DGD) sur facture de situation; décompte général (récapitulatif chantier) | costructor:ventes/comment-afficher-le-decompte-general-sur-une-facture-de-situation-h7074x.md |
| dépannage d'ajout d'un compte chantier au planning d'intervention | 2 | vertuoza:2 | dépannage d'ajout d'un compte chantier au planning d'intervention (droits responsable) | vertuoza:faq-foires-aux-questions/pourquoi-je-n-arrive-pas-a-ajouter-un-compte-chantier-dans-le-planning-d-intervention-348328.md |
| dépenses | 2 | inter-fast:1, progbat:1 | dépenses (tableau, filtres, exports); dépenses (achats, commandes, livraisons, factures d'achat) | inter-fast:inter-fast/finances/comprendre-le-tableau-des-depenses.md |
| en-tête planning | 2 | extrabat:2 | en-tête planning (figer) | extrabat:commnet-figer-len-tete-des-taches-planning.md |
| espace client | 2 | extrabat:1, sellsy:1 | espace client (accès, mot de passe); espace client | extrabat:mon-client-ne-peut-pas-aller-sur-son-espace-client.md |
| exercice comptable | 2 | extrabat:1, openfire:1 | exercice comptable (création); exercice comptable / période (création, génération auto) | extrabat:comment-creer-un-nouvel-exercice-comptable.md |
| export comptable | 2 | obat:1, progbat:1 | export comptable / comptes auxiliaires; export comptable (journal des ventes/achats/règlements) | obat:`export-comptable-et-comptes-auxiliaires-sur-obat.md` |
| export de données | 2 | axonaut:1, sellsy:1 | export de données (Excel, contacts/factures/produits); export de données (CSV/PDF/JSON/PARQUET) | axonaut:configurer-votre-compte/exporter-ses-donnees-depuis-axonaut.md |
| extension chrome | 2 | inter-fast:1, obat:1 | extension Chrome (import d'articles depuis sites fournisseurs); extension Chrome (copie fiches produits) | inter-fast:inter-fast/application-web/installer-l-extension-chrome.md |
| extension navigateur | 2 | axonaut:1, obat:1 | extension navigateur (import contact depuis Gmail/Outlook); extension navigateur (copie fiches produits fournisseurs) | axonaut:centralisez-gestion-emails-courriers/comment-ajouter-un-contact-depuis-gmail-ou-outlook.md |
| facturation d'un avenant validé | 2 | vertuoza:2 | facturation d'un avenant validé (avancement à 100%) | vertuoza:faq-foires-aux-questions/comment-facturer-un-avenant-une-fois-qu-il-est-valide.md |
| facturation d'une intervention | 2 | inter-fast:1, vertuoza:1 | facturation d'une intervention (app web/mobile); facturation d'une intervention (rapport → facture) | inter-fast:inter-fast/finances/facturer-une-intervention-depuis-l-application-web-et-mobile.md |
| facturation électronique obligatoire | 2 | obat:2 | facturation électronique obligatoire (Belgique, Peppol); facturation électronique obligatoire (France, PPF/Iopole) | obat:`facturation-electronique-obligatoire-en-belgique-des-2026.md` |
| facture d'avancement | 2 | axonaut:1, sellsy:1 | facture d'avancement / de situation (avancement cumulé, verrouillage prévisionnel); facture d'avancement (chantier long) | axonaut:gerez-vos-factures/comment-creer-une-facture-davancement-dans-axonaut.md |
| facture de situation | 2 | costructor:1, obat:1 | facture de situation / d'avancement (transition depuis devis); facture de situation | costructor:ventes/comment-creer-une-facture-de-situation-1ptizga.md |
| factures fournisseurs | 2 | inter-fast:1, sellsy:1 | factures fournisseurs (personnalisation présentation, numérotation); factures fournisseurs (module Achats) | inter-fast:inter-fast/finances/personnaliser-mes-factures-fournisseurs.md |
| feuille d'heures | 2 | costructor:2 | feuille d'heures / temps de travail; feuille d'heures / modèle | costructor:equipe-collaborateurs/comment-utiliser-les-feuilles-dheures-ypj0g5.md |
| fiche contact | 2 | obat:1, sellsy:1 | fiche contact / accès depuis panneaux; fiche contact (présentation complète) | obat:`accedez-a-vos-contacts-en-un-clic-depuis-vos-chantiers-devis-ou-factures.md` |
| fiche produit | 2 | inter-fast:1, openfire:1 | fiche produit (stock, mouvements, alarmes, bibliothèque); fiche produit (configuration achats/stocks) | inter-fast:inter-fast/outils/comprendre-la-fiche-d-un-produit.md |
| fiche prospect | 2 | inter-fast:1, sellsy:1 | fiche prospect (informations, conversion en client, équipements); fiche prospect (présentation complète) | inter-fast:inter-fast/outils/comprendre-la-fiche-d-un-prospect.md |
| fiche répertoire | 2 | sellsy:2 | fiche répertoire (client/prospect/fournisseur); fiche répertoire (modification) | sellsy:app-mobile-sellsy-crm/app-sellsy-crm-creer-un-client-prospect-ou-fournisseur.md |
| fichier | 2 | sellsy:2 | fichier (répertoire, mobile); fichier (ajout, gestion documentaire) | sellsy:app-mobile-sellsy-crm/app-sellsy-crm-importer-et-classer-vos-fichiers-sur-notre-application-mobile.md |
| financement client | 2 | extrabat:2 | financement client (partenariat Franfinance) | extrabat:infos.md |
| fond de caisse | 2 | extrabat:2 | fond de caisse (comptage fin de journée); fond de caisse (paramétrage + saisie) | extrabat:compter-caisse-fin-de-journee.md |
| fournisseurs | 2 | extrabat:1, inter-fast:1 | fournisseurs (fusion doublons); fournisseurs (fiches, gestion CRM, app mobile) | extrabat:fusionner-des-fournisseurs.md |
| gestion des achats | 2 | obat:2 | gestion des achats (suivi et règlements); gestion des achats/rentabilité/marge (chantier) | obat:`comment-suivre-vos-achats-avec-obat-et-g-c3-a9rer-leurs-r-c3-a8glements.md` |
| horaires | 2 | openfire:1, progbat:1 | horaires (techniciens); horaires (entreprise, prime repas) | openfire:guides-videos/gerer-les-horaires-des-techniciens.md |
| identifiants de connexion | 2 | costructor:1, obat:1 | identifiants de connexion (email/mot de passe); identifiants de connexion | costructor:securite/comment-modifier-son-adresse-mail-de-connexion-son-mot-de-passe-175htc3.md |
| import de contacts | 2 | progbat:1, vertuoza:1 | import de contacts (fichier Excel/CSV); import de contacts/entreprises depuis un fichier Excel (template) | progbat:pour-bien-demarrer/demarrer-avec-progbat/importer-mes-contacts.md |
| intervention | 2 | openfire:2 | intervention (multi-équipements, mobile); intervention (planning, champs complets) | openfire:guides-videos/creer-ou-realiser-une-intervention-avec-plusieurs-equipements.md |
| intégration batiprix | 2 | inter-fast:1, vertuoza:1 | intégration Batiprix (bibliothèque d'ouvrages dans les devis); intégration Batiprix (connexion, recherche et import d'ouvrages dans les devis) | inter-fast:inter-fast/mon-entreprise/connecter-batiprix-a-interfast.md |
| journal d'achats | 2 | inter-fast:1, openfire:1 | journal d'achats (export comptable, justificatifs); journal d'achats (association adresse annuaire) | inter-fast:inter-fast/mon-entreprise/exporter-son-journal-d-achats.md |
| liste factures | 2 | extrabat:2 | liste factures (soldées/non soldées); liste factures (impression) | extrabat:comment-faire-apparaitre-la-liste-des-factures-soldees-ou-non.md |
| marketplace | 2 | obat:2 | marketplace (leads chantiers); Marketplace (page de catégorie) | obat:`comment-trouver-un-chantier-sur-la-marketplace-obat.md` |
| mentions légales | 2 | costructor:1, sellsy:1 | mentions légales (documents); mentions légales (document de vente) | costructor:debuter-sur-costructor/comment-modifier-les-mentions-legales-de-mes-documents-1r8xgyu.md |
| migration de données | 2 | costructor:1, inter-fast:1 | migration de données (guide agrégateur, multi-objets); migration de données (accompagnement gratuit/payant, changement de logiciel) | costructor:imports-exports/comment-migrer-mes-donnees-dun-autre-logiciel-sur-costructor-1l718d6.md |
| mode de règlement | 2 | extrabat:2 | mode de règlement (création); mode de règlement (exclusion de la liste des relances) | extrabat:creer-nouveau-mode-de-reglement.md |
| multi-entreprise | 2 | costructor:1, inter-fast:1 | multi-entreprise / abonnement; multi-entreprise (basculement, création, coûts) | costructor:abonnement/comment-ajouter-une-seconde-entreprise-c2jr6v.md |
| newsletter produit | 2 | openfire:2 | newsletter produit (nouveautés) | openfire:bien-debuter/newsletter-openfire-avril-2025.md |
| notifications | 2 | inter-fast:1, sellsy:1 | notifications (app mobile, paramétrage, types, traitement); notifications (fonctionnement / réglages) | inter-fast:inter-fast/application-mobile/consulter-mes-notifications-app-mobile.md |
| onboarding | 2 | sellsy:1, progbat:1 | onboarding (parcours de démarrage); onboarding / import de données | sellsy:conseils-d-utilisation/bien-demarrer-avec-sellsy.md |
| opportunités | 2 | sellsy:2 | opportunités / pipeline (intro module); opportunités (import) | sellsy:app-mobile-sellsy-crm/app-sellsy-crm-introduction-gestion-des-opportunites-et-pipeline.md |
| page d'accueil | 2 | batikko:1, progbat:1 | page d'accueil / sommaire des fonctionnalités; page d'accueil (tableau de bord, onglets, accès rapides, menu général) | batikko:index.md |
| page partenaires | 2 | obat:2 | page partenaires (offres, experts-comptables); page partenaires (filtrage assistants administratifs) | obat:`la-page-partenaires.md` |
| pdf | 2 | sellsy:2 | PDF (insertion document Redactor); PDF (export documents) | sellsy:crm-et-prospection/inserer-un-pdf-dans-un-document-redactor.md |
| pilotage | 2 | costructor:1, obat:1 | pilotage (ventes/achats/trésorerie); pilotage (page de catégorie) | costructor:gestion-dentreprise/comment-fonctionne-le-pilotage-fm83ry.md |
| planning de chantier | 2 | costructor:1, progbat:1 | planning de chantier / tâche / lot / jalon; planning de chantier (phases, dépendances type Gantt) | costructor:chantiers/comment-creer-un-planning-de-chantier-s6jnge.md |
| plus | 2 | obat:2 | plus/moins-values (factures de situation détaillées) | obat:`gerez-vos-plus-et-moins-values-facilement-dans-les-factures-de-situation-detaillees.md` |
| portail client | 2 | axonaut:1, inter-fast:1 | portail client (signature, paiement, espace collaboratif); portail client (accès, visibilité, signature électronique, demandes en ligne) | axonaut:gerez-vos-devis/le-portail-client-axonaut-comment-ca-marche.md |
| postes libres ht | 2 | obat:2 | postes libres HT; postes libres HT/TTC (améliorations) | obat:`comment-ajouter-des-postes-libres-ht-sur-vos-devis-et-factures.md` |
| postman | 2 | sellsy:2 | Postman (configuration API V1); Postman (configuration API V2) | sellsy:integrations-et-api/configuration-postman-api-v1.md |
| profil de privilèges | 2 | sellsy:2 | profil de privilèges; profil de privilèges (définition) | sellsy:configuration-du-compte/gerer-les-profils-de-privileges-de-mes-collaborateurs.md |
| profil utilisateur | 2 | inter-fast:1, progbat:1 | profil utilisateur (app mobile, paramétrage et navigation); profil utilisateur (identifiant de connexion, mot de passe) | inter-fast:inter-fast/application-mobile/consulter-mon-profil-app-mobile.md |
| programme de parrainage | 2 | inter-fast:1, obat:1 | programme de parrainage (lien, avantages, crédits); programme de parrainage | inter-fast:inter-fast/mon-entreprise/parrainer-un-artisan-sur-interfast.md |
| promotion | 2 | sellsy:2 | promotion (catalogue); promotion (gestion / application) | sellsy:catalogue-produits-et-services/creer-des-promotions.md |
| prospect | 2 | progbat:1, axonaut:1 | prospect (distinction client/prospect); prospect / dépense (ajout par email) | progbat:le-menu-principal/contacts/prospects.md |
| préférences utilisateur | 2 | extrabat:1, openfire:1 | préférences utilisateur (personnalisation globale); préférences utilisateur (mobile) | extrabat:je-veux-personnaliser-mes-preferences-utilisateurs.md |
| prélèvement sepa | 2 | openfire:1, sellsy:1 | prélèvement SEPA (mandats, ordres de paiement); prélèvement SEPA (mandat, export) | openfire:configurer-openfire/configurer-les-prelevements-sepa.md |
| qr codes | 2 | inter-fast:2 | QR codes (association et scan d'actifs physiques, app mobile); QR codes (création, association, utilisation mobile) | inter-fast:inter-fast/application-mobile/scanner-les-qr-codes-app-mobile.md |
| raccourcis | 2 | extrabat:2 | raccourcis (moteur de recherche) | extrabat:les-raccourcis-du-moteur-de-recherche.md |
| recherche | 2 | openfire:1, sellsy:1 | recherche / filtres / regroupement; recherche (barre de recherche) | openfire:bien-debuter/recherche-filtre-et-regroupement-de-donnees.md |
| recherche devis | 2 | obat:2 | recherche devis/factures/chantiers; recherche devis / configuration chantier (planning) | obat:`comment-retrouver-facilement-un-devis-ou-une-facture-sur-obat.md` |
| relance | 2 | sellsy:2 | relance (consultation par document); relance (introduction, méthodes) | sellsy:documents-de-vente/etape-3-consulter-les-relances-liees-a-un-document.md |
| relance automatique | 2 | sellsy:2 | relance automatique (activation); relance automatique (personnalisation par client) | sellsy:documents-de-vente/etape-1-activer-la-relance-automatique.md |
| relance devis | 2 | extrabat:2 | relance devis (SMS, réponse client) | extrabat:relance-des-devis-par-sms.md |
| relevé bancaire | 2 | openfire:1, sellsy:1 | relevé bancaire (intégration, import); relevé bancaire (import CSV) | openfire:utiliser-openfire/integrez-vos-releves-bancaire-dans-openfire.md |
| remboursement client | 2 | extrabat:1, sellsy:1 | remboursement client (espèces, interface caisse); remboursement client (avoir) | extrabat:je-veux-rembourser-un-client-en-especes-par-linterface-de-caisse.md |
| remise | 2 | openfire:1, sellsy:1 | remise (rendez-vous, mobile); remise (document de vente) | openfire:guides-videos/appliquer-une-remise-sur-un-rendez-vous-sur-mobile.md |
| remise globale | 2 | obat:1, openfire:1 | remise globale/ligne par ligne; remise globale (devis) | obat:`comment-ajouter-une-remise-globale-ou-ligne-par-ligne-sur-vos-devis/factures.md` |
| retenue de garantie | 2 | costructor:1, obat:1 | retenue de garantie (RG); retenue de garantie | costructor:ventes/comment-ajouter-une-retenue-de-garantie-tp6j75.md |
| rgpd | 2 | extrabat:2 | RGPD (droits utilisateurs, gestion données personnelles) | extrabat:le-rgpd-tout-savoir-sur-le-reglement-general-sur-la-protection-des-donnees.md |
| règlement facture | 2 | extrabat:2 | règlement facture (enregistrement); règlement facture (espace client, multi-modes) | extrabat:enregistrer-reglement.md |
| règlements | 2 | progbat:1, sellsy:1 | règlements (encaissement clients, paiement fournisseurs, retenue de garantie); règlements (paramétrage : moyens / libellés / conditions) | progbat:le-menu-principal/reglements.md |
| récupération du lien de connexion à l'espace entreprise | 2 | vertuoza:2 | récupération du lien de connexion à l'espace entreprise (tenant ID) | vertuoza:faq-foires-aux-questions/comment-retrouver-mon-lien-de-connexion-a-l-espace-entreprise-354012.md |
| répertoire | 2 | sellsy:2 | répertoire (intro module); répertoire (contacts / sociétés / particuliers, statuts) | sellsy:app-mobile-sellsy-crm/app-sellsy-crm-introduction-gestion-du-repertoire.md |
| serveur smtp | 2 | axonaut:2 | serveur SMTP (envoi d'emails, multi-fournisseurs); serveur SMTP (Mailjet, authentification domaine) | axonaut:centralisez-gestion-emails-courriers/configurer-lenvoi-demails-depuis-axonaut.md |
| service | 2 | extrabat:2 | service (suppression); service (enregistrement + planification RDV) | extrabat:comment-supprimer-un-service.md |
| signature email | 2 | axonaut:1, sellsy:1 | signature email (texte, champs dynamiques, image); signature email | axonaut:configurer-votre-compte/comment-creer-sa-signature-e-mail-dans-axonaut.md |
| signatures électroniques | 2 | extrabat:2 | signatures électroniques (accès Oodrive) | extrabat:astuces.md |
| site internet | 2 | batikko:1, costructor:1 | site internet (vitrine, personnalisation); site internet (vitrine) | batikko:guides/site-internet.md |
| suivi de chantier | 2 | vertuoza:2 | suivi de chantier (remarque interne, photos) sur mobile; suivi de chantier (avancement / réclamation) | vertuoza:application-mobile/ouvrier-realiser-un-suivi-de-chantier.md |
| suivi des appels | 2 | sellsy:2 | suivi des appels (configuration); suivi des appels (module) | sellsy:crm-et-prospection/configurer-le-suivi-des-appels.md |
| support | 2 | extrabat:1, openfire:1 | support/assistance (migration vers Zendesk); support (contact) | extrabat:migration-du-support-vers-zendesk.md |
| support client | 2 | inter-fast:2 | support client (accès et fonctionnement, app mobile); support client (philosophie, canaux, académie vidéo) | inter-fast:inter-fast/application-mobile/acceder-au-support-client-app-mobile.md |
| synchronisation calendrier | 2 | obat:2 | synchronisation calendrier (Google); synchronisation calendrier (Google/Outlook/iCal) | obat:`comment-synchroniser-son-calendrier-obat-avec-son-calendrier-google.md` |
| tag | 2 | extrabat:2 | tag (bibliothèque, porte-documents) | extrabat:biblitoheque.md |
| taxe | 2 | openfire:2 | taxe (TVA, groupes de taxes); taxe / TVA (fiscalité) | openfire:configurer-openfire/configuration-des-taxes.md |
| ticket de support | 2 | openfire:1, sellsy:1 | ticket de support / priorité d'incident; ticket de support / contact | openfire:bien-debuter/comment-indiquer-le-niveau-de-priorite-de-mon-probleme-quand-je-contacte-openfire.md |
| transfert d'appels | 2 | obat:2 | transfert d'appels (répondeur intelligent); transfert d'appels (injoignabilité) | obat:`comment-transferer-vos-appels-vers-le-repondeur-intelligent.md` |
| tâche | 2 | axonaut:1, sellsy:1 | tâche (affectation, statut, portail client); tâche (usage) | axonaut:gerez-rentabilite-projets/comment-creer-une-tache.md |
| valorisation de stock | 2 | extrabat:1, sellsy:1 | valorisation de stock (export à date); valorisation de stock (CMUP) | extrabat:voir-valorisation-de-stock-a-date.md |
| widget notifications | 2 | extrabat:2 | widget notifications (Extrabat Today) | extrabat:un-nouveau-widget-notifications.md |
| écritures comptables | 2 | extrabat:1, sellsy:1 | écritures comptables (suppression, sauvegarde préalable); écritures comptables (export CSV / FEC / JSON / PARQUET) | extrabat:supprimer-ecritures-comptabilite.md |
| éléments de fourniture | 2 | obat:2 | éléments de fourniture / main d'œuvre sur devis-factures; éléments de fourniture/main d'œuvre/ouvrage sur facture | obat:`comment-ajouter-des-c3-a9l-c3-a9ments-de-fourniture-et-de-main-d-c5-93uvre-c3-a0-vos-devis/factures.md` |
| équipement | 2 | openfire:2 | équipement (création, mobile); équipement (consultation portail client) | openfire:guides-videos/creer-un-equipement-sur-mobile.md |
| étiquettes articles | 2 | extrabat:2 | étiquettes articles (export/impression); étiquettes articles (impression via Excel/Word, bon de réception) | extrabat:faire-etiquettes-articles.md |

### 3.3 Racines uniques (1 occurrence — 1624 racines)

Liste exhaustive, triée par ordre alphabétique de racine. Chaque racine de
cette section n'apparaît qu'une seule fois dans tout le corpus LIGHT, chez un
seul concurrent. Individuellement, aucune ne permet de conclure à une
tendance ; collectivement, elles forment la réserve où des concepts encore
non regroupés peuvent apparaître (à consulter en recherche libre plutôt qu'en
lecture linéaire).

| Racine | Concurrent | Valeur exacte unique | Chemin | moment_parcours |
|---|---|---|---|---|
| 2fa | sellsy | 2FA (obligation facturation électronique) | sellsy:facturation-electronique/activation-de-la-double-authentification-pour-la-facturation-electronique.md | indetermine |
| abonnement bibliothèque batichiffrage | obat | abonnement bibliothèque Batichiffrage | obat:`comment-sabonner-c3-a0-batichiffrage-sur-obat.md` | indetermine |
| absence de liaison automatique des rapports d'intervention aux factures groupées | vertuoza | absence de liaison automatique des rapports d'intervention aux factures groupées | vertuoza:faq-foires-aux-questions/pourquoi-les-rapports-d-interventions-ne-sont-ils-pas-automatiquement-lies-aux-factures-globales.md | facturation |
| absence de module trésorerie natif | vertuoza | absence de module trésorerie natif (intégrations tierces pour paiements/comptabilité/PEPPOL) | vertuoza:faq-foires-aux-questions/vertuoza-propose-t-il-un-logiciel-de-tresorerie-integre.md | facturation |
| absence de valeur légale probante de la signature électronique gratuite | vertuoza | absence de valeur légale probante de la signature électronique gratuite | vertuoza:faq-foires-aux-questions/le-systeme-de-signature-electronique-gratuite-a-t-il-une-valeur-legale-en-cas-de-litige.md | devis |
| académie vidéo | inter-fast | académie vidéo (accès et navigation, formation) | inter-fast:inter-fast/debuter-avec-interfast/maitrisez-interfast-grace-a-l-academie-video.md | indetermine |
| acceptation | axonaut | acceptation/refus de devis (transition en commande) | axonaut:gerez-vos-devis/accepter-refuser-un-devis.md | devis |
| accessibilité hors ligne | obat | accessibilité hors ligne (FAQ) | obat:`obat-est-il-accessible-hors-ligne.md` | indetermine |
| accompagnement 30 jours | inter-fast | accompagnement 30 jours (sessions live d'onboarding) | inter-fast:inter-fast/debuter-avec-interfast/debuter-votre-accompagnement-30-jours.md | indetermine |
| accusé de réception | extrabat | accusé de réception (email) | extrabat:accuse-de-reception-sur-les-e-mails-envoyes-par-extrabat.md | indetermine |
| accès api | sellsy | accès API (types, scopes) | sellsy:integrations-et-api/types-d-acces-api.md | indetermine |
| accès expert-comptable | sellsy | accès expert-comptable | sellsy:configuration-du-compte/donner-un-acces-sellsy-a-mon-expert-comptable.md | indetermine |
| accès module achats | sellsy | accès module achats (privilèges) | sellsy:module-achats/gestion-des-acces-au-module-achats-pour-les-utilisateurs.md | achat |
| accès rapides | progbat | accès rapides (recherche, raccourcis de consultation/création, multi-comptes) | progbat:presentation-generale/les-acces-rapides.md | indetermine |
| achat de packs de licences utilisateurs | obat | achat de packs de licences utilisateurs | obat:`lachat-de-packs-de-licences-utilisateurs-sur-obat.md` | indetermine |
| achat groupé de licences utilisateurs | obat | achat groupé de licences utilisateurs | obat:`gagnez-du-temps-avec-lachat-de-packs-de-licences-utilisateurs-sur-obat.md` | indetermine |
| achat rapide | sellsy | achat rapide (saisie manuelle) | sellsy:module-achats/enregistrer-des-achats-rapides.md | indetermine |
| acompte au prorata | costructor | acompte au prorata (déduction sur facture de situation) | costructor:ventes/comment-deduire-un-acompte-au-prorata-lwkl1w.md | facturation |
| acompte et solde | axonaut | acompte et solde (facture partielle, déduction automatique) | axonaut:gerez-vos-factures/faire-un-acompte-sur-axonaut.md | facturation |
| activation de l'affichage des prix | vertuoza | activation de l'affichage des prix (régie/forfait) pour un responsable d'intervention | vertuoza:faq-foires-aux-questions/comment-puis-je-afficher-l-option-permettant-de-selectionner-regie-ou-forfait-lors-de-la-creation-d-une-intervention-via-l-acces-chantier.md | chantier-intervention |
| activation de l'option enveloppe à fenêtre sur un modèle de devis 2 colonnes | vertuoza | activation de l'option enveloppe à fenêtre sur un modèle de devis 2 colonnes | vertuoza:parametres/comment-activer-l-option-enveloppe-a-fenetre.md | devis |
| activation de la facturation électronique | vertuoza | activation de la facturation électronique (Peppol, vérification d'identité KYC) | vertuoza:parametres/comment-activer-la-facturation-electronique.md | facturation |
| activation de la facturation électronique peppol | vertuoza | activation de la facturation électronique PEPPOL | vertuoza:faq-foires-aux-questions/comment-activer-la-facturation-electronique-peppol-dans-vertuoza.md | facturation |
| activation de la numérotation des lignes de devis | vertuoza | activation de la numérotation des lignes de devis | vertuoza:faq-foires-aux-questions/comment-numeroter-des-lignes-dans-un-devis.md | devis |
| activation de plusieurs taux de tva sur un devis | vertuoza | activation de plusieurs taux de TVA sur un devis (TVA à la ligne) | vertuoza:faq-foires-aux-questions/est-il-possible-d-avoir-2-taux-de-tva-sur-un-devis.md | devis |
| activation des frais kilométriques pour les interventions | vertuoza | activation des frais kilométriques pour les interventions | vertuoza:faq-foires-aux-questions/comment-puis-je-entrer-les-frais-kilometriques-pour-mes-interventions.md | chantier-intervention |
| activation des préférences d'affichage pour un devis | vertuoza | activation des préférences d'affichage pour un devis | vertuoza:faq-foires-aux-questions/comment-activer-les-preferences-d-affichage-pour-un-devis.md | devis |
| activation des quantités présumées | vertuoza | activation des quantités présumées (QP) sur un devis | vertuoza:faq-foires-aux-questions/comment-activer-les-quantites-presumees-qp.md | devis |
| activation du module de pointage | vertuoza | activation du module de pointage (temps de travail) | vertuoza:faq-foires-aux-questions/comment-puis-je-activer-la-gestion-du-pointage.md | indetermine |
| activation et configuration des listes de prix | openfire | activation et configuration des listes de prix | openfire:knowsystem/gerer-les-listes-de-prix-150.md | devis |
| activation et fonctionnement de la qr-facture suisse | vertuoza | activation et fonctionnement de la QR-facture suisse (obligation légale) | vertuoza:finance/facture-suisse-activer-la-qr-facture.md | facturation |
| activation et utilisation des pistes commerciales avant conversion en opportunités | openfire | activation et utilisation des pistes commerciales avant conversion en opportunités | openfire:knowsystem/utiliser-les-pistes-127.md | demande |
| activation javascript | extrabat | activation JavaScript (Android) | extrabat:comment-activer-javascript-sous-android.md | indetermine |
| activation ou désactivation d'un modèle de devis | vertuoza | activation ou désactivation d'un modèle de devis | vertuoza:parametres/gestion-des-modeles-activer-ou-desactiver-un-modele-de-devis.md | devis |
| activité | sellsy | activité (répertoire) | sellsy:app-mobile-sellsy-crm/app-sellsy-crm-ajouter-une-activite-sur-une-fiche-du-repertoire.md | indetermine |
| activités | sellsy | activités (liste tâches/appels) | sellsy:crm-et-prospection/liste-d-activite.md | indetermine |
| actualisation des prix de lignes sélectionnées dans un devis | vertuoza | actualisation des prix de lignes sélectionnées dans un devis | vertuoza:faq-foires-aux-questions/comment-actualiser-les-prix-depuis-un-devis-en-selectionnant-uniquement-certaines-lignes.md | devis |
| adresse d'envoi fixe des avenants | vertuoza | adresse d'envoi fixe des avenants (adresse client, non modifiable) | vertuoza:faq-foires-aux-questions/pourquoi-les-avenants-sont-ils-envoyes-a-l-adresse-du-client-et-non-a-l-adresse-de-facturation-et-est-il-possible-de-changer-cela.md | chantier-intervention |
| adresse de facturation électronique | sellsy | adresse de facturation électronique (concept) | sellsy:facturation-electronique/comprendre-l-adresse-de-facturation-electronique.md | indetermine |
| adresse e-mail client | extrabat | adresse e-mail client (contrôle qualité fichier) | extrabat:fichier-e-mail-jour.md | indetermine |
| adresse par défaut | extrabat | adresse par défaut (pièces fournisseur) | extrabat:comment-attribuer-une-adresse-par-defaut-pour-les-pieces-type-fournisseur.md | achat |
| adresses de l'entreprise | progbat | adresses de l'entreprise (siège social, établissements/dépôts) | progbat:pour-bien-demarrer/parametrage/parametres-de-lentreprise/adresses.md | indetermine |
| affectation de personnel | progbat | affectation de personnel (phases de chantier, planning) | progbat:le-menu-principal/chantiers-personnel/planning/affecter-du-personnel.md | chantier-intervention |
| affectation stock | extrabat | affectation stock (article) | extrabat:avoir-en-temps-reel-sur-un-article-toutes-ses-affectations-reassort-reserve-a-commander.md | indetermine |
| affichage coordonnées client sur documents | obat | affichage coordonnées client sur documents | obat:`comment-afficher-les-coordonn-c3-a9es-de-vos-clients-sur-vos-documents.md` | devis |
| affichage d'une révision de prix avec totaux avant | vertuoza | affichage d'une révision de prix avec totaux avant/après sur un devis | vertuoza:faq-foires-aux-questions/comment-effectuer-une-revision-sur-un-devis-avec-des-totaux-avant-et-apres-revision.md | devis |
| affichage des prévisions météo par chantier dans le planning | vertuoza | affichage des prévisions météo par chantier dans le planning | vertuoza:planning/fonctionnement-de-la-meteo-dans-le-planning.md | chantier-intervention |
| affichage références articles sur devis | obat | affichage références articles sur devis | obat:`comment-afficher-les-r-c3-a9f-c3-a9rences-das-articles-sur-le-devis.md` | devis |
| affichage sans fil | openfire | affichage sans fil (Windows Connect, mobile) | openfire:knowsystem/configuration-connect-affichage-sans-fil-windows-242.md | indetermine |
| affichage sav | extrabat | affichage SAV (page d'accueil) | extrabat:amelioration-affichage-sav-sur-page-daccueil.md | chantier-intervention |
| agences | inter-fast | agences (multi-établissement, comptabilité analytique) | inter-fast:inter-fast/equipe/configurer-et-gerer-vos-agences.md | indetermine |
| agenda externe | inter-fast | agenda externe (import iCal dans InterFast) | inter-fast:inter-fast/equipe/integrer-un-agenda-dans-le-calendrier-interfast.md | indetermine |
| agent ia conversationnel | costructor | agent IA conversationnel (assistant intégré) | costructor:gestion-dentreprise/comment-utiliser-lia-conversationnelle-1h3my79.md | indetermine |
| aide contextuelle à la recherche | obat | aide contextuelle à la recherche (listes) | obat:`nouvelle-aide-c3-a0-la-recherche-sur-obat-gagnez-du-temps-et-exploitez-tout-le-potentiel-de-votre-logiciel.md` | indetermine |
| aide obat | obat | aide Obat (page d'accueil) | obat:`index.md` | indetermine |
| ajout automatique d'un chantier au planning à l'acceptation du devis | vertuoza | ajout automatique d'un chantier au planning à l'acceptation du devis | vertuoza:planning/comment-ajouter-un-chantier-au-planning.md | chantier-intervention |
| ajout client sur devis | obat | ajout client sur devis/facture | obat:`comment-ajouter-un-client-c3-a0-votre-devis/factures.md` | devis |
| ajout clients | inter-fast | ajout clients/prospects/fournisseurs/contacts (CRM) | inter-fast:inter-fast/outils/ajouter-des-clients-prospects-fournisseurs.md | indetermine |
| ajout d'un chantier depuis un devis | obat | ajout d'un chantier depuis un devis | obat:`comment-ajouter-un-chantier-sur-obat.md` | devis |
| ajout d'un sous-traitant à un chantier | vertuoza | ajout d'un sous-traitant à un chantier/planning | vertuoza:faq-foires-aux-questions/comment-ajouter-un-sous-traitant-a-un-planning.md | chantier-intervention |
| ajout d'une mention descriptive au taux de tva affichée sur les documents | vertuoza | ajout d'une mention descriptive au taux de TVA affichée sur les documents | vertuoza:faq-foires-aux-questions/comment-ajouter-une-mention-de-tva-sur-les-documents.md | indetermine |
| ajout d'une prime déduite du montant ttc sur une offre | vertuoza | ajout d'une prime déduite du montant TTC sur une offre | vertuoza:documents/prime.md | devis |
| ajout de commentaires | vertuoza | ajout de commentaires (notes, email, appel, RDV) sur un document | vertuoza:documents/commentaires.md | indetermine |
| ajout de rendez-vous d'entretien véhicule dans le planning | vertuoza | ajout de rendez-vous d'entretien véhicule dans le planning (type « autre entrée ») | vertuoza:faq-foires-aux-questions/est-il-possible-dans-le-planning-d-indiquer-les-rdv-des-vehicules-pour-entretien-ou-reparation.md | chantier-intervention |
| ajustement des prix batiprix | vertuoza | ajustement des prix Batiprix (main-d'œuvre) selon les réalités belges | vertuoza:faq-foires-aux-questions/comment-adapter-les-prix-batiprix-aux-realites-belges-et-encoder-une-adresse-belge-dans-le-systeme-de-facturation.md | devis |
| ajustement ht | costructor | ajustement HT / net à payer (devis ou facture) | costructor:ventes/comment-realiser-un-ajustement-ht-sur-le-net-a-payer-1h2vz89.md | indetermine |
| ajustement ttc | obat | ajustement TTC (postes complémentaires) | obat:`ajustez-facilement-vos-factures-avec-le-nouvel-ajustement-ttc.md` | facturation |
| alarmes rdv | extrabat | alarmes RDV/intervention | extrabat:alarmes-pour-les-rdv.md | chantier-intervention |
| alerte planning | extrabat | alerte planning (widget, texte d'alerte) | extrabat:je-veux-creer-une-alerte-planning.md | chantier-intervention |
| alerte stock | sellsy | alerte stock (commandes fournisseur) | sellsy:module-stocks/alertes-stock-et-commandes-fournisseur.md | indetermine |
| alerte sécurité rib | extrabat | alerte sécurité RIB | extrabat:alerte-en-cas-dajout-ou-suppression-de-rib.md | indetermine |
| amortissement | openfire | amortissement (immobilisations, méthodes de calcul) | openfire:knowsystem/amortissements-224.md | indetermine |
| analyse des tunnels de conversion commerciale | openfire | analyse des tunnels de conversion commerciale (Quali, Quanti, objectifs) | openfire:knowsystem/le-tunnel-de-conversion-149.md | demande |
| analyse des ventes et devis via tableau croisé dynamique | openfire | analyse des ventes et devis via tableau croisé dynamique | openfire:knowsystem/rapport-des-ventes-142.md | demande |
| analyse du chiffre d'affaires facturé | openfire | analyse du chiffre d'affaires facturé (rapport) | openfire:knowsystem/analyse-ca-facture-280.md | facturation |
| annuaire | openfire | annuaire (lignes multiples, SUPER PDP, facturation électronique) | openfire:configurer-openfire/configurer-plusieurs-lignes-d-annuaire-dans-super-pdp-pour-votre-propre-entreprise.md | facturation |
| annuaire national | openfire | annuaire national (synchronisation données légales partenaires) | openfire:configurer-openfire/activer-parametrer-et-utiliser-l-annuaire-national.md | indetermine |
| annulation d'une facture d'acompte | vertuoza | annulation d'une facture d'acompte (note de crédit) | vertuoza:faq-foires-aux-questions/comment-annuler-une-facture-d-acompte.md | facturation |
| annulation de facture | costructor | annulation de facture (avoir total) | costructor:ventes/comment-annuler-une-facture-vb12e9.md | facturation |
| annulation facture | obat | annulation facture / avoir obligatoire | obat:`annuler-une-facture-sans-cr-c3-a9er-un-avoir-ce-nest-plus-possible.md` | facturation |
| api | sellsy | API (introduction, choix version) | sellsy:integrations-et-api/introduction-api.md | indetermine |
| api rest interfast | inter-fast | API REST InterFast (documentation, authentification, différences MCP) | inter-fast:inter-fast/mon-entreprise/utiliser-l-api-d-interfast.md | indetermine |
| api v1 | sellsy | API V1 (documentation, tokens) | sellsy:integrations-et-api/api-v1.md | indetermine |
| api v1 via v2 | sellsy | API V1 via V2 (compatibilité) | sellsy:integrations-et-api/utiliser-l-api-v1-via-des-acces-api-v2.md | indetermine |
| api v2 | sellsy | API V2 (documentation, tokens, scopes) | sellsy:integrations-et-api/api-v2.md | indetermine |
| apparence | obat | apparence/présentation devis | obat:`comment-modifier-l-apparence-dun-devis-sur-obat.md` | devis |
| application d'un escompte | vertuoza | application d'un escompte (comportement de calcul actuel, contournement) | vertuoza:faq-foires-aux-questions/comment-appliquer-un-escompte-correctement-dans-l-application.md | facturation |
| application d'un prorata sur un sous-total de l'offre | vertuoza | application d'un prorata sur un sous-total de l'offre | vertuoza:documents/prorata.md | devis |
| application d'une remise globale sur un devis | vertuoza | application d'une remise globale sur un devis | vertuoza:documents/remise-globale.md | devis |
| application d'une remise sur une ligne de devis | vertuoza | application d'une remise sur une ligne de devis | vertuoza:documents/remise-a-la-ligne.md | devis |
| application d'une retenue sur le sous-total d'une offre | vertuoza | application d'une retenue sur le sous-total d'une offre | vertuoza:documents/retenue.md | devis |
| application de coefficients de révision de prix sur des lignes de devis | vertuoza | application de coefficients de révision de prix sur des lignes de devis | vertuoza:gestion-de-chantier/formules-de-revisions.md | devis |
| application de gestion | inter-fast | application de gestion (installation PWA, iOS/Android) | inter-fast:inter-fast/application-mobile/telecharger-l-application-de-gestion.md | indetermine |
| application desktop | costructor | application desktop (PWA) | costructor:debuter-sur-costructor/telecharger-lapplication-costructor-sur-ordinateur-18x4qxr.md | indetermine |
| application extrabat today | extrabat | application Extrabat Today (téléchargement, géolocalisation RDV) | extrabat:extrabat-today-telechargeable-sur-lapple-store.md | chantier-intervention |
| application mobile extrabat today | extrabat | application mobile Extrabat Today | extrabat:application-extrabat-today.md | chantier-intervention |
| application openfire | openfire | application OpenFire (présentation générale) | openfire:guides-videos/decouvrir-l-application-openfire.md | indetermine |
| application terrain | inter-fast | application terrain (installation, connexion, mode hors-ligne) | inter-fast:inter-fast/application-mobile/telecharger-l-application-terrain.md | chantier-intervention |
| applications | inter-fast | applications (web, PWA, terrain — installation par plateforme) | inter-fast:inter-fast/debuter-avec-interfast/decouvrir-l-application-web-et-mobile-pour-les-smartphones.md | indetermine |
| approvisionnement en exception | openfire | approvisionnement en exception (erreurs de traitement) | openfire:knowsystem/approvisionnement-en-exeption-252.md | achat |
| approvisionnement intersociété | openfire | approvisionnement intersociété (module, règles) | openfire:knowsystem/approvisionnement-intersociete-245.md | achat |
| approvisionnement à la contremarque | openfire | approvisionnement à la contremarque (achat lié à vente) | openfire:utiliser-openfire/comment-realiser-un-approvisionnement-a-la-contremarque.md | achat |
| archivage | inter-fast | archivage/désarchivage d'un chantier (conservation de l'historique) | inter-fast:inter-fast/operations/archiver-desarchiver-un-chantier.md | chantier-intervention |
| archivage d'un client | inter-fast | archivage d'un client (CRM) | inter-fast:inter-fast/outils/archiver-un-client.md | indetermine |
| archivage et réactivation d'un chantier | vertuoza | archivage et réactivation d'un chantier | vertuoza:gestion-de-chantier/archiver-le-chantier.md | chantier-intervention |
| archives | progbat | archives (factures, archive fiscale NF-525) | progbat:le-menu-principal/comptabilite/archives.md | facturation |
| arrondis de tva | obat | arrondis de TVA (méthode de calcul) | obat:`les-arrondis-de-tva.md` | facturation |
| arrêt du développement du connecteur comptable winbizz | vertuoza | arrêt du développement du connecteur comptable Winbizz | vertuoza:faq-foires-aux-questions/que-devient-le-connecteur-avec-winbizz.md | indetermine |
| article centralisé | openfire | article centralisé (mise à jour tarifs, archivage) | openfire:mettre-a-jour-un-article-centralise.md | achat |
| article complémentaire | openfire | article complémentaire (facturation, mobile) | openfire:guides-videos/facturer-un-article-en-complement-de-ma-prestation-sur-mobile.md | facturation |
| article en option | extrabat | article en option (devis/commande/facture) | extrabat:mettre-un-article-en-option.md | devis |
| article inactif | extrabat | article inactif (recherche) | extrabat:rechercher-article-inactif-ou-desactive.md | indetermine |
| article texte | extrabat | article texte (sans prix/quantité) | extrabat:creer-un-article-texte-sans-prix-ni-quantite.md | devis |
| article vendu | extrabat | article vendu (recherche historique client) | extrabat:trouver-article-vendu-a-client.md | indetermine |
| articles | extrabat | articles (mise à jour en masse) | extrabat:mettre-a-jour-base-articles.md | indetermine |
| assistance | progbat | assistance (accès aux 3 services : documentation, tutos, support) | progbat:le-menu-principal/assistance.md | indetermine |
| assistant ia | sellsy | assistant IA / crédits IA | sellsy:sellsy-ia/decouvrir-sellsy-ia.md | indetermine |
| assistant ia « max » | inter-fast | assistant IA « Max » (support tchat, workflow, prompts) | inter-fast:inter-fast/debuter-avec-interfast/comment-utiliser-max-l-ia-dans-le-tchat.md | indetermine |
| assistant ia « za » | obat | assistant IA « Za » (page de catégorie) | obat:`lassistant-ia-dobat.md` | indetermine |
| assistant vocal ia pour créer devis et avenants depuis l'app mobile | vertuoza | assistant vocal IA pour créer devis et avenants depuis l'app mobile | vertuoza:application-mobile/gestionnaire-assistant-ia-pour-creer-vos-devis-et-avenant-sur-l-app-mobile.md | devis |
| association automatique des fournisseurs sur les factures reçues | vertuoza | association automatique des fournisseurs sur les factures reçues (TVA, ID PEPPOL) | vertuoza:faq-foires-aux-questions/comment-le-systeme-vertuoza-gere-t-il-les-fournisseurs-sur-les-factures-recues.md | achat |
| associations | sellsy | associations (TVA, réforme facturation électronique) | sellsy:facturation-electronique/associations-et-reforme-de-la-facturation-electronique.md | indetermine |
| assurance décennale | costructor | assurance décennale / mentions légales | costructor:debuter-sur-costructor/comment-ajouter-mon-assurance-sur-mes-documents-uv3nwc.md | indetermine |
| assurances et cgv | progbat | assurances et CGV (conditions générales de vente, mentions obligatoires) | progbat:pour-bien-demarrer/parametrage/parametres-de-lentreprise/assurances-et-conditions-generales.md | indetermine |
| astuces | extrabat | astuces (gain de temps, liste transversale) | extrabat:les-astuces-extrabat-gagner-du-temps.md | indetermine |
| astuces d'utilisation | obat | astuces d'utilisation (page de catégorie) | obat:`astuces.md` | indetermine |
| astuces navigateur et outils tiers | inter-fast | astuces navigateur et outils tiers (recommandations) | inter-fast:inter-fast/debuter-avec-interfast/decouvrir-les-petites-astuces-interfast.md | indetermine |
| attestation de tva | progbat | attestation de TVA (remplacement réglementaire, texte automatique dans le devis) | progbat:le-menu-principal/devis-factures/attestations-de-tva.md | devis |
| attestation de tva taux réduit | obat | attestation de TVA taux réduit | obat:`comment-g-c3-a9n-c3-a9rer-une-attestation-de-tva-sur-obat.md` | devis |
| attribution commercial | obat | attribution commercial (multi-utilisateur) | obat:`evolution-multiutilisateur-une-gestion-commerciale-encore-plus-precise-avec-obat-bientot-disponible.md` | indetermine |
| attribution du numéro de facture après comptabilisation | vertuoza | attribution du numéro de facture après comptabilisation | vertuoza:faq-foires-aux-questions/pourquoi-est-ce-que-ma-facture-n-a-pas-de-numero.md | facturation |
| authentification | costructor | authentification / sécurité du compte | costructor:securite/comment-activer-lauthentification-a-deux-facteurs-17ypgjk.md | indetermine |
| authentification azure | openfire | authentification Azure (Office 365, serveur mail) | openfire:knowsystem/authentification-azure-pour-office-365-294.md | indetermine |
| authentification multifacteur | progbat | authentification multifacteur (sécurité de connexion) | progbat:pour-bien-demarrer/parametrage/mon-profil/authentification-multifacteur.md | indetermine |
| authentification à deux facteurs | openfire | authentification à deux facteurs (2FA) | openfire:configurer-openfire/gerer-la-double-authentification.md | indetermine |
| autocomplétion d'adresse | openfire | autocomplétion d'adresse (fiche contact) | openfire:configurer-openfire/autocompleter-une-adresse-dans-une-fiche-contact.md | indetermine |
| autocomplétion données entreprise | obat | autocomplétion données entreprise (API SIRENE) | obat:`gagnez-du-temps-avec-lautocompl-c3-a9tion-des-entreprises-dans-obat.md` | indetermine |
| autoliquidation de la tva sur les commandes sous-traitants btp | vertuoza | autoliquidation de la TVA sur les commandes sous-traitants BTP (absence de TVA) | vertuoza:faq-foires-aux-questions/pourquoi-n-y-a-t-il-pas-de-tva-sur-mes-bons-de-commande-lorsque-je-fais-appel-a-un-sous-traitant-dans-le-secteur-du-batiment.md | achat |
| autoliquidation tva | obat | autoliquidation TVA (devis) | obat:`comment-passer-votre-devis-en-autoliquidation-sur-obat.md` | devis |
| automatisation commerciale | axonaut | automatisation commerciale (déclencheur/action, opportunités) | axonaut:optimisez-gestion-commerciale/automatisez-vos-actions-commerciales-avec-axonaut.md | indetermine |
| automatisation comptable | openfire | automatisation comptable (produits, catégories, taxes, positions fiscales) | openfire:configurer-openfire/introduction-aux-regles-d-automatisation-comptables-dans-openfire.md | indetermine |
| automatisation des demandes d'avis clients | inter-fast | automatisation des demandes d'avis clients (Eldo, Bilik, Google My Business) | inter-fast:inter-fast/outils/automatiser-les-demandes-d-avis-clients.md | facturation |
| automatisations | inter-fast | automatisations (actions et tâches, modèles, scénarios) | inter-fast:inter-fast/outils/automatiser-mes-actions-et-taches.md | indetermine |
| autres paramètres entreprise | progbat | autres paramètres entreprise (signature, validité devis, conditions de règlement, acomptes, pénalités) | progbat:pour-bien-demarrer/parametrage/parametres-de-lentreprise/autres-parametres.md | devis |
| avance de trésorerie | axonaut | avance de trésorerie (Defacto, éligibilité, statuts de financement) | axonaut:etat-tresorerie-temps-reel/comment-obtenir-une-avance-de-tresorerie.md | facturation |
| avance immédiate | axonaut | avance immédiate (API tiers de prestation URSSAF) | axonaut:connectez-axonaut/proposez-lavance-immediate-avec-axonaut.md | facturation |
| avenant | progbat | avenant (devis complémentaire en cours de chantier) | progbat:le-menu-principal/devis-factures/avenant.md | devis |
| avenant au devis | inter-fast | avenant au devis (plus/moins-values, facturation finale) | inter-fast:inter-fast/finances/creer-un-avenant-au-devis.md | chantier-intervention |
| avis clients via qr code | obat | avis clients via QR Code (E-Réputation) | obat:`collectez-des-avis-clients-sur-le-terrain-grace-au-qr-code.md` | chantier-intervention |
| avoir client | inter-fast | avoir client (création, méthodes, cas particuliers) | inter-fast:inter-fast/finances/creer-une-facture-d-avoir-client.md | facturation |
| avoir fournisseur | inter-fast | avoir fournisseur (enregistrement, suivi) | inter-fast:inter-fast/finances/enregistrer-un-avoir-fournisseur.md | achat |
| avoir sur facture | obat | avoir sur facture | obat:`comment-cr-c3-a9er-un-avoir-sur-une-facture-sur-obat.md` | facturation |
| avoirs clients | inter-fast | avoirs clients (tableau, filtres, exports) | inter-fast:inter-fast/finances/comprendre-le-tableau-des-avoirs-clients.md | facturation |
| backlog d'événements | obat | backlog d'événements (calendrier) | obat:`le-backlog-d-c3-a9v-c3-a8nements.md` | chantier-intervention |
| banque | openfire | banque / compte bancaire (création, journal comptable) | openfire:configurer-openfire/banques-et-comptes-bancaires.md | indetermine |
| base articles | extrabat | base articles (import depuis catalogues fournisseurs) | extrabat:comment-se-creer-une-base-article-a-partir-des-catalogues-fournisseurs.md | devis |
| base de calcul htva d'une facture d'acompte | vertuoza | base de calcul HTVA d'une facture d'acompte (TVA appliquée à la facturation finale) | vertuoza:faq-foires-aux-questions/quelle-est-la-difference-entre-une-facture-d-acompte-etablie-en-htva-et-une-facture-d-acompte-avec-tva-comprise.md | facturation |
| bibliothèque batichiffrage | obat | bibliothèque Batichiffrage (import ouvrage) | obat:`comment-ajouter-un-ouvrage-de-batichiffrage-sur-obat.md` | devis |
| bibliothèque batichiffrage depuis éditeur devis | obat | bibliothèque Batichiffrage depuis éditeur devis/factures | obat:`comment-acc-c3-a9der-c3-a0-votre-biblioth-c3-a8que-batichiffrage-depuis-l-c3-a9diteur-de-devis/factures.md` | devis |
| bibliothèque collaborative d'ouvrages | costructor | bibliothèque collaborative d'ouvrages (Costlib) | costructor:ventes/comment-acceder-et-utiliser-a-la-bibliotheque-costlib-1xxi4w7.md | devis |
| bibliothèque d'articles | inter-fast | bibliothèque d'articles (catalogue, ouvrages, import/export, stock) | inter-fast:inter-fast/outils/comprendre-le-tableau-de-la-bibliotheque.md | devis |
| bibliothèque d'ouvrages | obat | bibliothèque d'ouvrages | obat:`accedez-a-une-bibliotheque-complete-douvrages-pour-vos-devis.md` | devis |
| bibliothèque de lots et tâches | obat | bibliothèque de lots et tâches | obat:`administrer-bibliotheque-et-taches.md` | chantier-intervention |
| bibliothèque de prix | costructor | bibliothèque de prix (Batiprix, intégration tierce) | costructor:abonnement/comment-essayer-ou-sabonner-a-batiprix-1k44gf1.md | devis |
| bibliothèque personnalisée depuis éditeur facture | obat | bibliothèque personnalisée depuis éditeur facture/devis | obat:`comment-acc-c3-a9der-c3-a0-votre-biblioth-c3-a8que-depuis-l-c3-a9diteur-de-facture/devis.md` | devis |
| blocage gestion commerciale | extrabat | blocage gestion commerciale (client) | extrabat:bloquer-gestion-commerciale-client-independant-de-lencours.md | indetermine |
| blocs | sellsy | blocs / palettes personnalisées (éditeur marketing) | sellsy:module-marketing/marketing-gerer-des-blocs-et-palettes-personnalisees.md | indetermine |
| blocs de texte | inter-fast | blocs de texte (mentions légales, notes, insertion dans documents) | inter-fast:inter-fast/mon-entreprise/utiliser-les-blocs-de-texte.md | indetermine |
| bon d'intervention | progbat | bon d'intervention (création, planification, signature, facturation, suivi) | progbat:les-options/pourquoi-des-options/maintenance-et-interventions/interventions.md | chantier-intervention |
| bon de commande client | costructor | bon de commande client (création, conversion depuis devis) | costructor:ventes/comment-creer-un-bon-de-commande-client-1856wke.md | devis |
| bon de livraison | costructor | bon de livraison (création, conversion depuis devis) | costructor:ventes/comment-creer-un-bon-de-livraison-1cu8wh8.md | chantier-intervention |
| bon de réception | extrabat | bon de réception (affectation multi-affaires) | extrabat:affecter-de-reception-a-plusieurs-affaires.md | achat |
| bon de sortie de stock | vertuoza | bon de sortie de stock (chantier/intervention, réservation de matériaux) | vertuoza:application-mobile/bon-de-sortie-de-stock.md | chantier-intervention |
| bon de travaux | extrabat | bon de travaux (intervenant) | extrabat:bon-de-travaux.md | chantier-intervention |
| bons de commande | obat | bons de commande (achats fournisseurs) | obat:`gestion-des-bons-de-commande-sur-obat.md` | achat |
| bordereaux de chantier | obat | bordereaux de chantier (accès mobile calendrier) | obat:`consultez-et-partagez-vos-bordereaux-de-chantier-directement-dans-le-calendrier-obat.md` | chantier-intervention |
| bouteilles de fluide | inter-fast | bouteilles de fluide (gestion complète, BSFF, Trackdéchets) | inter-fast:inter-fast/fluides-frigorigenes/guide-complet-gerer-les-bouteilles-de-fluide.md | chantier-intervention |
| bénéficiaire effectif | axonaut | bénéficiaire effectif / compte pro bancaire | axonaut:compte-pro-cartes/beneficiaire-effectif-quels-documents-sont-acceptes.md | indetermine |
| calcul automatique des frais de déplacement | vertuoza | calcul automatique des frais de déplacement (distance société-client) | vertuoza:faq-foires-aux-questions/comment-sont-calcules-les-frais-de-deplacement-dans-vertuoza.md | chantier-intervention |
| calcul d'avancement | obat | calcul d'avancement (retenues de garantie, primes) | obat:`une-gestion-des-avancements-enfin-juste-et-fiable-dans-obat.md` | facturation |
| calcul de l'abonnement au pro-rata | inter-fast | calcul de l'abonnement au pro-rata (ajout/archivage utilisateur, changement de plan) | inter-fast:inter-fast/mon-entreprise/calculer-votre-abonnement-au-pro-rata.md | facturation |
| calcul de la rentabilité d'un chantier sur une période définie | vertuoza | calcul de la rentabilité d'un chantier sur une période définie (dépenses/ventes pondérées) | vertuoza:gestion-de-chantier/rentabilite-periodique.md | chantier-intervention |
| calcul de la rentabilité main-d'œuvre d'un chantier | vertuoza | calcul de la rentabilité main-d'œuvre d'un chantier (prévisionnel vs pointage réel) | vertuoza:faq-foires-aux-questions/comment-est-calculee-la-rentabilite-main-d-oeuvre-d-un-chantier.md | chantier-intervention |
| calcul de quantités avancées | vertuoza | calcul de quantités avancées (mesures multiples) sur une ligne de devis | vertuoza:documents/quantites-avances.md | devis |
| calcul des dépenses | vertuoza | calcul des dépenses (heures) dans la rentabilité d'un chantier (planning vs pointage) | vertuoza:faq-foires-aux-questions/comment-sont-calculees-les-depenses-dans-la-rentabilite-d-un-chantier.md | chantier-intervention |
| calcul des heures supplémentaires | vertuoza | calcul des heures supplémentaires (règles, dépannage) | vertuoza:faq-foires-aux-questions/comment-sont-calculees-les-heures-supplementaires-dans-le-logiciel.md | chantier-intervention |
| calcul du kilométrage dans le système de pointage | vertuoza | calcul du kilométrage dans le système de pointage (adresse de référence) | vertuoza:faq-foires-aux-questions/comment-est-calcule-le-kilometrage-dans-le-systeme-de-pointage.md | chantier-intervention |
| calcul et arrondi tva | sellsy | calcul et arrondi TVA (facturation électronique) | sellsy:facturation-electronique/comprendre-les-regles-de-calcul-et-d-arrondi-pour-la-facturation-electronique.md | facturation |
| calendrier | sellsy | calendrier / obligations (réforme facturation électronique) | sellsy:facturation-electronique/calendrier-obligations-et-definitions-de-la-reforme-francaise.md | indetermine |
| calendrier ical | inter-fast | calendrier iCal (partage vers Google Calendar, Outlook, Apple) | inter-fast:inter-fast/equipe/integrer-le-calendrier-interfast-dans-une-autre-application.md | indetermine |
| calendrier temps réel | obat | calendrier temps réel (édition directe) | obat:`nouveau-calendrier-obat-plus-simple-plus-rapide-plus-adapt-c3-a9-c3-a0-votre-quotidien.md` | chantier-intervention |
| candidature à une annonce sur vertuowork | vertuoza | candidature à une annonce sur VertuoWork | vertuoza:vertuowork/postulez-a-une-annonce-sur-vertuowork.md | indetermine |
| carte bancaire de paiement | inter-fast | carte bancaire de paiement (mise à jour, échec de paiement) | inter-fast:inter-fast/mon-entreprise/mettre-a-jour-la-carte-bancaire-de-paiement.md | facturation |
| carte de paiement | axonaut | carte de paiement (commande, activation, PIN, perte/vol) | axonaut:compte-pro-cartes/quelles-sont-les-cartes-de-paiement-axonaut.md | indetermine |
| carte de paiement mobile | axonaut | carte de paiement mobile (Apple Pay/Google Pay, double authentification) | axonaut:compte-pro-cartes/comment-ajouter-carte-de-paiement-axonaut-sur-mon-telephone-wallet.md | indetermine |
| carte à débit différé | sellsy | carte à débit différé (rapprochement bancaire) | sellsy:suivi-financier/gerer-les-cartes-a-debit-differe.md | indetermine |
| catalogue | sellsy | catalogue (traduction) | sellsy:documents-de-vente/etape-4-traduire-mon-catalogue.md | indetermine |
| catalogue services | sellsy | catalogue services (import) | sellsy:gestion-des-donnees/importer-mon-catalogue-de-services.md | indetermine |
| catalogues fournisseurs | extrabat | catalogues fournisseurs (mise à jour tarifs, widget) | extrabat:mise-jour-des-catalogues-fournisseurs.md | achat |
| catégorie comptable de vente | costructor | catégorie comptable de vente / TVA | costructor:debuter-sur-costructor/comment-ajuster-les-categories-de-ventes-par-taux-de-tva-v48dla.md | indetermine |
| catégorie d'achat | costructor | catégorie d'achat (comptable) | costructor:debuter-sur-costructor/comment-parametrer-les-categories-dachats-19pewed.md | achat |
| catégorie d'article | openfire | catégorie d'article (regroupement, valorisation, comptabilité) | openfire:knowsystem/categories-d-articles-188.md | indetermine |
| catégorie de produit | openfire | catégorie de produit (méthode de valorisation des stocks) | openfire:configurer-openfire/configuration-des-categories-d-articles-pour-la-valorisation-des-stocks.md | indetermine |
| catégorie de produits | sellsy | catégorie de produits (catalogue) | sellsy:catalogue-produits-et-services/gerer-mes-categories-de-produits.md | indetermine |
| catégorisation | axonaut | catégorisation (contacts, produits, champs personnalisés) | axonaut:optimisez-gestion-commerciale/categoriser-les-contacts-sur-votre-compte-axonaut.md | indetermine |
| centre d'aide | inter-fast | centre d'aide (canaux : académie, aide en ligne, support, actualités) | inter-fast:inter-fast/debuter-avec-interfast/trouver-les-reponses-a-mes-questions.md | indetermine |
| cerfa | inter-fast | CERFA (tableau des mouvements de fluide, bilan, export) | inter-fast:inter-fast/fluides-frigorigenes/comprendre-le-tableau-des-cerfas.md | chantier-intervention |
| certifications d'entreprise | inter-fast | certifications d'entreprise (ajout, affichage sur documents) | inter-fast:inter-fast/mon-entreprise/ajouter-mes-certifications-d-entreprise.md | indetermine |
| changement d'étape | openfire | changement d'étape (manuel ou automatisé) d'une opportunité dans le pipeline | openfire:knowsystem/faire-evoluer-l-opportunite-189.md | demande |
| chat obat | obat | Chat Obat (messagerie interne) | obat:`le-chat-obat-communiquez-efficacement-depuis-votre-application.md` | indetermine |
| chatbot ia | progbat | chatbot IA / hotline juridique (Caarl) | progbat:le-menu-principal/service-juridique/chatbot-ia-et-hotline-juridique.md | indetermine |
| checklist conformité | sellsy | checklist conformité (facturation électronique) | sellsy:facturation-electronique/la-checklist-dediee-et-les-etapes-a-suivre.md | indetermine |
| checklist de démarrage | inter-fast | checklist de démarrage (onboarding complet InterFast) | inter-fast:inter-fast/debuter-avec-interfast/checklist-de-demarrage.md | indetermine |
| checklist de dépannage de soumission de devis bloquée | vertuoza | checklist de dépannage de soumission de devis bloquée | vertuoza:faq-foires-aux-questions/quelles-sont-toutes-les-raisons-possibles-pour-lesquelles-je-n-arrive-pas-a-soumettre-mon-devis.md | devis |
| chiffrage de devis | progbat | chiffrage de devis (3 méthodes : simple, avancée, expert/ouvrages composés) | progbat:le-menu-principal/devis-factures/devis/chiffrer-un-devis.md | devis |
| chiffre d'affaires | obat | chiffre d'affaires (visualisation) | obat:`comment-visualiser-votre-chiffre-d-affaires.md` | facturation |
| choix du modèle de document par défaut affiché à l'ouverture du pdf | vertuoza | choix du modèle de document par défaut affiché à l'ouverture du PDF | vertuoza:parametres/preferences-des-modeles-de-documents.md | devis |
| choix du sens de synchronisation des factures fournisseurs | vertuoza | choix du sens de synchronisation des factures fournisseurs (envoi/réception) et procédure d'import | vertuoza:parametres/synchroniser-vos-factures-fournisseurs-bidirectionnel.md | achat |
| choix statut juridique | obat | choix statut juridique (micro-entreprise vs EI) | obat:`micro-entreprise-ou-entreprise-individuelle-quand-changer-de-statut-dans-le-btp.md` | indetermine |
| classification comptable des factures par taux de tva et activité | vertuoza | classification comptable des factures par taux de TVA et activité | vertuoza:faq-foires-aux-questions/synchronisation-comptable-comment-seront-classees-les-factures-en-fonction-du-taux-de-tva-et-des-activites.md | facturation |
| click-to-call | inter-fast | click-to-call (appel depuis le CRM, intégrations téléphonie VoIP) | inter-fast:inter-fast/application-mobile/utiliser-le-click-to-call-pour-appeler-depuis-le-crm.md | indetermine |
| client sur devis | inter-fast | client sur devis (modification, statuts brouillon/finalisé) | inter-fast:inter-fast/finances/modifier-le-client-sur-un-devis.md | devis |
| client sur facture | inter-fast | client sur facture (modification, statuts brouillon/finalisé) | inter-fast:inter-fast/finances/modifier-le-client-sur-une-facture.md | facturation |
| clients | inter-fast | clients/prospects (gestion CRM, app mobile) | inter-fast:inter-fast/application-mobile/gerer-les-clients-app-mobile.md | indetermine |
| clé api | costructor | clé API | costructor:debuter-sur-costructor/comment-creer-une-cle-api-i7mrya.md | indetermine |
| clôture d'exercice comptable | axonaut | clôture d'exercice comptable (verrouillage irréversible, portail comptable) | axonaut:gerez-votre-comptabilite/comment-cloturer-mon-exercice-comptable.md | indetermine |
| clôture d'une intervention | openfire | clôture d'une intervention (saisie des temps, compte-rendu, statut) | openfire:knowsystem/terminer-une-intervention-95.md | chantier-intervention |
| code postal | extrabat | code postal/ville (autocomplétion, fiche contact) | extrabat:je-saisis-mon-code-postal-ou-ma-ville.md | indetermine |
| code promo de démarrage | inter-fast | code promo de démarrage (éligibilité, activation) | inter-fast:inter-fast/mon-entreprise/beneficier-du-code-promo-de-demarrage.md | achat |
| code promotionnel | sellsy | code promotionnel | sellsy:catalogue-produits-et-services/gestion-des-codes-promotionnels.md | indetermine |
| code unece | openfire | code UNECE (facturation électronique, taxes/unités/paiement) | openfire:configurer-openfire/verifier-et-associer-vos-codes-unece-pour-la-facturation-electronique.md | facturation |
| code-barres | sellsy | code-barres (produit) | sellsy:catalogue-produits-et-services/ajouter-un-code-barres-a-un-produit.md | indetermine |
| codes tiers | axonaut | codes tiers (formats de numérotation clients/fournisseurs) | axonaut:gerez-votre-comptabilite/automatisez-la-gestion-des-codes-tiers-numeros-clients-fournisseurs.md | indetermine |
| coefficient global d'ajustement | obat | coefficient global d'ajustement (devis) | obat:`comment-ajouter-un-coefficient-global-dajustement-sur-votre-devis.md` | devis |
| collaborateur | sellsy | collaborateur (gestion accès) | sellsy:configuration-du-compte/gerer-les-acces-collaborateurs.md | indetermine |
| colonne latérale | sellsy | colonne latérale (fiches société / contact / opportunité) | sellsy:repertoire/repertoire-la-colonne-laterale-des-fiches.md | indetermine |
| colonne ttc | costructor | colonne TTC (affichage document) | costructor:ventes/comment-ajouter-la-colonne-ttc-sur-mes-documents-quiaob.md | indetermine |
| colonnes de documents | sellsy | colonnes de documents (affichage) | sellsy:documents-de-vente/masquer-certaines-colonnes-des-documents.md | facturation |
| commande | inter-fast | commande (réception marchandises, app mobile) | inter-fast:inter-fast/application-mobile/receptionner-une-commande-app-mobile.md | achat |
| commande client | axonaut | commande client (conteneur devis/factures/BL, clôture) | axonaut:commandes-clients-fournisseurs/fonctionnement-dune-commande-client.md | devis |
| commande à renouveler | extrabat | commande à renouveler (augmentation tarifaire, contrat services) | extrabat:pratiquer-augmentation-dune-commande-a-renouveler-type-contrat-de-services.md | facturation |
| commandes | extrabat | commandes/BL (regroupement en facture) | extrabat:veux-regrouper-plusieurs-commandes-bons-de-livraison-seule-facture.md | facturation |
| commission commerciale | extrabat | commission commerciale (commande client) | extrabat:comment-associer-un-commercial-a-une-commande-client-pour-le-calcul-de-sa-commission.md | achat |
| commission de recouvrement | progbat | commission de recouvrement (honoraires, barème, reversement) | progbat:le-menu-principal/service-juridique/recouvrement-de-factures-impayees/paiement-de-la-commission.md | facturation |
| compatibilité de l'application mobile | vertuoza | compatibilité de l'application mobile (tablettes Windows non supportées) | vertuoza:demarrer/l-application-est-elle-disponible-sur-les-tablettes-windows.md | indetermine |
| comportement d'affichage des factures partiellement payées dans l'export excel | vertuoza | comportement d'affichage des factures partiellement payées dans l'export Excel | vertuoza:faq-foires-aux-questions/pourquoi-certaines-factures-apparaissent-elles-encore-dans-la-liste-dans-mon-export-excel-meme-apres-paiement-partiel.md | facturation |
| comportement d'affichage des indicateurs de rentabilité | vertuoza | comportement d'affichage des indicateurs de rentabilité (facture brouillon ou partielle) | vertuoza:faq-foires-aux-questions/pourquoi-un-montant-reste-t-il-affiche-dans-les-indicateurs-de-rentabilite-meme-apres-avoir-encode-une-facture-fournisseur.md | achat |
| comportement d'import excel | vertuoza | comportement d'import Excel (ligne sans prix total = option) | vertuoza:faq-foires-aux-questions/pourquoi-mes-lignes-sont-elles-definies-comme-options-par-defaut-lorsque-je-les-importe-depuis-excel.md | devis |
| comportement de l'envoi d'emails via l'intégration gmail | vertuoza | comportement de l'envoi d'emails via l'intégration Gmail (traçabilité modifiée) | vertuoza:faq-foires-aux-questions/que-se-passe-t-il-si-j-envoie-mes-emails-depuis-ma-propre-adresse-gmail-via-vertuoza.md | indetermine |
| comportement de l'envoi peppol si le client n'est pas connecté au réseau | vertuoza | comportement de l'envoi PEPPOL si le client n'est pas connecté au réseau | vertuoza:faq-foires-aux-questions/que-se-passe-t-il-si-un-client-n-est-pas-connecte-au-reseau-peppol.md | facturation |
| comportement de l'option « chantier inconnu » sur un bon de retour | vertuoza | comportement de l'option « chantier inconnu » sur un bon de retour (ajout direct au stock) | vertuoza:faq-foires-aux-questions/que-se-passe-t-il-lorsque-je-selectionne-chantier-inconnu-pour-un-article-dans-un-bon-de-retour.md | achat |
| comportement de l'option « tout exporter » | vertuoza | comportement de l'option « Tout exporter » (réexport uniquement, sélection requise) | vertuoza:faq-foires-aux-questions/pourquoi-ne-puis-je-pas-exporter-mes-factures-avec-l-option-tout-exporter.md | facturation |
| comportement de mise à jour partielle lors de la réactivation d'un contact importé | vertuoza | comportement de mise à jour partielle lors de la réactivation d'un contact importé | vertuoza:faq-foires-aux-questions/pourquoi-certaines-informations-restent-elles-apres-un-import-de-contacts-dans-vertuoza.md | indetermine |
| comportement de non-intégration rétroactive d'un avenant validé après création d'un état d'avancement | vertuoza | comportement de non-intégration rétroactive d'un avenant validé après création d'un état d'avancement | vertuoza:faq-foires-aux-questions/pourquoi-mon-avenant-n-a-t-il-pas-ete-integre-dans-l-etat-d-avancement-que-j-ai-cree.md | chantier-intervention |
| comportement de recherche stock | vertuoza | comportement de recherche stock (référence exacte vs partielle) en cas d'entrées similaires | vertuoza:faq-foires-aux-questions/pourquoi-ma-recherche-de-stock-avec-la-reference-complete-ne-donne-aucun-resultat-alors-que-l-article-existe-bien.md | achat |
| comportement de statut d'une note de crédit et solutions de régularisation | vertuoza | comportement de statut d'une note de crédit et solutions de régularisation | vertuoza:faq-foires-aux-questions/pourquoi-ma-note-de-credit-reste-t-elle-en-statut-non-payee-et-que-faire.md | facturation |
| comportement de tri des factures fournisseurs créées par ia | vertuoza | comportement de tri des factures fournisseurs créées par IA (tri par date facture) | vertuoza:faq-foires-aux-questions/pourquoi-certaines-factures-fournisseurs-creees-par-l-ia-ne-s-affichent-pas-en-haut-de-la-liste.md | achat |
| comportement du bouton « lien devis | vertuoza | comportement du bouton « lien devis/facture » (envoi par lien vs pièce jointe PDF) | vertuoza:faq-foires-aux-questions/pourquoi-le-bouton-lien-devis-ou-facture-en-haut-a-gauche-empeche-t-il-l-envoi-du-pdf-avec-le-devis-ou-la-facture.md | devis |
| comportement du champ marge | vertuoza | comportement du champ marge (calculé, non modifiable directement) sur une commande | vertuoza:faq-foires-aux-questions/pourquoi-la-marge-peut-elle-apparaitre-a-100-dans-une-commande-et-comment-la-modifier.md | chantier-intervention |
| comportement du copier-coller des ressources d'un ouvrier sur une autre journée | vertuoza | comportement du copier-coller des ressources d'un ouvrier sur une autre journée | vertuoza:planning/que-se-passe-t-il-lorsque-l-on-copie-colle-les-ressources-d-un-ouvrier-sur-une-autre-journee-via-la-plateforme.md | chantier-intervention |
| comportement du pointage pour un ouvrier non planifié | vertuoza | comportement du pointage pour un ouvrier non planifié (absence) | vertuoza:faq-foires-aux-questions/est-ce-qu-un-pointage-est-cree-lorsqu-un-ouvrier-n-est-pas-cense-travailler-par-exemple-le-week-end.md | chantier-intervention |
| comportement du statut de facture après envoi d'un rappel de paiement | vertuoza | comportement du statut de facture après envoi d'un rappel de paiement | vertuoza:faq-foires-aux-questions/est-ce-que-le-statut-d-une-facture-passe-automatiquement-a-rappel-envoye-lorsqu-un-rappel-de-paiement-est-effectue.md | facturation |
| comptabilisation | sellsy | comptabilisation (factures achat / vente) | sellsy:suivi-financier/comptabiliser-des-factures-d-achat-et-de-vente.md | facturation |
| comptabilité analytique | sellsy | comptabilité analytique (codes, produits / affaires) | sellsy:suivi-financier/utiliser-les-codes-comptables-analytiques.md | indetermine |
| comptabilité auxiliaire | sellsy | comptabilité auxiliaire (comptes clients / fournisseurs) | sellsy:suivi-financier/utiliser-la-comptabilite-auxiliaire.md | indetermine |
| comptable | inter-fast | comptable (invitation, rôle lecture seule) | inter-fast:inter-fast/equipe/inviter-mon-comptable-sur-interfast.md | indetermine |
| compte axonaut | axonaut | compte Axonaut (inscription, modules, alias email, profil — hub multi-sujets) | axonaut:configurer-votre-compte/comment-creer-son-compte-axonaut-facilement-et-rapidement.md | indetermine |
| compte bancaire professionnel | obat | compte bancaire professionnel (SWAN) | obat:`comment-creer-et-parametrer-votre-compte-pro-swan.md` | indetermine |
| compte bancaire synchronisé | sellsy | compte bancaire synchronisé (suppression / modification) | sellsy:suivi-financier/supprimer-ou-modifier-un-compte-bancaire-synchronise.md | indetermine |
| compte comptable | extrabat | compte comptable (création/modification) | extrabat:creer-ou-modifier-un-compte-comptable.md | facturation |
| compte pro swan | obat | compte pro Swan (ouverture) | obat:`ouvrez-votre-compte-pro-swan-avec-obat-simple-gratuit-et-sans-frais-cach-c3-a9s.md` | indetermine |
| compte prorata | obat | compte prorata (devis/factures) | obat:`comment-mettre-en-place-un-compte-prorata-sur-vos-devis-et-factures.md` | indetermine |
| comptes auxiliaires | obat | comptes auxiliaires (paramétrage comptabilité) | obat:`comptes-auxiliaires-comptable.md` | indetermine |
| comptes auxiliaires clients | obat | comptes auxiliaires clients (numérotation flexible) | obat:`comptes-auxiliaires-plus-de-souplesse-moins-de-contraintes.md` | indetermine |
| comptes auxiliaires fournisseurs | obat | comptes auxiliaires fournisseurs (numérotation) | obat:`les-comptes-auxiliaires-fournisseurs.md` | achat |
| comptes bancaires | progbat | comptes bancaires (paramétrage, connexion Powens) | progbat:pour-bien-demarrer/parametrage/parametres-de-lentreprise/comptes-bancaires.md | indetermine |
| comptes complémentaires | progbat | comptes complémentaires (majorations/déductions factures, compte prorata) | progbat:le-menu-principal/comptabilite/parametrage-comptable/comptes-complementaires.md | indetermine |
| comptes de tiers | progbat | comptes de tiers / comptes auxiliaires (clients, fournisseurs, sous-traitants) | progbat:le-menu-principal/comptabilite/parametrage-comptable/comptes-de-tiers.md | indetermine |
| comptes de tva | progbat | comptes de TVA (facture d'acompte, extensions par taux) | progbat:le-menu-principal/comptabilite/parametrage-comptable/comptes-de-tva.md | facturation |
| comptes financiers | progbat | comptes financiers (comptes bancaires/caisse, extension par mode de paiement) | progbat:le-menu-principal/comptabilite/parametrage-comptable/comptes-financiers.md | indetermine |
| condition de règlement | openfire | condition de règlement (échéancier) | openfire:knowsystem/conditions-de-reglement-156.md | facturation |
| conditions d'accès au recouvrement amiable | progbat | conditions d'accès au recouvrement amiable (créance certaine/liquide/exigible, délais de prescription) | progbat:le-menu-principal/service-juridique/recouvrement-de-factures-impayees/conditions-dacces-au-service-de-recouvrement-amiable.md | facturation |
| conditions de bas de page des documents standards | vertuoza | conditions de bas de page des documents standards (devis, commandes) | vertuoza:parametres/conditions-de-bas-de-page-des-documents-standards.md | devis |
| conditions de correspondance pour la synchronisation des paiements ponto | vertuoza | conditions de correspondance pour la synchronisation des paiements Ponto/Codabox | vertuoza:faq-foires-aux-questions/pourquoi-est-ce-que-la-synchronisation-des-paiements-echoue-et-quelles-conditions-doivent-etre-verifiees-pour-resoudre-ce-probleme.md | facturation |
| conditions de paiement par défaut | obat | conditions de paiement par défaut | obat:`comment-ajouter-vos-conditions-de-paiements-par-d-c3-a9faut-sur-obat.md` | indetermine |
| conditions techniques de synchronisation bancaire vertuoza | vertuoza | conditions techniques de synchronisation bancaire Vertuoza/Codabox/Ponto | vertuoza:faq-foires-aux-questions/quelles-sont-les-conditions-pour-qu-une-synchronisation-entre-vertuoza-et-codabox-ponto-soit-effectuee.md | facturation |
| configuration chift | obat | configuration Chift (journaux, comptes, clients) | obat:`configuration-des-c3-a9l-c3-a9ments-du-logiciel-comptable.md` | indetermine |
| configuration comptable des situations, retenues de garantie et prorata | openfire | configuration comptable des situations, retenues de garantie et prorata | openfire:knowsystem/configurer-la-situation-retenue-de-garantie-et-compte-prorata-208.md | facturation |
| configuration d'un modèle d'email par défaut | vertuoza | configuration d'un modèle d'email par défaut | vertuoza:faq-foires-aux-questions/comment-puis-je-faire-en-sorte-que-le-texte-de-mes-emails-soit-toujours-le-meme-sans-avoir-a-le-reecrire-a-chaque-fois.md | indetermine |
| configuration d'un ouvrier étant aussi son propre chef d'équipe | vertuoza | configuration d'un ouvrier étant aussi son propre chef d'équipe (double compte) | vertuoza:faq-foires-aux-questions/comment-gerer-un-ouvrier-qui-est-egalement-son-propre-chef-d-equipe.md | indetermine |
| configuration d'un serveur mail sortant et dépannage des erreurs smtp | openfire | configuration d'un serveur mail sortant et dépannage des erreurs SMTP | openfire:knowsystem/parametrer-un-serveur-mail-151.md | indetermine |
| configuration d'une automatisation | inter-fast | configuration d'une automatisation (déclencheur, scénario, arrêt, modèle devis→chantier) | inter-fast:inter-fast/outils/configurer-une-automatisation.md | devis |
| configuration d'une signature d'email automatique | vertuoza | configuration d'une signature d'email automatique | vertuoza:parametres/signature-d-e-mail.md | indetermine |
| configuration de l'affichage du montant total htva sur une facture | vertuoza | configuration de l'affichage du montant total HTVA sur une facture | vertuoza:faq-foires-aux-questions/comment-afficher-le-montant-total-htva-sur-ma-facture.md | facturation |
| configuration de l'année fiscale | vertuoza | configuration de l'année fiscale (impact sur numérotation des factures) | vertuoza:finance/annee-fiscale.md | facturation |
| configuration de l'horaire par défaut de la société | vertuoza | configuration de l'horaire par défaut de la société (ouvriers, planning) | vertuoza:parametres/horaire-de-la-societe.md | indetermine |
| configuration de l'impression des primes dans le sous-total des factures | openfire | configuration de l'impression des primes dans le sous-total des factures | openfire:knowsystem/impression-des-totaux-dans-les-factures-183.md | facturation |
| configuration de la messagerie professionnelle via smtp | vertuoza | configuration de la messagerie professionnelle via SMTP/IMAP (par fournisseur) | vertuoza:parametres/configurer-votre-adresse-email-avec-smtp.md | indetermine |
| configuration de la politique de facturation | openfire | configuration de la politique de facturation (quantités commandées vs livrées) | openfire:knowsystem/politique-de-facturation-141.md | facturation |
| configuration de la synchronisation google agenda | openfire | configuration de la synchronisation Google Agenda (API Google, identifiants OAuth) | openfire:knowsystem/synchronisation-google-agenda-269.md | chantier-intervention |
| configuration de la visibilité des prix pour l'ouvrier | vertuoza | configuration de la visibilité des prix pour l'ouvrier | vertuoza:application-mobile/visibilite-des-prix-par-l-ouvrier.md | indetermine |
| configuration de tâches automatiques déclenchées par événement | vertuoza | configuration de tâches automatiques déclenchées par événement (envoi de devis, transformation en chantier) | vertuoza:parametres/taches-automatisees.md | devis |
| configuration des adresses de livraison distinctes pour les commandes de matériaux | vertuoza | configuration des adresses de livraison distinctes pour les commandes de matériaux | vertuoza:parametres/adresses-de-livraison-de-la-societe.md | achat |
| configuration des campagnes, canaux et origines marketing | openfire | configuration des campagnes, canaux et origines marketing | openfire:knowsystem/parametrer-les-campagnes-les-canaux-et-les-origines-197.md | demande |
| configuration des champs d'informations générales affichés sur le devis | vertuoza | configuration des champs d'informations générales affichés sur le devis | vertuoza:devis/informations-generales-du-devis.md | devis |
| configuration des civilités de contact | vertuoza | configuration des civilités de contact | vertuoza:contacts/civilite.md | indetermine |
| configuration des conditions de paiement | vertuoza | configuration des conditions de paiement (délai, type) | vertuoza:parametres/conditions-de-paiements.md | facturation |
| configuration des couleurs des documents pdf standards | vertuoza | configuration des couleurs des documents PDF standards | vertuoza:parametres/couleurs-des-documents-standards.md | devis |
| configuration des créneaux et types d'horaires des employés | openfire | configuration des créneaux et types d'horaires des employés | openfire:knowsystem/creneaux-horaires-67.md | indetermine |
| configuration des emails envoyés | obat | configuration des emails envoyés | obat:`comment-configurer-les-emails-envoyes-depuis-obat.md` | indetermine |
| configuration des frais généraux facturables associés aux interventions | vertuoza | configuration des frais généraux facturables associés aux interventions | vertuoza:gestion-des-interventions/frais-generaux.md | facturation |
| configuration des indemnités de déplacement et paniers repas | vertuoza | configuration des indemnités de déplacement et paniers repas (France) | vertuoza:beta/zones-de-deplacement-et-panier-repas-france.md | indetermine |
| configuration des informations générales de la société | vertuoza | configuration des informations générales de la société (logo, coordonnées) réutilisées dans les documents | vertuoza:parametres/informations-generales-de-la-societe.md | indetermine |
| configuration des modèles d'intervention | openfire | configuration des modèles d'intervention (facturation, questionnaire, rapport) | openfire:knowsystem/modeles-dintervention-73.md | chantier-intervention |
| configuration des modèles de projets et attributs pour les opportunités | openfire | configuration des modèles de projets et attributs pour les opportunités | openfire:knowsystem/parametrer-les-projets-195.md | demande |
| configuration des modèles par défaut par type de document et de l'affichage pdf direct | vertuoza | configuration des modèles par défaut par type de document et de l'affichage PDF direct | vertuoza:parametres/preferences-configurez-vos-modeles-par-defaut-et-l-affichage-pdf.md | devis |
| configuration des méthodes de paiement disponibles | vertuoza | configuration des méthodes de paiement disponibles | vertuoza:parametres/methodes-de-paiements.md | facturation |
| configuration des métiers de contact | vertuoza | configuration des métiers de contact (sous-traitants, fournisseurs) | vertuoza:contacts/metiers.md | indetermine |
| configuration des positions fiscales | openfire | configuration des positions fiscales (taxes automatiques par contact/pays) | openfire:knowsystem/position-fiscale-143.md | devis |
| configuration des préférences d'interventions et d'affichage du planning | vertuoza | configuration des préférences d'interventions et d'affichage du planning | vertuoza:gestion-des-interventions/preferences.md | chantier-intervention |
| configuration des préférences de facturation | vertuoza | configuration des préférences de facturation (type, QR code, numérotation, suppression) | vertuoza:finance/preferences.md | facturation |
| configuration des préférences du stock | vertuoza | configuration des préférences du stock (niveaux d'emplacements, réapprovisionnement automatique) | vertuoza:stock/preferences-du-stock.md | indetermine |
| configuration des relances de factures impayées | openfire | configuration des relances de factures impayées | openfire:knowsystem/configurer-mes-relances-144.md | facturation |
| configuration des routes logistiques | openfire | configuration des routes logistiques (itinéraires des articles, règles de flux) | openfire:knowsystem/routes-226.md | achat |
| configuration des règles d'approvisionnement | openfire | configuration des règles d'approvisionnement (achat, flux poussés/tirés, quantités min/max) | openfire:knowsystem/regles-d-approvisionnement-249.md | achat |
| configuration des secteurs géographiques pour la planification des tournées | openfire | configuration des secteurs géographiques pour la planification des tournées | openfire:knowsystem/secteurs-70.md | chantier-intervention |
| configuration des sections de devis | openfire | configuration des sections de devis (classiques et avancées) | openfire:knowsystem/parametrer-les-sections-175.md | devis |
| configuration des sources commerciales | vertuoza | configuration des sources commerciales (origine des prospects) liées aux opportunités | vertuoza:devis/sources.md | demande |
| configuration des statuts d'opportunité | vertuoza | configuration des statuts d'opportunité (probabilité, ordre) et des droits d'accès | vertuoza:crm/parametres.md | demande |
| configuration des séquences de numérotation des journaux comptables | openfire | configuration des séquences de numérotation des journaux comptables | openfire:knowsystem/sequences-des-journaux-278.md | facturation |
| configuration des taux de tva | vertuoza | configuration des taux de TVA (correspondance avec le logiciel comptable) | vertuoza:parametres/les-taux-de-tva.md | indetermine |
| configuration des taxes | openfire | configuration des taxes (TVA, intracommunautaire, autoliquidation sous-traitance BTP) | openfire:knowsystem/taxes-193.md | facturation |
| configuration des types d'absences | vertuoza | configuration des types d'absences | vertuoza:rh/type-d-absences.md | indetermine |
| configuration des types d'installation | vertuoza | configuration des types d'installation (classification) | vertuoza:gestion-des-interventions/types-d-installation.md | chantier-intervention |
| configuration des types d'intervention | vertuoza | configuration des types d'intervention (durée, forfait/régie, frais) | vertuoza:gestion-des-interventions/types-d-intervention.md | chantier-intervention |
| configuration des types de chantier | vertuoza | configuration des types de chantier (classification personnalisée) | vertuoza:gestion-de-chantier/types-de-chantier.md | chantier-intervention |
| configuration des types de frais pour factures fournisseurs « autres » | vertuoza | configuration des types de frais pour factures fournisseurs « autres » | vertuoza:finance/types-de-frais.md | achat |
| configuration des tâches de chantier | vertuoza | configuration des tâches de chantier (checklist qualité, planification quotidienne) | vertuoza:gestion-de-chantier/taches-de-chantier.md | chantier-intervention |
| configuration du module calendrier | inter-fast | configuration du module Calendrier (affichage, absences, feuilles d'heures, statuts) | inter-fast:inter-fast/operations/configurer-le-module-calendrier.md | chantier-intervention |
| configuration du modèle d'email par défaut à l'envoi | vertuoza | configuration du modèle d'email par défaut à l'envoi | vertuoza:parametres/modele-d-email-par-defaut.md | indetermine |
| configuration du profil utilisateur | vertuoza | configuration du profil utilisateur (informations, photo) | vertuoza:parametres/informations-generales-du-profil.md | indetermine |
| configuration du style général | vertuoza | configuration du style général (polices, couleurs) par défaut des documents | vertuoza:parametres/style-general-personnalisez-les-couleurs-et-polices-de-vos-documents.md | devis |
| configuration et gestion des parrainages clients | openfire | configuration et gestion des parrainages clients (récompenses) | openfire:knowsystem/gestion-des-parrainages-254.md | demande |
| configuration et gestion des relations entre contacts | openfire | configuration et gestion des relations entre contacts | openfire:knowsystem/relations-273.md | indetermine |
| configuration et gestion du pointage | vertuoza | configuration et gestion du pointage (temps de travail, mobilité, indemnités, heures supplémentaires en France) | vertuoza:rh/pointage.md | indetermine |
| configuration et utilisation du connecteur eldotravo | openfire | configuration et utilisation du connecteur EldoTravo (collecte d'avis clients) | openfire:knowsystem/eldotravo-267.md | chantier-intervention |
| configuration générale | openfire | configuration générale (planning, intervention, mobile) | openfire:knowsystem/configurations-generales-20.md | chantier-intervention |
| configuration planning | obat | configuration planning (semaines type, congés) | obat:`configuration-de-votre-planning/calendrier/suivi-du-temps-version-2.md` | chantier-intervention |
| configuration ressources | obat | configuration ressources (mini module RH) | obat:`configurer-vos-ressources-le-planning.md` | indetermine |
| configuration technique | openfire | configuration technique (navigateur/OS) | openfire:bien-debuter/caracteristiques-techniques-et-configurations-requises.md | indetermine |
| conformité facturation lors d'une transition logicielle | obat | conformité facturation lors d'une transition logicielle | obat:`comment-bien-gerer-votre-facturation-pendant-la-bascule-vers-obat.md` | facturation |
| conformité loi anti-fraude 2018 | obat | conformité loi anti-fraude 2018 (FAQ) | obat:`obat-est-il-conforme-c3-a0-a-loi-anti-fraude-de-2018.md` | indetermine |
| connecteur | sellsy | connecteur / intégration (Sellsy) | sellsy:facturation-electronique/integrer-un-outil-a-sellsy.md | indetermine |
| connecteur comptable acd | sellsy | connecteur comptable ACD | sellsy:integrations-et-api/connecter-sellsy-et-acd.md | indetermine |
| connecteur comptable cegid loop | sellsy | connecteur comptable Cegid Loop | sellsy:integrations-et-api/connecter-sellsy-et-cegid-loop.md | indetermine |
| connecteur comptable fulll | sellsy | connecteur comptable Fulll | sellsy:integrations-et-api/connecter-sellsy-et-fulll.md | indetermine |
| connecteur comptable inexweb | sellsy | connecteur comptable InexWeb (In Extenso) | sellsy:integrations-et-api/connecter-sellsy-et-inexweb-in-extenso.md | indetermine |
| connecteur comptable inqom | sellsy | connecteur comptable Inqom | sellsy:integrations-et-api/connecter-sellsy-et-inqom.md | indetermine |
| connecteur comptable myunisoft | sellsy | connecteur comptable MyUnisoft | sellsy:integrations-et-api/connecter-sellsy-et-myunisoft.md | indetermine |
| connecteur comptable sage génération experts | sellsy | connecteur comptable Sage Génération Experts | sellsy:integrations-et-api/connecter-sellsy-et-sage-generation-experts.md | indetermine |
| connecteur comptable tiime | sellsy | connecteur comptable Tiime | sellsy:integrations-et-api/connecter-sellsy-et-tiime.md | indetermine |
| connecteur de leads | openfire | connecteur de leads (Réseau Seguin, CRM) | openfire:configurer-openfire/reseau-seguin-configurer-le-connecteur-de-leads.md | demande |
| connecteur multi-entités | sellsy | connecteur multi-entités (facturation groupe) | sellsy:documents-de-vente/connecteur-multi-entites-de-facturation.md | facturation |
| connexion collaborateur | inter-fast | connexion collaborateur (activation, dépannage, réinitialisation) | inter-fast:inter-fast/equipe/aider-un-collaborateur-a-se-connecter.md | indetermine |
| connexion comptable acd | progbat | connexion comptable ACD (synchronisation factures avec expert-comptable) | progbat:les-options/pourquoi-des-options/connexions-comptables/mes-outils-comptables-en-option/acd.md | facturation |
| connexion comptable cegid loop | progbat | connexion comptable Cegid Loop (synchronisation factures avec expert-comptable) | progbat:les-options/pourquoi-des-options/connexions-comptables/mes-outils-comptables-en-option/cegid-loop.md | facturation |
| connexion comptable inqom | progbat | connexion comptable Inqom (synchronisation factures avec expert-comptable) | progbat:les-options/pourquoi-des-options/connexions-comptables/mes-outils-comptables-en-option/inqom.md | facturation |
| connexion comptable meg | progbat | connexion comptable MEG (mon expert en gestion) | progbat:les-options/pourquoi-des-options/connexions-comptables/mes-outils-de-gestion-externe/meg-mon-expert-en-gestion.md | facturation |
| connexion comptable myunisoft | progbat | connexion comptable MyUnisoft (synchronisation factures avec expert-comptable) | progbat:les-options/pourquoi-des-options/connexions-comptables/mes-outils-comptables-en-option/myunisoft.md | facturation |
| connexion comptable pennylane | progbat | connexion comptable Pennylane (synchronisation factures, mode d'envoi) | progbat:les-options/pourquoi-des-options/connexions-comptables/mes-outils-de-gestion-externe/pennylane.md | facturation |
| connexion comptable sage 100 fr | progbat | connexion comptable Sage 100 FR (synchronisation factures avec expert-comptable) | progbat:les-options/pourquoi-des-options/connexions-comptables/mes-outils-comptables-en-option/sage-100-fr.md | facturation |
| connexion comptable sage bob 50 | progbat | connexion comptable Sage BOB 50 (synchronisation factures avec expert-comptable) | progbat:les-options/pourquoi-des-options/connexions-comptables/mes-outils-comptables-en-option/sage-bob-50.md | facturation |
| connexion comptable sage génération experts | progbat | connexion comptable Sage Génération Experts (synchronisation factures avec expert-comptable) | progbat:les-options/pourquoi-des-options/connexions-comptables/mes-outils-comptables-en-option/sage-generation-experts.md | facturation |
| connexion compte legrand | obat | connexion compte Legrand (multi-société) | obat:`connectez-votre-compte-legrand.md` | indetermine |
| connexion e-commerce | axonaut | connexion e-commerce (Shopify/Prestashop/Woocommerce) | axonaut:connectez-axonaut/comment-connecter-votre-boutique-en-ligne-a-axonaut-shopify-prestashop-woocommerce.md | indetermine |
| connexion initiale à vertuoza | vertuoza | connexion initiale à Vertuoza (lien tenant, identifiants) | vertuoza:demarrer/se-connecter-a-vertuoza.md | indetermine |
| connexion paypal | axonaut | connexion PayPal (identifiants API, paiement devis/factures) | axonaut:gerez-vos-factures/comment-connecter-paypal-a-axonaut.md | indetermine |
| connexion pdp | progbat | connexion PDP / OD (outils comptables en option, réforme facturation électronique) | progbat:les-options/pourquoi-des-options/connexions-comptables/mes-outils-comptables-en-option.md | facturation |
| connexion point de vente | axonaut | connexion point de vente (Hiboutik, facturation auto, client anonyme) | axonaut:connectez-axonaut/connexion-axonaut-hiboutik-comment-ca-marche.md | indetermine |
| connexion simultanée à deux comptes | inter-fast | connexion simultanée à deux comptes (multi-entreprise, navigation privée) | inter-fast:inter-fast/equipe/connexion-a-deux-comptes-interfast.md | indetermine |
| connexion simultanée à plusieurs environnements vertuoza | vertuoza | connexion simultanée à plusieurs environnements Vertuoza (profils navigateur) | vertuoza:demarrer/comment-se-connecter-a-plusieurs-environnements-en-meme-temps.md | indetermine |
| connexion téléphonie | axonaut | connexion téléphonie (3CX/Wildix/Ringover, click-to-call) | axonaut:connectez-axonaut/connecter-votre-systeme-de-telephonie.md | indetermine |
| connexion via google | obat | connexion via Google/Facebook (SSO) | obat:`connexion-simplifiee-a-obat-utilisez-google-ou-facebook.md` | indetermine |
| connexion à l'application mobile | vertuoza | connexion à l'application mobile (code société, identifiants) | vertuoza:application-mobile/se-connecter-a-l-application-mobile.md | indetermine |
| connexion à la base de production et à la base de test | openfire | connexion à la base de production et à la base de test | openfire:knowsystem/connexion-96.md | indetermine |
| consultation avocat en visioconférence | progbat | consultation avocat en visioconférence (Caarl) | progbat:le-menu-principal/service-juridique/consultations-avocats-en-visioconference.md | indetermine |
| consultation bancaire | obat | consultation bancaire (page de catégorie) | obat:`la-consultation-bancaire-sur-obat.md` | indetermine |
| consultation de l'historique des actions | vertuoza | consultation de l'historique des actions/envois sur un document | vertuoza:documents/historique.md | indetermine |
| consultation des informations de chantier | vertuoza | consultation des informations de chantier (carnet de route) sur mobile | vertuoza:application-mobile/ouvrier-consulter-les-informations-de-chantiers.md | chantier-intervention |
| consultation des photos ajoutées en commentaire sur une fiche contact | vertuoza | consultation des photos ajoutées en commentaire sur une fiche contact | vertuoza:faq-foires-aux-questions/ou-puis-je-trouver-les-photos-ajoutees-a-un-de-mes-contacts-en-commentaires.md | indetermine |
| consultation du nombre de comptes utilisateurs restants disponibles | vertuoza | consultation du nombre de comptes utilisateurs restants disponibles | vertuoza:parametres/combien-d-utilisateur-puis-je-encore-creer.md | indetermine |
| consultation du planning de l'ouvrier sur mobile | vertuoza | consultation du planning de l'ouvrier sur mobile | vertuoza:application-mobile/ouvrier-planning-de-l-ouvrier.md | chantier-intervention |
| consultation et gestion des candidatures reçues sur une annonce vertuowork | vertuoza | consultation et gestion des candidatures reçues sur une annonce VertuoWork | vertuoza:vertuowork/comment-consulter-et-gerer-les-candidatures-a-mon-annonce-sur-vertuowork.md | indetermine |
| consultation et suivi des stocks | openfire | consultation et suivi des stocks (quantités, mouvements, inventaire à la date) | openfire:knowsystem/consulter-mes-stocks-225.md | achat |
| contestation de fraude | axonaut | contestation de fraude (carte de paiement, chargeback) | axonaut:compte-pro-cartes/comment-contester-une-operation-frauduleuse-sur-une-carte-de-paiement-axonaut.md | indetermine |
| contournement pour déduire un acompte ttc quand le système demande un montant ht | vertuoza | contournement pour déduire un acompte TTC quand le système demande un montant HT | vertuoza:faq-foires-aux-questions/comment-deduire-un-acompte-en-ttc-d-une-facture-pour-obtenir-le-bon-montant-final-lorsque-le-montant-ht-est-requis-pour-l-avenant.md | chantier-intervention |
| contournement pour qu'un bon de sortie de stock reste « réservé » | vertuoza | contournement pour qu'un bon de sortie de stock reste « réservé » (via commande chantier) | vertuoza:faq-foires-aux-questions/comment-puis-je-faire-en-sorte-qu-un-bon-de-sortie-de-stock-soit-reserve-et-non-termine.md | achat |
| contournement pour revenir à l'état précédent d'un avenant | vertuoza | contournement pour revenir à l'état précédent d'un avenant | vertuoza:faq-foires-aux-questions/comment-modifier-un-avenant-et-revenir-a-l-etat-precedent-lorsqu-elle-n-est-pas-disponible.md | chantier-intervention |
| contournement pour une remise globale non répartie ligne par ligne | vertuoza | contournement pour une remise globale non répartie ligne par ligne | vertuoza:faq-foires-aux-questions/comment-appliquer-une-remise-globale-sans-qu-elle-soit-repartie-sur-chaque-ligne-du-devis.md | devis |
| contrat d'entretien | openfire | contrat d'entretien (comparatif simple/avancé) | openfire:utiliser-openfire/planifier-vos-contrats-d-entretien-choisir-entre-le-mode-simple-ou-avance.md | indetermine |
| contrat simplifié | openfire | contrat simplifié (DI récurrente, cycle complet) | openfire:utiliser-openfire/contrat-simplifie-gerer-vos-contrats-de-maintenance-avec-les-demandes-d-intervention-di-recurrentes.md | chantier-intervention |
| contrats de maintenance | inter-fast | contrats de maintenance (échéancier de facturation indépendant des visites) | inter-fast:inter-fast/operations/comprendre-les-contrats-de-maintenance.md | chantier-intervention |
| contrôle de la planification des interventions | openfire | contrôle de la planification des interventions (retard, à programmer) | openfire:knowsystem/controler-mes-interventions-81.md | chantier-intervention |
| coordonnées bancaires | sellsy | coordonnées bancaires (RIB / IBAN) | sellsy:documents-de-vente/ajouter-mes-coordonnees-bancaires-sur-un-document-rib-iban.md | facturation |
| coordonnées gps | extrabat | coordonnées GPS (mise à jour depuis Extrabat Today) | extrabat:je-veux-mettre-a-jour-mes-coordonnees-gps-dans-la-fiche-extrabat-a-partir-dextrabat-today.md | chantier-intervention |
| copier-coller | extrabat | copier-coller (articles, pièces commerciales) | extrabat:utiliser-le-copier-coller.md | indetermine |
| correction d'une erreur dans un avenant et ses états d'avancement | vertuoza | correction d'une erreur dans un avenant et ses états d'avancement | vertuoza:faq-foires-aux-questions/comment-corriger-une-erreur-dans-un-avenant-et-ses-etats-d-avancement-associes.md | chantier-intervention |
| correction d'une facture validée d'avancement | vertuoza | correction d'une facture validée d'avancement (note de crédit, avancement négatif) | vertuoza:faq-foires-aux-questions/comment-modifier-une-facture-validee-ou-une-note-de-credit-sur-une-facture-d-avancement.md | facturation |
| correction de la synchronisation comptable pour clients non assujettis à la tva | vertuoza | correction de la synchronisation comptable pour clients non assujettis à la TVA | vertuoza:faq-foires-aux-questions/comment-corriger-la-synchronisation-comptable-pour-les-clients-non-assujettis-a-la-tva.md | facturation |
| correction des écarts de stock négatifs | vertuoza | correction des écarts de stock négatifs (bon de sortie manuel lié au chantier) | vertuoza:faq-foires-aux-questions/wat-te-doen-als-mijn-voorraad-negatieve-hoeveelheden-of-ontbrekende-producten-aangeeft.md | achat |
| couleurs d'affichage | openfire | couleurs d'affichage (interventions, planning web) | openfire:guides-videos/modifier-les-couleurs-d-affichage-des-interventions.md | chantier-intervention |
| couleurs d'affichage des interventions | openfire | couleurs d'affichage des interventions (titre incohérent avec le corps, voir incidents) | openfire:guides-videos/faire-un-devis-complementaire.md | chantier-intervention |
| coût horaire des ressources | obat | coût horaire des ressources | obat:`comment-modifier-le-co-c3-bbt-horaire-de-vos-ressources.md` | indetermine |
| coût sav | extrabat | coût SAV (sous garantie) | extrabat:calculez-le-cout-de-son-sav-sous-garantie.md | chantier-intervention |
| coûts internes | sellsy | coûts internes (calcul marge) | sellsy:module-achats/prendre-en-compte-les-couts-internes-dans-le-calcul-de-marge.md | achat |
| crm | axonaut | CRM (agenda, répertoire, opportunités, marketing — tour de fonctionnalités) | axonaut:optimisez-gestion-commerciale/comment-ca-marche-commercial.md | indetermine |
| création | inter-fast | création/modification/export/suppression d'articles (bibliothèque) | inter-fast:inter-fast/outils/creer-et-utiliser-les-articles.md | devis |
| création automatique d'opportunités par transfert d'email | vertuoza | création automatique d'opportunités par transfert d'email/formulaire de contact | vertuoza:crm/creez-vos-opportunites-automatiquement-via-votre-formulaire-de-contact.md | demande |
| création d'un avenant | vertuoza | création d'un avenant / avancement sur une commande sous-traitant | vertuoza:faq-foires-aux-questions/comment-creer-un-avenant-ou-effectuer-l-avancement-d-une-commande-sous-traitant-dans-vertuoza.md | chantier-intervention |
| création d'un avoir | openfire | création d'un avoir (partiel, annulation, modification de facture) | openfire:knowsystem/creer-un-avoir-130.md | facturation |
| création d'un bon de retour de stock | vertuoza | création d'un bon de retour de stock (paramétrage préalable et procédure) | vertuoza:stock/bon-de-retour.md | achat |
| création d'un bon de sortie de stock vers un chantier | vertuoza | création d'un bon de sortie de stock vers un chantier/intervention | vertuoza:stock/bon-de-sortie-de-stock.md | chantier-intervention |
| création d'un carnet de route journalier pour un chantier | vertuoza | création d'un carnet de route journalier pour un chantier (tâches, commentaires par ressource) | vertuoza:planning/creation-d-un-carnet-de-route.md | chantier-intervention |
| création d'un contact | vertuoza | création d'un contact (fiche individuelle) | vertuoza:contacts/ajouter-un-contact.md | indetermine |
| création d'un devis | openfire | création d'un devis (client, dates, taxes, lignes, envoi) | openfire:knowsystem/creer-un-devis-1.md | devis |
| création d'un devis depuis une opportunité crm | openfire | création d'un devis depuis une opportunité CRM | openfire:knowsystem/creer-un-devis-depuis-une-opportunite-128.md | devis |
| création d'un modèle de devis personnalisé | vertuoza | création d'un modèle de devis personnalisé (mise en page, zones, image de fond) | vertuoza:parametres/comment-creer-un-modele-de-devis-personnalise.md | devis |
| création d'une entreprise | vertuoza | création d'une entreprise (fiche société) | vertuoza:contacts/ajouter-une-entreprise.md | indetermine |
| création d'une facture acquittée | vertuoza | création d'une facture acquittée (mise en page, facture finale à 0€) | vertuoza:faq-foires-aux-questions/comment-creer-une-facture-acquittee.md | facturation |
| création d'une facture acquittée à 0€ avec historique des règlements | vertuoza | création d'une facture acquittée à 0€ avec historique des règlements | vertuoza:faq-foires-aux-questions/comment-creer-et-personnaliser-une-facture-acquittee-a-0-avec-l-historique-des-reglements-et-des-montants-precis-et-detailles.md | facturation |
| création d'une facture avec retenue de garantie | openfire | création d'une facture avec retenue de garantie | openfire:knowsystem/creer-une-facture-avec-retenue-de-garantie-220.md | facturation |
| création d'une facture boutique | openfire | création d'une facture boutique (vente comptoir avec sortie de stock) | openfire:knowsystem/factures-client-boutique-286.md | facturation |
| création d'une facture d'acompte | openfire | création d'une facture d'acompte | openfire:knowsystem/facturer-un-acompte-133.md | facturation |
| création d'une facture d'acompte depuis la gestion de chantier | vertuoza | création d'une facture d'acompte depuis la gestion de chantier | vertuoza:gestion-de-chantier/factures-d-acomptes.md | facturation |
| création d'une facture de situation | openfire | création d'une facture de situation (facturation intermédiaire de chantier) | openfire:knowsystem/creer-une-facture-de-situation-204.md | facturation |
| création d'une facture finale de chantier | vertuoza | création d'une facture finale de chantier | vertuoza:gestion-de-chantier/factures-finales.md | facturation |
| création d'une facture proforma | vertuoza | création d'une facture proforma (non comptabilisée, non numérotée) | vertuoza:faq-foires-aux-questions/comment-creer-une-facture-proforma-sur-vertuoza.md | facturation |
| création d'une note de crédit pour une facture d'avancement | vertuoza | création d'une note de crédit pour une facture d'avancement | vertuoza:faq-foires-aux-questions/comment-crediter-une-facture-d-avancement.md | facturation |
| création d'une opportunité commerciale | openfire | création d'une opportunité commerciale (manuelle ou automatique) dans le CRM | openfire:knowsystem/creer-une-opportunite-106.md | demande |
| création de catalogue et sous-catalogue d'articles | inter-fast | création de catalogue et sous-catalogue d'articles | inter-fast:inter-fast/outils/creer-un-catalogue-d-articles.md | indetermine |
| création de demandes de prix et commandes auprès de sous-traitants | vertuoza | création de demandes de prix et commandes auprès de sous-traitants | vertuoza:gestion-de-chantier/commandes-sous-traitants.md | achat |
| création de demandes de prix et commandes de matériaux | vertuoza | création de demandes de prix et commandes de matériaux (fournisseurs) | vertuoza:gestion-de-chantier/commandes-de-materiaux.md | achat |
| création de dossiers de fiches techniques liés à un chantier | vertuoza | création de dossiers de fiches techniques liés à un chantier | vertuoza:fiches-techniques/dossiers-de-fiche-techniques.md | chantier-intervention |
| création de factures récurrentes sur un même contrat | vertuoza | création de factures récurrentes sur un même contrat | vertuoza:faq-foires-aux-questions/comment-generer-des-factures-sur-un-meme-contrat-tout-au-long-de-l-annee.md | facturation |
| création de fiches employés | vertuoza | création de fiches employés (coordonnées, gestion des accès) | vertuoza:parametres/employes.md | indetermine |
| création de fiches indépendants | vertuoza | création de fiches indépendants (coordonnées, horaire) | vertuoza:parametres/independants.md | indetermine |
| création de fiches ouvriers | vertuoza | création de fiches ouvriers (coordonnées, horaire) | vertuoza:parametres/ouvriers.md | indetermine |
| création de la facture finale après acompte | openfire | création de la facture finale après acompte | openfire:knowsystem/creer-ma-facture-finale-145.md | facturation |
| création de modèles d'e-mails réutilisables par type de document | vertuoza | création de modèles d'e-mails réutilisables par type de document | vertuoza:parametres/modeles-d-e-mails.md | indetermine |
| création de pourcentages de probabilité de signature liés aux opportunités | vertuoza | création de pourcentages de probabilité de signature liés aux opportunités | vertuoza:devis/pourcentages.md | demande |
| création du rapport d'intervention sur mobile | vertuoza | création du rapport d'intervention sur mobile (accompagnants, coûts, facturation, signature) | vertuoza:application-mobile/ouvrier-rapport-d-intervention.md | chantier-intervention |
| création et affichage des normes techniques sur les documents | openfire | création et affichage des normes techniques sur les documents | openfire:knowsystem/parametrer-une-norme-165.md | devis |
| création et alimentation des listes de diffusion | openfire | création et alimentation des listes de diffusion (manuelle, import, formulaire web) | openfire:knowsystem/liste-de-diffusion-229.md | demande |
| création et catégorisation des tâches d'intervention | openfire | création et catégorisation des tâches d'intervention | openfire:knowsystem/gestion-des-taches-69.md | chantier-intervention |
| création et configuration d'un tableau de bord | openfire | création et configuration d'un tableau de bord | openfire:knowsystem/creer-et-configurer-un-tableau-287.md | indetermine |
| création et configuration d'une marque | openfire | création et configuration d'une marque (conditions d'achat/vente, règles de gestion) | openfire:knowsystem/parametrer-une-marque-5.md | devis |
| création et configuration des journaux comptables | openfire | création et configuration des journaux comptables | openfire:knowsystem/journaux-comptables-205.md | facturation |
| création et configuration des questionnaires et questions d'intervention | openfire | création et configuration des questionnaires et questions d'intervention | openfire:knowsystem/questionnaires-74.md | chantier-intervention |
| création et configuration des responsables d'intervention | vertuoza | création et configuration des responsables d'intervention (compétences, autorisations) | vertuoza:gestion-des-interventions/responsable-d-intervention.md | chantier-intervention |
| création et envoi d'un publipostage | openfire | création et envoi d'un publipostage (mailing de masse) | openfire:knowsystem/creer-un-publipostage-228.md | demande |
| création et envoi d'une commande de matériaux au fournisseur depuis l'app mobile | vertuoza | création et envoi d'une commande de matériaux au fournisseur depuis l'app mobile | vertuoza:application-mobile/creation-d-une-commande-materiaux-et-envoi-au-fournisseur-avec-l-app-mobile.md | achat |
| création et gestion d'un avenant | vertuoza | création et gestion d'un avenant (modification du contrat initial) | vertuoza:gestion-de-chantier/avenant.md | chantier-intervention |
| création et gestion d'une fiche d'installation | vertuoza | création et gestion d'une fiche d'installation (client, TVA, photos, fichiers) | vertuoza:gestion-des-interventions/creation-d-une-installation.md | chantier-intervention |
| création et gestion d'une ligne de contrat | openfire | création et gestion d'une ligne de contrat (facturation, planification, équipement) | openfire:knowsystem/creer-ligne-de-contrat-308.md | chantier-intervention |
| création et gestion d'une opportunité commerciale | vertuoza | création et gestion d'une opportunité commerciale (montant, statut, tâches) | vertuoza:crm/opportunites.md | demande |
| création et gestion des ordres d'approvisionnement | openfire | création et gestion des ordres d'approvisionnement (automatique, manuel) | openfire:knowsystem/ordre-d-approvisionnement-253.md | achat |
| création et gestion des remises en banque | openfire | création et gestion des remises en banque (regroupement de paiements) | openfire:knowsystem/remise-en-banque-304.md | facturation |
| création et gestion des équipes commerciales | openfire | création et gestion des équipes commerciales | openfire:knowsystem/equipes-commerciales-176.md | demande |
| création et gestion des étapes du pipeline commercial | openfire | création et gestion des étapes du pipeline commercial | openfire:knowsystem/parametrer-les-etapes-119.md | demande |
| création et gestion du parc installé | openfire | création et gestion du parc installé (équipements chez le client) | openfire:knowsystem/gerer-mon-parc-installe-72.md | chantier-intervention |
| création et génération des périodes comptables | openfire | création et génération des périodes comptables | openfire:knowsystem/gerer-les-periodes-comptables-170.md | facturation |
| création et hiérarchisation des immobilisations comptables | openfire | création et hiérarchisation des immobilisations comptables | openfire:knowsystem/immobilisations-223.md | indetermine |
| création et mise en forme des modèles de commentaires de devis | openfire | création et mise en forme des modèles de commentaires de devis | openfire:knowsystem/modeles-de-commentaire-186.md | devis |
| création et optimisation des tournées d'intervention | openfire | création et optimisation des tournées d'intervention | openfire:knowsystem/optimisation-des-tournees-285.md | chantier-intervention |
| création et paramétrage d'un article | openfire | création et paramétrage d'un article (produit, service, consommable) | openfire:knowsystem/creer-un-article-6.md | devis |
| création et paramétrage d'un contrat récurrent | openfire | création et paramétrage d'un contrat récurrent (facturation, renouvellement) | openfire:knowsystem/creer-un-contrat-302.md | chantier-intervention |
| création et paramétrage d'une fiche fournisseur | openfire | création et paramétrage d'une fiche fournisseur | openfire:knowsystem/creer-un-fournisseur-61.md | achat |
| création et paramétrage de modèles de courriers pdf | openfire | création et paramétrage de modèles de courriers PDF (impression, remplissage automatique) | openfire:knowsystem/modele-de-courriers-182.md | indetermine |
| création et permissions d'un utilisateur avec compte gestion | vertuoza | création et permissions d'un utilisateur avec compte gestion (accès complet) | vertuoza:parametres/utilisateur-avec-un-compte-gestion.md | indetermine |
| création et permissions d'un utilisateur avec compte ouvrier | vertuoza | création et permissions d'un utilisateur avec compte ouvrier (accès restreint) | vertuoza:parametres/utilisateur-avec-un-compte-ouvrier.md | indetermine |
| création et personnalisation des widgets d'un tableau de bord | openfire | création et personnalisation des widgets d'un tableau de bord | openfire:knowsystem/creer-et-personnaliser-un-widget-256.md | indetermine |
| création et structuration d'une demande d'intervention | openfire | création et structuration d'une demande d'intervention (types, planification, facturation) | openfire:knowsystem/demandes-dintervention-78.md | chantier-intervention |
| création et structuration d'une fiche contact | openfire | création et structuration d'une fiche contact | openfire:knowsystem/creer-un-contact-16.md | indetermine |
| création et structuration du plan comptable | openfire | création et structuration du plan comptable (comptes, types, multisociété) | openfire:knowsystem/plan-comptable-279.md | facturation |
| création et suivi d'une intervention depuis l'application mobile | openfire | création et suivi d'une intervention depuis l'application mobile | openfire:knowsystem/creer-une-intervention-299.md | chantier-intervention |
| création et suivi de campagnes marketing | openfire | création et suivi de campagnes marketing (publipostage) | openfire:knowsystem/creer-et-suivre-une-campagne-234.md | demande |
| création et suivi des commandes de réapprovisionnement de stock auprès des fournisseurs | vertuoza | création et suivi des commandes de réapprovisionnement de stock auprès des fournisseurs | vertuoza:stock/commande-de-stock.md | achat |
| création et suivi des tâches administratives liées à un chantier | vertuoza | création et suivi des tâches administratives liées à un chantier | vertuoza:gestion-de-chantier/taches.md | chantier-intervention |
| création et utilisation de modèles de pièces comptables | openfire | création et utilisation de modèles de pièces comptables | openfire:knowsystem/generer-une-piece-comptable-depuis-un-modele-268.md | facturation |
| création et utilisation des conditions particulières de paiement sur devis | vertuoza | création et utilisation des conditions particulières de paiement sur devis | vertuoza:devis/conditions-particulieres.md | devis |
| création et utilisation des kits d'articles dans les devis | openfire | création et utilisation des kits d'articles dans les devis | openfire:knowsystem/gerer-les-kits-4.md | devis |
| création et utilisation des modèles de devis | openfire | création et utilisation des modèles de devis | openfire:knowsystem/les-modeles-de-devis-2.md | devis |
| création et workflow de validation d'une facture fournisseur | vertuoza | création et workflow de validation d'une facture fournisseur | vertuoza:finance/creation-d-une-nouvelle-facture-fournisseur.md | achat |
| création, import et export des composants | vertuoza | création, import et export des composants (éléments constitutifs des ouvrages) | vertuoza:bibliotheque-de-prix/composants.md | devis |
| création, import et export des ouvrages | vertuoza | création, import et export des ouvrages (bibliothèque de prix) | vertuoza:bibliotheque-de-prix/ouvrages.md | devis |
| création, structuration et gestion complète d'un devis | vertuoza | création, structuration et gestion complète d'un devis (lignes, marges, statuts) | vertuoza:devis/devis.md | devis |
| création, structure et gestion des factures client | openfire | création, structure et gestion des factures client (pro-forma, manuelle, boutique, depuis commande) | openfire:knowsystem/factures-client-132.md | facturation |
| création, validation et facturation d'un état d'avancement de chantier | vertuoza | création, validation et facturation d'un état d'avancement de chantier | vertuoza:gestion-de-chantier/avancement.md | chantier-intervention |
| crédits | sellsy | crédits (compte Sellsy) | sellsy:configuration-du-compte/ajouter-des-credits-a-mon-compte-sellsy.md | indetermine |
| créneau | openfire | créneau (recherche, optimisation planning) | openfire:utiliser-openfire/rechercher-un-creneau-disponible.md | chantier-intervention |
| cybersécurité | sellsy | cybersécurité (bonnes pratiques) | sellsy:conseils-d-utilisation/securiser-les-donnees-de-votre-entreprise.md | indetermine |
| cycle complet de gestion d'un chantier | inter-fast | cycle complet de gestion d'un chantier (demande → devis → chantier → exécution → facturation → rentabilité) | inter-fast:inter-fast/operations/guide-complet-gerer-un-chantier-dans-interfast.md | indetermine |
| cycle d'avancement | sellsy | cycle d'avancement (facturation, suivi) | sellsy:documents-de-vente/suivre-les-cycles-d-avancement.md | facturation |
| date de règlement | openfire | date de règlement (impression facture, personnalisation) | openfire:knowsystem/comment-supprimer-la-date-de-reglement-a-l-impression-des-factures-206.md | facturation |
| date de visite préalable | obat | date de visite préalable (devis) | obat:`comment-indiquer-la-date-de-visite-pr-c3-a9alable-sur-le-devis.md` | devis |
| date du jour | extrabat | date du jour (modèle courrier Word) | extrabat:inserer-la-date-du-jour-dans-un-modele-de-courrier-cree-sous-word.md | indetermine |
| dates de service | sellsy | dates de service (document de vente) | sellsy:documents-de-vente/afficher-les-dates-de-service-sur-un-document-de-vente.md | facturation |
| demande d'avis client | costructor | demande d'avis client (e-réputation) | costructor:debuter-sur-costructor/comment-envoyer-une-demande-davis-1rmfknu.md | facturation |
| demande de matériel | inter-fast | demande de matériel (création et suivi depuis une intervention, app mobile) | inter-fast:inter-fast/application-mobile/gerer-vos-demandes-de-materiel-app-mobile.md | chantier-intervention |
| demande de prix | openfire | demande de prix / réapprovisionnement | openfire:utiliser-openfire/choisir-son-mode-de-reapprovisionnement.md | achat |
| demandes de matériel | inter-fast | demandes de matériel (préparation, récupération, liaison chantier) | inter-fast:inter-fast/outils/gerer-vos-demandes-de-materiel-app-web.md | chantier-intervention |
| description | sellsy | description / nom commercial (conformité FacturX) | sellsy:facturation-electronique/description-et-nom-commercial-dans-les-documents-de-vente.md | facturation |
| devis et facture | batikko | devis et facture (cycle de vie, TVA BTP) | batikko:guides/devis-factures.md | facturation |
| devis généré par ia | costructor | devis généré par IA (prompt, pièce jointe, vocal) | costructor:ventes/comment-creer-un-devis-ia-9jz7n7.md | devis |
| devis importé | inter-fast | devis importé (facturation en continu, liaison acompte) | inter-fast:inter-fast/finances/poursuivre-la-facturation-d-un-devis-importe.md | facturation |
| devis type | progbat | devis type / BPU (bibliothèque de contenus de devis réutilisables) | progbat:le-menu-principal/devis-factures/devis-type-et-bpu.md | devis |
| devis vocal | batikko | devis vocal (génération par IA, dictée) | batikko:guides/devis-vocal-ia.md | devis |
| devise de facturation | axonaut | devise de facturation (compte et par client) | axonaut:gerez-vos-factures/changer-de-devise-sur-axonaut.md | facturation |
| dictionnaire des fonctionnalités | inter-fast | dictionnaire des fonctionnalités (glossaire, définitions métier) | inter-fast:inter-fast/debuter-avec-interfast/le-dictionnaire-des-fonctionnalites-d-interfast.md | indetermine |
| dimensionnement vitalome | openfire | dimensionnement Vitalome (formulaire, devis auto) | openfire:utiliser-openfire/vital-etudes-outil-d-aide-au-dimensionnement-vitalome.md | chantier-intervention |
| distinction chiffre d'affaires | vertuoza | distinction chiffre d'affaires (devis+avenants) vs total des ventes facturées | vertuoza:faq-foires-aux-questions/pourquoi-y-a-t-il-une-difference-entre-le-montant-du-chiffre-d-affaires-affiche-et-le-total-des-ventes-facturees.md | facturation |
| distinction des statuts d'affichage mobile d'un rapport d'intervention payé | vertuoza | distinction des statuts d'affichage mobile d'un rapport d'intervention payé (envoyé ou non) | vertuoza:faq-foires-aux-questions/pourquoi-certains-rapports-d-interventions-affichent-termine-et-d-autres-renvoyer-la-facture-sur-mobile.md | facturation |
| distinction entre commande de chantier | vertuoza | distinction entre commande de chantier (livraison directe) et commande de réapprovisionnement de stock | vertuoza:faq-foires-aux-questions/quelle-est-la-difference-entre-une-commande-de-chantier-et-une-commande-d-approvisionnement-de-stock.md | achat |
| distinction entre commande de matériaux | vertuoza | distinction entre commande de matériaux (devis) et commande de stock (visibilité du stock) | vertuoza:faq-foires-aux-questions/pourquoi-je-ne-vois-pas-le-stock-disponible-lorsque-je-passe-une-commande-de-materiaux.md | achat |
| distinction entre facture d'acompte | vertuoza | distinction entre facture d'acompte (déduite) et facture d'avancement (non déduite) | vertuoza:faq-foires-aux-questions/pourquoi-certaines-factures-d-acompte-apparaissent-dans-la-section-deduction-des-acomptes-alors-que.md | facturation |
| distinction entre marge brute | vertuoza | distinction entre marge brute (historique) et bénéfice complet (tableau de bord) | vertuoza:faq-foires-aux-questions/quelle-est-la-difference-entre-la-marge-affichee-dans-l-historique-des-chantiers-et-le-benefice-indique-dans-le-tableau-de-bord-du-chantier-dans-vertuoza.md | chantier-intervention |
| distinction entre reste à produire | vertuoza | distinction entre reste à produire (basé sur avancement) et statut de facturation | vertuoza:faq-foires-aux-questions/pourquoi-certains-chantiers-affichent-ils-un-reste-a-produire-alors-qu-ils-sont-deja-factures.md | chantier-intervention |
| distinction entre « reste à produire » | vertuoza | distinction entre « reste à produire » (avancement) et « reste à facturer » (facturation) | vertuoza:faq-foires-aux-questions/pourquoi-mon-chantier-affiche-t-il-encore-un-reste-a-produire-alors-qu-il-est-facture-a-100.md | chantier-intervention |
| distinction facture simple | vertuoza | distinction facture simple (libre) vs facture d'avancement (basée sur état d'avancement) | vertuoza:faq-foires-aux-questions/quelle-est-la-difference-entre-une-facture-d-avancement-et-une-facture-simple.md | facturation |
| distinction référence | vertuoza | distinction référence (interne) vs description (visible client) sur un composant | vertuoza:faq-foires-aux-questions/quelle-est-la-difference-entre-une-reference-et-une-description.md | devis |
| document de gestion | axonaut | document de gestion (K-bis, documents publics, fiche client) | axonaut:optimisez-gestion-commerciale/ajouter-mes-documents-de-gestion.md | indetermine |
| document ht | sellsy | document HT (export) | sellsy:documents-de-vente/creer-un-document-ht-pour-l-export.md | facturation |
| document principal | sellsy | document principal (opportunité) | sellsy:crm-et-prospection/definir-un-document-en-tant-que-document-principal-d-une-opportunite.md | indetermine |
| document privé | progbat | document privé (devis/facture, statut public/privé, héritage) | progbat:presentation-generale/les-documents-prives.md | indetermine |
| documents | sellsy | documents (impression en masse) | sellsy:documents-de-vente/imprimer-des-documents-en-masse-devis-factures-etc.md | facturation |
| documents annexes | obat | documents annexes / galerie de chantier | obat:`comment-ajouter-vos-documents-annexes-dans-vos-chantiers.md` | chantier-intervention |
| documents liés au chantier | obat | documents liés au chantier (centralisation) | obat:`comment-retrouver-vos-documents-facilement-sur-le-menu-chantier.md` | chantier-intervention |
| données | sellsy | données (import, introduction générale) | sellsy:gestion-des-donnees/importer-des-donnees.md | indetermine |
| données de démonstration | axonaut | données de démonstration (suppression, cas bloquant facture) | axonaut:configurer-votre-compte/demo-effacer-les-donnees-factices.md | indetermine |
| doublons | sellsy | doublons (répertoire, détection) | sellsy:repertoire/repertoire-utilisation-de-la-liste-des-doublons.md | indetermine |
| doublons clients | extrabat | doublons clients/prospects (gestion) | extrabat:gerer-les-doublons-dans-les-bases-clients-prospects.md | indetermine |
| douchette | openfire | douchette / scanner (configuration groupes d'options code-barres) | openfire:configurer-openfire/installation-et-configuration-de-la-gestion-des-inventaires-par-douchette.md | indetermine |
| dpgf | inter-fast | DPGF (import structuré, chiffrage, export retour) | inter-fast:inter-fast/finances/importer-et-gerer-un-dpgf.md | devis |
| droits | axonaut | droits/responsabilités utilisateur (rôles, personnel vs utilisateur) | axonaut:configurer-votre-compte/droits-responsabilites-utilisateurs-a-quoi-ca-correspond-2.md | indetermine |
| droits agenda | extrabat | droits agenda (partage) | extrabat:droits-de-lagenda.md | indetermine |
| droits utilisateur | axonaut | droits utilisateur (Compte Pro, invitation, vérification identité) | axonaut:compte-pro-cartes/la-gestion-des-droits-utilisateurs-pour-le-compte-pro-axonaut.md | indetermine |
| drom-com | sellsy | DROM-COM (obligations réforme facturation électronique) | sellsy:facturation-electronique/departements-et-regions-d-outre-mer.md | indetermine |
| duplication facture | obat | duplication facture/devis | obat:`comment-dupliquer-une-facture-finale/devis.md` | indetermine |
| duplication planning de chantier | obat | duplication planning de chantier | obat:`r-c3-a9utiliser-le-planning-dun-chantier.md` | chantier-intervention |
| durée de garantie | extrabat | durée de garantie (article) | extrabat:mettre-a-jour-la-duree-de-garantie-dun-article.md | indetermine |
| déboursé | extrabat | déboursé (devis, répartition par type d'article) | extrabat:je-veux-voir-mon-debourse-a-partir-dun-devis.md | devis |
| décalage entre ordre d'affichage et numérotation des devis après modification de dates | vertuoza | décalage entre ordre d'affichage et numérotation des devis après modification de dates (contournement) | vertuoza:faq-foires-aux-questions/pourquoi-l-ordre-des-devis-est-il-decale-apres-avoir-modifie-les-dates.md | devis |
| décimales | sellsy | décimales (affichage document) | sellsy:documents-de-vente/modifier-le-nombre-de-decimales-dans-un-document.md | facturation |
| déclaration d'absence | inter-fast | déclaration d'absence (activation, saisie) | inter-fast:inter-fast/operations/declarer-une-absence.md | indetermine |
| déclaration de tva | axonaut | déclaration de TVA (tableau collecté/déductible, codes comptables requis) | axonaut:gerez-votre-comptabilite/comment-faciliter-sa-declaration-de-tva-avec-axonaut.md | indetermine |
| déclinaison | sellsy | déclinaison (produit) | sellsy:catalogue-produits-et-services/creer-et-gerer-les-declinaisons-de-mes-produits.md | indetermine |
| décompte général définitif dgd | inter-fast | décompte général définitif DGD (bilan financier de fin de chantier) | inter-fast:inter-fast/operations/creer-un-decompte-general-definitif-dgd.md | facturation |
| déconnexion | obat | déconnexion (page technique) | obat:`hcms/mem/logout.md` | indetermine |
| déduction d'acompte | obat | déduction d'acompte / facture finale | obat:`comment-d-c3-a9duire-un-acompte-d-une-facture-finale.md` | facturation |
| déduction d'une prime sur la facture finale via un devis | vertuoza | déduction d'une prime sur la facture finale via un devis | vertuoza:faq-foires-aux-questions/peut-on-deduire-une-prime-dans-un-devis.md | devis |
| définition d'un modèle de devis par défaut | vertuoza | définition d'un modèle de devis par défaut | vertuoza:faq-foires-aux-questions/comment-definir-un-modele-de-devis-par-defaut-dans-le-logiciel.md | devis |
| définition de l'ajustement prorata | vertuoza | définition de l'ajustement prorata (recalcul des prix unitaires devis→facture) | vertuoza:faq-foires-aux-questions/que-signifie-ajustement-prorata-dans-le-cadre-de-la-facturation.md | facturation |
| définition de la retenue de garantie sur un devis | vertuoza | définition de la retenue de garantie sur un devis | vertuoza:faq-foires-aux-questions/a-quoi-sert-une-retenue-de-garantie-dans-un-devis.md | devis |
| définition des conditions tarifaires par marque, catégorie ou article | openfire | définition des conditions tarifaires par marque, catégorie ou article | openfire:knowsystem/definir-ses-conditions-tarifaires-169.md | devis |
| définition et causes du statut d'envoi email « soft bounce » | vertuoza | définition et causes du statut d'envoi email « soft bounce » | vertuoza:faq-foires-aux-questions/mes-mails-ont-le-statut-soft-bounce-qu-est-ce-que-cela-signifie.md | indetermine |
| définition total brut ht vs total net ht | vertuoza | définition Total Brut HT vs Total Net HT (identiques en l'absence de remise) | vertuoza:faq-foires-aux-questions/pourquoi-le-total-brut-ht-et-le-total-net-ht-sont-ils-identiques-dans-mon-devis.md | devis |
| délettrage | extrabat | délettrage (droits d'accès) | extrabat:brouillon-2.md | indetermine |
| dépannage d'accès au lien de devis | vertuoza | dépannage d'accès au lien de devis (réseau, pare-feu, proxy client) | vertuoza:faq-foires-aux-questions/pourquoi-ne-puis-je-pas-ouvrir-mon-devis-depuis-le-lien-dans-l-email-de-reception.md | devis |
| dépannage d'affichage pdf incomplet lié à une modification manuelle du modèle | vertuoza | dépannage d'affichage PDF incomplet lié à une modification manuelle du modèle | vertuoza:faq-foires-aux-questions/pourquoi-seules-certaines-informations-comme-la-tva-apparaissent-dans-mon-pdf-de-devis.md | devis |
| dépannage d'application incorrecte de la marge sur les lignes de facture | vertuoza | dépannage d'application incorrecte de la marge sur les lignes de facture | vertuoza:faq-foires-aux-questions/pourquoi-ma-marge-de-x-ne-s-applique-t-elle-pas-correctement-dans-le-tableau-des-factures.md | facturation |
| dépannage d'erreur d'envoi liée aux droits d'accès de l'intégration gmail | vertuoza | dépannage d'erreur d'envoi liée aux droits d'accès de l'intégration Gmail | vertuoza:faq-foires-aux-questions/pourquoi-j-obtiens-erreur-lors-de-l-envoi-depuis-que-j-ai-active-l-integration-gmail.md | indetermine |
| dépannage d'import d'inventaire | vertuoza | dépannage d'import d'inventaire (identifiants fournitures manquants dans CSV) | vertuoza:faq-foires-aux-questions/pourquoi-ne-puis-je-pas-importer-mon-inventaire.md | achat |
| dépannage d'une erreur de duplication d'ouvrage | vertuoza | dépannage d'une erreur de duplication d'ouvrage (incohérence fournisseur composant/bibliothèque) | vertuoza:faq-foires-aux-questions/pourquoi-ai-je-un-message-d-erreur-lorsque-je-modifie-la-duplication-d-un-ouvrage.md | devis |
| dépannage d'échec d'aperçu pdf | vertuoza | dépannage d'échec d'aperçu PDF (taille fichier, format image) | vertuoza:faq-foires-aux-questions/pourquoi-je-n-arrive-pas-a-obtenir-l-apercu-pdf-de-mon-document.md | indetermine |
| dépannage d'échec d'import d'inventaire | vertuoza | dépannage d'échec d'import d'inventaire (identifiants manquants) | vertuoza:faq-foires-aux-questions/pourquoi-je-n-arrive-pas-a-importer-mon-inventaire.md | achat |
| dépannage de blocage de modification d'ouvrage | vertuoza | dépannage de blocage de modification d'ouvrage (incohérence fournisseur composant) | vertuoza:faq-foires-aux-questions/pourquoi-mes-modifications-ne-sont-elles-pas-appliquees-au-niveau-de-la-modification-d-ouvrage.md | devis |
| dépannage de comportement des liens cliquables dans les commentaires | vertuoza | dépannage de comportement des liens cliquables dans les commentaires (changement tiers Microsoft) | vertuoza:faq-foires-aux-questions/pourquoi-ne-puis-je-plus-copier-coller-des-liens-qui-deviennent-cliquables-dans-mes-bulles-de-commentaires.md | indetermine |
| dépannage de comptabilisation de facture | vertuoza | dépannage de comptabilisation de facture (année fiscale manquante) | vertuoza:faq-foires-aux-questions/je-n-arrive-pas-a-comptabiliser-une-facture-que-faire.md | facturation |
| dépannage de connexion | openfire | dépannage de connexion (URL, identifiants incorrects) | openfire:knowsystem/je-n-arrive-pas-a-me-connecter-200.md | indetermine |
| dépannage de connexion à l'application mobile | openfire | dépannage de connexion à l'application mobile | openfire:knowsystem/je-n-arrive-pas-a-me-connecter-a-l-application-mobile-314.md | indetermine |
| dépannage de correspondance bon de commande | vertuoza | dépannage de correspondance bon de commande / facture fournisseur (fournisseur différent) | vertuoza:faq-foires-aux-questions/pourquoi-je-n-arrive-pas-a-trouver-mon-bon-de-commande-afin-de-pouvoir-le-renseigner-dans-la-lier-facture-fournisseur-alors-qu-il-a-ete-valide.md | achat |
| dépannage de génération de qr code | vertuoza | dépannage de génération de QR code (facture non comptabilisée) | vertuoza:faq-foires-aux-questions/pourquoi-mon-qr-code-ne-se-genere-t-il-pas-apres-avoir-soumis-ma-proposition-de-facture.md | facturation |
| dépannage de l'erreur navigateur « bad request » | vertuoza | dépannage de l'erreur navigateur « Bad Request » | vertuoza:faq-foires-aux-questions/que-signifie-l-erreur-bad-request-your-browser-sent-a-request-that-this-server-could-not-understand-et-comment-la-resoudre.md | indetermine |
| dépannage de l'impression pdf obsolète | openfire | dépannage de l'impression PDF obsolète (pièce jointe figée) | openfire:knowsystem/pourquoi-le-pdf-que-j-imprime-n-est-pas-a-jour-207.md | indetermine |
| dépannage de la disparition du bouton de création d'un nouvel avancement | vertuoza | dépannage de la disparition du bouton de création d'un nouvel avancement | vertuoza:faq-foires-aux-questions/pourquoi-le-bouton-pour-creer-un-nouvel-avancement-a-t-il-disparu.md | chantier-intervention |
| dépannage de la délivrabilité des emails | vertuoza | dépannage de la délivrabilité des emails (spam), recommandations SPF/DKIM/DMARC | vertuoza:faq-foires-aux-questions/mes-e-mails-de-devis-ou-de-factures-arrivent-dans-les-spams-de-mes-clients-que-faire.md | indetermine |
| dépannage de la suppression de signature email de profil | vertuoza | dépannage de la suppression de signature email de profil | vertuoza:faq-foires-aux-questions/comment-supprimer-ma-signature-dans-le-profil-si-ca-ne-fonctionne-pas.md | indetermine |
| dépannage de lenteur | vertuoza | dépannage de lenteur (navigateur recommandé, cache, extensions) | vertuoza:faq-foires-aux-questions/pourquoi-mon-compte-vertuoza-est-il-lent.md | indetermine |
| dépannage de marge négative sur devis | vertuoza | dépannage de marge négative sur devis (erreur de saisie de prix) | vertuoza:faq-foires-aux-questions/pourquoi-ma-marge-beneficiaire-est-elle-negative-dans-un-devis.md | devis |
| dépannage de marge à 0 après import | vertuoza | dépannage de marge à 0 après import (colonne prix d'achat/marge mal configurée) | vertuoza:faq-foires-aux-questions/pourquoi-la-marge-est-elle-a-0-apres-l-import-de-la-bibliotheque.md | devis |
| dépannage de modification automatique de texte | vertuoza | dépannage de modification automatique de texte (correcteur/traducteur navigateur) | vertuoza:faq-foires-aux-questions/pourquoi-les-mots-changent-ils-automatiquement-dans-notre-devis-facture.md | indetermine |
| dépannage de non-création d'opportunité par email | vertuoza | dépannage de non-création d'opportunité par email (email prospect manquant) | vertuoza:faq-foires-aux-questions/pourquoi-une-opportunite-ne-se-cree-t-elle-pas-apres-l-envoi-d-un-email.md | demande |
| dépannage de rentabilité chantier faussée | vertuoza | dépannage de rentabilité chantier faussée (coût horaire ouvrier non défini) | vertuoza:faq-foires-aux-questions/pourquoi-mes-pointages-clotures-ne-sont-ils-pas-encore-pris-en-compte-dans-la-rentabilite-du-chantier.md | chantier-intervention |
| dépannage de sauvegarde de texte | vertuoza | dépannage de sauvegarde de texte (caractères spéciaux non supportés) | vertuoza:faq-foires-aux-questions/que-faire-si-mon-texte-dans-une-ligne-de-mon-devis-ne-se-sauvegarde-pas.md | devis |
| dépannage de statut de facture bloqué « partiellement payé » | vertuoza | dépannage de statut de facture bloqué « partiellement payé » (validation manuelle requise) | vertuoza:faq-foires-aux-questions/pourquoi-une-facture-apparait-elle-en-statut-partiellement-paye-alors-que-le-client-a-regle-le-montant-et-recu-une-note-de-credit.md | facturation |
| dépannage de taux de tva résiduel après désactivation de l'option tva à la ligne | vertuoza | dépannage de taux de TVA résiduel après désactivation de l'option TVA à la ligne | vertuoza:faq-foires-aux-questions/que-puis-je-faire-si-un-taux-de-tva-incorrect-apparait-dans-les-sous-totaux-de-mon-devis.md | devis |
| déplacement chantier | obat | déplacement chantier (planning, drag&drop) | obat:`d-c3-a9placer-un-chantier-dans-sa-globalit-c3-a9-en-dragdrop.md` | chantier-intervention |
| dépôt de facture impayée et suivi | progbat | dépôt de facture impayée et suivi (recouvrement, Caarl) | progbat:le-menu-principal/service-juridique/recouvrement-de-factures-impayees/depot-de-ma-facture-et-suivi.md | facturation |
| dépôt facture chorus pro | axonaut | dépôt facture Chorus Pro (secteur public, obligation légale) | axonaut:gerez-vos-factures/axonaut-chorus-pro-comment-ca-marche.md | facturation |
| désactivation | vertuoza | désactivation (déconnexion) de la facturation électronique | vertuoza:parametres/comment-desactiver-la-facturation-electronique.md | facturation |
| désactivation du bouton de statut de commande liée à un avenant | vertuoza | désactivation du bouton de statut de commande liée à un avenant | vertuoza:faq-foires-aux-questions/pourquoi-le-bouton-pour-modifier-le-statut-d-une-commande-est-il-desactive.md | achat |
| déstockage | sellsy | déstockage / mouvement de stock (entrepôts) | sellsy:module-stocks/destockage-automatique-et-mouvement-de-stocks-inter-entrepots.md | indetermine |
| détails d'ouvrage | costructor | détails d'ouvrage (masquage sur document) | costructor:ventes/comment-masquer-les-details-dun-ouvrage-1nm8dfh.md | indetermine |
| détecteur manuel de fuite | inter-fast | détecteur manuel de fuite (enregistrement, pré-remplissage documents) | inter-fast:inter-fast/fluides-frigorigenes/recenser-un-detecteur-manuel-de-fuite.md | chantier-intervention |
| détection et fusion des doublons de contacts | openfire | détection et fusion des doublons de contacts | openfire:knowsystem/gestion-des-doublons-8.md | indetermine |
| effet de la suppression d'un compte chantier sur la fiche ouvrier | vertuoza | effet de la suppression d'un compte chantier sur la fiche ouvrier | vertuoza:faq-foires-aux-questions/la-suppression-d-un-compte-chantier-supprime-t-elle-egalement-l-ouvrier-associe.md | indetermine |
| email | sellsy | email (liaison à un objet) | sellsy:configuration-du-compte/lier-un-email-a-un-objet-contact-societe-opportunite-document.md | indetermine |
| email automatique | sellsy | email automatique (résultats / scoring) | sellsy:crm-et-prospection/suivre-les-resultats-d-un-email-automatique.md | indetermine |
| email rejeté | extrabat | email rejeté (SPF, domaine) | extrabat:mon-email-revient-delivery-alors-que-ladresse-mail-bonne-fonctionne-autre-mesasagerie.md | indetermine |
| emailing | extrabat | emailing (campagne, éditeur, ciblage) | extrabat:realiser-un-emailing.md | indetermine |
| emails en spam | extrabat | emails en spam (diagnostic, préconisations) | extrabat:pourquoi-mes-mails-arrivent-dans-les-spams.md | indetermine |
| emails support | sellsy | emails support (redirection) | sellsy:module-support/transferer-mes-emails-de-support.md | indetermine |
| encaissement de facture client | progbat | encaissement de facture client (saisie manuelle du règlement) | progbat:le-menu-principal/reglements/encaissement-dune-facture-client.md | facturation |
| encaissements et retards d'encaissement | obat | encaissements et retards d'encaissement | obat:`comment-visualiser-vos-encaissements-et-vos-retards-dencaissement-sur-obat.md` | facturation |
| encodage du personnel et gestion des accès utilisateurs | vertuoza | encodage du personnel et gestion des accès utilisateurs (comptes gestion/ouvrier) | vertuoza:demarrer/personnel-et-utilisateurs-ajoutez-vos-collaborateurs.md | indetermine |
| enregistrement d'écran | inter-fast | enregistrement d'écran (outil tiers Loom, pour le support) | inter-fast:inter-fast/debuter-avec-interfast/enregistrer-votre-ecran-avec-l-outil-loom.md | indetermine |
| enregistrement des dépenses liées à un véhicule | vertuoza | enregistrement des dépenses liées à un véhicule (carburant, réparations) | vertuoza:faq-foires-aux-questions/comment-ajouter-des-depenses-liees-a-un-vehicule-par-exemple-essence.md | indetermine |
| enregistrement, catégorisation et régularisation des paiements de factures | openfire | enregistrement, catégorisation et régularisation des paiements de factures | openfire:knowsystem/enregistrer-un-paiement-161.md | facturation |
| entreprises étrangères | sellsy | entreprises étrangères (réforme facturation électronique) | sellsy:facturation-electronique/entreprises-etrangeres-et-echanges-internationaux-dans-le-cadre-de-la-reforme.md | indetermine |
| entête de devis | progbat | entête de devis (informations, objet, client, chantier) | progbat:le-menu-principal/devis-factures/devis/lentete-du-devis.md | devis |
| entête de facture | progbat | entête de facture (informations, objet, client, chantier) | progbat:le-menu-principal/devis-factures/factures/lentete-de-la-facture.md | facturation |
| envoi automatique | vertuoza | envoi automatique (désactivable) d'un email à la création d'une fiche sous-traitant | vertuoza:faq-foires-aux-questions/un-sous-traitant-recoit-il-automatiquement-un-email-a-sa-creation.md | indetermine |
| envoi d'emails | progbat | envoi d'emails (expéditeur, signature, méthode d'envoi : serveur ProGBat vs boîte mail propre) | progbat:pour-bien-demarrer/parametrage/mon-profil/envoi-demails.md | indetermine |
| envoi d'emails et courriers | axonaut | envoi d'emails et courriers (fiche client, pièces jointes) | axonaut:centralisez-gestion-emails-courriers/envoyer-des-mails-depuis-axonaut.md | indetermine |
| envoi d'un document | vertuoza | envoi d'un document (devis, facture) par e-mail | vertuoza:documents/envoi-d-un-document-par-mail.md | indetermine |
| envoi d'une facture électronique via peppol | vertuoza | envoi d'une facture électronique via PEPPOL | vertuoza:faq-foires-aux-questions/comment-envoyer-une-facture-electronique-depuis-le-logiciel.md | facturation |
| envoi d'une note de crédit via lien consultable en ligne | vertuoza | envoi d'une note de crédit via lien consultable en ligne | vertuoza:finance/envoi-de-la-note-de-credit-via-un-lien.md | facturation |
| envoi de devis | axonaut | envoi de devis (email, portail client, lecture) | axonaut:gerez-vos-devis/envoyer-mes-devis-depuis-axonaut.md | devis |
| envoi de documents | openfire | envoi de documents (devis, commande, facture) par mail et gestion des échecs d'envoi | openfire:knowsystem/envoyer-un-document-par-mail-146.md | indetermine |
| envoi de rappels de paiement pour factures échues | vertuoza | envoi de rappels de paiement pour factures échues | vertuoza:faq-foires-aux-questions/comment-envoyer-des-rappels-de-paiement.md | facturation |
| envoi de sms | openfire | envoi de SMS (marketing, rappel de RDV, à la demande) | openfire:knowsystem/envoyer-un-sms-sur-openfire-238.md | indetermine |
| envoi document redactor par courrier | sellsy | envoi document Redactor par courrier | sellsy:crm-et-prospection/envoyer-mon-document-redactor-par-courrier.md | indetermine |
| envoi documents par courrier postal | sellsy | envoi documents par courrier postal | sellsy:documents-de-vente/envoyer-mes-documents-par-courrier.md | facturation |
| envoi et suivi des emails | inter-fast | envoi et suivi des emails (statuts, pixel invisible, expéditeur) | inter-fast:inter-fast/outils/envoyer-et-suivre-l-envoi-et-le-statut-de-vos-emails-historique-et-actions.md | indetermine |
| erreur csp | sellsy | erreur CSP (widget, dépannage technique) | sellsy:integrations-et-api/resoudre-une-erreur-de-content-security-policy.md | indetermine |
| erreurs api | sellsy | erreurs API (codes, dépannage) | sellsy:integrations-et-api/les-erreurs-api.md | indetermine |
| erreurs fréquentes de la facturation électronique peppol | vertuoza | erreurs fréquentes de la facturation électronique PEPPOL (checklist) | vertuoza:faq-foires-aux-questions/quelles-erreurs-frequentes-peuvent-survenir-avec-peppol.md | facturation |
| essai gratuit progbat | progbat | essai gratuit ProGBat (inscription, compte de test réel, factures de test) | progbat:pour-bien-demarrer/tester-progbat.md | indetermine |
| exception tarifaire | sellsy | exception tarifaire (client) | sellsy:catalogue-produits-et-services/utiliser-les-exceptions-tarifaires.md | indetermine |
| exclusion des lignes à montant nul dans une facture groupée d'intervention | vertuoza | exclusion des lignes à montant nul dans une facture groupée d'intervention | vertuoza:faq-foires-aux-questions/pourquoi-toutes-les-lignes-ne-sont-elles-pas-reprises-dans-une-facture-groupee-d-intervention.md | facturation |
| exclusion des lignes à quantité | vertuoza | exclusion des lignes à quantité/prix nul dans une facture groupée | vertuoza:faq-foires-aux-questions/pourquoi-certaines-lignes-ne-sont-elles-pas-reprises-dans-la-facture-groupee.md | facturation |
| exclusion poste complémentaire | obat | exclusion poste complémentaire / retenue de garantie | obat:`comment-exclure-les-postes-complementaires-des-retenues-garanties.md` | indetermine |
| exercice fiscal | openfire | exercice fiscal (clôture, verrouillage) | openfire:knowsystem/cloturer-un-exercice-fiscal-124.md | indetermine |
| expert-comptable | sellsy | expert-comptable (connecteurs, réforme facturation électronique) | sellsy:facturation-electronique/la-reforme-sellsy-et-mon-expert-comptable.md | indetermine |
| explication du protocole smtp et des intégrations email disponibles | vertuoza | explication du protocole SMTP et des intégrations email disponibles (avant/après la mise à jour) | vertuoza:parametres/smtp-qu-est-ce-que-c-est.md | indetermine |
| export | extrabat | export (articles, factures/règlements — agrégat) | extrabat:tag/export-2.md | indetermine |
| export affaires | extrabat | export affaires (par utilisateur) | extrabat:exporter-affaires-utilisateur.md | indetermine |
| export ca | extrabat | export CA (origine de contact) | extrabat:exporter-chiffre-daffaires-origine-de-contact.md | indetermine |
| export commandes | extrabat | export commandes | extrabat:exporter-les-commandes.md | achat |
| export complet des données | inter-fast | export complet des données (procédure sécurisée, structure CSV) | inter-fast:inter-fast/application-web/exporter-toutes-mes-donnees.md | indetermine |
| export comptable factures | inter-fast | export comptable factures (paramétrage journal des ventes, export) | inter-fast:inter-fast/finances/exporter-mes-factures-client.md | facturation |
| export comptable factures fournisseurs | inter-fast | export comptable factures fournisseurs (paramétrage journal des achats, export) | inter-fast:inter-fast/finances/exporter-ses-factures-fournisseur.md | achat |
| export d'inventaire | axonaut | export d'inventaire (Excel, CMUP) | axonaut:gerez-stock-temps-reel/comment-exporter-un-inventaire-des-stocks.md | indetermine |
| export d'un document en excel | vertuoza | export d'un document en Excel | vertuoza:documents/export-excel.md | indetermine |
| export d'un document en pdf | vertuoza | export d'un document en PDF | vertuoza:documents/export-pdf.md | indetermine |
| export de factures | costructor | export de factures (CSV/XLSX/FEC) | costructor:imports-exports/comment-exporter-mes-factures-de-ventes-1872kji.md | facturation |
| export des achats | obat | export des achats | obat:`export-des-achats-sur-obat.md` | achat |
| export des contacts | vertuoza | export des contacts/entreprises en fichier Excel | vertuoza:contacts/exporter-des-contacts.md | indetermine |
| export des documents comptables pour le comptable | openfire | export des documents comptables pour le comptable (factures, FEC, écritures) | openfire:knowsystem/quels-documents-fournir-a-votre-comptable-212.md | facturation |
| export des interventions | inter-fast | export des interventions (CSV, PDF) | inter-fast:inter-fast/operations/exporter-mes-interventions.md | chantier-intervention |
| export des paiements | inter-fast | export des paiements (simple, comptable / journal de banque) | inter-fast:inter-fast/finances/exporter-ses-paiements.md | facturation |
| export des stocks csv avec qr codes | inter-fast | export des stocks CSV avec QR codes (inventaire, import masse) | inter-fast:inter-fast/outils/exporter-ses-stocks-au-format-csv-avec-qr-codes-associes.md | indetermine |
| export du fichier clients | inter-fast | export du fichier clients (CSV, campagnes email externes) | inter-fast:inter-fast/outils/exporter-mon-fichier-clients.md | indetermine |
| export du planning | vertuoza | export du planning (global ou par chantier) au format PDF | vertuoza:planning/exporter-le-planning-en-pdf.md | chantier-intervention |
| export excel vide si seulement des ouvrages composés | vertuoza | export Excel vide si seulement des ouvrages composés (limite export ouvrages simples) | vertuoza:faq-foires-aux-questions/pourquoi-mon-export-excel-d-ouvrages-est-il-vide.md | devis |
| export factures | extrabat | export factures/règlements (Excel) | extrabat:je-veux-exporter-sous-excell-mes-factures-et-reglements.md | facturation |
| export groupé de factures | vertuoza | export groupé de factures (PDF/UBL) sur une période | vertuoza:finance/export-des-factures.md | facturation |
| export lignes devis | obat | export lignes devis/factures (CSV/XLSX) | obat:`comment-exporter-les-lignes-de-vos-devis/factures.md` | indetermine |
| export personnalisé | axonaut | export personnalisé (factures/devis/dépenses, champs CSV) | axonaut:configurer-votre-compte/personnaliser-ses-exports-de-factures-depenses-et-devis.md | indetermine |
| export sepa | sellsy | export SEPA (factures fournisseur) | sellsy:module-achats/export-sepa-des-factures-fournisseur.md | indetermine |
| export services | extrabat | export services (contrats) | extrabat:exports-des-services.md | chantier-intervention |
| export suivi du temps | obat | export suivi du temps (personnel) | obat:`comment-exporter-votre-suivi-du-temps.md` | indetermine |
| export écritures comptables | extrabat | export écritures comptables | extrabat:exporter-ecritures-de-gestion-commerciale-logiciel-de-comptabilite.md | facturation |
| exports | extrabat | exports (catégorie, index) | extrabat:export.md | indetermine |
| exports comptables | axonaut | exports comptables (ventes/achats/paiements/lignes bancaires, personnalisation) | axonaut:gerez-votre-comptabilite/realiser-ses-exports-comptables.md | indetermine |
| extension chrome « l'assistant vertuoza » | vertuoza | extension Chrome « L'assistant Vertuoza » (page sans contenu exploitable) | vertuoza:bibliotheque-de-prix/extension-chrome-l-assistant-vertuoza.md | indetermine |
| extraction du fichier des écritures comptables | openfire | extraction du fichier des écritures comptables (FEC) et verrouillage des périodes | openfire:knowsystem/rapport-comptable-fec-213.md | facturation |
| extraction du rapport tva sur encaissement | openfire | extraction du rapport TVA sur encaissement | openfire:knowsystem/extraire-la-tva-sur-encaissement-214.md | facturation |
| fabrication | axonaut | fabrication (produit fini, décrémentation matières premières) | axonaut:gerez-stock-temps-reel/fabrications-comment-ca-marche.md | indetermine |
| facturation b2b | sellsy | facturation B2B (e-invoicing) | sellsy:facturation-electronique/l-emission-de-factures-pour-les-professionnels-b2b.md | facturation |
| facturation b2c | sellsy | facturation B2C (e-reporting) | sellsy:facturation-electronique/l-emission-de-factures-pour-les-particuliers-b2c.md | facturation |
| facturation b2g | sellsy | facturation B2G (Chorus Pro) | sellsy:facturation-electronique/l-emission-des-factures-pour-le-secteur-public-b2g.md | facturation |
| facturation d'intervention | openfire | facturation d'intervention (sans devis préalable) | openfire:utiliser-openfire/facturer-votre-intervention-obsolete.md | facturation |
| facturation d'une intervention depuis l'app mobile par l'ouvrier | vertuoza | facturation d'une intervention depuis l'app mobile par l'ouvrier | vertuoza:application-mobile/facturation-d-une-intervention-par-l-ouvrier-sur-l-app-mobile.md | facturation |
| facturation de temps | axonaut | facturation de temps (type de tâche associé à un produit) | axonaut:gerez-vos-factures/comment-facturer-du-temps-dans-axonaut.md | facturation |
| facturation des interventions | openfire | facturation des interventions (depuis DI, RDV, ou contrats) | openfire:knowsystem/facturer-mes-interventions-91.md | facturation |
| facturation par étapes | inter-fast | facturation par étapes (acompte, situation, solde) | inter-fast:inter-fast/finances/creer-une-facture-d-acompte-de-situation-de-solde.md | facturation |
| facturation prorata | inter-fast | facturation prorata (erreur d'ajout d'utilisateur, conversion en crédit) | inter-fast:inter-fast/equipe/resoudre-un-ajout-d-utilisateur-par-erreur.md | facturation |
| facturation séparée d'un avenant sans nouveau chantier | vertuoza | facturation séparée d'un avenant sans nouveau chantier | vertuoza:faq-foires-aux-questions/comment-facturer-un-avenant-separement-sans-creer-un-nouveau-chantier.md | chantier-intervention |
| facture d'abonnement sellsy | sellsy | facture d'abonnement Sellsy | sellsy:configuration-du-compte/les-factures-de-mon-abonnement-sellsy.md | facturation |
| facture d'achat liée à facture de vente | sellsy | facture d'achat liée à facture de vente (marge) | sellsy:module-achats/lier-une-facture-d-achat-et-une-facture-de-vente.md | achat |
| facture d'acompte libre | obat | facture d'acompte libre (montant personnalisé) | obat:`la-facture-dacompte-libre.md` | facturation |
| facture d'avoir | costructor | facture d'avoir (partiel/total/libre, correction ou annulation) | costructor:ventes/comment-creer-une-facture-davoir-vwjxpf.md | facturation |
| facture de débours | obat | facture de débours | obat:`comment-faire-une-facture-de-d-c3-a9bours-sur-obat.md` | facturation |
| facture finale | obat | facture finale | obat:`comment-cr-c3-a9er-et-modifier-une-facture-finale.md` | facturation |
| facture fournisseur | progbat | facture fournisseur (saisie : PDF/image, OCR/océrisation, papier) | progbat:le-menu-principal/depenses/factures-dachat/saisie-des-factures-fournisseurs.md | achat |
| facture fournisseur électronique | openfire | facture fournisseur électronique (réception via Plateforme Agréée) | openfire:utiliser-openfire/recevoir-et-gerer-ses-factures-fournisseurs-via-la-plateforme-agreee.md | facturation |
| facture partielle | sellsy | facture partielle (facturation progressive) | sellsy:documents-de-vente/utiliser-les-factures-partielles.md | facturation |
| facture récurrente | axonaut | facture récurrente / abonnement (prévisionnel, délai de sécurité) | axonaut:gerez-vos-factures/comment-faire-une-facture-recurrente-un-abonnement-sur-axonaut.md | facturation |
| facture simple | inter-fast | facture simple (création sans devis) | inter-fast:inter-fast/finances/creer-une-facture-simple.md | facturation |
| facture validée | openfire | facture validée (modification via avoir) | openfire:knowsystem/comment-modifier-une-facture-validee-210.md | facturation |
| facture électronique | openfire | facture électronique (envoi via Plateforme Agréée) | openfire:utiliser-openfire/envoyer-ses-factures-clients-via-la-plateforme-agreee.md | facturation |
| factures d'abonnement obat | obat | factures d'abonnement Obat | obat:`comment-acc-c3-a9der-c3-a0-vos-factures-d-abonnement-obat.md` | indetermine |
| famille | progbat | famille (organisation de la bibliothèque : famille métier / famille ouvrage-élément) | progbat:le-menu-principal/bibliotheque/familles.md | indetermine |
| familles | obat | familles/sous-familles bibliothèque | obat:`comment-g-c3-a9rer-les-familles-de-votre-biblioth-c3-a8que-personnalis-c3-a9e.md` | indetermine |
| faq | openfire | FAQ (sommaire des questions, sans réponses) | openfire:faq.md | indetermine |
| faq dépannage | progbat | FAQ dépannage (faux bugs courants : filtres actifs, multi-utilisateur, numérotation provisoire, chiffre d'affaires apparent) | progbat:presentation-generale/la-panicroom.md | indetermine |
| fec | extrabat | FEC (Fichier des Écritures Comptables, conformité) | extrabat:logiciel-extrabat-comptabilite-comptatible-fec.md | facturation |
| feuille de temps | inter-fast | feuille de temps (déclaration heures et astreintes, app mobile) | inter-fast:inter-fast/application-mobile/remplir-ses-feuilles-de-temps-app-mobile.md | chantier-intervention |
| feuilles de temps | inter-fast | feuilles de temps (activation, validation, export, mode détaillé — app web) | inter-fast:inter-fast/equipe/utiliser-les-feuilles-de-temps-app-web.md | chantier-intervention |
| fiche annuaire | obat | fiche annuaire / vitrine en ligne | obat:`cr-c3-a9e-ta-vitrine-en-ligne-avec-lannuaire-obat.md` | indetermine |
| fiche chantier | progbat | fiche chantier (analyse, pilotage, simulation d'avancement) | progbat:le-menu-principal/chantiers-personnel/chantiers/gestion-de-chantier-analyse-et-pilotage.md | chantier-intervention |
| fiche d'intervention | inter-fast | fiche d'intervention (app mobile, sections et actions) | inter-fast:inter-fast/application-mobile/comprendre-la-fiche-d-intervention-app-mobile.md | chantier-intervention |
| fiche d'intervention app web | inter-fast | fiche d'intervention app web (actions, onglets, rapport, suppression) | inter-fast:inter-fast/operations/comprendre-la-fiche-d-intervention-app-web.md | chantier-intervention |
| fiche d'un chantier | inter-fast | fiche d'un chantier (informations générales, onglets vente/dépenses/interventions) | inter-fast:inter-fast/operations/comprendre-la-fiche-d-un-chantier.md | chantier-intervention |
| fiche de maintenance | inter-fast | fiche de maintenance (visites, interventions, équipements, devis/factures) | inter-fast:inter-fast/operations/comprendre-la-fiche-d-une-maintenance.md | chantier-intervention |
| fiche opportunité | sellsy | fiche opportunité (présentation complète) | sellsy:crm-et-prospection/presentation-de-la-fiche-opportunite.md | indetermine |
| fiche personnel | progbat | fiche personnel/salarié (état civil, contrat, rémunération, accès mobile compagnons) | progbat:le-menu-principal/chantiers-personnel/personnel/la-fiche-personnel-salarie.md | indetermine |
| fiche sav | extrabat | fiche SAV (retour fournisseur) | extrabat:nouvelle-fonctionnalites-sur-les-fiches-sav.md | chantier-intervention |
| fiche utilisateur | inter-fast | fiche utilisateur (droits, coûts, documents, historique) | inter-fast:inter-fast/equipe/comprendre-et-parametrer-la-fiche-utilisateur.md | indetermine |
| fichiers | sellsy | fichiers (stockage contextuel sur fiches) | sellsy:gestion-des-donnees/stocker-des-fichiers-sur-un-objet-client-document-opportunite.md | indetermine |
| fichiers export | sellsy | fichiers export (format texte, marketing) | sellsy:module-marketing/marketing-exploiter-les-fichiers-au-format-texte-txt.md | indetermine |
| fil d'activité du chantier | inter-fast | fil d'activité du chantier (communication temps réel) | inter-fast:inter-fast/operations/consulter-et-utiliser-le-fil-d-activite-du-chantier.md | chantier-intervention |
| filtre de dates | extrabat | filtre de dates (pièces commerciales, évolution infra) | extrabat:evolutions-plage-de-dates-au-niveau-des-pieces-commerciales.md | indetermine |
| filtre favori | sellsy | filtre favori (listes) | sellsy:gestion-des-donnees/utiliser-les-filtres-favoris.md | indetermine |
| filtre sav | extrabat | filtre SAV/contrats (code postal) | extrabat:filtrer-sav-contrats-de-services-code-postal.md | chantier-intervention |
| filtres favoris | sellsy | filtres favoris (répertoire, mobile) | sellsy:app-mobile-sellsy-crm/app-sellsy-crm-utiliser-des-filtres-favoris.md | indetermine |
| fonctionnalité optionnelle d'analytique comptable liée à la synchronisation | vertuoza | fonctionnalité optionnelle d'analytique comptable liée à la synchronisation | vertuoza:faq-foires-aux-questions/qu-est-ce-que-l-analytique-dans-la-synchronisation-comptable.md | indetermine |
| fonctionnalités collaboratives | sellsy | fonctionnalités collaboratives (mention, épinglage, Slack) | sellsy:conseils-d-utilisation/decouvrez-toutes-nos-fonctionnalites-collaboratives.md | indetermine |
| fonctionnalités ia | axonaut | fonctionnalités IA (résumé, analyse devis/factures, description produit, segmentation) | axonaut:configurer-votre-compte/axonaut-et-ia.md | indetermine |
| fonctionnement du tri des colonnes dans les tableaux | vertuoza | fonctionnement du tri des colonnes dans les tableaux | vertuoza:faq-foires-aux-questions/comment-fonctionne-le-tri-des-colonnes.md | indetermine |
| fonctionnement détaillé de l'envoi de factures via le réseau peppol | vertuoza | fonctionnement détaillé de l'envoi de factures via le réseau PEPPOL | vertuoza:faq-foires-aux-questions/comment-fonctionne-concretement-l-envoi-via-peppol.md | facturation |
| fonctionnement et suivi des mouvements de stock | openfire | fonctionnement et suivi des mouvements de stock (double entrée) | openfire:knowsystem/mouvement-de-stocks-248.md | achat |
| fonctions collaboratives | sellsy | fonctions collaboratives (travail d'équipe) | sellsy:crm-et-prospection/utiliser-les-fonctions-collaboratives.md | indetermine |
| fond de page | sellsy | fond de page (personnalisation document) | sellsy:documents-de-vente/creer-un-fond-de-page.md | facturation |
| forfait | costructor | forfait / abonnement | costructor:abonnement/comment-modifier-son-abonnement-3z9g1l.md | indetermine |
| format du numéro d'identification peppol en belgique | vertuoza | format du numéro d'identification PEPPOL en Belgique | vertuoza:faq-foires-aux-questions/comment-saisir-le-numero-d-identification-peppol-en-belgique.md | indetermine |
| format du numéro peppol et vérification d'enregistrement fournisseur | vertuoza | format du numéro PEPPOL et vérification d'enregistrement fournisseur | vertuoza:faq-foires-aux-questions/que-faire-si-le-fournisseur-n-est-pas-encore-enregistre-sur-peppol.md | achat |
| formation complète application web | inter-fast | formation complète application web (index de tutoriels) | inter-fast:inter-fast/debuter-avec-interfast/formation-complete-a-l-application-web-d-interfast.md | indetermine |
| formats de données | sellsy | formats de données (téléphone, date, devise) | sellsy:configuration-du-compte/parametrer-les-formats-de-donnees.md | indetermine |
| formulaire | axonaut | formulaire (création, partage, statistiques, réponses) | axonaut:optimisez-gestion-commerciale/formulaire-axonaut.md | indetermine |
| formulaire de demande de devis | obat | formulaire de demande de devis (fiche annuaire) | obat:`formulaire-de-demande-de-devis-int-c3-a9gre-a-votre-fiche-annuaire-obat.md` | demande |
| formulaire inscription campagnes marketing | sellsy | formulaire inscription campagnes marketing (widget) | sellsy:integrations-et-api/personnaliser-le-formulaire-d-inscription-aux-campagnes-marketing.md | indetermine |
| formulaires de demande | inter-fast | formulaires de demande (public, personnalisés, intégration) | inter-fast:inter-fast/operations/utiliser-les-formulaires-de-demande.md | demande |
| formulaires et zones de saisie | progbat | formulaires et zones de saisie (textes enregistrés, champs date, champs calculés, texte enrichi) | progbat:presentation-generale/les-formulaires-et-zones-de-saisie.md | indetermine |
| formules de calcul des graphiques statistiques | obat | formules de calcul des graphiques statistiques | obat:`comment-sont-calcul-c3-a9s-les-graphiques-statistiques-dobat.md` | indetermine |
| frais annexes | axonaut | frais annexes (Compte Pro, retraits, virements internationaux) | axonaut:compte-pro-cartes/quels-sont-les-frais-annexes-du-compte-pro-axonaut.md | indetermine |
| frais masqués | inter-fast | frais masqués (application, cumul, impact marge) | inter-fast:inter-fast/finances/utiliser-les-frais-masques.md | devis |
| freelances | sellsy | freelances / auto-entrepreneurs (réforme facturation électronique) | sellsy:facturation-electronique/freelances-auto-entrepreneurs.md | indetermine |
| fusion des pistes et opportunités en doublon | openfire | fusion des pistes et opportunités en doublon | openfire:knowsystem/fusionner-des-pistes-opportunites-159.md | demande |
| gestion avancée des fiches contact | openfire | gestion avancée des fiches contact (adresses, notes, comptabilité, marketing, géolocalisation) | openfire:knowsystem/gestion-avancee-des-contacts-109.md | indetermine |
| gestion d'index de révision de prix pour factures récurrentes | vertuoza | gestion d'index de révision de prix pour factures récurrentes | vertuoza:finance/table-d-index.md | facturation |
| gestion de l'intervention depuis l'app mobile | vertuoza | gestion de l'intervention depuis l'app mobile (récapitulatif, installation, commandes) | vertuoza:application-mobile/ouvrier-gestion-de-l-intervention.md | chantier-intervention |
| gestion de la liste des pays | vertuoza | gestion de la liste des pays | vertuoza:parametres/les-pays.md | indetermine |
| gestion de la liste des véhicules utilisables en planification | vertuoza | gestion de la liste des véhicules utilisables en planification | vertuoza:parametres/vehicules.md | chantier-intervention |
| gestion de la traçabilité des articles | openfire | gestion de la traçabilité des articles (numéros de série, lots) | openfire:knowsystem/tracabilite-251.md | achat |
| gestion de plusieurs adresses de livraison | openfire | gestion de plusieurs adresses de livraison/facturation par contact | openfire:knowsystem/livrer-et-facturer-a-plusieurs-adresses-219.md | indetermine |
| gestion de réseau de franchises | axonaut | gestion de réseau de franchises (tableau de bord, redevances) | axonaut:axonaut-et-votre-secteur-activite/franchises-comment-gerer-votre-reseau-avec-axonaut.md | indetermine |
| gestion des avoirs fournisseurs | obat | gestion des avoirs fournisseurs | obat:`gestion-des-avoirs-fournisseurs.md` | achat |
| gestion des civilités et de leur affichage sur devis | openfire | gestion des civilités et de leur affichage sur devis/factures | openfire:knowsystem/parametrage-des-civilites-113.md | indetermine |
| gestion des compétences des responsables d'intervention | vertuoza | gestion des compétences des responsables d'intervention (aide à l'assignation) | vertuoza:gestion-des-interventions/competences.md | chantier-intervention |
| gestion des droits d'accès | progbat | gestion des droits d'accès (rôles personnalisés, permissions détaillées, documents privés) | progbat:pour-bien-demarrer/parametrage/utilisateurs/gestion-des-droits-dacces.md | indetermine |
| gestion des droits utilisateurs pour les interventions et le paiement | openfire | gestion des droits utilisateurs pour les interventions et le paiement | openfire:knowsystem/gerer-les-droits-utilisateurs-63.md | indetermine |
| gestion des déchets | costructor | gestion des déchets (obligation légale devis BTP, code de l'environnement) | costructor:ventes/gestion-des-dechets-3t2w0p.md | devis |
| gestion des emplacements de stock | vertuoza | gestion des emplacements de stock (cartographie par niveaux) | vertuoza:stock/emplacement-de-stock.md | indetermine |
| gestion des entrepôts et emplacements de stockage | openfire | gestion des entrepôts et emplacements de stockage | openfire:knowsystem/entrepots-et-emplacements-227.md | achat |
| gestion des fiches techniques | vertuoza | gestion des fiches techniques (groupes, import, liaison chantier) | vertuoza:fiches-techniques/fiches-techniques.md | indetermine |
| gestion des fluides frigorigènes | openfire | gestion des fluides frigorigènes (Cerfa 15497, Trackdéchets) | openfire:configurer-openfire/configurer-la-gestion-des-fluides.md | chantier-intervention |
| gestion des motifs et du suivi des opportunités perdues | openfire | gestion des motifs et du suivi des opportunités perdues | openfire:knowsystem/gerer-les-opportunites-perdues-121.md | demande |
| gestion des paiements partiels et leur non-affichage sur les totaux de facture | vertuoza | gestion des paiements partiels et leur non-affichage sur les totaux de facture | vertuoza:faq-foires-aux-questions/comment-gerer-les-paiements-partiels-dans-vertuoza-et-pourquoi-ne-sont-ils-pas-visibles-sur-les-totaux-des-factures.md | facturation |
| gestion des permissions et rôles utilisateurs | vertuoza | gestion des permissions et rôles utilisateurs (accès aux menus) | vertuoza:parametres/gestion-des-permissions.md | indetermine |
| gestion des primes énergétiques | openfire | gestion des primes énergétiques (CEE, Rénov) dans les devis et factures | openfire:knowsystem/gerer-les-primes-energetiques-148.md | devis |
| gestion des remises et marges sur devis | openfire | gestion des remises et marges sur devis (manuelle, outil de gestion de prix, listes de prix) | openfire:knowsystem/gerer-la-marge-et-les-remises-125.md | devis |
| gestion des ressources | obat | gestion des ressources (personnel/matériel) | obat:`centralisez-toutes-vos-ressources-sur-obat-grace-a-un-nouveau-listing-simplifie.md` | indetermine |
| gestion des retenues de garantie sur devis et suivi de leur libération | vertuoza | gestion des retenues de garantie sur devis et suivi de leur libération (rappels) | vertuoza:faq-foires-aux-questions/comment-gerer-les-retenues-dans-les-devis-et-suivre-leur-liberation.md | devis |
| gestion des retours fournisseurs et reliquats de réception | openfire | gestion des retours fournisseurs et reliquats de réception | openfire:knowsystem/gerer-les-retours-et-les-reliquats-179.md | achat |
| gestion des tâches | inter-fast | gestion des tâches (listes, assignation, usage mobile) | inter-fast:inter-fast/operations/gerer-les-taches-app-web.md | indetermine |
| gestion des tâches administratives | vertuoza | gestion des tâches administratives (champs requis, module tâches admin) | vertuoza:taches/taches.md | indetermine |
| gestion des unités utilisées dans les formulaires | vertuoza | gestion des unités utilisées dans les formulaires (devis, factures, commandes) | vertuoza:parametres/les-unites.md | indetermine |
| gestion des utilisateurs | inter-fast | gestion des utilisateurs (ajout, archivage, changement de statut) | inter-fast:inter-fast/equipe/gerer-mon-equipe-et-mes-utilisateurs.md | indetermine |
| gestion des écritures et pièces comptables | openfire | gestion des écritures et pièces comptables (automatisation, saisie, import) | openfire:knowsystem/ecritures-comptables-et-pieces-comptables-275.md | facturation |
| gestion des étiquettes | openfire | gestion des étiquettes (contact, intervention, opportunité) | openfire:knowsystem/gerer-les-etiquettes-112.md | indetermine |
| gestion du calendrier | obat | gestion du calendrier (types d'événements) | obat:`gerer-votre-calendrier.md` | chantier-intervention |
| gestion du consentement rgpd | extrabat | gestion du consentement RGPD (campagnes emailing) | extrabat:gestion-consentement.md | indetermine |
| gestion du planning des absences des ouvriers et indépendants | vertuoza | gestion du planning des absences des ouvriers et indépendants | vertuoza:rh/planning-des-absences.md | indetermine |
| gestion du reste à payer lors de l'application d'un crédit sur facture | vertuoza | gestion du reste à payer lors de l'application d'un crédit sur facture | vertuoza:faq-foires-aux-questions/comment-le-reste-a-payer-est-il-gere-lorsqu-un-credit-est-applique.md | facturation |
| gestion et ajustement des marges sur devis | vertuoza | gestion et ajustement des marges sur devis (poste libre, composant, ouvrage, majoration globale) | vertuoza:devis/marges.md | devis |
| gestionnaire de fichiers | sellsy | gestionnaire de fichiers (introduction) | sellsy:gestion-des-donnees/introduction-presentation-du-gestionnaire-de-fichiers-sellsy.md | indetermine |
| gocardless | sellsy | GoCardless (FAQ, limites, dépannage) | sellsy:paiements/questions-frequentes-sur-gocardless.md | indetermine |
| grades et badges | openfire | grades et badges (plateforme documentaire, hors produit) | openfire:profile/ranks-badges.md | indetermine |
| groupe de champs personnalisés | sellsy | groupe de champs personnalisés | sellsy:gestion-des-donnees/creer-un-groupe-de-champs-personnalises.md | indetermine |
| groupe de collaborateurs | sellsy | groupe de collaborateurs | sellsy:configuration-du-compte/utiliser-les-groupes-de-collaborateurs.md | indetermine |
| guide complet d'installation de la synchronisation comptable | vertuoza | guide complet d'installation de la synchronisation comptable (connexion, TVA, comptes généraux, journaux, plan analytique, contacts) | vertuoza:parametres/guide-d-installation-de-la-synchronisation-comptable.md | facturation |
| guide de démarrage pour initialiser le stock | vertuoza | guide de démarrage pour initialiser le stock (préparation des fournitures, import, premier inventaire) | vertuoza:stock/remplir-son-stock-pour-la-premiere-fois.md | indetermine |
| guide de la gestion des stocks | inter-fast | guide de la gestion des stocks (mouvements, liaison bibliothèque, cas d'usage) | inter-fast:inter-fast/outils/guide-complet-la-gestion-des-stocks-dans-interfast.md | indetermine |
| générateur de cgv | obat | générateur de CGV (outil externe) | obat:`comment-utiliser-le-generateur-de-cgv-obat.md` | indetermine |
| générateur de logo | obat | générateur de logo (IA) | obat:`cr-c3-a9ez-votre-logo-professionnel-en-quelques-clics-avec-obat.md` | indetermine |
| génération automatique de pistes et opportunités | openfire | génération automatique de pistes et opportunités (email, formulaire web) | openfire:knowsystem/generer-automatiquement-des-opportunites-166.md | demande |
| génération d'une demande de prix et transformation en commande d'achat | openfire | génération d'une demande de prix et transformation en commande d'achat | openfire:knowsystem/generer-une-commande-d-achat-157.md | achat |
| génération de devis | openfire | génération de devis (modèles d'intervention, rapports d'équipement) | openfire:configurer-openfire/configurer-la-generation-des-devis-dans-vos-modeles-d-intervention-et-rapports-d-equipement.md | devis |
| génération de factures depuis un contrat | openfire | génération de factures depuis un contrat (assistant de facturation) | openfire:knowsystem/facturer-un-contrat-309.md | facturation |
| génération des factures fournisseurs et paiement fournisseur | openfire | génération des factures fournisseurs et paiement fournisseur | openfire:knowsystem/generer-mes-factures-fournisseurs-173.md | achat |
| génération des rapports de gestion | openfire | génération des rapports de gestion (encours, échéancier fournisseurs, TVA sur encaissement) | openfire:knowsystem/rapports-de-gestion-tva-sur-encaissement-56.md | facturation |
| génération et structure du bon de livraison client | openfire | génération et structure du bon de livraison client | openfire:knowsystem/generation-du-bon-de-livraison-59.md | achat |
| géolocalisation des contacts | openfire | géolocalisation des contacts (manuelle ou automatique) | openfire:knowsystem/geolocalisation-180.md | indetermine |
| géolocalisation des salariés | inter-fast | géolocalisation des salariés (suivi des déplacements, cadre légal) | inter-fast:inter-fast/application-mobile/autoriser-le-suivi-des-deplacements-app-mobile.md | chantier-intervention |
| heures de main d'œuvre | openfire | heures de main d'œuvre (produits, devis, interventions) | openfire:utiliser-openfire/suivre-mes-heures-de-main-d-oeuvre-dans-mes-produits-bons-de-commande-et-interventions.md | indetermine |
| heures saisies | progbat | heures saisies (consultation, export, filtres) | progbat:le-menu-principal/chantiers-personnel/saisie-des-heures/consulter-et-exporter-les-heures.md | chantier-intervention |
| historique | costructor | historique / révision de devis (restauration) | costructor:ventes/comment-recuperer-une-version-anterieure-dun-devis-eg0od3.md | devis |
| historique d'interventions client | openfire | historique d'interventions client | openfire:guides-videos/consulter-l-historique-des-interventions-d-un-client-sur-mobile.md | chantier-intervention |
| historique des interventions | inter-fast | historique des interventions (accès selon rôle utilisateur) | inter-fast:inter-fast/application-mobile/suivre-l-historique-des-interventions.md | chantier-intervention |
| historique des ventes | extrabat | historique des ventes (client) | extrabat:historique-ventes-gestion-commerciale.md | indetermine |
| historique et filtrage des mouvements de stock | vertuoza | historique et filtrage des mouvements de stock (entrées, sorties, transferts, ajustements) | vertuoza:stock/mouvement-des-stocks.md | indetermine |
| horaires spécifiques | progbat | horaires spécifiques (personnel) | progbat:le-menu-principal/chantiers-personnel/personnel/horaires-specifiques.md | indetermine |
| hébergement | sellsy | hébergement / chiffrement des données | sellsy:conseils-d-utilisation/ou-sont-hebergees-vos-donnees-et-comment-elles-sont-chiffrees.md | indetermine |
| iban | extrabat | IBAN (coordonnées bancaires, pièces commerciales) | extrabat:modifier-coordonnees-de-iban-devis-commandes-factures.md | indetermine |
| identifiants api | sellsy | identifiants API (types ID) | sellsy:integrations-et-api/les-differents-types-d-id-sur-l-api-v1.md | indetermine |
| identifiants bancaires | sellsy | identifiants bancaires (modification, synchronisation) | sellsy:suivi-financier/modifier-ses-identifiants-bancaires.md | indetermine |
| identifiants espace client | extrabat | identifiants espace client (envoi email) | extrabat:comment-envoyer-lidentifiant-de-lespace-client-sur-sa-boite-mail.md | indetermine |
| identification et résolution des factures en erreur de synchronisation comptable | vertuoza | identification et résolution des factures en erreur de synchronisation comptable | vertuoza:parametres/comment-identifier-les-factures-en-erreurs.md | facturation |
| image | costructor | image (insertion sur ligne de document) | costructor:ventes/comment-inserer-une-image-dans-un-document-1289smb.md | indetermine |
| impact des avenants | vertuoza | impact des avenants/notes de crédit sur le chiffre d'affaires | vertuoza:faq-foires-aux-questions/comment-les-avenants-impactent-ils-le-chiffre-d-affaires-dans-vertuoza.md | chantier-intervention |
| impact des notes de crédit sur la gestion des stocks | vertuoza | impact des notes de crédit sur la gestion des stocks (absence de lien automatique) | vertuoza:faq-foires-aux-questions/comment-fonctionnent-les-notes-de-credit-et-leur-impact-sur-le-stock-dans-vertuoza.md | facturation |
| import articles | extrabat | import articles (catalogue fournisseur) | extrabat:comment-importer-des-articles-dun-catalogue-fournisseur.md | achat |
| import cgv au format pdf | obat | import CGV au format PDF | obat:`comment-importer-vos-cgv-eu-format-pdf-sur-obat.md` | indetermine |
| import d'articles | inter-fast | import d'articles (préparation fichier, matching, correction erreurs) | inter-fast:inter-fast/outils/importer-des-articles.md | indetermine |
| import d'ouvrages | progbat | import d'ouvrages (fichier Excel/CSV) | progbat:pour-bien-demarrer/demarrer-avec-progbat/importer-une-bibliotheque/importer-mes-ouvrages.md | indetermine |
| import d'un devis depuis un fichier excel externe | vertuoza | import d'un devis depuis un fichier Excel externe (bordereau de prix, appel d'offres) | vertuoza:devis/import-d-un-devis-depuis-un-excel.md | devis |
| import d'une ancienne facture | costructor | import d'une ancienne facture (rétro-saisie) | costructor:imports-exports/comment-importer-une-ancienne-facture-15ddlrf.md | facturation |
| import de bibliothèque | progbat | import de bibliothèque (fournitures, ouvrages, tarif fournisseur) | progbat:pour-bien-demarrer/demarrer-avec-progbat/importer-une-bibliotheque.md | indetermine |
| import de bibliothèque de produits | costructor | import de bibliothèque de produits (fichier CSV) | costructor:imports-exports/comment-importer-des-produits-dans-ma-bibliotheque-vgrbpu.md | indetermine |
| import de clients | inter-fast | import de clients (préparation fichier, mapping, annulation) | inter-fast:inter-fast/outils/importer-des-clients.md | indetermine |
| import de données | axonaut | import de données (contacts/produits/factures, fichier modèle) | axonaut:configurer-votre-compte/importer-ses-contacts.md | indetermine |
| import de facture d'achat | costructor | import de facture d'achat (dépôt fichier + transfert mail) | costructor:imports-exports/comment-importer-une-facture-dachat-1fo750j.md | achat |
| import de factures fournisseurs par ia | vertuoza | import de factures fournisseurs par IA (email, web, mobile, reconnaissance de champs) | vertuoza:finance/utiliser-l-ia-pour-importer-ses-factures-fournisseurs-beta.md | achat |
| import de fournitures | progbat | import de fournitures (fichier ou tarif fournisseur) | progbat:pour-bien-demarrer/demarrer-avec-progbat/importer-une-bibliotheque/importer-mes-fournitures.md | indetermine |
| import de lignes inter-documents | costructor | import de lignes inter-documents (devis/facture/BC/BI) | costructor:ventes/comment-importer-des-lignes-dun-autre-document-1ph07xo.md | indetermine |
| import de tarif fournisseur | progbat | import de tarif fournisseur (fichier fourniture ou tarif fournisseur — contenu quasi identique à #149, cf. limites) | progbat:pour-bien-demarrer/demarrer-avec-progbat/importer-une-bibliotheque/importer-un-tarif-fournisseur.md | indetermine |
| import des conditions générales de vente | vertuoza | import des conditions générales de vente (CGV) en pièce jointe automatique aux devis/factures | vertuoza:parametres/conditions-generales-de-ventes-cgv.md | devis |
| import et mise à jour en masse d'articles et de kits via fichier excel | openfire | import et mise à jour en masse d'articles et de kits via fichier Excel | openfire:knowsystem/importer-des-articles-ou-des-kits-160.md | devis |
| import excel | obat | import Excel/DPGF (devis) | obat:`import-externe-excel/dpgf.md` | devis |
| import fichier client | obat | import fichier client/bibliothèque (service) | obat:`importer-votre-fichier-client.md` | indetermine |
| import ia de devis | inter-fast | import IA de devis/factures (ancien logiciel) | inter-fast:inter-fast/finances/import-des-devis-factures-de-mon-ancien-logiciel-avec-l-ia.md | indetermine |
| import produit | costructor | import produit (extension navigateur, catalogue fournisseur) | costructor:debuter-sur-costructor/comment-importer-plus-de-100-millions-darticles-en-1-clic-div3pc.md | indetermine |
| imports de données | sellsy | imports de données (types disponibles) | sellsy:gestion-des-donnees/les-differents-types-d-imports-de-donnees-sur-sellsy.md | indetermine |
| impossibilité d'intégration directe des paiements bob50 | vertuoza | impossibilité d'intégration directe des paiements BOB50 (alternative Codabox/Ponto) | vertuoza:faq-foires-aux-questions/est-il-possible-d-implementer-les-paiements-des-clients-venant-des-coda-bob-50-dans-vertuoza.md | facturation |
| impossibilité de modifier l'adresse de chantier après édition de facture | vertuoza | impossibilité de modifier l'adresse de chantier après édition de facture (contournement) | vertuoza:faq-foires-aux-questions/puis-je-modifier-l-adresse-d-un-chantier-apres-l-edition-d-une-facture.md | facturation |
| impossibilité de modifier manuellement le statut d'une offre | vertuoza | impossibilité de modifier manuellement le statut d'une offre (contournement) | vertuoza:faq-foires-aux-questions/est-il-possible-d-adapter-manuellement-le-statut-d-une-offre.md | devis |
| impossibilité de récupérer une facture supprimée | vertuoza | impossibilité de récupérer une facture supprimée | vertuoza:faq-foires-aux-questions/comment-recuperer-une-facture-supprimee.md | facturation |
| impression de factures | openfire | impression de factures/devis/commandes en PDF et gestion des acomptes à l'impression | openfire:knowsystem/imprimer-ma-facture-140.md | facturation |
| impression du planning | obat | impression du planning | obat:`imprimer-et-diffuser-votre-planning.md` | chantier-intervention |
| impression du planning d'intervention au format pdf | openfire | impression du planning d'intervention au format PDF | openfire:knowsystem/impression-du-planning-82.md | chantier-intervention |
| impression illisible | extrabat | impression illisible (bug polices Firefox) | extrabat:ma-piece-commerciale-est-illisible-a-limpression-sous-firefox.md | indetermine |
| inclusion d'un acompte déjà perçu via un avenant négatif | vertuoza | inclusion d'un acompte déjà perçu via un avenant négatif | vertuoza:faq-foires-aux-questions/comment-inclure-un-montant-deja-paye-par-le-client-dans-une-facture-d-acompte.md | facturation |
| indemnité kilométrique | axonaut | indemnité kilométrique (barème URSSAF, seuils, rattrapage) | axonaut:creez-depenses-facilement/les-indemnites-kilometriques-axonaut.md | achat |
| informations de profil | sellsy | informations de profil (collaborateur) | sellsy:conseils-d-utilisation/parametrer-les-informations-de-mon-profil.md | indetermine |
| informations générales entreprise | progbat | informations générales entreprise (mentions légales, informations commerciales) | progbat:pour-bien-demarrer/parametrage/parametres-de-lentreprise/informations-generales.md | indetermine |
| insertion de variables dynamiques dans les modèles de documents | vertuoza | insertion de variables dynamiques dans les modèles de documents (société, client, devis, chantier) | vertuoza:parametres/comment-utiliser-les-variables-dans-vos-modeles.md | devis |
| installation, connexion et mise à jour de l'application mobile | openfire | installation, connexion et mise à jour de l'application mobile | openfire:knowsystem/telechargement-et-connexion-93.md | indetermine |
| interface pointage mobile | obat | interface pointage mobile (nouvelle version) | obat:`nouvelle-interface-de-pointage-mobile-plus-rapide-plus-claire-plus-efficace-bientot-disponible.md` | chantier-intervention |
| interlocuteur par défaut | extrabat | interlocuteur par défaut (devis/commande) | extrabat:choisir-de-mettre-non-interlocuteur-devis-commande.md | devis |
| interruption de session liée à une facture ouverte sur le compte | vertuoza | interruption de session liée à une facture ouverte sur le compte | vertuoza:faq-foires-aux-questions/pourquoi-ma-session-a-t-elle-ete-interrompue.md | indetermine |
| intervention planifiée depuis un devis | inter-fast | intervention planifiée depuis un devis (création, liaison) | inter-fast:inter-fast/finances/planifier-une-intervention-a-partir-d-un-devis.md | chantier-intervention |
| interventions | obat | interventions (page de catégorie) | obat:`interventions.md` | chantier-intervention |
| intitulé de document | sellsy | intitulé de document (personnalisation) | sellsy:documents-de-vente/changer-l-intitule-d-un-document.md | facturation |
| intégration | axonaut | intégration / API (Zapier) | axonaut:connectez-axonaut/axonaut-zapier-connectez-vos-meilleurs-logiciels.md | indetermine |
| intégration bancaire qonto | obat | intégration bancaire Qonto | obat:`gagnez-du-temps-gr-c3-a2ce-c3-a0-lint-c3-a9gration-entre-obat-et-qonto.md` | indetermine |
| intégration beltys | extrabat | intégration Beltys (Drive, publication article) | extrabat:interface-extrabat-beltys.md | indetermine |
| intégration brevo | extrabat | intégration Brevo (SMTP, emailing) | extrabat:comment-parametrer-le-smtp-brevo-dans-extrabat.md | indetermine |
| intégration buzzee mail | extrabat | intégration Buzzee Mail (messagerie professionnelle) | extrabat:messagerie-pro-buzzee-mail.md | indetermine |
| intégration catalogues fournisseurs | obat | intégration catalogues fournisseurs (FAQ) | obat:`peut-on-int-c3-a9grer-des-catalogues-fournisseurs.md` | indetermine |
| intégration cebeo | vertuoza | intégration CEBEO (catalogue de fournitures électriques importable dans devis, ouvrages, bibliothèque de prix) | vertuoza:parametres/integration-cebeo.md | devis |
| intégration de l'écoparticipation dans un devis | vertuoza | intégration de l'écoparticipation dans un devis (poste libre ou majoration) | vertuoza:faq-foires-aux-questions/comment-integrer-l-ecoparticipation-dans-un-devis.md | devis |
| intégration des frais généraux dans le calcul de rentabilité d'un devis | vertuoza | intégration des frais généraux dans le calcul de rentabilité d'un devis | vertuoza:faq-foires-aux-questions/pourquoi-est-il-important-de-prendre-en-compte-les-frais-generaux-dans-un-devis.md | devis |
| intégration domotique kléreo | extrabat | intégration domotique Kléreo (piscine) | extrabat:associer-la-domotique-klereo-a-extrabat.md | indetermine |
| intégration gmail | vertuoza | intégration Gmail/Google Workspace pour l'envoi d'emails depuis sa propre adresse | vertuoza:parametres/gmail-envoi-des-emails-avec-ta-propre-adresse.md | indetermine |
| intégration google agenda | openfire | intégration Google Agenda (configuration technique OAuth) | openfire:configurer-openfire/configuration-de-la-synchronisation-google-agenda.md | indetermine |
| intégration logiciel d'analyse de l'eau | extrabat | intégration logiciel d'analyse de l'eau (Ocediciel/Actisoft/Test'o) | extrabat:je-veux-faire-la-liaison-dextrabat-piscines-avec-mon-logiciel-danalyse-de-leau-ocediciel-actisoft-testo.md | chantier-intervention |
| intégration logiciel de comptabilité | extrabat | intégration logiciel de comptabilité (protocole d'export) | extrabat:comment-parametrer-un-nouveau-logiciel-de-comptabilite-dans-extrabat.md | indetermine |
| intégration mailjet | extrabat | intégration Mailjet (clé API, emailing) | extrabat:comment-parametrer-cle-api-mailjet.md | indetermine |
| intégration make | sellsy | intégration Make (tokens API) | sellsy:integrations-et-api/connecter-sellsy-a-make.md | indetermine |
| intégration mcp | inter-fast | intégration MCP (connexion IA externe, clé API, création de devis assistée) | inter-fast:inter-fast/mon-entreprise/connecter-interfast-a-une-ia-via-mcp.md | indetermine |
| intégration outlook | vertuoza | intégration Outlook/Microsoft 365 pour l'envoi d'emails depuis sa propre adresse | vertuoza:parametres/outlook-envoi-des-emails-avec-ta-propre-adresse.md | indetermine |
| intégration pennylane | inter-fast | intégration Pennylane (facturation électronique, comptabilité, synchronisation) | inter-fast:inter-fast/mon-entreprise/connecter-interfast-a-pennylane.md | facturation |
| intégration peppol | inter-fast | intégration Peppol (envoi/réception factures électroniques, Belgique) | inter-fast:inter-fast/mon-entreprise/connecter-interfast-a-peppol.md | facturation |
| intégration ringover | sellsy | intégration Ringover (téléphonie) | sellsy:crm-et-prospection/synchroniser-ringover-avec-sellsy.md | indetermine |
| intégration testo | vertuoza | intégration Testo (import de rapports d'entretien dans les rapports d'intervention mobile) via clé API | vertuoza:parametres/testo.md | chantier-intervention |
| intégration trackdéchets | inter-fast | intégration Trackdéchets (traçabilité déchets dangereux) | inter-fast:inter-fast/mon-entreprise/connecter-trackdechets-a-interfast.md | indetermine |
| intégration zapier | sellsy | intégration Zapier | sellsy:integrations-et-api/connecter-sellsy-a-zapier.md | indetermine |
| intégrations | sellsy | intégrations / connecteurs / API (panorama) | sellsy:integrations-et-api/integrations-connecteurs-et-api.md | indetermine |
| inventaire de stocks | sellsy | inventaire de stocks | sellsy:gestion-des-donnees/effectuer-un-inventaire-de-stocks.md | indetermine |
| inventaire fin d'exercice | extrabat | inventaire fin d'exercice (bonnes pratiques préparatoires) | extrabat:les-bonnes-pratiques-avant-de-faire-son-inventaire-de-fin-dexercice.md | indetermine |
| invitation collaborateurs par téléphone | obat | invitation collaborateurs par téléphone (SMS) | obat:`invitez-vos-collaborateurs-sur-obat-par-numero-de-telephone.md` | indetermine |
| invitation comptable | costructor | invitation comptable (accès externe) | costructor:equipe-collaborateurs/comment-inviter-mon-comptable-1gj4div.md | indetermine |
| invitation utilisateur | obat | invitation utilisateur (multi-user) | obat:`multi-user-comment-inviter-un-utilisateur.md` | indetermine |
| ip dédiée | sellsy | IP dédiée / mutualisée (délivrabilité emailing) | sellsy:module-marketing/marketing-opter-pour-une-ip-dediee-ou-une-ip-mutualisee.md | indetermine |
| jour férié | openfire | jour férié (configuration, planning) | openfire:configurer-openfire/configurer-les-jours-feries.md | chantier-intervention |
| journal comptable | openfire | journal comptable (création, séquences) | openfire:configurer-openfire/configurez-vos-journaux.md | indetermine |
| journal de banque | sellsy | journal de banque (export) | sellsy:suivi-financier/exporter-le-journal-de-banque.md | indetermine |
| journal de caisse | extrabat | journal de caisse (paramétrage, fond de caisse) | extrabat:parametrer-journal-de-caisse-rentrer-fond-de-caisse.md | indetermine |
| journal de facturation | sellsy | journal de facturation (contrôle conformité) | sellsy:documents-de-vente/journal-de-facturation.md | facturation |
| journal de ventes | inter-fast | journal de ventes (export comptable, justificatifs) | inter-fast:inter-fast/mon-entreprise/exporter-son-journal-de-ventes.md | facturation |
| journal des appels | sellsy | journal des appels | sellsy:app-mobile-sellsy-crm/app-sellsy-crm-le-journal-des-appels.md | indetermine |
| journaux comptables | progbat | journaux comptables (codes achats/ventes/banques/caisse) | progbat:le-menu-principal/comptabilite/parametrage-comptable/journaux.md | indetermine |
| labels d'événements | sellsy | labels d'événements (agenda) | sellsy:configuration-du-compte/personnaliser-les-labels-des-evenements.md | indetermine |
| labels de tâches | sellsy | labels de tâches | sellsy:configuration-du-compte/personnaliser-les-labels-de-taches.md | indetermine |
| langue | sellsy | langue (compte, traduction) | sellsy:documents-de-vente/etape-1-ajouter-une-langue-au-compte.md | indetermine |
| lettrage | extrabat | lettrage (facture/avoir) | extrabat:lettrer-payer-facture.md | facturation |
| lettrage comptable des factures et paiements | openfire | lettrage comptable des factures et paiements (à la facturation, en comptabilité, depuis les écritures) | openfire:knowsystem/lettrage-comptable-192.md | facturation |
| lettrage des factures et paiements non rapprochés | openfire | lettrage des factures et paiements non rapprochés | openfire:knowsystem/correspondance-des-paiements-et-des-factures-167.md | facturation |
| lettre de mission | axonaut | lettre de mission (modèle Word, génération depuis fiche client) | axonaut:gerez-vos-devis/comment-creer-une-lettre-de-mission-sur-axonaut.md | indetermine |
| liaison d'un poste libre à un ouvrage existant de la bibliothèque | vertuoza | liaison d'un poste libre à un ouvrage existant de la bibliothèque | vertuoza:documents/lier-une-ligne-a-un-ouvrage.md | devis |
| liaison d'un sous-traitant à un chantier | vertuoza | liaison d'un sous-traitant à un chantier | vertuoza:faq-foires-aux-questions/comment-lier-un-sous-traitant-a-un-chantier.md | chantier-intervention |
| liaison d'une facture à un chantier | vertuoza | liaison d'une facture à un chantier | vertuoza:faq-foires-aux-questions/comment-lier-une-facture-a-un-chantier.md | facturation |
| liaison plusieurs entreprises à un compte | obat | liaison plusieurs entreprises à un compte (FAQ) | obat:`peut-on-lier-plusieurs-entreprises-c3-a0-un-seul-compte-obat.md` | indetermine |
| licences utilisateurs | obat | licences utilisateurs / invitation collaborateurs | obat:`1-mois-de-licences-gratuites-pour-bien-d-c3-a9marrer-avec-obat.md` | indetermine |
| lien public | sellsy | lien public (partage document de vente) | sellsy:documents-de-vente/partager-mes-documents-de-vente-via-un-lien-public.md | facturation |
| ligne | costructor | ligne/section optionnelle (devis) | costructor:ventes/comment-rendre-optionnelle-une-ligne-ou-une-section-dans-un-devis-q3axji.md | devis |
| ligne de facture | progbat | ligne de facture (saisie d'avancement, suppression, annulation, modification) | progbat:le-menu-principal/devis-factures/factures/les-lignes-de-la-facture.md | facturation |
| lignes | extrabat | lignes/nomenclature dynamique (déplacement, pièce commerciale) | extrabat:deplacer-plusieurs-lignes-dans-la-gestion-commerciale.md | indetermine |
| lignes de devis | progbat | lignes de devis (chiffrage, cœur de métier) | progbat:le-menu-principal/devis-factures/devis/les-lignes-du-devis.md | devis |
| lignes de document | sellsy | lignes de document (lecteur code-barres) | sellsy:documents-de-vente/ajouter-des-lignes-avec-un-lecteur-code-barres.md | indetermine |
| lignes de documents de vente | sellsy | lignes de documents de vente (consultation / export) | sellsy:documents-de-vente/consulter-le-detail-des-lignes-des-documents-de-vente.md | facturation |
| lignes en option | sellsy | lignes en option (document de vente) | sellsy:documents-de-vente/ajouter-des-lignes-en-option.md | facturation |
| limite d'acquittement partiel d'une facture | vertuoza | limite d'acquittement partiel d'une facture (contournement) | vertuoza:faq-foires-aux-questions/comment-faire-une-facture-acquittee-partiellement-dans-vertuoza.md | facturation |
| limite d'export de certains modèles de devis | vertuoza | limite d'export de certains modèles de devis (type « document personnel ») | vertuoza:faq-foires-aux-questions/pourquoi-je-ne-peux-pas-exporter-mon-modele-de-devis.md | devis |
| limite d'export excel de la bibliothèque | vertuoza | limite d'export Excel de la bibliothèque (composants exclus, ouvrages selon contrat) | vertuoza:faq-foires-aux-questions/peut-on-exporter-la-bibliotheque-des-composants-et-ouvrages-en-excel-pour-effectuer-des-modifications-en-masse.md | devis |
| limite d'une seule retenue par facture d'avancement | vertuoza | limite d'une seule retenue par facture d'avancement (contournements) | vertuoza:faq-foires-aux-questions/peut-on-ajouter-plusieurs-retenues-sur-une-facture-d-avancement.md | facturation |
| limite d'unité de mesure unique par fourniture en gestion des stocks | vertuoza | limite d'unité de mesure unique par fourniture en gestion des stocks | vertuoza:faq-foires-aux-questions/est-il-possible-d-encoder-plusieurs-unites-pour-une-meme-fourniture-dans-la-gestion-des-stocks.md | achat |
| limite de détail de l'export excel des commandes | vertuoza | limite de détail de l'export Excel des commandes (ouvrages composés/composants exclus) | vertuoza:faq-foires-aux-questions/pourquoi-l-export-excel-ne-detaille-t-il-pas-ce-qui-a-ete-saisi-dans-chaque-commande.md | achat |
| limite de gestion des stocks en nombres entiers uniquement | vertuoza | limite de gestion des stocks en nombres entiers uniquement | vertuoza:faq-foires-aux-questions/pourquoi-mon-inventaire-ne-prend-il-en-compte-que-des-chiffres-entiers.md | achat |
| limite de l'unité « heures » pour la main d'œuvre en bibliothèque | vertuoza | limite de l'unité « heures » pour la main d'œuvre en bibliothèque (contournement) | vertuoza:faq-foires-aux-questions/comment-utiliser-un-autre-type-d-unite-jour-forfait-pour-la-main-d-oeuvre-dans-la-bibliotheque.md | devis |
| limite de la retenue de garantie sur une facture simple | vertuoza | limite de la retenue de garantie sur une facture simple (nécessite un chantier) | vertuoza:faq-foires-aux-questions/comment-ajouter-une-retenue-de-garantie-sur-une-facture-simple.md | facturation |
| limite de modification d'un avenant accepté | vertuoza | limite de modification d'un avenant accepté (suppression des documents ultérieurs requise) | vertuoza:faq-foires-aux-questions/est-il-possible-de-revenir-sur-un-avenant-accepte-et-rajouter-des-quantites-sans-creer-un-nouvel-avenant.md | chantier-intervention |
| limite de modification d'une facture comptabilisée | vertuoza | limite de modification d'une facture comptabilisée (contournement PDF externe) | vertuoza:faq-foires-aux-questions/comment-modifier-la-reference-d-une-facture-deja-comptabilisee.md | facturation |
| limite de sélection d'ouvriers pour un pointage antérieur | vertuoza | limite de sélection d'ouvriers pour un pointage antérieur (uniquement dates futures) | vertuoza:faq-foires-aux-questions/pourquoi-la-liste-des-ouvriers-n-apparait-elle-pas-dans-la-creation-d-un-pointage.md | chantier-intervention |
| limite de taille des pièces jointes | vertuoza | limite de taille des pièces jointes (10 Mo) | vertuoza:faq-foires-aux-questions/existe-t-il-une-limite-a-la-taille-des-pieces-jointes-que-je-peux-envoyer.md | indetermine |
| limite du calcul de l'avance | vertuoza | limite du calcul de l'avance (appliquée sur le sous-total HT, pas le montant final ajusté) | vertuoza:faq-foires-aux-questions/pourquoi-l-avance-n-est-elle-pas-appliquee-sur-le-montant-final-ajuste.md | chantier-intervention |
| liste | progbat | liste (recherche, filtre, tri, export, modification en masse) | progbat:presentation-generale/les-listes.md | indetermine |
| liste articles | extrabat | liste articles (export) | extrabat:editer-la-liste-des-articles.md | indetermine |
| liste de factures | extrabat | liste de factures (impression en masse) | extrabat:imprimer-plusieurs-factures-seule.md | facturation |
| liste de fournisseurs référencés | costructor | liste de fournisseurs référencés (catalogue) | costructor:debuter-sur-costructor/liste-des-fournisseurs-references-1rdft3t.md | achat |
| liste de prix | openfire | liste de prix (règles par contact) | openfire:knowsystem/comment-appliquer-des-regles-de-prix-par-contact-221.md | devis |
| liste des métadonnées disponibles pour la personnalisation des modèles d'email | vertuoza | liste des métadonnées disponibles pour la personnalisation des modèles d'email | vertuoza:faq-foires-aux-questions/metadonnees-existantes-dans-vertuoza-pour-l-envoi-d-e-mails.md | indetermine |
| liste des statuts du cycle d'envoi de la facturation électronique peppol | vertuoza | liste des statuts du cycle d'envoi de la facturation électronique PEPPOL | vertuoza:faq-foires-aux-questions/quels-sont-les-statuts-de-la-facturation-electronique.md | facturation |
| liste du personnel | progbat | liste du personnel (filtres, statuts) | progbat:le-menu-principal/chantiers-personnel/personnel/la-liste-du-personnel.md | indetermine |
| listes | sellsy | listes (personnalisation affichage) | sellsy:gestion-des-donnees/personnaliser-les-listes-prospect-client-contact-document.md | indetermine |
| livre blanc | obat | livre blanc (page de catégorie) | obat:`livres-blanc-dobat.md` | indetermine |
| livre de caisse électronique | extrabat | livre de caisse électronique (paramétrage, plan comptable) | extrabat:parametrer-son-livre-de-caisse-electronique.md | indetermine |
| livre des recettes | costructor | livre des recettes (comptabilité) | costructor:gestion-dentreprise/comment-fonctionne-le-livre-des-recettes-1bj062h.md | facturation |
| localisation client | openfire | localisation client (mise à jour, mobile) | openfire:guides-videos/mettre-a-jour-la-localisation-d-un-client-sur-mobile.md | indetermine |
| localisation du code d'entreprise | vertuoza | localisation du code d'entreprise (tenant) dans l'URL | vertuoza:faq-foires-aux-questions/ou-trouver-le-code-de-mon-entreprise.md | indetermine |
| logique cumulative des pourcentages d'avancement sur un poste | vertuoza | logique cumulative des pourcentages d'avancement sur un poste | vertuoza:faq-foires-aux-questions/pourquoi-mes-70-d-avancement-ne-sont-ils-pas-pris-en-compte.md | chantier-intervention |
| logique de génération automatique du numéro de devis | vertuoza | logique de génération automatique du numéro de devis | vertuoza:faq-foires-aux-questions/comment-le-systeme-genere-t-il-le-numero-d-un-nouveau-devis.md | devis |
| logique de mapping clients | vertuoza | logique de mapping clients/fournisseurs lors de la synchronisation comptable (cascade ID puis nom) | vertuoza:parametres/comment-fonctionne-le-mapping-des-clients-et-fournisseurs-lors-de-la-synchronisation.md | facturation |
| logique de recalcul automatique entre prix d'achat, marge et prix total | vertuoza | logique de recalcul automatique entre prix d'achat, marge et prix total | vertuoza:faq-foires-aux-questions/comment-fonctionne-le-calcul-lorsque-je-modifie-la-marge-ou-le-prix-d-achat.md | devis |
| logique de substitution du montant de bon de commande par le montant de facture supérieur | vertuoza | logique de substitution du montant de bon de commande par le montant de facture supérieur | vertuoza:faq-foires-aux-questions/quel-montant-est-pris-en-compte-si-ma-facture-fournisseur-est-superieure-au-bon-de-commande.md | achat |
| logique et procédure de déduction des acomptes dans les états d'avancement | vertuoza | logique et procédure de déduction des acomptes dans les états d'avancement | vertuoza:gestion-de-chantier/pourquoi-deduire-les-acomptes-lors-des-etats-d-avancements.md | facturation |
| logo | costructor | logo (marque blanche, documents) | costructor:debuter-sur-costructor/comment-supprimer-le-logo-costructor-de-mes-documents-1uh70of.md | indetermine |
| logo et informations de l'entreprise | inter-fast | logo et informations de l'entreprise (onboarding, coordonnées, métiers) | inter-fast:inter-fast/mon-entreprise/modifier-le-logo-et-les-informations-de-l-entreprise.md | indetermine |
| logo société | sellsy | logo société (document) | sellsy:documents-de-vente/inserer-le-logo-de-ma-societe-sur-un-document.md | facturation |
| logo sur documents | obat | logo sur documents | obat:`comment-ajouter-votre-logo-sur-vos-documents.md` | indetermine |
| légende des codes couleur du planning d'intervention | vertuoza | légende des codes couleur du planning d'intervention | vertuoza:faq-foires-aux-questions/quels-sont-les-codes-couleur-utilises-dans-le-planning-d-intervention-et-que-signifient-ils.md | chantier-intervention |
| majoration du rendement | vertuoza | majoration du rendement (heures de main-d'œuvre supplémentaires) sur un devis | vertuoza:documents/majoration-du-rendement.md | devis |
| majoration globale des prix de vente sur un devis | vertuoza | majoration globale des prix de vente sur un devis | vertuoza:documents/majoration-des-prix-de-vente.md | devis |
| mandats gocardless | sellsy | mandats GoCardless (import) | sellsy:paiements/importer-des-mandats-gocardless.md | indetermine |
| marketplace obat | obat | Marketplace Obat (sous-traitance/matériel) | obat:`la-marketplace-obat.md` | indetermine |
| marque | openfire | marque (conditions tarifaires, remises, prix) | openfire:configurer-openfire/configurer-mes-marques-definir-mes-conditions-tarifaires.md | indetermine |
| masquage d'informations sur devis | obat | masquage d'informations sur devis | obat:`comment-cacher-certaines-informations-sur-votre-devis.md` | devis |
| matériel installé | progbat | matériel installé (enregistrement, traçabilité, tâches de maintenance) | progbat:les-options/pourquoi-des-options/maintenance-et-interventions/materiels-installes.md | chantier-intervention |
| mention gestion des déchets sur devis | obat | mention gestion des déchets sur devis | obat:`comment-faire-apparaitre-la-gestion-des-d-c3-a9chets-sur-vos-devis-avec-obat.md` | devis |
| mention indemnités de retard | obat | mention indemnités de retard | obat:`comment-int-c3-a9grer-les-indemnit-c3-a9s-de-retard.md` | devis |
| mention légale franchise tva | obat | mention légale franchise TVA (changement réglementaire) | obat:`franchise-en-base-de-tva-la-mention-legale-de-vos-factures-change-au-1er-septembre-2026.md` | indetermine |
| mentions automatiques de bas de page sur les documents | vertuoza | mentions automatiques de bas de page sur les documents (fonctionnalité dépréciée pour les devis) | vertuoza:parametres/conditions-de-bas-de-page-ajoutez-des-mentions-automatiques-a-vos-documents.md | devis |
| mentions légales et politique de confidentialité | openfire | mentions légales et politique de confidentialité | openfire:mentions.md | indetermine |
| mentions obligatoires | sellsy | mentions obligatoires (facture, conformité légale) | sellsy:facturation-electronique/les-informations-obligatoires-d-une-facture.md | facturation |
| mentions obligatoires du devis | progbat | mentions obligatoires du devis (cadre légal) | progbat:le-menu-principal/devis-factures/devis/mentions-obligatoires-du-devis.md | devis |
| mentions obligatoires facture | obat | mentions obligatoires facture (Siret/TVA) | obat:`affichage-du-num-c3-a9ro-de-siret-du-professionnel.md` | facturation |
| mentions tva belge spécifiques | obat | mentions TVA belge spécifiques (factures) | obat:`mentions-specifiques-tva-belge-des-factures-conformes-et-securisees-avec-obat.md` | facturation |
| menu achat | openfire | menu Achat (navigation) | openfire:knowsystem/153.md | indetermine |
| menu comptabilité | openfire | menu Comptabilité (navigation) | openfire:knowsystem/154.md | indetermine |
| menu contact | openfire | menu Contact (navigation) | openfire:knowsystem/108.md | indetermine |
| menu crm | openfire | menu CRM (navigation) | openfire:knowsystem/126.md | indetermine |
| menu dashboard | openfire | menu Dashboard (navigation) | openfire:knowsystem/258.md | indetermine |
| menu facturation | openfire | menu Facturation (navigation) | openfire:knowsystem/181.md | indetermine |
| menu général + sous-menu ged | openfire | menu général + sous-menu GED (navigation) | openfire:knowsystem/303.md | indetermine |
| menu général + sous-menu outils de calcul | openfire | menu général + sous-menu Outils de Calcul (navigation) | openfire:knowsystem/270.md | indetermine |
| menu général + sous-menu rdv en ligne | openfire | menu général + sous-menu RDV en Ligne (navigation) | openfire:knowsystem/266.md | indetermine |
| menu général + sous-menu serveur mail | openfire | menu général + sous-menu Serveur Mail (navigation) | openfire:knowsystem/298.md | indetermine |
| menu général + sous-menu signature électronique | openfire | menu général + sous-menu Signature Électronique (navigation) | openfire:knowsystem/260.md | indetermine |
| menu général + sous-menu sms | openfire | menu général + sous-menu SMS (navigation) | openfire:knowsystem/241.md | indetermine |
| menu intervention | openfire | menu Intervention (navigation) | openfire:knowsystem/103.md | indetermine |
| menu marketing | axonaut | menu Marketing (campagnes email/SMS, statistiques, segmentation IA) | axonaut:creez-campagnes-marketing/comment-ca-marche-le-menu-marketing.md | indetermine |
| menu mobile | openfire | menu Mobile (navigation) | openfire:knowsystem/277.md | indetermine |
| menu publipostage | openfire | menu Publipostage (navigation) | openfire:knowsystem/231.md | indetermine |
| menu stock | openfire | menu Stock (navigation) | openfire:knowsystem/110.md | indetermine |
| menu vente | openfire | menu Vente (navigation) | openfire:knowsystem/116.md | indetermine |
| messagerie | obat | messagerie/contact entre artisans (Marketplace) | obat:`simplifiez-vos-echanges-entre-artisans-sur-la-marketplace.md` | indetermine |
| messagerie personnelle | progbat | messagerie personnelle (connexion Gmail/Outlook/FAI/domaine à ProGBat) | progbat:pour-bien-demarrer/parametrage/mon-profil/envoi-demails/parametrer-ma-propre-messagerie.md | indetermine |
| migration d'un suivi d'avancement de chantier depuis un autre logiciel | vertuoza | migration d'un suivi d'avancement de chantier depuis un autre logiciel | vertuoza:faq-foires-aux-questions/comment-creer-un-avancement-dans-vertuoza-lorsque-les-precedents-ont-ete-faits-sur-un-autre-logiciel.md | chantier-intervention |
| migration de contacts et bibliothèque de prix depuis un autre logiciel | vertuoza | migration de contacts et bibliothèque de prix depuis un autre logiciel (import Excel) | vertuoza:demarrer/les-imports-migrez-d-un-autre-logiciel-vers-vertuoza.md | indetermine |
| migration de données quickbooks | axonaut | migration de données QuickBooks (clients, fournisseurs, produits, factures) | axonaut:configurer-votre-compte/comment-importer-ses-donnees-quickbooks-dans-axonaut.md | indetermine |
| migration de facturation | progbat | migration de facturation (poursuite depuis un ancien logiciel, cas multiples : devis, acompte, situations) | progbat:pour-bien-demarrer/demarrer-avec-progbat/importer-mes-devis-et-factures/poursuivre-la-facturation-faite-sur-mon-ancien-logiciel.md | facturation |
| migration des anciens sav vers les demandes d'intervention | openfire | migration des anciens SAV vers les demandes d'intervention | openfire:knowsystem/migration-des-sav-291.md | chantier-intervention |
| migration facturation électronique | obat | migration facturation électronique (clé de migration) | obat:`vous-etes-deja-inscrit-sur-une-autre-plateforme-la-cle-de-migration.md` | facturation |
| minute de calcul | progbat | minute de calcul / modèle de calcul (surface, volume, application automatique aux lignes de devis) | progbat:presentation-generale/les-minutes-de-calcul-ou-modeles-de-calcul.md | devis |
| mise en avant des achats | obat | mise en avant des achats (synthèse « reste à payer ») | obat:`mettez-en-avant-vos-achats-pour-une-gestion-plus-claire-de-votre-tr-c3-a9sorerie.md` | achat |
| mise en forme devis | extrabat | mise en forme devis (texte, raccourcis) | extrabat:comment-mettre-en-forme-devis-gras-italique-souligne-total-etc.md | devis |
| mise en option d'une ligne de devis | vertuoza | mise en option d'une ligne de devis (poste non comptabilisé dans le total) | vertuoza:documents/mettre-en-option.md | devis |
| mise en page | vertuoza | mise en page (saut de page) du texte dans un devis | vertuoza:faq-foires-aux-questions/comment-faire-passer-du-texte-a-la-page-suivante-dans-un-devis.md | devis |
| mise en place et utilisation de la signature électronique | openfire | mise en place et utilisation de la signature électronique (Yousign) sur les devis | openfire:knowsystem/mise-en-place-de-la-signature-electronique-261.md | devis |
| mise à jour catalogue fournisseur | extrabat | mise à jour catalogue fournisseur (tarifs) | extrabat:comment-cela-se-passe-t-il-lors-de-la-mise-a-jour-dun-catalogue-fournisseur.md | achat |
| mise à jour du taux de tva sur un devis dans un état d'avancement | vertuoza | mise à jour du taux de TVA sur un devis dans un état d'avancement | vertuoza:faq-foires-aux-questions/comment-mettre-a-jour-le-taux-de-tva-sur-un-devis.md | devis |
| mise à jour en masse des articles de la bibliothèque | inter-fast | mise à jour en masse des articles de la bibliothèque (import CSV, prix) | inter-fast:inter-fast/outils/mettre-a-jour-les-articles-de-votre-bibliotheque.md | indetermine |
| mise à jour et archivage des articles depuis une base tarifaire centralisée fournisseur | openfire | mise à jour et archivage des articles depuis une base tarifaire centralisée fournisseur | openfire:knowsystem/mettre-a-jour-un-article-centralise-168.md | devis |
| mise à jour manuelle requise des pointages après déclaration tardive d'absence maladie | vertuoza | mise à jour manuelle requise des pointages après déclaration tardive d'absence maladie | vertuoza:faq-foires-aux-questions/que-faire-si-une-absence-pour-maladie-est-declaree-apres-la-generation-des-pointages.md | chantier-intervention |
| modale de fin de chantier | obat | modale de fin de chantier (avis, photos, Google) | obat:`valorisez-chaque-fin-de-chantier-avec-la-modale-de-fin-de-chantier-dans-obat.md` | chantier-intervention |
| mode conforme | sellsy | mode conforme (facturation, conformité légale) | sellsy:documents-de-vente/activer-le-mode-conforme-pour-les-documents-de-vente.md | facturation |
| mode de paiement | openfire | mode de paiement (comptabilisation directe/différée) | openfire:configurer-openfire/modes-de-paiement-manuels.md | facturation |
| mode hors ligne | inter-fast | mode hors ligne (rapport d'intervention sans réseau) | inter-fast:inter-fast/application-mobile/utiliser-l-application-mobile-sans-reseau-mode-hors-ligne.md | chantier-intervention |
| mode test | inter-fast | mode test (sortie, gestion des données de démarrage) | inter-fast:inter-fast/debuter-avec-interfast/sortir-du-mode-test.md | indetermine |
| modes de règlement | extrabat | modes de règlement (multi-agences, interface caisse) | extrabat:jai-plusieurs-agences-plusieurs-modes-de-reglements-carte-bleue-especes.md | facturation |
| modification d'un contrat et gestion des avenants | openfire | modification d'un contrat et gestion des avenants | openfire:knowsystem/modifier-un-contrat-312.md | chantier-intervention |
| modification d'un devis déjà validé | vertuoza | modification d'un devis déjà validé (suppression de chantier, avenant) | vertuoza:faq-foires-aux-questions/comment-modifie-un-devis-deja-valide.md | devis |
| modification d'une annonce publiée sur vertuowork | vertuoza | modification d'une annonce publiée sur VertuoWork | vertuoza:vertuowork/modifier-une-annonce-sur-vertuowork.md | indetermine |
| modification de la date d'une facture | vertuoza | modification de la date d'une facture (règles de chronologie légale) | vertuoza:faq-foires-aux-questions/puis-je-modifier-la-date-d-une-facture-emise-par-erreur.md | facturation |
| modification du mot de passe d'un utilisateur | vertuoza | modification du mot de passe d'un utilisateur (compte gestion/chantier) | vertuoza:parametres/comment-modifier-le-mot-de-passe-d-un-utilisateur.md | indetermine |
| modification du mot de passe de son propre profil | vertuoza | modification du mot de passe de son propre profil | vertuoza:parametres/modifier-le-mot-de-passe-de-mon-profil.md | indetermine |
| modification du nom d'un chantier | vertuoza | modification du nom d'un chantier (propagation sur tous les documents) | vertuoza:faq-foires-aux-questions/comment-modifier-le-nom-d-un-chantier-pour-qu-il-s-adapte-sur-tous-les-documents.md | chantier-intervention |
| modification détaillée d'un modèle de document | vertuoza | modification détaillée d'un modèle de document (page, zones, aperçu) | vertuoza:parametres/modifier-un-modele-personnalisez-vos-documents-etape-par-etape.md | devis |
| modification en masse de contacts ou ouvrages | vertuoza | modification en masse de contacts ou ouvrages (export/import Excel) | vertuoza:faq-foires-aux-questions/comment-puis-je-apporter-des-modifications-en-masse-a-mes-contacts-ou-ouvrages.md | indetermine |
| module abonnement | sellsy | module abonnement (introduction) | sellsy:documents-de-vente/introduction-module-abonnement.md | indetermine |
| module calendrier | inter-fast | module Calendrier (vues, filtres, synchronisation iCal) | inter-fast:inter-fast/operations/comprendre-le-module-calendrier.md | chantier-intervention |
| module de pointage | vertuoza | module de pointage (temps de travail) sur l'app mobile | vertuoza:application-mobile/ouvrier-module-pointage-sur-l-app-mobile.md | chantier-intervention |
| module exports comptables | sellsy | module exports comptables (introduction) | sellsy:suivi-financier/introduction-module-d-exports-comptables.md | indetermine |
| module interventions | obat | module Interventions (planification, rapport, facturation, signature) | obat:`la-gestion-des-interventions-dans-obat.md` | chantier-intervention |
| module marketing | sellsy | module marketing (découverte, checklist) | sellsy:module-marketing/marketing-decouvrir-sellsy-marketing.md | indetermine |
| module métrés | obat | module Métrés (relevé terrain) | obat:`les-metres-dans-obat-relevez-vos-chantiers-directement-depuis-votre-logiciel.md` | chantier-intervention |
| module redactor | sellsy | module Redactor (introduction) | sellsy:crm-et-prospection/introduction-module-redactor.md | indetermine |
| module sms | extrabat | module SMS (confirmation RDV) | extrabat:module-sms.md | indetermine |
| module stock | sellsy | module stock (introduction) | sellsy:module-stocks/introduction-module-stock.md | indetermine |
| module support | sellsy | module support (paramétrage) | sellsy:module-support/parametrer-le-module-support.md | indetermine |
| module wordpress | sellsy | module WordPress (formulaire, tracking) | sellsy:integrations-et-api/module-sellsy-pour-wordpress.md | indetermine |
| modules installés | openfire | modules installés (instance Odoo, informations techniques) | openfire:website/info.md | indetermine |
| modèle d'email | costructor | modèle d'email / espace client | costructor:debuter-sur-costructor/comment-personnaliser-les-modeles-demail-fjou49.md | indetermine |
| modèle d'email personnalisé | sellsy | modèle d'email personnalisé | sellsy:configuration-du-compte/creer-des-modeles-d-emails-personnalises.md | indetermine |
| modèle de devis | costructor | modèle de devis (réutilisable) | costructor:ventes/comment-creer-un-modele-de-devis-171gtrc.md | devis |
| modèle de document juridique | progbat | modèle de document juridique (Caarl, téléchargement) | progbat:le-menu-principal/service-juridique/base-de-modeles-de-documents.md | indetermine |
| modèle de document sur mesure | extrabat | modèle de document sur mesure (devis/facture) | extrabat:creer-un-modele-de-document-sur-mesure-devis-facture-etc.md | indetermine |
| modèle de document word | axonaut | modèle de document Word (champs dynamiques, génération fiche client) | axonaut:optimisez-gestion-commerciale/creer-un-modele-de-document-word-docx.md | indetermine |
| modèle de rapprochement bancaire | openfire | modèle de rapprochement bancaire (automatisation lettrage) | openfire:utiliser-openfire/utilisez-des-modeles-rapprochement-bancaire-automatiques.md | facturation |
| modèle de réponse | sellsy | modèle de réponse (ticket support) | sellsy:module-support/definir-un-modele-de-reponse-standardisee-pour-un-ticket-de-support.md | indetermine |
| modèle facture d'abonnement | sellsy | modèle facture d'abonnement (variables période) | sellsy:documents-de-vente/creer-un-modele-de-facture-d-abonnement.md | facturation |
| modèle redactor | sellsy | modèle Redactor (document dynamique) | sellsy:crm-et-prospection/creer-un-modele-redactor.md | indetermine |
| modèles | axonaut | modèles (documents, emails, tâches, commentaires — index) | axonaut:centralisez-gestion-emails-courriers/modeles-emails-2.md | indetermine |
| modèles d'email | inter-fast | modèles d'email (création, variables, envoi) | inter-fast:inter-fast/mon-entreprise/creer-un-modele-d-e-mail.md | indetermine |
| modèles de devis | inter-fast | modèles de devis (création, personnalisation, utilisation) | inter-fast:inter-fast/mon-entreprise/construire-ses-modeles-de-devis.md | devis |
| modèles de devis préconfigurés | obat | modèles de devis préconfigurés (par métier) | obat:`les-modeles-de-documents-obat.md` | devis |
| modèles de rapports d'intervention | inter-fast | modèles de rapports d'intervention (constructeur, personnalisation) | inter-fast:inter-fast/mon-entreprise/construire-les-modeles-de-rapports.md | chantier-intervention |
| modèles et gabarits | inter-fast | modèles et gabarits (documents légaux, imports, présentation commerciale) | inter-fast:inter-fast/debuter-avec-interfast/boite-a-outils-telecharger-nos-modeles-et-gabarits-de-documents.md | indetermine |
| moyens | sellsy | moyens / délais de paiement (traduction) | sellsy:documents-de-vente/etape-5-traduire-les-moyens-et-delais-de-paiement.md | indetermine |
| moyens de paiement | progbat | moyens de paiement (extension de compte comptable par mode de règlement) | progbat:le-menu-principal/comptabilite/parametrage-comptable/moyens-de-paiement.md | indetermine |
| multi-adresse client | obat | multi-adresse client | obat:`comment-ajouter-plusieurs-adresses-diff-c3-a9rentes-c3-a0-un-client-sur-obat.md` | devis |
| multi-ressources sur événement calendrier | obat | multi-ressources sur événement calendrier | obat:`comment-ajouter-plusieurs-ressources-dans-un-evenement-du-calendrier.md` | indetermine |
| multi-taux tva sur achats | obat | multi-taux TVA sur achats | obat:`multi-taux-de-tva-sur-les-achats-saisissez-vos-factures-fournisseurs-en-toute-precision.md` | achat |
| multi-user | obat | multi-user (page de catégorie) | obat:`multi-user.md` | indetermine |
| mécanique d'application d'une remise sur une facture | vertuoza | mécanique d'application d'une remise sur une facture (répartition, double effet) | vertuoza:faq-foires-aux-questions/comment-est-appliquee-la-remise-sur-une-facture.md | facturation |
| mécanique d'application des remises et du prorata | vertuoza | mécanique d'application des remises et du prorata (héritage, calcul d'acompte) | vertuoza:faq-foires-aux-questions/comment-fonctionne-l-application-des-remises-et-du-prorata-dans-vertuoza.md | devis |
| médiation de la consommation | obat | médiation de la consommation (obligation légale) | obat:`la-mediation-de-la-consommation-une-obligation-et-une-opportunite-pour-les-professionnels-du-batiment.md` | indetermine |
| métadonnées | vertuoza | métadonnées/balises dynamiques personnalisables dans les modèles d'email | vertuoza:parametres/les-metadonnees-dans-les-e-mails.md | indetermine |
| méthode d'arrondi de tva | costructor | méthode d'arrondi de TVA | costructor:debuter-sur-costructor/comment-changer-la-methode-darrondi-de-tva-zvscnf.md | indetermine |
| méthode recommandée pour que la retenue soit correctement héritée dans le chantier | vertuoza | méthode recommandée pour que la retenue soit correctement héritée dans le chantier | vertuoza:faq-foires-aux-questions/comment-gerer-une-retenue-pour-qu-elle-soit-bien-prise-en-compte-dans-le-chantier.md | devis |
| méthodes de modification d'un devis accepté | vertuoza | méthodes de modification d'un devis accepté (avenant ou suppression du chantier vide) | vertuoza:faq-foires-aux-questions/que-faire-si-je-dois-modifier-un-devis-deja-accepte.md | devis |
| météo intégrée | obat | météo intégrée (widget) | obat:`la-meteo-sur-obat.md` | chantier-intervention |
| navigateur recommandé | obat | navigateur recommandé (Google Chrome) | obat:`utilisez-obat-via-google-chrome.md` | indetermine |
| navigateurs compatibles | sellsy | navigateurs compatibles (configuration système) | sellsy:conseils-d-utilisation/navigateurs-compatibles-avec-sellsy.md | indetermine |
| navigation dans l'application mobile | openfire | navigation dans l'application mobile (vues jour/planning/contacts) et notifications | openfire:knowsystem/navigation-et-notifications-222.md | chantier-intervention |
| newsletter | sellsy | newsletter (conseils marketing) | sellsy:module-marketing/marketing-5-astuces-pour-maximiser-les-performances-de-vos-newsletters.md | indetermine |
| nom client | extrabat | nom client (affichage agenda, champ objet/notes) | extrabat:le-nom-du-client-napparait-pas-dans-lagenda.md | indetermine |
| nom de document pdf | costructor | nom de document PDF (personnalisation) | costructor:debuter-sur-costructor/comment-personnaliser-le-nom-des-documents-pdf-11saa5b.md | indetermine |
| nomenclature dynamique | extrabat | nomenclature dynamique (création, devis) | extrabat:nomenclature-dynamique.md | devis |
| nomenclatures | extrabat | nomenclatures (mise à jour) | extrabat:mise-a-jour-des-nomenclatures.md | indetermine |
| nommage des pièces justificatives | obat | nommage des pièces justificatives (exports comptables) | obat:`exports-comptables-vos-pieces-justificatives-sont-desormais-nommees-de-fa-c3-a7on-coherente.md` | achat |
| non-mise à jour automatique des coordonnées de facturation d'un chantier existant | vertuoza | non-mise à jour automatique des coordonnées de facturation d'un chantier existant | vertuoza:faq-foires-aux-questions/les-coordonnees-de-facturation-d-un-chantier-se-mettent-elles-automatiquement-a-jour-si-les-coordonnees-du-client-sont-modifiees.md | facturation |
| non-répercussion automatique des mises à jour de bibliothèque sur les devis existants | vertuoza | non-répercussion automatique des mises à jour de bibliothèque sur les devis existants | vertuoza:faq-foires-aux-questions/quand-un-ouvrage-est-mis-a-jour-dans-la-biblio-de-prix-les-prix-sont-ils-automatiquement-mis-a-jour-dans-les-devis-existants.md | devis |
| non-rétroactivité de la synchronisation ponto pour les paiements | vertuoza | non-rétroactivité de la synchronisation Ponto pour les paiements | vertuoza:faq-foires-aux-questions/est-ce-que-la-synchronisation-avec-ponto-est-retroactive-pour-les-paiements.md | facturation |
| note de frais | axonaut | note de frais (création, validation, suppression selon statut de paiement) | axonaut:creez-depenses-facilement/valider-une-note-de-frais-ndf.md | achat |
| notes de chantier | obat | notes de chantier (centralisation infos terrain) | obat:`notes-de-chantier-ne-perdez-plus-aucune-information-terrain-avec-obat.md` | chantier-intervention |
| notes de chantier depuis le devis | obat | notes de chantier depuis le devis | obat:`vos-notes-de-chantier-directement-dans-votre-devis.md` | devis |
| notes de frais | sellsy | notes de frais (réforme facturation électronique) | sellsy:facturation-electronique/facturation-electronique-frais-generaux-et-notes-de-frais.md | indetermine |
| notice technique | extrabat | notice technique/éclaté (liaison à un article) | extrabat:relier-une-notice-etou-un-eclate-a-un-article-dans-un-dossier-client.md | indetermine |
| notifications push | obat | notifications push (consentement, configuration) | obat:`notifications-push-simplifiez-la-reception-dalertes-en-temps-reel.md` | indetermine |
| nouveau planning par ouvrier | vertuoza | nouveau planning par ouvrier (drag & drop, indicateurs visuels) | vertuoza:beta/planning-par-homme.md | chantier-intervention |
| nouvel éditeur de devis v2 | inter-fast | nouvel éditeur de devis V2 (fonctionnalités, structuration) | inter-fast:inter-fast/finances/utiliser-le-nouvel-editeur-de-devis.md | devis |
| nouvel éditeur de facture v2 | inter-fast | nouvel éditeur de facture V2 (fonctionnalités, structuration) | inter-fast:inter-fast/finances/utiliser-le-nouvel-editeur-de-facture.md | facturation |
| nouvelles fonctionnalités des pages de listes | vertuoza | nouvelles fonctionnalités des pages de listes (colonnes, tri, filtres, persistance) | vertuoza:parametres/configuration-des-nouvelles-pages-listes.md | indetermine |
| numéro de capacité | inter-fast | numéro de capacité (définition, renseignement) | inter-fast:inter-fast/fluides-frigorigenes/renseigner-mon-numero-de-capacite.md | indetermine |
| numéro de révision de devis | costructor | numéro de révision de devis (masquage) | costructor:ventes/comment-masquer-le-numero-de-revision-dun-devis-1miqhx5.md | devis |
| numéro de série | sellsy | numéro de série (stock) | sellsy:module-stocks/gerer-les-numeros-de-serie.md | indetermine |
| numéro sap | extrabat | numéro SAP (obligation URSSAF) | extrabat:nouvelle-obligation-de-lurssaf-renseignement-du-numero-sap-de-lintervenant.md | indetermine |
| numérotation | sellsy | numérotation (devis / factures) | sellsy:documents-de-vente/changer-la-numerotation-des-devis-et-factures.md | facturation |
| numérotation de facture | costructor | numérotation de facture | costructor:debuter-sur-costructor/comment-parametrer-la-numerotation-des-factures-yovy8o.md | facturation |
| numérotation des devis | inter-fast | numérotation des devis/factures (format, prochain numéro) | inter-fast:inter-fast/mon-entreprise/modifier-la-numerotation-des-devis-factures.md | facturation |
| numérotation des documents | progbat | numérotation des documents (factures, devis — séquence chronologique) | progbat:pour-bien-demarrer/parametrage/parametres-de-lentreprise/numero-des-documents.md | facturation |
| numérotation des dépenses | inter-fast | numérotation des dépenses (format, prochain numéro) | inter-fast:inter-fast/mon-entreprise/modifier-la-numerotation-des-depenses.md | facturation |
| numérotation devis | axonaut | numérotation devis/factures (préfixe, compteur, obligation légale) | axonaut:gerez-vos-devis/comment-numeroter-mes-devis-dans-axonaut.md | indetermine |
| numérotation documents | obat | numérotation documents (factures/avoirs/devis) | obat:`comment-modifier-la-num-c3-a9rotation-de-vos-factures/avoirs/devis.md` | indetermine |
| numérotation forcée | costructor | numérotation forcée (recréation d'un ancien devis) | costructor:ventes/recreer-un-ancien-devis-rcvxtx.md | devis |
| numérotation lignes | obat | numérotation lignes/sections (devis) | obat:`comment-ins-c3-a9rer-un-c3-a9l-c3-a9ment-c3-a0-une-section-pour-r-c3-a9tablir-la-bonne-num-c3-a9rotation-de-vos-lignes-et-le-bon-calcul-des-sous-totaux.md` | devis |
| numérotation manuelle vs automatique des factures fournisseurs | vertuoza | numérotation manuelle vs automatique des factures fournisseurs (selon synchro comptable) | vertuoza:faq-foires-aux-questions/pourquoi-certaines-factures-fournisseurs-n-ont-elles-pas-de-numero-par-defaut.md | achat |
| numérotation personnalisée | obat | numérotation personnalisée (lignes devis) | obat:`comment-modifier-et-personnaliser-la-num-c3-a9rotation-des-lignes-dun-devis-sur-obat.md` | devis |
| nécessité d'un responsable assigné pour créer une note de crédit liée à un créditeur | vertuoza | nécessité d'un responsable assigné pour créer une note de crédit liée à un créditeur | vertuoza:faq-foires-aux-questions/pourquoi-ne-puis-je-pas-creer-une-note-de-credit-si-la-facture-est-liee-a-un-crediteur.md | facturation |
| obat & chift | obat | Obat & Chift (comptabilité BTP) | obat:`obat-chift-la-solution-incontournable-pour-la-comptabilit-c3-a9-des-entreprises-du-b-c3-a2timent.md` | indetermine |
| objectif ca mensuel | extrabat | objectif CA mensuel (paramétrage, widget) | extrabat:rentrer-son-objectif-mensuel-de-chiffre-daffaire.md | indetermine |
| objectifs commerciaux | sellsy | objectifs commerciaux | sellsy:crm-et-prospection/definir-des-objectifs-commerciaux.md | indetermine |
| obsolescence des anciens modèles de devis | vertuoza | obsolescence des anciens modèles de devis (migration vers nouveau module) | vertuoza:faq-foires-aux-questions/pourquoi-mon-modele-de-devis-est-il-marque-comme-obsolete-et-que-faire.md | devis |
| ocr pour saisie des achats | obat | OCR pour saisie des achats | obat:`comment-utiliser-la-reconnaissance-optique-de-caract-c3-a8res-ocr-lors-de-la-saisie-de-vos-d-c3-a9penses-sur-obat.md` | achat |
| offre e-réputation | obat | offre E-Réputation (avis clients, visibilité) | obat:`offre-e-reputation.md` | indetermine |
| offre jeune entreprise | costructor | offre jeune entreprise / abonnement | costructor:abonnement/comment-beneficier-de-loffre-jeune-entreprise-1vs4eiy.md | indetermine |
| offre progbat | progbat | offre ProGBat (licence, abonnement, factures, multi-comptes) | progbat:pour-bien-demarrer/parametrage/mon-offre-progbat.md | indetermine |
| onglet mon abonnement | inter-fast | onglet Mon abonnement (factures, plan, moyen de paiement) | inter-fast:inter-fast/mon-entreprise/comprendre-l-onglet-mon-abonnement.md | facturation |
| onglet planning | obat | onglet Planning (par chantier) | obat:`g-c3-a9rez-vos-chantiers-plus-facilement-gr-c3-a2ce-c3-a0-longlet-planning.md` | chantier-intervention |
| onglets | progbat | onglets (multitâche, navigation) | progbat:presentation-generale/les-onglets.md | indetermine |
| optimisation de la planification des rendez-vous | openfire | optimisation de la planification des rendez-vous (recherche de créneau) | openfire:knowsystem/optimisation-des-rdv-89.md | chantier-intervention |
| option | progbat | option/variante de devis (lignes non comptées dans le total) | progbat:le-menu-principal/devis-factures/devis/variantes-et-options.md | devis |
| option bordereau | obat | option bordereau (afficher sections uniquement) | obat:`nouvelle-option-sur-le-bordereau-gagnez-en-clart-c3-a9-et-en-efficacit-c3-a9.md` | devis |
| option « accès compagnons » | progbat | option « accès compagnons » (application mobile salariés) | progbat:les-options/pourquoi-des-options/acces-compagnons.md | indetermine |
| option « assistance juridique et recouvrement » | progbat | option « assistance juridique et recouvrement » | progbat:les-options/pourquoi-des-options/assistance-juridique-et-recouvrement.md | indetermine |
| option « bibliothèques batichiffrage© » | progbat | option « bibliothèques BatiChiffrage© » (achat de licence par corps de métier) | progbat:les-options/pourquoi-des-options/bibliotheques-batichiffrage-c.md | devis |
| option « connexion comptes bancaires » | progbat | option « connexion comptes bancaires » (Powens, rapprochement) | progbat:les-options/pourquoi-des-options/connexion-comptes-bancaires.md | indetermine |
| option « connexions supplémentaires » | progbat | option « connexions supplémentaires » (utilisateurs simultanés) | progbat:les-options/pourquoi-des-options/connexions-supplementaires.md | indetermine |
| option « gestion des droits » | progbat | option « gestion des droits » (permissions utilisateurs) | progbat:les-options/pourquoi-des-options/gestion-des-droits.md | indetermine |
| option « maintenance et interventions » | progbat | option « maintenance et interventions » (module) | progbat:les-options/pourquoi-des-options/maintenance-et-interventions.md | chantier-intervention |
| option « océrisation » | progbat | option « océrisation » (crédits OCR pour factures/tickets) | progbat:les-options/pourquoi-des-options/ocerisation.md | achat |
| options | progbat | options (modèle économique : Essential/Premium/All Inclusive, liste des options) | progbat:les-options/pourquoi-des-options.md | indetermine |
| options par défaut des documents | obat | options par défaut des documents | obat:`les-options-par-d-c3-a9faut-des-documents.md` | indetermine |
| options visuelles du planning | obat | options visuelles du planning (colonnes) | obat:`param-c3-a9trer-vos-options-visuel-de-planning.md` | chantier-intervention |
| organisation et gestion documentaire | openfire | organisation et gestion documentaire (GED) des documents clients | openfire:knowsystem/gestion-electronique-des-documents-ged-301.md | indetermine |
| outils de gestion externe | progbat | outils de gestion externe (transfert de données de facturation/comptables) | progbat:les-options/pourquoi-des-options/connexions-comptables/mes-outils-de-gestion-externe.md | facturation |
| outils pour experts-comptables | obat | outils pour experts-comptables (accès, exports) | obat:`les-outils-a-disposition-pour-les-experts-comptables.md` | indetermine |
| outils transversaux | extrabat | outils transversaux (création article, statistiques — agrégat) | extrabat:tag/outils.md | indetermine |
| ouverture de compte pro | axonaut | ouverture de Compte Pro (éligibilité, KYC, bénéficiaires effectifs, découvert) | axonaut:compte-pro-cartes/comment-ouvrir-un-compte-pro-axonaut.md | indetermine |
| ouvrage composé | progbat | ouvrage composé (décomposition en éléments : matériaux, main d'œuvre, location, sous-traitance, outillage) | progbat:le-menu-principal/bibliotheque/ouvrages/les-ouvrages-composes.md | devis |
| ouvrage détaillé | costructor | ouvrage détaillé / composé (devis ou bibliothèque) | costructor:ventes/comment-creer-un-ouvrage-detaille-1sv5az8.md | devis |
| ouvrages | inter-fast | ouvrages (création, imbrication, masquage prix/composition, mobile) | inter-fast:inter-fast/outils/utiliser-les-ouvrages.md | devis |
| pa d'émission | sellsy | PA d'émission (rôle, obligations) | sellsy:facturation-electronique/sellsy-pa-d-emission-et-vous.md | indetermine |
| pa de réception | sellsy | PA de réception (rôle, obligations, activation) | sellsy:facturation-electronique/sellsy-pa-de-reception-et-vous.md | indetermine |
| page client document | obat | page client document (visualisation devis/facture) | obat:`la-page-client-document-obat.md` | indetermine |
| page de renvoi vers un webinaire enregistré sur l'application mobile et les rdv | openfire | page de renvoi vers un webinaire enregistré sur l'application mobile et les RDV | openfire:knowsystem/webinaire-mobile-244.md | indetermine |
| page de renvoi vers un webinaire enregistré sur la gestion d'inventaire | openfire | page de renvoi vers un webinaire enregistré sur la gestion d'inventaire | openfire:knowsystem/webinaire-inventaire-235.md | indetermine |
| page de renvoi vers un webinaire enregistré sur la signature électronique | openfire | page de renvoi vers un webinaire enregistré sur la signature électronique | openfire:knowsystem/webinaire-signature-electronique-263.md | indetermine |
| page publique des équipements via qr code | inter-fast | page publique des équipements via QR code (accès sans authentification, signalement) | inter-fast:inter-fast/outils/activer-et-utiliser-la-page-publique-de-vos-equipements-via-qr-code.md | chantier-intervention |
| page tarifaire | obat | page tarifaire (options complémentaires) | obat:`la-page-tarifaire-obat-decouvrez-les-options-qui-boostent-votre-activite.md` | indetermine |
| page visibilité | obat | page visibilité (teaser E-réputation) | obat:`la-page-visibilit-c3-a9-obat.md` | indetermine |
| pages favorites | inter-fast | pages favorites (vues personnalisées, filtres enregistrés) | inter-fast:inter-fast/debuter-avec-interfast/comment-enregistrer-et-retrouver-vos-pages-favorites-dans-interfast.md | indetermine |
| paiement de dépense | axonaut | paiement de dépense (virement, prélèvement, rapprochement bancaire) | axonaut:creez-depenses-facilement/comment-payer-ses-depenses-sur-axonaut.md | achat |
| paiement de facture | axonaut | paiement de facture (manuel vs rapprochement, cas de doublon) | axonaut:gerez-vos-factures/comment-ajouter-un-paiement-sur-une-facture.md | facturation |
| paiement de facture via qr code | vertuoza | paiement de facture via QR code (activation, expérience client) | vertuoza:finance/paiement-de-la-facture-via-qr-code.md | facturation |
| paiement différé | extrabat | paiement différé (chèques) | extrabat:comment-sont-geres-les-paiements-differes-par-cheques.md | facturation |
| paiement en ligne adyen | sellsy | paiement en ligne Adyen (activation) | sellsy:paiements/activer-le-paiement-en-ligne-avec-adyen.md | facturation |
| paiement en ligne de devis | axonaut | paiement en ligne de devis (transition automatique en facture) | axonaut:gerez-vos-devis/comment-faire-payer-mes-devis-sur-axonaut.md | devis |
| paiement en ligne paypal | sellsy | paiement en ligne PayPal (activation) | sellsy:paiements/activer-le-paiement-en-ligne-avec-paypal.md | facturation |
| paiement en ligne stancer | sellsy | paiement en ligne Stancer (activation) | sellsy:paiements/activer-le-paiement-en-ligne-avec-stancer.md | facturation |
| paiement en ligne stripe | sellsy | paiement en ligne Stripe (activation) | sellsy:paiements/activer-le-paiement-en-ligne-avec-stripe.md | facturation |
| paiement multiple | extrabat | paiement multiple (fiche client) | extrabat:comment-effectuer-un-paiement-multiple-par-la-fiche-client.md | facturation |
| paiement par carte | axonaut | paiement par carte (Stripe, portail client, risque de doublon) | axonaut:gerez-vos-factures/faire-payer-mes-factures-par-carte-via-stripe.md | facturation |
| paiement par virement simplifié | obat | paiement par virement simplifié | obat:`le-paiement-par-virement-simplifie.md` | facturation |
| paiement récurrent stripe | sellsy | paiement récurrent Stripe (empreinte CB) | sellsy:paiements/encaissez-vos-paiements-recurrents-avec-stripe.md | facturation |
| paiements | inter-fast | paiements (tableau, consignation partielle, export) | inter-fast:inter-fast/finances/comprendre-le-tableau-des-paiements.md | facturation |
| paiements en ligne | sellsy | paiements en ligne (guide complet, panorama prestataires) | sellsy:paiements/paiements-en-ligne-guide-complet.md | facturation |
| paiements en masse | sellsy | paiements en masse (enregistrement) | sellsy:paiements/enregistrer-des-paiements-en-masse.md | facturation |
| paiements et taxes | inter-fast | paiements et taxes (RIB, conditions de paiement, TVA, acomptes devis) | inter-fast:inter-fast/mon-entreprise/configurer-la-partie-paiements-taxes.md | indetermine |
| paramètres d'utilisation | progbat | paramètres d'utilisation (enregistrement auto, visibilité privée, export CSV/Excel) | progbat:pour-bien-demarrer/parametrage/mon-profil/parametres-dutilisation.md | indetermine |
| paramètres utilisateur | extrabat | paramètres utilisateur (application Extrabat Today) | extrabat:gerer-ses-parametres-utilisateurs-dans-lapplication-extrabat-today.md | indetermine |
| paramétrage | progbat | paramétrage (accès, droits administrateur) | progbat:pour-bien-demarrer/parametrage.md | indetermine |
| paramétrage comptable | progbat | paramétrage comptable (comptes, TVA, familles, tiers) | progbat:le-menu-principal/comptabilite/parametrage-comptable.md | indetermine |
| paramétrage compte | obat | paramétrage compte / mise en page documents | obat:`comment-parametrer-votre-compte-obat.md` | indetermine |
| paramétrage de l'export comptable | inter-fast | paramétrage de l'export comptable (TVA, journal ventes/achats, agences) | inter-fast:inter-fast/mon-entreprise/parametrer-l-export-comptable.md | facturation |
| paramétrage de l'impression du devis | openfire | paramétrage de l'impression du devis (structure, images, titres, modèles) | openfire:knowsystem/parametrer-l-impression-du-devis-129.md | devis |
| paramétrage des fiches employés | openfire | paramétrage des fiches employés (poste, horaires, RH, compétences) | openfire:knowsystem/employes-65.md | indetermine |
| paramétrage des modes de paiement | openfire | paramétrage des modes de paiement (journal, compte bancaire, affichage) | openfire:knowsystem/modes-de-paiements-283.md | facturation |
| paramétrage des modules | obat | paramétrage des modules (activation/désactivation) | obat:`le-parametrage-des-modules-sur-obat.md` | indetermine |
| paramétrage du module chantiers | inter-fast | paramétrage du module Chantiers (renommage, accès documents, traitement des déchets) | inter-fast:inter-fast/mon-entreprise/parametrer-mes-chantiers.md | chantier-intervention |
| paramétrage initial du logiciel | vertuoza | paramétrage initial du logiciel (profil, société, personnalisation des documents) | vertuoza:demarrer/parametrage-essentiel-configurez-le-logiciel-a-votre-image.md | indetermine |
| paramétrage sav | axonaut | paramétrage SAV/ticketing (portail client, statuts, réponses auto) | axonaut:centralisez-gestion-sav/parametrer-son-sav-ou-ticketing.md | chantier-intervention |
| paramétrer mon compte | obat | paramétrer mon compte (page de catégorie) | obat:`param-c3-a9trer-mon-compte.md` | indetermine |
| parrainage | costructor | parrainage (programme de référencement) | costructor:abonnement/comment-parrainer-une-entreprise-psonbr.md | indetermine |
| parrainage et affiliation | axonaut | parrainage et affiliation (récompenses, conditions d'activation) | axonaut:configurer-votre-compte/parrainage-comment-ca-marche.md | indetermine |
| partage de bibliothèque d'articles entre entreprises | inter-fast | partage de bibliothèque d'articles entre entreprises (multi-société) | inter-fast:inter-fast/outils/partager-sa-bibliotheque-d-articles-et-d-ouvrages.md | indetermine |
| partage de données | sellsy | partage de données (collaborateurs) | sellsy:configuration-du-compte/partager-des-donnees-entre-collaborateurs.md | indetermine |
| partenaire professionnel | openfire | partenaire professionnel (configuration facturation électronique) | openfire:utiliser-openfire/verifier-et-configurer-un-partenaire-professionnel-pour-la-facturation-electronique.md | facturation |
| pays d'établissement | inter-fast | pays d'établissement (modification, adaptation des formats d'adresse) | inter-fast:inter-fast/mon-entreprise/modifier-le-pays-d-etablissement-de-mon-entreprise.md | indetermine |
| performance | sellsy | performance (conseils techniques) | sellsy:conseils-d-utilisation/conseils-pour-ameliorer-la-performance-de-sellsy.md | indetermine |
| performance commerciale | obat | performance commerciale (ratio devis) | obat:`comment-visualiser-votre-performance-commerciale-sur-obat.md` | devis |
| personnalisation apparence devis | obat | personnalisation apparence devis | obat:`comment-soigner-lapparence-de-vos-devis.md` | devis |
| personnalisation avancée de la mise en page des documents | vertuoza | personnalisation avancée de la mise en page des documents (avenants, factures) via PDF builder | vertuoza:parametres/documents-personnalises-pdf-builder.md | facturation |
| personnalisation colonnes listings | obat | personnalisation colonnes listings | obat:`personnaliser-l-affichage-de-vos-tableaux.md` | indetermine |
| personnalisation de documents | costructor | personnalisation de documents (apparence/thème) | costructor:debuter-sur-costructor/comment-personnaliser-mes-documents-13ywvrp.md | indetermine |
| personnalisation de l'affichage du planning | openfire | personnalisation de l'affichage du planning (filtres, couleurs, créneaux) | openfire:knowsystem/personnalisation-du-planning-117.md | chantier-intervention |
| personnalisation de la présentation des devis | inter-fast | personnalisation de la présentation des devis/factures (en-tête, polices, filigrane, CGV, pied de page) | inter-fast:inter-fast/mon-entreprise/personnaliser-mes-devis-factures-clients.md | indetermine |
| personnalisation des rapports d'intervention | inter-fast | personnalisation des rapports d'intervention (style, filigrane, géolocalisation) | inter-fast:inter-fast/mon-entreprise/personnaliser-mes-rapports-d-intervention.md | chantier-intervention |
| personnalisation du compte utilisateur | openfire | personnalisation du compte utilisateur (mot de passe, fuseau horaire, notifications, page d'accueil) | openfire:knowsystem/personnaliser-votre-compte-utilisateur-97.md | indetermine |
| personnalisation ponctuelle d'un modèle pour un devis précis sans affecter le modèle principal | vertuoza | personnalisation ponctuelle d'un modèle pour un devis précis sans affecter le modèle principal | vertuoza:parametres/visualisation-et-ajustements-comment-personnaliser-un-modele-pour-un-devis-precis.md | devis |
| personnalisation présentation documents | obat | personnalisation présentation documents | obat:`comment-am-c3-a9liorer-la-pr-c3-a9sentation-de-vos-documents-sur-obat.md` | indetermine |
| personnalisation visuelle | axonaut | personnalisation visuelle (devis/factures, thèmes, champs) | axonaut:gerez-vos-devis/personnaliser-ses-devis-et-factures-sur-axonaut.md | indetermine |
| personnel | progbat | personnel (fiche salarié/intérimaire, gestion RH) | progbat:le-menu-principal/chantiers-personnel/personnel.md | indetermine |
| photo juridique | batikko | photo juridique (horodatage, valeur probante) | batikko:guides/photos-juridiques.md | chantier-intervention |
| photos | sellsy | photos (produit / déclinaison) | sellsy:catalogue-produits-et-services/ajouter-des-photos-a-mes-produits-et-declinaisons.md | indetermine |
| photos certifiées | obat | photos certifiées (Certificall) | obat:`comment-prendre-des-photos-certifi-c3-a9es-avec-obat.md` | chantier-intervention |
| photos dans devis | obat | photos dans devis/facture | obat:`ins-c3-a9rer-des-photos-dans-un-devis-ou-une-facture.md` | devis |
| pied de devis | progbat | pied de devis (conditions de règlement, texte d'acceptation, gestion des déchets, totaux, mentions TVA) | progbat:le-menu-principal/devis-factures/devis/le-pied-du-devis.md | devis |
| pied de facture | progbat | pied de facture (conditions de règlement, totaux, remises, déductions, avancement) | progbat:le-menu-principal/devis-factures/factures/le-pied-de-la-facture.md | facturation |
| pied de page | sellsy | pied de page (document) | sellsy:documents-de-vente/modifier-le-pied-de-page-de-mes-documents.md | facturation |
| pipeline de prospection | sellsy | pipeline de prospection (rapport prévisionnel) | sellsy:crm-et-prospection/configurer-les-pipelines-de-prospection-pour-le-rapport-de-vente-previsionnel.md | indetermine |
| piratage | sellsy | piratage (réaction en cas d'incident) | sellsy:conseils-d-utilisation/les-bons-reflexes-a-adopter-en-cas-de-piratage.md | indetermine |
| pixel tracking | sellsy | pixel tracking (conformité RGPD, campagnes emailing) | sellsy:module-marketing/marketing-pixel-et-gestion-du-tracking-dans-les-campagnes-emailing.md | indetermine |
| pièce commerciale sans prix | extrabat | pièce commerciale sans prix (BL) | extrabat:creer-un-bon-de-livraison-sans-prix.md | indetermine |
| pièce jointe | costructor | pièce jointe (devis/facture, brouillon ou finalisé) | costructor:ventes/comment-ajouter-une-piece-jointe-sur-un-document-miurrx.md | indetermine |
| pièces commerciales | extrabat | pièces commerciales (regroupement BL en facture) | extrabat:transformer-plusieurs-bl-en-seule-facture.md | facturation |
| pièces jointes automatiques | vertuoza | pièces jointes automatiques (devis, CGV) lors de l'envoi d'une facture liée | vertuoza:faq-foires-aux-questions/est-il-obligatoire-d-envoyer-le-devis-avec-la-facture.md | facturation |
| plage de dates | extrabat | plage de dates (recherche pièces commerciales, tutoriel vidéo) | extrabat:tutorial-plage-de-date.md | indetermine |
| plan comptable paramétrable | obat | plan comptable paramétrable | obat:`le-plan-comptable-parametrable.md` | indetermine |
| plan de charge | obat | plan de charge (conflits d'attribution) | obat:`utilisation-du-plan-de-charge.md` | chantier-intervention |
| plan de relance | sellsy | plan de relance (paramétrage) | sellsy:documents-de-vente/etape-2-parametrer-un-plan-de-relance.md | facturation |
| planification cartographique des interventions | inter-fast | planification cartographique des interventions (géolocalisation, tournées) | inter-fast:inter-fast/operations/planifier-les-interventions-sur-une-carte.md | chantier-intervention |
| planification cartographique des maintenances | inter-fast | planification cartographique des maintenances | inter-fast:inter-fast/operations/planifier-les-maintenances-sur-une-carte.md | chantier-intervention |
| planification chantier | extrabat | planification chantier (planning, RDV rapide) | extrabat:plannification-plus-rapide.md | chantier-intervention |
| planification chantiers devisés | obat | planification chantiers devisés (calendrier/planning) | obat:`comment-ajouter-des-chantiers-devises-dans-le-calendrier/planning.md` | chantier-intervention |
| planification d'un événement | inter-fast | planification d'un événement (intervention, rendez-vous, absence) | inter-fast:inter-fast/operations/planifier-un-evenement-app-web.md | chantier-intervention |
| planification des ressources | vertuoza | planification des ressources (ouvriers, indépendants) dans le planning et impact sur la rentabilité | vertuoza:planning/planification-des-ressources-dans-le-planning.md | chantier-intervention |
| planification directe d'un rendez-vous d'intervention depuis le planning | openfire | planification directe d'un rendez-vous d'intervention depuis le planning | openfire:knowsystem/planification-directe-86.md | chantier-intervention |
| planification et annulation de rendez-vous réguliers | openfire | planification et annulation de rendez-vous réguliers/récurrents | openfire:knowsystem/gerer-les-rdv-reguliers-194.md | chantier-intervention |
| planification et modification d'interventions depuis le smartphone de l'ouvrier | vertuoza | planification et modification d'interventions depuis le smartphone de l'ouvrier | vertuoza:application-mobile/ouvrier-planifiez-et-editez-vos-interventions-depuis-votre-smartphone.md | chantier-intervention |
| planification et suivi des activités de relance liées aux opportunités | openfire | planification et suivi des activités de relance liées aux opportunités | openfire:knowsystem/planifier-et-suivre-une-activite-190.md | demande |
| planification lots | obat | planification lots/tâches (planning chantier) | obat:`planifier-vos-lots-et-vos-t-c3-a2ches-sur-votre-planning.md` | chantier-intervention |
| planification, statuts et gestion des interventions dans le planning | vertuoza | planification, statuts et gestion des interventions dans le planning | vertuoza:gestion-des-interventions/planification-et-gestion-des-interventions.md | chantier-intervention |
| plaquette de présentation commerciale | inter-fast | plaquette de présentation commerciale (création accompagnée, intégration aux devis) | inter-fast:inter-fast/debuter-avec-interfast/creer-votre-plaquette-de-presentation-commerciale.md | devis |
| plus-value | costructor | plus-value / moins-value (ligne de facture) | costructor:ventes/comment-ajouter-une-plus-value-moins-value-sur-une-facture-c1xd5u.md | facturation |
| poids et dimensions | sellsy | poids et dimensions (produit) | sellsy:catalogue-produits-et-services/gerer-les-poids-et-dimensions-de-mes-produits.md | indetermine |
| pointage d'un ouvrier possible indépendamment de l'existence d'un compte chantier | vertuoza | pointage d'un ouvrier possible indépendamment de l'existence d'un compte chantier | vertuoza:faq-foires-aux-questions/un-ouvrier-peut-il-etre-pointe-sans-compte-chantier.md | chantier-intervention |
| pointage du matériel | obat | pointage du matériel (suivi du temps) | obat:`le-pointage-du-materiel.md` | chantier-intervention |
| pointage mobile employés + validation admin | obat | pointage mobile employés + validation admin | obat:`multi-user-interface-pointage-mobile-pour-employes-validation-par-l-administrateur-et-chef-de-chantier-et-proprietaire.md` | chantier-intervention |
| politique de facturation anticipée de l'abonnement vertuoza | vertuoza | politique de facturation anticipée de l'abonnement Vertuoza | vertuoza:faq-foires-aux-questions/pourquoi-ma-facture-vertuoza-est-elle-envoyees-un-mois-a-l-avance.md | facturation |
| portail client obat | obat | portail client Obat (espace client en ligne) | obat:`le-portail-client-obat-un-outil-pour-simplifier-votre-quotidien-dartisan.md` | indetermine |
| portail comptable | axonaut | portail comptable (invitation, exports automatisés, intégrations logiciels) | axonaut:gerez-votre-comptabilite/le-portail-comptable-axonaut.md | indetermine |
| position fiscale | openfire | position fiscale (règles TVA/comptes automatiques) | openfire:configurer-openfire/creer-et-gerer-vos-positions-fiscales.md | indetermine |
| postes complémentaires | obat | postes complémentaires / factures de situation | obat:`ajouter-ou-modifier-des-postes-complementaires-sur-vos-factures-de-situation-dans-obat.md` | facturation |
| prestation | openfire | prestation (réservation en ligne, modèles d'intervention) | openfire:configurer-openfire/configuration-des-prestations-disponibles.md | chantier-intervention |
| primes et retenues de garantie | inter-fast | primes et retenues de garantie (ajout, suivi de versement) | inter-fast:inter-fast/finances/gerer-les-primes-et-les-retenues-de-garantie.md | devis |
| primes énergétiques | obat | primes énergétiques (devis) | obat:`comment-ins-c3-a9rer-vos-primes-c3-a9nerg-c3-a9tiques-dans-vos-devis.md` | devis |
| prise de rdv en ligne | openfire | prise de RDV en ligne (configuration complète) | openfire:knowsystem/configuration-265.md | chantier-intervention |
| prise de rendez-vous | axonaut | prise de rendez-vous (page de réservation, rappels, paiement en ligne) | axonaut:optimisez-gestion-commerciale/prise-de-rendez-vous.md | indetermine |
| prise de rendez-vous en ligne | openfire | prise de rendez-vous en ligne (paramétrage général) | openfire:configurer-openfire/configuration-generale.md | chantier-intervention |
| prise de rendez-vous en ligne par le client | openfire | prise de rendez-vous en ligne par le client (équipement, créneau, contrat) | openfire:knowsystem/prise-de-rdv-en-ligne-264.md | chantier-intervention |
| prix d'achat | extrabat | prix d'achat (mise à jour via devis/commande) | extrabat:mettre-a-jour-prix-dachat-via-devis-commande.md | devis |
| prix d'achat catalogue | extrabat | prix d'achat catalogue (mise à jour via widget) | extrabat:mise-jour-prix-dachat-catalogue.md | achat |
| procédure de connexion mobile | vertuoza | procédure de connexion mobile (numéro société, identifiants) | vertuoza:faq-foires-aux-questions/je-n-arrive-pas-a-me-connecter-sur-mobile.md | indetermine |
| procédure de finalisation d'un chantier après correction de tva par note de crédit | vertuoza | procédure de finalisation d'un chantier après correction de TVA par note de crédit | vertuoza:faq-foires-aux-questions/que-faire-si-j-ai-emis-une-note-de-credit-pour-corriger-la-tva-sur-une-facture-d-acompte-dans-un-chantier.md | facturation |
| procédure interservices | extrabat | procédure interservices (facturation/dépôt, sortie de stock) | extrabat:de-la-facturation-de-la-commande-jusqua-la-gestion-de-la-preparation-du-kit-sortie-du-stock.md | chantier-intervention |
| procédure pour clôturer un chantier arrêté | vertuoza | procédure pour clôturer un chantier arrêté (avenant négatif, note de crédit, facture finale) | vertuoza:faq-foires-aux-questions/comment-gerer-un-chantier-arrete-avec-un-avancement-negatif-et-l-impossibilite-de-generer-une-facture.md | chantier-intervention |
| procédure si le fournisseur | vertuoza | procédure si le fournisseur/client n'est pas enregistré sur PEPPOL | vertuoza:faq-foires-aux-questions/que-faire-si-le-fournisseur-ou-client-n-est-pas-encore-enregistre-sur-peppol.md | indetermine |
| produits précurseurs d'explosifs | extrabat | produits précurseurs d'explosifs (signalement réglementaire) | extrabat:nouvelle-fonctionnalite-les-produits-precurseurs-dexplosifs.md | indetermine |
| profil sous-traitant | inter-fast | profil sous-traitant (invitation, permissions) | inter-fast:inter-fast/equipe/inviter-et-gerer-un-profil-sous-traitant.md | indetermine |
| progbox | progbat | ProGBox (archivage de documents, stockage cloud intégré) | progbat:presentation-generale/progbox-archivage-de-documents.md | indetermine |
| projet | axonaut | projet (rentabilité, tâches, feuille de temps) | axonaut:gerez-rentabilite-projets/comment-creer-un-projet.md | indetermine |
| proposition commerciale dynamique | sellsy | proposition commerciale dynamique (Redactor) | sellsy:crm-et-prospection/creer-une-proposition-commerciale-dynamique-avec-redactor.md | devis |
| propriétaire de compte | sellsy | propriétaire de compte | sellsy:configuration-du-compte/definir-un-nouveau-proprietaire-du-compte-sellsy.md | indetermine |
| propriétés personnalisées | inter-fast | propriétés personnalisées (création, objets compatibles, export) | inter-fast:inter-fast/mon-entreprise/utiliser-les-proprietes-personnalisees.md | indetermine |
| protection contre la suppression de factures fournisseurs déjà exportées | vertuoza | protection contre la suppression de factures fournisseurs déjà exportées | vertuoza:faq-foires-aux-questions/pourquoi-je-ne-parviens-pas-a-supprimer-certaines-factures-fournisseur.md | achat |
| pré-comptabilité | sellsy | pré-comptabilité (accès expert-comptable) | sellsy:suivi-financier/experts-comptables-gerez-votre-pre-comptabilite-sur-sellsy.md | indetermine |
| préfixes dynamiques conditionnels dans les modèles de documents | vertuoza | préfixes dynamiques conditionnels dans les modèles de documents | vertuoza:parametres/comment-utiliser-des-prefixes-dynamiques-dans-vos-modeles.md | devis |
| préférences d'affichage et valeurs par défaut des champs dans les formulaires et lignes de documents | vertuoza | préférences d'affichage et valeurs par défaut des champs dans les formulaires et lignes de documents | vertuoza:parametres/preferences-d-affichage.md | devis |
| préférences exports comptables | sellsy | préférences exports comptables (paramétrage) | sellsy:suivi-financier/parametrer-les-preferences-d-exports-comptables.md | indetermine |
| préférences générales de stock | sellsy | préférences générales de stock | sellsy:module-stocks/definir-mes-preferences-generales-de-stocks.md | indetermine |
| préférences personnelles du profil | vertuoza | préférences personnelles du profil (copie d'email, affichage chantier, alertes) | vertuoza:parametres/preferences-du-profil.md | indetermine |
| prélèvement | axonaut | prélèvement (GoCardless/Compte Pro, mandats, devise, import) | axonaut:gerez-vos-factures/faire-payer-mes-factures-par-prelevement-via-gocardless.md | facturation |
| prélèvement automatique | sellsy | prélèvement automatique (GoCardless, abonnements) | sellsy:documents-de-vente/activer-le-prelevement-automatique-pour-le-reglement-des-factures-d-abonnements-gocardless.md | facturation |
| prélèvement bancaire gocardless | sellsy | prélèvement bancaire GoCardless (activation, mandat SEPA) | sellsy:paiements/activer-le-prelevement-bancaire-avec-gocardless.md | facturation |
| prélèvement client | axonaut | prélèvement client (mandat SEPA, Compte Pro) | axonaut:compte-pro-cartes/comment-activer-prelevement-client-compte-pro-axonaut.md | facturation |
| présentation de l'entreprise openfire | openfire | présentation de l'entreprise OpenFire | openfire:l-equipe-openfire.md | indetermine |
| présentation de l'écran de gestion des factures fournisseurs | vertuoza | présentation de l'écran de gestion des factures fournisseurs | vertuoza:finance/la-liste-des-factures-fournisseurs.md | achat |
| présentation de l'état des stocks | vertuoza | présentation de l'état des stocks (quantité, valeur, emplacement) à un instant donné | vertuoza:stock/etat-des-stocks.md | indetermine |
| présentation de la bibliothèque de prix | vertuoza | présentation de la bibliothèque de prix (catégories, ouvrages, composants) | vertuoza:bibliotheque-de-prix/bibliotheque-de-prix.md | devis |
| présentation de la navigation générale | openfire | présentation de la navigation générale (applications, menus, fil d'Ariane) | openfire:knowsystem/la-navigation-83.md | indetermine |
| présentation de vertuowork | vertuoza | présentation de VertuoWork (plateforme de mise en relation porteurs de projet / entreprises de construction) | vertuoza:vertuowork/decouvrir-vertuowork.md | indetermine |
| présentation des différents modes d'affichage | openfire | présentation des différents modes d'affichage (liste, kanban, carte, pivot) | openfire:knowsystem/les-vues-84.md | indetermine |
| présentation des menus comptables et du tableau de bord | openfire | présentation des menus comptables et du tableau de bord (ventes, achats, caisse, banque, à-nouveaux) | openfire:knowsystem/menu-de-la-comptabilite-et-tableau-de-bord-174.md | facturation |
| présentation des niveaux de personnalisation des modèles de documents | vertuoza | présentation des niveaux de personnalisation des modèles de documents (devis, avenants, factures) | vertuoza:parametres/modeles-de-documents.md | indetermine |
| présentation des tableaux de bord statistiques | vertuoza | présentation des tableaux de bord statistiques (KPI, devis, finances, CRM, commandes, interventions) | vertuoza:statistiques/statistiques.md | indetermine |
| présentation du planning gantt des chantiers | vertuoza | présentation du planning Gantt des chantiers (vue macro, planification stratégique) | vertuoza:gestion-de-chantier/la-vue-gantt.md | chantier-intervention |
| présentation du principe de standardisation peppol | vertuoza | présentation du principe de standardisation PEPPOL | vertuoza:faq-foires-aux-questions/comment-peppol-facilite-t-il-la-facturation-electronique-securisee-et-standardisee.md | facturation |
| présentation du service sms ovh et de son fonctionnement technique | openfire | présentation du service SMS OVH et de son fonctionnement technique | openfire:knowsystem/introduction-aux-sms-236.md | indetermine |
| présentation et personnalisation du tableau de bord | vertuoza | présentation et personnalisation du tableau de bord (widgets selon le pack) | vertuoza:tableau-de-bord/tableau-de-bord.md | indetermine |
| présentation générale | progbat | présentation générale / FAQ (licence, tarifs, conformité, hébergement, sécurité, migration) | progbat:index.md | indetermine |
| présentation générale de l'encodage des contacts | vertuoza | présentation générale de l'encodage des contacts (distinction contact/entreprise) | vertuoza:contacts/encodage-contacts.md | indetermine |
| présentation générale du module crm | openfire | présentation générale du module CRM (tableau de bord, pipeline, étapes) | openfire:knowsystem/introduction-au-crm-118.md | demande |
| présentation générale du module inventaire | openfire | présentation générale du module Inventaire (tableau de bord des stocks, gestion en double entrée, configuration multi-société) | openfire:knowsystem/generalites-et-tableau-de-bord-164.md | achat |
| présentation générale du processus d'achat | openfire | présentation générale du processus d'achat (du bon de livraison à la commande fournisseur) | openfire:knowsystem/introduction-aux-achats-sur-openfire-58.md | achat |
| présentation générale et accès à l'application dashboard | openfire | présentation générale et accès à l'application Dashboard (tableaux, widgets, domaines) | openfire:knowsystem/generalites-et-acces-255.md | indetermine |
| prévisionnel de trésorerie | axonaut | prévisionnel de trésorerie (module, scénarios, sources de calcul) | axonaut:etat-tresorerie-temps-reel/le-previsionnel-de-tresorerie.md | indetermine |
| prêt bancaire | axonaut | prêt bancaire (déclaration, rapprochement des mensualités) | axonaut:etat-tresorerie-temps-reel/gerer-mon-pret-bancaire-sur-axonaut.md | indetermine |
| publication d'une nouvelle annonce sur vertuowork | vertuoza | publication d'une nouvelle annonce sur VertuoWork | vertuoza:vertuowork/publier-une-nouvelle-annonce-sur-vertuowork.md | indetermine |
| pv de réception de chantier | inter-fast | PV de réception de chantier (rédaction, signature) | inter-fast:inter-fast/operations/remplir-un-pv-de-reception-de-chantier.md | chantier-intervention |
| pv de réception de fin de chantier | obat | PV de réception de fin de chantier | obat:`le-pv-de-reception-de-fin-de-chantier.md` | chantier-intervention |
| qr code | costructor | QR Code (document) | costructor:debuter-sur-costructor/comment-supprimer-le-qrcode-des-documents-10oxf0t.md | indetermine |
| qr code facture | axonaut | QR code facture (Suisse, obligation légale) | axonaut:gerez-vos-factures/qr-code-facture-suisse-comment-configurer-dans-axonaut.md | facturation |
| qr code sur devis | obat | QR code sur devis/factures | obat:`comment-ajouter-un-qr-code-sur-vos-documents-devis-et-factures.md` | indetermine |
| question complémentaire | extrabat | question complémentaire (page d'accueil) | extrabat:afficher-question-complementaire-page-daccueil.md | indetermine |
| questionnaire | openfire | questionnaire (modèles de certificats/rapports) | openfire:guides-videos/creer-un-questionnaire.md | indetermine |
| questions complémentaires | extrabat | questions complémentaires (création) | extrabat:veux-creer-questions-complementaires.md | indetermine |
| questions fréquentes | obat | questions fréquentes (page de catégorie) | obat:`questions-fr-c3-a9quentes.md` | indetermine |
| raccourci bureau | obat | raccourci bureau/écran d'accueil | obat:`comment-cr-c3-a9er-un-raccourcis-obat-sur-le-bureau/c3-a9cran-d-accueil-depuis-google-chrome.md` | indetermine |
| raccourci création document | obat | raccourci création document | obat:`comment-acc-c3-a9der-rapidement-c3-a0-un-nouveau-document-sur-obat.md` | indetermine |
| raccourci f3 | extrabat | raccourci F3 (fiche article) | extrabat:un-raccourci-f3-afin-de-consulter-rapidement-la-fiche-article.md | indetermine |
| raccourci recherche | extrabat | raccourci recherche (tâches planning par client) | extrabat:un-nouveau-raccourci-dans-le-moteur-de-recherche-le-nom-du-client.md | chantier-intervention |
| raccourcis clavier | extrabat | raccourcis clavier (recherche/impression) | extrabat:ctrl-f-et-ctrl-p.md | indetermine |
| raccourcis moteur de recherche | extrabat | raccourcis moteur de recherche (astérisques) | extrabat:sachez-vous-servir-des-etoiles.md | indetermine |
| rapport d'intervention app web | inter-fast | rapport d'intervention app web (remplissage, modification, traçabilité) | inter-fast:inter-fast/operations/remplir-modifier-un-rapport-d-intervention-app-web.md | chantier-intervention |
| rapports sellsy | sellsy | rapports Sellsy (présentation, panorama) | sellsy:rapports-et-pilotage/presentation-des-rapports-sellsy.md | indetermine |
| rapprochement bancaire automatique | sellsy | rapprochement bancaire automatique (paiements) | sellsy:paiements/rapprochement-automatique-depuis-un-virement-stancer-stripe-ou-gocardless.md | facturation |
| rapprochement bancaire des achats | obat | rapprochement bancaire des achats | obat:`rapprochement-bancaire-des-achats.md` | achat |
| rapprochement bancaire factures client | inter-fast | rapprochement bancaire factures client (procédure, cas multi-factures) | inter-fast:inter-fast/finances/rapprocher-des-factures-client-a-une-operation-bancaire.md | facturation |
| rapprochement bancaire factures fournisseur | inter-fast | rapprochement bancaire factures fournisseur (suggestions automatiques, multi-factures) | inter-fast:inter-fast/finances/rapprocher-des-factures-fournisseur-a-une-operation-bancaire.md | achat |
| recherche article | extrabat | recherche article (filtre « commence par ») | extrabat:rechercher-un-article.md | indetermine |
| recherche client | extrabat | recherche client (par téléphone) | extrabat:je-veux-retrouver-un-client-par-son-numero-de-telephone.md | indetermine |
| recherche dans bibliothèque personnalisée | obat | recherche dans bibliothèque personnalisée | obat:`comment-rechercher-des-c3-a9l-c3-a9ments-dans-votre-biblioth-c3-a8que-personnalis-c3-a9e.md` | devis |
| recommandation du produit batiprix compatible | vertuoza | recommandation du produit Batiprix compatible (BATIPRIX DATA) | vertuoza:faq-foires-aux-questions/quel-produit-batiprix-dois-je-acheter-pour-mon-entreprise.md | indetermine |
| recommandations pour un calcul de marge réaliste sur devis | vertuoza | recommandations pour un calcul de marge réaliste sur devis (éviter prix à 0€) | vertuoza:faq-foires-aux-questions/pourquoi-la-marge-peut-sembler-incorrecte-dans-un-devis.md | devis |
| reconnaissance ocr automatique du fournisseur sur facture | vertuoza | reconnaissance OCR automatique du fournisseur sur facture (conditions) | vertuoza:faq-foires-aux-questions/pourquoi-certaines-factures-ne-remplissent-pas-automatiquement-le-champ-fournisseur.md | achat |
| recouvrement de factures impayées | progbat | recouvrement de factures impayées (Caarl, amiable + judiciaire) | progbat:le-menu-principal/service-juridique/recouvrement-de-factures-impayees.md | facturation |
| recréation d'un ancien devis | obat | recréation d'un ancien devis (transition logicielle) | obat:`comment-recr-c3-a9er-un-devis-pr-c3-a9c-c3-a9demment-cr-c3-a9-c3-a9-sur-un-autre-logiciel-dans-obat.md` | devis |
| redimensionnement image | extrabat | redimensionnement image (Paint.NET) | extrabat:comment-formater-une-image-en-708-x-142-pixels.md | indetermine |
| redirection email | sellsy | redirection email (import factures) | sellsy:gestion-des-donnees/mettre-en-place-une-redirection-automatique-pour-l-import-de-factures.md | indetermine |
| redirection par défaut depuis une notification si accès module restreint | vertuoza | redirection par défaut depuis une notification si accès module restreint | vertuoza:faq-foires-aux-questions/pourquoi-lorsque-je-clique-sur-ma-notification-suis-je-redirige-vers-la-page-d-accueil-tableau-de-bord-au-lieu-de-la-module-indiquee.md | indetermine |
| redirection par défaut faute de droits d'accès au module gestion de chantier | vertuoza | redirection par défaut faute de droits d'accès au module Gestion de chantier | vertuoza:faq-foires-aux-questions/pourquoi-suis-je-redirige-vers-la-page-d-accueil-apres-avoir-clique-sur-gestion-de-chantier.md | chantier-intervention |
| refacturation d'heures | sellsy | refacturation d'heures | sellsy:crm-et-prospection/gestion-de-la-refacturation-d-heure.md | indetermine |
| regroupement des résultats de recherche et création de favoris | openfire | regroupement des résultats de recherche et création de favoris | openfire:knowsystem/grouper-les-resultats-et-creer-des-favoris-105.md | indetermine |
| relance automatique de devis | axonaut | relance automatique de devis (exclusion client, escalade huissier) | axonaut:gerez-vos-devis/comment-relancer-automatiquement-ses-devis.md | devis |
| relance client | extrabat | relance client (annulation) | extrabat:annuler-des-relances-clients.md | facturation |
| relance de devis | costructor | relance de devis | costructor:debuter-sur-costructor/comment-relancer-un-devis-en-attente-1vxtfm6.md | devis |
| relance de facture impayée | costructor | relance de facture impayée | costructor:debuter-sur-costructor/comment-relancer-une-facture-impayee-1wfw3kk.md | facturation |
| relance des factures impayées | openfire | relance des factures impayées (individuelle ou groupée) | openfire:knowsystem/relancer-mes-factures-139.md | facturation |
| relance et recouvrement de factures impayées | axonaut | relance et recouvrement de factures impayées (huissiers, litige) | axonaut:gerez-vos-factures/comment-relancer-mes-factures-impayees-automatiquement-avec-axonaut.md | facturation |
| relance facture client | extrabat | relance facture client | extrabat:effectuer-relance-facture-client.md | facturation |
| relance manuelle | sellsy | relance manuelle (client) | sellsy:documents-de-vente/la-relance-manuelle.md | facturation |
| relance manuelle en masse | sellsy | relance manuelle en masse (factures) | sellsy:documents-de-vente/la-relance-manuelle-en-masse.md | facturation |
| relance sms | extrabat | relance SMS (contrat d'entretien) | extrabat:activer-les-relances-par-sms-a-vos-clients-de-vos-contrats-dentretien.md | chantier-intervention |
| relances de factures | obat | relances de factures (recouvrement) | obat:`comment-parametrer-les-relances-des-factures.md` | facturation |
| relations clients | inter-fast | relations clients (liens propriétaire/locataire, payeur automatique maintenance) | inter-fast:inter-fast/outils/utiliser-les-relations-clients.md | facturation |
| reliquat | sellsy | reliquat (commande, livraison) | sellsy:documents-de-vente/gerer-les-reliquats.md | indetermine |
| remise ttc | sellsy | remise TTC (primes CEE / éco-primes) | sellsy:documents-de-vente/appliquer-une-remise-ttc-a-un-document-de-vente-prime-cee-eco-primes.md | facturation |
| remplacement attestation tva par mention | obat | remplacement attestation TVA par mention | obat:`remplacement-de-lattestation-tva-par-une-nouvelle-mention-sur-les-documents.md` | indetermine |
| rendez-vous d'intervention | openfire | rendez-vous d'intervention (portail client) | openfire:utiliser-openfire/suivre-et-gerer-ses-rendez-vous-d-intervention-sur-le-portail.md | chantier-intervention |
| renommage d'un catalogue d'articles | inter-fast | renommage d'un catalogue d'articles | inter-fast:inter-fast/outils/modifier-un-catalogue-d-articles.md | indetermine |
| rentabilité | costructor | rentabilité (marge + frais généraux) | costructor:debuter-sur-costructor/comment-parametrer-la-rentabilite-dma01r.md | indetermine |
| rentabilité canaux de publicité | extrabat | rentabilité canaux de publicité (statistiques) | extrabat:rentabilite-des-canaux-de-publicites.md | indetermine |
| rentabilité de chantier | costructor | rentabilité de chantier (prévue/réelle) | costructor:chantiers/comment-suivre-la-rentabilite-de-mon-chantier-zc3nkk.md | chantier-intervention |
| renvoi vers l'article détaillé du suivi de chantier pour chef d'équipe | vertuoza | renvoi vers l'article détaillé du suivi de chantier pour chef d'équipe | vertuoza:faq-foires-aux-questions/comment-fonctionne-le-suivi-de-chantier-pour-un-chef-d-equipe.md | chantier-intervention |
| replays de formation hebdomadaire | inter-fast | replays de formation hebdomadaire (archives thématiques) | inter-fast:inter-fast/debuter-avec-interfast/visionner-les-replays-de-formation-hebdo.md | indetermine |
| requête http | sellsy | requête HTTP (Make, OAuth) | sellsy:integrations-et-api/faire-une-requete-http-avec-make.md | indetermine |
| ressources d'accompagnement | sellsy | ressources d'accompagnement (facturation électronique) | sellsy:facturation-electronique/autres-ressources.md | indetermine |
| ressources d'aide | sellsy | ressources d'aide (Academy, blog, FAQ, webinars) | sellsy:conseils-d-utilisation/debuter-sur-sellsy-quelques-liens-utiles.md | indetermine |
| ressources humaines | axonaut | ressources humaines / congés / bulletin de salaire | axonaut:gerez-ressources-humaines/comment-ca-marche-ressources-humaines.md | indetermine |
| retard | extrabat | retard (notification client, Extrabat Today) | extrabat:je-veux-prevenir-de-mon-retard-via-lapplication-extrabat-today.md | chantier-intervention |
| retour article | extrabat | retour article (interface de caisse, avoir) | extrabat:faire-retour-article-linterface-de-caisse.md | achat |
| retour matériel | extrabat | retour matériel (garantie, SAV) | extrabat:faire-retour-materiel-garantie.md | chantier-intervention |
| retrait d'un chantier de l'affichage du planning | vertuoza | retrait d'un chantier de l'affichage du planning | vertuoza:planning/comment-retirer-un-chantier-du-planning.md | chantier-intervention |
| retrait d'une candidature déposée sur vertuowork | vertuoza | retrait d'une candidature déposée sur VertuoWork | vertuoza:vertuowork/retirer-une-candidature-sur-vertuowork.md | indetermine |
| retrouver un devis signé via l'historique du document | vertuoza | retrouver un devis signé via l'historique du document | vertuoza:faq-foires-aux-questions/comment-retrouver-un-devis-signe.md | devis |
| rib | obat | RIB (IBAN/BIC) sur documents | obat:`comment-ajouter-votre-rib-sur-vos-documents-obat.md` | indetermine |
| règlement libre | sellsy | règlement libre (décaissement, avant facturation) | sellsy:paiements/ajouter-un-reglement-decaissement-libre.md | indetermine |
| règlements de factures | obat | règlements de factures (encours/acquittée) | obat:`la-gestion-des-r-c3-a8glement-sur-obat-facture-acquitt-c3-a9e.md` | facturation |
| règles de comportement lors de la modification de champs de composants | vertuoza | règles de comportement lors de la modification de champs de composants (référence/description/fournisseur) | vertuoza:faq-foires-aux-questions/quelles-sont-les-regles-de-modification-des-composants-en-masse.md | devis |
| réalisation d'une intervention depuis l'application mobile | openfire | réalisation d'une intervention depuis l'application mobile (parc installé, photos, questionnaire, facturation, paiement, livraison, signature) | openfire:knowsystem/realiser-une-intervention-300.md | chantier-intervention |
| réalisation et clôture d'un inventaire de stock | vertuoza | réalisation et clôture d'un inventaire de stock (comptage, delta, import/export) | vertuoza:stock/inventaire.md | indetermine |
| réalisation et suivi des transferts internes de stock entre entrepôts | openfire | réalisation et suivi des transferts internes de stock entre entrepôts | openfire:knowsystem/transferts-internes-246.md | achat |
| réception de factures fournisseurs via peppol | vertuoza | réception de factures fournisseurs via PEPPOL (deux modes) | vertuoza:faq-foires-aux-questions/comment-recevoir-des-factures-fournisseurs-via-peppol.md | achat |
| réception de stock | extrabat | réception de stock (commande fournisseur) | extrabat:enregistrer-une-reception-de-stock.md | achat |
| réception des articles | openfire | réception des articles (bon de réception total ou partiel) | openfire:knowsystem/receptionner-mes-articles-178.md | achat |
| récolte avis clients sans chantier | obat | récolte avis clients sans chantier | obat:`recoltez-des-avis-clients-meme-sans-chantier-cree-dans-obat.md` | indetermine |
| récupération d'accès en cas de mot de passe oublié | vertuoza | récupération d'accès en cas de mot de passe oublié (suppression/recréation du compte) | vertuoza:parametres/mot-de-passe-oublie-que-faire.md | indetermine |
| récupération d'un mot de passe enregistré dans le navigateur | vertuoza | récupération d'un mot de passe enregistré dans le navigateur | vertuoza:demarrer/comment-retrouver-un-mot-de-passe-qui-est-enregistre-sur-votre-navigateur.md | indetermine |
| récupération des identifiants de connexion perdus | openfire | récupération des identifiants de connexion perdus | openfire:knowsystem/j-ai-perdu-mes-identifiants-de-connexion-199.md | indetermine |
| récurrence de facturation | extrabat | récurrence de facturation (commande divisée) | extrabat:creer-recurrence.md | facturation |
| référence produit | costructor | référence produit (affichage sur document) | costructor:ventes/comment-afficher-la-reference-dun-produit-sur-un-devis-ou-dune-facture-3mc3hp.md | indetermine |
| référentiel des codes d'erreur de synchronisation comptable et leurs solutions | vertuoza | référentiel des codes d'erreur de synchronisation comptable et leurs solutions | vertuoza:parametres/liste-des-codes-d-erreurs-de-synchronisation-comptable.md | facturation |
| régime de tva | sellsy | régime de TVA (e-reporting, fréquence) | sellsy:facturation-electronique/regime-de-tva-et-frequence-d-envoi-du-e-reporting.md | facturation |
| régime tva non assujetti | obat | régime TVA non assujetti (micro-entreprise) | obat:`comment-passer-son-compte-en-non-assujetti-c3-a0-la-tva.md` | indetermine |
| réglages module redactor | sellsy | réglages module Redactor | sellsy:crm-et-prospection/reglages-du-module-redactor.md | indetermine |
| réinitialisation du mot de passe | vertuoza | réinitialisation du mot de passe | vertuoza:demarrer/reinitialiser-le-mot-de-passe.md | indetermine |
| répartition des achats par catégorie | obat | répartition des achats par catégorie | obat:`comment-visualiser-la-repartition-des-achats-par-categorie-sur-obat.md` | achat |
| réservation de stock | sellsy | réservation de stock (devis / bon de commande) | sellsy:module-stocks/gerer-mes-reservations-de-stocks.md | indetermine |
| résiliation abonnement | obat | résiliation abonnement (autonomie) | obat:`resiliez-votre-abonnement-obat-en-toute-autonomie.md` | indetermine |
| résiliation d'abonnement | inter-fast | résiliation d'abonnement (demande, conditions) | inter-fast:inter-fast/mon-entreprise/arreter-mon-abonnement.md | facturation |
| résolution automatique des conflits de planning | obat | résolution automatique des conflits de planning | obat:`r-c3-a9solution-des-conflits-du-planning.md` | chantier-intervention |
| résolution de l'erreur de séquençage chronologique à la validation d'une facture | openfire | résolution de l'erreur de séquençage chronologique à la validation d'une facture | openfire:knowsystem/j-ai-un-message-d-erreur-a-la-validation-de-mes-factures-313.md | facturation |
| résolution de l'erreur smtp 535 gmail | openfire | résolution de l'erreur SMTP 535 Gmail (mot de passe d'application) | openfire:knowsystem/mails-en-erreurs-sur-gmail-smtp-535-282.md | indetermine |
| résolution erreurs envoi facture électronique | obat | résolution erreurs envoi facture électronique | obat:`resoudre-les-erreurs-denvoi-dune-facture-electronique.md` | facturation |
| réutilisation éléments d'anciens devis dans facture | obat | réutilisation éléments d'anciens devis dans facture | obat:`comment-ajouter-des-c3-a9l-c3-a9ments-de-fourniture-main-d-c5-93uvre-ouvrage-danciens-devis-depuis-l-c3-a9diteur-de-facture/devis.md` | facturation |
| rôles et permissions | obat | rôles et permissions (multi-user) | obat:`multi-user-les-differents-roles-et-acces.md` | indetermine |
| rôles utilisateurs | inter-fast | rôles utilisateurs (matrice de droits et tarification) | inter-fast:inter-fast/equipe/comprendre-les-roles-utilisateurs.md | indetermine |
| saisie des heures | progbat | saisie des heures (objectifs : coût salarial, rentabilité chantier) | progbat:le-menu-principal/chantiers-personnel/saisie-des-heures.md | chantier-intervention |
| saisie des heures par les salariés | progbat | saisie des heures par les salariés/chefs d'équipe (application mobile compagnons) | progbat:le-menu-principal/chantiers-personnel/saisie-des-heures/saisie-des-heures-par-les-salaries-et-chefs-dequipes.md | chantier-intervention |
| saisie des heures « au bureau » | progbat | saisie des heures « au bureau » (transfert depuis planning, saisie manuelle) | progbat:le-menu-principal/chantiers-personnel/saisie-des-heures/saisie-des-heures-au-bureau.md | chantier-intervention |
| saisie des temps | extrabat | saisie des temps (Extrabat Today) | extrabat:la-saisie-des-temps-sur-extrabat-today.md | chantier-intervention |
| saisie et validation d'un inventaire physique | openfire | saisie et validation d'un inventaire physique (ajustement de stock) | openfire:knowsystem/saisir-un-inventaire-57.md | achat |
| saison | extrabat | saison (couleur, planning) | extrabat:creer-nouvelle-saison.md | indetermine |
| saut de page sur devis | obat | saut de page sur devis | obat:`comment-ajouter-un-saut-de-page-sur-vos-devis/factures.md` | devis |
| sauvegarde | sellsy | sauvegarde / sécurité infrastructure | sellsy:conseils-d-utilisation/sauvegarde-continuite-de-service-et-prevention-des-intrusions.md | indetermine |
| scoring | sellsy | scoring (sociétés, widget tracking) | sellsy:integrations-et-api/mettre-en-place-un-scoring-sur-les-societes.md | indetermine |
| sections | obat | sections/sous-sections sur devis | obat:`comment-ajouter-une-section-c3-a0-votre-devis/facture.md` | devis |
| segmentation client | axonaut | segmentation client (CRM) | axonaut:creez-campagnes-marketing/boostez-vos-ventes-grace-au-module-segmentation-axonaut.md | indetermine |
| sellsy | sellsy | Sellsy (positionnement PA, réforme facturation électronique) | sellsy:facturation-electronique/positionnement-de-sellsy.md | indetermine |
| serveur mcp | costructor | serveur MCP / agent IA (intégration API) | costructor:debuter-sur-costructor/comment-connecter-costructor-a-votre-agent-ia-en-mcp-ey5k4v.md | indetermine |
| service juridique | progbat | service juridique (Caarl : chatbot IA, modèles de documents, avocats, recouvrement) | progbat:le-menu-principal/service-juridique.md | indetermine |
| signalisation visuelle | vertuoza | signalisation visuelle (rouge) des montants de commande de stock modifiés | vertuoza:faq-foires-aux-questions/pourquoi-certains-montants-de-commandes-de-stock-sont-ils-indiques-en-rouge.md | achat |
| signature pv de réception | obat | signature PV de réception (mobile, envoi mail) | obat:`signez-vos-pv-de-r-c3-a9ception-directement-sur-chantier-et-envoyez-les-par-mail-en-2-clics.md` | chantier-intervention |
| signature utilisateur | extrabat | signature utilisateur (image) | extrabat:mettre-une-image-dans-sa-signature-utilisateur.md | indetermine |
| signature électronique d'un contrat de maintenance | inter-fast | signature électronique d'un contrat de maintenance (via devis, pièce jointe) | inter-fast:inter-fast/operations/signer-un-contrat-de-maintenance.md | devis |
| signature électronique de devis | inter-fast | signature électronique de devis (procédure, documents annexes) | inter-fast:inter-fast/finances/signer-electroniquement-un-devis.md | devis |
| signature électronique du devis en ligne | vertuoza | signature électronique du devis en ligne | vertuoza:devis/signature-electronique-du-devis.md | devis |
| signature électronique en ligne d'un avenant | vertuoza | signature électronique en ligne d'un avenant | vertuoza:gestion-de-chantier/signature-electronique-de-l-avenant.md | chantier-intervention |
| signature électronique légale | sellsy | signature électronique légale (présentation, YouSign) | sellsy:documents-de-vente/presentation-de-la-signature-electronique-legale.md | indetermine |
| sms | openfire | SMS (configuration alertes, passerelle, modèles) | openfire:knowsystem/configuration-sms-237.md | indetermine |
| sociétés | sellsy | sociétés / contacts (import) | sellsy:gestion-des-donnees/importer-mes-donnees-societes-et-contacts.md | indetermine |
| sortie de stock | extrabat | sortie de stock (sous-commandes) | extrabat:comment-bloquer-les-sorties-de-stock-depuis-le-module-diviser-en-sous-commandes.md | chantier-intervention |
| sources d'opportunités | sellsy | sources d'opportunités (rapport) | sellsy:crm-et-prospection/rapport-des-sources-d-opportunites.md | indetermine |
| sous-total de section | costructor | sous-total de section (devis/facture) | costructor:ventes/comment-afficher-le-sous-total-des-sections-84iupw.md | indetermine |
| sous-totaux | extrabat | sous-totaux (pièces commerciales) | extrabat:totaux-dans-les-pieces-commerciales.md | indetermine |
| sous-traitant | progbat | sous-traitant (gestion identique à fournisseur) | progbat:le-menu-principal/contacts/sous-traitants.md | indetermine |
| souscription d'option | progbat | souscription d'option (boutique, paiement, renouvellement) | progbat:les-options/pourquoi-des-options/souscrire-une-option.md | indetermine |
| souscription à un abonnement | inter-fast | souscription à un abonnement (choix du plan, paiement) | inter-fast:inter-fast/mon-entreprise/souscrire-a-un-abonnement.md | achat |
| spécifications | sellsy | spécifications (produit) | sellsy:catalogue-produits-et-services/ajouter-des-specifications-a-mon-produit.md | indetermine |
| sso | sellsy | SSO (connexion) | sellsy:configuration-du-compte/connexion-sso.md | indetermine |
| statistiques origines de contact | extrabat | statistiques origines de contact (par année) | extrabat:statistiques-origines-par-annee.md | indetermine |
| statistiques rendez-vous | extrabat | statistiques rendez-vous | extrabat:connaitre-les-statistiques-des-rendez-vous.md | indetermine |
| statistiques ventes | extrabat | statistiques ventes (préparation commandes pré-saison) | extrabat:bien-preparer-ses-commandes-pre-saison.md | achat |
| statut | sellsy | statut (contact / société / particulier, transformation) | sellsy:repertoire/repertoire-modification-des-statuts-contacts-societes-et-particuliers.md | indetermine |
| statut client | extrabat | statut client/prospect (chantier) | extrabat:changer-le-statut-dun-clientprospecten-cours-de-chantier.md | chantier-intervention |
| statut d'envoi d'email | costructor | statut d'envoi d'email (devis/facture) | costructor:ventes/comment-consulter-le-statut-dun-email-envoye-9uearw.md | facturation |
| statut d'un client | inter-fast | statut d'un client (client/prospect/fournisseur) | inter-fast:inter-fast/outils/changer-le-statut-d-un-client.md | indetermine |
| statut de documents | sellsy | statut de documents (changement en masse) | sellsy:documents-de-vente/changer-les-statuts-de-documents-en-masse.md | facturation |
| statut eti | sellsy | statut ETI/GE (déclaration, facturation électronique) | sellsy:facturation-electronique/facturation-electronique-declaration-du-statut-eti-ge.md | indetermine |
| statut intervention | extrabat | statut intervention (SAV/Services, application Today) | extrabat:je-veux-changer-le-statut-de-mon-intervention-sav-ou-services-dans-extrabat-today.md | chantier-intervention |
| statut « à corriger » | sellsy | statut « à corriger » (transaction bancaire) | sellsy:suivi-financier/le-statut-des-transactions-a-corriger.md | indetermine |
| statuts | sellsy | statuts (opérations rapprochement bancaire, référence) | sellsy:suivi-financier/les-differents-statuts-des-operations-de-rapprochement-bancaire.md | indetermine |
| statuts de documents | sellsy | statuts de documents (cycle de vie) | sellsy:documents-de-vente/statuts-de-documents.md | facturation |
| statuts de prélèvement gocardless | sellsy | statuts de prélèvement GoCardless (référence) | sellsy:paiements/comprendre-les-statuts-d-un-prelevement-gocardless.md | facturation |
| statuts de suivi d'envoi des e-mails | vertuoza | statuts de suivi d'envoi des e-mails (succès, erreurs) | vertuoza:documents/les-statuts-d-envoi-d-e-mails.md | indetermine |
| stock | extrabat | stock (mise à jour via bon de réception) | extrabat:mettre-a-jour-mon-stock-sans-faire-dinventaire.md | achat |
| stock alerte | extrabat | stock alerte (article) | extrabat:comment-gerer-un-stock-alerte.md | achat |
| stock produit | sellsy | stock produit (vérification) | sellsy:module-stocks/verifier-le-stock-d-un-produit.md | indetermine |
| stock réservé | extrabat | stock réservé (détail par article) | extrabat:detail-du-stock-reserve.md | indetermine |
| stocks | inter-fast | stocks (consultation, mouvements, app mobile) | inter-fast:inter-fast/application-mobile/suivre-les-stocks-app-mobile.md | chantier-intervention |
| stocks et entrepôts | sellsy | stocks et entrepôts (configuration produit) | sellsy:module-stocks/gerer-les-stocks-et-entrepots-d-un-produit.md | indetermine |
| structure des données | inter-fast | structure des données (objets et relations InterFast) | inter-fast:inter-fast/debuter-avec-interfast/comprendre-la-structure-d-interfast.md | indetermine |
| suivi d'installation | vertuoza | suivi d'installation (numéro de série, date) et rappels de maintenance via interventions récurrentes | vertuoza:faq-foires-aux-questions/est-il-possible-de-lier-une-installation-a-un-numero-de-serie-et-a-une-date-d-installation-dans-vertuoza-afin-de-recevoir-un-rappel-de-maintenance-un-an-plus-tard.md | chantier-intervention |
| suivi de chantier par le chef d'équipe | vertuoza | suivi de chantier par le chef d'équipe (remarques, photos) depuis mobile | vertuoza:gestion-de-chantier/suivi-de-chantier-chef-d-equipe.md | chantier-intervention |
| suivi des déplacements techniciens | inter-fast | suivi des déplacements techniciens (paramétrage, cadre légal, app web) | inter-fast:inter-fast/equipe/suivre-les-deplacements-des-techniciens-app-web.md | chantier-intervention |
| suivi des exécutions des automatisations | inter-fast | suivi des exécutions des automatisations (journal, statuts, relance) | inter-fast:inter-fast/outils/suivre-les-executions-des-automatisations.md | indetermine |
| suivi des heures et rentabilité d'un chantier | inter-fast | suivi des heures et rentabilité d'un chantier (déboursé, marges) | inter-fast:inter-fast/operations/suivre-les-heures-et-la-rentabilite-d-un-chantier.md | chantier-intervention |
| suivi des heures et rentabilité d'une maintenance | inter-fast | suivi des heures et rentabilité d'une maintenance | inter-fast:inter-fast/operations/suivre-les-heures-et-la-rentabilite-d-une-maintenance.md | chantier-intervention |
| suivi du temps | obat | suivi du temps (par chantier/ressources) | obat:`le-suivi-du-temps-sur-obat.md` | chantier-intervention |
| suivi du temps simplifié | obat | suivi du temps simplifié (artisan seul) | obat:`suivi-du-temps-simplifie-pour-artisan-seul.md` | chantier-intervention |
| suivi et reporting des campagnes de publipostage | openfire | suivi et reporting des campagnes de publipostage | openfire:knowsystem/rapport-et-suivi-d-envoi-232.md | demande |
| suivi prospect | extrabat | suivi prospect | extrabat:ajouter-suivi-prospect.md | demande |
| support téléphonique | inter-fast | support téléphonique (canaux d'assistance, agents IA) | inter-fast:inter-fast/debuter-avec-interfast/comment-joindre-le-support-par-telephone.md | indetermine |
| suppression | obat | suppression/annulation facture selon statut | obat:`dans-quelles-conditions-puis-je-supprimer-ou-annuler-une-facture.md` | facturation |
| suppression d'un avenant accepté | vertuoza | suppression d'un avenant accepté (préalable : gestion des états d'avancement liés) | vertuoza:faq-foires-aux-questions/comment-puis-je-supprimer-un-avenant-accepte-qui-n-est-plus-d-actualite-et-ne-doit-pas-apparaitre-dans-la-facture-d-avancement.md | chantier-intervention |
| suppression d'un import de fichier | inter-fast | suppression d'un import de fichier (annulation, nettoyage base) | inter-fast:inter-fast/mon-entreprise/supprimer-un-import-de-fichier.md | indetermine |
| suppression d'un taux de tva conditionnée à son non-usage dans les documents | vertuoza | suppression d'un taux de TVA conditionnée à son non-usage dans les documents | vertuoza:faq-foires-aux-questions/pourquoi-ne-puis-je-pas-supprimer-un-taux-de-tva-dans-mes-parametres.md | indetermine |
| suppression d'un utilisateur | vertuoza | suppression d'un utilisateur (compte gestion/chantier), historique conservé | vertuoza:parametres/comment-supprimer-un-utilisateur.md | indetermine |
| suppression de la fonction « retour au statut précédent » sur devis accepté | vertuoza | suppression de la fonction « retour au statut précédent » sur devis accepté (alternative : suppression du chantier) | vertuoza:faq-foires-aux-questions/pourquoi-le-retour-au-statut-precedent-a-t-il-ete-retire-sur-un-devis-accepte-dans-vertuoza.md | devis |
| suppression définitive d'une annonce sur vertuowork | vertuoza | suppression définitive d'une annonce sur VertuoWork | vertuoza:vertuowork/supprimer-une-annonce-sur-vertuowork.md | indetermine |
| suppression et recréation d'une facture générée depuis un avancement | vertuoza | suppression et recréation d'une facture générée depuis un avancement | vertuoza:faq-foires-aux-questions/comment-gerer-une-facture-generee-a-partir-d-un-avancement-si-elle-ne-me-convient-pas.md | facturation |
| suppression éléments facture de situation | obat | suppression éléments facture de situation (FAQ) | obat:`peut-on-supprimer-des-c3-a9l-c3-a9ments-ciffr-c3-a9s-sur-une-facture-de-situation.md` | facturation |
| synchronisation | vertuoza | synchronisation/envoi des factures (clients, notes de crédit, fournisseurs) vers le logiciel comptable | vertuoza:parametres/envoyer-les-factures-vers-le-logiciel-comptable.md | facturation |
| synchronisation agenda google | axonaut | synchronisation agenda Google (bidirectionnelle, dépannage) | axonaut:optimisez-gestion-commerciale/synchroniser-son-agenda-google-avec-axonaut.md | indetermine |
| synchronisation agenda microsoft | axonaut | synchronisation agenda Microsoft (connexion, reconnexion après déconnexion) | axonaut:optimisez-gestion-commerciale/synchroniser-son-agenda-microsoft-avec-axonaut.md | indetermine |
| synchronisation automatique des statuts de paiement | vertuoza | synchronisation automatique des statuts de paiement (Ponto/Codabox), réconciliation manuelle si besoin | vertuoza:parametres/synchronisation-des-paiements.md | facturation |
| synchronisation bancaire ponto | inter-fast | synchronisation bancaire Ponto (dépannage, réautorisation DSP2) | inter-fast:inter-fast/finances/resoudre-les-problemes-de-synchronisation-bancaire-ponto.md | indetermine |
| synchronisation bancaire powens | inter-fast | synchronisation bancaire Powens (dépannage, réautorisation DSP2) | inter-fast:inter-fast/finances/resoudre-les-problemes-de-synchronisation-bancaire-powens.md | indetermine |
| synchronisation bidirectionnelle des factures d'achats entre bob et vertuoza | vertuoza | synchronisation bidirectionnelle des factures d'achats entre BOB et Vertuoza | vertuoza:faq-foires-aux-questions/peut-on-envoyer-les-achats-encodes-dans-bob-vers-vertuoza.md | achat |
| synchronisation calendrier apple | axonaut | synchronisation calendrier Apple (via Google Agenda, prérequis) | axonaut:optimisez-gestion-commerciale/synchroniser-son-calendrier-apple.md | indetermine |
| synchronisation comptable des factures de vente vers bob | vertuoza | synchronisation comptable des factures de vente vers BOB (écritures uniquement, pas le PDF) | vertuoza:faq-foires-aux-questions/les-factures-de-vente-generees-dans-vertuoza-peuvent-elles-etre-envoyees-dans-bob.md | facturation |
| synchronisation compte email | sellsy | synchronisation compte email | sellsy:conseils-d-utilisation/synchroniser-et-parametrer-votre-compte-email.md | indetermine |
| synchronisation dropbox | sellsy | synchronisation Dropbox | sellsy:gestion-des-donnees/fonctionnement-de-la-synchronisation-dropbox.md | indetermine |
| synchronisation google drive | sellsy | synchronisation Google Drive | sellsy:gestion-des-donnees/utiliser-le-module-google-drive.md | indetermine |
| synchronisation logiciel comptable | obat | synchronisation logiciel comptable (Chift/Pennylane) | obat:`chift-synchronisation-initiale-du-logiciel-comptable-a-pennylane.md` | indetermine |
| synchronisation outlook | extrabat | synchronisation Outlook (non supportée officiellement) | extrabat:synchronisation-avec-outlook.md | indetermine |
| synchronisation planning | progbat | synchronisation planning/agenda (Google/Outlook/iCal, compagnons) | progbat:le-menu-principal/chantiers-personnel/personnel/synchroniser-le-planning-chantier-avec-lagenda-des-compagnons.md | indetermine |
| synchronisation rendez-vous | extrabat | synchronisation rendez-vous (accès externe) | extrabat:avoir-acces-ses-rendez-vous-sans-avoir-acces-extrabat.md | indetermine |
| synthèse « reste à encaisser » et filtres factures | obat | synthèse « reste à encaisser » et filtres factures | obat:`le-bouton-de-synth-c3-a8se-total-reste-c3-a0-encaisser-et-les-diff-c3-a9rents-filtres-du-listing-de-vos-factures.md` | facturation |
| système de notifications des actions gestionnaires | vertuoza | système de notifications des actions gestionnaires (rapports, factures, signatures, paiements) | vertuoza:notifications/les-notifications.md | indetermine |
| système de vidéos d'aide | obat | système de vidéos d'aide (navigation) | obat:`un-nouveau-syst-c3-a8me-de-vid-c3-a9os-daide-encore-plus-simple-et-pratique-sur-obat.md` | indetermine |
| sécurité | sellsy | sécurité / confidentialité (mesures organisationnelles) | sellsy:conseils-d-utilisation/acces-confidentialite-et-mesures-organisationnelles.md | indetermine |
| sécurité des données | obat | sécurité des données (RGPD, hébergement) | obat:`la-s-c3-a9curit-c3-a9-de-vos-donn-c3-a9es.md` | indetermine |
| sécurité du compte | sellsy | sécurité du compte (bonnes pratiques) | sellsy:conseils-d-utilisation/securiser-votre-compte-sellsy.md | indetermine |
| sécurité et conformité | batikko | sécurité et conformité (2FA, RGPD, rôles) | batikko:guides/securite-conformite.md | indetermine |
| sélection d'options par le client | costructor | sélection d'options par le client (portail signature) | costructor:ventes/comment-selectionner-les-options-avant-la-signature-electronique-du-devis-u2qvt.md | devis |
| sélection multiple d'articles | extrabat | sélection multiple d'articles (pièce commerciale) | extrabat:selectionner-plusieurs-articles-dans-une-piece-commerciale.md | indetermine |
| séquence d'emails automatiques | sellsy | séquence d'emails automatiques (opportunité) | sellsy:crm-et-prospection/mettre-en-place-une-sequence-d-emails-automatiques-sur-une-opportunite.md | indetermine |
| tableau de suivi | progbat | tableau de suivi (board personnalisable, type CRM simplifié) | progbat:le-menu-principal/tableaux-de-suivi.md | indetermine |
| tableau des chantiers | inter-fast | tableau des chantiers (vues tableau/planning/synthèse) | inter-fast:inter-fast/operations/comprendre-le-tableau-des-chantiers.md | chantier-intervention |
| tableau des maintenances | inter-fast | tableau des maintenances (facturation automatique, planification des visites, visites prévisionnelles) | inter-fast:inter-fast/operations/comprendre-le-tableau-des-maintenances.md | chantier-intervention |
| tableaux de bord | inter-fast | tableaux de bord (activité, financier) | inter-fast:inter-fast/outils/utiliser-les-tableaux-de-bord.md | indetermine |
| tableaux de bord multi-user | obat | tableaux de bord multi-user (ouvriers/chef de chantier) | obat:`les-tableaux-de-bord-adaptes-a-chaque-role-ouvriers-et-chef-de-chantier.md` | chantier-intervention |
| tableaux du crm | inter-fast | tableaux du CRM (vues clients/prospects/fournisseurs/contacts/équipements, carte) | inter-fast:inter-fast/outils/comprendre-les-tableaux-du-crm.md | indetermine |
| tag analytique | costructor | tag analytique (catégorisation transverse) | costructor:debuter-sur-costructor/comment-utiliser-les-tags-analytiques-oa11ec.md | indetermine |
| tarifs articles | extrabat | tarifs articles (mise à jour export/import CSV) | extrabat:mettre-a-jour-ses-tarifs-darticles-via-la-fonction-dexport-import.md | indetermine |
| tarifs d'abonnement | sellsy | tarifs d'abonnement | sellsy:documents-de-vente/ajuster-mes-tarifs-d-abonnement.md | facturation |
| taux de marge par défaut | costructor | taux de marge par défaut | costructor:debuter-sur-costructor/comment-configurer-mon-taux-de-marge-par-defaut-wqw4cd.md | indetermine |
| taux de tva personnalisé | obat | taux de TVA personnalisé | obat:`comment-ajouter-un-taux-de-tva-personnalis-c3-a9-sur-obat.md` | indetermine |
| technicien | openfire | technicien (horaires, adresse, aptitude aux tâches) | openfire:configurer-openfire/techniciens-et-horaires.md | chantier-intervention |
| template marketing | axonaut | template marketing (éditeur d'apparence et de contenu) | axonaut:creez-campagnes-marketing/creer-un-template-marketing-dans-axonaut.md | indetermine |
| texte enregistré | progbat | texte enregistré (bibliothèque de textes réutilisables) | progbat:le-menu-principal/bibliotheque/textes.md | indetermine |
| textes fixes | sellsy | textes fixes (document, apparence) | sellsy:documents-de-vente/modifier-les-textes-fixes-des-documents.md | facturation |
| ticket de support technique | progbat | ticket de support technique | progbat:assistance/le-support-technique.md | indetermine |
| ticket sav | axonaut | ticket SAV (création, bon d'intervention, statistiques) | axonaut:centralisez-gestion-sav/comment-ca-marche-le-ticketing.md | chantier-intervention |
| tiers payant | extrabat | tiers payant (création) | extrabat:comment-creer-un-tiers-payant.md | facturation |
| timer | sellsy | timer (time tracking) | sellsy:crm-et-prospection/utiliser-les-timers.md | indetermine |
| tiroir-caisse | extrabat | tiroir-caisse (mécanisme d'ouverture) | extrabat:comment-souvre-le-tiroir-caisse.md | indetermine |
| titre facture | extrabat | titre facture (interface de caisse) | extrabat:saisir-titre-a-facture-via-linterface-de-caisse.md | facturation |
| tracking de consultation | sellsy | tracking de consultation (documents, lien public) | sellsy:documents-de-vente/tracking-de-consultation-des-documents.md | facturation |
| tracking prospects | sellsy | tracking prospects (widget, site web) | sellsy:integrations-et-api/suivre-l-activite-de-mes-prospects-sur-mon-site-web.md | indetermine |
| traduction automatique du navigateur | openfire | traduction automatique du navigateur (dépannage interface) | openfire:knowsystem/certains-termes-ou-noms-de-l-interface-sont-etranges-ou-traduits-209.md | indetermine |
| traduction des champs de documents | sellsy | traduction des champs de documents | sellsy:documents-de-vente/etape-3-parametrer-la-traduction-de-l-ensemble-des-champs-de-documents.md | indetermine |
| traitement des demandes d'amélioration produit | progbat | traitement des demandes d'amélioration produit | progbat:assistance/que-deviennent-mes-demandes-damelioration-du-logiciel-apres-en-avoir-fait-part-a-lequipe-support.md | indetermine |
| transaction | sellsy | transaction (montant différent facture, rapprochement) | sellsy:suivi-financier/traiter-un-montant-de-transaction-different-du-montant-de-la-facture.md | facturation |
| transaction bancaire | openfire | transaction bancaire (consultation, rapprochement) | openfire:utiliser-openfire/consultez-vos-transactions-bancaires.md | facturation |
| transactions bancaires | sellsy | transactions bancaires (transfert entre comptes) | sellsy:suivi-financier/transferer-des-transactions-entre-comptes-bancaires.md | indetermine |
| transfert de fournitures entre emplacements de stock | vertuoza | transfert de fournitures entre emplacements de stock (paramétrage et procédure) | vertuoza:stock/bon-de-transfert.md | indetermine |
| transfert de stock | extrabat | transfert de stock (entre dépôts) | extrabat:transfert-dun-article-dun-depot-a-un-autre.md | indetermine |
| transformation automatique d'emails en opportunités via ia | vertuoza | transformation automatique d'emails en opportunités via IA (alias email dédié) | vertuoza:faq-foires-aux-questions/comment-fonctionne-la-fonctionnalite-email-ai-dans-vertuoza-pour-transformer-les-emails-en-opportunites.md | demande |
| transformation devis en facture | axonaut | transformation devis en facture (2 méthodes, droits utilisateur) | axonaut:gerez-vos-devis/comment-transformer-un-devis-en-facture.md | devis |
| transformation devis → facture | obat | transformation devis → facture | obat:`comment-passer-vos-devis-en-factures-de-mani-c3-a8re-efficace-et-simple.md` | facturation |
| transformation planning → calendrier | obat | transformation planning → calendrier | obat:`transformer-votre-planning-en-calendrier.md` | chantier-intervention |
| transmission des achats par email | obat | transmission des achats par email | obat:`transmission-des-achats-par-e-mail.md` | achat |
| transmission écritures comptables de factures | obat | transmission écritures comptables de factures (Chift) | obat:`chift-transmettre-les-c3-a9critures-comptables-de-factures.md` | facturation |
| transporteur | sellsy | transporteur / tarif de transport | sellsy:module-stocks/transporteurs-et-tarifs-de-transport.md | indetermine |
| travailler avec syndics | inter-fast | travailler avec syndics/agences/donneurs d'ordre (relations, sites et emplacements GMAO) | inter-fast:inter-fast/outils/guide-complet-travailler-avec-des-proprietaires-syndics-agences-immobilieres-et-autres-donneurs-d-ordre.md | indetermine |
| traçabilité produit | axonaut | traçabilité produit (DLC/DDM, lots, garanties) | axonaut:gerez-stock-temps-reel/gestion-dlc-dluo-dlm-et-garanties.md | indetermine |
| tri et filtres | obat | tri et filtres (listings mobile/ordinateur) | obat:`tri-et-filtres-sur-les-listings-en-mode-mobile-et-ordinateur.md` | indetermine |
| trop-perçu | sellsy | trop-perçu (gestion, rapprochement bancaire) | sellsy:suivi-financier/gestion-d-un-trop-percu.md | facturation |
| tutos vidéo | progbat | tutos vidéo (support) | progbat:assistance/les-tutos-video.md | indetermine |
| tva 0 % sur factures | obat | TVA 0 % sur factures | obat:`ajoutez-facilement-une-tva-c3-a0-0-sur-vos-factures-de-situation-ou-finales.md` | facturation |
| tva collectée | obat | TVA collectée (visualisation) | obat:`comment-visualiser-votre-tva-collect-c3-a9e-sur-obat.md` | facturation |
| tva déductible | obat | TVA déductible (achats) | obat:`comment-visualiser-la-tva-deductible-payee-lors-des-achats.md` | achat |
| tva sur encaissement | progbat | TVA sur encaissement (déclaration, tableau de suivi) | progbat:le-menu-principal/comptabilite/tva-sur-encaissement.md | facturation |
| tva sur encaissements | sellsy | TVA sur encaissements (paramétrage) | sellsy:suivi-financier/mettre-en-place-la-tva-sur-les-encaissements.md | facturation |
| tva sur marge | axonaut | TVA sur marge (calcul, affichage, mention légale — cf. limites, contenu fiscal dense) | axonaut:gerez-vos-factures/comment-utiliser-la-tva-sur-marge-dans-axonaut.md | facturation |
| tva taux réduits | inter-fast | TVA taux réduits (mention légale automatique) | inter-fast:inter-fast/finances/mentionner-la-tva-a-taux-reduits.md | devis |
| type d'article | extrabat | type d'article (création) | extrabat:creer-type-darticle.md | indetermine |
| type de collecte de la tva | obat | type de collecte de la TVA (facturation/encaissement) | obat:`comment-s-c3-a9lectionner-le-type-de-collecte-de-la-tva-sur-votre-compte-obat.md` | facturation |
| type de livraison | obat | type de livraison / adresse de livraison | obat:`mise-en-place-du-type-de-livraison-et-de-ladresse-de-livraison-des-marchandises.md` | facturation |
| types de documents de vente | sellsy | types de documents de vente (activation) | sellsy:documents-de-vente/activer-les-bons-de-commande-bons-de-livraison-et-proforma.md | indetermine |
| types de facture | progbat | types de facture (acompte, travaux, avancement/situation, directe, avoir) | progbat:le-menu-principal/devis-factures/factures/les-differents-types-de-factures.md | facturation |
| types de lignes disponibles dans un devis | vertuoza | types de lignes disponibles dans un devis (titre, texte, poste libre, ouvrages, composants) | vertuoza:faq-foires-aux-questions/quels-types-de-lignes-peut-on-ajouter-dans-un-devis.md | devis |
| tâches | inter-fast | tâches (création, suivi, app mobile) | inter-fast:inter-fast/application-mobile/suivre-ses-taches-app-mobile.md | indetermine |
| tâches planning | extrabat | tâches planning (classement/ordre) | extrabat:classer-les-taches-planning.md | indetermine |
| téléchargement de l'application mobile sur android | vertuoza | téléchargement de l'application mobile sur Android | vertuoza:application-mobile/telecharger-l-application-sur-android.md | indetermine |
| téléchargement de l'application mobile sur ios | vertuoza | téléchargement de l'application mobile sur iOS | vertuoza:application-mobile/telecharger-l-application-sur-ios-apple.md | indetermine |
| unicité obligatoire de l'identifiant | vertuoza | unicité obligatoire de l'identifiant/email de compte gestion | vertuoza:faq-foires-aux-questions/pourquoi-ne-puis-je-pas-creer-un-identifiant-avec-une-adresse-e-mail-qui-existe-deja.md | indetermine |
| unité de quantité personnalisée | obat | unité de quantité personnalisée (bibliothèque) | obat:`comment-ajouter-une-nouvelle-unit-c3-a9-de-quantit-c3-a9-sur-obat.md` | indetermine |
| unités | sellsy | unités (catalogue) | sellsy:configuration-du-compte/parametrer-les-unites.md | indetermine |
| utilisateur additionnel | costructor | utilisateur additionnel / abonnement | costructor:abonnement/comment-ajouter-un-utilisateur-additionnel-j9e14d.md | indetermine |
| utilisateurs | progbat | utilisateurs (accès, licence vs connexions simultanées) | progbat:pour-bien-demarrer/parametrage/utilisateurs.md | indetermine |
| utilisation avancée des modèles, domaines et opérateurs python pour personnaliser les widgets | openfire | utilisation avancée des modèles, domaines et opérateurs Python pour personnaliser les Widgets | openfire:knowsystem/notion-de-modele-domaine-et-operateur-288.md | indetermine |
| utilisation de l'application mobile sur ordinateur | vertuoza | utilisation de l'application mobile sur ordinateur (émulateur, changement de plateforme) | vertuoza:faq-foires-aux-questions/comment-utiliser-l-application-mobile-vertuoza-sur-son-ordinateur.md | indetermine |
| utilisation de la messagerie interne | openfire | utilisation de la messagerie interne (canaux, messages directs, favoris, notifications) | openfire:knowsystem/l-application-discussion-158.md | indetermine |
| utilisation de la recherche simple | openfire | utilisation de la recherche simple | openfire:knowsystem/la-recherche-simple-18.md | indetermine |
| utilisation des filtres de recherche prédéfinis et personnalisés | openfire | utilisation des filtres de recherche prédéfinis et personnalisés | openfire:knowsystem/filtrer-vos-recherches-98.md | indetermine |
| utilisation des opérateurs de recherche avancée | openfire | utilisation des opérateurs de recherche avancée (ET/OU, caractères spéciaux) | openfire:knowsystem/la-recherche-avancee-104.md | indetermine |
| validation des commandes fournisseurs | inter-fast | validation des commandes fournisseurs (contrôle financier) | inter-fast:inter-fast/finances/activer-la-validation-des-commandes-fournisseurs.md | achat |
| valorisation des stocks | openfire | valorisation des stocks (méthodes de coût, inventaire à la date) | openfire:knowsystem/valoriser-les-stocks-191.md | achat |
| vente en caisse | extrabat | vente en caisse (Extrabat Piscine) | extrabat:comment-faire-une-vente-en-caisse.md | achat |
| ventilation du chiffre d'affaires | obat | ventilation du chiffre d'affaires | obat:`comment-analyser-la-ventilation-de-votre-chiffre-d-affaires-sur-obat.md` | indetermine |
| verrouillage de planification lié à la clôture du pointage | vertuoza | verrouillage de planification lié à la clôture du pointage | vertuoza:faq-foires-aux-questions/pourquoi-je-ne-peux-pas-planifier-un-ouvrier-a-une-certaine-date.md | chantier-intervention |
| verrouillage des quantités avancées sur une ligne de devis | vertuoza | verrouillage des quantités avancées sur une ligne de devis | vertuoza:faq-foires-aux-questions/pourquoi-certaines-lignes-de-mon-devis-ont-elles-des-quantites-grises-et-non-modifiables.md | devis |
| verrouillage rétroactif de planification après clôture du pointage | vertuoza | verrouillage rétroactif de planification après clôture du pointage | vertuoza:faq-foires-aux-questions/pourquoi-ne-puis-je-pas-ajouter-un-utilisateur-a-une-planification-passee-si-son-pointage-est-deja-cloture.md | chantier-intervention |
| verrouillage suppression achats électroniques | obat | verrouillage suppression achats électroniques | obat:`les-achats-re-c3-a7us-par-facturation-electronique-ne-peuvent-plus-etre-supprimes-dans-obat.md` | achat |
| vider cache navigateur | obat | vider cache navigateur (Chrome) | obat:`comment-vider-les-caches-sur-google-chrome.md` | indetermine |
| vidéo d'intervention | inter-fast | vidéo d'intervention (enregistrement, app mobile, abonnement Business) | inter-fast:inter-fast/application-mobile/enregistrer-une-video-d-intervention-app-mobile.md | chantier-intervention |
| virement bancaire | axonaut | virement bancaire (ponctuel, récurrent, bénéficiaires) | axonaut:compte-pro-cartes/comment-faire-un-virement-depuis-le-compte-pro-axonaut.md | indetermine |
| visibilité conditionnelle d'un contact dans le champ client | vertuoza | visibilité conditionnelle d'un contact dans le champ client (profil requis) | vertuoza:faq-foires-aux-questions/pourquoi-mon-client-n-apparait-elle-pas-dans-le-menu-deroulant-du-champ-client-lors-de-la-creation-ou-de-l-edition-de-ma-facture-devis.md | indetermine |
| visibilité conditionnelle d'une commande sous-traitant lors de la liaison à une facture fournisseur | vertuoza | visibilité conditionnelle d'une commande sous-traitant lors de la liaison à une facture fournisseur | vertuoza:faq-foires-aux-questions/pourquoi-ma-commande-n-apparait-elle-pas-lors-de-l-ajout-d-une-facture-fournisseur-sous-traitant.md | achat |
| visibilité conditionnelle du prix d'achat sur poste libre après passage en chantier | vertuoza | visibilité conditionnelle du prix d'achat sur poste libre après passage en chantier | vertuoza:faq-foires-aux-questions/pourquoi-je-ne-vois-plus-les-prix-d-achat-dans-un-poste-libre-d-un-devis-passe-en-chantier.md | chantier-intervention |
| visibilité des articles en stock selon l'attribution d'un emplacement | vertuoza | visibilité des articles en stock selon l'attribution d'un emplacement (stock réel vs théorique) | vertuoza:faq-foires-aux-questions/pourquoi-certains-articles-ne-sont-ils-pas-visibles-dans-l-etat-des-stocks-meme-s-ils-sont-physiquement-presents.md | achat |
| visibilité des commandes limitée aux gestionnaires du chantier concerné | vertuoza | visibilité des commandes limitée aux gestionnaires du chantier concerné | vertuoza:faq-foires-aux-questions/pourquoi-je-ne-vois-pas-les-commandes-a-envoyer-dans-mon-tableau-de-bord.md | achat |
| visite avant devis | inter-fast | visite avant devis (chiffrage terrain, photos, rapport) | inter-fast:inter-fast/operations/documenter-les-visites-avant-devis.md | devis |
| visualisation des clients sur une carte | inter-fast | visualisation des clients sur une carte (CRM, géolocalisation) | inter-fast:inter-fast/outils/visualiser-les-clients-sur-une-carte.md | indetermine |
| vue d'ensemble de la synchronisation comptable | vertuoza | vue d'ensemble de la synchronisation comptable (bénéfices, champs transférés, compatibilité logiciels) | vertuoza:parametres/synchronisation-comptable-vue-d-ensemble.md | facturation |
| vue kanban des devis | obat | vue Kanban des devis | obat:`vue-kanban-des-devis-pilotez-votre-activite-commerciale-dun-coup-d-c5-93il.md` | devis |
| vues calendrier | obat | vues calendrier (jour/semaine/mois) | obat:`visualiser-votre-calendrier-en-vue-journali-c3-a8re/hebdomadaire/mensuelle.md` | chantier-intervention |
| vérification d'identité | obat | vérification d'identité (facturation électronique) | obat:`facturation-electronique-tout-savoir-sur-la-verification-didentite.md` | facturation |
| vérification du format et de l'inscription d'un id peppol | vertuoza | vérification du format et de l'inscription d'un ID PEPPOL | vertuoza:faq-foires-aux-questions/comment-verifier-rapidement-son-id-peppol-ou-celui-d-un-fournisseur.md | indetermine |
| vérification par code email | obat | vérification par code email (sécurité bancaire) | obat:`protegez-vos-donnees-bancaires-avec-obat-la-verification-par-code-email.md` | indetermine |
| webhook | sellsy | webhook (Slack/HTTP) | sellsy:integrations-et-api/webhooks.md | indetermine |
| widget météo | extrabat | widget météo (page d'accueil) | extrabat:le-widjet-meteo-refait-son-apparition-pour-noel.md | indetermine |
| widget nouveautés | obat | widget nouveautés (actualités produit) | obat:`comment-consulter-le-widget-nouveaut-c3-a9s.md` | indetermine |
| za, assistant ia d'obat | obat | Za, assistant IA d'Obat | obat:`za-lassistant-ia-dobat.md` | indetermine |
| « cerveau numérique » | inter-fast | « cerveau numérique » (argumentaire centralisation des données, témoignages clients) | inter-fast:inter-fast/debuter-avec-interfast/construire-le-cerveau-numerique-de-votre-entreprise.md | indetermine |
| écart entre statistiques et liste des devis | vertuoza | écart entre statistiques et liste des devis (critères de date différents) | vertuoza:faq-foires-aux-questions/pourquoi-les-montants-affiches-dans-les-statistiques-different-de-ceux-visibles-en-bas-de-page-des-devis.md | devis |
| écarts d'arrondi après remise globale | vertuoza | écarts d'arrondi après remise globale (contournement pour un total rond) | vertuoza:faq-foires-aux-questions/pourquoi-le-total-de-mon-devis-n-est-pas-parfaitement-rond-apres-une-remise-globale.md | devis |
| écarts de prix entre détail d'ouvrage et devis | vertuoza | écarts de prix entre détail d'ouvrage et devis (méthodes d'arrondi différentes) | vertuoza:faq-foires-aux-questions/pourquoi-le-prix-dans-le-detail-d-ouvrages-peut-il-differer-du-prix-dans-le-devis.md | devis |
| écarts entre devis et facturation liés au mode d'application des remises | vertuoza | écarts entre devis et facturation liés au mode d'application des remises | vertuoza:faq-foires-aux-questions/pourquoi-y-a-t-il-des-differences-dans-les-montants-factures-par-rapport-aux-devis-initiaux.md | facturation |
| échéances clients | progbat | échéances clients (factures impayées, relances niveau 1-3) | progbat:le-menu-principal/devis-factures/echeances-clients.md | facturation |
| échéances multiples | sellsy | échéances multiples (règlement, document de vente) | sellsy:paiements/utiliser-les-reglements-avec-echeances-multiples-sur-les-documents-de-vente.md | facturation |
| éco-participation | axonaut | éco-participation / taxe DEEE (configuration produit, décomposition facture) | axonaut:gerez-vos-factures/comment-gerer-leco-participation-dans-axonaut.md | facturation |
| écotaxe | sellsy | écotaxe (produit) | sellsy:catalogue-produits-et-services/activer-et-utiliser-l-ecotaxe.md | indetermine |
| écrans vides enrichis | obat | écrans vides enrichis (onboarding UI) | obat:`decouvrez-les-ecrans-vides-enrichis-dans-obat-un-vrai-coup-de-pouce-pour-demarrer-sereinement.md` | indetermine |
| écritures de trésorerie | sellsy | écritures de trésorerie (comptabilité) | sellsy:suivi-financier/enregistrement-des-ecritures-de-tresorerie-en-comptabilite.md | indetermine |
| éditeur de devis | obat | éditeur de devis (renvoi) | obat:`comment-c3-a9diter-et-mettre-en-forme-un-devis-sur-obat.md` | devis |
| élément de bibliothèque | costructor | élément de bibliothèque (produit, dossier, prix/marge) | costructor:ventes/comment-creer-des-elements-et-les-organiser-dans-la-bibliotheque-1sh3nn2.md | indetermine |
| équipements | inter-fast | équipements (fiches, historique, ajout, app mobile) | inter-fast:inter-fast/application-mobile/gerer-les-equipements-app-mobile.md | chantier-intervention |
| équipements niveau 1 | inter-fast | équipements niveau 1 (saisie, import CSV, association intervention) | inter-fast:inter-fast/outils/ajouter-et-consigner-des-equipements-niveau-1.md | indetermine |
| équipements niveau 2 | inter-fast | équipements niveau 2 (types, propriétés personnalisées, IA plaque signalétique, pré-remplissage) | inter-fast:inter-fast/outils/gerer-les-equipements-niveau-2.md | chantier-intervention |
| état de compte client | costructor | état de compte client (récapitulatif factures/paiements) | costructor:ventes/comment-creer-un-etat-de-compte-client-1yzp3f5.md | facturation |
| état de stock | axonaut | état de stock (table, alerte de seuil, catalogue vs stock) | axonaut:gerez-stock-temps-reel/controler-letat-de-mon-stock-dans-axonaut.md | indetermine |
| évènement | inter-fast | évènement (intervention ou rendez-vous, planification app mobile) | inter-fast:inter-fast/application-mobile/planifier-un-evenement-app-mobile.md | chantier-intervention |
| événement calendrier | obat | événement calendrier | obat:`cr-c3-a9er-un-c3-a9v-c3-a9nement-sur-un-calendrier.md` | chantier-intervention |
| événement de facturation électronique | openfire | événement de facturation électronique (statuts, cycle de vie) | openfire:utiliser-openfire/gerer-vos-evenements-de-facturation-electronique.md | facturation |
| événement vs intervention | openfire | événement vs intervention (comparatif fonctionnel) | openfire:utiliser-openfire/evenement-ou-intervention.md | chantier-intervention |
| événements récurrents | obat | événements récurrents (calendrier) | obat:`creez-des-evenements-recurrents-dans-votre-calendrier-obat.md` | chantier-intervention |

## 4. Répartition par concurrent

Nombre de lignes, de valeurs exactes distinctes et de racines distinctes par
concurrent, toutes productions confondues (une production par corpus + la part
du pilote + la part du micro-lot H3 rattachées à leur concurrent réel).

| Concurrent | Lignes LIGHT | Valeurs exactes distinctes | Racines distinctes |
|---|---:|---:|---:|
| sellsy | 462 | 460 | 310 |
| vertuoza | 433 | 429 | 426 |
| extrabat | 347 | 290 | 215 |
| openfire | 340 | 337 | 294 |
| obat | 274 | 273 | 255 |
| inter-fast | 221 | 221 | 205 |
| progbat | 190 | 169 | 145 |
| axonaut | 127 | 127 | 113 |
| costructor | 102 | 102 | 99 |
| batikko | 14 | 14 | 12 |
| **Total** | **2510** | **2417** | **1864** |

**Lecture.** Sellsy (462) et Vertuoza (433) portent, à eux deux, environ 36 %
du volume total de lignes LIGHT — leurs productions sont aussi les deux plus
volumineuses du corpus (454 et 431 documents respectivement, plus les
compléments pilote/H3). Batikko (14 lignes) est de très loin le corpus le plus
réduit, cohérent avec la taille de son centre d'aide observée dans
`corpus_index.json`. Le ratio racines/lignes varie fortement d'un concurrent à
l'autre (ex. Vertuoza : 426 racines pour 433 lignes, vocabulaire très peu
répété ; Sellsy : 310 racines pour 462 lignes, vocabulaire un peu plus
répétitif — cohérent avec ses familles de documents « fortement répétitifs »
signalées dans sa propre production). Ce contraste est descriptif : il ne dit
rien de la richesse fonctionnelle réelle des produits, seulement de la
diversité lexicale de leur documentation telle que codée par LIGHT.

## 5. Regroupements sémantiques candidats

Regroupements **candidats**, jamais des fusions actées. Chaque regroupement
associe des racines distinctes observées dans l'inventaire (§3), avec un
niveau de confiance et les concurrents concernés. Aucun de ces regroupements
ne doit être lu comme une décision de vocabulaire SUPORDO.

### Famille « facture »
Racines : `facture`, `factures`, `facture d'acompte`, `facture d'achat`,
`facture d'abonnement`, `facture proforma`, `facture de situation`,
`facture d'avancement`, `liste factures`, `factures fournisseurs`,
`règlement facture`.
Justification : `facture`/`factures` est une variation singulier/pluriel pure
→ **SYNONYME_PROBABLE**. Les sous-types (acompte, proforma, situation,
avancement, abonnement) désignent des objets ou des statuts de facture
distincts du point de vue métier, pas de simples reformulations →
**CONCEPT_PROCHE_MAIS_DISTINCT**. Concurrents : les 10 (racine `facture` seule
déjà observée chez 7 : sellsy, openfire, progbat, inter-fast, extrabat,
axonaut, costructor).

### Famille « devis »
Racines : `devis`, `ligne de devis`, `variantes de devis`, `import de devis`,
`relance devis`, `recherche devis`, `assistant devis vocal`.
Justification : `devis` est l'objet parent ; `ligne de devis` en est un
sous-composant ; `variantes de devis` un mécanisme de version/déclinaison ;
les autres racines sont des opérations sur l'objet, pas des synonymes →
**CONCEPT_PROCHE_MAIS_DISTINCT** pour l'ensemble. Concurrents : progbat,
inter-fast, extrabat, openfire, sellsy, axonaut, obat (racine `devis` seule).

### Famille « client / contact / prospect »
Racines : `client`, `contact`, `prospect`, `fiche client`, `fiche contact`,
`fiche prospect`, `portail client`, `espace client`.
Justification : au moins un concurrent (Extrabat) utilise lui-même
`client/prospect` comme valeur exacte unique dans un même document
(`extrabat:supprimer-prospect-client.md`), signe que la frontière n'est pas
stable même à l'intérieur d'une seule documentation → **AMBIGU**. Voir §7 pour
le détail. Concurrents : extrabat, progbat, batikko, costructor, openfire,
sellsy, inter-fast, axonaut.

### Famille « chantier / affaire »
Racines : `chantier`, `affaire`, `bordereau de chantier`, `suivi de
chantier`.
Justification : `affaire` (Extrabat uniquement, 3 occurrences : « bonnes
pratiques, gestion », « création, association pièces commerciales »,
« synthèse rentabilité ») recouvre un périmètre qui, à la lecture des valeurs
exactes seules, chevauche fortement ce que `chantier` désigne chez
InterFast/ProGBat/Obat/Batikko → **CONCEPT_PROCHE_MAIS_DISTINCT à AMBIGU**,
non tranchable depuis LIGHT seul. Voir §7. Concurrents : extrabat (affaire),
inter-fast, progbat, obat, batikko (chantier).

### Famille « intervention / SAV »
Racines : `intervention`, `demande d'intervention`, `rapport d'intervention`,
`sav`.
Justification : `sav` désigne tantôt un dossier/objet (Extrabat : « SAV
[enregistrement] », « SAV [dossier complet, cycle commercial/logistique/
technique] »), tantôt semble recouper une intervention de dépannage — la
distinction objet vs type d'intervention n'est pas tranchable ici →
**CONCEPT_PROCHE_MAIS_DISTINCT à AMBIGU**. Voir §7. Concurrents : extrabat,
openfire, inter-fast, vertuoza.

### Famille « paiement / règlement »
Racines : `paiement`, `règlement`, `règlements`, `moyen de paiement`,
`conditions de paiement`, `mode de règlement`, `prélèvement sepa`.
Justification : `paiement` et `règlement` recouvrent probablement la même
action dans plusieurs contextes → **SYNONYME_PROBABLE** partiel ; `moyen de
paiement` et `conditions de paiement` sont des objets de configuration
distincts de l'action elle-même → **CONCEPT_PROCHE_MAIS_DISTINCT** pour
l'ensemble de la famille. Concurrents : sellsy, openfire, vertuoza, extrabat,
inter-fast, axonaut, obat, costructor, progbat (9 des 10).

### Famille « avoir / note de crédit / remboursement »
Racines : `avoir`, `remboursement client` (racine « création d'une note de
crédit » regroupée par sens, pas par racine mécanique — la racine littérale
diffère).
Justification : « avoir » (terminologie comptable française classique, ex.
Axonaut, Extrabat, OpenFire, Sellsy) et « note de crédit » (terminologie
employée par Vertuoza : `création d'une note de crédit`,
`comportement de statut d'une note de crédit`) désignent très probablement le
même objet métier sous deux étiquettes différentes → **SYNONYME_PROBABLE**.
`remboursement client` est une opération liée mais distincte (mouvement de
trésorerie effectif vs émission d'un avoir comptable) →
**CONCEPT_PROCHE_MAIS_DISTINCT**. Concurrents : vertuoza, inter-fast,
extrabat, openfire, sellsy, obat, axonaut, costructor.

### Famille « commande »
Racines : `commande fournisseur`, `commande client`, `bon de commande`,
`connecteur d'achat`.
Justification : `bon de commande` est le terme documentaire générique, décliné
en sens client/fournisseur selon le flux → **CONCEPT_PROCHE_MAIS_DISTINCT**.
Concurrents : openfire, extrabat, inter-fast, axonaut, sellsy, vertuoza,
costructor.

### Famille « comptabilité »
Racines : `comptabilité`, `rapprochement bancaire`, `plan comptable`,
`écritures comptables`, `export comptable`, `code comptable`, `exercice
comptable`, `journal d'achats`, `débours`, `décompte général`.
Justification : plusieurs facettes distinctes d'un même domaine comptable, pas
des synonymes entre elles → **CONCEPT_PROCHE_MAIS_DISTINCT**. Concurrents :
sellsy, openfire, inter-fast, obat, extrabat, costructor, axonaut, progbat (8
des 10).

### Famille « signature »
Racines : `signature électronique`, `signatures électroniques`, `signature
email`.
Justification : `signature électronique`/`signatures électroniques` est une
variation singulier/pluriel non fusionnée par la racine mécanique (le pluriel
change le mot entier, pas seulement une terminaison après le point de
troncature) → **SYNONYME_PROBABLE**. `signature email` (signature de
courriel) est un objet distinct de la signature légale de document — ne pas
fusionner → **CONCEPT_PROCHE_MAIS_DISTINCT/AMBIGU** si le terme seul
`signature` était utilisé sans qualification. Concurrents : extrabat, sellsy,
vertuoza, openfire, axonaut, progbat, obat, inter-fast (8 des 10).

### Famille « rapport / tableau de bord / pilotage »
Racines : `rapport`, `tableau de bord`, `rapport crm`, `rapport
d'intervention`, `pilotage`, `balance âgée`.
Justification : `rapport` (Sellsy, documents unitaires par thème métier),
`tableau de bord` (vue agrégée, Sellsy/ProGBat/Extrabat) et `pilotage`
(terme générique employé par Costructor/Obat) ne sont pas interchangeables
a priori → **CONCEPT_PROCHE_MAIS_DISTINCT**. Concurrents : sellsy, extrabat,
openfire, inter-fast, vertuoza, progbat, costructor, obat (8 des 10) — mais
fortement concentré chez Sellsy (62/86 documents du domaine, cf. §6).

### Famille « conformité fiscale/légale »
Racines : `facturation électronique`, `taux de tva`, `tva`, `taxe`, `cgv`,
`conditions générales de vente`, `mentions légales`, `rgpd`, `cerfa 15497`.
Justification : racines thématiquement proches (conformité) mais désignant
des objets distincts — `facturation électronique` est un flux/plateforme
réglementaire, `tva`/`taxe` un calcul fiscal, `cgv`/`mentions légales`/`rgpd`
des documents juridiques → **CONCEPT_PROCHE_MAIS_DISTINCT**, à ne pas
fusionner en un objet unique malgré la proximité thématique. Concurrents :
les 10.

### Famille « application mobile »
Racines : `application mobile`, `application extrabat today v3.5`,
`application extradoc`.
Justification : `application mobile` est le terme générique ; les deux autres
sont des noms de produits internes Extrabat (déclinaisons commerciales
nommées) → **CONCEPT_PROCHE_MAIS_DISTINCT** (nommage propriétaire, pas une
simple reformulation). Concurrents : openfire, extrabat, vertuoza, costructor,
inter-fast, obat, progbat, sellsy (8 des 10).

### Famille « opportunité / pipeline »
Racines : `opportunité`, `opportunités`, `pipeline`.
Justification : singulier/pluriel → **SYNONYME_PROBABLE** entre les deux
premières. `pipeline` (terme anglicisé, Sellsy) peut désigner le processus
plutôt que l'objet lui-même → **CONCEPT_PROCHE_MAIS_DISTINCT**. Concurrents :
sellsy, openfire, vertuoza — 3 concurrents seulement, tous éditeurs à
composante CRM affirmée.

### Famille « utilisateur / compte / profil »
Racines : `utilisateur`, `compte utilisateur`, `profil utilisateur`,
`identifiants de connexion`.
Justification : `utilisateur` désigne la personne/l'entité, `compte
utilisateur` et `profil utilisateur` des objets système associés,
`identifiants de connexion` un sous-composant de sécurité →
**CONCEPT_PROCHE_MAIS_DISTINCT**. Concurrents : vertuoza, extrabat, openfire,
obat, inter-fast, progbat, axonaut, costructor (8 des 10).

### Famille « automatisation / IA »
Racines : `automatisation`, `ia`, `assistant devis vocal`.
Justification : `automatisation` (règles conditionnelles déclenchées par
événement, Sellsy) est un mécanisme différent de `ia` (assistant
vocal/génératif, Sellsy/Obat) même si les deux relèvent d'un axe transverse
« automatisation avancée » → **CONCEPT_PROCHE_MAIS_DISTINCT**. Concurrents :
sellsy, inter-fast, obat, axonaut, openfire.

## 6. Domaines fonctionnels candidats

Domaines construits à partir des racines observées (§3), par recherche de
mots-clés dans l'ensemble des 1864 racines (pas seulement le top). Liste de
départ = celle suggérée par la mission ; domaines ajoutés en fin de tableau
car réellement observés sans figurer dans cette liste de départ. « Documents »
compte les lignes LIGHT dont la racine correspond au domaine — une même ligne
peut être comptée dans plusieurs domaines si sa racine est ambiguë entre deux
thèmes (ex. `synchronisation agenda` compte à la fois dans « planning » et
dans « intégrations/synchronisations »). Ce chevauchement est volontaire :
les domaines candidats ne sont pas une partition, seulement des pistes de
lecture.

| Domaine candidat | Documents | Racines | Concurrents | Racines principales (extrait) |
|---|---:|---:|---:|---|
| facture/facturation | 193 | 146 | 10 | facture, facture d'acompte, facture proforma, ca restant à facturer, facture d'abonnement, facture d'achat, factures, calcul du montant d'une commande sous-traitant liée à une facture fournisseur |
| devis | 144 | 115 | 10 | devis, assistant devis vocal, import de devis, ligne de devis, variantes de devis, recherche devis, relance devis, activation de l'option enveloppe à fenêtre sur un modèle de devis 2 colonnes |
| intégrations/synchronisations | 120 | 94 | 10 | synchronisation agenda, synchronisation email, intégration comptable, fichier csv, intégration install bois, connecteur d'achat, connecteur wizville, connecteurs d'achat |
| client/contact | 118 | 84 | 10 | fiche client, client, contact, contacts, annuaire des sociétés, code client, espace client, fiche contact |
| rapports/pilotage/tableaux de bord | 86 | 20 | 8 | rapport, tableau de bord, rapport crm, rapport d'intervention, rapports d'intervention et signatures, balance âgée, pilotage, absence de liaison automatique des rapports d'intervention aux factures groupées |
| affaire/projet/chantier | 84 | 71 | 8 | chantier, affaire, planning chantier, bordereau de chantier, dépannage d'ajout d'un compte chantier au planning d'intervention, planning de chantier, suivi de chantier, affichage des prévisions météo par chantier dans le planning |
| catalogue/tarification | 82 | 60 | 9 | produit, ouvrage, bibliothèque, catégorie tarifaire, produit centralisé, tarif centralisé, bibliothèque de prix tierce, catalogue produits |
| planning | 72 | 47 | 10 | rendez-vous, synchronisation agenda, planning, agenda, planning chantier, dépannage d'ajout d'un compte chantier au planning d'intervention, en-tête planning, planning de chantier |
| stock/réception | 71 | 63 | 9 | gestion de stock, gestion des stocks, inventaire, valorisation de stock, accusé de réception, affectation stock, alerte stock, bon de réception |
| paiement/règlement | 70 | 54 | 9 | règlement, paiement, moyen de paiement, conditions de paiement, mode de règlement, prélèvement sepa, règlement facture, règlements |
| documents | 70 | 60 | 8 | pièce commerciale, document de vente, modèle de document, apparence de document, document, documentation, affichage coordonnées client sur documents, ajout d'une mention descriptive au taux de tva affichée sur les documents |
| comptabilité/rapprochement bancaire | 66 | 39 | 8 | rapprochement bancaire, compte bancaire, code comptable, remise en banque, plan comptable, comptabilité, compte de charge, connexion bancaire |
| intervention | 65 | 56 | 6 | demande d'intervention, rapport d'intervention, rapports d'intervention et signatures, dépannage d'ajout d'un compte chantier au planning d'intervention, facturation d'une intervention, intervention, absence de liaison automatique des rapports d'intervention aux factures groupées, activation des frais kilométriques pour les interventions |
| facturation électronique / conformité fiscale | 63 | 35 | 10 | facturation électronique, taux de tva, cgv, tva, cerfa 15497, conditions générales de vente, facturation électronique obligatoire, mentions légales |
| sécurité/authentification | 58 | 43 | 9 | mot de passe, connexion, double authentification, connexion bancaire, identifiants de connexion, rgpd, récupération du lien de connexion à l'espace entreprise, connexion collaborateur |
| sav/support | 54 | 48 | 7 | sav, dépannage d'ajout d'un compte chantier au planning d'intervention, support, support client, ticket de support, affichage sav, checklist de dépannage de soumission de devis bloquée, configuration d'un serveur mail sortant et dépannage des erreurs smtp |
| utilisateurs/comptes | 34 | 28 | 8 | utilisateur, compte utilisateur, identifiants de connexion, profil utilisateur, préférences utilisateur, achat de packs de licences utilisateurs, achat groupé de licences utilisateurs, configuration du profil utilisateur |
| signature | 33 | 18 | 8 | signature électronique, rapports d'intervention et signatures, signature email, signatures électroniques, absence de valeur légale probante de la signature électronique gratuite, configuration d'une signature d'email automatique, création de pourcentages de probabilité de signature liés aux opportunités, dépannage de la suppression de signature email de profil |
| crm/opportunités | 29 | 21 | 3 | opportunité, pipeline, opportunités, activation et utilisation des pistes commerciales avant conversion en opportunités, configuration des modèles de projets et attributs pour les opportunités, configuration des statuts d'opportunité, création automatique d'opportunités par transfert d'email, création d'un devis depuis une opportunité crm |
| ia/automatisation | 27 | 9 | 5 | automatisation, ia, assistant devis vocal, automatisation commerciale, automatisation comptable, automatisation des demandes d'avis clients, automatisations, configuration d'une automatisation |
| site/adresse/lieu | 24 | 18 | 9 | géolocalisation, tournée, adresse, site internet, adresse d'envoi fixe des avenants, adresse de facturation électronique, adresse e-mail client, adresse par défaut |
| application mobile | 23 | 16 | 8 | application mobile, application extrabat today v3.5, application extradoc, application extrabat today, application mobile extrabat today, compatibilité de l'application mobile, connexion à l'application mobile, création et suivi d'une intervention depuis l'application mobile |
| acompte | 22 | 15 | 7 | facture d'acompte, acompte, acompte au prorata, acompte et solde, annulation d'une facture d'acompte, base de calcul htva d'une facture d'acompte, contournement pour déduire un acompte ttc quand le système demande un montant ht, création d'une facture d'acompte |
| avoir/remboursement | 20 | 15 | 8 | avoir, création d'une note de crédit, remboursement client, avoir client, avoir fournisseur, avoir sur facture, avoirs clients, comportement de statut d'une note de crédit et solutions de régularisation |
| tâches/notifications | 19 | 16 | 7 | notifications, tâche, widget notifications, bibliothèque de lots et tâches, configuration de tâches automatiques déclenchées par événement, configuration des tâches de chantier, création et catégorisation des tâches d'intervention, création et suivi des tâches administratives liées à un chantier |
| onboarding/configuration | 15 | 6 | 7 | configuration smtp, paramétrage navigateur, extension chrome, extension navigateur, onboarding, extension chrome « l'assistant vertuoza » |
| commande fournisseur | 13 | 4 | 5 | commande fournisseur, bon de commande v1, connecteur d'achat, connecteurs d'achat |
| marketing/communication | 13 | 6 | 3 | smart tag, campagne emailing, newsletter produit, promotion, code promotionnel, newsletter |
| prospect/demande/lead | 12 | 8 | 6 | demande d'intervention, fiche prospect, prospect, connecteur de leads, création et structuration d'une demande d'intervention, pipeline de prospection, suivi prospect, tracking prospects |
| commande client | 10 | 7 | 6 | bon de commande, bon de commande v1, commandes v2, bon de commande client, commande client, dépannage de correspondance bon de commande, logique de substitution du montant de bon de commande par le montant de facture supérieur |
| photos | 10 | 6 | 5 | photo, consultation des photos ajoutées en commentaire sur une fiche contact, photo juridique, photos, photos certifiées, photos dans devis |
| équipement/actif/parc | 9 | 7 | 2 | bouteille de fluide, équipement, création et gestion du parc installé, page publique des équipements via qr code, équipements, équipements niveau 1, équipements niveau 2 |
| maintenance | 9 | 8 | 3 | contrat de maintenance, contrats de maintenance, fiche de maintenance, option « maintenance et interventions », planification cartographique des maintenances, signature électronique d'un contrat de maintenance, suivi des heures et rentabilité d'une maintenance, tableau des maintenances |
| rôles/permissions | 8 | 7 | 5 | profil de privilèges, création et permissions d'un utilisateur avec compte gestion, création et permissions d'un utilisateur avec compte ouvrier, droits utilisateur, gestion des droits utilisateurs pour les interventions et le paiement, gestion des permissions et rôles utilisateurs, rôles et permissions |
| visite | 2 | 2 | 2 | date de visite préalable, visite avant devis |

**Lecture — volume suffisant pour une analyse ultérieure ?**

- **Volume large (≥ 50 documents, ≥ 6 concurrents)** : facture/facturation
  (193, 10 concurrents), devis (144, 10), intégrations/synchronisations (120,
  10), client/contact (118, 10), rapports/pilotage/tableaux de bord (86, 8 —
  mais concentré à 72 % chez Sellsy, à vérifier avant de généraliser),
  affaire/projet/chantier (84, 8), catalogue/tarification (82, 9), planning
  (72, 10), stock/réception (71, 9), paiement/règlement (70, 9), documents
  (70, 8), comptabilité/rapprochement bancaire (66, 8), intervention (65, 6),
  facturation électronique / conformité fiscale (63, 10), sécurité/
  authentification (58, 9), sav/support (54, 7 — concentré à 54 % chez
  Vertuoza). Ces domaines ont, en l'état, un volume documentaire qui paraît
  suffisant pour justifier une analyse V3 ciblée.
- **Volume moyen (15-50 documents)** : utilisateurs/comptes (34, 8), signature
  (33, 8), crm/opportunités (29, 3 — concentré chez 3 éditeurs seulement),
  ia/automatisation (27, 5), site/adresse/lieu (24, 9), application mobile
  (23, 8), acompte (22, 7), avoir/remboursement (20, 8), tâches/notifications
  (19, 7), onboarding/configuration (15, 8). Volume exploitable mais plus
  étroit ; une analyse ciblée y trouverait moins de variance inter-éditeurs.
- **Volume faible (< 15 documents)** : commande fournisseur (13, 5), marketing/
  communication (13, 3), prospect/demande/lead (12, 6), commande client (10,
  6), photos (10, 5), équipement/actif/parc (9, 2), maintenance (9, 3), rôles/
  permissions (8, 5), visite (2, 2). À ce stade, silence documentaire ne veut
  pas dire absence fonctionnelle (SCHEMA-LIGHT.md §9) — un volume faible dans
  LIGHT peut aussi refléter un objet peu documenté plutôt que peu présent dans
  le produit. Une lecture ciblée serait nécessaire avant toute conclusion.

**Domaines ajoutés, non présents dans la liste de départ de la mission** :
facturation électronique / conformité fiscale, comptabilité/rapprochement
bancaire, rapports/pilotage/tableaux de bord, crm/opportunités, marketing/
communication, sécurité/authentification, intégrations/synchronisations,
ia/automatisation, application mobile. Plusieurs de ces domaines ajoutés
(facturation électronique, intégrations, comptabilité) affichent des volumes
et une couverture inter-éditeurs comparables ou supérieurs à des domaines de
la liste suggérée — ils ne devraient pas être traités comme secondaires du
seul fait de ne pas avoir été anticipés.

## 7. Ambiguïtés à résoudre

### Client vs Contact vs Prospect

**Termes observés.** `client`, `contact`, `prospect`, `fiche client`, `fiche
contact`, `fiche prospect`, `client/prospect` (valeur exacte composite chez
Extrabat).

**Ce que LIGHT établit.** Les trois termes coexistent chez plusieurs éditeurs
(Extrabat, Costructor, Batikko utilisent `client`/`prospect` de façon
apparemment interchangeable dans un même document — `extrabat:
supprimer-prospect-client.md` a pour valeur exacte `client/prospect
(suppression impossible, corbeille)`, `costructor:ventes/comment-creer-un-
client-prospect-ue8wib.md` traite « client prospect » comme une seule entité
dans son URL). OpenFire et Sellsy emploient plutôt `contact` comme terme
générique unique, avec des déclinaisons de fiche.

**Ce que LIGHT n'établit pas.** Si `client` et `prospect` sont deux statuts
d'un même objet (cycle de conversion) ou deux objets distincts avec
migration ; si `contact` chez OpenFire/Sellsy est un troisième objet parent
(société + rôle) ou un synonyme d'un des deux autres.

**Sources à relire plus tard.**
`extrabat:supprimer-prospect-client.md`,
`extrabat:creer-un-client-via-lagenda.md`,
`costructor:ventes/comment-creer-un-client-prospect-ue8wib.md`,
`openfire:utiliser-openfire/fusionner-vos-contacts.md`,
`batikko:guides/clients-crm.md`.

### Chantier vs Affaire vs Projet

**Termes observés.** `chantier` (inter-fast, progbat, obat, batikko),
`affaire` (extrabat exclusivement, 3 occurrences).

**Ce que LIGHT établit.** Extrabat n'utilise jamais `chantier` comme racine
distincte de `affaire` sur les documents observés ; les valeurs exactes
d'`affaire` (« création, association pièces commerciales », « synthèse
rentabilité ») recouvrent des fonctions qu'InterFast/ProGBat/Obat rattachent à
`chantier` (planning, suivi, dossier). ProGBat, lui, distingue explicitement
« chantier » et « marché de travaux » dans une même valeur exacte (`chantier
[concept, distinction chantier/marché de travaux, statuts]`), preuve qu'au
moins un éditeur traite ces notions comme non équivalentes en interne.

**Ce que LIGHT n'établit pas.** Si `affaire` chez Extrabat est un synonyme
éditorial de `chantier`, ou un objet parent plus large (dont le chantier ne
serait qu'une composante), ou un vestige terminologique (Extrabat vient du
BTP/artisanat, vocabulaire potentiellement plus proche de la gestion
commerciale que du terrain).

**Sources à relire plus tard.**
`extrabat:bonnes-regles-afin-de-creer-affaire-de-gerer.md`,
`extrabat:synthese-rentabilite-dune-affaire.md`,
`progbat:le-menu-principal/chantiers-personnel/chantiers.md`,
`obat:chantier.md`.

### Site / adresse d'intervention vs lieu

**Termes observés.** `adresse`, `site internet` (sens différent : vitrine web,
pas lieu physique), `géolocalisation`, `tournée`.

**Ce que LIGHT établit.** `site internet` chez Batikko/Costructor désigne un
site web vitrine, sans rapport avec un lieu d'intervention — homonymie pure
avec le sens BTP usuel de « site » (chantier physique). Aucune racine
distincte de type « site d'intervention » ou « lieu » n'apparaît dans
l'inventaire ; les notions de lieu physique se rattachent à `adresse` ou
directement à `chantier`.

**Ce que LIGHT n'établit pas.** Si les éditeurs orientés terrain (InterFast,
Vertuoza, OpenFire) modélisent un objet « site/lieu d'intervention » distinct
du chantier lui-même (plusieurs sites par chantier, ou l'inverse) — LIGHT ne
donne aucune racine dédiée pour trancher.

**Sources à relire plus tard.**
`batikko:guides/site-internet.md`,
`costructor:site-internet/comment-creer-son-site-internet-f61wvw.md`,
`openfire` (racine `adresse`, `géolocalisation`, `tournée` — chemins non
repris ici, cf. inventaire §3).

### Visite vs Intervention

**Termes observés.** `visite` (2 occurrences seulement : obat, inter-fast —
`date de visite préalable`, `visite avant devis`), `intervention`, `demande
d'intervention`, `rapport d'intervention`.

**Ce que LIGHT établit.** `visite` est quasi absente du corpus en tant que
racine autonome (2/2510 lignes) et se rattache, dans les deux occurrences
observées, à une étape *avant* devis — pas à une notion de type
d'intervention parallèle. `intervention` est beaucoup plus fréquent (65
documents sur le domaine, §6) et couvre un spectre large (planification,
facturation, rapport, clôture).

**Ce que LIGHT n'établit pas.** Si « visite » est un type particulier
d'intervention (visite technique, visite commerciale) chez les éditeurs qui
ne l'emploient pas comme racine explicite, ou si le concept existe mais sous
d'autres termes (ex. « rendez-vous », racine distincte à 8 occurrences,
2 concurrents) — LIGHT ne permet pas de faire le lien sémantique entre les
deux sans relecture.

**Sources à relire plus tard.**
`obat` (racine `visite`, chemin non repris ici), `inter-fast` (racine
`visite`), et le domaine `intervention` en général (§6) pour vérifier
l'absence/présence du terme « visite » à l'intérieur du corps des documents
(LIGHT ne code que l'objet principal, pas tous les termes employés dans le
corps).

### Équipement vs installation vs actif vs parc

**Termes observés.** `équipement` (openfire, 2 occurrences), racine
`équipement/actif/parc` du domaine §6 (« création et gestion du parc
installé », « page publique des équipements via qr code », « bouteille de
fluide » — inter-fast, openfire).

**Ce que LIGHT établit.** Seuls InterFast et OpenFire portent ce domaine dans
le corpus observé (9 documents au total, §6) — signe d'un domaine
potentiellement spécifique aux métiers avec parc matériel installé (froid/
climatisation pour la « bouteille de fluide », qui renvoie à la
réglementation fluides frigorigènes). Aucune racine `installation` ou `actif`
distincte n'apparaît : le terme utilisé est `équipement` ou `parc`.

**Ce que LIGHT n'établit pas.** Si `équipement`, `installation` (terme non
observé comme racine autonome) et `actif` (terme non observé) désignent des
objets réellement différents chez ces éditeurs, ou si LIGHT a simplement codé
la même réalité sous des libellés voisins selon le document. Volume trop
faible (9 documents) pour trancher sans relecture.

**Sources à relire plus tard.**
`openfire:guides-videos/creer-un-equipement-sur-mobile.md`,
`openfire:utiliser-openfire/consulter-et-gerer-ses-equipements-sur-le-
portail.md`, et les documents inter-fast du domaine équipement/actif/parc
(§6).

### Devis / version / avenant

**Termes observés.** `devis`, `variantes de devis` (obat, inter-fast),
`avenant` (progbat, 1 occurrence : « avenant [devis complémentaire en cours de
chantier] »), `import de devis`.

**Ce que LIGHT établit.** `avenant` n'apparaît qu'une seule fois comme racine
distincte (ProGBat), avec une valeur exacte qui le définit explicitement comme
un « devis complémentaire en cours de chantier » — donc un sous-type de devis
plutôt qu'un objet contractuel séparé, au moins pour cet éditeur. `variantes
de devis` (obat, inter-fast) suggère un mécanisme de version parallèle
(plusieurs devis concurrents pour une même demande), distinct de l'avenant
(devis complémentaire en cours d'exécution).

**Ce que LIGHT n'établit pas.** Si « avenant » chez les éditeurs qui ne
l'utilisent pas comme racine (Vertuoza, Sellsy, etc.) existe sous un autre
terme, ou si le mécanisme de versionnement du devis (variante, révision,
avenant) est unifié ou éclaté en plusieurs objets selon les éditeurs.

**Sources à relire plus tard.**
`progbat:le-menu-principal/devis-factures/avenant.md`, et les documents des
racines `variantes de devis`, `import de devis` (obat, inter-fast, progbat,
costructor — cf. §3.2).

### SAV comme objet ou comme type d'intervention

**Termes observés.** `sav` (extrabat, openfire — 3 occurrences), `intervention`,
`sav/support` (domaine §6, 54 documents, 7 concurrents, concentré 54% chez
Vertuoza sous d'autres racines que `sav` littéralement).

**Ce que LIGHT établit.** Chez Extrabat, `sav` est codé comme un objet/dossier
à part entière (« SAV [dossier complet, cycle commercial/logistique/
technique] », « SAV [enregistrement + planification RDV] ») — un objet qui
génère lui-même une planification, pas seulement une étiquette sur une
intervention. Chez OpenFire, l'unique occurrence (`gerer-et-planifier-un-
sav.md`) est côté « gérer et planifier », compatible avec les deux lectures.

**Ce que LIGHT n'établit pas.** Si, chez les éditeurs qui ne codent jamais
`sav` comme racine (la majorité), le SAV existe comme type d'intervention
(tag/statut sur l'objet intervention) plutôt que comme objet séparé, ou n'a
simplement pas été rencontré dans les rubriques échantillonnées par LIGHT
(silence documentaire ≠ absence fonctionnelle).

**Sources à relire plus tard.**
`extrabat:comment-enregistrer-sav.md`,
`extrabat:enregistrer-un-nouveau-sav-et-caler-le-rendez-vous.md`,
`openfire:utiliser-openfire/gerer-et-planifier-un-sav.md`, et le domaine
`intervention` en général (§6) pour vérifier si un tag « SAV » apparaît dans
le corps des documents InterFast/Vertuoza/ProGBat/Sellsy sans être devenu
`objet_principal`.


## 8. Limites

- **Fréquence documentaire ≠ importance produit.** Un domaine peu représenté
  dans LIGHT (ex. visite, 2 documents) peut correspondre à une fonctionnalité
  importante mais peu documentée, ou documentée ailleurs (FAQ, in-app) hors du
  périmètre LIGHT (aide/documentation produit uniquement, cf. SCHEMA-LIGHT.md
  §2).
- **Silence documentaire ≠ absence fonctionnelle.** L'absence d'une racine chez
  un concurrent ne prouve pas que la fonction correspondante n'existe pas dans
  le produit — seulement qu'elle n'a pas donné lieu à un document dont
  `objet_principal` porte ce terme, dans le périmètre effectivement codé par
  LIGHT à ce jour.
- **Regroupement lexical ≠ identité métier.** Les familles du §5 sont des
  candidats de rapprochement fondés sur la forme des racines, pas des preuves
  que les objets sous-jacents sont identiques. Plusieurs sont explicitement
  qualifiées AMBIGU ou CONCEPT_PROCHE_MAIS_DISTINCT pour cette raison.
- **La racine mécanique ne fusionne pas tout ce qui devrait l'être.**
  Singulier/pluriel (`opportunité`/`opportunités`, `signature électronique`/
  `signatures électroniques`), synonymes non structurels (`avoir`/`note de
  crédit`), ou variantes orthographiques ne sont pas normalisés par la règle
  de troncature — ils apparaissent comme des racines séparées dans
  l'inventaire (§3) et n'ont été rapprochés que manuellement, en tant que
  candidats, au §5. D'autres rapprochements de cette nature existent
  probablement dans les 1624 racines uniques du §3.3 sans avoir été
  repérés ici (aucune relecture exhaustive de la longue traîne n'a été menée
  au-delà de la recherche par mots-clés du §6).
- **Convention Extrabat du tiret cadratin.** Les 37 lignes à racine vide
  (§3.1) codent une absence d'objet substantiel, pas un concept métier — à
  exclure de toute lecture de fréquence par racine.
- **Micro-lot H3 non représentatif.** Les 6 lignes InterFast/Vertuoza du
  micro-lot H3 ont été sélectionnées pour porter des contrôles de
  conditionnalité connus, pas pour échantillonner ces deux corpus — leurs
  `objet_principal` (validation de commandes fournisseurs, fil d'activité de
  chantier, etc.) ne doivent pas être lus comme représentatifs de la
  proportion réelle de ces sujets chez InterFast/Vertuoza, même si elles
  s'additionnent sans doublon aux productions complètes (cf. §2).
- **Pilote historique, discipline légèrement différente.** Le pilote applique
  SCHEMA-LIGHT.md par anticipation (le contrat a été écrit après coup, cf.
  SCHEMA-LIGHT.md préambule) ; ses `longueur_mots` sont des estimations
  visuelles, pas un comptage mécanique (SCHEMA-LIGHT.md §11) — sans incidence
  sur `objet_principal`, seul champ exploité ici.
- **Aucune conclusion produit SUPORDO.** Ce document ne propose aucune
  architecture, aucune table, aucun backlog, aucun objet canonique. Il
  présélectionne des pistes de lecture (§6) et signale des questions
  ouvertes (§7) pour une mission ultérieure.

