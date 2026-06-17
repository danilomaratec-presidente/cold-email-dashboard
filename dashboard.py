import streamlit as st
import requests

# L'URL del tuo servizio Cloud Run (quello che abbiamo ottenuto prima)
BASE_URL = "https://cold-email-agents-172583723475.europe-west1.run.app"

st.title("🚀 Cold Email Automation Dashboard")

# Pulsante per testare lo stato
if st.button("Verifica stato sistema"):
    response = requests.get(f"{BASE_URL}/health")
    st.json(response.json())

# Pulsante per far partire la pipeline (es. lo scrape)
if st.button("Avvia Pipeline Scrape"):
    with st.spinner('Lavoro in corso...'):
        # Qui chiamiamo il tuo endpoint reale
        response = requests.post(f"{BASE_URL}/pipeline/scrape")
        if response.status_code == 200:
            st.success("Scrape avviato con successo!")
        else:
            st.error("Errore durante l'avvio")

# Esempio di input per inviare un'email singola
email = st.text_input("Inserisci email destinatario")
if st.button("Invia Email di Test"):
    st.write(f"Inviando email a {email}...")
    # Qui chiameresti la tua rotta di invio