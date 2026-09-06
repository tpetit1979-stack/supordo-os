# 0004 — Architecture de l'assessment concurrentiel

Cette décision fixe la séparation entre les sources documentaires, les
sources marketing et la couche d'assessment.

Elle ne définit pas encore le schéma d'extraction du corpus marketing.

---

## BLOC 1 — DOCS / CENTRES D'AIDE

Observer notamment :

- comportements documentés ;
- règles et contraintes ;
- transitions d'objets ;
- mécanismes de coordination ;
- continuités documentées ;
- ruptures documentées ;
- procédures de correction et de récupération ;
- limites et cas particuliers explicitement décrits.

**Finalité :**

> documenter ce que l'éditeur décrit du fonctionnement de son produit,
> avec les mécanismes, conditions et limites observables dans les sources.

Ne jamais reformuler cette finalité comme :

> ce que le produit fait réellement

La documentation est une source éditoriale. Elle ne démontre ni l'usage
réel, ni l'exhaustivité fonctionnelle, ni l'absence d'une fonctionnalité
non documentée.

**Silence documentaire ≠ absence produit.**

Instrument : contrat V2, puis V3 après arbitrage. Voir
`analysis/SCHEMA-V2.md`.

---

## BLOC 2 — SITES MARKETING

Observer notamment :

- positionnement revendiqué ;
- segments ciblés ;
- métiers déclarés ;
- personas explicitement adressés ;
- problèmes mis en avant ;
- promesses de valeur ;
- différenciation affirmée ;
- prix et paliers lorsqu'ils sont publics ;
- comparatifs publiés par l'éditeur lui-même ;
- vocabulaire et concepts que l'éditeur choisit de mettre au premier plan.

**Finalité :**

> documenter ce que l'éditeur affirme vendre, à qui, et autour de quelles
> promesses.

Ne pas transformer une formulation marketing en comportement produit sans
corroboration documentaire.

---

## BLOC 3 — ASSESSMENT

Croiser les deux corpus pour analyser notamment :

- promesse revendiquée vs comportement documenté ;
- mécanismes soutenant une promesse ;
- limites documentées derrière une promesse ;
- modèles d'organisation ;
- continuités et ruptures ;
- différences entre positionnement annoncé et fonctionnement documenté ;
- angles morts documentaires ;
- questions nécessitant d'autres sources ;
- implications produit, clairement séparées des constats concurrentiels.

**Finalité :**

> produire une interprétation comparative qui n'existe telle quelle dans
> aucun des deux corpus.

Toute sortie d'assessment doit permettre de distinguer :

- **FAIT DOCUMENTÉ**
- **INTERPRÉTATION**
- **QUESTION OUVERTE**

Les implications pour SUPORDO appartiennent à la couche d'assessment.
Elles ne doivent jamais être réinjectées dans l'extraction comme si elles
provenaient des concurrents.

---

## SÉPARATION DES SCHÉMAS

Le contrat V2/V3 conçu pour les centres d'aide **ne doit pas être appliqué
mécaniquement au corpus marketing.**

Une procédure d'aide décrit fréquemment acteurs, objets, actions, règles
et transitions.

Une page marketing peut ne documenter aucun de ces éléments.

Le corpus marketing devra donc disposer d'un instrument d'extraction
distinct, plus léger.

Cet instrument fera l'objet :

1. d'un petit pilote ;
2. d'un contrôle de perte d'information ;
3. d'un contrôle du niveau d'inférence ;
4. d'un arbitrage avant industrialisation.

Le marketing présente un risque particulier d'inférence : une promesse,
un superlatif ou une formulation vague ne doit jamais être converti en
capacité fonctionnelle précise sans preuve.

---

## PREMIER EXEMPLE OBSERVÉ — À NE PAS SURINTERPRÉTER

Dans l'article d'aide InterFast « Créer un chantier », la conclusion
affirme :

> « fluidifiez la communication entre vos équipes de terrain et le
> bureau »

L'extraction mécanisme par mécanisme documente :

- une affectation ;
- une notification ;
- une permission ;
- une visibilité ;
- **aucune transmission** selon la définition retenue par le contrat.

Ce cas montre qu'une formulation de promesse et les mécanismes documentés
qui l'accompagnent peuvent diverger.

**IMPORTANT :**

Ce n'est **pas** encore un exemple de croisement
`site marketing ↔ documentation`, puisque la formulation de promesse et
les mécanismes proviennent ici du même article d'aide.

Il constitue un précédent méthodologique justifiant l'intérêt futur du
croisement entre corpus marketing et corpus documentaire.
