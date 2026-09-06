# Mini-audit V2 — Pilote A recodé

30 articles recodés depuis les sources, sans réutiliser les YAML V1.
Le contrat n'a pas été modifié pendant le recodage.

Volumes produits :

| Bloc | Total | Moyenne / article |
|---|---:|---:|
| interactions | 44 | 1,5 |
| transitions_objet | 90 | 3,0 |
| regles_operationnelles | 145 | 4,8 |
| signaux_emergents | 23 | 0,8 |
| mécanismes | 59 | 1,3 par interaction |
| ruptures | 14 | sur 90 transitions |

---

## 1. Les six erreurs de V1 ont-elles disparu ?

Oui, les six. Mais il faut distinguer deux causes : deux erreurs sont
corrigées par une règle de lecture, quatre disparaissent parce que
**V2 n'a plus de score à gonfler**. C'est la suppression du champ
`niveau` qui fait le travail, pas ma vigilance.

### E1 — Vertuoza / devis.md

V1 : niveau 4, sur « le devis a été accepté par le client ».

V2 : l'interaction porte un seul mécanisme, `transmission`. **Aucune
`validation` n'est écrite** : l'article n'attribue au client aucun geste
dans le produit, et les commandes disponibles sont des boutons côté
entreprise. L'acceptation n'apparaît que comme une transition
`Envoyé → Chantier en cours`, dont la continuité est codée
`non_determinable`.

### E2 — InterFast / creer-un-avenant-au-devis.md

V1 : niveau 4, sur le libellé « Accepté : Le client valide ».

V2 : un seul mécanisme, `transmission`, appuyé sur « Vous transmettez
l'avenant au client ». Le libellé de cycle de vie ne produit plus rien :
il n'y a pas de geste du client documenté.

### E3 — InterFast / creer-un-chantier-app-web.md

V1 : niveau 5, sur une notification push « pour chaque étape ».

V2 : quatre mécanismes distincts, chacun avec sa preuve — `affectation`,
`notification`, `permission`, `visibilite`. **Aucune `transmission`.**
Le flux réel (le temps déclaré alimente le déboursé) est isolé dans une
seconde interaction portant `automatisation`. Le 5 n'avait aucun support.

### E4 — InterFast / remplir-modifier-un-rapport-d-intervention-app-web.md

V1 : niveau 3, sur « aux techniciens ou aux services administratifs ».

V2 : `edition_partagee` + `visibilite`, **canal `aucun`** — rien n'est
envoyé, et le champ canal le dit explicitement.

### E5 — InterFast / resoudre-un-ajout-d-utilisateur-par-erreur.md

V1 : niveau 3, sur un ticket adressé au support de l'éditeur.

V2 : `perimetre: editeur` et `dans_logiciel: partiel`. La relation est
toujours enregistrée mais elle est désormais **typée**, donc excluable
de tout calcul portant sur la coordination interne.

### E6 — Sellsy / gerer-les-profils-de-privileges-de-mes-collaborateurs.md

V1 : niveau 3, sur « rapprochez-vous de votre administrateur ».

V2 : `dans_logiciel: non`, `canal: aucun`, `mecanismes: []`. La
dépendance hiérarchique est conservée, le fait qu'elle ne soit pas
outillée est explicite.

---

## 2. Contrôles négatifs

| Contrôle | Attendu | Obtenu |
|---|---|---|
| IF créer chantier — affectation automatique | `affectation`, pas `transmission` | `affectation`, `notification`, `permission`, `visibilite`. Aucune `transmission`. **PASSÉ** |
| IF rapport app web — édition successive | `edition_partagee`, pas `transmission` | `edition_partagee`, `visibilite`, `canal: aucun`. **PASSÉ** |
| S profils de privilèges — demande hors logiciel | `dans_logiciel: non` | `dans_logiciel: non`, `canal: aucun`, `mecanismes: []`. **PASSÉ** |

`affectation` n'apparaît **qu'une seule fois** dans tout le corpus, sur
l'article même du contrôle négatif. C'est cohérent avec la définition
étroite retenue, mais cela signifie aussi que le contrôle ne teste
qu'un cas.

---

## 3. STATUT ≠ ACTION

### `validation` — 6 occurrences

