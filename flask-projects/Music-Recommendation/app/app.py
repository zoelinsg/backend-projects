from flask import Flask, render_template, request
from flask_restful import Api
from resources.music import MusicRecommendation
from dotenv import load_dotenv
import os

# 加載 .env 文件中的環境變數
load_dotenv()

app = Flask(__name__, template_folder='../templates', static_folder='../static')  # 設置模板和靜態文件夾位置
api = Api(app)

# 註冊 API 路由
api.add_resource(MusicRecommendation, '/api/recommend')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['GET'])
def recommend():
    genre = request.args.get('genre')
    recommendation = MusicRecommendation()
    result = recommendation.get()
    return render_template('recommend.html', genre=genre, recommendations=result['recommendations'])

if __name__ == '__main__':
    app.run(debug=True)