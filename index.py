import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

st.title('Application Elec gaz')

nom = 'Donnees/consommation-quotidienne-brute.csv'
lien = nom
df = pd.read_csv(lien, sep=";")

@st.cache
def importer_donnee():

    df['date'] = pd.to_datetime(df['Date'])
    df['horodate'] = pd.to_datetime(df['Date - Heure']) # This makes the function take 2s to run

#graphique = df['horodate'] , df['Consommation brute électricité (MW) - RTE'], df['Consommation brute gaz totale (MW PCS 0°C)']

importer_donnee()

#st.write(df)

data = df['Consommation brute électricité (MW) - RTE']

st.line_chart(y=data,x=df['date'])
