---
url: https://documentation.openfire.fr/knowsystem/configuration-262
url_finale: https://documentation.openfire.fr/knowsystem/configuration-262
date_collecte: 2026-09-06
destination: documentation_2
---

- Rapport à signer par défaut 
: liste du ou des documents à inclure dans le dossier de signature. Devis / Commande (Yousign) doit être mis par défaut.

 A savoir : 
Pour ajouter des documents tels que les modèles de courriers (Attestation TVA, CGV,etc) dans le mail et afin que ces modèles de courriers apparaissent dans le champ Rapport à signer par défaut,  rendez-vous dans les modèles de courriers: 

Ventes>Configuration>Modèle de courriers
L'étiquette 

Bon de commande
 doit être mise dans impression rapide :   

Ensuite, rendez-vous dans le menu 

**Ventes > Configuration > Modèles de requêtes**
 puis cliquez sur 

Modifier.
Vous pourrez alors ajouter les documents de votre choix dans le champ Rapport à signer par défaut :



 Configuration des signataires

Pour chaque modèle de requête, une liste de signataire(s) peut être définie. Appelez le support pour la gestion des signataires. 






## Configuration des emails, notifications et rappels


Configuration du premier email 



Le “premier email” est l’email utilisé lorsque la procédure de signature électronique est transmise aux signataires par email (à ne pas confondre avec l’email pouvant être envoyé en tant que mode d’authentification du signataire). 



Pour ce “Premier email”, vous pouvez configurer un “sujet” type et un modèle de “Corps” sur le même format que les emails standard.

  Attention : il ne faut pas modifier les balises {yousignSignatoryName} et {yousignUrl|Accéder au devis}





Les autres balises utilisées sont des balises standard Odoo : 

- ${object.company_id.name} → Nom de la société émetrice

- ${object.name} → numéro de devis

- ${object.amount_untaxed} → montant HT du devis

- ${object.amount_total} → total TTC du devis 

- ${object.currency_id.name} → devise du devis



Configuration du workflow de notification email



Un workflow de notifications email peut être mis en place pour chaque étape clé du processus de signature : procédure créée, terminée, refusée, expirée, nouveau signataire et nouveau commentaire. Par défaut, seule une notification pour la procédure terminée est paramétrée. Contactez le support pour modifier le workflow de notification.



Configuration des règles de rappel



Pour augmenter les chances de succès d’une procédure de signature électronique, un workflow de relance (=rappel) des signataires peut être mis en place :





Détail des champs : 

- Intervalle des rappels = définit le nombre de jours d’intervalle entre deux relances par email du signataire ;

- Nombre limite de rappels = définit le nombre de relance maximum au signataire ;

- Sujet du mail de rappel = sujet de l’email utilisé pour la relance du signataire ;

- Corps du mail de rappel = corps de l’email utilisé pour la relance du signataire.