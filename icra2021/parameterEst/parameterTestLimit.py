import gym, assistive_gym
import pybullet as p
import numpy as np
import os
from stable_baselines3 import PPO

env = gym.make("ScratchItchJacoHuman-v1")
model = PPO.load("model/model_400000_steps")
success_arr = []
for j in range(100):
    print(j)
    obs = env.reset()
    for i in range(200):
        act = model.predict([obs])[0]
        obs, rew, done, info  = env.step(act[0])
    print(info)
    success_arr.append(info["human"]["task_sucess_value"])
np.savetxt("limit.dat", success_arr)
