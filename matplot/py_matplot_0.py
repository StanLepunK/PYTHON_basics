import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
from mylinearregression import MyLinearRegression as MyLR
from matplotlib import pyplot
import matplotlib.pyplot as mpl


mpl.plot([1, 2, 4, 4, 2, 1], color = 'red', linestyle = 'dashed', linewidth = 2, markerfacecolor = 'blue', markersize = 5)
mpl.ylim(0, 5)
mpl.title('Un exemple')
mpl.show()


# data = pd.read_csv("are_blue_pills_magics.csv")
# Xpill = np.array(data["Micrograms"]).reshape(-1,1)
# # print(Xpill.shape)
# Yscore = np.array(data["Score"]).reshape(-1,1)

# linear_model1 = MyLR(np.array([[89.0], [-8]]))
# linear_model2 = MyLR(np.array([[89.0], [-6]]))
# Y_model1 = linear_model1.predict(Xpill)
# Y_model2 = linear_model2.predict(Xpill)

# print(linear_model1.mse(Xpill, Yscore))
# # 57.60304285714282
# print(mean_squared_error(Yscore, Y_model1))
# # 57.603042857142825
# print(linear_model2.mse(Xpill, Yscore))
# # 232.16344285714285
# print(mean_squared_error(Yscore, Y_model2))
# # 232.16344285714285