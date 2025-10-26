import os
import docx
from app.clean_text import cleaner_text
from PyPDF2 import PdfReader
from PyPDF2.errors import PdfReadError

text_path = input(
    "Enter the path:")  # txt = D:\\Python project\\Project\\DataScinse\\Banword\\data\\resumes\\resume_01.txt
filename, file_extension = os.path.splitext(
    text_path)  # pdf = D:\Python project\Project\DataScinse\Banword\app\test.pdf
print(file_extension)  # docx = D:\Python project\Project\DataScinse\Banword\app\test.docx


def extract_pdf_text(path):
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text


def extract_txt_text(path):
    with open(path, 'r', encoding='utf-8') as file:
        return file.read()


def extract_docx_text(path):
    doc = docx.Document(path)
    full_text = [para.text for para in doc.paragraphs]
    return '\n'.join(full_text)


if file_extension == ".pdf":
    print("Текст до обработки:")
    print(extract_pdf_text(text_path))
    print("Текст после обработки:")
    cleaner_text(extract_pdf_text(text_path))

elif file_extension == ".txt":
    print("Текст до обработки:")
    print(extract_txt_text(text_path))
    print("Текст после обработки:")
    cleaner_text(extract_txt_text(text_path))

elif file_extension == ".docx":
    print("Текст до обработки:")
    print(extract_docx_text(text_path))
    print("Текст после обработки:")
    cleaner_text(extract_docx_text(text_path))

else:
    raise PdfReadError("File extension not supported")