| Article | Citation portant la preuve | Verdict |
|---|---|---|
| V signature du devis | « En cliquant sur le bouton « Signer », la signature est enregistrée » | geste explicite — **solide** |
| V pointage | « Pour valider un pointage, cliquez sur l'icone "V" bleu » | geste explicite — **solide** |
| IF feuilles de temps | « Il doit refuser votre feuille de temps (…) depuis son interface Web » | geste explicite — **solide** |
| IF devis app web | « Votre client a signé votre devis via signature électronique. » | verbe d'action au passé attribué à un rôle nommé, **sans description du geste** — à surveiller |
| S signature électronique | « Lorsque le document aura été signé par l'ensemble des signataires » | idem — à surveiller |
| S accès expert-comptable | « Une fois les informations validées par Sellsy » | idem — à surveiller |

**Aucune `validation` ne repose sur un libellé d'état nu.** Trois
reposent sur un geste décrit, trois sur un verbe d'action attribué à un
rôle nommé mais dont le mécanisme n'est pas décrit. Ces trois-là sont un
cran au-dessus de l'erreur E2 — un acteur agit, il est nommé — mais un
cran en dessous de la preuve idéale. Le critère « geste ou mécanisme
cité » n'est donc pas binaire dans les faits.

### `transmission` — 23 occurrences

Trois faux positifs légers, que je signale :

| Article | Citation | Problème |
|---|---|---|
| V devis | « le devis a été envoyé mais pas encore accepté par le client » | citation tirée de la **définition d'un statut**. Un geste existe ailleurs dans l'article (« boutons d'action : Envoyer ») ; j'ai cité le mauvais passage. |
| IF facture d'acompte | « Une fois la facture finalisée, elle pourra être envoyée » | **modal** : possibilité, pas geste observé. |
| S avoirs | « Un avoir est une facture rectificative que vous adressez à un client » | phrase **définitionnelle**, pas description d'un mécanisme. |

Les 20 autres s'appuient sur un geste ou un mécanisme décrit.

**Conclusion du contrôle :** le glissement statut → action a disparu,
mais un glissement plus fin subsiste — **définition → mécanisme**. Trois
transmissions sur 23 (13 %) reposent sur une phrase qui décrit ce qu'est
un objet plutôt que ce que quelqu'un en fait.

---

## 4. Perte d'information

23 signaux émergents ont été écrits, répartis sur 17 articles.
13 articles n'en produisent aucun.

| | Articles |
|---|---:|
| Aucune perte détectée après les quatre blocs | 13 |
| Au moins une perte, capturée par `signaux_emergents` | 17 |
| Perte non représentable même avec `signaux_emergents` | 0 |

**Pertes capturables mais qui auraient pu être oubliées.** Deux cas où
j'ai failli ne rien écrire, et où l'écriture s'est imposée à la relecture :

- **S journal des appels** — la note se dicte à la voix juste après avoir
  raccroché. La transition « note dictée → note » enregistrait le
  résultat en perdant entièrement le mode de saisie. C'est exactement la
  forme du contre-exemple pédagogique du contrat, rencontrée sans avoir
  été cherchée.
- **V pointage** — l'entrée « AUTRE » permet de pointer du temps rattaché
  à aucun objet métier (visite au contrôle technique du véhicule).
  Les transitions supposent toujours un objet source et un objet
  résultat ; une activité orpheline n'y entre pas.

**Familles de pertes observées**, sans ontologie :

1. Un objet dont le contenu change selon le rôle qui le lit (IF liste de
   matériel sans prix d'achat ; S liste des règlements filtrée par
   périmètre).
2. Un rôle porté par l'objet et non par une interaction (V « responsable »
   d'un avenant ; S « référent en charge du devis » ; IF signature du
   rédacteur).
3. Une prérogative déplacée d'un rôle vers un autre (V l'ouvrier décide
   du facturable ; IF le Technicien + encaisse chez le client).
4. Une continuité tenue par une discipline humaine plutôt que par le
   produit (IF précharger avant la zone blanche ; IF filtrer « Non
   exportée » avant clôture ; S « il faudra penser à annuler ces
   prélèvements »).
5. Une partition d'accès qui n'est pas un réglage mais une architecture
   (V compte chantier / compte gestion).
6. Un état délibérément découplé de ce qu'il nomme (IF devis « marqué
   manuellement comme facturé », sans effet comptable).

