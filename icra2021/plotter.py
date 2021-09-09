import matplotlib.pyplot as plt
import numpy as np

dir_path = "model"
filename = "monitor.csv"

reward_arr = []
mean_arr = []
count = 0 
with open(dir_path + "/" + filename, 'r') as fin:
	line = fin.readline()
	while line:
		values = line.split(",")
		if count >= 2:
			reward_arr.append(float(values[0]))
			if(len(reward_arr) > 5):
				mean_arr.append(np.mean(reward_arr[-20:]))
		line = fin.readline()
		count += 1
plt.figure()
plt.plot(mean_arr)
plt.show()
plt.figure()
plt.plot(reward_arr)
plt.show()
