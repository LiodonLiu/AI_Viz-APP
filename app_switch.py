import streamlit as st
import os

def run():
    os.system(f'streamlit run app_api.py')

if st.button('use'):
  run()
