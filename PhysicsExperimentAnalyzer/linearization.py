import numpy as np
from typing import Dict, Callable, Tuple, List
from regression import linear_regression


def transform_ln_y(x, y):
    mask = y > 0
    return x[mask], np.log(y[mask]), "ln(y)", mask


def transform_log10_y(x, y):
    mask = y > 0
    return x[mask], np.log10(y[mask]), "log10(y)", mask


def transform_inv_x(x, y):
    mask = x != 0
    return 1 / x[mask], y[mask], "1/x", mask


def transform_inv_x2(x, y):
    mask = x != 0
    return 1 / (x[mask] ** 2), y[mask], "1/x^2", mask


TRANSFORMS: Dict[str, Callable] = {
    "ln_y": transform_ln_y,
    "log10_y": transform_log10_y,
    "inv_x": transform_inv_x,
    "inv_x2": transform_inv_x2,
}


def try_all_linearizations(x, y) -> List[Tuple[str, float]]: #嘗試所有線性化方式，回傳 [(描述, R^2), ...]
    results = []
    for name, func in TRANSFORMS.items():
        try:
            x_t, y_t, desc, mask = func(np.array(x, float), np.array(y, float))
            if len(x_t) < 2:
                continue
            _, _, _, _, r2 = linear_regression(x_t, y_t)
            results.append((desc, r2))
        except Exception:
            continue
    return results


def best_linearization(x, y): #回傳最佳線性化方式：(best_desc, x_transformed, y_transformed, slope, intercept, y_pred, r2) 如果完全失敗，回傳 None。
    best = None
    best_r2 = -1
    best_data = None
    for name, func in TRANSFORMS.items():
        try:
            x_t, y_t, desc, mask = func(np.array(x, float), np.array(y, float))
            if len(x_t) < 2:
                continue
            slope, intercept, y_pred, residuals, r2 = linear_regression(x_t, y_t)
            if r2 > best_r2:
                best_r2 = r2
                best = desc
                best_data = (x_t, y_t, slope, intercept, y_pred, r2)
        except Exception:
            continue
    if best is None:
        return None
    x_t, y_t, slope, intercept, y_pred, r2 = best_data
    return best, x_t, y_t, slope, intercept, y_pred, r2