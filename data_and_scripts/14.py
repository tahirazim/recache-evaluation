# Credit: Josh Hemann

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from collections import namedtuple
import matplotlib

matplotlib.rcParams.update({'font.size': 30})
matplotlib.rcParams.update({'figure.autolayout': True})


fo = open("14.txt", "r")

tarr = []
sarr1 = []
sarr2 = []
sarr3 = []
sarr4 = []
sarr5=[]
sarr6=[]
sarr7=[]
sarr8=[]

fo.readline()

while True:
  str = fo.readline();
  if str == "":
    break;

  strArr = str.split('\t')


  if strArr[1]:
    tarr.append(int(strArr[0]))
    sarr1.append(float(strArr[1]))
    sarr2.append(float(strArr[2]))
    sarr3.append(float(strArr[3]))
    sarr4.append(float(strArr[4]))
    sarr5.append(float(strArr[5]))
    sarr6.append(float(strArr[6]))
    sarr7.append(float(strArr[7]))
    sarr8.append(float(strArr[8]))



# Data for plotting
t = np.array(tarr)
s1 = np.array(sarr1)
s2 = np.array(sarr2)
s3 = np.array(sarr3)
s4 = np.array(sarr4)
s5 = np.array(sarr5)
s6 = np.array(sarr6)
s7 = np.array(sarr7)
s8 = np.array(sarr8)


n_groups = 4

fig, ax = plt.subplots( figsize=(20,7.5) )

index = np.arange(n_groups)+0.05
bar_width = 0.12


rects1 = ax.bar(index, s1, bar_width,
                color='#014686',
                label='ReCache')

rects2 = ax.bar(index + 1*bar_width, s8, bar_width,
                color='white',
                label='Cost-based(MonetDB)')


rects3 = ax.bar(index + 2*bar_width, s7, bar_width,
                color='white',hatch='/',
                label='Cost-based(Vectorwise)')



rects4 = ax.bar(index + 3*bar_width, s2, bar_width,
                color='red',alpha=0.8,
                label='LRU')

rects5 = ax.bar(index + 4*bar_width, s3, bar_width,
                color='#d0d0d0',
                label='LRU (JSON>>CSV)')

rects6 = ax.bar(index + 5*bar_width, s4, bar_width,
                color='#d0d0d0',hatch='+',
                label='Offline(farthest-first)')

rects7 = ax.bar(index + 6*bar_width, s5, bar_width,
                color='black',
                label='Offline(log-optimal)')


plt.yticks(np.arange(0, 8001, 2000) )

ax.set_xlabel('Cache Size (GB)', fontsize=32)
ax.set_ylabel('Execution Time (s)', fontsize=36)
ax.set_xticks(index + 7 * bar_width / 2)
ax.set_xticklabels((1, 2, 4, 8))
#ax.legend(fontsize=25, framealpha=0.0, borderpad=0)
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,ncol=3,fontsize=31,
           mode="expand", borderaxespad=0.)



fig.tight_layout()
plt.savefig('lru_vs_cost_based_exec_time.pdf', dpi=200, bbox_inches='tight')
