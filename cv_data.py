import json
import pandas as pd
from faker import Faker
import random
from datetime import datetime

# Initialiser Faker
fake = Faker('fr_FR')

# Domaines étendus
domaines = [
    'Informatique', 'Santé', 'Finance', 'Éducation', 'Ingénierie', 'Marketing', 'Ventes', 
    'Droit', 'Manufacture', 'Commerce', 'Hôtellerie', 'Transport',
    'Énergie', 'Immobilier', 'Télécommunications', 'Média', 'Divertissement', 'Sports', 
    'Science', 'Fonction publique', 'ONG', 'Consulting', 'Art', 
    'Design', 'Agriculture', 'Industrie alimentaire', 'Aérospatial', 'Défense', 'Manutention',
    'Logistique', 'Ressources humaines', 'Environnement', 'Tourisme', 'Sécurité', 'Automobile',
    'Mode', 'Beauté', 'Restauration', 'Événementiel', 'BTP', 'Assurance', 'Banque',
    'Assistance', 'Social', 'Culture', 'Recherche', 'Technologie', 'Innovation'
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
weights_handicaps = [86] + [1] * (len(handicaps) - 1)  # 14% avec handicap répartis également parmi les types de handicaps

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
        'homme': ["Wei", "Ming", "Jian", "Li", "Chen"],
        'femme': ["Xia", "Ying", "Lan", "Mei", "Lina"]
    },
    'Hongrie': {
        'homme': ["Bence", "László", "Gábor", "Tamás", "Zoltán"],
        'femme': ["Anna", "Katalin", "Eszter", "Zsófia", "Erika"]
    },
    'France': {
        'homme': ["Jean", "Pierre", "Julien", "Antoine", "Louis"],
        'femme': ["Marie", "Lucie", "Camille", "Manon", "Claire"]
    },
    'Algérie': {
        'homme': ["Karim", "Mehdi", "Youssef", "Sofiane", "Nadir"],
        'femme': ["Zineb", "Sabrina", "Nadia", "Nora", "Lina"]
    },
    'Tunisie': {
        'homme': ["Ali", "Fares", "Mehdi", "Amine", "Hamza"],
        'femme': ["Leila", "Rania", "Hana", "Sarra", "Mouna"]
    },
    'Côte d\'Ivoire': {
        'homme': ["Adama", "Kouadio", "Bakary", "Mamadou", "Yao"],
        'femme': ["Aïcha", "Fatoumata", "Kadiatou", "Aminata", "Mariama"]
    },
    'Nigeria': {
        'homme': ["Olufemi", "Chinedu", "Obinna", "Chukwu", "Emeka"],
        'femme': ["Ngozi", "Yemi", "Chinwe", "Chinonye", "Ifunanya"]
    },
    'Afrique du Sud': {
        'homme': ["Thabo", "Mandla", "Sizwe", "Sipho", "Bongani"],
        'femme': ["Nandi", "Thandeka", "Ntombi", "Nomvula", "Zanele"]
    },
    'Vietnam': {
        'homme': ["Nguyen", "Tran", "Le", "Pham", "Hoang"],
        'femme': ["Thuy", "Linh", "Trang", "Huong", "Anh"]
    },
    'Cambodge': {
        'homme': ["Sok", "Chea", "Chhim", "Pich", "Chann"],
        'femme': ["Sreyna", "Chanthou", "Sothea", "Pisey", "Davy"]
    },
    'Inde': {
        'homme': ["Rahul", "Sanjay", "Amit", "Vijay", "Arjun"],
        'femme': ["Anjali", "Sunita", "Pooja", "Kavita", "Rekha"]
    },
    'Pakistan': {
        'homme': ["Ahmed", "Ali", "Hassan", "Imran", "Usman"],
        'femme': ["Aisha", "Fatima", "Nadia", "Sana", "Zara"]
    },
    'Japon': {
        'homme': ["Hiroshi", "Kenji", "Takeshi", "Akira", "Yuto"],
        'femme': ["Yuki", "Sakura", "Rin", "Miyu", "Hana"]
    },
    'Corée du Sud': {
        'homme': ["Minho", "Jisoo", "Hyun", "Jin", "Taeyang"],
        'femme': ["Jiwoo", "Soojin", "Yuna", "Hyejin", "Nari"]
    },
    'Congo': {
        'homme': ["Mbemba", "Ndombe", "Ngita", "Mukoko", "Yoka"],
        'femme': ["Mwamba", "Ndaye", "Mbila", "Nzinga", "Lunda"]
    },
    'Cameroun': {
        'homme': ["Ndongo", "Ndomo", "Nji", "Biya", "Mbappe"],
        'femme': ["Ngono", "Nadege", "Elodie", "Berthe", "Florence"]
    },
    'Togo': {
        'homme': ["Kodjo", "Afi", "Yawovi", "Ayélé", "Kossi"],
        'femme': ["Akouvi", "Ama", "Afi", "Dede", "Yawa"]
    },
    'Ghana': {
        'homme': ["Kwame", "Kojo", "Yaw", "Kofi", "Kwesi"],
        'femme': ["Akosua", "Adwoa", "Abena", "Afia", "Ama"]
    },
    'Bénin': {
        'homme': ["Agnidé", "Sèmèvo", "Dossou", "Koutché", "Houngbédji"],
        'femme': ["Adjovi", "Akpédjé", "Amavi", "Gnanhoui", "Ayawa"]
    },
    'Angola': {
        'homme': ["Manuel", "João", "Pedro", "José", "Luís"],
        'femme': ["Ana", "Maria", "Josefa", "Luisa", "Teresa"]
    },
    'Mali': {
        'homme': ["Modibo", "Bakary", "Seydou", "Oumar", "Amadou"],
        'femme': ["Aïssata", "Kadiatou", "Djénéba", "Fatoumata", "Mariam"]
    },
    'Mauritanie': {
        'homme': ["Mohamed", "Ahmed", "Cheikh", "El Hacen", "Sid'Ahmed"],
        'femme': ["Aminata", "Fatimatou", "Mbarka", "Mariem", "Safi"]
    },
    'Royaume-Uni': {
        'homme': ["James", "John", "Robert", "Michael", "William"],
        'femme': ["Mary", "Patricia", "Jennifer", "Linda", "Elizabeth"]
    },
    'Allemagne': {
        'homme': ["Lukas", "Finn", "Jonas", "Leon", "Felix"],
        'femme': ["Sophie", "Marie", "Hannah", "Emilia", "Anna"]
    },
    'Italie': {
        'homme': ["Luca", "Matteo", "Leonardo", "Francesco", "Alessandro"],
        'femme': ["Sofia", "Giulia", "Aurora", "Alice", "Martina"]
    },
    'Espagne': {
        'homme': ["Hugo", "Daniel", "Pablo", "Alejandro", "Adrián"],
        'femme': ["Lucía", "Sofía", "Martina", "María", "Paula"]
    },
    'Portugal': {
        'homme': ["João", "Francisco", "Martim", "Santiago", "Afonso"],
        'femme': ["Maria", "Leonor", "Matilde", "Carolina", "Ana"]
    },
    'Pays-Bas': {
        'homme': ["Daan", "Sem", "Milan", "Levi", "Lucas"],
        'femme': ["Emma", "Tess", "Sophie", "Julia", "Anna"]
    },
    'Belgique': {
        'homme': ["Lucas", "Louis", "Nathan", "Liam", "Noah"],
        'femme': ["Emma", "Olivia", "Louise", "Mila", "Alice"]
    },
    'Suisse': {
        'homme': ["Liam", "Noah", "Elias", "Luca", "Levi"],
        'femme': ["Mia", "Emma", "Sofia", "Lena", "Lina"]
    },
    'Suède': {
        'homme': ["Lucas", "William", "Oscar", "Hugo", "Elias"],
        'femme': ["Alice", "Maja", "Lilly", "Ella", "Wilma"]
    },
    'Norvège': {
        'homme': ["Jakob", "Emil", "Noah", "Oliver", "William"],
        'femme': ["Emma", "Nora", "Olivia", "Sofie", "Emilie"]
    },
    'Danemark': {
        'homme': ["William", "Oscar", "Lucas", "Emil", "Oliver"],
        'femme': ["Emma", "Ida", "Clara", "Ella", "Sofia"]
    },
    'Finlande': {
        'homme': ["Elias", "Leo", "Eino", "Mikael", "Onni"],
        'femme': ["Aino", "Sofia", "Emilia", "Ella", "Olivia"]
    },
    'Grèce': {
        'homme': ["Giorgos", "Dimitris", "Kostas", "Nikos", "Yannis"],
        'femme': ["Maria", "Eleni", "Katerina", "Sophia", "Anna"]
    },
    'Pologne': {
        'homme': ["Jakub", "Jan", "Szymon", "Antoni", "Filip"],
        'femme': ["Zuzanna", "Julia", "Maja", "Hanna", "Aleksandra"]
    },
    'Ukraine': {
        'homme': ["Oleksandr", "Dmytro", "Andriy", "Yuriy", "Mykola"],
        'femme': ["Olena", "Natalia", "Svitlana", "Iryna", "Tetiana"]
    },
    'Russie': {
        'homme': ["Dmitry", "Alexey", "Sergey", "Ivan", "Vladimir"],
        'femme': ["Anna", "Olga", "Elena", "Maria", "Natalia"]
    },
    'Brésil': {
        'homme': ["Miguel", "Arthur", "Davi", "Gabriel", "Heitor"],
        'femme': ["Alice", "Sophia", "Laura", "Valentina", "Heloisa"]
    },
    'Argentine': {
        'homme': ["Santiago", "Mateo", "Juan", "Tomas", "Lucas"],
        'femme': ["Sofia", "Valentina", "Martina", "Luciana", "Emma"]
    },
    'Mexique': {
        'homme': ["Santiago", "Mateo", "Sebastián", "Leonardo", "Matías"],
        'femme': ["Sofía", "Valentina", "Regina", "Mariana", "Victoria"]
    },
    'Colombie': {
        'homme': ["Santiago", "Mateo", "Samuel", "Alejandro", "Daniel"],
        'femme': ["Sofía", "Valentina", "Isabella", "Mariana", "Gabriela"]
    },
    'Chili': {
        'homme': ["Agustín", "Benjamín", "Vicente", "Martín", "Matías"],
        'femme': ["Isabella", "Florencia", "Josefa", "Martina", "Emilia"]
    },
    'Pérou': {
        'homme': ["Sebastián", "Mateo", "Thiago", "Martín", "Daniel"],
        'femme': ["Camila", "María José", "Valentina", "Victoria", "Luciana"]
    },
    'Venezuela': {
        'homme': ["Santiago", "Mateo", "Gabriel", "Daniel", "Alejandro"],
        'femme': ["Sofía", "Valentina", "Camila", "Victoria", "Luciana"]
    },
    'Canada': {
        'homme': ["Liam", "Noah", "Jackson", "Lucas", "James"],
        'femme': ["Emma", "Olivia", "Sophia", "Charlotte", "Amelia"]
    },
    'États-Unis': {
        'homme': ["Liam", "Noah", "William", "James", "Logan"],
        'femme': ["Emma", "Olivia", "Ava", "Isabella", "Sophia"]
    },
    'Antilles Françaises': {
        'homme': ["Jean-Luc", "Pierre", "Michel", "Jacques", "Alain"],
        'femme': ["Marie", "Chantal", "Suzanne", "Monique", "Brigitte"]
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
    'Afrique du Sud': ["Dlamini", "Nkosi", "Zulu", "Ngcobo", "Khumalo"],
    'Vietnam': ["Nguyen", "Tran", "Le", "Pham", "Hoang"],
    'Cambodge': ["Sok", "Chea", "Chhim", "Pich", "Chann"],
    'Inde': ["Sharma", "Patel", "Reddy", "Singh", "Kumar"],
    'Pakistan': ["Hussain", "Butt", "Sheikh", "Malik", "Shah"],
    'Japon': ["Tanaka", "Suzuki", "Takahashi", "Sato", "Kobayashi"],
    'Corée du Sud': ["Kim", "Lee", "Park", "Choi", "Jung"],
    'Congo': ["Mbemba", "Ndombe", "Ngita", "Mukoko", "Yoka"],
    'Cameroun': ["Ndongo", "Ndomo", "Nji", "Biya", "Mbappe"],
    'Togo': ["Kodjo", "Afi", "Yawovi", "Ayélé", "Kossi"],
    'Ghana': ["Kwame", "Akosua", "Kofi", "Abena", "Yaw"],
    'Bénin': ["Agnidé", "Sèmèvo", "Dossou", "Koutché", "Houngbédji"],
    'Angola': ["Da Costa", "Mendosa", "De Oliveira", "Maria", "João"],
    'Mali': ["Modibo", "Aïssata", "Kadiatou", "Bakary", "Djénéba"],
    'Mauritanie': ["Mohamed", "Aminata", "El Hacen", "Mbarka", "Cheikh"],
    'Royaume-Uni': ["Smith", "Johnson", "Williams", "Jones", "Brown"],
    'Allemagne': ["Müller", "Schmidt", "Schneider", "Fischer", "Weber"],
    'Italie': ["Rossi", "Russo", "Ferrari", "Esposito", "Bianchi"],
    'Espagne': ["García", "Martínez", "López", "Sánchez", "Pérez"],
    'Portugal': ["Silva", "Santos", "Ferreira", "Pereira", "Oliveira"],
    'Pays-Bas': ["de Jong", "Jansen", "de Vries", "van den Berg", "Bakker"],
    'Belgique': ["Peeters", "Janssens", "Maes", "Jacobs", "Mertens"],
    'Suisse': ["Müller", "Meier", "Schmid", "Keller", "Weber"],
    'Suède': ["Johansson", "Andersson", "Karlsson", "Nilsson", "Eriksson"],
    'Norvège': ["Hansen", "Johansen", "Olsen", "Larsen", "Andersen"],
    'Danemark': ["Nielsen", "Jensen", "Hansen", "Pedersen", "Andersen"],
    'Finlande': ["Korhonen", "Virtanen", "Mäkinen", "Nieminen", "Mäkelä"],
    'Grèce': ["Papadopoulos", "Nikolaou", "Georgiou", "Christou", "Panagiotou"],
    'Pologne': ["Nowak", "Kowalski", "Wiśniewski", "Wójcik", "Kamiński"],
    'Ukraine': ["Shevchenko", "Kovalenko", "Bondarenko", "Tkachenko", "Kravchenko"],
    'Russie': ["Ivanov", "Smirnov", "Kuznetsov", "Popov", "Vasiliev"],
    'Brésil': ["Silva", "Santos", "Oliveira", "Souza", "Lima"],
    'Argentine': ["González", "Rodríguez", "Pérez", "Fernández", "Gómez"],
    'Mexique': ["Hernández", "García", "Martínez", "López", "González"],
    'Colombie': ["García", "Rodríguez", "Martínez", "López", "González"],
    'Chili': ["González", "Muñoz", "Rojas", "Díaz", "Pérez"],
    'Pérou': ["García", "Rodríguez", "Martínez", "López", "González"],
    'Venezuela': ["González", "Rodríguez", "Martínez", "López", "García"],
    'Canada': ["Smith", "Brown", "Tremblay", "Martin", "Roy"],
    'États-Unis': ["Smith", "Johnson", "Williams", "Jones", "Brown"],
    'Antilles Françaises': ["Durand", "Leroy", "Morel", "Simon", "Laurent"]
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
               'Université de Limoges', 'Université de Pau', 'Université de Perpignan',
               'Université Cheikh Anta Diop', 'Université de Ouagadougou', 'Université de Bamako',
               'Université de Kinshasa', 'Université de Brazzaville', 'Université de Libreville'],
    'Ingénieur': ['École Polytechnique', 'École Centrale Paris', 'École des Ponts ParisTech',
                  'École des Mines ParisTech', 'École Normale Supérieure', 'École Supérieure de Physique et de Chimie Industrielles',
                  'École Nationale des Ponts et Chaussées', 'École Nationale Supérieure des Mines de Saint-Étienne',
                  'CentraleSupélec', 'Conservation des Arts et Métiers', 'École Nationale Supérieure de Techniques Avancées'],
    'Doctorat': ['Université Paris-Saclay', 'Université de Lyon', 'Université de Marseille',
                 'Université de Montpellier', 'Université de Nantes', 'Université de Strasbourg',
                 'Université de Bordeaux', 'Université de Lille', 'Université de Toulouse']
}

