import pandas as pd
import numpy as np
def assign_Genre_values(df):
    p_values=df.to_list()
    #Converting p_values to set so that we get the core types of genre present on it.
    p_values=set(p_values)
    p_values=list(p_values)

    #Here we are creating dictionary to map the genre with corresponding key value.
    dictionary={}
    count=0
    for value in p_values:
        dictionary[value]=count
        count+=1
    
    # mapping the dataframe with their corresponding numerical value so that it can be processed easily 
    for index in range(0,df.shape[0]):
        try:
            if df[index] in dict.keys(dictionary):
                df[index]=dictionary[df[index]]
        except:
            pass
    return df

def construct_proper_dataframe():
    df=pd.read_csv('Dataset.csv')
    df.columns=['S.N','Movie','P_Genre','S_Genre','T_Genre']
    df['Movie']=df['Movie'].str.lower()

    #Now Lets remove the duplicaes with df.drop_duplicates
    df.drop_duplicates(subset ="Movie",keep='first',inplace=True)

    #Lets remove double space between words
    df['Movie']=df['Movie'].str.replace("  "," ")
    #dropping irrelevant parts of the dataframe.
    df=df.drop(['S.N'],axis=1)
    df=df.reset_index(inplace=False)
    Genres=['P_Genre','S_Genre','T_Genre']
    for Genre in Genres:
        df[Genre]=assign_Genre_values(df[Genre])
    
    return df

def pre_process_all():
    df=pd.DataFrame()
    df=construct_proper_dataframe()
    #print(df.head(50))
    return df


#This is for testing purpose comment the function call whn not using
#pre_process_all()