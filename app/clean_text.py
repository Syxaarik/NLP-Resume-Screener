import re


def cleaner_text(text):
    text = text.lower()
    text = re.sub(r"[\d\+\-\(\)]+", ' ', text)  # удаляем номера
    text = re.sub(r"[^a-zа-яё\s]", ' ', text)  # убираем знаки
    text = re.sub(r"\s+", ' ', text).strip()
    print(text)
