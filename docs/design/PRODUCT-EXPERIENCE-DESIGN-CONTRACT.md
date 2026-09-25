# Product Experience Design Contract

`STATUS = CANONICAL_PRODUCT_EXPERIENCE_CONTRACT`

Contrainte transversale, **pas une couche canonique numérotée** de
`16`→`20` (`docs/product-blueprint-antigravity/`). Ce document ne
remplace, ne supersède, ne modifie et ne réinterprète ni
`docs/brand/BRAND-FOUNDATIONS.md` ni
`docs/product-blueprint-antigravity/20-APPLICATION-UX-ARCHITECTURE-
CONTRACT.md`. Il traduit leurs principes en **langage d'interaction, de
composition et d'exécution visuelle** — la couche intermédiaire dont
l'absence a été constatée par l'audit documentaire du 2026-09-25 (aucun
document ne couvrait l'espace entre l'identité de marque, l'architecture
des parcours, et le code réel).

**Ce document n'est pas un design system de tokens.** Un design system
de tokens répond à "quelles valeurs utiliser". Ce document répond à
"comment SUPORDO doit-il se comporter, bouger et se formuler pour être
reconnaissable et éviter l'effet CRM générique produit par un outil
d'IA" — les tokens (§6) sont un moyen, pas la finalité de ce contrat.

## Relation avec le reste du corpus

- `docs/brand/BRAND-FOUNDATIONS.md` — identité de marque (personnalité,
  palette, typographie, principes d'évitement). Ce document **hérite**
  la palette et la typographie sans les redéfinir (§6) et **applique**
  les principes d'évitement de marque au niveau interaction (§1).
- `20-APPLICATION-UX-ARCHITECTURE-CONTRACT.md` — architecture UX
  (continuité de contexte, anti-CRUD, anatomie d'écran, hiérarchie de
  l'information, doctrine bureau/tablette/terrain, contrat responsive,
  cadre de navigation, accessibilité au niveau principe, contrat de
  validation, registre d'anti-patterns). Ce document **applique** cette
  architecture au niveau composant, interaction et exécution visuelle —
  il ne rejoue jamais une décision déjà actée par `20`.
- `04-JOURNEYS-UX-BLUEPRINT.md` — parcours et architecture de
  l'information par zone. Source des exemples de microcopy (§4) et des
  signatures (§2) — jamais recopié.
- `docs/architecture/TECHNICAL-STACK-CONTRACT.md` — rails techniques
  (React, Tailwind, shadcn/ui, Radix). Ce document ne prescrit aucune
  technologie ; il prescrit un comportement, indépendamment de son
  implémentation.
- `13-ACCEPTANCE-NEGATIVE-TEST-MATRIX.md` / `16-CANONICAL-EXECUTION-
  INDEX.md` §8 — doctrine de preuve (aucune déclaration `REAL` sans
  vérification). Toute valeur numérique introduite ici sans validation
  visuelle réelle est marquée `SUPORDO_BASELINE_TO_VALIDATE` —
  application directe de cette doctrine à l'exécution visuelle.

**Ce document ne fait pas** : ne redéfinit pas la palette, la
typographie ou les principes de marque (`BRAND`) ; ne redéfinit pas les
parcours métier, la continuité de contexte ou le cadre de navigation
(`20`) ; ne tranche aucune décision `OPEN` de `16` §6 ; n'implémente
rien — c'est un contrat d'expérience, pas du code. Toute valeur
présentée ici est un point de départ à valider visuellement dans le
navigateur avant d'être considérée stable (§12).

## Table des matières

1. Product Experience Principles (+ `GENERIC_SAAS_SMELL`)
2. SUPORDO Signatures (A–E)
3. Interaction Model
4. Microcopy System
5. Motion & Microinteractions
6. Visual Language
7. Density Modes
8. Adaptive Composition
9. Component Experience Contracts (16 composants)
10. Accessibility Quality Bar
11. Perceived Performance
12. Visual QA Contract
13. Benchmark Principles
14. Décisions ouvertes & valeurs à valider

## Repère rapide

Pour un agent qui doit décider vite, sans relire le document entier :

```
Que préserver ?          — les 5 signatures (§2) et tout [PRINCIPLE]
                            hérité de BRAND/20 (voir Relation ci-dessus).
Que éviter ?              — GENERIC_SAAS_SMELL (§1) et chaque
                            [ANTI_PATTERN] du document, chacun avec un
                            critère d'audit.
Desktop ou terrain ?      — §7 (OFFICE_DENSITY/FIELD_DENSITY) + §8
                            (seuils 360/390/768/1280) ; la zone
                            768–1279 est une zone de transition `OPEN`
                            (§7, §14), pas encore un troisième mode.
Quelle action primaire ?  — §3 (hiérarchie des 5 tiers) + §2.C (Next
                            Action Strip) : une seule à la fois.
Comment écrire ?          — §4 (règles + exemples canoniques par objet
                            et par état).
Quelle motion ?            — §5 (échelle + doctrine d'easing), déclinée
                            par composant en §9.
Est-ce que ça "fait
SUPORDO" ?                — l'écran porte-t-il au moins une des 5
                            signatures (§2) de façon reconnaissable
                            même logo masqué (§1, critère d'audit
                            "sidebar + cards interchangeable") ?
```

---

## 1. Product Experience Principles

[PRINCIPLE] **Workflow before screen.** Une vue n'existe pas pour
représenter un objet ou une table ; elle existe pour faire avancer un
workflow métier réel (devis → accepté → chantier, RDV → intervention →
facture). Rejoint et applique l'anti-CRUD de `20` §6 au niveau
composition d'écran.

[PRINCIPLE] **Context before navigation.** L'utilisateur ne doit jamais
avoir à renaviguer pour retrouver un contexte déjà établi. La navigation
est un dernier recours, pas le mécanisme par défaut de continuité —
application directe de `20` §3 au niveau interaction.

[PRINCIPLE] **Action before decoration.** Chaque élément visuel doit
soit porter de l'information, soit permettre une action. Un élément qui
ne fait ni l'un ni l'autre est retiré, pas justifié.

[PRINCIPLE] **Density without clutter.** Une densité d'information
élevée est un objectif pour le bureau (§7), pas un prétexte à
l'entassement. La densité vient de la suppression de l'inutile, jamais
de la réduction d'espacement en dessous du seuil de confort tactile.

[PRINCIPLE] **Progressive disclosure.** L'essentiel apparaît d'abord ;
le détail existe à un clic/tap, jamais imposé par défaut — application
au niveau composant de `20` §8.

[PRINCIPLE] **Field ergonomics.** Toute décision de composition doit
rester valide pour un utilisateur terrain : une main, gants possibles,
lumière extérieure, connexion incertaine, interruption fréquente (§7,
§8).

[PRINCIPLE] **Perceived speed.** L'interface doit *paraître* immédiate
même quand une opération réseau ne l'est pas — feedback avant
confirmation serveur lorsque c'est sûr (§5, §11).

[PRINCIPLE] **One coherent interaction language.** Un pattern
d'interaction (comment on édite, comment on confirme, comment on
annule) ne varie jamais d'un objet métier à l'autre sans raison métier
explicite. Un utilisateur qui a appris à éditer un Client sait éditer un
Lieu.

[PRINCIPLE] **No generic SaaS aesthetic.** SUPORDO ne doit être
confondable avec aucun CRM/SaaS générique produit par un gabarit IA ou
un thème shadcn par défaut. Voir `GENERIC_SAAS_SMELL` ci-dessous.

### GENERIC_SAAS_SMELL

Registre ouvert, complémentaire de `20` §17 (registre d'anti-patterns
UX) — celui-ci porte spécifiquement sur la **reconnaissabilité
visuelle et d'interaction**, jamais dupliqué avec `20` §17.

[ANTI_PATTERN] **Card-per-section.** Chaque section d'écran encapsulée
dans une carte avec ombre et bordure, par défaut, sans raison de
séparation réelle. Rejoint `docs/brand/BRAND-FOUNDATIONS.md`
("éviter la prolifération artificielle de cards") — voir §6 pour la
doctrine d'usage de `CARD`.

[ANTI_PATTERN] **Dashboard de KPI sans action réelle.** Déjà interdit
par `20` §12 au niveau parcours ; ici étendu au niveau visuel — une
grille de chiffres décoratifs en haut d'écran, sans lien vers l'action
qu'ils devraient déclencher.

[ANTI_PATTERN] **Gros espaces décoratifs.** Hero sections, bandeaux
marketing, espace vide gratuit dans l'interface opérationnelle — la
doctrine d'imagerie de `BRAND-FOUNDATIONS.md` réserve l'univers
éditorial/3D à l'onboarding et aux empty states, jamais à l'écran de
travail. *Critère d'audit* : sur la première zone visible sans scroll
(§12), plus d'un tiers de la hauteur sans information ni action
exploitable.

[ANTI_PATTERN] **Gradient/blob/glassmorphism gratuit.** Déjà interdit
par `BRAND-FOUNDATIONS.md` ; rappelé ici comme smell le plus
diagnostique d'une interface générée sans intention.

[ANTI_PATTERN] **Badges partout.** Un badge de statut sur chaque ligne,
chaque carte, chaque titre — au point que le badge cesse de signaler
quoi que ce soit. Voir `Status` (§9) pour la doctrine d'usage. *Critère
d'audit* : plus d'un badge de statut simultané pour un même objet, ou un
badge présent sur un élément qui ne porte aucun état métier réel.

[ANTI_PATTERN] **Formulaires CRUD sans contexte.** Un formulaire qui
demande des champs sans rappeler à quel objet parent, quel workflow,
quel état métier il se rattache. Rejoint `20` §6.

[ANTI_PATTERN] **Sidebar + cards interchangeable avec n'importe quel
SaaS.** Une coquille de navigation qui ne porte aucune des signatures
`§2` (Context Spine, Next Action Strip) — reconnaissable seulement par
son logo, jamais par son comportement. *Critère d'audit* : masquer le
logo/nom de marque sur une capture — si rien d'autre (signatures §2,
microcopy §4) ne permet d'identifier SUPORDO, l'écran échoue ce
critère.

