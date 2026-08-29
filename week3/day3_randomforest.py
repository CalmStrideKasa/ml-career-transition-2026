from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import root_mean_squared_error, r2_score
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import learning_curve
import numpy as np
import matplotlib.pyplot as plt

#dataset = fetch_california_housing()
#X = dataset.data
#y = dataset.target

#csv reader
df = pd.read_csv('data/housing.csv')

# postprocess
df['total_bedrooms'] = df['total_bedrooms'].fillna(df['total_bedrooms'].mean())
df = pd.get_dummies(df, columns=['ocean_proximity'])

#define x and y
X = df.drop(columns=['median_house_value'])
y = df['median_house_value']

# division 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# standardization
scaler = StandardScaler()
scaler.fit(X_train)
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)


train_sizes, train_scores, test_scores = learning_curve(
    estimator=RandomForestRegressor(n_estimators=100, random_state=42),
    X=X_train_scaled,
    y=y_train,
    cv=5,
    scoring='neg_mean_squared_error',
    train_sizes=np.linspace(0.1, 1.0, 5)
)
train_rmse = np.sqrt(-train_scores).mean(axis=1)
test_rmse = np.sqrt(-test_scores).mean(axis=1)
print(train_sizes)
print(train_rmse)
print(test_rmse)

"""
#randomforest
def run_randomforest(X_train, X_test, y_train, y_test, n):
    model = RandomForestRegressor(n_estimators=n,random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    model_RMSE = root_mean_squared_error(y_test, y_pred)
    model_R2 = r2_score(y_test, y_pred)

    print(f"RandomForest(n={n}) RMSE = {model_RMSE}")
    print(f"RandomForest(n={n}) R2   = {model_R2}")

n = [1, 10, 100]

for i in n:
    #run_RandomForest(X_train, X_test, y_train, y_test, a)
    #run_lasso(X_train, X_test, y_train, y_test, a)
    run_randomforest(X_train, X_test, y_train, y_test,i)
"""

plt.plot(train_sizes, train_rmse, label='Train RMSE')
plt.plot(train_sizes, test_rmse, label='Test RMSE')
plt.xlabel('size')
plt.ylabel('rmse')
plt.title('result')
plt.legend()
plt.savefig('randomforest_learning_curve.png')