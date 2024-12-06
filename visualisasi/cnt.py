import pandas as pd
import numpy as np
from sklearn.cluster import KMeans

# Misal dataset memiliki satu kolom nilai
data = pd.read_excel('8182.xlsx')  # Ganti sesuai nama file dan sheet
values = data['Raport']  # Ganti sesuai nama kolom yang sesuai

# K-Means dengan centroid awal yang ditentukan
initial_centroids = np.array([[65], [73], [78]])
kmeans = KMeans(n_clusters=3, init=initial_centroids, n_init=1, max_iter=300, random_state=42)

# Fitting model
kmeans.fit(values.values.reshape(-1, 1))

# Centroids dan jumlah iterasi
print(f"Centroids akhir: {kmeans.cluster_centers_}")
print(f"Jumlah iterasi: {kmeans.n_iter_}")
