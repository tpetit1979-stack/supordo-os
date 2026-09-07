---
url: https://go.sellsy.com/blog/peppol
url_finale: https://go.sellsy.com/blog/peppol
date_collecte: 2026-09-07
destination: site_marketing
---

Facturation Electronique

11/8/2025

- mis à jour le

# PEPPOL : qu’est-ce que c’est et comment l’utiliser ?

### Sommaire

{{video-banner-blog}}

Depuis plus de quinze ans, Peppol tisse un réseau d’échanges électroniques qui, à l’origine, visait surtout les marchés publics. En 2026, **il s’impose comme l’un des piliers de la réforme française** de la facture électronique. 

Comprendre son fonctionnement et son calendrier n’est pas une obligation, mais **une nécessité stratégique pour toute entreprise** qui veut rester conforme, efficace et compétitive. 

Décryptage complet dans cet article.

## Qu’est-ce que PEPPOL?

Peppol, en bref, est un passeport universel pour vos documents. L’acronyme PEPPOL (Pan-European Public Procurement Online) **est un réseau sécurisé et normalisé qui permet l’échange électronique de documents commerciaux** (factures, bons de commande, avis de livraison, catalogues, etc.) entre entreprises et administrations, en Europe et au-delà. 

Concrètement, il repose sur des « points d’accès » certifiés et un registre d’adressage centralisé ; ainsi, deux organisations peuvent échanger des documents structurés (par exemple au format Factur-X, UBL ou CII) sans se soucier de la compatibilité technique de leurs systèmes respectifs. PEPPOL garantit **l’interopérabilité**, **la traçabilité** et **la sécurité** des échanges, tout en facilitant la conformité aux [obligations de facturation électronique](https://go.sellsy.com/facturation-electronique-obligatoire), notamment dans le cadre des marchés publics et, en France, de la réforme e-invoicing B2B.

Peppol repose sur une architecture fédérée. Concrètement, vous (l’émetteur) envoyez votre facture à un Point d’Accès certifié ; celui-ci la transmet, via le protocole sécurisé AS4, à un autre Point d’Accès, qui la remet au destinataire. Entre les deux, des registres SML/SMP recensent chaque participant : plus besoin de connaître ses préférences techniques, le réseau les gère pour vous.

Résultat : un échange standardisé, traçable et chiffré, quel que soit le pays ou le logiciel comptable utilisé.

## Pourquoi PEPPOL est-il important ?

La Direction Générale Des Finances Publiques (DGFiP), nommée Autorité Peppol nationale en juillet 2025, souhaite harmoniser les flux B2B et B2G autour de normes communes. Pourquoi la France mise-t-elle sur Peppol ? Plusieurs raisons expliquent ce choix :

- **Interopérabilité européenne :** Peppol compte plus de 1,4 million de participants dans près de 100 pays. Pour les groupes exportateurs ou les PME qui travaillent déjà hors frontières, la continuité est immédiate.
- **Sécurité fiscale :** en centralisant la traçabilité, la DGFiP peut mieux lutter contre la fraude et contrôler la TVA dans un environnement dématérialisé.
- **Économie d’échelle :** plutôt que de multiplier les passerelles propriétaires, l’État s’appuie sur une infrastructure éprouvée, déjà compatible avec [Chorus Pro](https://go.sellsy.com/blog/chorus-pro) (obligatoire pour la sphère publique) et les futurs Portails Privés de Facturation (PPF).

## Évolution du système Peppol en France

Depuis plus d’une décennie, la France adopte progressivement Peppol pour sécuriser et standardiser les échanges de factures électroniques. D’abord cantonné aux marchés publics, le réseau est devenu la colonne vertébrale de la réforme B2B. Cette évolution s’est déroulée par étapes : expérimentation européenne, généralisation à Chorus Pro, puis extension aux entreprises privées via le Portail Public de Facturation (PPF) et les plateformes agréées.

Le tableau ci-dessous synthétise les dates clés de 2012 à 2025 et la feuille de route jusqu’aux obligations de 2026-2027.

## Avantages de l’utilisation de Peppol

Adopter Peppol, c’est bénéficier d’un cadre d’échange unique pour toutes vos factures électroniques. Voici pourquoi :

- **Réduction des erreurs et des litiges :** Les champs obligatoires, la validation automatique des identifiants et le transfert sans ressaisie réduisent drastiquement les rejets de factures et les doublons.
- **Accélération des paiements :** Un format standard simplifie la reconnaissance côté acheteur ; combiné à l’automatisation du rapprochement, il accélère les circuits d’approbation et donc la trésorerie.
- **Sécurité et conformité :** Le chiffrement TLS et l’authentification forte protègent contre la fraude au RIB ou au faux fournisseur. L’audit trail Peppol sert de preuve en cas de contrôle fiscal.
- **Vision unifiée :** En connectant vos ventes, achats et dépôts à la DGFiP, vous disposez d’une base de données fiable, exploitable pour la trésorerie, la comptabilité analytique ou la stratégie achats.

## Comment fonctionne le système PEPPOL ?

Le réseau PEPPOL repose sur une architecture dite « quatre-coins » : chaque acteur (émetteur, destinataire) choisit librement son Point d’accès (Access Point). Ces points d’accès, certifiés par OpenPeppol, se chargent d’acheminer les documents entre eux via un protocole sécurisé, sans que les systèmes des entreprises aient besoin d’être connectés directement.

### 1. Découverte automatique des partenaires

- L’entreprise émettrice prépare une facture structurée (Factur-X, UBL 2.1, CII) conforme au Peppol BIS Billing 3.0.
- Elle envoie le document à son Access Point (Coin 1 → Coin 2).
- L’Access Point interroge le Service Metadata Locator (SML), registre mondial qui renvoie l’adresse d’un Service Metadata Publisher (SMP) associé au numéro Peppol du destinataire.
- Le SMP indique quel Access Point (Coin 3) sert le destinataire (Coin 4) et quelles versions de messages il accepte.

### 2. Transmission sécurisée AS4

Une fois l’endpoint découvert, les deux Access Points échangent la facture en AS4 :

- chiffrée et signée via la PKI Peppol ;
- horodatée et journalisée pour l’audit trail.

Cette couche garantit intégrité, authenticité et non-répudiation, répondant ainsi aux exigences du règlement eIDAS et aux règles fiscales françaises.

### 3. Rôle des Peppol Authorities

OpenPeppol délègue la gouvernance locale à des autorités nationales. Depuis le 8 juillet 2025, la DGFiP est Autorité Peppol pour la France :

- elle délivre ou révoque les certificats des Access Points français ;
- définit les conventions d’usage (identifiants SIREN, code pays FR) ;
- aligne Peppol sur le Portail Public de Facturation (PPF).

### 4. Formats de message et règles métier

La spécification BIS Billing 3.0 intègre le modèle EN 16931 et publie ses propres règles (ex. « no more than one note », types de TVA, code devise). Les releases trimestrielles 2025 (Q2) détaillent les validations applicables à chaque champ.

{{rt-banner-1}}

## Comment Peppol s’intègre-t-il à votre système ?

Sur le plan opérationnel, trois briques suffisent :

- ERP ou outil de facturation capable de produire un fichier structuré (Factur-X, UBL, CII).
- Plateforme agréée (PA, anciennement PDP) ou Point d’accès Peppol : elle agit comme votre « hub » de transmission vers le Portail public de facturation (PPF) et vos partenaires commerciaux.
- Processus interne : validation, archivage légal, reporting fiscal.

**À savoir :** [Sellsy](https://go.sellsy.com/) candidat à l’agrément, travaille déjà à l’intégration native de ce triptyque. L’objectif : vous permettre de générer, envoyer et rapprocher vos factures Peppol sans quitter votre interface quotidienne.

## Comment cela vous impacte-t-il si vous facturez depuis la France ?

À partir du 1ᵉʳ septembre 2026, les grandes entreprises et ETI françaises devront émettre et recevoir toutes leurs factures B2B au format électronique structuré, via :

- Le Portail Public de Facturation (PPF), ou
- Une Plateforme Agréée (PA, ex-PDP) connectée à Peppol ou à Chorus Pro.

Douze mois plus tard, la réception électronique deviendra obligatoire pour toutes les sociétés et l’émission pour la plupart des TPE-PME. En pratique, cela signifie :

- Fin du PDF simple : vos ERP ou outils de facturation devront produire Factur-X, UBL ou CII.
- Transmission temps réel à la DGFiP : e-reporting TVA intégré.
- Interopérabilité obligatoire : votre solution devra parler Peppol ou passer par Chorus Pro.

**Quelques Objections fréquentes… et réponses pratiques :**

- « Nous n’exportons pas ; Peppol est-il vraiment utile ? » : Même pour un périmètre 100 % France, Peppol devient incontournable à partir de 2026 : la législation impose de passer par des plateformes agréées raccordées au réseau. Il vaut mieux anticiper que subir.
- « Notre ERP est maison, l’intégration sera trop coûteuse » : Les Points d’Accès Peppol proposent des API standardisées ; le coût de connexion reste bien inférieur à celui d’un EDI propriétaire et la maintenance est assurée par le fournisseur.
- « Peppol ne gère qu’un type de document » : Faux. Au-delà de la facture, le modèle EN 16931 couvre également les commandes, accusés de réception, catalogues, etc. Vous pouvez étendre le périmètre progressivement, selon vos besoins.

**En tant qu’éditeur SaaS français de facturation et CRM, Sellsy prépare :**

- Une passerelle Peppol native pour émettre et recevoir vos factures dématérialisées.
- Une synchronisation en temps réel avec le PPF pour le e-reporting TVA.
- Des tableaux de bord complets afin de suivre conformité, statuts d’envoi et délais de paiement.

L’objectif : rendre Peppol « invisible » pour l’utilisateur. Vous continuez de créer vos factures et bons de commande dans Sellsy ; la transmission structurée, la traçabilité et les obligations fiscales sont gérées en arrière-plan. Ainsi, vous restez concentré sur votre activité tout en respectant, dès aujourd’hui, les exigences de 2026-2027.