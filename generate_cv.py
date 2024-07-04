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
    'situation', 'domaine', 'age', 'sexe', 'centres_d_interet', 'ethnie', 'handicap'
]

# Domaines étendus
domaines = [
    'Informatique', 'Santé', 'Finance', 'Éducation', 'Ingénierie', 'Marketing', 'Ventes', 
    'Droit', 'Manufacture', 'Commerce de détail', 'Hôtellerie', 'Transport', 'Construction', 
    'Énergie', 'Immobilier', 'Télécommunications', 'Média', 'Divertissement', 'Sports', 
    'Science', 'Recherche', 'Administration publique', 'ONG', 'Consulting', 'Art', 
    'Design', 'Agriculture', 'Industrie alimentaire', 'Aérospatiale', 'Défense'
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

# Générer les données factices
def generate_fake_data(num_records):
    data = []
    for i in range(num_records):
        ethnie = random.choices(
            ['Africain', 'Maghrébin', 'Asiatique', 'Européen de l\'Est', 'Autre Européen'], 
            weights=[22, 18, 7, 13, 40], 
            k=1
        )[0]

        # Utiliser des noms et prénoms spécifiques selon l'ethnie
        if ethnie == 'Africain':
            prenom = fake.first_name_male()
            nom = fake.last_name()
        elif ethnie == 'Maghrébin':
            prenom = fake.first_name_male()
            nom = fake.last_name()
        elif ethnie == 'Asiatique':
            prenom = fake.first_name_male()
            nom = fake.last_name()
        elif ethnie == 'Européen de l\'Est':
            prenom = fake.first_name_male()
            nom = fake.last_name()
        else:
            prenom = fake.first_name()
            nom = fake.last_name()
        
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
            'nom': nom,
            'prenom': prenom,
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
            'ethnie': ethnie,
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
df = explode_column(df, 'recommendations', 'recommendation_')

# Exporter le DataFrame en fichier CSV
csv_filename = 'generated_cv_data.csv'
df.to_csv(csv_filename, index=False, encoding='utf-8-sig')

print(f"DataFrame generated and saved to {csv_filename}")
