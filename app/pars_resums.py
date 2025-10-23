from faker import Faker
import random
import json
import os

fake = Faker('ru_RU')

# Загружаем словарь навыков
skills_dict = json.load(open('../data/skills_dictionary.json', 'r', encoding='utf-8'))
all_skills = [s for lst in skills_dict.values() for s in lst]

os.makedirs('../data/resumes', exist_ok=True)

for i in range(1, 51):
    name = fake.name()
    company = fake.company()
    position = random.choice(["Data Analyst", "Python Developer", "ML Engineer", "Backend Developer"])
    exp_years = random.randint(1, 7)
    selected_skills = random.sample(all_skills, k=random.randint(5, 10))

    text = f"""{name}
Email: {fake.email()}
Телефон: {fake.phone_number()}

Опыт работы:
{2017 + random.randint(0, 5)}–2024 — {position}, {company}
• Работа с {', '.join(selected_skills[:3])}
• Опыт анализа данных и автоматизации

Навыки: {', '.join(selected_skills)}
Образование: {fake.company()} Университет, Прикладная информатика
"""

    with open(f"data/resumes/resume_{i:02d}.txt", "w", encoding="utf-8") as f:
        f.write(text)

print("✅ 50 синтетических резюме успешно сгенерировано.")
