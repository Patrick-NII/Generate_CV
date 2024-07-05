# Génération de Base de Données de CV

Ce projet génère une base de données fictive de CV en utilisant Python, Faker et Pandas. Il crée un fichier JSON et CSV contenant des informations détaillées sur des candidats fictifs dans divers domaines professionnels. Ce projet est utile pour les tests, la démonstration de logiciels ou les analyses de données.

## Table des Matières

- [Installation](#installation)
- [Usage](#usage)
- [Structure des Données](#structure-des-données)
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
- **nom** : Nom du candidat
- **prenom** : Prénom du candidat
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
