

"""
Code Challenge
  Name: 
    Webscrapping ICC Cricket Page
  Filename: 
    icccricket.py
  Problem Statement:
    Write a Python code to Scrap data from ICC Ranking's 
    page and get the ranking table for ODI's (Men). 
    Create a DataFrame using pandas to store the information.
  Hint: 
    https://www.icc-cricket.com/rankings/mens/team-rankings/odi 
    
    
    #https://www.icc-cricket.com/rankings/mens/team-rankings/t20i
    #https://www.icc-cricket.com/rankings/mens/team-rankings/test
"""

import  requests as r
from bs4 import BeautifulSoup as bs
url="https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
response=r.get(url).text
soup=bs(response,'lxml')

table=soup.find('table',class_='table')

import pandas as pd
h=[]
a=[]
b=[]
c=[]
d=[]
e=[]

for row in table.thead.findAll('th'):
        h.append(row.text)
for row in table.findAll('tr'):
    data=row.findAll('td')
    if len(data)==5:
        a.append(data[0].text.strip())
        b.append(data[1].text.strip())
        c.append(data[2].text.strip())
        d.append(data[3].text.strip())
        e.append(data[4].text.strip())
        
from collections import OrderedDict
col_data = OrderedDict(zip(h,[a,b,c,d]))
df = pd.DataFrame(col_data) 
df.to_csv("icc.csv", index=False)
    




