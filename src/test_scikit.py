from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Sample data
texts = ["""Вера Васильевна Горшкова
Email: amos_2011@example.com
Телефон: 8 461 056 4823

Опыт работы:
2021–2024 — ML Engineer, Лихачева Лтд
• Работа с sklearn, java, javascript
• Опыт анализа данных и автоматизации

Навыки: sklearn, java, javascript, python, pandas, git
Образование: ОАО «Нестерова» Университет, Прикладная информатика
""", """Синклитикия Владимировна Белякова
Email: filaret25@example.net
Телефон: +7 637 176 36 87

Опыт работы:
2021–2024 — Data Analyst, Никонова Групп
• Работа с rust, pytorch, pandas
• Опыт анализа данных и автоматизации

Навыки: rust, pytorch, pandas, python, c++, tableau, javascript, sklearn, linux
Образование: ООО «Беспалова Дроздова» Университет, Прикладная информатика
""", """Суханов Святополк Богданович
Email: sergeevaverjan@example.com
Телефон: 82755842999

Опыт работы:
2018–2024 — ML Engineer, ООО «Казакова»
• Работа с deep learning, pytorch, rust
• Опыт анализа данных и автоматизации

Навыки: deep learning, pytorch, rust, javascript, xgboost, python, pandas, powerbi, fastapi, sql
Образование: ОАО «Капустин-Гуляев» Университет, Прикладная информатика

""", """Полина Станиславовна Игнатова
Email: savingedeon@example.net
Телефон: +7 135 603 99 53

Опыт работы:
2018–2024 — ML Engineer, Корпорация Электросевкавмонтаж
• Работа с linux, go, fastapi
• Опыт анализа данных и автоматизации

Навыки: linux, go, fastapi, javascript, rust, pandas, python, sklearn, git, excel
Образование: НПО «Галкин, Кондратьев и Мельников» Университет, Прикладная информатика

"""]
labels = ["2021–2024 — ML Engineer, Навыки: sklearn, java, javascript, python, pandas, git",
          "2021–2024 — Data Analyst, Навыки: rust, pytorch, pandas, python, c++, tableau, javascript, sklearn, linux",
          "2018–2024 — ML Engineer, Навыки: deep learning, pytorch, rust, javascript, xgboost, python, pandas, powerbi, fastapi, sql",
          "2018–2024 — ML Engineer, Навыки: linux, go, fastapi, javascript, rust, pandas, python, sklearn, git, excel"]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.25, random_state=42)

# Vectorize text data using TF-IDF
vectorizer = TfidfVectorizer()
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

# Train a Naive Bayes classifier
classifier = MultinomialNB()
classifier.fit(X_train_vectorized, y_train)

# Make predictions
y_pred = classifier.predict(X_test_vectorized)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(classifier.predict(vectorizer.transform(["""Кулагин Корнил Федосеевич
Email: moiseevjaroslav@example.org
Телефон: 83585573742

Опыт работы:
2022–2024 — Data Analyst, Уральские локомотивы
• Работа с xgboost, go, rust
• Опыт анализа данных и автоматизации

Навыки: xgboost, go, rust, deep learning, javascript
Образование: ИП «Семенова, Макарова и Селиверстов» Университет, Прикладная информатика
"""])))