# 0002 — Carte métier initiale SUPORDO — hypothèse de départ

Cette carte décrit le modèle métier initial utilisé par SUPORDO pour
formuler certaines questions de recherche. Elle provient de la
connaissance actuelle des métiers ciblés : chauffage, fumisterie,
vente/installation, SAV et maintenance.

Elle n'est ni un cycle universel des artisans, ni une taxonomie imposée
au corpus, ni une grille de complétude permettant de noter les
concurrents.

L'extraction reste ouverte : tout objet, état, transition, mécanisme ou
phénomène documenté par un concurrent doit être conservé dans ses
propres termes, même s'il n'existe pas dans cette carte.

Le corpus pourra conduire à modifier, compléter ou abandonner cette
représentation.

## Portes d'entrée

- site web
- téléphone
- showroom
- réseaux sociaux
- recommandation
- client existant

## Trajectoires

Parmi les trajectoires identifiées à ce jour figurent notamment
vente/installation et SAV/intervention. Elles ne sont ni exclusives ni
nécessairement linéaires. Une affaire peut commencer à différentes
étapes, bifurquer, boucler, changer de nature, s'arrêter ou déclencher
une nouvelle affaire.

Quatre exemples, pour rendre le principe concret :

- SAV → opportunité commerciale
- visite → abandon
- chantier → avenant → retour au devis
- maintenance → anomalie → intervention

Cette liste est illustrative. La carte reste une hypothèse
intelligible ; elle n'a pas vocation à devenir un graphe de toutes les
trajectoires possibles.

## Trajectoire vente / installation

```
demande
  → qualification
  → devis estimatif
  → visite technique
  → relevé technique
  → étude / note de calcul
      (fumisterie, dimensionnement chaudière, étude clim/PAC)
  → devis définitif
  → envoi
  → relance
  → signature
  → acompte
  → commande fournisseur
  → réception matériel
  → planification
  → chantier
  → réception / clôture
  → facturation
  → parc installé
  → maintenance / SAV
  → boucle
```

### Variante showroom

Le devis estimatif **précède** la visite technique et sert d'outil
commercial d'engagement, avant validation technique. L'ordre des deux
étapes est donc inversé par rapport à la trajectoire nominale.

## Règle d'usage

Cette carte représente l'espace des étapes **possibles**, pas un
workflow obligatoire.

- Chaque affaire en emprunte un **sous-ensemble**.
- Certaines étapes **bouclent ou se répètent** : avenant, facture de
  situation, paiement intermédiaire.
- Un SAV peut n'avoir **aucun devis**.
- Un entretien périodique peut aller directement :
  `demande → planning → intervention → facture`.

Corollaire pour l'extraction : un article ne doit jamais être forcé dans
la trajectoire vente / installation. Le champ `parcours.origine` prévoit
`sav`, `maintenance`, `interne` et `inconnu` précisément pour cela.

## Deux configurations d'entreprise, à ne jamais confondre

### ARTISAN SOLO

La continuité organisationnelle (H2) est généralement non applicable
lorsqu'une seule personne réalise le cycle. Cela ne préjuge en rien de
la continuité opérationnelle (H1). Un utilisateur seul peut subir
ressaisies, changements d'outil, reconstruction de contexte et ruptures
entre objets.

### PME / SHOWROOM

Même cycle, mais réparti :

```
commercial → métreur → bureau → administration
           → équipe terrain → bureau
```

Chaque flèche est un passage observable entre plusieurs rôles. Ce sont
des objets d'observation, pas des défauts présumés.

### Conséquence

Les deux configurations ne doivent jamais être évaluées avec le même
critère, ni leurs résultats agrégés. H2 n'est applicable qu'à la
seconde ; H1 s'applique aux deux.

## Portée de ce document

Cette carte sert à **situer** ce qu'un article documente. Elle ne
constitue ni une prescription pour SUPORDO, ni un référentiel de
complétude fonctionnelle. Un concurrent ne couvrant qu'une portion du
cycle n'est pas pour autant déficient : il est positionné différemment
(voir la règle de dénominateur en 0003).
