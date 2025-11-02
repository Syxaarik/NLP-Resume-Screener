import streamlit as st
st.title("Smart Resume Screener")
resume = st.text_area("Резюме:")
vacancy = st.text_area("Описание вакансии:")
print(resume)
print(vacancy)
# if st.button("Оценить"):
#     score = model.compare(resume, vacancy)
#     st.write("Совпадение:", score)
