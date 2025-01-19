# NFT Image Generator

這是一個使用 Flask 構建的簡單應用程式，用於上傳圖片並生成對應的 NFT metadata。

## 功能說明

- 上傳圖片文件
- 生成圖片的 NFT metadata，包括名稱、格式、尺寸和唯一的 Token ID
- 將生成的 metadata 顯示在網頁上

## 文件結構
nft-image-generator/
├── app.py                     # 主應用程式文件，包含 Flask 應用程式的配置和路由
├── config.py                  # 配置文件，包含上傳目錄和允許的圖片格式
├── resources/
│   └── nft_resource.py        # 處理圖片上傳和生成 NFT metadata 的資源文件
├── services/
│   └── image_service.py       # 處理圖片並生成 metadata 的服務文件
├── templates/
│   └── index.html             # 主頁面模板文件，包含上傳圖片的表單和顯示生成的 metadata
└── README.md                  # 說明文件