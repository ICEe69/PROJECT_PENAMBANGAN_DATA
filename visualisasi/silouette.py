from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import pandas as pd

# Load data
data = pd.read_csv('nilai82.csv')  # Ganti dengan nama file Anda
data['Average'] = data[['UTS', 'SAS']].mean(axis=1)

# Clustering dengan K-Means
features = data[['Average']].values
kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(features)

# Tambahkan label kluster ke dataset
data['Cluster'] = clusters

# Hitung Silhouette Score
silhouette_avg = silhouette_score(features, clusters)
print(f"Silhouette Score: {silhouette_avg:.3f}")

# Distribusi kluster
cluster_counts = data['Cluster'].value_counts(normalize=True) * 100
print("Distribusi Kluster:")
print(cluster_counts)
