import pandas as pd
from faker import Faker
import random
import json
from datetime import datetime

# Initialiser Faker
fake = Faker('fr_FR')

# Définir les colonnes du DataFrame
colonnes = [
    'ID', 'nom', 'prenom', 'adresse', 'email', 'numero_de_telephone', 'intitule',
    'diplome', 'experiences', 'educations', 'langues', 'competences', 'competences_humaines', 'recommendations',
    'situation', 'domaine', 'age', 'sexe', 'centres_d_interet', 'nationalite', 'handicap', 'pretention_salariale'
]

# Domaines étendus
domaines = [
    'Informatique', 'Santé', 'Finance', 'Éducation', 'Ingénierie', 'Marketing', 'Ventes',
    'Droit', 'Manufacture', 'Commerce', 'Hôtellerie', 'Transport',
    'Énergie', 'Immobilier', 'Télécommunications', 'Média', 'Divertissement', 'Sports',
    'Science', 'Fonction publique', 'ONG', 'Consulting', 'Art',
    'Design', 'Agriculture', 'Industrie alimentaire', 'Aérospatial', 'Défense', 'Manutention',
    'Logistique', 'Ressources humaines', 'Environnement', 'Tourisme', 'Sécurité', 'Automobile',
    'Mode', 'Beauté', 'Restauration', 'Événementiel', 'BTP', 'Assurance', 'Banque',
    'Assistance', 'Social', 'Culture', 'Recherche', 'Enseignement'
]

# Types de handicaps
handicaps = [
    'aucun', 'mental', 'auditif', 'visuel',
    'moteur', 'psychique', 'mutilé',
    'Autisme et Troubles Envahissants du Développement',
    'Plurihandicap', 'Maladie invalidante', 'Polyhandicap',
    'Traumatisme crânien', 'Maladie neurologique', 'Les troubles dys'
]

# Poids pour chaque type de handicap
weights_handicaps = [86] + [1] * (len(handicaps) - 1)

# Prénoms et noms spécifiques par genre et pays
prenoms_pays = {
    'Sénégal': {
        'homme': ["Mamadou", "Ibrahima", "Moussa", "Ousmane", "Abdou"],
        'femme': ["Awa", "Fatou", "Aminata", "Ndeye", "Khady"]
    },
    'Maroc': {
        'homme': ["Omar", "Mohamed", "Hassan", "Ali"],
        'femme': ["Fatima", "Nour", "Yasmine", "Amina"]
    },
    'Chine': {
        'homme': ["Linh", "Minh", "Tuan", "Dung"],
        'femme': ["Yen", "Thanh", "Huong", "Hoa"]
    },
    'Hongrie': {
        'homme': ["Boris", "Ivan", "Viktor", "Maksim"],
        'femme': ["Mila", "Daria", "Anya", "Nina"]
    },
    'France': {
        'homme': ["Jean", "Pierre", "Julien", "Antoine"],
        'femme': ["Marie", "Lucie", "Camille", "Manon"]
    },
    'Algérie': {
        'homme': ["Karim", "Mehdi", "Youssef", "Sofiane"],
        'femme': ["Zineb", "Sabrina", "Nadia", "Nora"]
    },
    'Tunisie': {
        'homme': ["Ali", "Fares", "Mehdi", "Amine"],
        'femme': ["Leila", "Rania", "Hana", "Sarra"]
    },
    'Côte d\'Ivoire': {
        'homme': ["Adama", "Kouadio", "Bakary", "Mamadou"],
        'femme': ["Aïcha", "Fatoumata", "Kadiatou", "Aminata"]
    },
    'Nigeria': {
        'homme': ["Olufemi", "Chinedu", "Obinna", "Chukwu"],
        'femme': ["Ngozi", "Yemi", "Chinwe", "Chinonye"]
    },
    'Afrique du Sud': {
        'homme': ["Thabo", "Mandla", "Sizwe", "Sipho"],
        'femme': ["Nandi", "Thandeka", "Ntombi", "Nomvula"]
    }
}

noms_pays = {
    'Sénégal': ["Diop", "Traoré", "Sow", "Ndiaye", "Diallo"],
    'Maroc': ["Ben Ali", "Bouzid", "Haddad", "Jaziri", "Bensaid"],
    'Chine': ["Nguyen", "Wang", "Chen", "Tran", "Li"],
    'Hongrie': ["Kovacs", "Nagy", "Horvat", "Novak", "Popov"],
    'France': ["Dupont", "Martin", "Bernard", "Dubois", "Moreau"],
    'Algérie': ["Belaid", "Bouhadjar", "Haddadi", "Karoui", "Saadi"],
    'Tunisie': ["Trabelsi", "Sfar", "Khémiri", "Jebali", "Saïdi"],
    'Côte d\'Ivoire': ["Kouassi", "Koffi", "Traoré", "Koné", "Ouattara"],
    'Nigeria': ["Okafor", "Balogun", "Chukwu", "Eze", "Adeyemi"],
    'Afrique du Sud': ["Dlamini", "Nkosi", "Zulu", "Ngcobo", "Khumalo"]
}

# Nationalités par continent
nationalites_afrique = ['Sénégal', 'Algérie', 'Tunisie', 'Côte d\'Ivoire', 'Nigeria',
                        'Afrique du Sud', 'Congo', 'Cameroun', 'Togo', 'Ghana',
                        'Bénin', 'Angola', 'Mali', 'Mauritanie', 'Maroc']
