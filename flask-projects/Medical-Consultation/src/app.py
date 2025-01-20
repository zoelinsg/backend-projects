from flask import Flask, render_template
from src.routes import health  # 修改這行

app = Flask(__name__)
app.register_blueprint(health.bp)

@app.route("/")
def home():
    return render_template("submit.html")