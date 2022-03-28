import streamlit as st
import prediction


st.set_page_config(
    page_title="Crack Surface Detection",
    page_icon="🔨",
    layout="wide",
    initial_sidebar_state='expanded',
    menu_items={
          "Get Help": "https://www.linkedin.com/in/kevin-giovanni-pradana-50aa61145/",
          "Report a bug": "https://github.com/KevinGiovanniP",
          "About": "### Surface Crack Detection - Kevin Giovanni Pradana",
    },

)



PAGES = {"Prediction": prediction}


st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Choose pages", list(PAGES.keys()))

page = PAGES[page]
page.app()