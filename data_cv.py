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
    'Immobilier', 'Assistance', 'Social', 'Culture', 'Recherche', 'Enseignement', 'Formation',
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

# Prénoms et noms spécifiques par ethnie
noms_africains = ["Diop", "Traoré", "Sow", "Ndiaye", "Diallo"]
prenoms_africains = ["Awa", "Mamadou", "Fatou", "Ibrahima", "Aminata"]

noms_magrebins = ["Ben Ali", "Bouzid", "Haddad", "Jaziri", "Bensaid"]
prenoms_magrebins = ["Omar", "Fatima", "Nour", "Yasmine", "Mohamed"]

noms_asiatiques = ["Nguyen", "Wang", "Chen", "Tran", "Li"]
prenoms_asiatiques = ["Linh", "Minh", "Yen", "Thanh", "Huong"]

noms_est_europeens = ["Kovacs", "Nagy", "Horvat", "Novak", "Popov"]
prenoms_est_europeens = ["Boris", "Mila", "Daria", "Ivan", "Anya"]

noms_autres_europeens = ["Dupont", "Martin", "Bernard", "Dubois", "Moreau"]
prenoms_autres_europeens = ["Jean", "Marie", "Pierre", "Lucie", "Julien"]

# Générer les données factices
def generate_fake_data(num_records):
    data = []
    for i in range(num_records):
        nationalite = random.choices(
            ['Sénégal', 'Maroc', 'Chine', 'Hongrie', 'France'], 
            weights=[22, 18, 7, 13, 40], 
            k=1
        )[0]

        if nationalite == 'Sénégal':
            prenom = random.choice(prenoms_africains)
            nom = random.choice(noms_africains)
        elif nationalite == 'Maroc':
            prenom = random.choice(prenoms_magrebins)
            nom = random.choice(noms_magrebins)
        elif nationalite == 'Chine':
            prenom = random.choice(prenoms_asiatiques)
            nom = random.choice(noms_asiatiques)
        elif nationalite == 'Hongrie':
            prenom = random.choice(prenoms_est_europeens)
            nom = random.choice(noms_est_europeens)
        else:
            prenom = random.choice(prenoms_autres_europeens)
            nom = random.choice(noms_autres_europeens)
        
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
                'degree': random.choice(['Baccalauréat', 'Licence', 'Master', 'Doctorat']),
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
                'email': fake.email(domain="exemple.com"),
                'phone': fake.phone_number()
            }
            for _ in range(random.randint(0, 3))  # Maximum 3 recommendations
        ]

        situations = [
            'employé', 'chômeur', 'étudiant', 'freelance', 'retraité'
        ]
        
        sexes = ['homme', 'femme', 'autre']
        
        langues = [
            {'français': 'C2', 'anglais': 'B2', 'espagnol': 'B1'},
            {'français': 'C2', 'anglais': 'A2', 'allemand': 'B1'},
            {'français': 'C1', 'anglais': 'B2', 'italien': 'A2'},
            {'français': 'C2', 'anglais': 'C1', 'chinois': 'B2'},
            {'français': 'C2', 'arabe': 'C1', 'anglais': 'B1'}
        ]
        
        centres_d_interet = [
            'lecture', 'sport', 'voyages', 'musique', 'cinéma',
            'cuisine', 'photographie', 'jardinage', 'randonnée', 'peinture'
        ]
        
        row = {
            'ID': i + 1,
            'nom': nom,
            'prenom': prenom,
            'adresse': fake.address(),
            'email': fake.email(domain="exemple.com"),
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
            'age': random.randint(22, 65),
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