**Aucune perte n'a été jugée irreprésentable.** Ce résultat doit être lu
avec prudence : `signaux_emergents` étant un champ libre, il absorbe par
construction ce que les autres blocs manquent. Le contrôle ne peut donc
pas échouer sur ce point — sa vraie valeur est la liste ci-dessus, pas
le compteur.

---

## 5. Taux de null par champ

Pour les énumérations, `inconnu` est comptabilisé séparément de `null` :
les deux signalent une absence d'information mais ne se corrigent pas de
la même façon.

### parcours — 30 valeurs par champ

| Champ | Renseigné | inconnu | % inconnu | Recommandation |
|---|---:|---:|---:|---|
| parcours.origine | 21 | 9 | 30 % | **modifier** — `sav` et `maintenance` sont à **0 occurrence sur 30**, et le champ est scalaire alors que plusieurs articles documentent plusieurs origines. Voir cas problématique CP-1. |
| parcours.nature | 23 | 7 | 23 % | **modifier** — les 7 `inconnu` ne sont pas des indéterminations mais des activités commerciales pures, que l'énumération ne prévoit pas. Voir CP-2. |

### interactions — 44 entrées

| Champ | Renseigné | null / inconnu | % | Recommandation |
|---|---:|---:|---:|---|
| acteur.role_brut | 29 | 15 null | 34 % | **conserver** |
| acteur.preuve.niveau = explicite | 29 | 15 inconnu | 34 % | **conserver** — 0 inféré, voir §6 |
| destinataire.role_brut | 39 | 5 null | 11 % | **conserver** |
| perimetre | 43 | 1 inconnu | 2 % | **conserver** — champ le plus discriminant du bloc |
| relation | 37 | 7 inconnu | 16 % | **conserver** |
| canal | 35 | 6 inconnu + 3 « aucun » | 20 % | **modifier** — pas de valeur pour un appel téléphonique (CP-3) |
| dans_logiciel | 43 | 1 inconnu | 2 % | **conserver** — champ décisif, voir §11 |
| mecanismes (liste vide) | 38 | 6 vides | 14 % | **conserver** — les listes vides sont informatives, voir CP-4 |

### transitions_objet — 90 entrées

| Champ | Renseigné | null | % null | Recommandation |
|---|---:|---:|---:|---|
| objet_source | 90 | 0 | 0 % | conserver |
| action | 90 | 0 | 0 % | conserver |
| objet_resultat | 89 | 1 | 1 % | conserver |
| etat_entree | 47 | 43 | **48 %** | **conserver** — le null est ici un fait : la documentation décrit souvent une action sans état de départ |
| etat_sortie | 30 | 60 | **67 %** | **conserver, mais réexaminer** — sous le seuil de 90 %, mais c'est le champ le plus vide du bloc. Il reste discriminant : les articles qui le renseignent sont exactement ceux qui décrivent un cycle de vie. |
| owner_avant (déterminable) | 11 | 79 | **88 %** | voir §7 |
| owner_apres (déterminable) | 13 | 77 | **86 %** | voir §7 |
| continuite.ruptures (liste vide) | 14 | 76 vides | 84 % | conserver — la liste vide est prescrite par R5 |

### regles_operationnelles — 145 entrées

| Champ | Renseigné | null | % null | Recommandation |
|---|---:|---:|---:|---|
| description_brute | 145 | 0 | 0 % | conserver |
| objet_concerne | 145 | 0 | 0 % | conserver |
| condition | 142 | 3 | 2 % | conserver |
| consequence | 145 | 0 | 0 % | conserver |
| resolution_documentee | 61 | 84 | 58 % | **conserver** — le champ sépare nettement les contraintes subies des contraintes contournables |
| resolution.acteur | 19 | 42 | 69 % des résolutions | **conserver** — quand il est renseigné, il nomme presque toujours un rôle que rien d'autre ne fait apparaître (Employeur, support, administrateur) |

**Aucun champ n'atteint 90 % de null.** Les deux plus vides,
`owner_avant` et `owner_apres` à 86-88 %, sont traités au §7.

**Le bloc `regles_operationnelles` est le plus productif du schéma :
145 entrées, 4,8 par article, aucun article à zéro.** Il justifie
rétrospectivement le blocage identifié en session 1.

---

## 6. Niveaux de preuve par type de fait