[ANTI_PATTERN] **Microcopy générique.** "Élément", "enregistrement",
"soumettre", "opération réussie" — voir §4 pour la règle et les
alternatives.

[ANTI_PATTERN] **Animations décoratives.** Toute animation qui ne
communique aucune information d'état ou de relation spatiale — voir §5.

---

## 2. SUPORDO Signatures

Cinq signatures, reconnaissables indépendamment du thème visuel — elles
définissent le **comportement** de SUPORDO, pas seulement son style.
Une implémentation qui change la palette mais conserve ces cinq
signatures reste reconnaissable comme SUPORDO ; l'inverse est faux.

### A. CONTEXT SPINE

```
PURPOSE            — rendre visible en permanence la chaîne métier qui
                      justifie la présence de l'utilisateur sur cet
                      écran : Client → Lieu → Devis (objet
                      transactionnel réel, `T1`) → état courant.
                      Application directe de `20` §3 (Context
                      Continuity Contract) au niveau composition.
WHEN_VISIBLE        — sur tout écran atteint depuis un objet parent
                      identifié (ex. Devis atteint depuis un Client).
                      Absent sur les écrans sans contexte parent
                      (listes racine, accueil).
INFORMATION         — identité du/des objet(s) parents, état courant de
                      l'objet actif (ex. "Devis · Brouillon"), jamais
                      plus de 4 maillons simultanés.
PRIMARY_ACTION      — chaque maillon est navigable vers l'objet qu'il
                      représente, sans perte du reste de la chaîne.
DESKTOP_BEHAVIOR    — fil persistant en tête d'écran, toujours visible,
                      typographie discrète mais lisible.
MOBILE_BEHAVIOR     — compacté au maillon actif + un niveau parent ;
                      la chaîne complète s'ouvre au tap (reveal, pas
                      navigation) — voir §8.
MOTION              — aucune animation d'entrée récurrente ; seul le
                      remplacement d'un maillon (changement de contexte)
                      anime en transition de contexte (§5,
                      220–300 ms).
MICROCOPY           — noms métier réels ("Marc Dubois", "12 rue de la
                      Paix"), jamais un identifiant technique.
ANTI_PATTERN        — un fil d'Ariane générique de type
                      `Accueil > Clients > Détail` qui reflète le
                      schéma de routes plutôt que le contexte métier
                      (rejoint `20` §17, nav = schéma DB).
```

**Note terminologique** — « Affaire » n'est **pas** un objet du modèle
SUPORDO : `20` §3 interdit explicitement son introduction silencieuse
tant qu'aucune `SUPORDO_DECISION` ne l'a actée. La chaîne ci-dessus
utilise « Devis », objet réel et livré (`T1`), comme maillon
transactionnel. Si un objet fédérateur générique était un jour décidé,
il remplacerait ce maillon — décision explicitement hors du périmètre
de ce document.

### B. LIVING DOSSIER

```
PURPOSE             — rendre lisible en un seul endroit l'historique
                      métier complet d'un Client ou d'un Lieu : RDV,
                      photos, devis, accord, facture, avoir,
                      intervention — sans reconstitution manuelle par
                      l'utilisateur.
WHEN_VISIBLE        — sur la fiche Client et la fiche Lieu (`20` §6,
                      fiche d'objet `DOMAIN_CORE`) ; en aperçu réduit
                      sur les écrans où le Client/Lieu est identifié
                      en contexte.
INFORMATION         — événements ordonnés chronologiquement, typés
                      (devis, RDV, facture, avoir, intervention), état
                      de chacun visible sans ouverture.
PRIMARY_ACTION      — ouvrir l'objet source de l'événement, contexte
                      préservé (retour possible sans perte, `20` §3
                      EXAMPLE Devis→RDV).
DESKTOP_BEHAVIOR    — colonne/panneau dédié, défilement indépendant du
                      reste de la fiche, filtrable par type
                      d'événement.
MOBILE_BEHAVIOR     — liste verticale unique, les plus récents
                      d'abord, filtrage réduit à l'essentiel (curatage,
                      `20` §8).
MOTION              — insertion d'un nouvel événement en liste anime
                      (§5, 180–240 ms) pour signaler qu'une action
                      vient de produire un résultat traçable —
                      renforce §11 (perceived performance).
MICROCOPY           — verbe métier au passé : "Devis envoyé le 12
                      mars", jamais "Devis — created_at: 2026-03-12".
ANTI_PATTERN        — un historique tronqué à un seul type d'objet
                      (ex. seulement les factures) présenté comme
                      complet, ou un événement présenté avant sa
                      confirmation réelle (rejoint `09` §C, discipline
                      REAL/PROTOTYPE/MOCK).
```

### C. NEXT ACTION STRIP

```
PURPOSE             — exposer une action primaire unique,
                      contextualisée selon l'état métier réel de
                      l'objet — application directe de `20` §5
                      (Next-Action Doctrine) au niveau composant.
WHEN_VISIBLE        — sur tout écran d'objet dont l'état détermine une
                      suite logique (Devis brouillon → "Envoyer le
                      devis" ; Devis accepté → "Planifier
                      l'intervention" si la capacité existe déjà,
                      jamais sinon).
INFORMATION         — le seul verbe d'action pertinent pour l'état
                      courant ; pas de liste d'actions possibles
                      mélangées.
PRIMARY_ACTION      — une seule action à la fois — voir §3
                      `PRIMARY_ACTION` pour le contrat de placement.
DESKTOP_BEHAVIOR    — positionnée en zone haute/droite de l'écran
                      d'objet, toujours visible sans scroll (au-dessus
                      du pli).
MOBILE_BEHAVIOR     — ancrée en bas d'écran, cible tactile ≥ 44px
                      (§7 FIELD_DENSITY), jamais recouverte par le
                      clavier virtuel.
MOTION              — apparition/disparition liée au changement d'état
                      métier anime en feedback de succès (§5, ≤400 ms
                      non bloquant), jamais en boucle ou répétitive.
MICROCOPY           — verbe métier précis ("Envoyer le devis", pas
                      "Continuer" ni "Suivant").
ANTI_PATTERN        — un bouton menant vers une capacité non construite
                      (`20` §5 ANTI_PATTERN), ou plusieurs actions de
                      poids visuel égal se disputant le statut de
                      primaire.
```

### D. TERRAIN MODE

```
PURPOSE             — offrir sur mobile une composition organisée
                      strictement autour de l'ordre de valeur terrain
                      défini par `20` §12 : quoi · quand · où · pour
                      qui · pourquoi · action immédiate.
WHEN_VISIBLE        — toute vue "Aujourd'hui"/Planning/terrain
                      consultée en largeur mobile (< 768px, §8).
INFORMATION         — RDV/intervention du jour uniquement par défaut ;
                      lieu, client, devis lié — jamais de KPI en tête
                      (`20` §12).
PRIMARY_ACTION      — action directe liée à la tâche du moment (appel,
                      itinéraire, ouverture du devis lié) — pas de
                      formulaire multi-étape en entrée.
DESKTOP_BEHAVIOR    — non applicable tel quel ; l'équivalent bureau est
                      une vue planning multi-jours/multi-ressources
                      (`20` §9 BUREAU).
MOBILE_BEHAVIOR     — liste à une main, un item = une tâche, défilement
                      vertical unique, pas de tableau.
MOTION              — transition entre tâches du jour = state
                      transition (§5, 100–160 ms), jamais de
                      transition de page complète pour rester dans le
                      même contexte terrain.
MICROCOPY           — direct et actionnable : "Appeler Marc Dubois",
                      "Itinéraire vers le chantier", jamais "Voir les
                      détails".
ANTI_PATTERN        — copie miniature du planning bureau sur mobile
                      (`20` §17, déjà interdit) ; capture perdue en cas
                      de coupure réseau (`04` §4, contrainte terrain).
```

