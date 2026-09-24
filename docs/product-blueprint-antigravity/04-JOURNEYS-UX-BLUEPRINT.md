# 04 — Journeys & UX Blueprint

Parcours métier de bout en bout et architecture de l'information. Pas un design
pixel-perfect — une carte de ce que chaque zone doit permettre de faire, et avec
quelle donnée disponible.

Sources : `functional-onboarding-pilot.md`, `functional-propagation-pilot.md`,
`functional-devis-3c-sorties.md` (parcours 2 en particulier), contrat V0, `03`.

## 1. Neuf parcours, classés par niveau de preuve

### Bien documentés (ferment un cycle complet, preuve croisée multi-éditeurs)

**Parcours A — Devis → acceptation → chantier/intervention.** Acteurs : client
signataire, artisan/équipe. Chantier central chez Vertuoza/InterFast/Obat/Costructor
(`ACQUIS DOCUMENTAIRE`), **absence confirmée** (pas un silence) chez Axonaut/Sellsy.
Intervention : InterFast documente le sens attendu (devis accepté → planifier une
intervention, données copiées, un devis → plusieurs interventions) ; Costructor
documente une boucle bidirectionnelle franche ; **OpenFire documente le sens
inverse** (intervention/étude → devis) — `OPEN`, question renvoyée au terrain (`03`
§4.4). Vertuoza bifurque vers chantier OU intervention selon un critère non
documenté. Friction connue : chez InterFast, le client associé au chantier devient
irréversible une fois créé.

**Parcours B — Chantier → achats/temps → facture → paiement.** Chantier = hub de
recalcul (jamais de saisie directe), convergent sur 3 éditeurs indépendants (`03`
§4, INV-4). Acompte/situation/solde = **le motif le plus convergent du corpus après
la création client à la volée** — 8/8 corpus, déduction automatique jamais ressaisie
(3C, INV-3C-1). Frictions documentées : blocage mutuel facture finale/facture de
situation déjà engagée (Obat) ; incompatibilité acompte + factures partielles
multiples (Sellsy) ; **retenue de garantie non héritée dans le chantier chez
Vertuoza** — anomalie confirmée, contournement officiel documenté (ligne poste
libre à montant négatif).

### Partiellement documentés (fragments solides, non généralisables)

**Parcours C — Demande entrante → client → devis → suite.** Solide sur
client/devis (client créable à la volée 8/8, aucune affaire requise en amont 8/8) ;
**trou total sur la capture de la demande elle-même** (canal, lead, qualification
initiale) — angle mort complet du corpus fonctionnel disponible à ce jour.

**Parcours D — Qualification → estimation → visite technique → devis final.** Deux
cas forts sur huit :
- **InterFast** — objet « Visite avant devis » dédié (intervention typée, rapport
  mobile structuré : métrés, photos annotées, croquis) → bouton générant un
  **brouillon de devis lié**. Pas de devis estimatif distinct du définitif, pas de
  transfert automatique des métrés vers les lignes (ajout manuel).
- **OpenFire Zendesk** — preuve la plus forte : module « Vital Études » (mobile,
  rattaché à une intervention type « Dimensionnement »), formulaire structuré →
  **« votre devis est automatiquement généré avec les produits adaptés »**
  (génération automatique de lignes, pas un simple stockage). Verticale spécifique
  (ventilation/ITE), pas générique.
- Obat amorce la même idée (champ « date de visite préalable », module Métrés
  « bientôt disponible ») sans l'aboutir. Vertuoza, Axonaut, Sellsy, Costructor,
  OpenFire Odoo : `NON DÉTERMINÉ`.
- **Aucune séquence à 7 étapes** (demande→proposition→visite→étude→devis
  définitif→docs techniques→engagement) n'existe chez un seul éditeur du corpus.

**Parcours I — Petite équipe.** Vertuoza impose un ordre explicite personnel →
compte utilisateur ; Costructor documente une délégation comptable explicite ;
feuilles d'heures validées puis verrouillées chez InterFast, avec remontée
automatique sur la rentabilité chez Costructor. Jamais un parcours complet et
nommé — des fragments de coordination, pas un flux.

