# Registre des cas problématiques — CP-1 à CP-18

> Ce registre est un index de travail pour l'arbitrage post-Pilotes A+B.
> Il ne constitue ni une nouvelle analyse ni une proposition de V3.

Les descriptions détaillées restent dans leur mini-audit d'origine :
`mini-audit-V2.md` §10 pour CP-1 à CP-13, `mini-audit-B.md` §4 pour
CP-14 à CP-18. Aucun CP n'est ici reformulé, fusionné ni résolu.

---

## Définition des statuts

**structurel** — défaut démontré du contrat affectant un axe central, ou
empêchant la représentation fiable d'un phénomène pertinent.

**récurrent** — même problème observé dans plusieurs cas, sans blocage
structurel établi.

**isolé** — une seule occurrence documentée.

**non testé** — cas non réellement exercé dans A ou B.

Ces définitions ne font pas dépendre `structurel` du nombre
d'occurrences. Une occurrence unique peut suffire à démontrer qu'un
champ ne sait pas représenter un phénomène.

## Définition des priorités d'arbitrage

**1 — bloque une hypothèse.** Sans correction, une hypothèse ne peut pas
être testée.

**2 — pollue une hypothèse.** L'hypothèse reste testable, mais les
données qui la servent portent des qualifications fausses.

**3 — structurel sans blocage.** Défaut démontré, aucune hypothèse
empêchée ni polluée.

**4 — à réexaminer plus tard.**

`Sert` dit ce que la correction apporte ; `Priorité` dit dans quel ordre
arbitrer. Les deux colonnes ne se déduisent pas l'une de l'autre.

---

| CP | Énoncé court | Origine | Occurrences cumulées A+B | Sert | Statut | Priorité |
|---|---|---|---:|---|---|:-:|
| CP-1 | `parcours.origine` et `parcours.nature` sont scalaires alors que des articles documentent plusieurs valeurs | mini-audit-V2 | 4 | fidélité factuelle | récurrent | 4 |
| CP-2 | `nature` n'a pas de valeur pour une activité commerciale pure ; produit de faux `inconnu` | mini-audit-V2 | 7 | fidélité factuelle | récurrent | 4 |
| CP-3 | `canal` n'a pas de valeur pour un appel téléphonique | mini-audit-V2 | 1 | fidélité factuelle | isolé | 4 |
| CP-4 | une signature client sans effet d'état documenté n'entre dans aucune `forme` | mini-audit-V2 | 5 | fidélité factuelle | structurel | 3 |
| CP-5 | une automatisation sans second rôle n'a pas d'emplacement dans `interactions` | mini-audit-V2 | 2 | fidélité factuelle | récurrent | 4 |
| CP-6 | `statut_observation` n'a pas de valeur pour une destruction volontaire | mini-audit-V2 | 1 | fidélité factuelle | isolé | 4 |
| CP-7 | une non-propagation entre deux objets ou systèmes n'est aucun des trois types de rupture | mini-audit-V2 | 4 | H1 | structurel | 2 |
| CP-8 | suppression puis recréation : entre `ressaisie` et `reconstruction_contexte` | mini-audit-V2 | 3 | fidélité factuelle | récurrent | 4 |
| CP-9 | emplacements de configuration codés comme acteurs | mini-audit-V2 | 2 | fidélité factuelle | récurrent | 4 |
| CP-10 | une interaction sans mécanisme est indiscernable d'une interaction substantielle en cardinalité | mini-audit-V2 | 3 | fidélité factuelle | récurrent | 4 |
| CP-11 | une règle portant sur plusieurs objets n'a qu'un `objet_concerne` | mini-audit-V2 | non comptabilisé | fidélité factuelle | récurrent | 4 |
| CP-12 | `objet_source` et `objet_resultat` ne sont pas normalisés ; le graphe des objets n'est pas calculable | crash-test d'utilité, consigné dans mini-audit-V2 | non comptabilisé | H1 | structurel | 1 |
| CP-13 | régression `job_to_be_done`, présent en V1 et non repris en V2 | crash-test d'utilité, consigné dans mini-audit-V2 | non comptabilisé | fidélité factuelle | structurel | 4 |
| CP-14 | le temps n'existe pas dans le modèle de rupture : aucun type ne décrit une information qui expire | mini-audit-B | 1 | H1 | structurel | 2 |
| CP-15 | un canal unique dont l'audience bascule message par message n'est pas représentable | mini-audit-B | 1 | D1 | isolé | 4 |
| CP-16 | une rupture assumée et motivée est indiscernable d'une lacune | mini-audit-B | 1 | H1 | structurel | 2 |
| CP-17 | un acteur appartenant à plusieurs périmètres simultanément n'est pas représentable | mini-audit-B | 1 | fidélité factuelle | isolé | 4 |
| CP-18 | une interaction conditionnée par un seuil, un état, un rôle, une durée, un abonnement, un réglage ou une donnée n'est pas représentable | mini-audit-B | 7 formes distinctes documentées en B | H3 | structurel | 1 |

