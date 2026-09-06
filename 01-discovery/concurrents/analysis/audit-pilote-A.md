# Audit du Pilote A — trace méthodologique

Ce document est la trace canonique des erreurs du schéma V1.
Les 30 YAML produits sous V1 seront recodés en place en session 2 ;
leur état V1 reste consultable dans l'historique git.
**Ce document est ce qui survit de V1, pas les fichiers.**

Périmètre : 30 articles (Vertuoza 10, InterFast 10, Sellsy 10),
sélectionnés par thème métier — devis, chantier/intervention,
facturation, mobile/terrain, correction d'erreur, paramétrage.

---

## 1. Schéma V1 utilisé

```
source:       vendor, fichier, rubrique_originale, titre
metier:       moments[], roles_bruts[], roles_canoniques[],
              actions[], objets[], job_to_be_done
coordination: niveau (0-5), justification, niveau_infere,
              de, vers, objet
resultat:     objet_produit, prochaine_etape
complexite:   preconditions[], nb_etapes, etats[], exceptions[],
              systemes_externes[]
contexte:     dispositif, temporalite, recovery, sortie_du_logiciel[]
preuve:       statut, citation, champs_inferes[], ambiguite, note
```

Échelle de coordination V1 :
0 aucun second rôle · 1 rôles séparés · 2 même objet ou visibilité
commune · 3 transmission explicite · 4 la transmission déclenche une
action chez le destinataire · 5 orchestration de bout en bout.

**Défaut de conception principal, identifié a posteriori :** le schéma
demandait à l'extraction de produire un *score* (`niveau`) au lieu de
produire des *faits*. Un score est un jugement ; il ne peut être ni
vérifié ni recalculé sans relire l'article. Toutes les erreurs
ci-dessous en découlent.

**Trois défauts secondaires :**

- `coordination` était un objet unique : un article documentant deux
  relais différents en perdait un.
- `roles_canoniques` mélangeait acteurs et destinataires dans une seule
  liste, rendant tout agrégat ininterprétable.
- La preuve était portée par l'article (`preuve.citation`, unique), pas
  par chaque fait.

---

## 2. Les six erreurs de niveau

### E1 — Vertuoza / devis.md — 4 → 3

Citation qui a trompé : « le devis a été accepté par le client et
transformé en chantier ».

Pourquoi le raisonnement était faux : cette phrase décrit un *résultat*
dans une section narrative. La section opératoire du même article
énumère les commandes disponibles : « gérer le devis via les boutons
d'action : Envoyer, Refuser, Accepter ». L'acceptation est donc saisie
**par l'entreprise**, pas exécutée par le client dans le produit. J'ai
lu une phrase de récit comme la description d'un mécanisme.

> **Règle R1** — Une phrase décrivant un résultat n'est pas une preuve
> de mécanisme. Avant de créditer une action au destinataire, il faut
> identifier qui déclenche l'action dans l'interface.

### E2 — InterFast / creer-un-avenant-au-devis.md — 4 → 3

Citation qui a trompé : « Accepté : Le client valide les modifications. »

Pourquoi le raisonnement était faux : c'est un **libellé de cycle de
vie**, une définition d'état. L'article ne documente nulle part par quel
geste le client valide. J'ai déduit une action à partir du nom d'un
statut.

> **Règle R2** — Un libellé de statut n'est pas une action documentée.
> Un état nommé « Accepté » ne prouve pas que quelqu'un l'a accepté dans
> le logiciel.

### E3 — InterFast / creer-un-chantier-app-web.md — 5 → 4

Citation qui a trompé : « Il reçoit une notification push sur son mobile
pour chaque étape ».

Pourquoi le raisonnement était faux : « pour chaque étape » est une
formule promotionnelle sans description d'étapes. Le contenu réel de
l'article est une **affectation** automatique et un réglage de
**permissions** — ni l'une ni l'autre n'étant de la transmission. Il
subsiste un flux authentique (le temps déclaré par le terrain alimente
automatiquement le déboursé sec), qui justifie 4 mais pas 5.

