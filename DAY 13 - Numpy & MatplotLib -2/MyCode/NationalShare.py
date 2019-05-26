
"""
Code Challenge

https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area


Scrap the data from State/Territory and National Share (%) columns for top 6 
states basis on National Share (%). 
Create a Pie Chart using MatPlotLib and explode the state with largest national share %.

"""
from bs4 import BeautifulSoup as bs
import requests as r
import numpy as np

response=r.get('https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area').text
page_content=bs(response)
table=page_content.find("table",class_="wikitable sortable")

states=[]
national_share=[]
temp=[]
body=table.find('tbody')

for row in body.findAll('tr'):
    columns=row.find_all('td')
    if len(columns)==7:
        states.append(columns[1].text.strip())
        national_share.append(float(columns[4].text.strip()))
states=states[0:6]
national_share=national_share[0:6]

import matplotlib.pyplot as plt

plt.pie(national_share,(.25,0,0,0,0,0),states,['red','blue','green','yellow','orange','purple'],autopct='%1.1f%%')

    









