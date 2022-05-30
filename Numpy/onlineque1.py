import numpy as np

a = list(map(int , input().split()))

a = np.array(a , dtype=float)

out = a[::-1]
print(out)