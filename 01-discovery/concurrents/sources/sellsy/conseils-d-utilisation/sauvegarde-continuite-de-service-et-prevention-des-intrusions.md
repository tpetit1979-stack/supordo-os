---
source: https://help.sellsy.com/fr/articles/12927828-sauvegarde-continuite-de-service-et-prevention-des-intrusions
categorie: Conseils d'utilisation
titre: Sauvegarde, continuité de service et prévention des intrusions
date_recuperation: 2026-09-05
---

# Sauvegarde, continuité de service et prévention des intrusions

![](https://downloads.intercomcdn.com/i/o/p6qpddj1/1848175376/cd8c771c1f96590cc355c93dfebf/image.png?expires=1788635700&signature=8a47ef6f70141e50682347ff1a053158b0f5da31b822e97c669599f8f163c1fe&req=dSgjHsh5mIJYX%2FMW1HO4zdkie%2FdXKsTyuViim99XzIYH14WoOatyxt8FL468%0AatKQEziXIrfsG7yCMxk%3D%0A)

___________________________________________________________

### **Sauvegarde de vos données**

Pour prévenir les risques en cas de panne, de dégâts impactant les locaux (incendie, inondation) ou encore de perte de données résultant d'une attaque informatique, Sellsy met en place un système de sauvegarde complet.

___________________________________________________________

### **Fréquence et conservation des sauvegardes**

Les données sont **sauvegardées automatiquement toutes les nuits** avec une conservation sur **14 jours glissants**.

Une copie supplémentaire est effectuée **chaque semaine**. Cette copie est **chiffrée** et stockée sur un support **S3 AWS**, avec une conservation sur **12 semaines glissantes**.

___________________________________________________________

### **Utilisation des sauvegardes**

Cette sauvegarde permet de pallier la défaillance du système d'information de Sellsy.

Si des données étaient endommagées ou supprimées à la suite d'une mauvaise manipulation de votre part, la restauration serait possible manuellement, sur devis établi en fonction de la complexité de la restauration.

___________________________________________________________

### **Prévention des intrusions informatiques**

La sécurité du réseau de Sellsy repose sur plusieurs dispositifs de protection.

___________________________________________________________

### **Architecture réseau sécurisée**

Chaque service possède son propre réseau, isolé des autres. La protection du réseau local de Sellsy est assurée par un système de pare-feux.

___________________________________________________________

### **Dispositifs de surveillance**

La sécurité des services est garantie par :

- Un **WAF (Web Application Firewall)** qui filtre et protège les applications web
- Un **SIEM** qui supervise l'ensemble des machines
- Une **équipe SOC externalisée** qui surveille et analyse les événements de sécurité en continu

___________________________________________________________

### **Protection du réseau local**

La protection du réseau local de Sellsy est doublement assurée par :

- Un système de pare-feux
- Un système de détection d'intrusion

Chaque service possède son propre réseau, isolé des autres, ce qui limite la propagation en cas d'incident.

___________________________________________________________

### **Prévention des intrusions physiques**

L'accès aux locaux de Sellsy est protégé par des serrures à clés et badges salariés. Toutes les entrées sont placées sous **vidéosurveillance permanente**.

Une **alarme anti-intrusion** connectée à un service de télésurveillance est installée. En cas d'incident, une intervention sur site est immédiatement déclenchée.

Mis a jour le : 08/04/2026
