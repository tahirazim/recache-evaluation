import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import sys

matplotlib.rcParams.update({'font.size': 24})
matplotlib.rcParams.update({'figure.autolayout': True})


fo = open("11a.txt", "r")

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
fig, ax = plt.subplots(figsize=(8,4.75) )


ax.plot(t, s2, '-+', markersize=10, color='#c2c2c2', linewidth=4, label="Rel. Columnar")
ax.plot(t, s1, '-x', markersize=8,color='#ff430f', linewidth=4, label="Parquet")

plt.yticks(np.arange( -20, 80, 20))


legend = ax.legend(loc='upper left',  framealpha=0.0, fontsize=24, 
                   borderpad=0)

ax.set_xlabel('Percentage of Queries with \n Nested Attributes', fontsize=24);
ax.set_ylabel('%age Time Reduction', fontsize=24);


#ax.grid()

fig.savefig("symantec_varying_nested_attributes.pdf", dpi=200, bbox_inches='tight')
#plt.show()
