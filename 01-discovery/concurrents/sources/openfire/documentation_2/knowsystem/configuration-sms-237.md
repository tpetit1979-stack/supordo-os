---
url: https://documentation.openfire.fr/knowsystem/configuration-sms-237
url_finale: https://documentation.openfire.fr/knowsystem/configuration-sms-237
date_collecte: 2026-09-06
destination: documentation_2
---

## Configuration des alertes

Les alertes sont configurables depuis le menu  Configuration > SMS > Configuration

Nous pouvons définir les destinataires des alertes :

Intervenants : techniciens en charge des interventions (en théorie si les techniciens n’ont pas l’application Mobile !)

Clients : tous les clients qui recevrons un SMS la veille de notre intervention

Les techniciens ne sont généralement pas destinataires sauf s’ils sont des intervenant externes.

## Configuration OpenFire


Configuration de la passerelle SMS

Module **Configuration > SMS > Compte passerelle**

1. Compte OpenFire (nom interne, Fournisseur & Entreprise)
2. Passerelle –> Choix dans la liste, seulement OVH à ce jour !
3. Compte SMS chez OVH
4. Utilisateur API chez OVH
5. Mot de passe de l’utilisateur API chez OVH
6. Utilisateur API chez OVH (idem 4)
7. Expéditeur défini chez OVH. **Attention** : il ne doit pas y avoir d'espace dans le nom.
8. Compte OpenFire (idem 1)

## Définition des modèles de SMS

Le modèle de SMS Rappel automatique RDV est configuré lors de l’installation.

Ces modèles sont configurables depuis le menu Configuration > SMS > Modèles:

1. Nom du modèle
2. Objet associé au modèle : Planning, Client, …
3. Utilisateur API chez OVH
4. Expéditeur chez OVH : apparait en début de SMS
5. Destinataire : vide dans le modèle, rempli automatiquement à l’envoi du SMS
6. Texte du SMS avec les balises de publipostage