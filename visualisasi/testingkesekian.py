import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import pandas as pd

# Load data
data = pd.read_csv('8283.csv')

# Extract the Raport column for clustering
raport_values = data[['Raport']]

# Define k-means clustering with predefined centroids
initial_centroids = [[65], [73], [78]]
kmeans = KMeans(n_clusters=3, init=initial_centroids, n_init=1, random_state=42)

# Fit the KMeans and assign clusters
data['Cluster'] = kmeans.fit_predict(raport_values)

# Visualize the distribution of Raport values and their clusters
plt.figure(figsize=(8, 6))
colors = ['red', 'blue', 'green']
for cluster in range(3):
    cluster_data = data[data['Cluster'] == cluster]
    plt.scatter(cluster_data.index, cluster_data['Raport'], color=colors[cluster], label=f'Cluster {cluster}')

# Mark centroids on the graph
for i, centroid in enumerate(kmeans.cluster_centers_):
    plt.scatter(len(data) + i, centroid, color=colors[i], edgecolor='black', s=100, label=f'Centroid {i}')

plt.title('Persebaran Nilai Raport Berdasarkan Cluster')
plt.xlabel('Index Data')
plt.ylabel('Nilai Raport')
plt.legend()
plt.show()
