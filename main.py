import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("quran_data.csv")

# 1. Bar Chart - Jumlah Ayat per Surat
ayat_per_surat = df.groupby("nama_surat")["ayat"].count()
plt.figure(figsize=(40, 6))
ayat_per_surat.sort_values().plot(kind='bar', color='skyblue')
plt.title("Jumlah Ayat per Surat")
plt.xlabel("Nama Surat")
plt.ylabel("Jumlah Ayat")
plt.xticks(rotation=70)
plt.savefig("nama_surat.svg", format='svg', bbox_inches='tight', dpi=300)
plt.show()

# 2. Pie Chart - Distribusi Surat Berdasarkan Tempat Turun
tempat_turun_counts = df.drop_duplicates(subset=["nama_surat"])["tempat_turun"].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(tempat_turun_counts, labels=tempat_turun_counts.index, autopct='%1.1f%%', colors=["lightcoral", "lightskyblue"])
plt.title("Distribusi Surat Berdasarkan Tempat Turun")
plt.savefig("distribusi_surat_turun.svg", format='svg', bbox_inches='tight', dpi=300)
plt.show()

# 3. Boxplot - Panjang Ayat dalam Setiap Surat
df["panjang_ayat"] = df["surat"].apply(lambda x: len(str(x)))
plt.figure(figsize=(40, 6))
sns.boxplot(x="nama_surat", y="panjang_ayat", data=df, palette="coolwarm")
plt.xticks(rotation=70)
plt.title("Panjang Ayat dalam Setiap Surat")
plt.xlabel("Nama Surat")
plt.ylabel("Panjang Ayat (karakter)")
plt.savefig("panjang_ayat.svg", format='svg', bbox_inches='tight', dpi=300)
plt.show()
