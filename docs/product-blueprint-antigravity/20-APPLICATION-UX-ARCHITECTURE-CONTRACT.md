# 20 — Application UX Architecture Contract

Contrat UX applicatif canonique de SUPORDO. Rejoint la couche
`16`→`20` (voir `16` §1) — n'est ni une recherche ni un historique,
c'est un contrat opérationnel appliqué à chaque tranche à composante UI.

**Ce document n'appartient à aucun outil.** Il ne s'adresse ni à Claude,
ni à Antigravity, ni à Cursor, ni à Lovable, ni à un framework, ni à une
IA particulière. Toute phrase normative utilise "toute implémentation
SUPORDO", "tout contributeur", "une tranche UI", "l'interface doit" —
jamais le nom d'un outil de développement.

## 1. Purpose & Scope

**Rôle** : répondre à "comment toute interface SUPORDO doit-elle
transformer les objets et workflows métier en une expérience cohérente,
continue, rapide et adaptée aux entreprises de terrain ?"

**Ce document couvre** : continuité de contexte, exploitation UI des
relations métier, doctrine d'action suivante, anti-CRUD, anatomie
d'écran, hiérarchie de l'information, différenciation bureau/tablette/
terrain, contrat responsive, cadre de décision de navigation, doctrine
des vues opérationnelles, séparation CORE/VERTICAL au niveau interface,
accessibilité, contrat de validation, registre d'anti-patterns.

**Ce document ne couvre pas** : design visuel final, pixels, une forme
de navigation imposée (sidebar/topbar/bottom-bar), un framework
frontend, le choix de la première verticale métier, les décisions
actuellement `OPEN`, la technologie PWA/offline.

**Relation avec le reste du corpus** — ce document réutilise et
référence, il ne duplique pas :
- `02-CORE-VERTICAL-BLUEPRINT.md` — frontière CORE/VERTICAL au niveau
  **donnée/capacité**. Ce document (`20`) porte la même frontière au
  niveau **interface** (§13) — les deux se complètent, ne se
  chevauchent pas.
- `03-DOMAIN-DEPENDENCIES-LIFECYCLES.md` — graphe des objets métier et
  de leurs relations. Source de vérité pour "quels objets existent et
  comment ils se relient" — jamais recopié ici.
- `04-JOURNEYS-UX-BLUEPRINT.md` — parcours et architecture de
  l'information par zone fonctionnelle, niveau de preuve variable selon
  la zone. Ce document généralise et rend obligatoire ce que `04`
  esquissait par zone.
- `10-SUPPORT-FRICTION-RECOVERY-ATLAS.md` / `11-SIMPLIFICATION-
  PRINCIPLES.md` — doctrine d'intégrité des données et de récupération
  d'erreur (PREVENT/DETECT/EXPLAIN/RECOVER). Doctrine sœur, jamais
  fusionnée : `11` porte l'intégrité et la récupération, `20` porte
  l'architecture d'écran et de parcours.
- `13-ACCEPTANCE-NEGATIVE-TEST-MATRIX.md` — matrice de preuve. §16
  s'y réfère, ne la recopie pas.
- `16-CANONICAL-EXECUTION-INDEX.md` — registre unique des décisions
  ouvertes (Q1→Q19). §18 s'y réfère, ne le recopie jamais.
- `17-BUILD-GATES-AND-SLICE-CONTRACT.md` / `19-SLICE-HANDOFF-
  TEMPLATE.md` — toute tranche à composante UI doit respecter ce
  document ; `19` §"FRONTEND CONTRACT" y renvoie explicitement.
- `docs/brand/BRAND-FOUNDATIONS.md` — identité de marque. §14 trace la
  frontière : la marque ne définit jamais l'architecture produit.
- `docs/architecture/TECHNICAL-STACK-CONTRACT.md` — rails techniques.
  Ce document n'impose aucune technologie, seulement des principes.

## 2. Fundamental Product UX Principles

[PRINCIPLE] Le produit n'est pas une représentation de tables de base de
données. Une structure de données n'est pas, par défaut, une structure
d'écran.

[PRINCIPLE] L'utilisateur travaille sur un contexte métier — un
ensemble d'objets reliés pertinents pour la tâche en cours — jamais sur
un enregistrement isolé.

[PRINCIPLE] Une information déjà connue par le système ne doit pas être
redemandée à l'utilisateur à l'étape suivante lorsqu'elle reste
pertinente.

