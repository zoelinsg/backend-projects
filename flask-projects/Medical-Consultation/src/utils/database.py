# 檔案名稱: src/utils/database.py
# 用途: 資料庫連線管理工具

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from config import DATABASE_URI

# 建立資料庫引擎
engine = create_engine(DATABASE_URI, echo=True)

# 配置 Session
SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

def get_db():
    """依需求取得資料庫 Session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()