# nft-api/config.py
# 配置檔案，包含上傳目錄、允許的圖片格式
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

class Config:
    UPLOAD_FOLDER = UPLOAD_FOLDER
    ALLOWED_EXTENSIONS = ALLOWED_EXTENSIONS