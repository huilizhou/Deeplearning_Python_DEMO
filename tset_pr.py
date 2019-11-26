
import matplotlib

import numpy as np
import matplotlib.pyplot as plt

plt.figure(1)  # 创建图表1
plt.title('Precision/Recall Curve')  # give plot a title
plt.xlabel('Recall')  # make axis labels
plt.ylabel('Precision')

# y_true和y_scores分别是gt label和predict score
# y_true = np.array([1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0])
# y_scores = np.array([0.9, 0.75, 0.86, 0.47, 0.55, 0.56, 0.74, 0.62,
#                      0.5, 0.86, 0.8, 0.47, 0.44, 0.67, 0.43, 0.4, 0.52, 0.4, 0.35, 0.1])
# precision, recall, thresholds = precision_recall_curve(y_true, y_scores)
x = np.array([0.0, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
y = np.array([1.0, 0.98, 0.96, 0.89, 0.86, 0.78, 0.73, 0.63, 0.58, 0.4])
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.figure(1)
plt.plot(x, y)
plt.show()
