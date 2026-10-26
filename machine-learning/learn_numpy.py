import numpy as np

y_true = np.array([1,0,1])
y_pred = np.array([1,0,1])

MSE = np.mean((y_true - y_pred) ** 2)

print(MSE)