import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

N = 500
true_w = 3.0
true_b = 5.0
x = np.random.normal(0, 2, size=N)
noise = np.random.normal(0, 1, size=N)
y = true_w * x + true_b + noise

print("x shape:", x.shape)
print("y shape:", y.shape)
print("First 5 x, y:", x[:5], y[:5])

def gradient_descent_batch(x, y, lr=0.01, epochs=100):
    w, b = 0.0, 0.0
    n = len(x)
    losses = []

    for epoch in range(epochs):
        y_pred = w * x + b
        error = y_pred - y

        dw = (2 / n) * np.sum(error * x)
        db = (2 / n) * np.sum(error)

        w -= lr * dw
        b -= lr * db

        loss = np.mean(error ** 2)
        losses.append(loss)

    return w, b, losses

w_final, b_final, losses_batch = gradient_descent_batch(x, y, lr=0.01, epochs=100)
print(f"Batch GD: w={w_final:.3f}, b={b_final:.3f}")


def gradient_descent_sgd(x, y, lr=0.01, epochs=100):
    w, b = 0.0, 0.0
    n = len(x)
    losses = []

    for epoch in range(epochs):
        indices = np.random.permutation(n)
        epoch_loss = 0.0

        for i in indices:
            xi = x[i]
            yi = y[i]
            y_pred = w * xi + b
            error = y_pred - yi

            dw = 2 * error * xi
            db = 2 * error

            w -= lr * dw
            b -= lr * db

            epoch_loss += error ** 2

        losses.append(epoch_loss / n)

    return w, b, losses

w_sgd, b_sgd, losses_sgd = gradient_descent_sgd(x, y, lr=0.01, epochs=100)
print(f"SGD: w={w_sgd:.3f}, b={b_sgd:.3f}")


def gradient_descent_minibatch(x, y, lr=0.01, epochs=100, batch_size=32):
    w, b = 0.0, 0.0
    n = len(x)
    losses = []

    for epoch in range(epochs):
        indices = np.random.permutation(n)
        epoch_loss = 0.0

        for start in range(0, n, batch_size):
            batch_idx = indices[start:start + batch_size]
            x_batch = x[batch_idx]
            y_batch = y[batch_idx]

            y_pred = w * x_batch + b
            error = y_pred - y_batch

            dw = (2 / len(batch_idx)) * np.sum(error * x_batch)
            db = (2 / len(batch_idx)) * np.sum(error)

            w -= lr * dw
            b -= lr * db

            epoch_loss += np.sum(error ** 2)

        losses.append(epoch_loss / n)

    return w, b, losses


w_mb, b_mb, losses_mb = gradient_descent_minibatch(x, y, lr=0.01, epochs=100, batch_size=32)
print(f"Mini-batch: w={w_mb:.3f}, b={b_mb:.3f}")


w_batch2, b_batch2, _ = gradient_descent_batch(x, y, lr=0.01, epochs=1000)
print(f"Batch GD (1000 epochs): w={w_batch2:.3f}, b={b_batch2:.3f}")

plt.figure()
plt.plot(losses_batch, label="Batch GD")
plt.plot(losses_sgd, label="SGD")
plt.plot(losses_mb, label="Mini-batch")
plt.xlabel("Epoch")
plt.ylabel("Loss (MSE)")
plt.title("Loss Curve Comparison")
plt.legend()
plt.savefig("loss_curve_comparison.png")
plt.close()

def gradient_descent_sgd_detailed(x, y, lr=0.01, epochs=5):
    w, b = 0.0, 0.0
    n = len(x)
    per_step_losses = []

    for epoch in range(epochs):
        indices = np.random.permutation(n)

        for i in indices:
            xi = x[i]
            yi = y[i]
            y_pred = w * xi + b
            error = y_pred - yi

            dw = 2 * error * xi
            db = 2 * error

            w -= lr * dw
            b -= lr * db

            per_step_losses.append(error ** 2)

    return w, b, per_step_losses


_, _, per_step_losses = gradient_descent_sgd_detailed(x, y, lr=0.01, epochs=5)

plt.figure()
plt.plot(per_step_losses)
plt.xlabel("Step (1 data point per step)")
plt.ylabel("Loss")
plt.title("SGD Loss per Step (first 5 epochs)")
plt.savefig("sgd_per_step_loss.png")
plt.close()