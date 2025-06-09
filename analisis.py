import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# URL RAW del CSV en GitHub
url_csv = 'https://raw.githubusercontent.com/derekvc/dataset/main/uso_ram_procesos_20250609_084506.csv'

# Leer el dataset con separador por defecto (usa coma si no especificaste ';' al guardarlo)
df = pd.read_csv(url_csv)

# Verifica estructura
print("\n🔍 Primeras filas del dataset:")
print(df.head())

# Estadísticas básicas
print("\n📊 Estadísticas básicas:")
print(df[['rss_MB', 'vms_MB']].describe())

# Mediana
print("\n🔸 Mediana:")
print(df[['rss_MB', 'vms_MB']].median())

# Moda
print("\n🔸 Moda:")
print(df[['rss_MB', 'vms_MB']].mode().iloc[0])

# Desviación estándar
print("\n🔸 Desviación estándar:")
print(df[['rss_MB', 'vms_MB']].std())

# Matriz de correlación
print("\n🔗 Matriz de correlación:")
print(df[['rss_MB', 'vms_MB']].corr())

# Visualización
sns.heatmap(df[['rss_MB', 'vms_MB']].corr(), annot=True, cmap='coolwarm')
plt.title('Correlación entre uso de memoria RSS y VMS')
plt.show()
