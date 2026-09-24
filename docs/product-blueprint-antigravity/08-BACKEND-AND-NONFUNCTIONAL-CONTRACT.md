# 08 — Backend & Non-Functional Contract

Ce que le futur backend Supabase devra garantir. **Aucune table, aucune migration,
aucun SQL ici** — uniquement des contraintes de conception, traduites depuis les
règles fonctionnelles établies dans `03`, `0007` et les documents précédents.
Destiné à cadrer Antigravity, pas à le remplacer.

## 1. Multi-tenant et isolation

- SUPORDO sert plusieurs entreprises (tenants) sur une infrastructure partagée. **L'isolation par tenant est la contrainte de sécurité la plus critique du produit** — au même titre que l'immuabilité de la facture (L1) est la contrainte légale la plus critique.
- Row Level Security doit être posée **dès la première migration**, pas ajoutée après coup — un rattrapage tardif de RLS sur des données déjà en production est un chantier à haut risque, pas un simple correctif.
- Tout objet métier (Client, Lieu, Devis, Facture, Catalogue, Personnel...) doit porter un identifiant de tenant dès sa conception, même en environnement pilote à un seul tenant.
- Un utilisateur externe délégué (expert-comptable — précédent Costructor, `03`) doit pouvoir accéder à un périmètre restreint d'un tenant **sans être un "personnel" de ce tenant** — l'isolation doit prévoir un accès invité scoping, pas seulement une appartenance binaire tenant/hors-tenant.

## 2. Utilisateurs, personnel, rôles

- `03` établit une distinction M14 (personnel ≠ compte utilisateur) avec une preuve faible (2/6 éditeurs) — le V1 (`07`) choisit un modèle unifié simple. **Contrainte de conception** : ne pas fusionner irréversiblement l'identité "personne physique dans l'entreprise" et "compte applicatif" dans le même identifiant technique, même si le V1 les traite comme un seul objet côté produit — pour permettre la séparation en V2 sans migration de données destructrice.
- Rôles/permissions : preuve faible dans le corpus (5/10 en LIGIGHT, jamais détaillée en audit fonctionnel). `RECOMMANDATION ANALYTIQUE` : un modèle de rôles minimal (propriétaire/administrateur/membre), pas un système d'ACL fin — cohérent avec le "1 seul utilisateur suffit" documenté chez ProGBat.

## 3. Auth

- Authentification via le fournisseur Auth de Supabase — aucune preuve corpus n'impose de mécanisme particulier, c'est un choix d'infrastructure, pas une contrainte métier.
- Le modèle d'invitation (personnel → compte utilisateur, ordre explicite chez Vertuoza — `03`) doit être représentable comme un flux en deux temps, même si le V1 le simplifie.

## 4. Storage — documents et photos

