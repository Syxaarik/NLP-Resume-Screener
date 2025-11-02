import re


def cleaner_text(text):
    text = text.lower()
    text = re.sub(r"\s+", ' ', text).strip()
    print(text)
