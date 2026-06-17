# Sostituisci il blocco del bottone "Verifica stato sistema" con questo:
if st.button("Verifica stato sistema"):
    if BASE_URL:
        try:
            response = requests.get(f"{BASE_URL}/health")
            # Controlliamo prima se la risposta contiene JSON valido
            if response.headers.get('Content-Type') == 'application/json':
                st.json(response.json())
            else:
                # Se non è JSON, mostriamo il testo grezzo per capire cosa succede
                st.warning("Risposta non in formato JSON:")
                st.text(response.text)
        except Exception as e:
            st.error(f"Errore nella connessione: {e}")