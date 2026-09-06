# 0003 — Hypothèses de continuité

Deux hypothèses distinctes. **Elles ne doivent jamais être fusionnées**,
ni dans l'extraction, ni dans l'analyse, ni dans la restitution.

---

## H1 — CONTINUITÉ OPÉRATIONNELLE

> Chez les concurrents spécialisés étudiés, des transitions du cycle
> métier provoquent une rupture de continuité de l'objet.

### Trois ruptures observables

Chacune exige une **preuve positive** dans le texte analysé.

1. **ressaisie** — une information déjà disponible dans le logiciel doit
   être saisie de nouveau.
2. **sortie_logiciel** — il faut sortir de l'outil pour poursuivre :
   Excel, email, papier, téléphone, support éditeur.
3. **reconstruction_contexte** — le nouvel objet ne reprend pas les
   données de l'objet précédent ; l'utilisateur doit reconstituer le
   contexte.

### Règle absolue

**L'absence de documentation n'est pas une rupture.**

Un article qui décrit le devis sans dire comment il devient une visite
se code `non_determinable`, **jamais** `rupture_documentee`.

Cette règle est la principale protection contre l'erreur qui
invaliderait l'ensemble de l'analyse : transformer un silence
documentaire en défaut produit.

### Critère de continuité

> Le passage réutilise-t-il l'information et le contexte disponibles
> sans reconstruction significative ?

**L'automatisation n'est pas le critère.**

- Un bouton « créer l'intervention depuis le devis » qui reprend tout le
  contexte est une **bonne** continuité.
- Une création automatique qui perd les données techniques est une
  **mauvaise** continuité.

### Dénominateur

Les transitions **applicables au positionnement du produit**, jamais
toutes les transitions du cycle SUPORDO.

Un pur-player du SAV ne doit pas être pénalisé pour ne pas couvrir
`estimatif → visite → étude`. Une matrice d'applicabilité par concurrent
sera construite avant tout calcul.

### Seuil de falsification

**NON FIGÉ à ce stade.**

Il sera fixé avant l'analyse C, une fois la matrice d'applicabilité
connue, et **avant lecture des résultats de C**.

> Interdiction de choisir le seuil après avoir vu la distribution.

---

## H2 — CONTINUITÉ ORGANISATIONNELLE

> Lorsque plusieurs personnes participent au même cycle, le logiciel
> conserve-t-il l'information, l'état de l'objet et l'action attendue
> lors du passage entre commercial/patron, bureau et terrain ?

**Ne s'applique pas à la configuration solo** (voir 0002).

### Condition de réfutation

H2 tombe si les passages sont documentés avec :

- une transmission explicite,
- une action attendue du destinataire,
- une traçabilité de la progression.

**Le retour vers l'émetteur n'est pas une condition nécessaire.**
Exiger un accusé de réception reviendrait à juger les concurrents sur
notre conception du workflow plutôt qu'à observer la leur. Un produit
peut organiser une continuité parfaitement valable sans boucle de
retour.

---

## Statut des deux hypothèses

H1 et H2 constituent deux hypothèses particulières testées par l'étude.
Elles ne définissent pas à elles seules ce que le corpus doit permettre
de découvrir. Une observation qui n'est pertinente ni pour H1 ni pour H2
ne doit jamais être écartée pour cette raison.

**Non testées.** Ni le Pilote A ni le Pilote B ne les trancheront.

- Le Pilote A a été construit par thème métier : il ne mesure pas la
  continuité.
- Le Pilote B est construit pour maximiser la coordination : il est
  biaisé par construction et ne peut pas produire de taux.

Seule l'analyse C, menée sur un corpus étendu avec un dénominateur
d'applicabilité explicite, pourra les trancher.

---

## Avertissement

**La continuité est une hypothèse en cours de test, pas la doctrine
produit.**

Le corpus peut révéler que la différenciation se situe ailleurs :

- vitesse
- mobilité
- recovery
- profondeur métier
- automatisation
- communication

Le schéma V2 extrait des faits sans présupposer laquelle de ces
dimensions comptera. Si les données désignent une autre dimension, la
doctrine doit suivre les données, pas l'inverse.
