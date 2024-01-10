from fastapi import FastAPI, HTTPException
from fastapi.openapi.utils import get_openapi
from fastapi.responses import JSONResponse
from fastapi.openapi.docs import get_swagger_ui_html
from fuzzywuzzy import fuzz
from pydantic import BaseModel
import uvicorn

app = FastAPI()

dizionario = []

PATH_OUTPUT = "C:\\Users\\utente17\\Desktop\\QuestIT_project_work\\task\\output\\output_fase003.csv"


class Item(BaseModel):
    parola: str
    score: float
 
@app.get("/items/")
async def read_items() -> list[Item]:
    return [
        Item(parola="a", score=1)
    ]


@app.post("/carica_parola/{parola}")
async def carica_parola(parola: str):
    """
    API per caricare una parola nel dizionario.
    """
    if parola in dizionario:
        raise HTTPException(status_code=400, detail="La parola è già presente nel dizionario.")
    
    dizionario.append(parola)
    return {"messaggio": "Parola caricata con successo nel dizionario"}

@app.post("/correggi_parola/{parola}")
async def correggi_parola(parola: str):
    if parola not in dizionario:
        raise HTTPException(status_code=404, detail="La parola non è nel dizionario.")
    
    res = []
    
    for item in dizionario:
        score = fuzz.ratio(parola, item)
        if score >= 80: 
            res.append((item, score))

    return res
    

@app.get("/openapi.json")
def get_open_api_endpoint():
    custom_openapi = get_openapi(
        title="Custom Swagger Documentation",
        version="1.0.0",
        description="Questa è la documentazione personalizzata della mia API.",
        routes=app.routes,
    )
    return JSONResponse(content=custom_openapi)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

