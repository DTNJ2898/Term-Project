# 主題：物理實驗資料分析與曲線擬合工具

# 程式的功能與技術原理
本程式提供一套完整的物理實驗資料分析功能，包含：
1. 資料讀取與前處理
    支援 CSV、TXT 檔案導入
    自動解析數據欄位
    去除空白行與不合法數據
2. 線性回歸
    計算斜率、截距、R²
    顯示殘差
    畫出散佈圖與最佳擬合線
3. 自動線性化
    支援常見物理模型的線性化：
        Exponential Decay
        Power-law
    程式可：
        自動判斷適合的轉換方式
        執行線性化後的回歸
        畫出線性化前後的比較圖
4. 非線性模型擬合
    使用 SciPy 擬合物理模型：
        Hooke’s Law
        Exponential Decay
        Power-law
5. 視覺化
    散佈圖
    線性回歸線
    模型擬合曲線
    線性化後數據圖
    殘差圖
    自動輸出 PNG 圖片
技術原理：
1. 最小平方法
2. 非線性模型擬合
3. 線性化
4. R² 與殘差
    殘差圖能幫助檢查模型是否適用

# 使用方式
1. 本工具需在Python環境下運作
2. 需先安裝以下套件
    numpy
    scipy
    matplotlib
    pandas
3. 執行 main.py
4. 輸入資料檔案路徑
5. 選擇要作為 x 與 y 的欄位名稱
6. 選擇分析模式
7. 查看結果與輸出

# 程式的架構
PhysicsExperimentAnalyzer/
├── main.py              # 主程式
├── data_loader.py       # 資料讀取與處理模組
├── regression.py        # 線性回歸與 R² 計算模組
├── linearization.py     # 自動線性化模組
├── fitting_models.py    # 物理模型擬合模組
├── visualize.py         # 視覺化繪圖模組
├── sample_data/
│   └── example.csv      # 內建數據範例
└── results/             # 圖片儲存資料夾

# 開發過程
1. 題目發想
    在物理與工程實驗課中，常需要進行資料回歸、線性化與模型參數推估，但手算或僅用 Excel 處理並不方便。因此，本專題希望開發一個專門為物理實驗設計的資料分析工具，能自動完成資料讀取、回歸分析、線性化與曲線擬合，並產生清楚的圖形結果。
2. 功能規劃
    初期規劃：
        讀取實驗資料
        進行線性回歸
        輸出圖表
    後續逐步擴充：
        加入自動線性化
        加入多種物理模型
        加入殘差分析與 R² 計算
        整合為互動式操作流程
3. 程式架構設計
    設計時採用模組化架構，將不同任務拆分成獨立檔案，提升可讀性與維護性：
        data_loader.py：資料讀取與前處理  
        regression.py：線性回歸與 R² 計算  
        linearization.py：自動線性化處理  
        fitting_models.py：非線性模型擬合 
        visualize.py：負責繪圖與輸出結果  
        main.py：整合所有功能並提供互動式操作
4. 開發流程
    1. 先完成資料讀取系統：確保能穩定讀取 CSV / TXT 並處理格式錯誤。
    2. 實作線性回歸與 R²：先完成最基本但最重要的分析功能。
    3. 加入自動線性化系統：設計多種常見轉換並自動比較 R²，挑選最佳方案。
    4. 實作 curve_fit 非線性擬合：支援不同物理模型並回傳參數及評估結果。
    5. 完善視覺化與輸出：圖片統一輸出，方便展示與檢查。
5. 遇到的問題與解決方式
    1. 資料不乾淨導致分析錯誤：加入資料檢查與例外處理機制  
    2. 指數模型擬合有時不收斂：增加初始猜測參數（p0）與 maxfev 次數  
    3. 線性化後資料量變少：增加篩選 mask 與例外處理避免崩潰  

# 參考資料來源、以及程式修改或增強的內容
1. 數值方法與演算法
    1. Least Squares Method — Wikipedia  
       https://en.wikipedia.org/wiki/Least_squares
    2. Exponential Decay & Linearization Concepts  
       https://en.wikipedia.org/wiki/Exponential_decay
    3. Nonlinear Least Squares — Levenberg–Marquardt Method  
       https://en.wikipedia.org/wiki/Levenberg%E2%80%93Marquardt_algorithm
2. Python 技術文件
    1. NumPy 函式庫 - STEAM 教育學習網
       https://steam.oxxostudio.tw/category/python/numpy/about-numpy.html
    2. 程式設計概論Programming 101 ─SciPy進行科學運算  
       https://www.cs.nccu.edu.tw/~sichiu/10902_ppt/10902_week_13_scipy.pdf
    3. SciPy 統計分析
       https://scipylectures.org/packages/statistics/index.html
    4. matplotlib 函式庫- matplotlib 教學( Python ) | STEAM 教育學習網
       https://steam.oxxostudio.tw/category/python/example/matplotlib.html
    5. 10分鐘的Pandas入門-繁中版
       https://hackmd.io/@wiimax/10-minutes-to-pandas