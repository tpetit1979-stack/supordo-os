# Cartographie des besoins d'intégration et candidats d'API — SUPORDO (2026)

Document de recherche pour le Product Blueprint SUPORDO (CRM/mini-ERP pour artisans
BTP, verticales de test fumisterie/poêles/cheminées et climatisation/PAC/chauffage ;
build cible Google Antigravity + Supabase).

**Objet** : pour chaque catégorie de besoin d'intégration, lister 2 à 4 candidats
sérieux d'API/services (2026), prioritairement disponibles France/UE, avec leurs
compromis. **Aucun choix de fournisseur n'est fait ici** — l'objectif est de garder
les portes ouvertes (abstraction provider-neutral). Toute affirmation est sourcée par
URL ; les incertitudes sont signalées explicitement plutôt que lissées.

**Méthode** : recherche web menée le 23 septembre 2026, par lots thématiques
(sous-agents dédiés par groupe de catégories, plus un lot dédié en priorité à la
réforme facturation électronique France 2026 — voir §9). Chaque sous-section reprend
les affirmations telles que sourcées par sa recherche d'origine, sans reformulation
qui en altérerait la portée.

**Statut du document** : recherche complète sur les 20 catégories (23 septembre 2026).
Plusieurs points restent signalés « non confirmé » ou « à revérifier » dans le corps du
texte (pages officielles inaccessibles au moment de la recherche, tarifs non extraits,
résidence de données non confirmée) — voir la synthèse en fin de document (§ Notes
méthodologiques générales) avant tout arbitrage contractuel.

---

## Table des matières

1. Adresse / géocodage / cartographie / itinéraires — **fait**
2. Email transactionnel/marketing — **fait**
3. Agenda / calendrier — **fait**
4. SMS / messagerie — **fait**
5. Téléphonie — **fait**
6. Paiement — **fait**
7. Banque / open banking — **fait**
8. Comptabilité / expert-comptable — **fait**
9. Facturation électronique France (réforme 2026) — **fait**
10. Identité entreprise France — **fait**
11. Signature électronique — **fait**
12. Stockage cloud documents/photos — **fait**
13. OCR — **fait**
14. Transcription vocale / speech-to-text — **fait**
15. LLM providers — **fait**
16. Vision/image AI (photos terrain) — **fait**
17. Catalogues fabricants/distributeurs BTP — **fait**
18. Météo — **fait**
19. Notifications push — **fait**
20. Portail client — **fait**

---

## 1. Adresse / géocodage / cartographie / itinéraires

### API Adresse (Base Adresse Nationale) / IGN Géoplateforme

