# 02 — E-Invoicing Frontend Contract

Contrat UX par état, pas une maquette. Dérivé de `01`. Applique les principes
`PREVENT`/`DETECT`/`EXPLAIN`/`RECOVER` déjà posés dans le Product Blueprint
principal (`11-SIMPLIFICATION-PRINCIPLES.md`). **Aucun état ci-dessous
n'affiche jamais un code technique brut** (`HTTP 422`, `invalid_addressing`,
`retry_too_soon`) — chaque erreur est traduite en situation exploitable par un
artisan qui n'a jamais entendu parler de PDP, PA, ou Factur-X.

Modèle par étape : Contexte → Information → Action → Résultat → Erreur
possible → Recovery.

**Correction apportée par une mission corrective ultérieure.** `01` §4bis
sépare strictement trois notions de statut : `SUPORDO UX STATE` (ce document),
`EXTERNAL TECHNICAL STATUS` et `EXTERNAL BUSINESS STATUS` (portés par
`ElectronicInvoiceExchange`, dont les libellés réglementaires exacts restent
`OPEN`). Les états « Acceptée » et « Refusée » ci-dessous sont des **états UX
SUPORDO**, choisis pour leur clarté pour l'artisan — ils ne prétendent
**jamais** être les libellés réglementaires exacts du cycle de vie externe
(inconnus à ce jour). Le mapping `EXTERNAL BUSINESS STATUS → SUPORDO UX
STATE` est **versionné** (`01` §4ter) — à réviser explicitement si les
libellés officiels, une fois connus, ne correspondent pas exactement à ce
que ce document anticipe.

## Vue d'ensemble du parcours

```
Facture prête / incomplète
        ↓ (EXPLAIN si incomplète)
Informations client manquantes ──→ corrigées
        ↓
Adresse de routage à choisir / résolue automatiquement
        ↓
Prête à transmettre
        ↓ (action utilisateur)
Transmission en cours
        ↓
   ┌────┼────┐
Transmise  Erreur temporaire  Action requise
   ↓            ↓ (retry auto)   ↓ (correction utilisateur)
Acceptée    → retour "Transmission en cours"
   ↓
(ou) Refusée → recovery (avoir, ou nouvelle tentative si légalement possible)
```

## Table des états

