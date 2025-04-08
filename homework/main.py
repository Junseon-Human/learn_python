from input import get_user_input
from diary import DiaryEntry
from file import update_entry
from read import list_diary_dates, read_diary
from emotion import get_emotion_stats


def main():
    while True:
        print("\n감정 일기장 📘")
        print("1. 일기 쓰기")
        print("2. 일기 보기")
        print("3. 감정 통계 보기")
        print("4. 종료")

        choice = input("번호를 선택해줘 > ")

        if choice == "1":
            date, emotion, content = get_user_input()
            entry = DiaryEntry(date, emotion, content)
            update_entry(entry.format_entry(), date)
            print("일기 저장 :)")
        elif choice == "2":
            view_old_entry()
        elif choice == "3":
            view_emotion_stats()
        elif choice == "4":
            print("안녕!")
            break
        else:
            print("잘못된 선택이야. 다시 입력해줘.")


def view_old_entry():
    dates = list_diary_dates()
    if not dates:
        print("저장된 일기가 없어요 😢")
        return

    print("저장된 일기 날짜들:")
    for d in dates:
        print(f"- {d}")

    selected = input("열어볼 날짜를 입력해주세요 (YYYY-MM-DD) > ")
    content = read_diary(selected)
    if content:
        print(f"\n📖 [{selected}]의 일기\n")

        lines = content.strip().split("\n")
        cleaned_lines = []
        first_line_done = False

        for line in lines:
            if line.startswith("[") and "기분:" in line and not first_line_done:
                # "[2025-04-07] 기분: 분노" → "기분: 분노"
                emotion = line.split("기분:")[-1].strip()
                cleaned_lines.append(f"기분: {emotion}\n")  # <-- 여기 줄바꿈 추가!
                first_line_done = True
            elif not line.startswith("["):
                cleaned_lines.append(line)

        print("\n".join(cleaned_lines))

    else:
        print("그 날짜의 일기를 찾을 수 없어요!")


def view_emotion_stats():
    stats = get_emotion_stats()
    if not stats:
        print(
            "감정 통계를 낼 수 없어요. 아직 일기가 없거나 감정 정보가 없을 수도 있어요 😢"
        )
        return

    print("\n🧠 감정 통계 📊")
    for emotion, count in stats.most_common():
        print(f"- {emotion}: {count}번")

    top_emotion = stats.most_common(1)[0][0]
    print(f"\n🎉 가장 자주 느낀 감정은 '{top_emotion}'입니다")


if __name__ == "__main__":
    main()
