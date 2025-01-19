from flask import Flask

# 工廠函式，用來建立 Flask 應用程式實例
def create_app():
    app = Flask(__name__)

    # 在這裡可以註冊路由或藍圖
    from .main import app as main_app
    app.register_blueprint(main_app)

    return app