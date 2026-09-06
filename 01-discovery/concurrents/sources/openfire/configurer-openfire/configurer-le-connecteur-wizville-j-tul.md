---
source: https://support.openfire.fr/hc/fr/articles/26297092194332-Configurer-le-connecteur-Wizville-J%C3%B8tul
categorie: Configurer OpenFire
titre: Configurer le connecteur Wizville Jøtul
date_recuperation: 2026-09-05
---

# Configurer le connecteur Wizville Jøtul

Wizville est une solution d’enquête de satisfaction en continu pour les réseaux de points de vente permettant aux clients de partager leur avis en répondant à un court questionnaire de satisfaction.

Dans le cadre de son partenariat avec OpenFire, Jøtul a souhaité développer un connecteur Wizville pour vous permettre de solliciter des avis clients, directement depuis votre base OpenFire, suite à la pose d'un appareil Jøtul, et de réceptionner les avis clients émis.

**Cette fonctionnalité est dédiée aux concessionnaires Jøtul. Elle nécessite l'installation d'un module dédié. Pour cela, vous rapprocher de support@openfire.fr**

Cet article contient les sections suivantes:

- [Configurer le connecteur Wizville Jøtul](#h_01KMCWR8A4J136FXNAG12TQ9E6)
- [Mettre en place le connecteur pour une société](#h_01KMCWR8A4J136FXNAG12TQ9E6)
- [Configurer des catégories comme "Article principal"](#h_01KMCWR8A4J136FXNAG12TQ9E6)

---

### Configurer le connecteur Wizville Jøtul

Chemin d'accès: *Paramètres > Wizville > Connecteurs Wizville.*

Un connecteur "Wizville Jøtul" est pré-configuré avec les paramètres nécessaires pour se connecter au serveur Wizville, y déposer et y récupérer les fichiers des informations clients sollicités pour un avis.

- **Connexion SFTP: **Ces paramètres vous permettent de vous connecter au serveur Wizville
- **Export: **
  Votre base OpenFire déposera quotidiennement sur le serveur Wizville un fichier avec les informations issues des factures de votre base concernant les clients à contacter pour solliciter un avis Wizville.
  - **Dossier de dépôt: **le nom du dossier sur le serveur Wizville où votre base déposera le fichier contenant les informations des clients à solliciter
  - **Nom du fichier d'export: **le nom du fichier généré par votre base, il contient la date du jour et votre identifiant Wizville
- **Import:**
  Votre base OpenFire récupérera quotidiennement les réponses des avis clients sollicités par Wizville.** **
  - **Dossier des réponses: **le nom du dossier sur le serveur Wizville où votre base récupérera le fichier des réponses clients
  - **Nom du fichier d'import: **le nom du fichier Wizville contenant les réponses des clients sollicités. Il contient la date du jour et votre identifiant Wizville.
- **Configuration du questionnaire**
  Le questionnaire envoyé par Wizville contient en particulier deux questions dont les réponses seront inscrites dans la fiche client sur votre base OpenFire.
  - **N° de question pour la satisfaction globale: **par défaut, 1
  - **N° de question pour le score NPS (Net Promoter Score): **par défaut, 2. 
    "Le NPS ou Net Promoter Score (NPS ®) ou taux de recommandation net est un indicateur permettant de mesurer la satisfaction et le degré de fidélisation de vos clients. [...] Exemple de question NPS: « Recommanderiez ce produit, service ou point de vente à vos amis ou collègues ? » / « Recommanderiez-vous cette entreprise à un ami ? 0= Pas du tout, 10= Tout à fait » (Source: Wizville.com)
- **Sélection des factures**
  Le connecteur Openfire <> Wizville se base sur vos factures émises pour connaître la liste des clients à solliciter.
  - **Marques: **Les marques pour lesquelles vous souhaitez solliciter des avis clients. Ici Jøtul uniquement.
  - **Filtre sur les factures: **Le filtre qui sélectionnera les factures donnant lieu à la sollicitation d'un client. Par défaut les critères sélectionnés sont:
    - Facture client
    - Facture comptabilité (pas de brouillon)
    - Facture contenant un produit principal
    - Facture d'un montant supérieur ou égal à 900€
    - Facture n'ayant pas déjà donné lieu à l'émission d'un avis Wizville

| 💡**Note **: Dans la configuration du filtre, nous ajouterons la date limite à partir de laquelle vous souhaitez que les facture soient sélectionnées pour sollicitation Wizville. |
| --- |

### Mettre en place le connecteur pour une société

Chemin d'accès: *Paramètres >Paramètres des connecteurs > Gestion des connecteurs Wizville.*

Vous pouvez mettre en place autant de connecteurs Wizville que vous avez d'identifiants Wizville (souvent 1 par société). L'identifiant Wizville est un identifiant qui vous est communiqué par Wizville lorsque vous souscrivez au service.

Par exemple, votre identifiant Wizville pourrait-être *jotul-allaire.*

![](https://support.openfire.fr/hc/article_attachments/26308773829148)

Les paramètres à renseigner sont:

- **Connecteur Wizville: **le connecteur précédemment configuré
- **Société associée au connecteur: **La société pour laquelle vous souhaitez configurer le connecteur Wizville
- **Identifiant Wizville: **L'identifiant Wizville de la société (fourni par Wizville)

### Configurer des catégories comme "Article principal"

Les factures éligibles à l'envoi d'une sollicitation Wizville sont les factures qui contiennent au moins un "article principal" de la marque configurée dans le connecteur Wizville.

Chemin d'accès: *Vente > Configuration > Catégories de produits*

![](https://support.openfire.fr/hc/article_attachments/26308933504284)

Vous devez donc définir quelles catégories de produit sont considérées comme des catégories "Article Principal". Pour cela, il suffit de cocher la case "Article principal" dans la catégorie de produit.

Dans la configuration de la marque "Jøtul", les catégories d'origine doivent correspondre à une catégorie dans votre base OpenFire. Si la catégorie d'origine concerne un appareil, la catégorie de produit correspondant dans votre base doit avoir la case "Article principal" cochée.

![](https://support.openfire.fr/hc/article_attachments/26308933505820)

  **📓**Pour aller plus loin →
  [Utiliser le connecteur Wizville](https://support.openfire.fr/hc/fr/articles/26309314521756)

Mis a jour le : 23/03/2026
