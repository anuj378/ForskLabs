# -*- coding: utf-8 -*-
"""
Q3. Code Challenge -
Data: "data.csv"

This data is provided by The Metropolitan Museum of Art Open Access
1. Visualize the various countries from where the artworks are coming.
2. Visualize the top 2 classification for the artworks
3. Visualize the artist interested in the artworks
4. Visualize the top 2 culture for the artworks

"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset=pd.read_csv("data.csv")

filtered_dataset=None
for i in list(dataset.columns):
    if( dataset[i].isnull().all()):
        print(i)
        dataset=dataset.drop(i,axis=1)


#1
country_names=dataset.Country
country_names=country_names.dropna()
names=country_names.value_counts().index
counts=country_names.value_counts().values
plt.bar(names,counts)
plt.xticks(names,fontsize=5,rotation=90)
plt.savefig("Bar_of_countries.jpeg")


#2
classes=((dataset['Classification'].value_counts())).index
classes=classes[:2]
counts_classes=(dataset['Classification'].value_counts()).values
counts_classes=counts_classes[:2]
plt.pie(counts_classes,(0,0),classes,autopct='%1.2f%%')


#3
object_names=dataset['Object Name']
object_names=object_names.dropna()
names=object_names.value_counts().index[0:10]
counts=object_names.value_counts().values[0:10]
#plt.bar(names,counts)
plt.pie(counts,labels=names,autopct='%1.2f%%',radius=1.5)
#plt.xticks(names,fontsize=5,rotation=90)
plt.savefig("Items_interested.jpeg")

#4
classes=((dataset['Culture'].value_counts())).index
classes=classes[:2]
counts_classes=(dataset['Culture'].value_counts()).values
counts_classes=counts_classes[:2]





plt.pie(counts_classes,(0,0),classes,autopct='%1.2f%%')





