---
source: https://support.openfire.fr/hc/fr/articles/28943804944156-Activer-la-facturation-%C3%A9lectronique-dans-OpenFire-et-connecter-SUPER-PDP
categorie: Configurer OpenFire
titre: Activer la facturation électronique dans OpenFire et connecter SUPER PDP
date_recuperation: 2026-09-05
---

# Activer la facturation électronique dans OpenFire et connecter SUPER PDP

Cet article vous guide pas à pas dans l'activation de la facturation électronique sur votre plateforme OpenFire. Vous y découvrirez comment installer le module requis, paramétrer votre fiche société et connecter votre compte à la plateforme agréée (PA) partenaire : SUPER PDP.

Cet article contient les sections suivantes :

- [Section 1 : Configuration préalable de votre société ](#h_01KXMZX2M0TTAXEAQQZS4YKK10)
- [Section 2 : Accès à la fonctionnalité](#h_01M1P9G1AGZ4T3RYKB158WJM92)
- [](#h_01KXMZX2M0TTAXEAQQZS4YKK10)[Section 3 : Activation et connexion à la Plateforme Agréée Super PDP ](#h_01KXNBD4AB37TCVK7FYRD6JZVJ)
- [Section 4 : Validation de votre format de fichier](#h_01KXNBD4AB828JVCWH3M2CWG87)
- [Bonnes pratiques](#h_01KXNE9Z6MRMZ4F7WS5139RX3M)

##

## Section 1 : Configuration préalable de votre société

Avant de lier votre compte à la plateforme de facturation, vous devez impérativement configurer les informations légales de votre structure.

Suivre le chemin d'accès suivant : Paramètres > Utilisateurs & Sociétés > Votre société

- Sélectionner la fiche de votre société.
- Vérifier et compléter obligatoirement les champs suivants dans l'onglet **Informations générales**

  - **Pays** : doit être défini sur **France ou Belgique**
  - **SIREN** : doit être correctement renseigné avec vos 9 chiffres.
  - **Tax ID** (votre numéro de TVA intracommunautaire) : doit être valide.
- Cliquer sur le bouton **Enregistrer**.

![](https://support.openfire.fr/hc/article_attachments/28943813767452)

| 🚨**Avertissement** : Si vous gérez plusieurs sociétés comptables dans votre base de données, vous devez répéter cette configuration rigoureusement pour chacune d'entre elles. |
| --- |

##

##

## Section 2 : Accès à la fonctionnalité

Pour accéder aux fonctions d'activation de la facturation électronique

- Si vous utilisez notre interface simplifiée : OpenFire > Configuration > Paramètre généraux

![](https://support.openfire.fr/hc/article_attachments/30068408297756)

- Si vous utilisez notre interface standard : Comptabilité > Configuration > Paramètres

![](https://support.openfire.fr/hc/article_attachments/30068408298524)

## Section 3 : Activation et connexion à la Plateforme Agréée Super PDP

Une fois votre société paramétrée, vous devez lier OpenFire à la plateforme SUPER PDP.

| 🚨**Avertissement** : Dans un contexte multi-société, vérifier que vous êtes bien positionné sur la société comptable pour laquelle vous souhaitez faire l'enregistrement. |
| --- |

Pas à pas :

- Faire défiler la page jusqu'à la section **Facturation électronique en France**.
- Sélectionner **SUPER PDP** dans le champ **Plateforme Agréée**.
- Choisir votre méthode d'authentification selon l'un des deux cas de figure possibles :

  - **Option 1 => Code d'autorisation (Délégation de gestion à OpenFire - Recommandé)** : idéal si vous souhaitez que OpenFire gère automatiquement l'envoi, la réception de vos factures et vos lignes d'annuaire. 
    (= gestion déléguée)
  - **Option 2 => Identifiants du client (Gestion autonome)** : si vous préférez créer et gérer vous-même votre compte en autonomie complète à l'extérieur de OpenFire.

Ces deux options sont détaillées ci-dessous ; reportez vous à celle vous concernant.

### Option 1 - Code d'autorisation = Délégation à OpenFire (Recommandé)

Les étapes à franchir :

- Cocher l'option **Code d'autorisation**.
- Cliquer sur le bouton **Enregistrer**.

![](https://support.openfire.fr/hc/article_attachments/28948488689948)

- Cliquer sur le bouton **ONBOARDING** qui apparaît sous le champ.
  Une nouvelle fenêtre d'inscription Super PDP s'ouvre alors dans votre navigateur.

#### **Etape 1. Adresse e-mail**

![](https://support.openfire.fr/hc/article_attachments/28944038446620)

- Renseigner l'**Adresse e-mail** du collaborateur en charge de la configuration (elle servira d'identifiant de connexion).
- Cocher la case pour accepter les Conditions Générales d'Utilisation.
- Cliquer sur **Valider**.
- Saisir le **Code de vérification** reçu instantanément par e-mail de la part de SUPER PDP.

![](https://support.openfire.fr/hc/article_attachments/28944054504732)

- Valider pour passer à l'étape suivante.

#### **Etape 2. Entreprise**

Si vous avez bien renseigné au préalable les données de votre société (SIREN), l'étape 2 sera validée automatiquement.

#### **Etape 3. Accord formel**

Donner votre **Accord formel** en cochant la case pour autoriser l'envoi/la réception des factures et l'inscription dans l'annuaire.

![](https://support.openfire.fr/hc/article_attachments/28944054506012)

Choisir vos préférences d'inscription:

- Cocher ou non l'option **Phase pilote** si vous souhaitez participer et démarrer dès à présent avant le lancement officiel prévu le 01/09/2026.
- Sélectionner l'inscription dans l'annuaire de votre adresse de réception avec effet immédiat ou à la date officielle de la réforme.

#### **Etape 4. Vérification d'identité**

Procéder à la **Vérification d'identité** du représentant légal via le QR code ou le lien direct s'affichant à l'écran à ouvrir sur votre téléphone avec le partenaire Datakeen.

| 🚨**Avertissement** : Pour un parcours de vérification d'identité plus fluide, nous vous conseillons vivement de photographier au préalable le recto et le verso de votre pièce d'identité. L'importation des photos existantes s'avère bien plus stable que la capture d'image en direct via votre téléphone. |
| --- |

![](https://support.openfire.fr/hc/article_attachments/28944038450332)

| 💡**Important **: Si la vérification d'identité automatique via Datakeen échoue, cliquez simplement sur le bouton **Demander une vérification manuelle** afin qu'un membre du support valide votre dossier. Cette validation pourra prendre de quelques minutes à quelques heures.  Pour vérifier l'activation, connectez vous directement à votre compte Super PDP : Navigateur web > Se connecter à votre espace client sur [https://www.superpdp.tech](https://www.superpdp.tech) |
| --- |

| 💡**Important **: si vous avez opté pour la délégation à OpenFire lors de l'enregistrement de votre compte SUPER PDP, vous n'avez peut-être pas encore défini de mot de passe.  Effectuez simplement une **demande de réinitialisation** via le lien "Mot de passe oublié" sur `https://www.superpdp.tech/app/users/reset_password` en utilisant l'adresse e-mail déclarée lors de votre inscription. |
| --- |

![](https://support.openfire.fr/hc/article_attachments/28944054510876)

#### **Etape 5. Autorisation**

Cliquer sur le bouton **Autoriser** pour accorder à OpenFire l'accès à la gestion de vos factures et de votre annuaire sur SUPER PDP.

![](https://support.openfire.fr/hc/article_attachments/28944054514844)

Fermer l'onglet de votre navigateur une fois le message "Onboarding réussi" affiché.

![](https://support.openfire.fr/hc/article_attachments/28944038459676)

#### **Etape 6 - test API**

Vous pouvez ensuite réaliser un TEST API pour vérifier que la connexion à SUPER PDP est bien activée !

![](https://support.openfire.fr/hc/article_attachments/28948665734940)

| 💡**Note **: L’enregistrement devra se faire pour chaque société comptable de votre base que vous souhaitez brancher à Super PDP. |
| --- |

### Option 2 - Identifiant du client = Gestion en autonomie

La gestion en autonomie consiste pour vous à créer et piloter votre compte SUPER PDP seul. 
Dans ce cas de figure, vous avez la responsabilité de la création et de la gestion du compte. Le coût du service SUPER PDP dans ce contexte vous sera facturé directement par SUPER PDP et ne sera pas pris en charge par OpenFire.

![](https://support.openfire.fr/hc/article_attachments/29089243772444)

1. Au niveau de la méthode d'authentification, cocher l'option **Identifiants du client**.
2. Créer votre compte directement sur le portail SUPER PDP à l'adresse suivante : `https://www.superpdp.tech/app/users/create`.
3. Effectuer toutes les étapes requises (SIREN, accords formels, vérification d'identité du dirigeant) directement sur l'interface de SUPER PDP.
4. Copier votre **ID client** et votre **Secret client** générés sur SUPER PDP puis les coller dans les champs correspondants sur OpenFire.
5. Cliquer sur le bouton **Enregistrer**.

##

## Section 4 : Validation de votre format de fichier

Par défaut, le format utilisé pour la communication avec SUPER PDP est le format Factur-X (CII). 
Si vous souhaitez modifier ce format standard au profit d'un autre format prévu par la réforme, veuillez vous rapprocher de votre équipe OpenFire

##

## Bonnes pratiques

- **Tester systématiquement votre connexion** : Une fois votre configuration terminée (par délégation ou en autonomie), cliquez toujours sur le bouton **TEST API**. 
  Un bandeau vert indiquant "Connexion établie avec succès à l'API de SUPER PDP" doit s'afficher en haut à droite pour valider l'opération !
- **Une question ou un blocage ?** si vous avez choisi la délégation, n'hésitez pas à contacter directement votre support OpenFire. Si vous créez votre compte directement sur SUPER PDP, vous pouvez envoyer un message directement à l'équipe technique de la plateforme à l'adresse suivante : `support@superpdp.tech`.

Mis a jour le : 04/09/2026
