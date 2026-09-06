# Mini-audit B — Pilote B recodé

10 articles extraits selon le contrat V2, strictement inchangé.

> **Le Pilote B est biaisé par construction.** Il a été sélectionné pour
> maximiser la coordination. Aucun taux calculé ici ne caractérise le
> marché, et aucune comparaison A / B ne mesure une évolution des
> produits : elle mesure l'effet d'un échantillonnage différent.
> Silence documentaire ≠ absence produit.

## Volumes

| Bloc | Pilote A (30 art.) | Pilote B (10 art.) | Par article A | Par article B |
|---|---:|---:|---:|---:|
| interactions | 44 | 25 | 1,5 | 2,5 |
| mécanismes | 59 | 46 | 2,0 | 4,6 |
| transitions_objet | 90 | 33 | 3,0 | 3,3 |
| regles_operationnelles | 145 | 53 | 4,8 | 5,3 |
| signaux_emergents | 23 | 15 | 0,8 | 1,5 |
| ruptures | 14 | 7 | 0,5 | 0,7 |

---

## Substitution de cible — motif consigné

`inter-fast/operations/planifier-une-intervention-a-partir-d-un-devis.md`
n'existe pas dans le corpus collecté. Remplacé par
`inter-fast/operations/guide-complet-gerer-un-chantier-dans-interfast.md`.

> Motif : préserver l'intention expérimentale initiale du cas — tester une
> continuité traversant devis / chantier / planning / intervention — sans
> sélectionner un remplaçant en fonction d'un résultat déjà observé.

---

## Le cas adversarial obligatoire n'était pas le phénomène attendu

Le cas obligatoire de B avait été retenu sur son titre : « Pourquoi je ne
peux pas récupérer certaines photos ajoutées par mes chefs d'équipe dans
les suivis gestionnaires ? ». Le titre annonçait un handoff cassé entre
chef d'équipe et gestionnaire.

**La source documente autre chose** : une péremption paramétrée. « Si vous
avez, par exemple, défini une période de 20 jours, seules les photos
prises dans ce délai seront disponibles. Si les photos datent de plus de
20 jours, elles ne seront plus sélectionnables. » Aucun rôle n'échoue à
transmettre ; c'est un réglage de durée qui rend l'information
indisponible.

**Conséquence méthodologique :** une sélection par titre ne garantit pas
le phénomène visé. Le titre d'un article de FAQ décrit le symptôme perçu
par l'utilisateur, pas le mécanisme documenté par l'éditeur. Pour les
1 464 articles restants, un échantillonnage ciblé sur un phénomène devra
soit accepter ce taux d'erreur, soit prévoir une vérification de contenu
avant fixation de l'échantillon — ce qui rouvrirait le risque de
sélectionner sur le résultat.

Le cas n'est pas perdu : il a produit CP-14, et une rupture documentée
d'un type que le modèle ne prévoit pas.

---

## 1. Les deux contrôles négatifs passent-ils ?

**Oui, les trois.**

### `responsable-d-intervention` — affectation ≠ handoff

Mécanismes produits : **`affectation`** (« sélectionnez parmi votre liste
d'ouvriers votre responsable d'interventions ») et **`permission`**
(« vous avez la possibilité de personnaliser les autorisations pour chaque
responsable »).

**Aucune `transmission`, aucune `notification`.** L'article décrit la
constitution d'un profil et l'attribution de droits ; rien n'est envoyé,
personne n'accuse réception. Le contrôle est passé.

### `visibilite-des-prix-par-l-ouvrier` — visibilité ≠ coordination

Mécanisme unique : **`permission`** (« paramétrer la visibilité des prix
de votre ouvrier »). Zéro transition d'objet — **le seul article des 40
qui n'en produit aucune.** L'article ne décrit ni un échange, ni une
transformation : un réglage, et rien d'autre. Le schéma le restitue
comme tel.

### `partager-des-donnees-entre-collaborateurs` — visibilité ≠ orchestration

