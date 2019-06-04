"""
Q1. (Create a program that fulfills the following specification.)
Auto_mpg.txt

Here is the dataset about cars. The data concerns city-cycle fuel consumption in miles per gallon (MPG).

    Import the dataset Auto_mpg.txt
    Give the column names as "mpg", "cylinders", "displacement","horsepower","weight","acceleration", 
    "model year", "origin", "car name" respectively
    
    Display the Car Name with highest miles per gallon value
    
    Build the Decision Tree and Random Forest models and find out which of the two 
    is more accurate in predicting the MPG value
    
    Find out the MPG value of a 80's model car of origin 3, weighing 2630 kgs 
    with 6 cylinders, having acceleration around 22.2 m/s due to it's 100 horsepower engine 
    giving it a displacement of about 215. (Give the prediction from both the models)

[[6,215,100,2630,22.2,80,3]]
"""

import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  

columns_1=["mpg", "cylinders", "displacement","horsepower","weight","acceleration", 
    "model year", "origin", "car name"]

dataset = pd.read_csv('Auto_mpg.txt',header=None,names=columns_1,delim_whitespace=True)
highest_mpg_car=dataset['car name'][(dataset['mpg']) == max(dataset['mpg'])].values[0]
highest_mpg_car

features = dataset.iloc[:, 1:-1]
features['horsepower']=features['horsepower'].replace('?', np.nan).astype(np.float64)
features['horsepower']=features['horsepower'].fillna(features['horsepower'].mean())
#.values
features = features.values
labels = dataset.iloc[:, 0].values.reshape(-1,1)

from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.20)  


from sklearn.tree import DecisionTreeRegressor  as dtr
regressor = dtr()  
regressor.fit(features_train, labels_train)
demo_pred=classifier.predict([[6,215,100,2630,22.2,80,3]])

regressor.score(features_test,labels_test) 
##############################################################################################################


import pandas as pd  
import numpy as np  


columns_1=["mpg", "cylinders", "displacement","horsepower","weight","acceleration", 
    "model year", "origin", "car name"]

dataset = pd.read_csv('Auto_mpg.txt',header=None,names=columns_1,delim_whitespace=True)


features = dataset.iloc[:, 1:-1]
features['horsepower']=features['horsepower'].replace('?', np.nan).astype(np.float64)
features['horsepower']=features['horsepower'].fillna(features['horsepower'].mean())
#.values
features = features.values
labels = dataset.iloc[:, 0].values.reshape(-1,1)

from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.20)  

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()  
features_train = sc.fit_transform(features_train)  
features_test = sc.transform(features_test)  


from sklearn.ensemble import RandomForestRegressor

regressor = RandomForestRegressor(n_estimators=25, random_state=0)  
regressor.fit(features_train, labels_train)  
labels_pred = regressor.predict(features_test) 


regressor.score(features_test,labels_test)
