import numpy as np

a = np.fromfile("1.bin",  dtype=np.float32)
print(type(a))
print(a.shape)
print(a)
