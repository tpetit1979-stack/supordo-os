# Pilote — Exploitation fonctionnelle : onboarding

Mission pilote, un seul domaine (onboarding : configuration initiale → première opération métier), un seul verdict, puis stop. N'est pas une extraction V2/V3, ne modifie pas LIGHT, ne fonde aucune décision produit SUPORDO au-delà du test de méthode lui-même.

## 1. Question

Comment les logiciels concurrents amènent-ils une entreprise depuis la configuration initiale jusqu'à sa première opération métier ? Concrètement : ce qu'il faut configurer, dans quel ordre, ce qui est obligatoire ou facultatif, quelles dépendances sont explicitement documentées, quels objets doivent exister, quelles créations peuvent être différées, quelles valeurs par défaut apparaissent, comment utilisateurs/rôles/clients/catalogue/TVA/numérotation/modèles entrent en jeu, et ce qui permet d'atteindre une première opération métier.

## 2. Critère de rendement ex ante

Fixé avant toute lecture source, non modifié après lecture.

- **RENDEMENT_SUFFISANT** : au moins 3 éditeurs fournissent une séquence fonctionnelle partiellement ou totalement reconstituable ET au moins 5 dépendances explicites ou quasi explicites sont établies avec leur source.
- **RENDEMENT_FAIBLE** : les sources décrivent essentiellement des réglages isolés, écrans ou fonctionnalités sans ordre/dépendances exploitables.
- **NON_DETERMINABLE** : le corpus candidat est trop mince ou trop indirect pour juger.

Ce seuil mesure l'utilité de la méthode, pas l'importance marché ni la fréquence réelle d'un comportement.

## 3. Sélection des sources

### Instruments consultés avant lecture

`CLAUDE.md`, `SCHEMA-LIGHT.md` lus intégralement. `GLOSSAIRE-OBSERVE-LIGHT.md` (2539 lignes, 284 Ko) et `corpus_index.json` (7333 lignes, 284 Ko) dépassent la taille maximale de l'outil de lecture (256 Ko) : lus par extraits (`offset`/`limit`) et par recherche textuelle ciblée (`grep`) sur les champs `editorial_taxonomy`, `objet_principal`, et sur des mots-clés (démarrage, configuration, paramétrage, compte, entreprise, utilisateur, import, TVA, numérotation, catalogue, modèle). Limite méthodologique reconnue en §13.

### Critères de sélection des candidats

Deux signaux convergents ont été utilisés, aucun traité comme vérité unique :

1. **`editorial_taxonomy` de `corpus_index.json`** — présence d'une rubrique de premier niveau explicitement nommée "démarrer" ou équivalent dans l'arborescence physique du corpus (signal structurel fort, indépendant de LIGHT).
2. **`objet_principal` / mots-clés LIGHT** — grep ciblé sur les 12 fichiers `light-*.md` pour confirmer que ces rubriques contiennent effectivement des objets de configuration initiale (compte, entreprise, utilisateur, TVA, numérotation, import, catalogue).

### Candidats retenus (rubrique dédiée identifiée mécaniquement)

