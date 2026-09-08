# Test de sensibilité LIGHT sur H3 — 6 contrôles positifs

**Ce n'est pas le crash-test H3 complet**, qui n'a pas eu lieu faute de
contrôles dans le périmètre LIGHT (voir `pre-test-light-h3.md`). Ce fichier
ferme uniquement la question de sensibilité restée ouverte à l'issue du
pré-test.

## Question testée

H3 — coordination conditionnelle : « Les champs LIGHT permettent-ils
d'identifier, sans relire l'ensemble du corpus source, les documents
susceptibles de contenir des mécanismes où une action, une validation, une
transmission ou un comportement dépend d'une condition métier ? »

Ici, restreinte à la sensibilité seule : les 6 documents portant des
contrôles H3 démontrés indépendamment de LIGHT obtiennent-ils
`regle_ou_condition = oui` une fois codés selon SCHEMA-LIGHT.md ?

## Provenance des positifs et des contrôles

6 documents, 7 contrôles, gelés dans `pre-test-light-h3.md` à partir de
`mini-audit-B.md` §6 (lecture V2/V3 antérieure et indépendante de LIGHT) —
aucun dérivé du contenu d'un fichier `light-*.md`.

## Règle de sélection gelée

Filtre primaire, gelé avant codage : `regle_ou_condition = oui`. Vue
secondaire descriptive, non décisive pour H3 : `regle_ou_condition = oui`
ET (`roles` ou `permissions` dans `capacites_transverses`).

## NOTE OBLIGATOIRE — ordre d'exécution et amorçage

**L'ordre « coder d'abord, révéler ensuite » n'a pas pu être tenu.** J'ai
rédigé la table chemin → phénomène de `pre-test-light-h3.md` au tour
précédent de cette même conversation ; je connaissais donc déjà, avant de
coder les 6 documents, le phénomène H3 attendu dans chacun (seuil
InterFast, durée Vertuoza, etc.). Je l'ai signalé avant de commencer le
codage plutôt que de prétendre une neutralité que je n'avais pas.

Conséquence à en tirer, telle que fixée avant le codage : **un résultat
élevé sous amorce ne démontre pas la sensibilité de LIGHT** — il peut
refléter le fait que je savais quoi chercher plutôt qu'une propriété de
l'instrument. **Un raté sous amorce, en revanche, aurait démontré une
limite réelle**, puisqu'il serait allé à l'encontre du biais attendu. Le
résultat obtenu ci-dessous (6/6) doit être lu à la lumière de cette
asymétrie : il est **cohérent avec** une bonne sensibilité, mais il ne la
**prouve pas** de façon indépendante.

## Résultats document par document

| # | Chemin | Phénomène(s) H3 historique(s) | `regle_ou_condition` LIGHT | Sélectionné |
|---|---|---|---|---|
| 1 | `inter-fast/finances/activer-la-validation-des-commandes-fournisseurs.md` | seuil chiffré (500 €) ; rôle (Validateur exempté) ; abonnement (Business) | oui | OUI |
| 2 | `inter-fast/operations/creer-un-chantier-app-web.md` | état de l'objet (devis Accepté → Opérations) | oui | OUI |
| 3 | `inter-fast/equipe/inviter-et-gerer-un-profil-sous-traitant.md` | rôle (sous-traitant sans accès Web) | oui | OUI |
| 4 | `inter-fast/operations/consulter-et-utiliser-le-fil-d-activite-du-chantier.md` | abonnement (fil de chantier « Pro ») | oui | OUI |
| 5 | `vertuoza/.../pourquoi-je-ne-peux-pas-recuperer-certaines-photos-...md` | durée (20 jours) | oui | OUI |
| 6 | `vertuoza/gestion-de-chantier/suivi-de-chantier-gestionnaire.md` | réglage à la création (avancement interne) ; présence de donnée (responsable de réclamation) | oui | OUI |

```
DOCUMENTS_POSITIFS_SELECTIONNES = 6/6
CONTROLES_H3_COUVERTS_PAR_DOCUMENT_SELECTIONNE = 7/7
```

