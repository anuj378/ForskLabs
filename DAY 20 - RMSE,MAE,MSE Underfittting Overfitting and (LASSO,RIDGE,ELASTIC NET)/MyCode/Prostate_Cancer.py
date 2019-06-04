"""Code Challenge 01: (Prostate Dataset)
Load the dataset from given link: 
pd.read_csv("http://www.stat.cmu.edu/~ryantibs/statcomp/data/pros.dat")

This is the Prostate Cancer dataset. Perform the train test split before you apply the model.

(a) Can we predict lpsa from the other variables?
(1) Train the unregularized model (linear regressor) and calculate the mean squared error.
(2) Apply a regularized model now - Ridge regression and lasso as well and check the mean squared error.

(b) Can we predict whether lpsa is high or low, from other variables?
"""
import numpy as np
import pandas as pd

data=pd.read_csv("http://www.stat.cmu.edu/~ryantibs/statcomp/data/pros.dat",delim_whitespace=True)


features=data.drop('lpsa',axis=1)
labels=data.iloc[:,-1]

#data[data.isnull().any(axis=1)]
for i in features.columns:
    if(data[i].isnull().any()):
        data[i].fillna(data[i].mean())
        
features=features.values
labels=labels.values
labels=labels.reshape(-1,1)


from sklearn.model_selection import train_test_split as TTS
ftr,ft,ltr,lt =TTS(features,labels,test_size=.2,random_state=0)

from sklearn.preprocessing import StandardScaler as SC
sc=SC()
ftr=sc.fit_transform(ftr)
ft=sc.transform(ft)

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
from sklearn.linear_model import ElasticNet

lm = LinearRegression ()
lm_lasso = Lasso() 
lm_ridge =  Ridge() 
lm_elastic = ElasticNet()

lm.fit(ftr, ltr)
lm_lasso.fit(ftr, ltr)
lm_ridge.fit(ftr, ltr)
lm_elastic.fit(ftr, ltr)
predict_test_lm=lm.predict(ft)
predict_test_lasso=lm_lasso.predict(ft)
predict_test_ridge=lm_ridge.predict(ft)

lm.score(ftr,ltr) 
#65-72
lm_lasso.score(ftr,ltr)
#0.0
lm_ridge.score(ftr,ltr)
#65-72s
lm_elastic.score(ftr,ltr)
#25-34s

import numpy as np
from sklearn import metrics
print ("Simple Regression  Mean Square Error (MSE) for TEST data is") 
print (np.round( (metrics.mean_squared_error(lt, predict_test_lm)),2) )

'''
print ("Simple Regression  ROOT Mean Square Error (MSE) for TEST data is") 
print ((np.sqrt (metrics.mean_squared_error(lt, predict_test_lm))) )
RMS=np.sqrt (metrics.mean_squared_error(lt, predict_test_lm))
meann_lpsa=data['lpsa'].mean()
if(meann_lpsa*.1<RMS):
    print("Its a good model ")
else:
    print("Needs improvement")
'''
print ("Lasso Regression Mean Square Error (MSE) for TEST data is") 
print (np.round (metrics .mean_squared_error(lt, predict_test_lasso),2))

print ("Ridge Regression Mean Square Error (MSE) for TEST data is") 
print (np.round (metrics .mean_squared_error(lt, predict_test_ridge),2))



################################################################################################33

import numpy as np
import pandas as pd

data=pd.read_csv("http://www.stat.cmu.edu/~ryantibs/statcomp/data/pros.dat",delim_whitespace=True)


data['lpsa']=data['lpsa'].map(lambda x: 1 if (x>2) else 0 )        
features=data.drop('lpsa',axis=1)
labels=data.iloc[:,-1]

for i in features.columns:
    if(data[i].isnull().any()):
        data[i].fillna(data[i].mean())


features=features.values
labels=labels.values
labels=labels.reshape(-1,1)


from sklearn.model_selection import train_test_split as TTS
ftr,ft,ltr,lt =TTS(features,labels,test_size=.2,random_state=0)

from sklearn.preprocessing import StandardScaler as SC
sc=SC()
ftr=sc.fit_transform(ftr)
ft=sc.transform(ft)

from sklearn.linear_model import LogisticRegression
lm=LogisticRegression()
lm=lm.fit(ftr,ltr)

pred=lm.predict(ft)
data_match=pd.DataFrame({"Actual":lt.flatten(),"Predicted":pred})

from sklearn.metrics import confusion_matrix as CM
cm=CM(lt,pred)


print("Score of Training data",lm.score(ftr,ltr))
print("Score of Testing data",lm.score(ft,lt) )







