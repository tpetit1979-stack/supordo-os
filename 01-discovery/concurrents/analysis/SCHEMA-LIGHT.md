# SCHEMA LIGHT — Contrat canonique de production

Contrat écrit après coup, à partir de trois productions (Costructor 94, Axonaut 119, ProGBat 186) et d'un pilote (40) déjà réalisés par imitation, sans document de contrat. Il fixe les règles **à compter de maintenant**. Voir §11 pour ce qu'il ne répare pas.

## 1. Objet

LIGHT est un instrument de cartographie légère des corpus d'aide/documentation concurrentiels. Il produit une observation minimale par document, pour présélectionner des candidats à une analyse plus riche, notamment V3.

LIGHT n'est **pas** : une extraction V2/V3 ; une analyse produit SUPORDO ; une mesure d'adoption, de qualité UX ou de performance ; un instrument marketing ; une preuve d'absence fonctionnelle lorsqu'un sujet n'est pas documenté.

## 2. Périmètre

S'applique aux corpus d'aide, documentation produit, FAQ et support/troubleshooting du corpus documentaire produit.

Le corpus marketing est hors périmètre (décision 0004 : instrument distinct, non encore défini). Un contenu promotionnel trouvé **à l'intérieur** d'un corpus d'aide se classe `marketing_dans_aide` — un marqueur, pas une extension de périmètre.

## 3. Schéma canonique — 12 colonnes

Pour toute future production, dans cet ordre exact :

```
# | chemin_relatif | longueur_mots | objet_principal | moment_parcours | capacites_transverses | procedure | transition_objet | regle_ou_condition | contrainte_ou_limite | exception_ou_correction | genre_documentaire
```

`chemin_relatif` est obligatoire dans le tableau de sortie lui-même — pas seulement dans un tableau de sélection séparé.

## 4. Définition des champs

**chemin_relatif** — chemin exact du document dans le corpus. Doit permettre la reconstitution mécanique du périmètre.

**longueur_mots** — comptage mécanique des mots du corps Markdown après suppression du frontmatter YAML. Aucune estimation visuelle. Méthode et outil déclarés en tête de chaque run.

**objet_principal** — vocabulaire ouvert/émergent. Objet métier ou documentaire principalement traité. Ne jamais forcer une ontologie fermée.

**moment_parcours** — vocabulaire **fermé pendant un run, extensible entre deux runs** par décision méthodologique écrite :

```
indetermine · demande · devis · achat · chantier-intervention · facturation
```

Canonisé à partir de la pratique historique observée sur les quatre artefacts existants — ne provient pas d'un contrat antérieur. Constat à retenir : `demande` n'apparaît qu'au pilote (1 occurrence) et n'a resservi dans aucune des trois productions — la liste n'est donc pas une énumération éprouvée. En cours de run : aucune valeur nouvelle. Un document hors de toute valeur se code `indetermine`, cas journalisé.

**capacites_transverses** — vocabulaire ouvert/émergent, maximum 3 par document. Valeurs historiquement observées, liste descriptive non close :

```
automatisation · catalogue · communication · conformite_reglementaire · documents · gestion_stock · integrations · mobile · notifications · offline · paiement · permissions · photos · planning · presence_en_ligne · recherche · roles · securite_compte · support_editeur · validation
```

`—` signifie : aucune capacité transversale identifiée dans le document selon LIGHT. Ne signifie **pas** que le produit n'en possède aucune. Une nouvelle capacité peut émerger lors d'un futur run ; ne pas créer de doublon lexical d'une capacité existante — `presence_en_ligne (nouveau)` rencontré au pilote se lit prospectivement comme la racine `presence_en_ligne`, sans modification rétroactive du pilote.

**contenu_observable** — les cinq champs `procedure`, `transition_objet`, `regle_ou_condition`, `contrainte_ou_limite`, `exception_ou_correction` partagent exactement les mêmes valeurs et la même sémantique :

```
oui     — le phénomène est observable dans le contenu du document
non     — le phénomène n'est pas observable dans le contenu, selon LIGHT
inconnu — le contenu ne permet pas de trancher honnêtement
```

Règle : un `non` LIGHT ne permet jamais, à lui seul, de conclure à une absence fonctionnelle dans le produit.

**genre_documentaire** — vocabulaire ouvert par convention. Racines observées et réutilisables :

```
procedure · definitionnel · reference_configuration · autre · politique_legale · faq_depannage · marketing_dans_aide
```

Règle canonique : une annotation entre parenthèses est un commentaire ou un qualificatif, **jamais une valeur distincte** — `politique_legale (avec procédures associées)` compte comme racine `politique_legale`, `procedure (ton partiellement promotionnel)` comme racine `procedure`. Tout agrégat de `genre_documentaire` se calcule sur la racine.

