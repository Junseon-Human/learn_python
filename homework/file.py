import os


def update_entry(entry_text, date):
    if not os.path.exists("diarys"):
        os.makedirs("diarys")

    # date 만 때서 파일 이름을 만들기 위해서 date 만 따로 변수로 받아옴
    filename = f"diarys/{date}.txt"

    # 새 기분 및 일기내용 추출
    lines = entry_text.strip().split("\n")  # 문자열 양 끝의 공백과 개행 제거
    new_emotion_line = lines[0]  # 기분: ~
    new_content = "\n".join(lines[1:]).strip()
    # print(f"lines = {lines}")
    # print(f"new emotion line = {new_emotion_line}")
    # print(f"new content = {new_content}")

    if os.path.exists(filename):
        # 기존 내용 불러오기 (두 번째 줄부터 끝까지)
        with open(filename, "r", encoding="utf-8") as f:
            old_lines = f.readlines()
            # print(f"old_lines = {old_lines}")
        old_content = "".join(old_lines[1:]).strip()  # 기존 내용만
        # print(f"new old_lines = {old_content}")

        # 감정은 새로, 내용은 이어붙이기
        updated_text = f"{new_emotion_line}\n{old_content}\n{new_content}"
    else:
        # 새로 작성
        updated_text = entry_text

    with open(filename, "w", encoding="utf-8") as f:
        f.write(updated_text.strip() + "\n")
