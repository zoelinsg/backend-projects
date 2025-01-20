from stock_prediction import create_app

# 建立 Flask 應用程式實例
app = create_app()

if __name__ == "__main__":
    # 啟動應用程式
    app.run(debug=True)