import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import sys

matplotlib.rcParams.update({'font.size': 32})
matplotlib.rcParams.update({'figure.autolayout': True})


fo = open("12b.txt", "r")

tarr = []
sarr1 = []
sarr2 = []
sarr3 = []
sarr4 = []
sarr5 = []

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



# Data for plotting
t = np.array(tarr)
s1 = np.array(sarr1)
s2 = np.array(sarr2)
s3 = np.array(sarr3) 
s4 = np.array(sarr4)
s5 = np.array(sarr5)


# Note that using plt.subplots below is equivalent to using
# fig = plt.figure and then ax = fig.add_subplot(111)
print plt.figure().get_size_inches()
fig, ax = plt.subplots(figsize=(8,6))
plt.xticks(np.arange( 0, 51, 10))


ax.plot(s4, t, color='#a2a2a2', linewidth=6, label="Lazy Caching")
ax.plot(s1, t, linestyle='--', color='#014686', linewidth=6, label="ReCache (T=1%)")
ax.plot(s2, t, linestyle='-', color='#014686', linewidth=4, label="ReCache (T=10%)")
ax.plot(s5, t, linestyle='--', color='#a2a2a2', linewidth=4, label="ReCache (T=20%)")
ax.plot(s3, t, color='#FF0000', linewidth=7, linestyle=':', label="ReCache (T=50%)")


legend = ax.legend(loc='lower left',  framealpha=0.0, fontsize=28, 
                   borderpad=0, bbox_to_anchor=(0.133, -0.025) )

ax.set_xlabel('Percentage Overhead', fontsize=32);
ax.set_ylabel('CDF', fontsize=32);


#ax.grid()

fig.savefig("lazy_vs_eager_vs_cost_adaptive_overhead_vs_threshold.pdf", dpi=200, bbox_inches='tight')
#plt.show()
