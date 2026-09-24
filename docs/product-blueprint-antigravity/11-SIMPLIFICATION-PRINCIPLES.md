# 11 — Simplification Principles

Transformation des frictions de `10-SUPPORT-FRICTION-RECOVERY-ATLAS.md` en
principes de conception PREVENT / DETECT / EXPLAIN / RECOVER pour SUPORDO.
Chaque principe reste une `RECOMMANDATION ANALYTIQUE` jusqu'à décision PO
explicite — aucun n'est présenté comme acté.

Format : SOURCE DU PROBLÈME · RAISONNEMENT · RECOMMANDATION SUPORDO · RISQUE DE
SUR-SIMPLIFICATION · VALIDATION TERRAIN NÉCESSAIRE OU NON.

---

## PREVENT — empêcher l'erreur avant qu'elle arrive

### P1 — Aucune suppression dure sur un document engagé

- **SOURCE DU PROBLÈME** : `10` M4 (motif le mieux corroboré, 5/10 indépendants) et son exception la plus grave — Vertuoza, suppression de facture strictement irréversible sans corbeille ni délai de grâce.
- **RAISONNEMENT** : le marché converge massivement vers le soft-delete/archivage réversible sur les objets métier centraux ; la seule exception documentée (Vertuoza facture) est aussi la friction la plus dangereuse du corpus entier.
- **RECOMMANDATION SUPORDO** : aucun document engagé (devis envoyé, facture, avoir, chantier avec activité) n'est supprimable en dur — seulement archivable/annulable de façon réversible. Un devis brouillon jamais envoyé reste supprimable en dur (pas d'irréversibilité à créer là où le marché n'en documente aucune).
- **RISQUE DE SUR-SIMPLIFICATION** : rendre absolument tout indestructible pourrait gêner la correction rapide d'une erreur de saisie triviale sur un objet jamais engagé — la limite proposée (brouillon jamais envoyé) doit rester nette, pas floue.
- **VALIDATION TERRAIN NÉCESSAIRE** : non — cohérent avec L1-L3 déjà actés dans `0007`.

### P4 — Création contextuelle étendue au-delà du client déjà acté (M1/0007)

- **SOURCE DU PROBLÈME** : asymétrie documentée `03` (OpenFire crée le client à la volée mais pas le produit) et Sellsy (le prospect ne peut créer qu'un devis, rien d'autre, avant conversion — pertinent pour Q19/`12`).
- **RAISONNEMENT** : le principe de création contextuelle sans quitter le flux est déjà une `MARKET_BASELINE` forte pour le client (8/8) — le corpus montre que son absence pour d'autres objets légers (lieu, contact secondaire) est vécue comme une friction, même si non nommée comme telle par les éditeurs.
- **RECOMMANDATION SUPORDO** : étendre la création contextuelle (sans changer d'écran) à tout objet léger nécessaire en cours de flux — pas seulement le client déjà couvert par `07`.
- **RISQUE DE SUR-SIMPLIFICATION** : créer trop facilement des objets à la volée sans aucun contrôle augmente le risque de doublons silencieux (voir P5 ci-dessous, couplage nécessaire).
- **VALIDATION TERRAIN NÉCESSAIRE** : non pour le principe, oui pour la liste exacte des objets à couvrir en V1.

### P8 — Discipline stricte "jamais un état dérivé n'est saisissable" étendue

- **SOURCE DU PROBLÈME** : déjà acté partiellement (`08` §6, INV-4, INV-3C-1) ; ce mining ajoute deux preuves supplémentaires de ce qui arrive quand ce n'est pas respecté — Vertuoza (« reste à produire » désynchronisé de l'état facturé réel, M18) et Sellsy (montant dû GoCardless non recalculé après annulation, M7).
- **RAISONNEMENT** : chaque fois qu'un concurrent laisse un indicateur agrégé se désynchroniser de sa source, c'est une confusion utilisateur documentée, jamais un avantage.
- **RECOMMANDATION SUPORDO** : étendre la discipline déjà posée en `08` §6 à **tout** indicateur agrégé affiché à l'utilisateur (pas seulement acompte/solde et rentabilité déjà couverts) — jamais de champ éditable pour une valeur dérivée, y compris les indicateurs secondaires (statuts d'avancement, montants dus après annulation).
- **RISQUE DE SUR-SIMPLIFICATION** : aucun identifié — c'est un renforcement d'une conviction déjà forte, pas une nouvelle contrainte.
- **VALIDATION TERRAIN NÉCESSAIRE** : non.

