import pandas as pd
d=pd.read_excel('data_DJA.csv.xlsx',header=None)
d.columns=['n','y']
d['n'].value_counts()