### E. FINANCIAL LANGUAGE

```
PURPOSE             — traiter HT / TVA / TTC / marge / acompte / reste
                      dû / payé avec un vocabulaire et une présentation
                      strictement cohérents partout où un montant
                      apparaît.
WHEN_VISIBLE        — Devis, Facture, Avoir, tout résumé financier de
                      Chantier.
INFORMATION         — le montant affiché indique toujours explicitement
                      sa nature (HT/TTC), jamais un nombre nu ambigu.
PRIMARY_ACTION      — action financière engageante (émettre, encaisser
                      un acompte) toujours distincte visuellement d'une
                      action de consultation — voir `DESTRUCTIVE_ACTION`
                      §3 pour les actions irréversibles adjacentes.
DESKTOP_BEHAVIOR    — tableau de lignes aligné à droite,
                      totaux/sous-totaux visuellement hiérarchisés
                      (§6 numeric typography).
MOBILE_BEHAVIOR     — total TTC et reste dû toujours visibles sans
                      scroll ; détail des lignes en second niveau.
MOTION              — recalcul de montant (ajout/suppression de ligne)
                      anime la valeur qui change (§5, 100–160 ms) pour
                      que l'utilisateur perçoive *quoi* a changé, jamais
                      un simple remplacement muet.
MICROCOPY           — "Reste dû : 450 € TTC", jamais "Balance: 450".
                      Voir §4 pour les formulations canoniques Facture.
ANTI_PATTERN        — afficher un total sans préciser HT/TTC ; modifier
                      visuellement une facture numérotée comme si
                      c'était possible (`04`, Zone Facturation, déjà
                      interdit).
```

---

## 3. Interaction Model

### Hiérarchie des actions

[PRINCIPLE] **`PRIMARY_ACTION`** — une seule par écran/contexte, portée
par le Next Action Strip (§2.C). Poids visuel maximal (bouton plein,
couleur brand). Ne coexiste jamais avec une seconde action de poids
identique.

[PRINCIPLE] **`CONTEXTUAL_ACTION`** — rattachée visuellement à l'objet
qu'elle affecte (ligne de tableau, carte, panneau). Poids visuel
intermédiaire (icône+label ou icône seule avec libellé accessible).
Visible par défaut en densité terrain (§7, pas de hover sur tactile),
révélée au survol/focus en densité bureau si l'espace le justifie.

[PRINCIPLE] **`SECONDARY_ACTION`** — action de support (dupliquer,
exporter, imprimer). Poids visuel faible (bouton fantôme/texte).
Regroupée derrière un menu au-delà de 3 actions secondaires
simultanées sur un même objet.

[PRINCIPLE] **`DESTRUCTIVE_ACTION`** — visuellement isolée des actions
non destructrices (espacement ou séparateur, jamais adjacente
directe au primaire). Couleur "danger" réservée exclusivement à cet
usage — jamais employée à titre décoratif ailleurs. Confirmation
explicite obligatoire uniquement pour les opérations réellement
risquées ou irréversibles (§4, règle de confirmation) — pas de
confirmation systématique qui banalise le geste.

[PRINCIPLE] **`GLOBAL_ACTION`** — non rattachée à un objet de l'écran
courant (ex. "Nouveau client" depuis n'importe où). Emplacement unique
et prévisible dans toute l'application (zone d'en-tête ou command
menu, §3 ci-dessous) — jamais dupliquée à un endroit différent par
écran.

[ARCHITECTURE_DECISION] Règle de placement : le poids visuel d'une
action doit toujours refléter sa position dans cette hiérarchie —
aucune `SECONDARY_ACTION` ne peut recevoir un traitement visuel
supérieur à celui d'une `PRIMARY_ACTION` sur le même écran, aucune
`DESTRUCTIVE_ACTION` ne peut se fondre visuellement dans les actions
neutres.

### Étude de référence — Linear, Attio, Raycast

Étudiés comme **références fonctionnelles d'interaction**, jamais comme
identité visuelle à reproduire — voir §13 pour l'analyse complète
`REFERENCE`/`WHY_GOOD`/`SUPORDO_ADAPTATION`/`WHAT_NOT_TO_COPY`. Décisions
d'adoption pour le modèle d'interaction SUPORDO :

- **Command menu / command palette** : adopté comme accélérateur
  optionnel pour `GLOBAL_ACTION` et navigation rapide (clavier-first).
  **Jamais** un chemin obligatoire — un utilisateur terrain sans clavier
  doit accomplir la même tâche par le chemin visuel standard.
- **Contextual side panels** : adopté pour le composant `ContextPanel`
  (§9) — consulter/éditer un objet lié sans perdre le Context Spine
  (§2.A), application directe de `20` §3.
- **Peek / preview** : adopté pour un aperçu rapide d'un objet lié
  (ex. peek du devis depuis un RDV) sans navigation complète — ne
  remplace jamais le Living Dossier (§2.B) comme vue d'historique
  complète.
- **Persistent filtered views** : adopté pour les listes (Clients,
  Devis, Factures) — vues filtrées mémorisables, jamais imposées par
  défaut.
- **Quick actions** : adopté comme forme de `CONTEXTUAL_ACTION`, jamais
  comme rangée d'icônes décoratives systématiques (rejoint
  `GENERIC_SAAS_SMELL`, badges/icônes partout).

**Rejeté explicitement** : l'esthétique monochrome/minimaliste de ces
outils en tant que telle (déjà couverte par §6, héritée de `BRAND`),
et l'absence de pensée terrain/mobile-first de ces produits — ce sont
des outils desktop de power-users, SUPORDO ne l'est pas par défaut.

---

## 4. Microcopy System

### Règles

[PRINCIPLE] Verbes métier concrets : "Envoyer le devis", "Planifier
l'intervention", "Encaisser l'acompte" — jamais "Soumettre",
"Valider", "Continuer" seuls.

[PRINCIPLE] Jamais "élément", "enregistrement", "objet" si un terme
métier existe : "client", "lieu", "devis", "facture", "rendez-vous",
"avoir" — pas d'exception.

