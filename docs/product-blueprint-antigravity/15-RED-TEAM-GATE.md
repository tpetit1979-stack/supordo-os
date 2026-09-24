# 15 — Red Team Gate

Audit adverse indépendant du Product Blueprint SUPORDO avant premier build Google
Antigravity. **L'auteur de ce document n'est pas l'auteur de `00-14`** et n'a reçu
aucun contexte préalable sur le projet. Son rôle est de casser, pas de défendre.

Périmètre lu : `README` + `01` à `14`, `docs/decisions/0007-contraintes-acquises.md`
(intégral), `01-discovery/concurrents/analysis/SUPORDO-CONTRAT-FONCTIONNEL-DEVIS-V0.md`
(intégral), `10` §0. Vérification externe de la documentation officielle Antigravity
(`antigravity.google/docs/*`, `/changelog`, `/terms`) au 23/09/2026.

Le benchmark concurrentiel n'a pas été refait.

---

# A — VERDICT GLOBAL

## `NOT_READY`

Le blueprint est d'une qualité méthodologique inhabituelle : la discipline de preuve
est réelle, les statuts sont tenus, les corrections de `10` et `12` sur `01-09` sont
honnêtes et datées. Ce n'est pas un document complaisant. **Mais il n'est pas
exécutable en l'état**, pour quatre raisons qui ne sont pas des imperfections de
rédaction :

1. **Un `SUPORDO_DECISION` opposable et structurant — S1, le Lieu distinct du client —
   n'est construit par aucune tranche et testé par aucun test.** `03` §4 le désigne
   comme l'effet domino n°1 et exige qu'il soit posé « dès la première migration ». La
   séquence `12` l'a perdu.
2. **La sécurité multi-tenant repose sur une phrase fausse.** `12` écrit « RLS :
   inchangé / héritées de T0 » sur six tranches. Les politiques RLS ne s'héritent pas
   en Postgres. Aucun test cross-tenant n'existe sur Facture, Chantier, Rapport de
   visite ni Storage photo. `12` §0.8 demande en outre explicitement de ne pas poser de
   `tenant_id` systématique sur le Catalogue, en contradiction frontale avec `08` §1.
3. **Le pack de sécurité Antigravity (`14` §3) décrit un moteur de permissions qui
   n'existe pas sur Windows.** La documentation officielle indique que Windows tourne
   encore sur l'ancien système. Le `settings.json` recommandé — la configuration de
   sécurité centrale du projet — ne s'applique pas sur la plateforme réelle du projet.
   Plusieurs garde-fous sont par ailleurs mappés sur des fichiers `Rules`, que la
   documentation officielle décrit comme consultatifs, jamais bloquants.
4. **Le corpus n'a pas d'ordre de précédence.** Neuf conclusions de `00-09` sont
   corrigées par `10`/`12` sans que `00-09` soit modifié, `09` ignore deux questions
   `STRUCTURAL_BEFORE_SCHEMA` créées par `12`, et le `README` — porte d'entrée —
   s'arrête à `09`. Un agent lisant le dossier dans le désordre appliquera des
   conclusions périmées.

Aucun de ces quatre points n'exige de rouvrir le travail d'analyse. Tous sont
corrigeables sans nouvelle recherche corpus. **Le verdict est `NOT_READY`, pas
`NOT_SALVAGEABLE`.**

---

# B — ERREURS CRITIQUES

Neuf. Critères retenus : mauvaise architecture, fuite de données, modèle
non-évolutif, violation d'un invariant métier majeur, faux sentiment de sécurité.

---

### B1 — S1 (Lieu) est acté, structurant, et absent de toute la chaîne d'exécution

**SOURCE** — `0007` §S1 ; `03` §4 point 1 ; `07` §1 (core minimum) ; `12` §2 ; `13`.

**PREUVE**
- `0007` S1 : `SUPORDO_DECISION`. « Le lieu survit au changement de propriétaire, de
  locataire ou de payeur. L'historique d'intervention est rattaché au lieu, pas
  seulement au tiers. **Conséquence : très coûteux à changer — casse la mémoire longue
  et le SAV.** »
- `03` §4 : effet domino **n°1**, « son implémentation doit être posée **dès la
  première migration** ».
