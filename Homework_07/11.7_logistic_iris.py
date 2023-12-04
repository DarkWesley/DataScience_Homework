import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
iris = load_iris()
x, y = iris.data, iris.target
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=23)
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)
# 创建Logistic回归模型
model = LogisticRegression(solver='lbfgs', multi_class='auto', max_iter=100000)
model.fit(x_train, y_train)
y_predict = model.predict(x_test)
accuracy = accuracy_score(y_test, y_predict)
print(f"分类准确度：{accuracy}")
print("分类报告：")
print(classification_report(y_test, y_predict))
print("混淆矩阵：")
print(confusion_matrix(y_test, y_predict))