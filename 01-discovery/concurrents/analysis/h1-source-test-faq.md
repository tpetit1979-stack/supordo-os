# H1_SOURCE_TEST — genre FAQ/dépannage (Vertuoza + InterFast)

## Question

Le genre FAQ/dépannage peut-il produire des preuves positives de ruptures pertinentes pour H1 ?

## Sélection

- 17 articles Vertuoza (`faq-foires-aux-questions/`), 3 articles InterFast (seule population disponible dans ce genre sur les 9 rubriques historiques — vérifiées en entier).
- Méthode outcome-blind : filtrage par mots-clés de titre (erreur, problème, impossible, ne-fonctionne-pas, bloqué, récupérer, corriger, résoudre, pourquoi, échec, disparu, annuler…), puis sélection des N premiers résultats par ordre alphabétique. Aucun choix qualitatif sur le contenu supposé.
- Exclusion des articles déjà présents dans les 40 pilotes V2 (`comment-corriger-une-erreur-dans-un-avenant...`, `pourquoi-je-ne-peux-pas-recuperer-certaines-photos...`, `resoudre-un-ajout-d-utilisateur-par-erreur`).

## Résultat

| Concurrent | Article | Type V3 | Preuve courte |
|---|---|---|---|
| Vertuoza | `comment-gerer-les-paiements-partiels...` | `non_propagation` | paiement partiel enregistré, non visible sur le PDF/totaux |
| Vertuoza | `pourquoi-ai-je-un-message-d-erreur-...duplication-d-un-ouvrage` | `non_propagation` | changement fournisseur en bibliothèque non répercuté sur l'ouvrage |
| Vertuoza | `pourquoi-certaines-factures-apparaissent-elles-encore-...` | `non_propagation` | statut de paiement non reflété en liste avant comptabilisation |
| Vertuoza | `pourquoi-certaines-lignes-ne-sont-elles-pas-reprises-...` | `non_propagation` | lignes à 0€ absentes de la facture groupée |
| InterFast | `resoudre-les-problemes-de-synchronisation-bancaire-ponto` | `reconstruction_contexte` | dissociation bancaire : « brise la continuité de votre historique comptable » |
| InterFast | `resoudre-les-problemes-de-synchronisation-bancaire-powens` | `ressaisie` | transactions resynchronisées à re-rapprocher manuellement |
| InterFast | `resoudre-les-erreurs-sur-un-bsff` | `sortie_logiciel` | suppression d'un BSFF impossible dans InterFast, à faire sur Trackdéchets |
| InterFast | `resoudre-les-erreurs-sur-un-bsff` | `ressaisie` | BSFF sur CERFA déjà validé → recréer un nouveau CERFA |

**8 ruptures positivement documentées, sur 4 des 5 types V3.**

## Verdict

`SOURCE_CAPABLE_DE_DOCUMENTER_H1`

## Limites

- H1_SOURCE_TEST ≠ H1_REAL_WORLD : ce résultat ne confirme ni n'infirme l'existence réelle de ruptures chez ces éditeurs.
- Aucune prévalence, aucun taux extrapolable — 8/20 n'est pas une mesure de fréquence.
- Silence documentaire ≠ absence produit : les 12 articles sans rupture positive ne prouvent aucune continuité réelle.
- **Échantillon déséquilibré et concentré sur un seul éditeur.** 17 articles Vertuoza contre 3 InterFast : 85 % du volume lu vient d'un seul éditeur. La capacité du genre FAQ/dépannage n'est donc démontrée en profondeur que pour Vertuoza ; pour InterFast, elle repose sur la totalité (et non un échantillon) de sa population disponible dans ce genre, qui est elle-même très réduite. **Ce test ne prouve rien sur les FAQ des huit autres éditeurs du corpus** (aucun n'a été touché).
- **Répartition réelle des ruptures trouvées, par éditeur** : 4 ruptures Vertuoza (sur 17 articles lus, soit 4 articles distincts sur 17) et 4 ruptures InterFast (sur seulement 3 articles lus — dont 2 ruptures dans un seul article). Le compte de ruptures est donc égal entre les deux éditeurs malgré un volume de lecture très inégal ; le rendement par article est nettement plus élevé côté InterFast sur cet échantillon minuscule. Ce constat ne doit pas non plus être lu comme une mesure de prévalence — 3 articles ne permettent aucune généralisation sur InterFast.

## Signal émergent

Un cas de **sur-persistance non documentée comme telle** a été observé (Vertuoza, import de contacts) : un contact supprimé puis réimporté est réactivé, avec ses anciennes valeurs de champs conservées si le fichier réimporté ne les écrase pas explicitement — l'inverse d'une rupture. Aucun des 5 types V3 ne le couvre. Conservé tel quel, non arbitré, aucun CP créé.
