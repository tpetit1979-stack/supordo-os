# 05 — Acceptance & Negative Test Matrix

Tests futurs à préparer pour la tranche e-invoicing/comptabilité. **Aucun test
n'est codé ici** — définition seulement, à instancier au moment où la tranche
est ouverte, dans le même esprit que `13-ACCEPTANCE-NEGATIVE-TEST-MATRIX.md`
du Product Blueprint principal (jamais « build réussi »/« page visible »/
« API 200 » comme preuve suffisante).

## CANONICAL DATA

| Test | Description |
|---|---|
| Facture complète | Toutes les mentions obligatoires (`01` §2, §5.1) présentes → éligible à la génération de format sans erreur de validation. |
| Données obligatoires manquantes | SIREN acheteur absent, ou numéro de TVA absent sur une facture &gt; 150 € HT → rejet à l'étape VALIDATION (`01` §4), jamais à SUBMISSION. |
| TVA multiples | Une facture porte plusieurs lignes à taux de TVA différents (cas BTP mixte main d'œuvre/fourniture, `01` §2.4 — **corrigé : un seul taux par ligne, EN 16931 BT-151/BT-152**, la multiplicité se joue entre lignes) → ventilation agrégée correcte par taux au niveau facture (BT-118/BT-119). Test négatif complémentaire : une tentative de porter plusieurs taux sur une seule ligne est rejetée à la validation, pas silencieusement acceptée. |
| Snapshot Seller/Buyer/Lieu à l'émission | Modifier le Lieu ou l'identité du Client après émission d'une facture ne modifie jamais les données historisées sur cette facture (`01` §2.1, y compris le SIREN utilisé pour un éventuel adressage électronique) — tout en gardant le lien métier vers le Lieu/Client navigable. |
| Avoir | Un avoir généré depuis une facture porte la référence directe et bidirectionnelle vers son origine (`01` §2.7 — contrairement au modèle Evoliz sans FK directe). |
| Particulier vs entreprise | Une facture à un particulier (pas de SIREN acheteur) reste valide — ne pas exiger un champ obligatoire uniquement pour les entreprises. |
| Lieu de prestation distinct | Une facture dont le Lieu SUPORDO diffère de l'adresse de facturation du Client conserve les deux informations séparément, sans fusion (`01` §2.1). |

## IMMUTABILITY

| Test | Description |
|---|---|
| Facture définitive non modifiable | Une facture numérotée (statut commercial verrouillé, `L1`/`0007`) refuse toute modification de contenu, y compris par un chemin direct contournant l'API applicative — même exigence que `13` §T4 du Product Blueprint principal, étendue ici à toute tentative de modification **après transmission électronique**. |
| Artefact transmis non régénérable silencieusement | Le fichier Factur-X/UBL/CII effectivement transmis reste identique à l'archive conservée, même si le mapper est mis à jour entre-temps (`01` §3). |

## IDEMPOTENCY

| Test | Description |
|---|---|
| Double clic | Deux clics rapprochés sur « Transmettre » ne produisent qu'une seule soumission réelle (`01` §6 cas 1). |
| Double POST | Deux appels API identiques avec la même clé d'idempotence ne produisent qu'un seul effet (`03` §3). |
| Retry après timeout | Un retry automatique après timeout ne duplique pas la transmission si le provider avait en réalité déjà reçu la facture (`01` §6 cas 3-4). |
| Webhook dupliqué | Un même statut reçu deux fois du provider n'applique son effet qu'une seule fois (`01` §6 cas 8). |

## PROVIDER FAILURE

| Test | Description |
|---|---|
| Indisponible | Le provider ne répond pas → mise en file d'attente explicite, jamais un échec silencieux (`01` §6 cas 10). |
| Timeout | Le provider dépasse le délai de réponse → comportement défini en `01` §6 cas 3, pas un retry sauvage. |
| Auth expirée | Les identifiants du provider adapter ont expiré → échec détecté et remonté comme « Action requise » côté support, jamais confondu avec un rejet métier de la facture. |
| Mapping invalide | Un mapping comptable (§12 de `04`) mal configuré empêche l'export → échec explicite, jamais une donnée poussée avec un compte erroné par défaut. |
| Destinataire introuvable | L'annuaire ne résout aucune Plateforme Agréée pour le SIREN du client → état « Destinataire introuvable » côté frontend (`02`), jamais un blocage muet. |

## SECURITY

| Test | Description |
|---|---|
| Cross-tenant read (échange) | Tenant A ne peut jamais lire l'`ElectronicInvoiceExchange` du tenant B, y compris via un accès direct à la donnée. |
| Cross-tenant write (échange) | Tenant A ne peut jamais déclencher ou modifier une transmission pour une facture du tenant B. |
| Expert externe scopé | Un compte expert-comptable délégué ne voit que les tenants explicitement autorisés, jamais la liste complète des tenants de la plateforme. |
| Secret provider jamais exposé | Aucune clé d'authentification vers un provider n'apparaît dans une réponse API consommée par le navigateur, ni dans un log accessible au frontend. |

## RECOVERY

| Test | Description |
|---|---|
| Rejet | Une facture refusée par la Plateforme Agréée ne propose un avoir **qu'après vérification des préconditions réelles** (`01` §4ter, §6 cas 6) — jamais une réécriture de l'originale. Test négatif complémentaire : simuler un état où l'avoir lui-même serait bloqué (document source non déposé/refusé/rejeté, pattern observé chez Evoliz v1.56) et vérifier que le système l'explique plutôt que d'échouer silencieusement. |
| Erreur temporaire | Une erreur temporaire n'engage aucune action utilisateur destructive — le système reste en état cohérent en attendant la résolution automatique. |
| Correction autorisée | Une correction de données client (SIREN corrigé après échec d'adressage) permet une nouvelle tentative sans dupliquer l'historique de tentatives précédentes. |
| Nouvelle transmission légalement possible | Le système ne propose une nouvelle transmission que dans les cas où c'est légalement licite (ex. avant acceptation confirmée) — jamais après un statut business définitif accepté. |

## FORMAT

| Test | Description |
|---|---|
| Canonical invoice → format attendu | Une facture canonique complète se projette sans perte vers le profil Factur-X ciblé (`01` §3), avec les champs obligatoires de la norme EN 16931 correctement peuplés. |
| Version mapper connue | Chaque artefact généré porte un `format_version` traçable et vérifiable a posteriori. |
| Round-trip / validation | Quand un outil de validation officiel ou reconnu est disponible, l'artefact généré est validable contre le schéma du profil choisi avant toute transmission réelle. |

## Ce que ce document ne fait pas

Ne code aucun test. Ne choisit aucun framework de test. Ne fixe aucune
donnée de test réelle (aucun SIREN, aucune entreprise réelle ne doit être
utilisée, même en exemple, dans une implémentation future de ces tests).
