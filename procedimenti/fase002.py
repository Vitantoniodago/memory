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
    # elementi_da_elim = ['(2010)','(2012)']

    for i in range(1,170+1):
        url = SCRAPING_URL+str(i)+'/'
        print(f"Richiesta HTTP alla pagina {url}...")
        response = requests.get(url)
        # Verifica se la richiesta è andata a buon fine (status code 200)
        if response.status_code == 200:
            # Utilizza BeautifulSoup per analizzare il contenuto HTML della pagina
            soup = BeautifulSoup(response.text, 'html.parser')
            # Trova la tag div con classe "MuiStack-root css-hxp9p6"
            container_div = soup.find_all('div', class_='MuiStack-root css-hxp9p6')
            # stampa il numero di risultati trovati
            print(f"Numero di risultati trovati: {len(container_div)}")
            # Trova la tag a dentro la tag div
            links_with_specific_class = container_div[0].find_all('a')
            print(f"Numero di link trovati: {len(links_with_specific_class)}")
            # Itera attraverso i link e stampa il testo
            for link in links_with_specific_class:
                print(f'{i} / - {link.text} - ')
                # words = link.text.split()
                # append the link text to the list
                list.append(link.text)
            # print("Dati salvati nel file CSV.")
        else:
            print(f"Errore nella richiesta: {response.status_code}")

    # with open(PATH_OUTPUT, 'w', newline='', encoding='utf-8') as csvfile:
                # fieldnames = ['dizionario']
                # writer = csv.DictWriter(csvfile, fieldnames=fieldnames) 
                # # Scrivi l'intestazione
                # writer.writeheader()
                # # Scrivi le parole
                # for word in list:
                #     for elemento in elementi_da_elim:
                #         word = word.replace(elemento,"")
                #     writer.writerow({'dizionario': word})

    # Salva la lista in un file di testo, una parola per riga
    with open(PATH_OUTPUT, 'w', newline='', encoding='utf-8') as file:
        file.write('\n'.join(list))
    


if __name__ == "__main__":
    main()