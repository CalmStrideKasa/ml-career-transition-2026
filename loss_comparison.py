import numpy as np
import matplotlib.pyplot as plt

def compute_loss(y_true: np.ndarray, y_pred: np.ndarray, kind: str, delta: float = 1.0) -> np.ndarray:
    error = y_pred - y_true

    if kind == "mse":
        return error ** 2
    elif kind == "mae":
        return np.abs(error)
    elif kind == "huber":
        abs_error = np.abs(error)
        quadratic = 0.5 * error ** 2
        linear = delta * (abs_error - 0.5 * delta)
        return np.where(abs_error <= delta, quadratic, linear)
    else:
        raise ValueError(f"Unknown loss kind: {kind}")

y_true = np.array([10.0])
y_pred = np.array([12.0])

print("MSE:", compute_loss(y_true, y_pred, "mse"))
print("MAE:", compute_loss(y_true, y_pred, "mae"))
print("Huber (delta=1.0):", compute_loss(y_true, y_pred, "huber", delta=1.0))


errors = np.linspace(-5, 5, 200)
y_true_dummy = np.zeros_like(errors)
y_pred_dummy = errors

mse_vals = compute_loss(y_true_dummy, y_pred_dummy, "mse")
mae_vals = compute_loss(y_true_dummy, y_pred_dummy, "mae")
huber_vals = compute_loss(y_true_dummy, y_pred_dummy, "huber", delta=1.0)

plt.figure()
plt.plot(errors, mse_vals, label="MSE")
plt.plot(errors, mae_vals, label="MAE")
plt.plot(errors, huber_vals, label="Huber (delta=1.0)")
plt.xlabel("Error (y_pred - y_true)")
plt.ylabel("Loss")
plt.title("Loss Function Shapes")
plt.legend()
plt.savefig("loss_function_shapes.png")
plt.close()

np.random.seed(42)

N = 500
np.random.seed(42)

N = 500
true_w = 3.0
true_b = 5.0
x = np.random.normal(0, 2, size=N)
noise = np.random.normal(0, 1, size=N)
y = true_w * x + true_b + noise

n_outliers = 5
outlier_idx = np.random.choice(N, size=n_outliers, replace=False)
y[outlier_idx] += 100

print("Outlier y values:", y[outlier_idx])

def gradient_descent_with_loss(x, y, kind, lr=0.01, epochs=200, batch_size=32, delta=1.0):
    w, b = 0.0, 0.0
    n = len(x)

    for epoch in range(epochs):
        indices = np.random.permutation(n)

        for start in range(0, n, batch_size):
            batch_idx = indices[start:start + batch_size]
            x_batch = x[batch_idx]
            y_batch = y[batch_idx]

            y_pred = w * x_batch + b
            error = y_pred - y_batch
            m = len(batch_idx)

            if kind == "mse":
                grad_factor = 2 * error
            elif kind == "mae":
                grad_factor = np.sign(error)
            elif kind == "huber":
                grad_factor = np.where(np.abs(error) <= delta, error, delta * np.sign(error))
            else:
                raise ValueError(f"Unknown loss kind: {kind}")

            dw = (1 / m) * np.sum(grad_factor * x_batch)
            db = (1 / m) * np.sum(grad_factor)

            w -= lr * dw
            b -= lr * db

    return w, b


w_mse, b_mse = gradient_descent_with_loss(x, y, "mse", epochs=200)
w_mae, b_mae = gradient_descent_with_loss(x, y, "mae", epochs=200)
w_huber, b_huber = gradient_descent_with_loss(x, y, "huber", epochs=200, delta=1.0)

print(f"MSE:   w={w_mse:.3f}, b={b_mse:.3f}")
print(f"MAE:   w={w_mae:.3f}, b={b_mae:.3f}")
print(f"Huber: w={w_huber:.3f}, b={b_huber:.3f}")