nationalites_asie = ['Chine', 'Vietnam', 'Cambodge', 'Inde', 'Pakistan', 'Japon', 'Corée du Sud']
nationalites_europe = ['Hongrie', 'France', 'Allemagne', 'Italie', 'Espagne',
                       'Portugal', 'Royaume-Uni', 'Pays-Bas', 'Belgique',
                       'Suisse', 'Suède', 'Norvège', 'Danemark', 'Finlande',
                       'Grèce', 'Pologne', 'Ukraine', 'Russie']
nationalites_ameriques = ['Brésil', 'Argentine', 'Mexique', 'Colombie',
                          'Chili', 'Pérou', 'Venezuela',
                          'Canada', 'États-Unis', 'Antilles Françaises']

# Écoles réelles
ecoles = {
    'Bep': ['Lycée professionnel Jean Moulin', 'Lycée professionnel Louis Armand',
            'Lycée professionnel Gustave Eiffel', 'Lycée professionnel Jules Ferry',
            'Lycée professionnel Henri IV', 'Lycée professionnel Van Gogh',
            'Lycée professionnel Jean Jaurès', 'Lycée professionnel Victor Hugo'],
    'Baccalauréat': ['Lycée Van Gogh', 'Lycée Jean Jaurès', 'Lycée Henri IV',
                     'Lycée Victor Hugo', 'Lycée Louis Armand', 'Lycée Jules Ferry',
                     'Lycée Gustave Eiffel', 'Lycée Jean Moulin'],
    'BTS': ['Lycée Louis Armand', 'Lycée Jules Ferry', 'Lycée Gustave Eiffel',
            'Lycée Jean Jaurès', 'Lycée Victor Hugo', 'Lycée Van Gogh',
            'Lycée Jean Moulin', 'Lycée Henri IV'],
    'Licence': ['Université Paris 1 Panthéon-Sorbonne', 'Université de Bordeaux', 'Université de Lille',
                'Université de Lyon', 'Université de Marseille', 'Université de Montpellier',
                'Université de Nantes', 'Université de Strasbourg'],
    'Master': ['Université Paris-Dauphine', 'Université de Strasbourg', 'Université de Grenoble',
               'Université de Toulouse', 'Université de Rennes', 'Université de Nice',
               'Université de Reims', 'Université de Tours', 'Université de Poitiers',
               'Université de Limoges', 'Université de Pau', 'Université de Perpignan'],
    'Ingénieur': ['École Polytechnique', 'École Centrale Paris', 'École des Ponts ParisTech',
                  'École des Mines ParisTech', 'École Normale Supérieure', 'École Supérieure de Physique et de Chimie Industrielles',
                  'École Nationale des Ponts et Chaussées', 'École Nationale Supérieure des Mines de Saint-Étienne',
                  'CentraleSupélec', 'Conservation des Arts et Métiers', 'École Nationale Supérieure de Techniques Avancées'],
    'Doctorat': ['Université Paris-Saclay', 'Université de Lyon', 'Université de Marseille',
                 'Université de Montpellier', 'Université de Nantes', 'Université de Strasbourg',
                 'Université de Bordeaux', 'Université de Lille', 'Université de Toulouse']
}

# Langues
langues = [
    {'français': 'C2', 'anglais': 'B2', 'espagnol': 'B1'},
    {'français': 'C2', 'anglais': 'A2', 'allemand': 'B1'},
    {'français': 'C1', 'anglais': 'B2', 'italien': 'A2'},
    {'français': 'C2', 'anglais': 'C1', 'chinois': 'B2'},
    {'français': 'C2', 'arabe': 'C1', 'anglais': 'B1'},
    {'français': 'C2', 'lingala': 'B1', 'swahili': 'A2'},
    {'français': 'C2', 'wolof': 'B2', 'peul': 'B1'},
    {'français': 'C2', 'portugais': 'B2', 'créole': 'B1'},
    {'français': 'C2', 'russe': 'B2', 'polonais': 'B1'},
    {'français': 'C2', 'japonais': 'B1', 'coréen': 'A2'},
    {'français': 'C2', 'turc': 'B1', 'persan': 'A2'},
    {'français': 'C2', 'grec': 'B1', 'hébreu': 'A2'},
    {'français': 'C2', 'roumain': 'B1', 'hongrois': 'A2'},
    {'français': 'C2', 'néerlandais': 'B2', 'norvégien': 'A2'},
    {'français': 'C2', 'danois': 'B1', 'finnois': 'A2'},
    {'français': 'C2', 'slovaque': 'B1', 'tchèque': 'A2'},
    {'français': 'C2', 'serbe': 'B1', 'croate': 'A2'}
]

