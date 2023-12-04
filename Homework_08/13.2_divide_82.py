from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
iris = load_iris()
x = iris.data #特征矩阵
y = iris.target #目标向量
x_train, x_test, y_train, y_test = train_test_split(x, y,test_size=0.2, random_state=23)
print("训练集:", len(x_train))
print("测试集:", len(x_test))