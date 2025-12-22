from pathlib import Path
from data_loader import load_data, show_columns, select_xy_columns
from regression import linear_regression
from linearization import best_linearization
from fitting_models import fit_model, MODEL_FUNCTIONS
from visualize import plot_regression, plot_residuals, plot_model_fit


def choose_mode() -> int:
    print("\n請選擇分析方式：")
    print("1. 線性回歸 (Linear Regression)")
    print("2. 自動線性化 (Automatic Linearization)")
    print("3. 模型擬合 (Model Fitting)")
    mode = input("輸入選項 (1/2/3): ").strip()
    return int(mode)


def choose_model_name() -> str:
    print("\n可用模型：")
    for key, (_, desc) in MODEL_FUNCTIONS.items():
        print(f"- {key}: {desc}")
    model_name = input("請輸入模型名稱 (例如 hooke / exp_decay / power_law): ").strip()
    return model_name


def main():
    print("=== Physics Experiment Analyzer ===")
    file_path = input("請輸入資料檔案路徑 (例如 sample_data/example_decay.csv): ").strip()
    if not Path(file_path).exists():
        print("[ERROR] 檔案不存在，請確認路徑。")
        return
    df = load_data(file_path)
    show_columns(df)
    x_col = input("請輸入作為 x 的欄位名稱: ").strip()
    y_col = input("請輸入作為 y 的欄位名稱: ").strip()
    try:
        x, y = select_xy_columns(df, x_col, y_col)
    except Exception as e:
        print(f"[ERROR] 選擇欄位失敗: {e}")
        return
    try:
        mode = choose_mode()
    except ValueError:
        print("[ERROR] 請輸入 1, 2 或 3。")
        return
    if mode == 1:
        print("\n[模式] 線性回歸")
        slope, intercept, y_pred, residuals, r2 = linear_regression(x, y)
        print(f"slope (斜率) = {slope:.4f}")
        print(f"intercept (截距) = {intercept:.4f}")
        print(f"R^2 = {r2:.4f}")
        plot_regression(x, y, y_pred, title="Linear Regression", filename="linear_regression.png")
        plot_residuals(x, residuals, title="Linear Regression Residuals", filename="linear_residuals.png")
    elif mode == 2:
        print("\n[模式] 自動線性化")
        result = best_linearization(x, y)
        if result is None:
            print("[WARN] 沒有找到合適的線性化方式。")
            return
        desc, x_t, y_t, slope, intercept, y_pred, r2 = result
        print(f"最佳線性化方式: {desc}")
        print(f"slope = {slope:.4f}, intercept = {intercept:.4f}, R^2 = {r2:.4f}")
        plot_regression(x_t, y_t, y_pred, title=f"Linearized Regression ({desc})", filename="linearized_regression.png")
    elif mode == 3:
        print("\n[模式] 模型擬合 (curve_fit)")
        model_name = choose_model_name()
        try:
            params, y_fit, r2, cov = fit_model(model_name, x, y)
        except Exception as e:
            print(f"[ERROR] 模型擬合失敗: {e}")
            return
        print(f"擬合參數 (params) = {params}")
        print(f"R^2 = {r2:.4f}")
        plot_model_fit(x, y, y_fit, title=f"Model Fit: {model_name}", filename=f"model_fit_{model_name}.png")
    else:
        print("[ERROR] 不合法的選項。")
        return
    print("\n分析完成！請查看 PhysicsExperimentAnalyzer/results/ 資料夾中的輸出圖檔。")


if __name__ == "__main__":
    main()