Mécanismes produits : **`visibilite`** (« les collaborateurs et les
groupes qui peuvent voir et modifier l'élément »), **`affectation`**
(« attribuer facilement le propriétaire de l'objet concerné ») et
**`permission`** (« les réglages de partage interviennent après les
réglages individuels »).

**Aucune `transmission`, aucune `automatisation`.** Un objet partagé
devient visible ; personne ne le remet à personne. Le contrôle est passé.

---

## 2. CP-4 — le cas photos confirme-t-il le problème du geste sans effet d'état ?

**Le cas photos laisse CP-4 non testé** : aucune signature, aucun geste
d'un destinataire n'y figure. Le cas obligatoire ne pouvait donc pas
trancher la question qu'on lui prêtait.

**Mais B produit deux nouvelles occurrences de CP-4**, dans d'autres
articles :

- InterFast, profil sous-traitant : « Il remplit son rapport, ajoute des
  photos et fait signer le client sur son téléphone. » Interaction
  sous-traitant → client codée `mecanismes: []`.
- InterFast, guide complet : « Présentez le récapitulatif au Client et
  demandez-lui de signer le rapport sur votre téléphone. » Interaction
  technicien → client codée `mecanismes: []`.

**Cumul A + B : cinq occurrences** — Vertuoza rapport d'intervention,
InterFast PV de réception, InterFast rapport app web, InterFast
sous-traitant, InterFast guide complet.

Le client accomplit chaque fois un geste décrit — il signe — mais aucun
article ne documente que ce geste change l'état de l'objet. La définition
de `validation` exigeant les deux, la liste de mécanismes reste vide.

**CP-4 n'est pas une anomalie isolée : c'est un défaut structurel.** Il
concerne le geste le plus fréquent de la relation client dans un métier
de terrain. Non résolu ici.

---

## 3. Quels CP du Pilote A réapparaissent dans B ?

C'est la question qui distingue un défaut structurel d'une anomalie.

| CP | Réapparaît ? | Occurrences en B | Verdict |
|---|---|---|---|
| **CP-4** geste sans effet d'état | **oui** | 2 (sous-traitant, guide complet) | **structurel** — 5 au total |
| **CP-7** non-propagation entre deux objets ou systèmes | **oui** | 3 (fil → onglet Documents ; devis/factures → fil ; intervention démarrée → statut chantier) | **structurel** — devenu le motif de rupture dominant |
| **CP-5** automatisation sans second rôle | oui | 1 (décrémentation automatique du stock à l'acceptation du devis, codée en transition) | récurrent |
| **CP-10** interaction sans mécanisme indiscernable en cardinalité | oui | 2 (les deux interactions à `mecanismes: []`) | récurrent |
| **CP-11** règle portant sur plusieurs objets | oui | plusieurs, dans le guide complet (devis + facture + chantier) | récurrent |
| **CP-9** emplacement de configuration codé comme rôle | partiellement | 1 (`responsable de la réclamation`, champ d'un formulaire) | récurrent atténué |
| **CP-1** parcours scalaire | faiblement | guide complet touche installation et maintenance future, codé installation | mineur en B |
| CP-2 `nature` sans valeur commerciale | non | 0 — les articles B sont administratifs ou installation | non testé |
| CP-3 `canal` sans valeur téléphone | non | 0 — et `fil_activite`, valeur jamais utilisée en A, sert ici 2 fois | non testé |
| CP-6 destruction volontaire | non | 0 | non testé |
| CP-8 suppression puis recréation | non | 0 | non testé |

**Sept CP sur onze réapparaissent.** Les deux plus lourds — CP-4 et
CP-7 — sont désormais adossés à cinq et six occurrences respectivement,
sur deux échantillons construits selon des logiques opposées. Ce ne sont
pas des anomalies d'échantillon.

---

## 4. Nouveaux cas problématiques

**CP-14 — le temps n'existe pas dans le modèle de rupture.**
Vertuoza documente une disponibilité bornée dans la durée : « Si les
photos datent de plus de 20 jours, elles ne seront plus sélectionnables »,
avec un réglage configurable et un risque nommé par l'éditeur lui-même
(« pour éviter toute perte de données »). Aucun des trois types de
rupture ne décrit **une information qui expire** : `ressaisie` suppose
une re-saisie, `sortie_logiciel` un déplacement vers un autre outil,
`reconstruction_contexte` une donnée non reprise lors d'un passage.
Ici l'information a bien été reprise — puis elle cesse d'être disponible,
sans qu'aucun passage n'ait lieu.
**Le codage retenu, `reconstruction_contexte`, est un pis-aller.** Il ne
doit pas être lu comme une qualification propre du phénomène. Le YAML
concerné porte cette réserve dans son signal émergent ; elle est répétée
ici pour que le champ ne trompe pas un lecteur pressé.

**CP-15 — un canal unique dont l'audience bascule message par message.**
InterFast, fil du chantier : « vous pouvez choisir s'il s'agit d'un
échange interne à l'équipe ou d'un message visible par le client », via
une icône cadenas ou planète. `perimetre` étant une valeur unique par
interaction, j'ai créé deux interactions sur le même canal, ce qui
duplique le canal et laisse croire à deux dispositifs distincts alors
qu'il n'y en a qu'un.

**CP-16 — une rupture assumée est indiscernable d'une lacune.**
InterFast justifie explicitement l'absence de propagation du statut :
« Nous avons choisi de laisser cette étape manuelle car un chantier peut
nécessiter des préparations administratives (…) selon votre propre
organisation interne. » `statut_observation: rupture_documentee`
enregistre le fait, mais ne distingue pas un manque d'un choix de
conception revendiqué et motivé.

**CP-17 — un acteur appartenant à plusieurs périmètres simultanément.**
InterFast, sous-traitant multi-entreprise : invité avec l'adresse de son
propre compte, il « bascule de son espace au vôtre en un clic ». Il est
`externe` dans un périmètre et titulaire du sien dans un autre.
`perimetre` étant une valeur par interaction, cette double appartenance
n'est représentable nulle part.

**CP-18 — une interaction conditionnée par un seuil chiffré.**
InterFast, validation des commandes : « Définissez votre plafond de
tolérance (ex: 500 €). En dessous de ce seuil : les commandes sont
envoyées directement. Au-dessus : le processus de validation se déclenche
automatiquement. » Le schéma décrit des interactions qui existent ou non ;
il n'a aucun champ pour dire sous quelle condition une interaction
s'active. C'est aussi le cas des six autres formes de conditionnalité
relevées en §6.

Aucun de ces cas n'est résolu ici.

---

## 5. Boucles de retour vers l'émetteur

Rappel du Pilote A : 2 cas sur 30.

**B en documente trois de plus.**

| Cas | Boucle documentée |
|---|---|
| InterFast, validation des commandes | La plus complète du corpus. « Le validateur doit obligatoirement saisir un motif de refus » → « Le demandeur reçoit une notification avec le motif du refus » → « Il peut alors modifier la commande (…) et la soumettre à nouveau pour validation. » Demandeur → validateur → refus motivé → notification → modification → nouvelle soumission. |
| InterFast, guide complet — refus du devis | « Que se passe-t-il si le client refuse le devis ? Vous recevez également une notification. Le devis passera au statut Refusé. » |
| InterFast, guide complet — tracker d'emails | « InterFast intègre un tracker d'emails qui vous indique précisément l'heure et le nombre d'ouvertures de votre devis par le client. » |

Total sur les 40 articles analysés : **5 boucles de retour documentées**.
Une seule est interne à l'entreprise et complète — celle de la validation
des commandes. Les quatre autres portent sur le comportement du client.

**Ce comptage ne mesure rien du marché.** Il indique que, dans les
40 articles analysés, le retour vers l'émetteur est très rarement
documenté. Il ne permet en aucun cas de conclure qu'il est absent des
produits.

---

## 6. Mécanismes de coordination conditionnels

B fait apparaître **sept formes distinctes de conditionnalité**, toutes
documentées :

| Condition | Occurrence |
|---|---|
| **un seuil chiffré** | InterFast : « plafond de tolérance (ex: 500 €) » déclenche le circuit de validation |
| **une durée** | Vertuoza : au-delà du nombre de jours configuré, les photos ne sont plus sélectionnables |
| **un état de l'objet** | InterFast : le devis doit être « Accepté » pour accéder à Opérations ; l'avenant doit être « Accepté » pour entrer dans le solde |
| **un rôle** | InterFast : « les profils configurés comme Validateurs (…) ne sont pas soumis au plafond » ; le sous-traitant n'a « pas d'accès Web » |
| **un niveau d'abonnement** | InterFast : le fil du chantier est « disponible à partir de l'abonnement Pro » ; la validation des commandes « fait partie de l'abonnement Business » |
| **une case cochée à la création** | Vertuoza : un avancement « interne » ne pourra jamais être envoyé au client. InterFast : « Inclure la liste d'articles (sans les prix) » |
| **la présence d'une donnée** | Vertuoza : « si un responsable n'est pas sélectionné, alors vous ne saurez pas utiliser les réclamations pour la suite » |

Le contrat V2 n'a aucun champ pour représenter cette conditionnalité — 
voir CP-18. Les sept cas ci-dessus sont actuellement dispersés entre
`regles_operationnelles` et `signaux_emergents`, sans lien avec
l'interaction qu'ils conditionnent.

---

## 7. Phénomènes de A réapparaissant dans B

### Un objet dont le contenu change selon le lecteur — fortement confirmé

A : 2 occurrences. **B en ajoute quatre**, chez les deux spécialistes :

- Vertuoza : « paramétrer la visibilité des prix de votre ouvrier », dans
  la fiche du responsable d'intervention — la visibilité est un attribut
  du rôle, pas du document.
- InterFast, sous-traitant : « Il est possible de masquer les prix sur le
  PDF final, mais pas totalement lors de la saisie sur mobile
  actuellement. » Étanchéité partielle et documentée.
- InterFast, guide complet : « Inclure la liste d'articles (sans les
  prix) », « sans voir vos conditions commerciales ».
- InterFast, fil du chantier : un même fil, message interne ou visible par
  le client selon une icône.

Six occurrences sur 40 articles, chez deux éditeurs, sur quatre
mécanismes différents.

### Une continuité tenue par la discipline humaine — fortement confirmé

A : 7 occurrences. **B en ajoute cinq**, toutes chez InterFast :

- « prenez systématiquement le Bon de livraison en photo » ;
- « surveillez régulièrement votre consommation de temps (…) idéalement,
  chaque semaine » ;
- « prenez l'habitude de réaliser ces sorties de stock dès que vos
  techniciens signalent l'utilisation du matériel » ;
- « pensez tout de même à vérifier (…) la visibilité du message » ;
- « développez la bonne habitude de consulter systématiquement l'onglet
  Historique ».

Douze occurrences sur 40 articles. Formulation à conserver : dans
plusieurs situations documentées, la prévention dépend d'une consigne à
l'utilisateur plutôt que d'un contrôle produit décrit.

### Un rôle porté par l'objet — confirmé

Vertuoza, suivi gestionnaire : « Indiquez le responsable de la
réclamation. » Comme le « responsable » d'un avenant en A, c'est un champ
de formulaire, ni acteur ni destinataire d'une interaction documentée.

### Une prérogative déplacée d'un rôle à l'autre — confirmé, plus faiblement

InterFast : le sous-traitant, externe, remplit des rapports et fait signer
le client. Et « Qui peut modifier le statut d'un chantier ? Cette action
est possible pour l'ensemble des profils Utilisateurs ayant accès à
l'Application web. »

---

## 8. Nouveaux phénomènes apparus en B

Observations conservées telles quelles, sans en faire des catégories.

- **Un canal partagé dont l'audience se décide message par message.**
  InterFast, fil du chantier : cadenas pour l'interne, planète pour le
  client, dans un espace commun équipe + client.
- **Un espace applicatif dédié au client, révocable.** InterFast, Portail
  client : « un espace distinct de votre environnement de travail », où le
  client « n'a jamais accès à votre suivi de rentabilité, à vos prix
  d'achat fournisseurs ou au suivi de temps interne », et dont l'accès peut
  être retiré.
- **Un objet qui documente ses propres angles morts.** Le fil du chantier
  énumère quatre catégories d'événements qu'il ne capte pas, et précise
  que « le fil et l'onglet Documents restent deux espaces distincts ».
- **Une non-automatisation revendiquée et motivée.** Voir CP-16.
- **Un acteur appartenant à plusieurs entreprises du même logiciel.**
  Voir CP-17.
- **Une extraction automatique de document avec vérification humaine
  explicite.** InterFast : « L'intelligence artificielle analysera
  instantanément le document pour extraire le nom du fournisseur, la date
  (…) Vérifiez les informations extraites et modifiez-les si nécessaire. »
- **Une procédure de nettoyage de données enseignée par l'éditeur.**
  InterFast : « InterFast ne permet pas encore l'export de la Synthèse des
  Chantiers », puis copier-coller vers un tableur, suppression des « € »
  et des espaces par Rechercher-Remplacer, reformatage en Devise.
- **Une coordination qui s'active à un montant.** Voir CP-18.

### Sur le contraste collaboration

Formulation exigée, à ne pas élargir :

> Dans les articles B étudiés, InterFast documente un fil de collaboration
> rattaché au chantier, tandis que l'article Sellsy étudié inclut une
> recommandation d'utiliser Slack pour la messagerie interne.

Le fil InterFast est en bêta et « nécessite une activation préalable par
l'équipe support ». L'article Sellsy porte le titre « Découvrez toutes nos
fonctionnalités collaboratives » et recommande « Slack version gratuite ».
Ces deux faits sont documentés ; ils ne permettent aucune conclusion
comparative sur les produits, ni sur ce que chaque éditeur propose
ailleurs dans son corpus.

---

## 9. Le contrôle définition ≠ mécanisme

Rappel A : 3 transmissions sur 23 (13 %) reposaient sur une phrase
définitionnelle ou un verbe au passé.

**B : 12 transmissions, 2 faibles (17 %).** Nommément :

| Article | Citation portant la preuve | Problème |
|---|---|---|
| Vertuoza, suivi gestionnaire | « vous ne pourrez pas l'envoyer par mail au client final » | **formulation négative** : la capacité d'envoi est prouvée par ce qui l'empêche, non par un geste décrit. |
| InterFast, fil du chantier | « Cela permet d'adresser clairement une demande à une personne précise. » | **formulation de capacité** (« permet »), non geste observé. Le geste existe ailleurs dans l'article (bouton @, flèche d'envoi) ; j'ai cité le mauvais passage. |

Les dix autres s'appuient sur un geste ou un événement décrit.

**Les 2 `validation` de B :** celle d'InterFast validation des commandes
est solide (« 2 options sont possibles : valider ou refuser la
commande »). Celle du guide complet repose sur « Le Client peut consulter,
valider ou refuser le document » — **formulation de capacité**, atténuée
par le fait que l'article documente séparément le changement de statut
automatique et le message de confirmation affiché au client.

**Le contrôle tient, au même taux qu'en A.** Le glissement statut → action
reste mort ; le glissement définition/capacité → mécanisme persiste
autour de 15 %, sur les deux échantillons. C'est un défaut d'exécution
stable, pas une dérive.

---

## 10. Rendement des signaux émergents

A : environ 12 sur 23 révélaient un aplatissement réel (52 %).

**B : 13 sur 15 (87 %).** Les deux que je retire à la relecture :

- Vertuoza, visibilité des prix : largement porté par le mécanisme
  `permission` et la règle associée ;
- Sellsy, trois couches d'accès : les trois règles le disent déjà.

**Cette hausse ne signifie pas que le schéma s'est amélioré.** B a été
sélectionné sur la coordination, et la coordination est précisément le
domaine où le contrat V2 n'a pas de vocabulaire : conditionnalité,
audience par message, appartenance multiple, non-automatisation assumée,
péremption. Un rendement de signaux plus élevé en B mesure **la densité
des angles morts du schéma dans ce domaine**, pas sa qualité.

Quatre des cinq nouveaux CP de ce mini-audit sont d'ailleurs nés de
signaux émergents.

---

## 11. Ownership

| | Emplacements déterminables | Total | % |
|---|---:|---:|---:|
| Pilote A | 24 | 180 | **13 %** |
| Pilote B | 18 | 66 | **27 %** |

**Le taux double, et reste faible.**

Répartition en B : les trois articles décrivant explicitement un circuit
concentrent 14 des 18 emplacements renseignés — validation des commandes
(5), guide complet (6), profil sous-traitant (3). Le fil du chantier, avec
ses cinq transitions, n'en renseigne **aucun** : les événements y sont
horodatés et nominatifs à l'affichage, mais l'article ne dit jamais à qui
l'objet appartient avant et après.

Formulation à conserver :

> Même dans des articles sélectionnés pour leur richesse en passages de
> main, l'ownership des objets n'est documenté que sur un peu plus d'un
> quart des extrémités de transition, dans le corpus analysé.

Et non : « les produits ne gèrent pas l'ownership ».

**Note complémentaire.** `resolution_documentee` chute : 42 % renseigné en
A, **23 % en B** (12 sur 53). Les règles de B énoncent davantage de
contraintes sans remède documenté que celles de A. Constat brut, sur deux
échantillons non comparables.

---

## 12. V2 reste-t-il exploitable pour l'analyse de coordination ?

**Oui, mais il atteint sa limite exactement là où B l'a poussé.**

### Ce qui fonctionne

- Les trois contrôles négatifs passent. `affectation`, `visibilite` et
  `permission` retiennent ce que `transmission` aurait absorbé.
- `perimetre`, `dans_logiciel` et `canal` sont renseignés à 100 % en B —
  aucun `inconnu`, aucun `aucun`. La valeur `fil_activite`, inutilisée en
  A, sert deux fois. L'énumération des canaux tient.
- La granularité des mécanismes monte de 2,0 à 4,6 par article sans
  produire de bruit : les 46 mécanismes de B sont tous adossés à une
  citation distincte.
- `edition_partagee` n'apparaît **aucune fois** en B. Un schéma qui laisse
  une forme à zéro sur un échantillon où elle n'existe pas est un bon
  signe.

### Ce qui bloque

Quatre recommandations pour l'arbitrage post-B. **Je ne résous rien ; je
classe par coût.**

1. **`ruptures.type` est le champ à revoir en priorité.** CP-7
   (non-propagation), CP-14 (péremption) et CP-16 (non-automatisation
   assumée) disent la même chose sous trois formes : trois valeurs ne
   suffisent pas, et `reconstruction_contexte` sert de fourre-tout dans
   10 des 21 ruptures des deux pilotes. Pour une étude qui porte sur la
   continuité, c'est le défaut le plus coûteux après CP-12.

2. **CP-12 reste le blocage n° 1 pour H1.** Les noms d'objets ne sont
   toujours pas normalisés ; les 123 transitions des deux pilotes ne
   peuvent pas être jointes. Le guide complet, à lui seul, décrit une
   chaîne de quatorze transitions qu'aucun calcul ne peut reconstituer.

3. **CP-18, la conditionnalité, est le manque le plus visible sur la
   coordination.** Sept formes documentées en dix articles, aucune
   représentable. Une interaction qui n'existe qu'au-dessus de 500 € n'est
   pas la même chose qu'une interaction permanente, et le schéma les écrit
   de la même façon.

4. **CP-4 doit être tranché.** Cinq occurrences, sur le geste le plus
   courant de la relation client en métier de terrain. Deux issues
   possibles — relâcher la définition de `validation`, ou reconnaître une
   forme absente. **Cet arbitrage ne m'appartient pas.**

### Ce que je ne recommande pas

Rouvrir le contrat avant d'avoir décidé du périmètre de l'analyse C. Trois
des quatre points ci-dessus ne comptent que si H1 et la coordination
restent les axes retenus. Si le corpus étendu désigne une autre dimension,
l'ordre de priorité change.
