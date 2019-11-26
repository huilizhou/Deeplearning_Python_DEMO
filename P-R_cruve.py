# import matplotlib
# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.metrics import precision_recall_curve
# from sklearn.utils.fixes import signature
# plt.figure("P-R Curve")
# plt.title('Precision/Recall Curve')
# plt.xlabel('Recall')
# plt.ylabel('Precision')
# # y_true为样本实际的类别，y_scores为样本为正例的概率
# y_true = np.array([1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0])
# y_scores = np.array([0.9, 0.75, 0.86, 0.47, 0.55, 0.56, 0.74, 0.62,
#                      0.5, 0.86, 0.8, 0.47, 0.44, 0.67, 0.43, 0.4, 0.52, 0.4, 0.35, 0.1])
# precision, recall, thresholds = precision_recall_curve(y_true, y_scores)
# # print(precision)
# # print(recall)
# # print(thresholds)
# plt.plot(recall, precision)


import matplotlib
# matplotlib.use("Agg")
import numpy as np
import matplotlib.pyplot as plt
# from sklearn.metrics import precision_recall_curve
plt.figure(1)  # 创建图表1
plt.title('Precision/Recall Curve')  # give plot a title
plt.xlabel('Recall')  # make axis labels
plt.ylabel('Precision')

# y_true和y_scores分别是gt label和predict score
y_true = np.array([1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0])
y_scores = np.array([0.9, 0.75, 0.86, 0.47, 0.55, 0.56, 0.74, 0.62,
                     0.5, 0.86, 0.8, 0.47, 0.44, 0.67, 0.43, 0.4, 0.52, 0.4, 0.35, 0.1])
precision, recall, thresholds = precision_recall_curve(y_true, y_scores)
plt.figure(1)
plt.plot(precision, recall)
plt.show()
