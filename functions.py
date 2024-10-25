import streamlit as st
from pathlib import Path
import os

def redirect():
    if st.session_state is None:
        redirect()

s3_path = '/Users/puneetkucheria/projects/S3/'

def store_file_s3_folder(uploaded_file, save_folder = 'model_demo_temp'):
    # save_folder = '/Users/puneetkucheria/projects/S3/model_demo_temp'
    folder_path = Path(s3_path, save_folder)
    save_path = Path(s3_path , save_folder, uploaded_file.name)
    print(save_path)
    
    try:
        os.makedirs(folder_path)
    except FileExistsError:
        # directory already exists
        pass

    with open(save_path, mode='wb') as w:
        w.write(uploaded_file.getvalue())
    if save_path.exists():
        # save_path.unlink()
        return save_path
        # st.success(f'File {uploaded_file.name} is successfully saved!')

def del_file_s3_folder(save_path):
    if save_path.exists():
        save_path.unlink()