- `07` §1 le place en V1 core (« Client + Lieu (S1) »).
- `12` : le mot « Lieu » apparaît **trois fois** — une dans le tableau taxonomique
  §0.2, une dans la DoD de `T-PACK-CLIM` (« rattaché à un client/**lieu** ») qui en
  présuppose l'existence, une hors sujet. **Aucune tranche n'a Lieu dans ses `OBJETS`,
  aucun `SCOPE`, aucune `DEFINITION OF DONE`.** Il n'est pas non plus listé en §3 « ce
  qui reste explicitement hors séquence V1 ».
- `13` : **zéro occurrence de « lieu »**.
- Vérification amont : le contrat fonctionnel V0 contient **zéro occurrence** de
  « lieu ». Le trou est donc hérité de V0, et `12` ne l'a pas rattrapé.

**CONSÉQUENCE** — Le produit se construit avec l'adresse portée par le Client. Chaque
Devis, Facture, Chantier et Rapport de visite créé en T1→T8 se rattache à un modèle
sans Lieu. Introduire S1 après T4 impose de rétro-attribuer un Lieu à toutes les lignes
existantes sans information suffisante pour le faire — exactement le scénario que
`0007` qualifie de « très coûteux ». C'est le contraire d'une décision différable : le
coût croît avec chaque tranche livrée.

**CORRECTION MINIMALE AVANT BUILD** — Poser Lieu dans la première tranche qui crée un
Client (T1), avec la cardinalité minimale Client 1→N Lieu et le rattachement des objets
d'exécution au Lieu, pas au Client. Ne pas construire d'UI Lieu en V1 si le PO ne le
souhaite pas — la contrainte porte sur le **schéma**, pas sur l'écran. Ajouter un test
`13` §T1 vérifiant qu'un Devis porte une référence de Lieu résoluble.

---

### B2 — « RLS : inchangé » est faux, et aucun test cross-tenant ne couvre Facture, Chantier, Visite ni Storage

**SOURCE** — `12` §2 (T1, T2, T3, T4, T5, T6, T8) ; `13` ; `08` §1 ; `09` R9.

**PREUVE**
- `12` T1 : « **RLS/PERMISSIONS : héritées de T0, aucune règle additionnelle.** »
- `12` T2, T4, T5, T6, T8 : « **RLS/PERMISSIONS : inchangé.** »
- En PostgreSQL/Supabase, RLS s'active et se définit **par table**. Une table créée sans
  `ENABLE ROW LEVEL SECURITY` et sans policy est lisible par tout rôle authentifié.
  Il n'existe aucun mécanisme d'héritage. La formulation de `12` est techniquement
  fausse, pas seulement imprécise.
- `13` : tests `CROSS-TENANT` présents uniquement en §T0, §T1 et §T-PACK-CLIM.
  **Aucun** en §T2, §T3, §T4, §T5, §T6, §T8. Les tables Facture, Facture d'acompte,
  Facture de solde, Chantier, Rapport de visite ne sont jamais testées pour l'isolation.
- `12` T8 introduit le **Storage photo**. Les politiques Storage de Supabase sont
  distinctes des policies de table. `13` §T8 ne contient aucun test d'isolation Storage.
- `12` T0 prouve l'isolation sur « **une table factice** ». La preuve d'isolation porte
  donc sur une table qui ne survivra pas à la tranche.

**CONSÉQUENCE** — Un agent qui lit « RLS : inchangé » crée les tables des tranches T2→T8
sans politique. Les factures, les chantiers et les photos de chantier d'un tenant
deviennent lisibles par tout autre tenant. `08` §1 qualifie l'isolation tenant de
« contrainte de sécurité la plus critique du produit » ; `09` R9 l'appelle « non
négociable ». La séquence d'exécution la détruit en sept mots répétés six fois. Et le
dispositif de test donne l'assurance inverse : trois tests cross-tenant verts sur les
trois premières tranches laissent croire que le sujet est traité.

**CORRECTION MINIMALE AVANT BUILD** — (a) Remplacer « inchangé / héritées » par une
obligation explicite : *toute table créée par une tranche active RLS et définit sa
policy tenant dans la même migration ; aucune table sans policy ne passe la DoD*.
(b) Ajouter un test `CROSS-TENANT` (lecture **et** écriture) dans chaque section de
`13` à partir de §T2, plus un test d'isolation de bucket Storage en §T8. (c) Faire
porter la DoD de T0 sur une table réelle du domaine, pas sur une table factice.

---

### B3 — `12` §0.8 interdit le `tenant_id` là où `08` §1 l'exige, sur l'objet qui porte les prix et les marges

**SOURCE** — `08` §1 ; `12` §0.8 ; `12` T-PACK-CLIM ; `13` §T-PACK-CLIM.

**PREUVE** — Contradiction frontale, sur le même objet nommé dans les deux textes.
- `08` §1 : « **Tout objet métier (Client, Lieu, Devis, Facture, Catalogue,
  Personnel...) doit porter un identifiant de tenant dès sa conception**, même en
  environnement pilote à un seul tenant. »
- `12` §0.8 : « **le modèle de données du Catalogue ne doit pas imposer un `tenant_id`
  systématique sur chaque ligne dès la conception** — un référentiel de marques/
  caractéristiques techniques partagé entre tenants [...] doit rester représentable ».
- Le même §0.8 reconnaît pourtant que le Catalogue porte des données privées :
  « **son propre prix, ses propres marges, ses lignes personnalisées** ».
- `13` §T-PACK-CLIM ne teste que « comportement conforme à la décision de conception
  documentée » — un test qui ne peut pas échouer tant que la décision n'est pas prise.

**CONSÉQUENCE** — Le besoin de `12` §0.8 est légitime (ne pas dupliquer un référentiel
de marques par tenant). La solution proposée ne l'est pas : elle mélange, dans un seul
modèle, une donnée partagée et la donnée commercialement la plus sensible du produit —
les prix d'achat et les marges d'un artisan. Un catalogue sans `tenant_id` avec une
policy permissive expose la structure de marge d'un tenant à ses concurrents sur la même
instance. C'est la fuite la plus coûteuse commercialement que ce produit puisse
produire, et elle est introduite par une consigne d'architecture explicite, dans une
tranche présente dans **deux des trois candidats de première tranche**.

**CORRECTION MINIMALE AVANT BUILD** — Séparer en deux objets dès la conception :
`referentiel_produit` (partagé, sans `tenant_id`, **lecture seule pour les tenants**) et
`article_catalogue` (privé, `tenant_id` obligatoire, porte prix/marge/personnalisation,
référence optionnelle vers le référentiel). Cette séparation satisfait `08` §1 et
l'objectif de `12` §0.8 sans arbitrage. Elle n'exige aucune décision PO. Remplacer le
test `13` §T-PACK-CLIM par un test dur : *un tenant ne peut ni lire ni écrire une ligne
de `article_catalogue` d'un autre tenant ; aucun tenant ne peut écrire dans
`referentiel_produit`*.

---

### B4 — Le portail client est introduit en T3 comme surface d'accès externe, hors contrat V0, sans aucun test

**SOURCE** — `12` T3 ; `13` §T3 ; contrat V0 §7 ; `06` §1 et §3.

**PREUVE**
- `12` T3 `FRONTEND` : « action "Accepter"/"Signer" côté client (**portail client
  minimal** ou action manuelle côté artisan si pas de portail en V1) ».
- `12` T3 `RLS/PERMISSIONS` : « **si un portail client existe, accès en lecture seule
  scoping strict au devis concerné** ».
- `13` §T3 : six tests. Aucun ne concerne le portail. Le seul test `ROLE/PERMISSION`
  porte sur « un utilisateur sans droit ne peut pas forcer l'acceptation » — un
  utilisateur **interne**, authentifié.
- Vérification amont : le contrat V0 ne contient ni « portail », ni « espace client »,
  ni aucune notion d'accès externe. V0 §7 **écarte explicitement** le mécanisme
  adjacent : « **Différer** relance automatique, **partage lien public**, export
  multi-format et archivage ». `12` T3 fait donc entrer en V1 une capacité que sa propre
  source de cadrage a différée.

**CONSÉQUENCE** — Un portail client est, par construction, une route d'accès
**non authentifiée ou faiblement authentifiée** vers une donnée de tenant, généralement
par jeton en URL. C'est le point de fuite le plus probable de toute l'architecture : un
jeton devinable, non expirant, non scopé, ou une policy qui autorise la lecture d'un
devis arbitraire donne accès aux devis — donc aux prix, aux clients et aux adresses — de
tous les tenants. Cette surface est mentionnée en deux demi-phrases, laissée optionnelle
(« si un portail existe »), et n'a aucun test. Une capacité optionnelle sans test est
précisément celle qu'un agent implémentera de la façon la plus rapide.

**CORRECTION MINIMALE AVANT BUILD** — Trancher explicitement avant T3 : *pas de portail
en V1* (acceptation manuelle côté artisan, conforme à V0), **ou** portail construit
comme une tranche nommée avec son propre jeu de tests — jeton opaque à forte entropie,
expiration, révocation, scope à un seul devis, et deux tests négatifs obligatoires
(jeton d'un autre devis, jeton d'un autre tenant). Ne pas laisser cette capacité en
option implicite dans une tranche dont le sujet est autre chose.

---

### B5 — Le `settings.json` de sécurité de `14` §3 ne s'applique pas sur Windows

**SOURCE** — `14` §3 ; `14` §17 ; documentation officielle `antigravity.google/docs/permissions` et `/docs/sandbox` (consultée 23/09/2026).

**PREUVE**
- `14` §3 décrit le « moteur de permission fin unifié, trois listes **Deny / Ask /
  Allow**, priorité stricte `Deny > Ask > Allow` », et fournit le `settings.json`
  recommandé du projet — la configuration de sécurité centrale de tout le dispositif.
- La documentation officielle, sur **les deux pages** `/docs/permissions` et
  `/docs/sandbox`, porte la mention suivante, verbatim : « **Windows currently uses the
  permission system described in this section. It will be updated to the unified system
  described above in a future release.** »
- Sur Windows, les contrôles réels sont d'une autre nature : **Security Presets**,
  **Terminal Command Auto Execution** (*Proceed in Sandbox* / *Require Review* /
  *Always Proceed*) et **Agent Non-Workspace File Access** (*Always Allow* / *Always
  Ask* / *Always Deny*). Il n'y a pas de listes `deny`/`ask`/`allow` par action.
- Corollaire non vu par `14` : deux presets Windows — **« Full machine »** *et*
  « Turbo mode » — positionnent l'accès hors dossier sur **Allow**. `14` n'interdit que
  Turbo. Un utilisateur qui choisit « Full machine » pour se simplifier le terminal
  accorde silencieusement la lecture/écriture sur tout le disque, **y compris
  `C:\Users\devfi\supordo-os`** — ce que la première règle minimale du PO interdit.
- À l'inverse, `14` §3 a **raison** sur deux points vérifiés : sur Windows le preset
  Default impose bien *Require Review* sur les commandes, et **aucun preset n'active le
  sandbox** (« None of the presets turn the sandbox on »).

**CONSÉQUENCE** — Faux sentiment de sécurité maximal. La règle PO n°1 (« ne jamais
accéder à `supordo-os` ») est mappée en `14` §17 sur le périmètre du Project et sur les
règles `deny` du `settings.json`. Sur Windows, la première protection est contournable
par un réglage de preset, et la seconde n'existe pas sous cette forme. Le projet
croirait avoir posé une barrière là où il n'y a qu'un réglage d'interface.

**CORRECTION MINIMALE AVANT BUILD** — Trois options, une à choisir :
(a) **Recommandée** — utiliser le mode **WSL** ajouté le 22/09/2026 (changelog v2.16.0 :
*« Added a Windows Subsystem for Linux (WSL) section to Application Settings on
Windows »*), ce qui place le projet sur le chemin de code Linux où le moteur unifié et
le sandbox GA s'appliquent réellement ; (b) rester en Windows natif et **réécrire `14`
§3 dans le vocabulaire Windows réel** (preset `Default` imposé, *Agent Non-Workspace
File Access = **Always Deny***, interdiction explicite des presets « Full machine » et
« Turbo »), en acceptant l'absence de règles par chemin ; (c) déplacer le dépôt
applicatif de sorte qu'aucune règle de chemin relatif ne soit nécessaire. Dans tous les
cas : **vérifier empiriquement sur le build installé**, la documentation et le changelog
se contredisant (voir H).

---

### B6 — Sur Windows le sandbox est désactivé par défaut, ce qui annule la seule protection de secrets invoquée par `14`

**SOURCE** — `14` §3 ; `14` §11 ; `13` (absence) ; `08` §9 ; doc officielle `/docs/sandbox`, `/docs/cli/features`, `/changelog` v2.15.1.

**PREUVE**
- `14` §11 : « **seule protection connue : le sandbox bloque par défaut la lecture de
  `.env` et `~/.ssh`** ».
- `14` §3, dix lignes plus haut : « sous Windows [...] **le sandbox terminal est
  désactivé par défaut**, nécessitant une activation manuelle ».
- Confirmé officiellement : « **None of the presets turn the sandbox on** ». Le blocage
  de `.env` est documenté **comme une propriété du sandbox** (« Sensitive files like
  `~/.ssh` and `.env` are blocked » — *inside the sandbox*).
- `14` se contredit donc : la protection invoquée en §11 est éteinte par le constat de
  §3, sur la plateforme réelle du projet.
- Statut réel du sandbox Windows : **contesté**. `/docs/sandbox` l'étiquette
  « Enable Sandbox Mode (**Preview**) » ; `/docs/cli/features` documente AppContainer
  sans réserve ; le changelog **v2.15.1 du 19/09/2026** — quatre jours avant la date du
  blueprint — annonce « *File and network sandboxing on Windows are now supported* ».
- `13` : **zéro occurrence** de « secret », « clé » ou « key ». Aucun test ne vérifie
  qu'une clé service-role n'atterrit pas dans le bundle client, alors que `08` §9 en
  fait une contrainte explicite.

**CONSÉQUENCE** — Sur la machine réelle, un agent disposant d'un accès terminal peut
lire `.env` sans obstacle, et rien dans le dispositif de test ne détecterait une clé
exposée côté client. La combinaison « `14` §11 se repose sur le sandbox » + « le sandbox
est éteint » + « `13` ne teste aucun secret » constitue un angle mort complet sur le
seul vecteur qui compromettrait toutes les données de tous les tenants simultanément.

**CORRECTION MINIMALE AVANT BUILD** — (a) Activer et **vérifier empiriquement** le
sandbox Windows avant T0, ou passer en WSL (cf. B5) ; (b) ne placer aucun secret réel
dans le périmètre de lecture du Project tant que (a) n'est pas vérifié ; (c) ajouter à
`13` §T0 deux tests : *aucun secret en clair dans le dépôt (scan de motifs sur le diff)*
et *la clé service-role n'apparaît dans aucun artefact servi au client*.

---

### B7 — Cinq des onze garde-fous du PO sont mappés sur des mécanismes que la documentation officielle décrit comme consultatifs

**SOURCE** — `14` §17 (tableau « Règle → Mécanisme d'application concret ») ;
doc officielle `/docs/rules-workflows`, `/docs/skills`, `/docs/hooks`,
`/docs/implementation-plan`.

**PREUVE** — Le tableau `14` §17 est intitulé « **mécanisme d'application concret** ».
Confrontation à la documentation officielle :

| Règle PO | Mécanisme invoqué par `14` | Nature réelle |
|---|---|---|
| Ne jamais accéder à `supordo-os` | Périmètre du Project | Réel **mais** contournable par preset sur Windows (B5) |
| Ne jamais inventer le comportement d'une question `OPEN` | Rule `supordo-doctrine.md` | **Texte de prompt** |
| Ne jamais transformer REAL en MOCK / présenter un MOCK comme REAL | Rule `supordo-honesty.md` | **Texte de prompt** |
| Ne jamais présenter un mécanisme IA/réglementaire comme réel | « même discipline » | **Texte de prompt** |
| Ne jamais considérer le Plan comme preuve | VERIFY/AUDIT | Procédural, non enforcé |
| Ne jamais contourner une RLS ou un test | Hook `force_ask` + AUDIT | Hook = réel (cf. C10 pour Windows) |

La documentation officielle n'emploie, pour les Rules, que des verbes de conseil :
elles sont là pour « **guide** agent behaviors » et sont « **consulted** ». **Aucune
page officielle ne prétend qu'un fichier de règles bloque quoi que ce soit.** Les Skills
sont des paquets d'instructions de même nature. L'approbation de plan est réelle mais
reste **un réglage**, désactivable par « Always Proceed ».

Les seuls mécanismes réellement enforcés par le runtime sont : le moteur de permissions
(Deny bloque, Ask suspend), les hooks `PreToolUse` (`deny`, `force_ask`,
`deny_unless_prior_grant`), le sandbox OS, et la denylist navigateur côté serveur
(fail-closed).

**CONSÉQUENCE** — `09` R5 identifie correctement le risque central : « présenter une
approximation comme une fonction avancée, promettre dans un plan des éléments finalement
absents ». Sa mitigation est une **Rule Markdown** — c'est-à-dire demander poliment à
l'agent de ne pas faire ce qu'on redoute qu'il fasse. Le tableau §17, en présentant ces
lignes comme des « mécanismes d'application concrets », produit exactement le faux
sentiment de sécurité que le blueprint cherche à éviter partout ailleurs.

**CORRECTION MINIMALE AVANT BUILD** — Scinder le tableau `14` §17 en deux colonnes de
statut : **ENFORCÉ** (permissions, hooks, sandbox, denylist, merge humain) et
**CONSULTATIF** (Rules, Skills, discipline de prompt). Pour chaque ligne aujourd'hui
consultative dont l'échec est coûteux, soit poser un contrôle réel (hook `PreToolUse`),
soit déplacer la garantie sur l'étape humaine (`AUDIT`, `TEST HUMAIN`, `MERGE`) en
l'assumant explicitement comme telle.

---

### B8 — S3 (prix catalogue figé), deuxième effet domino du produit, n'a aucun test

**SOURCE** — `0007` §S3 ; `03` §4 point 2 ; `08` §5 ; `13` (absence).

**PREUVE**
- `0007` S3, `SUPORDO_DECISION` : « Un prix repris du catalogue est **copié** dans la
  ligne, pas référencé. Une modification ultérieure du catalogue n'altère pas les
  documents existants. »
- `03` §4 : effet domino **n°2**. « Poser un mode "référence vivante" par défaut
  casserait l'historique dès le premier changement de prix catalogue. »
- `08` §5 : « modifier un prix catalogue ne doit **jamais** altérer une ligne déjà
  émise ».
- `13` : recherche exhaustive sur `snapshot`, `prix`, `S3`, `figé`. **Deux** occurrences
  de « prix », aucune pertinente : un test de saisie invalide (§T1, « prix non
  numérique ») et un test d'import catalogue (§T-PACK-CLIM, marge à 0). **Le test
  central — modifier un prix au catalogue, vérifier que la ligne de devis existante est
  inchangée — n'existe nulle part.**
- Aggravant : `03` §3 documente que le corpus contient **deux modes concurrents** jamais
  réconciliés (snapshot chez Obat, référence vivante chez Vertuoza pour un catalogue
  synchronisé). Un agent sans test peut légitimement implémenter une jointure vivante —
  c'est la solution la plus naturelle en SQL, et elle viole S3 silencieusement.

**CONSÉQUENCE** — La violation est **invisible à la livraison** : au moment de T1 les
prix n'ont pas encore bougé, tous les affichages sont corrects, le test `HAPPY PATH`
passe. Elle se manifeste des semaines plus tard, quand un artisan modifie son catalogue
et voit ses devis émis, ses factures et son historique changer rétroactivement de
montant. À ce stade la correction exige de reconstruire des prix historiques qui n'ont
jamais été stockés. C'est une perte de données irréversible produite par une décision
déjà actée et jamais vérifiée.

**CORRECTION MINIMALE AVANT BUILD** — Ajouter à `13` §T1 un test obligatoire :
*créer un devis avec une ligne catalogue à prix P ; modifier le prix catalogue à P' ;
recharger le devis ; la ligne vaut toujours P*. Étendre le même test à la Facture en
§T4. Ce test est le seul qui distingue une implémentation conforme à S3 d'une
implémentation qui ne l'est pas.

---

### B9 — L3 est testée sur le devis, où elle n'a aucun fondement, et non testée sur la facture, où elle est la contrainte légale

**SOURCE** — `0007` §L3 et §O3 ; `12` T2 ; `13` §T2 et §T4 ; contrat V0 §8.

**PREUVE**
- `0007` **L3**, `LEGAL_CITÉ` : « **Numérotation séquentielle continue.** Pas de trou,
  pas de réattribution, pas de renumérotation. » Le régime porte sur la **facture**
  (sections L1/L2/L3, « contraintes externes » du document comptable).
- `0007` **O3** : « **aucune cause réglementaire sur le devis, dans aucun des 8
  corpus** ».
- `12` T2 impose pourtant au **devis** une numérotation séquentielle, et la justifie
  ainsi : « séquentiel, **cohérent avec le futur régime facture L3** même si le devis
  lui-même n'a pas de contrainte légale — **`0007` §V le rappelle** ».
- **Double défaut.** (i) `0007` **§V** est la section « *Vocabulaire à ne pas
  employer* ». Elle ne dit rien de la numérotation. La citation correcte serait §O/O3.
  (ii) Le contrat fonctionnel V0 §8 **met explicitement en garde contre ce raisonnement
  exact** : recommandation de « continuité de numérotation "**par analogie**" »,
  « **jamais confirmée comme obligation pour le devis** ». `12` fait précisément
  l'analogie contre laquelle sa source de cadrage prévient.
- `13` §T2 teste la séquentialité du **devis** sous concurrence
  (« NUMBERING/BOUNDARY »). `13` §T4 ne contient **aucun** test de numérotation de
  **facture** : ni séquentialité, ni absence de trou, ni comportement sous concurrence.
  Le seul test §T4 pertinent porte sur l'immuabilité (L1), pas sur L3.

**CONSÉQUENCE** — La contrainte légale la mieux identifiée du produit après L1 n'est
vérifiée nulle part sur l'objet qu'elle régit. Deux émissions de facture concurrentes
produisant un doublon ou un trou de numérotation constituent une non-conformité
directement opposable, et rien dans le dispositif ne la détecterait. Symétriquement, une
contrainte inventée est imposée au devis, où elle crée une rigidité inutile (un devis
finalisé puis supprimé laisse un trou dans une séquence qui n'avait pas à exister).

**CORRECTION MINIMALE AVANT BUILD** — (a) Déplacer le test `NUMBERING/BOUNDARY` de
`13` §T2 vers `13` §T4, appliqué à la **facture**, avec émission concurrente et
vérification d'absence de trou et de doublon ; (b) garantir la séquence au niveau base
(séquence transactionnelle ou contrainte, pas un `MAX()+1` applicatif) ; (c) décider
explicitement si le devis porte un numéro séquentiel — et si oui, le documenter comme un
choix produit assumé, **jamais** comme une conséquence de L3.

---

# C — ERREURS MAJEURES

Quinze. Éléments susceptibles de fausser le V1, la première tranche, l'UX
structurante, le choix de verticalité ou la séquence de build.

---

**C1 — L'Avoir disparaît entre `07` et `12` : V1 livre une facture irréversible sans
aucun chemin de correction.**
`07` §1 place « Facture + Avoir (L1 immuabilité) » dans le core minimum V1. `12` ne
construit aucune tranche Avoir, et ne le liste pas non plus en §3 « hors séquence ». Le
mot n'apparaît que dans le tableau taxonomique §0.2 et dans une incise de T5 :
« annulation d'un acompte déjà facturé (**renvoie vers Avoir, hors scope V1 minimal si
non couvert**) » — le blueprint constate son propre trou en passant. Or `03` établit que
l'Avoir est le **seul** véhicule de correction documenté (`HARD`, 6/7 éditeurs, aucune
alternative), et `10` M1 le corrobore à **9/10**, motif quasi universel. Conséquence :
un artisan pilote qui émet une facture erronée n'a aucun recours dans le produit. Le
contournement documenté chez Vertuoza — éditer le PDF avec un outil externe — que `12`
T4 s'engage explicitement à refuser, devient la seule issue réelle. **Correction :**
soit ajouter une tranche Avoir en V1, soit inscrire noir sur blanc dans `07` et `12` que
V1 est livré sans mécanisme de correction, comme dette acceptée et datée.

**C2 — Le Planning/RDV disparaît silencieusement.**
`07` §1 le place en V1 core (« Planning/RDV simple », universel 10/10 LIGHT, « nécessaire
à toute intervention », parcours A et D débloqués). `12` ne le construit pas et ne le
diffère pas explicitement. Comme pour l'Avoir, ce n'est pas un arbitrage : c'est une
omission. Le contrat V0 ne le couvre pas non plus (zéro occurrence). **Correction :**
trancher explicitement — V1, V2, ou hors scope — et l'inscrire dans `12` §3.

**C3 — Le candidat n°2 de première tranche est invalide : il omet un prérequis qu'il
déclare lui-même.**
`12` §4 candidat 2 = `T0 + T-PACK-CLIM + T8`. Or `12` T-PACK-CLIM déclare
« **DÉPENDANCES : T1** (moteur catalogue nu doit exister) » et `12` T8 déclare
« **DÉPENDANCES : T1, T-PACK-CLIM** ». T1 est donc un prérequis déclaré des **deux**
tranches du candidat, et le candidat ne l'inclut pas. Le contenu le confirme : T8
consiste à « alimenter manuellement les lignes de **devis** depuis le rapport » — il n'y
a pas de devis sans T1. Le candidat 2 est, en pratique, `T0 + T1 + T-PACK-CLIM + T8`,
c'est-à-dire la totalité du candidat 3 plus une tranche. Son argument comparatif
(« nécessite Q7 et Q9 tranchées, alors que le candidat 1 n'a besoin que de Q1 ») est
faux : il nécessite aussi Q1. **Correction :** corriger le périmètre et les décisions
bloquantes du candidat 2, ou le retirer. Le PO choisit ensuite — ce document ne choisit
pas à sa place (voir G).

**C4 — Q7 (`BLOCKS_V1`, verticale de lancement) est soumise au PO sur une base de preuve
que `10` a corrigée, et que quatre documents continuent d'affirmer.**
`10` §0.1, titre explicite : « La fumisterie a une preuve fonctionnelle documentaire
réelle — pas seulement marketing », et sur `01`/`02` : « **C'est inexact** ». Le centre
d'aide OpenFire Odoo documente une catégorie native `POELE A BOIS` et des connecteurs
d'achat vers des fabricants nommés (Poujoulat, Modinox, Laudevco, Lorflex, Turbofonte),
fichiers sources vérifiés et hors marketing. Or **quatre** documents portent encore
l'affirmation périmée : `README` (« jamais confirmés en centre d'aide [...]
`MARKETING_ONLY` — aucun des 12 corpus d'aide étudiés ne documente cette verticale »),
`01` §5 (« Aucun concurrent ne cible la fumisterie [...] Le signal existe uniquement
côté marketing »), `02` (« aucune preuve équivalente pour fumisterie »), `07` §0 (« la
fumisterie n'a **aucune** preuve fonctionnelle en centre d'aide dans tout le corpus »).
`09` Q7 reprend le même cadrage. Seul `12` T-PACK-CLIM porte la nuance. L'écart réel est
**2 témoins contre 1**, pas *2 contre 0* — et le PO cite la fumisterie en premier. La
recommandation reste défendable ; l'asymétrie sur laquelle on la lui présente est
surévaluée. *Réserve de fidélité :* `10` décrit une « intégration catalogue fabricant
réelle », `12` paraphrase en « catalogue fumisterie réel » — léger glissement, un
connecteur d'achat fournisseur n'est pas un catalogue verticalisé.
**Correction :** corriger le libellé de Q7 avant de la soumettre au PO.

**C5 — Q18 et Q19 n'existent que dans `12`, alors que le protocole d'exécution renvoie
l'agent au registre de `09`.**
`12` §0.3 crée **Q18** (Chantier ≠ Intervention, urgence **`STRUCTURAL_BEFORE_SCHEMA`**)
et §0.7 crée **Q19**, toutes deux « à ajouter au registre `09` sans le modifier ». `09`
n'a pas été modifié : son registre s'arrête à Q17. Or les templates de prompts de `09`
Partie C — le protocole d'exécution effectif — disent à l'agent de vérifier « les
questions du registre **`09-DECISIONS-RISKS-ANTIGRAVITY-HANDOFF.md` Partie A** ». Un
agent qui suit le protocole à la lettre ne verra jamais Q18. **Correction :** registre
unique, ou index de précédence (voir J).

**C6 — La chaîne de citation de `12` §0 vers le contrat V0 est rompue en trois endroits,
dans les sections mêmes qui corrigent les erreurs de citation de `09`.**
Vérification faite en retournant au contrat V0 intégral :
- `12` §0.3 attribue à « V0 §21 et `0007` O4 » le constat que Vertuoza n'a aucune
  transformation directe devis→facture. Le fait est exact mais se trouve en **V0 §11** ;
  §21 ne mentionne ni Vertuoza ni intervention. Pire, **`0007` O4 affirme l'inverse** :
  « 8/8 se classent dans l'une ou l'autre famille, aucun ne fait les deux » — O4 pose une
  binaire qui *écrase* le troisième cas. `12` s'appuie donc sur une source qui le
  contredit.
- `12` §0.6 cite « V0 **§17** » **deux fois** ; le passage est en **§11**. V0 §17
  s'intitule « Historique et recovery ».
- `12` §0.6 présente « 4/8, 3/8, 1/8 » comme lues dans V0 : **ces fractions n'y figurent
  pas**, ce sont des comptages dérivés (arithmétiquement corrects, dénominateur cohérent
  — OpenFire compte bien pour 2 dans les 8 corpus). Et l'argument de « plurality
  relative » est présenté comme « celle que V0 §17 donne réellement » alors qu'il est un
  **ajout de `12`** ; le troisième motif réel de V0 (« compatible avec un passage
  optionnel par le chantier ») est en revanche omis.
Le fond de ces corrections est juste et utile. La forme reproduit le défaut qu'elles
dénoncent. **Correction :** rectifier les renvois, marquer les comptages comme dérivés.

**C7 — L'IA est totalement évacuée du V1 par `12`, alors que `05`, `07` et le contrat V0
la prévoient, et que `10` vient d'en renforcer la preuve.**
Trois sources placent une IA légère en V1 : `05` opportunité **#4** (transcription vocale
libre, « risque d'erreur : faible », « la brique la plus simple ») et **#1 partie basse**,
toutes deux `V1` ; `07` §1 « IA (V1) : transcription vocale libre ; premier pilote devis
vocal simple » ; et le contrat V0 §16 prévoit explicitement une structuration IA **dans
le rapport de visite** (« Structuration des mesures dictées/photographiées en champs du
rapport de visite », validation humaine « avant toute alimentation du devis »). `12` T8
pose « **IA : aucune en V1** » et revendique reprendre « le **périmètre exact** de T8
tel que défini par V0 §21 » — c'est un **sous-ensemble**, pas le périmètre exact : V0
interdit la *génération automatique de lignes de devis*, pas l'IA dans le rapport. Et
`13` §T8 inscrit « AI WRONG OUTPUT / AI LOW CONFIDENCE : **sans objet en V1** ».
Pendant ce temps `10` §0.3 fait passer la thèse voix de `MARKETING_ONLY` à
**`ACQUIS DOCUMENTAIRE` à 3 témoins** (InterFast, OpenFire Zendesk, **Obat**, ce dernier
documentant un pipeline voix→pré-devis avec validation humaine obligatoire). C'est
l'excès B de l'audit IA : repousser une capacité simple et peu risquée au moment
précis où le corpus cesse de la sous-documenter. La transcription libre (#4) n'est en
outre **ni construite ni explicitement différée** — elle disparaît de la séquence sans
trace. **Correction :** trancher explicitement le périmètre IA du V1 (y compris #4), et
remplacer « périmètre exact de V0 » par « sous-ensemble volontairement plus étroit ».

**C8 — La contrainte d'identité de `08` §2 tombe dans le `OUT OF SCOPE` de T0, alors
qu'elle est précisément une contrainte de conception de T0.**
`08` §2 : « **ne pas fusionner irréversiblement** l'identité "personne physique dans
l'entreprise" et "compte applicatif" dans le même identifiant technique, **même si le
V1 les traite comme un seul objet** côté produit — pour permettre la séparation en V2
sans migration de données destructrice ». `12` T0 se contente de : « OUT OF SCOPE :
[...] personnel vs compte utilisateur (`09` Q10, `CAN_WAIT_V2`) ». La contrainte n'est
pas reportée — elle est *perdue*. Un agent construira `user_id` comme identité unique,
et la séparation V2 deviendra exactement la migration destructrice que `08` interdit.
**Correction :** remonter la contrainte dans le `BACKEND` de T0.

**C9 — Le régime « facture importée » (L4) exigé « dès le départ » par `08` §5 n'existe
dans aucune tranche.**
`08` §5 : le modèle « doit prévoir **dès le départ** un régime distinct » pour une
facture importée, « sans quoi les contrôles d'immuabilité et de numérotation continue
(L1/L3) appliqués aux factures natives seraient à tort imposés à des données de
reprise, ou l'inverse ». `12` T4 crée la Facture sans aucun discriminant
natif/importé, et `13` §T4 renvoie le test à « si la tranche import est construite
(V2) ». Ajouter un discriminant de régime après que des factures immuables existent est
exactement la migration coûteuse que `08` cherche à éviter. **Correction :** poser la
colonne de régime/provenance en T4, sans construire l'import.

**C10 — L'étape `AUDIT INDÉPENDANT` repose sur des mécanismes non confirmés par la
documentation officielle, et les hooks — seul levier réellement enforçant — n'ont
aucune sémantique Windows documentée.**
`14` §15 s'appuie sur **Teamwork** (`/teamwork-preview`, rôles Critic / Challenger /
Auditor / Success Auditor) et sur des « subagents nommés pouvant lire les transcripts
les uns des autres ». La recherche dans la documentation officielle actuelle ne retrouve
ni Teamwork, ni ces rôles, ni la lecture croisée de transcripts : `/docs/subagents`
documente **trois subagents intégrés** (Research, Browser, Self). `14` signale
honnêtement le statut `-preview` de Teamwork, mais l'étape `AUDIT INDÉPENDANT` figure
comme obligatoire dans la séquence §16 et porte, en §17, la garantie « ne jamais
contourner une RLS ou un test ». Par ailleurs `/docs/hooks` confirme les cinq événements
et les décisions bloquantes (`deny`, `force_ask`, `deny_unless_prior_grant`) — mais
**ne mentionne ni Windows, ni PowerShell, ni `.bat`/`.ps1`, ni quel interpréteur exécute
le champ `command`** ; les seuls exemples officiels sont des scripts `.sh`. Les trois
hooks recommandés par `14` §6 sont donc les garde-fous les plus importants du
dispositif, et les moins vérifiables sur la plateforme réelle. **Correction :** tester
empiriquement un hook trivial sur Windows **avant** T0 ; si les hooks ne s'exécutent pas,
le dispositif de sécurité entier doit être repensé (WSL, cf. B5). Retirer ou marquer
`NON VÉRIFIÉ` les affirmations Teamwork.

**C11 — Aucune position de gouvernance des données, alors que les conditions officielles
autorisent la revue humaine du contenu transmis.**
`/terms` officiel, verbatim : « **Google employees and contractors may access, view,
review and use Interactions** », les interactions étant enregistrées et utilisées pour
« evaluate, develop, and improve Google and Alphabet research, products, services and
machine learning technologies ». Un opt-out existe (réglage de télémétrie du compte),
et l'offre Enterprise est matériellement différente — mais « **Antigravity IDE is not
supported for enterprise customers** ». `14` §11 ne traite que les secrets techniques et
ne dit rien de ce sujet. Le pilote manipulera des données personnelles réelles (noms,
adresses, factures d'artisans et de leurs clients). `08` §10 exige déjà que les données
de tenants réels ne soient jamais accessibles en développement — ce qui est la bonne
barrière — mais elle n'est nulle part reliée à cette contrainte contractuelle.
**Correction :** ajouter à `14` une décision explicite (télémétrie off / Enterprise /
données de dev synthétiques uniquement) avant tout accès MCP à une base contenant des
données réelles.

**C12 — `14` §7 confond deux mécanismes distincts portant un nom voisin.**
`14` §7 pose « **Planning Mode = Request Review** ». Dans la documentation officielle,
« Request Review » est le nom d'un **preset de permissions** (macOS/Linux : « the
sandbox is off and every terminal command requires approval ») et, sur Windows, une
valeur de *Terminal Command Auto Execution*. L'approbation de plan est un objet
différent : l'**Implementation Plan artifact**, soumis à une *artifact review policy*
qui peut être mise à « Always Proceed ». Configurer l'un en croyant configurer l'autre
laisse le contrôle réel ouvert. **Correction :** séparer les deux réglages dans `14`,
avec leurs noms officiels respectifs.

**C13 — Le corpus qui sert de contrat de construction n'est ni committé, ni référencé
dans la carte du dépôt, et son `README` s'arrête à `09`.**
`git ls-files docs/product-blueprint-antigravity/` retourne **0**. Le dossier entier est
en `??`. `CLAUDE.md` pose pourtant « Git = état durable ». Le dossier n'apparaît ni dans
`01-discovery/ARBORESCENCE.md` ni dans le `README` racine. Et le `README` du blueprint
lui-même s'arrête à `09` dans sa carte des documents : `10` à `14` — dont les cinq
corrections de `10` §0, les neuf réconciliations de `12` §0 et tout le pack Antigravity —
n'y figurent pas. La porte d'entrée du dossier dirige le lecteur vers la version
périmée. **Correction :** committer, enregistrer dans ARBORESCENCE, compléter la carte
du `README`.

**C14 — « Client devient requis à la finalisation » est une règle de validation
structurante qui n'appartient à aucune question du registre, et `13` la route vers des
questions qui ne la couvrent pas.**
`12` T2 `SCOPE` : « passage `BROUILLON → FINALISÉ` (numérotation, **client devient
requis**) ». C'est une contrainte d'intégrité, pas un détail d'UI. `13` §T1 traite le cas
« Créer un devis sans client » en renvoyant à « **Q1/Q6** » — or Q1 porte sur la ligne
libre et Q6 sur le minimum de contenu ; **aucune des deux ne porte sur l'obligation de
client**. `03` classe la relation Client→Devis en `SOFT`/`STRUCTURAL`, `HARD` chez
OpenFire seul. La règle vient en réalité du contrat V0 §4 (« client requis à la
finalisation, pas à l'enregistrement en brouillon ») — un renvoi que ni `12` ni `13` ne
font. **Correction :** citer V0 §4 dans `12` T2, et corriger le renvoi de `13` §T1.

**C15 — Trois catégories de test annoncées ne sont jamais instanciées ; le soft-delete,
principe le mieux corroboré du corpus, n'est testé nulle part.**
`13` déclare en tête 19 catégories. **`STALE DATA` n'est utilisée dans aucun test.**
Aucune catégorie « soft delete / archivage / recovery » n'existe, alors que `11` P1
(« aucune suppression dure sur un document engagé ») s'appuie sur `10` **M4**, décrit
comme « le motif positif le **mieux corroboré du corpus entier** » (5/10 indépendants).
Aucun test de **rollback de migration** non plus, alors que `13` §T0 teste l'application
d'un schéma initial. Enfin `11` P6 avertit lui-même que « la complexité réelle de la
synchronisation offline (**conflits, doublons potentiels lors de la reconnexion**) ne
doit pas être sous-estimée » — et `13` §T8 ne teste que « rien n'est perdu », jamais la
resynchronisation conflictuelle. **Correction :** instancier ou retirer `STALE DATA` ;
ajouter un test de suppression/archivage par tranche créant un document engageable ;
ajouter un test de resynchronisation avec conflit en §T8.

---

# D — AMBIGUÏTÉS À MAINTENIR `OPEN`

Aucune décision n'est proposée ici. La preuve manque, et en proposer une serait
reproduire le défaut que le blueprint combat.

| # | Question | Pourquoi elle doit rester ouverte |
|---|---|---|
| D1 | **O1-O6 / Q1-Q6** — ligne libre, signature=acceptation, verrou de mutabilité, pivot devis→facture, mécanismes de dérivation, minimum de contenu | Vérification faite : le contrat V0 **n'en arbitre aucune**. Le terme `SUPORDO_DECISION` n'y apparaît pas une seule fois ; son statut « DÉCISION SUPORDO **À ARBITRER** » est défini comme « réservé au PO, options présentées sans réponse imposée ». Bilan réel : **0 décidée**, 3 recommandées (O1, O4, O5), 2 réservées au PO (O2, O3), 1 `NON DÉTERMINÉ` (O6). Le gate de V0 dit « PRÊT_POUR_DÉCISION_PRODUIT » — prêt pour, pas décidé. `0007` §O les liste toujours comme ouvertes et aucune n'est remontée en section S. **Elles sont donc toutes intactes.** |
| D2 | **Q18 — Chantier et Intervention sont-ils deux objets ?** | `12` §0.3 a raison de la poser et raison de ne pas la trancher. Le corpus emploie les deux mots de façon inconsistante selon l'orientation de l'éditeur. `STRUCTURAL_BEFORE_SCHEMA` maintenu. |
| D3 | **Q8 — sens de la relation devis ↔ intervention** | Corpus contradictoire chez des éditeurs différents, aucune majorité. `FIELD_TEST_REQUIRED` justifié. |
| D4 | **Q17 — critère de bifurcation devis→chantier vs devis→intervention** | Aucun critère de marché observé, y compris chez Vertuoza qui bifurque sans le documenter. La proposition de `04`/`09` (choix explicite offert à l'utilisateur plutôt que règle devinée) est la bonne posture face à un vide de preuve. |
| D5 | **O6/Q6 — minimum de contenu pour finaliser** | Nuance à préserver : V0 §5 conclut `NON DÉTERMINÉ` (« silence total sur les 8 corpus ») et **ne reprend pas** le signal Vertuoza « bloque à 0 € ». `09` Q6 et `12` T2 en font pourtant leur recommandation. Un signal à 1 témoin que la source aval a écarté ne doit pas devenir un défaut. |
| D6 | **Deux chantiers depuis un même devis ; re-facturer un devis déjà facturé** | `12` T4/T6 les laissent `NON DÉTERMINÉ` — c'est correct. M7 (1→N, jamais 1→1) plaide pour l'autorisation, mais M7 porte sur le devis en général, pas sur ce cas. Ne pas trancher par analogie. |
| D7 | **Catalogue : référence vivante pour une source externe synchronisée** | `03` §3 documente deux modes coexistants jamais réconciliés (Obat snapshot / Vertuoza CEBEO référence vivante). S3 tranche pour le catalogue propre au tenant ; il ne dit rien d'un catalogue synchronisé externe. Ne pas étendre S3 par défaut à un cas qu'il ne couvre pas. |
| D8 | **L1/L2/L3 — vérification à la source officielle** | `0007` est explicite : aucune n'a été vérifiée sur Légifrance. `09` Q12 propose de les appliquer par précaution — c'est la bonne posture (coût de conformité faible, coût de non-conformité élevé). La **vérification** reste due avant toute communication publique de conformité. À noter : `10` §0.4 ajoute que ProGBat invoque une base légale précise (« loi de finance 2016 ») elle aussi non vérifiée. |
| D9 | **Terminologie PDP / « Plateforme Agréée »** | L'annexe `06` §9.2 établit que le décret n° 2026-677 du 27/07/2026 remplace « PDP » par la notion unique de **« plateforme agréée » (PA)**. `06` §2, `07`, `08` §14, `09` Q13 et `12` T4 continuent d'employer « PDP ». Sujet mineur mais réel pour une abstraction dont le nom porte un statut juridique. Ne pas renommer à la volée — vérifier d'abord, puis nommer une fois. |

---

# E — SUR-ARCHITECTURE

| Élément | Verdict | Justification |
|---|---|---|
| Référentiel catalogue partagé entre tenants (`12` §0.8) | **SIMPLIFY FOR PILOT** | Le besoin est réel mais aucun second tenant n'existe. Poser les **deux tables** (cf. B3) coûte quasi rien et supprime le risque ; construire le mécanisme de partage, non. |
| Accès invité délégué expert-comptable (`08` §1) | **DEFER** | T0 ne construit qu'un seul rôle. Concevoir un scoping non-binaire avant d'avoir deux rôles, c'est abstraire sans deuxième cas. Garder la forme `tenant_id`, différer le modèle d'invité. |
| Trois environnements distincts (`08` §10) | **SIMPLIFY FOR PILOT** | Dev + pilote suffisent : la production n'existe pas encore. La contrainte réelle — *aucune donnée de tenant réel accessible en développement* — est à garder intacte, c'est elle qui porte la valeur. |
| Observabilité par appel externe avec coût mesuré (`08` §12) | **SIMPLIFY FOR PILOT** | V1 n'a qu'une intégration réelle (email). Garder la règle « un échec est visible comme un échec, jamais comme un succès dégradé » ; différer l'instrumentation de latence/coût. |
| P8 étendu à **tout** indicateur agrégé (`11`) | **SIMPLIFY FOR PILOT** | Deux agrégats seulement existent en V1 (acompte/solde, rentabilité), tous deux déjà couverts par `08` §6. Généraliser à « tout indicateur secondaire » avant qu'il en existe, c'est une règle sans objet. |
| P12 — modèle de permissions extensible vers un système fin type Obat (`11`) | **DEFER** | Preuve à 1 témoin (`10` §0.2). Garder les rôles minimaux ; ne pas pré-câbler une matrice de permissions individuelles. |
| P11 — architecture de scellement photo (`11`) | **DEFER** | Déjà V2/V3, correctement borné. Aucune action V1. |
| Adaptateur PDP | **KEEP la couture / DEFER l'adaptateur** | `06` §2 est sourcé en primaire (décret + arrêté sur Legifrance), l'échéance 01/09/2027 est réelle, et corriger après coup est une migration lourde. Mais une *interface* suffit : ne pas écrire d'adaptateur vers un fournisseur non choisi. |
| Pack métier générique/paramétrable | **KEEP NOW (tel que cadré)** | `02` §4 et `12` T-PACK-CLIM font déjà le bon choix : construire **un** pack concret, ne figer le moteur qu'après le second. Rien à retrancher. |
| `14` — Rules + Skills + Hooks + Browser Subagent + subagent auditeur + Teamwork, tous avant T0 | **SIMPLIFY FOR PILOT** | Harnais agentique lourd posé avant d'avoir prouvé une seule tranche. Charge utile réelle : **permissions correctement configurées pour Windows, worktree, revue de plan, hooks (si exécutables), merge humain**. Les trois Skills (`slice-observe`, `slice-verify`, `check-tenant-isolation`) sont des commodités — sauf `check-tenant-isolation`, à garder comme **script** de test plutôt que comme Skill. Teamwork : non confirmé, à écarter du chemin critique. |
| `13` §T8-VOIX préparée par anticipation | **KEEP NOW** | Coût nul, et empêche la dérive silencieuse de T8 vers T8-VOIX. Bon dispositif. |

---

# F — SOUS-ARCHITECTURE

Ce qui doit exister avant le pilote parce que l'ajouter tard coûte disproportionnément
cher. Liste dérivée de l'analyse, non recopiée de la grille de la mission.

1. **Lieu (S1)** — dans la première migration qui crée un Client. Voir B1. Le coût croît
   avec chaque tranche livrée ; c'est le seul élément de cette liste dont le coût de
   report est déjà en train d'augmenter.
2. **RLS par table, posée dans la même migration que la table** — avec la règle
   « aucune table sans policy ne passe la DoD ». Voir B2. Un rattrapage de RLS après
   mise en pilote est, selon `08` §11 lui-même, « un chantier à haut risque ».
3. **Frontière `referentiel_produit` / `article_catalogue`** — deux tables dès la
   conception. Voir B3. Coût immédiat quasi nul, coût de séparation ultérieure élevé
   (les prix et marges sont déjà mélangés).
4. **Snapshot de prix effectivement stocké sur la ligne, et testé** — voir B8. Non
   rattrapable : les prix historiques non stockés sont définitivement perdus.
5. **Séquence de numérotation de facture garantie au niveau base** — voir B9.
6. **Discriminant de régime sur la Facture (native / importée, `provenance`)** — voir
   C9 et `08` §5. Une colonne posée en T4 ; l'import lui-même reste V2.
7. **Identifiants distincts pour la personne et pour le compte applicatif** — voir C8 et
   `08` §2. Une colonne, aucune UI. Sans cela, la séparation V2 est destructive.
8. **Marqueur d'archivage/soft-delete sur les documents engageables** — voir C15 et
   `11` P1. Un document détruit en dur avant l'introduction du soft-delete n'est pas
   récupérable rétroactivement.
9. **Métadonnées de consentement média posées à la création du fichier (S5)** — `08` §4
   le dit déjà (« pas être ajoutée après coup sur des fichiers déjà stockés sans cette
   métadonnée ») ; aucune tranche ne le pose. T8 est la tranche concernée.
10. **Migrations versionnées, ordonnées, rejouables sur base vide** — `13` §T0 teste
    l'application d'un schéma initial, mais rien n'impose un outil de migration ni un
    format. C'est le prérequis de toute reprise sans Antigravity (voir I).
11. **Politique de secrets écrite et appliquée avant T0** — `14` §11 reconnaît devoir la
    construire ; elle n'existe pas encore, et le sandbox Windows ne la remplace pas
    (voir B6).
12. **Trace d'état minimale sur les transitions verrouillantes** — `08` §7 l'exige
    (auteur, horodatage, état précédent) ; aucune tranche ne la construit, alors que T3
    et T4 créent précisément ces transitions.

Ne figurent **pas** dans cette liste, après examen : la provenance IA généralisée (S4 la
borne explicitement, et V1 n'a pas de donnée IA), l'idempotency globale (`13` la couvre
là où elle est utile), et le hors-ligne au-delà de la capture terrain (`09` Q16 le borne
correctement).

---

# G — AUDIT DES CANDIDATS DE PREMIÈRE TRANCHE

**Ce document ne choisit pas à la place du PO.** Les trois candidats sont audités selon
leurs propres déclarations.

### Candidat 1 — `T0 + T1`

| Critère | Verdict |
|---|---|
| **EXECUTABLE ?** | Oui, sous réserve des corrections B1, B2, B3, B8. |
| **PRÉREQUIS COMPLETS ?** | **Oui.** T0 n'a aucune dépendance, T1 dépend de T0. Le seul candidat dont le graphe est cohérent tel qu'écrit. |
| **TESTE QUOI TECHNIQUEMENT ?** | Auth, isolation tenant, persistance, chaîne front/back, et surtout la discipline REAL/PROTOTYPE/MOCK d'Antigravity sur un cas où la tricherie est facile à détecter. |
| **TESTE QUOI PRODUIT ?** | Très peu. Un devis brouillon ne démontre aucune différenciation. `12` le dit honnêtement. |
| **RISQUE DE FAUSSE CONFIANCE ?** | **Élevé, et sous-estimé par `12`.** `12` ne mentionne que le risque de « fausse impression de rapidité ». Le risque réel est plus précis : T0 prouve l'isolation sur **une table factice**, et T1 déclare « RLS héritées de T0 ». Deux tranches vertes peuvent coexister avec des tables de production sans policy. C'est le candidat qui produit la plus forte impression de sécurité acquise. |
| **DÉCISION BLOQUANTE ?** | **Q1** (ligne libre, `BLOCKS_V1`). Exact tel que déclaré. |

### Candidat 2 — `T0 + T-PACK-CLIM + T8`

| Critère | Verdict |
|---|---|
| **EXECUTABLE ?** | **Non, tel que défini.** |
| **PRÉREQUIS COMPLETS ?** | **NON — candidat invalide.** T-PACK-CLIM déclare « DÉPENDANCES : **T1** » ; T8 déclare « DÉPENDANCES : **T1**, T-PACK-CLIM ». T1 est omis alors qu'il est le prérequis déclaré des deux tranches. T8 consiste par ailleurs à alimenter des lignes de **devis** — objet créé par T1. |
| **TESTE QUOI TECHNIQUEMENT ?** | Modèle `CORE_EXTENSIBLE` et résilience terrain — **si** T1 est réintégré. |
| **TESTE QUOI PRODUIT ?** | Le plus proche de la thèse PO, mais partiellement : sans la génération automatique (différée en T8-VOIX), ce qui est testé est un formulaire mobile typé, pas la thèse voix. |
| **RISQUE DE FAUSSE CONFIANCE ?** | **Élevé.** Risque de conclure « la thèse terrain fonctionne » à partir d'un formulaire de saisie structurée — ce que `12` §0.1 met justement en garde de ne pas faire pour l'abstraction CORE+PACKS. Aggravé par le fait que ce candidat inclut T-PACK-CLIM, tranche portant la contradiction `tenant_id` non résolue (B3). |
| **DÉCISION BLOQUANTE ?** | Déclaré : Q7, Q9. **Réel : Q1, Q7, Q9** — identique au candidat 3, plus T8. L'argument comparatif de `12` (« le candidat 1 n'a besoin que de Q1 ») repose sur cet oubli. |

### Candidat 3 — `T0 + T1 + T-PACK-CLIM`

| Critère | Verdict |
|---|---|
| **EXECUTABLE ?** | Oui, sous réserve des corrections B1, B2, B3, B8. |
| **PRÉREQUIS COMPLETS ?** | **Oui.** Graphe cohérent. |
| **TESTE QUOI TECHNIQUEMENT ?** | Tout du candidat 1, plus le mécanisme d'extension du catalogue par pack — donc la frontière `CORE_EXTENSIBLE`/`VERTICAL_DATA` en conditions réelles. C'est aussi le candidat qui **force** à résoudre B3 avant de coder, ce qui est un avantage, pas un coût. |
| **TESTE QUOI PRODUIT ?** | Partiellement — un devis avec du contenu métier réel. Pas la démonstration terrain. |
| **RISQUE DE FAUSSE CONFIANCE ?** | **Modéré.** Risque principal : conclure que « CORE+PACKS est validé » alors qu'un seul pack existe. `12` §0.1 et `02` §4 anticipent correctement ce piège (le second pack, fumisterie, est l'épreuve réelle). |
| **DÉCISION BLOQUANTE ?** | **Q1, Q7, Q9.** Exact tel que déclaré. |

**Observation transversale, sans recommandation.** Distinction demandée par la mission :
aucun des trois candidats n'est *réellement testable avec un artisan*. T0 ne teste qu'une
infrastructure ; T1 et T-PACK-CLIM sont démontrables mais ne ferment aucun cycle
utilisable en conditions réelles (un devis qu'on ne peut ni envoyer ni facturer) ; T8
seul serait testable terrain mais dépend de T1 et T-PACK-CLIM. **La première tranche
réellement testable avec un artisan est T2** (finaliser et envoyer un devis). C'est un
fait de séquence, pas un argument pour l'un des candidats — mais le PO doit le savoir
avant d'arbitrer, car aucun des trois candidats ne produira de retour terrain.

---

# H — ANTIGRAVITY / WINDOWS SAFETY CHECK

Vérification de la documentation officielle (`antigravity.google/docs/*`, `/changelog`,
`/terms`) au 23/09/2026. **Réserve de méthode :** la vérification a été faite par lecture
directe des pages officielles ; la recherche indexée tierce n'était pas disponible, donc
les rapports de bugs Windows de la communauté ne sont **pas** couverts. Cette réserve est
la même que celle que `14` §18 signale honnêtement pour lui-même.

| # | Mécanisme affirmé par `14` | Statut vérifié | Conséquence |
|---|---|---|---|
| H1 | **Project / périmètre de dossiers** (§1) | **CONFIRMÉ WINDOWS** — nom exact « Project », multi-dossiers, « directories and repositories the agent is allowed to access » | Correct. **Mais** un réglage Windows dédié existe, non mentionné par `14` : *« Outside of folder file access policy (Windows) »* (Always Allow / Ask / Deny). Le périmètre du Project **ne suffit pas** : ce réglage doit être mis à **Always Deny**. |
| H2 | **New Worktree Mode** (§2) | **CONFIRMÉ** (nom exact, verbatim officiel) / **Windows NON CONFIRMÉ** | Aucune doc sur symlinks, MAX_PATH, ou merge-back sous Windows. Deux correctifs au changelog (v1.1.26, v1.2.2) pour des worktrees orphelins sous `.system_generated/worktrees` — mécanisme récent et encore instable. |
| H3 | **Moteur de permissions unifié Deny/Ask/Allow + `settings.json`** (§3) | **NON CONFIRMÉ SUR WINDOWS — l'inverse est documenté** | Verbatim officiel, sur deux pages : « *Windows currently uses the permission system described in this section. It will be updated to the unified system described above in a future release.* » **Le `settings.json` de `14` §3 ne s'applique pas.** Erreur critique B5. |
| H4 | **« Sous Windows toutes les commandes sont Ask par défaut »** (§3) | **CONFIRMÉ WINDOWS** | Exact : preset Default = Terminal Auto Execution *Require Review*, accès hors dossier *Always Ask*. `14` a raison ici. |
| H5 | **« Le sandbox terminal est désactivé par défaut sous Windows »** (§3) | **CONFIRMÉ WINDOWS** | Verbatim : « **None of the presets turn the sandbox on.** » Activation manuelle → preset « Custom ». |
| H6 | **Sandbox Windows comme protection de `.env`** (§11) | **EXPÉRIMENTAL / CONTESTÉ — et nul par défaut** | `/docs/sandbox` : « Enable Sandbox Mode (**Preview**) ». `/docs/cli/features` : AppContainer, sans réserve. `/changelog` **v2.15.1 (19/09/2026)** : « *File and network sandboxing on Windows are now supported.* » Trois sources, trois statuts. Et comme aucun preset ne l'active, la protection `.env` est **absente par défaut**. Erreur critique B6. |
| H7 | **Presets : seul Turbo est interdit** (§3) | **INCOMPLET — risque non couvert** | Sur Windows il existe **trois** presets, et **« Full machine »** met l'accès hors dossier sur **Allow** tout en gardant *Require Review* sur les commandes. Un utilisateur cherchant du confort le choisira. `14` ne l'interdit pas. |
| H8 | **Rules `.agents/rules/`, 12 000 caractères, always-on** (§4) | **CONFIRMÉ** (chemins et limite exacts) mais **CONSULTATIF** | Global = `~/.gemini/GEMINI.md`, workspace = `.agents/rules/`, rétro-compat `.agent/rules` : tout exact. **Mais** les docs n'emploient que « guide » / « consulted » — aucune page ne prétend qu'une Rule bloque. `AGENTS.md` n'est **pas** un nom officiellement documenté (c'est `GEMINI.md`). Erreur critique B7. Chemins écrits en Unix (`~/.gemini/`) sans équivalent Windows documenté. |
| H9 | **Skills `.agents/skills/<nom>/SKILL.md` ; Workflows dépréciés au 01/11/2026** (§5) | **CONFIRMÉ** | Exact, y compris la date verbatim : « *Workflows are deprecated and will be retired on November 1, 2026.* » `14` a raison de construire sur les Skills. Consultatives comme les Rules. |
| H10 | **Hooks : 5 événements, `PreToolUse` bloquant** (§6) | **CONFIRMÉ (mécanisme)** / **NON CONFIRMÉ SUR WINDOWS (exécution)** | Les cinq événements, `.agents/hooks.json`, et les décisions `allow`/`deny`/`ask`/`force_ask`/`deny_unless_prior_grant` sont exacts. C'est bien le seul levier programmatique réel. **Mais la page hooks ne mentionne ni Windows, ni PowerShell, ni `.bat`/`.ps1`, ni quel interpréteur exécute `command` ; les seuls exemples sont des `.sh`.** Les trois hooks de `14` §6 portent la part enforçante du dispositif et ne sont pas vérifiables sur doc. Erreur majeure C10. |
| H11 | **Implementation Plan + revue humaine** (§7) | **CONFIRMÉ** mais **désactivable** | L'artefact existe, la revue est réelle (bouton « Proceed », commentaires inline). Elle obéit à une *artifact review policy* qui peut valoir « Always Proceed ». Garantie conditionnelle à un réglage. |
| H12 | **« Planning Mode = Request Review »** (§7) | **CONFUSION DE NOMS** | « Request Review » est un **preset de permissions** (macOS/Linux) et une valeur de *Terminal Command Auto Execution* (Windows). Le mode plan du CLI s'appelle `plan` (`Shift+Tab`). Erreur majeure C12. Note : `/planning` et `/fast` ont été **supprimés en 1.1.0**. |
| H13 | **Browser Subagent, profil Chrome séparé, denylist serveur fail-closed** (§8) | **CONFIRMÉ**, plateforme non précisée | Tout exact, y compris « *If the server is unavailable, access is denied by default* ». Aucune mention Windows. Aucune intégration « extension Chrome » trouvée dans la doc actuelle. |
| H14 | **MCP `.agents/mcp_config.json`** (§10) | **CONFIRMÉ** / **Windows NON DOCUMENTÉ** | Chemin exact, trois transports (stdio, Streamable HTTP, SSE), MCP en `Ask` par défaut. **Zéro guidance Windows** : pas de `cmd /c`, pas de `npx.cmd`, pas d'échappement, pas d'équivalent `%APPDATA%` pour `~/.gemini/`. C'est le mode d'échec MCP classique sous Windows, et la doc n'aide pas. |
| H15 | **Artifacts + Walkthrough** (§14) | **CONFIRMÉ** | Existent, incluent captures et enregistrements navigateur (WebM). **Emplacement de stockage sur disque non documenté** — point important pour la reprise (voir I). |
| H16 | **Teamwork `/teamwork-preview`, rôles Critic/Challenger/Auditor** (§15) | **NON CONFIRMÉ / NOT_FOUND** | Introuvable dans la documentation officielle actuelle. `/docs/subagents` documente **trois** subagents intégrés : Research, Browser, Self. La lecture croisée de transcripts entre subagents n'est pas documentée non plus. `14` signale le statut `-preview`, ce qui est prudent, mais l'étape `AUDIT INDÉPENDANT` en dépend. Erreur majeure C10. |
| H17 | **Secrets applicatifs : zone d'ombre documentaire** (§11) | **CONFIRMÉ — le constat de `14` est exact** | Aucune page dédiée aux secrets applicatifs. Aucune redaction de secrets documentée. Aucune durée de rétention publiée. `14` a raison de ne rien présumer. |
| H18 | **Données envoyées à Google / revue humaine** (non traité par `14`) | **CONFIRMÉ — lacune de `14`** | `/terms` verbatim : « *Google employees and contractors may access, view, review and use Interactions.* » Opt-out télémétrie disponible ; offre Enterprise matériellement différente, mais « *Antigravity IDE is not supported for enterprise customers* ». Erreur majeure C11. |
| H19 | **Retour d'expérience « sharp-kepler »** (§18) | **NON TROUVÉ — et `14` le dit** | `14` §18 refuse explicitement de combler ce vide par une supposition. C'est la bonne posture et il faut la porter au crédit du document. |
| H20 | **Mode WSL** (absent de `14`) | **CONFIRMÉ — opportunité manquée** | `/changelog` **v2.16.0, 22/09/2026** — la veille de la rédaction de `14` : « *Added a Windows Subsystem for Linux (WSL) section to Application Settings on Windows, so you can connect to an installed WSL distribution.* » C'est le levier le plus direct pour récupérer le moteur de permissions unifié et le sandbox GA. Voir B5. |

**Synthèse H.** `14` est honnête là où il ne sait pas (§11, §18) et exact sur la majorité
des noms et des chemins — c'est un document sérieux. Mais **la sécurité critique du
projet repose sur trois mécanismes dont aucun n'est confirmé sur Windows** : le moteur de
permissions unifié (H3, documenté comme *non applicable*), le sandbox (H6, contesté et
désactivé par défaut), et l'exécution des hooks (H10, sémantique Windows absente de la
documentation). Conformément au cadrage de la mission, cela constitue une **erreur
majeure à critique selon l'impact** — retenue ici en critique (B5, B6) parce que ces
trois mécanismes portent, ensemble, les six premières règles minimales du PO.

---

# I — RECOVERABILITY

**Question posée : si Antigravity s'arrête définitivement après n'importe quelle tranche,
Claude Code ou un développeur humain peut-il reprendre sans reconstruire mentalement ce
qui a été fait ?**

## Réponse : non, en l'état.

Le seul artefact de fin de tranche exigé par le blueprint est le **Walkthrough**
d'Antigravity (`14` §14). C'est un artefact **propriétaire, interne au produit, dont la
documentation officielle ne précise même pas l'emplacement sur disque**. Si Antigravity
disparaît, le raisonnement de chaque tranche disparaît avec lui. Le code resterait ; le
*pourquoi* ne resterait pas.

Trois aggravants propres à ce projet :

1. **Le blueprint vit dans un autre dépôt que le code, et l'agent a interdiction d'y
   accéder.** `14` §1 impose de **copier** les documents pertinents dans le dépôt
   applicatif (`docs/blueprint-reference/`). Aucune règle de synchronisation, de
   versionnage ni de datation de ces copies n'est définie. Les copies divergeront
   silencieusement de `supordo-os`, et rien ne permettra de savoir quelle version d'un
   document a effectivement cadré quelle tranche.
2. **Le blueprint lui-même n'est pas committé** (C13). L'état durable du projet n'existe
   aujourd'hui que sur un disque.
3. **Aucune obligation de migration versionnée** n'est posée (F10). Sans historique de
   migrations ordonné dans le dépôt, le schéma effectif n'est reconstructible que depuis
   la base elle-même.

## Artefacts à produire tranche par tranche, dans le dépôt applicatif

À inscrire comme condition de DoD de **chaque** tranche, en Markdown versionné dans le
dépôt — jamais uniquement dans un artefact Antigravity :

| Artefact | Pourquoi il est irremplaçable |
|---|---|
| Ce qui a été construit, et **pourquoi** | Le code dit le quoi, jamais le pourquoi. |
| Architecture réellement retenue (pas celle planifiée) | `14` §17 interdit à juste titre de confondre le Plan et la réalisation. |
| **Migrations versionnées et ordonnées** | Seul moyen de reconstruire le schéma sans la base. |
| **Schéma effectif** en fin de tranche (dump) | Permet de détecter une dérive entre migrations et réalité. |
| **Politiques RLS effectives** (dump depuis la base, pas le code) | Exigé par `13` §T0 pour T0 ; à généraliser (voir B2). C'est la preuve de sécurité la moins falsifiable. |
| Interfaces externes posées, et leur statut de branchement | Évite qu'un successeur croie une intégration active. |
| **Décisions prises pendant la tranche**, y compris les micro-arbitrages non prévus | C'est ce qui disparaît le plus vite et coûte le plus cher à reconstituer. |
| Questions `OPEN` touchées, et la réponse appliquée si une a été tranchée | Contrôle direct contre l'arbitrage silencieux (`14` §17). |
| Tests écrits **et résultats d'exécution** (pas seulement les fichiers de test) | `13` exige une preuve exécutée ; elle doit survivre à la session. |
| Statut par capacité : `REAL` / `PROTOTYPE` / `MOCK` / `NOT_IMPLEMENTED` | Déjà exigé par `14` §14 — à déplacer du Walkthrough vers le dépôt. |
| Limitations connues et **dette acceptée**, datée | Sans cela une dette devient un comportement supposé intentionnel. |
| Prochaine tranche prévue et ses prérequis | Permet une reprise à froid sans relire toute la séquence. |
| **Version exacte des documents de blueprint** ayant cadré la tranche (hash ou date) | Résout l'aggravant n°1 : sans cela, on ne saura pas sur quelle version on a construit. |

**Classement :** en l'absence de ces artefacts, le projet présente un **risque de
maintenabilité et de dépendance fournisseur élevé**. Il n'est pas critique au sens de la
section B — il ne produit ni fuite ni corruption — mais il est le seul risque de cette
liste dont le coût augmente à chaque tranche livrée sans être détecté, et il contredit
directement la doctrine du dépôt (`CLAUDE.md` : « Git = état durable, session = contexte
jetable »).

---

# J — SUPERSESSION MAP

Le dossier contient délibérément des documents anciens corrigés par des documents plus
récents, sans réécriture rétroactive. Le tableau suivant établit la précédence.

| Sujet | Ancienne source | Ancienne conclusion | Source corrective | Conclusion à utiliser | Impact si Antigravity lit la mauvaise version |
|---|---|---|---|---|---|
| **Fumisterie : niveau de preuve** | `README`, `01` §5, `02`, `07` §0 | Aucune preuve en centre d'aide ; `MARKETING_ONLY` seul | **`10` §0.1** | Preuve fonctionnelle réelle à **1 témoin** (OpenFire Odoo) ; écart 2 vs 1, pas 2 vs 0 | Q7 (`BLOCKS_V1`) arbitrée sur une asymétrie surévaluée, contre l'exemple cité en premier par le PO |
| **Verrou de mutabilité du devis** | `09` Q3 | « Verrouiller à la première sortie structurante (M10) » | **`12` §0.5** | M10 = changement d'**état** ; O3 = verrou de **contenu**. Deux événements distincts. Verrou à l'engagement (T3), pas à l'envoi (T2) | Devis verrouillé dès l'envoi — contredit M5 (3 éditeurs) et casse le cycle commercial normal |
| **Justification de la transformation directe** | `09` Q4 | « Cohérente avec **l'absence de preuve d'un pivot** » | **`12` §0.6** (corrigé par le présent audit : la source est **V0 §11**, pas §17) | Le pivot **est** documenté (3/8). Justification réelle : pluralité relative 4/8 + modèle le plus direct pour un solo + n'impose pas d'objet « commande » | Décision `STRUCTURAL_BEFORE_SCHEMA` prise sur un fait faux ; le PO croit trancher entre une option et un vide |
| **Classement CORE des services techniques** | `02` §2 | Auth, RLS, multi-tenant, transcription vocale = `CORE`, au rang de Client/Devis | **`12` §0.2** | `PLATFORM_CAPABILITY` — service technique transversal, distinct de l'objet métier | Un connecteur fournisseur modélisé comme objet métier ; couplage du modèle Devis à un prestataire de signature |
| **Chantier et Intervention** | `02` §2, `03` §1 | Une seule fiche/ligne fusionnée | **`12` §0.3** | Deux objets distincts ; **Q18** ouverte, `STRUCTURAL_BEFORE_SCHEMA` | Fusion de deux objets encore `OPEN` en une table ; T6 construirait un objet hybride impossible à séparer ensuite |
| **Rôles/permissions : niveau de preuve** | `09` Q11 | « Preuve faible (5/10), jamais détaillée » | **`10` §0.2** | Obat documente 7 rôles + permissions individuelles. Rôles minimaux restent défendables en V1, mais **plus** par absence de preuve | Justification fausse conservée ; risque de sous-dimensionner le **modèle** (pas seulement l'UI) — cf. `11` P12 |
| **Devis vocal : niveau de preuve** | `05` (préambule) | 2 précédents fonctionnels + 2 revendications `MARKETING_ONLY` | **`10` §0.3** | **3 témoins `ACQUIS DOCUMENTAIRE`** (InterFast, OpenFire Zendesk, **Obat**), dont un portant spécifiquement sur la **voix** | Thèse centrale du PO sous-évaluée au moment d'arbitrer le périmètre IA du V1 (cf. C7) |
| **Périmètre IA du V1** | `05` §10, `07` §1 | Transcription vocale libre (#4) + pilote devis vocal simple **en V1** | **`12` §0.4 / T8, `13` §T8** | Aucune IA en V1 ; tout en `T8-VOIX` (V2) | Contradiction directe non résolue. L'agent construira ou omettra l'IA selon le fichier lu en premier. #4 n'est ni construit ni différé explicitement |
| **Irréversibilité : niveaux couverts** | `08` §7, `09` | Niveau **document** (facture numérotée, avoir finalisé) | **`10` §0.5**, `11` P7 | Troisième niveau : bascule irréversible au niveau **compte entier** (mode conforme, migration PDP) | Une bascule irréversible présentée comme un réglage ordinaire |
| **Complexité du relevé terrain** | `01` §7 | `FORTE` en bloc | **`12` §0.9** | `FAIBLE-MOYENNE` pour le niveau 1 ; `FORTE` pour les niveaux 2-4 | T8 différé à tort comme « complexe », ou sur-construit d'emblée |
| **Devis : une tranche ou deux ?** | `07` §1 | « Devis (naissance + **un modèle de verrouillage**) » — une ligne | **`12` §0.9** | Deux tranches distinctes : changement d'état (T1/T2), verrou (T3) | Une seule tranche mélangeant deux décisions dont une reste `OPEN` |
| **L4 / facture importée** | `0007` L4 | Interdiction ProGBat = « choix éditeur, rien n'établit une interdiction générale » | **`10` §0.4** | Tension non résolue : ProGBat invoque une base légale (« loi de finance 2016 ») non vérifiable. **Ne pas trancher.** Statut `SUPORDO_DECISION` de L4 inchangé (il porte sur ce que fait SUPORDO) | Import d'historique construit en V2 sur une lecture légale non vérifiée |
| **Registre des questions ouvertes** | `09` Partie A | 17 questions (Q1-Q17) | **`12` §0.3 et §0.7** | **19 questions** — Q18 (`STRUCTURAL_BEFORE_SCHEMA`) et Q19 (`CAN_WAIT_V2`) | Les templates de `09` Partie C renvoient l'agent au registre de `09` : **Q18 est invisible au protocole** |
| **Carte des documents** | `README` | 9 documents (`01`-`09`) | **existence de `10`-`14`** | 15 documents | La porte d'entrée du dossier dirige vers la version périmée du corpus |
| **Terminologie facturation électronique** | `06` §2, `07`, `08` §14, `09` Q13, `12` T4 | « PDP » (Plateforme de Dématérialisation Partenaire) | **`06-ANNEXE` §9.2** | Décret n° 2026-677 : notion unique de **« plateforme agréée » (PA)** | Interface nommée d'après un statut juridique supprimé |

## Un `CANONICAL EXECUTION INDEX` est-il nécessaire ?

**Oui. Obligatoire avant de donner le corpus à Antigravity.**

Quinze conclusions sont superseded, réparties sur cinq documents correcteurs, sans
qu'aucun document ancien ne porte de marque de péremption. Trois circonstances rendent
la situation non gérable par la seule lecture :

1. **Le `README` — seul point d'entrée — ne mentionne pas l'existence de `10`-`14`.** Un
   lecteur diligent qui suit la carte des documents ne verra aucune correction.
2. **`14` §1 impose de copier les documents dans le dépôt applicatif**, sélectivement,
   tranche par tranche. Un agent recevra donc des **sous-ensembles** du corpus. Copier
   `09` sans `12` — plausible pour une tranche devis — transmet Q3 et Q4 dans leur
   version fausse, dont l'une est `STRUCTURAL_BEFORE_SCHEMA`.
3. **Les corrections sont enfouies dans des sections `§0`** de documents dont le titre
   annonce autre chose (`10` est un « atlas de frictions », `12` une « séquence de
   build »). Rien n'indique de l'extérieur qu'ils contiennent des corrections.

Un index canonique doit, au minimum : établir l'ordre de précédence document par
document ; lister les 15 conclusions superseded avec leur version à utiliser ; fusionner
Q1-Q19 en un registre unique ; et **interdire la transmission d'un document `00-09` à un
agent sans l'index**. C'est la condition `GO-01` ci-dessous, et la moins coûteuse de
toutes — elle n'exige aucune décision produit.

---

# K — CONDITIONS DE GO

Liste **fermée**. Conditions nécessaires avant le **premier prompt Antigravity
`IMPLEMENT`**. Chaque condition est binaire. Les améliorations souhaitables des sections
D et E n'y figurent pas.

| # | Condition | Binaire | Statut |
|---|---|---|---|
| **GO-01** | Un `CANONICAL EXECUTION INDEX` existe, couvre les 15 supersessions de la section J, fusionne Q1-Q19 en un registre unique, et aucun document `00-09` ne peut être transmis à un agent sans lui. | Existe / n'existe pas | **NON SATISFAITE** |
| **GO-02** | Lieu (S1) est posé dans la tranche qui crée le Client, avec sa cardinalité et le rattachement des objets d'exécution, et un test `13` le vérifie. | Posé et testé / non | **NON SATISFAITE** |
| **GO-03** | La mention « RLS : inchangé / héritées » est supprimée de `12` et remplacée par l'obligation *toute table nouvelle active RLS et définit sa policy tenant dans la même migration* ; un test `CROSS-TENANT` lecture **et** écriture existe dans chaque section de `13` à partir de §T2, plus un test d'isolation Storage en §T8. | Tous présents / non | **NON SATISFAITE** |
| **GO-04** | La frontière Catalogue est tranchée en deux objets (`referentiel_produit` partagé en lecture seule / `article_catalogue` privé à `tenant_id` obligatoire), la contradiction `08` §1 vs `12` §0.8 est levée, et le test `13` §T-PACK-CLIM est un test dur, pas conditionnel à une décision non prise. | Tranchée / non | **NON SATISFAITE** |
| **GO-05** | Le portail client est explicitement exclu du V1, **ou** défini comme tranche nommée avec ses tests de jeton (entropie, expiration, révocation, scope) et ses deux tests négatifs obligatoires (autre devis, autre tenant). | Exclu ou défini+testé / ni l'un ni l'autre | **NON SATISFAITE** |
| **GO-06** | Un test `13` §T1 vérifie S3 : modifier un prix catalogue laisse inchangée une ligne de devis déjà créée. Étendu à la Facture en §T4. | Existe / n'existe pas | **NON SATISFAITE** |
| **GO-07** | Le test de numérotation séquentielle sous concurrence porte sur la **Facture** (`13` §T4), la séquence est garantie au niveau base, et le statut du numéro de devis est un choix produit assumé — jamais présenté comme une conséquence de L3. | Fait / non | **NON SATISFAITE** |
| **GO-08** | Le modèle de permissions Antigravity est configuré et **vérifié empiriquement sur la machine Windows réelle** — soit via WSL (chemin de code Linux, moteur unifié + sandbox GA), soit en vocabulaire Windows natif avec *Agent Non-Workspace File Access = Always Deny* et interdiction explicite des presets « Full machine » **et** « Turbo ». `14` §3 est réécrit en conséquence. | Vérifié sur la machine / non | **NON SATISFAITE** |
| **GO-09** | Un hook `PreToolUse` trivial a été **exécuté avec succès sur la machine Windows réelle** et son blocage constaté. Si les hooks ne s'exécutent pas, le dispositif de sécurité est repensé avant T0. | Exécuté et constaté / non | **NON SATISFAITE** |
| **GO-10** | Le sandbox est soit activé et vérifié sur la machine, soit déclaré inactif — et dans ce cas aucun secret réel ne se trouve dans le périmètre de lecture du Project. Deux tests secrets existent dans `13` §T0. | Fait / non | **NON SATISFAITE** |
| **GO-11** | Le tableau `14` §17 distingue **ENFORCÉ** et **CONSULTATIF**, et chaque règle PO aujourd'hui consultative à échec coûteux est soit adossée à un contrôle réel, soit explicitement assumée comme garantie humaine. | Fait / non | **NON SATISFAITE** |
| **GO-12** | Les questions `BLOCKS_V1` / `BLOCKS_A_SLICE` / `STRUCTURAL_BEFORE_SCHEMA` de la tranche choisie sont tranchées par le PO — au minimum **Q1**, plus **Q7 et Q9** si la tranche inclut `T-PACK-CLIM`. Q7 est soumise **après** correction de son libellé par `10` §0.1. | Tranchées / non | **NON SATISFAITE** |
| **GO-13** | Le sort de l'**Avoir**, du **Planning** et de la **transcription vocale libre (#4)** est explicite : construit en V1, ou inscrit en dette datée dans `12` §3. Aucun des trois ne reste omis. | Explicite pour les trois / non | **NON SATISFAITE** |
| **GO-14** | Le périmètre du candidat de première tranche retenu est cohérent avec les dépendances déclarées ; si le candidat 2 est retenu, son périmètre inclut T1 et sa liste de décisions bloquantes inclut Q1. | Cohérent / non | **NON SATISFAITE** |
| **GO-15** | Le format de **dossier de tranche versionné dans le dépôt applicatif** est défini (12 artefacts de la section I, dont migrations versionnées, dump RLS effectif, résultats de tests, décisions, dette, et version des documents de blueprint ayant cadré la tranche), et la règle de copie/versionnage du blueprint depuis `supordo-os` est écrite. | Défini / non | **NON SATISFAITE** |
| **GO-16** | Une position de gouvernance des données est prise (télémétrie, Enterprise, ou données de développement synthétiques uniquement) avant tout accès MCP à une base contenant des données réelles. | Prise / non | **NON SATISFAITE** |
| **GO-17** | Le dossier `docs/product-blueprint-antigravity/` est committé et enregistré dans `01-discovery/ARBORESCENCE.md` ; la carte des documents du `README` couvre `01` à `15`. | Fait / non | **NON SATISFAITE** |

**17 conditions, 0 satisfaite.**

Trois d'entre elles n'exigent **aucune décision produit** et peuvent être levées
immédiatement : **GO-01** (index canonique), **GO-15** (format de dossier de tranche),
**GO-17** (commit et carte). Trois autres — **GO-08**, **GO-09**, **GO-10** — n'exigent
pas non plus de décision produit mais **une vérification empirique sur la machine
Windows**, qu'aucune lecture de documentation ne peut remplacer.

---

## Ce que cet audit ne fait pas

- Il ne choisit **aucun** candidat de première tranche — c'est la décision du PO (G).
- Il ne tranche **aucune** question `OPEN`, et n'en propose pas de nouvelle là où la
  preuve manque (D).
- Il ne refait pas le benchmark concurrentiel et ne conteste aucun fait du corpus
  au-delà des vérifications de citation explicitement rapportées (C6).
- Il n'a modifié **aucun** fichier existant. Seul ce document a été créé. Aucun code,
  aucune table, aucune migration, aucun projet Supabase, aucune configuration
  Antigravity, aucun commit, aucun push.
- Sa vérification Antigravity porte sur la documentation officielle au 23/09/2026 par
  lecture directe ; la recherche indexée tierce n'était pas disponible, donc les
  rapports de bugs Windows de la communauté ne sont pas couverts. Trois points (H6,
  H10, H14) ne sont **pas résolubles par documentation** et exigent un test sur la
  machine réelle — c'est l'objet de GO-08, GO-09 et GO-10.
