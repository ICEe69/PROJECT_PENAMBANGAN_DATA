import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

# 1. Load dataset (ganti sesuai file dan kolom Anda)
file_path = '8182.xlsx'  # Ganti dengan nama file Anda
data = pd.read_excel(file_path)

# Misalkan ada kolom 'Nilai' yang digunakan untuk clustering
values = data['Raport'].values.reshape(-1, 1)  # Pastikan kolom yang sesuai

# 2. Tentukan jumlah cluster
n_clusters = 3
initial_centroids = np.array([[65], [73], [78]])

# 3. K-Means clustering
kmeans = KMeans(n_clusters=3, init=initial_centroids, n_init=1, max_iter=300, random_state=42)
kmeans.fit(values)

# 4. Hitung silhouette score
labels = kmeans.labels_
sil_score = silhouette_score(values, labels)

# 5. Visualisasi hasil clustering dengan silhouette score
plt.bar(range(len(values)), labels, color='skyblue', edgecolor='black')
plt.title(f'Clustering Bar Plot (Silhouette Score = {sil_score:.2f})')
plt.xlabel('Data Index')
plt.ylabel('Cluster Labels')
plt.show()

# Output silhouette score
print(f'Silhouette Score: {sil_score:.2f}')
