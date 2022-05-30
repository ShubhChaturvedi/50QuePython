import numpy as np

lst1 = ["shu" , "chatur" , "i" , "brill"]
lst2 = ["bh" , "vedi" , "s" , "ient"]

lst1 = np.array(lst1)
lst2 = np.array(lst2)

lst3 = np.char.add(lst1 , lst2)

print(lst3)