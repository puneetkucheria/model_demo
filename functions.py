import streamlit as st
from pathlib import Path

def redirect():
    if st.session_state is None:
        redirect()

#/Users/puneetkucheria/projects/S3
def store_file_s3_foler(uploaded_file, save_folder = '/Users/puneetkucheria/projects/S3/model_demo_temp'):
    # save_folder = '/Users/puneetkucheria/projects/S3/model_demo_temp'
    save_path = Path(save_folder, uploaded_file.name)
    with open(save_path, mode='wb') as w:
        w.write(uploaded_file.getvalue())
    if save_path.exists():
        # save_path.unlink()
        return save_path
        # st.success(f'File {uploaded_file.name} is successfully saved!')

def del_file_s3_folder(save_path):
    if save_path.exists():
        save_path.unlink()