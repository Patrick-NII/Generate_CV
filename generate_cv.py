import pandas as pd
from faker import Faker
import random
import json

# Initialiser Faker
fake = Faker()

# Définir les colonnes du DataFrame
columns = [
    'ID', 'nom', 'prenom', 'adresse', 'email', 'numero_de_telephone', 'intitule', 
    'diplome', 'experiences', 'educations', 'langues', 'competences', 'recommendations', 
    'situation', 'domaine', 'age', 'sexe', 'centres_d_interet', 'ethnie', 'handicap'
]

# Domaines étendus
domaines = [
    'IT', 'Healthcare', 'Finance', 'Education', 'Engineering', 'Marketing', 'Sales', 
    'Legal', 'Manufacturing', 'Retail', 'Hospitality', 'Transportation', 'Construction', 
    'Energy', 'Real Estate', 'Telecommunications', 'Media', 'Entertainment', 'Sports', 
    'Science', 'Research', 'Public Administration', 'NGO', 'Consulting', 'Art', 
    'Design', 'Agriculture', 'Food Industry', 'Aerospace', 'Defense'
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
weights = [86] + [1] * (len(handicaps) - 1)  # 14% avec handicap répartis également parmi les types de handicaps

# Générer les données factices
def generate_fake_data(num_records):
    data = []
    for i in range(num_records):
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
                'degree': fake.word().title() + ' ' + fake.word().title(),
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
                'email': fake.email(),
                'phone': fake.phone_number()
            }
            for _ in range(random.randint(0, 3))  # Maximum 3 recommendations
        ]

        situations = [
            'employed', 'unemployed', 'student', 'freelancer', 'retired'
        ]
        
        sexes = ['male', 'female', 'other']
        
        row = {
            'ID': i + 1,
            'nom': fake.last_name(),
            'prenom': fake.first_name(),
            'adresse': fake.address(),
            'email': fake.email(),
            'numero_de_telephone': fake.phone_number(),
            'intitule': fake.job(),
            'diplome': fake.word().title(),
            'experiences': experiences,
            'educations': educations,
            'langues': ', '.join(fake.words(nb=3)),
            'competences': ', '.join(fake.words(nb=5)),
            'recommendations': recommendations,
            'situation': random.choice(situations),
            'domaine': random.choice(domaines),
            'age': random.randint(22, 65),
            'sexe': random.choice(sexes),
            'centres_d_interet': ', '.join(fake.words(nb=4)),
            'ethnie': random.choice(['Asian', 'Black', 'Hispanic', 'White', 'Mixed', 'Native American']),
            'handicap': random.choices(handicaps, weights=weights, k=1)[0]  # 14% avec handicap répartis parmi les types
        }
        data.append(row)
    return data

# Convertir les données en DataFrame
num_records = 12000
data = generate_fake_data(num_records)
df = pd.DataFrame(data, columns=columns)

# Convertir les listes de dictionnaires en chaînes JSON pour les colonnes correspondantes
df['experiences'] = df['experiences'].apply(lambda x: json.dumps(x, ensure_ascii=False))
df['educations'] = df['educations'].apply(lambda x: json.dumps(x, ensure_ascii=False))
df['recommendations'] = df['recommendations'].apply(lambda x: json.dumps(x, ensure_ascii=False))

# Exporter le DataFrame en fichier CSV
csv_filename = 'generated_cv_data.csv'
df.to_csv(csv_filename, index=False, encoding='utf-8-sig')

print(f"DataFrame generated and saved to {csv_filename}")
