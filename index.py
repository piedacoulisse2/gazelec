import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd


st.title('Application Elec gaz')

nom = 'Donnees/consommation-quotidienne-brute.csv'
lien = nom
df = pd.read_csv(lien, sep=";")

@st.cache  # 👈 Added this
def importer_donnee():

    df['date'] = pd.to_datetime(df['Date'])
    df['horodate'] = pd.to_datetime(df['Date - Heure']) # This makes the function take 2s to run

#graphique = df['horodate'] , df['Consommation brute électricité (MW) - RTE'], df['Consommation brute gaz totale (MW PCS 0°C)']

importer_donnee()

st.write(df)

with st.echo(code_location='below'):
    import plotly.express as px

    fig = px.scatter(
        x=df['horodate'],
        y=df['Consommation brute électricité (MW) - RTE'],
    )
    fig.update_layout(
        xaxis_title="horodate",
        yaxis_title="Consommation électrique",
    )

    st.write(fig)




