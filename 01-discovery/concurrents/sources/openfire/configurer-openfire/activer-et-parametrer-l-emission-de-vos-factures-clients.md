---
source: https://support.openfire.fr/hc/fr/articles/29465837149212-Activer-et-param%C3%A9trer-l-%C3%A9mission-de-vos-factures-clients
categorie: Configurer OpenFire
titre: Activer et paramétrer l'émission de vos factures clients
date_recuperation: 2026-09-05
---

# Activer et paramétrer l'émission de vos factures clients

Dans le cadre de la réforme de la facturation électronique, cet article vous guide pas à pas dans la configuration de l'émission de vos factures clients dans OpenFire. Vous découvrirez comment choisir le bon format de fichier, automatiser le traitement des rejets et paramétrer la synchronisation de l'annuaire pour sécuriser vos envois.

Cet article contient les sections suivantes :

- [Chemin d’accès de la fonctionnalité](#h_01KZGQ4PW7E5X2KMM4RN85MS2Q)
- [Configuration de l'émission des factures clients](#h_01KZGQ4PW7TNHW1NS1V2BDAK67)

  - [Étape 1 : Choisir le format d'envoi de la facture](#h_01KZGQ4PW7XHZYFS7N9JAYQ5HF)
  - [Étape 2 : Définir la gestion des avertissements et notifications](#h_01KZGQ4PWGZ19DEKQ953AB35ZH)
  - [Etape 3 : Gérer l'envoi des factures pour les clients privés](#h_01KZPJFWC6HDYXAFBKA612034P)
  - [Étape 4 : Paramétrer la synchronisation de l'annuaire](#h_01KZGQ4PWMV7Z0A3745T7Q8CQZ)
- [Bonnes pratiques](#h_01KZGQ4PX2M3KAYMS4HJ7XEH78)

## Chemin d’accès de la fonctionnalité

`Suivre le chemin d'accès suivant : Comptabilité > Configuration > Paramètres > Facturation électronique.`

![](https://support.openfire.fr/hc/article_attachments/29466171300892)

## Configuration de l'émission des factures clients

### Étape 1 : Choisir le format d'envoi de la facture

Dans le champ **Format d'envoi de facture**, sélectionnez le format sous lequel vos factures clients seront transmises à la Plateforme Agréée :

- **Factur-X (par défaut)** : format hybride PDF/XML, lisible à la fois par les humains et les systèmes informatiques. C'est le format recommandé pour la majorité des entreprises.
- **UBL XML avec fichier PDF intégré** : format structuré XML UBL auquel est attaché le fichier PDF visualisable.
- **UBL XML** : format XML UBL pur, sans fichier PDF associé.
- **CII XML avec fichier PDF intégré** : format structuré XML CII incluant le fichier PDF.
- **CII XML** : format XML CII pur, sans fichier PDF.

### Étape 2 : Définir la gestion des avertissements et notifications

Lorsqu'un événement d'avertissement est renvoyé par la Plateforme Agréée (par exemple en cas d'incohérence de données ou de format), OpenFire peut attribuer automatiquement des activités (tâches à réaliser) aux personnes concernées :

**Activité effectuée par le créateur de la facture lorsqu'un événement d'avertissement est reçu** :

- **Activé (par défaut)** : l'utilisateur ayant créé la facture reçoit automatiquement une activité à réaliser pour vérifier le document.
- **Désactivé** : le créateur ne reçoit aucune tâche.

**Activité effectuée par le vendeur de la facture lorsqu'un événement d'avertissement est reçu** :

- **Activé (par défaut)** : le commercial ou vendeur associé à la facture reçoit automatiquement une activité.
- **Désactivé** : le vendeur ne reçoit aucune tâche.

### Etape 3 : Gérer l'envoi des factures pour les clients privés

**Désactiver l'envoi automatique des factures pour clients privés** : permet de bloquer l'envoi automatique des factures vers les clients particuliers (non référencés dans l'annuaire).

- **Activé** : les factures destinées aux particuliers ne sont pas transmises à la plateforme.
- **Désactivé (par défaut)** : les factures sont envoyées normalement.

### Étape 4 : Paramétrer la synchronisation de l'annuaire

Pour s'assurer que vos clients sont bien enregistrés dans l'annuaire central de facturation électronique, vous devez définir la fréquence et les conditions de synchronisation.

#### Synchronisation lors de la validation des factures ou commandes

**Synchronisation de l'annuaire lors de la validation des factures** :

- **Oui, toujours** : la synchronisation est obligatoire.
- **Oui, si l'annuaire est accessible (par défaut)** : la synchronisation est tentée. En cas d'indisponibilité de l'annuaire, la validation de la facture n'est pas bloquée.
- **Non** : aucune synchronisation n'est effectuée lors de la validation.

| 🚨**Avertissement** : Si vous choisissez l'option « Oui, toujours », la validation de vos factures sera bloquée en cas d'indisponibilité de l'annuaire. Privilégiez l'option « Oui, si l'annuaire est accessible » pour éviter toute interruption d'activité. |
| --- |

**S****ynchronisation de l'annuaire lors de la validation d'une commande client** :

- **Oui, toujours** : la synchronisation est obligatoire et bloque la confirmation du bon de commande si l'annuaire ne répond pas.
- **Oui, si l'annuaire est accessible (par défaut)** : la synchronisation est exécutée sans bloquer la confirmation en cas d'erreur de connexion.
- **Non** : aucune synchronisation lors de la confirmation du bon de commande.

#### Fréquence et délais de rafraîchissement des partenaires

**Synchronisation de l'annuaire lors de la confirmation d'une commande client si la dernière synchronisation a été réalisée il y a plus de X jours** : définit le nombre de jours au-delà duquel les données d'un client doivent être rafraîchies lors de la commande.

Valeur par défaut : **30 jours**.

| 💡**Note **: Un partenaire dont les informations ont été synchronisées récemment ne sera pas interrogé de nouveau, ce qui optimise la rapidité du système. |
| --- |

**Synchronisation de l'annuaire du partenaire si la dernière synchronisation remonte à plus de X Jours** : définit le délai avant de revérifier un partenaire lors de la validation d'une facture.

Valeur par défaut : **30 jours**.

**Synchronisation de l'annuaire d'un partenaire privé inactif si la dernière synchronisation remonte à plus de X jours** : détermine l'intervalle de vérification des clients privés inactifs dans l'annuaire.

Valeur par défaut : **7 jours**.

| 💡**Note **: Les partenaires inactifs doivent être contrôlés plus fréquemment, car ils sont susceptibles d'activer leur adresse de facturation électronique à tout moment. |
| --- |

## Bonnes pratiques

- **Testez votre connexion** : Après avoir configuré l'authentification, cliquez systématiquement sur le bouton **Test API** pour vérifier que la liaison est opérationnelle avant de transmettre vos factures.
- **Vérifiez la conformité EN16931** : Utilisez le bouton de vérification de la norme EN16931 avant le passage en production pour éviter les rejets de factures par la plateforme.
- **Conservez les envois automatiques activés** : Laissez l'inversion automatique et les notifications activées pour assurer un suivi fluide et réactif en cas de problème.
- **Surveillez les activités d'avertissement** : Assurez-vous que les créateurs et vendeurs traitent leurs tâches attribuées afin de corriger rapidement les éventuelles erreurs sur les factures émettant un avertissement.
- **Ajustez la fréquence de synchronisation** : Si votre volume de transactions ou votre base clients est très important, ajustez les délais de rafraîchissement pour conserver un annuaire toujours à jour sans alourdir les temps de traitement.

Mis a jour le : 25/08/2026
