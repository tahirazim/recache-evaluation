import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import sys

matplotlib.rcParams.update({'font.size': 32})
matplotlib.rcParams.update({'figure.autolayout': True})


fo = open("7.txt", "r")

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
    tarr.append(float(strArr[0]))
    sarr1.append(float(strArr[1]))


# Data for plotting
t = np.array(tarr)
s1 = np.array(sarr1)

# Note that using plt.subplots below is equivalent to using
# fig = plt.figure and then ax = fig.add_subplot(111)
print plt.figure().get_size_inches()
fig, ax = plt.subplots( figsize=(13,5.75) )



ax.plot(t, s1, color='#0000ff', linewidth=7, label="Eager Caching")

plt.yticks(np.arange( 0, 110, 20))


ax.set_xlabel('Percentage Error', fontsize=35);
ax.set_ylabel('CDF', fontsize=35);

ax.grid(color="#b2b2b2", linestyle='dashed')

fig.savefig("cost_model_validation.pdf", dpi=200,  bbox_inches='tight')
#plt.show()
