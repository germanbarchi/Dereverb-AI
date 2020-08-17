import numpy as np

def pad_upto(x,N):
  return np.pad(x,((0,N-len(x))))