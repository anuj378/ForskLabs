"""
Code Challenge
  Name: 
    Titanic Analysis
  Filename: 
    titanic.py
  Dataset:
    training_titanic.csv
  Problem Statement:
      It’s a real-world data containing the details of titanic ships 
      passengers list.
      Import the training set "training_titanic.csv"
  Answer the Following:
      How many people in the given training set survived the disaster ?
      How many people in the given training set died ?
      Calculate and print the survival rates as proportions (percentage) 
      by setting the normalize argument to True.
      Males that survived vs males that passed away
      Females that survived vs Females that passed away
      
      Does age play a role?
      since it's probable that children were saved first.
      
      Another variable that could influence survival is age; 
      since it's probable that children were saved first.

      You can test this by creating a new column with a categorical variable Child. 
      Child will take the value 1 in cases where age is less than 18, 
      and a value of 0 in cases where age is greater than or equal to 18.
 
      Then assign the value 0 to observations where the passenger 
      is greater than or equal to 18 years in the new Child column.
      Compare the normalized survival rates for those who are <18 and 
      those who are older. 
    
      To add this new variable you need to do two things
        1.     create a new column, and
        2.     Provide the values for each observation (i.e., row) based on the age of the passenger.
    
  Hint: 
      To calculate this, you can use the value_counts() method in 
      combination with standard bracket notation to select a single column of
      a DataFrame
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as py
#NUMBER OF SURVIVERS AND NON SURVIVERS
data=pd.read_csv('training_titanic.csv')
survival_status=data['Survived'].value_counts()
print("Total Survivers ={} and Non-Survivers={}".format(survival_status.loc[1],survival_status.loc[0]))

#IN PERCENTAGE
survival_status=data['Survived'].value_counts(normalize=True)
print("Total Survivers percentage ={}%  and  Non-Survivers percantage={}%".format(  round(survival_status.loc[1]*100,2)  ,   round(survival_status.loc[0]*100,2)))

#
data['Sex'].isnull()
male_status=data['Survived'][data['Sex']=='male'].value_counts(normalize=True)
print("Total Male Survivers percentage ={}%  and Male Non-Survivers percantage={}%".format(  round(male_status.loc[1]*100,2)  ,   round(male_status.loc[0]*100,2)))

female_status=data['Survived'][data['Sex']=='female'].value_counts(normalize=True)
print("Total female Survivers percentage ={}%  and female Non-Survivers percantage={}%".format(  round(female_status.loc[1]*100,2)  ,   round(female_status.loc[0]*100,2)))

data['Age'] = data['Age'].replace(np.NaN, data['Age'].mean())
data["Child"] = data["Age"].map(lambda x: 0 if x>=18 else 1 )
status_child_ratio=data['Survived'][data['Child']==1].value_counts(normalize=True)
status_child_ratio
print("53% children were saved and 46% were unable to be saved so.. Children were given preference")