# Centres d'intérêt
centres_d_interet = [
    'lecture', 'sport', 'voyages', 'musique', 'cinéma',
    'cuisine', 'photographie', 'jardinage', 'randonnée', 'peinture',
    'écriture', 'danse', 'natation', 'cyclisme', 'course à pied',
    'yoga', 'méditation', 'programmation', 'jeux vidéo', 'bricolage',
    'sculpture', 'théâtre', 'chant', 'pêche', 'astronomie',
    'mode', 'dessin', 'volleyball', 'basketball', 'football',
    'rugby', 'tennis', 'badminton', 'escalade', 'ski',
    'snowboard', 'surf', 'kayak', 'canoë', 'parapente',
    'parachutisme', 'planche à voile', 'plongée', 'équitation', 'patinage',
    'escrime', 'karaté', 'judo', 'taekwondo', 'aikido',
    'boxe', 'haltérophilie', 'fitness', 'musculation', 'bodybuilding',
    'crossfit', 'pilates', 'spinning', 'danse classique', 'danse contemporaine',
    'danse hip-hop', 'danse salsa', 'danse tango', 'danse flamenco', 'danse de salon',
    'danse orientale', 'danse africaine', 'danse indienne', 'danse jazz', 'danse moderne',
    'électronique', 'mécanique', 'robotique', 'domotique', 'maquettisme',
    'modélisme', 'radiocommandé', 'cinéma amateur', 'réalisation de films', 'montage vidéo'
]

# Compétences humaines
competences_humaines_list = [
    'Communication', 'Travail en équipe', 'Gestion du temps', 'Résolution de problèmes', 'Leadership',
    'Adaptabilité', 'Créativité', 'Esprit critique', 'Empathie', 'Motivation', 'Gestion du stress',
    'Prise de décision', 'Négociation', 'Persuasion', 'Gestion de conflits', 'Organisation',
    'Autonomie', 'Sens des responsabilités', 'Fiabilité', 'Dynamisme', 'Polyvalence', 'Sens du service'
]

