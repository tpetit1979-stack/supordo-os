---
url: https://documentation.openfire.fr/knowsystem/cloturer-un-exercice-fiscal-124
url_finale: https://documentation.openfire.fr/knowsystem/cloturer-un-exercice-fiscal-124
date_collecte: 2026-09-06
destination: documentation_2
---

Avant de clôturer un exercice fiscal, il faut d'abord vérifier les données de la balance et le résultat qui se trouvera dans le compte 999999.

En effet, sur OpenFire le résultat est affecté au compte 999999 Profits/pertes non distribués.

Lors de la réaffectation de compte, le cabinet comptable choisira alors s'il souhaite passer une écriture vers le compte de bénéfice (120) ou de perte (129).

Ces données sont accessibles depuis le menu **Comptabilité>Rapport>Rapport comptable/Balance générale.**

## Vérification pièces comptables comptabilisées

Une clôture définitive ne sera possible que si les pièces comptables sur la période définie sont comptabilisées. Pour vérifier l'état des pièces comptables, rendez-vous dans le menu **Comptabilité>Conseiller>Pièces comptables** :

## Verrouillage définitif exercice fiscal

Rendez-vous dans le menu **Comptabilité>Configuration>Configuration**

Cliquer sur Verrouillez les écritures définitivement et noter la date de clôture.

Cette opération est irréversible et la clôture est définitive. La date notée dans la date de verrouillage sera inscrite automatiquement dans Date de verrouillage pour les non-conseillers et dans Date de verrouillage.

Lorsque la clôture est validée, vous trouverez l'information dans Comptabilité>Configuration>Configuration :

**Pour rappel** : Il est possible à tout moment de rééditer les rapports comptables des exercices antérieurs, même si l'exercice est clôturé. Le report à nouveau (dans le journal "OUV") se génère mais n'apparaîtra que lors d'une édition de fichier FEC. Dès que la clôture est effectuée, les écritures du report à nouveau qui se trouvent dans le journal "OUV" ne changera plus et n'apparaît pas dans les écritures comptables. En effet, du fait qu'OpenFire soit un ERP, les écritures des à nouveaux se génèrent mais se lettrent entre elles. Les comptes lettrables (comptes auxiliaires clients et fournisseurs) restent ouverts et donc non lettrés dans les exercices antérieures car ils sont liés à la gestion commerciale (factures) et ils ne peuvent pas être lettrés auxquels cas ils seraient considérés comme soldés.

## Le fichier des écritures comptables

Le fichier des écritures comptables (FEC) est un document reprenant toutes les écritures comptables qui se sont déroulées durant un exercice donné.

Le FEC reprend l’ensemble des enregistrements informatiques qui constituent les écritures comptables de la comptabilité générale. Vous devez être en mesure de présenter un FEC pour chaque exercice comptable clos, avec toutes les écritures comptables enregistrées, y compris les écritures d’à nouveau.

##### Où se trouve le FEC ?

Le fichier des écritures comptables est généré directement par OpenFire. Il est possible d'éditer ce rapport FEC au format csv ou txt en vous rendant dans Comptabilité > Rapports > FEC


Dans la fenêtre qui s’ouvre, il faudra alors sélectionner la plage de date concernée via les champs Start Date et End Date.

Pour votre comptable, il faudra en général sélectionner l'option Non-officiel comptabilisé uniquement.

Vous pouvez également choisir de désélectionner l’option inclure le journal d’ouverture afin de ne pas faire apparaitre les à-nouveaux.