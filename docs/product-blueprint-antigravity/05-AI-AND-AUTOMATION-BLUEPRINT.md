# 05 — AI & Automation Blueprint

Carte des opportunités IA — pas une rubrique gadget. Principe directeur du PO (§2 de
la mission) : la voix, la photo et l'IA doivent devenir des **moyens de capturer et
structurer de l'information métier**, pas des fonctionnalités ajoutées au CRM. Ce
document teste explicitement l'hypothèse **VOIX + VERTICAL MÉTIER + CATALOGUE +
RELEVÉ TECHNIQUE**, désignée par le PO comme porteuse de plus de valeur qu'un simple
assistant conversationnel.

**Aucune de ces opportunités n'est un acquis du corpus.** Le corpus documente deux
précédents fonctionnels réels proches de la cible (InterFast « Visite avant devis »,
OpenFire Zendesk « Vital Études » — `03`/`04`) et deux revendications marketing
(`MARKETING_ONLY`) : Vertuoza (devis vocal 45s) et Batikko (devis vocal BTP avec
structuration TVA). Aucune de ces quatre sources ne permet d'auditer la fiabilité
réelle du mécanisme — elles prouvent une **faisabilité de marché**, pas une
**qualité**.

Format par opportunité : job utilisateur, entrées, contexte disponible,
transformation, sortie structurée, action possible, risque d'erreur, validation
humaine nécessaire, provenance à conserver (S4/0007), décision automatique
autorisable ou suggestion seulement, version cible.

## 1. Devis vocal en sortie de visite terrain (opportunité phare)

