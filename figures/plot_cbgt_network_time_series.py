import pandas as pd; import numpy as np; import matplotlib.pyplot as plt; import seaborn as sns


df = pd.read_csv('/home/zetetic/Downloads/sim_cbgt_network_time_series_clean.csv')

sns.set(font_scale=1.5, style='whitegrid')


fig, ax = plt.subplots(1, 1, figsize=(10, 4))
plt.axvline(10, color='darkgray', linestyle='--', linewidth=3)
plt.axvline(20, color='darkgray', linestyle='--', linewidth=3)
plt.axvline(30, color='darkgray', linestyle='--', linewidth=3)
plt.axhline(0.5, color='darkgray', linestyle='--', linewidth=1.5)
sns.lineplot(ax=ax, x='trial', y='p_left', color='red', data=df);
sns.despine(); plt.xlabel('Block'); plt.ylabel('P(Choice=Left)')
plt.tight_layout()


plt.savefig('/home/zetetic/Desktop/loki_figs/sim_cbgt_network_time_series.png', dpi=300)
plt.savefig('/home/zetetic/Desktop/loki_figs/sim_cbgt_network_time_series.png', dpi=300)
