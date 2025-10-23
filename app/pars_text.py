from PyPDF2 import PdfReader


def extract_text(path):
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text
print(extract_text("D:\\Python project\\Project\\DataScinse\\Banword\\app\\test.pdf"))