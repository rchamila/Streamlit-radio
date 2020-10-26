import streamlit as st
import random


with open("main.css") as f:
    st.markdown(f"""<style>{f.read()}</style>""",unsafe_allow_html=True)


st.title("Radio button group with no selection by default")
st.radio("Choose a number.", list(range(5)))