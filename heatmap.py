import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Consum_d_aigua_a_Catalunya_per_comarques_20241104.csv")

heatmap_data = data.pivot_table(
    index='Comarca', 
    columns='Any', 
    values='Consum domèstic per càpita'
)
cmap = sns.light_palette("blue", as_cmap=True)
plt.figure(figsize=(12, 8))  # Ajusta la mida de la figura segons sigui necessari
sns.heatmap(heatmap_data, annot=False, linewidths=0.01, linecolor='white')
plt.title('Consum domèstic per càpita per Any i Comarca')
plt.xlabel('Any')
plt.ylabel('Comarca')
plt.show()