import gym, assistive_gym
import pybullet as p
import numpy as np

env = gym.make('DressingBaxter-v1')
env.render()
obs = env.reset()