- Stockage via Supabase Storage. Deux régimes de fichiers, structurellement différents (S5, `0007`) :
  - **Documents standards** (facture PDF, bon fournisseur, notice fabricant) — pas de régime de consentement.
  - **Médias publiables** (photos susceptibles de diffusion externe) — portent obligatoirement finalité, date, auteur du consentement, droit de retrait. Cette distinction doit exister au niveau du modèle de stockage dès le V1 (mécanisme d'attachement générique, `01`/`02`), pas être ajoutée après coup sur des fichiers déjà stockés sans cette métadonnée.
- Le mode "snapshotté" documenté pour les pièces jointes de documents commerciaux (`03`, OpenFire Odoo — PDF figé à l'instant T) doit être respecté : un document généré (devis PDF, facture PDF) ne doit jamais être re-généré silencieusement avec un contenu différent sous le même identifiant.

## 5. Migrations

- Aucune migration ne doit permettre, même techniquement, une écriture directe sur une facture déjà numérotée (L1) ou un avoir déjà numéroté (L2) — la contrainte doit être posée au niveau base de données (fonction/contrainte), pas seulement au niveau applicatif, pour rester vraie même si un futur agent de code (Antigravity ou autre) écrit un chemin d'accès direct.
- Toute migration touchant Client, Devis, Facture, Catalogue doit être pensée en tenant compte de S3 (prix catalogue snapshotté) : modifier un prix catalogue ne doit **jamais** altérer une ligne déjà émise sur un document existant.
- Le modèle de données doit prévoir dès le départ un régime distinct pour une **facture importée** lors de l'onboarding (reprise d'historique depuis un autre logiciel) : elle porte une `provenance = système précédent` et n'est jamais assimilée techniquement à une facture émise nativement par SUPORDO (L4/0007, `SUPORDO_DECISION`) — sans quoi les contrôles d'immuabilité et de numérotation continue (L1/L3) appliqués aux factures natives seraient à tort imposés à des données de reprise, ou l'inverse.

## 6. Fonctions métier transactionnelles

- Les mécanismes documentés comme "toujours recalculés, jamais ressaisis" (acompte/situation/solde — le plus corroboré du corpus ; rentabilité chantier — INV-4, 3 éditeurs indépendants) doivent être implémentés comme des calculs backend fiables (fonction ou vue), **pas comme des champs librement éditables** dont la cohérence dépendrait de la discipline du frontend. C'est une garantie d'intégrité, pas une préférence d'architecture.
- Le statut de facture recalculé après rapprochement de paiement (`03`) doit suivre la même logique : dérivé, jamais un champ que l'utilisateur peut positionner à la main.

## 7. Audit et historique

- 0007 (§N) établit qu'« aucune correction n'est jamais une réécriture silencieuse de l'historique » comme constat transversal du corpus (avoir vs facture, notamment). **Contrainte de conception** : toute transition d'état verrouillante (devis signé, facture numérotée, avoir finalisé) doit laisser une trace consultable — auteur, horodatage, état précédent — même si le V1 ne construit pas encore d'écran d'audit dédié.
- Les feuilles d'heures verrouillées après validation (InterFast, `03`) suivent le même principe : une validation qui remonte automatiquement vers un agrégat financier (rentabilité) doit être traçable jusqu'à sa source.

## 8. Provenance IA ciblée (S4)

- Rappel strict de 0007 : la provenance se trace **là où elle sert** la validation, la sécurité ou la traçabilité métier — jamais comme un système de data lineage universel au niveau de chaque champ.
- Contrainte de conception concrète : tout champ alimenté par une capture IA (transcription structurée, OCR, détection visuelle — `05`) qui nourrit un document commercial (devis) ou une donnée réglementaire (parc installé, obligation d'entretien) doit pouvoir porter une marque de provenance (source = IA, horodatage, statut de validation humaine). Un champ client saisi manuellement au clavier n'a besoin d'aucune provenance.
- Ce mécanisme doit être conçu comme une capacité optionnelle activable champ par champ ou flux par flux — pas une colonne systématique sur toutes les tables.

## 9. Sécurité

- RLS + isolation tenant (§1) est la priorité de sécurité n°1.
- Les clés d'accès aux services externes (`06` : LLM, OCR, transcription, PDP, paiement) doivent être gérées côté serveur, jamais exposées côté client — cohérent avec l'exigence de neutralité fournisseur de `06` (un changement de fournisseur ne doit pas nécessiter de changement côté app cliente).
- Les données sensibles identifiées par catégorie d'intégration (`06` §1, colonne "donnée sensible") — bancaires, financières, contexte métier envoyé à un LLM — doivent transiter par des canaux chiffrés et ne jamais être journalisées en clair dans les logs applicatifs.

## 10. Environnements

- Au minimum trois environnements distincts (développement, pilote/staging, production), avec des données de tenants réels **jamais accessibles en développement**. C'est une exigence directement liée aux risques Antigravity documentés en `09` (accès à d'autres chemins locaux, écriture directe dans le dépôt principal) — l'environnement de développement d'Antigravity ne doit jamais pouvoir toucher des données de pilote réelles.
- L'environnement pilote doit permettre un test avec de vrais utilisateurs sans exposer l'infrastructure de production.

## 11. Sauvegarde et restauration

- À activer **avant** l'entrée en pilote avec de vraies données — pas après un premier incident. Aucune preuve corpus sur ce sujet (c'est une exigence d'infrastructure standard, pas une découverte du corpus).

## 12. Observabilité

- Chaque appel à un service externe (`06`) doit être observable individuellement : succès/échec, latence, coût si mesurable — en particulier pour les intégrations à conséquence d'indisponibilité "haute" (facturation électronique, paiement, LLM structurant un devis).
- Les échecs silencieux sont le risque principal identifié pour les flux IA (`05`) : un échec de transcription ou d'extraction ne doit jamais produire un résultat par défaut invisible à l'utilisateur — il doit être visible comme un échec, pas comme un succès dégradé.

## 13. Performance et hors-ligne

- Aucune preuve corpus n'impose un mode hors-ligne général (0004 : la documentation ne prouve pas l'usage réel). **Mais** la contrainte terrain identifiée en `04` (connexion intermittente sur chantier) impose un besoin ciblé : la capture (photo, note, dictée, relevé) en zone Visite/Terrain ne doit jamais dépendre d'une connexion continue pour être conservée localement en attente de synchronisation.
- Le reste du produit (bureau, facturation, planning) peut rester dépendant d'une connexion standard sans que cela ait été identifié comme un problème dans le corpus.

## 14. Interfaces avec services externes

- Chaque catégorie de besoin d'intégration (`06` §1) doit être encapsulée derrière une interface interne propre au domaine SUPORDO (ex. une interface "Transcription", une interface "PDP facturation électronique", une interface "Paiement") — jamais un appel direct à l'API d'un fournisseur depuis le code métier. C'est la contrainte la plus explicitement demandée par la mission (garder les portes ouvertes) et la plus coûteuse à corriger après coup si elle est ignorée en V1, en particulier pour la facturation électronique (`06` §2 — bascule PDP obligatoire au 01/09/2027) et le LLM (aucun cœur de produit ne doit dépendre irréversiblement d'un seul fournisseur de modèle).

## 15. Ce que ce document ne fait pas

- Ne nomme aucune table, aucune colonne, aucune fonction Postgres/Supabase précise.
- Ne choisit aucun fournisseur pour les intégrations — voir `06`.
- Ne remplace pas une revue de sécurité Supabase avant mise en production (RLS, advisors) — c'est un prérequis d'exécution, pas un livrable de ce blueprint.
