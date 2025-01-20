from flask import Flask, render_template
from flask_restful import Api
import os
from resources.nft_resource import NFTResource
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)

# 註冊資源
api.add_resource(NFTResource, '/generate')

# 首頁
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # 確保上傳目錄存在
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    # 啟動 Flask 應用程式
    app.run(debug=True)