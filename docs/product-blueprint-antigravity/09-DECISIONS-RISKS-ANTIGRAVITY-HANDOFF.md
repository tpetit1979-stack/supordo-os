# 09 — Decisions, Risks & Antigravity Handoff

Trois parties : A) registre unique des décisions/inconnues/validations terrain,
réconciliant les listes existantes sans en supprimer aucune ; B) principaux
risques produit et techniques ; C) protocole de transmission à Antigravity, avec
templates de prompts.

## Partie A — Registre des décisions ouvertes

Urgences : `BLOCKS_V1` · `BLOCKS_A_SLICE` · `STRUCTURAL_BEFORE_SCHEMA` ·
`CAN_WAIT_V2` · `CAN_WAIT_V3` · `FIELD_TEST_REQUIRED` · `LEGAL_VERIFICATION_REQUIRED`.

**Une recommandation de ce document reste une `RECOMMANDATION ANALYTIQUE`. Elle ne
devient `SUPORDO_DECISION` que sur arbitrage explicite du PO — cette règle,
héritée de `0007`, s'applique à chaque ligne ci-dessous sans exception.**

| # | Question | Source | Options documentées | Objets | Impact backend | Impact UX | Recommandation analytique | Qui décide | Urgence |
|---|---|---|---|---|---|---|---|---|---|
| Q1 | Ligne libre hors catalogue, oui/non ? | 0007 O1 | 4/8 oui, 3 silences cohérents | Devis, Catalogue | schéma de ligne sans référence catalogue | bouton "ligne libre" dès l'écran devis | autoriser par défaut (majorité relative, coût de l'interdire plus élevé) | PO | `BLOCKS_V1` |
| Q2 | Signature = acceptation, ou deux événements ? | 0007 O2 | 2 séparent / 4 fusionnent, aucune contrainte légale | Devis, Signature électronique | modèle d'état du devis | flux d'acceptation | fusionner par défaut (majorité), garder la séparation possible en V2 | PO | `BLOCKS_V1` |
| Q3 | Où placer le verrou de mutabilité du devis ? | 0007 O3 | 5 modèles, aucun dominant, aucune cause légale sur le devis | Devis | contrainte de mutabilité côté backend | moment où le devis devient non-éditable | verrouiller à la première sortie structurante (M10, 7/8 — l'invariant le mieux prouvé du cycle) | PO | `BLOCKS_V1` |
| Q4 | Objet pivot entre devis et facture, ou transformation directe ? | 0007 O4 | 8/8 se classent dans l'une ou l'autre, aucun ne fait les deux | Devis, Facture | **le trou documentaire le plus important du corpus** (`03` §4) — mode de transformation | invisible pour l'utilisateur si bien fait | transformation directe (pas d'objet pivot), plus simple et cohérente avec l'absence de preuve d'un pivot | PO | `STRUCTURAL_BEFORE_SCHEMA` |
| Q5 | Mécanismes de dérivation à retenir (duplication/variante/révision/avenant) ? | 0007 O5 | 4 mécanismes distincts, aucun éditeur ne les a tous | Devis | modèle de dérivation | boutons d'action sur le devis | V1 = duplication seule ; avenant (bien documenté, additif) en V2 | PO | `CAN_WAIT_V2` |
| Q6 | Minimum de contenu pour finaliser un devis ? | 0007 O6 | silence total 8/8, sauf Vertuoza (bloque à 0 €) | Devis | validation de finalisation | message de blocage éventuel | bloquer à 0 € uniquement, ne rien imposer de plus | PO | `BLOCKS_A_SLICE` |
| Q7 | Verticale de lancement : fumisterie ou climatisation/PAC/chauffage ? | `07` §0 | corpus favorise clim/PAC (2 preuves fonctionnelles indépendantes), le PO cite fumisterie en premier exemple | Pack métier V1 | conditionne tout le pack V1 | conditionne tout l'écran Visite/Relevé | climatisation/PAC/chauffage (voir justification `07` §0) | PO | `BLOCKS_V1` |
| Q8 | Sens de la relation devis ↔ intervention | `03` §4.4, `04` | InterFast : devis→intervention ; OpenFire : intervention→devis ; Vertuoza : bifurcation, critère non documenté | Devis, Intervention | architecture du flux terrain | direction de navigation du parcours D | aucune — corpus contradictoire, pas de majorité exploitable | Terrain d'abord, PO ensuite | `FIELD_TEST_REQUIRED` puis `STRUCTURAL_BEFORE_SCHEMA` |
| Q9 | Jusqu'où automatiser la conformité réglementaire froid (Cerfa/Trackdéchets) en V1 ? | `07` (pack V1) | corpus documente l'obligation, pas le mécanisme applicatif détaillé | Parc installé, Facture | intégration Trackdéchets à border ou non | déclaratif simple vs intégration complète | déclaratif seulement en V1, intégration complète V2 | PO | `BLOCKS_A_SLICE` |
| Q10 | Séparer Personnel et Compte utilisateur dès quand ? | 0007 M14 | 2/6 éditeurs seulement, preuve faible | Personnel, Utilisateur | modèle d'identité (voir `08` §2) | écran de gestion d'équipe | V1 = modèle unifié, séparable en V2 sans migration destructrice si posé correctement dès le début | PO (faible urgence) | `CAN_WAIT_V2` |
| Q11 | Granularité des rôles/permissions | LIGHT (5/10, jamais détaillé) | aucune | Utilisateur, Rôle | modèle de permissions | écran de gestion des droits | rôles minimaux (propriétaire/admin/membre) | PO | `CAN_WAIT_V2`/`CAN_WAIT_V3` |
| Q12 | Vérification officielle de L1 (facture immuable), L2 (avoir même régime), L3 (numérotation continue) | 0007 §L | citées par 6/8/– éditeurs, **jamais vérifiées à Légifrance** | Facture, Avoir | contrainte d'intégrité déjà à poser par précaution (`08` §5) | aucun | appliquer les contraintes dès maintenant (le coût de les respecter par précaution est faible), vérifier la source légale avant toute communication publique de conformité | PO / juridique | `LEGAL_VERIFICATION_REQUIRED` avant mise en production réelle |
| Q13 | Facturation électronique : nombre exact de PDP, version Factur-X, URL Chorus Pro | `06` §2, annexe | non confirmés par la recherche du 23/09/2026 | Facture | choix du/des PDP à intégrer | aucun (transparent si bien abstrait) | revérifier avant tout engagement contractuel avec un PDP | PO / juridique | `LEGAL_VERIFICATION_REQUIRED` avant V2 (branchement réel, échéance 01/09/2027) |
| Q14 | Généralisation de la cascade maintenance/parc installé (Contrat→Ligne de contrat→DI→RDV) | `03` §1, propagation §4.12 | preuve à un seul témoin (OpenFire Odoo), aucune corroboration | Parc installé, Maintenance | modèle de contrat de maintenance | écran de suivi de parc | ne pas généraliser sans validation terrain | Terrain | `FIELD_TEST_REQUIRED` |
| Q15 | Usage réel de la capture voix/photo terrain (parcours G) | `04` §1 | quasi absent du corpus, 2 fragments seulement | Visite/Relevé | conception de l'interface de capture | ergonomie mains-occupées | concevoir un pilote minimal et tester, ne pas sur-construire avant retour terrain | Terrain | `FIELD_TEST_REQUIRED` |
| Q16 | Besoin réel de mode hors-ligne au-delà de la zone Visite/Terrain | `08` §13 | aucune preuve corpus | tout le produit | architecture de synchronisation | disponibilité en connexion dégradée | limiter le hors-ligne à la capture terrain, ne pas l'étendre par défaut | PO / terrain | `FIELD_TEST_REQUIRED` |
| Q17 | Critère de bifurcation devis→chantier vs devis→intervention chez le modèle SUPORDO | `04` (constat Vertuoza : critère jamais documenté) | aucun critère de marché observé | Devis, Chantier, Intervention | logique de branchement | écran de sortie du devis accepté | à concevoir comme un choix explicite proposé à l'utilisateur plutôt qu'une règle devinée | PO | `STRUCTURAL_BEFORE_SCHEMA` |