# Langues avec poids ajustés
langues = [
    {'français': 'C2', 'anglais': 'B2', 'espagnol': 'B1'},
    {'français': 'C2', 'anglais': 'A2', 'allemand': 'B1'},
    {'français': 'C1', 'anglais': 'B2', 'italien': 'A2'},
    {'français': 'C2', 'anglais': 'C1', 'chinois': 'B2'},
    {'français': 'C2', 'arabe': 'C1', 'anglais': 'B1'},
    {'français': 'C2', 'lingala': 'B1', 'swahili': 'A2'},         # Modification prévue: langues directement dans pays et nationalités
    {'français': 'C2', 'wolof': 'B2', 'peul': 'B1'},              # pour une meilleure coherence
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

weights_langues = [8, 7, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 2, 2, 2, 2, 2]

# Sélection des langues parlées avec les poids
langues_parlees = random.choices(langues, weights=weights_langues, k=1)[0]

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
        "Gestion des réseaux sociaux et des relations publiques",
        "Rédaction d'articles et de communiqués de presse",
        "Organisation des événements médiatiques et des conférences de presse"
    ],
    'Manufacture': [
        "Supervision des opérations de production",
        "Contrôle de la qualité et respect des normes",
        "Gestion des équipes et répartition des tâches",
        "Optimisation des processus de production",
        "Maintenance des équipements et des machines"
    ],
    'Commerce': [
        "Gestion des stocks et des approvisionnements",
        "Négociation avec les fournisseurs et les partenaires",
        "Développement de la stratégie commerciale",
        "Analyse des ventes et des performances",
        "Organisation des promotions et des actions commerciales"
    ],
    'Hôtellerie': [
        "Accueil et prise en charge des clients",
        "Gestion des réservations et des check-ins/check-outs",
        "Coordination des équipes de service",
        "Supervision de l'entretien et de la propreté des chambres",
        "Organisation des événements et des séminaires"
    ],
    'Transport': [
        "Planification et optimisation des itinéraires",
        "Gestion des équipes de chauffeurs",
        "Suivi des livraisons et des expéditions",
        "Maintenance des véhicules et des équipements",
        "Respect des réglementations et des normes de sécurité"
    ],
    'Énergie': [
        "Gestion des projets de production énergétique",
        "Maintenance des infrastructures énergétiques",
        "Optimisation des processus de distribution",
        "Développement des énergies renouvelables",
        "Veille technologique et innovation dans le secteur énergétique"
    ],
    'Immobilier': [
        "Prospection et négociation des biens immobiliers",
        "Gestion des locations et des ventes",
        "Évaluation et estimation des biens",
        "Conseil et accompagnement des clients",
        "Suivi des projets de construction et de rénovation"
    ],
    'Télécommunications': [
        "Installation et maintenance des équipements télécom",
        "Gestion des réseaux et des infrastructures",
        "Développement des offres et des services télécom",
        "Support technique et assistance aux clients",
        "Veille technologique et innovation dans le secteur télécom"
    ],
    'Divertissement': [
        "Production et réalisation de contenus audiovisuels",
        "Organisation des événements et des spectacles",
        "Gestion des talents et des artistes",
        "Promotion et marketing des productions",
        "Collaboration avec les partenaires et les sponsors"
    ],
    'Sports': [
        "Entraînement et préparation physique des athlètes",
        "Organisation des compétitions et des événements sportifs",
        "Gestion des installations sportives",
        "Suivi médical et rééducation des sportifs",
        "Promotion et développement des activités sportives"
    ],
    'Science': [
        "Conduite des projets de recherche scientifique",
        "Analyse des données et publication des résultats",
        "Développement des protocoles expérimentaux",
        "Collaboration avec les institutions et les partenaires",
        "Veille scientifique et participation aux conférences"
    ],
    'Fonction publique': [
        "Gestion administrative et budgétaire",
        "Mise en œuvre des politiques publiques",
        "Service aux citoyens et gestion des demandes",
        "Coordination des équipes et des services",
        "Contrôle et suivi des projets publics"
    ],
    'Logistique': [
        "Planification et optimisation des flux logistiques",
        "Gestion des stocks et des entrepôts",
        "Suivi des expéditions et des livraisons",
        "Négociation avec les transporteurs et les fournisseurs",
        "Analyse des performances logistiques et amélioration continue"
    ],
    'Banque': [
        "Gestion des comptes et des portefeuilles clients",
        "Analyse financière et conseil en investissement",
        "Suivi des opérations bancaires et des transactions",
        "Développement des produits et services bancaires",
        "Gestion des risques et conformité réglementaire"
    ],
    'Assurance': [
        "Souscription des contrats d'assurance",
        "Gestion des sinistres et des indemnisations",
        "Analyse des risques et tarification",
        "Conseil et accompagnement des clients",
        "Développement des produits d'assurance"
    ],
    'Consulting': [
        "Audit et analyse des besoins des clients",
        "Développement des stratégies et des plans d'action",
        "Gestion des projets de transformation",
        "Formation et accompagnement des équipes",
        "Veille et innovation dans le secteur du consulting"
    ],
    'Ressources humaines': [
        "Recrutement et gestion des talents",
        "Formation et développement des compétences",
        "Gestion de la paie et des avantages sociaux",
        "Développement des politiques RH",
        "Gestion des conflits et des relations sociales"
    ],
    'Communication': [
        "Développement et mise en œuvre des stratégies de communication",
        "Gestion des relations publiques et des médias",
        "Création de contenus et gestion des réseaux sociaux",
        "Organisation des événements et des campagnes",
        "Analyse des performances et ajustements"
    ],
    'Maintenance': [
        "Planification et réalisation des opérations de maintenance",
        "Diagnostic et réparation des pannes",
        "Gestion des équipes de techniciens",
        "Optimisation des processus de maintenance",
        "Veille technologique et innovation dans la maintenance"
    ],
    'Sécurité': [
        "Gestion des systèmes de sécurité",
        "Surveillance et contrôle des accès",
        "Formation et sensibilisation à la sécurité",
        "Intervention en cas d'incident",
        "Veille et mise en conformité réglementaire"
    ],
    'Automobile': [
        "Conception et développement des véhicules",
        "Production et assemblage des pièces automobiles",
        "Maintenance et réparation des véhicules",
        "Gestion des stocks et des approvisionnements",
        "Commercialisation et vente des véhicules"
    ],
    'Mode': [
        "Création et design des collections",
        "Production et assemblage des pièces",
        "Gestion des stocks et des approvisionnements",
        "Commercialisation et vente des produits",
        "Promotion et marketing des collections"
    ],
    'Technique': [
        "Installation et maintenance des équipements",
        "Diagnostic et réparation des pannes",
        "Gestion des équipes de techniciens",
        "Optimisation des processus techniques",
        "Veille technologique et innovation dans le domaine technique"
    ],
    'Production': [
        "Planification et gestion de la production",
        "Supervision des équipes et des opérations",
        "Contrôle de la qualité et respect des normes",
        "Optimisation des processus de production",
        "Maintenance des équipements de production"
    ],
    'Agriculture': [
        "Gestion des cultures et des élevages",
        "Planification des récoltes et des productions",
        "Optimisation des processus agricoles",
        "Maintenance des équipements agricoles",
        "Commercialisation et vente des produits agricoles"
    ],
    'Art': [
        "Création et production des œuvres artistiques",
        "Organisation des expositions et des événements",
        "Promotion et commercialisation des œuvres",
        "Gestion des relations avec les galeristes et les collectionneurs",
        "Formation et animation des ateliers artistiques"
    ],
    'Design': [
        "Conception et développement des produits",
        "Création des maquettes et des prototypes",
        "Gestion des projets de design",
        "Optimisation des processus de production",
        "Veille et innovation dans le domaine du design"
    ],
    'Environnement': [
        "Gestion des projets de développement durable",
        "Analyse et réduction de l'empreinte carbone",
        "Gestion des déchets et des ressources",
        "Sensibilisation et formation aux enjeux environnementaux",
        "Veille et innovation dans le domaine environnemental"
    ],
    'Tourisme': [
        "Organisation et gestion des voyages",
        "Accueil et prise en charge des clients",
        "Promotion et commercialisation des destinations touristiques",
        "Gestion des réservations et des contrats",
        "Développement des produits et services touristiques"
    ],
    'Assistance': [
        "Gestion des appels et des agendas",
        "Organisation des déplacements et des réunions",
        "Accueil des visiteurs et gestion des courriers",
        "Support administratif et logistique",
        "Gestion des bases de données et des dossiers"
    ],
    'Social': [
        "Accompagnement des personnes en difficulté",
        "Organisation des activités et des ateliers",
        "Gestion des dossiers et des demandes d'aide",
        "Coordination avec les partenaires sociaux",
        "Sensibilisation et formation aux enjeux sociaux"
    ],
    'Événementiel': [
        "Organisation et gestion des événements",
        "Coordination des équipes et des prestataires",
        "Promotion et communication des événements",
        "Gestion des budgets et des plannings",
        "Suivi et évaluation des événements"
    ],
    'Manutention': [
        "Chargement et déchargement des marchandises",
        "Gestion des stocks et des entrepôts",
        "Maintenance des équipements de manutention",
        "Optimisation des processus de manutention",
        "Respect des normes de sécurité"
    ],
    'Défense': [
        "Gestion des opérations de défense",
        "Formation et entraînement des personnels",
        "Maintenance des équipements de défense",
        "Veille et gestion des risques",
        "Coordination avec les partenaires internationaux"
    ],
    'ONG': [
        "Gestion des projets humanitaires",
        "Coordination avec les partenaires locaux",
        "Gestion des équipes et des bénévoles",
        "Collecte de fonds et gestion des dons",
        "Sensibilisation et communication sur les enjeux humanitaires"
    ],
    'Industrie alimentaire': [
        "Production et transformation des produits alimentaires",
        "Contrôle de la qualité et respect des normes",
        "Gestion des stocks et des approvisionnements",
        "Optimisation des processus de production",
        "Maintenance des équipements de production"
    ],
    'Culture': [
        "Organisation et gestion des événements culturels",
        "Promotion et communication des événements",
        "Gestion des relations avec les artistes et les partenaires",
        "Suivi et évaluation des événements",
        "Veille et innovation dans le domaine culturel"
    ],
    'BTP': [
        "Gestion des projets de construction",
        "Coordination des équipes et des sous-traitants",
        "Contrôle de la qualité et respect des normes",
        "Optimisation des processus de construction",
        "Maintenance des équipements et des infrastructures"
    ],
    'Recherche': [
        "Conduite des projets de recherche",
        "Analyse des données et publication des résultats",
        "Développement des protocoles expérimentaux",
        "Collaboration avec les institutions et les partenaires",
        "Veille scientifique et participation aux conférences"
    ],
    'Aérospatial': [
        "Conception et développement des véhicules spatiaux",
        "Gestion des projets aérospatiaux",
        "Maintenance des équipements aérospatiaux",
        "Optimisation des processus de production",
        "Veille technologique et innovation dans le domaine aérospatial"
    ],
    'Technologie': [
        "Développement et maintenance des systèmes informatiques",
        "Gestion des bases de données et des infrastructures",
        "Sécurité et protection des données",
        "Veille technologique et innovation",
        "Support technique et assistance aux utilisateurs"
    ],
    'Innovation': [
        "Gestion des projets d'innovation",
        "Recherche et développement de nouvelles technologies",
        "Veille technologique et analyse des tendances",
        "Développement de prototypes et de maquettes",
        "Promotion et commercialisation des innovations"
    ],
    'Beauté': [
        'Conseil en soins de la peau et en maquillage',
        'Coupe et coiffure personnalisées',
        'Réalisation de manucures et de pédicures',
        'Soins du visage et massages relaxants',
        'Vente de produits de beauté',
        'Formation en techniques esthétiques',
        'Gestion des rendez-vous et des clients',
        'Développement de nouveaux traitements de beauté'
    ],
    'Restauration': [
        'Préparation et présentation des plats',
        'Gestion des commandes et des stocks',
        'Service en salle et accueil des clients',
        'Nettoyage et entretien de la cuisine',
        'Création de menus innovants',
        'Supervision de l\'équipe de cuisine',
        'Organisation d\'événements gastronomiques',
        'Application des normes d\'hygiène et de sécurité'
    ],
    'Sécurité': [
        'Surveillance des lieux et des accès',
        'Gestion des systèmes de sécurité',
        'Intervention en cas d\'urgence',
        'Rédaction de rapports de sécurité',
        'Formation des agents de sécurité',
        'Patrouilles régulières et gestion des incidents',
        'Contrôle des accès et des entrées',
        'Mise en place de protocoles de sécurité'
    ],
    'Innovation': [
        'Développement de nouvelles technologies',
        'Veille technologique et analyse des tendances',
        'Conception et test de prototypes',
        'Gestion de projets innovants',
        'Collaboration avec les équipes de recherche',
        'Test et validation des nouveaux produits',
        'Analyse des besoins du marché',
        'Rédaction et dépôt de brevets'
    ]
}

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
                     'Développement veille technologique','Python', 'Machine Learning', 'Deep Learning',
                     'Data Science', 'Data Engineering', 'Data Analysis', 'Data Mining', 'Data Warehousing',
                     'Data Modeling', 'Data Visualization', 'Business Intelligence', 'ETL', 'ELT', 'OLAP',
                     'OLTP', 'DWH', 'BI', 'Big Data', 'Hadoop', 'Spark', 'Flink', 'Kafka', 'Hive', 'Pig',
                     'Sqoop', 'Flume', 'HBase', 'Cassandra', 'MongoDB', 'Redis', 'MySQL', 'PostgreSQL'],
    'Santé': ['Soins infirmiers', 'Anatomie', 'Pharmacologie', 'Gestion des patients', 'Premiers secours', 
              'Soins intensifs', 'Soins palliatifs', 'Soins à domicile', 'Soins pédiatriques', 'Soins gériatriques',
              'Soins obstétriques', 'Soins psychiatriques', 'Soins chirurgicaux', 'Soins médicaux', 'Soins dentaires',
              'Soins ophtalmologiques', 'Soins ORL', 'Soins dermatologiques', 'Soins orthopédiques', 'Soins neurologiques',
              'Soins cardiovasculaires', 'Soins respiratoires', 'Soins oncologiques', 'Soins endocriniens', 'Soins urologiques',
              'Éducation thérapeutique', 'Gestion des dossiers médicaux', 'Utilisation des équipements médicaux', 'Connaissances en bioéthique', 'Soins d’urgence', 'Gestion des maladies chroniques'],
    'Finance': ['Comptabilité', 'Analyse financière', 'Gestion de trésorerie', 'Audit', 'Prévision financière',
                'Contrôle de gestion', 'Finance d\'entreprise', 'Finance de marché', 'Finance de projet', 'Finance internationale',
                'Gestion des risques financiers', 'Modélisation financière', 'Fusions et acquisitions', 'Gestion d’actifs', 'Gestion de portefeuille',
                'Compliance financière', 'Fiscalité', 'Reporting financier', 'Analyse de crédit', 'Banque d’investissement'],
    'Éducation': ['Pédagogie', 'Gestion de classe', 'Planification de cours', 'Évaluation', 'Didactique',
                  'Technologies éducatives', 'Formation continue', 'Orientation scolaire', 
                  'Conseil pédagogique', 'Recherche en éducation', 'Développement de programmes éducatifs', 'Gestion des comportements',
                  'Accompagnement des élèves à besoins particuliers', 'Création de supports pédagogiques', 'Utilisation des plateformes d’apprentissage en ligne',
                  'Coordination pédagogique', 'Mentorat et tutorat', 'Animation d’ateliers'],
    'Ingénierie': ['AutoCAD', 'MATLAB', 'Gestion de projet', 'Conception', 'Modélisation 3D',
                   'Calculs de structures', 'Calculs thermiques', 'Calculs électriques', 'Calculs hydrauliques',
                   'Calculs mécaniques', 'Calculs aérodynamiques', 'Calculs acoustiques', 'Calculs optiques',
                   'Calculs électromagnétiques', 'Calculs quantiques', 'Calculs statistiques', 'Calculs probabilistes',
                   'Solidworks', 'Catia', 'NX', 'Creo', 'Inventor', 'Revit', 'RobotStudio', 'TIA Portal',
                   'Fusion 360', 'Creality', 'Ultimaker', 'Prusa', 'Ansys', 'Abaqus', 'Comsol', 'StarCCM+',
                   'Ingénierie des matériaux', 'Thermodynamique', 'Énergie renouvelable', 'Ingénierie de l’environnement',
                   'Mécatronique', 'Contrôle des systèmes', 'Robotiques', 'Gestion de la qualité', 'Lean Manufacturing',
                   'Six Sigma', 'Gestion des coûts', 'Gestion des risques', 'Planification et ordonnancement de la production'],
    'Marketing': ['SEO', 'Publicité', 'Analyse de marché', 'Stratégie de marque', 'Réseaux sociaux', 
                  'Marketing digital', 'Marketing de contenu', 'Marketing viral', 'Marketing relationnel',
                  'Marketing événementiel', 'Marketing direct', 'Marketing de proximité', 'Marketing de masse',
                  'CRM', 'Publicité en ligne', 'Email marketing', 'Analytics', 'Google Analytics', 'Google Ads',
                  'Facebook Ads', 'Content Management System (CMS)', 'Automatisation du marketing', 'Influence marketing',
                  'Branding', 'Gestion de la réputation en ligne', 'Segmentation du marché', 'Optimisation des taux de conversion (CRO)',
                  'Création de campagnes marketing', 'Planification des médias'],
    'Ventes': ['Négociation', 'Gestion des comptes', 'Service à la clientèle', 'Prospection', 'CRM',
               'Vente B2B', 'Vente B2C', 'Vente en ligne', 'Vente en magasin', 'Vente par téléphone',
               'Techniques de closing', 'Stratégie de vente', 'Analyse des performances de vente', 'Gestion des objections',
               'Formation des équipes de vente', 'Développement des relations clients', 'Techniques de présentation',
               'Gestion des ventes complexes', 'Vente consultative', 'Développement des affaires', 'Suivi après-vente'],
    'Droit': ['Droit des affaires', 'Droit pénal', 'Rédaction de contrats', 'Conseil juridique', 'Plaidoyer',
              'Droit du travail', 'Droit de la famille', 'Droit des sociétés', 'Droit fiscal', 'Droit immobilier',
              'Droit international', 'Droit commercial', 'Droit de la propriété intellectuelle', 'Droit des nouvelles technologies',
              'Droit de l’environnement', 'Droit de la consommation', 'Contentieux', 'Médiation', 'Arbitrage',
              'Droit des assurances', 'Compliance', 'Rédaction de mémoires', 'Analyse juridique', 'Veille juridique'],
    'Média': ['Montage vidéo', 'Journalisme', 'Photographie', 'Rédaction', 'Gestion des réseaux sociaux',
              'Production audiovisuelle', 'Animation', 'Infographie', 'Édition', 'Révision de contenu',
              'Techniques de reportage', 'Écriture de scripts', 'SEO pour les médias', 'Gestion de communauté',
              'Relations publiques', 'Gestion de projet médiatique', 'Marketing des médias', 'Planification éditoriale',
              'Conception sonore', 'Réalisation de documentaires'],
    'Manufacture': ['Supervision', 'Maintenance', 'Qualité', 'Production', 'Planification',
                    'Gestion de la chaîne logistique', 'Contrôle des stocks', 'Automatisation des processus',
                    'Lean Manufacturing', 'Six Sigma', 'Gestion des opérations', 'Sécurité industrielle',
                    'Gestion des flux de production', 'Planification des capacités', 'Optimisation des processus',
                    'Maintenance prédictive', 'Contrôle statistique des processus (SPC)', 'Gestion des ressources humaines',
                    'Implantation des équipements', 'Gestion des coûts de production'],
    'Commerce': ['Gestion de stock', 'Relation client', 'Stratégie de vente', 'Merchandising', 'Logistique',
                 'Gestion des achats', 'Négociation avec les fournisseurs', 'Analyse des ventes', 'Gestion de la chaîne d’approvisionnement',
                 'E-commerce', 'Marketing de détail', 'Service après-vente', 'Organisation des promotions', 'Planification des ventes',
                 'Gestion des inventaires', 'Optimisation des processus de vente', 'Analyse des données de vente',
                 'Développement des relations clients', 'Prévisions des ventes', 'Techniques de vente'],
    'Hôtellerie': ['Accueil', 'Service en salle', 'Service en chambre', 'Service en cuisine', 'Service en bar',
                   'Gestion des réservations', 'Gestion des plaintes clients', 'Coordination des événements',
                   'Gestion de la réception', 'Supervision du personnel', 'Hygiène et sécurité alimentaire',
                   'Organisation des conférences et banquets', 'Gestion des coûts', 'Marketing hôtelier',
                   'Relation avec les clients VIP', 'Gestion des opérations hôtelières', 'Techniques de vente et de promotion',
                   'Gestion des équipements hôteliers', 'Maintenance des installations', 'Service de conciergerie'],
    'Transport': ['Logistique', 'Gestion de flotte', 'Conduite', 'Maintenance', 'Sécurité',
                  'Planification des itinéraires', 'Optimisation des coûts de transport', 'Gestion des stocks',
                  'Réglementation du transport', 'Gestion des expéditions', 'Coordination des livraisons',
                  'Suivi des performances de livraison', 'Service à la clientèle', 'Gestion des opérations de transport',
                  'Transport international', 'Gestion des entrepôts', 'Gestion des documents de transport',
                  'Technologies de l’information pour la logistique', 'Contrôle des coûts', 'Gestion des contrats de transport'],
    'Énergie': ['Production', 'Distribution', 'Renouvelable', 'Nucléaire', 'Pétrole',
                'Gestion des réseaux électriques', 'Énergie éolienne', 'Énergie solaire', 'Énergie hydroélectrique',
                'Gestion de la demande énergétique', 'Maintenance des infrastructures énergétiques', 'Réglementation énergétique',
                'Optimisation des ressources énergétiques', 'Audit énergétique', 'Conception des systèmes énergétiques',
                'Économie de l’énergie', 'Planification énergétique', 'Technologies des smart grids',
                'Sécurité des installations énergétiques', 'Stockage de l’énergie', 'Innovation énergétique'],
    'Immobilier': ['Transaction', 'Location', 'Gestion', 'Promotion', 'Construction',
                   'Estimation immobilière', 'Négociation immobilière', 'Droit immobilier', 'Gestion de patrimoine',
                   'Commercialisation de biens', 'Gestion de copropriété', 'Prospection foncière', 'Marketing immobilier',
                   'Financement immobilier', 'Gestion des baux', 'Gestion des relations clients', 'Aménagement du territoire',
                   'Développement immobilier', 'Gestion des projets immobiliers', 'Évaluation des risques immobiliers'],
    'Télécommunications': ['Réseaux', 'Téléphonie', 'Fibre', 'Satellite', 'Mobile',
                           'Sécurité des réseaux', 'Gestion des infrastructures télécom', 'Réglementation des télécommunications',
                           'Maintenance des équipements télécom', 'Conception des réseaux', 'Technologies 5G', 'Internet des objets (IoT)',
                           'Gestion des services télécom', 'Développement des offres télécom', 'Gestion de la bande passante',
                           'Optimisation des réseaux', 'Supervision des réseaux', 'Gestion des clients télécom', 'Innovation télécom',
                           'Communication unifiée', 'Téléphonie IP', 'Gestion des projets télécom', 'Déploiement des réseaux'],
    'Divertissement': ['Animation', 'Musique', 'Théâtre', 'Cirque', 'Cinéma',
                       'Production audiovisuelle', 'Gestion de projets culturels', 'Organisation de spectacles',
                       'Gestion des droits d’auteur', 'Marketing des arts', 'Réalisation de films', 'Scénarisation',
                       'Design sonore', 'Organisation d’événements', 'Gestion des équipements de scène', 'Technologies du spectacle',
                       'Création de contenus', 'Gestion de la billetterie', 'Promotion des artistes', 'Relations publiques pour les arts'],
    'Sports': ['Entraînement', 'Arbitrage', 'Compétition', 'Organisation', 'Santé',
               'Préparation physique', 'Coaching sportif', 'Gestion des installations sportives', 'Planification des entraînements',
               'Gestion des événements sportifs', 'Nutrition sportive', 'Récupération et rééducation des sportifs',
               'Analyse de la performance', 'Gestion des équipes sportives', 'Marketing sportif', 'Psychologie du sport',
               'Médias sportifs', 'Gestion des talents sportifs', 'Évaluation des capacités physiques',
               'Organisation des compétitions', 'Gestion des sponsors'],
    'Science': ['Recherche', 'Expérimentation', 'Analyse', 'Publication', 'Enseignement',
                'Gestion de projets de recherche', 'Rédaction de protocoles de recherche', 'Collecte et traitement des données',
                'Statistiques scientifiques', 'Rédaction d’articles scientifiques', 'Présentations scientifiques',
                'Collaboration interdisciplinaire', 'Gestion des laboratoires', 'Éthique de la recherche', 'Développement de nouvelles technologies',
                'Brevetage', 'Innovation scientifique', 'Gestion des financements de recherche', 'Formation scientifique',
                'Réalisation d’études cliniques', 'Utilisation des équipements de laboratoire', 'Analyse des résultats de recherche'],
    'Fonction publique': ['Administration', 'Service', 'Sécurité', 'Justice', 'Éducation', 'Santé',
                          'Gestion des ressources publiques', 'Droit public', 'Politiques publiques', 'Gestion des budgets publics',
                          'Communication publique', 'Gestion des crises', 'Relations internationales', 'Gestion des infrastructures publiques',
                          'Gestion des ressources humaines publiques', 'Planification urbaine', 'Protection de l’environnement public',
                          'Médiation sociale', 'Sécurité publique', 'Gestion des services sociaux', 'Gestion des transports publics'],
    'Logistique': ['Gestion de stock', 'Transport', 'Distribution', 'Approvisionnement', 'Manutention',
                   'Gestion des entrepôts', 'Planification logistique', 'Optimisation des flux logistiques', 'Gestion des inventaires',
                   'Gestion des fournisseurs', 'Suivi des expéditions', 'Réglementation du transport', 'Sécurité logistique',
                   'Analyse des performances logistiques', 'Gestion des retours', 'Gestion des coûts logistiques', 'Transport international',
                   'Technologies de l’information pour la logistique', 'Gestion des risques logistiques', 'Coordination des opérations logistiques',
                   'Élaboration des plans logistiques', 'Supervision des équipes logistiques'],
    'Banque': ['Gestion de compte', 'Crédit', 'Assurance', 'Placements', 'Conseil',
               'Gestion des risques bancaires', 'Analyse financière', 'Services bancaires aux particuliers', 'Services bancaires aux entreprises',
               'Gestion des portefeuilles', 'Fusions et acquisitions', 'Banque d’investissement', 'Conformité réglementaire',
               'Audit interne', 'Gestion de la trésorerie', 'Crédits hypothécaires', 'Crédits à la consommation', 'Crédits commerciaux',
               'Analyse des crédits', 'Gestion des actifs', 'Gestion des liquidités', 'Banque digitale'],
    'Assurance': ['Assurance vie', 'Assurance auto', 'Assurance habitation', 'Assurance santé', 'Assurance voyage',
                  'Gestion des risques assurantiels', 'Souscription des polices d’assurance', 'Gestion des sinistres', 'Évaluation des risques',
                  'Assurance responsabilité civile', 'Assurance des biens', 'Assurance des personnes', 'Assurance des entreprises',
                  'Assurance maritime', 'Assurance aviation', 'Assurance agricole', 'Assurance construction', 'Assurance professionnelle',
                  'Gestion des réclamations', 'Audit des assurances', 'Conformité réglementaire', 'Développement de produits d’assurance'],
    'Consulting': ['Conseil', 'Audit', 'Stratégie', 'Transformation', 'Formation',
                   'Gestion de projet', 'Gestion du changement', 'Gestion de la performance', 'Analyse des processus', 'Optimisation des processus',
                   'Gestion des risques', 'Gestion de la qualité', 'Conseil en innovation', 'Conseil en management', 'Conseil en organisation',
                   'Conseil en stratégie d’entreprise', 'Conseil en ressources humaines', 'Conseil en technologie', 'Conseil en développement durable',
                   'Accompagnement à la transformation digitale', 'Benchmarking', 'Conseil en marketing', 'Conseil en vente'],
    'Ressources humaines': ['Recrutement', 'Formation', 'Gestion de carrière', 'Gestion de paie', 'Gestion des conflits',
                            'Développement organisationnel', 'Gestion de la performance', 'Gestion des talents', 'Relations de travail',
                            'Gestion des avantages sociaux', 'Planification des ressources humaines', 'Droit du travail', 'Santé et sécurité au travail',
                            'Gestion des relations syndicales', 'Gestion des effectifs', 'Gestion des compétences', 'Développement des compétences',
                            'Gestion des programmes de reconnaissance', 'Médiation', 'Gestion de la diversité', 'Gestion des expatriés'],
    'Communication': ['Relations publiques', 'Communication interne', 'Communication externe', 'Communication digitale', 'Communication événementielle',
                      'Rédaction de communiqués de presse', 'Gestion des médias', 'Gestion de crise', 'Gestion de la réputation', 'Stratégie de communication',
                      'Relations institutionnelles', 'Community management', 'Création de contenu', 'Planification de la communication', 'Organisation d’événements',
                      'Veille médiatique', 'Gestion des réseaux sociaux', 'Rédaction de discours', 'Édition de newsletters', 'Communication corporate'],
    'Maintenance': ['Maintenance préventive', 'Maintenance curative', 'Maintenance corrective', 'Maintenance prédictive', 'Maintenance conditionnelle',
                    'Gestion des équipements', 'Gestion de la maintenance assistée par ordinateur (GMAO)', 'Planification de la maintenance', 'Gestion des stocks de pièces détachées',
                    'Diagnostic des pannes', 'Supervision des équipes de maintenance', 'Sécurité des installations', 'Formation des techniciens de maintenance',
                    'Optimisation des processus de maintenance', 'Gestion des contrats de maintenance', 'Maintenance industrielle', 'Maintenance des bâtiments',
                    'Maintenance des infrastructures', 'Audit de maintenance', 'Amélioration continue de la maintenance'],
    'Sécurité': ['Sécurité des biens', 'Sécurité des personnes', 'Sécurité incendie', 'Sécurité informatique', 'Sécurité des données',
                 'Gestion des risques', 'Surveillance', 'Gestion des accès', 'Protection rapprochée', 'Sécurité électronique',
                 'Planification de la sécurité', 'Intervention en cas de crise', 'Formation à la sécurité', 'Rédaction de plans de sécurité',
                 'Contrôle des installations de sécurité', 'Gestion des incidents de sécurité', 'Conformité aux normes de sécurité', 'Prévention des risques',
                 'Sécurité des événements', 'Cyber-sécurité', 'Analyse des risques sécuritaires', 'Gestion des systèmes d’alarme', 'Réalisation d’audits de sécurité'],
    'Automobile': ['Conception', 'Production', 'Maintenance', 'Vente', 'Réparation',
                   'Diagnostic des pannes automobiles', 'Mécanique automobile', 'Électronique automobile', 'Carrosserie', 'Peinture automobile',
                   'Gestion des stocks de pièces détachées', 'Technologies de l’automobile', 'Contrôle qualité des véhicules', 'Réalisation des contrôles techniques',
                   'Vente de véhicules neufs', 'Vente de véhicules d’occasion', 'Service après-vente automobile', 'Maintenance préventive des véhicules',
                   'Gestion des garanties', 'Gestion des réclamations clients', 'Optimisation des processus de production automobile', 'Gestion des équipes de production'],
    'Mode': ['Design', 'Stylisme', 'Couture', 'Modélisme', 'Marketing',
             'Gestion de collection', 'Achats de mode', 'Communication de mode', 'Gestion des événements de mode', 'Commercialisation des produits de mode',
             'Merchandising visuel', 'Analyse des tendances de mode', 'Développement de produits de mode', 'Gestion de la production de mode',
             'Négociation avec les fournisseurs de mode', 'Élaboration des prototypes de mode', 'Gestion des relations avec les créateurs de mode', 'Gestion de la chaîne d’approvisionnement en mode',
             'Organisation de défilés de mode', 'Photographie de mode', 'Rédaction pour les médias de mode', 'Création de moodboards', 'Gestion des réseaux sociaux de mode'],
    'Technique': ['Électricité', 'Mécanique', 'Plomberie', 'Menuiserie', 'Soudure',
                  'Maintenance des équipements techniques', 'Installation de systèmes techniques', 'Diagnostic des pannes techniques', 'Réalisation des schémas techniques',
                  'Gestion des chantiers techniques', 'Conformité aux normes techniques', 'Optimisation des processus techniques', 'Supervision des équipes techniques',
                  'Gestion des stocks de pièces techniques', 'Formation des techniciens', 'Sécurité des installations techniques', 'Gestion des projets techniques',
                  'Programmation des automates', 'Contrôle des installations techniques', 'Réalisation des essais techniques', 'Gestion des contrats de maintenance technique'],
    'Production': ['Fabrication', 'Assemblage', 'Conditionnement', 'Contrôle qualité', 'Logistique',
                   'Optimisation des processus de production', 'Gestion des stocks de matières premières', 'Planification de la production', 'Gestion des flux de production',
                   'Maintenance des équipements de production', 'Gestion des équipes de production', 'Sécurité industrielle', 'Analyse des performances de production',
                   'Gestion des coûts de production', 'Lean Manufacturing', 'Six Sigma', 'Amélioration continue de la production', 'Conformité aux normes de production',
                   'Automatisation des processus de production', 'Gestion des déchets de production', 'Formation des opérateurs de production', 'Supervision des lignes de production'],
    'Agriculture': ['Culture', 'Élevage', 'Pêche', 'Sylviculture', 'Agroalimentaire',
                    'Gestion des exploitations agricoles', 'Utilisation des équipements agricoles', 'Gestion des cultures agricoles', 'Élevage des animaux de ferme',
                    'Gestion des stocks de produits agricoles', 'Transformation des produits agricoles', 'Commercialisation des produits agricoles', 'Analyse des sols agricoles',
                    'Gestion des ressources en eau pour l’agriculture', 'Planification des récoltes', 'Gestion des maladies des cultures', 'Innovation agricole',
                    'Agriculture biologique', 'Utilisation des technologies agricoles', 'Gestion des déchets agricoles', 'Conformité aux normes agricoles',
                    'Gestion des subventions agricoles', 'Optimisation des rendements agricoles', 'Formation des agriculteurs', 'Développement des pratiques agricoles durables'],
    'Art': ['Peinture', 'Sculpture', 'Photographie', 'Dessin', 'Cinéma',
            'Histoire de l’art', 'Critique d’art', 'Conservation des œuvres d’art', 'Curatelle', 'Gestion des galeries d’art',
            'Organisation des expositions d’art', 'Restauration des œuvres d’art', 'Évaluation des œuvres d’art', 'Commercialisation des œuvres d’art',
            'Communication pour les artistes', 'Création de catalogues d’art', 'Gestion des collections d’art', 'Création de portfolios artistiques',
            'Développement des compétences artistiques', 'Animation des ateliers d’art', 'Médiation culturelle', 'Promotion des artistes', 'Formation artistique',
            'Gestion des contrats artistiques', 'Négociation avec les collectionneurs', 'Analyse des tendances artistiques', 'Réalisation des projets artistiques'],
    'Design': ['Graphisme', 'Web design', 'Design industriel', 'Design d\'intérieur', 'Design de mode',
               'Illustration', 'Création de logos', 'Typographie', 'Animation graphique', 'Création de sites web',
               'UX/UI design', 'Conception de produits', 'Prototypage', 'Conception de packaging', 'Design interactif',
               'Design d’expérience utilisateur', 'Création de wireframes', 'Création de maquettes', 'Impression 3D',
               'Design d’espace', 'Design environnemental', 'Infographie', 'Réalité augmentée', 'Réalité virtuelle',
               'Gestion des projets de design', 'Création d’identités visuelles', 'Design thinking', 'Utilisation des logiciels de design (Photoshop, Illustrator, InDesign)'],
    'Environnement': ['Écologie', 'Développement durable', 'Gestion des déchets', 'Énergies renouvelables', 'Biodiversité',
                      'Analyse environnementale', 'Audit environnemental', 'Gestion des ressources naturelles', 'Gestion de l’eau',
                      'Gestion de l’air', 'Gestion des sols', 'Planification environnementale', 'Gestion des risques environnementaux',
                      'Éducation à l’environnement', 'Gestion des espaces naturels', 'Protection de la faune et de la flore',
                      'Gestion des projets environnementaux', 'Conformité aux réglementations environnementales', 'Évaluation de l’impact environnemental',
                      'Gestion des émissions de gaz à effet de serre', 'Gestion des zones protégées', 'Conservation des habitats naturels',
                      'Restauration écologique', 'Utilisation des technologies environnementales', 'Gestion des catastrophes naturelles'],
    'Tourisme': ['Hôtellerie', 'Restauration', 'Guidage', 'Animation', 'Transport',
                 'Gestion des agences de voyage', 'Organisation des circuits touristiques', 'Marketing touristique',
                 'Gestion des réservations de voyages', 'Gestion des événements touristiques', 'Gestion des relations clients dans le tourisme',
                 'Gestion des équipements touristiques', 'Optimisation des itinéraires touristiques', 'Développement des produits touristiques',
                 'Planification des voyages', 'Analyse des tendances touristiques', 'Gestion des services touristiques', 'Réglementation touristique',
                 'Promotion des destinations touristiques', 'Gestion des contrats touristiques', 'Écotourisme', 'Tourisme durable', 'Animation des groupes touristiques'],
    'Assistance': ['Secrétariat', 'Accueil', 'Gestion des appels', 'Gestion des agendas', 'Organisation des déplacements',
                   'Gestion des courriers', 'Gestion des fournitures de bureau', 'Rédaction de comptes-rendus', 'Classement des documents',
                   'Préparation des réunions', 'Gestion des bases de données', 'Gestion des archives', 'Gestion des notes de frais',
                   'Gestion des commandes', 'Gestion des plannings', 'Gestion des réclamations', 'Gestion des dossiers clients',
                   'Gestion des réservations', 'Gestion des stocks', 'Gestion des contrats', 'Gestion des factures', 'Gestion des paiements',
                   'Gestion des litiges', 'Gestion des relations clients', 'Gestion des réseaux sociaux', 'Gestion des bases de données clients'],
    'Social': ['Travail social', 'Aide à la personne', 'Médiation', 'Insertion', 'Accompagnement',
               'Gestion des conflits', 'Gestion des situations d’urgence', 'Écoute active', 'Conseil social', 'Médiation familiale',
               'Aide à l’insertion professionnelle', 'Aide à l’autonomie', 'Aide à la parentalité', 'Aide aux personnes âgées', 'Aide aux personnes handicapées',
               'Aide aux personnes en difficulté', 'Aide aux migrants', 'Aide aux sans-abri', 'Aide aux victimes', 'Aide aux détenus',
               'Aide aux réfugiés', 'Aide aux personnes en situation de précarité', 'Aide aux personnes en situation de handicap', 'Aide aux personnes en situation d’exclusion'],
    'Événementiel': ['Organisation', 'Coordination', 'Logistique', 'Communication', 'Animation',
                     'Gestion des événements professionnels', 'Gestion des événements culturels', 'Gestion des événements sportifs', 'Gestion des événements artistiques', 'Gestion des événements caritatifs',
                     'Gestion des événements d’entreprise', 'Gestion des événements publics', 'Gestion des événements privés', 'Gestion des événements festifs', 'Gestion des événements institutionnels',
                     'Gestion des événements politiques', 'Gestion des événements musicaux', 'Gestion des événements gastronomiques', 'Gestion des événements touristiques', 'Gestion des événements de mode',
                     'Gestion des événements de luxe', 'Gestion des événements numériques', 'Gestion des événements virtuels', 'Gestion des événements hybrides', 'Gestion des événements en ligne'],
    'Manutention': ['Chargement', 'Déchargement', 'Tri', 'Stockage', 'Conditionnement',
                    'Gestion des stocks', 'Préparation de commandes', 'Manutention de marchandises', 'Manutention de colis', 'Manutention de palettes',
                    'Manutention de containers', 'Manutention de matériaux lourds', 'Manutention de produits chimiques', 'Manutention de produits dangereux',
                    'Manutention de produits fragiles', 'Manutention de produits périssables', 'Manutention de produits pharmaceutiques', 'Manutention de produits électroniques',
                    'Manutention de produits alimentaires', 'Manutention de produits finis', 'Manutention de produits semi-finis', 'Manutention de produits en vrac'],
    'Défense': ['Armée', 'Gendarmerie', 'Police', 'Sécurité', 'Défense nationale',
                'Gestion des opérations militaires', 'Gestion des ressources militaires', 'Gestion des effectifs militaires', 'Gestion des équipements militaires', 'Gestion des bases militaires',
                'Gestion des missions de défense', 'Gestion des missions de sécurité', 'Gestion des missions de secours', 'Gestion des missions de protection', 'Gestion des missions de surveillance',
                'Gestion des missions de renseignement', 'Gestion des missions de maintien de l’ordre', 'Gestion des missions d’intervention', 'Gestion des missions de sauvetage', 'Gestion des missions de formation', 'Gestion des missions de prévention', 'Gestion des missions de lute contre le terrorisme', 'Gestion des missions de lute contre la criminalité'],
    'ONG': ['Humanitaire', 'Environnement', 'Santé', 'Éducation', 'Développement',
            'Gestion de projets humanitaires', 'Gestion de projets environnementaux', 'Gestion de projets de santé', 'Gestion de projets éducatifs', 'Gestion de projets de développement',
            'Gestion des ressources humanitaires', 'Gestion des ressources environnementales', 'Gestion des ressources sanitaires', 'Gestion des ressources éducatives', 'Gestion des ressources de développement',
            'Gestion des missions humanitaires', 'Gestion des missions environnementales', 'Gestion des missions de santé', 'Gestion des missions éducatives', 'Gestion des missions de développement',
            'Gestion des bénévoles', 'Gestion des partenariats', 'Gestion des financements', 'Gestion des dons', 'Gestion des subventions',
            'Gestion des événements humanitaires', 'Gestion des événements environnementaux', 'Gestion des événements de santé', 'Gestion des événements éducatifs', 'Gestion des événements de développement'],
    'Industrie alimentaire': ['Production', 'Transformation', 'Conditionnement', 'Distribution', 'Qualité',
                              'Gestion des stocks de matières premières', 'Gestion des stocks de produits finis', 'Planification de la production', 'Optimisation des processus de production', 'Gestion des flux de production',
                              'Maintenance des équipements de production', 'Contrôle qualité des produits alimentaires', 'Gestion des équipes de production', 'Sécurité alimentaire', 'Hygiène alimentaire',
                              'Conformité aux normes alimentaires', 'Gestion des certifications alimentaires', 'Gestion des audits alimentaires', 'Gestion des risques alimentaires', 'Gestion des allergènes',
                              'Gestion des déchets alimentaires', 'Gestion des coûts de production alimentaire', 'Gestion des fournisseurs alimentaires', 'Gestion des clients alimentaires', 'Gestion des partenariats alimentaires',
                              'Gestion des labels alimentaires', 'Gestion des emballages alimentaires', 'Gestion des recettes alimentaires', 'Gestion des menus alimentaires', 'Gestion des régimes alimentaires'],
    'Culture': ['Musique', 'Danse', 'Théâtre', 'Cinéma', 'Littérature',
                'Gestion des spectacles', 'Gestion des concerts', 'Gestion des festivals', 'Gestion des tournées', 'Gestion des expositions',
                'Gestion des événements culturels', 'Gestion des événements artistiques', 'Gestion des événements musicaux', 'Gestion des événements théâtraux', 'Gestion des événements cinématographiques',
                'Gestion des événements littéraires', 'Gestion des événements numériques', 'Gestion des événements virtuels', 'Gestion des événements hybrides', 'Gestion des événements en ligne',
                'Gestion des artistes', 'Gestion des créateurs', 'Gestion des interprètes', 'Gestion des auteurs', 'Gestion des réalisateurs',
                'Gestion des scénaristes', 'Gestion des compositeurs', 'Gestion des chorégraphes', 'Gestion des metteurs en scène', 'Gestion des producteurs'],
    'BTP': ['Construction', 'Travaux publics', 'Génie civil', 'Aménagement', 'Rénovation',
            'Gestion de chantier', 'Planification des travaux', 'Coordination des équipes', 'Gestion des sous-traitants', 'Gestion des fournisseurs',
            'Gestion des approvisionnements', 'Gestion des délais', 'Gestion des coûts', 'Gestion des risques', 'Gestion des litiges',
            'Sécurité sur les chantiers', 'Hygiène sur les chantiers', 'Qualité des travaux', 'Respect des normes', 'Respect des réglementations',
            'Respect des normes environnementales', 'Respect des normes de sécurité', 'Respect des normes de qualité', 'Respect des normes de durabilité', 'Respect des normes de performance',
            'Respect des normes de fiabilité', 'Respect des normes de solidité', 'Respect des normes de résistance', 'Respect des normes de stabilité', 'Respect des normes de durée de vie'],
    'Recherche': ['Recherche scientifique', 'Recherche médicale', 'Recherche technologique', 'Recherche sociale', 'Recherche économique',
                  'Gestion de projets de recherche', 'Rédaction de protocoles de recherche', 'Collecte et traitement des données', 'Statistiques scientifiques', 'Rédaction d’articles scientifiques',
                  'Présentations scientifiques', 'Collaboration interdisciplinaire', 'Gestion des laboratoires', 'Éthique de la recherche', 'Développement de nouvelles technologies',
                  'Brevetage', 'Innovation scientifique', 'Gestion des financements de recherche', 'Formation scientifique', 'Réalisation d’études cliniques',
                  'Utilisation des équipements de laboratoire', 'Analyse des résultats de recherche', 'Recherche fondamentale', 'Recherche appliquée', 'Recherche expérimentale'],
    'Aérospatial': ['Conception', 'Production', 'Maintenance', 'Essais', 'Navigation',
                    'Gestion de projets aérospatiaux', 'Gestion des ressources aérospatiales', 'Gestion des équipements aérospatiaux', 'Gestion des missions aérospatiales', 'Gestion des vols spatiaux',
                    'Gestion des opérations aérospatiales', 'Gestion des lancements spatiaux', 'Gestion des satellites', 'Gestion des stations spatiales', 'Gestion des bases spatiales',
                    'Gestion des missions lunaires', 'Gestion des missions martiennes', 'Gestion des missions interplanétaires', 'Gestion des missions interstellaires', 'Gestion des missions intergalactiques',
                    'Gestion des missions d’exploration', 'Gestion des missions de recherche', 'Gestion des missions de surveillance', 'Gestion des missions de défense', 'Gestion des missions de sécurité']
}

