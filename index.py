import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
from bokeh.plotting import figure

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
x = df['date']

chart_data = pd.DataFrame(
     df,
     columns=['Consommation brute électricité (MW) - RTE'])

st.line_chart(chart_data)
p = figure(
     title='simple line example',
     x_axis_label='x',
     y_axis_label='y')
p.line(x, data, legend='Trend', line_width=2)
st.bokeh_chart(p, use_container_width=True)

