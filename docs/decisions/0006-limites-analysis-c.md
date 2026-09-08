# 0006 — Limites d'Analysis C et prérequis avant agrégation H1

Cette décision consigne ce qu'Analysis C (crash-test externe de V3, 37
articles Axonaut/Costructor/OpenFire/ProGBat, 2026-09-08) a établi sur la
testabilité de H1, et ce qui reste délibérément non tranché. Elle
complète 0003 (hypothèses de continuité) et 0005 (axes de recherche),
qu'elle ne remplace pas.

## Ce qu'Analysis C a établi

**0 rupture documentée sur 39 transitions**, dans un échantillon
délibérément curaté (stress test ciblé + diversité documentaire), pas un
échantillon proportionnel ou aléatoire du corpus restant.

**Ce résultat n'est PAS une conclusion de marché.** Il est probablement
lié au genre documentaire des articles choisis (procédures de
configuration/référence) plus qu'au produit ou au secteur : le même type
de contrôle appliqué aux Pilotes A/B (genre plus narratif,
FAQ/dépannage) avait produit 21 ruptures sur 123 transitions. Aucune
comparaison de taux entre Pilotes et Analysis C ne doit être tirée : les
deux échantillons ne sont pas construits pour être comparables entre eux.

**Conséquence directe : `non_propagation` et `rupture_temporelle`**
(ajoutés en V3 pour corriger CP-7/CP-14/CP-16, voir
`analysis/SCHEMA-V2.md` §V3.5) **n'ont reçu aucun exercice sur du
matériel neuf.** Ce sont des corrections conçues et arbitrées, pas encore
validées empiriquement.

**La testabilité documentaire de H1 sur le corpus restant reste donc une
question ouverte** — ni réfutée, ni confirmée : simplement pas encore
mise à l'épreuve sur un échantillon construit pour répondre précisément à
cette question.

## Correction du 2026-09-08 (même jour, avant toute exécution)

La première version de cette décision proposait d'exécuter le lot test
FAQ/dépannage **avant** la matrice d'applicabilité et le seuil de
falsification, au motif qu'un lot sans rupture rendrait les deux inutiles.
**Cet ordre est corrigé.** Motif de la correction : le lot FAQ/dépannage
est lui-même une distribution. Le fixer avant la matrice et le seuil
reviendrait à choisir le seuil après avoir vu une distribution — exactement
l'interdiction déjà posée par la décision 0003 (« Interdiction de choisir
le seuil après avoir vu la distribution »). Cette interdiction ne
s'appliquait pas seulement à l'Analysis C originellement visée par 0003 ;
elle s'applique à toute distribution non encore observée, y compris un
lot test cheap conçu pour « voir s'il vaut le coup ». Le raisonnement
économique (« ne pas construire la matrice pour rien ») reste compris,
mais il ne peut pas passer avant la règle méthodologique qu'il menacerait
de contourner.

**Ordre corrigé, retenu, à exécuter séparément — rien n'est commencé par
cette décision :**

1. matrice minimale d'applicabilité (Vertuoza + InterFast) — ci-dessous ;
2. règle de qualification de la source (H1_SOURCE_TEST), fixée ex ante —
   ci-dessous ;
3. lot test FAQ/dépannage (Vertuoza + InterFast, ~20 articles) — non
   lancé par cette décision ;
4. interprétation du résultat à la lumière de la règle fixée à l'étape 2,
   jamais l'inverse ;
5. industrialisation.

## Matrice minimale d'applicabilité — Vertuoza et InterFast uniquement

