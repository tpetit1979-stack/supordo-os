# LIGHT — production Axonaut (corpus help/documentation complet)

Deuxième production LIGHT réelle, après clôture de Costructor LIGHT
(contre-audit : EXECUTION_VALIDEE_AVEC_CORRECTIONS_MINEURES). Schéma LIGHT
appliqué strictement sans modification. Discipline : un document à la fois,
lu intégralement, sortie écrite immédiatement, aucune correction
rétroactive sauf erreur mécanique démontrée et journalisée.

## Périmètre — vérification mécanique et gel

- `axonaut_help` (`corpus_index.json`) : **127** documents (18 rubriques,
  `index.md`/`erreurs.md` exclus du comptage canonique).
- Déjà utilisés (pilote LIGHT sur corpus inédit, lignes 26-33) : **8**.
- **Inédits à traiter, périmètre gelé : 119.**

Vérification mécanique : 127 (disque) = 119 (inédits) + 8 (exclus), union
exacte, 0 doublon, 0 chemin manquant, 0 chevauchement.

Fichiers exclus (8, déjà utilisés) :
1. `axonaut-et-votre-secteur-activite/evenementiel-pourquoi-axonaut-est-adapte-a-votre-activite.md`
2. `centralisez-gestion-emails-courriers/ajout-rapide-par-email.md`
3. `compte-pro-cartes/beneficiaire-effectif-quels-documents-sont-acceptes.md`
4. `connectez-axonaut/axonaut-zapier-connectez-vos-meilleurs-logiciels.md`
5. `creez-campagnes-marketing/boostez-vos-ventes-grace-au-module-segmentation-axonaut.md`
6. `creez-depenses-facilement/ajouter-un-paiement-sur-une-depense.md`
7. `etat-tresorerie-temps-reel/comment-ca-marche-le-menu-pilotage-tresorerie.md`
8. `gerez-ressources-humaines/comment-ca-marche-ressources-humaines.md`

Aucune substitution prévue à ce stade ; toute exception (fichier illisible/
vide/doublon) sera journalisée explicitement le cas échéant.

## Incidents et corrections

(journal tenu en continu ; vide si rien à signaler)

## Sorties LIGHT