# Compétences techniques par domaine
competences_techniques = {
    'Informatique': ['Python', 'SQL', 'Java', 'C++', 'HTML', 'CSS', 'JavaScript', 'Linux', 'Git', 'Django',
                     'Flask', 'React', 'Angular', 'Vue.js', 'Node.js', 'Express.js', 'MongoDB',
                     'PostgreSQL', 'MySQL', 'SQLite', 'NoSQL', 'API', 'REST', 'GraphQL',
                     'Docker', 'Kubernetes', 'CI/CD', 'AWS', 'Azure', 'GCP', 'Heroku', 'Firebase',
                     'Jenkins', 'Ansible', 'Terraform', 'Kafka', 'RabbitMQ', 'Redis', 'Elasticsearch',
                     'Kibana', 'Logstash', 'Prometheus', 'Grafana', 'Nginx', 'Apache', 'Jira',
                     'Confluence', 'Slack', 'Trello', 'Asana', 'GitLab', 'GitHub', 'Bitbucket', 'Jenkins',
                     'Travis CI', 'CircleCI', 'Codecov', 'SonarQube', 'Jest', 'Pytest', 'Mocha', 'Chai',
                     'Cypress', 'Selenium', 'JMeter', 'Postman', 'Swagger', 'OpenAPI', 'OAuth', 'JWT', 'SAML',
                     'PHP', 'Base de données', 'Sécurité informatique', 'Sécurité Réseaux', 'Sécurité Cloud',
                     'Développement web', 'Développement mobile', 'Développement logiciel',
                     'Développement d\'applications', 'Développement d\'API', 'Développement back-end',
                     'Développement front-end', 'Développement full-stack', 'Développement cloud',
                     'Développement DevOps', 'Développement Big Data', 'Développement IA', 'Développement IoT',
                     'Développement blockchain', 'Développement AR/VR', 'Développement jeux vidéo',
                     'Développement systèmes embarqués', 'Développement sécurité', 'Développement qualité',
                     'Développement test', 'Développement automatisation', 'Développement maintenance',
                     'Développement support', 'Développement consulting', 'Développement formation',
                     'Développement gestion de projet', 'Développement recherche',
                     'Développement veille technologique', 'Python', 'Machine Learning', 'Deep Learning',
                     'Data Science', 'Data Engineering', 'Data Analysis', 'Data Mining', 'Data Warehousing',
                     'Data Modeling', 'Data Visualization', 'Business Intelligence', 'ETL', 'ELT', 'OLAP',
                     'OLTP', 'DWH', 'BI', 'Big Data', 'Hadoop', 'Spark', 'Flink', 'Kafka', 'Hive', 'Pig',
                     'Sqoop', 'Flume', 'HBase', 'Cassandra', 'MongoDB', 'Redis', 'MySQL', 'PostgreSQL'],
    'Santé': ['Soins infirmiers', 'Anatomie', 'Pharmacologie', 'Gestion des patients', 'Premiers secours',
              'Soins intensifs', 'Soins palliatifs', 'Soins à domicile', 'Soins pédiatriques', 'Soins gériatriques',
              'Soins obstétriques', 'Soins psychiatriques', 'Soins chirurgicaux', 'Soins médicaux', 'Soins dentaires',
              'Soins ophtalmologiques', 'Soins ORL', 'Soins dermatologiques', 'Soins orthopédiques', 'Soins neurologiques',
              'Soins cardiovasculaires', 'Soins respiratoires', 'Soins oncologiques', 'Soins endocriniens', 'Soins urologiques'],
    'Finance': ['Comptabilité', 'Analyse financière', 'Gestion de trésorerie', 'Audit', 'Prévision financière',
                'Contrôle de gestion', 'Finance d\'entreprise', 'Finance de marché', 'Finance de projet', 'Finance internationale'],
    'Éducation': ['Pédagogie', 'Gestion de classe', 'Planification de cours', 'Évaluation', 'Didactique',
                  'Technologies éducatives', 'Formation continue', 'Orientation scolaire',
                  'Conseil pédagogique', 'Recherche en éducation'],
    'Ingénierie': ['AutoCAD', 'MATLAB', 'Gestion de projet', 'Conception', 'Modélisation 3D',
                   'Calculs de structures', 'Calculs thermiques', 'Calculs électriques', 'Calculs hydrauliques',
                   'Calculs mécaniques', 'Calculs aérodynamiques', 'Calculs acoustiques', 'Calculs optiques',
                   'Calculs électromagnétiques', 'Calculs quantiques', 'Calculs statistiques', 'Calculs probabilistes',
                   'Solidworks', 'Catia', 'NX', 'Creo', 'Inventor', 'Revit', 'RobotStudio', 'TIA Portal',
                   'Fusion 360', 'Creality', 'Ultimaker', 'Prusa', 'Ansys', 'Abaqus', 'Comsol', 'StarCCM+'],
    'Marketing': ['SEO', 'Publicité', 'Analyse de marché', 'Stratégie de marque', 'Réseaux sociaux',
                  'Marketing digital', 'Marketing de contenu', 'Marketing viral', 'Marketing relationnel',
                  'Marketing événementiel', 'Marketing direct', 'Marketing de proximité', 'Marketing de masse'],
    'Ventes': ['Négociation', 'Gestion des comptes', 'Service à la clientèle', 'Prospection', 'CRM',
               'Vente B2B', 'Vente B2C', 'Vente en ligne', 'Vente en magasin', 'Vente par téléphone'],
    'Droit': ['Droit des affaires', 'Droit pénal', 'Rédaction de contrats', 'Conseil juridique', 'Plaidoyer',
              'Droit du travail', 'Droit de la famille', 'Droit des sociétés', 'Droit fiscal', 'Droit immobilier'],
    'Média': ['Montage vidéo', 'Journalisme', 'Photographie', 'Rédaction', 'Gestion des réseaux sociaux'],
    'Manufacture': ['Supervision', 'Maintenance', 'Qualité', 'Production', 'Planification'],
    'Commerce': ['Gestion de stock', 'Relation client', 'Stratégie de vente', 'Merchandising', 'Logistique'],
    'Hôtellerie': ['Accueil', 'Service en salle', 'Service en chambre', 'Service en cuisine', 'Service en bar'],
    'Transport': ['Logistique', 'Gestion de flotte', 'Conduite', 'Maintenance', 'Sécurité'],
    'Énergie': ['Production', 'Distribution', 'Renouvelable', 'Nucléaire', 'Pétrole'],
    'Immobilier': ['Transaction', 'Location', 'Gestion', 'Promotion', 'Construction'],
    'Télécommunications': ['Réseaux', 'Téléphonie', 'Fibre', 'Satellite', 'Mobile'],
    'Divertissement': ['Animation', 'Musique', 'Théâtre', 'Cirque', 'Cinéma'],
    'Sports': ['Entraînement', 'Arbitrage', 'Compétition', 'Organisation', 'Santé'],
    'Science': ['Recherche', 'Expérimentation', 'Analyse', 'Publication', 'Enseignement'],
    'Fonction publique': ['Administration', 'Service', 'Sécurité', 'Justice', 'Éducation', 'Santé',
                          'Agent de Police', 'Pompier', 'Agent de sécurité', 'Agent de surveillance', 'Agent de protection'],
    'Logistique': ['Gestion de stock', 'Transport', 'Distribution', 'Approvisionnement', 'Manutention'],
    'Banque': ['Gestion de compte', 'Crédit', 'Assurance', 'Placements', 'Conseil'],
    'Assurance': ['Assurance vie', 'Assurance auto', 'Assurance habitation', 'Assurance santé', 'Assurance voyage'],
    'Consulting': ['Conseil', 'Audit', 'Stratégie', 'Transformation', 'Formation'],
    'Ressources humaines': ['Recrutement', 'Formation', 'Gestion de carrière', 'Gestion de paie', 'Gestion des conflits'],
    'Communication': ['Relations publiques', 'Communication interne', 'Communication externe', 'Communication digitale', 'Communication événementielle'],
    'Maintenance': ['Maintenance préventive', 'Maintenance curative', 'Maintenance corrective', 'Maintenance prédictive', 'Maintenance conditionnelle'],
    'Sécurité': ['Sécurité des biens', 'Sécurité des personnes', 'Sécurité incendie', 'Sécurité informatique', 'Sécurité des données'],
    'Automobile': ['Conception', 'Production', 'Maintenance', 'Vente', 'Réparation'],
    'Mode': ['Design', 'Stylisme', 'Couture', 'Modélisme', 'Marketing'],
    'Technique': ['Électricité', 'Mécanique', 'Plomberie', 'Menuiserie', 'Soudure'],
    'Production': ['Fabrication', 'Assemblage', 'Conditionnement', 'Contrôle qualité', 'Logistique'],
    'Agriculture': ['Culture', 'Élevage', 'Pêche', 'Sylviculture', 'Agroalimentaire'],
    'Art': ['Peinture', 'Sculpture', 'Photographie', 'Dessin', 'Cinéma'],
    'Design': ['Graphisme', 'Web design', 'Design industriel', 'Design d\'intérieur', 'Design de mode'],
    'Environnement': ['Écologie', 'Développement durable', 'Gestion des déchets', 'Énergies renouvelables', 'Biodiversité'],
    'Tourisme': ['Hôtellerie', 'Restauration', 'Guidage', 'Animation', 'Transport']
}