[PRINCIPLE] État ≠ action. Un badge de statut affiche un état ("En
attente de paiement") ; un bouton affiche une action ("Encaisser") —
jamais un badge cliquable qui mélange les deux registres.

[PRINCIPLE] Erreur = cause + conséquence + solution. Une erreur qui ne
donne que la cause laisse l'utilisateur bloqué ; une erreur sans
solution n'est pas actionnable.

[PRINCIPLE] Succès = résultat concret, jamais générique ("Opération
réussie").

[PRINCIPLE] Empty state = contexte + action, jamais une simple absence
("Aucune donnée").

[PRINCIPLE] Confirmation exigée uniquement pour les opérations
réellement risquées (irréversibles ou à conséquence financière/légale,
ex. émission de facture — `20` §16, `04` Zone Facturation L1) — jamais
pour un geste anodin et réversible, sous peine de banaliser la
confirmation elle-même.

[PRINCIPLE] Langage court, professionnel, humain — pas de familiarité
artificielle, pas de ton robotique.

[PRINCIPLE] Aucun jargon développeur exposé à l'utilisateur (`id`,
`null`, `enum`, noms de champs techniques).

### Exemples canoniques par objet

**Client**
- `EMPTY` — "Aucun client pour l'instant. Ajoutez votre premier client
  pour créer un devis." + action "Ajouter un client".
- `ERROR` — "Ce numéro de téléphone est déjà utilisé par un autre
  client. Vérifiez la fiche existante avant d'en créer une nouvelle."
- `SUCCESS` — "Client ajouté. Vous pouvez créer un devis pour lui dès
  maintenant."

**Lieu**
- `EMPTY` — "Aucun lieu rattaché à ce client. Ajoutez l'adresse du
  chantier pour planifier une intervention." + action "Ajouter un
  lieu".
- `ERROR` — "Cette adresse n'a pas pu être localisée. Vérifiez le code
  postal ou enregistrez-la sans localisation."
- `SUCCESS` — "Lieu ajouté à la fiche de Marc Dubois."

**Devis**
- `EMPTY` — "Aucun devis pour ce client. Créez-en un pour démarrer une
  affaire." + action "Créer un devis".
- `ERROR` — "Ce devis contient une ligne sans prix. Complétez-la avant
  de l'envoyer."
- `SUCCESS` — "Devis envoyé à marc.dubois@email.fr le 25 septembre."

**RDV**
- `EMPTY` — "Aucun rendez-vous planifié. Planifiez une visite ou une
  intervention." + action "Planifier un rendez-vous".
- `ERROR` — "Ce créneau chevauche un autre rendez-vous déjà planifié à
  la même adresse."
- `SUCCESS` — "Rendez-vous confirmé le 30 septembre à 14h chez Marc
  Dubois."

**Facture**
- `EMPTY` — "Aucune facture émise pour ce devis. Facturez-le une fois
  le chantier terminé." + action "Créer une facture".
- `ERROR` — "Le solde restant ne correspond pas au montant du devis.
  Vérifiez les acomptes déjà encaissés avant d'émettre."
- `SUCCESS` — "Facture F-2026-0042 émise. Reste dû : 450 € TTC."

**Avoir**
- `EMPTY` — non applicable par défaut (un avoir n'a pas d'état vide
  autonome — il naît d'une correction de facture).
- `ERROR` — "Impossible de créer un avoir supérieur au montant restant
  de la facture d'origine."
- `SUCCESS` — "Avoir A-2026-0007 créé pour la facture F-2026-0042. Le
  solde dû a été recalculé."

**Planning**
- `EMPTY` — "Rien de prévu aujourd'hui. Planifiez un rendez-vous ou
  consultez la semaine." + action "Planifier".
- `ERROR` — "Impossible d'afficher le planning : connexion perdue.
  Les rendez-vous déjà chargés restent consultables."
- `SUCCESS` — non applicable comme feedback autonome (le succès se lit
  dans l'apparition de l'événement, §2.B Living Dossier, pas dans un
  message dédié).

### États transverses

**`LOCKED`** — s'applique principalement à Devis accepté et Facture
émise (immutabilité, `04` Zone Facturation).
> "Cette facture a été émise le 25 septembre et ne peut plus être
> modifiée. Pour corriger un montant, créez un avoir."

**`DESTRUCTIVE`** — suppression d'un Client, Lieu, ou ligne de devis
non encore engagée. **Exemple illustratif du registre de langage
uniquement** — le périmètre exact de la suppression en cascade (quels
objets liés sont réellement supprimés) est une décision produit non
traitée par ce document, à confirmer avant implémentation.
> "Supprimer ce client supprimera aussi ses lieux et devis en
> brouillon associés. Cette action est irréversible." + confirmation
> explicite (nom du client à reconfirmer si l'historique n'est pas
> vide).

**`OFFLINE/FUTURE`** — capacité non encore implémentée (PWA/offline,
`TECHNICAL-BASELINE.md`) ou perte de connexion réelle.
> "La capture hors connexion n'est pas encore disponible sur SUPORDO."
> (jamais un message qui laisse croire à une synchronisation
> silencieuse qui n'existe pas — rejoint `20` §17, faux module).

**`PERMISSION_DENIED`** — accès refusé par la RLS/le rôle du membre du
tenant.
> "Vous n'avez pas les droits pour émettre une facture. Contactez un
> administrateur de votre entreprise."

---

## 5. Motion & Microinteractions

[PRINCIPLE] Le motion communique une information (quoi vient de
changer, où va le contexte, quel est le nouvel état) — il ne décore
jamais un geste qui n'a pas besoin d'être expliqué.

### Échelle initiale — `SUPORDO_BASELINE_TO_VALIDATE`

```
instant feedback (clic, tap)          80–120 ms
selection / toggle                    100–160 ms
popover / menu                        120–180 ms
drawer / panel                        180–240 ms
context / layout transition           220–300 ms
success feedback (non bloquant)       ≤ 400 ms
```

Ces valeurs sont un point de départ raisonné, **non validées
visuellement** — à confirmer lors du premier audit visuel réel (§12)
avant d'être considérées stables, conséquence directe de la doctrine de
preuve `13`/`20` §16 appliquée au motion.

### Doctrine d'easing

[PRINCIPLE] Entrée (apparition) : easing "ease-out" — départ rapide,
arrivée douce, perçu comme réactif.
[PRINCIPLE] Sortie (disparition) : easing "ease-in" — départ doux,
sortie rapide, ne retient pas l'attention sur un élément qui part.
[PRINCIPLE] Transition d'état (toggle, sélection) : easing standard
symétrique, la plus courte de l'échelle — l'utilisateur ne doit jamais
attendre une confirmation d'état déjà décidée.
[PRINCIPLE] Transition de panneau/contexte : easing "ease-out" plus
long, doit préserver la sensation de continuité spatiale (le panneau
vient "de" l'élément qui l'a déclenché, jamais un remplacement brutal
de l'écran).

### Comportements spécifiques

- **Insertion/suppression de liste** (Living Dossier §2.B, lignes de
  devis) : l'élément entrant/sortant anime sa propre apparition/
  disparition, les voisins se repositionnent en douceur — jamais un
  saut brutal de mise en page (rejoint §11, no layout jumping).
- **Skeleton vs spinner** : skeleton pour tout contenu structurel en
  cours de chargement (liste, fiche) ; spinner réservé aux actions
  courtes indéterminées (bouton en cours de soumission) — voir §11.
- **Feedback optimiste** : autorisé uniquement lorsque l'opération est
  techniquement sûre (faible risque d'échec serveur, effet réversible
  côté UI) — ex. cocher une tâche planning. **Interdit** pour toute
  opération financière engageante (émission facture, acceptation
  devis) : l'UI attend la confirmation réelle avant d'afficher le
  succès (rejoint `04` Zone Facturation, `09` §C REAL/PROTOTYPE).
- **`prefers-reduced-motion`** : toute animation non essentielle à la
  compréhension (transitions décoratives, easing long) est supprimée
  ou réduite à un fondu instantané ; les animations qui communiquent un
  changement d'état réel (§ci-dessus) restent mais raccourcies au
  minimum de l'échelle.

[ANTI_PATTERN] Bounce, parallax, ou toute animation décorative
répétitive (rejoint `GENERIC_SAAS_SMELL` §1) — interdits sans
exception.

---

## 6. Visual Language

**Hérité, jamais redéfini**, de `BRAND-FOUNDATIONS.md` : typographie
Manrope, palette Brand Green `#00875A` · Forest `#10291C` · Forest Dark
`#07140D` · Warm `#FAF8F4` · Mint `#EAF4EE`. **`BRAND-FOUNDATIONS.md`
reste l'unique source de vérité** de ces valeurs — recopiées ci-dessus
par confort de lecture uniquement ; en cas d'écart futur entre les deux
fichiers, `BRAND-FOUNDATIONS.md` fait foi et ce document doit être
corrigé en conséquence, jamais l'inverse. Ce document ne redéfinit
aucune de ces valeurs — il définit comment les décliner en échelles
d'exécution.

### Échelles — toutes `SUPORDO_BASELINE_TO_VALIDATE` sauf mention contraire

- **Typographic hierarchy** : niveaux nommés (Display, Title, Heading,
  Body, Caption, Numeric) — valeurs px/line-height à fixer lors du
  premier audit visuel (§12), jamais improvisées écran par écran.
- **Spacing scale** : échelle à base 4px (4/8/12/16/24/32/48/64),
  compatible avec l'échelle Tailwind déjà en usage dans le code —
  cohérente avec `tailwind.config.ts` actuel, à valider visuellement.
- **Density scale** : deux modes distincts, `OFFICE_DENSITY` et
  `FIELD_DENSITY` — voir §7, pas une simple réduction proportionnelle.
- **Surface hierarchy** : `CANVAS` (fond d'application) → `SECTION`
  (regroupement sans conteneur visible) → `PANEL` (regroupement avec
  bordure/fond différencié) → `CARD` (unité autonome répétée, usage
  restreint) → `SHEET`/`DIALOG` (superposition modale) — ordre
  d'élévation croissante, chaque niveau ajouté seulement si le niveau
  précédent ne suffit pas à distinguer l'information.
- **Border hierarchy** : trait fin (`--border` existant, séparateur
  discret) distinct du contour de conteneur (`PANEL`/`CARD`), distinct
  du focus ring (§ci-dessous) — trois poids visuels jamais confondus.
- **Radius scale** : héritée de `--radius: 0.5rem` (code actuel) —
  `sm`/`md`/`lg` déjà définis en relatif dans `tailwind.config.ts`,
  conservés comme base ; un radius `pill` (statuts, filtres) reste à
  valider visuellement.
- **Elevation scale** : plate par défaut (pas d'ombre sur `SECTION`/
  `CARD` de base) ; élévation réservée aux couches superposées
  (`SHEET`/`DIALOG`/popover) — jamais une ombre décorative sur un
  élément au même plan que le reste de l'écran (rejoint
  `GENERIC_SAAS_SMELL`).
- **Icon sizing** : échelle 16/20/24px liée à la densité (§7) — icônes
  toujours accompagnées d'un libellé explicite sur action (`20` §15).
- **Numeric typography** : chiffres tabulaires (`tabular-nums`) pour
  tout montant ou tableau de données ; alignement à droite pour les
  colonnes monétaires ; formatage décimal cohérent HT/TTC (§2.E).
- **Focus ring** : visible en permanence au clavier, dérivé du token
  `--ring` déjà présent dans le code — jamais supprimé pour raison
  esthétique (`20` §15).
- **Selection state** : fond teinté Mint (`#EAF4EE`), jamais un bleu
  générique de sélection navigateur — cohérence de marque appliquée à
  l'état, rejoint `BRAND-FOUNDATIONS.md` ("éviter le SaaS générique
  bleu/violet").

### Doctrine des surfaces — quand utiliser quoi

```
CANVAS       — fond global de l'application. Jamais d'action ni
               d'information directement dessus.
SECTION      — regroupement logique d'information sans conteneur
               visible propre (simple espacement/titre). Usage par
               défaut à l'intérieur d'un écran.
PANEL        — regroupement avec délimitation visuelle propre,
               généralement latéral ou empilé (ContextPanel §9) —
               utilisé quand deux zones d'information distinctes
               coexistent à l'écran.
CARD         — unité autonome répétée dans une collection (une carte =
               un objet d'une liste). Interdiction stricte d'une carte
               par section d'écran unique (`GENERIC_SAAS_SMELL`).
TABLE/LIST   — collection d'objets comparables, densité bureau par
               défaut (§7) ; devient liste de cartes empilées en
               densité terrain (§8, pattern `replace`).
SHEET        — superposition plein écran ou quasi plein écran sur
               mobile, pour une tâche focalisée qui interrompt le flux
               (édition complète d'un objet en TERRAIN MODE).
DIALOG       — superposition centrée bureau, pour une confirmation ou
               une tâche courte qui ne justifie pas un panneau complet.
```

---

## 7. Density Modes

[ARCHITECTURE_DECISION] Deux modes de densité, définis structurellement
— pas un simple scale-down responsive d'un mode vers l'autre.

### OFFICE_DENSITY

- Contexte : bureau, clavier/souris, grands écrans (`20` §9 BUREAU).
- Sélection d'information : large — tableaux complets, colonnes
  multiples, vision multi-objets simultanée.
- Actions simultanées : plusieurs `CONTEXTUAL_ACTION` visibles par
  ligne, menus secondaires accessibles au survol.
- Layout : multi-panel possible (liste + détail + contexte, §8 split).
- Cibles : dimensionnées pour la précision du pointeur, pas de
  contrainte tactile minimale.

### FIELD_DENSITY

- Contexte : terrain, tactile, une main, conditions dégradées (`20`
  §9 TERRAIN).
- Sélection d'information : curatée — un focus principal à la fois
  (§2.D Terrain Mode), jamais un tableau dense.
- Actions simultanées : une action primaire visible, actions
  secondaires masquées derrière un geste explicite.
- Layout : simple colonne, focus unique, pas de multi-panel.
- Cibles : **44–48px minimum** sur tout élément interactif principal —
  seuil non négociable, distinct du minimum WCAG générique (§10).

[PRINCIPLE] Le passage `OFFICE_DENSITY` → `FIELD_DENSITY` change la
*sélection* et l'*organisation* de l'information, jamais seulement sa
taille — un tableau qui rétrécit reste un tableau raté sur mobile
(rejoint `20` §17, copie miniature du desktop).

### Zone tablette (768–1279px)

[OPEN] `20` §9 exige que bureau/tablette/terrain restent *« pensés
séparément »* — *« un mode n'est pas une simple contraction visuelle
d'un autre »*. Ce document ne définit **pas** de troisième mode de
densité stabilisé pour la tablette : la zone 768–1279px (§8) reste une
zone de transition entre `OFFICE_DENSITY` et `FIELD_DENSITY`, dont le
comportement exact (bascule nette vs. dégradé progressif, voire un
futur `TABLET_DENSITY` distinct) n'est pas tranché ici et doit être
validé par un audit visuel réel (§12) avant de devenir stable. Ne pas
lire le traitement actuel de la tablette comme une fermeture silencieuse
de l'exigence `20` §9 — reporté en `OPEN` (§14).

---

## 8. Adaptive Composition

Aux seuils déjà actés par `20` §10 (360 · 390 · 768 · desktop, étendu
ici à 1280 comme large desktop validé par le code existant) — ce
document décrit le **changement de composition**, jamais seulement de
largeur.

### 360–389px

- **Context Spine** (§2.A) : `hide` → `reveal` au tap (compacté par
  défaut).
- **Table/List** : `replace` par liste de cartes empilées
  (`FIELD_DENSITY`).
- **ContextPanel** : `replace` par `Sheet` plein écran (jamais de
  panneau latéral partiel).
- **ActionBar** : `reposition` en bas d'écran, ancrée (Next Action
  Strip §2.C).
- **Dialog** : `replace` par `Sheet` si le contenu dépasse une
  confirmation courte.

### 390–767px

- Identique à 360–389 avec plus de respiration ; `reveal` d'un second
  niveau d'information dans le Living Dossier (§2.B) devient possible
  sans scroll excessif.

### 768–1279px (tablette — zone de transition, voir §7)

- **Table/List + ContextPanel** : `split` devient possible — liste à
  gauche, panneau contextuel/peek à droite, si l'espace le permet
  (`20` §9 TABLETTE, usage intermédiaire).
- **Context Spine** : `reveal` complet sans repli.
- **ActionBar** : `reposition` en tête d'écran (retour au
  comportement bureau), plus seulement ancrée en bas.
- **CONTEXTUAL_ACTION** : passage progressif du modèle "révélé au
  tap" vers "visible par défaut" si la densité de la vue le permet.

### 1280px et plus (bureau)

- **Multi-panel** : `split` pleinement exploité — liste + détail +
  contexte simultanés (`OFFICE_DENSITY`).
- **ContextPanel** : panneau latéral natif, jamais un `Sheet`.
- **Command menu** (§3) : pleinement disponible, raccourcis clavier
  actifs.
- **Table/List** : colonnes complètes, tri/filtre visibles sans menu
  supplémentaire.

[PRINCIPLE] Chaque changement de seuil doit être justifiable en termes
de `reflow`/`reveal`/`hide`/`replace`/`reposition`/`split` — un
changement de composition qui ne peut être nommé par l'un de ces six
verbes n'est pas une décision volontaire, c'est un accident CSS.

---

## 9. Component Experience Contracts

Contrats d'expérience — **aucune implémentation attendue à ce stade**
(`Aucun code`). Sert de spécification pour une tranche UI future, que
le composant soit déjà implémenté en style shadcn/ui (`Button`,
`Input`, `Dialog`, `Card`, `Label`, `Separator` existent déjà dans
`src/components/ui/`) ou reste à construire (`Select`, `Status`,
`Timeline`, etc.). Ce contrat ne prescrit ni ne proscrit shadcn/ui comme
mécanisme d'implémentation (`TECHNICAL-STACK-CONTRACT.md` s'en charge)
— il prescrit un comportement attendu, quel que soit le mécanisme qui
le réalise.

### Button

```
PURPOSE          Déclencher une action (§3) — jamais un lien de
                 navigation pure (utiliser EntityLink).
VISUAL_HIERARCHY Variantes alignées sur §3 : primary / contextual /
                 secondary(ghost) / destructive.
STATES           default, hover, focus, active, disabled, loading.
KEYBOARD         Activable par Entrée/Espace, focus visible (§6).
TOUCH            Cible ≥ 44px en FIELD_DENSITY (§7).
MOBILE           Bouton primaire pleine largeur en Sheet/formulaire
                 mobile ; icône seule interdite sans libellé
                 accessible.
MICROCOPY        Verbe métier (§4), jamais "OK"/"Valider" seul.
MOTION           Feedback instantané au clic (§5, 80–120ms).
ERROR            Un bouton d'action qui échoue revient à `default`
                 avec le message d'erreur porté par le composant
                 appelant, jamais un état "erreur" silencieux sur le
                 bouton seul.
ACCESSIBILITY    `aria-label` si icône seule, `aria-busy` en loading.
```

### Input

```
PURPOSE          Saisie d'une donnée atomique.
VISUAL_HIERARCHY Libellé toujours visible (jamais placeholder-only).
STATES           default, focus, filled, error, disabled, readonly.
KEYBOARD         Tab order logique, pas de piège de focus.
TOUCH            Hauteur ≥ 44px en FIELD_DENSITY.
MOBILE           Type de clavier adapté (numérique pour montant/
                 téléphone, jamais clavier texte générique).
MICROCOPY        Message d'erreur inline sous le champ concerné,
                 jamais un toast global pour une erreur de saisie
                 locale.
MOTION           Transition de focus quasi instantanée (§5).
ERROR            Cause + solution directement sous le champ (§4).
ACCESSIBILITY    Libellé lié (`for`/`id`), erreur annoncée
                 (`aria-describedby`).
```

### Select

```
PURPOSE          Choix unique/multiple dans un ensemble fermé.
VISUAL_HIERARCHY Identique visuellement à `Input` au repos ; diffère à
                 l'ouverture (popover, §5 120–180ms).
STATES           default, open, selected, disabled, empty (aucune
                 option).
KEYBOARD         Navigation flèches, sélection Entrée, fermeture Échap.
TOUCH            Liste d'options avec cibles ≥ 44px en FIELD_DENSITY ;
                 bascule vers `Sheet` de sélection plein écran sur
                 mobile si la liste est longue (§8).
MOBILE           Voir TOUCH.
MICROCOPY        Option vide explicite ("Aucun catalogue disponible"),
                 jamais une liste muette.
MOTION           Popover : entrée/sortie easing dédié (§5).
ERROR            Sélection requise non faite signalée au même endroit
                 qu'`Input`.
ACCESSIBILITY    Rôle `listbox`/`combobox` correct, focus géré à
                 l'ouverture/fermeture.
```

### Status

```
PURPOSE          Communiquer un état métier (jamais une action, §4
                 état ≠ action).
VISUAL_HIERARCHY Couleur + libellé texte toujours combinés — jamais la
                 couleur seule (`20` §15, no color-only meaning).
STATES           Un état = une couleur/libellé fixe par objet métier
                 (Devis brouillon/envoyé/accepté ; Facture brouillon/
                 émise/payée/en retard).
KEYBOARD         Non interactif par défaut — si cliquable pour filtrer,
                 devient un composant de filtre distinct, pas un badge
                 déguisé.
TOUCH            Non applicable (non interactif).
MOBILE           Reste visible même en vue compactée (§8) — un état
                 métier n'est jamais sacrifié pour l'espace (`20` §8).
MICROCOPY        Libellé métier explicite, jamais une abréviation
                 technique.
MOTION           Transition de couleur douce au changement d'état
                 (§5, 100–160ms) — jamais un clignotement.
ERROR            Non applicable.
ACCESSIBILITY    Contraste suffisant indépendamment de la couleur de
                 fond (§10).
```

### Table/List

```
PURPOSE          Comparer/parcourir une collection d'objets
                 comparables.
VISUAL_HIERARCHY Colonnes priorisées selon `20` §8 (essentiel
                 d'abord) ; `OFFICE_DENSITY` uniquement (§7) — remplacé
                 par liste de cartes en `FIELD_DENSITY` (§8 replace).
STATES           loading (skeleton, §11), empty (EmptyState §9),
                 error, loaded, filtered.
KEYBOARD         Navigation ligne par ligne, activation Entrée.
TOUCH            Ligne = cible tactile complète en version carte
                 mobile.
MOBILE           Voir Table/List §8 — jamais un tableau scrollable
                 horizontalement comme solution par défaut.
MICROCOPY        En-têtes de colonnes en langage métier, jamais un nom
                 de champ technique.
MOTION           Tri/filtre : transition de réordonnancement des
                 lignes (§5, list insertion/removal).
ERROR            Bandeau d'erreur au-dessus du tableau, lignes déjà
                 chargées conservées si possible.
ACCESSIBILITY    Structure sémantique de tableau réelle en
                 `OFFICE_DENSITY` (pas une grille de `div`).
```

### PageHeader

```
PURPOSE          Ancrer le Context Spine (§2.A) et l'identité de
                 l'écran courant.
VISUAL_HIERARCHY Zone haute persistante, distincte du contenu par
                 espacement plutôt que par bordure lourde.
STATES           avec/sans action globale, avec/sans Context Spine
                 (écrans racine).
KEYBOARD         Non interactif hors ses actions/liens.
TOUCH            Compacté en mobile (§8, hide/reveal).
MOBILE           Voir Context Spine §2.A MOBILE_BEHAVIOR.
MICROCOPY        Titre = nom métier réel, jamais un nom de route.
MOTION           Transition de contexte lors du changement d'objet
                 actif (§5, 220–300ms).
ERROR            Non applicable directement.
ACCESSIBILITY    `h1`/landmark clair pour la navigation assistive.
```

### ContextPanel

```
PURPOSE          Consulter/éditer un objet lié sans perdre le contexte
                 principal — implémentation du "contextual side panel"
                 (§3).
VISUAL_HIERARCHY `PANEL` (§6), jamais `DIALOG` quand le contexte
                 parent doit rester visible.
STATES           closed, opening, open, editing, closing.
KEYBOARD         Échap ferme, focus piégé à l'intérieur pendant
                 l'ouverture.
TOUCH            `replace` par `Sheet` plein écran sous 768px (§8).
MOBILE           Voir TOUCH.
MICROCOPY        Titre du panneau = objet consulté, action de retour
                 explicite.
MOTION           Ouverture/fermeture = panel transition (§5,
                 180–240ms), glisse depuis le bord lié à l'élément
                 déclencheur.
ERROR            Erreur de chargement affichée dans le panneau, jamais
                 par un toast qui masque le contexte parent.
ACCESSIBILITY    `role="dialog"` ou landmark équivalent, focus rendu
                 au déclencheur à la fermeture.
```

### ActionBar

```
PURPOSE          Regrouper les actions d'un écran/objet selon la
                 hiérarchie §3.
VISUAL_HIERARCHY Ordre gauche→droite ou haut→bas : primaire visible en
                 premier, destructif toujours isolé en dernier.
STATES           avec actions disponibles, vide (aucune action
                 possible pour l'état courant — jamais simulée, `20`
                 §5).
KEYBOARD         Tab order suit l'ordre visuel de priorité.
TOUCH            `reposition` ancrée en bas sous 768px (§8).
MOBILE           Voir §2.C Next Action Strip.
MICROCOPY        Voir §4.
MOTION           Voir §2.C MOTION.
ERROR            Action échouée : le bouton concerné revient à
                 `default`, erreur affichée localement (§4).
ACCESSIBILITY    Groupe de boutons annoncé comme tel (`role="group"`
                 si pertinent).
```

### Timeline

```
PURPOSE          Support visuel du Living Dossier (§2.B) — événements
                 métier ordonnés.
VISUAL_HIERARCHY Ligne verticale de repère + un point par événement,
                 typé par icône + couleur neutre (jamais la couleur de
                 statut réservée à `Status`).
STATES           loading (skeleton), empty, loaded, filtré par type.
KEYBOARD         Navigation séquentielle entre événements.
TOUCH            Cible tactile = ligne complète de l'événement.
MOBILE           Colonne unique, défilement naturel (§2.B).
MICROCOPY        Verbe métier au passé (§2.B, §4).
MOTION           Insertion d'un nouvel événement anime (§5,
                 180–240ms).
ERROR            Événement dont le chargement échoue affiché en état
                 dégradé explicite, jamais silencieusement omis.
ACCESSIBILITY    Liste sémantique (`ol`/`ul`), ordre chronologique
                 explicite dans le DOM.
```

### EmptyState

```
PURPOSE          Contexte + action quand une collection est vide (§4).
VISUAL_HIERARCHY Pas d'illustration décorative par défaut dans
                 l'interface opérationnelle (`BRAND-FOUNDATIONS.md`,
                 imagerie réservée à l'onboarding/accueil) ; texte +
                 action primaire suffisent.
STATES           première utilisation (aucune donnée jamais créée) vs
                 résultat de filtre vide — formulations différentes.
KEYBOARD         Action primaire du EmptyState suit §3.
TOUCH            Action ≥ 44px en FIELD_DENSITY.
MOBILE           Compact, une ligne de contexte + un bouton.
MICROCOPY        Voir §4, exemples par objet.
MOTION           Apparition simple, pas d'animation d'entrée notable.
ERROR            Un EmptyState n'est jamais utilisé pour masquer une
                 erreur de chargement réelle — distinct de `ERROR
                 STATE`.
ACCESSIBILITY    Message annoncé aux lecteurs d'écran (`aria-live`
                 poli si apparition dynamique après filtre).
```

### Toast

```
PURPOSE          Confirmation courte d'une action réussie ou échouée
                 qui ne nécessite pas de rester à l'écran.
VISUAL_HIERARCHY Discret, en périphérie, jamais bloquant le contenu
                 principal.
STATES           success, error, info — jamais utilisé pour une
                 confirmation d'opération financière engageante (celle-
                 ci reste visible dans le flux, §5 feedback optimiste).
KEYBOARD         Dismissible au clavier, ne vole jamais le focus actif.
TOUCH            Swipe pour fermer, ne bloque aucune zone d'action
                 principale en bas d'écran mobile (§8 ActionBar).
MOBILE           Positionné pour ne jamais recouvrir le Next Action
                 Strip (§2.C).
MICROCOPY        Résultat concret (§4 SUCCESS), pas générique.
MOTION           Entrée/sortie courte (§5, ≤400ms), auto-dismiss non
                 bloquant.
ERROR            Toast d'erreur persiste plus longtemps que succès,
                 dismissible manuellement.
ACCESSIBILITY    `aria-live="polite"` (ou `assertive` pour erreur
                 bloquante réelle).
```

### Dialog

```
PURPOSE          Confirmation ou tâche courte centrée, interrompt
                 volontairement le flux (destructif, engageant).
VISUAL_HIERARCHY `DIALOG` (§6) — jamais utilisé pour une tâche longue
                 (préférer `Sheet`/`ContextPanel`).
STATES           closed, open, confirming (action en cours).
KEYBOARD         Focus piégé, Échap ferme sauf pendant `confirming`.
TOUCH            `replace` par `Sheet` sous 768px si le contenu dépasse
                 une confirmation simple (§8).
MOBILE           Voir TOUCH.
MICROCOPY        Question directe + conséquence explicite pour le
                 destructif (§4 DESTRUCTIVE).
MOTION           Fondu + léger scale d'entrée (§5, popover/menu
                 120–180ms).
ERROR            Erreur affichée dans le dialog, action de fermeture
                 toujours disponible.
ACCESSIBILITY    `role="alertdialog"` pour le destructif, `role=
                 "dialog"` sinon.
```

### Sheet

```
PURPOSE          Équivalent mobile du `ContextPanel`/`Dialog` complexe
                 — tâche focalisée plein écran ou quasi plein écran.
VISUAL_HIERARCHY Glisse depuis le bord (bas en mobile), couvre le
                 contenu sans le détruire (retour préservé, §11).
STATES           closed, opening, open, closing.
KEYBOARD         Focus piégé pendant l'ouverture (usage bureau
                 occasionnel).
TOUCH            Zone de fermeture (glisser vers le bas) en plus d'un
                 bouton explicite.
MOBILE           Mode par défaut pour toute édition complexe sous
                 768px (§8).
MICROCOPY        Titre clair de la tâche en cours.
MOTION           Panel transition (§5, 180–240ms), glisse depuis le
                 bord d'origine.
ERROR            Erreur affichée en tête du Sheet, contenu déjà saisi
                 préservé (§11 preserve form state).
ACCESSIBILITY    Focus rendu à l'élément déclencheur à la fermeture.
```

### MoneyDisplay

```
PURPOSE          Rendu cohérent de tout montant — implémentation de
                 §2.E Financial Language.
VISUAL_HIERARCHY Chiffres tabulaires, alignement droit en tableau,
                 nature du montant (HT/TTC) toujours explicite à
                 proximité immédiate.
STATES           positif, négatif (avoir), en attente (acompte non
                 confirmé) — traitement visuel distinct pour chacun.
KEYBOARD         Non interactif (affichage seul).
TOUCH            Non applicable.
MOBILE           Montant total/reste dû toujours visible sans scroll
                 (§2.E).
MICROCOPY        Format `450,00 € TTC`, jamais un nombre nu.
MOTION           Recalcul anime la valeur (§2.E, §5, 100–160ms).
ERROR            Montant impossible à calculer affiché comme état
                 distinct explicite ("—" avec explication), jamais 0€
                 par défaut silencieux.
ACCESSIBILITY    Valeur et devise lues ensemble par lecteur d'écran.
```

### Date/Time

```
PURPOSE          Rendu cohérent de toute date/heure métier (RDV,
                 échéance, historique).
VISUAL_HIERARCHY Format relatif pour le récent ("Aujourd'hui 14h"),
                 absolu au-delà d'un seuil à définir visuellement.
STATES           passé, aujourd'hui, futur — traitement visuel
                 distinct pertinent pour Planning (§2.D).
KEYBOARD         Non interactif sauf en tant que déclencheur de
                 sélecteur de date (→ voir `Select`).
TOUCH            Sélecteur de date/heure natif mobile privilégié sur
                 terrain (rapidité, §1 field ergonomics).
MOBILE           Format compact, jamais un timestamp technique.
MICROCOPY        Français, jamais ISO brut affiché à l'utilisateur.
MOTION           Non applicable en affichage seul.
ERROR            Date invalide signalée au niveau du champ de saisie
                 (`Input`), pas au niveau de l'affichage.
ACCESSIBILITY    `<time datetime>` sémantique pour tout affichage de
                 date.
```

### EntityLink

```
PURPOSE          Rendre navigable une relation structurante entre
                 objets — implémentation de `20` §4 (Relation-to-UI
                 Contract).
VISUAL_HIERARCHY Distinct visuellement d'un `Button` (texte de lien,
                 pas un bouton plein) — jamais confondu avec une
                 action.
STATES           default, hover/focus, visité (si pertinent),
                 indisponible (objet supprimé/inaccessible).
KEYBOARD         Focusable, activation Entrée, comportement de lien
                 standard.
TOUCH            Cible ≥ 44px en FIELD_DENSITY malgré le rendu texte.
MOBILE           Utilisé dans Context Spine (§2.A) et Living Dossier
                 (§2.B) pour la navigation contextuelle.
MICROCOPY        Nom métier réel de l'objet cible, jamais "Voir plus".
MOTION           Aucune animation propre — hérite de la transition de
                 contexte de destination (§5).
ERROR            Objet cible inaccessible (supprimé, permission) rendu
                 en état `indisponible` explicite, jamais un lien mort
                 silencieux.
ACCESSIBILITY    Libellé de lien explicite pour lecteur d'écran (pas
                 "cliquez ici").
```

---

## 10. Accessibility Quality Bar

Applique et opérationnalise `20` §15 (principes) — ce document ajoute
les seuils chiffrés que `20` ne fixe pas volontairement.

| Critère | `WCAG_MINIMUM` | `SUPORDO_FIELD_TARGET` |
|---|---|---|
| Navigation clavier | Toute action accessible sans souris | Identique — non négociable, aucun écart terrain |
| Focus visible | Indicateur de focus présent | Indicateur de focus renforcé (contraste élevé, visible en extérieur) |
| Contraste texte | AA — 4.5:1 texte normal, 3:1 grand texte | AA sur tout texte, viser AAA (7:1) sur les actions primaires et montants critiques — extérieur/soleil (`20` §9) |
| Taille de cible | 24×24px CSS minimum (WCAG 2.2 AA) | 44–48px minimum sur toute action principale en `FIELD_DENSITY` (§7) |
| Zoom | Contenu utilisable jusqu'à 200% de zoom sans perte | Identique, testé en priorité sur les écrans Devis/Facture (denses) |
| Réduction de mouvement | Respect de `prefers-reduced-motion` | Identique (§5) |
| UI persistante (headers/bars sticky) | Ne doit jamais masquer l'élément focus actif | Identique — vérifié explicitement à chaque révision d'ActionBar/PageHeader |
| Sens porté par la couleur | Jamais la seule information (WCAG 1.4.1) | Identique, appliqué systématiquement à `Status` (§9) |

[ARCHITECTURE_DECISION] `SUPORDO_FIELD_TARGET` est toujours au moins
aussi strict que `WCAG_MINIMUM` — jamais un compromis en dessous.
Lorsqu'un composant ne précise pas de cible spécifique, `WCAG_MINIMUM`
s'applique par défaut.

---

## 11. Perceived Performance

[PRINCIPLE] **Skeleton vs spinner** : skeleton pour tout chargement de
contenu structurel identifiable à l'avance (liste, fiche) — communique
la forme du résultat attendu. Spinner réservé aux actions courtes sans
structure prévisible (soumission de formulaire).

[PRINCIPLE] **Feedback immédiat** : toute interaction reçoit un
accusé visuel en moins de 100ms (§5 instant feedback), indépendamment
du temps de réponse réel du serveur.

[PRINCIPLE] **Transitions qui préservent le contexte** : un changement
d'écran ne doit jamais donner la sensation d'un rechargement complet —
le Context Spine (§2.A) et les éléments stables restent visuellement
continus pendant la transition (§5 context/layout transition).

[PRINCIPLE] **Pas de saut de mise en page** : tout espace dont le
contenu va se charger est réservé à l'avance (dimensions connues ou
skeleton de taille équivalente) — aucun contenu ne doit décaler ce qui
est déjà affiché.

