---
url: https://documentation.openfire.fr/knowsystem/relations-273
url_finale: https://documentation.openfire.fr/knowsystem/relations-273
date_collecte: 2026-09-06
destination: documentation_2
---

Pour une meilleure lecture de vos contacts, OpenFire vous permet de créer et de gérer les relations entre ceux-ci.

Cette fonctionnalité peut ne pas être nativement présente sur votre base : rapprochez-vous du support Openfire pour son installation.

## Configuration des relations


Pour configurer les relations possibles entre contacts, rendez-vous dans le module **Ventes>Configuration>****Types de relation de partenaire.**

Nom : définit le qualificatif contact selon la relation que vous voulez créer. Par exemple : "est le propriétaire de" ;

Nom inverse : définit le pendant au champ précédent. Par exemple : "est le locataire de" ;

Type de partenaire (de gauche ou de droite) : définit si le contact est une personne ou une organisation ;

Catégorie du partenaire (de gauche ou de droite) : définit l'étiquette requise sur le contact pour qu'il puisse être qualifié du nom de la relation correspondante. Par exemple, pour être qualifié de "est le propriétaire de", le contact doit au préalable avoir l'étiquette "Copropriété" ;

Réflexif : si coché, cette relation peut être configurée avec le même partenaire à gauche et à droite ;

Symétrique : si coché, cette relation est la même de droite à gauche que de gauche à droite. Par exemple, la relation "est le colocataire de" est symétrique car si le contact A est le colocataire du contact B, le contact B est également le colocataire du contact A ;

Invalid relation handling : lors de l'ajout de critères de relations tels que le type et la catégorie de partenaire sont cochés : *ne pas autoriser les modifications qui entraîneront des relations non valides* OU a*utoriser les relations existantes qui ne correspondent pas aux conditions modifiées* OU t*erminer les relations par aujourd'hui, si elles ne correspondent pas aux conditions modifiées* OU *supprimer les relations qui ne correspondent pas aux conditions modifiées.*

## Ajouts des relations aux contacts

Une fois vos types de relations configurées, rendez-vous dans vos contacts et cliquez sur l'un d'eux. Cliquez sur le smart button "Relations" à gauche. C'est ici que vous verrez les relations de votre contacts et que vous pourrez en créer/modifier/supprimer.

Vous pourrez y adjoindre des dates de début et/ou de fin pour des relations appelées à se terminer à un moment donné.

Les relations sont purement informatives et n'induisent aucune action automatique sur les devis, bons de commande, factures etc.

 Plus d'information sur la [gestion avancée des contacts](https://documentation.openfire.fr/knowsystem/gestion-avancee-des-contacts-109)