**Portée volontairement restreinte** : ni les dix concurrents, ni la
totalité du cycle métier de la décision 0002 — seulement ce qui est
nécessaire pour rendre interprétable le futur lot FAQ/dépannage sur ces
deux concurrents. Regroupement en six phases du cycle 0002, pour la
lisibilité de cette matrice, pas une nouvelle taxonomie. Construite
uniquement à partir de ce qui est déjà établi (décision 0001, mini-audit-V2,
mini-audit-B, crash-test d'utilité) — aucune source relue pour cette
décision.

| Phase (cycle 0002) | Vertuoza | InterFast | Justification |
|---|---|---|---|
| Amont commercial (demande → qualification → étude/relevé) | **non déterminable** | **non déterminable** | crash-test §11.A : « Toute l'amont : demande, qualification, visite technique, relevé, étude / note de calcul. Zéro [article sur 30]. » — jamais échantillonné, silence ≠ absence (0003) |
| Devis (estimatif/définitif) → signature | **applicable, documenté** | **applicable, documenté** | 0001 ; mini-audit-V2/crash-test : devis, avenant, signature électronique documentés chez les deux |
| Commande fournisseur / réception matériel | **non déterminable** | **applicable, documenté** | InterFast : `activer-la-validation-des-commandes-fournisseurs` (pilote B) ; Vertuoza : aucun article pilote sur ce sujet — non observé, pas absent |
| Planification → chantier | **applicable, documenté** | **applicable, documenté** | crash-test : compte chantier/gestion (Vertuoza) ; guide complet de gestion de chantier (InterFast) |
| Facturation par étapes (acompte/solde) | **applicable, documenté** | **applicable, documenté** | crash-test §2 : « Facturation par étapes — Vertuoza 10 étapes 3 règles ; InterFast 12 règles » |
| Parc installé → maintenance/SAV | **non déterminable** | **non déterminable** | mini-audit-V2 §9 : `sav: 0, maintenance: 0` occurrence sur `parcours.origine` des 40 pilotes — jamais échantillonné |

**Lecture obligatoire** : une phase `non déterminable` n'est ni
`applicable` ni `non applicable` — c'est un angle mort de l'échantillon
pilote, pas un fait sur le produit (0003). Cette distinction ne
conditionne pas la classification binaire de la source (voir plus bas),
qui porte sur la simple présence d'au moins une preuve positive,
indépendamment de la phase. Elle reste utile pour interpréter, après
coup, la portée d'une rupture trouvée dans le lot FAQ — savoir si elle se
situe dans une phase `applicable, documenté` (rattachable au
positionnement connu du concurrent) ou `non déterminable` (informative,
mais sans base de comparaison établie).

## H1_REAL_WORLD et H1_SOURCE_TEST — deux notions à ne jamais confondre

**Correction du 2026-09-08 (bis).** La version précédente de cette
décision fixait un seuil quantitatif (10 % de transitions applicables en
rupture, sur un minimum de 15, comparé aux 15,6 % du Pilote A via une
règle des deux tiers) pour juger si un résultat du futur lot FAQ
« confirmait » ou « infirmait » H1. **Ce seuil est retiré avant tout
usage — aucun commit ne l'a jamais fixé.** Motif : un taux bas, même
mesuré avec un dénominateur restreint aux phases applicables, resterait
un fait sur la documentation lue, pas sur le produit — l'ériger en
verdict quantitatif sur H1 aurait commis exactement l'erreur que la règle
« silence documentaire ≠ absence produit » (0003) interdit déjà. Comparer
ce taux aux 15,6 % du Pilote A ajoutait une fausse précision : aucun des
deux échantillons ne mesure une prévalence, comme 0005 le rappelle déjà
pour le Pilote B.

Deux hypothèses distinctes doivent être nommées séparément et ne jamais
être fusionnées :

**H1_REAL_WORLD** — hypothèse substantielle : les logiciels et processus
réels des concurrents étudiés peuvent présenter des ruptures de
continuité opérationnelle. **Cette hypothèse ne peut pas être confirmée
ni réfutée par le seul silence d'une documentation produit** — un centre
d'aide ne documente pas l'usage réel (0004 : la documentation est une
source éditoriale, elle ne démontre ni l'usage réel ni l'absence d'une
fonctionnalité). Aucun lot documentaire, quel qu'il soit, ne peut trancher
H1_REAL_WORLD seul.

**H1_SOURCE_TEST** — question documentaire, la seule que le futur lot FAQ
teste réellement : **le genre FAQ/dépannage est-il capable de fournir des
preuves positives de ruptures pertinentes pour H1** ? C'est une question
sur l'instrument de collecte (quel genre de source produit quel type de
preuve), pas sur le produit concurrent.

