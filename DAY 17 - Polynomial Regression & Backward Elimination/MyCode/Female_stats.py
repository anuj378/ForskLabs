"""Q. (Create a program that fulfills the following specification.)
Female_Stats.Csv

Female Stat Students

Import The Female_Stats.Csv File

The Data Are From N = 214 Females In Statistics Classes At The University Of California At Davi.

Column1 = Student’s Self-Reported Height,

Column2 = Student’s Guess At Her Mother’s Height, And

Column 3 = Student’s Guess At Her Father’s Height. All Heights Are In Inches.

 

Build A Predictive Model And Conclude If Both Predictors (Independent Variables) Are Significant For A Students’ Height Or Not
When Father’s Height Is Held Constant, The Average Student Height Increases By How Many Inches For Each One-Inch Increase In Mother’s Height.
When Mother’s Height Is Held Constant, The Average Student Height Increases By How Many Inches For Each One-Inch Increase In Father’s Height.

"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression as lr
"""

obj= lr()
obj.fit(features,labels)
plt.plot(features[:,0],labels, marker='o')
plt.scatter(features[:,1],labels, marker='o')
###########YOU CANT PLOT IT###################
"""

dataset=pd.read_csv("Female_Stats.csv")
features = dataset.iloc[:, -2:].values
labels = dataset.iloc[:, :-2].values

import statsmodels.api as sm
features = sm.add_constant(features)


features_opt = features[:, :]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt)
regressor_OLS=regressor_OLS.fit()
print(regressor_OLS.summary())



print("\n\tPVALUES are - \nmom - {}\ndad - {}".format(round(regressor_OLS.pvalues[0],2),round(regressor_OLS.pvalues[1],2)))
print("Both the factors are affecting equally")

#ANS 2 and ANS-3
"""see the coefficients only.. they are the answers..

obj= lr()
obj.fit(features,labels)
x1=obj.predict([[1,66,66]])
x2=obj.predict([[1,67,67]])
x2=x2-x1
x2

"""



