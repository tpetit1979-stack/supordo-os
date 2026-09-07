---
url: https://documentation.openfire.fr/knowsystem/migration-des-sav-291
url_finale: https://documentation.openfire.fr/knowsystem/migration-des-sav-291
date_collecte: 2026-09-06
destination: documentation_2
---

Si vous avez utilisé OpenFire avant 2022, il est possible que des interventions de type SAV aient été créées avant l'introduction du menu des Demandes d'interventions.

Les Demandes d'intervention de type SAV ont été conçues pour fusionner le fonctionnement précédemment géré séparément du module Interventions via le module SAV.

À la fin de l'année 2021, les interventions à planifier ont été renommées "Demandes d'interventions" et sont maintenant regroupées dans le menu Interventions > Demandes d'intervention :

Dans cette optique, il est possible de migrer les SAV de manière à ce qu'ils apparaissent au niveau des demandes d'interventions.

## Explications des changements

Tous les champs ont été récupérés pour faciliter la reprise de données des anciennes interventions SAV. Certains ont cependant été repensés, c'est le cas des champs "Garantie", "Payant client" et "Payant fournisseur" maintenant gérés par les champs "Payeur" et "Type de garantie", tous deux disponible dans l'onglet Produit Installé*:*

Le Type de garantie est par ailleurs disponible dans le Parc installé et calculé par rapport à la date de "Fin de garantie".

## Migration des SAV

Une fois que vous vous sentez à l'aise avec l'utilisation des Demandes d'intervention, nous vous encourageons à migrer vos services après-vente actuels vers ce système.

Pour cela, rendez-vous dans le menu **Interventions > Configuration > Configuration**, puis cliquez sur l'option Migrer les SAV:

Une fenêtre s'ouvre alors pour vous permettre de faire la correspondance des étapes kanban de vos SAV vers les étapes kanban des Demandes d'intervention (que vous pouvez créer en amont).

Validez ensuite la migration. Tous vos SAV sont maintenant des Demandes d'intervention de type SAV.