# 06 — Integrations & API Horizon

Besoins d'intégration d'abord, candidats ensuite. Aucun choix de fournisseur n'est
fait ici — l'objectif est de garder les portes ouvertes (abstraction
provider-neutral) le plus longtemps possible.

**Recherche de candidats** : voir l'annexe complète et sourcée
[`06-ANNEXE-recherche-api-candidats.md`](./06-ANNEXE-recherche-api-candidats.md)
(1232 lignes, 20 catégories, recherche web du 23/09/2026, chaque affirmation
sourcée par URL). Ce document-ci en donne la synthèse condensée et l'analyse des
**besoins**, que l'annexe ne couvre pas.

## 1. Besoin d'intégration, analysé par catégorie

| Besoin | Problème résolu | Moment du workflow | Données envoyées/reçues | Sync | Criticité | Donnée sensible | Conséquence indispo | Fallback | Intérêt provider-neutral |
|---|---|---|---|---|---|---|---|---|---|
| Adresse/géocodage/carto | fiabiliser une adresse, calculer un itinéraire terrain | création Client/Lieu, planning tournée | adresse → coordonnées, itinéraire | synchrone | moyenne | non | saisie manuelle possible | oui, facile | fort — plusieurs candidats équivalents (`06-ANNEXE` §1) |
| Email transactionnel | envoyer devis/facture/notification | sortie de tout document | destinataire, pièce jointe, contenu | asynchrone | haute (devis non reçu = vente perdue) | modérée (coordonnées client) | file d'attente/retry | oui | fort |
| Agenda/calendrier | synchroniser planning terrain avec l'agenda perso/pro | planification RDV/intervention | événement, créneau | synchrone + webhook | moyenne | faible | planning interne suffit en secours | partiel (pas de push) | fort |
| SMS/messagerie | rappel RDV, confirmation | avant intervention | numéro, message court | asynchrone | moyenne | modérée | email de repli | oui | fort |
| Téléphonie (CTI) | tracer les appels clients | prise de contact | numéro, historique appel | webhook | faible-moyenne | modérée | pas de trace d'appel, dégradé pas bloquant | oui | modéré — usage optionnel V2/V3 |
| Paiement | encaisser un acompte/solde en ligne ou sur site | facturation | montant, méthode, statut | synchrone + webhook | haute | forte (donnée bancaire, jamais stockée en direct) | paiement manuel/virement classique | oui, mais coûteux à changer une fois les flux de réconciliation posés | fort |
| Banque/open banking | rapprochement automatique des paiements | après facturation | relevé, transaction | asynchrone (webhook/polling) | moyenne | forte | rapprochement manuel | oui | modéré |
| Comptabilité/expert-comptable | exporter les écritures | fin de période | facture, écriture | asynchrone (export/API) | moyenne | forte (données financières) | export manuel (FEC) | oui | fort |
| **Facturation électronique (PDP)** | obligation légale de transmission | émission de toute facture B2B | facture structurée (Factur-X) | synchrone/asynchrone selon PDP | **structurelle, non optionnelle** | forte | **blocage réglementaire si absent au 01/09/2027** | aucun — obligation légale | fort mais contraint par le calendrier légal (voir §2) |
| Identité entreprise | vérifier/préremplir une fiche client pro | création client B2B | SIRET → raison sociale, adresse | synchrone | faible | non (donnée publique) | saisie manuelle | oui, facile | fort |
| Signature électronique | faire signer un devis à distance | acceptation devis (`O2`, `03`) | document, signataire, statut | asynchrone + webhook | haute (verrou métier, `OPEN` sur son effet exact) | modérée | signature papier/mention manuscrite | oui | fort |
| Stockage documents/photos | conserver devis/factures/photos terrain | tout au long du cycle | fichier | synchrone | haute | variable (S5 — consentement média) | aucun (structurel) | Supabase Storage natif, faible urgence à abstraire | faible — déjà couvert par la cible Supabase |
| OCR | lire une plaque signalétique, un document fournisseur | relevé terrain (`05` #2) | image → texte structuré | asynchrone | moyenne | faible-modérée | saisie manuelle | oui | modéré |
| Transcription vocale | dictée terrain (`05` #1, #4) | visite/relevé | audio → texte | asynchrone | haute pour la thèse produit | faible (sauf contenu client mentionné) | saisie clavier | oui, souhaitable | fort |
| LLM | structuration, résumé, génération (`05`) | visite, relevé, devis, CRM | texte/contexte → texte structuré | synchrone/asynchrone | haute pour `05` #1/#2 | modérée (contexte métier envoyé) | dégradation gracieuse vers saisie manuelle | oui, essentiel | **très fort — ne jamais coupler le cœur produit à un seul fournisseur LLM** |
| Vision/image AI | détection anomalie, lecture image (`05` #2/#3) | relevé terrain | photo → description/détection | asynchrone | moyenne, forte si #3 activé | modérée | pas de détection, capture brute conservée | oui | fort |
| Catalogues fabricants BTP | alimenter le catalogue pack métier (`02`) | configuration pack, création ligne devis | référence produit → prix/caractéristiques | asynchrone (peu de temps réel) | moyenne | non | saisie manuelle du catalogue | **non pertinent en V1** — marché peu digitalisé (voir §3) | faible à ce stade |
| Météo | anticiper une intervention terrain (secondaire) | planification | lieu → prévision | synchrone | faible | non | aucune conséquence bloquante | oui | faible priorité |
| Notifications push | alerter sur mobile (RDV, relance) | tout au long du cycle | device token, message | asynchrone | moyenne | faible | email/SMS de repli | oui | modéré |
| Portail client | consulter devis/factures en autonomie | après émission de document | lecture seule de documents | synchrone | moyenne | modérée | envoi par email classique | **à construire en interne** (voir §3) | sans objet — pas une brique tierce |

## 2. Facturation électronique — le besoin le plus structurant (priorité de recherche du PO)

Calendrier consolidé par décret n° 2026-677 du 27/07/2026 (source : annexe §9) :
**réception obligatoire pour toutes les entreprises depuis le 1er septembre 2026** ;
**émission obligatoire pour les TPE/PME — le cœur de cible SUPORDO — au 1er
septembre 2027**. SUPORDO sera une **« Solution Compatible »**, pas une Plateforme
Agréée : le produit doit s'intégrer en API à une Plateforme de Dématérialisation
Partenaire (PDP) de la liste officielle DGFiP, pas construire sa propre
plateforme de facturation électronique.

**Conséquence de conception directe** : l'abstraction "facturation électronique"
doit être posée comme une interface vers un PDP interchangeable dès la conception
du module Facture (`03`), et non comme un appel direct câblé à un fournisseur. Ne
pas provider-lock ce point serait une erreur `STRUCTURAL` coûteuse à corriger après
la bascule de septembre 2027.

**Points signalés non vérifiés en source primaire par la recherche (annexe §9)** :
nombre exact de PDP enregistrées, version précise de la norme Factur-X, URL Chorus
Pro actuelle — **à revérifier avant de figer tout texte contractuel ou toute
architecture d'intégration**, cette recherche datant du 23/09/2026.

## 3. Deux besoins où la recherche a produit une conclusion négative claire

- **Catalogues fabricants/distributeurs BTP** (§17 de l'annexe) : secteur peu
  digitalisé, **aucun standard API unique** ; seul Rexel a une offre API B2B
  publiquement annoncée. `RECOMMANDATION ANALYTIQUE` : ne pas prévoir d'intégration
  catalogue temps réel en V1 — construire le catalogue de chaque pack métier comme
  donnée saisie/importée, pas comme flux synchronisé.
- **Portail client** (§20 de l'annexe) : aucune brique tierce pertinente
  identifiée. `RECOMMANDATION ANALYTIQUE` : fonctionnalité à construire en interne
  (lecture seule des documents déjà émis), pas une intégration à chercher.

## 4. Candidats retirés en cours de recherche (documentés, pas simplement supprimés)

- **QuickBooks** — retiré du marché français fin 2023, écarté de la catégorie comptabilité.
- **GoCardless Bank Account Data** — nouvelles inscriptions fermées depuis juillet 2025, écarté de la catégorie open banking.

## 5. Ce que ce document ne fait pas

- Ne choisit **aucun** fournisseur — chaque besoin garde plusieurs candidats viables (détail complet dans l'annexe).
- Ne fixe aucun contrat, aucune clé d'API, aucun prix engageant — plusieurs pages officielles de tarification étaient inaccessibles au moment de la recherche (403, rendu JS) et sont signalées comme telles dans l'annexe plutôt que masquées.
- La priorité relative de branchement effectif (quel besoin en premier) relève de `07-V1-V2-V3-80-20.md`, pas de ce document.
