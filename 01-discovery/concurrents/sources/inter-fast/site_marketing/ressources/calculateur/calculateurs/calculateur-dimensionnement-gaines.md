---
url: https://inter-fast.fr/ressources/calculateur/calculateurs/calculateur-dimensionnement-gaines
url_finale: https://inter-fast.fr/ressources/calculateur/calculateurs/calculateur-dimensionnement-gaines
date_collecte: 2026-09-07
destination: site_marketing
---

# Calculateur de dimensionnement de gaines aérauliques

Déterminez le **diamètre de gaine** adapté à votre débit d'air et à la vitesse cible du local. Section circulaire ou rectangulaire, vérification instantanée de la vitesse réelle.

## 💨 Dimensionnement gaines

Diamètre de gaine selon débit et vitesse

Sur un chantier de ventilation, la question revient à chaque tronçon : « quel diamètre je mets là ? ». Trop petit, la gaine siffle et le ventilateur s'essouffle ; trop gros, on perd de la place en faux plafond et on paie de la tôle pour rien. Le **dimensionnement aéraulique** repose sur un principe simple : à débit imposé, c'est la **vitesse de l'air** qu'on choisit qui fixe la section. Ce calculateur convertit votre **débit en m³/h** et la vitesse cible du local en un diamètre de gaine normalisé, puis vérifie la vitesse réellement obtenue.

## Comment se calcule le diamètre d'une gaine ?

Tout part de l'**équation de continuité** : le débit volumique `Q` qui traverse une gaine est égal au produit de la vitesse de l'air `V` par la section de passage `A`. On en déduit la section nécessaire, puis le diamètre d'une gaine circulaire :

| Étape | Formule | Remarque | 
|---|---|---|
| Débit en m³/s | Q <sub>s</sub> = Q<sub>(m³/h)</sub> ÷ 3 600 | Conversion préalable | 
| Section de passage | A = Q <sub>s</sub> ÷ V | V = vitesse moyenne cible | 
| Diamètre circulaire | D = √(4A ÷ π) | Puis arrondi au standard supérieur | 
| Vitesse réelle | V <sub>r</sub> = Q<sub>s</sub> ÷ A<sub>std</sub> | Recalculée sur le Ø normalisé | 

La **vitesse cible** dépend du type de local et du tronçon. Le calculateur prend la moyenne de la plage recommandée, puis arrondit au diamètre normalisé immédiatement supérieur dans la série standard (100, 125, 150, 160, 180, 200, 224, 250, 280, 315, 355, 400 mm…). Il recalcule enfin la vitesse réelle dans cette section et indique si elle reste conforme.

| Type de local | Gaine principale | Secondaire | Bouche | 
|---|---|---|---|
| Résidentiel | 3–5 m/s | 2,5–4 m/s | 1,5–2,5 m/s | 
| Tertiaire | 5–8 m/s | 4–6 m/s | 2–3,5 m/s | 
| Industriel | 8–12 m/s | 6–9 m/s | 3–5 m/s | 

**Une fois le diamètre fixé, vérifiez les pertes de charge du réseau.**

Enchaînez avec notre [**calculateur de pertes de charge**](https://inter-fast.fr/ressources/calculateur/calculateurs/calculateur-pertes-de-charge), ou convertissez une puissance en débit hydraulique avec le [**calculateur de débit d'eau**](https://inter-fast.fr/ressources/calculateur/calculateurs/calculateur-debit-eau).

## Exemple chiffré : une gaine principale à 500 m³/h

Prenons les valeurs par défaut : un **débit de 500 m³/h** sur la **gaine principale** d'un local **résidentiel**, en section circulaire. La plage cible est 3–5 m/s, soit une vitesse moyenne de 4 m/s.

- **Débit en m³/s** : 500 ÷ 3 600 ≈**0,139 m³/s**
- **Section nécessaire** : 0,139 ÷ 4 ≈**0,0347 m²**
- **Diamètre calculé** : √(4 × 0,0347 ÷ π) ≈**210 mm**
- **Diamètre normalisé** : on retient le**Ø 224 mm** (premier standard ≥ 210)
- **Vitesse réelle** dans le Ø 224 : ≈**3,5 m/s** → conforme (≤ 5 m/s)

En section rectangulaire, le calculateur propose un format de l'ordre de 2:1 (largeur ≈ 2 × hauteur) offrant la même section utile, pratique lorsque la hauteur de faux plafond est contrainte.

## 3 erreurs fréquentes en dimensionnement de gaines

### 1. Garder le même diamètre du collecteur à la bouche

Le débit diminue à chaque dérivation : conserver le diamètre principal jusqu'aux bouches donne des vitesses ridiculement faibles et un réseau hors de prix. Redimensionnez **tronçon par tronçon** avec le débit réel de chaque branche.

### 2. Pousser la vitesse pour gagner de la place

Réduire le diamètre fait gagner du faux plafond, mais le bruit et les pertes de charge augmentent vite. Au-delà des plages recommandées, le confort acoustique se dégrade et le ventilateur consomme davantage.

### 3. Oublier de revenir au diamètre normalisé

Le diamètre « calculé » n'existe pas en rayon : il faut toujours retenir le format standard supérieur et **revérifier la vitesse réelle** dans cette section, ce que fait automatiquement le calculateur.

## Du dimensionnement au devis signé, sans ressaisie

Une fois le réseau dimensionné, transformez-le en chiffrage propre : [le logiciel de devis & factures InterFast](https://inter-fast.fr/fonctionnalites/logiciel-devis-factures) vous aide à éditer des devis CVC clairs et à suivre la marge chantier. [Testez InterFast gratuitement](https://inter-fast.fr).