from fastapi import FastAPI, HTTPException
from fuzzywuzzy import fuzz
import uvicorn

app = FastAPI()
dizionario = []

PATH_OUTPUT = "C:\\Users\\utente17\\Desktop\\QuestIT_project_work\\task\\output\\output_fase003.csv"

@app.post("/carica_parola/{parola}")
async def carica_parola(parola: str):
    """
    API per caricare una parola nel dizionario.
    """
    if parola in dizionario:
        raise HTTPException(status_code=400, detail="La parola è già presente nel dizionario.")
    
    dizionario.append(parola)  # Inizializziamo il punteggio a 0
    return {"messaggio": "Parola caricata con successo nel dizionario"}

@app.post("/correggi_parola/{parola}")
async def correggi_parola(parola: str):

    if parola not in dizionario:
        raise HTTPException(status_code=404, detail="La parola non è nel dizionario.")
    
    res = {}

    for item in dizionario:
        score = fuzz.ratio(parola, item)
        if score >= 80: 
            res[item] = score

    return res

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