| État | Ce que voit l'utilisateur | Action primaire | Action secondaire | Modifiable | Non modifiable | Explication langage métier | Info technique cachée (support) |
|---|---|---|---|---|---|---|---|
| **Facture prête** | Bandeau vert, récapitulatif complet | « Transmettre » | Télécharger le PDF, modifier | Tout, tant que non transmise | — | « Votre facture est complète et prête à être envoyée électroniquement à votre client. » | `eligibility=true`, validation OK |
| **Facture incomplète** | Liste des champs manquants, en évidence sur le formulaire | « Compléter » (mène directement au champ) | Enregistrer en brouillon | Tout | — | « Il manque [le SIREN du client] pour pouvoir transmettre cette facture électroniquement. » (`PREVENT`) | Liste exacte des champs `OFFICIAL_SPEC` manquants |
| **Informations client manquantes** | Message ciblé sur la fiche client, pas seulement sur la facture | « Compléter la fiche client » | Continuer en brouillon | Fiche client | — | « Le SIREN ou le numéro de TVA de ce client est nécessaire pour la facturation électronique. » | Champ exact manquant côté Buyer (§2.2 de `01`) |
| **Destinataire introuvable** | « Nous ne trouvons pas ce client dans l'annuaire de facturation électronique » | « Vérifier le SIREN » | Contacter le support, facturer par un autre moyen si légalement possible pendant la période de transition | Fiche client | — | Traduction de l'échec `ADDRESSING` (`01` §4) — jamais affiché comme un code d'erreur brut | `routing_address` non résolue, `last_error_code` |
| **Adresse de routage à choisir** | Rare — seulement si plusieurs plateformes possibles sont détectées pour un même destinataire | Sélection guidée avec explication | Laisser SUPORDO choisir par défaut si un seul résultat fiable | Le choix | — | « Ce client peut recevoir ses factures via plusieurs services — choisissez celui qu'il utilise, ou laissez-nous deviner. » | `routing_scheme`, candidats résolus par l'annuaire |
| **Prête à transmettre** | Bouton de confirmation, résumé de ce qui va se passer | « Confirmer la transmission » | Annuler, revenir en arrière | Tout, jusqu'à confirmation | — | « Une fois transmise, cette facture ne pourra plus être modifiée directement — toute correction se fera par avoir. » (`EXPLAIN` avant l'irréversibilité, cf. matrice `01` §6 cas 6) | — |
| **Transmission en cours** | Indicateur de progression, bouton désactivé | Aucune (attente) | Consulter le statut plus tard | Rien | Tout | « Votre facture est en cours d'envoi. » | `technical_status`, `submitted_at`, `attempt_count` |
| **Transmise** | Confirmation, horodatage | Consulter, télécharger le justificatif de transmission | — | Rien (facture verrouillée, `01` §2.10) | Le contenu de la facture | « Votre facture a été transmise avec succès à la plateforme de votre client. » | `flow_id`, `tracking_id`, `acknowledged_at` |
| **Acceptée** | Statut final positif | Suivre le paiement | — | Rien | Tout | « Votre client a bien reçu et accepté cette facture. » | `business_status`, `last_status_at` |
| **Refusée** | Motif de refus traduit en langage métier, jamais le code brut | Action **déterminée au moment réel par la vérification des préconditions** (`01` §4ter) — « Émettre un avoir » seulement si les préconditions le permettent, sinon « Contacter le support » | Contacter le support | Rien sur la facture elle-même | La facture | « Votre client (ou la plateforme) a signalé un problème sur cette facture : [motif traduit]. » — la suite exacte (avoir possible ou non) dépend de l'état réel du document, jamais annoncée par défaut avant vérification (`RECOVER`, cohérent avec `01` §6 cas 6, qui documente aussi le cas où l'avoir lui-même est bloqué) | `last_error_code`, `last_error_message`, `raw_provider_reference`, `EXTERNAL BUSINESS STATUS` exact |
| **Erreur temporaire** | Bandeau discret, pas alarmant | Aucune (retry automatique en cours) | Forcer une nouvelle tentative (avec avertissement si trop tôt, cas 7 de `01` §6) | Rien | Rien | « Le service de transmission met un peu plus de temps que prévu — nous réessayons automatiquement. » | `last_error_code=timeout/unavailable`, `retry_after` |
| **Action requise** | Message explicite de ce qui bloque et comment le résoudre | Selon le blocage (corriger une donnée, contacter le support) | — | Selon le blocage | — | Jamais un message générique — toujours la cause exacte traduite (`EXPLAIN`) | Détail technique complet réservé au support |

## Règles transversales

- **PREVENT** : « Facture incomplète » et « Informations client manquantes »
  interceptent l'utilisateur **avant** la tentative de transmission, pas après
  un rejet.
- **DETECT** : toute incohérence entre les données facture et les exigences du
  format cible (§01 §5.1, mentions obligatoires) est détectée à l'étape
  VALIDATION (`01` §4), avant SUBMISSION — jamais découverte via un rejet de
  la Plateforme Agréée.
- **EXPLAIN** : chaque état d'erreur traduit systématiquement la cause exacte,
  jamais un message générique « une erreur est survenue ».
- **RECOVER** : toute correction d'une facture transmise passe par un avoir,
  jamais par une réécriture silencieuse (cohérent avec `L1`/`L2` de `0007`) —
  **mais l'avoir n'est jamais proposé par défaut sans vérification des
  préconditions réelles** (`01` §4ter). Aucune règle universelle « statut
  externe = refus ⇒ avoir automatiquement disponible » n'est codée : le cas
  Evoliz v1.56 (`01` §4bis) montre qu'un avoir peut lui-même être bloqué
  selon l'état exact du document source.

## Ce que ce document ne fait pas

Ne dessine aucune maquette pixel-perfect. Ne fixe aucun texte définitif — les
formulations ci-dessus sont des exemples de ton et de niveau de langage,
révisables au moment de la construction réelle. Ne suppose aucune capacité IA
de traduction d'erreur — la traduction en langage métier est une
responsabilité de code explicite (mapping cause → message), pas un appel à un
modèle de langage.
