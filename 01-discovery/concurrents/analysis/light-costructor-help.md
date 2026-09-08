# LIGHT — production Costructor (corpus help/documentation complet)

Première production LIGHT réelle (post-pilote). Schéma LIGHT validé
(`pilote-light-corpus-inedit.md`) appliqué sans modification. Discipline :
un document à la fois, lu intégralement, sortie écrite immédiatement,
aucune correction rétroactive.

## Périmètre — vérification mécanique et gel

- `costructor_help` (`corpus_index.json`) : **112** documents (10 rubriques,
  `index.md`/`erreurs.md` déjà exclus du comptage canonique).
- Déjà utilisés dans les travaux précédents (Analysis C fork A : 10 ;
  pilote LIGHT sur corpus inédit : 8) : **18**.
- **Inédits à traiter, périmètre gelé : 94.**

Aucune substitution prévue à ce stade ; toute exception (fichier illisible/
vide/doublon) sera journalisée explicitement le cas échéant.

## Sorties LIGHT

| # | chemin_relatif | longueur_mots | objet_principal | moment_parcours | capacites_transverses | procedure | transition_objet | regle_ou_condition | contrainte_ou_limite | exception_ou_correction | genre_documentaire |
|---:|---|---:|---|---|---|:-:|:-:|:-:|:-:|:-:|---|
| 1 | abonnement/comment-ajouter-une-seconde-entreprise-c2jr6v.md | 130 | multi-entreprise / abonnement | indetermine | paiement | oui | non | oui | non | non | procedure |
| 2 | abonnement/comment-beneficier-de-loffre-jeune-entreprise-1vs4eiy.md | 120 | offre jeune entreprise / abonnement | indetermine | paiement | oui | non | oui | non | non | procedure |
| 3 | abonnement/comment-essayer-ou-sabonner-a-batiprix-1k44gf1.md | 200 | bibliothèque de prix (Batiprix, intégration tierce) | devis | catalogue, integrations, paiement | oui | non | oui | oui | non | procedure |
| 4 | abonnement/comment-mettre-a-jour-son-moyen-de-paiement-6rwou1.md | 90 | moyen de paiement (abonnement) | indetermine | paiement | oui | non | non | non | non | procedure |
| 5 | abonnement/comment-modifier-son-abonnement-3z9g1l.md | 90 | forfait / abonnement | indetermine | paiement | oui | oui | oui | non | non | procedure |
| 6 | abonnement/comment-parrainer-une-entreprise-psonbr.md | 220 | parrainage (programme de référencement) | indetermine | paiement, communication | oui | non | oui | oui | non | reference_configuration |
| 7 | abonnement/comment-sabonner-a-costructor-vxkaie.md | 90 | abonnement (souscription initiale) | indetermine | paiement | oui | non | non | non | non | procedure |
| 8 | abonnement/telecharger-les-factures-dabonnement-costructor-1cmafv1.md | 50 | facture d'abonnement | indetermine | paiement, documents | oui | non | non | non | non | procedure |
| 9 | chantiers/comment-creer-un-bordereau-de-chantier-1492z8v.md | 130 | bordereau de chantier | chantier-intervention | documents | oui | oui | oui | oui | non | procedure |
| 10 | chantiers/comment-creer-un-planning-de-chantier-s6jnge.md | 450 | planning de chantier / tâche / lot / jalon | chantier-intervention | planning, roles | oui | oui | oui | oui | non | procedure |
| 11 | chantiers/comment-suivre-la-rentabilite-de-mon-chantier-zc3nkk.md | 550 | rentabilité de chantier (prévue/réelle) | chantier-intervention | paiement, planning | oui | oui | oui | oui | non | reference_configuration |
| 12 | debuter-sur-costructor/comment-ajouter-mon-assurance-sur-mes-documents-uv3nwc.md | 150 | assurance décennale / mentions légales | indetermine | conformite_reglementaire, documents | oui | non | oui | oui | non | procedure |
| 13 | debuter-sur-costructor/comment-ajuster-les-categories-de-ventes-par-taux-de-tva-v48dla.md | 110 | catégorie comptable de vente / TVA | indetermine | conformite_reglementaire, roles | oui | non | oui | oui | non | reference_configuration |
| 14 | debuter-sur-costructor/comment-changer-la-methode-darrondi-de-tva-zvscnf.md | 170 | méthode d'arrondi de TVA | indetermine | conformite_reglementaire | oui | non | oui | non | non | procedure |
| 15 | debuter-sur-costructor/comment-configurer-mon-taux-de-marge-par-defaut-wqw4cd.md | 160 | taux de marge par défaut | indetermine | catalogue | oui | non | non | non | non | procedure |
| 16 | debuter-sur-costructor/comment-connecter-costructor-a-pennylane-14mfqxx.md | 25 (quasi uniquement captures d'écran, sans légende) | intégration comptable (Pennylane via Chift) | facturation | integrations | oui | non | non | non | non | procedure |
| 17 | debuter-sur-costructor/comment-connecter-costructor-a-votre-agent-ia-en-mcp-ey5k4v.md | 700 | serveur MCP / agent IA (intégration API) | indetermine | integrations, automatisation, securite_compte | oui | non | oui | oui | non | reference_configuration |
| 18 | debuter-sur-costructor/comment-connecter-son-compte-bancaire-xupyjb.md | 100 | compte bancaire (rapprochement) | indetermine | paiement, integrations | oui | oui | non | non | non | procedure |
| 19 | debuter-sur-costructor/comment-creer-une-cle-api-i7mrya.md | 160 | clé API | indetermine | integrations, securite_compte | oui | non | oui | oui | non | procedure |
| 20 | debuter-sur-costructor/comment-envoyer-une-demande-davis-1rmfknu.md | 220 | demande d'avis client (e-réputation) | facturation | automatisation, communication, notifications | oui | oui | oui | oui | non | procedure (ton partiellement promotionnel) |
| 21 | debuter-sur-costructor/comment-gerer-ses-stocks-cb6503.md | 190 | gestion de stock / produit | indetermine | gestion_stock, catalogue, automatisation | oui | oui | oui | non | non | procedure |
| 22 | debuter-sur-costructor/comment-importer-plus-de-100-millions-darticles-en-1-clic-div3pc.md | 350 | import produit (extension navigateur, catalogue fournisseur) | indetermine | catalogue, integrations, automatisation | oui | oui | oui | oui | oui | procedure |
| 23 | debuter-sur-costructor/comment-modifier-les-mentions-legales-de-mes-documents-1r8xgyu.md | 130 | mentions légales (documents) | indetermine | conformite_reglementaire, documents | oui | non | oui | non | non | procedure |
| 24 | debuter-sur-costructor/comment-parametrer-la-numerotation-des-factures-yovy8o.md | 130 | numérotation de facture | facturation | conformite_reglementaire | oui | non | oui | oui | non | procedure |
| 25 | debuter-sur-costructor/comment-parametrer-la-rentabilite-dma01r.md | 160 | rentabilité (marge + frais généraux) | indetermine | paiement | oui | non | oui | non | non | reference_configuration |
| 26 | debuter-sur-costructor/comment-parametrer-le-plan-comptable-et-les-comptes-auxiliaires-8bld86.md | 170 | plan comptable / comptes auxiliaires | indetermine | documents, roles | oui | non | oui | non | non | procedure |
| 27 | debuter-sur-costructor/comment-parametrer-les-categories-dachats-19pewed.md | 180 | catégorie d'achat (comptable) | achat | roles | oui | non | oui | non | non | procedure |
| 28 | debuter-sur-costructor/comment-personnaliser-le-nom-des-documents-pdf-11saa5b.md | 100 | nom de document PDF (personnalisation) | indetermine | documents | oui | non | non | non | non | procedure |
| 29 | debuter-sur-costructor/comment-personnaliser-les-modeles-demail-fjou49.md | 260 | modèle d'email / espace client | indetermine | communication, documents, notifications | oui | non | oui | oui | non | procedure |
| 30 | debuter-sur-costructor/comment-personnaliser-mes-documents-13ywvrp.md | 260 | personnalisation de documents (apparence/thème) | indetermine | documents, automatisation | oui | non | oui | oui | non | procedure |
| 31 | debuter-sur-costructor/comment-relancer-un-devis-en-attente-1vxtfm6.md | 200 | relance de devis | devis | automatisation, communication | oui | non | oui | oui | non | procedure |
| 32 | debuter-sur-costructor/comment-relancer-une-facture-impayee-1wfw3kk.md | 200 | relance de facture impayée | facturation | automatisation, communication | oui | non | oui | oui | non | procedure |
| 33 | debuter-sur-costructor/comment-supprimer-le-logo-costructor-de-mes-documents-1uh70of.md | 80 | logo (marque blanche, documents) | indetermine | documents | oui | non | oui | oui | non | procedure |
| 34 | debuter-sur-costructor/comment-supprimer-le-qrcode-des-documents-10oxf0t.md | 90 | QR Code (document) | indetermine | documents | oui | non | oui | oui | non | procedure |
| 35 | debuter-sur-costructor/comment-synchroniser-lagenda-costructor-avec-google-agenda-7f0syd.md | 160 | agenda (synchronisation Google Agenda) | chantier-intervention | planning, integrations | oui | non | non | oui | non | procedure |
| 36 | debuter-sur-costructor/comment-transferer-les-factures-electroniques-vers-une-adresse-mail-comptable-wizy4e.md | 150 | facturation électronique / transfert comptable | facturation | automatisation, integrations, communication | oui | non | non | non | non | procedure |
| 37 | debuter-sur-costructor/comment-utiliser-les-tags-analytiques-oa11ec.md | 220 | tag analytique (catégorisation transverse) | indetermine | recherche | oui | non | oui | oui | non | procedure |
| 38 | debuter-sur-costructor/inserer-mes-cgv-conditions-generales-de-ventes-vk2gwi.md | 110 | CGV (conditions générales de vente) | indetermine | conformite_reglementaire, documents | oui | non | non | non | non | procedure |
| 39 | debuter-sur-costructor/liste-des-fournisseurs-references-1rdft3t.md | 400 (essentiellement une table de liens) | liste de fournisseurs référencés (catalogue) | achat | catalogue, integrations | non | non | non | non | non | reference_configuration |
| 40 | debuter-sur-costructor/telecharger-lapplication-costructor-sur-mobile-s25hdg.md | 140 | application mobile (PWA) | indetermine | mobile | oui | non | non | non | non | procedure (ton partiellement promotionnel) |
| 41 | debuter-sur-costructor/telecharger-lapplication-costructor-sur-ordinateur-18x4qxr.md | 180 | application desktop (PWA) | indetermine | offline | oui | non | non | oui | non | procedure |
| 42 | equipe-collaborateurs/comment-inviter-mon-comptable-1gj4div.md | 130 | invitation comptable (accès externe) | indetermine | permissions, roles, notifications | oui | oui | non | non | non | procedure |
| 43 | equipe-collaborateurs/comment-utiliser-les-feuilles-dheures-ypj0g5.md | 400 | feuille d'heures / temps de travail | chantier-intervention | validation, permissions, roles | oui | oui | oui | oui | oui | procedure |
| 44 | gestion-dentreprise/comment-fonctionne-le-pilotage-fm83ry.md | 350 | pilotage (ventes/achats/trésorerie) | indetermine | paiement, recherche, automatisation | non | oui | oui | oui | non | definitionnel |
| 45 | gestion-dentreprise/comment-justifier-une-transaction-bancaire-7y52fe.md | 260 | rapprochement bancaire / transaction | indetermine | paiement, automatisation, recherche | oui | oui | oui | non | oui | procedure |
| 46 | gestion-dentreprise/comment-utiliser-lia-conversationnelle-1h3my79.md | 280 | agent IA conversationnel (assistant intégré) | indetermine | automatisation, integrations, communication | oui | non | non | non | non | procedure (ton partiellement promotionnel) |
| 47 | imports-exports/comment-exporter-mes-factures-de-ventes-1872kji.md | 130 | export de factures (CSV/XLSX/FEC) | facturation | documents, integrations, paiement | oui | non | oui | oui | non | procedure |
| 48 | imports-exports/comment-importer-des-produits-dans-ma-bibliotheque-vgrbpu.md | 150 | import de bibliothèque de produits (fichier CSV) | indetermine | catalogue, integrations | oui | non | oui | oui | non | procedure |
| 49 | imports-exports/comment-importer-un-devis-dpgf-dqe-excelpdf-1btrzbp.md | 310 | import de devis (DPGF/DQE, Excel/PDF) | devis | catalogue, integrations, automatisation | oui | oui | oui | oui | oui | procedure |
| 50 | imports-exports/comment-importer-une-ancienne-facture-15ddlrf.md | 140 | import d'une ancienne facture (rétro-saisie) | facturation | documents, integrations | oui | oui | non | non | non | procedure |
| 51 | imports-exports/comment-importer-une-facture-dachat-1fo750j.md | 230 | import de facture d'achat (dépôt fichier + transfert mail) | achat | documents, integrations, automatisation | oui | oui | non | non | non | procedure |
| 52 | imports-exports/comment-migrer-mes-donnees-dun-autre-logiciel-sur-costructor-1l718d6.md | 340 | migration de données (guide agrégateur, multi-objets) | indetermine | documents, integrations, communication | oui | non | oui | oui | non | autre (page-carrefour renvoyant vers d'autres articles + assistance humaine) |
| 53 | securite/comment-modifier-son-adresse-mail-de-connexion-son-mot-de-passe-175htc3.md | 100 | identifiants de connexion (email/mot de passe) | indetermine | securite_compte, roles | oui | non | non | non | oui | procedure |
| 54 | ventes/comment-acceder-et-utiliser-a-la-bibliotheque-costlib-1xxi4w7.md | 290 | bibliothèque collaborative d'ouvrages (Costlib) | devis | catalogue, communication | oui | oui | oui | non | non | procedure |
| 55 | ventes/comment-activer-le-calcul-des-marges-vv5czm.md | 150 | calcul de marge (option devis brouillon) | devis | catalogue | oui | non | oui | oui | non | procedure |
| 56 | ventes/comment-afficher-la-reference-dun-produit-sur-un-devis-ou-dune-facture-3mc3hp.md | 90 | référence produit (affichage sur document) | indetermine | catalogue, documents | oui | non | non | non | non | procedure |
| 57 | ventes/comment-afficher-le-decompte-general-sur-une-facture-de-situation-h7074x.md | 170 | décompte général (DGD) sur facture de situation | facturation | documents | oui | oui | oui | oui | non | procedure |
| 58 | ventes/comment-afficher-le-sous-total-des-sections-84iupw.md | 210 | sous-total de section (devis/facture) | indetermine | documents | oui | non | oui | oui | non | procedure |
| 59 | ventes/comment-ajouter-des-debours-sur-un-document-c8oa7n.md | 100 | débours (ajustement net à payer) | indetermine | paiement, documents | oui | non | non | non | non | procedure |
| 60 | ventes/comment-ajouter-la-colonne-ttc-sur-mes-documents-quiaob.md | 170 | colonne TTC (affichage document) | indetermine | documents, conformite_reglementaire | oui | non | oui | oui | non | procedure |
| 61 | ventes/comment-ajouter-une-piece-jointe-sur-un-document-miurrx.md | 260 | pièce jointe (devis/facture, brouillon ou finalisé) | indetermine | documents, notifications | oui | oui | oui | oui | non | procedure |
| 62 | ventes/comment-ajouter-une-plus-value-moins-value-sur-une-facture-c1xd5u.md | 240 | plus-value / moins-value (ligne de facture) | facturation | documents | oui | oui | oui | oui | non | procedure |
| 63 | ventes/comment-ajouter-une-retenue-de-garantie-tp6j75.md | 340 | retenue de garantie (RG) | facturation | paiement, conformite_reglementaire, notifications | oui | oui | oui | oui | non | procedure |
| 64 | ventes/comment-ajuster-la-marge-ou-les-prix-dun-devis-1pvn0w4.md | 260 | marge / prix (ajustement en masse sur devis) | devis | catalogue | oui | non | oui | oui | non | procedure |
| 65 | ventes/comment-annuler-une-facture-vb12e9.md | 220 | annulation de facture (avoir total) | facturation | conformite_reglementaire, documents | oui | oui | oui | oui | non | procedure |
| 66 | ventes/comment-consulter-le-statut-dun-email-envoye-9uearw.md | 280 | statut d'envoi d'email (devis/facture) | facturation | notifications, communication | oui | non | oui | oui | oui | procedure (avec lexique des statuts) |
| 67 | ventes/comment-creer-des-elements-et-les-organiser-dans-la-bibliotheque-1sh3nn2.md | 400 | élément de bibliothèque (produit, dossier, prix/marge) | indetermine | catalogue | oui | non | oui | non | non | procedure |
| 68 | ventes/comment-creer-un-bon-de-commande-client-1856wke.md | 750 | bon de commande client (création, conversion depuis devis) | devis | documents, catalogue, paiement | oui | oui | oui | oui | non | procedure |
| 69 | ventes/comment-creer-un-bon-de-livraison-1cu8wh8.md | 160 | bon de livraison (création, conversion depuis devis) | chantier-intervention | documents | oui | oui | non | non | non | procedure |
| 70 | ventes/comment-creer-un-client-prospect-ue8wib.md | 100 | client / prospect (fiche contact) | indetermine | roles | oui | non | oui | non | non | procedure |
| 71 | ventes/comment-creer-un-devis-ia-9jz7n7.md | 350 | devis généré par IA (prompt, pièce jointe, vocal) | devis | automatisation, documents | oui | oui | oui | oui | non | procedure (ton partiellement promotionnel) |
| 72 | ventes/comment-creer-un-etat-de-compte-client-1yzp3f5.md | 170 | état de compte client (récapitulatif factures/paiements) | facturation | paiement, documents | oui | non | oui | non | non | procedure |
| 73 | ventes/comment-creer-un-modele-de-devis-171gtrc.md | 140 | modèle de devis (réutilisable) | devis | documents, catalogue | oui | non | non | non | non | procedure |
| 74 | ventes/comment-creer-un-ouvrage-detaille-1sv5az8.md | 380 | ouvrage détaillé / composé (devis ou bibliothèque) | devis | catalogue | oui | oui | oui | non | non | procedure |
| 75 | ventes/comment-creer-une-facture-dacompte-fllvsr.md | 250 | facture d'acompte (transition depuis devis) | facturation | paiement, documents | oui | oui | oui | oui | non | procedure |
| 76 | ventes/comment-creer-une-facture-davoir-vwjxpf.md | 480 | facture d'avoir (partiel/total/libre, correction ou annulation) | facturation | paiement, documents | oui | oui | oui | oui | oui | procedure |
| 77 | ventes/comment-creer-une-facture-de-situation-1ptizga.md | 260 | facture de situation / d'avancement (transition depuis devis) | facturation | paiement, documents | oui | oui | oui | oui | non | procedure |
| 78 | ventes/comment-creer-une-facture-ndrp7y.md | 320 | facture (avec ou sans devis) | facturation | paiement, conformite_reglementaire, documents | oui | oui | oui | oui | non | procedure |
| 79 | ventes/comment-deduire-un-acompte-au-prorata-lwkl1w.md | 120 | acompte au prorata (déduction sur facture de situation) | facturation | paiement, automatisation | oui | non | oui | non | non | procedure |
| 80 | ventes/comment-enregistrer-un-reglement-sur-une-facture-j8zd6o.md | 170 | règlement (paiement sur facture) | facturation | paiement | oui | oui | non | non | non | procedure |
| 81 | ventes/comment-importer-des-lignes-dun-autre-document-1ph07xo.md | 210 | import de lignes inter-documents (devis/facture/BC/BI) | indetermine | documents, catalogue, automatisation | oui | oui | oui | oui | non | procedure |
| 82 | ventes/comment-imprimerenvoyer-une-facture-proforma-ou-un-devis-en-brouillon-yme5bk.md | 190 | facture proforma / devis en brouillon (filigrane) | indetermine | documents, communication | oui | non | oui | oui | non | procedure |
| 83 | ventes/comment-inserer-une-image-dans-un-document-1289smb.md | 150 | image (insertion sur ligne de document) | indetermine | documents, catalogue | oui | non | non | non | non | procedure (ton partiellement promotionnel) |
| 84 | ventes/comment-masquer-le-numero-de-revision-dun-devis-1miqhx5.md | 150 | numéro de révision de devis (masquage) | devis | documents | oui | non | oui | oui | non | procedure |
| 85 | ventes/comment-masquer-les-details-dun-ouvrage-1nm8dfh.md | 100 | détails d'ouvrage (masquage sur document) | indetermine | documents, catalogue | oui | non | non | non | non | procedure |
| 86 | ventes/comment-modifier-le-taux-de-tva-dun-document-y36yd8.md | 170 | taux de TVA (modification sur document) | indetermine | conformite_reglementaire, documents | oui | non | oui | oui | non | procedure |
| 87 | ventes/comment-modifier-supprimer-une-facture-1ex0kq5.md | 420 | modification/suppression de facture (encadrement légal anti-fraude TVA) | facturation | conformite_reglementaire, documents | oui | oui | oui | oui | oui | politique_legale (avec procédures associées) |
| 88 | ventes/comment-realiser-un-ajustement-ht-sur-le-net-a-payer-1h2vz89.md | 200 | ajustement HT / net à payer (devis ou facture) | indetermine | paiement, documents | oui | non | oui | non | non | procedure |
| 89 | ventes/comment-recuperer-une-version-anterieure-dun-devis-eg0od3.md | 230 | historique / révision de devis (restauration) | devis | documents | oui | oui | oui | oui | non | procedure |
| 90 | ventes/comment-rendre-optionnelle-une-ligne-ou-une-section-dans-un-devis-q3axji.md | 130 | ligne/section optionnelle (devis) | devis | catalogue | oui | non | oui | oui | non | procedure |
| 91 | ventes/comment-selectionner-les-options-avant-la-signature-electronique-du-devis-u2qvt.md | 150 | sélection d'options par le client (portail signature) | devis | catalogue, paiement | oui | oui | oui | oui | non | procedure |
| 92 | ventes/comment-supprimer-un-reglement-sur-une-facture-1jal4w6.md | 130 | règlement (suppression sur facture) | facturation | paiement | oui | oui | non | non | non | procedure |
| 93 | ventes/gestion-des-dechets-3t2w0p.md | 260 | gestion des déchets (obligation légale devis BTP, code de l'environnement) | devis | conformite_reglementaire | oui | non | oui | oui | non | politique_legale (avec méthode pratique conseillée) |
| 94 | ventes/recreer-un-ancien-devis-rcvxtx.md | 140 | numérotation forcée (recréation d'un ancien devis) | devis | documents, integrations | oui | non | oui | oui | non | procedure |

## Résultat mécanique final

Tous les totaux ci-dessous sont calculés par script (parsing des 94 lignes du
tableau, aucun comptage manuel).

- **Documents traités : 94/94** (périmètre gelé intégralement couvert).
- **Mots lus (somme mécanique de `longueur_mots`) : 20 055.**
- **Durée : CONTEXTE_SESSION_NON_MESURABLE** (aucune estimation produite).
- **Incidents : aucun** sur l'ensemble des 4 lots. Une correction mécanique a
  été appliquée en cours de vérification finale : la ligne 48 utilisait par
  erreur la valeur `catalogue` pour `moment_parcours`, hors du vocabulaire
  fermé (phases du cycle métier ou `indetermine`) — corrigée en
  `indetermine`, seule correction effectuée sur ce document, avant tout
  calcul d'agrégat.

### objet_principal

Champ ouvert/émergent par construction. **94 valeurs distinctes sur 94
documents** : aucune répartition en catégories fermées n'est produite (ce
serait fabriquer une taxonomie que le schéma LIGHT ne prévoit pas). On note
cependant des regroupements thématiques informels récurrents : documents
(fiches produits), facturation/paiement (règlements, avoirs, relances,
retenue de garantie), devis (création, modèles, ajustements, ouvrages),
imports/exports, et une poignée d'objets isolés notables (agent IA
conversationnel, devis généré par IA, serveur MCP, extension navigateur
fournisseur, programme de parrainage).

### moment_parcours (94 documents)

| valeur | n | % |
|---|---:|---:|
| indetermine | 48 | 51,1 % |
| facturation | 21 | 22,3 % |
| devis | 16 | 17,0 % |
| chantier-intervention | 6 | 6,4 % |
| achat | 3 | 3,2 % |
| **somme** | **94** | **100,0 %** |

**Taux `indetermine` : 51,1 % (48/94).** Ce taux confirme, sur un corpus de
production complet, l'observation déjà faite au pilote : une bonne moitié
des articles d'aide Costructor documentent des réglages/options transverses
(affichage, personnalisation, sécurité, comptabilité) qui ne se rattachent
pas à une phase précise du cycle métier — ce n'est pas une faiblesse de
LIGHT, c'est une propriété du corpus.

### capacites_transverses (occurrences, un document peut en porter jusqu'à 3)

| capacité | n |
|---|---:|
| documents | 42 |
| paiement | 27 |
| catalogue | 20 |
| integrations | 17 |
| automatisation | 16 |
| conformite_reglementaire | 13 |
| communication | 11 |
| roles | 8 |
| notifications | 6 |
| planning | 3 |
| securite_compte | 3 |
| recherche | 3 |
| permissions | 2 |
| gestion_stock | 1 |
| mobile | 1 |
| offline | 1 |
| validation | 1 |

### genre_documentaire (94 documents)

| valeur | n | % |
|---|---:|---:|
| procedure | 78 | 83,0 % |
| procedure (ton partiellement promotionnel) | 5 | 5,3 % |
| reference_configuration | 6 | 6,4 % |
| procedure (avec lexique des statuts) | 1 | 1,1 % |
| definitionnel | 1 | 1,1 % |
| autre (page-carrefour renvoyant vers d'autres articles + assistance humaine) | 1 | 1,1 % |
| politique_legale (avec procédures associées) | 1 | 1,1 % |
| politique_legale (avec méthode pratique conseillée) | 1 | 1,1 % |
| **somme** | **94** | **100,0 %** |

En regroupant les variantes annotées à leur catégorie de base : procédure
(84/94, 89,4 %), reference_configuration (6/94, 6,4 %), politique_legale
(2/94, 2,1 %), definitionnel (1/94, 1,1 %), autre (1/94, 1,1 %).

### contenu_observable (5 booléens, 94 documents, oui/non/inconnu)

| champ | oui | non | inconnu |
|---|---:|---:|---:|
| procedure | 92 | 2 | 0 |
| transition_objet | 35 | 59 | 0 |
| regle_ou_condition | 68 | 26 | 0 |
| contrainte_ou_limite | 53 | 41 | 0 |
| exception_ou_correction | 8 | 86 | 0 |

Aucune valeur `inconnu` n'a été nécessaire sur ce lot : les 94 documents
étaient chacun suffisamment explicites pour trancher les 5 booléens de
manière factuelle.

### Cas que LIGHT représente mal

- **Pages-carrefour / hub multi-objets** (doc 52, migration de données) :
  LIGHT force un `objet_principal` et un `moment_parcours` uniques alors
  que le document agrège plusieurs objets (clients, bibliothèque, devis,
  factures) et renvoie vers d'autres articles. Le `genre_documentaire`
  `autre` a dû être inventé hors du vocabulaire de base pour ne pas forcer
  une catégorie inadéquate.
- **Contenu réglementaire non spécifique au logiciel** (doc 87 — loi
  anti-fraude TVA de 2018, amende de 7 500 € ; doc 93 — obligation légale
  du code de l'environnement sur les déchets de chantier) : ces documents
  sont davantage des fiches de conformité juridique illustrées par des
  procédures Costructor que des documentations produit au sens strict.
  LIGHT les code correctement (`politique_legale`) mais le schéma ne capture
  pas la distinction « obligation légale externe » vs « fonctionnalité
  propriétaire », ce qui aplatit une différence de nature importante pour
  une lecture concurrentielle.
- **Fonctionnalités IA émergentes** (doc 46 — agent conversationnel intégré ;
  doc 71 — génération de devis par IA) : `objet_principal` capture bien
  l'objet mais `capacites_transverses` (vocabulaire encore restreint,
  ex. `automatisation`) ne rend pas la spécificité de ces mécanismes
  (agent conversationnel multi-tours, génération structurée à partir d'un
  prompt) — un signal faible mais récurrent (avec le serveur MCP du pilote
  précédent) que Costructor investit sur des capacités IA que le
  vocabulaire actuel de LIGHT sous-décrit.
- **Contenu quasi vide / à dominante visuelle** (ex. connexion Pennylane,
  ~25 mots hors légendes de captures d'écran) : `longueur_mots` reste
  mesurable mais très peu représentatif du contenu réel du document
  (majoritairement des images non-OCRisées) — un biais déjà identifié au
  pilote, confirmé ici sur un nouveau cas.
