import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import sys

matplotlib.rcParams.update({'font.size': 28})
matplotlib.rcParams.update({'figure.autolayout': True})


fo = open("10b.txt", "r")

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
fig, ax = plt.subplots(figsize=(8,6))



ax.plot(t, s2, color='#c2c2c2', linewidth=6, label="Rel. Columnar")
ax.plot(t, s1, color='#ff430f', linewidth=4, label="Parquet")
ax.plot(t, s3, linestyle='--', color='#014686', linewidth=4, label="ReCache")

legend = ax.legend(loc='lower left',  framealpha=0.0, fontsize=28, 
                   borderpad=0,bbox_to_anchor=(-0.02, 0.55))

ax.set_xlabel('Query Sequence', fontsize=28);
ax.set_ylabel('Cumulative Exec. Time (s)', fontsize=28);


#ax.grid()

fig.savefig("spam_2000_onlyjson_b.pdf", dpi=200, pad_inches=0)
#plt.show()
