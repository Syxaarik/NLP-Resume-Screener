import os
import docx # txt = D:\\Python project\\Project\\DataScinse\\Banword\\data\\resumes\\resume_01.txt
from app.clean_text import cleaner_text # pdf = D:\Python project\Project\DataScinse\Banword\app\test.pdf
from PyPDF2 import PdfReader # docx = D:\Python project\Project\DataScinse\Banword\app\test.docx
from PyPDF2.errors import PdfReadError


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


def file_proc(file_path):
    filename, extension = os.path.splitext(file_path)
    print(extension)


    if extension == ".pdf":
        cleaner_text(extract_pdf_text(file_path))

    elif extension == ".txt":
        cleaner_text(extract_txt_text(file_path))

    elif extension == ".docx":
        cleaner_text(extract_docx_text(file_path))
    else:
        raise PdfReadError("File extension not supported")
