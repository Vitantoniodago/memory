import pandas as pd
import numpy as np

INPUT_FILE = "C:\\Users\\utente17\\Desktop\\QuestIT_project_work\\task\\file\\mispelled.csv"
PATH_OUTPUT="C:\\Users\\utente17\\Desktop\\QuestIT_project_work\\task\\output\\mispelled_fase001.csv"

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
columns_to_load = ['Value', 'Corretto']
multiple_columns_df = df[columns_to_load]

# Aggiungi una terza colonna come indice (ad esempio, 'Nuovo_Indice')
multiple_columns_df['Nuovo_Indice'] = range(1, len(multiple_columns_df) + 1)

# Aggiungi una colonna contenente il numero di caratteri di spazio nella colonna 'Value'
multiple_columns_df['Spazi_in_Value'] = multiple_columns_df['Value'].apply(lambda x: x.count(' '))

# Aggiungi una colonna contenente il numero di caratteri di spazio nella colonna 'Corretto'
multiple_columns_df['Spazi_in_Corretto'] = multiple_columns_df['Corretto'].apply(lambda x: x.count(' '))

# Filtra le righe con un conteggio diverso tra 'Spazi_in_Value' e 'Spazi_in_Corretto'
righe_con_conteggio_diverso = multiple_columns_df.query('Spazi_in_Value != Spazi_in_Corretto')

# Stampa il DataFrame filtrato
print(righe_con_conteggio_diverso)




