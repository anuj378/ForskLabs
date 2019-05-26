
"""
Code Challenge 

import Automobile.csv file.

Using MatPlotLib create a PIE Chart of top 10 car makers according to the number 
of their cars and explode the largest car maker


"""
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('Automobile.csv')
rank=df['make'].value_counts()
make_names=rank.index[0:10]
make_counts=rank.values[0:10]
plt.pie(make_counts,(.35,0,0,0,0,0,0,0,0,0),make_names,['red','blue','green','yellow','orange','purple','pink','magenta','grey','violet'],autopct='%1.1f%%')
