import streamlit as st
import requests

st.title("🚀 Cold Email Automation Dashboard")

# Definiamo i segreti in modo sicuro
# Assicurati di averli impostati su Streamlit Cloud (Settings -> Secrets)
try:
    BASE_URL = st.secrets["BACKEND_URL"]
    AUTH_TOKEN = st.secrets["API_AUTH_TOKEN"]
except Exception:
    st.error("Errore: Segreti non configurati correttamente su Streamlit Cloud.")
    st.stop()

# Pulsante per verificare lo stato
if st.button("Verifica stato sistema"):
    try:
        response = requests.get(f"{BASE_URL}/health")
        if response.headers.get('Content-Type') == 'application/json':
            st.json(response.json())
        else:
            st.warning("Risposta non JSON:")
            st.text(response.text)
    except Exception as e:
        st.error(f"Errore nella connessione: {e}")

# Pulsante per avviare lo scrape
if st.button("Avvia Pipeline Scrape"):
    with st.spinner('Lavoro in corso...'):
        headers = {"Authorization": f"Bearer {AUTH_TOKEN}"}
        try:
            response = requests.post(f"{BASE_URL}/pipeline/scrape", headers=headers)
            if response.status_code == 200:
                st.success("Scrape avviato con successo!")
            else:
                st.error(f"Errore {response.status_code}: {response.text}")
        except Exception as e:
            st.error(f"Errore di rete: {e}")

# Input email
email = st.text_input("Inserisci email destinatario")
if st.button("Invia Email di Test"):
    st.write(f"Inviando email a {email}...")