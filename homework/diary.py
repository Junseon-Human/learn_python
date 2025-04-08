class DiaryEntry:
    def __init__(self, date, emotion, content):
        self.date = date
        self.emotion = emotion
        self.content = content

    def format_entry(self):
        return f"[{self.date}] 기분: {self.emotion}\n{self.content}\n"
