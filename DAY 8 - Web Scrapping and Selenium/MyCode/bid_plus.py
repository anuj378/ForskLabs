"""
Code Challenge:
  Name: 
    Bid Plus
  Filename: 
    bid_plus.py
  Problem Statement:
      USE SELENIUM
      Write a Python code to Scrap data and download data from given url.
      url = "https://bidplus.gem.gov.in/bidlists"
      Make list and append given data:
          1. BID NO
          2. items
          3. Quantity Required
          4. Department Name And Address
          5. Start Date/Time(Enter date and time in different columns)
          6. End Date/Time(Enter date and time in different columns)
     Make a csv file add all data in it.
      csv Name: bid_plus.csv
"""

#'//*[@id="pagi_content"]/div[{}]/div[2]/p[1]/span'

#'/html/body/section[2]/div/div/div/div[1]/div/div/div/div[2]/div/div[1]/div[{}]/div[1]/p[1]/span'
from selenium import webdriver
from collections import OrderedDict
import pandas as pd
from time import sleep
driver=webdriver.Firefox(executable_path=r'geckodriver.exe')
res=driver.get('https://bidplus.gem.gov.in/bidlists')

sleep(5)


#main_div=driver.find_element_by_xpath('//*[@id="pagi_content"]')
header=['BID NO','Item(s)','Quantity Required','Department Name And Address','Start Date','End Date']
B_ID=[]
Items=[]
Quatity_Required=[]
Dept_Name_and_Address=[]
Start_Date=[]
End_Date=[]
for i in range(1,11):
    B_ID.append(driver.find_element_by_xpath('/html/body/section[2]/div/div/div/div[1]/div/div/div/div[2]/div/div[1]/div[{}]/div[1]/p[1]/a'.format(i)).text)
    #print(B_ID)
    Items.append(driver.find_element_by_xpath('/html/body/section[2]/div/div/div/div[1]/div/div/div/div[2]/div/div[1]/div[{}]/div[2]/p[1]/span'.format(i)).text)
    Quatity_Required.append(driver.find_element_by_xpath('/html/body/section[2]/div/div/div/div[1]/div/div/div/div[2]/div/div[1]/div[{}]/div[2]/p[2]/span'.format(i)).text)
    Dept_Name_and_Address.append(driver.find_element_by_xpath('/html/body/section[2]/div/div/div/div[1]/div/div/div/div[2]/div/div[1]/div[{}]/div[3]/p[2]'.format(i)).text)
    Start_Date.append(driver.find_element_by_xpath('/html/body/section[2]/div/div/div/div[1]/div/div/div/div[2]/div/div[1]/div[{}]/div[4]/p[1]/span'.format(i)).text)
    End_Date.append(driver.find_element_by_xpath('/html/body/section[2]/div/div/div/div[1]/div/div/div/div[2]/div/div[1]/div[{}]/div[4]/p[2]/span'.format(i)).text)    
'''
/html/body/section[2]/div/div/div/div[1]/div/div/div/div[2]/div/div[1]/div[1]/div[2]/p[2]/span

'''
data=OrderedDict(zip(header,[B_ID,
Items,
Quatity_Required,
Dept_Name_and_Address,
Start_Date,
End_Date,]))

for i in range(1,11):
    temp=driver.find_element_by_xpath('/html/body/section[2]/div/div/div/div[1]/div/div/div/div[2]/div/div[1]/div[{}]/div[2]/p[1]/span'.format(i))
    temp.click()
    sleep(5)
    
df=pd.DataFrame(data)
print(df)




"""
/html/body/section[2]/div/div/div/div[1]/div/div/div/div[2]/div/div[1]/div[1]/div[2]/p[1]/span
/html/body/section[2]/div/div/div/div[1]/div/div/div/div[2]/div/div[1]/div[1]/div[3]/p[2]
"""