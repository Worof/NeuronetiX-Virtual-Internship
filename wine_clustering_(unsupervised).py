# -*- coding: utf-8 -*-
"""Wine Clustering (Unsupervised).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18_PWQ1qvA4E4AOG-fDKGT7jFwCP7X934

***First Model: Hierarchical Clustering ***
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster

data = pd.read_csv('wine-clustering.csv')
data
data.head()
data.info()
data.describe()

features = data[['Alcohol', 'Color_Intensity']]

scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)
features_scaled

sns.set(style='whitegrid')

linked = linkage(wine_scaled, method='ward')

plt.figure(figsize=(10, 7))
dendrogram(linked, orientation='top', distance_sort='descending', show_leaf_counts=True)
plt.title('Dendrogram for Hierarchical Clustering')
plt.xlabel('Sample Index')
plt.ylabel('Distance')
plt.show()

hierarchical_clusters = fcluster(linked, t=3, criterion='maxclust')

pca = PCA(n_components=2)
wine_pca = pca.fit_transform(features_scaled)

plt.figure(figsize=(10, 6))
scatter = plt.scatter(features['Alcohol'], features['Color_Intensity'], c=wine_clusters, s=100, cmap='viridis', alpha=0.6, edgecolors='w', linewidths=0.5)
plt.title('Clusters of Wine Samples Based on Alcohol and Color Intensity (Hierarchical Clustering)')
plt.xlabel('Alcohol')
plt.ylabel('Color Intensity')
plt.legend(*scatter.legend_elements(), title="Clusters")
plt.grid(True)
plt.show()

"""**Second Model: K-means**"""

from sklearn.cluster import KMeans

inertia = []
k_range = range(1, 11)
for k in k_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(features_scaled)
    inertia.append(kmeans.inertia_)

plt.figure(figsize=(10, 6))
plt.plot(k_range, inertia, marker='o')
plt.title('Elbow Method For Optimal k (K-means)')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')
plt.show()

kmeans = KMeans(n_clusters=3, random_state=42)
wine_clusters = kmeans.fit_predict(features_scaled)

centroids = scaler.inverse_transform(kmeans.cluster_centers_)

plt.figure(figsize=(10, 6))
scatter = plt.scatter(features['Alcohol'], features['Color_Intensity'], c=wine_clusters, s=100, cmap='viridis', alpha=0.6, edgecolors='w', linewidths=0.5)
plt.scatter(centroids[:, 0], centroids[:, 1], s=300, c='yellow', marker='o', alpha=0.8, label='Centroid')
plt.title('Clusters of Wine Samples Based on Alcohol and Color Intensity (K-means)')
plt.xlabel('Alcohol')
plt.ylabel('Color Intensity')
plt.legend(*scatter.legend_elements(), title="Clusters")
plt.grid(True)
plt.show()