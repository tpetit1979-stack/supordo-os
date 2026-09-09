# LIGHT — production Obat (corpus aide)

**ÉTAT : COMPLET — 274/274 documents traités, tous les contrôles mécaniques
ont réussi (voir § Contrôles mécaniques).**

Production sous SCHEMA-LIGHT.md (contrat canonique), lu intégralement avant
ce run. Discipline : un document à la fois, lu intégralement, sortie écrite
immédiatement, aucune correction rétroactive sauf erreur mécanique démontrée
et journalisée. Run de production, pas un test méthodologique de LIGHT.

## Périmètre — vérification mécanique et gel

- `obat_help` (`corpus_index.json`) : **274** documents (`type: aide`,
  source `https://aide.obat.fr/`, `collection_method: automatique`,
  `coverage_status: collected`). Centre d'aide HubSpot, articles à plat :
  les 23 entrées d'`editorial_taxonomy` dans `corpus_index.json` sont en
  réalité des préfixes de dossier issus de slugs source contenant des `/`
  (22 chemins du périmètre en portent la trace, ex. `hcms/mem/logout.md`),
  pas une arborescence éditoriale au sens Sellsy/Axonaut.
  `analysis_exclusions: []` dans `corpus_index.json` : **aucune exclusion
  déclarée pour ce corpus.**
- Vérification mécanique disque : `find 01-discovery/concurrents/sources/obat/centre_aide -name "*.md" | wc -l`
  = **274**, identique au chiffre `corpus_index.json`. Écart nul.
- Règle « inédit » (SCHEMA-LIGHT.md §5) : recherche `grep -ril obat` sur
  l'ensemble des fichiers `light-*.md` existants du dépôt — **aucune
  occurrence**. Aucun document obat n'a d'observation LIGHT antérieure.
  Périmètre LIGHT = périmètre de collecte intégral, sans soustraction.
- Garde-fou de mission (274 documents, aucune exclusion) : recalculé
  mécaniquement, écart nul avec le chiffre annoncé en mission.