## 5. Règle « inédit »

`inédit` = **sans observation LIGHT antérieure**. Une lecture antérieure via V2, V3, Analysis C, lecture flottante ou tout autre instrument n'équivaut pas à une observation LIGHT et n'exclut donc pas, par principe, un document du périmètre LIGHT.

Pour un corpus déjà largement lu avec un autre instrument, cette règle peut entraîner une relecture substantielle : avant le lancement d'un run, ce coût doit être rendu explicite. Toute exception à la règle canonique se décide et se documente **avant** l'extraction, chemins concernés à l'appui.

Ce schéma ne décide pas aujourd'hui de lancer ni de retraiter InterFast ou Vertuoza. Costructor reste une exception historique, non réparée rétroactivement.

## 6. Exclusions de périmètre

Tout document exclu est énuméré individuellement : chemin exact + motif. Un nombre total seul est insuffisant — `light-costructor-help.md` n'énumère que 8 de ses 18 exclusions ; son périmètre n'est pas reconstituable depuis le fichier seul, contrairement à Axonaut et ProGBat.

## 7. Règles d'exécution

- un document à la fois, lu intégralement ;
- ligne écrite immédiatement, avant de passer au suivant ;
- aucun préfiltrage mécanique ne dispense de lire un document du périmètre ;
- pas de recodage rétroactif après observation des agrégats, sauf erreur factuelle ou mécanique démontrée **et** journalisée ;
- conserver `inconnu` quand c'est la valeur honnête ;
- distinguer contenu documentaire et interprétation produit ;
- silence documentaire ≠ absence fonctionnelle.

Les outils mécaniques construisent le périmètre, comptent, vérifient doublons/chemins/agrégats. Ils ne remplacent jamais la lecture.

## 8. Sortie minimale d'un run

Chaque `light-<concurrent>-*.md` contient au minimum : périmètre canonique ; exclusions listées par chemin ; méthode de `longueur_mots` déclarée ; tableau LIGHT complet ; contrôles mécaniques de complétude ; journal d'incidents et corrections ; agrégats descriptifs calculés mécaniquement ; limites documentées. Aucune conclusion produit SUPORDO dans un fichier LIGHT.

## 9. Limites de LIGHT

Une carte de sélection, pas une conclusion. Ne permet pas de trancher seul : fréquence d'usage, importance métier, adoption, satisfaction, qualité UX ou du support, performance réelle, absence d'une fonctionnalité, prévalence d'un phénomène sur le marché. Un document pauvre ou vide signifie seulement : peu ou pas de contenu documentaire observable dans cette source.

## 10. Relation avec V3

LIGHT présélectionne. V3 analyse en profondeur (transitions, règles, acteurs, conditions, ruptures, continuités, preuves). LIGHT ne doit pas devenir une version simplifiée de V3 enrichie progressivement.

## 11. Compatibilité historique

Les productions antérieures ne sont pas parfaitement homogènes. Ce schéma fixe les règles à appliquer à compter de maintenant ; il ne réécrit pas rétroactivement les runs existants.

Divergences et dettes enregistrées, non réparées :

- pilote : `chemin_relatif` absent du tableau de sortie (présent seulement dans son tableau de sélection, jointure par `#`) ;
- règle « inédit » divergente : Costructor exclut Analysis C, Axonaut et ProGBat non ;
- `longueur_mots` non comparable inter-corpus : pilote/Costructor/Axonaut par estimation visuelle, ProGBat par `wc -w` frontmatter inclus ;
- agrégation de `genre_documentaire` divergente : Costructor compte les variantes annotées comme valeurs distinctes, Axonaut et ProGBat regroupent les racines — distributions historiques non comparables sans retraitement ;
- Analysis C : la liste des 37 chemins n'est pas reconstructible (4 chemins seulement retrouvés dans le dépôt) ;
- contradiction non résolue : le pilote attribue un motif à « InterFast — Analysis C », alors qu'Analysis C est définie ailleurs comme portant sur Axonaut/Costructor/OpenFire/ProGBat uniquement ;
- statut des exclusions Analysis C chez ProGBat : non déterminable depuis les fichiers.

Constat historique vérifié mécaniquement, à titre de repère et non de règle : `marketing_dans_aide` (racine) apparaît 7 fois au total — pilote 2, Costructor 0, Axonaut 1, ProGBat 4.

Ces points sont des faits et des dettes documentées. Le schéma ne les masque pas et ne cherche pas à les réparer maintenant.
