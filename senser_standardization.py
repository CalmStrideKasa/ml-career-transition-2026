import numpy as np

np.random.seed(42)

X = np.random.normal(loc=25, scale=3, size=(1000,4))

def standardize_sensors(X: np.ndarray) -> np.ndarray:
    """Standardize each column of the input array to mean 0 and std 1.

    Args:
    ----
        X: Input array of shape (n_samples, n_features).

    Returns:
    -------
        Standardized array with the same shape as X.
    """
    col_mean = X.mean(axis=0)
    col_std = X.std(axis=0)
    X_std = (X-col_mean)/col_std

    return X_std

X_std = standardize_sensors(X)

print("mean after standardization:", X_std.mean(axis=0))
print("std after standardization:", X_std.std(axis=0))

print("shape:", X.shape)
print("first 3 rows:")
print(X[:3])