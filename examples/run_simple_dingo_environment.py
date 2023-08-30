from dingo_fabrics.create_environment import init_env

if __name__ == "__main__":
    env = init_env()
    for _ in range(100):
        env.step()