**Le futur lot FAQ teste uniquement H1_SOURCE_TEST. Il ne teste, ne
confirme ni ne réfute jamais H1_REAL_WORLD.**

## Règle de qualification de la source — fixée ex ante, avant toute lecture du lot FAQ

Binaire, sans seuil numérique, sans comparaison à un taux antérieur.
Conforme à 0003 (« le seuil sera fixé... avant lecture des résultats ») :
écrite **avant** l'exécution du lot test FAQ/dépannage, elle ne sera pas
modifiée après avoir vu sa distribution.

- **Si au moins une rupture claire, positivement documentée et conforme
  aux règles V3** (`ruptures.type` parmi les 5 valeurs, preuve positive
  au sens de R5, `statut_observation: rupture_documentee`) **est
  trouvée** dans le lot FAQ, quel qu'en soit le nombre :
  → **`SOURCE_CAPABLE_DE_DOCUMENTER_H1`**

- **Si aucune rupture claire et positivement documentée n'est trouvée** :
  → **`SOURCE_FAIBLE_POUR_RUPTURES_H1`**

**Dans les deux cas, explicitement et sans exception :**

- ne pas inférer la prévalence réelle des ruptures depuis ce résultat —
  ni un taux, ni un ordre de grandeur, ni une tendance ;
- ne jamais conclure H1_REAL_WORLD vraie ou fausse à partir de ce seul
  résultat ;
- silence documentaire ≠ absence produit — `SOURCE_FAIBLE_POUR_RUPTURES_H1`
  qualifie le genre FAQ/dépannage comme instrument, jamais le produit
  concurrent comme exempt de ruptures ;
- toute rupture positive trouvée reste une observation exploitable en
  elle-même (source, preuve, type), indépendamment de ce que sa présence
  ou son absence dit de H1_SOURCE_TEST.

**Ce que cette règle ne dit toujours pas.** La matrice d'applicabilité
complète (tous concurrents) et un éventuel seuil de falsification
substantiel de H1_REAL_WORLD — s'il doit un jour en exister un, sur un
corpus construit spécifiquement pour cela — restent hors du périmètre de
cette décision.

**Le lot FAQ/dépannage n'est pas exécuté par cette décision.**

## Lecture flottante

Le principe de lecture flottante (relire la source sans le schéma en
tête, après extraction, pour détecter les angles morts) est retenu comme
contrôle permanent. **Le taux d'échantillonnage utilisé pendant Analysis
C (environ un quart des articles) n'est pas gravé comme ratio
permanent** : un échantillonnage substantiel reste utile en début
d'industrialisation et pourra être réduit si le rendement de découverte
— élevé lors d'Analysis C, chaque article relu ayant produit au moins une
observation nouvelle — venait à diminuer.

## Résultat du H1_SOURCE_TEST (2026-09-08)

Le lot test FAQ/dépannage (17 Vertuoza + 3 InterFast) a été exécuté selon
la règle de qualification ci-dessus. Rapport complet :
`analysis/h1-source-test-faq.md`.

**Verdict : `SOURCE_CAPABLE_DE_DOCUMENTER_H1`** — 8 ruptures positivement
documentées trouvées, sur 4 des 5 types V3.

**H1_REAL_WORLD reste entièrement non tranchée.** Ce résultat dit
seulement que le genre FAQ/dépannage peut porter ce type de preuve chez
ces deux éditeurs ; il ne dit rien de la fréquence réelle des ruptures
dans les produits, ni des huit autres éditeurs du corpus (échantillon
déséquilibré 17/3, voir le rapport pour le détail).
