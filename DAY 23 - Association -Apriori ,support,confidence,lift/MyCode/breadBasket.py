"""
Code Challenge:
dataset: BreadBasket_DMS.csv

Q1. In this code challenge, you are given a dataset which has data and 
time wise transaction on a bakery retail store.
1. Draw the pie chart of top 15 selling items.
2. Find the associations of items where min support should be 0.0025, min_confidence=0.2, min_lift=3.
3. Out of given results sets, show only names of the associated item from given result row wise.

"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from apyori import apriori

dataset=pd.read_csv('BreadBasket_DMS.csv')
dataset['Item']=dataset['Item'].replace('NONE',np.nan)
dataset=dataset.dropna(axis=0)


#1
top_selling=dataset['Item'].value_counts()
values=top_selling.values[0:15]
items=top_selling.index[0:15]


plt.pie(values,(0.5,0,0,0,0,0,0,0,0,0,0,0,0,0,0),items)

#2
dataset=dataset.iloc[:,[2,3]]
listTransactions=[]

data=dataset.groupby('Transaction')['Item'].apply(list)
for i in data.index:
    listTransactions.append(data[i])

rules = apriori(listTransactions, min_support = 0.0025, min_confidence = 0.2, min_lift = 3)
results = list(rules)



for item in results:

    # first index of the inner list
    # Contains base item and add item
    pair = item[0] 
    items = [x for x in pair]
    print("Rule: " + items[0] + " -> " + items[1])

    #second index of the inner list
    print("Support: " + str(item[1]))

    #third index of the list located at 0th
    #of the third index of the inner list

    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")




    

