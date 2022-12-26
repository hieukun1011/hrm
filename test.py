import numpy as np

R = np.random.randint(low=0, high=100, size=(12, 12))
print(R)
# print(len(R))
d = np.arange(1, R.size, 12)
print(d)