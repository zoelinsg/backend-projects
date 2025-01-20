def diagnose(symptoms):
    """根據症狀進行診斷"""
    symptoms = symptoms.lower()
    if "發燒" in symptoms and "咳嗽" in symptoms:
        return "可能是感冒或流感"
    elif "發燒" in symptoms and "皮疹" in symptoms:
        return "可能是麻疹"
    elif "頭痛" in symptoms and "噁心" in symptoms:
        return "可能是偏頭痛"
    elif "胸痛" in symptoms and "呼吸急促" in symptoms:
        return "可能是心臟病"
    elif "腹痛" in symptoms and "腹瀉" in symptoms:
        return "可能是腸胃炎"
    elif "喉嚨痛" in symptoms and "發燒" in symptoms:
        return "可能是扁桃腺炎"
    elif "關節痛" in symptoms and "疲勞" in symptoms:
        return "可能是關節炎"
    elif "耳痛" in symptoms and "聽力下降" in symptoms:
        return "可能是中耳炎"
    elif "眼睛紅" in symptoms and "流淚" in symptoms:
        return "可能是結膜炎"
    elif "皮膚癢" in symptoms and "紅疹" in symptoms:
        return "可能是過敏"
    else:
        return "需要更多資料進行診斷"