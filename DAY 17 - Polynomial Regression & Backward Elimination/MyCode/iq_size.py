"""Q. (Create a program that fulfills the following specification.)
iq_size.csv

Are a person's brain size and body size (Height and weight)
 predictive of his or her intelligence?

 

Import the iq_size.csv file

It Contains the details of 38 students, where

Column 1: The intelligence (PIQ) of students

Column 2:  The brain size (MRI) of students (given as count/10,000).

Column 3: The height (Height) of students (inches)

Column 4: The weight (Weight) of student (pounds)

   _____ What is the IQ of an individual with a given brain size of 90,
      height of 70 inches, and weight 150 pounds ? 
    ____Build an optimal model and conclude which is more useful in predicting intelligence Height,
      Weight or brain size.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


dataset = pd.read_csv("iq_size.csv")
features = dataset.iloc[:,-3: ].values
labels = dataset.iloc[:, 0].values

from sklearn.linear_model import LinearRegression
lin_reg_1 = LinearRegression()
lin_reg_1.fit(features, labels)
#1
lin_reg_1.predict([[90,70,150]])

#2
import statsmodels.api as sm
features = sm.add_constant(features)
features_opt = features[:,:  ]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
#regressor_OLS.summary()
p_values=regressor_OLS.pvalues
list_indices=list(range(0,len(features_opt[0])))

while(max(p_values)>0.05):
    list_features=(list(features_opt))
    index_val=(list_features.index(max(p_values)))
    features_opt = features_opt[:,list_indices.remove(index_val)]
    regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()   
    p_values=regressor_OLS.pvalues    
