---
source: https://intercom-help.eu/vertuoza/fr/articles/254749-signature-electronique-du-devis
categorie: Devis
titre: Signature électronique du devis
date_recuperation: 2026-09-05
---

# Signature électronique du devis

## Pourquoi utiliser la signature électronique ?

La signature électronique permet à vos clients de signer un devis directement en ligne, simplifiant ainsi le processus et augmentant vos chances de conversion. En plus de faciliter l'expérience de vos clients, vous recevez une notification chaque fois que le devis est ouvert ou signé.

## Comment utiliser la signature électronique ?

1. Activer la signature électronique

Pour activer la signature électronique, suivez ces étapes lors de l'envoi de votre devis par email :

- Cochez la case « signature électronique » en haut de la page.
- Insérez la méta-donnée **[LINK_DEVIS]** dans le corps de l'email. Cette métadonnée sera automatiquement remplacée par un lien permettant à votre client de consulter et de signer le devis.

![](https://downloads.intercomcdn.eu/i/o/yr18hzl2/35327050/b0909d6561e6bb43378d4dcea58e/image.png?expires=1788620400&signature=a7d64d82003a89c904720af03620e11f64d547fa6ad125df18c286890cc2d081&req=09Bsx1%2F6qTdk2hL085ZhoYdraLRkoOOTgtmLnjkmZzeEShjNp8WaAxDAvJwm%0ANOf%2B0%2FqfQrwa53F3%0A)

> Le modèle de document utilisé est celui défini par défaut dans les paramètres > Documents > Préférences. Il n'est plus possible de définir un modèle lors de l'envoi par email car le lien sera toujours le même pour ce devis, il n'est pas différent d'un envoi à un autre.
> **Attention : La signature électronique est disponible uniquement à partir du pack Pro+**

2. L'expérience de signature pour votre client

Voici comment votre client signera le devis :

1. **Consultation du devis** : Le client ouvre le lien dans son email pour consulter le devis.
2. **Renseignement des informations** : Il complète ses informations (nom, prénom) et coche la case « J’ai lu et j’approuve le devis ».
3. **Signature** : En cliquant sur le bouton « Signer », la signature est enregistrée et un message de confirmation s'affiche. Le client peut ensuite télécharger une copie du devis signé.

3. Notifications de signature

Vous recevrez des notifications dès qu'un client ouvre ou signe le devis. Ces notifications apparaîtront dans votre centre de notifications, et vous pourrez également les consulter dans l'historique du document.

Lorsque le devis est signé, il passe automatiquement du statut "ENVOYÉ" à "SIGNÉ" et il ne vous reste qu'à accepter le devis pour le transformer en chantier ou en intervention.

### 1. Modèle d'email
Le modèle d'email par défaut contient déjà la métadonnée **[LINK_DEVIS]**. Si vous avez créé votre propre modèle, assurez-vous d'y inclure cette métadonnée pour permettre à vos clients de consulter et signer le devis en ligne.
[Plus d'info ici](https://intercom-help.eu/vertuoza/fr/articles/196665-comment-puis-je-faire-en-sorte-que-le-texte-de-mes-emails-soit-toujours-le-meme-sans-avoir-a-le-reecrire-a-chaque-fois)
> **Exemple d'e-mail:**
> **Objet : Votre devis [NUMBER_QUOTE] est disponible**
> Cher(e) [CIVILITE_CLIENT] [NOM_CLIENT],
> Veuillez trouver ci-joint le devis portant la référence **[REFERENCE].**
> Vous pouvez consulter et signer ce devis en cliquant sur ce lien : **[LINK_DEVIS]**
> Merci et bonne journée,
> 
> Bien à vous,



### 2. Modèle de document PDF
Le modèle PDF par défaut est configuré pour accepter la signature électronique. Si vous utilisez un modèle personnalisé, vérifiez qu'il contient bien une zone de signature (et une seule). Cela permettra au processus de signature de fonctionner correctement.
[Plus d'info ici](https://intercom-help.eu/vertuoza/fr/articles/132102-modeles-de-documents)

### 


​

Mis a jour le : 19/08/2025
