"""

Code Challenge:
Datset: Market_Basket_Optimization.csv

Q2. In today's demo sesssion, we did not handle the null values before fitting
 the data to model, remove the null values from each row and perform the associations 
 once again.
Also draw the bar chart of top 10 edibles.
"""
import numpy as np
import pandas as pd
from apyori import apriori
import matplotlib.pyplot as plt

# Data Preprocessing
dataset = pd.read_csv('Market_Basket_Optimisation.csv', header = None)
transactions = []
for i in range(0,dataset.shape[0]):
    sub_list = list(set(dataset.iloc[i,:]))
    if i!=0:
        sub_list.remove(np.nan)
    transactions.append(sub_list)
        
    
"""
a = list(set(dataset.iloc[3,:]))
a.remove(np.nan)

a=dnum.iloc[0,:]=list(dnum.iloc[0,:].apply(lambda x:1))
"""

"""
for i in range(0, 7501):
    #transactions.append(str(dataset.iloc[i,:].values)) #need to check this one
    for j in range()
    transactions.append([str(dataset.values[i,j]) for j in range(0, 20)])
    
"""
# Training Apriori on the dataset

rules = apriori(transactions, min_support = 0.003, min_confidence = 0.25, min_lift = 4)

# Visualising the results
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
    


"""
objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
performance = [10,8,6,4,2,1]
 
plt.bar([0,1,2,3,4,5], performance, align='center', alpha=1.0)
plt.xticks([0,1,2,3,4,5], objects)
plt.ylabel('Usage')
plt.title('Programming Language Usage')
 
plt.show()
"""