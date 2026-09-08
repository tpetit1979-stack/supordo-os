# Pré-test H3 — pouvoir discriminant de LIGHT

Diagnostic, pas le crash-test H3 complet. Établit si le test est exécutable
et mesure ce qui est mesurable sans lui. HEAD au moment de l'exécution :
`c58e9b7`.

## Question fixée ex ante

H3 — coordination conditionnelle : « Les champs LIGHT permettent-ils
d'identifier, sans relire l'ensemble du corpus source, les documents
susceptibles de contenir des mécanismes où une action, une validation, une
transmission ou un comportement dépend d'une condition métier ? »

Formes de conditionnalité (décision 0005, mini-audit-B §6, non limitatif) :
montant · durée · état de l'objet · rôle · niveau d'abonnement · réglage à
la création · présence d'une donnée.

## 1. Périmètre LIGHT analysable

Reconstruit mécaniquement (comptage des lignes de données de chaque
tableau « Sorties LIGHT », vérifié par recoupement avec les agrégats
`contenu_observable` publiés dans chaque fichier — égalité exacte trouvée
partout où un agrégat existe).

| Artefact | Lignes | `chemin_relatif` en sortie |
|---|---:|---|
| Pilote (`pilote-light-corpus-inedit.md`) | 40 | absent du tableau de sortie (lignes 89-128) ; présent dans le tableau de sélection séparé (lignes 42-81), jointure exacte par `#` |
| Costructor (`light-costructor-help.md`) | 94 | présent directement |
| Axonaut (`light-axonaut-help.md`) | 119 | présent directement |
| ProGBat (`light-progbat-help.md`) | 186 | présent directement |

**Statut du pilote : inclus.** Ses 40 observations sont interrogeables sur
`regle_ou_condition` (colonne présente dans son propre tableau) et
rattachables à un chemin exact via la jointure `#` ↔ tableau de sélection
(les deux tableaux partagent la même numérotation 1-40, sans trou ni
doublon, vérifié à la lecture). Aucune ambiguïté de jointure rencontrée.

```
OBSERVATIONS_LIGHT_ANALYSABLES = 439  (40 + 94 + 119 + 186)
Aucune exclusion.
```

## 2. Contrôles positifs H3, gelés avant tout filtre

Construits uniquement à partir de `mini-audit-B.md` §6 (« Mécanismes de
coordination conditionnels », 7 formes documentées) et `REGISTRE-CP.md`
CP-18 (axe H3 explicite, statut `structurel`). Aucune valeur de champ
LIGHT consultée pour cette étape. Chaque source a été repointée à son
fichier exact dans `extracted/` (V2/V3, antérieur à LIGHT).

| # | Concurrent | Forme | Chemin source exact | Preuve antérieure | Ligne LIGHT ? |
|---|---|---|---|---|---|
| 1 | InterFast | seuil chiffré (500 €) | `extracted/inter-fast/activer-la-validation-des-commandes-fournisseurs.yaml` | « plafond de tolérance (ex: 500 €) [...] le processus de validation se déclenche automatiquement » | **NON** |
| 2 | Vertuoza | durée (20 jours) | `extracted/vertuoza/pourquoi-je-ne-peux-pas-recuperer-certaines-photos-ajoutees-par-mes-chefs-d-equipe-dans-les-suivis-gestionnaires.yaml` | « Si les photos datent de plus de 20 jours, elles ne seront plus sélectionnables. » | **NON** |
| 3 | InterFast | état de l'objet (devis Accepté → Opérations) | `extracted/inter-fast/creer-un-chantier-app-web.yaml` | mini-audit-B §6 ; occurrence « Opérations » confirmée dans ce fichier | **NON** |
| 4 | InterFast | rôle (Validateur exempté du plafond) | `extracted/inter-fast/activer-la-validation-des-commandes-fournisseurs.yaml` | « les profils configurés comme Validateurs [...] ne sont pas soumis au plafond » | **NON** |
| 4b | InterFast | rôle (sous-traitant sans accès Web) | `extracted/inter-fast/inviter-et-gerer-un-profil-sous-traitant.yaml` | mini-audit-B §6 ; « pas d'accès Web » | **NON** |
| 5 | InterFast | abonnement (fil de chantier « Pro ») | `extracted/inter-fast/consulter-et-utiliser-le-fil-d-activite-du-chantier.yaml` | « le fil du chantier est disponible à partir de l'abonnement Pro » | **NON** |
| 5b | InterFast | abonnement (validation commandes « Business ») | `extracted/inter-fast/activer-la-validation-des-commandes-fournisseurs.yaml` | « La validation des commandes fait partie de l'abonnement Business. » | **NON** |
| 6 | Vertuoza | réglage à la création (avancement « interne ») | `extracted/vertuoza/suivi-de-chantier-gestionnaire.yaml` | « si vous cliquez sur 'interne', vous ne pourrez pas l'envoyer par mail » | **NON** |
| 7 | Vertuoza | présence d'une donnée (responsable de réclamation) | `extracted/vertuoza/suivi-de-chantier-gestionnaire.yaml` | « si un responsable n'est pas sélectionné, alors vous ne saurez pas utiliser [les réclamations] » | **NON** |

