import os

DATABASE_URI = os.getenv("DATABASE_URI", "sqlite:///medical.db")
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key")