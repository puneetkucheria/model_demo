import streamlit as st
import requests
st.write("## this is model one")
st.write(st.session_state['s3-path'])

uploaded_file = st.file_uploader("Choose a PDF file")
if uploaded_file is not None:
    # To read file as bytes:
    # bytes_data = uploaded_file.getbuffer()
    
    # resp = requests()
    st.write(bytes_data)