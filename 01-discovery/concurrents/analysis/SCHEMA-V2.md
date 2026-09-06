# SCHEMA V2 — Contrat d'extraction

**CONTRAT IMMUABLE POUR LE RECODAGE DES 30 ARTICLES DU PILOTE A.**

Ce gel vaut pour la session de recodage, pas pour les 1 494 articles. Le
contrat pourra être révisé entre le mini-audit et l'industrialisation —
jamais pendant une extraction en cours.

Si un cas résiste, il est accumulé dans « Cas problématiques ». Aucune
définition, aucun enum n'est ajusté en cours de route — **même au
douzième cas bizarre**. Un schéma modifié pendant l'extraction produit
un corpus dont la première moitié et la seconde ne sont pas comparables.

---

## Règle fondamentale

> Toute information métier ou produit potentiellement significative
> perdue lors du passage du texte source au YAML constitue une perte
> d'extraction, même lorsque le YAML respecte formellement le schéma.

Un YAML conforme n'est pas un YAML réussi.

---

## Séparation des responsabilités

| Bloc | Contenu |
|---|---|
| `interactions` | relation ou mécanisme entre acteurs |
| `transitions_objet` | transformation d'un objet métier |
| `regles_operationnelles` | conditions, contraintes, conséquences et résolutions documentées |
| `signaux_emergents` | ce qui reste significativement mal représenté **après** prise en compte des trois blocs ci-dessus |
| Cas problématiques | difficulté d'application du contrat |

Une information ne va **jamais** dans `signaux_emergents` parce qu'elle
est une règle, une exception ou une correction d'erreur. Elle n'y va que
si un aspect significatif reste aplati après extraction dans les champs
structurés.

---

## Structure

```yaml
parcours:
  origine: vente | sav | maintenance | interne | inconnu
  nature:  installation | intervention | administratif | inconnu

interactions:                   # LISTE, 0 à N par article
  - acteur:
      role_brut:
      role_canonique:
      preuve: {niveau, source, citation}
    destinataire:
      role_brut:
      role_canonique:
      preuve: {niveau, source, citation}
    perimetre:     interne | client | partenaire | editeur | inconnu
    relation:      pair | hierarchique | autre | inconnu
    canal:         email | push | interface | fil_activite |
                   statut | sms | aucun | inconnu
    dans_logiciel: oui | non | partiel | inconnu
    mecanismes:                 # LISTE, chacun sa preuve
      - forme: visibilite | affectation | permission |
               transmission | validation | notification |
               edition_partagee | automatisation
        preuve: {niveau, source, citation}

transitions_objet:              # LISTE, 0 à N par article
  - objet_source:
    etat_entree:
    action:
    objet_resultat:
    etat_sortie:
    owner_avant: {role, preuve}
    owner_apres: {role, preuve}
    continuite:
      statut_observation: continue_documentee |
                          rupture_documentee | non_determinable
      ruptures:               # LISTE, chacune sa preuve
        - type: ressaisie | sortie_logiciel |
                reconstruction_contexte
          preuve: {niveau, source, citation}
    preuve: {niveau, source, citation}

regles_operationnelles:         # LISTE, 0 à N par article
  - description_brute:          # la règle dans les termes source,
                                # sans la qualifier de friction,
                                # complexité, qualité ou défaut
    objet_concerne:
    condition:                  # null si aucune condition
                                # distincte identifiable
    consequence:                # null si aucune conséquence
                                # distincte identifiable
    preuve: {niveau, source, citation}
    resolution_documentee:      # null si aucune n'est documentée
      action:
      acteur:                   # null si aucun rôle documenté
      preuve: {niveau, source, citation}

signaux_emergents:              # LISTE, 0 à N par article
  - description_brute:
    pourquoi_notable:
    termes_source: []
    preuve: {niveau, source, citation}
```

### Bloc preuve, partout identique

```yaml
preuve:
  niveau:   explicite | contextuel | infere | inconnu
  source:   texte | titre | rubrique | permission | autre
  citation: moins de 15 mots, ou null
```

**niveau**

- `explicite` — le texte l'énonce directement.
- `contextuel` — établi par la structure de l'article (titre, rubrique,
  section) sans être énoncé dans une phrase.
- `infere` — reconstruit par le lecteur à partir d'indices. Doit rester
  minoritaire ; un champ majoritairement inféré mesure l'analyste, pas
  le produit.
- `inconnu` — non déterminable dans cet article.

