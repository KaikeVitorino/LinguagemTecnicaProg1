import numpy as np
import matplotlib.pyplot as plt

m = [[1,2,3],
     [3,1,2],
     [2,3,1]]

print(m)
s = 1
for i in range(len(m[0])):
    for j in range(len(m[0])):
        if j == i:
            s=s+m[i][j]
            print(m[i][j])
print("Produto da diagonal", s)

# usando mports

m = np.array([[1,2,3],
              [3,1,2],
              [2,3,1]])
print(m)
