# import numpy as np
import pandas as pd

arr = np.array(list((x.split())), dtype=int)
arr = arr.reshape(20, 20)
arr_m = np.zeros((20, 20))
for i in range(0, 17):
    for j in range(0, 17):
        x = [k for k in range(i, i + 4)]
        y = [k for k in range(j, j + 4)]
        arr_m[i, j] = max(arr[i, j: j + 4].prod(), arr[i:i + 4, j].prod(), arr[x, y].prod(), )

print(arr_m.max())

arr1 = np.zeros((20, 20), dtype=int)
arr2 = np.zeros((20, 20), dtype=int)
arr3 = np.zeros((20, 20), dtype=int)

for i in range(0, 20):
  arr1[:, i] = arr[:, i: i+4].prod(1)

for i in range(0, 20):
  arr2[i, :] = arr[i:i+4, :].prod(0)

for i in range(0, 20):
  for j in range(0, 20):
    arr3[i,j] = arr[i: i+4, j: j+4].diagonal().prod()

max(arr1.max(), arr2.max(), arr3.max())