**source** — d'où vient l'information : du corps du texte, du titre, de
la rubrique du concurrent, d'une mention de permission ou de licence, ou
d'autre chose.

**citation** — moins de 15 mots, verbatim, ou `null`. Une citation
absente n'interdit pas le fait ; elle interdit `niveau: explicite`.

---

## Règles du contrat

### R1 — Aucun score

**Aucun score, aucun niveau 0-5.** L'extraction produit des faits ; les
scores seront calculés en aval, à partir des faits, et pourront être
recalculés sans relire les articles.

C'est la correction principale du Pilote A : V1 demandait un jugement là
où il fallait une observation, et 33 % des jugements positifs étaient
faux.

### R2 — La preuve appartient au fait

La preuve appartient au **fait**, jamais à l'article. Chaque acteur,
chaque destinataire, chaque mécanisme, chaque transition, chaque
rupture, chaque règle et chaque résolution porte la sienne.

V1 avait une citation unique par article : impossible de savoir lequel
des faits elle appuyait.

### R3 — Pas de mécanisme sans preuve distincte

Un mécanisme sans preuve distincte **ne doit pas être écrit**.

Une affectation ne peut recevoir la forme `transmission` que si une
citation documente réellement une transmission. Chaque forme se gagne
séparément.

### R4 — Listes, jamais objets uniques

`interactions`, `transitions_objet`, `regles_operationnelles` et
`signaux_emergents` sont des **listes**.

Un article décrivant `technicien → client` **et** `technicien → bureau`
produit **deux** interactions. V1 les écrasait sur une seule ligne et
perdait systématiquement la seconde.

### R5 — La rupture exige une preuve positive, fait par fait

La preuve appartient au fait. Cette règle vaut pour les ruptures comme
pour les mécanismes.

- `continue_documentee` → `ruptures: []`
- `non_determinable` → `ruptures: []`
- `rupture_documentee` → au moins une rupture, **chacune avec sa propre
  preuve**
- Aucune rupture n'est déduite du silence documentaire.
- Aucun nouveau type de rupture n'est créé pendant le recodage.

**Arbitrage** — Une rupture réelle qui ne rentre dans aucun des trois
types va dans « Cas problématiques ». Si l'article énonce par ailleurs
la contrainte sous forme de règle, cette règle se code dans
`regles_operationnelles` — ce sont deux faits distincts, chacun avec sa
preuve, non un doublon. Une rupture ne va dans `signaux_emergents` que
si elle révèle en outre un phénomène produit qui dépasse la question de
la continuité. Jamais plusieurs de ces destinations par défaut.

### R6 — Sémantique de `inconnu`

`owner: inconnu` signifie « non déterminable dans cet article »,
**jamais** « le produit ne gère pas l'ownership ».

Cette lecture vaut pour toute valeur `inconnu` du schéma, ainsi que pour
`resolution_documentee: null`.

### R7 — Ne jamais forcer le parcours

Ne force jamais un article dans la trajectoire vente / installation. Les
valeurs `sav`, `maintenance`, `interne` et `inconnu` existent pour cela
(voir décision 0002).

---

## Les 8 valeurs de `forme`

### visibilite

Deux rôles accèdent au même objet ou aux mêmes données, sans qu'un geste
de transmission soit décrit.

> **Contre-exemple** — Le fait que le gestionnaire puisse ouvrir la
> liste des suivis de chantier n'est pas une transmission : personne ne
> lui a rien envoyé.

### affectation

Un objet est rattaché nominativement à une personne, par règle ou par
choix.

> **Contre-exemple** — « L'intervenant principal sera automatiquement
> affecté à toutes les nouvelles interventions » : personne ne décide de
> transmettre, personne n'accuse réception. **affectation ≠
> transmission.**

### permission

Un droit d'accès est accordé, refusé, requis ou paramétré.

> **Contre-exemple** — « Les profils terrain n'ont pas accès à vos
> marges » décrit une frontière d'accès, pas une coordination entre deux
> personnes. **permission ≠ coordination.**

### transmission

Un objet ou une information est explicitement remis d'un rôle à un
autre, par un geste identifiable.

> **Contre-exemple** — Enregistrer un document que quelqu'un d'autre
> pourra consulter plus tard n'est pas une transmission : c'est de la
> **visibilite**.

### validation

Un rôle approuve ou refuse ce qu'un autre a produit, et ce verdict
change l'état de l'objet.

