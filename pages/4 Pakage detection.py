import streamlit as st
import requests
from functions import store_file_s3_folder
from PIL import Image

if 's3-path' not in st.session_state:
    # st.switch_page("../home.py")
    st.switch_page("./home.py")

#check status of api
try:
    response = requests.get("http://127.0.0.1:8003").json()
    st.success(response['state'])
except:
    st.error('api is not running')

# import requests
st.write("## Find delivery package in the given image")
# st.write(st.session_state['s3-path'])

uploaded_file = None
# uploaded_file.name = {'name':''}

if uploaded_file is None:
    with st.form(key="Form :", clear_on_submit = True):
        # st.info('Please upload a file')
        uploaded_file = st.file_uploader("Choose a JPEG Image file", type=['png', 'jpg', 'jpeg'])
        Submit = st.form_submit_button(label='Submit')

if Submit and uploaded_file is not None:
    # store_path = store_file_s3_foler(uploaded_file._file_urls.upload_url)
    store_path = store_file_s3_folder(uploaded_file)
    st.success(f'File {store_path} is successfully saved!')
    # response = requests.post(f"http://127.0.0.1:8000/pkg_detect?file="+str(uploaded_file._file_urls.upload_url))
    response = requests.post("http://127.0.0.1:8003/pkg_detect?file="+str(store_path))
    st.success(response.text)
    st.image(str(store_path))
    st.image(response.text.replace('"',''))
    # image_bi = Image.open(response.text)
    # st.image(image_bi)
    # st.image("runs/detect/predict13/File 00009.jpg")
    # st.success(uploaded_file._file_urls.upload_url)