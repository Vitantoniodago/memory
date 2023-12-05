import csv

INPUT_FILE = "../output/output_fase002.csv"
PATH_OUTPUT = "../output/output_fase003.csv"

def contiene_solo_lettere(testo):
    # return all(carattere.isalpha() or carattere.isspace() for carattere in testo)
    return all(carattere.isalpha() for carattere in testo)

def filtra_righe_lettere(file_input, file_output):
    with open(file_input, 'r', encoding="utf-8") as input_csv, open(file_output, 'w', encoding="utf-8") as output_csv:
        lettore = csv.reader(input_csv)
        # scrittore = csv.writer(output_csv)
        
        for riga in lettore:
            stringa = str(riga[0])
            # riga_filtrata = [colonna for colonna in riga if colonna.strip()]
            # if riga_filtrata and all(contiene_solo_lettere(colonna) for colonna in riga_filtrata):
            #     scrittore.writerow(riga_filtrata)
            # elimina anno e parentesi (ad es. (2010))
            tonda = stringa.find('(')
            if tonda != -1:
                stringa = stringa[:tonda-1]
            print(f"{stringa} => {contiene_solo_lettere(stringa)}")
            if len(stringa) > 3 and contiene_solo_lettere(stringa):
                # scrittore.writerow(stringa)
                output_csv.write(stringa.upper()+'\n')


file_input = INPUT_FILE
file_output = PATH_OUTPUT

filtra_righe_lettere(file_input, file_output)