| # | chemin_relatif | longueur_mots | objet_principal | moment_parcours | capacites_transverses | procedure | transition_objet | regle_ou_condition | contrainte_ou_limite | exception_ou_correction | genre_documentaire |
|---:|---|---:|---|---|---|:-:|:-:|:-:|:-:|:-:|---|
| 1 | axonaut-et-votre-secteur-activite/franchises-comment-gerer-votre-reseau-avec-axonaut.md | 750 | gestion de réseau de franchises (tableau de bord, redevances) | indetermine | automatisation, paiement, recherche | oui | oui | oui | non | non | definitionnel (ton fortement promotionnel) |
| 2 | centralisez-gestion-emails-courriers/comment-ajouter-un-contact-depuis-gmail-ou-outlook.md | 480 | extension navigateur (import contact depuis Gmail/Outlook) | indetermine | integrations, automatisation, communication | oui | oui | oui | non | oui | procedure (ton partiellement promotionnel) |
| 3 | centralisez-gestion-emails-courriers/comment-synchroniser-ses-emails-google-workspace-avec-axonaut.md | 300 | synchronisation email (Google Workspace, routage) | indetermine | integrations, communication | oui | non | oui | oui | oui | procedure |
| 4 | centralisez-gestion-emails-courriers/configurer-lenvoi-demails-depuis-axonaut.md | 750 | serveur SMTP (envoi d'emails, multi-fournisseurs) | indetermine | integrations, communication, securite_compte | oui | non | oui | oui | oui | procedure |
| 5 | centralisez-gestion-emails-courriers/emails-synchroniser-ovh-avec-axonaut.md | 380 | synchronisation email (OVH, règle de redirection) | indetermine | integrations, communication | oui | non | oui | non | non | procedure |
| 6 | centralisez-gestion-emails-courriers/envoyer-des-mails-depuis-axonaut.md | 700 | envoi d'emails et courriers (fiche client, pièces jointes) | indetermine | communication, documents, paiement | oui | non | oui | oui | oui | procedure |
| 7 | centralisez-gestion-emails-courriers/modeles-emails-2.md | 320 | modèles (documents, emails, tâches, commentaires — index) | indetermine | documents, communication, automatisation | non | non | non | non | non | reference_configuration |
| 8 | centralisez-gestion-emails-courriers/synchronisation-des-emails-parametrer-mailjet.md | 580 | serveur SMTP (Mailjet, authentification domaine) | indetermine | integrations, communication, securite_compte | oui | non | oui | oui | oui | procedure (ton partiellement promotionnel) |
| 9 | centralisez-gestion-emails-courriers/synchronisation-des-mails-avec-gandi.md | 240 | synchronisation email (Gandi, redirection) | indetermine | integrations, communication | oui | non | oui | oui | non | procedure |
| 10 | centralisez-gestion-emails-courriers/synchronisation-des-mails-avec-microsoft365-office-365.md | 620 | synchronisation email (Microsoft 365, règle de flux) | indetermine | integrations, communication, automatisation | oui | non | oui | oui | oui | procedure (ton fortement promotionnel) |
| 11 | centralisez-gestion-emails-courriers/synchroniser-ses-emails-ca-veut-dire-quoi-2.md | 550 | synchronisation email (définition + multi-fournisseurs) | indetermine | integrations, communication | oui | non | oui | oui | oui | definitionnel (avec instructions partielles) |
| 12 | centralisez-gestion-sav/comment-ca-marche-le-ticketing.md | 700 | ticket SAV (création, bon d'intervention, statistiques) | chantier-intervention | communication, documents, automatisation | oui | oui | oui | non | non | definitionnel (ton partiellement promotionnel) |
| 13 | centralisez-gestion-sav/parametrer-son-sav-ou-ticketing.md | 650 | paramétrage SAV/ticketing (portail client, statuts, réponses auto) | chantier-intervention | automatisation, communication, roles | oui | oui | oui | oui | non | procedure |
| 14 | commandes-clients-fournisseurs/creer-une-commande-fournisseur.md | 550 | commande fournisseur (bon de commande PDF) | achat | catalogue, documents, gestion_stock | oui | oui | oui | non | non | procedure |
| 15 | commandes-clients-fournisseurs/fonctionnement-dune-commande-client.md | 650 | commande client (conteneur devis/factures/BL, clôture) | devis | documents, paiement, gestion_stock | oui | oui | oui | oui | oui | procedure (ton partiellement promotionnel) |
| 16 | compte-pro-cartes/comment-activer-prelevement-client-compte-pro-axonaut.md | 620 | prélèvement client (mandat SEPA, Compte Pro) | facturation | paiement, securite_compte, communication | oui | oui | oui | oui | oui | procedure |
| 17 | compte-pro-cartes/comment-ajouter-carte-de-paiement-axonaut-sur-mon-telephone-wallet.md | 480 | carte de paiement mobile (Apple Pay/Google Pay, double authentification) | indetermine | mobile, securite_compte, paiement | oui | non | oui | oui | non | procedure (ton fortement promotionnel) |
| 18 | compte-pro-cartes/comment-contester-une-operation-frauduleuse-sur-une-carte-de-paiement-axonaut.md | 620 | contestation de fraude (carte de paiement, chargeback) | indetermine | paiement, securite_compte, documents | oui | oui | oui | oui | oui | faq_depannage |
| 19 | compte-pro-cartes/comment-faire-un-virement-depuis-le-compte-pro-axonaut.md | 950 | virement bancaire (ponctuel, récurrent, bénéficiaires) | indetermine | paiement, securite_compte, automatisation | oui | oui | oui | oui | oui | procedure |
| 20 | compte-pro-cartes/comment-ouvrir-un-compte-pro-axonaut.md | 2200 | ouverture de Compte Pro (éligibilité, KYC, bénéficiaires effectifs, découvert) | indetermine | paiement, conformite_reglementaire, securite_compte | oui | oui | oui | oui | oui | faq_depannage (contenu réglementaire et procédure imbriqués — cf. limites) |
| 21 | compte-pro-cartes/la-gestion-des-droits-utilisateurs-pour-le-compte-pro-axonaut.md | 300 | droits utilisateur (Compte Pro, invitation, vérification identité) | indetermine | roles, permissions, securite_compte | oui | oui | oui | oui | non | procedure |
| 22 | compte-pro-cartes/quelles-sont-les-cartes-de-paiement-axonaut.md | 1800 | carte de paiement (commande, activation, PIN, perte/vol) | indetermine | paiement, securite_compte, mobile | oui | oui | oui | oui | oui | faq_depannage |
| 23 | compte-pro-cartes/quels-sont-les-frais-annexes-du-compte-pro-axonaut.md | 550 | frais annexes (Compte Pro, retraits, virements internationaux) | indetermine | paiement, conformite_reglementaire | non | non | oui | oui | non | reference_configuration |
| 24 | configurer-votre-compte/abonnement-axonaut-on-vous-explique-tout.md | 750 | abonnement (formules, renouvellement, factures, frais tiers) | indetermine | paiement, documents | oui | oui | oui | oui | oui | definitionnel (ton partiellement promotionnel) |
| 25 | configurer-votre-compte/ajouter-un-utilisateur-dans-axonaut.md | 650 | utilisateur (ajout/suppression/réactivation, message d'erreur email) | indetermine | roles, permissions, paiement | oui | oui | oui | oui | oui | procedure |
| 26 | configurer-votre-compte/axonaut-et-ia.md | 620 | fonctionnalités IA (résumé, analyse devis/factures, description produit, segmentation) | indetermine | automatisation, catalogue, communication | non | non | non | non | non | marketing_dans_aide |
| 27 | configurer-votre-compte/comment-creer-sa-signature-e-mail-dans-axonaut.md | 320 | signature email (texte, champs dynamiques, image) | indetermine | communication, documents | oui | non | non | non | non | procedure |
| 28 | configurer-votre-compte/comment-creer-son-compte-axonaut-facilement-et-rapidement.md | 750 | compte Axonaut (inscription, modules, alias email, profil — hub multi-sujets) | indetermine | roles, communication, integrations | oui | oui | oui | oui | non | autre (page multi-sujets : inscription, modules, alias, profil) |
| 29 | configurer-votre-compte/comment-importer-ses-donnees-quickbooks-dans-axonaut.md | 1500 | migration de données QuickBooks (clients, fournisseurs, produits, factures) | indetermine | integrations, documents, catalogue | oui | oui | oui | oui | oui | procedure |
| 30 | configurer-votre-compte/demo-effacer-les-donnees-factices.md | 480 | données de démonstration (suppression, cas bloquant facture) | indetermine | documents, catalogue, automatisation | oui | oui | oui | oui | oui | procedure |
| 31 | configurer-votre-compte/droits-responsabilites-utilisateurs-a-quoi-ca-correspond-2.md | 680 | droits/responsabilités utilisateur (rôles, personnel vs utilisateur) | indetermine | roles, permissions, paiement | oui | non | oui | oui | non | reference_configuration |
| 32 | configurer-votre-compte/exporter-ses-donnees-depuis-axonaut.md | 550 | export de données (Excel, contacts/factures/produits) | indetermine | documents, integrations, automatisation | oui | oui | oui | non | non | procedure (ton partiellement promotionnel) |
| 33 | configurer-votre-compte/importer-ses-contacts.md | 470 | import de données (contacts/produits/factures, fichier modèle) | indetermine | integrations, documents, catalogue | oui | oui | oui | non | oui | procedure |
| 34 | configurer-votre-compte/parrainage-comment-ca-marche.md | 620 | parrainage et affiliation (récompenses, conditions d'activation) | indetermine | paiement, communication, automatisation | oui | oui | oui | oui | oui | procedure (ton partiellement promotionnel) |
| 35 | configurer-votre-compte/personnaliser-ses-exports-de-factures-depenses-et-devis.md | 550 | export personnalisé (factures/devis/dépenses, champs CSV) | indetermine | documents, paiement, integrations | oui | non | non | non | non | procedure |
| 36 | connectez-axonaut/comment-connecter-votre-boutique-en-ligne-a-axonaut-shopify-prestashop-woocommerce.md | 900 | connexion e-commerce (Shopify/Prestashop/Woocommerce) | indetermine | integrations, catalogue, automatisation | oui | oui | oui | oui | oui | procedure (ton partiellement promotionnel) |
| 37 | connectez-axonaut/connecter-votre-systeme-de-telephonie.md | 650 | connexion téléphonie (3CX/Wildix/Ringover, click-to-call) | indetermine | integrations, communication, automatisation | oui | oui | oui | oui | non | procedure (ton partiellement promotionnel) |
| 38 | connectez-axonaut/connexion-axonaut-hiboutik-comment-ca-marche.md | 700 | connexion point de vente (Hiboutik, facturation auto, client anonyme) | indetermine | integrations, gestion_stock, automatisation | oui | oui | oui | oui | oui | procedure (ton partiellement promotionnel) |
| 39 | connectez-axonaut/proposez-lavance-immediate-avec-axonaut.md | 480 | avance immédiate (API tiers de prestation URSSAF) | facturation | paiement, conformite_reglementaire, integrations | oui | oui | oui | oui | oui | procedure |
| 40 | creez-campagnes-marketing/campagne-emailing-importer-mon-template-mailchimp.md | 500 | import de template email (Mailchimp, conversion HTML) | indetermine | integrations, communication, documents | oui | oui | oui | oui | non | procedure |
| 41 | creez-campagnes-marketing/campagne-emailing-importer-mon-template-sendinblue.md | 380 | import de template email (Sendinblue, code HTML) | indetermine | integrations, communication, documents | oui | oui | non | non | non | procedure |
| 42 | creez-campagnes-marketing/comment-ca-marche-le-menu-marketing.md | 750 | menu Marketing (campagnes email/SMS, statistiques, segmentation IA) | indetermine | communication, automatisation, recherche | oui | oui | oui | non | non | definitionnel (ton partiellement promotionnel) |
| 43 | creez-campagnes-marketing/creer-un-template-marketing-dans-axonaut.md | 650 | template marketing (éditeur d'apparence et de contenu) | indetermine | documents, communication | oui | non | oui | oui | non | procedure |
| 44 | creez-campagnes-marketing/creer-une-campagne-emailing-a-partir-dun-template-axonaut.md | 800 | campagne emailing (ciblage, coût, opt-out, verrouillage post-envoi) | indetermine | communication, paiement, conformite_reglementaire | oui | oui | oui | oui | non | procedure |
| 45 | creez-campagnes-marketing/creer-une-campagne-emailing-a-partir-dun-template-hors-axonaut.md | 350 | campagne emailing (template externe, opt-out, verrouillage post-envoi) | indetermine | communication, conformite_reglementaire, documents | oui | oui | oui | oui | non | procedure |
| 46 | creez-campagnes-marketing/utiliser-un-template-mailjet-pour-vos-campagnes-marketing-axonaut.md | 600 | import de template email (Mailjet, conversion HTML) | indetermine | integrations, communication, documents | oui | oui | non | non | non | procedure |
| 47 | creez-depenses-facilement/ajouter-une-depense.md | 900 | dépense (OCR, devise, récurrence) | achat | automatisation, paiement, documents | oui | oui | oui | non | non | procedure |
| 48 | creez-depenses-facilement/comment-ca-marche-achats.md | 1000 | achats (fournisseurs, dépenses, commandes, notes de frais, indemnités km) | achat | automatisation, paiement, mobile | oui | oui | oui | non | non | definitionnel |
| 49 | creez-depenses-facilement/comment-payer-ses-depenses-sur-axonaut.md | 850 | paiement de dépense (virement, prélèvement, rapprochement bancaire) | achat | paiement, automatisation, integrations | oui | oui | oui | non | non | procedure |
| 50 | creez-depenses-facilement/les-indemnites-kilometriques-axonaut.md | 1400 | indemnité kilométrique (barème URSSAF, seuils, rattrapage) | achat | paiement, conformite_reglementaire, automatisation | oui | oui | oui | oui | oui | definitionnel (avec calculs et procédures associées — cf. limites) |
| 51 | creez-depenses-facilement/modifier-supprimer-une-depense.md | 320 | modification/suppression de dépense (cas bloquants : payée, réceptionnée, droits) | achat | gestion_stock, permissions, paiement | oui | oui | oui | oui | oui | faq_depannage |
| 52 | creez-depenses-facilement/valider-une-note-de-frais-ndf.md | 400 | note de frais (création, validation, suppression selon statut de paiement) | achat | paiement, documents, roles | oui | oui | oui | oui | oui | procedure |
| 53 | etat-tresorerie-temps-reel/comment-obtenir-une-avance-de-tresorerie.md | 950 | avance de trésorerie (Defacto, éligibilité, statuts de financement) | facturation | paiement, integrations, conformite_reglementaire | oui | oui | oui | oui | non | procedure (ton partiellement promotionnel) |
| 54 | etat-tresorerie-temps-reel/gerer-mon-pret-bancaire-sur-axonaut.md | 350 | prêt bancaire (déclaration, rapprochement des mensualités) | indetermine | paiement, automatisation, integrations | oui | oui | oui | non | non | procedure |
| 55 | etat-tresorerie-temps-reel/le-previsionnel-de-tresorerie.md | 1200 | prévisionnel de trésorerie (module, scénarios, sources de calcul) | indetermine | paiement, automatisation, recherche | oui | non | oui | non | non | reference_configuration |
| 56 | etat-tresorerie-temps-reel/rapprochement-bancaire-comment-ca-marche.md | 1100 | rapprochement bancaire (connexion, réconciliation, DSP2, instabilité) | indetermine | paiement, integrations, conformite_reglementaire | oui | oui | oui | oui | oui | procedure (avec section réglementaire DSP2) |
| 57 | gerez-rentabilite-projets/comment-creer-un-projet.md | 950 | projet (rentabilité, tâches, feuille de temps) | indetermine | planning, paiement, recherche | oui | oui | oui | non | non | definitionnel |
| 58 | gerez-rentabilite-projets/comment-creer-une-tache.md | 950 | tâche (affectation, statut, portail client) | indetermine | planning, roles, notifications | oui | oui | oui | oui | non | procedure |
| 59 | gerez-stock-temps-reel/comment-ca-marche-la-gestion-de-stock.md | 850 | gestion de stock (fabrication, bons de livraison, réception, location) | indetermine | gestion_stock, catalogue, documents | oui | oui | oui | non | oui | definitionnel |
| 60 | gerez-stock-temps-reel/comment-exporter-un-inventaire-des-stocks.md | 250 | export d'inventaire (Excel, CMUP) | indetermine | gestion_stock, documents, integrations | oui | non | non | non | non | procedure |
| 61 | gerez-stock-temps-reel/controler-letat-de-mon-stock-dans-axonaut.md | 750 | état de stock (table, alerte de seuil, catalogue vs stock) | indetermine | gestion_stock, notifications, automatisation | oui | oui | oui | oui | oui | reference_configuration |
| 62 | gerez-stock-temps-reel/fabrications-comment-ca-marche.md | 250 | fabrication (produit fini, décrémentation matières premières) | indetermine | gestion_stock, catalogue, automatisation | oui | oui | oui | non | non | procedure |
| 63 | gerez-stock-temps-reel/gestion-dlc-dluo-dlm-et-garanties.md | 650 | traçabilité produit (DLC/DDM, lots, garanties) | indetermine | gestion_stock, conformite_reglementaire, documents | oui | oui | oui | oui | non | definitionnel (avec procédures associées) |
| 64 | gerez-vos-devis/accepter-refuser-un-devis.md | 220 | acceptation/refus de devis (transition en commande) | devis | documents, automatisation | oui | oui | oui | non | non | procedure |
| 65 | gerez-vos-devis/comment-connecter-jesignexpert-a-axonaut.md | 600 | signature électronique (jesignexpert, lettre de mission) | indetermine | integrations, securite_compte, communication | oui | oui | oui | oui | non | procedure |
| 66 | gerez-vos-devis/comment-creer-une-lettre-de-mission-sur-axonaut.md | 350 | lettre de mission (modèle Word, génération depuis fiche client) | indetermine | documents, integrations | oui | oui | non | non | non | procedure |
| 67 | gerez-vos-devis/comment-faire-payer-mes-devis-sur-axonaut.md | 450 | paiement en ligne de devis (transition automatique en facture) | devis | paiement, automatisation, notifications | oui | oui | non | non | non | procedure |
| 68 | gerez-vos-devis/comment-numeroter-mes-devis-dans-axonaut.md | 750 | numérotation devis/factures (préfixe, compteur, obligation légale) | indetermine | conformite_reglementaire, documents | oui | non | oui | oui | non | reference_configuration |
| 69 | gerez-vos-devis/comment-relancer-automatiquement-ses-devis.md | 600 | relance automatique de devis (exclusion client, escalade huissier) | devis | automatisation, communication, paiement | oui | oui | oui | oui | oui | procedure |
| 70 | gerez-vos-devis/comment-transformer-un-devis-en-facture.md | 800 | transformation devis en facture (2 méthodes, droits utilisateur) | devis | documents, roles, automatisation | oui | oui | oui | oui | oui | procedure |
| 71 | gerez-vos-devis/creer-un-devis-avec-axonaut.md | 1000 | devis (création, IA, duplication, téléchargement PDF) | devis | catalogue, documents, automatisation | oui | oui | oui | oui | oui | procedure (ton partiellement promotionnel) |
| 72 | gerez-vos-devis/envoyer-mes-devis-depuis-axonaut.md | 350 | envoi de devis (email, portail client, lecture) | devis | communication, notifications, documents | oui | oui | non | non | non | procedure |
| 73 | gerez-vos-devis/le-portail-client-axonaut-comment-ca-marche.md | 550 | portail client (signature, paiement, espace collaboratif) | indetermine | communication, securite_compte, paiement | oui | oui | non | oui | non | definitionnel (ton fortement promotionnel) |
| 74 | gerez-vos-devis/modifier-un-devis.md | 800 | modification/suppression de devis (statuts, cas bloquants) | devis | documents, roles, automatisation | oui | oui | oui | oui | oui | procedure |
| 75 | gerez-vos-devis/personnaliser-ses-devis-et-factures-sur-axonaut.md | 750 | personnalisation visuelle (devis/factures, thèmes, champs) | indetermine | documents, communication | oui | non | non | non | non | procedure (ton fortement promotionnel) |
| 76 | gerez-vos-devis/signature-electronique-des-devis-documents-yousign.md | 800 | signature électronique (Yousign, eIDAS, crédit par signature) | devis | securite_compte, integrations, conformite_reglementaire | oui | oui | oui | oui | non | procedure (ton fortement promotionnel) |
| 77 | gerez-vos-factures/ajouter-des-taux-de-tva.md | 550 | taux de TVA (ajout, TVA intracommunautaire) | indetermine | conformite_reglementaire, integrations | oui | non | oui | non | non | reference_configuration |
| 78 | gerez-vos-factures/axonaut-chorus-pro-comment-ca-marche.md | 280 | dépôt facture Chorus Pro (secteur public, obligation légale) | facturation | conformite_reglementaire, integrations, documents | oui | oui | oui | oui | non | procedure (ton partiellement promotionnel) |
| 79 | gerez-vos-factures/changer-de-devise-sur-axonaut.md | 600 | devise de facturation (compte et par client) | facturation | paiement, documents | oui | non | oui | non | non | procedure (ton fortement promotionnel) |
| 80 | gerez-vos-factures/comment-ajouter-un-paiement-sur-une-facture.md | 900 | paiement de facture (manuel vs rapprochement, cas de doublon) | facturation | paiement, automatisation, integrations | oui | oui | oui | oui | oui | procedure |
| 81 | gerez-vos-factures/comment-connecter-paypal-a-axonaut.md | 400 | connexion PayPal (identifiants API, paiement devis/factures) | indetermine | paiement, integrations, securite_compte | oui | non | non | non | non | procedure |
| 82 | gerez-vos-factures/comment-creer-une-facture-davancement-dans-axonaut.md | 950 | facture d'avancement / de situation (avancement cumulé, verrouillage prévisionnel) | facturation | documents, paiement, planning | oui | oui | oui | oui | non | procedure |
| 83 | gerez-vos-factures/comment-facturer-du-temps-dans-axonaut.md | 600 | facturation de temps (type de tâche associé à un produit) | facturation | planning, paiement, automatisation | oui | oui | oui | non | non | procedure |
| 84 | gerez-vos-factures/comment-faire-un-avoir-sur-axonaut.md | 750 | avoir (global/partiel/fournisseur, suppression encadrée de facture) | facturation | conformite_reglementaire, documents, paiement | oui | oui | oui | oui | oui | politique_legale (avec procédures associées) |
| 85 | gerez-vos-factures/comment-faire-une-facture-recurrente-un-abonnement-sur-axonaut.md | 950 | facture récurrente / abonnement (prévisionnel, délai de sécurité) | facturation | automatisation, paiement, communication | oui | oui | oui | oui | oui | procedure |
| 86 | gerez-vos-factures/comment-gerer-leco-participation-dans-axonaut.md | 500 | éco-participation / taxe DEEE (configuration produit, décomposition facture) | facturation | conformite_reglementaire, catalogue, documents | oui | oui | oui | non | non | definitionnel (avec procédure associée) |
| 87 | gerez-vos-factures/comment-modifier-une-facture.md | 900 | modification/suppression de facture (paiement, avoir, droits — contenu recoupant #80/#84) | facturation | conformite_reglementaire, paiement, roles | oui | oui | oui | oui | oui | politique_legale (avec procédures associées — cf. limites, contenu dupliqué) |
| 88 | gerez-vos-factures/comment-relancer-mes-factures-impayees-automatiquement-avec-axonaut.md | 700 | relance et recouvrement de factures impayées (huissiers, litige) | facturation | automatisation, paiement, communication | oui | oui | oui | oui | oui | procedure |
| 89 | gerez-vos-factures/comment-utiliser-la-tva-sur-marge-dans-axonaut.md | 750 | TVA sur marge (calcul, affichage, mention légale — cf. limites, contenu fiscal dense) | facturation | conformite_reglementaire, documents | oui | non | oui | oui | non | definitionnel (avec procédure associée) |
| 90 | gerez-vos-factures/creer-un-debours-ou-note-de-debit-dans-axonaut.md | 700 | débours / note de débit (produit hors CA) | facturation | conformite_reglementaire, catalogue, documents | oui | oui | oui | oui | non | procedure |
| 91 | gerez-vos-factures/creer-une-facture-avec-axonaut-2.md | 2200 | facture (création, langues, adresses communes, CGV, images — hub multi-sujets) | facturation | documents, catalogue, conformite_reglementaire | oui | oui | oui | oui | non | autre (page multi-sujets — cf. limites) |
| 92 | gerez-vos-factures/facture-proforma.md | 650 | facture proforma (devis/douane/financement, création depuis commande) | devis | documents, conformite_reglementaire | oui | oui | oui | non | non | definitionnel (avec procédure associée) |
| 93 | gerez-vos-factures/faire-payer-mes-factures-par-carte-via-stripe.md | 750 | paiement par carte (Stripe, portail client, risque de doublon) | facturation | paiement, integrations, securite_compte | oui | oui | oui | oui | non | procedure (ton fortement promotionnel) |
| 94 | gerez-vos-factures/faire-payer-mes-factures-par-prelevement-via-gocardless.md | 1100 | prélèvement (GoCardless/Compte Pro, mandats, devise, import) | facturation | paiement, integrations, automatisation | oui | oui | oui | oui | oui | procedure |
| 95 | gerez-vos-factures/faire-un-acompte-sur-axonaut.md | 800 | acompte et solde (facture partielle, déduction automatique) | facturation | paiement, documents, automatisation | oui | oui | oui | non | non | procedure (ton fortement promotionnel) |
| 96 | gerez-vos-factures/qr-code-facture-suisse-comment-configurer-dans-axonaut.md | 350 | QR code facture (Suisse, obligation légale) | facturation | conformite_reglementaire, paiement, documents | oui | non | oui | oui | oui | procedure |
| 97 | gerez-vos-produits/comment-ajouter-des-produits-services-dans-axonaut.md | 1900 | produit/service (ajout, IA, vente en ligne, code-barres, traduction — hub multi-sujets) | indetermine | catalogue, integrations, automatisation | oui | oui | oui | oui | non | autre (page multi-sujets — cf. limites) |
| 98 | gerez-vos-produits/modifier-un-produit.md | 400 | modification/suppression de produit (désactivation, archives, droits) | indetermine | catalogue, roles, integrations | oui | oui | oui | oui | oui | procedure |
| 99 | gerez-votre-comptabilite/automatisez-la-gestion-des-codes-tiers-numeros-clients-fournisseurs.md | 750 | codes tiers (formats de numérotation clients/fournisseurs) | indetermine | conformite_reglementaire, integrations, automatisation | oui | non | oui | non | non | procedure |
| 100 | gerez-votre-comptabilite/comment-cloturer-mon-exercice-comptable.md | 600 | clôture d'exercice comptable (verrouillage irréversible, portail comptable) | indetermine | conformite_reglementaire, documents, roles | oui | oui | oui | oui | non | procedure |
| 101 | gerez-votre-comptabilite/comment-faciliter-sa-declaration-de-tva-avec-axonaut.md | 800 | déclaration de TVA (tableau collecté/déductible, codes comptables requis) | indetermine | conformite_reglementaire, recherche, paiement | oui | non | oui | oui | non | reference_configuration |
| 102 | gerez-votre-comptabilite/le-portail-comptable-axonaut.md | 750 | portail comptable (invitation, exports automatisés, intégrations logiciels) | indetermine | integrations, roles, documents | oui | oui | non | non | oui | definitionnel (ton partiellement promotionnel) |
| 103 | gerez-votre-comptabilite/realiser-ses-exports-comptables.md | 650 | exports comptables (ventes/achats/paiements/lignes bancaires, personnalisation) | indetermine | integrations, documents, conformite_reglementaire | oui | non | oui | non | oui | procedure |
| 104 | gerez-votre-comptabilite/saisir-ou-importer-mon-plan-comptable-dans-axonaut.md | 700 | plan comptable (saisie manuelle ou import massif) | indetermine | conformite_reglementaire, integrations, documents | oui | non | non | non | non | procedure |
| 105 | optimisez-gestion-commerciale/ajouter-mes-documents-de-gestion.md | 700 | document de gestion (K-bis, documents publics, fiche client) | indetermine | documents, communication, securite_compte | oui | non | non | non | non | procedure |
| 106 | optimisez-gestion-commerciale/automatisez-vos-actions-commerciales-avec-axonaut.md | 800 | automatisation commerciale (déclencheur/action, opportunités) | indetermine | automatisation, planning, communication | oui | oui | oui | non | non | procedure |
| 107 | optimisez-gestion-commerciale/categoriser-les-contacts-sur-votre-compte-axonaut.md | 900 | catégorisation (contacts, produits, champs personnalisés) | indetermine | catalogue, recherche, roles | oui | non | non | non | non | procedure |
| 108 | optimisez-gestion-commerciale/comment-ca-marche-commercial.md | 550 | CRM (agenda, répertoire, opportunités, marketing — tour de fonctionnalités) | indetermine | communication, recherche, automatisation | oui | oui | non | non | non | definitionnel |
| 109 | optimisez-gestion-commerciale/comment-creer-une-societe-dans-axonaut.md | 750 | société/contact (fiche, catégorisation auto, unicité particulier) | indetermine | integrations, conformite_reglementaire, roles | oui | oui | oui | oui | non | procedure |
| 110 | optimisez-gestion-commerciale/creer-un-modele-de-document-word-docx.md | 1000 | modèle de document Word (champs dynamiques, génération fiche client) | indetermine | documents, integrations, communication | oui | oui | oui | oui | non | procedure |
| 111 | optimisez-gestion-commerciale/formulaire-axonaut.md | 1100 | formulaire (création, partage, statistiques, réponses) | indetermine | automatisation, communication, recherche | oui | oui | oui | non | non | procedure |
| 112 | optimisez-gestion-commerciale/la-fiche-client-axonaut.md | 1900 | fiche client (échanges, prospect→client, fusion de doublons) | indetermine | documents, communication, roles | oui | oui | oui | oui | oui | reference_configuration |
| 113 | optimisez-gestion-commerciale/la-fiche-fournisseur.md | 700 | fiche fournisseur (échanges, commandes, fusion de doublons) | achat | documents, communication, roles | oui | oui | non | non | oui | reference_configuration |
| 114 | optimisez-gestion-commerciale/les-champs-personnalises-dans-axonaut-cest-quoi.md | 650 | champ personnalisé (types, zones d'affichage, vs catégories) | indetermine | catalogue, recherche, documents | oui | non | non | oui | non | definitionnel (avec procédure associée) |
| 115 | optimisez-gestion-commerciale/modifier-un-contact.md | 350 | modification/suppression de contact (archives, droits, réaffectation) | indetermine | roles, catalogue, integrations | oui | oui | oui | oui | oui | procedure |
| 116 | optimisez-gestion-commerciale/prise-de-rendez-vous.md | 1300 | prise de rendez-vous (page de réservation, rappels, paiement en ligne) | indetermine | planning, communication, automatisation | oui | oui | oui | non | non | procedure |
| 117 | optimisez-gestion-commerciale/synchroniser-son-agenda-google-avec-axonaut.md | 750 | synchronisation agenda Google (bidirectionnelle, dépannage) | indetermine | integrations, communication, notifications | oui | oui | oui | oui | oui | procedure |
| 118 | optimisez-gestion-commerciale/synchroniser-son-agenda-microsoft-avec-axonaut.md | 400 | synchronisation agenda Microsoft (connexion, reconnexion après déconnexion) | indetermine | integrations, communication, securite_compte | oui | oui | oui | oui | oui | procedure |
| 119 | optimisez-gestion-commerciale/synchroniser-son-calendrier-apple.md | 300 | synchronisation calendrier Apple (via Google Agenda, prérequis) | indetermine | integrations, mobile, communication | oui | non | oui | oui | non | procedure |

## Résultat mécanique final

Tous les totaux ci-dessous sont calculés par script (parsing des 119 lignes
du tableau, aucun comptage manuel).

- **Documents traités : 119/119** (périmètre gelé intégralement couvert,
  numérotation 1→119 continue, 0 doublon, 0 trou).
- **Mots lus (somme mécanique de `longueur_mots`) : 85 660.**
- **Durée : CONTEXTE_SESSION_NON_MESURABLE** (aucune estimation produite).
- **Incidents : aucun** sur les 5 lots. **0 document vide ou quasi vide**
  (aucune ligne ≤ 30 mots) — à la différence de Costructor, ce corpus ne
  contient pas d'article réduit à des captures d'écran sans légende.
- **Corrections mécaniques : aucune** (contrairement à Costructor, aucune
  valeur hors vocabulaire fermé n'a été introduite pendant ce run).

### moment_parcours (119 documents)

| valeur | n | % |
|---|---:|---:|
| indetermine | 79 | 66,4 % |
| facturation | 20 | 16,8 % |
| devis | 10 | 8,4 % |
| achat | 8 | 6,7 % |
| chantier-intervention | 2 | 1,7 % |
| **somme** | **119** | **100,0 %** |

**Taux `indetermine` : 66,4 % (79/119).** Plus élevé que sur Costructor
(51,1 %). Ce n'est pas un défaut de codage : Axonaut est un outil de
gestion généraliste (CRM, compte pro, comptabilité, RH, marketing) dont une
large majorité des articles d'aide couvrent des réglages transverses
(comptes, intégrations, agenda, campagnes) qui ne se rattachent à aucune
phase du cycle devis→facturation. Le corpus Costructor, plus centré métier
BTP, produisait mécaniquement moins d'« indetermine ».

### capacites_transverses (occurrences, un document peut en porter jusqu'à 3)

| capacité | n |
|---|---:|
| documents | 51 |
| integrations | 46 |
| paiement | 45 |
| communication | 43 |
| automatisation | 41 |
| conformite_reglementaire | 27 |
| roles | 18 |
| catalogue | 17 |
| securite_compte | 16 |
| recherche | 9 |
| gestion_stock | 9 |
| planning | 6 |
| notifications | 5 |
| mobile | 4 |
| permissions | 4 |

`integrations` domine davantage que sur Costructor (Axonaut multiplie les
connecteurs tiers : Stripe, PayPal, GoCardless, Defacto, Hiboutik, Shopify,
Prestashop, WooCommerce, jesignexpert, Yousign, Chorus Pro, Caarl, Bankin,
logiciels comptables…).

### genre_documentaire (119 documents, racines regroupées)

| valeur | n | % |
|---|---:|---:|
| procedure | 82 | 68,9 % |
| definitionnel | 17 | 14,3 % |
| reference_configuration | 10 | 8,4 % |
| faq_depannage | 4 | 3,4 % |
| autre | 3 | 2,5 % |
| politique_legale | 2 | 1,7 % |
| marketing_dans_aide | 1 | 0,8 % |
| **somme** | **119** | **100,0 %** |

`marketing_dans_aide` apparaît ici pour la première fois sur l'ensemble des
deux corpus traités (doc 26, présentation des fonctionnalités IA, 0/5
booléens à `oui` — page entièrement promotionnelle, sans contenu procédural
vérifiable).

### contenu_observable (5 booléens, 119 documents, oui/non/inconnu)

| champ | oui | non | inconnu |
|---|---:|---:|---:|
| procedure | 116 | 3 | 0 |
| transition_objet | 86 | 33 | 0 |
| regle_ou_condition | 99 | 20 | 0 |
| contrainte_ou_limite | 73 | 46 | 0 |
| exception_ou_correction | 47 | 72 | 0 |

Aucune valeur `inconnu` n'a été nécessaire : les 119 documents étaient
chacun suffisamment explicites pour trancher les 5 booléens de manière
factuelle — y compris les documents les plus courts (aucun cas de type
« Pennylane » à contenu quasi entièrement visuel comme sur Costructor).

`exception_ou_correction` est sensiblement plus fréquent que sur Costructor
(39,5 % contre 8,5 %) : le corpus Axonaut documente un nombre important de
cas bloquants et de workarounds explicites (facture/dépense/devis déjà
payés, droits utilisateur manquants, doublons de fiches à fusionner,
synchronisations d'agenda en échec, mandats de prélèvement en double) —
un style éditorial plus orienté dépannage que Costructor.

### Cas que LIGHT représente mal

**Limitations déjà connues (confirmées sur ce corpus) :**

- **Pages-hub multi-sujets.** Comme sur Costructor (doc 52), plusieurs
  pages Axonaut agrègent des sujets hétérogènes sous une seule URL :
  doc 28 (inscription + modules + alias email + profil), doc 91 (création
  de facture + langues + adresses communes + CGV + images, 2200 mots),
  doc 97 (ajout produit + IA + vente en ligne + code-barres + traduction,
  1900 mots). `objet_principal` et `moment_parcours` uniques ne peuvent
  pas représenter fidèlement ces documents ; `autre` a dû être utilisé
  hors du cas d'usage initial (page-carrefour ponctuelle) pour des
  documents bien plus longs et denses.
- **Contenu quasi vide / visuel dominant.** Aucun cas trouvé sur ce
  corpus (à la différence de Costructor) — limitation confirmée comme
  possible mais non généralisable à tout éditeur.

**Nouveaux cas observés sur ce corpus (non rencontrés sur Costructor) :**

- **Contenu fiscal/réglementaire dense et calculatoire.** Plusieurs
  documents Axonaut vont bien au-delà d'une simple procédure logicielle et
  exigent une expertise comptable/fiscale pour être pleinement compris :
  le barème kilométrique URSSAF et son mécanisme de « rattrapage »
  (doc 50, avec formules et exemples chiffrés), la TVA sur marge et sa
  mention légale obligatoire (doc 89), l'éco-participation / taxe DEEE
  (doc 86). LIGHT les code correctement (`definitionnel`, `regle_ou_
  condition`, `contrainte_ou_limite`) mais aplatit une différence de
  nature : ces pages sont autant des mini-guides fiscaux que de la
  documentation produit, ce qui a une valeur concurrentielle propre
  (Axonaut investit dans de la vulgarisation réglementaire poussée) que le
  schéma ne capture pas comme dimension à part entière.
- **Contenu dupliqué entre articles.** Au moins trois documents
  (`comment-ajouter-un-paiement-sur-une-facture.md`,
  `comment-faire-un-avoir-sur-axonaut.md`,
  `comment-modifier-une-facture.md`) partagent des paragraphes quasi
  identiques sur les règles de suppression de facture. LIGHT code chaque
  URL indépendamment et ne détecte pas cette redondance éditoriale — trois
  lignes distinctes du tableau surreprésentent donc la même information
  factuelle, ce qui pourrait légèrement biaiser une lecture agrégée fine
  (au-delà des distributions globales produites ici, qui restent
  correctes).
- **Automatisations à règles conditionnelles complexes.** Le moteur
  d'automatisation commerciale (doc 106, déclencheur→action) et les
  formulaires avec routage automatique (doc 111) décrivent des logiques
  conditionnelles combinatoires (plusieurs actions par déclencheur,
  délais paramétrables) que le simple booléen `regle_ou_condition=oui`
  signale sans en refléter la richesse structurelle.
- **IA quasi non capturée par le vocabulaire de capacités.** Comme
  pressenti sur Costructor, les fonctionnalités IA d'Axonaut (résumé de
  fiche client, analyse de devis/factures, génération de description
  produit, segmentation marketing — doc 26 ; devis payés recommandés par
  IA) restent sous-décrites par `automatisation`, terme trop générique
  pour distinguer une automatisation déterministe (relance programmée)
  d'une fonctionnalité génération de contenu par IA.

