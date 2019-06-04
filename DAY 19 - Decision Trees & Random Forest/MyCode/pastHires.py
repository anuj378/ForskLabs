"""


Q1. (Create a program that fulfills the following specification.)
PastHires.csv


Here, we are building a decision tree to check if a person is hired or not based on certain predictors.

Import PastHires.csv File.

scikit-learn needs everything to be numerical for decision trees to work.

So, use any technique to map Y,N to 1,0 and levels of education to some scale of 0-2.

    Build and perform Decision tree based on the predictors and see how accurate your 
    prediction is for a being hired.

Now use a random forest of 10 decision trees to predict employment of specific candidate profiles:

    Predict employment of a currently employed 10-year veteran, previous employers 4,
    went to top-tire school, having Bachelor's Degree without Internship.
    [[10,1,4,0,1,0]]
    Predict employment of an unemployed 10-year veteran, ,previous employers 4,
    didn't went to any top-tire school, having Master's Degree with Internship.
    [[10,0,4,1,0,1]]
"""

 
import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  



dataset = pd.read_csv("PastHires.csv")
dataset['Employed?']=dataset['Employed?'].map(lambda x:(1 if (x=='Y') else 0))
dataset['Interned']=dataset['Interned'].map(lambda x:(1 if (x=='Y') else 0))
dataset['Hired']=dataset['Hired'].map(lambda x:(1 if (x=='Y') else 0))
dataset['Top-tier school']=dataset['Top-tier school'].map(lambda x:(1 if (x=='Y') else 0))

features = dataset.drop('Employed?', axis=1)  
labels = dataset['Employed?']  

from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
features.iloc[:, 2] = labelencoder.fit_transform(features.iloc[:, 2])

from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.20)  


from sklearn.tree import DecisionTreeClassifier  
classifier = DecisionTreeClassifier()  
classifier.fit(features_train, labels_train)

labels_pred = classifier.predict(features_test) 


from sklearn.metrics import confusion_matrix  
print(confusion_matrix(labels_test, labels_pred))

print(classifier.score(features_train,labels_train))
####################

  
import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  



dataset = pd.read_csv("PastHires.csv")
dataset['Employed?']=dataset['Employed?'].map(lambda x:(1 if (x=='Y') else 0))
dataset['Interned']=dataset['Interned'].map(lambda x:(1 if (x=='Y') else 0))
dataset['Hired']=dataset['Hired'].map(lambda x:(1 if (x=='Y') else 0))
dataset['Top-tier school']=dataset['Top-tier school'].map(lambda x:(1 if (x=='Y') else 0))

features = dataset.drop('Employed?', axis=1)  
labels = dataset['Employed?']  

from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
features.iloc[:, 2] = labelencoder.fit_transform(features.iloc[:, 2])

from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.20)  


from sklearn.ensemble import RandomForestClassifier  
classifier = DecisionTreeClassifier()  
classifier.fit(features_train, labels_train)

labels_pred = classifier.predict(features_test) 


from sklearn.metrics import confusion_matrix  
print(confusion_matrix(labels_test, labels_pred))


classifier.score(features_train,labels_train)
pred_1=classifier.predict([[10,1,4,0,1,0]])
#THIS IS ALSO A WAY
#pred_1=classifier.predict([[10,1,4,0,1,0],[10,0,4,1,0,1]])
pred_2=classifier.predict([[10,0,4,1,0,1]])
print(classifier.score(features_train,labels_train))