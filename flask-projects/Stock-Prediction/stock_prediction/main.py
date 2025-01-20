from flask import Blueprint, render_template, jsonify, request
import yfinance as yf
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import os
from datetime import datetime, timedelta

# 使用 Agg 後端，避免啟動 GUI
plt.switch_backend('Agg')

# 建立 Blueprint
app = Blueprint('main', __name__)

@app.route('/')
def home():
    # 渲染首頁模板
    return render_template('index.html')

@app.route('/predict', methods=['GET'])
def predict_stock():
    # 獲取股票代號
    ticker = request.args.get('ticker')
    if not ticker:
        return jsonify({"error": "Please provide a stock ticker"}), 400

    # 獲取過去三個月的股票數據
    end_date = datetime.today()
    start_date = end_date - timedelta(days=90)
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    if stock_data.empty:
        return jsonify({"error": "Unable to fetch stock data"}), 404

    stock_data['Date'] = stock_data.index
    history_data = stock_data.to_dict(orient='records')

    # 當前值
    current_price = stock_data['Close'].iloc[-1]
    current_price = round(current_price, 2)  # 格式化為兩位小數

    # 建立模型並預測未來價格
    X = pd.to_numeric(stock_data['Date'].dt.strftime('%Y%m%d')).values.reshape(-1, 1)
    y = stock_data['Close'].values
    model = LinearRegression()
    model.fit(X, y)

    # 預測未來價格（預測未來一個月的價格）
    future_date = (datetime.today() + timedelta(days=30)).strftime('%Y%m%d')
    future_price = model.predict([[int(future_date)]])[0]
    future_price = round(float(future_price), 2)  # 格式化為兩位小數

    # 確保 static 目錄存在
    static_dir = os.path.join(app.root_path, 'static')
    if not os.path.exists(static_dir):
        os.makedirs(static_dir)

    # 生成圖表
    plt.figure(figsize=(10, 5))
    plt.plot(stock_data['Date'], stock_data['Close'], label='Close Price')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title(f'{ticker} Stock Data for the Last 3 Months')
    plt.legend()
    chart_filename = f'{ticker}_history.png'
    chart_path = os.path.join(static_dir, chart_filename)
    plt.savefig(chart_path)
    plt.close()

    # 渲染結果模板
    return render_template('index.html', history_data=history_data, chart_path=chart_filename, current_price=current_price, future_price=future_price, ticker=ticker)