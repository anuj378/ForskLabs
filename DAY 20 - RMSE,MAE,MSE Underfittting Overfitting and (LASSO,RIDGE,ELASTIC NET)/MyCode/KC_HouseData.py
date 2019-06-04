"""Code Challenges 02: (House Data)
This is kings house society data.
In particular, we will: 
• Use Linear Regression and see the results
• Use Lasso (L1) and see the resuls
• Use Ridge and see the score
"""


import numpy as np
import pandas as pd

data=pd.read_csv("kc_house_data.csv")

features=data.drop('id',axis=1)
features=features.drop('price',axis=1)
data['price']=data['price'].fillna(data['price'].mean())
labels=data['price'].values.reshape(-1,1)
features['date']=features['date'].map(lambda x:x[0:4]).astype(np.int64)
features=features.fillna(features.mean())

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



lm.score(ftr,ltr)
lm_lasso.score(ftr,ltr)
lm_ridge.score(ftr,ltr)
lm_elastic.score(ftr,ltr)

