import os


def list_diary_dates():
    try:
        files = os.listdir("diarys")
        dates = [f.replace(".txt", "") for f in files if f.endswith(".txt")]
        return sorted(dates)
    except FileNotFoundError:
        return []


def read_diary(date):
    filename = f"diarys/{date}.txt"
    if not os.path.exists(filename):
        return None
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()
