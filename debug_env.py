import gymnasium as gym
from gymnasium import spaces
import numpy as np

class CardioDebugEnv(gym.Env):
    def __init__(self, maxlen=10, discrete=True) -> None:
        self.maxlen = maxlen
        self.discrete = discrete
        self._reset_env_vars()

        self.action_space = spaces.Discrete(2)
        self.observation_space = spaces.Box(0, self.maxlen, dtype=np.float32)

    def step(self, action):
        self.count +=1        
        state = np.ones(5)*self.count
        state[-1] = action
        if self.count == self.maxlen:
            return np.array(state), 1, True, False, {}
        
        return np.array(state), 1, False, False, {}        

    def reset(self):
        self._reset_env_vars()
        return np.ones(5)*self.count, {}

    def _reset_env_vars(self):
        self.count = 0

def main():
    env = CardioDebugEnv()

    s_t = env.reset()
    while True:
        print(s_t)
        a_t = env.action_space.sample()
        s_tp1, r, d, t, i = env.step(a_t)
        print(s_t, a_t, s_tp1, r, d)
        s_t = s_tp1
        if d:
            break

if __name__ == '__main__':
    main()
