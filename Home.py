import streamlit as st
import sqlite3
from PIL import Image

conn = sqlite3.connect('demo.db')
st.session_state['s3-path'] = "../S3/demo_model"


st.markdown(
    """
    # Home Page
    ## This is Domain for all the demos
    """
)

with st.form(key="Form :", clear_on_submit = True):
    name = st.text_input("Enter host address", "localhost")
    # uploaded_file = st.file_uploader("Choose a PDF file",)
    Submit = st.form_submit_button(label='Submit')

if Submit:
    #update yaml configuration file with new host
    conn.execute("UPDATE config SET host = ? WHERE id = 1", (name))
    st.write('Data updated successfully')