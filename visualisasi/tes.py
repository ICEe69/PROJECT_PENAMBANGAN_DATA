import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import seaborn as sns

# Load data (ganti 'nilai_rapor.csv' dengan nama file Anda)
data = pd.read_csv('82.csv')

# Pilih fitur nilai
X = data[['Raport']]

# Clustering dengan 3 cluster (contoh)
kmeans = KMeans(n_clusters=4, init='k-means++', random_state=42)
y_kmeans = kmeans.fit_predict(X)

# Tambahkan kolom cluster ke DataFrame
data['cluster'] = y_kmeans

# Hitung rata-rata nilai per cluster
cluster_means = data.groupby('cluster')['Raport'].mean().sort_values()

# Pemetaan keterangan cluster berdasarkan urutan rata-rata nilai
cluster_labels = {
    cluster_means.index[0]: 'Kurang Memahami', 
    cluster_means.index[1]: 'Baik', 
    cluster_means.index[2]: 'Cukup Faham', 
    cluster_means.index[3]: 'Sangat Memahami'
}

# Ganti nilai cluster dengan label
data['keterangan'] = data['cluster'].map(cluster_labels)

# Visualisasi
plt.figure(figsize=(10, 6))
sns.countplot(x='keterangan', data=data)
plt.title('Distribusi Tingkat Pemahaman Siswa')
plt.xlabel('Tingkat Pemahaman')
plt.ylabel('Jumlah Siswa')
plt.show()

# Tampilkan data untuk memastikan pemetaan keterangan sudah benar
print(data[['Nama', 'Raport', 'keterangan']])
