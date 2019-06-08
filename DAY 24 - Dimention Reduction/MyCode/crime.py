# -*- coding: utf-8 -*-
"""
Q1. (Create a program that fulfills the following specification.)

Import Crime.csv File.
Perform dimension reduction and group the cities using k-means
based on Rape, Murder and assault predictors.

"""

import pandas as pd
dataset=pd.read_csv("crime_data.csv")
features=dataset.iloc[:,[1,2,4]]

#checking If any column has a null value
for i in features.columns:
    if (features[i].isnull().any()):
        print(i)


'''
from sklearn.model_selection import train_test_split
features_train, features_test = train_test_split(features, test_size = 0.2, random_state = 0)
'''
# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features= sc.fit_transform(features)

from sklearn.decomposition import PCA
pca = PCA(n_components = 2)
features = pca.fit_transform(features)

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters = 3, init = 'k-means++', random_state = 0)
pred_cluster = kmeans.fit_predict(features)
import matplotlib.pyplot as plt
plt.scatter(features[pred_cluster == 0, 0], features[pred_cluster == 0, 1], c = 'blue', label = 'Cluster 1')
plt.scatter(features[pred_cluster == 1, 0], features[pred_cluster == 1, 1], c = 'red', label = 'Cluster 2')
plt.scatter(features[pred_cluster == 2, 0], features[pred_cluster == 2, 1], c = 'green', label = 'Cluster 3')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'yellow', label = 'Centroids')
plt.title('Clusters of Cities')
plt.xlabel('P1 Coordindates')
plt.ylabel('P2 Coordinates')
#plt.legend()
plt.show()

