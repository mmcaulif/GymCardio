from typing import NamedTuple
import torch as th
import numpy as np
import jax.numpy as jnp

class BaseTransition(NamedTuple):
    s: list  # state
    a: float  # action
    r: float  # reward
    s_p: list  # next state
    d: int  # done

    def __call__(self):
        s = self.s
        a = self.a
        r = self.r
        s_p = self.s_p
        d = self.d
        return s, a, r, s_p, d

class TorchTransition(BaseTransition):

    def __call__(self):
        s = th.from_numpy(np.array(self.s)).float()
        a = th.from_numpy(np.array(self.a)).unsqueeze(1).float()
        r = th.from_numpy(np.array(self.r)).unsqueeze(1).float()
        s_p = th.from_numpy(np.array(self.s_p)).float()
        d = th.from_numpy(np.array(self.d)).unsqueeze(1).int()
        return s, a, r, s_p, d
    
class JaxTransition(BaseTransition):

    def __call__(self):
        s = jnp.asarray(np.array(self.s))
        a = jnp.asarray(np.array(self.a))
        r = jnp.expand_dims(jnp.asarray(np.array(self.r)), -1)
        s_p = jnp.asarray(np.array(self.s_p))
        d = jnp.expand_dims(jnp.asarray(np.array(self.d)), -1)
        return s, a, r, s_p, d
    