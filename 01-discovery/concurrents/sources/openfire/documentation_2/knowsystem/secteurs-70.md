---
url: https://documentation.openfire.fr/knowsystem/secteurs-70
url_finale: https://documentation.openfire.fr/knowsystem/secteurs-70
date_collecte: 2026-09-06
destination: documentation_2
---

L'utilisation des secteurs permet de simplifier la planification des tournées d'interventions. La recherche des interventions peut ainsi être optimisée et OpenFire analyse pour vous les secteurs pour vous proposer la meilleure option de planification. Ils sont également utiles dans le cadre de la prise de RDV en ligne.

## Configuration des secteurs

Les Secteurs sont accessibles depuis le menu **Intervention > Configuration > Secteurs**

A la création d'un secteur, plusieurs champs sont à renseigner:

Les secteurs peuvent être définis pour l’activité commerciale, technique ou bien les deux.

La saisie des codes postaux du secteur, individuellement ou par groupe (CP début et CP fin) permet d’auto-affecter les secteurs au contacts concernés.

  *Les secteurs peuvent être affectés manuellement au niveau des contacts mais il existe également une fonctionnalité d'affectation automatique du secteur au moment de la création d'un contact. Cette fonctionnalité est disponible depuis le menu **Intervention > Configuration > Configuration:***

*Si cette option est cochée, un secteur sera automatiquement affecté pour toute création de contact au moment de la saisie de la complétion par ville (code postal et ville).*

Le bouton Actualiser permettra d'ajouter automatiquement les clients ayant un code postal correspondant à ceux du secteur.

Le bouton Actualiser et Supprimer viendra ajouter automatiquement les clients ayant un code postal correspondant à ceux du secteur et supprimer ceux qui n'ont plus de codes postal correspondants.

Attention: si un contact a un code postal qui ne correspond pas mais que vous l'aviez ajouté manuellement, il sera donc supprimé de ce secteur.

Exemple: si un client est affilié à un secteur A et qu'il déménage dans le secteur B, il faudra d'abord "actualiser et supprimer" sur le secteur A avant d'actualiser sur le secteur B. Si son nouveau code postal ne correspond à aucun secteur, il se retrouvera cependant sans secteur attribué.

## Utilisation des secteurs

Une fois les secteurs créés, OpenFire va pouvoir optimiser les tournées lorsque vous planifiez une intervention. Vous devez noter le secteur concerné et le logiciel va pouvoir trouver un RDV adapté:

Ainsi, lors de la recherche de créneaux disponibles:

- Si des codes postaux sont définis dans le secteur, la recherche se limitera aux adresses d’interventions incluses dans les codes postaux définis ;
- Si les codes postaux ne sont pas définis au niveau du secteur, la recherche sera limitée aux contacts qui auront manuellement été ajoutés au secteur ;

   Plus d'information sur la [prise de rdv optimisée](https://documentation.openfire.fr/knowsystem/optimisation-du-planning-89)