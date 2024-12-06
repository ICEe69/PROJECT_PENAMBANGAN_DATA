import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Baca data dari CSV
file_path = "nilai82.csv"  # Ubah sesuai lokasi file Anda
df = pd.read_csv(file_path)

# Pastikan kolom sesuai
df.columns = ["Nama", "UTS", "SAS"]

# Centroid
centroids = {
    "C1": np.array([82.57142857, 63.57142857]),
    "C2": np.array([83.44, 50.56]),
    "C3": np.array([84.83333333, 73.66666667])
}

# Function to calculate Euclidean distance
def calculate_distance(point, centroid):
    return np.sqrt(np.sum((point - centroid) ** 2))

# Menentukan cluster berdasarkan centroid
clusters = []
for index, row in df.iterrows():
    point = np.array([row['UTS'], row['SAS']])
    distances = {c: calculate_distance(point, coord) for c, coord in centroids.items()}
    cluster = min(distances, key=distances.get)
    clusters.append(cluster)

# Tambahkan kluster ke DataFrame
df['Cluster'] = clusters

# Warna untuk setiap cluster
cluster_colors = {"C1": "blue", "C2": "green", "C3": "red"}

# Plot data points
plt.figure(figsize=(10, 7))
for cluster, color in cluster_colors.items():
    cluster_data = df[df['Cluster'] == cluster]
    plt.scatter(cluster_data['UTS'], cluster_data['SAS'], label=f"Cluster {cluster}", color=color, alpha=0.7)

    # Menambahkan label dengan nama dan cluster untuk setiap titik data
    for i, row in cluster_data.iterrows():
        plt.text(row['UTS'], row['SAS'], f"{row['Nama']} ({cluster})", fontsize=9, color='black', ha='right', va='bottom')

# Plot centroids
for cluster, coord in centroids.items():
    plt.scatter(coord[0], coord[1], label=f"Centroid {cluster}", color=cluster_colors[cluster], marker='X', s=200)

# Label plot
plt.title("K-Means Clustering Visualization", fontsize=14)
plt.xlabel("UTS", fontsize=12)
plt.ylabel("SAS", fontsize=12)
plt.legend()
plt.grid(True)
plt.show()