- **Périmètre gelé à traiter : 274. Exclusions : aucune (le confirmer
  explicitement, comme demandé — obat_help ne porte aucune exclusion
  d'analyse).**

Méthode `longueur_mots` (déclarée avant toute lecture de contenu) :
frontmatter YAML retiré mécaniquement (bloc délimité par les deux premières
lignes `---` du fichier), puis comptage de mots du corps Markdown restant
par `wc -w` (script bash dédié, appliqué uniformément aux 274 documents du
périmètre gelé avant tout codage). Le compte est donc mécanique et non une
estimation visuelle, conformément à SCHEMA-LIGHT.md §4.

Liste du périmètre gelé, par chemin relatif à
`01-discovery/concurrents/sources/obat/centre_aide/` (274, triée) :

```
1-mois-de-licences-gratuites-pour-bien-d-c3-a9marrer-avec-obat.md
accedez-a-une-bibliotheque-complete-douvrages-pour-vos-devis.md
accedez-a-vos-contacts-en-un-clic-depuis-vos-chantiers-devis-ou-factures.md
activation-de-lassistant-devis-vocal.md
administrer-bibliotheque-et-taches.md
affichage-du-num-c3-a9ro-de-siret-du-professionnel.md
ajouter-ou-modifier-des-postes-complementaires-sur-vos-factures-de-situation-dans-obat.md
ajouter-ou-modifier-un-moyen-de-paiement-sur-obat.md
ajoutez-facilement-une-tva-c3-a0-0-sur-vos-factures-de-situation-ou-finales.md
ajustez-facilement-vos-factures-avec-le-nouvel-ajustement-ttc.md
annuler-une-facture-sans-cr-c3-a9er-un-avoir-ce-nest-plus-possible.md
application-mobile.md
assistante-devis-vocal.md
astuces.md
biblioth-c3-a8que.md
centralisez-toutes-vos-ressources-sur-obat-grace-a-un-nouveau-listing-simplifie.md
chantier.md
chift-synchronisation-initiale-du-logiciel-comptable-a-pennylane.md
chift-transmettre-les-c3-a9critures-comptables-de-factures.md
collectez-des-avis-clients-sur-le-terrain-grace-au-qr-code.md
comment-acc-c3-a9der-c3-a0-vos-factures-d-abonnement-obat.md
comment-acc-c3-a9der-c3-a0-votre-biblioth-c3-a8que-batichiffrage-depuis-l-c3-a9diteur-de-devis/factures.md
comment-acc-c3-a9der-c3-a0-votre-biblioth-c3-a8que-depuis-l-c3-a9diteur-de-facture/devis.md
comment-acc-c3-a9der-et-param-c3-a9trer-vos-conditions-g-c3-a9n-c3-a9rales-de-vente-sur-obat.md
comment-acc-c3-a9der-rapidement-c3-a0-un-nouveau-document-sur-obat.md
comment-activer-la-signature-c3-a9lectronique-sur-obat.md
comment-afficher-les-coordonn-c3-a9es-de-vos-clients-sur-vos-documents.md
comment-afficher-les-r-c3-a9f-c3-a9rences-das-articles-sur-le-devis.md
comment-ajouter-des-c3-a9l-c3-a9ments-de-fourniture-et-de-main-d-c5-93uvre-c3-a0-vos-devis/factures.md
comment-ajouter-des-c3-a9l-c3-a9ments-de-fourniture-main-d-c5-93uvre-ouvrage-danciens-devis-depuis-l-c3-a9diteur-de-facture/devis.md
comment-ajouter-des-c3-a9l-c3-a9ments-de-fourniture/main-doeuvre/ouvrage-sur-une-facture.md
comment-ajouter-des-chantiers-devises-dans-le-calendrier/planning.md
comment-ajouter-des-postes-libres-ht-sur-vos-devis-et-factures.md
comment-ajouter-plusieurs-adresses-diff-c3-a9rentes-c3-a0-un-client-sur-obat.md
comment-ajouter-plusieurs-ressources-dans-un-evenement-du-calendrier.md
comment-ajouter-un-chantier-sur-obat.md
comment-ajouter-un-client-c3-a0-votre-devis/factures.md
comment-ajouter-un-coefficient-global-dajustement-sur-votre-devis.md
comment-ajouter-un-ouvrage-de-batichiffrage-sur-obat.md
comment-ajouter-un-ouvrage-sur-vos-devis/factures.md
comment-ajouter-un-qr-code-sur-vos-documents-devis-et-factures.md
comment-ajouter-un-saut-de-page-sur-vos-devis/factures.md
comment-ajouter-un-taux-de-tva-personnalis-c3-a9-sur-obat.md
comment-ajouter-une-nouvelle-unit-c3-a9-de-quantit-c3-a9-sur-obat.md
comment-ajouter-une-remise-globale-ou-ligne-par-ligne-sur-vos-devis/factures.md
comment-ajouter-une-retenue-de-garantie-sur-vos-devis/factures.md
comment-ajouter-une-section-c3-a0-votre-devis/facture.md
comment-ajouter-vos-conditions-de-paiements-par-d-c3-a9faut-sur-obat.md
comment-ajouter-vos-documents-annexes-dans-vos-chantiers.md
comment-ajouter-votre-logo-sur-vos-documents.md
comment-ajouter-votre-rib-sur-vos-documents-obat.md
comment-am-c3-a9liorer-la-pr-c3-a9sentation-de-vos-documents-sur-obat.md
comment-analyser-la-ventilation-de-votre-chiffre-d-affaires-sur-obat.md
comment-bien-gerer-votre-facturation-pendant-la-bascule-vers-obat.md
comment-c3-a9diter-et-mettre-en-forme-un-devis-sur-obat.md
comment-c3-a9diter-un-bordereau-de-chantier-sur-obat.md
comment-cacher-certaines-informations-sur-votre-devis.md
comment-cacher-l-c3-a9diteur-de-style-sur-le-devis.md
comment-configurer-les-emails-envoyes-depuis-obat.md
comment-connecter-votre-banque-sur-obat.md
comment-consulter-le-widget-nouveaut-c3-a9s.md
comment-cr-c3-a9er-et-modifier-une-facture-finale.md
comment-cr-c3-a9er-un-avoir-sur-une-facture-sur-obat.md
comment-cr-c3-a9er-un-raccourcis-obat-sur-le-bureau/c3-a9cran-d-accueil-depuis-google-chrome.md
comment-creer-et-parametrer-votre-compte-pro-swan.md
comment-d-c3-a9duire-un-acompte-d-une-facture-finale.md
comment-dupliquer-une-facture-finale/devis.md
comment-effectuer-une-facture-de-situation-sur-obat.md
comment-exclure-les-postes-complementaires-des-retenues-garanties.md
comment-exporter-les-lignes-de-vos-devis/factures.md
comment-exporter-votre-suivi-du-temps.md
comment-facturer-un-acompte-depuis-un-devis-sur-obat.md
comment-faire-apparaitre-la-gestion-des-d-c3-a9chets-sur-vos-devis-avec-obat.md
comment-faire-une-facture-de-d-c3-a9bours-sur-obat.md
comment-faire-une-facture-proforma-avec-obat.md
comment-faire-vos-conditions-g-c3-a9n-c3-a9rales-de-vente-dans-le-btp.md
comment-g-c3-a9n-c3-a9rer-un-d-c3-a9compte-g-c3-a9n-c3-a9ral-sur-obat.md
comment-g-c3-a9n-c3-a9rer-une-attestation-de-tva-sur-obat.md
comment-g-c3-a9rer-les-familles-de-votre-biblioth-c3-a8que-personnalis-c3-a9e.md
comment-importer-vos-cgv-eu-format-pdf-sur-obat.md
comment-indiquer-la-date-de-visite-pr-c3-a9alable-sur-le-devis.md
comment-ins-c3-a9rer-un-c3-a9l-c3-a9ment-c3-a0-une-section-pour-r-c3-a9tablir-la-bonne-num-c3-a9rotation-de-vos-lignes-et-le-bon-calcul-des-sous-totaux.md
comment-ins-c3-a9rer-vos-primes-c3-a9nerg-c3-a9tiques-dans-vos-devis.md
comment-int-c3-a9grer-les-indemnit-c3-a9s-de-retard.md
comment-mettre-en-place-un-compte-prorata-sur-vos-devis-et-factures.md
comment-modifier-et-personnaliser-la-num-c3-a9rotation-des-lignes-dun-devis-sur-obat.md
comment-modifier-l-apparence-dun-devis-sur-obat.md
comment-modifier-la-num-c3-a9rotation-de-vos-factures/avoirs/devis.md
comment-modifier-le-co-c3-bbt-horaire-de-vos-ressources.md
comment-modifier-votre-adresse-mail-de-connexion-et-votre-mot-de-passe.md
comment-parametrer-les-relances-des-factures.md
comment-parametrer-votre-compte-obat.md
comment-parrainer-un-ami-sur-obat.md
comment-passer-son-compte-en-non-assujetti-c3-a0-la-tva.md
comment-passer-vos-devis-en-factures-de-mani-c3-a8re-efficace-et-simple.md
comment-passer-votre-devis-en-autoliquidation-sur-obat.md
comment-prendre-des-photos-certifi-c3-a9es-avec-obat.md
comment-rechercher-des-c3-a9l-c3-a9ments-dans-votre-biblioth-c3-a8que-personnalis-c3-a9e.md
comment-recr-c3-a9er-un-devis-pr-c3-a9c-c3-a9demment-cr-c3-a9-c3-a9-sur-un-autre-logiciel-dans-obat.md
comment-retrouver-facilement-un-devis-ou-une-facture-sur-obat.md
comment-retrouver-vos-documents-facilement-sur-le-menu-chantier.md
comment-s-c3-a9lectionner-le-type-de-collecte-de-la-tva-sur-votre-compte-obat.md
comment-sabonner-c3-a0-batichiffrage-sur-obat.md
comment-soigner-lapparence-de-vos-devis.md
comment-sont-calcul-c3-a9s-les-graphiques-statistiques-dobat.md
comment-suivre-vos-achats-avec-obat-et-g-c3-a9rer-leurs-r-c3-a8glements.md
comment-synchroniser-rapidement-votre-compte-obat-avec-votre-adresse-gmail.md
comment-synchroniser-son-calendrier-obat-avec-son-calendrier-google.md
comment-transferer-vos-appels-vers-le-repondeur-intelligent.md
comment-trouver-un-chantier-sur-la-marketplace-obat.md
comment-utiliser-l-c3-a9diteur-de-style.md
comment-utiliser-la-reconnaissance-optique-de-caract-c3-a8res-ocr-lors-de-la-saisie-de-vos-d-c3-a9penses-sur-obat.md
comment-utiliser-le-calcul-de-marge-sur-obat.md
comment-utiliser-le-generateur-de-cgv-obat.md
comment-vider-les-caches-sur-google-chrome.md
comment-visualiser-la-repartition-des-achats-par-categorie-sur-obat.md
comment-visualiser-la-tva-deductible-payee-lors-des-achats.md
comment-visualiser-vos-encaissements-et-vos-retards-dencaissement-sur-obat.md
comment-visualiser-votre-chiffre-d-affaires.md
comment-visualiser-votre-performance-commerciale-sur-obat.md
comment-visualiser-votre-tva-collect-c3-a9e-sur-obat.md
comptabilit-c3-a9.md
comptes-auxiliaires-comptable.md
comptes-auxiliaires-plus-de-souplesse-moins-de-contraintes.md
configuration-de-votre-planning/calendrier/suivi-du-temps-version-2.md
configuration-des-c3-a9l-c3-a9ments-du-logiciel-comptable.md
configurer-vos-ressources-le-planning.md
connectez-votre-compte-legrand.md
connexion-simplifiee-a-obat-utilisez-google-ou-facebook.md
consultez-et-partagez-vos-bordereaux-de-chantier-directement-dans-le-calendrier-obat.md
contacts.md
cr-c3-a9e-ta-vitrine-en-ligne-avec-lannuaire-obat.md
cr-c3-a9er-un-c3-a9v-c3-a9nement-sur-un-calendrier.md
cr-c3-a9ez-votre-logo-professionnel-en-quelques-clics-avec-obat.md
creez-des-evenements-recurrents-dans-votre-calendrier-obat.md
d-c3-a9placer-un-chantier-dans-sa-globalit-c3-a9-en-dragdrop.md
dans-quelles-conditions-puis-je-supprimer-ou-annuler-une-facture.md
decouvrez-les-ecrans-vides-enrichis-dans-obat-un-vrai-coup-de-pouce-pour-demarrer-sereinement.md
devis.md
dictez-vos-devis-depuis-obat-grace-a-notre-assistant-vocal.md
entreprise-eurl/sarl/sas-comment-s-abonner-c3-a0-obat-et-choisir-son-pack.md
evolution-multiutilisateur-une-gestion-commerciale-encore-plus-precise-avec-obat-bientot-disponible.md
export-comptable-et-comptes-auxiliaires-sur-obat.md
export-des-achats-sur-obat.md
exports-comptables-vos-pieces-justificatives-sont-desormais-nommees-de-fa-c3-a7on-coherente.md
extension-navigateur-obat-v2-copiez-vos-fiches-produits-encore-plus-facilement.md
facturation-c3-a9lectronique.md
facturation-electronique-dans-le-btp-dates-cles-formats-et-obligations.md
facturation-electronique-obligatoire-en-belgique-des-2026.md
facturation-electronique-obligatoire-en-france-des-septembre-2026.md
facturation-electronique-tout-savoir-sur-la-verification-didentite.md
factures.md
formulaire-de-demande-de-devis-int-c3-a9gre-a-votre-fiche-annuaire-obat.md
franchise-en-base-de-tva-la-mention-legale-de-vos-factures-change-au-1er-septembre-2026.md
g-c3-a9rez-vos-chantiers-plus-facilement-gr-c3-a2ce-c3-a0-longlet-planning.md
gagnez-du-temps-avec-lachat-de-packs-de-licences-utilisateurs-sur-obat.md
gagnez-du-temps-avec-lautocompl-c3-a9tion-des-entreprises-dans-obat.md
gagnez-du-temps-gr-c3-a2ce-c3-a0-lint-c3-a9gration-entre-obat-et-qonto.md
gagnez-du-temps-sur-vos-devis-grace-a-lextension-chrome-obat.md
gerer-votre-calendrier.md
gerez-vos-plus-et-moins-values-facilement-dans-les-factures-de-situation-detaillees.md
gestion-des-avoirs-fournisseurs.md
gestion-des-bons-de-commande-sur-obat.md
gestion-des-stocks-simplifi-c3-a9s.md
hcms/mem/logout.md
import-externe-excel/dpgf.md
importer-votre-fichier-client.md
imprimer-et-diffuser-votre-planning.md
index.md
ins-c3-a9rer-des-photos-dans-un-devis-ou-une-facture.md
interventions.md
invitez-vos-collaborateurs-sur-obat-par-numero-de-telephone.md
la-consultation-bancaire-sur-obat.md
la-facture-dacompte-libre.md
la-gestion-des-achats-bons-de-commande-et-de-la-rentabilit-c3-a9-sur-obat.md
la-gestion-des-achats-et-de-la-rentabilite-et-le-suivi-des-marges-sur-obat.md
la-gestion-des-interventions-dans-obat.md
la-gestion-des-plus-et-moins-values-sur-les-factures-de-situations-d-c3-a9taill-c3-a9es.md
la-gestion-des-r-c3-a8glement-sur-obat-facture-acquitt-c3-a9e.md
la-gestion-des-stocks-sur-obat.md
la-marketplace-obat.md
la-mediation-de-la-consommation-une-obligation-et-une-opportunite-pour-les-professionnels-du-batiment.md
la-meteo-sur-obat.md
la-page-client-document-obat.md
la-page-partenaires.md
la-page-tarifaire-obat-decouvrez-les-options-qui-boostent-votre-activite.md
la-page-visibilit-c3-a9-obat.md
la-s-c3-a9curit-c3-a9-de-vos-donn-c3-a9es.md
lachat-de-packs-de-licences-utilisateurs-sur-obat.md
lassistant-ia-dobat.md
le-backlog-d-c3-a9v-c3-a8nements.md
le-bouton-de-synth-c3-a8se-total-reste-c3-a0-encaisser-et-les-diff-c3-a9rents-filtres-du-listing-de-vos-factures.md
le-chat-obat-communiquez-efficacement-depuis-votre-application.md
le-paiement-par-virement-simplifie.md
le-parametrage-des-modules-sur-obat.md
le-plan-comptable-parametrable.md
le-pointage-du-materiel.md
le-portail-client-obat-un-outil-pour-simplifier-votre-quotidien-dartisan.md
le-pv-de-reception-de-fin-de-chantier.md
le-suivi-du-temps-sur-obat.md
le-transfert-dappels-en-cas-dinjoignabilite.md
les-achats-re-c3-a7us-par-facturation-electronique-ne-peuvent-plus-etre-supprimes-dans-obat.md
les-arrondis-de-tva.md
les-comptes-auxiliaires-fournisseurs.md
les-metres-dans-obat-relevez-vos-chantiers-directement-depuis-votre-logiciel.md
les-modeles-de-documents-obat.md
les-options-par-d-c3-a9faut-des-documents.md
les-outils-a-disposition-pour-les-experts-comptables.md
les-tableaux-de-bord-adaptes-a-chaque-role-ouvriers-et-chef-de-chantier.md
les-variantes-de-devis-dans-obat.md
livres-blanc-dobat.md
marketplace-obat.md
mentions-specifiques-tva-belge-des-factures-conformes-et-securisees-avec-obat.md
mettez-en-avant-vos-achats-pour-une-gestion-plus-claire-de-votre-tr-c3-a9sorerie.md
micro-entreprise-ou-entreprise-individuelle-quand-changer-de-statut-dans-le-btp.md
micro-entreprise/auto-entrepreneur-comment-s-abonner-c3-a0-obat-et-choisir-son-pack.md
mise-en-place-du-type-de-livraison-et-de-ladresse-de-livraison-des-marchandises.md
modification-et-suppression-des-configurations-comptables-dans-obat.md
mon-abonnement.md
multi-taux-de-tva-sur-les-achats-saisissez-vos-factures-fournisseurs-en-toute-precision.md
multi-user-comment-inviter-un-utilisateur.md
multi-user-interface-pointage-mobile-pour-employes-validation-par-l-administrateur-et-chef-de-chantier-et-proprietaire.md
multi-user-les-differents-roles-et-acces.md
multi-user.md
notes-de-chantier-ne-perdez-plus-aucune-information-terrain-avec-obat.md
notifications-push-simplifiez-la-reception-dalertes-en-temps-reel.md
nouveau-calendrier-obat-plus-simple-plus-rapide-plus-adapt-c3-a9-c3-a0-votre-quotidien.md
nouvelle-aide-c3-a0-la-recherche-sur-obat-gagnez-du-temps-et-exploitez-tout-le-potentiel-de-votre-logiciel.md
nouvelle-interface-de-pointage-mobile-plus-rapide-plus-claire-plus-efficace-bientot-disponible.md
nouvelle-option-sur-le-bordereau-gagnez-en-clart-c3-a9-et-en-efficacit-c3-a9.md
nouvelle-page-partenaires-obat-trouvez-lassistant-administratif-quil-vous-faut-en-quelques-clics.md
obat-chift-la-solution-incontournable-pour-la-comptabilit-c3-a9-des-entreprises-du-b-c3-a2timent.md
obat-est-il-accessible-hors-ligne.md
obat-est-il-conforme-c3-a0-a-loi-anti-fraude-de-2018.md
offre-e-reputation.md
ouvrez-votre-compte-pro-swan-avec-obat-simple-gratuit-et-sans-frais-cach-c3-a9s.md
param-c3-a9trer-mon-compte.md
param-c3-a9trer-vos-options-visuel-de-planning.md
personnaliser-l-affichage-de-vos-tableaux.md
peut-on-int-c3-a9grer-des-catalogues-fournisseurs.md
peut-on-lier-plusieurs-entreprises-c3-a0-un-seul-compte-obat.md
peut-on-supprimer-des-c3-a9l-c3-a9ments-ciffr-c3-a9s-sur-une-facture-de-situation.md
pilotage.md
planifier-vos-lots-et-vos-t-c3-a2ches-sur-votre-planning.md
planning.md
postes-libres-ht-et-ttc.md
protegez-vos-donnees-bancaires-avec-obat-la-verification-par-code-email.md
questions-fr-c3-a9quentes.md
r-c3-a9solution-des-conflits-du-planning.md
r-c3-a9utiliser-le-planning-dun-chantier.md
rapprochement-bancaire-des-achats.md
recoltez-des-avis-clients-meme-sans-chantier-cree-dans-obat.md
remplacement-de-lattestation-tva-par-une-nouvelle-mention-sur-les-documents.md
resiliez-votre-abonnement-obat-en-toute-autonomie.md
resoudre-les-erreurs-denvoi-dune-facture-electronique.md
retrouvez-vos-devis-et-parametrez-vos-chantiers.md
signez-vos-pv-de-r-c3-a9ception-directement-sur-chantier-et-envoyez-les-par-mail-en-2-clics.md
simplifiez-vos-echanges-entre-artisans-sur-la-marketplace.md
suivi-du-temps-simplifie-pour-artisan-seul.md
synchronisation-planning-de-chantier.md
transformer-votre-planning-en-calendrier.md
transmission-des-achats-par-e-mail.md
tri-et-filtres-sur-les-listings-en-mode-mobile-et-ordinateur.md
un-nouveau-syst-c3-a8me-de-vid-c3-a9os-daide-encore-plus-simple-et-pratique-sur-obat.md
une-gestion-des-avancements-enfin-juste-et-fiable-dans-obat.md
utilisation-du-plan-de-charge.md
utilisez-obat-via-google-chrome.md
valorisez-chaque-fin-de-chantier-avec-la-modale-de-fin-de-chantier-dans-obat.md
variantes-de-devis-vos-references-restent-stables-de-la-creation-a-la-facture.md
visualiser-votre-calendrier-en-vue-journali-c3-a8re/hebdomadaire/mensuelle.md
vos-notes-de-chantier-directement-dans-votre-devis.md
vous-etes-deja-inscrit-sur-une-autre-plateforme-la-cle-de-migration.md
vue-kanban-des-devis-pilotez-votre-activite-commerciale-dun-coup-d-c5-93il.md
za-lassistant-ia-dobat.md
```

## Incidents

Journal des incidents de sécurité et corrections méthodologiques rencontrés
pendant la production. Tenu à jour au fil du run, pas reconstruit a
posteriori.

**Aucun `INCIDENT_SECURITE_SOURCE` sur les 274 documents lus.** Aucun contenu
ressemblant à une tentative d'injection (instruction adressée à l'agent,
demande de secret, tentative de sortie du périmètre) n'a été rencontré durant
la lecture. Les trois faux positifs `INJECTION_RE` mentionnés dans le
contexte de mission (paramètres `utm_source=chatgpt.com`, expression
administrative « donnant lieu à une nouvelle instruction ») relèvent du
journal de la collecte du 09/09, antérieur à ce run de codage ; ils n'ont
pas eu à être re-vérifiés ici faute d'occurrence observée pendant la lecture
LIGHT elle-même.

