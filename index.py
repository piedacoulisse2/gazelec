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
#importer_donnee()
#st.write(df)
#data = df['Consommation brute électricité (MW) - RTE']
#x = df['Date']
#chart_data = pd.DataFrame(data=df['Consommation brute électricité (MW) - RTE'].values,index=df['Date'].values,columns=['Valeur électricité'])
#chart_data['valeurs gaz'] = df['Consommation brute gaz totale (MW PCS 0°C)'].values

#st.line_chart(chart_data)


from bokeh.plotting import figure

x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

p = figure(
     title='simple line example',
     x_axis_label='x',
     y_axis_label='y')

p.line(x, y)

fig = st.bokeh_chart(p)





