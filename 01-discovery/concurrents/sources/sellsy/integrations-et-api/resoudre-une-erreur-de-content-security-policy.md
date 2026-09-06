---
source: https://help.sellsy.com/fr/articles/5876640-resoudre-une-erreur-de-content-security-policy
categorie: Intégrations et API
titre: Résoudre une erreur de “Content-Security-Policy”
date_recuperation: 2026-09-05
---

# Résoudre une erreur de “Content-Security-Policy”

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/2159335561/4774efe5406174d5bfe5090e75fc/FAQ-Bannie%CC%80reAcademy-2+%282%29.png?expires=1788635700&signature=15cf83ba0fd50d01a1a7bf00bc9d113991a279c5b358dc99964bd026cd1d79c0&req=diEiH8p9mIRZWPMW1HO4zbMXlS0h6S9Vt4xA1V%2ByT5cBRqBDme1Vf4w8bb4F%0ANIYhdDycVxR%2FAqKw3C4%3D%0A)

Lors du chargement du widget Sellsy sur votre site internet, vous pouvez obtenir une erreur de Content-Security-Policy".

Pour corriger cela vous devez ajouter le domaine de sellsy.fr et sellsy.com dans votre déclaration CSP.

Ajoutez les informations suivantes sur la configuration de votre serveur :

- [https://*.sellsy.com](https://help.sellsy.com/hc/widget-sellsy/comment-resoudre-une-erreur-de-content-security-policy#)

- [https://*.sellsy.fr](https://help.sellsy.com/hc/widget-sellsy/comment-resoudre-une-erreur-de-content-security-policy#)

**Par exemple :** via un fichier htaccess

< IfModule mod_headers.c>
Header set Content-Security-Policy "default-src [https://*.sellsy.fr ](https://%2A.sellsy.fr/)[https://*.sellsy.com;"
​](https://%2A.sellsy.com%3B/)< /IfModule>

Mis a jour le : 13/03/2026
