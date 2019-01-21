import pandas as pd
import quandl
quandl.ApiConfig.api_key = "WeADDwzQZcKWGrkGkbhH"
mydata = quandl.get_table('WIKI/PRICES', ticker='AAPL')
yrlist = pd.DatetimeIndex(mydata['date']).year
yr5_data = mydata[(yrlist >= 2012) & (yrlist <= 2017)]
yr5_close = yr5_data.loc[:,['date','adj_close']]
ts = yr5_close.set_index('date')

import matplotlib.pyplot as plt
%matplotlib inline

groups = [g for n, g in ts.groupby(pd.Grouper(freq='A'))]
years_val = [list(groups[j]['adj_close']) for j in range(len(groups))]
years_ind = [str(groups[j].index[0].year) for j in range(len(groups))]
for yval in years_val:
     yval[:] = [x for x in yval if x is not None]
fig, ax = plt.subplots(figsize=(5, 5))
plt.rcParams.update({'font.size': 10})

bp = ax.boxplot(years_val, patch_artist=True, showfliers=False)
colors = ['pink', 'lightblue', 'lightgreen', 'lightsalmon' ,'dodgerblue', 'lightseagreen']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
# enable horizontal gridlines
# ax.yaxis.grid(True)
#plt.setp(bp['whiskers'], color='#1f77b4')
#plt.setp(bp['boxes'], color='#1f77b4')
#plt.setp(bp['fliers'], color='#1f77b4')
plt.setp(bp['medians'], color='k')
#for patch in bp['boxes']:
#    patch.set(facecolor='w')
ax.set_xticklabels(years_ind, rotation=30)
plt.show()