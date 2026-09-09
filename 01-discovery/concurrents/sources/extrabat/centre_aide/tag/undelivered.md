---
url: https://servicescompris.extrabat.com/tag/undelivered
url_finale: https://servicescompris.extrabat.com:443/tag/undelivered/
date_collecte: 2026-09-09
destination: centre_aide
---

Votre client envoie des emails depuis l'application Extrabat avec son adresse @masociete.com.
Or, le domaine masociete.com n'autorise pas les envois de mail depuis des serveurs différents des siens. Les messages envoyés par l'application sont donc rejetés et vous avez un message d'erreur (voir ci-dessous) :

- Ajouter le paramètre suivant à l'enregistrement SPF du domaine masociete.com : 
 "include:_spf.extrabat.com"
Une fois ceci fait, les serveurs Extrabat seront autorisés à envoyer des emails depuis votre nom de domaine.