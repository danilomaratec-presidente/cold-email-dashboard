# Sostituisci il blocco del pulsante Scrape con questo:
if st.button("Avvia Pipeline Scrape"):
    with st.spinner('Lavoro in corso...'):
        # Usiamo i Secrets configurati su Streamlit Cloud
        headers = {"Authorization": f"Bearer {st.secrets['API_AUTH_TOKEN']}"}
        
        # Facciamo la chiamata passando gli headers di sicurezza
        response = requests.post(f"{st.secrets['BACKEND_URL']}/pipeline/scrape", headers=headers)
        
        if response.status_code == 200:
            st.success("Scrape avviato con successo!")
        else:
            # Mostriamo l'errore reale per capire cosa succede
            st.error(f"Errore durante l'avvio: {response.status_code} - {response.text}")