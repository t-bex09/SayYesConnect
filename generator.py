import random
import string
from User import User

def generate_random_users(num_users):
    first_names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Henry", "Isabella", "Jack"]
    last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Taylor", "Clark"]
    colleges = ["Example University", "ABC College", "XYZ Institute"]
    majors = ["Computer Science", "Engineering", "Business", "Biology", "Psychology"]
    degrees = ["Bachelor's", "Master's", "Ph.D."]
    occupations = ["Software Developer", "Data Analyst", "Teacher", "Doctor", "Engineer"]
    companies = ["ABC Company", "XYZ Corporation", "Example Inc"]
    struggles = ["Lack of relevant work experience","Limited networking opportunities","Tough competition from other candidates","Difficulty in showcasing skills and qualifications","Unclear career goals","Insufficient knowledge about the job market",
    "Challenges in writing an effective resume and cover letter",
    "Poor interview skills",
    "Bias or discrimination in the hiring process",
    "Lack of confidence or self-esteem",
    "Limited access to job opportunities",
    "Financial constraints and inability to afford necessary resources",
    "Inadequate guidance or mentorship",
    "Geographical limitations",
    "Difficulty in balancing job search with other commitments",
    "Unstable job market and economic conditions",
    "Industry-specific challenges and requirements",
    "Mismatch between skills and job requirements",
    "Inability to find entry-level positions",
    "Struggles related to remote job searching or remote work"
        ]
    password_length = 8

    users = []

    for _ in range(num_users):
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        age = random.randint(18, 65)
        gender = random.choice(["Male", "Female"])
        college = random.choice(colleges)
        major = random.choice(majors)
        degree = random.choice(degrees)
        occupation = random.choice(occupations)
        company = random.choice(companies)
        username = f"{first_name.lower()}.{last_name.lower()}"

        # Generate a random password
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=password_length))
        struggle = random.choice(struggles)
        user = User(first_name, last_name, age, gender, college, major, degree, occupation, company, username, password,struggle)
        users.append(user)

    return users