| Fait | explicite | contextuel | inféré | inconnu |
|---|---:|---:|---:|---:|
| acteur (44) | 29 — 66 % | 0 | **0** | 15 — 34 % |
| destinataire (44) | 37 — 84 % | 2 — 5 % | **0** | 5 — 11 % |
| mécanisme (59) | 59 — 100 % | 0 | **0** | 0 |
| transition (90) | 90 — 100 % | 0 | **0** | 0 |
| rupture (14) | 14 — 100 % | 0 | **0** | 0 |
| règle (145) | 145 — 100 % | 0 | **0** | 0 |
| résolution (61) | 59 — 97 % | 2 — 3 % | **0** | 0 |
| owner (180 emplacements) | 18 — 10 % | 6 — 3 % | **0** | 156 — 87 % |
| signal (23) | 23 — 100 % | 0 | **0** | 0 |

**Le taux d'inférence est de 0 % sur l'ensemble du corpus.**

Ce résultat demande une lecture méfiante, pas de l'autosatisfaction. Il
ne signifie pas que l'extraction est plus juste : il signifie que **V2
rend l'inférence inutile**. Là où V1 exigeait un score et forçait donc à
combler les trous, V2 accepte `null` et `inconnu` partout. Le taux de
0 % mesure la structure du schéma, pas la rigueur de l'analyste.

Le seuil d'alerte fixé — acteur au-delà de 60 % d'inférence — n'est pas
atteint (0 %). En revanche l'acteur reste **non nommé dans un tiers des
interactions**, ce qui confirme l'asymétrie relevée dans
`audit-pilote-A.md` : le destinataire est nommé dans 84 % des cas,
l'acteur dans 66 %.

---

## 7. owner_avant / owner_apres

| | Déterminables | Total | % |
|---|---:|---:|---:|
| owner_avant | 11 | 90 | 12 % |
| owner_apres | 13 | 90 | 14 % |
| Les deux emplacements confondus | 24 | 180 | **13 %** |

Répartition par concurrent : Vertuoza 10 emplacements renseignés,
InterFast 12, **Sellsy 2**.

Formulation exigée :

> **L'ownership des objets n'est pas documenté dans le corpus analysé.**

Et non « les produits ne gèrent pas l'ownership ». Les 24 emplacements
renseignés le sont sur des articles où le passage de main est le sujet
même de l'article — pointage, feuilles de temps, suivi de chantier,
rapport d'intervention. Partout ailleurs, la documentation décrit une
action sans jamais dire à qui appartient l'objet avant et après.

**Recommandation : conserver, et réserver l'exploitation au Pilote B.**
Un champ renseigné 13 % du temps est inexploitable en agrégat, mais les
24 cas renseignés sont précisément les situations multi-rôles que B doit
observer. Le supprimer reviendrait à aveugler B sur sa question centrale.

---

## 8. Cardinalité

| Nombre par article | interactions | transitions_objet | regles_operationnelles | signaux_emergents |
|---:|---:|---:|---:|---:|
| 0 | 5 | 0 | 0 | 10 |
| 1 | 9 | 2 | 1 | 17 |
| 2 | 14 | 7 | 2 | 3 |
| 3 et + | 2 | 21 | 27 | 0 |

Lectures :

- **5 articles ne produisent aucune interaction** : V factures d'acomptes,
  V corriger un avenant, V modifier un devis validé, V supprimer un
  utilisateur, S supprimer un règlement. Tous décrivent un travail
  solitaire. La liste vide est un résultat, pas un échec.
- **Aucun article ne produit zéro transition ni zéro règle.** Les deux
  blocs structurés portent le corpus.
- Le maximum d'interactions est **4** (S signature électronique), obtenu
  parce que R4 impose d'éclater un même mécanisme en deux périmètres
  (client et collaborateur interne) — exactement la perte que V1 causait.
- `regles_operationnelles` va jusqu'à **12 entrées** (IF facture
  d'acompte/situation/solde) et **10** (IF Pennylane).

---

## 9. Répartition des parcours

| origine | Articles | | nature | Articles |
|---|---:|---|---|---:|
| vente | 14 | | installation | 10 |
| interne | 7 | | administratif | 10 |
| inconnu | 9 | | intervention | 3 |
| **sav** | **0** | | inconnu | 7 |
| **maintenance** | **0** | | | |

