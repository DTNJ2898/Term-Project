import numpy as np
from typing import Tuple
from scipy.optimize import curve_fit
from regression import compute_r2


#各種物理模型

def hooke_law(x, k):
    return k * x


def exp_decay(x, A, b):
    return A * np.exp(-b * x)


def power_law(x, A, n):
    return A * (x ** n)


#模型名稱對應表
MODEL_FUNCTIONS = {
    "hooke": (hooke_law, "Hooke's Law: y = kx"),
    "exp_decay": (exp_decay, "Exponential Decay: y = A e^(-b x)"),
    "power_law": (power_law, "Power-law: y = A x^n"),
}


def fit_model(model_name: str, x, y) -> Tuple[np.ndarray, np.ndarray, float, np.ndarray]: #使用指定模型進行 curve_fit，回傳：params, y_fit, r2, params_cov
    if model_name not in MODEL_FUNCTIONS:
        raise ValueError(f"未知的模型名稱: {model_name}")
    func, _ = MODEL_FUNCTIONS[model_name]
    x = np.array(x, dtype=float)
    y = np.array(y, dtype=float)
    if model_name == "hooke":
        p0 = [1.0]
    elif model_name == "exp_decay":
        p0 = [max(y), 1.0]
    elif model_name == "power_law":
        p0 = [1.0, 1.0]
    else:
        p0 = None
    params, cov = curve_fit(func, x, y, p0=p0, maxfev=10000)
    y_fit = func(x, *params)
    r2 = compute_r2(y, y_fit)
    return params, y_fit, r2, cov