import matplotlib.pyplot as plt
import numpy as np

dir_path = "model_random"
filename = "monitor.csv"

reward_arr = [];
mean_arr = []
count = 0
with open(dir_path + "/" + filename, 'r') as fin:
    line = fin.readline()
    while line:
        values = line.split(",")
        if count >= 2:
            reward_arr.append(float(values[0]))
            mean_arr.append(np.mean(reward_arr[-50:]))
        line = fin.readline()
        count += 1
plt.figure()
print(reward_arr)
plt.plot(mean_arr)
plt.show()