# Liste de noms d'entreprises classées par domaine
entreprises = {
    'Informatique': ['Google', 'Microsoft', 'IBM', 'Capgemini', 'Atos', 'SAP', 'Apple', 'Oracle', 'Dell', 'Intel'],
    'Santé': ['Sanofi', 'Pfizer', 'Roche', 'Novartis', 'GSK', 'Johnson & Johnson', 'Merck', 'AstraZeneca', 'AbbVie', 'Bristol-Myers Squibb'],
    'Finance': ['BNP Paribas', 'Société Générale', 'Crédit Agricole', 'HSBC', 'AXA', 'Goldman Sachs', 'JP Morgan', 'Morgan Stanley', 'Deutsche Bank', 'UBS'],
    'Éducation': ['Acadomia', 'Khan Academy', 'Coursera', 'OpenClassrooms', 'Éducation Nationale', 'Udemy', 'edX', 'FutureLearn', 'Skillshare', 'LinkedIn Learning'],
    'Ingénierie': ['Dassault Systèmes', 'Schneider Electric', 'Thales', 'Alstom', 'Bouygues', 'Siemens', 'Bosch', 'Honeywell', 'General Electric', 'ABB'],
    'Marketing': ['Publicis', 'Havas', 'WPP', 'Omnicom', 'Dentsu', 'Ogilvy', 'BBDO', 'Leo Burnett', 'TBWA', 'Saatchi & Saatchi'],
    'Ventes': ['Decathlon', 'Carrefour', 'Auchan', 'Casino', 'Intermarché', 'Amazon', 'Walmart', 'Alibaba', 'eBay', 'Home Depot'],
    'Droit': ['Gide Loyrette Nouel', 'Clifford Chance', 'Baker McKenzie', 'Linklaters', 'Allen & Overy', 'Freshfields Bruckhaus Deringer', 'Herbert Smith Freehills', 'Norton Rose Fulbright', 'White & Case', 'CMS'],
    'Média': ['Le Monde', 'Le Figaro', 'Les Echos', 'L\'Equipe', 'M6', 'TF1', 'France Télévisions', 'Canal+', 'RTL', 'Ouest-France'],
    'Manufacture': ['Michelin', 'Renault', 'Peugeot', 'Valeo', 'Airbus', 'Boeing', 'Safran', 'Thales', 'Alstom', 'Saint-Gobain'],
    'Commerce': ['Carrefour', 'Auchan', 'LVMH', 'Hermès', 'Kering', 'L\'Oréal', 'Sephora', 'Zara', 'H&M', 'Nike'],
    'Hôtellerie': ['Accor', 'Marriott', 'Hilton', 'Hyatt', 'InterContinental', 'Wyndham', 'Best Western', 'Radisson', 'Choice Hotels', 'Four Seasons'],
    'Transport': ['SNCF', 'Air France', 'RATP', 'Transdev', 'Keolis', 'DHL', 'FedEx', 'UPS', 'Maersk', 'CMA CGM'],
    'Énergie': ['Total', 'EDF', 'Engie', 'Schneider Electric', 'Veolia', 'Chevron', 'ExxonMobil', 'Shell', 'BP', 'Eni'],
    'Immobilier': ['Bouygues Immobilier', 'Nexity', 'Vinci Immobilier', 'Icade', 'Unibail-Rodamco', 'CBRE', 'JLL', 'Savills', 'Colliers', 'Klepierre'],
    'Télécommunications': ['Orange', 'SFR', 'Bouygues Telecom', 'Free', 'Altice', 'AT&T', 'Verizon', 'Vodafone', 'Telefónica', 'T-Mobile'],
    'Divertissement': ['Disney', 'Netflix', 'Warner Bros', 'Universal', 'Sony Pictures', 'Paramount', 'DreamWorks', 'HBO', 'NBCUniversal', '20th Century Fox'],
    'Sports': ['Nike', 'Adidas', 'Puma', 'Decathlon', 'Under Armour', 'Reebok', 'Asics', 'New Balance', 'Columbia', 'Patagonia'],
    'Science': ['CNRS', 'INRAE', 'INSERM', 'CEA', 'IRSN', 'Institut Pasteur', 'NASA', 'ESA', 'Max Planck Society', 'MIT'],
    'Fonction publique': ['Ministère de l\'Intérieur', 'Ministère de la Défense', 'Ministère de la Santé', 'Ministère de l\'Éducation Nationale', 'Ministère des Finances', 'Commission Européenne', 'ONU', 'OCDE', 'FMI', 'Banque Mondiale'],
    'Logistique': ['DHL', 'FedEx', 'UPS', 'Kuehne+Nagel', 'Geodis', 'DB Schenker', 'CEVA Logistics', 'XPO Logistics', 'Rhenus', 'Nippon Express'],
    'Banque': ['BNP Paribas', 'Crédit Agricole', 'Société Générale', 'HSBC', 'Natixis', 'Barclays', 'Citi', 'Wells Fargo', 'Bank of America', 'Santander'],
    'Assurance': ['AXA', 'Allianz', 'Generali', 'MAIF', 'MACIF', 'Aviva', 'Prudential', 'MetLife', 'Zurich Insurance', 'Chubb'],
    'Consulting': ['McKinsey', 'Boston Consulting Group', 'Bain & Company', 'Roland Berger', 'Oliver Wyman', 'PwC', 'Deloitte', 'EY', 'KPMG', 'Accenture'],
    'Ressources humaines': ['Adecco', 'Randstad', 'Manpower', 'Michael Page', 'Hays', 'Robert Half', 'Kelly Services', 'Robert Walters', 'Hudson', 'Korn Ferry'],
    'Communication': ['Publicis', 'Havas', 'Dentsu', 'Omnicom', 'WPP', 'FleishmanHillard', 'Ketchum', 'Weber Shandwick', 'Edelman', 'Burson Cohn & Wolfe'],
    'Maintenance': ['Vinci', 'Eiffage', 'Bouygues Construction', 'Colas', 'Fayat', 'SNC Lavalin', 'Jacobs Engineering', 'Fluor', 'Bechtel', 'TechnipFMC'],
    'Sécurité': ['Securitas', 'Prosegur', 'G4S', 'Allied Universal', 'Brinks', 'ADT', 'Tyco', 'Stanley Security', 'GardaWorld', 'Axis Communications'],
    'Automobile': ['Renault', 'Peugeot', 'Citroën', 'Tesla', 'Volkswagen', 'Toyota', 'Ford', 'General Motors', 'BMW', 'Honda'],
    'Mode': ['LVMH', 'Kering', 'Chanel', 'Hermès', 'Gucci', 'Prada', 'Louis Vuitton', 'Dior', 'Burberry', 'Versace'],
    'Technique': ['Schneider Electric', 'Siemens', 'ABB', 'Legrand', 'Bosch', 'Honeywell', 'General Electric', 'Emerson', 'Rockwell Automation', 'Mitsubishi Electric'],
    'Production': ['Airbus', 'Boeing', 'Safran', 'Thales', 'Dassault Aviation', 'Lockheed Martin', 'Northrop Grumman', 'General Dynamics', 'Raytheon', 'BAE Systems'],
    'Agriculture': ['Monsanto', 'Syngenta', 'Bayer', 'BASF', 'Dow AgroSciences', 'John Deere', 'CNH Industrial', 'AGCO', 'Kubota', 'Archer Daniels Midland'],
    'Art': ['Christie\'s', 'Sotheby\'s', 'Gagosian', 'Hauser & Wirth', 'Pace Gallery', 'Tate Modern', 'MoMA', 'Louvre', 'Uffizi Gallery', 'Guggenheim'],
    'Design': ['IDEO', 'Frog Design', 'Pentagram', 'Landor', 'R/GA', 'Zaha Hadid Architects', 'Norman Foster', 'BIG - Bjarke Ingels Group', 'Snøhetta', 'SOM'],
    'Environnement': ['Veolia', 'Suez', 'Schneider Electric', 'EDF', 'Engie', 'Total', 'Eni', 'BP', 'Shell', 'Neste'],
    'Tourisme': ['Airbnb', 'Booking.com', 'Expedia', 'TripAdvisor', 'TUI', 'Thomas Cook', 'Club Med', 'Marriott Vacations', 'Hyatt', 'Hilton'],
    'Assistance': ['Seris', 'Onet', 'Fiducial', 'Samsic', 'Atalian', 'Groupe Crit', 'Securitas', 'G4S', 'Prosegur', 'Allied Universal'],
    'Social': ['Emmaüs', 'Secours Catholique', 'Croix-Rouge', 'Médecins Sans Frontières', 'Amnesty International', 'UNICEF', 'Handicap International', 'Caritas', 'Oxfam', 'World Vision'],
    'Événementiel': ['GL Events', 'Comexposium', 'Reed Exhibitions', 'VIPARIS', 'MCI Group', 'UFI', 'Messe Frankfurt', 'Informa', 'Tarsus', 'Clarion Events'],
    'Manutention': ['Manitou', 'Toyota Material Handling', 'Caterpillar', 'Hyster-Yale', 'Jungheinrich', 'Linde Material Handling', 'Komatsu', 'Doosan', 'Mitsubishi Logisnext', 'Clark'],
    'Défense': ['Thales', 'Dassault Aviation', 'Naval Group', 'MBDA', 'Airbus Defence and Space', 'Lockheed Martin', 'Northrop Grumman', 'Raytheon', 'BAE Systems', 'General Dynamics'],
    'ONG': ['Greenpeace', 'WWF', 'Amnesty International', 'Oxfam', 'Médecins Sans Frontières', 'Human Rights Watch', 'CARE', 'Save the Children', 'International Rescue Committee', 'Plan International'],
    'Industrie alimentaire': ['Danone', 'Nestlé', 'Unilever', 'Mondelez', 'Kraft Heinz', 'General Mills', 'PepsiCo', 'Coca-Cola', 'Mars', 'Kellogg\'s'],
    'Culture': ['Le Louvre', 'Musée d\'Orsay', 'Centre Pompidou', 'Bibliothèque Nationale de France', 'Opéra de Paris', 'British Museum', 'Metropolitan Museum of Art', 'Rijksmuseum', 'Museo del Prado', 'Hermitage Museum'],
    'BTP': ['Bouygues Construction', 'Eiffage', 'Vinci Construction', 'Colas', 'Spie Batignolles', 'Skanska', 'Hochtief', 'Strabag', 'Fluor', 'Bechtel'],
    'Recherche': ['CNRS', 'INRAE', 'INSERM', 'CEA', 'IRSN', 'Institut Pasteur', 'NASA', 'ESA', 'Max Planck Society', 'MIT'],
    'Aérospatial': ['Airbus', 'Boeing', 'Safran', 'Thales', 'Dassault Aviation', 'Lockheed Martin', 'Northrop Grumman', 'General Dynamics', 'Raytheon', 'BAE Systems'],
    'Technologie': ['Google', 'Microsoft', 'IBM', 'Apple', 'Amazon', 'Facebook', 'Intel', 'Oracle', 'Cisco', 'Samsung'],
    'Innovation': ['Tesla', 'SpaceX', 'Google X', 'Apple', 'Microsoft', 'Amazon', 'Facebook', 'IBM Research', 'Intel Labs', 'Bell Labs'],
    'Restauration': ['McDonald\'s', 'Starbucks', 'Subway', 'KFC', 'Burger King', 'Pizza Hut', 'Domino\'s', 'Chipotle', 'Dunkin\'', 'Chick-fil-A'],
    'Beauté': ['L\'Oréal', 'Estée Lauder', 'Procter & Gamble', 'Unilever', 'Shiseido', 'Coty', 'Beiersdorf', 'Johnson & Johnson', 'Avon', 'LVMH']
}


