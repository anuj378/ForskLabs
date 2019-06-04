"""
Q. (Create a program that fulfills the following specification.)
bluegills.csv

How is the length of a bluegill fish related to its age?

In 1981, n = 78 bluegills were randomly sampled from Lake Mary in Minnesota.
 The researchers (Cook and Weisberg, 1999) measured and recorded the following data (Import bluegills.csv File)

Response variable(Dependent): length (in mm) of the fish

Potential Predictor (Independent Variable): age (in years) of the fish

    How is the length of a bluegill fish best related to its age? (Linear/Quadratic nature?)
    What is the length of a randomly selected five-year-old bluegill fish? Perform polynomial regression on the dataset.

NOTE: Observe that 80.1% of the variation in the length of bluegill fish is reduced 
by taking into account a quadratic function of the age of the fish.

"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


dataset = pd.read_csv("bluegills.csv")
features = dataset.iloc[:, 0].values
labels = dataset.iloc[:, 1].values
features=features.reshape(78,1)
plt.scatter(features, labels)

from sklearn.linear_model import LinearRegression
lin_reg_1 = LinearRegression()
lin_reg_1.fit(features, labels)
plt.scatter(features,labels)
plt.plot(features,lin_reg_1.predict(features))





from sklearn.preprocessing import PolynomialFeatures
poly_object = PolynomialFeatures(degree = 5)
features_poly = poly_object.fit_transform(features)

lin_reg_2 = LinearRegression()
lin_reg_2.fit(features_poly, labels)
plt.scatter(features,labels)
plt.plot(features,lin_reg_2.predict(features_poly))

#FOR COLLECTIVE VISUALIZATION

plt.scatter(features,labels)
plt.plot(features,lin_reg_2.predict(features_poly))
plt.plot(features,lin_reg_1.predict(features))

print("For 5 year old,Lenght will be {}inches ".format(round(float(lin_reg_2.predict(poly_object.transform([[5]]))),3)))

