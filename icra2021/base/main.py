import gym, assistive_gym
import pybullet as p
import numpy as np
import os
from stable_baselines3 import PPO
from stable_baselines3.common.results_plotter import load_results, ts2xy, plot_results
from stable_baselines3.common.monitor import Monitor
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.common.callbacks import CheckpointCallback
log_dir = "model"
os.makedirs(log_dir, exist_ok=True)
env = gym.make("ScratchItchJacoHuman-v1")
env = Monitor(env, log_dir)

model = PPO.load("model_normal_tremor/model_2000000_steps")
model.set_env(env)
callback = CheckpointCallback(save_freq=1000, save_path = log_dir, name_prefix = 'model')
model.learn(total_timesteps=1000000, callback=callback)
