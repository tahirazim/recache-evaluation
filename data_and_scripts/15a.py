import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import sys

matplotlib.rcParams.update({'font.size': 32})
matplotlib.rcParams.update({'figure.autolayout': True})


fo = open("15a.txt", "r")

tarr = []
sarr1 = []
sarr2 = []
sarr3 = []
sarr4 = []

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


# Data for plotting
t = np.array(tarr)
s1 = np.array(sarr1)
s2 = np.array(sarr2)
s3 = np.array(sarr3) 
s4 = np.array(sarr4)

# Note that using plt.subplots below is equivalent to using
# fig = plt.figure and then ax = fig.add_subplot(111)
print plt.figure().get_size_inches()
fig, ax = plt.subplots(figsize=(10,8.5))
plt.xticks(np.arange( 0, 4001, 800))


ax.plot(t, s4, linestyle='-', color='#000000', linewidth=4, label="Columnar/LRU")
ax.plot(t, s3, color='#c2c2c2', linewidth=6, label="Columnar/Greedy")
ax.plot(t, s2, color='#ff000f', linewidth=3, label="Parquet/Greedy")
ax.plot(t, s1, linestyle='--', color='#014686', linewidth=4, label="ReCache")


legend = ax.legend(loc='best',  framealpha=0.0, fontsize=30, 
                   borderpad=0)

ax.set_xlabel('Query Sequence', fontsize=32);
ax.set_ylabel('Cumulative Exec. Time (s)', fontsize=32);


#ax.grid()

fig.savefig("symantec_overall.pdf", dpi=200, bbox_inches='tight')
#plt.show()
