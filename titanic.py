import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns

#df = data frame
#\n = untuk membuat baris baru

# Load dataset contoh dari seaborn
df = sns.load_dataset('titanic')

# Tampilkan 5 data pertama
print("\nPreview Data:")
print(df.head())

# Informasi dataset
print("\nInformasi Dataset:")
print(df.info())

# Cek missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Statistik Deskriptif
print("\nStatistik Deskriptif:")
print(df.describe())

# Visualisasi distribusi umur
plt.figure(figsize=(8,5))
sns.histplot(df['age'].dropna(), bins=20, kde=True)
plt.title('Distribusi Umur Penumpang Titanic')
plt.xlabel('Umur')
plt.ylabel('Jumlah Penumpang')
plt.show()
