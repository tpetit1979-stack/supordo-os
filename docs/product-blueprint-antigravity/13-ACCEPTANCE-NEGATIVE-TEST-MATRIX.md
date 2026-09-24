# 13 — Acceptance & Negative Test Matrix

Transforme les invariants du Product Blueprint (et les frictions de `10`) en
tests concrets, tranche par tranche (`12`). **Aucun des éléments suivants n'est
jamais une preuve suffisante de comportement métier** : build réussi, page
visible, API renvoie 200. Chaque test ci-dessous doit produire une preuve
vérifiable indépendamment (résultat de test automatisé, capture, log).

## Catégories de test (mission §8)

`HAPPY PATH` · `NEGATIVE PATH` · `BOUNDARY CASE` · `CROSS-TENANT` · `ROLE/
PERMISSION` · `IMMUTABILITY` · `RETRY` · `IDEMPOTENCY` · `PROVIDER FAILURE` ·
`NETWORK FAILURE` · `UPLOAD INTERRUPTION` · `INVALID INPUT` · `AI WRONG OUTPUT` ·
`AI LOW CONFIDENCE` · `HUMAN VALIDATION` · `STALE DATA` · `CONCURRENT EDIT` ·
`MIGRATION` · `BACKWARD COMPATIBILITY`.

Seules les catégories pertinentes sont listées par tranche — ne pas forcer une
catégorie sans objet.

---

## §T0 — Fondations plateforme

