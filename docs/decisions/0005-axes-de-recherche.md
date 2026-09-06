# 0005 — Axes de recherche

Cette décision fixe les axes de l'étude concurrentielle après les Pilotes
A et B. Elle complète les décisions 0001 (hypothèse initiale sur les
rôles) et 0003 (hypothèses de continuité), qu'elle ne remplace pas.

Sources : `analysis/audit-pilote-A.md`, `analysis/mini-audit-V2.md`,
`analysis/crash-test-utilite-pilote-A.md`, `analysis/mini-audit-B.md`.

---

## AXE PRINCIPAL — H1, continuité opérationnelle

**Inchangée.** Reste la colonne vertébrale de l'étude.

Énoncé, conditions d'observation, règle absolue sur le silence
documentaire, critère de continuité et règle de dénominateur : voir
décision 0003, section H1. Le seuil de falsification reste **non figé**,
et sera fixé avant l'analyse C, une fois la matrice d'applicabilité
connue, et avant lecture des résultats de C.

---

## AXE ORGANISATIONNEL — H2, continuité entre rôles

**Inchangée.**

Énoncé, condition de réfutation et périmètre d'application : voir
décision 0003, section H2. Rappel : le retour vers l'émetteur n'est pas
une condition nécessaire de la réfutation.

---

## NOUVELLE HYPOTHÈSE — H3, coordination conditionnelle

### Énoncé

> La coordination n'est pas seulement présente ou absente : elle peut
> s'activer selon un montant, un état, un rôle, une durée, un niveau
> d'abonnement, un réglage à la création, ou la présence d'une donnée.

### Origine

Sept formes de conditionnalité documentées dans les 10 articles du
Pilote B (voir `mini-audit-B.md`, §6) :

| Condition | Occurrence documentée |
|---|---|
| un montant | InterFast : « Définissez votre plafond de tolérance (ex: 500 €) » |
| une durée | Vertuoza : au-delà du nombre de jours configuré, les photos « ne seront plus sélectionnables » |
| un état de l'objet | InterFast : le devis doit être « Accepté » pour accéder à Opérations |
| un rôle | InterFast : « les profils configurés comme Validateurs (…) ne sont pas soumis au plafond » |
| un niveau d'abonnement | InterFast : le fil du chantier « disponible à partir de l'abonnement Pro » ; la validation des commandes « fait partie de l'abonnement Business » |
| un réglage à la création | Vertuoza : un avancement marqué « interne » ne pourra jamais être envoyé au client |
| la présence d'une donnée | Vertuoza : « si un responsable n'est pas sélectionné, alors vous ne saurez pas utiliser les réclamations pour la suite » |

Le cas le plus explicite est celui d'InterFast : un circuit hiérarchique
qui s'ouvre au-dessus d'un seuil chiffré paramétrable, et dont les
validateurs sont exemptés de leur propre règle.

### Statut

**Non testée.** La prévalence concurrentielle reste à établir sur le
corpus étendu.

### Formulations

Formulation exigée :

> peu documentée dans les 40 articles analysés

Formulation interdite :

> personne ne l'occupe

Les 40 articles des Pilotes A et B ont été sélectionnés, pour les uns par
thème métier, pour les autres pour maximiser la coordination. Aucun des
deux échantillons ne permet d'estimer une prévalence. Le Pilote B est
biaisé par construction ; ses taux ne caractérisent pas le marché.

---

## DIMENSION TRANSVERSALE — D1, distribution de visibilité et de prérogatives

### Énoncé

Qui voit quoi, qui peut faire quoi, sur le même objet.

### Base d'observation

6 occurrences sur 40 articles, chez deux éditeurs, sur quatre mécanismes
différents :

- Vertuoza : la visibilité des prix se règle dans la fiche du responsable
  d'intervention — elle est un attribut du rôle, non du document.
- Vertuoza : partition compte chantier / compte gestion.
- InterFast : « Inclure la liste d'articles (sans les prix) » — le même
  document existe en deux versions selon son lecteur.
- InterFast : « Il est possible de masquer les prix sur le PDF final,
  mais pas totalement lors de la saisie sur mobile actuellement. »
- InterFast : un fil unique où l'audience de chaque message bascule entre
  l'équipe et le client.
- Sellsy : « la liste des règlements n'affichera que les règlements des
  clients/prospects/fournisseurs auxquels vous avez accès ».

S'y rattachent, plus faiblement, les cas de prérogative déplacée d'un
rôle à l'autre : l'ouvrier qui décide du facturable chez Vertuoza, le
« Technicien + » qui encaisse chez le client chez InterFast.

### Statut

**Dimension inductive à surveiller.** Elle éclaire H1, H2 et H3 sans
constituer un axe autonome. Elle pourra monter en statut si le corpus
étendu la confirme massivement.

D1 n'a pas été cherchée : elle est apparue par `signaux_emergents` sur
les deux pilotes. C'est à ce titre qu'elle est conservée — pas parce
qu'elle est intéressante.

---

## DISTINCTION À NE JAMAIS PERDRE

**H3 est une hypothèse CONCURRENTIELLE.** Elle porte sur ce que les
concurrents documentent, et elle est testable sur le corpus.

**L'idée qu'un moteur de conditionnalité permettrait à un même produit de
servir l'artisan solo et la PME de 30 personnes est une hypothèse
PRODUIT.** Elle n'est pas testable sur de la documentation concurrente et
devra être vérifiée auprès d'utilisateurs réels.

Confondre les deux reviendrait à lire dans le corpus la réponse qu'on
souhaite y trouver. La documentation d'un concurrent dit ce que ce
concurrent décrit ; elle ne dit rien de ce qui manque au marché, ni de ce
dont une entreprise de 30 personnes a besoin.

Rappel de la décision 0002 : les configurations artisan solo et
PME / showroom ne doivent jamais être évaluées avec le même critère, ni
leurs résultats agrégés. H2 ne s'applique pas au solo ; H1 s'applique aux
deux.

---

## Ce que cette décision sert dans V3

Les cas problématiques ouverts par les mini-audits ne se valent pas. Ils
sont désormais rattachés à l'hypothèse qu'ils servent, ce qui donne
l'ordre de leur arbitrage.

| Correction envisagée | Cas problématique | Sert |
|---|---|---|
| Normalisation des noms d'objets | CP-12 | **H1** |
| Refonte des types de rupture | CP-7, CP-14, CP-16 | **H1** |
| Représentation de la conditionnalité | CP-18 | **H3** |
| Séparation `validation` / `effet_etat_documente` | CP-4 | fidélité factuelle générale — **ne sert aucune hypothèse en particulier** |

La dernière ligne mérite d'être lue pour ce qu'elle est : la séparation
entre le geste et son effet d'état n'améliore aucun axe de recherche.
Elle empêche seulement le schéma d'affirmer plus que la source. C'est un
motif suffisant, mais il ne doit pas être présenté comme un gain
analytique.

**Cette décision n'ouvre pas V3.** Elle classe. La révision du contrat
d'extraction reste conditionnée au périmètre retenu pour l'analyse C : si
le corpus étendu désignait une autre dimension que la continuité, l'ordre
de priorité ci-dessus changerait.
