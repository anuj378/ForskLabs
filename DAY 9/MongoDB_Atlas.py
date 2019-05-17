
'''
Code Challenge 2
Perform similar steps as in the above code challenge but store the contents in 
an online mongo atlas database.'''
#!pip install pymongo


import pymongo
#import dns # required for connecting with SRV

#client = pymongo.MongoClient("mongodb://K_Vaid:123chandu30%26@cluster0-shard-00-00-tofyu.mongodb.net:27017,cluster0-shard-00-01-tofyu.mongodb.net:27017,cluster0-shard-00-02-tofyu.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")

client = pymongo.MongoClient("mongodb://Anuj378:mdb_Anuj378@firstcluster-shard-00-00-xd34b.mongodb.net:27017,firstcluster-shard-00-01-xd34b.mongodb.net:27017,firstcluster-shard-00-02-xd34b.mongodb.net:27017/test?ssl=true&replicaSet=FirstCluster-shard-0&authSource=admin&retryWrites=true")
mydb = client.PLAY_DB
#mydb.ForskEmployees.drop()

def add_employee(idd, first, last, pay):
    unique_employee = mydb.ForskEmployees.find_one({"id":idd})
    if unique_employee:
        return "Employee already exists"
    else:
        mydb.ForskEmployees.insert_one(
            {
            "id" : idd,
            "first" : first,
            "last" : last,
            "pay" : pay
            })
    return "Employee added successfully"
add_employee(1,'Sylvester', 'Fernandes', '50000')
add_employee(2,'Yogendra', 'Singh', 70000)
add_employee(3,'Rohit', 'Mishra', 30000)
add_employee(4,'Kunal', 'Vaid', 30000)
add_employee(5,'Devendra', 'Shekhawat', 30000)


def fetch_all_employee():
    user = mydb.ForskEmployees.find()
    for i in user:
        print (i)
        
fetch_all_employee()
Final_Data=[]
a=[]
b=[]
c=[]
d=[]
heads=["id", "first","last","pay"]


for i in mydb.ForskEmployees.find():
    a.append(i["id"])
    b.append(i["first"])
    c.append(i["last"])
    d.append(i["pay"])


from collections import OrderedDict
Final_Data=[a,b,c,d]
data=OrderedDict(zip(heads,Final_Data))
    
import pandas as pd
df=pd.DataFrame(data)
print(df)
