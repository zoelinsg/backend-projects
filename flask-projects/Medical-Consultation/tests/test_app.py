import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from flask import Flask
from src.app import app as flask_app

@pytest.fixture
def app():
    """建立並配置 Flask 測試客戶端"""
    flask_app.config.update({
        "TESTING": True,
    })
    yield flask_app

@pytest.fixture
def client(app):
    """建立測試客戶端"""
    return app.test_client()

def test_home_page(client):
    """測試首頁是否正確加載"""
    response = client.get("/")
    assert response.status_code == 200
    assert u"醫療問診" in response.data.decode('utf-8')

def test_health_check(client):
    """測試健康檢查 API"""
    response = client.post("/api/health/", data={"symptoms": "發燒 咳嗽"})
    assert response.status_code == 200
    assert u"可能是感冒或流感" in response.data.decode('utf-8')