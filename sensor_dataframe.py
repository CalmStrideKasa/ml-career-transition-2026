import numpy as np
import pandas as pd
from ydata_profiling import ProfileReport


np.random.seed(42)

X = np.random.normal(loc=25, scale=3, size=(1000, 4))

df = pd.DataFrame(X, columns=["temperature", "humidity", "pressure", "vibration"])

df["sensor_id"] = np.random.choice([1, 2, 3, 4, 5], size=1000)
sensor_means = df.groupby("sensor_id").mean()

print(sensor_means)
print(df.head())
print(df.shape)

np.random.seed(0)
missing_mask = np.random.random(df.shape) < 0.05
df_missing = df.mask(missing_mask)

print("Missing values per column:")
print(df_missing.isnull().sum())

#df_ffill = df_missing.fillna(method="ffill")
df_ffill = df_missing.ffill()
print("After ffill:")
print(df_ffill.isnull().sum())

df_mean = df_missing.fillna(df_missing.mean())
print("After mean fill:")
print(df_mean.isnull().sum())

high_temp = df[df["temperature"] > 28]
print("High temperature rows:", high_temp.shape[0])
print(high_temp.head())

profile = ProfileReport(df, title="Sensor Data Profiling Report")
profile.to_file("sensor_profile_report.html")