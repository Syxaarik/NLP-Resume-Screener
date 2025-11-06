import streamlit as st
from src.pars_text import file_proc


st.title("Smart Resume Screener")
resume = st.file_uploader("Резюме:")
vacancy = st.file_uploader("Описание вакансии:")

print(resume)
print(vacancy)
# if st.button("Оценить"):
#     score = model.compare(resume, vacancy)
#     st.write("Совпадение:", score)