Toutes les preuves sont exactement repointées (aucun contrôle « non
repointé »). Les 7 formes se répartissent sur 6 documents source distincts
(2 formes co-localisées dans `activer-la-validation-des-commandes-
fournisseurs.yaml`, 2 formes co-localisées dans `suivi-de-chantier-
gestionnaire.yaml`).

Recherche complémentaire effectuée sans résultat exploitable : le motif
« seuil 5 000 € » cité pour OpenFire (SCHEMA-V2.md §V3.3) n'est pas
repointé à un chemin dans ce dépôt, et OpenFire n'a de toute façon aucune
production LIGHT — non ajouté à la liste.

```
CONTROLES_H3_GELES = 7
CONTROLES_H3_AVEC_LIGNE_LIGHT = 0
```

**M = 0.** Les deux seuls concurrents porteurs de contrôles H3 démontrés
(InterFast, Vertuoza) n'ont aucune production LIGHT dans ce dépôt — ni
production complète, ni présence dans le pilote (qui les a explicitement
exclus : « aucun Vertuoza/InterFast, déjà largement couverts par les
travaux précédents »). Ce n'est pas un défaut de LIGHT : c'est une absence
de recouvrement entre les deux périmètres exécutés à ce jour.

Conformément à la clause de sortie : liste gelée telle quelle, aucun
substitut cherché, aucune définition assouplie, rien dérivé du contenu
LIGHT.

## 3. Filtre primaire — `regle_ou_condition = oui`

Exécuté mécaniquement sur les 439 observations (colonne vérifiée par
recoupement avec les agrégats publiés par Costructor/Axonaut/ProGBat —
égalité exacte dans les trois cas ; pilote sans agrégat publié, recompté
directement).

| Corpus | oui | / analysable | % |
|---|---:|---:|---:|
| Pilote | 25 | 40 | 62,5 % |
| Costructor | 68 | 94 | 72,3 % |
| Axonaut | 99 | 119 | 83,2 % |
| ProGBat | 84 | 186 | 45,2 % |
| **Total** | **276** | **439** | **62,9 %** |

## 4. Vue secondaire — `H3_COORDINATION_ROLE_CANDIDATES`

`regle_ou_condition = oui` ET (`roles` ou `permissions` présent dans
`capacites_transverses`).

**Avertissement, à ne jamais faire porter le verdict général** : cette vue
ne couvre qu'une sous-question de H3 — la conditionnalité impliquant
explicitement des rôles ou des droits. Une règle conditionnée par un
montant, une durée, un état ou un abonnement (5 des 7 formes gelées en
§2, dont les 2 seules à avoir un chemin InterFast/Vertuoza indépendant
de `roles`/`permissions`) peut ne porter aucun des deux tags. L'utiliser
comme mesure de LIGHT sur H3 rétrécirait la définition de H3 au lieu de
mesurer la carte — elle est rapportée ici uniquement à titre descriptif.

| Corpus | candidats | / analysable | % |
|---|---:|---:|---:|
| Pilote | 5 | 40 | 12,5 % |
| Costructor | 6 | 94 | 6,4 % |
| Axonaut | 16 | 119 | 13,4 % |
| ProGBat | 13 | 186 | 7,0 % |
| **Total** | **40** | **439** | **9,1 %** |

## 5. Contrôles retrouvés / manqués

**Non testable.** M = 0 : aucun des 7 contrôles gelés ne possède de ligne
LIGHT à retrouver ou à manquer. Le filtre n'a pu être confronté à aucun
cas positif connu.

## 6. Réduction de l'espace (mesurable indépendamment de M)

Filtre primaire seul, ratio exact : **276/439 retenus (62,9 %)**.

```
REDUCTION_FAIBLE → PAS_DE_REDUCTION
```

Retenir 63 % du corpus n'allège pas significativement une présélection :
plus des deux tiers des documents porteraient encore la charge de lecture
qu'une carte est censée éviter. `regle_ou_condition` est un booléen large
(toute règle ou condition mentionnée, de nature très variée — fiscale,
procédurale, contractuelle — pas seulement de coordination H3), ce qui
explique mécaniquement sa faible sélectivité : il est vrai dans la
majorité des documents de chacun des quatre artefacts, y compris ProGBat
où il reste minoritaire mais encore à 45,2 %. Aucun seuil universel n'est
posé ici ; la qualification `PAS_DE_REDUCTION` est justifiée par ce ratio
seul, pas par une norme ajoutée au schéma.