[PRINCIPLE] Une relation métier structurante du modèle de données doit
être exploitable dans l'interface lorsque sa navigation apporte une
valeur opérationnelle réelle — elle ne doit pas rester une clé étrangère
invisible.

[PRINCIPLE] Le travail concret (quoi faire, quand, où, pour qui) prime
sur les statistiques décoratives dans toute vue opérationnelle.

[PRINCIPLE] Lorsqu'une capacité suivante existe déjà dans le produit,
l'écran courant doit permettre d'y accéder naturellement — une capacité
non construite ne doit jamais être simulée par un lien qui ne mène
nulle part.

[PRINCIPLE] L'information essentielle apparaît d'abord ; le détail
existe sans saturer l'écran ; la complexité ne s'affiche que lorsqu'elle
devient pertinente pour l'utilisateur.

[PRINCIPLE] La continuité de l'expérience prime sur la multiplication de
modules indépendants — une nouvelle capacité doit d'abord chercher à
prolonger un parcours existant avant de justifier un nouvel écran
autonome.

## 3. Context Continuity Contract

[PRINCIPLE] Le contexte métier pertinent suit l'utilisateur d'un objet
vers l'action ou l'objet suivant. Doctrine générale, indépendante des
objets précis impliqués :

```
Objet A → Objet B → Objet C
```

Chaque transition vers un objet B qui dépend d'un objet A déjà identifié
doit porter cette identité vers B sans redemande, tant que la relation
est `HARD` ou `STRUCTURAL` au sens de `03`.

**Ne crée aucun objet universel non décidé.** Aucune entité générique de
type "Affaire" n'est introduite par ce document — elle n'existe dans
aucune `SUPORDO_DECISION` de `0007` ni dans `16`. Si un besoin de ce type
apparaît dans l'implémentation, c'est une `OPEN`, à remonter au PO — pas
une doctrine à déduire silencieusement d'ici.

