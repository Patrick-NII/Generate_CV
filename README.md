# Génération de Base de Données de CV

Ce projet génère une base de données fictive de CV en utilisant Python, Faker et Pandas. Il crée un fichier JSON et CSV contenant des informations détaillées sur des candidats fictifs dans divers domaines professionnels. Ce projet est utile pour les tests, la démonstration de logiciels ou les analyses de données.

## Table des Matières

- [Installation](#installation)
- [Usage](#usage)
- [Structure des Données](#structure-des-données)
- [Démarche](#démarche)
- [Contributions](#contributions)
- [Licence](#licence)

## Installation

1. Clonez le dépôt sur votre machine locale :

    git clone https://github.com/Patrick-NII/Generate_CV.git
   
## Usage

3. Les fichiers `cv_data.json` et `cv_data.csv` seront générés dans le répertoire courant.

## Structure des Données

Les CV générés contiennent les champs suivants :

- **ID** : Identifiant unique du CV
- **prenom** : Prénom du candidat
- **nom** : Nom du candidat
- **adresse** : Adresse du candidat
- **email** : Adresse email du candidat
- **numero_de_telephone** : Numéro de téléphone du candidat
- **intitule** : Intitulé du poste actuel ou recherché
- **diplome** : Diplômes obtenus
- **experiences** : Liste des expériences professionnelles
  - **intitulé_poste** : Intitulé du poste
  - **entreprise** : Nom de l'entreprise
  - **date_debut** : Date de début de l'emploi
  - **date_fin** : Date de fin de l'emploi
  - **description** : Description du poste
- **educations** : Liste des formations
  - **diplome** : Intitulé du diplôme
  - **ecole** : Nom de l'école
  - **annee** : Année d'obtention
- **langues** : Langues parlées et niveaux de compétence
- **competences_techniques** : Compétences techniques spécifiques au domaine
- **competences_humaines** : Compétences humaines
- **recommendations** : Liste des recommandations
  - **nom** : Nom du référent
  - **poste** : Poste du référent
  - **entreprise** : Entreprise du référent
  - **email** : Email du référent
  - **telephone** : Téléphone du référent
- **situation** : Situation professionnelle actuelle (en poste, demandeur d'emploi, étudiant, etc.)
- **domaine** : Domaine professionnel
- **age** : Âge du candidat
- **sexe** : Sexe du candidat
- **centres_d_interet** : Centres d'intérêt du candidat
- **nationalite** : Nationalité du candidat
- **handicap** : Type de handicap, si applicable
- **pretention_salariale** : Prétention salariale exprimée en k€

## Démarche

### 1. Initialisation

- **Bibliothèque utilisée** : Faker, pour générer des données réalistes (prénoms, noms, adresses, entreprises, etc.).
- **Importation des bibliothèques** : Importation des bibliothèques nécessaires comme `faker`, `random`, `datetime` et `json`.

### 2. Définition des Données de Base

- **Domaines** : Une liste de domaines professionnels variés (ex : Informatique, Marketing, etc.).
- **Handicaps** : Une liste de types de handicaps avec une distribution réaliste.
- **Prénoms et Noms** : Des dictionnaires contenant des prénoms et noms spécifiques par genre et nationalité.
- **Nationalités** : Des listes de nationalités par continent (Afrique, Asie, Europe, Amériques).
- **Écoles** : Une liste d'écoles réelles classées par niveau d'études.
- **Langues** : Un ensemble de combinaisons de langues parlées avec différents niveaux de maîtrise.
- **Centres d'intérêt** : Une liste de centres d'intérêt communs.
- **Descriptions de postes** : Un dictionnaire de descriptions de postes réalistes par domaine.
- **Compétences** : Des listes de compétences humaines et techniques classées par domaine.
- **Entreprises** : Une liste de noms d'entreprises classées par domaine.
- **Tâches** : Un dictionnaire de tâches courantes par domaine.

### 3. Génération des CVs

- **Sélection des Données** : Choix aléatoire de données telles que nationalité, genre, prénoms, noms, etc.
- **Génération des Expériences Professionnelles** : En fonction de l'âge de la personne, un certain nombre d'expériences sont générées avec des dates aléatoires et des tâches associées.
- **Génération du Parcours Éducatif** : Génération des diplômes dans un ordre chronologique cohérent avec des années d'obtention valides.
- **Sélection des Langues Parlées** : Choix des langues parlées avec des niveaux de maîtrise réalistes.
- **Sélection des Compétences** : Génération aléatoire de compétences humaines et techniques en fonction du domaine d'expertise.
- **Génération des Centres d'Intérêt et Recommandations** : Ajout de centres d'intérêt et de recommandations professionnelles.
- **Calcul de la Prétention Salariale** : Calcul basé sur le niveau d'éducation et les années d'expérience.

### 4. Sauvegarde des Données

- **Format de Sauvegarde** : Les 12 500 CVs générés sont sauvegardés dans un fichier JSON avec une indentation pour une meilleure lisibilité.

## Contributions

Les contributions sont les bienvenues ! Pour proposer une nouvelle fonctionnalité, corriger un bug ou améliorer la documentation :

1. Forkez le projet
2. Créez une branche pour votre fonctionnalité (`git checkout -b feature/AmazingFeature`)
3. Commitez vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Poussez votre branche (`git push origin feature/AmazingFeature`)
5. Ouvrez une Pull Request

## Licence

Distribué sous la licence MIT. Voir `LICENSE` pour plus d'informations.

---

Fait avec ❤️ par [Patrick NII](https://github.com/Patrick-NII)