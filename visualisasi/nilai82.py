import pandas as pd

# Ganti dengan nama file Excel Anda
excel_file = "82.xlsx"  # File Excel yang akan dibaca
csv_file = "82.csv"     # Nama file CSV output

# Membaca file Excel dengan baris pertama sebagai header
df = pd.read_excel(excel_file, header=0)

# Menangani nilai yang tidak valid atau kosong, dan mengonversi kolom ke tipe numerik (jika perlu)
df['UTS'] = pd.to_numeric(df['UTS'], errors='coerce')
df['SAS'] = pd.to_numeric(df['SAS'], errors='coerce')

# Mengonversi kolom UTS dan SAS menjadi integer
df['UTS'] = df['UTS'].fillna(0).astype(int)  # Mengganti NaN dengan 0 lalu mengonversi ke integer
df['SAS'] = df['SAS'].fillna(0).astype(int)  # Mengganti NaN dengan 0 lalu mengonversi ke integer

# Menyimpan data ke dalam format CSV
df.to_csv(csv_file, index=False)  # Menyimpan sebagai CSV

print(f"File berhasil dikonversi ke {csv_file}")
