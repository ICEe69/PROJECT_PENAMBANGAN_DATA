import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

# 1. Membaca data dari file CSV
file_name = "nilai82.csv"  # Ganti dengan nama file Anda
df = pd.read_csv(file_name)

# Menampilkan 5 baris pertama untuk memastikan data terbaca dengan benar
print("Data Awal:")
print(df.head())

# 2. Standarisasi Data
scaler = StandardScaler()
data_scaled = scaler.fit_transform(df[['UTS', 'SAS']])  # Hanya kolom numerik

# 3. Menentukan jumlah klaster optimal dengan Elbow Method
inertias = []
range_k = range(1, 11)

for k in range_k:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(data_scaled)
    inertias.append(kmeans.inertia_)

# Visualisasi Elbow Method
plt.figure(figsize=(1, 10))
plt.plot(range_k, inertias, marker='o', linestyle='--')
plt.xlabel('Jumlah Klaster (k)')
plt.ylabel('Inertia (Sum of Squared Distances)')
plt.title('Elbow Method untuk Menentukan Jumlah Klaster Optimal')
plt.show()

# 4. Menentukan jumlah klaster (k optimal) - Ganti dengan hasil Elbow Method
k_optimal = 3
kmeans = KMeans(n_clusters=k_optimal, random_state=42)
df['Cluster'] = kmeans.fit_predict(data_scaled)

# Menampilkan hasil klasterisasi
print("\nHasil Klasterisasi:")
print(df)

# 5. Visualisasi Hasil Klaster dalam Grafik 2D
plt.figure(figsize=(8, 5))
for cluster in range(k_optimal):
    cluster_data = df[df['Cluster'] == cluster]
    plt.scatter(cluster_data['UTS'], cluster_data['SAS'], label=f'Klaster {cluster}')

# Menambahkan centroid ke grafik
centroids = scaler.inverse_transform(kmeans.cluster_centers_)
plt.scatter(centroids[:, 0], centroids[:, 1], s=200, c='red', marker='X', label='Centroid')

plt.xlabel('UTS')
plt.ylabel('SAS')
plt.title('Visualisasi Klaster dengan K-Means')
plt.legend()
plt.show()

# 6. Evaluasi Silhouette Score (Opsional)
silhouette_avg = silhouette_score(data_scaled, df['Cluster'])
print(f"\nSilhouette Score untuk {k_optimal} klaster: {silhouette_avg:.2f}")

# 7. Menyimpan hasil klaster ke file baru
df.to_csv("hasil_klaster.csv", index=False)
print("\nHasil klaster telah disimpan ke file 'hasil_klaster.csv'")