---

## Notes de lecture

**Sur la colonne `Sert`.** Quatre affectations seulement sont établies par
la décision 0005 : CP-12 → H1, CP-7 / CP-14 / CP-16 → H1 (refonte des
types de rupture), CP-18 → H3, CP-4 → fidélité factuelle. CP-15 est
rattaché à D1 parce que le phénomène concerné — un fil dont l'audience
bascule par message — figure explicitement dans les preuves de D1 en
0005. Les autres CP sont marqués `fidélité factuelle` faute d'un lien
démontré par un audit : ils rendent l'extraction plus fidèle sans servir
un axe de recherche particulier. Ce marquage par défaut est un constat
d'absence de démonstration, pas une évaluation de leur importance.

**Sur la colonne `Occurrences`.** Les nombres reprennent les comptages des
mini-audits. `non comptabilisé` signifie que les audits ne permettent pas
un comptage fiable :

- CP-11 : les deux audits écrivent « plusieurs » sans dénombrer.
- CP-12 et CP-13 : défauts de schéma présents sur les 40 fichiers, non
  dénombrables par occurrence d'article.

CP-18 ne porte pas un nombre d'occurrences mais **sept formes distinctes
de conditionnalité** relevées dans le §6 du mini-audit B. Aucun comptage
exhaustif des occurrences de chaque forme n'existe dans les audits.

---

## Relecture des statuts à l'aune des définitions

Les définitions ci-dessus ne font pas dépendre `structurel` de la
récurrence. Cette relecture a produit **trois requalifications**.

### CP-14 : isolé → structurel

Une seule péremption documentée suffit à démontrer que les trois valeurs
de `ruptures.type` ne représentent pas ce phénomène. Le codage forcé en
`reconstruction_contexte` n'est pas une approximation neutre : il **affirme
un type de rupture faux** sur le champ qui porte l'essentiel des preuves
de H1. Une seconde occurrence n'apprendrait rien de plus sur le défaut du
contrat.

### CP-16 : isolé → structurel

Même raisonnement. `statut_observation: rupture_documentee` posé sur une
non-automatisation revendiquée et motivée par l'éditeur affirme une
lacune là où la source documente un choix de conception. Faux positif sur
un champ central de H1.

### CP-18 : récurrent → structurel

La décision 0005 a érigé la coordination conditionnelle en hypothèse H3.
Un défaut du contrat qui empêche de représenter la conditionnalité rend
H3 non testable : c'est un « défaut démontré du contrat affectant un axe
central » au sens de la définition. Le statut `récurrent` de la première
version reflétait un comptage de fréquence, non un effet sur un axe.

### Ce que je n'ai pas promu, et pourquoi

Quatre CP à occurrence unique restent `isolé`. Le critère que j'ai
appliqué : le codage forcé produit-il une **affirmation fausse** sur le
champ, ou seulement un **trou** ?

- **CP-3** — `canal: inconnu` sur un appel téléphonique laisse un trou
  signalé, il n'affirme rien de faux. Et l'ajout d'une valeur d'énumération
  n'engage aucun axe.
- **CP-6** — `non_determinable` sur une destruction volontaire est un
  aveu d'incertitude, pas une qualification fausse. Le phénomène — la
  suppression délibérée d'un règlement — n'a pas été montré pertinent
  pour un axe central.
- **CP-15** — le dédoublement d'un canal unique en deux interactions
  gonfle une cardinalité ; c'est une distorsion de comptage, pas un faux
  label sur le champ qui porte les preuves de H1. Rattaché à D1, qui n'est
  pas un axe autonome.
- **CP-17** — même nature : `perimetre` scalaire perd une appartenance
  multiple sans affirmer une appartenance fausse.

Ces quatre décisions sont des arbitrages de ma part, pas des constats
d'audit. Elles sont réversibles si le corpus étendu les contredit.

**CP-13 reste `structurel` mais en priorité 4.** Un défaut de contrat
affectant les 40 fichiers ne bloque ni ne pollue aucune hypothèse : il
dégrade l'utilité de lecture des YAML. Le décalage entre son statut et sa
priorité est délibéré et illustre que les deux colonnes ne se déduisent
pas l'une de l'autre.

**CP-18 n'a pas été recherché dans le Pilote A.** Ses sept formes
proviennent toutes des dix articles du Pilote B, échantillon biaisé par
construction. Sa promotion en `structurel` tient à son effet sur H3, non
à sa fréquence, et ne préjuge pas de sa prévalence dans le corpus étendu.
