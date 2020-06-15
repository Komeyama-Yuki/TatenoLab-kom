import numpy as np

n = 3
m = 4

mat_Ab = np.array([
    [2.0, 3.0, 3.0, 1.0],
    [1.0, 2.0, 3.0, 2.0],
    [3.0, 2.0, 1.0, 2.0]
])

print(mat_Ab)

for k in range(n):
    for j in range(k + 1, m):
        mat_Ab[k][j] /= mat_Ab[k][k]
    mat_Ab[k][k] = 1.0
    print(mat_Ab)
    for i in range(n):
        if i == k:
            continue
        for j in range(k + 1, m):
            mat_Ab[i][j] -= mat_Ab[i][k] * mat_Ab[k][j]
        mat_Ab[i][k] = 0.0
    print(mat_Ab)
