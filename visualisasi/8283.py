import pandas as pd

# Ganti dengan nama file Excel Anda
excel_file = "8182.xlsx"  # File Excel yang akan dibaca
csv_file = "8283.csv"     # Nama file CSV output

# Membaca file Excel dengan baris pertama sebagai header
df = pd.read_excel(excel_file, header=0)

# Menangani nilai yang tidak valid atau kosong, dan mengonversi kolom ke tipe numerik (jika perlu)
df['Raport'] = pd.to_numeric(df['Raport'], errors='coerce')

# Mengonversi kolom UTS dan SAS menjadi integer
df['Raport'] = df['Raport'].fillna(0).astype(int)  # Mengganti NaN dengan 0 lalu mengonversi ke integer


# Menyimpan data ke dalam format CSV
df.to_csv(csv_file, index=False)  # Menyimpan sebagai CSV

print(f"File berhasil dikonversi ke {csv_file}")