# Tâches par domaine
taches = {
    'Informatique': [
        'Développement et maintenance de logiciels',
        'Gestion des bases de données',
        'Support technique et dépannage',
        'Développement de sites web',
        'Développement d\'applications mobiles',
        'Analyse de données et génération de rapports',
        'Gestion de projets informatiques'
    ],
    'Santé': [
        'Soins aux patients',
        'Administration des médicaments',
        'Coordination avec les médecins',
        'Tenue des dossiers médicaux',
        'Éducation des patients sur la santé',
        'Prélèvements sanguins et analyses'
    ],
    'Finance': [
        'Analyse des états financiers',
        'Préparation des déclarations fiscales',
        'Gestion des comptes clients',
        'Analyse des risques financiers',
        'Audit interne et externe',
        'Planification financière'
    ],
    'Éducation': [
        'Préparation des cours',
        'Enseignement en classe',
        'Évaluation des étudiants',
        'Développement de matériel pédagogique',
        'Organisation d\'événements éducatifs'
    ],
    'Ingénierie': [
        'Conception et développement de produits',
        'Gestion de projets techniques',
        'Réalisation de tests et validation',
        'Maintenance des équipements',
        'Amélioration des processus de production'
    ],
    'Marketing': [
        'Développement de stratégies marketing',
        'Gestion des campagnes publicitaires',
        'Analyse des tendances du marché',
        'Rédaction de contenu promotionnel',
        'Gestion des réseaux sociaux'
    ],
    'Ventes': [
        'Prospection de nouveaux clients',
        'Négociation des contrats',
        'Suivi des commandes clients',
        'Analyse des ventes',
        'Formation des équipes de vente'
    ],
    'Droit': [
        'Rédaction de contrats',
        'Conseil juridique',
        'Représentation en justice',
        'Recherche juridique',
        'Négociation de règlements'
    ],
    'Média': [
        'Création de contenu',
        'Montage vidéo',
        'Gestion des réseaux sociaux',
        'Rédaction d\'articles',
        'Production de podcasts'
    ],
    'Manufacture': [
        'Supervision de la production',
        'Maintenance des équipements',
        'Contrôle qualité',
        'Gestion des stocks',
        'Amélioration continue'
    ],
    'Commerce': [
        'Gestion des stocks',
        'Service à la clientèle',
        'Merchandising',
        'Planification des ventes',
        'Négociation avec les fournisseurs'
    ],
    'Hôtellerie': [
        'Accueil des clients',
        'Gestion des réservations',
        'Coordination des services de nettoyage',
        'Organisation d\'événements',
        'Service en salle'
    ],
    'Transport': [
        'Planification des itinéraires',
        'Gestion de la flotte de véhicules',
        'Coordination des livraisons',
        'Suivi des expéditions',
        'Optimisation des coûts de transport'
    ],
    'Énergie': [
        'Maintenance des infrastructures énergétiques',
        'Gestion des réseaux électriques',
        'Audit énergétique',
        'Développement de solutions renouvelables',
        'Analyse de la consommation énergétique'
    ],
    'Immobilier': [
        'Négociation des transactions immobilières',
        'Gestion des biens locatifs',
        'Prospection de nouveaux biens',
        'Évaluation des biens immobiliers',
        'Gestion des baux'
    ],
    'Télécommunications': [
        'Installation de réseaux',
        'Maintenance des équipements télécoms',
        'Support technique aux clients',
        'Développement de solutions de téléphonie',
        'Optimisation des réseaux existants'
    ],
    'Divertissement': [
        'Organisation d\'événements',
        'Production de contenu',
        'Gestion des talents',
        'Promotion des spectacles',
        'Création de campagnes de marketing'
    ],
    'Sports': [
        'Entraînement des athlètes',
        'Organisation de compétitions',
        'Analyse des performances',
        'Gestion des installations sportives',
        'Promotion des événements sportifs'
    ],
    'Science': [
        'Réalisation de recherches',
        'Analyse de données scientifiques',
        'Publication de résultats',
        'Participation à des conférences',
        'Développement de nouvelles technologies'
    ],
    'Fonction publique': [
        'Gestion administrative',
        'Développement de politiques publiques',
        'Service aux citoyens',
        'Coordination des services publics',
        'Gestion des budgets publics'
    ],
    'Logistique': [
        'Gestion des stocks',
        'Planification des transports',
        'Optimisation des chaînes d\'approvisionnement',
        'Suivi des expéditions',
        'Coordination des entrepôts'
    ],
    'Banque': [
        'Gestion des comptes clients',
        'Analyse des risques de crédit',
        'Développement de produits financiers',
        'Conseil en investissement',
        'Audit interne'
    ],
    'Assurance': [
        'Évaluation des demandes de remboursement',
        'Gestion des contrats d\'assurance',
        'Analyse des risques assurantiels',
        'Développement de nouveaux produits',
        'Conseil aux clients'
    ],
    'Consulting': [
        'Analyse des processus',
        'Développement de stratégies',
        'Gestion de projets',
        'Conseil en transformation digitale',
        'Formation des équipes'
    ],
    'Ressources humaines': [
        'Recrutement et intégration des employés',
        'Gestion des paies et des avantages sociaux',
        'Développement de plans de formation',
        'Gestion des relations de travail',
        'Mise en place de stratégies de rétention'
    ],
    'Communication': [
        'Gestion des relations publiques',
        'Rédaction de communiqués de presse',
        'Développement de stratégies de communication',
        'Gestion des réseaux sociaux',
        'Organisation d\'événements médiatiques'
    ],
    'Maintenance': [
        'Diagnostic des pannes',
        'Maintenance préventive et corrective',
        'Gestion des pièces de rechange',
        'Planification des interventions',
        'Formation des techniciens'
    ],
    'Sécurité': [
        'Surveillance des lieux',
        'Gestion des systèmes de sécurité',
        'Intervention en cas d\'urgence',
        'Rédaction de rapports de sécurité',
        'Formation des agents de sécurité'
    ],
    'Automobile': [
        'Réparation des véhicules',
        'Entretien courant',
        'Diagnostic des pannes',
        'Vente de pièces détachées',
        'Service à la clientèle'
    ],
    'Mode': [
        'Design de vêtements',
        'Gestion des collections',
        'Marketing de mode',
        'Organisation de défilés',
        'Analyse des tendances'
    ],
    'Technique': [
        'Installation et maintenance des équipements',
        'Réalisation de schémas techniques',
        'Diagnostic des pannes',
        'Gestion des chantiers',
        'Conformité aux normes'
    ],
    'Production': [
        'Gestion des lignes de production',
        'Contrôle qualité',
        'Optimisation des processus',
        'Maintenance des équipements',
        'Gestion des équipes de production'
    ],
    'Agriculture': [
        'Gestion des cultures',
        'Élevage des animaux',
        'Maintenance des équipements agricoles',
        'Commercialisation des produits agricoles',
        'Planification des récoltes'
    ],
    'Art': [
        'Création d\'œuvres artistiques',
        'Exposition des œuvres',
        'Promotion des artistes',
        'Restauration d\'œuvres d\'art',
        'Organisation d\'événements artistiques'
    ],
    'Design': [
        'Conception de produits',
        'Design graphique',
        'Création de maquettes',
        'Gestion des projets de design',
        'Utilisation de logiciels de design'
    ],
    'Environnement': [
        'Gestion des ressources naturelles',
        'Développement de projets durables',
        'Analyse environnementale',
        'Gestion des déchets',
        'Éducation à l\'environnement'
    ],
    'Tourisme': [
        'Organisation de voyages',
        'Gestion des réservations',
        'Accueil des touristes',
        'Planification d\'itinéraires',
        'Promotion des destinations'
    ],
    'Assistance': [
        'Accueil des visiteurs',
        'Gestion des appels',
        'Organisation des agendas',
        'Rédaction de comptes-rendus',
        'Gestion des fournitures de bureau'
    ],
    'Social': [
        'Accompagnement des personnes en difficulté',
        'Organisation d\'ateliers',
        'Gestion de projets sociaux',
        'Écoute et conseil',
        'Coordination avec les services sociaux'
    ],
    'Événementiel': [
        'Organisation d\'événements',
        'Coordination des prestataires',
        'Gestion des invités',
        'Promotion des événements',
        'Suivi logistique'
    ],
    'Manutention': [
        'Chargement et déchargement des marchandises',
        'Gestion des stocks',
        'Préparation des commandes',
        'Tri des colis',
        'Maintenance des équipements de manutention'
    ],
    'Défense': [
        'Surveillance et protection',
        'Gestion des opérations',
        'Entraînement des troupes',
        'Planification des missions',
        'Sécurité des installations'
    ],
    'ONG': [
        'Gestion de projets humanitaires',
        'Coordination avec les partenaires',
        'Collecte de fonds',
        'Sensibilisation du public',
        'Gestion des bénévoles'
    ],
    'Industrie alimentaire': [
        'Production de denrées alimentaires',
        'Contrôle qualité',
        'Gestion des stocks',
        'Maintenance des équipements',
        'Logistique et distribution'
    ],
    'Culture': [
        'Organisation d\'événements culturels',
        'Promotion des artistes',
        'Gestion des expositions',
        'Coordination avec les partenaires culturels',
        'Développement de projets artistiques'
    ],
    'BTP': [
        'Gestion de chantiers',
        'Coordination des équipes',
        'Planification des travaux',
        'Contrôle qualité',
        'Sécurité sur les chantiers'
    ],
    'Recherche': [
        'Réalisation de recherches',
        'Analyse de données',
        'Publication de résultats',
        'Gestion de projets de recherche',
        'Développement de nouvelles technologies'
    ],
    'Aérospatial': [
        'Conception de systèmes aérospatiaux',
        'Maintenance des équipements',
        'Gestion des missions spatiales',
        'Analyse des données',
        'Développement de technologies spatiales'
    ],
    'Technologie': [
        'Développement de logiciels',
        'Conception de produits technologiques',
        'Gestion de projets',
        'Support technique',
        'Formation des utilisateurs'
    ],
    'Beauté': [
        'Conseil en soins de la peau',
        'Maquillage professionnel',
        'Coupe et coiffure',
        'Manucure et pédicure',
        'Soins du visage',
        'Massage relaxant',
        'Vente de produits de beauté',
        'Formation en esthétique'
    ],
    'Restauration': [
        'Préparation des plats',
        'Gestion des commandes',
        'Service en salle',
        'Gestion des stocks',
        'Nettoyage et entretien de la cuisine',
        'Accueil et prise en charge des clients',
        'Création de menus',
        'Supervision de l\'équipe de cuisine'
    ],
    'Sécurité': [
        'Surveillance des lieux',
        'Gestion des systèmes de sécurité',
        'Intervention en cas d\'urgence',
        'Rédaction de rapports de sécurité',
        'Formation des agents de sécurité',
        'Contrôle des accès',
        'Patrouilles régulières',
        'Gestion des incidents'
    ],
    'Innovation': [
        'Développement de nouvelles technologies',
        'Veille technologique et analyse des tendances',
        'Conception de prototypes',
        'Gestion de projets innovants',
        'Collaboration avec les équipes de recherche',
        'Test et validation des nouveaux produits',
        'Analyse des besoins du marché',
        'Rédaction de brevets'
    ]
}

