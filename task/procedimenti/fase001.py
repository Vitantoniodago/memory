import pandas as pd
import numpy as np

INPUT_FILE = "../file/mispelled.csv"
PATH_OUTPUT="../output/mispelled_fase001.csv"

# def split_rows_and_check(df,column1,column2,path):
#     words = df[column1].str.split(expand=True).stack().unique()
# # Convert the array of words into a DataFrame
#     df1 = pd.DataFrame(words, columns=[column1])
# # Write the DataFrame to a new CSV file
#     words = df[column2].str.split(expand=True).stack().unique()
# # Convert the array of words into a DataFrame
#     df2 = pd.DataFrame(words, columns=[column2])
# # Write the DataFrame to a new CSV file
#     concatenated_df = pd.concat([df1, df2], axis=1) #concatena il db
#     concatenated_df.to_csv(path, index=False)
#     if concatenated_df[['Value', 'Corretto']].isnull().any().any():
#         print("Il DataFrame contiene valori nulli.")
#     else:
#         mapping_df = pd.DataFrame({'Index': range(1, len(words_column1) + 1),
#                                    column1: words_column1,
#                                    column2: words_column2})
#         # Salva il DataFrame con la mappatura in un nuovo file CSV
#         mapping_df.to_csv(output_path, index=False)
# df= pd.read_csv(INPUT_FILE)    
# columns_to_load = ['Value', 'Corretto']
# multiple_columns_df = df[columns_to_load]

# split_rows_and_check(multiple_columns_df,'Value','Corretto',PATH_OUTPUT)



# Supponendo che df sia il DataFrame originale
df = pd.read_csv(INPUT_FILE)

# Seleziona le colonne 'Value' e 'Corretto'
# columns_to_load = ['Value', 'Corretto']
multiple_columns_df = df #[columns_to_load]

# Aggiungi una terza colonna come indice (ad esempio, 'Nuovo_Indice')
multiple_columns_df['Nuovo_Indice'] = range(1, len(multiple_columns_df) + 1)

# Aggiungi una colonna contenente il numero di caratteri di spazio nella colonna 'Value'
multiple_columns_df['Spazi_in_Value'] = multiple_columns_df['Value'].apply(lambda x: x.count(' '))

# Aggiungi una colonna contenente il numero di caratteri di spazio nella colonna 'Corretto'
multiple_columns_df['Spazi_in_Corretto'] = multiple_columns_df['Corretto'].apply(lambda x: x.count(' '))

# Filtra le righe con un conteggio uguale tra 'Spazi_in_Value' e 'Spazi_in_Corretto'
righe_con_conteggio_uguale = multiple_columns_df.query('Spazi_in_Value == Spazi_in_Corretto')

# Stampa il DataFrame filtrato
print(righe_con_conteggio_uguale)

# crea un nuovo dataframe vuoto con le stesse colonne di df
new_df = pd.DataFrame(columns=df.columns)
# aggiungici una colonna IndiceParola
new_df['IndiceParola'] = np.nan

# per ogni riga del dataframe
for index, row in righe_con_conteggio_uguale.iterrows():
    # esegui lo split di Value e Corretto, e crea due liste
    value_words = row['Value'].split()
    corretto_words = row['Corretto'].split()
    # se le due liste hanno lunghezza diversa, stampa un messaggio di errore
    if len(value_words) != len(corretto_words):
        print("Errore: le due liste hanno lunghezza diversa")
        continue
    # per ogni parola delle due liste duplica la colonna row in next_row
    for i in range(len(value_words)):
        # se le parole sono brevi (lunghezza <= 3) escludile
        if len(value_words[i]) <= 3 or len(corretto_words[i]) <= 3:
            print("Errore: le parole sono brevi")
            continue
        # crea un nuovo dataframe vuoto con le stesse colonne di df e una riga
        next_row_df = pd.DataFrame(columns=df.columns, index=[0])
        # copia i valori della riga originale
        next_row_df = next_row_df.fillna(row)
        # sulla riga appena creata, imposta IndiceParola uguale all'indice della parola nella lista, Value e Corretto alla Iesima parola della lista
        next_row_df['IndiceParola'] = i
        next_row_df['Value'] = value_words[i]
        next_row_df['Corretto'] = corretto_words[i]
        # aggiungi la riga al nuovo dataframe (la riga è una serie  pandas)
        new_df = pd.concat([new_df, next_row_df])
        
# cancella le colonne Spazi_in_Value e Spazi_in_Corretto, parte_non_relavata, Nuovo_Indice da new_df
new_df = new_df.drop(['Spazi_in_Value', 'Spazi_in_Corretto', 'parte_non_relavata', 'Nuovo_Indice'], axis=1)
# IndiceParola deve essere di tipo int
new_df['IndiceParola'] = new_df['IndiceParola'].astype(int)
        
# Stampa il nuovo dataframe
print(new_df)

# salva il file in PATH_OUTPUT
new_df.to_csv(PATH_OUTPUT, index=False)    



