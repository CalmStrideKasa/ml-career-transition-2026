import numpy as np

X = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])

col_mean = X.mean(axis=0)

print("X:")
print(X)
print("shape of X:", X.shape)
print("column means:", col_mean)
print("shape of col_mean:", col_mean.shape)

result = X - col_mean
print("X - col_mean:")
print(result)