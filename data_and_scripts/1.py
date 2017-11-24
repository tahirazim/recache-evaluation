import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import sys

matplotlib.rcParams.update({'font.size': 22})
matplotlib.rcParams.update({'figure.autolayout': True})


fo = open("9a.txt", "r")

tarr = []
sarr1 = []
sarr2 = []
sarr3 = []

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

# Data for plotting
t = np.array(tarr)
s1 = np.array(sarr1)
s2 = np.array(sarr2)
s3 = np.array(sarr3) 


# Note that using plt.subplots below is equivalent to using
# fig = plt.figure and then ax = fig.add_subplot(111)
fig, ax = plt.subplots(figsize=(9,6.5))

negy = -0.06
ax.annotate('All attributes', fontsize=17,annotation_clip=False,
            xy=(85, negy-0.01), xycoords='data')

ax.annotate('Only non-nested attributes', fontsize=17,annotation_clip=False,
            xy=(325, negy-0.01), xycoords='data')

plt.annotate(
    '', xy=(75, negy), xycoords='data',
    xytext=(0, negy), textcoords='data',annotation_clip=False,
    arrowprops={'arrowstyle': '<-' })

plt.annotate(
    '', xy=(220, negy), xycoords='data',
    xytext=(300, negy), textcoords='data',annotation_clip=False,
    arrowprops={'arrowstyle': '<-'})

plt.annotate(
    '', xy=(325, negy), xycoords='data',
    xytext=(300, negy), textcoords='data',annotation_clip=False,
    arrowprops={'arrowstyle': '<-'})

plt.annotate(
    '', xy=(590, negy), xycoords='data',
    xytext=(615, negy), textcoords='data',annotation_clip=False,
    arrowprops={'arrowstyle': '<-'})


ax.plot(t, s2, color='#ff434f', linewidth=4, label="Parquet")
ax.plot(t, s3, color='#111111', linewidth=1, label="Rel. Columnar")

plt.yticks(np.arange( 0, 0.51, 0.1))


legend = ax.legend(loc='best',  framealpha=0.0, fontsize=24, 
                   bbox_to_anchor=(0.415, 0.645), borderpad=0)

ax.set_xlabel('\nQuery Sequence', fontsize=24,fontweight='bold');
ax.set_ylabel('Execution Time (s)', fontsize=24,fontweight='bold');

#ax.grid()

fig.savefig( "dremel_vs_columnar_better.pdf" , dpi=200, bbox_inches='tight')
#plt.show()