> **Règle R3** — Une affectation n'est pas un handoff : personne ne
> décide de transmettre, personne n'accuse réception. Une permission
> n'est pas de la coordination : elle décrit une frontière d'accès. Une
> formule totalisante non détaillée ne prouve pas une orchestration.

### E4 — InterFast / remplir-modifier-un-rapport-d-intervention-app-web.md — 3 → 2

Citation qui a trompé : « aux techniciens ou aux services administratifs
de remplir ou de compléter ».

Pourquoi le raisonnement était faux : c'est l'énumération de deux
**publics possibles** du même écran, pas un relais entre eux. Rien n'est
envoyé, le rédacteur initial n'est pas prévenu quand un autre reprend
son rapport. J'ai lu une continuité là où il n'y a qu'un accès partagé.

> **Règle R4** — « A ou B peuvent faire X » n'est pas « A transmet à B ».
> Deux rôles éditant successivement le même objet relèvent de l'édition
> partagée, pas de la transmission.

### E5 — InterFast / resoudre-un-ajout-d-utilisateur-par-erreur.md — 3 → 1

Citation qui a trompé : « Contactez le support (…) pour valider la
conversion du montant en crédit ».

Pourquoi le raisonnement était faux : le destinataire est le **support
de l'éditeur**, pas un rôle de l'entreprise cliente. J'ai compté un
ticket de support comme un handoff métier, gonflant une mesure censée
porter sur la coordination organisationnelle.

> **Règle R5** — Le périmètre du destinataire (interne, client,
> partenaire, éditeur) doit être qualifié **avant** toute
> caractérisation de la relation, jamais après.

### E6 — Sellsy / gerer-les-profils-de-privileges-de-mes-collaborateurs.md — 3 → 2

Citation qui a trompé : « vous rapprocher de votre administrateur afin
qu'il vous donne les droits nécessaires ».

Pourquoi le raisonnement était faux : c'est une **instruction hors
produit**. Aucune demande de droits n'est outillée dans Sellsy. La
dépendance hiérarchique est réelle, la transmission logicielle est
nulle. J'ai codé au même rang un mécanisme produit et une consigne
d'organisation.

> **Règle R6** — Distinguer systématiquement une transmission outillée
> par le logiciel d'une transmission qui suppose de sortir du logiciel.
> Cette distinction est portée par un champ dédié dans V2
> (`dans_logiciel`) ; elle n'existait pas en V1.

---

## 3. Erreurs de remplissage, distinctes des erreurs de niveau

- **Sellsy / plan de relance** — le champ `de` contient « référent
  interne, propriétaire du document ou collaborateur interne ». Ce sont
  des **emplacements de configuration** (des options d'un menu
  déroulant), pas des personnes qui transmettent. Un rôle configurable a
  été codé comme un acteur.
- **Sellsy / créer un document de vente** — « commercial » a été porté
  en `roles_bruts` alors qu'il n'apparaît que dans un exemple
  parenthétique (« par exemple : vous, en tant que commercial »).
- **InterFast / facture d'acompte** — le champ `etats` agrège sept
  valeurs appartenant à deux objets différents (devis et facture). V1 ne
  rattachait pas les états à un objet.

---

## 4. Les deux chiffres, nommés distinctement

> **Articles recodés sur le pilote : 6 / 30 = 20 %**
> Part des articles du Pilote A dont le niveau de coordination change
> après audit.

> **Erreur de l'instrument sur ses positifs : 6 / 18 = 33 %**
> Part des articles que V1 avait classés à un niveau ≥ 3 et qui étaient
> mal classés.

Ces deux nombres ne sont pas interchangeables. Le premier mesure
l'ampleur du recodage à effectuer. Le second mesure la fiabilité de
l'instrument **là où il prétend détecter quelque chose** — c'est le seul
des deux qui qualifie l'outil. Un instrument qui se trompe sur un tiers
de ses détections ne peut pas être industrialisé.

Distribution avant / après recodage :

