---
url: https://inter-fast.fr/ressources/blog/articles/blog-maintenance-curative-delais
url_finale: https://inter-fast.fr/ressources/blog/articles/blog-maintenance-curative-delais
date_collecte: 2026-09-07
destination: site_marketing
---

Un client tertiaire vous appelle à 9h pour une panne de chauffage. Vous lui dites que vous passez. Le tech arrive à 14h, diagnostique en 30 min, et constate qu'il manque la pièce. Il revient le lendemain à 11h pour l'installer. Bilan : 26 heures entre l'appel et la remise en service. Le client est mécontent, votre tech a fait 2 déplacements pour 1 panne, et la prochaine fois qu'un concurrent passera, le client écoutera. **Votre problème n'est pas la panne. C'est le délai.**

Cet article structure la méthode pour réduire les délais d'intervention curative dans une PME CVC : qu'est-ce que le MTTR, comment le calculer, les 5 leviers concrets pour le réduire, et les KPIs à suivre. Pas la version industrielle d'IBM, la version terrain pour 5-15 techniciens.

## 01 - MTTRCe que mesure vraiment le MTTR (et pourquoi c'est central)

Le **MTTR** (Mean Time To Repair) est l'indicateur central de la maintenance curative. Il mesure le temps moyen nécessaire pour remettre en service un équipement après une panne. C'est l'inverse du MTBF (Mean Time Between Failures, temps moyen entre 2 pannes) qui lui mesure la fiabilité.

**Formule MTTR :**

MTTR = temps total consacré aux réparations / nombre de réparations sur la période.

