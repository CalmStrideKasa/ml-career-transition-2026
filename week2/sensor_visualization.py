import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)
X = np.random.normal(loc=25, scale=3, size=(1000, 4))
df = pd.DataFrame(X, columns=["temperature", "humidity", "pressure", "vibration"])
df["sensor_id"] = np.random.choice([1, 2, 3, 4, 5], size=1000)

plt.figure()
plt.hist(df["temperature"], bins=30)
plt.xlabel("Temperature")
plt.ylabel("Frequency")
plt.title("Temperature Distribution")
plt.savefig("temperature_histogram.png")
plt.close()

plt.figure()
colors = df["sensor_id"]
plt.scatter(df["temperature"], df["pressure"], c=colors, cmap="viridis")
plt.xlabel("Temperature")
plt.ylabel("Pressure")
plt.title("Temperature vs Pressure (colored by sensor_id)")
plt.colorbar(label="Sensor ID")
plt.savefig("temp_vs_pressure_scatter.png")
plt.close()

import plotly.express as px

fig_hist = px.histogram(df, x="temperature", nbins=30, title="Temperature Distribution (Interactive)")
fig_hist.write_html("temperature_histogram_interactive.html")

fig_scatter = px.scatter(
    df, x="temperature", y="pressure", color="sensor_id",
    title="Temperature vs Pressure (Interactive)"
)
fig_scatter.write_html("temp_vs_pressure_scatter_interactive.html")