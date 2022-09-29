

import seaborn as sns; import matplotlib.pyplot as plt
import os; import numpy as np; import pandas as pd

sns.set(rc={'figure.figsize':(10,4)})

home = os.path.expanduser('~')
fn = os.path.join(home, 'Downloads/sim_cbgt_network_firing_rates_str_only.csv')

df = pd.read_csv(fn)



sns.set(font_scale=1.5, style='whitegrid'); pal=['red', 'blue']; g = sns.relplot(x="time",
y="firing_rate",data=df,col="nucleus",hue="action_channel",kind="line",col_wrap=2,
facet_kws={'sharey': True},col_order=["D1STR","D2STR"],n_boot=1000,estimator=np.mean,
linewidth=3.9, aspect=1.4, palette=pal, style='rt_speed', sizes={'Fast':3.9,'Slow':1.5},
size='rt_speed',legend=False);
g.set_xlabels('Time (ms)'); g.set_ylabels('Firing Rate (spikes/s)')
g.set_titles("")

for i,ax in enumerate(g.axes):
   plt.setp(ax.collections[1],alpha=0.1)
   plt.setp(ax.collections[3],alpha=0.1)

plt.tight_layout()
plt.savefig(os.path.join(home, 'Downloads/firing_rates.png'))
plt.savefig(os.path.join(home, 'Downloads/firing_rates.pdf'))

plt.show()
