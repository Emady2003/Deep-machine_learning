import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def gradient_descent_visualization(
    x_train,
    true_w=2,
    n_epochs=100,
    random_state=1,
    learning_rate=2,
    grandient_step=True,
    plot_range=1,
):
    """
    Visualize gradient descent optimization for linear regression.

    Parameters:
    x_train (array-like): Training data (should be 1D or 2D array)
    random_state (int): Random seed for reproducibility
    learning_rate (float): Learning rate for gradient descent

    Returns:
    dict: Dictionary containing final parameters, loss history, and parameter history
    """

    # Convert to numpy array and ensure proper shape
    x = (
        np.array(x_train).reshape(-1, 1)
        if len(np.array(x_train).shape) == 1
        else np.array(x_train)
    )
    N = len(x)

    # Generate true parameters and target values
    true_b = 1
    true_w = true_w
    np.random.seed(42)  # Fixed seed for consistent data generation
    e = np.random.randn(N, 1) * 0.2
    y = true_b + true_w * x + e

    # Initialize parameters
    np.random.seed(random_state)
    b = np.random.randn(1)
    w = np.random.randn(1)

    # Gradient descent parameters
    lr = learning_rate

    # Store history for plotting
    w_history = [w[0]]
    b_history = [b[0]]
    loss_history = []

    # Calculate initial loss
    y_pred = b + w * x
    error = y_pred - y
    loss = 0.5 * (error**2).mean()
    loss_history.append(loss)

    print(f"Initial: loss = {loss:.4f}, b = {b[0]:.4f}, w = {w[0]:.4f}")

    # Create grid for 3D plot
    b_range = np.linspace(min(-1, b[0] - plot_range), max(3, b[0] + plot_range), 30)
    w_range = np.linspace(min(-1, w[0] - plot_range), max(5, w[0] + plot_range), 30)
    B, W = np.meshgrid(b_range, w_range)

    # Calculate loss for each (b,w) pair
    Z = np.zeros_like(B)
    for i in range(len(b_range)):
        for j in range(len(w_range)):
            y_pred_grid = B[j, i] + W[j, i] * x
            error_grid = y_pred_grid - y
            Z[j, i] = 0.5 * (error_grid**2).mean()

    # Perform gradient descent and store steps
    steps_to_show = []
    for epoch in range(n_epochs):
        # Calculate gradients
        y_pred = b + w * x
        error = y_pred - y
        w_grad = (error * x).mean()
        b_grad = error.mean()

        # Update parameters
        w = w - lr * w_grad
        b = b - lr * b_grad

        # Calculate new loss
        y_pred = b + w * x
        error = y_pred - y
        loss = 0.5 * (error**2).mean()

        # Store history
        w_history.append(w[0])
        b_history.append(b[0])
        loss_history.append(loss)

        # Store specific steps for visualization
        if epoch + 1 in [3, 10, 100]:
            steps_to_show.append(
                {
                    "epoch": epoch + 1,
                    "w": w[0],
                    "b": b[0],
                    "loss": loss,
                    "y_pred": y_pred.copy(),
                    "w_grad": w_grad,
                    "b_grad": b_grad,
                }
            )

        if (epoch + 1) % 20 == 0:
            print(f"Epoch {epoch+1}: loss = {loss:.4f}, b = {b[0]:.4f}, w = {w[0]:.4f}")

    print(f"Final: loss = {loss:.4f}, b = {b[0]:.4f}, w = {w[0]:.4f}")
    print(f"True parameters: b = {true_b}, w = {true_w}")

    # Create figure with subplots
    fig = plt.figure(figsize=(20, 8))

    # 3D plot
    ax1 = fig.add_subplot(111, projection="3d")

    # Plot the loss surface
    surf = ax1.plot_surface(W, B, Z, cmap="viridis", alpha=0.6)
    if grandient_step:
        # Plot trajectory
        ax1.plot(
            w_history,
            b_history,
            loss_history,
            "ro-",
            markersize=4,
            linewidth=1,
            alpha=0.7,
            label="GD trajectory",
        )

        # Plot initial point
        ax1.scatter(
            w_history[0],
            b_history[0],
            loss_history[0],
            color="red",
            s=100,
            label="Start",
        )

        # Plot steps
        colors = ["orange", "purple", "cyan"]
        for i, step in enumerate(steps_to_show):
            ax1.scatter(
                step["w"],
                step["b"],
                step["loss"],
                color=colors[i],
                s=100,
                label=f'Step {step["epoch"]}',
            )

        # Plot final point
        ax1.scatter(
            w_history[-1],
            b_history[-1],
            loss_history[-1],
            color="green",
            s=100,
            label="Final",
        )

    # Add labels and title
    ax1.set_xlabel("Weight (w)")
    ax1.set_ylabel("Bias (b)")
    ax1.set_zlabel("Loss")
    ax1.set_title(
        f"3D Loss Function with Gradient Descent Steps\n(Learning Rate = {learning_rate})"
    )
    ax1.legend()

    plt.tight_layout()
    plt.show()

    # Plot loss curve
    plt.figure(figsize=(10, 6))
    plt.plot(range(len(loss_history)), loss_history, "b-", linewidth=2)
    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.title(f"Loss vs Epoch (Learning Rate = {learning_rate})")
    plt.grid(True, alpha=0.3)
    plt.show()

    # Print summary
    print("\n=== SUMMARY ===")
    print(f"True parameters: w = {true_w}, b = {true_b}")
    print(f"Final parameters: w = {w_history[-1]:.4f}, b = {b_history[-1]:.4f}")
    print(f"Final loss: {loss_history[-1]:.6f}")
    print(f"Learning rate: {learning_rate}")
    print(f"Random state: {random_state}")

    # Return results
    return {
        "final_w": w_history[-1],
        "final_b": b_history[-1],
        "final_loss": loss_history[-1],
        "w_history": w_history,
        "b_history": b_history,
        "loss_history": loss_history,
        "true_w": true_w,
        "true_b": true_b,
        "x_data": x,
        "y_data": y,
    }
