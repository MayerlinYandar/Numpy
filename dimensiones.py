import numpy as np
#0 d
scalar = np.array(42)
print(scalar)
print(scalar.ndim)
#1 d
vector = np.array([1,2,3])
print(vector)
print(vector.ndim)
#2 d
matriz = np.array([[2,4,1],[5,6,3]])
print(matriz)
print(matriz.ndim)
# n d
tensor = np.array([[[2,4,1],[5,6,3],[9,8,7],[0,0,0]]])
print(tensor)
print(tensor.ndim)