**Deux valeurs sur cinq de `origine` ne sont jamais utilisées.** Ce
n'est pas un défaut de l'énumération : le Pilote A a été échantillonné
par thème métier (devis, chantier, facturation, mobile, correction,
paramétrage) et ne contient aucun article consacré au SAV ou à la
maintenance. Le constat porte sur l'échantillon, pas sur les produits.

**Articles n'entrant dans aucune origine ni nature du cycle : 7**, tous
codés `nature: inconnu` — 5 Sellsy, 1 InterFast, 1 Vertuoza. Six d'entre
eux sont des articles commerciaux d'un ERP généraliste (devis, avoirs,
document de vente, signature, mobile, journal d'appels) : ils décrivent
une activité réelle et parfaitement déterminée, que l'énumération ne
sait simplement pas nommer. Voir CP-2.

---

## 10. Cas problématiques

Onze cas, non résolus, consignés tels quels.

**CP-1 — `parcours.origine` et `parcours.nature` sont scalaires.**
Trois articles documentent explicitement plusieurs valeurs : V signature
du devis (« en chantier ou en intervention »), IF créer un chantier
(quatre points d'entrée dont un devis accepté et une intervention), IF
créer un devis (SAV, chantier ou maintenance). J'ai codé la valeur
dominante et perdu les autres. `inconnu` aurait été pire : l'information
existe, elle est simplement plurielle.

**CP-2 — `nature` n'a pas de valeur pour une activité commerciale pure.**
Sept articles codés `inconnu` alors que leur nature est parfaitement
déterminée. Cela contredit R6, qui définit `inconnu` comme « non
déterminable dans cet article ». L'énumération est calquée sur la carte
métier BTP de la décision 0002 ; elle ne couvre pas un ERP généraliste.

**CP-3 — `canal` n'a pas de valeur pour un appel téléphonique.**
S journal des appels porte entièrement sur des appels sortants ; codé
`inconnu`, ce qui est faux — le canal est parfaitement identifié.

**CP-4 — une signature client sans effet d'état documenté n'entre dans
aucune `forme`.** Trois interactions écrites avec `mecanismes: []` :
V rapport d'intervention, IF PV de réception, IF rapport app web. Le
client accomplit un geste décrit (il signe), mais l'article ne dit pas
que ce geste change l'état de l'objet — la définition de `validation`
exige les deux. J'ai préféré la liste vide à la sur-attribution.

**CP-5 — une automatisation sans second rôle n'a pas d'emplacement.**
V pointage : « Un pointage est automatiquement généré chaque jour ».
`automatisation` est une `forme` de mécanisme, donc logée dans
`interactions`, qui suppose un acteur et un destinataire. Codé en
transition, ce qui perd le caractère automatique.

**CP-6 — `statut_observation` n'a pas de valeur pour une destruction
volontaire.** S supprimer un règlement : l'objet est effacé
intentionnellement. Ni `continue_documentee` (rien ne se poursuit), ni
`rupture_documentee` (rien n'est subi), ni vraiment `non_determinable`
(tout est documenté). Codé `non_determinable` par défaut.

**CP-7 — une non-propagation entre deux systèmes n'est aucun des trois
types de rupture.** IF Pennylane : « cette information ne redescend pas
encore automatiquement ». Codé `reconstruction_contexte` faute de mieux.
Le type naturel serait « non-propagation ».

**CP-8 — suppression puis recréation : entre `ressaisie` et
`reconstruction_contexte`.** V corriger un avenant : les états
d'avancement sont supprimés puis recréés. L'information était dans le
logiciel (donc `ressaisie`) mais n'y est plus au moment de la ressaisie
(donc `reconstruction_contexte`). Codé `reconstruction_contexte`. Le
même arbitrage se repose sur IF facture d'acompte et IF ajout
d'utilisateur.

**CP-9 — emplacements de configuration codés comme acteurs.**
S plan de relance : l'expéditeur de la relance est « à choisir entre le
référent interne, le propriétaire du document ou un collaborateur
interne ». Ce sont des options d'un menu déroulant. Je les ai codées
comme `acteur` du mécanisme de transmission, ce qui est défendable pour
le mécanisme mais reste une personne non observée. C'est une version
atténuée de l'erreur de remplissage relevée en V1.

**CP-10 — une interaction sans mécanisme est indiscernable d'une
interaction substantielle en cardinalité.** IF mode hors ligne :
« une synchronisation instantanée entre le terrain et le bureau » nomme
deux rôles sans décrire aucun mécanisme. Codée avec `mecanismes: []`,
elle compte pourtant comme 1 dans les statistiques d'interactions.

**CP-11 — une règle portant sur plusieurs objets n'a qu'un
`objet_concerne`.** Plusieurs règles InterFast lient un devis, une
facture et un acompte ; j'ai retenu l'objet principal.

**CP-12 — `objet_source` et `objet_resultat` ne sont pas normalisés.**
Ce sont des chaînes libres : « devis », « devis d'origine », « devis
initial et avenant » sont trois valeurs distinctes. Les 90 transitions
ne peuvent donc pas être jointes pour reconstruire le graphe des objets.
Conséquence directe : la question « combien d'objets un devis traverse-t-il,
chez quel rôle, avant d'être encaissé » n'est pas calculable — c'est la
question centrale de H1. Identifié par le crash-test d'utilité, non par
le mini-audit de conformité.

**CP-13 — régression `job_to_be_done`.** Ce champ existait en V1 et porte
en une phrase l'intention métier de l'article. V2 ne l'a pas repris. Un
YAML V2 lu seul ne dit donc pas à quoi sert l'article. À tester en couche
assessment — c'est-à-dire en aval de l'extraction — avant d'envisager de
rouvrir le contrat d'extraction.

---

## 11. Verdict

**V2 est prêt pour le Pilote B, sous une réserve qui ne bloque pas B.**

### Ce qui fonctionne

- Les six erreurs de V1 ont disparu, et les trois contrôles négatifs
  passent.
- Le taux d'inférence est nul sur tous les types de faits : l'extraction
  ne produit plus de jugement déguisé en observation.
- `regles_operationnelles` porte 145 faits — le blocage de session 1
  était réel, et sa résolution est le principal gain de V2.
- `perimetre` et `dans_logiciel` sont renseignés à 98 %. Ce sont eux qui
  rendent E5 et E6 impossibles à reproduire : une relation avec
  l'éditeur et une demande hors produit sont désormais visibles dans les
  données, sans qu'aucun score n'ait à les absorber.
- Les listes (R4) restituent ce que V1 écrasait : S signature
  électronique produit quatre interactions là où V1 en écrivait une.

### Ce qui doit être surveillé pendant B, sans modifier le contrat

- **Trois `validation` et trois `transmission` reposent sur des phrases
  définitionnelles ou des verbes au passé plutôt que sur un geste
  décrit** (§3). Le glissement statut → action est mort ; un glissement
  définition → mécanisme subsiste, à 13 % sur les transmissions.
- **`affectation` n'a qu'une occurrence** : le contrôle négatif ne teste
  qu'un cas. B, qui vise les workflows multi-rôles, en produira
  davantage — c'est là que la frontière affectation / transmission sera
  réellement éprouvée.
- **CP-4 concerne trois interactions et touchera B de plein fouet** : le
  cas obligatoire de B (photos de chefs d'équipe non récupérées) est
  exactement un cas de geste sans effet d'état documenté.

### Ce qui devra être tranché avant l'industrialisation, pas avant B

CP-1, CP-2 et CP-3 sont des défauts d'énumération qui produisent des
`inconnu` faux. Sur 30 articles, ils touchent 7 valeurs de `nature`,
3 valeurs de `origine` et 1 valeur de `canal`. Sur 1 494 articles, ils
produiront un volume de faux `inconnu` qui rendra ces trois champs
ininterprétables.

Ils **ne bloquent pas B** : B porte sur la coordination, et ces trois
champs n'en font pas partie. Ils devront être arbitrés — par toi — entre
le mini-audit de B et l'industrialisation.

### Réserve honnête sur ce mini-audit

Le contrôle de perte d'information ne peut pas échouer tant que
`signaux_emergents` existe : c'est un champ libre, il absorbe par
construction ce que les blocs structurés manquent. Le « 0 perte
irreprésentable » n'est donc pas une bonne nouvelle, c'est une propriété
du dispositif. Ce que ce contrôle a réellement produit, ce sont les six
familles de pertes du §4 et les onze cas problématiques du §10 — c'est
là qu'il faut chercher les modes d'échec du schéma, pas dans le compteur.
