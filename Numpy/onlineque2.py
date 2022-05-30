import numpy as np

lst = list(map(int , input().split()))

lst = np.array(lst).reshape(3,3)

print(lst)