[PRINCIPLE] **Position de défilement préservée** : un retour en arrière
(fermeture de panneau, navigation retour) restaure la position de
défilement précédente — jamais un retour en haut de liste imposé.

[PRINCIPLE] **État de formulaire préservé** : une saisie en cours ne
doit jamais être perdue lors d'une interruption non intentionnelle
(navigation accidentelle, perte de focus, latence réseau) — particuliè-
rement critique en usage terrain (`04` §4). Rejoint le gap technique
déjà identifié dans `TECHNICAL-BASELINE.md` sur l'atomicité de
`saveQuote` — non recopié ici, référence uniquement.

[PRINCIPLE] **Éviter la sensation de rechargement de page complète** :
toute navigation interne reste dans le modèle SPA déjà acté par
`TECHNICAL-STACK-CONTRACT.md` — aucune transition ne doit imiter
visuellement un rechargement de document complet (flash blanc,
réinitialisation totale du scroll/layout).

---

## 12. Visual QA Contract

Étend `20` §16 (Validation Contract) et `20` §10 (Responsive Contract)
avec les exigences propres à l'exécution visuelle — ne les redéfinit
pas.

[ARCHITECTURE_DECISION] Toute tranche UI importante doit être auditée
réellement dans le navigateur, avec de vraies données `DEMO` (pas des
placeholders), sur les quatre largeurs de validation de `20` §10
(`360` · `390` · `768` · desktop) — desktop étant vérifié à `1280`
comme extension propre à ce document (§8), jamais une largeur imposée
par `20` lui-même.