# Liste de noms d'entreprises
entreprises = [
    'Total', 'Renault', 'Orange', 'Air France', 'Carrefour', 'Société Générale', 'EDF', 'BNP Paribas',
    'Capgemini', 'Thales', 'Michelin', 'LVMH', 'Danone', 'Sanofi', 'L\'Oréal', 'Veolia', 'Bouygues', 'Vinci',
    'Pernod Ricard', 'Engie', 'Dassault', 'AXA', 'Saint-Gobain', 'Schneider Electric', 'Crédit Agricole',
    'SNCF', 'Decathlon', 'Alstom', 'PSA', 'Safran', 'Atos', 'Areva', 'Accor', 'Natixis', 'Groupe La Poste',
    'Caisse des Dépôts', 'RTE', 'Transdev', 'RATP', 'Eiffage', 'Airbus', 'Suez', 'Thalès', 'Dassault Aviation',
    'Naval Group', 'Framatome', 'Technip', 'Bolloré', 'Groupe BPCE', 'Kering', 'Hermès', 'Publicis',
    'JCDecaux', 'Iliad', 'SFR', 'Bouygues Telecom', 'Altice', 'M6', 'TF1', 'France Télévisions', 'Canal+',
    'RMC', 'Europe 1', 'RTL', 'Le Monde', 'Le Figaro', 'Les Echos', 'Libération', 'L\'Express', 'Le Point',
    'Marianne', 'Valeurs Actuelles', 'L\'Humanité', 'Le Parisien', '20 Minutes', 'Metro', 'Ouest-France',
    'Sud Ouest', 'La Dépêche', 'La Voix du Nord', 'Nice-Matin', 'L\'Alsace', 'Le Progrès', 'Le Télégramme',
    'La Croix', 'L\'Equipe', 'Le Journal du Dimanche', 'Les Inrockuptibles', 'Télérama', 'Paris Match'
]

