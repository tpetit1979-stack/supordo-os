---
url: https://go.sellsy.com/blog/formats-facture-electronique
url_finale: https://go.sellsy.com/blog/formats-facture-electronique
date_collecte: 2026-09-07
destination: site_marketing
---

Facturation Electronique

17/6/2025

- mis à jour le

# Quels sont les formats de la facture électronique ?

### Sommaire

{{video-banner-blog}}

On parle depuis un certain temps de [la facture électronique](https://go.sellsy.com/facturation-electronique-obligatoire) et de son déploiement progressif pour l’ensemble des entreprises. Aujourd’hui, nous allons nous pencher sur un aspect plus technique — mais tout aussi crucial : **les formats de cette facture électronique**. 

Pour garantir son succès, des formats normalisés ont été définis pour permettre l'interopérabilité entre les différents acteurs. Découvrez tout ce que vous devez savoir sur ces formats.

Dans ce guide, nous **répondons à toutes ces questions et vous aidons à réussir votre transition** vers la facturation électronique.

## Pourquoi des formats normalisés ?

La normalisation des formats de facture électronique répond à plusieurs objectifs essentiels :

- Assurer l'**interopérabilité entre les systèmes d'information.**
- Garantir la **conformité réglementaire.**
- Faciliter l'**automatisation des traitements.**
- Permettre le **contrôle fiscal.**

Ces formats standardisés sont indispensables pour les échanges avec les [Plateformes de Dématérialisation Partenaires (PDP)](https://go.sellsy.com/blog/plateforme-dematerialisation-partenaire) et le [Portail Public de Facturation](https://go.sellsy.com/blog/portail-public-de-facturation) (PPF), piliers de la nouvelle architecture de facturation électronique. 

Autrement dit, les formats normalisés ne sont pas un détail technique, mais un prérequis essentiel pour une facturation électronique fiable, conforme et pleinement opérationnelle.

## Trois formats officiels reconnus

Depuis la publication de la norme européenne EN 16931, la France a retenu **trois formats de facturation électronique**. Tous sont conformes à cette norme, mais chacun présente ses spécificités, ses avantages et ses contraintes. Voici une présentation détaillée et comparative.

### Factur-X : le format hybride innovant

Factur-X est l'un des trois formats du "socle minimal" de la réforme rendus obligatoires en réception par toutes les entreprises et toutes les PDP. Ce format hybride combine :

- Un fichier PDF/A-3 lisible par l'humain
- Un fichier XML structuré intégré pour le traitement automatisé

Caractéristiques techniques importantes :

- Format basé sur la norme UN/CEFACT CII D22B (rétrocompatible avec D16B)
- Le document PDF/A-3 doit être conforme même sans les données XML
- Recommandation d'utiliser le niveau 3a pour l'accessibilité des personnes malvoyantes

Factur-X propose plusieurs profils adaptés aux besoins des entreprises :

1. **Profil MINIMUM** :

- Contient les données minimums obligatoires
- Certaines données sont conditionnelles (ex : numéro de TVA intracommunautaire si existant)

1. **Profil BASIC WL (sans lignes)** :

- Inclut tous les champs obligatoires au niveau document
- Intègre les règles de gestion de la norme EN 16931
- Adapté aux entreprises ne pouvant pas gérer le détail des lignes

1. **Profil BASIC** :

- Reprend le profil BASIC WL avec les données essentielles de ligne
- Recommandé pour une automatisation plus poussée

1. **Profil EN 16931** :

- Implémente toutes les données de la norme européenne
- Permet une interopérabilité maximale

1. **Profil EXTENDED** :

- Étend le profil EN 16931 avec des données additionnelles
- Adapté aux besoins spécifiques sectoriels

Déployé depuis 2018 sur [Chorus Pro](https://go.sellsy.com/blog/chorus-pro), Factur-X est déjà adopté par 89 PDP immatriculées provisoirement (au 4 avril 2025). Nouveauté importante : le format peut désormais s'échanger via le réseau d'interopérabilité [PEPPOL](https://go.sellsy.com/blog/peppol) sous gouvernance PEPPOL France.

### UBL : le format international

UBL (Universal Business Language) est un format 100% structuré en XML, particulièrement adapté pour :

- Les échanges internationaux
- L'intégration avec les ERP
- Les volumes importants de factures

**Avantages :**

- Excellente interopérabilité
- Reconnaissance internationale
- Adapté à l'automatisation complète

**Limites :**

- Nécessite des outils de visualisation
- Mise en place plus complexe

### CII : la précision industrielle

Le format CII (Cross Industry Invoice) répond aux besoins des secteurs ayant des exigences spécifiques :

- Santé
- Automobile
- Aéronautique
- Industries réglementées

**Points forts :**

- Structure très détaillée
- Haute personnalisation possible
- Conformité EN 16931

**Limites :**

- Complexité technique
- Adoption plus restreinte

{{rt-banner-1}}

## Le choix du format selon votre activité

Le format à utiliser dépend principalement de votre secteur d'activité et de vos processus métiers :

### Pour les activités commerciales classiques

Factur-X est particulièrement adapté car il permet une transition en douceur vers la facturation électronique tout en maintenant une lisibilité optimale des factures. Il est particulièrement pertinent pour les échanges nationaux et les processus de facturation standards.

### Pour les activités internationales

Le format UBL est recommandé pour les entreprises ayant une forte activité à l'international ou intégrées dans des chaînes logistiques européennes. Il facilite notamment les échanges via le réseau PEPPOL et s'intègre naturellement avec les systèmes internationaux.

### Pour les secteurs industriels spécifiques

Le format CII est privilégié dans les secteurs nécessitant des informations très détaillées comme :

- L'industrie pharmaceutique (traçabilité des lots, dates de péremption)
- L'automobile (références techniques précises)
- L'aéronautique (données de certification)
- Les secteurs soumis à des réglementations particulières

Si vous utilisez un outil de gestion pour l'édition de vos factures, comme Sellsy, celui-ci gèrera automatiquement la compatibilité avec les différents formats requis, vous libérant ainsi de ces considérations techniques.

## Calendrier de mise en place en France

La réforme se déploie selon le calendrier suivant :

- **2025** : Phase pilote pour les entreprises volontaires et les PDP
- **1er septembre 2026** :
  - Obligation de réception pour toutes les entreprises
  - Obligation d'émission pour les grandes entreprises et ETI
- **1er septembre 2027** : Obligation d'émission pour les PME, TPE et microentreprises

À noter : la dernière version de Factur-X (1.07.3) est applicable au 15 mai 2025, intégrant la mise à jour semestrielle de la norme EN16931 sur les listes de codes et les schematrons.