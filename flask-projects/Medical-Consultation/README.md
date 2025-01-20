# 醫療問診系統

這是一個基於 Flask 的簡單醫療問診系統，允許用戶提交症狀並獲得診斷結果。

## 功能

- 提交症狀表單
- 根據症狀進行診斷
- 顯示診斷結果

## 安裝

1. 克隆此專案到本地：

    ```sh
    git clone https://github.com/yourusername/medical-consultation.git
    cd medical-consultation
    ```

2. 安裝依賴：

    ```sh
    poetry install
    ```

3. 進入虛擬環境：

    ```sh
    poetry shell
    ```

4. 設置環境變數：

    在 Windows 上：

    ```sh
    set FLASK_APP=src.app
    set FLASK_ENV=development
    ```

    在 macOS/Linux 上：

    ```sh
    export FLASK_APP=src.app
    export FLASK_ENV=development
    ```

5. 建立資料庫：

    ```sh
    python
    ```

    在 Python 互動式環境中，執行以下代碼來建立資料庫：

    ```python
    from src.models import Base
    from src.utils.database import engine

    Base.metadata.create_all(engine)
    ```

    然後退出 Python 互動式環境：

    ```python
    exit()
    ```

## 使用

1. 啟動 Flask 應用：

    ```sh
    flask run
    ```

2. 在瀏覽器中訪問 `http://127.0.0.1:5000` 來查看應用。

## 測試

1. 運行測試：

    ```sh
    pytest
    ```

## 文件結構

- [src](http://_vscodecontentref_/2) - 源代碼目錄
  - `app.py` - Flask 應用的入口
  - `routes/` - 路由定義
    - `health.py` - 健康檢查路由
  - `services/` - 業務邏輯
    - `diagnosis.py` - 診斷服務
  - `templates/` - HTML 模板
    - `base.html` - 基礎模板
    - `result.html` - 診斷結果頁面
    - `submit.html` - 症狀提交頁面
  - `utils/` - 工具
    - `database.py` - 資料庫連接管理
  - `models.py` - 資料庫模型
  - `config.py` - 配置文件
- [tests](http://_vscodecontentref_/3) - 測試文件
  - `test_app.py` - 應用測試
  - `test_diagnosis.py` - 診斷測試

## 貢獻

歡迎提交問題和請求，並且非常感謝您的貢獻！

## 授權

此專案使用 MIT 授權。