- **Job utilisateur** : structurer un devis exploitable sans ressaisie au bureau, immédiatement après une visite.
- **Entrées** : voix (dictée libre ou guidée par le relevé), photos prises pendant la visite, relevé structuré s'il existe.
- **Contexte disponible** : pack métier actif (`02`), catalogue du pack, lieu, client, historique du lieu.
- **Transformation** : extraction (structuration voix→champs), classification (rattachement aux articles du catalogue du pack), génération (lignes de devis brouillon).
- **Sortie structurée** : lignes de devis à l'état brouillon, jamais finalisées automatiquement.
- **Action possible** : pré-remplir le devis ; ne jamais l'envoyer ni le signer automatiquement.
- **Risque d'erreur** : mauvaise interprétation d'une quantité, d'une référence produit ou d'un prix — coût direct si le devis part sans relecture.
- **Validation humaine nécessaire** : **oui, systématique**, avant tout envoi. Cohérent avec le seul document du corpus qui documente ce principe explicitement (Batikko, `MARKETING_ONLY` : « vous gardez la main, l'IA fait le brouillon »).
- **Provenance à conserver** : oui — nécessaire à la validation (S4).
- **Décision automatique autorisable** : non — suggestion uniquement.
- **Version cible** : `V1` pour un pilote sur le pack métier retenu (transcription + rattachement catalogue simple) ; `EXPERIMENTAL` pour la structuration automatique complète en lignes prêtes à valider.

## 2. Relevé technique guidé (formulaire vertical + photo)

- **Job utilisateur** : ne rien oublier des données nécessaires au dimensionnement/chiffrage pendant la visite.
- **Entrées** : réponses à un formulaire conditionnel (`VERTICAL_CAPTURE`, `02`), photos, position optionnelle.
- **Contexte disponible** : pack métier actif, parc installé déjà connu sur ce lieu s'il existe.
- **Transformation** : extraction (OCR plaque signalétique), classification (type d'équipement), suggestion.
- **Sortie structurée** : fiche de relevé typée, rattachée au lieu.
- **Action possible** : préremplir le parc installé (`VERTICAL_DATA`) et alimenter le devis.
- **Risque d'erreur** : lecture erronée d'une plaque signalétique ou d'une caractéristique technique — impact direct sur un devis ou une donnée réglementaire.
- **Validation humaine nécessaire** : oui, systématique dès que la donnée extraite nourrit un document commercial ou réglementaire.
- **Provenance à conserver** : oui.
- **Décision automatique autorisable** : non.
- **Version cible** : `V2` — dépend d'un pack métier déjà stable en V1.

## 3. Détection d'anomalie visuelle (photo terrain)

- **Job utilisateur** : repérer un état visible anormal (conduit, tableau électrique, isolation) sans expertise systématique sur place.
- **Entrées** : photo terrain, contexte pack métier.
- **Transformation** : détection d'anomalie (vision).
- **Sortie structurée** : signalement avec niveau de confiance, jamais une conclusion ferme.
- **Action possible** : suggestion d'attention au technicien, jamais une certification ou une attestation.
- **Risque d'erreur** : le plus élevé de toute cette carte — un faux négatif sur une anomalie de sécurité (fuite de fluide frigorigène, défaut électrique) a une conséquence physique, pas seulement commerciale.
- **Validation humaine nécessaire** : oui, absolue — **ne jamais présenter comme une certification ou un contrôle réglementaire** (cf. `09` §C, interdiction de prétendre à une conformité non réelle).
- **Provenance à conserver** : oui.
- **Décision automatique autorisable** : **non, sous aucune circonstance**.
- **Version cible** : `EXPERIMENTAL` — à ne pas construire avant que le reste du produit soit stable, et jamais sans cadrage juridique/assurantiel explicite.

## 4. Transcription vocale libre (notes de chantier)

- **Job utilisateur** : garder une trace rapide sans taper, sans structuration immédiate exigée.
- **Entrées** : voix.
- **Contexte disponible** : lieu/chantier courant.
- **Transformation** : transcription pure, aucune extraction.
- **Sortie structurée** : texte libre horodaté, rattaché au chantier.
- **Action possible** : note consultable, pas d'action déclenchée.
- **Risque d'erreur** : faible (pas d'action automatique en aval).
- **Validation humaine nécessaire** : relecture normale, pas un contrôle spécifique.
- **Provenance à conserver** : non nécessaire à ce stade (pas de donnée de validation/sécurité en jeu).
- **Décision automatique autorisable** : sans objet (pas une décision).
- **Version cible** : `V1` — la brique la plus simple, sert de fondation technique à l'opportunité 1.

## 5. Résumé de fiche client / historique avant intervention

- **Job utilisateur** : se préparer rapidement avant un rendez-vous SAV.
- **Entrées** : historique client, interventions passées, notes.
- **Transformation** : résumé.
- **Sortie structurée** : texte, non structuré en champs.
- **Action possible** : lecture seule.
- **Risque d'erreur** : faible — aucune action déclenchée.
- **Validation humaine nécessaire** : faible (lecture, pas une décision).
- **Provenance à conserver** : non.
- **Décision automatique autorisable** : sans objet.
- **Version cible** : `V2`/`V3` — précédent marché existant (Sellsy IA, `MARKETING_ONLY`), mais **faible différenciation** : capacité `CORE_EXTENSIBLE` générique de CRM, pas liée au terrain ni à une verticale.

## 6. Relance de maintenance périodique (parc installé)

- **Job utilisateur** : ne pas manquer une obligation d'entretien réglementaire ou contractuelle (ramonage, entretien PAC).
- **Entrées** : parc installé (`VERTICAL_DATA`), règle de fréquence du pack (`VERTICAL_RULE`/`VERTICAL_REGULATORY`).
- **Transformation** : automatisation par règle (pas de génération IA nécessaire au cœur du mécanisme) ; génération de message personnalisé optionnelle (IA légère).
- **Sortie structurée** : rappel planifié.
- **Action possible** : la **notification** peut être déclenchée automatiquement (pas engageante) ; la **planification définitive du rendez-vous** reste une action utilisateur.
- **Risque d'erreur** : faible sur la notification, moyen si la fréquence réglementaire est mal paramétrée par pack — erreur de configuration, pas d'IA.
- **Validation humaine nécessaire** : non pour la notification, oui pour la planification.
- **Provenance à conserver** : non (pas une donnée interprétée, une règle explicite).
- **Décision automatique autorisable** : oui pour la notification uniquement.
- **Version cible** : `V2`/`V3`, dépend du pack métier et de la présence du parc installé (`03`, preuve à un seul témoin — OpenFire Odoo).

## 7. Génération de contenu commercial (email de relance, description produit)

- **Job utilisateur** : gagner du temps sur des tâches rédactionnelles répétitives.
- **Transformation** : génération.
- **Risque d'erreur** : faible à modéré (image de marque, pas de conséquence métier directe).
- **Validation humaine nécessaire** : recommandée, non critique.
- **Décision automatique autorisable** : non recommandé par défaut (image de marque).
- **Version cible** : `V3`/Parking Lot — précédent marché existant (Sellsy IA), **différenciation faible**, capacité `CORE_EXTENSIBLE` générique.

## 8. Ce que ce document écarte explicitement du cœur de la thèse IA

- **Assistant conversationnel générique** ("posez une question à vos données") : aucune preuve corpus ne le rattache à un job utilisateur terrain précis, et la mission demande explicitement de ne pas supposer qu'un LLM doit être utilisé partout. Candidat `Parking Lot`, pas une brique V1/V2.
- **Certification ou conformité automatique par IA** (Factur-X, signature qualifiée, attestation réglementaire) : à ne jamais construire comme automatique — voir la règle transversale `09` §C. Une detection IA peut *alerter*, jamais *attester*.

## 9. Pourquoi VOIX + VERTICAL + CATALOGUE + RELEVÉ dépasse l'assistant conversationnel

Les deux précédents fonctionnels les plus solides du corpus (InterFast, OpenFire
Zendesk — `03`/`04`) ne sont **pas** des assistants conversationnels : ce sont des
**pipelines de structuration** qui partent d'une capture terrain typée et
produisent directement des lignes de devis exploitables, dans le contexte d'un
métier précis (catalogue + règles). C'est ce schéma — capture typée par pack →
extraction → lignes structurées → validation humaine — qui est repris pour
l'opportunité 1, plutôt que le modèle "chat génératif" que revendiquent Sellsy ou
un assistant générique. C'est un choix de conception argumenté par le corpus, pas
une préférence esthétique.

## 10. Synthèse par version

| Version | Opportunités |
|---|---|
| V1 | Transcription vocale libre (#4) ; premier pilote de devis vocal simple sur le pack métier retenu (#1, brique transcription + rattachement catalogue) |
| V2 | Relevé technique guidé + OCR (#2) ; structuration complète du devis vocal (#1, partie extraction avancée) ; relance de maintenance (#6, si pack avec parc installé) |
| V3 / Parking Lot | Résumé fiche client (#5) ; génération de contenu commercial (#7) ; assistant conversationnel générique (écarté §8) |
| EXPERIMENTAL, cadrage préalable obligatoire | Détection d'anomalie visuelle (#3) — jamais sans cadrage juridique/assurantiel |
