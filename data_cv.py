import pandas as pd
from faker import Faker
import random
from datetime import datetime


fake = Faker('fr_FR')

# Définir les colonnes du DataFrame
colonnes = [
    'ID', 'nom', 'prenom', 'adresse', 'email', 'numero_de_telephone', 'intitule', 
    'diplome', 'experiences', 'educations', 'langues', 'competences_techniques', 'competences_humaines', 
    'recommendations', 'situation', 'domaine', 'age', 'sexe', 'centres_d_interet', 'nationalite', 
    'handicap', 'pretention_salariale'
]

# Domaines étendus
domaines = [
    'Informatique', 'Santé', 'Finance', 'Éducation', 'Ingénierie', 'Marketing', 'Ventes', 
    'Droit', 'Manufacture', 'Commerce', 'Hôtellerie', 'Transport', 'Énergie', 'Immobilier', 
    'Télécommunications', 'Média', 'Divertissement', 'Sports', 'Science', 'Fonction publique', 
    'ONG', 'Consulting', 'Art', 'Design', 'Agriculture', 'Industrie alimentaire', 'Aérospatial', 
    'Défense', 'Manutention', 'Logistique', 'Ressources humaines', 'Environnement', 'Tourisme', 
    'Sécurité', 'Automobile', 'Mode', 'Beauté', 'Restauration', 'Événementiel', 'BTP', 'Assurance', 
    'Banque', 'Assistance', 'Social', 'Culture', 'Recherche', 'Enseignement'
]

# Types de handicaps
handicaps = [
    'aucun', 'mental', 'auditif', 'visuel', 'moteur', 'psychique', 'mutilé', 
    'Autisme et Troubles Envahissants du Développement', 'Plurihandicap', 'Maladie invalidante', 
    'Polyhandicap', 'Traumatisme crânien', 'Maladie neurologique', 'Les troubles dys'
]

# Poids pour chaque type de handicap
weights_handicaps = [86] + [1] * (len(handicaps) - 1)

