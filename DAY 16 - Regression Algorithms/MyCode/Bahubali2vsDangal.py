

"""
Code Challenge: Simple Linear Regression

  Name: 
    Box Office Collection Prediction Tool
  Filename: 
    Bahubali2vsDangal.py
  Dataset:
    Bahubali2vsDangal.csv
  Problem Statement:
    It contains Data of Day wise collections of the movies Bahubali 2 and Dangal 
    (in crores) for the first 9 days.
    
    Now, you have to write a python code to predict which movie would collect 
    more on the 10th day.
  Hint:
    First Approach - Create two models, one for Bahubali and another for Dangal
    Second Approach - Create one model with two labels
"""
import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt

dataset=pd.read_csv('Bahubali2_vs_Dangal.csv')

features = dataset.iloc[:, :-2].values  
labels = dataset.iloc[:, 1:].values 


from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(features, labels) 

day=int(input("What is the day number?"))
money_made=regressor.predict(np.array(day).reshape(1,1))

if money_made[0][0]>money_made[0][1]:
    print("Bahubali earned more i.e.  {}".format(money_made[0][0]))
else:
    print("Dangal earned more i.e.  {}".format(money_made[0][1]))

