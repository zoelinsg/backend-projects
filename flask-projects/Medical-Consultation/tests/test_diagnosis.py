import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from src.services.diagnosis import diagnose

def test_diagnose_cold_flu():
    """測試感冒或流感的診斷"""
    result = diagnose("發燒 咳嗽")
    assert result == "可能是感冒或流感"

def test_diagnose_measles():
    """測試麻疹的診斷"""
    result = diagnose("發燒 皮疹")
    assert result == "可能是麻疹"

def test_diagnose_migraine():
    """測試偏頭痛的診斷"""
    result = diagnose("頭痛 噁心")
    assert result == "可能是偏頭痛"

def test_diagnose_heart_disease():
    """測試心臟病的診斷"""
    result = diagnose("胸痛 呼吸急促")
    assert result == "可能是心臟病"

def test_diagnose_gastroenteritis():
    """測試腸胃炎的診斷"""
    result = diagnose("腹痛 腹瀉")
    assert result == "可能是腸胃炎"

def test_diagnose_tonsillitis():
    """測試扁桃腺炎的診斷"""
    result = diagnose("喉嚨痛 發燒")
    assert result == "可能是扁桃腺炎"

def test_diagnose_arthritis():
    """測試關節炎的診斷"""
    result = diagnose("關節痛 疲勞")
    assert result == "可能是關節炎"

def test_diagnose_otitis_media():
    """測試中耳炎的診斷"""
    result = diagnose("耳痛 聽力下降")
    assert result == "可能是中耳炎"

def test_diagnose_conjunctivitis():
    """測試結膜炎的診斷"""
    result = diagnose("眼睛紅 流淚")
    assert result == "可能是結膜炎"

def test_diagnose_allergy():
    """測試過敏的診斷"""
    result = diagnose("皮膚癢 紅疹")
    assert result == "可能是過敏"

def test_diagnose_unknown():
    """測試未知症狀的診斷"""
    result = diagnose("未知症狀")
    assert result == "需要更多資料進行診斷"