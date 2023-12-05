from fuzzywuzzy import fuzz
import pandas as pd
import numpy as np

INPUT_FILE = "C:\\Users\\utente17\\Desktop\\QuestIT_project_work\\task\\file\\mispelled.csv"
DB_FILE = "C:\\Users\\utente17\\Desktop\\QuestIT_project_work\\task\\file\\icd10.csv"
PATH_OUTPUT= "C:\\Users\\utente17\\Desktop\\QuestIT_project_work\\task\\output"
PROCESSED_PATH="C:\\Users\\utente17\\Desktop\\QuestIT_project_work\\task\\file\\"

def split_row(df,column,path):
    words = df[column].str.split(expand=True).stack().unique()
# Convert the array of words into a DataFrame
    words_df = pd.DataFrame(words, columns=[column])
# Write the DataFrame to a new CSV file
    words_df.to_csv(path, index=False)
 
def main():

    df_1= pd.read_csv(INPUT_FILE, usecols=["Value"])
    df_2= pd.read_csv(DB_FILE, usecols=["DESCRIZIONE"])
    
    split_row(df_1,"Value",PROCESSED_PATH+"mispelled_splitted.csv")
    split_row(df_2,"DESCRIZIONE",PROCESSED_PATH+"icd10_splitted.csv")
    
    dataframecolumn = pd.read_csv(PROCESSED_PATH+"mispelled_splitted.csv",usecols=["Value"])
    dataframecolumn.columns = ['INPUT']
    compare = pd.read_csv(PROCESSED_PATH+"icd10_splitted.csv",usecols=["DESCRIZIONE"])
    compare.columns = ['OUTPUT']
    dataframecolumn['Key'] = 1
    compare['Key'] = 1
    combined_dataframe = dataframecolumn.merge(compare,on="Key",how="left")
    combined_dataframe = combined_dataframe[~(combined_dataframe.INPUT==combined_dataframe.compare)]
    
    def partial_match(x,y):
        return(fuzz.ratio(x,y))
    partial_match_vector = np.vectorize(partial_match)

    combined_dataframe['score']=partial_match_vector(combined_dataframe['INPUT'],combined_dataframe['OUTPUT'])
    combined_dataframe = combined_dataframe[combined_dataframe.score>=80]
    combined_dataframe.drop('Key', axis=1, inplace=True)
    combined_dataframe.to_csv(PATH_OUTPUT+"\\output.csv", index=False)

    max_scores_df = combined_dataframe.loc[combined_dataframe.groupby('INPUT')['score'].idxmax()]
    result_df = pd.merge(max_scores_df[['INPUT','OUTPUT','score']], combined_dataframe, on=['INPUT', 'OUTPUT', 'score'], how='inner')
    print(result_df)

if __name__ == "__main__":
    main()