Preuve exigée pour chaque tranche concernée :

```
SCREENSHOTS            — une capture par largeur, par état pertinent
                          (rempli, vide, erreur).
WORKFLOW_RECORDING      — enregistrement du parcours réel (clics,
                          navigation), pas seulement des captures
                          statiques — application de `20` §16 (vrais
                          clics, vraie navigation).
OVERFLOW_CHECK          — absence de débordement horizontal accidentel
                          à chaque largeur (`20` §10).
FOCUS_CHECK             — ordre et visibilité du focus clavier
                          vérifiés à chaque largeur pertinente.
LOADING_ERROR_EMPTY     — les trois états vérifiés visuellement, pas
                          seulement déclarés dans le code.
MICROCOPY_REVIEW        — conformité aux règles §4 (verbes métier,
                          erreur = cause+conséquence+solution, etc.).
MOTION_REVIEW           — conformité à §5, y compris test manuel de
                          `prefers-reduced-motion` activé.
```

[ARCHITECTURE_DECISION] Une tranche n'est jamais considérée visuellement
validée sur la seule base d'un test de rendu composant (Vitest/RTL) —
rappel direct de `20` §16, appliqué explicitement ici à la couche
visuelle et au motion.

---

## 13. Benchmark Principles

Étudiés sans jamais copier — chaque ligne distingue explicitement ce
qui est retenu de ce qui est écarté. Ce registre **approfondit** les
décisions d'adoption déjà actées en §3 (Interaction Model) — il n'y
revient pas, il les justifie (`WHY_GOOD`) et les étend à deux
références supplémentaires hors interaction pure (Material, Apple HIG).
Pour la décision elle-même, §3 fait foi ; pour le raisonnement complet,
cette section fait foi.

