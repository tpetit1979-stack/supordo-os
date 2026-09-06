# Crash-test d'utilité — Pilote A V2

> Cette analyse évalue l'utilité analytique de V2 sur les 30 articles du
> Pilote A. Elle ne constitue ni un benchmark des concurrents ni une
> conclusion de marché.

## Avertissement de provenance

Une synthèse narrative de ces mêmes 30 articles a été produite avant ce
crash-test. À la relecture honnête : **elle venait majoritairement des
articles source, pas des YAML.** Ce document distingue donc
systématiquement ce que les YAML ont permis de voir de ce que seule la
lecture permettait. C'est le seul moyen de juger l'instrument plutôt que
le corpus.

Trois niveaux d'affirmation sont explicitement séparés :
**FAIT DOCUMENTÉ**, **INTERPRÉTATION**, **QUESTION OUVERTE**.
Un silence documentaire n'est jamais traité comme une absence produit.

---

## 1. Ce que les 10 articles Vertuoza apprennent

**FAIT DOCUMENTÉ.** Le produit est organisé autour d'une partition de
comptes : « Visualisation, Édition et Clôture (compte gestion) » face à
« aller sur votre compte chantier sur mobile ». Cette partition
détermine à la fois le rôle, l'appareil et les actions possibles sur un
même objet.

**FAIT DOCUMENTÉ.** Trois circuits terrain → bureau sont décrits, avec un
acte de bascule explicite à chaque fois :

- suivi de chantier — « Pour le rendre visible aux gestionnaires,
  clôturez le suivi » ;
- rapport d'intervention — « Cela indiquera au gestionnaire que tout
  s'est déroulé comme prévu et qu'il peut clôturer cette intervention » ;
- pointage — « Le pointage validé sera ensuite clôturé par le
  gestionnaire ou la secrétaire sur ordinateur ».

**FAIT DOCUMENTÉ.** L'ouvrier décide sur le terrain de ce qui sera
facturé : « L'ouvrier peut définir si la main-d'œuvre est facturable ou
non, modifier le prix unitaire et ajouter une note », et « L'élément
apparaîtra sur la facture si l'option facturable est activée ».

**FAIT DOCUMENTÉ.** Le pointage n'est pas saisi mais généré : « Un
pointage est automatiquement généré chaque jour, pour chaque ouvrier en
fonction du planning de chantier et d'intervention. »

**INTERPRÉTATION.** Vertuoza traite le terrain comme un producteur de
données financières, pas seulement comme un exécutant. Trois des cinq
articles terrain de l'échantillon confient à l'ouvrier ou au chef
d'équipe une décision qui engage la facture ou la paie.

