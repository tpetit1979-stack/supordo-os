---
url: https://documentation.openfire.fr/knowsystem/gestion-avancee-des-contacts-109
url_finale: https://documentation.openfire.fr/knowsystem/gestion-avancee-des-contacts-109
date_collecte: 2026-09-06
destination: documentation_2
---

Des onglets de gestion, situés au bas de chacune de vos fiches contact, vous permettent de renseigner des informations complémentaires utiles pour votre gestion interne.

## Contacts & Adresses


Cet onglet permet de créer des sous-contacts. Par exemple, si votre client n'habite pas à l'endroit où le chantier est effectué vous aurez besoin d'une adresse d'expédition différente.

- **Contact** : C'est l'adresse principale,
- **Adresse de facturation** : C'est l'adresse où sera envoyée la facture, à renseigner seulement si elle est différente de l'adresse principale.
- **Adresse d'expédition** : Elle correspond à l’adresse du chantier, à remplir dans le cas où les produits vendus ou les prestations réalisées ne situent à une autre adresse.
- **Autre adresse** : Si vous avez une autre adresse utile à renseigner.
- **Adresse personnelle** : Si votre contact est une entreprise mais que vous avez besoin de l'adresse personnelle d'un contact.

 Dans la vue liste des contacts, les adresses secondaires sont présentées comme des contacts à part entière, visuellement rattachées à un contact principal.

## 


Notes internes 


Les notes internes correspondent à un bloc-notes dans lequel vous pouvez ajouter des informations spécifiques à votre contact.

**Notes client** : Ces notes seront affichées dans la rubrique *note client* des devis et planning d'intervention.

**Avertissements**: Cet encart offre la possibilité d'appliquer un message d'avertissement ou bloquant sur un contact. 

Dans cet exemple, le message "Mauvais payeur" apparaitra si j'essaie de fixer un rendez-vous, et le champ du client se videra pour bloquer la prise de rdv. Il en sera de même si j'essaie de créer une opportunité, un devis / bon de commande ou une facture pour ce contact.

## Ventes et achats

Cet onglet permet de préciser le rôle du contact. Par défaut un nouveau contact est de type client prospect, visible via l'icône .

Il existe 4 types de contact :

- Le prospect : Il s'agit d'un contact à qui vous n'avez encore rien vendu.
- Le client : Il s'agit d'un client (particulier ou entreprise) à qui vous avez réalisé des ventes.
- L'utilisateur : Il s'agit de vous, la ou les personne(s) utilisant OpenFire.
- Le fournisseur : C'est l'entreprise à qui vous achetez vos produits.

Dès qu'un devis est validé, le prospect devient automatiquement un client. Cependant il est possible de forcer un statut.

**Vendeur** : Par défaut le vendeur va être l'utilisateur qui a créé et renseigné la fiche client. Vous avez ici la possibilité de renseigner d'autres contacts.

**Référence interne /** Code magasin: vous pouvez créer et utiliser une numérotation pour vos clients. La possibilité de créer des références en interne permet de vous repérer plus facilement. Vous pouvez par exemple utiliser des comptes comptables etc.

**Utilisation données personnelles** : Cet encart est destiné à entrer les préférences RGPD du contact.

## Historique

Cet onglet permet de visualiser en un clin d'œil les tâches réalisées et celles à venir.

En cliquant sur le bouton "Imprimer" à droite, vous pouvez éditer le rapport d'intervention du rendez vous.

## Comptabilité

Dans cet onglet, vous allez pouvoir renseigner toutes les informations utiles à la comptabilité, des comptes auxiliaires à la position fiscale (pour les contacts de type fournisseur) ainsi que la politique de facturation.

Voir en détail la section __[Comptabilité](https://documentation.openfire.fr/knowsystem/comptabilite-154)__

## Marketing

C'est ici que sont centralisées les dernières informations de marketing connues pour le client à savoir la campagne, la source et le canal utilisés.

Ces données sont synchronisées avec le dernière opportunité du pipeline connue du contact.

Plus d'information sur les __[Campagnes marketing](https://documentation.openfire.fr/knowsystem/parametrer-les-campagnes-les-canaux-et-les-origines-197)__

## Localisation

La fonction de géolocalisation permet d'associer les coordonnées GPS à la fiche du contact. Cette fonctionnalité est notamment utilisée dans la gestion des interventions et sur l'application mobile.

 Plus d'information sur la [géolocalisation](https://documentation.openfire.fr/knowsystem/geolocalisation-180)