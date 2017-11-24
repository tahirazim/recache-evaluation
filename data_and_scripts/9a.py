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
fig, ax = plt.subplots(figsize=(8,5.75))



ax.semilogy(t, s3, color='#c2c2c2', linewidth=6, label="Rel. Columnar")
ax.semilogy(t, s2, color='#ff434f', linewidth=4, label="Parquet")
ax.semilogy(t, s1, linestyle='--', color='#014686', linewidth=2, label="ReCache")

legend = ax.legend(loc='best',  framealpha=0.0, fontsize=24, 
                   bbox_to_anchor=(0.415, 0.645), borderpad=0)

ax.set_xlabel('Query Sequence', fontsize=24);
ax.set_ylabel('Execution Time (s)', fontsize=24);


#ax.grid()

fig.savefig("dremel_vs_columnar_vs_auto.pdf", dpi=200, bbox_inches='tight')
#plt.show()
