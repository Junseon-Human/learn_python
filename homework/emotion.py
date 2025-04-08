import os
from collections import Counter


def extract_emotions_from_diarys():
    emotion_list = []
    try:
        files = os.listdir("diarys")
        for file in files:
            if file.endswith(".txt"):
                with open(f"diarys/{file}", "r", encoding="utf-8") as f:
                    lines = f.readlines()
                    for line in lines:
                        if "기분:" in line:
                            # "기분: 행복" → "행복" 추출
                            emotion = line.strip().split("기분:")[-1].strip()
                            if emotion:
                                emotion_list.append(emotion)
        return emotion_list
    except FileNotFoundError:
        return []


def get_emotion_stats():
    emotions = extract_emotions_from_diarys()
    if not emotions:
        return None
    counter = Counter(emotions)
    return counter
