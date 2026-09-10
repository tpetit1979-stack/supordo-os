# SUPORDO — Contrat fonctionnel du devis — V0

Document pont entre l'analyse concurrentielle ciblée du devis (`functional-devis-3a-naissance.md`, `functional-devis-3b-cycle.md`, `functional-devis-3c-sorties.md`, toutes trois EXPLOITABLE — STOP) et une décision produit SUPORDO. Aucune nouvelle recherche concurrentielle n'a été menée pour produire ce document ; aucun schéma SQL, API ou composant n'y figure.

**Révision (statuts).** Ce document applique désormais exactement six statuts, sans en inventer d'autre :

| Situation | Statut appliqué |
|---|---|
| plusieurs sources indépendantes établissent le comportement | **ACQUIS DOCUMENTAIRE** |
| comportement observé chez un ou quelques éditeurs seulement | **VARIANTE DE MARCHÉ** |
| choix intéressant pour SUPORDO mais non démontré par le corpus | **RECOMMANDATION SUPORDO** |
| choix structurant explicitement réservé au Product Owner, options présentées sans réponse imposée | **DÉCISION SUPORDO À ARBITRER** |
| nécessite validation avec des artisans réels | **À TESTER TERRAIN** |
| corpus insuffisant pour conclure, dans un sens ou dans l'autre | **NON DÉTERMINÉ** |

Un standard concurrent n'est jamais recopié automatiquement en décision SUPORDO, et une absence documentaire n'est jamais transformée en conclusion produit (silence documentaire ≠ absence fonctionnelle — principe du dépôt, rappelé à chaque fois qu'il s'applique).

Sources : `functional-devis-3a-naissance.md` (naissance), `functional-devis-3b-cycle.md` (cycle de vie), `functional-devis-3c-sorties.md` (sorties/propagation). Renvois `§` dans ce document = sections des trois sources, précédées de 3A/3B/3C.

---

## 1. Rôle métier du devis

**ACQUIS DOCUMENTAIRE.** Sur les 8 corpus (Vertuoza, InterFast, Axonaut, Sellsy, OpenFire Zendesk, OpenFire Odoo, Obat, Costructor), le devis remplit trois fonctions convergentes, jamais contestées :

1. **Outil de chiffrage** : un document qui associe un client (créable à la volée, 8/8, 3A §7) à des lignes de prestations/produits (catalogue quasi universel, 8/8, 3A §9), avec un état non engageant par défaut (3B §3).
2. **Support d'engagement commercial** : un objet dont un événement (signature, acceptation, validation — jamais uniformément nommé) déclenche un changement d'état fort et/ou la création d'un objet aval (3B §7, 3C §4).
3. **Source unique de propagation** : les données du devis (client, lignes, montants, taxes, conditions) sont reprises — copiées, recalculées ou référencées selon les cas — par tous les objets qu'il engendre (3C §11, INV-3C-2).

Ce que le devis n'est **jamais**, dans aucun des 8 corpus : un document à portée légale intrinsèque (3B §6.2, 3C INV-3C-4 — aucune cause légale n'est jamais invoquée pour son propre verrouillage, contrairement à la facture).

**RECOMMANDATION SUPORDO** : retenir le devis comme **document de proposition commerciale chiffrée, non engageant par défaut, qui devient la source de vérité traçable de tout ce qu'il engendre après son événement d'engagement**. Pourquoi : c'est la lecture qui recoupe les trois fonctions démontrées sans en privilégier arbitrairement une, et elle reste compatible avec les cinq modèles de verrouillage observés (3B §6.2) sans en imposer un a priori — mais c'est une formulation de travail, pas une conclusion que le corpus imposerait.

## 2. Périmètre fonctionnel

**ACQUIS DOCUMENTAIRE.** Le périmètre effectivement documenté par le marché couvre : naissance (contextes, dépendances, lignes) → cycle (édition, communication, engagement, dérivation) → sorties (facturation, commande, chantier, intervention) → recovery. Un quatrième périmètre, demandé en complément par la commande de mission (visite → relevé → étude → devis), n'est couvert que par deux cas nets sur 8 (3C §10bis) — traité séparément en §13 pour ne pas gonfler artificiellement le niveau de preuve du cœur du sujet.

**RECOMMANDATION SUPORDO** : le périmètre fonctionnel V0 du devis SUPORDO couvre naissance + cycle + sorties immédiates (facture, acompte/situation/solde, chantier). Le périmètre visite/relevé/étude est traité comme une extension distincte et moins mûre (§13), pas comme un prérequis du cœur — ce découpage reste une proposition d'éditeur du document, révisable par le Product Owner.

## 3. Relations avec les autres objets métier

**ACQUIS DOCUMENTAIRE** — synthèse des relations amont et aval démontrées (3A §7, 3C §3-§9) :

| Objet | Sens de la relation | Statut de preuve |
|---|---|---|
| Client / contact | Amont (créable inline, 8/8) | STANDARD_FORT |
| Catalogue / produit / ouvrage | Amont ET aval (créable inline, alimente les lignes) | STANDARD_FORT |
| Opportunité CRM | Amont, point d'entrée distinct optionnel | SPÉCIFICITÉ_ÉDITEUR (2/8) |
| Chantier / projet / affaire | Aval dominant (créé depuis le devis accepté) chez 3 éditeurs BTP ; amont chez aucun ; absent chez 2 ; réattribué à l'opportunité chez 1 | VARIANTE_DE_MARCHE |
| Intervention / visite | Amont ET aval selon l'éditeur — sens inversé chez OpenFire×2 (intervention/étude → devis dominant) | VARIANTE_DE_MARCHE structurante (3C §9, §17 phénomène 4) |
| Facture (ordinaire, acompte, situation, solde) | Aval, universel comme capacité (8/8) | STANDARD_FORT sur l'existence, VARIANTE_DE_MARCHE sur le mécanisme |
| Commande client | Aval, non universel (3 modèles distincts, absent chez 2 éditeurs) | VARIANTE_DE_MARCHE |
| Commande / demande de prix fournisseur | Aval, présent chez 7/8 | STANDARD_PROBABLE (mécanismes hétérogènes) |
| Devis existant (duplication/variante/révision) | Auto-référence | STANDARD_PROBABLE (6/8 pour la duplication) |
| Avenant | Aval, toujours post-engagement | Acquis 3B, réutilisé pour son effet aval en 3C |

