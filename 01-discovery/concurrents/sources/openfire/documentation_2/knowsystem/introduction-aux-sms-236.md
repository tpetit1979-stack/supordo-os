---
url: https://documentation.openfire.fr/knowsystem/introduction-aux-sms-236
url_finale: https://documentation.openfire.fr/knowsystem/introduction-aux-sms-236
date_collecte: 2026-09-06
destination: documentation_2
---

Le service de messagerie SMS (pour « Short Message Service ») permet de transmettre de courts messages textuels. C’est l’un des services de la téléphonie mobile.

Ce SMS est devenu incontournable dans notre quotidien puisque, comme le rappelle OVH, plus de 90 % des SMS sont lus dans les 3 minutes qui suivent leur réception.

## Type et taille de SMS

Par défaut, ce SMS a une taille maximum de 160 caractères. Si le message dépasse les 160 caractères, il sera découpé en plusieurs SMS comme suit :

*1 SMS → 160 caractères au total (160 / sms)*

*2 SMS → 306 caractères au total (153 / sms)*

*3 SMS → 459 caractères au total (153 / sms)*

*… (153 / sms)*

*Attention: Pour GSM7 SMS, la taille limite est de 160 caractères et pour Unicode est de 70. Au-dessus de ces limites, le contenu est divisé en un message en plusieurs parties et la limite de caractères est abaissée à 153 pour GSM7 et à 67 pour Unicode. Le système vous informera en temps réel du nombre de SMS que votre message représente.*

## Choix du Fournisseur de SMS OVH

Pour envoyer un SMS depuis une application web, nous devons connecter notre application à un service spécifique.

OpenFire a fait le choix du service SMS OVH Telecom pour plusieurs raisons :

- Technicité de la solution,
- Proximité “philosophique” open source,
- Cohérence avec notre infrastructure existante : OVH Cloud est aussi notre fournisseur pour l’hébergement, le web et la téléphonie,
- Contrainte du lieu de stockage des données : hébergement des données sur le territoire national,
- Indépendance des fournisseurs de cloud américains Amazon, Google et Microsoft souhaitée par certains clients à l’esprit citoyen français ou européen.

Plus d’informations sur le service SMS Pro sur le site OVH Telecom

Avant d’utiliser notre service SMS, nous devons configurer :

- Notre abonnement chez OVH Telecom,
- Notre service SMS dans l’application OpenFire.

Important : Votre abonnement SMS Pro est une « boîte noire » seulement utile pour configurer le service SMS !

## Abonnement SMS OVH

Souscription de l’abonnement

Préparez deux adresses mail pour la gestion de votre abonnement OVH :

- Adresse mail principale
- Adresse mail de secours

Pour souscrire un abonnement au service SMS Pro rendez vous sur le site OVH Telecom

Nous attirons votre attention que quelques informations essentielles de votre abonnement SMS Pro chez OVH Telecom :

- Identifiant Client
- Expéditeur
- Utilisateur API
- Recharge automatique
- Email de transfert des réponses par SMS

Connexion en tant que Manager pour gérer le service SMS Pro sur Manager OVH Telecom

Tableau de bord OVH SMS

Ce tableau de bord est le panneau de contrôle de votre abonnement.

Parmi les informations essentielles, nous notons :

1. Identifiant du service SMS
2. Crédit « SMS restants »
3. Recharge automatique
4. Statistiques

## Expéditeur


Cette information est vitale car elle identifie l’émetteur du SMS reçu par le destinataire. Il est donc conseillé de donner le nom de l’entreprise ou de la marque comme expéditeur.

Le numéro de l’émetteur est un numéro abrégé à 5 chiffres auquel, théoriquement, le destinataire ne doit pas répondre.

Utilisateur API

L’utilisateur API définit l’accès au service SMS Pro chez OVH Telecom. Ce nom d’utilisateur est seulement requis par la passerelle SMS et n’est donc pas visible dans les SMS.

*Astuce: Nommez cet utilisateur API en minuscules pour identifier une information interne !*