### P13 — Reset de mot de passe standard

- **SOURCE DU PROBLÈME** : `10` M10 — Vertuoza n'a aucun flux de reset, la solution officielle est de supprimer le compte utilisateur et d'en recréer un.
- **RAISONNEMENT** : c'est un contre-exemple net, pas un motif de marché à répliquer — aucun autre concurrent du corpus ne documente une absence de reset.
- **RECOMMANDATION SUPORDO** : un flux de réinitialisation de mot de passe self-service standard fait partie de `T0` (`12`), sans débat produit — c'est une exigence Auth infrastructure (`08` §3), pas une question métier.
- **RISQUE DE SUR-SIMPLIFICATION** : aucun.
- **VALIDATION TERRAIN NÉCESSAIRE** : non.

---

## DETECT — détecter l'incohérence avant dommage

### P5 — Détection de doublon non bloquante à la création/import

- **SOURCE DU PROBLÈME** : `10` M6/M19 — Extrabat (orthographe différente = doublon silencieux), Sellsy (critère de dédoublonnage mal choisi crée des doublons ou écrase des données silencieusement à l'import).
- **RAISONNEMENT** : aucun concurrent du corpus mining ne documente de détection de doublon proactive — c'est un vide de marché réel, pas seulement une lacune isolée chez un éditeur.
- **RECOMMANDATION SUPORDO** : suggestion de doublon probable (nom proche, téléphone/email identique) à la création d'un client, **non bloquante** — cohérent avec S2/M1 (création à la volée jamais entravée).
- **RISQUE DE SUR-SIMPLIFICATION** : des faux positifs fréquents ralentiraient la création rapide en mobilité, à l'opposé de l'objectif de `T1`.
- **VALIDATION TERRAIN NÉCESSAIRE** : oui — calibrage du seuil de similarité, aucune preuve corpus disponible sur ce point.

### P10 — IA jamais finalisée sans validation humaine (confirmation, pas nouveauté)

- **SOURCE DU PROBLÈME** : `10` M12, maintenant **3 témoins `ACQUIS DOCUMENTAIRE` indépendants** (InterFast, OpenFire Zendesk, Obat) — voir `10` §0.3.
- **RAISONNEMENT** : ce principe était déjà posé en `05` comme discipline transversale ; le mining élève son niveau de preuve de "précédent plausible" à "motif de marché confirmé par 3 sources fonctionnelles indépendantes".
- **RECOMMANDATION SUPORDO** : aucun changement de politique — noter simplement que `05` (opportunité #1, validation humaine systématique) est maintenant mieux corroborée qu'au moment de sa rédaction.
- **RISQUE DE SUR-SIMPLIFICATION** : aucun — le principe est déjà conservateur par construction.
- **VALIDATION TERRAIN NÉCESSAIRE** : non pour le principe ; oui pour l'ergonomie exacte de validation sur mobile (déjà signalé `04`/`05`).

### P15 — Avertir avant d'atteindre une limite technique dure

- **SOURCE DU PROBLÈME** : `10` — Extrabat (limite de 3 exercices comptables, jamais mentionnée ailleurs dans le corpus), Costructor (5000 lignes par import catalogue).
- **RAISONNEMENT** : ces limites existent réellement chez au moins deux éditeurs indépendants et ne sont documentées qu'au moment de l'échec, jamais en amont.
- **RECOMMANDATION SUPORDO** : si une limite technique dure est introduite (import catalogue notamment, pertinent pour `T-PACK-CLIM`), elle doit être communiquée à l'utilisateur avant qu'il ne l'atteigne, pas découverte à l'échec.
- **RISQUE DE SUR-SIMPLIFICATION** : construire un système d'avertissement générique pour des limites hypothétiques qui n'existeront peut-être jamais dans l'architecture Supabase cible serait une sur-ingénierie — à appliquer seulement si une limite dure réelle est introduite.
- **VALIDATION TERRAIN NÉCESSAIRE** : non, conditionnel à l'existence d'une limite.

---

## EXPLAIN — montrer clairement pourquoi une action est impossible ou quel état existe

### P3 — Afficher la dépendance cachée au moment du blocage, pas dans une page séparée

- **SOURCE DU PROBLÈME** : `10` M3, le motif le plus riche du corpus (7/10) — Extrabat (IBAN caché dans un template), OpenFire Odoo (ordre remise bancaire/lettrage), InterFast (facture de solde bloque l'avoir d'acompte), Obat (acompte bloque l'avoir détaillé).
- **RAISONNEMENT** : dans tous les cas, le blocage a une cause réelle et légitime — mais aucun concurrent ne l'affiche au moment de l'échec, l'utilisateur la découvre après coup ou doit lire une page d'aide séparée.
- **RECOMMANDATION SUPORDO** : toute action bloquée par l'état d'un objet lié doit afficher, **au moment même du blocage**, quel objet et quel état le bloque, avec un accès direct pour le résoudre si possible — pas un message générique "action impossible".
- **RISQUE DE SUR-SIMPLIFICATION** : sur-expliquer chaque contrainte technique en détail pourrait noyer l'utilisateur en mobilité (mains occupées, écran réduit) — le message doit rester court et actionnable, pas un essai explicatif.
- **VALIDATION TERRAIN NÉCESSAIRE** : oui, pour le format exact du message sur mobile.

### P7 — Bascule de conformité au niveau du compte = moment de décision solennel

- **SOURCE DU PROBLÈME** : `10` M13, motif nouveau — Sellsy (« Mode conforme », irréversible, présenté sobrement en article d'aide) vs Obat (migration de PDP, dépendance externe complexe rendue invisible à l'utilisateur, exemple positif).
- **RAISONNEMENT** : `08`/`09` couvrent l'irréversibilité au niveau document, pas au niveau compte entier — c'est un angle mort identifié par ce mining, pas par le blueprint initial.
- **RECOMMANDATION SUPORDO** : toute bascule irréversible au niveau du compte (facturation électronique, changement de PDP, tout futur "mode conforme") passe par un écran de confirmation dédié avec conséquences explicites — jamais un simple interrupteur dans les paramètres.
- **RISQUE DE SUR-SIMPLIFICATION** : multiplier les écrans de confirmation solennels pour des réglages en réalité anodins lasserait l'utilisateur — réserver ce traitement aux bascules réellement irréversibles.
- **VALIDATION TERRAIN NÉCESSAIRE** : non — question de discipline UX, pas de fait de marché à confirmer.

### P14 — Traduire les erreurs d'intégration externe en langage utilisateur actionnable

- **SOURCE DU PROBLÈME** : `10` M5 — Vertuoza (~40 codes d'erreur de synchronisation comptable exposés bruts) vs Obat (table diagnostic cause→action pour les erreurs de facturation électronique, exemplaire).
- **RAISONNEMENT** : les deux éditeurs traitent le même type de problème (échec d'intégration externe) avec une maturité radicalement différente — le modèle Obat est directement transposable.
- **RECOMMANDATION SUPORDO** : toute intégration externe (banque, PDP, futur Trackdéchets si pack froid/climatisation) doit traduire ses erreurs en langage utilisateur avec une action suggérée — suivre le modèle Obat, jamais afficher un code opaque seul.
- **RISQUE DE SUR-SIMPLIFICATION** : traduire chaque code d'erreur externe est un travail d'intégration non négligeable — acceptable de le limiter aux intégrations V1 (`06`) et différer les intégrations secondaires en V2/V3.
- **VALIDATION TERRAIN NÉCESSAIRE** : non.

### P16 — Si un objet Demande/Lead est construit, ne pas répéter le piège Sellsy

- **SOURCE DU PROBLÈME** : `10` — Sellsy, un prospect ne peut créer qu'un devis, aucun autre document, avant transformation en client.
- **RAISONNEMENT** : cette friction est un premier élément factuel (1 témoin) pour la question Q19 (`12`, objet Demande/Lead) — encore `CAN_WAIT_V2`, mais si elle est un jour tranchée positivement, ce piège est déjà documenté et évitable.
- **RECOMMANDATION SUPORDO** : conditionnelle — **si** Q19 est tranchée en faveur d'un objet Demande/Lead, ne pas restreindre rigidement ses capacités avant conversion en client.
- **RISQUE DE SUR-SIMPLIFICATION** : sur-investir dans ce principe avant que Q19 soit tranchée serait prématuré.
- **VALIDATION TERRAIN NÉCESSAIRE** : non dans l'immédiat — dépend d'abord d'une décision PO sur Q19.

---

## RECOVER — permettre de réparer ou revenir à un état sûr

### P2 — Annuler un engagement (signature/acceptation) sans casser l'historique

- **SOURCE DU PROBLÈME** : `10` §2 M2 — Obat (« variantes de devis », annulation de signature sans renommage ni casse des références, RECOVER exemplaire) vs Vertuoza (retour au statut précédent d'un devis accepté **retiré du produit** car il supprimait tout le chantier lié, `03`/`10`).
- **RAISONNEMENT** : Q3 (`09`, verrou de mutabilité) reste `OPEN` — ce principe ne prétend pas la trancher, mais montre qu'un mécanisme de recovery de l'**engagement** (distinct de l'édition de **contenu**, voir `12` §0.5) est possible sans compromettre l'intégrité des objets déjà créés en aval, si conçu comme un événement propre plutôt qu'un retour en arrière destructif.
- **RECOMMANDATION SUPORDO** : quel que soit le modèle retenu pour Q3, prévoir dès `T3` (`12`) un mécanisme explicite « annuler l'engagement » distinct de « modifier le contenu », inspiré du modèle Obat plutôt que du modèle Vertuoza (retiré car destructeur).
- **RISQUE DE SUR-SIMPLIFICATION** : si l'annulation d'engagement devient trop facile, elle pourrait être utilisée pour contourner l'irréversibilité légale par la bande (ex. annuler un devis juste avant facturation pour changer des prix rétroactivement) — le recovery doit être borné : impossible dès qu'un objet aval légalement contraint (facture) existe.
- **VALIDATION TERRAIN NÉCESSAIRE** : oui — fréquence réelle du besoin de correction post-engagement inconnue du corpus.

### P6 — Ne jamais perdre une capture terrain, même hors connexion

- **SOURCE DU PROBLÈME** : `10` M17, 3 concurrents indépendants (Extrabat, Obat, Batikko) convergent sur la capture terrain offline-tolerant avec synchronisation différée.
- **RAISONNEMENT** : ce n'est plus seulement une exigence déduite de la contrainte métier (déjà posée `08` §13) — c'est maintenant un motif de marché observé chez plusieurs éditeurs indépendants, ce qui renforce sa priorité.
- **RECOMMANDATION SUPORDO** : confirmation du principe déjà posé en `08` §13 pour `T8` (`12`) — brouillon local systématique pour toute capture, synchronisation différée à la reconnexion.
- **RISQUE DE SUR-SIMPLIFICATION** : la complexité technique réelle de la synchronisation offline (conflits, doublons potentiels lors de la reconnexion) ne doit pas être sous-estimée malgré la simplicité apparente du principe énoncé.
- **VALIDATION TERRAIN NÉCESSAIRE** : oui — comportement réseau réel sur chantier, déjà signalé `04`/`09` Q15/Q16.

### P9 — Un contournement manuel documenté par un concurrent est un signal de capacité produit manquante

- **SOURCE DU PROBLÈME** : `10` M14 — InterFast (double CERFA manuel pour rattraper un oubli, risque de double comptage de stock si mal exécuté), Extrabat (orthographe exacte requise à l'import, sinon doublon silencieux).
- **RAISONNEMENT** : chaque fois qu'un centre d'aide concurrent documente une procédure manuelle en plusieurs étapes pour une opération qui devrait être simple, c'est le signe qu'aucun mécanisme produit adapté n'existe chez cet éditeur — un candidat direct de capacité à construire nativement dans SUPORDO plutôt que documenter un contournement équivalent.
- **RECOMMANDATION SUPORDO** : traiter chaque contournement documenté à fort risque (financier ou réglementaire) comme un candidat de fonctionnalité native, priorisé par le risque associé — le cluster BSFF/CERFA (`10` §2) et les imports de catalogue (marge/prix silencieusement écrasés) sont les candidats les plus urgents pour le pack climatisation/PAC.
- **RISQUE DE SUR-SIMPLIFICATION** : construire un mécanisme natif pour chaque contournement documenté serait démesuré en V1 — se limiter aux cas à fort risque financier/réglementaire identifiés en `10` §4.
- **VALIDATION TERRAIN NÉCESSAIRE** : non pour le principe, oui pour la priorisation exacte.

### P11 — Provenance renforcée (scellement) pour la photo quand elle sert de preuve juridique

- **SOURCE DU PROBLÈME** : `10` M15 — Obat (Certificall, scellement horodaté + hash) et Batikko (Certigna, équivalent), deux éditeurs indépendants convergents.
- **RAISONNEMENT** : S4 (`0007`) prévoit déjà que la provenance se trace là où elle sert la validation, la sécurité ou la traçabilité — la photo de chantier utilisée en cas de litige est un cas d'usage réel et documenté de ce principe, pas une extrapolation.
- **RECOMMANDATION SUPORDO** : concevoir l'architecture de stockage photo (`08` §4) pour permettre, en V2/V3, un scellement (horodatage + hash) sur les photos identifiées comme juridiquement sensibles par le pack métier — sans nécessairement construire de partenariat tiers dès V1.
- **RISQUE DE SUR-SIMPLIFICATION** : sceller systématiquement chaque photo (y compris les photos de contexte non probantes) serait un coût inutile — réserver le mécanisme aux cas identifiés par le pack métier comme juridiquement sensibles.
- **VALIDATION TERRAIN NÉCESSAIRE** : oui — quel usage réel de la preuve photo en cas de litige chantier, aucune preuve corpus au-delà de l'existence du service tiers chez deux éditeurs.

### P12 — Modèle de permission simple en V1, mais architecturé pour être extensible

- **SOURCE DU PROBLÈME** : `10` M9 — Vertuoza (permission grossière, fuite d'accès résiduelle admise par l'éditeur), Costructor (9 rôles sans matrice comparative, mauvais exemple), Obat (7 rôles + permissions individuelles, contre-exemple riche, voir `10` §0.2).
- **RAISONNEMENT** : la recommandation V1 déjà actée (`07`/`08`/`09` Q11 — rôles minimaux) reste valable, mais ne peut plus être justifiée par une absence de preuve de marché (`10` §0.2 corrige cette justification) — un système fin existe réellement (Obat).
- **RECOMMANDATION SUPORDO** : garder un modèle de rôles minimal en V1 (`RECOMMANDATION ANALYTIQUE` inchangée) mais concevoir le modèle de données de permission pour rester extensible vers un système fin (à la Obat) sans réécriture majeure en V2/V3.
- **RISQUE DE SUR-SIMPLIFICATION** : sous-dimensionner l'architecture de permission dès le départ (pas seulement l'UI, le modèle de données) pourrait coûter cher à étendre plus tard.
- **VALIDATION TERRAIN NÉCESSAIRE** : non — question d'architecture technique, pas de fait de marché supplémentaire à confirmer.

---

## Synthèse — dix principes les plus prometteurs

Sélection pour la sortie terminale de la mission, par ordre d'importance perçue
(effet domino + risque évité + facilité d'application en V1) : P1, P3, P2, P8,
P4, P6, P14, P5, P9, P7. Les six autres (P10, P11, P12, P13, P15, P16) restent
documentés ci-dessus mais sont soit des confirmations de principes déjà actés
(P10, P13), soit conditionnels/V2-V3 (P11, P12, P15, P16).