> **Contre-exemple** — Cliquer soi-même sur « Accepter » pour
> enregistrer la réponse orale d'un client n'est pas une validation par
> le client : l'entreprise saisit un fait externe.

### notification

Un signal informe un rôle qu'un événement s'est produit, sans lui
remettre le travail.

> **Contre-exemple** — L'email de remerciement automatique envoyé au
> client après paiement informe, mais ne transfère aucune tâche.

### edition_partagee

Plusieurs rôles modifient successivement le même objet.

> **Contre-exemple** — Le bureau qui reprend et corrige le rapport d'un
> technicien n'a rien reçu : le technicien ne lui a rien envoyé et n'est
> pas prévenu. **edition_partagee ≠ transmission.**

### automatisation

Le système exécute lui-même une étape qui relie deux objets ou deux
rôles.

> **Contre-exemple** — Un calcul interne à un seul objet (l'arrondi de
> TVA d'une facture) n'est pas de l'automatisation de coordination :
> rien ne circule entre objets ni entre rôles.

---

## regles_operationnelles

Ce bloc recueille les conditions, contraintes, conséquences et
résolutions documentées par l'article.

**Aucun enum de nature de règle.** Précondition, interdiction,
verrouillage, récupération sont des classifications analytiques, pas des
observations. Les construire maintenant, à partir d'une poignée
d'exemples, reproduirait l'erreur du score 0-5. Elles pourront émerger
du corpus si les données les justifient.

`description_brute` conserve la règle dans les termes de la source. Elle
ne la qualifie ni de friction, ni de complexité, ni de défaut, ni de
qualité. Le nom du bloc lui-même évite « complexité », qui est déjà une
interprétation.

### Règles

- **Une règle par entrée.** Ne les agrège jamais.
- La règle et sa résolution portent **chacune leur propre preuve** : une
  règle peut être explicite et sa résolution seulement inférée.
- **Aucun comportement ne se déduit d'un silence.** Une résolution non
  documentée se code `resolution_documentee: null`, jamais une
  résolution supposée.
- `condition` et `consequence` sont `null` lorsqu'aucune n'est
  distinctement identifiable dans le texte. Une règle peut exister sans
  que l'article sépare les deux.

### Frontière avec `transitions_objet.etat_entree`

`transitions_objet.etat_entree` décrit l'état d'un objet dans une
transformation documentée. `regles_operationnelles.condition` enregistre
la règle lorsque l'article l'énonce comme telle. Un article qui montre
une transition sans énoncer de règle ne produit aucune entrée de règle.

### Calibration

L'énoncé « une feuille validée n'est plus modifiable ; seul l'employeur
peut la rouvrir » doit être **entièrement représentable ici, sans aucun
signal émergent** :

```yaml
- description_brute: une feuille de temps validée n'est plus
                     modifiable sur l'application mobile
  objet_concerne: feuille de temps
  condition: la feuille est au statut validée
  consequence: le salarié ne peut plus la modifier
  preuve: {niveau: explicite, source: texte,
           citation: "une feuille de temps validée n'est plus modifiable"}
  resolution_documentee:
    action: l'employeur refuse la feuille, qui redevient modifiable
    acteur: Employeur
    preuve: {niveau: explicite, source: texte,
             citation: "Il doit refuser votre feuille de temps"}
```

Cet exemple **n'est pas une catégorie à rechercher**. Il calibre le
niveau de détail attendu, rien d'autre.

---

## signaux_emergents

`signaux_emergents` sert lorsqu'une information métier ou produit
potentiellement significative n'est pas suffisamment représentée par les
champs structurés.

Cela peut concerner un objet inattendu, une transformation, une manière
de travailler, un mécanisme, un mode de capture, une règle métier, une
exception, un comportement de récupération après erreur, une contrainte,
une organisation, ou quelque chose que notre vocabulaire ne sait pas
encore nommer.

**Cette liste est illustrative et non exhaustive.** Ne recherche pas
activement ces catégories. Observe l'article.

**Aucun enum.** Une liste fermée de phénomènes à chercher reproduirait
exactement le défaut que ce champ corrige.

### Trois conditions cumulatives

Un signal ne s'écrit que si les trois sont réunies :

1. il est supporté par la source ;
2. il est potentiellement significatif pour comprendre le produit ou le
   travail ;
3. il est insuffisamment représenté par les champs structurés.

La condition 3 s'évalue **après** avoir renseigné `interactions`,
`transitions_objet` et `regles_operationnelles`. Un phénomène
correctement représenté par l'un de ces trois blocs n'est pas un signal
émergent.

`signaux_emergents` **n'est pas un résumé libre de l'article**. N'y
place pas tout ce qui n'entre pas ailleurs.

### Exemple

Si un article documentait « l'utilisateur dicte depuis le mobile ; le
système interprète la dictée et prépare un devis », il serait
insuffisant de conserver uniquement :

```yaml
mecanismes: [{forme: automatisation}]
transitions_objet: [{objet_source: qualification,
                     objet_resultat: devis}]
```

Une partie importante du comportement produit aurait disparu. Le signal
émergent doit conserver, dans les termes de la source, ce que le schéma
structuré ne représente pas.

Cet exemple ne signifie pas « cherche la voix ou l'IA chez tous les
concurrents ». Il signifie : lorsqu'un phénomène important est aplati
par la normalisation, conserve ce qui serait perdu.

---

## Cas problématiques

*Section à alimenter pendant le recodage — une entrée par cas : article,
ce qui résiste, ce qui a été codé faute de mieux. Aucune règle du
contrat n'est modifiée ici.*

---

## Protocole du mini-audit de session 2

À exécuter après le recodage des 30 articles, pas pendant.

### Contrôle — STATUT ≠ ACTION

Auditer toutes les occurrences des formes `validation` et
`transmission`. Vérifier qu'aucune ne repose uniquement sur un libellé
d'état : Accepté, Validé, Refusé, Transmis, Clôturé.

Un statut ne prouve pas qu'un rôle a réalisé l'action correspondante.
Créditer une action exige la citation d'un geste ou d'un mécanisme.

Rapporter les faux positifs.

### Contrôle — PERTE D'INFORMATION

C'est le contrôle majeur du pilote. Pour chacun des 30 articles :

1. produire le YAML V2 ;
2. relire ensuite l'article source ;
3. demander : « après prise en compte des quatre blocs — `interactions`,
   `transitions_objet`, `regles_operationnelles`, `signaux_emergents` —
   existe-t-il une information métier ou produit potentiellement
   significative qui disparaît entièrement ou est matériellement aplatie
   dans le YAML ? »

Ce contrôle détecte ce que **l'ensemble du dispositif** perd. Une règle
correctement représentée dans `regles_operationnelles` n'est pas une
perte.

Si oui : consigner ce qui est perdu, indiquer si `signaux_emergents`
aurait dû le conserver, et **ne jamais modifier le schéma**.

Rapporter au mini-audit :

- nombre d'articles sans perte détectée ;
- nombre avec au moins une perte significative ;
- nature brute de chaque perte ;
- pertes capturables par `signaux_emergents` mais oubliées ;
- pertes impossibles à représenter même avec `signaux_emergents`.

Ne pas transformer ces résultats en score de qualité. Le but est
d'identifier les modes d'échec du schéma.

---

## Discipline de découverte

Deux règles simultanées pendant le recodage.

**NE PAS INVENTER** — n'extraire rien qui ne soit soutenu par l'article.
Un signal émergent n'autorise aucune spéculation sur l'importance réelle
d'une fonctionnalité, sa fréquence, sa qualité, son adoption, son
efficacité ou l'intention stratégique du concurrent.

**NE PAS ÉCRASER** — ne pas supprimer une information significative
parce qu'elle ne rentre pas dans le modèle. En cas de doute : conserver
les termes source, qualifier le niveau de preuve, utiliser `inconnu` si
nécessaire, utiliser `signaux_emergents` si le phénomène est significatif
mais mal représenté, utiliser « Cas problématiques » si le contrat ne
permet pas de le coder proprement.

Le contrat doit éviter deux échecs symétriques :

- **SURINTERPRÉTATION** — trouver ce qu'on voulait trouver.
- **SOUS-OBSERVATION** — ne trouver que ce qu'on a appris à chercher.

Le Pilote A teste la résistance aux deux.

---

## Ce que ce schéma ne prétend pas mesurer

V2 n'évalue pas :

- la qualité UX
- la fréquence d'usage
- la criticité métier
- la satisfaction utilisateur
- la performance réelle du logiciel
- l'absence d'une fonctionnalité

Il extrait uniquement ce qui est **observable dans la documentation
analysée**.

> `inconnu` et `non documenté` ne signifient jamais `absent du produit`.

Formulation interdite : « X n'a pas la fonctionnalité Y ».
Formulation exigée : « La fonctionnalité Y n'a pas été trouvée dans les
articles analysés de X ».
