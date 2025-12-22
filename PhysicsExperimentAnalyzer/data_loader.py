import pandas as pd


def load_data(file_path: str) -> pd.DataFrame: #從 CSV 或 TXT 檔案讀取資料，回傳 pandas DataFrame
    try:
        df = pd.read_csv(file_path) # 預設當成 CSV 讀，如果有需要可以再加其他 delimiter 選項
        if df.empty:
            raise ValueError("讀到的資料是空的，請檢查檔案內容。")
        return df
    except Exception as e:
        print(f"[ERROR] 讀取資料時發生錯誤: {e}")
        raise


def show_columns(df: pd.DataFrame) -> None: #顯示 DataFrame 的欄位名稱，讓使用者選 x / y
    print("\n資料欄位如下：")
    for i, col in enumerate(df.columns):
        print(f"  {i}: {col}")


def select_xy_columns(df: pd.DataFrame, x_col: str, y_col: str): #從 DataFrame 中選出 x, y 欄位並轉成數值陣列
    if x_col not in df.columns or y_col not in df.columns:
        raise KeyError("指定的 x 或 y 欄位不存在。")
    x = df[x_col].values
    y = df[y_col].values
    return x, y