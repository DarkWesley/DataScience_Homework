import numpy as np
#输入矩阵
data = np.array([[1, -1, 4],
                 [2, 1, 3],
                 [1, 3, -1]])
A = np.cov(data, bias=False)
#求解特征值和其对应的特征向量
eigval,eigvec = np.linalg.eig(A)
for i in range(len(eigval)):
    print(f'特征值：{eigval[i]}\n对应的特征向量:\n{eigvec[i]}\n')