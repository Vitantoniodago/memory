from fuzzywuzzy import fuzz
import pandas as pd
import numpy as np

INPUT_PATH = "C:\\Users\\utente17\\Desktop\\QuestIT_project_work\\task\\output\\"
PATH_OUTPUT = "C:\\Users\\utente17\\Desktop\\QuestIT_project_work\\task\\output\\output_fase004.csv"

dataframecolumn= pd.read_csv(INPUT_PATH+'mispelled_fase001.csv')
compare= pd.read_csv(INPUT_PATH+'mispelled_fase001.csv',usecols=["Corretto"])
compare.columns = ['Compare_corretto']
dataframecolumn['Key'] = 1
compare['Key'] = 1
combined_dataframe = dataframecolumn.merge(compare,on="Key",how="left")
combined_dataframe = combined_dataframe[~(combined_dataframe.Value==combined_dataframe.Compare_corretto)]
    
def partial_match(x,y):
        return(fuzz.ratio(x,y))
partial_match_vector = np.vectorize(partial_match)

combined_dataframe['score']=partial_match_vector(combined_dataframe['Value'],combined_dataframe['Compare_corretto'])
combined_dataframe = combined_dataframe[combined_dataframe.score>=80]

#----------------------------------------------------------------------------------------------
compare2= pd.read_csv(INPUT_PATH+'output_fase003.csv')
compare2.columns = ['Compare_dict']
compare2['Key'] = 1
dataframe = combined_dataframe.merge(compare2,on="Key",how="left")
dataframe = dataframe[~(dataframe.Value==dataframe.Compare_dict)]
    

dataframe['final_score']=partial_match_vector(dataframe['Value'],dataframe['Compare_dict'])
dataframe = dataframe[dataframe.final_score>=80]

dataframe.to_csv(PATH_OUTPUT, index=False)