| Catégorie | Test | Résultat attendu | Preuve requise |
|---|---|---|---|
| HAPPY PATH | Créer un tenant, s'authentifier, créer une ligne dans la table de test | ligne créée, visible par ce tenant | test automatisé + capture |
| CROSS-TENANT | Tenant A tente de lire une ligne créée par tenant B (via l'API, pas seulement l'UI) | **refus systématique**, y compris en contournant l'UI | test automatisé exécuté directement contre l'API/la base |
| CROSS-TENANT | Tenant A tente d'écrire dans une ligne de tenant B | refus systématique | test automatisé |
| BOUNDARY CASE | Créer deux tenants avec un nom identique | les deux coexistent, aucun mélange de données | test automatisé |
| INVALID INPUT | Créer un compte avec un email déjà utilisé (`10` friction Vertuoza #25) | message d'erreur clair, pas de compte fantôme créé | test automatisé |
| RETRY | Tentative de connexion après mot de passe oublié, flux de reset (P13/`11`) | reset self-service fonctionnel, **jamais** suppression+recréation de compte | test automatisé + test humain |
| MIGRATION | Appliquer le schéma initial sur une base vide | RLS activée dès la première migration, pas ajoutée après coup | audit indépendant de la politique RLS effective en base, pas du code source uniquement |

## §T1 — Création rapide d'un devis

| Catégorie | Test | Résultat attendu | Preuve requise |
|---|---|---|---|
| HAPPY PATH | Créer un devis avec client sélectionné + 1 ligne catalogue | devis `BROUILLON` persisté, réaffiché après rechargement | capture + test automatisé |
| HAPPY PATH | Créer un client à la volée pendant la création du devis (M1, 8/8) | client créé, devis non interrompu | test automatisé |
| NEGATIVE PATH | Créer un devis sans client | comportement dépend de Q1/Q6 — documenter le choix effectif, ne pas le deviner en silence | test automatisé cohérent avec la décision PO actée |
| BOUNDARY CASE | Devis sans aucune ligne, sauvegardé en brouillon | autorisé en `BROUILLON` (le blocage ne s'applique qu'à la finalisation, Q6) | test automatisé |
| CROSS-TENANT | Tenant A tente de lire/modifier un devis de tenant B | refus systématique | test automatisé |
| INVALID INPUT | Ligne avec quantité négative ou prix non numérique | rejet avec message clair | test automatisé |
| CONCURRENT EDIT | Deux sessions du même utilisateur modifient le même devis brouillon simultanément | dernier enregistrement gagne ou conflit signalé — comportement à définir explicitement, pas laissé au hasard | test automatisé + décision de conception documentée |

## §T-PACK-CLIM — Contenu du pack métier climatisation/PAC/chauffage

| Catégorie | Test | Résultat attendu | Preuve requise |
|---|---|---|---|
| HAPPY PATH | Créer un article catalogue avec caractéristiques techniques (marque, puissance, type de fluide) | article utilisable dans une ligne de devis T1 | capture + test automatisé |
| BOUNDARY CASE | Import catalogue en masse (si construit) sans le champ marge (`10` friction Vertuoza M6) | **ne doit jamais silencieusement mettre la marge/le prix à 0** — rejet ou avertissement explicite (P5/P15, `11`) | test automatisé |
| INVALID INPUT | Caractéristique technique manquante sur un article requis par le formulaire de relevé | avertissement clair, pas d'échec silencieux | test automatisé |
| MIGRATION | Ajout d'un second pack métier (simulation, ne construit pas le contenu réel) sans casser le premier pack | schéma extensible sans réécriture (risque R1/`09`) | test de non-régression sur le pack existant |
| CROSS-TENANT | Un référentiel partagé éventuel (marques) reste-t-il visible/isolé correctement selon la conception retenue (`12` §0.8) | comportement conforme à la décision de conception documentée, pas une fuite accidentelle | test automatisé |

## §T2 — Finalisation et envoi

| Catégorie | Test | Résultat attendu | Preuve requise |
|---|---|---|---|
| HAPPY PATH | Finaliser un devis valide (respecte Q6), numérotation attribuée | devis `FINALISÉ`, numéro séquentiel, **toujours éditable** (0.5/`12`, M5) | test automatisé |
| IMMUTABILITY (négatif attendu) | Vérifier qu'un devis `ENVOYÉ` reste modifiable | modification acceptée — **c'est le test négatif de non-verrouillage**, contre-preuve explicite que `T2` ne verrouille rien | test automatisé dédié, pas une simple absence de test |
| BOUNDARY CASE | Finaliser un devis à 0 € (limite Vertuoza, seule preuve du corpus sur Q6) | comportement conforme à la décision PO sur Q6 | test automatisé |
| PROVIDER FAILURE | Le fournisseur d'email transactionnel échoue à l'envoi | statut d'échec visible à l'utilisateur, **jamais présenté comme "envoyé avec succès"** (R5/R10, `09`) | test automatisé simulant l'échec provider |
| RETRY | Renvoi d'un devis après échec d'envoi | pas de duplication d'email, statut mis à jour correctement | test automatisé |
| NUMBERING/BOUNDARY | Deux finalisations quasi simultanées (deux devis) | numérotation strictement séquentielle, aucun trou ni doublon | test automatisé de concurrence |

## §T3 — Engagement du client

| Catégorie | Test | Résultat attendu | Preuve requise |
|---|---|---|---|
| HAPPY PATH | Client accepte/signe un devis `ENVOYÉ` | passage à `ACCEPTÉ/SIGNÉ`, contenu verrouillé | test automatisé + capture |
| IMMUTABILITY | Tentative de modification du contenu après verrouillage, **via l'API directement, pas seulement l'UI** | échec explicite, pas silencieux | test automatisé contournant l'UI |
| NEGATIVE PATH | Recovery : annuler un engagement erroné (P2/`11`) | annulation possible **si aucun objet aval légalement contraint n'existe encore** (pas de facture liée) ; refusée sinon | test automatisé sur les deux cas |
| BOUNDARY CASE | Double tentative d'acceptation (deux clics, deux sessions) | idempotent — un seul passage à `ACCEPTÉ`, pas d'erreur ni de double effet | test automatisé (`IDEMPOTENCY`) |
| PROVIDER FAILURE | Si signature électronique tierce activée (Q2) : le fournisseur échoue ou le document expire (friction Sellsy, `10` — état "expiré" non couvert par `03`) | état "expiré" géré explicitement, chemin de relance documenté | test automatisé |
| ROLE/PERMISSION | Un utilisateur sans droit ne peut pas forcer l'acceptation à la place du client | refus | test automatisé |

## §T4 — Devis → Facture directe

| Catégorie | Test | Résultat attendu | Preuve requise |
|---|---|---|---|
| HAPPY PATH | Facturer un devis `ACCEPTÉ/SIGNÉ` | facture `BROUILLON` puis `NUMÉROTÉE`, lignes/client/montants copiés, devis original consultable | test automatisé + capture |
| NEGATIVE PATH | Tenter de facturer un devis non accepté | refus | test automatisé |
| IMMUTABILITY | Tentative de modification d'une facture numérotée, **par un chemin d'accès direct à la base, pas seulement l'API applicative** | échec systématique — **c'est le test le plus critique de toute la séquence V1** (L1/0007) | test automatisé + audit indépendant (`14`) |
| BOUNDARY CASE | Tentative de re-facturer un devis déjà facturé | comportement défini explicitement (nouveau document distinct ou refus) — jamais laissé indéterminé | test automatisé |
| MIGRATION | Facture importée (L4/0007, cas particulier) coexistant avec des factures natives | jamais assimilée à une facture émise nativement, provenance tracée | test automatisé si la tranche import est construite (V2) |
| BACKWARD COMPATIBILITY | Interface PDP abstraite posée mais non branchée (V1) | le système fonctionne sans PDP réel connecté, sans erreur ni fausse promesse de transmission | test automatisé + vérification qu'aucun badge "transmis" n'apparaît sans transmission réelle |

## §T5 — Acompte puis solde

| Catégorie | Test | Résultat attendu | Preuve requise |
|---|---|---|---|
| HAPPY PATH | Paramétrer un acompte, facturer l'acompte, puis facturer le solde | solde correctement déduit, **recalculé**, jamais ressaisi | test automatisé sur plusieurs montants |
| BOUNDARY CASE | Acompte égal à 100 % du montant total | facture de solde à 0 €, pas d'erreur | test automatisé |
| BOUNDARY CASE | Acompte supérieur au montant total (cas d'erreur de saisie) | rejet ou avertissement explicite | test automatisé |
| INVALID INPUT | Tentative de modifier manuellement le montant déduit affiché sur la facture de solde | champ non éditable, refus si tenté par API directe | test automatisé |
| CONCURRENT EDIT | Deux factures de solde générées quasi simultanément sur le même devis (erreur utilisateur) | comportement défini explicitement (blocage ou détection) | test automatisé |

## §T6 — Devis → Chantier

| Catégorie | Test | Résultat attendu | Preuve requise |
|---|---|---|---|
| HAPPY PATH | Créer un chantier depuis un devis accepté | chantier créé, lien bidirectionnel consultable | test automatisé + capture |
| NEGATIVE PATH | Créer un chantier sans devis (cas autonome, cohérent avec S2) | autorisé, reste sans lien devis | test automatisé |
| BOUNDARY CASE | Tenter de créer un second chantier depuis le même devis | comportement défini explicitement (autorisé ou refusé) — `NON DÉTERMINÉ` par le corpus (`12`), décision de conception à documenter, pas à deviner | test automatisé conforme à la décision prise |
| HAPPY PATH | Rentabilité chantier affichée à vide (aucune dépense/facture encore liée) | calcul dérivé fonctionnel, pas d'erreur, affiche 0 ou équivalent neutre | test automatisé |

## §T8 — Visite/relevé alimentant un devis (niveau 1)

| Catégorie | Test | Résultat attendu | Preuve requise |
|---|---|---|---|
| HAPPY PATH | Remplir un relevé climatisation/PAC (champs fixes du pack), rattacher au devis | relevé persisté, consultable, copiable manuellement vers le devis | test automatisé + capture |
| NETWORK FAILURE | Couper la connexion pendant la capture (formulaire rempli, photo prise) | **rien n'est perdu** — brouillon conservé localement (P6/`11`, M17/`10`) | test automatisé simulant la coupure + test humain terrain si possible |
| UPLOAD INTERRUPTION | Interruption pendant l'envoi d'une photo | reprise ou nouvelle tentative sans perte du reste du relevé | test automatisé |
| HUMAN VALIDATION | Aucune ligne de devis n'est générée automatiquement depuis le relevé en V1 (0.4/`12`) | vérifier explicitement l'**absence** de génération automatique — test négatif volontaire pour éviter toute dérive silencieuse vers `T8-VOIX` avant l'heure | test automatisé de non-régression |
| AI WRONG OUTPUT / AI LOW CONFIDENCE | **Sans objet en V1** (aucune IA dans le scope de cette tranche, voir 0.4/`12`) — catégories à activer explicitement pour `T8-VOIX` (V2) | — | — |
| PROVENANCE | Photo marquée comme publiable sans consentement (S5/0007) | blocage ou avertissement selon la règle de conception retenue en `08` §4 | test automatisé |

## §T8-VOIX (V2, hors scope construction actuelle — matrice préparée par anticipation)

Ne pas construire en V1. Catégories à couvrir **quand** cette tranche sera
ouverte :

| Catégorie | Test | Résultat attendu |
|---|---|---|
| AI WRONG OUTPUT | Dictée mal transcrite ou mal structurée en lignes de devis | jamais finalisé automatiquement — reste un brouillon à valider (P10/`11`, M12/`10`) |
| AI LOW CONFIDENCE | Extraction incertaine sur un champ | signalé visuellement comme incertain, pas présenté avec la même confiance qu'une saisie manuelle |
| HUMAN VALIDATION | Validation explicite requise avant toute ligne ajoutée au devis réel | aucune ligne n'entre dans le devis sans un geste de validation humaine distinct |
| PROVIDER FAILURE | Fournisseur de transcription/LLM indisponible | **aucune donnée inventée**, fallback vers saisie manuelle visible et explicite (mission §8, exemple donné) |
| PROVENANCE | Donnée issue de l'IA intégrée au devis | provenance tracée (S4/0007), consultable |

---

## Règle transversale de preuve (rappel)

Pour chaque tranche de `12`, la case « PREUVES QUE L'AGENT DEVRA FOURNIR » ne se
satisfait d'aucun des trois signaux suivants pris isolément : `build réussi`,
`page visible`, `API renvoie 200`. Un test de cette matrice est considéré
passé seulement s'il vérifie un **comportement métier vérifiable** (état en
base, refus effectif, absence de perte de données), constaté par un résultat de
test automatisé ou une vérification humaine documentée — jamais par une
inspection du code source déclarant l'intention.
