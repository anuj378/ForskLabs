
"""
Code Challenge
  Name: 
    SSA Analysis
  Filename: 
    ssa.py
  Problem Statement:
    (Baby_Names.zip)
    The United States Social Security Administration (SSA) has made available 
    data on the frequency of baby names from 1880 through the 2010. 
    (Use Baby_Names.zip from Resources)  
    
    Read data from all the year files starting from 1880 to 2010, 
    add an extra column named as year that contains year of that particular data
    Concatinate all the data to form single dataframe using pandas concat method
    Display the top 5 male and female baby names of 2010
    Calculate sum of the births column by sex as the total number of births 
    in that year(use pandas pivot_table method)
    Plot the results of the above activity to show total births by sex and year  
     
"""
import pandas as pd
data=pd.DataFrame(columns = ['Name','Gender','ID','Year'])
for i in range(1880,2018):
    yName="yob"+str(i)+".txt"
    temp_df=pd.read_csv(yName,header=None)
    temp_df.columns=['Name','Gender','ID']
    temp_df['Year']=i
    data=pd.concat([data,temp_df])
top_5_male=data['Name'][(data['Gender']=='M') & (data['Year']==2010)][0:5]
top_5_female=data['Name'][(data['Gender']=='F') & (data['Year']==2010)][0:5]

