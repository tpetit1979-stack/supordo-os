---
source: https://help.sellsy.com/fr/articles/5876622-webhooks
categorie: Intégrations et API
titre: Webhooks
date_recuperation: 2026-09-05
---

# Webhooks

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2159295103/e814793762cb57c5133880491a96/FAQ-Bannie%CC%80reAcademy-2+%282%29.png?expires=1788635700&signature=0b363c76de2498c7fac09470d472bee6b962755ecd20c81f89c480a1838511e8&req=diEiH8t3mIBfWvMW1HO4zf508uTiGviW0jiMA1i9i5qlZ3K7LFL9UN7Sl1JE%0AL3%2Ff0Mide%2F%2Bupyt80bY%3D%0A)

Sellsy propose un système de webhook pour optimiser la liaison avec vos solutions.

Lors d’un évènement côté Sellsy (création client, mise à jour document) nous vous donnons la possibilité de déclencher l’envoi d’information de Sellsy vers une URL à configurer par vos soins (à vous de traiter ces données à réception).

Actuellement, 2 types de webhooks existent via Sellsy :

- Webhook Slack,
- Webhook HTTP.

___________________________________________________________

### **Qui doit mettre en place le webhook sur Sellsy **

Seul un administrateur du compte Sellsy peut configurer les webhooks. Il s’agit de manipulations sensibles, tant d’un point de vue technique, que sur le plan de la confidentialité des données.

___________________________________________________________

### **Configuration du webhook sur Sellsy **

Rendez-vous dans "*Menu" > "Réglages" > "Portail développeurs"* et cliquez sur *“Webhooks”*.

