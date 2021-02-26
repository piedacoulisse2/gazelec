import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd


st.title('Application Elec gaz')
df = pd.DataFrame()

@st.cache  # 👈 Added this
def importer_donnee():
    nom = 'Donnees/consommation-quotidienne-brute.csv'
    lien = nom
    df = pd.read_csv(lien, sep=";")
    df['date'] = pd.to_datetime(df['Date'])
    df['horodate'] = pd.to_datetime(df['Date - Heure']) # This makes the function take 2s to run

importer_donnee()

st.write(df)