**QUESTION OUVERTE.** Les cinq articles bureau (devis, avenant,
acomptes, correction d'avenant, modification de devis validé) ne nomment
aucun rôle. Vertuoza ne différencie-t-il pas les rôles côté bureau, ou
est-ce la convention du « vous » ? Non déterminable ici.

**Apport du YAML : faible.** La narration vient des sources. Le YAML a
servi à un seul constat : les six acteurs nommés du corpus Vertuoza sont
tous des rôles terrain — ce qui ne se voit qu'en agrégeant.

---

## 2. Différences observables sur les situations comparables

Seules six situations sont réellement comparables dans cet échantillon.

| Situation | Vertuoza | InterFast | Sellsy |
|---|---|---|---|
| Devis → acceptation | Statuts définis, commandes côté entreprise : « Envoyer, Refuser, Accepter » | Trois chemins dont un automatique : « Votre client a signé (…) Votre devis passe automatiquement comme étant Accepté » | Signature envoyable au client **ou à un collaborateur interne** |
| Avenant | Contenu et intégration décrits ; qui accepte n'est pas dit | Cycle de vie à trois états + fusion automatique au solde | Non trouvé dans les articles Sellsy analysés |
| Facturation par étapes | 10 étapes, 3 règles | 12 règles, dont verrouillage anti-fraude et cinq chemins de rattrapage | Non trouvé sous cette forme dans l'échantillon |
| Rapport d'intervention | Rédigé par l'ouvrier sur mobile, verrouillé après acceptation | Rédigeable aussi par le bureau, avec choix de conserver ou remplacer la signature du collègue | Non trouvé dans l'échantillon |
| Heures | Généré depuis le planning, validé terrain, clôturé bureau, exporté paie | Saisi par le salarié, validé/refusé par l'Employeur, boucle de correction | Non trouvé dans l'échantillon |
| Droits | Deux types de comptes | Accès aux documents cochés par rôle | Profil de privilèges × licence, plus écran de comparaison |

**INTERPRÉTATION.** Sur ces six situations, InterFast documente ses
contraintes davantage que les deux autres (65 règles contre 36 et 44).
Cela peut refléter un produit plus contraint, une documentation plus
mature, ou une culture éditoriale différente — les trois hypothèses sont
compatibles avec les données.

**QUESTION OUVERTE.** Quatre des six lignes portent « non trouvé dans
l'échantillon » pour Sellsy. L'échantillon Sellsy a été choisi par
substitution, la comparaison n'est donc pas contrôlée. **Ce tableau ne
permet aucune conclusion sur Sellsy.**

---

## 3. Cinq mécanismes que la grille ne demandait pas de chercher

1. **Vertuoza — compte chantier / compte gestion.** FAIT. La frontière
   terrain/bureau est une architecture de comptes, pas un réglage.
2. **InterFast — le statut « Facturé » posé à la main.** FAIT : « Elle
   sert uniquement à nettoyer votre tableau de bord des devis En cours »
   et « ne génère aucune écriture comptable ». INTERPRÉTATION : un champ
   porte simultanément un fait comptable et un état de charge de travail,
   et l'éditeur assume de le laisser mentir sur le premier.
3. **InterFast — la liste de matériel sans les prix d'achat.** FAIT :
   « En liant votre liste de matériel (sans les prix d'achat) au
   chantier, vos techniciens peuvent charger le camion sans erreur. »
4. **Vertuoza — la quantité avancée.** FAIT : « 10mc de gouttière pour la
   façade avant + 5mc pour la façade est + 3mc de sécurité = 18mc »,
   affichable ou non selon le template.
5. **Sellsy — la dictée vocale de la note d'appel.** FAIT : « utiliser la
   synthèse vocale pour résumer les points clé dans les notes ».

**Apport du YAML : réel, sur trois des cinq.** Les mécanismes 2, 3 et 5
ont été écrits parce que `signaux_emergents` obligeait à se demander ce
qui restait aplati.

---

## 4. Cinq continuités documentées

### ① Facturation du solde avec avenants — InterFast

- Situation : chantier terminé, avec plus-values ou moins-values.
- Objet avant : devis initial `Accepté` + avenants `Accepté`.
- Action : *Facturer* → *Facturer le solde*.
- Objet après : facture de solde.
- Contexte conservé : montant du devis, montant des avenants avec leur
  signe, acomptes déjà versés, et mention des deux documents au
  récapitulatif.
- Preuve : « reprendra automatiquement le montant du devis initial + ou -
  le montant de l'avenant, tout en déduisant les acomptes déjà versés ».
- **Ne permet pas d'affirmer** que les données techniques du devis
  (descriptions, quantités, ouvrages) soient reprises. La source ne parle
  que de montants.

### ② Pointage généré depuis le planning — Vertuoza

- Situation : fin de journée, chef d'équipe sur mobile.
- Objet avant : planning de chantier et d'intervention.
- Action : génération automatique quotidienne.
- Objet après : un pointage par ouvrier, à valider.
- Contexte conservé : « Si les informations sont correctes dans les
  plannings, le chef d'équipe n'a qu'à les valider ».
- **Ne permet pas d'affirmer** ce qui se passe quand le planning est faux
  ou vide. Le « si » n'est jamais développé.

### ③ Série d'interventions journalières — InterFast

- Objet avant : chantier + dates sélectionnées au calendrier.
- Action : planification.
- Objet après : une intervention par jour, « inter-reliées les uns aux
  autres ».
- Contexte conservé : le rattachement au chantier sur chaque journée.
- **Ne permet pas d'affirmer** que le contenu technique ou le matériel
  soit repris d'un jour sur l'autre.

### ④ Interventions terminées → feuille de temps — InterFast

- Objet avant : interventions marquées terminées dans la journée.
- Action : ouverture de la feuille de temps mobile.
- Objet après : feuille de temps pré-remplie.
- Contexte conservé : les interventions « apparaissent sous les plages
  horaires correspondantes ».
- **Ne permet pas d'affirmer** que les heures réelles soient reprises. Et
  le même article documente que cette continuité casse si la feuille a
  été enregistrée en brouillon avant.

### ⑤ Achèvement terrain → planning du gestionnaire — Vertuoza

- Objet avant : rapport d'intervention accepté par l'ouvrier.
- Action : acceptation.
- Objet après : intervention verte sur le planning du gestionnaire,
  rapport « Clôturé ».
- **Ne permet pas d'affirmer** que le gestionnaire soit notifié.
  « Deviendra verte sur le planning » suppose qu'il regarde le planning.

**Apport du YAML : moyen.** Les cinq continuités sont lisibles dans les
sources. En revanche la ligne « ne permet pas d'affirmer » vient
directement de la discipline `continue_documentee` vs `non_determinable`.

---

## 5. Ruptures documentées, en expérience utilisateur

**Le sous-traitant — InterFast.** Il pointe ses heures toute la semaine.
Vendredi, elles ne sont pas dans la marge : « les heures effectuées par
un profil externe ayant le rôle Sous-traitant ne sont pas valorisées
financièrement dans le déboursé de main-d'œuvre interne ». Il faut
attendre sa facture et la ressaisir dans l'onglet Dépenses. Le travail
est enregistré deux fois — une fois en temps sans valeur financière, une
fois en euros tapés à la main.

**Le mauvais client — InterFast.** « Il est impossible de modifier le
client associé à un chantier existant. » Il faut archiver et recréer.

**L'acompte orphelin — InterFast.** La facture de solde ne déduit pas
l'acompte, « si vous avez importé vos données d'un ancien logiciel ou si
le lien a été brisé ». Il faut ouvrir l'acompte et cliquer « Lier à un
devis ». Sans cela, on réclame au client une somme déjà payée.

**L'astreinte du soir — InterFast.** Feuille du lundi validée,
intervention à 22h. « Il n'est pas possible d'avoir deux feuilles de
temps pour la même date » et « vous ne devez pas utiliser le bouton
Déclarer une astreinte ». Il faut faire refuser la feuille par
l'employeur ; si celui-ci l'a déjà validée, « votre Employeur devra
solliciter l'aide du Support dans le tchat en ligne ».

**La feuille en brouillon — InterFast.** Une intervention réalisée après
l'enregistrement en brouillon n'apparaît pas. « Pour la charger, appuyez
sur les trois petits points (…) puis Réinitialiser » — une action que
rien ne signale.

**Le paiement invisible du comptable — InterFast/Pennylane.** « Cette
information ne redescend pas encore automatiquement dans Pennylane. »

**L'import Excel — Vertuoza.** « Les informations générales et mentions
légales doivent être saisies dans Vertuoza. » On importe les prix, on
retape le contexte.

**Le doublon — Sellsy.** « La copie ne sera pas rattachée au cycle de
vente du document d'origine. »

**Apport du YAML : élevé.** L'inventaire de 14 ruptures typées, chacune
avec preuve positive, est le produit le plus directement exploitable du
dispositif. Aucune ne vient d'un silence.

---

## 6. Situations dépendant d'une discipline humaine

Sept occurrences, **chacune limitée à son article**. Aucune
généralisation à un produit entier.

- **InterFast, article Pennylane** : « Contrôler un lot après une journée
  d'émission : filtrez sur Non exportée. La liste doit être vide. »
- **Sellsy, article avoirs** : « il faudra penser à annuler ces
  prélèvements » GoCardless.
- **InterFast, article hors ligne** : précharger « dans votre véhicule en
  arrivant devant le bâtiment » ; « ne cliquez pas tout de suite sur
  Terminer l'intervention ».
- **Vertuoza, article pointage** : « Motiver vos chefs d'équipe à arriver
  à 0 à la fin de chaque journée. »
- **InterFast, article chantier** : « demandez à vos techniciens
  d'actualiser leur application » après un changement de droits.
- **InterFast, article facture** : « Ne créez pas de facture test en
  usage réel. »
- **Sellsy, article mobile** : « Pensez à vérifiez le destinataire et le
  contenu avant l'envoi. »

**INTERPRÉTATION.** Dans plusieurs situations documentées, la prévention
dépend d'une consigne à l'utilisateur plutôt que d'un contrôle produit
décrit. Sept occurrences sur 30 articles est un signal, pas une mesure.

**QUESTION OUVERTE.** Ces sept cas sont-ils des zones connues des
éditeurs, ou l'artefact d'un genre documentaire qui donne naturellement
des conseils ? Non tranchable ici.

---

## 7. Passages entre rôles

**Réellement outillés**

- **Terrain → bureau.** Vertuoza (trois articles) et InterFast (feuilles
  de temps). Chez InterFast, seul passage du corpus avec boucle de retour
  complète : En attente / Validée / Refusée, et « Elle repasse parmi les
  déclarations à saisir / modifiables ».
- **Entreprise → client.** Les trois éditeurs, avec mécanismes
  documentés.
- **Administrateur → collaborateur.** Les trois, sous forme de permission.
- **Entreprise → comptable.** InterFast (« votre comptable pourra la
  rattacher manuellement ») et Sellsy (accès « réservé à une personne
  externe »).
- **Collaborateur → collaborateur pour signature.** Sellsy uniquement.

**Seulement suggérés**

- **Bureau → terrain.** InterFast affecte et notifie, mais aucun article
  ne documente que le technicien accepte, refuse, ou que le bureau sache
  qu'il a vu. C'est une affectation, pas un relais.
- **Bureau reprenant le travail du terrain.** InterFast : deux rôles
  éditent le même objet successivement, rien n'est transmis, et le
  rédacteur initial n'est pas prévenu.
- **Entreprise ↔ sous-traitant.** Rôle et accès existent, heures
  financièrement inertes.

**Impossibles à déterminer dans cet échantillon**

- Commercial → métreur ou visite technique : zéro article.
- Terrain → terrain. Atelier/stock → chantier.
- Le retour vers l'émetteur en général : deux cas sur 30.

**Apport du YAML : élevé.** `perimetre` et `dans_logiciel` produisent un
fait invisible article par article : quatre interactions sur 44 se
passent hors du logiciel, et trois s'adressent à l'éditeur et non à un
collègue.

---

## 8. Dix règles structurantes

Critère unique : elles obligent à travailler autrement, ou à travailler
ensemble.

1. **IF** — « il est figé pour garantir la traçabilité juridique et
   commerciale » (devis Accepté). On n'ajuste plus, on annexe.
2. **IF** — « doit impérativement être passé au statut Accepté pour être
   pris en compte ». Un avenant oublié en Envoyé fausse le solde.
3. **IF** — « la législation anti-fraude à la TVA interdit de la modifier
   ou de la supprimer ».
4. **IF** — « un devis ne peut être lié qu'à une seule facture en
   brouillon ». Sérialise le travail administratif.
5. **IF** — « logique d'intervention journalière (max 24h) ». Structure
   le rythme du terrain.
6. **IF** — « les profils terrain (…) n'ont pas accès à votre onglet
   Documents (…) ni à vos marges ».
7. **Vertuoza** — « Une fois accepté, l'ouvrier ne peut plus modifier le
   rapport. »
8. **Vertuoza** — « Pour le rendre visible aux gestionnaires, clôturez le
   suivi. » La visibilité est un acte, pas un état.
9. **IF** — « votre Employeur devra solliciter l'aide du Support dans le
   tchat en ligne ».
10. **Sellsy** — « vous ne pourrez pas accéder à la fonctionnalité si
    votre licence ne l'inclut pas ». Deux systèmes de droits superposés.

Cette sélection n'est pas une statistique : dix règles de trois produits
sur trente articles choisis par thème.

---

## 9. Erreurs, corrections, réouvertures

**FAIT DOCUMENTÉ — trois régimes.**

*Libre tant que brouillon.* Partout.

*Verrouillé par la loi.* Correction par contre-document uniquement.
InterFast : avoir total puis recréation. Vertuoza : « Créditer la
Facture ». Sellsy : un avoir finalisé ne peut pas être supprimé, on le
neutralise par « une facture du même montant que l'avoir ».

*Verrouillé par le workflow* — et c'est là que l'organisation apparaît :

- **Vertuoza / pointage** : le chef d'équipe rouvre lui-même —
  « L'icône se transformera en flèche, permettant de rouvrir le
  pointage ».
- **InterFast / feuille de temps** : seul l'Employeur, en refusant ; et si
  déjà validée, l'éditeur.
- **InterFast / rapport** : le bureau peut éditer le rapport signé d'un
  collègue, avec « deux choix (…) remplacer la signature initiale du
  collaborateur par sa propre signature » ou la conserver.

**FAIT DOCUMENTÉ.** Deux fois, l'éditeur est le dernier maillon, les deux
chez InterFast : rouvrir une feuille de temps validée, et valider la
conversion en crédit d'une licence ajoutée par erreur.

**INTERPRÉTATION.** La capacité de correction est distribuée
différemment : Vertuoza rend au terrain le droit de se corriger,
InterFast le remonte à la hiérarchie puis à l'éditeur, Sellsy le traite
comme une question de droits.

**QUESTION OUVERTE.** Deux occurrences ne font pas une politique produit.
À vérifier sur les 227 articles InterFast restants.

---

## 10. Les 23 signaux : lesquels révèlent un aplatissement réel

Regroupements manifestes seulement, sans ontologie.

- **Un objet dont le contenu dépend du lecteur — 2 signaux.** IF liste de
  matériel sans prix d'achat ; Sellsy liste des règlements filtrée par
  périmètre. Les blocs savent dire « accès accordé/refusé », pas
  « contenu différent ». **Aplatissement réel.**
- **Un rôle porté par l'objet — 3 signaux.** Vertuoza « responsable » ;
  Sellsy « référent en charge » ; InterFast signature du rédacteur.
  **Aplatissement réel.**
- **Une continuité tenue par l'humain — 4 signaux.** Voir §6.
  **Aplatissement réel.**
- **Une prérogative déplacée d'un rôle vers un autre — 2 signaux.**
  Vertuoza l'ouvrier décide du facturable ; IF le Technicien + encaisse.
  **Aplatissement réel.**
- **Un mode de saisie — 1 signal.** Sellsy dictée vocale.
  **Aplatissement réel.**

**Signaux plus faibles** : le « Récapitulatif des privilèges » et les
quatre types de contacts Sellsy restaient largement représentables en
règles ; le signal Vertuoza sur WhatsApp/papier documente un état
antérieur du travail, pas le produit.

**Bilan : environ 12 signaux sur 23 révèlent un aplatissement réel.**

---

## 11. Ce qui reste hors de portée

### A — Non documenté dans les 30 articles

*Vérifiable en élargissant l'échantillon.*

- Toute l'amont : demande, qualification, visite technique, relevé,
  étude / note de calcul. Zéro.
- SAV et maintenance comme origine : zéro sur 30.
- Le planning comme objet de travail : attribution, déplacement, conflit.
- Stock, commande fournisseur, réception matériel.
- Parc installé et équipements.
- Le pilotage : rentabilité, déboursé sec, mentionnés comme conséquences.
- Quatre concurrents déjà collectés n'ont pas été touchés.

### B — Ce que ce type de source ne permet probablement pas d'établir

*Élargir l'échantillon n'y changera rien.*

- Si les mécanismes documentés fonctionnent, sont utilisés, ou sont
  supportables au quotidien.
- La charge réelle d'un gestionnaire avec trente chantiers en cours. Un
  centre d'aide ne décrit jamais la simultanéité.
- Pourquoi une contrainte existe — arbitrage produit, dette technique ou
  obligation légale.
- Ce que les utilisateurs contournent réellement.
- Délais, fiabilité, performance.

### C — Défauts de notre instrument

- **`objet_source` et `objet_resultat` ne sont pas normalisés.** On ne
  peut pas joindre les 90 transitions pour reconstruire le graphe des
  objets. C'est la question centrale de H1, et elle n'est pas calculable.
  Consigné en CP-12.
- **V2 a supprimé `job_to_be_done`, présent en V1.** Un YAML V2 lu seul
  ne dit pas à quoi sert l'article. Consigné en CP-13.
- **Aucune notion d'importance.** Une règle sur le verrouillage
  anti-fraude et une règle sur l'ordre des colonnes ont la même forme.
  Méthodologiquement correct, analytiquement coûteux.
- **La comparabilité inter-concurrents n'est pas encodée.**

---

## 12. Cinq questions à investiguer

1. **Où s'arrête le document commercial et où commence l'acte
   technique ?** Zéro article sur 30 documente la visite, le relevé ou
   l'étude.
2. **Le retour vers l'émetteur est-il une convention documentaire ou une
   absence produit ?** Deux cas sur 30. Si le ratio tient sur 500
   articles, on pourra dire qu'il est très rarement documenté dans le
   corpus analysé — jamais qu'il est absent des produits.
3. **À quelle fréquence l'éditeur est-il le dernier maillon d'un
   rattrapage ?** Deux fois en dix articles InterFast. Un produit dont
   les chemins de correction finissent dans le chat du support soulève
   une question de scalabilité organisationnelle à 30 personnes.
4. **L'attribution du travail est-elle jamais accusée réception ?**
   L'affectation est partout, l'acceptation nulle part.
5. **Le contenu d'un objet varie-t-il selon le rôle qui le regarde ?**
   Deux occurrences, chez deux éditeurs différents.

---

## VERDICT : B — PARTIELLEMENT UTILE

Le dispositif produit des enseignements concurrentiels réels et
vérifiables, mais **la part la plus riche de la compréhension vient
encore des sources, pas des YAML.**

### Trois apports de valeur

1. **L'inventaire des ruptures.** Quatorze ruptures typées, chacune
   adossée à une preuve positive, sur 90 transitions, aucune déduite d'un
   silence. Cet objet n'existe dans aucun article et ne se produit pas
   par lecture.
2. **`perimetre` et `dans_logiciel` produisent un fait que la lecture ne
   donne pas.** Quatre interactions sur 44 hors du logiciel, trois
   adressées à l'éditeur. C'est ce qui transforme une impression en
   observation comptée.
3. **La typologie des mécanismes a révélé une contradiction.** L'article
   « Créer un chantier » d'InterFast se conclut par « fluidifiez la
   communication entre vos équipes de terrain et le bureau ». Codé
   mécanisme par mécanisme, il contient une affectation, une
   notification, une permission, une visibilité — **et zéro
   transmission.** L'écart entre la promesse et ce que l'article
   documente vient entièrement de la discipline du codage.

### Trois échecs

1. **La narration du §1 ne doit quasiment rien aux YAML.** Avec les 30
   YAML sans les articles, elle serait impossible : il manque la
   séquence, l'intention et le pourquoi. La suppression de
   `job_to_be_done` aggrave cela.
2. **Le graphe des objets n'est pas calculable.** 90 transitions, noms
   d'objets en chaînes libres non normalisées.
3. **Onze signaux sur vingt-trois n'apportent rien que les blocs
   structurés ne portaient déjà.** Rendement de moitié.

---

## Ce que cela change — ou ne change pas — pour la suite

**Ne change pas.** Le contrat reste valable pour le Pilote B. B porte sur
la coordination, domaine où le dispositif a le mieux fonctionné :
`perimetre`, `dans_logiciel` et la typologie des mécanismes sont les
trois apports démontrés. Rien ici ne justifie de rouvrir le schéma avant
B.

**Change, à trancher avant l'industrialisation — pas avant B.**

- CP-12, la normalisation des noms d'objets, est le seul défaut qui
  empêche une question centrale d'être posée. Arbitrage plus lourd que
  CP-1 à CP-3.
- CP-13, la régression `job_to_be_done`, mérite un examen. Le mini-audit
  ne l'avait pas vue parce qu'il jugeait la conformité, pas l'utilité.

**Change pour la lecture des résultats.** Les YAML seuls ne suffisent
pas : toute restitution devra continuer à s'appuyer sur les sources. Le
dispositif est un instrument de repérage et de comptage fiable, pas un
substitut à la lecture.

**Une remarque orientée SUPORDO, et une seule.** Les deux découvertes les
plus inattendues de ces 30 articles — un objet dont le contenu change
selon le rôle, et une prérogative qui se déplace d'un rôle à un autre —
ne figuraient dans aucune de nos hypothèses de départ. Elles ne valident
ni H1 ni H2. Si le reste du corpus les confirme, elles mériteront d'être
traitées comme une hypothèse distincte, et non ajoutées aux deux
existantes.
