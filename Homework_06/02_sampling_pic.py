import numpy as np
import matplotlib.pyplot as plt
samples = np.random.normal(0, 1, 100)

# 绘制直方图
plt.hist(samples, bins=20,density=True,edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Samples')
# 绘制分布函数
plt.plot(np.sort(samples), 1/(np.sqrt(2 * np.pi)) * np.exp(- (np.sort(samples))**2 /2), color='black')
# 显示图表
plt.show()