from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import root_mean_squared_error, r2_score


dataset = fetch_california_housing()
X = dataset.data
y = dataset.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model1_LinearRegression = LinearRegression()
model1_LinearRegression.fit(X_train, y_train)
y_pred = model1_LinearRegression.predict(X_test)

model1_RMSE = root_mean_squared_error(y_test, y_pred)
model1_R2 = r2_score(y_test, y_pred)

print(f"model1 RMSE = {model1_RMSE}")
print(f"model1 R2 = {model1_R2}")