# tests/test_main_script.py
from fastapi.testclient import TestClient
from fase005 import app

client = TestClient(app)

def test_carica_parola():
    # Test caso di successo
    response = client.post("/carica_parola/nuova_parola")
    assert response.status_code == 200
    assert response.json() == {"messaggio": "Parola caricata con successo nel dizionario"}

    # Test caso di errore (parola già presente)
    response = client.post("/carica_parola/nuova_parola")
    assert response.status_code == 400
    assert response.json() == {"detail": "La parola è già presente nel dizionario."}

def test_correggi_parola():
    # Prima, carichiamo una parola nel dizionario
    client.post("/carica_parola/parola_di_test")

    # Test caso di successo
    response = client.post("/correggi_parola/parola_di_test")
    assert response.status_code == 200
    assert response.json() == {"parola_di_test": 100}  # Poiché la stessa parola ha score al 100%

    # Test caso di errore (parola non presente)
    response = client.post("/correggi_parola/parola_non_presente")
    assert response.status_code == 404
    assert response.json() == {"detail": "La parola non è nel dizionario."}
