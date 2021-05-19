import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
import time
from ethnicolr import census_ln
import os
### Data URL



"""
# Run Race-Ethnicity Imputation Model
A tool to generate predicted race and ethnicity based on last name information.
"""
uploaded_files = st.file_uploader("Upload CSV", type="csv")


if uploaded_files:
    file_upload_path = 'src/' + uploaded_files.name
    upr = pd.read_csv(file_upload_path)

    st.table(upr.head())

"""
### Run Imputation Model
Click the button to run the imputation model, display output, and save results.
"""

imp_button = st.button('Run Imputation Model')


if imp_button:

    pred_name = census_ln(upr, 'last_name')
    with st.spinner('Model is Running'):
        time.sleep(3)
    #print(help(ethnicolr))
    st.table(pred_name.head())
    st.write('Imputation model results have been saved.')
    pred_name.to_csv('src/model_output.csv')












