---
url: https://docv5.progbat.com/le-menu-principal/comptabilite/parametrage-comptable/comptes-de-tiers
url_finale: https://docv5.progbat.com/le-menu-principal/comptabilite/parametrage-comptable/comptes-de-tiers
date_collecte: 2026-09-06
destination: centre_aide
---

# Comptes de tiers

## Les comptes

- Définissez le compte de tiers pour chaque type : Fournisseur, client, sous-traitant.
- Le compte pour les acomptes clients, généralement 419xxx, sera utilisé en contrepartie du 411 
  - En effet, les factures d'acompte ne génèrent pas de chiffre d'affaires.
- Le préfixe de compte auxiliaire est requis par certains logiciels de comptabilité. 
  - ACD par exemple utilisera C à la place de 411
  - Quadratus utilisera 9 à la place de 411
  - Dans ces cas, ne pas saisir 411 dans le compte client.

## Les comptes auxiliaires

Les comptes auxiliaires de tiers sont utilisés en comptabilité pour différencier chaque client. Il y a plusieurs manières de paramétrer les comptes auxiliaires :

- **Uniquement le compte auxiliaire saisi dans la fiche du tiers**  - Si aucun compte auxiliaire n'est saisi dans la fiche du tiers, aucun compte auxiliaire ne sera appliqué à l'écriture comptable
- **Numéro interne**  - Chaque Tiers dispose d'un numéro interne, du type 1,2,3,...,1526,1527... Si vous avez saisi le compte client "4111-" et que vous cochez cette option, le compte de chaque tiers sera du type 4111-0001, ..., 4111-0437, ..., 4111-1527, ... (si la taille maximum du compte est de 9 et que vous avez complété avec des zéros à gauche)
- **Identifiant (*****Recommandé*****)**
  - Le logiciel va "fabriquer" le compte auxiliaire à partir de l'identifiant du tiers, en supprimant tout espace ou caractère qui n'est pas une lettre.
  - Par exemple, si l'identifiant est DUPONT LYON, que le compte client est 411, et que vous avez défini 12 caractères maximum, le compte auxiliaire comportera 9 lettres au maximum, et sera DUPONTLYO
  - 💡 **Si vous saisissez un compte auxiliaire dans la fiche d'un Tiers, c'est ce compte qui sera utilisé.
Cette méthode permet donc d'utiliser les comptes auxiliaires automatiques, tout en privilégiant un compte auxiliaire s'il est renseigné.**

Mis à jour