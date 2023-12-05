import requests
from bs4 import BeautifulSoup
import csv
from io import StringIO
SCRAPING_URL = 'https://www.treccani.it/enciclopedia/elenco-opere/Dizionario_di_Medicina/'
PATH_OUTPUT = "C:\\Users\\utente17\\Desktop\\QuestIT_project_work\\task\\output\\output_fase002.csv"
def main():
    # Effettua la richiesta HTTP alla pagina
    response = requests.get(SCRAPING_URL)
    i = 1
    list = []
    elementi_da_elim = ['(2010)','(2012)']
    while(i <= 170):
        response = requests.get(SCRAPING_URL+str(i)+'/')
        # Verifica se la richiesta è andata a buon fine (status code 200)
        if response.status_code == 200:
            # Utilizza BeautifulSoup per analizzare il contenuto HTML della pagina
            soup = BeautifulSoup(response.text, 'html.parser')
                    # Trova tutti i tag <a> con una classe specifica
            links_with_specific_class = soup.find_all('div', class_='MuiStack-root css-hxp9p6')
            # Itera attraverso i link e stampa il testo
            for link in links_with_specific_class:
                words = link.text.split()
                list.extend(words)
            print("Dati salvati nel file CSV.")
        else:
            print(f"Errore nella richiesta: {response.status_code}")
        i = i+1
    with open(PATH_OUTPUT, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['dizionario']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames) 
                # Scrivi l'intestazione
                writer.writeheader()
                # Scrivi le parole
                for word in list:
                    for elemento in elementi_da_elim:
                        word = word.replace(elemento,"")
                    writer.writerow({'dizionario': word})

if __name__ == "__main__":
    main()