Exemple concret : sur 1 mois, votre PME a fait 12 dépannages représentant un total de 60 heures cumulées de « temps panne client » (de l'appel à la remise en service). MTTR = 60/12 = **5 heures**.

**Attention à la nuance :** il existe 4 variantes du MTTR.

- **MTTR (Repair)** : temps actif de réparation par le tech, hors logistique
- **MTTR (Recover)** : temps total de la panne pour le client, du déclenchement à la remise en service complète
- **MTTR (Resolve)** : temps total jusqu'à résolution complète du problème (avec validation)
- **MTTR (Respond)** : temps moyen de réponse, de la détection au début d'intervention

Pour une PME CVC qui pilote la satisfaction client, **c'est le MTTR Recover qui compte vraiment**. C'est ce que ressent le client : combien de temps son équipement a été inutilisable. Pas le temps actif du tech.

**Benchmark sectoriel :**un MTTR Recover moyen sous

**5 heures**est considéré comme bon. Sur des contrats premium ou critiques (EHPAD, salle blanche, data center), on descend à 2-3h. Au-dessus de 8h en moyenne sur du tertiaire courant, vous avez un problème structurel.

## 02 - FacteursLes 5 facteurs qui plombent les délais d'intervention

Avant les solutions, identifier précisément ce qui ralentit. Dans une PME CVC, ces 5 facteurs reviennent systématiquement.

**Facteur 1 : Diagnostic à distance impossible.**

Le client appelle, dit « ma chaudière ne marche plus ». Le dispatcher n'a aucune info technique pour préparer l'intervention. Le tech part à l'aveugle, perd 20-30 min sur place pour comprendre, repart chercher la pièce. Sans pré-qualification téléphonique structurée, vous payez systématiquement 1h de surcoût par panne.

**Facteur 2 : Pièces détachées non disponibles.**

Le tech diagnostique sur place : il faut un compresseur, un thermostat, une pompe. Pas dans la camionnette. Pas au dépôt. Il faut commander chez le fournisseur, livraison J+1 ou J+2. C'est ce qui transforme une panne de 3h en panne de 36h. Sur les contrats CVC, c'est le facteur n°1 d'allongement du délai.

**Facteur 3 : Affectation lente du technicien.**

La panne arrive à 14h. Votre dispatcher cherche qui est dispo, qui est compétent, qui est proche. 30-45 min de coups de fil pour décider qui y va. Ce temps est invisible mais compte dans le MTTR Recover du client.

**Facteur 4 : Trajet et accès au site.**

Tech à 45 min de route, parking impossible, code immeuble pas à jour, contact technique du site introuvable. Tout ça fait 30-60 min de plus avant le diagnostic. Souvent évitable avec une bonne fiche site dans la GMAO.

**Facteur 5 : Pas de procédure standardisée pour le diagnostic.**

Chaque tech diagnostique à sa façon, avec son expérience. Un tech junior met 2x plus de temps qu'un tech senior pour la même panne. Sans procédure standardisée (arbres de décision, checklist), vous payez le différentiel.

Ces 5 facteurs cumulés peuvent faire passer un MTTR théorique de 3h à un MTTR réel de 12h. Inversement, traiter ces 5 points peut diviser votre MTTR par 2 sans engager une seule heure technicien supplémentaire.

### Pilotez votre maintenance curative dans un outil unifié

Pré-qualification structurée, fiches équipement enrichies, stock atelier connecté, checklists embarquées : InterFast couvre toute la chaîne curative pour réduire votre MTTR sans surcoût technicien.

[Voir le logiciel GMAO](https://inter-fast.fr/fonctionnalites/logiciel-gmao)

[Essayer gratuitement](https://app.inter-fast.fr/register)

## 03 - Pré-qualificationLevier 1 : La pré-qualification téléphonique structurée

Le MTTR commence à l'appel client. La qualité de cette première étape détermine 30-40 % du temps total.

**Ce que doit obtenir le standard ou le dispatcher en 5 minutes :**

- Identification précise de l'équipement concerné (marque, modèle, année si possible, lieu dans le bâtiment)
- Description du symptôme par le client (avec questions guidées : « ça fait du bruit ? ça affiche un code ? ça démarre puis s'arrête ? la lumière est verte/rouge/éteinte ? »)
- Photo du panneau de contrôle ou du voyant si possible (envoyée par SMS pendant l'appel)
- Date de la dernière intervention sur cet équipement
- Niveau d'urgence client réel (peut-il attendre 24h ? besoin immédiat ?)
- Accès au site, contact sur place, particularités

Avec ces infos, le dispatcher peut :

- Identifier la panne probable dans 60-70 % des cas
- Pré-charger les pièces probables dans la camionnette du tech
- Affecter le tech ayant le plus d'expérience sur ce type de panne
- Donner au tech le contexte avant départ

Une intervention bien pré-qualifiée se déroule en 1h sur place. Une intervention mal pré-qualifiée se déroule en 2-3h. Le différentiel est massif et purement organisationnel.

## 04 - Stock atelierLevier 2 : Le stock atelier intelligent

Le manque de pièces est le facteur n°1 d'allongement du délai. Il se traite par un stock atelier construit selon les pannes statistiquement les plus fréquentes.

**Méthode pour construire le bon stock :**

**Étape 1 : Analyser les 12 derniers mois.**

Sortir de votre GMAO ou Excel la liste des pièces utilisées en intervention curative sur l'année. Trier par fréquence d'usage et par valeur unitaire. Vous obtenez le top 50 des pièces qui couvrent 80 % de vos pannes.

**Étape 2 : Définir le niveau de stock par catégorie.**

- **Niveau A (top 20 pièces, usage très fréquent)** : stock 5-10 unités au dépôt + 1-2 unités dans chaque camionnette
- **Niveau B (pièces 21-50, usage régulier)** : stock 2-3 unités au dépôt
- **Niveau C (pièces rares, usage exceptionnel)** : pas de stock, commande à la demande

**Étape 3 : Système de réapprovisionnement automatique.**

Seuil minimum par référence dans la GMAO. Quand le stock descend sous le seuil, alerte automatique au responsable achats. Évite la rupture quand un tech utilise la dernière pièce sans le signaler.

**Étape 4 : Stock en camionnette personnalisé.**

Chaque camionnette a une dotation de base (pièces les plus communes) plus une dotation spécifique au secteur du tech (équipements particuliers chez ses clients). Re-stockage hebdomadaire automatique.

**Coût d'investissement pour une PME CVC moyenne : 8 000 à 15 000 € de stock dormant**, qui se rentabilise en 4-8 mois par les déplacements évités et la satisfaction client préservée.

## 05 - Fiche équipementLevier 3 : La fiche équipement enrichie en mobile

Un tech qui arrive sur site avec sur sa tablette **l'historique complet de l'équipement** diagnostique 50 % plus vite qu'un tech qui découvre la machine.

**Ce que la fiche équipement doit contenir, accessible offline :**

- Marque, modèle, année, n° de série, plan d'implantation
- Historique des 5 dernières interventions (date, motif, résolution, pièces utilisées)
- Schémas hydrauliques et frigorifiques si dispo
- Notice constructeur en PDF embarqué
- Contacts utiles : référent technique du site, propriétaire, syndic
- Notes spécifiques du précédent technicien (« attention vanne 3 grippée », « code accès local 1234 »)

Ces infos peuvent diviser par 2 le temps de diagnostic. Sur 100 dépannages annuels, c'est 100h de tech récupérées, soit 6 500 € de coût direct économisé.

**Pour aller plus loin sur la maintenance préventive CVC :**la maintenance curative est le miroir du préventif. Pour structurer toute votre activité maintenance (obligations, planning, contrats, ROI), consultez notre

[guide complet maintenance préventive CVC](https://inter-fast.fr/ressources/blog/articles/blog-guide-maintenance-preventive-cvc).

## 06 - SLALevier 4 : Les SLA contractuels comme outil de pilotage

Beaucoup de PME CVC subissent les attentes client sans les cadrer. C'est ce qui crée les frustrations. La solution : intégrer des **SLA explicites** dans le contrat de maintenance.

**Exemples de SLA réalistes pour une PME CVC :**

| Type d'urgence | Délai d'arrivée | Délai de remise en service | 
|---|---|---|
| Vital (perte totale chauffage hiver, perte totale froid alimentaire) | < 4h jour ouvré, < 8h week-end | < 24h | 
| Urgent (panne impactant le confort, mais pas vital) | < 24h jour ouvré | < 48h | 
| Standard (panne mineure, mode dégradé) | < 72h jour ouvré | < 5 jours | 
| Programmable (équipement secondaire) | RDV sous 5 jours | < 10 jours | 

Ces SLA structurent les attentes des deux côtés. Le client sait à quoi s'attendre. Vous savez ce qui justifie une mobilisation immédiate vs ce qui peut attendre. Vous arbitrez sereinement.

**Conséquences pratiques :**

- Vous tarifez différemment les contrats avec SLA serrés (premium 20-30 %)
- Vous mesurez la conformité SLA mensuellement (KPI clé)
- Vous renégociez les contrats où vous êtes systématiquement hors SLA (soit le SLA est irréaliste, soit le tarif ne couvre pas le service)

Le contrat sans SLA explicite est une bombe à retardement : le client a ses propres attentes en tête (souvent irréalistes), et vous le décevez à chaque panne.

## 07 - ChecklistsLevier 5 : Les checklists et arbres de décision

Pour les pannes récurrentes (compresseur qui ne démarre pas, condenseur en surchauffe, fuite réseau, perte de pression), des **checklists standardisées** permettent à n'importe quel tech de diagnostiquer aussi vite qu'un senior.

**Format type d'une checklist diagnostic :**

1. Vérifier alimentation électrique → si KO : tester disjoncteur, fusibles
2. Vérifier pression circuit → si basse : test étanchéité avant recharge
3. Vérifier paramètres régulation → si dérive : recalibrer
4. Vérifier filtres → si encrassés : nettoyer ou remplacer
5. Si rien ci-dessus : escalade au senior ou retour avec diagnostic approfondi

Ces checklists se construisent à partir de l'expérience accumulée des techs seniors. **C'est le savoir tacite mis en explicite**. Le bénéfice : un tech junior diagnostique en 30 min ce qu'il aurait fait en 1h sans procédure. Sur 50 dépannages/an, c'est 25h économisées par tech, soit 1 600 € de coût direct.

**Intégration dans la GMAO :** les checklists sont disponibles en mobile, le tech les remplit en temps réel pendant l'intervention. Cela alimente aussi automatiquement le rapport et le carnet d'entretien.

### Réduisez votre MTTR avec InterFast

Pré-qualification structurée, fiches équipement offline, stock atelier connecté, checklists mobiles : InterFast outille vos techs pour diviser le délai d'intervention par 2. Démarrez gratuitement ou réservez une démo pour voir la couche curative sur votre cas réel.

[Réserver une démo](https://inter-fast.fr/reserver-demo)

[Essayer gratuitement](https://app.inter-fast.fr/register)

## 08 - KPIsLes KPIs à suivre pour piloter le MTTR

Quatre indicateurs hebdomadaires à mesurer, en plus du MTTR Recover global.

**1. Taux de pannes résolues en 1 passage.** Cible : 80 % minimum. Indicateur direct de la qualité du diagnostic et de la dotation pièces.

**2. Délai médian d'arrivée sur site.** Cible selon SLA : généralement < 4h sur urgences, < 24h sur standard. Le médian est plus pertinent que la moyenne (qui est polluée par les outliers).

**3. Taux de conformité SLA contractuels.** Cible : 95 % minimum. En dessous, soit vous renégociez le SLA, soit vous structurez mieux votre opérationnel.

**4. Coût moyen par dépannage.** Cible : à comparer dans le temps. Si le coût baisse à qualité égale, c'est que les leviers fonctionnent.

Ces 4 chiffres se lisent en 5 minutes par semaine. Si l'un d'eux dérive, vous identifiez la cause (un secteur particulier, un type d'équipement, un tech) et vous corrigez.

## 09 - ConclusionConclusion : le délai, c'est la différence entre garder et perdre un client

Dans le CVC, la maintenance curative est l'épreuve de vérité de votre PME. Le client jugera votre service sur la rapidité de remise en route, pas sur la qualité du préventif passé. Un MTTR Recover qui passe de 12h à 5h est ce qui transforme un client qui hésite en un client qui recommande.

**Trois actions à lancer cette semaine :**

1. **Calculer votre MTTR Recover actuel** sur les 3 derniers mois. Si vous ne savez pas, c'est le premier symptôme. Suivez 10 dernières pannes, mesurez le temps appel → remise en service.
2. **Identifier le top 20 des pièces** consommées en curatif sur les 12 derniers mois. Vérifier si elles sont toutes en stock atelier. Sinon, commander les manquantes cette semaine.
3. **Vérifier vos contrats** : combien explicitent un SLA ? Pour les autres, prévoir une révision lors du prochain renouvellement.

## 10 - QuestionsFAQ

## Quelle différence entre maintenance curative et maintenance corrective ?

## Le MTTR inclut-il le temps de commande de pièces ?

## Comment réduire le MTTR sans investir massivement dans le stock ?

## Faut-il viser le MTTR le plus bas possible ?

## Combien de temps pour structurer la maintenance curative dans une PME CVC ?

**Articles liés :**

#### Sources

1. Mainsim, [Le temps moyen de réparation MTTR : définition, calcul, optimisation](https://fr.mainsim.com/academy/mttr/)
2. GMAO.com, [Optimisation maintenance industrielle : maîtriser le MTTR](https://www.gmao.com/gestion-maintenance/mttr-indicateur-maintenance/)
3. IBM, [What is mean time to repair (MTTR)](https://www.ibm.com/think/topics/mttr)
4. Atlassian, [MTBF, MTTR, MTTA et MTTF (les 4 variantes du MTTR)](https://www.atlassian.com/fr/incident-management/kpis/common-metrics)
5. OTRS, [MTTR : definition, calculation, best practices](https://otrs.com/blog/itsm/mttr/)
6. Mapex, [MTTR in industrial maintenance: what it is and how to reduce it](https://mapex.io/en/news/mttr-what-it-is-and-how-to-reduce-it/)
7. Centreon, [MTTR : KPI clé pour la maintenance et SLA](https://www.centreon.com/glossary/definition-mean-time-to-repair-mttr/)
8. FCMicro, [MTTR : temps moyen de réparation et optimisation PME](https://fcmicro.net/mttr-temps-moyen-reparation/)