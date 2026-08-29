from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import root_mean_squared_error, r2_score
import pandas as pd
from sklearn.preprocessing import StandardScaler

#dataset = fetch_california_housing()
#X = dataset.data
#y = dataset.target

df = pd.read_csv('data/housing.csv')

df['total_bedrooms'] = df['total_bedrooms'].fillna(df['total_bedrooms'].mean())
df = pd.get_dummies(df, columns=['ocean_proximity'])

X = df.drop(columns=['median_house_value'])
y = df['median_house_value']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
scaler.fit(X_train)
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)


def run_ridge(X_train, X_test, y_train, y_test, alpha):
    model = Ridge(alpha=alpha)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    model_RMSE = root_mean_squared_error(y_test, y_pred)
    model_R2 = r2_score(y_test, y_pred)

    print(f"Ridge(alpha={alpha}) RMSE = {model_RMSE}")
    print(f"Ridge(alpha={alpha}) R2   = {model_R2}")


def run_lasso(X_train, X_test, y_train, y_test, alpha):
    model = Lasso(alpha=alpha, max_iter=10000)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    model_RMSE = root_mean_squared_error(y_test, y_pred)
    model_R2 = r2_score(y_test, y_pred)

    print(f"Lasso(alpha={alpha}) RMSE = {model_RMSE}")
    print(f"Lasso(alpha={alpha}) R2   = {model_R2}")


alphas = [0.1, 1, 10]

for a in alphas:
    #run_ridge(X_train, X_test, y_train, y_test, a)
    #run_lasso(X_train, X_test, y_train, y_test, a)
    run_ridge(X_train_scaled, X_test_scaled, y_train, y_test, a)
    run_lasso(X_train_scaled, X_test_scaled, y_train, y_test, a)