## Partie B — Principaux risques

| Risque | Nature | Description | Mitigation recommandée |
|---|---|---|---|
| R1 | Produit | Sur-généraliser le modèle de pack métier depuis la seule verticale bien documentée (froid/climatisation) | `02` §4 — concevoir le pack métier assez nu pour qu'"aucune obligation réglementaire" et "pas de parc installé" soient des états valides, pas des exceptions ; valider avec un deuxième pack (fumisterie) avant de généraliser |
| R2 | Produit | L'objet Chantier/Intervention, sous-documenté par le corpus, porte pourtant la différenciation SUPORDO (`03`) | accepter `À TESTER TERRAIN` explicitement, ne pas attendre une preuve documentaire qui n'existe pas |
| R3 | Technique/légal | Le trou documentaire devis→facture (transformation la plus fréquente, la moins documentée du corpus, `03` §4) mal implémenté pourrait compromettre l'irréversibilité légale L1 | trancher Q4 avant le schéma, pas après ; tester explicitement l'invariant "facture numérotée immuable" indépendamment du mode de transformation choisi |
| R4 | Légal | Bascule facturation électronique obligatoire au 01/09/2027 (`06` §2) si l'abstraction PDP n'est pas posée dès V1 | interface abstraite dès V1 (`08` §14), branchement réel piloté comme un jalon calendaire indépendant du reste de la roadmap V2 |
| R5 | Exécution (Antigravity) | Présenter une approximation comme une fonction avancée, implémenter un faux équivalent crédible, promettre dans un plan des éléments finalement absents (mission §16, retour d'expérience direct) | discipline REAL/PROTOTYPE/MOCK/NOT_IMPLEMENTED strictement appliquée à chaque tranche — voir Partie C |
| R6 | Sécurité produit | Détection d'anomalie visuelle par IA (`05` #3) utilisée à tort comme une certification — conséquence potentiellement physique (sécurité gaz/électricité) | jamais de décision automatique sur ce point (`05`), cadrage juridique/assurantiel avant toute construction |
| R7 | Architecture | Sur-architecturer la provenance IA en système de data lineage universel, contredisant explicitement S4 | limiter la provenance aux champs qui servent réellement la validation/sécurité/traçabilité (`08` §8) |
| R8 | Priorisation | Investir du temps V1 sur une intégration catalogue fabricant temps réel alors qu'aucun marché API mature n'existe (`06` §3) | catalogue V1 saisi/importé, pas synchronisé |
| R9 | Sécurité multi-tenant | RLS non posée dès la première migration | `08` §1 — contrainte non négociable avant tout premier déploiement, même pilote |
| R10 | Exécution (Antigravity) | Accès à des chemins locaux ou modification de l'environnement système hors du périmètre du projet (mission §16, retour d'expérience direct) | environnements strictement séparés (`08` §10), permissions explicites, jamais d'écriture directe sur la branche principale sans confirmation |