| Niveau | V1 | Après audit |
|---:|---:|---:|
| 0 | 4 | 4 |
| 1 | 4 | 5 |
| 2 | 4 | 6 |
| 3 | 6 | 5 |
| 4 | 9 | 8 |
| 5 | 3 | 2 |
| **≥ 3** | **18 (60 %)** | **15 (50 %)** |

---

## 5. Asymétrie acteur / destinataire

| | Explicitement nommé | Inféré | Indéterminable |
|---|---:|---:|---:|
| **Acteur** (lecture stricte : rôle métier) | 6 / 30 — **20 %** | 3 — 10 % | 21 — 70 % |
| **Acteur** (lecture permissive : + rôles génériques et de permission) | 10 / 30 — **33 %** | 3 — 10 % | 17 — 57 % |
| **Destinataire** | 23 / 30 — **77 %** | 0 — 0 % | 7 — 23 % |

**Explication proposée, non démontrée : convention éditoriale du genre
documentaire.** Un centre d'aide s'écrit à la deuxième personne. Le
lecteur *est* l'acteur ; le nommer serait redondant. Le destinataire,
lui, doit être nommé pour que la phrase soit compréhensible
(« transmise à votre Employeur »).

Si cette explication est juste, l'asymétrie mesurée serait une propriété
du genre documentaire plutôt qu'une caractéristique des logiciels
étudiés. Cette explication n'a pas été testée : elle demanderait de
vérifier que la même asymétrie apparaît dans des centres d'aide de
domaines sans rapport. En l'état, l'asymétrie est un fait mesuré dont la
cause reste ouverte.

Conséquence pour V2 : acteur et destinataire sont séparés, et chacun
porte son propre bloc de preuve avec un niveau
`explicite | contextuel | infere | inconnu`. Une liste unique de rôles
est inexploitable.

---

## 6. Observation brute à conserver

> Les 6 acteurs strictement nommés du pilote appartiennent tous à des
> articles terrain.

Articles concernés : Vertuoza *suivi de chantier chef d'équipe*,
Vertuoza *rapport d'intervention*, Vertuoza *pointage*, InterFast
*rapport d'intervention app web*, InterFast *PV de réception*,
InterFast *feuilles de temps*.

Séparément, et sans confusion avec ce qui précède :

> Ce pattern est **compatible** avec l'hypothèse que les rôles terrain
> constituent une exception au lecteur implicite du centre d'aide.
> Ce n'est pas un fait produit et devra être vérifié sur le corpus
> étendu.

Formulation interdite : « les éditeurs conçoivent leurs produits pour le
patron ». Le corpus ne permet pas de l'établir. Il permet seulement
d'observer que le rôle devient explicite quand le lecteur cesse d'être
le destinataire par défaut de la documentation.

---

## 7. Statut du chiffre de coordination organisationnelle

Une seconde lecture excluant les interactions avec le client et les
acteurs externes donne, sur les 30 articles :

| Niveau organisationnel | Articles |
|---:|---:|
| 0 | 11 |
| 1 | 9 |
| 2 | 3 |
| 3 | 2 |
| 4 | 3 |
| 5 | 2 |
| **≥ 3** | **7 / 30 — 23 %** |

**Ce 23 % est un diagnostic de calibration, jamais un résultat de
marché.**

Trois raisons, à rappeler chaque fois que ce nombre est cité :

1. L'échantillon a été construit **par thème métier** — devis, chantier,
   facturation, mobile, correction, paramétrage — et non pour mesurer la
   coordination. Il sous-échantillonne par construction les articles de
   coordination.
2. Le nombre mesure ce que la documentation **fait apparaître
   spontanément**, jamais ce que les produits savent faire.
3. Sur les 7 articles concernés, 2 reposent sur de simples *options de
   configuration* chez Sellsy. Le noyau se réduit à 5 observations —
   base beaucoup trop mince pour une conclusion concurrentielle.

Usage autorisé de ce chiffre : montrer l'écart entre 60 % (mesure V1) et
23 % (après qualification du périmètre), c'est-à-dire l'ampleur de la
dérive que V1 produisait.

Usage interdit : « les concurrents ne coordonnent que 23 % du temps ».
