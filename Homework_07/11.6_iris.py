from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import numpy as np
iris = load_iris()
x, y = iris.data, iris.target
np.random.seed(23)
indices = np.arange(len(x))
np.random.shuffle(indices)
x_shuffled = x[indices]
y_shuffled = y[indices]

# 划分数据集为训练集和测试集（3:7的比例）
x_train, x_test, y_train, y_test = train_test_split(x_shuffled, y_shuffled, test_size=0.3, random_state=23)
print(f"训练集大小：{len(x_train)}")
print(f"测试集大小：{len(x_test)}")