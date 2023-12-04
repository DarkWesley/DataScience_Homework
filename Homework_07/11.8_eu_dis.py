import numpy as np
from sklearn.datasets import load_iris
iris = load_iris()
x, y = iris.data, iris.target
unique_labels = np.unique(y)
class_centers = {}
for label in unique_labels:
    class_samples = x[y == label]
    class_center = np.mean(class_samples, axis=0)
    class_centers[label] = class_center
for label, center in class_centers.items():
    print(f"类别 {label} 的中心点：{center}")