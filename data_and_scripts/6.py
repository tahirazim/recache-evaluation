import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import sys

matplotlib.rcParams.update({'font.size': 24})
matplotlib.rcParams.update({'figure.autolayout': True})


fo = open("6.txt", "r")

tarr = []
sarr1 = []
sarr2 = []

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


# Data for plotting
t = np.array(tarr)
s1 = np.array(sarr1)
s2 = np.array(sarr2)

# Note that using plt.subplots below is equivalent to using
# fig = plt.figure and then ax = fig.add_subplot(111)
print plt.figure().get_size_inches()
fig, ax = plt.subplots(figsize=(8,5) )


ax.plot(t, s1, '-+', markersize=8, color='#a2a2a2', linewidth=3, label="Rel. Columnar")
ax.plot(t, s2, '-x', markersize=5,color='#ff430f', linewidth=1, label="Parquet")

plt.yticks(np.arange( 0, 181, 30))


legend = ax.legend(loc='upper left',  framealpha=0.0, fontsize=24, 
                   borderpad=0)

ax.set_xlabel('Cardinality', fontsize=24);
ax.set_ylabel('Write Latency (s)', fontsize=24);


#ax.grid()

fig.savefig("dremel_vs_columnar_write_latency.pdf", dpi=200, bbox_inches='tight')
#plt.show()
