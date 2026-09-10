# Journal méthodologique — exploitation du corpus concurrentiel

Note interne. **Ne pas placer sous les yeux d'un agent qui code.**
Sert à arbitrer de futures analyses, pas à construire SUPORDO.

---

## Ce que le corpus a réellement rendu

Cinq missions d'exploitation, après treize productions LIGHT
(2 510 documents, 12 éditeurs).

| Mission | Coût observé | Utilité pour décider |
|---|---:|---|
| Pilote onboarding — 6 éditeurs | non relevé | moyenne |
| Pilote propagation — 7 éditeurs, transversal | 9,25 $ | faible |
| Devis 3A — naissance | 7,89 $ | bonne |
| Devis 3B — cycle de vie | 8,14 $ | bonne |
| Devis 3C — sorties et propagation | non relevé | bonne |

Les coûts non relevés ne sont pas estimés : ils n'ont pas été observés.

---

## Trois leçons

### 1. Découper par objet et par étape, jamais par phénomène

La passe transversale « propagation et irréversibilité » couvrait sept
éditeurs et six domaines en une fois. Elle a coûté le plus cher et rendu le
moins.

Les trois passes étroites sur le devis — naissance, cycle, sorties — ont
chacune rendu davantage. Et la troisième a **corrigé** la passe transversale
sur le régime devis→facture chez quatre éditeurs (`3C` §25).

La largeur produit des règles vraies mais dispersées, parfois mal classées.
La profondeur trouve ce que la largeur manque.

### 2. Le corpus documente les exceptions, pas la norme

Un centre d'aide existe pour expliquer ce qui coince. Il décrit l'avoir,
l'avenant, la facture de situation — et saute le cas standard.

Exemple net : `devis → facture simple`, sans acompte ni situation, n'est
documenté nulle part alors que c'est le cas le plus fréquent.

Conséquence : toute extraction supplémentaire rendra des exceptions. Ne pas
attendre du corpus qu'il décrive un comportement normal.

### 3. Le coût vient de la longueur de session, pas du parallélisme

Diagnostic de l'outil sur 24 heures : **75 % de l'usage à plus de 150 k de
contexte**, contre 11 % attribués aux sous-agents (`general-purpose` 9 %,
`fork` 2 %).

Le levier n'est donc pas d'interdire les sous-agents mais de **plafonner le
volume lu** — et donc la taille du contexte.

---

## Réglages pour une future mission d'extraction

- **Plafonner dans le prompt, pas dans l'agent.** « Au plus 12 documents par
  éditeur, dis lesquels tu as écartés. » Laissé libre, un agent se fixe 25.
- **Couvrir plusieurs familles avant de conclure au rendement décroissant** —
  un spécialiste BTP, un généraliste, un ERP, un léger artisan. L'ordre de
  lecture détermine sinon artificiellement la saturation.
- **La saturation est un indicateur, jamais un STOP automatique.**
- **Filtrer par `objet_principal`** (≈ 16 % de rétention sur « devis »),
  jamais par `regle_ou_condition` seul (63 %) ni `transition_objet` seul
  (53 %).
- **Prévoir un mode de repli** pour les corpus à arborescence plate, où la
  présélection par rubrique échoue (cas Obat).
- **Écrire le critère de rendement avant la lecture**, et ne pas le modifier
  après. Décision 0006 : ne jamais choisir un seuil après avoir vu la
  distribution.

---

## Ce qui n'a pas été fait, et pourquoi

- **Corpus marketing** — environ 3 700 pages collectées, aucune analysée. La
  décision 0004 exige un instrument distinct, avec pilote et arbitrage. Ce
  chantier n'est pas ouvert.
- **Sous-domaines Obat** — `travaux.obat.fr` (annuaire de mise en relation),
  `education.obat.fr`, `partenariats.obat.fr`. Identifiés, répondent en 200,
  non collectés. Suggèrent un modèle d'acquisition par apport d'affaires,
  non vérifié.
- **Six corpus historiques** — Axonaut, Costructor, InterFast, OpenFire
  Zendesk, Sellsy, Vertuoza ont été collectés par une méthode antérieure à
  `collecte.py`. Leur couverture individuelle est **non déterminable**. À
  rappeler avant toute conclusion comparative de profondeur fonctionnelle.
- **Tolteck et Leobati** — non collectables, blocages techniques documentés
  dans `COUVERTURE.md`. Le segment artisan léger est donc amputé de deux
  acteurs.

---

## Où s'arrêter

Le corpus a rendu ce qu'il pouvait rendre sur le devis. Les six questions
restées ouvertes (`0007` section O) ne sont pas des trous d'information :
ce sont des **choix de produit**, que le marché lui-même ne tranche pas.

Les questions de terrain — régime réel de travail, où naît l'information
après une visite, ce qui est ressaisi, comment on retrouve une affaire de
trois ans, ce qui a cassé à la première embauche — ne se résolvent par aucune
analyse documentaire. Décisions 0004 et 0006.
