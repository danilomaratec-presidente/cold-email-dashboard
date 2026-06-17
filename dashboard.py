import streamlit as st
import requests

st.title("🚀 Cold Email Automation Dashboard")

# Funzione per ottenere l'URL e il Token in modo sicuro
def get_secrets():
    try:
        url = st.secrets["BACKEND_URL"]
        token = st.secrets["API_AUTH_TOKEN"]
        return url, token
    except Exception as e:
        st.error("Configurazione Segreti mancante su Streamlit Cloud!")
        return None, None

BASE_URL, AUTH_TOKEN = get_secrets()

# Pulsante per testare lo stato
if st.button("Verifica stato sistema"):
    if BASE_URL:
        response = requests.get(f"{BASE_URL}/health")
        st.json(response.json())

# Pulsante per far partire la pipeline
if st.button("Avvia Pipeline Scrape"):
    if BASE_URL and AUTH_TOKEN:
        with st.spinner('Lavoro in corso...'):
            headers = {"Authorization": f"Bearer {AUTH_TOKEN}"}
            response = requests.post(f"{BASE_URL}/pipeline/scrape", headers=headers)
            
            if response.status_code == 200:
                st.success("Scrape avviato con successo!")
            else:
                st.error(f"Errore: {response.status_code} - {response.text}")

# Input email
email = st.text_input("Inserisci email destinatario")
if st.button("Invia Email di Test"):
    st.write(f"Inviando email a {email}...")