# Descriptions de postes réalistes
descriptions_postes = {
    'Informatique': [
        "Développement et maintenance des applications web",
        "Analyse des besoins des utilisateurs et conception des solutions logicielles",
        "Supervision des projets de développement informatique",
        "Assistance technique et résolution des problèmes informatiques",
        "Formation des utilisateurs sur les nouvelles technologies"
    ],
    'Santé': [
        "Prise en charge des patients et administration des soins",
        "Préparation et administration des médicaments",
        "Gestion des dossiers médicaux et suivi des patients",
        "Collaboration avec les médecins pour établir les diagnostics",
        "Participation aux campagnes de prévention et d'éducation à la santé"
    ],
    'Finance': [
        "Analyse des états financiers et élaboration des rapports",
        "Gestion de la trésorerie et des flux de trésorerie",
        "Réalisation des audits internes et externes",
        "Élaboration des prévisions financières et des budgets",
        "Conseil en matière de gestion financière et d'investissement"
    ],
    'Éducation': [
        "Préparation et animation des cours",
        "Suivi pédagogique et évaluation des étudiants",
        "Développement de programmes éducatifs",
        "Organisation et participation aux conseils de classe",
        "Encadrement des activités périscolaires et des projets éducatifs"
    ],
    'Ingénierie': [
        "Conception et développement des systèmes mécaniques",
        "Réalisation des études techniques et des analyses de faisabilité",
        "Supervision des projets de construction et de maintenance",
        "Élaboration des plans et des schémas techniques",
        "Collaboration avec les équipes de production pour améliorer les procédés"
    ],
    'Marketing': [
        "Développement et mise en œuvre des stratégies marketing",
        "Analyse du marché et identification des opportunités",
        "Gestion des campagnes publicitaires et promotionnelles",
        "Création de contenus pour les réseaux sociaux et le site web",
        "Suivi des performances des actions marketing et ajustements"
    ],
    'Ventes': [
        "Prospection de nouveaux clients et développement du portefeuille",
        "Négociation des contrats et des conditions commerciales",
        "Suivi des commandes et des livraisons",
        "Gestion des réclamations et des litiges",
        "Reporting des activités commerciales et des résultats"
    ],
    'Droit': [
        "Conseil juridique aux clients et aux partenaires",
        "Rédaction des contrats et des actes juridiques",
        "Représentation des clients devant les tribunaux",
        "Veille juridique et analyse de la réglementation",
        "Médiation et résolution des conflits"
    ],
    'Média': [
        "Réalisation de reportages et d'interviews",
        "Montage et post-production des contenus audiovisuels",
        "Rédaction d'articles et de chroniques",
        "Animation des réseaux sociaux et des plateformes web",
        "Organisation d'événements et de conférences de presse"
    ],
    'Manufacture': [
        "Planification et organisation de la production",
        "Gestion des stocks et des approvisionnements",
        "Contrôle qualité des produits et des processus",
        "Maintenance préventive et curative des équipements",
        "Amélioration continue des méthodes de travail"
    ],
    'Commerce': [
        "Gestion des achats et des approvisionnements",
        "Suivi des ventes et des indicateurs de performance",
        "Animation commerciale et merchandising",
        "Relation client et service après-vente",
        "Analyse des données de marché et des tendances"
    ],
    'Hôtellerie': [
        "Accueil et prise en charge des clients",
        "Service en salle et en chambre",
        "Gestion des réservations et des plannings",
        "Coordination des équipes et des prestataires",
        "Suivi de la satisfaction client et traitement des réclamations"
    ],
    'Transport': [
        "Organisation des tournées et des livraisons",
        "Gestion des stocks et des approvisionnements",
        "Maintenance préventive et curative des véhicules",
        "Sécurité des marchandises et des passagers",
        "Optimisation des coûts et des délais de transport"
    ],
    'Énergie': [
        "Production et distribution d'énergie électrique",
        "Gestion des réseaux de transport et de distribution",
        "Développement des énergies renouvelables",
        "Maintenance des installations et des équipements",
        "Sécurité des installations et des intervenants"
    ],
    'Immobilier': [
        "Transaction et négociation immobilière",
        "Gestion locative et syndic de copropriété",
        "Promotion immobilière et construction",
        "Expertise et évaluation des biens",
        "Conseil en investissement et en financement"
    ],
    'Télécommunications': [
        "Installation et maintenance des réseaux",
        "Déploiement des infrastructures de télécommunication",
        "Gestion des services et des abonnements",
        "Développement des offres et des produits",
        "Veille technologique et réglementaire"
    ],
    'Divertissement': [
        "Animation et spectacle pour tous les publics",
        "Production et réalisation d'émissions et de films",
        "Organisation d'événements culturels et artistiques",
        "Promotion et diffusion des œuvres et des artistes",
        "Gestion des droits d'auteur et des contrats"
    ],
    'Sports': [
        "Entraînement et préparation physique des sportifs",
        "Arbitrage et organisation des compétitions",
        "Gestion des infrastructures et des équipements",
        "Suivi médical et rééducation des blessures",
        "Promotion et développement des disciplines sportives"
    ],
    'Science': [
        "Recherche fondamentale et appliquée",
        "Expérimentation et analyse des données",
        "Publication des résultats et des découvertes",
        "Enseignement et transmission des connaissances",
        "Collaboration avec les équipes internationales"
    ],
    'Fonction publique': [
        "Administration des services publics",
        "Sécurité et protection des citoyens",
        "Justice et respect de la loi",
        "Éducation et formation des jeunes",
        "Santé et bien-être de la population"
    ],
    'Logistique': [
        "Gestion des stocks et des approvisionnements",
        "Organisation des transports et des livraisons",
        "Optimisation des flux et des coûts logistiques",
        "Suivi des opérations et des indicateurs de performance",
        "Sécurité des biens et des personnes"
    ],
    'Banque': [
        "Accueil et conseil aux clients",
        "Gestion des comptes et des transactions",
        "Analyse des risques et des crédits",
        "Placement et gestion de patrimoine",
        "Conformité réglementaire et lutte contre la fraude"
    ],
    'Assurance': [
        "Évaluation des risques et des sinistres",
        "Souscription des contrats et des polices",
        "Gestion des dossiers et des indemnisations",
        "Prévention et sécurité des biens et des personnes",
        "Développement des produits et des services"
    ],
    'Consulting': [
        "Conseil en stratégie et en organisation",
        "Audit et diagnostic des performances",
        "Accompagnement du changement et des transformations",
        "Formation et développement des compétences",
        "Veille concurrentielle et technologique"
    ],
    'Ressources humaines': [
        "Recrutement et intégration des collaborateurs",
        "Gestion des carrières et des compétences",
        "Formation et développement professionnel",
        "Gestion des conflits et des relations sociales",
        "Santé et qualité de vie au travail"
    ],
    'Communication': [
        "Relations presse et relations publiques",
        "Communication interne et externe",
        "Événementiel et relations institutionnelles",
        "Community management et réseaux sociaux",
        "Création de contenus et de supports de communication"
    ],
    'Environnement': [
        "Protection de la nature et des espèces",
        "Gestion des déchets et des ressources",
        "Étude et prévention des pollutions",
        "Aménagement et développement durable",
        "Sensibilisation et éducation à l'environnement"
    ],
    'Agriculture': [
        "Production et transformation des cultures",
        "Élevage et transformation des animaux",
        "Gestion des exploitations et des terres",
        "Commercialisation et distribution des produits",
        "Innovation et développement des pratiques agricoles"
    ],
    'Art': [
        "Création et production artistique",
        "Exposition et diffusion des œuvres",
        "Gestion de projets culturels et artistiques",
        "Médiation et animation culturelle",
        "Formation et transmission des savoir-faire"
    ],
    'Mode': [
        "Création et design de vêtements et d'accessoires",
        "Production et fabrication des collections",
        "Commercialisation et distribution des produits",
        "Communication et promotion des marques",
        "Développement durable et éthique de la mode"
    ],
    'Tourisme': [
        "Accueil et information des touristes",
        "Organisation et promotion des séjours",
        "Gestion des réservations et des prestations",
        "Animation et encadrement des activités",
        "Développement et valorisation des territoires"
    ],
    'Restauration': [
        "Préparation et service des plats et des boissons",
        "Gestion des approvisionnements et des stocks",
        "Hygiène et sécurité alimentaire",
        "Accueil et satisfaction des clients",
        "Création et innovation culinaires"
    ],
    'Événementiel': [
        "Organisation et coordination des événements",
        "Logistique et gestion des prestataires",
        "Communication et promotion des manifestations",
        "Accueil et animation des participants",
        "Évaluation et bilan des opérations"
    ],
    'Sécurité': [
        "Surveillance et protection des biens et des personnes",
        "Prévention des risques et des intrusions",
        "Intervention et secours en cas d'incident",
        "Contrôle et vérification des accès",
        "Formation et sensibilisation à la sécurité"
    ],
    'Technologies': [
        "Développement et maintenance des applications web",
        "Analyse des besoins des utilisateurs et conception des solutions logicielles",
        "Supervision des projets de développement informatique",
        "Assistance technique et résolution des problèmes informatiques",
        "Formation des utilisateurs sur les nouvelles technologies"
    ],
    'Techniques': [
        "Conception et développement des systèmes mécaniques",
        "Réalisation des études techniques et des analyses de faisabilité",
        "Supervision des projets de construction et de maintenance",
        "Élaboration des plans et des schémas techniques",
        "Collaboration avec les équipes de production pour améliorer les procédés"
    ],
    "Maintenance": [
        "Planification et organisation de la production",
        "Gestion des stocks et des approvisionnements",
        "Contrôle qualité des produits et des processus",
        "Maintenance préventive et curative des équipements",
        "Amélioration continue des méthodes de travail"
    ],
    'Culture': [
        "Organisation d'événements culturels",
        "Gestion des collections et des expositions",
        "Développement de projets artistiques",
        "Médiation culturelle et éducation artistique",
        "Promotion du patrimoine culturel"
    ],
    'Design': [
        "Conception et réalisation de projets graphiques",
        "Création de supports de communication visuelle",
        "Développement de l'identité visuelle des marques",
        "Mise en page et publication de contenus",
        "Veille créative et technologique"
    ],
    "ONG": [
        "Sensibilisation et mobilisation des citoyens",
        "Défense des droits de l'homme et de l'environnement",
        "Actions humanitaires et solidaires",
        "Plaidoyer et lobbying auprès des institutions",
        "Gestion de projets de développement et de coopération"
    ],
    "Beauté": [
        "Conseil et diagnostic en esthétique",
        "Soins du visage et du corps",
        "Maquillage et coiffure",
        "Vente de produits cosmétiques",
        "Formation et animation d'ateliers beauté"
    ],
    "Industrie alimentaire": [
        "Production et transformation des denrées",
        "Contrôle qualité et sécurité alimentaire",
        "Gestion des approvisionnements et des stocks",
        "Commercialisation et distribution des produits",
        "Innovation et développement de nouveaux produits"
    ],
    "Social": [
        "Accompagnement et soutien des personnes en difficulté",
        "Médiation et résolution des conflits",
        "Animation et encadrement des groupes",
        "Écoute et conseil psychologique",
        "Coordination des actions sociales et solidaires"
    ],
    "Aérospatial": [
        "Conception et fabrication d'aéronefs",
        "Maintenance et réparation des appareils",
        "Contrôle qualité et sécurité des vols",
        "Formation et certification des pilotes",
        "Recherche et développement de nouvelles technologies"
    ],
    "Enseignement": [
        "Préparation et animation des cours",
        "Suivi pédagogique et évaluation des élèves",
        "Conception de supports pédagogiques",
        "Orientation et conseil aux étudiants",
        "Participation aux projets éducatifs et aux examens"
    ],
    "Manutention": [
        "Chargement et déchargement des marchandises",
        "Tri et rangement des produits",
        "Préparation des commandes et des expéditions",
        "Utilisation des engins de manutention",
        "Respect des consignes de sécurité et des délais"
    ],
    "BTP": [
        "Construction et rénovation de bâtiments",
        "Gros œuvre et second œuvre",
        "Travaux publics et aménagement urbain",
        "Coordination des chantiers et des équipes",
        "Respect des normes et des réglementations en vigueur"
    ],
    "Assistance": [
        "Accueil et orientation des usagers",
        "Gestion des appels et des rendez-vous",
        "Traitement des dossiers administratifs",
        "Rédaction de courriers et de comptes-rendus",
        "Collaboration avec les services internes et externes"
    ],
    "Défense": [
        "Protection du territoire et des citoyens",
        "Surveillance et renseignement militaire",
        "Intervention et secours en cas de crise",
        "Formation et entraînement des soldats",
        "Coopération internationale et missions de paix"
    ],
    "Automobile": [
        "Conception et fabrication des véhicules",
        "Maintenance et réparation des moteurs",
        "Contrôle qualité et sécurité routière",
        "Vente et location de véhicules",
        "Développement de nouvelles technologies et de motorisations"
    ],
    "Recherche": [
        "Expérimentation et analyse des données",
        "Publication des résultats et des découvertes",
        "Enseignement et transmission des connaissances",
        "Collaboration avec les équipes internationales",
        "Innovation et développement de nouvelles technologies"
    ],
}

