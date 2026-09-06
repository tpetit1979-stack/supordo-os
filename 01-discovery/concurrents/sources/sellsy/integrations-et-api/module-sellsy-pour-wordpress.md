---
source: https://help.sellsy.com/fr/articles/5877018-module-sellsy-pour-wordpress
categorie: Intégrations et API
titre: Module Sellsy pour Wordpress
date_recuperation: 2026-09-05
---

# Module Sellsy pour Wordpress

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2159339933/9e8b6699fd46d92685f42f26f2c3/FAQ-Bannie%CC%80reAcademy-2+%282%29.png?expires=1788635700&signature=4e74ddbebe2df9ac2c1e3fa4e676f52daa8f3a4e6bcb8c4d17ba0a9061a9e4fd&req=diEiH8p9lIhcWvMW1HO4zUjFUQxBghyfMPPFMRuu1Bo5tmb03VlXvSBUMb%2Fu%0AKVlZXUZnIV4BTDDXrWU%3D%0A)

___________________________________________________________

### Obtenir le formulaire Wordpress 

Pour obtenir le formulaire Sellsy sur WordPress, vous pouvez le télécharger sur  [https://wordpress.org/plugins/sellsy/](https://wordpress.org/plugins/sellsy/) ou via l'administration de votre site WordPress (menu "Extensions").

___________________________________________________________

### Configurer la connexion API WordPress/Sellsy

Vous devez récupérer les keys de l’API Sellsy sur la page suivante : [https://www.sellsy.fr/developer/my-apps](https://www.sellsy.fr/developer/my-apps)

Pour cela vous devez créer une application :

![](https://sellsy-a9cc78fb6d3a.intercom-attachments-7.com/i/o/446450188/4742f1050ea7082832e4221f/6407876c-d2b4-493f-98fc-8ac6b09e4c73-acc1cc5f-78e4-468b-a3e5-a9f823dc7534.?expires=1788635700&signature=a7bd4c02b9855e5c08a108ea1612879ad9394db1e829fd435bbeb712f1ba5890&req=cCQhEsx%2BnIlXFb4f3HP0gEEbuEvbPigg0ZoW3C7Cav3jJNgRMNlamb3IoduC%0AWBN%2Fw0fWxEytm4rYkA%3D%3D%0A)

Ensuite vous devez cliquer sur “Générer un token utilisateur”.

![](https://sellsy-a9cc78fb6d3a.intercom-attachments-7.com/i/o/446450191/e191acee54ae443f50c40c46/ebc6cc4f-4516-4f08-8644-6ac323093cef-60f431e9-e3ff-482e-9216-f6a2f100e380.?expires=1788635700&signature=e47269d846172633c82f843fee96388e913bd58927587b3f804acdd261bd08db&req=cCQhEsx%2BnIheFb4f3HP0gFkPWmqtRba8B37fF%2Fs8wqxWGoZ6z3D1RSDcGc00%0AzVhHMan77DikZF4%2BEw%3D%3D%0A)

Vous pouvez ensuite copier / coller les différentes informations nécessaires sur la page de configuration du module WordPress.

- Consumer token
- Consumer secret
- Utilisateur token
- Utilisateur secret

![](https://sellsy-a9cc78fb6d3a.intercom-attachments-7.com/i/o/446450198/6bccb327659fdde61a0a6910/adb203b6-5c57-499a-93dd-a4e10a76a0db-b32bf155-1165-4627-8485-80c4bf9cb9c9.?expires=1788635700&signature=1fa51619d1666aaa6925582c4e98d035103d3d951ac61a0bcd70483b50015b71&req=cCQhEsx%2BnIhXFb4f3HP0gHaTITKb3%2FMyc2bAwSisyKTDl%2F9UXPZ5BTBThkkd%0A6DGA1V3Bu8MJGNasCA%3D%3D%0A)

___________________________________________________________

### Configurer le tracking 

Depuis l'onglet Configuration, vous pouvez activer / désactiver l'option tracking. Cette option vous permettra de connaitre l’ensemble des pages consultées par le visiteur qui aura validé le formulaire. Vous retrouverez ces informations sur la fiche prospect sur l'interface Sellsy.

Ex : rendu obtenu sur Sellsy (onglet Tracking d’un prospect)

![](https://sellsy-a9cc78fb6d3a.intercom-attachments-7.com/i/o/446450200/01ac2a0c3616ee83d2b15835/6347f359-66c3-4480-b4ac-d4d15a525eba-b85eb6be-4c23-45e4-b10b-07cb4dbbfc18.?expires=1788635700&signature=f5579a32e91cc0485cfce5186fc1c8c57240c02afa8ef4abf62196a015a4913e&req=cCQhEsx%2Bn4FfFb4f3HP0gMuqPn0K56CuOM4J5kDAf%2BRst%2F2cJ9q2Z1yfh5h8%0ACdyYsnl8tzZwN9Pr%2BQ%3D%3D%0A)

___________________________________________________________

### Configurer le Captcha

Le captcha vous permettra de sécuriser votre formulaire pour qu’il ne soit pas soumis par un robot.

Plus d’informations sur reCaptcha qui est utilisé sur le plugin WordPress :

[https://www.google.com/recaptcha/intro/android.html](https://www.google.com/recaptcha/intro/android.html)

Pour configurer le captcha, vous devrez récupérer 2 keys sur [https://www.google.com/recaptcha/admin#list](https://www.google.com/recaptcha/admin#list)

- Site key
- Secret key

Puis les ajouter sur la page “configuration” du plugin.

L’option “Etat”, vous permettra d’activer / désactiver le captcha sur l’ensemble de vos formulaires.

![](https://sellsy-a9cc78fb6d3a.intercom-attachments-7.com/i/o/446450202/aee79947d3611c1ce822feee/c0250b51-e8ca-4bf2-a22b-78b1bdce40c2-4ec574dc-8f5f-4bf9-9a45-81ce704129c2.?expires=1788635700&signature=0bb20151e343247a3283d46e4d52f8882447a186180e9d868d7aed4c09be64af&req=cCQhEsx%2Bn4FdFb4f3HP0gNHfSatpZ0sxNFCfAuxISrRc3p2RqNzmun%2FbMFyA%0AJNKXEwTJA0LjIhQQeQ%3D%3D%0A)

Suite clic bouton “Register”.

![](https://sellsy-a9cc78fb6d3a.intercom-attachments-7.com/i/o/446450204/58f11e153ed066083f923386/1866190b-42db-4188-b95e-05f7fbd17416-69fc15a2-2282-4102-aca0-4dd2838d0736.?expires=1788635700&signature=4abb58d78ccc7dffffb4cbb8d2e9bb18e3ffa8e16d89f763b571e38f32043865&req=cCQhEsx%2Bn4FbFb4f3HP0gHX4vjRds5QpUcpi4g3ygGGeUNY9hh%2BtqD%2FaKYSm%0AV9bsRxDHLqeA%2BnYSCw%3D%3D%0A)

NB : les clefs “Site key” et “Secret key” seront différentes lorsque vous réaliserez cette manipulation.

___________________________________________________________

### Configurer un formulaire de contact

![](https://sellsy-a9cc78fb6d3a.intercom-attachments-7.com/i/o/446450208/6d7bdc58e1454cb312999d2e/e5cafeb6-0db3-4194-8d99-56e9146edf47-8ff1389a-02d5-416e-9eb7-d720f03fbbe8.?expires=1788635700&signature=9511595885ae58bad79e53fdda14d0ceaba67e0ec5ce358bc0b2261108f931b5&req=cCQhEsx%2Bn4FXFb4f3HP0gJtftGBu9AA2bg2tpQZzIQmi6jwhgY4pMjMg70gx%0AGV%2B%2B6Xnuqkzex1vAuA%3D%3D%0A)

- **Shortcode** : Exemple [contactSellsy id="25"] Chaque formulaire dispose d'un id différent. Le shortcode ci-dessous doit-être copier/coller sur la page/article sur laquelle vous désirez voir apparaître votre formulaire.

- **Nom** : Il s’agit du nom du formulaire, uniquement utilisé dans votre back-office Wordpress.
- **Ajouter sur Sellsy** : “Prospect” ou “Prospect et opportunité”.

- **Etat** : Activer / désactiver le formulaire. S’il est désactivé, il ne sera plus visible sur votre site.
- **Notification** : Ajouter un email pour recevoir une notification vous indiquant qu’un formulaire a été validé.

**Information Opportunité** :

![](https://sellsy-a9cc78fb6d3a.intercom-attachments-7.com/i/o/446450216/6ef4a9fedb2613ae5f5b0dd1/mgGmdO0IAWBAwjHB-pqEfQfL8OL_vx8_rogau8zOO11oZkpdvqCoucS7ZaOoSxWQW-ka97au-6hkI6QbzAnyxx9tFxRJkwe41K3xqCsCR13ZLr-BQQ2fJO1Vv-4GJGYw-OkQifo7?expires=1788635700&signature=237c458d7fc11205165652c90e02431f3b7de03a02ddd20af190ed98b2e5d7be&req=cCQhEsx%2Bn4BZFb4f3HP0gBav63LKuO%2B%2B6%2BRvcJNe8JebTjjQhIqpobjVxhnh%0AuvPC0atq2PiTopGDww%3D%3D%0A)

- **Nom de l’opportunité** : Il s’agit du nom qui sera utilisé sur Sellsy lors de la validation du formulaire. Si un nom de société est indiqué, ce dernier sera ajouté au nom de l'opportunité. Sinon, si un Prénom NOM est indiqué, ce dernier sera ajouté au nom de l'opportunité.
- **Source d’opportunité** : Sélectionnez une source Sellsy. Présent uniquement si vos keys API Sellsy sont valides et si vous avez configuré une source sur votre compte Sellsy.
- **Pipeline** : Sélectionnez un pipeline et une étape. Présent uniquement si vos keys API Sellsy sont valides.
- **Date d’échéance (en jours)** : Indique l’échéance de votre opportunité.
- **Probabilité** : Indique la valeur en pourcentage de votre probabilité (max=100).
- **Assigné à** : Choix du collaborateur Sellsy qui sera assigné à l’opportunité.
- **Smart-tag **: Smart-tag rattaché à l’opportunité.

**Information société** :

![](https://sellsy-a9cc78fb6d3a.intercom-attachments-7.com/i/o/446450225/34a7ddb0970d0f0348e99379/4fc7cdca-0e89-45a9-900f-6d6e1ad25ba6-1144f425-78c2-48b1-98bc-5b5e65ce0038.?expires=1788635700&signature=079b48d4f83cda736179edb255112f86fc3b5ee743230134399f3581f1b190f0&req=cCQhEsx%2Bn4NaFb4f3HP0gOfJ5RuXABSqtyZ9evw20XVTMP1WupDuYKtjxhv3%0AFrgAoMkikrk2S%2BVF5Q%3D%3D%0A)

- **Nom** : Nom de la société.
- **Siren** : Numéro siren.
- **Siret** : Numéro siret.
- **RCS** : RCS.
- **Smart-tag** : Smart-tag rattaché au client (=société).

**Information Contact** :

![](https://sellsy-a9cc78fb6d3a.intercom-attachments-7.com/i/o/446450235/15f24097c8550ac88594ebec/a03d041e-cf65-422d-a0e9-fcd821e9ea67-c533a1dc-6b78-462a-85b4-993fa1a6990d.?expires=1788635700&signature=9a0c3fc09e6bf315c694e84957370cc039039db2e0560f84326e44a9e9dac9b9&req=cCQhEsx%2Bn4JaFb4f3HP0gIJUDv%2BgUaDrcwWmKTpDaZqoeg7bPpBDlaFwnB1P%0Al9Fd9qczEfJBHyEW5A%3D%3D%0A)

- **Nom** : Nom du contact.
- **Prénom** : Prénom du contact.
- **Email** : Email du contact.
- **Téléphone** : Téléphone du contact.
- **Mobile** : Téléphone mobile du contact.
- **Fonction** : Poste occupé par le contact.
- **Smart-tag** : Smart-tag rattaché au contact.

**Marketing** : 

![](https://sellsy-a9cc78fb6d3a.intercom-attachments-7.com/i/o/446450243/4feece01219e4d69afca906e/c471d270-f897-4a33-b1b8-44ba69d0f307-faccf418-2ae2-4aad-8021-c889a6e5ed50.?expires=1788635700&signature=5dc203e7fdf2b8aa167a9134b788d3a972eef8dd7a4a053e8fb87d4e7bf99d33&req=cCQhEsx%2Bn4VcFb4f3HP0gBpx8ZwdU8bLS8uLuSpGO4%2BwfHethblbOsAWXDnv%0A2wMJS7KDTNihKXhTIQ%3D%3D%0A)

- **Tous** : Afficher une “case à cocher” pour que votre prospect puisse souscrire à l’ensemble des choix.
- **Email, Sms, Téléphone, Courrier, Marketing personnalisé** : Afficher une “case à cocher” pour chaque choix désiré.

**Autre** :

![](https://sellsy-a9cc78fb6d3a.intercom-attachments-7.com/i/o/446450247/9c572e5a96785c7aa5083778/d6657242-44d7-44b6-a62d-2a7a3ea1d22c-e618f373-a341-43d6-a8dc-34c398b0388e.?expires=1788635700&signature=a8748bed4ee7fb872f4ef79afbe4e2ea07f08b6a3e491569311912f519248753&req=cCQhEsx%2Bn4VYFb4f3HP0gET82NiMIroYeF4quw4WGiu1W%2B5UWkl%2Fs4VcSq2E%0ANC8Ukjx%2Fz5MBJmFnaQ%3D%3D%0A)

- **Site web **: Url du site internet
- **Note** : Message qui sera ajouté en tant que note sur le prospect et en tant que brief sur l’opportunité.

**Champs personnalisés** :

![](https://sellsy-a9cc78fb6d3a.intercom-attachments-7.com/i/o/446450252/4b0b8772e95763cf6f066c9c/FrDuuiBKMwR6vw-cTUeUvPGrFPzZ9Cnzw2-DiuK5V3Hp3erK5BCRZUIgfb11QXkIaTIWUzxZELE6mDi4xNrp1aSJAiCBN1khvUxGz4nbCBeLMRxyX65SdQwMhC9sf7thzNylzpIh?expires=1788635700&signature=a84fa76465969730c62b258ecd86bc74c0a3a43b74e65d3b060bd7ec612f3c65&req=cCQhEsx%2Bn4RdFb4f3HP0gFnfxkNpP5rMnlLfT7tY9Pc9gC2MJa%2BMv7M4AzD0%0AGspJxJw23ypI5QS2bA%3D%3D%0A)

Ajouter un champ personnalisé de type :

- Texte simple
- Texte riche
- Liste de choix

___________________________________________________________

### Ajouter un formulaire de contact / opportunité dans une page

Pour ajouter un formulaire de type contact dans une page il vous suffit d’identifier le shortcode correspondant à votre formulaire.

Shortcode : Correspond à la valeur à copier / coller sur une page / article, pour obtenir le rendu du formulaire. Ex : [contactSellsy id=25]

Vous pouvez retrouver le shortcode dans la liste des formulaires : *"Sellsy" > "Contact".*

![](https://sellsy-a9cc78fb6d3a.intercom-attachments-7.com/i/o/446450258/9e6e68b1f1e3fae94174a5a4/0b22048b-e44c-4fca-87ca-4007bd5d0135-ec1f7c45-9b55-42c3-bf32-f452a787fdd8.?expires=1788635700&signature=5ba805694e4995ee604adb1cb26f0e34894e081adcec7c41b00247ede16f7f1a&req=cCQhEsx%2Bn4RXFb4f3HP0gBlU%2BpFtcGGdiBRo3RHsrz1XqtzyRISQ%2FoT%2BI%2BJ%2F%0AbIECRFYwtPdo9fmy8w%3D%3D%0A)

Il suffit ensuite d’éditer une page et d’ajouter le shortcode directement dans la page pour ajouter le formulaire.

![](https://sellsy-a9cc78fb6d3a.intercom-attachments-7.com/i/o/446450261/0f3a395c014d5afe9c0d8712/WdfBs5B7uM1ATZsX1pXr7KbcDr1sNcwsCLZfTj1Uy2wAo2EadqHEd9tn6ts5NP5Bn6lWIk_2U_3cylWlatWDE5Q3VK4WxpFLt2MWq_mnJ_uhTNgufDLM76tUZC1ftsYNtnnI5vFe?expires=1788635700&signature=73fec0ca69c16a0253d06dc90be39c13e294fa50d565bb17eb8fc207df63144b&req=cCQhEsx%2Bn4deFb4f3HP0gJy2UZtSaXL2Vkic0%2Fznf1%2B8EAFSdEk9F0XaiBok%0AE63ghHv%2FNTFD4vbxxA%3D%3D%0A)

___________________________________________________________

### Configurer un formulaire de ticket

- **Nom** : Il s’agit du nom du formulaire, uniquement utilisé dans votre back-office Wordpress.
- **Sujet préfixe** : Libellé utilisé sur Sellsy pour référencer le ticket.
- **Assigné à** : Collaborateur qui sera assigné au ticket.
- **Etat** : Activer / désactiver le formulaire. S’il est désactivé, il ne sera plus visible sur votre site.

___________________________________________________________

### Ajouter un formulaire de ticket dans une page

Pour ajouter un formulaire de type ticket de support dans une page il vous suffit d’identifier le shortcode correspondant à votre formulaire.

Vous pouvez retrouver le shortcode dans la liste des formulaires : *"Sellsy" > "Contact".*

![](https://sellsy-a9cc78fb6d3a.intercom-attachments-7.com/i/o/446450265/84c96db20c1a4c0c079972a3/2ba05b0a-8635-42b9-84af-f49af77e0594-2365320a-2d68-4aa1-b5cc-41039c9318c0.?expires=1788635700&signature=dd4c7517a0fa8dd9ae499a8edcdac36cc63e184c325d974ed6c9d37420637bd2&req=cCQhEsx%2Bn4daFb4f3HP0gC5w6ChjkTQQKzAcxlP0YyFBPlAa0LAF49pEtR%2Bz%0ARjfYF%2BC%2BdtG5%2FkBxGw%3D%3D%0A)

Ensuite, éditez une page et ajoutez le shortcode directement dans la page pour ajouter le formulaire.

Ex : [ticketSellsy id=1]

![](https://sellsy-a9cc78fb6d3a.intercom-attachments-7.com/i/o/446450268/93d199a2d6b0b0b03b373899/0eZZh4hGaju6mYwGmkfLWjBNrGQ4uyYRw46GOWsew-L1x7gCMD60PR-SnFZvkuGm_Fi1IFKqwNjMO-OrkAVvgy7n9iFyiTvkFJBObPd-lstpHkrKEsBXpU6H382U0IaTPHOYQefK?expires=1788635700&signature=1c93b66a9995ba21fd74c92f222c6ce6cd044d3f26229c891076bac53ce5c89b&req=cCQhEsx%2Bn4dXFb4f3HP0gN7JMZfrsI8zOwaMpJJvp0HFubN%2FKR0EIHS8lJ%2BO%0AHsFwyhUEJ95MpN1n0w%3D%3D%0A)

___________________________________________________________

### Duplication de prospect / contact  

Lors de la soumission du formulaire de type *"contact"*, le plugin va vérifier :

- Si le nom du prospect existe, sinon si le nom du client existe (ex : Nom de la société "Sellsy").
- Si le prospect existe il sera rattaché au contact.
- Si le client existe (et pas le prospect), il sera rattaché au contact.
- Sinon un prospect sera créé.

Pour le contact : 

- Si son email existe, on utilisera le contact de Sellsy.
- Sinon un nouveau contact sera créé.

Mis a jour le : 13/03/2026