### Quasi absents du corpus (1 éditeur ou fragments isolés)

**Parcours E — Client existant → SAV → intervention → facturation.** Un seul
fragment : InterFast restreint la liaison devis↔intervention **existante** au
SAV/maintenance — confirme la notion, sans documenter le déclenchement ni le cycle.

**Parcours F — Équipement installé → maintenance → relance → intervention.**
Couverture exclusive à OpenFire Odoo (cascade Contrat → Ligne de contrat → Demande
d'intervention → RDV), **aucune corroboration croisée chez les 6 autres éditeurs**
du pilote propagation. Mode exact de reprise à chaque niveau `NON DÉTERMINÉ`.

**Parcours G — Terrain par voix/photo.** Quasi absent, confirmé par une recherche
dédiée (3C §10bis). InterFast documente photos+croquis dans son rapport de visite ;
Obat qualifie explicitement son assistant vocal d'« accélérateur de saisie », pas
d'outil de relevé. Aucune extraction structurée voix→données documentée nulle part.

**Parcours H — Solo (artisan seul).** Jamais documenté comme parcours nommé.
Indices indirects seulement : ProGBat prévoit explicitement un usage mono-
utilisateur (rôles par défaut gratuits) — preuve que le cas est **prévu**, pas qu'il
bénéficie d'un **parcours optimisé**.

## 2. Ce que ce classement signifie pour SUPORDO

Les deux parcours les plus riches (A, B) couvrent la chaîne déjà instruite par le
contrat fonctionnel devis. Les quatre parcours les plus pauvres (E, F, G, H)
couvrent précisément les zones que la doctrine du dépôt identifie comme les plus
différenciantes pour SUPORDO — confirmation croisée, sur l'axe parcours plutôt que
sur l'axe objet, du même constat que `02` et `03`. **Ne pas chercher à combler ces
trous par une lecture corpus supplémentaire** — ce sont des candidats `À TESTER
TERRAIN` ou de conception produit propre.

## 3. Architecture de l'information par zone fonctionnelle

Modèle : Contexte utilisateur → Intention → Information nécessaire → Action →
Résultat → Prochaine action.

### Zone Client / Lieu

- **Contexte** : au bureau ou en mobilité, souvent en train de créer autre chose (un devis).
- **Intention** : retrouver ou créer un client sans interrompre le flux en cours.
- **Information prioritaire** : nom, coordonnées, lieu(x) rattaché(s), historique d'intervention par lieu (S1).
- **Action primaire** : créer/sélectionner à la volée (`MARKET_BASELINE`, 8/8).
- **Actions secondaires** : rattacher un second lieu, voir l'historique complet.
- **États vides** : premier client de l'entreprise — ne doit jamais bloquer la création d'un devis.
- **Contraintes terrain** : saisie minimale au clavier en mobilité — priorité à la recherche par nom/téléphone.
- **Opportunité voix/photo** : capture vocale des coordonnées en fin de RDV (`05`).

### Zone Devis — naissance

- **Contexte** : au bureau après une demande, ou sur le terrain après une visite (parcours D).
- **Intention** : produire un document chiffré exploitable rapidement, avec le contenu de la visite si elle a eu lieu.
- **Information prioritaire** : client/lieu, lignes issues du catalogue ou de la visite, total.
- **Action primaire** : ajouter une ligne (catalogue, ligne libre — `OPEN` O1, ou ligne générée depuis un relevé).
- **Résultat** : devis en état initial exploitable — **l'état "brouillon" lui-même n'est pas un acquis de marché stable** (2/8 seulement), à ne pas présenter comme une garantie univoque à l'utilisateur.
- **Élément à ne jamais afficher comme acquis** : mécanisme de "conversion automatique du relevé en lignes" tant qu'il n'est pas réellement implémenté (cf. `09` §C, discipline REAL/PROTOTYPE/MOCK).

### Zone Visite / Relevé terrain (candidate différenciante, `À TESTER TERRAIN`)

- **Contexte** : sur site, mobile, potentiellement mains occupées, connexion incertaine.
- **Intention** : capturer suffisamment d'information structurée pour ne pas avoir à revenir sur site.
- **Information nécessaire** : dépend du pack métier (`02`) — schéma de relevé injecté, pas généraliste.
- **Action primaire** : dicter/photographier/remplir un formulaire court typé par métier.
- **Résultat** : rapport structuré rattaché au lieu/client, capable de préremplir un devis (preuve InterFast/OpenFire Zendesk).
- **États d'erreur** : perte de connexion en cours de capture — la capture ne doit jamais être perdue (contrainte terrain, pas une preuve de corpus).
- **Ce que l'interface ne doit pas prétendre** : qu'une donnée dictée est déjà structurée avant validation humaine (S4 — provenance, et discipline `09` §C).

### Zone Chantier / Intervention (objet le moins bien outillé par le corpus, `03` §1)

- **Contexte** : suivi dans la durée, plusieurs intervenants possibles.
- **Intention** : voir où en est un chantier sans recalculer à la main.
- **Information prioritaire** : rentabilité **recalculée**, jamais un champ de saisie manuelle (invariant `03` §4).
- **Action primaire** : rattacher une dépense/un temps/une intervention.
- **Trou documentaire à assumer explicitement dans l'UX** : le critère de bifurcation devis→chantier vs devis→intervention n'est tranché par aucune source — l'interface devra proposer un choix explicite plutôt que de deviner une règle qui n'existe pas dans le marché.

### Zone Facturation

- **Contexte** : souvent au bureau, geste engageant (irréversibilité légale).
- **Intention** : émettre sans erreur, corriger sans jamais réécrire.
- **Information prioritaire** : statut (brouillon vs numérotée), acompte/solde déjà déduits (jamais ressaisis).
- **Action primaire** : numéroter/émettre — geste à confirmer explicitement (irréversible, L1).
- **Action de correction** : toujours un avoir, jamais une édition de la facture émise.
- **État d'erreur** : ne jamais permettre visuellement une modification d'une facture numérotée, même en apparence mineure.

### Zone Planning

- **Contexte** : vue d'ensemble (bureau) et vue du jour (terrain).
- **Information prioritaire** : RDV/intervention du jour, lieu, contexte (devis lié, visite à faire).
- **Contrainte terrain** : doit rester utilisable en connexion dégradée pour la vue du jour au minimum.

## 4. Contraintes mobile/terrain transversales

- Connexion intermittente sur chantier — aucune capture (photo, note, dictée) ne doit dépendre d'une connexion continue pour être conservée localement en attente de synchronisation. C'est une exigence de conception, pas une observation du corpus (`À TESTER TERRAIN`).
- Mains occupées / gants — la voix et la photo priment sur la saisie clavier dans les zones terrain (cohérent avec la direction PO §2).
- Écran réduit — les zones Devis et Facturation doivent rester utilisables sur mobile sans devenir le mode de saisie principal pour les documents complexes (aucune preuve marché sur ce point — jugement de conception).
- Aucune fonctionnalité affichée à l'écran (badge "conforme", "signé", "synchronisé", "IA") ne doit apparaître si le mécanisme réel n'est pas implémenté — voir `09` §C pour la discipline REAL/PROTOTYPE/MOCK/NOT_IMPLEMENTED à appliquer à chaque zone ci-dessus lors de la construction avec Antigravity.

## 5. Limites de ce document

Ce document reconstruit des parcours à partir de ce que le corpus documente — il ne
mesure ni l'usage réel, ni la préférence d'un utilisateur SUPORDO, ni le temps
d'exécution d'un parcours (0004 : la documentation est une source éditoriale, pas
une donnée d'usage). Les zones "Visite/Relevé terrain" et "Chantier/Intervention"
sont les plus fragiles en preuve et les plus centrales à la thèse produit — elles
doivent être validées par du test terrain avant d'être considérées stables.
