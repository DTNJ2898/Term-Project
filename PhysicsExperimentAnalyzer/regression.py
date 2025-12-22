import numpy as np


def linear_regression(x, y): #使用最小平方法做線性回歸，回傳：slope, intercept, y_pred, residuals, r2
    x = np.array(x, dtype=float)
    y = np.array(y, dtype=float)
    if len(x) != len(y):
        raise ValueError("x 與 y 長度不一致。")
    n = len(x)
    if n < 2:
        raise ValueError("資料點太少，無法回歸。")
    slope, intercept = np.polyfit(x, y, 1)
    y_pred = slope * x + intercept
    residuals = y - y_pred
    ss_res = np.sum(residuals ** 2)
    ss_tot = np.sum((y - np.mean(y)) ** 2)
    r2 = 1 - ss_res / ss_tot if ss_tot != 0 else 0.0
    return slope, intercept, y_pred, residuals, r2


def compute_r2(y_true, y_pred): #給非線性 model 用的 R^2 計算。
    y_true = np.array(y_true, dtype=float)
    y_pred = np.array(y_pred, dtype=float)
    ss_res = np.sum((y_true - y_pred) ** 2)
    ss_tot = np.sum((y_true - np.mean(y_true)) ** 2)
    return 1 - ss_res / ss_tot if ss_tot != 0 else 0.0