# Fonction pour générer un CV
def generer_cv(id):
    nationalite = random.choice(nationalites_afrique + nationalites_asie + nationalites_europe + nationalites_ameriques)
    genre = random.choice(['homme', 'femme'])
    prenom = random.choice(prenoms_pays[nationalite][genre])
    nom = random.choice(noms_pays[nationalite])
    pays = nationalite  # Simplification, on considère que le pays est le même que la nationalité
    age = random.randint(22, 65)
    handicap = random.choices(handicaps, weights=weights_handicaps, k=1)[0]

    domaine = random.choice(domaines)
    intitule = random.choice(taches[domaine])
    
    # Déterminer le nombre d'expériences en fonction de l'âge
    if age < 30:
        nb_experiences = random.randint(0, 3)
    elif age < 40:
        nb_experiences = random.randint(2, 5)
    elif age < 50:
        nb_experiences = random.randint(3, 7)
    else:
        nb_experiences = random.randint(4, 10)

    experiences = []
    for _ in range(nb_experiences):
        entreprise = f"{intitule} chez {random.choice(entreprises[domaine])}"
        debut = fake.date_between(start_date='-20y', end_date='-1y')
        fin = fake.date_between(start_date=debut, end_date='today')
        taches_realisees = random.sample(taches[domaine], k=random.randint(1, 3))
        experiences.append({
            'entreprise': entreprise,
            'debut': debut.isoformat(),
            'fin': fin.isoformat(),
            'taches': taches_realisees
        })

    # Génération du parcours éducatif
    parcours_educatif = []
    niveaux_etudes = ['Bep', 'Baccalauréat', 'BTS', 'Licence', 'Master', 'Ingénieur', 'Doctorat']
    niveau_obtenu = random.choice(niveaux_etudes)
    annee_obtention_precedente = datetime.now().year
    
    for niveau in niveaux_etudes[:niveaux_etudes.index(niveau_obtenu) + 1]:
        ecole = random.choice(ecoles[niveau])
        annee_obtention = random.randint(2000, annee_obtention_precedente)
        parcours_educatif.append({
            'niveau': niveau,
            'ecole': ecole,
            'annee': annee_obtention
        })
        annee_obtention_precedente = annee_obtention - 1  # Assurer que les diplômes sont obtenus dans un ordre chronologique cohérent
    # Trier le parcours éducatif par année décroissante
    parcours_educatif = sorted(parcours_educatif, key=lambda x: x['annee'], reverse=True)

    langues_parlees = random.choice(langues)
    competences_humaines = random.sample(competences_humaines_list, k=random.randint(3, 6))
    
    # Déterminer le nombre de compétences techniques en fonction du niveau d'éducation
    if niveau_obtenu in ['Bep', 'Baccalauréat']:
        nb_competences_techniques = random.randint(3, 6)
    elif niveau_obtenu in ['BTS', 'Licence']:
        nb_competences_techniques = random.randint(6, 10)
    else:
        nb_competences_techniques = random.randint(10, 15)
    
    competences_techniques_domaine = competences_techniques.get(domaine, [])
    competences_techniques_personne = random.sample(competences_techniques_domaine, k=min(nb_competences_techniques, len(competences_techniques_domaine)))

    centres_interet = random.sample(centres_d_interet, k=random.randint(2, 5))

    recommendations = [
        {
            'nom': fake.name(),
            'poste': fake.job(),
            'entreprise': random.choice(entreprises[domaine]),
            'email': fake.email(domain=random.choices(
                ['google.com', 'msn.com', 'aol.com', 'orange.fr', 'free.fr', 'yahoo.com', 'outlook.com', 'hotmail.com'],
                weights=[50, 10, 10, 10, 5, 20, 10, 10],
                k=1)[0]),
            'telephone': fake.phone_number()
        }
        for _ in range(random.randint(0, 3))  # Maximum 3 recommendations
    ]

    statut = random.choice(['En poste', 'Demandeur d\'emploi', 'étudiant', 'freelance', 'Alternant', 'stagiaire'])

    # Calcul de la prétention salariale
    salaire_base = 21  # Base de 21k€
    if niveau_obtenu == 'Baccalauréat':
        salaire_base += 10
    elif niveau_obtenu == 'BTS':
        salaire_base += 15
    elif niveau_obtenu in ['Licence', 'Master']:
        salaire_base += 20
    elif niveau_obtenu == 'Ingénieur':
        salaire_base += 40
    elif niveau_obtenu == 'Doctorat':
        salaire_base += 50
    pretention_salariale = salaire_base + (len(experiences) * 2)  # +2k€ par année d'expérience

    return {
        'id': id,
        'prenom': prenom,
        'nom': nom,
        'nationalite': nationalite,
        'genre': genre,
        'age': age,
        'pays': pays,
        'handicap': handicap,
        'domaine': domaine,
        'intitule': intitule,
        'experiences': experiences,
        'parcours_educatif': parcours_educatif,
        'langues': langues_parlees,
        'competences_humaines': competences_humaines,
        'competences_techniques': competences_techniques_personne,
        'centres_interet': centres_interet,
        'recommendations': recommendations,
        'statut': statut,
        'pretention_salariale': f"{pretention_salariale}k€"
    }

# Générer 12 500 CVs
cv_list = [generer_cv(i) for i in range(1, 12501)]

# Sauvegarder en JSON avec indentation
with open('cv_data.json', 'w', encoding='utf-8') as f:
    json.dump(cv_list, f, ensure_ascii=False, indent=4)