"""
Code Challenge
  Name: 
    Telecom Churn Analysis
  Dataset:
    Telecom_churn.csv
  Filename: 
    telecom_churn.py
  Problem Statement:
    Read the telecom_churn.csv file and perform the following task :
        To perfrom analysis on the Telecom industry churn dataset -
1. Predict the count of Churned customer availing both voice mail plan and international plan schema
2. Total charges for international calls made by churned and non-churned customer and visualize it
3. Predict the state having highest night call minutes for churned customer
4. Visualize -
    a. the most popular call type among churned user
    b. the minimum charges among all call type among churned user
5. Which category of customer having maximum account lenght? Predict and print it
6. Predict a relation between the customer and customer care service that whether churned customer have shown their concern to inform the customer care service about their problem or not
7. In which area code the international plan is most availed?
    
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#1. Predict the count of Churned customer availing both voice mail plan and international plan schema
data=pd.read_csv("Telecom_churn.csv")
data=data.fillna(data.mean())
df_1=data['churn'][(data['international plan']=='yes')&(data['voice mail plan']=='yes')].value_counts()
print(df_1[1])
#2. Total charges for international calls made by churned and non-churned customer and visualize it
total_churned_International=data['total intl charge'][data['churn']==True]
total_Nonchurned_International=data['total intl charge'][data['churn']==False]
print("Total International Charges for churned users  ",total_churned_International.sum())
print("Total International Charges for non-churned users  ",total_Nonchurned_International.sum())

plt.pie([total_churned_International.sum(),total_Nonchurned_International.sum()],(0,0),['Churned','Non-Churned'])
 
#3. Predict the state having highest night call minutes for churned customer
minutes=data[(data['churn']==True)]
minutes=minutes['state'][(minutes['total night minutes'] == (minutes['total night minutes'].max()))]
print("Name of the state is = {}".format(minutes[244]))
#4. 
""" 4 Visualize -
    a. the most popular call type among churned user
    b. the minimum charges among all call type among churned user
"""
 #a
churned_users = data[(data['churn']==True)]
call_types = ["day","eve", "night","intl"]
call_freq = []

for i in call_types:
    call_freq.append(sum(churned_users["total "+i+" calls"]))
max_val = call_freq.index(max(call_freq))
print(call_types[max_val])

#b
churned_users = data[(data['churn']==True)]
call_types = ["day","eve", "night","intl"]
call_min = []

for i in call_types:
    call_min.append(min(churned_users["total "+i+" calls"]))
min_val = call_min.index(min(call_min))
print(call_types[min_val])


#5 MAXIMUM ACCOUNT LENGTH
x=data['churn'][(data['account length']) == (max((data['account length']))) ].values[0]
if x==True:
    print('CHURNED')
else:
    print('Non-CHURNED')


#6
    

#7
availing_intPlan=(data['area code'][data['international plan']=='yes'].value_counts()).values[0]
availing_intPlan
