from flask_restful import Resource
from flask import request, jsonify
from werkzeug.utils import secure_filename
import os
from services.image_service import process_image
from config import Config

class NFTResource(Resource):
    def post(self):
        """
        接收圖片並生成 NFT metadata
        :return: JSON 格式的消息和 metadata
        """
        if 'image' not in request.files:
            return jsonify({"message": "No file part"}), 400  # 檢查請求中是否包含文件
        file = request.files['image']
        if file.filename == '':
            return jsonify({"message": "No selected file"}), 400  # 檢查是否選擇了文件
        if file and self.allowed_file(file.filename):
            filename = secure_filename(file.filename)  # 確保文件名安全
            file_path = os.path.join(Config.UPLOAD_FOLDER, filename)  # 生成文件保存路徑
            file.save(file_path)  # 保存文件
            metadata = process_image(file_path)  # 處理圖片並生成 metadata
            return jsonify({"message": "NFT generated", "metadata": metadata})  # 返回生成的 metadata
        else:
            return jsonify({"message": "File type not allowed"}), 400  # 文件類型不允許

    def allowed_file(self, filename):
        """
        檢查文件是否為允許的格式
        :param filename: 文件名
        :return: 是否允許的布林值
        """
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_EXTENSIONS