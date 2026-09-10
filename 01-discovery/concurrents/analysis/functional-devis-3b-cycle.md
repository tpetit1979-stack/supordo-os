# 3B — Cycle de vie du devis : exploitation fonctionnelle ciblée

Mission ciblée, un seul sous-problème (ce qui peut arriver à un devis déjà
créé, jusqu'à sa sortie du cycle de devis), un seul livrable, un seul
verdict, puis stop. Ne reconstruit pas la naissance du devis (acquise par
`functional-devis-3a-naissance.md`, verdict `DEVIS_3A_TERMINE — EXPLOITABLE
— STOP`), ne modifie pas LIGHT/V2/V3, ne prend aucune décision produit
SUPORDO définitive.

## 1. Question et périmètre

> Une fois qu'un devis créé existe, que peut-il lui arriver jusqu'à sa
> sortie du cycle de devis ? Quelles actions peuvent être réalisées sur un
> devis existant, depuis quels états ou contextes, sous quelles conditions,
> avec quels effets, et vers quels nouveaux états ou situations ?

Périmètre : le devis commence à exister (3A acquis, non refait). Sont
étudiés, lorsqu'ils sont documentés : édition, réutilisation/évolution
(duplication, variante, révision, avenant), génération/envoi de document,
communication, engagement (soumission, validation, acceptation, refus,
signature), fin/administration (annulation, suppression, archivage,
restauration, expiration).

Explicitement hors périmètre, quelle que soit la richesse rencontrée en
lecture : spécification SUPORDO finale, schéma Supabase, API, frontend,
machine d'états SUPORDO, backlog, analyse complète devis → facture/commande/
intervention (seule la frontière immédiate devis→facture est effleurée
quand elle éclaire une frontière de mutabilité, jamais approfondie),
architecture générique de workflow, nouvelle taxonomie méthodologique.

## 2. Corpus et méthode réellement utilisés

### 2.1 Instruments consultés avant lecture

`CLAUDE.md`, `functional-devis-3a-naissance.md` (intégral), `functional-propagation-pilot.md` (intégral), `functional-onboarding-pilot.md` (extrait), `01-discovery/ARBORESCENCE.md` (intégral) lus avant toute sélection de sources, conformément à la section 0 de la mission. `functional-devis-3a-naissance.md` a servi de routage (mêmes 8 corpus, même séparation stricte OpenFire Zendesk/Odoo) et d'inventaire des sujets explicitement exclus de 3A (cycle de vie post-création, précisément le périmètre de 3B).

### 2.2 Méthode de sélection

Les 8 corpus retenus par 3A sont conservés à l'identique pour garantir la comparabilité directe des deux missions : Vertuoza, InterFast, Axonaut, Sellsy, OpenFire (Zendesk), OpenFire (Odoo), Obat, Costructor. Séparation stricte OpenFire maintenue (deux agents indépendants, aucun accès croisé).

Pour chaque éditeur, une liste fermée de fichiers a été constituée par inspection directe de l'arborescence physique des corpus sources (rubriques `devis/`, `gerez-vos-devis/`, `documents-de-vente/`, `ventes/`, `finances/`, `gestion-de-chantier/`, `knowsystem/`, `centre_aide/`), puis élargie par recherche de motifs sur les noms de fichiers (`devis`, `statut`, `signat`, `accept`, `refus`, `annul`, `archiv`, `dupliqu`, `revision`, `variante`, `envoi`, `email`, `expir`, `final`, `valid`, `soumettre`, `supprim`, `restaur`, `telecharg`, `imprim`, `pdf`, `partage`, `portail`, `kanban`, `export`). Les fichiers déjà exploités en détail par 3A pour la seule naissance du devis (formulaires de création) n'ont pas été systématiquement repris, sauf quand un même fichier couvrait aussi des actions post-création. Un petit nombre de fichiers portant sur un objet voisin (facture, paiement, opportunité) a été inclus délibérément comme corroboration/contraste chez OpenFire (Odoo) et Obat, avec instruction explicite aux agents de ne jamais les traiter comme portant directement sur le devis sauf mention explicite.

Chaque éditeur a été confié à un agent dédié, contraint à sa liste fermée, lecture intégrale obligatoire, aucune autre source autorisée (pas de web, pas d'autre éditeur, pas de mémoire générale du modèle). Aucun agent n'a eu accès aux rapports des autres — le rapprochement inter-éditeurs qui suit est fait après coup, à partir des 8 rapports reçus séparément, selon le même protocole que 3A et le pilote propagation.

### 2.3 Couverture

| Éditeur | Fichiers dans la liste fermée | Fichiers exploités | Fichiers sans apport |
|---|---:|---:|---:|
| Vertuoza | 28 | 14 apport direct + 5 indirect | 9 (paramétrage de mise en page, objets voisins hors sujet) |
| InterFast | 15 | 12 (fort/moyen) | 2 (branding pur), 1 faible |
| Axonaut | 13 | 11 | 2 (lettre de mission — objet distinct du devis) |
| Sellsy | 19 | 19 (tous exploités à des degrés divers) | 0 |
| OpenFire (Zendesk) | 7 | 5 | 2 (stubs, dont un contenu mal indexé) |
| OpenFire (Odoo) | 12 | 6 directs + 4 corroboration objet voisin | 2 (vidéo replay, campagnes marketing) |
| Obat | 14 | 9 forts + 3 marginaux | 2 (renvoi vidéo, page sommaire) |
| Costructor | 14 | 12 | 1 (modèles de devis, hors cycle de vie) |

Rendement très inégal entre éditeurs : Sellsy, Vertuoza, InterFast et Costructor produisent une matière riche et croisée ; OpenFire (Zendesk) et OpenFire (Odoo) restent pauvres à moyens sur cette question précise (constat assumé, pas un défaut d'extraction — leur documentation se concentre ailleurs, comme déjà noté par 3A).

### 2.4 Discipline de preuve

Identique à 3A et au pilote propagation : FAIT DOCUMENTÉ (citation exacte + chemin) / INTERPRÉTATION (marquée comme telle) / NON DÉTERMINÉ (silence documentaire ≠ absence fonctionnelle). Chaque agent avait consigne explicite de ne jamais fusionner enregistrer/finaliser/numéroter/générer le PDF/envoyer/accepter/signer/valider sans vérification, et de ne jamais inventer de cause légale/comptable/technique à un verrou non justifié dans la source. Deux tensions documentaires internes à un même éditeur ont été relevées et conservées telles quelles plutôt que résolues arbitrairement (Axonaut §3, InterFast §6).

## 3. Inventaire des états par éditeur

| Éditeur | Terme exact | Signification observable | Nature | Source (rapport d'agent) |
|---|---|---|---|---|
| Vertuoza | Draft | « le devis n'a pas encore été Soumis » | utilisateur/système, réversible | `devis/devis.md` |
| Vertuoza | A envoyer | enregistré, pas encore envoyé | système, réversible | `devis/devis.md` |
| Vertuoza | Envoyé | envoyé, pas encore accepté | système, réversible | `devis/devis.md` |
| Vertuoza | SIGNÉ | signature électronique client ; **distinct** de l'acceptation | système, transitoire | `devis/signature-electronique-du-devis.md` |
| Vertuoza | Chantier en cours | accepté et transformé en chantier | système, quasi-terminal (réversible par suppression du chantier vide) | `devis/devis.md` |
| Vertuoza | Refusé | refusé par le client, sorti du filtre par défaut mais conservé | système/utilisateur, terminal non confirmé | `devis/devis.md` |
| InterFast | Brouillon | en cours d'édition, aucun numéro | système, réversible, éditable | `finances/comprendre-la-fiche-d-un-devis.md` |
| InterFast | Finalisé | numéro de référence attribué | système, suppression bloquée | idem |
| InterFast | Envoyé | transmis au client | système, réversible depuis Accepté | idem |
| InterFast | Accepté | client a accepté (signature manuelle ou électronique) | système, « figé », réversible manuellement vers Envoyé | idem |
| InterFast | Facturé | intégralement facturé | système, verrouillé | idem |
| InterFast | Refusé | rejeté par le client | système, réversibilité NON DÉTERMINÉE | idem |
| InterFast | Annulé | abandonné à la discrétion de l'artisan | système, archivage réversible | idem |
| InterFast | (filtre) date de validité dépassée | critère de recherche, **pas un des 7 statuts** | calculé/implicite | `finances/comprendre-le-tableau-des-devis.md` |
| Axonaut | Devis en attente | créé, envoyé, pas encore accepté/refusé — **mais aussi** utilisé pour un devis tout juste créé et pas encore envoyé (tension documentaire, voir §10) | utilisateur/système, non terminal | `gerez-vos-devis/modifier-un-devis.md` vs `envoyer-mes-devis-depuis-axonaut.md` |
| Axonaut | Devis accepté | validé par le client, crée une commande liée | système, verrouille l'édition directe | `gerez-vos-devis/modifier-un-devis.md` |
| Axonaut | Devis refusé | rejeté/annulé | utilisateur, réversibilité NON DÉTERMINÉE | idem |
| Sellsy | Brouillon | statut initial, non numéroté | utilisateur/système, réversible | `documents-de-vente/les-factures-et-les-avoirs-brouillon.md` |
| Sellsy | Envoyé | envoi email standard OU envoi pour signature | système, déclenché automatiquement | `documents-de-vente/statuts-de-documents.md` |
| Sellsy | Accepté | tous les signataires ont signé | système, déclencheur d'automatisations | `documents-de-vente/envoyer-un-document-pour-signature-electronique.md` |
| Sellsy | Facturé | converti en facture (ou forcé manuellement sans conversion réelle) | système/utilisateur | `documents-de-vente/statuts-de-documents.md` |
| Sellsy | Expiré | date « à signer avant le » dépassée | calculé, bloque signature et paiement en ligne | idem |
| Sellsy | Annulé | statut manuel, hors facture/avoir | utilisateur, terminal non destructif | `documents-de-vente/supprimer-un-document-de-vente.md` |
| Sellsy | *(rappel)* « Ces statuts diffèrent d'un type de document à l'autre » — pas de liste unique et officielle pour le devis | — | — | `documents-de-vente/statuts-de-documents.md` |
| OpenFire (Zendesk) | Bon de commande | statut atteint après « Confirmer la vente » | système | `utiliser-openfire/creer-et-personnaliser-votre-devis.md` |
| OpenFire (Zendesk) | Devis envoyé (case) | indicateur booléen, pas un statut de workflow | système/utilisateur | idem |
| OpenFire (Zendesk) | Brouillon | génération automatique désactivée depuis une intervention | système | `configurer-openfire/configurer-la-generation-des-devis...md` |
| OpenFire (Zendesk) | Statut de facturation / statut de livraison | champs calculés, apparaissant seulement après transformation en bon de commande | calculé | `utiliser-openfire/creer-et-personnaliser-votre-devis.md` |
| OpenFire (Odoo) | « estimation, devis, bon de commande = un seul et même document dont l'état évolue » | progression non détaillée dans ses transitions | système | `creer-un-devis-1.md` |
| OpenFire (Odoo) | Annulé | déclenché en cascade quand l'opportunité liée est marquée perdue | système, automatique | `faire-evoluer-l-opportunite-189.md` — comble un trou signalé par 3A |
| OpenFire (Odoo) | Demande de signature envoyée / Devis signés | filtres de recherche liés à la signature électronique | système | `mise-en-place-de-la-signature-electronique-261.md` |
| Obat | Brouillon | créé/enregistré, non finalisé | utilisateur, réversible | `comment-passer-vos-devis-en-factures...md` |
| Obat | Finalisé | numéro définitif attribué | utilisateur, reste modifiable | idem ; `les-variantes-de-devis-dans-obat.md` |
| Obat | Envoyé | transmis au client | utilisateur, reste modifiable | idem |
| Obat | Signé | accepté/signé (auto si signature électronique, manuel sinon) | système/utilisateur, **verrouille modification et suppression**, réversible via « annulation de signature » | `comment-facturer-un-acompte-depuis-un-devis-sur-obat.md`, `variantes-de-devis-vos-references...md` |
| Obat | Refusé | statut Kanban, aucune transition sortante documentée | utilisateur, terminal apparent | Vue Kanban (⚠️ fonctionnalité « Bientôt disponible », voir §12) |
| Obat | Annulé | (a) automatique pour le parent + variantes non retenues quand une variante est signée ; (b) filtre de liste | système (a) / mécanisme manuel non documenté (b) | `les-variantes-de-devis-dans-obat.md` |
| Costructor | brouillon | en construction, filigrane, non engageant | utilisateur/système, réversible | `comment-imprimerenvoyer-une-facture-proforma-ou-un-devis-en-brouillon...md` |
| Costructor | en attente | envoyé, cible des relances | système | `comment-relancer-un-devis-en-attente...md` |
| Costructor | accepté | atteint automatiquement après signature électronique réussie | système/calculé | `comment-signer-un-devis-electroniquement...md` |
| Costructor | finalisé | préalable à la conversion en bon de commande | utilisateur, NON DÉTERMINÉ si distinct d'« en attente » | `comment-creer-un-bon-de-commande-client...md` |
| Costructor | numéro de révision (v1, v2…) | marqueur de version auto-généré à chaque modification, **pas** un état commercial | calculé/implicite | `comment-masquer-le-numero-de-revision-dun-devis...md` |
| Costructor | *(absent)* « refusé » | aucun terme de ce type dans le corpus lu | — | — |

**Constat transversal** : aucun éditeur n'emploie un vocabulaire d'état identique à un autre ; seul InterFast documente une liste complète et stable de 7 statuts confirmée par deux sources indépendantes et concordantes. Les autres éditeurs présentent des listes partielles, parfois contradictoires en interne (Axonaut), parfois conditionnées (Obat, avec une fonctionnalité Kanban non confirmée en production), ou fusionnent devis et facture dans un même vocabulaire de statuts (Sellsy, « document de vente »). Un même mot peut désigner des choses différentes d'un éditeur à l'autre : « révision » signifie chez Vertuoza une formule d'indexation de prix affichée en totaux avant/après (rien à voir avec une nouvelle version du document), et chez Costructor un marqueur de version automatique du même objet — piège terminologique à ne jamais résoudre par généralisation (voir §8).

## 4. Inventaire des actions

Actions significatives documentées par au moins un éditeur, au-delà de la simple communication (édition de contenu déjà couverte par 3A pour la phase de naissance, ici uniquement pour un devis déjà créé) :

- **Édition** : modifier le contenu (lignes, prix, remise, TVA, client), modifier l'auteur, réordonner/supprimer une ligne, forcer un statut de facturation/livraison, ajuster marge/prix en masse, rendre une ligne/section optionnelle.
- **Réutilisation/évolution** : dupliquer, créer une variante, créer une révision (historique auto), créer un avenant, remplacer/basculer le devis principal, recréer un ancien devis (migration).
- **Document** : générer/imprimer le PDF, exporter (Excel, ZIP), aperçu client, personnaliser le canal d'envoi (PJ vs lien « espace client »).
- **Communication** : envoyer par email, déclarer envoyé (sans passer par l'email de l'outil), relancer (manuel ou automatique), partager via lien public, suivre le statut de l'email (délivré/ouvert/cliqué).
- **Engagement** : soumettre, finaliser/numéroter, accepter, refuser, signer électroniquement, sélectionner des options avant signature, confirmer la vente, annuler une signature.
- **Fin/administration** : annuler, supprimer, archiver (chantier, pas le devis lui-même sauf Sellsy), restaurer (portée limitée, voir §9), expirer.

## 5. Matrice ACTION × ÉTAT/CONTEXTE × CONDITION × EFFET

Sélection des couples les plus structurants et les mieux sourcés (matrice complète disponible dans les 8 rapports d'agents sous-jacents — non reproduite intégralement pour éviter la duplication).

| Éditeur | ACTION | ÉTAT/CONTEXTE SOURCE | CONDITION | EFFET | ÉTAT/SITUATION CIBLE |
|---|---|---|---|---|---|
| Vertuoza | Accepter | Envoyé ou Signé | bouton d'action en liste | transformation en chantier | Chantier en cours |
| Vertuoza | Créer un avenant | Chantier en cours | menu Gestion de chantier | nouveau document additif, lignes du devis de base cochables | Avenant créé (Brouillon) |
| Vertuoza | Supprimer le chantier | Chantier en cours | aucun document généré dans le chantier | chantier supprimé | Devis réouvert, modifiable |
| InterFast | Accepter (signature manuelle/électronique) | Envoyé | — | devis « figé » | Accepté |
| InterFast | Retour temporaire à Envoyé | Accepté | action manuelle, désactiver relances avant | déverrouille l'éditeur | Envoyé |
| InterFast | Créer un avenant | Devis Accepté | — | nouveau document lié financièrement/commercialement | Avenant (cycle propre) |
| Axonaut | Accepter | Devis en attente | icône sablier + bouton vert, ou signature électronique, ou paiement en ligne | crée automatiquement une commande | Devis accepté (verrou indirect via la commande) |
| Axonaut | Supprimer la commande | Devis accepté | commande sans documents associés | « remet le devis à l'état en attente » | Devis en attente, modifiable |
| Sellsy | Envoyer pour signature | document édité | module activé, destinataire avec téléphone+email | passage auto de statut | Envoyé |
| Sellsy | Signature complète (tous signataires) | Envoyé (signature) | — | « légalement plus modifiable » | Accepté |
| Sellsy | Convertir en facture | Devis (tout statut modifiable) | seul moyen documenté de lier deux documents de vente | nouveau document créé, infos reprises | Devis → Facturé (devis conservé, consultable) |
| OpenFire (Zendesk) | Confirmer la vente | Devis signé par le client | bouton « Confirmer la vente » | passage de statut | Bon de commande |
| OpenFire (Zendesk) | Génération auto + confirmation auto depuis intervention | Modèle d'intervention configuré | option « Confirmer automatiquement » activée | devis généré ET confirmé ; non éditable depuis l'appli terrain | Bon de commande |
| OpenFire (Odoo) | Marquer l'opportunité perdue | opportunité liée à un/des devis | clic « MARQUER COMME PERDU » | annulation automatique en cascade, sans action directe sur le devis | Annulé |
| Obat | Créer une variante | Finalisé ou Envoyé | bouton « Créer une variante » | duplication intégrale automatique, pas de ressaisie | Nouvel objet lié, visible dans l'encart Variantes |
| Obat | Signer une variante | Variante Finalisé/Envoyé | passage au statut Signé | devient la version retenue ; parent + autres variantes → Annulé | Signé (retenue) |
| Obat | Annuler une signature | Signé (erreur) | — | retour au statut antérieur, pastilles réapparaissent | Finalisé ou Envoyé (recovery documenté) |
| Costructor | Signer électroniquement | Devis envoyé | signature électronique activée | signature apposée | accepté (automatique) |
| Costructor | Modifier un devis déjà signé | Accepté | — | signature invalidée (pas de blocage technique documenté) | doit être re-signé |
| Costructor | Créer un avenant | Devis initial existant | aucune condition explicite | nouveau devis via bouton standard « + Nouveau devis », lignes saisies manuellement | Nouvel objet devis distinct |

Le détail complet (acteur, confirmation, notification, réversibilité, trace/historique, point d'entrée UX, exception) est conservé au niveau de chaque rapport d'agent et repris par thème dans les sections suivantes.

## 6. Frontières de mutabilité

Sous-question prioritaire de la mission. Résultat central : **il n'existe pas un modèle unique de verrouillage du devis sur le marché observé — cinq modèles distincts coexistent**, souvent sur le même événement déclencheur nominal (« acceptation » ou « signature »).

### 6.1 Par éditeur

| Éditeur | Événement verrouillant | Ce qui devient impossible | Ce qui reste possible | Recovery documenté | Source |
|---|---|---|---|---|---|
| Vertuoza | Acceptation (→ Chantier en cours) | modification **directe** du devis | avenant, export, consultation historique | supprimer le chantier (si vide de documents) → devis réouvert, **même objet** | `faq-foires-aux-questions/que-faire-si-je-dois-modifier-un-devis-deja-accepte.md` |
| InterFast | Acceptation (→ Accepté) | édition directe du contenu, accès au nouvel éditeur | consultation, avenant, planification d'intervention, facturation | retour temporaire au statut Envoyé (désactiver les relances avant) | `finances/comprendre-la-fiche-d-un-devis.md` (FAQ) |
| InterFast | Facturation (→ Facturé) | édition directe | — | annuler la facture, ou Annulé→Accepté | `finances/modifier-un-devis.md` |
| Axonaut | Acceptation — **verrou indirect** : c'est la commande liée qui se verrouille, pas le devis lui-même | modification/suppression **directe** du devis via son interface propre | modification via la commande liée | supprimer la commande (si aucun document associé) → devis repasse « en attente » | `gerez-vos-devis/modifier-un-devis.md` |
| Sellsy | Signature **complète** par tous les signataires (pas l'envoi en signature, pas l'acceptation seule) | modification du document | consultation | aucune — verrou présenté comme définitif (« légalement plus modifiable ») | `documents-de-vente/envoyer-un-document-pour-signature-electronique.md` |
| Sellsy (comparaison) | Facture : sortie du statut Brouillon | modification/suppression directe | consultation, avoir | avoir + nouvelle facture | `documents-de-vente/statuts-de-documents.md` |
| OpenFire (Zendesk) | Confirmation automatique **spécifiquement sur l'application terrain/mobile** | édition depuis l'app terrain | NON DÉTERMINÉ pour le desktop | NON DÉTERMINÉ | `configurer-openfire/configurer-la-generation-des-devis...md` — portée limitée, à ne pas généraliser |
| OpenFire (Odoo) | **Aucun verrou documenté** sur le devis lui-même, ni à la signature, ni à l'acceptation, ni au passage en bon de commande | — | — | — | silence documentaire, contrastant explicitement avec le verrou légal de la facture et le verrou opérationnel du paiement, documentés eux dans le même corpus |
| Obat | Signature (→ Signé) | « vous ne pourrez alors plus le modifier ni le supprimer » | facturer le devis signé | **« annuler une signature »** : retour documenté au statut antérieur (Finalisé ou Envoyé), pastilles réapparaissent — mécanisme de réversibilité explicite unique dans le corpus | `comment-facturer-un-acompte-depuis-un-devis-sur-obat.md`, `variantes-de-devis-vos-references...md` |
| Costructor | **Aucun verrou technique documenté** — modifier un devis signé reste possible mais invalide la signature, obligeant une nouvelle signature | rien de bloqué techniquement | modification libre | re-signature par le client | `comment-masquer-le-numero-de-revision-dun-devis...md` |

### 6.2 Les cinq modèles observés

1. **Verrou direct et dur sur le devis, au moment de la signature/acceptation, avec recovery explicite** — Obat (« annulation de signature », le seul mécanisme de déverrouillage direct et nommé du corpus).
2. **Verrou direct et dur sur le devis, avec recovery indirect via un objet parent/enfant** — Vertuoza (suppression du chantier vide), InterFast (retour temporaire au statut Envoyé, ou déverrouillage de la facture).
3. **Verrou indirect : le devis n'est jamais verrouillé lui-même, c'est l'objet créé à l'acceptation qui l'est** — Axonaut (la commande).
4. **Verrou dur et présenté comme définitif, sans recovery documenté** — Sellsy, mais seulement à la signature *complète* (pas à l'envoi en signature ni à l'acceptation simple).
5. **Absence de verrou technique, remplacée par une invalidation logique nécessitant une nouvelle validation** — Costructor (re-signature), OpenFire Zendesk (portée mobile seulement, desktop NON DÉTERMINÉ), OpenFire Odoo (aucun verrou documenté du tout).

**Lecture structurante** : contrairement à la facture — verrouillée par une cause réglementaire quasi unanime chez 6 éditeurs sur 7 selon le pilote propagation (§6.1 du pilote, INV-1) — le devis n'a **aucune cause réglementaire documentée** pour son propre verrouillage dans aucun des 8 corpus lus ici. Quand un verrou existe, sa cause est **toujours métier ou technique**, jamais légale, et sa portée exacte (objet lui-même vs objet lié) varie fortement. Ceci confirme et affine, sur le sous-domaine précis du devis, le motif déjà observé par le pilote propagation (INV-6, « réserve sur la généralisation ») : le verrou du devis accepté est un CANDIDAT plausible mais nettement moins robuste et nettement moins uniforme que le verrou de la facture.

### 6.3 Numérotation et suppression — un verrou distinct de l'acceptation

Chez InterFast et Obat, la **numérotation** (finalisation) constitue un verrou distinct et antérieur à l'acceptation, mais porte uniquement sur la **suppression**, pas sur l'édition du contenu : « un devis avec numéro ne peut plus être modifiée » (InterFast, tension notée en §10) coexiste avec « il sera donc impossible de le supprimer » comme énoncé séparé et plus robuste. Chez Obat, la numérotation verrouille le **format** de la séquence pour tous les documents futurs du même préfixe, pas le contenu du document lui-même. Ce verrou de suppression-par-numérotation est structurellement proche du motif « continuité de numérotation » déjà isolé par le pilote propagation pour la facture (§6.2 du pilote), mais appliqué ici au devis sans qu'aucune source ne l'justifie par une obligation légale — silence à ne pas combler par déduction.

## 7. Finalisation / numérotation / envoi / acceptation / signature — événements distincts, jamais fusionnés

Conformément à la consigne de mission (§3), chaque événement a été vérifié séparément dans chaque corpus. Résultat : **ce sont bien des événements distincts, aux effets différents, et leur articulation exacte varie par éditeur** — aucune paire n'est interchangeable sur l'ensemble du marché.

| Événement | Effet typiquement observé | Éditeurs où il est **clairement distinct** d'un événement voisin | Éditeurs où deux événements semblent fusionnés ou dont l'articulation reste floue |
|---|---|---|---|
| Enregistrer | sauvegarde sans numéro, aucun effet d'état fort | tous (où documenté) | — |
| Finaliser / numéroter | attribution du numéro définitif, verrouille la **suppression** (pas toujours l'édition) | InterFast, Obat, Costructor (implicite) | Vertuoza (moment exact d'attribution NON DÉTERMINÉ) |
| Générer le PDF / imprimer | aucun effet d'état documenté nulle part | Vertuoza, OpenFire Zendesk, OpenFire Odoo, Sellsy, Costructor | — (convergence forte : simple sortie de document) |
| Envoyer | déclenche un statut « Envoyé » ou une simple coche/indicateur ; **n'entame pas l'éditabilité** chez la majorité des éditeurs qui documentent ce point | Vertuoza (« complètement éditable » durant Draft/A envoyer/Envoyé), Axonaut (le blocage vient de l'acceptation, pas de l'envoi), Sellsy (envoi ≠ signature) | InterFast (tension entre deux articles sur la mutabilité du champ client au statut Envoyé, §10) |
| Signer électroniquement | chez plusieurs éditeurs, **événement distinct de l'acceptation** — signer ne suffit pas toujours à faire progresser l'état commercial | Vertuoza (SIGNÉ ≠ Chantier en cours, une action « Accepter » reste nécessaire), OpenFire Zendesk (lien exact signature→confirmation non détaillé, mais les deux boutons sont distincts) | Obat, Costructor, Sellsy, InterFast (chez ces quatre, signature complète déclenche **directement** l'état « accepté »/« signé » — un seul événement) |
| Accepter / valider | déclenche un objet lié (commande, chantier, facture) et/ou verrouille le devis | Vertuoza (→ chantier), Axonaut (→ commande), OpenFire Zendesk (→ bon de commande, action « Confirmer la vente » séparée de la signature) | Obat, Costructor (signature = acceptation, un seul événement) |

**Lecture structurante** : le marché se scinde en deux familles nettes sur l'articulation signature/acceptation — une famille où **signer ≠ accepter** (Vertuoza, OpenFire Zendesk) et une famille où **signer = accepter automatiquement** (Obat, Costructor, Sellsy pour la signature complète, InterFast où la signature électronique aboutit directement au statut Accepté). Ce n'est pas un détail : c'est une divergence de modèle qui conditionne directement si SUPORDO doit prévoir une étape d'acceptation manuelle distincte de la signature ou fusionner les deux.

## 8. Duplication / variante / révision / avenant

Quatre mécanismes distincts, traités séparément conformément à la consigne de mission. Aucun éditeur ne documente les quatre à la fois.

### 8.1 Duplication (nouvel objet indépendant, lien rompu ou non précisé)

| Éditeur | Nouvel objet ? | Ancien conservé ? | Lien conservé ? | Lignes reprises ? | Numéro | État du précédent | Source |
|---|---|---|---|---|---|---|---|
| Vertuoza | oui (bouton existe) | NON DÉTERMINÉ | NON DÉTERMINÉ | NON DÉTERMINÉ | NON DÉTERMINÉ | NON DÉTERMINÉ | `devis/devis.md` — mention du bouton seule |
| InterFast | oui | oui | NON DÉTERMINÉ | oui, intégralement **sauf** conditions de paiement et infos bancaires | NON DÉTERMINÉ (probablement nouveau) | inchangé | `finances/comprendre-la-fiche-d-un-devis.md` |
| Sellsy | oui | oui | **explicitement rompu** : « la copie ne sera pas rattachée au cycle de vente du document d'origine » | INTERPRÉTATION (contenu présumé repris) | NON DÉTERMINÉ | inchangé | `documents-de-vente/creer-une-facture-un-devis-un-document-de-vente.md` |
| Obat | oui (bouton distinct de « Créer une variante ») | NON DÉTERMINÉ | NON DÉTERMINÉ | NON DÉTERMINÉ (article dédié absent du corpus lu) | NON DÉTERMINÉ | NON DÉTERMINÉ | `les-variantes-de-devis-dans-obat.md` — existence du bouton seule |
| Costructor | oui, mais **seulement documenté dans le contexte d'une ancienne révision** (« Récupérer une version antérieure ») | oui | NON DÉTERMINÉ pour le cas général | INTERPRÉTATION | nouveau numéro, distinct | inchangé | `comment-recuperer-une-version-anterieure-dun-devis...md` |
| Axonaut, OpenFire (Zendesk), OpenFire (Odoo) | NON DÉTERMINÉ — silence total, fonctionnalité non documentée dans le périmètre lu | — | — | — | — | — | — |

### 8.2 Variante (objet lié, coexistant, concurrent)

Mécanisme le mieux documenté chez **InterFast** et **Obat**, absent ailleurs.

- **InterFast** : nouvel objet lié au devis principal ; conditions de paiement (acomptes, primes, remises, retenue de garantie) **non dupliquées mais héritées en temps réel** du principal ; lignes propres à chaque variante ; à l'acceptation d'une variante, elle « remplacera automatiquement la proposition initiale et deviendra le devis principal » ; l'ancien principal est **renommé, pas supprimé**, devient non modifiable mais reste consultable dans l'historique. Suppression possible tant que la variante reste dans un statut modifiable (Brouillon/Finalisé/Envoyé).
- **Obat** : duplication automatique intégrale du contenu (« pas de ressaisie »), nom avec suffixe -Vx, historique visible dans un encart dédié (date/heure de création, statut, montants) sur le devis parent. Chaînage possible (variante créée depuis une autre variante). À la signature d'une variante, elle devient la version retenue ; le parent et les autres variantes passent en **Annulé**, chacun conservant sa propre référence (système récent, sans renommage — un ancien mécanisme avec renommage/suffixe « V0 » existait et reste actif sur les séquences déjà signées avant le déploiement du nouveau système, signalé explicitement par la source comme déploiement progressif).
- Chez les 6 autres éditeurs : terme absent du corpus lu. NON DÉTERMINÉ.

### 8.3 Révision (historique de versions du même objet)

Concept distinct de la variante, documenté chez deux éditeurs seulement, avec un **sens différent chez chacun** — piège terminologique à ne jamais confondre :

- **Costructor** : marqueur de version **auto-généré à chaque modification** d'un même devis (v1, v2, v3…), numéro de devis inchangé. Historique conservé (10 dernières révisions, réservé aux abonnements Business+/Enterprise). Actions possibles sur une ancienne révision : consulter/imprimer/télécharger, ou **dupliquer** (crée alors un nouvel objet à numéro distinct). Aucune restauration *en place* n'est décrite malgré le titre de l'article source (« récupérer une version antérieure ») — NON DÉTERMINÉ si un rollback réel existe.
- **Vertuoza** : le seul usage du mot « révision » concerne une **formule d'indexation de prix** affichée en totaux « avant/après révision » dans le même devis — sans aucun rapport avec une nouvelle version du document. Signalé explicitement par l'agent d'extraction comme un risque de confusion à ne pas reproduire dans la synthèse.
- Chez les 6 autres éditeurs : terme absent. NON DÉTERMINÉ.

### 8.4 Avenant (modification postérieure à un engagement)

Le concept le plus systématiquement post-acceptation/signature du corpus.

| Éditeur | Déclencheur | Nature de l'objet | Lignes reprises | Numérotation | Lien au devis initial | Cycle de statuts propre ? | Source |
|---|---|---|---|---|---|---|---|
| Vertuoza | Chantier en cours (post-acceptation) | nouvel objet, module dédié « Gestion de chantier &gt; Finance &gt; Avenants » | reprise **sélective** (cases à cocher) des lignes du devis de base, combinable avec de nouvelles lignes | propre, mécanique non détaillée | additif : « ajoutant ou soustrayant son montant au devis de base », qui reste la référence | oui — ENVOYÉ → **ACCEPTE** (nommage différent du devis, qui passe par SIGNÉ) | `gestion-de-chantier/avenant.md`, `gestion-de-chantier/signature-electronique-de-l-avenant.md` |
| InterFast | Devis d'origine au statut **Accepté** | nouvel objet, « lié financièrement et commercialement au devis premier » | NON DÉTERMINÉ (silence) | NON DÉTERMINÉ | additif, agrégé seulement à la facturation du solde (avenants Acceptés déduits/ajoutés) | oui — cycle propre Brouillon→Envoyé→Accepté, doit être Accepté pour être pris en compte | `finances/creer-un-avenant-au-devis.md` |
| Costructor | aucune condition explicite documentée | **devis ordinaire** créé via le bouton standard « + Nouveau devis » — pas un type d'objet système dédié (INTERPRÉTATION) | saisie manuelle (« + Nouvelle ligne »), aucune reprise automatique documentée | NON DÉTERMINÉ | rattachement au chantier initial **explicitement optionnel** (« vous pouvez ») ; client NON DÉTERMINÉ (silence) | NON DÉTERMINÉ (pas de cycle distinct documenté) | `ventes/comment-creer-un-avenant-a-un-devis...md` |
| Les 5 autres éditeurs | terme absent du corpus lu (Sellsy, Axonaut, OpenFire×2, Obat) | — | — | — | — | — | — |

**Lecture structurante** : l'avenant, quand il existe, est presque toujours un **objet distinct, additif, jamais fusionné dans le devis d'origine**, mais son degré de formalisation varie fortement — d'un module dédié avec cycle de statuts propre (Vertuoza, InterFast) à un simple usage détourné du bouton de création standard (Costructor, où le mot « avenant » semble relever du vocabulaire utilisateur plutôt que d'un champ technique). Le lien au projet/chantier est systématiquement présenté comme optionnel quand il est documenté (InterFast implicite, Costructor explicite) — confirmation croisée d'un point déjà relevé par 3A pour la naissance du devis.

## 9. Annulation / suppression / archivage / restauration

- **Suppression** : documentée comme possible uniquement en statut non numéroté/Brouillon chez InterFast (« il sera donc impossible de le supprimer » après Finalisé) et implicitement chez Sellsy (facture : impossible hors Brouillon). Chez Obat, aucune source du corpus lu ne décrit la suppression d'un devis en Brouillon — silence, pas absence. Sellsy documente une suppression **totale et définitive** pour tout document de vente hors facture finalisée, sans mécanisme de corbeille/restauration identifié (NON DÉTERMINÉ).
- **Annulation** : InterFast présente explicitement l'annulation comme la **bonne pratique recommandée en remplacement de la suppression** pour un devis numéroté, par analogie avec l'obligation légale de continuité de séquence des factures — extension **non confirmée légalement pour le devis** ("il est recommandé d'appliquer le même principe aux devis", cité tel quel, sans sur-interprétation). Sellsy propose une annulation manuelle de statut pour tout document hors facture/avoir, qui exclut le document des statistiques sans le supprimer. Obat et OpenFire (Odoo) documentent un état « Annulé » **automatique et non manuel** dans deux contextes précis et non généralisables : la variante perdante lors de la signature d'une autre variante (Obat), et le devis rattaché à une opportunité marquée perdue (OpenFire Odoo).
- **Archivage** : documenté uniquement pour le **chantier** chez Vertuoza (`gestion-de-chantier/archiver-le-chantier.md`), pas pour le devis lui-même — retiré des modules actifs, consultable et réactivable. Aucun mécanisme d'archivage propre au devis n'est documenté ailleurs.
- **Restauration** : le seul mécanisme de restauration direct et nommé du corpus est l'« annulation de signature » d'Obat (retour au statut antérieur). Chez Vertuoza, la suppression du chantier vide « réouvre » le devis original (recovery indirect, pas une restauration d'archive). Ailleurs : NON DÉTERMINÉ.
- **Expiration** : formalisée comme état calculé chez Sellsy (bloque signature et paiement en ligne, recovery par ajustement de la date « à signer avant le ») et comme simple filtre de recherche chez InterFast (pas un des 7 statuts officiels, bloque seulement l'envoi par email si la date d'échéance est dépassée). Absente ou non trouvée dans les 6 autres corpus.

## 10. Conditions structurantes

Classées par type, uniquement quand documentées et distinctes d'un état/d'une permission/d'une dépendance :

- **Condition de donnée** : signature électronique bloquée sans prénom+nom+email+mobile valides du contact (InterFast, OpenFire Odoo) ; soumission bloquée si montant total = 0 ou champs obligatoires manquants (Vertuoza) ; caractères spéciaux non supportés bloquant la soumission (Vertuoza).
- **Condition de montant** : arbitrage manuel requis chez Sellsy si le montant facturé diffère du montant du devis parent (remise ajoutée par exemple).
- **Condition de rôle/permission** : transformation en facture et suppression de commande soumises à un droit spécifique chez Axonaut (« édition de facture », sinon contacter l'administrateur) ; envoi en signature, suppression, finalisation de brouillon et export PDF chacun soumis à un privilège distinct chez Sellsy.
- **Condition de configuration/abonnement** : signature électronique réservée à un palier d'abonnement chez Vertuoza (pack Pro+), InterFast (plafond de 30 signatures/mois/utilisateur payant, réservé au secteur BTP par code APE), Costructor (illimité en Business+/Premium, facturé à l'unité en Pro) ; récupération de révisions réservée à Business+/Enterprise chez Costructor ; relance automatique réservée à Business+ chez Costructor.
- **Condition temporelle** : date d'échéance dépassée bloquant l'envoi par email (InterFast) ; date « à signer avant le » dépassée bloquant signature et paiement en ligne (Sellsy) ; validité Universign de 14 jours à partir de l'envoi (Obat).
- **Condition de relation** : avenant nécessitant un devis source Accepté (InterFast) ou un chantier en cours (Vertuoza) ; facturation du solde nécessitant devis + avenant(s) tous Accepté (InterFast) ; suppression de commande impossible si documents associés (Axonaut) ; suppression du chantier impossible si documents générés dans le chantier (Vertuoza).
- **Condition métier (citée telle quelle, sans extrapolation)** : « la législation impose une séquence chronologique continue... il est recommandé d'appliquer le même principe aux devis » (InterFast) — recommandation explicitement non assortie d'une obligation légale directe sur le devis lui-même.
- **Condition externe** : choix du prestataire de signature électronique (Yousign chez Axonaut/Sellsy, Docusign en option chez Sellsy, Universign chez Obat) — changement de prestataire bloquant les demandes en cours chez l'ancien (Sellsy).
- **Condition de configuration produit (ligne)** : articles marqués « Non remisables » chez OpenFire (Odoo) — prix de vente non modifiable, verrou **au niveau ligne**, jamais généralisé au document entier ; prix de vente « déverrouillé »/« verrouillé » ligne par ligne chez Costructor pour les ajustements de marge en masse.

Rappel de discipline : ÉTAT ≠ CONDITION ≠ PERMISSION ≠ DÉPENDANCE — les tableaux ci-dessus séparent systématiquement ces catégories, aucune n'a été fusionnée dans la rédaction des rapports d'agents.

## 11. Multi-utilisateur documenté

Le corpus est globalement pauvre sur ce sujet pour le devis — NON DÉTERMINÉ chez OpenFire (Zendesk), OpenFire (Odoo, hors signataires externes), Obat et Vertuoza (hors traçabilité) et Costructor. Les seuls faits documentés :

| Éditeur | Fait documenté | Source |
|---|---|---|
| Axonaut | Droit « édition de facture » requis pour transformer un devis ; autorisation requise pour supprimer une commande ; notification de signature envoyée **uniquement** à l'utilisateur nommé en haut à gauche du devis | `gerez-vos-devis/comment-transformer-un-devis-en-facture.md`, `gerez-vos-devis/modifier-un-devis.md`, `gerez-vos-devis/signature-electronique-des-devis-documents-yousign.md` |
| Sellsy | Privilèges distincts par action (création de signature, suppression par type de document, validation de facture/avoir, accès aux fichiers), activation du module réservée à l'administrateur ; un « propriétaire »/« référent » peut être désigné à la création | `documents-de-vente/envoyer-un-document-pour-signature-electronique.md`, `documents-de-vente/supprimer-un-document-de-vente.md` |
| InterFast | Auteur du devis modifiable seulement en Brouillon/Envoyé ; historique trace l'utilisateur pour chaque action ; commentaires internes avec mention `@` | `finances/comprendre-la-fiche-d-un-devis.md` |
| Vertuoza | Historique trace l'utilisateur par action, sans règle de permission documentée ; champ « responsable » sur l'avenant, rôle fonctionnel NON DÉTERMINÉ | `documents/historique.md`, `gestion-de-chantier/avenant.md` |
| OpenFire (Odoo) | Signature multi-signataires séquentielle (mobile+prénom obligatoires pour chacun, validation par le dernier signataire) — mécanisme multi-**acteur externe**, pas multi-utilisateur interne | `mise-en-place-de-la-signature-electronique-261.md` |

Aucun éditeur ne documente de validation hiérarchique (workflow d'approbation à plusieurs niveaux) ni de transfert/réassignation de devis entre utilisateurs. Silence quasi total à traiter comme NON DÉTERMINÉ, pas comme absence de la fonctionnalité chez ces éditeurs.

## 12. UX fonctionnelle documentée

Motif transversal, cohérent avec le constat déjà fait par 3A pour la naissance du devis : les points d'entrée et boutons d'action sont **bien documentés** pour la quasi-totalité des éditeurs (fiche devis, liste, menu d'action, portail client), mais la **mécanique d'interface exacte** (modal vs page dédiée, comportement bloquant) reste largement UX_PARTIELLEMENT_RECONSTRUCTIBLE.

| Éditeur | Classification dominante | Point notable |
|---|---|---|
| Vertuoza | UX_DOCUMENTEE pour l'essentiel (liste, envoi, portail client signature, avenant) | icône crayon comme indicateur visuel d'éditabilité, mentionnée une seule fois |
| InterFast | UX_DOCUMENTEE (fiche, tableau, éditeur V1/V2, portail signature) | UX_INCONNUE pour la gestion du devis sur mobile (seule la restitution de rapports d'intervention y est documentée) |
| Axonaut | UX_DOCUMENTEE (liste, fiche client, portail client, commandes) | UX_INCONNUE pour l'application mobile |
| Sellsy | UX_DOCUMENTEE (fiche, listing, réglages, app mobile pour création/modification/envoi) | UX_PARTIELLEMENT_RECONSTRUCTIBLE pour l'interface client du lien public ; UX_INCONNUE pour signature/suppression/conversion sur mobile |
| OpenFire (Zendesk) | UX_DOCUMENTEE pour impression/envoi/aperçu client/confirmation de vente | UX_INCONNUE pour tout point d'entrée de duplication/variante |
| OpenFire (Odoo) | UX_DOCUMENTEE pour création, modèle, impression, envoi, signature | UX_INCONNUE pour le comportement visuel du devis une fois Annulé ou Signé |
| Obat | UX_DOCUMENTEE pour finalisation, facturation, variantes, signature électronique, numérotation | Vue Kanban explicitement « Bientôt disponible » à la date de collecte — à ne pas traiter comme UX confirmée en production |
| Costructor | UX_DOCUMENTEE pour la quasi-totalité des parcours (avenant, révisions, signature, marge, options, conversion, relance) | UX_INCONNUE pour l'état du devis d'origine après conversion en bon de commande, et pour tout verrou global d'édition |

## 13. Comparaison inter-éditeurs

Cette section synthétise, phénomène par phénomène, les constats déjà détaillés en §6-9.

**Phénomène 1 — Séparation signature / acceptation.** Deux familles nettes de marché (détail §7) : signer ≠ accepter chez Vertuoza et OpenFire (Zendesk) ; signer = accepter automatiquement chez Obat, Costructor, Sellsy (à la signature complète) et InterFast.

**Phénomène 2 — Localisation du verrou de mutabilité.** Cinq modèles distincts (détail §6.2), du verrou direct avec recovery nommé (Obat) au verrou indirect porté par un objet lié (Axonaut) en passant par l'absence totale de verrou documenté (OpenFire Odoo).

**Phénomène 3 — Cause du verrou, jamais légale pour le devis.** Contraste fort avec la facture (pilote propagation, INV-1 : cause réglementaire quasi unanime, 6 éditeurs sur 7). Aucun des 8 corpus lus ici n'attribue de cause légale au verrou du devis lui-même ; seul InterFast évoque une recommandation par analogie, explicitement non confirmée comme obligation.

**Phénomène 4 — Multiplicité des mécanismes de dérivation.** Duplication, variante, révision et avenant coexistent rarement chez un même éditeur (aucun n'en documente quatre) ; InterFast est le seul à distinguer clairement trois de ces quatre mécanismes (duplication, variante, avenant) avec des règles différentes pour chacun. Le mot « révision » désigne deux choses différentes selon l'éditeur (Costructor : historique de versions ; Vertuoza : formule de prix) — variance strictement terminologique, pas fonctionnelle.

**Phénomène 5 — Avenant toujours additif, jamais fusionné.** Convergence chez les 3 éditeurs qui le documentent (Vertuoza, InterFast, Costructor) : l'avenant ne remplace jamais le devis d'origine, il s'y ajoute (financièrement ou en tant qu'objet lié consultable séparément).

**Phénomène 6 — Numérotation ≠ verrou de contenu.** Chez InterFast et Obat, l'attribution du numéro définitif verrouille la suppression mais pas nécessairement l'édition du contenu — ces deux effets sont documentés séparément et ne doivent pas être fusionnés.

**Phénomène 7 — Multi-utilisateur, angle mort quasi général.** Sur les 8 corpus, seuls Axonaut, Sellsy et InterFast documentent des règles de permission ou de traçabilité par utilisateur pour le devis ; aucun ne documente de validation hiérarchique.

## 14. Contrat fonctionnel observé du cycle du devis

Synthèse compacte, directement réutilisable pour construire plus tard le contrat fonctionnel SUPORDO — ne prend aucune décision produit.

**Comment le devis évolue.** Depuis sa création (3A), le devis suit une trajectoire faite de trois familles d'événements documentées de façon quasi universelle mais jamais identiquement nommées : (1) des événements de **préparation** sans effet d'état fort (enregistrer, imprimer/PDF — convergence forte, aucun effet documenté nulle part) ; (2) un événement de **communication** (envoyer) qui, chez la majorité des éditeurs qui le documentent explicitement, ne verrouille rien par lui-même ; (3) un événement d'**engagement** (signature et/ou acceptation) qui déclenche presque toujours un objet lié ou un changement d'état commercial fort, mais dont la mécanique exacte diverge structurellement (§7, §13).

**Quels événements ont un effet d'état.** Avec un niveau de preuve élevé : la signature électronique complète (5/8 éditeurs qui la documentent en détail) et l'acceptation/validation manuelle (Vertuoza, Axonaut, InterFast) ont systématiquement un effet d'état ou déclenchent un objet lié. Avec un niveau de preuve plus faible : l'envoi seul a un effet d'état documenté explicitement chez Vertuoza et Sellsy (passage à « Envoyé »), mais ce passage n'entame l'éditabilité chez aucun des éditeurs qui le documentent.

**Quand il reste modifiable.** Chez tous les éditeurs qui documentent ce point (6/8), le devis reste modifiable au moins jusqu'à l'envoi, et souvent au-delà (jusqu'à l'acceptation ou la signature complète). Aucun éditeur ne verrouille le contenu à l'enregistrement ou à la simple numérotation seule (le verrou de numérotation porte sur la suppression, pas l'édition, quand il existe).

**Quand il devient engagé/verrouillé.** Cinq modèles distincts coexistent (§6.2) — verrou direct avec recovery nommé, verrou direct avec recovery indirect via un objet lié, verrou porté par un objet créé à l'acceptation (jamais le devis lui-même), verrou dur sans recovery, absence de verrou technique remplacée par une invalidation logique. Aucune cause légale n'est jamais invoquée pour ce verrou (contraste fort avec la facture).

**Comment une modification ultérieure est gérée.** Trois voies distinctes et non exclusives selon l'éditeur : réouverture directe du même objet (Vertuoza via suppression du chantier, InterFast via retour à Envoyé, Obat via annulation de signature) ; objet additif séparé qui ne remplace jamais le devis d'origine (avenant, 3 éditeurs) ; ré-engagement complet nécessaire (Costructor — modifier invalide la signature, il faut re-signer).

**Comment il peut être envoyé/partagé.** Email systématiquement documenté (8/8, hérité de 3A) ; partage via lien public/portail client documenté explicitement chez Sellsy et Axonaut ; suivi de statut d'envoi (délivré/ouvert/cliqué) documenté chez Costructor et Vertuoza (au niveau email, pas au niveau devis).

**Comment acceptation et signature s'articulent.** Point le plus structurant de toute la mission pour une décision SUPORDO à venir (§7, phénomène 1) : deux familles de marché, pas une convention unique.

**Comment duplication/variante/révision/avenant diffèrent.** Quatre mécanismes fonctionnellement distincts quand ils existent : la duplication rompt ou ne précise pas le lien avec l'original ; la variante coexiste et concurrence l'original jusqu'à ce que l'une gagne (l'original devient alors non modifiable mais reste consultable, jamais supprimé) ; la révision est un historique interne du même objet (sens non stable d'un éditeur à l'autre — piège terminologique) ; l'avenant est toujours additif et post-engagement, jamais un remplacement.

**Quelles divergences sont réellement structurantes** (à ne pas lisser dans une future spécification SUPORDO) : l'articulation signature/acceptation (§7), la localisation du verrou de mutabilité (§6.2), et l'existence ou non d'un mécanisme de variante concurrente distinct de la duplication (seuls InterFast et Obat le documentent, avec des règles de bascule différentes).

## 15. Standards forts / probables

- **STANDARD_FORT** : génération de PDF/impression sans effet sur l'état du devis (documenté explicitement et sans contre-exemple chez 5 éditeurs sur 8 qui traitent le sujet — Vertuoza, OpenFire Zendesk, OpenFire Odoo, Sellsy, Costructor) ; l'avenant, quand il existe, est toujours additif et jamais fusionné/remplaçant (3/3 éditeurs qui le documentent, sans contre-exemple).
- **STANDARD_PROBABLE** : le devis reste modifiable au moins jusqu'à l'envoi (documenté explicitement chez 3 éditeurs — Vertuoza, Axonaut, Sellsy — jamais contredit ailleurs, mais 5 corpus restent silencieux sur ce point précis) ; un événement d'engagement (signature complète et/ou acceptation manuelle) déclenche un changement d'état fort ou un objet lié (6/8 éditeurs, silencieux chez OpenFire Odoo et partiellement chez OpenFire Zendesk) ; la suppression devient impossible après numérotation/finalisation (InterFast, Obat implicitement par contraste avec la facture, Sellsy pour la facture — cohérent mais faiblement corroboré côté devis lui-même).

## 16. Variantes de marché

- **Articulation signature/acceptation** : deux modèles francs et irréductibles (§7, phénomène 1) — pas un spectre, une bascule binaire par éditeur.
- **Localisation du verrou de mutabilité** : cinq modèles distincts (§6.2), aucun ne domine numériquement (2 éditeurs max par modèle).
- **Existence d'un mécanisme de variante concurrente** : InterFast et Obat le documentent richement et de façon convergente sur le principe (bascule automatique du « principal », original non supprimé) ; les 6 autres éditeurs n'en documentent aucune trace — silence cohérent chez 6/8, à traiter comme variante de marché potentielle plutôt que fait établi (silence documentaire ≠ absence fonctionnelle, mais la cohérence du silence chez la majorité mérite d'être notée).
- **Formalisation de l'avenant** : d'un module dédié avec cycle de statuts propre (Vertuoza, InterFast) à un simple devis ordinaire réutilisé par convention (Costructor) — même mot, degrés de systématisation très différents.
- **Sens du mot « révision »** : deux significations incompatibles chez les deux seuls éditeurs qui l'emploient (Costructor : version automatique ; Vertuoza : formule de prix) — variance purement terminologique, à ne jamais traiter comme fonctionnelle.
- **Cause des verrous** : quand un verrou existe, sa cause reste toujours métier ou technique dans ce corpus (jamais légale pour le devis), contrairement au motif documenté pour la facture par le pilote propagation.

## 17. Non déterminé

- Mode exact (verrou direct vs invalidation logique) chez 4 des 8 éditeurs pour lesquels le comportement précis après signature/acceptation reste imprécis ou absent (OpenFire Zendesk au-delà du mobile, OpenFire Odoo entièrement, Vertuoza pour le statut intermédiaire SIGNÉ, InterFast pour la tension client/statut Envoyé).
- Comportement exact d'une tentative de suppression/modification d'un devis en statut Refusé, sur la quasi-totalité des corpus (seul Obat suggère un statut Kanban terminal, non confirmé en production).
- Existence d'un minimum de contenu requis pour finaliser/soumettre un devis — silence quasi total, à l'exception du blocage à 0 € chez Vertuoza.
- Comportement précis de la duplication (contenu repris, numéro, lien) chez 4 des 6 éditeurs qui documentent son existence par un simple bouton (Vertuoza, Obat, et partiellement Sellsy/Costructor).
- Fréquence réelle d'usage de chaque mécanisme (variante, avenant, révision, duplication) dans la pratique — la mission documente l'existence de la capacité, jamais son taux d'adoption.
- Rôles/permissions/validation hiérarchique pour la quasi-totalité des actions chez 5 des 8 éditeurs (Vertuoza hors traçabilité, OpenFire×2, Obat, Costructor).
- Comportement du devis sur application mobile pour la gestion du cycle de vie (statuts, envoi, signature) chez la majorité des éditeurs — seule la création/modification simple est documentée par endroits (Sellsy, InterFast pour les rapports d'intervention seulement).

## 18. Questions SUPORDO désormais instruisibles

**Faut-il séparer finalisation/numérotation et envoi ?**
- FAITS DISPONIBLES : chez les éditeurs qui documentent la numérotation (InterFast, Obat, Costructor implicitement), elle est explicitement distincte de l'envoi et porte uniquement sur le verrou de suppression, pas sur l'éditabilité du contenu.
- VARIANTES OBSERVÉES : numérotation avant envoi possible (InterFast : Finalisé puis Envoyé, deux étapes) ; numérotation liée au choix de canal (Obat : « Finaliser et envoyer » propose 4 choix, articulation exacte imprécise).
- TERRAIN NÉCESSAIRE : non — le corpus suffit à motiver la séparation de principe.

**Faut-il séparer signature et acceptation, ou les fusionner ?**
- FAITS DISPONIBLES : deux familles de marché nettes et à peu près à parité (§7) — Vertuoza et OpenFire Zendesk séparent ; Obat, Costructor, Sellsy (signature complète) et InterFast fusionnent.
- VARIANTES OBSERVÉES : chez Vertuoza, la séparation sert à distinguer la preuve de consentement client (SIGNÉ) de l'engagement commercial interne (Chantier en cours, après action « Accepter » distincte) — utile si SUPORDO veut un point de contrôle humain avant engagement définitif.
- INFORMATION MANQUANTE : aucun corpus ne documente pourquoi un éditeur a choisi l'un ou l'autre modèle (contrainte technique, choix produit délibéré, historique).
- TERRAIN NÉCESSAIRE : non pour la décision de principe (les deux modèles sont également bien attestés) ; oui pour arbitrer lequel convient mieux à l'usage réel des artisans SUPORDO.

**Quand faut-il verrouiller le contenu du devis ?**
- FAITS DISPONIBLES : cinq modèles observés (§6.2), aucune cause légale documentée nulle part pour le devis lui-même.
- VARIANTES OBSERVÉES : verrou direct et dur (Obat, Sellsy, InterFast, Vertuoza) vs verrou indirect porté par un objet lié (Axonaut) vs absence de verrou technique (Costructor, OpenFire Odoo).
- INFORMATION MANQUANTE : aucune donnée sur la fréquence des demandes de modification post-engagement en pratique réelle.
- TERRAIN NÉCESSAIRE : non pour la décision de principe (verrouiller ou non est arbitrable sur la seule base du corpus) ; oui pour calibrer le mécanisme de recovery le plus adapté (retour de statut à la Obat/InterFast, ou re-validation à la Costructor).

**Faut-il un mécanisme de recovery explicite après verrouillage ?**
- FAITS DISPONIBLES : 3 éditeurs sur les 5 qui verrouillent documentent un recovery nommé (Obat : annulation de signature ; InterFast : retour à Envoyé ; Vertuoza : suppression du chantier vide) ; Sellsy ne documente aucun recovery pour son verrou (présenté comme définitif).
- TERRAIN NÉCESSAIRE : non — la majorité documentée (3/5) suffit à motiver l'inclusion d'un recovery de principe.

**Faut-il duplication, variante, révision et/ou avenant — et lesquels combiner ?**
- FAITS DISPONIBLES : quatre mécanismes fonctionnellement distincts et non redondants quand ils coexistent (InterFast en documente trois, avec des règles différentes pour chacun) ; aucun éditeur n'a les quatre.
- VARIANTES OBSERVÉES : la variante (concurrence commerciale, une seule gagne) répond à un besoin différent de l'avenant (évolution après engagement) et de la révision (historique de versions) — ce ne sont pas des synonymes interchangeables.
- TERRAIN NÉCESSAIRE : non pour la distinction conceptuelle elle-même (le corpus la démontre clairement) ; oui pour savoir lesquels de ces quatre besoins sont réellement rencontrés par les artisans cibles de SUPORDO.

**Quelle trace conserver après engagement ?**
- FAITS DISPONIBLES : historique par utilisateur/action documenté chez Vertuoza et InterFast ; encart dédié aux variantes chez Obat (date, statut, montants) ; onglet « Historique du document » chez Sellsy pour les conversions (mais explicitement rompu pour les duplications).
- TERRAIN NÉCESSAIRE : non — le corpus fournit assez de patterns pour instruire une décision de traçabilité minimale.

## 19. Questions qui restent terrain / produit

- Le choix entre séparer ou fusionner signature/acceptation change-t-il la perception de fiabilité ou de rapidité perçue par un artisan solo vs une équipe avec un rôle « commercial » distinct du rôle « exécutant » ?
- La fonctionnalité de variante concurrente (InterFast, Obat) répond-elle à un besoin réel et fréquent chez les artisans BTP visés par SUPORDO, ou est-ce une fonctionnalité de niche peu utilisée en pratique malgré sa richesse documentaire ?
- Le recovery par « annulation de signature » (Obat) est-il perçu comme rassurant ou au contraire comme fragilisant la valeur probante de la signature côté client ?
- La friction du modèle Costructor (modifier un devis signé invalide la signature, oblige une re-signature) est-elle vécue comme protectrice ou comme un frein commercial dans l'usage réel ?
- Quelle est la fréquence réelle d'usage de chaque mécanisme de dérivation (duplication, variante, avenant, révision) chez les artisans, au-delà de leur existence documentaire ?
- Le lien optionnel avenant↔chantier (documenté chez InterFast et Costructor) est-il utilisé en pratique surtout avec ou surtout sans ce rattachement ?

## 20. Limites de l'analyse

- Le corpus OpenFire (Zendesk) et OpenFire (Odoo) reste pauvre à moyen sur cette question précise (2 stubs sans apport chez Zendesk, dont un contenu manifestement mal indexé ; aucun verrou de mutabilité documenté du tout chez Odoo) — un futur travail plus large sur OpenFire pourrait devoir élargir la liste fermée de fichiers au-delà de celle utilisée ici.
- La fonctionnalité « vue Kanban » d'Obat est explicitement marquée « Bientôt disponible » dans son propre titre source — traitée ici comme signal sur l'intention de modèle de statuts, pas comme comportement confirmé en production.
- Deux tensions documentaires internes non résolues ont été conservées telles quelles plutôt qu'arbitrées (Axonaut sur la définition de « devis en attente », InterFast sur la mutabilité du champ client au statut Envoyé) — une vérification directe sur les logiciels concurrents permettrait de trancher, non tentée ici (hors périmètre d'une mission documentaire).
- Les listes fermées de fichiers ont été constituées par recherche de motifs sur les noms de fichiers, pas par un grep mécanique du champ `moment_parcours` des fichiers LIGHT (même écart méthodologique assumé qu'en 3A, pour les mêmes raisons d'économie face à des fichiers LIGHT de plusieurs milliers de lignes) — un candidat supplémentaire pourrait exister hors de ces listes, notamment pour Axonaut et OpenFire où le rendement de cette mission est resté plus faible.
- Aucune vérification n'a été faite sur des éditeurs hors des 8 corpus déjà retenus par 3A (Batikko, Extrabat, Tolteck, Leobati) — cohérent avec la décision de suffisance déjà actée en 3A, non rouverte ici.
- La matrice ACTION×ÉTAT×CONDITION×EFFET présentée en §5 est une sélection des couples les plus structurants ; le détail exhaustif reste dans les 8 rapports d'agents sous-jacents, non reproduits intégralement dans ce livrable pour éviter une duplication disproportionnée par rapport à la question posée (principe de suffisance décisionnelle).

## 21. Verdict

**L'analyse permet-elle maintenant de répondre de façon suffisamment fiable à : « Que peut-il arriver à un devis après sa création, depuis quels états/contextes, sous quelles conditions, et avec quels effets ? »**

**EXPLOITABLE.**

Justification stricte au regard du critère qualitatif de la mission : 8 corpus indépendants (les mêmes 4 familles de marché que 3A, avec la même corroboration systématique) permettent de reconstruire concrètement le contrat fonctionnel du cycle de vie post-création — trois familles d'événements (préparation, communication, engagement), cinq modèles distincts de verrouillage de mutabilité, une divergence de marché structurante et bien attestée sur l'articulation signature/acceptation, et quatre mécanismes de dérivation fonctionnellement distingués (duplication, variante, révision, avenant) avec suffisamment de matière convergente pour instruire directement les six questions SUPORDO listées en §18 sans enquête terrain supplémentaire pour leur décision de principe.

Les inconnues restantes (§17) sont nommées et non dissimulées : le comportement précis après signature/acceptation reste flou ou absent chez la moitié des éditeurs (les deux corpus OpenFire, plus des zones d'ombre chez Vertuoza et InterFast), le mécanisme exact de duplication reste largement NON DÉTERMINÉ, et aucune donnée de fréquence d'usage réelle n'est disponible pour aucun mécanisme. Ces trous n'empêchent pas une décision SUPORDO de principe — ils appellent une corroboration terrain ciblée uniquement pour le calibrage fin (§19), pas pour la structure d'ensemble du cycle de vie.

DEVIS_3B_TERMINE — EXPLOITABLE — STOP
