import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd


import seaborn as sns


st.title('Application Elec gaz')

adresse ='C:\\Users\\4799XA\\OneDrive\\CODE\\gazelec\\Donnees\\'
nom ='consommation-quotidienne-brute.csv'
lien = adresse + nom

df = pd.read_csv(lien,sep=";")
df['date'] = pd.to_datetime(df['Date'])
df['horodate'] = pd.to_datetime(df['Date - Heure'])


st.write(df)



