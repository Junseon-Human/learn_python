import streamlit as st
from diary import DiaryEntry
from file import update_entry
from read import list_diary_dates, read_diary
from emotion import get_emotion_stats
from datetime import datetime

# 페이지 설정
st.set_page_config(page_title="감정 일기장", layout="centered")

st.title("📘 감정 일기장")

menu = st.sidebar.selectbox("메뉴 선택", ["일기 쓰기", "일기 보기", "감정 통계"])

if menu == "일기 쓰기":
    st.subheader("✍️ 오늘의 일기 작성")
    date = st.date_input("날짜 선택", value=datetime.today())
    str_date = date.strftime("%Y-%m-%d")

    emotion = st.selectbox(
        "오늘의 기분", ["행복", "슬픔", "분노", "불안", "피곤", "설렘", "짜증", "감사"]
    )
    content = st.text_area("일기 내용")

    if st.button("저장하기"):
        entry = DiaryEntry(str_date, emotion, content)
        update_entry(entry.format_entry(), str_date)
        st.success("일기가 저장되었어요 😊")

elif menu == "일기 보기":
    st.subheader("📖 지난 일기 보기")
    dates = list_diary_dates()
    if dates:
        selected_date = st.selectbox("날짜 선택", dates)
        diary = read_diary(selected_date)
        if diary:
            # 중복된 기분 출력 방지 처리
            lines = diary.strip().split("\n")
            cleaned_lines = []
            first_line_done = False
            for line in lines:
                if line.startswith("[") and "기분:" in line and not first_line_done:
                    emotion = line.split("기분:")[-1].strip()
                    cleaned_lines.append(f"기분: {emotion}\n")
                    first_line_done = True
                elif not line.startswith("["):
                    cleaned_lines.append(line)

            st.text(f"[{selected_date}]의 일기\n\n" + "\n".join(cleaned_lines))
    else:
        st.info("저장된 일기가 없어요 😢")

elif menu == "감정 통계":
    st.subheader("📊 감정 통계 보기")
    stats = get_emotion_stats()
    if stats:
        st.bar_chart(dict(stats))
        top = stats.most_common(1)[0][0]
        st.markdown(f"🎉 가장 자주 느낀 감정은 **{top}**입니다")
    else:
        st.warning("아직 일기가 없어서 통계를 볼 수 없어요")
