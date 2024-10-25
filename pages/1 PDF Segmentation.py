import streamlit as st
import requests
from functions import store_file_s3_folder

if 's3-path' not in st.session_state:
    # st.switch_page("../home.py")
    st.switch_page("./home.py")

#check status of api
try:
    response = requests.get("http://127.0.0.1:8000").json()
    st.success(response['state'])
except:
    st.error('api is not running')

# import requests
st.write("## Check pdf's for digital or non-digital pages")
# st.write(st.session_state['s3-path'])

uploaded_file = None
# uploaded_file.name = {'name':''}

if uploaded_file is None:
    with st.form(key="Form :", clear_on_submit = True):
        # st.info('Please upload a file')
        uploaded_file = st.file_uploader("Choose a PDF file",type=['pdf'])
        Submit = st.form_submit_button(label='Submit')

if Submit and uploaded_file is not None:
    store_path = store_file_s3_folder(uploaded_file, save_folder='pdf_seg')
    st.success(f'File {store_path} is successfully saved!')
    response = requests.post(f"http://127.0.0.1:8000/dnc?file_path="+str(store_path))
    st.success(response.text)

