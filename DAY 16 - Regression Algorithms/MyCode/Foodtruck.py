"""
Code Challenge: Simple Linear Regression
  Name: 
    Food Truck Profit Prediction Tool
  Filename: 
    Foodtruck.py
  Dataset:
    Foodtruck.csv
  Problem Statement:
    Suppose you are the CEO of a restaurant franchise and are considering 
    different cities for opening a new outlet. 
    
    The chain already has food-trucks in various cities and you have data for profits 
    and populations from the cities. 
    
    You would like to use this data to help you select which city to expand to next.
    
    Perform Simple Linear regression to predict the profit based on the 
    population observed and visualize the result.
    
    Based on the above trained results, what will be your estimated profit, 
    
    If you set up your outlet in Jaipur? 
    (Current population in Jaipur is 3.073 million)
        
  Hint: 
    You will implement linear regression to predict the profits for a 
    food chain company.
    Foodtruck.csv contains the dataset for our linear regression problem. 
    The first column is the population of a city and the second column is the 
    profit of a food truck in that city. 
    A negative value for profit indicates a loss.
"""
import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt

dataset=pd.read_csv('Foodtruck.csv')

features = dataset.iloc[:, :-1].values  
labels = dataset.iloc[:, 1].values 


from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(features, labels) 

pop=float(input("What is the population?"))
profit=regressor.predict(np.array(pop).reshape(1,1))
print("PROFIT -",profit)
if profit<0:
    print("Business in this city is not beneficial")

