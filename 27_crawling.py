# 사용하는 크롬의 버전에따라 크롬 드라이버 최신화 및 버전 일치 필요함
# pip install selenium
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from openpyxl import *

link = "https://news.naver.com/breakingnews/section/105/229?date="
date = "20250417"

main_link = link + date
Main_link = pd.DataFrame({"number": [], "title": [], "link": []})

service = Service("etc/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get(main_link)
time.sleep(3)

more_button = driver.find_element(
    By.CLASS_NAME, "section_more_inner._CONTENT_LIST_LOAD_MORE_BUTTON"
)

while True:
    try:
        more_button.click()
        time.sleep(3)
    except:
        break

articles = driver.find_elements(By.CLASS_NAME, "sa_text_title._NLOG_IMPRESSION")
for i in range(len(articles)):
    title = articles[i].text.strip()
    link = articles[i].get_attribute("href")
    li = [i + 1, title, link]
    Main_link.loc[i] = li


excel_name = "news_" + date + ".xlsx"
with pd.ExcelWriter(excel_name) as writer:
    Main_link.to_excel(writer, sheet_name="링크", index=False)
