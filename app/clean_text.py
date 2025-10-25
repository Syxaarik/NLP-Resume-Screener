import re

def cleaner_text(text):
    text = re.sub(r'\d', '', text)
    print(text)


cleaner_text(text)