# Générer les données factices
def generate_fake_data(num_records):
    data = []
    for i in range(num_records):
        nationalite = random.choice(nationalites_afrique + nationalites_asie + nationalites_europe + nationalites_ameriques)
        sexe = random.choices(['homme', 'femme'], weights=[62, 38], k=1)[0] if random.random() > 0.08 else random.choice(['homme', 'femme'])

        prenoms = prenoms_pays.get(nationalite, {'homme': ["Jean"], 'femme': ["Marie"]})
        noms = noms_pays.get(nationalite, ["Dupont", "Martin", "Bernard", "Dubois", "Moreau"])

        prenom = random.choice(prenoms[sexe])
        nom = random.choice(noms)

        email = f"{prenom.lower()}.{nom.lower()}@{random.choices(['google.com', 'msn.com', 'aol.com', 'orange.fr', 'free.fr', 'yahoo.com', 'outlook.com', 'hotmail.com'], weights=[50, 10, 10, 10, 5, 20, 10, 10], k=1)[0]}"

        age = random.randint(18, 65)
        annee_naissance = datetime.now().year - age

        domaine = random.choice(domaines)
        intitule = random.choice(descriptions_postes[domaine])

        educations = []
        niveaux_diplome = ['Sans diplome', 'Bep', 'Baccalauréat', 'BTS', 'Licence', 'Ingénieur', 'Doctorat']
        poids_diplomes = [20, 10, 30, 12, 14, 23, 1]
        niveau_diplome = random.choices(niveaux_diplome, weights=poids_diplomes, k=1)[0]
        annee_diplome = annee_naissance + 18

        if niveau_diplome != 'Sans diplome':
            educations.append({
                'diplome': niveau_diplome,
                'ecole': random.choice(ecoles[niveau_diplome]),
                'annee': annee_diplome
            })

        experiences = []
        start_year = annee_diplome + 1 if educations else annee_naissance + 18

        for _ in range(random.randint(1, 5)):
            end_year = start_year + random.randint(1, 5)
            if end_year > datetime.now().year:
                end_year = datetime.now().year
            experiences.append({
                'intitulé_poste': intitule,
                'entreprise': random.choice(entreprises),
                'date_debut': f"{start_year}-01-01",
                'date_fin': f"{end_year}-12-31",
                'description': random.choice(descriptions_postes[domaine]) + f" {intitule} chez {random.choice(entreprises)}, j'ai supervisé {fake.sentence(nb_words=6)}."
            })
            start_year = end_year + 1
            if start_year > datetime.now().year:
                break

        recommendations = [
            {
                'nom': fake.name(),
                'poste': fake.job(),
                'entreprise': random.choice(entreprises),
                'email': fake.email(domain=random.choices(
                    ['google.com', 'msn.com', 'aol.com', 'orange.fr', 'free.fr', 'yahoo.com', 'outlook.com', 'hotmail.com'],
                    weights=[50, 10, 10, 10, 5, 20, 10, 10],
                    k=1)[0]),
                'telephone': fake.phone_number()
            }
            for _ in range(random.randint(0, 3))  # Maximum 3 recommendations
        ]

        Status = [
            'En poste', 'Demandeur d\'emploi', 'étudiant', 'freelance', 'Alternant', 'stagiaire'
        ]

        def competences_tech(domaine):
            if domaine in competences_techniques:
                return random.choices(competences_techniques[domaine], k=5)
            return []

        competences = competences_tech(domaine)

        competences_humaines = random.choices(competences_humaines_list, k=5)

        # Calcul de la prétention salariale
        salaire_base = 21  # Base de 21k€
        if niveau_diplome == 'Baccalauréat':
            salaire_base += 10
        elif niveau_diplome == 'BTS':
            salaire_base += 15
        elif niveau_diplome in ['Licence', 'Master']:
            salaire_base += 20
        elif niveau_diplome == 'Ingénieur':
            salaire_base += 40
        elif niveau_diplome == 'Doctorat':
            salaire_base += 50
        pretention_salariale = salaire_base + (len(experiences) * 2)  # +2k€ par année d'expérience

        row = {
            'ID': i + 1,
            'nom': nom,
            'prenom': prenom,
            'adresse': fake.address(),
            'email': email,
            'numero_de_telephone': fake.phone_number(),
            'intitule': intitule,
            'diplome': ', '.join([ed['diplome'] for ed in educations]),
            'experiences': experiences,
            'educations': educations,
            'langues': random.choice(langues),
            'competences_techniques': ', '.join(competences),
            'competences_humaines': ', '.join(competences_humaines),
            'recommendations': recommendations,
            'situation': random.choice(Status),
            'domaine': domaine,
            'age': age,
            'sexe': sexe,
            'centres_d_interet': ', '.join(random.sample(centres_d_interet, 4)),
            'nationalite': nationalite,
            'handicap': random.choices(handicaps, weights=weights_handicaps, k=1)[0],
            'pretention_salariale': f"{pretention_salariale}k€"
        }
        data.append(row)
    return data

# Convertir les données en DataFrame
num_records = 12000
data = generate_fake_data(num_records)
df = pd.DataFrame(data, columns=colonnes)

# Éclater les colonnes JSON en colonnes distinctes
def explode_column(df, column, prefix):
    temp_df = df.drop(column, axis=1).join(
        pd.json_normalize(df[column], sep='_').add_prefix(prefix)
    )
    return temp_df

df = explode_column(df, 'experiences', 'experience_')
df = explode_column(df, 'educations', 'education_')
df = explode_column(df, 'langues', 'langue_')
df = explode_column(df, 'recommendations', 'recommendation_')

# Exporter le DataFrame en fichier JSON
json_filename = 'cv_data.json'
df.to_json(json_filename, orient='records', force_ascii=False, indent=4)

print(f"DataFrame generated and saved to {json_filename}")

# Exporter en fichier CSV
df.to_csv('cv_data.csv', index=False)
