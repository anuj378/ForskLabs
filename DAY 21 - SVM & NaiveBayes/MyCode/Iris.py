"""

Q2. This famous classification dataset first time used in Fisher’s classic 1936 paper, The Use of Multiple Measurements 
in Taxonomic Problems. Iris dataset is having 4 features of iris flower and one target class.

The 4 features are

SepalLengthCm
SepalWidthCm
PetalLengthCm
PetalWidthCm
The target class

The flower species type is the target class and it having 3 types

Setosa
Versicolor
Virginica
The idea of implementing svm classifier in Python is to use the iris features to train an svm classifier and use the trained svm model
to predict the Iris species type. To begin with let’s try to load the Iris dataset.

"""


import numpy as np 
import pandas as pd 
from sklearn import datasets 
data = datasets.load_iris()

labels=data.target
labels=labels.reshape(-1,1)
features=data.data
features=pd.DataFrame(features,columns=['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm'])


from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.3, random_state = 0)

# Feature Scaling may be applied

# Fitting Kernel SVM to the Training set
# kernels: linear, poly and rbf

from sklearn.svm import SVC
classifier = SVC(kernel = 'rbf', random_state = 0)
classifier.fit(features_train, labels_train)
"""

classifier_lin = SVC(kernel = 'linear', random_state = 0)
classifier_lin.fit(features_train, labels_train)


classifier_poly = SVC(kernel = 'poly', random_state = 0)
classifier_poly.fit(features_train, labels_train)
"""

# Predicting the Test set results
labels_pred = classifier.predict(features_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)

# Model Score
score = classifier.score(features_test,labels_test)


"""

# Predicting the Test set results
labels_pred_lin = classifier_lin.predict(features_test)


# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)

# Model Score
score = classifier_lin.score(features_test,labels_test)

print("LINEAR",classifier_lin.predict([[6,2,5,3,2,7,9,2,4]]))

################################################################


# Predicting the Test set results
labels_pred_poly = classifier_poly.predict(features_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)

# Model Score
score = classifier_poly.score(features_test,labels_test)


print("POLY",classifier_poly.predict([[6,2,5,3,2,7,9,2,4]]))

"""
x=pd.DataFrame({"rbf":labels_pred,"Linear":labels_pred_lin,"Poly":labels_pred_poly})