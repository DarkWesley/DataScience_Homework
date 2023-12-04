import numpy as np
data = np.array([[1, -1, 4],
                 [2, 1, 3],
                 [1, 3, -1]])
C = np.cov(data, bias=False)
print("协方差矩阵C为:")
print(C)