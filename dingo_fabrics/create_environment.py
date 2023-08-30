import os
import gymnasium as gym
import numpy as np

from urdfenvs.robots.generic_urdf import GenericUrdfReacher

def init_env(n_steps=1000, render=False):

    abs_path = os.path.dirname(os.path.abspath(__file__))
    urdf_file = abs_path + '/urdf/dingo_o.urdf'

    robots = [
        GenericUrdfReacher(urdf=urdf_file, mode="vel"),
    ]
    env = gym.make(
        "urdf-env-v0",
        dt=0.01, robots=robots, render=render
    )
    env.reset()
    return env


