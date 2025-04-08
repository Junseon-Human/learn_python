import os
from datetime import datetime


def get_user_input():
    # 1. 날짜 입력
    while True:
        date_input = input(
            "일기 날짜를 입력해주세요 (기본: 오늘) [YYYY-MM-DD] > "
        ).strip()
        if not date_input:
            date = datetime.today().strftime("%Y-%m-%d")
            break
        try:
            date = datetime.strptime(date_input, "%Y-%m-%d").strftime("%Y-%m-%d")
            break
        except ValueError:
            print("날짜 형식이 올바르지 않아요! 예: 2025-04-08")

    filename = f"diarys/{date}.txt"

    # 2. 기존 내용 보여주기
    if os.path.exists(filename):
        print(f"\n📖 {date}의 기존 일기 내용:")
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()
            emotion_line = lines[0].strip() if lines else ""
            content = "".join(lines[1:]).strip()
            print(f"{emotion_line}\n{content}")
        print("\n--- 이어서 작성해주세요 ---")

    # 3. 감정 선택
    emotions = ["행복", "슬픔", "분노", "불안", "피곤", "설렘", "짜증", "감사"]
    print("지금 기분을 선택해주세요:")
    for idx, emo in enumerate(emotions, start=1):
        print(f"{idx}. {emo}")

    while True:
        try:
            choice = int(input("번호 입력 > "))
            if 1 <= choice <= len(emotions):
                emotion = emotions[choice - 1]
                break
            else:
                print("범위 안의 숫자를 입력해주세요!")
        except ValueError:
            print("숫자를 입력해주세요!.")

    # 4. 새 내용 입력
    content = input("오늘의 일기 > ")

    return date, emotion, content