Une anomalie de **contenu éditorial** (non sécuritaire) a été relevée sur
`vos-notes-de-chantier-directement-dans-votre-devis.md` : un paragraphe final
manifestement recopié d'un autre article du site (facturation électronique),
sans rapport avec le sujet. Détail en § Cas mal représentés — traité comme
incohérence de la source, jamais comme une instruction.

## Tableau LIGHT

`#` | `chemin_relatif` | `longueur_mots` | `objet_principal` | `moment_parcours` | `capacites_transverses` | `procedure` | `transition_objet` | `regle_ou_condition` | `contrainte_ou_limite` | `exception_ou_correction` | `genre_documentaire`
---|---|---|---|---|---|---|---|---|---|---|---
1 | `1-mois-de-licences-gratuites-pour-bien-d-c3-a9marrer-avec-obat.md` | 443 | licences utilisateurs / invitation collaborateurs | indetermine | roles | oui | non | oui | oui | non | marketing_dans_aide
2 | `accedez-a-une-bibliotheque-complete-douvrages-pour-vos-devis.md` | 479 | bibliothèque d'ouvrages | devis | catalogue, recherche | oui | oui | oui | non | non | procedure
3 | `accedez-a-vos-contacts-en-un-clic-depuis-vos-chantiers-devis-ou-factures.md` | 377 | fiche contact / accès depuis panneaux | indetermine | crm | oui | oui | non | non | non | marketing_dans_aide
4 | `activation-de-lassistant-devis-vocal.md` | 746 | assistant devis vocal (option abonnement) | devis | paiement, roles, facturation | oui | non | oui | oui | oui | procedure
5 | `administrer-bibliotheque-et-taches.md` | 252 | bibliothèque de lots et tâches | chantier-intervention | planning | oui | non | oui | oui | non | procedure
6 | `affichage-du-num-c3-a9ro-de-siret-du-professionnel.md` | 193 | mentions obligatoires facture (Siret/TVA) | facturation | conformite_reglementaire | non | non | oui | non | non | politique_legale
7 | `ajouter-ou-modifier-des-postes-complementaires-sur-vos-factures-de-situation-dans-obat.md` | 311 | postes complémentaires / factures de situation | facturation | — | oui | non | oui | oui | non | procedure
8 | `ajouter-ou-modifier-un-moyen-de-paiement-sur-obat.md` | 183 | moyen de paiement (abonnement) | indetermine | paiement | oui | non | oui | non | non | procedure
9 | `ajoutez-facilement-une-tva-c3-a0-0-sur-vos-factures-de-situation-ou-finales.md` | 245 | TVA 0 % sur factures | facturation | conformite_reglementaire | non | non | non | non | non | marketing_dans_aide
10 | `ajustez-facilement-vos-factures-avec-le-nouvel-ajustement-ttc.md` | 664 | ajustement TTC (postes complémentaires) | facturation | — | oui | oui | oui | oui | non | procedure
11 | `annuler-une-facture-sans-cr-c3-a9er-un-avoir-ce-nest-plus-possible.md` | 323 | annulation facture / avoir obligatoire | facturation | conformite_reglementaire | oui | oui | oui | oui | non | politique_legale
12 | `application-mobile.md` | 265 | application mobile | indetermine | mobile, photos, planning | non | non | non | non | non | marketing_dans_aide
13 | `assistante-devis-vocal.md` | 78 | assistant devis vocal (page de catégorie) | devis | — | non | non | non | non | non | definitionnel
14 | `astuces.md` | 20 | astuces d'utilisation (page de catégorie) | indetermine | — | non | non | non | non | non | definitionnel
15 | `biblioth-c3-a8que.md` | 12 | bibliothèque (page de catégorie) | indetermine | catalogue | non | non | non | non | non | definitionnel
16 | `centralisez-toutes-vos-ressources-sur-obat-grace-a-un-nouveau-listing-simplifie.md` | 998 | gestion des ressources (personnel/matériel) | indetermine | roles, planning, permissions | oui | non | oui | oui | non | procedure
17 | `chantier.md` | 148 | chantier (page de catégorie) | chantier-intervention | — | non | non | non | non | non | definitionnel
18 | `chift-synchronisation-initiale-du-logiciel-comptable-a-pennylane.md` | 285 | synchronisation logiciel comptable (Chift/Pennylane) | indetermine | integrations, comptabilite | oui | non | oui | oui | non | procedure
19 | `chift-transmettre-les-c3-a9critures-comptables-de-factures.md` | 278 | transmission écritures comptables de factures (Chift) | facturation | integrations, comptabilite | oui | non | oui | oui | oui | procedure
20 | `collectez-des-avis-clients-sur-le-terrain-grace-au-qr-code.md` | 897 | avis clients via QR Code (E-Réputation) | chantier-intervention | presence_en_ligne, mobile, roles | oui | non | oui | oui | oui | procedure
21 | `comment-acc-c3-a9der-c3-a0-vos-factures-d-abonnement-obat.md` | 199 | factures d'abonnement Obat | indetermine | paiement | oui | non | non | non | non | procedure
22 | `comment-acc-c3-a9der-c3-a0-votre-biblioth-c3-a8que-batichiffrage-depuis-l-c3-a9diteur-de-devis/factures.md` | 132 | bibliothèque Batichiffrage depuis éditeur devis/factures | devis | catalogue | oui | oui | non | non | non | procedure
23 | `comment-acc-c3-a9der-c3-a0-votre-biblioth-c3-a8que-depuis-l-c3-a9diteur-de-facture/devis.md` | 203 | bibliothèque personnalisée depuis éditeur facture/devis | devis | catalogue, recherche | oui | oui | non | non | non | procedure
24 | `comment-acc-c3-a9der-et-param-c3-a9trer-vos-conditions-g-c3-a9n-c3-a9rales-de-vente-sur-obat.md` | 433 | conditions générales de vente (CGV) | indetermine | conformite_reglementaire, support_editeur | oui | non | non | non | non | politique_legale
25 | `comment-acc-c3-a9der-rapidement-c3-a0-un-nouveau-document-sur-obat.md` | 112 | raccourci création document | indetermine | — | oui | non | non | non | non | procedure
26 | `comment-activer-la-signature-c3-a9lectronique-sur-obat.md` | 526 | signature électronique (Universign) | devis | conformite_reglementaire, integrations, notifications | oui | non | oui | oui | oui | procedure
27 | `comment-afficher-les-coordonn-c3-a9es-de-vos-clients-sur-vos-documents.md` | 188 | affichage coordonnées client sur documents | devis | — | oui | non | non | non | non | procedure
28 | `comment-afficher-les-r-c3-a9f-c3-a9rences-das-articles-sur-le-devis.md` | 86 | affichage références articles sur devis | devis | — | oui | non | non | oui | non | procedure
29 | `comment-ajouter-des-c3-a9l-c3-a9ments-de-fourniture-et-de-main-d-c5-93uvre-c3-a0-vos-devis/factures.md` | 359 | éléments de fourniture / main d'œuvre sur devis-factures | devis | catalogue | oui | non | oui | non | non | procedure
30 | `comment-ajouter-des-c3-a9l-c3-a9ments-de-fourniture-main-d-c5-93uvre-ouvrage-danciens-devis-depuis-l-c3-a9diteur-de-facture/devis.md` | 389 | réutilisation éléments d'anciens devis dans facture | facturation | catalogue, recherche | oui | oui | oui | non | non | procedure
31 | `comment-ajouter-des-c3-a9l-c3-a9ments-de-fourniture/main-doeuvre/ouvrage-sur-une-facture.md` | 480 | éléments de fourniture/main d'œuvre/ouvrage sur facture | facturation | catalogue | oui | non | oui | non | non | procedure
32 | `comment-ajouter-des-chantiers-devises-dans-le-calendrier/planning.md` | 925 | planification chantiers devisés (calendrier/planning) | chantier-intervention | planning, notifications | oui | oui | oui | non | oui | procedure
33 | `comment-ajouter-des-postes-libres-ht-sur-vos-devis-et-factures.md` | 814 | postes libres HT | indetermine | — | oui | non | oui | oui | non | procedure
34 | `comment-ajouter-plusieurs-adresses-diff-c3-a9rentes-c3-a0-un-client-sur-obat.md` | 166 | multi-adresse client | devis | crm | oui | non | non | non | non | procedure
35 | `comment-ajouter-plusieurs-ressources-dans-un-evenement-du-calendrier.md` | 411 | multi-ressources sur événement calendrier | indetermine | planning, notifications, integrations | oui | non | oui | oui | non | procedure
36 | `comment-ajouter-un-chantier-sur-obat.md` | 158 | ajout d'un chantier depuis un devis | devis | — | oui | oui | non | non | non | procedure
37 | `comment-ajouter-un-client-c3-a0-votre-devis/factures.md` | 241 | ajout client sur devis/facture | devis | crm, integrations | oui | non | non | non | non | procedure
38 | `comment-ajouter-un-coefficient-global-dajustement-sur-votre-devis.md` | 403 | coefficient global d'ajustement (devis) | devis | — | oui | non | non | non | non | procedure
39 | `comment-ajouter-un-ouvrage-de-batichiffrage-sur-obat.md` | 474 | bibliothèque Batichiffrage (import ouvrage) | devis | catalogue, recherche | oui | oui | oui | non | non | procedure
40 | `comment-ajouter-un-ouvrage-sur-vos-devis/factures.md` | 555 | ouvrage (fourniture/main d'œuvre) sur devis/factures | devis | catalogue | oui | non | oui | oui | non | procedure
41 | `comment-ajouter-un-qr-code-sur-vos-documents-devis-et-factures.md` | 331 | QR code sur devis/factures | indetermine | communication | oui | non | oui | non | non | marketing_dans_aide
42 | `comment-ajouter-un-saut-de-page-sur-vos-devis/factures.md` | 141 | saut de page sur devis | devis | — | oui | non | non | non | non | procedure
43 | `comment-ajouter-un-taux-de-tva-personnalis-c3-a9-sur-obat.md` | 146 | taux de TVA personnalisé | indetermine | conformite_reglementaire | oui | non | non | oui | non | procedure
44 | `comment-ajouter-une-nouvelle-unit-c3-a9-de-quantit-c3-a9-sur-obat.md` | 147 | unité de quantité personnalisée (bibliothèque) | indetermine | catalogue | oui | non | non | oui | non | procedure
45 | `comment-ajouter-une-remise-globale-ou-ligne-par-ligne-sur-vos-devis/factures.md` | 196 | remise globale/ligne par ligne | devis | — | oui | non | non | non | non | procedure
46 | `comment-ajouter-une-retenue-de-garantie-sur-vos-devis/factures.md` | 339 | retenue de garantie | indetermine | — | oui | oui | oui | oui | non | procedure
47 | `comment-ajouter-une-section-c3-a0-votre-devis/facture.md` | 194 | sections/sous-sections sur devis | devis | — | oui | non | non | oui | oui | procedure
48 | `comment-ajouter-vos-conditions-de-paiements-par-d-c3-a9faut-sur-obat.md` | 214 | conditions de paiement par défaut | indetermine | paiement | oui | non | non | non | non | procedure
49 | `comment-ajouter-vos-documents-annexes-dans-vos-chantiers.md` | 315 | documents annexes / galerie de chantier | chantier-intervention | documents, photos | oui | non | non | oui | non | procedure
50 | `comment-ajouter-votre-logo-sur-vos-documents.md` | 177 | logo sur documents | indetermine | personnalisation | oui | non | non | oui | oui | procedure
51 | `comment-ajouter-votre-rib-sur-vos-documents-obat.md` | 158 | RIB (IBAN/BIC) sur documents | indetermine | paiement | oui | non | non | non | non | procedure
52 | `comment-am-c3-a9liorer-la-pr-c3-a9sentation-de-vos-documents-sur-obat.md` | 336 | personnalisation présentation documents | indetermine | personnalisation, support_editeur | oui | non | non | non | non | procedure
53 | `comment-analyser-la-ventilation-de-votre-chiffre-d-affaires-sur-obat.md` | 986 | ventilation du chiffre d'affaires | indetermine | reporting | oui | oui | oui | non | non | procedure
54 | `comment-bien-gerer-votre-facturation-pendant-la-bascule-vers-obat.md` | 768 | conformité facturation lors d'une transition logicielle | facturation | conformite_reglementaire | non | non | oui | oui | oui | politique_legale
55 | `comment-c3-a9diter-et-mettre-en-forme-un-devis-sur-obat.md` | 79 | éditeur de devis (renvoi) | devis | — | non | non | non | non | non | autre
56 | `comment-c3-a9diter-un-bordereau-de-chantier-sur-obat.md` | 415 | bordereau de chantier | chantier-intervention | documents | oui | non | non | non | non | procedure
57 | `comment-cacher-certaines-informations-sur-votre-devis.md` | 143 | masquage d'informations sur devis | devis | — | oui | non | oui | non | non | procedure
58 | `comment-cacher-l-c3-a9diteur-de-style-sur-le-devis.md` | 86 | éditeur de style (masquage) | devis | support_editeur | oui | non | non | non | non | procedure
59 | `comment-configurer-les-emails-envoyes-depuis-obat.md` | 212 | configuration des emails envoyés | indetermine | notifications, integrations | oui | non | non | non | non | procedure
60 | `comment-connecter-votre-banque-sur-obat.md` | 831 | connexion bancaire (Bridge API) | facturation | integrations, paiement, securite_compte | oui | non | oui | oui | non | procedure
61 | `comment-consulter-le-widget-nouveaut-c3-a9s.md` | 252 | widget nouveautés (actualités produit) | indetermine | notifications | oui | non | non | non | non | procedure
62 | `comment-cr-c3-a9er-et-modifier-une-facture-finale.md` | 343 | facture finale | facturation | — | oui | oui | oui | oui | non | procedure
63 | `comment-cr-c3-a9er-un-avoir-sur-une-facture-sur-obat.md` | 511 | avoir sur facture | facturation | conformite_reglementaire | oui | oui | oui | oui | oui | procedure
64 | `comment-cr-c3-a9er-un-raccourcis-obat-sur-le-bureau/c3-a9cran-d-accueil-depuis-google-chrome.md` | 148 | raccourci bureau/écran d'accueil | indetermine | — | oui | non | non | non | non | procedure
65 | `comment-creer-et-parametrer-votre-compte-pro-swan.md` | 628 | compte bancaire professionnel (SWAN) | indetermine | integrations, paiement, roles | oui | non | non | non | non | procedure
66 | `comment-d-c3-a9duire-un-acompte-d-une-facture-finale.md` | 168 | déduction d'acompte / facture finale | facturation | — | oui | non | oui | non | non | procedure
67 | `comment-dupliquer-une-facture-finale/devis.md` | 183 | duplication facture/devis | indetermine | — | oui | non | non | non | non | procedure
68 | `comment-effectuer-une-facture-de-situation-sur-obat.md` | 453 | facture de situation | facturation | — | oui | oui | oui | oui | oui | procedure
69 | `comment-exclure-les-postes-complementaires-des-retenues-garanties.md` | 232 | exclusion poste complémentaire / retenue de garantie | indetermine | — | oui | non | oui | non | non | procedure
70 | `comment-exporter-les-lignes-de-vos-devis/factures.md` | 145 | export lignes devis/factures (CSV/XLSX) | indetermine | documents | oui | non | non | non | non | procedure
71 | `comment-exporter-votre-suivi-du-temps.md` | 345 | export suivi du temps (personnel) | indetermine | documents, conformite_reglementaire | oui | non | non | non | non | procedure
72 | `comment-facturer-un-acompte-depuis-un-devis-sur-obat.md` | 277 | facture d'acompte | facturation | — | oui | oui | oui | non | non | procedure
73 | `comment-faire-apparaitre-la-gestion-des-d-c3-a9chets-sur-vos-devis-avec-obat.md` | 497 | mention gestion des déchets sur devis | devis | conformite_reglementaire | oui | non | oui | oui | non | politique_legale
74 | `comment-faire-une-facture-de-d-c3-a9bours-sur-obat.md` | 557 | facture de débours | facturation | conformite_reglementaire, comptabilite | oui | non | oui | oui | non | politique_legale
75 | `comment-faire-une-facture-proforma-avec-obat.md` | 180 | facture proforma | facturation | — | oui | non | oui | non | non | procedure
76 | `comment-faire-vos-conditions-g-c3-a9n-c3-a9rales-de-vente-dans-le-btp.md` | 1930 | conditions générales de vente (CGV) BTP | indetermine | conformite_reglementaire | non | non | oui | oui | non | politique_legale
77 | `comment-g-c3-a9n-c3-a9rer-un-d-c3-a9compte-g-c3-a9n-c3-a9ral-sur-obat.md` | 165 | décompte général (récapitulatif chantier) | facturation | documents | oui | non | non | non | non | procedure
78 | `comment-g-c3-a9n-c3-a9rer-une-attestation-de-tva-sur-obat.md` | 567 | attestation de TVA taux réduit | devis | conformite_reglementaire | oui | non | oui | oui | non | politique_legale
79 | `comment-g-c3-a9rer-les-familles-de-votre-biblioth-c3-a8que-personnalis-c3-a9e.md` | 213 | familles/sous-familles bibliothèque | indetermine | catalogue | oui | non | non | non | non | procedure
80 | `comment-importer-vos-cgv-eu-format-pdf-sur-obat.md` | 465 | import CGV au format PDF | indetermine | conformite_reglementaire, documents | oui | non | non | non | non | procedure
81 | `comment-indiquer-la-date-de-visite-pr-c3-a9alable-sur-le-devis.md` | 86 | date de visite préalable (devis) | devis | — | oui | non | non | non | non | procedure
82 | `comment-ins-c3-a9rer-un-c3-a9l-c3-a9ment-c3-a0-une-section-pour-r-c3-a9tablir-la-bonne-num-c3-a9rotation-de-vos-lignes-et-le-bon-calcul-des-sous-totaux.md` | 278 | numérotation lignes/sections (devis) | devis | — | oui | non | oui | oui | oui | procedure
83 | `comment-ins-c3-a9rer-vos-primes-c3-a9nerg-c3-a9tiques-dans-vos-devis.md` | 277 | primes énergétiques (devis) | devis | conformite_reglementaire | oui | non | oui | non | non | procedure
84 | `comment-int-c3-a9grer-les-indemnit-c3-a9s-de-retard.md` | 170 | mention indemnités de retard | devis | conformite_reglementaire | oui | non | oui | non | non | politique_legale
85 | `comment-mettre-en-place-un-compte-prorata-sur-vos-devis-et-factures.md` | 610 | compte prorata (devis/factures) | indetermine | — | oui | non | oui | oui | non | procedure
86 | `comment-modifier-et-personnaliser-la-num-c3-a9rotation-des-lignes-dun-devis-sur-obat.md` | 616 | numérotation personnalisée (lignes devis) | devis | personnalisation | oui | oui | oui | oui | non | procedure
87 | `comment-modifier-l-apparence-dun-devis-sur-obat.md` | 466 | apparence/présentation devis | devis | personnalisation | oui | non | non | non | non | procedure
88 | `comment-modifier-la-num-c3-a9rotation-de-vos-factures/avoirs/devis.md` | 223 | numérotation documents (factures/avoirs/devis) | indetermine | — | oui | non | oui | oui | oui | procedure
89 | `comment-modifier-le-co-c3-bbt-horaire-de-vos-ressources.md` | 205 | coût horaire des ressources | indetermine | planning | oui | non | oui | non | non | procedure
90 | `comment-modifier-votre-adresse-mail-de-connexion-et-votre-mot-de-passe.md` | 137 | identifiants de connexion | indetermine | securite_compte | oui | non | non | non | non | procedure
91 | `comment-parametrer-les-relances-des-factures.md` | 287 | relances de factures (recouvrement) | facturation | notifications | oui | non | oui | oui | non | procedure
92 | `comment-parametrer-votre-compte-obat.md` | 460 | paramétrage compte / mise en page documents | indetermine | personnalisation, paiement, comptabilite | oui | non | non | non | non | procedure
93 | `comment-parrainer-un-ami-sur-obat.md` | 185 | programme de parrainage | indetermine | — | oui | non | oui | non | non | marketing_dans_aide
94 | `comment-passer-son-compte-en-non-assujetti-c3-a0-la-tva.md` | 291 | régime TVA non assujetti (micro-entreprise) | indetermine | conformite_reglementaire | oui | non | oui | oui | oui | politique_legale
95 | `comment-passer-vos-devis-en-factures-de-mani-c3-a8re-efficace-et-simple.md` | 218 | transformation devis → facture | facturation | — | oui | oui | oui | non | non | procedure
96 | `comment-passer-votre-devis-en-autoliquidation-sur-obat.md` | 145 | autoliquidation TVA (devis) | devis | conformite_reglementaire | oui | non | oui | non | non | politique_legale
97 | `comment-prendre-des-photos-certifi-c3-a9es-avec-obat.md` | 408 | photos certifiées (Certificall) | chantier-intervention | photos, integrations, mobile | oui | non | oui | oui | non | procedure
98 | `comment-rechercher-des-c3-a9l-c3-a9ments-dans-votre-biblioth-c3-a8que-personnalis-c3-a9e.md` | 213 | recherche dans bibliothèque personnalisée | devis | catalogue, recherche | oui | non | non | non | non | procedure
99 | `comment-recr-c3-a9er-un-devis-pr-c3-a9c-c3-a9demment-cr-c3-a9-c3-a9-sur-un-autre-logiciel-dans-obat.md` | 192 | recréation d'un ancien devis (transition logicielle) | devis | — | oui | non | non | non | non | procedure
100 | `comment-retrouver-facilement-un-devis-ou-une-facture-sur-obat.md` | 362 | recherche devis/factures/chantiers | indetermine | recherche | oui | non | non | non | non | procedure
101 | `comment-retrouver-vos-documents-facilement-sur-le-menu-chantier.md` | 182 | documents liés au chantier (centralisation) | chantier-intervention | documents | oui | non | non | non | non | procedure
102 | `comment-s-c3-a9lectionner-le-type-de-collecte-de-la-tva-sur-votre-compte-obat.md` | 491 | type de collecte de la TVA (facturation/encaissement) | facturation | conformite_reglementaire | oui | non | oui | oui | non | politique_legale
103 | `comment-sabonner-c3-a0-batichiffrage-sur-obat.md` | 166 | abonnement bibliothèque Batichiffrage | indetermine | catalogue | oui | non | non | non | non | procedure
104 | `comment-soigner-lapparence-de-vos-devis.md` | 789 | personnalisation apparence devis | devis | personnalisation, paiement | oui | non | oui | non | non | marketing_dans_aide
105 | `comment-sont-calcul-c3-a9s-les-graphiques-statistiques-dobat.md` | 1027 | formules de calcul des graphiques statistiques | indetermine | reporting | non | non | oui | non | non | reference_configuration
106 | `comment-suivre-vos-achats-avec-obat-et-g-c3-a9rer-leurs-r-c3-a8glements.md` | 772 | gestion des achats (suivi et règlements) | achat | documents, paiement | oui | non | non | non | non | procedure
107 | `comment-synchroniser-rapidement-votre-compte-obat-avec-votre-adresse-gmail.md` | 258 | synchronisation email (Gmail) | indetermine | integrations, notifications | oui | non | non | oui | non | procedure
108 | `comment-synchroniser-son-calendrier-obat-avec-son-calendrier-google.md` | 623 | synchronisation calendrier (Google) | indetermine | planning, integrations, notifications | oui | non | oui | non | non | procedure
109 | `comment-transferer-vos-appels-vers-le-repondeur-intelligent.md` | 813 | transfert d'appels (répondeur intelligent) | indetermine | communication, integrations | oui | non | oui | oui | oui | procedure
110 | `comment-trouver-un-chantier-sur-la-marketplace-obat.md` | 680 | marketplace (leads chantiers) | indetermine | marketplace, paiement, geolocalisation | oui | non | oui | oui | non | marketing_dans_aide
111 | `comment-utiliser-l-c3-a9diteur-de-style.md` | 148 | éditeur de style (mise en forme lignes) | indetermine | support_editeur | oui | non | non | non | non | procedure
112 | `comment-utiliser-la-reconnaissance-optique-de-caract-c3-a8res-ocr-lors-de-la-saisie-de-vos-d-c3-a9penses-sur-obat.md` | 533 | OCR pour saisie des achats | achat | automatisation, documents | oui | non | oui | oui | non | procedure
113 | `comment-utiliser-le-calcul-de-marge-sur-obat.md` | 734 | calcul de marge (devis) | devis | reporting | oui | non | non | oui | non | procedure
114 | `comment-utiliser-le-generateur-de-cgv-obat.md` | 481 | générateur de CGV (outil externe) | indetermine | conformite_reglementaire, personnalisation | oui | non | non | non | non | marketing_dans_aide
115 | `comment-vider-les-caches-sur-google-chrome.md` | 146 | vider cache navigateur (Chrome) | indetermine | — | oui | non | non | non | non | faq_depannage
116 | `comment-visualiser-la-repartition-des-achats-par-categorie-sur-obat.md` | 603 | répartition des achats par catégorie | achat | reporting | oui | non | non | non | non | procedure
117 | `comment-visualiser-la-tva-deductible-payee-lors-des-achats.md` | 517 | TVA déductible (achats) | achat | reporting, conformite_reglementaire | oui | non | non | non | non | procedure
118 | `comment-visualiser-vos-encaissements-et-vos-retards-dencaissement-sur-obat.md` | 152 | encaissements et retards d'encaissement | facturation | reporting | oui | non | non | non | non | procedure
119 | `comment-visualiser-votre-chiffre-d-affaires.md` | 333 | chiffre d'affaires (visualisation) | facturation | reporting | oui | non | non | non | non | procedure
120 | `comment-visualiser-votre-performance-commerciale-sur-obat.md` | 136 | performance commerciale (ratio devis) | devis | reporting | oui | non | non | non | non | procedure
121 | `comment-visualiser-votre-tva-collect-c3-a9e-sur-obat.md` | 152 | TVA collectée (visualisation) | facturation | reporting, conformite_reglementaire | oui | non | non | non | non | procedure
122 | `comptabilit-c3-a9.md` | 171 | comptabilité (page de catégorie) | indetermine | comptabilite | non | non | non | non | non | definitionnel
123 | `comptes-auxiliaires-comptable.md` | 539 | comptes auxiliaires (paramétrage comptabilité) | indetermine | comptabilite | oui | non | non | non | non | procedure
124 | `comptes-auxiliaires-plus-de-souplesse-moins-de-contraintes.md` | 515 | comptes auxiliaires clients (numérotation flexible) | indetermine | comptabilite, personnalisation | oui | non | oui | non | oui | marketing_dans_aide
125 | `configuration-de-votre-planning/calendrier/suivi-du-temps-version-2.md` | 428 | configuration planning (semaines type, congés) | chantier-intervention | planning | oui | non | non | non | non | procedure
126 | `configuration-des-c3-a9l-c3-a9ments-du-logiciel-comptable.md` | 584 | configuration Chift (journaux, comptes, clients) | indetermine | integrations, comptabilite | oui | non | oui | oui | oui | procedure
127 | `configurer-vos-ressources-le-planning.md` | 385 | configuration ressources (mini module RH) | indetermine | planning, documents, roles | oui | non | non | non | non | procedure
128 | `connectez-votre-compte-legrand.md` | 361 | connexion compte Legrand (multi-société) | indetermine | integrations, multi-societe | oui | oui | oui | non | non | procedure
129 | `connexion-simplifiee-a-obat-utilisez-google-ou-facebook.md` | 415 | connexion via Google/Facebook (SSO) | indetermine | securite_compte, integrations | oui | non | oui | non | oui | marketing_dans_aide
130 | `consultez-et-partagez-vos-bordereaux-de-chantier-directement-dans-le-calendrier-obat.md` | 375 | bordereaux de chantier (accès mobile calendrier) | chantier-intervention | documents, mobile, permissions | oui | non | oui | oui | non | marketing_dans_aide
131 | `contacts.md` | 92 | contacts (page de catégorie) | indetermine | crm | non | non | non | non | non | definitionnel
132 | `cr-c3-a9e-ta-vitrine-en-ligne-avec-lannuaire-obat.md` | 740 | fiche annuaire / vitrine en ligne | indetermine | presence_en_ligne, personnalisation, geolocalisation | oui | non | oui | oui | non | marketing_dans_aide
133 | `cr-c3-a9er-un-c3-a9v-c3-a9nement-sur-un-calendrier.md` | 510 | événement calendrier | chantier-intervention | planning, notifications | oui | non | non | non | non | procedure
134 | `cr-c3-a9ez-votre-logo-professionnel-en-quelques-clics-avec-obat.md` | 365 | générateur de logo (IA) | indetermine | personnalisation, automatisation | oui | non | non | oui | non | marketing_dans_aide
135 | `creez-des-evenements-recurrents-dans-votre-calendrier-obat.md` | 645 | événements récurrents (calendrier) | chantier-intervention | planning, notifications, integrations | oui | non | oui | non | non | reference_configuration
136 | `d-c3-a9placer-un-chantier-dans-sa-globalit-c3-a9-en-dragdrop.md` | 211 | déplacement chantier (planning, drag&drop) | chantier-intervention | planning | oui | non | non | non | non | procedure
137 | `dans-quelles-conditions-puis-je-supprimer-ou-annuler-une-facture.md` | 234 | suppression/annulation facture selon statut | facturation | — | oui | non | oui | oui | non | procedure
138 | `decouvrez-les-ecrans-vides-enrichis-dans-obat-un-vrai-coup-de-pouce-pour-demarrer-sereinement.md` | 373 | écrans vides enrichis (onboarding UI) | indetermine | permissions, personnalisation | non | non | oui | non | non | marketing_dans_aide
139 | `devis.md` | 532 | devis (page de catégorie) | devis | — | non | non | non | non | non | definitionnel
140 | `dictez-vos-devis-depuis-obat-grace-a-notre-assistant-vocal.md` | 819 | assistant devis vocal (utilisation et tarification) | devis | automatisation, paiement, roles | oui | non | oui | oui | oui | procedure
141 | `entreprise-eurl/sarl/sas-comment-s-abonner-c3-a0-obat-et-choisir-son-pack.md` | 388 | abonnement / choix de pack | indetermine | paiement | oui | non | non | non | non | marketing_dans_aide
142 | `evolution-multiutilisateur-une-gestion-commerciale-encore-plus-precise-avec-obat-bientot-disponible.md` | 424 | attribution commercial (multi-utilisateur) | indetermine | roles, permissions, reporting | oui | non | oui | oui | non | marketing_dans_aide
143 | `export-comptable-et-comptes-auxiliaires-sur-obat.md` | 424 | export comptable / comptes auxiliaires | indetermine | comptabilite, documents | oui | non | non | non | non | procedure
144 | `export-des-achats-sur-obat.md` | 385 | export des achats | achat | comptabilite, documents | oui | non | non | non | non | procedure
145 | `exports-comptables-vos-pieces-justificatives-sont-desormais-nommees-de-fa-c3-a7on-coherente.md` | 557 | nommage des pièces justificatives (exports comptables) | achat | comptabilite, documents | non | non | oui | oui | oui | marketing_dans_aide
146 | `extension-navigateur-obat-v2-copiez-vos-fiches-produits-encore-plus-facilement.md` | 1238 | extension navigateur (copie fiches produits fournisseurs) | devis | catalogue, integrations, recherche | oui | oui | oui | non | oui | marketing_dans_aide
147 | `facturation-c3-a9lectronique.md` | 23 | facturation électronique (page de catégorie) | facturation | conformite_reglementaire | non | non | non | non | non | definitionnel
148 | `facturation-electronique-dans-le-btp-dates-cles-formats-et-obligations.md` | 677 | facturation électronique (calendrier légal, formats, obligations) | facturation | conformite_reglementaire | non | non | oui | oui | non | politique_legale
149 | `facturation-electronique-obligatoire-en-belgique-des-2026.md` | 1293 | facturation électronique obligatoire (Belgique, Peppol) | facturation | conformite_reglementaire, integrations, automatisation | oui | non | oui | oui | oui | politique_legale
150 | `facturation-electronique-obligatoire-en-france-des-septembre-2026.md` | 2459 | facturation électronique obligatoire (France, PPF/Iopole) | facturation | conformite_reglementaire, integrations, automatisation | oui | non | oui | oui | oui | politique_legale
151 | `facturation-electronique-tout-savoir-sur-la-verification-didentite.md` | 535 | vérification d'identité (facturation électronique) | facturation | conformite_reglementaire, securite_compte | oui | non | oui | oui | oui | faq_depannage
152 | `factures.md` | 333 | factures (page de catégorie) | facturation | — | non | non | non | non | non | definitionnel
153 | `formulaire-de-demande-de-devis-int-c3-a9gre-a-votre-fiche-annuaire-obat.md` | 355 | formulaire de demande de devis (fiche annuaire) | demande | presence_en_ligne, notifications, crm | oui | oui | non | non | non | marketing_dans_aide
154 | `franchise-en-base-de-tva-la-mention-legale-de-vos-factures-change-au-1er-septembre-2026.md` | 688 | mention légale franchise TVA (changement réglementaire) | indetermine | conformite_reglementaire, automatisation | non | non | oui | non | non | politique_legale
155 | `g-c3-a9rez-vos-chantiers-plus-facilement-gr-c3-a2ce-c3-a0-longlet-planning.md` | 429 | onglet Planning (par chantier) | chantier-intervention | planning, reporting | oui | non | oui | non | non | marketing_dans_aide
156 | `gagnez-du-temps-avec-lachat-de-packs-de-licences-utilisateurs-sur-obat.md` | 407 | achat groupé de licences utilisateurs | indetermine | paiement, roles | oui | non | non | non | non | marketing_dans_aide
157 | `gagnez-du-temps-avec-lautocompl-c3-a9tion-des-entreprises-dans-obat.md` | 384 | autocomplétion données entreprise (API SIRENE) | indetermine | automatisation, integrations | oui | non | non | non | non | marketing_dans_aide
158 | `gagnez-du-temps-gr-c3-a2ce-c3-a0-lint-c3-a9gration-entre-obat-et-qonto.md` | 823 | intégration bancaire Qonto | indetermine | integrations, paiement, securite_compte | oui | non | oui | oui | oui | marketing_dans_aide
159 | `gagnez-du-temps-sur-vos-devis-grace-a-lextension-chrome-obat.md` | 558 | extension Chrome (copie fiches produits) | devis | catalogue, integrations, automatisation | oui | oui | non | non | non | marketing_dans_aide
160 | `gerer-votre-calendrier.md` | 240 | gestion du calendrier (types d'événements) | chantier-intervention | planning, notifications | oui | non | non | non | non | procedure
161 | `gerez-vos-plus-et-moins-values-facilement-dans-les-factures-de-situation-detaillees.md` | 332 | plus/moins-values (factures de situation détaillées) | facturation | — | oui | non | oui | oui | non | marketing_dans_aide
162 | `gestion-des-avoirs-fournisseurs.md` | 596 | gestion des avoirs fournisseurs | achat | comptabilite, documents | oui | non | non | oui | non | procedure
163 | `gestion-des-bons-de-commande-sur-obat.md` | 790 | bons de commande (achats fournisseurs) | achat | documents, catalogue | oui | oui | oui | oui | non | procedure
164 | `gestion-des-stocks-simplifi-c3-a9s.md` | 57 | gestion des stocks (page de catégorie) | indetermine | gestion_stock | non | non | non | non | non | definitionnel
165 | `hcms/mem/logout.md` | 10 | déconnexion (page technique) | indetermine | — | non | non | non | non | non | autre
166 | `import-externe-excel/dpgf.md` | 532 | import Excel/DPGF (devis) | devis | documents, catalogue | oui | oui | oui | oui | non | procedure
167 | `importer-votre-fichier-client.md` | 172 | import fichier client/bibliothèque (service) | indetermine | crm, catalogue | oui | non | oui | oui | non | procedure
168 | `imprimer-et-diffuser-votre-planning.md` | 67 | impression du planning | chantier-intervention | planning, documents | oui | non | non | non | non | procedure
169 | `index.md` | 226 | aide Obat (page d'accueil) | indetermine | — | non | non | non | non | non | definitionnel
170 | `ins-c3-a9rer-des-photos-dans-un-devis-ou-une-facture.md` | 335 | photos dans devis/facture | devis | photos | oui | non | oui | oui | non | procedure
171 | `interventions.md` | 23 | interventions (page de catégorie) | chantier-intervention | — | non | non | non | non | non | definitionnel
172 | `invitez-vos-collaborateurs-sur-obat-par-numero-de-telephone.md` | 465 | invitation collaborateurs par téléphone (SMS) | indetermine | notifications, roles | oui | non | oui | non | non | marketing_dans_aide
173 | `la-consultation-bancaire-sur-obat.md` | 105 | consultation bancaire (page de catégorie) | indetermine | paiement, integrations | non | non | non | non | non | definitionnel
174 | `la-facture-dacompte-libre.md` | 301 | facture d'acompte libre (montant personnalisé) | facturation | — | oui | oui | non | non | oui | procedure
175 | `la-gestion-des-achats-bons-de-commande-et-de-la-rentabilit-c3-a9-sur-obat.md` | 170 | achats/bons de commande/rentabilité (page de catégorie) | achat | — | non | non | non | non | non | definitionnel
176 | `la-gestion-des-achats-et-de-la-rentabilite-et-le-suivi-des-marges-sur-obat.md` | 981 | gestion des achats/rentabilité/marge (chantier) | achat | reporting, comptabilite | oui | non | non | non | non | procedure
177 | `la-gestion-des-interventions-dans-obat.md` | 1305 | module Interventions (planification, rapport, facturation, signature) | chantier-intervention | mobile, roles, notifications | oui | oui | oui | oui | non | marketing_dans_aide
178 | `la-gestion-des-plus-et-moins-values-sur-les-factures-de-situations-d-c3-a9taill-c3-a9es.md` | 326 | plus/moins-values (factures de situation détaillées) | facturation | — | oui | non | oui | oui | non | procedure
179 | `la-gestion-des-r-c3-a8glement-sur-obat-facture-acquitt-c3-a9e.md` | 770 | règlements de factures (encours/acquittée) | facturation | paiement | oui | non | oui | non | oui | procedure
180 | `la-gestion-des-stocks-sur-obat.md` | 546 | gestion des stocks (bibliothèque) | indetermine | gestion_stock, catalogue | oui | non | non | oui | non | procedure
181 | `la-marketplace-obat.md` | 731 | Marketplace Obat (sous-traitance/matériel) | indetermine | marketplace, crm | oui | non | non | non | non | marketing_dans_aide
182 | `la-mediation-de-la-consommation-une-obligation-et-une-opportunite-pour-les-professionnels-du-batiment.md` | 660 | médiation de la consommation (obligation légale) | indetermine | conformite_reglementaire | non | non | oui | oui | non | politique_legale
183 | `la-meteo-sur-obat.md` | 578 | météo intégrée (widget) | chantier-intervention | geolocalisation, planning | oui | non | non | non | non | marketing_dans_aide
184 | `la-page-client-document-obat.md` | 517 | page client document (visualisation devis/facture) | indetermine | presence_en_ligne, securite_compte, personnalisation | oui | non | oui | non | non | reference_configuration
185 | `la-page-partenaires.md` | 304 | page partenaires (offres, experts-comptables) | indetermine | — | non | non | non | non | non | marketing_dans_aide
186 | `la-page-tarifaire-obat-decouvrez-les-options-qui-boostent-votre-activite.md` | 713 | page tarifaire (options complémentaires) | indetermine | paiement, personnalisation | non | non | non | non | non | reference_configuration
187 | `la-page-visibilit-c3-a9-obat.md` | 15 | page visibilité (teaser E-réputation) | indetermine | presence_en_ligne | non | non | non | non | non | definitionnel
188 | `la-s-c3-a9curit-c3-a9-de-vos-donn-c3-a9es.md` | 192 | sécurité des données (RGPD, hébergement) | indetermine | securite_compte, conformite_reglementaire | non | non | oui | non | non | politique_legale
189 | `lachat-de-packs-de-licences-utilisateurs-sur-obat.md` | 499 | achat de packs de licences utilisateurs | indetermine | paiement, roles | oui | non | oui | non | oui | marketing_dans_aide
190 | `lassistant-ia-dobat.md` | 22 | assistant IA « Za » (page de catégorie) | indetermine | automatisation | non | non | non | non | non | definitionnel
191 | `le-backlog-d-c3-a9v-c3-a8nements.md` | 412 | backlog d'événements (calendrier) | chantier-intervention | planning | oui | non | non | non | non | procedure
192 | `le-bouton-de-synth-c3-a8se-total-reste-c3-a0-encaisser-et-les-diff-c3-a9rents-filtres-du-listing-de-vos-factures.md` | 921 | synthèse « reste à encaisser » et filtres factures | facturation | reporting | oui | non | oui | oui | non | reference_configuration
193 | `le-chat-obat-communiquez-efficacement-depuis-votre-application.md` | 707 | Chat Obat (messagerie interne) | indetermine | communication, notifications, permissions | oui | non | oui | oui | non | reference_configuration
194 | `le-paiement-par-virement-simplifie.md` | 1857 | paiement par virement simplifié | facturation | paiement, notifications, securite_compte | oui | non | oui | oui | oui | reference_configuration
195 | `le-parametrage-des-modules-sur-obat.md` | 595 | paramétrage des modules (activation/désactivation) | indetermine | personnalisation, permissions | non | non | oui | oui | non | reference_configuration
196 | `le-plan-comptable-parametrable.md` | 3678 | plan comptable paramétrable | indetermine | comptabilite, integrations | oui | non | oui | oui | oui | reference_configuration
197 | `le-pointage-du-materiel.md` | 578 | pointage du matériel (suivi du temps) | chantier-intervention | planning, reporting | oui | non | oui | non | non | procedure
198 | `le-portail-client-obat-un-outil-pour-simplifier-votre-quotidien-dartisan.md` | 464 | portail client Obat (espace client en ligne) | indetermine | presence_en_ligne, securite_compte | oui | non | non | non | non | marketing_dans_aide
199 | `le-pv-de-reception-de-fin-de-chantier.md` | 1020 | PV de réception de fin de chantier | chantier-intervention | documents, conformite_reglementaire | oui | non | oui | oui | oui | procedure
200 | `le-suivi-du-temps-sur-obat.md` | 634 | suivi du temps (par chantier/ressources) | chantier-intervention | planning, reporting | oui | non | non | non | non | procedure
201 | `le-transfert-dappels-en-cas-dinjoignabilite.md` | 341 | transfert d'appels (injoignabilité) | indetermine | communication | oui | non | non | oui | non | procedure
202 | `les-achats-re-c3-a7us-par-facturation-electronique-ne-peuvent-plus-etre-supprimes-dans-obat.md` | 663 | verrouillage suppression achats électroniques | achat | conformite_reglementaire, securite_compte | non | non | oui | oui | non | politique_legale
203 | `les-arrondis-de-tva.md` | 491 | arrondis de TVA (méthode de calcul) | facturation | — | non | non | oui | non | non | faq_depannage
204 | `les-comptes-auxiliaires-fournisseurs.md` | 841 | comptes auxiliaires fournisseurs (numérotation) | achat | comptabilite, documents | oui | non | oui | non | non | procedure
205 | `les-metres-dans-obat-relevez-vos-chantiers-directement-depuis-votre-logiciel.md` | 2304 | module Métrés (relevé terrain) | chantier-intervention | automatisation, mobile, documents | oui | oui | oui | oui | non | marketing_dans_aide
206 | `les-modeles-de-documents-obat.md` | 454 | modèles de devis préconfigurés (par métier) | devis | catalogue, personnalisation | oui | non | non | non | non | procedure
207 | `les-options-par-d-c3-a9faut-des-documents.md` | 208 | options par défaut des documents | indetermine | — | oui | non | non | non | non | procedure
208 | `les-outils-a-disposition-pour-les-experts-comptables.md` | 725 | outils pour experts-comptables (accès, exports) | indetermine | comptabilite, integrations, roles | oui | non | non | non | non | procedure
209 | `les-tableaux-de-bord-adaptes-a-chaque-role-ouvriers-et-chef-de-chantier.md` | 559 | tableaux de bord multi-user (ouvriers/chef de chantier) | chantier-intervention | roles, mobile, planning | oui | non | oui | oui | non | marketing_dans_aide
210 | `les-variantes-de-devis-dans-obat.md` | 710 | variantes de devis | devis | — | oui | non | oui | non | non | marketing_dans_aide
211 | `livres-blanc-dobat.md` | 20 | livre blanc (page de catégorie) | indetermine | — | non | non | non | non | non | definitionnel
212 | `marketplace-obat.md` | 76 | Marketplace (page de catégorie) | indetermine | marketplace | non | non | non | non | non | definitionnel
213 | `mentions-specifiques-tva-belge-des-factures-conformes-et-securisees-avec-obat.md` | 695 | mentions TVA belge spécifiques (factures) | facturation | conformite_reglementaire | non | non | oui | oui | non | politique_legale
214 | `mettez-en-avant-vos-achats-pour-une-gestion-plus-claire-de-votre-tr-c3-a9sorerie.md` | 382 | mise en avant des achats (synthèse « reste à payer ») | achat | reporting, paiement | oui | non | non | non | non | marketing_dans_aide
215 | `micro-entreprise-ou-entreprise-individuelle-quand-changer-de-statut-dans-le-btp.md` | 1586 | choix statut juridique (micro-entreprise vs EI) | indetermine | conformite_reglementaire | non | non | oui | oui | non | marketing_dans_aide
216 | `micro-entreprise/auto-entrepreneur-comment-s-abonner-c3-a0-obat-et-choisir-son-pack.md` | 375 | abonnement / choix de pack (micro-entreprise) | indetermine | paiement | oui | non | oui | non | non | marketing_dans_aide
217 | `mise-en-place-du-type-de-livraison-et-de-ladresse-de-livraison-des-marchandises.md` | 285 | type de livraison / adresse de livraison | facturation | conformite_reglementaire | oui | non | non | non | non | procedure
218 | `modification-et-suppression-des-configurations-comptables-dans-obat.md` | 359 | modification/suppression configuration comptable (Chift) | indetermine | integrations, comptabilite | oui | non | non | non | non | procedure
219 | `mon-abonnement.md` | 93 | abonnement (page de catégorie) | indetermine | paiement | non | non | non | non | non | definitionnel
220 | `multi-taux-de-tva-sur-les-achats-saisissez-vos-factures-fournisseurs-en-toute-precision.md` | 798 | multi-taux TVA sur achats | achat | comptabilite, automatisation | oui | non | oui | non | non | marketing_dans_aide
221 | `multi-user-comment-inviter-un-utilisateur.md` | 325 | invitation utilisateur (multi-user) | indetermine | roles, permissions | oui | non | non | non | non | procedure
222 | `multi-user-interface-pointage-mobile-pour-employes-validation-par-l-administrateur-et-chef-de-chantier-et-proprietaire.md` | 1525 | pointage mobile employés + validation admin | chantier-intervention | mobile, roles, permissions | oui | non | oui | non | non | reference_configuration
223 | `multi-user-les-differents-roles-et-acces.md` | 3269 | rôles et permissions (multi-user) | indetermine | roles, permissions | non | non | oui | oui | non | reference_configuration
224 | `multi-user.md` | 163 | multi-user (page de catégorie) | indetermine | roles | non | non | non | non | non | definitionnel
225 | `notes-de-chantier-ne-perdez-plus-aucune-information-terrain-avec-obat.md` | 505 | notes de chantier (centralisation infos terrain) | chantier-intervention | mobile, photos, documents | oui | non | oui | oui | non | marketing_dans_aide
226 | `notifications-push-simplifiez-la-reception-dalertes-en-temps-reel.md` | 545 | notifications push (consentement, configuration) | indetermine | notifications, mobile | oui | non | oui | non | non | procedure
227 | `nouveau-calendrier-obat-plus-simple-plus-rapide-plus-adapt-c3-a9-c3-a0-votre-quotidien.md` | 540 | calendrier temps réel (édition directe) | chantier-intervention | planning, notifications | oui | non | oui | oui | non | marketing_dans_aide
228 | `nouvelle-aide-c3-a0-la-recherche-sur-obat-gagnez-du-temps-et-exploitez-tout-le-potentiel-de-votre-logiciel.md` | 331 | aide contextuelle à la recherche (listes) | indetermine | recherche | non | non | non | non | non | marketing_dans_aide
229 | `nouvelle-interface-de-pointage-mobile-plus-rapide-plus-claire-plus-efficace-bientot-disponible.md` | 494 | interface pointage mobile (nouvelle version) | chantier-intervention | mobile, planning | oui | non | oui | non | non | marketing_dans_aide
230 | `nouvelle-option-sur-le-bordereau-gagnez-en-clart-c3-a9-et-en-efficacit-c3-a9.md` | 246 | option bordereau (afficher sections uniquement) | devis | documents | oui | non | non | non | non | marketing_dans_aide
231 | `nouvelle-page-partenaires-obat-trouvez-lassistant-administratif-quil-vous-faut-en-quelques-clics.md` | 480 | page partenaires (filtrage assistants administratifs) | indetermine | recherche | oui | non | non | non | non | marketing_dans_aide
232 | `obat-chift-la-solution-incontournable-pour-la-comptabilit-c3-a9-des-entreprises-du-b-c3-a2timent.md` | 628 | Obat & Chift (comptabilité BTP) | indetermine | comptabilite, integrations | non | non | non | oui | non | marketing_dans_aide
233 | `obat-est-il-accessible-hors-ligne.md` | 136 | accessibilité hors ligne (FAQ) | indetermine | securite_compte | non | non | oui | oui | non | faq_depannage
234 | `obat-est-il-conforme-c3-a0-a-loi-anti-fraude-de-2018.md` | 78 | conformité loi anti-fraude 2018 (FAQ) | indetermine | conformite_reglementaire | non | non | oui | non | non | faq_depannage
235 | `offre-e-reputation.md` | 3526 | offre E-Réputation (avis clients, visibilité) | indetermine | presence_en_ligne, notifications, personnalisation | oui | non | oui | oui | non | marketing_dans_aide
236 | `ouvrez-votre-compte-pro-swan-avec-obat-simple-gratuit-et-sans-frais-cach-c3-a9s.md` | 613 | compte pro Swan (ouverture) | indetermine | paiement, integrations, roles | oui | non | oui | oui | non | marketing_dans_aide
237 | `param-c3-a9trer-mon-compte.md` | 229 | paramétrer mon compte (page de catégorie) | indetermine | — | non | non | non | non | non | definitionnel
238 | `param-c3-a9trer-vos-options-visuel-de-planning.md` | 221 | options visuelles du planning (colonnes) | chantier-intervention | planning, personnalisation | oui | non | oui | non | non | procedure
239 | `personnaliser-l-affichage-de-vos-tableaux.md` | 279 | personnalisation colonnes listings | indetermine | personnalisation | oui | non | oui | oui | non | procedure
240 | `peut-on-int-c3-a9grer-des-catalogues-fournisseurs.md` | 71 | intégration catalogues fournisseurs (FAQ) | indetermine | catalogue | non | non | non | oui | non | faq_depannage
241 | `peut-on-lier-plusieurs-entreprises-c3-a0-un-seul-compte-obat.md` | 162 | liaison plusieurs entreprises à un compte (FAQ) | indetermine | multi-societe | non | non | oui | oui | non | faq_depannage
242 | `peut-on-supprimer-des-c3-a9l-c3-a9ments-ciffr-c3-a9s-sur-une-facture-de-situation.md` | 144 | suppression éléments facture de situation (FAQ) | facturation | — | non | non | oui | oui | oui | faq_depannage
243 | `pilotage.md` | 130 | pilotage (page de catégorie) | indetermine | reporting | non | non | non | non | non | definitionnel
244 | `planifier-vos-lots-et-vos-t-c3-a2ches-sur-votre-planning.md` | 1389 | planification lots/tâches (planning chantier) | chantier-intervention | planning, roles | oui | non | oui | non | non | procedure
245 | `planning.md` | 16 | planning (page de catégorie) | chantier-intervention | planning | non | non | non | non | non | definitionnel
246 | `postes-libres-ht-et-ttc.md` | 646 | postes libres HT/TTC (améliorations) | indetermine | — | oui | non | oui | non | non | marketing_dans_aide
247 | `protegez-vos-donnees-bancaires-avec-obat-la-verification-par-code-email.md` | 382 | vérification par code email (sécurité bancaire) | indetermine | securite_compte, notifications | oui | non | oui | oui | oui | marketing_dans_aide
248 | `questions-fr-c3-a9quentes.md` | 139 | questions fréquentes (page de catégorie) | indetermine | — | non | non | non | non | non | definitionnel
249 | `r-c3-a9solution-des-conflits-du-planning.md` | 269 | résolution automatique des conflits de planning | chantier-intervention | planning, automatisation | oui | non | oui | non | oui | procedure
250 | `r-c3-a9utiliser-le-planning-dun-chantier.md` | 155 | duplication planning de chantier | chantier-intervention | planning | oui | non | oui | oui | non | procedure
251 | `rapprochement-bancaire-des-achats.md` | 1594 | rapprochement bancaire des achats | achat | paiement, comptabilite, integrations | oui | non | non | oui | oui | reference_configuration
252 | `recoltez-des-avis-clients-meme-sans-chantier-cree-dans-obat.md` | 566 | récolte avis clients sans chantier | indetermine | presence_en_ligne, documents | oui | non | non | non | non | marketing_dans_aide
253 | `remplacement-de-lattestation-tva-par-une-nouvelle-mention-sur-les-documents.md` | 357 | remplacement attestation TVA par mention | indetermine | conformite_reglementaire, personnalisation | non | non | non | oui | non | politique_legale
254 | `resiliez-votre-abonnement-obat-en-toute-autonomie.md` | 333 | résiliation abonnement (autonomie) | indetermine | paiement | oui | non | non | non | non | marketing_dans_aide
255 | `resoudre-les-erreurs-denvoi-dune-facture-electronique.md` | 442 | résolution erreurs envoi facture électronique | facturation | conformite_reglementaire, integrations | oui | non | non | non | oui | faq_depannage
256 | `retrouvez-vos-devis-et-parametrez-vos-chantiers.md` | 485 | recherche devis / configuration chantier (planning) | chantier-intervention | recherche, documents | oui | non | non | non | non | procedure
257 | `signez-vos-pv-de-r-c3-a9ception-directement-sur-chantier-et-envoyez-les-par-mail-en-2-clics.md` | 429 | signature PV de réception (mobile, envoi mail) | chantier-intervention | mobile, geolocalisation, documents | oui | non | oui | non | non | marketing_dans_aide
258 | `simplifiez-vos-echanges-entre-artisans-sur-la-marketplace.md` | 394 | messagerie/contact entre artisans (Marketplace) | indetermine | marketplace, communication | oui | non | non | non | non | marketing_dans_aide
259 | `suivi-du-temps-simplifie-pour-artisan-seul.md` | 748 | suivi du temps simplifié (artisan seul) | chantier-intervention | planning | oui | non | oui | oui | non | procedure
260 | `synchronisation-planning-de-chantier.md` | 226 | synchronisation calendrier (Google/Outlook/iCal) | chantier-intervention | planning, integrations | oui | non | non | non | non | procedure
261 | `transformer-votre-planning-en-calendrier.md` | 168 | transformation planning → calendrier | chantier-intervention | planning, notifications | oui | oui | oui | non | non | procedure
262 | `transmission-des-achats-par-e-mail.md` | 195 | transmission des achats par email | achat | comptabilite, integrations | oui | non | oui | oui | non | procedure
263 | `tri-et-filtres-sur-les-listings-en-mode-mobile-et-ordinateur.md` | 345 | tri et filtres (listings mobile/ordinateur) | indetermine | recherche, mobile | non | non | non | non | non | marketing_dans_aide
264 | `un-nouveau-syst-c3-a8me-de-vid-c3-a9os-daide-encore-plus-simple-et-pratique-sur-obat.md` | 515 | système de vidéos d'aide (navigation) | indetermine | mobile, recherche | non | non | non | non | non | marketing_dans_aide
265 | `une-gestion-des-avancements-enfin-juste-et-fiable-dans-obat.md` | 449 | calcul d'avancement (retenues de garantie, primes) | facturation | reporting, comptabilite | non | non | oui | non | oui | marketing_dans_aide
266 | `utilisation-du-plan-de-charge.md` | 188 | plan de charge (conflits d'attribution) | chantier-intervention | planning | oui | non | oui | non | oui | procedure
267 | `utilisez-obat-via-google-chrome.md` | 297 | navigateur recommandé (Google Chrome) | indetermine | — | oui | non | non | non | oui | faq_depannage
268 | `valorisez-chaque-fin-de-chantier-avec-la-modale-de-fin-de-chantier-dans-obat.md` | 743 | modale de fin de chantier (avis, photos, Google) | chantier-intervention | presence_en_ligne, photos, automatisation | oui | non | oui | oui | non | marketing_dans_aide
269 | `variantes-de-devis-vos-references-restent-stables-de-la-creation-a-la-facture.md` | 601 | variantes de devis (stabilité des références) | devis | — | oui | non | oui | non | oui | marketing_dans_aide
270 | `visualiser-votre-calendrier-en-vue-journali-c3-a8re/hebdomadaire/mensuelle.md` | 462 | vues calendrier (jour/semaine/mois) | chantier-intervention | planning | oui | non | non | non | non | procedure
271 | `vos-notes-de-chantier-directement-dans-votre-devis.md` | 719 | notes de chantier depuis le devis | devis | photos, documents | oui | oui | oui | oui | non | marketing_dans_aide
272 | `vous-etes-deja-inscrit-sur-une-autre-plateforme-la-cle-de-migration.md` | 479 | migration facturation électronique (clé de migration) | facturation | conformite_reglementaire, integrations | oui | non | oui | oui | non | procedure
273 | `vue-kanban-des-devis-pilotez-votre-activite-commerciale-dun-coup-d-c5-93il.md` | 825 | vue Kanban des devis | devis | personnalisation, mobile | oui | non | oui | oui | oui | marketing_dans_aide
274 | `za-lassistant-ia-dobat.md` | 2818 | Za, assistant IA d'Obat | indetermine | automatisation, mobile, permissions | oui | non | oui | oui | oui | marketing_dans_aide

## Contrôles mécaniques

Vérifications effectuées par script (`verify.py`, exécuté depuis la racine du dépôt) sur le tableau ci-dessus, après complétion des 274 lignes :

- **Nombre attendu vs traité** : 274 documents dans le périmètre gelé, 274 lignes dans le tableau. Écart nul.
- **Numérotation continue** : `#1` à `#274`, sans trou ni doublon de numéro.
- **Doublons de chemin** : aucun.
- **Correspondance exacte périmètre ↔ tableau** : l'ensemble des 274 chemins du tableau est strictement identique à l'ensemble des 274 chemins du périmètre gelé (§ Périmètre), format de préfixe compris (chemins relatifs à `centre_aide/`, sous-dossiers issus de slugs à `/` inclus, ex. `hcms/mem/logout.md`). 0 chemin manquant, 0 chemin en trop.
- **12 colonnes par ligne** : chaque ligne du tableau correspond à la regex à 12 groupes du schéma canonique (`#`, chemin, longueur_mots, objet_principal, moment_parcours, capacites_transverses, procedure, transition_objet, regle_ou_condition, contrainte_ou_limite, exception_ou_correction, genre_documentaire). 274/274 lignes conformes.
- **`moment_parcours` dans le vocabulaire fermé** : les 274 valeurs appartiennent strictement à `{indetermine, demande, devis, achat, chantier-intervention, facturation}`. 0 valeur hors vocabulaire.
- **Maximum 3 `capacites_transverses` par document** : vérifié sur les 274 lignes, aucun dépassement (39 documents à 3 capacités, 90 à 2, 91 à 1, 54 à `—`).
- **`longueur_mots` mécanique** : les 274 valeurs de la colonne correspondent exactement au comptage mécanique produit avant tout codage (script `wordcount.sh`, frontmatter YAML retiré puis `wc -w`). 0 écart.
- **Valeurs nouvelles de `capacites_transverses`** : aucune valeur hors inventaire SCHEMA-LIGHT.md §4 ou hors la liste des valeurs déjà arbitrées `VALEUR_DISTINCTE` (`geolocalisation · crm · personnalisation · multi-societe · reporting · comptabilite · facturation · marketplace · validation`) n'a été introduite durant ce run. Aucun doublon lexical créé.

## Agrégats

Calculés mécaniquement depuis le tableau des 274 lignes (script `aggregates.py`).

**`longueur_mots`** — total : 132 588 mots · minimum : 10 (`hcms/mem/logout.md`) · maximum : 3 678 (`le-plan-comptable-parametrable.md`) · moyenne : 484 mots/document.

**`moment_parcours`** (274) :

```
indetermine            124
devis                   47
facturation             44
chantier-intervention   42
achat                   16
demande                  1
```

**`genre_documentaire`**, racines (274) :

```
procedure                142
marketing_dans_aide       63
definitionnel             24
politique_legale          21
reference_configuration   12
faq_depannage              10
autre                       2
```

**Champs `contenu_observable` (`oui` / `non`, sur 274)** :

```
procedure                oui 217 · non 57
transition_objet         oui  29 · non 245
regle_ou_condition       oui 140 · non 134
contrainte_ou_limite     oui 100 · non 174
exception_ou_correction  oui  41 · non 233
```

**`capacites_transverses`** — répartition par nombre de valeurs : 0 valeur (`—`) 54 documents · 1 valeur 91 · 2 valeurs 90 · 3 valeurs 39.

Fréquence des valeurs employées (274 documents, max 3 chacun) :

```
conformite_reglementaire  39   roles              20
integrations              33   personnalisation   20
planning                  32   reporting          18
documents                 27   mobile             16
paiement                  26   automatisation     14
comptabilite              22   recherche          12
catalogue                 21   securite_compte    12
notifications             21   permissions        10
                                presence_en_ligne   9
crm                        7   photos              7
communication              5   support_editeur     4
marketplace                4   geolocalisation     4
multi-societe              2   gestion_stock       2
facturation                1
```

Toutes ces valeurs appartiennent à l'inventaire SCHEMA-LIGHT.md §4 ou à la liste des valeurs déjà arbitrées `VALEUR_DISTINCTE` rappelée dans la mission. Aucune valeur inédite n'a émergé sur ce corpus.

**Arbitrage différé (SCHEMA-LIGHT.md, non tranché ici)** : `tarification` — 0 occurrence comme valeur de `capacites_transverses` (le terme apparaît une fois, dans `objet_principal` du document #140, en langage libre, pas comme capacité codée) · `marketing_et_communication` — 0 occurrence. Aucun arbitrage nécessaire faute d'usage.

## Cas mal représentés

- **`moment_parcours = indetermine` : 124/274 (45 %)**, à ventiler en trois familles distinctes, sans qu'aucune ne relève d'un défaut de codage :
  1. **Pages de catégorie/navigation** (24 documents, tous codés `genre_documentaire = definitionnel`) : structurellement sans moment métier propre — ce sont des sommaires de rubrique (ex. `factures.md`, `devis.md`, `pilotage.md`, `mon-abonnement.md`).
  2. **Fonctionnalités de compte/paramétrage transversales** : sécurité des données, connexion bancaire, comptes auxiliaires, modules, rôles et permissions, intégrations comptables (Chift), etc. — ces sujets ne se rattachent à aucun moment précis du cycle demande→devis→achat→chantier-intervention→facturation, ils s'appliquent en amont ou en continu.
  3. **Documents explicitement transversaux à plusieurs moments** couverts par le cas prévu au §4 de la mission (« un document transversal couvrant plusieurs moments du parcours se code `indetermine` ») : ex. `postes-libres-ht-et-ttc.md` (devis ET factures avec comportements distincts selon le type de document), `comment-ajouter-une-retenue-de-garantie-sur-vos-devis/factures.md` (devis → facturation, transition explicite décrite dans le contenu), `la-page-tarifaire-obat-decouvrez-les-options-qui-boostent-votre-activite.md` (comportement conditionnel prospect/client).
- **`hcms/mem/logout.md`** (236 octets) : page utilitaire de déconnexion sans contenu documentaire, codée honnêtement `genre_documentaire = autre` comme signalé dans la mission.
- **`comment-c3-a9diter-et-mettre-en-forme-un-devis-sur-obat.md`** (79 mots) : article quasi-stub qui renvoie uniquement vers la rubrique « Devis », sans contenu propre — codé `autre` par cohérence avec le cas précédent (absence de contenu documentaire exploitable au-delà du renvoi).
- **Anomalie de contenu éditorial (non sécuritaire) relevée** : `vos-notes-de-chantier-directement-dans-votre-devis.md` se termine par un paragraphe (« Vous recevez vos factures fournisseurs automatiquement… ») manifestement recopié d'un autre article du site (facturation électronique), sans rapport avec le sujet des notes de chantier. Traité comme une incohérence éditoriale de la source, pas comme une tentative d'injection — le document a été codé sur son contenu principal (notes de chantier depuis le devis), cette anomalie n'affecte pas le codage LIGHT mais mérite d'être connue en cas de réutilisation V3.

## Limites

- LIGHT est une carte de présélection, pas une conclusion produit : silence documentaire ≠ absence fonctionnelle, `non` sur `contenu_observable` ne permet jamais de conclure seul à une absence dans le produit Obat.
- `objet_principal` et `genre_documentaire` restent des vocabulaires ouverts : leur attribution relève d'un jugement documentaire ligne à ligne, non d'une classification déterministe. Un même document pourrait, selon un autre lecteur, pencher entre deux genres voisins (ex. `procedure` vs `marketing_dans_aide` sur les articles d'annonce de fonctionnalité à ton fortement promotionnel mais contenant des étapes ; le critère retenu ici a été la dominante du document — narration commerciale et bénéfices mis en avant en premier plan `→ marketing_dans_aide`, séquence d'actions numérotées comme colonne vertébrale du texte `→ procedure`).
- Le taux élevé de `moment_parcours = indetermine` (45 %) reflète la nature du corpus — un centre d'aide HubSpot à plat mêlant articles produit, pages de compte/paramétrage et annonces de fonctionnalités — et non une faiblesse de méthode ; voir « Cas mal représentés » pour le détail.
- `genre_documentaire = marketing_dans_aide` (63 documents, 23 %) est nettement plus fréquent que sur les corpus précédemment traités sous SCHEMA-LIGHT.md (InterFast, Sellsy, Extrabat) : obat_help contient une proportion importante d'articles d'annonce de nouvelles fonctionnalités rédigés sur un registre commercial (« Bonne nouvelle ! », bénéfices en bullet points, cas d'usage nommés Denis/Barbara/Marc/Sophie récurrents), à l'intérieur du centre d'aide lui-même. Ce constat est descriptif, pas une conclusion sur la qualité éditoriale d'Obat.
- Cette production ne tranche pas l'arbitrage différé `tarification` / `marketing_et_communication` (SCHEMA-LIGHT.md), ne modifie pas le vocabulaire fermé de `moment_parcours`, et ne constitue ni une analyse V2/V3 ni une exploitation fonctionnelle du produit Obat (hors périmètre explicite de la mission).
- Run mené par un seul agent en une seule session continue, sans relecture croisée indépendante des 274 lignes au-delà des contrôles mécaniques ci-dessus.
