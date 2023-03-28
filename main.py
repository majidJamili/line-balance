import math
import pandas as pd
import numpy as np


def weld_data():    
    df = pd.read_csv('plateBoatsData.csv')
    df['planned ETA'] = pd.to_datetime(df['planned ETA'] )    
    col_name = pd.DataFrame(df.columns.values, columns=["workcenters"])
    col_select = col_name.iloc[[0,1,5,6,8,15,16,17, 21,22,23,24,25,26,27,28,29,32,36,37,38,39,40,44,45,46,48,49,50,51,52,54,55,56,57,58,62,63,64],]
    col_select_list = col_select['workcenters'].tolist()
    return df[col_select_list]

data = weld_data()

print(data.describe().to_csv('data.csv'))


#print( df[['boat name', 'WELD1', 'WELD2', 'WELD3', 'WELD4', 'WeldPartsD']].value_counts())
#print(df[['boat name','hullstack','weldpartsassembly','weldpartsbowriderplateWPbunks', 'WELD1', 'WELD2', 'WELD3', 'WELD4', 'WeldPartsD', 'prepaintclean']].describe())


