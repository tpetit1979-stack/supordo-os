---
url: https://documentation.openfire.fr/knowsystem/configurer-mes-relances-144
url_finale: https://documentation.openfire.fr/knowsystem/configurer-mes-relances-144
date_collecte: 2026-09-06
destination: documentation_2
---

La relance de factures impayées peut-être effectuée depuis OpenFire. Différents délais de relance peuvent être définis, et un modèle de mail de relance de factures peut être créé pour chaque étape.

Si vous n'avez pas le module de Relance, merci de contacter le support à ***support@openfire.fr***.

## Configurer mes relances



Accès : **Comptabilité > Configuration > Étapes de relance facture.** Par défaut, 3 étapes sont configurées dans votre base. Il est possible de définir des délais avant relance.

Vous pouvez indiquer le moment où doit se déclencher cette relance en indiquant la Date de déclenchement ainsi que le nombre de jours après cette date (nombre de jours par rapport à la date d’échéance de votre facture ou encore par rapport à la dernière relance).

Sélectionnez ensuite le modèle de mail lié à cette relance. Vous pouvez paramétrer autant de relances que vous le souhaitez:

Par exemple, ci-dessous l'étape de la première relance va être indiquée dans la facture 8 jours après la date de l'échéance de la facture :

Sur la facture, cette information se trouvera dans Autres informations :

 **A Savoir:** L'étiquette 'A relancer' est automatiquement attribuée aux factures ouvertes en fonction de leur date d'échéance. Cette action est effectuée quotidiennement. Une tâche planifiée vérifie chaque jour toutes les dates d'échéance des factures ayant le statut 'Ouverte'.