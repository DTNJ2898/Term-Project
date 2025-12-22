from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np


RESULT_DIR = Path("PhysicsExperimentAnalyzer/results")


def ensure_result_dir():
    RESULT_DIR.mkdir(exist_ok=True)


def plot_regression(x, y, y_pred, title="Linear Regression", filename="regression.png"):
    ensure_result_dir()
    plt.figure()
    plt.scatter(x, y, label="Data")
    plt.plot(x, y_pred, label="Fit", linewidth=2)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(title)
    plt.legend()
    save_path = RESULT_DIR / filename
    plt.savefig(save_path, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"[INFO] 已儲存圖檔：{save_path}")


def plot_residuals(x, residuals, title="Residuals", filename="residuals.png"):
    ensure_result_dir()
    plt.figure()
    plt.scatter(x, residuals)
    plt.axhline(0, linestyle="--")
    plt.xlabel("x")
    plt.ylabel("Residual")
    plt.title(title)
    save_path = RESULT_DIR / filename
    plt.savefig(save_path, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"[INFO] 已儲存圖檔：{save_path}")


def plot_model_fit(x, y, y_fit, title="Model Fit", filename="model_fit.png"):
    ensure_result_dir()
    x = np.array(x, float)
    y = np.array(y, float)
    y_fit = np.array(y_fit, float)
    order = np.argsort(x)
    x_sorted = x[order]
    y_fit_sorted = y_fit[order]
    plt.figure()
    plt.scatter(x, y, label="Data")
    plt.plot(x_sorted, y_fit_sorted, label="Model", linewidth=2)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(title)
    plt.legend()
    save_path = RESULT_DIR / filename
    plt.savefig(save_path, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"[INFO] 已儲存圖檔：{save_path}")