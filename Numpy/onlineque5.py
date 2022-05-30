import numpy as np

r , c = list(map(int , input().split()))
lstfinal = []
for i in range(0,r):
    lst  = list(map(int , input().split()))
    lstfinal.append(lst)

lst = np.array(lstfinal).reshape(r ,c )

out = lst.T
out2 = np.ravel(lst)

print(out)
print(out2)