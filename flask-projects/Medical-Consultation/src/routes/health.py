from flask import Blueprint, request, render_template
from src.services.diagnosis import diagnose  # 修改這行

bp = Blueprint("health", __name__, url_prefix="/api/health")

@bp.route("/", methods=["POST"])
def health_check():
    data = request.form  # 從表單接收資料
    symptoms = data.get("symptoms", "")
    diagnosis = diagnose(symptoms)
    return render_template("result.html", diagnosis=diagnosis)