import streamlit as st
import altair as alt
import urllib
import requests
import http.client
import json
import pandas as pd
import seaborn as sns

@st.cache
def getToken_RTE():
    try:
        client_id = '299e8ff8-011b-4376-bc62-d2e08b1967fc'
        client_secret = 'd598bb8a-7080-4049-8de9-9a10018041f9'
        scope = ''
        url = 'https://digital.iservices.rte-france.com/token/oauth/'

        payload = 'grant_type=client_credentials&client_id=' + client_id + '&client_secret=' + client_secret
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        data = json.loads(response.text)
        sortie = data
    except:
        sortie = 'Erreur_Token'
        pass
    return sortie

@st.cache
def get_UN_data():
    #token = getToken_RTE()
    token = 'Lhb04hCBVjoxshq7tLzPxzQu9o8n1IWSRCY2OCF3Kr6wvGTsIbB7Vg'
    url = "https://digital.iservices.rte-france.com/open_api/actual_generation/v1/actual_generations_per_production_type"
    payload = {}
    headers = {
        'Authorization': 'Bearer '+token
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    return response

def valeur():
    adresse = 'C:\\Users\\4799XA\\Desktop\\response.json'
    dataF = pd.read_json(adresse)
    return dataF


c = pd.read_json(get_UN_data().text)
df = pd.DataFrame(c['actual_generations_per_production_type'])
c['actual_generations_per_production_type'][1]['production_type']

z = []
c.size

for i in range(c.size-1):
    i
    c['actual_generations_per_production_type'][i]['production_type']
    z.append(c['actual_generations_per_production_type'][i]['production_type'])
z
df
#df['production'] = z[:df['value'].size]

st.bar_chart(data=df['value'])

#sns.barplot(x='production', y='value', data=df)

