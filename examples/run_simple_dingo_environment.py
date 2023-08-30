import numpy as np
from dingo_fabrics.create_environment import init_env

if __name__ == "__main__":
    env = init_env(render=True)
    action = np.array([0.3, 0.4, 1.0])
    for _ in range(1000):
        env.step(action)