# Prénoms et noms spécifiques par genre et pays
prenoms_pays = {
    'Sénégal': {'homme': ["Mamadou", "Ibrahima", "Moussa", "Ousmane", "Abdou"], 'femme': ["Awa", "Fatou", "Aminata", "Ndeye", "Khady"]},
    'Maroc': {'homme': ["Omar", "Mohamed", "Hassan", "Ali"], 'femme': ["Fatima", "Nour", "Yasmine", "Amina"]},
    'Chine': {'homme': ["Linh", "Minh", "Tuan", "Dung"], 'femme': ["Yen", "Thanh", "Huong", "Hoa"]},
    'Hongrie': {'homme': ["Boris", "Ivan", "Viktor", "Maksim"], 'femme': ["Mila", "Daria", "Anya", "Nina"]},
    'France': {'homme': ["Jean", "Pierre", "Julien", "Antoine"], 'femme': ["Marie", "Lucie", "Camille", "Manon"]},
    'Algérie': {'homme': ["Karim", "Mehdi", "Youssef", "Sofiane"], 'femme': ["Zineb", "Sabrina", "Nadia", "Nora"]},
    'Tunisie': {'homme': ["Ali", "Fares", "Mehdi", "Amine"], 'femme': ["Leila", "Rania", "Hana", "Sarra"]},
    'Côte d\'Ivoire': {'homme': ["Adama", "Kouadio", "Bakary", "Mamadou"], 'femme': ["Aïcha", "Fatoumata", "Kadiatou", "Aminata"]},
    'Nigeria': {'homme': ["Olufemi", "Chinedu", "Obinna", "Chukwu"], 'femme': ["Ngozi", "Yemi", "Chinwe", "Chinonye"]},
    'Afrique du Sud': {'homme': ["Thabo", "Mandla", "Sizwe", "Sipho"], 'femme': ["Nandi", "Thandeka", "Ntombi", "Nomvula"]}
    
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
nationalites_afrique = ['Sénégal', 'Algérie', 'Tunisie', 'Côte d\'Ivoire', 'Nigeria', 'Afrique du Sud', 'Congo', 'Cameroun', 'Togo', 'Ghana', 'Bénin', 'Angola', 'Mali', 'Mauritanie', 'Maroc']
nationalites_asie = ['Chine', 'Vietnam', 'Cambodge', 'Inde', 'Pakistan', 'Japon', 'Corée du Sud']
nationalites_europe = ['Hongrie', 'France', 'Allemagne', 'Italie', 'Espagne', 'Portugal', 'Royaume-Uni', 'Pays-Bas', 'Belgique', 'Suisse', 'Suède', 'Norvège', 'Danemark', 'Finlande', 'Grèce', 'Pologne', 'Ukraine', 'Russie']
nationalites_ameriques = ['Brésil', 'Argentine', 'Mexique', 'Colombie', 'Chili', 'Pérou', 'Venezuela', 'Canada', 'États-Unis', 'Antilles Françaises']

# Écoles réelles
ecoles = {
    'Bep': ['Lycée professionnel Jean Moulin', 'Lycée professionnel Louis Armand', 'Lycée professionnel Gustave Eiffel', 'Lycée professionnel Jules Ferry', 'Lycée professionnel Henri IV', 'Lycée professionnel Van Gogh', 'Lycée professionnel Jean Jaurès', 'Lycée professionnel Victor Hugo'], 
    'Baccalauréat': ['Lycée Van Gogh', 'Lycée Jean Jaurès', 'Lycée Henri IV', 'Lycée Victor Hugo', 'Lycée Louis Armand', 'Lycée Jules Ferry', 'Lycée Gustave Eiffel', 'Lycée Jean Moulin'],
    'BTS': ['Lycée Louis Armand', 'Lycée Jules Ferry', 'Lycée Gustave Eiffel', 'Lycée Jean Jaurès', 'Lycée Victor Hugo', 'Lycée Van Gogh', 'Lycée Jean Moulin', 'Lycée Henri IV'],
    'Licence': ['Université Paris 1 Panthéon-Sorbonne', 'Université de Bordeaux', 'Université de Lille', 'Université de Lyon', 'Université de Marseille', 'Université de Montpellier', 'Université de Nantes', 'Université de Strasbourg'],
    'Master': ['Université Paris-Dauphine', 'Université de Strasbourg', 'Université de Grenoble', 'Université de Toulouse', 'Université de Rennes', 'Université de Nice', 'Université de Reims', 'Université de Tours', 'Université de Poitiers', 'Université de Limoges', 'Université de Pau', 'Université de Perpignan', 'Université Cheikh Anta Diop', 'Université de Ouagadougou', 'Université de Bamako', 'Université de Kinshasa', 'Université de Brazzaville', 'Université de Libreville'],
    'Ingénieur': ['École Polytechnique', 'École Centrale Paris', 'École des Ponts ParisTech', 'École des Mines ParisTech', 'École Normale Supérieure', 'École Supérieure de Physique et de Chimie Industrielles', 'École Nationale des Ponts et Chaussées', 'École Nationale Supérieure des Mines de Saint-Étienne', 'CentraleSupélec', 'Conservation des Arts et Métiers', 'École Nationale Supérieure de Techniques Avancées'],
    'Doctorat': ['Université Paris-Saclay', 'Université de Lyon', 'Université de Marseille', 'Université de Montpellier', 'Université de Nantes', 'Université de Strasbourg', 'Université de Bordeaux', 'Université de Lille', 'Université de Toulouse']
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
    'lecture', 'sport', 'voyages', 'musique', 'cinéma', 'cuisine', 'photographie', 'jardinage', 'randonnée', 
    'peinture', 'écriture', 'danse', 'natation', 'cyclisme', 'course à pied', 'yoga', 'méditation', 'programmation', 
    'jeux vidéo', 'bricolage', 'sculpture', 'théâtre', 'chant', 'pêche', 'astronomie', 'mode', 'dessin', 'volleyball', 
    'basketball', 'football', 'rugby', 'tennis', 'badminton', 'escalade', 'ski', 'snowboard', 'surf', 'kayak', 'canoë', 
    'parapente', 'parachutisme', 'planche à voile', 'plongée', 'équitation', 'patinage', 'escrime', 'karaté', 'judo', 
    'taekwondo', 'aikido', 'boxe', 'haltérophilie', 'fitness', 'musculation', 'bodybuilding', 'crossfit', 'pilates', 
    'spinning', 'danse classique', 'danse contemporaine', 'danse hip-hop', 'danse salsa', 'danse tango', 'danse flamenco', 
    'danse de salon', 'danse orientale', 'danse africaine', 'danse indienne', 'danse jazz', 'danse moderne', 'électronique', 
    'mécanique', 'robotique', 'domotique', 'maquettisme', 'modélisme', 'radiocommandé', 'cinéma amateur', 'réalisation de films', 
    'montage vidéo'
]

# Compétences humaines
competences_humaines_list = [
    'Communication', 'Travail en équipe', 'Gestion du temps', 'Résolution de problèmes', 'Leadership', 'Adaptabilité', 
    'Créativité', 'Esprit critique', 'Empathie', 'Motivation', 'Gestion du stress', 'Prise de décision', 'Négociation', 
    'Persuasion', 'Gestion de conflits', 'Organisation', 'Autonomie', 'Sens des responsabilités', 'Fiabilité', 'Dynamisme', 
    'Polyvalence', 'Sens du service'
]

# Compétences techniques par domaine
competences_techniques = {
    'Informatique': ['Python', 'SQL', 'Java', 'C++', 'HTML', 'CSS', 'JavaScript', 'Linux', 'Git', 'Django', 'Flask', 
                     'React', 'Angular', 'Vue.js', 'Node.js', 'Express.js', 'MongoDB', 'PostgreSQL', 'MySQL', 'SQLite', 
                     'NoSQL', 'API', 'REST', 'GraphQL', 'Docker', 'Kubernetes', 'CI/CD', 'AWS', 'Azure', 'GCP', 'Heroku', 
                     'Firebase', 'Jenkins', 'Ansible', 'Terraform', 'Kafka', 'RabbitMQ', 'Redis', 'Elasticsearch', 'Kibana', 
                     'Logstash', 'Prometheus', 'Grafana', 'Nginx', 'Apache', 'Jira', 'Confluence', 'Slack', 'Trello', 'Asana', 
                     'GitLab', 'GitHub', 'Bitbucket', 'Jenkins', 'Travis CI', 'CircleCI', 'Codecov', 'SonarQube', 'Jest', 
                     'Pytest', 'Mocha', 'Chai', 'Cypress', 'Selenium', 'JMeter', 'Postman', 'Swagger', 'OpenAPI', 'OAuth', 
                     'JWT', 'SAML', 'PHP', 'Base de données', 'Sécurité informatique', 'Sécurité Réseaux', 'Sécurité Cloud', 
                     'Développement web', 'Développement mobile', 'Développement logiciel', 'Développement d\'applications', 
                     'Développement d\'API', 'Développement back-end', 'Développement front-end', 'Développement full-stack', 
                     'Développement cloud', 'Développement DevOps', 'Développement Big Data', 'Développement IA', 'Développement IoT', 
                     'Développement blockchain', 'Développement AR/VR', 'Développement jeux vidéo', 'Développement systèmes embarqués', 
                     'Développement sécurité', 'Développement qualité', 'Développement test', 'Développement automatisation', 
                     'Développement maintenance', 'Développement support', 'Développement consulting', 'Développement formation', 
                     'Développement gestion de projet', 'Développement recherche', 'Développement veille technologique', 
                     'Machine Learning', 'Deep Learning', 'Data Science', 'Data Engineering', 'Data Analysis', 'Data Mining', 
                     'Data Warehousing', 'Data Modeling', 'Data Visualization', 'Business Intelligence', 'ETL', 'ELT', 'OLAP', 
                     'OLTP', 'DWH', 'BI', 'Big Data', 'Hadoop', 'Spark', 'Flink', 'Kafka', 'Hive', 'Pig', 'Sqoop', 'Flume', 
                     'HBase', 'Cassandra', 'MongoDB', 'Redis', 'MySQL', 'PostgreSQL'],
    'Santé': ['Soins infirmiers', 'Anatomie', 'Pharmacologie', 'Gestion des patients', 'Premiers secours', 'Soins intensifs', 
              'Soins palliatifs', 'Soins à domicile', 'Soins pédiatriques', 'Soins gériatriques', 'Soins obstétriques', 
              'Soins psychiatriques', 'Soins chirurgicaux', 'Soins médicaux', 'Soins dentaires', 'Soins ophtalmologiques', 
              'Soins ORL', 'Soins dermatologiques', 'Soins orthopédiques', 'Soins neurologiques', 'Soins cardiovasculaires', 
              'Soins respiratoires', 'Soins oncologiques', 'Soins endocriniens', 'Soins urologiques', 'Éducation thérapeutique', 
              'Gestion des dossiers médicaux', 'Utilisation des équipements médicaux', 'Connaissances en bioéthique', 
              'Soins d’urgence', 'Gestion des maladies chroniques'],
    'Finance': ['Comptabilité', 'Analyse financière', 'Gestion de trésorerie', 'Audit', 'Prévision financière', 
                'Contrôle de gestion', 'Finance d\'entreprise', 'Finance de marché', 'Finance de projet', 'Finance internationale', 
                'Gestion des risques financiers', 'Modélisation financière', 'Fusions et acquisitions', 'Gestion d’actifs', 
                'Gestion de portefeuille', 'Compliance financière', 'Fiscalité', 'Reporting financier', 'Analyse de crédit', 
                'Banque d’investissement'],
    'Éducation': ['Pédagogie', 'Gestion de classe', 'Planification de cours', 'Évaluation', 'Didactique', 
                  'Technologies éducatives', 'Formation continue', 'Orientation scolaire', 'Conseil pédagogique', 
                  'Recherche en éducation', 'Développement de programmes éducatifs', 'Gestion des comportements', 
                  'Accompagnement des élèves à besoins particuliers', 'Création de supports pédagogiques', 
                  'Utilisation des plateformes d’apprentissage en ligne', 'Coordination pédagogique', 'Mentorat et tutorat', 
                  'Animation d’ateliers'],
    'Ingénierie': ['AutoCAD', 'MATLAB', 'Gestion de projet', 'Conception', 'Modélisation 3D', 'Calculs de structures', 
                   'Calculs thermiques', 'Calculs électriques', 'Calculs hydrauliques', 'Calculs mécaniques', 'Calculs aérodynamiques', 
                   'Calculs acoustiques', 'Calculs optiques', 'Calculs électromagnétiques', 'Calculs quantiques', 'Calculs statistiques', 
                   'Calculs probabilistes', 'Solidworks', 'Catia', 'NX', 'Creo', 'Inventor', 'Revit', 'RobotStudio', 'TIA Portal', 
                   'Fusion 360', 'Creality', 'Ultimaker', 'Prusa', 'Ansys', 'Abaqus', 'Comsol', 'StarCCM+', 'Ingénierie des matériaux', 
                   'Thermodynamique', 'Énergie renouvelable', 'Ingénierie de l’environnement', 'Mécatronique', 'Contrôle des systèmes', 
                   'Robotiques', 'Gestion de la qualité', 'Lean Manufacturing', 'Six Sigma', 'Gestion des coûts', 'Gestion des risques', 
                   'Planification et ordonnancement de la production'],
    'Marketing': ['SEO', 'Publicité', 'Analyse de marché', 'Stratégie de marque', 'Réseaux sociaux', 'Marketing digital', 
                  'Marketing de contenu', 'Marketing viral', 'Marketing relationnel', 'Marketing événementiel', 'Marketing direct', 
                  'Marketing de proximité', 'Marketing de masse', 'CRM', 'Publicité en ligne', 'Email marketing', 'Analytics', 
                  'Google Analytics', 'Google Ads', 'Facebook Ads', 'Content Management System (CMS)', 'Automatisation du marketing', 
                  'Influence marketing', 'Branding', 'Gestion de la réputation en ligne', 'Segmentation du marché', 'Optimisation des taux de conversion (CRO)', 
                  'Création de campagnes marketing', 'Planification des médias'],
    'Ventes': ['Négociation', 'Gestion des comptes', 'Service à la clientèle', 'Prospection', 'CRM', 'Vente B2B', 'Vente B2C', 
               'Vente en ligne', 'Vente en magasin', 'Vente par téléphone', 'Techniques de closing', 'Stratégie de vente', 
               'Analyse des performances de vente', 'Gestion des objections', 'Formation des équipes de vente', 
               'Développement des relations clients', 'Techniques de présentation', 'Gestion des ventes complexes', 'Vente consultative', 
               'Développement des affaires', 'Suivi après-vente'],
    'Droit': ['Droit des affaires', 'Droit pénal', 'Rédaction de contrats', 'Conseil juridique', 'Plaidoyer', 'Droit du travail', 
              'Droit de la famille', 'Droit des sociétés', 'Droit fiscal', 'Droit immobilier', 'Droit international', 'Droit commercial', 
              'Droit de la propriété intellectuelle', 'Droit des nouvelles technologies', 'Droit de l’environnement', 'Droit de la consommation', 
              'Contentieux', 'Médiation', 'Arbitrage', 'Droit des assurances', 'Compliance', 'Rédaction de mémoires', 'Analyse juridique', 
              'Veille juridique'],
    'Média': ['Montage vidéo', 'Journalisme', 'Photographie', 'Rédaction', 'Gestion des réseaux sociaux', 'Production audiovisuelle', 
              'Animation', 'Infographie', 'Édition', 'Révision de contenu', 'Techniques de reportage', 'Écriture de scripts', 'SEO pour les médias', 
              'Gestion de communauté', 'Relations publiques', 'Gestion de projet médiatique', 'Marketing des médias', 'Planification éditoriale', 
              'Conception sonore', 'Réalisation de documentaires'],
    'Manufacture': ['Supervision', 'Maintenance', 'Qualité', 'Production', 'Planification', 'Gestion de la chaîne logistique', 
                    'Contrôle des stocks', 'Automatisation des processus', 'Lean Manufacturing', 'Six Sigma', 'Gestion des opérations', 
                    'Sécurité industrielle', 'Gestion des flux de production', 'Planification des capacités', 'Optimisation des processus', 
                    'Maintenance prédictive', 'Contrôle statistique des processus (SPC)', 'Gestion des ressources humaines', 
                    'Implantation des équipements', 'Gestion des coûts de production'],
    'Commerce': ['Gestion de stock', 'Relation client', 'Stratégie de vente', 'Merchandising', 'Logistique', 'Gestion des achats', 
                 'Négociation avec les fournisseurs', 'Analyse des ventes', 'Gestion de la chaîne d’approvisionnement', 'E-commerce', 
                 'Marketing de détail', 'Service après-vente', 'Organisation des promotions', 'Planification des ventes', 'Gestion des inventaires', 
                 'Optimisation des processus de vente', 'Analyse des données de vente', 'Développement des relations clients', 'Prévisions des ventes', 
                 'Techniques de vente'],
    'Hôtellerie': ['Accueil', 'Service en salle', 'Service en chambre', 'Service en cuisine', 'Service en bar', 'Gestion des réservations', 
                   'Gestion des plaintes clients', 'Coordination des événements', 'Gestion de la réception', 'Supervision du personnel', 
                   'Hygiène et sécurité alimentaire', 'Organisation des conférences et banquets', 'Gestion des coûts', 'Marketing hôtelier', 
                   'Relation avec les clients VIP', 'Gestion des opérations hôtelières', 'Techniques de vente et de promotion', 'Gestion des équipements hôteliers', 
                   'Maintenance des installations', 'Service de conciergerie'],
    'Transport': ['Logistique', 'Gestion de flotte', 'Conduite', 'Maintenance', 'Sécurité', 'Planification des itinéraires', 
                  'Optimisation des coûts de transport', 'Gestion des stocks', 'Réglementation du transport', 'Gestion des expéditions', 
                  'Coordination des livraisons', 'Suivi des performances de livraison', 'Service à la clientèle', 'Gestion des opérations de transport', 
                  'Transport international', 'Gestion des entrepôts', 'Gestion des documents de transport', 'Technologies de l’information pour la logistique', 
                  'Contrôle des coûts', 'Gestion des contrats de transport'],
    'Énergie': ['Production', 'Distribution', 'Renouvelable', 'Nucléaire', 'Pétrole', 'Gestion des réseaux électriques', 
                'Énergie éolienne', 'Énergie solaire', 'Énergie hydroélectrique', 'Gestion de la demande énergétique', 
                'Maintenance des infrastructures énergétiques', 'Réglementation énergétique', 'Optimisation des ressources énergétiques', 
                'Audit énergétique', 'Conception des systèmes énergétiques', 'Économie de l’énergie', 'Planification énergétique', 
                'Technologies des smart grids', 'Sécurité des installations énergétiques', 'Stockage de l’énergie', 'Innovation énergétique'],
    'Immobilier': ['Transaction', 'Location', 'Gestion', 'Promotion', 'Construction', 'Estimation immobilière', 'Négociation immobilière', 
                   'Droit immobilier', 'Gestion de patrimoine', 'Commercialisation de biens', 'Gestion de copropriété', 'Prospection foncière', 
                   'Marketing immobilier', 'Financement immobilier', 'Gestion des baux', 'Gestion des relations clients', 'Aménagement du territoire', 
                   'Développement immobilier', 'Gestion des projets immobiliers', 'Évaluation des risques immobiliers'],
    'Télécommunications': ['Réseaux', 'Téléphonie', 'Fibre', 'Satellite', 'Mobile', 'Sécurité des réseaux', 'Gestion des infrastructures télécom', 
                           'Réglementation des télécommunications', 'Maintenance des équipements télécom', 'Conception des réseaux', 'Technologies 5G', 
                           'Internet des objets (IoT)', 'Gestion des services télécom', 'Développement des offres télécom', 'Gestion de la bande passante', 
                           'Optimisation des réseaux', 'Supervision des réseaux', 'Gestion des clients télécom', 'Innovation télécom', 'Communication unifiée', 
                           'Téléphonie IP', 'Gestion des projets télécom', 'Déploiement des réseaux'],
    'Divertissement': ['Animation', 'Musique', 'Théâtre', 'Cirque', 'Cinéma', 'Production audiovisuelle', 'Gestion de projets culturels', 
                       'Organisation de spectacles', 'Gestion des droits d’auteur', 'Marketing des arts', 'Réalisation de films', 'Scénarisation', 
                       'Design sonore', 'Organisation d’événements', 'Gestion des équipements de scène', 'Technologies du spectacle', 'Création de contenus', 
                       'Gestion de la billetterie', 'Promotion des artistes', 'Relations publiques pour les arts'],
    'Sports': ['Entraînement', 'Arbitrage', 'Compétition', 'Organisation', 'Santé', 'Préparation physique', 'Coaching sportif', 
               'Gestion des installations sportives', 'Planification des entraînements', 'Gestion des événements sportifs', 'Nutrition sportive', 
               'Récupération et rééducation des sportifs', 'Analyse de la performance', 'Gestion des équipes sportives', 'Marketing sportif', 'Psychologie du sport', 
               'Médias sportifs', 'Gestion des talents sportifs', 'Évaluation des capacités physiques', 'Organisation des compétitions', 'Gestion des sponsors'],
    'Science': ['Recherche', 'Expérimentation', 'Analyse', 'Publication', 'Enseignement', 'Gestion de projets de recherche', 
                'Rédaction de protocoles de recherche', 'Collecte et traitement des données', 'Statistiques scientifiques', 'Rédaction d’articles scientifiques', 
                'Présentations scientifiques', 'Collaboration interdisciplinaire', 'Gestion des laboratoires', 'Éthique de la recherche', 'Développement de nouvelles technologies', 
                'Brevetage', 'Innovation scientifique', 'Gestion des financements de recherche', 'Formation scientifique', 'Réalisation d’études cliniques', 
                'Utilisation des équipements de laboratoire', 'Analyse des résultats de recherche'],
    'Fonction publique': ['Administration', 'Service', 'Sécurité', 'Justice', 'Éducation', 'Santé', 'Gestion des ressources publiques', 'Droit public', 
                          'Politiques publiques', 'Gestion des budgets publics', 'Communication publique', 'Gestion des crises', 'Relations internationales', 
                          'Gestion des infrastructures publiques', 'Gestion des ressources humaines publiques', 'Planification urbaine', 'Protection de l’environnement public', 
                          'Médiation sociale', 'Sécurité publique', 'Gestion des services sociaux', 'Gestion des transports publics'],
    'Logistique': ['Gestion de stock', 'Transport', 'Distribution', 'Approvisionnement', 'Manutention', 'Gestion des entrepôts', 'Planification logistique', 
                   'Optimisation des flux logistiques', 'Gestion des inventaires', 'Gestion des fournisseurs', 'Suivi des expéditions', 'Réglementation du transport', 
                   'Sécurité logistique', 'Analyse des performances logistiques', 'Gestion des retours', 'Gestion des coûts logistiques', 'Transport international', 
                   'Technologies de l’information pour la logistique', 'Gestion des risques logistiques', 'Coordination des opérations logistiques', 
                   'Élaboration des plans logistiques', 'Supervision des équipes logistiques'],
    'Banque': ['Gestion de compte', 'Crédit', 'Assurance', 'Placements', 'Conseil', 'Gestion des risques bancaires', 'Analyse financière', 
               'Services bancaires aux particuliers', 'Services bancaires aux entreprises', 'Gestion des portefeuilles', 'Fusions et acquisitions', 
               'Banque d’investissement', 'Conformité réglementaire', 'Audit interne', 'Gestion de la trésorerie', 'Crédits hypothécaires', 'Crédits à la consommation', 
               'Crédits commerciaux', 'Analyse des crédits', 'Gestion des actifs', 'Gestion des liquidités', 'Banque digitale'],
    'Assurance': ['Assurance vie', 'Assurance auto', 'Assurance habitation', 'Assurance santé', 'Assurance voyage', 'Gestion des risques assurantiels', 
                  'Souscription des polices d’assurance', 'Gestion des sinistres', 'Évaluation des risques', 'Assurance responsabilité civile', 
                  'Assurance des biens', 'Assurance des personnes', 'Assurance des entreprises', 'Assurance maritime', 'Assurance aviation', 'Assurance agricole', 
                  'Assurance construction', 'Assurance professionnelle', 'Gestion des réclamations', 'Audit des assurances', 'Conformité réglementaire', 
                  'Développement de produits d’assurance'],
    'Consulting': ['Conseil', 'Audit', 'Stratégie', 'Transformation', 'Formation', 'Gestion de projet', 'Gestion du changement', 
                   'Gestion de la performance', 'Analyse des processus', 'Optimisation des processus', 'Gestion des risques', 'Gestion de la qualité', 
                   'Conseil en innovation', 'Conseil en management', 'Conseil en organisation', 'Conseil en stratégie d’entreprise', 'Conseil en ressources humaines', 
                   'Conseil en technologie', 'Conseil en développement durable', 'Accompagnement à la transformation digitale', 'Benchmarking', 'Conseil en marketing', 
                   'Conseil en vente'],
    'Ressources humaines': ['Recrutement', 'Formation', 'Gestion de carrière', 'Gestion de paie', 'Gestion des conflits', 'Développement organisationnel', 
                            'Gestion de la performance', 'Gestion des talents', 'Relations de travail', 'Gestion des avantages sociaux', 'Planification des ressources humaines', 
                            'Droit du travail', 'Santé et sécurité au travail', 'Gestion des relations syndicales', 'Gestion des effectifs', 'Gestion des compétences', 
                            'Développement des compétences', 'Gestion des programmes de reconnaissance', 'Médiation', 'Gestion de la diversité', 'Gestion des expatriés'],
    'Communication': ['Relations publiques', 'Communication interne', 'Communication externe', 'Communication digitale', 'Communication événementielle', 
                      'Rédaction de communiqués de presse', 'Gestion des médias', 'Gestion de crise', 'Gestion de la réputation', 'Stratégie de communication', 
                      'Relations institutionnelles', 'Community management', 'Création de contenu', 'Planification de la communication', 'Organisation d’événements', 
                      'Veille médiatique', 'Gestion des réseaux sociaux', 'Rédaction de discours', 'Édition de newsletters', 'Communication corporate'],
    'Maintenance': ['Maintenance préventive', 'Maintenance curative', 'Maintenance corrective', 'Maintenance prédictive', 'Maintenance conditionnelle', 
                    'Gestion des équipements', 'Gestion de la maintenance assistée par ordinateur (GMAO)', 'Planification de la maintenance', 'Gestion des stocks de pièces détachées', 
                    'Diagnostic des pannes', 'Supervision des équipes de maintenance', 'Sécurité des installations', 'Formation des techniciens de maintenance', 
                    'Optimisation des processus de maintenance', 'Gestion des contrats de maintenance', 'Maintenance industrielle', 'Maintenance des bâtiments', 
                    'Maintenance des infrastructures', 'Audit de maintenance', 'Amélioration continue de la maintenance'],
    'Sécurité': ['Sécurité des biens', 'Sécurité des personnes', 'Sécurité incendie', 'Sécurité informatique', 'Sécurité des données', 'Gestion des risques', 
                 'Surveillance', 'Gestion des accès', 'Protection rapprochée', 'Sécurité électronique', 'Planification de la sécurité', 'Intervention en cas de crise', 
                 'Formation à la sécurité', 'Rédaction de plans de sécurité', 'Contrôle des installations de sécurité', 'Gestion des incidents de sécurité', 
                 'Conformité aux normes de sécurité', 'Prévention des risques', 'Sécurité des événements', 'Cyber-sécurité', 'Analyse des risques sécuritaires', 
                 'Gestion des systèmes d’alarme', 'Réalisation d’audits de sécurité'],
    'Automobile': ['Conception', 'Production', 'Maintenance', 'Vente', 'Réparation', 'Diagnostic des pannes automobiles', 'Mécanique automobile', 
                   'Électronique automobile', 'Carrosserie', 'Peinture automobile', 'Gestion des stocks de pièces détachées', 'Technologies de l’automobile', 
                   'Contrôle qualité des véhicules', 'Réalisation des contrôles techniques', 'Vente de véhicules neufs', 'Vente de véhicules d’occasion', 
                   'Service après-vente automobile', 'Maintenance préventive des véhicules', 'Gestion des garanties', 'Gestion des réclamations clients', 
                   'Optimisation des processus de production automobile', 'Gestion des équipes de production'],
    'Mode': ['Design', 'Stylisme', 'Couture', 'Modélisme', 'Marketing', 'Gestion de collection', 'Achats de mode', 'Communication de mode', 
             'Gestion des événements de mode', 'Commercialisation des produits de mode', 'Merchandising visuel', 'Analyse des tendances de mode', 
             'Développement de produits de mode', 'Gestion de la production de mode', 'Négociation avec les fournisseurs de mode', 'Élaboration des prototypes de mode', 
             'Gestion des relations avec les créateurs de mode', 'Gestion de la chaîne d’approvisionnement en mode', 'Organisation de défilés de mode', 
             'Photographie de mode', 'Rédaction pour les médias de mode', 'Création de moodboards', 'Gestion des réseaux sociaux de mode'],
    'Technique': ['Électricité', 'Mécanique', 'Plomberie', 'Menuiserie', 'Soudure', 'Maintenance des équipements techniques', 'Installation de systèmes techniques', 
                  'Diagnostic des pannes techniques', 'Réalisation des schémas techniques', 'Gestion des chantiers techniques', 'Conformité aux normes techniques', 
                  'Optimisation des processus techniques', 'Supervision des équipes techniques', 'Gestion des stocks de pièces techniques', 'Formation des techniciens', 
                  'Sécurité des installations techniques', 'Gestion des projets techniques', 'Programmation des automates', 'Contrôle des installations techniques', 
                  'Réalisation des essais techniques', 'Gestion des contrats de maintenance technique'],
    'Production': ['Fabrication', 'Assemblage', 'Conditionnement', 'Contrôle qualité', 'Logistique', 'Optimisation des processus de production', 
                   'Gestion des stocks de matières premières', 'Planification de la production', 'Gestion des flux de production', 'Maintenance des équipements de production', 
                   'Gestion des équipes de production', 'Sécurité industrielle', 'Analyse des performances de production', 'Gestion des coûts de production', 'Lean Manufacturing', 
                   'Six Sigma', 'Amélioration continue de la production', 'Conformité aux normes de production', 'Automatisation des processus de production', 
                   'Gestion des déchets de production', 'Formation des opérateurs de production', 'Supervision des lignes de production'],
    'Agriculture': ['Culture', 'Élevage', 'Pêche', 'Sylviculture', 'Agroalimentaire', 'Gestion des exploitations agricoles', 'Utilisation des équipements agricoles', 
                    'Gestion des cultures agricoles', 'Élevage des animaux de ferme', 'Gestion des stocks de produits agricoles', 'Transformation des produits agricoles', 
                    'Commercialisation des produits agricoles', 'Analyse des sols agricoles', 'Gestion des ressources en eau pour l’agriculture', 'Planification des récoltes', 
                    'Gestion des maladies des cultures', 'Innovation agricole', 'Agriculture biologique', 'Utilisation des technologies agricoles', 'Gestion des déchets agricoles', 
                    'Conformité aux normes agricoles', 'Gestion des subventions agricoles', 'Optimisation des rendements agricoles', 'Formation des agriculteurs', 
                    'Développement des pratiques agricoles durables'],
    'Art': ['Peinture', 'Sculpture', 'Photographie', 'Dessin', 'Cinéma', 'Histoire de l’art', 'Critique d’art', 'Conservation des œuvres d’art', 'Curatelle', 
            'Gestion des galeries d’art', 'Organisation des expositions d’art', 'Restauration des œuvres d’art', 'Évaluation des œuvres d’art', 'Commercialisation des œuvres d’art', 
            'Communication pour les artistes', 'Création de catalogues d’art', 'Gestion des collections d’art', 'Création de portfolios artistiques', 
            'Développement des compétences artistiques', 'Animation des ateliers d’art', 'Médiation culturelle', 'Promotion des artistes', 'Formation artistique', 
            'Gestion des contrats artistiques', 'Négociation avec les collectionneurs', 'Analyse des tendances artistiques', 'Réalisation des projets artistiques'],
    'Design': ['Graphisme', 'Web design', 'Design industriel', 'Design d\'intérieur', 'Design de mode', 'Illustration', 'Création de logos', 'Typographie', 
               'Animation graphique', 'Création de sites web', 'UX/UI design', 'Conception de produits', 'Prototypage', 'Conception de packaging', 'Design interactif', 
               'Design d’expérience utilisateur', 'Création de wireframes', 'Création de maquettes', 'Impression 3D', 'Design d’espace', 'Design environnemental', 
               'Infographie', 'Réalité augmentée', 'Réalité virtuelle', 'Gestion des projets de design', 'Création d’identités visuelles', 'Design thinking', 
               'Utilisation des logiciels de design (Photoshop, Illustrator, InDesign)'],
    'Environnement': ['Écologie', 'Développement durable', 'Gestion des déchets', 'Énergies renouvelables', 'Biodiversité', 'Analyse environnementale', 'Audit environnemental', 
                      'Gestion des ressources naturelles', 'Gestion de l’eau', 'Gestion de l’air', 'Gestion des sols', 'Planification environnementale', 
                      'Gestion des risques environnementaux', 'Éducation à l’environnement', 'Gestion des espaces naturels', 'Protection de la faune et de la flore', 
                      'Gestion des projets environnementaux', 'Conformité aux réglementations environnementales', 'Évaluation de l’impact environnemental', 
                      'Gestion des émissions de gaz à effet de serre', 'Gestion des zones protégées', 'Conservation des habitats naturels', 'Restauration écologique', 
                      'Utilisation des technologies environnementales', 'Gestion des catastrophes naturelles'],
    'Tourisme': ['Hôtellerie', 'Restauration', 'Guidage', 'Animation', 'Transport', 'Gestion des agences de voyage', 'Organisation des circuits touristiques', 
                 'Marketing touristique', 'Gestion des réservations de voyages', 'Gestion des événements touristiques', 'Gestion des relations clients dans le tourisme', 
                 'Gestion des équipements touristiques', 'Optimisation des itinéraires touristiques', 'Développement des produits touristiques', 'Planification des voyages', 
                 'Analyse des tendances touristiques', 'Gestion des services touristiques', 'Réglementation touristique', 'Promotion des destinations touristiques', 
                 'Gestion des contrats touristiques', 'Écotourisme', 'Tourisme durable', 'Animation des groupes touristiques']
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
    'Informatique': ["Développement et maintenance des applications web", "Analyse des besoins des utilisateurs et conception des solutions logicielles", 
                     "Supervision des projets de développement informatique", "Assistance technique et résolution des problèmes informatiques", 
                     "Formation des utilisateurs sur les nouvelles technologies"],
    'Santé': ["Prise en charge des patients et administration des soins", "Préparation et administration des médicaments", "Gestion des dossiers médicaux et suivi des patients", 
              "Collaboration avec les médecins pour établir les diagnostics", "Participation aux campagnes de prévention et d'éducation à la santé"],
    'Finance': ["Analyse des états financiers et élaboration des rapports", "Gestion de la trésorerie et des flux de trésorerie", "Réalisation des audits internes et externes", 
                "Élaboration des prévisions financières et des budgets", "Conseil en matière de gestion financière et d'investissement"],
    'Éducation': ["Préparation et animation des cours", "Suivi pédagogique et évaluation des étudiants", "Développement de programmes éducatifs", 
                  "Organisation et participation aux conseils de classe", "Encadrement des activités périscolaires et des projets éducatifs"],
    'Ingénierie': ["Conception et développement des systèmes mécaniques", "Réalisation des études techniques et des analyses de faisabilité", "Supervision des projets de construction et de maintenance", 
                   "Élaboration des plans et des schémas techniques", "Collaboration avec les équipes de production pour améliorer les procédés"],
    'Marketing': ["Développement et mise en œuvre des stratégies marketing", "Analyse du marché et identification des opportunités", "Gestion des campagnes publicitaires et promotionnelles", 
                  "Création de contenus pour les réseaux sociaux et le site web", "Suivi des performances des actions marketing et ajustements"],
    'Ventes': ["Prospection de nouveaux clients et développement du portefeuille", "Négociation des contrats et des conditions commerciales", "Suivi des commandes et des livraisons", 
               "Gestion des réclamations et des litiges", "Reporting des activités commerciales et des résultats"],
    'Droit': ["Conseil juridique aux clients et aux partenaires", "Rédaction des contrats et des actes juridiques", "Représentation des clients devant les tribunaux", 
              "Veille juridique et analyse de la réglementation", "Médiation et résolution des conflits"],
    'Média': ["Réalisation de reportages et d'interviews", "Montage et post-production des contenus audiovisuels", "Rédaction d'articles et de chroniques", 
              "Animation des réseaux sociaux et des plateformes web", "Organisation d'événements et de conférences de presse"],
    'Manufacture': ["Planification et organisation de la production", "Gestion des stocks et des approvisionnements", "Contrôle qualité des produits et des processus", 
                    "Maintenance préventive et curative des équipements", "Amélioration continue des méthodes de travail"],
    'Commerce': ["Gestion des achats et des approvisionnements", "Suivi des ventes et des indicateurs de performance", "Animation commerciale et merchandising", 
                 "Relation client et service après-vente", "Analyse des données de marché et des tendances"],
    'Hôtellerie': ["Accueil et prise en charge des clients", "Service en salle et en chambre", "Gestion des réservations et des plannings", 
                   "Coordination des équipes et des prestataires", "Suivi de la satisfaction client et traitement des réclamations"],
    'Transport': ["Organisation des tournées et des livraisons", "Gestion des stocks et des approvisionnements", "Maintenance préventive et curative des véhicules", 
                  "Sécurité des marchandises et des passagers", "Optimisation des coûts et des délais de transport"],
    'Énergie': ["Production et distribution d'énergie électrique", "Gestion des réseaux de transport et de distribution", "Développement des énergies renouvelables", 
                "Maintenance des installations et des équipements", "Sécurité des installations et des intervenants"],
    'Immobilier': ["Transaction et négociation immobilière", "Gestion locative et syndic de copropriété", "Promotion immobilière et construction", 
                   "Expertise et évaluation des biens", "Conseil en investissement et en financement"],
    'Télécommunications': ["Installation et maintenance des réseaux", "Déploiement des infrastructures de télécommunication", "Gestion des services et des abonnements", 
                           "Développement des offres et des produits", "Veille technologique et réglementaire"],
    'Divertissement': ["Animation et spectacle pour tous les publics", "Production et réalisation d'émissions et de films", "Organisation d'événements culturels et artistiques", 
                       "Promotion et diffusion des œuvres et des artistes", "Gestion des droits d'auteur et des contrats"],
    'Sports': ["Entraînement et préparation physique des sportifs", "Arbitrage et organisation des compétitions", "Gestion des infrastructures et des équipements", 
               "Suivi médical et rééducation des blessures", "Promotion et développement des disciplines sportives"],
    'Science': ["Recherche fondamentale et appliquée", "Expérimentation et analyse des données", "Publication des résultats et des découvertes", 
                "Enseignement et transmission des connaissances", "Collaboration avec les équipes internationales"],
    'Fonction publique': ["Administration des services publics", "Sécurité et protection des citoyens", "Justice et respect de la loi", 
                          "Éducation et formation des jeunes", "Santé et bien-être de la population"],
    'Logistique': ["Gestion des stocks et des approvisionnements", "Organisation des transports et des livraisons", "Optimisation des flux et des coûts logistiques", 
                   "Suivi des opérations et des indicateurs de performance", "Sécurité des biens et des personnes"],
    'Banque': ["Accueil et conseil aux clients", "Gestion des comptes et des transactions", "Analyse des risques et des crédits", 
               "Placement et gestion de patrimoine", "Conformité réglementaire et lutte contre la fraude"],
    'Assurance': ["Évaluation des risques et des sinistres", "Souscription des contrats et des polices", "Gestion des dossiers et des indemnisations", 
                  "Prévention et sécurité des biens et des personnes", "Développement des produits et des services"],
    'Consulting': ["Conseil en stratégie et en organisation", "Audit et diagnostic des performances", "Accompagnement du changement et des transformations", 
                   "Formation et développement des compétences", "Veille concurrentielle et technologique"],
    'Ressources humaines': ["Recrutement et intégration des collaborateurs", "Gestion des carrières et des compétences", "Formation et développement professionnel", 
                            "Gestion des conflits et des relations sociales", "Santé et qualité de vie au travail"],
    'Communication': ["Relations presse et relations publiques", "Communication interne et externe", "Événementiel et relations institutionnelles", 
                      "Community management et réseaux sociaux", "Création de contenus et de supports de communication"],
    'Environnement': ["Protection de la nature et des espèces", "Gestion des déchets et des ressources", "Étude et prévention des pollutions", 
                      "Aménagement et développement durable", "Sensibilisation et éducation à l'environnement"],
    'Agriculture': ["Production et transformation des cultures", "Élevage et transformation des animaux", "Gestion des exploitations et des terres", 
                    "Commercialisation et distribution des produits", "Innovation et développement des pratiques agricoles"],
    'Art': ["Création et production artistique", "Exposition et diffusion des œuvres", "Gestion de projets culturels et artistiques", 
            "Médiation et animation culturelle", "Formation et transmission des savoir-faire"],
    'Mode': ["Création et design de vêtements et d'accessoires", "Production et fabrication des collections", "Commercialisation et distribution des produits", 
             "Communication et promotion des marques", "Développement durable et éthique de la mode"],
    'Tourisme': ["Accueil et information des touristes", "Organisation et promotion des séjours", "Gestion des réservations et des prestations", 
                 "Animation et encadrement des activités", "Développement et valorisation des territoires"],
    'Restauration': ["Préparation et service des plats et des boissons", "Gestion des approvisionnements et des stocks", "Hygiène et sécurité alimentaire", 
                     "Accueil et satisfaction des clients", "Création et innovation culinaires"],
    'Événementiel': ["Organisation et coordination des événements", "Logistique et gestion des prestataires", "Communication et promotion des manifestations", 
                     "Accueil et animation des participants", "Évaluation et bilan des opérations"],
    'Sécurité': ["Surveillance et protection des biens et des personnes", "Prévention des risques et des intrusions", "Intervention et secours en cas d'incident", 
                 "Contrôle et vérification des accès", "Formation et sensibilisation à la sécurité"],
    'Technologies': ["Développement et maintenance des applications web", "Analyse des besoins des utilisateurs et conception des solutions logicielles", 
                     "Supervision des projets de développement informatique", "Assistance technique et résolution des problèmes informatiques", 
                     "Formation des utilisateurs sur les nouvelles technologies"],
    'Techniques': ["Conception et développement des systèmes mécaniques", "Réalisation des études techniques et des analyses de faisabilité", 
                   "Supervision des projets de construction et de maintenance", "Élaboration des plans et des schémas techniques", 
                   "Collaboration avec les équipes de production pour améliorer les procédés"],
    "Maintenance": ["Planification et organisation de la production", "Gestion des stocks et des approvisionnements", "Contrôle qualité des produits et des processus", 
                   "Maintenance préventive et curative des équipements", "Amélioration continue des méthodes de travail"],
    'Culture': ["Organisation d'événements culturels", "Gestion des collections et des expositions", "Développement de projets artistiques", 
                "Médiation culturelle et éducation artistique", "Promotion du patrimoine culturel"],
    'Design': ["Conception et réalisation de projets graphiques", "Création de supports de communication visuelle", "Développement de l'identité visuelle des marques", 
               "Mise en page et publication de contenus", "Veille créative et technologique"],
    "ONG": ["Sensibilisation et mobilisation des citoyens", "Défense des droits de l'homme et de l'environnement", "Actions humanitaires et solidaires", 
            "Plaidoyer et lobbying auprès des institutions", "Gestion de projets de développement et de coopération"],
    "Beauté": ["Conseil et diagnostic en esthétique", "Soins du visage et du corps", "Maquillage et coiffure", "Vente de produits cosmétiques", 
               "Formation et animation d'ateliers beauté"],
    "Industrie alimentaire": ["Production et transformation des denrées", "Contrôle qualité et sécurité alimentaire", "Gestion des approvisionnements et des stocks", 
                              "Commercialisation et distribution des produits", "Innovation et développement de nouveaux produits"],
    "Social": ["Accompagnement et soutien des personnes en difficulté", "Médiation et résolution des conflits", "Animation et encadrement des groupes", 
               "Écoute et conseil psychologique", "Coordination des actions sociales et solidaires"],
    "Aérospatial": ["Conception et fabrication d'aéronefs", "Maintenance et réparation des appareils", "Contrôle qualité et sécurité des vols", 
                    "Formation et certification des pilotes", "Recherche et développement de nouvelles technologies"],
    "Enseignement": ["Préparation et animation des cours", "Suivi pédagogique et évaluation des élèves", "Conception de supports pédagogiques", 
                     "Orientation et conseil aux étudiants", "Participation aux projets éducatifs et aux examens"],
    "Immobilier": ["Transaction et négociation immobilière", "Gestion locative et syndic de copropriété", "Promotion immobilière et construction", 
                   "Expertise et évaluation des biens", "Conseil en investissement et en financement"],
    "Manutention": ["Chargement et déchargement des marchandises", "Tri et rangement des produits", "Préparation des commandes et des expéditions", 
                    "Utilisation des engins de manutention", "Respect des consignes de sécurité et des délais"],
    "BTP": ["Construction et rénovation de bâtiments", "Gros œuvre et second œuvre", "Travaux publics et aménagement urbain", 
            "Coordination des chantiers et des équipes", "Respect des normes et des réglementations en vigueur"],
    "Assistance": ["Accueil et orientation des usagers", "Gestion des appels et des rendez-vous", "Traitement des dossiers administratifs", 
                   "Rédaction de courriers et de comptes-rendus", "Collaboration avec les services internes et externes"],
    "Défense": ["Protection du territoire et des citoyens", "Surveillance et renseignement militaire", "Intervention et secours en cas de crise", 
                "Formation et entraînement des soldats", "Coopération internationale et missions de paix"],
    "Automobile": ["Conception et fabrication des véhicules", "Maintenance et réparation des moteurs", "Contrôle qualité et sécurité routière", 
                   "Vente et location de véhicules", "Développement de nouvelles technologies et de motorisations"],
    "Recherche": ["Expérimentation et analyse des données", "Publication des résultats et des découvertes", "Enseignement et transmission des connaissances", 
                  "Collaboration avec les équipes internationales", "Innovation et développement de nouvelles technologies"]
}

# Générer les données factices
def generate_fake_data(num_records):
    data = []
    for i in range(num_records):
        nationalite = random.choice(nationalites_afrique + nationalites_asie + nationalites_europe + nationalites_ameriques)
        sexe = random.choices(['homme', 'femme'], weights=[92, 8], k=1)[0] if random.random() > 0.08 else random.choice(['homme', 'femme'])

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
        
        for j in range(random.randint(1, 5)):
            end_year = start_year + random.randint(1, 5)
            if end_year > datetime.now().year:
                end_year = datetime.now().year
            experiences.append({
                'intitulé_poste': intitule,
                'entreprise': random.choice(entreprises),
                'date_debut': f"{start_year}-01-01",
                'date_fin': f"{end_year}-12-31",
                'description': random.choice(descriptions_postes[domaine]) + f" {intitule} chez {random.choice(entreprises)}."
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
            for k in range(random.randint(0, 3))  # Maximum 3 recommendations
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

# Exporter le DataFrame en fichier CSV
csv_filename = 'cv_data.csv'
df.to_csv(csv_filename, index=False)

print(f"DataFrame generated and saved to {json_filename} and {csv_filename}")