[EXAMPLE] Client → Devis (client prérempli, non redemandé).
[EXAMPLE] Lieu → Devis (lieu prérempli lorsqu'il est déjà identifié).
[EXAMPLE] Devis → Rendez-vous (devis lié visible, pas juste implicite).
[EXAMPLE] Rendez-vous → Devis (retour possible sans reperte de contexte).

Ces exemples ne sont pas normatifs individuellement — la règle
générale ci-dessus l'est.

## 4. Relation-to-UI Contract

[PRINCIPLE] Une relation structurante (`HARD`/`STRUCTURAL` selon la
grille `03` §3) entre deux objets métier doit être exploitable dans
l'interface — visible, navigable — dès lors que cette navigation sert
une tâche réelle de l'utilisateur.

Critères pour juger qu'une relation "apporte de la valeur opérationnelle"
et doit donc devenir navigable :
- l'utilisateur a besoin de retrouver l'objet lié pour accomplir la
  tâche en cours (ex. retrouver le devis d'un rendez-vous) ;
- la relation conditionne une action possible ou bloquée (`10` P3
  EXPLAIN — la cause d'un blocage doit être visible, pas seulement
  déduite) ;
- la relation porte un état qui affecte la décision de l'utilisateur
  (ex. un devis encore en brouillon vs accepté, visible depuis l'objet
  lié).

Une relation `SOFT`/`OPTIONAL` (`03` §3) n'a pas cette obligation par
défaut — elle peut rester une donnée de second plan.

[ANTI_PATTERN] Une relation `HARD` du modèle qui n'apparaît nulle part
dans l'interface, forçant l'utilisateur à deviner ou à chercher ailleurs
une information que le système connaît déjà.

## 5. Next-Action Doctrine

[PRINCIPLE] Un écran métier ne doit pas se terminer en cul-de-sac
lorsqu'une capacité suivante, déjà construite, existe dans le produit.

[PRINCIPLE] Ne jamais inventer une transition métier qui n'a pas été
décidée. Si la capacité suivante n'existe pas encore ou si le sens de la
transition est `OPEN` (voir `16` §6, ex. Q8/Q17/Q18 — sens Devis↔
Intervention), l'écran ne doit ni la simuler ni forcer un choix que le
produit n'a pas tranché.

[ANTI_PATTERN] Un bouton ou un lien menant vers une capacité non
construite, ou une action suivante inexistante présentée comme
disponible.

## 6. Anti-CRUD Doctrine

[ANTI_PATTERN] Table de base de données → liste brute → formulaire de
champs → bouton "Ajouter" comme architecture UX par défaut d'un objet
métier.

[PRINCIPLE] Une fiche d'un objet métier important (Client, Lieu, et tout
objet `DOMAIN_CORE` équivalent) doit exposer, selon pertinence pour cet
objet :
- identité ;
- contexte (objets reliés directement utiles) ;
- relations (voir §4) ;
- activité récente ;
- historique disponible ;
- actions utiles à partir de cette fiche.

Une fiche qui n'expose que des champs éditables sans aucun de ces
éléments, alors qu'ils existent dans le modèle, viole cette doctrine.

## 7. Screen Anatomy Contract

[PRINCIPLE] Toute nouvelle vue métier doit expliciter, au moment de sa
conception (dans le packet de tranche, voir `19`) :

```
USER_GOAL             — pourquoi l'utilisateur arrive ici
ENTRY_CONTEXT          — quel contexte métier il apporte avec lui
PRIMARY_INFORMATION     — quelle information est prioritaire
PRIMARY_ACTION           — quelle action principale il accomplit
SECONDARY_ACTIONS         — quelles actions secondaires sont utiles
CONTEXT_TO_PRESERVE        — quel contexte doit persister en sortie
NEXT_SUPPORTED_ACTION       — quelle suite est réellement possible (§5)
EMPTY_STATE                  — état sans donnée
LOADING_STATE                  — état de chargement
ERROR_STATE                      — état d'échec
SUCCESS_FEEDBACK                   — confirmation de réussite
```

[ARCHITECTURE_DECISION] Une tranche frontend ne peut pas être considérée
comme close (`DoD`, voir `17`) sans que ces onze champs aient été
explicitement renseignés pour chaque écran métier nouveau ou modifié —
conséquence directe de l'exigence de preuve déjà actée par `13`
(aucune déclaration d'intention non vérifiée). Un champ répondant
légitimement "sans objet" pour cet écran reste acceptable ; un champ
simplement omis ne l'est pas.

## 8. Information Hierarchy & Progressive Disclosure

[PRINCIPLE] L'essentiel apparaît d'abord ; le détail vient ensuite, sans
saturer l'écran initial.

[PRINCIPLE] Le mobile/terrain reçoit une sélection plus fortement
curatée que le bureau (voir §9) — mais **ne supprime jamais une
information critique à la décision de l'utilisateur uniquement pour
gagner de la place**. Curatage ≠ perte d'information nécessaire.

[REFERENCE] InterFast (corpus concurrentiel) restreint délibérément la
surface d'action mobile à un sous-ensemble d'actions terrain plutôt que
de reproduire le CRUD complet du bureau — illustration externe, jamais
une autorité canonique.

## 9. Desktop / Tablet / Field Doctrine

**BUREAU** : densité maîtrisée, clavier/souris, grands écrans, vision
multi-objets, planification.

**TABLETTE** : usage intermédiaire, tactile, contexte chantier/showroom/
véhicule.

**TERRAIN** : smartphone, usage à une main, conditions dégradées
(soleil, bruit, interruptions), actions directes, intégration
téléphone/GPS lorsque pertinent, priorité au contexte immédiat de la
tâche en cours.

[PRINCIPLE] Ces trois contextes d'usage sont distincts et doivent être
pensés séparément — un mode n'est pas une simple contraction visuelle
d'un autre.

**Ce document ne préjuge pas de la PWA ou d'une technologie offline** —
voir `docs/architecture/TECHNICAL-BASELINE.md` de `supordo-app` pour
l'état et la trajectoire réels, hors périmètre canonique ici.

## 10. Responsive Contract

[ARCHITECTURE_DECISION] Toute tranche UI doit être validée au minimum
sur les largeurs suivantes, conséquence directe de la doctrine de preuve
de `13` (aucune déclaration `REAL` sans vérification) appliquée au
responsive :

```
360 px · 390 px · 768 px · desktop
```

[PRINCIPLE] À chaque largeur :
- aucun débordement horizontal accidentel ;
- un ordre de priorité de l'information cohérent avec §8 ;
- un reflow qui préserve le sens, pas seulement l'esthétique ;
- des cibles tactiles dimensionnées pour un usage terrain (main, pas
  seulement pointeur précis) ;
- un comportement défini pour les modales, formulaires, tableaux et la
  navigation à chaque largeur — pas seulement au format desktop.

**Ce document ne fige pas un jeu de breakpoints CSS arbitraire** — les
quatre largeurs ci-dessus sont un seuil de validation, pas une
implémentation imposée.

## 11. Navigation Decision Framework

Ce document ne décide **pas** entre sidebar, top-bar, rail ou bottom-bar
— aucune de ces formes n'est aujourd'hui une `SUPORDO_DECISION` ni une
`ARCHITECTURE_DECISION`. Il fournit les critères pour choisir, à
n'importe quel moment de l'évolution du produit :

[PRINCIPLE] Le choix de forme de navigation doit être réévalué en
fonction de :
- le nombre de domaines fonctionnels réellement actifs ;
- la profondeur de navigation typique d'une tâche ;
- la fréquence d'utilisation de chaque domaine ;
- le rôle de l'utilisateur connecté ;
- le contexte d'usage courant (bureau/tablette/terrain, voir §9) ;
- la surface d'écran réellement disponible ;
- le besoin de recherche globale ;
- le besoin de création rapide, à tout moment, sans changer de contexte.

[ANTI_PATTERN] Faire croître indéfiniment une forme de navigation
simplement parce qu'elle suffisait au périmètre du MVP, sans
réévaluation lorsque le nombre de domaines augmente.

## 12. Operational / Today View Doctrine

[PRINCIPLE] Toute vue "Aujourd'hui", Planning, ou vue terrain doit
prioriser, dans cet ordre de valeur :

```
quoi · quand · où · pour qui · pourquoi · action immédiate
```

[PRINCIPLE] Les indicateurs chiffrés (KPI) ne doivent jamais repousser
le travail opérationnel hors de la première zone utile de l'écran, sauf
justification explicite documentée dans le packet de tranche concerné.

[REFERENCE] Vertuoza (corpus concurrentiel) structure sa vue d'accueil
comme une file de travail actionnable (retards, en attente, à envoyer)
plutôt que comme un tableau de indicateurs, et son éditeur met
explicitement en garde contre la surcharge de widgets — illustration
externe, jamais une autorité canonique.

## 13. CORE UX vs VERTICAL UX

**CORE UX** : principes de ce document, communs à toute entreprise de
terrain quel que soit son métier (électricien, plombier, couvreur,
paysagiste, garage, maintenance, climatisation, fumisterie, etc.).

**VERTICAL UX** : vocabulaire, champs de formulaire, règles de calcul,
documents attendus, actions spécifiques à un métier — injectés dans la
coquille CORE, jamais l'inverse.

[PRINCIPLE] La première verticale construite ne doit pas contaminer
l'architecture UX universelle du CORE. Une coquille d'écran générique
(voir §7) doit accepter une injection de champs/règles verticales sans
que sa structure de navigation, sa hiérarchie d'information ou son
contrat responsive n'en dépendent.

[VERTICAL_EXTENSION] La chaîne `Client → Installation → Appareil →
Intervention` peut être pertinente pour un métier avec suivi de parc
installé (climatisation/PAC, chauffage) — ce n'est **pas** une doctrine
générique du CORE. D'autres métiers (paysagiste, couvreur ponctuel)
n'ont pas nécessairement cette chaîne.

## 14. Brand Foundations vs Product UX

**BRAND** (`docs/brand/BRAND-FOUNDATIONS.md`) : couleur, typographie,
personnalité, identité visuelle — un seul propriétaire, ce document ne
le redéfinit jamais.

**PRODUCT UX** (ce document) : parcours, contexte, hiérarchie,
navigation, responsive, actions, relations.

[PRINCIPLE] Les deux couches coopèrent mais ne se substituent jamais
l'une à l'autre. Un principe de marque (ex. "cohérence avant
décoration") ne dicte pas une architecture d'écran ; un principe
d'architecture (ex. §11) ne dicte pas une couleur ou une police.

## 15. Accessibility & Interaction

[PRINCIPLE] Toute interface SUPORDO doit rester utilisable :
- au clavier, avec un focus visible à tout moment ;
- au tactile, avec des cibles dimensionnées pour un usage terrain ;
- avec des libellés explicites sur les actions et champs, pas
  uniquement des icônes ;
- avec un contraste suffisant pour un usage extérieur (voir §9,
  contrainte soleil) ;
- sans dépendre exclusivement d'un état `hover`, absent sur tactile.

## 16. Validation Contract

[ARCHITECTURE_DECISION] Une tranche UX n'est jamais considérée validée
au seul motif que le code compile, qu'un composant rend, qu'une requête
retourne 200, ou qu'un test DOM trouve un élément — conséquence directe
de la règle déjà actée par `13-ACCEPTANCE-NEGATIVE-TEST-MATRIX.md`
(aucune de ces preuves n'est jamais suffisante pour un comportement
métier), appliquée explicitement ici au rendu et à la navigation UI —
un test de rendu composant (Vitest/RTL) prouve que l'écran s'affiche,
jamais qu'un parcours utilisateur fonctionne.

Selon pertinence pour la tranche, la validation exige :

```
USER STORY → vrais clics → vraie navigation → contexte conservé
→ résultat attendu → responsive (§10) → erreurs/empty states (§7)
→ preuve navigateur/E2E
```

Le format de preuve (résultats de test exécutés, capture, log) reste
celui défini par `13` — non recopié ici.

## 17. Anti-Patterns Register

Registre ouvert, alimenté par ce corpus et par le corpus concurrentiel
classé en `REFERENCE`. Au minimum :

- [ANTI_PATTERN] CRUD par table (§6).
- [ANTI_PATTERN] Dashboard de KPI sans action possible (§12).
- [ANTI_PATTERN] Contexte perdu entre deux écrans reliés (§3).
- [ANTI_PATTERN] Ressaisie d'une donnée déjà connue du système (§3).
- [ANTI_PATTERN] Action suivante présentée comme disponible alors que la
  capacité n'existe pas encore (§5).
- [ANTI_PATTERN] Navigation qui reflète directement le schéma de base de
  données plutôt que les tâches réelles de l'utilisateur (§11).
- [ANTI_PATTERN] Copie miniature du desktop sur mobile plutôt qu'une
  surface d'action curatée pour le terrain (§8, §9).
- [ANTI_PATTERN] Faux module ou chiffre inventé pour remplir une
  interface — rejoint l'interdiction déjà actée par `docs/brand/
  BRAND-FOUNDATIONS.md` ("aucune fausse métrique").
- [ANTI_PATTERN] Redirection silencieuse inattendue lorsqu'une action
  est bloquée, au lieu d'expliquer la cause (`10` P3 EXPLAIN).
  [REFERENCE] Vertuoza — un clic sur une notification vers un module
  inaccessible redirige silencieusement vers le tableau de bord sans
  explication ; l'éditeur lui-même reconnaît le défaut. Illustration
  externe d'un comportement à éviter, jamais une autorité canonique.
- [ANTI_PATTERN] Un choix UX ponctuel transformé silencieusement en
  règle métier implicite, sans passer par une `SUPORDO_DECISION`.

## 18. Open Decisions & Evolution

Registre unique des questions ouvertes : `16-CANONICAL-EXECUTION-
INDEX.md` §6 — jamais dupliqué ici. Pertinentes pour ce document,
notamment :
- [OPEN] Le sens de la relation Devis↔Intervention (Q8/Q17/Q18,
  `03` §4.4) — détermine directement l'application de §3/§5 au parcours
  terrain. Ce document ne le tranche pas.
- [OPEN] La forme de navigation retenue (§11) — aucune `SUPORDO_DECISION`
  ni `ARCHITECTURE_DECISION` à ce jour.
- [OPEN] La liste des verticales au-delà des deux verticales de
  stress-test (`02` §5) — conditionne l'étendue réelle de §13.

**Règle d'évolution** : une modification de ce document doit distinguer
explicitement si elle relève d'un raffinement de `PRINCIPLE` déjà
canonique (autorisé sans arbitrage PO), d'une nouvelle
`SUPORDO_DECISION` (nécessite arbitrage PO, tracée dans `0007`/`16`), ou
d'une `ARCHITECTURE_DECISION` (dérivée directement d'un invariant déjà
acté, sans arbitrage produit). **Une expérimentation locale à une
tranche (`EXAMPLE`) ne devient jamais une doctrine (`PRINCIPLE`) sans
être explicitement généralisée ici** — c'est la règle la plus souvent
violée sous pression de production, au même titre que `16` §11 le
signale déjà pour les décisions ouvertes en général.