![](https://sellsy-a9cc78fb6d3a.intercom-attachments-7.com/i/o/446372201/e6c6ac85f6f9ef21c95538cd/nhT7qRezHLeDRxkg05uj_SOh6zW83AQfSmZDwIrCeQhBT2x0HbcMXdTsXJ_1WwpMtfS4Gj3Ehc1BDDtZszWL35PS7-aIF6lQtvHZnWF-q-zqOw3ksbXUh6hh3B-7GsWT50pVsWB7?expires=1788635700&signature=fc566868f45e65d89658840913a1c91b72e4e7d8977dbe5bf058ba22c10e64d4&req=cCQhFc58n4FeFb4f3HP0gHGTzrQJ7uTPCpRC%2FE9AOz6OzzBx9yqYCEBfpe%2Bn%0ALWIYf5HNoT5FyCQJaA%3D%3D%0A)

Ensuite, choisissez le webhook à configurer.

### 

___________________________________________________________

### **Configurer un webhook Slack ** 

La configuration sur Slack demande aussi d’être administrateur du compte Slack.

Vous devez :

1. Créer l’url du webhook sur Slack,
2. Finaliser la configuration sur Sellsy.

___________________________________________________________

### **Créer l’url du Webhook Slack ** 

- Connectez-vous à votre compte Slack.
- Accédez à l’adresse suivante : [https://my.slack.com/services/new/incoming-webhook/](https://my.slack.com/services/new/incoming-webhook/)
- Vous allez être redirigé vers une URL du type [https://votre_pseudo.slack.com/apps/new/XXXXXXXX-incoming-webhooks](https://votre_pseudo.slack.com/apps/new/XXXXXXXX-incoming-webhooks)

![](https://sellsy-a9cc78fb6d3a.intercom-attachments-7.com/i/o/446372207/8b89cba1e031ea253524023a/o4xiiyr9KvI3c39VgdbqRUpXuUNeY889hjvld1AF5i0RJY3dfBJKnPfGIaLexYjOJ4mSY19ZQPtcIj55f0sQq66H2-v9ogRJCm5XMmx6QOqu-ur0tyJRSrvZLAB809tr5Qxan2kN?expires=1788635700&signature=91aa2e54bf9fd76a733b6cf5b1518abb4b3afc678cbf52653cb7c189d03728b9&req=cCQhFc58n4FYFb4f3HP0gOIr21K%2F%2FhMp4kz6YbAMzjGg%2Ffd%2BfIufMXfjAEg8%0A%2FsIR%2BQnptQRxiM%2FdUA%3D%3D%0A)

- Choisissez un channel par défaut (cette valeur est obligatoire pour valider l’ajout sur Slack, mais elle sera surchargée sur Sellsy). Exemple : channel “#general” ci-dessous.

![](https://sellsy-a9cc78fb6d3a.intercom-attachments-7.com/i/o/446372212/29b104621c65e0c1925336f3/U33AjWayLacSyi6x4eoLOGn4y6ZhBjyyf_zJ1xWGks0ltIw3PO1TP05y612wxd1eeSCw_aDeCDhgtCviNTNCdK7B9Ib-9avrNx9eHyMR5joyfrGCyBV276VXapv979uRI-DknXRV?expires=1788635700&signature=db0e92880fd2fedb54c2471ccf222744081614058721544d83ab29bfe0e1784c&req=cCQhFc58n4BdFb4f3HP0gJ4l5dG4wDY3morhgkCeLQucALuDOSij9MCWls%2BC%0AvSZ5ilr%2B3mDt%2Bro23Q%3D%3D%0A)

- Cliquez sur “*Add Incoming WehHooks integration”*.
- Vous allez ensuite obtenir le *“Webhook URL”* à utiliser sur Sellsy.

![](https://sellsy-a9cc78fb6d3a.intercom-attachments-7.com/i/o/446372219/427d442227b6b7fbee2c4cc7/SFBOypSkJXXa03gpJQJzxUNx2wtBU11_Imrv0WcUPzoBoLVKfCRMWiuZVsoPC6pX0E34f0AM8f7VUeggLfo62PJrPNO3SoSEgB2no09xetPJMfxJ3l-hjvYiNfS_yS8MjeHjQQcs?expires=1788635700&signature=0e5174093a06e44b962e82f16eac2e4c4afca25d14300be7a0242adcef9f08ac&req=cCQhFc58n4BWFb4f3HP0gMPYJQYx2%2B0pKxI56kUv35%2FQjeCXtb9bAIhMf4Z6%0A4aNPOiTK9C%2FlRJD1%2FA%3D%3D%0A)

> **Bon à savoir :** vous retrouverez la documentation technique sur le webhook Slack[ ici](https://api.slack.com/incoming-webhooks).

___________________________________________________________

### **Finaliser la configuration Slack sur Sellsy**

- Copiez le *“Webhook URL”* récupéré à l’étape précédente puis collez-le sur Sellsy (champ nommé *“Endpoint Slack”*).

![](https://sellsy-a9cc78fb6d3a.intercom-attachments-7.com/i/o/446372227/e5e52675562bec1348b93ecf/KsYdO871EVRpjZxr0QFOr4XRs95YFPKmw6-rM0YGoz3vo70FCGTt5k2P6Blz7C_soP8tNjG3FN5Do5A_DOOQAi23klanoEb-WA6vYYiLkYYooVAYjy1UaC3xOedfEOwBpWnzB2FX?expires=1788635700&signature=04aa8468196660a83c8d0bb66718798c40ceabf4fe3ea427700b2216f6d8a93c&req=cCQhFc58n4NYFb4f3HP0gB%2BqxftNKVMp3S5JxDUbUgTDoePOomDIzjAP%2FSjy%0A%2BCvgT28IIlZ1u%2B0gIA%3D%3D%0A)

- Inscrivez le nom channel Slack par défaut (qui va surcharger la valeur de l’étape ci-dessus).
- Choisissez ensuite d’activer ou non l’envoi des données sur Slack.
- Concernant les informations envoyées au Webhook, vous pouvez choisir un “Channel” propre à chaque action.

![](https://sellsy-a9cc78fb6d3a.intercom-attachments-7.com/i/o/446372238/2078bb6b316be8b27e409993/g6dEveitBzV8-ITiYxFNzMrBXL00iihfyc72DQlqV54gNEjoblgDTt8vc86W7tXNRgC5jteiuvjmrcsZEg7psUmXKTepbv5xRDj3_H6y4SLGWTnrU_qhUKH9yN6YfvO0qoS6jPZ3?expires=1788635700&signature=9bcce4fb84086bc44405e6c5834a37832fc85e286f29ad844d7d239a5ae99d14&req=cCQhFc58n4JXFb4f3HP0gKU5Zndb%2FnPKL1f3e1VFzoylQuAlQKR8Ne5XW5D0%0AnMfQY1PRZFVhSZ3T2A%3D%3D%0A)

___________________________________________________________

### **Webhook HTTP ** 

1. Vous devez ajouter l’URL vers votre script dans la section nommée : *Configurer le webhook*.
2. Puis *“Endpoint personnalisé”*.
3. Activez le webhook (cochez la case en face de *“Webhook Actif ?”*).
4. Sélectionnez les actions sur lesquelles vous souhaitez obtenir un retour via le webhook.

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/1444411801/9c2e83b5b1d420fda3d85e163966/Brice_Flacelie%CC%80re__message_direct__-_Sellsy_-_15_nouveaux_e%CC%81le%CC%81ments_-_Slack.png?expires=1788635700&signature=0fb82ecd0fc05d042da38415560b2cb60634f2701212111ec1b8bb607e5c6935&req=dSQjEs1%2FnIlfWPMW1HO4zW2KUbkjhDXfWONSZ2MVuK3iDLQN0skPiUscS359%0AeyrHibfKnMSdEXXjyb8%3D%0A)

Informations utiles sur le format de retour du webhook :

- Un exemple vous permettant de récupérer le contenu POST envoyé par le webhook en PHP,
- Le contenu du “form-urlencoded” envoyé par le webhook,
- La liste des types d’objets renvoyé (relatedtype),
- Le webhook n’attends pas de réponse,
- Le webhook ne gère pas les erreurs.

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/1315537898/b4a517455d7d35b004017dd52c29/unnamed.png?expires=1788635700&signature=e52805e9d591112001bd11adc05ffe88ad462299d2bedb81a9e86e864c4d4b86&req=dSMmE8x9molWUfMW1HO4zQ7FR8cgAn9ZcG8S3MtZMc2ozNYdbM%2Flo8%2BOFGOU%0ArNm0Sc%2FJQIT9u35X%2B8M%3D%0A)

**Options avancées** 

- Signature des webhooks.

Les webhooks sont signés afin de garantir leur intégrité. 

Un en-tête HTTP X-Webhook-Signature est ajouté à chaque requête, contenant la valeur suivante : `SHA1(SIGN_KEY + WEBHOOK_BODY)` 

La clé de signature (`SIGN_KEY`) est disponible et personnalisable depuis le formulaire de création du webhook. 

- Exemple en php

```
&lt;?php <br><br>// Corps brut de la requête (body reçu tel quel) <br><br>$body = file_get_contents('php://input'); <br><br>// Signature calculée <br><br>$expectedSignature = sha1('ma_clé_secrète' . $body); <br><br>// Vérification <br><br>$webhookIsValid = hash_equals($expectedSignature, $_SERVER['HTTP_X_WEBHOOK_SIGNATURE'])
```

​

**Liste des objets (related types) :**
​

$related = [

'staff', ## staff member

'third', ## company: client,prospect,supplier

'people', ## contact

'item', ## catalog item or service

'import', ## import

'purinvoice', ## purchase supplier invoice

'purdeliery', ## purchase supplier delivery

'purorder', ## purchase supplier order

'purcredinote', ## purchase supplier credit note

'timetracking', ## timetracking entry

'opportunity', ## prospection opportunity

'ticket', ## support ticket

'project', ## project

'expense', ## expense

'rent', ## rental : rent or book

'campaignemail', ## email marketing campaing

'campaignsms', ## sms marketing campaign

'proptemplate', ## proposale template

'propdocument', ## proposal

'estimate', ## sale estimate

'invoice', ## sale invoice

'delivery', ## sale delivery

'order', ## sale order

'proforma', ## sale proforma invoice

'model' ## sale model

];

___________________________________________________________

### **Ressources complémentaires**

Pour en savoir plus sur les webhooks :

- **Documentation technique générale :** **[https://en.wikipedia.org/wiki/Webhook](https://en.wikipedia.org/wiki/Webhook)** (en anglais)
- **Documentation Slack Incoming Webhooks :** **[https://api.slack.com/incoming-webhooks](https://api.slack.com/incoming-webhooks)**
- **Article sur l'API Sellsy :** **[API V2](https://help.sellsy.com/fr/articles/5876614-api-v2)**

Mis a jour le : 13/03/2026
