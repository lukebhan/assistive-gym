import matplotlib.pyplot as plt
import numpy as np

dir_paths = ["model_normal_tremor", "model_limits_normal", "model_weakness_normal"]
filename = "monitor.csv"
plt.figure()
for dir_path in dir_paths:
    print(dir_path)
    reward_arr = [];
    mean_arr = []
    count = 0
    with open(dir_path + "/" + filename, 'r') as fin:
        line = fin.readline()
        while line:
            values = line.split(",")
            print(values)
            if count >= 2:
                if(dir_path == dir_paths[1]):
                    if count % 2 != 0:
                        reward_arr.append(float(values[0]))
                        mean_arr.append(np.mean(reward_arr[-50:]))
                else:
                    reward_arr.append(float(values[0]))
                    mean_arr.append(np.mean(reward_arr[-50:]))
            line = fin.readline()
            count += 1
    plt.plot(mean_arr, label=dir_path)
plt.legend()
plt.show()
