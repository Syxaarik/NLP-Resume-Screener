import os
import docx
from PyPDF2 import PdfReader
from PyPDF2.errors import PdfReadError

text_path = input("Enter the path:")  # txt = D:\\Python project\\Project\\DataScinse\\Banword\\data\\resumes\\resume_01.txt
filename, file_extension = os.path.splitext(text_path) # pdf = D:\Python project\Project\DataScinse\Banword\app\test.pdf
print(file_extension) # docx = D:\Python project\Project\DataScinse\Banword\app\test.docx

def extract_pdf_text(path):
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    print(text)


def extract_txt_text(path):
    with open(path, 'r', encoding='utf-8') as file:
        print(file.readlines())


def extract_docx_text(path):
    doc = docx.Document(path)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    print('\n'.join(full_text))


if file_extension == ".pdf":
    extract_pdf_text(text_path)
elif file_extension == ".txt":
    extract_txt_text(text_path)
elif file_extension == ".docx":
    extract_docx_text(text_path)
else:
    raise PdfReadError("File extension not supported")