**Avertissement, reproduit tel qu'exigé** : LIGHT code le document, pas
chaque phénomène. Le document 1 porte 3 phénomènes (seuil, rôle,
abonnement) et le document 6 en porte 2 (réglage, donnée) ; chacun
n'obtient qu'une seule valeur `regle_ou_condition`. Un document
sélectionné et couvrant plusieurs contrôles ne démontre en aucun cas que
LIGHT représente séparément chaque forme de conditionnalité qu'il
contient — `regle_ou_condition = oui` ne dit pas laquelle des 7 formes
(montant, durée, état, rôle, abonnement, réglage, donnée) est en cause,
ni combien. 7/7 est une mesure de présélection au niveau document, jamais
une mesure de détection sémantique fine.

## Faux négatifs

**Aucun.** Les 6 documents obtiennent `regle_ou_condition = oui` ; aucun
`non` ni `inconnu` observé sur ce lot.

## Vue secondaire (descriptive uniquement)

`roles` ou `permissions` apparaît dans `capacites_transverses` de 4
documents sur 6 (#1, #2, #3 ; absent de #4, #5, #6 qui portent
respectivement une conditionnalité d'abonnement, de durée et de
réglage/donnée). Confirme, sur ce micro-lot, l'avertissement déjà posé au
pré-test : cette vue n'aurait pas capturé les documents #4, #5 et #6 —
soit 3 des 7 formes de conditionnalité (durée, abonnement, réglage à la
création, présence de donnée). Non utilisée pour le verdict.

## Verdict de sensibilité

```
LIGHT_H3_SENSIBILITE_CONFIRMEE
```

Fait observé : les 6 documents positifs connus sont tous sélectionnables
par le filtre primaire, sans défaut substantiel observé sur ce lot.

**Portée réelle de ce verdict, à ne pas dépasser** : en raison de
l'amorçage documenté ci-dessus, ce résultat établit que LIGHT n'a *pas
échoué* sur les cas connus quand l'agent savait où regarder — il
n'établit pas, de façon indépendante, que LIGHT aurait détecté ces mêmes
mécanismes à l'aveugle. Le résultat est **nécessaire mais non suffisant**
pour une confirmation forte. Un test à l'aveugle réel (agent sans mémoire
de la table chemin → phénomène, ou lecture des 22 documents restants
d'`extracted/` sans savoir lesquels sont positifs) resterait nécessaire
pour une preuve indépendante de sensibilité.

## Rappel du pouvoir discriminant

Établi au pré-test, non refait ici : filtre primaire global
`regle_ou_condition = oui` = **276/439 = 62,9 %** du corpus LIGHT complet
(pilote + Costructor + Axonaut + ProGBat) — réduction faible à nulle.

## Décision finale sur LIGHT pour H3

A — Sensibilité : confirmée sur les cas connus, avec la réserve
d'amorçage ci-dessus (ni infirmée, ni prouvée indépendamment).
B — Pouvoir discriminant : faible (62,9 % retenus).

```
LIGHT_EST_IL_UTILE_COMME_CARTE_DE_PRESELECTION_H3 = PARTIELLEMENT
```

Logique appliquée telle que fixée avant le test : une sensibilité qui
semble bonne mais une discrimination faible signifient que LIGHT signale
largement des documents porteurs de règles, sans être à lui seul une carte
H3 suffisamment sélective — exactement le cas prévu par la mission pour
`PARTIELLEMENT`. Aucune conclusion plus forte n'est tirée.

## Conséquence minimale

```
A. LIGHT reste utile comme cartographie générale du corpus, mais H3 devra
   être sélectionné ensuite par une lecture ou une extraction ciblée, ou
   par d'autres indices.
```

Justification : le filtre primaire seul ne réduit pas assez l'espace
(62,9 % retenus) pour servir de présélection H3 autonome, même si les cas
connus n'y échappent pas. Cette décision ne porte que sur H3 : elle ne
remet en cause ni LIGHT comme cartographie générale, ni les productions
déjà réalisées, ni V3, ni le corpus, ni H3_REAL_WORLD.
