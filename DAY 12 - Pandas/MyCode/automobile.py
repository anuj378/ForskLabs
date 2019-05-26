
"""
Code Challenge
  Name: 
      Exploratory Data Analysis - Automobile
  Filename: 
      automobile.py
  Dataset:
      Automobile.csv
  Problem Statement:
      Perform the following task :
      1. Handle the missing values for Price column
      2. Get the values from Price column into a numpy.ndarray
      3. Calculate the Minimum Price, Maximum Price, Average Price and Standard Deviation of Price
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data_AM=pd.read_csv('Automobile.csv')
#1
data_AM['price'].fillna((data_AM['price']).mean())


#2
price_array=data_AM['price']
price_array=price_array.values
print("MINIMUM - {}\nMAXIMUM - {}\nAVERAGE - {}\nSD - {}".format(price_array.min(),price_array.max(),np.mean(price_array),np.std(price_array)))