**RECOMMANDATION SUPORDO** (conceptuelle, sans préjuger d'un schéma) : distinguer le devis de chacun des objets ci-dessus par une relation nommée et de nature propre — pas un lien générique unique « document associé » — vers : client (cf. §4), catalogue (par ligne), chantier (cf. §3, §11), intervention/visite (les deux sens doivent rester possibles — cf. §13), facture(s), commande fournisseur. Pourquoi : c'est la seule lecture compatible avec la variance documentée (§3) sans forcer un ordre ou un mécanisme unique ; elle ne préjuge d'aucune structure de données, laissée à une étape ultérieure hors du périmètre de ce document.

## 4. Modes de naissance

**ACQUIS DOCUMENTAIRE** (3A §6, §10, §13) — points d'entrée démontrés, avec niveau de convergence :

- Création autonome (liste devis, bouton global) — 8/8.
- Depuis une fiche client — 5/8 (bouton dédié documenté, contenu du formulaire résultant rarement redétaillé).
- Depuis une fiche chantier — 3/8 (InterFast, Costructor, OpenFire Zendesk via contrat d'entretien).
- Depuis une opportunité CRM — 2/8 (Vertuoza, OpenFire Odoo).
- Depuis une fiche intervention/visite — 2/8+ (InterFast « Créer un devis », OpenFire Zendesk Vital Études génère automatiquement).
- Par duplication ou variante d'un devis existant — 6/8.
- Depuis un modèle — 4/8 avec lignes préremplies (Sellsy exclut explicitement les lignes d'un modèle).
- Par import fichier (Excel, PDF, DPGF/DQE) — 3/8.
- Par génération assistée (IA, dictée) — 2/8 (Costructor, InterFast import).

**DÉPENDANCE CLIENT — arbitrage disponible.** 8/8 documentent la création de client à la volée pendant la création du devis (STANDARD_FORT) ; mais seuls 3/8 affirment un caractère strictement requis, et à des stades différents (mobile pour InterFast, « premier temps » pour OpenFire Odoo, finalisation pour Obat). Aucun corpus ne documente le comportement exact d'un devis sans client à l'enregistrement (3A §15).

**RECOMMANDATION SUPORDO** : client requis **à la finalisation** (attribution du numéro), pas à l'enregistrement en brouillon. Pourquoi : parmi les 3 modèles qui tranchent explicitement, c'est celui le mieux attesté isolément (Obat), il concilie liberté de brouillon (cohérent avec « enregistrer sans effet d'état fort », 3B §14) et intégrité du document numéroté transmis au client — mais les deux autres modèles documentés (requis dès le formulaire mobile, requis « en premier temps ») restent des options tout aussi légitimes, cf. table §18. Points d'entrée à retenir en V0 : création autonome, depuis fiche client, depuis fiche chantier, duplication. Point d'entrée depuis intervention/visite traité en §13. Import fichier et génération IA hors V0 (fonctionnalités d'accélération, pas fondation).

**À TESTER TERRAIN** : fréquence réelle de la création « from scratch » vs par duplication chez les artisans cibles (3A §16).

## 5. Données et contenu

**ACQUIS DOCUMENTAIRE** (3A §8, 3C §11) — données héritées documentées à la création : adresse(s) de facturation/livraison (5/8), conditions de paiement par défaut (4/8), position fiscale/TVA (2/8, spécifique OpenFire), prix/description d'un élément catalogue (5/8), contenu d'un modèle hors lignes (Sellsy) ou avec lignes (4/8), données d'une opportunité liée (2/8). Le **mode technique** (copié/référencé/généré) n'est tranché explicitement que pour de rares exceptions : prix catalogue SNAPSHOTTÉ (Obat, confirmé aussi en 3C §11), numérotation GÉNÉRÉE (Costructor), description produit GÉNÉRÉE (OpenFire Zendesk). Partout ailleurs, silence documentaire sur le mécanisme backend — constat déjà fait par le pilote propagation et reconfirmé trois fois (3A §8, 3B, 3C §22).

Ce silence est confirmé indépendamment une quatrième fois par le pilote propagation (« Le mode technique exact (copie en base vs référence vivante) de la quasi-totalité des propagations — le corpus documentaire ne descend jamais à ce niveau de précision, quel que soit l'éditeur »).

**DÉCISION SUPORDO À ARBITRER** : quel mode technique adopter — snapshot (figement à l'ajout/l'engagement) ou référence vivante (valeur recalculée si la source change) — pour chaque type de donnée propagée (prix de ligne, coordonnées de facturation, conditions particulières, libellés) ? Le corpus ne permet pas de recommander un choix unique avec un niveau de preuve suffisant : seules deux sources primaires tranchent explicitement, et de façon non uniforme (Obat : snapshot du prix catalogue ; Vertuoza : snapshot des coordonnées de facturation mais référence vivante et propagée rétroactivement pour le nom du chantier, sans que la documentation explique cette différence). Éléments à verser au débat du Product Owner, sans trancher à sa place : l'anomalie observée chez Vertuoza (la retenue de garantie ajoutée via le bouton natif du devis n'est *pas* propagée au chantier, 3C §6) illustre le risque si le mode n'est pas choisi explicitement et de façon cohérente pour chaque type de donnée — c'est un argument en faveur d'un choix assumé, pas en faveur d'un mode particulier.

**NON DÉTERMINÉ** : le comportement exact d'un devis sans contenu (0 ligne, montant nul) à la finalisation — silence total sur les 8 corpus (3A §19, 3B §17).

## 6. États et transitions candidats

**ACQUIS DOCUMENTAIRE** (3B §3, §11, §14). Aucun vocabulaire d'état n'est partagé à l'identique par deux éditeurs. Seul InterFast documente une liste complète et stable de 7 statuts (Brouillon / Finalisé / Envoyé / Accepté / Facturé / Refusé / Annulé), confirmée par deux sources indépendantes. Trois familles d'événements se dégagent, quasi universelles dans leur nature mais jamais nommées identiquement :

1. **Préparation** (enregistrer, générer un PDF) — aucun effet d'état documenté nulle part (convergence forte, 5/8 explicitement).
2. **Communication** (envoyer) — ne verrouille rien par lui-même chez la majorité qui documente ce point (Vertuoza, Axonaut, Sellsy).
3. **Engagement** (signature et/ou acceptation) — déclenche presque toujours un objet lié ou un changement d'état fort, mais l'articulation exacte diverge structurellement (§8).

**RECOMMANDATION SUPORDO** : adopter une machine d'états inspirée du modèle le plus robuste et le plus complet du marché (InterFast), adaptée aux principes retenus ailleurs dans ce document :

`BROUILLON → FINALISÉ (numéroté) → ENVOYÉ → ACCEPTÉ/SIGNÉ (engagé) → [FACTURÉ | lié à un CHANTIER]`, avec `REFUSÉ` et `ANNULÉ` comme états terminaux non destructifs atteignables depuis plusieurs points.

Pourquoi : reprend le seul modèle du marché confirmé par deux sources indépendantes plutôt que d'en inventer un ; respecte l'acquis « numérotation ≠ verrou de contenu » (§8) et « préparation sans effet d'état » (ci-dessus).

**NON DÉTERMINÉ** : réversibilité de l'état `REFUSÉ` (peut-il redevenir `ENVOYÉ` ou `BROUILLON` ?) — silence sur la quasi-totalité des corpus, seul Obat suggère un état Kanban terminal non confirmé en production (3B §17). Le corpus ne permet ni d'affirmer ni d'exclure une réversibilité ; la question reste ouverte plutôt que fixée par défaut.

## 7. Actions

**ACQUIS DOCUMENTAIRE** (3B §4) — catégories d'actions documentées, au-delà de la simple édition de contenu (déjà couverte en §4/§5 pour la naissance) :

- **Édition** : modifier lignes/prix/remise/TVA/client, réordonner/supprimer une ligne, ajuster marge en masse.
- **Réutilisation/évolution** : dupliquer, créer une variante, créer une révision, créer un avenant.
- **Document** : générer/imprimer le PDF, exporter, aperçu client, personnaliser le canal d'envoi.
- **Communication** : envoyer par email, déclarer envoyé manuellement, relancer, partager via lien public, suivre le statut d'envoi.
- **Engagement** : soumettre, finaliser/numéroter, accepter, refuser, signer électroniquement, confirmer la vente, annuler une signature.
- **Fin/administration** : annuler, supprimer (statut non numéroté seulement, quand documenté), archiver (jamais le devis lui-même sauf Sellsy — c'est le chantier qui s'archive), restaurer (portée limitée).

**RECOMMANDATION SUPORDO** : couvrir en V0 édition, génération PDF, envoi, finalisation/numérotation, acceptation/signature, duplication, avenant. Différer relance automatique, partage lien public, export multi-format et archivage — fonctionnalités secondaires bien documentées mais non structurantes pour un premier contrat fonctionnel.

## 8. Règles et conditions

**ACQUIS DOCUMENTAIRE** (3B §10, 3C §14) — typologie de conditions observées, à ne jamais fusionner avec un état/une permission/une dépendance (discipline explicitement respectée par les 8 rapports d'agents) :

- Condition de donnée (champs contact valides pour signer).
- Condition de montant (écart devis/facturé nécessitant un arbitrage manuel).
- Condition de rôle/permission (droit « édition de facture », privilèges par action).
- Condition de configuration/abonnement (signature électronique réservée à un palier).
- Condition temporelle (date d'échéance, validité de signature).
- Condition de relation (avenant nécessitant un devis source Accepté, suppression bloquée si documents associés).
- Condition métier citée sans extrapolation légale (recommandation de continuité de numérotation « par analogie », jamais confirmée comme obligation pour le devis).

**RECOMMANDATION SUPORDO** : conserver, dans la spécification comme dans le vocabulaire produit, la distinction fonctionnelle entre **état**, **permission**, **précondition**, **verrou** et **dépendance** — ne jamais les fusionner sous une notion unique de « blocage ». Pourquoi : c'est la discipline que les 8 rapports d'agents ont eux-mêmes strictement respectée pour produire une matière exploitable ; la perdre en conception reviendrait à jeter une partie de la valeur de l'analyse. Cette recommandation ne dit rien d'une architecture ou d'un moteur de règles — c'est une distinction de vocabulaire fonctionnel, pas une décision technique. Aucune règle SUPORDO ne doit invoquer de cause légale pour le verrou du devis lui-même — aucun corpus ne le justifie (3B §6.2, 3C INV-3C-4, CANDIDAT_FORT sans contre-exemple).

## 9. Signature / acceptation / engagement

C'est le point le plus structurant identifié par 3B pour une décision produit (§7, §13 phénomène 1, §18).

**ACQUIS DOCUMENTAIRE** : signature, acceptation, finalisation/numérotation et envoi sont des événements **distincts**, aux effets différents, chez tous les éditeurs qui les documentent séparément — aucune paire n'est interchangeable sur l'ensemble du marché (3B §7). Le marché se scinde en **deux familles à peu près à parité** sur l'articulation signature/acceptation :

- **Séparées** : Vertuoza (SIGNÉ ≠ Chantier en cours, une action « Accepter » distincte reste nécessaire), OpenFire Zendesk (bouton « Confirmer la vente » séparé de la signature).
- **Fusionnées** (signer = accepter automatiquement) : Obat, Costructor, Sellsy (à la signature complète), InterFast (signature électronique → statut Accepté directement).

**VARIANTE DE MARCHÉ** : les deux modèles sont également bien attestés ; aucune information ne documente *pourquoi* un éditeur a choisi l'un ou l'autre (contrainte technique, choix produit délibéré, historique) — 3B §18.

**RECOMMANDATION SUPORDO** : traiter conceptuellement signature et acceptation comme **deux événements distincts**, même si une première itération peut les présenter à l'utilisateur comme une seule action. Pourquoi : cette distinction reste compatible avec les deux familles de marché (rien n'empêche de les fusionner dans le parcours utilisateur si la distinction existe déjà conceptuellement ; l'inverse — les séparer plus tard alors qu'elles n'ont jamais été distinguées — est plus coûteux). C'est une remarque de robustesse conceptuelle, pas une architecture de données ni un choix d'UX arrêté.

**DÉCISION SUPORDO À ARBITRER** : laquelle des deux familles de marché adopter pour l'expérience utilisateur — signature et acceptation séparées (avec point de contrôle humain distinct) ou fusionnées (signer = accepter automatiquement) ? Les deux modèles sont également bien attestés (§ ci-dessus) ; ce choix est réservé au Product Owner, cf. §18.

**À TESTER TERRAIN** : laquelle des deux familles (séparée vs fusionnée) convient le mieux à l'usage réel des artisans SUPORDO — le corpus ne permet pas de trancher ce point de calibrage (3B §18).

**DÉCISION SUPORDO À ARBITRER** (verrou de mutabilité) : lequel des cinq modèles de verrouillage observés (3B §6.2 — direct avec recovery nommé, direct avec recovery indirect via un objet lié, indirect porté par un objet créé à l'acceptation, dur sans recovery, absence de verrou technique remplacée par une invalidation logique) adopter pour SUPORDO ? Aucun modèle ne domine numériquement (2 éditeurs max chacun) et aucune cause légale n'est jamais invoquée pour ce verrou (3B §6.2, 3C INV-3C-4) — SUPORDO n'est donc contraint par aucune obligation externe sur ce point, ce qui laisse un choix ouvert plutôt qu'une convention à copier. **RECOMMANDATION SUPORDO**, limitée au principe et non au modèle précis : quel que soit le modèle retenu, il doit être **métier, jamais présenté comme légal**, et accompagné d'un **recovery nommé** (cohérent avec le fait que 3 des 5 éditeurs qui verrouillent en documentent un, et avec le principe retenu en §17).

## 10. Modification / versions / variantes / avenants

**ACQUIS DOCUMENTAIRE** (3B §8, §13 phénomène 4) — quatre mécanismes fonctionnellement distincts, jamais tous les quatre chez un même éditeur, répondant à des besoins différents :

| Mécanisme | Nature | Meilleure preuve | Convergence |
|---|---|---|---|
| Duplication | Nouvel objet indépendant, lien rompu ou non précisé | InterFast, Sellsy (lien explicitement rompu) | 6/8 |
| Variante | Objet lié, concurrent, une seule gagne ; l'original devient non modifiable mais reste consultable, jamais supprimé | InterFast, Obat | 2/8, mais convergent sur le principe |
| Révision | Historique interne du même objet — **sens différent chez chacun des 2 éditeurs qui l'emploient** (Costructor : version auto ; Vertuoza : formule de prix, piège terminologique) | Costructor | 2/8 |
| Avenant | Toujours additif, jamais fusionné, systématiquement post-engagement | Vertuoza, InterFast | 3/8, convergent sur le principe additif |

**RECOMMANDATION SUPORDO**, priorisée :

1. **Duplication simple** — priorité 1 (mécanisme le plus universel, le moins coûteux à implémenter, comble un besoin de création rapide déjà arbitré en §4).
2. **Avenant** — priorité 1 (convergence forte sur le principe additif, répond directement au besoin terrain BTP de travaux supplémentaires après engagement, cohérent avec le principe « jamais de réécriture silencieuse » retenu en §17).
3. **Variante** (option commerciale concurrente) — priorité 2, fonctionnalité de niche mais bien documentée chez deux éditeurs BTP spécialistes ; pertinente seulement si SUPORDO veut proposer plusieurs options chiffrées au même client.
4. **Révision (historique de versions interne)** — priorité 3, besoin de traçabilité technique plutôt qu'action utilisateur explicite ; peut être satisfait par un historique d'audit générique plutôt qu'un objet dédié.

**À TESTER TERRAIN** : fréquence réelle de chaque mécanisme chez les artisans cibles (3B §19) — aucune donnée d'adoption disponible dans le corpus documentaire.

## 11. Sorties et propagations

**ACQUIS DOCUMENTAIRE** — objets aval démontrés et matrice de relations, voir §3 et tableau 3C §3-§4. Point le plus structurant (3C §5, §17 phénomène 1) : **la relation devis→facture existe universellement comme capacité (8/8, STANDARD_FORT)**, mais son architecture est une **VARIANTE_DE_MARCHE nette**, avec trois modèles :

1. **Transformation directe** (InterFast, Obat, Costructor, Sellsy via conversion manuelle) — condition = un statut minimal du devis (Accepté, Signé ou Finalisé selon l'éditeur), lignes copiées.
2. **Objet pivot obligatoire** (Axonaut via commande automatique ; OpenFire×2 où devis/estimation/bon de commande sont un seul document dont l'état évolue).
3. **Passage exclusif par un objet tiers** (Vertuoza — aucune transformation directe devis→facture n'existe ; seules les voies chantier et intervention y mènent).

**RECOMMANDATION SUPORDO** : adopter la **transformation directe** comme mécanisme de base (modèle InterFast/Obat/Costructor), avec condition = devis Accepté/Signé. Pourquoi : c'est le modèle documenté comme le plus direct pour un utilisateur solo (cohérent avec le positionnement produit de SUPORDO décrit dans la commande de mission — artisan de terrain), il n'impose pas d'objet « commande » intermédiaire non universellement pertinent (absent chez 2/8), et il reste compatible avec un passage optionnel par le chantier quand celui-ci existe (§3, §12).

**DÉCISION SUPORDO À ARBITRER** : faut-il malgré tout un objet « commande client » distinct pour les cas où plusieurs bons de commande/situations doivent être suivis séparément (modèle Sellsy, arborescence 1 devis → N bons de commande) ? Le corpus documente l'existence de ce besoin chez un éditeur sans permettre de juger sa pertinence pour SUPORDO — options présentées, choix laissé au Product Owner, traité comme extension possible plutôt que fondation V0.

## 12. Acompte / situation / solde

**ACQUIS DOCUMENTAIRE** — mécanisme le plus convergent de toute la trilogie après la création de client/catalogue à la volée (3C §6, INV-3C-1 CANDIDAT_FORT) :

- Paramètre d'acompte au niveau du devis (%, montant HT ou TTC) — documenté explicitement par 4/8.
- Facture d'acompte distincte du devis.
- **Déduction automatique et systématique (RECALCULÉ)** de tout montant déjà facturé (acompte + situations antérieures) sur le document de facturation suivant — jamais ressaisi manuellement à l'identique. Documenté par 6/8, jamais contredit.
- Le modèle le plus abouti (OpenFire Odoo) : la facture de solde reprend toutes les lignes avec déduction des situations antérieures, et est « toujours à 0 € » par construction.
- Exclusions croisées fréquentes : acompte + factures partielles multiples souvent incompatibles (Sellsy) ; facture finale bloquée une fois une cascade de situations engagée (Obat) ; primes énergétiques incompatibles avec une facture de situation (Costructor).

**RECOMMANDATION SUPORDO** : reprendre le principe convergent tel quel — un paramètre d'acompte au niveau du devis, une ou plusieurs factures d'acompte/situation comme objets distincts, une déduction automatique systématique (jamais ressaisie) jusqu'au solde. Pourquoi : c'est l'invariant le mieux corroboré de toute l'analyse (INV-3C-1, 6 sources indépendantes, aucun contre-exemple qui infirme le principe, seulement des nuances d'exclusion) — c'est la recommandation la plus fortement étayée de tout ce document. Un seul régime de facturation actif par devis à la fois (acompte simple XOR cascade de situations) est également recommandé, pour éviter les incohérences observées chez plusieurs éditeurs qui interdisent explicitement le mélange ; le détail exact des exclusions croisées reste renvoyé au terrain (§19).

**NON DÉTERMINÉ** : le déclencheur exact du recalcul automatique (statut de la facture d'acompte vs encaissement réel documenté indépendamment) — seul Obat documente une nuance à ce sujet (3C §6).

## 13. Visite / relevé / validation technique

Traité séparément conformément à l'extension demandée par la commande de mission, avec sa propre discipline de preuve (3C §10bis).

**ACQUIS DOCUMENTAIRE** : aucun des 8 corpus ne documente une séquence formalisée à 7 étapes (Demande → Qualification → Devis estimatif → Visite → Relevé → Étude → Devis définitif). Deux cas de continuité **partielle et vérifiée** existent :

- **InterFast** : objet dédié « Visite avant devis » (rapport structuré mobile, métrés, photos, croquis), explicitement positionné pour la phase de découverte. Un bouton génère un **brouillon de devis lié**, mais aucun transfert automatique des métrés vers les lignes (ajout manuel via bibliothèque), aucun devis estimatif distinct, aucun objet étude/calcul séparé.
- **OpenFire (Zendesk)** : « Vital Études », un outil de dimensionnement terrain mobile rattaché obligatoirement à une intervention type. Le seul cas de **génération automatique** de lignes de devis depuis une étude structurée — mais verticalisé (dimensionnement ventilation uniquement), sans dépendance bloquante documentée sur l'envoi/la signature.

Ailleurs (Vertuoza, Axonaut, Sellsy, Costructor, OpenFire Odoo) : briques disjointes ou silence quasi total.

**Cinq notions à distinguer, jamais fusionnées** (demandé explicitement par la commande de mission) :

1. **Estimatif commercial** — chiffrage rapide, non engageant (cf. §14).
2. **Visite / relevé terrain** — observation, mesures, photos.
3. **Étude ou note de calcul éventuelle** — dimensionnement technique.
4. **Validation technique** — contrôle ou accord formel avant devis engageable.
5. **Devis engageable / définitif** — prêt à signature.

**NON DÉTERMINÉ — validation technique bloquante.** Aucun des 8 corpus ne documente de gate formel « validation technique obligatoire avant devis définitif ». Cette absence documentaire ne permet cependant **ni d'affirmer ni d'exclure** qu'un tel gate soit pertinent pour SUPORDO — silence documentaire ≠ absence fonctionnelle, et aucun concurrent n'a été observé refusant explicitement ce mécanisme pour une raison articulée ; le marché ne le documente simplement pas dans le périmètre lu. La question reste **explicitement ouverte**, elle n'est pas tranchée par défaut dans un sens ou dans l'autre.

**DÉCISION SUPORDO À ARBITRER** : SUPORDO doit-il introduire une étape de validation technique bloquante (avant devis engageable) pour les métiers techniques visés (dimensionnement, calcul réglementaire) ? Deux options restent ouvertes, sans qu'aucune ne soit favorisée par ce document faute de preuve de marché dans un sens ou l'autre : (a) aucun gate formel, alignée sur ce qui est observable dans le périmètre lu (mais qui ne prouve pas l'absence du besoin) ; (b) un gate explicite propre aux verticaux techniques de SUPORDO. Choix réservé au Product Owner.

**RECOMMANDATION SUPORDO**, limitée à ce que le corpus permet positivement d'étayer : modéliser VISITE/RELEVÉ comme un objet lié au devis (rapport structuré : métrés, photos, notes) qui **alimente manuellement** les lignes du devis — reprend le seul modèle net et robuste du corpus (InterFast). Pas de génération automatique de lignes depuis une étude proposée pour la V0 (le seul cas positif, Vital Études, est isolé — 1/8 — et verticalisé sur un métier précis, insuffisant pour fonder une généralisation) ; ceci ne préjuge pas qu'une génération automatique soit indésirable pour SUPORDO, seulement qu'elle n'est pas assez étayée pour être recommandée maintenant (cf. §19).

**NON DÉTERMINÉ — objet étude/dimensionnement** : faut-il un objet « étude/calcul/dimensionnement » distinct de la visite ? Aucun des 8 corpus ne le documente comme objet séparé et stable — corpus insuffisant pour conclure dans un sens ou dans l'autre ; à arbitrer par le Product Owner si un besoin apparaît, sans préjugé de ce document.

**À TESTER TERRAIN** : la relation devis↔intervention doit-elle privilégier le sens devis→intervention (attendu, documenté chez InterFast/Vertuoza) ou intervention/étude→devis (dominant chez OpenFire×2) ? Le corpus documente une **inversion de sens structurante et non anticipée** (3C §9, §17 phénomène 4) — seul Costructor documente une boucle bidirectionnelle symétrique. C'est une des deux questions que 3C juge structurellement insuffisantes pour une décision de principe sans corroboration terrain (3C §23, §26).

## 14. Devis estimatif / devis définitif

**ACQUIS DOCUMENTAIRE** : aucun des 8 corpus ne modélise un devis estimatif comme objet distinct d'un devis définitif avec son propre cycle de vie. Le modèle dominant, quand il est explicite, est celui d'**un seul document dont l'état évolue** (OpenFire Zendesk/Odoo : « devis, estimation et bon de commande sont un seul et même document dont l'état évolue »). Le mécanisme de « variante » (§10) répond à un besoin différent — concurrence commerciale entre options, pas progression de précision.

**Mise en garde méthodologique** : l'absence de séparation objet-à-objet chez les 8 éditeurs ne prouve pas, à elle seule, qu'un objet unique soit la bonne conception pour SUPORDO — silence documentaire ≠ absence fonctionnelle. Aucun concurrent n'a été observé refusant explicitement un modèle à deux objets pour une raison articulée ; le marché ne documente simplement pas ce cas dans le périmètre lu. Ce qui suit n'est donc pas présenté comme une conséquence logique de cette absence, mais comme une hypothèse fonctionnelle appuyée par le seul signal *positif* disponible.

**RECOMMANDATION SUPORDO** (hypothèse fonctionnelle, pas une déduction automatique du silence documentaire) : traiter devis estimatif et devis définitif comme **le même objet à plusieurs maturités**, différencié par un état ou un niveau de précision explicite (ex. état `ESTIMATIF` avant relevé/étude, puis `CHIFFRÉ`/`BROUILLON` après), plutôt que deux objets distincts liés par une transformation. Pourquoi : c'est le seul modèle positivement illustré par le marché quand le sujet est abordé explicitement (OpenFire, « un seul document dont l'état évolue ») — l'absence des 7 autres éditeurs n'est pas invoquée comme preuve à l'appui, seulement ce signal positif isolé.

**DÉCISION SUPORDO À ARBITRER** : si un besoin distinct émerge (par exemple présenter au client un chiffrage non engageant sans lui attribuer de numérotation officielle), l'ouverture vers un objet à plusieurs maturités explicites reste disponible et n'est pas fermée par la recommandation ci-dessus — à trancher par le Product Owner si ce besoin apparaît, pas figé par ce document.

## 15. Documents techniques

**ACQUIS DOCUMENTAIRE** (3C §10bis point 4) : seuls deux documents techniques structurés et explicitement rattachés à l'objet devis/intervention existent dans le corpus — le rapport d'intervention PDF (InterFast, Vertuoza) et le rapport Vitalome avec schéma/tableau de dimensionnement (OpenFire Zendesk). Ailleurs, il s'agit de pièces jointes génériques et manuelles (Costructor), sans typage.

**RECOMMANDATION SUPORDO** : prévoir en V0 (a) une pièce jointe générique liée au devis (minimum universel, faible risque) et (b) un objet « rapport de visite/relevé » structuré et rattaché explicitement (aligné sur le modèle InterFast retenu en §13). Génération de documents techniques avancés (schémas de dimensionnement automatiques) hors périmètre V0 — signal trop isolé (1/8) pour investir dessus maintenant.

## 16. Capture voix / photo / documents / IA

Section demandée explicitement par la commande de mission. Aucune architecture IA n'est conçue ici ; seule une cartographie par étape du workflow, fondée sur ce que 3A/3C documentent réellement (devis IA Costructor, import PDF via IA InterFast, assistant vocal Obat — mécanisme interne non détaillé, Vital Études OpenFire Zendesk).

Modèle appliqué à chaque étape : **CAPTURE → COMPRÉHENSION → PROPOSITION STRUCTURÉE → VALIDATION HUMAINE → APPLICATION → TRACE**.

| Étape du workflow | Création humaine (aujourd'hui) | Voix (hypothèse) | Photo (hypothèse) | Document/email/import (hypothèse) | Ce que l'IA pourrait proposer | Validation humaine requise | Donnée métier fiable ensuite |
|---|---|---|---|---|---|---|---|
| Sélection/création du client | Saisie manuelle ou sélection | Dictée du nom/coordonnées | — | Import carte de visite/email signature | Proposition de fiche client structurée | Oui, systématique (création d'entité) | Fiche client validée |
| Construction des lignes (catalogue) | Sélection manuelle dans le catalogue | Dictée d'un poste (« pose de 20m² de carrelage ») | Photo d'un ancien devis papier ou d'un support existant | Import Excel/PDF d'un ancien devis (InterFast le documente) | Rapprochement avec des éléments catalogue existants, proposition de lignes | Oui, systématique (impact financier direct) | Ligne de devis avec prix catalogue au moment de l'ajout (mode technique — snapshot ou référence vivante — à arbitrer, cf. §5) |
| Ligne libre / ajustement | Saisie manuelle de texte + prix | Dictée d'un ajustement ou d'une remise | — | — | Proposition de formulation | Oui | Ligne libre validée |
| Visite/relevé terrain | Formulaire structuré (métrés, notes) | Dictée de mesures/observations pendant la visite | Photo du chantier, d'un défaut, d'un élément à chiffrer | — | Structuration des mesures dictées/photographiées en champs du rapport de visite (aligné modèle InterFast §13) | Oui, avant toute alimentation du devis (aucune génération automatique retenue, §13) | Rapport de visite structuré, lié au devis |
| Étude/dimensionnement (si applicable) | Calcul manuel ou outil externe | — | Photo de plan/schéma existant | Import de fiche technique fournisseur | Proposition de dimensionnement à partir de données structurées (cas Vital Études, verticalisé) | Oui, obligatoire (aucun gate documenté par le marché ; ce document n'en impose pas non plus, question laissée ouverte, §13) | Donnée de dimensionnement, si validée, alimente une ligne |
| Finalisation/envoi | Action manuelle | — | — | — | Relecture/synthèse du contenu avant envoi | Oui (événement d'engagement, §9) | Devis finalisé, traçable |

**Principe retenu, cohérent avec la discipline de la commande** : à chaque étape, l'IA ne fait que **proposer une structuration**, jamais n'applique directement une donnée à impact financier ou contractuel sans validation humaine explicite — cohérent avec le constat documentaire que même les mécanismes les plus automatisés du marché (Vital Études) ne verrouillent rien sans action humaine ultérieure (signature/envoi restent des actions distinctes, 3C §10bis).

## 17. Historique et recovery

**ACQUIS DOCUMENTAIRE** (3B §6, §9, §14 ; 3C §14, §19 point 8) — principe sans contre-exemple sur toute la trilogie : **aucune correction n'est jamais une réécriture silencieuse de l'historique**. Trois mécanismes de recovery documentés :

1. **Réouverture directe du même objet**, via une action nommée (Obat : « annulation de signature », retour à l'état antérieur, pastilles réapparaissent ; InterFast : retour temporaire à Envoyé ; Vertuoza : suppression du chantier vide réouvre le devis).
2. **Objet additif séparé** qui ne remplace jamais l'original (avenant).
3. **Ré-engagement complet** nécessaire (Costructor : modifier un devis signé invalide la signature, oblige une re-signature — pas de blocage technique, mais pas de modification silencieuse non plus).

Correction toujours par document correctif ou retour de statut documenté, jamais par UPDATE discret.

**RECOMMANDATION SUPORDO** : adopter ce principe comme **invariant de conception SUPORDO**, pas seulement pour le devis — toute modification après un événement d'engagement doit produire une trace explicite (avenant, action de recovery nommée avec retour d'état documenté, ou nouvelle signature). Pourquoi : c'est l'invariant le mieux corroboré de toute l'analyse documentaire (aucun contre-exemple sur 8 corpus × 3 missions), et il conditionne directement la confiance qu'un artisan peut avoir dans l'historique de ses documents commerciaux.

## 18. Table de synthèse des positions SUPORDO

Chaque ligne porte un statut explicite en première colonne de la position — un seul des six statuts définis en tête de document. Aucune ligne ne mélange un acquis et une décision sans les distinguer.

| SUJET | ACQUIS | OPTIONS | STATUT + POSITION SUPORDO | POURQUOI | TERRAIN ? |
|---|---|---|---|---|---|
| Rôle du devis | Chiffrage + engagement + source de propagation, 8/8 convergent | — | **RECOMMANDATION** : document de proposition commerciale chiffrée, non engageant par défaut, source de vérité traçable après engagement | Recoupe les 3 fonctions démontrées sans en privilégier une | Non |
| Devis estimatif vs définitif | 0/8 modélise deux objets distincts ; modèle « objet unique évolutif » documenté explicitement (OpenFire×2) | Objet unique à plusieurs maturités / deux objets liés / versions | **RECOMMANDATION** (hypothèse, pas déduction du silence) : objet unique, différencié par état | Seul modèle positivement illustré par le marché quand le sujet est abordé ; l'absence des 7 autres n'est pas invoquée comme preuve | Non pour l'hypothèse ; oui sur le besoin réel d'un chiffrage non engageant distinct |
| Chantier précondition du devis ? | 3/8 lien direct chantier→devis ; Vertuoza documente l'inverse (devis produit le chantier) | Précondition / créable inline / résultat de l'acceptation | **RECOMMANDATION** : chantier non bloquant, créable avant ou après, jamais précondition | 5/8 ne bloquent jamais sur le chantier ; cohérent avec le mode dominant (chantier né du devis accepté) | Oui, sur l'ordre réel de création chez les artisans cibles |
| Client requis ? | 8/8 créable inline ; 3/8 requis à un stade précis (mobile / « 1er temps » / finalisation) | Requis dès le formulaire / requis à la finalisation / jamais bloquant | **RECOMMANDATION** : requis à la finalisation, pas au brouillon | Modèle le mieux attesté isolément parmi les 3 qui tranchent (Obat) ; les 2 autres restent des options légitimes | Non |
| Lignes libres hors catalogue | 4/8 documentent, 3/8 silence cohérent (potentiel choix produit assumé) | Catalogue seul / catalogue + ligne libre | **RECOMMANDATION** : garder catalogue (obligatoire) + ligne libre | Hypothèse d'un besoin d'ajustement texte libre chez le public cible, non démontrée par le corpus lui-même | Oui — le besoin réel et la friction éventuelle d'un modèle « catalogue seul » ne sont pas établis par la documentation concurrentielle |
| États du devis | Vocabulaire non uniforme ; InterFast = seul modèle complet et stable (7 statuts, 2 sources) | Reprendre un modèle existant / en inventer un | **RECOMMANDATION** : Brouillon → Finalisé → Envoyé → Accepté/Signé → Facturé/Chantier ; Refusé/Annulé terminaux | Reprend le seul modèle robuste et documenté deux fois | Non |
| Signature vs acceptation (modèle UX) | 2 familles à parité (séparées vs fusionnées) | Séparer / fusionner dans le parcours utilisateur | **DÉCISION À ARBITRER** : les deux familles restent des options ouvertes, aucune n'est favorisée ici | Preuve également répartie, aucune information sur le pourquoi du choix de chaque éditeur | Oui — explicitement le point de calibrage central |
| Verrou de mutabilité (modèle précis) | 5 modèles distincts, jamais de cause légale | Direct+recovery / direct+recovery indirect / indirect via objet lié / dur sans recovery / absence de verrou technique | **DÉCISION À ARBITRER** sur le modèle précis ; **RECOMMANDATION** sur le principe seul : verrou toujours métier (jamais légal), toujours accompagné d'un recovery nommé | Aucun modèle ne domine numériquement (2 éditeurs max chacun) ; le principe seul est bien corroboré | Oui, pour calibrer le recovery |
| Duplication/variante/révision/avenant | 4 besoins distincts, jamais les 4 ensemble | Prioriser lesquels | **RECOMMANDATION** : priorité 1 duplication + avenant, priorité 2 variante, priorité 3 révision (historique technique) | Duplication = universel/peu coûteux ; avenant = besoin BTP direct ; variante = niche BTP documentée ; révision = traçabilité plutôt qu'action utilisateur | Oui, sur la fréquence réelle de chaque mécanisme |
| Devis → Facture (architecture) | 8/8 capacité ; 3 architectures (directe / pivot / exclusive via chantier) | Directe / objet pivot / exclusive | **RECOMMANDATION** : transformation directe, condition = Accepté/Signé | Modèle le plus direct pour un utilisateur solo ; n'impose pas d'objet commande non universel | Non pour le principe ; oui pour la pertinence d'un objet commande en extension |
| Objet « commande client » distinct | Existe chez 3/8 sous des formes hétérogènes, absent chez 2/8 | Avec / sans objet commande dédié | **DÉCISION À ARBITRER** : non fondé en V0, extension possible | Preuve insuffisante pour juger la pertinence pour SUPORDO dans un sens ou l'autre | Oui |
| Acompte / situation / solde | Mécanisme le plus convergent (INV-3C-1, 6/8, aucun contre-exemple ; confirmé indépendamment par le pilote propagation, INV-5) | — | **RECOMMANDATION**, la mieux étayée du document : paramètre au devis, facture(s) distinctes, déduction automatique systématique | Invariant le mieux corroboré de toute l'analyse, deux fois confirmé indépendamment | Non pour le principe ; oui pour les exclusions croisées à calibrer |
| Génération automatique de lignes depuis une étude | 1 cas net et isolé (OpenFire Zendesk, Vital Études, verticalisé) ; 1 cas d'alimentation manuelle robuste (InterFast) | Alimentation manuelle / génération automatique | **RECOMMANDATION** limitée : alimentation manuelle proposée pour la V0 (ne préjuge pas que l'automatique soit indésirable) | Le seul cas positif de génération automatique est trop isolé (1/8) pour fonder une recommandation en ce sens | Oui, sur la pertinence de la génération automatique pour les métiers techniques visés par SUPORDO |
| Sens devis↔intervention | 2 sens documentés, quasi à parité, 1 boucle bidirectionnelle (Costructor) | devis→intervention / intervention→devis / bidirectionnel | **À TESTER TERRAIN** — 3C juge lui-même cette question structurellement insuffisante sans corroboration terrain | Variance trop structurante pour trancher sans observer l'usage réel | Oui, explicitement |
| Validation technique bloquante | Aucun gate documenté sur 8 corpus (silence, jamais présenté comme une absence confirmée) | Bloquant / non bloquant | **DÉCISION À ARBITRER** — aucune option favorisée par défaut | L'absence de preuve documentaire ne permet ni d'affirmer ni d'exclure la pertinence d'un tel gate | Oui |
| Objet étude/calcul/dimensionnement distinct | Aucun des 8 corpus ne le documente comme objet séparé et stable | Objet dédié / rattaché à la visite | **NON DÉTERMINÉ** — corpus insuffisant pour conclure | Aucune source ne stabilise cette notion comme objet à part | Non déterminable par le terrain seul non plus ; dépend d'abord d'un besoin produit à identifier |
| Trace après correction | Principe sans contre-exemple sur 8 corpus × 3 missions : jamais de réécriture silencieuse | — | **RECOMMANDATION**, très fortement étayée : adopté comme invariant de conception SUPORDO | Invariant le mieux corroboré de toute la trilogie | Non |
| Snapshot vs référence vivante (mode technique) | Tranché explicitement seulement pour le prix catalogue (Obat) et, de façon non uniforme, les coordonnées de facturation vs le nom du chantier (Vertuoza) | Snapshot systématique / référence vivante / mixte | **DÉCISION À ARBITRER** — options posées sans réponse imposée | Preuve trop mince (2 sources, non uniformes) pour recommander un mode unique ; l'anomalie Vertuoza illustre le risque d'un choix non assumé, sans indiquer lequel choisir | Non — c'est un choix de conception, pas une question d'usage artisan |
| Réversibilité de l'état Refusé | Silence quasi total, un seul signal faible (Obat, non confirmé en production) | Réversible / terminal | **NON DÉTERMINÉ** | Corpus insuffisant pour conclure dans un sens ou l'autre | Non prioritaire pour le choix d'une première tranche |

## 19. Décisions nécessitant terrain

- Ordre réel de création chantier/devis chez les artisans cibles SUPORDO (§3, §4).
- Sens à privilégier pour la relation devis↔intervention/étude — jugé structurellement insuffisant par le corpus documentaire lui-même (3C §23, §26).
- Friction réelle d'un modèle « catalogue seul, pas de ligne libre » chez un profil d'artisan SUPORDO (§4).
- Modèle signature/acceptation (séparé vs fusionné) le mieux perçu par les artisans cibles (§9).
- Calibrage du mécanisme de recovery après verrouillage (retour de statut vs re-validation complète) (§9, §17).
- Fréquence réelle d'usage de chaque mécanisme de dérivation (duplication, variante, avenant, révision) (§10).
- Pertinence d'un objet « commande client » distinct pour un usage SUPORDO (§11) — non tranché, extension possible.
- Pertinence de la génération automatique de lignes depuis une étude technique pour les verticaux visés par SUPORDO (§13, §16) — un seul cas de marché, non généralisable sans validation terrain.
- Exclusions croisées à retenir pour le régime acompte/situation (§12).

## 20. Questions encore ouvertes

- Existence ou non d'un minimum de contenu requis pour finaliser un devis (0 ligne, montant nul) — silence total du corpus (§5).
- Déclencheur exact du recalcul automatique de l'acompte (statut vs encaissement réel) — seul Obat documente une nuance (§12).
- Réversibilité de l'état `REFUSÉ` — NON DÉTERMINÉ (§6).
- Nécessité ou non d'un objet « étude/calcul/dimensionnement » distinct de la visite — aucun corpus ne le stabilise comme objet séparé (§13).
- Effet d'une modification du devis après création d'un objet aval sur cet objet déjà créé — silence quasi total du marché (3C §22), à trancher par choix de conception SUPORDO assumé plutôt que copié, faute de précédent.
- Mode technique exact (copié vs référencé) pour la majorité des propagations non listées explicitement en §5 — silence structurel confirmé trois fois par la trilogie (3A/3B/3C), à combler par décision de conception, pas par preuve de marché.

## 21. Première découpe en tranches fonctionnelles candidates

Chaque item ci-dessous est une **TRANCHE FONCTIONNELLE CANDIDATE** — une tranche de construction testable, pas une verticale métier (au sens marché du terme employé ailleurs dans ce document, ex. dimensionnement ventilation) et pas un backlog technique. Chacune est directement dérivable des positions ci-dessus.

**T1 — Création rapide d'un devis**
SITUATION MÉTIER : un artisan veut chiffrer une demande client sans préparation préalable.
COMPORTEMENT ATTENDU : création autonome, client sélectionnable ou créable inline, lignes construites depuis le catalogue et/ou en texte libre, sauvegarde en brouillon sans effet d'état fort.
OBJETS IMPLIQUÉS : Devis (état `BROUILLON`), Client, Catalogue.
RÈGLES CRITIQUES : client non bloquant à ce stade (§4) ; mode technique du prix catalogue à l'ajout de ligne (snapshot ou référence vivante) laissé à arbitrer (§5).
RÉSULTAT UTILISATEUR : un devis brouillon complet, éditable, non numéroté.

**T2 — Finalisation et envoi**
SITUATION MÉTIER : l'artisan veut transmettre un devis chiffré au client.
COMPORTEMENT ATTENDU : passage `BROUILLON → FINALISÉ` (numérotation, client devient requis), puis envoi (`→ ENVOYÉ`), sans verrouillage de contenu à ce stade.
OBJETS IMPLIQUÉS : Devis.
RÈGLES CRITIQUES : numérotation ≠ verrou de contenu (§6, §8) ; client requis à la finalisation (§4).
RÉSULTAT UTILISATEUR : un devis numéroté, transmis, toujours éditable.

**T3 — Engagement du client**
SITUATION MÉTIER : le client accepte ou signe le devis.
COMPORTEMENT ATTENDU : passage `ENVOYÉ → ACCEPTÉ/SIGNÉ`, verrouillage métier du contenu, recovery nommé disponible.
OBJETS IMPLIQUÉS : Devis.
RÈGLES CRITIQUES : signature et acceptation modélisées comme deux événements distincts (§9) ; verrou toujours métier, jamais légal (§8, §9) ; recovery explicite obligatoire (§17).
RÉSULTAT UTILISATEUR : devis engagé, verrouillé, avec un chemin de retour documenté en cas d'erreur.

**T4 — Devis → Facture directe**
SITUATION MÉTIER : un devis accepté doit être facturé.
COMPORTEMENT ATTENDU : transformation directe, lignes/client/montants copiés, devis original conservé et référencé.
OBJETS IMPLIQUÉS : Devis, Facture.
RÈGLES CRITIQUES : condition = devis Accepté/Signé (§11) ; jamais de réécriture silencieuse (§17) ; devis reste consultable après transformation (§17, INV-3C-2).
RÉSULTAT UTILISATEUR : une facture générée, traçable jusqu'au devis d'origine.

**T5 — Acompte puis solde**
SITUATION MÉTIER : l'artisan demande un acompte avant travaux, puis solde en fin de chantier.
COMPORTEMENT ATTENDU : paramètre d'acompte défini sur le devis, facture d'acompte distincte générée, déduction automatique de l'acompte à la facturation du solde.
OBJETS IMPLIQUÉS : Devis, Facture d'acompte, Facture de solde.
RÈGLES CRITIQUES : montant déjà facturé toujours RECALCULÉ, jamais ressaisi (§12, INV-3C-1) ; un seul régime actif (acompte simple XOR cascade de situations).
RÉSULTAT UTILISATEUR : facture de solde correcte sans ressaisie manuelle du montant déjà encaissé.

**T6 — Devis → Chantier**
SITUATION MÉTIER : un devis accepté déclenche le suivi de l'exécution.
COMPORTEMENT ATTENDU : création (ou liaison) du chantier depuis le devis engagé, sans que le chantier ait été un préalable.
OBJETS IMPLIQUÉS : Devis, Chantier.
RÈGLES CRITIQUES : chantier non bloquant à la création du devis (§3, §4) ; référence explicite au devis d'origine conservée (§17).
RÉSULTAT UTILISATEUR : un chantier créé et lié à son devis d'origine, consultable dans les deux sens.

**T7 — Modification après engagement (avenant)**
SITUATION MÉTIER : des travaux supplémentaires apparaissent après acceptation du devis initial.
COMPORTEMENT ATTENDU : création d'un avenant, objet additif distinct, jamais fusionné dans le devis d'origine.
OBJETS IMPLIQUÉS : Devis, Avenant.
RÈGLES CRITIQUES : additif, jamais remplaçant (§10) ; conserve l'historique complet du devis initial (§17).
RÉSULTAT UTILISATEUR : un montant total révisé, avec une trace claire de ce qui a été ajouté et quand.

**T8 — Visite/relevé alimentant un devis**
SITUATION MÉTIER : un artisan effectue une visite technique avant de chiffrer.
COMPORTEMENT ATTENDU : création d'un rapport de visite structuré (métrés, photos, notes), lié au devis, alimentation manuelle des lignes depuis ce rapport.
OBJETS IMPLIQUÉS : Devis, Rapport de visite.
RÈGLES CRITIQUES : pas de génération automatique de lignes en V0 (§13) ; validation humaine systématique de toute proposition issue de la capture (§16).
RÉSULTAT UTILISATEUR : un devis chiffré à partir d'observations terrain tracées et consultables.

---

## Gate final

> Ce document est-il suffisamment précis pour permettre au Product Owner de choisir une première tranche fonctionnelle SUPORDO et seulement ensuite dériver le modèle data, le backend et l'UX nécessaires ?

**PRÊT_POUR_DÉCISION_PRODUIT.**

Justification : les 20 questions d'arbitrage demandées par la commande de mission sont toutes traitées (§4 à §17, table §18), chacune portant un statut explicite parmi les six définis en tête de document — RECOMMANDATION SUPORDO quand une position est proposée et justifiée, DÉCISION SUPORDO À ARBITRER quand les options sont posées sans réponse imposée (signature/acceptation et verrou de mutabilité §9, snapshot vs référence vivante §5, objet commande client §11, validation technique bloquante §13), À TESTER TERRAIN quand le corpus documentaire lui-même se déclare insuffisant (sens devis↔intervention §13), NON DÉTERMINÉ quand le corpus ne permet de conclure ni dans un sens ni dans l'autre (objet étude/dimensionnement §13, réversibilité de Refusé §6). Aucune de ces zones ouvertes n'est masquée en recommandation déguisée. Les huit tranches fonctionnelles candidates (§21) sont directement dérivables des positions prises et suffisamment précises pour être découpées en modèle data, backend et UX sans retour préalable à l'analyse concurrentielle. Les points renvoyés au terrain (§19) portent sur du calibrage fin (fréquence d'usage, sens d'une relation, perception UX) et non sur la structure d'ensemble — ils n'empêchent pas de choisir une première tranche ; ils devront être tranchés avant d'industrialiser les tranches qui en dépendent le plus directement (T6, T8).

STOP.
