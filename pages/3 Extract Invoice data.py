import streamlit as st
import requests


#check status of api
try:
    response = requests.get("http://127.0.0.1:8002").json()
    st.success(response['state'])
except:
    st.error('api is not running')

st.write("this is model one")