### Linear

```
REFERENCE            Densité d'information, hiérarchie typographique
                      stricte, actions contextuelles au survol, command
                      menu omniprésent, preview d'objet lié.
WHY_GOOD              Permet un travail rapide sans jamais masquer
                      l'information nécessaire à la décision —
                      cohérent avec §1 density without clutter.
SUPORDO_ADAPTATION    Densité en `OFFICE_DENSITY` (§7), `ContextPanel`
                      et peek (§3), hiérarchie typographique §6 —
                      jamais l'esthétique monochrome/dark-first comme
                      identité.
WHAT_NOT_TO_COPY      Absence quasi totale de pensée mobile/terrain
                      (produit desktop de power-users) ; identité
                      visuelle (typographie, palette, ton) — SUPORDO a
                      la sienne (`BRAND-FOUNDATIONS.md`).
```

### Attio

```
REFERENCE            Navigation d'espace de travail, command palette,
                      enregistrements contextuels reliés entre eux.
WHY_GOOD              Les relations entre objets (personnes,
                      entreprises) restent navigables sans jamais
                      perdre le fil — proche de `20` §4 Relation-to-UI.
SUPORDO_ADAPTATION    `EntityLink` (§9), Context Spine (§2.A), Living
                      Dossier (§2.B) comme équivalents SUPORDO de la
                      navigation relationnelle.
WHAT_NOT_TO_COPY      Modèle générique "CRM de contacts" — SUPORDO
                      n'est pas un CRM de contacts, c'est un mini-ERP
                      terrain ; ne pas importer sa structure d'écran
                      objet-par-objet sans le filtre des signatures §2.
```

