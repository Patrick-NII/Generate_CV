import pandas as pd
from faker import Faker
import random
import json

# Initialiser Faker
fake = Faker('fr_FR')

# Définir les colonnes du DataFrame
columns = [
    'ID', 'nom', 'prenom', 'adresse', 'email', 'numero_de_telephone', 'intitule', 
    'diplome', 'experiences', 'educations', 'langues', 'competences', 'recommendations', 
    'situation', 'domaine', 'age', 'sexe', 'centres_d_interet', 'nationalite', 'handicap'
]

# Domaines étendus
domaines = [
    'Informatique', 'Santé', 'Finance', 'Éducation', 'Ingénierie', 'Marketing', 'Ventes', 
    'Droit', 'Manufacture', 'Commerce', 'Hôtellerie', 'Transport', 'Etudiant', 
    'Énergie', 'Immobilier', 'Télécommunications', 'Média', 'Divertissement', 'Sports', 
    'Science', 'Sans Emploi', 'Fonction publique', 'ONG', 'Consulting', 'Art', 
    'Design', 'Agriculture', 'Industrie alimentaire', 'Aérospatiale', 'Défense', 'Manutention',
    'Logistique', 'Ressources humaines', 'Environnement', 'Tourisme', 'Sécurité', 'Automobile',
    'Mode', 'Beauté', 'Restauration', 'Événementiel', 'BTP', 'Sécurité', 'Assurance', 'Banque',
    'Immobilier', 'Assistance', 'Social', 'Culture', 'Recherche', 'Enseignement', 'Formation'
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

# Prénoms et noms spécifiques par pays
prenoms_pays = {
    'Sénégal': ["Awa", "Mamadou", "Fatou", "Ibrahima", "Aminata", "Moussa", "Ndeye", "Ousmane", "Khady", "Abdou"],
    'Maroc': ["Omar", "Fatima", "Nour", "Yasmine", "Mohamed", "Amina", "Hassan", "Sara", "Ali", "Loubna"],
    'Chine': ["Linh", "Minh", "Yen", "Thanh", "Huong", "Hoa", "Anh", "Dung", "Tuan", "Thao"],
    'Hongrie': ["Boris", "Mila", "Daria", "Ivan", "Anya", "Viktor", "Nina", "Maksim", "Sofia", "Dmitri"],
    'France': ["Jean", "Marie", "Pierre", "Lucie", "Julien", "Camille", "Antoine", "Manon", "Théo", "Léa"],
    'Algérie': ["Karim", "Zineb", "Mehdi", "Sabrina", "Nadia", "Youssef", "Sofiane", "Nora", "Sami", "Fatima"],
    'Tunisie': ["Ali", "Leila", "Rania", "Fares", "Hana", "Mehdi", "Sarra", "Amine", "Nour", "Mohamed"],
    'Côte d\'Ivoire': ["Adama", "Aïcha", "Kouadio", "Fatoumata", "Bakary", "Kadiatou", "Mamadou", "Aminata", "Koffi", "Awa"],
    'Nigeria': ["Olufemi", "Ngozi", "Chinedu", "Yemi", "Chinwe", "Obinna", "Chinonye", "Chukwu", "Nkiru", "Chukwuma"],
    'Afrique du Sud': ["Thabo", "Nandi", "Mandla", "Thandeka", "Sizwe", "Ntombi", "Sipho", "Nomvula", "Bongani", "Nokuthula"],
    'Vietnam': ["Anh", "Binh", "Chi", "Duc", "Ha", "Hai", "Hoa", "Huong", "Khanh", "Lan"],
    'Cambodge': ["Sok", "Chenda", "Dara", "Rathana", "Srey", "Sokha", "Sophea", "Sovann", "Sreyneang", "Sreypov"],
    'Inde': ["Amit", "Priya", "Ravi", "Anjali", "Sunil", "Sunita", "Raj", "Pooja", "Rahul", "Sarita"],
    'Pakistan': ["Ahmed", "Aisha", "Bilal", "Zara", "Imran", "Sana", "Ali", "Fatima", "Kamran", "Sadia"],
    'Japon': ["Yuki", "Sakura", "Hiro", "Mika", "Ken", "Aya", "Takumi", "Yui", "Haru", "Rina"],
    'Corée du Sud': ["Ji-hoon", "Min-ji", "Seo-yeon", "Hyun-woo", "Hye-jin", "Ji-woo", "Seung-hyun", "Ji-hye", "Min-ho", "Hye-won"],
    'Congo': ["Fabrice", "Patrick", "Trésor", "Rodrigue", "Hervé", "Rossi", "Héritier", "Patience", "Jolie", "Grâce", "Bénédicte", "Blandine", "Béatrice"],
    'Cameroun': ["Jean-Eudes", "Bernard", "Alain-Antoine", "Emmanuel", "Marie","Francine", "Hélène", "Louise", "Thérèse", "Marie-Claire"],
    'Togo': ["Kodjo", "Afi", "Yawovi", "Ayélé", "Kossi"],
    'Ghana': ["Kwame", "Akosua", "Kofi", "Abena", "Yaw"],
    'Bénin': ["Agnidé", "Sèmèvo", "Dossou", "Koutché", "Houngbédji"],
    'Angola': ["Miguel", "Ana", "Pedro", "Luísa", "João", "Maria", "Manuel", "Isabel", "António", "Teresa"],
    'Mali': ["Modibo", "Aïssata", "Kadiatou", "Bakary", "Djénéba"],
    'Mauritanie': ["Mohamed", "Aminata", "El Hacen", "Mbarka", "Cheikh"]
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
    'Congo': ["Mbemba", "Ndombe Muandi", "Ngita Makaya", "Mukoko", "Yoka",],
    'Cameroun': ["Ndongo", "Ndomo", "Nji", "Biya", "Mbappe"],
    'Togo': ["Kodjo", "Afi", "Yawovi", "Ayélé", "Kossi"],
    'Ghana': ["Kwame", "Akosua", "Kofi", "Abena", "Yaw"],
    'Bénin': ["Agnidé", "Sèmèvo", "Dossou", "Koutché", "Houngbédji"],
    'Angola': ["Da Costa", "Mendosa", "De Oliveira", "Maria", "João"],
    'Mali': ["Modibo", "Aïssata", "Kadiatou", "Bakary", "Djénéba"],
    'Mauritanie': ["Mohamed", "Aminata", "El Hacen", "Mbarka", "Cheikh"]
}

# Nationalités par continent
nationalites_afrique = ['Sénégal', 'Algérie', 'Tunisie', 'Côte d\'Ivoire', 'Nigeria', 
                        'Afrique du Sud', 'Congo', 'Cameroun', 'Togo', 'Ghana', 
                        'Bénin', 'Angola', 'Mali', 'Mauritanie']
nationalites_asie = ['Chine', 'Vietnam', 'Cambodge', 'Inde', 'Pakistan', 'Japon', 'Corée du Sud']
nationalites_europe = ['Hongrie', 'France', 'Allemagne', 'Italie', 'Espagne', 
                       'Portugal', 'Royaume-Uni', 'Pays-Bas', 'Belgique', 
                       'Suisse', 'Suède', 'Norvège', 'Danemark', 'Finlande', 
                       'Grèce', 'Pologne', 'Ukraine', 'Russie']
nationalites_ameriques = ['Brésil', 'Argentine', 'Mexique', 'Colombie', 
                          'Chili', 'Pérou', 'Venezuela', 
                          'Canada', 'États-Unis', 'Antilles Françaises']

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

# Générer les données factices
def generate_fake_data(num_records):
    data = []
    for i in range(num_records):
        nationalite = random.choice(nationalites_afrique + nationalites_asie + nationalites_europe + nationalites_ameriques)

        prenoms = prenoms_pays.get(nationalite, ["Jean", "Marie", "Pierre", "Lucie", "Julien"])
        noms = noms_pays.get(nationalite, ["Dupont", "Martin", "Bernard", "Dubois", "Moreau"])
        
        prenom = random.choice(prenoms)
        nom = random.choice(noms)
        
        experiences = [
            {
                'job_title': fake.job(),
                'company': fake.company(),
                'start_date': fake.date_between(start_date='-5y', end_date='-3y').strftime('%Y-%m-%d'),
                'end_date': fake.date_between(start_date='-3y', end_date='today').strftime('%Y-%m-%d'),
                'description': fake.text(max_nb_chars=150)
            }
            for _ in range(random.randint(1, 5))
        ]

        educations = [
            {
                'degree': random.choice(['Baccalauréat', 'Licence', 'Master', 'Ingénieur', 'Doctorat']),
                'school': fake.company(),
                'year': fake.year()
            }
            for _ in range(random.randint(1, 3))
        ]

        recommendations = [
            {
                'name': fake.name(),
                'position': fake.job(),
                'company': fake.company(),
                'email': fake.email(domain=random.choices(
                    ['google.com', 'msn.com', 'aol.com', 'orange.fr', 'free.fr', 'yahoo.com', 'outlook.com', 'hotmail.com'],
                    weights=[50, 10, 10, 10, 5, 20, 10, 10],
                    k=1)[0]),
                'phone': fake.phone_number()
            }
            for _ in range(random.randint(0, 3))  # Maximum 3 recommendations
        ]

        situations = [
            'employé', 'chômeur', 'étudiant', 'freelance', 'retraité'
        ]
        
        sexes = ['homme', 'femme', 'autre']
        
        row = {
            'ID': i + 1,
            'nom': nom,
            'prenom': prenom,
            'adresse': fake.address(),
            'email': fake.email(domain=random.choices(
                    ['google.com', 'msn.com', 'aol.com', 'orange.fr', 'free.fr', 'yahoo.com', 'outlook.com', 'hotmail.com'],
                    weights=[50, 10, 10, 10, 5, 20, 10, 10],
                    k=1)[0]),
            'numero_de_telephone': fake.phone_number(),
            'intitule': fake.job(),
            'diplome': random.choice(['Baccalauréat', 'Licence', 'Master', 'Doctorat']),
            'experiences': experiences,
            'educations': educations,
            'langues': random.choice(langues),
            'competences': ', '.join(fake.words(nb=5)),
            'recommendations': recommendations,
            'situation': random.choice(situations),
            'domaine': random.choice(domaines),
            'age': random.randint(18, 65),
            'sexe': random.choice(sexes),
            'centres_d_interet': ', '.join(random.sample(centres_d_interet, 4)),
            'nationalite': nationalite,
            'handicap': random.choices(handicaps, weights=weights_handicaps, k=1)[0]  # 14% avec handicap répartis parmi les types
        }
        data.append(row)
    return data

# Convertir les données en DataFrame
num_records = 12000
data = generate_fake_data(num_records)
df = pd.DataFrame(data, columns=columns)

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
json_filename = 'generated_cv_data.json'
df.to_json(json_filename, orient='records', force_ascii=False, indent=4)

print(f"DataFrame generated and saved to {json_filename}")
