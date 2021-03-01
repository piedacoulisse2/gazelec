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

st.write(df)

x=df['horodate']
y=df['Consommation brute électricité (MW) - RTE']

data = df['Consommation brute électricité (MW) - RTE']

st.write("Conso RTE", data.sort_index())

chart = (
    alt.Chart(data)
    .mark_area(opacity=0.3)
    .encode(
        x="year:T",
        y=alt.Y("Gross Agricultural Product ($B):Q", stack=None),
        color="Region:N",
    )
)
st.altair_chart(chart, use_container_width=True)

