# Registre des cas problématiques — CP-1 à CP-22

> Ce registre est un index de travail pour l'arbitrage post-Pilotes A+B,
> complété après le crash-test externe de V3 (Analysis C). Il ne
> constitue ni une nouvelle analyse ni une proposition de V4.

Les descriptions détaillées restent dans leur document d'origine :
`mini-audit-V2.md` §10 pour CP-1 à CP-13, `mini-audit-B.md` §4 pour
CP-14 à CP-18, la section « CP-19 à CP-22 » ci-dessous pour les quatre
cas issus d'Analysis C (pas de fichier d'audit dédié dans ce dépôt — la
source est l'article cité et sa citation, comme pour tout fait de ce
registre). Aucun CP n'est ici reformulé, fusionné ni résolu.

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
| CP-19 | un signataire au-delà de deux (`acteur`/`destinataire`) n'est pas représentable | Analysis C (fork stress-test) | 1 | fidélité factuelle | isolé | 4 |
| CP-20 | un objet dont l'état est un agrégat automatique de plusieurs objets-enfants n'a pas d'emplacement dans `transitions_objet` | Analysis C (fork stress-test, lecture flottante) | 2 | fidélité factuelle | récurrent | 4 |
| CP-21 | `dans_logiciel: non` confond une action hors logiciel et un acteur sans compte utilisateur | Analysis C (fork stress-test, lecture flottante) | 1 | fidélité factuelle | isolé | 4 |
| CP-22 | `perimetre` n'a pas de valeur pour un tiers réglementaire | Analysis C (fork diversité) | 1 | fidélité factuelle | isolé | 4 |

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

---

## CP-19 à CP-22 — issus d'Analysis C (crash-test externe de V3, 37
articles Axonaut/Costructor/OpenFire/ProGBat, 2026-09-08)

Ces quatre cas n'ont pas été recherchés : ils sont apparus par le
protocole de lecture flottante (relecture de la source sans le schéma en
tête, question unique : qu'est-ce qui est important ici que l'extraction
n'a pas naturellement fait ressortir ?) ou par relecture directe d'un
mécanisme de signature. Aucun ne provient d'un fichier d'audit dédié dans
ce dépôt — leur trace est l'article source cité et sa citation, comme
pour tout autre fait de ce registre.

### CP-19 — un signataire au-delà de deux n'est pas représentable

**Description factuelle.** `interactions.acteur`/`destinataire` est une
paire ; un document signé par trois parties distinctes (maître d'ouvrage,
entreprise, maître d'œuvre) ne peut désigner qu'un acteur et un
destinataire — le troisième signataire n'a nulle part où aller.

**Cas/source.** Costructor, PV de réception de travaux
(`chantiers/comment-creer-un-pv-de-reception-de-travaux-408xa.md`) — trois
signataires nommés explicitement dans l'article.

**Impact.** Un signataire est silencieusement omis ou artificiellement
fusionné avec un autre — un trou, pas une affirmation fausse sur les deux
rôles effectivement codés.

**Statut : isolé** (1 cas). **Priorité 4.**

**Bloquant : NON.** Ne touche aucune des hypothèses H1/H2/H3 actuellement
testées.

### CP-20 — un objet-conteneur à état agrégé n'a pas d'emplacement

**Description factuelle.** `transitions_objet` représente des passages
point-à-point (`objet_source` → `objet_resultat` via une `action`). Un
objet dont l'état dérive automatiquement de plusieurs objets-enfants
(devis, factures, bons de commande et de livraison rattachés à une
« commande » ; devis/factures/rapports rattachés à un « chantier » vu
depuis un portail client) n'a pas de représentation : ce n'est pas un
passage mais une architecture d'agrégation.

**Cas/source.** Axonaut,
`commandes-clients-fournisseurs/fonctionnement-dune-commande-client.md` ;
Costructor,
`chantiers/comment-fonctionne-le-portail-clientchantier-17oxarx.md` —
deux éditeurs indépendants, tous deux trouvés par lecture flottante.

**Impact.** Champs structurés muets sur ce point ; le phénomène ne serait
capturable qu'en texte libre (`signaux_emergents`), sans structure
comparable entre concurrents.

**Statut : récurrent** (2 occurrences, 2 concurrents indépendants — la
récurrence est notée mais, comme pour CP-3/CP-6/CP-17, ne suffit pas seule
à qualifier `structurel` : aucune affirmation fausse n'est produite,
c'est un trou). **Priorité 4.**

**Bloquant : NON.**

### CP-21 — identité sans accès produit confondue avec une action hors logiciel

**Description factuelle.** `dans_logiciel: non` sert à la fois pour « ce
qui se passe hors du logiciel » et pour « un acteur qui n'a tout
simplement pas de compte utilisateur ». Un « personnel » peut exister dans
le système (assignable, traçable) sans jamais avoir de compte — ces deux
faits sont différents et se confondent aujourd'hui dans une seule valeur.

**Cas/source.** Axonaut,
`configurer-votre-compte/droits-responsabilites-utilisateurs-a-quoi-ca-correspond-2.md`
— trouvé par lecture flottante.

**Impact.** Un trou de nuance, pas une affirmation fausse : les deux
situations restent codées identiquement, aucune n'est niée.

**Statut : isolé** (1 cas). **Priorité 4.**

**Bloquant : NON.**

### CP-22 — `perimetre` n'a pas de valeur pour un tiers réglementaire

**Description factuelle.** `interactions.perimetre` prévoit
`interne | client | partenaire | editeur | inconnu`. Une « Plateforme
Agréée » (tiers réglementaire de la facturation électronique) ne
correspond nommément à aucune des cinq valeurs.

**Cas/source.** OpenFire, corpus de configuration/facturation
électronique — trouvé par relecture directe, pas par lecture flottante.

**Impact.** Codable en `partenaire` par extension ou `inconnu` sans
affirmer de faux, mais aucune des deux ne le nomme correctement.

**Statut : isolé** (1 cas). **Priorité 4.**

**Bloquant : NON.**

---

**Aucun des quatre ne modifie le statut ou la priorité des CP-1 à CP-18.**
Aucun n'a été corrigé par cette mise à jour — ils restent **ouverts, non
bloquants**, conformément au critère déjà établi dans ce registre
(l'occurrence, rare ou récurrente, n'élève le statut à `structurel` que
si le codage forcé produit une affirmation fausse, pas un trou).
