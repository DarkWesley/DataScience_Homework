import numpy as np
A = np.array([[2, 1], [4, 5]])
n = A.shape[0]
x = np.random.randn(n)
max_iter = 1000
tol = 1e-6

for i in range(max_iter):
    y = np.dot(A, x)
    lmd = np.dot(x, y) / np.dot(x, x)
    err = np.linalg.norm(y - lmd * x)
    if err < tol:
        break
    x = y / np.linalg.norm(y)
print('矩阵A的最大特征值为：', lmd)