- **Documentation** : ancienne API — [adresse.data.gouv.fr/api-doc/adresse](https://adresse.data.gouv.fr/api-doc/adresse) ; nouvelle API (remplaçante) — [IGN Géoplateforme — géocodage](https://geoservices.ign.fr/documentation/services/services-geoplateforme/geocodage), endpoint `https://data.geopf.fr/geocodage/search`
- **Migration en cours** : l'ancienne API `api-adresse.data.gouv.fr` est dépréciée, maintenue jusqu'à janvier 2026, redirection déjà en place vers l'API IGN Géoplateforme — **migration à anticiper dans l'architecture SUPORDO** ([data.gouv.fr — annonce](https://www.data.gouv.fr/posts/lapi-adresse-de-la-base-adresse-nationale-est-transferee-a-lign-10))
- **Disponibilité France/Europe** : service souverain français, couverture France uniquement (BAN, BD TOPO, PCI).
- **Authentification** : aucune clé requise, accès public direct.
- **Sandbox/test** : non trouvé dans la documentation publique consultée.
- **Webhooks** : absents — mode requête/réponse HTTP uniquement, y compris pour le géocodage par lot CSV.
- **Capacités principales** : géocodage direct/inverse (adresse, lieu, parcelle cadastrale), traitement par lot, autocomplétion, itinéraire, isochrone/isodistance, altitude.
- **Limites principales** : 50 req/s/IP sur le géocodage (429 + blocage 5s au-delà) ; autres services 5-10 req/s — [cartes.gouv.fr — limites d'usage](https://cartes.gouv.fr/aide/fr/guides-utilisateur/utiliser-les-services-de-la-geoplateforme/limites-d-usage/)
- **Prix** : gratuit, service public.
- **RGPD/résidence** : pas de page RGPD dédiée trouvée ; hébergement gouv.fr (France/UE présumé, non documenté explicitement).
- **Licence** : Etalab 2.0 (licence ouverte).
- **Dépendance fournisseur / alternatives** : faible (gratuit, sans clé), mais migration d'URL forcée en cours ; alternatives = Mapbox/Google/HERE en repli, avec perte de la précision cadastrale française.

### Google Maps Platform

- **Documentation** : [Geocoding API overview](https://developers.google.com/maps/documentation/geocoding/overview) ; pricing — [mapsplatform.google.com/pricing](https://mapsplatform.google.com/pricing/) et [détail SKU](https://developers.google.com/maps/billing-and-pricing/pricing)
- **Disponibilité France/Europe** : disponible, « functionality varies by region » sans détail précis France trouvé.
- **Authentification** : clé API.
- **Sandbox/test** : non trouvé.
- **Webhooks** : absents.
- **Capacités principales** : géocodage direct/inverse, Place ID, Directions API, Distance Matrix, Maps JavaScript API, Places Autocomplete.
- **Limites principales** : rate-limit précis non trouvé ; contrôle par facturation/quotas Cloud Console.
- **Prix** ([billing-and-pricing/pricing](https://developers.google.com/maps/billing-and-pricing/pricing)) : plans Starter 100 $/mois (50k appels), Essentials 275 $/mois (100k), Pro 1 200 $/mois (250k), Enterprise sur devis ; crédit d'essai 300 $ ; Geocoding gratuit jusqu'à 10 000 appels/mois puis 5,00 $/1000 dégressif ; Directions similaire ; Maps JS 7,00 $/1000 ; Places Autocomplete 2,83 $/1000.
- **RGPD/résidence** : engagement contractuel RGPD, SCC pour clients EEE, « EEA Terms of Service » dédiés depuis juillet 2025 ([Trust Center GDPR](https://mapsplatform.google.com/resources/trust-center/gdpr/)) ; **aucune résidence géographique dédiée UE confirmée** (société US, risque CLOUD Act non confirmé officiellement).
- **Dépendance fournisseur / alternatives** : fort (écosystème dominant, pricing par SKU modifiable unilatéralement — historique de révisions tarifaires) ; alternatives = Mapbox, HERE, API Adresse (France uniquement).

### Mapbox

- **Documentation** : [Geocoding API docs](https://docs.mapbox.com/api/search/geocoding/) ; pricing — [mapbox.com/pricing](https://www.mapbox.com/pricing)
- **Disponibilité France/Europe** : couverture mondiale, français listé parmi les langues supportées.
- **Authentification** : token d'accès (`access_token`).
- **Sandbox/test** : non trouvé.
- **Webhooks** : absents.
- **Capacités principales** : géocodage direct/inverse, autocomplétion, intersections, batch (jusqu'à 1000 req/appel), 9 « worldviews » régionales, Directions API.
- **Limites principales** : 1000 req/min par défaut (ajustable sur devis, 429 au-delà) ; distinction tarifaire « Temporary » (non stockable) vs « Permanent Geocoding » (stockable, non redistribuable).
- **Prix** ([mapbox.com/pricing](https://www.mapbox.com/pricing)) : Geocoding temporaire — 100 000 req/mois gratuites puis 0,75 $/1000 dégressif ; Geocoding permanent — 5,00 $/1000 puis 4,00 $/1000 (pas de palier gratuit) ; Directions — 100 000 req/mois gratuites puis 2,00 $/1000 dégressif.
- **RGPD/résidence** : certifié EU-US Data Privacy Framework + SCC 2021 ; **données source hébergées sur AWS aux États-Unis** (mise en cache CDN globale pour performance uniquement, pas de résidence UE garantie) ; option « Atlas » on-premise pour contrôle strict de localisation — [Legal FAQ](https://www.mapbox.com/legal/legal-faq)
- **Dépendance fournisseur / alternatives** : modéré (tarif « permanent » 6-10x plus cher si stockage des résultats) ; alternatives = Google, HERE, API Adresse.

### HERE (Geocoding & Search, Routing)

- **Documentation** : [Introduction to HERE Geocoding & Search API v7](https://docs.here.com/geocoding-and-search/docs/introduction-to-here-geocoding-search-api-v7) ; auth — [Get credentials](https://docs.here.com/geocoding-and-search/docs/get-credentials-ols.md)
- **Disponibilité France/Europe** : couverture mondiale annoncée ; société d'origine néerlandaise (ex-Nokia, consortium auto germano-japonais) mais pas de garantie de résidence UE (voir RGPD).
- **Authentification** : clé API ou OAuth2 (client credentials).
- **Sandbox/test** : non trouvé.
- **Webhooks** : absents.
- **Capacités principales** : geocode, reverse/multi-reverse geocode (batch), autocomplete, autosuggest, discover, browse, lookup by ID, Routing API séparée.
- **Limites principales** : rate-limit précis non trouvé.
- **Prix** : **page de pricing officielle non accessible** (404 / contenu générique lors de la consultation) — chiffres tiers non officiels non retenus ; à vérifier directement auprès de HERE.
- **RGPD/résidence** : reconnaît les droits RGPD, SCC + UK IDTA pour transferts ; **déclaration explicite que les données peuvent être transférées hors UE/EEE/UK, y compris vers les États-Unis** — [Privacy Policy](https://legal.here.com/en-gb/privacy)
- **Dépendance fournisseur / alternatives** : écosystème moins répandu (moins d'effet réseau/support communautaire) ; alternatives = Google, Mapbox, API Adresse.

**Points à vérifier avant décision** : pricing HERE chiffré officiel, rate limits précis Google/HERE, résidence géographique précise Google Maps Platform, disponibilité sandbox pour les 4 candidats (aucun confirmé).

---

## 2. Email transactionnel/marketing

*Note méthodologique : la page pricing officielle Brevo (`brevo.com/pricing/`) est rendue en JavaScript côté client et n'a pas pu être extraite en texte brut ; les chiffres Brevo proviennent de sources secondaires convergentes, signalés comme tels.*

### Brevo (ex-Sendinblue)

- **Documentation** : [developers.brevo.com/docs](https://developers.brevo.com/docs)
- **Disponibilité France/Europe** : société française (Paris) ; hébergement exclusivement UE — OVH (France, Allemagne) + Google Cloud (Belgique), réplication sur ≥2 zones ; ISO 27001:2022 (source secondaire résumant une page officielle non accessible en direct — HTTP 403).
- **Authentification** : clé API (header `api-key`) ; mention OAuth 2.0 dans une page connexe, usage précis non détaillé.
- **Sandbox/test** : non trouvé dans la documentation consultée.
- **Webhooks** : oui — sent/delivered/hardBounce/softBounce/blocked/spam/invalid/deferred/click/opened/unsubscribed ; max 40 webhooks/compte — [transactional-webhooks](https://developers.brevo.com/docs/transactional-webhooks)
- **Capacités principales** : API unifiée email + SMS + WhatsApp, campagnes, contacts, automation, tracking d'événements, sync e-commerce.
- **Limites principales** : envoi email 3 600 000 req/h / 1000 req/s ; SMS 540 000 req/h / 150 req/s ; contacts 36 000 req/h / 10 req/s ; autres endpoints 100 req/h — [api-limits](https://developers.brevo.com/docs/api-limits)
- **Prix** (source secondaire, non vérifiée officiellement) : gratuit 300 emails/jour, jusqu'à 100k contacts stockés ; Starter dès 9 $/mois (5000 emails), paliers 19 $/29 $/69 $ ; depuis octobre 2025 le volume acheté plafonne aussi les contacts stockables.
- **RGPD/résidence** : traitement/stockage entièrement UE selon pages officielles (non intégralement récupérables — 403), évite le recours aux SCC transatlantiques.
- **Dépendance fournisseur / alternatives** : API propriétaire REST ; alternative de profil équivalent = Mailjet.

### Mailjet

- **Documentation** : [dev.mailjet.com](https://dev.mailjet.com/)
- **Disponibilité France/Europe** : société fondée à Paris, filiale du groupe Sinch ; données hébergées exclusivement UE (Francfort + Saint-Ghislain, Google Cloud, 6 data centers/2 régions) ; 1ère ESP certifiée ISO 27001 (2017), certification AFAQ/AFNOR RGPD — [data-security-and-privacy](https://www.mailjet.com/products/data-security-and-privacy/)
- **Authentification** : Basic Auth (clé publique/secrète) pour l'API, + relais SMTP dédié ; rotation clé secrète recommandée tous les 90 jours.
- **Sandbox/test** : oui — `SandboxMode` dans le payload Send API v3.1 (valide sans délivrer) — [sandbox.mode](https://dev.mailjet.com/docs/email-api/send-api-v31/sandbox.mode)
- **Webhooks** : oui — open/click/bounce/spam/blocked/unsub/sent, applicable transactionnel + marketing.
- **Capacités principales** : Email API + SMTP + Parse API (réception entrante), templates drag-and-drop, automation, A/B testing, segmentation, générateur IA.
- **Limites principales** : plan gratuit 200 emails/jour (~6000/mois), 1000 contacts ; file d'attente 3 jours puis suppression au-delà du plafond quotidien ; crédits non reportables.
- **Prix** ([mailjet.com/pricing](https://www.mailjet.com/pricing/), vérifiée) : Free 0 $ (6000/mois, 1000 contacts) ; Starter 9 $/mois (8000 emails, 2000 contacts) ; Essential 19 $/mois (15 000 emails, contacts illimités) ; Premium 29 $/mois ; Custom sur devis ; -10 % en paiement annuel.
- **RGPD/résidence** : conforme RGPD, DPA fourni, outils DSAR, hébergement 100 % UE documenté.
- **Dépendance fournisseur / alternatives** : API propriétaire + option SMTP standard (réduit le lock-in pour l'envoi pur) ; alternative = Brevo.

### SendGrid (Twilio SendGrid)

- **Documentation** : [twilio.com/docs/sendgrid](https://www.twilio.com/docs/sendgrid)
- **Disponibilité France/Europe** : société américaine (groupe Twilio) ; option payante « Data Residency » pour stocker/traiter en UE, réservée aux offres Pro/Premier, nécessite un « EU subuser » + endpoint dédié — [data-residency](https://www.twilio.com/docs/sendgrid/data-residency)
- **Authentification** : clé API (Bearer token).
- **Sandbox/test** : oui — « Sandbox Mode » dans `mail_settings`, valide sans délivrer, pas de crédits consommés — [sandbox-mode](https://www.twilio.com/docs/sendgrid/for-developers/sending-email/sandbox-mode)
- **Webhooks** : oui — bounce/click/deferred/delivered/dropped/group_resubscribe/group_unsubscribe/open/processed/spam report/unsubscribe.
- **Capacités principales** : Email API transactionnel séparé du produit « Marketing Campaigns » (pricing distinct), templates dynamiques, validation d'adresses, sous-comptes, analytics.
- **Limites principales** : essai gratuit 100 emails/jour pendant 60 jours (plus de plan gratuit permanent) ; dépassement 0,0005-0,0013 $/email.
- **Prix** ([email-api/pricing](https://www.twilio.com/en-us/products/email-api/pricing), vérifiée) : Essentials dès 19,95 $/mois (50k-100k emails) ; Pro dès 89,95 $/mois (100k-2,5M emails, IP dédiée) ; Premier sur devis (5M+ emails).
- **RGPD/résidence** : participe au Data Privacy Framework UE-US ; résidence UE = fonctionnalité payante réservée Pro/Premier, non incluse par défaut.
- **Dépendance fournisseur / alternatives** : fort (écosystème Twilio large) ; lock-in juridictionnel notable pour usage UE strict ; alternatives = Brevo, Mailjet (UE native sans surcoût).

### Postmark

- **Documentation** : [postmarkapp.com/developer/api/overview](https://postmarkapp.com/developer/api/overview)
- **Disponibilité France/Europe** : société américaine (ActiveCampaign) ; serveurs aux États-Unis (Deft/Chicago + AWS) ; **pas d'hébergement UE**, s'appuie sur SCC/DPA plutôt que résidence physique — [eu-privacy](https://postmarkapp.com/eu-privacy)
- **Authentification** : Server API Token (header `X-Postmark-Server-Token`), max 3 tokens/serveur.
- **Sandbox/test** : oui, natif — « Sandbox Server » dédié, messages livrés en « black hole » mais apparaissant « Delivered » dans l'UI/webhooks/API — [sandbox-mode](https://postmarkapp.com/developer/user-guide/sandbox-mode)
- **Webhooks** : 8 types — Bounce, Delivery, Open, Click, Spam Complaint, Subscription Change, Inbound, SMTP API Error.
- **Capacités principales** : transactionnel centré avec « Message Streams » (isolation transactionnel/broadcast pour protéger la réputation IP) ; batch jusqu'à 500 messages/requête ; broadcast simple mais pas d'éditeur WYSIWYG de campagne ni segmentation avancée.
- **Limites principales** : plan Free permanent 100 emails/mois sans dépassement payant possible à ce palier ; rétention 45 jours par défaut (7/28 jours via add-on, non revérifié officiellement).
- **Prix** ([postmarkapp.com/pricing](https://postmarkapp.com/pricing), vérifiée) : Free 0 $ (100/mois) ; Basic 15 $/mois, Pro 16,50 $/mois, Platform 18 $/mois (tous 10 000 emails inclus) ; dépassement 1,20-1,80 $/1000 selon plan.
- **RGPD/résidence** : DPA + SCC, **sans résidence UE** — point de vigilance si exigence stricte de résidence UE.
- **Dépendance fournisseur / alternatives** : architecture « Message Streams » simple à répliquer ; le vrai facteur de lock-in est l'absence d'option UE native ; alternative = Mailjet.

**Synthèse** : résidence UE native sans surcoût = Brevo/Mailjet ; SendGrid = résidence UE payante (Pro/Premier) ; Postmark = aucune résidence UE. Sandbox confirmé pour Mailjet/SendGrid/Postmark, non trouvé pour Brevo. Ampleur marketing complète = Brevo/Mailjet ; Postmark reste délibérément transactionnel-only.

---

## 3. Agenda / calendrier

### Google Calendar API

- **Documentation** : [Calendar API — Overview](https://developers.google.com/workspace/calendar/api/guides/overview)
- **Disponibilité France/Europe** : accessible sans restriction géographique documentée ; pas de mention de résidence des données spécifique à l'API Calendar trouvée.
- **Authentification** : OAuth 2.0, 18 scopes (de `calendar` complet à `calendar.freebusy` ou `calendar.settings.readonly`) — [auth](https://developers.google.com/workspace/calendar/api/auth)
- **Sandbox/test** : pas de sandbox dédié trouvé (mode « Testing » de l'écran de consentement OAuth, pas spécifique à Calendar).
- **Webhooks** : oui, « push notifications » — channel `web_hook`, HTTPS + certificat SSL valide obligatoire, ressources observables limitées (ACL, CalendarList, Events, Settings), fiabilité non garantie à 100 %, abonnement par calendrier avec expiration/renouvellement — [push](https://developers.google.com/workspace/calendar/api/guides/push)
- **Capacités principales** : CRUD événements (incl. récurrents), freebusy, synchronisation incrémentale, ACL/partage, paramètres de calendrier.
- **Limites principales** : 10 000 req/min/projet, 600 req/min/utilisateur/projet, 1 000 000 req/jour/projet avant facturation — [quota](https://developers.google.com/workspace/calendar/api/guides/quota)
- **Prix** : gratuit pour un usage standard ; passage payant en cas de dépassement prévu courant 2026, préavis ≥90 jours (même page quota).
- **RGPD/résidence** : pas de mention spécifique Calendar API ; au niveau Google Cloud général, engagements de résidence par région ([data-residency](https://cloud.google.com/terms/data-residency)) et SCC/DPA Workspace ([privacy/gdpr](https://cloud.google.com/privacy/gdpr)) — non confirmé si Calendar figure dans le périmètre couvert.
- **Dépendance fournisseur / alternatives** : fort (scopes/quotas/OAuth propriétaires) ; l'accès CalDAV de Google existe mais exige lui-même OAuth2 exclusif (Basic Auth refusée) — peu utile comme voie de portabilité réelle.

### Microsoft Graph / Outlook Calendar API

- **Documentation** : [calendar resource type](https://learn.microsoft.com/en-us/graph/api/resources/calendar?view=graph-rest-1.0)
- **Disponibilité France/Europe** : programme **EU Data Boundary** couvrant Microsoft 365 (donc Outlook/Calendar) — stockage/traitement dans l'UE/AELE avec exceptions limitées documentées — [eu-data-boundary-learn](https://learn.microsoft.com/en-us/privacy/eudb/eu-data-boundary-learn)
- **Authentification** : OAuth 2.0 (Microsoft identity platform), mode délégué ou application seule ; scopes `Calendars.Read/.ReadBasic/.ReadWrite[.Shared/.All]` — [permissions-reference](https://learn.microsoft.com/en-us/graph/permissions-reference)
- **Sandbox/test** : oui — Microsoft 365 Developer Program, tenant sandbox gratuit type E5 (25 licences), préconfiguré Graph/Teams/SharePoint/Outlook, actif tant que le compte l'est — [dev-program-faq](https://learn.microsoft.com/en-us/office/developer-program/microsoft-365-developer-program-faq)
- **Webhooks** : oui — API subscriptions, endpoint HTTPS public, validation par jeton, réponse sous 3s, retries jusqu'à 4h ; durée max d'abonnement Outlook `event` = 10 080 min (7 jours), réduite à 1 440 min si « rich notifications » ; latence `calendar` moyenne &lt;1min/max 3min — [change-notifications-delivery-webhooks](https://learn.microsoft.com/en-us/graph/change-notifications-delivery-webhooks)
- **Capacités principales** : CRUD événements/calendriers, `calendarView`, freebusy (`getSchedule`), suggestion de créneaux (`findMeetingTimes`), propriétés étendues, permissions de calendrier partagé.
- **Limites principales** : 130 000 req/10s par app tous tenants confondus — [throttling-limits](https://learn.microsoft.com/en-us/graph/throttling-limits) ; pas de chiffre spécifique Calendar trouvé.
- **Prix** : pas de page pricing dédiée à Graph ; inclus dans l'usage Entra ID/Microsoft 365, pas de coût par appel documenté séparément.
- **RGPD/résidence** : couvert par l'EU Data Boundary (voir ci-dessus).
- **Dépendance fournisseur / alternatives** : fort (Entra ID/365, consentement admin pour permissions étendues) ; EWS legacy en dépréciation ; connecteurs CalDAV tiers possibles mais non documentés officiellement.

### CalDAV (protocole ouvert, RFC 4791)

Pas un fournisseur mais un **standard IETF** implémenté par Apple iCloud, Nextcloud (auto-hébergé), Fastmail, et un accès (contraint) chez Google.

- **Documentation** : [RFC 4791](https://www.rfc-editor.org/rfc/rfc4791)
- **Disponibilité France/Europe** : indépendante du protocole, dépend de l'implémentation choisie.
- **Authentification** : **non standardisée en pratique** malgré le protocole commun — Nextcloud : Basic Auth + mot de passe d'application ; Fastmail : Basic Auth + mot de passe d'application obligatoire (serveur `caldav.fastmail.com`) ; Google : OAuth2 exclusif (Basic Auth refusée, 401) ; Apple : documentation technique officielle non localisée dans le temps imparti.
- **Sandbox/test** : non applicable au protocole ; dépend du fournisseur (Nextcloud auto-hébergé = sandbox de facto).
- **Webhooks** : **absents nativement du protocole** — synchronisation par polling (`REPORT`/`sync-collection`) ou extensions propriétaires non normalisées ; limite structurelle face à Google/Microsoft.
- **Capacités principales** (RFC 4791) : lecture filtrée (`calendar-query`), récupération partielle, création par `PUT`, événements récurrents/exceptions, gestion participants, requêtes free/busy, exigence WebDAV ACL.
- **Limites principales** : aucune définie par le protocole, dépend entièrement du serveur.
- **Prix** : protocole libre/gratuit ; coût = hébergeur choisi (Nextcloud = infra uniquement ; Fastmail/Apple = grilles non vérifiées dans cette recherche).
- **RGPD/résidence** : dépend intégralement du fournisseur — Nextcloud auto-hébergé permet une souveraineté totale (hébergement au choix France/UE) ; Fastmail annonce des serveurs régionaux (« data residency ») sans détail vérifié ; Apple non documenté ici.
- **Dépendance fournisseur / alternatives** : **c'est sa valeur structurelle** — standard multi-implémentations, élimine le lock-in d'API propriétaire, mais reporte la charge d'abstraction (auth hétérogène, pas de push) sur l'intégration SUPORDO.

**Synthèse** : Google/Microsoft offrent OAuth2 documenté, freebusy natif, webhooks, quotas chiffrés, sandbox dev — au prix d'un couplage fort à leur écosystème. CalDAV élimine ce couplage par nature de standard ouvert, mais sans push natif ni authentification homogène entre fournisseurs.

---

## 4. SMS / messagerie

### Twilio (Programmable Messaging / SMS)

- **Documentation** : [twilio.com/docs/sms](https://www.twilio.com/docs/sms) ; règles France — [twilio.com/en-us/guidelines/fr/sms](https://www.twilio.com/en-us/guidelines/fr/sms)
- **Disponibilité France/Europe** : expéditeur alphanumérique **obligatoire pour le trafic A2P en France** (max 11 caractères, sans caractères spéciaux) ; trafic marketing autorisé uniquement 08h00-21h30 heure française, lun-sam (transactionnel exempté) ; opt-in explicite requis, opt-out par lien web uniquement (pas de numéro de téléphone).
- **Authentification** : Basic Auth (Account SID + Auth Token) ou API Key SID/Secret.
- **Sandbox/test** : pas de sandbox SMS dédié confirmé (test credentials documentés surtout pour Voice/WhatsApp).
- **Webhooks** : oui — webhook SMS entrant (réponse TwiML) + Status Callback sortant (queued→sent→delivered/failed) — [messaging-webhooks](https://www.twilio.com/docs/usage/webhooks/messaging-webhooks)
- **Capacités principales** : SMS, MMS, RCS, WhatsApp, Messenger (bêta).
- **Limites principales** : expéditeur alphanumérique réservé comptes payants, usage one-way uniquement (pas de réponse possible) ; rate limits précis non trouvés.
- **Prix** ([sms/pricing/fr](https://www.twilio.com/en-us/sms/pricing/fr), vérifiée) : sortant 0,0798 $/message, entrant 0,0075 $/message, alphanumérique gratuit à l'usage, frais d'échec 0,001 $/message (USD, hors frais opérateur).
- **RGPD/résidence** : installations principales aux États-Unis, BCR + Data Privacy Framework UE-US, siège européen Dublin ; **pas de résidence UE garantie** pour le traitement principal.
- **Dépendance fournisseur / alternatives** : API REST propriétaire ; alternatives = Vonage, OVHcloud, Brevo, tout agrégateur SMPP.

### Vonage (SMS API / Messages API)

- **Documentation** : [developer.vonage.com/en/messaging/sms/overview](https://developer.vonage.com/en/messaging/sms/overview)
- **Disponibilité France/Europe** : expéditeur alphanumérique supporté globalement (max 11 car.) ; page spécifique restrictions France retournée en HTTP 403 au fetch — **non confirmé directement**, à revérifier manuellement.
- **Authentification** : API Key + Secret (Basic Auth).
- **Sandbox/test** : Messages API Sandbox existe mais couvre WhatsApp/Viber/Messenger/Instagram — **le SMS pur n'y est pas listé** ([messages-api-sandbox](https://developer.vonage.com/en/messages/concepts/messages-api-sandbox)), gratuit, 100 messages/mois, 1 msg/s.
- **Webhooks** : oui — SMS entrant + Delivery Receipts (accepted/delivered/buffered/expired/failed/rejected/unknown).
- **Capacités principales** : SMS sortant/entrant haut volume, SMPP entreprise, auto-redact, Unicode ; MMS non confirmé pour la SMS API classique.
- **Limites principales** : non trouvées précisément ; obligations 10DLC spécifiques aux États-Unis (non applicables en France).
- **Prix** : pas de prix public en clair — distribué via CSV téléchargeable depuis un dashboard authentifié ([dashboard/control/pricing](https://developer.vonage.com/en/dashboard/control/pricing)) — **non trouvé dans la documentation publique consultée**.
- **RGPD/résidence** : conformité RGPD revendiquée, SCC, « EU and Germany Regional Multi-tenancy Zone » avec masquage IP mentionnée mais contenu cible non récupéré directement — à vérifier.
- **Dépendance fournisseur / alternatives** : API propriétaire + option SMPP (réduit le lock-in gros volume) ; alternatives = Twilio, OVHcloud, Brevo.

### OVHcloud SMS

- **Documentation** : [docs.ovhcloud.com — SMS](https://docs.ovhcloud.com/en/guides/web-cloud/messaging/sms/landing-page-sms)
- **Disponibilité France/Europe** : périmètre **explicitement limité** — « France, the United Kingdom, Ireland, Spain, Italy and Poland » ; expéditeur alphanumérique max 11 caractères, validation ~72h avec justificatif.
- **Authentification** : clés API OVHcloud (Application Key + Secret + Consumer Key), ou http2sms/email2sms simplifiés.
- **Sandbox/test** : pas de sandbox confirmé officiellement ; système de crédits prépayés sans essai gratuit documenté officiellement (mention de « 20 crédits offerts » trouvée en recherche web mais non confirmée par fetch direct).
- **Webhooks** : oui — callback `PUT /sms/{serviceName}` + pull `GET /sms/{serviceName}/incoming` ; **réception SMS entrant disponible en France uniquement**, pas dans les 5 autres pays couverts.
- **Capacités principales** : SMS sortant unitaire/masse, entrant/conversationnel « Time2Chat » (France uniquement), campagnes, listes, SMPP haut volume ; MMS non mentionné.
- **Limites principales** : couverture 6 pays seulement, réception entrante France uniquement, RGPD explicitement à la charge du client (opt-in, registre de consentement).
- **Prix** : page [ovhcloud.com/fr/sms/prices](https://www.ovhcloud.com/fr/sms/prices/) existe, système de crédits avec remises jusqu'à 23 % selon volume évoqué en recherche web, mais **tableau chiffré exact non extrait** lors du fetch — à consulter directement.
- **RGPD/résidence** : entreprise française/européenne, mais **aucune déclaration explicite de résidence des données pour le service SMS spécifiquement** trouvée.
- **Dépendance fournisseur / alternatives** : API propriétaire + SMPP standard ; couverture pays plus restreinte = facteur de dépendance si expansion hors des 6 pays ; alternatives = Twilio, Vonage, Brevo.

### Brevo SMS

- **Documentation** : [developers.brevo.com](https://developers.brevo.com/), [transactional-sms-endpoints](https://developers.brevo.com/docs/transactional-sms-endpoints)
- **Disponibilité France/Europe** : entreprise française ; page pays/pricing renvoyée en HTTP 403 au fetch — non confirmé directement.
- **Authentification** : clé API (header `api-key`) ou OAuth 2.0.
- **Sandbox/test** : **aucun trouvé** dans les pages officielles consultées (contredit une mention tierce non officielle).
- **Webhooks** : oui — `webUrl` à l'envoi, événements sent/delivered/bounced/blocked/unsubscribed/replied/accepted/rejected, également via `/transactionalSMS/statistics/events`.
- **Capacités principales** : SMS transactionnel + marketing confirmés ; **SMS entrant non documenté** (probable absence) ; WhatsApp disponible en canal séparé.
- **Limites principales** : rate limits évoqués sans valeurs chiffrées trouvées ; pas de réception SMS entrante apparente.
- **Prix** : page dédiée non récupérable (403) ; chiffre tiers non vérifié directement évoqué (« 100 crédits France ≈ 4,5 € ») — **à confirmer avant usage décisionnel**.
- **RGPD/résidence** : société française, page privacy identifiée mais contenu non récupérable en fetch — non confirmé directement dans cette recherche.
- **Dépendance fournisseur / alternatives** : API propriétaire intégrée à une plateforme CRM plus large (email+SMS+WhatsApp) — avantage guichet unique mais aussi lock-in fonctionnel si SUPORDO n'a besoin que du SMS.

**Synthèse** : couverture mondiale = Twilio/Vonage ; couverture restreinte (6 pays dont France) = OVHcloud. SMS entrant confirmé chez Twilio/Vonage/OVHcloud (France uniquement pour ce dernier), non confirmé chez Brevo. Ancrage français/UE = OVHcloud et Brevo (mais RGPD/pricing SMS non pleinement vérifiables sur leurs pages, plusieurs en 403). Seul Twilio a un prix exact et sourcé pour la France.

---

## 5. Téléphonie

### Twilio Voice (Programmable Voice)

- **Documentation** : [twilio.com/docs/voice](https://www.twilio.com/docs/voice)
- **Disponibilité France/Europe** : numéros français disponibles à l'achat ; siège EEA Dublin, région infra Ireland (IE1) ; résidence UE **documentée pour SMS** mais **non confirmée pour Voice** spécifiquement — [sms-eu-data-residency](https://www.twilio.com/docs/global-infrastructure/sms-eu-data-residency)
- **Authentification** : Account SID + Auth Token (Basic Auth), rotation possible, ou API Keys.
- **Sandbox/test** : oui — test credentials, « magic numbers » simulant succès/échec/numéro invalide, sans frais ni appel réel, incompatible CLI — [test-credentials](https://www.twilio.com/docs/iam/test-credentials)
- **Webhooks** : oui — webhook appel entrant, `StatusCallbackEvent` (initiated/ringing/answered/completed), callback enregistrement (in-progress/completed/absent/failed).
- **Capacités principales** : appels entrants/sortants programmables, IVR/DTMF, enregistrement + transcription, routage avancé ; pas de connecteur CRM natif documenté.
- **Limites principales** : rate limits API non retrouvés (page dédiée en 404 au moment du contrôle).
- **Prix** ([voice/pricing/fr](https://www.twilio.com/en-us/voice/pricing/fr)) : sortant fixe France ≈ 0,0187 $/min, mobile France (EEA) ≈ 0,0404 $/min, mobile France hors EEA ≈ 0,1603 $/min, réception ≈ 0,0100 $/min + 1,35 $/mois location numéro, SIP/navigateur ≈ 0,0040 $/min (à revérifier via la Pricing API pour un chiffre certifié).
- **RGPD/résidence** : DPA, SCC UE/UK, BCR, ISO 27001, siège EEA Dublin ; résidence UE confirmée SMS uniquement.
- **Dépendance fournisseur / alternatives** : fort si TwiML utilisé directement dans le code métier (recommandation : interface interne « Téléphonie » abstraite) ; alternatives = Vonage, Aircall, Ringover.

### Aircall

- **Documentation** : [developer.aircall.io](https://developer.aircall.io/)
- **Disponibilité France/Europe** : entreprise **française** (Paris), DPO enregistré CNIL, numéros français nativement supportés.
- **Authentification** : OAuth (multi-comptes/Marketplace) ou Basic Auth + clé API (mono-compte).
- **Sandbox/test** : **pas d'environnement sandbox dédié** — tests dans le compte de production via utilisateurs/numéros « TEST », avertissement officiel d'impact possible sur la facturation — [Aircall Sandbox](https://support.aircall.io/hc/en-gb/articles/23108614387485-Aircall-Sandbox)
- **Webhooks** : riches — `call.created/answered/hungup/ended/comm_assets_generated/transferred/tagged` + événements IA (transcription, résumé, add-on payant).
- **Capacités principales** : click-to-call sortant, gestion entrant, IVR/distribution, pause/suppression enregistrement, messagerie vocale, API Contacts pour sync CRM.
- **Limites principales** : 120 req/min/entreprise (en-têtes `X-AircallApi-*`) ; pagination 20/défaut (max 50) ; **plafond dur 10 000 éléments** récupérables.
- **Prix** ([aircall.io/pricing](https://aircall.io/pricing/)) : Essentials 30 $/licence/mois, Professional 50 $/licence/mois (min. 3 licences), Custom/Enterprise sur devis (min. 25 users) ; numéro additionnel 6 $/mois ; **aucun tarif à la minute France trouvé** (modèle par licence, pas consommation).
- **RGPD/résidence** : SCC UE + mesures EDPB 1/2020, obligations de conservation de métadonnées d'appel imposées par le droit télécom européen même après suppression demandée.
- **Dépendance fournisseur / alternatives** : couche produit orientée CTI/CRM (webhooks propriétaires `call.*` à isoler) ; alternatives = Ringover (français), Twilio Voice, Vonage.

### Vonage Voice API

- **Documentation** : [developer.vonage.com/en/voice/voice-api/overview](https://developer.vonage.com/en/voice/voice-api/overview)
- **Disponibilité France/Europe** : couverture mondiale revendiquée ; **disponibilité de numéros français non confirmée** (plusieurs pages pricing/couverture en 403 au fetch) — à vérifier manuellement.
- **Authentification** : API key+secret (Base64) ou JWT (Application ID + clé privée).
- **Sandbox/test** : « Voice Playground » référencé, nature exacte non détaillée davantage.
- **Webhooks** : oui — started/ringing/answered/completed/disconnected, échecs busy/cancelled/unanswered/rejected/failed/timeout, record/input/transfer, détection répondeur.
- **Capacités principales** : notifications vocales sortantes + TTS (50+ langues), IVR/bots vocaux, SDK iOS/Android/Web, speech-to-text, WebSockets audio temps réel.
- **Limites principales** : non trouvées (pages bloquées en 403).
- **Prix** : page dédiée **inaccessible (403)** ; un chiffre tiers (0,414 €, non standard) évoqué mais **non confirmé directement** — ne pas retenir sans revérification.
- **RGPD/résidence** : pages Trust Center/privacy inaccessibles lors de cette recherche (403/DNS) — **non trouvé**, à revérifier manuellement.
- **Dépendance fournisseur / alternatives** : API bas niveau comparable à Twilio (NCCO ~ TwiML) ; alternatives = Twilio Voice, Ringover, Aircall.

### Ringover

- **Documentation** : [developer.ringover.com](https://developer.ringover.com/)
- **Disponibilité France/Europe** : solution française ; confirmation forte — « l'ensemble des data centers [...] sont hébergés et localisés en France, n'engendrant [...] aucun transfert de données en dehors de l'Union Européenne » — [ringover.fr/rgpd](https://www.ringover.fr/rgpd)
- **Authentification** : clé API générée depuis Dashboard &gt; Developer.
- **Sandbox/test** : pas de « sandbox » nommé, mais environnements **Test et Production distincts** documentés avec credentials séparés.
- **Webhooks** : oui — appels entrants, appels manqués, appels répondus, messages vocaux (transcription), durée d'appel.
- **Capacités principales** : API REST appels/contacts/utilisateurs/IVR/SMS, API Webhook, API Analytics.
- **Limites principales** : rate limits non trouvés dans la documentation consultée.
- **Prix** ([ringover.com/pricing](https://www.ringover.com/pricing)) : TALK 15 $/user/mois (appels nationaux illimités), BUSINESS 47 $/user/mois, ADVANCED sur devis ; add-on IA Voice Agent dès 0,19 $/min ; rattachement de l'accès API à un palier précis **non confirmé** ; pas de tarif à la minute standard trouvé (abonnement avec appels nationaux inclus).
- **RGPD/résidence** : hébergement 100 % France/UE confirmé, DPO désigné, DPA disponibles, certifications HDS/ISO 27001:2013/ISO 9001-14001-50001, chiffrement DTLS-SRTP.
- **Dépendance fournisseur / alternatives** : acteur français plus modeste que Twilio/Vonage, documentation/SLA publics moins matures ; alternatives = Aircall, Twilio Voice, Vonage.

**Note — OVHcloud Telecom (écarté après vérification)** : API OVHcloud `/telephony` vérifiée directement (`api.eu.ovhcloud.com/1.0/telephony.json`) — expose la gestion de lignes/SIP trunk/DDI/conférence/easy hunting, mais **aucun endpoint click-to-call, aucun webhook d'événements d'appel, aucune gestion d'enregistrement** — pas fonctionnellement comparable à Twilio/Vonage/Aircall/Ringover pour un usage CTI/IVR programmable, écarté après vérification (pas par supposition).

**Synthèse** : Twilio/Vonage = API bas niveau, tarification à la minute, hébergement hors UE par défaut (résidence UE confirmée SMS chez Twilio, non pour Voice ; non documentée chez Vonage dans cette recherche). Aircall/Ringover = solutions françaises CTI clé-en-main, webhooks riches, hébergement France/UE documenté, mais modèle par abonnement/licence (pas à la minute) et couche API plus haut niveau (donc lock-in fonctionnel sur leur modèle d'objets).

### Points de vigilance transverses catégories 1-5 (non résolus après recherche raisonnable)

- **Sandbox** : absent ou non confirmé pour la quasi-totalité des candidats API bas niveau (API Adresse, Google Maps, Mapbox, HERE, Brevo email et SMS, Vonage SMS/Voice, Google Calendar, Aircall) — présent et documenté surtout chez Mailjet, SendGrid, Postmark, Twilio (Voice/SMS via test credentials), Microsoft 365 Dev Program, Ringover (environnements Test/Prod).
- **Plusieurs pages officielles inaccessibles au moment de la recherche** (HTTP 403 ou contenu JS non extrait) : pricing HERE, pricing/RGPD Vonage (SMS et Voice), pricing/RGPD Brevo (email et SMS), certaines pages Aircall/Fastmail — à revérifier manuellement avant toute décision engageante.
- **Résidence des données UE** : garantie explicite et documentée seulement pour un sous-ensemble (Mailjet, Brevo email — sources partiellement secondaires —, Ringover, Microsoft 365/EU Data Boundary) ; absente ou non confirmée pour Google Maps Platform, Mapbox (source US par défaut), HERE (transferts hors UE explicitement autorisés), Postmark, Twilio Voice, Vonage.

---

## 6. Paiement

### Stripe

- **Documentation officielle** : [docs.stripe.com/api](https://docs.stripe.com/api) — API REST, réponses JSON, versionnée.
- **Disponibilité France/Europe** : page tarifs France dédiée — [stripe.com/en-fr/pricing](https://stripe.com/en-fr/pricing) ; entité européenne Stripe Technology Company, Limited (Irlande).
- **Authentification** : clé API (Bearer) ; mode live/sandbox déterminé par la clé ; OAuth disponible côté Connect pour comptes connectés — [docs.stripe.com/api/authentication.md](https://docs.stripe.com/api/authentication.md)
- **Sandbox/test** : oui, environnements « sandboxes » isolés des données live — [docs.stripe.com/sandboxes.md](https://docs.stripe.com/sandboxes.md)
- **Webhooks** : oui, endpoint HTTPS temps réel, relais possible vers Amazon EventBridge/Azure Event Grid — [docs.stripe.com/webhooks](https://docs.stripe.com/webhooks)
- **Capacités principales** : cartes, Payment Links, Connect (marketplaces, virements vers comptes connectés, Treasury, Issuing) — [docs.stripe.com/connect](https://docs.stripe.com/connect)
- **Limites principales** : pas de mise à jour en masse (un objet par requête) — [docs.stripe.com/api](https://docs.stripe.com/api)
- **Prix public France** : cartes EEE standard 1,5 % + 0,25 € ; premium 2,8 % + 0,25 € ; UK 2,5 % + 0,25 € ; internationales 3,15 % + 0,25 € (+2 % conversion) ; SEPA 0,35 €/transaction ; pas de frais fixes — [stripe.com/en-fr/pricing](https://stripe.com/en-fr/pricing)
- **RGPD / résidence des données** : pas de résidence UE garantie — flux possibles vers les États-Unis, encadrés par le Data Privacy Framework et des SCC — DPA officiel : [stripe.com/legal/dpa](https://stripe.com/legal/dpa)
- **Dépendance fournisseur / alternatives** : forte intégration Connect/Treasury/Issuing (migration complexe si largement utilisés) ; alternatives France/UE : Mollie, Adyen, Lyra.

### GoCardless

- **Documentation officielle** : [docs.gocardless.com/api-reference](https://docs.gocardless.com/api-reference) ; guides SEPA — [gocardless.com/guides/sepa/mandates](https://gocardless.com/guides/sepa/mandates)
- **Disponibilité France/Europe** : spécialiste prélèvement SEPA Core, zone euro — [gocardless.com/en-us/guides/sepa/mandate-contents/](https://gocardless.com/en-us/guides/sepa/mandate-contents/)
- **Authentification** : Bearer token, OAuth également supporté.
- **Sandbox/test** : oui, `https://api-sandbox.gocardless.com/`, inscription séparée.
- **Webhooks** : oui — mandate, payment, payout, refund, subscription.
- **Capacités principales** : mandats SEPA, paiements récurrents/abonnements, échéanciers, payouts.
- **Limites principales** : pas de paiement carte/TPE in-person identifié dans la documentation.
- **Prix public** : plan Standard international 2 % + 20p, Advanced 2,25 % + 20p, Pro 2,4 % + 20p ; **le taux Eurozone précis n'a pas été confirmé sur une page officielle** — à vérifier sur [gocardless.com/pricing](https://gocardless.com/pricing).
- **RGPD / résidence des données** : programme conforme RGPD documenté — [gocardless.com/privacy/en-gdpr/](https://gocardless.com/privacy/en-gdpr/) ; résidence UE non confirmée textuellement.
- **Dépendance fournisseur / alternatives** : société britannique opérant en zone SEPA ; alternatives : Stripe (SEPA natif), Mollie.

### SumUp

- **Documentation officielle** : [developer.sumup.com/api](https://developer.sumup.com/api)
- **Disponibilité France/Europe** : page tarifs France — [sumup.com/fr-fr/tarifs/](https://www.sumup.com/fr-fr/tarifs/)
- **Authentification** : clés API Bearer (`sup_sk_...`).
- **Sandbox/test** : oui, comptes marchands sandbox via dashboard.
- **Webhooks** : oui mais limités — un seul type d'événement (changement de statut checkout), signature HMAC SHA-256 — [developer.sumup.com/docs/online-payments/introduction/webhooks/](https://developer.sumup.com/docs/online-payments/introduction/webhooks/)
- **Capacités principales** : paiement terrain/TPE (lecteurs Air/3G), paiements en ligne, Apple Pay, payouts.
- **Limites principales** : webhooks pauvres ; positionnement historique terrain plus que SaaS B2B.
- **Prix public (France)** : sans abonnement — 1,75 % en personne, 2,5 % en ligne ; plan Payments Plus 19 €/mois — 0,89 % cartes domestiques, 1,75 % premium/internationales — [sumup.com/fr-fr/tarifs/](https://www.sumup.com/fr-fr/tarifs/)
- **RGPD / résidence des données** : non trouvé.
- **Dépendance fournisseur / alternatives** : dépendance matérielle propriétaire (lecteurs) ; alternatives : Zettle (PayPal), Lyra, Stripe Terminal.

### Lyra (PayZen / Lyra Collect)

- **Documentation officielle** : [docs.lyra.com/fr](https://docs.lyra.com/fr) (fetch direct en échec technique lors de cette recherche — page fortement dynamique).
- **Disponibilité France/Europe** : « Made in France », plateforme opérée depuis la France — [payzen.eu](https://www.payzen.eu/)
- **Authentification** : clés API test/production distinctes ; mécanisme précis non revérifié en source primaire.
- **Sandbox/test** : clés API test séparées des clés production.
- **Webhooks** : oui — mécanisme IPN (Instant Payment Notification), signé par clé partagée — [docs.lyra.com/fr/rest/V4.0/api/kb/ipn.html](https://docs.lyra.com/fr/rest/V4.0/api/kb/ipn.html)
- **Capacités principales** : paiement à distance, TPE, 3DS2, infrastructure bancaire française redondante, PCI DSS/DSP2/ISO 27001.
- **Limites principales** : documentation officielle difficile à récupérer automatiquement (page JS) ; acteur de taille plus modeste que Stripe/Adyen à l'international.
- **Prix public** : non confirmé — modèle IC++ dégressif sur devis, sans grille chiffrée publique ([lyra.com/fr/tarifs/](https://www.lyra.com/fr/tarifs/)) ; un chiffre tiers (1,4 % + 0,20 €) circule mais n'est pas officiel, à ne pas retenir tel quel.
- **RGPD / résidence des données** : hébergement européen revendiqué, non vérifié par fetch direct d'une page officielle.
- **Dépendance fournisseur / alternatives** : positionnement « souveraineté » plus marqué que Stripe ; alternatives : Stripe, Mollie, Adyen.

### Mollie (candidat complémentaire, non approfondi)

- **Documentation officielle** : [docs.mollie.com/reference/overview](https://docs.mollie.com/reference/overview)
- **Disponibilité France/Europe** : acteur néerlandais, fort ancrage UE (iDEAL, SEPA).
- **Sandbox/test** : oui, comportement identique test/prod y compris webhooks — [docs.mollie.com/reference/testing](https://docs.mollie.com/reference/testing)
- **Webhooks** : oui, « Next-gen Webhooks » (bêta) — [docs.mollie.com/reference/webhooks](https://docs.mollie.com/reference/webhooks)
- **Capacités principales** : cartes, iDEAL, SEPA Direct Debit, Outbound Payments (virements SEPA Instant sortants).
- **Prix public** : ~1,8 % + 0,25 € cartes UE selon source tierce — page pricing officielle non fetchée, à confirmer sur mollie.com/pricing.
- Authentification, RGPD, limites : non approfondis dans cette recherche (candidat secondaire retenu pour complétude du panorama).

*Note méthodologique : quota de recherche atteint avant vérification indépendante complète de certains points (taux Eurozone exact GoCardless, RGPD SumUp, pricing officiel Mollie, partie de la doc Lyra) — signalés comme tels plutôt qu'affirmés.*

---

## 7. Banque / open banking

### Budget Insight / Powens

- **Documentation officielle** : [docs.powens.com](https://docs.powens.com/documentation), référence API — [docs.powens.com/api-reference](https://docs.powens.com/api-reference)
- **Disponibilité France/Europe** : « plus de 1 800 banques » en Europe revendiquées — [powens.com/fr](https://www.powens.com/fr/) ; établissement de paiement enregistré ACPR (code banque 16948) + entité liée régulée par la Banque d'Espagne.
- **Authentification** : tokens à scopes (user access tokens temporaires 30 min ou permanents, service tokens scopés type `payments:admin`) — [docs.powens.com/api-reference/overview/authentication](https://docs.powens.com/api-reference/overview/authentication)
- **Sandbox/test** : « test connector » documenté pour Pay by Bank ; pas de sandbox complet clairement distinct de la production identifié.
- **Webhooks** : oui — [docs.powens.com/documentation/integration-guides/webhooks](https://docs.powens.com/documentation/integration-guides/webhooks)
- **Capacités principales** : agrégation de comptes, agrégation de patrimoine, récupération de documents, initiation de paiement (Pay by Bank, SEPA instantané), IBAN virtuels, prélèvement, vérification d'identité.
- **Limites principales** : pas de quotas publics trouvés.
- **Prix public** : non trouvé — modèle sur devis (forfait/transaction/revenue-sharing).
- **RGPD / résidence des données** : ISO 27001 revendiqué ; pas de page RGPD dédiée trouvée.
- **Dépendance fournisseur / alternatives** : acteur français historique, double agrément ACPR + Banque d'Espagne ; alternatives : Bridge, Tink.

### Bridge API (Bankin')

- **Documentation officielle** : [docs.bridgeapi.io](https://docs.bridgeapi.io/docs/quickstart)
- **Disponibilité France/Europe** : entreprise française, 4,2M+ utilisateurs Bankin' revendiqués, 10M comptes synchronisés/jour ; nombre exact de banques couvertes non confirmé de façon fiable.
- **Statut réglementaire** : premier acteur européen agréé PISP+AISP par l'ACPR (2018) — [bridgeapi.io/actualites/dsp2](https://www.bridgeapi.io/actualites/dsp2)
- **Authentification** : mécanisme exact non extrait avec certitude (page dynamique) — à vérifier directement.
- **Sandbox/test** : oui, mais **explicitement non migrable vers la production** (« This is not a preproduction environment ») — [docs.bridgeapi.io/docs/quickstart](https://docs.bridgeapi.io/docs/quickstart)
- **Webhooks** : oui, jusqu'à 10 par application, IP whitelisting + signature — [docs.bridgeapi.io/docs/webhooks](https://docs.bridgeapi.io/docs/webhooks)
- **Capacités principales** : agrégation continue, initiation de paiement (liens email/SMS/QR), vérification d'identité par IBAN, scoring, réconciliation bancaire assistée par IA.
- **Limites principales** : sandbox non migrable vers la production ; quotas non trouvés.
- **Prix public** : non trouvé officiellement (pages tarifs testées en erreur) ; mention tierce non confirmée d'environ 499 €/mois, à ne pas retenir sans confirmation.
- **RGPD / résidence des données** : pages légales référencées par l'éditeur, détails non extraits dans cette recherche.
- **Dépendance fournisseur / alternatives** : acteur français (groupe Bankin'), 700+ clients pro revendiqués ; alternatives : Powens, Tink.

### Tink (groupe Visa)

- **Documentation officielle** : [docs.tink.com/api](https://docs.tink.com/api)
- **Disponibilité France/Europe** : 6 000+ connexions bancaires en Europe revendiquées (chiffre variable selon sources/dates).
- **Statut réglementaire** : licence PSD2 propre (Suède, Finansinspektionen), passportée UE ; pas d'agrément ACPR direct ; racheté par Visa en 2022.
- **Authentification** : OAuth (client credentials + mutual TLS), Bearer token, scopes fins — [docs.tink.com/resources/api-setup/get-access-token](https://docs.tink.com/resources/api-setup/get-access-token)
- **Sandbox/test** : oui, « Demo Bank » — [docs.tink.com/resources/console/demo-bank](https://docs.tink.com/resources/console/demo-bank)
- **Webhooks** : oui, par produit — [docs.tink.com/resources/api-setup/webhooks](https://docs.tink.com/resources/api-setup/webhooks)
- **Capacités principales** : agrégation, paiements (Pay by Bank, Variable Recurring Payments, Payouts), risque/scoring, vérification de compte, enrichissement de données, Money Manager.
- **Limites principales** : fonctionnalités avancées réservées au tier Enterprise (contact commercial uniquement).
- **Prix public** : non trouvé — page pricing réservée aux clients existants, nouveaux prospects redirigés vers les ventes — [tink.com/pricing](https://tink.com/pricing/)
- **RGPD / résidence des données** : SOC 2 Type II revendiqué ; détails RGPD non extraits.
- **Dépendance fournisseur / alternatives** : dépendance à un groupe international (Visa), modèle commercial peu transparent ; alternatives plus ancrées France/ACPR : Powens, Bridge.

**Point d'attention : GoCardless Bank Account Data (ex-Nordigen)**, envisagé initialement comme candidat, mais **les nouvelles inscriptions sont fermées depuis juillet 2025** (« New signups for Bank Account Data are currently disabled », sans date de reprise annoncée) — [bankaccountdata.gocardless.com/new-signups-disabled](https://bankaccountdata.gocardless.com/new-signups-disabled). **Non exploitable pour SUPORDO en l'état 2026.** Les sources consultées citent Enable Banking comme remplaçant pratique le plus fréquemment mentionné, non vérifié en profondeur dans cette recherche.

---

## 8. Comptabilité / expert-comptable

### Pennylane (API)

- **Documentation officielle** : [pennylane.readme.io](https://pennylane.readme.io/) — Company API, Firm API, FirmGroup API.
- **Disponibilité France/Europe** : éditeur français, données hébergées AWS Irlande (UE) — [pennylane.com/fr/legal/centre-de-confiance](https://www.pennylane.com/fr/legal/centre-de-confiance)
- **Authentification** : tokens API (usage standard) ; OAuth 2.0 pour usage massif via partenariat.
- **Sandbox/test** : oui, hérite du plan d'abonnement de l'espace principal.
- **Webhooks** : disponibles, en version bêta — [pennylane.readme.io/docs/webhooks](https://pennylane.readme.io/docs/webhooks)
- **Capacités principales** : facturation (Factur-X), clients/fournisseurs/produits, écritures comptables, transactions bancaires.
- **Export FEC via API** : oui — endpoints dédiés `POST/GET .../exports/fecs`, OAuth2 + scope `exports:fec`, génération asynchrone — [pennylane.readme.io/reference/exportfec](https://pennylane.readme.io/reference/exportfec) ; export également disponible via l'UI.
- **Limites principales** : accès API non inclus sous le plan Essentiel minimum (24 €/mois) ; migration API majeure annoncée pour le 1er juillet 2026.
- **Prix public** : Gratuit 0 €, Starter 7 €/mois, Basique 14 €/mois, Essentiel 24 €/mois (accès API) — [pennylane.com/fr/tarifs](https://www.pennylane.com/fr/tarifs)
- **RGPD / résidence des données** : ISO 27001, chiffrement, données limitées à l'UE (AWS Irlande) — [pennylane.com/fr/legal/centre-de-confiance](https://www.pennylane.com/fr/legal/centre-de-confiance)
- **Dépendance fournisseur / alternatives** : offre unifiée facturation + compta + API assez rare sur le marché français ; alternatives : Sage.

### QuickBooks (Intuit) — écarté de facto pour la France

- **Point critique constaté** : **Intuit a cessé la commercialisation et le support de QuickBooks en France** (arrêt total au 31/12/2023, intégrations tierces cessées) — [blog.insightfulaccountant.com](https://blog.insightfulaccountant.com/intuit-is-turning-out-the-lights-in-france). **Candidat non exploitable pour des artisans/TPE françaises en 2026.**
- Documentation officielle (usage hors France) : [developer.intuit.com](https://developer.intuit.com/app/developer/qbo/docs/learn/explore-the-quickbooks-online-api) — OAuth 2.0, sandbox jusqu'à 5 entreprises de test, webhooks (30+ entités, migration CloudEvents 2026), API REST/JSON.
- Export FEC : non trouvé (cohérent avec le retrait du marché français).
- **Conservé dans ce document uniquement pour mémoire** — à ne pas retenir comme candidat viable pour SUPORDO.

### Sage (Business Cloud Accounting API / Sage Active)

- **Documentation officielle** : [developer.sage.com](https://developer.sage.com/) — offre fragmentée : Business Cloud Accounting API (international), Sage Active Developer (TPE France, accès bloqué HTTP 403 lors de la vérification), Sage 100 France (pas d'API REST publique standard identifiée).
- **Authentification** : OAuth 2.0, access token ~1h, refresh token ~31 jours.
- **Sandbox/test** : oui pour Business Cloud Accounting.
- **Webhooks** : non disponibles sur Business Cloud Accounting (polling uniquement) ; statut sur Sage Active non trouvé.
- **Capacités principales** : contacts, factures, paiements, grand livre, TVA (Business Cloud) ; immobilisations, facturation électronique France (Sage Active).
- **Export FEC** : import FEC disponible via l'UI Sage Active (conforme DGFiP) ; **aucun endpoint API dédié à l'export FEC identifié**, contrairement à Pennylane.
- **Limites principales** : forte hétérogénéité entre produits Sage (risque de migration interne à l'éditeur lui-même) ; documentation officielle partiellement inaccessible lors de cette recherche.
- **Prix public** : accès développeur gratuit ; tarification production non trouvée.
- **Dépendance fournisseur / alternatives** : alternative principale = Pennylane (API plus unifiée) ; Cegid/Quadratus et Indy non documentés publiquement de façon vérifiable dans cette recherche (candidats non retenus faute d'API publique documentée).

### Norme FEC (référence légale, transverse à cette catégorie)

- **Base légale** : obligation posée par l'**article L47 A du Livre des procédures fiscales** (comptabilité informatisée → fourniture d'une copie dématérialisée en cas de contrôle) — [legifrance.gouv.fr](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000037526053) ; forme et contenu précisés par l'**article A47 A-1 du LPF** — [legifrance.gouv.fr](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000027804775) ; page DGFiP dédiée — [impots.gouv.fr](https://www.impots.gouv.fr/fichiers-standards-des-ecritures-comptables-art-l-47-1-du-lpf) ; doctrine BOFiP — [BOI-CF-IOR-60-40-20](https://bofip.impots.gouv.fr/bofip/9028-PGP.html/identifiant=BOI-CF-IOR-60-40-20-20170607)
- **Structure** : fichier texte à colonnes délimitées ou XML (XSD publiés par la DGFiP), 18 champs obligatoires (JournalCode, EcritureNum, EcritureDate, CompteNum, Debit, Credit, etc.) — détail des champs confirmé par une source spécialisée tierce, à recouper avec le texte légal pour un usage réglementaire strict.
- **Qui doit produire un FEC** : tout contribuable tenant une comptabilité informatisée (couvre la quasi-totalité des artisans/TPE outillés), sur demande de l'administration lors d'une vérification de comptabilité (contrôle fiscal).

---

## 9. Facturation électronique France — réforme B2B 2026 (PRIORITAIRE)

> Contrainte réglementaire structurante pour SUPORDO en tant qu'émetteur de factures
> pour ses clients artisans. Recherche menée en priorité, sources officielles
> privilégiées (Légifrance, impots.gouv.fr, economie.gouv.fr).

**Avertissement méthodologique du sous-agent** : le calendrier de cette réforme a été
modifié plusieurs fois depuis son lancement (2023-2025). La version la plus récente et
juridiquement stabilisée à la date de cette recherche (23 septembre 2026) est le
**décret n° 2026-677 du 27 juillet 2026** et son **arrêté d'application** du même
jour (JO du 28 juillet 2026), qui ont clôturé le cadre réglementaire un mois avant
l'entrée en vigueur du 1er septembre 2026.

### 9.1 Calendrier légal obligatoire

| Date | Obligation | Entreprises concernées |
|---|---|---|
| **1er septembre 2026** | Réception des factures électroniques | **Toutes** les entreprises assujetties à la TVA établies en France |
| **1er septembre 2026** | Émission des factures électroniques + transmission des données d'e-reporting | Grandes entreprises et ETI |
| **1er septembre 2027** | Émission des factures électroniques + e-reporting | PME, TPE et micro-entreprises (**cœur de cible SUPORDO**) |

Sources :
- Décret n° 2026-677 du 27 juillet 2026 — https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000054499487 (JO 28/07/2026)
- Arrêté du 27 juillet 2026 — https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000054499535 (JO 28/07/2026)
- impots.gouv.fr, « Je passe à la facturation électronique » — https://www.impots.gouv.fr/professionnel/je-passe-la-facturation-electronique (page mise à jour au 01/09/2026)

**Tentative de report en 2025 — rejetée.** Un amendement (CS1268), adopté en
commission spéciale le 24 mars 2025, proposait un nouveau report de l'échéance ; il a
été **rejeté en séance publique** à l'Assemblée nationale au printemps 2025. Le
calendrier ci-dessus n'a donc pas été repoussé une nouvelle fois. *Point signalé comme
non vérifié en source primaire (Assemblée nationale) par le sous-agent — à confirmer
sur assemblee-nationale.fr avant citation ferme dans une version finale du blueprint.*

**Conclusion** : à la date du 23 septembre 2026, aucun report supplémentaire n'est
documenté après le décret/arrêté du 27 juillet 2026. Le régime du 1er septembre 2026
(réception universelle + émission grandes entreprises/ETI) est en vigueur depuis 3
semaines au moment de la rédaction.

### 9.2 PDP → « Plateforme Agréée » (PA) — statut de l'annuaire officiel

Le décret n° 2026-677 du 27 juillet 2026 remplace dans les textes réglementaires
(annexe II du CGI) les notions de « plateforme de dématérialisation partenaire »
(PDP) et de « portail public de facturation » par la notion unique de **« plateforme
agréée » (PA)**. Source : https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000054499487

*Nuance signalée par le sous-agent* : plusieurs sources professionnelles (Libeo,
ecma-solutions) évoquent un usage informel du terme « Plateforme Agréée » circulant
dès juillet 2025, avant sa consécration officielle en juillet 2026 — ancrage juridique
ferme = le décret de juillet 2026.

**Annuaire officiel** :
- Liste des plateformes agréées (DGFiP) — **https://www.impots.gouv.fr/je-consulte-la-liste-des-plateformes-agreees**
  (page modifiée le 22/09/2026, veille de cette recherche). Deux listes téléchargeables
  (ODS/XLSX/PDF) : opérateurs pleinement immatriculés vs opérateurs en attente
  d'immatriculation finale. Pas d'annuaire interactif en ligne.
- https://www.impots.gouv.fr/facturation-electronique-et-plateformes-agreees
- Annonce DGFiP de la première publication de la liste — https://www.impots.gouv.fr/actualite/facturation-electronique-publication-de-la-liste-des-plateformes-agreees
- Annonce economie.gouv.fr — https://www.economie.gouv.fr/actualites/facturation-electronique-la-liste-des-101-premieres-plateformes-agreees-est-disponible

**Nombre de plateformes agréées — chiffre volatil, à ne pas figer.** Sources
secondaires convergentes mais divergentes en valeur : 101 (annonce initiale, date non
capturée précisément) → 138 au 14/06/2026 → 147 en août 2026 (tool-advisor.fr) → 150
immatriculations / 148 opérateurs distincts au 02/09/2026 (comparateur-efacturation.fr).
**Recommandation : le blueprint doit toujours renvoyer vers la page officielle
impots.gouv.fr ci-dessus plutôt que citer un nombre figé.**

### 9.3 Rôle du Portail Public de Facturation (PPF) — périmètre modifié

**Changement majeur confirmé** : depuis un communiqué DGFiP du 15 octobre 2024, le
PPF **n'est plus une solution gratuite d'émission/réception de factures** — abandonné
avant même l'entrée en vigueur de la réforme. Le décret n° 2026-677 retire toute
référence au PPF comme opérateur de facturation et ne lui conserve que deux fonctions :

1. **Annuaire central** — répertorie chaque entreprise assujettie (SIREN/SIRET ou code
   de routage interne) et sa plateforme agréée de rattachement.
2. **Concentrateur de données fiscales** — achemine vers la DGFiP les données
   d'e-invoicing et d'e-reporting transmises par les PA.

Sources : décret n° 2026-677 (idem) ; analyse PwC Avocats —
https://www.pwcavocats.com/fr/ealertes/ealertes-france/2026/juillet/decret-et-arrete-du-27-juillet-2026-la-reforme-franchit-sa-derniere-etape-reglementaire.html

**Inscription obligatoire à l'annuaire central** avant le 1er septembre 2026, avec
choix d'un niveau d'adressage (SIREN, SIRET, ou code de routage interne). *Accès de
consultation mentionné via Chorus Pro (facturation.chorus-pro.gouv.fr) par des sources
secondaires (why.eu, france-factures.fr) — non vérifié par fetch primaire, à confirmer.*

**Tolérances actées par le même décret/arrêté** (annoncées informellement à l'automne
2025, désormais juridiques) : pas de sanction pour absence de SIREN seule ; tolérance
en cas de retard d'intégration à l'annuaire imputable à un dysfonctionnement de
l'administration ; abandon de l'obligation de détail ligne par ligne pour les flux
internationaux entrants.

### 9.4 Format Factur-X (et alternatives UBL, CII)

**Factur-X** — format de référence recommandé pour les petites structures :
- Format hybride **PDF/A-3 + XML embarqué**, conforme à la norme sémantique
  européenne **EN 16931**.
- Cinq profils : MINIMUM, BASIC WL, BASIC, EN 16931, EXTENDED (richesse croissante).
- Co-développé par **FNFE-MPE** (France) et **FeRD** (Allemagne).
- Documentation technique officielle : **https://fnfe-mpe.org/factur-x/**
  (anglais : https://fnfe-mpe.org/factur-x/factur-x_en/)
- Schémas XSD/Schematrons et validateurs (FNFE-MPE, KoSIT) disponibles librement.
- *Version « Factur-X 1.08 », publiée décembre 2025, applicable au 15/01/2026 —
  donnée par sources secondaires agrégées uniquement, non confirmée par fetch direct
  du site FNFE-MPE. À vérifier avant citation ferme.*

**Formats alternatifs** (tous conformes EN 16931) :
- **UBL** (Universal Business Language, OASIS) — référence du réseau **PEPPOL** ; pour
  la France, doit respecter le profil **CIUS-FR** (champs SIREN, code de routage PA,
  type d'opération, mentions légales obligatoires).
- **CII** (Cross Industry Invoice, UN/CEFACT) — pour échanges B2B complexes/globaux.

Le choix entre formats dépend de la complexité du SI de l'émetteur/destinataire, pas
d'une hiérarchie de conformité — les trois véhiculent le même socle EN 16931.

### 9.5 e-invoicing vs e-reporting — deux flux distincts

| | e-invoicing | e-reporting |
|---|---|---|
| Objet | Facture électronique complète (Factur-X/UBL/CII) | Données de transaction (pas la facture complète) |
| Périmètre | B2B domestique entre assujettis TVA établis en France | B2C, international (import/export, intra/extra-UE), données de paiement (prestations de services) |
| Destinataire | Le client, via sa plateforme agréée | L'administration fiscale uniquement |
| Vecteur | PA émettrice → PA du destinataire (statuts de cycle de vie : dépôt, rejet, encaissement…) | PA → concentrateur PPF → DGFiP |
| Échéance | 01/09/2026 (grandes entreprises/ETI) puis 01/09/2027 (PME/TPE/micro) | Idem |

Sources : impots.gouv.fr (« Je passe à la facturation électronique ») ; décret
n° 2026-677 (modifie notamment les art. 289 bis, 289 E, 290, 290 A, 290 B, 242 nonies
B et suivants du CGI).

### 9.6 Implications concrètes pour SUPORDO

**SUPORDO n'a pas d'obligation de devenir lui-même une plateforme agréée.** Un logiciel
de gestion/CRM/facturation comme SUPORDO est qualifié de **« Solution Compatible »
(SC)** : génère des factures conformes mais n'est pas immatriculé par l'État. Une
Solution Compatible **doit transiter par une Plateforme Agréée immatriculée** — elle
ne peut pas court-circuiter le dispositif. Confirmé par la mention explicite du
« label solution compatible » sur la page officielle impots.gouv.fr (§9.2).

Deux voies d'architecture possibles, sans choix fait ici :
1. **Intégration API directe avec une PA tierce** (liste officielle DGFiP, §9.2) pour
   émission, réception, suivi des statuts de cycle de vie, transmission e-reporting —
   voie la plus légère opérationnellement.
2. **Partenariat white-label** : certaines PA opèrent en arrière-plan sous la marque
   de l'éditeur logiciel, qui garde la relation client directe. Exemple de mécanisme
   documenté dans le marché (cité à titre illustratif, sans recommandation) :
   https://www.esalink.com/nos-services/partenaires-solutions-compatibles/

**Obligations minimales pour SUPORDO comme Solution Compatible** :
- Générer des factures conformes EN 16931 (Factur-X recommandé pour public TPE/artisans ;
  UBL/CIUS-FR si interconnexion PEPPOL nécessaire).
- Se connecter (API) à une/des PA pour l'acheminement effectif et l'e-reporting — pas
  d'émission « en direct » possible à partir du 01/09/2026 (clients grandes entreprises/
  ETI) puis du 01/09/2027 (généralisation aux artisans/TPE eux-mêmes).
- Intégrer les règles de **portabilité entre PA** fixées par le décret n° 2026-677 :
  délais réglementaires de 2, 5 et 15 jours ouvrés selon les étapes, maintien des
  services pendant un an après changement de PA, information gratuite du client sur
  les modalités de bascule.
- Distinguer dans le moteur de facturation les flux e-invoicing (B2B domestique) des
  flux e-reporting (B2C/international/paiement) — cf. §9.5.

**Calendrier pertinent pour le cœur de cible SUPORDO** (artisans BTP, typiquement
TPE/PME) : obligation d'**émission** seulement à partir du **1er septembre 2027**.
Obligation de **réception** déjà applicable à tous depuis le **1er septembre 2026**.
→ Le blueprint doit prévoir SUPORDO opérationnel en réception dès la mise en
production si elle intervient après septembre 2026, et en émission conforme au plus
tard pour septembre 2027.

*Sources de ce point 9.6 : synthèses de marché non officielles (Tiime,
ma-facture-electronique.org, comparepdp.com, iopole.com) pour les mécanismes
opérationnels ; la structure Solution Compatible / Plateforme Agréée elle-même est
confirmée par la page officielle impots.gouv.fr (§9.2).*

### 9.7 Chronologie récapitulative (2024-2026)

| Date | Événement | Source |
|---|---|---|
| 15/10/2024 | Communiqué DGFiP : abandon du PPF comme plateforme gratuite d'émission/réception | Cité par décret n° 2026-677 / analyse PwC |
| 24/03/2025 | Amendement CS1268 (report) adopté en commission spéciale | Sources secondaires convergentes |
| Printemps 2025 | CS1268 **rejeté en séance publique** — calendrier maintenu | Sources secondaires convergentes (non vérifié en primaire) |
| Automne 2025 | Tolérances DGFiP annoncées (SIREN, annuaire, flux internationaux) | Formalisées ensuite par décret/arrêté 27/07/2026 |
| 27/07/2026 | **Décret n° 2026-677** + arrêté — cadre réglementaire bouclé | Légifrance (liens §9.1) |
| 28/07/2026 | Publication JO, entrée en vigueur le lendemain | idem |
| 01/09/2026 | Entrée en vigueur opérationnelle : réception universelle + émission grandes entreprises/ETI | LF 2024, confirmée par décret 2026-677 |
| 22/09/2026 | Dernière mise à jour constatée de la page officielle liste PA | impots.gouv.fr (§9.2) |

**Verdict à date (23/09/2026)** : calendrier 01/09/2026 / 01/09/2027 définitif et en
vigueur, consolidé par le décret/arrêté du 27/07/2026, sans report supplémentaire
documenté. Point d'attention pour le blueprint : non plus « le calendrier va-t-il
bouger » mais « SUPORDO doit être prêt pour l'échéance émission TPE/PME du
1er septembre 2027 », réception déjà obligatoire pour tous depuis le 1er septembre 2026.

### 9.8 Points d'incertitude à ne pas figer sans revérification

1. **Nombre exact de plateformes agréées immatriculées** (101 à 150 selon source/date)
   — toujours renvoyer vers la page officielle DGFiP plutôt que citer un chiffre figé.
2. **URL Chorus Pro pour l'annuaire central** (facturation.chorus-pro.gouv.fr) —
   mentionnée par sources secondaires uniquement, non vérifiée par fetch primaire.
3. **Version et date exactes de Factur-X 1.08** — sources secondaires agrégées
   uniquement, non confirmées par fetch direct de fnfe-mpe.org.
4. **Rejet précis de l'amendement CS1268** (date, modalités du vote) — confirmé par
   plusieurs sources secondaires convergentes mais pas par une source primaire
   Assemblée nationale consultée directement.

---

## 10. Identité entreprise France

### API INSEE Sirene (api.insee.fr)

- **Documentation officielle** : [portail-api.insee.fr](https://portail-api.insee.fr/catalog/api/2ba0e549-5587-3ef1-9082-99cd865de66f/doc) ; fiche — [data.gouv.fr](https://www.data.gouv.fr/dataservices/api-sirene-open-data)
- **Disponibilité** : France uniquement.
- **Authentification** : compte + application sur api.insee.fr, jeton Bearer valable 24h (renouvellement quotidien recommandé).
- **Sandbox/test** : non trouvé explicitement.
- **Webhooks** : non trouvé (API de lookup).
- **Capacités principales** : recherche/consultation base SIRENE (unités légales, établissements, historique d'événements).
- **Limites principales** : **30 requêtes/minute** (usage open data) ; gestion du statut « diffusion partielle » (remplace le statut « non diffusible » depuis le 21/03/2023).
- **Prix** : gratuit — [data.gouv.fr](https://www.data.gouv.fr/dataservices/api-sirene-open-data)
- **RGPD/résidence des données** : mécanisme de diffusion partielle protégeant les données personnelles des dirigeants d'entreprises individuelles ; registre public français, administration française.
- **Dépendance fournisseur / alternatives** : source primaire officielle, faible lock-in ; bascule possible vers Recherche d'Entreprises ou Pappers.

### API Recherche d'Entreprises (recherche-entreprises.api.gouv.fr)

- **Documentation officielle** : [recherche-entreprises.api.gouv.fr/docs/](https://recherche-entreprises.api.gouv.fr/docs/) ; fiche — [data.gouv.fr](https://www.data.gouv.fr/dataservices/api-recherche-dentreprises)
- **Disponibilité** : France uniquement.
- **Authentification** : **aucune** — accès complètement ouvert.
- **Sandbox/test** : non applicable (accès libre direct), interface Swagger interactive disponible.
- **Webhooks** : non trouvé.
- **Capacités principales** : recherche textuelle (raison sociale, adresse, dirigeants/élus), recherche par SIREN/SIRET.
- **Limites principales** : **7 appels/seconde** (l'administration se réserve le droit de l'abaisser) ; pas d'accès aux entités non diffusibles ni aux refus d'immatriculation RCS ; pas d'accès complet à la base SIRENE contrairement à l'API Sirene.
- **Prix** : gratuit, disponibilité annoncée 100 %.
- **RGPD/résidence des données** : politique dédiée — [annuaire-entreprises.data.gouv.fr/vie-privee](https://annuaire-entreprises.data.gouv.fr/vie-privee)
- **Dépendance fournisseur / alternatives** : lock-in quasi nul, API publique ouverte ; limite à surveiller si besoin de débit &gt;7 req/s.

### Pappers API

- **Documentation officielle** : [pappers.fr/api](https://www.pappers.fr/api) (accès direct bloqué HTTP 403 lors de cette recherche), [pappers.fr/api/documentation](https://www.pappers.fr/api/documentation)
- **Disponibilité** : France (agrégation INSEE + INPI + BODACC).
- **Authentification** : non confirmé précisément (page officielle non accessible en fetch direct) — à vérifier.
- **Sandbox/test** : non trouvé explicitement ; 100 crédits gratuits à l'inscription avec email professionnel.
- **Webhooks** : non trouvé.
- **Capacités principales** : informations légales enrichies (comptes, actes, statuts, dirigeants), enrichissement CRM/prospection.
- **Limites principales** : non quantifié précisément dans les sources consultées.
- **Prix** : modèle par crédits — 100 gratuits, puis Pay As You Go ou abonnements dégressifs selon volume, **montants exacts non confirmés en accès direct** (page 403) ; service annexe registres numérisés à 45 € HT/entreprise (depuis février 2026, page distincte) — [services.pappers.fr/annonces-legales/tarifs](https://services.pappers.fr/annonces-legales/tarifs)
- **RGPD/résidence des données** : politique dédiée — [pappers.fr/politique-de-protection-des-donnees-personnelles](https://www.pappers.fr/politique-de-protection-des-donnees-personnelles) ; droits RGPD standards, exercice via formulaire dédié, recours CNIL possible ; pas de mention explicite de résidence géographique des serveurs trouvée.
- **Dépendance fournisseur / alternatives** : service commercial à valeur ajoutée sur donnée publique ; lock-in modéré, la donnée brute reste accessible gratuitement via Sirene/Recherche d'Entreprises.

**Synthèse catégorie 10** : les deux API publiques gratuites couvrent le besoin de base sans dépendance commerciale ; Pappers apporte une valeur ajoutée (agrégation, historique, dirigeants) dont le tarif précis doit être reconfirmé (page pricing bloquée lors de cette recherche).

---

## 11. Signature électronique

### Yousign

- **Documentation officielle** : [developers.youtrust.com](https://developers.youtrust.com/) (Yousign racheté/rebrandé Youtrust ; ancien domaine developers.yousign.com redirige en 301).
- **Disponibilité France/Europe** : éditeur français, référence France/UE.
- **Authentification** : API Key ; pas de confirmation d'une alternative OAuth2 dans la doc consultée.
- **Sandbox/test** : oui, `api-sandbox.yousign.app/v3` isolé de la production, limité à 30 req/min et 200/h, signatures non juridiquement valides (documents filigranés) — [developers.youtrust.com/docs/environments-new](https://developers.youtrust.com/docs/environments-new)
- **Webhooks** : oui, notification temps réel des événements de signature.
- **Capacités principales** : signature simple/avancée/qualifiée (Tiers de Confiance eIDAS), cachet électronique, vérification d'identité/document.
- **Limites principales** : sandbox non probante légalement ; rate limit bas en sandbox ; offre gratuite limitée aux emails de l'organisation.
- **Prix** (chiffres issus d'un agrégateur tiers, **non confirmés directement sur yousign.com/prix**) : Free 5 signatures/mois ; One 9 €/mois HT ; Plus 23 €/utilisateur/mois ; Pro à partir de 38 € ; API Plus à partir de 104 €/mois HT (500 signatures/an) ; API Pro à partir de 129 €/mois HT ; QES 10-15 €/unité.
- **RGPD/résidence des données** : données stockées en France (OVH, AWS, Azure), chiffrement AES256 — [help.yousign.app](https://help.yousign.app/en/articles/73158-yousign-the-gdpr)
- **Dépendance fournisseur / alternatives** : acteur français indépendant, positionné souveraineté vs DocuSign/Adobe ; portabilité des données non documentée (non trouvé).

### DocuSign

- **Documentation officielle** : [developers.docusign.com/docs/esign-rest-api/](https://developers.docusign.com/docs/esign-rest-api/)
- **Disponibilité France/Europe** : région de données dédiée « Europe » (parmi 5 régions), eSignature/IAM/CLM disponibles dans cette région — [docusign.com/privacy/data-residency](https://www.docusign.com/privacy/data-residency)
- **Authentification** : OAuth2 (Authorization Code confidentiel/public, Implicit, JWT Grant), scope `signature`.
- **Sandbox/test** : compte développeur gratuit, environnement démo.
- **Webhooks** : DocuSign Connect (mécanisme natif), confirmation de source primaire directe non extraite dans cette recherche.
- **Capacités principales — eIDAS** : QTSP enregistré en Europe, QES avec vérification d'identité en face-à-face (ou équivalent), distinction Simple/Avancée/Qualifiée.
- **Limites principales** : accès API probablement réservé aux plans Business Pro+ (non vérifié officiellement).
- **Prix** (agrégateurs tiers, **non officiels, à recouper**) : Personal 10-15 $/mois ; Standard 25-45 $/mois ; Business Pro 40-65 $/mois ; Enterprise sur devis ; Developer API Starter 50 $/mois ou 600 $/an.
- **RGPD/résidence des données** : DPA + SCC + BCR approuvées le 16/03/2018 ; données d'accord stockées en permanence en région Europe (sauf métadonnées limitées) ; la page officielle précise que le RGPD n'exige pas un stockage exclusivement intra-UE — [docusign.com/privacy/data-residency](https://www.docusign.com/privacy/data-residency)
- **Dépendance fournisseur / alternatives** : leader américain ; QES Europe réalisée via QTSP basé en France ; alternative citée : Yousign.

### Adobe Sign (Adobe Acrobat Sign)

- **Documentation officielle** : [developer.adobe.com/acrobat-sign/docs/overview/developer_guide/apiusage](https://developer.adobe.com/acrobat-sign/docs/overview/developer_guide/apiusage)
- **Disponibilité France/Europe** : shard européen « EU1 », format PAdES par défaut (ETSI EN 319142) pour conformité eIDAS.
- **Authentification** : OAuth 2.0, Bearer token, scopes dédiés (ex. `webhook_read`, `webhook_write`).
- **Sandbox/test** : « Acrobat Sign Developer Edition » gratuit ; production nécessite un plan Entreprise pour l'accès API.
- **Webhooks** : oui, « WebhookEndpoint APIs », two-way SSL handshake pour les callbacks.
- **Capacités principales — eIDAS** : trois niveaux (simple/avancé/qualifié), Adobe Approved Trust List + EU Trusted Lists, certificats QTSP européens.
- **Limites principales** : accès API réservé aux comptes Entreprise/développeur ; rate limiting par plan, HTTP 429 au-delà.
- **Prix** : **prix exact du plan Enterprise/API non trouvé** (contact commercial requis) ; plans Acrobat grand public identifiés (9,99-24,99 $/mois) sans lien clair avec l'accès API Sign.
- **RGPD/résidence des données** : centres de données UE/US/Asie, options de résidence configurables mais activation non automatique (nécessite paramétrage), DPA + SCC + Transfer Impact Assessment, AES-256/TLS 1.2+.
- **Dépendance fournisseur / alternatives** : acteur américain intégré à Document Cloud ; accès API = dépendance contractuelle/commerciale forte ; alternative citée : Yousign.

**Synthèse catégorie 11** : Yousign se distingue par une résidence de données explicitement France (OVH/AWS/Azure en France) contre une résidence « Europe » (DocuSign) ou « configurable mais non automatique » (Adobe) pour les deux acteurs américains ; plusieurs prix restent à reconfirmer directement sur les pages officielles.

---

## 12. Stockage cloud de documents/photos

### Supabase Storage

- **Documentation** : [supabase.com/docs/guides/storage](https://supabase.com/docs/guides/storage)
- **Compatibilité S3** : API compatible protocole S3 (rclone, AWS CLI, SDK AWS utilisables), en plus des API REST/TUS natives. Opérations bucket supportées : `ListBuckets`, `HeadBucket`, `CreateBucket`, `DeleteBucket`, `GetBucketLocation` (non supporté : CORS, chiffrement, lifecycle au niveau bucket). Opérations objet : `GetObject`, `PutObject`, `DeleteObject`, `HeadObject`, `ListObjects`/`ListObjectsV2`, requêtes conditionnelles, range requests, multipart upload complet, `CopyObject`. Limites vs S3 réel : pas de versioning, pas de SSE-C/KMS, pas d'ACL, pas de tagging d'objet, pas d'object locking, pas de Content-MD5, pas de redirection website — [supabase.com/docs/guides/storage/s3/compatibility](https://supabase.com/docs/guides/storage/s3/compatibility)
- **Authentification** : signature AWS SigV4, paire access_key/secret_key générée dans les paramètres Storage du projet (accès S3 à activer explicitement).
- **Disponibilité France/Europe** : 4 régions État membre UE — Ireland (`eu-west-1`), Paris (`eu-west-3`), Frankfurt (`eu-central-1`), Stockholm (`eu-north-1`) — + 2 régions européennes hors UE (Londres, Zurich). DB, Auth et Storage restent dans la région choisie à la création — [supabase.com/docs/guides/platform/regions](https://supabase.com/docs/guides/platform/regions)
- **Sandbox/test** : pas de mode dédié documenté ; plan Free et développement local via CLI en tiennent lieu.
- **Webhooks** : pas de webhook Storage natif dédié, mais Database Webhooks attachables à la table `storage.objects` (INSERT/UPDATE/DELETE) — [supabase.com/docs/guides/database/webhooks](https://supabase.com/docs/guides/database/webhooks)
- **Capacités principales** : upload standard/TUS (resumable)/S3, transformation d'images à la volée, buckets publics/privés, RLS Postgres sur les objets.
- **Limites principales** : taille fichier max 50 MB (Free), jusqu'à 500 GB (Pro/Team) — [supabase.com/docs/guides/storage/uploads/file-limits](https://supabase.com/docs/guides/storage/uploads/file-limits) ; quota inclus 1 GB (Free), 100 GB (Pro/Team).
- **Prix** ([supabase.com/pricing](https://supabase.com/pricing)) : Free $0 (1 GB storage, 5 GB egress) ; Pro dès $25/mois (100 GB inclus puis $0,0213/GB/mois ; egress $0,09/GB au-delà de 250 GB) ; Team dès $599/mois ; Enterprise sur devis. Transformation images : $5/1000 images au-delà de 100 incluses.
- **RGPD/résidence des données** : DPA ([supabase.com/legal/dpa](https://supabase.com/legal/dpa)), ISO 27001, SOC 2 (clients Team/Enterprise) — [supabase.com/docs/guides/security/gdpr-compliance](https://supabase.com/docs/guides/security/gdpr-compliance)
- **Dépendance fournisseur / alternatives** : réduite — compatibilité S3 + service `storage` open source (github.com/supabase/storage), migration possible vers tout store S3-compatible.

### AWS S3

- **Documentation** : [docs.aws.amazon.com/s3/](https://docs.aws.amazon.com/s3/)
- **Disponibilité France/Europe** : régions dédiées Paris (`eu-west-3`), Frankfurt, Ireland, Stockholm, Milan, Espagne. Attention : certains services globaux (IAM, Route 53, CloudFront) peuvent traiter des métadonnées hors UE.
- **Authentification** : IAM (clés, rôles, STS), bucket policies, URLs présignées.
- **Sandbox/test** : pas de mode dédié ; Free Tier (crédit pour nouveaux comptes selon source secondaire, non confirmée officiellement).
- **Webhooks** : pas de webhook HTTP direct — S3 Event Notifications route vers SNS/SQS/Lambda/EventBridge ; un webhook HTTP externe nécessite un relais Lambda — [docs.aws.amazon.com/AmazonS3/latest/userguide/EventNotifications.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/EventNotifications.html)
- **Capacités principales** : standard de facto du marché, classes de stockage multiples, réplication cross-région, versioning, lifecycle, SSE-C/KMS, ACL fines, écosystème Lambda/CloudFront/Athena.
- **Limites principales** : tarification complexe (stockage + requêtes + egress), 5 TB max par objet.
- **Prix** : page officielle [aws.amazon.com/s3/pricing/](https://aws.amazon.com/s3/pricing/) — contenu régional précis non extractible (rendu dynamique) ; des sources secondaires avancent ~$0,023-0,0245/GB/mois en régions UE — **à vérifier sur AWS Pricing Calculator avant décision**, non confirmé en source primaire.
- **RGPD/résidence des données** : DPA article 28 RGPD, centre de conformité dédié — [aws.amazon.com/compliance/gdpr-center/](https://aws.amazon.com/compliance/gdpr-center/), [aws.amazon.com/compliance/eu-data-protection/](https://aws.amazon.com/compliance/eu-data-protection/)
- **Dépendance fournisseur / alternatives** : protocole S3 devenu standard répliqué par la plupart des concurrents (R2, B2, Supabase Storage) — migration de données relativement aisée ; lock-in réel surtout via l'écosystème AWS (IAM/Lambda/CloudFront).

### Cloudflare R2

- **Documentation** : [developers.cloudflare.com/r2/](https://developers.cloudflare.com/r2/)
- **Compatibilité S3** : API S3-compatible pour la majorité des opérations bucket/objet standard.
- **Disponibilité France/Europe** : pas de sélection région par ville, mais réglage de « juridiction bucket » **EU jurisdiction** épinglant les données aux datacenters UE sans réplication hors UE (figé une fois défini) — [developers.cloudflare.com/r2/reference/data-location/](https://developers.cloudflare.com/r2/reference/data-location/)
- **Authentification** : jetons API R2 (SigV4) pour l'API S3-compatible ; jetons API Cloudflare pour la gestion.
- **Sandbox/test** : pas de mode dédié ; tier gratuit (10 GB inclus) + Wrangler CLI en local.
- **Webhooks** : pas de webhook HTTP direct — event notifications vers Cloudflare Queues (consommées par Worker ou pull HTTP), jusqu'à 100 règles/bucket, ~5000 messages/s — [developers.cloudflare.com/r2/buckets/event-notifications/](https://developers.cloudflare.com/r2/buckets/event-notifications/)
- **Capacités principales** : stockage S3-compatible, **egress gratuit** (différenciateur principal), classe Infrequent Access, intégration Workers/CDN.
- **Prix** ([developers.cloudflare.com/r2/pricing/](https://developers.cloudflare.com/r2/pricing/)) : Standard $0,015/GB/mois, IA $0,01/GB/mois ; opérations classe A $4,50/million (Standard), classe B $0,36/million ; egress gratuit ; free tier 10 GB-mois + 1M requêtes classe A.
- **RGPD/résidence des données** : la doc officielle présente la juridiction EU comme réponse aux « réglementations locales telles que le RGPD » — DPA spécifique non vérifié ici.
- **Dépendance fournisseur / alternatives** : faible au niveau protocole S3 ; lock-in ciblé si usage des extras Cloudflare (Workers bindings, Queues).

### Cloudinary

- **Documentation** : [cloudinary.com/documentation](https://cloudinary.com/documentation)
- **Disponibilité France/Europe** : datacenter par défaut aux États-Unis ; résidence EEA disponible **uniquement Enterprise**, coût additionnel possible (source croisée citant cloudinary.com/trust et la DPA Cloudinary).
- **Authentification** : API Key + Secret (Basic Auth ou signature SHA + timestamp) ; uploads signés côté serveur pour l'upload widget.
- **Sandbox/test** : plan Free (25 crédits/mois) en tient lieu.
- **Webhooks** : oui — notifications POST vers `notification_url`, signées HMAC (`X-Cld-Signature`/`X-Cld-Timestamp`) — [cloudinary.com/documentation/notifications](https://cloudinary.com/documentation/notifications), [cloudinary.com/documentation/notification_signatures](https://cloudinary.com/documentation/notification_signatures)
- **Capacités principales** : transformations image/vidéo à la volée, transcodage/streaming adaptatif, CDN, tags automatiques, backup vers bucket S3 propre (Plus+), gestion rôles (Advanced+).
- **Limites principales** : tarification par crédits mutualisés (1 crédit = 1000 transformations OU 1 GB storage OU 1 GB bande passante), pas de quotas séparés lisibles indépendamment.
- **Prix** ([cloudinary.com/pricing](https://cloudinary.com/pricing)) : Free $0 (25 crédits) ; Plus $99/mois (225 crédits, backup S3) ; Advanced $249/mois (600 crédits, CNAME/SSL) ; Enterprise sur devis.
- **RGPD/résidence des données** : DPA ([cloudinary.com/gdpr/dpa](https://cloudinary.com/gdpr/dpa)), SCC + EU-US DPF ; résidence EEA = option Enterprise seulement.
- **Dépendance fournisseur / alternatives** : plus élevée — URLs de transformation et syntaxe propriétaires ; migration implique re-traitement des médias. Alternatives : imgix, ImageKit, Cloudflare Images, ou stockage S3-compatible + outil de transformation (imgproxy/Sharp).

**Synthèse catégorie 12** : Supabase Storage est le choix « déjà dans le stack » avec compatibilité S3 partielle ; R2 se distingue par l'egress gratuit ; S3 reste le standard le plus complet fonctionnellement ; Cloudinary est seul spécialisé image/vidéo mais avec le lock-in le plus fort et la résidence EU la plus restrictive (Enterprise only).

---

## 13. OCR

### Google Document AI

- **Documentation** : [docs.cloud.google.com/document-ai/docs/overview](https://docs.cloud.google.com/document-ai/docs/overview) ; régions — [docs.cloud.google.com/document-ai/docs/regions](https://docs.cloud.google.com/document-ai/docs/regions) ; pricing — [cloud.google.com/document-ai/pricing](https://cloud.google.com/document-ai/pricing)
- **Disponibilité France/Europe** : multi-région `eu`, régions unitaires Londres, Francfort, Amsterdam. **Pas de région française dédiée** (pas de Paris `europe-west9`).
- **Authentification** : Application Default Credentials via compte de service (JSON), ou clé API recommandée pour tests.
- **Sandbox/test** : pas d'environnement dédié, mais quota gratuit permanent de 0-1000 pages/mois sur Enterprise Document OCR, plus test interactif en console.
- **Webhooks** : aucun mécanisme natif trouvé — opérations longue durée en polling, résultat dans Cloud Storage ; couplage Pub/Sub/Eventarc possible mais non documenté comme fonctionnalité native (non confirmé).
- **Capacités principales** : OCR générique, Form Parser, Layout Parser, Custom Extractor entraînable, parseurs préentraînés Invoice/Expense/Utility/Bank statement/Pay slip. Parseurs d'identité limités aux documents américains. Pour factures/devis BTP français : Invoice parser + Custom Extractor entraîné sur gabarits propres (pas de spécialisation France prête à l'emploi).
- **Limites principales** : taille fichier/pages max non trouvée dans la doc consultée (non confirmé).
- **Prix** ([cloud.google.com/document-ai/pricing](https://cloud.google.com/document-ai/pricing)) : Enterprise Document OCR gratuit 0-1000 pages/mois puis $1,50/1000 pages (jusqu'à 5M), $0,60/1000 au-delà ; Invoice parser $0,10/document ; Form Parser $30/1000 pages ; Layout Parser $10/1000 pages ; Custom Extractor $30/1000 pages ; Bank statement $0,75/document ; Pay slip $0,30/document.
- **RGPD/résidence des données** : Cloud DPA standard, EU GDPR/UK GDPR/Swiss FADP, suppression sous 180 jours en fin de contrat ([cloud.google.com/terms/data-processing-addendum](https://cloud.google.com/terms/data-processing-addendum)) ; couverture spécifique Document AI renvoyée à l'Annexe 4, non vérifiée en détail.
- **Dépendance fournisseur / alternatives** : écosystème GCP, format JSON propriétaire (`Document` proto).

### AWS Textract

- **Documentation** : [docs.aws.amazon.com/textract/latest/dg/what-is.html](https://docs.aws.amazon.com/textract/latest/dg/what-is.html) ; limites — [docs.aws.amazon.com/textract/latest/dg/limits.html](https://docs.aws.amazon.com/textract/latest/dg/limits.html) ; pricing — [aws.amazon.com/textract/pricing/](https://aws.amazon.com/textract/pricing/)
- **Disponibilité France/Europe** : Ireland, Londres, Frankfurt, Paris — [aws.amazon.com/textract/faqs/](https://aws.amazon.com/textract/faqs/). Tarifs EU alignés sur US East depuis 2021.
- **Authentification** : IAM (SigV4), pas de simple clé API par en-tête.
- **Sandbox/test** : Free Tier 3 mois pour nouveaux comptes (1000 pages/mois DetectDocumentText, 100 pages AnalyzeExpense/AnalyzeID).
- **Webhooks** : pas de webhook HTTP natif — opérations async publient leur statut sur SNS, à combiner avec SQS/Lambda — [docs.aws.amazon.com/textract/latest/dg/api-async-roles.html](https://docs.aws.amazon.com/textract/latest/dg/api-async-roles.html)
- **Capacités principales** : DetectDocumentText (OCR brut), AnalyzeDocument (formulaires, tableaux, requêtes, signatures), **AnalyzeExpense** (factures/reçus), AnalyzeID (passeports/permis américains uniquement). OCR/formulaires/tableaux supportent le français — **mais** écriture manuscrite, AnalyzeExpense, documents d'identité et Queries sont documentés **anglais uniquement** : limite significative pour un usage factures françaises — [aws.amazon.com/textract/faqs/](https://aws.amazon.com/textract/faqs/)
- **Limites principales** : synchrone 10 Mo/1 page (PDF/TIFF) ; async jusqu'à 500 Mo/3000 pages.
- **Prix** : DetectDocumentText $0,0015/page (≤1M/mois) ; AnalyzeDocument Forms $0,05/page ; Tables $0,015/page ; AnalyzeExpense $0,01/page ; AnalyzeID $0,025/page.
- **RGPD/résidence des données** : AWS déclare la propriété du contenu au client ; cadre DPA non approfondi au-delà de la FAQ produit.
- **Dépendance fournisseur / alternatives** : format JSON propriétaire (`Blocks`), dépendance IAM/SNS/S3 pour les flux async.

### Mindee (français)

- **Documentation** : [developers.mindee.com/docs](https://developers.mindee.com/docs), [docs.mindee.com](https://docs.mindee.com/) ; pricing — [mindee.com/pricing](https://www.mindee.com/pricing)
- **Disponibilité France/Europe** : société française (Paris). Option de **localisation du traitement** sur plans Pro/Enterprise : « Europe » / « United States » / « No Preference » (défaut) — [docs.mindee.com/models/data-processing-policies](https://docs.mindee.com/models/data-processing-policies)
- **Authentification** : clé API via en-tête dédié, confirmé dans l'OpenAPI officiel.
- **Sandbox/test** : pas d'environnements séparés dev/staging/prod, mais fonctionnalité « Live Test » recommandée + essai gratuit 14 jours sans CB.
- **Webhooks** : supportés nativement et recommandés pour la production — POST vers URL serveur du client, authentification via paramètres d'URL et validation HMAC (« Signing Secret ») — [docs.mindee.com/integrations/webhooks](https://docs.mindee.com/integrations/webhooks)
- **Capacités principales** : spécialisé documents métier dès l'origine. Invoice OCR : n° facture, dates, fournisseur/client, HT/TTC, **TVA**, IBAN/SWIFT, n° bon de commande, **lignes de détail**. Aussi reçus/dépenses et fiche de paie française — [mindee.com/product/invoice-ocr-api](https://www.mindee.com/product/invoice-ocr-api) — seul candidat des 4 avec extraction facture prête à l'emploi alignée France.
- **Limites principales** : taille fichier/page max non trouvée (non confirmé). Système crédits : 1 page = 1 crédit (1,5 avec scores de confiance).
- **Prix** (EUR, [mindee.com/pricing](https://www.mindee.com/pricing)) : Starter 24€/mois ; Pro 104€/mois (inclut localisation UE, support live chat) ; crédits à la carte 500 = 25€ (0,05€/crédit) à 25000 = 976€ (0,039€/crédit) ; Enterprise sur devis dès 500 000 crédits/an.
- **RGPD/résidence des données** : conforme RGPD, SOC 2 Type II, DPA ([mindee.com/legals/data-processing-agreement](https://www.mindee.com/legals/data-processing-agreement)), rétention par défaut 12h (configurable 1-24h), option suppression immédiate après accès, fichiers originaux jamais stockés sur disque — [docs.mindee.com/models/data-processing-policies](https://docs.mindee.com/models/data-processing-policies)
- **Dépendance fournisseur / alternatives** : format JSON propre à Mindee ; acteur plus petit qu'AWS/Google/Microsoft mais spécialisé factures/documents métier de longue date.

### Azure AI Document Intelligence

- **Documentation** : [learn.microsoft.com/azure/ai-services/document-intelligence/overview](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/overview) ; FAQ et pricing — [azure.microsoft.com/pricing/details/document-intelligence/](https://azure.microsoft.com/en-us/pricing/details/document-intelligence/)
- **Disponibilité France/Europe** : déployable en région Azure UE au choix, données traitées/stockées temporairement dans la même région. Disponibilité précise d'une région France Central pour ce service spécifique **non vérifiée**.
- **Authentification** : clé API + endpoint, ou Microsoft Entra ID / identités managées.
- **Sandbox/test** : niveau gratuit F0 : 500 pages/mois mais **seulement les 2 premières pages** de chaque document (y compris via API), fichiers max 4 Mo. Document Intelligence Studio pour test visuel.
- **Webhooks** : pas de webhook natif documenté dans l'API elle-même ; intégration via Logic Apps/Functions.
- **Capacités principales** : modèles Read (OCR), Layout, prédéfinis Invoice/Receipt/Contract/Pay stub/Bank statement/Identity/Check/Credit card, modèles personnalisés entraînables. Adéquation spécificités françaises (mentions légales BTP, TVA) non vérifiée précisément.
- **Limites principales** : F0 limité à 2 pages/document ; entraînement modèle neuronal custom : 10h gratuites puis 3$/heure.
- **Prix** : montants précis Read/Layout/Invoice **non extractibles** lors de cette recherche (rendu dynamique) — chiffres tiers non officiels (~1,50$/1000 pages Read, ~10$/1000 pages prédéfinis) **non validés en source primaire**, à reconfirmer via le calculateur Azure.
- **RGPD/résidence des données** : Microsoft sous-traitant RGPD, suppression automatique sous 24h après analyse, suppression anticipée via API dédiée (v4.0).
- **Dépendance fournisseur / alternatives** : écosystème Azure ; point différenciant — **conteneurs déconnectés** disponibles pour modèles custom et Invoice, permettant un déploiement partiellement on-premise (absent chez les 3 autres candidats).

**Points non résolus signalés par la recherche** : limites taille fichier Google Document AI et Mindee, mécanisme webhook réel Google Document AI, région Azure française spécifique, tarifs Azure exacts par page.

---

## 14. Transcription vocale / speech-to-text

### OpenAI Whisper API

- **Documentation** : [developers.openai.com/api/docs/guides/speech-to-text](https://developers.openai.com/api/docs/guides/speech-to-text)
- **Disponibilité France/Europe** : aucune restriction géographique documentée pour l'API elle-même. Une résidence de données EU existe pour d'autres produits OpenAI (Enterprise), mais **couverture de l'endpoint Transcriptions non confirmée** — pages officielles dédiées inaccessibles lors de la recherche (Cloudflare challenge / 403). À vérifier avant décision.
- **Authentification** : Bearer token (`Authorization: Bearer`).
- **Sandbox/test** : pas d'environnement dédié documenté sur la page officielle (crédit offert aux nouveaux comptes mentionné par des sources tierces, non confirmé officiellement).
- **Webhooks** : non documentés sur l'API Transcriptions — mode streaming existe mais pas de callback HTTP asynchrone natif.
- **Capacités principales** : multilingue par codes ISO (français inclus), diarisation via `gpt-4o-transcribe-diarize`, timestamps mot/segment. Pas de mention documentée de traitement spécifique du bruit de chantier.
- **Limites principales** : fichier max 25 Mo ; traduction vers l'anglais uniquement (Whisper-1) ; prompt limité à 224 tokens (Whisper-1).
- **Prix** ([platform.openai.com/docs/pricing](https://platform.openai.com/docs/pricing)) : Whisper $0,006/min ; `gpt-4o-transcribe` $0,006/min ; `gpt-4o-mini-transcribe` $0,003/min ; `gpt-transcribe` $0,0045/min ; temps réel $0,017/min ; traduction temps réel $0,034/min.
- **RGPD/résidence des données** : non confirmé pour cet endpoint précis.
- **Dépendance fournisseur / alternatives** : modèle Whisper publié en open-weight par OpenAI, réhébergé par des tiers (Groq, Azure AI Speech, AWS, auto-hébergement) — réduit le lock-in sur le modèle sous-jacent même si l'API OpenAI reste propriétaire.

### Google Speech-to-Text

- **Documentation** : [docs.cloud.google.com/speech-to-text/v2/docs](https://docs.cloud.google.com/speech-to-text/v2/docs)
- **Disponibilité France/Europe** : résidence multi-région et mono-région en V2 (V1 : multi-région seulement), régions européennes (ex. Belgique) documentées — [docs.cloud.google.com/speech-to-text/v2/docs/migration](https://docs.cloud.google.com/speech-to-text/v2/docs/migration)
- **Authentification** : clé API, OAuth client ID, ou compte de service (recommandé).
- **Sandbox/test** : palier gratuit 60 min/mois confirmé ([cloud.google.com/speech-to-text/pricing](https://cloud.google.com/speech-to-text/pricing)).
- **Webhooks** : aucun mécanisme natif — reconnaissance asynchrone (&gt;60s, jusqu'à 480 min) en opération longue durée (polling), ou contournement Cloud Storage Trigger + Cloud Functions.
- **Capacités principales** : français (fr-FR) supporté par plusieurs modèles (chirp_3, chirp_2, chirp, chirp_telephony, long, short), ponctuation auto, diarisation, confiance mot par mot selon modèle. Pas de doc officielle sur traitement du bruit de chantier.
- **Limites principales** : synchrone recommandé &lt;60s ; asynchrone plafonné à 480 min.
- **Prix** : V2 dès $0,016/min (paliers dégressifs jusqu'à ~$0,0024/min gros volume), V1 dès $0,024/min, 60 min/mois gratuites. Grille complète par palier non extraite proprement (rendu dynamique) — à vérifier en console.
- **RGPD/résidence des données** : couvert par cadre résidence des données GCP général (V2 régions Europe), audit logging et clés gérées par le client en V2.
- **Dépendance fournisseur / alternatives** : forte intégration GCP (IAM, Cloud Storage), modèles Chirp propriétaires.

### Deepgram

- **Documentation** : [developers.deepgram.com/docs](https://developers.deepgram.com/docs)
- **Disponibilité France/Europe** : endpoint dédié EU (`api.eu.deepgram.com`), sans liste d'attente ni changement de facturation/auth — [developers.deepgram.com/trust-security/data-privacy-compliance](https://developers.deepgram.com/trust-security/data-privacy-compliance), [deepgram.com/learn/deepgram-eu-endpoint-now-generally-available](https://deepgram.com/learn/deepgram-eu-endpoint-now-generally-available)
- **Authentification** : header `Authorization: Token &lt;API_KEY&gt;`.
- **Sandbox/test** : playground public sans inscription (60 min gratuites) + $200 crédit à l'inscription (~45 000 minutes) — [deepgram.com/pricing](https://deepgram.com/pricing)
- **Webhooks** : natifs via paramètre `callback` (HTTP/HTTPS pré-enregistré, HTTP/HTTPS/WS/WSS streaming), auth par Basic Auth ou header `dg-token`, retries jusqu'à 10 fois/30s — [developers.deepgram.com/docs/callback](https://developers.deepgram.com/docs/callback)
- **Capacités principales** : modèle Nova-3 multilingue, code-switching entre 10 langues incluant le français. Robustesse au bruit mise en avant marketing mais non quantifiée officiellement.
- **Limites principales** : formats/taille max non explorés en détail dans cette recherche — à vérifier.
- **Prix** ([deepgram.com/pricing](https://deepgram.com/pricing)) : pré-enregistré mono-langue $0,0043/min (PAYG) / $0,0036/min (Growth) ; multilingue $0,0052/$0,0043 ; streaming mono $0,0048/$0,0042 ; streaming multilingue $0,0058/$0,0050. Enterprise sur devis (rétention zéro, SLA).
- **RGPD/résidence des données** : « GDPR ready », HIPAA, SOC 2 Type II sur tous les plans payants, endpoint EU dédié.
- **Dépendance fournisseur / alternatives** : modèles Nova propriétaires, mais API REST/WebSocket standard facilitant la portabilité.

### ElevenLabs Scribe

- **Documentation** : [elevenlabs.io/docs/overview/capabilities/speech-to-text](https://elevenlabs.io/docs/overview/capabilities/speech-to-text)
- **Disponibilité France/Europe** : résidence EU via `api.eu.residency.elevenlabs.io`, **réservée aux clients Enterprise** — [elevenlabs.io/docs/overview/administration/data-residency](https://elevenlabs.io/docs/overview/administration/data-residency)
- **Authentification** : header `xi-api-key`.
- **Sandbox/test** : pas de tier gratuit pur pay-as-you-go pour la transcription ; heures incluses dès le plan Starter (6$/mois, 4,5h). Pas de sandbox technique dédié identifié.
- **Webhooks** : confirmés — résultats de transcription asynchrone envoyables vers des webhooks configurés côté interface.
- **Capacités principales** : français parmi 90+ langues, diarisation jusqu'à 32 locuteurs, timestamps au mot, détection d'entités (65 types), keyterm prompting (jusqu'à 1000 termes), détection automatique de langue. Modèle « Scribe v2 Medical » dédié au vocabulaire clinique.
- **Limites principales** : fichier max 3 Go, durée max ~10h ; add-ons majorent le coût unitaire de 20-30 % chacun.
- **Prix** ([elevenlabs.io/pricing/api](https://elevenlabs.io/pricing/api)) : Scribe v2 $0,22/heure (~$0,0037/min) ; Scribe v2 Realtime $0,39/heure ; détection d'entités +$0,07/h ; keyterm prompting +$0,05/h. Abonnements : Starter 6$/mois (4,5h) à Business 990$/mois (1359h).
- **RGPD/résidence des données** : conçu pour aligner sur le RGPD, DPA public sans compte Enterprise ([elevenlabs.io/dpa](https://elevenlabs.io/dpa)), EU-US DPF actif, mode « Zero Retention » disponible. Résidence EU stricte = Enterprise only.
- **Dépendance fournisseur / alternatives** : modèle Scribe propriétaire, pas d'option d'auto-hébergement.

**Synthèse catégorie 14** : les 4 candidats couvrent le français ; Deepgram offre la résidence EU nativement sur tous les plans payants sans surcoût, ElevenLabs la réserve à l'Enterprise, Google l'intègre au cadre GCP standard, OpenAI reste à clarifier sur ce point. Webhooks natifs chez Deepgram et ElevenLabs seulement. Aucune des 4 pages officielles ne quantifie la robustesse au bruit de chantier — point à tester empiriquement avant choix.

---

## 15. LLM providers

*Note : noms de modèles/tarifs reflètent l'état des catalogues au 23 septembre 2026 ; à revérifier sur les pages de pricing officielles au moment de l'implémentation.*

### Anthropic Claude

- **Documentation** : [platform.claude.com/docs/](https://platform.claude.com/docs/)
- **Disponibilité France/Europe** : l'API directe (api.anthropic.com) traite/stocke les données **aux États-Unis** — pas de résidence UE native. Pour résidence UE/EEE : passer par **AWS Bedrock, Google Vertex AI ou Microsoft Foundry** avec sélection de région — [claude.com/regional-compliance](https://claude.com/regional-compliance)
- **Authentification** : clé API (`x-api-key`), ou OAuth via CLI officiel, Workload Identity Federation.
- **Sandbox/test** : Workbench dans la Console pour tester des prompts ; pas de free tier API documenté (le plan gratuit concerne l'app consommateur Claude.ai, pas l'API) — [claude.com/pricing](https://claude.com/pricing)
- **Webhooks** : disponibles pour la Batch API uniquement selon sources secondaires convergentes (`webhook_url`, HMAC-SHA256, retries 24h) — **non confirmé en doc officielle primaire** dans cette recherche, à vérifier avant implémentation. Pas de webhook pour les appels synchrones (polling requis).
- **Capacités principales** : tool use/function calling natif (appels parallèles), support français solide (non chiffré précisément), contexte jusqu'à 1M tokens selon modèle.
- **Limites principales** : pas de résidence UE native sur l'API directe — point structurant pour données clients UE.
- **Prix** ([claude.com/pricing](https://claude.com/pricing), /1M tokens) : Haiku ~$1/$5 ; Sonnet ~$2/$10 ; Opus ~$4-5/$20-25. Batch API -50 % ; cache de prompt réduit les coûts d'input répété.
- **RGPD/résidence des données** : DPA avec SCC inclus automatiquement (API/Enterprise), données non utilisées pour l'entraînement par défaut. Résidence UE possible **uniquement via Bedrock/Vertex/Foundry**. SOC 2 Type 2, ISO 27001/27017/27018, CSA STAR.
- **Dépendance fournisseur / alternatives** : modéré en usage direct (format propriétaire) ; réduit via une couche d'abstraction (LangChain, LiteLLM).

### OpenAI

- **Documentation** : [developers.openai.com/api/docs/](https://developers.openai.com/api/docs/)
- **Disponibilité France/Europe** : **résidence UE disponible** — créer un nouveau projet région Europe pointant vers `api.openai.eu/v1` (conversion a posteriori impossible), données (inputs/outputs/traitement intermédiaire) restant sur datacenters Azure UE — [openai.com/index/introducing-data-residency-in-europe/](https://openai.com/index/introducing-data-residency-in-europe/)
- **Authentification** : clé API (`Authorization: Bearer`), gestion par projet.
- **Sandbox/test** : Playground disponible sur la plateforme développeur.
- **Webhooks** : disponibles nativement — endpoint public, secret de signature, couvrent réponses background (`response.completed`), Batch API, fine-tuning — [developers.openai.com/api/docs/guides/webhooks](https://developers.openai.com/api/docs/guides/webhooks)
- **Capacités principales** : function calling mature (standard de facto largement copié), support français solide, écosystème d'outils large.
- **Limites principales** : activer la résidence UE exige une reconfiguration de projet (pas automatique sur comptes existants).
- **Prix** ([developers.openai.com/api/docs/pricing](https://developers.openai.com/api/docs/pricing), /1M tokens) : modèle économique ~$0,10-0,20/$0,50-1,20 ; intermédiaire ~$2-4/$10-20 ; flagship $10/$50. Cache d'input ~10 % du tarif standard ; Batch -50 %.
- **RGPD/résidence des données** : données non utilisées pour l'entraînement sauf opt-in ; certifications CSA STAR, SOC 2 Type 2. La doc précise que la résidence seule ne suffit pas à la conformité RGPD (base légale, DPA, garanties de transfert restent à la charge du client).
- **Dépendance fournisseur / alternatives** : function calling quasi-standard de facto (repris par Mistral/Google) limitant un peu le lock-in technique ; verrouillage commercial classique d'un fournisseur propriétaire US.

### Mistral AI (français)

- **Documentation** : [docs.mistral.ai/](https://docs.mistral.ai/)
- **Disponibilité France/Europe** : entreprise française (Paris, 2023), régie par le droit UE/RGPD. **Données hébergées dans l'UE par défaut** ; endpoint US disponible en option. Offre entreprise avec infrastructure certifiée **SecNumCloud (ANSSI)** via Outscale — [help.mistral.ai/en/articles/347629-where-do-you-store-my-data-or-my-organization-s-data](https://help.mistral.ai/en/articles/347629-where-do-you-store-my-data-or-my-organization-s-data)
- **Authentification** : clé API générée depuis Studio (console.mistral.ai).
- **Sandbox/test** : Playground dans Studio pour tester les modèles, mode Free pour activer Studio sans frais.
- **Webhooks** : **absents** — Batch API poll-only selon recherche croisée (non confirmé en doc officielle primaire dans cette recherche, à vérifier sur `docs.mistral.ai/studio/batch-processing`).
- **Capacités principales** : function/tool calling natif sur la gamme généraliste (Mistral Large 3, Medium 3.5, Small 3.2/4) et modèles spécialisés (Codestral, Devstral, Magistral, Ministral). Français langue native de l'éditeur — [docs.mistral.ai/capabilities/function_calling/](https://docs.mistral.ai/capabilities/function_calling/)
- **Limites principales** : gamme moins « frontier » que Claude/GPT/Gemini sur benchmarks de raisonnement complexe (non vérifié empiriquement) ; écosystème tiers plus restreint ; absence de webhooks natifs.
- **Prix** ([docs.mistral.ai/inference/pricing](https://docs.mistral.ai/inference/pricing), /1M tokens) : Ministral 3 $0,10-0,20/$0,10-0,20 ; Small 4 $0,15/$0,60 ; Codestral $0,30/$0,90 ; Large 3 $0,50/$1,50 ; Medium 3.5 $1,50/$7,50. Cache ~10 % du tarif standard.
- **RGPD/résidence des données** : résidence UE par défaut, cadre RGPD natif. Point de vigilance : si `endpoint=` n'est pas explicitement fixé, les requêtes peuvent router vers `api.mistral.ai` (US) sans avertissement — à contrôler techniquement si la résidence UE est contractuelle.
- **Dépendance fournisseur / alternatives** : positionnement « souveraineté numérique européenne » pertinent pour un SaaS français BTP ; lock-in technique comparable aux autres, mais ancrage juridictionnel UE réduit le risque réglementaire.

### Google Gemini

- **Documentation** : [ai.google.dev/gemini-api/docs/](https://ai.google.dev/gemini-api/docs/) (API grand public) ; version entreprise via Vertex AI.
- **Disponibilité France/Europe** : l'API Gemini « consumer » traite les données globalement, pas de garantie régionale. Pour résidence UE : passer par **Vertex AI** (`europe-west1` Belgique, `europe-west4` Pays-Bas). Distinction Google entre DRZ (résidence au repos) et MLP (traitement ML en région) — les deux nécessaires pour une localisation UE complète, à valider directement sur doc Vertex AI officielle avant usage contractuel (source croisée, non confirmée en primaire ici).
- **Authentification** : clé API (`GEMINI_API_KEY`), migration en cours vers « auth keys » liées à des comptes de service. Pour Vertex AI : auth GCP standard (IAM/ADC).
- **Sandbox/test** : Google AI Studio.
- **Webhooks** : disponibles nativement — statiques (niveau projet) et dynamiques (niveau requête), couvrant les opérations longues : `batch.succeeded/expired/failed`, `interaction.*`, `video.generated` — [ai.google.dev/gemini-api/docs/webhooks](https://ai.google.dev/gemini-api/docs/webhooks)
- **Capacités principales** : function calling natif complet (appels parallèles, compositionnels), combinable avec outils Google (Search, Maps), SDK multi-langage, français bien supporté.
- **Limites principales** : meilleure garantie de résidence/traitement UE réservée à Vertex AI (entreprise), pas à l'API Gemini grand public.
- **Prix** ([ai.google.dev/gemini-api/docs/pricing](https://ai.google.dev/gemini-api/docs/pricing), /1M tokens) : Flash-Lite ~$0,25-0,30/$1,50-2,50 ; Flash ~$0,75-1,50/$3,75-9,00 (tarif promotionnel jusqu'au 31/12/2026) ; Pro (≤200K tokens) $2,00/$12,00, doublé au-delà. Batch -50 %.
- **RGPD/résidence des données** : Vertex AI = DPA complet avec clauses RGPD spécifiques, rétention zéro en option, inférence UE-only pour charges éligibles — posture la plus complète du trio Google. Point de vigilance : mise en cache implicite (TTL 24h par défaut), nécessitant configuration explicite pour rétention zéro réelle (source croisée, à confirmer sur doc Vertex AI officielle).
- **Dépendance fournisseur / alternatives** : significative si adoption complète de l'écosystème GCP pour la conformité UE ; l'API Gemini simple est plus légère mais avec une posture de résidence plus faible.

**Synthèse résidence UE (point structurant, catégorie 15)** :

| Candidat | API directe/standard | Offre entreprise/cloud |
|---|---|---|
| Claude | Non (US par défaut) | Oui via Bedrock/Vertex/Foundry |
| OpenAI | Oui via `api.openai.eu` (reconfiguration requise) | — |
| Mistral | **Oui par défaut** | Oui, renforcé (SecNumCloud) |
| Gemini | Non garanti | Oui via Vertex AI |

---

## 16. Vision/image AI pour analyse de photos terrain

### Claude vision (Anthropic)

- **Documentation** : [platform.claude.com/docs/en/build-with-claude/vision](https://platform.claude.com/docs/en/build-with-claude/vision)
- **Disponibilité France/Europe** : pas de résidence UE native sur l'API directe (infrastructure US). Pour résidence UE : AWS Bedrock (Frankfurt, Ireland, Paris, Stockholm) ou Google Vertex AI en régions UE. DPA + SCC inclus automatiquement dans les CGU commerciales. Option Zero Data Retention pour clients entreprise (source croisée : compound.law/en-DE/tools/anthropic-api/).
- **Authentification** : clé API (`x-api-key`) + en-tête `anthropic-version`.
- **Sandbox/test** : pas d'environnement de test distinct — Playground Console existe mais chaque appel API est facturé au tarif standard.
- **Webhooks** : **absents pour l'API standard**. Batch API documentée avec **polling uniquement** (`GET /v1/messages/batches/{id}`) dans la doc officielle lue intégralement — aucune mention de `webhook_url` trouvée en source primaire, malgré des affirmations tierces non confirmées — [platform.claude.com/docs/en/build-with-claude/batch-processing](https://platform.claude.com/docs/en/build-with-claude/batch-processing)
- **Capacités principales** : reconnaissance d'objets/texte (OCR), interprétation de graphiques, compréhension de documents, raisonnement libre sur image, comparaison multi-images, bounding box approximatives. LLM multimodal généraliste, pas un catalogue de détection fixe.
- **Limites principales** (documentées) : JPEG/PNG/GIF/WebP (pas d'animation) ; 10 Mo max (API directe), 5 Mo (Bedrock/GCP) ; 8000×8000 px max ; jusqu'à 100-600 images/requête selon modèle ; **comptage approximatif** d'objets (pertinent pour compter du matériel sur chantier) ; **raisonnement spatial/localisation approximatif** — coordonnées à vérifier avant usage critique ; ne peut pas identifier des personnes nommément ; images non conservées après traitement, non utilisées pour l'entraînement.
- **Prix** ([claude.com/pricing](https://claude.com/pricing)) : facturation par « visual tokens » (patch 28×28 px). Sonnet 5 : $2/$10 par MTok ; Opus 5.5 : $4/$20 ; Haiku 4.5 : $1/$5. Image 1000×1000 px ≈ 1296 tokens. Batch -50 %. Option « US-only inference » +10 %.
- **RGPD/résidence des données** : DPA + SCC standard, pas de résidence UE native sur l'API directe.
- **Dépendance fournisseur / alternatives** : format de requête propre à Anthropic mais structurellement proche des autres LLM multimodaux — portage faisable via réécriture de prompts.

### GPT-4o/GPT-5 vision (OpenAI)

- **Documentation** : [developers.openai.com/api/docs/guides/images-vision](https://developers.openai.com/api/docs/guides/images-vision)
- **Disponibilité France/Europe** : résidence UE disponible via endpoint dédié `eu.api.openai.com`, datacenters Microsoft Azure Europe, zero data retention par défaut pour ces requêtes (source citée, accès direct bloqué en 403 lors de la recherche, repris via résumé — à revérifier : [openai.com/index/introducing-data-residency-in-europe/](https://openai.com/index/introducing-data-residency-in-europe/)).
- **Authentification** : clé API (Bearer token).
- **Sandbox/test** : pas d'environnement distinct — production uniquement.
- **Webhooks** : oui, natifs ([platform.openai.com/docs/api-reference/webhook-events](https://platform.openai.com/docs/api-reference/webhook-events)) — fin de réponse background, complétion batch, fin fine-tuning, alertes sécurité.
- **Capacités principales** : description d'image, OCR, identification d'objets, analyse formes/couleurs/textures, raisonnement libre — comparable à Claude vision.
- **Limites principales** (documentées) : PNG/JPEG/WEBP/GIF non-animé ; jusqu'à 512 Mo payload, 1500 images/requête ; **OCR dégradé sur alphabets non latins** ; **faible en raisonnement spatial** ; **comptage approximatif** d'objets ; performance dégradée sur images pivotées ; faible sur imagerie médicale.
- **Prix** ([developers.openai.com/api/docs/pricing](https://developers.openai.com/api/docs/pricing)) : GPT-4o $2,50/$10 par MTok (cache $1,25) ; GPT-5 $1,25/$10 (cache $0,125) ; GPT-4o-mini $0,15/$0,60. Gamme évoluant vite — vérifier le modèle exact à l'implémentation.
- **RGPD/résidence des données** : DPA disponible, résidence UE via endpoint dédié avec zero data retention pour requêtes en région ; logs d'abus conservés jusqu'à 30 jours hors résidence UE/ZDR.
- **Dépendance fournisseur / alternatives** : format Chat Completions/Responses API propriétaire.

### Google Cloud Vision AI

- **Documentation** : [cloud.google.com/vision/docs](https://cloud.google.com/vision/docs)
- **Disponibilité France/Europe** : Google Cloud propose des engagements de résidence au niveau plateforme (« EU Data Boundary ») et le DPA Cloud mentionne des engagements de localisation par service (Appendice 4). **Aucune confirmation primaire d'un endpoint régional UE dédié pour Vision API spécifiquement** trouvée (page attendue en 404) — à vérifier avant de considérer la résidence UE comme acquise pour ce service précis.
- **Authentification** : clé API, compte de service (recommandé), ou OAuth 2.0 — [docs.cloud.google.com/vision/docs/authentication](https://docs.cloud.google.com/vision/docs/authentication)
- **Sandbox/test** : pas de sandbox dédié ; crédit d'essai $300 GCP + quota gratuit 1000 unités/mois font office de test à faible enjeu (reste de la production réelle).
- **Webhooks** : pas de webhook natif pour appels synchrones ; opérations async en long-running operations (polling) ; notification quasi-webhook possible via Pub/Sub + Cloud Functions (pattern d'intégration, pas fonctionnalité native).
- **Capacités principales** : détection d'étiquettes, **localisation d'objets avec bounding box** (catalogue prédéfini), OCR, logos, repères, visages, contenu inapproprié, propriétés d'image. **Vision par ordinateur classique** (classification/détection sur catalogue fixe) — **pas de raisonnement libre**, pas de détection de défauts BTP spécifiques sans AutoML Vision/Vertex AI (modèle personnalisé, coût/effort supplémentaires).
- **Limites principales** ([docs.cloud.google.com/vision/docs/supported-files](https://docs.cloud.google.com/vision/docs/supported-files)) : JPEG/PNG8/24/GIF/BMP/WEBP/RAW/ICO/PDF/TIFF ; 20 Mo max fichier, 10 Mo requête JSON ; résolution min recommandée 640×480 ; limite OCR 75 millions de pixels (redimensionnement auto au-delà).
- **Prix** ([cloud.google.com/vision/pricing](https://cloud.google.com/vision/pricing)) : par tranche de 1000 unités, 1000 premières unités/mois gratuites. 1001-5M unités/mois : Label Detection $1,50, Object Localization $2,25, Text/Document Text Detection $1,50, Face/Landmark/Logo/Image Properties $1,50 ; dégressif au-delà de 5M. Safe Search gratuit combiné à Label Detection.
- **RGPD/résidence des données** : DPA Cloud standard, clauses GDPR/UK GDPR/Swiss FADP, suppression sous 180 jours en fin de contrat, ISO 27001/SOC 2/SOC 3. Engagements de localisation précis pour Vision AI renvoyés à l'Appendice 4, non vérifiés en détail.
- **Dépendance fournisseur / alternatives** : schéma de réponse propre à Google ; portage vers AWS Rekognition/Azure AI Vision demande réécriture client mais concept transposable.

### Gemini vision (Google, complément)

Ajouté à titre de complément — distinct de Vision AI classique (détection catalogue fixe).

- **Documentation** : [ai.google.dev/gemini-api/docs/image-understanding](https://ai.google.dev/gemini-api/docs/image-understanding)
- **Capacités principales** : légendage et Q&A sur image, **bounding box**, **segmentation** (masques/contours), classification et **raisonnement libre** sans entraînement spécialisé — combine raisonnement type LLM (comme Claude/GPT) et sorties structurées type détection (comme Vision AI). Pertinent pour identification de matériel + jugement libre (ex. conformité d'un raccordement).
- **Limites** : formats PNG/JPEG/WEBP/HEIC/HEIF ; jusqu'à 3600 images/requête, tuiles 768×768 px (258 tokens/tuile), coordonnées normalisées [0,1000], entrée base64 limitée à 20 Mo (au-delà : Files API).
- **Pricing/résidence UE/auth/sandbox** : non vérifiés en détail dans cette recherche (budget de recherche épuisé) — à documenter séparément si Gemini vision devient candidat sérieux plutôt que simple complément.

**Lacunes méthodologiques signalées par la recherche, catégorie 16** : webhooks Claude (doc officielle = polling uniquement, sources tierces contradictoires non retenues) ; résidence UE dédiée Google Vision AI (404 sur page attendue) ; page officielle OpenAI résidence UE (accès bloqué, repris via résumé) ; Gemini vision pricing/EU/auth non creusés.

---

## 17. Catalogues fabricants/distributeurs BTP

**Constat général** : contrairement aux catégories API SaaS classiques, ce secteur ne présente pas d'API candidate unique évidente. Il s'agit d'un écosystème de **standards d'échange de données produit** (souvent en fichiers XML/EDI plus qu'en API REST moderne), plus quelques initiatives API B2B chez les grands distributeurs, encore peu documentées publiquement.

### Standards de classification et d'échange de catalogues

**BMEcat** — format XML d'échange de catalogues électroniques (données produit, prix, EAN, descriptions techniques/commerciales/packaging), créé en 1999 avec l'association allemande BME, l'un des standards e-commerce B2B les plus répandus avec GS1 XML. Pas un standard sectoriel BTP dédié, mais utilisé par des fabricants du secteur, y compris électrotechnique/CVC. Pas d'API au sens SaaS — fichiers échangés point à point ou via PIM. Aucun registre centralisé BMEcat pour le BTP français identifié.
Sources : [weidmuller.com — BMEcat](https://www.weidmuller.com/en/service/electronics_catalogue_in_bmecat_and_other_formats.jsp), [etim.ch/fr/classification/bmecat](https://etim.ch/fr/classification/bmecat), [ide.es/eng/news/bmecat-format-according-to-etim-standards](https://ide.es/eng/news/bmecat-format-according-to-etim-standards)

**ETIM (ETIM International / ETIM France)** — classification technique taxinomique internationale gérée par ETIM International (Pays-Bas), déclinaison française ETIM France (association loi 1901, Paris). Couverture confirmée : chauffage, ventilation, climatisation, plomberie, matériaux de construction — donc pertinent CVC/fumisterie. Version française ETIM 10.0 publiée le 7 avril 2025. Outils d'accès : CMT (Classification Management Tool, base en ligne publique), une **API documentée via Swagger** en accès libre sur le portail ETIM, outil de certification BMEcat et TD Bear/ETIM Manager (réservés aux adhérents), ETIM Viewer (mobile). Zone d'ombre : authentification précise, sandbox, coût/licence de l'API — non trouvés publiquement, probablement réservés membres/éditeurs partenaires.
Sources : [etim-france.fr/qui-sommes-nous/](https://www.etim-france.fr/qui-sommes-nous/), [etim-france.fr/classification/format-echange-donnees/](https://www.etim-france.fr/classification/format-echange-donnees/), [etim-france.fr/outils/](https://www.etim-france.fr/outils/), [interactiv-technologies.com](https://www.interactiv-technologies.com/fr/sortie-officielle-detim-10-0-version-francaise/)

**GS1 France / GDSN (fiche produit bâtiment)** — fiche produit GS1 bâtiment lancée en octobre 2017 (19 attributs obligatoires logistiques + 9 attributs sectoriels + données consommateur), diffusée via le réseau mondial GDSN (data pools certifiés, synchronisation sécurisée sans ressaisie). Adoption initiée Belgique/Luxembourg/Pays-Bas (250+ fournisseurs), GS1 France présent depuis 20 ans (2 500 membres tous secteurs). GS1 anime aussi une « Communauté d'Intérêt Construction » (GTIN, GLN, SSCC, QR Code augmenté, Passeport Produit Numérique). Accès technique via data pool certifié GDSN (abonnement), pas d'API publique ouverte.
Sources : [gs1.fr/fiche-produit-gs1](https://www.gs1.fr/fiche-produit-gs1), [gs1.fr/reseau-gdsn-canal-lechange-dinformations-produit](https://www.gs1.fr/reseau-gdsn-canal-lechange-dinformations-produit), [gs1.fr/vos-secteurs-dactivite/ensemble-faconnons-lavenir-construction](https://www.gs1.fr/vos-secteurs-dactivite/ensemble-faconnons-lavenir-construction)

**Edoni et Fab-Dis** (référentiels sectoriels français négoce BTP) — deux standards français dédiés à la distribution BTP/quincaillerie/matériel électrique, distincts de GS1 mais convergents avec lui. Edoni : créé en 1986, fédère négociants/fournisseurs quincaillerie/fournitures industrielles/matériaux de construction autour de l'EDI, exploite ~90 % des standards GS1, accord de partenariat GS1 France/Edoni signé en 2018. Fab-Dis : lancé fin 2014 par la filière matériel électrique, utilisé par **1 200 à 1 500 fabricants/distributeurs** en France (électrique, quincaillerie, sanitaire-chauffage, outillage), exploitant 80 %+ des standards GS1 ; depuis la version 2.3 (2019), un onglet dédié aux données ETIM existe. **Constat clé** : Saint-Gobain Distribution (maison mère Cedeo/Point.P/Brossette) exploite les trois référentiels (GS1, Edoni, Fab-Dis) en parallèle — signe de fragmentation persistante plutôt que d'un standard unique. Limite : référentiels B2B fermés (fichiers/EDI entre adhérents), pas d'API ouverte pour éditeurs SaaS tiers.
Sources : [bati.zepros.fr — Le négoce parlera-t-il le même langage](https://bati.zepros.fr/edi-le-negoce-parlera-t-il-enfin-le-meme-langage---1938), [gs1.fr — accord GS1/Edoni](https://www.gs1.fr/communique-presse/gs1-france-edoni-signent-accord-partenariat), [tenorsolutions.com — Qu'est-ce que le FAB-DIS](https://tenorsolutions.com/quest-ce-que-le-fab-dis/), [lemoniteur.fr](https://www.lemoniteur.fr/article/gs1-france-futur-concurrent-de-fab-dis-et-d-edoni.937944)

**Edibatec** — association française (1993), base de données technique pour outils de calcul thermique/prescription (isolation, enveloppe, menuiserie, vitrage, générateurs chauffage/ECS/climatisation), utilisée par des centaines de bureaux d'études via logiciels métiers. Orienté données techniques réglementaires (RE2020) plutôt que catalogue commercial prix/stock — potentiellement utile pour un futur module de calcul thermique SUPORDO. Tarifs/accès éditeur tiers non documentés publiquement.
Source : [edibatec.org](https://www.edibatec.org/)

**Protocoles punch-out génériques** (transversaux, non spécifiques BTP) — **OCI (Open Catalog Interface)**, développé par SAP, et **cXML** (Ariba, Coupa) sont des standards de catalogue « punch-out » connectant système d'achat acheteur et e-commerce fournisseur, largement utilisés en e-procurement B2B. Probablement le mécanisme technique réel derrière les intégrations ERP de Rexel/Cedeo évoquées ci-dessous, mais leur usage effectif chez ces distributeurs n'est pas confirmé publiquement.
Sources : [en.wikipedia.org/wiki/Open_Catalog_Interface](https://en.wikipedia.org/wiki/Open_Catalog_Interface), [oxalys.fr — Catalogue Punch-Out](https://www.oxalys.fr/blog/procure-to-pay/catalogue-punch-out-une-solution-cle-en-main-de-le-procurement/)

*(GALIA, standard EDI spécifique au secteur automobile français, a été écarté explicitement comme fausse piste — sans lien avec le BTP.)*

### Distributeurs CVC/fumisterie français — API pour intégration tierce

- **Rexel France** — seul distributeur avec une offre API publiquement annoncée : « Solutions Achats Connectées », espace API (`achatconnect.rexelservices.fr`) pour récupération de prix, stocks, délais de livraison, informations produit, et passation de commande depuis un ERP/solution d'achat tiers, conditions tarifaires négociées propres au client. Authentification, sandbox, tarification et mentions RGPD **non publiées publiquement** — accès semble conditionné à une relation commerciale existante. Source : [rexel.fr/frx/solutions/solutions_achats_connectees/api](https://www.rexel.fr/frx/solutions/solutions_achats_connectees/api)
- **Cedeo** (Saint-Gobain Distribution Bâtiment) — sanitaire/chauffage/plomberie/électricité, ~30 000 produits, 430 points de vente ; solution « e-procurement » présentée pour grands comptes. **Aucune documentation d'API publique** trouvée pour intégration tierce. Source : [cedeo.fr/e-procurement](https://www.cedeo.fr/e-procurement)
- **Point.P, Brossette, Frans Bonhomme** (Saint-Gobain Distribution Bâtiment) — **aucune API publique documentée trouvée** pour ces trois enseignes (Point.P : site en erreur HTTP 403 lors de la vérification, information non vérifiable).
- **Fumisterie/poêles-cheminées (Poujoulat)** — leader européen conduits de fumée/cheminées, fonctionne via un réseau de distributeurs physiques régionaux (Asturienne, Larivière, Coaxel). Un « Espace Pro » existe mais nécessite une connexion (portail revendeur classique) — **aucune mention d'API, de flux catalogue, de prix ou de stock pour intégration tierce**. Sous-secteur qui semble le moins digitalisé de tous ceux investigués sur ce point. Source : [poujoulat.fr](https://www.poujoulat.fr)

### Synthèse décision — catégorie 17

1. Aucun standard unique ne domine : ETIM (classification), BMEcat (format d'échange), GS1/GDSN (identifiants), Edoni et Fab-Dis (référentiels franco-français) coexistent, avec une convergence engagée mais incomplète depuis 2018.
2. Rexel est le seul distributeur investigué avec une offre API B2B formalisée et publiquement annoncée — détails techniques (auth, sandbox, RGPD, prix) à obtenir par contact commercial direct.
3. Cedeo, Point.P, Brossette, Frans Bonhomme (Saint-Gobain Distribution) et le secteur fumisterie (Poujoulat) n'ont **aucune API publique tierce documentée** — intégration probable via EDI/Fab-Dis/GS1 classiques, pas via API REST moderne.
4. **Implication architecture pour SUPORDO** : pas réaliste de prévoir une intégration catalogue temps réel multi-fournisseurs en V1 — la donnée catalogue devra rester saisie/importée manuellement (CSV, BMEcat si le fabricant le propose), sauf partenariat spécifique à explorer avec Rexel.

---

## 18. Météo

### Météo-France (portail API officiel)

Deux points d'entrée coexistent : `portail-api.meteofrance.fr` (portail API technique, inscription + token) et `meteo.data.gouv.fr` / `donneespubliques.meteofrance.fr` (données publiques, référencées aussi sur data.gouv.fr).

- **Disponibilité France/Europe** : service national français, France métropolitaine + outre-mer.
- **Authentification** : compte sur le portail (email + mot de passe), abonnement gratuit par API, token d'accès à durée de vie courte (~1h) à régénérer ; absence/invalidité de token → `401 Unauthorized`.
- **Sandbox/test** : « mode découverte » permettant de tester les API en ligne avant intégration.
- **Webhooks** : aucune mention trouvée — modèle pull uniquement (interrogation active de l'API).
- **Capacités principales** : API Bulletin Vigilance (niveau de danger par département, JSON + 3 vignettes PNG cartes nationales, quota 60 req/min, SLA 99,9 %) ; API Données climatologiques (historique) ; API Package Observations (temps réel stations) ; large volume de prévisions/climatologie auparavant payant passé en accès gratuit sous licence Etalab.
- **Offre commerciale dédiée BTP** : `services.meteofrance.com/btp` propose un « suivi météorologique de chantier » (alertes rafales de vent &gt; 60 km/h, notifications SMS/email, alertes foudre/pluie temps réel) — produit commercial distinct du portail open data, pertinent si SUPORDO veut une brique clé en main plutôt que construire sur l'API brute.
- **Limites principales** : quota 60 req/min sur Vigilance (autres API non quantifiées) ; token à courte durée de vie ; documentation dispersée entre plusieurs portails.
- **Prix** : gratuit pour les API open data après inscription ; l'offre pro BTP est probablement payante mais **aucun tarif public trouvé**.
- **RGPD/résidence des données** : **non documenté explicitement** dans les pages consultées ; résidence France présumée (établissement public) mais non confirmée par une mention officielle.
- **Dépendance fournisseur / alternatives** : source institutionnelle unique pour la vigilance météo réglementaire française (pas d'équivalent avec la même légitimité) ; substituable par OpenWeatherMap pour des prévisions générales non réglementaires.

Sources : [confluence-meteofrance.atlassian.net — Guide de démarrage rapide](https://confluence-meteofrance.atlassian.net/wiki/spaces/OpenDataMeteoFrance/pages/1447788546/Guide+de+d+marrage+rapide+d+couvrir+les+APIs+de+M+t+o-France), [donneespubliques.meteofrance.fr](https://donneespubliques.meteofrance.fr/), [data.gouv.fr — Météo-France](https://www.data.gouv.fr/organizations/meteo-france), [API Bulletin Vigilance](https://www.data.gouv.fr/dataservices/api-bulletin-vigilance), [services.meteofrance.com/btp](https://services.meteofrance.com/btp)

### OpenWeatherMap

Société OpenWeather Ltd (Londres, UK), service mondial sans restriction géographique connue pour la France.

- **Authentification** : clé API en query param (standard industrie).
- **Sandbox/test / free tier** : plan gratuit — 60 appels/min, 1 000 000 appels/mois. One Call API 3.0 : 1 000 appels/jour gratuits, facturation à l'appel au-delà.
- **Webhooks** : non trouvés — architecture pull uniquement.
- **Capacités principales** : météo actuelle, prévisions 5j/3h et 16j (tous plans) ; prévisions 30j et horaires 4j à partir de Developer ; téléchargement en masse et précipitations globales à partir de Professional ; Road Risk API et stats à partir d'Expert ; pollution de l'air et géocodage inclus dans tous les plans.
- **Grille tarifaire mensuelle (HT)** :

| Plan | Prix | Appels/min | Appels/mois | Disponibilité |
|---|---|---|---|---|
| Free | 0 € | 60 | 1M | — |
| Startup | 35 € | 600 | 10M | 95 % |
| Developer | 160 € | 3 000 | 100M | 99,5 % |
| Professional | 410 € | 30 000 | 1Md | 99,5 % |
| Expert | 1 200 € | 100 000 | 3Md | 99,9 % |
| Enterprise | sur devis | — | — | — |

- **Limites principales** : quotas par plan, facturation à l'appel au-delà ; pas de vigilance réglementaire française officielle.
- **RGPD/résidence des données** : politique de confidentialité existante mais **aucune précision sur la localisation des data centers ou une garantie de résidence UE trouvée** — à clarifier directement avec le fournisseur si bloquant.
- **Dépendance fournisseur / alternatives** : substituable. Alternatives identifiées : Meteomatics (modèles propriétaires Europe/US, tarif sur devis), Weatherbit, Tomorrow.io ; solutions spécialisées BTP : UBIMET (Autriche, « Weather Cockpit »/« UBIMET Connect ») et Frogcast (prévisions ultra-locales chantiers).

Sources : [openweathermap.org/guide](https://openweathermap.org/guide), [openweathermap.org/price](https://openweathermap.org/price), [en.wikipedia.org/wiki/OpenWeatherMap](https://en.wikipedia.org/wiki/OpenWeatherMap)

**Synthèse décision — catégorie 18** : pour un usage France (planification chantiers extérieurs), Météo-France API est la source la plus légitime sur la vigilance/prévisions officielles françaises et gratuite pour un usage raisonnable ; OpenWeatherMap offre un modèle de prix plus structuré pour une volumétrie prévisible ou une couverture internationale. RGPD/résidence des données non confirmé officiellement pour aucun des deux — point à lever avant contractualisation si critique.

---

## 19. Notifications push (mobile)

### Firebase Cloud Messaging (FCM)

- **Disponibilité France/Europe** : iOS, Android, Web, Flutter, C++, Unity — mondiale, y compris France/Europe.
- **Authentification** : SDK Firebase Admin côté serveur ou API FCM v1, nécessite un environnement serveur de confiance (Cloud Functions ou serveur applicatif).
- **Sandbox/test** : console Firebase avec compositeur de notifications pour tests avant production.
- **Webhooks** : pas de webhooks natifs identifiés ; export vers BigQuery et FCM Data API disponibles pour l'analyse de livraison.
- **Capacités principales** : messages de notification ou de données (jusqu'à 4096 octets), ciblage par device unique, groupe de devices, ou topics.
- **Limites principales** : mécanismes de throttling/quotas existent mais valeurs numériques précises non détaillées dans la documentation de présentation consultée.
- **Prix** : gratuit, sans coût affiché ni limite d'usage explicite (« No-cost »).
- **RGPD/résidence des données** : des sources tierces indiquent une conformité RGPD/HIPAA possible, mais la page de tarification officielle **ne détaille pas les régions/résidence des données pour FCM spécifiquement** — à documenter précisément avec Google avant usage de données personnelles sensibles.

Sources : [firebase.google.com/docs/cloud-messaging](https://firebase.google.com/docs/cloud-messaging), [firebase.google.com/pricing](https://firebase.google.com/pricing)

### OneSignal

- **Plans tarifaires** ([onesignal.com/pricing](https://onesignal.com/pricing)) : Free — 10 000 envois email/mois, push mobile illimité jusqu'à 1 000 MAU, 10 000 abonnés web push/envoi, 3 journeys actifs, 6 segments ; Growth — à partir de 19 $/mois, puis 0,012 $/MAU (push mobile), 0,004 $/abonné web push, 5 journeys, 10 segments ; Professional/Enterprise sur devis annuel.
- **Webhooks** : disponibles — événements `notification.willDisplay`, `notification.clicked`, `notification.dismissed` (web push), configurables via dashboard, URL HTTPS obligatoire, compatibilité variable selon navigateur (Chrome complet, Firefox partiel, Safari non supporté). *Divergence signalée entre sources* : la page de pricing mentionne par ailleurs les webhooks comme « disponibles sur plans annuels » — à clarifier avant contractualisation. Source : [documentation.onesignal.com/docs/webhooks](https://documentation.onesignal.com/docs/webhooks)
- **RGPD/résidence des données** : DPA inclus sur les plans payants ; OneSignal a annoncé la migration de ses centres de données vers l'UE, avec des frais additionnels possibles pour l'hébergement UE/APAC selon certaines sources commerciales. Source : [onesignal.com/blog/onesignals-data-centers-are-moving-to-the-eu/](https://onesignal.com/blog/onesignals-data-centers-are-moving-to-the-eu/)

### Alternative mentionnée : Expo Push Notifications

Abstraction unifiée au-dessus de FCM (Android) et APNs (iOS), pertinente si l'app mobile SUPORDO est développée en React Native/Expo. Prix/limites/RGPD non détaillés dans la documentation de présentation consultée — reposant sur FCM/APNs sous-jacents, coût direct probablement nul mais à confirmer. Source : [docs.expo.dev/push-notifications/overview](https://docs.expo.dev/push-notifications/overview/)

*Note* : la piste « Batch » (éditeur français de push notifications) avait été identifiée comme piste à vérifier mais n'a pas pu être creusée en détail dans le temps de recherche disponible.

**Synthèse décision — catégorie 19** : FCM est gratuit et suffit fonctionnellement pour le cas d'usage SUPORDO (notifier les techniciens terrain). OneSignal apporte une couche de gestion (segments, journeys, webhooks) utile si SUPORDO veut piloter des campagnes de notification plus riches, au prix d'un coût croissant avec le nombre d'utilisateurs actifs et d'un flou à lever sur la disponibilité effective des webhooks selon le plan.

---

## 20. Portail client

**Conclusion : aucune brique tierce sérieuse et pertinente identifiée.** Le portail client (espace où le client final consulte devis/factures/statut de chantier) est structurellement une fonctionnalité à construire en interne dans SUPORDO, pas une brique d'API à intégrer. Les recherches menées confirment cette hypothèse plutôt que de la contredire.

- **Copilot** (`copilot.com`) : le domaine renvoie aujourd'hui vers Microsoft Copilot, un assistant conversationnel grand public sans rapport avec un portail client en marque blanche intégrable. Pas un candidat pertinent.
- **SuiteDash** : plateforme SaaS « tout-en-un » avec un mode « EXTREME White Label » (personnalisation domaine, logo, couleurs, app mobile en marque blanche). Il s'agit de personnaliser une **instance SuiteDash utilisée comme logiciel de gestion complet**, pas d'une brique API intégrable dans un autre CRM/ERP comme SUPORDO — c'est un concurrent fonctionnel potentiel, pas un composant d'intégration. Tarif : 99 $/mois (équipe et clients illimités). RGPD mentionné de façon générique, sans détail sur l'hébergement UE. Source : [suitedash.com](https://www.suitedash.com)

Aucun autre candidat de type « constructeur de portail client en marque blanche, intégrable via API/iframe/SDK dans un logiciel tiers » n'a été identifié comme suffisamment pertinent et sérieux pour ce cas d'usage BTP France.

**Recommandation** : construction interne du portail client (espace web authentifié consultant les objets métier déjà présents dans SUPORDO — devis, factures, statut de chantier), sans dépendance fournisseur externe sur cette brique.

---

## Notes méthodologiques générales et limites transverses

- Recherche conduite le 23 septembre 2026, en parallèle par 5 sous-agents dédiés par groupe de catégories (un lot prioritaire dédié à la réforme facturation électronique France 2026, et 4 lots couvrant les 19 autres catégories), chacun consultant directement la documentation officielle publique (WebSearch/WebFetch) et signalant explicitement ce qui n'a pas pu être vérifié plutôt que de l'estimer.
- Plusieurs pages officielles se sont révélées inaccessibles au moment de la recherche (HTTP 403, contenu rendu en JavaScript côté client non extractible) : notamment les pages pricing de Brevo, Vonage, HERE, Pappers, Point.P, une partie de la documentation Lyra et Azure AI Document Intelligence. Ces points sont signalés section par section et doivent être revérifiés manuellement avant toute décision engageante ou contractuelle.
- Deux candidats initialement envisagés se sont révélés non exploitables après vérification et sont documentés comme tels plutôt que simplement omis : **QuickBooks** (retrait commercial total du marché français depuis le 31/12/2023) et **GoCardless Bank Account Data / ex-Nordigen** (nouvelles inscriptions fermées depuis juillet 2025).
- Conformément au principe de suffisance décisionnelle retenu pour ce dépôt, la profondeur de recherche a été calibrée à la décision d'architecture à servir (pas de choix de fournisseur à faire à ce stade) — sauf pour la catégorie 17 (catalogues BTP) où une cartographie plus large a été jugée nécessaire vu la fragmentation constatée du secteur, et pour la catégorie 9 (facturation électronique) traitée en priorité et en profondeur vu son caractère réglementaire structurant.
- **Prochaine étape suggérée** : lever les points signalés « non confirmé »/« à revérifier » qui concernent des candidats susceptibles d'entrer en short-list réelle, avant tout arbitrage contractuel — notamment la résidence UE exacte (Google Maps, Claude API directe, Vonage, HERE), les tarifs non extraits (HERE, GoCardless SEPA exact, Lyra, Azure Document Intelligence, AWS S3 régions UE), et la confirmation directe du calendrier de facturation électronique auprès d'assemblee-nationale.fr et fnfe-mpe.org (cf. §9.8).