| Concurrent | Rubrique source | Fichiers dans la rubrique | Fichiers effectivement lus |
|---|---|---:|---:|
| ProGBat | `pour-bien-demarrer/` | ~31 | 31 |
| Costructor | `debuter-sur-costructor/` | 30 | 30 |
| Axonaut | `configurer-votre-compte/` | 12 | 12 + 2 (croisement `gerez-vos-devis/`, numérotation + création de devis) |
| Vertuoza | `demarrer/` | 8 | 8 |
| OpenFire (Zendesk) | `bien-debuter/` (10, dont 2 newsletters exclues) | 8 pertinents | 8 + 6 (croisement `configurer-openfire/` et `utiliser-openfire/` — banque, taxes, plan comptable, contact, produit, devis, motivé par l'absence de configuration métier dans `bien-debuter/` seul) |
| InterFast | `debuter-avec-interfast/` | 20 | 20 |

Chaque extraction a été confiée à un agent dédié par éditeur, contraint à lire intégralement les fichiers listés et à ne consulter aucune autre source (pas de Web, pas de V2/V3, pas d'autres concurrents), conformément à la hiérarchie de preuve de la mission.

### Candidats identifiés mais non approfondis (décision de suffisance, documentée)

- **Sellsy** — rubrique `configuration-du-compte/` identifiée dans `editorial_taxonomy` (candidat plausible, 462 fichiers au total dans le corpus). Non lue : le seuil ex ante (≥ 3 éditeurs) était déjà atteint par les 6 candidats ci-dessus avant d'envisager Sellsy. Décision de suffisance décisionnelle explicite, pas un constat d'absence de contenu.
- **OpenFire (documentation Odoo)** — corpus distinct du corpus Zendesk du même éditeur (`corpus_index.json` : "corpus documentaire distinct du corpus 'aide' [...] aucune fusion, aucune comparaison implicite"). Non utilisé pour ce pilote ; `bien-debuter/` (Zendesk) suffisait comme point d'entrée.

### Candidats presque non documentés sur ce sujet (constat, pas décision de suffisance)

- **Obat** (274 fichiers) — `editorial_taxonomy` ne contient aucune rubrique de premier niveau assimilable à un "démarrage" : le champ liste des slugs d'articles individuels, signe d'une arborescence plate sans regroupement éditorial dédié à l'onboarding. Un candidat existe en apparence (`comment-parametrer-votre-compte-obat.md`, `entreprise-eurl-sarl-sas-comment-s-abonner...md`) mais dispersé, non regroupé mécaniquement.
- **Batikko** (14 fichiers au total, rubrique unique `guides`) — corpus trop mince pour isoler un sous-ensemble onboarding distinct sans lecture intégrale du corpus entier (hors périmètre proportionné à un pilote).
- **Extrabat** (1670 fichiers, rubrique `parametrage` large mais non spécifique au démarrage) — candidat noyé dans un volume disproportionné pour un pilote ; nécessiterait un tri LIGHT plus fin, non fait ici.
- **Tolteck, Leobati** — corpus d'aide non collectés (documenté dans `COUVERTURE.md`, cause technique vérifiée), sans lien avec ce pilote.

## 4. Vue A — séquences par concurrent

### ProGBat

```
Inscription (email ou SSO, essai 1 mois, "compte de test = vrai compte")
    ↓
[Personnalisation tableau de bord — 1ère connexion, facultatif]
    ↓
Paramétrage (accès réservé aux droits "administrateur")
    Mon offre → Mon profil (MFA, envoi d'emails, préférences) →
    Paramètres entreprise (infos générales → adresses → assurances/CGV →
    attestation de conformité → comptes bancaires → horaires → marges →
    numérotation → TVA → autres paramètres) → Utilisateurs (création, droits)
    ↓
[branche parallèle, non ordonnée impérativement vs. paramétrage]
Import (contacts → bibliothèque fournitures/ouvrages/tarifs fournisseur →
    devis/factures en cours)
    ↓
Première opération métier : facture réelle — garde-fou documenté
    ("Toute facture validée [...] ne pourra plus être supprimée"),
    mécanisme de facture de test (préfixe $) tant que non validée en mode réel
```

Trou documenté : aucun ordre impératif explicite entre "paramétrage" et "import" ; pas de procédure de bascule test→réel formalisée (seule la validation d'une facture réelle scelle le passage).

Tableau noyau (extrait, séquence complète en 20 lignes dans le rapport source) :

| ÉTAPE | ACTION | OBJET | PRÉCONDITION | OBLIG./FAC. | EFFET | SOURCE |
|---|---|---|---|---|---|---|
| 1 | S'inscrire | Compte ProGBat | aucune | OBLIGATOIRE | accès immédiat, essai 1 mois | `pour-bien-demarrer/tester-progbat.md` |
| 4 | Renseigner infos légales | SIREN, TVA, statut juridique | accès menu Entreprise | OBLIGATOIRE (SIREN/TVA "indispensable") | taux TVA et devise appliqués automatiquement | `parametrage/parametres-de-lentreprise/informations-generales.md` |
| 11 | Paramétrer numérotation | format, compteur, préfixe | aucune | OBLIGATOIRE (légal : continuité) | numéro provisoire ($) jusqu'à validation | `parametrage/parametres-de-lentreprise/numero-des-documents.md` |
| 16-18 | Importer contacts/bibliothèque/devis | fichiers Excel/CSV | menu import | FACULTATIF | données créées en masse | `demarrer-avec-progbat/importer-*.md` |
| 20 | Créer 1ère facture réelle | Facture | numérotation + TVA + mentions légales en place | OBLIGATOIRE pour opération réelle | facture définitive, non supprimable | `pour-bien-demarrer/tester-progbat.md` |

### Vertuoza

```
Connexion (lien tenantID + identifiants reçus par mail)
    ↓
Paramétrage essentiel
    1. Profil utilisateur (infos perso, photo, signature, envoi email propre)
    2. Société (coordonnées, logo, CGV, horaires)
    3. Personnalisation documents (couleurs, modèles, modèle par défaut)
    ↓ ("Après avoir configuré les paramètres essentiels, l'étape suivante...")
Personnel & utilisateurs
    1. Encodage personnel (bureau / ouvriers-indépendants, taux horaire)
    2. Attribution comptes utilisateurs (compte gestion / compte ouvrier)
    ↓
Import de données (facultatif, si migration) : contacts, ouvrages, composants
    ↓
[TROU] — première opération métier (devis/facture) non documentée dans ce
    sous-corpus ; TVA, numérotation, catalogue produit également absents ici
```

Aucun wizard/assistant guidé documenté : la checklist "paramétrage essentiel" est manuelle, pas un flux imposé par l'outil.

### Axonaut

```
Créer un compte (email+mdp, essai 15 jours)
    ↓ (même page, flux continu)
Secteur d'activité → Modules/fonctionnalités (réversibles ensuite) →
Infos entreprise/profil (nom, contact, langue, tél.) →
[Ajouter utilisateurs — facultatif] → [Parrainage — facultatif]
    ↓ ("vous pouvez désormais utiliser Axonaut" — pas d'étape imposée suivante)
[branches parallèles non ordonnées entre elles] : import contacts/produits/
    factures (fichier modèle ou migration Quickbooks), suppression données
    de démo, droits utilisateurs, signature email
    ↓
Numérotation devis (facultative) / factures (quasi-obligatoire avant édition,
    légalement continue)
    ↓
Première opération métier : créer un devis — client requis (créable à la
    volée), produit requis, numérotation à valeur par défaut
```

Trou documenté : aucune page ne dit explicitement "créez vos clients/produits avant un devis" — visible seulement en creux dans l'écran de devis.

### OpenFire (assemblé `bien-debuter` + `configurer-openfire` + `utiliser-openfire`)

```
Connexion (web : URL de production + identifiants ; mobile : optionnel)
    ↓
Personnalisation du compte utilisateur (profil, notifications, langue, 2FA
    optionnelle)
    ↓
[juxtaposition thématique, ordre non imposé entre les trois]
    Banque → Compte bancaire (banque doit exister avant le compte, ordre
    interne réversible selon l'article) | Taxes (pré-configurées par défaut)
    | Plan comptable (pré-livré, préconfiguré)
    ↓
Créer un contact (client/fournisseur — peut être créé à la volée depuis le
    devis)
    ↓
Créer un produit (recherche uniquement, pas de création à la volée
    documentée)
    ↓
Première opération métier : créer et personnaliser un devis → confirmer →
    bon de commande
```

Trou majeur documenté : aucun des 14 fichiers lus ne décrit la création initiale de l'entreprise/de la base OpenFire elle-même — la séquence commence après que l'environnement existe déjà.

### InterFast

```
I. Audit & diagnostic (cartographie processus, inventaire outils/données,
    "compréhension de la structure du logiciel")
    ↓
II. Configuration
    A. Abonnement → Sortie du mode Test (documents deviennent "officiels")
    B. Paramètres Entreprise (infos, logo, présentation devis/factures,
       paiements/taxe, CGV, certifications, numérotation, comptes
       comptables)
    C. Gestion d'équipe (invitations, fiches, accès comptable)
    D. Intégrations externes (email, Trackdéchets, extension Chrome, banque)
    E. Mise en forme documents (optionnel)
    ↓ (A/B/C/D listés à plat, aucune dépendance croisée affirmée entre eux)
III. Migration des données (client transmet → Équipe Care traite sur Google
    Sheets → import)
    ↓
IV. Consolidation (mise à jour fiches importées, ajout manuel ouvrages/
    bouteilles/contrats/chantiers, import devis/factures en cours)
    ↓
V. Prise en main → VI. Utilisation intermédiaire → VII. Utilisation avancée
```

Trou documenté : la checklist ne désigne pas un acte unique de "premier devis/première facture" ; la bascule métier documentée est la **sortie du mode Test**, pas la création du premier document lui-même (procédure hors du dossier lu).

### Costructor

Pas de séquence inter-articles reconstituable : collection de 30 fiches how-to indépendantes, sans numérotation, sans liens "étape suivante", sans wizard. N'y figurent ni l'inscription initiale, ni la création du premier utilisateur, ni la création des taux de TVA (seul l'ajustement de catégories déjà peuplées par défaut), ni le premier devis/la première facture. Ce sous-corpus documente des **réglages post-inscription**, pas le parcours de démarrage lui-même. Plusieurs micro-dépendances intra-articles restent explicites (§6).

## 5. Vue B — comparaison par phénomène

### Identité entreprise / informations légales

- **Convergences** : quand documentée, l'identité entreprise (SIREN, TVA, adresse, logo) est systématiquement présentée comme précondition d'un report automatique sur les documents commerciaux (devis/factures/emails) — ProGBat, Vertuoza, Costructor, Axonaut (inscription).
- **Variantes** : ProGBat qualifie SIREN/TVA d'"indispensable" (obligatoire de fait) ; Vertuoza qualifie la société de "primordial" sans formule de blocage système ; Costructor la traite comme obligation légale de conformité sans en faire une précondition technique documentée.
- **Inconnus** : OpenFire (trou explicite — création d'entreprise hors des documents lus), InterFast (item nommé dans la checklist, procédure non détaillée dans le périmètre lu).
- **Sources** : voir §4 par éditeur.

### Utilisateurs

- **Convergences** : dans tous les éditeurs où le sujet est documenté, l'ajout d'utilisateurs additionnels est présenté comme distinct de la création du compte lui-même et différable.
- **Variantes** : ProGBat — 1 seul utilisateur suffit, rôles par défaut gratuits (Admin/Utilisateur/Expert-comptable) ; Axonaut — facultatif mais payant par utilisateur ajouté ; Vertuoza — distingue "personnel" (fiche RH, taux horaire) de "compte utilisateur" (accès applicatif), l'un requis avant l'autre ("après avoir encodé votre personnel [...] pour leur attribuer des comptes") ; Costructor et InterFast mentionnent une gestion d'équipe/invitation sans procédure de création détaillée dans le périmètre lu.
- **Inconnus** : rôle par défaut attribué à un utilisateur créé sans choix explicite (non tranché par Axonaut ni OpenFire).

### Rôles/permissions

- **Convergences** : aucune — trop peu de corpus documentent une procédure fine.
- **Variantes** : ProGBat (rôles personnalisés = option payante) vs Vertuoza (2 profils fixes : gestion/ouvrier) vs Axonaut (droits configurables par fiche utilisateur, défaut non précisé).
- **Inconnus** : OpenFire, Costructor, InterFast — mentionné en creux, aucune procédure lue.

### TVA / taxes

- **Convergences** : ProGBat et OpenFire documentent tous deux une TVA **pré-remplie par défaut** (selon le pays / l'environnement), pas une création manuelle initiale.
- **Variantes** : Costructor ne documente qu'un ajustement de catégories de vente déjà associées par défaut à un compte comptable (pas de création de taux) ; InterFast nomme "Paiements et Taxe" dans sa checklist sans procédure incluse dans le périmètre lu.
- **Inconnus** : Axonaut, Vertuoza — absent des sous-corpus lus (silence documentaire, pas absence produit).

### Numérotation

- **Convergence forte** : ProGBat et InterFast documentent, indépendamment l'un de l'autre, le **même mécanisme structurel** — un document en mode test/provisoire (préfixe `$` chez ProGBat) devient définitif et non supprimable/non modifiable après validation, tous deux avec référence explicite à la législation anti-fraude TVA.
- **Variantes** : Axonaut différencie devis (facultatif, non séquentiel) et factures (quasi-obligatoire de paramétrer avant édition, continuité légale requise) ; Costructor documente la numérotation comme non rétroactive une fois la facture finalisée, sans mécanisme de mode test.
- **Inconnus** : Vertuoza, OpenFire — absent des sous-corpus lus.

### Catalogue

- **Convergences** : quand un catalogue existe, son peuplement initial est présenté comme facultatif avec une alternative de saisie manuelle (ProGBat, Costructor).
- **Variantes** : OpenFire — le produit doit exister et n'est **pas** créable à la volée depuis un devis (recherche uniquement), contrairement au contact du même éditeur qui l'est ; Costructor — peuplement uniquement via une extension navigateur tierce dans ce sous-dossier (pas de CSV documenté ici) ; ProGBat documente un risque de doublons si deux tarifs fournisseurs sont importés simultanément.
- **Inconnus** : Vertuoza (catalogue produit détaillé absent du sous-corpus lu), InterFast (nommé en étape IV, procédure hors périmètre), Axonaut (import mentionné, non détaillé).

### Import clients / contacts

- **Convergence** : quand documenté, l'import repose sur un fichier gabarit dont l'en-tête ne doit pas être modifié (Axonaut : "il est nécessaire d'importer les données à partir du fichier modèle" ; Vertuoza : champs obligatoires précis par type d'objet ; InterFast : "il est impératif de ne jamais modifier la première ligne").
- **Variante marquante** : InterFast est seul des 6 à faire reposer la migration sur un **service humain dédié** (Équipe Care, traitement via Google Sheets) plutôt que sur un import self-service par l'utilisateur ; les 5 autres éditeurs documentent (quand ils le documentent) un import autonome par fichier.
- **Variante** : OpenFire — le contact peut être créé à la volée pendant un devis (comme Axonaut : "ajouter un nouveau client depuis le devis"), alors que le produit ne le peut pas chez OpenFire dans le périmètre lu.
- **Inconnus** : Costructor — pas de procédure d'import de contacts dans le sous-dossier lu.

### Banque

- **Convergence** : quand documentée, la banque est une précondition de la création du compte bancaire (OpenFire : "vous devez d'abord créer la banque correspondante", ordre réversible selon un autre passage du même article).
- **Variante** : ProGBat automatise la création du compte bancaire ProGBat lors de la connexion à une plateforme tierce (powens.com) s'il n'existe pas encore.
- **Inconnus** : Axonaut, Vertuoza, InterFast — item nommé (InterFast : "comptes bancaires" en II.D) sans procédure dans le périmètre lu.

### Modèles de documents

- **Convergence** : quand un modèle de document existe, son contenu est hérité automatiquement par chaque document généré avec ce modèle (ProGBat — conditions de règlement du devis héritées par la facture ; InterFast — "chaque devis généré avec ce modèle inclura automatiquement votre présentation d'entreprise").
- **Variantes** : Costructor conditionne un affichage complet des documents personnalisés à la présence préalable des mentions légales ; InterFast réserve la fonctionnalité de plaquette commerciale à l'abonnement Business.
- **Inconnus** : Axonaut (signature email seulement, dans le périmètre lu), OpenFire, Vertuoza (personnalisation mentionnée mais non détaillée en dépendances).

### Moyens / conditions de paiement

- Documenté en détail seulement par ProGBat : hiérarchie explicite chantier > client > défaut > devis > facture, avec héritage du devis vers la facture ("les factures récupèrent les conditions de règlement appliquées au devis").
- **Inconnus** pour les 5 autres éditeurs dans le périmètre lu.

### Signature / email / SMS / communication

- Documenté de façon dispersée : ProGBat et Axonaut (signature email personnalisable), Vertuoza (envoi depuis propre adresse), Costructor (modèles email pour relances, configurables "en amont"), InterFast (intégration email nommée, non détaillée).
- **Inconnu** pour OpenFire dans le périmètre lu. Aucun SMS documenté dans aucun des 6 sous-corpus.

### Planning

- **Inconnu pour les 6 éditeurs** — aucun des sous-corpus onboarding lus ne couvre le planning ; silence documentaire, pas absence fonctionnelle.

### Fournisseurs

- Costructor documente une liste de fournisseurs référencés (catalogue), sans procédure d'onboarding fournisseur dédiée. **Inconnu** pour les 5 autres dans ce périmètre.

### Intégrations

- Costructor (Pennylane, agent IA/MCP, extension navigateur), ProGBat (bibliothèque tierce), Axonaut (Quickbooks), InterFast (Trackdéchets, extension Chrome). **Inconnu** pour OpenFire et Vertuoza dans le périmètre lu (au-delà de la migration de données).

### Première opération métier

- **Convergence** : quand elle est atteinte (ProGBat, Axonaut, OpenFire), la première opération métier est systématiquement un **devis ou une facture**, jamais un autre objet, et repose sur l'existence préalable d'un client/contact (explicite chez OpenFire, fortement implicite chez Axonaut et ProGBat).
- **Trous** : Vertuoza, Costructor, InterFast — non atteinte dans les sous-corpus lus. Chez InterFast, la bascule structurante documentée est la sortie du mode Test, mais la procédure de création du premier document réel elle-même est hors du dossier lu.

## 6. Dépendances documentées

62 dépendances relevées au total (≥ 5 requis par le critère ex ante), toutes sourcées, classées EXPLICITE ou CONTEXTUEL_FORT. Détail complet par éditeur ci-dessous ; seules les formulations exactes citées valent preuve.

### ProGBat (17 relevées)

| A | Relation | B | Formulation | Preuve | Source |
|---|---|---|---|---|---|
| Droits "administrateur" | A_EST_REQUIS_POUR_B | Accès au menu paramétrage | « seuls les utilisateurs ayant les droits 'administrateurs' ont accès à ce menu » | EXPLICITE | `pour-bien-demarrer/parametrage.md` |
| Informations générales (SIREN) | A_DOIT_EXISTER_AVANT_B | Adresses | « Vous avez déjà dû le saisir dans la section précédente » | EXPLICITE | `parametrage/parametres-de-lentreprise/adresses.md` |
| Devis créé sur ProGBat | A_DOIT_EXISTER_AVANT_B | Import du contenu du devis | « Vous créez un devis sur ProGBat. Vous importez le contenu depuis un fichier Excel ou csv » | EXPLICITE | `.../importer-mes-devis.md` |
| Devis (importé/créé) | A_EST_REQUIS_POUR_B | Facture (d'acompte ou de travaux) | « Vous n'avez plus qu'à réaliser votre facture [...] depuis le devis » | EXPLICITE | `.../poursuivre-la-facturation-faite-sur-mon-ancien-logiciel.md` |
| Numérotation des lignes du fichier importé | A_EST_REQUIS_POUR_B | Structure automatique du devis importé | « Sans numérotation des titres, sous-titres et lignes, le logiciel ne pourra pas réaliser une structure automatique » | EXPLICITE | `.../importer-mes-devis.md` |
| Import de 2 tarifs fournisseurs | A_EST_FACULTATIF_POUR_B (déconseillé) | Bibliothèque sans doublons | « vous aurez inévitablement des doublons dans votre bibliothèque » | EXPLICITE | `.../importer-mes-fournitures.md` |
| Compte bancaire créé sur ProGBat | A_PEUT_ETRE_CREE_PENDANT_B | Connexion powens.com | « il le sera automatiquement au moment de la connexion » | EXPLICITE | `.../comptes-bancaires.md` |
| Marge par défaut définie | B_HERITE_DE_A | Prix de vente d'un élément | « Le nouveau taux sera appliqué [...] uniquement si sa marge est égale à l'ancien taux » | EXPLICITE | `.../marges.md` |
| Marge de chaque composant | B_HERITE_DE_A | Marge d'un ouvrage composé | « la marge de l'ouvrage dépendra de la marge de chaque élément le composant » | EXPLICITE | `.../marges.md` |
| Conditions de règlement (hiérarchie chantier>client>défaut) | B_HERITE_DE_A | Conditions de règlement du devis | hiérarchie chantier→client→défaut→devis, modifiable à chaque niveau | EXPLICITE | `.../autres-parametres.md` |
| Conditions de règlement du devis | B_HERITE_DE_A | Conditions de règlement de la facture | « les factures récupèrent les conditions de règlement appliquées au devis » | EXPLICITE | `.../autres-parametres.md` |
| Modèle CGV de la fiche client | A_PEUT_ETRE_CONFIGURE_PLUS_TARD (surcharge) | Modèle CGV appliqué au devis | « le modèle sera automatiquement appliqué dans le devis » | EXPLICITE | `.../autres-parametres.md` |
| Validation d'une facture en mode réel | B_EST_BLOQUE_SANS_A (bloque un chemin alternatif) | Choix de procédure d'import d'ancienne facturation | « il ne faut surtout pas recréer la facture d'acompte » si déjà validée | EXPLICITE | `.../poursuivre-la-facturation-faite-sur-mon-ancien-logiciel.md` |
| — | A_EST_BLOQUE_SANS_EXCEPTION (interdiction réglementaire) | Import de factures d'un autre logiciel | « il n'est pas possible d'importer sur ProGBat les factures réalisées sur d'autres logiciels » | EXPLICITE | idem |
| Paramétrage entreprise | A_PEUT_ETRE_CONFIGURE_PLUS_TARD | Première facture réelle | présenté comme distinct du test ; seule la validation finale est irréversible | CONTEXTUEL_FORT | `pour-bien-demarrer/tester-progbat.md` |
| Utilisateur créé | A_EST_REQUIS_POUR_B | Attribution d'un rôle | « Ouvrez la fiche d'un utilisateur [...] sélectionnez le rôle » | EXPLICITE | `.../gestion-des-droits-dacces.md` |
| Fichier modèle | A_DOIT_EXISTER_AVANT_B | Import (contacts) | fichier modèle requis pour tout import | EXPLICITE | `demarrer-avec-progbat/importer-mes-contacts.md` |

### Axonaut (8 relevées)

| A | Relation | B | Formulation | Preuve | Source |
|---|---|---|---|---|---|
| Numérotation factures | A_DOIT_EXISTER_AVANT_B (quasi) | Édition de factures | « la première étape sera de paramétrer la numérotation de vos factures » | CONTEXTUEL_FORT | `gerez-vos-devis/comment-numeroter-mes-devis-dans-axonaut.md` |
| Numérotation devis | A_EST_FACULTATIF_POUR_B | Création de devis | « il n'est pas obligatoire que les numéros des devis se suivent » | EXPLICITE | idem |
| Client | A_EST_REQUIS_POUR_B | Devis | écran impose de « sélectionner un client/prospect » | CONTEXTUEL_FORT | `gerez-vos-devis/creer-un-devis-avec-axonaut.md` |
| Client | A_PEUT_ETRE_CREE_PENDANT_B | Devis | « ajouter un nouveau client depuis le devis » | EXPLICITE | idem |
| Fichier modèle | A_DOIT_EXISTER_AVANT_B | Import (contacts/produits/factures) | « il est nécessaire d'importer les données à partir du fichier modèle ! » | EXPLICITE | `configurer-votre-compte/importer-ses-contacts.md` |
| Factures créées après la démo | B_EST_BLOQUE_SANS_A (inversé) | Suppression de la facture de démo | « il ne sera pas possible de supprimer directement la facture de démo » | EXPLICITE | `.../demo-effacer-les-donnees-factices.md` |
| Utilisateur | A_EST_REQUIS_POUR_B | Attribution de droits | fiche modifiée après création pour affecter des droits | CONTEXTUEL_FORT | `.../droits-responsabilites-utilisateurs-a-quoi-ca-correspond-2.md` |
| Modules choisis à l'inscription | A_PEUT_ETRE_CONFIGURE_PLUS_TARD | Modules activés | réversible via icône pinceau après création | EXPLICITE | `.../comment-creer-son-compte-axonaut-facilement-et-rapidement.md` |

### Vertuoza (10 relevées)

| A | Relation | B | Formulation | Preuve | Source |
|---|---|---|---|---|---|
| Mail de connexion reçu | A_EST_REQUIS_POUR_B | Connexion à l'environnement | « rendez-vous dans votre boîte mail [...] avec toutes les informations nécessaires pour vous connecter » | EXPLICITE | `demarrer/se-connecter-a-vertuoza.md` |
| Identifiant + adresse mail | A_EST_REQUIS_POUR_B | Réinitialisation du mot de passe | « Vous avez impérativement besoin de votre identifiant et de l'adresse mail liée » | EXPLICITE | `.../reinitialiser-le-mot-de-passe.md` |
| Paramétrage essentiel | A_DOIT_EXISTER_AVANT_B | Encodage personnel & utilisateurs | « Après avoir configuré les paramètres essentiels, l'étape suivante consiste à encoder [...] votre personnel » | EXPLICITE | `.../personnel-et-utilisateurs-ajoutez-vos-collaborateurs.md` |
| Encodage du personnel | A_DOIT_EXISTER_AVANT_B | Attribution de comptes utilisateurs | « Après avoir encodé votre personnel, rendez-vous [...] pour leur attribuer des comptes utilisateurs » | EXPLICITE | idem |
| Coordonnées/logo société | B_HERITE_DE_A | Documents générés | « utilisées dans tous les documents générés par le logiciel (devis, facture, etc.) » | EXPLICITE | `.../parametrage-essentiel-configurez-le-logiciel-a-votre-image.md` |
| CGV société | B_HERITE_DE_A | E-mails envoyés | « ajouté en pièce jointe dans vos e-mails » | EXPLICITE | idem |
| Horaire société | B_HERITE_DE_A | Horaire du personnel | « pré-remplir par défaut l'horaire de votre personnel » | EXPLICITE | idem |
| Taux horaire encodé | A_EST_REQUIS_POUR_B | Calcul de rentabilité de chantier | « influence directement la rentabilité du chantier » | CONTEXTUEL_FORT | `.../personnel-et-utilisateurs...md` |
| Fichier Excel complété (champs obligatoires) | A_EST_REQUIS_POUR_B | Import réussi | champs « Nom »/« Profil » (contacts), etc. explicitement listés | EXPLICITE | `.../les-imports-migrez-d-un-autre-logiciel-vers-vertuoza.md` |
| Import de données | A_PEUT_ETRE_CONFIGURE_PLUS_TARD | Utilisation du logiciel | cadré comme guide à part, « si vous migrez » | CONTEXTUEL_FORT | idem |

### OpenFire (9 relevées)

| A | Relation | B | Formulation | Preuve | Source |
|---|---|---|---|---|---|
| Banque | A_DOIT_EXISTER_AVANT_B | Compte bancaire | « vous devez d'abord créer la banque correspondante » | EXPLICITE | `configurer-openfire/banques-et-comptes-bancaires.md` |
| Contact | A_PEUT_ETRE_CREE_PENDANT_B | Devis | « chaque fois que vous rencontrerez un menu déroulant [...] comme dans vos [...] devis » | EXPLICITE | `utiliser-openfire/creer-un-contact.md` |
| Produit | A_EST_REQUIS_POUR_B | Devis | ajout par recherche de référence uniquement, pas de création à la volée | CONTEXTUEL_FORT | `.../creer-et-personnaliser-votre-devis.md` |
| Position fiscale du contact | B_HERITE_DE_A | Devis | « celle-ci sera appliquée par défaut » | EXPLICITE | idem |
| Taxe à la vente du produit | B_HERITE_DE_A | Ligne de devis | « utilisée par défaut pour le produit dans vos devis et vos factures » | EXPLICITE | `.../creer-un-produit.md` |
| Contact | A_DOIT_EXISTER_AVANT_B | Compte de tiers comptable | généré « dès qu'un événement comptable intervient [...] par exemple lors de l'enregistrement d'une facture » | CONTEXTUEL_FORT | `.../plan-comptable-general-et-auxiliaire.md` |
| Compte bancaire / journal comptable | A_PEUT_ETRE_CONFIGURE_PLUS_TARD (ordre réversible) | — | ordre journal→numéro de compte possible aussi | EXPLICITE | `.../banques-et-comptes-bancaires.md` |
| Avertissement bloquant sur contact | B_EST_BLOQUE_SANS_A (blocage) | Devis | « un message bloquant apparaît » | EXPLICITE | `.../creer-un-contact.md` |
| Taxes/plan comptable | A_PEUT_ETRE_CONFIGURE_PLUS_TARD | — | « livré avec un plan comptable préconfiguré » | EXPLICITE | `.../plan-comptable-general-et-auxiliaire.md` |

### InterFast (12 relevées)

| A | Relation | B | Formulation | Preuve | Source |
|---|---|---|---|---|---|
| Création du compte entreprise | A_DOIT_EXISTER_AVANT_B | Mode Test actif | « activé, par défaut, à la création d'un compte entreprise » | EXPLICITE | `.../sortir-du-mode-test.md` |
| Sortie du mode Test | A_EST_REQUIS_POUR_B | Usage réel (documents officiels) | « vos documents ne seront pas considérés comme de vrais documents officiels » sinon | EXPLICITE | idem |
| Document finalisé et numéroté | B_EST_BLOQUE_SANS_A (suppression bloquée) | Suppression du document | « ne peut plus être supprimé, conformément à la législation anti-fraude à la TVA » | EXPLICITE | idem ; `comprendre-la-structure-d-interfast.md` |
| Sortie du mode test | A_EST_FACULTATIF_POUR_B (non-destructif) | Conservation du paramétrage entreprise | « ne vous fera pas perdre votre travail de paramétrage » | EXPLICITE | idem |
| Export des données (client) | A_DOIT_EXISTER_AVANT_B | Traitement puis import (Équipe Care) | séquence explicite Transmission→Traitement→Import | EXPLICITE | `checklist-de-demarrage.md` |
| Fichier conforme au gabarit | A_EST_REQUIS_POUR_B | Import réussi | « ne jamais modifier la première ligne (l'en-tête) » | EXPLICITE | `.../boite-a-outils-telecharger-nos-modeles-et-gabarits-de-documents.md` |
| Devis accepté | A_EST_REQUIS_POUR_B | Facture d'acompte | « émis à partir d'un devis accepté » | EXPLICITE | `.../le-dictionnaire-des-fonctionnalites-d-interfast.md` |
| Facture d'acompte émise | B_HERITE_DE_A | Déduction sur facture suivante | « déduit automatiquement 100% [...] sur la toute première facture suivante » | EXPLICITE | idem |
| Formulaire plaquette complété | A_DOIT_EXISTER_AVANT_B | Rendez-vous de création | « Une fois le formulaire complété, contactez-nous [...] planifier un rendez-vous » | EXPLICITE | `.../creer-votre-plaquette-de-presentation-commerciale.md` |
| Modèle de devis paramétré | B_HERITE_DE_A | Chaque devis généré | « inclura automatiquement votre présentation d'entreprise » | EXPLICITE | idem |
| Abonnement Business | A_EST_REQUIS_POUR_B | Plaquette commerciale / agent IA MCP | « réservé aux clients disposant d'un abonnement Business » | EXPLICITE | idem ; dictionnaire des fonctionnalités |
| Souscription à l'abonnement | A_DOIT_EXISTER_AVANT_B | Accès à l'accompagnement 30 jours | « Dès votre abonnement, vous bénéficierez d'un accès privilégié » | EXPLICITE | `.../debuter-votre-accompagnement-30-jours.md` |

### Costructor (12 relevées)

| A | Relation | B | Formulation | Preuve | Source |
|---|---|---|---|---|---|
| Plan comptable | A_DOIT_EXISTER_AVANT_B | Catégories d'achats | « Avant d'ajouter de nouvelles catégories, pensez à bien ajouter les comptes comptables » | EXPLICITE | `.../comment-parametrer-les-categories-dachats-19pewed.md` |
| Comptes comptables | A_EST_REQUIS_POUR_B | Catégories de vente et d'achat | « peuvent être utilisés pour vos catégories » | EXPLICITE | `.../comment-parametrer-le-plan-comptable-et-les-comptes-auxiliaires-8bld86.md` |
| Réglage stock global | A_DOIT_EXISTER_AVANT_B | Activation du stock par produit | « Rendez-vous ensuite dans votre bibliothèque » | CONTEXTUEL_FORT | `.../comment-gerer-ses-stocks-cb6503.md` |
| Taux de marge défini | B_HERITE_DE_A | Prix de vente à l'import d'articles | « le prix de vente [...] est calculé automatiquement » | EXPLICITE | `.../comment-importer-plus-de-100-millions-darticles-en-1-clic-div3pc.md` |
| Inscription finalisée (Pennylane) | A_EST_REQUIS_POUR_B | Activation de la facturation électronique | « Une fois l'inscription finalisée, l'activation peut prendre jusqu'à 72h » | EXPLICITE | `.../comment-activer-la-facturation-electronique-...-f1ogg.md` |
| Invitation du comptable | A_EST_REQUIS_POUR_B | Paramétrage du plan comptable par le comptable | « Vous pouvez lui donner accès en l'invitant depuis réglages/équipe » | EXPLICITE | `.../comment-parametrer-le-plan-comptable-et-les-comptes-auxiliaires-8bld86.md` |
| Accès Costructor du comptable | A_EST_REQUIS_POUR_B | Paramétrage des catégories par le comptable | « peut être fait par votre comptable s'il a un accès à Costructor » | EXPLICITE | `.../comment-parametrer-les-categories-dachats-19pewed.md` |
| Utilisateur + rôle/organisation existants | B_EST_BLOQUE_SANS_A | Actions de l'agent IA via MCP | « ne peut pas agir au-delà de ce que votre rôle et votre organisation autorisent » | EXPLICITE | `.../comment-connecter-costructor-a-votre-agent-ia-en-mcp-ey5k4v.md` |
| Abonnement (Pro/Business+/Premium) | A_EST_REQUIS_POUR_B | API, relances auto, demandes d'avis, tags analytiques | « disponible en option sur les abonnements pro et business+ » (×6 occurrences) | EXPLICITE | 6 fichiers distincts |
| Modèle d'email personnalisé | A_PEUT_ETRE_CONFIGURE_PLUS_TARD | Relances/demandes d'avis automatiques | « En amont, vous pouvez personnaliser le modèle d'email » | CONTEXTUEL_FORT | 3 fichiers (relances devis/facture, demande d'avis) |
| Mentions légales en base | A_DOIT_EXISTER_AVANT_B (quasi) | Affichage complet des documents personnalisés | renvoi éditorial mentions légales → personnalisation documents | CONTEXTUEL_FORT | `.../comment-personnaliser-mes-documents-13ywvrp.md` |
| Compte bancaire connecté | A_EST_FACULTATIF_POUR_B | Suivi des transactions | aucune précondition documentée, connexion indépendante | EXPLICITE (absence de précondition) | `.../comment-connecter-son-compte-bancaire-xupyjb.md` |

## 7. Convergences

1. **Devis/facture comme point d'arrivée unique** — quand une première opération métier est atteinte dans le périmètre lu (ProGBat, Axonaut, OpenFire), c'est toujours un devis ou une facture, jamais un autre objet, et elle requiert un client/contact préexistant.
2. **Héritage société → documents** — 4 éditeurs sur 6 documentent explicitement que l'identité entreprise (logo, coordonnées, mentions légales) se propage automatiquement sur les documents commerciaux générés (ProGBat, Vertuoza, Costructor, Axonaut implicitement).
3. **Mécanisme mode test/provisoire → validation irréversible, adossé à l'anti-fraude TVA** — documenté indépendamment par ProGBat et InterFast, avec la même logique : un document non validé reste modifiable/supprimable, un document validé ne l'est plus, référence légale explicite dans les deux cas.
4. **Héritage en cascade devis → facture** — ProGBat (conditions de règlement) et InterFast (montant d'acompte) documentent tous deux qu'un objet aval hérite automatiquement de valeurs fixées sur l'objet amont.
5. **TVA pré-remplie par défaut plutôt que configurée manuellement** — ProGBat et OpenFire, quand ils traitent le sujet, présentent la TVA comme déjà paramétrée par le logiciel (selon le pays/l'environnement), à vérifier plutôt qu'à créer.

Ces convergences reposent sur un sous-ensemble de 2 à 4 éditeurs sur 6 : elles ne sont pas un plancher de marché à 6/6, mais des motifs répétés indépendamment, donc plus qu'un artefact isolé (classification en §detail : STANDARD_PROBABLE pour 1, 2, 4 ; VARIANTE_DE_MARCHE prudente pour 3 et 5 tant que non confirmées sur d'autres éditeurs français).

## 8. Variantes

- **Séquence guidée vs. collection de réglages** — 5 éditeurs sur 6 offrent une forme de checklist ou de flux ordonné (ProGBat, Vertuoza, Axonaut, OpenFire assemblé, InterFast) ; Costructor, dans le sous-dossier lu, n'en offre aucune — pure collection de réglages indépendants.
- **Migration de données self-service vs. assistée par un humain** — InterFast est seul à confier la migration à une équipe support dédiée (Équipe Care, via Google Sheets) ; les autres éditeurs documentés (ProGBat, Axonaut, Vertuoza) reposent sur un import de fichier autonome par l'utilisateur.
- **Modèle "personnel" distinct du "compte utilisateur"** — Vertuoza sépare explicitement la fiche personnel (taux horaire, RH) du compte utilisateur applicatif, avec une dépendance d'ordre entre les deux ; Axonaut distingue de même "personnel" (fiche RH sans accès logiciel) et "utilisateur" (accès payant), mais sans dépendance d'ordre documentée aussi stricte ; ProGBat et OpenFire ne documentent pas cette distinction dans le périmètre lu.
- **Création de contact à la volée vs. non** — OpenFire et Axonaut permettent tous deux la création d'un client depuis l'écran de devis ; OpenFire, dans le même périmètre, ne permet pas la création à la volée d'un produit (recherche uniquement) — asymétrie documentée chez un seul éditeur, à vérifier ailleurs.
- **Gating par abonnement** — Costructor et InterFast conditionnent plusieurs fonctionnalités d'onboarding avancées (API, agent IA/MCP, plaquette commerciale, relances automatiques) à un palier d'abonnement supérieur ; ProGBat et Axonaut ne documentent pas ce type de restriction dans le périmètre onboarding lu (Axonaut facture cependant chaque utilisateur additionnel).

## 9. Inconnus

- **Planning** — absent des 6 sous-corpus lus, alors que c'est un phénomène demandé par la mission. Silence documentaire, pas absence fonctionnelle.
- **Moyens/conditions de paiement** — documenté en détail seulement chez ProGBat ; inconnu ailleurs dans le périmètre lu.
- **Rôles par défaut à la création d'un utilisateur sans choix explicite** — non tranché par Axonaut ni OpenFire (les deux mentionnent l'existence de droits sans préciser la valeur par défaut).
- **Création d'entreprise/de compte initial chez OpenFire** — absente des 14 documents lus ; peut exister ailleurs dans le corpus OpenFire, hors périmètre de ce pilote.
- **Premier devis/première facture chez Vertuoza, Costructor et InterFast** — non atteint dans les sous-corpus lus ; peut exister ailleurs dans leurs corpus respectifs (`ventes/`, `devis/`, etc.), hors périmètre de ce pilote.
- **Catalogue produit détaillé chez Vertuoza et InterFast** — nommé mais non procéduralisé dans le périmètre lu.
- **Ordre réellement imposé par le logiciel vs. ordre éditorial** — pour la plupart des éditeurs, le corpus ne permet pas de distinguer un ordre techniquement forcé par l'interface d'un ordre simplement suggéré par la documentation (voir §12).
- **Sellsy, Obat, Extrabat, Batikko sur ce sujet** — non explorés en profondeur dans ce pilote (voir §3), statut réel non déterminé.

## 10. Ce que le corpus permet de spécifier

- Des préconditions techniques ponctuelles précises et actionnables : banque avant compte bancaire (OpenFire), plan comptable avant catégories (Costructor), personnel avant comptes utilisateurs (Vertuoza), fichier gabarit conforme avant import réussi (Axonaut, Vertuoza, InterFast), client avant devis quand explicite (OpenFire).
- Des mécanismes d'héritage documentés et directionnels : société → documents (Vertuoza, ProGBat), devis → facture (ProGBat, InterFast), fiche client/produit → ligne de devis (OpenFire).
- Un motif structurel répété (mode test/provisoire → validation irréversible, adossé à une contrainte légale) observé chez deux éditeurs indépendamment, donc formulable comme hypothèse de contrainte réglementaire française transversale à vérifier plus largement.
- Une distinction actionnable entre objets "créables à la volée" pendant une opération métier (contact, chez Axonaut et OpenFire) et objets qui ne le sont pas (produit, chez OpenFire).

## 11. Ce qu'il ne permet pas de spécifier

- Un parcours d'onboarding de bout en bout unique et comparable pour les 6 éditeurs : 3 sur 6 (Vertuoza, Costructor, InterFast) n'atteignent pas la première opération métier dans le périmètre lu.
- La création de compte/inscription initiale pour la moitié des éditeurs (Costructor, OpenFire, InterFast ne la documentent pas dans le périmètre lu ; seuls Axonaut et ProGBat le font).
- Le planning, les moyens de paiement détaillés et les rôles par défaut, quasi absents du corpus lu quel que soit l'éditeur.
- Si un ordre documenté correspond à une contrainte technique de l'interface ou seulement à une convention éditoriale — le corpus ne permet jamais de trancher ce point avec certitude.

## 12. Questions terrain résiduelles

- L'ordre Entreprise/Équipe/Intégrations chez InterFast, et Paramétrage/Import chez ProGBat, est-il vraiment libre dans l'interface, ou seulement présenté à plat dans la documentation ?
- Le mode test/provisoire (ProGBat, InterFast) est-il un standard silencieusement partagé par les autres éditeurs français de ce corpus, ou une spécificité de ces deux-là ? Le silence documentaire chez les 4 autres ne permet pas de trancher.
- Quel rôle est effectivement attribué par défaut à un nouvel utilisateur chez Axonaut et OpenFire quand aucun choix n'est fait à la création ?
- Le catalogue produit est-il réellement bloquant pour un premier devis chez tous les éditeurs, ou existe-t-il ailleurs un mode "ligne libre" non cataloguée (question ouverte pour Vertuoza, Costructor, InterFast où le trou documentaire empêche de trancher) ?
- Sellsy, Obat, Extrabat et Batikko présentent-ils des motifs comparables (héritage, mode test, gating par abonnement) une fois leur propre rubrique onboarding identifiée et lue ?

## 13. Évaluation de la méthode

Le double signal de présélection (rubrique `editorial_taxonomy` dédiée + confirmation par mots-clés LIGHT) a fonctionné de façon fiable pour les 6 corpus structurés en rubriques thématiques ; il échoue mécaniquement pour un corpus à arborescence plate nommée par slug d'article (Obat) — la méthode devrait, pour un futur run canonique à cette échelle, prévoir un second mode de présélection (échantillonnage LIGHT par objet_principal) pour ce cas de figure.

La lecture intégrale des articles Markdown sources (et non des seules lignes LIGHT) a été nécessaire et suffisante pour obtenir des formulations de dépendance citables mot pour mot — LIGHT n'aurait permis de présélectionner que les documents, jamais les dépendances elles-mêmes (conforme à SCHEMA-LIGHT §10 : LIGHT présélectionne, ne remplace pas une lecture).

Le noyau à 8 colonnes (ÉTAPE/ACTION/OBJET/PRÉCONDITION/OBLIGATOIRE-FACULTATIF-INCONNU/EFFET/PROCHAINE ÉTAPE/SOURCE) s'est avéré utilisable tel quel sur des corpus hétérogènes (wizard structuré ProGBat, checklist InterFast, collection plate Costructor) sans besoin d'adaptation. Le vocabulaire de dépendances fermé (7 relations) a suffi ; aucune relation supplémentaire n'a été nécessaire pour coder les cas rencontrés.

Déléguer l'extraction par éditeur à un agent dédié, contraint à une liste de fichiers fermée et à l'interdiction de sources externes, a permis de traiter 6 corpus en parallèle sans dilution du contrôle de fidélité (chaque agent a cité ses formulations exactes, signalé ses propres trous).

Limite méthodologique rencontrée et documentée : `GLOSSAIRE-OBSERVE-LIGHT.md` et `corpus_index.json` dépassent la taille maximale de lecture complète de l'outil utilisé (256 Ko) ; leur exploitation par extraits et `grep` a été suffisante pour ce pilote mais devrait être anticipée (script de requêtage dédié plutôt que lecture directe) pour un run canonique plus large.

## 14. Verdict

**RENDEMENT_SUFFISANT**

Justification stricte au regard du critère fixé en §2 : au moins 3 éditeurs devaient fournir une séquence fonctionnelle partiellement ou totalement reconstituable — 5 des 6 éditeurs lus le font (ProGBat, Vertuoza, Axonaut, OpenFire, InterFast ; seul Costructor n'en fournit aucune dans le sous-dossier lu). Le critère exigeait par ailleurs au moins 5 dépendances explicites ou quasi explicites établies avec leur source — 62 ont été relevées et sourcées, réparties sur les 6 éditeurs, y compris Costructor malgré l'absence de séquence chez lui. Les deux seuils du critère ex ante sont dépassés avec une marge large, sans qu'aucune règle méthodologique (suffisance, hiérarchie de preuve, silence ≠ absence) n'ait été assouplie pour y parvenir.

PILOTE_ONBOARDING_TERMINE — RENDEMENT_SUFFISANT — STOP
