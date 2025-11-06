import streamlit as st
from src.pars_text import file_proc
from sentence_transformers import SentenceTransformer, util


def app_model(resumes, vacancies):
    model = SentenceTransformer('all-MiniLM-L6-v2')

    emb_resume = model.encode(resumes, convert_to_tensor=True)
    emb_vacancy = model.encode(vacancy, convert_to_tensor=True)

    similarity = util.pytorch_cos_sim(emb_resume, emb_vacancy)
    return f"{similarity.item():.4f}"


st.title("Smart Resume Screener")
resume = st.file_uploader("Резюме:")
vacancy = st.file_uploader("Описание вакансии:")

print(resume)
print(vacancy)
# if st.button("Оценить"):
#     score = model.compare(resume, vacancy)
#     st.write("Совпадение:", score)