### Raycast

```
REFERENCE            Modèle d'action, vitesse perçue, découvrabilité
                      clavier des commandes.
WHY_GOOD              Chaque action est atteignable en un minimum de
                      gestes pour l'utilisateur qui la connaît déjà —
                      cohérent avec §1 perceived speed.
SUPORDO_ADAPTATION    Command menu comme accélérateur optionnel
                      uniquement (§3) — jamais le chemin principal, à
                      la différence de Raycast où c'est le produit
                      entier.
WHAT_NOT_TO_COPY      Le clavier comme mode d'interaction par défaut —
                      inadapté à l'usage terrain tactile à une main
                      (`20` §9 TERRAIN), qui reste le cas d'usage
                      prioritaire de SUPORDO.
```

### Material / Android Adaptive

```
REFERENCE            Doctrine `reflow`/`reveal`/`hide`/`replace`/
                      `reposition`/`split` pour la composition
                      adaptive multi-écran.
WHY_GOOD              Vocabulaire précis pour décrire un changement de
                      composition sans se limiter à "ça rétrécit" —
                      directement repris comme vocabulaire de §8.
SUPORDO_ADAPTATION    §8 utilise explicitement ce vocabulaire pour les
                      quatre seuils SUPORDO (360/390/768/1280).
WHAT_NOT_TO_COPY      Le langage visuel Material lui-même (élévation
                      Material, ripple, iconographie Google) — SUPORDO
                      garde sa propre échelle d'élévation (§6, plate
                      par défaut) et sa propre iconographie.
```

### Apple HIG

```
REFERENCE            Motion porteur de sens, préservation du contexte
                      spatial lors des transitions, exigence de
                      finition ("craft") sur chaque micro-détail.
WHY_GOOD              Une transition qui respecte l'origine spatiale
                      d'un élément renforce la compréhension du
                      changement d'état — directement repris en §5
                      (panel transition "vient de" l'élément
                      déclencheur).
SUPORDO_ADAPTATION    Doctrine de motion §5 (le motion = information),
                      transitions de `ContextPanel`/`Sheet` ancrées
                      spatialement à leur déclencheur.
WHAT_NOT_TO_COPY      Le niveau de raffinement visuel spécifique à
                      l'écosystème Apple (skeuomorphisme résiduel,
                      matériaux "verre") — hors de portée et hors sujet
                      pour un CRM terrain professionnel.
```

---

## 14. Décisions ouvertes & valeurs à valider

[OPEN] Toute valeur numérique marquée `SUPORDO_BASELINE_TO_VALIDATE`
dans ce document (échelle de motion §5, échelles typographique/
spacing/icon §6) — à confirmer lors du premier audit visuel réel (§12)
sur une tranche UI existante avant d'être considérée stable.

[OPEN] Forme de navigation (sidebar/topbar/rail/bottom-bar) — non
tranchée par `20` §11 ni par ce document ; les trois prototypes non
documentés (`src/prototypes/concept-1-rail`, `concept-2-command`,
`concept-3-lifecycle`) identifiés par l'audit du 2026-09-25 sont une
matière d'expérimentation possible pour instruire ce choix, pas une
décision actée — à évaluer contre les critères de `20` §11 avant tout
arbitrage.

[OPEN] Zone tablette (768–1279px) comme troisième mode de densité à
part entière (`20` §9 l'exige comme contexte pensé séparément) vs.
simple zone de transition `OFFICE_DENSITY`↔`FIELD_DENSITY` — §7/§8
décrivent volontairement un dégradé progressif sans trancher, en
attente de validation terrain (§12).

[OPEN] Sens de la relation Devis↔Intervention (`16` §6 Q8/Q17/Q18,
déjà `OPEN` dans `20` §18) — les signatures Context Spine (§2.A) et
Living Dossier (§2.B) restent valides quel que soit le sens retenu,
mais leur contenu exact en dépend.

**Règle d'évolution** : identique à `20` §18 — toute modification doit
distinguer un raffinement de `PRINCIPLE` déjà canonique (sans
arbitrage), une nouvelle `SUPORDO_DECISION` (arbitrage PO requis,
tracée dans `0007`/`16`), ou une `ARCHITECTURE_DECISION` dérivée d'un
invariant déjà acté. Une valeur `SUPORDO_BASELINE_TO_VALIDATE` ne
devient un invariant stable qu'après preuve visuelle réelle (§12) — pas
par simple ancienneté dans ce document.
