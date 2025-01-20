import os
from PIL import Image
import json
import uuid

def process_image(image_path):
    """
    處理圖片並生成 metadata
    :param image_path: 圖片路徑
    :return: metadata 字典
    """
    image = Image.open(image_path)  # 開啟圖片

    # 生成唯一的 Token ID
    token_id = str(uuid.uuid4())

    # 生成 metadata
    metadata = {
        "token_id": token_id,
        "name": os.path.basename(image_path),
        "format": image.format,
        "size": image.size
    }

    # 儲存 metadata.json
    metadata_path = f"{os.path.splitext(image_path)[0]}_metadata.json"  # 生成 metadata.json 路徑
    with open(metadata_path, 'w') as f:  # 開啟文件
        json.dump(metadata, f, ensure_ascii=False, indent=4)  # 寫入 metadata，使用縮排美化格式

    return metadata  # 返回 metadata