La vue secondaire (§4, 9,1 %) réduit fortement l'espace, mais seulement
sur sa sous-question restreinte — elle ne peut pas se substituer au
filtre primaire pour juger H3 dans son ensemble (§4, avertissement).

## 7. Limites affectant ce test

- **M = 0 structurel** : les corpus porteurs de contrôles H3 connus
  (InterFast, Vertuoza) et les corpus porteurs de LIGHT (pilote,
  Costructor, Axonaut, ProGBat) ne se recouvrent pas. Aucune inférence
  sur la sensibilité réelle de LIGHT n'est possible depuis ce seul fait.
- **CP-18** (`REGISTRE-CP.md`) documente que le contrat V2/V3 lui-même
  a un défaut structurel pour représenter la conditionnalité dans
  `interactions`/`transitions_objet` — un rappel que même une analyse
  V3 en aval de LIGHT n'est pas encore éprouvée pour capturer ces
  mécanismes ; ceci ne teste pas LIGHT mais borne ce qu'une future
  extraction V3 pourrait elle-même manquer.
- `regle_ou_condition` mélange par construction des règles de toute
  nature (fiscale, légale, procédurale) avec la coordination
  conditionnelle spécifique à H3 — le champ n'a jamais été conçu comme
  un filtre H3 dédié.
- Pilote : jointure par `#` fonctionnelle mais indirecte — un futur
  script devrait matérialiser cette jointure plutôt que la refaire à
  chaque analyse.

## 8. Verdict

```
TEST_H3_INCOMPLET_CONTROLES_POSITIFS_ABSENTS
```

M = 0 : sensibilité non testée, ni succès ni échec de LIGHT. La mesure de
réduction (§6) reste valide et rapportée : le filtre primaire seul montre
une réduction faible à nulle (62,9 % retenus), indépendamment de la
question de sensibilité. Ce verdict ne conclut rien sur H3_REAL_WORLD, la
prévalence des mécanismes chez les concurrents, la qualité des produits,
ni sur SUPORDO.

## 9. Suite proposée — micro-lot de validation (NON LANCÉ)

Les 7 contrôles gelés se concentrent sur 6 documents source, tous déjà lus
en V2/V3 (`extracted/inter-fast/`, `extracted/vertuoza/`) :

**Contrôles positifs (chemins réels, relatifs à `sources/`) :**
1. `inter-fast/finances/activer-la-validation-des-commandes-fournisseurs.md`
2. `inter-fast/operations/creer-un-chantier-app-web.md`
3. `inter-fast/equipe/inviter-et-gerer-un-profil-sous-traitant.md`
4. `inter-fast/operations/consulter-et-utiliser-le-fil-d-activite-du-chantier.md`
5. `vertuoza/faq-foires-aux-questions/pourquoi-je-ne-peux-pas-recuperer-certaines-photos-ajoutees-par-mes-chefs-d-equipe-dans-les-suivis-gestionnaires.md`
6. `vertuoza/gestion-de-chantier/suivi-de-chantier-gestionnaire.md`

**Contrôles négatifs (candidats, non pré-vérifiés) :** le reste du pool
déjà lu par le même instrument (V2/V3) — 10 documents InterFast et 12
documents Vertuoza restants dans `extracted/inter-fast/` et
`extracted/vertuoza/`. Leur statut « sans conditionnalité relevée » n'est
pas garanti a priori (mini-audit-B ne les cite pas comme porteurs d'une
des 7 formes, mais leur absence de citation n'a pas été relue
individuellement pour cette mission) — leur codage LIGHT confirmerait ou
infirmerait ce statut, plutôt que de le présupposer.

**Volume total du micro-lot proposé : 28 documents** (14 InterFast + 14
Vertuoza — l'intégralité de `extracted/`, un ensemble déjà borné et
naturel, très inférieur à une production complète sur ces deux corpus).

**Note explicite (SCHEMA-LIGHT.md §5)** : ces 28 documents ont déjà été lus
en V2/V3. Cela ne les exclut pas du périmètre LIGHT — « inédit » signifie
« sans observation LIGHT antérieure », pas « jamais lu par aucun
instrument ». Le coût de relecture est ici assumé et borné à 28 documents,
choisi précisément parce que c'est l'unique ensemble qui rend le test de
sensibilité H3 exécutable sans produire deux corpus entiers.

**Ce micro-lot n'est pas lancé par cette mission.**
