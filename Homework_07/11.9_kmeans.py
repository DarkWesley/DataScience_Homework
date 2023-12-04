import numpy as np
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
iris = load_iris()
x= iris.data
kmeans = KMeans(n_clusters=3, random_state=23)
kmeans.fit(x)
labels = kmeans.labels_
centers = kmeans.cluster_centers_
plt.figure(figsize=(8,6))
for i in range(3):
    cluster_points =x[labels == i]
    plt.scatter(cluster_points[:, 0], cluster_points[:, 1], label=f'cluster{i + 1}')
plt.scatter(centers[:, 0], centers[:, 1,], c='red', s=200, marker='x', label='center_point')
plt.xlabel('feature1')
plt.ylabel('feature12')
plt.legend()
plt.title('K-means Clustering')
plt.show()