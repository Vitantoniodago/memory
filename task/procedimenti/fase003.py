import csv

INPUT_FILE = "C:\\Users\\utente17\\Desktop\\QuestIT_project_work\\task\\output\\output_fase002.csv"
PATH_OUTPUT = "C:\\Users\\utente17\\Desktop\\QuestIT_project_work\\task\\output\\output_fase003.csv"

def contiene_solo_lettere(testo):
    return all(carattere.isalpha() or carattere.isspace() for carattere in testo)

def filtra_righe_lettere(file_input, file_output):
    with open(file_input, 'r', newline='') as input_csv, open(file_output, 'w', newline='') as output_csv:
        lettore = csv.reader(input_csv)
        scrittore = csv.writer(output_csv)
        
        for riga in lettore:
            riga_filtrata = [colonna for colonna in riga if colonna.strip()]
            if riga_filtrata and all(contiene_solo_lettere(colonna) for colonna in riga_filtrata):
                scrittore.writerow(riga_filtrata)


file_input = INPUT_FILE
file_output = PATH_OUTPUT

filtra_righe_lettere(file_input, file_output)


