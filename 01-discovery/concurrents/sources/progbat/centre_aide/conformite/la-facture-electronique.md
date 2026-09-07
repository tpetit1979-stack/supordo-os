---
url: https://docv5.progbat.com/conformite/la-facture-electronique
url_finale: https://docv5.progbat.com/conformite/la-facture-electronique
date_collecte: 2026-09-06
destination: centre_aide
---

# La facture électronique

Cet article concerne exclusivement les utilisateurs de ProGBat en France.

Bien plus que le simple pdf que vous éditez et envoyez par mail à votre client, **la facture électronique** est à la fois : 

- ce document pdf, tel que vous le connaissez, que l'on peut lire sur un écran ou imprimer,
- et un fichier contenant les données de la facture, "caché" dans le pdf.

On appelle ce format **la "Factur-X".** *(en savoir plus sur* *https://fnfe-mpe.org/factur-x/**)*

## Un document mixte

⚡ Ainsi, la facture électronique est à la fois lisible par un humain (le pdf) et par un système informatique (le fichier de données), ce qui va faciliter les échanges de factures entre entreprises, entre l'entreprise et son expert-comptable, et entre l'entreprise et l'Etat.

## Le vocabulaire de la facture électronique

Voici les principaux termes à connaître pour aborder sereinement la réforme de la facture électronique.

- **Factur-X** : c'est le format du fichier de la facture électronique.
  - Il s'agit d'un document pdf, intégrant un fichier de données au format XML.
- **SC** : Solution Compatible (anciennement OD)
  - Il s'agit le plus souvent de votre logiciel de facturation, comme ProGBat.
  - La SC se charge de générer automatiquement des factures au format Factur-X, et de les transmettre à votre PA.
  - La SC pourra également récupérer automatiquement les factures de vos fournisseurs sur votre PA pour les consulter et les traiter directement sur ProGBat.
- **PA** : Plateforme Agréée (anciennement PDP).
  - Lorsque vous finalisez une facture sur ProGBat, celle-ci est générée au format Factur-X, et déposée automatiquement et en temps réel sur votre PA.
  - La PA se charge de transmettre les données de la facture (la partie XML) au concentrateur de l'Etat (anciennement appelé PPF), et : 
    - Si la facture s'adresse à un professionnel (BtoB), ou à l'Etat (BtoG), elle sera transmise à la PA de votre client, qui peut être différente de la vôtre. On appelle cela le e-invocing.
    - Si la facture s'adresse à un particulier (BtoC), les données fiscales seront transmises à l'Etat à interval régulier, on appelle cela le e-reporting. Dans ce cas, bien sur, vous devrez transmettre la facture à votre client comme d'habitude, par mail ou par courrier.

## 💡Choisir sa PA

- Il s'agit de plateformes privées, agréées par l'Etat. Au 29/07/2026, 153 plateformes sont agréées et disponibles.
- Vous avez le choix de la PDP que vous souhaitez utiliser, chacune proposant ses propres offres commerciales et ses propres services complémentaires à leurs obligations légales.
- ProGBat propose 3 PA, comprises dans votre licence : 
  - Pennylane, idéal si votre expert-comptable utilise lui-même Pennylane pour votre comptabilité,
  - Qonto, idéal si vous possédez ou souhaitez souscrire à un compte pro (banque en ligne) Qonto. Mais vous pouvez choisir la PA Qonto sans ouverture de compte pro.
  - SuperPDP, plateforme indépendante de tout outil ou service commercial.

La liste des PA est disponible ici : [https://www.impots.gouv.fr/je-consulte-la-liste-des-plateformes-agreees](https://www.impots.gouv.fr/je-consulte-la-liste-des-plateformes-agreees)

- **PPF** : Plateforme Publique de Facturation
  - la PPF, qui devait permettre de déposer gratuitement vos factures sans passer par une PA a finalement été abandonnée par l'Etat, dont le rôle se limite maintenant à réceptionner les factures transmises par les PA, et à maintenir l'Annuaire des entreprises.
- **L'Annuaire des entreprises**
  - Cet annuaire permet de recenser l'ensemble des entreprises de France, et de préciser quelle PA est rattachée à chacune d'elle.
  - Chaque entreprise est identifiée dans l'annuaire par son numéro SIREN, plus éventuellement un suffixe. Pour la majorité des entreprises, le numéro de SIREN constitue l **'adresse de facturation électronique.**
    - **Pensez à communiquer votre adresse de facturation électronique à vos fournisseurs.**

## Le calendrier de la facture électronique

Plusieurs fois reportée, la réforme est désormais fixée comme suit :

- ▶️ **Septembre 2026**  - Obligation pour **les grandes entreprises** d'émettre des factures électroniques.
  - Obligation pour **toutes les entreprises** de recevoir des factures électroniques.

- ▶️ **Septembre 2027**
  - Obligation pour **toutes les entreprises** d'émettre et de recevoir des factures électroniques.
  - Pour vos clients "particuliers", obligation de e-reporting

Mis à jour