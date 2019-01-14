import numpy as np

m,n = map(int, input().split(" "))

x = np.array([input().split() for i in range(n)], int)

print(np.prod(np.sum(x,axis = 0),dtype = np.int))