## Partie C — Protocole de transmission à Antigravity

### Principe

Chaque tranche fonctionnelle (issue de `07`, ex. "Devis V1 — naissance + un
modèle de verrouillage") est transmise indépendamment, avec les documents
pertinents de ce blueprint cités explicitement en contexte. Aucune tranche ne
doit être ouverte tant qu'une question `BLOCKS_V1` ou `BLOCKS_A_SLICE` qui la
concerne (Partie A) n'a pas été tranchée par le PO.

### Template — prompt OBSERVE

```
Avant toute implémentation, observe l'état actuel du dépôt/backend/frontend
concerné par la tranche [NOM DE LA TRANCHE]. Ne modifie rien.

Rapporte :
- quels fichiers, tables, endpoints existants sont pertinents pour cette tranche ;
- pour chacun, son statut réel actuel : REAL (implémenté, connecté, persisté,
  testé) / PROTOTYPE (simplifié, à signaler explicitement en quoi) / MOCK
  (simulé) / NOT_IMPLEMENTED ;
- les hypothèses que tu ferais si tu devais implémenter sans clarification
  supplémentaire ;
- les questions bloquantes avant de commencer, en particulier si l'une des
  questions du registre `09-DECISIONS-RISKS-ANTIGRAVITY-HANDOFF.md` Partie A
  concerne cette tranche et n'a pas encore de décision PO actée.

N'invente aucun comportement métier non spécifié dans les documents de
référence fournis : [lister les documents du blueprint pertinents].
```

### Template — prompt PLAN

```
À partir de l'observation précédente et des documents [lister], produis un
plan d'implémentation pour la tranche [NOM DE LA TRANCHE] uniquement.

Le plan doit :
- lister les fichiers/tables/endpoints à créer ou modifier ;
- déclarer explicitement le statut cible de chaque élément (REAL / PROTOTYPE /
  MOCK / NOT_IMPLEMENTED) — ne jamais planifier un MOCK sans le nommer ;
- respecter les contraintes de `08-BACKEND-AND-NONFUNCTIONAL-CONTRACT.md`
  (isolation RLS, provenance ciblée S4, aucune réécriture silencieuse d'un
  document verrouillé) ;
- ne pas trancher silencieusement une question encore `OPEN` du registre
  Partie A qui bloque cette tranche — s'arrêter et demander plutôt que choisir
  par défaut.

Ne commence pas l'implémentation à cette étape.
```

### Template — prompt IMPLEMENT

```
Implémente strictement le plan validé pour la tranche [NOM DE LA TRANCHE].

Contraintes :
- ne modifie que les fichiers/tables listés dans le plan approuvé ;
- n'installe aucune dépendance non prévue sans le signaler avant de le faire ;
- ne touche pas à l'environnement système ni à des chemins hors du
  projet/dépôt désigné ;
- n'écris jamais directement sur la branche principale ni sur une base de
  données de production sans confirmation explicite ;
- respecte la discipline REAL/PROTOTYPE/MOCK/NOT_IMPLEMENTED déclarée dans le
  plan — si l'implémentation réelle s'avère impossible dans le temps imparti,
  dis-le et livre un PROTOTYPE explicitement signalé plutôt que de simuler
  silencieusement une fonctionnalité avancée (IA, conformité, signature,
  synchronisation) qui n'existe pas réellement.
```

### Template — prompt VERIFY

```
Vérifie la tranche [NOM DE LA TRANCHE] telle qu'implémentée.

- Exécute les tests existants et écris les tests manquants pour les invariants
  critiques de cette tranche (ex. immuabilité d'une facture numérotée,
  isolation RLS multi-tenant, recalcul jamais ressaisi de l'acompte/solde).
- Vérifie visuellement l'application dans l'environnement cible pour toute
  tranche avec un impact interface — une compilation réussie n'est pas une
  vérification suffisante.
- Rapporte, capacité par capacité livrée : REAL (testé et fonctionnel) /
  PROTOTYPE (fonctionne mais simplifié — dis en quoi) / MOCK (simulé — dis ce
  qui manque pour le rendre réel) / NOT_IMPLEMENTED.
- Ne déclare jamais REAL une capacité que tu n'as pas testée toi-même.
```

### Template — prompt AUDIT

```
Effectue un audit indépendant de la tranche [NOM DE LA TRANCHE] livrée, si
possible sans réutiliser le contexte de planification/implémentation qui l'a
produite.

Vérifie :
- toute affirmation d'IA, de conformité, de certification, de signature
  qualifiée, de Factur-X ou de synchronisation correspond-elle à un mécanisme
  réellement implémenté, et non à une simulation présentée comme réelle ? ;
- les contraintes de `08-BACKEND-AND-NONFUNCTIONAL-CONTRACT.md` sont-elles
  respectées (RLS, provenance ciblée, aucune réécriture silencieuse) ? ;
- une question `OPEN` du registre `09-DECISIONS-RISKS-ANTIGRAVITY-HANDOFF.md`
  Partie A a-t-elle été tranchée silencieusement, sans validation PO ? ;
- le statut REAL/PROTOTYPE/MOCK/NOT_IMPLEMENTED déclaré à l'étape VERIFY
  correspond-il à un examen indépendant du code et de l'interface ?

Liste les écarts trouvés, classés par gravité.
```

## Ce que cette partie C ne fait pas

Elle ne remplace pas un cadrage de sécurité Antigravity au niveau de
l'infrastructure (permissions système, accès réseau) — c'est un sujet de
configuration d'environnement, hors du périmètre documentaire de ce blueprint.
